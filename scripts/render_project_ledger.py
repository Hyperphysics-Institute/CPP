#!/usr/bin/env python3
"""
render_project_ledger.py — render a project-grouped per-patch ledger FROM git history.

The git history IS the canonical per-patch ledger: every patch is one commit (every window
pushes to the same main), append-only and collision-free by construction. This script renders
that history into a human-readable, project-grouped view (project_ledger.md) so a window booting
on any track can see — in one location — every patch on that track, in order, across all windows,
and the last patch worked.

Track assignment, in priority order:
  1. an explicit `Track: <NAME>` trailer line in the commit body (authoritative);
  2. else inferred from the paths the commit touched, via TRACK_MAP below;
  3. else 'UNTAGGED'.

Usage:  python3 scripts/render_project_ledger.py [--out project_ledger.md] [--max N]
This script is READ-ONLY on git; it never edits history. Re-run any time to refresh the view.
"""
import subprocess, sys, re, argparse, datetime

# path-prefix -> track  (first match wins; order matters, most-specific first)
TRACK_MAP = [
    ("series_relativity/development/mu_eps_closure",            "R2 (impedance falsifier / SR-9 EM-emergence)"),
    ("series_relativity/development/velocity_ssv_time_dilation","R2 (impedance falsifier / SR-9 EM-emergence)"),
    ("series_relativity/op_einstein_closure",                  "op:einstein / SR-2 (spin-2 graviton)"),
    ("series_phenomena/cosmology/dark_matter",                 "DM / OPEN-COSMO-DM-2"),
    ("series_phenomena/cosmology/sea_gravitation",             "DM-2 (Sea-gravitation)"),
    ("series_phenomena/cosmology/early_universe",              "EU-1 / early universe"),
    ("series_umbrella/series_cosmological_constant_arc",       "CC umbrella (cosmological constant)"),
    ("series_umbrella/series_substrate_chirality_arc",         "Chirality arc"),
    ("series_foundations/dynamical_substrate_law",             "DSL / F.1"),
    ("series_relativity/papers",                               "SR papers"),
    ("series_standard_model",                                  "Standard-Model series"),
    ("series_electroweak",                                     "Electroweak / SF-2"),
    ("series_strong",                                          "Strong sector / SF-5"),
    ("flagship_papers",                                        "Flagship papers"),
    ("book_project",                                           "Book (TATWD)"),
    ("frontier_sectors",                                       "WORKFLOW / frontier"),
    ("templates",                                              "WORKFLOW / protocol"),
    ("handovers",                                              "WORKFLOW / handover"),
    ("parallel_dev",                                           "WORKFLOW / multi-window"),
    ("scripts",                                                "WORKFLOW / tooling"),
]
ROOT_GOVERNANCE = {"todolist.md","operating_system.md","research_frontier.md","theorem-registry.md",
                   "predictions.md","master_glossary.md","paper_catalog.md","founders_vision.md","INDEX.md","README.md"}

def sh(args):
    return subprocess.run(args, cwd=".", capture_output=True, text=True, check=True).stdout

def infer_track(paths, trailer):
    if trailer:
        return trailer
    for p in paths:
        for prefix, track in TRACK_MAP:
            if p.startswith(prefix):
                return track
    for p in paths:
        if p in ROOT_GOVERNANCE:
            return "WORKFLOW / governance"
    return "UNTAGGED"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="project_ledger.md")
    ap.add_argument("--max", type=int, default=400)
    args = ap.parse_args()

    # %H hash | %ad date | %s subject | %b body  — records split on \x1e, fields on \x1f
    fmt = "%x1e%H%x1f%ad%x1f%s%x1f%b"
    raw = sh(["git","log",f"-{args.max}","--date=short",f"--pretty=format:{fmt}","--name-only"])
    records = [r for r in raw.split("\x1e") if r.strip()]

    rows = []
    for rec in records:
        head, _, files_blob = rec.partition("\n")
        parts = head.split("\x1f")
        if len(parts) < 3:
            continue
        h, date, subject = parts[0], parts[1], parts[2]
        body = parts[3] if len(parts) > 3 else ""
        m = re.search(r"^Track:\s*(.+)$", body, re.MULTILINE)
        trailer = m.group(1).strip() if m else None
        paths = [ln for ln in files_blob.splitlines() if ln.strip()]
        track = infer_track(paths, trailer)
        pm = re.match(r"^\s*(\d{3,4})\b", subject)
        patch = pm.group(1) if pm else "----"
        rows.append({"patch":patch,"date":date,"subject":subject,"track":track,"hash":h[:8]})

    by_track = {}
    for r in rows:
        by_track.setdefault(r["track"], []).append(r)

    def last_patch_num(rs):
        nums = [int(r["patch"]) for r in rs if r["patch"].isdigit()]
        return max(nums) if nums else -1

    out = []
    out.append("# CPP Project Ledger — per-patch development trail, grouped by track")
    out.append("")
    out.append(f"*Generated by `scripts/render_project_ledger.py` from git history on "
               f"{datetime.date.today().isoformat()}. This is a RENDERED VIEW — the source of truth is "
               f"git log. Re-run the script any time to refresh; a stale render is never wrong, only old.*")
    out.append("")
    # dashboard: last patch per track, most-recent first
    out.append("## Dashboard — last patch worked, per track")
    out.append("")
    out.append("| Track | Last patch | Date | Last summary |")
    out.append("|---|---|---|---|")
    for track in sorted(by_track, key=lambda t: last_patch_num(by_track[t]), reverse=True):
        rs = sorted(by_track[track], key=lambda r: (r["patch"].isdigit(), r["patch"]))
        last = rs[-1]
        summ = last["subject"][:70].replace("|","\\|")
        out.append(f"| {track} | {last['patch']} | {last['date']} | {summ} |")
    out.append("")
    # full per-track trails
    out.append("## Full trails")
    out.append("")
    for track in sorted(by_track, key=lambda t: last_patch_num(by_track[t]), reverse=True):
        rs = sorted(by_track[track], key=lambda r: (r["patch"].isdigit(), r["patch"]))
        out.append(f"### {track}")
        out.append("")
        for r in rs:
            summ = r["subject"].replace("|","\\|")
            out.append(f"- **{r['patch']}** ({r['date']}, `{r['hash']}`) — {summ}")
        out.append("")

    with open(args.out, "w") as f:
        f.write("\n".join(out) + "\n")
    print(f"Wrote {args.out}: {len(rows)} patches across {len(by_track)} tracks.")

if __name__ == "__main__":
    main()
