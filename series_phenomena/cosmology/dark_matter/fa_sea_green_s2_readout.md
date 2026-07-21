# FA-SEA-GREEN S2 READOUT — outcome class FG-OTHER: the derived Sea response operator screens exponentially (envelope over seven decades) at ℓ = 0.091 ± 0.002 fm ≈ d_DP/4 — a gap-generated scale on NEITHER fork endpoint — with a sign-staggered lattice-scale component registered as a new structural finding; the registered I1 arena itself is readout-inconclusive (compactness, disclosed in advance), the readout coming from the same zero-parameter operator on the extended z=12 instrument

**Patch 2671, 20 July 2026. Stage S2 of the FA-SEA-GREEN charter (FROZEN
2666). This is the readout stage: the fork candidate values appear below
for the first time in the arc, per the blind protocol's design. Everything
upstream (S1a 2668, S1b 2669, S1c 2670) was executed and committed blind.
79.5% not in scope. Every sentence below routes to the CONV-001 packet —
the panel opened the fork; only the panel closes it.**

## §1 — Assembly (zero free parameters, all inputs derived upstream)

Sites = the registered I1 graph (120-vertex 600-cell, SS-2 embedding,
ℓ_unit = 0.589 fm, edge = ℓ_edge = 0.364 fm; instrument check: |V|=120,
min chord = ℓ_edge, degree 12 — re-verified). Operator = the S1b-derived
discrete-site scattering form M = I + αG, G_ij = 1/r_ij. Gap κ = 2/d_DP
with d_DP = ℓ_edge (S1c, INF-S1C-1). Coupling α = κ²/(4πn) with
n = √2/ℓ_edge³ (z = 12 packing density — **the 2527 4D→3D density flag is
consumed exactly here and nowhere else**), giving α = ℓ_edge/(π√2) =
0.0819 fm. External point source at a vertex; response on the remaining
sites; I6 normalization applied at the shell nearest d = 1.15 fm.
Scripts: `code/2671_s2_spectrum_readout.py` (registered arena, both
distance metrics), `code/2671b_s2_diagnostics.py` (D1 spectrum, D2
extended instrument), `code/2671c_s2_envelope.py` (shell-resolved
envelope), `code/2671d_s2_robustness.py` (size/window band).

## §2 — The registered arena: READOUT-INCONCLUSIVE (disclosed limitation realized)

On I1 the solved field is **sign-oscillating across shells** under both
the primary (4D chord) and robustness (graph-geodesic) metrics: no clean
decay regime exists on a compact 120-vertex arena whose largest pair
distance is 3.2× its smallest. This is precisely the compactness
limitation S1b §5 disclosed before any spectrum existed. Diagnostic D1:
the assembled operator is **positive-definite** (spectrum 0.64–14.3, no
negative eigenvalues) — the oscillation is not an operator pathology or
resonance. The registered-arena computation is reported as
**REGISTERED-ARENA-INCONCLUSIVE**, in full, for the panel.

## §3 — The readout: extended instrument, identical operator

Diagnostic D2 ran the IDENTICAL derived operator — same α, same 1/r
couplings, same κ, zero parameters changed — on extended z = 12 lattices
(FCC instrument proxy, the same proxy validated fork-blind at 2668/2669)
with a genuine asymptotic regime. Findings:

1. **The sign oscillation persists** — it is physics of the derived
   operator in the κ·a = 2 strong-lattice regime, not an arena artifact:
   the static response is **sign-staggered at lattice scale with a
   cleanly exponential envelope** (Friedel-type evanescent response).
   Registered as a new structural finding of the Sea's static response;
   adjacent to Seat 4's 2664 anisotropy note.
2. **The envelope decays exponentially over seven decades** (shell table
   in `2671c` output), with

   **ℓ_env = 0.091 ± 0.002 fm** (band across lattice sizes R = 7, 9 —
   size-converged to 4 decimals per window — and three fit windows;
   instrument uncertainty, NOT FG-BAND: I5 was answered at S1c, no
   E_qq window propagates).

## §4 — First appearance of the candidate values, and the class

Fork candidates (first appearance in this arc, per protocol):
βd = 1.953 (per-cell, ℓ = ℓ_unit = 0.589 fm) and βd = 3.159 (per-edge,
ℓ = ℓ_edge = 0.364 fm). The derivation lands

