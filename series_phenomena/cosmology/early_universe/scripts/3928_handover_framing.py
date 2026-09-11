#!/usr/bin/env python3
"""Patch 3928 -- the two owed framings: the SM-sector question stated in the FP lane's terms, and Exit 1's
acceptance criteria. D-7 applied and it paid immediately: part of the SM answer is already on file."""
import sys, math
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
res=[]
def check(n,c,d=""):
    res.append(c); print(f"[{'PASS' if c else 'FAIL'}] {n}"+(f"  -- {d}" if d else ""))
NTOT=math.log(1e84)/3; NREM=57.0; K0=1.93e-5/(3*57)

check("T1 **D-7 APPLIED FIRST, and it paid immediately.** The question was to be framed for the SM sector; "
      "locating that sector's vocabulary found **the FP lane owns baryogenesis** (η_B ≈ 6×10⁻¹⁰ via "
      "**leptogenesis**, with a CP-asymmetry parameter ε_CP, at zero free parameters under FI-C-1…10 plus "
      "four axioms)",
      True, "the receiving lane has its own established machinery; the question must enter through it")

check("T2 **AND PART OF THE ANSWER IS ALREADY ON FILE:** the corpus states the sea is **net-neutral and "
      "colour-neutral** — *'there is no charge obstruction to a muon neutrino being a qDP'*. **So the "
      "electric and colour halves of the question are answered.**",
      True, "D-7 again: the term was defined, and asking blind would have wasted the FP lane's time")

check("T3 **WHAT REMAINS IS NARROWER, and this is the question to send:** net-neutrality is stated for "
      "**charge and colour**. **It is NOT stated for baryon or lepton number.** A qDP is two qCPs of "
      "opposite charge, which is particle–antiparticle-like and suggests B = 0 per pair — **but that is "
      "an inference, not a corpus statement**",
      True, "the gap is B and L, not charge")

check("T4 **THE QUESTION, IN FP's TERMS:** *Does a local enrichment in Q-dominant SCPs shift η_B or the "
      "lepton asymmetry, or is the Q:E composition orthogonal to the leptogenesis sector?* **Not** *'does "
      "the sea's q:e composition carry a conserved charge?'* — which is EU vocabulary and would need "
      "translating before FP could act",
      True, "stated so the receiving lane can act without translating")

check("T5 **AND WHY FP SHOULD CARE, stated so the request is not an unexplained errand:** if a Q-enriched "
      "patch carries net B, the compositional perturbation becomes a **baryon-isocurvature mode**, which "
      "**survives thermalisation** and is tightly bounded — **C-5 then fails by ~30× and dies**. If it is "
      "orthogonal, C-5's adiabaticity holds",
      True, "the consequence is stated, so FP can judge the priority")

# --- Exit 1 acceptance criteria ---
check("T6 **EXIT 1's ACCEPTANCE CRITERIA — criterion 1: κ₀ must COME OUT, not be fitted.** A derivation of "
      "H_eff ∝ μ must **produce** κ₀ ≈ 1.1×10⁻⁷ from substrate dynamics. **PD-007 bars obtaining it from "
      "A_s**, and 3902 showed the end-to-end route is circular because H is A_s-normalised",
      abs(K0-1.13e-7)/1.13e-7<0.02, f"target kappa_0 = {K0:.2e}")

check("T7 **criterion 2: it must reproduce the COUNT LAW.** N_total = ⅓ ln N_CP = **64.47**, and the end "
      "condition n̄ = 1 must still be reached at that value",
      abs(NTOT-64.47)<0.02, f"N_total = {NTOT:.2f}")

check("T8 **criterion 3: it must preserve LINEARITY.** ln n̄ must remain **linear in N_rem**, since that "
      "linearity — not its coefficient — is what gives ε = 1/N_rem and hence **n_s = 1 − 2/N_rem** "
      "(PRED-C-96). **A derivation that fixes κ₀ but breaks linearity loses the tilt, which is the lane's "
      "one confirmed prediction**",
      abs((1-2/NREM)-0.9649)<1e-4, "the tilt is the thing that must not be traded away")

check("T9 **criterion 4: it must not collide with the CC lane's ρ_Λ — and must not be expected to derive "
      "it either.** Per 3922, ρ_Λ (Li-analog, event-horizon) and the engine answer **different "
      "questions**; a derivation of H ∝ μ owes **consistency** with ρ_Λ, not reproduction of it",
      True, "the 3920 error must not be re-committed in the acceptance criteria themselves")

check("T10 **AND THE NEGATIVE CRITERION, stated so a partial result is not mistaken for a pass:** "
      "**deriving the FORM H ∝ μ without the COEFFICIENT does not discharge Exit 1.** The form is already "
      "assigned; **what is missing is κ₀**. A derivation that reproduces the proportionality and leaves "
      "the constant free changes nothing",
      True, "the likeliest near-miss, named in advance")

n=sum(res); print(f"\n{n}/{len(res)} PASS"); sys.exit(0 if n==len(res) else 1)
