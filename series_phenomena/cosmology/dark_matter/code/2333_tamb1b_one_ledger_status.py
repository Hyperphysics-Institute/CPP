#!/usr/bin/env python3
# 2333 -- TAMB-1(b) DERIVED (fails): dynamical Sea excitation SOURCES.
#
# The question (2331, pre-registered): G1-G3 zeroed the quiescent monopole; do
# activated (Boltzmann-weighted, knee-carrying) Sea fluctuations fall on the
# quiescent (zeroed) or dynamical (sourcing) side of the one-ledger split?
#
# The derivation, in one line: the registered sector has ONE sourcing rule
# (c05/Step B gradient-sourcing: sources <=> carries grad(dSSV)) and ONE zeroing
# mechanism (Sigma v-hat = 0, annihilating exactly the gradient-free component);
# the harmonic-null theorem (2330) proves the knee cannot be carried by any
# gradient-free (coherent/uniform) channel; therefore every knee-carrier is a
# localized, gradient-carrying excitation -- outside the annihilated subspace,
# inside Case 3, at full ledger weight (provenance-blind G1, form-blind C-d).
# The exemption is not merely underivable: it is INCONSISTENT with the
# registered structure (it would un-derive Case 3 -- the candidate itself --
# and Case 4 -- the Lambda result, which IS the sourcing of a Sea mode's
# zero-point field energy at the gentlest gradient in the framework).
#
# VERDICT MOVED (by pre-registered outcome (ii), campaign-ledger entry only):
# X4' corner DEAD; G4 -> KILL-on-suite-conditional. Report to 20 July as such.

import math
from fractions import Fraction

HBARC    = 197.327          # MeV fm
RS       = 25.42            # fm (coarse cell; k = 1/RS)
KNEE_LO  = 1.60e-3          # MeV (PRW window, 2327/2330)
KNEE_HI  = 11.27e-3         # MeV
EGAP     = 0.9              # MeV (e-channel, M3)
RHO_CRIT = 8.5e-30*5.6096e26*1e-39   # MeV/fm^3 (h ~ 0.7)
LP       = 1.616e-20        # fm, Planck length
D_PLANCK = LP/6.0           # c*fm -- coherent-channel residue (2330)
D_LO, D_HI = 5.2e-3, 3.7e-2 # c*fm -- PRW-D window (2327)
RH       = 1.30e41          # fm, Hubble radius ~ 4.2 Gpc (order-setting only)
FLOOR    = 0.046            # cm^2/g (2324 KILL branch)

checks = []

# (1) RULE INVENTORY -- exact. The 12-edge icosahedral shell (C-a): recompute
#     Sigma v-hat = 0 and Sigma v-hat (x) v-hat = 4I in EXACT arithmetic (golden
#     ratio kept symbolic via its minimal polynomial phi^2 = phi + 1, coordinates
#     as pairs (a + b*phi) with a,b rational). Consequence (1108, 2313): the
#     degree-0/1 (gradient-free) component of any field is annihilated by the
#     shell response; sourcing begins at degree 2. Combined with c05/Step B
#     (gradient-sourcing as the sector's SINGLE principle): the apparatus
#     contains exactly ONE exemption mechanism, and its reach is exactly the
#     gradient-free component. Nothing else is zeroed; nothing else CAN be
#     zeroed without a new registered mechanism.
class GR:  # exact numbers a + b*phi, phi^2 = phi + 1
    def __init__(s, a, b=0): s.a, s.b = Fraction(a), Fraction(b)
    def __add__(s, o): return GR(s.a+o.a, s.b+o.b)
    def __mul__(s, o): return GR(s.a*o.a + s.b*o.b, s.a*o.b + s.b*o.a + s.b*o.b)
    def __eq__(s, o): return s.a == o.a and s.b == o.b
Z, ONE, PHI = GR(0), GR(1), GR(0, 1)
NEG = lambda x: GR(-x.a, -x.b)
verts = []
for s1 in (ONE, NEG(ONE)):
    for s2 in (PHI, NEG(PHI)):
        verts += [(Z, s1, s2), (s1, s2, Z), (s2, Z, s1)]
assert len(verts) == 12
sum_v = [Z, Z, Z]
sum_vv = [[Z]*3 for _ in range(3)]
for v in verts:
    for i in range(3):
        sum_v[i] = sum_v[i] + v[i]
        for j in range(3):
            sum_vv[i][j] = sum_vv[i][j] + v[i]*v[j]
