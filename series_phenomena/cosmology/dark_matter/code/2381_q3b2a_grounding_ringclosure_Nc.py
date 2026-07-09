#!/usr/bin/env python3
"""
PATCH 2381 -- Q3b-2a GROUNDING PASS (Q3b-2 contract, registered 2380).

Deliverables (per the pre-registered contract):
  (1) 0861/0881 kinetics machinery re-grounded on clean clone: the key
      registered quantities RECOMPUTED from the registered functional forms
      and asserted against stored values (full scripts also re-run; see
      reasoning/2381.md).
  (2) The ring-closure BENDING-COST statement extracted from the registered
      0861 machinery (SY J-factor) and cross-checked against the exact
      discrete-polygon computation.
  (3) The N_c IMPLICATION computed: structural floor, energetic closure
      window vs the D1 band (2374), peak-placement stiffness demand for
      survivors N in [3,6], and an INDICATIVE ring-population tail preview.
  (4) The VERIFY BATTERY for Q3b-2b/2c FIXED (V1-V5 below); this script IS
      the battery and must pass 5/5 before any Q3b-2b kinetics is trusted.

Discipline: 0865 (no smuggled parameters -- every number below is either a
registered stored value or derived from one); the contract's no-steering
rule (walls are checked against, not aimed at); SY validity boundary u <~ 6
carried loudly where it binds.

Run: python3 2381_q3b2a_grounding_ringclosure_Nc.py
Exit code 0 iff verify battery 5/5.
"""

import json
import os
import sys
import numpy as np

FAILURES = []


def check(name, ok, detail):
    tag = "PASS" if ok else "FAIL"
    print(f"   [{tag}] {name}: {detail}")
    if not ok:
        FAILURES.append(name)


# ---------------------------------------------------------------------------
# Registered inputs (stored values; provenance in comments)
# ---------------------------------------------------------------------------
L_RUNG_FM = 1.0            # 0861 registered convention (rung spacing, fm)
SY_A, SY_B, SY_P = 14.054, 0.246, 5.0   # 0861 registered SY J-factor shape
U_STAR_STORED = 3.37       # 0861 stored closure peak (L*/l_p)
LP_BAND_STORED = (105.0, 702.0)  # 0861 stored l_p band [fm] for N* in [355,2366]
N_BAND_0860 = (355.0, 2366.0)    # 0860 band used by 0861
PHI_RANGE = (6.7e-15, 7.4e-10)   # 0881 stored volume-fraction bracket
EKT_BAND_0881 = (24.0, 41.0)     # 0881 stored inverse-map band (N ~ 5-60)
D1_BAND_STORED = (23.2, 36.2)    # 2374 demand sheet D1 (survivors N = 3-6)
SURVIVOR_N = (3, 6)              # corridor survivors (2374/2375 small-N regime)
CACHE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                          "2379_unit_cache.json")


def J_SY_stiff(u):
    """0861 registered Shimada-Yamakawa stiff-chain J-factor shape,
    u = L/l_p. Valid u <~ 6."""
    return u ** (-SY_P) * np.exp(-SY_A / u + SY_B * u)


print("=" * 76)
print(" PATCH 2381 -- Q3b-2a GROUNDING: 0861/0881 + ring-closure N_c implication")
print("=" * 76)

# ---------------------------------------------------------------------------
# V1 -- SY closure peak reproduces the 0861 stored value
# ---------------------------------------------------------------------------
print("\n V1 -- SY ring-closure peak (0861 machinery reproduction)")
u = np.linspace(0.5, 6.0, 20000)
u_star = u[np.argmax(J_SY_stiff(u))]
check("V1 SY peak", abs(u_star - U_STAR_STORED) <= 0.01,
      f"u* = {u_star:.3f} vs stored {U_STAR_STORED} (tol 0.01)")

# ---------------------------------------------------------------------------
# V2 -- 0861 l_p band endpoints reproduce
# ---------------------------------------------------------------------------
print("\n V2 -- 0861 l_p band (formation peak in the 0860 band)")
lp_lo = N_BAND_0860[0] * L_RUNG_FM / u_star
lp_hi = N_BAND_0860[1] * L_RUNG_FM / u_star
check("V2 l_p band",
      abs(lp_lo - LP_BAND_STORED[0]) <= 1.0 and abs(lp_hi - LP_BAND_STORED[1]) <= 1.0,
      f"[{lp_lo:.0f}, {lp_hi:.0f}] fm vs stored [{LP_BAND_STORED[0]:.0f}, "
      f"{LP_BAND_STORED[1]:.0f}] fm (tol 1)")

