# The Hop Gate's First Falsifier — Both Universal Forms Fail; a Vertex Form Is Left Standing

> **⚠ SCOPE — Patch 4195.** This patch tested **one hop per Moment with the gate altering the net
> displacement.** The founder's configuration is different: **V_i fixes the end GP and the gate acts
> at each GP of a many-hop sub-Moment transit**, shaping the track only. §§2–3 stand for the
> configuration tested and **do not reach his**; §4's argument for a vertex-only gate is no longer
> forced. See `4195_sub_moment_transit_explored.md`.

**Patch:** 4194. **Lane:** EW. **Session:** 236.
**Runs:** TODO-4193-HOPGATE test (1), self-propulsion — and test (2), F2, falls with it.
**Verify:** `series_standard_model/code/4194_hop_gate_self_propulsion.py`.
**Status:** the *universal* gate (every hop, everywhere) is excluded in both forms. **4193's symmetry
result is untouched.** What survives is narrower and is a worker proposal (§4).

---

## 1. Corpus inputs — located before building (D-3, D-7)

- **c03:** *"The CP still executes a **deterministic** 12-edge step each tick"*; and the net SSV at its
  GP *"fluctuates rapidly, at the ZBW frequency"* — the DP Sea's ZBW noise is always present in V.
- **4161:** V is *"prior to the selection and continuous."*
- **Founder 4097:** a CP carries no velocity; momentum lives in the DP arcs laid down in acceleration.
- **SF-2 (PROP-SF-2-2):** a charge captured by the W bracelet sits at the **D₆-symmetric centroid,
  the SSV-gradient minimum** — where the organised V vanishes by symmetry.

## 2. Tie-only never fires

V is a continuous, noisy vector, so an exact tie in e·V has measure zero (script: 0 in 400,000
ticks). **A gate that acts only on ties is an empty rule.** 4155 §3 had this backwards (*"common on a
lattice"*): the lattice quantises the hop, not V — the point 4161 already made.

## 3. Always-on is an electric-like field along the particle's own spin

The score is linear, so *maximise e·V + κ q (e·A)* **is identically** the ungated rule in an extra
uniform field **κ q A**. No modelling is involved in that step. The Monte Carlo only sizes the result
for a free CP at rest (V_org = 0, isotropic noise σ). Rows verbatim (D-11):

```
fraction of ticks with an exact tie in e.V (tie-only gate fires): 0.0e+00

always-on gate, free CP at rest (V_org = 0), spin along three inequivalent lattice directions
 kappa/sigma  drift/c along A: 5-fold     3-fold     2-fold  drift/(kappa/sigma)
       1e-03                  0.00052    0.00050    0.00053                0.518
       1e-02                  0.00475    0.00481    0.00489                0.481
       1e-01                  0.04844    0.04861    0.04845                0.485
       1e+00                  0.44440    0.44182    0.44304                0.443
```

**A free spin-polarised CP drifts along its spin at ≈ 0.49 (κ/σ) c, the same along every lattice
axis.** Nothing averages it away, because the spin of a polarised particle is by definition steady;
and under 4097 a steady push lays down DP arcs, so the drift is an **acceleration**. Every unpaired
electron in a magnet has the same charge and aligned spin, so **a magnet would push itself along its
own axis.** A one-gram magnet (2.4×10²² aligned spins) whose weight does not change by a microgram
when it is turned over bounds the push at < 4×10⁻³¹ N per electron — the force of a field of
**2.6×10⁻¹² V/m, or 5×10⁻²⁴ of the field that binds an atom.** That is the most κ can be, a deliberately
loose bound, and it settles F2 with room to spare — but a term that small cannot produce the **order-one**
asymmetry of weak decay.

**And the escape "small everywhere, decisive at the vertex" is closed by SF-2 itself.** At the
bracelet's centroid the organised V is zero; so is it for a free particle at rest. **To a rule with a
constant weight these are the same situation.** Whatever the gate does to the captured charge it does
to every free polarised particle.

## 4. What is left — worker proposal, not corpus

The symmetry table says a P-odd, T-even, CP-even hop rule **must** have the form q (e·A). §§2–3 say it
cannot act on every hop. **So it must be switched by something the GP can read locally**, present at a
W and absent in free space and in atoms. The corpus already points there: THEO-CHIR-1 (4157) proved
the bracelet achiral, so *"its handedness must be imported"* — it reads the incoming particle's bit.
**The gate would be the rule by which the captured charge leaves the centroid:** toward the side of
the ring along q A. That keeps EM mirror-symmetric by construction, leaves free particles alone, is
short-ranged because the bracelet is small, and is all-or-nothing, as F4 requires. **Not located:**
whether any existing axiom lets a GP's rule depend on *which sector's* content is in its register.
If none does, this is a second amendment, not a refinement of the first.

## 5. PD-008

**Convenient branch: this one** — it returns A to "local, at the weak vertex", where I stood at 4191.
A critic should press: (i) §3's linearity is exact only if the gate enters the *score*; a gate acting
some other way is not covered; (ii) the magnet bound assumes the unpaired electrons' CPs are the ones
carrying A, per A1′; (iii) §4's "same situation" claim assumes the centroid's noise equals free
space's.
