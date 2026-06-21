# Reasoning capture — Patch 2002: R2 / Z₀-geometric via the harmonic virial mechanism

**STATUS: verbatim (captured at-patch).** Window: 2000-band. Opus worker; integrator = Thomas.
Continues the OPEN-COSMO-DM-2 lane after 2001 (P(k) closure). Target: R2, the VSL μ↔ε falsifier.

## The job and the trap
Thomas asked me to elevate the buried 0739/0740 μ↔ε note into a decidable substrate computation, since
it's the last clean-kill candidate for the EU-1 horizon mechanism. The trap I had to avoid: the
framework "wants" Z₀ to be geometric (PASS), and 0740 already wrote three corpus facts pointing that
way. Reciting those and declaring victory would be motivated reasoning. Falsification-first means I had
to actually derive Z₀'s C-dependence and be willing to find it carries C (a kill).

## What the reduction already gave me (0740, correct and kept)
c=1/√(μ₀ε₀), α∝√(μ₀/ε₀)=Z₀ ⇒ Δα/α = Δln Z₀, A=−dZ/dc. So the whole thing is "does Z₀ move under SSV?"
0740 reduced it cleanly but only ARGUED the answer. I needed to compute it.

## Where the real physics was
Two corpus facts decided the computation:
1. c02: stiffness C = α_geom·E_P/l_P³ is the SSV-variable quantity; the ZBW frequency ω_ZBW~1/t_P is
   FIXED by the Absolute Moment (geometric), not a function of C.
2. c06/0743: "there is no separate B field — B is the rotation of the same DP whose radial displacement
   is E." This asserts a SINGLE oscillator with one stiffness, E=radial, B=rotational.

Fact 1 is double-edged and I made myself confront it: ω_ZBW fixed ⇒ m = C/ω_ZBW² ∝ C. So IF the
magnetic response had its own inertia (independent oscillator), μ₀ ∝ m ∝ C while ε₀ ∝ 1/C ⇒ Z₀ ∝ C ⇒
A~O(1) ⇒ a clean ~6-order KILL. The naive "fixed ZBW" reading actually points toward FAIL. That is the
honest danger 0740's three-facts gloss hid, and I refused to skip it.

## The mechanism I found (the actual content beyond 0740)
The c06 single-oscillator picture rescues it, but NOT for the reason 0740 gave ("they share a
stiffness"). The real mechanism is the HARMONIC VIRIAL THEOREM: for one oscillator ⟨KE⟩=⟨PE⟩ exactly
(because ω²=C/m). In the DP Sea the kinetic energy IS the magnetic field energy and the potential energy
IS the electric field energy. Their equality forces the electric:magnetic energy ratio — hence Z₀ — to
be geometric, with C cancelling in the ratio while surviving in the product μ₀ε₀=1/c² (so c varies =
gravity, with the right sign: stiffer→faster, c∝√C, matching the VSL early high-c_eff). This converts
0740's three hand-wave facts into ONE derivable mechanism, and it's checkable: I coded both readings and
confirmed Reading A gives A=0 exact (Z₀ flat across 4× C) while Reading B gives Z₀∝C¹ (A~O(1) fail).

## Why I kept it conditional (honesty boundary)
I did NOT claim R2 closed. The PASS is conditional on the single-oscillator structure, and Reading B is
a real clean kill. The c06/0743 cartoon is currently logged as "a physical cartoon, NOT in the corpus as
a derivation" — so the load-bearing claim is unproven. The honest verdict: R2 advances from "open
falsifier" to "PASS-conditional on one formally-establishable EM-sector claim (no independent magnetic
inertia), with the virial mechanism as the test, and a bounded anharmonic residual." The clean-kill
exposure is removed; the conditional remains. That is a real elevation of the note — derived mechanism +
explicit falsifiable fork — without overclaiming a closure the corpus hasn't earned.

## Residual I quantified
Anharmonic A ~ ε_anh·strain². For the tight local clock-LPI bound the strain is the LOCAL potential
~10⁻⁶, so A~10⁻¹²·ε_anh ≪ 10⁻⁶ — safe. I made sure to use the local strain for the local bound rather
than a cosmological strain, so as not to manufacture either a false alarm or a false comfort.

## Discipline
- Worker patch, owned greenfield path series_relativity/development/mu_eps_closure/ only. NO edit to
  c06, dp_sea_mu_eps_symmetry.md (0740), CONJ.md, or SR.md — proposed cross-refs handed to the
  integrator (§6 of the finding).
- NO THEO (structural derivation conditional on the single-oscillator structure; no new axiom/term/
  counted prediction). Consistent with no-THEO-for-conditional and how 0740 was scoped.
- Patch 2002 in the leased 2000–2099 band.
