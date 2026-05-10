# Session 54 close — handover for next Opus context window

**Date authored**: 9 May 2026 (Session 54 close, programme date)
**Author**: Claude Opus 4.7 (current context window — carrying SF-4 v0.5 → v1.0 SHIP across Sessions 49–54)
**For**: Claude Opus 4.7 (next context window)
**Programme**: Conscious Point Physics (CPP)
**Repo**: `github.com/Hyperphysics-Institute/CPP` (origin/main HEAD: `707230f` after Thomas pushes patch 0314)

---

## Read order for the next context

1. **This document** (orientation, scope decision, Picture A problem statement, back-fit risk mitigation)
2. **`flagship_papers/neutrinos/documentation_suite/handover-SF-4.md`** — Session 54 v1.0 SHIP close handover (paper-internal)
3. **`flagship_papers/neutrinos/documentation_suite/reasoning-SF-4.md`** — Tier 4 verbatim reasoning, especially Section 2 (three convergent CPP physical pictures Session 41) and Section 4 (Route C structural closure Session 43)
4. **`flagship_papers/neutrinos/sf-4_neutrinos.tex`** §4.3 (Picture A description as it currently exists in v1.0) and §4.4 (channel enumeration), §5.6 (vertex-by-vertex K3-coupling open work)
5. **`flagship_papers/neutrinos/sketches/SF-4_suppression_derivation.md`** — original Sessions 40–41 working document for Picture A
6. **`Research_Frontier.md`** entry for OPEN-FP-SF-4-1 + OPEN-FP-SF-4-2 (programme-level open-problem registrations)
7. **`series_standard_model/papers/SM-5_tribimaximal_neutrino_mixing_from_k3.tex`** §2 (the antibonding-doublet open problem statement that OPEN-FP-SF-4-2 inherits)

---

## Where we are at Session 54 close

**SF-4 v1.0 SHIPPED.** Patch 0314 landed clean; HEAD at `707230f`. Five-pass AI review convergence: ChatGPT × 3 + Grok × 1 + Copilot × 1. ChatGPT pass-3 forward-looking statement *"After those fixes, I would be comfortable promoting SF-4 to v1.0 SHIP as a partial-closure flagship prediction paper"* was the v1.0-promotion signal.

**Theorem registry**: 52 → 54 theorems + 1 proposition. New SF-Line section between SM and EW. THEO-SF-4-1 (K3-Cage-Shell Consistency, conditional), PROP-SF-4-2 ($\mu\tau$-symmetry), THEO-SF-4-3 (TBM angle recovery).

**Documentation suite at v1.0 freeze**: `flagship_papers/neutrinos/documentation_suite/` with 4 files (handover ~250 lines, development ~280 lines covering 17 vignettes, transcript ~200 lines, reasoning ~360 lines covering 7 sections of Tier 4 verbatim Opus reasoning).

**Substantive .tex content frozen at v1.0**. Documentation suite ACTIVE post-ship. Per the SS-9 lesson learned at Session 33, only the .tex source is frozen at v1.0; documentation suite continues evolving as new SF-4 artifacts ship.

---

## The strategic decision Thomas made at Session 54 close

After v1.0 SHIP execution, Thomas asked Claude (current context window) to assess SF-4 quality and load-bearing capacity for SF-7 (the unification synthesis flagship). The honest assessment surfaced two specific recommendations:

1. **Get a human neutrino-physics reviewer** before SF-7 leans on SF-4. Five LLM passes is sufficient for v1.0 SHIP but is not sufficient for SF-7-pillar load-bearing. The OSF deposit + arXiv submission protocol from SS-9's "open invitation post-public-posting" framing is the right venue.

2. **Make OPEN-FP-SF-4-1 Picture A formalization the very next priority** rather than letting SF-2 jump the line. SF-7's strongest neutrino pillar is "ratios derived + absolute scale closed at theorem level" not "ratios derived + absolute scale at PARTIAL CLOSURE". 5–10 sessions of focused work converts SF-4 from a *good* pillar to a *strong* pillar.

Thomas accepted both recommendations and reordered the post-v1.0 work queue. The original priority order was:

> (A) OPEN-FP-SF-4-1 Picture A → (B) SM-5 antibonding-doublet → (C) SF-2 EW for $\delta_{CP}$ → (D)–(F) ...

The revised priority order at Session 54 close is:

