# HANDOVER — Geometry lane: the DM dwarf-branch make-or-break is ΔG*_nuc, the Cross-Rod ribbon→cross nucleation barrier (target ~6.5 kT_form)
**Date:** 2026-06-30 · **Lane:** formation-geometry (SF-2/SF-5-adjacent assembly) · **From:** Opus (substrate-cosmology lane, patches 2204–2207) · **Consumers:** geometry lane (derive ΔG*_nuc) + DM-1 (consume the verdict)
**Completes the cosmology side of:** OPEN-COSMO-DM-4 (route B, `frontier_sectors/CONJ.md`).

## ⛔ CLONE GATE
```
cd ~/Documents/GitHub/CPP && git pull --rebase origin main && git log --oneline -8
```
Confirm HEAD includes **2207** (route-B ε_nuc execution) on top of the DM **1847/1848** + DM **2206 handover**. Grep before reserving a successor ID.

## Orientation — read this first
The founder chose route B (1848: reframe the dwarf make-or-break onto the seed fraction ε_nuc, N_form ~ 1/ε_nuc, target ε_nuc ~ 10⁻³). Substrate-cosmology executed it (2207) and reached a clean stopping point: **ε_nuc = exp(−ΔG*_nuc/kT_form).** In the nucleation-and-growth competition the collision prefactors (n_mono, σ, v — the whole epoch/abundance dependence) **cancel** between the nucleation and accretion channels, so ε_nuc is set by the Cross-Rod nucleation **barrier**, not the aggregation epoch. That means:
- **ε_nuc ~ 10⁻³ ⇔ ΔG*_nuc ~ 6.0–6.9 kT_form** — a *modest* barrier, the generic scale of a specific-geometry nucleus.
- **The pin is ΔG*_nuc, a geometry/energetics quantity — substrate-cosmology cannot go further alone.** The epoch dropped out; the last number is the barrier.
- **Route B is genuinely the better gradient than A** (~4× looser pinning — exponent ΔG*/kT ~ 6.6 vs A's E/2kT ~ 25 — *and* a natural few-kT scale where A's T_DM/T_rad ~ 10⁻² has none). But note the honest correction to 1848: N_form = exp(ΔG*/kT) is *exponential* in the barrier (linear in ε_nuc, but ε_nuc is exp(−ΔG*/kT)), so it is not tuning-free — it is *less* tuned than A, and lands naturally *iff* ΔG*_nuc ~ 6 kT.

## THE ASK (geometry lane) — the successor make-or-break
**Derive ΔG*_nuc, the Cross-Rod nucleation barrier: the free-energy cost to form the smallest stable relic-forming seed along the ribbon→cross pathway, relative to free monomers, at the formation epoch.** The three formation tracks and the ribbon intermediate are mapped (1842: four-hTetra-direct / ribbon+2hTetra / ribbon+two eCP-qCP chains; amorphous polymerization ruled out ⇒ Cross-Rod is the sole relic). ΔG*_nuc is the barrier along the *selective* branch that discriminates ordered Cross-Rod seeds from amorphous product — it is E_qq/E_ee bond-energetics + assembly entropy, the same SF-2/SF-5 edge-bond kit.
- **Target / win:** ΔG*_nuc ~ 6.0–6.9 kT_form ⇒ ε_nuc ~ 10⁻³ ⇒ N_form ~ 400–1000 ⇒ the dwarf normalization is a (non-tuned) prediction.
- **Kill:** ΔG*_nuc ≲ 4 kT (ε_nuc ≳ 10⁻² ⇒ N_form ≲ 100, under-cored) or ΔG*_nuc ≳ 9 kT (ε_nuc ≲ 10⁻⁴ ⇒ N_form ≳ 10⁴, over-cored) — misses by orders; dwarf branch dies (cluster branch still stands).
- **Tolerance:** ~14% pinning of ΔG*_nuc/kT holds N in-band (verify 2207 §3) — modest, but it must be *computed*, not assumed.

## LANE BOUNDARY
- **Substrate-cosmology delivered (2204–2207, done):** the over-cored equilibrium bound (2204); the nucleation reframe kinetics (2206); **ε_nuc = exp(−ΔG*_nuc/kT), the epoch-cancellation, the ε_nuc↔ΔG* map, the corrected sensitivity comparison** (2207). OPEN-COSMO-DM-4 is **cosmology-complete**; do not reopen kT_form or ε_nuc's cosmology side.
- **Geometry owes:** ΔG*_nuc from the ribbon→cross seed energetics (this ask). SF-2/SF-5-adjacent, not cosmology.
- **DM consumes:** once ΔG*_nuc lands, ε_nuc = exp(−ΔG*_nuc/kT) → N_form = 1/ε_nuc → dwarf σ/m = K·N_form·ε_bounce → the σ/m(v) curve. Until then, dwarf branch = "reframed onto ΔG*_nuc, non-tuned prediction pending the barrier"; **panel round 2** leads with the cluster branch (parameter-free) and reports the dwarf branch as pending-ΔG*_nuc.

## POINTERS
- `reasoning/2207.md` + `scripts/2207_eps_nuc_from_nucleation_growth.py` (ε_nuc = exp(−ΔG*/kT), the cancellation, the sensitivity table). `reasoning/1848.md` (the founder choice + the sensitivity argument this corrects). `reasoning/1842.md` (the ribbon→cross tracks ΔG*_nuc lives on).
- **OPEN-COSMO-DM-4** (`frontier_sectors/CONJ.md`) — route-B executed, pin relocated to ΔG*_nuc.

## SUGGESTED SEQUENCE
Register a successor open item for **ΔG*_nuc** (the Cross-Rod nucleation barrier) under a fresh grep — it is the dwarf-branch make-or-break and it is geometry/energetics, so it likely belongs in the SS/SF sector, not COSMO. Derive ΔG*_nuc from the ribbon→cross seed (bond energetics + assembly entropy) and hand N_form back to DM. Founder-gated: whether to open it now and where. The candidate stands on the cluster branch meanwhile; only the dwarf branch waits on this one number.
