# N2B-FUNNEL-3 execution record — VERDICT RF3-BRACKET: R_f(ON, w = 4) ∈ [10, 12)D DRAWS DT-STABLY AT THE FINER UNION; THE TWO WIDTHS BRACKET IDENTICALLY, AND THE 2640 WIDTH-ORDERING OBSERVATION DOES NOT SURVIVE AT DRAWN RESOLUTION

**Patch 2642, 20 July 2026.** Execution under `n2b_funnel3_prereg.md` (2641)
only. Verify: `code/2642_n2b_funnel3.py`.

## 1. Control: PASS

**C-F3 (convention-pin):** b = 9, w = 4, ON at dt = 1/200 → CAP (d_inc = 0.85),
reproducing the 2640 dt-stable fact exactly. The cell reads.

## 2. The walk

```
b=9 :  1/200 CAP (0.85)   1/400 CAP (0.85)   dt-STABLE
b=10:  1/200 CAP (1.16)   1/400 CAP (0.84)   dt-STABLE
b=12:  1/200 SCA (27.45)  1/400 SCA (27.53)  dt-STABLE   <- STOP (first dt-stable non-CAP)
```

No FRG; no dt-unstable cell anywhere on the walk — the margin note class never
fires. The b = 10 cell that flipped SCA(1/100) → CAP(1/200) at 2640 resolves as
CAP at the finer union: **the coarse 1/100 leg was the unstable one**, the same
lesson the w = 2 OFF bracket taught at 2640 (and the third instance tonight of
a marginal-cell instability living in the coarsest leg).

## 3. Reading (frozen at 2641 §4): RF3-BRACKET

**R_f(ON, w = 4) ∈ [10, 12)D registers** — last-CAP b = 10, first-non-CAP
b = 12, both pairs dt-stable, no unstable interior. The 2640 "≥ 9D, upper bound
undrawn" entry is superseded by citation. The steep funnel now has drawn walls
on both sides: R_f(OFF, w4) = 5D (2624) below, [10, 12)D above — the
sink-mediated excess at the steep width is ≥ 5D, sharper than the ≥ 3D the
class gate required.

**Width-coherence re-read (registered as observation only, per the frozen
reading):** the drawn brackets are now IDENTICAL at both widths —
R_f(ON, w2) ∈ [10, 12)D (2640) and R_f(ON, w4) ∈ [10, 12)D (this record). The
2640 observation "the soft width out-reaches the steep in the analytic-well
ordering" does NOT survive at drawn resolution; it was an artifact of the then-
undrawn steep bracket. What the drawn pair actually says is stronger for the
registered classification and is registered as observation only: the analytic
wells differ by nearly a factor of two (b_W = 4.5D vs 2.5D) yet the ON reach is
width-indistinguishable on this grid — **the sink-mediated funnel washes out
the well-width ordering**, which is exactly what "the reach is sink-mediated,
not potential-driven" (RF1, both widths) predicts of itself. No claim promoted;
the sentence lives here as the re-read the prereg mandated.

## 4. Standing

**The funnel program's declared successors are now EMPTY**: upper bounds drawn
at both widths, OFF boundaries drawn at both widths (w4: 5D at 2624; w2: 7D at
2640), RF1 sink-mediated at both widths, no undrawn cells, no dt-unstable
brackets. Remaining funnel questions are derivational (FORM-1 lineage: the
Morse-form session inherits the boundary-shape and wash-out observations as
exhibits). DEP-1 row appended at this patch. Fences held: classification only;
no rates, no σ, no flux, no relic contact; v = 0.10c, DISC block untouched;
σ_cap withheld; EDGE-2(i) queued; 2624/2640 records unedited; **79.5%
untouched.** Founder-free queue after this patch: the optional soft-width wall
confirmation (ROB-2 walls at w = 2; declared optional at 2638, never queued) —
otherwise the queue is empty and the founder's packet (2636 §4, unchanged — no
flags raised by 2637–2642) remains the next act at the founder's timing.