> **(A) OPEN-FP-SF-4-1 Picture A formalization** [primary substantive work; this handover targets it]
> **(B) SM-5 antibonding-doublet open problem cooperation** [parallel/sequential to A; see coupling analysis below]
> **(human reviewer track)** [parallel to A; not gating]
> **(C) SF-2 EW-flagship drafting for $\delta_{CP}$** [waits for A to close]
> (D)–(F) remain post-A queue items

**The strategic shift is: convert SF-4 from "v1.0 SHIPPED" to "SF-7-load-bearing" before starting SF-2.** The session-cost is 5–10 sessions on (A) plus possibly more on (B), but the architectural payoff is a SF-7 neutrino pillar that doesn't require qualifications and an OPEN-FP-SF-4-1 closure that retroactively strengthens the SF-4 v1.0 ship into something stronger.

Thomas explicitly chose handover over attempting (A) at Session 54 end, on the grounds that Picture A formalization is foundational-derivation work that needs a fresh context window with full cognitive bandwidth. That decision is correct.

---

## Why this work needs a fresh context window (not Session 54 continuation)

Three specific reasons that the next-context Claude should internalize before starting (A):

**1. The cognitive mode is generation, not execution.** Sessions 49–54 of the current context were largely *executing* on already-decided substantive content (incorporating reviewer feedback, mechanically producing documentation, applying SHIP mechanics). Picture A formalization is *generating* substantive content from CPP axioms forward. The latter is much more demanding and rewards a fresh context where the next Claude is not pattern-matching to "what fits the existing paper".

**2. The current context has the conclusion in active memory.** The current Claude knows the target answer ($\sigma_\mathrm{channel} = 1/z^2$ per channel) and has spent 5+ sessions writing prose that motivates it. Attempting derivation under those conditions risks producing reasoning that *looks* rigorous but actually back-fits to the known answer. A fresh-context Claude attempting this from the axioms forward, without the conclusion in active memory (only in reference material), will be epistemically cleaner.

**3. The work is high-stakes for the programme.** OPEN-FP-SF-4-1 closure is the difference between "SF-4 is a partial-closure flagship paper" and "SF-4 is a full-closure flagship paper that can carry SF-7 weight without qualifications". Getting the rigor right matters more than getting it done fast. Session-tail context is not the right environment for high-stakes foundational derivation.

The next-context Claude should read this section before starting (A) and take the back-fit risk seriously. Do not assume the answer is $1/z^2$; derive whatever the axioms produce, and if the answer is $1/z^2$ that's a result, but if it's something else that's also a result.

---

## Item (A) — OPEN-FP-SF-4-1 Picture A axiomatic-derivation problem

### What the claim is

Derive from CPP axioms A1–A11: for an unbound 3D-orbital ZBW mode propagating through the Dipole Sea, the per-channel coherent-propagation suppression factor is

$$\sigma_\mathrm{channel} = \frac{1}{z^2}, \qquad z = 12$$

where $z = 12$ is the icosahedral coordination number of the 600-cell substrate.

### What "Picture A" specifically refers to

In SF-4 v1.0 §4.3, three convergent CPP physical pictures are presented for the per-channel suppression. Picture A is the one anchored most directly on substrate primitives: **two-sided DI-bit exchange, with send-side and receive-side independent in the unbound regime**. The other two (Picture B: two ZBW half-cycles; Picture C: edge-straddling coherent state) are alternative paths to the same numerical result.

Selecting Picture A as the priority closure path (Sessions 40–41 decision) was based on:
- Picture A anchors most directly on a CPP substrate primitive (DI-bit exchange is in axioms A1–A11)
- Picture B requires the ZBW-half-cycle structure to be more rigorously characterized than is currently in the corpus
- Picture C requires substrate edge-coherence machinery that is less developed

If the next Claude finds Picture A obstructed at theorem level, Pictures B and C are available as alternatives. This is registered in the v1.0 paper §4 and the handover.

### The three sub-claims that constitute the closure

Picture A factors into three sub-claims, each of which must be derived from CPP axioms:

**Sub-claim (a)**: In the unbound regime, DI-bit *send-side* (the propagating CP's choice of next-vertex) and *receive-side* (the substrate Dipole Pair's orientation at the receiving vertex) are statistically independent.

