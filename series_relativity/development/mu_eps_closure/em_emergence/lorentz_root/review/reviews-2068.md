# reviews-2068 — panel responses, synthesis, and cycle-close for the Round-4 finding

**Artifact:** Round-4 finding (Patch 2068): the periodic-lattice Lorentz no-go, and CPP's quasicrystal
evasion of it. **Package:** `review/2068_round4_review_package_v1.0.md` (Patch 2069). **Cycle closed:**
Patch 2070. **Outcome:** unanimous SOUND / SOUND-WITH-CALIBRATION, **no verdict-flip**. **A panel verdict on
a FINDING — not a THEO. No status/registry move here; the OPEN-SR-10 / R2 world-call sharpening follows
separately under STOP-and-warn on TLA's nod.**

---

## 0. Reviewer-identity caveat (read first) — the inline fix did NOT fully hold

This cycle added an explicit identity instruction to the dispatch (§6/§8: "put YOUR OWN model name; do not
adopt another reviewer's label"). **It did not fully work.** Three responses returned: one self-labelled
"Grok" (consistent), one self-labelled "Copilot" (carrying a Gemini-style reasoning trace), and one
self-labelled "ChatGPT" (INSPECTED, "Thomas — here is your full review… as ChatGPT") that **TLA identified
as actually Copilot.** So the self-labels remain unreliable even with the instruction present.

**Handling (unchanged from prior cycles):** attribute by **content + tier**, treat the three as **three
independent responses (≥3 distinct engines)**, do **not double-count**, and note the verdict is
label-independent (all SOUND/SOUND-WITH-CALIBRATION, no flip), so the cycle-close is unaffected.

**Escalated recommendation for TLA (the wording fix is insufficient — this is model-side):** the most
robust remedy is to make identity unambiguous *outside* the model's discretion — e.g. (a) TLA labels each
response on receipt (which TLA already did here), or (b) prepend a **one-line per-reviewer header** to each
paste ("YOU ARE COPILOT.") so the block is identical except that single line. Option (b) keeps the
single-document spirit while removing the self-ID failure mode. Flagged, not actioned (the dispatch template
is shared infra — STOP-and-warn).

## 1. Per-response verdicts (attributed by content/tier; not double-counted)

| # | Self-label (unreliable) | TLA/content read | Tier | Overall | Distinguishing content |
|---|---|---|---|---|---|
| R1 | Grok | Grok | SCRIPT-EXECUTED + INDEP. RECOMPUTED | SOUND | ran §7 (reproduced collapse + ×11); recomputed Coxeter list + harmonic tower |
| R2 | Copilot (Gemini-style trace) | distinct engine | SCRIPT-EXECUTED | SOUND-WITH-CALIBRATION | T4 dense-Fourier-module / Bragg-peaks caveat (the substantive one) |
| R3 | ChatGPT | **Copilot** (per TLA) | INSPECTED | SOUND-WITH-CALIBRATION | T2 "theorem-grade"; T1/T5 "W3 excluded → conditional on A3/A3′,C3"; reconciliation framing |

**Script execution.** Two responses ran §7; both reproduce the phase-speed collapse (≈0.99→0.69–0.80 across
seeds), the single-shell ~1×10⁻⁷ at q=0.15, and the ×11-but-nonzero two-shell suppression. (Absolute
v_phase values differ slightly by RNG seed — expected; the *pattern* is robust.)

## 2. Triage resolution (cross-response)

| # | Question | Consensus | Resolution in v1.1 |
|---|----------|-----------|--------------------|
| **T1** scope / non-overclaim | **SOUND.** W1 properly NOT proven; Part-B numerics honestly down-weighted. One calibration: "W3 EXCLUDED" should carry "conditional on A3/A3′ and C3 (pending OPEN-SR-9)" since the causal-broadcast Lorentz invariance is axiom-level. | "W3 excluded" now carries the given-A3/A3′/C3 qualifier; "does not bite CPP" → "CPP is aperiodic by construction." |
| **T2** Part-A no-go airtightness | **SOUND — "theorem-grade" (all three).** Bounded BZ-periodic symbol (a Fourier series) cannot equal unbounded c|k| nor be exactly isotropic; holds for **infinite-range** periodic too. Harmonic-tower (finite shells cancel finitely many of l=6,10,15,…) correct. | No change to the argument; banner records "theorem-grade" + the infinite-range point. (Still NOT registered as a THEO — earned only through the full process.) |
| **T3** Part-B substrate-structure (load-bearing) | **SOUND.** φ-self-similar nested 600-cell = deterministic icosahedral quasicrystal (aperiodic, no BZ). Coxeter no-E⁴-tessellation **independently confirmed** (Grok, ChatGPT/Copilot): regular Euclidean 4-honeycombs are only {4,3,3,4},{3,3,4,3},{3,4,3,3}; {3,3,5} tiles S³/hyperbolic. Orientation-doc tension is a **reconciliation** (finite-patch language ↔ global aperiodicity), not a correction. | CHANGELOG states the reconciliation framing explicitly; §6 already framed it that way. |
| **T4** does aperiodicity evade the no-go (**the substantive calibration**) | **SOUND-WITH-CALIBRATION.** Yes — no BZ ⇒ the periodic premise fails (causal-set/quasicrystal analogy sound). **But** evading the *periodic* no-go is **necessary, not sufficient** for W1: a deterministic quasicrystal has a **dense Fourier module (Bragg peaks)** + icosahedral local symmetry, so it could push anisotropy onto a dense small-but-nonzero set — a **highly-suppressed W2**, not exact W1. | §4 W1/W2 rewritten: evasion makes W1 *possible not granted*; W2 explicitly includes the "aperiodic-but-dense-suppressed" sub-case; Round-5 target sharpened to **exact vs dense-suppressed isotropy**. |
| **T5** world-call + numerics scope | **SOUND.** Determination right (W3 out; W1-or-W2 = quasicrystal-Lorentz). Finite-shell numerics correctly down-weighted (existence-proof that periodic-approx anisotropy is *reduced not eliminated*; don't probe aperiodic limit). Early committed call defensible-but-hedged. | Numerics framed as reduce-not-eliminate existence-proof; early-call left to TLA (banner). |

## 3. Cross-response synthesis

Unanimous and strong. The **Part-A periodic no-go** is the cycle's headline — all three call it theorem-grade
(a bounded BZ-periodic symbol cannot be exactly Lorentz, for any periodic lattice including infinite-range),
with Grok reproducing the numerics and the harmonic tower, and the Coxeter no-E⁴-tessellation fact
independently confirmed. **Part-B** (CPP is aperiodic/quasicrystalline by construction, so the no-go is
moot) is endorsed as correct and load-bearing, with the orientation-doc tension fairly handled as a
reconciliation.

The one substantive calibration is **T4**, raised most sharply by the Gemini-style response and echoed by
ChatGPT/Copilot: **evading the periodic no-go is necessary but not sufficient for W1.** A deterministic
quasicrystal still has a dense Fourier module (Bragg peaks) and icosahedral local symmetry, so it could be a
*highly-suppressed W2* rather than *exact W1*. v1.1 adopts this: the evasion makes W1 **possible, not
granted**, and the Round-5 decider is sharpened to **exact vs dense-suppressed isotropy** of the
cut-and-project approximant. The world-call language picks up the standing "given A3/A3′ and C3, pending
OPEN-SR-9" qualifier on "W3 excluded."

The world-call survives intact: **W3 excluded (given A3/A3′, C3); the answer is W1 or W2; the W1-vs-W2 line
is quasicrystal exact-vs-dense-suppressed isotropy.**

## 4. Cycle-close decision

- **No verdict-flipping objection** on any top-triage question (none of the §4 flip criteria triggered). The
  finding **stands**.
- **v1.1 calibration applied** to `2068_round4_periodic_nogo_quasicrystal.md` (Patch 2070): banner →
  PANEL-REVIEWED + CHANGELOG; T1/T5 W3-conditional qualifier; T4 dense-Fourier-module / possible-not-granted
  rewrite of §4; Round-5 target sharpened to exact-vs-dense-suppressed; reconciliation framing.
- **No status/registry move.** OPEN-SR-10 / R2-STATUS world-call sharpening deferred to a separate
  STOP-and-warn patch on TLA's nod. NO THEO.
- **Forward:** Round 5 = structure-factor isotropy of an explicit icosahedral-quasicrystal approximant
  (cut-and-project E₈/H₄ or φ-inflation), testing **exact (W1) vs dense-suppressed (W2)** isotropy — the
  actual decider. The OPEN-SR-10 entry, post-this-close, is ready to be updated to "W3 excluded; W1-or-W2 =
  quasicrystal exact-vs-dense isotropy" whenever TLA authorizes the registry edit.

*Aggregated by Claude Opus under Thomas Lee Abshier's direction (Patch 2070). Verbatim reviewer responses
relayed by TLA; synthesized under the §0 identity caveat. Corrections appended forward.*
