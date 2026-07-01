# HANDOVER — Substrate-cosmology lane (2200-series): OPEN-COSMO-DM-4 REFRAMED — pin the nucleation density ε_nuc (route B, founder-chosen)
**Date:** 2026-06-30 · **Opening patch:** **2206** (2200-series; 2200–2202 G1a, 2203–2205 kT_form freeze-out) · **From:** Opus (DM 18xx lane) · **Consumer:** DM-1 · **Registered target:** **OPEN-COSMO-DM-4** (reframed, `frontier_sectors/CONJ.md`).

## ⛔ CLONE GATE
```
cd ~/Documents/GitHub/CPP && git pull --rebase origin main && git log --oneline -8
```
Confirm HEAD includes **1847** (DM consumed the over-cored result) and **1848** (founder choice of route B). Begin at **patch 2206**; grep before reserving sub-IDs. **Substrate-cosmology lane** work — DM consumes.

## WHY THE ASK CHANGED (route B, founder-chosen 1848)
The kT_form freeze-out (2204) over-cored (⟨N⟩ ~ 10⁴–10⁶). That over-shoot is a **regime error**: the equilibrium
size law ⟨N⟩ = √(φ·ν/H) assumes reversible detach, but at **E_bond/kT ~ 50 monomers don't detach** — the system is
strong-binding, so the size is set by **nucleation-and-growth**, not freeze-out temperature. The founder chose
**route B** over route A (make DM ~10²× colder): B fixes the cause, is the standard strong-binding treatment, and
is **linear** (robust) where A is **exponential** (fine-tuned). kT_form is *not* the controlling variable; ε_nuc is.

## THE ASK (substrate-cosmology lane, patch 2206+)
Derive, from CPP substrate cosmology, the **nucleation-limited Cross-Rod size**:
1. **The nucleation rate** — the rate of forming a *stable seed* (dimer/small-cluster past the nucleation barrier)
   from DM-element monomers, at the aggregation epoch.
2. **The growth rate** — the rate of monomer addition to an existing seed.
3. **The seed fraction ε_nuc = n_seed/n_monomer** — set by the competition (fast nucleation → many seeds → small
   aggregates; slow → few seeds → large). Then **N_form ~ n_monomer/n_seed = 1/ε_nuc.**
4. Compare to the dwarf target: **N_form ~ 400–1000 ⇔ ε_nuc ~ 1.0–2.5×10⁻³.**

**The decisive question:** does CPP nucleation kinetics give ε_nuc ~ 10⁻³ (order-of-magnitude), i.e. N_form in the
few-hundred-to-thousand band?
- Because N_form ~ 1/ε_nuc is **linear**, an order-of-magnitude-right ε_nuc gives an order-of-magnitude-right
  N_form — **no fine-tuning needed** (contrast route A's ~15%-pinned temperature). So an ε_nuc that comes out
  "naturally ~10⁻³" makes the dwarf normalization a **genuine (non-tuned) prediction**.
- If ε_nuc ≪ 10⁻³ (too few seeds) → aggregates too large → still over-cored. If ε_nuc ≫ 10⁻³ (too many seeds) →
  aggregates too small → under-cored. Either is a clean, non-exponential miss — and route A (DM decoupling) remains
  the fallback (non-exclusive: decoupling can shift the nucleation kinetics).

## LANE BOUNDARY
- **Substrate-cosmology delivers:** the nucleation rate, growth rate, ε_nuc, N_form, and the natural-vs-tuned
  verdict. Register under 2206+ and update OPEN-COSMO-DM-4.
- **DM consumes (NOT here):** N_form → the dwarf σ/m = K·N_form·ε_bounce normalization → the full σ/m(v) curve vs
  dwarf cores. DM 18xx lane.
- Cross-link the substrate-thermodynamic framework but **distinct from OPEN-FP-SF-2-η** (EW boson η factors).

## POINTERS
- `reasoning/1848.md` + `code/1848_nucleation_vs_freezeout_sensitivity.py` (the choice + the exponential-vs-linear
  sensitivity contrast). `reasoning/1847.md` (the over-cored consumption). `scripts/2204_kTform_freezeout.py` (the
  equilibrium bound that motivated the reframe — the over-cored ⟨N⟩ is the strong-binding signature).
- **OPEN-COSMO-DM-4** (`frontier_sectors/CONJ.md`) — reframed onto ε_nuc; the target and falsification route.
- Sibling: the kT_form handover `2026-06-30_cosmology_kTform_OPEN-COSMO-DM-4_patch2203.md` (the superseded ask).

## SUGGESTED SEQUENCE
The nucleation barrier (dimer stability vs the monomer collision/growth rate) sets ε_nuc — do that first; it is the
one number that decides the dwarf branch. Hand ε_nuc + N_form back; the DM dwarf-normalization consumption and the
held panel round 2 wait on it. If ε_nuc lands ~10⁻³ naturally, the dwarf branch becomes a genuine prediction and
the candidate is a full σ/m(v) fit; if not, route A (DM-decoupling) is the flagged fallback.
