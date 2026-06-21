# Reviews — TP-1 (compiled) + FAQ

Part 1 compiles the panel; the raw aggregated log is `../review/reviews-TP-1.md` and the dispatched package is `../review/TP-1_review_package_v1.0.md`.

## Part 1 — Formal reviews

**Panel: 4 reviewers, DG-3 satisfied. Zero physics objections. Unanimous: NOT "standard QFT plus a renamed cutoff."**

| Reviewer | Round | Verdict | Critiques accepted | Outcome |
|---|---|---|---|---|
| **Grok** | v0.2 | SHIP toward v1.0 | √ω normalization note; "physical-within-CPP/formal-within-RGS" | folded → v0.3 |
| **Gemini** | v0.2 | SHIP as v1.0 | domain-folder justification; own the "renamed cutoff" critique | folded → v0.3 |
| **Copilot** | v0.2 | restate → v0.3 | instantiate-not-identify; disown v0.1 overclaim; embedding-not-explaining; log-class → Lemma; C-across-profiles; two-regime paragraph; "compat + foundational regularization" | all folded → v0.3 |
| **ChatGPT** | v0.2 | restate → v0.3 | compatibility-not-entailment; cutoff framework-conditional; "RGS-derived, CPP-regularized"; honest "thin until HS sum" | all folded → v0.3/v0.4 |

**Declined:** none (no reviewer asked for anything the paper rejected). **Attribution note:** review 1 was initially logged as ChatGPT; operator confirmed it was Grok (corrected in 1705).

**Post-review strengthening (v0.4):** the band-top advance (cutoff grounded as $\omega_{\max} = \sqrt{12}/t_P$) directly answers the one caveat both restate-requesters raised — review-responsive, not a new unreviewed claim.

## Part 2 — FAQ

**Methodology.**
- *Q: Does CPP derive the RGS effect?* No. It embeds it: CPP supplies a substrate realizing the structures RGS assume. Standard QFT already permits the effect if RGS is correct.
- *Q: Is the divergence class assumed or derived?* Derived, from the RGS kernel (Lemma): Heaviside truncation → $1/\omega$ tail → $\times\sqrt\omega$ → $1/\omega$ spectrum → logarithmic.

**Scope.**
- *Q: Is this just "standard QFT + a Planck cutoff"?* The cutoff is intrinsic (the 600-cell has a hard band top, no modes above it) and $z$-specific ($\omega_{\max} = \sqrt{12}/t_P$), not a generic Planck regulator. The honest residual: the precise $C$ still needs the lattice HS mode sum (OPEN-TP-1).
- *Q: Why a new quantum-optics domain for a compatibility paper?* TP-1 is the foundational bridge mapping standard optics formalism (Fock states, mode truncation, Bogoliubov boundaries) onto the DP-Sea, for later optical phenomena.

**Falsifiability.**
- *Q: Is TP-1 experimentally testable?* No — the ceiling is reached only in the unphysical instantaneous limit; realistic shutters self-regularize. It is foundational, not falsifiable in the testable regime.

**SM relationship.**
- *Q: Does it disagree with standard QFT?* No — it reproduces it and adds only the fate of the instantaneous-shutter divergence.

**Future work.**
- *Q: What closes OPEN-TP-1?* Evaluating $\|T_2\|^2_{\mathrm{HS}}$ over the 600-cell modes with the band-top density of states, returning a definite $O(1)$ $C$.
