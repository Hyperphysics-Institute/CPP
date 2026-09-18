# Session 232 — EW lane: the chirality axiom maturation (Patches 4063–4092, plus 0991–0994)

**BLOCKING — CLONE-FIRST GATE.** Before registering any ID, placing any file, or computing any coefficient:
clone the repo (full history, **no `--depth`**), read `bootup.md`, and grep the registry. Then run
`python code/next_id.py ew` — **and claim the number in the frontier's "Next patch (EW): NNNN" pointer, not
the tool's "NEXT FREE"**, which reads one past it because the pointer is itself a reservation. Taking
"NEXT FREE" literally is what left 4065 and 4067 permanently unused this session.

**Next-session kickoff line:** "Bootup for Conscious Point Physics (CPP) … honor the line-1 CLONE-FIRST GATE …
open `handovers/` (plural), sort by filename, read the newest dated `YYYY-MM-DD_session_NNN_*.md`; there is no
`handover.md`."

---

## 1. What this session was

A single arc: **can CPP derive the parity-odd (P-odd) source that the weak interaction requires — and if not,
what is the minimal axiom, and is it worth adopting?** It began from Session 231's chirality close and ran
thirty patches. The founder's standing instruction, given mid-session and still in force:

> *"I would rather adopt an axiomatic change after we have a clean win. It looks like it's in the right
> direction, but something is missing. Let's keep working on this problem."*

**No verdict moved in this entire session.** Nothing was promoted, no panel was convened, and the axiom was
**not** adopted.

## 2. The result, in one paragraph

**Every route to a *derived* P-odd source is closed.** n̂ alone (4046, regeneralised at 4071), Mechanism A's
δ-tilt (4068 — it breaks **T**, not **P**), electromagnetism (4069/4070 — the right-hand rule is a *convention*;
magnetostatics rebuilt left-handed gives bit-identical forces), internal vector structure (4071), the
tie-break/degeneracy family (4082 — refuted by V−A's maximality across five orders of magnitude in momentum),
and the capture criterion (4086 — the strong sector captures too). What survives is **χ₄**, the founder's spin
bit with a helicity write rule: **a faithful CPP *encoding* of V−A, not a derivation of it** (4083). Four of its
five legs now rest on existing structure — second plane (4091/4092), frequency ratio (4090), fourth-axis motion
(4091), and the variable itself (4092: the geometry selects **helicity**). **The fifth leg, the sign, is
irreducible and undrived.** That is exactly the "something missing" the founder named.

## 3. Patch table

| patch | what landed |
|---|---|
| 0991–0994 | (chir/cross-lane) Θ_OS run-2 adjudication; PD-008 attack on 0985 fails; VW-a-4 refuted on the single-walker measure; founder's −eCP mass ruling filed |
| 4063 | 4054's target MET — a chiral 4D structure with z = 12; Steinberg explains why 4051–4054 could not land |
| 4064 | founder ruling on decoration points; **U stays mathematical**, not a corpus object |
| 4066 | **ERRATUM** — my chat summary had overstated n̂ as a working mechanism; the chirality *mechanism* question is open and is a W⁰ question |
| 4068 | **Mechanism A cannot split the W bracelet** — Θ is an exact improper symmetry of its dynamics at every δ |
| 4069/4070 | **EM is P-even and must be**; the right-hand rule is bookkeeping; both proposed EM↔W⁰ bridges closed |
| 4071 | the P-odd search is **exhausted**; a P-odd axiom is **not single-use** (three disjoint sectors) |
| 4072–4074 | maturation opened; n̂ vs −n̂ is **not** a chirality in ℝ⁴; a **double rotation** carries the pseudoscalar; the founder's fourth axis is the **carrier**, L2 and L3 merge into χ₄ |
| 4075 | χ₄ passes the EM filter **conditionally** — EM must read the 4th axis only through even functions |
| 4076 | the founder's **spin bit**: P-even as defined, **P-odd if written with helicity**; response must be **linear**; two slots per GP revises THEO-QM-10's basis |
| 4077 | **correction to my own counting** — three spatial directions suffice; 3-space *arrangements* can be chiral; four further routes (K2–K5) |
| 4078 | helix is a **lattice** answer, not a chirality answer; **K4 withdrawn as circular** (Sakharov) |
| 4079–4082 | K3 tie-break: maximality delivered, then **refuted** — V−A is maximal across 1 MeV → 40 GeV, so no degeneracy mechanism can produce it |
| 4083 | ω **is** defined; its freedom is necessary; **χ₄ encodes V−A rather than deriving it** |
| 4084 | **F8 passes** — every closed umbrella theorem is a *magnitude*; χ₄ supplies the missing sign for three sectors |
| 4085 | **CPT forces the polarity clause** (the one real derivation of the arc); F5 fails as then posed |
| 4086 | capture criterion fails; F2/F3 are **SM-level stipulations**, F5 a gap by CPP's **own** standard |
| 4087 | **F5 reframed** — my factor-400 verdict withdrawn; J is small because *mixing* is small; maximal phase excluded at 8.5σ |
| 4088 | owed items cleared: SF-6 4th-axis check **clean**; manifestation inventory corrected — **five manifestations are really three** |
| 4089–4092 | the founder's oscillation: driver fails, **oscillation supplies the missing double rotation**; 1:1 resonance kills it; SPIN-1's derived 2√2 ratio satisfies that; the 600-cell supplies orthogonal plane pairs (60 of 66); **the geometry selects helicity** |

## 4. Traps for a fresh worker

1. **Claim the pointer number, not `next_id`'s "NEXT FREE".** Cost this session: 4065 and 4067, unused forever.
2. **Verify the file diff, not the gate output.** Two patches (4086, 4087) had their registry/frontier/todolist
   edits silently fail when a Python block aborted mid-way; the gates passed regardless. `git show --stat`.
3. **`git reset --hard origin/main` destroys unpushed work.** 4086 was lost this way and recovered from reflog
   only because it was noticed. Check `git log origin/main` *before* resetting.
4. **A control that cannot fire is worse than no control.** Ten estimator/model errors were caught this session
   *by controls*, not by inspection — a magnetic field built from the modified field (⊥ by construction), a
   torque compared across conventions (itself axial), a symmetric source that wasn't symmetric, a spin plane
   with a basis-dependent orientation, a 3-dimensional model of a 4-dimensional invariant, a complement tested
   against only 12 of 119 directions (**this one reversed a verdict: 0 of 66 → 60 of 66**).
5. **Magnitude is not sign.** Every geometric route in this arc produced a *carrier* and never a *choice*. If a
   new route seems to give handedness, check whether both hands remain available; they always have so far.

## 5. What the next window should take up — the founder's own question, answered

**(a) A fresh-eyes adversarial audit of this arc — highest value, and it cannot be done in this window.**
Thirty patches of my own reasoning now sit in `series_standard_model/axiom_maturation/chirality_axiom_maturation.md`.
I am the worst possible auditor of it: I chose χ₄, rescued it at 4080, withdrew my own blocking verdict at 4087,
and wrote every "convenient branch" label in it. **A window with no investment in χ₄ should attack the
maturation document under PD-008** — specifically §2q's honest accounting (is it really an encoding?), §2r's
"one sign fixes three sectors" (is the relative sign truly fixed by existing conventions, or is that two
assumptions?), and 4082's refutation of the tie-break family (the one attack left on it is a co-moving SSV
comparison). **This is a review, it is cheap, and it gates everything else.**

