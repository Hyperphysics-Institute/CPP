# Development History: EU-1 — The Primordial Scalar Spectral Index from Substrate Inflation

**Document type:** Development narrative — laboratory notebook record
**Paper:** EU-1, `series_phenomena/cosmology/early_universe/EU-1/EU-1_primordial_spectral_index.tex`
**Status:** v1.0 SHIPPED (6 June 2026, Session 155)
**Result:** $n_s = 1 - 2/N_* \approx 0.9649$, $\alpha_s \approx -0.0006$, zero-new-axiom, framework-conditional.

## Purpose of This File

How EU-1 came to be — the decisions, the dead ends, and the timeline — for future collaborators (human and AI) who need to understand not just *what* the paper claims but *why the derivation took the shape it did*. The honest scope of EU-1 is the product of a long process of elimination, and that process is itself the strongest evidence that the result is not a fit.

## The Starting Point

EU-1 was not the goal of the session that produced it. The session began as the dark-matter programme: prove that qDP/hTetra aggregates clouding each galaxy *are* dark matter. Pursuing that required understanding how primordial structure is generated, which forced a detour into the CPP account of the Big Bang and inflation. The n_s derivation is a load-bearing brick of that detour — the *generation* of the primordial adiabatic spectrum — but it is not DM-centric, and it was filed in its own early-universe home accordingly (the DM-first paper will cite it, not contain it).

The physical setting was already fixed by the CPP cosmology sector: the early universe is a near-100%-occupied Grid-Point lattice that expands by **dilution of DP-Sea occupancy on a fixed scaffold** (not by stretching the lattice), with a large early Propagation-Speed-Ratio (VSL) solving causal contact. Inflation in CPP is thus *repurposed as the spectrum generator*, and the question became: does that picture produce the measured CMB tilt $n_s = 0.9649$?

## Key Discoveries (chronological)

### Discovery 1: the tilt reduces to a single integer $p$ (Patches 0741–0742)
The whole spectrum collapses to $n_s = 1 - p/N_*$, with $N_*$ fixed by the CP count (not free). So the entire problem became: derive the exponent $p$. $p = 2$ gives $0.9649$ on the standard pivot.

### Discovery 2: only a *logarithmic* boost law works (Patches 0743–0746)
Every mechanical / geometric / packing primitive tested gave a power-law boost $H_{\text{eff}} \propto \bar n^{q}$ and hence an absurd tilt ($n_s = 1 - 6q$: $q=1 \to -5$; packing $\bar n^{1/3} \to -1$; on/off saturation $\to$ the $n_s=1$ cliff). Near-scale-invariance selects the **logarithmic (entropic / chemical-potential) law** as the unique robust candidate among the natural occupation laws — and a logarithm arises only from a microstate-counting source.

### Discovery 3: the logarithm IS axiom A1 (Patch 0749)
The microstate-counting source is indistinguishability: same-type CPs on a GP are occupation-number objects (A1, no individual identity) $\Rightarrow$ Gibbs $1/n!$ $\Rightarrow$ $\mu(\bar n) = kT\ln\bar n + \text{const}$. The log is ontological, not a bookkeeping convention. This is the spine: $p = 2$ within the A1$\to$ZRP$\to\delta N$ chain.

### Discovery 4: the bath is a zero-range process with a provable $H$-theorem (Patches 0772–0775)
For the chemical potential to drive the spectrum, the occupations must actually reach the indistinguishable Gibbs state, fast. LEMMA-NS-HTHEOREM (0772): the symmetric constant-rate ZRP relaxes via a KL-divergence Lyapunov function. LEMMA-NS-ZRP-DERIVE (0774/0775): the minimal PCD/ZBW dynamics *reduces to* that ZRP at leading order from {A1, per-CP PCD, vertex-transitive 600-cell, homogeneous inflation}. Grok independently built a Monte-Carlo bath test that reproduced Poisson + fast equilibration.

