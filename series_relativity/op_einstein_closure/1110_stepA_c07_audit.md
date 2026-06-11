# Step (a) — Audit of companion 7 §6: the helicity-2 modes are asserted, not derived (Patch 1110)

**Arc:** `series_relativity/op_einstein_closure/` · **Charter:** `README.md`
**Result:** c08 attributed the GR tensor GW polarizations to "companion 7 §6." Auditing c07 §6: it
**does not derive them from the LSP** — it writes the standard GR wave equation and invokes "the
transverse-traceless gauge," while its own metric map sources `h_ij` from the gradient of a vector
(no helicity-2 content). c07's own open-problems list concedes full tensor recovery is unproven.
**op:einstein (a) is genuinely OPEN; the gap is now pinned to a precise missing ingredient.** c08/c07
are **not** thereby falsified — the fix is identifiable. **NO VERDICT MOVED.**

## What c07 §6 actually contains
1. **Metric map (c07 eqs. for `g_tt`, `g_ij`):**
   `g_tt = 1 − kΔ|SSV|_abs` (scalar source) and
   `g_ij = δ_ij + k·|∇SSV_net|_ij` — the spatial perturbation is the **spatial gradient tensor of the
   vector `SSV_net`**, `h_ij ∝ ∂_i(SSV_net)_j`. c07 (Remark "metric mapping is forced") fixes this by
   the equal-magnitude constraint `|h_tt| = |h_rr|` from the single coupling `k = l_P³/E_P`.
2. **GW section (c07 §6):** asserts GWs are "perturbations of the 600-cell lattice geometry, sourced by
   time-varying mass-energy quadrupoles," with `|SSV|_abs` and `SSV_net` "jointly perturbed in the
   transverse-traceless gauge," and writes the **standard GR linearised wave equation**
   `□h̄_μν = −(16πG/c⁴)T_μν`, noting solutions propagate at `c` (consistent with LIGO/Virgo/KAGRA).
3. **Open-problems list:** problem #1 — "Full nonlinear Einstein equations… requires proving
   convergence of the discrete lattice sum to a smooth Riemannian manifold." Full tensor (Ricci)
   recovery is explicitly listed as **unproven/open**.

## The audit finding
c07 §6 **does not bridge the helicity-2 gap**; it asserts the GR tensor wave equation while its own
metric map provides only scalar + gradient-of-vector content:

- The TT (helicity-±2) part of `h_μν` — the actual GR `+`/`×` radiation — is **gauge-invariant**.
  Invoking "the transverse-traceless gauge" cannot create TT content that the source lacks; a gauge
  choice removes unphysical parts, it does not add physical modes.
- c07's metric map defines `h_ij` as `∂_i(SSV_net)_j` (gradient of a vector). By the 1109 helicity
  computation (`code/1109_stepA_helicity_decomposition.py`), for a transverse wave this populates only
  helicity 0 and ±1 — `h_xx−h_yy = 0`, `h_xy = 0`. **No helicity-2.** So `h_μν` as *defined by c07's
  own map* cannot satisfy the radiative content of the `□h̄_μν` equation it writes.
- Internal inconsistency in the radiative sector: c07 §6's wave equation treats `h_μν` as a full
  independent tensor field (which has TT modes), but c07's metric map defines `h_μν` as a derived
  scalar+vector object (which has none). The two are incompatible for gravitational radiation.
- c07's own open-problems list concedes the full tensor recovery is unproven — consistent with this
  audit.

**Verdict:** the helicity-2 tensor GW modes are **asserted** (by writing the GR equation), **not
derived** from the CPP LSP/lattice structure. c08's appeal to "companion 7 §6" does not substantiate
its claim that "the tensor modes reproduce GR exactly."

## What this means for op:einstein (the honest summit assessment)
**(a) does not close.** The precise, pinned obstruction: **the LSP has no rank-2 (spin-2) degree of
freedom.** Its content is one scalar (`|SSV|_abs`) + one vector (`SSV_net`), and the metric map sends
them to `g_tt` and to `∂_i(SSV_net)_j` respectively. GR's propagating radiation lives in the
transverse-traceless (helicity-±2) sector, which neither source can populate. So the CPP field
equation + metric map, as currently defined, is a **scalar–vector theory of gravity**: exact in the
static/Newtonian sector (Schwarzschild, time dilation), plausibly correct in the gravitomagnetic
sector (frame-dragging from `SSV_net`), but **missing the spin-2 radiative sector**.

## The fork (honest, and it is empirical)
1. **Fix:** extend the LSP/broadcast with a genuine **spin-2 (rank-2) degree of freedom** — a lattice
   shear/strain mode that carries the transverse-traceless quadrupole. Closing op:einstein's (a)
   *requires* this; it is now a concrete, well-posed construction task, not a fog.
2. **Tension:** until such a d.o.f. exists, CPP cannot produce the tensor GW polarizations that
   LIGO/Virgo/KAGRA observe (their signals are consistent with GR's two tensor modes; non-tensor
   admixtures are bounded). c08's claim that the tensor modes are present and the scalar/vector modes
   are suppressed by `(l_P/λ)² ≈ 10⁻⁷⁶` is **inverted** by this audit: it is the *tensor* modes that
   are currently unsourced. This is a real, standing tension with GW data — not a fatal one (the fix
   in (1) is available), but it must be stated plainly.

## Status / owed
- **op:einstein (a): OPEN**, gap pinned (no spin-2 d.o.f.); the dark-sector cap therefore **stands
  open** at (a). The excess-sourcing half (b/b′) remains conditionally closed and grounded in 600-cell
  symmetry; the CC reconciliation's honest grade is unchanged (conditional on (a)), with (a) now
  fully mapped: it is the spin-2 construction problem.
- **NOT a falsification of CPP** — it is a precise identification of a missing structural ingredient
  and the construction needed to supply it.
- **Owed (shared-registry, STOP-and-warn, INT patch):** frontier note recording (i) op:einstein (a)
  gap = missing spin-2 d.o.f. in the LSP; (ii) the GW-polarization tension as a falsifiable test and
  the spin-2 lattice-mode construction as the path to close (a). Coordinate with SR.md OPEN-SR-5.

## Bottom line of the climb
We reached the summit's true face. `op:einstein` is a genuine open problem, and we now know **exactly
why**: the CPP broadcast carries scalar + vector data but no spin-2 mode, so it reproduces gravity in
every sector *except* the transverse-traceless radiation that GR observations confirm. Closing it is a
specific, nameable construction (a lattice spin-2 mode), and the GW-polarization data is the test that
keeps it honest.
