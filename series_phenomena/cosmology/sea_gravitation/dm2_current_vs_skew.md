# DM-2 — Does the O(δ³) NESS Current Accumulate into the Bulk Residual? (DM-side angle on the H-NESS lift)

**Patch:** 0810 (Session 156, 8 June 2026) · **Work item:** DM-2 / net-broadcast lemma condition (b), DM-side sub-question
**Predecessor:** Step-2(b) (0809), which reduced (b) to `⟨𝓕⟩_bulk = −4k²⟨δδ'²⟩` and located the gate at the (H-NESS) lift.
**Verify:** `scripts/0810_current_vs_skew.py` (2-D Fokker–Planck NESS: current vs equal-time skew).
**Grade:** structural result; sharpens (b). No verdict change.

---

## The sub-question

Step 2(b) left one escape flagged but unclaimed: the established O(δ³) substrate effect is a *steady NESS current* (chirality Patch 0689 — detailed balance violated, steady current at O(δ³)), and a steady current is divergence-free by stationarity. Does that current **accumulate** into the equal-time third moment `⟨δδ'²⟩` that sources the bulk residual (→ catastrophe), or not (→ clean horizon-only Λ)? This is the DM-side angle on the (H-NESS) lift.

## The answer: a current is not a skew

`⟨𝓕⟩_bulk = −4k²⟨δδ'²⟩` sources from an **equal-time skew** of the field distribution (a third moment of the stationary measure π). A NESS current is a **flow** property (broken detailed balance, net circulation). These are different objects, and a current does not imply a skew.

The verify script makes this rigorous on a controlled 2-D Fokker–Planck system. Drift `A = −∇V + b` with symmetric `V = (x²+y²)/2` and a solenoidal rotation `b = ω(−y, x)`:

- **Genuine NESS:** `curl(A) = 2ω = 2.6 ≠ 0` (non-conservative, detailed balance broken); steady current `|J| ≠ 0`; `∇·J ≈ 10⁻⁴ ≈ 0` (stationary, divergence-free).
- **Symmetric equal-time π:** because `b·∇V = 0`, the stationary `π ∝ e^{−V}` is **unchanged** by the current. All odd/third moments vanish to machine precision: `⟨x³⟩ = 0`, `⟨xy²⟩ = 0`, `⟨x²y⟩ ~ 10⁻¹⁸`.

So a real circulating NESS current coexists with a perfectly symmetric equal-time distribution → **zero skew → `⟨δδ'²⟩ = 0` → clean horizon-only Λ**, *even though* detailed balance is broken.

## What this does to condition (b)

It sharpens (b) decisively. The catastrophe branch (`⟨𝓕⟩_bulk ≠ 0`) does **not** follow from the existence of the O(δ³) current; it requires the stationary measure π itself to carry an **O(δ³) third moment (skew)** — a *separate* effect from the current. The chirality lane's own characterization of π reports, at the orders computed: a **tilt at O(δ¹)** (a first-moment / mean shift — gradient-controlled away if uniform, per 0806) and a **steady current at O(δ³)** (a flow). It does **not** report an O(δ³) skew of π. On that characterization, the π-solenoidal (current-without-skew) case is the natural reading → **clean horizon-only Λ is the favored branch.**

This is a genuine de-risking, not a closure. Stated precisely:

> Condition (b) reduces from "is the bulk symmetric?" to the sharper, checkable question **"does the Mechanism-A stationary measure π acquire an O(δ³) third moment, or only the O(δ³) current (and the O(δ¹) tilt)?"** A current alone leaves Λ clean; only a π-skew would source a bulk residual.

## Contribution back to the (H-NESS) lift (cross-sector)

This decomposes the shared gate usefully for both lanes. The (H-NESS) lift must produce the field/η measure from the single-walker π; the DM-2 residual cares **only about that measure's third moment (skew)**, not its current. So when the chirality lane lifts π, the specific quantity DM-2 needs is "the O(δ³) skew of the lifted measure" — a single scalar diagnostic. If the lift shows the O(δ³) content is purely current (π-solenoidal), **both** results land cleanly: the chirality μ²-sign is set by the current (their "only sign-flip source"), and DM-2's Λ stays horizon-only (no skew). The two are not in tension; they read complementary parts of the same lifted measure.

## Honest status

- **Not closed.** Whether π has an O(δ³) skew is unresolved (the lift). 
- **Favored.** The current-vs-skew distinction makes clean-Λ the default; catastrophe requires an unreported π-skew.
- **Falsification-first caveat.** The 2-D demo shows a current *can* coexist with symmetric π (the π-solenoidal case); it does not prove the CPP current *is* π-solenoidal. A general NESS drift could skew π. The decisive check is the π third moment, now named as the sharp sub-target.

## Net-broadcast lemma — status after 0806–0810

- **(a)** weak-field at ZBW scale: **CLOSED** (0806).
- **(b)** bulk symmetry: **sharpened to a single scalar** — the O(δ³) skew of the lifted measure; current alone (established) leaves Λ clean; favored branch is clean-Λ; closure awaits the (H-NESS) lift, shared with chirality.

## Scope held

No verdict moved. No THEO, no ID. No chirality-lane edits (CHIR.md read-only). The cross-sector contribution is a decomposition offered to the shared lift, not a claim on the chirality verdict. SR.md / registry updates remain batched/deferred.
