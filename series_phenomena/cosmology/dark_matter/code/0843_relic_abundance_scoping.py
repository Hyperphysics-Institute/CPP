# Scoping the 5:1: asymmetric-DM bookkeeping Omega_DM/Omega_b = (m_DM/m_p)(n_DM/n_b) = 5.36
m_p=0.938; target=5.36
print("Route B (asymmetric DM) required n_DM/n_b for Omega_DM/Omega_b=5.36:")
for lbl,m in [("single qDP (0.264)",0.264),("single hTetra (~0.79)",0.792),("~5 m_p aggregate (4.7)",4.69)]:
    print(f"  {lbl:24s}: n_DM/n_b = {target*m_p/m:.2f}")
print("n_DM~n_b (shared asymmetry) needs m_DM~4.7 GeV (heavy aggregate); single qDP needs n_DM~19 n_b.")
print("Neither m_DM (aggregate mass, Project-C-adjacent) nor n_DM/n_b (production history) derived -> 5.36 NOT a first-pass derivation.")
