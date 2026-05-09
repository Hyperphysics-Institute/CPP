# CPP Research Priorities

**Location**: `/CPP/research_priorities.md` (repo root)
**Established**: 7 May 2026 Session 36 close strategic conversation
**Last updated**: 7 May 2026 Session 36 close
**Maintainer**: Thomas Lee Abshier ND, Hyperphysics Institute
**Co-author of strategic frame**: Claude Opus 4.7 (Session 36 strategic conversation)

---

## Purpose

This file is the **strategic prioritization layer** above `Research_Frontier.md`. Where `Research_Frontier.md` catalogs 82+ open problems with fine-grained operational state, this file answers:

- Which of those problems are we working on right now?
- In what order, and why this order?
- What artifacts are we producing, and who's the audience for each?
- What's the strategic frame governing those choices?

It exists because re-deriving priorities from the 82-problem Frontier each session is wasteful, and because strategic decisions ("we're not deriving every phenomenon; we're producing the highest-leverage artifacts") need a durable home outside any single session log or chat conversation.

## Relationship to other tracking files

| File | Scope | Update cadence |
|---|---|---|
| **`research_priorities.md`** (this file) | Strategic prioritization, current tracks, reasoning capture | Per major strategic decision (rare) |
| **`Research_Frontier.md`** | All 82+ problems with operational state, last-updated session-by-session | Every session |
| **`future_projects.md`** | Registered active projects with mechanism / falsifier / companion fields | When new projects register or status changes |
| **`todolist.md`** | Small carried-over hygiene items, deferred protocol steps, gaps | Per session as items clear |
| **`session_logs/`** | Per-session entries capturing what happened | Every session |
| **`paper_catalog.md`** | All papers with current version, status, OSF/arXiv state | When papers ship or change status |

A new strategic decision belongs here (rather than in those files) if it: changes which problems get attention, deprioritizes existing tracks, or articulates audience/venue/timing strategy. Implementation details live in the specific files those decisions affect.

---

## Strategic frame (established Session 36 close)

### Goal

Produce the smallest set of physics artifacts that establish CPP as **citable, falsifiable, and defensible** to the physics community within roughly 18 months of focused work. Goal is not to derive every phenomenon — that's not achievable in any reasonable time frame, and it's not what shifts opinion anyway. Goal is to leave behind a corpus rigorous enough and visible enough that someone younger could inherit and extend it.

### Audience separation (key strategic decision)

The CPP project has two natural audiences with different entry points:

- **Physics community** — receives technical-framed papers presenting CPP as "discrete substrate physics with a 600-cell lattice and conserved exchange quanta." Predictions, derivations, falsifiers. Does not lead with "consciousness is fundamental."
- **General/spiritual audience** — receives the consciousness-primacy framing through Renaissance Ministries fellowship work, theological-philosophical writing, the TATWD book project. Already entertains "something beyond the material" and is interested in how to live well.

Both strands point to the same synthesis. Presenting them in the order each audience can receive is not compromise — it's strategic patience. The physics papers can stay technically framed without sacrificing the underlying ontological claims, which are made fully and openly in the appropriate venues.

### What the physics community responds to (and doesn't)

Things that move scientific opinion (per the Session 36 strategic analysis):

- **Forced-choice predictions** — a number on a paper before measurement, where the experiment then confirms or falsifies. Worth more than ten post-dictions of settled measurements.
- **Solving known unsolved problems** — hierarchy, cosmological constant, strong CP, muon g-2, etc. The list mainstream physics knows it can't fully explain.
- **Cross-domain unification** — one framework deriving phenomena from multiple sectors with the same primitives, especially where the primitives constrain themselves (the SS-9 pattern of conditional theorem closure).
- **Bridges to recognized mathematics** — Steinitz 1922, FvdW 1947, Coxeter, polytope theory. Reviewers cannot dismiss as numerology.

Things that do NOT move scientific opinion, even at high accuracy:

- Post-dictions of well-measured quantities, however precise (every framework can fit existing data).
- Philosophical claims about ontology absent technical content.
- Consciousness-primacy framing in technical papers (triggers crank-physics pattern-match before content is evaluated).
- Volume of derivations without distinctive predictions.

