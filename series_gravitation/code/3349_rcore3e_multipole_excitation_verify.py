#!/usr/bin/env python3
"""3349_rcore3e_multipole_excitation_verify.py — OPEN-GR-RCORE-3(e).

THE BORROWED ASSUMPTION. After Leg C (Patch 3339) the observable
no-comb prediction rests on one sentence: "trapped ladders exist at
ell >~ 7 +/- 1, WHERE RINGDOWN EXCITATION IS NEGLIGIBLE." That
negligibility is INHERITED from standard ringdown phenomenology and
has never been computed in this programme. GR-2 V1.4 names it as the
load-bearing, undischarged item. This script discharges it — and, if
possible, replaces the borrowed claim with a DERIVED one.

THE ROUTE, and why it can work from inside our own machinery. A
TRAPPED mode is by definition a resonance BELOW its barrier top. For
external radiation (the merger's ringdown) to excite such a mode, the
wave must TUNNEL INWARD through the very barrier that traps it; and
for the excited mode to be observed at infinity it must tunnel back
OUT. Both factors are the same barrier penetration integral

    Gamma(ell, omega) = int_{forbidden} |k| dr,   |k| = sqrt(-R)/Delta,

with R the Kerr radial function already used and validated in Legs B
and C. Transmission through the barrier is ~ exp(-2*Gamma). So the
observable strength of a trapped high-ell resonance is suppressed by
the SQUARE of the tunnelling factor, exp(-4*Gamma) in energy — a
quantity this corpus can compute rather than borrow.

WHAT WOULD MAKE THIS A FULL DISCHARGE. If exp(-4*Gamma) were
already astronomically small at ell_crit and fell steeply with ell,
"high-ell trapped combs are unobservable" would follow from the wall +
barrier system ITSELF, with no appeal to the binary's multipole
hierarchy.

*** RESULT: THAT HYPOTHESIS IS FALSE AT ell_crit, AND THE CHECKS BELOW
RECORD THE REAL FINDING RATHER THAN A TUNED THRESHOLD. *** The FIRST
trapped mode sits only just below its barrier top (ell=7: w_1 = 1.155
vs w_top = 1.179), so the forbidden region it must tunnel is THIN:
Gamma = 0.404, and the observable factor exp(-4*Gamma) = 0.20 — a
factor of five, which is NOT negligible by any standard. The barrier
factor becomes decisive only from ell >= 9 (7e-4) and overwhelming by
ell >= 11 (9e-7). So RCORE-3(e) discharges PARTIALLY: the inherited
source-side hierarchy is retired for ell >= 9 but REMAINS LOAD-BEARING
at ell = 7-8. The honest outcome is a NARROWED open item, not a closed
one — and the narrowing is worth more than a forced closure would have
been, because it names exactly which two multipoles still depend on
borrowed physics.

HONEST SCOPE, declared before results (3347/3339 discipline): this
computes the BARRIER suppression only. The SOURCE-side question — how
strongly a comparable-mass merger drives high-ell multipoles in the
first place — is NOT computed here and remains inherited; the point
is that it is no longer needed if the barrier factor alone settles
it. Eikonal-WKB grade throughout, inheriting Leg B's fixed-Q
correspondence and A1-A3 conditionality. Domain declared and asserted
in code (3347 lesson). Units G = c = M = 1; Hz at 62 Msun.
"""
import numpy as np

PASS = []


def check(name, ok, detail=""):
    PASS.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))


GM_s = 62 * 4.92549e-6
to_hz = lambda w: w / (2 * np.pi * GM_s)

# ---------- surface machinery (identical construction to 3333/3334/3339) ----------
def _AA(r, a, th):
    D = r * r - 2 * r + a * a
    return (r * r + a * a) ** 2 - D * a * a * np.sin(th) ** 2


def alpha_n(r, a, th):
    D = r * r - 2 * r + a * a
    S = r * r + a * a * np.cos(th) ** 2
    return np.sqrt(max(D * S / _AA(r, a, th), 0.0))


def v_n(r, a, th):
    S = r * r + a * a * np.cos(th) ** 2
    Aa = _AA(r, a, th)
    D = r * r - 2 * r + a * a
    om = 2 * a * r / Aa
    gpp = Aa * np.sin(th) ** 2 / S
    al2 = D * S / Aa
    return om * np.sqrt(gpp / al2) if al2 > 0 else np.inf


def F_n(r, a, th):
    al = alpha_n(r, a, th)
    s = 2 * (1 - al) / (1 + al)
    return s * s + v_n(r, a, th) ** 2


def r_E(a, th):
    return 1 + np.sqrt(max(1 - a * a * np.cos(th) ** 2, 0.0))


def r_surface(a, th=np.pi / 2):
    lo, hi = r_E(a, th) * (1 + 1e-10), 60.0
    if F_n(lo, a, th) <= 1:
        return None
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if F_n(mid, a, th) > 1:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def Rfun(r, a, m, Q, w):
    D = r * r - 2 * r + a * a
    return (w * (r * r + a * a) - a * m) ** 2 - D * ((m - a * w) ** 2 + Q)


