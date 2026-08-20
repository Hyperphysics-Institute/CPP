# CONV-028 ADJUDICATION

**Patch 3266 (20 Aug 2026, Session 150). All five seats returned
same-session; verbatim in `reviews-CONV-028.md`. All named conditions
discharged at this patch; verify 3263 extended and re-run (10/10).**

## §1 — Seat ledger

Both CONV-027 protocol defects are CURED this round: the Gemini seat
self-identifies "Gemini"; the Copilot seat uses the full §8 skeleton.
One reporting anomaly recorded: the Grok seat pasted five check lines
and wrote "6/6 checks pass" against a 9-check script — the digits it
pasted match the script's outputs; recorded, votes counted. Script
executions this round: ChatGPT seat (full 9/9 with digits); Gemini
seat (full 9/9 PASS lines pasted). Copilot's requested independent
SCRIPT-EXECUTED artifact is therefore supplied by the panel itself,
and the worker re-ran the EXTENDED script post-revision (10/10).

## §2 — Tally (majority binding)

| Q | Verdicts | Outcome |
|---|---|---|
| Q1 (T-2 chain) | SOUND ×4; DEFECT-NAMED ×1 (Copilot: regularity class; explicitly NOT verdict-flipping) | **SOUND** |
| Q2 (T-2 framing) | CORRECT-AND-HONEST ×5 | **CORRECT-AND-HONEST (unanimous)** |
| Q3 (T-3 chain) | SOUND ×5 | **SOUND (unanimous)** |
| Q4 (GR-1j discipline) | DISCIPLINED ×5 | **DISCIPLINED (unanimous)** — the Q6c gate is satisfied |
| Q5 (completeness) | READY ×4; REVISE-NAMED ×1 (Copilot: three named revisions) | **READY**, with the minority's revisions ADOPTED anyway (§3) |
| Q6a (T-2) | RATIFY ×3; RATIFY-CONDITIONAL ×2 (GPT: hypotheses + regularity in the theorem statement; Copilot: Q5 revisions + re-run) | **RATIFIED — conditions discharged (§3)** |
| Q6b (T-3) | RATIFY ×5 | **RATIFIED (unanimous)** |
| Q6c (GR-1j) | SHIP-PATH-CLEAR ×4; RESTATE-REQUIRED ×1 (Copilot) | **SHIP-PATH-CLEAR** (Q4 gate met 5–0) — and the restate's content is ADOPTED regardless (§3) |

## §3 — Conditions and minority items: all discharged/adopted at this patch

1. **The regularity defect (Copilot Q1/Q5a; GPT Q6a).** Discharged by
   ADOPTING THE GPT SEAT'S STRONGER PROOF, not merely a hypothesis
   clause: the two-radius subtraction argument — at fixed s = t−R/c,
   f(s) + (R/c)f′(s) = K at two radii forces (R₁−R₂)f′(s)/c = 0, so
   f′ = 0 with only C¹ regularity, no second derivative, no growth
   condition. Machine-checked as the new 3263 check T2-3b (script
   extended, re-run, 10/10). Theorem statements in the T2_T3 document
   AND GR-1j now carry hypotheses (i)–(iii) explicitly, with the
   regularity note crediting both seats.
2. **Decay-class / cosmological exclusion (Copilot Q5b; Gemini
   objection).** Both theorem statements now say it outright: the
   uniqueness claim lives in the asymptotically-flat LOCAL class;
   C₁ ≠ 0 is a cosmological embedding, outside scope; "this is not a
   universal vacuum statement."
3. **Units mapping (Copilot Q5c).** A units note added to GR-1j:
   census excess → mass density through the k + G chain via the Gauss
   anchor; no new constant; the exact-integer conservation checks hold
   identically in both unit systems.
4. **The sharper comparative-cost statement (Grok; DeepSeek).** A new
   remark in GR-1j ("What this theorem does NOT give"): GR's Birkhoff
   is unconditional; the CPP theorem does not apply under residual
   incoming radiation; staticity is not guaranteed for a radiating
   exterior even with conserved census; readers must not over-read
   full Birkhoff equivalence.
5. **Gemini's trace mapping.** Adopted as a remark: for dust the CPP
   scalar source matches the GR stress-energy trace exactly; CPP has
   the trace-sector current derived, not the full T_μν.
6. **DeepSeek's GW note.** Registered as an extension of
   NOTE-GR-CSTAR-STRONGFIELD (frequency-dependent dispersion and
   birefringence of gravitational waves in strong fields — dynamic-
   sector, unminted).
7. **Copilot's numeric vignette suggestion** (a slow-decay f violating
   the old coefficient separation): SUPERSEDED by the two-radius proof
   — the C² step it would have illustrated no longer exists; recorded
   here, not implemented.

GR-1j: V0 → **V0.1** (all adoptions in; compile gate clean).

## §4 — Outcomes

- **T-2: RATIFIED** (panel 5–0 in the RATIFY family; both named
  conditions discharged with a stronger proof than requested).
- **T-3: RATIFIED (unanimous).**
- **GR-1j: SHIP-PATH-CLEAR at V0.1** — V1.0 preparation may begin.
  Deposit remains governed by the Patch-3231 gate + the founder's
  queue approvals (the round granted no deposit authority).
- **OPEN-GR-FE-1: ALL THREE THEOREM TARGETS RATIFIED.** The charter is
  COMPLETE pending one founder confirmation, upon which the Patch-3231
  big-wave deposit gate formally MOVES.

## §5 — What the founder decides next

One word — **"Confirm FE-1 complete"** — closes OPEN-GR-FE-1 and
formally moves the big-wave gate. Then the mechanical sequence for
opening the wave: (i) the founder's APPROVED column on the queue rows
(fail-closed by design); (ii) Isak's DOI reservations (spin trio
first, per the test-run ruling); (iii) GR-1j V1.0 prep in the normal
paper-production cycle.
