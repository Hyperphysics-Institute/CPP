#!/usr/bin/env python3
"""
AME 2020 loader (mass.mas20 format) — for SS-8 Phase 1 and beyond.

Source: M. Wang, W.J. Huang, F.G. Kondev, G. Audi, S. Naimi,
"The AME 2020 atomic mass evaluation (II). Tables, graphs and references,"
Chinese Phys. C 45, 030003 (2021).

Format spec (from the file's own preamble):
  a1,i3,i5,i5,i5,1x,a3,a4,1x,f14.6,f12.6,f13.5,1x,f10.5,1x,a2,f13.5,f11.5,1x,i3,1x,f13.6,f12.6
  cc NZ  N  Z  A    el  o     mass   unc   binding  unc   B    beta  unc   atomic_mass  unc

  '#' in a decimal slot => estimated (non-experimental) value
  '*' in a value slot   => not calculable

We read BE/A in keV, return total B = (BE/A) * A in MeV, flagged experimental vs estimated.

Data file location: the loader expects the AME 2020 data file to be at
  series_strong/data/ame2020_mass.txt
(relative to the CPP repository root). The data file itself is NOT
distributed with the repository for licensing and version-hygiene reasons;
see series_strong/data/data-README.md for download instructions and the
canonical citation.

Author: Claude Opus, 21 April 2026 (SS-8 Phase 1).
Default-path migration: 24 April 2026 — path changed from sandbox-specific
  /home/claude/ame_data/data/ame2020_mass.txt to repo-relative
  series_strong/data/ame2020_mass.txt. FileNotFoundError handling added
  with pointer to data-README.md. No behavior change for scripts that pass
  an explicit path argument.
"""

from pathlib import Path

# --- default path: repo-relative, at series_strong/data/ ---
# This loader is located at series_strong/papers/ame2020_loader.py,
# so the data directory is one level up from papers/. The path is
# computed relative to this file's location so the loader works
# regardless of the user's current working directory at call time.
#
# The AME 2020 data file itself is NOT distributed with the CPP
# repository. See series_strong/data/data-README.md for the rationale
# and for current download instructions.
_DEFAULT = Path(__file__).resolve().parent.parent / "data" / "ame2020_mass.txt"


def _parse_float(field: str):
    """Return (value, is_estimated). Returns (None, _) for '*' or unparseable."""
    s = field.strip()
    if not s or "*" in s:
        return None, False
    est = "#" in s
    if est:
        s = s.replace("#", ".")
    try:
        return float(s), est
    except ValueError:
        return None, est


