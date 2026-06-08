# DM-2 — Residual↔Λ Identification, and the Cross-Sector Substrate-Parity Conjecture

**Patch:** 0807 (Session 156, 8 June 2026) · **Work item:** DM-2 / net-broadcast lemma condition (b) + cross-sector link
**Predecessor:** Step-1 parity result (0805), Step-2(a) gradient-control (0806).
**Verify:** `scripts/0807_residual_lambda_scaling.py` (bulk cancellation + 1/R_H² residual scaling).
**Grade:** CONJECTURE with mechanism + scaling support. **NOT a theorem; no verdict change.**

---

## 1. The identification

Step 1 showed the Sea's symmetric, zero-mean ZBW fluctuations source zero mean gravitation by parity (`⟨𝓕⟩ = 0`; 𝓕 is cubic-leading and odd-leading). The surviving gravitating piece is whatever *breaks* that parity. The conjecture developed here:

> **The surviving parity-breaking residual is the horizon-scale mode, and it is Λ.**

The mechanism is the finite causal Sea. Parity cancellation requires that each fluctuation have its antisymmetric partner *inside* the averaging region. On a causal patch of size `R ~ R_H`:

- **Sub-horizon modes** (wavelength ≪ R_H) fit many periods in the patch → their partners are present → `⟨𝓕⟩ = 0` exactly. The bulk vacuum does not gravitate.
- **The horizon-scale mode** (wavelength ~ R_H) spans only a fraction of a period in the patch; its antisymmetric partner would lie *beyond* the causal horizon and is absent → parity cancellation is **incomplete** → a nonzero residual `⟨𝓕⟩` survives.

So the IR boundary (finite causal extent of the Sea) breaks parity for exactly one mode — the longest one — and that uncancelled residual is the gravitating vacuum piece.

## 2. Scaling support (verify 0807)

Window-averaging the Step-1 cubic source `s = 2k²δ²δ''` over the patch `[0,R]` for `δ = sin(qx)`:

- Modes with integer periods in the patch (5, 2, 1 periods) give `⟨s⟩ = 0` to numerical precision — **bulk parity cancellation confirmed.**
- The horizon mode `q = π/R` gives a nonzero residual with `⟨s⟩·R² = const` across `R ∈ [0.5, 8]` — i.e. **residual ∝ 1/R²**.

This matches Step C (5b): `ρ_Λ ~ c⁴/(8πG R_H²)`. The IR-boundary-breaks-parity mechanism **reproduces the 5b Λ scaling**. The two results — Step-1's "what survives parity" and 5b's "largest gradient the finite Sea cannot cancel" — are revealed as the **same physics**, which also explains *why R_H enters* (the IR boundary is what breaks parity).

**Claimed here: the 1/R_H² scaling and the mechanism. NOT claimed: the exact coefficient or the Hubble-vs-event-horizon choice** — those are the 5b/D3 results (event horizon, `c ≈ 0.8`, `w_Λ ≈ −1.02`), unchanged. This patch unifies the *origin* of the residual with 5b; it does not re-derive 5b's number.

## 3. Honest gaps (this is a conjecture, deliberately quarantined)

- The demonstration uses a single sinusoidal mode on a 1-D interval. The full claim needs the 3-D mode sum over the causal patch and a proof that *all* sub-horizon contributions cancel (not just the symmetric representative tested).
- It assumes the bulk fluctuation spectrum is statistically symmetric (net-broadcast lemma condition (b)); §4 is where that assumption acquires physical content and its own risk.
- The handover's standing warning applies in full here: this is exactly the kind of elegant identification that it would be tempting to promote to a proof. It is recorded as a conjecture-with-mechanism so it is not mistaken for one.

## 4. The cross-sector substrate-parity conjecture (re: chirality emergent-vs-primitive)

Condition (b) — is the ZBW zero-point statistically symmetric? — is, at root, asking **whether the CPP substrate has a primitive handedness.** This is the same physical question the chirality arc is asking with its μ²-sign computation, and it is worth recording the link precisely so the two are **not conflated**.

**The shared root (conjecture):** the substrate either has a primitive parity asymmetry or it does not, and that single fact would manifest in *both* sectors:

- **If the substrate is parity-symmetric** (no primitive handedness): the ZBW zero-point is symmetric → the *only* parity breaking is the IR-boundary geometric effect of §1 → Λ is purely a finite-causal-patch residual, and the bulk vacuum has no intrinsic skew. In the chirality sector, this is the **chirality-emergent** branch.
- **If the substrate has primitive handedness:** the ZBW zero-point carries an intrinsic skew → an *additional*, non-geometric parity-breaking residual appears in the Sea → and in the chirality sector this is the **chirality-primitive** branch.

**What is genuinely linked vs what is not.** The link is the shared substrate-parity root — a real and interesting unification hypothesis. But the **computations are distinct and live in different sectors**: the chirality verdict moves on the μ²-sign via the η-susceptibility (`sign(μ²)=sign(m²)`), currently bottomed out at the H-NESS gap (other window, 0902); the DM-2 residual moves on the ZBW skew via the parity of `⟨𝓕⟩`. **Step 2(b) of DM-2 will not, by itself, resolve the chirality μ²-sign**, and the chirality sign will not, by itself, fix the DM-2 residual coefficient. They are two windows onto one substrate property, not one calculation.

**Recorded as:** a candidate cross-sector conjecture (substrate parity is the common root of the chirality-primitive question and the Sea parity-residual). **No ID minted** (registry freeze; the chirality registry is the other window's lane). If pursued, it would be registered jointly and would need *both* sector computations to agree on the substrate-parity sign — which, if it happened, would itself be strong cross-sector evidence.

## 5. Net-broadcast lemma status after 0805–0807

- **Condition (a)** — weak-field at the ZBW scale: **CLOSED** by gradient-control (0806). D2 is not OP1-gated.
- **Condition (b)** — ZBW zero-point symmetry: **reframed**, not closed. The bulk-vs-IR mechanism (§1–2) shows that *if* the bulk is symmetric, the residual is exactly the 1/R_H² horizon piece = Λ; whether the bulk carries an intrinsic skew is the substrate-parity question (§4), now linked to chirality.

## Scope held

No verdict moved (CONJ-COSMO-1 NOT-confirmed; chirality verdict untouched). No THEO, no ID minted, no shared-registry edits (SR.md / CHIR.md / theorem-registry all deferred or out-of-lane). The residual↔Λ identification is a conjecture; the cross-sector link is a candidate conjecture. Both recorded, neither promoted.
