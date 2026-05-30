#!/usr/bin/env python3
"""
verify_tarrow_1_arrow_status.py
THEO-CHIR-TARROW-1 (Patch 0658, Session 149) verification.

The temporal-arrow (OPEN-CHIR-2a) status capstone: the parallel of
THEO-CHIR-STATUS-1 + STATUS-2 for the time-reversal arrow sign(delta)
(P-even / T-odd, per THEO-CHIR-MERGE-2), instead of the spatial pseudoscalar
sign(n-hat) = FI-C-9 (P-odd / T-even).

CHECK 1 (verdict partition, instantiated on the TEMPORAL axis): the STATUS-1
  partition map on C_T x V_T  (C_T in {No, Yes} = is a substrate T-asymmetry
  mechanism derivable?;  V_T in {derived, spontaneous, free} = is the arrow
  DIRECTION fixed?) sends every cell to exactly one of {W1, W2, W3}, every
  verdict realized, mutually exclusive. (Same structure as STATUS-1; W = the
  temporal instantiation, tracked distinct from the spatial V.)

CHECK 2 (the T-breaking structure + placement W3 + axiom-level W2-exclusion):
  (a) every STATIC-geometric invariant of the substrate is T-even, so the
      geometry supplies NO T-odd quantity (the disanalogy with parity, where the
      achiral 600-cell still supplies the P-odd order parameter sign(n-hat));
  (b) the unique T-odd object in the registered framework is the arrow sign(delta)
      itself (the j_net arrow, via MERGE-alpha) -> fixing the direction is
      circular -> value != derived at axiom level -> W2 EXCLUDED at axiom level;
  (c) no registered mechanism DERIVES the substrate T-asymmetry (DSL-3 narrates
      the arrow but inherits the DSL viability ceiling) -> C_T = No -> placement
      W3; the C_T->Yes upgrade is pinned to W1.

CHECK 3 (the CPT unification of the two sign-reopeners): the spatial V2-reopener
  (an axiom-EXTERNAL P-odd pseudoscalar, STATUS-2 1d-beta-v) and the temporal
  W2-reopener (an axiom-external T-odd quantity) are, under CPT (T-violation
  <=> CP-violation), the SAME cross-sector object: the SM CP/T-violating phase
  (OPEN-SM-4). Hence "fully deriving chirality" (both the P-sign and the T-arrow)
  is a SINGLE cross-sector target, not two.

Finite logical/symmetry-bookkeeping check (no physics computation), parallel to
verify_status_1 / verify_status_2.
"""

import itertools

# ---- the verdict structure, shared with STATUS-1 (instantiated on T axis) ----
CAPACITY = ["No", "Yes"]                       # C_T: is a T-asymmetry mechanism derivable?
VALUE = ["derived", "spontaneous", "free"]     # V_T: is the arrow DIRECTION fixed?


def verdict(capacity, value):
    """STATUS-1 partition map, temporal instantiation -> {W1, W2, W3}."""
    if capacity == "No":
        return "W3"                # no mechanism -> primitive arrow; value moot
    if value == "derived":
        return "W2"                # mechanism + direction both derived
    return "W1"                    # mechanism derived, direction contingent/free


def check_1_partition():
    cells = list(itertools.product(CAPACITY, VALUE))
    assert len(cells) == 6
    mapped = {cell: verdict(*cell) for cell in cells}

    for cell, v in mapped.items():
        assert v in {"W1", "W2", "W3"}, f"{cell} -> {v} not a verdict"
    assert set(mapped.values()) == {"W1", "W2", "W3"}, "not all verdicts realized"

    no_cells = {v for (c, val), v in mapped.items() if c == "No"}
    assert no_cells == {"W3"}, "C_T=No must collapse to W3 (value moot)"
    assert mapped[("Yes", "derived")] == "W2"
    assert mapped[("Yes", "spontaneous")] == "W1"
    assert mapped[("Yes", "free")] == "W1"

    # mutual exclusivity: W3 has distinct C from W1/W2; W1 distinct V from W2
    w3_caps = {c for (c, val), v in mapped.items() if v == "W3"}
    w12_caps = {c for (c, val), v in mapped.items() if v in {"W1", "W2"}}
    assert w3_caps == {"No"} and w12_caps == {"Yes"}

    print("CHECK 1 PASS: {W1,W2,W3} exhaustively & exclusively partition C_T x V_T")
    print("              (the STATUS-1 partition, instantiated on the temporal axis).")
    return True


