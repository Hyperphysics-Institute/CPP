# SR-5 Condition (2) — Why the Sea coherence scale is the future event horizon (SCOPE SKETCH)

**Arc:** OPEN-SR-5 ≡ OPEN-SM-6 (cosmological constant) · **Patch:** 1162 (13 June 2026) · **Sub-item:** OPEN-SR-5d, condition (2) / falsifier D3-1
**Type:** scope-and-precondition sketch — **NO derivation, NO verdict change, NO THEO.** Frames the one remaining condition of the CC arc and identifies the decisive fork. The arc stays conditionally supported.

---

## Orientation — read this first

After Patch 1161 discharged condition (1) (the c08 field equation), the CC arc rests on **one** condition: **why is the Sea's uncancelled-vacuum IR scale the future event horizon `R_h`, rather than the Hubble radius `R_H` or the particle horizon?** This is falsifier D3-1 — and it is a genuine break-point, not a loose end. If CPP physics forces the Hubble/causal scale, the residual cannot be the observed dark energy and the arc fails on the magnitude. So this sketch opens the question that decides whether the arc becomes a zero-parameter CC result or does not.

## The three-horizons tension (the honest problem statement)

The CC-arc lineage has pointed at **three different IR scales**, and only the third gives the right cosmology:

| Scale | Where it came from | CPP argument used | Dynamical status |
|---|---|---|---|
| `R_obs` (observable/particle horizon, N=R_obs/l_P) | TN-SR-1 (Mar 2026), `1/N²` | lattice-step count across the horizon | **demoted** — present-epoch coincidence (CC umbrella, Patch 1103); `1/N⁴≈(l_P/R_H)²` only *now* |
| `R_H = c/H` (Hubble radius) | Step C (Patch 0722) | **PSR-at-c**: "info advances at c per Absolute Moment → the Sea equilibrates over a Hubble time → residual at R_H" | **ruled out** — Friedmann forces Ω_Λ = const, no decel→accel (Hsu 2004) |
| `R_h = a∫_t^∞ dt'/a'` (future event horizon) | Step D / D3 (Patch 0723) | **none yet** — *selected by requiring* the right dynamics (Li 2004: w_now≈−1.02, Ω_Λ: 0→0.685→1) | **admissible** — reproduces the observed history; `0723_horizon_wz.py` CHECK 2/3 PASS |

**The crux:** the event horizon is currently a *fit*, not a *derivation* — it was chosen because it works (D3), while CPP's only worked-out substrate argument (Step C) points to the **wrong** scale (`R_H`). A real closure must derive `R_h` from CPP, and in doing so **supersede the Step-C Hubble argument**. This sketch's claim is that Step C used the wrong CPP causal primitive.

## The decisive fork: A4 (Nexus) vs A3′ (PSR-at-c)

CPP carries **two distinct causal structures**, and they select different scales:

- **PSR-at-c (A3′):** retarded, finite-speed, light-cone-causal propagation (`c = l_P/t_P` per Absolute Moment). A *retarded smoothing* process reaches the **Hubble radius** in a Hubble time. **This is what Step C used.** Light-cone-causal scales are the particle horizon (past) and the Hubble radius (instantaneous) — *not* the event horizon.
- **The Nexus (A4):** *"a global consistency constraint [that] enforces lattice-wide coherence at each Absolute Moment"* (axiom-registry; the mechanism behind Bell-violation/superdeterminism, QM-3/SD). It is **instantaneous, non-local, and global** — coherence is *enforced*, not *propagated*. The axiom-registry explicitly flags A4 as **underused** ("appears only in QM and SD; should appear in charge quantisation, baryon number…") — cosmology is a natural new home.

**The lead (candidate, not claim):** the suppressed Λ is the field energy of the *largest coherent vacuum-mode residual* — the one mode the Sea cannot cancel. Cancellation of the *bulk* Sea is local (the 600-cell shell-sum monopole annihilation, 1107–1108). But the *coherence* that determines which long-wavelength mode survives uncancelled is a **lattice-wide coherence property — exactly A4's job**, not a retarded PSR smoothing. If the Sea's vacuum coherence is Nexus-enforced (A4), then:

1. The Sea is globally coherent over the entire **Nexus-coordinated region**, instantaneously at each Absolute Moment.
2. The uncancelled residual mode sits at the **boundary** of that region — where global coherence is *severed*.
3. That boundary is the **future event horizon**: the surface beyond which a comoving region recedes permanently and can *never again* exchange information with the observer's patch. Once past `R_h`, a region is permanently outside any possible Nexus co-coordination. (The particle horizon is what *has* reached us; the event horizon is what can *ever* stay coordinated — the relevant one for an ongoing coherence constraint.)
4. The event horizon's **future-dependence** — the standard "conceptual cost" of holographic dark energy (it depends on `a(t')` for `t'>t`) — is *natural* for A4, which is **atemporal/global** (it already coordinates entanglement non-locally and a-causally; a future-referencing boundary is the same character, not a new pathology).

So the candidate resolution is: **Step C's `R_H` is the retarded-equilibration scale (A3′); the vacuum residual's coherence is Nexus-enforced (A4), whose severance boundary is `R_h`.** Different primitives, different scales; the residual is a coherence phenomenon ⇒ A4 ⇒ event horizon.

## Decomposition into sub-targets

