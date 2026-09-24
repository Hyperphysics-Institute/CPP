# The Frame at Lattice Size: g_A and r_p Both Within ~2% Across the Whole Allowed Stretch — CONVENIENT, FOR CRITIC

**Patch:** 4274. **Lanes:** EW → strong and foundations (4273 owed (a)). **Session:** 239.
**Verify:** `series_standard_model/code/4274_frame_at_lattice_size.py`. **Status:** result stated; the whole chain is
submitted for critique (PD-008) before anything downstream is changed.

## 1. The argument

1. **The fractional charges barely affect the frame.** In SS-2's u–u balance, V = [4α/9 − (2/3)α_geom + 1]ħc/r +
   (σ/2)r, the fractional-charge term is 0.4% of the bracket. So 4273's pointer at fractional charges was wrong in
   emphasis (corrected here); integer charges change the frame by about 0.3%. Separately, SS-2's displayed r_eq
   formula has a spurious factor 2 inside the root; its 1.071 fm is the value without it.
2. **The dominant term is double counting.** The bracket is dominated by "+ħc/r", which SS-2 labels the relativistic
   kinetic (uncertainty) energy of the pair. Since 4243 that kinetic energy has been carried *explicitly* by the ZBW
   breath modes. Keeping +ħc/r in the frame balance counts it twice.
3. **Without it, the frame is held by the hTetra's own bonds.** Remove the term and the balance has no repulsion
   left beyond the tiny EM one. The frame is then held by its bonds: the attractive u–d (−/+) edges at the lattice
   edge l_edge = l_unit/φ = 0.364 fm (SS-2), and the repulsive u–u (−/−) edge pushed open by like charge, somewhere
   between l_edge and 2 l_edge.
4. **Scan the whole allowed stretch; choose nothing.** SS-2's own shape ratio (1.071/0.620 ≈ √3, a 120° apex) is one
   point in the range.

## 2. Rows verbatim (D-11)

```
l_edge = 0.3640 fm;  SS-2 frame (u-u 1.071, u-d 0.620) for reference:
  SS-2 frame: r_p=0.9382 (+11.6%)  g_A=1.2954 (+1.6%)

u-d = l_edge; u-u stretched across its allowed range:
  u-u = 1.200 l_edge (0.437 fm): r_p=0.8232 ( -2.1%)  g_A=1.2609 ( -1.1%)  m_q(mu_p)=294.9  mu_n=-1.867 ( -2.4%)  overlaps x 0.81 p 0.80
  u-u = 1.500 l_edge (0.546 fm): r_p=0.8289 ( -1.4%)  g_A=1.2685 ( -0.5%)  m_q(mu_p)=295.8  mu_n=-1.866 ( -2.5%)  overlaps x 0.73 p 0.71
  u-u = 1.732 l_edge (0.631 fm): r_p=0.8394 ( -0.2%)  g_A=1.2759 ( +0.0%)  m_q(mu_p)=296.6  mu_n=-1.864 ( -2.6%)  overlaps x 0.68 p 0.63  <- SS-2's shape (120 deg)
  u-u = 1.900 l_edge (0.692 fm): r_p=0.8487 ( +0.9%)  g_A=1.2822 ( +0.5%)  m_q(mu_p)=297.3  mu_n=-1.863 ( -2.6%)  overlaps x 0.64 p 0.58
  u-u = 2.000 l_edge (0.728 fm): r_p=0.8550 ( +1.7%)  g_A=1.2861 ( +0.8%)  m_q(mu_p)=297.8  mu_n=-1.863 ( -2.6%)  overlaps x 0.61 p 0.55

-> With the double-counted kinetic term removed, the frame sits at lattice size, and across the WHOLE allowed u-u
   stretch both r_p and g_A stay within about 2% of measured, with no parameter chosen; SS-2's own shape gives
   r_p -0.2%, g_A 0.0%.  Overlaps are large (0.6-0.8), so the Gaussian exchange is at its roughest here.
```

## 3. Result

Across the entire allowed u–u stretch, **r_p = 0.823–0.855 fm (−2.1% to +1.7%)** and **g_A = 1.261–1.286 (−1.1% to
+0.8%)**, with no parameter chosen. At SS-2's own shape: **r_p = 0.8394 fm (−0.2%), g_A = 1.2759 (0.0%)**. μ_p fixes
m_q ≈ 295–298 MeV, and μ_n is then −1.864 (−2.6%). The 4272–4273 frequency tension disappears: it came from SS-2's
frame being too large, and route (H) now serves both observables.

## 4. PD-008 — why this is marked for critique, not adopted downstream

This is the most convenient result of the session. It closes both observables, so the weak points are listed here
for the next context window to press:

- **The double-counting argument (§1.2)** carries everything. Is SS-2's ħc/r really the same energy as the breath's?
  The breath is each quark's motion about its seat; ħc/r was the pair's localisation energy at separation r. They
  overlap in meaning, but whether exactly, or only partly, is the question.
- **The Gaussian exchange at overlaps of 0.6–0.8** is at its roughest. Seats that close are barely distinct.
- **The r_p model** uses SS-2's formula, centroid origin, δ = 0, and no finite size for the CPs themselves.
- **l_edge = 0.364 fm** comes from SS-2's lattice unit, which is anchored to Λ_QCD. It is an input, not a CPP
  derivation.
- **g_A is only weakly sensitive to the frame** (it changes 2% across the range). Its agreement is therefore modest
  evidence. r_p is the discriminating observable, and it is the one resting on the coarser model.

## 5. Downstream, if it survives critique

SS-5, SS-6 and SS-9 use SS-2's 1.07/0.62 fm geometry, and SS-2's own r_p (+5%) and ε = 1.94 would change. All are
filed and **held**; nothing is changed until the critique.

## 6. Founder question (a physical picture)

Is the proton's hTetra frame about the size of one lattice cell, with the up–down bonds at the ordinary lattice
spacing (≈ 0.36 fm) and the two ups pushed only somewhat further apart? Or is the whole frame stretched to about
1.7–3 times that, as SS-2 has it (up–down 0.62 fm, up–up 1.07 fm)?
