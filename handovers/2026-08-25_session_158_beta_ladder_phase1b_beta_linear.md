Bootup for Conscious Point Physics (CPP). Clone the repo and read the bootup file at https://raw.githubusercontent.com/Hyperphysics-Institute/CPP/main/bootup.md. Honor the line-1 CLONE-FIRST GATE before registering any ID, placing any file, or computing any coefficient (clone the repo and grep the registry first). Then open the handovers/ folder, sort by filename, and read the most recent dated file (named YYYY-MM-DD_session_NNN_*.md) — that newest entry is the canonical "what's next" pointer. Note: the folder is handovers/ (plural) and there is no file named handover.md; never look for either — always use the newest dated entry.

---

# Session 158 — β-ladder Phase 1B closed: BETA-LINEAR, and the comparator is still void

**Date:** 25 August 2026 · **Lane:** DM (cosmology) · **Machine:** Kila6
**Patches this session:** 3173, 3174, 3175, 3180, 3199, 3424
**Session-number note:** the previous dated handover is
`2026-08-23_session_157_dmde_cheap_routes_exhausted.md`, so this is 158.
(Handovers `session_160/161/162` are June-dated legacy files; the
sequence is not monotone with date. Sort by DATE, not by session number.)

---

## Orientation — read this first

The β-ladder is finished and its scaling question is answered:
**BETA-LINEAR**, BETA-FLAT excluded at 99%, on a duplicate gate that
passed on legs computed *after* an unexplained host crash. **But do not
mistake this for a physics result.** Patch 3176 voided `SUST_REF` as a
comparator (a Sea-pair *polarization amplitude* had been transplanted
into a *force* band with an implied conversion factor of 1, against a
computed factor ≤ 0.008 or exactly 0 by profile), the 3175
COEFFICIENT-OVERPREDICTED finding is **RETRACTED**, and nothing in the DM
lane can be read as magnitude until a valid comparator exists.
**The single most valuable next action is OPEN-BAND-CONV-1 (S1):
build the full-fidelity conversion under retardation and re-compare Route
B, Route C and all four β-ladder rungs against the corrected band. It is
container work — hours, no Kila6 time — and DISP-I3 cannot be
re-adjudicated without it.** Kila6 is FREE and should stay idle until S1
returns (3177 strategy §1; Phase 1B was the named exception and that
exception is now spent). Before any new multi-day campaign, spend five
minutes reading the **BMC System Event Log via DM_LAN1** — the machine
now demonstrably crashes at idle with no warning and no Windows record,
and a mid-campaign crash costs days.

---

## 1. Current state — what shipped

| Patch | What |
|---|---|
| **3173** | MemTest86 PASSED (4 passes, 0 errors) ⇒ prereg §5.4 acceptance SATISFIED, campaign not provisional. β-ladder driver shipped. Prereg under-specification disclosed via `--calibrate` (L = 240β over-determines the freezes). |
| **3174** | **R-INSIDE-SEA** — founder ruled the domain-exit rungs non-physical, selected the SPLIT design over the ~3-week enlarged-Sea build. Ladder rescoped to {0.05, 0.10, 0.15, 0.20}. Founder's **DP-Entity Sea picture + expansion addendum registered VERBATIM** (`founders_voice/founder_ruling_inside_sea_dp_entities_2026-08-18.md`). LIM-ISOLATED-DP registered. |
| **3175** | Phase 1 verdict: **BETA-UNRESOLVED** (β=0.05 CI spanned zero ⇒ ratio CI [−222, +188]). COEFFICIENT-OVERPREDICTED fired — **later retracted at 3176**. |
| **3180** | Phase 1B preregistered + driver. N 128 → 685 at β=0.05 only. Seed continuity verified and asserted at import. |
| **3199** | **Phase 1B verdict: BETA-LINEAR.** Gate PASS across a host crash. H-CORETEMP refuted; load-independence established; H-USB-RAIL registered. **The 3100 block is consumed.** |
| **3424** | Untracked a false gate certificate committed at 3180 (`duplicates_1b_verified.json` reading INCOMPLETE). |

**Interleaved by other windows this session:** 3176 (band provenance
audit), 3177 (Kila6 DM strategy), 3178 (3400–3499 reserved), 3179 (Phase
B driver), and the DM/DE arc 3420–3423 (varying-c mechanism, F-W-1
demoted). **Read 3176 and 3177 before proposing any DM route.**

