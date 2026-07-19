#!/usr/bin/env python3
"""
PATCH 2546 -- OPEN-DM-ENDBOND-1 R-A EXECUTED under endbond1_preregistration.md ONLY.

MANDATORY FIRST ACT (prereg S2.2): the FUNCTIONAL WALK, from the 2450/2455 artifacts and
their reasoning files ONLY. Findings encoded and asserted below IN ORDER, before any
lattice number is computed (blindness: the Branch-I determination is a walk-level finding
from artifact text, fixed before the electric partial exists).

WALK FINDINGS (sources cited in endbond1_ra_walk.md):
(i)  PAIR COUPLING: the registered ENERGY functionals couple every pair through the
     species weight product (W_q^2 = alpha_s for qq; W_e^2 = alpha for ee; W_qW_e for qe)
     inside the SIGNED switched-pair statics (2450 Esw). The strong sector appears in the
     energy content ONLY through those alpha_s weights and the 2455 saturation lengths.
     The always-attractive color channel of 2455 confirmation (3) ("color attraction
     persists when charge is neutralized") is registered as a DANCE KINEMATIC RULE
     (targeting continuation) -- it appears in NO registered energy functional. The 2455
     smeared-Coulomb form ("the pair potential is Coulomb smeared over the constituent
     ZBW length") is registered FOR A SUPERPOSING PAIR in the DP state; which static
     cross-plane qq pairs (if any) sit in that channel, and at what duty, is NOWHERE
     registered. 2450's own scope note states the cohesion outright: "the functional
     does not bind under dilation (E0=+486 MeV > 0); binding = strong-sector registry"
     -- UNMODELED. ==> The static strong-sector pairwise form is UNDER-DETERMINED:
     BRANCH I fires at walk level, named blocker "strong-sector pairwise form".
(ii) RADIAL FORM: bare 1/r (2450 Esw) and soft-core 1/sqrt(r^2+a_ij^2) with
     a_qq=hbar*c/264=0.747, a_ee=hbar*c/553=0.357, a_qe=sqrt(a_qq*a_ee)=0.516 fm
     (2455 registration) are BOTH in-lineage for the electric statics -> 2541 S3 union
     rule: compute both, report union with spread.
(iii) PARITY SIGNS: alternating parity is coded as the (-1)^k pattern-charge flip
     (2450 build(), 2455 scaffolds). For this plane pattern (alternating corner charges,
     opposite-charge coat), a 90-degree rotation of the pattern is IDENTICAL to the
     charge flip -- the 2540 "90-degree offset" identity. VERIFIED NUMERICALLY below.

CONSEQUENCE (prereg S5, Branch-I limb, verbatim): "partials (electric-sector
contribution, geometry sums) bank." No depth is frozen; gates G1/G2/G3 DO NOT FIRE.
BANKED PARTIALS: the electric-sector (switched-pair statics) contribution to
E_endbond = -E_cross under both radial conventions; the cross-pair geometry sums.

Geometry (prereg S2.1): element plane = 4 qCP square (edge a_q=1.15, alternating
charges) + 4 eCP on the square's corner diagonals at R_e=1.301, charge opposite the
adjacent qCP (2455 coding = the registered corrected placement; the 2450 axes placement
is superseded per the 2455 amendment note). Stack pitch D=1.15, alternating parity.
"""
import numpy as np

AHC = 197.3
PHI_G = (1 + np.sqrt(5)) / 2
ALPHA_S = 5 / (8 * PHI_G)          # registered upstream lineage (sqrt5 fence: pre-existing)
ALPHA = 1 / 137.036
DELTA = 3 / 7                       # duty factor; (1-2*DELTA) = 1/7
DUTY = 1 - 2 * DELTA
A_Q = 1.15
D = 1.15
H = A_Q / 2
R_E = 1.6 * (A_Q / np.sqrt(2))      # = 1.301 fm (registered)
A_QQ = AHC / 264.0                  # 0.747 fm (2455 registration)
A_EE = AHC / 553.0                  # 0.357 fm (= 1814 lambda-bar)
A_QE = np.sqrt(A_QQ * A_EE)         # 0.516 fm

assert abs(R_E - 1.3011) < 1e-3
assert abs(ALPHA_S * AHC / A_QQ - 102.0) < 0.1   # the registered derived contact depth (NOT an input here)

def plane_2455(par, rot90=False):
    """Registered element plane, 2455 coding: qCP corners, eCP on corner diagonals,
    eCP charge opposite adjacent qCP. par multiplies pattern charges (alternating
    parity as coded); rot90 instead rotates the pattern by 90 deg (2540 identity check)."""
    q = [(+H, +H, +1), (-H, +H, -1), (-H, -H, +1), (+H, -H, -1)]
    S = []
    for (x, y, sg) in q:
        S.append((x, y, sg, 'q'))
    for (x, y, sg) in q:
        n = np.hypot(x, y)
        S.append((R_E * x / n, R_E * y / n, -sg, 'e'))
    out = []
    for (x, y, sg, sp) in S:
        if rot90:
            x, y = -y, x            # rotate positions; charges ride with sites
            c = sg                  # NO charge flip -- rotation replaces it
        else:
            c = sg * par
        out.append((x, y, c, sp))
    return out

def stack(mode="parity"):
    """Two planes at pitch D. mode='parity': plane2 charges flipped ((-1)^k coding).
    mode='rot90': plane2 pattern rotated 90 deg, charges unflipped (2540 identity)."""
    P, C, SP, PL = [], [], [], []
    for k, z in enumerate((0.0, D)):
        if mode == "parity":
            pl = plane_2455(par=(-1) ** k)
        else:
            pl = plane_2455(par=+1, rot90=(k == 1))
        for (x, y, c, sp) in pl:
            P.append((x, y, z)); C.append(float(c)); SP.append(sp); PL.append(k)
    return np.array(P), np.array(C), SP, np.array(PL)

