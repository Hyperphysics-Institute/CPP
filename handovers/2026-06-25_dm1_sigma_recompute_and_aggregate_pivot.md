# HANDOVER — DM-1 dark-matter paper: σ/m recompute, review-in-hand, and the extended-aggregate pivot
**Date:** 2026-06-25 · **Lane:** DM 08xx (dark_matter/ subtree) · **From:** Opus (this session)

---

## ⛔ LINE 1 — BLOCKING CLONE GATE (do this before anything else)
```
cd ~/Documents/GitHub/CPP && git pull --rebase origin main && git log --oneline -6
```
Do NOT register an ID, place a file, or compute a coefficient before cloning and grepping the registry.
Confirm origin/main HEAD. The patches below (0848–0859) were built and delivered this session; verify which actually landed (a couple needed `git am --3way` after a missing-patch chain). **Next free DM number: 0860** (confirm with `git log --oneline | grep -oE ' 08[0-9][0-9] '`).
Lane discipline: this lane owns `series_phenomena/cosmology/dark_matter/` only. Collision-safe vs 0900 chirality / 1000 Project-C / 1100 CC-umbrella / 2100 capture-audit windows. Shared-template edits (e.g. the review protocol) are OUT of lane → separate patch in the workflow/templates band.

---

## WHERE THINGS STAND (one paragraph)
DM-1 ("substrate dark matter = charge-neutral qDP/hTetra aggregates; velocity-independent SIDM, σ/m") was assembled (0700–0855), promoted to a publication `.tex` at **v0.1 (DRAFT)** (0856/0857), sent to the panel (0858), and **reviewed** (4 responses in hand). The panel converged on a wording calibration hit but no scientific kill. **Then the floor moved:** Thomas refused to paper over the magnitude tension, I did the proper partial-wave recompute (Patch 0859, validated solver), and it shows the shipped **σ/m ≈ 0.20 is an artifact** — the physical potential gives **≈ 0.11, flat, ~5–20× below what dwarf cores need, with no closure in the f-band**. Velocity-independence survives; the magnitude/coring discriminant does not. Thomas then proposed a **physics pivot** (extended ribbon/loop aggregates) that I assessed as genuinely promising. **The paper is paused at v0.1; the next move is physics, not paper edits.**

---

## WHAT IS COMMITTED THIS SESSION (DM lane)
| patch | what | status |
|---|---|---|
| 0848 | §1 substrate primer + 3 flagship cites | landed (was the missing-patch culprit; applied late) |
| 0849 | §4 residual V(r) + saturation figure | landed |
| 0850 | §6 specific-dwarf density confrontation (Fornax + IC 2574) | landed |
| 0851 | §6 core-radius-vs-σ/m panel (NFW r₁ inversion) | landed |
| 0852 | number-honesty pass (f-band reconcile + IC 2574 → abstract/§7) | landed |
| 0853 | §8 calibrated-inputs cleanup + final grade | landed |
| 0854 | references-threading (SF-5/SF-3/QM-1/SR-1; Project C by name) | landed |
| 0855 | §9 + R2: c08 DISCHARGED (Patch 1161) → gate down to one condition | landed |
| 0856 | .tex promotion → `DM-1/DM-1_substrate_dark_matter_candidate.tex` | landed |
| 0857 | version correction v1.0 → **v0.1 (DRAFT)** (house format, SF-7) | landed |
| 0858 | review package `DM-1/review/DM-1_review_package_v0.1.md` (cycle-opening) | built/delivered — **confirm on origin** |
| 0859 | **THIS handover patch**: validated σ/m recompute (the finding) + this handover | building now |

Apply contract (every patch): `cd ~/Documents/GitHub/CPP && git pull --rebase origin main && git am ~/Downloads/<file>.patch && git push origin main && git log --oneline -3`; recovery `git am --abort; git am --3way ...`. Commit identity `Thomas Lee Abshier (Opus) <opus@hyperphysics.local>`.

---

## THE LOAD-BEARING FINDING (Patch 0859 — read `reasoning/0859.md` + run `code/0859_phase_shift_sigma_scan.py`)
- Solver **validated to machine precision** vs the analytic square-well scattering length, incl. across the first bound-state resonance. Trust it.
- **screened-LJ (Fig.1, the physical potential, real eDP-coat hard core): σ_V/m ≈ 0.11 cm²/g, FLAT** across f∈[0.07,1.0] and v∈[30,3000]. The hard core caps the scattering length at ~r_c regardless of well depth → no resonance, no climb to the data band.
- The shipped **"0.20" is reproduced exactly (0.197) by a Yukawa with an accidental wall at r=1.0** — which is literally what `code/0841` did (it started integration at r=rc=1.0 with u=0 on a coreless Yukawa). Artifact, not a derived value.
- Pure coreless Yukawa: 0.47 at f=0.2, resonant (~95) by f≈0.5 — wildly f-dependent, also not physical.
- **Data want σ/m ≈ 0.6 (density) to ~1–2 (core sizes).** Point-scattering on the physical potential cannot reach it. **The coring discriminant is closer to a NULL than to 0.20.** Velocity-INDEPENDENCE is real and robust.

