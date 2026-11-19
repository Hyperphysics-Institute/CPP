# Session 244 — Fresh-Context Critic Returns, Verbatim

**Filed:** Patch 4488, 18 November 2026. Each report is the final message of an independent sub-agent with no stake in the
work, reproduced verbatim (AI output, not founder text). The fragment that acted on it:
`series_standard_model/axiom_maturation/4488_reading_the_copilot_conversation.md`.


## Patch 4488 — Independent critic of the reading of the Copilot conversation (4483–4486)

VERDICT: ACCEPT WITH CHANGES

The verify script runs 5/5 PASS, and the §4.3 table matches its output exactly (D-11). The central conclusion stands: anything a CP carries and reads on its own at the detector cannot reach 2√2, and the corpus home for the tie is the Nexus. But there are wrong citations, a superseded registry clause, a weaker-than-favourable reading of the founder's map, a missed corpus prior, and a carry-forward list that does not match 4481 §5.

REQUIRED CHANGES
1. **§4.3 and title: the founder's map is not read at its strongest (D-15).** In 4485 he says the parameter the CP watches "is the state of entanglement, which means direct connection/communication regardless of address of the CP". He also says the CP will "respond to a collision with its entangled CPs".
   - Fix: quote both lines in §4.3. State that his own wording already reaches for a link that ignores distance (the Nexus reading). Only the "carried copy" reading falls under the L1 bound.
   - Retitle so the title no longer says "the Founder's PSR Map … Cannot Reach the Measured Bell Value". Say instead that a carried-copy reading cannot reach it, and his "direct connection" reading is the Nexus.
   - Add to §9 Marked: choosing the carried-copy reading for the test was the branch convenient to Claude.
2. **§4.3: the main corpus prior is not cited (D-3, D-10).**
   - QM-3 already withdrew this exact local model: `QM-3_bell_entanglement.tex` l.128–131, "The previous CPP argument was wrong… a fixed DI-bit pool set at emission… LHV… |CHSH| ≤ 2". 4477 §2 already corrected the website-era "PSR chaining without non-locality".
   - `series_quantum_mechanics/code/3315_qm3_bell_verify.py` checks 5, 2, 4 and 0 already do what rows L1, J1, the no-signalling row and P1 do.
   - Fix: cite these, and replace "now with the script behind it" with "restating QM-3's retraction and 3315 check 5 for the per-CP case".
3. **§4.3: list every assumption behind the bound.** Add these:
   - Nothing carrying the far setting updates the record before the local outcome. Under A3′ the relay runs at c, so a map rebuilt each Moment from arrivals stays local.
   - Measurement independence holds only up to O(ε).
   - Add CONV-031 §3.3: the smallness of ε is itself underived (calibration b), and the superdeterminism story is not an independent derivation pending K₀(λ) (calibration a).
   - Change "so the bound applies to CPP as registered" to "applies to CPP as registered, given ε small (underived, CONV-031 §3.3)".
4. **§4.1, DI-bit bullet: the cited clause is superseded.** AP-2's {charge, type, origin address} was replaced by AP-4 (Patch 3032).
   - Fix: "DI-bit (A1′, AP-4, superseding AP-2): exactly {origin address, E, S}, a static snapshot; no per-messenger phase; 4120 adds A_i provisionally."
   - Also correct the packet: the registry has LSP′ = (x_GP, t_abs; Φ, V_i, Q_ij), not "(origin address, t; …)".
5. **§4.4: the GP's computed state is not a map.** The registered computed state is the census moments (Φ, V_i, Q_ij, provisional A_i). Line 403 of the axiom registry has the far-CP state as the mean over the PSR shell.
   - Fix: "the origin addresses that would build such a map arrive each Moment, but the registered state keeps moments, not a per-origin map. Storing the map is new state (4481 placement iii)." Delete "exists already, as the GP's computed state".
6. **Attributions.**
   - §2 and §4.2 quote "The Nexus is not local" as QM-3. It is in `papers/FAQ-QM-3.md` l.11; QM-3 says "despite being non-local". Cite FAQ-QM-3.
   - §4.2 cites "CONV-031 §1" for "the Nexus maintains this joint state globally". That section is the seat ledger. The phrase is in `QM-3_bell_entanglement.tex` l.90. (4478 §4 carries the same error.)
7. **§4.2 table, §5, title and §8: the archive sentence is misdated and misattributed.**
   - The archive file is dated 2025-09-09, not January 2026. The 29 January 2026 date belongs to the unfiled Word document, which was written with Grok.
   - Copilot did not quote the sentence back. 4486 records Copilot's paraphrase, and the filer added the archive quote.
   - The quote begins "Quantum Group Entities (QGEs) orchestrate…" in the source.
   - Fix: "his September 2025 website wording (archive, Part 4)". Drop "which Copilot quoted back from his Word document". Restore the opening words of the quote.
8. **§4.3, tensor-network paragraph: the physics is imprecise.**
   - In a tensor network each site's tensor holds one leg of the bond. The non-local step is the contraction plus the Born rule on the joint amplitude. It is not that the bond "belongs to neither end".
   - Fix: "per-site amplitude and phase (FI-QMRG-1) describe single-site patterns. A non-product joint amplitude lives on configuration space, so outcomes need a joint step, which in the registry is the Nexus."
   - Change "the tie cannot sit in what each CP carries" to "the tie cannot be read out from what each CP carries without a joint step."
9. **§5, the condition: no-signalling applies to selection too.** Stating only "no momentum of its own" is incomplete. Choosing among allowed moves also signals if B's weights depend on A's setting.
   - Fix: add "and the selection weights at one side, summed over the other side's outcomes, must not depend on the other side's setting (THEO-QM-5)". Copilot's "shapes the probabilities" is agreement only under that condition.
10. **§2 and §7(e): wrong target for Jacques 2007 and Ma 2013.**
   - Both experiments test whether the photon commits at entry (or whether erasure can act retrocausally). They do not test light-speed collapse.
   - Light-speed collapse is already ruled out in the corpus (Guerreiro et al. 2012, 4477 §3), and the founder withdrew light-speed timing (4478 f).
   - Neither experiment changes one arm at a spacelike-separated event: Jacques changes the output beamsplitter; Ma changes the erasure basis on the partner photon.
   - Fix: "close relatives of Copilot's test have been done". Retarget them as constraints on readings that commit at entry and on 4477(g), the pilot-wave rival (which survives both). Join them to 4478(g) only in its "local locking" form. Make §7(e) say that.
