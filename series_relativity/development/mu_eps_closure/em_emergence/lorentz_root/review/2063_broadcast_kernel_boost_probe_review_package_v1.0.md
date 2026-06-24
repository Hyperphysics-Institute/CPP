# Review Package v1.0 — Round-3 probe: does the A3′ retarded broadcast carry the boost?

**Artifact:** Round-3 finding of the exact-emergent-Lorentz root campaign (Patch 2063), CPP series_relativity.
**Self-contained:** everything needed to review is inline (context, claim chain, triage, verify code in
full, response format). Fetch nothing. **Find YOUR steer in §6.**
**This is a FINDING under review, NOT a registered theorem.** No THEO / status move made; the panel verdict
decides whether the stated world-call shift is sound before anything is recorded.

---

## §0. Cold-start context

CPP derives Standard-Model structure from a discrete 600-cell lattice (120 vertices, coordination z = 12,
icosahedral point group). Conscious Points execute Perceive→Compute→Displace (PCD) once per universal
Absolute Moment (tick t_P). The **root campaign** asks whether the PCD dynamics admit an **exact continuous
SO⁺(3,1)** action on the emergent fields, at a continuum of velocities and all directions, with no lattice
drag / no lattice-Cherenkov. Three worlds: **W1** exact-discrete (the prize); **W2** exact only in the
block-spin continuum limit, Planck-suppressed floor; **W3** genuine obstruction (real preferred frame).

**Round 2 (already panel-closed SOUND)** showed the *static* PCD budget partition
l_P² = (c·Δτ)² + |d_spatial|² is positive-definite (Euclidean), so its "boost" is a **compact** rotation
(generator M, M² = −I) — the static-geometric quaternion bridge is dead. The panel-endorsed relocation: the
Minkowski (−) sign, if any, must come from the **causal** structure (the retarded A3′ broadcast), and the
identity ds² = (c·t_P)² − |d_spatial|² is **bookkeeping until the broadcast is shown to dynamically enforce
the cone**.

**Round 3 (this artifact)** runs that test: build the boost from the A3′ broadcast kernel and re-run the
three diagnostics.

## §1. The claim being reviewed (one paragraph)

**Claim.** The causal route carries the boost. (A) The A3′ broadcast propagates at a fixed **speed** c
(axiom A3: c = l_P/t_P) on a **retarded** light-cone (C4: h^TT ∝ Q̈(t_ret)), and its continuum limit is the
wave operator □ (C3). The boost that preserves a fixed *speed* (cone slope) is the **non-compact**
hyperbolic Lorentz boost (generator N, N² = +I, β = tanh η), giving relativistic addition
(β₁+β₂)/(1+β₁β₂) — the exact inverse of Round 2's compact result. The conceptual key: the broadcast's
invariant is a fixed **speed**, not a fixed **length**; the same Absolute Moment supplies both l_P and
c = l_P/t_P, and the boost-relevant invariant is the speed. This **resolves the Round-2 T3 caveat**: the
broadcast dynamically enforces the cone, so the − sign is physical, not bookkeeping. (B) With the continuum
limit Lorentz-invariant, the remaining **W1-vs-W2** question collapses to one quantity — **discrete
dispersion isotropy** (is ω(k) = c|k| exact at finite a, all directions?). 1D at Courant 1 is exact
(single-axis); generic cubic lattices are anisotropic ∝ q² (→ W2); the 600-cell's icosahedral z = 12 shell
is anisotropic ∝ **q⁴** (~10²–10³× smaller, because icosahedral symmetry has no degree-4 anisotropic
invariant). **Scope:** "carries the boost" is established **in the continuum limit** (W2 secured, modulo
OPEN-SR-9); W1 (exact-discrete) is **open** and needs the full nested PSR shell-sum to cancel the residual
q⁴ exactly. Net world-call effect (informal, committed call at Round 15): **W3 strongly disfavoured, W2
secured floor, W1 the open upside.**

## §2. The claim chain (what to scrutinize)

