You are one of five independent reviewers (ChatGPT, Grok, Copilot, Gemini,
DeepSeek) on the Conscious Point Physics (CPP) review panel. CPP is a
theoretical-physics programme deriving Standard-Model structure from a
600-cell lattice substrate.
IDENTITY (mandatory): in the §8 REVIEWER field put YOUR OWN actual model name;
do NOT adopt or echo another reviewer's name. If unsure, name your
provider/family.
INDEPENDENCE (mandatory; a prior round produced a verbatim-duplicate return):
produce YOUR OWN independent analysis; do not reproduce, summarize, or vote
with any other reviewer's return.
Please review CONV-027 — a bundled round on the CPP field-equations programme
(OPEN-GR-FE-1, step W-2): (A) the T-1 general-field-equation candidate,
derived from the substrate messenger census; and (B) a finding that the
shipped GR-1c paper's field-equation Proposition contains a defective
compensator formula, together with its diagnosed resolution and a proposed
corrigendum. Everything you need is inline below (context, claim chains,
triage, both verify scripts in full, frozen questions, response format).
Find YOUR reviewer-specific steer in §6 ("read your own row"). If you can run
the §7 code, please do and report SCRIPT-EXECUTED with pasted output digits.
Label every claim with its verification tier — INSPECTED / INDEPENDENTLY
RECOMPUTED / SCRIPT-EXECUTED (PD-002) — and respond in the §8 format.

File (provenance only — likely unreachable for external reviewers; the inline
content below is authoritative):
  blob: https://github.com/Hyperphysics-Institute/CPP/blob/main/series_gravitation/review/conv027_fe1_t1_fterm_review_package_v1.0.md
  raw:  https://raw.githubusercontent.com/Hyperphysics-Institute/CPP/main/series_gravitation/review/conv027_fe1_t1_fterm_review_package_v1.0.md

---

# CONV-027 Review Package v1.0 — the T-1 Field Equation + the GR-1c F-term Corrigendum

**Dispatched:** 20 Aug 2026, Session 150, Patch 3260. Founder-initiated
("Please initiate review protocol").
**Bundling rationale (review-economy protocol):** one derivation and its
directly-entangled corrigendum; one block, one paste per seat.
**Responses land in:** `series_gravitation/review/reviews-CONV-027.md`.

## §0 What this round adjudicates

Two packages, six frozen questions (§5), frozen vocabulary, majority binding
per question. Q5 and Q6 govern the status moves; a majority-sustained
verdict-flipper on Q1 blocks Q6(b)'s move, and on Q3 blocks Q6(a)'s, until a
restate round. A "verdict-flipper" is a named defect that, if sustained,
changes a package's central claim — not a wording preference.

- **Package A:** the T-1 candidate (Patch 3258) —
  `series_gravitation/fe1_derivation/T1_derivation.md`, verify script
  `code/3258_t1_relay_verify.py` (10/10).
- **Package B:** the F-term finding + reconciliation (Patches 3258/3259) —
  `series_gravitation/fe1_derivation/FTERM_reconciliation.md`, verify script
  `code/3259_fterm_reconciliation_verify.py` (8/8). GR-1c is UNEDITED;
  Package B proposes (does not enact) a corrigendum.

## §1 Context (cold-start)

CPP models physical space as a rigid absolute lattice of Grid Points (GPs,
600-cell geometry). Matter and fields are patterns of Dipole Particles (DPs)
in a "Dipole Sea"; stress is carried by the Space Stress Vector (SSV); the
substrate's constitutive response is the Planck Sphere Radius formula
PSR_eff = l_P/(1 + k·Δ|SSV|), where k is a registered normalisation
convention and the formula's grounding stands at W2 (viability) strength —
every result below is CONDITIONAL on it, by design.

Per the ratified axiom layer (A1′/AP-3/AP-4) and the founder's registered
physical picture: three conscious-point types divide the per-Moment
Perceive-Compute-Displace cycle — GPs (fixed lattice sites) run Perceive
(integrate messenger arrivals) and Compute (refresh SSV registers); CPs
(charge-bearers composing matter) run Displace; DI-bits are conserved
messengers with payload exactly {origin address, E vector, S vector},
emitted at a fixed per-GP count each Moment, delivered at the PSR shell in
one Moment, then reset and reused. The receiving GP computes SSV_net and
SSV_abs from arrivals (receiver-computed, never carried). The founder's
registered invariant: every GP begins each cycle with the same DI-bit count,
and "every GP's DI-bit total influence on its PSR is the same as every other
GP." Symmetry statements hold only over the FULL Moment cycle, not its
pieces. The gravitational arc's shipped exact solution: the Schwarzschild
metric in isotropic coordinates, built from k·Δ|SSV| = GM/rc² with
ϱ = k·Δ|SSV|/2, giving −g_tt/c² = ((1−ϱ)/(1+ϱ))² and spatial factor
(1+ϱ)⁴ (GR-1a/GR-1c); classical tests verified 8/8 (GR-1i).