# ---------------------------------------------------------------------------
# V3 -- 0881 inverse map + the 2374 D1 small-N band reproduce
# ---------------------------------------------------------------------------
print("\n V3 -- 0881 inverse map E_bond/kT_form = 2 ln N - ln phi")
phi_lo, phi_hi = PHI_RANGE
ekt_0881 = (2 * np.log(5.0) - np.log(phi_hi), 2 * np.log(60.0) - np.log(phi_lo))
d1 = (2 * np.log(SURVIVOR_N[0]) - np.log(phi_hi),
      2 * np.log(SURVIVOR_N[1]) - np.log(phi_lo))
check("V3a 0881 band",
      abs(round(ekt_0881[0]) - EKT_BAND_0881[0]) <= 1 and
      abs(round(ekt_0881[1]) - EKT_BAND_0881[1]) <= 1,
      f"N~5-60 -> [{ekt_0881[0]:.1f}, {ekt_0881[1]:.1f}] vs stored "
      f"[{EKT_BAND_0881[0]:.0f}, {EKT_BAND_0881[1]:.0f}] (tol 1 on rounding)")
check("V3b D1 small-N band",
      abs(d1[0] - D1_BAND_STORED[0]) <= 0.1 and abs(d1[1] - D1_BAND_STORED[1]) <= 0.1,
      f"survivors N=3-6 -> [{d1[0]:.1f}, {d1[1]:.1f}] vs stored 2374 D1 "
      f"[{D1_BAND_STORED[0]}, {D1_BAND_STORED[1]}] (tol 0.1)")

# ---------------------------------------------------------------------------
# V4 -- discrete-polygon bending vs continuum rigid ring: exact identity
# ---------------------------------------------------------------------------
print("\n V4 -- bending-cost cross-check: discrete N-gon vs continuum rigid ring")
# Discrete: N joints, each bent by exterior angle 2pi/N, quadratic joint
# stiffness B = (l_p/l_rung) kT  =>  E = N * (B/2) (2pi/N)^2 = 2 pi^2 (l_p/l_rung) kT / N.
# Continuum rigid circular ring: E = 2 pi^2 kappa / L = 2 pi^2 (l_p/l_rung) kT / N.
ok4 = True
for N in range(3, 33):
    for r in (0.5, 0.9, 1.78, 5.0, 300.0):
        Ed = N * 0.5 * r * (2 * np.pi / N) ** 2          # discrete polygon
        Ec = 2 * np.pi ** 2 * r / N                       # continuum rigid ring
        if abs(Ed - Ec) > 1e-12 * max(Ed, 1.0):
            ok4 = False
check("V4 identity", ok4,
      "E_discrete(N-gon) == 2 pi^2 (l_p/l_rung)/N kT to machine precision, "
      "N=3..32, ratios 0.5..300")
print("   NOTE: the SY exponent uses c = 14.054 (fluctuation-corrected saddle),")
print("         not the rigid 2 pi^2 = 19.739; SAME 1/N form, coefficient ratio "
      f"{SY_A / (2 * np.pi ** 2):.3f}.")
print("         Both coefficients are carried below; neither is chosen to help.")

# ---------------------------------------------------------------------------
# V5 -- 2379 unit-cache integrity (the committed reusable infrastructure)
# ---------------------------------------------------------------------------
print("\n V5 -- 2379_unit_cache.json integrity")
try:
    cache = json.load(open(CACHE_PATH))
    n_keys = len(cache)
    schema_ok, bins_ok = True, True
    Ns, signs, scs, eps = set(), set(), set(), set()
    for k, v in cache.items():
        parts = k.split(",")
        if len(parts) != 4:
            schema_ok = False
            continue
        Ns.add(int(parts[0])); signs.add(parts[1])
        scs.add(float(parts[2])); eps.add(float(parts[3]))
        if not (isinstance(v, list) and len(v) == 13
                and all(isinstance(x, (int, float)) and x >= 0 for x in v)):
            bins_ok = False
    check("V5 cache", schema_ok and bins_ok and n_keys == 336,
          f"{n_keys} keys (expect 336); schema N,sign,S_c,eps_th; 13 non-negative "
          f"bins each; N in [{min(Ns)},{max(Ns)}], signs {sorted(signs)}, "
          f"S_c {sorted(scs)}, eps_th {sorted(eps)}")
    print("   NOTE: semantic cross-check (eps_th=1 reproducing the stored 2366b")
    print("         viol=3/642.219095) lives in the summed-criterion machinery and")
    print("         is re-asserted when that channel runs in Q3b-2c -- not duplicated here.")
