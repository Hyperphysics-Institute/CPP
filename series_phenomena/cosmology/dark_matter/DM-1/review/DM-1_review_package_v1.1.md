# DM-1 Review Package v1.1 — Mechanism Correction: Fragmentation → Capture (re-ratification request)

**Artifact:** DM-1 v1.1 — mechanism correction to the panel-ratified v1.0 (4/4 CONFIRM, 28 June 2026).
**Patches:** 1859 (collision-energy reconciliation, the deciding audit) + 1860 (the §5/§Falsifiability rewrite, convention decision, registry sync). Cycle-opening: 1861.
**What changed and why you are being re-consulted:** the v1.0 you ratified carried a velocity-dependence mechanism — *the Cross-Rod fragments at cluster velocities* — whose supporting figures (~1.95 MeV cluster / ~0.78 keV dwarf collision energies) have been **proven to be unrescaled imports from a retired morphology's ledger**. At the Cross-Rod's own parameters, typical clusters do **not** fragment it. The velocity-dependent, cluster/Bullet-safe headline **stands**, on a corrected mechanism: **capture** (screened unipolar E_qq residual). Dwarf cores are **demoted from resolved to conditional**. We are asking you to ratify the correction, not to re-review the whole paper.
**Grade claimed (v1.1):** robust/parameter-free = velocity-dependent, cluster- and Bullet-safe self-interaction. Conditional = dwarf-core magnitude (gated on OPEN-SS-43, a de-novo screening-length derivation that has never been performed). Layer-C consistency, unchanged. No THEO registered.

**Full sources (inline content below is authoritative; links are provenance only):**
- Paper: https://github.com/Hyperphysics-Institute/CPP/blob/main/series_phenomena/cosmology/dark_matter/DM-1/DM-1_substrate_dark_matter_candidate.tex
- Audit: https://github.com/Hyperphysics-Institute/CPP/blob/main/series_phenomena/cosmology/dark_matter/reasoning/1859.md
- Registry: https://github.com/Hyperphysics-Institute/CPP/blob/main/frontier_sectors/SS.md (OPEN-SS-43)

**Responses aggregate in:** `series_phenomena/cosmology/dark_matter/DM-1/review/reviews-DM-1.md`.

---

## §1. Context (cold-start; skip if you reviewed v1.0)

DM-1 identifies dark matter with a charge-neutral substrate aggregate: the **Cross-Rod**, a rod of N cube elements (each 8 qCP color-balanced core + 8 eCP shell, m_el = 1408 MeV), selected by the 0865–0878 morphology arc you ratified. v1.0's headline was a velocity-dependent self-interaction: σ/m in the dwarf-core band at N ≈ 5–60, falling to collisionless at clusters *because cluster collisions fragment the rod*. The paper shipped v1.0 on your 4/4.

## §2. The correction chain (this is what to review)

1. **Provenance (proven, not argued).** §5's figures "cluster collisions (~1.95 MeV) … dwarf collisions (~0.78 keV)" reproduce **to three digits** from ½μv², μ = N·m/2, at the **0860 hoop ledger's parameters**: N = 1183, m_rung = 264 MeV — a **312 GeV** rod. The v1.0 Cross-Rod paragraph quotes those figures in the same sentence that sets N ≈ 5–60 at m_el = 1408 MeV — a **7–85 GeV** rod. Same formula, same velocities, stale (N, m). The embedded code (§7) reproduces both numbers; run it.

2. **The honest energies.** At the Cross-Rod's own pins, typical-cluster collisions (1500 km/s) deposit **0.044–0.53 MeV across the entire N = 5–60 band** — below the weakest bond, E_ee = 0.9 MeV (the side/coat bond; the axial end-bond is deeper, E_qq-class, which only strengthens the verdict). Threshold velocities: 6780 / 3915 / 1957 km/s at N = 5 / 15 / 60 (∝ 1/√N).

3. **The tail.** In a rich cluster (σ_1D = 1000 km/s, Maxwellian v_rel), the per-encounter fraction exceeding threshold is ~0% (N=5), ~5% (N=15), ~28% (N=30), ~59% (N=60). Fragmentation is partial, N-dependent, and confined to the long end — not the clean above-window switch v1.0 described.