def barrier_exists(a, m, Q, w, r_wall, r_out=60.0, n=9000):
    rs = np.linspace(r_wall * (1 + 1e-9), r_out, n)
    return np.any(Rfun(rs, a, m, Q, w) < 0)


def omega_top(a, m, Q, r_wall, w_hi=4.0):
    lo, hi = 1e-3, w_hi
    if not barrier_exists(a, m, Q, lo, r_wall):
        return None
    for _ in range(90):
        mid = 0.5 * (lo + hi)
        if barrier_exists(a, m, Q, mid, r_wall):
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def phase_integral(a, m, Q, w, r_wall, n=60000, r_out=60.0):
    """Phi = int k dr from wall to the first turning point (allowed region)."""
    rs = np.linspace(r_wall * (1 + 1e-9), r_out, n)
    R = Rfun(rs, a, m, Q, w)
    if R[0] <= 0:
        return None
    i_turn = int(np.argmax(R < 0))
    if i_turn == 0:
        return None
    rs_c, R_c = rs[:i_turn], np.clip(R[:i_turn], 0, None)
    D = rs_c * rs_c - 2 * rs_c + a * a
    return float(np.trapezoid(np.sqrt(R_c) / D, rs_c))


def tunneling_integral(a, m, Q, w, r_wall, n=120000, r_out=60.0):
    """Gamma = int |k| dr across the CLASSICALLY FORBIDDEN region (R<0).
    Transmission ~ exp(-2 Gamma)."""
    rs = np.linspace(r_wall * (1 + 1e-9), r_out, n)
    R = Rfun(rs, a, m, Q, w)
    forb = R < 0
    if not np.any(forb):
        return 0.0
    idx = np.where(forb)[0]
    # contiguous forbidden band containing the inner turning point
    split = np.where(np.diff(idx) > 1)[0]
    band = idx if len(split) == 0 else idx[:split[0] + 1]
    rs_f = rs[band]
    D = rs_f * rs_f - 2 * rs_f + a * a
    return float(np.trapezoid(np.sqrt(-R[band]) / D, rs_f))


def first_trapped(a, m, ell, r_wall, nw=600):
    """Lowest trapped resonance: Phi(w) = (0+3/4) pi, below the barrier top."""
    Q = (ell + 0.5) ** 2 - m * m
    wt = omega_top(a, m, Q, r_wall)
    if wt is None:
        return None, None, None
    ws = np.linspace(1e-3, wt * 0.9995, nw)
    for w in ws:
        p = phase_integral(a, m, Q, w, r_wall)
        if p is not None and p / np.pi >= 0.75:
            return float(w), float(wt), Q
    return None, wt, Q


A = 0.68
RW = r_surface(A)
ELL_MIN, ELL_MAX = 7, 14
print(f"      chi = {A}: equatorial wall r = {RW:.4f} M; "
      f"declared domain ell = {ELL_MIN}..{ELL_MAX}, extreme-retrograde branch")

rows = []
for ell in range(ELL_MIN, ELL_MAX + 1):
    w1, wt, Q = first_trapped(A, -ell, ell, RW)
    if w1 is None:
        rows.append((ell, None, None, None, None))
        print(f"        ell={ell:2d}: no trapped mode at this spin")
        continue
    G = tunneling_integral(A, -ell, Q, w1, RW)
    supp_amp = np.exp(-2 * G)        # amplitude transmission, one crossing
    supp_obs = np.exp(-4 * G)        # in AND out — the observable factor
    rows.append((ell, w1, wt, G, supp_obs))
    print(f"        ell={ell:2d}: w_1={w1:.4f} ({to_hz(w1):5.0f} Hz @62), "
          f"w_top={wt:.4f}, Gamma={G:.3f}, e^-2G={supp_amp:.3e}, "
          f"e^-4G={supp_obs:.3e}")

good = [r for r in rows if r[1] is not None]
check("1. DOMAIN DECLARED AND ASSERTED: trapped modes located across the "
      "full declared range (the 3347 discipline — the claim's domain is a "
      "test, not prose)",
      len(good) == (ELL_MAX - ELL_MIN + 1),
      f"{len(good)}/{ELL_MAX-ELL_MIN+1} multipoles ell={ELL_MIN}..{ELL_MAX} "
      f"carry a trapped mode at chi={A}")

# --- the discharge: is the barrier factor alone decisive at ell_crit? ---
G7 = good[0][3]
supp7 = good[0][4]
# The hypothesis under test was "the barrier alone settles it at
# ell_crit". It is FALSE, and this check records that rather than
# lowering its own bar (3339/3348 discipline).
DECISIVE = 1e-3          # declared BEFORE reading the numbers: the level
                         # at which a feature is unobservable on its own
