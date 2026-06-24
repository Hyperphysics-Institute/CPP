# Review Package v1.0 — Round-2 probe: does the 2I → SL(2,ℂ) boost half survive the PCD update?

**Artifact:** Round-2 finding of the exact-emergent-Lorentz root campaign (Patch 2060), CPP series_relativity.
**Self-contained:** everything needed to review is inline below (context, claim chain, triage questions,
verify code in full, response format). Fetch nothing. **Find YOUR steer in §6.**
**This is a FINDING under review, NOT a registered theorem.** No THEO, no status move has been made; the
panel verdict decides whether the stated world-probability shift is sound before anything is recorded.

---

## §0. What CPP is, and what this campaign is trying to do (cold-start context)

Conscious Point Physics (CPP) derives Standard-Model structure from a discrete **600-cell** polytope
substrate (120 vertices, symmetry group H₄ of order 14400). Conscious Points on the lattice execute a
**Perceive→Compute→Displace (PCD)** cycle once per universal **Absolute Moment** (a global clock tick of
duration the Planck time t_P). The displacement law partitions a fixed per-Moment budget l_P as
  **l_P² = (c·Δτ)² + |d_spatial|²,   |d_spatial| = l_P·β  (β = v/c).**
After the A3′ amendment, the GP→GP broadcast carries a nine-component field 𝔽 = (Φ, V_i, Q_ij)
[scalar l=0, vector l=1, symmetric-traceless tensor l=2].

**The root campaign** asks whether the PCD dynamics admit an **exact continuous SO⁺(3,1) (Lorentz)
action** on 𝔽 — a boosted self-field being an exact rigidly-translating stationary configuration in its
co-moving frame, at a continuum of velocities and all directions, with no lattice drag and no
lattice-Cherenkov radiation. Three outcomes ("worlds") are in play: **W1** clean algebraic
(discrete-exact) bridge; **W2** Lorentz exact only in the block-spin continuum limit with a
Planck-suppressed violation floor; **W3** a genuine obstruction (real preferred frame). The handover
authorized a budget of 10–50 rounds with a committed world-call at round 15.

**Round 2 (this artifact)** runs the single highest-information probe: the 600-cell's 120 vertices are
the binary icosahedral group **2I** (unit icosians) ⊂ unit quaternions; the Lorentz group has the
quaternionic/Clifford presentation **SL(2,ℂ) ≅ Spin⁺(3,1)**. Does the **2I → SL(2,ℂ) boost half**
survive contact with the PCD update, or does the fixed Absolute-Moment τ = l_P obstruct the boost
generators "at the first commutator"?

## §1. The claim being reviewed (one paragraph)

**Claim.** The naive World-1 *static-geometric quaternion bridge* fails. (i) 2I ⊂ SU(2) = maximal
compact subgroup of SL(2,ℂ), so it contains **no boost** — the vertices supply only the rotation half.
(ii) The boost the PCD **budget split** manufactures is a **compact Euclidean rotation** (generator
M, M² = −I, angle α = arcsin β), **not** a Lorentz boost (generator N, N² = +I, β = tanh η). (iii) Three
diagnostics confirm the compact real form so(4) ≠ so(3,1): the collinear composition law is circular
(β₃ = β₁√(1−β₂²)+β₂√(1−β₁²)), reaches β=1 at finite β=1/√2 and is non-monotone beyond; the boost-pair
commutator carries the **compact** real-form sign. The fixed τ = l_P entering as a **+τ²** quadrature
term is the obstruction (positive-definite form ⇒ compact isometry group). **Scope of the claim:** this
kills *one specific W1 path* (the static quaternion bridge); it does **not** claim Lorentz emergence
fails. The Minkowski (−) signature is argued to live in the **causal** structure
(ds² = (c·t_P)² − |d_spatial|², light-cone bound |d_spatial| ≤ c·t_P), carried by the **retarded A3′
broadcast**, not the static budget — relocating W1/W2 to a causal-broadcast route (Round-3 target).

## §2. The claim chain, step by step (what to scrutinize)

**S1 — 2I is compact, contains no boost.** 600-cell vertices as unit quaternions = 2I ⊂ S³ ≅ SU(2).
SL(2,ℂ) = SU(2)·{P}, P = exp(½ η n̂·σ) Hermitian-positive (boosts, eigenvalues e^{±η/2}). SU(2) is the
maximal compact; unit quaternions are unitary ⇒ 2I ∩ {boosts} = ∅. *Therefore the vertex group can
supply the rotation half only; the boost half must come from the PCD dynamics.*

**S2 — the PCD budget-split boost is a Euclidean rotation.** (c·Δτ, |d_spatial|)/l_P = (√(1−β²), β) lies
on the **unit circle**; the rest→motion map preserving the positive-definite l_P² = (c·Δτ)²+|d_spatial|²
is a Euclidean rotation by α = arcsin β, generator antisymmetric M = [[0,−1],[1,0]], **M² = −I**
(compact). A genuine boost has symmetric N = [[0,1],[1,0]], **N² = +I** (non-compact, β = tanh η). The
sign of the generator square is the entire compact/non-compact (so(4) vs so(3,1)) distinction.