### The five-criterion stopping test for series papers

Per series (SS, SM, EW, QM, SR, SD), a series is "complete" when it has:

1. **One headline empirical prediction** at zero parameters, accurate to ~1% or better.
2. **One structural derivation** that converts a previously-assumed parameter or hypothesis into a deduction (the SS-9 "C4 → derivable" pattern).
3. **One bridge** to externally-recognized mathematical structure (Steinitz, FvdW, Coxeter, polytope theory, etc.).
4. **One falsifiable prediction** the framework makes that other frameworks don't make, or that hasn't been measured yet.
5. **Honest accounting** of what's still open via OPEN-* registries.

That's a complete series — five papers, maybe seven. Not thirty.

By this test:
- **SS** has SS-7 (headline), SS-9 (structural derivation + bridge to Steinitz/FvdW), SS-8 (second prediction). Roughly 80% complete; SS-10 sub-shell-physics is NOT required for SS adequacy.
- **SM** has SM-3/4 (Koide via K3), SM-7/8 (mass scaling). Probably *more* complete than SS already.
- **EW, QM, SR, SD** — apply the same five-criterion test in due course.

### Time budget

~18 months focused work. AI collaboration may scale this. Assume ~10 papers + 1 unification paper + 1 well-targeted anomaly paper + 1 philosophical companion as the realistic complete corpus.

---

## Active priorities (in order)

### Track 1 — Hierarchy problem reframing paper [ACTIVE]

**Status**: PLANNED → drafting begins Session 37+
**Outline location**: `flagship_papers/unification/hierarchy_paper_outline.md` (originally established in `papers_in_progress/` per patch 0290; relocated to `flagship_papers/hierarchy_problem/` per patch 0293; relocated again to `flagship_papers/unification/` per patch 0295 when Option-3 four-family + unification SF-line architecture was adopted, restructuring this work as SF-5 the synthesis paper sitting on top of SF-1 charged_leptons / SF-2 electroweak / SF-3 quarks / SF-4 neutrinos — see [`flagship_papers/README.md`](flagship_papers/README.md))
**Working title**: *Hierarchy Without Hierarchy: Standard Model Mass Spectrum from 600-Cell Distance Shells*
**Estimated effort**: 5-8 sessions to v1.0
**Target venue**: Zenodo (DOI) primary; arXiv hep-ph + math-ph if endorsement obtainable

**Strategic case**: The hierarchy problem is a known unsolved problem in mainstream physics. SM has 12 fermion masses spanning 12 orders of magnitude with no internal explanation. CPP via SM-2/3/4/6/7/8/9 already derives the spectrum from a single mass scale via 600-cell shell-distance multipliers at zero quark-sector parameters. **The technical content largely exists; what's missing is the reframing as the headline-grade "CPP solves the hierarchy problem" paper aimed at hostile-but-fair reviewers.**