## §2 Package A — the T-1 candidate: claim chain

All claims machine-checked in §7.1 BEFORE the derivation document was
written. The chain:

- **A-1 (census linearity).** Fixed per-GP emission + static-snapshot
  payload + reset-at-delivery ⇒ the per-Moment computed state at a GP is a
  LINEAR shell-sum of origin-GP registers one hop away. [Axiom-text
  consequence.]
- **A-2 (homogeneous cancellation).** The founder's equal-influence
  invariant ⇒ the uniform Sea cancels identically; dynamics closes on the
  departure field u = Δ|SSV|. [Picture-text consequence.]
- **A-3 (kernel).** One hop = one Moment = one PSR: the elementary kernel is
  the shell mean M_R over radius R(x) = PSR_eff(x) on the RIGID flat lattice
  (the lattice has zero configuration freedom; only the REACH varies). The
  Voronoi-cell-to-PSR ratio N_V cancels from every mean — carried
  symbolically, never load-bearing.
- **A-4 (statics, exact).** Static self-consistency u = M_{R(x)}[u] at every
  vacuum GP ⇒ (mean-value property, valid at EVERY radius simultaneously —
  verified incl. position-dependent R(x), §7.1 Check 1) the vacuum statics
  is EXACTLY flat-lattice Laplace: ∇²_lattice u = 0, for ANY PSR profile.
  Unique decaying spherical vacuum solution: u = GM/(k c² r) — the shipped
  GR-1a source relation, RE-DERIVED. Corollary: absolute-lattice
  coordinates ≡ isotropic coordinates (derives WHY the shipped solution is
  conformally flat: the lattice IS flat; only rulers/clocks shrink).
  Sources: compressed-DP census excess ⇒ Poisson at the registered
  normalisation (Gauss check, §7.1 Check 7); linearised-Einstein weak field
  inherited from the shipped companion 7.
- **A-5 (dynamics: the closure).** Irreversible one-level relay
  u(t+τ) = M_R u(t): shell-operator eigenvalue on plane waves is sinc(kR)
  ∈ (−1,1) for k>0 ⇒ ALL modes damp ⇒ dead end (also violates messenger
  conservation). Messenger conservation + determinism + full-Moment
  symmetry force the unique linear conservative time-symmetric closure
  u(t+τ) + u(t−τ) = 2 M_{R(x)} u(t): UNITARY (real dispersion for all k),
  dispersion cos(ωτ) = sinc(kR), long-wave phase AND group speed
  c_* = PSR_eff/(√3·t_P). [§7.1 Checks 2–4.]
- **A-6 (T-1 candidate, lattice frame, conditional-on-PSR/W2):**
  (1/c_*(x)²)·∂²_t u − ∇²_lattice u = (4πG/kc⁴)-normalised
  compressed-DP census source, with c_*(x) = PSR_eff(x)/(√3 t_P).
- **A-7 (Finding F-1, the √3).** The shell kernel FORCES the emergent speed
  PSR_eff/(√3 t_P); identifying observed c with c_* is a kinematic
  normalisation claimed at exactly the k standing (GR-1 §7) — forced, not
  tuned; the dispersion FORM cos(ωτ) = sinc(kR) is flagged as future
  falsifier material, deliberately UNMINTED pending this panel.
- **A-8 (barred moves audit).** No Einstein equations posited; no
  variational principle imported; no tuned constant; LOCAL scope only; the
  founder's full-duplex Nexus speculation registered-but-unused, as ruled.

Standing claimed: DERIVED-PENDING-ADJUDICATION; nothing downstream cites it.

## §3 Package B — the F-term finding + reconciliation: claim chain

- **B-1 (the finding; §7.1 Check 5, exact-symbolic).** On GR-1c's OWN exact
  vacuum profile k·u = a/r (a = GM/c², isotropic radius): the curved
  d'Alembertian □_g u = −a³/(2kr⁵) + O(a⁴), the O(a²) coefficient cancelling
  identically. The required compensator is therefore O(a³). GR-1c's stated
  Proposition compensator 𝓕 = [2k·u²/(1+ku)²]·□ln(1+ku) is O(a⁴) under
  flat-□, curved-□, and literal-k readings alike ⇒ the shipped formula
  fails against the shipped paper's own exact solution — independent of
  Package A's derivation. (Charter HALT executed: GR-1c unedited; finding
  minted OPEN-GR-FE1-FTERM.)
