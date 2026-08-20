#!/usr/bin/env python3
"""
3261_a5_closure_annex_verify.py — verify script for the A-5 closure annex
(CONV-027 adjudication, Patch 3261).

Discharges the panel's conditions on Package A (GPT Q1/Q6b; Copilot Q6b;
Grok/DeepSeek strongest objections): instead of claiming the two-level
closure is UNIQUE, prove the continuum operator is ROBUST over the full
admissible class, and make the kinematic mapping explicit.

  L1  Time-reversal symmetry forces the two-level FORM: a linear
      one-register recurrence u(t+1) = A u(t) + B u(t-1) that is invariant
      under running the same law backwards requires B = -1 (the companion
      map is then volume-preserving, det = 1). Checked symbolically.
  L2  One-hop locality restricts A to A = 2[alpha*M_R + (1-alpha) I];
      the admissible-class dispersion is
          cos(w tau) = alpha*sinc(kR) + (1-alpha).
      Unitarity (real w for all k) holds for alpha in (0,1]. Checked over
      a dense k-grid for alpha in {0.25, 0.5, 0.75, 1.0}.
  L3  Long-wave limit for every admissible alpha:
          c_*(alpha) = sqrt(alpha) * R / (sqrt(3) tau)
      — the OPERATOR (variable-speed wave equation) is closure-independent;
      only the speed coefficient varies, and it is degenerate with the
      kinematic c-identification. Checked numerically (phase and group).
  L4  alpha = 1 reproduces the Patch-3258 dispersion exactly.
  L5  The falsifier statement is correspondingly WEAKENED and honest: the
      registered discrete-dispersion residue is the one-parameter FAMILY
      cos(w tau) = alpha*sinc(kR) + (1-alpha), not the single alpha=1 curve.
      (Statement check: the family members are numerically distinguishable
      at kR ~ 1 — max pairwise separation reported — so the family is a
      real, testable residue, not vacuous.)
"""
import numpy as np
import sympy as sp

PASS = []
def check(name, ok, detail=""):
    PASS.append(ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))

print("== L1: time-reversal symmetry forces B = -1 (two-level form) ==")
Asym, Bsym = sp.symbols('A B')
# forward: u2 = A u1 + B u0 ; time-reversed same law: u0 = A u1 + B u2.
# Substituting the reversed relation into the forward one must be an identity
# for all trajectories: u2 = A u1 + B (A u1 + B u2) => (1 - B^2) u2 = A(1+B) u1
# Identity for all (u1, u2) requires 1 - B^2 = 0 and A(1+B) = 0.
sols = sp.solve([1 - Bsym**2, Asym*(1 + Bsym)], [Asym, Bsym], dict=True)
nontrivial = [s for s in sols if s.get(Bsym) == -1]
trivial = [s for s in sols if s.get(Bsym) == 1]
ok1 = any(Bsym in s and s[Bsym] == -1 and Asym not in s for s in sols) or \
      (len(nontrivial) > 0)
# also: companion matrix [[A, -1],[1, 0]] has det = +1 (volume-preserving)
Amat = sp.Matrix([[Asym, -1], [1, 0]])
ok1b = sp.simplify(Amat.det() - 1) == 0
check("B = -1 branch exists with A free; B = +1 branch forces A = 0 (trivial swap)",
      ok1 and all(s.get(Asym, None) == 0 for s in trivial),
      f"solutions: {sols}")
check("companion map det = +1 (volume-preserving) for B = -1", ok1b)

print("== L2: admissible-class unitarity, alpha in (0,1] ==")
kk = np.linspace(1e-6, 40.0, 20000); R = 1.0
sinc = np.sinc(kk*R/np.pi)
ok2 = True; det = []
for alpha in [0.25, 0.5, 0.75, 1.0]:
    P = alpha*sinc + (1-alpha)
    ok2 = ok2 and np.all(np.abs(P) <= 1.0 + 1e-12)
    det.append(f"alpha={alpha}: max|P|={np.max(np.abs(P)):.6f}")
check("|alpha*sinc(kR)+(1-alpha)| <= 1 for all k (real dispersion, unitary)",
      ok2, "; ".join(det))

print("== L3: long-wave speed sqrt(alpha)*R/(sqrt(3) tau) for every alpha ==")
ok3 = True; det = []
for alpha in [0.25, 0.5, 0.75, 1.0]:
    for k2 in [(2e-3, 2.1e-3)]:
        k_lo = np.array(k2)
        w = np.arccos(alpha*np.sinc(k_lo*R/np.pi) + (1-alpha))
        vph = w[0]/k_lo[0]
        vg = (w[1]-w[0])/(k_lo[1]-k_lo[0])
        target = np.sqrt(alpha)/np.sqrt(3)
        ok3 = ok3 and abs(vph - target) < 1e-4 and abs(vg - target) < 1e-4
        det.append(f"alpha={alpha}: vph={vph:.6f}, vg={vg:.6f}, target={target:.6f}")
check("phase AND group speed -> sqrt(alpha)*R/(sqrt(3) tau): wave OPERATOR "
      "closure-independent; speed coefficient degenerate with c-identification",
      ok3, " | ".join(det[:2]) + " ...")

print("== L4: alpha = 1 reproduces Patch-3258 exactly ==")
w1 = np.arccos(np.sinc(np.array([2e-3])*R/np.pi))[0]/2e-3
check("alpha=1 long-wave speed = 1/sqrt(3) (3258 value)",
      abs(w1 - 1/np.sqrt(3)) < 1e-4, f"{w1:.8f}")

print("== L5: the family is a real (non-vacuous) falsifier residue ==")
kmid = np.linspace(0.5, 3.0, 200)
curves = [np.arccos(np.clip(al*np.sinc(kmid*R/np.pi) + (1-al), -1, 1))
          for al in [0.25, 1.0]]
sep = np.max(np.abs(curves[0] - curves[1]))
check("family members distinguishable at kR ~ 1 (max separation > 0.1 rad)",
      sep > 0.1, f"max |w(alpha=0.25)-w(alpha=1)|*tau = {sep:.3f} rad")

print(f"\n{sum(PASS)}/{len(PASS)} checks pass")
raise SystemExit(0 if all(PASS) else 1)