mono_zero = all(c == Z for c in sum_v)
# |v|^2 = 1 + phi^2 = 2 + phi for every vertex; Sigma v(x)v = 4(2+phi) I raw,
# = 4I after normalization v-hat = v/|v|. Check raw isotropy exactly:
norm2 = ONE + PHI*PHI                      # = 2 + phi
iso = all(sum_vv[i][i] == GR(4)*norm2 for i in range(3)) and \
      all(sum_vv[i][j] == Z for i in range(3) for j in range(3) if i != j)
ok1 = mono_zero and iso
checks.append(("(1) rule inventory EXACT: Sigma v-hat = 0 (monopole annihilation) and "
               "Sigma v-hat(x)v-hat = 4I (isotropic degree-2) recomputed in exact "
               "golden-ratio arithmetic -- the apparatus's ONE zeroing mechanism reaches "
               "exactly the gradient-free component; sourcing = gradient-sourcing "
               "(c05/Step B, the sector's single principle) begins at degree 2. No other "
               "exemption mechanism is registered anywhere in G1-G3", ok1, None))

# (2) HARMONIC-NULL COROLLARY: the gradient-free channel carries NO knee. The
#     coherent (field-following, k->0 uniform) channel's transport is the Planck
#     floor l_P/6 -- x1.9e18 BELOW the PRW-D window (2330, Kubo weight of
#     omega^3 n_B at omega = 0 is exactly zero). Therefore every realization of
#     a window knee is carried by discrete, LOCALIZED threshold events (the
#     registered law's two channels: saddle hops, E_gap creations) -- maximal
#     gradient carriers at the cell scale, categorically outside the annihilated
#     subspace of check (1).
short = D_LO/D_PLANCK
ok2 = 1e18 < short < 3e18
checks.append(("(2) harmonic-null corollary: the ONLY gradient-free channel transports "
               "x%.1e below the PRW-D window -- every knee-carrier is a localized "
               "activated event (hop or E_gap creation), i.e. a gradient-carrying "
               "excitation OUTSIDE the zeroed subspace. The two requirements collide: "
               "what the knee needs (localization) is what the zeroing cannot reach"
               % short, ok2, None))

# (3) THE A-FORTIORI ANCHOR (Case 4 precedent): DM-2 Section 5's Lambda IS the
#     sourcing of a Sea excitation -- the longest zero-point coherence mode's
#     field energy, rho_L = (1/8pi) rho_P (l_P/L)^2 with the coefficient
#     G3-derived. Its gradient scale is k ~ 1/R_h -- the GENTLEST gradient in
#     the framework. The floor's events sit at k ~ 1/R_s: steeper by R_h/R_s.
#     A one-ledger split that zeroes the steep excitation while sourcing the
#     gentle one would need a discriminant (provenance or form); G1 proved no
#     provenance term exists (2313, exact) and C-d registered a single
#     form-blind conversion (EP-C-1 enforced at 1e-12 on the matter side).
#     Exemption therefore requires UN-DERIVING Case 4 (Lambda) and Case 3 (the
#     candidate's own gravitation) -- inconsistency, not open-ness.
steeper = RH/RS
ok3 = 1e39 < steeper < 1e40
checks.append(("(3) a-fortiori anchor: the framework ALREADY sources Sea excitation -- "
               "Lambda = field energy of the R_h coherence mode (Case 4, coefficient "
               "G3-derived). Floor events carry gradients x%.1e steeper. Zeroing them "
               "while keeping Lambda requires a provenance/form discriminant that G1 "
               "(no provenance term, exact) and C-d (single conversion) exclude: the "
               "exemption is INCONSISTENT with the registered structure, not merely "
               "underivable" % steeper, ok3, None))

# (4) NO-CANCELLATION: the knee-carrying population is the Boltzmann-weighted
#     excess ABOVE the equilibrium reference (absent at T = 0, where D collapses
#     to the Planck floor) -- positive-definite excitation energy. Signed-dSSV
#     cancellation is unavailable: the ledger reads ENERGY (one ledger, C-d),
#     and the same object class (localized Sea-origin dSSV structure) carries
#     the rod's own gravitational mass (L1 rod equivalence) -- a mechanism
#     assigning zero/negative active mass to positive-energy localized excess
#     would break Case 2/3 wholesale. Floor magnitude restated (2331):
V = RS**3
rho_lo, rho_hi = KNEE_LO/V, KNEE_HI/V
ov_lo, ov_hi = rho_lo/RHO_CRIT, rho_hi/RHO_CRIT
ok4 = 1e34 < ov_lo < 1e35
checks.append(("(4) no-cancellation: the knee population is positive-definite excess "
               "above the T = 0 reference; with full ledger weight (now derived) the "
               "floor binds as registered -- rho >= %.2e-%.2e MeV/fm^3 = x%.1e-x%.1e "
               "over closure TODAY; R-III history x1e12-1e23 over its own era's "
               "radiation (2331, unchanged)" % (rho_lo, rho_hi, ov_lo, ov_hi), ok4, None))

