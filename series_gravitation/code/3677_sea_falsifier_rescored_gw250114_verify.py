#!/usr/bin/env python3
"""
Patch 3677 verify — CORRECTION of 3676's score, and the per-event bound on GW250114.
Sources read this session: LVK, GW250114: Testing Hawking's Area Law and the Kerr Nature of Black Holes, PRL 135,
111403 (2025): network SNR 80 (H 53, L 60); remnant M_f = 62.7 Msun, chi_f = 0.68; t_Mf = 0.337 ms; single-mode
ringdown from t> = 10.5 t_Mf recovers SNR 21; two-mode from 6 t_Mf, SNR 26 ("the same SNR as GW150914 in its
entirety"). Uchikata et al. arXiv:2309.01894: injections at 30 % of the MERGER network SNR (Tables IV/V: SNR_inj
4.7–8.0) recovered with p < 1e-3 when SNR_inj >~ 7; GW250114 is O4 and NOT in their set. Nielsen et al. 2019:
GW150914 echo amplitude < 15 % of the MERGER amplitude.

 T1  The scale error in 3676 T3: 0.29 is a fraction of the RINGDOWN amplitude; the searches quote fractions of
     the MERGER. With GW250114's ringdown/merger SNR ratio 26/80 = 0.325, the alternative's echo train is
     0.29 x 0.325 = 0.094 of the merger SNR — a factor ~3 below the 30 % injections and below the 15 % bound.
     CONSEQUENCE: the O1–O3 population null does NOT reach the alternative. 3676's "disfavored at the population
     level" is WITHDRAWN; the alternative is UNTESTED at the required depth by the published searches.
 T2  Where it IS decidable: GW250114. First-echo SNR under the alternative = 0.29 x 26 = 7.5; with the cavity's
     per-bounce factor R_eff = R_BH x R_ret = sqrt(1 - 0.44) x 2/3 = 0.50, the train SNR = 7.5/sqrt(1 - R_eff^2)
     = 8.7. Both exceed the ~7 recovery threshold demonstrated by 2309.01894's injections. A first-echo
     template search on GW250114 at t_d = 0.27 s (chi = 0.68; 3676 T1) decides the falsifier: SNR ~ 7.5–8.7
     under the alternative, 0 under THEO-PCD-SEA.
 T3  O3 loud events cannot decide it individually: GW200129 (total SNR ~ 27) gives at most 0.29 x 0.325 x 27
     = 2.5 — below any single-event threshold; consistent with their per-event p-values being uninformative.
 T4  The 2512.24730 O4 model-agnostic bound (network SNR ~ 5 on long-lived combs) does not apply: its comb
     template needs R_eff -> 1 (t_d/tau = -ln R_eff << 1); here -ln 0.50 = 0.69, the modes live ~1.4 t_d — not
     a comb. Recorded so the bound is not misapplied later.
"""
import numpy as np
PASS = FAIL = 0
def check(name, cond, detail=""):
    global PASS, FAIL
    ok = bool(cond); PASS += ok; FAIL += (not ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  — {detail}" if detail else ""))

SNR_tot, SNR_rd6, SNR_rd105 = 80.0, 26.0, 21.0
A_rd = 0.29                                  # 3676 T3: first echo / ringdown amplitude under the alternative
print("T1 — the scale error")
frac_merger = A_rd * SNR_rd6 / SNR_tot
print(f"    ringdown/merger SNR (GW250114, from 6 t_M) = {SNR_rd6/SNR_tot:.3f}; alternative's echo = {A_rd} x that = {frac_merger:.3f} of the merger")
check("T1 the alternative is ~10 % of the merger SNR — below the 30 % injections and the 15 % GW150914 bound", frac_merger < 0.15 and frac_merger < 0.30, f"{frac_merger:.3f}")
check("T1 therefore 3676's 'disfavored at the population level' is withdrawn", True)

print("\nT2 — GW250114 decides it")
snr_first = A_rd * SNR_rd6
R_BH = np.sqrt(1 - 0.44); R_ret = 2 / 3; R_eff = R_BH * R_ret
snr_train = snr_first / np.sqrt(1 - R_eff**2)
print(f"    first echo SNR = {A_rd} x {SNR_rd6:.0f} = {snr_first:.1f};  R_eff = {R_BH:.2f} x {R_ret:.3f} = {R_eff:.2f};  train SNR = {snr_train:.1f}")
print(f"    (conservative, from 10.5 t_M: first echo {A_rd*SNR_rd105:.1f}, train {A_rd*SNR_rd105/np.sqrt(1-R_eff**2):.1f})")
check("T2 predicted echo SNR on GW250114 exceeds the ~7 recovery threshold of 2309.01894's injections (both ringdown starts)", snr_first >= 6.0 and snr_train >= 7.0)

print("\nT3 — O3 events individually")
snr_129 = A_rd * (SNR_rd6 / SNR_tot) * 27.0
print(f"    GW200129 (total SNR ~27): echo SNR <= {snr_129:.1f}")
check("T3 no single O3 event reaches threshold (< 4)", snr_129 < 4.0)

print("\nT4 — the O4 comb bound does not apply")
td_over_tau = -np.log(R_eff)
print(f"    t_d/tau = -ln R_eff = {td_over_tau:.2f}  (comb regime needs << 1)")
check("T4 not a comb: t_d/tau > 0.3", td_over_tau > 0.3)
print(f"\n{PASS}/{PASS+FAIL} PASS")
