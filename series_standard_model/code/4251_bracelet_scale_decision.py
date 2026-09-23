#!/usr/bin/env python3
"""4251 -- the W0 bracelet's working physical size, decided under the founder's delegation (founders_voice/4251:
"choose a size that produces the right answer ... calibrate and triangulate"). Candidates: (i) 4229's hbar c/m_W;
(ii) the 600-cell reading, r_B = 0.58779 (SF-2 Thm W bracelet, circumradius units) x l_unit = 0.589 fm (SS-2).
Five constraints on file are checked against both; then 4231's kick bound and 4233's rate budget are recomputed."""
import math
hbarc=197.327; a_hc=1.43996; m_e,m_W,m_const=0.510999,80379.0,313.0
cands={'(i) Compton':hbarc/m_W,'(ii) 600-cell':0.58779*0.589}
r_orb=hbarc/m_const
print(f"{'constraint':62s} {'(i) 0.0025 fm':>16s} {'(ii) 0.346 fm':>16s}")
def row(name,f,ok):
    v=[f(r) for r in cands.values()]; print(f"{name:62s} {v[0]:>16s} {v[1]:>16s}")
row("C1 one lattice: bracelet at SS-2's l_unit (no second scale)",lambda r:"needs 2nd scale" if r<0.01 else "yes",None)
row("C2 SF-2 Delta E_centroid = O(m_e): ring well alpha hbar c / r_B",lambda r:f"{a_hc/r:.0f} MeV",None)
row("C3 trap beats the core's pull at d ~ r_B: (2/3) alpha hbar c / r_B",lambda r:f"{a_hc/r:.0f} vs {(2/3)*a_hc/r:.0f} MeV",None)
row("C4 linear -eCP oscillation (0.105 fm) inside the ring (held, 4247/4248)",lambda r:"no (43x ring)" if r<0.105 else f"yes ({0.105/r:.2f} r_B)",None)
row("C5 NC occupancy f = 1 (4246/4247)",lambda r:"only if held" if r<0.105 else "yes",None)
print("\nDECISION (worker, PD-006 under the founder's 4251 delegation): (ii) r_B = 0.346 fm -- G-EW-BRACELETSCALE-4251, working value.")
print("  (i) fails C1 and C2 outright and C4/C5 unless the trap is assumed; (ii) meets all five with no new scale introduced.\n")
rB=cands['(ii) 600-cell']
print("consequences, recomputed:")
print(f"  4231 kick bound: max |dL|/L = r_kick/r_orb.  At the pocket 0.0025 fm: {hbarc/m_W/r_orb:.1e} (0.4%).  If the kick can land anywhere")
print(f"  inside the ring: {rB/r_orb:.2f} (55%) -- the geometric guarantee of B = +1 is LOST; L-preservation must come from the")
print(f"  reset happening at the ring's zero-gradient CENTRE (lever arm << r_B) or from the pair state (4223/4228). Re-owed.")
hbar_MeVs=6.582119569e-22; G_F=1.1663788e-11; Vud2=0.9737**2; lam=-1.2754; D=1+3*lam*lam; f=1.6887
Gamma=G_F**2*Vud2*D*f*m_e**5/(2*math.pi**3); P=2*math.pi*Gamma/m_const
shape=(m_e/m_W)**4*(m_e/m_const)
for lab,r in cands.items():
    hit=2*r/(2*math.pi*r_orb); rest=P/hit
    print(f"  4233 budget at {lab:14s}: pole-in-ring per cycle = {hit:.2e};  (W0 present, aligned) x (outward) = {rest:.2e} = {rest/shape:.2e} x (m_e/m_W)^4 (m_e/m_const)")
print("  -> at 0.346 fm the ring is crossed on 18% of circulations, so the whole 1.4e-26 per cycle sits in (W0 present) x (outward):")
print("     the (E/m_W)^2 bracelet-formation target of 4233 stands, its O(1) coefficient changes from 4.4 to 0.03. Re-owed with the target.")
