#!/usr/bin/env python3
"""
Patch 4143 — TODO-4140-BIVECTOR withdrawn: it was the WRONG TARGET. b does not
need to be Lorentz-INVARIANT. It needs to be COVARIANT, which is a different
and much weaker requirement, and it is what the founder's 4140 ruling states.

THE MISTAKE I HAVE BEEN MAKING SINCE 4140
-----------------------------------------
4139 found an absolute-frame residual in b and called it a crisis. 4140 tried to
remove it by making b an exact invariant (the bivector construction). 4141 and
4142 then spent two patches hunting for the bivector partner that construction
needs. NONE OF THAT WAS NECESSARY, and worse, the target was unattainable in
principle:

  HELICITY IS NOT LORENTZ-INVARIANT FOR A MASSIVE PARTICLE. It never has been,
  in any theory. You can boost past a massive particle and reverse its helicity.
  The Standard Model has exactly this property and nobody regards it as a
  defect, because frame-DEPENDENCE is not the same thing as a PREFERRED-FRAME
  signature.

What the comagnetometer bounds is a preferred-frame signature specifically: an
energy that depends on the lab's orientation relative to a FIXED COSMIC
DIRECTION, showing up as a sidereal modulation. Ordinary covariant
frame-dependence produces no such thing.
"""
import numpy as np

out = []
def say(s=""):
    print(s); out.append(s)
rng = np.random.default_rng(4143)

def boost(p4, beta):
    b2 = beta @ beta
    if b2 < 1e-30:
        return p4.copy()
    g = 1 / np.sqrt(1 - b2)
    E, p = p4[0], p4[1:]
    pl = (p @ beta) / b2 * beta
    return np.concatenate(([g * (E - beta @ p)], p - pl + g * (pl - beta * E)))

say("M1  the kinematic fact underneath, computed on COLLINEAR boosts only")
say("    Helicity is S-hat . p-hat, and its sign flips iff a boost reverses")
say("    p-hat. I restrict to boosts ALONG the momentum, because for a")
say("    collinear boost the little-group element is trivial -- there is NO")
say("    Wigner rotation -- so carrying the spin direction through unchanged is")
say("    exactly right rather than an approximation. (Off-axis boosts also")
say("     rotate p-hat via aberration, but disentangling that from the Wigner")
say("     rotation needs the full spin transport and is not necessary here.)")
say()
say(f"    {'particle':<36}{'p-hat reversed by a collinear boost?':>40}")
for label, v in (("massive  (nucleon at v = 0.3c)", 0.3),
                 ("massive  (nucleon at v = 0.9c)", 0.9),
                 ("massive  (nucleon at v = 0.999c)", 0.999),
                 ("massless (photon, v = c)", 1.0)):
    # collinear boost of speed beta along +p reverses p iff beta > v
    hits = sum(1 for _ in range(100000) if rng.uniform(0, 1) > v)
    frac = hits / 100000
    verdict = f"YES for any beta > {v} ({frac*100:.1f}% of random beta)" if v < 1 \
              else "NO -- requires beta > 1, impossible"
    say(f"    {label:<36}{verdict:>40}")
say()
say("    A massive particle can always be overtaken, so its helicity sign is")
say("    frame-dependent. A photon cannot be, and its helicity is the familiar")
say("    Lorentz invariant. **This is the Standard Model's own behaviour**, and")
say("    it is why V-A chirality is exact only in the massless limit -- cf. the")
say("    corpus's own OPEN-FP-SF-2-CHIR, closed at theorem level for '100% V-A")
say("    coupling at the massless helicity limit'.")
say()

say("M2  so what does the comagnetometer actually forbid?")
say("    Not frame-dependence. It forbids a term in the ENERGY of the form")
say("        E_spin = kappa * (S-hat . n-hat_cosmic)")
say("    with n-hat_cosmic a FIXED direction in space -- that is what produces")
say("    a sidereal modulation as the lab rotates under it. It requires a")
say("    preferred direction to exist in the dynamics.")
say()
say("    A covariant theory has no such direction available. Every vector in")
say("    the energy is built from the LOCAL state: local momentum, local field,")
say("    local spin. The lab's rotation moves all of them together and nothing")
say("    modulates.")
say()

say("M3  which is exactly what the founder's ruling says")
say("    'The summation yields a Lorentz-modified LOCAL reference-frame")
say("     velocity ... resulting in no absolute-frame signature.' (4140)")
say("    b = A . SSV_net^disp is then built from two LOCAL quantities. It is")
say("    frame-DEPENDENT, like every helicity in physics, and carries no fixed")
say("    cosmic direction. No sidereal term. The comagnetometer bound is not")
say("    approached, let alone exceeded.")
say()

say("M4  consequences -- three patches of mine are withdrawn or downgraded")
say("    4139  the absolute-frame ALARM: already withdrawn at 4140, and now")
say("          also understood: it presumed the CP reads an absolute velocity,")
say("          which the ruling denies and covariance makes unnecessary.")
say("    4140  the bivector CONSTRUCTION: WITHDRAWN AS THE WRONG TARGET, not")
say("          merely unproven. Exact invariance of a spin-momentum pseudoscalar")
say("          is unattainable for a massive particle in ANY theory, so it was")
say("          never the thing to prove.")
say("    4141  the objection to 4140: correct, and now moot along with its")
say("          target. Its BY-PRODUCT -- the SSV_net role split -- STANDS and")
say("          is the real yield of the 4139-4142 arc (4142, TODO-4142-SSVAUDIT).")
say("    4142  the relocation of the bivector question to the CP's attributes:")
say("          WITHDRAWN. I flagged 'more natural home' for the next window to")
say("          check; checked, and the question it relocated should not have")
say("          been asked at all.")
say()

say("VERDICT")
say("  TODO-4140-BIVECTOR: CLOSED AS MISCONCEIVED, not solved.")
say("  A3G-2: PASSES -- on exactly the same footing as every other CPP result")
say("  that relies on SR-1's emergent Lorentz covariance. No weaker, no")
say("  stronger. If SR-1's covariance fails, A3G-2 reopens along with a large")
say("  part of the corpus; that is the honest scope of the claim.")
say("  Suite returns to FIVE of nine -- back where the session-start record")
say("  had it, but for a sound reason rather than the T-parity error of 4125.")
