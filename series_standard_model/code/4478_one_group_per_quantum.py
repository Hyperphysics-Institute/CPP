"""Patch 4478 -- founder: the split photon is handled by his Quantum Group Entity (QGE), possibly using the Nexus as its
connection point; can the same be done without adding a mechanism?

Toy bookkeeping (not CPP dynamics): one photon of energy E split by a beam splitter (transmission T) to detectors A and B.
Rule G (global conservation only): any split of E between A and B that sums to E is allowed -> e.g. E/2 at each.
Rule Q (per-quantum, all-or-nothing): the quantum's energy goes whole to one member site, chosen with Born weights (T, 1-T).
Checks: (1) under G, half-and-half conserves energy exactly, so global conservation alone does not give one lump;
(2) under Q, coincidences are zero and each detector's rate is its Born weight;
(3) no-signalling: B's click rate does not change when A's detector is removed or its efficiency changed (A only blocks or
    not; the choice of site is made with fixed weights) -- holds by construction (the site is drawn before A's setting is
    applied); displayed, not tested. No distance or timing is modelled, so 'at once' is not tested.
"""
import numpy as np
rng = np.random.default_rng(7)
E = 1.0; T = 0.5; N = 200000
print(f"(1) Rule G: E_A + E_B = {E/2 + E/2} = E with E_A = E_B = {E/2}: conserved, yet no detector receives a whole quantum")
print("(1b) Rule G with a gap (0.80 eV photon, 0.75 eV InGaAs gap, 4477 sec. 4): each half 0.40 eV < 0.75 eV -> neither detector fires; measured: each fires at the whole-photon rate")
site = rng.random(N) < T                      # True -> A, False -> B (Born weights)
for etaA in (1.0, 0.5, 0.0):                  # A's detector efficiency; 0.0 = detector removed
    clickA = site & (rng.random(N) < etaA)
    clickB = (~site) & (rng.random(N) < 0.8)  # B's efficiency fixed at 0.8
    print(f"(2,3) Rule Q, A efficiency {etaA:.1f}: P(A) = {clickA.mean():.4f}, P(B) = {clickB.mean():.4f}, coincidences = {np.mean(clickA & clickB):.1e}")
print("Rule Q gives zero coincidences (by construction) (measured: ~1e-3 of independent, near detector noise; Guerreiro et al. 2012) and B's rate is unchanged by A")