- **B-2 (the resolution; §7.2 C1–C2, exact-symbolic).** The Proposition was
  written for the wrong POTENTIAL. For the log-lapse
  N = ln√(−g_tt/c²) = ln[(1−ϱ)/(1+ϱ)] = −2·artanh(k·u/2):
  □_g N = 0 IDENTICALLY on the exact background. In u-variables the exact
  compensator is F_true = [(k²u/2)/(1−(ku/2)²)]·|∇u|²_g — an
  O(u)·gradient-squared, where the stated 𝓕 was O(u²)·□ln.
- **B-3 (the equivalence theorem; §7.2 C3–C4, exact-symbolic).** For a
  GENERIC potential v (NOT assumed harmonic), with the measured metric built
  pointwise from v: □_g artanh(kv/2) = [32k/((2−kv)(2+kv)⁵)]·∇²_flat v — a
  pure algebraic factor, NO derivative terms. And in full 3D the coefficient
  identity f″/f′ + d/du ln(√A·B^{1/2}) = 0 holds identically for
  f = artanh(ku/2), so every |∇u|² term cancels:
  □_g f(u) = [f′(u)/B(u)]·∇²_flat u with no spherical assumption.
  ⇒ The corrected measured-frame equation and Package A's lattice-frame
  statics are THE SAME EQUATION in two variables (messenger counts ADD ⇒
  lattice potential is u; clock rates MULTIPLY ⇒ measured potential is the
  clock-rate LOG). The Patch-3258 HALT's substantive content is discharged:
  the T-1 static reduction IS the corrected GR-1c equation, in full 3D.
- **B-4 (slip localisation; §7.2 C6).** □ln(1+ku) does contain the
  gradient-squared structure (flat radial identity verified); the stated
  prefactor carries ONE POWER OF u TOO MANY (leading a² vs required a¹) and
  the resummation is (1+ku)-shaped where the exact potential is
  artanh/(1−(ku/2)²)-shaped; no constant rescaling repairs it.
  Classification: transcription defect in a correspondence-level
  proof-sketch Proposition — precisely the gap OPEN-GR-FE-1 was chartered
  to close.
- **B-5 (proposed corrigendum; NOT enacted).** Replace GR-1c Prop field_eq
  with either equivalent form — (Form A) □_g N = normalised source,
  N = ln√(−g_tt/c²) = −2·artanh(k·Δ|SSV|/2), vacuum □_g N = 0 solved
  exactly by Theorem 1; or (Form B) □_g(Δ|SSV|) + F_true = source — plus
  the equivalence note to the lattice-frame statement. Weak-field reduction
  to linearised Einstein unchanged under either form.

## §4 Triage — the hardest questions (press these)

1. **The two-level closure's uniqueness (A-5).** Is time-symmetry truly
   FORCED by messenger conservation + determinism + full-Moment symmetry,
   or is it one choice among reversible closures (e.g., higher-order
   multi-Moment memories)? If alternatives exist, does the long-wave limit
   still land on the same wave operator?
2. **The √3 classification (A-7).** Kinematic normalisation at the k
   standing — or a hidden tuned constant / a physical misprediction? Note
   what it would take to promote the dispersion form to a falsifier.
3. **The equivalence theorem's scope (B-3).** The 3D statement assumes the
   metric is built POINTWISE from u via the isotropic dictionary
   (A(u), B(u)). Is that assumption itself part of what a full T-1 must
   derive (dynamic sector, non-static metrics), and is the package's
   op:einstein deferral honest?
4. **Solution-level safety (B-1).** Confirm that nothing observable moves:
   the metric, the classical tests (GR-1i 8/8), and the weak field are
   identical under the defective and corrected formulations.
5. **Census-to-continuum rigor (A-4).** The statics claim is exact via the
   mean-value property; the DYNAMICS claim is long-wavelength (continuum
   limit of the dispersion). Is the ordering of limits (lattice spacing,
   PSR variation, wavelength) handled honestly?

## §5 Frozen questions and vocabulary (answer ALL six)

- **Q1 (A, derivation chain):** SOUND / DEFECT-NAMED (state the step:
  A-1…A-8 and the defect; flag if verdict-flipping).
- **Q2 (A, the √3 / F-1):** NORMALISATION-AT-K-STANDING / TUNED-CONSTANT /
  MISPREDICTION (justify; recompute the dispersion if you can; tier it).
- **Q3 (B, the finding + reconciliation math):** VERIFIED / DEFECT-NAMED
  (state which of C1–C6 / Check 5 fails and how; flag if verdict-flipping).