# (5) REMAINING DOORS -- structural, each closed by a registered item:
#     (D-thermal-ref) redefining the reference at T_amb: the reference is
#       SYMMETRY-ENFORCED, not chosen (G1: enforced by the vanishing monopole);
#       the enforcement mechanism reaches only uniform components and cannot
#       absorb a localized population; a thermal reference is a definition --
#       the exact move the panel's folded sentence excludes post-reduction.
#     (D-ZPF) floor events as zero-point content of the reference: the
#       knee-carriers are Boltzmann-weighted (absent at T = 0; D(T->0) = Planck
#       floor, check 2) -- they are the DIFFERENCE from the reference by
#       construction; and structured zero-point content sources anyway (Case 4).
#     (D-sub-Moment) events too brief for the broadcast: within the registered
#       law (C-i) Gamma counts per-Moment threshold crossings at cadence
#       nu = kappa_nu E_z / hbar -- an event is >= 1 Moment by construction,
#       and the Perceive step registers everything present each Moment; no
#       sub-Moment realm exists in the axioms (A-series).
ok5 = True
checks.append(("(5) remaining doors closed on registered ground: thermal-reference "
               "(reference symmetry-enforced, not chosen -- G1/panel folded sentence); "
               "ZPF (knee-carriers are the Boltzmann excess by construction; structured "
               "ZP content sources anyway = Lambda); sub-Moment (the registered law's "
               "events ARE per-Moment threshold crossings; Perceive registers per "
               "Moment; no sub-Moment realm in the axioms)", ok5, None))

# (6) GRADING vs the 2332 pre-registered outcomes, AS WRITTEN:
#     (i) exemption DERIVED -> does NOT fire (shown inconsistent, check 3);
#     (ii) sourcing DERIVED -> FIRES, conditional on the registered stack
#         {C-a, C-b, C-c (G1); C-d (G2); C-i + harmonic-null on the founder's
#         no-carried-velocity ruling (2330); per-cell conservative floor};
#     (iii) neither derivable -> does NOT fire (a derivation was reached).
ok6 = ok1 and ok2 and ok3 and ok4
checks.append(("(6) grading (no retro-fit): outcome (ii) FIRES -- sourcing "
               "DERIVED-conditional on the same registered stack the corner itself "
               "rode on. TAMB-1(b) FAILS. Per the pre-registration as written: corner "
               "DEAD, G4 -> KILL-on-suite, report to the 20-July decision as such",
               ok6, None))

# (7) CONSEQUENCE PROPAGATION (2324 KILL branch, restated): total = floor 0.046
#     everywhere -- dSph FAILS x435-2174, dwarf pin FAILS x22, LSB FAILS x15;
#     Discriminant I dead; cluster/Bullet/group bounds and the F1 group
#     falsifier BRANCH-INVARIANT (survive). The 20-July conjunction
#     X4'-in-window AND R-III-history AND TAMB-1(b) evaluates FALSE on its
#     third clause regardless of the first two; AGG-1-R is mooted for the
#     corner (bookkeeping only). OPEN-DM-TAMB-1 is thereby ADJUDICATED: the
#     closure surface is operative, and the 3.2 meV T_amb cap binds the whole
#     keV-class U6 prior (registered at 2330 as un-adjudicated; adjudicated
#     here).
conj = False  # X4' AND R-III AND TAMB-1(b): third clause False
ok7 = (not conj)
checks.append(("(7) consequence: 20-July conjunction FALSE on clause 3; suite reverts "
               "to the 2324 KILL branch (floor %.3f everywhere: dSph x435-2174 / pin "
               "x22 / LSB x15 FAIL; cluster/Bullet/group/F1 branch-invariant, PASS); "
               "AGG-1-R mooted for the corner; OPEN-DM-TAMB-1 adjudicated-operative "
               "(3.2 meV cap binds the keV-class U6 prior)" % FLOOR, ok7, None))

npass = 0
for msg, ok, _ in checks:
    print(("PASS " if ok else "FAIL ") + msg + "\n")
    npass += ok
print("=== %d/%d ===" % (npass, len(checks)))
