# reviews-SF-6.md — SF-6 v0.2 Review Cycle 1 (4-reviewer panel)

**Artifact:** SF-6 v0.2 DRAFT — electromagnetism flagship (Patch 1600–1603).
**Package:** `flagship_papers/electromagnetism/review/sf-6_review_package_v1.0.md` (Patch 1603).
**Panel:** ChatGPT, Grok, Gemini, Copilot (single-document dispatch per `templates/review_dispatch_protocol.md` v1604).
**Cycle close:** Patch 1605 (this aggregation) → restate to v0.3 (Patch 1606).

---

## 1. Verdict tally

| Reviewer | SCRIPT-EXECUTED | T1 | T2 | T3 | T4 | T5 | SHIP verdict |
|----------|:---:|:--:|:--:|:--:|:--:|:--:|--------------|
| **Grok** | ✅ all pass | PASS | PASS (genuine reframing) | open OK | sound | fine | **SHIP v1.0** |
| **Gemini** | — | PASS | "definition dressed as derivation"; no-new-postulates holds | open OK | sound | fine | **SHIP v1.0** |
| **Copilot** | — | PASS | "relabeled definition, not a derivation" (obj. 1) | open OK | sound | fine | **advance v1.0, no restate** (2 objections to tighten) |
| **ChatGPT** | ✅ all pass | PASS | "not yet a derivation" (verdict-flipping) | "verdict-flipping unless named falsifier" | sound | fine | **restate to v0.3** |

**Two reviewers ran the embedded §7 code (Grok, ChatGPT); both report all Tier-1 identities pass** (`c=299792458`, `Z0=376.730314`, `h=2πℏ`, `mc²=ℏν_C`, `ω_max=6.425e43`, `ln(ω_max/ω_g)=65.01`).

---

## 2. Per-triage synthesis

**T1 — two-tier rigor honesty: 4/4 PASS (unanimous).** No reviewer found a leak where a Tier-2 toy-model constant (`μ0, ε0, c, γ(v)`) reads as Tier-1/zero-parameter. OPEN-FP-6-CONSTANTS is the agreed-correct disposition. One refinement (ChatGPT/Copilot): the phrase "Tier-1 inter-constant identities" can sound stronger than it is — they are *algebraic consistency identities among accepted constants*, not first-principles CPP derivations. → calibration, §7 / data-availability.

**T2 — the E=ℏν_C unification: the convergent finding.** Three of four (Gemini, Copilot, ChatGPT) state plainly that the unification is a **definitional / ontological identification**, not a mathematical derivation: `ν_C = mc²/ℏ` (standing) and `ν_C = ν` (traveling) are *assignments* matching the standard Compton/Planck–Einstein relations, and the `E²=(mc²)²+(pc)²` dispersion is *imported* from SR-1, not substrate-derived. Grok dissents mildly — calls it a "genuine substrate-level reframing, not a disguised definition" — but even Grok does not claim it is a *derivation*. The paper's current language ("derived in c06 with no new postulates," "the most rigorous result") therefore **overclaims**. ChatGPT and Copilot raise this at verdict-flipping level. **Convergent fix:** relabel as a substrate-level *identification* / *ontological reduction* (mass + photon → one ZDC pattern); soften "no new postulates" → "no new postulates beyond the companion framework"; state explicitly that the `ν_C` assignments match standard relations and the SR dispersion is imported. (Gemini's framing: own that the value is the *ontological reduction*, not novel predictive math.)

**T3 — Michelson–Morley tension.** All four agree it is currently handled honestly (open tension + falsifier, no resolution claimed). ChatGPT elevates it to verdict-flipping with a precise condition: survivable **only** if it is an explicit, prominent, **named flagship-level open falsifier**, with any language implying it is "basically resolved" removed; the SSV-independent-`Z0` route must read as a *research direction*, not a *resolution sketch*. Copilot's obj. 2 agrees the `Z0` conjecture is under-motivated and should be marked a possible (not preferred) route. Grok suggests adding one explicit falsifier sentence. **Convergent fix:** name the falsifier explicitly in §5/§9; mark SSV-independent-`Z0` as a direction not a resolution; scrub any "resolution" wording (conclusion §13 currently says "pending the SSV-independent-Z0 resolution" — change "resolution" → "route").

**T4 — EMHAND re-scope: 4/4 sound.** The parity-obstruction argument (P-even EM can express but not source P-odd handedness) is endorsed by all four; the re-scope to "EM-phenomenology expression of the closed manifestation (iii)" is correct. Keep as "phenomenology owed," not "closed" (ChatGPT).

**T5 — scope / breadth / partition: 4/4 fine.** Synthesis-not-derivation posture correct; NO-THEO / count-unchanged correct; photon-vs-cage-boson partition airtight (no double-assignment); TP-1 band-top a genuine imported consistency thread (not to be sold as SF-6 evidence — ChatGPT).

---

## 3. Disposition

**RESTATE to v0.3** (not 3/3 SHIP). Rationale: although three reviewers voted SHIP, the panel's *substance* converges on a real overclaim in the T2 language ("derived" / "most rigorous result" for what is an ontological identification), and ChatGPT + Copilot raise it at verdict-flipping level. Per the programme's "the verdict comes from the text" discipline, the text overclaims and is fixed, not defended. The fix is wording-only — the physics is sound and the breadth is earned — so v0.3 is a light restate, after which the cycle closes (every reviewer's substantive ask is satisfied):

**v0.3 changes (Patch 1606):**
1. **T2 relabel** (abstract, §1 box, §3): E=ℏν_C is a companion-grade substrate-level *identification* / *ontological reduction*, not a mathematical derivation; the `ν_C` assignments match standard Compton/Planck–Einstein relations; the SR dispersion is imported from SR-1; "no new postulates" → "no new postulates beyond the companion framework." Remove "most rigorous result." Own the ontological-reduction value (Gemini).
2. **T3 tighten** (§5, §9, §13): name the `c_eff(v)` falsifier explicitly as a flagship-level open falsifier; mark SSV-independent-`Z0` as a research direction, not a resolution; change conclusion's "SSV-independent-Z0 resolution" → "route."
3. **Boxed warning** (§1 box, ChatGPT): "SF-6 does not derive μ0, ε0, c, γ(v), or the Michelson–Morley null from first principles."
4. **Calibrations:** §7/data-availability — Tier-1 identities are algebraic consistency relations among accepted constants, not first-principles CPP derivations (ChatGPT/Copilot); §4 Maxwell — one-line reminder μ0, ε0 remain Tier-2 (Copilot); §3 — c06 cross-ref at the nucleation-center first mention (Grok).

No re-review required: all four converge, and the fix is the relabel/tightening they jointly requested. v0.3 is SHIP-ready on the strength of 3 prior SHIP votes + ChatGPT's restate condition being exactly what v0.3 does.

---

*Aggregated Patch 1605 per `templates/review_dispatch_protocol.md` §6. Four-reviewer panel; 2/4 SCRIPT-EXECUTED (Grok, ChatGPT), all Tier-1 identities pass. Verdict: restate to v0.3 on the convergent T2 overclaim + T3 falsifier-naming, then close. NO THEO; swarm count unchanged.*