def load_ame2020(path: Path = _DEFAULT) -> dict:
    """
    Parse mass.mas20 and return a dict keyed by (Z, A):
      (Z, A) -> {
        'el':          element symbol (str),
        'N':           neutron number (int),
        'A':           mass number (int),
        'Z':           proton number (int),
        'BE_per_A':    binding energy per nucleon (MeV),
        'BE_total':    total binding energy (MeV),
        'BE_unc':      BE/A uncertainty (MeV),
        'estimated':   True if BE/A is extrapolated (#), False if measured.
      }

    Rows with '*' in the BE/A field (unbound / not calculable) are skipped.
    """
    table = {}

    path = Path(path)  # accept str or Path
    if not path.exists():
        raise FileNotFoundError(
            f"AME 2020 mass data file not found at expected location:\n"
            f"  {path}\n\n"
            f"This data file is required but is not distributed with the CPP\n"
            f"repository (AME 2020 redistribution permissions not pursued;\n"
            f"researchers download directly from the canonical source). For\n"
            f"current download instructions, expected filename, and file-format\n"
            f"details, see:\n\n"
            f"  series_strong/data/data-README.md\n\n"
            f"Place the downloaded file at the path above (named 'ame2020_mass.txt')\n"
            f"and retry."
        )

    with open(path) as f:
        lines = f.readlines()

    # The header block ends at the line starting "0  1    1    0    1  n" (row for free neutron).
    # Easier: skip until we've passed the column-label line and a blank.
    header_passed = False
    for raw in lines:
        if not header_passed:
            # Data rows start at column 0 with a '0', '1', or ' ' control character
            # and have a 5-character A field at columns 14-19 with digits.
            # Use a simple sentinel: the label line contains "MASS EXCESS"; advance past it.
            if "MASS EXCESS" in raw:
                header_passed = True
            continue

        # skip blank lines or short lines
        if len(raw) < 80:
            continue

        # Fixed-width slicing per the Fortran format.
        # Column indices here are 0-based Python slices.
        try:
            # cc: raw[0:1]
            NmZ_str = raw[1:4]
            N_str   = raw[4:9]
            Z_str   = raw[9:14]
            A_str   = raw[14:19]
            el      = raw[20:23].strip()
            # origin: raw[23:27]

            N = int(N_str.strip())
            Z = int(Z_str.strip())
            A = int(A_str.strip())
        except ValueError:
            # Some header/repeat-banner lines intermix; skip.
            continue

        # BE/A and unc. Per format: after mass (f14.6, f12.6) comes BE/A (f13.5) then
        # a single space (1x) then unc (f10.5).
        # With 1x after a1,i3,i5,i5,i5 = position 19, then a3 (22), a4 (26), 1x (27),
        # f14.6 (41), f12.6 (53), f13.5 (66), 1x (67), f10.5 (77). Use generous slicing.
        BEperA_raw = raw[54:67]
        BEperA_unc_raw = raw[68:78]

        BEperA, est = _parse_float(BEperA_raw)
        if BEperA is None:
            continue

        BEperA_unc, _ = _parse_float(BEperA_unc_raw)
        BEperA_unc = BEperA_unc if BEperA_unc is not None else 0.0

        # Convert keV -> MeV; compute total binding.
        BEperA_MeV = BEperA / 1000.0
        BE_total   = BEperA_MeV * A
        BE_unc_MeV = (BEperA_unc / 1000.0) * A  # propagates linearly since BE = (BE/A)*A

        table[(Z, A)] = {
            "el": el,
            "N": N, "Z": Z, "A": A,
            "BE_per_A": BEperA_MeV,
            "BE_total": BE_total,
            "BE_unc":   BE_unc_MeV,
            "estimated": est,
        }

    return table


def B(table: dict, Z: int, A: int, allow_estimated: bool = False) -> float:
    """Lookup convenience: return total binding energy in MeV. Raises if missing
    or (by default) estimated. For Phase 1 we only use measured values."""
    if (Z, A) not in table:
        raise KeyError(f"AME 2020 has no entry for (Z={Z}, A={A})")
    entry = table[(Z, A)]
    if entry["estimated"] and not allow_estimated:
        raise ValueError(
            f"(Z={Z}, A={A}) = {entry['el']}{A} is extrapolated in AME 2020; "
            f"set allow_estimated=True to use the value {entry['BE_total']:.3f} MeV."
        )
    return entry["BE_total"]


if __name__ == "__main__":
    # Smoke test: known anchor values.
    t = load_ame2020()

    print(f"Loaded {len(t)} nuclides from AME 2020.\n")

    checks = [
        (2, 4,   "4He",  28.296),   # from SS-5
        (6, 12,  "12C",  92.162),   # from strict N=Z anchor
        (8, 16,  "16O",  127.619),
        (20, 40, "40Ca", 342.052),
        (20, 48, "48Ca", 415.991),  # widely-cited AME 2020 value (stress test)
        (28, 56, "56Ni", 483.990),  # top of the strict N=Z alpha chain
        (22, 48, "48Ti", 418.699),  # paper-choice anchor (retired)
        (26, 56, "56Fe", 492.254),  # paper-choice anchor (retired)
    ]
    print(f"{'Nuclide':>8} {'Z':>3} {'A':>4} {'B_AME (MeV)':>14} {'expected':>12} "
          f"{'diff (keV)':>12} {'est?':>5}")
    print("-" * 68)
    for Z, A, label, expected in checks:
        entry = t[(Z, A)]
        got = entry["BE_total"]
        diff_keV = (got - expected) * 1000.0
        print(f"{label:>8} {Z:>3} {A:>4} {got:>14.3f} {expected:>12.3f} "
              f"{diff_keV:>+12.1f} {str(entry['estimated']):>5}")
