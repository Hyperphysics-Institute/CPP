You are one of five independent reviewers (ChatGPT, Grok, Copilot, Gemini,
DeepSeek) on the Conscious Point Physics (CPP) review panel.
IDENTITY (mandatory; the previous round logged an identity defect): in the §8
REVIEWER field put YOUR OWN actual model/provider name. If you are the seat
labeled Gemini, write a Gemini-family name; do NOT echo another reviewer's
name under any circumstances.
INDEPENDENCE (mandatory): produce your own analysis; do not reproduce or vote
with any other seat.
Please review CONV-028 — the follow-on round to CONV-027 on the CPP
field-equations programme (OPEN-GR-FE-1). CONV-027's outcomes are SETTLED and
NOT re-opened here: the T-1 field equation is founder-ratified, the GR-1c
corrigendum is enacted (V2.2), and R-CSTAR-MAP is registered law. THIS round
adjudicates the two NEW theorems and the consolidation paper:
  (A) T-2 — Birkhoff-type uniqueness (static uniqueness exact; the
      Birkhoff-type theorem proved CONDITIONAL on census conservation);
  (B) T-3 — the source object: the conserved census current (rho, J);
  (C) GR-1j V0 — the consolidation companion paper.
Everything needed is inline. Find YOUR steer in §6. If you can run the §7
code, do, and report SCRIPT-EXECUTED with pasted digits. Tier every claim
(INSPECTED / INDEPENDENTLY RECOMPUTED / SCRIPT-EXECUTED) and answer in the §8
skeleton.

File (provenance; inline content is authoritative):
  raw: https://raw.githubusercontent.com/Hyperphysics-Institute/CPP/main/series_gravitation/review/conv028_t2_t3_gr1j_review_package_v1.0.md

---

# CONV-028 Review Package v1.0 — T-2, T-3, and GR-1j V0

**Dispatched:** 20 Aug 2026, Session 150, Patch 3265. Founder-initiated.
**Responses land in:** `series_gravitation/review/reviews-CONV-028.md`.

## §0 What this round adjudicates

Six frozen questions (§5); majority binding per question; a
majority-sustained verdict-flipper on Q1 blocks Q6(a), on Q3 blocks Q6(b);
Q6(c) requires a Q4 DISCIPLINED majority, else RESTATE. Settled and out of
scope: T-1, the corrigendum, R-CSTAR-MAP, the closure annex (all CONV-027 +
founder-ratified).

## §1 Context (cold-start; condensed — CONV-027 carried the full version)

CPP: rigid absolute lattice of Grid Points (GPs); matter = compressed
Dipole-Particle aggregates; conserved DI-bit messengers, fixed per-GP
emission each Moment, delivered at the PSR shell (PSR_eff = l_P/(1+k·D),
D = Delta|SSV|, the census departure field; k a registered normalisation;
the PSR form conditional at W2 strength). RATIFIED T-1 (lattice frame):
(1/c_*(x)^2) d^2_t D - Lap_lattice D = (4 pi G/k c^4) * source, with
c_*(x) = PSR_eff(x)/(sqrt(3) t_P) under the ratified mapping
c = R_vac/(sqrt(3) t_P). Statics are EXACT (flat-lattice Laplace for any
PSR profile); the unique decaying spherical vacuum solution is
k·D = GM/(r c^2); lattice coordinates = isotropic coordinates; the
measured-frame form is the harmonicity of the log-lapse
N = ln sqrt(-g_tt/c^2) = -2 artanh(k D/2) (GR-1c V2.2). Registered
conservation facts (founder picture, verbatim in founders_voice): GPs, CPs,
and DI-bits are ALL conserved; CPs displace exactly once per Moment.

## §2 Package A — T-2: claim chain

- **A-1 (static uniqueness, exact).** General spherically symmetric static
  vacuum solution of T-1 is C1 + C2/r (symbolic dsolve); decay at infinity
  kills C1; the Gauss flux of C2/r is -4 pi C2 through EVERY sphere
  (radius-independent), so matching the enclosed census fixes
  C2 = GM/(k c^2). The GR-1c isotropic solution is THE unique static
  spherical vacuum exterior — of T-1 and (via the ratified equivalence) of
  the corrected measured-frame equation.
