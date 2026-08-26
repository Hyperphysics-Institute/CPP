# CONV-001 PANEL BRIEF — ANA-MEM-1 (analytic route to OPEN-K1-MEMORY-1B)

**Registered Patch 3505, 26 August 2026. Dispatch pending founder
paste. Seats S1–S5, independent returns, no cross-reading. This packet
is self-contained: answer from what is stated here plus your own
physics; if you consult anything else, declare it.**

---

## PACKET — context (all statements are corpus-adjudicated or founder
verbatim; provenance in brackets)

P1. The candidate: a closed dark-matter ring of 16 planes organized as
8 two-plane elements (1.408 GeV per element, 11.26 GeV total). Its
promotion ledger stands at six of seven; the seventh item (PR7 clause
2 = OPEN-K1-MEMORY-1B) requires the memory-force subdominance bound
δ_mem ≡ |F_mem|/|F_inst| ≤ 0.15, where F_inst is the instantaneous
force and the norm, state class, and frequency range must be specified.
[K4 adjudication, Patch 2837]

P2. Substrate physics, founder verbatim [Patch 3426]: "There is no
memory of one Moment to the next carried by CPs, GPs, or DI-bits. CPs
respond only to the DI-bits that arrive at each GP at each Moment, and
yes, the signal of self on the environment affects the environment the
CP is going into through the DP arcs, their signal back-radiation, and
summation. That is the essence of the Kinetic energy mechanism." The
substrate is Markovian by specification; memory is projection-induced
in the charge-only description. [K2, 2837, with S1's state-enumeration
qualification]

P3. The promotion computation already contains a velocity-coupled Sea
response: the SF-6 speed-memory term at independently pinned
coefficients κ_q = 132 MeV/c², κ_e = 44 MeV/c². [Patch 2510]

P4. Fore/aft cancellation: for a uniformly moving charge, arc
establishment ahead and discharge behind cancel — no net longitudinal
first-order force. [Founder, 25 Jul; Patch 2838] The leading surviving
correction is Darwin-class O(v²/c²), CONDITIONAL on the relay
reproducing the transverse sector at the right order; emergent Coulomb
tested the scalar sector only. [2838]

P5. Proposed reduced dynamics [ANA-MEM-1 charter, 3504, DRAFT]:
m_bare a(t) = F_inst[x(t)] + ∫₀^∞ K(τ) v(t−τ) dτ + higher multipoles,
with the split K(τ) = K̄ δ(τ) + K_res(τ), K̄ = ∫K dτ, ∫K_res dτ = 0.

## QUESTIONS

**Q1 — The subtraction.** Is 1B's numerator correctly the RESIDUAL
memory force — |F_res| with the modeled SF-6 channel subtracted —
rather than the total kernel force? Argument for: the leading wake IS
the modeled kinetic-energy mechanism (P2, P3); bounding the total
would double-count physics already inside the promotion computation.
Argument against it, if you see one. Rule: CONFIRM / CORRECT (with the
corrected numerator) / UNDERDETERMINED (with what would decide).

**Q2 — The identification.** Is K̄ (the Markovian weight of the Sea
response kernel) the same object as the pinned SF-6 coefficient (P3)?
If yes: state the verification computation that would check it
numerically (inputs, output, tolerance). If no: state what K̄ is
instead, and what the SF-6 term then represents in the kernel picture.

**Q3 — The cancellation structure.** Does the zero-integral split (P5)
correctly express P4 — i.e., does F_res couple at leading order to
dv/dt (vanishing for uniform motion), and is the transverse-sector
conditional the ONLY failure mode that restores an O(v/c) term? If
other failure modes exist, name them.

**Q4 — LEG B route.** The ambient v/c bound must not use automaton
regime-artifact values [K4]. Three candidate routes: (a) the ring's
own pinned internal dynamics from the promotion computation; (b)
Sea-parameter lineage (λ̄_C/d_DP = 1061); (c) observational ceiling
from DM virial kinematics (~10⁻³ c). Which velocity is the physically
operative one for the ring's regime, and which route bounds it without
circularity? If the record underdetermines this, say so — it then goes
to the founder as a physical-picture question.

## EXECUTION KEY EK-1 (mandatory; distinguishes execution from reading)

For the exponential kernel K(τ) = (K̄/τ_K) e^(−τ/τ_K) and the test
velocity v(t) = v₀ sin(ωt), at ωτ_K = 0.30 exactly, compute:
(i) the amplitude ratio of the full memory force ∫₀^∞ K(τ) v(t−τ) dτ
to the Markovian force K̄ v(t), to 4 significant figures;
(ii) the phase lag in degrees, to 2 decimal places.
Return as the exact string: `ratio=X.XXXX;phase_deg=YY.YY`

**The answer appears nowhere in this packet, the linked corpus, or any
published document. Its SHA-256 is sealed here for verification:**

    16986c38d6cebec6f395c19d29944710ba25f3bf1bc76885a02b83857d3880ba

A return whose string hashes to this value earns execution credit; a
return that does not is answered-unverified regardless of prose
quality. (This closes the 2813/2838 defect class: the key value cannot
be read because it is not written anywhere in the clear.)

## RETURN FORMAT

Per seat: Q1 ruling + reasoning (≤300 words); Q2 ruling + verification
spec; Q3 ruling + failure-mode list; Q4 route + argument (≤200 words);
EK-1 string; declared sources. No ledger movement is authorized by any
return; adjudication is a separate patch.
