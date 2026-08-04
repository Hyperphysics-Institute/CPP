# QM-2..6 + SF-6 PHASE-ATTRIBUTION SWEEP — TODO-2988-A EXECUTED

**Patch 2995 (4 Aug 2026).** Executes the downstream sweep registered at
Patch 2988 §5 (follow-on to the QM-1 phase-provenance audit, W-7).
Method fixed by the 2988 precedent
(`series_quantum_mechanics/qm1_phase_provenance_audit.md`): per paper,
(1) a line-cited conflict inventory against the pinned founder rulings
P-1..P-3 (2957) and the ratified A1′ ontology (2982) with the AP-2
content clause (2989); (2) a separability analysis — does any PROOF
consume per-bit carried phase, or is the attribution prose-only; (3) a
verdict per paper: **clean / prose-layer / math-layer**. Every conflict
line cites its source line number in the shipped file; nothing is
tallied from memory (tally-from-verbatim-only, per the 2986 remedy).

**Governing standard** (unchanged from the 2988 audit §1): P-1 DI-bit
content = {charge, type, origin address}, NO phase; P-2 count-like
magnitude (intensity-like, not amplitude-like); P-3 synchronous
absorb/emit cycle; A1′ DI-bits are the third CP type, stateless
couriers that RESET at every hop; re-grounding candidate = phase at the
DP-displacement PATTERN level (2957 §3, now the derivation obligation
of OPEN-QM-1-REGROUND).

---

## §1 — QM-2 (`QM-2_superposition.tex`, v1.1)

### Conflict inventory

| # | Line(s) | Shipped text (abridged) | Layer |
|---|---------|--------------------------|-------|
| Q2-C1 | 62–65 | "coherent summation of **phase-carrying** Displacement Increment (DI) bits" | Abstract |
| Q2-C2 | 65–67 | "**Each DI bit** emitted from source vertex $s$ **accumulates** a deterministic geometric phase $\phi_k$ along path $k$" | Abstract |
| Q2-C3 | 139–147 (Eq. phaseedge) | "The phase per edge is $\Delta\phi_{\rm edge} = m_{\rm CP}c\Delta s/\hbar + V_{\rm SSV}\Delta t/\hbar$ … Summing along path $k$ gives the total action phase $\phi_k = S_k/\hbar$" | §2 numbered equation |
| Q2-C4 | 296 | "coherent summation of **phase-carrying DI bits** along all lattice paths" | Conclusion |

Q2-C2 contradicts P-1 AND A1′'s reset-per-hop clause independently
(per-bit accumulation is impossible content for a stateless courier) —
the same double contradiction as QM-1's C-4. Q2-C3 is the QM-1
Eq. (phasehop) reprised with a potential term. Notably, the Plain
Language Summary (line 88) is already near-compliant: "**Each path
picks up a phase** from the lattice geometry" — path-level, not
bit-level.

### Separability analysis

The derivation spine is: per-path amplitude $A_k = A_0 e^{i\phi_k}$
(Eq. Ak, lines 129–136) → coherent sum $\psi(d) = \sum_k A_0
e^{i\phi_k}$ (Eq. sum, 166–170) → interference (Eq. interference,
173–181) → Born rule (Theorem 4.1, 200–210) → Schrödinger continuum
limit (§7).

**Finding Q2-S1 (the phase is a PATH functional, not a bit
register).** Mathematically, $\phi_k = S_k/\hbar$ is an action
functional of the path geometry and the SSV potential along it. No
step of the mathematics reads or writes state on an individual DI-bit;
the sum is indexed by paths, not by bit identities. The attribution of
$\phi_k$ to bit-carried content is entirely prose.

**Finding Q2-S2 (Eq. phaseedge is LOAD-BEARING — the one substantive
difference from QM-1).** Unlike QM-1's decorative Eq. (phasehop), the
per-edge phase (Q2-C3) IS consumed: the interference results, fringe
positions, and the SSV which-path prediction (Eq. ssvphase) all
consume $\phi_k$'s value. But it is consumed AS a per-path action
functional. In revision, Eq. (phaseedge) is **re-labeled, not
withdrawn**: $\Delta\phi_{\rm edge}$ becomes the per-edge phase
advance of the propagating Sea-polarization pattern (the pattern
traverses the edge; the phase is a property of the pattern's
configuration history, with DI-bits as the stateless messengers whose
per-Moment arrival statistics refresh the GP-held state per A3′).

