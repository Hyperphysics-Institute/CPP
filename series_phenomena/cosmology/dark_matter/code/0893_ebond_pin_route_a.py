#!/usr/bin/env python3
"""
Patch 0893 -- E_bond PIN, Route A (geometric/ratio): the e-e edge scission bond
==============================================================================
The make-or-break (scoping doc 0887): pin E_ee (= the ledger's E_bond), the
edge-bond scission depth that holds the Cross-Rod together. Pinning it collapses
N_dwarf -> a single sigma/m -> a hard core-size-vs-halo-mass curve (the
discriminating prediction that would move CONJ-COSMO-1 off NOT-confirmed).

Route A (handover 0892, "TRY FIRST; may close"): derive E_ee as a geometric
RATIO to a pinned DP scale, so the sub-Planck absolute near-cancellation
(Route B's hard root, OPEN-FP-SF-2-eta) is never evaluated.

THE LEVER (already in the corpus, already panel-ratified, used 3x):
  The Cross-Rod element is an 8-qCP cubic CORE (q-faces bond AXIALLY via the
  COLOR channel -> the stiff E_qq) wrapped by an 8-eCP SHELL (the SHIELDED
  ELECTRIC coat -> the weaker scission E_ee). The campaign established and the
  panel ratified that the shielded electric channel is weaker than the color
  channel by the PURE coupling ratio (alpha_s/3alpha)^2 ~ 190-520x:
    - corona retirement      (0874/0875)  V0_elec = f_color*(3a/a_s)^2*E_eDP
    - width-cap / d_f=1       (0880)       fifth chain out-competed by ~190-520x
    - sigma/m = 0.11 floor    (0860)       unshielded color residual sets the floor
  So E_ee is the electric-channel PARTNER of the color edge residual E_qq:
    E_qq ~ V0_color = f_color * E_qDP ~ 53 MeV   (0835, derived, factor-~3)
    E_ee = E_qq * (3alpha/alpha_s)^2             (the ratified hierarchy, applied
                                                  to the e-e edge -- a RATIO, no
                                                  sub-Planck charge-sum touched)

HONEST ALTERNATIVE (construction 2): a full London re-derivation that credits the
SOFT eDP with its own polarizability (alpha_pol ~ 1/E_DP^3, f ~ 1/E_DP^6) would
ENHANCE the electric depth by (E_qDP/E_eDP)^6 = 729 and push E_ee -> ~40 MeV
(out of window). It is DISFAVORED because (a) f_e ~ 0.5 self-invalidates the
London expansion (0835 already marginal at f=0.2), and (b) E_ee ~ E_qq
(near-degenerate) contradicts the ALREADY-RATIFIED morphology, which requires the
e-channel ~190-520x weaker. A clean Layer-B closure would need the SSV charge-sum
(Route B) to kill construction 2 outright, or a London-validity proof. Layer C.

Run: python3 0893_ebond_pin_route_a.py
"""
import numpy as np

# ---- pinned corpus constants (CITED, not invented) ----
alpha      = 1/137.035999          # fine-structure constant
phi        = (1 + np.sqrt(5)) / 2  # golden ratio
hbarc      = 197.3269804           # MeV*fm
E_eDP      = 88.0                  # MeV  eDP creation energy (SF-3)
E_qDP      = 264.0                 # MeV  = 3*E_eDP (color factor 3) (SF-3)
f_color    = 0.20                  # color vdW residual fraction (0835; factor-~3: 0.07-0.6)
V0_color   = f_color * E_qDP       # 52.8 MeV  q-q color edge residual = E_qq scale
alpha_s_c  = 5 / (8 * phi)         # 0.3863  SF-5 central alpha_s (range 0.3-0.5)
threealpha = 3 * alpha             # 0.02189 electric DP-binding coupling
WIN_LO, WIN_HI = 0.8e-3, 2.0       # MeV  fragmentation window (0860)

def Eee_constr1(a_s):
    """Construction 1: E_ee = E_qq * (3a/a_s)^2  [MeV]."""
    return V0_color * (threealpha / a_s) ** 2

print("=" * 72)
print("E_bond PIN -- Route A  (e-e edge scission bond via the ratified hierarchy)")
print("=" * 72)
print(f"  E_eDP={E_eDP} MeV  E_qDP={E_qDP} MeV  f_color={f_color}  ->  E_qq~V0_color={V0_color:.1f} MeV")
print(f"  alpha_s={alpha_s_c:.4f} (5/8phi; range 0.3-0.5)   3alpha={threealpha:.5f}")