## 2. The result, stated at the right strength

- Ratio `s(0.20)/s(0.05)` = 5.839, 99% CI **[3.137, 18.883]** — excludes
  1.0, contains 4.0. Through-origin `k_hat = 7.1007e-03` holds all four
  rungs. β=0.05 at N=685: CI [7.09e-05, 4.28e-04], now excluding zero.
- **"The response scales with β" is ESTABLISHED. "It scales
  PROPORTIONALLY" is consistent but NOT pinned** — the interval admits
  3.1–18.9. Do not upgrade this downstream.
- **It is an INSTRUMENT property, not a physics verdict** (comparator
  void). Magnitude waits on S1.
- **It does not rescue Candidate (B).** BETA-FLAT would have given AK's
  null a benign β-scaling account; BETA-LINEAR removes that escape.
- **Ledger untouched:** DISP-I3 stands; six of seven; item 1B OPEN; 79.5%.

## 3. Worker error record (this session)

Kept because the programme's credibility rests on it being complete.

1. **COEFFICIENT-OVERPREDICTED (3175) — RETRACTED at 3176.** Asserted a
   3.5× overprediction against a comparator that was a category error.
   Written into the record before the provenance was checked.
2. **LIM-ISOLATED-DP over-credited (3175 §4).** Offered the isolated-DP
   idealization as a live reason the coefficient gap might be innocent.
   The 2918 number comes from the SAME engine, so the idealization is
   shared by both sides and cannot open the gap. Corrected in session.
3. **H-CORETEMP — REFUTED.** The crash recurred with Core Temp absent.
   The hypothesis explained the missing crash evidence too neatly and
   elegance was mistaken for support.
4. **Driver: `run_1b` printed CAMPAIGN COMPLETE unconditionally.** A
   post-crash relaunch announced success with zero legs run.
   Completeness had to be verified by hand. Fixed at 3199.
5. **Driver: `--analyze` crashed under `> file` on Windows cp1252** (the
   Greek β). Cost the founder a rerun. Fixed at 3175.
6. **Committed a false gate certificate at 3180** (`git add -A` swept in
   a container test artifact reading INCOMPLETE). Fixed at 3424.

**Pre-declaration ledger for the β-ladder: one blind prediction made,
one blind prediction FALSIFIED (Phase 1: FLAT/SUBLINEAR), one informed
update confirmed (Phase 1B: LINEAR, declared after seeing Phase 1's
fit — weak evidence, booked as such).**

## 4. Immediate next priority

**S1 = OPEN-BAND-CONV-1.** Full-fidelity polarization→force conversion
under retardation; then re-compare Route B, Route C and all four
β-ladder rungs against the corrected comparator. Container work, no
machine time. Everything downstream in the DM lane is blocked on it:
DISP-I3's re-adjudication, the coefficient question, and whether five
campaigns actually failed or merely had the wrong yardstick.

**Then, in order:** BMC log read (free, five minutes, before any
campaign); S2 = D-JITTER-1 Phase B on VideoCPU (driver gate-tested at
3179); S3 = the entity-aware instrument (gated on S2), which is what the
founder's DP-Entity picture actually requires.

**Kila6: FREE and deliberately idle.** Do not launch a campaign before
S1 returns.

## 5. Founder physics registered this session — do NOT formalize

The DP-Entity Sea picture and the expansion/equilibrium addendum are
captured verbatim in `founders_voice/`. **Its kinetics IS the blinded
D-EQUIL-KINETICS derivation reserved for the founder (OBL-KIN-BLIND).**
Capture deliberately stopped at registration; formalizing it in-corpus
would contaminate the blinding. Phase A's measured decomposition (bound
Sea ≈ 2% of the fluctuation; the unbound fraction carries the rest) is
consonant with the picture and was obtained blind — note the consonance,
do not build on it. Standing correction on record: the DE-lane number is
**w_now = −1.023** (equation-of-state), not a "1.02 acceleration rate."

## 6. Hardware — Kila6 (unresolved, and it will bite)

