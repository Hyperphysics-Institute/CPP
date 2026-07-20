# N2B-DISC-1-2 pre-registration (corrected re-entry): the strengthened sink-ON/sink-OFF single-transit discriminator + the 7D-funnel audit — the 2620 cell with the C2 gate corrected per the 2622 diagnostic, committed before any member run

**Patch 2623, 20 July 2026. Status: N2B-DISC-1-2 OPENED at pre-registration; NO
member run performed.** This is the corrected re-entry of the 2620 cell under the
RC4 discipline (stopped cells re-enter only via corrected prereg). **Everything in
`n2b_disc1_prereg.md` (2620) — framing, launch convention with drift compensation,
registered inputs, instrumentation, members M1–M5 with all grids, tolerances,
frozen readings RD1/RD2/RD3/RF1/RF2/RF-INT, and fences — carries VERBATIM into this
document by citation,** except the two corrections below, both designed from the
2622 measurements (the 2613 pattern: the same cell with the defective element fixed
and named).

## Correction 1 — C2's energy-integrity leg becomes a convergence gate

The 2620 FLOOR = 2.0 gate was a borrowed-gate transfer (2622 §2, lineage-checked:
no registered transit cell gates Edrift at FLOOR). Corrected C2:

- **C2a (unchanged):** Sea(η = 0) machine-zero (|Sea| < 10⁻⁶ MeV) at the C2 cell
  (v = 0.10, b = 0, w = 4, dt = 1/200).
- **C2b (corrected):** Edrift(η = 0) at the C2 cell FALLS under dt refinement with
  per-halving ratio ≥ 1.5 across 1/100 → 1/200 → 1/400. (The 2622 D1 measurements
  — 48.7 → 25.4 → 11.0, ratios 1.91/2.31 — satisfy this; the gate is re-executed
  fresh under this prereg, not cited.)

## Correction 2 — baseline-exposure guard on every gated deposit

Both instruments carry a 10–30 MeV encounter baseline at working dt (2622 D1/D2).
Every deposit reading that enters an M2/M3 gate is printed beside its own cell's
Edrift; **any gated deposit with S_1pass < 3 × (same-cell Edrift) is flagged
BASELINE-EXPOSED, excluded from gating, and reported raw.** If a baseline exposure
strikes an anchor cell, the affected gate reads UNGATEABLE-AT-THIS-INSTRUMENT
(neither pass nor adverse) and the record says so plainly.

## Controls (gating; run FIRST; any failure stops the cell unread)

C1 (convention-pin, METH-L2-015) and C3 (decomposition sanity) verbatim from 2620.
C2 = C2a + C2b above. The 2621 control outputs are NOT recycled; all controls
re-execute under this document.

## Bookkeeping

Members and readings: 2620 §3–§4 verbatim. Next patch: execution under this
document only. Verify script `code/2624_n2b_disc1_2.py` (the 2621 script re-run
whole under the corrected gates; stages controls | m1 | m23 | m4 | m5,
foreground-chunked). Fences unchanged: no rates, no σ_cap, no relic contact,
EDGE-2(i) not run, 79.5% untouched.
