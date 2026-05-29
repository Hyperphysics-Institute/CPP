# THEO-CHIR-CAP-1: Scope and Precondition Sketch

## The Capture/Partnering Handedness (audit E19) — Locating a Registered Source

**Patch 0639, Session 148** (29 May 2026)
**Sector:** CHIR (Substrate Chirality Arc) — third downstream target of the audit-spawned OPEN-CHIR-* programme, and **the deepest one**: E19 is the only entry the audit calls "the load-bearing dynamical chirality source," consumed by *every* SD-CHIR closure yet derived from no registered axiom.
**Resolves (target):** audit entry **E19** (D3 capture handedness) / **OPEN-CHIR-1c** (= **OPEN-CHIR-2d**, the dual listing).
**Status of this document:** scope-and-precondition sketch. Because E19 is the deepest unregistered entry, this sketch's discipline is the inverse of an eager closure: it must **locate a registered source or honestly conclude there is none**, and it must not manufacture a reduction. The sketch decomposes E19 into a registered-geometric piece (reachable) and a handedness-sign piece (the crux), and articulates — without asserting — the unifying hypothesis that the sign is the single frozen substrate-vacuum enantiomorph already registered as FI-C-9.

---

## §0 Working-session firewall and the no-false-reduction discipline

This sketch plans; it does not prove. E19 is where an over-eager reduction would do the most damage, because three published theorems (THEO-SD-CHIR-1/2, and the CONT arc downstream) *consume* the capture handedness; a spurious "derivation" would silently relabel a load-bearing input as a result. The discipline here: every proposed reduction step must terminate in a **registered** object (an axiom A1–A11, a registered FI, or an already-registered theorem output), and any step that imports an unregistered object is flagged as a gap, not a closure. The sketch's success criterion is an *honest map*, which may conclude "E19 is emergent" **or** "E19 is a genuine primitive that must be registered" — both are real outcomes.

---

## §1 The question

### §1.1 What E19 is

Audit entry E19 (dynamics-pass sub-question **D3**) is the **capture/partnering handedness**: when Conscious Points form Dipole Pairs (and when a CP is captured within a structure — e.g. the −eCP captured in a down quark, SS-2), does the partnering/capture step **prefer one handedness**? The audit's example: electric-positive CPs preferentially partnering with quark-negative CPs *in a specific orientation*. If the partnering rule is handed, chirality is sourced at the **dynamics** level, not the geometry level.

The audit's verdict (v1.1): **spatial/CP-asymmetric; unregistered**; "the load-bearing dynamical chirality source"; "consumed by SD-CHIR-1/2; derived from no registered axiom." It is the deepest unregistered entry (audit §6 conclusion: "consumed by every SD-CHIR closure… the omitted step being the derivation of the capture handedness").

### §1.2 Why it has the widest payoff

E19 is consumed by the pairing-convention generators of both shipped SD-CHIR theorems:
- **THEO-SD-CHIR-1** (W-bracelet): the audit states "the pairing-convention generator ζ^W (icosahedral-center inversion in 4D) **is the consumed capture handedness** (D3)."
- **THEO-SD-CHIR-2** (qDP/eDP): consumes ζ^qDP (host-CP inversion + n̂-flip + qCP-sign flip), "the CP-asymmetric variant of capture handedness (D3)."
- Downstream, the CONT arc (CONT-1/2/3) inherits whatever SD-CHIR supplies.

So a registered source for E19 retroactively grounds the ζ-generators of three theorems. Conversely, if E19 is irreducible, it should be *registered as a primitive* so the corpus stops treating it as silently-derived.

### §1.3 The dual listing (1c vs 2d)

E19 appears twice in CHIR.md: OPEN-CHIR-1c (under "derive the emergent entries") and OPEN-CHIR-2d (under "handle the unregistered entries"). The duplication encodes the open classification: 1c presumes E19 is *emergent* (derivable from n̂ + dynamics); 2d presumes it is *unregistered* (a genuine input to be handled). This sketch's decomposition (§3) is what will collapse the duplication, by determining which presumption holds.

---

## §2 Existing groundwork

### §2.1 The registered pairing/capture ingredients

The framework already registers several pairing/capture dynamics (master_glossary):
- **Polarity pairing (PROP-SS-5-1):** a ZBW attractive edge requires *opposite* polarities at its endpoints; (+,−) bonds, (+,+)/(−,−) do not. **Registered, but polarity-based — it fixes *which* CPs pair, not the chiral *orientation* of the pairing.**
- **ZBW / partner switching:** a CP oscillates between its left and right partner DPs (the Compton-frequency jitter). The left/right alternation is spatial but not, on its face, handed.
- **Capture:** a CP captured within a structure (the linear-oscillator −eCP in a down quark, SS-2). A genuine dynamical capture event.

