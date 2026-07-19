# REACH-AUDIT-2 R-A executed: the dependency ledger drawn; the old classifier's truncation defect confirmed; ONE live reach-S defect found (ring L=8 truncation binds — the window's lower endpoint carries a caveat); the duty verdict INVARIANT under reach-S; the pin and the 2514 record both independently reproduced

**Patch 2574, 19 July 2026. Governed by the 2567 §3 audit registration; readings frozen in
`code/2574_reach_audit2_ra.py` header before any run. Founder-input-free per the 19 Jul session
directive. Status: R-A EXECUTED; ledger below; R-B queue registered.**

## 1. Disclosure chain (anti-erasure; four events)

**(a) Process lesson:** the first execution attempt ran as a background job polled across session
turns; the job was killed at a turn boundary while liveness checks were matching their own
command line. Lesson registered for the operating notes: long runs execute in-foreground within
one tool call, sized to fit. **(b)** The first attempt's fallback path executed the entire 2557
re-registration — wasteful, but its completed cells BANK as an independent from-scratch
reproduction: the reach-S == reach-G straight-rod control returned True, and the E_close cells
reproduced at +156.5 / +152.7 / +153.5 / +156.9 — all inside the registered [+152.7, +156.9]
band. **(c) Override-failure-turned-reproduction-check:** the first duty "re-run" bound the
reach-S override in the wrong namespace, silently re-running the OLD classifier — and returned
0.0010 / 0.0021 / 0.0095, matching the registered 2514 record to every printed decimal: a
bit-exact reproduction of the registered result, banked; the four-decimal match is what exposed
the override failure; fixed (override bound in the chain namespace) and re-run. **(d)** The
truncation census was extended past its frozen list to L ∈ {10, 14, 18, 24, 26} — a disclosed
post-freeze extension, census-only, no physics reading attached.

## 2. The dependency ledger (every reach-consuming DM-lane file)

| File | Classifier | Registry load | Status |
|---|---|---|---|
| 2455 / 2461 | old (global Δz) — definition site | functional lineage | RETIRED at 2556/2557 |
| 2510 hardened inertia | old, ring | ring−straight(16) headline; SF-6-contended promotion runs | headline RE-REGISTERED (2557 arc); **contention/pile statistics → R-B** |
| 2513 MW-modes | old, ring | mode curvatures (C7 support) | **un-re-run → R-B** |
| 2514 emergent duty | old, ring | registry condition 2 (Branch L) | **RE-RUN THIS PATCH → INVARIANT (§4)** |
| 2549 ENDBOND-2 | old, 2-plane fragment | Branch-I closure [−3.6, +1.4] | **un-re-run → R-B** (low stakes; closure is a null) |
| 2551 ENDBOND-3 | old | E_close curve/pin | SUPERSEDED by 2557 P1 (reach-S) — CLEARED |
| 2554 FORM-L-1 | old | formation table | SUPERSEDED by 2557 P2 — CLEARED except §3's L=8 caveat |
| 2557 / 2559 / 2565 / 2571 / 2573 | reach-S | pin, window/wall, gate, maps, K1a | reach-S era; §3's L=8 caveat attaches to 2559's window endpoint |

## 3. Truncation findings (hunt item 6 — the audit's central results)

The 'q' reach list truncates as `sorted(set(inpl+axl))[:5]` — **INDEX order, not distance
order**. Census of when the cutoff actually binds:

- **Old Δz rule, ring L=16: BINDS (max count 7).** Every pre-correction ring run was silently
  discarding up to two in-reach neighbors by an arbitrary index rule — a second, independent
  defect COMPOUNDING the Δz misclassification in the retired classifier. Both died together at
  2556/2557; recorded to complete the damage accounting the panel asked for.
- **Reach-S: never binds at L ∈ {10, 12, 14, 16, 18, 20, 22, 24, 26} or on the straight rod —
  but BINDS at L = 8 (max count 7, at 16 of 32 qCPs).** The tightest ring crowds axial
  neighbors inside 1.3 fm. **This is a LIVE defect touching one registered quantity:** the
  E_close(8) cell — i.e., the "closure pays down to L=8" statement and the lower endpoint of
  the formation window "even L ∈ [8, 22]". **The wall bracket (22, 24), the payoff maximum,
  and the entire window body are CLEAN.** A caveat rider attaches to the window's lower
  endpoint until R-B item 1 clears it; the wall — the falsifiable positive — is untouched.
- **Zero-margin note:** at L = 16 the count is EXACTLY 5. One more in-reach neighbor on any
  future geometry would truncate silently. **Recommendation ADOPTED:** all future reach-S
  consumers carry an assert that the pre-truncation count ≤ 5, so binding can never again be
  silent.

## 4. The duty re-run (registry condition 2)

Genuinely under reach-S: duty_qq(contact) = **0.0000 / 0.0011 / 0.0052** at dt = τ_C/{100, 50,
25} (n = 27431 / 21924 / 17207 — thin-statistics guard clear), vs the registered old-classifier
values 0.0010 / 0.0021 / 0.0095. Numbers shift (roughly halve); **the pre-registered branch
reading is UNCHANGED: duty < 3/7 at all three dt → Branch L, adverse direction — at both
classifiers.** Per the frozen invariance verdict: **INVARIANT**; no supersession rider, no
founder-disclosure trigger; registry condition 2's recorded status stands as registered.

## 5. R-B queue (registered; order fixed)

1. **L=8 truncation sensitivity** (the one live defect): E_close(8) re-run under a declared
   convention union (distance-ordered [:5] AND untruncated), own mini-prereg since a frozen
   reading could move; the window's lower endpoint rider clears or supersedes per the outcome.
2. **2513 mode curvatures** under reach-S (C7-supporting; invariance verdict to be frozen in
   its own header).
3. **2549 ENDBOND-2 fragment** under reach-S (null-closure confirmation; low stakes).
4. **2510 contention/pile statistics** under reach-S.

## 6. Bookkeeping

79.5% untouched (the headline promotion observable was already reach-S re-registered; today
adds: duty verdict invariant, pin reproduced from scratch, one bounded caveat at the window's
lower endpoint, and the compounding old-classifier defect quantified — net integrity GAIN).
Dated line to the standing queue. The K-phase remains at the founder's adjudication #3
(F-a / F-b / F-c); R-B items are further founder-free interim work. Next patch: R-B item 1
(the L=8 sensitivity mini-prereg + run) unless the founder's adjudication arrives first.
