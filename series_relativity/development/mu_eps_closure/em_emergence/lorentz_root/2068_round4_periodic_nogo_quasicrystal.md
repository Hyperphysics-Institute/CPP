# Round 4 — the periodic no-go, and why CPP evades it: the substrate is a φ-self-similar quasicrystal

**Status:** FINDING from the dominant W1-vs-W2 decider. **PANEL-REVIEWED (Patches 2070+2071, CONV-001): 4
responses — unanimous SOUND / SOUND-WITH-CALIBRATION, no verdict-flip; SCRIPT-EXECUTED runs (incl. the real
ChatGPT / GPT-5.5) reproduced the Part-A numerics; the Coxeter regular-Euclidean-4-honeycomb list and
icosahedral harmonic tower independently recomputed.** The panel called the Part-A periodic no-go
"theorem-grade." v1.1 + v1.2 calibration applied below (see `review/reviews-2068.md`). **Still NOT a THEO;
NO status/registry move rides on this — the OPEN-SR-10 / R2 world-call sharpening follows separately, under
STOP-and-warn, on TLA's nod.** Numerics are consistency-evidence only (handover §7). The committed
world-call stays at the Round-15 checkpoint.
**⚠ This finding rests on a FOUNDATIONAL corpus point — the substrate's global structure (φ-self-similar /
quasicrystalline, not periodic). Panel-endorsed (T3 SOUND, incl. independent Coxeter recomputation), but any
status move still goes to TLA.** (See §6.)

