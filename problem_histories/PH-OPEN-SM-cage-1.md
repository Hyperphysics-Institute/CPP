# Problem History: OPEN-SM-cage-1 — Derive the Scaling Exponent α = 2.38

**Created:** April 2026 (SM-8/SM-9 sessions)
**Status:** OPEN
**Research_Frontier.md entry:** OPEN-SM-cage-1

---

## The Problem

SM-8 Theorem 6.1 shows that M_q = m_e(z/φ)V^(7/3) × [1 or 16] predicts all four heavy quark masses to 2.1% RMS. But the exponent α = 7/3 ≈ 2.33 (calibrated as α = 2.38 from s→c) is not derived — it is fitted.

Deriving α from 600-cell geometry would convert the quark mass prediction from "calibrated coherence" to a genuine zero-parameter derivation.

---

## The Journey

### April 2026 — Calibration from s→c

The power law m ~ V^α was calibrated from the strange-to-charm ratio: (12/4)^α = m_c/m_s. This gives α ≈ 2.38. The same exponent then predicts m_b and m_t to 3% and 0.02% respectively.

### April 2026 — CONJ-SM9-1: α = 7/3 from Pair Counting

SM-9 proposes a partial derivation: α = 7/3 from V² × V^(1/3), where V² comes from pair counting (the number of DP-DP interactions scales as V²) and V^(1/3) comes from the linear cage dimension (energy per pair scales with cage radius).

**Status:** Partially derived. Full rigorous derivation from DP dynamics pending SM-10 FEM.

### April 2026 — The Spectral Dimension Dead End

Copilot proposed that α might equal the spectral dimension d_s of the cage subgraph. Opus computed d_s on the 63-vertex cage subgraph (CPU): d_s ≈ 2.26–3.12 (window-dependent). Copilot computed d_s on a 2-ring tessellation (GPU): d_s ≈ 3.55. Conclusion: d_s ≠ α.

---

## What Remains

The FEM simulation (OPEN-SM-10-FEM) is the leading candidate approach. If DP chain dynamics produce V^(7/3) scaling from first principles, α is derived.

---

## Cross-References

- **Research_Frontier.md entry:** OPEN-SM-cage-1
- **Related:** OPEN-SM-10-FEM (FEM approach), CONJ-SM9-1 (partial derivation), FALS (spectral dimension route)
- **Development transcripts:** SM-8 transcript (Phase 8), SM-9/SM-10 transcript

---

*Stub created 12 April 2026. Needs enrichment from SM-8 Phase 8 transcript and SM-9 development sessions.*
