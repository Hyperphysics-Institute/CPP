# OPEN-DM-ENDBOND-3 — R-A executed under the 2550 pre-registration: the dance ⟨E⟩(κ) curve is barrier-free with κ* dt-stable; **E_close PINNED at dance strength: [+128.9, +137.5] MeV** — G1 PASS (fully inside the map band), G2 FAIL (102 not in band) → BANKED PIN; downstream 2542 revision licensed

**Patch 2551, 18 July 2026. Status: OPEN-DM-ENDBOND-3 CLOSED with a BANKED PIN** (G1 pass
without G2 → pin, not win-class, per the frozen readings). Verify:
`code/2551_endbond3_curve.py` (42 dance runs, 230 s; all assertions pass; the union table
and the frozen band print before the gates section; fenced numbers appear nowhere above
the freeze).

## 1. The frozen curve

dance_v8 verbatim on the 2450 corrected bend family, N = 16, grid κ/κ_ring ∈
{0, 1/5, 2/5, 3/5, 4/5, 15/16, 1}, union dt {τ_C/100, /50, /25} × FREF {grid 12.45,
16-plane 10.47}. Closure sanity: seam pitch 1.1426 fm = the uniform chord (exact ring).
⟨Ep⟩(κ) in every one of the six cells has its **grid maximum at κ = 0 (κ\* = 0,
dt/FREF-STABLE)** — the barrier-free reading applies:

**E_close ≡ ⟨E⟩(0) − ⟨E⟩(κ_ring) = −(ring−straight). FROZEN UNION BAND:
E_close ∈ [+128.9, +137.5] MeV** (interface total; positive = closure pays).

Curve shape (banked): mild descent 0 → 3/5 (~−12 MeV total); a large collective drop
3/5 → 4/5 (~−110 to −120 MeV, where the 270°-wrapped arc brings non-adjacent planes into
mutual range — the cooperative compaction the fragment null of 2549 predicted); a small
local rise 4/5 → 15/16 (+6 to +15 MeV — a shallow *approach* sub-structure, NOT κ\* under
the knob-free definition); the final seam-engagement drop 15/16 → 1 (−14 to −20 MeV).
⟨Etot⟩ accounting (disclosed) is same-signed and larger in magnitude at every cell.

## 2. Gates (fixed order, against the frozen band)

**G1 ([40, 170] membership): PASS — the band [128.9, 137.5] is fully inside.**
**G2 (102 lock): FAIL — 102 is not inside the band; midpoint offset +31.2 MeV.**
κ\* stability: STABLE (win-class requirement met on this axis, but win-class requires
G1+G2; G2 failed). **Reading: BANKED PIN at dance strength**, with the pre-registered
consequence: the downstream revision patch through 2542 is licensed (fires next patch).
The G2 miss is recorded as-is: the interface total exceeds the single-pair contact depth
by ×1.3 — no reinterpretation (the per-pair reframe is Branch T and is not taken; if the
comparison of interface-total to per-pair scales deserves study, it is a named future
question, not a rescue).

## 3. Internal-consistency statements (no gate force)

(a) **Reproduction vs 2510:** the κ = 0 and κ = 1 endpoints at FREF_16 ARE the registered
2510 configuration. Rod ⟨Ep⟩ reproduces **to the decimal** (−2598.2 / −2588.4 at dt =
1/100, 1/50); ring ⟨Ep⟩ agrees to ~2 MeV (−2732.3 vs −2734.2), i.e., within the
**registered chaotic floor** (2513 Branch-U diagnosis): scaffolds and rule functions were
verified bit-identical (max |ΔP| = 3×10⁻¹⁵), so the residual is float-ordering chaos
across numpy builds, at 0.07 % of ⟨Ep⟩. **A ±2 MeV chaotic-floor rider therefore attaches
to the band edges; no reading changes** (G1 remains comfortably passed, G2 remains out).
(b) Echo family: the barrier-free E_close equals −(r−s) by construction (declared 2550
§2.4, zero evidential weight); materially, the v8 value (~133) sits far from the v4-era
back-implication (~85) because v8's hardening roughly doubled the ring preference
(−68.8 → ~−133) — a registered fact of the functional's evolution, not news.

## 4. What is now known at dance strength

The formation path from straight rod to closed ring is **downhill the whole way at the
registered grid resolution** (no barrier; the 2453 "closure downhill" reading confirmed at
v8 hardening), with the net closure payoff pinned an order of magnitude more tightly than
the 2542 statics band: **ΔE_close(16) = −E_close ∈ [−137.5, −128.9] MeV (±2 floor)**,
inside and collapsing 2542's [−154.7, −23.0]. The ratchet picture strengthens: no impulse
threshold is even required at this resolution — the seam pays 14–20 MeV at engagement on
top of a large cooperative compaction. Cross-lineage note (disclosed, NOT a pin): with the
2542 statics bend E_bend(16) ∈ [15.3, 17.0] MeV, the implied seam-bond alone would be
E_bend − ΔE_close ∈ [144, 155] MeV — a mixed-lineage arithmetic in the same family as the
retired ≈85 construction, carried for orientation only.

## 5. Bookkeeping

79.5 % untouched (banked pin; no win-class). L = 16 consumed under the RODCLOSE
conditionality rider (no L-selection claim; NB-S3a-1 untouched). Dated pin line joins the
standing disclosure package. Next patch: 2552 — the licensed downstream revision rider on
`rodclose1_ra_statics.md` (ΔE_close and survival collapse; kT_form band explicitly NOT
collapsed). Queue after: RODCLOSE-1 kinetic limb → plane-resident-fraction limb → δ_E →
MW-MODES TC-extension.
