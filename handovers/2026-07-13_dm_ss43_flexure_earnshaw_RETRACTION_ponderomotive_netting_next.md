# Handover — 2026-07-13 — OPEN-DM-FLOQUET-1 / flexure-Earnshaw RETRACTION; next = flexure-ponderomotive netting

**Warm keyword: DM-WARM-2448**
**HEAD after this session: Patch 2449 (this handover). Substantive HEAD: Patch 2448.**
**Candidate (B): UNRESOLVED-leaning-MARGINAL (~35%). Registry NOT promoted. Ω_DM parked.**

---

## KICKOFF LINE (paste to open next window)
> Bootup for CPP. Clone the repo and read `bootup.md`. Honor the line-1 CLONE-FIRST GATE
> (clone + grep the registry) before registering any ID, placing any file, or computing any
> coefficient. Then open `handovers/`, sort by filename, read the newest dated
> `YYYY-MM-DD_session_NNN_*.md` — that is the canonical "what's next." Warm keyword
> DM-WARM-2448. Default action: the flexure-ponderomotive netting (R5-analog for the
> collective BEND mode) — does the ZBW ponderomotive net the −3263 MeV·fm² static bend
> instability into a STABLE minimum at N_planes=16, and in what ε-window? Honest state:
> candidate (B) UNRESOLVED-leaning-MARGINAL; the 2443-2446 flexure-robust/in-window case was
> RETRACTED at 2448 (axial-bond artifact); registry unpromoted; Ω_DM parked.

## ORIENTATION — read first (next session)
1. `frontier_sectors/SS.md` — the OPEN-SS-43 / FLOQUET block, newest lines first: read the
   **⚠ CORRECTION (2448)** line BEFORE the 2443-2447 lines, or you'll re-adopt a retracted premise.
2. `series_phenomena/cosmology/dark_matter/reasoning/2448.md` — the retraction, verbatim.
3. Then 2445 (transverse R5) and 2440/2441 (method a / R1 scoping) for the ponderomotive machinery.

## THE ONE THING THAT HAPPENED THIS SESSION
Founder directed examining the load-bearing joint ("does flexure escape Earnshaw?") BEFORE
taking anything to the CONV-001 panel. It OVERTURNED the session's favorable arc:
- The full-lattice collective **bend stiffness is NEGATIVE** (d²E/dκ² = −3263 MeV·fm²;
  collapse resisted +2.43 → genuine bend instability). **Flexure does NOT escape Earnshaw.**
- 2443/2446 computed κ_θ from **axial inter-plane bonds only** → missed the intra/cross-plane
  pairs that net-destabilize → the "geometric ratio 2(r_q/d)²≈0.66 in-window" was an
  **axial-bond ARTIFACT**. RETRACTED. The "flexure robust / transverse marginal / modes
  DISAGREE" story (2445) is CORRECTED: **both modes are Earnshaw-negative**, both need the
  ZBW/ponderomotive rescue. Same failure class as 2427 (axial average), which 2430 caught —
  caught this time before the panel.
- Verdict marked DOWN: prior "~55% favorable" WITHDRAWN → **~35%, UNRESOLVED-leaning-MARGINAL**.

## WHAT SURVIVES (do not re-derive)
- **Core ≫ coat ponderomotive rescue:** K_pond(core)/K_pond(coat) ~ (α_s/α)² = 2800; core ZBW
  migration exp(−53×) suppressed. Founder's core-integrity point HOLDS — now for BOTH modes.
  This is the lever the netting hinges on.
- **2447 collision kinematics** (mode-independent): rings form primordially (β~0.08, kT~20 MeV);
  present galactic DM collisionally INERT (~keV ≪ elastic) → CDM-consistent stability today.
- **2444 deep E_qq** (≥9–170 MeV) is a true depth fact; but the E_bond-denominator question is
  MOOT while the numerator κ_θ is negative/unrescued.
- **Favorable flip (not spun):** negative static bend ⇒ straight rods spontaneously CURL ⇒
  FORMATION is easy (2447 threshold may be an overestimate). Burden shifts entirely to STABILITY.

## NEXT ACTION (decisive, in order)
1. **FLEXURE-PONDEROMOTIVE NETTING** (R5-analog for the collective bend mode). Method: as 2445
   (ponderomotive Hessian at the |E|² minimum, positive semi-definite there), but for the BEND
   coordinate on the whole rod, netted against the −3263 static bend term. Question: does the
   core's α_s² ponderomotive net the bend to a STABLE minimum at N_planes=16, and for what ε?
   Pre-registered kill: if no stable minimum exists at N=16 for any plausible ε → FALSIFICATION
   (candidate B falsified). If stable only in a narrow ε-window → conditional (method-a state,
   the favorable case returns but unestablished pending drive-pinning).
2. **Pin the ZBW drive (a, ω)** — 1811 action #2, never executed — to know if the drive lands
   in that window. This has been owed for many sessions and now gates everything.
3. **DO NOT draft the CONV-001 packet yet** — it would rest on the retracted flexure premise.
   Draft only AFTER the netting (step 1) resolves the bend-mode sign.

## GUARDRAILS (unchanged, binding)
G1 both-phase; G3 equilibrium; G4 netting (report K_switch/K_pond/K_structural separately +
sum); G5 δ upper-bound; G6 branch derived; G7 pre-registered sign — report where it lands,
no re-parametrizing a miss. Anti-motivated-reasoning: this session is the proof the discipline
works — an Opus-favorable arc self-corrected under founder-directed scrutiny. Keep that posture.

## PER-PATCH CAPTURE AUDIT (this session)
2443 ✓ (code+reasoning+SS.md) · 2444 ✓ · 2445 ✓ · 2446 ✓ · 2447 ✓ · 2448 ✓ (retraction, all three) ·
2449 = this handover. All under Opus authorship.

## GIT STATE NOTE (IMPORTANT for next boot)
The founder hit a `git am` failure applying 2448 (context error at SS.md:1319) because 2445–2447
were not yet applied on the ClearPC tree when 2448 was attempted. Resolution path given: `git am
--abort`, then apply 2445→2446→2447→2448→2449 in order (`--3way` on any single context error).
**Next session: verify `git log --oneline` shows 2443–2449 on the remote before proceeding; if
not, the patch files in `/mnt/user-data/outputs/patches/` (or `~/Downloads/`) are the canonical
record and must be applied in order first.**

## SORT NOTE
This file (2026-07-13…) sorts AFTER all 2026-07-12 entries → it is the newest, the canonical
pointer. No same-date tiebreaker needed this time.