except Exception as e:
    check("V5 cache", False, f"load failed: {e}")

# ---------------------------------------------------------------------------
# THE RING-CLOSURE N_c IMPLICATION (computed, not asserted)
# ---------------------------------------------------------------------------
print("\n" + "-" * 76)
print(" THE BENDING-COST STATEMENT (extracted from registered 0861 machinery)")
print("-" * 76)
print("""   Closing an N-rung chain into a ring costs bending energy
        E_close(N) = c * (l_p/l_rung) * kT / N,
   with c = 14.054 (SY fluctuation-corrected exponent, registered 0861 J-factor)
   or c = 2 pi^2 = 19.739 (rigid/discrete polygon, exact -- V4). Loops with
   contour L << l_p are exponentially bending-suppressed; loops with L >> l_p
   are entropy-suppressed (u^-5 tail). Stiffness alone places the ring peak at
        N* = 3.37 * (l_p/l_rung).""")

print("-" * 76)
print(" N_c IMPLICATION 1 -- THE STRUCTURAL FLOOR")
print("-" * 76)
print("""   A non-degenerate closed polygon requires N >= 3. N=1 cannot close;
   N=2 closure is a doubled-back degenerate loop (two joints each bent by pi,
   the maximal bending configuration -- and geometrically two coincident,
   anti-parallel rungs, i.e. not a loop enclosing area at all). Therefore:
        IF the frozen-out stable species is the CLOSED ring
        (closure eliminating both reactive ends), THEN
        w_ring(1) = w_ring(2) = 0 IDENTICALLY and N_c = 3 EMERGES
        from ring topology -- it is not imposed.
   CONDITIONAL, loudly: 'stability = closure' is exactly what Q3b-2b must
   DERIVE from the substrate kinetics (open-chain end reactivity vs ring
   inertness at freeze-out, and the residual open-chain fraction). If the
   kinetics leaves an open-chain population at freeze-out, w(1), w(2) are
   NOT zero and must be computed -- the D2/D3 budgets then bind numerically.""")

print("-" * 76)
print(" N_c IMPLICATION 2 -- THE ENERGETIC CLOSURE WINDOW (vs D1)")
print("-" * 76)
print("   Closure trades ONE extra bond (gain E_bond) against E_close(N).")
print("   Favorable iff  (l_p/l_rung) <= N * (E_bond/kT_form) / c.")
print(f"   With the D1 band E_bond/kT_form in [{D1_BAND_STORED[0]}, {D1_BAND_STORED[1]}]:")
for c, cname in ((SY_A, "SY 14.054"), (2 * np.pi ** 2, "rigid 19.739")):
    for N in (3, 6):
        lo = N * D1_BAND_STORED[0] / c
        hi = N * D1_BAND_STORED[1] / c
        print(f"      c = {cname:13s} N = {N}:  l_p/l_rung <= [{lo:.2f}, {hi:.2f}]")

print("-" * 76)
print(" N_c IMPLICATION 3 -- PEAK PLACEMENT: THE STIFFNESS DEMAND INVERTS")
print("-" * 76)
r_lo = SURVIVOR_N[0] / u_star
r_hi = SURVIVOR_N[1] / u_star
print(f"   Survivor peak N* in [{SURVIVOR_N[0]}, {SURVIVOR_N[1]}]  =>  "
      f"l_p/l_rung in [{r_lo:.2f}, {r_hi:.2f}]")
print(f"   (at l_rung = {L_RUNG_FM} fm: l_p ~ {r_lo:.2f}-{r_hi:.2f} fm)")
old_lo, old_hi = LP_BAND_STORED
print(f"   The 0861 large-loop era demanded l_p in [{old_lo:.0f}, {old_hi:.0f}] fm --")
print(f"   the small-N corridor demand is x{old_lo / r_hi:.0f}-x{old_hi / r_lo:.0f} "
      "SOFTER. Same single substrate")
