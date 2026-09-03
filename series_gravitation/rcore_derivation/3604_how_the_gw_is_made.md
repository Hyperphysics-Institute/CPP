# How the gravitational wave is made — in GR, and what CPP must supply. It is not an EM wave; it is the Sea's spin-2 transverse polarization, sourced by the binary's changing mass-quadrupole. And the scalar census wave that CPP also has must radiate at < 5% of GR's amplitude or fail the binary pulsar

**Patch 3604, Session 161, 3 Sep 2026.** Verify `code/3604_scalar_radiation_bounds_verify.py` (5/5, order-of-magnitude). Founder statement in `founders_voice/`. Reasoning `reasoning/3604.md`.

## §1 Is the GW an EM wave? No — six facts

1. **What it couples to.** GW moves every mass, charged or not; EM moves charge. A neutral test mass responds to a GW and not to an EM wave.
2. **GW150914.** Two ~30 M_⊙ black holes, no matter to speak of, no electromagnetic counterpart of any kind — and a wave at `h ≈ 10⁻²¹` seen by two detectors.
3. **GW170817.** The gravitational wave arrived **1.7 s before** the gamma-rays from the same neutron-star merger. Two different waves: the EM one from the merger's *ejected matter*, the GW from the merger's *mass motion*.
4. **Transparency.** A 100-Hz GW passes through the Earth (the two LIGO sites see it with a 10-ms light-travel offset); 100-Hz EM does not propagate through rock.
5. **Polarization symmetry.** GW is spin-2: the `+` and `×` patterns repeat under a 90° rotation about the propagation axis. EM is spin-1: its patterns repeat under 180°.
6. **Lowest radiating multipole.** GW: quadrupole (the mass monopole and dipole are conserved — mass, momentum — and cannot radiate). EM: dipole.

So "extreme movements of mass generate a massive EM wave" is not what the detectors have measured. **But the founder's instinct is the right structural one:** the GW is *like* an EM wave in exactly the sense that matters here — **both are transverse polarizations of the medium** (the Sea), carried by DI-bit summations (founder, 3600). EM is the Sea's spin-1 (dipolar) transverse polarization sourced by *charge* currents; GW is the Sea's spin-2 (quadrupolar) transverse polarization sourced by *mass-energy* currents. Same medium, two ranks.

## §2 How GR makes it

Take two masses orbiting. Their **mass quadrupole** `Q_ij = Σ m x_i x_j` changes in time (the monopole `Σm` and dipole `Σ m x_i` are conserved and cannot radiate). Linearized GR says the metric far away carries a transverse-traceless strain

    h_ij^TT(t, r) = (2G / c⁴ r) · Q̈_ij^TT(t − r/c),

propagating at `c`, with two polarizations, and carrying energy away at the rate `L = (G/5c⁵)⟨Q⃛_ij Q⃛_ij⟩` — the quadrupole formula. The binary pulsar B1913+16 has been losing orbital energy at exactly that rate, to 0.2%, for forty years. That is "how the GW is generated in GR": *nothing propagates from body to body; the pair's changing shape shears the field, and the shear propagates.*

## §3 What CPP must supply — the mechanism, as far as the axioms already go

CPP has the ingredients registered and not derived:
- The DI-bit payload carries the emitter's **vector** state (E-separation, S-arc — the A3′ `V_i`, `Q_ij` broadcast channels), not only its count.
- Two orbiting masses emit DI-bits whose *vector* content, summed at a distant GP, has a **time-varying quadrupolar pattern**: the Sea there is polarized transversely, stretched along one axis and squeezed along the other, rotating at twice the orbital frequency. That is the `+`/`×` pattern. The count (`SSV_abs`) from the pair, summed at the same GP, varies only through the pair's changing *distance* — the scalar T-1 wave.
- So CPP's binary makes **two waves**: the scalar census wave (T-1, ratified) and the Sea's quadrupolar transverse polarization (`Q_ij`, registered as `op:einstein`, OPEN). The tensor one is what LIGO sees; its wave equation and its luminosity are what the theory must derive — and the luminosity must be GR's to 0.2%.

**The founder is right that nothing fundamentally different has been missed**: the channel is in the axioms. What is missing is a derivation, and it has a hard numerical target.

## §4 The scalar wave: bounded, and the bound is sharper than it looked

3603 said the scalar admixture `ε` "must be small." Here is what "small" means, at order of magnitude:

- **Amplitude.** For a massless scalar with T-1's normalization, the far-field quadrupole term is `u ≈ (G/2c⁴r)·n_i n_j Q̈_ij` — the *same* `G Q̈/c⁴ r` scaling as GR's tensor strain. Naively `ε_amp ~ ¼`. Nothing in T-1 suppresses it.
- **The interferometers are nearly blind to it.** An isotropic PSR modulation gives a Michelson differential of `(kL)²/6 ≈ 10⁻⁵` (3602). So — unexpectedly — the LIGO–Virgo *polarization tests do not strongly bound this mode by amplitude*; the breathing mode they test for couples to the arms differently from a PSR modulation. (Pulsar-timing arrays, which time light over kiloparsecs, would see it; NANOGrav's non-tensor limits apply and are weaker.)
- **Energy loss bounds it hard.** Any radiated scalar energy comes out of the binary's orbit. Hulse–Taylor's 0.2% agreement with the quadrupole formula bounds the scalar luminosity to `ε_L < 2 × 10⁻³`, i.e. `ε_amp < ~0.045` (comparable angular structure). **The T-1 scalar wave must radiate from a binary at least ~5× below its naive amplitude, or CPP fails the binary-pulsar test.**

Whether T-1 + T-3 (the census equation with its conserved source) supply that suppression — the way T-3 already kills the *monopole* (Birkhoff, T2-2) — is a computation the corpus has not done. **OPEN-GR-SCALAR-RADIATION-1** minted: *the quadrupole scalar luminosity of a binary in the ratified census dynamics, against Hulse–Taylor.* It is a T-1-level calculation, not a charter, and it is the second thing the lane must do — after, or alongside, the `Q_ij` derivation.

## §5 Standing
- Not an EM wave: settled by observation, §1.
- The tensor channel: registered (`op:einstein` / A3′ `Q_ij`), mechanism sketched from the axioms (§3), derivation OPEN — **OPEN-GR-TENSOR-1**, target luminosity = GR's to 0.2%.
- The scalar channel: exists in the ratified theory, nearly invisible to interferometers, bounded by binary-pulsar energy loss to `< ~5%` amplitude — **OPEN-GR-SCALAR-RADIATION-1**, a computation.
- The R-core arc: paused (3603) until TENSOR-1 establishes that the exterior tensor equations are CPP's.

## §6 F-11 to the founder — the mechanism, as a picture
Two masses orbit. Each broadcasts DI-bits every Moment carrying its state; at a distant GP the summed **vector** content of the pair's DI-bits points along the line to the pair, and that line *rotates* as they orbit. **Does the Sea at that GP respond to a rotating incoming vector pattern by a quadrupolar transverse deformation — DPs separated along one axis and compressed along the perpendicular one — the way it responds to a rotating incoming EM field by a dipolar polarization?** If yes, that is the `Q_ij` channel and the GW; the derivation is the relay dynamics of that deformation (the tensor analogue of T-1). If the Sea responds only through the count, CPP has no tensor wave and the exposure stands.
