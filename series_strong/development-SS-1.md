# Development History — SS-1: The Strong Sector from the 600-Cell Lattice

**Paper:** SS-1_strong_sector_from_600cell_lattice.tex
**Last updated:** 29 March 2026
**Purpose:** Chronological record of how the paper was developed,
what was tried, what failed, what succeeded, and why decisions
were made as they were. This file is a research provenance trail,
not a summary of results. Results are in the paper; this is the
story behind them.

---

## Phase 1: Companion Papers and Initial Architecture (pre-February 2026)

The strong sector work began as five separate companion papers
(cpp_ss1_overview_v1.tex through cpp_ss5_hadrons_v1.tex) produced
in early 2026, covering:

- SS#1: Cage geometry and eigenvalue bridge (tetrahedral cage as
  SU(3) host; 600-cell vertex adjacency eigenvalues)
- SS#2: SU(3)_c algebra — T^a = λ^a/2 exact derivation
- SS#3: Eight gluons as hDP structures
- SS#4: Confinement and the QCD β-function
- SS#5: Hadron spectrum — baryons, mesons, pion chiral limit

At this stage, the color degree of freedom was understood as vertex
identity on the tetrahedral base, and the 8-generator count had been
established via edge hopping. The companion papers were functional but
independent; they lacked the unified framing of a single submission
package and used the legacy `cpp_ss*_v1.tex` naming.

Concurrent with this: C14 (Cornell potential from qDP chaining) and
C15 (color charge from tetrahedral cage geometry) were produced as
SR-1 companion papers but carried essential strong-sector physics.
These were cross-referenced throughout the SS papers.

---

## Phase 2: Unified Submission Package v1 (February–March 2026)

`cpp_ss_unified_v1.tex` was produced as a synthesis of the five
companion papers. Key decisions made at this stage:

**Decision: Grok v1 merge.** Grok (xAI) contributed four physical
insights that were incorporated into the unified paper:
1. **1+3+4 = 8 layer-depth count** — an independent geometric count
   of gluon generators via cage architecture: 1 apex layer + 3 base
   vertices + 4 first-shell sites = 8. This confirmed the edge-hopping
   count by a completely different geometric argument.
2. **PSR saturation as the mechanism for asymptotic freedom** — the
   physical picture explaining *why* α_s → 0 at short distances.
3. **Transverse qDP oscillation language for gluons** — the
   complementary physical description alongside "open tetrahedral
   edge hDP pairs."
4. **Proton mass ≈ 99% qDP chain energy** — quantitative statement
   of this result which had been implicit but not explicitly computed.

These contributions are acknowledged in the v2 appendix and in the
`rem:two_counts` remark.

**Decision: Keep five companions + unified package.** The individual
SS#1–5 companion papers were retained in the repository as the detailed
derivation record; the unified package became the submission document.

---

## Phase 3: PS-1 Session — Shell Geometry and the C₆₀ Falsification (25 March 2026)

This session was pivotal. Thomas, Claude Sonnet (Anthropic), and Grok
(xAI) performed exact computation of the 600-cell distance-shell
structure, examining which shells could serve as the top quark's
fourth polyhedral cage.

### The C₆₀ falsification

**Prior state:** All CPP papers (SS-1, SM-1, SM-2) had used the
C₆₀ fullerene (60 vertices) as the fourth quark cage — the cage
expected to appear after the dodecahedron (20 vertices) in the
sequence tetrahedron → icosahedron → dodecahedron → ?

**The computation:** Exact enumeration of 600-cell distance shells
from a reference vertex. The shells have vertex counts:
- Shell 0: N=12 (icosahedron)
- Shell 1: N=20 (dodecahedron)
- Shell 2: N=12 (second icosahedron — duplicate vertex count)
- Shell 3: N=30 (degree-4, vertex-transitive, d²=2)
- Shell 4: N=12
- Shell 5: N=20
- (palindromic structure continues)

**Result:** No 60-vertex distance shell exists in the 600-cell.
The fullerene cage was ruled out. This was a genuine falsification —
the C₆₀ assignment had been used in multiple papers and needed to
be corrected across all of them.

