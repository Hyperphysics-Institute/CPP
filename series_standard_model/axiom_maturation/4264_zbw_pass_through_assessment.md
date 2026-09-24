# ZBW as Pass-Through: Assessment of the Founder's Proposal, One Computation, and the Blast Radius

**Patch:** 4264. **Lane:** foundations (raised in EW → strong). **Session:** 239.
**Founder:** `founders_voice/4264_proposal_zbw_is_pass_through_shm.md` (proposal, pending ruling).
**Verify:** `series_standard_model/code/4264_route_C_pass_through.py`.

## 1. What is being proposed, and what it reverses

Today's picture: the quark falls to superposition with its vertex, **keeps its momentum**, passes through into the
hTetra interior, is turned back there by the like-charged vertices, crosses the vertex again, goes out into the Sea,
is turned back by the vertex, and repeats. Energy is conserved and exchanged between KE and the SSV gradient.

The ruling on file (3134 §3, R-ARC-CANCEL-TURNAROUND) says the pair's stored DP arcs have opposite senses and cancel at
co-location. That zeroes the inertia and makes stop-and-turnaround possible. The ruling itself names the
alternative: surviving inertia would carry the CPs *through*. The proposal takes exactly that branch.

## 2. What I think

**(i) The conservation argument favours pass-through.** Under arc cancellation the kinetic energy built up during the
fall is erased at superposition and rebuilt on relaunch. That is a non-conservative step in every cycle, exactly as
the founder says. Pass-through keeps it: KE at the crossing, SSV-gradient energy at the turning points. Every
standard treatment of Zitterbewegung makes it a sinusoidal, energy-conserving oscillation. In CPP, c04's own
mathematics is a *standing wave* at the Compton frequency. That is an SHM-type resonance, which fits pass-through
naturally. Only c04's Version 2.1 scope banner leans on the arc-cancel carrier.

**(ii) The founder's asymmetry argument is decisive even on 3134's own terms.** Arc cancellation needs the two arc
stores to be equal and opposite. A vertex held by its hTetra bonds moves less than the free quark falling onto it, so
at co-location the quark's store exceeds the vertex's. The remainder is surviving inertia, and 3134 §3 itself says
surviving inertia means pass-through. So in the baryon, 3134 predicts pass-through once the asymmetry is recognised.
For a free, symmetric DP the cancellation argument conserves momentum but still not energy, so (i) applies there too.

**(iii) Two refinements to the wording.**
- *"ZBW is SHM"* is right in kind but not in detail. SHM has force proportional to displacement, zero at the centre.
  The founder's force grows toward superposition, like Coulomb's law, and vanishes at co-location (no SSV gradient
  there). That is a conservative but anharmonic pass-through oscillation: fastest at the crossing, with a sharp
  speed peak. Both calculations in this arc bracket this: route (H), the harmonic reading, and route (C), the classical
  Coulomb reading, below.
- The founder's own sequence keeps **one Moment of co-location** ("the next Moment, the DP arcs act on the two
  superimposed charges"). So R-DWELL-1's one-Moment dwell would survive as co-location. What changes is that the
  velocity no longer goes to zero there, so the "relaunch amplitude" becomes carried-through momentum. That
  softens the impact considerably.

**(iv) For the current arc the proposal helps.**
- Route (H), every g_A number from 4243 to 4263, is already an oscillation centred on the vertex that passes through
  it. It is unchanged, and it is now better grounded. 4263's reading (E), where the bounce keeps its energy, is
  exactly pass-through.
- The one calculation built on the reset model, 4243 route (C), changes, and in its favour. Pass-through halves the
  fall time at the fixed Compton period, so the amplitude shrinks to about 0.6 of its value. The classical breath
  then **fits inside the frame** (0.47–0.56 fm, under the 0.62 fm u–d edge), which removes the reason 4243 rejected
  it. Its one-line g_A drops from 1.43–1.50 to 1.34–1.43 (rows below).

  With integer CP charges (4263) the Coulomb coupling a is no longer SS-2's colour coefficient, so route (C) is
  owed a coupling from the founder's charge picture. That item is filed.

