# CONV-001 review package — Round 5 (Patch 2074): the icosahedral isotropy ceiling determines the world is W2

**Cycle-opening package (v1.0).** Self-contained: inline content is authoritative; GitHub links are
provenance only (likely unreachable for external reviewers — inline is authoritative). This reviews **the
W1-vs-W2 decider** — still a **FINDING, not a THEO**; the standard is *"is the determination (W2) justified
by the group theory actually shown, and is the inference from it sound?"* **No committed world-call rides on
this review — it makes the call ready; the call itself is TLA's.**

**IDENTITY (mandatory):** in §8 put **your own actual model name**; do **not** adopt or echo another
reviewer's name. If unsure, name your provider/family.

**Provenance (optional):**
- Finding (blob): `https://github.com/Hyperphysics-Institute/CPP/blob/main/series_relativity/development/mu_eps_closure/em_emergence/lorentz_root/2074_round5_icosahedral_isotropy_ceiling_W2.md`
- Verify (raw): `https://raw.githubusercontent.com/Hyperphysics-Institute/CPP/main/series_relativity/development/mu_eps_closure/em_emergence/lorentz_root/verify/2074_quasicrystal_isotropy_ceiling.py`

---

## §0. Context

**CPP** derives Standard-Model physics from Conscious Points executing PCD cycles on a 600-cell substrate.
The **exact-emergent-Lorentz root campaign** (OPEN-SR-10) asks whether the PCD dynamics admit an **exact
continuous SO⁺(3,1)** action on the emergent fields. Worlds: **W1** exact-discrete; **W2** exact only in the
continuum/IR limit + Planck floor; **W3** real preferred frame.

**Banked (Rounds 1–4, all panel-closed SOUND):** R2 killed the static-geometric boost (compact, M²=−I). R3:
the causal A3′ broadcast carries the non-compact boost *in the continuum limit*; W1-vs-W2 reduces to
discrete dispersion isotropy. R4: a *periodic* lattice can't be exactly Lorentz (bounded BZ symbol —
theorem-grade for any summable periodic kernel), **but** CPP's substrate is the φ-self-similar nested-600-cell
= an icosahedral **quasicrystal** (aperiodic, no BZ), which evades that periodic no-go. R4 left **one** fork:
does the deterministic quasicrystal reach **exact** isotropy (W1) or only **dense-suppressed** (W2)?

## §1. The claim under review (the decider)

**W2.** A structure with **icosahedral point symmetry** — periodic *or* quasicrystalline — is isotropic only
up to its first anisotropic invariant, which for the icosahedral group is **degree 6** (no l=2, **no l=4**).
So the dispersion is isotropic through rank-4 (**isotropic elasticity**, v_phase isotropic at O(q²)) but the
**rank-6 / l=6** harmonic is a **generic, nonzero q⁴ anisotropy floor**. The quasicrystal inherits it
(aperiodicity removed the *periodic* obstruction, not the *point-symmetry* one). **Exact W1 needs every
anisotropic harmonic to vanish — a continuum, or a statistically-isotropic *random* (causal-set) substrate —
neither of which is CPP's deterministic 600-cell.** ⇒ **W2:** IR-exact Lorentz (isotropic elasticity) + an
l=6/q⁴ floor pushed to ~l_P/10³⁰, unobservably tiny but **nonzero**.

## §2. The S1–S5 chain

- **S1.** Expand D(k)=Σ_x w(|x|)·2(1−cos(k·x)) at small k: the O(k²ⁿ) term is the rank-2n tensor
  Σ_x x_{i₁}…x_{i₂ₙ}. Anisotropy appears at the first rank whose tensor has a non-isotropic part.
- **S2.** Icosahedral anisotropic invariants begin at **degree 6** (then 10, 15, …); **no l=2, no l=4.**
  Verified to machine precision: rank-2 dev 2×10⁻¹⁶, rank-4 dev 3×10⁻¹⁶ (**isotropic** — isotropic
  elasticity), rank-6 dev 9.3×10⁻² (**anisotropic**, l=6), rank-8 anisotropic.
- **S3.** ⇒ v_phase isotropic at O(q²), anisotropy first at **O(q⁴)** (l=6), generic and nonzero. The q⁴ seen
  in Rounds 3–4 *is* this harmonic, not a finite-shell artifact.
