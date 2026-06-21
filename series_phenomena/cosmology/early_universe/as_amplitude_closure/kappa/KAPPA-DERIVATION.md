# R3 / Derive-κ: Can the Boost Coupling Be Derived, or Is It a Posited Constant?

**Patch:** 2004 (21 June 2026) · **Window:** 2000-band · **Work item:** OPEN-COSMO-DM-2 residual R3
(the genuine prize: if κ derives, A_s becomes a prediction beyond inflation)
**Status of result:** **κ does NOT derive from the current corpus. It is the *magnitude* of the H-engine
boost law — the refined form of the H-axiom constant that brick4 explicitly carries as "constant by
axiom, NOT derived." The smallness is localized cleanly to κ. A_s stays adopted (parity with inflation);
the R3 residual is sharpened from "derive A_s" to "derive one axiom-level constant, the H-engine boost
coupling κ."** This is an honest negative — the prize is not there — with the residual located precisely.
**Verify:** `scripts/2004_kappa_localization.py`
**Discipline:** worker patch; owned path
`series_phenomena/cosmology/early_universe/as_amplitude_closure/kappa/`; no shared-registry/EU-1 edit.

---

## 1. The target

R3 (Patch 2003) reduced A_s to one number, the boost coupling κ in `H_eff = κ·kT·ln n̄`. Deriving κ from
substrate structure would turn A_s from adopted to predicted — a win standard inflation lacks. This patch
attempts that derivation, falsification-first: willing to find that κ does not derive, and to report
exactly where it lives rather than reach for a number.

## 2. Where κ lives — and where it does not

`H_eff = κ·kT·ln n̄` (0751). The n_s arc (Patches 0741–0751) derived the **shape** of this boost law —
that `H_eff ∝ ln n̄` (the chemical-potential / A1-indistinguishability log), which forces the tilt p=2 and
gives `n_s = 0.9649`. What it did **not** fix is the **magnitude** — the proportionality κ. And κ is the
refined form of the H-axiom constant, which the corpus carries explicitly as posited:

> brick4, item 2: *"H — constant fractional PSR_base boost per superposed tick (the engine; **constant by
> axiom, NOT derived**)."* H-axiom status (0738): *evaluated-not-adopted → **adopted**-as-working-engine,
> gate passed at toy level.*

So κ is not a derived combination of the other axioms — it is (proportional to) an **axiom-level
constant** that CPP posits. This is the clean structural statement of the R3 residual:

> **The n_s arc fixed the boost law's SHAPE (→ tilt, derived); κ is its MAGNITUDE (→ amplitude, posited).**
> These are the orthogonal pieces of one boost law — the κ-orthogonality of Patch 2003, now traced to its
> source: the magnitude is the H-axiom constant, the shape is the chemical-potential structure.

## 3. The smallness is localized to κ (not kT, not the superposed fraction)

`A_s ∝ (κ·kT)²`, and the observed A_s requires a small `κ ~ 2×10⁻⁷` (single-field calibration; order
10⁻⁷–10⁻⁶ given the spectator-vs-single-field uncertainty). The smallness is **forced into κ itself**,
because the other factors are pinned:

- **kT** is pinned ~E_Pl by LEMMA-NS-BATH (Patch 0767) — not the small factor.
- **The superposed fraction f_sup** is ~1 at the pivot (occupancy `n̄ ~ 10⁷⁴`, almost all GPs stacked) —
  not the small factor. (And a small f_sup would *kill the tilt*: a constant boost gives the n_s=1 cliff,
  Patch 0741. So f_sup cannot be the source of smallness without breaking n_s.)

So `A_s ~ (κ·kT)²` with the smallness unavoidably in κ: the per-Moment boost is `H_eff·t_P = κ·ln n̄ ~
4×10⁻⁵` at the pivot — the H-engine barely nudges PSR_base each Absolute Moment, and this gentleness is
exactly the (posited) small boost coupling.

## 4. Falsification fences — κ is neither derived nor excluded

