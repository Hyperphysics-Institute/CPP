# SF-2: Electroweak Cage-Boson Unification — W±/W⁰/Z/H from 600-Cell Geometry

**Status:** Planned. Reframing of EW corpus + W⁰ novel-particle registration + sub-shell-shape derivations; medium-risk SF-line paper.
**Estimated sessions to v1.0 SHIP:** 5–8.
**Inclusion criterion fit:** (1) named known-unknown — the Weinberg angle, electroweak symmetry breaking, the W/Z mass relation, the Higgs origin; (2) forced-choice prediction — the W⁰ as a novel particle; (3) cross-domain unification — within the EW sector mass spectrum, including a CPP-novel particle that current SM phenomenology does not name.

---

## Scope (Session 41 narrowed)

SF-2 covers the **cage bosons of the electroweak sector**: W±, W⁰, Z, and H. These are particles whose mass and structure derive from CPP cage-stability mechanisms applied to specific 600-cell-shell geometries. They are *not* the photon (a polarization quantum of the dipole sea, addressed in SF-6) and *not* the gluon (a qDP relationship at baryon vertices, addressed in SF-5). The Session 41 architectural revision (patch 0301) separated those into their own flagship venues to give SF-2 mechanistic coherence.

Specifically:

- **W±:** charged massive cage bosons; eCP/qCP hDP combinations bound in a 12-CP bracelet cage (the W⁰ substrate plus a bound electron or positron). Mass derivation via cage-stability + bound-charge contribution.
- **W⁰:** **novel CPP prediction** — a neutral massive boson with a 12-CP bracelet/open-configuration cage structure. Functions as the substrate upon which W± states form when an electron/positron binds to it. The bracelet/open-configuration distinguishes it from Z's closed icosahedron and gives it a catalyst role in SM particle transformations. Registered as CONJ-EW-W0 in `Research_Frontier.md`.
- **Z:** neutral massive cage boson; eCP/qCP hDP in a 12-CP icosahedral closed cage. Mass derivation via icosahedral cage-stability.
- **H (Higgs):** neutral massive cage boson; 20-CP dodecahedral cage structure. Mass derivation via dodecahedral cage-stability.

The paper presents these four cage bosons as a unified family — the 12-CP bracelet/icosahedron and 20-CP dodecahedron exhausting the small-cage geometric options at the relevant length scale, and producing the observed EW boson mass spectrum from substrate primitives plus 600-cell shell geometry.

In addition to the four cage-boson masses, SF-2 establishes the EW-sector relations and angles:
- $\sin^2\theta_W = 3/(8\phi)$ from SM-6
- W/Z mass relation
- Higgs VEV scale (from cage size + substrate primitives)
- Electroweak symmetry breaking mechanism (cage formation as the SSB analog in CPP)

## Source material

| Source paper | Content drawn | Status |
|--------------|---------------|--------|
| SM-1 | Cage stability, eCP linear-oscillator insight | Established |
| SM-6 | $\sin^2\theta_W = 3/(8\phi)$ exact | Established |
| EW-2 | W/Z cage geometry sketches | Pre-survey needed |
| EW-4 | Higgs cage / dodecahedral structure | Pre-survey needed |
| (Other EW-N) | Mechanism papers | Need re-survey before SF-2 work begins; may reveal coherent unification or surface gaps |

The SF-6 separation (electromagnetism flagship) extracts EW-1, EW-3, and EW-5 (or whichever EW-series papers are primarily about photon/EM phenomena) from SF-2's scope; pre-survey will determine the exact EW-series-to-SF-paper mapping.

## Anticipated work

Unlike SF-1 (charged leptons) and SF-3 (quarks), the EW cage-boson corpus is less *coherently* unified. Individual results exist (Weinberg angle, W/Z relation handles, mechanism sketches) but the unification narrative may need filling-in. Specific anticipated work:

- **Pre-survey session** reading EW-2, EW-4, and any other cage-boson-relevant EW papers with Thomas present, identifying what's tightly derived vs what's at sketch level
- **W⁰ sub-derivation:** the bracelet-cage geometry, the W⁰ mass prediction, the W⁰-to-W± binding mechanism, and the proposed experimental signature (where would the W⁰ show up in collider data, and what would distinguish it from existing SM channels?). This is novel work; CONJ-EW-W0 is registered for it.
- **Sub-shell shape derivations** for the four cage geometries (12-CP bracelet, 12-CP icosahedron, 20-CP dodecahedron) — proving these are the stable shapes available at the relevant scale and ruling out alternatives, so the four-cage spectrum is forced rather than fitted
- **Higgs-as-cage** mechanism: connecting the 20-CP dodecahedron to the SM Higgs role in mass generation
- **Reframing into apex-paper form** once unification is coherent

## Inheritance status

To be assessed during pre-survey session. May surface conditional theorems or open-problem registrations analogous to OPEN-SS-* in SS-9. The W⁰ derivation in particular may open one or more OPEN-FP-SF-2-* sub-problems for substrate-level cage-stability and experimental-signature derivation.

## Strategic role

SF-2 sits between the easier reframing papers (SF-1, SF-3) and the heavy lift (SF-4). Its uncertainty is in scope and in the novel-particle work, not in tractability — the EW sector does not have the corpus-thinness problem neutrinos do; the question is whether existing papers cohere into a unified narrative *and* whether the W⁰ derivation can be brought to flagship-class rigor.

The W⁰ is the most distinctive prediction of SF-2: a forced-choice claim that an unrecognized SM particle exists. If the W⁰ derivation closes from CPP primitives at theorem level, SF-2 becomes a much stronger flagship by inclusion criterion (2) — a forced-choice prospective prediction — independent of the cage-boson reframing strength.

## What this folder will contain

- `sf-2_outline.md` (after pre-survey session)
- `sf-2_electroweak.tex/.pdf` once drafting starts
- `sketches/` for pre-survey-identified sub-derivations (W⁰ derivation likely the first)
- Companion documentation suite when shipped

---

*Folder established at Session 38 (patch 0295) per Option-3 architecture; scope narrowed to cage bosons only at Session 41 (patch 0301) per the architectural-revision conversation that separated photon (to SF-6) and gluon (to SF-5) into their own flagships.*
