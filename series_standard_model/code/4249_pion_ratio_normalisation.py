#!/usr/bin/env python3
"""4249 -- TODO-4222-CRITIC item (iii): does the ejection rule imply (1-beta) or (1-beta^2) in pi -> l nu?
Answer: (1-beta). The rule's wrong-helicity probability (1-beta)/2 = (E-p)/(2E) = m^2/(2E(E+p)) IS the squared
chirality-helicity overlap. 4215's 0.70 came from multiplying that per-particle probability by phase space p alone;
a rate carries the two outgoing states' normalisation 2E_l * 2E_nu as well. With it, the model equals the SM tree ratio
exactly, because E_l + p_l = m_pi in the two-body decay."""
mpi,mmu,me=139.570,105.658,0.511
def kin(m): p=(mpi**2-m**2)/(2*mpi); E=(mpi**2+m**2)/(2*mpi); return p,E,p/E
rows=[]
for lab,m in [("mu",mmu),("e",me)]:
    p,E,b=kin(m); P=(1-b)/2
    rows.append((lab,p,E,b,P,p*P,p*P*2*E*2*p))
    print(f"{lab:3s}: p={p:7.3f} E={E:8.3f} beta={b:.6f}  (1-beta)/2={P:.4e} = m^2/(2E(E+p))={m*m/(2*E*(E+p)):.4e}   E+p={E+p:.3f} (= m_pi)")
sm=(me**2/mmu**2)*((mpi**2-me**2)/(mpi**2-mmu**2))**2
r4215=rows[1][5]/rows[0][5]; rnew=rows[1][6]/rows[0][6]
print(f"\n4215 form  p*(1-beta)/2:               e/mu = {r4215:.4e}   /SM tree = {r4215/sm:.3f}")
print(f"with 2E_l 2E_nu normalisation:         e/mu = {rnew:.4e}   /SM tree = {rnew/sm:.6f}   (SM tree {sm:.4e}; measured 1.230e-4)")
print(f"(1-beta^2) alternative, same normalisation: e/mu = {(rows[1][1]**3*(1-rows[1][3]**2)*rows[1][2])/(rows[0][1]**3*(1-rows[0][3]**2)*rows[0][2]):.4e}  -> {(rows[1][1]**3*(1-rows[1][3]**2)*rows[1][2])/(rows[0][1]**3*(1-rows[0][3]**2)*rows[0][2])/sm:.3f} x SM: excluded")
print("\n-> the rule implies (1-beta); the SM's m^2 IS (1-beta)/2 x 2E_l x 2E_nu; the 0.70 of 4215 was the omitted normalisation, not a discrepancy.")
