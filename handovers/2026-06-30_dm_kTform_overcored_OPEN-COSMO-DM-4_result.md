# HANDOVER — DM: OPEN-COSMO-DM-4 is RESOLVED-AS-RUN — the natural freeze-out OVER-CORES; N_form is not a zero-parameter prediction of kT_form
**Date:** 2026-06-30 · **Lane:** DM 18xx (cosmology / dark-matter) · **From:** Opus (substrate-cosmology lane, patch 2204) · **Consumer:** DM-1
**Answers (does NOT supersede):** `handovers/2026-06-30_cosmology_kTform_OPEN-COSMO-DM-4_patch2203.md` — the DM→substrate-cosmology ask. This returns the number and verdict.

## ⛔ CLONE GATE
```
cd ~/Documents/GitHub/CPP && git pull --rebase origin main && git log --oneline -6
```
Confirm HEAD includes **2204** (substrate-cosmology OPEN-COSMO-DM-4 execution). This is **DM 18xx lane** work now — DM consumes; do not re-run the substrate calc or edit `reasoning/2204.md` / OPEN-COSMO-DM-4 in place.

## Orientation — read this first
The kT_form calc the 2203 handover asked for is done (2204), and it does **not** give the dwarf branch a free prediction. The forward freeze-out — with the physically-correct vibrational attempt frequency (ν_vib ~ 1.5×10²² Hz, **not** the Planck tick) and standard Friedmann H(T) — self-consistently gives **kT_form ~ 1.3–5.4 MeV, E_bond/kT_form ~ 49–51, ⟨N⟩ ~ 10⁴–10⁶**: **over the dwarf target (400–1000) by ~2–3 orders → over-cored.** The 1846 "kT_form ~ E_bond/13 ~ 5 MeV" that looked encouraging was a **φ ~ 1 artifact**; the physical dilute-gas φ ~ 10⁻⁹…10⁻¹⁴ (your own 0881) moves the band-required ratio to ~34–45, which the freeze-out ~matches — hence the over-shoot. **Net for DM:** N_form is **not** a zero-parameter prediction; the dwarf normalization has **no** zero-parameter route as currently posed. The **cluster σ/m ∝ 1/v² branch is untouched and stands** (independent, parameter-free) — the candidate is not killed, only its dwarf branch loses the free prediction.

## WHAT DM SHOULD DO NOW (consumption — your lane)
1. **Do NOT plug ⟨N⟩ ~ 10⁴–10⁶ into the dwarf σ/m as a prediction** — it gives σ/m = K·N ~ 10²–10⁴ cm²/g, ~10²–10⁴× the observed few cm²/g. Report the dwarf branch as **"no zero-parameter route; over-cored under natural inputs."**
2. **Update the disposition surfaces** (`DM-1/documentation_suite/mechanism-strip-then-fuse-DM-1.md` STATUS; DM-1 §5 re-scope draft): the dwarf normalization is **not** secured; the cluster branch is the parameter-free result to lead with.
3. **Panel round 2** (still held): run it framed as **"cluster branch = prediction (Bullet-safe, σ/m ∝ 1/v²); dwarf branch = over-cored under natural formation, salvage is founder-gated."** Do not present a dwarf σ/m normalization as a win.

## THE TWO FOUNDER-GATED SALVAGE ROUTES (flag to Thomas; do not choose)
The window (⟨N⟩ ~ 700) is reachable only by one of these, both unpinned:
- **(A) DM colder than radiation by ~10²× at the QCD epoch** (an unpinned decoupling history). If the DM sector decoupled early and is ~100× colder than radiation at freeze-out, H_form is larger → smaller log → ⟨N⟩ into window. This is a real substrate-cosmology calc (the DM thermal-decoupling temperature) — but until pinned it is a **tuning**, not a prediction.
- **(B) Reframe N_form as NUCLEATION-limited, not freeze-out-limited.** At E_bond/kT ~ 50 essentially all monomers polymerize, so the equilibrium ⟨N⟩ ~ 10⁵ exceeds any plausible monomers-per-nucleus → the **true** size is set by the nucleation-site density, and **kT_form is not the controlling variable.** This means the 1846 reduction ("size ↔ kT_form") is **incomplete**; the correct pin is the nucleation density (monomers-per-nucleus), which is a **different** substrate-cosmology calc. This is the more likely-correct physics and the recommended reframing of OPEN-COSMO-DM-4.

## LANE BOUNDARY
- **Substrate-cosmology delivered (done):** ν_PCD (vibrational, correct prefactor), H_form (Friedmann), kT_form, ⟨N⟩, the φ correction, and the over-cored verdict — `reasoning/2204.md`, `scripts/2204_kTform_freezeout.py`, OPEN-COSMO-DM-4 updated. **Still owed (founder-gated):** the DM-decoupling-temperature calc (route A) and the nucleation-density calc (route B) — either could be the next substrate-cosmology patch, on Thomas's call.
- **DM consumes (this handover):** the over-cored ⟨N⟩ verdict → dwarf σ/m framing, disposition updates, panel round 2. Do not do the substrate calcs here.

## POINTERS
- `reasoning/2204.md` + `scripts/2204_kTform_freezeout.py` (the calc; run it — §1 forward freeze-out, §2 φ correction, §3 DM-colder variant).
- **OPEN-COSMO-DM-4** (`frontier_sectors/CONJ.md`) — updated: over-cored, reduction incomplete, the two salvage routes.
- Your own `code/0881_freezeout_kinetics_Ndwarf.py` — the φ ~ 10⁻⁹…10⁻¹⁴ estimate that corrects 1846's φ ~ 1.

## SUGGESTED SEQUENCE
Disposition update + dwarf-branch reframing first (fast), then panel round 2 (cluster branch leads). The two salvage routes (A DM-decoupling, B nucleation-limited N_form) are founder-gated substrate-cosmology calcs — surface both to Thomas; route B (nucleation-limited) is the recommended reframing of OPEN-COSMO-DM-4. The candidate stands on the cluster branch regardless; the dwarf branch is the piece now waiting on a founder decision.
