# QM-1 PHASE-PROVENANCE AUDIT — TODO-2957-B EXECUTED (W-7)

**Patch 2988 (4 Aug 2026).** Executes the QM-1 phase-provenance audit
registered at Patch 2957 §3 and gated ahead of AP-2 ratification by
the CONV-012 panel ruling (2979, corrected tally 2986: audit-before
UNANIMOUS 4/4). Audit method: verbatim line-cited read of the shipped
`series_quantum_mechanics/papers/QM-1_schrodinger_emergence.tex`
against the pinned founder rulings (2957 P-1..P-3) and the ratified
A1′ ontology (2982). Per the 2986 remedy, every conflict line below
cites its source line number in the shipped file; nothing is tallied
from memory.

---

## §1 — Governing standard (what the audit checks against)

- **P-1 (2957, pinned):** DI-bit content = {charge, type, ORIGIN
  ADDRESS}; **NO phase**.
- **P-2 (2957, pinned):** magnitude is COUNT-like (more DI-bits
  received ⇒ greater SSV_abs; intensity-like, not amplitude-like).
- **P-3 (2957, pinned):** synchronous cycle — absorbed one Moment,
  emitted the next; temporal synchrony is the discrete system's
  maximal "in-phase."
- **A1′ (ratified 2982):** DI-bits are one of the three Conscious
  Point types; per the GP state protocol (A3′ clause, founder text
  2958 V-2) **DI-bits RESET at every hop** — the GP imprints on every
  outgoing DI-bit; nothing accumulates on the bit across hops.
- **Registered re-grounding candidate (2957 §3, not yet derived):**
  quantum phase lives at the **DP-displacement PATTERN level** — the
  Sea's polarization configuration — with DI-bits as sub-pattern
  influence carriers.

## §2 — Conflict inventory (verbatim, line-cited)

The shipped QM-1 text attributes phase to DI-bits as carried content
at every layer of the paper:

| # | Line(s) | Shipped text (abridged) | Layer |
|---|---------|--------------------------|-------|
| C-1 | 65–68 | "hopping of **phase-carrying** Displacement Increment (DI) bits … Each DI bit **carries** a complex amplitude ψ_i = √ρ_i e^{iφ_i}" | Abstract |
| C-2 | 77 | "The imaginary unit arises physically from **DI-bit phase accumulation**" | Abstract |
| C-3 | 111–114 | "the key physical fact is that **every DI bit carries** both a density ρ and a geometric phase φ **accumulated along its path**" | §1 grounding |
| C-4 | 133–142 (Eq. phasehop) | "When a DI bit hops … **it acquires the phase** Δφ_{j→i} = m_CP c Δs / ℏ" | §2 numbered equation |
| C-5 | 181–183 | "the imaginary unit is the direct signature of **phase-carrying DI bits**" | §3, the −i justification |
| C-6 | 260–264 | "the quantum pressure Q … is the geometric interference effect of **phase-carrying DI bits** arriving from regions of different density" | §5 interpretation |
| C-7 | 286–287 | "emerges … from complex **phase-carrying DI-bit hopping**" | Conclusion |
| C-8 | glossary `master_glossary.md` line 62 | "DI-bits carry phase, amplitude, and polarisation. The DI-bit hopping amplitude determines the Schrödinger equation (QM-1)." | Registered corpus (flagged 2982) |

**Every one of C-1..C-8 contradicts P-1.** C-4 additionally
contradicts A1′'s reset-per-hop clause independently of the phase
question: even if DI-bits carried a phase register, per-hop
accumulation is impossible content for an entity that resets at every
hop. Eq. (phasehop) as a per-bit statement is false twice over in
the current ontology.

## §3 — Separability analysis (what the mathematics actually uses)

The derivation chain of the paper's central result
(Theorem "Schrödinger equation from DI-bit hopping," lines 201–228) is:

1. **Definition (line 123–131):** a complex field ψ_i = √ρ_i e^{iφ_i}
   defined **at each Grid Point** — a SITE field.
