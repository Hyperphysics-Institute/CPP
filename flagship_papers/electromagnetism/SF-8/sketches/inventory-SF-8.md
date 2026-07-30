# SF-8 — MEASUREMENT INVENTORY WITH PER-RESULT PROVENANCE (Patch 2877)

**Charter §5 action 1, executed.** *"Assemble the measurement record from
the S4-X / AUTOMATON arc records into a `sketches/` inventory with
per-result patch provenance."* No draft text is produced here and none
should be until this inventory is checked — every load-bearing number
below is quoted with the file and line it comes from, per CONV-003 and
per the 2856 mitigation.

**PANEL INSTRUCTION ON STRUCTURE, ALREADY GIVEN.** At the win-packet
adjudication (`conv001_2026-07_win_packet_returns_adjudication.md` line
20) item **W6 returned 5–0 with a unanimous lead recommendation:
"paper, lead Coulomb."** All five seats. **SF-8 opens on the emergent
electrostatics result.** This is not the worker's structural preference;
it is a ratified panel instruction and it is recorded here so the drafting
step does not rediscover or quietly override it.

**A NOTE ON PATHS.** Every script and record for this paper lives in the
**dark-matter sector**, not in `flagship_papers/electromagnetism/`. The
AUTOMATON arc was executed under the DM campaign and its artifacts stayed
there. SF-8 must therefore cite cross-sector paths, and any verification
package shipped with the paper must either reference those paths or vendor
copies with provenance stated. **Flagged now because it is the kind of
thing that gets silently mis-cited at draft time.**

---

## §1 — RESULT 1: EMERGENT INVERSE-SQUARE ELECTROSTATICS (the lead result)

**Claim.** The founder's Moment rule — synchronous GP relay of DI-bits
carrying charge, polarity and origin only; d = (|SSV_net|/SSV_abs)·PSR —
produces Coulomb's law with **no field law as input**, under **two
independent relay implementations**.

### Relay A — idealized PSR shell (AUTOMATON-1, run V-1R)

| item | value | source |
|---|---|---|
| agreement with exact torus Coulomb | **±2.9% pointwise** | `automaton1_execution_record.md:78` |
| fitted-exponent gap vs the reference | **Δp ≤ 0.022** | `automaton1_execution_record.md:78` |
| replication | **3/3 R** | `automaton_arc_closure.md:14–17` |
| engine | `series_phenomena/cosmology/dark_matter/code/2797_automaton1_engine.py` | — |
| deliverables | `.../code/2799_automaton1_deliverables.py` | — |
| relay diagnostics | `.../code/2800_relay_diagnostics.py` | — |
| pre-registration (re-issued) | `automaton1_v1r_reprereg.md` | — |
| standing | *"leg 2, ±2.9% shape, Δp ≤ 0.022, **stands**"* | `automaton1_execution_record.md:166` |

### Relay B — lattice-native origin-directed 12-neighbour icosahedral hop (AUTOMATON-2, gate G1)

| hop count R | normalized ρ range | Δp | source |
|---|---|---|---|
| R = 2 | [0.986, 1.044] | 0.052 | `automaton2_execution_record.md:12` |
| R = 3 | [0.991, 1.004] | 0.011 | `automaton2_execution_record.md:12–13` |
| **R = 4** | **[0.996, 1.002]** | **0.010** | `automaton2_execution_record.md:13` |

**→ ±0.4% pointwise at R = 4; prediction P-A2-1 CONFIRMED**
(`automaton2_execution_record.md:17`). **Agreement TIGHTENS with hop
count** — the R = 2 → 3 → 4 progression above is the evidence for that
claim and should be presented as the progression rather than as the
endpoint alone. Engine:
`.../code/2802_automaton2_engine.py`.

### ⚠ CORRECTION TO THIS INVENTORY, PATCH 2878 — Δp WAS MIS-DEFINED ABOVE AT 2877

**Δp is NOT a "polarity/shape discriminant"**, which is how this file
described it when first written. Its frozen definition
(`automaton1_v1r_reprereg.md`, V-1R pass bands) is:

> **Δp ≡ |p_auto − p_Ewald| ≤ 0.15 on the window**

i.e. **the gap between the automaton's fitted power-law exponent and the
EWALD REFERENCE's exponent on the same window.** Corrected in the table
above.

**AND THE CONSEQUENCE IS THE SHARPEST PRESENTATION HAZARD IN THIS PAPER.
Exact torus Coulomb on this geometry has p = 2.291, NOT 2**
(`automaton1_v1r_reprereg.md:12–15`; `automaton1_execution_record.md:60–64`)
— a property of the periodic boundary plus the neutralising background, not
of the automaton. Two consequences:

1. An early gate band of [1.8, 2.2] on the exponent **was unsatisfiable
   by ANY Coulombic field on this geometry**, which is why the Patch 2797
   FAIL was reclassified a **GATE-DESIGN defect** rather than a defect of
   the implementation.