> **CHANGELOG.** v1.0 (Patch 2068): original probe. **v1.1 (Patch 2070): post-panel calibration** (3
> responses). Part-A no-go theorem-grade; Part-B substrate reading correct; T4 dense-Fourier caveat (W1
> possible-not-granted); W3-conditional qualifier. **v1.2 (Patch 2071): real-ChatGPT (GPT-5.5) late review,
> two precision fixes** — **(T2)** the Part-A boundedness no-go requires a **regular / ℓ¹-summable** periodic
> kernel (a pathological non-summable nonlocal kernel could engineer an unbounded symbol); CPP's A3′
> broadcast is finite-range, so it satisfies the hypothesis and the no-go applies. **(T1/T5)** "W3 EXCLUDED"
> was over-strong: Round 4 excludes the **periodic-lattice W3 channel**; **globally W3 is strongly
> disfavoured** (Round 3's continuum-limit invariance, given C3), with **full** exclusion pending the Round-5
> aperiodic spectral calculation. (GPT-5.5's arrival also confirms the v1.1 "ChatGPT"-labelled INSPECTED
> response was in fact Copilot — see `reviews-2068.md §0`.) One-line summary (ChatGPT): *Round 4 establishes
> a theorem-grade periodic no-go; CPP survives because it is not periodic.*

---

## 0. The probe

Round 3 reduced the W1-vs-W2 fork (dominantly) to **discrete dispersion isotropy** of the A3′ broadcast,
and flagged Round 4 as the full nested-shell computation. Round 4 asks the decider directly: does the full
600-cell broadcast reach **exact** dispersion isotropy at finite lattice spacing a (→ **W1**, exact-discrete
Lorentz), or only suppress the anisotropy (→ **W2**, IR-emergent with a Planck floor)? Attempting the
computation forces the question the earlier rounds deferred: **what is the substrate's global structure?**

## 1. Result in one line

**There is a hard no-go for any *periodic* lattice — but it does not apply to CPP, because CPP is aperiodic
by construction.** (A) Any regular periodic-lattice broadcast has a bounded, Brillouin-zone-periodic
dispersion symbol, which can neither equal ω = c|k| nor be exactly isotropic; finite shells suppress the
icosahedral anisotropy one harmonic at a time but never zero the infinite tower — so **exact W1 is
impossible for a periodic substrate.** (B) **The CPP substrate is the φ-self-similar nested-600-cell
hierarchy (SR-1) — an icosahedral *quasicrystal*, aperiodic, with no Brillouin zone.** Aperiodic order is
precisely the structure class that **evades** the periodic no-go (the deterministic analog of the causal-set
randomness route). **So W1 is not ruled out; it is pinned to one sharp question — does the φ-self-similar
quasicrystal broadcast carry exact Lorentz?** And **the periodic-lattice route to W3 is excluded, with W3
strongly disfavoured globally** (the IR/continuum limit is Lorentz-invariant given C3; any residual floor is
sub-Planck-nesting tiny, ~l_P/10³⁰) — full W3 exclusion pends the Round-5 aperiodic spectral calculation.

## 2. Part A — the periodic no-go (numerical; the solid part)

Model the broadcast as a translation-invariant hopping on a regular lattice; the linear dispersion symbol is
D(k) = Σ_shells w · Σ_{d∈shell} 2(1 − cos(k·d)), and ω(k) = √D.

- **(A1) A bounded periodic symbol cannot be ω = c|k|.** For a **regular** broadcast — finite-range, or
  more generally an ℓ¹-summable (absolutely convergent) periodic kernel — D(k) is a uniformly convergent
  Fourier series on the BZ, hence a **bounded** continuous periodic function, while c|k| is unbounded. (The
  hypothesis matters: a *pathological* non-summable nonlocal periodic kernel could engineer an unbounded or
  distributional symbol; CPP's A3′ broadcast is finite-range — the PSR shell — so it is trivially summable
  and the no-go applies.) The normalized phase speed √D/|k| therefore **collapses**
  away from k=0: measured (single icosahedral z=12 shell) **0.998 → 0.975 → 0.904 → 0.797** at
  q=|k|a = 0.3 → 1 → 2 → 3. Exact Lorentz needs 1.0000 at *all* q. This fails for **any** periodic lattice,
  at any hopping range (an infinite-range periodic sum is still a Fourier series on the BZ).
- **(A2) Finite shells suppress one harmonic at a time, never the whole tower.** The icosahedral group's
  anisotropy lives in the harmonic tower l = 6, 10, 15, …. A single z=12 shell gives leading anisotropy
  ∝ q⁴ (the l=6 harmonic); fractional anisotropy at q=0.15 ≈ **1.0×10⁻⁷**. Tuning a second icosahedral
  shell (radius φ) to cancel the leading l=6 term drops it to **8.9×10⁻⁹** (×11) — but **nonzero**, the
  residual now the next harmonic (l=10). Each added/tuned shell kills one more harmonic; the tower is
  infinite, so a **finite** shell sum never reaches **exact** isotropy.

**Part-A verdict:** for a periodic substrate, **exact W1 is impossible** — Lorentz is at best IR-emergent
(**W2**), with the 600-cell's icosahedral symmetry making the floor extraordinarily small (anisotropy first
at q⁴, two orders softer than a cubic lattice's q²).

## 3. Part B — the evasion: CPP's substrate is aperiodic by construction

Part A assumes a **periodic** lattice — a Brillouin zone. **The CPP substrate has none.**

- **SR-1's canonical reading is φ-self-similar.** "Grid Resolution: the Nested 600-Cell Hierarchy" fixes
  physical space as a *"heavily nested array of self-similar 600-cell motifs … down to the true grid-point
  spacing ∼ l_P/10³⁰,"* with the *"self-similar R/a = φ relation [holding] at every level of the nesting."*
  Golden-ratio self-similar inflation symmetry is the **defining** property of an **icosahedral
  quasicrystal** — aperiodic, with a dense φ-Fourier-module and **no Brillouin zone.**
- **A 600-cell admits no periodic Euclidean tessellation anyway.** The regular honeycombs of flat 4-space
  are only {4,3,3,4}, {3,3,4,3}, {3,4,3,3} (Coxeter); the 600-cell {3,3,5} tiles the 3-sphere and
  hyperbolic space, **not** Euclidean 4-space. So a periodic flat-space 600-cell lattice *does not exist* —
  the substrate is **necessarily** non-periodic (the loose "tessellated … per unit cell" phrasing in the
  orientation doc must be read as SR-1's self-similar nesting, not a Bravais lattice). **CPP is in the
  no-go-evading class by mathematical necessity.**
- **Aperiodicity is the known escape.** Exact (or statistically exact) Lorentz invariance on a discrete
  structure is achieved precisely by giving up periodicity: causal sets do it via Poisson randomness;
  quasicrystals via deterministic aperiodic order. The periodic no-go's premise (a BZ) is exactly what these
  structures lack. The 600-cell / icosian / golden-ratio data is the canonical icosahedral-quasicrystal
  structure (the H₄–E₈ connection).

**Honest numerical caveat.** A *finite* shell tower is still crystal-like and does **not** probe the
aperiodic limit — our nesting numerics only re-exhibit the Part-A suppression. The decisive computation is
the dispersion (structure factor) of an **icosahedral-quasicrystal approximant** (a cut-and-project /
φ-inflation point set) and whether it is exactly isotropic at finite resolution. **That is the Round-5
target — not done here.**

## 4. World-call determination

- **W3 (real, O(1) preferred frame): the periodic-lattice W3 channel is EXCLUDED; globally W3 is STRONGLY
  DISFAVOURED — given A3/A3′ and C3, full exclusion pending Round 5.** Part A excludes the periodic route to
  a preferred frame, and Round 3's continuum-limit Lorentz invariance (given C3) strongly disfavours W3
  globally — but *full* exclusion needs the actual infinite nested (aperiodic) broadcast shown to have
  IR-Lorentz spectral/causal behavior from-substrate, which is Round 5. So this is a narrowing, not yet a
  closed exclusion: any discreteness floor is bounded by the sub-Planck nesting scale (~l_P/10³⁰), but
  "no preferred frame at all" is provisional pending the quasicrystal spectral calculation.
- **W2 (limit-exact, Planck floor):** the realized world **if** the substrate is treated as effectively
  periodic — secured by Part A, with an icosahedrally tiny floor. **And note (panel T4):** even the
  *aperiodic* substrate could land here — a deterministic quasicrystal has a **dense Fourier module** (Bragg
  peaks) and retains icosahedral local symmetry, so it might only push the anisotropy onto an
  infinitesimally-small-but-nonzero dense set of scales — i.e. a **highly-suppressed W2**, not exact W1.
- **W1 (exact-discrete):** **made *possible* — not granted — by the substrate being φ-self-similar /
  quasicrystalline.** Evading the *periodic* no-go (no Brillouin zone) is **necessary but not sufficient**
  for W1. Not proven — pinned to the single sharp, decidable question of whether the quasicrystal broadcast
  achieves *exact* isotropy (W1) or merely dense-suppressed isotropy (W2) (Round 5).

So the campaign's three-world question is **determined down to one line:** **the periodic-lattice W3 channel
is out and W3 is strongly disfavoured globally (given A3/A3′, C3); the answer is W1 or W2; and the W1-vs-W2
decision is the quasicrystal-Lorentz question — exact vs dense-suppressed isotropy — on CPP's own
golden-ratio self-similar substrate.** For every physical purpose the distinction is moot (the floor, if
any, sits at ~l_P/10³⁰); for the foundational world-call it is the whole game.

## 5. Effect on the world-call (informal; committed call at Round 15)

This **strengthens** the Round-3 informal call rather than overturning it: the **periodic-lattice W3 channel
is now excluded** and **W3 strongly disfavoured globally** (vs merely strongly disfavoured before, with no
channel pinned down); W2 *secured* as the periodic-approximation floor; W1 *upgraded from "open upside" to
"made possible — not granted — by the substrate being quasicrystalline, pinned to a single decidable
question."* The committed call remains TLA's at Round 15 — and an early committed call would be **provisional**
(periodic-W3 excluded; W3 strongly disfavoured; W1-or-W2 = quasicrystal exact-vs-dense isotropy), defensible
only if phrased as a provisional world update pending the Round-5 spectral calculation, if TLA and the panel
concur.

## 6. The foundational flag (why this is bigger than a registry edit)

This finding's load-bearing claim is about the **substrate's global structure** — that it is φ-self-similar /
quasicrystalline (aperiodic), not a periodic lattice. That is a programme-foundational reading, with two
consequences worth explicit panel + TLA scrutiny: (i) it determines the exact-Lorentz world-call; (ii) it
implies the orientation-doc "tessellated … per unit cell" language should be reconciled with SR-1's
self-similar-nested reading (they are consistent only under the aperiodic interpretation, since no periodic
600-cell tessellation of flat 4-space exists). **No status move should be made on this until the panel has
pressed it and TLA has ruled** — it is more consequential than the OPEN-SR-10/R2 registry edits already
deposited.

## 7. Honest scope — what is NOT shown

- **W1 is NOT proven.** Part B is a structural/conceptual evasion of the no-go, plus a corpus reading — not a
  demonstration that the quasicrystal broadcast *is* exactly Lorentz. That is Round 5.
- **The numerics are consistency-evidence only.** Part A (the periodic no-go) is solid and reproducible;
  Part B's finite-tower numerics do **not** probe the aperiodic limit (stated plainly in the script).
- **No THEO. No status file touched** (R2-STATUS, SR.md, CONJ.md, world-call ledger untouched this round).
- The quasicrystal-Lorentz literature is genuinely unsettled; "aperiodic evades the lattice no-go" is the
  defensible claim, "quasicrystals realize exact Lorentz" is **not** — it is the open Round-5 question.

## 8. Ledger

- **NO THEO. NO status/registry move in this finding.** **PANEL-REVIEWED and cycle-closed (Patch 2070):**
  3 responses, unanimous SOUND / SOUND-WITH-CALIBRATION, no flip; Part-A numerics reproduced
  (SCRIPT-EXECUTED); Coxeter list + icosahedral harmonic tower independently recomputed. Aggregation in
  `review/reviews-2068.md`. The OPEN-SR-10 / R2-STATUS world-call sharpening follows **separately**, under
  STOP-and-warn, on TLA's nod — not here, and especially not unilaterally on a substrate-structure claim.
- **Forward (Round 5, sharpened by panel T4):** dispersion / structure-factor isotropy of an explicit
  icosahedral-quasicrystal approximant (cut-and-project from E₈/H₄ or φ-inflation) — and crucially, whether
  it reaches **exact** isotropy (W1) or only **dense-suppressed** isotropy (a highly-suppressed W2), since a
  quasicrystal's dense Fourier module (Bragg peaks) + icosahedral local symmetry do not *a priori* give
  exact Lorentz. This is the actual W1-vs-W2 decider.

*Probe by Claude Opus under Thomas Lee Abshier's direction. Numerics consistency-evidence only;
corrections appended forward.*
