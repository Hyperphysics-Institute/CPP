# DM-2 — Step 2(b): Is the Bulk ZBW Statistically Symmetric? (the last open condition)

**Patch:** 0809 (Session 156, 8 June 2026) · **Work item:** DM-2 / net-broadcast lemma condition (b)
**Predecessor:** Step-2(a) (0806, condition (a) closed); residual↔Λ (0807).
**Verify:** `scripts/0809_step2b_symmetry.py` (third-moment reduction + ensemble symmetry test).
**Grade:** CONDITIONAL result. No verdict change.

---

## What (b) actually is

After Step 2(a) closed condition (a) (D2 is not OP1-gated; gravitation is gradient-controlled), the net-broadcast lemma has one open condition: is the bulk ZBW zero-point statistically symmetric, so the Step-1 parity cancellation holds and the only gravitating residual is the IR-boundary horizon mode (= Λ, per 0807)?

## (b) reduces to a third moment

Over a closed/periodic causal patch the Step-1 cubic source integrates by parts to a pure third moment of the ZBW field:

    𝓕 = 2k² δ² δ''   ⟹   ⟨𝓕⟩_bulk = −4k² ⟨δ δ'²⟩.

The integrand `δ δ'²` is **odd under the field-amplitude flip δ → −δ**. So:

- **Symmetric bulk** (zero skew / vanishing third moment): `⟨𝓕⟩_bulk = 0` — the bulk vacuum does not gravitate; only the IR-boundary horizon residual survives → clean horizon-only Λ (0807).
- **Skewed bulk** (nonzero third moment): `⟨𝓕⟩_bulk ≠ 0` — a *uniform* intrinsic vacuum source, additional to the horizon residual.

The ensemble test (verify) confirms it: averaged over realizations, `⟨δ δ'²⟩ = −0.08 ± 0.09` for a symmetric field (consistent with zero) and grows with skew (`23, 78, 348` for skewness `0.5, 1.3, 1.9`).

## Why (b) is load-bearing — and not automatic

If the bulk skew is unsuppressed at the Planck/ZBW scale, `⟨𝓕⟩_bulk ~ k²⟨δδ'²⟩` is a *uniform vacuum source of Planck magnitude* — the cosmological-constant catastrophe, re-entering through the third moment. So a clean horizon-only Λ **requires** the bulk O(δ³) skew to vanish or be suppressed.

Is it automatic? **No.** The 600-cell is *achiral* (its symmetry group H₄ contains reflections), so there is no **static** source of skew — any net skew must be **dynamical**. And the substrate dynamics are not an equilibrium: the chirality lane has established (Patch 0689, read-only here) that the Mechanism-A substrate process **violates detailed balance, with a steady current onsetting at O(δ³)** — a genuine non-equilibrium steady state (NESS). So symmetry of the bulk ZBW is exactly what is *not* guaranteed at O(δ³).

## The shared gate: (b) and the chirality μ²-sign require the same (H-NESS) lift

The structural match between this and the chirality sector is exact at the decisive order:

| | symmetric / even part | decisive term | the open lift |
|---|---|---|---|
| **DM-2 (b)** | O(δ⁰–δ²): `⟨𝓕⟩=0` (parity) | **O(δ³)**: `−4k²⟨δδ'²⟩` (skew/current) | single-walker NESS π → **field measure** ⟨δδ'²⟩ |
| **Chirality μ²-sign** | O(δ⁰–δ²): tends μ²>0 | **O(δ³)**: NESS current, "the only sign-flip source" | single-walker NESS π → **η-field measure** (**H-NESS**) |

Both sectors: a benign even part, a decisive **O(δ³)** term tied to the detailed-balance-violating NESS current, and the same outstanding operation — **lifting the single-walker stationary measure π to the field-level measure** (named **(H-NESS)** in the chirality lane). The observables read off the lift differ (a μ²-sign there; a bulk vacuum residual here), but **the lift is the same mathematical object.** Progress on (H-NESS) in the chirality lane therefore advances DM-2's condition (b) directly, and vice versa.

This is a stronger statement than the §4 "shared root" of 0807: it is not merely that both touch substrate parity — it is that both **bottleneck on the identical NESS-lift**, at the identical order. That is a concrete shared gate, not an analogy.

## Verdict: CONDITIONAL — DM-2's Λ-cleanliness is gated on (H-NESS), the same gate as chirality

- **Not a kill.** A genuine possibility the lift may realize: the O(δ³) NESS object is a *steady current* (divergence-free circulation), and a pure circulation need not accumulate into the scalar `⟨δδ'²⟩` — in which case `⟨𝓕⟩_bulk = 0` survives and Λ is cleanly horizon-only. This is for the lift to decide; it is **not claimed here.**
- **Not closed.** Whether the bulk O(δ³) skew nets to zero in the field measure is exactly (H-NESS), unresolved in either lane.
- **Located.** DM-2's last open condition is not an independent new problem; it is the same lift the chirality arc is already working (currently blocked at the F.1 §14.17 → (H-NESS) reduction).

## Net-broadcast lemma — final status of this arc

- **(a)** weak-field at the ZBW scale: **CLOSED** (0806, gradient-control). D2 not OP1-gated.
- **(b)** bulk ZBW symmetry: **reduced and located** — `⟨𝓕⟩_bulk = −4k²⟨δδ'²⟩`, gated on the (H-NESS) lift, shared with the chirality μ²-sign. Open.

So DM-2's decisive gate (R2/OPEN-SR-5) is closed **except** for the (H-NESS) lift, which it now shares with chirality. The Λ magnitude/coefficient remains the separate 5b/D3 event-horizon result (unchanged).

## Recommended forward home: a cross-sector umbrella paper (for Thomas to register)

The (H-NESS) lift is now the common gate to (i) the chirality primitive-vs-emergent verdict (μ²-sign) and (ii) the DM-2 Λ-cleanliness. That shared gate is the natural spine of a **cross-sector umbrella paper**: "the O(δ³) NESS current of the substrate as the common origin of the chirality sign and the dark-energy residual." **Recommended, not registered here** — it spans the chirality lane and `future_projects.md` (a shared registry under freeze), so registration is left to Thomas as single integrator. Suggested stub: *PROJECT — Substrate-NESS umbrella: the O(δ³) detailed-balance-violating current as the shared gate of CHIR μ²-sign (H-NESS) and DM-2 Λ-cleanliness; deliverable contingent on the (H-NESS) lift.*

## Scope held

No verdict moved (CONJ-COSMO-1 NOT-confirmed; chirality verdict V3/W1-conditional untouched). No THEO, no ID minted. No edits to the chirality lane (CHIR.md read-only), no shared-registry edits (SR.md, future_projects.md, theorem-registry all deferred to a batched patch / to Thomas). The structural match is reported as a shared-gate finding; literal identity of the two lifts would need both lanes to confirm.
