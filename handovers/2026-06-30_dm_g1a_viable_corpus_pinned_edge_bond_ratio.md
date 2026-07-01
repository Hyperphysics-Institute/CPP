# HANDOVER — DM: G1a is DELIVERED — the edge-bond scissor/bend ratio g is VIABLE, direction corpus-pinned; panel round 2 can proceed
**Date:** 2026-06-30 · **Lane:** DM 18xx (cosmology / dark-matter) · **From:** Opus (SF-2/SF-5 session, patches 2200–2202) · **Consumer:** DM-1
**Answers (does NOT supersede):** `handovers/2026-06-30_sf2_sf5_edge_bond_ssv_ratio_sharpened.md` — the DM→SF ask that requested G1a first. This file returns G1a and hands the number back across the lane boundary.

---

## ⛔ LINE 1 — BLOCKING CLONE GATE (do this before anything else)
```
cd ~/Documents/GitHub/CPP && git pull --rebase origin main && git log --oneline -8
```
Confirm origin/main HEAD includes the SF G1a arc **2200 → 2201 → 2202** and the new **OPEN-SS-40** in `frontier_sectors/SS.md`. Do NOT register an ID, place a file, or compute anything before cloning and grepping the registry. **This is a cross-window handover: the work it asks for is DM 18xx lane, NOT SF.** G1a is now an SF-owned, registered result (OPEN-SS-40) — **do not re-register it, do not edit it as DM**; consume it. Pick your own next free DM patch number (18xx) for the DM-side consumption; grep before reserving.

---

## Orientation — read this first
The held item is unblocked. SF was asked for G1a — the scale-free ratio g = κ_scissor/κ_bend that decides the DM cluster floor — and **G1a comes back VIABLE, with the verdict *direction* now corpus-pinned** (not merely estimated). The scissor is the soft mode; the X-junction hinges freely; the cluster floor lands in the allowed band. Two honesty flags travel with it: (1) the *direction* (viable) is pinned, but the *exact* floor (comfortably-viable ~0.4 vs marginal ~0.8) is **not** — it needs the ZBW amplitude, which roots on OPEN-FP-SF-2-η; (2) the original DM estimate g ~ 0.1 had the right *direction* but the wrong *provenance* (see below), and the corrected ratio is actually *more* comfortably viable. **DM action:** run the cluster-floor verdict consuming g, update the mechanism note / DM-1 disposition to "floor viable (direction robust), exact value pending," and run the held **panel round 2** with this verdict — but do **not** promote DM-1 off Layer-C on the floor alone, because the floor *magnitude* and the formation-side numbers (G1b/G2/G3) are still open.

---

## WHAT SF DELIVERED (the number + the full verdict)

**G1a: g = κ_scissor/κ_bend is VIABLE (g ≪ g_crit = 6/N ≈ 0.43 at N≈14), direction corpus-pinned.** The arc took three patches, and the middle one matters for how you read the result:

- **2200 (static ratio) — a transient SCARE, now superseded.** Evaluating g from the *static* curvature (V″) of the same edge-bond potential in the two geometries gave **g ≈ 1.6–3.8, ABOVE g_crit → tense**, reversing the g ~ 0.1 estimate. This was correct *given the static operator* — but the static operator is wrong here (next bullet). **If you saw only 2200, disregard its verdict; it is superseded by 2201/2202.**
- **2201 (ponderomotive ratio) — the CORRECT operator, viable.** 1834 already showed the static edge-bond config is Earnshaw-unstable — so the bond is held *dynamically* by the qCP ZBW jitter (Kapitza/ponderomotive). The correct stiffness is the curvature of the **squared field |E|²**, not V″. On that operator: (i) Earnshaw is genuinely resolved (q=0 is a true |E|² minimum for both modes — both restoring); (ii) per-core **g_pond ≈ 0.02 < g_crit → VIABLE** in the steep/screened regime. This is the calc 1835 named "the full ponderomotive κ_θ, mine to run."
- **2202 (corpus close) — the viability CONDITION is met, not assumed.** 2201 left a "softer-SSV-law" escape hatch (a shallow/long field would go tense). That hatch is **closed by electrostatics**: the edge bond is a *localized electrostatic near-cancellation residual*, whose field cannot be sub-Coulomb (monopole 1/r² is the shallowest possible; a near-cancellation residual is dipole-like, 1/r³ or steeper), reinforced by the derived fm-scale screening (r_c ≈ 1.0 fm eDP coat; λ ≈ 1.3 fm confinement). g_pond at every corpus-physical leg = 0.000–0.025, a **~17× margin** under g_crit. Tense only in an unphysical flat-field (s→0) limit.

**On the g ~ 0.1 estimate you sent up:** its *direction* (soft scissor) was right, but its *provenance* was the wrong reference — the founder's 1835 softness read compared the scissor to the E_qq *core* (~66 MeV), whereas the floor-relevant denominator is the E_ee in-line *bend* (same perimeter shell as the scissor). The E_qq/E_ee hierarchy cancels in the true ratio, leaving a pure geometry ratio (~0.02) that is *more* comfortably viable than 0.1. So the DM floor is viable for a **sounder** reason than the estimate had.

**Bonus consistency result (carry this to the panel).** The stiff-ribbon requirement (σ/m ∝ N needs large κ_bend / ℓ_p ~ 100–700 fm; 0862 derives the hinge stiff) and the soft-scissor floor are **not** in tension: g is a *ratio*, so a large κ_bend is the denominator that makes g small — the two DM requirements reinforce. And g ≈ 0.02 with κ_bend *large* means κ_scissor is sizable in absolute terms (~1/50 of a stiff bend): the junction is the **softer of two stiff modes, not a fragile joint.** This preempts the natural panel worry that "flexible X-junction" smuggles in "fragile candidate."