**New candidate — 30-vertex shell (shell 3):**
Shell 3 was identified as the natural fourth cage candidate:
- All 30 vertices equidistant from the reference vertex ✓
- All vertices degree-4 in the 600-cell edge graph ✓
- Vertex-transitive ✓
- Shell 2 (N=12) is skipped because it has the same vertex count
  as the icosahedral (charm) cage — the cage sequence must use
  distinct vertex counts for distinct generations

The revised cage sequence: 4 → 12 → 20 → 30
(tetrahedron → icosahedron → dodecahedron → 30-vertex shell)

**Name correction — "icosidodecahedron" removed:**
An earlier draft had named shell 3 as the "icosidodecahedron."
Claude Opus (Anthropic), in the pre-submission review, correctly
caught that the actual icosidodecahedron has diameter 3 in its
graph, while the 600-cell shell 3 has diameter 5. The name was
removed and replaced with the descriptive "30-vertex degree-3 shell"
(later corrected to "30-vertex degree-4 shell" after verifying
the edge graph degree).

**Papers corrected:** SS-1 (v2), SM-1 (v6), SM-2 (v30), OP-SS-1.

### The φ^{3(l-1)} falsification

**Prior state:** The original CPP quark mass formula used a
volume-scaling hypothesis V_l ∝ φ^{3(l-1)}, predicting each
additional cage layer multiplies the mass contribution by φ³ ≈ 4.236.

**The computation:** Exact 600-cell shell volumes were compared
against this formula. The actual shell volumes have a palindromic
structure and do not follow φ^{3(l-1)}: the formula produces
factors of 3–8× error in the structural masses. For the top quark,
the additive formula would require ~7,217 vertices to hit the correct
mass — impossible given the 600-cell's structure.

**Result:** φ^{3(l-1)} scaling is quantitatively falsified. Removed
from all papers. The qualitative ordering (more cage → more mass)
remains correct; the exact formula is now OP-SS-1 (open).

**Positive finding from the same session:** K(c,b,t) = 2/3 to 0.42%
for the three heavy quarks, consistent with the K3 spectral structure
showing through when cage binding << current mass. This confirmed
Thomas's thermal ZBW picture as the leading candidate for the quark
mass formula.

---

## Phase 4: α_geom Resolution and sea_strength Derivation (23–25 March 2026)

Working with the 600-cell SM emergence series, the resolution of
OP-SM-1 (derive k ≈ 0.0185) and OP-SM-2 (reconcile k and sea_strength)
directly fed into SS-1's Section 8.

**The α_geom derivation (SS-1 Theorem 4 / Section 8):**

The exact algebraic constant:
α_geom = 3(11+5√5)√(5+√5)/320 ≈ 0.55936

was derived from the 600-cell H4 Voronoi stiffness integral —
the same constant that had appeared independently in the SR-1
coupling constant k_rel. This cross-series appearance of the
same geometric invariant was identified as the strongest evidence
to date for CPP's geometric unification program.

**sea_strength derivation:**

From α_geom:
- k_SM = α_geom / (12φ²) ≈ 0.01781 (per-vertex coupling)
- sea_strength = (N_lattice/z) × k_SM = (120/12) × k_SM = 10 × k_SM ≈ 0.17805

Factor 10 = N_lattice/z = 120/12 is an exact geometric integer
(total vertex count / coordination number). This resolved the
previously mysterious factor-of-10 between k and sea_strength.

**Status:** sea_strength was previously the sole calibrated parameter
of the strong sector. It is now derived to within 3.8% from geometry.
The 3.8% residual is the stereographic S³→ℝ³ projection correction,
identified as the single source of the gap across all CPP coupling
constants.

**Language decision (29 March 2026):** After reviewing the Sonnet 4.0
critique, "derived" was softened to "derived to within 3.8%" throughout
the paper. The conclusion's "zero free parameters" was softened to
"effectively zero free parameters." This is the more honest characterisation
while the projection residual's analytic derivation remains pending.

---

## Phase 5: v2 Production and Pre-submission Review (23–25 March 2026)

`cpp_ss_unified_v2.tex` was produced incorporating:
- The Grok v1 merge (1+3+4 count, PSR saturation, transverse qDP,
  proton mass quantification, glueball)
- The PS-1 corrections (30-vertex shell, φ^{3(l-1)} removal)
- The α_geom/sea_strength derivation (Section 8)
- Claude Sonnet (Anthropic) added to author line
- The revised cage sequence 4→12→20→30 throughout
- The K3 thermal remark (heavy quark thermal picture)
- The 30-vertex shell remark with corrected geometry