- **Load-independent.** Last leg written 10:11:24; crash at 11:41:28 —
  the machine died **at idle, 90 minutes after ~75 h at 100% on 32
  threads.** Thermal / current-draw / VRM-sag families eliminated.
- **Zero Event 1001 across all eight events** — bare 41/6008 pairs.
  Power cut, not OS fault.
- **17 Aug BIOS reset cut the rate ~100× (hours → weekly) without
  curing it.**
- **H-USB-RAIL:** a dongle failing across BOTH front and rear USB
  implicates the shared +5V/+5VSB rails. One upstream power fault
  explaining both symptoms beats two coincident faults ⇒ **PSU/rail
  health now outranks the PWR_SW header.**
- **Owed, never performed: the BMC System Event Log via DM_LAN1.**
  Own power rail; logs rail faults the host cannot. Outstanding since
  3173. Free PWR_SW test also unrun (unplug header, start by bridging
  pins).

Full detail: `series_phenomena/cosmology/dark_matter/kila6_hardware_log.md`.

## 7. Bootup instructions for the next window

**Read first:** `series_phenomena/cosmology/dark_matter/band_provenance_audit_3176.md`,
then `kila6_dm_strategy_3177.md`, then
`beta_ladder_phase1b_verdict_record.md`. **Do not propose a DM route
before reading the first two** — the 3157-session lesson repeated twice
this week is that refutations were already sitting in the repo.

**Avoid:** re-siting the β-ladder's frozen ratio endpoints (existing data
would resolve s(0.20)/s(0.10) — which is exactly why it is forbidden);
reviving the retracted coefficient claim with more data; reading
BETA-LINEAR as a physics verdict or as proportionality; launching Kila6
before S1.

**Numbering:** the 3100 block is CONSUMED. Cosmology continues in
**3400–3499**; the DM/DE lane pointer also names 3424, so **grep the
registry before claiming an ID** — a collision has bitten this programme
twice (3168/3169; and 3424 was claimed by two lanes this session).

## 8. Trajectory expectation

S1 is one session of container work and unblocks the lane. S2 is a
VideoCPU campaign already chartered and gate-tested. S3 is a build, not
a run, and is where the founder's picture enters the instrument. Realistic
closure on the DM disposition: **two to three sessions after S1 returns**,
and not before — the dispatch to the panel should carry a valid
comparator, on the founder's own instruction to try everything we know
before submitting.

---

## 9. Step A–H Completion Audit (§15.11)

| Step | Status |
|---|---|
| **A** — Tier 1 session log | **N/A** — no `session_logs/2026-08-25_*` exists; this session's record is carried by six patch commit messages, three verdict/prereg records and four reasoning fragments, all committed. Flagged for the next window as a deliberate gap, not a silent one. |
| **B** — Tier 2 transcript pointer-map | **N/A** — no transcript filed this session. |
| **C** — Tier 3 development vignettes | **N/A** — no paper-scoped `.tex` work; the session was campaign execution, verdict records and instrument repair. |
| **D** — Tier 4 verbatim reasoning | **✓** — `reasoning/3175.md`, `3180.md`, `3199.md`, `3424.md` (DM lane); `founders_voice/founder_ruling_inside_sea_dp_entities_2026-08-18.md` for founder verbatim (CONV-009). |
| **E** — Registry updates | `research_frontier.md` **✓** (headers at 3173/3174/3175/3180/3199). `frontier_sectors/DMDE.md` **✓** — the audit found this session's DM-lane entries missing (the file's last entries were 3421–3423 from the parallel window) and the gap was discharged in this same patch rather than deferred, per §15.14(a). `predictions.md`, `paper_catalog.md`, `theorem-registry`, `axiom-registry`, `master_glossary.md`, `methods_catalogue` — **N/A** (no new physics claim survived; the one candidate was retracted). `organizational_frontier.md` — **N/A**. |
| **F** — Reviewer response artifacts | **N/A** — nothing dispatched; dispatch deliberately deferred pending S1 on the founder's instruction. |
| **G** — Protocol / OS updates | **N/A** — no OS change. (Candidate for a future window: the `git add -A` habit that committed a container test artifact at 3180 is a repeat-risk worth a one-line OS discipline.) |
| **H** — This document | **✓** — `handovers/2026-08-25_session_158_beta_ladder_phase1b_beta_linear.md`, opening with the kickoff line. |