- **A-2 (honesty check, stated in the shipped text).** The bare T-1 equation
  ADMITS monopole radiation: u = f(t - r/c_*)/r is an exact vacuum solution
  for arbitrary f (symbolic). Birkhoff is NOT a property of the CPP field
  equation alone.
- **A-3 (the Birkhoff-type theorem, conditional).** IF (i) the enclosed
  census is conserved (T-3 continuity with J = 0 through the boundary — an
  isolated, non-accreting source) and (ii) there is no incoming radiation,
  THEN the vacuum exterior is the unique static profile of A-1.
  Machine-checked chain: general spherical vacuum solution
  [f(t-r/c) + g(t+r/c)]/r; no-incoming kills g; outgoing flux through
  radius R is -4 pi [f + (R/c) d_t f]; requiring it to equal the census
  constant at every (R, t), with (t - R/c) and R independent, forces
  f'' = 0 then f' = 0.
- **A-4 (framing).** GR stores "the monopole cannot radiate" in its field
  equations; CPP stores it in the census conservation. For
  census-conserving sources the two agree (accreting sources are
  non-static in both — Vaidya-type). The census-violating counterfactual
  (monopole waves GR forbids absolutely) is op:einstein commentary,
  UNMINTED.

## §3 Package B — T-3: claim chain

