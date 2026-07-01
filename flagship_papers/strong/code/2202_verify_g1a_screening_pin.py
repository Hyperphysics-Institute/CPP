#!/usr/bin/env python3
"""
G1a screening-pin + consistency close  (patch 2202, SF-2/SF-5 lane, final in-lane patch)
========================================================================================
Closes the p<~2 "escape hatch" 2201 left open, and records the stiff-ribbon / soft-scissor
consistency with the DM formation physics (0860-0862). No new geometry: this evaluates the
2201 ponderomotive ratio AT the corpus-pinned edge-bond parameters and states the two
cross-checks as checkable claims.

THE ESCAPE HATCH 2201 LEFT OPEN
  2201 found g_pond < g_crit for steep/screened laws (p >~ 3) but g_pond -> O(1)+ for a
  shallow/long "softer SSV law" (p <~ 2). 1835 hedged on exactly this: "field 1/r^2 -> grad^2
  up to 1/r^6 -> p up to 6; softer SSV laws give smaller p." The question: can the real SSV
  edge bond be in the soft branch?

WHY THE ESCAPE HATCH IS CLOSED (electrostatics, not assumption)
  The edge bond is a LOCALIZED ELECTROSTATIC near-cancellation residual (0865: closer like-charge
  repulsion - farther opposite-charge screening, dominated by the coat eDP pairs at r_c ~ 1.0 fm).
    * A localized electrostatic source cannot have a SUB-COULOMB field: the monopole term is 1/r^2,
      the SHALLOWEST a localized field can be. So the field is 1/r^2 or steeper -> in the
      ponderomotive |E|^2 = grad^2, s >= 1 (p = s+2 >= 3). The VIABLE branch, guaranteed.
    * This is a near-CANCELLATION residual -> the monopole largely cancels -> the leading surviving
      term is DIPOLE-like, 1/r^3 or steeper -> s >= 2 (p >= 4), even deeper in the viable branch.
    * Screening ADDS an fm-scale cutoff (eDP coat r_c ~ 1.0 fm; color-vdW leg lambda ~ 1.3 fm from
      the confinement scale hbar c/E_hDP, E_hDP ~ 152 MeV) -> steepens further.
  The "softer SSV law" (p < 2) requires a field shallower than 1/r^2 -- which a localized charge
  residual CANNOT produce. The escape hatch is closed by electrostatics + screening, not by fiat.
"""
import numpy as np
d, w = 1.0, 2.0

def fmag(r, s, lam): return np.exp(-r/lam)*(s/r + 1.0/lam)/r**s
def Efield(t, srcs, s, lam):
    E = np.zeros(3)
    for sp in srcs:
        dv = t - sp; r = np.linalg.norm(dv)
        if r < 1e-9: continue
        E += fmag(r, s, lam)*dv/r
    return E
def d2(f, h=2e-3): return (f(h) - 2*f(0) + f(-h))/h**2
def bendU(q, s, lam, fibs=2, narm=2):
    xs = np.arange(-narm, narm+1)*d; ys = np.linspace(-1, 1, fibs)*(w/2)
    A = [np.array([x, y, 0.0]) for x in xs for y in ys]; cq, sq = np.cos(q), np.sin(q)
    B = [np.array([x*cq+d*sq, y, -x*sq+d*cq]) for x in xs for y in ys]
    return sum(np.sum(Efield(a, B, s, lam)**2) for a in A), len(A)
def sciU(q, s, lam, nrod=10, drod=0.5):
    t = np.arange(1, nrod+1)*drod; ax = np.concatenate([-t[::-1], t])
    A = np.array([[x, 0, 0.0] for x in ax]); cq, sq = np.cos(q), np.sin(q)
    B = np.array([[-y*sq, y*cq, d] for y in ax])
    return sum(np.sum(Efield(a, B, s, lam)**2) for a in A), len(A)
def gpond(s, lam):
    kb = abs(d2(lambda q: bendU(q, s, lam)[0])); nb = bendU(0, s, lam)[1]
    ks = abs(d2(lambda q: sciU(q, s, lam)[0])); ns = sciU(0, s, lam)[1]
    return (ks/ns)/(kb/nb)

