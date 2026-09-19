"""
TEST-A3G-7: nucleon magnetic moments, with A_i supplying S-hat.
Targets OPEN-SS-8 / PRED-O-14 (mu_p = +2.793 mu_N, mu_n = -1.913 mu_N, still 'to derive').
"""
import numpy as np
q_u, q_d = 2/3, -1/3
obs_p, obs_n = 2.793, -1.913

print("="*70); print("STEP 1 - what the amendment makes POSSIBLE"); print("="*70)
print("""  OPEN-SS-8's route is 'compute <L-hat + 2 S-hat> ... apply SU(6)'. Before the
  A3' amendment CPP had NO spin operator (founder, 4107: 'we had not assigned a
  spin to any CP'), so this line could not even be written down. A_i supplies
  S-hat. The nucleon is a ground state, L = 0, so <L-hat> = 0 and the whole
  moment is the spin term -- exactly the half A_i provides (Patch 4112).""")

print("\n"+"="*70); print("STEP 2 - the SU(6) ratio (structure only, zero parameters)"); print("="*70)
mu_p_s = (4*q_u - q_d)/3     # in units of mu_0 = e hbar / (2 m_q c)
mu_n_s = (4*q_d - q_u)/3
print(f"  mu_p = (4 mu_u - mu_d)/3 = {mu_p_s:+.4f} mu_0")
print(f"  mu_n = (4 mu_d - mu_u)/3 = {mu_n_s:+.4f} mu_0")
print(f"  ratio = {mu_p_s/mu_n_s:+.4f}   observed {obs_p/obs_n:+.4f}   "
      f"error {abs((mu_p_s/mu_n_s)/(obs_p/obs_n)-1):.2%}")

print("\n"+"="*70); print("STEP 3 - normalisation from the cage (zero parameter)"); print("="*70)
print("""  mu_0 = e hbar / (2 m_q c) needs an effective quark mass. The CPP cage holds
  THREE quarks bound into the nucleon, so the zero-parameter assignment is
  m_q = M_N / 3, giving mu_0 = 3 mu_N.""")
mu0 = 3.0
pred_p, pred_n = mu_p_s*mu0, mu_n_s*mu0
print(f"\n  PREDICTED   mu_p = {pred_p:+.3f} mu_N     mu_n = {pred_n:+.3f} mu_N")
print(f"  OBSERVED    mu_p = {obs_p:+.3f} mu_N     mu_n = {obs_n:+.3f} mu_N")
print(f"  error              {abs(pred_p/obs_p-1):.1%}                {abs(pred_n/obs_n-1):.1%}")

print("\n"+"="*70); print("STEP 4 - what the implied mass would have to be"); print("="*70)
print(f"  matching mu_p exactly requires m_q = M_N/{obs_p:.3f} = 0.358 M_N")
print(f"  the cage's zero-parameter value is    m_q = M_N/3     = 0.333 M_N")
print(f"  discrepancy in m_q: {abs(0.3333/0.358-1):.1%}")

print("""
======================================================================
A3G-7 VERDICT -- a genuine zero-parameter postdiction, 4-7%
======================================================================
  ratio  mu_p/mu_n : -1.500 vs -1.460 observed   -> 2.7%, NO parameters
  mu_p             : +3.000 vs +2.793            -> 7.4%
  mu_n             : -2.000 vs -1.913            -> 4.5%

  This is the FIRST positive empirical result the amendment has produced.
  All three numbers come out with no fitting: the SU(6) structure supplies the
  ratio, and m_q = M_N/3 from the cage supplies the scale.

  HONEST LIMITS, and they matter:
   1. The SU(6) ratio is NOT new physics -- any theory with quark spin gets it.
      What the amendment contributes is that CPP can now WRITE IT DOWN at all;
      before 4120 there was no S-hat in the corpus. That is a real gain but it
      is an enabling gain, not a novel prediction.
   2. m_q = M_N/3 is the NAIVE cage assignment, not a cage calculation. A true
      <L-hat + 2 S-hat> evaluation over the icosahedral/dodecahedral cage
      geometry is what OPEN-SS-8 actually asks for and is NOT done here.
      The 7.4% gap is where that calculation would have to do its work.
   3. So OPEN-SS-8 is ADVANCED, not closed, and PRED-O-14 stays 'to derive'.""")
