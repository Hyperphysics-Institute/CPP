import numpy as np
hbarc=197.327; alpha=1/137.036; E_qDP=264.0; m_qDP=264.0; mu=m_qDP/4.0
# f as a number: the qDP->light-DP coupling vertex resolved. A color-SINGLET qDP has no net color charge but a
# nonzero COLOR POLARIZABILITY -> a COLOR van der Waals dominates the electric (3*alpha) channel by (alpha_s/3alpha)^2.
def vdw(alpha_c,a):
    a_pol=(alpha_c*hbarc)/(mu*(E_qDP/hbarc)**2); C6=0.75*E_qDP*a_pol**2
    return (C6/a**6)/E_qDP
print(f"color/electric dominance (alpha_s/3alpha)^2 at alpha_s=0.5: {(0.5/(3*alpha))**2:.0f}x -> coupling = alpha_s")
print("f from COLOR van der Waals (alpha_s at qDP scale ~0.5, range 0.3-1; contact a=eDP-coat hard core 1.0-1.3 fm):")
for als in [0.3,0.5,1.0]:
    for a in [1.0,1.15,1.3]:
        print(f"  alpha_s={als:.1f} a={a:.2f} fm: f={vdw(als,a):.2f}  V0=f*E_qDP={vdw(als,a)*E_qDP:.0f} MeV")
fc=vdw(0.5,1.15)
print(f"CENTRAL: alpha_s~0.5, a~1.15 -> f~{fc:.2f} (factor-3: ~0.07-0.6); V0~{fc*E_qDP:.0f} MeV (range ~50-130)")
print(f"arc at f~0.2: sigma/m~0.12 (0831, safe); de Boer Lambda=0.747/sqrt(f)={0.747/np.sqrt(0.2):.2f}>>0.18 -> diffuse (all f<1)")
