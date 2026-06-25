# HANDOVER — SF-2/SF-5: the edge-bond SSV potential is the DM-1 make-or-break (three numbered goalposts)
**Date:** 2026-06-25 · **Lane:** strong/EW substrate (SF-2 + SF-5) · **From:** Opus (DM 08xx session) · **Consumer:** DM-1

---

## ⛔ LINE 1 — BLOCKING CLONE GATE (do this before anything else)
```
cd ~/Documents/GitHub/CPP && git pull --rebase origin main && git log --oneline -8
```
Do NOT register an ID, place a file, or compute a coefficient before cloning and grepping the registry. Confirm origin/main HEAD includes the DM arc below (0860–0864 + OPEN-SS-39). **This is a cross-window handover: the work it asks for is SF-2/SF-5 lane, NOT DM lane.** Pick your own next free SF patch number in your band; grep the THEO/OPEN registry before reserving any ID. OPEN-SS-39 is already registered (do not re-register; it is the G3 home).

---

## WHERE THINGS STAND (one paragraph)
The DM-1 point-scattering magnitude died this session (σ/m ≈ 0.20 was a solver artifact, 0859; corrected ≈ 0.11, ~5–20× too small). The programme pivoted to **extended charge-offset aggregates** (2eDP:2qDP ribbons, hTetra-chain loops, 4-wide crosses) whose geometric cross-section scales **σ/m ∝ N**. Across patches 0860–0864 that pivot collapsed from a vague "derive the loop-size distribution" into **one well-posed substrate object**: the **edge-bond SSV potential** between adjacent rungs of the chain. Everything downstream (length distribution, loop size, cross-section magnitude, lifetime, fragmentation trend, glueball dilution) is determined by that one potential's depth, angular stiffness, and the cross-sections/arrest-size it implies. **DM-1 is paused at v0.1-R (honestly re-scoped, 0864). The next move is this strong/EW-sector calculation — it decides whether the entire DM candidate lives.**

---

## WHAT THE DM LANE COMMITTED THIS SESSION (context, all in `series_phenomena/cosmology/dark_matter/` except the frontier reg)
| patch | what | read for |
|---|---|---|
| 0860 | σ(N) cross-section pass + (N,E_bond) over-determination ledger | the N-target + how E_bond is constrained 3 ways |
| 0861 | PCD formation kinetics — loop-size knob collapses onto persistence length ℓ_p | why ℓ_p is the single size-setter |
| 0862 | candidate comparison — stiffness/collapse ladders, geometry-selection rule, dilution tax | why one bond strength selects the geometry |
| 0863 | chaperoning suppresses glueball dilution; hinge "medium" → κ_θ target | the G1 κ_θ target + dilution defang |
| OPEN-SS-39 | frontier(SS): glueball formation/growth/decay kinetics + cocoon-arrest radius | the G3 home (cross-links OPEN-SS-6) |
| 0864 | DM-1 re-scope to v0.1-R (retract 0.20, fold in 0860–0863) | the paper's honest current state |

Each physics patch has a verbatim `reasoning/<n>.md` + a runnable `code/<n>_*.py`. **Fastest orientation:** run `code/0863_*.py` and `code/0861_*.py`, read `reasoning/0863.md`. Commit identity `Thomas Lee Abshier (Opus) <opus@hyperphysics.local>`.

---

## THE ASK (one object, three numbered goalposts)
**Derive the SSV potential of the edge-bond between adjacent rungs of the 2eDP:2qDP / hTetra chain** — the qCP–qCP and eCP–eCP edge bonds where the tetrahedra/rungs join — as a function of separation and bend angle, at the sub-Planck pre-tension separations the substrate fixes. From that one potential, three quantities fall out, each with a DM target it must clear:

**G1 — angular stiffness κ_θ (well curvature in the bend coordinate) → persistence length ℓ_p.**
- Target: **ℓ_p ~ 100–700 fm**, i.e. **κ_θ ~ 100–700 × kT_form** (θ_rms ≈ 3–8° per hinge; relation ℓ_p/ℓ_rung = κ_θ/kT).
- ⚠️ **This is a NEAR-CANCELLATION and is the hard part.** Per Thomas: the free vertices on a q:q edge present like-charge e:e *repulsion* when the chain bends, partially *screened* by the two opposite charges of the bonded pair sitting slightly farther away — all pre-tensioned at sub-Planck separation. κ_θ is the residual of (closer like-charge repulsion) − (farther opposite-charge screening). Its sign is clearly restoring; its **magnitude cannot be eyeballed** and is what this calc must actually evaluate. Two configuration types **bracket** it: 2-repulsive-1-attractive (stiffer) vs 2-attractive-1-repulsive (softer, repulsive pole farther). There is a **~90° anharmonic ceiling** (non-hinge vertices superimpose) — the well is harmonic only for modest bends.
- Feeds: loop size via ring-closure (population peak at contour L* ≈ 3.4 ℓ_p, 0861) AND the σ/m ∝ N stiffness requirement (0860/0862).

**G2 — well DEPTH E_bond (two of them: E_qq > E_ee).**
- Target: **E_bond ~ 0.8 keV – 2 MeV** (0860 fragmentation window).
- The **e–e edge is the weaker/scission bond** (Thomas: breaks in ZBW State 2), so **E_ee** is the one that governs breakage/length kinetics; E_qq is the stiffer partner. Report both.
- Feeds: equilibrium-polymer length ⟨N⟩ ~ exp(E_ee/2kT_form); 14-Gyr lifetime floor E_ee ≳ ~100 kT_present; fragmentation onset (collision KE vs E_ee).

