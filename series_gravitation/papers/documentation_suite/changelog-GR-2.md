# Changelog — GR-2: The Echo Falsifier

**Paper:** `series_gravitation/papers/GR-2_echo_falsifier.tex`
**Convention:** canonical filename never carries a version suffix.

---

## V0 — 21 August 2026, Patch 3329 (Session 156)

Assembly draft, opened on the founder-ratified CONV-032 adjudication
(verbatim "Ratify the bundle. Please proceed with GR-2"). Complete
input set inherited at ratified strength: F-R1 (CONV-030), |R| = 1
(GR-1d V3, spin-independent), Schwarzschild closed form (3/2 + 8 ln 2)
GM/c³, derived Kerr exclusion surface + censorship theorem +
prograde-burial finding (Patch 3320; CONV-032 5/5,
derivation-conditional on A1–A3), binding error-bar rider. Claim
discipline: conditionality leads the abstract; no new derivations; no
new predictions (PRED-O-39 is the paper's single quantitative content;
swarm count unchanged). PD-001 suite in from the start (Keywords, PLS,
CP/GP Signature, Mechanism Bridge, Swarm-Validation, Verification).

**Verify:** `code/3329_gr2_template_verify.py`, 9/9 PASS; FAST subset
4/4 (first enactment of the CONV-032 FAST-mode dispatch adoption).
**Finding surfaced by the script's own first run:** the template
SATURATES in spin above burial onset — dΔt/dχ = 0.299 GM/c³ at
χ = 0.68, so the mandated ±0.1 spin bar is ±0.35% (mass ±6.5%
dominates ~20×); the worker's prior 3–10% expectation was wrong and
is recorded in the script header per computation-before-claims. The
strong spin lever lives below onset (2.151 → 2.607 ms across
χ = 0 → 0.55); for the remnant population the template is effectively
mass-only.

Compile gate: pdflatex ×2, 0 errors, 0 undefined refs, 7 pages.
Standing: V0 / inputs reviewed, assembly NOT yet panel-reviewed —
a CONV round is the natural next gate before any V1.0/ship move.

## V1.0 — 21 August 2026, Patch 3332 (Session 156) — SHIPPED

Review basis: CONV-033, 5/5 same-session, Q7b V1.0-PREP-CLEAR 4–1
(`review/conv033_adjudication.md` v1.0). The adjudication's six
adopted revisions folded at the bump (GR-1i/CONV-029 fold precedent;
the minority's restate list IS the fold list): (1) amplitude grade
split — |R| = 1 exact/parameter-free vs ~5% transmission as an
argument-level GR-1d estimate, in abstract, §4 (retitled "exact
reflectivity, estimate-grade transmission"), and PLS; strike
condition retained at estimate grade; (2) "effectively mass-only at
equatorial eikonal grade" at every occurrence incl. conclusion;
(3) search-coverage claim cited (Abedi+2017; Westerweck+2018;
Tsang+2020 — supplied in-round by the falsifier seat) and bounded to
"surveyed here"; (4) null falsifier operationalized: preregistered
injection-recovery-efficiency criterion at the predicted delay and
amplitude; (5) discriminator scoped: CPP surface ordering vs
horizon-keyed templates, not uniqueness over all ECOs; (6) dedicated
abstract sentence naming the eikonal systematic the dominant formal
uncertainty. No numbers changed; verify script unchanged, 9/9 PASS
(FAST 4/4). Compile gate: pdflatex ×2, 0 errors, 0 undefined refs,
7 pages. Deposit posture: queue row stays fail-closed (founder
APPROVED column + Isak's DOIs remain the gate).
