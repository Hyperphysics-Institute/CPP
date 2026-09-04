# Founder ruling — DI-bits are transient one-hop messengers; the GP register (SSV_abs, SSV_net) is what relays from source to detector; the medium's CP/DP concentration sets the propagation rate (3 Sep 2026, Session 161)

**Status:** verbatim founder text, registered Patch 3606. Ruling minted: **R-REGISTER-RELAYS-NOT-DI-BITS** (a restatement of AP-4 / T-1 C-i, now applied to gravitational radiation).

> "I think I see the problem. Please refer back to the place where we described
> the operation of the DI-bits in detail. I think we did it in DM, DE, and/or
> GR. The DI-bits do not carry information from the Gravitational source to the
> detector. The DI-bits are transient. The GP DI-bit emission is constant,
> uniform, and unchanging for every GP in the universe. The DI-bits emitted one
> Moment ago are dispersed to GPs at one PSR distance to inform them of the
> GP_origin's state, and are then redistributed to all GPs so that all emit the
> same DI-bit quota/cohort each Moment. The real question is what the CPs do in
> response to the SSV_abs and SSV_net they receive each Moment. The SSV_abs in
> the pulsar Binary will be the superposition of the two SSV_abs fields. The
> DI-bit count will be invisible, as it only acts between GPs at PSR distance
> and produces no lasting signature that radiates. The GPs carry the SSV_abs
> superposition as a sum from the binary pulsar source to the detector. The CP
> and DP concentration of the media (through space/the lattice/the vacuum
> filled with DPs) will modify the propagation rate, as they do in all signal
> propagation scenarios."

*Opus (Patch 3606):* agreed on every point, and it is the T-1 relay exactly (AP-4: fixed uniform emission; payload = the origin GP's registers; one hop; the receiving GP integrates and re-emits its own state). It sharpens the question rather than dissolving it: **the register that relays has rank 0 (the count) and rank 1 (the vector sum). A gravitational wave is rank 2.** A rank-1 relay makes spin-1 waves and cannot make the `+`/`×` pattern (proven, `code/3606_rank1_relay_no_spin2_verify.py`). See `rcore_derivation/3606_rank_of_the_register.md`.
