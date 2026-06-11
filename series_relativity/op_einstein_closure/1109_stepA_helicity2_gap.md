# Step (a) entry — GR-recovery localized to the helicity-2 (tensor GW) sector (Patch 1109)

**Arc:** `series_relativity/op_einstein_closure/` · **Charter:** `README.md` · **Verify:**
`code/1109_stepA_helicity_decomposition.py`
**Result:** the `op:einstein` summit — does c08's `F` recover the full Einstein tensor? — is
**localized** to a single, well-posed, falsifiable question: does the lattice produce the two
**helicity-±2** (the `+`, `×`) gravitational-wave polarizations? c08's LSP content (scalar + vector)
sources them as **identically zero**. **op:einstein NOT closed; c08 NOT falsified** (its tensor modes
are attributed to companion 7 §6, not audited here). **NO VERDICT MOVED.**

## The degrees-of-freedom probe (the cheapest way (a) could fail)
c08's field equation is a single **scalar** equation; Einstein's is a **tensor** (10). The metric map
(c08, companion 7 Prop 2.1) is explicit: `|SSV|_abs → g_tt` (a scalar) and `SSV_net → g_ij` (a
vector). So the LSP's dynamical content is **one scalar + one vector field** — there is no rank-2
(spin-2) field named to carry GR's two propagating tensor polarizations. The cheapest test of (a):
can a scalar+vector source the helicity-±2 GW modes at all?

## The computation (`code/1109_stepA_helicity_decomposition.py`)
For a plane wave propagating in `z`, the most general symmetric spatial perturbation a scalar `S`
(`= |SSV|_abs`) and vector `V_i` (`= SSV_net`) can build (up to gradients) is:
- helicity-0 (trace): `h_xx = h_yy = A·S`;
- helicity-0 (longitudinal): `h_zz = A·S + B·S'' + C·V_z'`;
- helicity-±1 (transverse shear): `h_xz = C·V_x'/2`, `h_yz = C·V_y'/2`;
- **helicity-±2 (the GR `+`, `×` modes): `h_xx − h_yy = 0` and `h_xy = 0` — identically.**

The transverse-plane quadrupole (`h_xx−h_yy`, `h_xy`) that *is* the GW `+`/`×` signal has **no source**
in a scalar+vector LSP. This is not a coincidence of the ansatz: a vector displacement field's elastic
strain `∂_(i u_j)` for a `z`-wave yields only `h_iz` components (helicity 0, ±1) — never the
transverse-plane quadrupole. Helicity-±2 requires a genuine rank-2 (spin-2) source.

**Consistency check:** the c08 Schwarzschild theorem's spatial metric is `g_ij = (1+ϱ)⁴ δ_ij` —
**conformally flat**, i.e. pure trace (helicity-0), zero helicity-2 content. The static success and
the radiative gap are the same fact: c08's demonstrated metric structure is scalar/vector, not tensor.

## What this means for op:einstein (honest)
- **Scalar + vector sectors:** c08 reproduces GR — Schwarzschild *exactly* (the conformally-flat
  isotropic form), Newtonian + leading PN (scalar potential), and plausibly gravitomagnetic
  frame-dragging (the vector `SSV_net`; c08 calls Kerr "qualitative").
- **Spin-2 (helicity-±2) sector:** the GR tensor GW polarizations are **not sourced** by the LSP's
  scalar+vector content. c08 *asserts* "the tensor modes reproduce GR exactly (companion 7 §6)" with
  scalar/vector modes suppressed by `(l_P/λ)² ≈ 10⁻⁷⁶`, but the metric map shown carries no helicity-2
  d.o.f. to substantiate that assertion.

**So `op:einstein`'s (a) reduces to one sharp, well-posed question:** *does companion 7 §6 genuinely
produce two helicity-±2 modes from the 600-cell lattice — i.e. a rank-2 dynamical degree of freedom
beyond the scalar+vector metric map — or only the helicity 0/±1 modes that content supports?* That is
the true summit, now precisely located.

## Why this is decidable (and a real prediction)
The fork is **falsifiable by data**: GR predicts pure helicity-±2 GW polarizations, and LIGO/Virgo
polarization tests are consistent with tensor modes and constrain scalar/vector admixtures. If
companion 7 §6 cannot produce helicity-±2, c08 is in tension with GW observations; if it can (a
genuine lattice spin-2 mode), (a) is substantially closed. Either way the question is empirical, not
merely formal.

## Honest status / residual
- **Not a closure, not a falsification.** This locates the summit and shows the c08-level metric map
  cannot carry it; the definitive statement requires **auditing companion 7 §6's tensor-mode
  derivation** — the recommended next pitch.
- The cosmological mode remains in SR-5 (separate).
- **Owed (shared-registry, STOP-and-warn, not done here):** a frontier note flagging (i) the
  helicity-2/companion-7-§6 question as the located `op:einstein` summit, and (ii) the GW-polarization
  content as a falsifiable CPP test — coordinate as an INT patch.

## Cap status update
After 1107 (b) + 1108 (b′), the excess-sourcing/inert-Sea half is conditionally closed and grounded in
600-cell symmetry. After 1109, the remaining cap — the nonlinear GR-recovery (a) — is no longer a
vague "does `F` → Einstein" but a **single localized, falsifiable question** (the helicity-±2 sector /
companion 7 §6). The CC reconciliation's honest grade is unchanged (conditional on (a)), but (a) is now
mapped to its true summit.