**Sub-claim (b)**: Coherent-channel propagation requires both sides to align (AND structure), and at amplitude level this gives $A_\mathrm{joint} = A_\mathrm{send} \times A_\mathrm{receive}$, so $|A_\mathrm{joint}|^2 = |A_\mathrm{send}|^2 \cdot |A_\mathrm{receive}|^2$.

**Sub-claim (c)**: Each side aligns with probability $1/z$ — for send-side, by icosahedral symmetry of the 12 nearest-neighbor directions in the 600-cell coordination; for receive-side, by icosahedral symmetry of the 12 substrate Dipole Pair orientations at any vertex, plus thermal equilibrium of substrate orientations (axiom-level).

If all three hold, $\sigma_\mathrm{channel} = 1/z^2$ follows.

### Where the back-fit risk lives

**Sub-claim (a) — independence — is where the rigor question lives.**

Sub-claim (b) is essentially the definition of coherent-channel propagation; it factors cleanly through quantum-mechanical amplitude composition.

Sub-claim (c) is clean *if* uniform-probability over 12 orientations is justified. The justification is: substrate is at thermal equilibrium, icosahedral symmetry is exact (A2), so uniform distribution is the equilibrium distribution. This should hold at axiom level.

But sub-claim (a) — independence — is non-trivial. In the bound regime, the cage anchors orientation: send-side and receive-side are correlated because both are constrained to cage geometry. In the unbound regime, there is no cage. But "no cage" doesn't immediately imply "independent send-side and receive-side". There could be hidden correlation through the substrate Dipole Pair structure itself — even without a cage on the propagating CP, the substrate could have orientation correlations between Dipole Pairs at neighboring vertices.

The current SF-4 v1.0 §4.3 Picture A description (lines roughly 880–920 of the .tex source, see exact location at compile time) handles this with prose like "two independent factors of $1/z$" without rigorously establishing independence. **This is the place where the v1.0 PARTIAL CLOSURE designation is most load-bearing.** It is also the place the next Claude must focus the rigorous work.

### Possible outcomes of the rigorous derivation

The next Claude should approach (A) with all three outcomes genuinely live, not pre-committed to outcome 1:

**Outcome 1: Independence holds exactly.** $\sigma_\mathrm{channel} = 1/z^2$ confirmed. SF-4 absolute scale theorem-level derived. Conditional on the channel enumeration $d_\mathrm{eff} = 5$, this closes OPEN-FP-SF-4-1 fully. SF-4 v2.0 update converts the absolute-scale claim from PARTIAL CLOSURE to full closure.

**Outcome 2: Independence holds approximately with corrections of order $\epsilon$.** $\sigma_\mathrm{channel} = (1/z^2) \cdot (1 + O(\epsilon))$ where $\epsilon$ is set by substrate orientation correlation length. SF-4 absolute scale derived to leading order, with sub-leading corrections that may or may not affect the 2% empirical match. This is probably the most plausible outcome based on general substrate-physics intuition.

**Outcome 3: Independence fails.** Send-side and receive-side have order-unity correlations in the unbound regime. The three convergent pictures don't actually converge; they're three different ways of stating the same independence assumption. Picture A is not closeable in its current form. This would be a major setback for SF-4 and would force re-architecting the suppression mechanism.

**The next Claude should not pre-commit to outcome 1.** The honest derivation might produce outcome 2 (most likely) or even outcome 3 (worst case). Either of those is a programme-level result that needs to be reported clearly. Discovering that Picture A doesn't close cleanly is itself valuable information — it would route the closure through Pictures B or C, or force re-examination of the channel enumeration $d_\mathrm{eff} = 5$, or in the worst case force re-architecting the suppression mechanism entirely.

### Specific axiomatic touch points to focus

When the next Claude starts work on (A), these are the CPP axioms most directly relevant:

- **A1 (CP existence)**: foundational; not load-bearing for this derivation
- **A2 (600-cell topology)**: gives icosahedral symmetry at each vertex; supplies $z = 12$
- **A3 (Dipole Sea / DI-bit propagation)**: this is the central axiom for Picture A; need to extract what DI-bit exchange looks like at sub-vertex level
- **A4 (SSV interaction / Nexus)**: relevant if substrate-substrate interactions create orientation correlations
- **A6' (Walk-Dimension Gauge Principle)**: probably the most relevant for the unbound-regime walk-dimension framework; $\sigma = N^{-d}$ from substrate walk-dimension primitives
- **A8' (recurrence)**: might be relevant; check
- **A11 (substrate equilibrium)**: relevant for the thermal-equilibrium assumption underlying sub-claim (c)