**S1 — the broadcast invariant is a fixed SPEED.** Corpus A3: broadcast propagates at c = l_P/t_P. A3′ C3:
the icosahedral PSR shell-sum's continuum limit is □Q = S (wave at exactly c). A3′ C4: retarded far field
h^TT = (2G/c⁴r) Q̈^TT(t_ret). So the broadcast is a finite-speed retarded propagator; its invariant is the
cone slope c, not a budget length.

**S2 — fixed-speed ⇒ non-compact boost (Part A).** By Einstein's constancy-of-c argument, the frame
transformations preserving a fixed signal speed c are the hyperbolic boosts L(η) = exp(ηN), N² = +I. They
fix the null cone (1, ±1) (eigenvalues e^{±η}) and compose by rapidity addition → β₃ = (β₁+β₂)/(1+β₁β₂)
(< 1 always, monotone). Inverse of Round 2's circle-preserving M (M² = −I, β₃ = sin-addition, reached c at
finite β). *Resolves Round-2 T3:* the broadcast's retarded speed-c dynamics enforce the cone — the − sign
is dynamical, not an algebraic rewrite.

**S3 — the W1-vs-W2 fork = discrete dispersion isotropy (Part B).** Continuum limit is Lorentz-invariant
(C3), so exactness-at-finite-a ⟺ discrete ω(k) exactly linear+isotropic, all n̂.
 (a) 1D leapfrog at Courant cΔt = a: ω = ck exactly (verified to 5×10⁻¹⁵) — single-axis exact; the
     obstruction is all-direction isotropy.
 (b) cubic z = 6: fractional phase-speed anisotropy ∝ q², no Courant fix → generic W2.
 (c) icosahedral z = 12 (the 600-cell coordination shell): anisotropy ∝ q⁴, ~10²–10³× smaller. Group
     theory: icosahedral group has no degree-4 anisotropic invariant (lowest harmonic l = 6) vs cubic l = 4.

**S4 — honest scope.** Even icosahedral nearest-neighbour is q⁴-anisotropic, NOT zero → the toy realizes W2
with a tiny floor, not W1. W1 needs the **full** nested PSR shell-sum to cancel the residual exactly —
unproven (Round-4 target). The 600-cell makes W1 uniquely favourable, not automatic.

**S5 — world-call effect + forward grounding.** W3 (real O(1) preferred frame) strongly disfavoured (the
continuum limit IS Lorentz-invariant; the boost is genuinely hyperbolic). W2 the secured floor (modulo
OPEN-SR-9, the from-substrate c_photon derivation). W1 open with a favourable mechanism. The dispersion-
isotropy decider (Round 4) is identically R2 premise (i)/(ii) (c_photon scalar, not anisotropic f(C,Σ)) and
OPEN-SR-9 — so closing it grounds those corpus items.

## §3. Triage — press these hardest

