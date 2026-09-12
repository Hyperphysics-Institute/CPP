# Founder question, 12 Sep 2026 — "the only motive forces I can think of… do you have any ideas?" (Patch 3517, DM block, from this window under PD-006)

**Founder text verbatim:**

> The engines that I have imagined, the entropic dilution into the edge with nothing, the KE developed by the motion between GPs, and the repulsion of like charges (which won't work) are the only motive forces that I can think of. Do you have any ideas?

## Worker's reply — five candidates, each held against the corpus's rules; one checked and found to change the shape of the problem

The question is what carries the crowding down past one CP per Planck sphere fast enough for the pairing residue to freeze in the band. Five candidates, in order of how much they change things. None is minted; the last is checked with a toy and flagged as a fork for the founder.

**1. Ballistic KE (the founder's second engine).** The stored self-energy released as motion: every CP at the cap, c, in a thermal direction. A gas expanding freely thins at d ln R/dt = c/R; at the count law's end R ≈ N_CP^{1/3} l_P ≈ 10²⁸ l_P, so ~10⁻²⁸ e-folds per Moment. Thermal motion inside a ball does not thin the ball; only its edge moves. **Too slow by ~30 orders for a Planck-epoch freeze.** (Same verdict for the entropic driver: the corpus's engine stalls as N_rem → 0 by its own form.)

**2. The DP sea relaxing to its vacuum spacing (exclusion).** A DP in ZBW oscillation claims a Planck-sphere-scale volume; a sea of freshly formed DPs is over-dense relative to the vacuum's DP density and relaxes to it. This is a motive force with a *target* (the vacuum sea) but no rate on file, and the corpus has no exclusion rule for DPs as written. Candidate only.

**3. Photon pressure.** Pairing and annihilation release energy as photons (the founder's own two-shells-to-a-photon picture), which leave at c. The energy budget is OPEN-EU-REHEAT-BUDGET-1; the coupling of a photon flux to lattice thinning is not written. Candidate only.

**4. Perceptual dilution.** n̄ is the perceived count within the PSR; pairing halves the number of emitters per volume without moving anything. It changes what the engine reads, not the crowding a hop meets. Not a motive force.

**5. THE ONE THAT CHANGES THE SHAPE: the freeze is thermal, not dilutional.** The founder's walk-and-talk (3513) says pairing "does not go to completion" because of *the violence of thermal collisions*: pair ⇌ two lone charges, held open by kT. If that is the residue's origin, the freeze is not "hops stop finding partners" at Planck kT but the ordinary freeze of a two-body equilibrium as kT falls through the binding energy E_b of the pair (or of the trio's third) — and the expansion needed is not a Planck-rate quench but any expansion *slower* than pairing. Checked with a toy Boltzmann equation (`code/3517_thermal_freeze_idea.py`, 3/3; comoving density, cooling and dilution on one time τ, composition mode at fixed T and a):

| expansion time τ / pairing time | p |
|---|---|
| ≪ 1 (quench) | **0.50** — the Saha stoichiometry n_lone² ∝ n_pair ∝ n_q, kernel-independent |
| 3–30 | 0.58 → 0.51 (freeze later in denser regions) |
| 100 / 300 / 1000 / 3000 | **0.43 / 0.38 / 0.32 / 0.28 — all in the band** |
| → ∞ | → 0, logarithmically |

**What this means.** In a thermal freeze the band is not a knife-edge: p sits at ½ for fast expansion and drifts down through [0.21, 0.48] over *two to three decades* of τ — exactly the regime (expansion much slower than the reaction) that every ordinary freeze-out occupies. The dilution-only freeze of 3512 needed a quench of 5–50 Moments per e-fold at Planck kT that nothing on file can supply; the thermal freeze needs the opposite and ordinary thing. The engine's stall is no longer a problem, because the freeze is at kT ≈ E_b, not at Planck kT.

**The cost, and it is a fork for the founder, not a decision I can take.** 3510 Q7 placed the cutoff "by dilution at Planck kT, during evaporation," with 2543's MeV window for dressing only, and the bootup orientation says the same. The thermal freeze moves the residue's origin to the epoch where kT crosses the qDP (or third) binding energy — the sea's thermal era, after the count law — and makes E_b, not the Planck-epoch dilution rate, the number that fixes u. p is then robustly in the band; **u and D2 need E_b and the pairing rate**, which the corpus does not have for qDPs. The two pictures are mutually exclusive on *when* the residue is made.

**Question for the founder (pictures only):** In the sea after the count law's end, is a qDP a bond that Planck-temperature collisions break and re-make — so the lone charges are a thermal population, and the residue freezes when the sea cools below the bond — or is a qDP unbreakable once formed, so the residue is whatever never paired? The first is the walk-and-talk's picture and gives the band naturally; the second is 3510's and needs a Planck-rate quench that nothing on file supplies.