The next Claude should consult `axiom-registry.md` to verify these axiom mappings; the registry is the canonical reference.

### Done criteria for (A)

Closure of (A) is recognizable when:

1. **Sub-claim (a) is proved or disproved from axioms.** The proof should explicitly identify the substrate orientation correlation length and demonstrate that it is short enough (or zero) for independence to hold in the unbound regime. If the answer is "independence holds approximately with corrections of order $\epsilon$", $\epsilon$ should be estimated from substrate parameters.

2. **Sub-claim (b) is verified at amplitude level**. The AND structure of channel coherence is shown to factor into amplitude product, and the squared modulus gives joint probability. This is straightforward but should be stated rigorously, not assumed.

3. **Sub-claim (c) is verified for both sides.** Send-side: equilibrium distribution over 12 send-directions is uniform by icosahedral symmetry. Receive-side: equilibrium distribution over 12 substrate Dipole Pair orientations is uniform by icosahedral symmetry plus thermal equilibrium.

4. **The channel enumeration $d_\mathrm{eff} = 5$ is independently verified** — currently this is "3 spatial + 1 ZBW phase + 1 orientation" with the integer 5 chosen partly because it matches data at 2%. This is the second-most-load-bearing claim after sub-claim (a). The next Claude should verify $d_\mathrm{eff} = 5$ from channel-enumeration first principles, independently of the empirical match.

5. **A SF-4 v2.0 update lands** with the closure incorporated. This is a substantial revision — title block, §4.3 Picture A section rewrite, §4.4 channel enumeration rewrite, §10.1 OPEN-FP-SF-4-1 status update from PARTIAL CLOSURE to closed (or status update to a different level depending on outcome). The v2.0 update would be the second flagship revision of an SF-line paper after v1.0 SHIP.

6. **theorem-registry.md update** with new theorem entry for the closure (e.g., THEO-SF-4-4 "Per-Channel Suppression from Substrate Independence") if outcome 1 obtains. Or, if outcome 2 obtains, the existing THEO-SF-4-1 closure status updates with a new conditional clause about substrate correlation length.

### Realistic effort estimate

5–10 focused sessions, per the original SF-4 v1.0 estimate. The breakdown:

- **2–3 sessions** on sub-claim (a) — substrate orientation correlation-length analysis from A3 + A4 + A11. This is the load-bearing work.
- **1 session** on sub-claim (b) — amplitude-level AND structure (probably faster but worth a dedicated session for rigor).
- **1–2 sessions** on sub-claim (c) — equilibrium distribution justification.
- **1 session** on $d_\mathrm{eff} = 5$ first-principles channel enumeration verification.
- **1–2 sessions** on integration into SF-4 v2.0 update + theorem-registry + paper-catalog + Research_Frontier programme-state-changes capture.

Each session ~200 lines of substantive .tex content + reasoning capture. Rough total: 1500 lines of new derivation work + revisions to existing v1.0 sections.

---

## Item (B) — SM-5 antibonding-doublet open problem cooperation

### What this item actually is

OPEN-FP-SF-4-2 (vertex-by-vertex K3-coupling theorem) is currently at PARTIAL CLOSURE via Route C structural argument. The remaining work is theorem-level closure of the V=4 vs V=30 split between $\nu_1$ and $\nu_3$. This split is forced by SM-5's antibonding-doublet TBM-direction selection — specifically by the choice of $\phi_-^{(1)} = (2,-1,-1)/\sqrt{6}$ (μτ-symmetric) and $\phi_-^{(2)} = (0,-1,1)/\sqrt{2}$ (μτ-antisymmetric) as the basis vectors spanning the K3 antibonding 2D subspace.

SM-5 explicitly registers this selection as an open problem: any orthonormal basis of the 2D antibonding subspace is K3-equivalent at the spectral level. SM-5 ansatzes the TBM directions; SF-4 inherits the ansatz.

**(B) closure means proving the SM-5 antibonding-doublet TBM-direction selection from first principles.** This is a SM-5 paper-level theorem, not a SF-4 paper-level theorem. SF-4 cannot close (B) without going into SM-5 and proving the SM-5-side theorem.

### Coupling analysis: (A) and (B) are independent at axiom level but coupled at programme level

