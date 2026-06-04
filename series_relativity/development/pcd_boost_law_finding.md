# Brick #4 follow-up: PCD derivation of the boost — the COUNT-vs-STRESS fork

*Patch 0746, Session 154. The decisive PCD-level attempt to derive the depth-law h(n) and settle whether
n_s = 0.9649 is a CPP prediction. Toy + verify:
`series_phenomena/cosmology/early_universe/scripts/0746_pcd_derive_boost_law.py`. NO THEO. **Result: a
genuine FORK. If the PSR_base boost is SSV-stress-driven it is mechanical → EXCLUDED (and charge
neutrality cannot save it); if it is occupation-count-driven it is entropic ∝ ln n → 0.9649. The
count-driven reading is structurally defensible because PSR_base is the SSV-independent baseline. n_s =
0.9649 is viable iff the boost is count-driven.***

## CPP grounding (master_glossary)

- Displacement / drift is driven by **SSV_net** = the *vector* sum of stress contributions (gravity =
  SSV_net gradient, c07).
- **SSV_abs** = the *magnitude*; it sets PSR and the time rate (the gravity/clock channel) and does not
  cancel.
- The DP Sea and the early cohort are net-**neutral** (dipoles; balanced mix, `DP_sea_composition`).
- The boost acts on **PSR_base**, the **SSV-independent baseline** reach: PSR_eff = PSR_base/(1 + α·SSV_abs).
  SSV only modulates PSR_base *downward* (gravity/SR). PSR_base itself is defined independent of SSV.

## The two readings of the over-occupation boost

**(i) Count-driven / configurational.** The baseline reach relaxes according to the *occupation count* n
(how over-stacked the site is), decoupled from the instantaneous SSV field. This is natural *because
PSR_base is SSV-independent by construction* — its growth need not be a stress response. The dispersal
drive of a count is the configurational chemical potential μ = μ₀ + kT·ln(n) (standard stat-mech, charge-
blind). ⇒ h(n) ∝ ln n ⇒ **n_s = 1 − 2/N_* = 0.9649.** The residual-fluctuation problem (below) does not
apply, because the drive is the count, not the field.

**(ii) SSV-stress-driven.** The boost magnitude tracks the stress the stack sources ⇒ mechanical:
- SSV_abs ∝ n ⇒ n_s = −5 (excluded), or
- SSV_net ∝ √n even for a *neutral* stack — the monopole cancels, but residual charge/multipole
  fluctuations random-walk to ∼√n ⇒ n_s = −2 (excluded).

## The decisive new content (why charge neutrality does NOT rescue the stress reading)

0745 hoped that charge neutrality would suppress the mechanical channel and expose the entropic log.
**It does not, for the stress reading.** Neutrality cancels the *monopole*, but the residual √n stress
from charge/multipole fluctuations still **dwarfs the entropic ln(n) by ~35 orders of magnitude at the
pivot** (n̄ ∼ 10⁷⁴: √n̄ ∼ 10³⁷ vs ln n̄ ∼ 10²). So if the boost is stress-mediated, it is mechanical and
excluded *regardless of neutrality*. The entropic log only operates if the boost is **decoupled from the
stress field** — i.e. the count-driven reading (i).

## Honest verdict — a genuine fork

- The data **require** reading (i): count-driven configurational ln(n) → 0.9649.
- Reading (i) is **structurally defensible**: the boost acts on the SSV-*independent* baseline PSR_base,
  so its growth being occupation/count-driven (not a stress response) is natural — arguably *more*
  natural than tying a baseline-geometry change to the instantaneous stress field.
- Reading (ii), the "everything-in-CPP-is-SSV-mediated" default, gives the **excluded** mechanical
  answer, and 0745's charge-neutrality rescue specifically **fails** for it.

So this is neither a clean win nor a clean kill. It is a sharply-posed fork with a **defensible path to
0.9649**: *n_s = 0.9649 is viable iff the PSR_base boost is count-driven/configurational rather than
SSV-stress-driven.* The escape from the mechanical/excluded answer is legitimate precisely because
PSR_base is the SSV-independent baseline.

## What changed across the arc

0738 tuning → 0741 cliff = excluded n_s=1 → 0742 n_s = 1 − p/N_* (N_* CP-fixed, p free) → 0744
smooth-vs-cliff fork → 0745 among depth-laws only entropic ln n works (favored) → **0746 the entropic
ln n is operative iff the boost is count-driven (not SSV-stress-driven); stress-driven is excluded and
neutrality can't save it.** The question is now a single, sharply-physical coupling choice.

## The remaining computation (the one that decides the sector)

Determine from the PCD rules whether the PSR_base growth under superposition is driven by the
**occupation COUNT** n (→ configurational ln n → n_s = 0.9649, a zero-parameter prediction since N_* is
CP-count-fixed) or by the **SSV STRESS** field the stack sources (→ mechanical → excluded). This is a
scaling-level analysis of a separately-posited mechanism (the H-engine), not a closed solution of the PCD
equations — so it is a sharpened fork, not a theorem. But it isolates the single coupling question that
closes or breaks the spectrum thread.

## Pointers

- Builds on 0745 (entropic favored among forms), 0744 (smooth-vs-cliff), 0742 (n_s=1−p/N_*).
- Toy + verify: `.../early_universe/scripts/0746_pcd_derive_boost_law.py`.
- Reasoning: `series_relativity/development/reasoning/0746_pcd_boost_law.md`.
- THE deciding question: is the PSR_base boost count-driven (→0.965) or SSV-stress-driven (→excluded)?