**Finding Q2-S3 (Born-rule proof already P-2-compliant).** The
Theorem 4.1 proof (lines 204–210) consumes ONLY $P \propto
\rho_{\rm bit}$ (companion C3) and the identity $\rho_{\rm bit} =
|\psi|^2$. The density is a count — exactly P-2. No phase is consumed
by the proof; the non-circularity remark (lines 212–218) survives
unchanged, since $A_0$ and $\phi_k$ remain probability-independent
under the pattern-level reading.

### Verdict: **PROSE-LAYER**

The theorem chain survives re-grounding intact. Revision obligations:
abstract + conclusion attribution language (Q2-C1/C2/C4); Eq.
(phaseedge) re-labeled at pattern level (Q2-S2). Status:
**lineage-CONDITIONAL on OPEN-QM-1-REGROUND** (the site field $\psi$
and the substrate origin of its phase are inherited from the QM-1
lineage).

---

## §2 — QM-3 (`QM-3_bell_entanglement.tex`)

### Conflict inventory

| # | Line(s) | Shipped text (abridged) | Layer |
|---|---------|--------------------------|-------|
| Q3-C1 | 64–66 | "A spin-$\tfrac12$ CP aggregate carries a two-component **DI-bit state whose phase** encodes the spin direction via the ZBW helix" | Abstract |
| Q3-C2 | 67–68, 134, 138, 174, 290 | "joint **DI-bit state**" (naming, five sites) | Abstract, §3 header, Eq. context, figure caption, Conclusion |

**Counter-indication on record:** lines 166–167 state "The joint state
is a property of the global Nexus ledger, **not carried locally by
either particle**." The shipped paper itself already disclaims local
carriage — the conflict is a naming convention, not an ontological
commitment.

### Separability analysis

**Finding Q3-S1.** The entire proof chain — non-separability
(Theorem 3.1, lines 146–161: coefficient-matching algebra), singlet
correlation (Proposition 4.2, 197–205: arithmetic), CHSH/Tsirelson
(Theorem 5.1, 211–226: substitution), no-signaling (Theorem 6.1,
247–257: marginalization) — is Hilbert-space algebra on a two-qubit
state plus the Born rule (companion C3). NOTHING consumes per-bit
content of any kind. The qubit state is an aggregate-level object by
the paper's own words (Q3-C1: "CP **aggregate** carries"); the
ZBW-helix spin encoding (companion C4) is a configuration-level
statement — already pattern-level in kind.

### Verdict: **PROSE-LAYER** (lightest of the five)

Revision obligation: rename "DI-bit state" → pattern-level state
(aggregate/Sea-polarization state) at the five naming sites; one
abstract clause. Status: **lineage-CONDITIONAL** through the Born-rule
citation only.

---

## §3 — QM-4 (`QM-4_measurement_problem.tex`)

### Conflict inventory

| # | Line(s) | Shipped text (abridged) | Layer |
|---|---------|--------------------------|-------|
| Q4-C1 | 65–66 | "decoheres the coherent **DI-bit state**" | Abstract |
| Q4-C2 | 110–112 | "the **DI-bit state** couples to the thermal DP Sea, whose random phase kicks destroy off-diagonal coherences" | §1 |
| Q4-C3 | 148 | "the reduced density matrix of the **DI-bit qubit**" | Theorem 3.1 statement |
| Q4-C4 | 203–204 | "the **DI-bit states** of definite phase projection onto the local SSV direction" | Theorem 4.1 statement |
| Q4-C5 | 229 | "An arbitrary **DI-bit state** $\ket{\psi}$ on the Bloch sphere" | Figure caption |

### Separability analysis