None of these *registered* rules states a handedness preference. The handedness — *which* chiral orientation the pairing/capture selects — is the unregistered increment E19 names.

### §2.2 The ζ-generators are the consumed handedness — and they are built from registered objects

The decisive datum (audit §7): the capture handedness, *as actually consumed*, is the SD-CHIR Z₂ pairing-convention generator ζ. And ζ is **not** an ad-hoc rule; it is a registered-geometry construction:
- **ζ^W:** the affine involution p ↦ φn̂ − p (icosahedral-center inversion in the 4D ambient), linear part −I. Built from **n̂ = v_host** (FI-C-RC-1/2) + the **600-cell geometry** (A2). Its linear part flips n̂ (chirality-flipping).
- **ζ^qDP:** host-CP spatial inversion (v → −v) + n̂-flip + **qCP-sign flip** (the charge-conjugation factor). Built from spatial inversion + n̂ + the **CP polarity/type structure of A1**.

So the geometric content of E19 is already registered. What is *not* yet pinned is (a) why these specific involutions, and (b) the handedness **sign** they carry — see §3.

### §2.3 Grok's review-seed and ChatGPT's calibration

Grok (AUDIT-1 review) proposed: capture handedness = sgn(n̂·(displacement × polarization)) at the capture step. ChatGPT calibrated it down: "a reasonable construction… but it is not a derivation: it introduces displacement, polarization, a cross product, and a capture rule **without showing that these are already present in the framework**" → E19 stays unregistered. **This sketch's §3.2 directly answers ChatGPT's objection** by replacing Grok's unregistered vectors with the registered ζ-involution structure of §2.2.

---

## §3 Decomposition and the registered-source proposal

### §3.1 The structural form: involution × sign

A handedness is a *signed* datum (left vs right). An involution ζ (ζ²=1) is *not* — it relates a configuration to its mirror/inverted partner without preferring one. So the capture handedness decomposes as
$$
\text{(capture handedness, E19)} \;=\; \underbrace{\zeta}_{\text{registered-geometric involution (§2.2)}} \;\times\; \underbrace{\sigma_{\text{capture}}}_{\text{the handedness sign (the crux)}},
$$
exactly parallel to the E20 result ω_PCD = σ_cycle · n̂ (a registered-geometric axis × a sign). This parallel is not incidental: it is the cross-link THEO-CHIR-PCD-ORIENTATION-1 flagged.

### §3.2 Sub-gap 1c-α — ground the involution in registered geometry (near-term; THEO-CHIR-CAP-1)

**Target:** show the capture handedness's geometric factor is the registered ζ-involution (n̂ + 600-cell + charge-conjugation), replacing Grok's unregistered triple product. The registered analog of Grok's sgn(n̂·(v₁×v₂)) uses two **specific first-shell 600-cell vertices** v₁, v₂ (registered objects via A2), making the pseudoscalar a registered construction; and it identifies that pseudoscalar's vanishing/structure with the ζ-parity bookkeeping already used in SD-CHIR. Plausible layer: **Layer 2/2.5** (a structural grounding over registered objects). This is the reachable piece — it answers ChatGPT's "not shown to be in the framework" objection. Reserved theorem ID: **THEO-CHIR-CAP-1**.

### §3.3 Sub-gap 1c-β — the handedness sign σ_capture (the crux)

**Target:** determine the source of σ_capture. Three candidate resolutions, to be distinguished, not assumed:

- **(R1) σ_capture = the FI-C-9 frozen enantiomorph (the unifying hypothesis).** ζ^W flips n̂ (its linear part is −I); the substrate's choice of *which* of {n̂, −n̂} is physical is exactly the FI-C-9 frozen substrate-vacuum chirality sign ("the sign of χ… a frozen boundary condition coeval with the existence of CPs," Capotauro FI-C-9 note). Under R1, σ_capture is **not a new primitive** — it is the single registered FI-C-9 enantiomorph, and E19 is **emergent** from {ζ (registered geometry), FI-C-9 (registered sign)}. This is the elegant outcome: one substrate chirality sign (FI-C-9) sources the capture handedness (E19), the cycle orientation (E20/σ_cycle), and the n̂-vs-−n̂ choice alike.
- **(R2) σ_capture = σ_cycle (merge with E20).** The capture occurs *during* the PCD cycle, so its orientation may be inherited from the cycle's temporal direction. Under R2, E19 and E20 share one sign; this *merges* the two entries (programme-positive) per the THEO-CHIR-PCD-ORIENTATION-1 §5.3 cross-link. R1 and R2 are compatible if σ_cycle itself traces to FI-C-9.
- **(R3) σ_capture is a genuinely independent sign.** Then E19 is an irreducible **primitive** and the honest outcome is to *register* it (promoting it from "unregistered/overlooked" to "registered primitive"), not to manufacture a reduction.

