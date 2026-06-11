# Spin-2 Step 6 — THE THIRD ASSAULT: the non-radiality (PSR-hop twist) re-run — verdict survives; the twist is channel optics, and the absolute frame is what keeps the broadcast massless (Patch 1119)

**Sub-arc:** `series_relativity/op_einstein_closure/spin2_construction/` · **Charter:** `README.md`
· **Verify:** `code/1119_step6_connection_covariant_modes.py`
**Architect's mechanism (Thomas, 11 June 2026):** the 600-cell's GPs are not radially aligned
with any propagation direction — each GP has 12 icosahedrally-arranged nearest neighbors, so
every GP→GP hop (one full PSR increment, l_P) requires *an incremental turn* to select the
neighbor. Over a GW's traversal of many light-years, this per-hop tangential/rotational element
accumulates. Could the twist place an effective spin bit on the GP→GP signal — opening the
helicity-±2 channel that 1116 found missing?
**Why this is a genuine third assault:** the 1116 dynamical matrix coupled neighbors with
*scalar coefficients only* (`λ δ_ab + μ n_a n_b`) — **no per-edge transport rotation anywhere
in the calculation**. The twist mechanism, formalized as a *discrete connection* (a per-edge
transport operator `R_j` applied to the carried data on every hop), was genuinely untested.
**Result — the verdict survives, for three independent reasons, and the run pays for itself
with new physics:** the twist cannot raise the rank of the carried data (representation bound);
if it acted on the data it would *gap the vector sector at the Planck scale* (empirically
excluded to ~10⁻⁴⁶) and add circular birefringence — *channel optics*, not new helicity; and
the empirically-forced flat connection is exactly the regime 1116 computed. **Option D remains
RULED OUT. The spin-bit axiom remains NECESSARY. NO VERDICT MOVED.**

---

## 1. Formalizing the mechanism: the twist is a discrete connection

The non-radiality is real as *path geometry*: a message crossing the lattice hops along edges
that each deviate from the straight-line path. The question is whether that geometry acts on
the *carried data*. The general formalization: each hop along edge `n_j` applies a transport
operator `R_j` (a rotation fixed by the edge geometry) to the broadcast `(|SSV|_abs, SSV_net)`
— a **discrete connection** on the (scalar, vector) bundle over the lattice. The
connection-covariant dynamical matrix is

> `D(k) = Σ_j [ T₀ − e^{i k·n_j} T_j ]`,  `T_j = blockdiag(1, R_j)` (+ mixing on the
> transported vector), with antipodal consistency `R_{−j} = R_jᵀ` (hopping back undoes the
> turn), which makes `D(k)` Hermitian.

The icosahedrally-equivariant connections form a **one-parameter family**: `R_j(θ)` = rotation
about the edge axis `n_j` by angle θ (the only per-edge axis available is the edge direction
itself). The geometric 4D value, if the data were transported quaternionically along a 600-cell
edge (adjacent vertices subtend 36° on S³), is **θ = π/5**. We also test *arbitrary* per-edge
rotations and full O(4) transports (slam-the-door).

## 2. The representation bound (P1) — why no connection can open the channel

The carried space per hop is `(φ, V)` — 4 real components. Under rotations about the
propagation axis `k̂`, its J_z (helicity) spectrum is **{0, 0, +1, −1}**; the character is
`χ(α) = 2 + 2cos α`, whose overlap with the helicity-±2 character `e^{±2iα}` is **exactly
zero** (verified numerically to 10⁻¹⁶). The helicity-±2 projector on this space is
*identically zero*. Since every transport operator is a rotation — and **rotations are
irrep-preserving** — no connection acting within this space can create helicity-±2 content,
for any dynamics whatsoever. **A twist reorients vector components; it cannot raise rank.**
This single bound covers the equivariant family, arbitrary SO(3) connections, and full O(4)
transports mixing φ↔V (the space is still 4-dimensional).

Two nearby loopholes, re-checked: gradient composites `k_(a V_b)` carry m ∈ {0, ±1} only
(k along z is m=0); the bilinear `V_a V_b` *does* reach m=±2 but at second order in amplitude
and double frequency — that is 1115's exclusion, unchanged. The *linear* GW strain (m=±2,
first order, source frequency) has no carrier.

## 3. What the twist actually does (P2) — the new physics

Building `D(k)` explicitly with `R_j(θ)` (verify script, all formulas confirmed numerically to
machine precision):

- **A Planck-scale gap.** `D(0) = Σ_j (I − R_j(θ)) = 16 sin²(θ/2) · I` on the vector block
  (using `Σ_j R_j(θ) = (8cosθ + 4)I` by icosahedral symmetry). A nonzero twist **gaps the
  helicity-0/±1 vector modes at mass M = 4|sin(θ/2)| in Planck units** — destroying long-range
  propagation. The twist does not add a mode; it *kills* the modes already there.