- **S4.** The quasicrystal is still only icosahedrally symmetric ⇒ inherits the l=6/q⁴ floor. QC approximant
  v_phase anisotropy ~q⁴ (fitted 4.0), small but nonzero. This **closes W1 at the free-dispersion level**, so
  the Round-4 §4.1 further channels (interactions, mode-mixing, C2, composition) are **moot**.
- **S5.** Exact isotropy ⇒ all harmonics vanish ⇒ continuum or **random** (Poisson/causal-set). Verified:
  Poisson rank-4 & rank-6 deviations → 0 with N. CPP is deterministic, not random ⇒ not that route ⇒ **W2.**

## §3. Triage (attack these)

- **T1 — the group theory (load-bearing).** Is "icosahedral group has no degree-2 and **no degree-4**
  anisotropic invariant; first is degree 6" correct (A₅ / binary-icosahedral representation theory)? Is the
  machine-precision rank-4-isotropic / rank-6-anisotropic result right and correctly read (isotropic
  elasticity at q²; anisotropy at q⁴)?
- **T2 — the inference to W2.** Does the broadcast dispersion **inherit** the substrate's icosahedral
  symmetry, so that W1 fails at the **free-dispersion** level? Is "W1 fails at dispersion ⇒ the §4.1 channels
  are moot for the W1-vs-W2 call" sound?
- **T3 — the deterministic-vs-random dichotomy.** Is "exact isotropy ⇒ continuum or statistically-isotropic
  random (causal-set); deterministic icosahedral ⇒ W2" correct? Is the Poisson→0 demonstration the right
  analog of the causal-set route, and is it right that CPP's *deterministic* substrate does not inherit it?
- **T4 — the loophole.** The finding says W1 is ruled out **modulo** a non-generic accidental vanishing of
  **all** anisotropic harmonics. Is that loophole truly non-generic/unmotivated, or could a CPP dynamical
  symmetry force the l=6 (and higher) coefficients to zero? Is "ruled out modulo a non-generic loophole" the
  right strength (vs over-claiming "W1 impossible" or under-claiming "W1 still open")?
- **T5 — world-call.** Is **W2 committed-call-ready**? Is "W3: periodic channel excluded; strongly
  disfavoured globally, now backed by from-substrate isotropic elasticity (not only C3)" the right strength?
  Is the ~l_P/10³⁰ floor characterization right?

## §4. Verdict-flip criteria

