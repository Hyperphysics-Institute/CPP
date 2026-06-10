# No near-threshold resonance in the qDP/hTetra residual color potential — the σ/m kill is excluded structurally

**Patch:** 0831 (Session 156, 10 June 2026) · **Type:** first-pass computation / scaffold (NOT a closure, two-body s-wave) · **Lane:** DM-2 / `dark_matter/`.
**Closes (first-pass):** the no-near-threshold-resonance condition flagged by 0830 ("next layer") and **Step-1's stated kill condition** (open problem #2: a near-threshold bound state in the residual potential lifts σ/m by ~10³). **Verify:** `code/0831_qdp_residual_resonance.py`.

---

## The question

Step-1 named the one thing that could break the qDP/hTetra-as-DM identification: if the residual (van-der-Waals-like) color potential between two color-neutral qDPs supports a **near-threshold bound state**, the scattering length `a` diverges, `σ = 4πa²` blows up, and σ/m exceeds the SIDM bound by orders of magnitude. The geometric model (0830) cannot see this — it needs the actual two-body quantum scattering problem.

## The calculation

Residual color potential between two neutral qDPs (the color analog of the nuclear force between color-neutral nucleons): a **hard core** at `r_c` (the eDP excluded-volume coat) plus an **attractive color Yukawa** outside, range `λ` (set by the mediating DP scale), depth `V₀`. Solve the zero-energy s-wave radial Schrödinger equation `u'' = (2μ/ℏ²)V(r)u`, `u(r_c)=0`, two equal masses `m_qDP = 0.30 GeV`, and read the scattering length from the linear asymptote `u → C(r − a)`. Representative scales `r_c = 1.0 fm`, `λ = 1.3 fm` (hDP). Sanity: `a(V₀=0) = 1.000 fm = r_c` (hard sphere) ✓.

**Scattering length and σ/m vs the attraction depth** (depth as a fraction `f` of the qDP internal binding `E_qDP = 264 MeV`):

| f | V₀ [MeV] | a [fm] | σ/m [cm²/g] | |
|---|---|---|---|---|
| 0.00 | 0 | 1.00 | 0.235 | OK |
| 0.05 | 13 | 0.93 | 0.204 | OK |
| 0.10 | 26 | 0.86 | 0.173 | OK |
| 0.20 | 53 | 0.71 | 0.117 | OK |
| 0.50 | 132 | 0.14 | 0.004 | OK |
| **1.00** | **264** | **−1.47** | **0.504** | **OK** |

**Kill features (require V₀ > E_qDP — unphysical for a residue):** σ/m crosses the SIDM bound at V₀ ≈ 300 MeV (V₀=320 → σ/m=1.69), and the resonance pole (`a → ∞`, the near-threshold bound state) sits at V₀ ≈ 500 MeV (V₀=480 → σ/m=75, `a`=−17.9 fm).

## The result — the ordering does the work

```
   residual depth (≤ E_qDP = 264)   <   σ/m = SIDM crossing (~300)   <   resonance pole (~500)   MeV
```

The residual color attraction between two **neutral** qDPs is the van-der-Waals **residue** of each qDP's own internal color binding `E_qDP = 264 MeV`. A residue is weaker than the binding it derives from — the internal charges are screened/saturated within each qDP, exactly as the nuclear force (~50–100 MeV well) is a small fraction of the GeV-scale internal quark binding. So **the physical residual depth is bounded above by E_qDP = 264 MeV**, and in that entire range σ/m stays at or below 0.504 cm²/g — below the SIDM bound. The near-threshold resonance, and even the bare σ/m=SIDM crossing, require an attraction *deeper than the qDP's own binding*, which a residue cannot reach.

So the no-near-threshold-resonance condition is satisfied **structurally, not by fine-tuning**: the kill is excluded by the residual-force hierarchy (residual < constituent binding < resonance onset), and it holds even in the unphysical worst case where the residual equals the full internal binding (f=1 → σ/m=0.50, still ×2 below SIDM). At a realistic residual fraction (f ~ 0.05–0.2 by the nuclear analogy) the scattering length is ~range (0.7–0.9 fm) and σ/m ~ 0.12–0.20 — well inside the bound and far from any resonance.

This also reconciles the σ/m story across the arc: Step-1's bare-geometric `4×10⁻³ cm²/g` was an underestimate (sub-fm size); 0830's eDP-coated value pushed σ/m up *near* the bound; and 0831 shows the scattering-theory value lands at ~0.1–0.5 cm²/g across the physical depth range — near the bound for a full-binding residual, comfortably under for a realistic one — with the catastrophic ~10³ lift structurally out of reach.

## What it rests on (firm-up path)

- **The residual depth fraction `f`** is the input. The bound `f ≤ 1` (residual ≤ internal binding) is the load-bearing physical claim; the realistic `f ~ 0.1` comes from the nuclear analogy, not yet a CPP derivation. Even `f=1` is safe here, so the conclusion is robust to this, but a derived `f` would firm the margin.
- **Scale-dependence.** The SIDM-crossing and pole positions move with `r_c`, `λ`, and `m_qDP`; a larger coat or longer range lowers the crossing toward 264, a heavier constituent (hTetra 1.5 GeV) raises it (σ/m ∝ 1/m). Representative hDP-scale values are used; the ordering holds for them with the worst-case margin quoted.
- **Two-body s-wave.** Identical-qDP statistics (symmetrization, possible internal d.o.f.) and higher partial waves are refinements; the cold-DM regime is s-wave dominated, so this is the right leading channel.

## Scope

First-pass / scaffold. **Not a closure, no THEO/ID, no verdict.** Two-body s-wave scattering with a hard-core + Yukawa residual potential; closes 0830's flagged no-resonance "next layer" and resolves Step-1's kill condition first-pass. Hybrid (gravity drives the diffuse halo; this governs the dense-core microphysics). Conditional on the qDP/hTetra-DM conjecture and the Mechanism-A measure.