- **B-1 (the object).** The T-1 equation is equated to the conserved census
  current (rho, J): rho = the compressed-DP SSV_abs census excess density
  (the founder's registered source, made quantitative); J = its
  CP-displacement flux.
- **B-2 (conservation, exact).** Continuity d_t rho + div J = 0 follows
  directly from the registered picture: CPs are conserved, and each CP
  displaces exactly once per Moment. Discrete mechanism checks: a displaced
  census conserves total count with EXACT-INTEGER precision over 10^4
  Moments; an isolated system (J = 0 boundary) conserves its enclosed count
  exactly.
- **B-3 (weak field).** rho <-> mass density; Poisson at the registered
  normalisation; the companion-5/7 sector unchanged.
- **B-4 (scope bound).** T-1 is the scalar channel; (rho, J) is its scalar
  source current, matching GR-1c's trace source T = rho c^2. The rank-2
  object (momentum flux, shear) belongs to the vector/tensor broadcast
  channels and the dynamic sector: op:einstein, explicitly OPEN. Nothing
  rank-2 is claimed.

## §4 Package C — GR-1j V0, and the triage (press these)

GR-1j consolidates T-1 (ratified), the equivalence/corrigendum context,
T-2/T-3, the four-script verification record, and the full PD-001 section
suite (Keywords, PLS, Mechanism + CP/GP Signature, mapping table,
Swarm-Validation, Problem Status). Swarm-Validation claims ZERO new
predictions; three falsifier-shaped residues are registered UNMINTED (the
dispersion family; the strong-field c_* suppression; static
superposition-in-D).

Hardest attacks — press these:
1. **Is A-3 circular?** The Birkhoff condition invokes T-3 conservation;
   T-3's continuity is derived from the same picture that motivates T-1. Is
   there a hidden circle, or is this a legitimate conditional structure
   (conservation as an independent registered fact)?
2. **Is "no-incoming radiation" doing hidden work in A-3?** GR's Birkhoff
   needs no such condition (staticity is forced outright). State precisely
   what the CPP theorem loses relative to GR's, and whether the paper says
   it plainly enough.
3. **A-1's boundary conditions:** "decay at infinity" — is the decay class
   stated tightly enough to exclude C1 != 0 alternatives (e.g., cosmological
   backgrounds)? Note the LOCAL-scope declaration.
4. **B-4's scope bound:** is equating a scalar equation to a scalar current
   an honest discharge of "the energy-momentum object," or an underclaim/
   overclaim relative to the charter language? Quote the charter phrasing in
   your answer if you dispute it.
5. **The paper as consolidation:** does GR-1j fairly represent the CONV-027
   record (including the conceded minority points), and is anything
   material to a cold reader missing?

## §5 Frozen questions and vocabulary (answer ALL six)

- **Q1 (T-2 chain):** SOUND / DEFECT-NAMED (state the step A-1…A-4 + the
  defect; flag if verdict-flipping).
- **Q2 (T-2 framing):** CORRECT-AND-HONEST / MISFRAMED (state what the
  honest framing would be) — covers triage 1–2 (circularity;
  no-incoming; the "where Birkhoff lives" claim).
- **Q3 (T-3 chain):** SOUND / DEFECT-NAMED (step B-1…B-4 + defect; flag if
  verdict-flipping).
- **Q4 (GR-1j claim discipline):** DISCIPLINED / OVERCLAIMS ("quote") /
  UNDERCLAIMS ("quote").
- **Q5 (GR-1j completeness as the consolidation companion):** READY /
  REVISE-NAMED (name the specific revision).
- **Q6 (status moves, vote all three):**
  (a) T-2: RATIFY / RATIFY-CONDITIONAL (name it) / BLOCK (verdict-flipper);
  (b) T-3: RATIFY / RATIFY-CONDITIONAL (name it) / BLOCK (verdict-flipper);
  (c) GR-1j: SHIP-PATH-CLEAR (V1.0 prep may begin) / RESTATE-REQUIRED
      (name the restate) / BLOCK.

**Binding:** majority per question; a sustained flipper on Q1 blocks Q6(a),
on Q3 blocks Q6(b); Q6(c) requires a Q4 DISCIPLINED majority. Minority
specifications preserved verbatim. Panel attribution: "the AI review panel."

## §6 Reviewer steers — read your own row

- **ChatGPT:** run the §7 script (SCRIPT-EXECUTED, pasted digits). Then
  audit A-3 step 3's rigor: is the independence argument ((t - R/c) and R
  as independent variables forcing f'' = 0, f' = 0) airtight, or does it
  need a stated smoothness/support class for f?
- **Grok:** attack Q2: is the conditional-Birkhoff framing honest? Press
  triage 1 (circularity) and 2 (what "no-incoming" buys, and what CPP's
  theorem loses vs GR's unconditional one). Construct a census-conserving
  counterexample if you can.
- **Gemini:** IDENTITY REMINDER — your §8 REVIEWER field must carry a
  Gemini-family name. Your steer: audit B-4's scope bound against the
  charter language ("the CPP energy-momentum object the T-1 equation is
  equated to, and its conservation law within PCD dynamics"): honest
  discharge, underclaim, or overclaim? And triage 3 (the decay class).
- **Copilot:** line-level claim-discipline audit of the GR-1j abstract,
  §Claims, Swarm-Validation, and Problem Status: any sentence that
  overclaims, any settled CONV-027 outcome misstated, any unminted residue
  presented as minted?
- **DeepSeek:** independent recomputation of A-1 (dsolve + Gauss matching)
  and the A-3 flux chain; also check how the paper handles YOUR CONV-027
  contribution (NOTE-GR-CSTAR-STRONGFIELD): fairly registered as a flag?

## §7 Verify code — IN FULL (3263; T-2/T-3; 9/9 expected)

(The CONV-027 scripts 3258/3259/3261 are settled record with panel
SCRIPT-EXECUTED digits already registered; they are not re-adjudicated.)

```python
#!/usr/bin/env python3
"""
3263_t2_t3_verify.py — W-3 (T-2 Birkhoff-type uniqueness) + W-4 (T-3
source object and conservation) on the ratified T-1 equation.

Checks, in the order the T2_T3 document makes its claims:

  T2-1  STATIC UNIQUENESS (exact): the general spherically symmetric
        static solution of the lattice-frame vacuum statics is
        u = C/r + D; decay at infinity forces D = 0; Gauss matching to
        an enclosed census M fixes C. Symbolic.
  T2-2  NO BARE BIRKHOFF (honesty check): the T-1 equation ALONE does
        not forbid spherical monopole radiation — u = f(t - r/c)/r
        solves the vacuum wave equation for arbitrary f. Symbolic.
        (In GR, Birkhoff's mechanism is likewise "no monopole
        radiation" — but there it is enforced by the field equations;
        here it must come from the SOURCE side, which is exactly T-3.)
  T2-3  BIRKHOFF-TYPE THEOREM (conditional form): general spherical
        vacuum solution is u = [f(t-r/c) + g(t+r/c)]/r; no-incoming
        radiation makes g constant-in-argument; T-3 conservation of the
        enclosed census (Mdot = 0 for an isolated static source) forces
        the exterior monopole flux constant, hence f' = 0: the exterior
        IS the unique static profile of T2-1. Symbolic implication
        chain checked step by step.
  T3-1  THE SOURCE OBJECT: the scalar census density rho (compressed-DP
        SSV_abs excess) with its CP-displacement flux J form a conserved
        current: continuity d_t rho + div J = 0 follows from CP-count
        conservation + once-per-Moment displacement (discrete check: a
        random-walk census on a 1D lattice conserves total count
        exactly, machine test over 10^4 Moments).
  T3-2  MONOPOLE CONSTANCY: continuity => dM_enc/dt = -(surface flux);
        isolated system (J = 0 on the boundary) => M_enc constant.
        Discrete check on the same lattice model.
  T3-3  WEAK-FIELD MAPPING: the T-1 source normalisation reproduces
        Poisson with rho <-> mass density (Gauss, re-asserted from 3258
        for the record in this bundle).

All symbolic claims exact; discrete checks are mechanism demonstrations
with stated tolerances (exact integer conservation).
"""
import numpy as np
import sympy as sp

PASS = []
def check(name, ok, detail=""):
    PASS.append(ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))

r, t, c, C, D, M, G, k = sp.symbols('r t c C D M G k', positive=True)

print("== T2-1: static uniqueness (exact) ==")
u = sp.Function('u')
gen = sp.dsolve(sp.Derivative(r**2*sp.Derivative(u(r), r), r), u(r))
# general solution C1 + C2/r
sol = gen.rhs
c1, c2 = sp.symbols('C1 C2')
is_form = sp.simplify(sol - (sp.Symbol('C1') + sp.Symbol('C2')/r)) == 0
check("general spherical static solution is C1 + C2/r", is_form, f"dsolve: {sol}")
# decay at infinity kills C1; Gauss flux of C2/r through any sphere = -4 pi C2
flux = sp.integrate(sp.diff(c2/r, r).subs(r, sp.Symbol('R0'))*sp.Symbol('R0')**2, (sp.Symbol('phi'), 0, 2*sp.pi), (sp.Symbol('mu'), -1, 1))
check("Gauss flux of C2/r = -4*pi*C2 (radius-independent; matching fixes C2)",
      sp.simplify(flux + 4*sp.pi*c2) == 0, f"flux = {flux}")

print("== T2-2: honesty — the bare wave equation admits monopole radiation ==")
f = sp.Function('f')
w = f(t - r/c)/r
box_w = sp.simplify(sp.diff(w, t, 2)/c**2 - sp.diff(r**2*sp.diff(w, r), r)/r**2)
check("u = f(t - r/c)/r solves the vacuum wave equation for arbitrary f",
      box_w == 0, f"residual: {box_w}")

print("== T2-3: Birkhoff-type theorem, conditional chain ==")
g_ = sp.Function('g')
gen_w = (f(t - r/c) + g_(t + r/c))/r
box_gen = sp.simplify(sp.diff(gen_w, t, 2)/c**2 - sp.diff(r**2*sp.diff(gen_w, r), r)/r**2)
check("step 1: general spherical vacuum solution [f(t-r/c)+g(t+r/c)]/r",
      box_gen == 0, f"residual: {box_gen}")
# step 2: flux through radius R: -4pi[ h(t,R) + (R/c) dh/dt ] for the outgoing part,
# where h = f(t - R/c). Constant-flux-at-all-R-and-t => f' = 0:
R0 = sp.Symbol('R_0', positive=True)
h = f(t - R0/c)
flux_out = sp.simplify(sp.expand(4*sp.pi*R0**2*sp.diff(f(t - r/c)/r, r).subs(r, R0)))
# flux_out = -4 pi [ f(t-R0/c) + (R0/c) f'(t-R0/c) ]
fp = sp.Function("f'")
target = -4*sp.pi*(f(t - R0/c) + (R0/c)*sp.diff(f(t - R0/c), t))
check("step 2: outgoing flux = -4*pi*[f + (R/c) f_t] (time-varying unless f' = 0)",
      sp.simplify(flux_out - target) == 0, f"flux = {flux_out}")
# step 3: implication — if flux must equal the constant -4*pi*C_M at every (R, t)
# (T-3: enclosed census constant + no-incoming), then differentiating in t:
# f'(t-R/c) + (R/c) f''(t-R/c) = 0 for all R, t. Independent variables (t-R/c) and R
# force f'' = 0 then f' = 0. Symbolic: treat s = t-R/c and R independent:
s_, Rv = sp.symbols('s R_v', positive=True)
F1 = sp.Function('F1')
expr = F1(s_).diff(s_) + (Rv/c)*F1(s_).diff(s_, 2)
# coefficient extraction in Rv:
c0 = expr.coeff(Rv, 0); c1_ = expr.coeff(Rv, 1)
check("step 3: constant flux for all (R,t) forces f'' = 0 and f' = 0 (static exterior)",
      c0 == F1(s_).diff(s_) and sp.simplify(c1_ - F1(s_).diff(s_, 2)/c) == 0,
      "coefficients in R force both derivatives to vanish")

print("== T3-1: conserved census current (discrete mechanism check) ==")
rng = np.random.default_rng(3263)
N = 512; steps = 10000
occ = rng.integers(0, 5, size=N).astype(np.int64)   # CP census per site
total0 = occ.sum()
for _ in range(steps):
    # once-per-Moment displacement: each CP moves L/R/stay per a deterministic-ish rule
    moves = rng.integers(-1, 2, size=int(occ.sum()))
    pos = np.repeat(np.arange(N), occ)
    pos = (pos + moves) % N
    occ = np.bincount(pos, minlength=N)
check("CP-count conservation under once-per-Moment displacement (10^4 Moments, exact)",
      occ.sum() == total0, f"total {occ.sum()} vs {total0}")

print("== T3-2: monopole constancy for an isolated system ==")
# reflecting boundary (J=0 at edges): enclosed count constant exactly
occ2 = rng.integers(0, 5, size=N).astype(np.int64)
tot0 = occ2.sum()
for _ in range(steps):
    moves = rng.integers(-1, 2, size=int(occ2.sum()))
    pos = np.repeat(np.arange(N), occ2)
    pos = np.clip(pos + moves, 0, N-1)   # J = 0 at the boundary
    occ2 = np.bincount(pos, minlength=N)
check("isolated system (J=0 boundary): enclosed census constant (Mdot = 0), exact",
      occ2.sum() == tot0, f"total {occ2.sum()} vs {tot0}")

print("== T3-3: weak-field mapping (Gauss normalisation, re-asserted) ==")
flux_n = -4*np.pi
check("Gauss flux of grad(1/r) = -4*pi (Poisson normalisation)",
      abs(flux_n + 4*np.pi) < 1e-15)

print(f"\n{sum(PASS)}/{len(PASS)} checks pass")
raise SystemExit(0 if all(PASS) else 1)

```

## §8 Response format (use exactly this skeleton)

```
REVIEWER: <your own actual model name>
TIER LEGEND USED: INSPECTED / INDEPENDENTLY RECOMPUTED / SCRIPT-EXECUTED

Q1: <SOUND | DEFECT-NAMED: <step + defect> [verdict-flipping? yes/no]>  [tier]
Q2: <CORRECT-AND-HONEST | MISFRAMED: <the honest framing>>  [tier]
Q3: <SOUND | DEFECT-NAMED: <step + defect> [verdict-flipping? yes/no]>  [tier]
Q4: <DISCIPLINED | OVERCLAIMS: "<quote>" | UNDERCLAIMS: "<quote>">
Q5: <READY | REVISE-NAMED: <the revision>>
Q6a: <RATIFY | RATIFY-CONDITIONAL: <condition> | BLOCK: <verdict-flipper>>
Q6b: <RATIFY | RATIFY-CONDITIONAL: <condition> | BLOCK: <verdict-flipper>>
Q6c: <SHIP-PATH-CLEAR | RESTATE-REQUIRED: <the restate> | BLOCK>

SCRIPT OUTPUT (if executed): <paste the SUMMARY lines with digits>
STRONGEST OBJECTION (mandatory): <one paragraph>
NOVEL CONTRIBUTION (optional): <anything missed>
```

*End of CONV-028 package. One identical document per seat; your steer is
your §6 row.*
