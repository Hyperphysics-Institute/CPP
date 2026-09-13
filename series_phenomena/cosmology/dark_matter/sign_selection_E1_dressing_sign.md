# OPEN-DM-SIGN-SELECTION-1 — reading E1 (the sign of dressing selectivity), first computation — **quark sector: S = +qCP, PASS conditional on one on-file convention; lepton sector: NOT PASSED under the same rule — the composition (+qCP, −eCP) requires a species-dependent chiral sign.**

**Patch 3528, 12 Sep 2026. DM block, from this window under PD-006.** Charter §6. Verify `code/3528_dressing_sign_E1.py` (7/7; builds the 600-cell, reproduces F.1 Theorem 5.1, computes the sign). Reasoning `reasoning/3528.md`. Nothing minted; the handedness is the registered one (n̂ = +v_host); no number chosen.

## §1 What the chirality arc supplies (D-1 read)
- Chirality is not an axiom; it enters as a Foundational Input: the primitive 4D direction n̂ (FI-C-RC-1) and the orientation bit sign(n̂) (FI-C-9), magnitude δ = χ = φ⁻³ ≈ 0.236, actualised as the DI-bit propagation-rate asymmetry r(ê) = r₀(1 + δ ê·n̂) (F.1, Mechanism A). Under **vertex-aligned Reading C the substrate direction is the host's own position, n̂ = v_host**; the residual symmetry at the host is I_h.
- **F.1 Theorem 5.1:** every host-to-first-shell direction has û_i·n̂ = −1/(2φ) ≈ −0.309, uniformly over the 12 neighbours. *A dressed centre's first shell is therefore not isotropic with respect to n̂.* This is the geometric fact that lets a sign-odd cocoon energy exist at first order in δ.
- **The polarity rule on file** (THEO-SD-CHIR-2 Finding C-W46; THEO-CHIR-CONT-3; SM-2 §10 as written): of the two ZBW configurations of a pair, the one with the −qCP at the n̂-ward (host) position is the stabilised one, with matrix element χ/6. **Convention input (stated once, flagged):** read geometrically, a shell DP whose − end lies n̂-ward of its + end (d̂·n̂ < 0, d̂ from − to +) is lowered in energy by χ·E_DP·|d̂·n̂|. If C-W46's convention is the mirror of this reading, every sign below flips; confirming the convention is part of the SM-lane corrigendum work (3524).

## §2 The computation (T1–T5)
600-cell with unit circumradius (120 vertices); host at v_host = n̂; first shell = the 12 vertices at chord 1/φ; Theorem 5.1 reproduced numerically. A centre of sign s polarises its shell radially: d̂_i = s·û_i (s = +: − ends inward). Chiral shell energy E(s) = κ Σ_i d̂_i·n̂ = κ·s·12·(−1/(2φ)) = −s·(6/φ)·κ, κ = χ·E_DP.

**Result: E(+) = −3.71 κ, E(−) = +3.71 κ; ΔF_dress = E(+) − E(−) = −(12/φ) κ.** The + centre's cocoon is stabilised, the − centre's destabilised. **S = +qCP.** Per DP the chiral factor is 1/(2φ) = 0.309 (the K3/qDP doublet's cage-shell factor is 1/6): |ΔF|/E_DP = χ/(2φ) = 0.073 per shell DP.

## §3 Readings
**E1, quark sector: PASS, conditional on the §1 convention.** The + centre dresses better; the − centre is the one undone by partner switching and returned to hDP-B — the founder's 3527 picture, with the sign from the registered geometry and handedness, not chosen. **Corollary for 3524's dilemma:** the same rule applied to SM-2 §10's object (a linear-ZBW extra on a centre; its − end toward the centre) stabilises the extra on **+qCP centres** — so the matter down quark keeps its extra *and* the + centre dresses better, from one sign. §10's "−qCP centres" is confirmed as a slip relative to the founder's composition (corrigendum strengthened, SM lane).

**E1, lepton sector: NOT PASSED (T7).** Under the same electric-polarity rule a −eCP centre (the electron) is *destabilised* and the +eCP (positron) stabilised: a rule depending on electric polarity alone makes matter quarks and *antimatter* leptons. The registered composition (+qCP, −eCP) therefore **requires the chiral coupling to carry opposite signs in the q and e sectors** — e.g. through the strong channel for q (the qCP's 3× DI-bit load) — a species-dependent sign that THEO-SD-CHIR-2's joint qDP/eDP construction either contains or refutes. This is now the charter's load-bearing check; the picture does not survive a purely electric rule.

**E2/E3 pointers (not readings, T6):** one shell DP's split is 6–19 MeV on the DP binding scales (E_eDP, E_hDP, E_qDP), a per-DP selectivity 0.19–0.74 at 2543's window; a coherent 12-DP shell saturates a → the magnitude needs E_coc (not on file) and the shell's coherence.

## §4 Owed
SM lane: confirm the C-W46 orientation convention and issue the §10 corrigendum. SD/chirality lane: the eDP-sector sign (does the joint qDP/eDP theorem give opposite signs by species?). DM lane: E_coc from the contact-polarizability scoping; then E2, E3.
