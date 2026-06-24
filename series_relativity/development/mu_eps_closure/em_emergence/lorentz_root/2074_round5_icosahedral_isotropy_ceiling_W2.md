# Round 5 — the decider: the icosahedral isotropy ceiling determines the world is W2

**Status:** FINDING — **the W1-vs-W2 decider.** **Panel-pending — NOT banked. NO THEO. NO committed
world-call (that is TLA's; this finding makes it ready).** Numerics in
`verify/2074_quasicrystal_isotropy_ceiling.py` are consistency-evidence only (handover §7), but the
load-bearing step is **group theory verified to machine precision**, not a fit. **This finding DETERMINES
the campaign's world-call: W2.**

---

## 0. The question

Round 4 left exactly one open fork: the CPP substrate is the φ-self-similar nested-600-cell = an icosahedral
**quasicrystal**, which evades the *periodic* no-go (no Brillouin zone) — but does the deterministic
quasicrystal reach **exact** dispersion isotropy (**W1**) or only **dense-suppressed** isotropy (**W2**)?
Round 5 answers it.

## 1. Result in one line

**W2.** A structure with **icosahedral point symmetry** — periodic *or* quasicrystalline — is isotropic only
up to a finite harmonic: the icosahedral invariants sit at degrees l = 0, **6**, 10, 15, … There is **no l=2
and no l=4** anisotropic invariant, so the dispersion is isotropic through rank-4 (**isotropic elasticity**;
v_phase isotropic at O(q²)) but the **rank-6 / l=6** harmonic is a **generic, nonzero q⁴ anisotropy floor**.
The quasicrystal inherits this floor — so it does **not** reach exact isotropy. **Exact W1 would require
every anisotropic harmonic to vanish — achieved only by a continuum or a statistically-isotropic *random*
(causal-set) substrate, neither of which is CPP's deterministic 600-cell.** The realized world is therefore
**W2: IR-exact Lorentz (isotropic elasticity) with an l=6/q⁴ anisotropy floor**, pushed unobservably tiny
(~l_P/10³⁰ nesting) but **nonzero**.

## 2. The icosahedral isotropy ceiling (the load-bearing group theory)

Expand the broadcast dispersion D(k) = Σ_x w(|x|)·2(1−cos(k·x)) at small k: the O(k²ⁿ) term is the rank-2n
tensor Σ_x x_{i₁}…x_{i₂ₙ} contracted with k's. Direction-dependence (anisotropy) appears at the first rank
whose tensor has a non-isotropic part — i.e. the first **anisotropic** harmonic of the point-group.

For the **icosahedral** group the anisotropic invariants begin at **degree 6** (then 10, 15, …); there is
**no degree-2 or degree-4** anisotropic invariant. Verified to machine precision (the angular deviation of
the rank-k tensor of the icosahedral shell):

| rank k | angular deviation | meaning |
|---|---|---|
| 2 | 2×10⁻¹⁶ | **isotropic** (always) |
| 4 | 3×10⁻¹⁶ | **isotropic** — no l=4 invariant ⇒ **isotropic elasticity**, v_phase isotropic at O(q²) |
| 6 | **9.3×10⁻²** | **anisotropic** — the l=6 harmonic ⇒ v_phase anisotropy enters at **O(q⁴)** |
| 8 | 2.2×10⁻¹ | anisotropic |

So the q⁴ (l=6) phase-speed anisotropy measured back in Rounds 3–4 is **not** a finite-shell artifact — it
is the **lowest icosahedral anisotropic harmonic**, present in *any* icosahedrally-symmetric dispersion. No
choice of shells or weights removes it (you can cancel one harmonic at a time, never the tower).

## 3. The quasicrystal inherits the floor — and the §4.1 channels are moot for W1

An icosahedral-quasicrystal approximant (φ-inflation nested shells) has v_phase anisotropy scaling **q⁴**
(fitted exponent 4.0), **small but nonzero** (2.6×10⁻⁷ → 4.4×10⁻⁵ over q = 0.05 → 0.18). Aperiodicity
removed the *periodic* obstruction (no BZ saturation, so ω can be linear ~ c|k|), but it does **not** remove
the **point-symmetry** obstruction — the quasicrystal is still only icosahedrally symmetric, so the l=6/q⁴
floor survives. This is **W2**.

Note this **closes the W1 question at the most basic level**: the Round-4 §4.1 further channels (interactions,
Φ/V/Q mode-mixing, C2 carriage, finite-a composition) were the *additional* hurdles a W1 claim would have to
clear — but they are now **moot**, because W1 already fails at the **free-field dispersion** level (the most
fundamental channel). You cannot have exact-discrete Lorentz when even the free dispersion is q⁴-anisotropic.

## 4. What exact W1 would have required (and why CPP isn't it)

Exact isotropy needs **every** anisotropic harmonic to vanish. Two structures achieve it: a **continuum**
(full rotation symmetry), or a **statistically-isotropic random** set — a Poisson sprinkling, the **causal-set**
route. Verified: a Poisson set's rank-4 and rank-6 deviations both → 0 as N grows (1.6×10⁻¹ → 6×10⁻³ at
rank-4 from N=200→20000), washing out *every* harmonic. **CPP's substrate is a deterministic icosahedral
quasicrystal, not a random sprinkling** — it does **not** inherit the causal-set route to exact Lorentz. Its
golden-ratio order is what made it *far* more isotropic than a cubic lattice (q⁴ vs q²) and what secures the
IR limit — but determinism + finite point symmetry is exactly what caps it at W2.

