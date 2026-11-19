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