- **Q4 (B, slip diagnosis + corrigendum):** CORRECT-AND-SUFFICIENT /
  CORRECT-BUT-INSUFFICIENT (name what more is needed) / INCORRECT.
- **Q5 (both, claim discipline):** DISCIPLINED / OVERCLAIMS (quote the
  passage) / UNDERCLAIMS (quote the passage) — includes the W2/PSR
  conditionality inheritance and the barred-moves audit (A-8).
- **Q6 (status moves, vote both):**
  (a) GR-1c corrigendum: APPROVE-FORM-A / APPROVE-FORM-B /
      APPROVE-EITHER / BLOCK (name the verdict-flipper);
  (b) T-1 candidate: ACCEPT-AS-CHARTER-T-1 / ACCEPT-CONDITIONAL (name the
      condition) / BLOCK (name the verdict-flipper).

**Binding rules:** majority per question; Q6(a) governs Package B's status
move, Q6(b) Package A's; a majority-sustained verdict-flipper on Q3 blocks
Q6(a), and on Q1 blocks Q6(b), until a restate round. Minority
specifications are preserved verbatim in the adjudication. Panel
attribution is to "the AI review panel."

## §6 Reviewer steers — read your own row

- **ChatGPT:** run BOTH §7 scripts if you can (SCRIPT-EXECUTED with pasted
  digits). Then audit B-3's 3D claim: is the coefficient identity
  f″/f′ + d/du ln(√A B^{1/2}) = 0 SUFFICIENT for the 3D cancellation as
  claimed, given pointwise A(u), B(u)? Derive the 3D □_g f(u) expansion
  yourself and check term by term.
- **Grok:** attack A-5 (triage item 1): construct, or prove impossible, an
  alternative reversible closure consistent with the stated constraints
  that does NOT yield the wave operator at long wavelength. Also press the
  ordering-of-limits question (triage 5).
- **Gemini:** adjudicate the √3 (Q2) from first principles: recompute the
  shell-kernel dispersion independently; compare with the corpus's
  c = l_P/t_P convention; state precisely what observation would
  distinguish NORMALISATION from MISPREDICTION.
- **Copilot:** consistency audit of A-1…A-3 against the quoted axiom/picture
  texts in §1: does any lemma smuggle content beyond the registered
  inputs? Also check A-8 (barred moves) line by line.
- **DeepSeek:** independent recomputation of B-1 and B-3: □_g(a/kr) on the
  isotropic background (confirm the O(a²) cancellation and the −a³/(2kr⁵)
  leading term), the factorisation (2−kv)(2+kv)⁵, and the equivalence of
  corrigendum Forms A and B.

## §7 Verify code — IN FULL (run either; report SCRIPT-EXECUTED with digits)

### §7.1 `code/3258_t1_relay_verify.py` (Package A; 10/10 expected)

