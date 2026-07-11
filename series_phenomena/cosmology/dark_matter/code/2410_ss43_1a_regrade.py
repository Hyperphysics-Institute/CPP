#!/usr/bin/env python3
"""Patch 2410 — SS43 (1a) adjudication: the N=7 re-grade fired against the
founder-provided official WS2022+WS2024 combined SI limit table.

Data artifact: 2410_HEPData-ins2841863-v2_SIcrosssection.csv
  (md5 6b613af81add72ba9eb3971efeb92753) = the official HEPData CSV export
  for arXiv:2410.17036 / PRL 135, 011802 (record ins2841863 v2), table
  "SI cross section", downloaded by the founder from the HEPData record
  page (the automated endpoints remain bot-blocked; a 503 hit the table-CSV
  button; the full-record CSV tarball succeeded) and delivered in-session
  alongside a screenshot of the rendered table.

Checks (authentication is four-factor):
  V-DOI     the CSV header self-identifies with the PINNED table DOI
            10.17182/hepdata.155182.v2/t1 (§34.16).
  V-NAME    header names the combined analysis (SI_WS2022+WS2024).
  V-ANCHOR  the 40-GeV row reproduces the §34.16 registered text anchor
            "curve minimum 2.2e-48 at 40 GeV" to 2 significant figures.
  V-COVER   coverage starts at 9.0 GeV ("masses >= 9 GeV" anchor).
  V-SHOT    the 9.0-GeV row equals the screenshot value digit-for-digit.
  (Parser reads ONLY the stacked block headed 'mass,limit' — the observed
  column; the CSV export stacks each dependent variable as its own block.
  The first parser version mixed blocks; V-SHOT and V-ANCHOR caught it —
  the incident is recorded in reasoning/2410.md §5.)
  V-BRACK   9.86 GeV strictly inside the 9.0–11.0 bracket.
  V-INTERP  log-log interpolant inside the bracket values.
  V-CONV    BOTH registered conventions (§34.16: nearest tabulated mass,
            or log-interpolated) agree in verdict.
  V-STRICT  strict-point re-arm consumed: the superseding strict point is
            the table's own minimum; N=8's derived 2.85e-49 clears it by
            the audited ~7.7x (re-verified arithmetically here).

Pre-staged re-grade (§34.16, fires on the number, no renegotiation):
  N = 7 CLEARS iff sigma_LZ,combined(9.86 GeV) > 1.16e-46 cm^2.

Zero tunables. Output: 2410_results.json.
"""
import csv, json, math, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "2410_HEPData-ins2841863-v2_SIcrosssection.csv")

PINNED_DOI = "10.17182/hepdata.155182.v2/t1"
SCREENSHOT_9GEV = 9.797484060822151e-47
N7_MASS, N7_THRESH = 9.86, 1.16e-46
N8_DERIVED = 2.85e-49

def main():
    header_lines, rows = [], []
    in_limit_block = False
    with open(DATA) as f:
        for line in f:
            s = line.strip()
            if s.startswith("#"):
                header_lines.append(s)
            elif s == "mass,limit":
                in_limit_block = True          # the OBSERVED-limit block only
            elif s.startswith("mass,"):
                in_limit_block = False         # any other dependent-variable block
            elif in_limit_block and s:
                m, v = s.split(",")[:2]
                rows.append((float(m), float(v)))
    rows.sort()
    masses = [r[0] for r in rows]
    lim = [r[1] for r in rows]
    head = "\n".join(header_lines)

    checks = {}
    checks["V-DOI_pinned_table_doi_in_header"] = PINNED_DOI in head
    checks["V-NAME_combined_analysis"] = "SI_WS2022+WS2024" in head
    m40 = lim[masses.index(40.0)]
    checks["V-ANCHOR_40GeV_min_eq_2.2e-48"] = float(f"{m40:.1e}") == 2.2e-48
    checks["V-ANCHOR_40GeV_is_curve_min"] = (m40 == min(lim))
    checks["V-COVER_starts_at_9GeV"] = (masses[0] == 9.0)
    checks["V-SHOT_9GeV_row_matches_screenshot"] = (lim[0] == SCREENSHOT_9GEV)

    # bracket + log-interp at 9.86
    i = max(j for j in range(len(masses)) if masses[j] < N7_MASS)
    lo, hi = (masses[i], lim[i]), (masses[i + 1], lim[i + 1])
    checks["V-BRACK_9.86_inside"] = lo[0] < N7_MASS < hi[0]
    t = (math.log(N7_MASS) - math.log(lo[0])) / (math.log(hi[0]) - math.log(lo[0]))
    v_interp = math.exp(math.log(lo[1]) + t * (math.log(hi[1]) - math.log(lo[1])))
    checks["V-INTERP_inside_bracket"] = min(lo[1], hi[1]) <= v_interp <= max(lo[1], hi[1])

    # nearest-tabulated-mass convention
    nearest = min(masses, key=lambda m: abs(m - N7_MASS))
    v_nearest = lim[masses.index(nearest)]

    clear_interp = v_interp > N7_THRESH
    clear_nearest = v_nearest > N7_THRESH
    checks["V-CONV_both_conventions_agree"] = (clear_interp == clear_nearest)

    # strict-point re-arm
    n8_factor = m40 / N8_DERIVED
    checks["V-STRICT_N8_clears_superseding_strict_point"] = N8_DERIVED < m40
    checks["V-STRICT_N8_factor_matches_audited_7.7x"] = abs(n8_factor - 7.7) < 0.1

    verdict = "CLEARS" if clear_interp else "FAILS"
    res = {
        "table": {
            "n_points": len(rows), "mass_range_GeV": [masses[0], masses[-1]],
            "file_md5": "6b613af81add72ba9eb3971efeb92753",
            "source": "founder-downloaded official HEPData CSV export, "
                      "record ins2841863 v2, table 'SI cross section' "
                      f"(header DOI {PINNED_DOI})",
        },
        "grade_N7": {
            "mass_GeV": N7_MASS,
            "sigma_LZ_loginterp_cm2": v_interp,
            "bracket_low": {"mass": lo[0], "limit": lo[1]},
            "bracket_high": {"mass": hi[0], "limit": hi[1]},
            "sigma_LZ_nearest_mass_cm2": {"mass": nearest, "limit": v_nearest},
            "derived_threshold_cm2": N7_THRESH,
            "pre_staged_condition": "N=7 CLEARS iff sigma_LZ(9.86) > 1.16e-46",
            "verdict": verdict,
            "fail_factor_interp": (N7_THRESH / v_interp) if not clear_interp else None,
            "fail_factor_nearest": (N7_THRESH / v_nearest) if not clear_nearest else None,
            "registered_fail_branch": "N=7 dies in-coverage fully derived; "
                "N=8 stands alone unconditionally clear; family-level "
                "survival persists on N=8 with member-weight consequences "
                "to the founder's desk (S34.16 verbatim)",
        },
        "strict_point_rearm_consumed": {
            "superseding_strict_point_cm2": m40, "at_mass_GeV": 40.0,
            "N8_derived_cm2": N8_DERIVED, "N8_clear_factor": n8_factor,
        },
        "checks": checks,
    }
    res["ALL_CHECKS_PASS"] = all(checks.values())
    json.dump(res, open(os.path.join(HERE, "2410_results.json"), "w"), indent=2)
    print(json.dumps(res, indent=2))
    if not res["ALL_CHECKS_PASS"]:
        sys.exit(1)

if __name__ == "__main__":
    main()
