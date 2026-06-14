# C5 pre-registration band — EU-1 spectral index n_s as the SF-2 campaign's now-shippable backbone

**Patch:** 1208 (SF-2 external-validation campaign, 1200-block). **Cycle:** Priority-2 deliverable from the Patch 1206 cycle-close forward queue — the now-shippable backbone of the two-track plan. **Type:** pre-registration framing + quantitative survival-band memo for candidate **C5** (EU-1 primordial scalar spectral index). **Not** a verdict-moving review; **not** new physics (the prediction is already shipped as PRED-C-96). Self-contained; verification script embedded in §7.

**Location note (collision discipline):** placed lane-private in `flagship_papers/electroweak/review/` rather than in the EU-1 paper folder (`series_phenomena/cosmology/early_universe/EU-1/`). The earlier Patch-1206 forward queue suggested the EU-1 folder, but that folder is cosmology-lane territory (at risk of brushing a concurrent cosmology window); this memo is an SF-2-campaign artifact and belongs in the SF-2 lane. EU-1 is referenced by path, not edited.

---

## Verdict

**C5 is shippable NOW as the SF-2 campaign's pre-registration backbone — and it is sharper than the Patch-1204 reviewers credited.** EU-1 claims the pivot e-fold count **N_∗ ≈ 57 is *derived* from the CP-count, not assumed from the standard inflationary range** — so the CPP prediction is a *point*, n_s = 0.9649, not a band over N_∗ ∈ [50, 60]. The reviewers (who treated N_∗ ≈ 55–60 as a free range) under-rated this. The catch is unchanged: n_s = 0.9649 is a **postdiction** against Planck, so its pre-registration value lives entirely in (a) the Simons Observatory / CMB-S4 *tightening* and (b) the companion **running α_s ≈ −0.0006**, which Planck constrains only weakly. Recommendation: pre-register the **joint (n_s-tightening, α_s) pair** against the survival band in §5, anchored to the existing PRED-C-96 timestamp.

---

## 1. The CPP prediction (sharp, already shipped)

EU-1 (`series_phenomena/cosmology/early_universe/EU-1/EU-1_primordial_spectral_index.tex`; PRED-C-96 + PRED-O-34; shipped 6 June 2026, Session 155):

$$\boxed{\,n_s = 1 - \frac{2}{N_*} = 1 - \frac{2}{57} = 0.964912\,}\qquad \alpha_s \equiv \frac{dn_s}{d\ln k} = -\frac{2}{N_*^2} = -0.000616.$$

The load-bearing sharpness claim: EU-1 derives the e-fold count itself, $N_* = \tfrac{1}{3}\ln(N_{\rm CP}/N_{\rm GP}) \approx 57$ at the pivot (≈60.5 total e-folds; pivot exits a few e-folds before the end), labelling it "*derived*, not assumed." If that derivation holds, n_s is a **point prediction**, not the [0.960, 0.967] band a free N_∗ ∈ [50, 60] would give. EU-1's own internal theory band is **Δn_s ≈ 5×10⁻⁴ ≈ 0.12 σ_Planck** (leading corrections), so the CPP prediction is effectively **n_s = 0.9649 ± 0.0005 (theory)**.

## 2. Current status: postdiction on n_s, open on the running

- **n_s:** Planck 2018 measures n_s = 0.9649 ± 0.0042, excluding scale-invariance (n_s = 1) at ~8σ. CPP matches the Planck **central value exactly** with zero free parameters → **postdiction**. No pre-registration credit from the match itself; the credit is in the *tightening* test (§5).
- **α_s:** Planck constrains the running only weakly — dn_s/dln k = 0.0011 ± 0.0099 (consistent with zero). CPP's α_s = −0.00062 is **not yet distinguished from zero**, i.e. genuinely **not-yet-precisely-measured**. This is the cleaner pre-registration handle: SO/CMB-S4 will tighten σ(α_s) by roughly an order of magnitude, and the CPP value sits inside the −10⁻³ to −10⁻⁴ target band those forecasts foreground.

## 3. The pre-registration mechanic (what makes this a pre-registration at all)

The pre-registration is not a new artifact to create — it already exists: **PRED-C-96 / PRED-O-34 were registered 6 June 2026 (git-history- and OSF-anchored), before the Simons Observatory n_s/α_s data window (SAT array doubled by 2027; LAT n_s/α_s constraints accumulating 2027→2035).** The timestamped, hash-anchored prediction predating the measurement *is* the pre-registration. This memo's job is to fix the **acceptance/falsification band** now, so the test is adjudicated against criteria set before the data — not after.

