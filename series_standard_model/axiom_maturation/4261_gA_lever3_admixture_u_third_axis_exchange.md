# g_A Residual, Lever 3: No Source for an Excitation; the Search Found an Omitted Axis and a Pauli Term

**Patch:** 4261. **Lane:** EW → strong (TODO-4234-DELTA). **Session:** 239.
**Verify:** `series_standard_model/code/4261_gA_lever3_admixture_and_the_u_third_axis.py`.

## 1. Searched first (D-1, D-3, D-10)

No mechanism is on file that would put a breath mode above its ground state. I searched `founders_vision.md` and
`founders_voice/` for Sea agitation, zero point and excitation. I then ran an unscoped search of the whole tree,
including `Development/` and `archive/`, for excited breath or excited modes, quark zero-point motion, and thermal
quark motion. The one related hit is the heavy-quark thermal DP-cloud mass picture
(`series_standard_model/development-transcripts/development_p3_koide_spectral.md`, Session I). It concerns c, b and
t masses, and it records that the light quarks remain non-perturbative, so it is not a source of breath excitation.
The other hits are the dodecahedral excited modes of EW-1 and SF-2, which belong to a different object. 4243 route (C), a classical breath
at the ZBW period, was rejected because its amplitude exceeds the frame. The founder's strong-sector story
(`founders_voice/phenomenon_su3_colour_and_quark_switching.md`) says the hops are *"real as structure but silent as
activity"* in a stable baryon. That makes a structural admixture possible, but not a thermal one.

Reading the u's state closely while doing this turned up two things 4244 did not include.

**(B) The u has no localisation along its third axis.** Under the founder's rule (4244) the u breathes radially and
along its u–d edge, and not toward the other u. 4244's u therefore carries zero momentum along the in-plane axis
normal to its u–d edge. Zero momentum spread means the u is spread out without limit along that axis. 4243 checked
⟨r²⟩ = r_ZBW² with zero *position* spread along the same axis. Both cannot hold. The u sits on its vertex
(founders_voice/4242), so it is held along that axis at some width w and must carry momentum ħ/2w there.

**(C) The two u's breaths antisymmetrise.** Colour is which vertex the quark sits on (founder's story). The colour
state is antisymmetric (SS-1c), and 4240 has the u's spin–flavour state symmetric. So the two u's vertex-attached
breath states enter as a Slater determinant. When the two breaths overlap, the exchange term suppresses low
momentum. This is Pauli exclusion acting on the breath, and it follows from premises already on file. It is not a
new assumption. u–d exchange also changes which seat carries the frame's distortion, so it is not included here.

## 2. Rows verbatim (D-11)