## 3. Rows verbatim (D-11)

```
Compton period = 2 pi (units hbar/m_const c^2).  u-d edge = 0.620 fm.

  a = (2/3) alpha_geom  (0.298)  reset, 2 falls/period (4243 C)   amplitude 0.777 fm  OUTSIDE the frame;  one line g_A = 1.5031 (+17.9%)
  a = (2/3) alpha_geom  (0.298)  pass-through, 4 falls/period     amplitude 0.471 fm  inside the frame;  one line g_A = 1.4335 (+12.4%)
  a = alpha_geom        (0.447)  reset, 2 falls/period (4243 C)   amplitude 0.871 fm  OUTSIDE the frame;  one line g_A = 1.4648 (+14.9%)
  a = alpha_geom        (0.447)  pass-through, 4 falls/period     amplitude 0.523 fm  inside the frame;  one line g_A = 1.3833 ( +8.5%)
  a = (4/3) alpha_geom  (0.596)  reset, 2 falls/period (4243 C)   amplitude 0.941 fm  OUTSIDE the frame;  one line g_A = 1.4335 (+12.4%)
  a = (4/3) alpha_geom  (0.596)  pass-through, 4 falls/period     amplitude 0.561 fm  inside the frame;  one line g_A = 1.3433 ( +5.3%)

-> Pass-through halves the fall time at a fixed period, so the amplitude shrinks to ~0.6 of its value (2^(-2/3) non-relativistically): the
   classical breath now fits inside the frame (0.47-0.56 fm), removing the reason 4243 rejected route (C), and
   its one-line g_A drops to 1.34-1.43.
```

## 4. Blast radius (searched: whole tree, `.md`/`.tex`/`.py`)

These are the sites that state or depend on stop-and-turnaround at superposition:

| Site | What it uses | Effect of adopting pass-through |
|---|---|---|
| `founders_voice/founder_ruling_radial_arc_cancel_2026-08-14.md` §3 (3134) | R-ARC-CANCEL-TURNAROUND itself | superseded (banner, verbatim kept) |
| c04 (`c04_ZBW_hbar_mass_units.tex`) v2.1 scope banner | carrier = arc store cancelled at co-location | banner rewritten; **mathematics untouched** (standing wave) |
| F-SW-10 audits 3140, 3201, 3203 | swept prose against 3134 §3 | re-sweep against the new ruling |
| sea-gravitation lane: R-DWELL-1 in `sigma_n_derivation.md`, `darcforce_*`, `selfconsist_*`, scripts 3078–3131 | one-Moment dwell + relaunch amplitude (σ_n) | dwell survives as co-location; the relaunch term becomes carried-through momentum; σ_n decomposition re-derived |
| `subpsr_pass2_radial_resolution.md`, OS WORKFLOW | cite 3134 | re-cite |
| EW 4231 / 4232 (reset mechanism: binding decided at the reset Moment; W⁰ release as a reset in the pocket) | reset at the core and in the W⁰ centroid | restated as transit. The founder's 4240 ruling already has the eCP pass the W⁰ centroid **by inertia** — the release mechanism was already half pass-through |
| 4243 route (C) | fall-reset-return | re-run here (above) |
| DM `2454_zbw_dance.py`, 2455, conv001 Floquet brief | turnaround in the ZBW dance | re-check whether ring survival used the stop |
| QM-1, QM-2, QM-6, SPIN-1, GR-1j (`.tex`) | contain "reset/turnaround/dwell" wording | read on sweep; may be unrelated uses |

This is roughly 25 files. The load-bearing ones are c04's banner, the R-DWELL-1 σ_n derivation, and EW 4231–4232. In
every case the dwell survives. What changes is whether momentum survives it.

## 5. PD-008

The convenient branch for this arc is to adopt pass-through: it keeps every g_A number and rescues route (C). I have
marked that. The recommendation rests on (i) and (ii), energy conservation and 3134's own logic applied to an
asymmetric pair, not on the g_A convenience. Adoption is an axiom-level change (ZBW cycle), so it is the founder's
ruling. On his ruling, the sweep in §4 runs as a filed campaign.
