# HANDOVER — Substrate-cosmology lane (2200-series): OPEN-COSMO-DM-4 — pin kT_form (the DM formation-size make-or-break)
**Date:** 2026-06-30 · **Opening patch:** **2203** (2200-series; 2200–2202 were the SF-2/SF-5 G1a work) · **From:** Opus (DM 18xx strip-then-fuse lane) · **Consumer:** DM-1 · **Registered target:** **OPEN-COSMO-DM-4** (`frontier_sectors/CONJ.md`).

## ⛔ CLONE GATE (before anything)
```
cd ~/Documents/GitHub/CPP && git pull --rebase origin main && git log --oneline -8
```
Confirm HEAD includes the DM consolidation + formation calc (**1842–1846**) and OPEN-COSMO-DM-4. Begin at **patch 2203**; grep the registry before reserving any sub-ID. This is **substrate-cosmology lane** work — **DM consumes** the result; do not do the DM consumption here.

## WHY THIS IS THE MAKE-OR-BREAK
The Cross-Rod DM candidate is, after this session, reduced to a single open quantity. Cleared/predictive already: the **cluster** floor (E_qq/E_qq hinge, g ≈ 0.02, pure geometry), the **cluster σ/m ∝ 1/v²** branch (near-parameter-free, Bullet-safe), and dilution (two-channel chaperone). The one open branch is the **dwarf** normalization, and it lives entirely on the **formation size** N_form — which reduces to **kT_form**.

## THE REDUCTION (DM-lane result, 1846 — inherit, don't re-derive)
Cross-Rod aggregation is reversible equilibrium polymerization:
- ⟨N⟩ = √φ · exp(E_bond/2 kT_form), and at freeze-out (detach rate ν_PCD·exp(−E_bond/kT_form) = H_form):
- **⟨N⟩ = √(φ · ν_PCD / H_form)** — the formation size is √ of (PCD attempt frequency / Hubble rate at freeze-out).
- Dwarf normalization needs **N_form ~ 400–1000 elements** ⇒ **E_bond/kT_form ~ 12–14** ⇒ **kT_form ~ E_bond/13**.
- For the element–element **E_qq** detachment bond (E_bond ~ 66–264 MeV): **kT_form ~ 4.7–19 MeV**.
- **Exponentially sensitive:** a factor ~3 in kT_form spans ~4 orders in ⟨N⟩ ⇒ kT_form needs pinning to ~10–15%.

## THE ASK (substrate-cosmology lane, patch 2203+)
Derive, from CPP substrate cosmology:
1. **ν_PCD** — the PCD attempt frequency governing element attach/detach at a rod end (a substrate microphysics rate).
2. **H_form** — the Hubble rate at the epoch when DM aggregation freezes out (the relic epoch).
3. **E_bond** — confirm the element–element detachment energy (the E_qq spine-bond count at the inter-element interface; SF-2/SF-5-adjacent).
4. From these, **kT_form** (via freeze-out ν_PCD·exp(−E_bond/kT_form) = H_form) and hence **⟨N⟩ = √(φ·ν_PCD/H_form)**.

**The decisive question:** does the substrate thermal history put kT_form in the ~10–15% window around E_bond/13 (⟨N⟩ ~ 400–1000)?
- If **yes and naturally** → N_form is a **zero-parameter prediction** → the dwarf branch is secured → the whole σ/m(v) fit is parameter-light.
- If it lands there only by tuning → N_form is a **fine-tuning** → report honestly (weakens, not necessarily kills — the cluster branch stands regardless).
- If **outside the window** → ⟨N⟩ misses by orders → the dwarf normalization **fails** (too small: no dwarf cores; too large: over-cored) → this is the candidate's kill route.

## LANE BOUNDARY
- **Substrate-cosmology delivers:** ν_PCD, H_form, kT_form, ⟨N⟩ (and the natural-vs-tuned verdict). Register under 2203+ and update OPEN-COSMO-DM-4.
- **DM consumes (NOT here):** ⟨N⟩ → the dwarf σ/m = K·N_form·ε_bounce normalization → the full σ/m(v) curve vs dwarf cores. DM 18xx lane.
- Cross-link the substrate-thermodynamic framework (OPEN-FP-SF-2-EWSB/shelldens/chaincomp) — the same "equilibrium/effective-temperature/ensemble" machinery — but **distinct from OPEN-FP-SF-2-η** (that is the EW boson η dilution factors, unrelated).

## POINTERS
- `reasoning/1846.md` + `code/1846_formation_size_kTform.py` (the reduction; run it). `reasoning/1845.md` (why N_form ~ 400–1000: the dwarf normalization + the σ/m ∝ 1/v² cluster branch).
- **OPEN-COSMO-DM-4** (`frontier_sectors/CONJ.md`) — the registered target, falsification route.
- `DM-1/section5_velocity_rescope_draft.md` — where ⟨N⟩ feeds the paper.
- Sibling cosmology open items: OPEN-COSMO-DM-1 (tetra-gravity), DM-2 (structure formation), DM-3 (corona, CLOSED).

## SUGGESTED SEQUENCE
Confirm E_bond (interface E_qq count) first — it sets the target kT_form. Then ν_PCD and H_form at the aggregation epoch → kT_form → ⟨N⟩. Hand ⟨N⟩ (and the natural-vs-tuned verdict) back; the DM dwarf-normalization consumption and the held panel round 2 both wait on it.
