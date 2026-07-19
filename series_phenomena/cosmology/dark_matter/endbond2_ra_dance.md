# OPEN-DM-ENDBOND-2 — R-A executed under the 2548 pre-registration: the two-plane fragment dance resolves NO bond at the registered grid — union band [−3.6, +1.4] MeV spans zero; Branch I (statistical limb); the in-context closure bond named as the successor target

**Patch 2549, 18 July 2026. Status: OPEN-DM-ENDBOND-2 CLOSED at Branch I (statistical
limb) as pre-registered.** Verify: `code/2549_endbond2_dance.py` (deterministic, 14 s; all
assertions pass; the union band is frozen in-code before the gates section prints; the
fenced numbers appear nowhere above the freeze).

## 1. The computation

dance_v8 verbatim (2510 rules; pinned κ_q = 132, κ_e = 44, kscale = 1.0; TC = 60,
burn = 0.15) on the two-plane stack (16 CPs, pitch D = 1.15, alternating parity) vs two
independent single-plane dances (exact non-interaction). Reach sanity passed: all 8 stack
qCPs acquire their axial partner; the isolated plane has zero cross partners. Union grid =
dt {τ_C/100, τ_C/50, τ_C/25} × FREF {local 10.80, registered-16-plane 10.47}.

## 2. Frozen result

| FREF | dt = τ_C/100 | τ_C/50 | τ_C/25 |
|---|---|---|---|
| local | +1.3 | −0.6 | −3.1 |
| 16-plane | +1.4 | −1.0 | −3.6 |

**FROZEN UNION BAND (primary ⟨Ep⟩, interface total): E_endbond ∈ [−3.6, +1.4] MeV —
spans zero.** Per the pre-registered readings this is the **Branch I statistical limb: no
depth claim; gates G1/G2 not licensed on a non-depth.** The ⟨Etot⟩ accounting (disclosed)
spans [−39, +6] — dt-dominated in the same way. Robustness check (disclosed only): the
20 fm finite-gap reference agrees with the independent-planes reference to 0.5 MeV.

## 3. Diagnosis (banked, not claimed)

The spread is **discretization-dominated**: the dt axis moves the number by ~5 MeV across
the registered grid while the FREF axis moves it by ≲0.5 MeV, and the sign flips along dt.
The fragment's dance cohesive energies are GeV-scale; a bond of order a few MeV — if it
exists at this fragment scale — sits below the integrator floor of the registered grid.
ZBW amplitudes (0.30–0.36 fm) are physically sensible (≈ a_ee), so the dance itself is
healthy; the *difference* is what the grid cannot resolve. Two honest readings, neither
claimable: (i) the isolated two-plane interface bond is genuinely weak (the stacking
cohesion could be cooperative — an in-context, many-plane effect, consistent with the
−68.8 ring−straight living at full ring scale while the fragment shows ~0); (ii) a real
few-tens-of-MeV fragment bond is masked by discretization. Extending the dt grid post-hoc
would be Branch T under the 2548 prereg; it is available to a successor pre-registration.

## 4. Successor target (named, not opened)

The 2542 downstream consumer (ΔE_close) wants the **in-context closure bond** — the energy
gained when the last interface of the presented rod closes into the ring — not the isolated
fragment bond. The natural instrument is a **cut-ring vs closed-ring dance comparison at
N = 16** (which inherently consumes L = 16 and therefore carries RODCLOSE-1's
conditionality rider), with a finer pre-registered dt grid sized to the expected
signal. Registrable as OPEN-DM-ENDBOND-3; queued for founder awareness, not opened in this
patch (two campaign closures in one day is the natural pause point, and the target
definition differs enough from ENDBOND-1/2 to deserve its own charter conversation).

## 5. Bookkeeping

79.5 % untouched. The 2542 E_endbond band [40, 170] **stands unrevised** (this campaign
produced no depth; the downstream revision fires only on a pin). Standing disclosure
package gains the dated Branch-I line. Queue: ENDBOND-3 charter decision → RODCLOSE-1
kinetic limb → plane-resident-fraction limb → δ_E → MW-MODES TC-extension. Next patch:
2550.
