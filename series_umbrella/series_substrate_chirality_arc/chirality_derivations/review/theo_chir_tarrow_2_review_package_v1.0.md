# Review package — THEO-CHIR-TARROW-2 (a derived substrate time-asymmetry mechanism: the O(δ³) non-reversibility of the Mechanism-A process)

**Artifact:** `chirality_derivations/theo_chir_tarrow_2.tex` (v1.0, Patch 0690). Verify: `code/verify_odelta3_kolmogorov_curl.py` (embedded in full, §7).
**Type:** Layer-2.5 provisional computational theorem. **Self-contained** — everything you need is in this package; no other files required.

---

## 0. IS / IS-NOT
- **IS** the *mechanism half* of TARROW-1: a derived substrate T-asymmetry mechanism (the O(δ³) non-reversibility / steady-state probability current of the Mechanism-A process), proposing a **candidate** 𝒞_T=Yes ⇒ **W3→W1** upgrade on the time-reversal axis, conditional on Mechanism A.
- **IS NOT** a spatial verdict move (FI-C-9 stays **V3**), a fixing of the arrow **direction** (W1, not W0), a proof that reflection positivity fails or sign(μ²)<0 (the P-side capacity is a *separate* computation), or a **closed** W-move. v1.0 is provisional; the W3→W1 claim is made only at review-close (DG-3). **V3/W3 stand.**

## 1. Context (settled — consumed, not re-derived)
**TARROW-1 v1.1** (review-closed 3/3): instantiated the STATUS-1 verdict partition on the time-reversal axis — capacity 𝒞_T (is a substrate T-asymmetry *mechanism* derivable?) × value 𝒱_T (is the arrow *direction* fixed?), verdicts W3 (primitive arrow), W1 (emergent mechanism, contingent direction), W2 (fully emergent). It placed sign(δ) at **W3**, with **𝒞_T=No** resting explicitly on "*no registered mechanism derives a substrate T-asymmetry* — DSL-3 narrates the arrow but inherits the DSL viability ceiling; the F.2 physicalization is unbuilt," and it **excluded W2 at the axiom level** (sign(δ) is the unique T-odd object, so fixing its direction is circular), pinning any upgrade to **W1** (direction free = cosmological inheritance). TARROW-1 stated it does **not** derive the mechanism.

Also consumed: **Mechanism A** (F.1 framework rate law r(ê)=r₀(1+δ ê·n̂) on the 600-cell, Axioms MA.1/MA.2 — a *framework axiom*, its Layer-4 derivation from A1–A11 is OPEN-FP-F1-2); **THEO-DSL-3** (δ=0 detailed balance); **Patch 0535** (the discrete curl of the net DI-bit current vanishes at O(δ¹)); **VW-2 v1.1** (the δ=0 RP anchor + the RP=OS-reflection≠T-symmetry caution, Θ_OS vs P_det). δ = chirality-deviation parameter; n̂ vertex-aligned Reading C.

## 2. THEO-CHIR-TARROW-2 — the claims (inline)

**Lemma A (order-counting).** The detailed-balance / Kolmogorov cycle log-ratio is L(a→b)=log[(1+δc)/(1−δc)]=2(δc+δ³c³/3+δ⁵c⁵/5+…), c=ê_ab·n̂ — **odd in δ** (reversing an edge sends c→−c). So the cycle violation has **only odd powers**; the O(δ²) term is **identically zero**, and the first possible violation is **O(δ³)**. (This corrects the Patch-0688 sketch, which located the gate at O(δ²).)

**Lemma B (per-face content).** The triangular faces generate the cycle space of the 600-cell 1-skeleton (the polytope boundary is a simply-connected triangulated 3-sphere), so detailed balance ⟺ Σ L vanishes around every triangular face. Per face with oriented edge-projections a,b,c: the three oriented edge *vectors* sum to zero (closed loop) and all edges share length ℓ=1/φ, so **a+b+c=0** ⇒ the O(δ¹) sum 2δ(a+b+c) vanishes for *every* face; and the O(δ³) sum is (2δ³/3)(a³+b³+c³) = **2δ³·abc** (via a+b+c=0 ⟹ a³+b³+c³=3abc).

