#!/usr/bin/env python3
"""4268 -- m_q audit (TODO-4234-DELTA item (iii)).
Route (H) works in units m_q c: the breath's momentum spread per mode is fixed in those units (omega = m_q c^2/hbar,
4266), so R_u, R_d -- and g_A -- do not depend on m_q.  m_q enters only the moments, mu = (M_N/m_q) x S.
So the g_A residual (+2.7%) and the mu_p deficit (-4.2%) are separate: m_q can fix mu_p, never g_A.
Take the ruled-picture state (4262: founder mode set, u-u exchange): R_u = 0.7781, R_d = 0.8162.
(1) m_q = m_p/3 as SS-2 assigns; (2) m_q fitted to mu_p alone -> mu_n becomes a prediction; (3) g_A unchanged."""
import numpy as np
MN=938.919; gA_t,mup_t,mun_t=1.2754,2.79285,-1.91304
Ru,Rd=0.7781,0.8162; Su,Sd=(1+Ru)/2,(1+Rd)/2
def mom(mq): x=MN/mq; return (4*(2/3)*x*Su+(1/3)*x*Sd)/3,(4*(-1/3)*x*Sd-(2/3)*x*Su)/3
gA=4/3*Ru+Rd/3
def row(lab,mq):
    mp,mn=mom(mq); print(f"  {lab:42s} m_q={mq:6.1f} MeV  g_A={gA:.4f} ({100*(gA/gA_t-1):+4.1f}%)  mu_p={mp:.3f} ({100*(mp/mup_t-1):+5.1f}%)  mu_n={mn:.3f} ({100*(mn/mun_t-1):+5.1f}%)  mu_n/mu_p={mn/mp:.4f} (meas {mun_t/mup_t:.4f})")
row("(1) SS-2: m_q = m_p/3 (assigned, M9)",938.272/3)
mq_fit=938.272/3*mom(938.272/3)[0]/mup_t
row("(2) m_q fitted to mu_p",mq_fit)
x=MN/(938.272/3); print(f"  NRQM reference (R_u = R_d = 1, m_q = m_p/3): mu_p = {x*(4*2/3+1/9)/3:.3f}, g_A = 1.6667 (SS-2's 2.789 used m_u, m_d = 336, 340)")
print("\n-> g_A is m_q-independent: its +2.7% is a residual of the motion, not of the mass.  Fitting m_q to mu_p (1 number)")
print("   leaves mu_n as a prediction (-1.5%); the ratio mu_n/mu_p, which no m_q can change, is -1.5% off as well.")