**Finding Q4-S1.** The Lindblad derivation (Theorem 3.1, lines
145–169) consumes: the dephasing coupling $H_{\rm int}$ (Eq. Hint),
the Born–Markov approximation, bath correlation collapse at
$\tau_{\rm corr} = t_P$. The pointer-basis proof (Theorem 4.1, lines
207–215) consumes commutation with $\hat\sigma_z$. The
global-unitarity proof (Theorem 6.1, 274–280) consumes Hermiticity +
Nexus conservation. All are operator-level statements on a qubit
density matrix — the system state whose substrate identity is
inherited, not constructed here. The "random phase kicks" (Q4-C2) are
bath-interaction phases acting ON the pattern-level state; no per-bit
phase register is consumed anywhere.

### Verdict: **PROSE-LAYER** (naming only, same class as QM-3)

Revision obligation: the five naming sites. Status:
**lineage-CONDITIONAL** through the QM-1/C3 inheritance.

---

## §4 — QM-5 (`QM-5_qft_emergence.tex`)

### Conflict inventory

| # | Line(s) | Shipped text (abridged) | Layer |
|---|---------|--------------------------|-------|
| Q5-C1 | 63–66 | "collective excitation modes of complex **phase-carrying DI bits** … The **DI-bit amplitude** $\psi_i = \sqrt{\rho_i}e^{i\phi_i}$" | Abstract |
| Q5-C2 | 106–107 | "collective excitations of **phase-carrying DI bits**" | §1 |
| Q5-C3 | 117–118 | "At each Grid Point $i$ the **DI-bit state** is $\psi_i = \sqrt{\rho_i}e^{i\phi_i}$ (Paper 2)" | §2 |

**Compliance notes (not conflicts):** line 145 "$\hat c_i$ annihilates
a DI bit at site $i$" — the operator acts on the site OCCUPATION
number, which is a count (P-2-compliant); lines 207–217 the
fermion–boson theorem consumes occupancy restrictions and SSV
self-repulsion, both count/charge-level.

### Separability analysis

**Finding Q5-S1.** The eigenmode expansion consumes: a complex site
field (inherited from Paper 2), the adjacency matrix's real-symmetric
orthonormality, and the site operator algebra $[\hat c_i, \hat
c_j^\dagger] = \delta_{ij}$. The commutator theorem's proof (lines
186–191) consumes ONLY eigenvector orthonormality. **The shipped
paper carries its own separability remark** (lines 195–198, Remark
4.2): "The commutation relations follow purely from eigenmode
orthonormality. **No appeal to '120°/240° phase geometry' is
needed.**" The Pauli/boson split consumes charge + SSV repulsion, not
phase. No proof consumes per-bit carried phase.

### Verdict: **PROSE-LAYER**

