# CRITICAL PATH TO DM-1/DM-2/DM-3 RELEASE — B7's TRIGGER, READ FROM SOURCE

**Patch 2859, 28 July 2026. Prompted by the founder's question "what
moves us down the road toward DM1,2,3 to OSF?" Answering it required
reading Founder Decision B7 itself rather than the handover's summary
of it — and the two do not say the same thing.**

---

## §1 — Disclosure: the worker mis-stated B7's trigger, twice, in this session

At the 2026-07-28 decision set the worker presented B7 to the founder as:

> ~~"(a) B7 REAFFIRMED — banners remain held on DM-1/DM-3 **pending PR7
> completion**."~~

**The founder ratified that framing. It is not what B7 says.** The
worker also carried "pending PR7" into the 2857 enactment record and
into the plain-language summary.

**This is the same failure mode registered at Patch 2856 four patches
ago** — carrying a summary of a founder decision without opening the
decision — and it is now its **second occurrence in a single session**,
by the same worker, after the mitigation was written. The 2856
mitigation required a citation for any motion *characterising* an
existing artifact. It was not applied to the worker's own framing of a
founder decision, because the worker scoped the mitigation to panel
motions. **The mitigation is hereby extended: it binds the worker's
own restatements of founder decisions, with equal force.**

## §2 — B7, verbatim (Patch 2684, 20 July 2026)

> **FOUNDER DECISION B7 (Patch 2684, 20 July 2026): option (i) — HOLD.**
> All three papers hold behind the **Candidate (B) revision path**. The
> revision checklist (2683 adjudications: stellar-capture row,
> cross-paper ledger, halo bracket, ±2 propagation, single pipeline;
> errata queue items 1–9) executes when the **Candidate (B) arc
> (FA-SG-R1 → OPEN-DM-RELIC-1 → promotion)** reaches paper-revision
> maturity. No standalone or record release.

And the release plan's own statement of the path back:

> the successor candidate arc (Candidate (B), N=8 ring — currently
> 79.5% PROVISIONAL-FAVORABLE with **FA-SG-R1, OPEN-DM-RELIC-1, and
> promotion outstanding**) reaching a **revised DM-1/DM-3**, a **fresh
> panel round**, and a **fresh stability cycle**.

**PR7 is not named in B7. Neither is 1B, K1-MEMORY, arc inertia, or
C23/C24.**

## §3 — Where PR1–PR7 actually live

PR1–PR7 are the **KINETIC-1 rider** promotion requirements
(`kinetic1_returns_adjudication.md`). Their own promotion rule:

> **Promotion rule.** Rider v2.5 → v3 only when PR1–PR7 are all
> satisfied under preregistered analyses.

That is a rule about the **screening-length rider** — the ℓ_phys =
d_DP/2 = 0.1820 fm claim and its methodological-floor cap. It is not,
on its face, a rule about Candidate (B)'s promotion from 79.5%.

## §4 — The unresolved question this exposes (**OPEN-B7-SCOPE-1**)

B7's chain ends in "**promotion**." Two readings:

- **Reading R-1:** "promotion" = Candidate (B)'s promotion from 79.5%
  PROVISIONAL-FAVORABLE. The KINETIC-1 rider is a separate track that
  feeds the screening-length claim, and **PR7/1B is not on the release
  critical path at all.**
- **Reading R-2:** "promotion" includes the rider reaching v3, so
  PR1–PR7 must all be MET, and **1B blocks release.**

**This is not resolved by any text the worker can find, and the worker
will not resolve it by preference** — the outcome determines whether
months of arc-inertia work is on the critical path or off it, which is
precisely the shape of decision the failure register says a motivated
worker gets wrong. **Registered as OPEN-B7-SCOPE-1, founder-facing.**

**Consequence pending resolution:** further effort on 1B, Route 2
revival, or the C23/C24 arc-inertia specification is **not justified as
release-critical** and should not be scheduled as such. Under R-1 it is
scientifically valuable and strategically irrelevant to OSF; under R-2
it is the whole game.

## §5 — The critical path under Reading R-1 (the one B7's text supports)

| # | item | status | blocked by |
|---|---|---|---|
| 1 | **OPEN-DM-RELIC-1** — relic abundance to verdict | ACTIVE; S3/S3b/f-yield pre-registrations frozen; Q-m2 gate executed (SM-A FAILS, SM-B takes the field); D3 calibrated incumbent as declared fallback | nothing structural |
| 2 | **FA-SG-R1** — panel-named decisive deliverable: *the missing derivation DP mechanics → χ_static → α* | ACTIVE; R1-SHIFT ratified 5–0, rider v2.6 enacted; L2 and L2R both FAILED as committed, class unaffected | **possibly OPEN-SEA-DENSITY-1** — see §6 |
| 3 | **Candidate (B) promotion** from 79.5% | outstanding | items 1 + 2 |
| 4 | **Revision checklist** (2683: stellar-capture row, cross-paper ledger, halo bracket, ±2 propagation, single pipeline; errata 1–9) | queued, specified | item 3 |
| 5 | **Fresh panel round** on revised DM-1/DM-3 | DM-1 v1.5 already carries *"NOT YET RE-SHIPPED: panel round pending per the R2 split release"* | item 4 |
| 6 | **Fresh stability cycle**, no load-bearing corrections | — | item 5 |
| 7 | **OSF deposit** | DM-1 §(vi): *"OSF release decision returned to the founder"* | item 6 |

## §6 — A dependency worth verifying, not asserting

FA-SG-R1's decisive deliverable terminates in **α**. The committed
continuum normalization is **α = κ_D²/(4π n_DP) = 0.08193374 fm** —
which is built from **κ_D and n_DP, the two α1-calibration quantities
that Patch 2858 just placed under OPEN-SEA-DENSITY-1 as unknown.**

If that dependency is real, OPEN-SEA-DENSITY-1 sits under item 2 of the
critical path and is **release-relevant under either reading of §4** —
which would make it the highest-value open item in the campaign.

**Flagged as a hypothesis requiring verification, not a finding.** The
worker has been wrong twice this session by treating a plausible
reading as an established one, and this reading is convenient (it makes
today's new open item important). **Verify before scheduling.**

## §7 — Available now, blocked by nothing

- **SF-8** (authorized 2857/2857a) — zero dependency on any held item.
- **DM-1 internal consistency sweep.** §(i) records the founder's
  CONV-004 ruling that *"the v1.3 language 'derivation debt /
  non-upgradable until derived' is superseded"* and re-reads m_s and
  S_c as **measurements**. §(vi) still reads *"two explicit derivation
  debts as promotion gates."* **The paper contradicts itself on whether
  its own promotion is gated.** Cheap to fix, and it sits directly on
  item 5.
- **OPEN-DM-RELIC-1 execution** — pre-registrations are frozen; this is
  the most execution-ready substantive item in the campaign.

## §8 — Recommended sequence (worker's call under PD-006, correctable)

**P0.** Resolve OPEN-B7-SCOPE-1 (§4). One founder sentence. Everything
below reprioritises on the answer.
**P1.** Verify the §6 α dependency. Cheap, and it decides whether
OPEN-SEA-DENSITY-1 is central or peripheral.
**P2.** OPEN-DM-RELIC-1 to verdict — named in B7, execution-ready.
**P3.** DM-1 consistency sweep + v1.5 panel round.
**P4.** FA-SG-R1 decisive deliverable (DP mechanics → χ_static → α).
**P5.** SF-8 assembly, in parallel — it needs no gate.
**Not scheduled:** 1B, Route 2 revival, the C23/C24 arc-inertia
specification — pending P0.
