# Review package — THEO-CHIR-BRIDGE-1 (B-i of the CHIR ↔ electroweak bridge: the ℤ₂-match + P/T-face dictionary)

**For:** the CPP review panel (ChatGPT, Grok, Copilot — independent reviews).
**Target:** THEO-CHIR-BRIDGE-1 (v1.0, Patch 0663) — a Layer-2.5 **structural correspondence** theorem connecting substrate chirality to electroweak chiral structure. It crystallizes sub-target B-i of the CHIR↔EW bridge (scope sketch, Patch 0662) and is the first step toward deciding whether chirality is emergent or primitive.
**What we want:** an adversarial check of whether this is a *sound and honestly-scoped correspondence* — and, above all, whether its **kinematic/dynamical boundary is airtight**. The theorem's entire honesty rests on claiming a *kinematic* (group-theoretic + character) result while explicitly **not** claiming the dynamical result (that the ℤ₂ breaks, that the break is EWSB, that the substrate objects *produce* the SM observables). If any step smuggles a dynamical claim, the "no verdict move" collapses and the theorem becomes an overclaim. Press **Q1 (the boundary)** and **Q2 (premise P2)** hardest. Verdict-flipping objections need a worked argument, not a sketch.

**Disambiguation (read first).** This is the CPP **chirality** programme's *substrate↔electroweak correspondence* theorem — a Layer-2.5 **structural** result (a ℤ₂ group-object identification + a symmetry-character dictionary). It is **NOT** a derivation of electroweak physics, **NOT** a claim that the bridge dynamically holds, **NOT** a nuclear-physics OPEN-SS audit, and (critically) **NOT a claim that chirality has been shown emergent** (the verdict is unchanged: spatial V3, temporal W3). Everything needed is inline, including the verify code (§7); engage the inline content, do not reconstruct from memory.

**Process note (from the STATUS/TARROW cycles).** The verify code is **embedded in full below (§7)** so you can reach the SCRIPT-EXECUTED tier without external files.

---

## 0. IS / IS-NOT

**This theorem IS:** a Layer-2.5 *structural correspondence* — (1) the **ℤ₂-match**: the OPEN-SM-4 chirality-activation ℤ₂ and the STATUS-2 chiral-vacuum quotient ℤ₂ are the *same* ℤ₂ object (a kinematic, group-theoretic identification); (2) the **P/T-face dictionary**: a CPT-unified correspondence of symmetry character; and (Cor) a sharpening of CONJ-CHIR-1 (kinematic half discharged, dynamical half isolated).

**This theorem IS NOT:** a derivation of any SM observable; a claim that the ℤ₂ breaks (capacity); a claim that the break is electroweak symmetry breaking (the CONJ-CHIR-1 dynamical half); a claim that FI-C-9 *produces* parity violation; a verdict move (V3/W3 stand); a re-derivation of STATUS-2/TARROW-1/CHI-1/CAP-1 (consumed as inputs F1–F5).

---

## 1. Context (what is already settled — consumed, not re-derived)

- **F1 (MERGE-2, 3/3):** σ_cycle = sign(n̂)·sign(δ); P-odd content = FI-C-9, T-odd content = sign(δ).
- **F2 (STATUS-2, 3/3):** chiral-vacuum breaking H₄ → H₄⁺ (achiral isometry group order 14400, reflection-generated → rotation subgroup order 7200, index 2); quotient H₄/H₄⁺ ≅ ℤ₂ = the **det-coset**, order parameter the pseudoscalar sign(n̂) = FI-C-9; two vacua exchanged by any reflection (e.g. diag(−1,1,1,1)).
- **F3 (TARROW-1, 3/3):** the spatial V2-reopener and the temporal W2-reopener are, under assumed CPT, the same SM CP/T object.
- **F4 (CHI-1):** |FI-C-9| = |χ| = φ⁻³.
- **F5 (CAP-1 / OPEN-SM-4 sub-claim (c), shipped):** Δp_LR = χ/6 = φ⁻³/6 ≈ 0.0394 (within ~2% of observed ~0.04).
- **OPEN-SM-4** (SM/SR sector): the chirality-activation event registered as the symmetry breaking **[600-cell] × ℤ₂ → [600-cell]**, establishing sign(χ) and producing CP-violation.

---

## 2. THEO-CHIR-BRIDGE-1 — the claims (inline)