Pre-submission review was conducted by Claude Opus (Anthropic).
Opus identified:
1. The icosidodecahedron name error (corrected)
2. The φ^{1/z} form of the 3.9% projection residual (noted)
3. The status of several mass predictions (confirmed honest)

---

## Phase 6: Sonnet 4.0 External Review (29 March 2026)

A fresh Sonnet 4.0 instance was used as a simulated external reviewer
to stress-test SS-1 v2 before OSF submission. The review raised five
substantive concerns, assessed and sorted in reviews-SS-1.md as:

**Misunderstandings (3):**
- M1: SU(3) derivation is circular — rejected (two-step structure
  already present; operators computed from geometry, not defined to match)
- M2: β₀ asserted — rejected (Casimir invariants derived from Theorem 1,
  β₀ is arithmetic from these)
- M3: Holographic dilution factor — misaddressed (SM-2 criticism, not
  present in SS-1 theorems)

**Valid concerns addressed (2):**
- V1: Physical identification asserted — valid; model postulate
  statement added to CPP primitives §1.1 (v3 H4)
- V2: "Derived" too strong for 3.8% residual — valid; language
  softened throughout (v3 H6)

**Genuine weakness identified (not by reviewer):**
- G1: Uniqueness of SU(3) operator mapping not proved — registered
  as OP-SS-11

---

## Phase 7: v3 Harmonization Session (29 March 2026)

Session with Thomas Lee Abshier ND and Claude Sonnet (Anthropic).
Seven harmonization patches applied to produce v3
(SS-1_strong_sector_from_600cell_lattice.tex):

| Patch | Content |
|-------|---------|
| H1 | Title to series standard: SS-1 prefix, \and authors, \date institution block |
| H2 | Keywords added after abstract |
| H3 | Table 1: linear ZBW DP explicit for all down-type quarks (d, s, b) |
| H4 | CPP primitives §1.1: tetrahedral cage assignment stated as model postulate |
| H5 | W bracelet locally-linear coupling face added to universal masslessness remark |
| H6 | sea_strength language softened to "derived to within 3.8%" throughout |
| H7 | \raggedright after \end{abstract} |

**Physics discussions during v3 session:**

Several physics clarifications were reached that, while not requiring
further paper changes, were registered as new open problems and
conjectures:

1. **qCP structure clarification:** u and d quarks have no polyhedral
   cage — they are bare qCPs with ZBW clouds. The tetrahedral cage is
   additional mass-adding structure that first appears at the strange
   quark. Free qCPs are energetically suppressed (dynamic confinement),
   not topologically forbidden.

2. **Linear ZBW DP universality:** All down-type quarks (d, s, b)
   carry the linear ZBW DP, not just the down quark. This was
   implicit in the charge screening argument but not explicit in
   Table 1. Corrected in v3.

3. **W bracelet polarity inversion:** Every quark flavor transition
   involves +qCP ↔ −qCP polarity switching, observed systematically
   across all decay pathways with Grok. The W₀ bracelet presents a
   locally linear coupling face to the qCP, and this directional
   asymmetry is the geometric origin of the polarity-inverting weak
   coupling. Registered as CJ-SS-new-1, CJ-SS-new-2, OP-SS-12.

4. **ZBW mechanism for δ = 1/3:** The C₃ geometric proof is
   authoritative; the ZBW orbital mechanism (inner orbital spending
   1/3 of its time in the tightly-bound 1/r³ configuration) should
   agree quantitatively. This agreement has not been proved.
   Registered as OP-SS-13.

5. **QCD deconfinement temperature:** CPP's energetic (not topological)
   confinement predicts T_c as the temperature at which thermal energy
   prevents qDP chain self-collimation. Dimensional estimate:
   k_B T_c ≈ σ r_conf ≈ 140 MeV (consistent with lattice QCD ≈ 155 MeV).
   Registered as OP-SS-14.

**File naming:** Thomas renamed the v3 output to
`SS-1_strong_sector_from_600cell_lattice.tex`, following the series
standard established by SM-1 through SM-5 and SR-1.

---

## Phase 8: Documentation Files Produced (29 March 2026)