- **Circular birefringence.** The O(k) term is `−4i sinθ [k]_×`, a chiral term splitting the
  transverse doublet: `ω²_± = M² ± 4 sinθ·k + c²k²`. Note `[k]_×` *is* the J_z generator —
  the term is m-diagonal, so it splits the ±1 modes but moves no weight toward ±2. The twist
  is **channel optics** (gap + optical activity on what is sent), not new radiative content.
- **Helicity content at every θ:** all four branches remain m ∈ {0, 0, +1, −1}; the m=±2
  weight is machine-zero (≤ 10⁻¹⁵) across the equivariant family and across 200 random
  antipodal-consistent SO(3) connections.

A physical way to see the whole result: the lattice twist is **static — a property of the
channel, not the signal**. The detected strain oscillates at ~10²–10³ Hz with the source's
quadrupole; a fixed geometric twist accumulated over light-years can rotate or birefringe what
was radiated, but cannot add first-order oscillating rank-2 content that was never sent.

## 4. The empirical bound (P3) — the absolute frame is doing real work

If the PSR-hop twist acted on the carried data, the vector sector would be massive:
M = 4|sin(θ/2)| ≈ 2θ Planck masses. Long-range propagation bounds force:

| Constraint | Bound on θ |
|---|---|
| photon mass < 10⁻¹⁸ eV | θ < 4×10⁻⁴⁷ rad |
| graviton mass < 1.2×10⁻²² eV (LIGO) | θ < 5×10⁻⁵¹ rad |
| geometric 4D value θ = π/5 (quaternionic edge transport) | M ≈ **1.24 Planck masses** — maximally excluded |

So the connection on the broadcast data must be **flat** (pure gauge) to ~10⁻⁴⁶ — i.e.
effectively exactly `R_j = I`. **And CPP already says why:** the substrate has an absolute
(Nexus) frame; the broadcast components are stated in the universal lattice frame, not
parallel-transported through each edge's local geometry. The non-radial path geometry shows up
in *which* neighbor is selected (the `e^{ik·n_j}` factors — fully present in 1116), not in a
rotation of *what is carried*. **This is a consistency point in CPP's favor: the absolute-frame
axiom is not decoration — it is precisely what keeps the broadcast massless and long-range.**
A relationalist lattice theory that transported data through local edge frames at the geometric
θ = π/5 would be dead on arrival.

## 5. Verdict and the state of the wall

- **The non-radiality twist does NOT evade 1116.** Three independent closures: (i) the
  representation bound — no connection raises rank; (ii) a data-acting twist Planck-gaps the
  vector sector, excluded to 10⁻⁴⁶–10⁻⁵¹; (iii) the empirically-forced flat connection is
  exactly the calculation 1116 already did.
- **Option D (emergent / no-new-axiom) remains RULED OUT — now after THREE assaults:** the
  linear map and bilinears (1115), the collective-mode spectrum (1116), and the architect's
  non-radial connection (1119, this step). Each closed for a stated structural reason. The
  spin-bit axiom (A/B/C) remains **NECESSARY**, and the "convenience patch" objection is now
  answered at its strongest: the architect's own best remaining no-axiom mechanism was
  formalized in its most general form and run to ground.
- **Byproducts banked:** (1) the lattice-connection gap formula `M² = 16 sin²(θ/2)` and the
  chiral birefringence law `ω²_± = M² ± 4 sinθ·k` — a quantitative constraint making
  *flat carriage* (absolute-frame transport) an empirical necessity, not a stylistic choice;
  (2) a sharpened statement of what the Nexus/absolute-frame axiom buys physically. The chiral
  O(k) term is also noted as a *potential future hook* for the chirality lane (a θ-twist is a
  natural substrate-chirality order parameter whose empirical ceiling is now known to be
  10⁻⁴⁶–10⁻⁵¹) — flagged as a DIRECTION, not a claim; no cross-lane file touched.
- **NO VERDICT MOVED:** no THEO/PRED registered, no count change; `op:einstein` (a) remains
  OPEN pending the axiom choice. The construction tasks (flow choice, axiom text, source
  coupling, GR-recovery, DG-3 review) are unchanged — now standing on firmer ground.

## 6. Next step

Step 7 (Patch 1120): the **tensor-meson test** — can CPP's strong sector build f₂(1270) as an
emergent orbital L=2 state (matter-side configurations can carry any l), or does it hit the
same per-point representational wall? Either outcome informs the axiom writeup: a second
independent motivation if the wall recurs, or a sharpened granularity contrast (matter
configurations represent l=2 effortlessly; per-point field data cannot) if it does not.