4. **The criterion ladder (all rungs same direction).** The total-COM-KE-vs-one-bond criterion above is already **generous**: an inelastic merger thermalizes ½μv² over ~2N bonds, so breaking one bond needs energy comfortably *above* E_ee. The per-contact criterion (μ = m_el/2) gives 8.8 keV at 1500 km/s — nothing astrophysical fragments anything. And if rod-cutting must break the axial E_qq-class end-bond rather than E_ee, fragmentation is excluded outright.

5. **Verdict.** Fragmentation **fails as the cluster-safety mechanism**; it survives only as a population-shaping assist pruning N ≳ 40.

6. **The corrected mechanism: capture.** σ/m(v) = σ_floor (elastic rod-bounce, v-independent) + capture term (v-dependent, smooth — the earlier threshold/v_thr framing and its "threshold, not power law" signature are retired). Capture force = the **screened unipolar E_qq residual**: E_qq is attract-only, so the qCP core cannot dipole-cancel its field the way the bipolar eCP coat does; a net ~1/r² residual escapes, DP-Sea-screened (SSV-summation-to-zero, the confinement mechanism) at finite length R_s. Steep Rutherford-like falloff ⇒ **cluster σ/m ~ 0.003, Bullet ~ 0.001 — safe for ANY R_s** (this is the robust, parameter-free part). Dwarf σ/m ~ 1–2 requires (E_c ~ 0.3 MeV, R_s ~ 15–30 fm) — **conditional**: R_s(N) has **never been derived** (OPEN-SS-43); R_s ~ 1 fm (pion-like) demotes the candidate to weak-SIDM.

7. **Convention decision (the 0.11·N vs N^0.7 residual, now closed).** Observable = momentum-transfer (transport) cross-section: σ_T/m = ε·0.11·N, ε ≈ 0.30 flat (1856 MC, sphere-validated 1.03; rod–rod scaling ~N^0.7). Bare 0.11·N = perpendicular-limit upper bound only. Under capture this convention sets only the high-v **floor**, not the dwarf magnitude — the right place for its residual normalization uncertainty to live.

8. **Consequence for N.** Cluster/Bullet floor bound (σ_floor ≲ 0.6–0.7) ⇒ **N ≲ 18–21** (transport; ≲ 5–6 on the bare-geometric upper bound). The v1.0 "band at N ≈ 5–60" is superseded on both counts: band-reaching is no longer the elastic channel's job, and the upper half of the old range is excluded from the cluster side. Short N is now *required* by the floor and independently favored by formation kinetics (1855–1856; N = 500 retired) and tail pruning (item 3).

9. **Falsifiers (restated, live).** (a) σ/m falls with v via a **smooth turnover** — flat/rising data kills it; (b) dwarf cores are a **computable conditional**: the de-novo R_s(N) must land ~15–30 fm, else weak-SIDM fallback — a pre-registered in-framework falsifier that survives either way on cluster safety; (c) **N-ceiling**: formation kinetics producing N ~ hundreds violates the cluster floor directly.

## §3. What v1.1 does NOT claim (deflation guardrails — confirm these are held)

- It does **not** claim dwarf cores are predicted. The magnitude has migrated across three mechanisms (flat point-scattering → fragmentation trend → capture residual) while cluster safety survived all three; the paper states this asymmetry plainly and labels the dwarf magnitude **reverse-engineered until R_s(N) is derived**.
- It does **not** silently rewrite the ratified v1.0: all superseded text is retained as record under layered, dated revision notices (house convention).
- It does **not** claim the E_bond/kT_form ~ 24–41 over-determination's "fragmentation window" cross-check still holds; that referent is gone under capture and the re-anchoring is **registered as open** (reasoning 1860), not patched over.
- It does **not** touch the corona retirement (Layer B, your 4/4) or CONJ-COSMO-1's NOT-confirmed status.

## §4. Open marks carried

- **OPEN-SS-43 (the make-or-break):** derive R_s(N) — DP-Sea penetration depth of a dense N-element qCP core. Target ~15–30 fm. Genuinely new Strong-Sector physics; corpus has never touched it.
- Absolute floor normalization (r fm-scale, per-element mass) unpinned; ε and scaling robust, exact cm²/g not.
- Genesis-paragraph window cross-check re-anchoring (above).

## §5. Triage order (verdict-flipping items first)

