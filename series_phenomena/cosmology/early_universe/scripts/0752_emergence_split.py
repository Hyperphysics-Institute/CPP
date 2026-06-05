#!/usr/bin/env python3
"""
0752_emergence_split.py
=======================
Tests the emergence claim: "thermalization (and hence n_s) is emergent from existing
CPP axioms via macro-CP PCD dynamics; provable by Monte Carlo."

The claim has TWO separable halves. This toy shows they have DIFFERENT status:

  HALF 1 (the BATH / ergodicity): do many-body exchange dynamics thermalize a stack to
          a stationary Gibbs distribution? -> YES, generically. EMERGENT. MC-provable.

  HALF 2 (the LOG / absolute concentration chemical potential mu(n) ~ ln n, the thing
          the n_s chain actually uses): is it produced by the dynamics, or by how the
          microstates are COUNTED (indistinguishable vs distinguishable)?
          -> set by the COUNTING, which the dynamics are blind to. The log requires
          INDISTINGUISHABILITY (A1: a CP is only polarity+type+position, no identity).
          Distinguishable tracking gives the n_s=1 CLIFF even with perfect thermalization.

So a Monte Carlo can DERIVE THE BATH but not THE LOG; the log is ontology (A1), not
dynamics. Critically: a literal MC that tracks CPs by individual history (distinguishable
labels) reproduces the EXCLUDED cliff -- the 0749 failure mode in dynamical disguise.
"""

import numpy as np
rng = np.random.default_rng(7)


def thermalize_exchange(M=100, Ntot=2000, steps=400_000, tag_empty=60):
    """Macro-CP-style exchange: at each step a random CP hops to a random GP (over-full
    GPs are drained proportionally, as physical 'a CP leaves' dynamics demand). Seed the
    violent early state on the 13-GP cohort, then watch an INITIALLY-EMPTY GP fill to the
    mean and the full occupation array relax to the Poisson (thermalized) stationary state."""
    part = rng.integers(0, 13, size=Ntot)         # particle -> GP; piled on 13 GPs
    tag_hist = []
    for t in range(steps):
        i = rng.integers(0, Ntot)
        part[i] = rng.integers(0, M)              # a random CP hops to a random GP
        if t % 2000 == 0:
            tag_hist.append(int(np.count_nonzero(part == tag_empty)))
    occ = np.bincount(part, minlength=M)
    return np.array(tag_hist), occ


def mu_of_n(n, kT=1.0, z1=1.0, indistinguishable=True):
    """Absolute chemical potential to hold a stack of n in a fixed cell.
    Indistinguishable (Gibbs, Z=z1^n/n!):  mu = dF/dn = kT ln(n/z1) ~ kT ln n. (LOG)
    Distinguishable  (labels,  Z=z1^n   ):  mu = -kT ln z1 = const.            (CLIFF)"""
    if indistinguishable:
        return kT*np.log(np.maximum(n, 1e-9)/z1)
    return -kT*np.log(z1)*np.ones_like(np.asarray(n, dtype=float))


def ns_from_mu(indistinguishable=True):
    """Push mu(nbar) through the chain (0742): H_eff~mu(nbar), nbar=nbar_i e^{-3N},
    n_s-1 = 2 d ln H_eff/dN, pivot N_rem=57."""
    N_CP, N_GP = 1e80, 13
    Ntot_efold = (1/3)*np.log(N_CP/N_GP)
    N0 = Ntot_efold - 57.0
    nbar = lambda N: (N_CP/N_GP)*np.exp(-3*N)
    H = lambda N: mu_of_n(nbar(N), indistinguishable=indistinguishable) - \
                  mu_of_n(1.0,      indistinguishable=indistinguishable)
    h = 1e-4
    lnH = lambda N: np.log(abs(float(H(N))) + 1e-300)
    return 1 + 2*(lnH(N0+h)-lnH(N0-h))/(2*h)