```
(A) excited-mode admixture: every mode's momentum scaled by f (4244 REL modes)
  f = 1 (4244)                                   R_u=0.8502 R_d=0.8163  g_A=1.4057 (+10.2%)  mu_p=2.772 ( -0.8%)  mu_n=-1.829 ( -4.4%)
  f = 1.492 (closes g_A; n ~ 0.61 quanta/mode)   R_u=0.7739 R_d=0.7308  g_A=1.2754 ( +0.0%)  mu_p=2.655 ( -4.9%)  mu_n=-1.746 ( -8.7%)
  -> at m_q = m_p/3 the tie costs mu_p; keeping mu_p needs m_q = 297.4 MeV (4243 (T): 296.7)

(B) the u localised on its vertex along its third axis, width w; (C) plus u-u exchange (colour = vertex)
  w = infinite (4244's u, Gaussian shapes)       R_u=0.8491 R_d=0.8163  g_A=1.4043 (+10.1%)  mu_p=2.770 ( -0.8%)  mu_n=-1.828 ( -4.4%)
  (B) w = 1.262 fm                               R_u=0.8393 R_d=0.8163  g_A=1.3911 ( +9.1%)  mu_p=2.757 ( -1.3%)  mu_n=-1.825 ( -4.6%)
  (C) w = 1.262 fm, overlap s = 0.652            R_u=0.8223 R_d=0.8163  g_A=1.3685 ( +7.3%)  mu_p=2.734 ( -2.1%)  mu_n=-1.820 ( -4.9%)
  (B) w = 0.631 fm                               R_u=0.8168 R_d=0.8163  g_A=1.3612 ( +6.7%)  mu_p=2.727 ( -2.4%)  mu_n=-1.818 ( -5.0%)
  (C) w = 0.631 fm, overlap s = 0.671            R_u=0.7982 R_d=0.8163  g_A=1.3364 ( +4.8%)  mu_p=2.702 ( -3.2%)  mu_n=-1.812 ( -5.3%)
  (B) w = 0.446 fm = r_ZBW/sqrt2, the breath's own width R_u=0.7953 R_d=0.8163  g_A=1.3324 ( +4.5%)  mu_p=2.698 ( -3.4%)  mu_n=-1.811 ( -5.4%)
  (C) w = 0.446 fm, overlap s = 0.611            R_u=0.7770 R_d=0.8163  g_A=1.3081 ( +2.6%)  mu_p=2.674 ( -4.3%)  mu_n=-1.804 ( -5.7%)
  (B) w = 0.315 fm                               R_u=0.7650 R_d=0.8163  g_A=1.2920 ( +1.3%)  mu_p=2.658 ( -4.8%)  mu_n=-1.800 ( -5.9%)
  (C) w = 0.315 fm, overlap s = 0.523            R_u=0.7475 R_d=0.8163  g_A=1.2688 ( -0.5%)  mu_p=2.635 ( -5.7%)  mu_n=-1.795 ( -6.2%)

-> (A): closing by excitation needs f above; no source of excitation is on file, and at m_q = m_p/3 it costs mu_p.
   (B): 4244's u is unlocalised along one axis; any seat width moves g_A down -- the omitted direction is a real
   part of the residual, of size set by w.  (C): the u-u exchange adds a further ~2% of g_A at the breath's width.
```

## 3. Result

**(A) Lever 3 as filed is closed as a mechanism search.** Closing g_A by excitation needs every mode's momentum
×1.49, about 0.6 quanta per mode. No source is on file.

**(B) and (C) are real, zero-parameter parts of the residual, but their size depends on w.** At w = r_ZBW/√2, the
width every held direction has under 4243's rule, the omitted axis gives g_A = 1.332 (+4.5%). The u–u exchange
takes it to 1.308 (+2.6%). Together these remove about three quarters of the residual. w is not fixed by anything on
file.

**The structure every row shares: g_A and μ_p move together.** Every mechanism that lowers g_A — excitation,
localisation, exchange — lowers μ_p through the 4242 tie, by about 5% at the point where g_A closes (m_q = m_p/3).
Keeping μ_p then needs m_q ≈ 297 MeV instead of 313. 4243 (T) found the same (296.7). So the g_A residual is
really the 4243 tension between g_A and SS-2's assignment m_q = m_p/3, and that assignment is not derived (SI-1 M9).
No additional motion can remove it at m_q = m_p/3.

## 4. PD-008 — the convenient branch, marked

w = 0.315 fm lands g_A at 1.269 (−0.5%). Choosing it would be a fit, and μ_p there is −5.7%. Not adopted. The result
stated is the pair at the breath's own width, 1.332 / 1.308. w goes to the founder as a physical question, below.

## 5. Founder question (a physical picture)

An up quark breathes out and in toward its vertex, and sideways toward the down quark. It does not breathe toward
the other up. Along the third direction — in the plane, across its line to the down quark — **is it held on its
vertex as firmly as along the directions it breathes, jittering by the same ZBW amount, or held more loosely (or more
tightly) by the frame?**

## 6. Filed in `todolist.md`

- The w question, recorded as awaiting the founder.
- u–d exchange under colour = vertex (frame-geometry change), EW → strong.
- The m_q tension: derive m_q, or show why g_A and μ_p jointly require ≈ 297 MeV, SS lane with EW.
