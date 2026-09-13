# OPEN-DM-PAIRING-KINETICS-1 — the THERMAL residue computation (R-RESIDUE-THERMAL, 3519), performed — **D1 READ: on the corpus's registered inputs p = 0.016, OUTSIDE the band [0.21, 0.48] by 13×; C-5 FAILS D1 on the record as it stands.** The band is reachable only if the lone-qCP pairing rate is suppressed by ~10¹⁷–10¹⁸ below colour strength into a one-decade window (λ ≈ 10–30) — the founder's cocoon is the only named suppressor and its strength is not on file; recorded as the reopening condition, not as a live conditional.

**Patch 3520, 12 Sep 2026. DM block, from this window under PD-006.** Ruling: `founders_voice/3519_qdp_bond_breakable_ruling.md`. Verify `code/3520_thermal_freeze_computation.py` (6/6). Reasoning `reasoning/3520.md`. **No constant minted; nothing fitted; the band untouched; the pairing strength carried as one parameter and scanned across nineteen decades.**

## §1 Inputs (D-7 pass) and the model
| input | value | source | status |
|---|---|---|---|
| qDP bond E_b | E_qDP = 264 MeV (= 3 E_eDP, E_eDP = 88 MeV) | DM-1 manuscript; `fa_sea_green_charter.md` | registered; "ratio-clean, absolute scale is Project C" |
| equilibrium | pair ⇌ +q + −q, Saha: n₊n₋/n_pair = (E_b T/2π)^{3/2} e^{−E_b/T} | 3519 (partner switching, collisions, two-DP swap) | ruled; the prefactor's mass scale ~E_b is **[model]** and enters only logarithmically |
| expansion | H(T) = 1.66 √g* T²/M_Pl, g* = 10 (60 as sensitivity) | charter §6 "the MeV-epoch H", selected by the 3519 epoch | **EXTERNAL** (radiation-era form; no CPP-derived H(T) on file) |
| pairing strength | λ ≡ ⟨σv⟩ n_pair / H at kT = E_b, scanned 10⁻²–10¹⁹ | — | **not on file**; colour strength (σ ~ 1/E_b², the DM lane's own scale for qDP scattering) gives λ ~ 10¹⁹ |
| symmetry | n₊ = n₋ exactly; all q in pairs at the freeze; composition mode at fixed total (n_pair → n_pair e^δ, T and H unchanged) | neutrality grounding; 3936 | registered |

Boltzmann: dn/dt + 3Hn = −⟨σv⟩(n² − n_eq²), integrated implicitly in x = E_b/T from x = 0.3 to 400. Output: u = n_lone/n_q, p = d ln n_∞/d ln n_pair by finite difference (δ = ±0.05), and the freeze temperature T_f (where n leaves n_eq by 50%).

## §2 Results (T1–T6)
| λ | u | p | T_f |
|---|---|---|---|
| ≪ 1 (never equilibrates) | 0.04 | **≈ ½** | ~50 MeV |
| 3 | 0.061 | 0.53 | 61 |
| **10** | **0.055** | **0.37 — in band** | **65** |
| **30** | **0.036** | **0.26 — in band** | **59** |
| 10² | 0.018 | 0.18 | 48 |
| 10³ | 3.5×10⁻³ | 0.11 | 32 |
| 10⁵ | 7.5×10⁻⁵ | 0.06 | 17 |
| 10⁸ | 1.4×10⁻⁷ | 0.04 | 9.5 |
| 10¹³ | 2.8×10⁻¹² | 0.02 | 5.4 |
| **10¹⁹ (colour strength)** | **4.6×10⁻¹⁸** | **0.016** | **3.5** |

- p starts at the Saha stoichiometry ½ when nothing pairs, and falls as soon as pairing outruns expansion: the standard freeze-out result that the relic density forgets the initial density (the recombination-style x_e ∝ 1/n). The band [0.21, 0.48] is occupied for **λ ≈ 10–30 only** — one decade of nineteen (T3).
- g* 10 → 60 moves p by < 0.08 (T5): the reading is set by λ, not by the external H's details.
- Ordering check (T4): in the band the residue freezes at T_f ≈ 60 MeV, above 2543's dressing window [10.2, 17.0] MeV, as the chain needs; at colour strength it freezes at 3.5 MeV, *below* the window.
- D2 pointer (T6, not a reading): in the band u ≈ 4–5% of the qCPs are left lone, so n_B = a·R puts η_B's 10⁻⁹ almost entirely in the asymmetry fraction a; at colour strength u ~ 5×10⁻¹⁸, a residue too small to carry η_B at all.

## §3 D1 reading — taken once
**On the registered inputs — E_qDP and the colour-strength interaction the DM lane uses for qDPs — p = 0.016. That is outside [0.21, 0.48], on the p = 0 side, by a factor 13. Under charter §5 D1, C-5 fails, by name and number.**

What would reopen it, stated so it cannot be improvised later (3907): the lone-qCP pairing rate at kT ≈ 264 MeV would have to be suppressed by 10¹⁷–10¹⁸ relative to colour strength, landing in λ ≈ 10–30 — pairing only a few to a few tens of times faster than the expansion — and the freeze would then sit at ~60 MeV with ~5% of the qCPs lone. The founder's cocoon (3513: a lone charge polarises the sea around it and "does not allow itself to be bonded") is the only mechanism on file that could do this, and nothing on file gives its strength. A suppression *chosen* to land in that decade would be post-hoc; a suppression *derived* from the cocoon's polarisation (the DM lane's qstiff/contact-polarizability scoping is the nearest tool) would be a legitimate reopening. C-5 is therefore **recorded as failed on the record, with one registered reopening route**, not carried as a live conditional.

D1′ (R₊/R₋ = 1) holds in the thermal picture by the same symmetry. D3 and D4 are not reached.

## §4 What this does not touch
The MeV-epoch H is external to CPP and enters only through λ's normalisation and logarithmically through x_f; a CPP-derived H(T) would move the λ scale, not the shape. The Saha prefactor likewise. The 3512 dilution results stand as results about a superseded model. The EU-side owed items (TODO-3930-EU) are untouched.