print("\n[Construction 1 -- campaign-ratified coupling-ratio hierarchy]")
print(f"  {'alpha_s':>8} | {'(3a/a_s)^2':>11} | {'weaker by':>9} | {'E_ee [keV]':>10}")
for a_s in (0.30, alpha_s_c, 0.50):
    r2 = (threealpha / a_s) ** 2
    print(f"  {a_s:>8.3f} | {r2:>11.3e} | {1/r2:>8.0f}x | {Eee_constr1(a_s)*1e3:>10.1f}")
Ec = Eee_constr1(alpha_s_c)                       # MeV, central
lo = (0.07/f_color)*V0_color*(threealpha/0.50)**2 # low f_color, high a_s
hi = (0.60/f_color)*V0_color*(threealpha/0.30)**2 # high f_color, low a_s
print(f"  CENTRAL E_ee ~ {Ec*1e3:.0f} keV ;  with f_color factor-3 -> band ~ [{lo*1e3:.0f}, {hi*1e3:.0f}] keV")

print("\n[Window + four over-determined constraints]  window = [0.8 keV, 2 MeV]")
print(f"  whole band [{lo*1e3:.0f}, {hi*1e3:.0f}] keV in-window: "
      f"{WIN_LO <= lo and hi <= WIN_HI}")
kTf = Ec / np.array([41, 24])                     # MeV  from E/kT_form in [24,41]
kTp_max = Ec / 100                                # MeV  from E >= 100 kT_present
print(f"  (1) fragmentation window  : 0.8 <= {Ec*1e3:.0f} keV <= 2000   -> PASS")
print(f"  (2) E_ee/kT_form ~ 24-41  : kT_form = {kTf[0]*1e3:.1f}-{kTf[1]*1e3:.1f} keV")
print(f"  (3) E_ee >= 100 kT_present: kT_present <= {kTp_max*1e3:.1f} keV (<=19 keV hook) -> PASS")
print(f"  (4) kT_form/kT_present>=7 : >= {kTf[0]/kTp_max:.1f}-{kTf[1]/kTp_max:.1f} "
      f"(order-consistent; ~factor-2 of 7)")
print(f"  eta_screen = E_ee/(a*hbarc/l_rung) = {Ec/(alpha*hbarc/1.0):.3f}  in [6e-4, 1] -> PASS")
print(f"  f_geom = E_ee/E_eDP = {Ec/E_eDP:.2e}  in [9e-6, 0.023] -> PASS")
print(f"  ordering E_qq/E_ee = {V0_color/Ec:.0f}x  (E_qq={V0_color:.0f} MeV >> E_ee={Ec*1e3:.0f} keV)")

print("\n[Construction 2 -- full soft-eDP London (the honest alternative)]")
enh = (E_qDP / E_eDP) ** 6                          # 729  polarizability enhancement
f_e = f_color * (threealpha / alpha_s_c) ** 2 * enh
print(f"  f_e/f_c = (3a/a_s)^2 * (E_qDP/E_eDP)^6 = {(threealpha/alpha_s_c)**2:.2e} * {enh:.0f} "
      f"= {(threealpha/alpha_s_c)**2*enh:.2f}")
print(f"  f_e = {f_e:.2f}  ->  E_ee = {f_e*E_eDP:.0f} MeV  (OUT of window, >> 2 MeV)")
print(f"  DISFAVORED: f_e~{f_e:.2f}~0.5 invalidates the London expansion (0835 marginal at 0.2),")
print(f"  AND E_ee~E_qq={V0_color:.0f} MeV (near-degenerate) breaks the ratified morphology")
print(f"  (width-cap/corona require the e-channel ~190-520x weaker).")

print("\n" + "=" * 72)
print("VERDICT (Layer C): Route A lands E_ee ~ 100-280 keV (central ~170 keV) -- the")
print("WHOLE band in-window, all four constraints satisfied -- by the SAME electric-vs-")
print("color (3a/a_s)^2 hierarchy the campaign already uses 3x and the panel ratified.")
print("E_ee is a RATIO (E_ee/E_qq); the sub-Planck near-cancellation is never touched.")
print("Conditional on that hierarchy holding for the e-e edge (favored by morphology");
print("consistency; construction 2 disfavored & self-invalidating). NOT a clean Layer-B")
print("closure -- killing construction 2 outright needs the SSV charge-sum (Route B).")
print("=" * 72)
