# Reasoning capture — Patch 1121 (Task 1, the flow choice: B)

**Protocol:** `templates/reasoning_capture_protocol.md`. Verbatim reasoning from the Opus
session, Session 156 lane (band 11xx), 11 June 2026. Companion to
`1121_task1_flow_choice_B.md` + `code/1121_task1_source_configurational.py`.

---

## How the decision was reached (the session's actual path)

The kickoff handover posed Task 1 as a three-way choice (A: CP State Register; B: LSP
broadcast; C: GP→CP instruction) to be argued from the PCD cycle and economy, with the hint
that B is the natural home if `Q_ij` is a field. The session's path to the decision ran
through the diagnostic steps rather than from first principles in isolation:

1. **Step 7 (1120) did the heavy lifting against A.** Once it was established that matter-side
   l=2 is configurational (the relative-coordinate function space carries every l; single
   constituents carry none), the CP register became the wrong home twice over: a per-CP rank-2
   attribute has nothing physical to report (a point has no quadrupole about itself — verify
   D1 makes this exact), and it would sit dangerously beside the emergent structures (ZBW
   spin-½, configurational hadron l=2) that need no bit.
2. **The architect's own formulation sealed it.** In the post-1120 exchange, Thomas framed the
   result as: "the spin does not originate with the CPs as a rule... it is an axiom of the
   field, not of the CPs... In some way, it arises from the conformation of the mass." The
   session's refinement — *sourced by conformation, carried by axiom* — is the flow-B
   architecture in one sentence: the conformation of the mass sets the broadcast's amplitude
   and pattern (the source, assembled from existing reports); the capacity to carry it is
   granted to the field (the packet).
3. **The corpus delivered the precedent.** Reading the c07 glossary for the canonical LSP
   definition before drafting (grounding discipline), the decisive find: the LSP "supersedes
   the SR-era DI-bit broadcast by adding the vector component needed for general relativity."
   The packet has been extended once before, under exactly this logic — a sector of gravity
   exceeding the packet's representational capacity. The DI-bit → LSP → extended-LSP ladder
   converts option B from "a reasonable design choice" into "the established pattern of the
   programme, applied a third time." This is the argument most likely to carry DG-3.
4. **C fell to the readout observation.** In the PCD cycle, GP→CP displacement is the Compute
   step's *output* — how the field acts on matter (what stretches a LIGO arm). Once the
   broadcast carries `Q_ij`, the TT extension of the displacement map is Task-4 derivation
   work, not a primitive. And the induction asymmetry: A or C as home would each still need a
   GP→GP channel to propagate (inducing B); B induces neither. B is the irreducible core.

## The two design constraints and where they came from

- **No-ZBW-double-counting** is inherited from the kickoff handover, now sharpened by 1120:
  the boundary is not just "don't disturb fermion spin" but "don't re-derive anything
  configurational" — `Q_ij` is the radiative field, full stop.
- **No-static-double-counting** emerged in the post-1120 exchange with the architect, from his
  mono-motivation challenge. Working through why CPP cannot borrow GR's "every apple is spin-2
  evidence" framing exposed the labor division: CPP's scalar already does statics *exactly*
  (Schwarzschild, c07/c08). Therefore the standard spin-2 bootstrap (massless tensor coupled
  to full T_μν regenerates all of GR — Deser/Weinberg-style) is a *hazard* here, not a
  convenience: it would double-count the recovered Newtonian sector. The constraint: source
  `Q_ij` from the time-varying (TT-projected) quadrupole only. Verify D3 demonstrates the
  physics (static pair: d²Q/dt² = 0, radiates nothing; orbiting pair: oscillation at
  2ω_orbit — the GW double-frequency signature — with the ×-channel visible in Q_xy). The
  covariant form of this projection is Task 3's central problem, flagged now so it shapes the
  axiom text rather than patching it later.

## The justification preamble (how the mono-motivation concern resolved)

The architect's challenge across the session: a single-purpose axiom is possible but odd —
"why was the world built this way and no other phenomena that we know of is touched by it?"
The resolution adopted, after tightening the bookkeeping:

- **Mono-sectoral, not mono-observational.** The precision matters because CPP divides
  gravity's labor where GR does not. The honest claim: load-bearing for one sector (radiative
  tensor gravity).
- **Multi-evidential within the sector:** direct detections (~100+), polarization
  discrimination (GW170814+), binary-pulsar decay (Hulse–Taylor five decades ~0.2%; double
  pulsar 10⁻⁴) as an independent back-reaction channel, and the no-dipole constraint
  (scalar–vector gravities radiate dipole; pulsar timing excludes it). One sector, four legs.
- **The architect's access argument, adopted:** gravity couples to everything, so the tensor
  field is universally sourced; its distinguishing signature is empirically reachable only
  through extreme amplification (astronomical masses, 10⁻²¹ strain, decades of timing). The
  evidence concentrates in one channel because that is the only open channel at our
  instrumental reach — "the axiom is not special-purpose; the telescope is."
- **The architect's lattice parallel, adopted:** he initially resisted the 4D/600-cell in
  favor of simple cubic packing; Step 7 showed cubic would split the very multiplet this
  axiom needs (E ⊕ T₂) while the icosahedral geometry protects it (H_g) and pre-slotted the
  seat (1112). The spin bit is the same category of commitment: subtle, initially resisted,
  load-bearing. And the chirality rhyme, stated with its conditionality intact: twice the
  programme asked whether the substrate could borrow a capacity from dynamics, and twice the
  answer was primitive (V3 spatial chirality, conditional on Mechanism A; the spin bit,
  unconditional after three assaults).

## Discipline notes

- Re-synced to origin before building (the architect's `git am` of 1120 created hash f7ff582;
  patch built on the pushed history). The architect's double-run of the 1120 apply block was
  diagnosed from this end by fetching origin (1120 present ⇒ the failure was a re-application;
  `git am --abort` resolved it cleanly — no repo damage).
- One trivial bug in-session: numpy 2.x removed the `.ptp()` array method; replaced with
  `np.ptp()`. No physics content.
- NO VERDICT MOVED: no THEO/PRED/ID registered, no count change; no axiom text written (Task
  2). Private-lane paths only (spin2_construction/ + parent INDEX/README, owned subtree). No
  contested file touched. The axiom-inventory and registry touches begin at Task 2+ under
  STOP-and-warn.
- Queued (architect's call): a founders_vision.md entry capturing the 11 June justification
  reasoning (the mono-sectoral/multi-evidential resolution + the cubic-resistance parallel) —
  root-level shared file, so proposed as its own patch with CONV-002 re-fetch, not bundled
  here.