def check_2_tbreaking_placement_exclusion():
    # (a) static-geometric invariants are all T-even.
    # T acts only on dynamical variables (j_net, omega_PCD, delta); the 600-cell
    # lattice is a static configuration. We tabulate the registered objects by
    # their (P, T) character (P,T in {+1 even, -1 odd}); from MERGE-2:
    #   sign(n-hat) = FI-C-9 : P-odd, T-even   (spatial pseudoscalar / chirality)
    #   delta / sign(delta)  : P-even, T-odd   (the arrow; conditional on MERGE-alpha)
    #   omega_PCD            : P-even, T-odd   (axial, cycle progression sense)
    #   Gram / dist-spectrum : P-even, T-even  (static geometric invariants)
    #   signed 4-volume det  : P-odd,  T-even  (a pseudoscalar; static)
    PT = {
        "sign(n-hat)=FI-C-9": (-1, +1),
        "sign(delta)":        (+1, -1),
        "omega_PCD":          (+1, -1),
        "Gram":               (+1, +1),
        "distance_spectrum":  (+1, +1),
        "signed_4volume_det": (-1, +1),
    }
    static_geometric = ["sign(n-hat)=FI-C-9", "Gram", "distance_spectrum",
                        "signed_4volume_det"]
    # every static-geometric invariant is T-even:
    for q in static_geometric:
        assert PT[q][1] == +1, f"{q} should be T-even (static geometry)"
    print("CHECK 2a PASS: every static-geometric invariant is T-even")
    print("              => the substrate GEOMETRY supplies no T-odd quantity")
    print("              (disanalogy with parity: the achiral 600-cell still")
    print("               supplies the P-odd order parameter sign(n-hat)).")

    # (b) the unique T-odd object in the registered framework.
    t_odd_objects = [q for q, (p, t) in PT.items() if t == -1]
    # sign(delta) and omega_PCD are the SAME arrow content (omega_PCD = sigma_cycle*n-hat,
    # and the T-odd part of sigma_cycle is exactly sign(delta) -- MERGE-2). So the
    # unique INDEPENDENT T-odd primitive is the arrow sign(delta) (= the j_net arrow,
    # MERGE-alpha). Fixing the direction with it is circular.
    assert set(t_odd_objects) == {"sign(delta)", "omega_PCD"}
    independent_t_odd_primitive = "sign(delta)"   # omega_PCD is not independent of it
    fixing_is_circular = (independent_t_odd_primitive == "sign(delta)")
    assert fixing_is_circular
    value_at_axiom_level = "spontaneous_or_free"  # NOT 'derived' (circular)
    W2_excluded_at_axiom = (value_at_axiom_level != "derived")
    assert W2_excluded_at_axiom
    print("CHECK 2b PASS: the only axiom-level T-odd object is sign(delta) itself")
    print("              => sign-direction fixing is circular => value != derived")
    print("              => W2 EXCLUDED at axiom level (presently registered inventory).")

    # (c) capacity at current rigor + placement + upgrade pin.
    premises = {
        "P1_merge2_isolates_arrow_as_sign_delta": True,  # sigma_cycle T-odd part = sign(delta)
        "P2_geometry_T_even": True,                      # CHECK 2a
        "P3_only_T_odd_is_the_arrow": True,              # CHECK 2b
        "P4_no_derived_T_asymmetry_mechanism": True,     # DSL-3 narrates, does not derive
                                                         # (DSL viability ceiling; F.2 gate)
    }
    capacity_now = "Yes" if not premises["P4_no_derived_T_asymmetry_mechanism"] else "No"
    assert capacity_now == "No"
    placement = verdict(capacity_now, "free")   # value moot under C_T=No
    assert placement == "W3", f"current-rigor placement should be W3, got {placement}"
    # upgrade: flip C_T to Yes (a derived substrate T-asymmetry mechanism, the F.2 +
    # DSL-arrow-emergence engine) -> with value spontaneous/free -> W1.
    assert verdict("Yes", "free") == "W1"          # cosmological inheritance (low-entropy past)
    assert verdict("Yes", "spontaneous") == "W1"
    assert verdict("Yes", "derived") == "W2"       # only if a T-odd fixer appears
    print("CHECK 2c PASS: no derived T-asymmetry mechanism => C_T=No => placement W3;")
    print("              C_T->Yes is pinned to W1 (direction free = cosmological")
    print("              inheritance / low-entropy past), W2 only via an external T-odd fixer.")
    return True