Revision obligation: the three attribution sites (Q5-C1/C2/C3 —
"phase-carrying DI bits" → pattern-level phrasing; "DI-bit amplitude/
state" → site-field naming under the re-grounded ontology). Status:
**lineage-CONDITIONAL** (the site field is the Paper-2 inheritance).

---

## §5 — QM-6 (`QM-6_capstone.tex`)

### Conflict inventory

| # | Line(s) | Shipped text (abridged) | Layer |
|---|---------|--------------------------|-------|
| Q6-C1 | 64–66 | "four primitives: Conscious Points (CPs), **phase-carrying** Displacement Increment (DI) bits, the 600-cell lattice, and the Nexus" | Abstract |
| Q6-C2 | 111–114 | Primitive #2: "DI bits: **Relational quanta exchanged between CPs, carrying both density $\rho$ and geometric phase $\phi$**. The complex amplitude … encodes the full **DI-bit state**" | §1 PRIMITIVE DEFINITION |
| Q6-C3 | 133 | "DI bits hop with **phase accumulation** $\Delta\phi = m_{\rm CP}c\Delta s/\hbar$" | §2.1 — verbatim reprise of the RETIRED QM-1 Eq. (phasehop) |
| Q6-C4 | 121–123, 197 | Nexus enforces "total **phase circulation**" / "Phase circulation (winding number)" | §1 primitive #4, Table 1 |
| Q6-C5 | 91 | "**DI-bit amplitudes**" as one of the four ingredients | Plain Language Summary |

Q6-C2 conflicts TWICE with A1′: (a) phase content contradicts
P-1/AP-2; (b) "relational quanta exchanged between CPs" contradicts
A1′'s type classification — DI-bits ARE the third CP type, not a
relational quantum passed between CPs. Q6-C3 reprises the doubly
contradicted, withdrawn per-bit equation. Q6-C4's "phase circulation"
conservation is re-attributable to the pattern level (the winding
number of the site-field configuration) — a relocation, not a retirement.

### Separability analysis

**Finding Q6-S1.** QM-6 is a synthesis capstone with NO independent
proofs: every equation is a reprint from Papers 2–6 (verified: §2.1
reprints QM-1's chain; §2.2 QM-2's sum; §2.3–2.5 state prior
theorems without proof). Its mathematics layer is derivative and is
covered by the per-paper separability findings above plus the 2988
audit's S-1.

**Finding Q6-S2 (severity).** The conflict lives at the
**PRIMITIVE-DEFINITION layer**: §1's four-primitives list is the QM
series' normative ontology statement, and it now states, as
foundation, content the programme has formally denied (P-1 pinned
2957; AP-2 ratified 2989; A1′ ratified 2982). This makes QM-6 the
**highest-severity revision target among QM-2..6** even though nothing
in it is load-bearing mathematics: any reader entering the series
through the capstone receives the retired ontology as the axioms.

### Verdict: **PROSE-LAYER, PRIMITIVE-DEFINITION severity**

Revision obligation: rewrite §1's four primitives under A1′/AP-2
(three CP types; DI-bits as stateless couriers with content {charge,
type, origin address}; count-like magnitude; phase at the
DP-displacement pattern level); strike or re-attribute line 133;
relocate "phase circulation" to the pattern level; abstract + PLS
sweep. Status: **lineage-CONDITIONAL** (wholly derivative).

---

## §6 — SF-6 (`flagship_papers/electromagnetism/sf-6_electromagnetism.tex`, v1.0 SHIPPED)

### Conflict inventory

**NONE.** Full grep of every DI-bit mention (lines 117, 232, 238, 303,
305) and every phase mention (79, 165, 232, 268) finds no per-bit
phase attribution:

- Line 117: CPs "exchange displacement-increment (DI-bit)
  **information** along SSV gradients" — no content claim beyond
  information transfer.
- Line 165: "the instantaneous spatial **pattern of DP alignment,
  density, and phase** is imprinted into the outgoing Grid-Point
  network" — phase attributed to the DP-alignment PATTERN held in the
  GP network. **This IS the 2957 §3 re-grounding candidate ontology.**
- Line 232: the photon is "a **phase-coherent SSV distribution**
  across the GP network, reconstructed each Absolute Moment by the
  vector summation of DI-bit strings" — phase at the
  distribution/pattern level; DI-bits as per-Moment-summed messengers
  (P-3-consistent synchrony).
- Line 238: "any DI-bit **amplitude configuration** expands over the
  lattice eigenvectors" — configuration-level phrasing for the QM-5
  site-field bridge; carries the lineage condition but asserts no
  per-bit content.

### Separability analysis

SF-6 is a synthesis flagship with **no new derivation** (its own §1,
line 114, and the catalog registration both state this). Its exposure
to the retired grounding is **citation-only**: it inherits "the QED
phenomena" from QM-1..6 (lines 79, 114, 117, 230) and the
second-quantization bridge from QM-5 (line 238).

### Verdict: **CLEAN** (attribution layer); lineage-conditional by citation only

No text change required. At the paper's next natural touch, an
optional one-line lineage footnote can note that the QM-series QED
inheritance is conditional on OPEN-QM-1-REGROUND; nothing in SF-6's
own claims moves either way.

**Finding SF6-A1 (ASSET — registered for OPEN-QM-1-REGROUND).**
SF-6's shipped, panel-reviewed, v1.0 language is a **ready-made
template for the QM-1 re-grounding**: the traveling-pattern photon
ontology — phase in the DP-alignment configuration imprinted in the GP
network, advanced per Absolute Moment, reconstructed by per-Moment
DI-bit-string summation — is precisely the pattern-level grounding
OPEN-QM-1-REGROUND must supply for the matter-sector site field. The
revision does not start from a blank page; it ports an already-shipped
flagship ontology from the EM sector to the QM sector.

---

## §7 — Sweep-level findings

**F-SW-1 (uniform conflict class; the S-1 separability propagates).**
Across all five QM papers, NO proof consumes per-bit carried phase.
The conflict class is uniform: attribution prose + inherited
site-field naming. The 2988 audit's Finding S-1 (spine independence)
propagates to the entire series: **the QM sector's mathematics
survives re-grounding intact.** No paper is math-layer contaminated.

**F-SW-2 (one load-bearing equation outside QM-1).** QM-2's Eq.
(phaseedge) is the sweep's only load-bearing phase equation — consumed
by the interference and which-path predictions — but load-bearing as a
per-PATH action functional, re-labelable at pattern level (Q2-S2).
QM-6 line 133 reprises the RETIRED per-bit form of QM-1's
Eq. (phasehop) and must be corrected, but is decorative there
(capstone reprint, Q6-S1).

**F-SW-3 (severity ordering).** QM-6 §1 (four-primitives list) is the
highest-severity site: primitive-definition layer, directly
contradicting ratified AP-2/A1′ twice over (phase content + type
misclassification). Then QM-2 (abstract accumulation claim + the
re-label obligation), then QM-5, then QM-4/QM-3 (naming only).

**F-SW-4 (SF-6 clean; supplies the template).** SF-6 needs no
revision and its shipped ontology is the re-grounding template
(SF6-A1). The expected outcome registered at 2988 §5 ("similar in
kind") is confirmed for the QM papers and BETTERED for SF-6.

**F-SW-5 (glossary Born Rule entry — the known target confirmed).**
`master_glossary.md` "Born Rule" entry (≈ line 211): "emerges from the
DI-bit interference pattern … the squared **amplitude of the DI-bit
field**" — amplitude-like language contradicting P-2. QM-2's actual
proof is already P-2-compliant ($P \propto \rho$, a count; Q2-S3); the
glossary OVERSTATES the shipped mathematics. Relocation: probability
from count-like DI-bit density, whose spatial interference structure
is set by the pattern-level phase. Edit rides the OPEN-QM-1-REGROUND
revision pass (same anti-erasure discipline as the 2989 DI-bit entry
edit).

**F-SW-6 (revision economics — the sequencing note pays off).** One
coherent revision pass, in order: (1) QM-1 re-ground (supplies the
pattern phase variable + the unitarity origin — the two derivation
obligations); (2) QM-6 primitives rewrite (the normative statement);
(3) QM-2 Eq. re-label + prose; (4) QM-5, QM-4, QM-3 naming sweeps
(light); (5) glossary Born Rule entry; (6) SF-6 — no change (optional
footnote at next touch). This confirms the 2993 handover's sequencing
rationale: sweep-first means one pass fixes the whole lineage
coherently instead of per-paper piecemeal.

---

## §8 — Registrations

- **TODO-2988-A EXECUTED, CLOSED** (this record).
- Per-paper statuses registered in `paper_catalog.md` (QM series
  section note + SF-6 row lineage sentence).
- **OPEN-QM-1-REGROUND scope CONFIRMED, not widened:** the sweep adds
  no new derivation obligations beyond the 2988 registrations (pattern
  phase variable; unitarity origin; QM-1 revision). It ADDS the
  downstream revision inventory (QM-2..6 sites listed above + glossary
  Born Rule entry) to the same revision pass, and the SF6-A1 template
  asset. Entry registered in `frontier_sectors/QM.md` (the sector
  file; previously tracked only in FP.md status blocks).
- **Citation bar unchanged:** the QM-1 lineage remains not-citable in
  the RELAY-MECH-1 arc until the re-grounding revision ships (2957 §3;
  ground per 2988: "conditional pending re-grounding").

## §9 — Ledger

Nothing moves: six of seven; PR7 PARTIAL (1B OPEN, gated on CONV-013);
B7 holds; Candidate (B) 79.5% PROVISIONAL-FAVORABLE; 2855 PROVISIONAL;
d_DP ceiling ACTIVE; nothing minted. New: TODO-2988-A EXECUTED;
QM-2..6 → lineage-CONDITIONAL (prose-layer); SF-6 → CLEAN
(lineage-conditional by citation); SF6-A1 template asset registered
for OPEN-QM-1-REGROUND. Open P1s: OPEN-QM-1-REGROUND (next queue
item). Campaign RUNNING (dispatch-day lane untriggered; `data/kmem2`
not present at this patch).