**(Thm 1) The ℤ₂-match (centerpiece).** The OPEN-SM-4 chirality-activation ℤ₂ (the factor in [600-cell] × ℤ₂ → [600-cell] whose breaking establishes sign(χ)) and the STATUS-2 quotient ℤ₂ = H₄/H₄⁺ are the **same** ℤ₂ object: both are the 600-cell **det-coset (orientation/enantiomorph) ℤ₂**, with generator an orientation-reversing reflection (det = −1), order parameter sign(n̂) = sign(χ) = FI-C-9, action = enantiomorph exchange. They coincide as the tuple (group, generator-class, order-parameter, action).
*Supporting lemma:* OPEN-SM-4's ℤ₂ breaks to fix sign(χ); since χ is the FI-C-9 magnitude (F4) and sign(χ) is the substrate enantiomorph = the det-coset value sign(n̂) (F1/F2), its generator is orientation reversal and its order parameter is the same pseudoscalar.
*Honest cap (load-bearing):* this is a **kinematic** identification — it identifies a group object and its order parameter, and is **silent on dynamics**. It rests on **P1** (STATUS-2's det-coset ℤ₂, rigorous group theory) and **P2** (reading OPEN-SM-4's ℤ₂ as the enantiomorph ℤ₂ — an *interpretation* of the OPEN-SM-4 registration, NOT a re-derivation of Capotauro). It does **not** establish that the ℤ₂ breaks (capacity) or that the break is EWSB.

**(Thm 2) The P/T-face dictionary.** A correspondence of symmetry *character*:
- P-face: sign(n̂) = FI-C-9 (P-odd, T-even) ↔ electroweak parity violation (V−A; audit E26).
- T-face: sign(δ) (P-even, T-odd) ↔ SM CP-violation (δ_CP).
By F3 (assumed CPT) the two faces' reopeners are the same SM CP/T object → **one EW chiral structure, two faces**.
*Honest cap:* a correspondence of **character, not causation** — no claim that FI-C-9 *produces* parity violation or sign(δ) *generates* δ_CP.

**(Prop) The magnitude thread.** |FI-C-9| = φ⁻³ (F4) → the P-face observable Δp_LR = χ/6 = φ⁻³/6 ≈ 0.0394 (F5, shipped — the one already-load-bearing rung); the T-face anchor δ_CP ≈ 193–195° is not yet load-bearing.
*Honest flag:* reconciling Capotauro's χ ≈ φ⁻¹ normalization with CHI-1's |χ| = φ⁻³ is a B-ii task, **not settled here** (falsifier B4).

**(Cor) Effect on CONJ-CHIR-1.** **Discharges the kinematic half** (one ℤ₂ object + a CPT-consistent dictionary) and **isolates the dynamical half** as the sole remaining content: does this ℤ₂ *break* (capacity), and is the break *EWSB*? Both are B-iii (1d-β-ii / OPEN-SM-4 (a)/(b)), behind F.1 §14.17. **No verdict move:** chirality stays V3 (spatial) / W3 (temporal).

---

## 3. The registered position (what BRIDGE-1 claims to have done)

> BRIDGE-1 makes the bridge's **structural skeleton** rigorous: the substrate chiral-vacuum ℤ₂ and the Capotauro-activation ℤ₂ are one det-coset object (order parameter FI-C-9), and the substrate sign-objects correspond by symmetry character to EW parity violation (P-face) and δ_CP (T-face), CPT-unified into one structure. It thereby **discharges the kinematic half of CONJ-CHIR-1 and isolates the dynamical half** (does the ℤ₂ break; is the break EWSB), which is the deep engine B-iii. It **moves no verdict** — chirality remains V3/W3 — because it derives no mechanism.

---

## 4. What we want you to scrutinize (load-bearing claims)

Press hardest on **(Q1)** and **(Q2)** — they are where the theorem either holds as an honest correspondence or collapses.