print("   object (the 2eDP:2qDP rung-bond SSV angular stiffness), inverted band.")
print("   CONSISTENCY: the peak-placement band sits INSIDE every energetic-window")
peak_inside = r_hi <= min(SURVIVOR_N[0] * D1_BAND_STORED[0] / (2 * np.pi ** 2),
                          SURVIVOR_N[0] * D1_BAND_STORED[0] / SY_A)
print(f"   ceiling above (tightest ceiling {SURVIVOR_N[0] * D1_BAND_STORED[0] / (2*np.pi**2):.2f} "
      f"> {r_hi:.2f}: {'YES' if peak_inside else 'NO'}) -- no tension between D1 and placement.")
print("   => Q3b-2b's kinetics must DELIVER l_p/l_rung ~ 0.9-1.8 or the ring")
print("      mechanism dies at peak placement. This is now a NAMED kill condition.")

print("-" * 76)
print(" N_c IMPLICATION 4 -- CEILING PREVIEW ABOVE N ~ 6 (INDICATIVE ONLY)")
print("-" * 76)
print("   w_ring(N) proportional to exp(-N/<N>) * J_SY(N/(l_p/l_rung)), N >= 3.")
print("   Tail mass W(N>6) vs Flory at matched <N> (SY validity u <~ 6 binds the")
print("   high-N tail at these stiffness ratios -- numbers are indicative; the")
print("   discrete kinetics in Q3b-2b owns the real tail):")
Ngrid = np.arange(3, 33)
for r in (0.9, 1.3, 1.78):
    for Nbar in (3.0, 4.5, 6.0):
        w = np.exp(-Ngrid / Nbar) * J_SY_stiff(Ngrid / r)
        w /= w.sum()
        tail = w[Ngrid > 6].sum()
        Nfl = np.arange(1, 33)
        wf = np.exp(-Nfl / Nbar)
        wf /= wf.sum()
        tail_f = wf[Nfl > 6].sum()
        supp = tail_f / tail if tail > 0 else np.inf
        print(f"      l_p/l_rung={r:.2f} <N>={Nbar:.1f}:  W_ring(N>6)={tail:.4f}  "
              f"W_Flory(N>6)={tail_f:.4f}  suppression x{supp:.1f}")
print("""   READ HONESTLY (the numbers above, not the hope): equilibrium ring
   weighting DOES NOT deliver the ceiling. At the soft end (l_p/l_rung=0.9,
   peak at N*=3) the tail suppression is a marginal x1.0-1.2; at the stiff
   end (1.78, peak at N*=6) the J-factor RISES through N=3..6 and the ring
   tail is ANTI-suppressed (x0.4-0.7 vs Flory) -- the u^-5 decay does not
   bite until N >> 3.37*(l_p/l_rung). SPLIT VERDICT of the grounding pass:
      * the FLOOR (N_c=3, w(1)=w(2)=0) is structural and robust;
      * the CEILING above N~6 is NOT free -- if it exists it must be
        KINETIC: a closed ring has no reactive ends, so RING GROWTH STOPS
        AT CLOSURE and rings exit the growth ladder. The frozen product is
        set by closure-rate vs growth-rate competition on OPEN chains --
        an ensemble the equilibrium weighting above cannot represent.
   That kinetic-closure shutoff is now Q3b-2b's NAMED ceiling candidate,
   and 'equilibrium shape emerges anyway' (the registered death mode)
   remains fully armed against it.""")

# ---------------------------------------------------------------------------
# Battery verdict
# ---------------------------------------------------------------------------
print("\n" + "=" * 76)
n_checks = 6  # V1, V2, V3a, V3b, V4, V5
print(f" VERIFY BATTERY: {n_checks - len(FAILURES)}/{n_checks} "
      f"({'ALL PASS' if not FAILURES else 'FAILURES: ' + ', '.join(FAILURES)})")
print(""" FIXED FOR Q3b-2b/2c (binding): V1 SY peak; V2 0861 l_p band; V3 0881
 inverse map + D1 small-N band; V4 discrete-continuum bending identity;
 V5 unit-cache integrity. Q3b-2b adds its own kinetics-level checks ON TOP;
 this battery must stay green underneath.""")
print("=" * 76)
sys.exit(0 if not FAILURES else 1)