- **T1 (Part A non-circularity).** Is S2 a *derivation* ("the broadcast fixes a speed; transforms
  preserving that speed are boosts") or a disguised assumption ("assume Minkowski, get Minkowski")? Is the
  input (corpus fixed-speed broadcast) genuinely independent of the output (hyperbolic boost)?
- **T2 (scope / overclaim).** Is "carries the boost" correctly confined to the **continuum limit** (W2),
  and W1 kept explicitly open? Flag any sentence that lets Round 3 read as establishing exact Lorentz.
- **T3 (the W1-vs-W2 reduction).** Is "exact-discrete ⟺ discrete dispersion isotropy" the **correct and
  complete** characterization of W1? Could the discrete broadcast fail (or achieve) exact Lorentz for a
  reason *other* than dispersion isotropy (e.g. interaction/nonlinear terms, the absolute-frame carriage
  clause C2, boost-induced mode mixing among Φ/V/Q)?
- **T4 (the dispersion numerics + group theory).** Is the cubic-q² / icosahedral-q⁴ result correct, and is
  the group-theory claim (no degree-4 icosahedral invariant; lowest harmonic l = 6) right? Crucially: is
  the **nearest-neighbour** z = 12 toy representative of the **full** PSR shell-sum, or could additional
  shells change the scaling (better → toward W1, or worse)?
- **T5 (corpus reading).** Is leaning on C3 ("continuum limit □Q = S") for "W2 secured" legitimate, given
  C3 is an axiom *clause* (asserted, the from-substrate derivation being OPEN-SR-9)? Is "W2
  secured-modulo-OPEN-SR-9" the honest statement, or is even W2 less secure than claimed?

## §4. What a verdict-flipping objection looks like

(a) Part A is circular (S2 assumes the answer) ⇒ the causal route does NOT demonstrably carry the boost; or
(b) the W1-vs-W2 reduction is wrong/incomplete (exact Lorentz hinges on something other than dispersion
isotropy) ⇒ Round 3 mislocates the remaining question; or (c) the scope is overclaimed (Round 3 read as
establishing exact Lorentz, or W3 dismissed too strongly). Anything else = calibration.

## §5. Verification tiers (PD-002) — label every claim

INSPECTED — read and judged sound. INDEPENDENTLY RECOMPUTED — re-derived the algebra/group theory/dispersion
yourself. SCRIPT-EXECUTED — ran the §7 code and report its output.

## §6. Read YOUR row (reviewer-specific steer)

- **ChatGPT** — press **T1 (non-circularity)**, T2 (scope), T5 (corpus reading) hardest. Verdict-honesty:
  is "W3 strongly disfavoured / W2 secured-modulo-OPEN-SR-9 / W1 open" defensible or inflated?
  *Disambiguation rider: this is the CPP relativity programme's exact-Lorentz root probe (Round 3); NOT a
  nuclear-physics OPEN-SS audit, NOT a different paper, NOT a memory-reconstruction request — engage the
  inline content directly.*
- **Grok** — run §7 → SCRIPT-EXECUTED; independently recompute the cubic-q² vs icosahedral-q⁴ dispersion
  scaling and the 1D Courant-1 exactness from first principles; verify the icosahedral invariant-degree
  claim. Press **T4**.
- **Copilot** — per-question structural consistency; is the S1→S5 chain valid step-by-step, and is the
  load-bearing step (S2, fixed-speed ⇒ N² = +I) doing the work the conclusion attributes to it? Press
  **T3** (is the W1-vs-W2 reduction complete?).
- **Gemini (optional breadth pass)** — confirmatory/breadth; if you run §7, show output (SCRIPT-EXECUTED
  claims without shown output → RESTATE-tier).

## §7. Verify code (consistency-evidence ONLY — never proof; run it if you can)

```python
import numpy as np
phi=(1+np.sqrt(5))/2

# PART A — broadcast boost is hyperbolic (cone/speed-c preserving), N^2=+I
def boost(eta): return np.array([[np.cosh(eta),np.sinh(eta)],[np.sinh(eta),np.cosh(eta)]])
N=np.array([[0.,1.],[1.,0.]]); M=np.array([[0.,-1.],[1.,0.]])
assert np.allclose(N@N,np.eye(2)) and np.allclose(M@M,-np.eye(2))
print("broadcast N^2=+I (non-compact) ; Round-2 budget M^2=-I (compact)  [OK]")
for eta in [0.3,0.9,2.0]:
    L=boost(eta)
    assert np.allclose((L@np.array([1,1.]))/ (L@np.array([1,1.]))[0],[1,1.])
    assert np.allclose((L@np.array([1,-1.]))/(L@np.array([1,-1.]))[0],[1,-1.])
print("null cone x=+-ct preserved by every boost (the SPEED c is the invariant)  [OK]")
for b in [(0.3,0.4),(0.6,0.6),(0.8,0.8),(2**-0.5,2**-0.5)]:
    e=np.arctanh(b[0])+np.arctanh(b[1]); L=boost(e)
    assert abs(L[1,0]/L[0,0]-(b[0]+b[1])/(1+b[0]*b[1]))<1e-12
    print(f"  b1=b2={b[0]:.6f}: BROADCAST boost b3={(b[0]+b[1])/(1+b[0]*b[1]):.6f}  (relativistic; <1 always)")

# PART B — discrete dispersion: 1D Courant-1 exact; cubic q^2 vs icosahedral q^4 anisotropy
def w1d(k,S=1.,dt=1.,a=1.): return (2/dt)*np.arcsin(np.clip(S*np.sin(k*a/2),-1,1))
ks=np.linspace(1e-3,np.pi*0.999,400)
print(f"(B1) 1D leapfrog Courant=1: max|w/k-1| over band = {np.max(np.abs(w1d(ks)/ks-1)):.2e}  -> EXACT (single-axis)")
def cub():
    d=[]; 
    for i in range(3):
        for s in (1,-1): v=np.zeros(3); v[i]=s; d.append(v)
    return np.array(d)
def ico():
    pts=[]
    for a_,b_ in [(1,phi),(-1,phi),(1,-phi),(-1,-phi)]: pts+=[(0,a_,b_),(a_,b_,0),(b_,0,a_)]
    P=np.array(pts,float); return P/np.linalg.norm(P[0])
def sym(D,k): return np.sum([2*(1-np.cos(k@d)) for d in D])
def aniso(D,q,nd=400,seed=0):
    rng=np.random.default_rng(seed)
    g=rng.standard_normal((200,3)); g/=np.linalg.norm(g,axis=1,keepdims=True)
    c2=np.mean([sym(D,1e-4*u)/1e-8 for u in g])
    u=rng.standard_normal((nd,3)); u/=np.linalg.norm(u,axis=1,keepdims=True)
    v=[np.sqrt(sym(D,q*kh)/c2)/q for kh in u]
    return (max(v)-min(v))/np.mean(v)
print("(B2) phase-speed anisotropy (max-min)/mean at fixed q=|k|a:")
for q in [0.2,0.4,0.8,1.2]:
    ac,ai=aniso(cub(),q),aniso(ico(),q); print(f"   q={q:.2f}: CUBIC={ac:.3e}  ICOSA={ai:.3e}  ratio={ac/ai:.1f}")
qs=np.array([0.1,0.15,0.2,0.3,0.4])
sc=np.polyfit(np.log(qs),np.log([aniso(cub(),q) for q in qs]),1)[0]
si=np.polyfit(np.log(qs),np.log([aniso(ico(),q) for q in qs]),1)[0]
print(f"   scaling: CUBIC ~ q^{sc:.1f} ; ICOSAHEDRAL ~ q^{si:.1f}  (icosahedral isotropic to higher order)")
```
Expected: N²=+I/M²=−I OK; null cone preserved; broadcast composition relativistic (β₁=β₂=0.6 → 0.882);
1D Courant-1 |w/k−1| ≈ 5e−15; cubic ~ q² , icosahedral ~ q⁴ , ratio grows ~10²–10³ as q→0.

## §8. Response format (please use this)

```
REVIEWER: <name>
OVERALL: <SOUND / SOUND-WITH-CALIBRATION / VERDICT-FLIP>
TIER USED: <INSPECTED / INDEPENDENTLY RECOMPUTED / SCRIPT-EXECUTED>
T1 Part-A non-circularity   : <assessment>
T2 scope / overclaim        : <assessment — quote any overreaching sentence>
T3 W1-vs-W2 reduction        : <is dispersion isotropy the complete characterization of W1?>
T4 dispersion + group theory : <cubic q² / icosahedral q⁴ ; is the nn toy representative of full shell-sum?>
T5 corpus reading (C3/OPEN-SR-9): <is "W2 secured-modulo-OPEN-SR-9" honest?>
STRONGEST OBJECTION: <the single most load-bearing problem, if any>
WORLD-CALL LANGUAGE: <defensible / inflated — and why>
OTHER NOTES: <calibration items for v1.1>
```

---

*Package authored by Claude Opus under Thomas Lee Abshier's direction (Patch 2064), exact-Lorentz root
campaign. Companion artifact: `lorentz_root/2063_round3_broadcast_kernel_boost_probe.md`. Responses
aggregate into `lorentz_root/review/reviews-2063.md`.*
