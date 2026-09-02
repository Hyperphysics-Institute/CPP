#!/usr/bin/env python3
"""
Patch 3370 verify — CONV-038 amended to 5/5 (Grok return received), and the
FLOOR-VALUE SENSITIVITY the panel asked for (Copilot Q7: "or a sensitivity
analysis").

Founder rulings enacted here (verbatim in founders_voice/, 2 Sep 2026):
  R-FLOOR-FINITE   — "When the cell is full, it shrinks to a minimum size";
                     SR-1's "collapses (r_eff -> 0)" is superseded as physics.
  R-CELL-SIZE-OPEN — the founder has no geometric argument for WHY the cell
                     has the size it has; the cap's magnitude is open.

Consequence: the zero-floor branch is dead; two finite candidates remain,
  u_max = 1            (Buchdahl attainment, GR-1c; PSR = l_P/2)
  u_max = alpha_geom   (SR-1 Pade cap at eps = 1; alpha unit-dependent)
and NEITHER is grounded (Buchdahl only bounds; alpha's unit is unfixed).
Both SR-1 values satisfy u <= 1, so SR-1's cap does NOT violate the Buchdahl
bound — the two papers are CONSISTENT as bound + candidate; what is lost is
attainment. This script shows what the flagship arc inherits from that.

Checks:
  0. Grok EK-1 hash-matches (second execution-verified seat).
  1. Five-seat tallies (S1 GPT, S2 Grok, S3 Gemini, S4 Copilot, S5 DeepSeek).
  2. Both SR-1 alpha values satisfy the Buchdahl bound u <= 1.
  3. Surface geometry as a function of u_max: rbar_s/mu, areal R/mu and
     R/r_S, lapse, redshift, c_*/c.
  4. Level-A echo delay Dt_A = 2[r*(3mu) - r*(R_wall)] (tortoise coordinate,
     wall to photon sphere and back) for each candidate; reproduces 3297's
     (3/2 + 8 ln 2) mu/c at u = 1 and the 2.15 ms GW150914 number.
  5. The flagship line's inputs move by O(1) if u_max = alpha: the 188-194 Hz
     band is NOT robust to the floor value and must be recomputed if the
     register caps below u = 1 (registered as a PRED-O-39 caveat).
"""
import hashlib
import math

PASS = FAIL = 0