2. **Evolution equation (Eq. evolution, lines 163–168):** a
   tight-binding unitary update ψ_i(t+Δt) = ψ_i − (iΔt/ℏ) Σ_j H_ij ψ_j
   with nearest-neighbour H_ij and T = ℏ²/(4mΔs²).
3. **Graph Laplacian (Appendix A):** Σ_{j∼i}(ψ_j − ψ_i) = 2Δs²∇²ψ +
   O(Δs⁴), with z/(2d) = 12/6 = 2 a property of the 600-cell.
4. **Continuum limit:** iℏ ∂ψ/∂t = −(ℏ²/2m)∇²ψ + Vψ.
5. **Madelung decomposition (§5):** continuity + quantum
   Hamilton–Jacobi with Q = −ℏ²∇²√ρ/(2m√ρ).

**Finding S-1 (spine independence).** Steps 1–5 consume: a complex
site field, a unitary neighbour-coupled update, and 600-cell
coordination geometry. **No step consumes per-bit carried phase.**
The per-hop phase equation (C-4, Eq. phasehop) is never used in the
theorem's proof: its value Δφ = m_CP/m_P does not enter T, does not
enter the Laplacian, and does not enter the continuum limit. T is
fixed by matching the kinetic operator (the paper's own Remark, lines
185–199), not derived from Eq. (phasehop). The equation is
ontological decoration relative to the proof.

**Finding S-2 (the density half already matches the pinned
content).** ρ_i is defined as "DI-bit number density" (line 128) and
enters only as a count — this is EXACTLY P-2's count-like magnitude
(the SSV_abs register). Half of ψ is already correctly grounded
under the founder's ruling. Only the phase half φ_i is mis-attributed.

**Finding S-3 (what genuinely dies).** The paper's central
"not-postulated" claim — that the imaginary unit "arises physically
from DI-bit phase accumulation" (C-2, C-5) — is the grounding layer,
and it dies with P-1. Under the current ontology, QM-1's −i is
**postulated pending derivation**, not derived. This is a real
demotion of the paper's headline claim, parallel in kind to the SR-1
Geometric Insufficiency Theorem demotion (theorem → proposition when
a step was found unsupported). No rescue-by-reinterpretation is
performed here: the shipped mechanism-attribution is RETIRED, not
"refined."

## §4 — Verdict (three parts)

**V-1 — The shipped grounding is RETIRED.** The per-bit
phase-accumulation picture (C-1..C-7) cannot stand under P-1 + A1′.
Eq. (phasehop) as a statement about DI-bit content is withdrawn from
the corpus's reliable layer.

**V-2 — The mathematical result is DEMOTED TO CONDITIONAL, not
falsified.** The theorem chain (S-1) survives re-grounding intact
IF a substrate origin is supplied for (a) the complex-valued site
state and (b) the unitary (−i) update. The registered candidate
(2957 §3) is the DP-displacement PATTERN level: φ_i as a variable of
the local Sea polarization configuration held/refreshed in GP state
per A3′, with DI-bits as the count-like, addressed messengers whose
arrival statistics drive the per-Moment refresh (their reset-per-hop
nature is then a feature, not a bug: the pattern persists at the
sites; the messengers are stateless couriers). Natural hook for (b):
QM-1's own opening (lines 106–110) — the substrate has NO diffusive
or stochastic process; deterministic, conserved PCD displacement is
reversibility, and a reversible conserved update on a complex site
field is unitary. Neither (a) nor (b) is derived here; both are
registered as the revision's derivation obligations. Status of the
QM-1 Schrödinger result until then: **CONDITIONAL on
OPEN-QM-1-REGROUND** (§5).

**V-3 — AP-2 is CLEARED for ratification.** The gate question
(2979/2986: does ratifying no-phase DI-bit content contradict shipped
physics?) is answered NO at the mathematics layer: no shipped
derivation CONSUMES DI-bit phase (S-1); the conflict lives entirely
in attribution prose and one decorative equation, repaired by a
registered paper revision. Ratifying AP-2 does not build on sand —
withholding it would leave the corpus carrying an ontology (glossary
C-8) the founder has explicitly denied.

## §5 — Registrations

