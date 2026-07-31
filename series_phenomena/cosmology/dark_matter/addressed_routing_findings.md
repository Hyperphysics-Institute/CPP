# ADDRESSED FCC ROUTING — TESTED AT LAST, AND A 2895 ERROR CORRECTED

**Patch 2896. The founder asked directly whether his described mechanism was
what the worker had tested. IT WAS NOT.**

---

## §1 — CORRECTION TO PATCH 2895

2895 reported an isotropy table with a **"lattice paths"** row and concluded
the discriminator was *whole-shell versus 12-direction emission*. Reading
the committed code:

```python
elif mode=="lattice_paths":
    # bit walks toward a RANDOM shell GP: random target direction, then
    # each hop takes the FCC edge best aligned with that target
    v=rng.normal(size=(per,3)); tgt=v/np.linalg.norm(v,axis=1,keepdims=True)
    d=tgt          # <-- STRAIGHT-LINE CONTINUUM TRAVEL
```

**The comment describes hop-by-hop lattice routing. The code implements
straight-line continuum travel.** `lattice_paths` and `continuum` were the
**same computation with different random draws** — which is why their
columns agreed to three decimals (0.024/0.022/0.023 vs 0.026/0.023/0.026).
**That agreement was not a cross-check; it was a duplicate.**

**The founder's mechanism had never been run.** His inference —
*"whatever you were using appeared to work, so it is probably right"* —
does not hold, and is corrected here.

**What 2895 does still establish:** continuum ballistic emission is
isotropic (0.023) and 12-fixed-direction emission is not (3.109). Those
rows were real and distinct. **The middle row was not.**

## §2 — THE MECHANISM AS THE FOUNDER SPECIFIED IT

> - DI-bits are emitted from GP_origin with an **address** to GP_PSR
>   computed by SSV_abs.
> - DI-bits are conserved.
> - The pathway is traversed by **a series of absorptions and
>   re-radiations to the 12 nearest neighbors** of each GP.
> - Re-radiation continues until all DI-bits have landed on the PSR shell.
> - This relay **distributes all the DI-bits evenly across all GPs at PSR.**

Implemented two ways, since *"re-radiation to the 12 nearest neighbors"*
admits both readings: **greedy** (deterministic best-aligned edge) and
**softmax** (probability distribution over all 12, biased by alignment).

## §3 — SECOND CORRECTION: THE OBSERVABLE, ONE LAYER DOWN

First measurement used solid-angle patches and reported in-transit CV of
2.61 at r = 4 — apparently catastrophic near-field anisotropy.

**That was the Patch 2891 error repeated one level deeper.** At small
radius the lattice has **very few sites** — exactly 12 GPs at r = √2, 6 at
r = 2, 24 at r = 2.449. Solid-angle patches containing **no lattice sites
at all** register as empty and inflate CV. **The measurement was reading
lattice discreteness, not field structure.**

**Correct observable: a CP can only sit AT a GP.** So compare bit counts
**across GPs at the same radius.**

## §4 — RESULT (code/2896_gp_level_isotropy.py, R = 24, 40k bits)

| radius | #GPs | greedy CV | softmax β=3 CV |
|---|---|---|---|
| **1.414 (√2)** | **12** | **0.0153** | **0.0132** |
| 2.449 | 24 | 0.0733 | 0.0313 |
| 2.828 | 36 | 1.4004 | 0.4342 |
| 3.162 | 44 | 1.6139 | 0.4196 |
| 4.000 | 90 | 1.9545 | 0.2556 |
| 6.000 | 186 | 2.8874 | 0.2318 |
| 8.000 | 246 | 1.4430 | 0.2108 |

**FINDING 1 — the nearest-neighbour shell is essentially PERFECTLY
isotropic (CV ≈ 0.014), under both routing rules.** All 12 GPs at r = √2
receive equal bit counts. This follows by symmetry: uniformly distributed
addresses give uniformly distributed first hops.

> **This is the scale at which the CONJ-FP-1 inertia mechanism operates.**
> The DP arcs whose fore/aft asymmetry drives inertia are nearest-neighbour
> structures. **At that scale the addressed-routing field is isotropic and
> the mechanism has the smooth background it requires.**

**FINDING 2 — probabilistic re-radiation is 5–8× better at intermediate
radii** (0.26 vs 1.95 at r = 4; 0.23 vs 2.89 at r = 6). **The founder's
phrasing — re-radiation *to the 12 nearest neighbors*, plural — reads more
naturally as a distribution than as a deterministic pick, and the
distribution is what performs better.**

**FINDING 3 — intermediate-radius anisotropy is real and unresolved.**
Even softmax leaves CV ≈ 0.2–0.4 at r = 3–8, against a noise floor near
0.03. Not catastrophic, not clean. Registered as open.

## §5 — THE COST OF DIFFUSE ROUTING

Mean hop counts to R = 30 (ideal R/√2 = 21.2): greedy 25.2; softmax β=6
26.5; β=3 32.9; **β=1.5 53.4.**

**Isotropy and ballistic speed trade off directly.** Strongly diffuse
routing fills the field in but takes 2.5× the minimum path, so the
effective propagation speed falls well below c_lat. **β ≈ 3 is the
observed compromise: 1.55× ideal path length with 5–8× better isotropy.**

**This is a genuine constraint on the mechanism and it has no free
parameter available to escape it** — β is set by whatever physically
determines the re-radiation distribution, which is a founder-physics
question.

## §6 — STANDING

**CONJ-FP-1 Condition B: remains CLOSED** — retardation is a property of
ballistic travel and is unaffected by the routing rule. **The nearest-
neighbour isotropy result strengthens the mechanism's footing** at the
scale where it operates.

**Open:** Condition A (sign of the Sea's response); LINK 2 (marginality);
LINK 3 (B1 stability). Statics suspension per 2892 stands.

Ledger untouched: 1B OPEN; PR7 PARTIAL; six of seven; B7 holds; Candidate
(B) 79.5%. G1 and P-A2-1 stand.