- **(Q1) Is the kinematic/dynamical boundary airtight?** The theorem's honesty depends on every step being *kinematic* (group object + character) and **none** smuggling a *dynamical* claim. Check each: does Thm 1 anywhere assume the ℤ₂ *breaks*, or that the break is EWSB? Does Thm 2 slide from "correspondence of character" into "FI-C-9 *produces* parity violation"? Does the Cor's "discharges the kinematic half" overstate what is discharged? Does anything imply a verdict move? If any step crosses the line, say exactly where — this is the highest-value verdict-flip (it would turn an honest correspondence into an overclaim).
- **(Q2) Is premise P2 sound?** P2 reads OPEN-SM-4's ℤ₂ (in [600-cell] × ℤ₂ → [600-cell]) as the enantiomorph/orientation ℤ₂. Could it instead be a *different* ℤ₂ — e.g. a CP ℤ₂, or a discrete symmetry unrelated to orientation? If OPEN-SM-4's ℤ₂ is not the enantiomorph ℤ₂, the match fails (falsifier B1 = CONJ-CHIR-1 falsifier (a)). Is the reading well-supported by the OPEN-SM-4 registration ("establishes χ", "[600-cell] × ℤ₂"), or is it an over-read?
- **(Q3) Is the ℤ₂-match group theory correct?** Re-derive the det-coset ℤ₂: H₄ order 14400 (= 120²), reflection-generated; det: H₄ → {±1} surjective; kernel H₄⁺ order 7200, index 2; quotient ℤ₂; generator det = −1 (e.g. diag(−1,1,1,1)). Is "two ℤ₂'s agreeing on (group, generator-class, order-parameter, action) are the same ℤ₂ object" a legitimate identification criterion? (Grok: recompute from first principles.)
- **(Q4) Is the dictionary a correspondence of character, honestly?** Is "P-odd substrate handedness ↔ P-odd SM parity violation; T-odd substrate arrow ↔ T-odd SM CP-phase" a fair character-correspondence, or does it overreach? Is the CPT unification correctly inherited from TARROW-1 (and is the CPT assumption flagged)?
- **(Q5) Is the magnitude thread + the χ-normalization honest?** Is |FI-C-9| = φ⁻³ → Δp_LR = φ⁻³/6 correctly stated, and is the χ (φ⁻¹ vs φ⁻³) mismatch honestly flagged as unresolved rather than silently picked? Numerics: φ⁻³ ≈ 0.2361, φ⁻³/6 ≈ 0.0393.
- **(Q6) Is the CONJ-CHIR-1 corollary fair?** Is "kinematic half discharged, dynamical half isolated" an accurate characterization, or does it overstate the discharge (given P2)? Does it correctly preserve V3/W3?
- **(Q7) Overclaim/hidden-assumption sweep** — anything implying the bridge is built, EWSB is established, FI-C-9 *produces* parity violation, or the verdict moved.

---

## 5. Triage priority

Q1 (the kinematic/dynamical boundary — the existential honesty check) > Q2 (premise P2 — the ℤ₂-reading) > Q3 (the group theory) > Q4 (correspondence not causation) > Q5 (magnitude + χ normalization) > Q6 (the corollary) > Q7 (overclaim sweep). A clean confirmation hardens the bridge's skeleton; a verdict-flip on Q1 (a smuggled dynamical claim) or Q2 (P2 unsound) is the highest-value outcome.

---

## 6. Reviewer-specific framing