**Theorem (O(δ³) non-reversibility).** Under Mechanism A at vertex-aligned Reading C, the induced Markov process on the 600-cell violates the Kolmogorov cycle condition at O(δ³): the per-face content 2δ³·abc is nonzero on **420 of the 1200 triangular faces** (|abc|∈{1/8,1/4}), all touching the second shell. The process is therefore **non-reversible**; it carries a nonzero steady-state probability current. (First-shell faces vanish: icosahedral faces have all edges ⊥ n̂; host-side faces have two host-edges of opposite orientation whose cubes cancel — so the residual sits at the second shell, as Patch 0688 predicted.)

**Remark (why third order).** The bias δ ê·n̂ is a single-step gradient (conservative ⇒ O(δ¹) cycle-zero), but the Kolmogorov condition lives in log r, *nonlinear* in ê·n̂; the δ³ term ∝(ê·n̂)³ is non-conservative. The arrow is a **nonlinear** effect of the multiplicative rate law.

**Proposition (candidate W3→W1).** A non-reversible Markov process carries a steady-state probability current = a genuine time-asymmetry. So 𝒞_T is answered **Yes** at the Mechanism-A framework level — the upgrade condition TARROW-1 named for W3→W1. 𝒱_T (direction) is untouched: a current exists but its "forward" sense is not fixed (consistent with TARROW-1's axiom-level W2-exclusion). Upgrade is to **W1**, not W2.

**Non-conflict with TARROW-1.** TARROW-1's "the only T-odd object is sign(δ)" concerned static *geometric* invariants (coordinates, Gram data, distance spectrum, sign(n̂)) — all T-even. The current is a *dynamical* object built from the rates — precisely the F.2 physicalization TARROW-1 flagged as unbuilt. This *builds* it; no contradiction.

## 3. The registered position
TARROW-2 supplies the derived mechanism TARROW-1 lacked, proposing the candidate W3→W1 upgrade conditional on Mechanism A. v1.0 is provisional; **registration does not close the W-move.** THEO-CHIR-CAPACITY-1 (the P-side/μ² ID) stays reserved. No spatial V-move; no direction; no μ²/RP claim.

## 4. What we want you to scrutinize (load-bearing)

**Q1 — the capacity-bar inference (DEEPEST RISK, press hardest).** TARROW-1's 𝒞_T=No rested on "no *derived* mechanism." TARROW-2 derives a mechanism **conditional on Mechanism A**, which is itself a *framework axiom* (OPEN-FP-F1-2), not derived from A1–A11. **(a)** Does "a mechanism conditional on an undischarged axiom" genuinely meet the 𝒞_T=Yes bar (⇒ W1), or does it merely *relocate* the No from "DSL viability ceiling / F.2 unbuilt" to "Mechanism A underived" — leaving the verdict effectively W3-pending-MA, or at most a **conditional W1** (W1 | Mechanism A)? **(b)** Apply the STATUS-1 calibration (a classification/upgrade is informative only if it yields a *falsifiable constraint*, not a relabeling): does the W3→W1 upgrade here yield a falsifiable constraint, or is it borderline-bookkeeping until Mechanism A is derived? **(c)** Is "candidate W3→W1, conditional on Mechanism A" the right registration language, or should it be qualified/weakened (e.g. "W1 conditional on Mechanism A," or "mechanism exhibited; W-move deferred to OPEN-FP-F1-2")? This is the question most likely to require a **restatement** of the Proposition.

**Q2 — current ⟹ time-asymmetry (is the arrow real, and is its direction free?).** Is a nonzero Kolmogorov/detailed-balance violation a genuine *physical* time-asymmetry (a substrate arrow), or merely a non-equilibrium circulation that need not be "the arrow of time"? And is the current's direction correctly tied to **sign(δ)** (the per-face content 2δ³·abc flips sign with δ), so that "direction free until sign(δ) is fixed" is the correct W1 reading (not W0)? Any overclaim in "probability current = arrow"?

**Q3 — the cycle-space generation (rigor of Lemma B).** Do the 1200 triangular faces actually generate the full cycle space of the 600-cell 1-skeleton (dimension E−V+1 = 720−120+1 = **601**), so that per-face Kolmogorov ⟺ global detailed balance? Is "simply-connected 3-sphere boundary ⇒ faces generate" airtight, or should the package carry an explicit rank-verification that the 1200 face-cycles span the 601-dim cycle space? (Grok: please rank-check.)

**Q4 — order-stability.** Is "a single nonzero face ⇒ non-reversible, hence order-stable" correct (reversibility is all-or-nothing per cycle), and is it right that higher odd orders (δ⁵,…) cannot *rescue* reversibility once O(δ³) violates it on 420 faces for small δ≠0? Any δ-regime subtlety?

**Q5 — non-conflict with TARROW-1 (likely calibration).** Is the "dynamical vs geometric T-odd object" distinction the cleanest framing — OR is the current more accurately the **dynamical realization of the unique T-odd object sign(δ)** (since it is built from δ), rather than "a new dynamical T-odd object"? If the latter, the non-conflict is *strengthened* (the current does not compete with sign(δ); it physicalizes it) and the §6 wording should be calibrated. Which framing is correct?

**Q6 — the verify script (§7).** Run it. Confirm the geometry (120/720/1200, degree 12), max|a+b+c|≈0, the a³+b³+c³=3abc identity, and the O(δ³) result (max|abc|=1/4; 420/1200 faces nonzero; all touching the second shell). Recompute abc per face from first principles if you can.

**Q7 — honest caps / overclaim / no closed verdict move.** Confirm: no spatial V-move (V3 stands); no arrow direction (W1, not W0); no μ²<0 / RP-failure claim (DB sufficient-not-necessary for RP; RP=OS reflection≠T-symmetry); the W-move is *not* closed by registration. Any place the theorem reads as stronger than "a mechanism, conditional on Mechanism A"?

## 5. Triage priority
**Q1 first — existential** (the capacity-bar / derivation-vs-axiom inference; the Proposition may need restatement). **Then Q5** (the TARROW-1 non-conflict framing — likely calibration). **Then Q3** (cycle-space rigor of Lemma B). Then Q2 (arrow reality + direction), Q4 (order-stability), Q6 (script), Q7 (caps).

## 6. Reviewer-specific framing
- **ChatGPT** — press **Q1** hardest (does a mechanism conditional on the Mechanism-A axiom meet the 𝒞_T=Yes bar, or relocate the No? apply the STATUS-1 falsifiable-constraint calibration) + the overclaim/deflation sweep (Q7). Adjudicate the registration language. Disambiguation rider applies.
- **Grok** — run the §7 code → SCRIPT-EXECUTED; recompute abc per face from first principles; **rank-check Q3** (do the 1200 face-cycles span the 601-dim cycle space?); verify the two identities and the 420/1200 count.
- **Copilot** — per-question structural consistency; the logic of **Q5** (is the dynamical/geometric non-conflict airtight, or should it be "the current realizes sign(δ)"?) and the Lemma-B chain (faces ⇒ cycle space ⇒ detailed balance, Q3).

## 7. Verification (embedded in full — run it)

```python
#!/usr/bin/env python3
"""
verify_odelta3_kolmogorov_curl.py  --  Patch 0689, Session 152.

The O(delta^3) Kolmogorov / detailed-balance computation for the Mechanism-A
substrate rate field (the first verdict-relevant computation of the deep engine,
1d-beta-ii / F.1 sec-14.17).

Mechanism A (F.1 framework axiom): r(e) = r0 (1 + delta * e.n_hat) on the 600-cell.
Detailed balance (reversibility) of the induced Markov process holds iff the
Kolmogorov cycle condition holds: for every cycle, prod(forward rates) =
prod(backward rates). The per-directed-edge log-ratio is

    L(a->b) = log[ r(a->b) / r(b->a) ] = log[(1+delta c)/(1-delta c)]
            = 2 ( delta c + delta^3 c^3/3 + delta^5 c^5/5 + ... ),   c = e_ab . n_hat

-- ODD in delta only (forward/backward antisymmetry). Detailed balance <=> the
sum of L around every face vanishes at every order.  KEY CORRECTION to the 0688
sketch's "O(delta^2) gate": there is NO O(delta^2) term; the first possible
violation is O(delta^3).

Per triangular face, the three oriented edge-projections satisfy a+b+c=0 (closed
loop + uniform 600-cell edge length), so the O(delta^1) sum vanishes for EVERY
face, and the O(delta^3) sum is (2/3)(a^3+b^3+c^3) = (2/3)(3abc) = 2abc -- the
triple product of edge-projections.

  CHECK 1  geometry: 120 vertices, 720 edges, 1200 triangular faces, degree 12.
  CHECK 2  O(delta^1): max|a+b+c| over all faces = 0 (DB holds at first order).
  CHECK 3  O(delta^3): compute abc per face. RESULT (reported, not assumed):
           is detailed balance preserved (all abc=0) or violated (some abc!=0)?
"""
import numpy as np
from itertools import permutations as P, combinations

phi = (1 + np.sqrt(5)) / 2
edge = 1 / phi


def build_600():
    Vs = []
    for i in range(4):
        for s in (1, -1):
            v = np.zeros(4); v[i] = s; Vs.append(v)
    for s in range(16):
        Vs.append(np.array([((s >> k) & 1) * 2 - 1 for k in range(4)]) / 2.0)
    base = [phi / 2, 1 / 2, 1 / (2 * phi), 0]
    for s1 in (1, -1):
        for s2 in (1, -1):
            for s3 in (1, -1):
                sg = [base[0] * s1, base[1] * s2, base[2] * s3, base[3]]
                for pm in P(range(4)):
                    inv = sum(1 for i in range(4) for j in range(i + 1, 4) if pm[i] > pm[j])
                    if inv % 2 == 0:
                        Vs.append(np.array([sg[pm[i]] for i in range(4)]))
    U = []
    for v in Vs:
        if not any(np.allclose(v, u, atol=1e-9) for u in U):
            U.append(v)
    return np.array(U)


def main():
    V = build_600(); N = len(V)
    Dm = np.array([[np.linalg.norm(V[i] - V[j]) for j in range(N)] for i in range(N)])
    adj = (np.abs(Dm - edge) < 1e-6)
    deg = adj.sum(1)
    edges = [(i, j) for i in range(N) for j in range(i + 1, N) if adj[i, j]]
    faces = [(i, j, k) for i, j, k in combinations(range(N), 3)
             if adj[i, j] and adj[j, k] and adj[i, k]]
    c1 = (N == 120 and len(edges) == 720 and len(faces) == 1200
          and deg.min() == 12 and deg.max() == 12)
    print("CHECK 1 -- 600-cell geometry")
    print(f"  vertices={N} edges={len(edges)} faces={len(faces)} degree=[{deg.min()},{deg.max()}]"
          f"  [{'PASS' if c1 else 'FAIL'}]\n")

    nhat = V[np.argmax(V[:, 0])].copy(); nhat /= np.linalg.norm(nhat)   # vertex-aligned Reading C

    def proj(a, b):
        e = V[b] - V[a]; return float(e @ nhat) / np.linalg.norm(e)

    sum1, abc = [], []
    for (i, j, k) in faces:
        a, b, cc = proj(i, j), proj(j, k), proj(k, i)
        sum1.append(a + b + cc); abc.append(a * b * cc)
    sum1 = np.array(sum1); abc = np.array(abc)

    c2 = np.max(np.abs(sum1)) < 1e-12
    print("CHECK 2 -- O(delta^1) per-face curl (detailed balance at first order)")
    print(f"  max|a+b+c| over 1200 faces = {np.max(np.abs(sum1)):.2e}  (=0 => DB holds at O(d^1))"
          f"  [{'PASS' if c2 else 'FAIL'}]\n")

    nz = np.abs(abc) > 1e-9
    print("CHECK 3 -- O(delta^3) Kolmogorov content (per-face curl ~ 2 delta^3 abc)")
    print(f"  max|abc| = {np.max(np.abs(abc)):.4f}")
    print(f"  faces with abc != 0: {int(nz.sum())} of {len(faces)}")
    print(f"  distinct nonzero |abc| values: {sorted(set(np.round(np.abs(abc[nz]),6)))}")
    db_holds_o3 = (np.max(np.abs(abc)) < 1e-9)
    host = int(np.argmax(V @ nhat))
    dh = np.array([np.linalg.norm(V[m] - V[host]) for m in range(N)])
    shell = np.where(np.arange(N) == host, 0, np.where(np.abs(dh - edge) < 1e-6, 1, 2))
    touches2 = sum(1 for idx, (i, j, k) in enumerate(faces)
                   if nz[idx] and 2 in (shell[i], shell[j], shell[k]))
    print(f"  of the {int(nz.sum())} nonzero faces, {touches2} touch the 2nd shell "
          f"(consistent with the first-shell cancellation)")
    print(f"\n  RESULT: detailed balance at O(delta^3) is "
          f"{'PRESERVED (all abc=0)' if db_holds_o3 else 'VIOLATED (probability current present)'}.")
    print(f"  => the Mechanism-A process is {'reversible' if db_holds_o3 else 'NON-reversible'} at third order;")
    print(f"     the curl-free / equilibrium (V3-by-principle) branch is "
          f"{'confirmed' if db_holds_o3 else 'RULED OUT'} at O(delta^3).")
    print(f"\n[CHECK 3 is a faithful computation, not a pass/fail gate -- it REPORTS the curl content.]")
    print("=" * 68)
    print("ALL STRUCTURAL CHECKS PASS" if (c1 and c2) else "STRUCTURAL CHECK FAILED")
    print("=" * 68)


if __name__ == "__main__":
    main()
```

**Expected output:** CHECK 1 PASS (120/720/1200, degree 12); CHECK 2 PASS (max|a+b+c| ≈ 2.2e-16); CHECK 3 reports max|abc|=0.25, 420/1200 faces nonzero (values 1/8, 1/4), all touching the 2nd shell ⇒ detailed balance VIOLATED at O(δ³), the process is NON-reversible, the curl-free branch is RULED OUT.

## 8. What CONFIRM / RESTATEMENT / FALSIFIER look like
- **CONFIRM:** the computation is faithful (Q6), Lemma B's cycle-space generation holds (Q3), the order-counting and per-face formula are correct (Q2/Q4), and the candidate W3→W1 (conditional on Mechanism A) is a fair registration (Q1) — possibly with calibrations (Q5 framing; Q1 language).
- **RESTATEMENT-NEEDED:** Q1 finds that "conditional on the Mechanism-A axiom" does not meet the 𝒞_T=Yes bar as stated ⇒ the Proposition is rescoped to a *conditional* W1 (or the W-move deferred to OPEN-FP-F1-2); and/or Q5 finds the non-conflict should be reframed as "the current realizes sign(δ)." Engine/computation unchanged.
- **FALSIFIER:** Q3 finds the faces do *not* generate the cycle space (per-face ≠ global detailed balance), or Q6 finds the computation wrong (the 420 count / identities fail), or Q2 finds "current ⇒ arrow" untenable for this process — any of which would break the Theorem or the Proposition.
