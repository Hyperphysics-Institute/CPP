# Brick #4 follow-up: auditing the swarm's H-micro-rules — architecture right, ln(n) not yet produced

*Patch 0747, Session 154. Audits the count-driven H-micro-rules proposed by the swarm (Thomas +
Copilot). Toy + verify: `series_phenomena/cosmology/early_universe/scripts/0747_microrule_audit.py`.
NO THEO. **Result: the conceptual architecture is correct (count-driven PSR_base, decoupled from the
gravity SSV), but the specific rules proposed do NOT give ln(n) — they give the excluded values (n_s =
−5 or the n_s = 1 cliff). There is also an internal inconsistency: a potential linear in n cannot give a
boost logarithmic in n unless the boost couples to the chemical potential, not the raw count. n_s =
0.9649 remains viable-and-favored (0746), not derived.***

## What is right (and it is real progress)

The swarm's architecture matches the 0746 favorable branch and should be kept:
- CPs move along **SSV_net** gradients (direction) — unchanged.
- **PSR_eff = PSR_base/(1+α·SSV_abs)** (gravity/SR) — unchanged.
- The H-engine acts on **PSR_base** (the SSV-independent baseline), driven by **over-occupation count**,
  decoupled from the gravity SSV_abs. ✓ (this is the count-driven branch, the only non-excluded one)
- Exponential expansion needs no extra multiplier: a multiplicative per-tick update
  PSR_base ← (1+H(n))·PSR_base is already exponential. ✓ (Thomas's instinct correct)

## What fails: the specific micro-rules do NOT give ln(n)

Per-tick boost H(n), n_s − 1 = 2 d ln H(n̄)/dN, pivot N_rem ≈ 57. Need H(n) ∝ ln n. Audit result:

| proposed rule | H(n) | n_s | verdict |
|---|---|---|---|
| R1 Thomas "2 CPs → PSR_base doubled" (boost ∝ count n) | ∝ n | −5.00 | EXCLUDED (mechanical) |
| R2 Copilot flux P∝1/(n_j+ε), gross outward ∝ n | ∝ n | −5.00 | EXCLUDED; and net flux ≈ 0 for a uniform stack (needs a gradient) |
| R3 Copilot "Π/n" = (n−1)/n | (n−1)/n | **1.0000** | EXCLUDED — saturates to a constant → the HZ **cliff**, not "ln n in disguise" |
| R4 harmonic / chemical-potential (k-th CP ∝ 1/k) | Σ1/k ≈ ln n | 0.9650 | gives 0.965 — **but not among the proposed rules** |
| R5 reference (asserted) | ln n | 0.9649 | gives 0.965 — asserted, not derived |

Specifics:
- **R1 / Thomas's "doubles per CP"** is boost ∝ over-occupation count = linear = the excluded mechanical
  branch (n_s = −5). Copilot correctly flagged this one.
- **R2 / flux** has two problems: the gross outward tendency ∝ n (linear, excluded), and the *net* flux
  needs a concentration **gradient**, so a roughly uniform over-dense early patch has net flux ≈ 0 →
  no expansion at all. Dispersal-flux cannot drive uniform expansion.
- **R3 / "Π/n"** does NOT coarse-grain to ln n. (n−1)/n **saturates to a constant** (~1) for large n, so
  H ≈ const → exact de Sitter → n_s = 1 (the Harrison–Zel'dovich cliff, already excluded). Note
  (n−1)/n → 1 while d(ln n)/dn = 1/n → 0 — opposite behaviors. It is the cliff in disguise, not the log.

## The internal inconsistency (the crux)

The proposal asserts **both**: (a) each CP contributes one unit of over-occupation potential, so the
potential = n ("n increments of SSV"); and (b) the boost H ∝ ln n. **These are incompatible** if the
boost is proportional to the potential: potential = n and H ∝ potential ⇒ H ∝ n (linear) ⇒ n_s = −5.

You cannot have a *linear* potential and a *logarithmic* boost unless the boost couples to the
**chemical potential** μ(n) = dF/dn ∝ ln n — the per-CP *entropy derivative* — rather than to the raw
count. "Boost ∝ count" is linear (excluded); "boost ∝ chemical potential of the count" is log (0.965).
The proposal conflates these, and relabeling n as "occupancy SSV" does not fix it — if the boost tracks
that channel's *amount* (n), it is still linear.

## What an ln(n)-producing rule actually requires

H(n) ∝ μ(n) = d/dn[ configurational free energy of n CPs on a GP ] ∝ ln n — equivalently, the per-CP
contribution must **diminish** so the total is the harmonic sum: the k-th stacked CP contributes ∝ 1/k,
giving Σ1/k = H_n ≈ ln n. A candidate CPP-native mechanism for the diminishing 1/k: **screening** — the
k-th CP to stack is buried behind the k−1 already present, so it couples to only the ~1/k unscreened
fraction of the dispersal drive. That would turn the count into ln(count). But "why exactly 1/k" needs
its own CPP justification; it is a candidate, not a derivation.

## Honest status

- **Architecture: correct and kept.** Count-driven PSR_base, decoupled from gravity SSV_abs; SSV_net for
  direction; multiplicative (exponential) update. The swarm got the structure right.
- **The ln(n)-producing micro-rule: NOT yet in hand.** Every proposed rule gives an excluded value
  (linear → −5, or the (n−1)/n cliff → 1). The log requires boost ∝ chemical potential ∝ diminishing/
  harmonic per-CP contributions, which none of the proposals implement, and which needs a CPP reason for
  the 1/k diminishing (screening is a candidate).
- So n_s = 0.9649 stays where 0746 left it: **viable and favored** (the count-driven branch is the only
  non-absurd one, and it lands on Planck *if* the boost is logarithmic in the count), **not derived**.
  The swarm's micro-rule attempt does not close the gap; it sharpens it to a single concrete demand:
  *show that the per-CP boost diminishes as 1/k (chemical-potential / screening), turning count into log.*

## Pointers

- Builds on 0746 (count-vs-stress fork). Audits the swarm proposal (Thomas + Copilot transcripts).
- Toy + verify: `.../early_universe/scripts/0747_microrule_audit.py`.
- Reasoning: `series_relativity/development/reasoning/0747_microrule_audit.md`.
- THE remaining task: a CPP-native rule with diminishing per-CP boost (∝1/k, e.g. screening) whose
  coarse-graining *provably* gives ln n (chemical potential), not asserted by analogy. That, plus N_*
  fixed by the CP count, would make n_s = 0.9649 a derived zero-parameter prediction.
