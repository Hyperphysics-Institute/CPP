# Reasoning capture — Patch 1123 (Task 2, the axiom text: A3′ candidate v0.1)

**Protocol:** `templates/reasoning_capture_protocol.md`. Verbatim reasoning from the Opus
session, Session 156 lane (band 11xx), 11 June 2026. Companion to
`1123_task2_axiom_text_A3prime.md` + `code/1123_task2_completion_check.py`.

---

## The decisive registry read (why amendment, not addition)

Before drafting, read `axiom-registry.md` in full (grounding discipline). Two finds shaped the
whole patch:

1. **A3 is already the broadcast axiom** ("DI-bit propagation"), still in its QM-era scalar
   form — while the c07 glossary records that the LSP superseded the DI-bit "by adding the
   vector component needed for general relativity." The registry and the corpus are one rung
   apart *already*. So the tensor extension is not the first amendment of the broadcast
   content; it is the second — and the first was never formally registered. A3′ consolidates
   the whole ladder (DI-bit → LSP → LSP′) into one closed statement, simultaneously fixing
   the registry's lag and adding the tensor rung.
2. **The A6′ precedent** (A6+A7+A8+A9 → one principle) establishes consolidation amendments
   as the registry's accepted mechanism. Under amendment accounting the count stays 9; the
   dual accounting (new axiom → 10) is presented honestly for DG-3 to settle, since the
   tensor clause adds a genuine new d.o.f. unlike a pure consolidation. The substantive,
   non-disputable claim is parameter-free-ness: one d.o.f., zero dials.

## The completion theorem (the session's structural discovery)

While preparing the minimality argument, the 1120 branching table suggested a stronger claim
than "H is protected": that the *protected* l-values might be exactly {0,1,2} — making the
completed packet literally the full protected content of the lattice. Checked computationally
for l = 0–12 and closed analytically by the dimension bound (for l ≥ 3, 2l+1 ≥ 7 > 5 = the
largest icosahedral irrep, so no l ≥ 3 ever descends intact). Both halves verified:

- intact l-values = {0, 1, 2} exactly; first split at l=3 (T₂⊕G);
- LSP′ content {A:1, T₁:1, H:1} = the summed protected content, exactly — and the icosahedral
  irreps absent from the packet (T₂, G) are precisely those that never occur as an intact l.

Consequence adopted into the axiom's name and §3: **the ladder terminates at rank 2; there is
no fourth rung; the axiom is a completion, not an increment.** This is also the structural
answer to the architect's "why was the world built this way" — the broadcast carries exactly
what the lattice protects — and it strengthens his cubic-resistance parallel: on a cubic
lattice not even the l=2 rung would survive intact. Registration of this observation as a
PROP/THEO is deliberately deferred (NO VERDICT MOVED); it rides inside the candidate text for
now and DG-3 will probe it.

## Drafting decisions, clause by clause

- **C1 (algebraic):** symmetric traceless, 5 components — forced by the H slot; also blocks
  surplus components (minimality is enforced, not assumed).
- **C2 (carriage):** absolute-frame, flat per-hop transport — imported directly from 1119's
  dichotomy (anything else Planck-gaps the field). Writing carriage as an explicit clause
  makes the Nexus frame's load-bearing role visible at axiom level.
- **C3 (dynamics):** "identically to Φ and V via the same shell-sum" — deliberately phrased
  so that *no new dynamical law* is introduced; 1113's rank-agnosticity is what licenses
  this. The wave equation and c-propagation are consequences, not clauses.
- **C4 (source):** the hardest drafting choice. Options considered: (a) source by the full
  T_μν analog (rejected — the spin-2 bootstrap would regenerate statics and double-count the
  recovered Schwarzschild sector); (b) source by a TT-projected density (rejected as an axiom
  clause — TT projection is direction-dependent, not local, so it cannot be a clean local
  law); (c) **adopted:** source by ∂²_t of the local traceless quadrupole density —
  local, frame-stated, kills statics by construction (∂²_t q = 0 for static sources), and
  pushes the transversality question where it honestly belongs: into OB-2.
- **C5 (readout):** listed but explicitly demoted to a derivation obligation — keeping the
  axiom minimal and honoring 1121's finding that the GP→CP extension is the Compute step's
  output.
- **κ fixed by G:** the zero-parameter discipline is the programme's spine; a new dial would
  be a real cost. The claim "one d.o.f., zero parameters" is checkable: Task 3 must land the
  GR quadrupole coefficient with the scalar-sector G and nothing adjustable.

## OB-2 — the axiom's primary attack surface, identified deliberately

A 5-component field sourced and propagating generically radiates helicities 0, ±1, ±2; GR
suppresses the non-TT content via gauge invariance, which CPP (absolute frame, no
diffeomorphism gauge) does not have. The candidate mechanism is GR's *other* half:
conservation. In linearized GR it is ∂^μT_μν = 0 — not gauge choice — that ties monopole and
dipole moments to non-radiative content; CPP's CP-count conservation (mass) and
displacement-rule momentum conservation are the corresponding laws. Whether they suffice is a
real derivation, not a formality — so it is stated as the axiom's primary falsifier ("ships
with its own kill switch"): if OB-2 fails, A3′ as stated predicts extra GW polarizations and
is dead against the multi-detector data. Flagging this *before* DG-3 dispatch is both the
honest move and the tactically correct one (the swarm will find it in minutes; better that
the submission arrives with it named and, ideally, discharged — hence the recommended
sequencing Task 3 → Task 4 → Task 5).

## Why the registry is not touched in this patch

Previewed to the architect as "Task 2 touches the axiom inventory under STOP-and-warn," but
the cleaner protocol crystallized during drafting: contested registries should be touched
*once*, with the reviewed final text, after DG-3 and sign-off — not with a v0.1 candidate
that review may revise. So 1123 stays private-lane; §7 of the candidate records the
registration path explicitly (STOP-and-warn + CONV-002 re-fetch at that step). This also
keeps the multi-window lease risk at zero during the review cycle.

## Discipline notes

- Built on the pushed 1121 (re-synced; architect's hash 1d749cc). Patch 1122
  (founders_vision capture) committed immediately prior in this session — shared root file,
  re-fetched before commit, no drift found.
- NO VERDICT MOVED: no THEO/PRED/ID registered; axiom count unchanged (the A3′ text is a
  *candidate*); no contested file touched.
- Falsifier honored: the completion check asserts and would fail loudly if any l ≥ 3
  descended intact or if the packet content mismatched the protected content.
