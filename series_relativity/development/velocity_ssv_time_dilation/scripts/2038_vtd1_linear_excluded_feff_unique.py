import numpy as np
# The founder-confirm question, made decidable by computation:
# Does the budget cost go as the LINEAR fraction v/c, or the QUADRATURE fraction f_eff = 1 - 1/gamma?
# SR-1's exact time-dilation gamma = 1/sqrt(1-v^2/c^2) is EXTERNALLY VALIDATED (A- review, App.H).
# So the test is: which reading reproduces that already-validated gamma, and is it UNIQUE?
print("v/c   gamma     internal-rate REQUIRED (=1/gamma)   LINEAR gives   QUADRATURE/f_eff gives")
linear_ok = quad_ok = True
for b in [0.1,0.3,0.6,0.8,0.9,0.99]:
    g = 1/np.sqrt(1-b**2)
    need = 1/g                       # validated time dilation => internal clock rate must be 1/gamma
    linear_internal = 1 - b          # collinear consumption
    quad_internal   = np.sqrt(1-b**2)# orthogonal remainder = 1 - f_eff, f_eff = 1-1/gamma
    if abs(linear_internal-need)>1e-9 and b>0.05: linear_ok=False
    if abs(quad_internal -need)>1e-12:            quad_ok=False
    print(f"{b:4.2f}  {g:7.4f}   {need:7.5f}                       {linear_internal:7.5f}        {quad_internal:7.5f}")
print()
print("LINEAR reproduces validated gamma? ", linear_ok, " -> gamma_linear = 1/(1-v/c), a DIFFERENT, FALSIFIED factor")
print("QUADRATURE/f_eff reproduces it?    ", quad_ok)
print()
# Uniqueness: demand internal-rate = 1/gamma (the validated datum). Solve for consumed fraction f.
# internal = 1 - f  AND  internal = 1/gamma  =>  f = 1 - 1/gamma = f_eff.  Unique, no free choice.
print("Uniqueness: internal = 1 - f  and validated internal = 1/gamma  =>  f = 1 - 1/gamma = f_eff (forced).")
print("=> Given SR-1's externally-validated exact gamma, the consumed fraction is UNIQUELY f_eff.")
print("   The linear reading is not a competing option; it is EXCLUDED (wrong gamma).")