The decisive test: does ζ^W/ζ^qDP's handedness sign *follow* from the FI-C-9 enantiomorph (R1), or is it an independent choice (R3)? Concretely: is the chirality-operator matrix-element sign in SD-CHIR fixed by the n̂-orientation (FI-C-9) alone, or does it require an extra input? This is answerable from the existing SD-CHIR proof chain (the ζ-parity bookkeeping) and is the substance of 1c-β.

### §3.4 Honest layer and E19's classification

E19 stays **unregistered** until *both* 1c-α (involution) and 1c-β (sign) resolve. The scope does **not** close it. If 1c-α + 1c-β(R1/R2) succeed, E19 → **emergent (provisional)** (registered ζ × registered FI-C-9 sign), collapsing the 1c/2d duplication onto 1c. If 1c-β resolves to R3, E19 → **registered primitive** (collapsing onto 2d). The sketch deliberately keeps both terminal outcomes live; this is the no-false-reduction discipline (§0).

---

## §4 Section structure of the eventual THEO-CHIR-CAP-1 artifact (1c-α, + a 1c-β verdict)

~7 sections, Layer 2/2.5:

1. **Setup** (~40 lines): E19, the involution×sign decomposition, the registered-source goal, the no-false-reduction discipline.
2. **The registered pairing/capture ingredients** (~50 lines): polarity pairing (PROP-SS-5-1), ZBW partner-switching, capture (SS-2) — and the gap each leaves (polarity ≠ handedness).
3. **The ζ-involution is registered geometry** (~70 lines): ζ^W = p ↦ φn̂ − p (n̂ + A2); ζ^qDP (+ charge-conjugation, A1); the registered analog of Grok's pseudoscalar via two first-shell vertices; identification with the SD-CHIR ζ-parity bookkeeping. **Closes 1c-α.**
4. **The handedness sign** (~70 lines): the involution≠sign subtlety; the FI-C-9 enantiomorph (R1) and σ_cycle-merge (R2) hypotheses; the decisive test against the SD-CHIR matrix-element sign; the **verdict** (R1/R2 emergent, or R3 register-as-primitive). This section's honesty is load-bearing.
5. **Cross-link to E20** (~30 lines): the parallel ω_PCD = σ_cycle·n̂ ↔ E19 = ζ·σ_capture; the merge condition; whether the programme now carries one chirality sign or two.
6. **Layer, what is/not claimed, classification verdict** (~40 lines): Layer 2/2.5; E19 → emergent (provisional) or registered-primitive per §4 verdict; FI-C-9 not eliminated by either outcome (R1 *uses* FI-C-9's sign; it does not derive it — that remains 1d-β's deep target).
7. **Conclusion + falsifiers** (~25 lines).

A `verify_capture_involution.py` (Tier 2/3) confirming ζ^W = p ↦ φn̂ − p is an involution flipping n̂, the registered-vertex pseudoscalar construction, and the ζ-parity/ matrix-element sign relation, is bundled.

Falsifiers: (F1) the geometric factor of E19 is shown *not* to be the ζ-involution (some other involution or a non-involution); (F2) σ_capture shown independent of both FI-C-9 and σ_cycle (forces R3 — E19 a new primitive); (F3) the ζ handedness sign shown to require an input beyond {n̂, FI-C-9, A1 charge-conjugation} (breaks the emergent claim).

---

## §5 Precondition and honesty notes

- **No false reduction (§0).** The artifact must terminate every step in a registered object. If 1c-β cannot identify σ_capture with a registered sign, the honest verdict is R3 (register E19 as a primitive), *not* a forced reduction.
- **The involution ≠ handedness subtlety** is the technical heart: do not conflate "ζ is registered geometry" (true, 1c-α) with "the handedness is derived" (requires the sign, 1c-β). E20's resolution had the same shape (axis registered; sign = temporal primitive); E19's sign is the open analog.
- **FI-C-9 is not eliminated by any outcome here.** Under R1, E19 *consumes* the FI-C-9 enantiomorph sign; deriving that sign (the symmetry-breaking dynamics) is 1d-β, the deep deferred target. E19's resolution is about whether the capture handedness is *a further primitive* beyond FI-C-9 + n̂, not about deriving FI-C-9 itself.
- **The merge is a hypothesis, not a result** (R2): keep E19 and E20 distinct in the record until the sign-identification is proven; the THEO-CHIR-PCD-ORIENTATION-1 cross-link is preserved as flagged-not-resolved.
- **qDP charge-conjugation:** the ζ^qDP qCP-sign flip is the one ingredient beyond pure geometry; it is registered (A1 CP polarity/type), but the artifact must show the *combined* CP operation's handedness still reduces to {n̂, FI-C-9, charge-conjugation} and introduces no fourth input.