**S3 — three falsifiable diagnostics (verify code §7).**
 (a) collinear composition: budget-split gives circular β₃ = β₁√(1−β₂²)+β₂√(1−β₁²); Lorentz gives
     (β₁+β₂)/(1+β₁β₂); they diverge at O(β³);
 (b) hard kill: two budget-split boosts at β=1/√2 compose to **exactly β=1** (reach c at finite β),
     non-monotone beyond — impossible for a boost group; Lorentz never reaches c;
 (c) real-form sign: the boost-pair commutator lands on the spatial-rotation block with the **compact**
     sign ([K_i,K_j] = +J for so(4) vs −J for so(3,1)).

**S4 — the obstruction is the fixed τ = l_P, and it is internally corroborated.** τ enters as +τ²
(R_4D² = r_3D² + τ², a 4D-insphere Euclidean relation) ⇒ positive-definite form ⇒ compact SO(4). SR-1's
own **Appendix H.1 elimination theorem** (no purely geometric displacement model recovers v²/c² scaling)
and its **energy-momentum bridge** (Lorentz factor injected by hand via ΔSSV = (γ−1)mc²) are exactly what
this predicts: the geometry is Euclidean, so it must fail geometrically and must import Lorentz from
elsewhere.

**S5 — relocation (the live route).** The Minkowski (−) sign is latent in the Grid frame:
ds² = (c·t_P)² − |d_spatial|² with the **fixed global tick** as cone slope and the **light-cone bound**
|d_spatial| ≤ c·t_P gives the correct proper time (c·t_P/γ). This signature is **causal** (the cone),
carried by the **retarded A3′ GP→GP broadcast** (perceive = read the backward cone), not by the static
budget partition. So the genuine boost generator, if it exists, is N built from the broadcast kernel, not
M from the budget angle. Round 3 tests exactly this.

## §3. Triage — the questions most likely to break the claim (press these hardest)

- **T1 (signature).** Is the identification "positive-definite budget form ⇒ compact real form ⇒
  M²=−I boost" correct and complete? Is there any legitimate way the *static* PCD geometry could carry an
  indefinite (Minkowski) form that this probe missed (e.g. a hidden sign in the projection, an analytic
  continuation that is physical rather than formal)?
- **T2 (scope / overclaim).** Is the conclusion correctly scoped as "kills the *static quaternion-bridge*
  boost," NOT "Lorentz emergence fails"? Flag any sentence that overreaches. (The campaign has a
  documented overclaim failure mode — be ruthless here.)
- **T3 (relocation soundness).** Is "the − sign lives in the causal/retarded broadcast, not the static
  geometry" a *sound* relocation, or a hopeful hand-wave? Specifically: does the latent identity
  ds² = (c·t_P)² − |d_spatial|² = (c·t_P/γ)² actually license attributing the Minkowski signature to
  broadcast causality, or is it just bookkeeping that any Euclidean theory could also write?
- **T4 (composition law).** Is the circular composition law the *correct* consequence of composing two
  budget-split boosts as the PCD rule defines composition? Could a different (physically-motivated)
  composition rule on the same budget yield the relativistic law without changing the signature?
- **T5 (corroboration reading).** Is SR-1's H.1 elimination theorem + energy-momentum bridge correctly
  read as corroboration (not as already containing the root)? Any misattribution?

## §4. What a verdict-flipping objection looks like

