# Reasoning capture — Patch 2003: R3 / A_s from the ZBW fluctuation normalization

**STATUS: verbatim (captured at-patch).** Window: 2000-band. Opus worker; integrator = Thomas.
OPEN-COSMO-DM-2 lane, after 2001 (P(k)) and 2002 (R2 / Z₀ virial).

## The job and the honest stance
Thomas asked: can A_s ~ 2.1e-9 be DERIVED from the ZBW fluctuation normalization rather than adopted?
This is hard — standard inflation doesn't derive A_s either — so I went in willing to conclude "no,
parity with inflation" or "reduces to one undetermined input," and not to manufacture a derivation the
structure doesn't support.

## Step 1 — kill the obvious wrong answer first (falsification-first)
The naive "ZBW fluctuation normalization" is stack Poisson shot noise: ζ=δN=(1/3)δ(ln n̄),
δn̄/n̄~1/√n̄. At the pivot n̄~e^171~10^74, so A_s~(1/9)/n̄~10^-75 — off by ~67 orders, AND white (wrong
shape). So the shot-noise reading is decisively excluded. This is the honest, decisive negative to the
question as literally posed — and it's informative: it confirms the curvature is the COLLECTIVE H_eff
mode (P_ζ∝H_eff², which EU-1 already uses), not stack shot noise.

## Step 2 — the core structural result (the κ-orthogonality)
Corpus (0751 Step 4): H_eff = κ·kT·ln n̄. The tilt n_s−1 = 2 d ln H_eff/dN is a LOG-DERIVATIVE, so the
κ·kT prefactor cancels — that's why 0751 found n_s invariant across κ, kT, z₁, offset, and why n_s is a
clean zero-parameter prediction. But A_s ∝ H_eff² ∝ (κ·kT)² — the prefactor SURVIVES. So the same
invariance that protects the tilt is exactly why the amplitude is undetermined: n_s and A_s depend on
orthogonal pieces of H_eff (log-slope vs absolute scale). This is the real content — not "A_s is hard"
but "A_s carries the one coefficient n_s throws away." I found this clean and it's the heart of the
finding.

## Step 3 — what A_s reduces to
A_s = (κ·kT)²-controlled ⟺ the absolute boost scale H_*. Single-field calibration gives H_*~9e13 GeV
(GUT scale, the standard inflationary value) ⟺ κ*~2e-7. So deriving A_s ≡ deriving κ (a substrate
coupling). CPP hasn't; it's bounded (κ≪1) not pinned — parity with inflation (which leaves the inflaton
scale free), NOT deficit. Upside flagged honestly: κ is a substrate quantity, so IF a future computation
yields κ*~2e-7 from first principles, A_s becomes a prediction (a win beyond inflation). The target is
now one number, sharply posed.

## Step 4 — caught my own overstatement (the r flag)
I initially wrote r=16ε~0.14 > bound 0.036 as an "adjacent tension." Then I checked: EU-1 is a
SPECTATOR mechanism (P_ζ∝H_eff², the paper explicitly says "spectator P~H² vs single-field 1/ε"), for
which r is DECOUPLED from ε and generically smaller — so r=16ε does NOT apply and there is no clean
tension. I corrected the script and finding: r is an UNDETERMINED separate CPP quantity (owed tensor
computation), flagged as open, NOT a falsifier. Important to neither manufacture a false alarm nor hide
a real one; the honest status is "undetermined."

## Honesty boundary
- A_s NOT derived; stays adopted; parity with inflation. Shot-noise route excluded. Residual = derive κ.
- This does NOT threaten OPEN-COSMO-DM-2 or PRED-C-96 — A_s-adopted was already the R3 caveat; I
  grounded WHY (κ-orthogonality) and excluded the wrong route, rather than finding a new tension. The
  2001 P(k) closure already used A_s-adopted with exactly this honesty.

## Discipline
- Worker patch, owned greenfield path early_universe/as_amplitude_closure/ only. NO edit to EU-1,
  predictions.md, frontier — proposed registry note handed to the integrator (§8 of the finding).
- NO THEO (characterization + exclusion; A_s remains adopted). Patch 2003 in the 2000–2099 band.