2. **SF-8 MUST NOT CLAIM A MEASURED EXPONENT OF 2, and must not let
   "emergent inverse-square" be read as one.** The tested quantity is
   agreement with the exact Coulomb solution *for the geometry simulated*
   — which is the correct comparison and strictly more demanding than
   fitting a free-space power law.

**Also load-bearing and easy to lose:** ρ is normalised by its own window
mean because *"the relay's amplitude unit is conventional."* **No coupling
constant is predicted by either relay.** Only the radial SHAPE is
measured. Pre-registered bands were ρ ∈ [0.90, 1.10] pointwise and
Δp ≤ 0.15 at ≥ 2 of 3 R values; both relays land far inside them, and
saying so is stronger than quoting the achieved figures alone.

**Blinding, for the record:** R = 3 was CONFIRMATORY-DISCLOSED (already of
record at freeze); **R = 2 and R = 4 were BLIND.**

### The external reference both were measured against

**Ewald comparator, `.../code/2798_ewald_comparator.py`:** V-1b validated
to **worst deviation 0.856% vs free space over r ∈ [3, 6], three
directions** (`automaton1_execution_record.md:60`;
`automaton1_v1r_reprereg.md:11`). **This is the anchor that makes both
relay numbers meaningful and it must appear in the paper — a percentage
agreement against an unvalidated reference is not a measurement.**

### Ratification and limitation status

- **W1 and W2 RATIFIED 5–0**; W6 5–0 unanimous lead
  (`conv001_2026-07_win_packet_returns_adjudication.md:15–16, 20`).
- **EXEMPT from L-1, L-2 and L-3 by L-4**, verbatim: *"Coulomb and
  ZBW-Sea results are exempt from L-1..L-3 — they were established under
  blocking gates with verified external references and are unaffected by
  the momentum question"* (`automaton_arc_closure.md:80–82`). **This
  exemption is why SF-8 is ungated, and it should be stated in the paper
  rather than assumed.**

## §2 — RESULT 2: THE BONDED ZBW SEA, MEASURED

| item | value | source |
|---|---|---|
| partner persistence | **100.0% at every lag to 4000 Moments** | `automaton_arc_closure.md:21–22` |
| random null | **2.0%** | `automaton_arc_closure.md:22` |
| dedicated pairs | **52/52** | `automaton_arc_closure.md:22` |
| turning radii (lattice-quantised) | **√2 and 2√2** | `automaton2_execution_record.md:140, 147` |
| oscillation period | **10–12 Moments** | `automaton_arc_closure.md:24` |
| engine | `.../code/2802_automaton2_engine.py` | — |
| scale hypothesis tests | `.../code/2805_scale_hypothesis_tests.py` | — |

**Confirms C26** (dedicated semi-persistent DP bonds), **C28** (shallow
dedicated-pair oscillation), **C25** (superposition exit as a consequence
of the one law) — `automaton_arc_closure.md:25–27`. **EXEMPT from
L-1..L-3 by L-4.**

### ⚠ ONE HAZARD ON THIS RESULT, AND IT IS THE PAPER'S SHARPEST TRAP

**The 10–12 Moment period is a LATTICE-SCALE quantity and must NOT be
transferred to the physical d_DP scale in this paper.** That transfer is
the move the DM sector's own derivation sketch calls **"the sketch's
weakest joint"** and names as such, on the grounds that *"the regime
diagnosis (Patch 2810) showed exactly how badly lattice-scale conclusions
can travel."* L-1 forbids AUTOMATON occupancy values as physical, and
whether it also forbids this period transfer is itself an open panel
question. **SF-8 reports the period as a measured property of the
automaton, full stop.** The turning radii √2 and 2√2 are likewise
lattice-quantised — they are quantised *in units of the lattice*, and
saying so is mandatory.

## §3 — RESULT 3: KINETIC RANDOMISATION IN PROXY (optional per charter, and the most dangerous to include)

| item | value | source |
|---|---|---|
| MSD exponent | **0.14 → 0.76** | `automaton_arc_closure.md:33–34` |
| collision events with axis re-randomisation | **797** | `automaton_arc_closure.md:34–35` |
| period-4 lock-in | **completely destroyed** | `automaton_arc_closure.md:35` |
| Maxwell–Boltzmann speed statistics | **decile χ² = 14.7 on 9 dof** | `automaton2_execution_record.md:390`; `automaton_arc_closure.md:36–37` |
| coefficient of variation | **0.409–0.513 bracketing MB's 0.422** | `automaton_arc_closure.md:37` |
| panel status | **W5′ RATIFIED 5–0, "L-1 emphasized"** | `conv001_2026-07_win_packet_returns_adjudication.md:19, 60` |

**TWO CONSTRAINTS, BOTH MANDATORY IF THIS SECTION IS INCLUDED:**

1. **L-2 binds it:** *"thermal claims are mechanism-level only. The MB
   speed statistics of §1.3 establish that momentum unlocks
   thermalisation; they do NOT establish Gibbs equilibrium, and must
   never be cited as satisfying PR4 or P-A2-3"*
   (`automaton_arc_closure.md:72–75`).
