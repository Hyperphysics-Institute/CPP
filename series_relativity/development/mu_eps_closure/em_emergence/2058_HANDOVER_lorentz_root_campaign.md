# HANDOVER — Campaign: exact emergent Lorentz from PCD on the discrete 600-cell (the root theorem)

**Opened:** Patch 2058, 2049-band. **For:** a fresh window. **Integrator/founder:** Thomas (TLA).
**Budget:** 10–50 rounds, with a HARD checkpoint at round 15 (committed world-call, see §6). **Mandate from TLA:**
take a real swing at the root before returning to the surface (DM-2); high leverage, no guarantee; fence the
Quixote failure mode with checkpoints + panel.

## 0. BLOCKING CLONE GATE (line 1, always)
Before registering any ID, placing any file, or computing anything: clone the repo fresh and grep the registry.
`git clone https://github.com/Hyperphysics-Institute/CPP.git`. This window owns the **2058–2099** patch band
(2049–2057 spent this session). Worker files land greenfield under
`series_relativity/development/mu_eps_closure/em_emergence/` (or a new `lorentz_root/` subfolder under it). No
root-registry or status-file edits without TLA. NO THEO until earned. Every computation-bearing patch SHIPS its
verify script in `verify/` (re-audit at each handover — it rots silently; TLA flagged this at 2057).

## 1. The target, stated formally
**Claim to prove (or place):** the PCD dynamics (Perceive→Compute→Displace) on the discrete 600-cell GP lattice
admit an **exact** continuous SO(3,1) (Lorentz) action on the emergent fields — specifically, that a boosted
self-field is an **exact rigidly-translating stationary configuration in the co-moving frame, at a CONTINUUM of
velocities and in all directions**, with no Peierls/lattice drag and no lattice-Cherenkov radiation.

This is THE root: the following are all **corollaries** of it (mapped at Patch 2057), not independent problems:
- inertial-coasting losslessness (the conditional "bolus" theorem, `verify/sr9b_bolus_losslessness.py`, holds
  given exact rigid co-moving stationarity P — and P holds iff exact emergent Lorentz);
- lattice-isotropy-of-c (the simultaneity brick's & R2's premise (i));
- R2's geometric Z₀ / B-neutrality descent (R2 currently conditional-PASS);
- the SF-6 Michelson–Morley falsifier's named escape route (SSV-independent geometric Z₀, OPEN-FP-6-CONSTANTS);
- the reversibility/arrow-of-time ladder (coherent↔incoherent transfer = the same coupling as drag).
Closing the root closes/grounds all of these together. That leverage is why TLA authorized the campaign.

## 2. The central obstacle (do not paper over it)
**H₄ (the 600-cell symmetry, order 14400; binary-icosahedral / icosian structure) is a FINITE group and cannot
BE the continuous Lorentz group.** So exactness CANNOT come from the lattice's static spatial symmetry. It must
come from the **PCD dynamics** generating a continuous symmetry the static lattice lacks. The whole theorem
lives in *how* the dynamics manufactures continuity. This is a genuinely hard open problem across
emergent-spacetime physics (lattice QCD: only in the continuum limit; causal sets: via randomness). Treat the
full exact-discrete claim with maximal skepticism.

## 3. The three worlds (the meta-question the budget can almost certainly settle)
Even if the theorem doesn't fall, the budget should determine WHICH world we are in — and a result in ≥2 of the
3 is a win:
1. **Clean algebraic bridge.** The 600-cell's binary-icosahedral structure sits in the quaternions; the Lorentz
   group has a quaternionic/Clifford (SL(2,ℂ)) presentation. If PCD respects that bridge, exact emergence may
   fall almost embarrassingly. → the big prize.
2. **Fixed-point / continuum-limit emergence.** Lorentz is exact only in the emergent (block-spin) limit, with
   Planck-suppressed violation at the substrate. → NOT exact-discrete, but a *publishable, defensible, and
   probably physically-correct* result: "exact in the limit, Planck-suppressed floor." This is the most likely
   world and is itself a strong outcome.