11. **§3: his bonded-entity claim is undersold (D-15).** At its strongest it is standard QM: bound states are internally entangled (the bonding electron pair is a spin singlet; electron–nucleus relative coordinates). That entanglement survives warm surroundings because the internal levels are gapped.
   - Fix: replace "it is a membership claim… not a claim that every pair carries a Bell-testable joint state" with that statement. Add that it is out of reach for experiment in practice, not absent in principle.
12. **§4.1: the "fifth element" count picks one reading of an ambiguous count.** The founder's first bullet puts the term "carried by the GP". 4481 §2 already counted GP channels (Φ, V_i, A_i, Q_ij, with the origin address as the possible fifth).
   - Fix: give both counts (CP: polarity, type, position, spin; GP: the four channels, with the origin address as the fifth), and do not presuppose either in §6.
13. **§7: the carry-forward list is wrong.** 4481 §5 runs (a)–(e), not (a)–(c).
   - 4481(b), the Copilot reading, is discharged by this patch and must be marked "answered (4488)", not carried.
   - 4481(d), the founder question 4481 §4, needs a disposition. Its first part is answered in part by his count. "Where the tie is kept" is answered in part by his "direct connection regardless of address".
   - 4481(e) dispositions must be carried.
   - 4478 (a)(b)(h)(i) and 4477(e′) are already inside 4481(c) word for word. Listing them again separately is redundant, and it suggests 4478 (c)(g)(j) were dropped.
   - Add "(f) Founder question 4488 §6" and "(g) Dispositions".
   - Move (c) out of the "New" heading, since it says itself that it is not new.
   - Add a 4488 entry to `todolist.md` in the same patch (D-9; none exists yet).
14. **§6: the founder question is reframed.** As written, its first option is one he already ruled out ("regardless of address"), and it leads him toward "membership card".
   - Fix: keep the pair-a-mile-apart picture. Then ask what the shared thing holds for the pair, and what changes in it at the far end when photon A is caught. This is 4481 §4's still-open second and third questions.