1. **Run §7 and check item 1.** If 1.955 MeV / 0.782 keV do NOT reproduce from (N=1183, m=264), the provenance claim fails and the whole correction is suspect. If they do, the v1.0 mechanism sentence rested on the wrong object's numbers — settle this before anything else.
2. **The criterion ladder (item 4).** Is total-COM-KE-vs-one-bond really the generous end? If you can articulate a physical channel that concentrates substantially MORE than ½μv² into a single bond at these velocities, the fragmentation verdict weakens — say so.
3. **Capture sufficiency (item 6).** Does the screened-residual falloff really deliver cluster ~0.003 / Bullet ~0.001 for any R_s? Check the scaling logic, not just the quoted numbers.
4. **The convention decision (item 7)** — is transport-σ_T the right observable, and is demoting 0.11·N to an upper bound honest?
5. **Grading honesty (§3)** — is "conditional/reverse-engineered" the right label for the dwarf magnitude, and is v1.1 (not v2.0, not a retraction to v0.x) the right version semantics for a mechanism correction under a standing headline?

## §6. Reviewer-specific steer

- **ChatGPT (triage-pressure / verdict-honesty):** §5 items 1 and 5. Was the panel's v1.0 4/4 given on a load-bearing number that a reviewer could have caught? What process flag should this raise?
- **Grok (independent verification):** §5 items 1–3. Reproduce the numbers independently; stress the Maxwell-tail computation and the per-contact bound.
- **Copilot (referee-grade / framework):** §5 items 3–5. Does the σ(v) = floor + capture decomposition hold together as presented, and are the falsifiers well-posed?

## §7. Embedded verification code (Python stdlib only; run → report SCRIPT-EXECUTED)

```python
# DM-1 v1.1 correction verification (stdlib only). Reproduces: (A) provenance of the
# v1.0 figures, (B) honest Cross-Rod collision energies + thresholds, (C) Maxwell tail,
# (D) per-contact bound, (E) floor N-ceilings. Run: python3 thisfile.py
from math import erf, sqrt, pi, exp
C = 299792.458
ke  = lambda N, m, v: 0.5*(0.5*N*m)*(v/C)**2                    # MeV
vth = lambda N, m, E: C*sqrt(2*E/(0.5*N*m))                     # km/s
def tail(v, s1d):                                                # P(v_rel > v), Maxwellian
    a = sqrt(2)*s1d; x = v/a
    return 1 - (erf(x/sqrt(2)) - sqrt(2/pi)*x*exp(-x*x/2))
print("(A) provenance: hoop (N=1183, m=264):",
      f"cluster {ke(1183,264,1500):.3f} MeV (paper '~1.95'),",
      f"dwarf {ke(1183,264,30)*1e3:.3f} keV (paper '~0.78')")
print("(B) Cross-Rod (m=1408, E_ee=0.9 MeV):")
for N in (5, 15, 30, 60):
    print(f"    N={N:>2}: KE@1500={ke(N,1408,1500):.3f} MeV,",
          f"v_thr={vth(N,1408,0.9):.0f} km/s,",
          f"(C) tail@sig1000={tail(vth(N,1408,0.9),1000)*100:.1f}%")
print(f"(D) per-contact: KE@1500={ke(1,1408,1500)*1e3:.1f} keV;",
      f"v for E_ee={vth(1,1408,0.9):.0f} km/s (~0.05c)")
print("(E) floor ceilings (sigma<=0.6/0.7): bare",
      f"N<={0.6/0.11:.1f}/{0.7/0.11:.1f}; transport(eps=0.30)",
      f"N<={0.6/0.033:.1f}/{0.7/0.033:.1f}")
```

Expected: (A) 1.955 MeV / 0.782 keV exactly; (B) 0.044–0.53 MeV, all < 0.9; thresholds 6779→1957 km/s; (C) ~0/5/28/59%; (D) 8.8 keV, ~15,160 km/s; (E) 5.5/6.4 and 18.2/21.2.

## §8. Response format (please follow)

For each of §5's five triage items: **CONFIRM / RESTATE / REFUTE** + one-paragraph reasoning. Then an overall verdict: **RATIFY v1.1 / RATIFY WITH CHANGES (list) / REJECT (grounds)**. Report SCRIPT-EXECUTED with the §7 output, or state why not run. Flag anything the correction should have surfaced and did not.
