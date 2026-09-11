# C-5's correlation length computed — **Gaussianity clears decisively, and that is the first test in this arc a candidate has PASSED that killed a predecessor.** The amplitude then reduces to a single number: **ℓ_corr ≈ 138 PSR**. Reachability is trivial; **the open question is SATURATION — what stops the correlation growing past 138?**

**Patch 3896, Session 207, 11 Sep 2026. Lane: EU.** Discharges the correlation-length half of C-5's amplitude debt. Verify `scripts/3896_correlation_length.py` (10/10). Reasoning `reasoning/3896_correlation_length.md`. Nothing adopted; **C-5 still not reported as working**; PRED-C-96 untouched; 3710 not retired.

## §1 The bare range is fixed by the protocol, not estimated (verify T1, T2)
The attraction between SCPs is mediated by **arriving DI-bits** — an SCP's pull on another is SSV_net, built from what reaches it. And AP-4/AP-4c give the DI-bit a **hard reach**: deposit once at the PSR shell, near field by the hop cascade within it.

> **The bare correlation length of the affinity is 1 PSR.** That is a protocol fact, not an estimate.

At the pivot, R_H = 5.2×10⁴ l_P, so the bare range gives **1.4×10¹⁴ independent patches per Hubble volume**.

## §2 Gaussianity clears — decisively (verify T3, T4)
The excess kurtosis of a sum of N independent patches goes as κ_patch/N. At the bare range:

| patch kurtosis | mode kurtosis |
|---|---|
| 10³ (cascade-like) | **7.2×10⁻¹²** |
| 10² | 7.2×10⁻¹³ |

Planck's f_NL bound is O(5–10). **This is utterly Gaussian, by eleven orders of margin.**

> **0730's wall does not apply to C-5.**

**This is the first time in this arc that a candidate has passed a test which killed a predecessor**, rather than failing the same test by a smaller margin. The fractal cascade died on non-Gaussianity; C-5 does not, and the reason is structural — a cascade at observable scales is one correlated object, while C-5's affinity is microscopic and gets averaged over 10¹⁴ independent patches.

## §3 The amplitude at the bare range fails — but by 3 orders, not 40 (verify T5)
> δ ln f per Hubble volume = (per-patch value)/√N_ind.

Reaching the observed ζ ≈ 4.6×10⁻⁵ at the bare range would need a **per-patch δ ln f of 1.6×10³**. A log-fraction fluctuation within one correlation volume cannot plausibly exceed **O(1)**.

**So C-5 falls short by ~1600× at the bare range** — ζ = 2.8×10⁻⁸ against 4.6×10⁻⁵. That is a failure, and it is worth noting it is a **three-order** failure where every other candidate in this arc failed by **forty or more**.

## §4 The target — a single number (verify T6, T7, T8)
With per-patch δ ln f = O(1), the relation is

> **ζ = ⅓ · (ℓ_corr/R_H)^{3/2}**

and the observed amplitude requires

> **ℓ_corr ≈ 138 l_P ≈ 138 PSR.**

**It is sharp, not a window.** Since ζ ∝ ℓ^{3/2}, a factor 2 in ℓ_corr moves the amplitude by 2.8:

| ℓ_corr | ζ/ζ_obs |
|---|---|
| 1 PSR | 6×10⁻⁴ |
| 10 PSR | 1.9×10⁻² |
| **138 PSR** | **1.0** |
| 500 PSR | 6.9 |
| R_H (5.2×10⁴) | 7.3×10³ |

**And Gaussianity is still safe there** — at ℓ_corr = 138 the mode kurtosis is 1.9×10⁻⁵, far inside any bound. **Both tests pass at the same correlation length; there is no conflict between them.** That is not guaranteed and it is worth recording: the two requirements could have been mutually exclusive, and they are not.

## §5 The open question is saturation, not reach (verify T9, T10)
**Reachability is trivial.** Local dynamics grow correlations by about 1 PSR per Moment, and there are 5.2×10⁴ Moments per e-fold, so 138 PSR takes **0.0027 e-folds**. The system has 64.

**That is the problem, not the solution.** If nothing stops the growth, correlations run to the Hubble radius, N_ind → 1, and **ζ overshoots by 7×10³**.

> **So C-5 now needs a saturation mechanism: what arrests the correlation at ~138 PSR?**

**This is a sharper and smaller question than any C-5 has had**, and it is the right kind: not "is there a source?" but "what sets a specific length?" Candidate answers to look at — **none evaluated here**:
- The **PSR's own contraction** under load (3837's B2 floor), which shortens the reach as occupancy rises.
- The **eDP pair-swapping** channel (3894), which destroys correlation as fast as the q-channel builds it — a natural competing rate.
- **Horizon exit itself**, if the affinity's build-up is slower than 1 PSR per Moment.

## §6 Standing
- **The bare correlation length is 1 PSR** — fixed by AP-4/AP-4c, not estimated.
- **GAUSSIANITY CLEARS** at any relevant range: mode kurtosis 7×10⁻¹² at the bare range, 1.9×10⁻⁵ at the target. **0730's wall does not apply.** **First test in this arc a candidate has passed that killed a predecessor.**
- **Amplitude at the bare range fails by ~1600×** (3 orders, against 40+ for every other candidate).
- **Target: ℓ_corr ≈ 138 PSR**, sharp to within ~×2 since ζ ∝ ℓ^{3/2}. **Both tests pass there.**
- **Reachability is trivial (0.0027 e-folds); the open question is SATURATION.**
- **C-5's amplitude debt is now: what arrests the correlation at ~138 PSR?** Three candidate mechanisms named, none evaluated.
- **Nothing adopted. C-5 still not reported as working.** PRED-C-96, T-1, T-2, the count law: unaffected.
