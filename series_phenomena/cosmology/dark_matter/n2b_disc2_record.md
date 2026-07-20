# N2B-DISC-2 execution record — VERDICT RD2′ (THE REPAIR FAILED; THE SINGLE-PASS DEPOSIT IS IMPLEMENTATION-SENSITIVE WITH THE WINDOW EXONERATED): THE BLOCK HARDENS; ESCALATION IS DERIVATIONAL; FOUNDER FLAG RAISED

**Patch 2626, 20 July 2026.** Execution under `n2b_disc2_prereg.md` (2625) only.
Verify: `code/2626_n2b_disc2.py`, stages controls | m1 | m23, all run.

## 1. Controls — ALL PASS

```
[C1] pin exact (CAP, Sea=304.706982, gmax=2.097582, deltas 0.0)
[C2a] Sea(eta=0) = -1.4e-13   [C2b] 48.715/25.446/11.002, ratios 1.91/2.31  PASS
[C3] max ktA=0.0079, ktB=0.0000                                              PASS
[C4] t_x=2.44 exists on the SCA cell, S_WA(eta=0)=2.8e-14 machine-zero;
     ON anchor t_x=11.13 <= t_m=12.40                                        PASS
```

## 2. Gates (raw, then reading)

```
v=0.10: S_WA(1/100,1/200,1/400) = 228.35, 203.85, 182.72   monotone decrements 24.5, 21.1
        [G1] shrinking TRUE, final-inc 0.116                        FAIL (<=0.05)
        [G2] 0.000, 0.001  PASS   [G2-band] |dbeta|=0.000
        [G3] 0.000, 0.000  PASS (windows IDENTICAL)
        [G4] S_cum 295.5, 296.8, 292.5  final-inc 0.015 PASSES magnitude;
             increments 1.3 -> 4.3 non-monotone                     FAIL as frozen
v=0.95: S_WA = 360.96, 168.52, 301.59  wild non-monotone; final-inc 0.441   [G1 FAIL]
        [G2] 0.426, 0.275 FAIL; band |dbeta|=0.150 NOT stable (<=0.05)
        [G3] 0.000, 0.000  PASS   t_x dt-stable to 0.02 fm/c (2.49/2.44/2.43)
        [G4] S_cum 578.6, 579.7, 572.5  final-inc 0.013 magnitude;
             increments 1.1 -> 7.2 non-monotone                     FAIL as frozen
[G5] ratios 0.496 and 2.085 (method-B excluded at the high anchor per the
     frozen band clause)                                            FAIL (<=0.20)
```

**READING — RD2′, as frozen: THE REPAIR FAILED.** G1 fails dt-stably at both
anchors; G4 fails as frozen at both; G5 fails at both. **The deposit itself — not
the window — is implementation-sensitive.** The exoneration of the window is
total and is this record's sharpest fact: the first-crossing trigger is dt-stable
to 0.02 fm/c, and W-A and W-B select IDENTICAL split sets at every anchor and dt
(G3 = 0.000 everywhere) — yet S_WA still swings 169 → 302 MeV across a dt-halving
at transit-γ. The per-cycle shed sequence during a steep-width encounter does not
converge with dt even though its full-window integral does. **The DISC-1 block
HARDENS FURTHER**; per the frozen escalation: **the transit-γ sink law needs
DERIVATION, not a third instrument — FORM-1-adjacent; the founder flag is raised
at this contact.** Adverse, same font.

## 3. Honest annotations on the frozen gates (disclosed, changing nothing)

- **G4's magnitude leg passed at 1.3–1.5% at both anchors**; the gate failed on its
  monotonicity conjunct, which at sub-percent increments is gating on noise
  ordering. The verdict does not lean on G4 (G1 and G5 fail independently), and a
  successor prereg should gate cumulative convergence on magnitude only — recorded
  here so the design lesson is banked at the patch where it was paid for.
- **The banner-erratum class from 2624 does not recur**: the 2626 script prints its
  own patch line.

## 4. Disclosed-unread bank (successor design input; nothing reads)

1. **S_cum is magnitude-converged to 1.3–1.5% at BOTH anchors** — across every
   tested dt, the end-of-window cumulative is the one deposit object this
   instrument renders registerable.
2. **The soft width is clean:** at w = 2, low-γ anchor, S_WA is dt-stable to 0.8%
   (149.86 → 151.10) with exact window agreement — the single-pass dt-sensitivity
   is STIFFNESS-COUPLED (steep Morse walls, trajectory-phase sensitivity against
   the once-per-τ_C split clock), not universal. A derivational account has a
   concrete discriminating fact to explain.
3. Low-γ method agreement at four decimals, again (fourth independent occurrence).
4. M2 physical span at 1/200: 203.85, 111.58, 168.52 — non-monotone in v
   (unread; the v = 0.40 dip is now seen at two dt values).

## 5. Standing

DISC-1 → DISC-2 arc complete at two adverse verdicts and one exoneration chain:
2624 convicted the global-argmin window; 2626 exonerated windows entirely and
convicted the single-pass deposit at the steep width. **What survives as
registerable at transit-γ, pending derivation: nothing single-pass; the cumulative
S_cum (magnitude-banded ~1.5%) is the candidate object for any successor prereg.**
The block stands at full strength: high-γ (v > 0.3c) consumers, Sea-deposit-growth
discussion, and H-a/H-b preference all remain blocked. **Founder flag (physics
question, PD-006 contact): the FORM-1 dedicated session should carry the transit-γ
sink derivation on its agenda alongside the Morse-form derivation — the
discriminator lineage has reached the limit of what instrumentation can certify.**
FUNNEL-1 remains discharged-at-class (2624). Fences: no rates, no σ_cap, no relic
contact; EDGE-2(i) queued; **79.5% untouched.** Founder-free queue after this
patch: ROB-1, DEP-1, R-B items 1–4.