Flip (not calibration) iff: **(a)** the group theory is wrong (icosahedral *does* have a degree-4 anisotropic
invariant, or the degree-6 coefficient vanishes generically); **(b)** the broadcast dispersion does **not**
inherit icosahedral symmetry (so W1 isn't killed at the dispersion level); **(c)** the
deterministic-vs-random dichotomy is wrong (a deterministic icosahedral quasicrystal *can* be exactly
isotropic); **(d)** the accidental-vanishing loophole is actually generic or CPP-motivated (W1 still live).
W2-vs-W3 wording, the floor size, and loophole phrasing are **calibration**.

## §5. Tiers (state which you used — PD-002)

INSPECTED (read the argument/algebra) | INDEPENDENTLY RECOMPUTED (re-derive the icosahedral invariant degrees
0,6,10,15 from A₅ rep theory; or the rank-4-isotropic result) | SCRIPT-EXECUTED (ran §7, report outputs).

## §6. Read your own row (reviewer-specific steer)

**IDENTITY:** put **your own** model name in §8; do not adopt another reviewer's label.

- **ChatGPT —** press **T1** and **T2** hardest. Is the icosahedral no-l=4 / first-l=6 invariant structure
  correct (A₅ rep theory), and is the rank-4-isotropic result the genuine isotropic-elasticity theorem? Does
  the broadcast dispersion inherit icosahedral symmetry so W1 dies at the free-dispersion level? You are the
  rigor anchor on whether the W2 determination follows.
- **Grok —** **SCRIPT-EXECUTED** if you can. Run §7; confirm rank-2/4 isotropic (~10⁻¹⁶), rank-6/8
  anisotropic, the QC approximant's q⁴ exponent, and Poisson rank-4/6 → 0 with N. Independently check the
  icosahedral invariant degrees (0, 6, 10, 15) from representation theory.
- **Copilot —** press **T3** and **T5**. Is the deterministic-vs-random dichotomy sound (causal-set = random
  = exact; deterministic icosahedral = W2)? Is W2 committed-call-ready and the W3 language correctly scoped?
- **Gemini (optional) —** press **T4** and scope. Is the accidental-vanishing loophole truly non-generic? Is
  "ruled out modulo a non-generic loophole" the right strength, neither over- nor under-claimed?

## §7. The verify code (full)

```python
import numpy as np
phi=(1+np.sqrt(5))/2
def icosa(r=1.0):
    pts=[]
    for a_,b_ in [(1,phi),(-1,phi),(1,-phi),(-1,-phi)]: pts+=[(0,a_,b_),(a_,b_,0),(b_,0,a_)]
    P=np.array(pts,float); return r*P/np.linalg.norm(P[0])
def qc_approx(levels=4):
    S=[icosa(phi**n) for n in range(levels)]; return np.vstack(S)
def rankk_anisotropy(dirs,k):
    xh=dirs/np.linalg.norm(dirs,axis=1,keepdims=True)
    rng=np.random.default_rng(3); U=rng.standard_normal((400,3)); U/=np.linalg.norm(U,axis=1,keepdims=True)
    f=np.array([np.mean((U[i]@xh.T)**k) for i in range(len(U))])
    return f.std()/abs(f.mean()) if abs(f.mean())>1e-15 else np.nan
def vphase_aniso(dirs,q,nd=500,seed=1):
    D=lambda k: np.sum(2*(1-np.cos(dirs@k)))
    rng=np.random.default_rng(seed); g=rng.standard_normal((300,3)); g/=np.linalg.norm(g,axis=1,keepdims=True)
    c2=np.mean([D(1e-4*u)/1e-8 for u in g])
    u=rng.standard_normal((nd,3)); u/=np.linalg.norm(u,axis=1,keepdims=True)
    v=np.array([np.sqrt(max(D(q*kh),0)/abs(c2))/q for kh in u]); m=v.mean()
    return (v.max()-v.min())/m if abs(m)>1e-30 else np.nan
ic=icosa(1.0)
for k in [2,4,6,8]:
    a=rankk_anisotropy(ic,k); print(f"rank-{k}: dev={a:.2e} [{'ISO' if a<1e-9 else 'ANISO'}]")
qc=qc_approx(4); qs=np.array([0.05,0.08,0.12,0.18]); av=[vphase_aniso(qc,q) for q in qs]
print("QC v_phase aniso exponent = q^%.1f" % np.polyfit(np.log(qs),np.log(av),1)[0], "; values", [f"{a:.2e}" for a in av])
rng=np.random.default_rng(7)
for N in [200,2000,20000]:
    P=rng.standard_normal((N,3)); print(f"Poisson N={N}: rank4={rankk_anisotropy(P,4):.2e} rank6={rankk_anisotropy(P,6):.2e}")
```

Expected: rank-2/4 dev ~10⁻¹⁶ (ISO), rank-6 ~9×10⁻² / rank-8 ~2×10⁻¹ (ANISO); QC exponent ~q⁴ (nonzero);
Poisson rank-4/6 → 0 as N grows.

## §8. Response format

```
REVIEWER: <your ACTUAL model name — do not use another reviewer's label>
OVERALL: <SOUND | SOUND-WITH-CALIBRATION | FLIP>
TIER USED: <INSPECTED | INDEPENDENTLY RECOMPUTED | SCRIPT-EXECUTED>
T1 group theory (no l=4; first l=6; rank-4 isotropic):
T2 inference to W2 (broadcast inherits icosahedral symmetry; §4.1 moot):
T3 deterministic-vs-random dichotomy:
T4 the accidental-vanishing loophole (non-generic?):
T5 world-call (W2 committed-ready? W3 scope? floor):
STRONGEST OBJECTION:
WORLD-CALL LANGUAGE (W2 the answer / W1 ruled-out-modulo-loophole / W3):
SCRIPT OUTPUT (if SCRIPT-EXECUTED):
OTHER NOTES (calibration for v1.1):
```
