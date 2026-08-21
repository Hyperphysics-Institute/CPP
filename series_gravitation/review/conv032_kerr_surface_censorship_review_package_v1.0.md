You are one of five independent reviewers (ChatGPT, Grok, Copilot, Gemini,
DeepSeek) on the Conscious Point Physics (CPP) review panel.
IDENTITY (mandatory): in the §8 REVIEWER field put YOUR OWN actual
model/provider name; never echo another seat's name. (Gemini seat: your
last return self-labeled "ChatGPT" — the sixth such event; please state
your own provider name this round.)
INDEPENDENCE (mandatory): your own analysis only.
COUNT-LINE (mandatory): if you execute the script, paste its OWN final
count line VERBATIM ("N/N PASS").
OWN-RUN (mandatory): SCRIPT-EXECUTED means YOUR OWN execution. Quoting
the package's reference run is INSPECTED and must be labeled as such.
DELIVERY NOTE: the verify script is supplied BOTH inline (§7) and as a
separate file `3320_kerr_surface_derivation_verify.py` alongside this
package, so execution-capable seats are not blocked by the Markdown
container (the CONV-031 lesson).
Please review CONV-032 — the Kerr exclusion surface derivation and the
**ergoregion-censorship theorem** (OPEN-GR-RCORE-2(iv), Patch 3320):
conditional on three stated assumptions, the exclusion surface of a
spinning CPP compact object lies strictly OUTSIDE the ergosphere at
every spin and latitude, so the ergoregion instability of horizonless
spinning reflectors — the arc's one viability-class threat — cannot
arise at any spin or reflectivity. **The three assumptions A1–A3 are
the round's designated attack surface**; the mathematics after them is
exact and machine-verified (8/8). Also under review: the
prograde-ring-burial finding (onset χ ≈ 0.55) and the eikonal-grade
GR-2 template inputs (Δt_ret(χ = 0.68) = 2.62 ms, GW150914). Tier
every claim; answer in the §8 skeleton.

File (provenance; inline content authoritative):
  raw: https://raw.githubusercontent.com/Hyperphysics-Institute/CPP/main/series_gravitation/review/conv032_kerr_surface_censorship_review_package_v1.0.md
  script: https://raw.githubusercontent.com/Hyperphysics-Institute/CPP/main/series_gravitation/code/3320_kerr_surface_derivation_verify.py

---

# CONV-032 Review Package v1.0 — The Kerr Exclusion Surface and Ergoregion Censorship