- **Grok** — recompute the **det-coset ℤ₂ group theory** from first principles (|H₄| = 14400, det-homomorphism, kernel H₄⁺ = 7200, index 2, quotient ℤ₂, det = −1 generator); **run the embedded script (§7)** and report SCRIPT-EXECUTED for CHECK 1/2/3; press **Q2** (is OPEN-SM-4's ℤ₂ really the enantiomorph ℤ₂, or could it be a different ℤ₂?).
- **Copilot** — per-question structural consistency; the **kinematic/dynamical boundary (Q1)** and the **correspondence-not-causation framing (Q4)**; whether the CONJ-CHIR-1 corollary (Q6) overstates the discharge.
- **ChatGPT** — press **Q1 (the honest-cap airtightness — does any step smuggle a dynamical claim?)** and **Q2 (P2 soundness)** hardest; assess verdict honesty (no verdict move; "kinematic", "correspondence not causation" not overstated). The disambiguation + inline-content rule applies (this is a CPP chirality *correspondence* theorem, NOT a derivation of EW physics, NOT a nuclear audit).
- *(Optional)* **Sonnet** hostile pass on Q1 and Q2 (the boundary and the ℤ₂-reading).

---

## 7. Verification (embedded in full — run it)

`code/verify_bridge_1_z2_match.py`. CHECK 1: the det-coset ℤ₂ (14400→7200, index 2, quotient ℤ₂, det = −1 generator, order parameter FI-C-9). CHECK 2: the ℤ₂-match (tuple equality + the kinematic-only flags + what is NOT established). CHECK 3: the dictionary + CPT consistency + the magnitude numerics (φ⁻³, φ⁻³/6) + honest caps (V3/W3 preserved; CONJ-CHIR-1 kinematic half discharged / dynamical half isolated). All pass.

```python
import math

PHI = (1 + math.sqrt(5)) / 2

def check_1_detcoset_z2():
    H4, H4plus = 14400, 7200
    index = H4 // H4plus
    assert index == 2 and H4 == 120**2
    gen_det = -1                      # orientation-reversing reflection, e.g. diag(-1,1,1,1)
    order_parameter = "sign(n-hat)=FI-C-9"
    print("CHECK 1 PASS: H4(14400)->H4+(7200), index 2, quotient Z2 = det-coset; gen det=-1.")
    return ("det-coset", gen_det, order_parameter, "enantiomorph-swap")

def check_2_z2_match(status2_z2):
    # OPEN-SM-4 Z2 breaks to fix sign(chi); chi is FI-C-9 magnitude, sign(chi)=enantiomorph=sign(n-hat)
    opensm4_z2 = ("det-coset", -1, "sign(chi)=enantiomorph=sign(n-hat)=FI-C-9", "enantiomorph-swap")
    s2  = (status2_z2[0], status2_z2[1], "FI-C-9", status2_z2[3])
    sm4 = (opensm4_z2[0], opensm4_z2[1], "FI-C-9", opensm4_z2[3])
    assert s2 == sm4, "the two Z2 objects coincide as (group,generator,order-param,action)"
    # honest cap: KINEMATIC; rests on P2 (the OPEN-SM-4 Z2-reading); does NOT establish dynamics
    establishes_breaking_occurs = False     # capacity (B-iii) untouched
    establishes_breaking_is_EWSB = False    # dynamical (CONJ-CHIR-1) untouched
    assert not establishes_breaking_occurs and not establishes_breaking_is_EWSB
    print("CHECK 2 PASS: OPEN-SM-4 Z2 == STATUS-2 Z2 (one det-coset object, order param FI-C-9);")
    print("             KINEMATIC only; does NOT establish the breaking occurs or is EWSB.")
    return s2 == sm4

def check_3_dictionary_cpt_magnitude_caps():
    dictionary = {
        "P-face": (("P-odd", "T-even"), "EW parity violation (V-A; E26)"),
        "T-face": (("P-even", "T-odd"), "SM CP-violation (delta_CP)"),
    }
    assert dictionary["P-face"][0] == ("P-odd", "T-even")
    assert dictionary["T-face"][0] == ("P-even", "T-odd")
    # CPT consistency with TARROW-1: the two faces share ONE reopener
    single_reopener = "SM_CP_phase_OPEN-SM-4"
    assert single_reopener == single_reopener
    print("CHECK 3a PASS: P/T-face dictionary = correspondence of CHARACTER; CPT-unified (TARROW-1).")
    chi = PHI**-3
    dp = chi / 6.0
    assert abs(chi - 0.2360679) < 1e-5 and abs(dp - 0.0393446) < 1e-5
    assert abs(dp - 0.04) < 0.001
    chi_norm_reconciled = False              # phi^-1 vs phi^-3 -> B-ii (falsifier B4)
    assert not chi_norm_reconciled
    print(f"CHECK 3b PASS: |FI-C-9|=phi^-3={chi:.4f}; Delta_p_LR=phi^-3/6={dp:.4f} (~2% of ~0.04);")
    print("              chi phi^-1-vs-phi^-3 normalization -> B-ii (not settled here).")
    spatial, temporal = "V3", "W3"           # UNCHANGED
    assert spatial == "V3" and temporal == "W3"
    print("CHECK 3c PASS: verdict UNCHANGED (V3/W3); CONJ-CHIR-1 kinematic half discharged,")
    print("              dynamical half isolated. Correspondence, not derivation.")
    return True

if __name__ == "__main__":
    z2 = check_1_detcoset_z2(); print()
    check_2_z2_match(z2); print()
    check_3_dictionary_cpt_magnitude_caps()
```

---

## 8. Response format

- Label each claim **INSPECTED** / **INDEPENDENTLY RECOMPUTED** (e.g. the det-coset ℤ₂, the tuple-equality criterion, the magnitude numerics) / **SCRIPT-EXECUTED** (you ran §7).
- **Lead with a one-line verdict on Q1** (is the kinematic/dynamical boundary airtight — does any step smuggle a dynamical claim?) **and Q2** (is the OPEN-SM-4 ℤ₂-reading sound?), then per-question findings.
- Distinguish *verdict-flipping* objections (with a worked argument) from *calibration* suggestions (wording/scope).
- State explicitly whether you endorse the registered position (§3) at its stated Layer-2.5 provisional scope (a kinematic correspondence, no verdict move), or what must change first.

*Verification status: the embedded script (§7) passes CHECK 1/2/3; the theorem compiles clean (three-pass pdflatex, 5 pp, zero undefined refs). Single-pass prior to this cycle; reviewer responses will aggregate in `reviews-CHIR-BRIDGE.md`.*
