# Reasoning capture — Patch 2022: does Thomas's asymmetry correction rescue R2? No.

**STATUS: verbatim (captured at-patch).** Window: 2000-band. Opus worker; integrator = Thomas.

Thomas correctly corrected my oversimplification: the inverse-square field is stronger on the near pole, so
the poles displace unequally and the DP centroid shifts (not a symmetric stretch). He asked if it could make
a difference. I took it seriously because it aims at the ONE quantity that could flip the 2021 retraction:
eps0's C-scaling (Z0=C/c; if asymmetry made eps0~1/sqrt(C), then with c~sqrt(C), Z0=const => PASS revives).

I computed it honestly (let the exponent land wherever): two poles, stiffness C, full inverse-square drive,
self-consistent, sweep C. Result: eps0 ~ C^(-1.00) in the linear/LPI regime, C^(-1.07) even under huge
asymmetry (field_asym ~1.08, big centroid shift). So the asymmetry is REAL (centroid shifts, Thomas right)
but does NOT move the leading exponent off -1. eps0 ~ 1/C robust => Z0 = C/c unchanged => R2 still leans FAIL.

I was careful not to taste toward confirming my own retraction: the fit was free to give -0.5 and would have
revived PASS; it gave -1.00. Reason it's robust: leading-order each pole displaces by force/C, so the dipole
polarizability is set by the curvature C; the asymmetry adds multipole/centroid structure on top, not a
rescaling of the leading term.

Credit where due: Thomas probed exactly the right quantity (eps0), not a red herring -- it was the only lever
on the verdict. It just doesn't move the leading scaling. The correction does matter for the polarization
FORCE (gravity side), which is genuinely gradient-driven; just not for the impedance.

Discipline: owned path only. NO THEO. Honest negative. Files via bash; git status verified.
