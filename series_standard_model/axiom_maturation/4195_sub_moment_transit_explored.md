# The Sub-Moment Transit, Explored — It Is Not What 4194 Tested, and It Behaves Differently

**Patch:** 4195. **Lane:** EW. **Session:** 236.
**Founder verbatim:** `founders_voice/4195_clarification_sub_moment_transit_and_per_gp_gating.md`.
**Verify:** `series_standard_model/code/4195_sub_moment_turn_gate.py`.
**Banners:** Patch 4194 (scope). **Status: exploration under the founder's mandate** (*"do as much
exploring and finding what rules reproduce the effects of the empirics"*). Nothing adopted.

---

## 1. Not the configuration 4194 tested

4194 took c03's *"12-edge step each tick"* as one hop per Moment and let the gate alter **where the CP
ends up**. The founder's picture: **V_i fixes the end GP; the CP reaches it through many GPs within
the one Moment; the gate acts at each GP on the way.** The gate shapes the **track**, not the
**displacement**. So **4194's self-propulsion argument does not reach it** — no drift, no
self-pushing magnet, whatever the gate prefers — and 4194 §3's "same situation" argument, which
forced the gate into the W vertex, loses its force. 4194 stands for the configuration it tested.

## 2. What was computed

Walks of 300 hops on the 12-neighbour shell to a fixed endpoint, 60 random travel directions. At each
GP the candidates are the K neighbours best aligned with the *remaining* displacement **(my modelling
choice, not the founder's)**. Two gates, against a random control:

- **toward** — take the candidate most aligned with A (4193's term, e·A);
- **turn** — take the candidate that turns counter-clockwise about A from the hop just made,
  (e_prev × e)·A.

Rows verbatim (D-11). *screw h* is the track's twist about its own direction of travel; *bow* is its
sideways bulge; the last column reruns the rule on a mirror image of the inputs.

```
averages over 60 random travel directions, 300 hops each; +/- is the standard error
gate     K spin                    miss          screw h   bow along A_perp    bow along DxA  mirror image obeys the rule
none     2 A parallel to travel    0.57   0.0073+/-0.0049       0.00+/- 0.00      0.00+/- 0.00  (control)
none     2 A anti-parallel         0.57   0.0073+/-0.0049       0.00+/- 0.00      0.00+/- 0.00  (control)
none     2 A perpendicular         0.57   0.0073+/-0.0049       1.89+/- 1.34      0.62+/- 1.12  (control)
none     3 A parallel to travel    0.53   0.0030+/-0.0026       0.00+/- 0.00      0.00+/- 0.00  (control)
none     3 A anti-parallel         0.53   0.0030+/-0.0026       0.00+/- 0.00      0.00+/- 0.00  (control)
none     3 A perpendicular         0.53   0.0030+/-0.0026       1.74+/- 1.39      1.24+/- 1.53  (control)
toward   2 A parallel to travel    0.53   0.0002+/-0.0002       0.00+/- 0.00      0.00+/- 0.00  0/60
toward   2 A anti-parallel         0.60   0.0350+/-0.0428       0.00+/- 0.00      0.00+/- 0.00  0/60
toward   2 A perpendicular         0.53   0.0003+/-0.0002      24.29+/- 1.70      3.72+/- 2.74  0/60
toward   3 A parallel to travel    0.59  -0.0000+/-0.0002       0.00+/- 0.00      0.00+/- 0.00  0/60
toward   3 A anti-parallel         0.59  -0.0048+/-0.0048       0.00+/- 0.00      0.00+/- 0.00  0/60
toward   3 A perpendicular         0.64  -0.0015+/-0.0012      25.92+/- 1.60      1.33+/- 2.08  0/60
turn     2 A parallel to travel    0.59   0.1649+/-0.0149       0.00+/- 0.00      0.00+/- 0.00  60/60
turn     2 A anti-parallel         0.58  -0.1481+/-0.0151       0.00+/- 0.00      0.00+/- 0.00  60/60
turn     2 A perpendicular         0.56  -0.0007+/-0.0057      -1.19+/- 2.82    -24.48+/- 1.63  60/60
turn     3 A parallel to travel    0.56   0.4685+/-0.0114       0.00+/- 0.00      0.00+/- 0.00  60/60
turn     3 A anti-parallel         0.52  -0.4575+/-0.0089       0.00+/- 0.00      0.00+/- 0.00  60/60
turn     3 A perpendicular         0.52  -0.0007+/-0.0033      -3.62+/- 2.43    -29.08+/- 1.51  60/60
```

## 3. What it says

**Every gate reaches the endpoint** (miss ≈ half a grid spacing, the same as the control).

**"Toward A" bows the track toward the spin** — 25 spacings in 300 — and the mirror image never obeys
the rule: it violates parity. **But it is the wrong kind.** The bow is a *position* (unchanged by time
reversal) tied to a *spin* (reversed by it): **mirror-odd and time-odd.** That is the signature of an
**electric dipole moment**, not of the weak interaction, which is mirror-odd and time-**even**; with
the polarity factor it breaks CPT (filter F6). It is small enough to have escaped notice — a bow of at
most ~0.08 l_P per Moment is ~10⁻³⁴ e·cm against a measured electron bound of 4×10⁻³⁰ — so it is
**not excluded, but it is not the effect being sought.** 4193's table was right for a free hop; with
the endpoint fixed, "toward A" becomes an *ordering* of hops, and an ordering reverses under T.

**"Turn about A" makes the track a screw.** Spin along the travel: twist +0.47; spin against it:
−0.46; spin across it: no twist, a sideways bow along D × A. **The handedness of the track is
sign(A·D) — the helicity bit b, now carried as a shape in space.** The mirror image obeys the same
rule 60 times in 60, and it is time-even: **a fully symmetric law.** It cannot by itself violate
parity, and it leaves electromagnetism mirror-symmetric (F2) for free.

## 4. The back-engineered reading — worker proposal

The empirics want mirror-odd, time-even, CP-even. No single per-GP preference explored here gives
that. **Two rules together would:**

1. **Expression (symmetric): the turn gate.** A CP's track through the GPs winds about the register's
   A. This is the founder's demand from 4192 met literally — A produces a 3D configuration, the
   screw — and it answers his 19 Sep question (4156) *what configuration carries A_i*: **the track.**
2. **Selection (handed): the W accepts one screw sense per polarity.** THEO-CHIR-1 (4157) proved the
   bracelet achiral, so its handedness must be imported; a ring of GPs is a thing that *can* tell a
   left-hand screw threading it from a right-hand one. **The chirality lane's one primitive sign
   (THEO-CHIR-STATUS-1, V3) would live in this acceptance rule and nowhere else.**

Because the track's handedness **is** b, every result already derived from b carries over unchanged
in form — ⟨b⟩ = (v/c)cos θ, the free/confined contrast (F3), V−A. **Not checked:** that the screw's
average sense under ZBW jitter reproduces (v/c)cos θ; that a six-GP ring reads screw sense under the
corpus's own register rules; how sub-Moment transit sits with c03's wording.

## 5. PD-008

No convenient branch that I can see — this keeps A in the register doing visible work, against my 4191
lean, and removes the vertex-only argument I made yesterday. Attack points: the candidate rule (§2) is
mine; the 12 icosahedral directions are used as step vectors only and do not tile space; "turn" needs
the GP to know the hop just made, which no axiom yet grants; K = 2 and K = 3 agree in sign but differ
threefold in size.