## 5. The determination — the world is W2

Assembling Rounds 2–5:
- **W3 (real preferred frame): the periodic-lattice channel EXCLUDED (theorem-grade); W3 strongly
  disfavoured globally** (Round 3's continuum-limit Lorentz invariance, given A3/A3′ and C3) — and Round 5
  *secures* the IR limit (isotropic elasticity), so the global disfavouring is now backed by a from-substrate
  isotropic-elasticity result, not only C3. W3 is dead in all but the most contrived reading.
- **W1 (exact-discrete): RULED OUT** for the deterministic 600-cell substrate — the icosahedral l=6/q⁴
  anisotropy floor is generic and nonzero (modulo a non-generic accidental-vanishing loophole, §6).
- **W2 (limit-exact + Planck floor): THE ANSWER** — IR-exact Lorentz (isotropic elasticity) with an l=6/q⁴
  anisotropy floor at the lattice scale, suppressed to ~l_P/10³⁰-nesting scale, unobservably tiny but
  nonzero.

**This is the campaign's terminal world-call (pending panel + TLA), reached at Round 5 of a 10–50 budget.**
W2 is the handover's "most likely world, itself a strong outcome": CPP reproduces exact special relativity
in the continuum/IR, from substrate, with Lorentz violation banished to ~10⁻³⁰ of the Planck scale — far
below any conceivable test. The 600-cell's icosahedral/golden-ratio structure is *why* the floor is q⁴ (two
orders better than a generic lattice) and *why* the IR is exactly isotropic.

## 6. Honest scope — what is NOT shown, and the one loophole

- **The group theory is rigorous** (machine-precision; the icosahedral degree-6 first-anisotropic-invariant
  is standard A₅ representation theory). The numerics on the quasicrystal approximant are
  consistency-evidence (handover §7).
- **The W1-killing inference** assumes the broadcast dispersion inherits the substrate's icosahedral
  symmetry — which it does, the broadcast being built on the icosian/600-cell structure. The **one loophole**:
  if the PCD dynamics carried an *additional* symmetry (beyond icosahedral) forcing **all** anisotropic
  harmonics to vanish, W1 could survive — but that would make the dispersion effectively continuum-like,
  contradicting discreteness, and there is **no such symmetry in evidence**. So the loophole is real but
  non-generic and unmotivated; absent a positive reason, **W2 is the determination.**
- **No THEO. No status/registry move** in this finding. This makes the **committed world-call (W2) ready**;
  the call itself is TLA's (and the registry move from "W1-or-W2" to "W2" would follow, under STOP-and-warn,
  after panel).

## 7. Ledger

- **NO THEO. NO status move.** The committed world-call (W2) is TLA's to make; this finding makes it ready.
- **Recommend CONV-001 dispatch** to pressure-test: (a) the icosahedral rank-4-isotropic / rank-6-anisotropic
  group theory and its machine-precision verification; (b) the inference that the broadcast dispersion
  inherits icosahedral symmetry, so W1 fails at the dispersion level (the §4.1 channels being moot); (c) the
  accidental-vanishing loophole — is it truly non-generic, or is there a CPP symmetry that could force it?;
  (d) whether W2 is now committed-call-ready and W3 fully excludable given the from-substrate isotropic
  elasticity.
- **Forward (post-panel):** if the panel concurs, TLA makes the committed call **W2**, OPEN-SR-10 moves to
  RESOLVED-W2 (under STOP-and-warn), and the campaign writes its closing handover. The residual (the exact
  size/coefficient of the l=6 floor, and the OPEN-SR-9 from-substrate c_photon it feeds) becomes a tidy
  post-campaign open item, no longer world-call-bearing.

*Probe by Claude Opus under Thomas Lee Abshier's direction. Numerics consistency-evidence; the load-bearing
icosahedral group theory is exact. Corrections appended forward.*