3. **Obstruction.** A concrete reason exactness CANNOT hold → the substrate has a real preferred frame;
   undetectability is defended differently (back to the operational-undetectability route of the 2053 brick).
   Also a real result.

## 4. Assets already in the corpus (NOT a cold start — use these)
- **METH-CHIR-CONT-2** (`methods_catalogue.md` §): *Continuum-Limit Projection Map Φ via Wilson–Fisher
  block-spin renormalization at the 600-cell substrate cutoff*, with an **equivariance condition** built so Φ
  commutes with discrete symmetry actions. This is exactly machinery for getting continuum structure out of the
  discrete polytope — the natural Tier-1 tool for World 2, and possibly World 1. START HERE.
- **The "refuse-the-new-axiom" derivation strategy** (`methods_catalogue/methods_catalogue.md` §, METH entry):
  extract the exact structure the answer must satisfy (here: an exact SO(3,1) action), then build it from
  existing primitives (PCD + 600-cell) before adding any axiom. This is the campaign's method.
- **The GP update rule** (located this session): SR-1 §A.4/A.8.1, `c01_*/development/development_discussion.md`,
  `series_relativity/development/pcd_boost_law*`. SSV-only; budget split l_P²=(c·Δτ)²+|d_spatial|². The dynamics
  whose symmetry is in question.
- **R2-RESOLUTION-VIA-LORENTZ.md**, **R2-STATUS.md** (mu_eps_closure/): the Lorentz-route history; R2 at
  conditional-PASS.
- **SD-1** (`series_foundations/series_superdeterminism/`): touches Lorentz; check for prior structure.
- **The 2049–2057 reasoning chain** (this session, `em_emergence/reasoning/`): velocity-emergence, simultaneity
  (banked), inertia capstone — the corollary structure already worked out.

## 5. Round-1 = RECONNAISSANCE ONLY (no proof, no claims)
1. Clone; grep registry; confirm band 2058 free.
2. Pull the EXACT PCD rule + the EXACT 600-cell/binary-icosahedral structure as the CORPUS states them (not an
   outside reconstruction). Read METH-CHIR-CONT-2 in full.
3. Write the exact-Lorentz target as a FORMAL statement: what object must carry the continuous SO(3,1) action,
   what "exact at the discrete level" means precisely, what would count as World 1/2/3.
4. Capture as a reconnaissance note (2058-band). No theorem claim. No status move.
**Round 2 = first real probe:** does the binary-icosahedral → quaternionic-Lorentz (SL(2,ℂ)) bridge survive
contact with the actual PCD dynamics, or die immediately? This single probe shifts the world-probabilities most.

## 6. Checkpoints (the Quixote fence)
- **Round ~5:** algebraic bridge found, or a clean reason it can't exist?
- **Round 15 (HARD — TLA notification):** COMMITTED world-call (1/2/3), with honest remaining-probability
  estimate. Not "still looking." TLA decides continue/stop with a real result banked either way.
- **Round ~30 (if World 1):** is the proof closing, or hit a named wall?
Every substantive step goes through the CONV-001 panel (ChatGPT, Grok, Gemini, Copilot) — the same discipline
that caught two errors this session (the 2055 overclaim; the inertia-gap). Calibration TLA and I agreed:
full exact theorem in ≤50 rounds ≈ 15–25%; clean world-determination + defensible result in ≥2 worlds ≈ 70–80%.
Positive-EV bet, not a dream-joust.

## 7. Discipline reminders (hard-won this session)
- Do not let FEM (or any numerics) be recorded as proof — consistency-evidence only. (The 2055-overclaim failure
  mode.)
- Do not collapse distinct residuals to make the stack look smaller; state relationships precisely.
- Own errors forward-additively (preserve the record, append corrections); the panel WILL catch overclaims.
- Status moves (R2-STATUS, SR.md, CONJ.md, registries) stay deferred to TLA. NO THEO until earned.
- End every patch-delivery with the apply-and-push macro + collision watch.