## THE PIVOT (Thomas's proposal — the live physics direction)
DM is NOT compact eDP-cocooned spheres but **extended 2qDP:2eDP charge-offset ribbons/loops** (= the W-boson 3qDP:3eDP bracelet substrate, in neutral looped form) **+ 2eDP:1hTetra ribbons**, as a mixture.
- Cross-section becomes **geometric**, not scattering-length. For a 1D loop, **σ/m ∝ N (grows with size)** → reaches 0.6–2 at loops of **~10²–10³ DPs (R ~ 40–500 fm)**, **velocity-independent**. (Estimate in `code/0859`, §4.)
- **Bonus:** could also give the data-preferred velocity-DEPENDENCE (σ/m rising toward dwarfs) via **collisional fragmentation** of large loops at high cluster velocity — a mechanism the point-particle picture fundamentally lacked.
- **This REPLACES §5 entirely** (geometric/transport, not partial-wave). New linchpin: **derive the loop-size distribution from PCD formation/aggregation dynamics** — else the size is a relocated free knob.
- Caveats: geometric σ is an order-of-magnitude estimate (loops can pass through/link/deform → real transport cross-section needs DP-contact dynamics). Structural claims (2qDP:2eDP ribbon stability, glueball avoidance via a color-singlet qDP ladder, the 3-eDP-cocoon charge-asymmetry argument, the W/SF-2 substrate link) are **SF-2/SF-5 strong-sector questions** — plausible, unverified.

---

## OPEN DECISIONS / NEXT ACTIONS (surface to Thomas; do NOT race cross-window items)
1. **Geometric/transport cross-section of the loop population** — pin the precise size→σ/m mapping beyond the πR² estimate (the precise size target). *In DM lane.*
2. **PCD formation-dynamics calculation** — does aggregation produce loops of ~10²–10³ DPs? This is the **deciding calculation**; if yes, the gap closes as a prediction. *May reach into strong-sector / coordinate with SF-5.*
3. **DM-1 paper:** keep at **v0.1**; re-scope §5 as "under revision — extended-aggregate geometry"; do NOT advance to v1.0 on the coring discriminant until the recompute is resolved. The 0859 finding should be folded into §5/§7 honesty when the paper is next touched.
4. **Structural claims** → SF-2 (W substrate) / SF-5 (color-singlet ladder, glueball) confirmation.

## PENDING ITEMS BUILT-UP THIS SESSION BUT NOT YET DONE
- **Review aggregation `DM-1/review/reviews-DM-1.md` NOT yet written.** 4 reviews are in hand (relayed by Thomas). Convergent verdict: physics T1/T2/T4/T5 pass (3 ran the §7 script, SCRIPT-EXECUTED, reproduced all numbers); the one calibration hit all four flagged = **"supports velocity-independence" overclaims** (density test is a flat ~3× *miss*, not a success; core-size test wants σ/m rising). 3 said advance-with-editorial, 1 said restate-to-v0.2. **BUT this is now SUPERSEDED**: the 0859 recompute shows the problem is deeper than wording (the σ/m number itself is wrong). When aggregating, record that the calibration verdict is overtaken by the recompute. **Identity caveat:** two reviews self-labelled "ChatGPT"; attribute by content + paste-order, never self-label (Grok ran the script and recomputed; one "ChatGPT" was the deflation/restate pass, one the GPT-5.5 pass, Copilot structural-only no-run). One reviewer slip to note: Grok inverted the density→σ/m (wrote ~0.06; correct is ~0.6, since σ∝1/(σ/m)).
- **Review-protocol fix NOT yet built (OUT of DM lane → workflow/templates band).** Root cause Thomas identified: `templates/review_dispatch_protocol.md` §4 hard-codes "You are one of three reviewers (ChatGPT, Grok, Copilot)" — a closed list that FORCES a 4th member (Gemini) to mis-pick a name. Fix: replace with an open, non-enumerating form ("one of several … which may include …"), and strengthen the IDENTITY line ("state your own name even if not listed; do not pick the nearest"). Benefits every future cycle.

---

## CONVENTIONS / REMINDERS
- PCD = **Perceive, Compute, Displace** (not Polarize/Capture/Depolarize). Ideomotion (never Idiomotion).
- Cite only **verified** bib keys; never fabricate (Project C / DM-2 have NO keys → name only). Write verdicts from computed numbers, not before.
- Filenames carry **no version suffix** (canonical fixed; version history in CHANGELOG/changelog-DM-1.md).
- DM-1 .tex uses EMBEDDED `thebibliography` (EU-1 house style), figures via `\graphicspath{{../figures/}}`, compiles clean 2-pass.
- Every physics patch bundles a verbatim reasoning fragment (and a verify script if it computes). Reasoning at `series_phenomena/cosmology/dark_matter/reasoning/<patch>.md`.
- The σ/m convention in play: constituent mass (264 MeV) for the point-scattering; the loop pivot uses per-rung mass. Velocity convention for cores: ⟨v_rel⟩ = 2.26 σ₁D, σ₁D = V_max/√2 for rotation-supported.
- Key numbers to keep straight: Fornax (σ₁D=11, ρ_obs 0.016–0.07, core ≲0.3–0.7 kpc); IC 2574 (V_max≈80, core ~8 kpc, ρ≈0.006); f-band [0.07,0.6]; c08 discharged Patch 1161 (D1 PASS, D2 CLOSED, one condition left = event-horizon selection).

**First action for the next window:** run the clone gate, then `python3 series_phenomena/cosmology/dark_matter/code/0859_phase_shift_sigma_scan.py` to see the finding for yourself, read `reasoning/0859.md`, and surface the decisions above to Thomas before doing anything else.
