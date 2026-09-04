# Founder statement — the original conception of the PSR had θ,φ (azimuth/elevation) dependence; the isotropic single-radius PSR was introduced in the AI rewrite; could the spherical PSR with time-delayed superposition reproduce the tensor effect at second order? (3 Sep 2026, Session 161)

**Status:** verbatim founder text, registered Patch 3607. Two items: a *provenance* statement (**P-ORIGINAL-DIRECTIONAL-PSR**, to be recovered) and a physics question (answered by computation in `rcore_derivation/3607_original_psr_and_the_rank_theorem.md`).

> "I think what you are really asking is how gravity works. Is this kind of
> configuration necessary to produce the gravitational effect, period? We have
> based the entire GR-1 and companion set, and all other effects that are
> related to SSV_net, on the idea that there was a single-radius sphere PSR,
> and that the gravitational effect was calculable based on that. This was not
> the way I originally wrote up the theory when I presented it to Grok over a
> year ago. Then, when you took it over (Sonnet first, then Opus), the theory
> was rewritten as an isotropic effect, with no azimuthal or elevation effects
> on the PSR's radius. In other words, this is a fundamental rewrite of the
> theory. It was my original conception of how gravity worked, but a single PSR
> at all azimuths and elevations replaced it. What you are essentially saying
> is that, to reproduce GWs, we must reincorporate my original theta, phi
> dependence to produce the GW effect. It appears that this refinement is
> invisible in the less complex GR-type experiments, and GR/gravity works with
> the simplified spherical PSR."

> "Is it possible that the spherical PSR would work by the superposition of the
> SSV_abs gradient of the two in such a way that there is a second-order effect
> that reproduces the GW/binary pulsar effects? I know you calculated it, and
> you basically said it is scalar addition and that such operations are linear,
> rather than having the second-derivative effect we need for the tensor field.
> It seems like the time-varying value from each star in the pulsar makes the
> superposition vary nonlinearly. The position of each star is varying as it
> orbits, and the superposition at every point is interacting with a
> time-delayed signal coming from a different distance at each moment, with the
> value of the SSV_abs from each star changing because of the changing distance
> and changing time delay from two different bodies. This system seems complex
> enough that a non-linear/second order/tensor type space-time varying SSV_abs
> might reproduce the GW tensor's complexity."

*Opus (Patch 3607):* (1) The provenance point changes the standing of the tensor question: what 3606 called a "CPP-native candidate" is the founder's **original** conception, simplified away in the rewrite. Restoring the directional PSR is a restoration, not a new rule; the retained corpus does not contain the original formulation (searched: the Grok-era GR-1c/GR-1f notes carry only the isotropic law plus a vector cross term), so it must be restated by the founder. (2) The second-order question is answered by direct computation: **no** — retardation and orbital motion give the right frequency (2Ω) and even the right amplitude scaling, but the stretch/squeeze content of a scalar field, however complex its source, falls as 1/r³ against the longitudinal 1/r; complexity does not change rank. And a bonus discriminator: the scalar radiates *nothing* along the orbital axis, where GR radiates most.