**(b) Bounded new physics, independent of the sign: THEO-QM-10.** The spin bit gives **two** slots per 3D GP;
THEO-QM-10 currently derives Pauli exclusion and spin-statistics from **one CP per GP** (via THEO-1). That
derivation needs rewriting over (3D address, spin bit) pairs — registered at 4076 B5, never attempted. It is
real physics, it does not depend on the sign question, and it may be the spin bit's most valuable consequence.
**Lane: QM.**

**(c) A long campaign, and the least-tested foundation in CPP: the lattice.** 4019/4030/4034 leave no flat-ℝ⁴
tiling with z = 12, and 4078 showed Boerdijk–Coxeter helices pack *perfectly regular* tetrahedra at the cost of
periodicity. **Can BC helices be bundled to fill 3-space at z = 12?** If yes, it may dissolve the tiling problem
and retire the founder's 4020 variable-position-GP ruling. This is a genuine multi-session campaign. **Lane: SR.**

**(d) The gate on the axiom, and it is not a chirality problem: F5 → CKM.** χ₄'s CP-violation filter cannot close
inside this arc. It needs an O(1) substrate phase near 68.5° **and** the three CKM mixing angles — SF-2's
generation-transition problem. **Until that lane moves, the axiom cannot be completed, and a panel should not be
convened.** **Lane: SM.**

**(e) NOT recommended: a panel, or adoption.** The founder has held adoption pending a clean win, and F5 is open
by CPP's own zero-parameter standard. Convening now would spend a round on a proposal with a known open problem
and two stipulations.

**Suggested order: (a) → (b) → (c), with (d) whenever the SM lane is live.**

## 6. Step A–H Completion Audit (§15.11)

- **Step A** (Tier 1 session log): N/A — this session's per-patch fragments carry the log; no separate Tier 1 file.
- **Step B** (Tier 2 transcript): N/A — no transcript session.
- **Step C** (Tier 3 vignette): N/A.
- **Step D** (Tier 4 reasoning): ✓ — verbatim fragments at `series_standard_model/reasoning/4063–4092.md` and
  `series_umbrella/.../reasoning/0991–0993.md`, one per patch, none exempt.
- **Step E** (registries, per-registry audit):
  - `research_frontier.md` ✓ — updated every patch.
  - `todolist.md` ✓ — TODO-4063 through TODO-4092 registered; deferral gate PASS on every patch.
  - `id_block_registry.md` ✓ — EW highest-used tracked to 4092; 4065/4067 recorded as unused.
  - `theorem-registry.md` N/A — no theorem registered (no verdict moved).
  - `axiom-registry.md` N/A — **deliberately**: the axiom is not adopted.
  - `manifestation_inventory.md` ✓ — corrected at 4088 (five → three).
  - `frontier_sectors/EW.md` ✓ — notices at 4066, 4068, 4088.
  - `paper_catalog` / `predictions` N/A — no paper shipped, no prediction registered.
  - `master_glossary` N/A. `methods_catalogue` N/A. `organizational_frontier` N/A.
- **Step F** (reviewer artifacts): N/A — no panel convened, by design.
- **Step G** (protocol/OS updates): N/A — no OS change; the numbering trap is recorded here and in the registry.
- **Step H** (this handover document): ✓ — `handovers/2026-09-17_session_232_ew_lane_chirality_axiom_maturation.md`.

## 7. Founder actions outstanding

- **Adoption decision on χ₄** — held at his instruction, pending a clean win.
- **Isak:** VW-1 v1.5 recompile (ledger A11), still owed from 0985.
- Nothing else. All owed items are registered in `todolist.md`.