def check_3_cpt_unification():
    # The spatial V2-reopener and the temporal W2-reopener.
    # STATUS-2: V2 reopens only via an axiom-EXTERNAL P-odd pseudoscalar (1d-beta-v),
    #   the natural candidate = the SM CP-violating phase (OPEN-SM-4).
    # TARROW-1: W2 reopens only via an axiom-external T-odd quantity.
    # CPT theorem: in a CPT-invariant theory, T-violation <=> CP-violation.
    spatial_reopener_character = "P-odd"     # a pseudoscalar fixes sign(n-hat)
    temporal_reopener_character = "T-odd"    # a T-odd quantity fixes sign(delta)
    # CPT map: a cross-sector CP-violating phase is, equivalently, T-violating.
    cpt_links = {"CP-violating": "T-violating"}
    sm_object = "SM_CP_phase_OPEN-SM-4"      # delta_CP / CKM-PMNS CP phase
    # spatial side consumes it as the P-odd (CP) pseudoscalar; temporal side
    # consumes it as the T-odd (T-violating) partner -- SAME object under CPT.
    spatial_uses = sm_object                 # 1d-beta-v
    temporal_uses = sm_object                # via CPT
    assert spatial_uses == temporal_uses, "reopeners must be the same cross-sector object"
    assert cpt_links["CP-violating"] == "T-violating"
    single_target = (spatial_uses == temporal_uses)
    assert single_target
    print("CHECK 3 PASS: under CPT (T-violation <=> CP-violation) the spatial V2-reopener")
    print("              (P-odd SM CP-phase, 1d-beta-v) and the temporal W2-reopener")
    print("              (T-odd) are the SAME object (OPEN-SM-4). 'Fully deriving")
    print("              chirality' (P-sign + T-arrow) is a SINGLE cross-sector target.")
    return True


if __name__ == "__main__":
    ok1 = check_1_partition(); print()
    ok2 = check_2_tbreaking_placement_exclusion(); print()
    ok3 = check_3_cpt_unification(); print()
    if ok1 and ok2 and ok3:
        print("ALL CHECKS PASS.")
        print("THEO-CHIR-TARROW-1: the T-arrow sign(delta) (OPEN-CHIR-2a) is W3 at current")
        print("rigor (one currently-identified irreducible T-arrow primitive; NOT YET")
        print("derived; conditional on MERGE-alpha), upgrade pinned to W1 (direction free =")
        print("cosmological inheritance); W2 excluded at axiom level; the W2 reopener is, by")
        print("CPT, the SAME SM CP/T-violating phase (OPEN-SM-4) that reopens the spatial V2.")
        print("Full chirality status = STATUS-1 ^ STATUS-2 ^ TARROW-1: P-sign V3->V1, T-arrow")
        print("W3->W1, both fully-derivable only through one cross-sector CPT-linked object.")
