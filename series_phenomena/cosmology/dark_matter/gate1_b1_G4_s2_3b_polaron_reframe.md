# G4 · S2-3b — self-red-team of 2321: the polaron reframe (Patch 2322, 7 July 2026)

**What this patch is:** a correction registered by the campaign against its own previous patch,
before the panel or the propagation work finds it. **Verify:** `code/2322_g4_s2_3b_subcone_kinematics.py`
(3/3). **Thresholds and the residue's identity are UNCHANGED; the frame and the protections improve.**

## The tension found in 2321

2321's two-branch Θ treatment is internally inconsistent. The quasi-static branch (Θ ~ 1) that
rescues dwarf capture also revives the steady-drag catastrophe (τ ~ 3×10⁻¹³ s), and no stationary
bath spectrum can block steady drag while passing encounters: the kinematic scales sit side by
side — ħk·v = 259 eV (steady transfer) vs ħω_enc = 45 eV (encounter, at dwarfs) — with the
encounter *lower*. A spectrum cannot be simultaneously empty at 259 eV to 24 orders and populated
at 45 eV to 10⁻⁵. **The two-branch Θ frame is RETIRED.**

## The resolution: dressed-state (polaron) structure

The rod + coat + local bath back-reaction is the **dressed ground state** of the moving rod. A
dressed eigenstate experiences no drag from the bath that dresses it — **steady subsonic motion is
protected automatically**, by eigenstate structure, not by spectral tuning. The 2321 drag
catastrophe was an artifact of treating the dressed state as scattering off its own dressing.
Halo protection is thereby **structural** (and Λ/W2 protection stands as computed at 2321).

**Encounters** are nonadiabatic overlaps of two dressed states — real emission is allowed, into
exactly two places: **(a) on-shell** quanta at ω_enc, whose wavelength is 3×10⁵–3×10⁷ fm — this
*is* the 2318 radiative channel, Adler-dead ×10¹³⁺; the circle closes with no double-counting.
**(b) the sub-cone continuum** at (k ~ 1/R_s, ω ~ ω_enc), ω/ck = 6×10⁻⁶–6×10⁻⁴ — which exists
only through the bath's nonlinear/disorder broadening: precisely the content of the founder's
D-C ruling, and precisely the residue.

## The residue, now well-posed (thresholds unchanged from 2321)

**G4 = UNRESOLVED-QUANTIFIED on S(k ~ 1/R_s, ω_enc) — the deeply sub-cone spectral weight of the
nonlinear configurational bath.** Survive/kill thresholds per anchor as tabulated at 2321
(Θ_crit = 6.3×10⁻⁶–2.6×10⁻⁵ dwarfs; 1.4–6.0×10⁻³ at 50; 0.23–0.98 at 200), now read as sub-cone
weight fractions. The consistency triple (halo/Λ/W2) is no longer a constraint the spectrum must
be tuned to satisfy — it is delivered structurally, which *widens* the physically admissible
spectra and honestly improves survival odds relative to the 2321 framing, without deciding them.
The computation that decides the gate — the sub-cone response of the PCD/ZBW configurational
dynamics — is Stage-3/DM-4 work, multi-session, and is NOT attempted by shortcut here.

## Release posture (20 July) — final form for the decision

G4 unresolved per the pre-stated rule; the open condition is one named, well-posed spectral
quantity with per-anchor thresholds, structural consistency protections, a favorable unforced
velocity shape, and a founder-ruled sink. Next work: **Grok's propagation** (branch-independent,
recommended for the following session with fresh context) → then the Stage-3 sub-cone computation.