## 4. Experimental window (verified forecasts)

- **Simons Observatory + Planck → σ(n_s) ≈ 2×10⁻³** (≈2× tighter than Planck's 0.0042). Source: arXiv:2512.10613 ("Inflation at the End of 2025"); SO Collaboration forecasts.
- **SO/CMB-S4 running:** SO's and CMB-S4's large-aperture telescopes give the long lever arm for α_s; SO is forecast to deliver *tighter* n_s and α_s than CMB-S4 at large scales (arXiv:2212.04115, "Constraining Cosmic Inflation: Prospects for 2030"). Target α_s sensitivity reaches the −10⁻³ to −10⁻⁴ band — straddling the CPP value −6.2×10⁻⁴.
- **Timeline:** SO data 2027→; this sits inside the campaign's 2026–2028 window for first constraints, with full tightening by ~2030.

## 5. Pre-registered acceptance / survival band

Combining EU-1's theory band with the Grok∧Copilot-converged Patch-1204 criteria (independently identical: central within ≈0.5σ_meas of 0.9649 **and** σ_meas ≥ 2× tighter than Planck; ≳3σ tension falsifies):

**CPP prediction of record:** n_s = 0.9649 (theory band ±0.0005); α_s = −0.00062.

**Confirmed-beyond-postdiction** (n_s leg) iff a CMB experiment reports n_s with:
1. **σ_meas ≲ 0.0020** (≥2× tighter than Planck — met by SO+Planck), AND
2. **|n_s^meas − 0.9649| ≤ 0.5 σ_meas** (central stays consistent; at σ_meas = 0.002 this is a ±0.0010 window; at σ_meas = 0.0015, ±0.00075).

**Tension / falsification** (n_s leg): |n_s^meas − 0.9649| / σ_meas ≳ 3 (at σ_meas = 0.002, any central outside 0.9649 ± 0.0060).

**Running leg (the genuine novelty):** α_s = −0.00062 is *pre-registered* now. SO/CMB-S4 consistency with a small negative running near −6×10⁻⁴ **strengthens**; a measured |α_s| ≳ 0.01 (an order of magnitude larger, either sign) **falsifies** the EU-1 mechanism. Because the predicted running is so close to zero, the running's discriminating power is asymmetric — strong as a *falsifier of large running*, weak as a *positive confirmation* — so it is framed as a joint constraint with n_s, not a standalone primary.

**Joint pre-registration statement (recommended campaign wording):** *CPP/EU-1 predicts the pair (n_s, α_s) = (0.9649 ± 0.0005, −0.00062), registered 6 June 2026 prior to Simons Observatory data. Confirmation: SO/CMB-S4 measures n_s within 0.9649 ± 0.5σ_meas at σ_meas ≲ 0.002 while α_s remains consistent with a small negative running. Falsification: n_s central shifts ≳3σ from 0.9649, or |α_s| is measured ≳10⁻².*

## 6. Honest scope — what a hostile reviewer probes first

1. **The N_∗ derivation is the single load-bearing assumption.** The entire sharpness claim (point vs band) rests on N_∗ = (1/3)ln(N_CP/N_GP) ≈ 57 being genuinely derived rather than back-solved to hit 0.9649. A reviewer will ask: how sensitive is the ≈57 to the input counts N_CP, N_GP, and to the pivot-vs-total choice (57 at pivot vs 60.5 total — "a few e-folds before the end")? This is tracked as **OPEN-EU-1**; if C5 is elevated past backbone status, hardening this derivation is the prerequisite. Until then the honest claim is "n_s = 0.9649 *given* the EU-1 N_∗ derivation," not "n_s = 0.9649 unconditionally."
2. **n_s is a postdiction — say so plainly.** The match to Planck carries zero pre-registration credit; over-claiming it invites the exact PSQ5 objection the reviewers already raised. The campaign value is in tightening + running, and the framing must lead with that.
3. **Framework-conditional, NO-THEO.** PRED-C-96 ships at sketch-Layer-3, framework-conditional, with no registered theorem (per the EU-1 catalog entry). The pre-registration is of a *framework-conditional* prediction; that conditionality belongs in the registered statement.

## 7. Verification

```python
# C5 pre-registration band — numerical checks (Patch 1208)
Ns = 57
ns = 1 - 2/Ns                  # 0.964912
alpha = -2/Ns**2               # -0.000616
planck_sigma = 0.0042          # Planck 2018 sigma(n_s)
theory_band = 5e-4             # EU-1 leading-correction band

assert abs(ns - 0.9649) < 1e-3
assert abs(alpha + 0.00062) < 1e-4
assert abs(theory_band/planck_sigma - 0.12) < 0.02   # theory band ~0.12 sigma_Planck

# n_s across N* range (point vs band): derived N*=57 => point; free [55,60] => band
for N in (55, 57, 60, 60.5):
    print(f"N*={N:>5}: n_s={1-2/N:.6f}")
# 55->0.963636, 57->0.964912, 60->0.966667, 60.5->0.966942  (band width ~0.003 if N* free)

# survival band vs measured sigma
def legs(sigma_meas):
    return dict(two_x_tighter = sigma_meas <= planck_sigma/2,   # >=2x tighter?
                consistency_halfwindow = 0.5*sigma_meas,         # |dev| must be <= this
                falsify_if_dev_gt = 3*sigma_meas)
for sm in (0.0030, 0.0026, 0.0020, 0.0015):                      # SO+Planck ~0.0020
    print(sm, legs(sm))
# sigma_meas=0.0020 (SO+Planck): two_x_tighter=True, consistency +/-0.0010, falsify if |dev|>0.0060
```
Run: `python3 C5_ns_pre-registration_band_verify.py` (or paste the block). All asserts pass; n_s=0.964912, α_s=−0.000616, theory band = 0.119 σ_Planck; SO+Planck σ≈0.0020 satisfies the 2×-tighter leg.

## 8. Recommendation

1. **Adopt C5 as the campaign's pre-registration backbone now.** It is the lowest-risk leg of the Patch-1206 two-track plan: the physics is shipped, only the framing was missing, and this memo supplies it.
2. **Pre-register the joint (n_s, α_s) pair** per §5, leading with the *tightening + running* value, not the (postdiction) central match.
3. **Do not over-claim sharpness without hardening OPEN-EU-1.** The point-prediction status depends on the N_∗ derivation; flag it as framework-conditional until hardened.
4. **Interaction with C7 (the other track):** C5 stands as the safe backbone regardless of whether the Patch-1209 C7 normalization-closure attempt succeeds. If C7 closes → portfolio upgrades to READY with C7 primary / C5 backbone backup. If C7 stalls → C5 is the pre-registration the campaign ships.

## Registry-touch ledger

| Recommended edit | Target | At-risk? | Status |
|------------------|--------|----------|--------|
| (none required to pre-register) — PRED-C-96/PRED-O-34 already anchor the timestamp | — | — | no edit |
| Optional: annotate PRED-C-96 status with the SO survival band + "pre-registered for SF-2 campaign" | `predictions.md` | **YES (shared registry)** | **NOT made; warn-and-resync if desired** |
| Optional: harden N_∗ derivation (OPEN-EU-1) before elevating C5 past backbone | EU-1 paper / `problem_histories/PH-OPEN-EU-1.md` | cosmology-lane | deferred; only if C5 elevated |

No at-risk shared file is touched in this patch. No verdict moves; no theorem/prediction registrations; header/theorem count UNCHANGED. All chirality-arc verdicts (V3/W3; W3→W1 candidate conditional on Mechanism A; CAPACITY-1 reserved) stand unchanged.

---

*Memo produced Patch 1208 (Session 159, 13 June 2026) on Thomas's authorization, as Priority-2 of the Patch 1206 forward queue. Finding: C5 is the now-shippable pre-registration backbone and is sharper than the Patch-1204 reviewers credited (N_∗ ≈ 57 derived → point prediction, not band), but its pre-registration value lives in the SO/CMB-S4 tightening + the running α_s = −0.00062, since n_s = 0.9649 alone is a Planck postdiction. SO+Planck reaches σ(n_s) ≈ 0.0020 (2× tighter than Planck — survival-band leg satisfiable). Recommend pre-registering the joint (n_s, α_s) pair anchored to the existing PRED-C-96 timestamp; harden OPEN-EU-1 N_∗ derivation before elevating past backbone. Band-discipline: 1200-block SF-2 portfolio lane; lane-private file, no at-risk shared file touched; 09xx H1 sprint continues in its own lane.*
