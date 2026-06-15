# Problem History: OPEN-FP-3-CKM — Substrate-derivation of the quark mixing matrix and quark CP phase

**Created:** 14 June 2026 (registered at SF-3 v1.0 SHIP, Session 161, Patch 1506)
**Status:** OPEN — registered open frontier at SF-3 v1.0 SHIP; candidate closure route flagged, unscoped
**frontier_sectors entry:** OPEN-FP-3-CKM (`frontier_sectors/FP.md`)
**Target paper:** SF-3 v1.x revision OR a dedicated quark-mixing paper
**Parent paper:** SF-3 v1.0 SHIPPED 14 June 2026 (Session 161, Patch 1505)

---

## The Problem

Derive from CPP primitives the Cabibbo–Kobayashi–Maskawa (CKM) mixing angles and
the quark CP-violating phase. These have no derivation anywhere in the CPP quark
corpus.

### Mechanism context (SF-3 v1.0)

SF-3 consolidates the shipped quark-sector results (SM-7/8/9/10, SS-1/2, SM-6)
into a single account: the heavy-quark masses from the cage formula
`M_q = m_e (z/φ) V^{7/3}` (RMS 2.1%, single `m_e` calibration, `m_c` demoted to
derived), the strong coupling `α_s = 5/(8φ)` with the complementarity
`sin²θ_W + α_s = 1/φ`, the quark Koide phase 124.04° (0.05%), and the
three-generation count selected within the SM-8 antipodal-identification model.

What SF-3 does **not** deliver is the quark mixing sector. SM-10, despite an
incidental mention, is the finite-element scaling-mechanism paper, not a mixing
paper. So SF-3 derives the quark *masses* and the generation count at zero
parameters but leaves the CKM mixing angles and the quark CP phase undelivered.

### Closure route

A candidate route — flagged at SHIP, not pursued — is a quark-sector cage-mixing
structure analogous to SM-5's K₃ → tri-bimaximal derivation of the PMNS matrix in
the neutrino sector. The CKM analog of that spectral-alignment mechanism is
presently **unscoped**. A first scoping task would be to ask whether the four
bonded quark cages admit a cross-cage alignment structure (analogous to the K₃
eigenmode alignment that fixed the neutrino mixing) and whether that structure
produces a non-trivial CP phase.

### Open remarks

- **Structural parallel to the open neutrino δ_CP (posture, not difficulty).**
  SF-4 ships seven of eight neutrino parameters with δ_CP deferred; SF-3 ships
  the quark masses and generation count with CKM deferred. The two flagships
  share a "masses derived, mixing-sector open" posture. This is a parallel of
  posture, NOT an equivalence of difficulty or status.
- **Low cross-window collision risk.** The quark CP phase inside CKM is a
  *separate object* from the neutrino δ_CP pursued in the dedicated δ_CP window;
  it is not that window's territory.
- **Falsification route (eventual).** A derived CKM structure disagreeing with the
  measured mixing angles or the Jarlskog invariant would falsify the mechanism.

---

## Timeline

- **14 June 2026 (Patch 1506):** registered OPEN at SF-3 v1.0 SHIP; candidate
  closure route (SM-5 K₃ → TBM analog) flagged as unscoped.
