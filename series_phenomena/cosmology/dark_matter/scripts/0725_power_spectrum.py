#!/usr/bin/env python3
"""
Patch 0725 verify -- DM Arc Step 4: power spectrum from "swirl" seeds.
THE MOST DISCRIMINATING STEP. Falsification-first: this is where CONJ-COSMO-1 is
most likely to break. Honest outcome below -- it is a SERIOUS TENSION, not a pass.

Two separable questions:
  (Q1, GROWTH) Given a near-scale-invariant adiabatic primordial spectrum, does the
      CPP (conditional Step-D) Friedmann background + standard gravitational growth
      reproduce the observed P(k)? -> YES (inherited; the transfer function is standard).
  (Q2, SEED ORIGIN) Do CPP's early-universe "swirl" seeds (radial-expansion collisions)
      PRODUCE a near-scale-invariant ADIABATIC spectrum? -> This is the hard part, and
      prima facie NO: swirls are a CAUSAL (active-source) mechanism, which hits the same
      observational wall that ruled out cosmic-string/defect models as the primary seed.

CHECK 1 (Q1) -- BBKS transfer function: scale-invariant seeds -> observed P(k) shape
        (rises ~k^n_s at low k, turns over at k_eq, falls ~k^(n_s-4) ln^2 k). PASS.
CHECK 2 (Q2) -- the causal-seed obstacle, quantified: the comoving particle horizon at
        recombination subtends l ~ 160; the observed CMB has correlated adiabatic power
        at l < 160 (Sachs-Wolfe plateau; the TE anti-correlation at l~100-150 is the
        textbook smoking gun for SUPER-horizon perturbations). Causal swirl seeds cannot
        produce these -> they fail as the primary structure source unless seeded acausally.
CHECK 3 -- verdict: NOT passed, NOT cleanly killed. CPP's atemporal Nexus (non-local
        coordination independent of light-cones) is a live escape standard active-source
        models lack -- but it is undeveloped and must be shown to yield n_s~0.96.
"""
import numpy as np

h=0.674; Om_m=0.315; ns=0.965

def Tbbks(k):                       # k in h/Mpc; BBKS transfer function
    Gamma=Om_m*h                    # (ignoring small baryon suppression)
    q=k/Gamma
    q=np.where(q<1e-8,1e-8,q)
    return (np.log(1+2.34*q)/(2.34*q))*(1+3.89*q+(16.1*q)**2+(5.46*q)**3+(6.71*q)**4)**(-0.25)

def check1_growth_given_seeds():
    k=np.logspace(-3,1,500)         # h/Mpc
    P=k**ns*Tbbks(k)**2
    kpk=k[np.argmax(P)]
    # low-k slope ~ ns; high-k slope ~ ns-4 (+ log)
    lo=np.polyfit(np.log(k[(k>1e-3)&(k<3e-3)]),np.log(P[(k>1e-3)&(k<3e-3)]),1)[0]
    hi=np.polyfit(np.log(k[(k>2)&(k<8)]),np.log(P[(k>2)&(k<8)]),1)[0]
    ok = 0.005<kpk<0.03 and abs(lo-ns)<0.1 and hi<-2.0
    print(f"CHECK 1 (growth, given scale-invariant seeds): P(k) turns over at k={kpk:.4f} h/Mpc "
          f"(k_eq~0.015); low-k slope={lo:.2f} (~n_s={ns}); high-k slope={hi:.2f} (~n_s-4)")
    print(f"          -> {'PASS' if ok else 'FAIL'}  (CPP inherits the standard transfer/growth; "
          f"this part is fine, CONDITIONAL on the Step-D background)")
    return ok

def check2_causal_seed_obstacle():
    eta_rec=280.0      # Mpc, comoving particle horizon at recombination (standard)
    D_LS=14000.0       # Mpc, comoving distance to last scattering
    theta_H=eta_rec/D_LS
    l_H=np.pi/theta_H
    ok = 100<l_H<250
    print(f"CHECK 2 (causal-seed obstacle): horizon at recombination subtends "
          f"theta_H={np.degrees(theta_H):.2f} deg -> l_H~{l_H:.0f}")
    print(f"          Causal seeds can correlate only l >~ {l_H:.0f}. But the observed CMB has")
    print(f"          correlated ADIABATIC power at l<{l_H:.0f}: the Sachs-Wolfe plateau (l~2-50) and")
    print(f"          the TE anti-correlation at l~100-150 -- the textbook signature of SUPER-horizon")
    print(f"          perturbations. Active/causal seeds (cosmic strings, textures, 'swirls') also give")
    print(f"          INCOHERENT (smeared) acoustic peaks, not the observed sharp harmonic series.")
    print(f"          -> {'PASS (obstacle is real & quantified)' if ok else 'FAIL'}  "
          f"-> causal swirl seeds fail as the PRIMARY structure source")
    return ok

def check3_verdict():
    print("CHECK 3 (verdict): Step 4 is NOT passed and NOT cleanly killed.")
    print("          - GROWTH (Q1): fine, inherited (conditional on Step D).")
    print("          - SEED ORIGIN (Q2): the swirl mechanism is prima facie CAUSAL -> hits the")
    print("            active-source wall (no super-horizon adiabatic plateau; smeared peaks).")
    print("          - LIVE ESCAPE: CPP's atemporal Nexus enforces non-local coordination")
    print("            INDEPENDENT of light-cones -> could seed acausal/super-horizon correlations")
    print("            (a horizon-problem resolution standard active-source models lack). BUT it is")
    print("            undeveloped, CPP-flagged as 'lacking physical grounding', and must be shown")
    print("            to yield a near-scale-invariant (n_s~0.96) ADIABATIC spectrum specifically.")
    print("          => CONJ-COSMO-1's structure-formation mechanism is its WEAKEST link; the")
    print("             discriminating requirement is UNMET. Do NOT claim CPP reproduces P(k).")
    return True

if __name__=="__main__":
    print("=== Patch 0725 -- DM Step 4: power spectrum from swirl seeds (MOST DISCRIMINATING) ===")
    r=[check1_growth_given_seeds(), check2_causal_seed_obstacle(), check3_verdict()]
    print(f"\nStep 4 {'CHECKS RAN' if all(r) else 'ERROR'} -- VERDICT: SERIOUS TENSION (not pass, not "
          f"clean kill). Growth is inherited & fine; the SEED ORIGIN is the wall -- causal swirls fail "
          f"as active sources unless the atemporal Nexus supplies acausal, scale-invariant, adiabatic "
          f"seeds (undeveloped). This is the dominant open problem for CONJ-COSMO-1.")
