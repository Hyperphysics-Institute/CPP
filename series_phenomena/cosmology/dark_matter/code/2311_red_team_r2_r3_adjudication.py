"""
2311 -- Red-team adjudications, returns 2-3 (Grok, Gemini): the computable parts.

(A) GEMINI KILL-CLAIM KINEMATICS (the serious one -- adjudicated as far as
    computation reaches today; the remainder becomes a NAMED GATE):
    encounter frequency content vs the registered channel gaps. If the collision's
    characteristic energy hbar*omega ~ hbar*v/b is far below every GAPPED channel,
    those channels cannot absorb -- Gemini is RIGHT that gapped channels are
    closed. The open question (the gate) is the GAPLESS channel's coupling.
(B) GEMINI SCRATCH (formation latent heat vs N_eff): full dismissal arithmetic.
(C) GEMINI WOUND-2 (solar accumulation / helioseismology): first-order capture
    estimate to size the queued computation (NOT a verdict).
(D) Grok WOUND-1 folds into (A)'s gate (same physics, weaker form).
"""
import math
HBARC = 197.327e-15  # MeV*m
C = 3e8
CHI = ((1 + 5 ** 0.5) / 2) ** -3 / 6
MS = 7.764           # MeV, colour-channel gap
M_ROD = 25344.0      # MeV
MU = M_ROD / 2

print("=" * 78)
print(" 2311 -- adjudication computations (returns 2-3)")
print("=" * 78)
print("\n(A) SUB-GAP KINEMATICS at the capture boundary (Gemini KILL claim, part 1):")
for vkms, b_fm in ((10, 145), (50, 79), (200, 31)):
    v = vkms * 1e3
    w = v / (b_fm * 1e-15)                    # rad/s
    hw = 6.582e-22 * w                        # MeV
    Ecol = 0.5 * MU * (v / C) ** 2
    print("   v = {:>4} km/s (b_max = {:>4} fm): E_col = {:.2e} MeV; hbar*omega = {:.2e} MeV".format(
        vkms, b_fm, Ecol, hw))
print("   vs channel gaps: colour m_s = 7.76 MeV; e-channel ~ E_ee = 0.9 MeV; rod internal")
print("   modes (vibration ~0.3-5 MeV; rotation ~0.04 MeV): ALL gapped channels are")
print("   1e2-1e4 x above the encounter's frequency content -> CANNOT absorb (sub-gap).")
print("   GEMINI IS RIGHT ABOUT EVERY GAPPED CHANNEL. But the premise 'no light mediator")
print("   exists' is FALSE in the registered corpus: the |SSV| coherence mode is GAPLESS")
print("   (shell-sum, 1107-1108; load-bearing in DM-2). Whether its coupling to a moving")
print("   rod pair delivers Delta-E >= E_col per encounter is UNREGISTERED -> THE GATE.")

print("\n(B) LATENT-HEAT / N_eff (Gemini SCRATCH) -- dismissal arithmetic:")
f_bind = 17 * 1.0 / M_ROD          # ~17 bonds x O(1 MeV) per rod mass
rho_ratio = 0.8e-6 / 16e-3         # (T_matter-rad equality ~0.8 eV)/(16 keV): rho_DM/rho_rad at formation
inj = f_bind * rho_ratio
print("   binding fraction ~ {:.1e}; rho_DM/rho_rad at T=16 keV ~ {:.1e}".format(f_bind, rho_ratio))
print("   -> fractional energy injection into the bath ~ {:.1e}".format(inj))
print("   vs N_eff sensitivity ~1e-2: SEVEN+ orders below. DISMISSED. (Entropy/eta_B same order.)")

print("\n(C) SOLAR ACCUMULATION (Gemini WOUND-2) -- sizing the queued computation:")
rho_dm, v_dm = 0.4e9 * 1.602e-19 / 1e-6, 270e3   # eV->J per m^3... keep simple in GeV/cm^3 units
flux = 0.4 * 2.7e7   # GeV cm^-2 s^-1 (rho*v)
R_sun = 6.96e10
rate_mass = flux * math.pi * R_sun ** 2 / 25.3    # rods/s if ALL captured
m_rod_kg = 4.51e-26
acc = rate_mass * m_rod_kg * 4.5e9 * 3.15e7
print("   geometric-ceiling accumulation over 4.5 Gyr (ALL incident captured):")
print("   ~ {:.1e} kg = {:.1e} M_sun".format(acc, acc / 2e30))
print("   Helioseismology-class sensitivities bite around 1e-3 M_sun-scale core effects for")
print("   conductive DM; the ceiling sits ~{:.0e} of that -> the queued computation must".format((acc/2e30)/1e-3))
print("   check CONDUCTION per rod (large sigma!) not mass fraction. QUEUED, not adjudicated:")
print("   the rods' huge self-interaction thermalizes them into a tiny isothermal core;")
print("   the rod-NUCLEON transport at S_c in the solar plasma sets the conduction effect.")
print("=" * 78)
