# F5 / OPEN-SM-11 — Premise Correction: SF-2 Has No Generation-Transition Structure

**Patch:** 4102. **Lane:** EW (SM cross-lane). **Status:** CORRECTION to Patch 4096, my own.
**Trigger:** Session-233-close priority (b), the SF-2/CKM campaign. Before opening it, the
Session-186 governance discipline was applied — *re-read the patch that registered the item
and check its premise against what has landed since.* The premise did not survive.

---

## 1. The claim that was wrong

OPEN-SM-11 (registered Patch 4096, by me) states the target as:

> "Derive the CKM quark mixing matrix elements and the quark CP-violating phase
> δ_CP ≈ 65.5° from **SF-2's generation-transition structure**."

**There is no such structure.** An unscoped corpus search (`--include=*.tex --include=*.md`,
whole tree) returns the phrase in exactly six places — `frontier_sectors/SM.md`,
`frontier_sectors/EW.md`, the maturation document, `reasoning/4096.md`, and the two
session-233 handovers. **Every one of them is downstream of Patch 4096.** The phrase appears
nowhere in SF-2, nowhere else in the corpus, and nowhere predating 18 Sep 2026. I supplied it
and then cited it back.

## 2. What SF-2 actually says — the opposite

SF-2 §`sec:W_universality`, **Proposition (Universality)**:

> "The W⁰ catalytic mechanism … is **identical for all source-particle generations and
> types**. Any source CP in a high-SSV-gradient host configuration is subject to the same
> centroid-capture process at the same rate (modulo kinematic factors)."

SF-2's structural claim is **generation-blindness**, and it is load-bearing: it is how SF-2
derives SM lepton universality and the absence of tree-level FCNC. A generation-blind
mechanism is the wrong shape to generate generation-dependent mixing angles.

Where CKM appears in SF-2 it is an **input**, not an output: hadronic branching channels are
"CKM-weighted" in the τ-decay postdictions. The corpus's own book chapter on SF-3 says it
plainly — the sector "does not derive" the mixing structure.

## 3. What SF-2 does offer — and its actual status

SF-2 §`sec:cap_sf2_attempt` (Phase 7):

> δ_CP^(CKM) = arg(Capotauro phase factor) ≈ 65° (structural prediction)

with the explicit rider: *"matches at the ~1% level **if** the Capotauro phase factor closure
proceeds as outlined."* SF-2's own summary table lists δ_CP^(CKM) ≈ 65° and δ_CP^(PMNS) ≈ 195°
as **"Conjectural (Phase 7 OPTIONAL)"**, and SF-2 pre-registers the failure branch honestly
("If Capotauro fails: the attempted closure is honestly registered as a failed cross-sector
hypothesis; SF-2 v1.0 still ships intact").

So the route exists, but it runs through **Capotauro**, not through generation structure.

## 4. arg(Capotauro phase factor) has never been computed

Unscoped search for the phase factor: five hits, all inside SF-2's Phase 7 section, all
**statements of the target** rather than evaluations of it. No file in the corpus computes
arg(Capotauro phase factor).

## 5. The consequence that matters — F5 is not an independent route

The June 2026 SF-2 external-validation campaign (1200 band, Patches 1201–1205) put δ_CP to a
three-reviewer panel. **SQ1 returned 3/3: no derivation chain** for the 193.3° signpost —
"empirical coincidence / back-calculation / signpost-only." Adjudicated **RESTATEMENT-NEEDED**
at Patch 1202: δ_CP is long-horizon (2028+), contingent on the capacity engine delivering
sign(μ²) via H1.

That panel audited the **PMNS** signpost (193.3°). The **CKM** value (65.5°) was never
audited — but it sits in the identical evidential position, and it depends on the **same**
Capotauro phase factor, hence the **same** H1 blocker.

H1's state since: refuted on the squared-occupation class (4056/4057), reopened conditionally
(4062), **neither refuted nor restored** as VW-2 defines it (0983), and VW-a-4 refuted on the
single-walker measure (0993). It has not delivered sign(μ²).

**Therefore F5 is not a fresh, untried SF-2 campaign. F5 reduces to the H1/Capotauro blocker
that was already adjudicated long-horizon in June.** Opening a generation-structure campaign
would have spent a session rediscovering that.

## 6. Status changes

- **OPEN-SM-11 premise corrected** in all six locations. Target restated: δ_CP^(CKM) via the
  Capotauro phase factor, contingent on Capotauro closure, contingent on H1 — *not* via a
  generation-transition structure, which does not exist.
- **F5 restated**: OPEN, and **not independent of H1**. χ₄'s panel-readiness is blocked by
  H1, not by an unattempted SF-2 derivation.
- **New item**: the 65.5° CKM signpost deserves the provenance audit the 193.3° signpost got
  in June (TODO-4102-CKM65).

No verdict moved. χ₄ remains NOT panel-ready, now for a more precisely located reason.

## 7. Governance note

The Session-186 handover recorded that "an item can outlive its own justification and be
handed forward indefinitely," and prescribed re-reading the registering patch before working
any carried-over item. Here the item was two days old and the false premise was **my own**,
introduced at 4096 and propagated to six files including two handovers. The discipline caught
it in one session instead of many. The lesson is narrower than the 186 note's: *a premise you
wrote yourself reads as corpus fact three patches later.* An unscoped grep distinguishes them;
nothing else does.