2. **The momentum was supplied as a LABELLED PROXY for C23 arc inertia,
   not derived from it** (`automaton_arc_closure.md:30–32`). The runs are
   a **driven system** with no back-reaction, in which kinetic energy
   grows 3.87× at η = 0.004 and 49× at η = 0.05, and **η is a coupling
   strength, not a dissipation term** (`automaton_arc_closure.md:63–68`).

**WORKER RECOMMENDATION: include it, briefly, and in a subsection whose
own heading carries the proxy caveat.** It is genuine and ratified, and
omitting it would understate the arc. But it is the one result in this
paper that a hostile reader could mistake for a thermal-equilibrium
claim, and W5′'s ratification came with L-1 *doubly* emphasised.

## §4 — RESULTS 4 AND 5: AVAILABLE, AND WHY THEY ARE NOT SF-8 MATERIAL

- **Zero-agitation limit** — the bare rule quenches (A1 NOT-GIBBS, 3/3
  R), retained as the correct T → 0 behaviour any successor must
  reproduce (`automaton_arc_closure.md:38–41`). **Citable in one
  sentence** as a consistency check; not a headline.
- **Regime map** — 13 CPs per PSR gives a frozen 1447-CP condensate while
  325 CPs per PSR gives no clusters and universal motion; condensation,
  crystallites, planar ± sheets and parked singletons are **artifacts of
  PSR/spacing ≈ 1.5 and the ½-GP displacement snap**
  (`automaton_arc_closure.md:42–44`). **EXCLUDE from SF-8's claims.**
  **L-3:** *"No crystallite, sheet, cluster, or chaining conclusion from
  this arc transfers to the physical Sea"*
  (`automaton_arc_closure.md:76–79`).

## §5 — THE EXCLUSION LIST THAT BINDS DRAFTING

Charter §2, plus one item added since the charter was written.

| excluded | authority |
|---|---|
| **Any magnetic claim.** The curl derivation (2842) and its normalisation (2843/2846) are **derived, not measured**; OPEN-C23-MAGNETIC-SECTOR-VALIDATION is open. | charter §2 |
| **"Transverse" as a description of the arc.** The arc is **LONGITUDINAL**; the transverse gloss was a 5–0 panel error corrected by founder ruling at Patch 2856, and the open item was renamed accordingly. Use corrected **C23-R** language if the arc is referenced at all. | charter §2; `founders_voice/founder_ruling_c23_arc_longitudinal_2026-07-28.md` |
| **CPP-DARWIN and the PR7 chain** as load-bearing. | charter §2 |
| **Candidate B, the 79.5%, anything under Founder Decision B7.** | charter §2 |
| **Any characterisation of the Sea's physical density** — not dilute, not dense, not geometrically anything. SF-8 may report the Sea is *bonded and dedicated* (C26) and nothing further. | charter §2; OPEN-SEA-DENSITY-1 |
| **NEW — the SF-6 pin's F = κa as a CPP substrate-mechanism result.** Demoted 4–0 to a scalar-toy analogue pending OPEN-FSELF-CORRESPONDENCE-1. SF-8 **may** cite the statics-pinned κ = (2/3)U/c² as a result, and **may** cite the toy result *as* a toy result. | Patch 2876 §4, §8 |

## §6 — THE HONESTY CONSTRAINT, RESTATED AS A DRAFTING RULE

Charter §3: the scalar sector is measured, the transverse/magnetic sector
is not, and **the abstract itself must say so** rather than letting a
reader infer that electromagnetism as a whole has been derived from the
substrate. SF-6 already ships the unification claim; **SF-8 supplies the
substrate measurement for one half of it and names the other half as
open.**

**Operationally: the abstract must contain an explicit negative clause.**
A reader who stops at the abstract must come away knowing the magnetic
sector is derived-but-unmeasured. This is the single most likely place for
this paper to overclaim, because "we measured Coulomb's law out of the
substrate rules" is a strong and true result that reads, to a hasty
reader, as more than it is.

## §7 — STATE AND NEXT ACTION

**Inventory complete. No draft text written. Nothing in §§1–4 is
re-derived here — every number is quoted from its record with file and
line, and the records themselves are unmodified by this patch.**

**Next: charter §5 action 2** — draft §1–§3 (substrate rules; the two
relay implementations; what was measured and to what precision), opening
on the Coulomb result per W6's unanimous instruction, with the Ewald
anchor stated before either agreement figure.

**Not yet done and needed before the panel dispatch (charter §5 action
3):** a runnable stdlib verification embedded in the review package per
CONV-003 §4. The existing engines are not stdlib-only and live
cross-sector; a self-contained verifier will have to be written rather
than referenced. **Note for that step: per Patch 2876 §7, a withheld key
must be scoped to a SINGLE self-contained artifact** — the previous round's
key was admissible and unanswerable because the diagnostic needed a
dependency no seat could fetch.