Following the v3 session, four documentation files were written to
complete the SS-1 five-file documentation standard:

| File | Content |
|------|---------|
| reviews-SS-1.md | Formal rebuttal of Sonnet 4.0 review |
| philosophy-SS-1.md | Foundational commitments, layer structure, epistemology |
| mechanism-SS-1.md | 30-step causal narrative from cage geometry to QCD |
| glossary-SS-1.md | Contextual definitions of all SS-1 terms |
| development-SS-1.md | This file |

Open problems register updated: OP-SS-9 resolved, OP-SS-11 through
OP-SS-14 added, conjectures-SS.md created.

---

## Current Status (29 March 2026)

| Item | Status |
|------|--------|
| SS-1_strong_sector_from_600cell_lattice.tex (v3) | ✅ Ready for OSF |
| reviews-SS-1.md | ✅ Complete |
| philosophy-SS-1.md | ✅ Complete |
| mechanism-SS-1.md | ✅ Complete |
| glossary-SS-1.md | ✅ Complete |
| development-SS-1.md | ✅ Complete (this file) |
| OSF submission | ⬜ Pending — batch with SM-1 through SM-5 and SR-1 |
| DOIs added to bibliography | ⬜ After OSF upload |
| OP-SS-11 uniqueness proof | ⬜ For v4 or SS-1b companion |

---

## Key Decisions Log

| Date | Decision | Rationale |
|------|----------|-----------|
| Feb 2026 | Produce unified package alongside five companions | Single citable document; companions remain for step-by-step reference |
| Feb 2026 | Include Grok v1 merge | 1+3+4 count and PSR saturation mechanism are genuine contributions |
| 25 Mar 2026 | Remove C₆₀ cage | Exact 600-cell computation shows no 60-vertex distance shell |
| 25 Mar 2026 | Remove φ^{3(l-1)} scaling | Falsified by 3–8× errors in structural masses |
| 25 Mar 2026 | Add 30-vertex shell as fourth cage candidate | Natural 600-cell distance shell with correct geometric properties |
| 25 Mar 2026 | Remove "icosidodecahedron" name | Diameter-3 graph, not diameter-5 like the actual shell; caught by Opus |
| 25 Mar 2026 | Derive sea_strength from α_geom | Resolves OP-SM-1 and OP-SM-2; unifies strong and SR coupling constants |
| 29 Mar 2026 | Soften "derived" → "derived to 3.8%" | Honest about 3.8% projection residual pending analytic derivation |
| 29 Mar 2026 | Add model postulate statement | Preempts circularity objection; distinguishes geometric derivation from physical identification |
| 29 Mar 2026 | Add W bracelet coupling face paragraph | Captures new physics insight; flags OP-SS-12 |
| 29 Mar 2026 | Rename to SS-1_strong_sector_from_600cell_lattice.tex | Matches series ID-based naming standard |

---

## Provenance of Key Results

| Result | First appearance | Verified by | Status |
|--------|-----------------|-------------|--------|
| T^a = λ^a/2 (exact) | SS#2 companion | mc_su3_algebra.py (33/33 checks) | Theorem 1 |
| C_A = 3, T_F = 1/2 | SS#3 companion | mc_su3_algebra.py | Theorem 1 corollary |
| β₀ = 7 | SS#4 companion | Arithmetic | Theorem 4 |
| GMO relations | SS#5 companion | PDG comparison | Theorem 5 |
| Gluon masslessness | SS#3 companion | Topological argument | Theorem 2 |
| Ω⁻ = 1681 MeV (0.5%) | SS#5 companion | PDG 1672.5 MeV | Theorem 5 |
| α_geom exact form | α_geom derivation session | SR-1 companion c02 independently | Theorem / SS-1 §8 |
| sea_strength = 10 k_SM | SM-1/SM-2 resolution | Exact geometric ratio 120/12 | Theorem / SS-1 §8 |
| φ^{3(l-1)} falsified | PS-1 session | Exact 600-cell shell computation | Falsified |
| C₆₀ cage falsified | PS-1 session | Exact 600-cell shell enumeration | Falsified |
| 30-vertex shell identified | PS-1 session | Shell 3 property verification | Candidate / open |
| K(c,b,t) = 2/3 to 0.42% | PS-1 thermal session | PDG data computation | Empirical finding |
