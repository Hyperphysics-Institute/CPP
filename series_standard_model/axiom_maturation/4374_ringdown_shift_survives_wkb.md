# The Ringdown Shift Survives a Better Calculation: the ℓ = 2 Mode of the Steady-Percentage Exterior Is 4.1% Low in Frequency (WKB, Validated), Against GW250114's ±2.4%

**Patch:** 4374. **Lane:** foundations, with GR. **Session:** 242.
**Answers:** TODO-4365-THIRDORDER (b), first step (the ringdown beyond the eikonal estimate; 4372 §4 idea 2).
**Verify:** `series_standard_model/code/4374_ringdown_wkb_beyond_eikonal.py` (sympy + scipy). The code reproduces Iyer's
3rd-order WKB values for the Schwarzschild scalar field exactly (ℓ = 1: 0.2911 − 0.0980i; ℓ = 2: 0.4832 − 0.0968i).
**Founder:** none this turn. The founder's 4373 §5 question is unanswered; this is the other branch that decides it
(PD-008).

## 1. What was computed

4369 and 4372 used the eikonal (large-ℓ) light-ring formula. Here the actual ℓ = 1, 2, 3 fundamental modes of a scalar
test field are computed by 3rd-order WKB on both exteriors: Schwarzschild, and the steady-percentage exterior
(λ = 0: g₀₀ = −e^{−2m/r}, g_ij = e^{2m/r}δ, isotropic).

| ℓ | Schwarzschild | steady-percentage exterior | frequency shift | damping shift |
|---|---|---|---|---|
| 1 | 0.2911 − 0.0980i | 0.2812 − 0.0935i | −3.41% | −4.55% |
| **2** | 0.4832 − 0.0968i | 0.4636 − 0.0924i | **−4.06%** | **−4.57%** |
| 3 | 0.6752 − 0.0965i | 0.6466 − 0.0921i | −4.24% | −4.52% |
| eikonal (4369) | | | −4.42% | −4.42% |

The ℓ = 2 frequency shift is −4.1%, approaching the eikonal −4.4% as ℓ grows, as it should. Against GW250114's box
(f₂₂₀ ± 2.4%) that is **about 1.7 box-widths outside**. The damping (−4.6%) is well inside its (−15, +17)% box.

## 2. What this changes

4372 §4 listed three possibilities:
1. clocks and rulers part at second order;
2. the ringdown is not yet decided;
3. one PSR stands as a prediction.

The eikonal shortcut was the weakest link in possibility 2, and it holds up: the shift is not an artefact of large-ℓ
approximation. Two gaps remain:
- **spin:** GW250114's remnant has χ_f = 0.68;
- **CPP's own tensor-wave operator** on this exterior, which is not derived. A scalar test field is the standard proxy;
  gravitational perturbations of a non-GR geometry can differ.

Unless one of these moves the frequency by about two percentage points toward Einstein, possibility 2 does not rescue
λ = 0. **The pressure toward possibility 1 (clocks slowing by more than the PSR deep in a well, the founder's 4373
idea) has increased.** This is not an exclusion: it is a scalar-field, non-spinning comparison with a 2σ-scale box.

## 3. Owed next (GR lane)

- The spinning case. Either a slow-rotation expansion of the exponential exterior, or a direct comparison of the
  fractional shift for Kerr against a rotating generalisation. No rotating version of the steady-percentage exterior is
  on file.
- CPP's tensor-wave operator on the exterior (GR-1j T-1 gives the scalar-sector wave equation; the tensor channel,
  SR-2/A3′, is needed).

## 4. PD-008

- **The convenient branch:** concluding that λ = 0 is excluded. It is not: spin and the tensor operator are open, and
  the box is 2σ-scale.
- **The inconvenient result, stated plainly:** the better calculation confirms the eikonal estimate to within 0.4
  points. The ringdown is the sharpest live test of the one-PSR ruling.
