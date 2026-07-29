# OPEN-SEA-DENSITY-1 — THE SEA'S PHYSICAL DENSITY IS UNKNOWN

**Registered Patch 2858, 28 July 2026, on founder ruling (b) of the
2026-07-28 decision set. Consequence: Patch 2855 is downgraded to
PROVISIONAL.**

---

## §1 — The founder's ruling, verbatim

> I do not know the density of the DPs. I had provisionally envisioned
> the DPs to be numerous and shallow in their oscillations, but the
> Schroedinger wave dispersion of the electron cloud and the de Broglie
> wavelength of mass may indicate a larger DP separation distance. The
> answer is, I don't know. This is entirely a triangulation
> measurement. All these types of phenomena should be determined by a
> swarm analysis of reality/experimental phenomena. I don't think we
> can guess our way into it, but I do think we can triangulate our
> results to calibrate what reality actually is.

## §2 — The committed numbers are a calibration convention, not a measurement

This ruling does not overturn a measurement. **There was never a
measurement.** The α1-arc parameters carry their own provenance:

| quantity | committed value | how it was obtained |
|---|---|---|
| d_DP | 0.3640220 fm | the lattice/DP spacing `a` inherited by the arc |
| κ_D | 5.4941731 /fm | **imposed** as κ_D = κ = 2/d_DP |
| θ (agitation scale) | 24.4100 q²/fm | **defined by that imposition**, not derived |
| n_DP | 29.3178443 /fm³ | follows from κ_D² = 4π n_CP q²/θ |

**`alpha1_s1_s2_record.md` flagged this at the time**, in its own
words: imposing κ_D = κ = 2/d_DP *"DEFINES the agitation scale θ… θ is
not independently derived — **CHI-INCOMPLETE** on that component,
**question with the founder**."*

**The founder has now answered that question, and the answer is "I
don't know."** The parameters are a self-consistent calibration
convention that has been carried as though it were a physical state.
The open item that was raised at α1 and left pending is hereby
promoted, named, and made blocking for anything that depends on the
Sea's geometry.

## §3 — What Patch 2855 actually depends on

2855's verdict rests on a **single dimensionless ratio**:

> **η ≡ d_DP · n_DP^(1/3)** — the bond length in units of the mean
> inter-pair spacing.

At the α1 calibration, **η = 1.1225**: each pair's own two CPs are
farther apart than the distance to the nearest neighbouring pair, so
the two CPs sample independent environments and the drift ratio
saturates at 1/√2. That is the whole of the 2855 argument.

**If η is much smaller, 2855's conclusion can invert.** From 2855 §4's
own scan, holding d_DP fixed and diluting self-consistently:

| η | R_drift RMS | R_drift median |
|---|---|---|
| 1.1225 (α1 calibration) | 0.711 | 0.706 |
| 0.521 | 0.648 | 0.650 |
| 0.242 | 0.479 | 0.429 |
| 0.112 | 0.294 | 0.217 |
| **0.0751** | **0.2195** | **0.1522** |

**On the frozen RMS statistic, no scanned value of η reaches the 0.15
bar.** The median crosses at roughly η ≈ 0.075. So Route 2 revives only
if η is **well below 0.075** — the Sea at least ~10⁴× less dense in
number than the α1 calibration — and at that point the RMS-vs-median
choice (2849 D4's "frozen RMS/tail definition") becomes
outcome-determining and must be settled before, not after, the number
is computed.

**Patch 2855 status: PROVISIONAL, conditional on η. Its physics — the
saturation mechanism, the 1/√2 ceiling, the regulator-sensitivity of
L_field — is unaffected and stands as a function of η. Only its
application to the physical Sea is suspended.**

## §4 — The founder's triangulation targets

Named in the ruling, both pointing toward **larger** DP separation
(smaller η, favourable to Route 2):

1. **Schrödinger wave dispersion of the electron cloud.** The spatial
   scale over which the orbital electron's wave description disperses
   should be set by the Sea's response granularity if the Sea is what
   the wave is a description of.
2. **The de Broglie wavelength of mass.** If λ_dB is a Sea-response
   wavelength, it constrains the Sea's spacing directly.

Both sit at atomic/Compton scales, **orders of magnitude above the
0.364 fm the α1 calibration assumes.** That is the source of the
founder's "may indicate a larger DP separation distance," and it is
also — if it survives — potentially the η ≪ 0.075 that Route 2 needs.
**This is stated as the direction of the tension, not as a result. No
number is claimed here and none should be quoted from this section.**

## §5 — Method: triangulation, not derivation

Founder-specified: *"All these types of phenomena should be determined
by a swarm analysis of reality/experimental phenomena. I don't think we
can guess our way into it, but I do think we can triangulate our
results to calibrate what reality actually is."*

**Constraints on any future work under this item:**

- **No guessing.** A value proposed from internal consistency alone
  (the α1 route) does not close this item, because that is exactly what
  produced the state being corrected.
- **Multiple independent anchors required.** Triangulation means ≥3
  phenomena with independent error structure, converging.
- **L-1 stands:** AUTOMATON occupancy values are regime artifacts and
  are forbidden as physical anchors.
- **The bar is set before the number is computed**, including the
  RMS/median choice, per the withheld-key discipline.

## §6 — Blocking scope

**This item blocks:** any promotion-critical use of the Sea's geometry;
the 2855 verdict's application to the physical Sea; any revival of
Route 2; any characterisation of the Sea as dilute or dense in SF-8 or
elsewhere.

**This item does not block:** SF-8's two authorized results (neither
depends on density); PR1/PR2/PR3/PR5/PR6, all MET; the emergent-Coulomb
and ZBW-Sea measurements; the magnetic curl derivation.

**It does not un-block PR7.** 1B remains OPEN. The ledger stays at six
of seven. **The status of 1B is now "open, and the route that would
close it depends on a quantity nobody has measured" — which is a more
honest description of the same gap, not a smaller one.**

## §7 — The worker's error this corrects

The α1 record flagged θ as CHI-INCOMPLETE and referred the question to
the founder. **That referral was never made.** The parameters were
carried forward through the KINETIC-1 arc, the S4-X campaign, the
Darwin restoration and into 2855 as though the pending question had
been closed. 2855 then used them to reach a verdict, and the verdict's
entire force came from the one ratio the unasked question controls.

**Patch 2855 §7 claimed "every input is a committed number with a cited
patch."** That was true and it was not sufficient — committed is not
the same as ratified, and a number can carry a clean provenance chain
back to a decision nobody ever made. The self-check tested the wrong
property. **Add to the guard: for any load-bearing input, check not
only that it is committed but that its own registration does not carry
an open flag.** The α1 record's CHI-INCOMPLETE marker was one grep away.
