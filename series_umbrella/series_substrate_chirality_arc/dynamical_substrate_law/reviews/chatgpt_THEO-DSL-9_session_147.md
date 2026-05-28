# ChatGPT Review of THEO-DSL-9 (Patch 0615) — face-aligned $V_4$/2-D correction to THEO-DSL-8

## Metadata

- **Reviewer**: ChatGPT (OpenAI)
- **Subject reviewed**: THEO-DSL-9 (candidate) — `series_umbrella/series_substrate_chirality_arc/dynamical_substrate_law/hardened_theorems/o_delta_two_face_aligned_coefficient.tex` (Patch 0615) — and the embedded structural correction to THEO-DSL-8 (Patch 0597) registered there.
- **Subject version commit**: `8893f86` (Patch 0616 origin/main head)
- **Review session**: Session 147
- **Review archived by**: Patch 0617 (this file)
- **Review delivered**: 28 May 2026 (Session 147 multi-AI review cycle for the THEO-DSL-8 $C_s\to V_4$ correction)
- **Reviewer panel position**: Round 1 of the THEO-DSL-9 / THEO-DSL-8-correction review cycle. ChatGPT continues to occupy the primary / strongest-reviewer position per programme convention.
- **Review character**: **Decisive CONFIRMED verdict with independent numeric verification, including a Q5 host-stabilizer enumeration that the other reviewers did not perform**. ChatGPT numerically built the 600-cell, verified Q1 ($\sigma_F$ permutes 120 vertices and fixes $v_h$, $\hat n_{F\perp}$), Q2 ($V_4$ group; rank-2 invariant projector), Q3 ($\hat n_{F\perp}$ components along $\hat n_{\perp 3}$ and $\hat n_{\text{diff}}$ both zero), Q4 (full 144-path sum reproducing $(\alpha_\rho, \alpha_{\text{ax}}, \alpha_{\perp 3}, \alpha_{\text{diff}}) = (-2.673762078750733, -2.763932022500209, 5.6\times 10^{-17}, 0)$ matching $(-14+7\phi, -6+2\phi)$, plus the $-9/\phi^2$ vertex cross-check). **Q5 (the strongest single result of the cycle)**: ChatGPT *enumerated the full 120-element host stabilizer* and found *exactly* 4 elements fixing $\hat n_{F\perp}$ — precisely $\{I, \sigma_E, \sigma_F, C_2\}$ — establishing that $V_4$ is **saturated**, with no enlargement possible. This closes the caveat that the residual symmetry might be larger than $V_4$ (which would have shrunk the subspace below 2-D), proving that 2-D is exact, not an upper bound. **No refutation; no ambiguity; no error.**
- **Programme-level reviewer ranking**: ChatGPT delivers the most decisive single result of the review cycle (the Q5 saturation proof via host-stabilizer enumeration). It is the only reviewer to perform that enumeration; this elevates the $V_4$ claim from "consistent with orbit-stabilizer bound" to "directly verified saturation by exhaustive search."
- **Verdict-state classification**: **EXPLICIT CONFIRMED (numeric independent, with Q5 saturation enumeration)**. Combined with Grok's CONFIRMED (numeric independent, explicit $\sigma_F = \mathrm{diag}(1,1,1,-1)$ witness) and Copilot's PARTIAL/UNCERTAIN (analytic-confirm-conditional-on-Q1, no refutation), overall cross-reviewer position is **THREE-FOR-THREE no-refutation with two independent numeric confirmations**. THEO-DSL-9's $V_4$/2-D/$1\!\to\!2\!\to\!2$ correction stands as multi-AI confirmed; THEO-DSL-8 is to be treated as superseded for its structural claim.

---

## Reviewer letter (verbatim)

CONFIRMED. I independently checked the load-bearing claim numerically from the self-contained 600-cell definition.

Q1: confirmed. $\sigma_F$ maps all 120 vertices to vertices, fixes $v_h$, and fixes $\hat n_{F\perp}$, so it preserves the rate function.

Q2: confirmed. $\{I,\sigma_E,\sigma_F,\sigma_E\sigma_F\}$ is $V_4$. Its invariant projector has rank 2, fixing exactly $\operatorname{span}\{\hat n_\rho,\hat n_{\rm ax}\}$.

Q3: confirmed. $\hat n_{F\perp}$ has zero components along $\hat n_{\perp 3}$ and $\hat n_{\rm diff}$, so the prior basis is rank 2, not rank 3.

Q4: confirmed. Summing all 144 two-edge paths gives
$$ (\alpha_\rho,\alpha_{\rm ax},\alpha_{\perp 3},\alpha_{\rm diff})
= (-2.673762078750733,\; -2.763932022500209,\; 5.6\times 10^{-17},\; 0), $$
matching $(-14+7\phi,\, -6+2\phi)$. The vertex-aligned cross-check gives $-9/\phi^2$.

Q5: I enumerated the full host stabilizer numerically: 120 host-fixing automorphisms. Exactly 4 fix $\hat n_{F\perp}$, and they are precisely $\{I,\sigma_E,\sigma_F,C_2\}$. I found no enlargement beyond $V_4$.

The correction in the theorem text is therefore substantively sound: THEO-DSL-8's $C_s$/3-D claim should be revised to $V_4$/2-D, and the $1\to 2\to 3$ pattern should become $1\to 2\to 2$.