- **OPEN-QM-1-REGROUND (new, QM sector, P1):** re-derive QM-1's
  grounding at the DP-displacement pattern level: (i) substrate
  origin of the complex site state (what Sea-polarization variable
  is φ_i — candidate: local DP polarization orientation registered
  in SSV_net's directional content; physics-picture input from the
  founder welcome per PD-006, not required to open); (ii) origin of
  unitarity (reversible conserved PCD displacement → −i, replacing
  the retired per-bit accumulation argument); (iii) revise
  `QM-1_schrodinger_emergence.tex` (abstract, §1, §2 incl. Eq.
  phasehop, §3 justification paragraph, §5 interpretation,
  conclusion) with anti-erasure history notes. Until the revision
  ships, the QM-1 result carries CONDITIONAL status in the catalog.
- **Citation bar CONTINUES:** the 2957 §3 bar (QM-1 lineage not
  citable as evidence in the RELAY-MECH-1 arc) remains in force until
  OPEN-QM-1-REGROUND closes. The bar's ground shifts from "under
  audit" to "conditional pending re-grounding."
- **Downstream sweep (follow-on, P2, outside W-7's charter):** QM-2's
  Born-rule grounding cites "DI-bit interference pattern" (glossary
  line 210) and QM-2..6 + SF-6's QM-1 citations need the same
  attribution-layer check. Registered as TODO-2988-A; expected
  outcome similar in kind (pattern-level relocation), but not
  audited here.

## §6 — STAGED TODO-2957-A EDIT (executes at AP-2 ratification, verbatim-ready)

Replacement for the `master_glossary.md` DI-bit entry (removes the
2982 editorial flag; anti-erasure history note included):

> ### DI-bit (Displacement Increment)
>
> One of the **three types of Conscious Points** (A1′, ratified Patch
> 2982): the messenger type. Content = **{charge, type, origin
> address}** (founder ruling 2957 P-1, ratified as AP-2). Magnitude
> is **count-like**: more DI-bits received by a GP ⇒ greater SSV_abs
> (P-2; intensity-like, not amplitude-like). Cycle is synchronous:
> absorbed one Moment, emitted the next (P-3) — temporal synchrony is
> the discrete system's maximal "in-phase." DI-bits are stateless
> couriers: they **reset at every hop** and are re-imprinted by the
> emitting GP (A3′ state protocol, founder text 2958 V-2). DI-bits
> carry **no phase**; quantum phase lives at the DP-displacement
> pattern level (the Sea's polarization configuration) — see
> OPEN-QM-1-REGROUND for the derivation obligation. *History note
> (anti-erasure): the pre-2957 entry read "DI-bits carry phase,
> amplitude, and polarisation. The DI-bit hopping amplitude
> determines the Schrödinger equation (QM-1)." That text was
> superseded by founder ruling 2957 P-1 and the Patch 2988
> phase-provenance audit; QM-1's Schrödinger result is conditional
> on pattern-level re-grounding, per
> `series_quantum_mechanics/qm1_phase_provenance_audit.md`.*

Also at execution: the acronym-table line 26 short definition is
consistent as-is ("fundamental quantum of information/energy
transfer") and needs no edit.

## §7 — RATIFICATION REQUEST (founder mechanical action)

The audit gate is cleared. **Requested: one word on AP-2** (DI-bit
content = {charge, type, origin address}, count-like magnitude, no
phase, synchronous absorb/emit — the panel-endorsed text at 2977,
endorsement corrected 4/4 at 2986). On "approve": the §6 glossary
edit executes and TODO-2957-A closes with full provenance.

## §8 — Ledger

Nothing moves: six of seven; PR7 PARTIAL (1B OPEN, gated
C-5(i–iii)-review + MEAS-2); B7 holds; Candidate (B) 79.5%
PROVISIONAL-FAVORABLE; 2855 PROVISIONAL; d_DP ceiling ACTIVE; nothing
minted. New: TODO-2957-B EXECUTED; OPEN-QM-1-REGROUND opened;
TODO-2988-A opened; QM-1 result → CONDITIONAL; AP-2 ratification
request issued; TODO-2957-A staged.