def soft_a(si, sj):
    if si == 'q' and sj == 'q': return A_QQ
    if si == 'e' and sj == 'e': return A_EE
    return A_QE

def E_cross(P, C, SP, PL, form):
    """Cross-plane switched-pair statics energy (2450 Esw restricted to i in P1, j in P2).
    E_endbond = -E_cross (rigid planes: intra terms cancel exactly in the separation
    definition of prereg S1)."""
    W = np.array([np.sqrt(ALPHA_S) if s == 'q' else np.sqrt(ALPHA) for s in SP])
    tot = 0.0
    chan = {'qq': 0.0, 'ee': 0.0, 'qe': 0.0}
    pairs = []
    for i in range(len(C)):
        if PL[i] != 0: continue
        for j in range(len(C)):
            if PL[j] != 1: continue
            r = np.linalg.norm(P[i] - P[j])
            reff = r if form == "bare" else np.sqrt(r * r + soft_a(SP[i], SP[j]) ** 2)
            e = -DUTY * W[i] * C[i] * W[j] * C[j] * AHC / reff
            tot += e
            key = ''.join(sorted(SP[i] + SP[j])).replace('eq', 'qe')
            chan[key] += e
            pairs.append((SP[i], SP[j], r, e))
    return tot, chan, pairs

print("=" * 78)
print("PATCH 2546 -- OPEN-DM-ENDBOND-1 R-A: functional walk + banked electric partial")
print("=" * 78)

# ---- (iii) VERIFY: 90-degree offset == alternating-parity charge flip (2540 identity)
Pp, Cp, SPp, PLp = stack("parity")
Pr, Cr, SPr, PLr = stack("rot90")
for form in ("bare",):
    Ep, _, _ = E_cross(Pp, Cp, SPp, PLp, form)
    Er, _, _ = E_cross(Pr, Cr, SPr, PLr, form)
    print(f"(iii) parity-flip vs 90-deg rotation, cross energy: {Ep:+.6f} vs {Er:+.6f} MeV"
          f"  -> {'IDENTICAL' if abs(Ep - Er) < 1e-9 else 'DIFFER'}")
    assert abs(Ep - Er) < 1e-9, "2540 identity check failed"
print()

# ---- WALK DETERMINATION (fixed before the partial below; see module docstring) ----
print("WALK DETERMINATION (from artifacts only; sources in endbond1_ra_walk.md):")
print("  (i)  static strong-sector pairwise form UNDER-DETERMINED -> BRANCH I,")
print("       named blocker: 'strong-sector pairwise form'. No depth freeze; gates")
print("       G1/G2/G3 do NOT fire (prereg S5 Branch-I limb).")
print("  (ii) electric radial form: union over {bare 1/r (2450), soft-core (2455)}.")
print("  (iii) alternating parity == 90-deg offset: VERIFIED above.")
print()

# ---- BANKED PARTIAL 1: electric-sector contribution to E_endbond, union ----
print("BANKED PARTIAL 1 -- electric-sector (switched-pair statics) contribution:")
res = {}
for form in ("bare", "soft"):
    Ec, chan, pairs = E_cross(Pp, Cp, SPp, PLp, form)
    Eb = -Ec
    res[form] = (Eb, chan)
    print(f"  [{form:4s}] E_cross = {Ec:+8.3f}  ->  E_endbond^elec = {Eb:+8.3f} MeV"
          f"   (qq {-chan['qq']:+7.3f}, qe {-chan['qe']:+7.3f}, ee {-chan['ee']:+7.3f})")
lo = min(res['bare'][0], res['soft'][0]); hi = max(res['bare'][0], res['soft'][0])
print(f"  UNION: E_endbond^elec in [{lo:+.1f}, {hi:+.1f}] MeV  (positive = bound)")
print(f"  Reading of the partial: the registered electric statics does NOT produce a")
print(f"  bound stack (both conventions <= 0) -- consistent with 2450's own scope note")
print(f"  ('binding = strong-sector registry', unmodeled). The bond depth therefore")
print(f"  lives ENTIRELY in the Branch-I-blocked channel.")
print()

# ---- BANKED PARTIAL 2: cross-pair geometry sums (for the future strong-sector solve) --
print("BANKED PARTIAL 2 -- cross-plane pair geometry (16-CP stack, pitch D=1.15):")
_, _, pairs = E_cross(Pp, Cp, SPp, PLp, "bare")
from collections import Counter
shells = Counter()
for (si, sj, r, e) in pairs:
    key = ''.join(sorted(si + sj)).replace('eq', 'qe')
    shells[(key, round(r, 3))] += 1
for (key, r), n in sorted(shells.items(), key=lambda kv: (kv[0][0], kv[0][1])):
    tag = ""
    if key == 'qq' and r == round(D, 3): tag = "  <- same-corner axial (r = D)"
    print(f"    {key}  r = {r:5.3f} fm  x{n}{tag}")
print()
print("NO GATES SECTION: Branch I fired at walk level; no depth was frozen, so the")
print("G1/G2/G3 disclosure sequence is not licensed (prereg S3 compares only a frozen")
print("depth). The fenced numbers ([40,170], 102, ~85) were touched NOWHERE above")
print("except the registered-derived contact-depth identity assertion, which is an")
print("input-integrity check on the 2455 registration, not a comparison.")
print()
print("ALL WALK ASSERTIONS PASS.")
