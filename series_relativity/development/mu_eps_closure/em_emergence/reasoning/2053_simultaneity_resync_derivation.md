# Reasoning capture — Patch 2053: simultaneity-resync derivation (OPEN-SR-9-B first brick)

**STATUS: verbatim (captured at-patch).** Window: 2049-band (SR-9). Verify:
`em_emergence/verify/sr9b_simultaneity_resync.py`. NO THEO; no status move; pending CONV-001.

## 0. What this is
The OPEN-SR-9-B first brick: derive the relativity of simultaneity (offset γvx/c²) from the located GP update
rule, with a no-hidden-velocity audit. **Result: closes at the kinematic level — the offset emerges EXACTLY,
no velocity register inserted.** Honest boundary in §4.

## 1. The rule (located; SR-1 §A.4/A.8.1, c01, pcd_boost_law) — SSV-only
Per CP per Absolute Moment: direction `i*=argmax_i(e_i·∇SSV)` (drift from SSV_net, vector); rate
`PSR_eff=l_P/(1+k·ΔSSV)` (from SSV_abs, scalar); displacement `d=l_P·e_{i*}`; **4D budget split**
`l_P²=(c·Δτ)²+|d_spatial|²`. Velocity is NOT an input — it is read off the partition: `|d_spatial|=l_P·(v/c)`,
`v=|d_spatial|/Δτ`. SR-1 already gives, EXACT (=γ_SR, A.8.1): dilation (Δτ/Moment=1/γ), contraction (L₀/γ),
momentum (γmv). The leg SR-1 deliberately did NOT use: relativity of simultaneity — the twin paradox is
resolved by absolute ΔSSV accumulation ("no appeal to relativity of simultaneity is needed", mechanism-SR-1).
So simultaneity is the genuinely open leg, and the one Obligation A (exact undetectability) most exposes.

## 2. The derivation
Two co-moving clocks A(trailing)/B(leading), proper separation L₀, moving +x at v through the lattice.
Substrate inputs, all from SR-1: light advances at c ISOTROPIC IN THE LATTICE frame (one PSR shell/Moment,
H₄-isotropic); clocks dilate by γ; rod contracts to L=L₀/γ. A co-moving observer Einstein-synchronizes A,B with
a light pulse, ASSUMING one-way c isotropic (they cannot detect lattice motion). In the lattice frame the pulse
moves at c, the clocks at v, so the one-way legs are asymmetric:
  t_AB = L/(c−v)  (light chases receding B),  t_BA = L/(c+v)  (meets approaching A).
- **Two-way (the easy null):** round-trip on the observer's own (dilated) clocks = 2L₀/c — isotropic. This is
  why Lorentz–FitzGerald already passes Michelson–Morley.
- **One-way (the hard leg):** Einstein sync assumes t_AB=t_BA; the real asymmetry is absorbed as a clock
  offset δ = ½(t_AB−t_BA) = **γvL₀/c²** in lattice time — which is EXACTLY the Lorentz prediction
  (verify: MATCH True). Contraction + dilation + this offset reconstruct the full transform t'=γ(t−vx/c²),
  so one-way light speed is isotropic in the MOVING frame too ⇒ the absolute lattice frame is exactly
  undetectable. **The one-way-isotropy worry raised at charter §3 is thereby RETIRED** — one-way isotropy is
  secured by the emergent offset, not assumed.

## 3. No-hidden-velocity audit — PASS
Every v in the derivation traces to a budget-partition OUTPUT (each clock-CP steps |d_spatial|=l_P·(v/c) per
Moment by its own budget split). The observer never uses v — they only emit/receive light and apply the
isotropy convention they're forced into. The light's advance (c, one shell/Moment) and the clock's advance (v,
from budget) are both GP-rule outputs; their relative rate (c∓v) is not computed by anything in the substrate,
it is just the rate at which the light pattern overtakes/meets the stepping clock-CP. v is the analyst's
lattice-frame coordinate bookkeeping, NOT a CP register. So velocity stays emergent throughout.

## 4. Honest boundary + residual (front-loaded for CONV-001)
This is a **kinematic-level** closure: it instantiates the textbook Lorentz–FitzGerald→Einstein equivalence (a
real preferred frame + contraction + dilation + light-sync ⇒ indistinguishable from SR) ON the CPP substrate,
which supplies the otherwise-stipulated pieces (the lattice frame is the 600-cell; contraction/dilation are
ΔSSV-budget effects, derived exact in SR-1). It is NOT yet a from-the-discrete-600-cell-dynamics theorem. The
load-bearing imported premise is **(i) light is isotropic at c in the lattice frame**. SR-1 takes this from the
budget-advance (one PSR shell/Moment) + H₄ symmetry; grounding it from the discrete dynamics is the residual —
and it is the SAME lattice-isotropy-of-c question that OPEN-SR-9 / R2 already turn on. So the simultaneity brick
**reduces its own residual to the R2 residual** — a real convergence: closing lattice-isotropy-of-c would
simultaneously theorem-grade this brick and ground R2.

Anticipated panel attacks to put up front: (a) is this a genuine substrate closure or textbook kinematics
re-skinned? (b) is premise (i) assumed rather than derived? (c) does the audit truly avoid a hidden velocity,
or is "c∓v closing speed" a velocity primitive in disguise? My read: (a) substrate-grounded for
contraction/dilation, kinematic for the sync step — honestly labeled; (b) yes, (i) is imported, and is the
named residual; (c) the closing speed is a relative rate of two budget outputs, not a register — but this is
exactly what the swarm should stress.

## 5. Where this leaves OPEN-SR-9-B
The simultaneity leg — the thinnest, the one SR-1 routed around, the one Obligation A most exposed — **closes at
the kinematic level with the offset exact and no velocity register.** Combined with the already-exact dilation +
contraction + momentum, the undetectability conspiracy is discharged at the kinematic level; full Lorentz
emerges; velocity stands confirmed as emergent bookkeeping (not a substrate register) for inertial kinematics.
Residual for theorem grade = lattice-isotropy-of-c (shared with R2). The B-neutrality/R2 descent (charter §7)
still waits on that shared residual, so **R2 stays conditional-PASS.** Pending CONV-001 on this brick.

## 6. Discipline
Owned subtree (mu_eps_closure/em_emergence/), 2049-band. No root-registry or status-file edit. NO THEO (kinematic
derivation pending panel; nothing recorded as theorem). Collision-clean against HEAD 2052.