- **2-i — The cancellation/coherence mechanism (THE FORK; examinable now).** Is the Sea's *large-scale vacuum-mode* coherence enforced by A4 (Nexus, global) or built by A3′ PSR-at-c (retarded)? Decided by examining the Step-B/c05 cancellation and the 1107–1108 shell-sum: the *monopole annihilation* is local-symmetric (per-GP), but the *long-wavelength residual selection* needs a coherence principle — and A4 is the only CPP primitive that enforces lattice-wide coherence without propagation delay. **If A4: the Nexus route is open (→ 2-ii). If PSR-at-c: the Hubble argument stands, D3-1 fires, the arc breaks on magnitude.** This is the make-or-break and it is cheap to confront first.
- **2-ii — Nexus boundary = future event horizon (THE CORE DERIVATION; genuinely open).** Given A4 governs the coherence, derive that the IR boundary of the Nexus-coordinated region is `R_h` specifically — not the particle horizon, not the Hubble radius, not an unbounded/infinite scale. Needs a precise statement of *which* region A4 must keep coherent (proposal: the region in persistent two-way causal contact = bounded by `R_h`).
- **2-iii — Reconcile with / supersede Step C.** Show the Step-C `R_H` argument is the retarded-smoothing scale (governing signal/matter equilibration) and is the *wrong* scale for the vacuum residual, so adopting `R_h` is a *correction*, not an inconsistency. Update stepC's "horizon fixed as the Hubble radius in principle" line accordingly (currently it asserts `R_H`).
- **2-iv — Land on the D3 numerics.** Confirm the derived `R_h` reproduces the Li-2004 dynamics already in hand (`c≈0.8`, w_now≈−1.02, Ω_Λ 0→0.685→1; `0723_horizon_wz.py`). This is bookkeeping *if* 2-ii lands — the numerics exist; the derivation just has to arrive at `R_h`.

## Decision gates

- **DG-1 (recommended next): open 2-i — confront the fork.** Cheapest, decides whether the Nexus route even exists. Read Step B + c05 gradient-sourcing + 1107–1108 for whether the long-wavelength residual selection is A4 or PSR.
- **DG-2:** if 2-i ⇒ A4, open 2-ii (the core derivation). If 2-i ⇒ PSR-at-c, register D3-1 as **fired** (honest negative — the arc breaks on magnitude) rather than forcing the event horizon.
- **DG-3:** reserve a theorem ID (THEO-COSMO-HORIZON-1?) only when 2-ii produces a real result; not now.

## Falsifiers

- **D3-1 (the standing one):** CPP physics forces the Hubble/particle scale ⇒ residual ≠ observed DE ⇒ arc breaks. (2-i decides this.)
- **F-NEXUS-1 (new):** A4's coherence region has no `R_h` boundary — it is either the whole lattice (infinite/no suppression) or the particle horizon (past, gives the wrong dynamics) ⇒ 2-ii fails, event horizon stays a fit.
- **F-COST-1:** if the future-dependence of `R_h` cannot be reconciled with A4 acting "at each Absolute Moment" (a present-tense constraint cannot reference the future evolution) ⇒ the atemporal-Nexus argument is illusory and the cost is real, not dissolved.

## Honest reachability verdict

**Reachable in principle via the Nexus (A4) route, with a real chance of failure** — exactly the "becomes a CC result or doesn't" character. 2-i is confrontable now and is the honest first move (it can *kill* the route cheaply). 2-ii is a genuine open derivation, not an L2.5 bookkeeping step: it requires making "the region A4 must keep coherent" precise enough to single out `R_h`, and F-COST-1 (a present-tense constraint referencing future evolution) is a real conceptual hazard that must be met head-on, not waved away. **No merge-for-elegance:** the event horizon is attractive because it *works*, which is precisely why the derivation must be held to deriving it, not assuming it. If 2-i comes back PSR-at-c, the right outcome is to register D3-1 as fired and report the arc broken on the IR scale — a clean negative, not a forced fit.

## Next

**2-i ADDRESSED (Patch 1163, DG-1 executed)** — see `condition2_2i_coherence_vs_equilibration.md`. The examination of Step B / c05 / 1107–1108 found the existing cancellation machinery is local/retarded with A4 absent, and that it **leaves the IR scale undetermined** (Step C's retarded `R_H` is Hsu-dead). The fork collapses to a binary: every retarded scale is dynamically dead → **the arc survives only if A4 (the Nexus) sets the scale to `R_h`**; D3-1 fires iff the residual is retarded-set. Arc did not break; the question narrowed to 2-ii.

Open **2-ii** (DG-2): (a) settle whether the CPP Sea residual is a retarded gradient (→ D3-1 FIRED, arc breaks) or a global zero-point coherence mode; (b) if coherence-mode, derive A4's coherence boundary = `R_h`, meeting F-COST-1. Per Thomas's choice.

**2-ii ADDRESSED (Patch 1164, DG-2)** — see `condition2_2ii_gradient_vs_mode_and_A4_horizon.md`. **(a) CLEARED:** the residual is a zero-point coherence mode (a drifting *ground state*'s residual is its mode structure, not a transient relaxation), so the IR scale is a coherence scale, not a retarded one — the PSR objection is defused and **D3-1 does not fire**. **(b) ADVANCED, NOT CLOSED:** A4 gives a coherent event-horizon rationale (finite because permanently-disconnected regions can't be coordinated; *not* particle horizon because A4 is spatially a-causal/Bell; event horizon = ongoing mutual reachability), with F-COST-1 addressed in principle (geometric future-dependence, not foreknowledge). **The arc survives condition (2) as a coherent substrate argument — NOT a derived theorem.** Live residual risk: the **particle-horizon alternative** ("coordinable = has-reached" vs "can-ever-reach"), settled only by a **formal A4 coordinable-region construction** (the deep gate). Next: that formalization (promote-or-break), or route the whole arc to multi-AI review as a unit.
