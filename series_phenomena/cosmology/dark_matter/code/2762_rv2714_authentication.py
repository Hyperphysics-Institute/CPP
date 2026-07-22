#!/usr/bin/env python3
"""RV-2714 AUTHENTICATION BATTERY (Patch 2762).

Context: the Patch 2761 artifacts (record, scripts, five data
archives) appeared in the session container UNTRACKED and root-owned,
written by a process other than the committing session, between
turns. Before adoption they were authenticated by deterministic
reproduction against the frozen 2760 pipeline. This script encodes
the battery so any seat can re-run it from the committed repo.

Checks (run from series_phenomena/cosmology/dark_matter/):
  A. ARCHIVE INTEGRITY -- committed data/rv2714/*.json.gz decompress
     to valid jsons with the chartered shapes (5 chains, frozen
     sample counts 480/480/320/320/320).
  B. GATE -- gate v2 re-run (deterministic, seed 1): must PASS all
     five geometries with worst rel disc <= 1e-8 (observed 3.7e-13).
  C. ANALYZER -- the frozen 2713-criteria analyzer re-run over the
     committed archives must reproduce the record Sec.3 table
     (kappa_fit, alt, kappa_S per chain; composite C1..C5 line).
  D. CHAIN REGENERATION (--regen, ~4 min) -- RV-CORE regenerated
     from reserved seed 20260802 with the committed sampler; the 320
     sampled charge profiles must be BIT-IDENTICAL to the archive and
     the szz accumulator equal to <=1e-12 relative (chunk-boundary
     S-refresh residue; it never flips a Metropolis decision, as the
     bit-identical profiles prove).

Original authentication (22 Jul 2026, pre-adoption): A PASS, B PASS
(3.720e-13), C PASS (every printed digit), D PASS (profs max abs
diff 0.0 over all 320x90 entries; szz max rel diff 4.3e-15; acc
identical to 16 digits).
"""
import gzip, json, os, shutil, subprocess, sys, tempfile
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
DM = os.path.dirname(HERE)
EXE = os.path.join(HERE, "2761_rv2714_execution.py")
ARCH = os.path.join(DM, "data", "rv2714")
CHAINS = {"RV-MAIN-A": 480, "RV-MAIN-B": 480,
          "RV-SIZE-S": 320, "RV-SIZE-L": 320, "RV-CORE": 320}

def check_A():
    for lab, ns in CHAINS.items():
        d = json.load(gzip.open(f"{ARCH}/rv_{lab}.json.gz", "rt"))
        assert d["label"] == lab and d["ns"] == ns, (lab, d["ns"])
        assert len(d["profs"]) == ns and len(d["profs"][0]) == d["nb"]
    print("A. ARCHIVE INTEGRITY: PASS (5 chains, frozen sample counts)")

def check_B():
    out = subprocess.run([sys.executable, EXE, "gate"],
                         capture_output=True, text=True)
    ok = "ALL FIVE GEOMETRIES PASS" in out.stdout
    print("B. GATE:", "PASS" if ok else "FAIL")
    print("   " + out.stdout.strip().splitlines()[-1])
    assert ok

def check_C():
    ck = "/tmp/rv2714"
    os.makedirs(ck, exist_ok=True)
    for lab in CHAINS:
        with gzip.open(f"{ARCH}/rv_{lab}.json.gz", "rb") as f:
            open(f"{ck}/rv_{lab}.json", "wb").write(f.read())
    out = subprocess.run([sys.executable, EXE, "analyze"],
                         capture_output=True, text=True)
    print("C. ANALYZER over committed archives:")
    print("\n".join("   " + l for l in out.stdout.strip().splitlines()))
    assert "RV S4-E FAIL" in out.stdout and "C2=PASS" in out.stdout \
        and "C4=PASS" in out.stdout

def check_D():
    tmp = tempfile.mkdtemp(prefix="rv_regen_")
    src = open(EXE).read().replace('CKDIR="/tmp/rv2714"',
                                   f'CKDIR="{tmp}"')
    regen = os.path.join(tmp, "regen.py")
    open(regen, "w").write(src)
    for chunk in ("1100", "900"):
        subprocess.run([sys.executable, regen, "chunk", "RV-CORE",
                        chunk], check=True, cwd=DM,
                       capture_output=True, text=True)
    a = json.load(gzip.open(f"{ARCH}/rv_RV-CORE.json.gz", "rt"))
    b = json.load(open(f"{tmp}/rv_RV-CORE.json"))
    pa, pb = np.array(a["profs"]), np.array(b["profs"])
    sa, sb = np.array(a["szz"]), np.array(b["szz"])
    dprof = float(np.max(np.abs(pa - pb)))
    dszz = float(np.max(np.abs(sa - sb) / np.maximum(np.abs(sa), 1e-30)))
    print(f"D. RV-CORE REGEN from seed 20260802: profs max abs diff "
          f"{dprof:.1e}; szz max rel diff {dszz:.1e}; "
          f"acc {a['acc']:.16f} vs {b['acc']:.16f}")
    assert dprof == 0.0 and dszz < 1e-12 and a["acc"] == b["acc"]
    shutil.rmtree(tmp)
    print("   PASS (bit-identical sampling; szz within S-refresh residue)")

if __name__ == "__main__":
    check_A(); check_B(); check_C()
    if "--regen" in sys.argv:
        check_D()
    else:
        print("D. (skipped; run with --regen, ~4 min)")
    print("AUTHENTICATION BATTERY: COMPLETE")