**Dispatched:** 21 Aug 2026, Patch 3321. Founder-authorized ("please
proceed", post-3320).
**Responses land in:** `series_gravitation/review/reviews-CONV-032.md`.
**Settled, out of scope:** T-1 (CHARTER), R-CSTAR-MAP, the log-lapse
dictionary and the static saturation ⟺ lapse-1/3 equivalence (CONV-030
check 2, ratified), F-R1 (the static horizonless reading, ratified and
enacted), |R| = 1 (CONV-030, ratified; its derivation is
spin-independent), GR-1i/GR-1c/GR-1d/GR-1e as amended.
**Under review here:** the Patch-3320 construction (A1–A3), theorem,
finding, and template grade. The 3318 reconnaissance (χ_crit = 2/√7,
scalar-only proxy) is CONTEXT — it is retired by this derivation if the
round confirms.

## §1 Context (cold-start, condensed)

CONV-030 established: CPP compact objects are horizonless, hard-surfaced
bodies; in the static case the exclusion surface (census saturation
k·Δ|SSV| = 1) sits at areal 9M/4 — the Buchdahl radius, lapse exactly
1/3 — via TWO ratified routes (isotropic Schwarzschild form; log-lapse
dictionary N = −2 artanh(kΔ/2)). GR-1h's amended open problems flagged
the ergoregion instability of horizonless spinning perfect reflectors
as LOAD-BEARING: if a spinning CPP object has an exterior ergoregion, a
|R| = 1 surface makes a gain loop with no drain, and rapid spins in the
sky would then falsify the picture. Patch 3318's reconnaissance
(scalar-only proxy: the surface = the Kerr ZAMO-lapse-1/3 locus) found
burial below χ = 2/√7 ≈ 0.756 — safe for merger remnants, exposed above.
The missing physics was the ROTATIONAL census contribution to the
register magnitude. Patch 3320 supplies it.

## §2 The construction: three assumptions (THE ATTACK SURFACE), then exactness

Kerr in Boyer–Lindquist (G = c = M = 1): Δ = r² − 2r + a²,
Σ = r² + a² cos²θ, A = (r² + a²)² − Δ a² sin²θ; ZAMO lapse
α² = ΔΣ/A; frame-drag ω = 2ar/A; proper azimuthal radius ϖ = √g_φφ.

- **A1 (scalar census ≡ lapse dictionary).** Invert the ratified
  dictionary: s ≡ kΔ_scalar = 2(1 − α)/(1 + α). On isotropic
  Schwarzschild this reproduces the ratified linear source relation
  μ/r̄ EXACTLY (script check 0 — symbolic identity, not approximation).
  A1 is the unique lapse-side extension preserving the ratified static
  limit.
- **A2 (vector census ≡ dragging speed).** The rotational SSV
  component's dimensionless register demand is v = ωϖ/α — the local
  dragging speed (velocity of static observers relative to ZAMOs):
  the azimuthal displacement demanded per Moment, in LOCAL REACH
  UNITS — the same units as the scalar demand, so the c-vs-c* ceiling
  question is resolved by construction rather than by choice.
- **A3 (quadrature).** Compression (radial) and circulation
  (azimuthal) are orthogonal demands on the register, so
  |kΔ|² = s² + v². The exclusion surface is the saturation locus
  **F ≡ s² + v² = 1.**

Everything below is exact given A1–A3.

## §3 The theorem and corollary

**Exact engine (script check 2, symbolic on Kerr):**
g_tt = −α²(1 − v²). The ergosphere (g_tt = 0) IS the v = 1 surface,
identically.

**Ergoregion censorship.** On the ergosphere v = 1, so F = s² + 1 > 1
strictly (α < 1 ⇒ s > 0). The census is over-saturated AT the
ergosphere; the saturation surface F = 1 therefore lies strictly
outside it — every spin a ∈ (0, M], every latitude with an ergosphere.
Scan: min F on the ergosphere 1.706; min clearance of the derived
surface over r_E: 0.25 M; extremal (χ = 0.998) equatorial clearance
0.258 M. Physical reading: the ergosphere is where standing still
costs one full reach per Moment azimuthally — the circulation register
alone is full there — so total saturation happens farther out, exactly
as the static floor saturated before the null horizon. **The same
floor that censors the horizon censors the ergoregion.**

**Corollary.** No exterior ergoregion at any spin ⇒ no negative-energy
modes ⇒ **no ergoregion instability, at any spin, at any
reflectivity.** The 3318 χ_crit = 2/√7 is retired as a conservative
scalar-only artifact (quadrature only ADDS census: derived surface ≥
proxy everywhere; χ = 0.68 equator: derived 2.267 M vs proxy 2.052 M
vs ergosphere 2 M). GR-1f's horizon-evaluated Kerr bound relocates to
the exclusion surface as a register-capacity statement.

## §4 Secondary finding: prograde-ring burial (the script's own first run surfaced it)

At χ = 0.68 the prograde equatorial photon ring
(r_ph = 2(1 + cos(⅔ arccos(−a))) ≈ 2.05 M) lies INSIDE the derived
surface (2.267 M); onset χ ≈ 0.55. Consequences registered, not
resolved: the eikonal echo cavity at remnant spins is
RETROGRADE-ring-keyed; Δt_ret(χ = 0.68) = 8.59 GM/c³ = **2.62 ms**
GW150914 (+22% over the Schwarzschild 7.045 GM/c³ = 2.15 ms; the
naively feared (a/M)² ≈ 45% systematic becomes a derived 22%);
f_echo ≈ 380 Hz, in-band; the pro/retro asymmetry is a
CPP-vs-horizon-ECO template discriminator. What buried eikonal rings
mean for finite-ℓ m > 0 barrier modes is OPEN-GR-RCORE-3 (minted:
time-domain Kerr wall spectroscopy on the co-rotating Dirichlet
surface).

## §5 Not claimed / residues

(i) A1–A3 are assumptions, not theorems — this round exists to attack
them. (ii) Eikonal grade only: the finite-ℓ (m, ℓ) Kerr barrier is not
the equatorial ring; hardening = RCORE-3's time-domain solve.
(iii) Zel'dovich SURFACE superradiance (rotating-reflector
amplification without an ergoregion) SURVIVES censorship as a milder
channel — bounded extraction, no known runaway at subcritical surface
speeds; registered, unexplored. (iv) The surface's own co-rotation is
not yet in the template. (v) No growth-time claims anywhere (none
needed: the instability's precondition fails). (vi) No paper edits
until this round + founder ratification.

## §6 Reviewer steers (read your own row)

- **ChatGPT:** verify the engine identity g_tt = −α²(1 − v²) on Kerr
  by hand, and re-derive s = 2(1 − α)/(1 + α) ⇒ μ/r̄ at a = 0. Then
  the round's hardest question: is A3's quadrature the RIGHT
  composition law for register demands, or could a different norm
  (max, L¹, metric-weighted) preserve the a = 0 limit and isotropy
  while changing the theorem? Construct an alternative or argue none
  exists.
- **Grok:** run the script (separate .py supplied) and paste the count
  line verbatim (own run). Physics steer: attack A2 — why the ZAMO
  dragging speed rather than another gravitomagnetic scalar (e.g.,
  ω itself, or B_g magnitude)? Does any defensible alternative UNDO
  censorship?
- **Copilot:** archival seat: verify the quoted CONV-030 dependencies
  (static saturation ⟺ lapse-1/3; F-R1) against the repo records; audit
  that Patches 3318/3320 touch no paper .tex (grade discipline); OWN-RUN
  rules if you execute.
- **Gemini:** constants/limits seat (and please self-identify
  correctly this round): check the numeric claims — r_ph(0.68) pro/ret,
  Δt_ret = 8.59 GM/c³ ⇒ 2.62 ms at 62 M_⊙, f_echo ≈ 380 Hz, the +22%
  statement, and the onset χ ≈ 0.55 — and state what error bars an
  amended template must carry (mass, spin, eikonal grade).
- **DeepSeek:** the falsifier seat: with censorship in place, what
  observation would now falsify the spinning-CPP picture SPECIFICALLY?
  (Candidates to assess: detection of ergoregion-instability GW
  signatures from any BH candidate; echo combs keyed to the PROGRADE
  ring at χ > 0.55; super-quantum... state your own.) Also rule on
  residue (iii): is the Zel'dovich channel correctly graded as
  bounded/milder?
- **All seats:** Q3 asks whether the theorem's strength is suspicious —
  a result this clean invites the worry that A2 was reverse-engineered
  to make the ergosphere special. The paper trail's defense: A2 was
  chosen on the units argument (local reach units, matching the scalar
  demand), and the identity g_tt = −α²(1 − v²) was found afterwards,
  while building check 2. Attack this.

## §7 Verify script

`series_gravitation/code/3320_kerr_surface_derivation_verify.py` —
supplied as a separate file alongside this package AND inline below.
Run if you can (OWN run); paste the final count line verbatim.
Expected: `8/8 PASS`.

```python
#!/usr/bin/env python3
"""
Patch 3320 verify — OPEN-GR-RCORE-2(iv) DERIVATION: the Kerr exclusion
surface from the two-component census, and the ergoregion-censorship
theorem.

Construction (assumptions A1-A3 stated for the panel; everything below
them is exact):
  A1 (scalar census = lapse dictionary): the ratified log-lapse
     dictionary inverts to k*Dssv_scalar = 2(1-alpha)/(1+alpha); on
     Schwarzschild this reproduces the ratified linear source relation
     mu/rbar EXACTLY (check 0), so A1 is the unique extension that
     preserves the ratified static limit.
  A2 (vector census = dragging speed): the rotational SSV component's
     dimensionless register demand is the local dragging speed v --
     the velocity of static observers relative to ZAMOs, v = omega*varpi
     / alpha -- i.e., azimuthal displacement demand per Moment in local
     reach units.
  A3 (quadrature): radial (compression) and azimuthal (circulation)
     register demands are orthogonal, so the total census magnitude is
     |k Dssv|^2 = s^2 + v^2 with s = 2(1-alpha)/(1+alpha).
     Saturation (the exclusion surface): s^2 + v^2 = 1.

Exact GR identity powering the theorem: for stationary axisymmetric
metrics, g_tt = -alpha^2 (1 - v^2), so the ergosphere (g_tt = 0) is
EXACTLY the v = 1 surface (check 2). Hence on the ergosphere
F = s^2 + v^2 = s^2 + 1 > 1 strictly (alpha < 1 there, so s > 0):
the census is already OVER-saturated at the ergosphere, so the
saturation surface lies strictly OUTSIDE it -- at every spin, every
latitude. The ergoregion is censored the way the horizon was.

Checks:
  0. A1 static exactness: 2(1-alpha)/(1+alpha) = mu/rbar on isotropic
     Schwarzschild, symbolically.
  1. a=0 recovery: the F=1 surface is areal r = 9M/4 exactly.
  2. Exact identity g_tt = -alpha^2(1 - v^2) on Kerr (symbolic), hence
     v(r_E, theta) = 1 identically on the ergosphere.
  3. CENSORSHIP: F(r_E, theta) > 1 strictly for a in (0, M], all theta
     with an ergosphere (symbolic inequality via s > 0, + numeric scan).
  4. The derived surface exists and lies strictly outside r_E: numeric
     root-find of F = 1 across a in [0, 0.998], theta in (0, pi/2];
     min clearance reported.
  5. Derived surface vs the 3318 scalar-only proxy: quadrature only ADDS
     census, so the derived surface is at r >= the proxy surface
     everywhere; at chi = 0.68 (equator) report both radii -- the 3318
     chi_crit = 2/sqrt(7) is confirmed as the CONSERVATIVE bound, now
     superseded by censorship at ALL spins.
  6. Extremal margin: at a = 0.998M the equatorial clearance
     r_surf - r_E stays positive; report it.
  7. Echo-delay spin template (Level-A eikonal, equatorial, static-frame
     light travel dt = sqrt(g_rr)/alpha dr): round trip between the
     derived surface and the Kerr equatorial photon rings
     r_ph(pro/retro) = 2M(1 + cos(2/3 arccos(-/+ a/M))). FINDING
     surfaced by the first run: at chi = 0.68 the PROGRADE ring
     (r ~ 2.05 M) lies INSIDE the derived surface (r ~ 2.27 M) -- the
     prograde light ring is itself censored, so no prograde-ring cavity
     exists there; the retrograde ring (r ~ 3.71 M) survives and sets
     the retrograde cavity delay. The check reports the retrograde
     delay, flags prograde burial, and locates the prograde-burial
     onset spin -- all template inputs for GR-2, at eikonal grade.
"""
import numpy as np
import sympy as sp

PASS = []


def check(name, ok, detail=""):
    PASS.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))


# ---------------------------------------------------------------- check 0
rbar, mu = sp.symbols("rbar mu", positive=True)
alpha_schw = (1 - mu / (2 * rbar)) / (1 + mu / (2 * rbar))
s_schw = sp.simplify(2 * (1 - alpha_schw) / (1 + alpha_schw))
check("0. A1 static exactness: 2(1-alpha)/(1+alpha) = mu/rbar on Schwarzschild",
      sp.simplify(s_schw - mu / rbar) == 0, f"s = {s_schw}")

# Kerr in BL, M = 1 symbolic
r_, a_, th_ = sp.symbols("r a theta", positive=True)
Delta = r_**2 - 2 * r_ + a_**2
Sigma = r_**2 + a_**2 * sp.cos(th_) ** 2
A_ = (r_**2 + a_**2) ** 2 - Delta * a_**2 * sp.sin(th_) ** 2
alpha2 = Delta * Sigma / A_
omega = 2 * a_ * r_ / A_
gphph = A_ * sp.sin(th_) ** 2 / Sigma
gtt = -(1 - 2 * r_ / Sigma)
v2 = omega**2 * gphph / alpha2                   # v = omega*varpi/alpha

# ---------------------------------------------------------------- check 1
F_a0 = sp.simplify((2 * (1 - sp.sqrt(alpha2)) / (1 + sp.sqrt(alpha2))) ** 2
                   + v2).subs({a_: 0, th_: sp.pi / 2})
sol = sp.solve(sp.Eq(F_a0, 1), r_)
check("1. a=0 recovery: F=1 surface at areal r = 9M/4",
      any(sp.simplify(x - sp.Rational(9, 4)) == 0 for x in sol),
      f"roots {sol}")

# ---------------------------------------------------------------- check 2
ident = sp.simplify(gtt + alpha2 * (1 - v2))
check("2. exact identity g_tt = -alpha^2 (1 - v^2) on Kerr (=> v=1 on the ergosphere)",
      ident == 0, "g_tt + alpha^2(1-v^2) == 0 identically")

# ---------------------------------------------------------------- check 3
# On the ergosphere v=1, so F = s^2 + 1 with s = 2(1-alpha)/(1+alpha) > 0
# strictly unless alpha = 1 (impossible at finite r). Numeric scan confirms.
def alpha_n(r, a, th):
    D = r * r - 2 * r + a * a
    S = r * r + a * a * np.cos(th) ** 2
    Aa = (r * r + a * a) ** 2 - D * a * a * np.sin(th) ** 2
    return np.sqrt(max(D * S / Aa, 0.0))


def v_n(r, a, th):
    D = r * r - 2 * r + a * a
    S = r * r + a * a * np.cos(th) ** 2
    Aa = (r * r + a * a) ** 2 - D * a * a * np.sin(th) ** 2
    om = 2 * a * r / Aa
    gpp = Aa * np.sin(th) ** 2 / S
    al2 = D * S / Aa
    return om * np.sqrt(gpp / al2) if al2 > 0 else np.inf


def s_n(r, a, th):
    al = alpha_n(r, a, th)
    return 2 * (1 - al) / (1 + al)


def F_n(r, a, th):
    return s_n(r, a, th) ** 2 + v_n(r, a, th) ** 2


def r_E(a, th):
    return 1 + np.sqrt(max(1 - a * a * np.cos(th) ** 2, 0.0))


ths = np.linspace(0.05, np.pi / 2, 120)
cens_ok, minF = True, np.inf
for a in np.linspace(0.05, 1.0, 40):
    for t in ths:
        Fe = F_n(r_E(a, t) * (1 + 1e-12), a, t)
        minF = min(minF, Fe)
        if Fe <= 1:
            cens_ok = False
check("3. CENSORSHIP: F(r_E, theta) > 1 strictly for all spins and latitudes",
      cens_ok, f"min F on the ergosphere over the scan = {minF:.6f} (> 1)")

# ---------------------------------------------------------------- check 4
def r_surface(a, th):
    """Outermost root of F = 1."""
    lo, hi = r_E(a, th) * (1 + 1e-10), 60.0
    if F_n(lo, a, th) <= 1:      # would mean not over-saturated at r_E
        return None
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if F_n(mid, a, th) > 1:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


exist_ok, min_clear = True, np.inf
for a in np.linspace(0.0, 0.998, 30):
    for t in ths:
        rs = r_surface(max(a, 1e-9), t)
        if rs is None:
            exist_ok = False
        else:
            min_clear = min(min_clear, rs - r_E(max(a, 1e-9), t))
check("4. derived surface exists, strictly outside r_E across the scan",
      exist_ok and min_clear > 0, f"min clearance r_surf - r_E = {min_clear:.4f} M")

# ---------------------------------------------------------------- check 5
a68 = 0.68
rs_derived = r_surface(a68, np.pi / 2)


def r_proxy(a, th):
    lo, hi = r_E(a, th) * (1 + 1e-10), 60.0
    f = lambda r: alpha_n(r, a, th) - 1.0 / 3.0
    if f(lo) > 0:
        return None
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if f(mid) > 0:
            hi = mid
        else:
            lo = mid
    return 0.5 * (lo + hi)


rp = r_proxy(a68, np.pi / 2)
mono_ok = True
for a in np.linspace(0.05, 0.74, 15):
    for t in ths[::10]:
        rd_, rp_ = r_surface(a, t), r_proxy(a, t)
        if rp_ is not None and rd_ is not None and rd_ < rp_ - 1e-9:
            mono_ok = False
check("5. derived surface >= scalar-only 3318 proxy everywhere (quadrature adds census); chi=0.68 radii",
      mono_ok and rs_derived is not None and rp is not None and rs_derived >= rp,
      f"chi=0.68 equator: derived r = {rs_derived:.4f} M vs proxy r = {rp:.4f} M "
      f"(vs ergosphere 2 M)")

# ---------------------------------------------------------------- check 6
rs_ext = r_surface(0.998, np.pi / 2)
check("6. extremal margin: at chi=0.998 equatorial clearance stays positive",
      rs_ext is not None and rs_ext - 2.0 > 0,
      f"r_surf = {rs_ext:.4f} M; clearance over the ergosphere = {rs_ext-2:.4f} M")

# ---------------------------------------------------------------- check 7
def r_ph(a, prograde=True):
    sgn = -1 if prograde else +1
    return 2 * (1 + np.cos(2.0 / 3.0 * np.arccos(sgn * a)))


def delay(a, r_in, r_out, n=200_000):
    rs = np.linspace(r_in, r_out, n)
    th = np.pi / 2
    grr = np.array([(r * r + a * a * 0) / (r * r - 2 * r + a * a) for r in rs])
    al = np.array([alpha_n(r, a, th) for r in rs])
    integ = np.sqrt(np.maximum(grr, 0)) / np.maximum(al, 1e-12)
    return 2 * np.trapezoid(integ, rs)


rph_pro, rph_ret = r_ph(a68, True), r_ph(a68, False)
pro_buried = rph_pro <= rs_derived
dt_ret = delay(a68, rs_derived, rph_ret)
dt_schw_num = delay(1e-9, 2.25, 3.0)
dt_schw_exact = 1.5 + 8 * np.log(2)
GM_c3 = 62 * 4.92549e-6
# prograde-burial onset: smallest a where r_ph(pro) = r_surface(a, eq)
a_pb = None
for a in np.linspace(0.01, 0.998, 300):
    rs_ = r_surface(a, np.pi / 2)
    if rs_ is not None and r_ph(a, True) <= rs_:
        a_pb = a
        break
detail7 = (f"Schwarzschild check: numeric {dt_schw_num:.4f} vs exact {dt_schw_exact:.4f}; "
           f"chi=0.68: prograde ring r={rph_pro:.3f} M "
           f"{'BURIED inside the surface' if pro_buried else 'outside'} "
           f"(surface {rs_derived:.3f} M) -- prograde-ring cavity absent; "
           f"retrograde ring r={rph_ret:.3f} M -> Dt_ret={dt_ret:.3f} GM/c^3 "
           f"({dt_ret*GM_c3*1e3:.2f} ms for GW150914) vs Schwarzschild "
           f"{dt_schw_exact:.3f} ({dt_schw_exact*GM_c3*1e3:.2f} ms); "
           f"prograde-burial onset chi ~ {a_pb:.3f}")
check("7. echo-delay spin template (equatorial eikonal): Schwarzschild limit recovered; "
      "chi=0.68 retrograde delay + prograde-ring burial finding",
      abs(dt_schw_num - dt_schw_exact) < 0.01 and dt_ret > 0 and pro_buried
      and a_pb is not None,
      detail7)

print()
print(f"{sum(PASS)}/{len(PASS)} PASS")
raise SystemExit(0 if all(PASS) else 1)
```

Reference run (Patch 3320 environment; quoting it is INSPECTED):

```
[PASS] 0. A1 static exactness: 2(1-alpha)/(1+alpha) = mu/rbar on Schwarzschild — s = mu/rbar
[PASS] 1. a=0 recovery: F=1 surface at areal r = 9M/4 — roots [9/4]
[PASS] 2. exact identity g_tt = -alpha^2 (1 - v^2) on Kerr (=> v=1 on the ergosphere) — g_tt + alpha^2(1-v^2) == 0 identically
[PASS] 3. CENSORSHIP: F(r_E, theta) > 1 strictly for all spins and latitudes — min F on the ergosphere over the scan = 1.706286 (> 1)
[PASS] 4. derived surface exists, strictly outside r_E across the scan — min clearance r_surf - r_E = 0.2500 M
[PASS] 5. derived surface >= scalar-only 3318 proxy everywhere (quadrature adds census); chi=0.68 radii — chi=0.68 equator: derived r = 2.2668 M vs proxy r = 2.0521 M (vs ergosphere 2 M)
[PASS] 6. extremal margin: at chi=0.998 equatorial clearance stays positive — r_surf = 2.2580 M; clearance over the ergosphere = 0.2580 M
[PASS] 7. echo-delay spin template (equatorial eikonal): Schwarzschild limit recovered; chi=0.68 retrograde delay + prograde-ring burial finding — Schwarzschild check: numeric 7.0452 vs exact 7.0452; chi=0.68: prograde ring r=2.050 M BURIED inside the surface (surface 2.267 M) -- prograde-ring cavity absent; retrograde ring r=3.706 M -> Dt_ret=8.592 GM/c^3 (2.62 ms for GW150914) vs Schwarzschild 7.045 (2.15 ms); prograde-burial onset chi ~ 0.555

8/8 PASS
```

## §8 Frozen questions + response skeleton

Answer ALL of Q1–Q7; use the verdict vocabulary given.

- **Q1 (A1).** Is the scalar-census identification SOUND /
  SOUND-WITH-GAPS / UNSOUND? (Note check 0's exactness at a = 0.)
- **Q2 (A2).** Is the dragging-speed identification JUSTIFIED /
  JUSTIFIED-BUT-NOT-UNIQUE (name a defensible alternative and whether
  it undoes censorship) / UNJUSTIFIED?
- **Q3 (A3 + reverse-engineering).** Is quadrature the right
  composition law — SOUND / SOUND-BUT-NOT-UNIQUE (does any alternative
  norm preserving the a = 0 limit undo the theorem?) / UNSOUND? And:
  does the construction survive the reverse-engineering suspicion
  (§6 all-seats steer) — SURVIVES / SUSPECT?
- **Q4 (theorem).** Given A1–A3: is the censorship theorem CORRECT /
  CORRECT-WITH-CAVEATS / INCORRECT? Is the retirement of χ_crit = 2/√7
  WARRANTED?
- **Q5 (finding + template).** Prograde-ring burial (onset ≈ 0.55):
  CONFIRMED / NOT-CONFIRMED? Template grade for GR-2 (Δt_ret = 2.62 ms
  ± mass ± eikonal): ADEQUATE-FOR-DRAFT / NEEDS (name it)?
- **Q6 (falsifiability).** With censorship, what falsifies spinning-CPP
  specifically? Assess the DeepSeek-steer candidates or supply better.
- **Q7 (residues).** OPEN-GR-RCORE-3 + the §5 list: COMPLETE /
  MISSING-ITEMS?

```
REVIEWER: <your own model/provider name>
TIER LEGEND USED: INSPECTED / INDEPENDENTLY RECOMPUTED / SCRIPT-EXECUTED
Q1: <verdict> [<tier>] — <2-6 sentences>
Q2: <verdict> [<tier>] — <2-6 sentences>
Q3: <A3 verdict; SURVIVES/SUSPECT> [<tier>] — <2-6 sentences>
Q4: <verdict; retirement WARRANTED/NOT> [<tier>] — <2-6 sentences>
Q5: <CONFIRMED/NOT; template verdict> [<tier>] — <2-6 sentences>
Q6: <falsifier statement> — <2-6 sentences>
Q7: <COMPLETE/MISSING-ITEMS> — <1-4 sentences>
SCRIPT: <SCRIPT-EXECUTED (own run) + verbatim final count line |
         INSPECTED (reference run) | NOT-EXECUTED + reason>
DEFECTS/OBJECTIONS: <numbered list or NONE>
```