---

## §6 Patch sequence

- **Patch 0639 (this patch):** this scope sketch; reasoning fragment; CHIR.md OPEN-CHIR-1c/2d update (the involution×sign decomposition; the R1/R2/R3 outcomes; the registered-source proposal replacing Grok's seed; THEO-CHIR-CAP-1 reserved for 1c-α). No theorem-registry proved-row.
- **Patch 0640+ (target):** the THEO-CHIR-CAP-1 artifact (1c-α involution grounding + the 1c-β sign verdict) + reasoning + verify script, after the SD-CHIR ζ-parity/matrix-element sign relation is checked (the decisive 1c-β test). Plausibly preceded by a short read of the SD-CHIR proof chain's sign bookkeeping.
- **Deferred:** if the verdict is R3, registering E19 as a primitive is itself the closure (no further derivation possible); if R1/R2, the residual FI-C-9-sign derivation is 1d-β (already deferred).

---

## §7 What the eventual artifact contributes

It grounds the ζ-generators of three shipped theorems (SD-CHIR-1/2 + CONT downstream) in registered objects, answering the standing "is the capture handedness in the framework?" objection (ChatGPT). It either (R1/R2) reduces E19 to {registered geometry × the one FI-C-9 chirality sign} — collapsing E19, E20, and the n̂-orientation onto a single substrate enantiomorph, the programme's most unifying chirality statement — or (R3) honestly registers E19 as an irreducible primitive, stopping the corpus from treating a load-bearing input as silently derived. Either outcome retires the deepest unregistered entry of the audit.

---

## §8 References

- `chirality_audit/theo_chir_audit_1.tex` (v1.1) — E19 / D3 (the deepest unregistered entry); the existing-derivation pass identifying ζ^W/ζ^qDP as the consumed capture handedness; the audit §6 conclusion.
- `chirality_audit/review/reviews-CHIR-AUDIT-1.md` — Grok's E19 seed (sgn(n̂·(displacement×polarization))); ChatGPT's calibration ("not shown to be in the framework").
- `theorem-registry.md` — THEO-SD-CHIR-1 (ζ^W = icosahedral-center inversion p ↦ φn̂ − p; the consumed D3); THEO-SD-CHIR-2 (ζ^qDP combined CP; the CP-asymmetric variant); FI-C-9 (the frozen substrate-vacuum enantiomorph sign).
- `chirality_derivations/theo_chir_pcd_orientation_1.tex` — the E20 resolution (ω_PCD = σ_cycle·n̂) and the §5.3 E19 cross-link (the merge condition); the involution×sign parallel.
- `master_glossary.md` — Polarity pairing (PROP-SS-5-1); ZBW / Partner switching; capture (SS-2 linear oscillator); PCD (Perceive-Compute-Displace, confirming "capture" is DP-pairing, not drift terminology).
- `capotauro/sketches/Capotauro_chi_phi_closure.md` — FI-C-9 note (the chirality sign as a frozen boundary condition, the R1 anchor).
- `axiom-registry.md` — A1 (CP polarity/type, the charge-conjugation source for ζ^qDP); A2 (600-cell geometry, the ζ^W inversion source).
- `frontier_sectors/CHIR.md` — OPEN-CHIR-1c / 2d; E19; the sibling E20/E21 resolutions.

---

**Scope document complete.** Patch 0639 commits this sketch + reasoning + the CHIR.md update. The artifact (THEO-CHIR-CAP-1) ships at Patch 0640+ once the SD-CHIR ζ-sign bookkeeping is checked (the 1c-β decisive test). The honest finding: E19's *geometric* factor is the already-registered ζ-involution (1c-α, reachable — this answers the reviewer objection); its *handedness sign* is the crux (1c-β), with the unifying hypothesis that it is the single FI-C-9 frozen enantiomorph (R1, → E19 emergent), the live alternative being a genuinely new primitive (R3, → register E19). E19 stays unregistered until both resolve.
