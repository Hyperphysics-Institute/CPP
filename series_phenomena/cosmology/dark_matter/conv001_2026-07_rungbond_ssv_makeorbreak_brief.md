# CONV-001 ROUND — VERIFY THE RUNG-BOND SSV MAKE-OR-BREAK (κ_θ/E_bond) + HOSTILE PASS on the favorable verdict

**Round type:** VERIFICATION + HOSTILE PASS (adversarial invited).
Worker recommended this round before building Ω_DM on the result.
**Patches under review:** 2426 (the derivation) + 2427 (the Kapitza test of 2426's one assumption).
**No verdict moves this round.** The frontier verdict is unchanged; the founder adjudicates on your returns.

**Raw links (AI-fetchable):**
- https://raw.githubusercontent.com/Hyperphysics-Institute/CPP/main/series_phenomena/cosmology/dark_matter/code/2426_rungbond_ssv_potential.py
- https://raw.githubusercontent.com/Hyperphysics-Institute/CPP/main/series_phenomena/cosmology/dark_matter/reasoning/2426.md
- https://raw.githubusercontent.com/Hyperphysics-Institute/CPP/main/series_phenomena/cosmology/dark_matter/code/2427_kapitza_pondermotive_stiffness.py
- https://raw.githubusercontent.com/Hyperphysics-Institute/CPP/main/series_phenomena/cosmology/dark_matter/reasoning/2427.md
- https://raw.githubusercontent.com/Hyperphysics-Institute/CPP/main/series_phenomena/cosmology/dark_matter/DM-CANDIDATE-B_N8_cdm_like_registration.md
- https://raw.githubusercontent.com/Hyperphysics-Institute/CPP/main/founders_vision.md   (Part V, 28–29 Jun captures — the Cross-Rod geometry)

## The stakes, stated plainly
DM candidate (B) — N=8 closed ring, CDM-like, coring closed on every route — has ONE open falsifier (i): does
its formation deliver DD-clear (heavy) rings rather than LZ-excluded light ones? 2421–2424 reduced that to a
single strong-sector number: **κ_θ/E_bond ≥ 0.43** (κ_θ = rung-bond hinge stiffness, E_bond = well depth;
central pre-derivation estimate 0.345 = "fails ×1.25"). 2426 derives it on the founder's canonical Cross-Rod
geometry; 2427 tests the one assumption 2426 rested on. The result LEANS FAVORABLE (clears 0.43). Before Ω_DM
gets built on top, this pair needs an adversarial pass. **If the favorable verdict is wrong, now is the time.**

## What was computed (one paragraph each)
**2426 — the derivation.** On the founder's Cross-Rod (alternating-charge square: qCP core + outer eCP layer,
first-order electrostatic, |q_eCP|=|q_qCP|=1), κ_θ and E_bond are the SAME outer-eCP-layer object seen two ways
(29 Jun: E_ee governs both the bending stiffness via its lever arm AND the fragmentation threshold via the
outer-fiber strain concentration). E_bond validates: outer-eCP axial bond depth at R_perp=0.9 fm, f_ZBW=1.0 →
**494 keV vs the registered 490**. The static Madelung bend is **Earnshaw-negative** (κ_static ≈ −4.2 MeV → no
static bending minimum → the stiffness is intrinsically dynamic). The beam relation gives, in the conservative
**E_ee-outer-layer-only** regime, **κ_θ/E_bond = 2 R_perp²/d²** → crossover R_perp* = 0.53 fm; the outer eCPs
sit at R_perp ≳ 0.7 fm → ratio ∈ **[0.74, 1.51]** → CLEARS 0.43 by 1.7–3.5×. The E_qq core (α_s/α ≈ 53) only
stiffens further.
**2427 — the Kapitza test.** 2426 used the STATIC curvature-to-depth ratio |V''|/|V| = 2/d²; the real stiffness
is dynamic (ZBW ponderomotive). A first-pass Paul-trap model (U_sec ∝ |E_static|²) gave a SINKING factor g ≈ 0.1
— but was DISCARDED on finding the eCP site is **not** a static field null (|E| = 3.09 ≠ 0), so that model's
precondition fails. The tractable 1D bond average then shows: small-amplitude ZBW (a/d ≪ 1) → factor → 1 (depth
& curvature scale together, 2426's ratio survives); large-amplitude (a/d = 0.8) → factor ≈ 10 (ENHANCES the
ratio). **No tractable amplitude branch sinks κ_θ/E_bond below 0.43.**