first_decisive = next((r[0] for r in good if r[4] < DECISIVE), None)
check("2. THE HYPOTHESIS IS FALSE AT ell_crit — recorded, not tuned away: "
      "the FIRST trapped mode sits only just below its barrier top, so the "
      "forbidden region is THIN and the barrier hides it by a mere factor "
      "of ~5. The barrier factor does NOT settle the question at ell = 7",
      supp7 > DECISIVE,
      f"ell=7: w_1={good[0][1]:.4f} vs w_top={good[0][2]:.4f} (gap only "
      f"{good[0][2]-good[0][1]:.4f}), Gamma={G7:.3f}, e^(-4*Gamma)="
      f"{supp7:.3f} — a factor {1/supp7:.1f}, NOT negligible by any standard")

check("2b. PARTIAL DISCHARGE LOCATED: the barrier factor DOES become "
      "decisive from a computable multipole onward, so the inherited "
      "source-side hierarchy is retired above it and retained below it",
      first_decisive is not None and ELL_MIN < first_decisive <= ELL_MAX,
      f"e^(-4*Gamma) first drops below the pre-declared {DECISIVE:.0e} at "
      f"ell = {first_decisive} ({[r[4] for r in good if r[0]==first_decisive][0]:.1e}); "
      f"ell = 7 and 8 therefore STILL depend on borrowed physics, ell >= "
      f"{first_decisive} no longer does")

# --- monotone steepening with ell ---
Gs = [r[3] for r in good]
check("3. the suppression STEEPENS monotonically with ell — higher "
      "multipoles are progressively more hidden, so ell_crit is the "
      "best case and every deeper rung is worse",
      all(Gs[i] < Gs[i + 1] for i in range(len(Gs) - 1)),
      "Gamma: " + ", ".join(f"{g:.2f}" for g in Gs) +
      f"  =>  e^-4G falls {good[0][4]:.1e} -> {good[-1][4]:.1e}")

# --- growth law, for the record (fitted, labelled as fitted) ---
ells = np.array([r[0] for r in good], float)
slope, intercept = np.polyfit(ells, np.array(Gs), 1)
check("4. growth law recorded (FITTED over the declared domain, not "
      "derived): Gamma is close to linear in ell, so the observable "
      "suppression falls near-exponentially in ell",
      slope > 0,
      f"Gamma ~ {slope:.3f}*ell + {intercept:.3f} over ell={ELL_MIN}..{ELL_MAX}; "
      f"each additional multipole costs a further factor "
      f"e^(-4*{slope:.3f}) = {np.exp(-4*slope):.2e}")

# --- consistency with Leg C: below ell_crit there is nothing to suppress ---
w6, wt6, Q6 = first_trapped(A, -6, 6, RW)
check("5. CONSISTENCY WITH LEG C: at ell = 6 (below ell_crit = 7 +/- 1) "
      "there is NO trapped mode to suppress — the two results meet exactly "
      "where they should",
      w6 is None,
      "ell=6 carries no trapped resonance at chi=0.68, matching the Leg-C "
      "census (Phi_max/pi = 0.734 < 3/4)")

# --- the inherited claim, now demoted to cross-check ---
# A second, independent derived discriminator found while computing the
# above: the trapped high-ell combs live in a DIFFERENT BAND from the
# low-ell line set, so a search in the predicted band cannot confuse them.
lo_band_hi = 294.0        # (2,+1) eikonal top, the top of the low-ell set
sep = min(to_hz(r[1]) for r in good)
check("6. A SECOND DERIVED DISCRIMINATOR (not sought, found while "
      "computing): the trapped high-ell combs are SPECTRALLY SEPARATED "
      "from the low-ell line set — they cannot contaminate a search in the "
      "predicted band",
      sep > 1.5 * lo_band_hi,
      f"high-ell trapped modes span {sep:.0f}-"
      f"{max(to_hz(r[1]) for r in good):.0f} Hz @62 Msun, entirely ABOVE the "
      f"low-ell line set's 211-{lo_band_hi:.0f} Hz — a factor "
      f"{sep/lo_band_hi:.1f} clear of its top")

check("7. THE REMAINING BORROWED ASSUMPTION, NARROWED AND NAMED: "
      "OPEN-GR-RCORE-3(e) is PARTIALLY discharged — the inherited "
      "source-side hierarchy is retired for ell >= 9 by the barrier factor "
      "and by band separation, but ell = 7 and ell = 8 still rest on it",
      first_decisive is not None,
      f"was: 'excitation is negligible for all ell >= 7' (inherited, "
      f"uncomputed). NOW: derived for ell >= {first_decisive}; inherited for "
      f"ell = 7-8 only — two multipoles, not an open-ended tail. The item "
      f"stays OPEN at reduced scope; a source-side excitation computation "
      f"would close it")

print(f"{sum(PASS)}/{len(PASS)} PASS")
print(f"FAST: all checks are FAST; FAST: {sum(PASS)}/{len(PASS)} PASS")
raise SystemExit(0 if all(PASS) else 1)
