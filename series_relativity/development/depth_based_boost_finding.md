# Brick #4 follow-up: depth-based boost — near-scale-invariance selects the ENTROPIC (log) law → p = 2

*Patch 0745, Session 154. Tests the depth-based H-boost (Thomas + Copilot: deeper stacks push harder).
Toy + verify: `series_phenomena/cosmology/early_universe/scripts/0745_depth_based_boost.py`. NO THEO.
**Result: among depth-based laws, near-scale-invariance UNIQUELY selects the logarithmic (entropic /
chemical-potential) form, which gives p = 2 / n_s = 0.9649 on the nose. This is consistent-and-favored
(physically natural + data-selected + correct running), but the entropic character is assumed, not yet
PCD-derived. p = 2 is upgraded from "a wish" (0744) to "favored and consistent" — short of proven.***

## What was tested (honestly — derive the law, don't assume the log)

The per-tick fractional PSR boost is h(n), a function of stack depth n. H_eff(N) = h(n̄(N)), and
n_s − 1 = 2 d ln H_eff/dN. Six physically-distinct depth-laws, evaluated at the observable pivot
(N_rem ≈ 57):

| physical picture | h(n) | n_s | assessment |
|---|---|---|---|
| (a) fraction / on-off (literal axiom) | const | 1.0000 | HZ — excluded |
| (b) mechanical, linear (each CP equal push) | ∝ n | −5.00 | **absurd — wildly excluded** |
| (c) mechanical, pairwise repulsion | ∝ n² | −11.0 | **absurd — wildly excluded** |
| (d) screened / surface | ∝ n^{2/3} | −3.00 | **absurd — wildly excluded** |
| (e) **entropic / chemical-potential** | **∝ ln n** | **0.9649** | **matches Planck** |
| (f) tuned weak power | ∝ n^{0.0055} | 0.9670 | matches, but fine-tuned |

## The key finding (and an important correction to the intuition)

**Any power-law "deeper pushes harder" is catastrophically excluded.** A boost that scales linearly
(or as any power) with stack depth gives n_s = −5, −11, −3 — absurd. So the naive reading of "deeper
stacks push harder" — a *linear* larger increment with depth — does **not** work; it is ruled out hard.

The intuition is right in *direction* but must be **logarithmic, not linear**: the boost may grow with
depth, but only as **ln(depth)**. A 10³⁰-deep stack then boosts only ~30× harder than a 10-deep stack
(the log ratio), not 10²⁹× harder. That gentle, saturating logarithmic growth is the *only* depth-law
that yields a sensible near-scale-invariant spectrum — and it lands on n_s = 1 − 2/N_* = 0.9649.

## Is the log motivated, or reverse-engineered? (the honest question)

The log is **not** the mechanical "deeper pushes harder" (that's power-law → absurd). It is specifically
the **entropic / chemical-potential** form: the drive to disperse an over-concentrated species is
μ = μ₀ + kT·ln(c) — logarithmic in concentration, standard statistical mechanics. Thomas's physical
story is literally "the lattice relaxing extreme over-occupation toward the 1-CP-per-GP equilibrium" —
a **dispersal** process, whose driving potential is exactly the entropic μ ∝ ln(n). So *if* the H-boost
is the entropic dispersal pressure (not a mechanical repulsion), h ∝ ln(n) is the natural, textbook
form, **not a tuning**, and p = 2 / n_s = 0.9649 is a consequence.

This is favored **three ways**: (i) physical naturalness — the chemical potential of dispersal is the
standard log; (ii) uniqueness — it is the *only* depth-law consistent with near-scale-invariance
(mechanical/power laws give absurd spectra); (iii) running — the log gives the correct small negative
running (n_s = 1 − 2/N form), whereas a tuned power gives the wrong constant running.

And the precise value is **not circular**: only the *qualitative* near-scale-invariance is used to select
the log; the *quantitative* 0.9649 then follows from N_* = (1/3)ln(N_CP) fixed independently by the CP
count (Brick #4 Test C). We did not use 0.965 to pick the law.

## Honest status

- **Consistent-and-favored, not yet derived.** The load-bearing assumption is that the over-occupation
  relaxation is **entropic** (μ ∝ ln n, dispersal) rather than **mechanical** (∝ n^q, repulsion).
  Mechanical → absurd; entropic → 0.9649. Both the physical story ("dispersal toward equilibrium") and
  the data (near-scale-invariance) point to entropic, but a PCD-level derivation that the relaxation is
  entropic-logarithmic is still owed.
- **If that derivation confirms the entropic ln(n)**, then with N_* fixed by the CP count, **n_s =
  0.9649 becomes a zero-parameter CPP prediction** and the spectrum thread closes.
- Net arc: 0738 tuning → 0741 cliff/excluded → 0742 n_s = 1 − p/N_* (N_* CP-fixed, p free) → 0744 p =
  smooth-vs-cliff fork → **0745 depth-based + entropic selects log → p = 2 favored & consistent.**

## The remaining first-principles step (sharp)

Derive from the PCD / superposition dynamics that the over-occupation relaxation drive is the
**entropic chemical potential ∝ ln(n)** (dispersal), as opposed to a mechanical ∝ n^q repulsion. The
data and the dispersal story both favor entropic; the mechanical readings are excluded. Confirming the
entropic form at the substrate level turns p = 2 / n_s = 0.9649 from "favored" into "predicted."

## Pointers

- Builds on 0744 (smooth-vs-cliff fork) and 0742 (n_s = 1 − p/N_*, N_* from CP count).
- Toy + verify: `.../early_universe/scripts/0745_depth_based_boost.py`.
- Reasoning: `series_relativity/development/reasoning/0745_depth_based_boost.md`.
- THE remaining computation: PCD-level derivation that over-occupation relaxation is entropic (∝ ln n),
  not mechanical (∝ n^q).
