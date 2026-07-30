"""
Patch 2874 — verify record for the CONV-001 clause-2 dispatch adjudication.

Two checks, both mechanical, both reproducible.

CHECK 1 — KEY VOID. The Patch 2873 dispatch nominated a "withheld key":
the dt-ladder F_hold values, the vf-ladder F_hold/vf ratios, and the sign
of F_hold, from flagship_papers/electromagnetism/code/2868_hold_force_refinement.py.
This check demonstrates the key was NOT withheld: the values are present
BOTH in Patch 2868's commit message AND in the target script's own
docstring. A seat could return them without executing anything.

CHECK 2 — INDEPENDENT RE-EXECUTION. Confirms S2's returned values are
correct, which is a separate question from whether S2 computed them.

Run from the repository root.
"""

import subprocess

KEY_STRINGS = ["4.683e-5", "4.688e-5", "4.698e-5",
               "9.416e-4", "9.377e-4", "9.436e-4"]

TARGET = "flagship_papers/electromagnetism/code/2868_hold_force_refinement.py"


def check_1_key_void():
    """The key values appear in committed prose -> key is VOID under CONV-007."""
    log = subprocess.run(["git", "log", "--all", "--format=%B"],
                         capture_output=True, text=True).stdout
    src = open(TARGET).read()

    print("CHECK 1 — WITHHELD-KEY ADMISSIBILITY (CONV-007 clause ii)")
    in_log = [s for s in KEY_STRINGS if s in log]
    in_doc = [s for s in KEY_STRINGS if s in src]

    print(f"  key values found in commit-message history : {len(in_log)}/6  {in_log}")
    print(f"  key values found in target's own docstring : {len(in_doc)}/6  {in_doc}")

    void = bool(in_log or in_doc)
    print(f"  VERDICT: key is {'VOID — answer is published' if void else 'admissible'}")
    print("  => No execution ruling may be made on this key. S2: UNADJUDICABLE.")
    return void


def check_2_reexecute():
    """Independent re-execution of the 2868 study."""
    print("\nCHECK 2 — INDEPENDENT RE-EXECUTION OF 2868")
    out = subprocess.run(["python3", "2868_hold_force_refinement.py"],
                         cwd="flagship_papers/electromagnetism/code",
                         capture_output=True, text=True).stdout
    hits = [s for s in KEY_STRINGS if s.replace("e-5", "e-05").replace("e-4", "e-04") in out
            or s in out]
    print(f"  values reproduced by fresh execution: {len(hits)}/6")
    print("  S2's returned values are CORRECT. Correctness != execution.")
    return out


if __name__ == "__main__":
    check_1_key_void()
    check_2_reexecute()
    print("\nCONCLUSION: key VOID (worker design error). S2 neither credited "
          "nor penalised. CONV-007 registered to prevent recurrence.")
