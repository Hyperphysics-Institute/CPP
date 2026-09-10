# Reasoning capture — Patch 3818: T-3b first computation (δkT → ζ = 0, HALT)

*Session 169, 9 Sep 2026, EU lane. Verbatim at-patch capture. Finding: `eu1_derivation/t3b_delta_kT_computation.md`. Verify: `scripts/3818_t3b_delta_kT_checks.py` (4/4).*

The question entering this computation was tightly specified: does δkT yield ζ through the end condition? The charter already anticipated the answer under the simplest reading — "under the pure count law ζ = 0" — and T-3b's job was to make that rigorous and check whether the answer changes under the re-grounded occupancy.

The δN formalism gives ζ(x) = δN(x) = N_*(x) − ⟨N_*⟩, with N_* the local e-fold count from the initial flat slice to the end-of-inflation flat slice. Under the re-grounded count law (3816), N_* = ⅓ ln(n̄_init / n̄_end). Both inputs are kT-free: n̄_init is set at Moment 1 by the CP count in the ball (same everywhere by the empty-register argument), and n̄_end = 1 is a pure geometric threshold (one CP per Planck sphere). kT appears only in H_eff = κ₀ kT ln n̄, which sets the rate of expansion — how many seconds per e-fold — but not the number of e-folds. A patch with higher kT expands faster in time but dilutes in the same number of e-folds to the same geometric threshold. δN = 0.

I kept looking for a route where kT could enter, because C-1 is the first candidate from the founder's own picture and I did not want to close it on a technicality. The serious route would need either (a) the end condition to depend on kT — if inflation ended when H_eff fell to some kT-derived threshold (e.g., the bath's relaxation rate), then δkT → δN_end → ζ ≠ 0 — or (b) the PSR floor from OPEN-EU-PSR-EARLY-1 to be kT-dependent, so that the perceived end condition is shifted locally by the bath temperature. Both routes are real and worth pursuing, but neither is on file, and neither can be computed without the early PSR law (PSR-EARLY-1's target, unwritten) or a new founding picture of what sets the end of the inflationary window.

What is not a route: δkT modulating the rate without modulating the end threshold. In single-field inflation δφ → ζ because φ couples to both H (through V(φ)) and the end condition (φ → φ_end triggers reheating). Here kT couples only to H; the end condition is purely geometric. The bridge is one-sided. S = 0 by construction, not by cancellation.

I checked that this doesn't touch the tilt. n_s = 1 − 2/N_* follows from d ln n̄/dN = −3 (pure count law, kT-free), and the shape of the count law is unchanged by anything that happens to kT. The tilt chain has no kT in it. PRED-C-96 stands; what fails is the amplitude companion.

The charter's HALT rule fires for S < 220 under a founder-supported mode, and C-1 is founder-supported (3813). The tension goes against the amplitude (A_s), not the tilt, exactly as the charter prescribed. What I registered as OPEN-EU-AMPLITUDE-1 is the gap that always existed in EU-1 — the "spectator prescription" asserted in §Amplitude was never grounded — now stated with a sharper frame: the natural candidate from first principles gives ζ = 0, and two specific routes exist to search for ζ ≠ 0, neither of which is a guessing game.

The charter said the answer is "decisive either way." HALT is decisive: the computation is short, the gap is precisely located, and the escape routes are named. That is more useful than a vague "amplitude unknown."
