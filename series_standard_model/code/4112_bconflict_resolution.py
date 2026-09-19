"""
TODO-4111-BCONFLICT: does Option B's axial channel A_i DOUBLE-COUNT SF-6's magnetism?

SF-6 derives B as the CURL of a polar displacement -> that is the ORBITAL (L-hat) part.
Option B's A_i would be the SPIN (S-hat) part.
OPEN-SS-8's own stated solution: "Compute <L-hat + 2 S-hat>_ZBW ... apply SU(6) formula."
So the corpus ALREADY says both are needed. Test whether orbital alone could suffice.
"""
import numpy as np

print("="*70)
print("T1  the nucleon ground state has L = 0, so ORBITAL contributes NOTHING")
print("="*70)
print("""  p and n are ground-state (1s) baryons: total quark orbital angular momentum
  L = 0. In <L-hat + 2 S-hat>, the <L-hat> term is therefore ZERO and 100% of
  the moment is the spin term. A curl-of-displacement (orbital) channel cannot
  supply ANY of it.""")

print("\n"+"="*70)
print("T2  SU(6) spin-only prediction vs experiment")
print("="*70)
# SU(6) wavefunction result: mu_p = (4 mu_u - mu_d)/3 , mu_n = (4 mu_d - mu_u)/3
# quark moments are SPIN moments, mu_q proportional to charge q
q_u, q_d = 2/3, -1/3
mu_u, mu_d = q_u, q_d                      # in units where mu_q ~ q (equal quark masses)
mu_p = (4*mu_u - mu_d)/3
mu_n = (4*mu_d - mu_u)/3
print(f"  SU(6):  mu_p ~ {mu_p:+.4f},  mu_n ~ {mu_n:+.4f},  ratio = {mu_p/mu_n:+.4f}")
obs_p, obs_n = 2.793, -1.913
print(f"  observed ratio mu_p/mu_n = {obs_p/obs_n:+.4f}")
err = abs((mu_p/mu_n)-(obs_p/obs_n))/abs(obs_p/obs_n)
print(f"  agreement: {err:.1%}  -- the classic SU(6) success, and it is PURELY a SPIN result")
assert err < 0.05

print("\n"+"="*70)
print("T3  could a curl-of-displacement (orbital) channel reproduce that ratio?")
print("="*70)
print("""  An orbital moment goes as q*L/(2m). With L = 0 in the ground state the
  prediction is mu_p = mu_n = 0 and the ratio is undefined. There is no choice
  of orbital dynamics that yields -1.46 from L = 0.""")
print(f"  orbital-only prediction: mu_p = 0, mu_n = 0, ratio undefined")
print(f"  observed:                mu_p = {obs_p:+.3f}, mu_n = {obs_n:+.3f}")
print("  => orbital magnetism CANNOT be the source. T3 decisive.")

print("\n"+"="*70)
print("VERDICT ON TODO-4111-BCONFLICT")
print("="*70)
print("""  NO DOUBLE-COUNT. The two axial objects are physically distinct halves of
  one operator that the corpus already names:

        <L-hat + 2 S-hat>       (OPEN-SS-8's own solution statement)
          |          |
          |          +-- Option B's A_i   (SPIN magnetism)  -- MISSING today
          +------------- SF-6's curl V    (ORBITAL magnetism) -- present today

  Far from being a risk, Option B supplies the half that a registered HIGH
  priority open problem (OPEN-SS-8) and a registered prediction (PRED-O-14)
  are both blocked on -- and for the nucleon ground state it is the ONLY
  half that contributes.

  SIDE FINDING: OPEN-SS-8 lists "Dependencies: None blocking". That is wrong.
  It is blocked on a spin attribute CPP does not have (founder, 4107: "we had
  not assigned a spin to any CP, whether ZBW or not").""")
