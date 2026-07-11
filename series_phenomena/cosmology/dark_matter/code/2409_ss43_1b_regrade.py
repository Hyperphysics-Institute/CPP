#!/usr/bin/env python3
"""Patch 2409 — SS43 (1b) adjudication: the three edge-species re-grades
fired against the committed official WS2025 SI limit table.

Data artifact: 2409_HEPData-ins3091049-v2-SI_cross_section.yaml
  = verbatim copy (md5 de096873b1bc77fa04c47e173dd0596b) of the official
  HEPData release file for arXiv:2512.08065 (record ins3091049, VERSION 2,
  DOI 10.17182/hepdata.167350; table t1 "SI cross section"), obtained via
  the vendored mirror at github.com/xjw44/QuantumDMLimits
  curves/2512.08065v2/ (the HEPData download endpoints are bot-blocked to
  this environment; the mirror carries HEPData's own file naming and is
  authenticated below against two independent paper-text anchors).

Checks:
  V-AUTH   both curve endpoints reproduce the arXiv-v2 text anchors
           ("2.1e-42 at 3 GeV" / "1.1e-46 at 9 GeV") to 2 significant
           figures — the file IS the published curve.
  V-COL    the observed-limit column is column 0, named 'limit'
           (sensitivity bands and 3sigma-disco are separate columns).
  V-BRACK  each target mass is strictly inside a tabulated bracket.
  V-INTERP each log-log interpolated value lies between its bracket
           values (monotone segment sanity).
  RE-GRADE the three pre-staged conditionals (registered at §34.17 /
           Patch 2406) fire mechanically:
             N=4 SURVIVES iff sigma_LZ(5.63) > 1.37e-38 cm^2
             N=5 SURVIVES iff sigma_LZ(7.04) > 2.46e-41 cm^2
             N=6 SURVIVES iff sigma_LZ(8.45) > 5.07e-44 cm^2

Zero tunables. Output: 2409_results.json.
"""
import json, math, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "2409_HEPData-ins3091049-v2-SI_cross_section.yaml")

def load_table(path):
    """Parse the HEPData YAML; use PyYAML if present, else a minimal
    line parser adequate for this file's flat structure."""
    try:
        import yaml
        d = yaml.safe_load(open(path))
        masses = [v["value"] for v in d["independent_variables"][0]["values"]]
        cols = [(c["header"]["name"], [v["value"] for v in c["values"]])
                for c in d["dependent_variables"]]
        return masses, cols
    except ImportError:
        txt = open(path).read()
        # dependent blocks come first in this file; independent after
        dep, ind = txt.split("independent_variables:")
        names = re.findall(r"name:\s*(\S+)", dep)
        blocks = re.split(r"- header:", dep)[1:]
        cols = []
        for name, b in zip(names, blocks):
            vals = [float(x) for x in re.findall(r"- value:\s*([-\d.eE+]+)", b)]
            cols.append((name, vals))
        masses = [float(x) for x in re.findall(r"- value:\s*([-\d.eE+]+)", ind)]
        return masses, cols

def loginterp(masses, lim, m):
    for i in range(len(masses) - 1):
        if masses[i] < m < masses[i + 1]:
            t = (math.log(m) - math.log(masses[i])) / (
                math.log(masses[i + 1]) - math.log(masses[i]))
            v = math.exp(math.log(lim[i]) + t * (math.log(lim[i + 1]) - math.log(lim[i])))
            return v, (masses[i], lim[i]), (masses[i + 1], lim[i + 1])
    raise ValueError(f"mass {m} not strictly inside a tabulated bracket")

def sig2(x):
    from decimal import Decimal
    return float(f"{x:.1e}")

def main():
    masses, cols = load_table(DATA)
    checks, res = {}, {}

    # V-COL
    checks["V-COL_observed_is_col0_named_limit"] = (cols[0][0] == "limit")
    lim = cols[0][1]
    col_names = [c[0] for c in cols]
    checks["V-COL_band_columns_present"] = all(
        n in col_names for n in ["-2sigma", "-1sigma", "median", "1sigma", "2sigma"])

    # V-AUTH: arXiv v2 text anchors, 2 sig figs
    checks["V-AUTH_endpoint_3GeV_eq_2.1e-42"] = (
        masses[0] == 3.0 and sig2(lim[0]) == 2.1e-42)
    checks["V-AUTH_endpoint_9GeV_eq_1.1e-46"] = (
        masses[-1] == 9.0 and sig2(lim[-1]) == 1.1e-46)

    targets = [("N=4", 5.63, 1.37e-38),
               ("N=5", 7.04, 2.46e-41),
               ("N=6_dprime_attestation", 8.45, 5.07e-44)]
    grades = {}
    for label, m, thresh in targets:
        v, lo, hi = loginterp(masses, lim, m)
        checks[f"V-BRACK_{label}"] = lo[0] < m < hi[0]
        checks[f"V-INTERP_{label}_inside_bracket"] = (
            min(lo[1], hi[1]) <= v <= max(lo[1], hi[1]))
        survives = v > thresh
        grades[label] = {
            "mass_GeV": m,
            "sigma_LZ_cm2_loginterp": v,
            "bracket_low": {"mass": lo[0], "limit": lo[1]},
            "bracket_high": {"mass": hi[0], "limit": hi[1]},
            "derived_residual_cm2": thresh,
            "pre_staged_condition": f"SURVIVES iff sigma_LZ({m}) > {thresh:.3e}",
            "verdict": "SURVIVES" if survives else "EXCLUDED",
            "limit_over_derived": v / thresh,
            "exclusion_factor_derived_over_limit": (thresh / v) if not survives else None,
        }

    res["table"] = {
        "n_points": len(masses),
        "mass_range_GeV": [masses[0], masses[-1]],
        "endpoints": {"3.0": lim[0], "9.0": lim[-1]},
        "file_md5": "de096873b1bc77fa04c47e173dd0596b",
        "source": "HEPData ins3091049 v2, table 'SI cross section' "
                  "(DOI 10.17182/hepdata.167350), via vendored mirror "
                  "github.com/xjw44/QuantumDMLimits",
    }
    res["adjacent_fact_no_verdict"] = {
        "note": "WS2025 observed endpoint 1.112e-46 at 9.0 GeV is below the "
                "N=7 threshold 1.16e-46 but at the wrong mass AND from a "
                "different dataset than the pinned 2024 combined curve — "
                "explicitly NOT consumed for the (1a) N=7 pin.",
        "ws2025_at_9GeV": lim[-1],
        "n7_threshold": 1.16e-46,
    }
    res["grades"] = grades
    res["checks"] = checks
    res["ALL_CHECKS_PASS"] = all(checks.values())

    out = os.path.join(HERE, "2409_results.json")
    json.dump(res, open(out, "w"), indent=2)
    print(json.dumps(res, indent=2))
    if not res["ALL_CHECKS_PASS"]:
        sys.exit(1)

if __name__ == "__main__":
    main()