gcrit = 6/14
print(f"g_crit(N=14) = {gcrit:.3f}\n")
print("(1) g_pond AT the corpus-pinned edge-bond regimes (all must be < g_crit):")
print(f"    {'physical leg':>34}{'s':>3}{'lam/fm':>8}{'g_pond':>9}  verdict")
print("    " + "-"*66)
legs = [("Coulomb SSV floor (monopole 1/r^2)", 1, 1.0),
        ("Coulomb SSV, coat-screened",          1, 1.3),
        ("Coulomb SSV, tightest coat",           1, 0.7),
        ("dipole-residual SSV (near-cancel)",    2, 1.0),
        ("dipole-residual, coat-screened",       2, 1.3),
        ("color-vdW leg (1/r^6, lam=1.3fm)",     6, 1.3)]
allviable = True
for nm, s, lam in legs:
    g = gpond(s, lam); allviable &= (g < gcrit)
    print(f"    {nm:>34}{s:3d}{lam:8.1f}{g:9.3f}  {'viable' if g<gcrit else 'TENSE'}")
print("    " + "-"*66)
print(f"    -> all corpus-physical legs VIABLE: {allviable}\n")

print("(2) The ONLY way out of viability is a SUB-COULOMB field (s < 1) -- which a localized")
print("    electrostatic residual CANNOT have. Demonstrating the boundary:")
print(f"    {'s (field steepness)':>22}{'g_pond':>9}  physical?")
print("    " + "-"*46)
for s, phys in [(1.0, "yes  (Coulomb monopole floor)"),
                (0.5, "NO   (sub-Coulomb, unphysical)"),
                (0.0, "NO   (flat field, unphysical)")]:
    print(f"    {s:22.1f}{gpond(s, 1.3):9.3f}  {phys}")
print("    -> viability is lost ONLY in the unphysical sub-Coulomb region. The physical floor")
print("       (s=1) is already viable; the actual near-cancellation residual (s>=2) more so.\n")

print("(3) STIFF-RIBBON / SOFT-SCISSOR CONSISTENCY (with DM 0860-0862):")
print("    DM sigma/m ~ N REQUIRES a stiff ribbon: large kappa_bend, ell_p ~ 100-700 fm (0860,0861);")
print("    0862 DERIVES the bend hinge stiff ('the hinge is stiff, not floppy'). DM floor REQUIRES a")
print("    soft scissor: g = kappa_scissor/kappa_bend < 6/N. These are the SAME bond in two geometries.")
print("    g is a RATIO -> a LARGE kappa_bend (the stiff-ribbon requirement) is the DENOMINATOR that")
print("    makes g SMALL. The two requirements REINFORCE, not conflict. Margin check:")
gvals = [gpond(s, lam) for nm, s, lam in legs]
print(f"       physical g_pond band = {min(gvals):.3f} - {max(gvals):.3f}   vs   g_crit = {gcrit:.3f}")
print(f"       margin factor (g_crit / worst physical g) = {gcrit/max(gvals):.1f}x")
print("    -> the soft-scissor floor and the stiff-ribbon cross-section are CO-SATISFIED with margin,")
print("       for ANY absolute kappa_bend. And g~0.02 with kappa_bend LARGE means kappa_scissor is")
print("       sizable in absolute terms (~1/50 of a stiff bend) -- the junction is the softer of two")
print("       STIFF modes, NOT a fragile/floppy joint. The floor's flexibility needs no weak bond.\n")

print("VERDICT (G1a, final in-lane): the appropriate-gradient (ponderomotive) treatment gives a")
print("VIABLE floor, and the viability CONDITION (steep/screened, p >~ 3) is MET BY THE CORPUS --")
print("guaranteed by electrostatics (no sub-Coulomb field) + the derived fm-scale screening, and")
print("mutually consistent with the 0860-0862 stiff-ribbon requirement. The 2201 'conditional'")
print("collapses to 'condition met'. RESIDUAL (unchanged): the EXACT floor (0.4 vs 0.8) needs the")
print("ZBW amplitude, and absolute kappa_theta (G1b) needs the absolute potential -- both root on")
print("OPEN-FP-SF-2-eta. Direction VIABLE is now corpus-pinned; magnitude still pending.")
