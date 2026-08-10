# OPEN-QMRG-ETA — MODE-INDEPENDENCE DERIVED AT LATTICE-BOOKKEEPING GRADE; THE VALUE REDUCED TO A GEOMETRIC CONSTANT

**GRADE LABEL (v1.1, Patch 3038 — the CONV-013 AUX-1 [GPT]
amendment executed): every result in this record is
LATTICE-BOOKKEEPING GRADE — an identity/computation of the ratified
accounting clauses (A3' universal Moment cadence; I-3 per-transit
quantum; Version-B relay multiplicity). It is NOT a MICROSCOPIC
LATTICE DERIVATION of eta from CP-level dynamics, and no citation of
this record may claim the microscopic grade. The distinction is
load-bearing for the AUX-1 closure question and is maintained
verbatim in the ALL-MODES lemma record
(`code/3038_eta_mode_coverage_extension.py` header) and the AUX-3
discharge record.**


**Patch 3009 (4 Aug 2026).** First work under ordinary bookkeeping in
the post-arc QM lane. Advances OPEN-QMRG-ETA: the participation
ratio η ≡ ρ/N (registered + quarantined at 3006; the E-2 persisting
note class "η-universality" hangs on exactly the claim derived
here). Status: **mode-independence DERIVED at lattice-bookkeeping
grade (panel touchpoint optional, batchable); η's numerical VALUE
reduced to a pure geometric constant, which remains the item's open
content.** Verify:
`series_quantum_mechanics/code/3009_eta_mode_independence_check.py`
— EXECUTED, ALL ASSERTIONS PASS, stdout §4. Unprinted sentinel per
the amended KEY-DESIGN RULE incl. clause (c): the sentinel is a
bookkeeping INTEGER (a packet count at a random unprinted
configuration) with no theoretically anticipated value.

## §1 — The derivation: a cancellation between two ratified clauses

Let a coherent mode of frequency ω hold N quanta with normalized
spatial profile |u_i|² over its support. The per-site register count
ρ_i is the number of messenger arrivals at GP i per Moment.

**Ingredient 1 (A3′, ratified): the turnover rate is the Moment
cadence — universal, not a mode property.** The GP resets its
registers EVERY Moment from arrivals; the sustained pattern's full
local content is therefore relayed once per Moment regardless of ω.
Content relayed through site i per Moment = the local energy share
E_i = N ħω |u_i|².

**Ingredient 2 (I-3 / E = ħν_C, SF-6 Tier 1): the effective content
per messenger transit scales with the mode's quantum, ħω.** (The
provenance of this input was audited acyclic at
`conv016_adjudication.md` §5.)

**The cancellation.** Arrivals at i per Moment:

    ρ_i = (content relayed)/(content per transit) × c_geo
        = (N ħω |u_i|²)/(ħω) × c_geo
        = c_geo · N |u_i|²

The ω's cancel. Hence η_i ≡ ρ_i/(N|u_i|²) = c_geo — a constant
depending only on the relay geometry (coordination z, edge-transit
multiplicity of the per-Moment rebuild), NOT on ω, k, N, or the mode
profile. **Mode-independence is not an additional assumption on top
of the quarantine; it is forced by the same two ratified clauses the
whole arc runs on.** Each ingredient is individually load-bearing:
break I-3 (fixed-energy packets) and η ∝ ω; break A3′ universality
(ω-proportional cadence) and η ∝ ω again — both demonstrated as
negative controls (§4, slopes +1.00 and +1.02 against the ratified
pair's +0.00).

## §2 — What remains open (the item's reduced scope)

**c_geo — the pure number.** The relay multiplicity of the
per-Moment rebuild (how many distinct messenger transits constitute
one site's refresh share of one quantum) is set by the committed
relay protocol on the z=12 shell and is not computed here. Two
honest notes: (a) nothing physical downstream depends on c_geo's
value — it is absorbed into the normalization conventions the 3006
labeling obligation already governs; (b) its computation is a
finite, well-posed bookkeeping exercise on the ratified protocol
(Version B relay), a suitable single-patch task when wanted.
OPEN-QMRG-ETA therefore REMAINS OPEN at reduced scope: value-only.

**Panel standing.** The E-2 persisting note class "η is universal /
mode-independent" was barred pending exactly this derivation. Bar
scope moves only through panel action; this record makes the note
class DISCHARGEABLE at the next panel touchpoint (batchable with
future QM-lane items — no dedicated round is warranted for ordinary
bookkeeping; the arc's special machinery is retired).

## §3 — Honest limits

The §1 argument is bookkeeping-grade: it consumes the two ratified
clauses and the arrival-count definition of ρ, and its sim (§4) is a
STRUCTURE verification with quantization noise and controls, not an
independent dynamical discovery. The linear weak-field regime
restriction stands (strong-field saturation would modify the relay
bookkeeping; outside the registered regime per the 3005 §2a table).

## §4 — Verify stdout (EXECUTED, Patch 3009)

```
--- (A) CPP reading: hbar-omega packets + Moment-cadence turnover ---
 ratified pair: omega=['0.311', '0.568', '1.050', '1.782', '2.033']  eta_hat=['0.989', '1.005', '1.002', '0.992', '0.995']  slope(log eta vs log omega) = +0.00
 N-scan at k=8: rates=['10.0', '40.0', '159.1']  slope = 1.00
 PASS: eta_hat flat across a decade of omega; rate linear in N — the cancellation is real

--- (B) CONTROL-1: fixed-energy packets (breaks I-3) ---
 eps0 packets: ... slope(log eta vs log omega) = +1.00
 PASS: without E = hbar-nu packet scaling, eta is mode-DEPENDENT — I-3 is load-bearing

--- (C) CONTROL-2: omega-proportional relay cadence (breaks A3' universality) ---
 omega cadence: ... slope(log eta vs log omega) = +1.02
 PASS: without the universal Moment cadence, eta is mode-DEPENDENT — A3' is load-bearing

ALL ASSERTIONS PASS
```

**Ledger:** DM untouched; MEAS-2 at 684/1280 per founder report;
`data/kmem2` absent — dispatch-day lane armed. QM (ordinary):
OPEN-QMRG-ETA → mode-independence derived (bookkeeping grade,
touchpoint-batchable), value-only residual (c_geo); UNIQ and
W-MULTILINK-1 unchanged; bar scope untouched (panel authority).