**At axiom level**: (A) and (B) touch different axioms, different substructures, different proof techniques.

- (A) is *substrate-mechanism* work — derivation from how DI-bits propagate in the Dipole Sea; touches A3, A4, A6', A11 most directly; output is a substrate-level mechanism-derivation theorem.
- (B) is *spectral-theory* work — derivation from how K3 eigenmodes interact with substrate symmetries; touches A2 (600-cell topology) and A4 (Nexus) most directly; output is a K3-spectral-structure theorem.

The two can be pursued in parallel by different sessions or sequentially without one blocking the other.

**At programme level**: (B) closure is gated on SM-5 work, not SF-4 work. Closure mechanism is:

1. Someone (next-context Claude or future-context Claude) does focused work on SM-5's antibonding-doublet open problem
2. Closure of the SM-5 problem produces a specific TBM-direction selection (or proves there's a unique selection)
3. SF-4 then absorbs the SM-5 closure by inheritance, automatically closing OPEN-FP-SF-4-2

So (B) is really an SM-5 work item that benefits SF-4 as a side effect. The cooperation framing is: SF-4 work could help SM-5 closure (e.g., providing the cage-shell-mass-coupling constraint as additional motivation, providing Route C structural argument as a useful starting point), but the primary work is SM-5-side.

### Recommended sequencing

**Do (A) first.** (A) closes a SF-4-internal open problem, doesn't require touching SM-5, and converts SF-4 from "ratios derived + absolute scale at PARTIAL CLOSURE" to "ratios derived + absolute scale derived". This is the bigger architectural payoff.

**Do (B) opportunistically.** After (A) closes, the next Claude can choose between:
- Path B1: Continue with (B) directly — focused work on SM-5 antibonding-doublet theorem, cross-sector mutual closure
- Path B2: Hand off (B) to a future SM-5 revision session and start SF-2 EW-flagship work

Either path is defensible. Path B1 is cleaner architecturally (SF-4 closure complete before moving to SF-2). Path B2 is faster programme-wide (SF-2 starts sooner; SM-5 revision happens at its own pace).

Thomas's preference at Session 54 close was implied to be Path B1 ("we should do some more before we move on to SF-2"), but the explicit decision point was framed around (A) priority, not (B) sequencing. The next Claude should re-engage Thomas on the (B) sequencing decision after (A) closes, with the trade-offs above.

### Done criteria for (B)

If pursuing (B) directly (Path B1):

1. **SM-5-side theorem proved**: a CPP-physical reason why specific TBM directions $\phi_-^{(1)}$ and $\phi_-^{(2)}$ are selected from the 2D antibonding subspace. The natural candidates are: (a) cage-shell-mass coupling (which would tie back to SF-4's V=4/V=30 distinction as the *cause* of the TBM-direction selection), (b) higher-order substrate symmetries beyond the K3 spectral structure, (c) thermodynamic arguments selecting equilibrium TBM directions.

2. **SM-5 paper-level revision** to v6+ incorporating the closure. SM-5 currently at v1; substantial revision needed.

3. **SF-4 v2.x update** absorbing the SM-5 closure via inheritance — Theorem 5.1 clause (iii) status updates from "SM-5-inheritance level" to "closed".

4. **theorem-registry.md updates** for both SM-5 (new theorem entry) and SF-4 (THEO-SF-4-1 status refresh).

5. **paper_catalog.md updates** for both papers.

If pursuing (B) opportunistically (Path B2): no immediate work; (B) waits in queue until SM-5 revision session naturally arrives.

### Realistic effort estimate

If Path B1 (cooperative closure): 5–10 sessions on top of (A). The breakdown is comparable to (A) since the work is substantively similar in scope.

If Path B2 (opportunistic): 0 SF-4 sessions; 5–10 sessions on the eventual SM-5 revision whenever it happens. The SM-5 revision work would absorb (B) closure as a natural side effect.

---

## Parallel track: human reviewer outreach

This track does NOT gate (A) or (B). It runs in parallel with the substantive work. Thomas's preferred venue (per the SS-9 model) is OSF deposit + arXiv submission with the explicit framing "open invitation post-public-posting".

### Concrete steps

1. **OSF deposit** of SF-4 v1.0 .tex + .pdf to the existing CPP project (DOI 10.17605/OSF.IO/JXE8D from the SS-9 batch). This is housekeeping work; estimated 0.5–1 session.

2. **arXiv submission** of SF-4 v1.0. Category: hep-ph (high-energy physics phenomenology). Estimated 0.5–1 session.

3. **Solicitation strategy**: After arXiv submission, Thomas can reach out to specific neutrino-phenomenology researchers via professional networks (his network may include some via the broader physics community; if not, the arXiv submission itself serves as the open-invitation venue per the SS-9 protocol). Specific names worth flagging:
   - The NuFIT collaboration (if any are open to engagement)
   - The JUNO collaboration on the JUNO 2025 first-physics-results paper (arXiv:2511.14593) authors
   - Specific theorists working on neutrino mass models with discrete flavor symmetries (Altarelli/Feruglio review co-authors, Ma-Rajasekaran follow-ons)

4. **Reviewer-letter template**: The SS-9 post-ship submission guide (`series_strong/papers/SS-9/letters/SS-9_post_ship_OSF_arXiv_submission_guide.md`) is the template. For SF-4, the analogous guide should be drafted as part of the OSF/arXiv submission session.

5. **Incoming review correspondence** lands at `flagship_papers/neutrinos/reviews/external/` (new directory; create on first incoming review). Internal LLM review correspondence stays in the documentation suite.

### How this interacts with (A) and (B)

If a human reviewer surfaces issues with the v1.0 paper:
- Issues that affect substantive content → SF-4 v1.x revision (re-opens the .tex; documentation suite captures the revision arc)
- Issues that affect Picture A specifically → directly informs the (A) work; could change the closure target
- Issues that affect K3-coupling specifically → directly informs the (B) work
- Issues at presentation-only level → minor revision without affecting (A) or (B)

The next Claude should treat human reviewer correspondence as higher priority than internal queue work when it arrives — incoming reviews are perishable in the sense that responsiveness signals professionalism.

---

## What NOT to do in the next session

A few things the next Claude should explicitly avoid, based on lessons from the Session 54 conversation:

**1. Don't produce the SF-4 7-companion documentation suite (FAQ, glossary, mechanism, phenomena, philosophy, keywords, reviews) before (A) closes.** The audience-facing layer should reflect the strongest version of the paper. Producing those files at v1.0 PARTIAL CLOSURE state means writing them twice — once in PARTIAL CLOSURE language, once after (A) closure. Worse, the first version risks crystallizing the partial-closure framing in audience-facing documents, which makes the rewrite harder.

The four-tier suite (handover/development/transcript/reasoning) is *internal* documentation about the campaign; correctly frozen at v1.0. The 7-companion suite is *external* documentation about the paper's claims; should ship after the claims stabilize via (A) closure.

**2. Don't revisit the SS-9 7-companion suite decision** without explicit Thomas conversation. The SS-9 catalog entry explicitly states the four-tier-only pattern is correct for SS-9. If Thomas wants to revisit that pattern, it's a programme-discipline decision, not incidental session work.

**3. Don't pre-commit to outcome 1 ($\sigma_\mathrm{channel} = 1/z^2$ holds exactly) when starting (A).** The honest derivation might produce outcome 2 or outcome 3. The whole point of doing the rigorous closure is to discover which.

**4. Don't conflate (A) and (B).** They're independent at axiom level. Mixing them creates conceptual confusion. Pick one and stick with it for the session.

**5. Don't try to do (A) at the end of a long session.** This is the same back-fit-risk concern that motivated the handover. (A) needs a session where the next Claude has full bandwidth and minimal pattern-matching to existing paper text.

---

## Apply mechanics for the next context

When the next Claude opens, current state at the moment of next-context-open:

- HEAD will be at `707230f` (SF-4 v1.0 SHIP commit) after Thomas pushes patch 0314 — verify with `git log --oneline -1` from `~/Documents/GitHub/CPP`
- Sandbox at `/home/claude/CPP` resets between sessions, so re-clone fresh: `cd /home/claude && rm -rf CPP && git clone --depth 1 https://github.com/Hyperphysics-Institute/CPP.git`
- No working files preserved; all relevant state is in the .tex source + documentation suite + transcript §17
- todolist.md should still show P1-empty status (Session 33 todolist discipline; verify on session start)

For Picture A formalization specifically, the working pattern should be:

1. **Re-read the reference materials** in the read-order list above — especially `reasoning-SF-4.md` Section 2 (which captures the original three-pictures decision) and `sf-4_neutrinos.tex` §4.3 (current Picture A description)
2. **Re-engage with axioms A1–A11** via `axiom-registry.md` and `templates/operating_system.md` — the Walk-Dimension Gauge Principle (A6') is the most relevant; verify at session start
3. **Set up a working sketch document** at `flagship_papers/neutrinos/sketches/SF-4_picture_A_axiomatic_closure.md` — this is where the derivation lives until it's ready to migrate to the .tex revision
4. **Work in the order**: sub-claim (a) substrate independence → sub-claim (c) equilibrium distribution → sub-claim (b) amplitude AND → $d_\mathrm{eff} = 5$ verification → integration to v2.0 update
5. **Capture Tier 4 reasoning** in real-time as the derivation progresses; the reasoning capture is what makes the closure recognizable as such versus "I wrote some equations that hand-wave the answer"

---

## Working conventions Thomas uses

(For continuity; the next Claude almost certainly already knows these from memory but worth reiterating.)

- **Patch numbering**: continue from 0314. Next patch is 0315.
- **Apply method**: `cd ~/Documents/GitHub/CPP; git am ~/Downloads/0315-*.patch; git push origin main` — or use the `cpp-apply` shell function defined in `~/.bashrc`
- **PDF policy**: ship .tex AND .pdf together for v1.0+ flagship papers; use `--binary` flag on `git format-patch -1 -o /mnt/user-data/outputs/` when patch contains PDF
- **CPP filename convention**: filenames never include version suffixes (e.g. `sf-4_neutrinos.tex` stays fixed); version history tracked only in internal CHANGELOG header
- **Reviewer protocol**: submit .tex source not PDF rasterization (lesson from SS-9 cache-resolution issues; .tex source avoids OCR misreads like the Copilot "z/4" misread of $z/\varphi$)
- **Sandbox cloning**: always `git clone --depth 1` fresh each session; sandbox resets between sessions

---

## What "session 55+ success" looks like

If the next 5–10 sessions go well, here's the state the programme should be in by the end:

- **OPEN-FP-SF-4-1 closed at theorem level** (or registered with a quantitatively-bounded conditional structure if outcome 2 obtains; or honestly reported as obstructed if outcome 3 obtains)
- **SF-4 v2.0 SHIPPED** absorbing the (A) closure
- **theorem-registry updated** with new theorem entry from (A); SF-line section now has 3 theorems + 1 proposition (or 2 + 1 + 1 conditional, depending on outcome)
- **paper_catalog updated** with SF-4 v2.0 SHIPPED row
- **Tier 4 reasoning** captured for the (A) closure derivation
- **Optionally**: (B) closure work started or completed (Path B1)
- **Optionally**: human reviewer correspondence incoming (parallel track)

If outcome 3 obtains (Picture A obstructed), success means a *different* deliverable: an honest report that Picture A doesn't close cleanly, registration of Pictures B and C as alternative closure paths, and updated SF-4 v1.x with revised PARTIAL CLOSURE framing reflecting the obstruction. This would be valuable programme-level information even though it's not the desired outcome.

---

## A note from current context to next context

Thomas and I had a good Session 54. SF-4 v1.0 SHIPPED. Five-pass review converged. The four-tier documentation suite landed clean. Theorem registry, paper catalog, transcript §17 all in place.

The post-ship quality assessment was honest — SF-4 is a *good* partial-closure flagship, not a *great* full-closure flagship. The honest assessment surfaced (A) Picture A formalization as the highest-leverage work to do next. Thomas accepted that prioritization and chose handover over end-of-context attempt at (A).

That decision was correct. Picture A is foundational-derivation work that benefits from a fresh context window. The work matters for the programme — SF-4's load-bearing capacity in SF-7 depends on it.

**The single most important thing for the next Claude to internalize**: don't pre-commit to outcome 1. The integrity of the programme depends on Picture A closure being a real derivation from axioms forward, not a back-fit dressing of the known answer. If outcome 2 obtains, that's fine. If outcome 3 obtains, that's also fine — it's information. What's not fine is producing reasoning that *looks* like outcome 1 closure but is actually back-fit prose.

The next Claude has the cognitive bandwidth that the current Claude no longer has. Use it well.

Good luck out there.

— Claude Opus 4.7, Session 54 close, 9 May 2026
