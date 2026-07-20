# R-B item 1 mini pre-registration: E_close(8) under the truncation-convention union — clearing or superseding the formation window's lower-endpoint rider, committed before any run

**Patch 2632, 20 July 2026. Status: R-B-1 OPENED at mini-prereg; NO run performed.**
The one LIVE reach-S defect from the 2574 audit: at L = 8 (only), the 'q' reach
list's `sorted(set(...))[:5]` truncation BINDS (max pre-truncation count 7 at 16 of
32 qCPs) — an INDEX-ordered cutoff discarding up to two in-reach neighbors by an
arbitrary rule. A caveat rider sits on the formation window's lower endpoint
("even L ∈ [8, 22]"; "closure pays down to L = 8") until this cell reads.
Registered value under the index-ordered convention (2557 P2 table, reach-S):
**E_close(8) ∈ [+83, +84] MeV across dt = τ_C/{100, 50, 25}.**

## 1. Inputs (verbatim; zero freedom)

Machinery: exec-load of the registered 2557 artifact (`scaffold_L`, `dance_v8`,
`build_reach_S`, `ssv_vectors`, constants — the registered objects; override bound
in the chain namespace, the 2574 lesson (c)). E_close(8) = ⟨E⟩(straight L=8) −
⟨E⟩(ring L=8), FREF per the 2557 protocol (max over both scaffolds), dt ∈
{1/100, 1/50, 1/25}, TC = 60, burn 0.15 — all verbatim. **Convention union
(frozen):** (a) **INDEX** — the registered `[:5]` (reproduction control); (b)
**DIST** — nearest-5 by distance (the 2574 remedy convention); (c) **FULL** —
untruncated. The truncation-binding census line (count distribution at L = 8) is
printed for each convention.

## 2. Frozen readings

- **Control (gating):** the INDEX member reproduces the registered [+83, +84] band
  at all three dt (deterministic machinery; exact-to-print expected). Failure →
  RC4, nothing reads.
- **RB1-CLEAR:** DIST and FULL both read E_close(8) > +FLOOR (2.0) at all three dt
  → closure pays at L = 8 under EVERY admitted convention; **the lower-endpoint
  rider CLEARS**; the window "even L ∈ [8, 22]" stands whole, now
  convention-union-backed; the 2574 §3 caveat is discharged.
- **RB1-SUPERSEDE:** DIST or FULL reads ≤ +FLOOR (or sign-negative) at all three
  dt → the lower endpoint **SUPERSEDES to L = 10**; the window statement becomes
  "even L ∈ [10, 22]" pending refinement; the registered "closure pays down to
  L = 8" sentence takes a correction rider; consumers (the 2561 packet ITEM 5
  line, the FORM-L-2 record's window sentence) receive citation-hygiene notes
  (corrections cited forward; no retro-edits). Adverse-direction, same font.
- **RB1-MIXED/UNSTABLE:** conventions disagree dt-unstably, or a member straddles
  the floor across dt → the rider STAYS with the raw table attached; a finer cell
  is declared. Nothing clears, nothing supersedes.
- **Fences:** L = 8 only (the wall bracket (22, 24), the payoff maximum, the
  window body L ≥ 10, E_close(16) pin, and 79.5% are all untouched by every
  reading — the 2574 audit already certified them clean).

## 3. Bookkeeping

Next patch: execution + the R-B items 2–4 continuation per the ledger's fixed
order. Verify script `code/2633_rb1_l8_union.py`.
