# HANDOVER — SF-2/SF-5: the edge-bond SSV ask is SHARPENED to a scale-free ratio g, and now closes THREE DM questions at once
**Date:** 2026-06-30 · **Lane:** strong/EW substrate (SF-2 + SF-5) · **From:** Opus (DM 18xx session) · **Consumer:** DM-1
**Supersedes the framing of (does NOT replace):** `handovers/2026-06-25_sf2_sf5_edge_bond_ssv_deciding_calc.md` — read that first; this file tightens its ASK, it does not cancel its goalposts.

---

## ⛔ LINE 1 — BLOCKING CLONE GATE (do this before anything else)
```
cd ~/Documents/GitHub/CPP && git pull --rebase origin main && git log --oneline -8
```
Do NOT register an ID, place a file, or compute a coefficient before cloning and grepping the registry. Confirm origin/main HEAD includes the DM junction arc **1830–1837** and the founders_vision 30 June extension (HEAD at handoff: `638d9261`). **This is a cross-window handover: the work it asks for is SF-2/SF-5 lane, NOT DM lane.** Pick your own next free SF patch number in your band; grep the THEO/OPEN registry before reserving any ID. **G3's home OPEN-SS-39 is already registered (do not re-register).** The G1 angular-stiffness item is NOT yet a registered OPEN — register it under your own grep when you take this up; do not let the DM lane register an SF ID.

---

## WHAT CHANGED SINCE 25 JUNE (one paragraph)
The 25 June handover asked for the full edge-bond SSV potential and its three goalposts (G1 κ_θ→ℓ_p, G2 E_qq/E_ee depths, G3 glueball-arrest). Since then the DM junction arc (reasoning/code **1830–1836**) worked the **angular-stiffness branch (G1)** hard and produced a structural simplification that **makes the DM-floor half of G1 much easier to deliver**: the DM cluster-floor verdict no longer needs the **absolute** κ_θ — it needs only a **ratio** of the same edge bond evaluated in two geometries, in which the absolute scale, the formation temperature, the ZBW frequency/amplitude, **and the static-vs-dynamic (Earnshaw) sign question all cancel.** That ratio, plus the same potential's absolute depths (still wanted for G2/ℓ_p), means **one substrate calculation now closes three DM questions instead of one.**

## THE KEY RECOGNITION (why the ask got easier)
The **X-junction dihedral stiffness** (two DM rods fused at a single qq edge bond, scissoring about that edge) and the **ribbon bending rigidity** B (adjacent rungs hinging in-line) are the **same qq-edge-bond SSV angular stiffness in two geometries.** The DM floor's flexibility test (DM reasoning 1830) is κ_θ < 3B/L_arm. Writing **g ≡ κ_scissor/κ_bend**, with B = κ_bend·ℓ_rung (worm-like chain) and L_arm = (N/2)·ℓ_rung, that test collapses to:

  **g < 6/N**  (= **0.43** at the floor-setting N ≈ 14 post-fusion arms).

Because g is a ratio of the *same* potential, the absolute normalization (depth, kT_form, ZBW amplitude) cancels, and so does the Earnshaw sign worry (DM 1834): whatever provides the restoring torque in the in-line bend provides it in the perpendicular scissor the same way. **Only the geometry survives.** The founder's gradient read (Thomas, 30 June; founders_vision 30 June entry, and DM reasoning 1835) estimates **g ~ 0.1** (the perpendicular crossing puts the off-hinge eDP/qDP pairs farther apart than the in-line bond → softer by the gradient-squared falloff) → **g < 0.43 → flexible hinge → cluster floor viable.** This is an **estimate from geometry + the SR-1 gradient law's distance dependence; the evaluated potential is yours to deliver.**

---

## THE ASK (one object, now with a CHEAPER primary target)
**Derive the qq-edge-bond SSV potential** (the qCP–qCP edge bond where rungs/rods join), as a function of separation and bend angle, at the sub-Planck pre-tension separations the substrate fixes — **and evaluate it in the two bend geometries.** From it, in priority order for DM:

**G1a — the RATIO g = κ_scissor/κ_bend (NEW, cheapest, decides the DM floor).**
- **κ_bend:** angular stiffness for the **in-line** bend (adjacent-rung hinge — the ribbon persistence-length mode).
- **κ_scissor:** angular stiffness for the **perpendicular** scissor (two rods crossed at one edge, hinging about it — the X-junction).
- **DM target: g < 6/N ≈ 0.43 (N≈14).** Founder estimate g ~ 0.1. Report g with its geometry inputs; the absolute normalization cancels, so this is the part that does **not** need the hard absolute-scale pin.
- ⚠️ Still a **near-cancellation in each geometry** (closer like-charge repulsion − farther opposite-charge screening; DM 1834 confirmed a naive static point sum is Earnshaw-unstable, so use the screened edge-bond charge set, not free points). But the **ratio** is far more robust than either absolute κ — the near-cancellation's overall scale divides out; what remains is how the cancellation's *geometry* differs between in-line and perpendicular.