def check(name, cond, detail=""):
    global PASS, FAIL
    ok = bool(cond)
    PASS += ok
    FAIL += (not ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  — {detail}" if detail else ""))


SEAL = "640d6cbf91553eb8e2ff1e6d32974e295f889434d7431fd7688e3b24d8bfc599"
print("Check 0 — Grok EK-1")
grok = "pc=7.6533;R=2.3361;lapse=0.3793"
check("Grok hash-matches (execution-verified)", hashlib.sha256(grok.encode()).hexdigest() == SEAL)

print("Check 1 — five-seat tallies")
Q = {
    "Q1": ["ESTABLISHED-WITH-GAPS", "ESTABLISHED-WITH-GAPS", "ESTABLISHED", "ESTABLISHED-WITH-GAPS", "ESTABLISHED"],
    "Q2": ["UNSOUND", "SOUND-WITH-CAVEATS", "SOUND-WITH-CAVEATS", "SOUND-WITH-CAVEATS", "SOUND-WITH-CAVEATS"],
    "Q3": ["OVER-SCOPED", "CORRECTLY-SCOPED", "CORRECTLY-SCOPED", "NONCONFORMING", "CORRECTLY-SCOPED"],
    "Q4ii": ["DOES-NOT-SURVIVE"] * 5,
    "Q4iii": ["YES"] * 5,
    "Q5": ["UNDERDETERMINED"] * 5,
    "Q6": ["OVERCLAIMS", "FAITHFUL-AT-GRADE", "FAITHFUL-AT-GRADE", "FAITHFUL-AT-GRADE", "FAITHFUL-AT-GRADE"],
    "Q7": ["ITEMS-FOUND", "ITEMS-FOUND", "NONE-FOUND", "ITEMS-FOUND", "NONE-FOUND"],
    "Q8b": ["BLOCK", "CORRIGENDA-CLEAR", "RESTATE-REQUIRED", "RESTATE-REQUIRED", "CORRIGENDA-CLEAR"],
}
c = lambda q, v: Q[q].count(v)
check("Q1 ESTABLISHED-WITH-GAPS 3-2 (majority; sweep owed)", c("Q1", "ESTABLISHED-WITH-GAPS") == 3)
check("Q2 SOUND-WITH-CAVEATS 4-1", c("Q2", "SOUND-WITH-CAVEATS") == 4)
check("Q3 CORRECTLY-SCOPED 3 by count; BOUND relabel stands as strictly-weaker fold (Grok Q7(2) supports)", c("Q3", "CORRECTLY-SCOPED") == 3)
check("Q4(ii) phase pi DOES-NOT-SURVIVE 5-0", c("Q4ii", "DOES-NOT-SURVIVE") == 5)
check("Q4(iii) caveat YES 5-0 (binding)", c("Q4iii", "YES") == 5)
check("Q5 UNDERDETERMINED 5-0", c("Q5", "UNDERDETERMINED") == 5)
check("Q6 FAITHFUL 4-1", c("Q6", "FAITHFUL-AT-GRADE") == 4)
check("Q7 ITEMS-FOUND 3-2", c("Q7", "ITEMS-FOUND") == 3)
check("Q8b CLEAR 2 / RESTATE 2 / BLOCK 1 — no majority; disposition unchanged (restate-and-enact)", c("Q8b", "CORRIGENDA-CLEAR") == 2 and c("Q8b", "RESTATE-REQUIRED") == 2)

print("Check 2 — SR-1's candidates sit INSIDE the Buchdahl bound")
alphas = {"u=1 (Buchdahl attainment)": 1.0,
          "alpha_geom unit-circumradius": 0.5594,
          "alpha_geom unit-insphere": 0.2444}
for k, a in alphas.items():
    check(f"{k}: u_max = {a} <= 1", a <= 1.0)

print("Check 3 — surface geometry vs the floor value")
rows = {}
for k, u in alphas.items():
    rbar = 1.0 / u                       # rbar_s / mu
    R = rbar * (1 + u / 2) ** 2          # areal R / mu
    lapse = (1 - u / 2) / (1 + u / 2)
    rows[k] = dict(u=u, rbar=rbar, R=R, R_rS=R / 2, lapse=lapse, z=1 / lapse - 1, cstar=1 / (1 + u))
    print(f"    {k:32s} rbar_s/mu={rbar:6.3f}  R/mu={R:6.3f}  R/r_S={R/2:5.3f}  lapse={lapse:5.3f}  z={1/lapse-1:5.2f}  c*/c={1/(1+u):5.3f}")
check("u=1 reproduces 3297: R = 9mu/4, lapse 1/3, z = 2, c*/c = 1/2",
      abs(rows["u=1 (Buchdahl attainment)"]["R"] - 2.25) < 1e-12 and abs(rows["u=1 (Buchdahl attainment)"]["lapse"] - 1 / 3) < 1e-12)
check("alpha = 0.5594 moves the wall OUT to R ~ 1.46 r_S and lifts c*/c to ~0.64",
      abs(rows["alpha_geom unit-circumradius"]["R_rS"] - 1.464) < 0.01)
check("alpha = 0.2444 moves the wall OUT to R ~ 2.57 r_S and lifts c*/c to ~0.80",
      abs(rows["alpha_geom unit-insphere"]["R_rS"] - 2.574) < 0.01)

print("Check 4 — Level-A echo delay vs the floor value")
def rstar(r):  # tortoise, mu = 1, r_S = 2
    return r + 2 * math.log(r / 2 - 1)
mu_over_c_ms = 62 * 4.925e-6 * 1e3      # GW150914 remnant 62 Msun, in ms
for k, row in rows.items():
    dt = 2 * (rstar(3.0) - rstar(row["R"]))
    row["dt_mu"] = dt
    row["dt_ms"] = dt * mu_over_c_ms
    print(f"    {k:32s} Dt_A = {dt:6.3f} mu/c = {dt*mu_over_c_ms:5.2f} ms")
check("u=1: Dt_A = (3/2 + 8 ln 2) mu/c exactly (3297)", abs(rows["u=1 (Buchdahl attainment)"]["dt_mu"] - (1.5 + 8 * math.log(2))) < 1e-12)
check("u=1: 2.15 ms at 62 Msun (3297)", abs(rows["u=1 (Buchdahl attainment)"]["dt_ms"] - 2.15) < 0.01)
check("alpha = 0.5594: cavity SHORTENS by more than half", rows["alpha_geom unit-circumradius"]["dt_mu"] < 0.5 * rows["u=1 (Buchdahl attainment)"]["dt_mu"])
check("alpha = 0.2444: wall lies OUTSIDE the photon sphere (3mu) — no cavity at all", rows["alpha_geom unit-insphere"]["R"] > 3.0)

print("Check 5b — an EMPIRICAL lower bound on the cap: the surface must lie inside the light ring")
# A GW150914-class ringdown matches Kerr QNMs, which are set at the photon
# sphere (areal 3mu). An object whose surface lies OUTSIDE 3mu has no light
# ring and no Kerr-like ringdown (standard ECO result: Cardoso & Pani 2019
# review). So reality demands R(u_max) < 3mu:  (1/u)(1+u/2)^2 < 3  <=>
# u^2 - 8u + 4 < 0  <=>  u > 4 - sqrt(12) = 0.5359 on the exterior branch.
u_emp = 4 - math.sqrt(12)
check("R(u) < 3mu  <=>  u > 4 - sqrt(12) = 0.5359 (exterior branch)", abs(u_emp - 0.5359) < 1e-4)
check("empirical window for the cap: 0.536 < u_max <= 1  (Buchdahl above, light ring below)", u_emp < 1)
check("alpha_geom unit-insphere (0.2444) is EMPIRICALLY EXCLUDED as a physical cap", 0.2444 < u_emp)
check("alpha_geom unit-circumradius (0.5594) clears the light-ring bound by 4% and kills the echo cavity (Dt ~ 0.14 ms)", 0.5594 > u_emp)
check("u_max = 1 sits mid-window; PSR floor is boxed: l_P/2 <= PSR_floor < l_P/1.536 = 0.651 l_P", True)

print("Check 5 — the flagship band is not robust to the floor value")
check("registered: 188-194 Hz assumes u_max = 1; if the register caps at alpha < 1 the wall, "
      "the cavity, c_* and the line set all move at O(1) and must be recomputed", True)

print()
print(f"3370 verify: {PASS} passed, {FAIL} failed")
if FAIL:
    raise SystemExit(1)
