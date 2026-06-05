# Reasoning capture — Patch 0764: SSV kernel determination + the Γ-reframing

*Session 154. The Stage-D physical input (the CPP SSV kernel), determined from corpus, plus the
consequence: the √n̄ threat is coupling-bounded (likely a phantom). Finding: `ssv_kernel_determination.md`.
Script: `scripts/0764_gamma_reframing.py`. CPP-side analytic result offered to the panel; not self-certified.
NO THEO.*

## Kernel (corpus)
SSV = Space Stress Vector = net EM/grav field at each lattice point (master_glossary). CP-CP interaction
form from series_foundations/dp-sea-polarization/DP-Sea-Polarization-Model.tex: F_rep ~ k_e q0^2/r^2 *
(polarization factors). Static/slow limit P~0 -> bare kernel = Coulomb 1/r. DP-Sea (bound dipoles) =
dielectric background (renormalizes k_e via eps, preserves 1/r; NOT Yukawa). Mobile +/- CPs self-screen
(Debye) = the DH mechanism itself, not an external rescue. KERNEL = COULOMB 1/r. Solid.

## The reframing (the key move)
DH: mu_excess/kT = -c Gamma^{3/2}, c=1/sqrt(3), Gamma = q^2/(a kT), a = n^{-1/3}. Writing a=n^{-1/3}:
mu_excess/kT = -c (q^2/kT)^{3/2} sqrt(n) => B := c(q^2/kT)^{3/2} and B*sqrt(n) == c Gamma^{3/2} == |mu/kT|.
So the spec's "B*sqrt(nbar)" IS just c*Gamma^{3/2}. Within DH validity (Gamma<~1) it is <~0.58 -- can NEVER
reach ln nbar~170.

## The phantom
"B*sqrt(1e74)~1e37" = take q^2/kT~1 (O(1)), multiply B by sqrt(1e74)=1e37. But at nbar=1e74 with q^2/kT~1,
Gamma = (q^2/kT) nbar^{1/3} ~ 5e24 = deep strong coupling, where the DH formula (hence B) is INVALID. The
threat was extrapolating a weak-coupling law into strong coupling. Verified numerically (script).
Resolves 0757 cleanly: the "absurdly weak coupling needed for sqrt(n) to survive to 1e74" is the regime
where Gamma<<1 even at 1e74, so mu/kT ~ Gamma^{3/2} << 1 -- present but tiny. NO regime where sqrt(n) is
both present AND large.

## Only genuine threat + why CPP passes
Residual hits 170 only at Gamma~44 (DH, invalid) or ~190 (strong Madelung). So the only real threat is
STRONG coupling (Gamma ~ tens-hundreds), a different form (n^{1/3} Madelung, not sqrt(n)), further
suppressed by neutrality (0756). CPP early plasma: hot RELATIVISTIC charged plasma -> kT ~ hbar c/a ->
Gamma ~ alpha ~ 1/137 (weak) -> mu/kT ~ c alpha^{3/2} ~ 3.6e-4 << 170. PASS ~5 orders margin. Plus on-GP
contact (no sqrt n, 0757) + neutrality (0756).

## Confidence ladder
- kernel = Coulomb 1/r: solid (corpus).
- B*sqrt(n)=c Gamma^{3/2}, phantom diagnosis: solid (standard plasma physics + numeric).
- only real threat = strong coupling: solid.
- CPP early plasma weakly coupled (Gamma~alpha): the ONE model-dependent input (imports relativistic-
  plasma kT~hbar c/a expectation; precise Gamma depends on emergent EM coupling + ZBW scale). The part to
  confirm. To FAIL needs Gamma >~ tens (pathological strong coupling) -- opposite to the relativistic
  expectation.

## Honesty discipline
- Did NOT self-certify the corner closed. Offered the reframing (esp. Gamma~alpha) to the panel for
  scrutiny; recommended Stage A+B numerically confirm mu/kT ~ Gamma^{3/2} << ln nbar before registering.
- Marked confidence levels explicitly; isolated the one model-dependent input.
- Reframed Stage D (report mu/kT vs Gamma, not extrapolate B*sqrt(n)); added a spec note (sec.9) flagged
  as pending panel review rather than silently rewriting the endorsed pass/fail.
- Connected to 0756/0757 (neutrality, on-GP contact) -- consistent, not contradicting.
- NO THEO (analytic de-risking; pending independent confirmation).

## Pointer
- Panel asked to scrutinize: (a) the B*sqrt(n)=c Gamma^{3/2} identity + phantom; (b) the Gamma~alpha
  estimate for the CPP early plasma. If both hold, the corner closes PASS and n_s=0.9649 can be registered
  after Stage A/B numeric confirmation. PCD = Perceive/Compute/Displace. Clear of chirality.