A verdict-flip on T1–T5 = a demonstration that either (a) the static PCD geometry *can* carry an exact
non-compact boost after all (reviving the static W1 path), or (b) the relocation to causal broadcast is
unsound (so the probe doesn't actually narrow the worlds), or (c) the scope is overclaimed (Lorentz is
being declared dead when it isn't). Anything short of that is calibration — note it for the artifact's
v1.1 but the finding stands.

## §5. Verification tiers (PD-002) — label every claim

- **INSPECTED** — read and judged sound by eye.
- **INDEPENDENTLY RECOMPUTED** — you re-derived the algebra/group theory from first principles yourself.
- **SCRIPT-EXECUTED** — you actually ran the §7 code and report its output.

## §6. Read YOUR row (reviewer-specific steer)

- **ChatGPT** — press T1, T2, T5 hardest (signature completeness, overclaim/scope, corroboration
  reading). Verdict-honesty: is the world-probability language defensible or inflated?
  *Disambiguation rider: this is the CPP relativity programme's exact-Lorentz root probe; it is NOT a
  nuclear-physics OPEN-SS audit, NOT a different paper, and NOT a request to reconstruct from memory —
  engage the inline package content directly.*
- **Grok** — independent recompute (run §7 → SCRIPT-EXECUTED; recompute the so(4) vs so(3,1) real-form
  distinction and the two addition laws from first principles). Strongest on the structural/group-theory
  verification — confirm or break S2/S3.
- **Copilot** — per-question structural consistency and referee-grade framing: is the S1→S5 logic chain
  valid step-by-step, and is the load-bearing step (S2, the M²=−I vs N²=+I signature) doing the work the
  conclusion attributes to it? Press T3, T4.
- **Gemini (optional breadth pass)** — confirmatory/breadth read; if you run the §7 code, show its output
  (SCRIPT-EXECUTED claims without shown output are treated as RESTATE-tier).

## §7. Verify code (consistency-evidence ONLY — never proof; run it if you can)

```python
import numpy as np

# Two candidate boost generators in the (time, x) plane.
#   Euclidean rotation  M = [[0,-1],[1,0]]  -> M^2 = -I (compact, circular)
#   Lorentz  boost       N = [[0, 1],[1,0]]  -> N^2 = +I (non-compact, hyperbolic)
M = np.array([[0.,-1.],[1.,0.]]); N = np.array([[0.,1.],[1.,0.]])
assert np.allclose(M@M, -np.eye(2)) and np.allclose(N@N, +np.eye(2))
print("M^2=-I (Euclidean/compact) ; N^2=+I (Lorentz/non-compact)  [OK]")

# velocity -> parameter:  Euclidean alpha=arcsin(beta) ; Lorentz eta=arctanh(beta)
eu = lambda b1,b2: b1*np.sqrt(1-b2**2)+b2*np.sqrt(1-b1**2)   # sin(a1+a2)
lo = lambda b1,b2: (b1+b2)/(1+b1*b2)                          # tanh(e1+e2)
# matrix-exp cross-check
eu_m = lambda b1,b2: np.sin(np.arcsin(b1)+np.arcsin(b2))
lo_m = lambda b1,b2: np.tanh(np.arctanh(b1)+np.arctanh(b2))
for b in [(0.3,0.4),(0.6,0.6),(0.8,0.8),(2**-0.5,2**-0.5)]:
    assert abs(eu(*b)-eu_m(*b))<1e-12 and abs(lo(*b)-lo_m(*b))<1e-12
    print(f"  b1=b2={b[0]:.6f}: EUCLID b3={eu(*b):.6f}  LORENTZ b3={lo(*b):.6f}  |d|={abs(eu(*b)-lo(*b)):.4f}")

# smoking guns
bs=2**-0.5
print(f"(a) two Euclidean boosts b={bs:.6f} compose to b3={eu(bs,bs):.6f}  (reaches c at FINITE b; Lorentz can't)")
print(f"(b) Euclidean compose(0.9,0.9)={eu(0.9,0.9):.6f} < compose(.707,.707)={eu(bs,bs):.6f}  (non-monotone) ; Lorentz(0.9,0.9)={lo(0.9,0.9):.6f}")
print(f"(c) at b=1e-3: |Euclid-Lorentz|={abs(eu(1e-3,1e-3)-lo(1e-3,1e-3)):.3e}  (agree to O(b^3); lab kinematics can't distinguish)")

# real-form / commutator sign (embed t-x and t-y boosts in 3x3)
def emb(g,i):
    G=np.zeros((3,3)); idx=[0,i]
    for a in range(2):
        for b in range(2): G[idx[a],idx[b]]=g[a,b]
    return G
comm=lambda A,B: A@B-B@A
print("Euclidean [M01,M02] =\n", comm(emb(M,1),emb(M,2)))
print("Lorentz   [N01,N02] =\n", comm(emb(N,1),emb(N,2)))
print("-> boost-pair commutator lands on the (x,y) rotation block with OPPOSITE sign: the [K,K]=+J (so4) vs -J (so3,1) distinction.")
```

Expected output (for cross-check): M²=−I/N²=+I OK; at β₁=β₂=0.6 EUCLID 0.960 vs LORENTZ 0.882; (a)
β₃=1.000000 at β=1/√2; (b) Euclidean 0.785 < 1.000, Lorentz 0.994; (c) |Δ|≈1e−9; the two commutators are
negatives of each other on the (x,y) block.

## §8. Response format (please use this)

```
REVIEWER: <name>
OVERALL: <SOUND / SOUND-WITH-CALIBRATION / VERDICT-FLIP>
TIER USED: <INSPECTED / INDEPENDENTLY RECOMPUTED / SCRIPT-EXECUTED>
T1 signature-completeness : <assessment>
T2 scope / overclaim      : <assessment — quote any overreaching sentence>
T3 relocation soundness   : <assessment>
T4 composition law        : <assessment>
T5 corroboration reading  : <assessment>
STRONGEST OBJECTION: <the single most load-bearing problem you found, if any>
WORLD-PROBABILITY LANGUAGE: <defensible / inflated — and why>
OTHER NOTES: <calibration items for v1.1>
```

---

*Package authored by Claude Opus under Thomas Lee Abshier's direction (Patch 2061), exact-Lorentz root
campaign. Companion artifact: `lorentz_root/2060_round2_quaternion_boost_commutator_probe.md`. Responses
aggregate into `lorentz_root/review/reviews-2060.md`.*