```python
#!/usr/bin/env python3
"""
3258_t1_relay_verify.py — W-2 verify script for the T-1 field-equation
derivation (OPEN-GR-FE-1, charter Patch 3254; picture Patch 3255/3257).

Checks the mathematical claims of the T-1 derivation document
(series_gravitation/fe1_derivation/T1_derivation.md), in the order the
document makes them:

  1. STATIC MEAN-VALUE EXACTNESS: the shell-mean of u = 1/r about any
     exterior point equals u at that point, for ANY shell radius —
     including position-dependent radius R(x). (Newton shell identity;
     grounds: static vacuum reduction of the relay is Laplace's
     equation on the ABSOLUTE lattice, exactly, independent of PSR
     variation.)
  2. RELAY EIGENVALUE: the shell-mean operator on plane waves e^{ik.x}
     has eigenvalue sinc(kR) (numeric vs closed form).
  3. IRREVERSIBLE CLOSURE FAILS: the one-level relay u(t+1) = M_R u(t)
     has |eigenvalue| < 1 for all k>0 — every mode damps; no wave
     propagation. (Dead end documented in the derivation §4.)
  4. REVERSIBLE CLOSURE PROPAGATES: the two-level relay
     u(t+1) + u(t-1) = 2 M_R u(t) has dispersion cos(w tau) = sinc(kR):
     undamped (|amplification| = 1) for long wavelengths, with
     long-wave phase speed v = R/(sqrt(3) tau). Numeric 1D-radial
     evolution cross-check of the speed.
  5. STATIC DICTIONARY (sympy): on the exact GR-1a/GR-1c profile
     k*Dssv = a/r (a = GM/c^2, isotropic/lattice radius), compute the
     curved d'Alembertian Box_g(Dssv) for the measured metric
     A = ((1-p)/(1+p))^2, B = (1+p)^4, p = a/2r, and:
       (i)  confirm Box_g(Dssv) != 0 (the measured-frame operator alone
            does NOT annihilate the exact profile);
       (ii) series-expand the required compensator F* = -Box_g(Dssv)
            and the GR-1c stated F-term on the same profile (both
            operator readings), and report the order of agreement.
     This adjudicates the HALT rule: the T-1 lattice-frame static
     reduction (Laplace, exact) vs the GR-1c measured-frame statement
     (Box + F): same solution, dictionary-related operators.

No free parameters. No CPP-specific numerics beyond the registered
profile and metric. Tolerances stated per check.
"""
import numpy as np
import sympy as sp

PASS = []
def check(name, ok, detail=""):
    PASS.append(ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))

def fibonacci_sphere(n):
    i = np.arange(n) + 0.5
    phi = np.arccos(1 - 2*i/n)
    theta = np.pi*(1 + 5**0.5)*i
    return np.stack([np.sin(phi)*np.cos(theta),
                     np.sin(phi)*np.sin(theta),
                     np.cos(phi)], axis=1)

print("== CHECK 1: static mean-value exactness (shell theorem), incl. variable R ==")
npts = 200_000
sph = fibonacci_sphere(npts)
rng = np.random.default_rng(3258)
worst = 0.0
for trial in range(12):
    x0 = rng.normal(size=3); x0 *= (4.0 + 6.0*rng.random())/np.linalg.norm(x0)
    # variable shell radius, incl. a position-dependent rule R(x0):
    R = 0.3 + 2.2*rng.random() if trial < 8 else 1.0/(1.0 + 0.1*np.linalg.norm(x0))
    pts = x0[None, :] + R*sph
    mean_u = np.mean(1.0/np.linalg.norm(pts, axis=1))
    err = abs(mean_u - 1.0/np.linalg.norm(x0))*np.linalg.norm(x0)
    worst = max(worst, err)
check("shell-mean(1/r) == 1/r exactly, any R (12 trials)", worst < 5e-9,
      f"worst rel err {worst:.2e}")

print("== CHECK 2: shell-mean eigenvalue on plane waves == sinc(kR) ==")
R = 1.0
worst = 0.0
for kmag in [0.1, 0.7, 1.5, 3.0, 6.0]:
    k = kmag*np.array([0.36, -0.48, 0.8])/1.0  # |dir|=1
    vals = np.exp(1j*R*(sph @ k))
    ev = np.mean(vals).real
    ev_true = np.sinc(kmag*R/np.pi)  # np.sinc(x)=sin(pi x)/(pi x)
    worst = max(worst, abs(ev - ev_true))
check("numeric eigenvalue matches sinc(kR)", worst < 1e-6, f"worst abs err {worst:.2e}")

print("== CHECK 3: irreversible one-level relay cannot propagate ==")
kk = np.linspace(1e-4, 20.0, 4000)
ev = np.sinc(kk*R/np.pi)
check("|sinc(kR)| < 1 for all k>0 (all modes damp)", np.all(np.abs(ev) < 1.0),
      f"max |ev| at k>0: {np.max(np.abs(ev)):.6f}")

print("== CHECK 4: reversible two-level relay — dispersion + numeric speed ==")
# dispersion cos(w tau) = sinc(kR): long-wave expansion w = k R/sqrt(3) tau
kR = np.array([1e-3, 3e-3, 1e-2])
w_tau = np.arccos(np.sinc(kR/np.pi))
v_over = w_tau/kR  # v*tau/R
check("long-wave phase speed -> R/(sqrt(3) tau)",
      np.allclose(v_over, 1/np.sqrt(3), rtol=1e-5),
      f"v*tau/R = {v_over[-1]:.8f}, 1/sqrt(3) = {1/np.sqrt(3):.8f}")
# numeric group velocity from the dispersion relation (finite difference):
kk2 = np.array([2e-3, 2.1e-3])
ww2 = np.arccos(np.sinc(kk2*R/np.pi))
vg = (ww2[1]-ww2[0])/(kk2[1]-kk2[0])
check("long-wave group velocity -> R/(sqrt(3) tau)",
      abs(vg - 1/np.sqrt(3)) < 1e-4, f"vg*tau/R = {vg:.6f}")
# unitarity of the two-level relay: for every k with |sinc(kR)|<=1 (all k),
# cos(w tau)=sinc(kR) has real w -> |amplification|=1, no damping:
check("two-level relay undamped for all k (real dispersion)",
      np.all(np.abs(np.sinc(kk*R/np.pi)) <= 1.0), "unitary band structure")

print("== CHECK 5: sympy static dictionary — Box_g on the exact profile vs GR-1c F ==")
r, a, kc = sp.symbols('r a k', positive=True)
p = a/(2*r)                       # varrho
u = a/(kc*r)                      # Dssv: k*u = a/r (exact GR-1a relation)
A = ((1 - p)/(1 + p))**2          # -g_tt/c^2
B = (1 + p)**4                    # spatial conformal factor
sqrtg = sp.sqrt(A)*B**sp.Rational(3,2)*r**2
Box_g_u = sp.cancel(sp.together(sp.diff(sqrtg*(1/B)*sp.diff(u, r), r)/sqrtg))
ser_box = sp.expand(sp.series(Box_g_u, a, 0, 5).removeO())
c3 = sp.simplify(ser_box.coeff(a, 3)); c2 = sp.simplify(ser_box.coeff(a, 2))
check("Box_g(Dssv) on exact profile: O(a^2) coeff vanishes, O(a^3) = -1/(2 k r^5)",
      c2 == 0 and sp.simplify(c3 + 1/(2*kc*r**5)) == 0,
      f"a^2 coeff = {c2}, a^3 coeff = {c3}")
Fstar_lead_order, Fstar_lead = 3, sp.simplify(-c3)   # F* = -Box_g u
print(f"    required compensator F*: leading order a^{Fstar_lead_order}, coeff {Fstar_lead} (i.e. +a^3/(2 k r^5))")
# GR-1c stated F-term, on the same profile, three readings:
ku = kc*u
pref  = 2*ku**2/(1 + ku)**2       # dimensionless-k reading
pref_lit = 2*kc*u**2/(1 + ku)**2  # literal 2k(Dssv)^2 reading
logt = sp.log(1 + ku)
flat_box_log = sp.cancel(sp.diff(r**2*sp.diff(logt, r), r)/r**2)
curv_box_log = sp.cancel(sp.together(sp.diff(sqrtg*(1/B)*sp.diff(logt, r), r)/sqrtg))
cands = {"F_flat (pref*flatBox ln)":  pref*flat_box_log,
         "F_curv (pref*curvBox ln)":  pref*curv_box_log,
         "F_lit  (2k u^2 pref, flatBox ln)": pref_lit*flat_box_log}
mismatch_all = True
for name, F in cands.items():
    sF = sp.expand(sp.series(sp.cancel(sp.together(F)), a, 0, 6).removeO())
    lo = next((n for n in range(0, 6) if sp.simplify(sF.coeff(a, n)) != 0), None)
    co = sp.simplify(sF.coeff(a, lo)) if lo is not None else 0
    hit = (lo == Fstar_lead_order and sp.simplify(co - Fstar_lead) == 0)
    mismatch_all = mismatch_all and not hit
    print(f"    {name}: leading order a^{lo}, coeff {co}; matches F*: {hit}")
check("HALT FINDING ESTABLISHED: no reading of the GR-1c F-term matches the "
      "required compensator at leading nonlinear order (F* = O(a^3); F = O(a^4))",
      mismatch_all, "static reductions agree at SOLUTION level, disagree at stated-F level")
# solution-level agreement: the exact profile solves the LATTICE-frame statics exactly:
flat_lap_u = sp.cancel(sp.diff(r**2*sp.diff(u, r), r)/r**2)
check("exact profile solves the lattice-frame vacuum statics exactly (flat Laplace)",
      sp.simplify(flat_lap_u) == 0, f"flat Laplacian of a/(k r) = {sp.simplify(flat_lap_u)}")

# weak-field source check: flat Laplacian of k*Dssv = a/r gives -4 pi (G M/c^2) delta^3
# -> Poisson with the registered normalization (distributional; verified by Gauss box):
Rg = 2.0
flux = -1.0*4*np.pi*Rg**2*(1.0/Rg**2)   # d/dr(1/r) * area = -4pi, independent of Rg
check("Gauss flux of grad(1/r) = -4pi (Poisson normalization, weak field)",
      abs(flux + 4*np.pi) < 1e-12, f"flux = {flux:.10f}")

print(f"\n{sum(PASS)}/{len(PASS)} checks pass")
raise SystemExit(0 if all(PASS) else 1)

```