### Discovery 5: the neutrality and Debye corners close (Patches 0764–0770)
Leg 2: DP-Sea $\pm$ pair structure $\Rightarrow$ exact charge neutrality $\Rightarrow$ leading mean-field cancels (no $\propto\bar n$ tilt contamination). The long-range $\sqrt{\bar n}$ Debye scare ($\sqrt{10^{74}} \sim 10^{37}$) dissolves under the $\Gamma$-reframing $|\mu_{\text{ex}}|/kT = c\,\Gamma^{3/2}$ with $\Gamma = \alpha/\kappa \sim \alpha$ in the ZBW substrate bath (LEMMA-NS-BATH) — residual $\sim 3.6\times10^{-4} \ll \ln\bar n \approx 170$.

### Discovery 6: the candidate axiom dissolves (Patches 0751–0778)
A candidate axiom (CAND-AX-EU-1, ZBW stack thermalization) was drafted, then split: its ergodicity half is MC-derivable, its log half is already A1. So no new axiom — the result stays at 9 axioms. Promoted to PRED-C-96 on full panel consensus at 0778.

## Failed Approaches

- **Mechanical / power-law boosts** ($H_{\text{eff}} \propto \bar n^q$, packing $\bar n^{1/3}$, on/off superposition fraction): all excluded — power-law absurdity or the $n_s=1$ cliff. This elimination is what *selects* the log; it is reported in the paper as the non-circularity argument.
- **Treating the log uniqueness as a theorem:** initially framed as "near-scale-invariance uniquely selects the log." Reviewers (ChatGPT, Copilot) correctly pressed that this is *practical*-uniqueness within minimal CPP assumptions, not theorem-level (RG/geometric/composite logs are unnatural but not formally excluded). Softened at v1.0.
- **A new axiom (CAND-AX-EU-1):** drafted, then dissolved once its two halves were separated — the axiom was unnecessary.
- **DM-centric framing:** briefly the n_s work risked being absorbed into the DM paper as its headline. Recognized as a category error — n_s is a reusable building block with its own taxonomic home.

## Key Decisions and Why

### Decision 1: file under `series_phenomena/cosmology/early_universe/`, paper ID EU-1
Native early-universe home, not DM-centric. The DM paper cites it. (Maintainer instruction, Session 155.)

### Decision 2: NO THEO registered
The result is conditional/grounded, not an unconditional A1–A11 derivation. Copilot suggested THEO-EU-1; declined per the no-THEO-for-conditional discipline + ChatGPT's "not fully derived from A1–A11" calibration.

### Decision 3: status wording "leading-order derived; consistent with Planck"
Softened from "confirmed at leading order" (Patch 0785, maintainer decision) — the register's ✅ CONFIRMED classification (= measured-and-consistent) and the swarm count (108) are unchanged; only the prose connotation was tightened.

### Decision 4: separate the derived total $N_* \approx 60.5$ from the adopted pivot $\approx 57$
Per reviewer pressure (ChatGPT T3, Copilot T3.2): the CP-count fixes the total e-folds; the pivot placement is the standard observable offset, consistency-level, not itself uniquely CP-count-derived.

## The Paper

EU-1 v1.0 ships the derivation in 13 pages with the formatting standard (CP/GP signature, swarm-validation contribution, problem-status). It contributes PRED-C-96 ($n_s$) + PRED-O-34 ($\alpha_s$) and is the first cosmology/early-universe-sector paper in the corpus. Review: 3/3 SHIP (ChatGPT/Grok/Copilot), zero verdict-flippers.

## Open Problems

- **OPEN-EU-1** — A1–A11 derivation of FRW/VSL homogeneity + the exact ZRP-correction structure (deepest residual; shared with standard inflationary cosmology, CPP at parity).
- **Constant-$H$ / inflation-engine debt** — EU-1 derives the *spectrum*, not the inflationary *engine*. Highest-leverage remaining target.
- **Leg-2 A1–A11 DP-pair-neutrality derivation** — most tractable; not the bottleneck.

*Source tiers consulted: reasoning fragments `reasoning/0781…`, `0783…`; the n_s-arc reasoning trail 0729–0778; `review/reviews-EU-1.md`; `predictions.md` PRED-C-96.*