**ℓ = 0.091 ± 0.002 fm ⟹ βd = d_reg/ℓ = 12.6 ± 0.3 — NEITHER candidate.**

**Outcome class: FG-OTHER** (frozen §4: "ℓ emerges at another
eigenlength (including PSR-derived or bridge-generated scales)"). The
emergent scale is gap-generated: ℓ_env coincides within instrument
uncertainty with **d_DP/4 = ℓ_edge/4 = 1/(2κ) = 0.0910 fm** — a factor-2
lattice shortening of the continuum 1/κ. **OBS-class observation,
registered non-adjudicative per standing rules:** the identification
ℓ = 1/(2κ) exactly is plausible-analytic but UNPROVEN; it is an
observation, not a claim.

**NOT FG-NEG:** exponential screening for the Sea is CONFIRMED, not
refuted — FA-C2's exponential form is derived; its registered-consumer
VALUE is another matter (below). **Not FG-CELL, not FG-EDGE, not
FG-BAND, not Branch I.**

## §5 — Consequences (all panel-gated; nothing promoted here)

1. **FA-C3:** the fork's dichotomy DISSOLVES — neither per-cell nor
   per-edge is the Sea's screening scale; the founder's 2666 structural
   consequence ("neither fork candidate is a property of the elementary
   process") is realized in the strongest form: both candidates fail to
   emerge. FA-C3-DISC-1 routing under FG-OTHER was left unspecified by
   charter §5 (replication route named for FG-CELL/EDGE, discovery route
   for Branch I/FG-BAND) — **routing is the panel's call.**
2. **FA-C2:** grounded at Sea level as to FORM (exponential screening
   derived from registered objects, G1-anchored), but the derived ℓ is
   ~4× shorter than the shorter fork candidate. Whether this stands in
   tension with FA-C2's registered consumers (the composite's screening
   usage; DEP-1 rows) is a panel adjudication item — flagged, not
   resolved, here. The 2664 rider travels on every Morse-class consumer
   sentence; none is edited by this patch.
3. **I5 (from S1c, carried):** zero-parameter point readout; the E_qq
   window does not propagate.

## §6 — Honest-status ledger for the packet

- Readout provenance: extended instrument (registered arena inconclusive,
  §2) — the panel may weigh this as it sees fit.
- The 2527 density flag consumed in α (§1) — a sensitivity scan over the
  flagged n was NOT run pre-readout (blind protocol barred
  decay-vs-parameter curves) and is available on panel demand.
- INF-S1C-1 (d_DP = ℓ_edge) is attackable by name; ℓ scales with d_DP.
- R = 11 exceeded container memory; R = 7 vs 9 size-convergence to
  4 decimals makes larger lattices unnecessary for the stated band.
- Blind-protocol audit: S1a–S1c committed with no candidate value, no ℓ,
  no decay curve (per-stage audits in reasoning/2668–2670); first
  appearance of candidate values = §4 above. **No breach.**

**79.5% untouched. Nothing renamed after results (classes as frozen).
Next action: the CONV-001 packet.** Reasoning: `reasoning/2671.md`.

---

## PANEL RULING NOTE (Patch 2675, additive; CONV-001 returns on the 2672 packet adjudicated at 2674, five of five)

The §5 panel-gated items are answered. §5.1: routing = **CLOSE-FORK-FG-OTHER
5–0** — FA-C3 CLOSED; FA-C3-DISC-1 replication route CLOSED, discovery route
re-scoped to the derived scale. §5.2: tension ADJUDICATED 5–0 — the **2674
rider** (canonical text at `conv001_2026-07_seagreen_readout_returns_adjudication.md`
§5) is in force on every FA-C2 consumer sentence; Gemini demotion clause
active for width-dependent quantities. Q1a: FG-OTHER ADOPTED 5–0 with
amendments A1+A2 — this record's readout is cited as **"FG-OTHER on the
present operator construction"**; the sign-staggered component is a property
of the derived operator pending representation-independence. Q1b:
SUFFICIENT-WITH-REMEDY-QUEUED 5–0 — **FA-SG-R1** registered (multi-motif
arena + robustness battery + mandatory J3 leg); the numerical ℓ is capped at
observation grade until R1 executes. No breach finding; the blind-protocol
close-out stands as audited. Nothing above this line is edited.
