# op:einstein Closure Arc — INDEX

**Folder:** `series_relativity/op_einstein_closure/` · **Charter:** `README.md`
**Kickoff handover:** `handovers/2026-06-11_session_156_c08_op_einstein_attack_kickoff.md`
**Status:** ATTACK OPEN — Step (b) examined (1107), cheapest kill does not fire. op:einstein NOT closed.

## Steps

| Step | Scope | Status |
|---|---|---|
| **(b)** | excess-vs-absolute \|SSV\| sourcing — cheapest kill | **1107: cheapest kill does NOT fire.** Source (b1) is pure-excess (F→0 at Δ\|SSV\|=0); uniform PSR_eff background is flat (b2, R=2(−ΩΩ''+Ω'²)/Ω⁴→0 const). Inert-Sea holds as c08 eq is written. |
| **(b′)** | rigorize the shell-sum reduction | **1108: conditionally CLOSED at leading order.** Neighbor shell = 600-cell 12-edge icosahedron = spherical 5-design: monopole Σv̂=0 exactly (absolute-\|SSV\| term annihilated), quadrupole isotropic exactly (operator = Laplacian); first anisotropy at deg 6. ⇒ shell-sum → ∇²(Δ\|SSV\|), no absolute term. Conditional on c05 (vector response) + c07 (12-edge shell). |
| **(cosmo)** | uniform-Sea cosmological/Friedmann mode | HANDOFF to SR-5 Step A/C (horizon mechanism); not a local-field-equation question. |
| **(a)** | nonlinear GR-recovery: F → R_μν − ½g_μν R | **OPEN — gap pinned (1109 + 1110).** 1109: scalar+vector LSP sources zero helicity-±2 (+,×) GW modes. 1110: audited companion 7 §6 — it ASSERTS the GR wave eq `□h̄=−16πG T/c⁴` + 'TT gauge' but its metric map sources `h_ij` from the gradient of the vector `SSV_net` (no helicity-2; TT is gauge-invariant so 'TT gauge' can't supply it); c07's own open-problems list concedes full tensor recovery unproven. ⇒ helicity-2 modes ASSERTED not derived; **gap = no spin-2 d.o.f. in the LSP**. Fork: extend LSP with a spin-2 lattice mode (the fix) **or** standing tension with observed tensor GW polarizations. NOT a falsification. |

## Patch log
- **1107** — Step (b): excess-vs-absolute check (doc + verify script + reasoning). New arc folder.
  Private-lane. op:einstein NOT closed; NO VERDICT MOVED (SR-5 D2 narrowed, not discharged).
- **1108** — Step (b′): shell-sum monopole annihilation via the icosahedral 12-edge shell (spherical
  5-design). (b)/(b′) excess-sourcing conditionally closed; cap now = just (a). New side-finding:
  deg-6 anisotropic-gravity prediction (frontier flag). op:einstein NOT closed; NO VERDICT MOVED.
- **1109** — Step (a) entry: GR-recovery summit LOCALIZED to the helicity-±2 (tensor GW) sector.
  Scalar+vector LSP sources zero helicity-2 (sympy); (a) reduces to auditing companion 7 §6's
  tensor-mode claim; falsifiable by GW polarization data. op:einstein NOT closed; NO VERDICT MOVED.
- **1110** — Step (a): audited companion 7 §6 — helicity-2 modes ASSERTED (GR wave eq + 'TT gauge'),
  NOT derived (metric map sources h_ij from gradient-of-vector; TT gauge-invariant; c07 concedes
  tensor recovery open). op:einstein (a) OPEN; gap pinned = no spin-2 d.o.f. in the LSP. Fork: spin-2
  lattice-mode extension (fix) vs tension with observed tensor GW polarizations. NO VERDICT MOVED.
- **1111** — INT frontier: recorded the (a) gap + GW-polarization tension (SR.md, CONJ.md). Pointers
  to this arc; flags the tension against c08's GW claim. No new ID. NO VERDICT MOVED.
- **1112** — opened the `spin2_construction/` sub-arc (the fix). Step 1: the missing spin-2 d.o.f. =
  the l=2 quadrupole of the 600-cell shell deformation — fully resolved + independent of l=0/l=1 on
  the icosahedral shell (rank 5, orthogonal); m=±2 = the GR +,× polarizations. Extend the LSP with a
  rank-2 Q_ij. (a) NOT closed (broadcast law + wave eq + GR-recovery remain). NO VERDICT MOVED.

## Cap status (for the CC umbrella)
Before 1107 the cap was "is the source excess or absolute?" After 1107 (Step b) the cheapest kill was
removed; after 1108 (Step b′) the shell-sum rigor is conditionally closed too — the entire
excess-sourcing / inert-Sea question is now **conditionally settled and grounded in 600-cell
symmetry**. The cap is therefore **just the nonlinear GR-recovery (a)** (+ the cosmological mode in
SR-5). The CC reconciliation's honest grade is unchanged (conditional on (a)), but the conditional is
now a single, well-posed GR-recovery problem.

After 1109, that problem is itself localized to the **helicity-±2 (tensor GW) sector**: the next pitch
is to audit **companion 7 §6** — does it produce two helicity-±2 modes from the 600-cell lattice (a
rank-2 d.o.f.), or only the helicity 0/±1 modes the scalar+vector LSP supports? That single question
decides op:einstein's (a), and it is empirically decidable (GW polarization observations).

**Resolved by 1110:** companion 7 §6 does NOT derive the helicity-2 modes (it asserts the GR wave
equation; its metric map sources h_ij from the gradient of a vector, which has no helicity-2 content,
and TT is gauge-invariant). So op:einstein (a) is **genuinely open**, with the gap pinned to **a
missing spin-2 degree of freedom in the LSP**. Closing (a) = constructing a lattice spin-2
(shear/strain) mode that carries the transverse-traceless quadrupole; the GW-polarization data is the
keeping-honest test. This is the true summit of the cosmological-constant problem in CPP.