Is κ *forced* to an excluded value by known structure? No, in both directions:
- `κ ~ O(1)` (the naive H-axiom "superposition ~doubles the rate") → `A_s ~ 10⁴` — wildly excluded.
- `κ ~ e⁻¹⁷¹` (the Poisson shot-noise scale) → `A_s ~ 10⁻¹⁵⁰` — wildly excluded (= the 2003 result).
- `κ ~ 2×10⁻⁷` (target) → `A_s = 2.1×10⁻⁹` — observed; **allowed, but not forced.**

Known CPP structure neither derives κ ~ 10⁻⁷ nor excludes it. It is genuinely open and posited — the
same epistemic status as the inflaton energy scale in standard inflation. **Parity, not deficit, not
tension.**

## 5. A numeric coincidence — flagged as a where-to-look hint, explicitly NOT evidence

`κ_target ~ 2.2×10⁻⁷`; `α³ = 3.9×10⁻⁷` (ratio 0.57). The order is suggestively near `α³`, which *would*
be natural **if** the per-superposition boost is EM/SSV-mediated (superposed CPs interact
electromagnetically). I record this so the direction is not lost — **but the single-field calibration
uncertainty (a factor of a few to ten) exceeds the α³ discrepancy**, so this is at most a hint for where
the H-engine-rate derivation might look, and is **NOT evidence and NOT a derivation**. I flag it
deliberately at non-evidence strength to neither bury a possible lead nor manufacture a false match.

## 6. Honest verdict (derive-κ)

- **κ does not derive.** It is the magnitude of the H-engine boost law, carried as a posited axiom-level
  constant (brick4 "constant by axiom, NOT derived"). The n_s arc fixed the *shape*; κ is the *magnitude*
  it structurally could not reach.
- **A_s stays adopted.** Parity with standard inflation (which posits the inflaton scale). Not a tension.
- **R3's open target is now maximally sharp:** derive the H-engine boost coupling κ (≡ the per-Moment
  superposition-boost rate) from A1–A11. If that yields κ ~ 10⁻⁷, A_s becomes a prediction — but this
  requires deriving an axiom-level constant, a genuine open problem (and the corpus's own framing is that
  the H-axiom constant is posited). Candidate direction (non-evidence): an EM/SSV-mediated boost, order
  α³.

This **slightly downgrades** the 2003 optimism ("if κ falls out of substrate structure, A_s becomes a
prediction"): the corpus carries κ's progenitor as a posited axiom constant, so the path to predicting
A_s runs through deriving the H-axiom constant itself — harder than a generic substrate computation.
That is the accurate, non-inflated status.

## 7. OPEN-COSMO-DM-2 residual ledger (post-2004)

- R1 (P(k)): DONE (2001).
- R2 (VSL μ↔ε): PASS-conditional on single-oscillator structure (2002).
- **R3 (A_s): adopted; reduced to the posited H-axiom boost coupling κ (target ~2×10⁻⁷). The genuine
  prize (derive κ) is NOT available from the current corpus — κ is an axiom-level constant. Parity with
  inflation; not a tension. (2003 + 2004.)**
- R4 (OPEN-EU-1 depth): unchanged; deriving the H-axiom constant is naturally part of this deeper layer.
- Owed (low priority): EU-1 tensor ratio r (spectator-sector, 2003).

## 8. Proposed registry note — FOR THE INTEGRATOR'S BATCHED PATCH (not edited here)

> **`frontier_sectors` OPEN-EU-1 (or a new low-priority owed item):** the A_s amplitude reduces to the
> H-engine boost coupling κ (target ~2×10⁻⁷), which is the magnitude of the boost law whose *shape* the
> n_s arc derived; κ is the refined H-axiom constant, posited ("constant by axiom, NOT derived", brick4),
> so A_s is adopted at the same epistemic level as the inflaton scale in standard inflation (parity).
> Deriving κ from A1–A11 (candidate: EM/SSV-mediated superposition boost, order α³ — a hint, not
> evidence) would promote A_s to a prediction. Patches 2003 + 2004.

NO THEO (negative result + localization; A_s remains adopted; no new axiom/term/counted prediction; the
α³ note is explicitly non-evidence).