**G3 — glueball-arrest radius + accretion/apposition cross-sections (OPEN-SS-39).**
- The compact endpoint is an OPEN-SS-6-type closed-hDP-loop glueball. Need its **cocoon-arrest radius** (eDP cocooning + local-resource depletion): **~100s of fm ⇒ a second size-setter that must agree with ℓ_p; ~few fm ⇒ pure dilutant (σ/m ~ 0.11).**
- Need **σ_accrete / σ_appose** → the suppression ratio ρ ≈ [hTetra]/[ribbon]·(σ_accrete/σ_appose). DM needs **ρ ≳ 9** to hold the glueball mass-fraction below 10% (else the dilution tax bites; 0862/0863).

**Also (smaller): the second-moment-of-area ladder** for hTetra vs 4-wide ribbon vs 4-wide cross — replaces the illustrative g_geom = {1, 10, 40} (0862) and pins which geometry sits in-window for a given E_ee/κ_θ. And **pin the per-rung 2eDP:2qDP mass** (currently defaulted to 264 MeV; moves the N-target linearly — SF-3/SF-2).

---

## SECTOR TOUCHPOINTS (route as you see fit; inputs already in hand)
- **eCP/qCP electrostatic SSV at sub-Planck pre-tension** (G1 κ_θ near-cancellation; G2 E_qq/E_ee depths) → **SF-2** territory (the W 3eDP:3qDP bracelet is the same constituent kit in charged form; the DM ribbon is its neutral, doubled-width, looped cousin). The SSV force law the well is computed from is **SR-1** (in hand).
- **hDP/gluon residual interaction + glueball-arrest** (G3) → **SF-5** (hDP = gluon, confinement, glueball mass OPEN-SS-6).
- **264 MeV constituent + qDP structure** → **SF-3** (in hand; cited by DM-1).

---

## LANE BOUNDARY (what is SF vs what stays DM — do not cross)
- **SF delivers:** the edge-bond SSV potential and its derived numbers — E_qq, E_ee, κ_θ (→ℓ_p), the second-moment ladder, σ_accrete/σ_appose, the glueball-arrest radius. Register results in your SF band + the relevant THEO/OPEN IDs (OPEN-SS-39 for G3).
- **DM consumes (do NOT do this in the SF window):** plugging those numbers back into the σ(N) cross-section, the mixture/dilution average, the DM-1 figures, and the v0.2 promotion. That is DM 08xx lane work, gated on your outputs. Hand the numbers back; the DM lane closes the loop.
- Collision-safe vs the DM 08xx, 0900 chirality, 1300 SF-7, 2100 capture-audit windows. This handover file is a new file in `handovers/` (no collision).

---

## WHAT A WIN LOOKS LIKE / WHAT A KILL LOOKS LIKE
- **Win:** the potential gives κ_θ landing ℓ_p in [100,700] fm for the cross and/or hTetra-loop, E_ee in [0.8 keV, 2 MeV], and a glueball-arrest radius that is either ≳100s fm (second size-setter agreeing with ℓ_p) or harmless given ρ ≳ 9. Then DM-1 promotes off Layer-C toward a near-prediction.
- **Clean kill (also valuable):** if the near-cancellation gives κ_θ ≪ 100 kT_form (all geometries floppy → σ/m collapses to the floppy constant) OR ≫ 700 kT_form for every geometry (loops too big/rare), the extended-aggregate channel fails on magnitude and we stop cleanly. The goalposts are sharp enough that the result is decisive either way.

---

## CONVENTIONS / REMINDERS
- PCD = **Perceive, Compute, Displace**. Filenames carry **no version suffix** (history in CHANGELOG). Cite only **verified** bib keys; write verdicts from computed numbers, not before.
- Every physics patch bundles a verbatim `reasoning/<n>.md` (+ verify script if it computes). CLONE-FIRST GATE: grep the registry before any ID/coefficient.
- Relation used throughout: ℓ_p/ℓ_rung = κ_θ/kT; θ_rms(total) = √(2 ℓ_rung/ℓ_p); ring-closure peak L* ≈ 3.4 ℓ_p; ℓ_rung ~ 1 fm.
- Two temperatures in play: **kT_form** (sets the length distribution at freeze-out) vs **kT_present** (sets the lifetime floor); the DM ledger needs kT_form/kT_present ≳ 7 and ambient kT_amb ≲ ~19 keV — both substrate-thermal-history inputs you may be able to pin.
- σ_geo is an UPPER bound on transport σ → every N-target is a LOWER bound; a transport efficiency ε<1 raises N by 1/ε.

**First action for the SF window:** run the clone gate, then `python3 series_phenomena/cosmology/dark_matter/code/0863_chaperone_suppression_and_hinge_target.py` and read `reasoning/0863.md` + `reasoning/0861.md` to see the three goalposts derived, then surface to Thomas whether the edge-bond SSV potential is tractable in SF-2/SF-5 as posed — and which of G1/G2/G3 to attack first (G1's κ_θ near-cancellation is the make-or-break; G2 is likely the easiest first win).
