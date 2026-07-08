# L1 first patch: the internal spectrum, mostly closed — one soft door left open by design (Patch 2340)

**Verify:** `code/2340_l1_internal_mode_thresholds.py` (6/6). Lane: OPEN-DM-DSPH-1 / L1.

The pinned rod's rigid and elastic internal spectrum cannot supply the SPEC-1 feature at
registered N: rigid-rotor J=0→1 sits at 48 keV (cusp velocity 827 km/s) at N = 18, with
window placement requiring N ∈ [72, 92] — excluded ×4 by the cluster-side bound and the
1859 pruning (both flagged: they predate the 2337 floor correction; L4-a recompute is the
registered reopening condition). Longitudinal phonons: ~1 MeV quanta. Bending: ~121 keV,
window at N ~ 190. All CLOSED-conditional.

**The surviving door, with its number:** the azimuthal/torsional sector. Nearest-neighbor
radial coat springs give no leading-order torsional resistance, and the cross-arm coat's
azimuthal stiffness is underived. An in-window torsional quantum at N = 18 requires
**κ ≈ 1×10⁻⁷ MeV (0.10 eV)** — six orders below the elastic coat scale. That is the
L1→L2/L3 handoff: derive κ_torsion from the coat structure; the lane lives iff it lands
within about an order of that number, and dies cleanly otherwise. **Rent template
registered:** any in-window internal mode is thermally live at z ~ 3×10⁵–3×10⁶
(T ≳ 100 eV), with pre-registerable relic-distribution consequences *before* any dwarf
evaluation. No SPEC-1 mechanism is claimed by this patch.
