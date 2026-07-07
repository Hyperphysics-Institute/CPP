# G4 · Stage-3 opening move — the transport reduction: the gate becomes one number (Patch 2327, 7 July 2026)

**What this patch is:** the 2326 handover's "cheap first move" (the Ohmic-excess bound at the LSB
frequency), executed as a structural reduction rather than a numerical shortcut. **Verify:**
`code/2327_g4_stage3_transport_reduction.py` (8/8). **No resting paper touched. No verdict moved:
G4 stays UNRESOLVED-QUANTIFIED** — but the residue changes identity: from an unknown *function*
S(k ~ 1/R_s, ω) to **one derivable transport number, with a two-sided survive window pre-registered
before the number is computed.**

## 1. The move (condition C-h)

Under condition C-g the spectrum entering the loss formula is **by definition the dynamic structure
factor of the occupancy field** — the Rayleigh coupling is defined through occupancy-fluctuation
cells (δ² = f_occ(1−f_occ)). Three registered facts then fix its frequency structure at k = 1/R_s:

- **(C-h-1) Occupancy is a conserved density at encounter frequencies.** CPs are ontological
  primitives (A1) with no registered creation/annihilation process, and every Sea creation channel
  is gapped ≥ 0.9 MeV (e-channel; 2311 inventory) — ħω_enc(LSB) = 4.25 keV sits ×212 below. The
  *configuration* regenerates every Moment (the founder's 2320 ruling — that fast local channel is
  the bare Ohmic tail, ωτ_b = 2.2×10⁻⁵ at LSB, and it stays); the *occupancy* can only relax by
  transport.
- **(C-h-2) Transport at the 25-fm scale is diffusive.** Portrait carrier mfp
  ℓ_cp = 1/(nσ) = 3.18 fm (n = f_occ/ℓ³, σ = πr_c²) gives kℓ_cp = 0.125 ≪ 1 — the hydrodynamic
  closure is forced by the portrait, not chosen. Ioffe–Regel outer bound: mfp ≥ ℓ = 1 fm.
- **(C-h-3) Normal diffusion** (no heavy-tailed waiting times). Named as a condition; see §6.

Then the correlation time at k = 1/R_s is the **transport time τ_k = 1/(Dk²)**, not τ_b, and the
2321 golden-rule construction gives the normalized dissipative factor

  **Θ(ω) = 2ωτ_k / (1 + (ωτ_k)²)** — the same construction as 2321's Ohmic-fast bound, which is
  its x ≪ 1 limit with τ_k → τ_b (order-unity factor 2 at that limit, disclosed).

**The whole gate is now the single number D** — the Sea occupancy diffusivity at the R_s scale.

## 2. The registered-kinetics cap, and the cheap-kill criterion evaluated

If Sea DP centers move at light speed between collisions (D = cℓ_cp/3), the diffusive knee lands at
ħ/τ_k = 324 keV (portrait) or 102 keV (Ioffe–Regel outer bound), giving

  **Θ(4.25 keV) = 0.026 (portrait) / 0.083 (outer bound) — below the survive bar 0.66 by ×25 / ×8.**

**Light-speed occupancy kinetics is on the kill side.** But the handover's pre-registered cheap-kill
criterion ("cannot exceed the Ohmic tail by ≳10³ at keV → KILL") **does not fire**: the conserved
channel exceeds bare Ohmic by ×1.2×10³–3.9×10³ — above the line. The honest reading: the bound
neither kills nor saves; the gap between achievable-at-light-speed (0.026–0.083) and required
(0.66) is decided by D, and D is a portrait quantity that has never been computed.

## 3. PRW-D — the pre-registered survive window

Θ(4.25 keV) ≥ 0.66 (the 2324 LSB bar, easy-coat end) iff ωτ_k ∈ [0.376, 2.66]:

| Form | Survive window |
|---|---|
| diffusive knee ħ/τ_k(R_s) | **1.60 – 11.3 keV** |
| diffusivity D | **5.2×10⁻³ – 3.7×10⁻² c·fm** (width ×7.1) |
| drift speed at portrait mfp | **1.5×10³ – 1.0×10⁴ km/s** (0.005c – 0.035c) |

E_coat ≥ 0.40 MeV rides along (2324). Light-speed kinetics overshoots the window top by ×29
(portrait mfp) / ×9 (outer bound): **survival requires Sea DP centers that are nearly
lattice-resident, drifting at percent-of-c speeds** — slow residual center-of-mass kinetics under
fast internal (ZBW) configuration dynamics.

**Inside the window the full published suite holds simultaneously and zero-refit:** at both window
edges the dwarf bar clears ×308+ (P > 0.99) and the pin bar ×12+, while the LSB holds by
construction — the rising Lorentzian supplies exactly the steep effective spectrum (s → 2-class
between pin and LSB) that 2324 showed a flat spectrum cannot. **A consistent resting point exists
where none did before.**

**Outside the window, on both sides, the outcome is uniform:** dwarf-pass + LSB-floor (×15 under
its window) — precisely the pattern 2324 proved is **excluded by the existing LSB anchor**. Above:
from the window top through light-speed kinetics. Below: for ≥ 7 decades of D (dwarf capture stays
alive down to knee ~ 0.1 neV). **Outside PRW-D, G4 resolves KILL-on-suite;** the elastic floor,
cluster/Bullet safety, and the F1 group falsifier are invariant throughout (2324).

## 4. What Stage-3 now is

Not "compute S(k,ω)" — **derive D**: the mean residual displacement per Moment of a quiescent Sea
DP center under the registered PCD rules (near-field SSV gradients, ZBW internal cycle, transiting
CPs), coarse-grained to the 25-fm scale. One number, from registered dynamics, against a window
registered here first. Forward-map note: at portrait mfp, D maps to drift kinetics
v = √(2T_amb/m_DP)-class, so PRW-D becomes a joint constraint with SI-1's U6 (T_amb) and U2 (E_z)
once the Sea DP inertial mass is pinned — flagged for Stage-3, not exploited here. New SI-1 unknown
**U7 (D_occ)** registered with PRW-D as its forward map.

## 5. Release input (20 July) — sharpened again, still no recommendation

The open condition is unchanged in status (G4 unresolved → founder decides) but changes character:
from "does the bath carry near-ceiling sub-cone weight" to "**does the Sea's occupancy diffusivity
fall in a factor-7 window that light-speed kinetics misses by ×9–29**." Both readings are honest;
the second names the ontological content: the candidate survives only if Sea DPs are slow-drifting
lattice residents. The founder's own picture bears on this and the derivation will decide it.

## 6. Caveats (named)

1. **C-h-3 (normal diffusion):** subdiffusive/glassy occupancy kinetics (trapping, heavy-tailed
   waiting times) would deform Θ(ω) and shift PRW-D. No registered generator supplies it; the PCD
   rules are homogeneous-lattice rules; but it is a closure, not a theorem. Stage-3's derivation of
   D from the PCD rules resolves it in passing (the same computation exposes anomalous kinetics if
   present).
2. **Ballistic variant:** if the true carrier mfp exceeds R_s (portrait says 3.18 fm — it does
   not), the box spectrum replaces the Lorentzian and the window re-forms around kv_drift ≈ ω
   (v_drift ~ 160 km/s-class). Same reduction, different window; the portrait pins the diffusive
   form.
3. **Normalization:** Θ ceiling 1 per the 2321 band construction; factor-2 convention at the Ohmic
   limit disclosed in §1.
4. **The 2324 caveats inherit** (flat-w slice geometry, band-edge robustness 0.81–0.94).