**G1b — the absolute κ_θ → ℓ_p (the original G1; still wanted for formation/stiffness).**
- Target unchanged: **ℓ_p ~ 100–700 fm** (κ_θ ~ 100–700 × kT_form; θ_rms ≈ 3–8°/hinge). Needs the absolute scale (kT_form / substrate thermal history — SF-input).

**G2 — well DEPTHS E_qq > E_ee (unchanged from 25 June).**
- Target **E_bond ~ 0.8 keV – 2 MeV**; e–e edge is the weaker/scission bond (governs breakage/length kinetics); report both.

**G3 — glueball-arrest radius + accretion/apposition cross-sections (OPEN-SS-39, unchanged).**

The **second-moment-of-area ladder** (hTetra vs 4-wide ribbon vs 4-wide cross) and the **per-rung 2eDP:2qDP mass** (defaulted 264 MeV) notes from 25 June still stand.

---

## LANE BOUNDARY (what is SF vs what stays DM — do not cross)
- **SF delivers:** the edge-bond SSV potential and its derived numbers — **g (the ratio)**, the absolute κ_θ (→ℓ_p), E_qq/E_ee, the second-moment ladder, σ_accrete/σ_appose, the glueball-arrest radius. Register results in your SF band + the relevant THEO/OPEN IDs (register a new OPEN for G1a/G1b under your own grep; OPEN-SS-39 for G3).
- **DM consumes (do NOT do this in the SF window):** plugging **g** into the cluster-floor verdict, **ℓ_p** into the loop-size/σ(N) distribution, **E_ee** into the fragmentation/lifetime kinetics, and any DM-1 promotion. That is DM 18xx lane work, gated on your outputs. Hand the numbers back; the DM lane closes the loop.
- The DM lane has deliberately **not** evaluated the potential itself (it needs the SR-1 SSV law at sub-Planck pre-tension separations — SF territory); it has only used the *ratio structure* + the founder's geometry read to place g ~ 0.1 as an estimate.

## SECTOR TOUCHPOINTS
- **eCP/qCP electrostatic SSV at sub-Planck pre-tension** (G1a/G1b near-cancellation; G2 depths) → **SF-2** (the W 3eDP:3qDP bracelet is the same kit, charged; the DM ribbon is its neutral, doubled-width, looped cousin). Force law = **SR-1** (in hand).
- **hDP/gluon residual + glueball-arrest** (G3) → **SF-5**.
- **264 MeV constituent + qDP structure** → **SF-3** (in hand).

---

## WHAT A WIN / WHAT A KILL LOOKS LIKE
- **Win (DM floor):** g < 6/N for the X-scissor vs ribbon-bend geometry at N≈14 (founder estimate g ~ 0.1 holds) → the junction hinges freely → cluster floor lands in the viable band (~0.4–0.8). Combined with ℓ_p ∈ [100,700] fm and E_ee ∈ [0.8 keV, 2 MeV], DM-1 promotes off Layer-C.
- **Clean kill (also valuable):** g ≳ 0.43 for every plausible geometry (the perpendicular scissor is **not** softer than the in-line bend) → the X-junction is rigid → the self-limiting weakens and the cluster floor rises to marginal/tense (~1.0–1.6). OR the absolute near-cancellation gives κ_θ ≪ 100 kT_form / ≫ 700 kT_form (ℓ_p out of band) → the extended-aggregate channel fails on the formation side. The goalposts are sharp enough to be decisive either way.

---

## POINTERS (read for orientation)
- **DM junction arc, reasoning + code 1830–1836** (in `series_phenomena/cosmology/dark_matter/`): 1830 (flexibility test κ_θ<3B/L_arm; first, knot-model, tense) → 1831 (founder edge-hinge corrects it) → 1833 (static κ_θ≈0.27, **retracted**) → 1834 (Earnshaw: naive static sum unstable) → 1835 (founder gradient read → soft) → **1836 (the ratio g collapse; run `code/1836_kappa_theta_scalefree_ratio.py`)**. Fastest orientation: read `reasoning/1836.md`, then `reasoning/1831.md`.
- **founders_vision.md, 30 June 2026 entry** — Thomas's edge-hinge mechanism + the scissor-mode gradient read, verbatim (the physical basis for g ~ 0.1).
- **The mechanism note** `DM-1/documentation_suite/mechanism-strip-then-fuse-DM-1.md` — STATUS/Disposition carry the current viable-pending-g state.
- **`handovers/2026-06-25_sf2_sf5_edge_bond_ssv_deciding_calc.md`** — the original three-goalpost ask this sharpens.

## SUGGESTED SEQUENCE (your call)
G1a (the ratio g) is the cheapest and decides the DM floor — worth doing **first** and handing back immediately, since it unblocks the DM-1 floor verdict and the panel round 2 without waiting on the absolute-scale pin. G1b/G2 (absolute κ_θ, E_qq/E_ee) and G3 follow. **DM panel round 2 is being held until g comes back**, so a fast G1a turnaround is the single highest-leverage SF deliverable right now.
