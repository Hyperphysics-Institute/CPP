# HANDOVER — 7 July 2026 (second session) — Grok propagation + F-1 (Patches 2324–2325)

**KEYWORD TO OPEN NEXT SESSION: "Stage-3 sub-cone"** (unless the founder opens with the 20-July
release decision, which needs no new computation — the input is at final form).

## Bootup for the next window

1. Clone fresh; **verify HEAD ≥ Patch 2325** — and verify the *predecessor chain*, not just HEAD:
   `git log --oneline -6` should show 2325 → 2324 → 2322 → 2323 → 2321 → 2320 (2322 was applied
   after 2323; see the incident note below). If any patch in the chain is absent, stop and report
   before any work — this session's first finding was exactly that failure mode.
2. Load: `handovers/` (this file), `series_phenomena/cosmology/dark_matter/gate1_b1_campaign.md`
   (full ledger), `gate1_b1_G4_grok_propagation.md` (2324 — the sharpest current statement of the
   gate), `gate1_b1_G4_s2_3b_polaron_reframe.md` (2322 — the operative frame).
3. Next patch number: **2326 is this handover; 2327 is next.** Grep the registry anyway
   (CLONE-FIRST GATE).

## What this session did (one screen)

- **2322 missing-patch incident (found at bootup, resolved by founder).** The 2322 patch had never
  landed on origin/main; 2323 (the handover) applied cleanly anyway because it only touched
  `handovers/`. Founder re-applied 2322 before any work proceeded. **Lesson registered: a handover
  patch cannot verify its own predecessor's presence — the next window's bootup must check the
  chain** (now step 1 above).
- **Patch 2324 — GROK PROPAGATION EXECUTED** (handover item 1; Grok W1 decisive check, 2322 frame).
  Capture-annulus law P(v,w) = 1−(Θ_crit/w)² derived from the C-g geometry; zero-parameter η=χ ⇒ P
  multiplies the published anchors, no refit. **Headline finding: the flat-spectrum PARTIAL branch
  is EXCLUDED by the existing LSB anchor** (turn-on ladder spans 5 decades; any flat w saving the
  dwarfs parks the LSB total on the floor ×15 under its window). **The gate is therefore nearly
  BINARY:** survive requires near-ceiling sub-cone weight at the LSB frequency — **w(4.2 keV) ≥
  0.66 AND E_coat ≥ 0.40 MeV** (hard-end coat infeasible) — or the whole velocity discriminant
  fails at once (kill → floor 0.046 everywhere; dSph/pin/LSB fail ×435/×22/×15; floor +
  cluster/Bullet safety survive every branch). Spectral ask graded: ×27–115 over bare Ohmic at
  dwarfs vs ×3×10⁴ at the LSB frequency (super-Ohmic s ≳ 2.6 or near-ceiling plateau by ~keV).
  F1 group falsifier branch-invariant. No verdict moved. Verify `code/2324` (7/7).
- **Patch 2325 — F-1 EXECUTED** (queued at 2313). `frontier_sectors/SR.md` D2 wording corrected
  subtraction→annihilation (Σv̂ = 0 exact; the zero is symmetry-enforced, not renormalized); F-1
  closed in the G1 audit; collision-surface notice carried in the commit; no status change.

## Current G4 state (the whole gate in two sentences)

**G4 = UNRESOLVED-QUANTIFIED on the sub-cone weight S(k ~ 1/R_s, ω_enc), thresholds per 2321/2322 —
and per 2324 the live outcomes are effectively two, not three:** near-ceiling weight at 4.2 keV
(full suite as published, upper coat band required) or a full velocity-discriminant kill (elastic
floor and cluster safety surviving either way). G1/G3/G2 remain discharged-conditional on C-a..C-d
+ EP-C-1; nothing in this session touched them.

## Next actions (in order)

1. **20-July founder decision** (on or after; pre-stated rule). Input is final: 2322 §Release
   posture + 2324's sharpening (the open condition is nearly binary; F1 is branch-invariant).
   Founder's call, no further computation owed.
2. **Stage-3/DM-4 — the sub-cone computation.** Multi-session; fresh window with full context.
   Per 2324 the spec is sharpened: **evaluate S(k ~ 1/R_s, ω) at ω = 4.2 keV (the LSB encounter
   frequency), not only the dwarf 45 eV — the bar there is ceiling-level (w ≥ 0.66)**. A cheap
   first move exists: if the computed spectrum cannot exceed the Ohmic tail by ≳10³ at keV, the
   gate resolves KILL-on-suite without the full machinery.
3. **Grok W2 (formation-N vs floor-N reconciliation)** — still queued from 2311 (1855-style
   kinetics with capture+floor active → N distribution → floor check). Independent of Stage-3;
   a candidate single-session item.
4. **Errata 5–6** — parked by design; fire at the next DM-2 wording pass, not standalone.

## Discipline notes for the next window

- Chain-verify at bootup (step 1) — new, from the 2322 incident.
- The 2324 propagation is decision *input*; do not let any summary of it shade "nearly binary"
  into a verdict. G4 is open until Stage-3 computes or the founder rules.
- SR.md was touched this session (wording-only); CC-lane (11xx) windows resync as normal.
- Founder contributions this session: session authorizations only; recorded in reasoning/2324.md
  §10. No founders_voice file warranted.
