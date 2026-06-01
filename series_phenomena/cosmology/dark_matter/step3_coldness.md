# DM Arc — Step 3: Coldness

**Patch:** 0706 (Session 149, 31 May 2026) · **Work item:** OPEN-COSMO-DM-1 Step 3 · **Gate:** coldness
**Status of result:** order-of-magnitude — **SURVIVES (cold by a wide margin).** The last cheap self-contained gate; does not depend on OPEN-SR-5.
**Verify:** `scripts/0706_coldness.py`

---

## 1. What Step 3 tests

Warm/hot dark matter free-streams out of small-scale perturbations and suppresses structure below its free-streaming length. Thermal-relic DM lighter than ~3 keV is excluded (Lyman-α forest, satellite-galaxy counts). For CONJ-COSMO-1 to hold, the free qDP/hTetra must be **cold** — non-relativistic early enough that their velocity dispersion is negligible by the onset of structure growth (matter-radiation equality, z ≈ 3400).

## 2. The decisive number

The qDP/hTetra masses (≈0.3–1.5 GeV, from the Step-1 confinement-scale estimate) sit **~10⁵–10⁶× above the ~3 keV warm-DM boundary**. Mass alone settles it: anything this heavy is deep CDM, far from the warm regime occupied by keV-scale candidates (e.g. sterile neutrinos).

The velocity dispersion confirms it (`scripts/0706_coldness.py`): both species are relativistic only in the early hot universe and go non-relativistic at T ~ m in the **QCD era** (~microseconds). By matter-radiation equality the rms speed is v/c ≈ 9×10⁻⁵ (qDP) and ≈4×10⁻⁵ (hTetra), falling further by recombination. The free-streaming length is therefore orders of magnitude below the ~keV-WDM suppression scale, so small-scale structure is untouched. (The early-universe "relativistic" tags in the script are expected and irrelevant — coldness is required at structure formation, not at the QCD era.)

## 3. Verdict

**Cold, decisively.** No kill. This is the cleanest of the three gates: it rests only on the GeV mass scale, not on any cosmological-sector assumption.

## 4. Honest caveat (does not change the verdict)

The estimate assumes the free qDP/hTetra kinetic temperature **redshifts like a decoupled species** rather than being pinned to an ongoing-hot Sea thermal bath. §6c supports the cooling picture: the hTetra freeze-out is a cosmological phase transition, and at STP thermal collisions only *degrade* bonding rather than dominate — i.e. the Sea cooled. A rigorous late-time Sea temperature ultimately ties to OPEN-SR-5, but coldness does **not** depend on it critically: the GeV mass scale secures coldness under any standard cooling history. One conceptual note: chemical freeze-out (when hTetras stop forming) is distinct from kinetic decoupling (what sets the velocity dispersion); coldness rides on the latter.

## 5. Arc status after Step 3

All three falsification gates that can be run **without** the cosmological sector are now computed, and none kills the model:

| Gate | Result |
|---|---|
| Step 1 — σ/m vs SIDM | survives, ~250–1250× below bound |
| Step 2 — free vs baryon-bound | no kill; ~5:1 underived (R1), Sea-gravitation requirement (R2) |
| Step 3 — coldness | survives, ~10⁵–10⁶× above warm bound |

The remaining steps are **gated on OPEN-SR-5** (the scoped cosmological sector): Step 4 (power spectrum from swirl seeds) needs the expansion dynamics; Step 5 (quantitative halo / rotation curve) needs the Sea-gravitation force law at cosmological scales. Neither can proceed honestly until OPEN-SR-5 delivers (i)–(iii) from `R2_sea_gravitation_scoping.md`.

**Recommendation:** this is the natural pause point for the DM arc. It has done everything achievable without the cosmological sector — two potential kills survived, one gate scoped into two named requirements, the dark-energy↔dark-matter unification ceiling identified, and the single load-bearing prerequisite (OPEN-SR-5) elevated and cross-linked. The honest next move is a **new arc** for the OPEN-SR-5 cosmological sector (its own handover), not more DM-side estimation. The DM arc stands clean and handover-ready here.
