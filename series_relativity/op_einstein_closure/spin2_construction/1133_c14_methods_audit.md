# Patch 1133 — C14 methods audit (SR-2 pre-draft): classification record + citation map

**Register:** Phase 7A gate work for the SR-2 flagship (per `flagship_assembly_scope.md` §6:
catalog-first-then-cite, paper_completion_checklist C14 workflow steps 1–3 executed pre-draft so
step 4's inline citations are available *during* drafting rather than retrofitted at SHIP).
**Source corpus read in full:** all 20 Tier-4 reasoning fragments (`op_einstein_closure/reasoning/
1107–1110` + `spin2_construction/reasoning/1112–1130`, ~1,086 lines) — the canonical record per
C14 step 1, not the polished step docs.
**Scope rule honored:** physics derivation methods only. Protocol/workflow patterns surfaced by
the corpus (verdict-honesty integration over vote-counting at 1127; contested-registry
touch-once discipline at 1123; CONV-002 re-sync practice) are noted in §3 as OUT OF SCOPE and
left to their proper homes.
**NO VERDICT MOVED.** Registry files other than `methods_catalogue/methods_catalogue.md`
untouched.

---

## 1. Catalogue additions made at this patch (NEW + ADAPTED)

| ID | Layer | Class | Method | Arc source |
|---|---|---|---|---|
| METH-L1-008 | L1 | NEW | Little-group helicity classification of lattice mode content | 1109, 1116 |
| METH-L1-009 | L1 | NEW | Spherical-design moment annihilation in shell-sums | 1108; deployed 1112, 1113, 1119 |
| METH-L1-010 | L1 | NEW | Discrete per-edge connection formalization (antipodal-consistent transport) | 1119 |
| METH-L1-011 | L1 | ADAPTED (standard GR radiation theory → CPP conservation anchors) | Conservation-identity far-field reduction | 1124, 1125 |
| METH-L1-012 | L1 | ADAPTED (from METH-L1-003 branching) | Protected-content enumeration via irrep dimension bound | 1123, 1120 |
| METH-L2-010 | L2 | NEW | Falsification-first attack ordering (cheapest kill before the summit) | 1107, 1109 |
| METH-L2-011 | L2 | NEW | Counterfactual-armed verification | 1125, 1127; sister: chirality 0828 |
| METH-L3-006 | L3 | NEW (fills reserved physics-scoped slot) | Axiom-necessity by exhaustive route closure (multi-assault standard) | 1115 + 1116 + 1119 → 1129 |

Plus example-application updates: **METH-L3-004** (the spin-2 arc as the first exercise of its
*terminal* branch — the primitives-only attempt genuinely failed — AND a same-arc deployment of
its *refusal* branch at the τ-redundancy resolution, 1125). Footer totals corrected (pre-existing
stale count 20 → actual 21 → new 29; symmetric-honesty note in the footer).

## 2. STRAIGHT REUSE classifications (no new entries; cite these inline in the SR-2 draft)

| Existing entry | Where the SR-2 draft invokes it |
|---|---|
| METH-L1-003 (Branching rule analysis) | §4/§8: $l=2 \downarrow I = H$ intact vs $l=2 \downarrow O = E \oplus T_2$ (1120 P3); feeds METH-L1-012 and PRED-O-37 |
| METH-L1-007 (Numerical verification at machine precision) | throughout: 5-design moments (3.9e-16), m=±2 weights (≤9e-16), conservation identity (6e-7), τ-completion (4e-19), flux ratios (1.000246 / 1.000640), character arithmetic (1e-12, φ cross-check) |
| METH-L2-004 (Symmetric-honesty discipline) | §10: the C4 v0.1 origin-dependence defect flagged not silently patched (1124); the τ=0 counterfactual documented (1125); the OB-2 kill switch named before DG-3 dispatch (1123) |
| METH-L3-003 (Suspicious foundational input → numerical verification) | §3: the Step-0 audit of 1116's coverage before the third assault ran (1119) — re-read the code, confirmed no per-edge rotation operator existed, established the run was well-posed |
| METH-L3-004 (Would-be-axiom → constraint first) | §3 + §7: the arc IS the canonical terminal-branch instance; the τ-redundancy is the refusal-branch instance (examples now recorded in the entry itself) |

## 3. Surfaced but OUT OF SCOPE for the methods catalogue (homes noted, not actioned here)

- Verdict-honesty integration rule (upholding a lone RESTATE against a 2–1 CONFIRM count; 1127)
  — review-protocol pattern; home: `templates/operating_system.md` / `relationship_protocol.md`.
- Contested-registry touch-once discipline (registries touched once with reviewed final text,
  post-sign-off; crystallized at 1123) — workflow; home: operating_system.md (already consonant
  with STOP-and-warn).
- The Step-0 "was this actually untested?" audit as a *review* practice (1119) — captured at the
  physics level under METH-L3-003's example; the protocol-level generalization belongs to OS.

## 4. Inline-citation plan for the draft (C14 step 4, to execute during 7B drafting)

Convention per `methods_catalogue/README-methods_catalogue.md`: `[METH-Lx-NNN method-name]` at
the point of invocation. Anticipated densest sections: §3 (L3-006, L1-008, L1-010, L3-004),
§4 (L1-009, L1-003, L1-012), §6 (L1-011), §7 (L1-011, L2-011, L1-007), §9 (L1-012 → PRED-O-37).
Step 5's audit-trail sweep (uncited substantive invocations) runs at draft completion, before
the 7C review dispatch.