OPTIONAL NOTES
1. Copilot's lines are quoted from the filed summaries (4485 and 4486 say "not filed verbatim"). Mark them "(as summarized at 4485/4486)".
2. §4.5 row 1 says "Nothing on capacity", but row 8 uses AP-5. AP-5's per-GP cap K is the nearest capacity object (a cap on arrivals, not on shared correlation). Cite it in row 1.
3. §5 "Momentum already travels by the relay" needs a registry anchor (D-7). R-CP-ONLY-SOURCE (the CP is the only source of every signal's size and direction) directly forbids a push from the entanglement matrix that no CP sources. That is a stronger anchor.
4. §3 says smallness "is exactly" indistinguishability. Better: it is a smooth measure, the overlap of the two mirror states, roughly exp(−q²/8σ_p²). Decoherence by the environment recording the recoil is a second route. Read the founder's "small" as small relative to σ_p.
5. Script row L2: uniform random mixtures pile up near the average, so the printed 1.35 says nothing. Print the analytic bound (the L1 maximum) or sample the corner points. The no-signalling row prints 0.5 under the "max |S|" column header, and it checks only A's marginal.
6. The archive's EMTT/QGE vocabulary is flagged in the Session 81 handover as older-framework vocabulary. Note this where it is used as anchor wording.
7. §4.3 bears directly on 4477(e′) (SD-1's "CPP is local" against QM-3's non-local Nexus). Cross-reference it.
8. Accurate as checked: "I accept your qualification, and limitations"; "adds NO state to the substrate"; CONV-031 Q4 "carried by the amplitudes, not the setting correlations"; THEO-QM-2 to QM-5 wording; 4481 §2's "local tag that the Nexus reads"; 4478's inheritance quote; the citations and contents of Jacques et al. and Ma et al.; the §4.5 row 4 branch-counting point; the swap and product-to-product exceptions.

PLAIN LANGUAGE
The reading gets the main point right. If each particle of an entangled pair carried only its own private notes, the pair could never produce the strong correlations that experiments measure. The link has to be something the two share, which CPP calls the Nexus. But the founder's own words already said the link works "regardless of address", so the document should credit him with that rather than test only the weaker version of his idea. It also needs to fix several citations: one rule it quotes has been replaced, two quotes point to the wrong files, and an archive sentence is misdated. One condition needs adding: even "choosing which move happens" must not let one side influence the other's odds. Two experiments are aimed at the wrong question. The list of unfinished items has to match exactly what was carried forward before. None of this overturns the conclusion; it makes the document accurate and fair to the founder.

---

## Claude's response to the 4488 return (not part of the verbatim report)

All fourteen required changes taken in, after spot-checking the critic's facts against the repo (QM-3 tex retraction and the "maintains this joint state globally" line; FAQ-QM-3 line 11; the archive date 2025-09-09; AP-4's {origin address, E, S} payload; R-CP-ONLY-SOURCE and the 4355 PSR-shell mean in the axiom registry; 4481 §5 (d)–(e); 4478 (g); 4477 (g); Guerreiro et al. in 4477 §3): (1) his "regardless of address" quoted and taken as the Nexus reading, the title rewritten, the carried-copy test marked convenient; (2) QM-3's retraction, 4477 §2 and 3315 cited as prior art; (3) the three assumptions and the CONV-031 §3.3 calibrations; (4) the DI-bit payload and LSP′ corrected; (5) §4.4 rewritten (moments, not a map); (6) FAQ-QM-3 and QM-3 tex attributions; (7) the archive dated September 2025, the Copilot attribution dropped, the quote restored; (8) the joint-step paragraph rewritten; (9) the no-signalling condition on selection added; (10) the two experiments retargeted; (11) the bonded-entity claim stated at its strongest; (12) both "fifth" counts; (13) the carry-forward list rebuilt against 4481 §5 (a)–(e), with (f) and (g) added and a todolist entry in this patch; (14) §6 re-asked as 4481 §4's open parts. Optional notes 1–7 taken (5 in the script: L2 now prints the vertex bound and sparse-mixture sample; the no-signalling row checks both marginals under a "value" column). The 4478 §4 mis-citation of CONV-031 §1 (critic's change 6) is filed as an owed correction in the todolist entry, not edited in 4478 here.


## Patch 4489 — Independent critic of the reading of the founder's Nexus-ledger answer (4488 §6)

VERDICT: ACCEPT WITH CHANGES

I ran the script with `python3 -I`. It exits 0, and its output matches the D-11 block in draft §3 (lines 56–69) character for character. The six checks are right: CKW for pure states uses tangle τ(A:BC) = 4·det ρ_A; W gives 8/9; GHZ gives zero for both pairs and 1 for A:BC; 2^300 ≈ 2.04×10^90. All four citations check out: CKW PRA 61 052306; Osborne–Verstraete PRL 96 220503; Pan et al. Nature 403, 515; and Fein et al. Nature Physics 15, 1242, whose abstract reads ">25,000 Da, up to 2,000 atoms, fringes >90% of expected visibility". The R-A4-ROLE quotes, the A4 row, the QM-3 sentence and the R-DS-BOUNDARY wording are all quoted correctly. No file in the repo reconciles R-A4-ROLE with QM-3's joint state, so §2 is right that this is open. The problems are four D-10 misses, one misreading of the founder's truncation, and several overstated physics claims.

REQUIRED CHANGES

1. **§1 line 25 and §9 line 161–162 (D-10, CONV-031 wording rule).** "First statement in the corpus of how the Nexus might keep QM-3's joint state" is false.
   - SD-4 (`SD-4_nexus_correlation_function.tex` ~l.178–208; `mechanism-SD-4.md` l.21–36) already has a report–compute–return shape. Every GP's δb_i enters a global sum Σδb_i = 0, and the "Nexus field μ couples all Grid Points globally".
   - QM-3 l.90–91 adds "enforcing total DI-bit conservation across all Grid Points".
   - The mechanism debt is registered as K₀(λ), OPEN-SD-1..4. CONV-031 package §5(i) says "HOW the Nexus computes the joint constraint".
   - **Fix:** say his shape is a founder-level statement of the role SD-4's μ plays and an input to OPEN-SD-1..4/K₀(λ), not the first. In §9, drop "first description anywhere in the repo". CONV-031 §3 adoption 2 requires that the Nexus label never be presented as the mechanism.

2. **§2 lines 41–42 (D-10 and accuracy).** "His 4489 message now gives the Nexus a third role… collecting, computing" is not new. QM-3 already has the Nexus enforcing DI-bit conservation. QM-4 `thm:unitary` (`QM-4_measurement_problem.tex` ~l.284–297) says "Global unitarity preserved by the Nexus". The cosmology files (`condition2_2ii_gradient_vs_mode_and_A4_horizon.md` l.29, 37) give A4 "computes the next state".
   - "The extraction goes further than his words" leaves out the context of 3059. Patch 3059 answered the 3058/1164 coordinable-region construction ("the Nexus binds what can still meet"). He read that as "creating and enforcing the ball of the observable universe". So the extraction's "coherence-enforcement" denies cosmological vacuum-coherence enforcement over a region, not QM-3's joint state.
   - **Fix:** state that context. Add reading (iv): R-A4-ROLE's "NOT coherence-enforcement" is scoped to the 3058 cosmological attribution, so it does not conflict with QM-3/QM-4. Mark (iv) as convenient to Claude along with (i). Recast "third role" as "a shape for the conservation and joint-state role QM-3/QM-4/SD-4 already give A4".

3. **§5 lines 107–113 and §7.2 (D-15, misreading).** His criterion is the size of the effect on a CP: drop a tie when its effect is below 1 GP displacement. His example is large-scale collisions whose effects are thin. That is not object mass. Read at its strongest, it drops weak, thinly spread ties. Under monogamy those are mostly environmental ties, and big objects keep their strong internal ties. That is close to the opposite of GRW/CSL, where heavy objects collapse.
   - **Fix:** add a reading (T-c): drop Schmidt weight, i.e. any tie whose effect per CP is below one GP step. This is standard tensor-network truncation, and it is non-unitary. Its testable signature is the loss of small-amplitude branches that are still coherent, such as weak-value or low-amplitude interference.
   - Keep the mass threshold (T-b) only as a secondary reading.
   - Rewrite §7.2 in his terms, so it does not lead toward "heavy enough". For example: "A tie so weak that it would move no CP by a full GP step — does the Nexus keep it while it could still interfere, or drop it?"

4. **§5 lines 111–113 (D-10, misattribution).** The `QM_series_development.md` l.92 sentence reads in full: "CPP is most similar to objective collapse models but derives its collapse mechanism (bit-sea decoherence) from first principles… not as a new postulate." That is decoherence, i.e. (T-a), not (T-b). QM-4 states "No collapse postulate is required" and proves global unitarity by the Nexus (`thm:unitary`). OPEN-QM-5 (`frontier_sectors/QM.md` l.118: "Entanglement Decoherence Threshold at ~10¹⁵ eV… from Nexus lattice path limits") is the registered threshold item. SD-1 has OPEN-P-SD-4, a decoherence threshold.
   - **Fix:** say (T-a) is what the development note and QM-4 already hold. Say (T-b)/(T-c) would contradict QM-4 `thm:unitary`, which needs a ruling. Cite OPEN-QM-5 and OPEN-P-SD-4 as the registered home of any threshold. Add both to §8(d).

5. **§4 lines 97–98 and §5 lines 104–106 (physics).** "Branches that have left records can never recombine… dropping the cross terms changes no future result" is overstated. A quantum eraser recombines branches that left a record, and the corpus treats erasers (4481; 4488 §7 (e), Walborn et al.).
   - **Fix:** say "records spread irreversibly beyond any practical recovery (for all practical purposes)". State that a pruning rule must not prune records an eraser can still undo. Join 4488 (e).

6. **§5 lines 105–106 (physics).** "Momentum is conserved in every branch… loses no momentum" is too strong. Branches selected by which-path (position) records are not momentum eigenstates. Dropping branches conserves momentum statistically (on average), as in standard measurement. It conserves it exactly in each run only when the branching respects total momentum (record basis compatible with P).
   - **Fix:** say "conserved on average (as in standard QM); per run only for momentum-compatible branchings". Note that GRW-type rules conserve mean momentum but heat the system, which is the same caveat.

7. **§4 lines 94–96 (physics).** "Typical states carry far less entanglement than the maximum" is wrong. Haar-typical states are near-maximally entangled (Page). The compact states are low-entanglement ones: ground states of gapped local Hamiltonians (area law) and short-time evolution. A long evolution after a quench grows volume-law entanglement. Locality, not monogamy, is what drives the area law.
   - **Fix:** "states reached by local dynamics from low-entanglement starts, and gapped ground states, obey area laws and compress to bounded-χ tensor networks; generic long-time states do not, and there decoherence pruning is what keeps the ledger small."

8. **§3 lines 77–78 and §8(e) (D-7).** Two symbols are conflated.
   - Copilot's χ is a bond dimension in a tensor network. The entanglement across a cut is at most (number of cut bonds)·log χ, and χ across a block cut can far exceed 2 even with qubit sites. A budget of one ebit per two-level unit caps a site's total entanglement, not χ.
   - The CKW "budget of one" holds for qubits. Tangle-monogamy fails for qudits (Ou 2007). Squashed entanglement is monogamous for any dimension, with a budget of log d (Koashi–Winter 2004).
   - **Fix:** restrict "budget of one" to two-level units. Say a larger quantum, made of many ħ units, has budget log₂ d. Recast the χ suggestion as "a per-site cap, from which a χ bound follows only per bond".

9. **§1 lines 29–32 and §8(b) (port rule).** "Acts on B only through the chances… never as a value" is weaker than 4488 §5 condition (2). Chances that shift with A's setting would still signal.
   - **Fix:** "the port acts on B only through the chances of B's displacements, and those chances, summed over A's outcomes, must not depend on A's setting (THEO-QM-5); no local process can copy out the port's content". Link this to 4488 (b), the no-signalling filter.

10. **§1 and §8 (4488 (d) not engaged).** His message gives the count explicitly: "the state of the environment vector (SSV_abs, SSV_net (V_i), etc.)". This is the GP computed state. Its list differs from 4488's GP count (Φ, V_i, A_i, Q_ij), since SSV_abs is not in that count (AP-4b; FI-QMRG-1 gives √ρ). "Tensor register" may point at rank 2, which is Q_ij's rank, or at a new slot. 4481 (a) owes "rank 0/1/2".
    - **Fix:** in §1, record his list as answering 4488 (d)'s "which count" (GP). Note the SSV_abs difference and the rank question. Carry the rest into 4481 (a) and 4488 (d).

11. **§8 (D-9).** No 4489 entry exists in `todolist.md` yet (grep finds none). The draft uses deferral vocabulary: "owed reconciliation", "Carried", "stays owed".
    - **Fix:** in the same patch, file a 4489 entry with (a)–(g) word for word, plus the new items from changes 2, 4, 5 and 10. Carry 4488 §7 (a)–(g), 4481 (a), (c), (e) and 4478 (a). Restate the 4478 §4 citation correction (todolist 4488, "critic change 6"). Run `code/deferral_gate.py`.

12. **Founder file (verbatim).** The text is word-perfect, but typography is normalized. The founder sent curly quotes and apostrophes (“direct connection regardless of address.”, they’re, B’s); the file has straight ones. The double blank line before "This is incomplete" became a single line.
    - **Fix:** restore them as sent, or add "(typographic quotes normalized)" to the header parenthetical. The added brackets around the pasted question are disclosed in the header, which is acceptable.

OPTIONAL NOTES

1. §3, D-15: "maximum amount of effect" has a second reading in the corpus. The per-Moment displacement cap (PSR reach ceiling; AP-5's K) already gives a maximum effect on a CP. It is worth one line beside monogamy.
2. §4, GHZ: every pair in GHZ has zero entanglement but nonzero classical ZZ correlation. A pairwise correlation table would therefore not be all zeros, but it still cannot tell GHZ from the mixture. Also cite CONV-031 §3 adoption 4(b), "multipartite entanglement within the CPP ontology", the residue this bears on (D-10).
3. §5: for "size" counted in atoms, entangled macroscopic mechanical oscillators (~10^12 atoms; e.g. Ockeloen-Korppi 2018) bound a size threshold beyond Fein et al. Collapse models are constrained as a rate–length pair (λ, r_C), not as a sharp threshold.
4. §6: SPDC photons do not leave with opposite momenta. Their momenta sum to the pump's, and their transverse momenta are opposite. Also, under (T-a), memory rests on records within the realized branch, not on global reversibility, which pruning breaks. QM-4 `thm:unitary` is the paper-level home for reversibility, beside QM-1 v2.0.
5. Script: the docstring refers to "M1-M3", but the printed table does not use those labels.
6. §7.1 is acceptable as an axiom-level question for him, but it could add the cosmological scope (change 2), so he can say whether 3059 was only about domains.
7. Under D-15, the chat reply must list what this critic changed.

PLAIN LANGUAGE: The draft is careful and its arithmetic checks out. Its claim that each particle has a limited "entanglement budget" is standard physics, and the program that tests it gives the same numbers as the document. It needs fixes before filing:
- It says Thomas's idea, the Nexus gathering every particle's report and handing back one universe-wide answer, is new to the repo. Earlier papers already have a version of it (a global "Nexus field" in SD-4).
- It reads his "drop effects smaller than one grid step" as "heavy things stop behaving quantum-mechanically". His words say "drop ties too weak to matter", which is a different idea with a different test.
- It overlooks a published CPP paper (QM-4) that already rules out true collapse.
- A few physics statements are too strong: that recorded alternatives can never rejoin (an "eraser" can rejoin them), that momentum is conserved in every single branch, and that typical states are easy to compress.
- The owed items still have to be written into the to-do list in the same patch.

---

## Claude's response to the 4489 return (not part of the verbatim report)

All twelve required changes taken in, after spot-checking SD-4's μ (mechanism-SD-4.md l.21–36), QM-4's thm:unitary and "No collapse postulate", OPEN-QM-5, OPEN-P-SD-4 and the cosmology file: (1) "first statement" replaced by "a founder-level statement of the role SD-4's μ plays, an input to K₀(λ) and OPEN-SD-1..4", in §1 and §9; (2) the 3058 context stated, reading (iv) added, (i) and (iv) marked convenient, "third role" recast; (3) reading (T-c) added as his criterion at its strongest, (T-b) made secondary, §7.2 rewritten in his terms; (4) the development-note sentence attributed to (T-a) with QM-4, (T-b)/(T-c) flagged as contradicting thm:unitary, OPEN-QM-5 and OPEN-P-SD-4 cited and added to §8(d); (5) decoherence pruning stated FAPP with the eraser limit; (6) momentum conserved on average, per run only for momentum-compatible branchings; (7) area-law wording; (8) budget restricted to two-level units, log₂ d for larger, χ recast as a per-site cap; (9) the port rule strengthened and linked to 4488 (b); (10) his GP list recorded against 4488 (d), the SSV_abs difference and rank question carried; (11) a 4489 todolist entry in this patch, the deferral gate run; (12) curly quotes and the double blank line restored, header notes typography as sent. Optional notes 1–7 taken (Ockeloen-Korppi et al. verified: Nature 556, 478, 2018, about 10¹² atoms each; Koashi–Winter cited as Phys. Rev. A 69, 022309, 2004). Claude's chat reply before this return had said "first description anywhere in the repo" and posed the cutoff question as heavy-versus-light; both are corrected in the reply that delivers this patch.


## Patch 4490 — Independent critic of the reading of the founder's two-jobs and weak-tie answers (4489 §7)

VERDICT: ACCEPT WITH CHANGES

The founder file is verbatim, and the D-11 table matches the script exactly. The required changes are about where rulings are marked, attribution, one wrong reading of the corpus (the lattice spacing), and one wrong physics citation (Hornberger 2003) that §4's question builds on.

**What I checked**
- **Verbatim:** I unwrapped the blockquote, took out the disclosed brackets and compared it with the message as sent. It is identical: text, curly vs straight apostrophes, double spaces and the counts of blank lines. The only losses are trailing single spaces ("applied. ", "apart? ", "transmission. ", "universe. ", "away. "), which is harmless in markdown. Line wrapping is disclosed and follows the 4489 founder file's convention.
- **D-11:** `python3 -I` exits 0, and the output is byte-identical to lines 67–75 of the draft (diffed).

**REQUIRED CHANGES**

1. **Founder file, R-A4-JOBS scope note.** It is written as if it were his ruling, unmarked. Draft §1 says "(Claude's extraction; the rulings file says so.)", but the rulings file does not say so.
   - Prefix the scope note: "*Claude's extraction (PD-008). He said he is not sure what he meant at 3059 ("I'm not sure what I meant at that time, in that context"), so this note rests on his present statement, not on what 3059 meant.*"
   - Mark "job (2) is the joint-state role QM-3, QM-4 and SD-4 already give A4" as Claude's reading, carried from 4489 §1, where it was marked "Claude's reading, not registered". He never said "coherence".
   - Also scope R-A4-ROLE's positive clause ("A4's role is THE synchronization"). It now reads as job (1) of two. The note currently fixes only the "NOT" clause.

2. **Founder file, R-ADDRESS-TABLE.** The ruling drops his "only … as an artifact". Use his words: "space only arises as an artifact of timing and address relationship; mass and energy arise only as an artifact of CP displacement and the relationship between CPs and their rule-of-relationship properties." Also add his sentence "the universe is only a collection of individual consciousnesses coordinated … by the timing pulse of the Nexus." It is the sentence that ties the ontology to job (1).

3. **Draft §2.3, Planck-scale remark.** This is a D-7/D-10 failure. The corpus does not put the GP spacing at Planck scale:
   - `founders_vision.md:984` (Opus correction, Patch 0733) says reading l_P as the lattice spacing was a mis-read, and l_P is the baseline PSR.
   - c01 has "~10³⁰ GPs per Planck length".
   - todolist 4357 has "grid spacing ~ l_P/10³⁰".
   - 4310 lists "two GP spacings" (N = 9×10²⁸ or 9×10³⁰).

   Replace with: "One GP step is far below the Planck length on the corpus's working values (c01: ~10³⁰ GPs per Planck length; Patch 0733 correction; 4310's two candidate spacings), so the threshold sits even further below anything an experiment touches." Drop "which CPP places at Planck scale (about 1.6 × 10⁻³⁵ m)" and "the lattice-spacing identification is the corpus's". The conclusion is unchanged, and stronger.

4. **Draft §2.2(3), Hornberger et al. 2003, wrong as an example of weak ties compounding.** In the C70 gas-collision experiment a single collision essentially decoheres: the gas atom's momentum kick is large next to the grating period. Visibility falls with pressure as the chance of no collision falls. Each collision is a strong record, not "a small record". Two fixes:
   - Keep Hornberger only as "collisions decohere".
   - For compounding of individually weak records, cite Kokorowski, Cronin, Roberts and Pritchard, "From Single- to Multiple-Photon Decoherence in an Atom Interferometer," PRL 86, 2191 (2001). There, photons with wavelength longer than the path separation each remove a little coherence, and many of them compound. Joos–Zeh long-wavelength scattering is the general theory.

   Hornberger 2003 is already in the corpus (4479 §3, line 52; 4480 line 35). Say so in §3.

5. **Draft §4, the founder question.** It has a false premise ("ten million gas atoms … each brush so faint") and a leading cue ("as experiments show"). Rewrite as a physical picture with no cue:

   "An atom flies through two slits while a dim glow of very long-wavelength light shines across it. Each photon that bounces off it has a wavelength far longer than the gap between the slits, so by itself it would tell almost nothing about which slit. Ten million such photons bounce off it. Does each faint bounce stay in the Nexus's ledger, so that together they add up, or does each one, being individually irrelevant, simply not count?"

   Update the §6 reply's "gas molecules brush past" to match.

6. **Draft §2.2(1) and the §6 reply, Walborn attribution.** In Walborn et al. 2002 the path is marked in the photon's own polarization (quarter-wave plates), which is entangled with the partner. That is how 4445 (line 85) and 4481 §2 file it. It is not a "path fully recorded in its partner".
   - Keep Englert's general which-way detector for D1.
   - Cite Walborn as: "marked in its own polarization, entangled with the partner; the fringes appear only when its hits are sorted by the partner's polarizer result in coincidence; the unsorted pattern is smooth (4481 §2)."
   - If you want a case where the partner holds the which-slit record, use Kim, Yu, Kulik, Shih and Scully, PRL 84, 1 (2000).
   - Fix §6's bullet the same way.

7. **Draft §2.1 / §2.2, D-15 most favourable reading missing.** His "cannot affect its entangled photon … when measured light-years away" is also, and most favourably, the no-signalling statement. Measuring the far partner never changes the near photon's own statistics, for any tie strength and any distance (THEO-QM-5, already in Reads-against). Add this reading. On it he is right without conditions (2) or (1): what removes the photon's own fringes is the existence of a strong tie, not the measurement of the partner. This also softens (2). Distance needs no reinterpretation on this reading, so present the dilution reading as the second reading, not the only one.

8. **Draft §2.1, (T-a) mislabelled.** 4489's (T-a) is "drop only what can no longer change any outcome", which is decoherence pruning (4489 §5, §6: "Under (T-a), memory rests on the records within the realized branch"). "Nothing is deleted, nothing is erased" is stricter than that: pure global unitarity, QM-4's "Apparent collapse is an artifact of tracing over the bath". Say: "kept and inert: (T-a) without even its pruning". Also mark the tension honestly in §2.1 and §7: his 4489 message proposed to "truncate the accounting of entanglement beyond a certain magnitude", so reading 4490 as "nothing dropped" goes beyond his 4489 words. That makes it more plainly the convenient branch, and the reason §4 asks.

9. **Draft §1, "The GP talks to the Nexus," a change not flagged.** In 4489 he wrote "Each CP connects to the nexus". Now he writes "Each GP … communicating with the Nexus". State the shift and read it, marked as Claude's reading, as the CP reporting through its GP (`founders_voice/4166_ruling_cp_reports_to_gp.md`; A1′: GPs compute).

10. **Draft §3, D-10 list incomplete or wrong.**
    - "Distance alone does not end the tie: 4481 §2": 4481 §2 is about absorption ("Absorption as such does not end the tie"), not distance. Cite 4484 (tranche 2, line 28) and 4488 §2 (line 38) only, or say "absorption alone: 4481 §2".
    - Add QM-4 thm:lindblad: a Lindblad rate γ = π Σ_j g_j² δ(ω_j) from many weak couplings to the DP Sea bath. That is the corpus's own form of "weak ties add up".
    - Add 4479/4480 for Hornberger.
    - Add 4074 ("the 4th dimension is simply an address") as the nearest prior address ontology, next to "no prior 'table of addresses'".

11. **§5 and D-9.** `todolist.md` has no 4490 entry, so the deferral gate will fail. File every new item (a)–(e) in todolist in the same patch. Also file these, which are owed but not listed anywhere:
    - (i) A forward pointer (anti-erasure annotation, text unchanged) on `founder_ruling_nexus_role_and_zbw_rebound_de_2026-08-10.md`'s R-A4-ROLE, pointing to the 4490 scope note.
    - (ii) `master_glossary.md` line 90 (PCD row, which cites "nexus ruling R-A4-ROLE") and line 131 (the Nexus entry) to carry R-A4-JOBS.
    - (iii) The registry decision in change 12.

    Add "(f) two ledgers" (claimed in the header's "Joins 4489 §8 (a), (d), (f), (h)") explicitly to §5: say whether "nothing deleted" makes it moot. Fix "(still his ruling at 4478 §6)" to "(awaiting his ruling, 4478 §6)": 4478 §6 is a question, not a ruling.

12. **Registry convention.** The repo does register founder rulings that bear on an axiom's statement in `axiom-registry.md`, as sections under the axiom:
    - "Registered ruling under A1′ — R-CP-NO-REST-MASS (Patch 4350 … under PD-006)", line 358.
    - The A3′/AP-4 DI-bit rulings, line 389.

    R-A4-ROLE (3059) was never registered, so leaving these in founders_voice alone has precedent. But R-A4-JOBS restates A4's role. Either register it under A4 on the 4350 precedent, as a clarifying clause with the axiom count unchanged and the reading marked, or say in the draft and the founder file why not, and file the decision in todolist. "By that file's convention" is not enough as written.

**OPTIONAL NOTES**

1. The script's seven PASS checks are identities: V² + D² = 1 holds because D is defined from g, and (1−δ)^N ≈ e^(−Nδ) is arithmetic. Call it an illustration script, not a verification of physics.
2. The independence assumption (product environment states, so overlaps multiply) is stated in the draft. Add to the script docstring that correlated environments can do better or worse than g^N.
3. A per-tie D = 1.4×10⁻³ against a per-tie V-shift of 10⁻⁶: say which one the "threshold" is measured in. His criterion is CP displacement under one GP step, and the draft never maps that to g.
4. §1 quotes "Synchronizing" with a capital; he typed "synchronizing". §2.2(1) quotes "it still does everything a photon does, on its own" without the ellipsis for the words cut.
5. R-NO-SEPARATION only reaffirms R-DISCONNECT. Consider recording it as a reaffirmation note on R-DISCONNECT rather than minting a new ID.
6. Micius: correct (Yin et al., Science 356, 1140, 2017; 1,203 km; 2.37 ± 0.09; strict Einstein locality). It does not close the detection loophole, which doesn't matter here.
7. §6 states the R-A4-ROLE rescoping to him as settled. One clause ("tell me if that's not what you mean") would match the 4351 confirm-the-marked-reading precedent.
8. D-15: the final chat message must say what this critic changed.

**PLAIN LANGUAGE**

Thomas's answers were copied into the record exactly. Two of the three rulings drawn from them need tightening. One sentence that reinterprets his August ruling is presented as his, but it is Claude's inference, and he said he doesn't remember what he meant then. The ontology ruling also drops his "only … as an artifact". The physics in the draft is mostly sound: a faint tie leaves a photon's interference intact, a strong tie removes it, and distance alone doesn't weaken entanglement. Three things need fixing:
- The draft says the grid is Planck-sized, but the repo's own notes put it far finer.
- The gas-collision experiment it cites shows strong single bumps, not many faint ones adding up; a different experiment, with long-wavelength light, shows the faint-ones-add-up effect.
- The question to Thomas hints at the answer and rests on that same mistaken picture of the experiment.

The draft also misses the simplest favourable reading of his answer: measuring a far-away partner never changes anything you can see here, for any tie strength and any distance. Finally, several things the draft defers need entries in the to-do list. Among them are pointers from the August ruling file and the glossary to the new ruling, and a decision on whether the ruling goes in the axiom registry.

---

## Claude's response to the 4490 return (not part of the verbatim report)

All twelve required changes taken in, after spot-checking founders_vision.md l.984 (Patch 0733 correction), the c01 "~10³⁰ GPs per Planck length" quote, 4310's two GP spacings, 4166, 4074, QM-4's thm:lindblad and "Apparent collapse is an artifact of tracing", and the registry's R-CP-NO-REST-MASS precedent: (1) the scope note marked as Claude's extraction, both R-A4-ROLE clauses scoped, job (2) marked as Claude's reading; (2) R-ADDRESS-TABLE in his words with "only ... as an artifact" and the "collection of individual consciousnesses" sentence; (3) the Planck remark replaced by the corpus's sub-Planck working values; (4) Hornberger kept only as "collisions decohere," compounding cited to Kokorowski et al. 2001; (5) §4 rewritten as the long-wavelength-light picture, no cue, and §6 matched; (6) Walborn re-described as own-polarization marking, Kim et al. 2000 added for partner-held records; (7) R1, the no-signalling reading, added first; (8) R2 labelled "(T-a) without even its pruning," its tension with his 4489 truncation words marked; (9) the CP→GP shift stated and read through 4166; (10) the D-10 list corrected (4484/4488 for distance; 4481 §2 for absorption; thm:lindblad; 4479/4480; 4074); (11) a 4490 todolist entry, the forward pointer on the 3059 file, the glossary PCD row and Nexus entry, (f) two ledgers dispositioned, "awaiting his ruling, 4478 §6"; (12) R-A4-JOBS registered under A4 in his words on the 4350 precedent, axiom count unchanged at 9, the reading marked. QM-4's Lindblad rate is quoted in the paper's boxed form, γ = (sea_strength)² E_P/ħ, not the critic's Σ form. Optional notes 1–8 taken (5: R-NO-SEPARATION recorded as a reaffirmation, no new ID; 7: "tell me if that's not what you mean" added to the reply).


## Patch 4491 — Independent critic of the reading of the founder's collision and faint-bounce answers (4490 §4)

VERDICT: ACCEPT WITH CHANGES

What I checked: the founder file against his message, byte for byte after rejoining lines; the script (ran it and checked it against the closed form); the D-11 table; and the claims against 4464, 4480, 4481, 4485, 4489, 4490, QM-4, the 4490 critic returns, Walborn et al. 2002 (arXiv quant-ph/0106078) and the Chapman et al. 1995 abstract.

REQUIRED CHANGES

1. **The kick is not the general cause (D-15, D-10).** Draft §3.2, §7, §8 "Agreed: … the kick as the cause", and the title.
   - The corpus already settled this at 4480, lines 44–55: the kick and the which-way record are two descriptions of one effect. What tells them apart is marking with no kick. In the Walborn eraser the path is marked in polarization, with no momentum given. Dürr, Nonn and Rempe (Nature 395, 33, 1998; verified at the Session 242 critic) found the back-action "too small to explain the disappearance."
   - 4491 never cites 4480, although 4480 already carries Pfau 1994 and Chapman 1995 in this same recoil role.
   - Fix:
     - Add 4480 to "Reads against".
     - In §3.2 add: "In this experiment the kick and the photon's record of the path are one effect described two ways (4480). Where the path is marked with no kick (Walborn 2002; Dürr, Nonn and Rempe 1998), the fringes still go. So the kick account covers scattering, but the general cause is the record."
     - In §8, move "the kick as the cause" from Agreed to Marked, worded as "for scattering, where kick and record coincide."
     - Add this as a new open item.
   - It also ties into §4, which explains Walborn without saying that this is exactly the case the kick picture does not cover.

2. **"(T-b) is not his picture" overreaches.** §3.1, and §6 "4489 (d)".
   - (T-b) is the object-size cut (GRW/CSL). His answer is about faint bounces on one atom and says nothing about object size.
   - Fix: "(T-c) is excluded by his answer. (T-b) is not addressed by it." Then either carry 4489 (d) for (T-b) or close it explicitly as Claude's reading. That reading: his 4489 criterion was the size of the effect, not the size of the object, so (T-b) was only ever a secondary reading.
   - Mark 4489 (d) as "closed on Claude's reading" either way.

3. **"Confirms the Nexus was never used to keep regions apart" overstates him.** He said: "I think that is what happened. I don't remember the Nexus being used to keep regions apart."
   - Locations: the title ("He Confirms the Nexus Was Never Used to Keep Regions Apart"), §8 ("the Nexus never kept regions apart"), and the theory-overview header ("the founder's confirmation that the Nexus was never used to keep regions apart").
   - Fix: "He agrees the scope note matches what happened ('I think…'); he does not remember the Nexus being used to keep regions apart." The physics claim that there is no separation job is already his, at 4490.

4. **Energy sign.** §3.2 "Energy" paragraph.
   - In resonant scattering the atom's kinetic energy changes by recoil in either direction. On average it gains (recoil heating); it does not lose.
   - Fix: "The atom's energy changes by a tiny recoil amount, up or down (on average slightly up). So 'a little' is right in size; what matters is the momentum."

5. **Walborn facts.** §4 and §7.
   - The quarter-wave plates are placed "in front of each slit" (Walborn et al. 2002), not behind. Fix "Behind each slit sits a plate" and "behind each slit a plate" to "Just before each slit sits a plate."
   - "sorted by whether B passed or not" is not how the experiment ran. Walborn's polarizer was set at the angle of one plate's fast axis for fringes, then of the other plate's for antifringes, in separate coincidence runs.
   - Fix: "…sort A's hits by B's result at a polarizer, set first at one angle, then at the perpendicular angle."
   - Optionally, "turns A's polarization one way / the opposite way" could become "gives it a left- or right-handed twist."

6. **4464 attribution.** §3.1.
   - 4464 §2 lists three differences from the pilot wave, not two. The third is "for light his photon has no part that takes one slit". 4464 also adds that his picture must give h/p.
   - Fix: "noted the resemblance and its differences, among them: …" or add the third.
   - The quote "DP-arc-separation volume extends out…" starts in the middle of the subject. His sentence is "That energetic driver of the DP-arc-separation volume extends out from the particle and can go through both slits…" Quote it from "That energetic driver".

7. **Script checks.** Script lines for K2 n = 1 and n = 10, and the title "Script 8/8".
   - Two K2 rows hard-code `True`, so they are reported values, not checks.
   - Fix one of two ways:
     - make them real checks, e.g. compare with the closed form j0 − j2/2 at kd = 0.2π, which gives C1 = 0.92270, C1^10 = 0.4473, C1^100 = 3.2e-4; or
     - relabel those rows as "value" and say "6 checks, 2 reported values" in the header and the title.
   - If either changes the output, re-paste the table under D-11.

8. **Consistency.** §1 says R-COLLISION-DISPERSES "joins 4489 (e) and 4490 (d)", but §6 closes 4490 (d). Fix to: "closes 4490 (d); joins 4489 (e)."

9. **§5 question is leading.** It is a physical picture, but §7 tells him the data require "both" before asking "both or one side?". He himself said the photons hit "one or the other side."
   - Fix — reword as an open "how": "A long-wave photon bounces off the atom's core as it passes through one slit, while its KE/DP-arcs pass through both. How does that bounce reach the arcs passing through the other slit?"
   - Keep the §8 marking: the condition is Claude's statement, drawn from the data.

10. **Bundled files (D-9).** `todolist.md` and `research_frontier.md` are not in the diff; 4488–4490 each updated both. Also add this critic return to `series_standard_model/reviews/2026-11-18_session_244_critic_returns_verbatim.md` or a 11-19 file. The todolist 4491 entry must contain:
    - the files;
    - Done: the R-A4-JOBS confirmation line, the overview header, R-COLLISION-DISPERSES filed in founders_voice only;
    - Closed: 4489 (d) for (T-c) (and (T-b) per change 2), 4489 (f) moot, 4490 (a), 4490 (b) summing part, 4490 (d), 4490 (f);
    - Owed, word for word: 4491 (a)–(e), plus the kick-versus-record item from change 1;
    - Carried unchanged: 4490 (c), (e); 4489 §8 (b), (c), (e), (g); 4488 §7 as carried at 4489 §8; 4481 (a), (c), (e); 4478 (a) and the 4478 §6 placement ruling; 4464 (d); 4477 (g); the 4478 §4 citation correction; and, if carried, (T-b).
    - The chat reply must say what this critic changed (D-15).

OPTIONAL NOTES

1. The founder file's text matches his message exactly: every double space ("happened.  I", "lines.  That", "slit.  The", "the  DP-arcs") and every blank line, including the two before "Question for you". The only difference is that trailing spaces at line ends were dropped. You could add "trailing spaces not kept" to the disclosure. I could not check the "01:23 local" time.
2. In the draft, §2 quotes "happened. I don't" and §3.1 quotes "changes the DP-arcs" with single spaces. The registry and the founder file keep his double spaces; match them.
3. The no-cut reading can be made stronger rather than only marked. Any real photon kick moves the atom by vastly more than one GP step during its flight (4490 §2.3: a GP step is far below the Planck length). So even his own 4489 "one GP displacement" criterion keeps every bounce. Saying so answers the obvious objection that his threshold was framed in exactly the displacement a kick produces. Keep the convenience marking in §8; it is honest.
4. §3.2's "multiplies … in both arms by the same factor" is loose. Better: "by the same factor exp(i q·x), which takes a different phase at each arm."
5. On the model's numbers: the closed form for dipole emission with its axis perpendicular to d is C = j0(kd) − j2(kd)/2. Its first zero is at 0.4367 λ and its revival is 0.3355 at 0.6737 λ. The script's 0.435 λ, 0.675 λ and 0.3353 are right to the grid step of 0.005 and the Monte-Carlo noise; the 0.0042 at the minimum is noise, the true value is 0. The incident direction only adds a constant phase, so |C| does not depend on it. The K3 cone sits in the strong-emission plane, so 0.9999 is right. The K2 rule C^N, with photons independent, is right.
6. Chapman et al. used a three-grating Mach–Zehnder interferometer, and the path separation was set by where along it the laser struck. "Two slits" is 4490's idealisation; a parenthesis would say so. The author list, PRL 75, 3783 (1995), the observed loss and revivals with separation, and the recovery by keeping only atoms correlated with photons in a limited range of directions all match the abstract.
7. The title's "Matches the Standard Account Under One Condition" goes further than 4464's critic allowed ("overclaimed the pilot-wave match"). K3 also needs the kick written in the photon. Consider "Is Consistent With … Under Conditions."
8. Registry: his confirmation sits inside the paragraph headed "Reading (Claude's, PD-008, not his words)". A separate "His confirmation (4491)" line would keep the attribution clean. Otherwise the edit is faithful. The overview refresh is adequate as a header line once change 3 is made.
9. 4485's exceptions (one possible outcome; alternatives acting alike; a swap passing a tie on) are reproduced faithfully. Note that 4485 is Copilot's text summarized, and that he called these "an exception that really is not an exception."
10. On reading his answers generously (D-15): "add up" is a fair reading of "See above comment" together with "the only thing that diminishes the entanglement is collision", and §8 marks it as convenient. The QM-4 quotes and labels (thm:unitary, thm:lindblad, "artifact of tracing") and the THEO-QM-5 reference check out.

PLAIN LANGUAGE: The draft is mostly right, and his message is filed word for word. His idea is that when light bounces off an atom it gives the atom a small push, the push disturbs the invisible waves that steer the atom, and many small pushes add up to blur the stripes on the screen. A real 1995 experiment fits that, provided the push acts on the steering waves in both slits at once. The draft needs fixes in a few places:
- Other experiments wipe out the stripes with almost no push at all, just by tagging which slit the particle used. So the push can't be the whole story, and the draft should say so; an earlier patch (4480) already did.
- It claims more from his answers than he said: on heavy-object cutoffs, and on his memory ("I think… I don't remember").
- It gets the sign of the energy change wrong (on average the atom gains a little, it doesn't lose).
- It puts the plates in the Walborn experiment behind the slits, when they sit in front of them.
- It counts two script rows as checks when they are only reported numbers.
- It asks him a question after already telling him the answer it wants.
- It still needs the to-do list and research-frontier entries bundled into the same patch.

---

## Claude's response to the 4491 return (not part of the verbatim report)

All ten required changes taken in, after spot-checking 4480 l.44–55 (kick and record as one effect; marking without a kick) and 4445/4481's description of Walborn: (1) 4480 added to Reads-against, a "Kick and record" paragraph in §3.2, "the kick as the cause" moved to Marked, new open item (f), and the §4 Walborn account tied to it; (2) (T-c) excluded by his answer, (T-b) closed as secondary on Claude's reading, 4489 (d) marked "closed on Claude's reading"; (3) "confirms" replaced by his agreement and his "I don't remember" in the title, §2, §8, the founder file, the registry and the overview header; (4) energy recoil up or down, on average slightly up; (5) plates "just before each slit", a left/right-handed twist, the polarizer set at one angle then the perpendicular angle in separate runs; (6) 4464's differences listed with the third and h/p, the quote begun at "That energetic driver"; (7) K1 and K2 now checked against the closed form j0 − j2/2 (the table re-pasted; values unchanged in K1/K3, K2 rows now show the exact value); (8) R-COLLISION-DISPERSES closes 4490 (d) and joins 4489 (e); (9) §5 reworded as an open "how"; (10) todolist and research_frontier entries in this patch, this return filed. Optional notes 1–10 taken (3: his own one-GP-step criterion keeps every bounce; 4: exp(i q·x) wording; 6: Chapman's three-grating interferometer noted; 7: "consistent with … under conditions"; 8: his words on a separate registry line).
