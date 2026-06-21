# R2 / Lattice-EM — The C-vs-K Stiffness Relation From Shared Coulomb Origin

**Patch:** 2008 (21 June 2026) · **Window:** 2000-band · **Work item:** OPEN-COSMO-DM-2 residual R2
**Status of result:** **The C-vs-K residual (the §3 question of Patch 2007, and the panel-dispatch Q2) is
substantially answered in CPP's favor — by derivation, not by construction.** The on-site stiffness C and
the inter-site coupling K are the *same* Coulomb interaction at different lattice distances, so both are
linear in the common coupling strength and **K/C is exactly invariant under the SSV-screening channel**.
The natural "silly-putty" SSV channel preserves *everything* Z₀ depends on (K/C *and* the geometry d_DP/a)
→ A=0 → PASS, with no residual from that channel. A FAIL now requires an *exotic* SSV channel that
differentially distorts the intra-DP geometry relative to the fixed GP lattice.
**Verify:** `scripts/2008_ck_coulomb_ratio.py` (K/C and d_DP both Q-invariant to 0.0e+00 across 8× Q).
**Discipline:** worker patch; owned path `mu_eps_closure/lattice_ck/`; no shared-registry/c06 edit.

---

## 1. The question, and the circularity trap

Patch 2007 hardened R2 (single-response structure is corpus-derived: B=∇×P) but left one honest residual:
the electric energy is on-site (stiffness C → ε₀∝nq²/C); the magnetic energy is the gradient/curl of the
displacement (inter-site coupling K). Is K rigidly locked to C under SSV (Z₀ geometric → PASS) or can it
split (FAIL)? The trap (flagged by the integrator): a lattice model built to taste could cancel C *by
construction* — circular. So the discipline here is to derive C and K from a **shared physical origin**,
not to assume them equal or independent, and to read off only what is robust.

## 2. The one corpus input, and the derivation

Corpus input (0739): the CP–CP interaction is **Coulomb-like**. Take it. Then both stiffnesses are
curvatures of the *same* Coulomb-derived pair potential (Coulomb attraction + short-range core, so a bound
minimum exists), evaluated at different separations:
- **on-site** `C = U''(d_DP)` — curvature at the intra-DP equilibrium separation d_DP;
- **inter-site** `K = U''(a)` — curvature at the GP spacing a = l_P.

Write the common Coulomb strength `Q = q²/(4πε₀)` (the same charge, the same Sea screening). SSV acts
through Q (silly-putty stiffening = changing the effective screening). The script sweeps Q by 8× and reads
off C, K, K/C, and d_DP.

**Result (robust, sign-independent):** C and K are *both linear in Q* (C: 34.99→279.88, K: −0.89→−7.14,
each exactly ×2 per ×2 of Q), because both are curvatures of the same Q-scaled potential. Therefore:

> **K/C is exactly Q-invariant** (0.0e+00 across the 8× sweep). The SSV-screening channel cancels in the
> ratio — moving C and K identically.

And, stronger than anticipated:

> **d_DP is also exactly Q-invariant.** Scaling the common Coulomb strength does not move the bond minimum
> (the equilibrium balance is scale-invariant). So the geometric ratio d_DP/a is preserved too.

(The negative sign of K and its precise value are toy-potential artifacts — the inter-site curvature at a
bare-pair separation a is not the real collective-mode coupling. What is robust and physical is the
**Q-linearity of both stiffnesses**, hence the **Q-invariance of K/C** — independent of sign or the core
details.)

## 3. What this means for Z₀ and R2

Z₀ = √(μ₀/ε₀) depends on the *ratio* of the magnetic (K-governed) to electric (C-governed) responses. The
natural SSV channel (uniform Coulomb screening, the silly-putty picture) moves C and K identically (K/C
fixed) and leaves d_DP/a fixed — so it preserves the ratio entirely and moves only the common scale (the
product μ₀ε₀=1/c², i.e. c varies = gravity). **A=0 → PASS, with no residual from the silly-putty channel.**
This is exactly c06 line 185's prediction (geometric Z₀), now derived rather than asserted, and it is the
favorable answer to the 2007 §3 residual and the panel-dispatch Q2.

## 4. The residual — now very narrow, and honest about the boundary

- **A FAIL requires an exotic SSV channel** that changes the geometric ratio d_DP/a *directly* — i.e. one
  that differentially distorts the intra-DP separation while the GP lattice (a = l_P) stays fixed/eternal
  (Brick #2). The silly-putty screening channel demonstrably does not do this. Sensitivity:
  `A ~ 3·|δ(d_DP/a)/(d_DP/a)|`, so even such a channel would have to move d_DP/a by >10⁻⁶ to threaten the
  clock bound.
- **Sub-residual:** whether the DP exclusion core scales with the EM coupling (→ d_DP fully Q-rigid, as in
  the toy) or is a fixed Planck-scale exclusion (→ a small d_DP shift under SSV). This is the one decidable
  microphysics input left, and it is narrow.
- **NOT attempted (circularity discipline):** the *absolute* Z₀ in lattice units. That needs the full c06
  EM Lagrangian with a self-consistent ε₀, and building it here would risk cancelling C by construction.
  The **ratio** result (K/C Q-invariant) is what is robust and non-circular, and it is what R2 needs.

## 5. R2 status after this patch

- **2002:** PASS conditional on an un-derived single-oscillator cartoon.
- **2007:** single-response structure (B=∇×P) shown corpus-derived; residual = C-vs-K stiffness locking.
- **2008 (this patch):** C-vs-K locking *derived* from shared Coulomb origin (K/C Q-invariant); the natural
  SSV channel gives full PASS. **Residual reduced to an exotic differential-distortion channel + the DP
  core-scaling sub-question, both narrow and favored toward PASS.**
- **Clean-kill exposure:** now requires a specific, exotic, un-suggested SSV channel — a long way from the
  open ~6-order falsifier R2 began as. R2 is, in substance, a conditional PASS with a narrow, characterized
  residual.

## 6. For the panel dispatch / integrator

This result strengthens the dispatch (`R2_panel_dispatch.md`): Q2 can now be posed as "here is the derived
K/C Q-invariance — can you construct an SSV channel that moves d_DP/a relative to the fixed lattice?" rather
than the open "is K locked to C?". Proposed c06 cross-ref (for the integrator's batch): annotate the owed
μ₀,ε₀(C,c) computation that the *ratio* part is settled (K/C geometric via shared Coulomb origin, 2008);
only the absolute normalization and the d_DP-rigidity sub-question remain.

NO THEO (derivation of a stiffness ratio + residual localization; no new axiom/term/counted prediction).