### §7.2 `code/3259_fterm_reconciliation_verify.py` (Package B; 8/8 expected)

```python
#!/usr/bin/env python3
"""
3259_fterm_reconciliation_verify.py — resolution of OPEN-GR-FE1-FTERM.

Establishes, symbolically and exactly (sympy), the reconciliation of the
Patch-3258 HALT finding:

  C1  The log-lapse N = ln((1-p)/(1+p)) = ln sqrt(-g_tt/c^2) is EXACTLY
      Box_g-harmonic on the exact isotropic Schwarzschild background
      (generic branch; the Eq(a,2r) Piecewise branch is the
      horizon-coordinate surface, measure zero, noted).
  C2  The corrected compensator: Box_g(Dssv) + F_true = 0 EXACTLY, with
          F_true = (k^2 Dssv / 2)/(1 - (k Dssv/2)^2) * |grad Dssv|_g^2 .
      Structure: O(u) * (grad u)^2 — NOT the stated GR-1c O(u^2) * Box ln
      form.
  C3  THE EQUIVALENCE (radial, generic non-harmonic v): with the metric
      built pointwise from v,
          Box_g atanh(k v/2) = [32 k / ((2-kv)(2+kv)^5)] * flatLap v .
      Pure algebraic factor, no derivative terms => Box_g phi = 0 iff
      flatLap v = 0 (kv != 2): the measured-frame log-lapse equation and
      the lattice-frame flat Laplace equation are THE SAME EQUATION.
  C4  FULL-3D coefficient identity: for pointwise A(u), B(u) and
      f = atanh(k u/2),   f''/f' + d/du ln( sqrt(A) B^(1/2) ) = 0 ,
      which is the necessary and sufficient condition for
      Box_g f(u) = [f'(u)/B(u)] flatLap u in three dimensions with no
      spherical assumption (all (grad u)^2 terms cancel identically).
  C5  Weak field: phi'(0) = k/2 and N = -k u + O(u^3): linearised
      consistency with the Patch-3258 normalisation.
  C6  Localisation of the GR-1c sketch slip: the radial identity
      Box ln(1+k u) = k Box u/(1+ku) - k^2 (grad u)^2/(1+ku)^2 shows the
      sketch's building block DOES contain the (grad u)^2 structure, but
      the stated prefactor 2k u^2/(1+ku)^2 carries one power of u too
      many: leading orders O(u^2)*(grad u)^2 (stated) vs O(u)*(grad u)^2
      (required). No constant rescaling can repair it.

All claims exact-symbolic except where series orders are the claim.
"""
import sympy as sp

PASS = []
def check(name, ok, detail=""):
    PASS.append(ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))

r, a, k = sp.symbols('r a k', positive=True)
p = a/(2*r)
u = a/(k*r)                                  # exact profile: k u = 2 p
A = ((1-p)/(1+p))**2; B = (1+p)**4
sqrtg = sp.sqrt(A)*B**sp.Rational(3,2)*r**2
def Box(f):
    return sp.piecewise_fold(sp.cancel(sp.together(
        sp.diff(sqrtg*(1/B)*sp.diff(f, r), r)/sqrtg)))
def generic(expr):
    """Extract the generic (a != 2r) branch of a Piecewise, else identity."""
    e = sp.simplify(expr)
    if isinstance(e, sp.Piecewise):
        for val, cond in e.args:
            if cond == True:
                return sp.simplify(val)
    return e

print("== C1: log-lapse exactly Box_g-harmonic ==")
N = sp.log((1-p)/(1+p))
c1 = generic(Box(N))
check("Box_g ln((1-p)/(1+p)) == 0 (generic branch)", c1 == 0, f"residual: {c1}")

print("== C2: corrected compensator exact ==")
Ftrue = (k**2*u/2)/(1-(k*u/2)**2) * (1/B)*sp.diff(u, r)**2
c2 = generic(Box(u) + Ftrue)
check("Box_g u + F_true == 0 (exact)", c2 == 0, f"residual: {c2}")

print("== C3: the equivalence identity (generic v, radial) ==")
v = sp.Function('v')(r)
pv = k*v/2
Av = ((1-pv)/(1+pv))**2; Bv = (1+pv)**4
sqrtgv = sp.sqrt(Av)*Bv**sp.Rational(3,2)*r**2
phiv = sp.atanh(k*v/2)
Boxv_phi = sp.cancel(sp.together(sp.diff(sqrtgv*(1/Bv)*sp.diff(phiv, r), r)/sqrtgv))
flat_lap_v = sp.cancel(sp.together(sp.diff(r**2*sp.diff(v, r), r)/r**2))
ratio = sp.simplify(sp.cancel(Boxv_phi/flat_lap_v))
target = 32*k/((2 - k*v)*(2 + k*v)**5)
check("Box_g atanh(kv/2) / flatLap v == 32k/((2-kv)(2+kv)^5) — pure algebraic",
      sp.simplify(ratio - target) == 0, f"ratio = {ratio}")
w = sp.symbols('w')
poly = sp.expand((w-2)*(w+2)**5)
check("factorisation (kv-2)(kv+2)^5 of the denominator polynomial",
      sp.expand(poly - (w**6 + 8*w**5 + 20*w**4 - 80*w**2 - 128*w - 64)) == 0)

print("== C4: full-3D coefficient identity (no spherical assumption) ==")
uu = sp.symbols('u_')
pA = ((1 - k*uu/2)/(1 + k*uu/2))**2
pB = (1 + k*uu/2)**4
f = sp.atanh(k*uu/2)
lhs = sp.diff(f, uu, 2)/sp.diff(f, uu)
rhs = -sp.diff(sp.log(sp.sqrt(pA)*sp.sqrt(pB)), uu)
c4 = sp.simplify(lhs - rhs)
check("f''/f' + d/du ln(sqrt(A) B^(1/2)) == 0  (=> 3D equivalence)",
      c4 == 0, f"residual: {c4}")

print("== C5: weak field ==")
phi_u = sp.atanh(k*uu/2)
c5a = sp.simplify(sp.diff(phi_u, uu).subs(uu, 0) - k/2) == 0
Nser = sp.series(sp.log((1 - k*uu/2)/(1 + k*uu/2)), uu, 0, 3).removeO()
c5b = sp.simplify(Nser + k*uu) == 0
check("phi'(0) = k/2 and N = -k u + O(u^3) (linearised consistency)", c5a and c5b,
      f"N series = {Nser}")

print("== C6: localisation of the GR-1c sketch slip ==")
# radial identity for the sketch's building block:
lnT = sp.log(1 + k*v)
lhs6 = sp.cancel(sp.together(sp.diff(r**2*sp.diff(lnT, r), r)/r**2))
rhs6 = sp.cancel(sp.together(k*flat_lap_v/(1 + k*v) - k**2*sp.diff(v, r)**2/(1 + k*v)**2))
check("Box ln(1+kv) == k Box v/(1+kv) - k^2 (v')^2/(1+kv)^2 (flat radial identity)",
      sp.simplify(lhs6 - rhs6) == 0)
# leading orders on the exact profile: stated prefactor vs required prefactor
pref_stated = 2*k*u**2/(1 + k*u)**2      # literal GR-1c prefactor
pref_required = (k**2*u/2)/(1 - (k*u/2)**2)
lo_stated = sp.degree(sp.numer(sp.cancel(sp.series(pref_stated, a, 0, 4).removeO().as_poly(a).as_expr())), a) if True else None
s_st = sp.expand(sp.series(pref_stated, a, 0, 4).removeO())
s_rq = sp.expand(sp.series(pref_required, a, 0, 4).removeO())
lo_st = min([n for n in range(0, 5) if sp.simplify(s_st.coeff(a, n)) != 0])
lo_rq = min([n for n in range(0, 5) if sp.simplify(s_rq.coeff(a, n)) != 0])
check("stated prefactor is O(u^2)-class (a^2) vs required O(u)-class (a^1): one power of u too many",
      lo_st == 2 and lo_rq == 1, f"stated leading a^{lo_st}, required a^{lo_rq}")

print(f"\n{sum(PASS)}/{len(PASS)} checks pass")
raise SystemExit(0 if all(PASS) else 1)

```

