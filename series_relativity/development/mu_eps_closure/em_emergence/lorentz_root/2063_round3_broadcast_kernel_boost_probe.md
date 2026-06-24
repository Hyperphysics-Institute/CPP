# Round 3 — decisive probe: does the A3′ retarded broadcast kernel carry the boost?

**Patch 2063, 2058-band.** Campaign: exact-emergent-Lorentz root (handover 2058). Builds on Round 2
(`lorentz_root/2060_round2_quaternion_boost_commutator_probe.md`, panel-closed SOUND at 2062).
**Status:** FINDING from the decisive probe. **Panel-pending — NOT banked. NO THEO. NO status move. NO
proof claim.** Numerics in `verify/2063_broadcast_cone_dispersion.py` are consistency-evidence only
(handover §7). The committed world-call stays at the Round-15 checkpoint.

---

## 0. The probe

Round 2 killed the *static-geometric* boost: the PCD budget partition is positive-definite (Euclidean),
so its "boost" is a compact rotation (M² = −I). The panel-endorsed relocation said the Minkowski (−) sign,
if it exists, must come from the **causal** structure — the retarded A3′ broadcast — and flagged (T3) that
the identity ds² = (c·t_P)² − |d_spatial|² is *bookkeeping* until the broadcast is shown to **dynamically
enforce** the light-cone. Round 3 runs exactly that test: build the boost from the A3′ broadcast kernel and
re-run the three diagnostics.

## 1. Result in one line

**The causal route carries the boost — and the Round-2 T3 caveat is resolved, not merely deferred.** The
A3′ broadcast *dynamically* propagates at a fixed speed c on a retarded light-cone; the boost built from it
is the **non-compact hyperbolic** Lorentz boost (N² = +I, tanh-addition, cone-preserving) — the exact
inverse of Round 2. So the − sign is real and dynamical, not bookkeeping. **This strongly disfavours W3**
(a real, O(1) preferred frame): the substrate's continuum limit *is* Lorentz-invariant. The remaining
question collapses to **W1 vs W2** — whether the **discrete** broadcast's light-cone is exact at finite
lattice spacing (W1) or only emergent in the IR with a Planck-suppressed floor (W2). The fork is now a
single sharp quantity: **discrete dispersion isotropy across all directions n̂.** The 600-cell's
icosahedral coordination shell (z = 12) is **far** more isotropic than a cubic lattice (anisotropy
∝ q⁴ vs q², verified) — the structural reason the 600-cell is the right substrate for approaching, and
possibly reaching, W1.

## 2. The A3′ broadcast kernel, as the corpus states it (build from this, not a reconstruction)

A3′ axiom text (`op_einstein_closure/spin2_construction/1123_task2_axiom_text_A3prime.md`, PASSED DG-3
3/3):
- **A3 (the broadcast axiom it amends):** "DI-bits propagate between CPs at **c = l_P/t_P**." The broadcast
  has a **fixed propagation speed** by axiom.
- **(C3) Dynamics:** "Q_ij participates in the PCD cycle identically to Φ and V_i: the Compute step applies
  the same icosahedral PSR shell-sum to all packet components. **In the continuum limit this yields wave
  propagation at exactly c, □Q_ij = S_ij.**" — the broadcast's continuum limit is the **d'Alembertian**
  □ = (1/c²)∂_t² − ∇², which carries the Minkowski signature by construction.
- **(C4) Far field:** "h^TT = (2G/c⁴r) Q̈^TT(**t_ret**)" — the **retarded** quadrupole kernel, supported on
  the light-cone (retarded time t_ret = t − r/c). Genuine finite-speed causal propagation.
- **(C2) Carriage:** packet components are stated in the **absolute (Nexus) frame**, flat connection. The
  preferred slicing is explicit at the substrate level — which is why exactness-at-finite-a is a real
  question, not automatic.

**The decisive structural reading.** The broadcast's invariant is a **fixed SPEED c** (the light-cone
slope), *not* a fixed length. Round 2's budget partition fixed a **length** (τ = l_P in +-quadrature) and
got the compact form; the broadcast fixes a **speed** and gets the Minkowski form. The *same* Absolute
Moment supplies both — l_P (a length) and c = l_P/t_P (a speed) — and **the boost-relevant invariant is the
speed, not the length.** That is the whole resolution of the Round-2 obstruction.

## 3. Part A — the broadcast boost is non-compact (N² = +I); the − sign is dynamically enforced

