# The edge-bond SSV make-or-break — a scoping / handoff specification

**Status:** SCOPING ONLY — no fabrication, no new number. This document poses the one open calculation that
would convert the Cross-Rod dark-matter candidate from *viable and corona-safe* into a *discriminating
prediction*. It is the registered SF-2/SF-5 make-or-break (0862–0865), here specified precisely so it is
well-posed for whenever it is attempted. **Lane:** SF-2 (electroweak) / SF-5 (strong), cross-window with the
DM lane. **Author:** Opus (DM 08xx), 28 June 2026. No registry IDs minted here (a scoping doc); it points to
the existing make-or-break and to OPEN-FP-SF-2-η.

---

## 1. The calculation, in one line

Derive, from the SF-2/SF-5 substrate primitives, the **edge-bond SSV potential** — the depth of the
2eDP:2qDP / hTetra edge bond that holds the Cross-Rod together. The depth that governs breakage, length
kinetics, and lifetime is specifically **E_ee** (the weaker *scission* bond; it breaks in ZBW State 2), with
**E_qq the stiffer partner** (it pairs with the G1 angular spring). The ledger's "E_bond" ≡ **E_ee**. So the
deliverable is one number with a sign-fixed companion: **E_ee (= E_bond), with E_qq > E_ee.**

## 2. The target window (four constraints, over-determined)

The DM campaign has reduced this make-or-break from an open-ended derivation to a **narrow, falsifiable
window**. The SF edge-bond SSV must land E_bond such that *all four* hold simultaneously:

| Constraint | Requirement | Source |
|---|---|---|
| **Fragmentation (velocity trend)** | E_bond ∈ **[0.8 keV, 2 MeV]** (≈0.78 keV deposited at dwarf v=30 km/s, ≈1.95 MeV at cluster v=1500 km/s → fragments in clusters, intact in dwarfs: the data-preferred rising trend) | 0860 |
| **Freeze-out / band size** | **E_bond / kT_form ~ 24–41** (from N_freeze ~ √φ · exp(E_bond/2kT_form), inverted for the band-N ~ tens of cube-elements) | 0881 |
| **14-Gyr lifetime** | **E_bond ≳ 100 kT_present** (Arrhenius; any-of-N rung breaking fragments the rod) | 0860 |
| **Two-temperature consistency** | **kT_form / kT_present ≳ 7** (formation bath a few× hotter than today — trivially satisfied by cosmological cooling) | 0861 |

These overlap on a single point **iff the ambient thermal-eDP scale kT_present ≲ ~19 keV** — itself a
falsifiable substrate-thermal hook (0860). The four constraints close on one (N, E_bond, kT_form) *if* the
substrate edge-bond SSV actually sits in the window; whether it does is exactly what the SF calculation decides.

## 3. Why it is hard (and why it was not fabricated)

The **absolute** edge-bond depth is a **sub-Planck near-cancellation SSV charge-sum** — a tiny residual of a
large cancellation between the edge's competing charge contributions. Worse, there is **no pinned
first-principles inter-CP binding potential to plug in** (0865): SF-2's cage masses are *calibrated* (partial
closure via the per-boson holographic dilution factor η ~ 10⁻¹⁷, registered **OPEN-FP-SF-2-η**), not derived
from a potential with a fixed coupling. So a real E_bond requires either (a) the substrate-derived
edge-bond SSV potential (the deep route), or (b) at minimum a pinned coupling for the near-cancellation sum.
0865 declined to fabricate a coupling to manufacture the number, and that discipline is preserved here.

## 4. The dependency chain

```
E_bond (= E_ee)
  └── edge-bond SSV potential  (the near-cancellation charge-sum; UNBUILT — the make-or-break)
        ├── SF-2 cage masses / couplings  ──► calibrated via η ~ 10⁻¹⁷  ──► OPEN-FP-SF-2-η  (open at SF-2 v1.0)
        └── SF-5 strong-sector edge couplings (E_qDP = 264 MeV scale; the qq partner)
```
The root blocker is **OPEN-FP-SF-2-η** (problem history `problem_histories/PH-OPEN-FP-SF-2-eta.md`): until the
cage-stability dilution is substrate-derived rather than calibrated, the absolute SSV charge-sum has no fixed
coupling. A shared substrate-thermodynamic closure path is already conjectured for OPEN-FP-SF-2-η (FP.md);
the edge-bond depth likely rides the same closure.

## 5. What is robust *despite* the near-cancellation (already banked)

Not everything waits on the absolute number. These hold regardless of where in the window the depth lands
(0865), and are the campaign's standing contribution to the make-or-break:
- **Ordering:** E_qq > E_ee (a sign result from the screening configuration, not a magnitude).
- **E_bond ≡ E_ee:** the scission bond is the one the fragmentation/lifetime arms act on.
- **In-window reachability:** the fm-scale Coulomb ceiling (1.44 MeV) sits at the *top* of the fragmentation
  window, so a natural screening residual lands in-window without tuning.
- **Lifetime floor shares the kT hook** with the freeze-out relation (one E_bond, two arms pulling oppositely).

## 6. The payoff (why it is worth the climb)

Pinning E_bond (or, equivalently, kT_form via the relic/epoch calc — itself open, downstream of the
un-derived abundance OPEN-COSMO-DM-1/DM-2) collapses N_freeze = N_dwarf to a **single value**, which turns the
band-*reachability* (σ/m = 0.11·N, N = cube-elements) into a **hard core-size-vs-halo-mass curve** —
distinguishable from CDM (σ/m = 0) and from the velocity-*independent* monomer (0.11–0.20). That curve is the
**discriminating positive signal** that would move CONJ-COSMO-1 off NOT-confirmed and could earn a swarm entry.

## 7. The falsifiable contract (pre-registered)

This is the make-or-break in the literal sense: **if the SF-2/SF-5 edge-bond SSV returns E_bond outside
[0.8 keV, 2 MeV], or a ratio E_bond/kT_form far from 24–41 with kT_present ≳ 19 keV, the Cross-Rod
dark-matter candidate fails** (the rod is either too fragile to survive 14 Gyr, or too stiff to fragment at
cluster velocities, or freezes out at the wrong size). The candidate has been built so that this single SF
output can kill it. That is the strength of the position, not a weakness.

## 8. Disposition

The DM lane has done everything it can without the SF input: morphology selected, width/length mechanisms
closed, corona retired unconditionally (OPEN-COSMO-DM-3, panel-ratified), element-level normalization verified
(0886). The remaining step is **not DM-local** — it is the SF-2/SF-5 edge-bond SSV calculation, blocked at root
on OPEN-FP-SF-2-η. This document is the handoff. When the SF lane (or a dedicated cross-lane arc) takes it up,
the target window above is the specification; a return inside the window is the discriminating prediction, a
return outside it is the falsification.