---

## WHAT DM SHOULD DO NOW (consumption — this is your lane)
1. **Cluster-floor verdict:** plug g (viable, g ≪ 0.43, direction robust) into the per-fusion drop → cluster-floor computation. Expect the floor to land in the allowed band. **Report it as "viable, direction robust; exact floor (0.4 vs 0.8) pending the ZBW amplitude" — do NOT quote a single sharp floor number as pinned.**
2. **Update the disposition surfaces:** `DM-1/documentation_suite/mechanism-strip-then-fuse-DM-1.md` STATUS/Disposition, and the DM-1 §5 re-scope line, from "viable-pending-g" to "floor viable (direction corpus-pinned), exact value pending OPEN-FP-SF-2-η."
3. **Run panel round 2** (which was held for g) with this verdict — including the stiff-vs-soft consistency result, which is the strongest new argument in the packet.
4. **Do NOT promote DM-1 off Layer-C on the floor alone.** The floor is one of three make-or-break quantities; G1b (ℓ_p formation side), G2 (E_qq/E_ee → fragmentation), and G3 (glueball-arrest, OPEN-SS-39) are still open, and the floor *magnitude* itself is not pinned.

---

## CROSS-LANE ROUTE — a partial G1b you can close on the DM side (no OPEN-FP-SF-2-η needed)
SF cannot pin the *absolute* κ_θ (G1b) without the absolute edge-bond potential (OPEN-FP-SF-2-η). But **you already have the piece that closes it**: 0861 pins **ℓ_p ∈ [105, 702] fm**, which via the worm-like-chain relation B = κ_bend·ℓ_rung and ℓ_p = B/k_BT_form **is an absolute κ_bend**. Combined with SF's ratio **g = κ_scissor/κ_bend ≈ 0.02**, that backs out an **absolute κ_scissor ≈ g·κ_bend** — i.e. a partial G1b — *without* waiting on the FP root-blocker. This is a legitimate DM-side move because ℓ_p is a DM-derived number; SF flagged it rather than doing it (pulling ℓ_p into SF would invert the lane boundary). Caveat to handle carefully: it needs ℓ_rung and the T_form (or k_BT_form) normalization consistent with 0861's WLC assumptions — check those match before quoting an absolute κ_scissor.

---

## LANE BOUNDARY (unchanged — do not cross back)
- **SF delivered (done):** the edge-bond scissor/bend ratio **g** (viable, corpus-pinned), the ponderomotive operator, the screening/electrostatics close, the stiff-ribbon consistency. Registered in **OPEN-SS-40** + reasoning/code 2200–2202. **SF still owes (blocked):** the *absolute* κ_θ (G1b) and E_qq/E_ee depths (G2) — both need the absolute potential (OPEN-FP-SF-2-η); the exact floor magnitude needs the ZBW amplitude (same root).
- **DM consumes (this handover's asks):** floor verdict, disposition updates, panel round 2, and the ℓ_p×g cross-lane κ_scissor. **Do not** edit OPEN-SS-40 or the SF reasoning fragments; if a DM consumption reveals an SF error, write it up DM-side and flag it back — don't rewrite the SF result in place.

---

## WHAT'S STILL BLOCKED, AND ON WHOM
- **Exact floor magnitude (0.4 vs 0.8), absolute κ_θ (G1b), E_qq/E_ee (G2)** → all root on **OPEN-FP-SF-2-η** (the substrate-thermodynamic framework: ZBW amplitude/frequency + the absolute SSV potential at sub-Planck pre-tension). This is an **FP-lane / founder** item, not movable by in-lane geometry. The ℓ_p×g route above is the one partial exception (DM-side).
- **G3 (glueball-arrest radius + accretion/apposition cross-sections)** → **OPEN-SS-39**, already registered, still open, still the most likely program-killer per 0862. Independent of G1a.

---

## POINTERS (read for orientation)
- **SF G1a arc, reasoning + code 2200–2202** (in `flagship_papers/strong/`): `reasoning/2200.md` (static ratio, the superseded scare) → `reasoning/2201.md` (ponderomotive, the correct viable) → `reasoning/2202.md` (corpus close). Fastest orientation: read **2201.md then 2202.md**; 2200 is context. Run `code/2201_verify_g1a_ponderomotive.py` and `code/2202_verify_g1a_screening_pin.py` to reproduce the viable band + the 17× margin.
- **OPEN-SS-40** in `frontier_sectors/SS.md` — the registered G1a result and its residual (the canonical SF-side statement of what's delivered vs blocked).
- **DM junction arc 1830–1836** — your own prior context; note 1835's "gradient read → soft" is now *vindicated in direction* but on corrected physics, and 1836's ratio collapse is *confirmed* (the framing was right; the number is ~0.02, not 0.1).
- **0860–0862** — the stiff-ribbon requirement the consistency result reconciles with the soft scissor.

## SUGGESTED SEQUENCE (your call)
Floor verdict + disposition update first (fast, unblocks the mechanism-note STATUS), then panel round 2 (the held item), then the ℓ_p×g cross-lane κ_scissor (a real bonus close), then back to the formation-side make-or-breaks (G3/OPEN-SS-39 is the sharpest remaining kill risk). The floor is viable — but DM-1's promotion still waits on the formation side and the FP root-blocker, so frame the panel-round-2 outcome as "velocity-sector floor cleared, formation side and absolute scale still pending," not as a candidate-wide green light.
