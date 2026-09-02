# CONV-038 Q1 — The retirement dependency sweep (owed by rule, 3–2) — **and the tombstone was wrong: the rule was not retired, it was DEMOTED TO A THEOREM (THEO-1), and that record has been in `theorem-registry.md` since 13 April 2026**

**Patch 3372, Session 161, 2 Sep 2026.** Reasoning `reasoning/3372.md`. Corrects the Patch-3366 tombstone by dated note (anti-erasure).

## §0 The finding against the worker, first

Patch 3366's tombstone row says: *"The founder states the rule was eliminated earlier as unnecessary; **no prior patch recorded the retirement** — this row is the tombstone."* **That sentence is false.** `theorem-registry.md` row **THEO-1 — CP Non-Persistent Co-Occupation** (entered 13 April 2026, commit 65acc6c0; source `propositions.md` §1, now in `archive/pre_frontier_2026-04-12/`) reads:

> *Two CPs cannot persistently occupy the same Grid Point. Same-polarity: repulsive SSV prevents approach. Opposite-polarity: superimposition lasts exactly one Absolute Moment (bulk SSV drives separation). **CP Exclusion Postulate is redundant — it's a theorem.** Axiom count reduced from 7 to 6.* [AXIM-1, AXIM-2, AXIM-4]

with corollary **CORL-1a** (ZBW turning point at Grid-Point superimposition; f_ZBW derived) and **CORL-1b** (stochastic partner exchange). This is exactly the founder's 31-Aug account — *"we eliminated it when we realized that it was unnecessary. We used the ZBW effect instead"* — and it was on the record all along. I grepped `axiom-registry.md`, `master_glossary.md` and `founders_vision.md` for "Exclusion" at 3366 and did not grep `theorem-registry.md`, because I was looking for a retired *axiom* and it had become a *theorem*. The panel's Q1 gap (GPT, Copilot, Grok: "replacement slogan, not derivation") was pointing at THEO-1; it has a proof.

**What actually happened, corrected:** the CP Exclusion *Postulate* (kinematic: co-occupation forbidden) was demoted to THEO-1 (dynamical: same-polarity CPs never reach superimposition because their SSV_net is repulsive; opposite-polarity CPs superimpose for exactly one Moment and separate). The *content* survived as a theorem; the *postulate* was removed. The GR lane (GR-1b, GR-1c) inherited the pre-demotion postulate text, read it as a packing floor, and derived `PSR ≥ l_P/2` from it. **THEO-1 says nothing about the PSR.** OPEN-GR-FLOOR-1 is unchanged: the floor still has no derivation from THEO-1, because THEO-1 constrains co-occupation, not perception radius.

## §1 Sweep results — 93 files; the load-bearing ones

Method: every `.tex`/`.md` outside archival transcripts, ten pattern strings (`Exclusion Rule`, `one CP per GP`, `occupy the same`, `identity conservation`, `drives the initial expansion`, `Exclusion floor`, `GP Exclusion`, `no two CPs`, …). 93 files hit; 40 are development notes, archives, or already-annotated GR-lane records. The dependants that matter, by what they *use*:

### 1a. Papers using THEO-1's CONTENT under the old NAME, citing c01 (which never contained it) — content correct, citation wrong

| Paper | Line | What it says | Reading |
|---|---|---|---|
| c02 (SR) | 198 | "maintained dynamically by the CP Exclusion Rule (if two CPs occupy the same GP at the same t_abs, both instantly displace to the PSR edge …)" | **dynamical — THEO-1** |
| c03 (SR) | 405 | "if two CPs occupy the same GP at the same t_abs, both displace to the PSR edge … candidate mechanism for Pauli exclusion" | **dynamical — THEO-1** |
| c04 (SR) | 178, 206, 297 | "no second CP can occupy the same GP" as the ZBW inner reflection boundary; "prevents the cloud from collapsing to zero radius" | kinematic phrasing, dynamical function — THEO-1/CORL-1a |
| c06 (SR) | 213 | "provides the inner reflection boundary for standing ZDC patterns" | THEO-1/CORL-1a |
| SPIN-1 (QM) | 460 | "provides the inner boundary node at r = 0" | THEO-1/CORL-1a |

**Owed (SR and QM lanes):** citation corrigenda — cite THEO-1 (`theorem-registry.md`), not c01 §2; c04's kinematic phrasing at 178 re-worded to THEO-1's. No physics changes.

### 1b. Papers attributing `PSR ≥ l_P/2` to the rule — inherit OPEN-GR-FLOOR-1

| Paper | Line | What it says |
|---|---|---|
| GR-1 (umbrella) | 364 | "The CP Exclusion Rule imposes … the Planck core" |
| SM-11 | 568 | "The CP Exclusion Rule (PSR_eff ≥ l_P/2) … provides the PSR attenuation underlying asymptotic freedom" |
| SM-12 | 986 | "CP Exclusion Rule (companion 1): the minimum PSR (≥ l_P/2) governs the scale at which quark-vertex bonds form" |
| GR-1d, GR-1e, GR-1f, GR-1g | various | "Exclusion floor" / "Exclusion Rule" as the core floor |

**Owed:** GR-1, GR-1d–g: dated pointer to GR-1c Corrigendum 3 (GR lane, next enactment). **SM-11, SM-12 (SM lane):** the `l_P/2` they use is a conditional bound with an open value (window 0.536 < u_max ≤ 1); whether asymptotic-freedom attenuation (SM-11) or the vertex-separation scale (SM-12) is *sensitive* to the floor value is an SM-lane question — registered in `frontier_sectors/SM.md`, not answered here.

### 1c. The two "jobs" the panel asked about

- **"CP identity conservation"** (GR-1c remark): done by A1′/A4 — no CP is created or destroyed at any GP; every departing CP arrives at exactly one GP (GR-1b's own "Nexus" paragraph). Not by Exclusion. No orphan.
- **"Drives the initial expansion"** (GR-1b): THEO-1's same-polarity repulsion + CORL-1a separation is the mechanism; the founder's Axiom H (founders_vision §6e) is its proposed inflationary extension. Not orphaned; still open as cosmology (OPEN-EU / CONJ-COSMO-3), unchanged by this sweep.

### 1d. Registries

- `theorem-registry.md` THEO-1: live, correct, **the tombstone**.
- `axiom-registry.md`: the 3366 row is corrected (below). THEO-1 is the referent, not "retired."
- `master_glossary.md`: no entry for THEO-1 / "CP Exclusion" — **glossary entry owed** (a two-line one: the name, the demotion, the pointer).

## §2 Consequence for the R-core arc and the wall

Nothing in FLOOR-1 changes. But the wall-condition item gains its physics: THEO-1's proof is for an *isolated pair* — same-polarity CPs never superimpose because their mutual SSV_net is repulsive. The founder's 31-Aug surface picture has CPs driven onto occupied GPs by an *external* SSV_net (the impact). Whether THEO-1's "never" survives external drive — i.e. whether a same-polarity co-occupation can be *forced* for one Moment — decides whether the surface layer's compliance is opposite-polarity-only (a DP-sea response) or general. That is the one question to put to the founder before the impedance computation.

## §3 Tombstone correction (enacted in `axiom-registry.md`, dated note)

The row title "CP Exclusion Rule — retired" stands as the ledger entry the founder asked for; the dated note records that the retirement *was* recorded — as THEO-1 — and that what the GR lane invoked was the pre-demotion postulate.