## VERIFY (please confirm or refute, item by item)
1. **The reduction** κ_θ/E_bond = 2 R_perp²/d² — is the beam decomposition (κ_θ = Σ_fibers k_axial·y², E_bond =
   outer-fiber depth) correct, and is |k_ee|/E_ee = 1/d² the right curvature-to-depth for the screened eCP bond?
2. **E_bond validation** — 494 keV at (R=0.9, f_ZBW=1) vs registered 490 keV: independent check or circular?
3. **Earnshaw → dynamic** — is κ_static < 0 correctly read as "static-null, stiffness must be dynamic," and does
   f_ZBW genuinely cancel in the ratio (common ponderomotive prefactor to depth AND curvature)?
4. **2427's two limits** — is the 1D small-amplitude average (factor→1) a fair proxy for f_stiff = f_depth? Is the
   large-amplitude factor ≈ 10 real or a 1D artifact?

## HOSTILE PASS — the attack surfaces I most want broken
**(A) THE r-BAND TENSION (strongest surface).** κ_θ/E_bond ∈ [0.74, 1.5] means r = ℓ_p/ℓ_rung = (κ_θ/E_bond)·ε
≈ **22–45** (ε = E_bond/kT_form = 29.7) — **2–4× the registered band r ∈ [8.5, 12]**. Consequences: N_stab =
c_eff·(r/ε) ≈ **10–21** (c_eff = 14.07), so the surviving ring family drifts from **N=8 (11.26 GeV) to N ≈ 10–21
(15–30 GeV)**. Is this a *reconciliation* (the registered r-band was a pre-Cross-Rod floppy-chain underestimate;
the candidate is genuinely a heavier ring, still DD-clear/CDM-like) — or a *contradiction* that breaks the
DD-selection the whole candidate rests on (σ and mass were pinned at N=8)? If the beam derivation over-stiffens,
where exactly?
**(B) E_ee-only vs the E_qq core.** I quoted E_ee-only as conservative. But does the continuous E_qq spine
contribute to *rung-scale* bending (α_s/α≈53 → ratio ≈ 54, absurd) or only to a *global* rigidity that doesn't
enter the per-joint ℓ_p? The beam decomposition may be the wrong framework for a continuous spine.
**(C) The lever arm R_perp.** Bracketed [0.7,1.0], not relaxed. Is the equilibrium outer-eCP radius actually
≳ 0.53 fm? Relax the transverse-plane Madelung/ZBW cross-section and check.
**(D) The 3D driven Kapitza (2427 residual).** 2427's F2/F3 are a 1D axial average; the rigorous object is 3D and
driven (neighbours oscillating, site not a static null). Could the TRANSVERSE/bending mode behave oppositely to
the axial mode I averaged — i.e., could the dynamics soften the bending stiffness specifically? This is the one
route I could not close.

## Per-seat asks
- **GPT (triage/verdict-honesty):** is the favorable verdict earned, or is the r-band drift (A) a disqualifier?
  Say plainly whether 2426+2427 support "survives" or only "not-yet-falsified."
- **Grok (independent verify):** re-derive 2 R_perp²/d² from the Cross-Rod independently; check the E_bond 494 keV.
- **Copilot (referee-grade):** attack (B) — is the beam decomposition legitimate for a continuous-spine rod?
- **Gemini (breadth):** attack (D) — the 3D driven Kapitza; can the bending mode soften where the axial didn't?
- **DeepSeek:** attack (A) — the r-band reconciliation and the N=8 → N≈10–21 mass drift; is the candidate still
  the same object, and does the DD-selection survive the mass shift?
