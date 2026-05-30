#!/usr/bin/env python3
"""
verify_status_1_verdict_partition.py
THEO-CHIR-STATUS-1 (Patch 0653, Session 149) verification.

CHECK 1 (Theorem "Exhaustive partition"): the verdict map on the outcome space
  C x V  (C in {No, Yes}, V in {derived, spontaneous, free}) sends every cell to
  exactly one of {V1, V2, V3}, every verdict is realized, and the three are
  mutually exclusive.

CHECK 2 (Theorem "Current-rigor status is V3"): given the registered-record
  premises P1-P4 (capacity NOT established => C = No), the placement logic yields
  V3; and the upgrade logic (flip C to Yes) yields V1 (spontaneous/free) or V2
  (derived), per Theorem "V1 upgrade condition".

This is a finite logical/classification check (no physics computation); it
machine-checks the partition and placement claims of a status theorem.
"""

import itertools

CAPACITY = ["No", "Yes"]
VALUE = ["derived", "spontaneous", "free"]


def verdict(capacity, value):
    """The verdict map of Definition 'The three verdicts'."""
    if capacity == "No":
        return "V3"                      # value moot
    # capacity == "Yes"
    if value == "derived":
        return "V2"
    return "V1"                          # spontaneous or free


def check_1_partition():
    cells = list(itertools.product(CAPACITY, VALUE))
    assert len(cells) == 6, "outcome space should have 2x3 = 6 cells"

    mapped = {cell: verdict(*cell) for cell in cells}

    # (a) every cell maps to exactly one verdict in {V1,V2,V3}
    for cell, v in mapped.items():
        assert v in {"V1", "V2", "V3"}, f"{cell} -> {v} not a verdict"

    # (b) every verdict is realized
    realized = set(mapped.values())
    assert realized == {"V1", "V2", "V3"}, f"not all verdicts realized: {realized}"

    # (c) the C=No cells all collapse to V3 (value moot)
    no_cells = [v for (c, val), v in mapped.items() if c == "No"]
    assert set(no_cells) == {"V3"}, "C=No must collapse to V3"

    # (d) C=Yes splits by value: derived->V2, {spontaneous,free}->V1
    assert mapped[("Yes", "derived")] == "V2"
    assert mapped[("Yes", "spontaneous")] == "V1"
    assert mapped[("Yes", "free")] == "V1"

    # (e) mutual exclusivity: V3 has distinct C from V1/V2; V1 distinct V from V2
    v3_caps = {c for (c, val), v in mapped.items() if v == "V3"}
    v12_caps = {c for (c, val), v in mapped.items() if v in {"V1", "V2"}}
    assert v3_caps == {"No"} and v12_caps == {"Yes"}, "V3 vs {V1,V2} not C-separated"

    print("CHECK 1 PASS: {V1,V2,V3} exhaustively & exclusively partition C x V.")
    print("              C=No -> V3 (3 cells collapse); C=Yes -> V2 (derived) / V1 (else).")
    return True


def check_2_placement_and_upgrade():
    # P1-P4: capacity NOT established under the present registered framework => C = No.
    premises = {
        "P1_merge2_reduces_to_FIC9": True,     # all currently-identified chirality -> FI-C-9
        "P2_600cell_achiral": True,            # geometry supplies no handedness
        "P3_FIC9_consumed_not_derived": True,  # CHI-1, CAP-1, MERGE-2 consume it
        "P4_no_chiral_vacuum_mechanism": True, # 1d-beta-ii open/deferred
    }
    # capacity is Yes only if a derivable chiral-vacuum mechanism is registered;
    # P4 says none is => capacity = No.
    capacity_now = "Yes" if not premises["P4_no_chiral_vacuum_mechanism"] else "No"
    assert capacity_now == "No"
    placement = verdict(capacity_now, "free")  # value moot under C=No
    assert placement == "V3", f"current-rigor placement should be V3, got {placement}"

    # upgrade logic: flip C to Yes (1d-beta-ii derives a mechanism)
    assert verdict("Yes", "spontaneous") == "V1"  # contingent sign  -> V1
    assert verdict("Yes", "free") == "V1"          # unconstrained sign -> V1
    assert verdict("Yes", "derived") == "V2"       # sign-fixing asymmetry -> V2

    print("CHECK 2 PASS: P1-P4 => C=No => current-rigor verdict V3 ('not yet derived').")
    print("              Upgrade: C->Yes gives V1 (spontaneous/free) or V2 (derived).")
    print("              => achievable upgrade is V1; V2 needs a sign-fixing asymmetry.")
    return True


if __name__ == "__main__":
    ok1 = check_1_partition()
    print()
    ok2 = check_2_placement_and_upgrade()
    print()
    if ok1 and ok2:
        print("ALL CHECKS PASS.")
        print("THEO-CHIR-STATUS-1: chirality status = V3 at current rigor (FI-C-9 the one")
        print("currently-identified irreducible chirality primitive, NOT YET derived;")
        print("conditional on MERGE-alpha), upgradeable to V1 via 1d-beta-ii. Temporal-arrow")
        print("status (sign(delta)) is the parallel OPEN-CHIR-2a, tracked separately.")
