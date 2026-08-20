# FAQ — GR-1d

**Q1. What is an echo, and why would a black hole produce one?**
A repeat pulse after the main ringdown. It requires something to bounce
off. GR's horizon is a perfect one-way membrane, so a ringdown decays
and the signal ends. If the interior instead holds a Planck-density core
(GR-1c), perturbations reaching the near-horizon region are partially
reflected, bounce against the photon-sphere barrier at r ≈ 3r_S/2, and
leak back out as a train of pulses.

**Q2. Where does the delay formula come from?**
It is the round-trip travel time in tortoise coordinates between the two
boundaries: Δt = (2r_S/c)[ln(r_S/l_P) − 0.193 + O(l_P/r_S)]. The
logarithm is the signature of near-horizon propagation; the −0.193 is
negligible against ln(r_S/l_P) ≈ 88–93 for any astrophysical hole.

**Q3. Is this tuned to match anything?**
No, and this is the paper's central comparative claim. Since
G = ħc/m_P² gives r_S/l_P = 2M/m_P, the delay is a function of M/m_P
alone: Δt(M) = (4GM/c³)·ln(2M/m_P). Gravastar models place the
reflective surface at r_S(1 + 10^−X) with X model-dependent; fuzzballs
at the string length. Both can absorb a non-detection by adjusting a
parameter. The Planck length cannot be adjusted.

**Q4. Has anyone looked, and did they find anything?**
The paper discusses the Abedi–Dykaar–Afshordi (2016) echo claim and the
subsequent controversy. Nothing here rests on that claim being correct.
The CPP-specific search — running the Δt(M) template against O1–O4 data,
event by event using each remnant mass from the inspiral — is explicitly
deferred to a dedicated analysis and has not been done.

**Q5. Could LIGO see the GW150914 echo?**
Not quite. The 112 ms delay corresponds to 8.9 Hz repetition, just below
LIGO O4's ~10 Hz lower cutoff. The Einstein Telescope's design
sensitivity reaches ~5 Hz, which brings it inside. For lighter remnants
the situation is better: 30 M_☉ gives 19 Hz, comfortably within current
sensitivity.

**Q6. If echoes were not seen for a 30 M_☉ merger, would that kill the
theory?**
It would be a serious problem for the *delay* prediction, which is
parameter-free — but not automatically fatal, because the paper has no
**amplitude** prediction. |R_core| = 1 is assumed, not derived; a small
real reflectivity would push the echoes below detectability without
changing the delay. This is a genuine weakness and the paper's own open
problem 1, not a retrofitted escape.

**Q7. Why isn't there an amplitude prediction?**
Because it requires the strong-field *interior* — the dynamics at
PSR_eff = l_P/2 — which needs the full CPP field equation evaluated
inside. The Session-150 field-equation programme derived the exterior
census equation (T-1) and the uniqueness and source theorems, but the
interior remains at `op:einstein`. Until that moves, there is a delay
formula, no strain formula, and hence no complete matched-filter
template.

**Q8. Why is the reflecting surface at r_S + l_P rather than at the core
radius r_S/2?**
Because the effective reflection for a wave in the tortoise coordinate
happens at the near-horizon quantum boundary, not at the core's
geometric radius. This is the step most worth external scrutiny: the
delay is logarithmically sensitive to that choice, and no reviewer has
yet examined it.

**Q9. Does spin change the answer?**
Yes, at order (a/r_S)². The present calculation uses the Schwarzschild
potential barrier; a Kerr treatment needs the Kerr QNM spectrum and the
spin-dependent barrier location. Registered as open problem 2.

**Q10. Has this paper been reviewed?**
No — no dedicated CONV round exists. And the inherited structure is
thinner than it looks: CONV-027 reviewed GR-1c's field-equation
Proposition, *not* the Planck-core theorem this paper depends on. The
exterior machinery is standard GR and was independently exercised at
CONV-029, but the CPP-specific content here is unexamined.