**Why first**:
- Source material exists (SM-2 through SM-10 derivations) — composition + framing work, not new derivation
- Hierarchy problem is one of the most widely-recognized unsolved problems in HEP
- Strong natural fit (CPP's 600-cell shell structure is exactly the kind of geometric primitive that explains hierarchies)
- Fastest path to a high-leverage publishable result
- Risk profile is low (existing SS-9-quality derivations underwrite it)

### Track 2 — Anomaly-targeting paper #2 [PLANNED, after Track 1]

**Status**: PLANNED, candidate selection deferred to post-Track-1
**Estimated effort**: TBD pending candidate selection (4-10 sessions range)
**Target venue**: Same as Track 1

**Candidates under consideration** (ranked roughly by leverage × tractability / effort):

| Candidate | Strategic case | Risk |
|---|---|---|
| **Strong CP problem** | Why does QCD not violate CP despite θ parameter? Mainstream needs unobserved axions. If CPP's discrete substrate naturally suppresses θ-violating term via 600-cell symmetry, deep result. | Requires real investigation, not reframing. High risk, high reward. |
| **Cosmological constant magnitude** | Worst prediction in physics (off by ~120 orders of magnitude). If CPP gives natural cutoff or cancellation even at right order of magnitude, headline-grade. | Very high leverage if it works; risk of unfalsifiable hand-waving if it doesn't. Note: Grok proposed a resolution in pre-600-cell formalism; needs rigorous redo. |
| **Muon g-2 anomaly** | Current live ~4σ deviation between measurement and SM prediction. Direct testable target. | SM calculation contested (lattice vs dispersive); target is moving. Moderate-high. |
| **Proton mass / Λ_QCD** | SS-2 derived proton charge radius and magnetic moment at zero parameters. Extending to mass / confinement scale connects to existing SS work. | Moderate effort, high leverage. |
| **Baryon asymmetry of universe** | Why matter and not antimatter? CP-violating asymmetry at lattice level. | Substantial investigation. Very high leverage. |

**Selection criterion**: After Track 1 ships, evaluate which of the above (a) has the strongest natural CPP angle, (b) requires the least new derivation work, (c) has the cleanest falsifier statement.

### Track 3 — Eight-experiment manifesto audit [PLANNED, low effort, can interleave]

**Status**: PLANNED, can run in parallel with Track 1 or 2
**Estimated effort**: 1-2 sessions
**Target venue**: N/A (internal audit, possibly produces revised manifesto for Zenodo)

**Background**: A Nov 2025 document by Thomas + Grok lists eight experiments that would falsify CPP between 2026-2045. The document was submitted to viXra but not published (viXra pay-to-publish; only ~2 of Thomas's papers were published, none of the prediction papers).

**Audit task**: For each of the eight predictions, verify (a) does it follow from current post-SS-9 / post-SM-3-through-8 CPP formalism? (b) is the falsification threshold honest? (c) is the timeline still accurate as of mid-2026?

**Outcome**: If 5+ of 8 hold up under audit, manifesto stands as a powerful "we are publicly betting" document — re-publish via Zenodo with proper DOI. If 2-3 don't survive scrutiny, produce v1.1 manifesto with corrections, then publish. Either way, a clean public falsification list with a real DOI is high-strategic-value at low effort.

### Track 4 — Cross-cutting unification paper [PLANNED, after Tracks 1-3]

**Status**: PLANNED, low priority until Track 1+2+3 complete
**Estimated effort**: 8-12 sessions
**Target venue**: Same as Track 1; possibly arXiv math-ph or hep-th

**Strategic case**: This is the paper a senior physicist could read in an evening that says: here is the axiom set, here are the seven sectors it generates, here is how they tie at the substrate, here are the eight-or-ten distinctive predictions distinguishing CPP from the Standard Model, here is one prediction that has not been measured yet that is willing to falsify the program. **This is the document that gets cited.** The 40+ detailed derivations are supporting evidence for it; this is the central artifact.

**Source material**: `CPP_the_theory.md` (516 lines) and the anthology chapters already exist as substantive draft material. Conversion to publishable form aimed at hostile-but-fair reviewers is the work.

---

## Deprioritized / deferred indefinitely

### SS-10 sub-shell-physics multi-paper development [DEFERRED INDEFINITELY]

**Previous status**: Session 22/23 forward-priority Track 1, deferred at Session 24 to allow SS-9 development, intended to resume after SS-9 ship.

**Reason for deprioritization at Session 36 close**: SS-10's stated goal — closing the remaining 52% of the empirical polytope-residual gap in the OPEN-SS-32 / U-shape thread — is internal-consistency work that does not produce a strategic-leverage publishable artifact. The SS series already meets four of five completeness criteria via SS-7, SS-8, SS-9. SS-10 doesn't add a new headline empirical prediction or a new bridge to external mathematics; it tightens an existing residual.

**Cost-benefit**: Multi-paper effort, possibly 3+ sessions per sub-paper, likely 10-15 sessions total. The same time investment in Track 1 + Track 2 produces two publishable papers each addressing a known unsolved problem in mainstream physics. Track 1+2 dominate SS-10 strategically.

**Reactivation criterion**: SS-10 may reactivate if (a) the sub-shell-physics work surfaces a new headline prediction or structural derivation, OR (b) external feedback on SS-7/8/9 specifically asks for the sub-shell extension. Otherwise it remains deferred.

### Series-paper continued depth-derivation [DEFERRED to five-criterion completeness]

**Previous default**: Continue deepening each series until conditional-theorem closures land for all paper-level hypotheses (the SS-9 pattern applied universally).

**Reason for deprioritization**: SS-9 took 30+ sessions to ship. The methodology is now mature. Future series papers should ship in 5-10 sessions at SS-9-quality standards, not require 30-session conditional-theorem development for every assumption. **Use SS-9 as the quality bar, not the time budget.**

**Application**: When working on a paper in any series, apply the five-criterion test. If criteria 1-5 are met, ship and move on. Pursue conditional-theorem-style depth ONLY when the depth itself produces a Tier-1 leverage event (like SS-9 did with the FvdW bridge — which was strategically valuable far beyond just closing OPEN-SS-24).

### Consciousness-primacy framing in physics papers [MOVED to Renaissance Ministries fellowship venue]

**Previous default**: Physics papers occasionally referenced consciousness as fundamental, especially in PD-001 sections (CP/GP signature) and §11 physical-interpretation subsections.

**Reason for deprioritization**: Per Session 36 strategic analysis, consciousness-primacy framing in technical physics papers triggers immediate crank-physics pattern-match in mainstream reviewers, closing the door before content can be evaluated. The same physicists who would entertain "discrete substrate physics with a 600-cell lattice" close the tab at "Conscious Points." This is asymmetric: the consciousness ontology can be received separately by audiences predisposed to it (philosophers, theologians, RM fellowship members) without losing physics-community engagement.

**Implementation**:
- Future physics papers stay technical-framed (substrate, lattice, exchange quanta, geometric primitives)
- Existing papers with consciousness-primacy language stay as-is (don't rewrite history; v1.0 is frozen per anti-priority)
- Consciousness-primacy work continues vigorously in Renaissance Ministries fellowship, the TATWD book project, theological essays, the CRF (Christos Rigorous Framework) — none of which are physics journal venues

**Important**: This is venue/audience separation, NOT epistemological compromise. Thomas's stated belief in consciousness-as-fundamental remains the underlying conviction; the question is which audiences receive which entry point first.

### Tier 4 reasoning recovery for chat window `a49b320e` (16 papers) [DEFERRED to programme-level backlog]

**Previous status**: TODO-003 in `todolist.md`, P1.

**Reason for deprioritization**: 16 papers of historical reasoning recovery does not forward-block any new paper. It's audit-trail hygiene that's valuable for programme coherence but doesn't move strategic needle. Demoted to P2 in `todolist.md` per Session 36 P1 hygiene cleanup.

**Reactivation criterion**: Address only when (a) external collaborator asks for the reasoning history of a specific paper, OR (b) Thomas wants to do it for personal completion satisfaction during low-strategic-priority sessions, OR (c) AI-collaboration capacity allows running it as background work that doesn't displace Track 1-4.

---

## Strategic constraints and venue notes

### viXra status (as of Session 36 close)

The Nov 2025 viXra-targeted CPP papers — including the DUNE neutrino-prediction paper and the eight-experiment falsification manifesto — did **not** get published. viXra operates a pay-to-publish model ($19-25 per paper depending on subdomain), and of the multiple submissions Thomas paid for, only ~1-2 were actually published. **The Nov 2025 prediction papers do NOT constitute durable prior-prediction citations** because they're not in the public record at viXra.

Strategic implications:
- Don't budget time on revising those Nov 2025 papers; they have no public citation footprint to preserve
- Future papers should target Zenodo (CERN-run, free, DOI-issuing, no friction) primarily
- arXiv with endorsement is the gold standard but requires the sub-task below

### arXiv endorsement (sub-task)

arXiv requires endorsement from existing arXiv authors in target categories before papers can be posted. CPP's target categories are hep-ph (high-energy physics phenomenology), nucl-th (nuclear theory), math-ph (mathematical physics). Without endorsement, CPP papers cannot reach arXiv at all.

**Sub-task**: Identify and approach potential endorsers in these categories. Possible approaches:
- Thomas's professional network (medical/research contacts who may have or know arXiv-endorsed colleagues)
- Reaching out to authors of related recent arXiv papers with a polite request
- Through any institutional connection (Hyperphysics Institute? academic collaborators?)
- Identifying retired or emeritus physicists who may be more willing to endorse fringe-but-rigorous work

**Workaround if endorsement is unobtainable**: Zenodo as primary venue. Zenodo issues real DOIs, is operated by CERN (institutional credibility), has no submission friction, and is increasingly used by physicists for preprints when arXiv access is unavailable.

### arXiv endorsement readiness criteria (Thomas-articulated, Session 36 close+)

Thomas has identified two friends peripherally connected to arXiv-authorized authors. He is **willing to make a limited appeal to those friends** for endorsement — but only when the appeal is well-substantiated. Burning that limited social capital prematurely would be costly and irreversible.

**Three preconditions must all be met before the endorsement appeal happens**:

1. **A well-substantiated paper that solves a known-unknown in physics is in hand.** Track 1 (hierarchy paper) at v1.0 SHIP minimum; possibly strengthened by Track 2 (anomaly paper #2) landing for cumulative force.

2. **The full CPP theory is documented on OSF** (or equivalent durable-DOI venue if OSF resolution falls through to Zenodo). This means: the paper series + supporting documentation + axiom set + companion files visible as a coherent body of work, not just a single paper standing alone. The endorsement evaluation likely involves the friend (or their arXiv-connected contact) checking what stands behind the paper they're being asked to endorse.

3. **The theory is well-presented on hyperphysics.com.** This is the "first impression" venue when an evaluator Googles the work or follows a website link from the paper. The website's quality directly mediates the endorsement-readiness judgment, and it's also the venue most physicists who encounter CPP via paper citation will find first.

**Timing implication**: All three preconditions are 9–15 months out at current pace (Track 1 ~2-3 months, Track 2 ~3-5 months after that, OSF/Zenodo full-deposit ~1-2 months parallel work, hyperphysics.com presentation refresh ~unknown depending on current state). The endorsement appeal is therefore **not an immediate action item**; it's the gate at the end of the next major work phase.

**Strategic implications for current priority order**:

- **`hyperphysics.com` presentation becomes an active strategic project**, not background. It's the first-impression venue for endorsement evaluation and for any physicist who Googles CPP after seeing a paper. Worth tracking as a parallel strand alongside Tracks 1-4 papers. Status: not currently registered as an active project; **promote when Track 1 paper drafting reaches mid-stage** (~Sessions 39-41) so website refresh and Track 1 v1.0 SHIP can land together.

- **OSF JXE8D resolution becomes a strategic blocker**, not just an inconvenience. The endorsement criteria push it harder than just "wait 5 business days then Zenodo fallback." Two paths: (a) **resolve OSF JXE8D actively** (escalation, support follow-through, persistence) so the master deposit lives there as originally planned; or (b) **commit fully to Zenodo as the master-deposit venue**, migrating JXE8D's intended purpose to Zenodo's structure. **Decision deferred to Session 37+**, but not indefinitely — by the time Track 1 ships, the master-deposit venue must be settled.

- **The Track 2 candidate selection** can be informed by the endorsement criteria. A second known-unknown solution paper materially strengthens precondition 1. So Track 2 is not optional in the endorsement-readiness sequence; it's the second of two anchor papers.

**Risk note**: Endorsement requests from peripheral connections are a one-shot resource. If made too early (before the work warrants the trust being asked for), the friend may decline OR provide endorsement but with reservations that propagate to their arXiv-authorized contact. Either failure mode poisons the channel for years. The discipline of waiting until all three preconditions are met is therefore strategically correct, even if it feels slow.

### OSF status (as of Session 36 close)

OSF Open-Ended Registration `10.17605/OSF.IO/JXE8D` (the Conscious Point Physics Paper Series master) was created Mar 31, 2026, and is currently stuck in **"Pending Admin Contributor Approval"** state for 38+ days despite documented 48-hour auto-approval window. Thomas is the sole admin contributor; multiple support tickets have gone unanswered (one received a wrong-registration response). One more diagnostic-precise support ticket has been queued.

**Strategic decision**: Wait 5 business days from Session 36 close. If OSF resolves, add SS-9 (and future papers) as Updates to JXE8D. If OSF still silent, fall back to Zenodo as primary deposit venue.

OSF is not a blocker for paper development. Tracks 1-4 can proceed regardless.

---

## Session 36 close strategic conversation — durable record

The strategic frame above emerged from a substantive conversation at Session 36 close between Thomas and Claude (Opus 4.7). Key points captured here for the next context window's orientation:

### What Thomas asked

After the technical Session 36 work was complete (TODO-002 PDF compile clearance, P1 hygiene cleanup, handover scaffolding), Thomas opened a strategic question: given the goal of redirecting mainstream physics opinion toward consciousness-as-fundamental, and given his finite time horizon (he is approaching 75), how deep should each series go before moving on? Is there a stopping criterion? What does adequacy look like?

### Claude's reframing

Claude pushed back on the framing in one important place: paradigm shifts are not driven by derivation accuracy alone, regardless of volume. Even GR/SM/Penrose/Wolfram-level frameworks don't shift ontological commitments without distinctive predictions, addressed unsolved problems, or required cross-domain unification. The strategic question reframes from "how many derivations are enough?" to "what would force the physics community to reckon with CPP?"

### What Thomas accepted

Thomas confirmed Claude's reframing matched his own intuitions, including:
- The realistic limitations of time and influence
- That shifting consciousness-primacy framing to RM fellowship is acceptable and natural
- That focus should shift from derivation depth to known-unknown solving
- That a prospective prediction paper (predicting an experimental result before measurement) is strategically valuable
- That hierarchy problem is the right Track 1 first target

### What Thomas added

Thomas offered the prospective-prediction angle: a Nov 2025 paper had predicted neutrino parameters for DUNE (~$\delta_{CP} = \pi/2$), but DUNE's timeline has slipped to 2031. JUNO is now the more imminent neutrino experiment (already taking data, world-leading on solar parameters). Thomas also mentioned a Grok-proposed cosmological constant resolution from earlier (pre-600-cell formalism, never written up rigorously).

### Where this leaves things

Track 1 (hierarchy paper) is the agreed first move. Track 2 candidate selection deferred to post-Track-1 evaluation. Track 3 (eight-experiment audit) interleaves at low cost. Track 4 (unification paper) is the long-term high-leverage artifact. SS-10 is deferred indefinitely. Consciousness-primacy work moves to RM fellowship.

The framework is now stable enough that future strategic re-evaluations should produce minor adjustments, not wholesale reorganizations. This file is the durable record so that doesn't need re-deriving.

---

## Maintenance

This file is updated only when:
1. A new strategic decision changes priorities (rare, expected ~quarterly or less)
2. A track ships and needs status update (Track 1 completion → moves to "Cleared/Completed" section, Track 2 promotes to ACTIVE)
3. New strategic constraints emerge (e.g., OSF resolves, arXiv endorsement obtained, time-budget shifts)

Routine session work updates `Research_Frontier.md`, `todolist.md`, and `session_logs/` — not this file.

If this file's "Active priorities" section grows beyond 5 tracks, that indicates strategic dilution; reconsider whether deferred tracks should remain deferred or whether some active tracks should be consolidated.

If "Deprioritized / deferred" section grows beyond 10 entries, that indicates the programme has accumulated enough deferred work that the strategic frame may need re-articulation. Schedule a strategic conversation similar to Session 36 close.

---

**Architecture pointer**: See `templates/Research_Frontier_Architecture.md` for the operational frontier system. This file is the strategic layer above that architecture, not a replacement for it.