A boost is, by Einstein's own constancy-of-c argument, the frame transformation that **preserves the
propagation speed c**. The broadcast fixes c by axiom (A3) and dynamically enforces it via the retarded
cone (C3/C4). So the transformations relating frames that all measure the broadcast speed c are exactly the
**hyperbolic boosts** L(η) = exp(η N), N = [[0,1],[1,0]], **N² = +I** (`verify/2063` Part A):

- **Null-cone preservation.** Every L(η) fixes the null directions (1, ±1) [the light-cone x = ±ct] as
  eigenvectors with eigenvalues e^{±η}. The cone — the speed c — is the invariant. (Contrast Round 2: the
  budget map preserved the *circle*, not the cone.)
- **Relativistic composition.** Collinear composition is rapidity addition η₁+η₂, i.e.
  β₃ = (β₁+β₂)/(1+β₁β₂) — **< 1 always, monotone, never reaches c at finite composition.** Exactly the
  inverse of Round 2's circular law (which reached c at finite β = 1/√2 and went non-monotone).

> **Non-circularity (pre-empting the panel's T4/T3).** The *input* is the corpus fact that the broadcast
> propagates at a fixed speed c (A3 + C3/C4, retarded cone); the *output* is that the frame-transformations
> preserving constant-c are hyperbolic boosts (Einstein's argument). This is not "assume Minkowski, get
> Minkowski": it is the demonstration that the broadcast's *fixed-speed* dynamics select the non-compact
> generator, where the budget's *fixed-length* geometry selected the compact one. **The Round-2 T3 caveat
> is thereby answered:** the broadcast *does* dynamically enforce the cone (it is a retarded, speed-c
> propagator), so the − sign is physical, not an algebraic rearrangement.

**Scope guard.** "Carries the boost" here means **in the continuum limit** (C3's own qualifier:
□Q = S holds *in the continuum limit*). The exact-discrete version is §4's open question. The − sign being
dynamical (vs bookkeeping) is settled; exactness-at-finite-a is not.

## 4. Part B — the W1-vs-W2 fork is now a single quantity: discrete dispersion isotropy

The continuum limit of the broadcast is Lorentz-invariant (§3). Whether the **discrete** broadcast (finite
a) carries the **exact** continuous SO⁺(3,1), or only its IR limit, is whether the discrete light-cone is
exact — i.e. whether the discrete dispersion ω(k) is **exactly linear and isotropic** (ω = c|k|, all
directions) at finite a. Three results (`verify/2063` Part B):

1. **Single-axis exactness is achievable (1D).** The 1D leapfrog discrete wave at the magic Courant number
   cΔt = a gives ω = ck **exactly** across the entire band (verified to 4.8×10⁻¹⁵). So a boost along a
   *single fixed direction* can be exact-discrete. The obstruction to W1 is therefore not the time-step; it
   is **isotropy across all directions n̂** (which the target T1 explicitly demands).

2. **Generic ≥2D lattices are anisotropic → W2.** On a cubic lattice the discrete phase speed depends on
   direction (axis vs diagonal), with fractional anisotropy ∝ **q²** (q = |k|a) and **no** Courant number
   removing it. Generic discreteness ⇒ Lorentz-violating dispersion floor ⇒ **World 2** (limit-exact,
   Planck-suppressed) — the most likely world, and (handover §3) itself a strong outcome.

3. **The 600-cell (icosahedral z = 12) is dramatically more isotropic.** Summing over the 600-cell's
   coordination shell (12 icosahedral directions = the corpus z = 12) gives fractional anisotropy ∝ **q⁴**,
   ~10²–10³× smaller than cubic at the same q (verified: cubic ~ q², icosahedral ~ q⁴). **Group-theory
   reason:** the icosahedral group has **no degree-4 anisotropic invariant** (its lowest non-trivial
   harmonic is l = 6), whereas cubic symmetry has a degree-4 (l = 4) anisotropy. The icosahedral broadcast
   suppresses dispersion anisotropy two full orders higher in q than any crystallographic lattice could.

**Honest reading of Part B.** Even the icosahedral nearest-neighbour shell is **q⁴-anisotropic, not exactly
isotropic** — so the nearest-neighbour toy alone realizes **W2 with a much-suppressed floor**, not W1. W1
(exact, zero anisotropy at finite a) would require the **full** 600-cell PSR shell structure (the nested
multi-shell broadcast, not just z = 12) to cancel the residual q⁴ term exactly. That cancellation is **not
shown** and is the Round-4 target. The 600-cell makes W1 *plausible and uniquely favourable* (no other
lattice gets this close); it does not make it automatic.

## 5. Effect on the world-call (informal; committed call at Round 15)

- **World 3 (real, O(1) preferred frame): strongly disfavoured.** The retarded broadcast's continuum limit
  *is* the Lorentz-invariant wave equation, and the boost it carries is genuinely hyperbolic. Any
  preferred-frame signature is at most a Planck-suppressed **dispersion** floor (operationally W2), not an
  O(1) obstruction. The "substrate is just Euclidean" reading of Round 2 is now closed: the substrate has a
  genuine causal cone.
- **World 2 (limit-exact, Planck floor): the secured floor and most-likely realized world.** Follows from
  A3′ C3 (continuum limit = □). *Caveat:* C3's discrete→continuum step (that the icosahedral PSR shell-sum
  limits to exactly □ at speed c) is the standard lattice-Laplacian result and is corpus-stated, but a full
  from-substrate derivation of c_photon is **OPEN-SR-9** — so even W2 is "secured modulo OPEN-SR-9."
- **World 1 (exact-discrete): the open upside, now with a concrete favourable mechanism.** Gated on the
  full 600-cell broadcast achieving **exact** dispersion isotropy at finite a. The icosahedral z = 12
  suppression (q⁴) is the strongest structural hint any substrate could give, but the residual is nonzero
  in the nearest-neighbour toy; exact cancellation across the nested shells is unproven.

Net (not a committed call): **W3 ↓↓, W2 ↑ (secured floor), W1 open with a favourable structural reason.**
The campaign has gone from three wide-open worlds to *W2-essentially-secured, W1-the-open-upside,
W3-nearly-excluded* — a major narrowing, and a defensible result in ≥2 worlds (the handover's win
condition).

## 6. Round-4 target (named, not begun) — and how it grounds the corpus

Compute the dispersion of the **full** 600-cell PSR shell-sum broadcast (all nested shells, not just
z = 12) and determine whether the residual q⁴ (and higher) anisotropy cancels **exactly** at finite a
(→ W1) or only suppresses (→ W2 with an icosahedrally-tiny floor). This is **identically** the corpus's
open question on two existing fronts, which the root campaign would thereby ground:
- **R2 premise (i)/(ii):** lattice-isotropy-of-c / "c_photon is a **scalar** function of C, not an
  anisotropic f(C,Σ)" (R2-STATUS Patch 2027 birefringence attack). Exact dispersion isotropy *is* that
  premise.
- **OPEN-SR-9:** the from-substrate emergence of the photon and c_photon(C)/Z₀ from the DP Sea. The
  emergent photon's dispersion isotropy is the same quantity.

So Round 4 is not a detour: closing the dispersion-isotropy question closes (or bounds) R2 and OPEN-SR-9
together — the leverage the handover §1 promised the root would have.

## 7. Discipline ledger (this round)

- Band 2058–2099; this = **2063**, built on origin HEAD (2062 cycle-close). Clone-and-grep gate honored.
- Bundle (reasoning-capture rider): this finding + verbatim reasoning `em_emergence/reasoning/2063.md`
  + verify `lorentz_root/verify/2063_broadcast_cone_dispersion.py`.
- Built from the corpus A3′ kernel (1123 C3/C4, A3 speed-c) — not an outside reconstruction.
- Numerics: consistency-evidence ONLY; not proof (handover §7). No FEM. No collapsed residuals (the W1/W2
  fork and the OPEN-SR-9 rigor gap are stated precisely, not merged).
- **No theorem. No status file touched (R2-STATUS, SR.md, CONJ.md, registries untouched). No THEO.**
  Recommend CONV-001 dispatch to pressure-test (a) the non-circularity of Part A, (b) the "W3 strongly
  disfavoured / W2 secured-modulo-OPEN-SR-9" world language, (c) whether the icosahedral q⁴ result is
  correctly scoped as *favourable-but-not-W1*.
- Honest scope: Round 3 demonstrates the broadcast carries the boost **in the continuum limit** and
  identifies the exact-discrete question as dispersion isotropy. It does **not** establish W1. The
  committed world-call remains at Round 15.

*Captured by Claude Opus under Thomas Lee Abshier's direction. Corrections appended forward (handover §7).*