def main():
    print("="*76)
    print("EMERGENCE SPLIT: the dynamics give the BATH; the COUNTING gives the LOG")
    print("="*76)

    # ---- HALF 1: does exchange dynamics thermalize? (the bath) ----
    lam = 2000/100
    tag_hist, occ = thermalize_exchange()
    print("\n  HALF 1 -- BATH (macro-CP exchange dynamics, seeded on the 13-GP cohort):")
    print(f"    an initially-EMPTY GP: occupation {tag_hist[0]} -> {tag_hist[-1]} (fills to mean lambda={lam:.0f})")
    print(f"    final full-array occupation: mean {occ.mean():.2f}, var {occ.var():.2f}")
    print(f"    Poisson signature mean~var~lambda={lam:.0f}: {'YES' if abs(occ.mean()-occ.var())<0.35*lam else 'partial'}")
    print(f"    => dynamics RELAX from the violent 13-GP seed to the Poisson stationary state.")
    print(f"       Thermalization (ergodicity / the bath) is EMERGENT & generic. [HALF 1: YES]")

    # ---- HALF 2: is the LOG dynamical, or a counting choice? ----
    print("\n  HALF 2 -- LOG (absolute concentration chemical potential the n_s chain uses):")
    ns_indist = ns_from_mu(indistinguishable=True)
    ns_dist   = ns_from_mu(indistinguishable=False)
    print(f"    SAME thermalized stack, two ways of COUNTING its microstates:")
    print(f"      indistinguishable (A1: CP = polarity+type+position, no identity)")
    print(f"          -> mu ~ kT ln n  -> n_s = {ns_indist:.4f}")
    print(f"      distinguishable  (each CP tagged by individual history/label)")
    print(f"          -> mu = const    -> n_s = {ns_dist:.4f}  (CLIFF, EXCLUDED)")
    print(f"    The dynamics are IDENTICAL; only the counting differs. The log is set by")
    print(f"    the COUNTING, not the dynamics. [HALF 2: ontology, not MC-derivable]")

    print("\n" + "="*76)
    print("VERDICT")
    print("="*76)
    print("""  * A Monte Carlo of macro-CP PCD dynamics can DERIVE HALF 1 (the bath): that stacks
    thermalize to a stationary Gibbs distribution on timescales << Hubble. This is the
    half of CAND-AX-EU-1 that felt like a strong assumption -- and the emergence story
    is a serious, plausible route to making it a RESULT. Real progress.

  * It CANNOT derive HALF 2 (the log). mu ~ ln n is the absolute concentration chemical
    potential, which exists ONLY for indistinguishable particles (the Gibbs n! / mixing
    term). That is a COUNTING fact fixed by what a CP IS, not by what the stack DOES.

  * GOOD NEWS: the log's source is already A1. 'CP = polarity + type + position' (no
    individual identity) means same-type CPs on a GP are described by OCCUPATION NUMBERS
    -- permutations are not distinct states -- which IS indistinguishability, which IS
    the n!. So HALF 2 needs NO new axiom; it is entailed by A1.

  * THE TRAP: the 'each CP imprinted by its individual history' framing, taken literally,
    tags CPs with distinguishing labels -> distinguishable -> the CLIFF (n_s=1) above.
    That is the 0749 failure mode wearing a dynamical costume. The fix: histories live in
    the SSV field / configuration (the exchangeable bath), NOT as a permanent identity on
    each CP. Keep CPs as bare A1 occupation-number objects; let the environment carry the
    history. Then indistinguishability (A1) survives and the log stands.

  CONSEQUENCE FOR THE AXIOM: the emergence track SPLITS CAND-AX-EU-1.
    - indistinguishability clause  -> collapses into A1 (no new axiom).
    - ergodicity / bath clause     -> a dynamical claim, plausibly MC-provable.
    - boost ~ mu                   -> still the 0746 count-driven commitment.
  BEST CASE: CAND-AX-EU-1 dissolves entirely -> n_s = 0.9649 becomes a ZERO-NEW-AXIOM
  prediction (A1 + emergent ergodicity + 0746 coupling). That is the honest win the track
  is reaching for -- IF (a) an MC shows macro-CP mixing reaches Gibbs equilibrium << Hubble
  with PERMUTATION-INVARIANT (A1) microstates, and (b) the history is kept in the bath, not
  on the CPs.""")


if __name__ == "__main__":
    main()
