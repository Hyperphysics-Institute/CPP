# The elastic channel: a real gap found, and closed in-prior by the suite's own windows (Patch 2335, 7 July 2026)

**What this patch is:** item 2 of the founder-approved pre-panel sequence — the one route
to the anchor suite that does not touch TAMB-1(b) in either direction. **Verify:**
`code/2335_elastic_channel_registry_check.py` (6/6; check 1 scans the 1870 MC source
programmatically). **NO VERDICT MOVED.** No resting paper touched.

## 1. The gap (the founder's instinct was right)

The question: with capture killed, can the *elastic* channel alone carry the suite —
specifically via the attractive screened E_qq residual, whose focusing was computed for
**capture** (1857/1858) but whose **elastic transport** (focused-but-not-captured
large-angle deflection) might carry intrinsic velocity dependence with no Sea dissipation
at all?

Registry answer, in two parts. First, the elastic floor's velocity dependence **was**
measured — the 1870–71 MC gives a mildly falling curve, 0.09–0.15 (50 km/s) → 0.02
(3500), not the flat 0.046 the 2324 KILL branch used (that is the ~1500 km/s value).
Second — **the gap is real**: the 1870 MC force law is the repulsive coat potential
only (`E_ee·e^(−r)/r`, confirmed by programmatic source scan). The attractive residual's
elastic transport was never in the measurement. Something we hadn't looked at existed,
exactly as suspected.

## 2. The closure (shape, not magnitude)

Whether the unevaluated channel can hold the suite is decided by window arithmetic
before any new MC is run. Any σ(v) holding the anchors must satisfy two ratios:

- **dSph/pin bar:** σ(30)/σ(50) ≥ 20/5 = 4 ⇒ local log-slope **s ≥ 2.71**;
- **pin/LSB bar:** σ(50)/σ(200) ≤ 5/0.7 = 7.14 ⇒ local log-slope **s ≤ 1.42**.

No monotone single-wing shape satisfies both (and mixtures are bounded by their steepest
component) — the 2324 no-stable-resting-point result, reproduced independently on the
elastic side. The attractive-elastic channel's *maximal* wings are s = 2 (classical
focusing = quantum s-wave unitarity; exact, by energy conservation) and s = 4 (resonant
Sommerfeld ceiling). **s = 2 fails both bars** (×1.44 short on dSph/pin, ×2.2 over on
pin/LSB); **s = 4 fails LSB ×36** (the LSB-parks-on-the-floor pattern). The de Broglie
check confirms the quantum framing is the right ceiling at dwarf velocities
(λ_dB = 28–336 fm vs R_scr 15–30 fm) — and it still fails.

Decisive detail: v_esc(R_scr) = 1130–3910 km/s puts the *entire* suite inside one wing,
and the wing's magnitude comfortably reaches the windows. **The route fails on slope
alone** — which no resolution of OPEN-SS-43 (R_s(N) moves magnitude, not slope) can
rescue. The suite demands a knee with a steep-then-flat structure between 30 and 200
km/s; the registered elastic physics supplies only smooth wings.

## 3. Ledger

- **Elastic route CLOSED-in-prior** (ratio arithmetic on registered windows; same
  spectral bar as 2324). Honest caveat, named: this is an in-prior exclusion of the
  channel's maximal wing — the MC-with-attraction remains a bounded one-session
  *measurement* if the founder prefers measured to arithmetic. The arithmetic says it
  cannot change the verdict.
- **DM-1 disclosure queued (errata-level):** the measured floor is repulsive-coat-only;
  the attractive-elastic contribution is unevaluated (it can only raise the floor's
  small numbers, which currently helps nothing and threatens nothing — cluster margins
  are ×2+).
- **KILL-branch refinement (class unchanged):** using the measured velocity-dependent
  floor instead of flat 0.046 — pin fails ×6.7–11 (was ×22), LSB ×11.7 (was ×15),
  dSph ×130–1100 (was ×435–2174). The failures soften by ×2–3 and remain fatal.
- **NO VERDICT MOVED:** G4 = KILL-on-suite-conditional stands (2333, self-red-teamed
  2334). The pre-panel sequence is complete: the kill survived its own red team, and the
  one gate-independent route is closed. **The CONV-001 package is ready to assemble on
  the founder's call** — pointers: axis-enumeration exhaustiveness, A3′ memorylessness
  reading (2334), and this patch's ratio bars as the elastic-side exclusion.