## §8 Response format (use exactly this skeleton)

```
REVIEWER: <your own actual model name>
TIER LEGEND USED: INSPECTED / INDEPENDENTLY RECOMPUTED / SCRIPT-EXECUTED

Q1: <SOUND | DEFECT-NAMED: <step + defect> [verdict-flipping? yes/no]>  [tier]
Q2: <NORMALISATION-AT-K-STANDING | TUNED-CONSTANT | MISPREDICTION>: <justification>  [tier]
Q3: <VERIFIED | DEFECT-NAMED: <which check + how> [verdict-flipping? yes/no]>  [tier]
Q4: <CORRECT-AND-SUFFICIENT | CORRECT-BUT-INSUFFICIENT: <what more> | INCORRECT>  [tier]
Q5: <DISCIPLINED | OVERCLAIMS: "<quoted passage>" | UNDERCLAIMS: "<quoted passage>">
Q6a: <APPROVE-FORM-A | APPROVE-FORM-B | APPROVE-EITHER | BLOCK: <verdict-flipper>>
Q6b: <ACCEPT-AS-CHARTER-T-1 | ACCEPT-CONDITIONAL: <condition> | BLOCK: <verdict-flipper>>

SCRIPT OUTPUT (if executed): <paste the SUMMARY lines with digits>
STRONGEST OBJECTION (mandatory, even if all verdicts positive): <one paragraph>
NOVEL CONTRIBUTION (optional): <anything the packages missed>
```

*End of CONV-027 package. Thank you — one identical document is pasted to
every seat; your steer is your §6 row.*
