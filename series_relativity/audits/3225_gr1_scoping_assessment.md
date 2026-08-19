# GR-1 scoping assessment — is the gravitation arc ready to consolidate?

**Patch 3225.** Founder-requested scoping of a **series** paper (GR-1), not the
flagship. Question asked: do the eight existing gravitational companions
constitute a synthesis GR-1 can assemble, or does GR-1 require new derivation
before it can be written?

**Verdict: GR-1 is ~75% synthesis. The arc is far more complete than its
orphaned filing suggests, but it is NOT a pure write-up — three gaps need
founder rulings and one needs actual derivation.**

---

## §1 — What exists: an intact dependency ladder, ~5,600 lines

Eight papers, none of which were written as strays. They cross-cite each other
explicitly ("companion 7", "companion 8", "companion 11") and form a clean
acyclic ladder:

```
c05  Newtonian gravity from SSV shell broadcast          (349 lines)
  |   source = mass-energy; same mechanism as Coulomb
  v
c07  Weak-field GR                                       (877 lines)
  |   extends DI-bit broadcast to SSV_net VECTOR alongside the scalar;
  |   matches linearised Einstein equations
  v
c08  Strong-field GR + the CPP field equation            (991 lines)
  |   exact Schwarzschild in isotropic coordinates, no approximation,
  |   no free parameters; CP Exclusion Rule replaces the point
  |   singularity with a Planck-density core at r_core = r_S/2
  |
  +---> c09  GW echoes from the Planck core              (714 lines)
  +---> c10  Hawking evaporation modified by the core     (599 lines)
  +---> c11  Kerr from azimuthal SSV_net                  (648 lines)
              |
              +---> c12  Kerr-Newman (M, J, Q)            (617 lines)
              +---> c13  Superradiance from c11           (651 lines)
```

For comparison, SR-1 is 2,762 lines. **The gravitational arc is more than
twice the size of the paper it is currently filed beneath.** That is the
strongest single argument that the filing, not the physics, is what went wrong.

## §2 — The load-bearing claim, and where GR-1's spine comes from

c08 is the keystone. Its claim: the PSR formula
`PSR_eff = l_P/(1 + k·Δ|SSV|)` is *already nonlinear*, so integrating the
mass-energy source over shells — the same shell-broadcast geometry used for
Coulomb's law and Newtonian gravity — yields **the exact Schwarzschild metric
in isotropic coordinates, with no approximation and no free parameters**, and
identifies the CPP equation playing the role of Einstein's field equations.

If that holds, GR-1's spine writes itself: one mechanism (shell-broadcast SSV)
generates Coulomb, Newton, weak-field GR and exact Schwarzschild as successive
regimes of a single nonlinear response. **That is a genuine series-paper
thesis**, and it is already distributed across c05, c07 and c08 rather than
needing invention.

## §3 — GAP 1 (needs a ruling): the field equations are claimed, not derived

Seven of eight papers discuss "field equations", but the treatment differs:

- c07: the CPP field equations are "the requirement that the metric g_μν
  [satisfy a] self-consistency condition ≡ Einstein field equations".
- c08: titled "…and the CPP Field Equation"; "identifies the CPP equation that
  plays the role of Einstein's field equations".

"Plays the role of" and "≡ … in [the continuum limit]" are **correspondence
claims, not derivations**. Recovering the Schwarzschild and Kerr *solutions*
is not the same as deriving the *equations* whose solutions they are — one can
reproduce specific metrics without ever obtaining the general field equation,
and a reader in general relativity will make exactly that distinction.

**Ruling needed:** does GR-1 claim to derive the field equations, or does it
claim exact recovery of the metric family and register the general equation as
open? The second is defensible and honest; the first requires work not visible
in the corpus. This is the single most consequential wording decision in the
paper.

## §4 — GAP 2 (needs derivation): no classical tests, no energy-momentum tensor

Term coverage across the eight papers:

| Concept | Papers mentioning |
|---|---|
| Schwarzschild | 7 of 8 |
| field equation | 7 of 8 |
| Einstein field equations | 3 of 8 |
| equivalence principle | 2 of 8 |
| geodesic | 1 of 8 |
| stress-energy | 1 of 8 |
| gravitational lensing | 1 of 8 |
| **perihelion precession** | **0** |
| **Shapiro delay** | **0** |
| **energy-momentum tensor** | **0** |
| **Birkhoff's theorem** | **0** |

The three classical tests of general relativity — perihelion precession, light
deflection, Shapiro delay — are **absent or barely touched**. So is the
energy-momentum tensor, which is what the field equations are equated *to*.

This matters more for a gravitation paper than the raw count suggests: those
three tests are the conventional entry criterion for any gravitational theory,
and a reader will look for them before anything else. Their absence alongside
an exact-Schwarzschild claim is conspicuous, because **the tests follow from
the Schwarzschild metric by standard geodesic integration** — if the metric is
genuinely exact, the tests should be recoverable without new physics.

**Assessment: this is derivation work, but bounded and low-risk** — standard
computations on a metric the corpus already claims. It is the clearest
candidate for what GR-1 must add rather than assemble.

## §5 — GAP 3 (needs a ruling): no cosmology, and that boundary must be stated

Zero occurrences of FRW, Friedmann, or Birkhoff across all eight papers; two
passing mentions of "cosmolog". Meanwhile `OPEN-EU-1` already registers an
axiom-level derivation of FRW/VSL homogeneity as open, and the dark-energy
lane is running an entirely separate campaign on substrate phase transitions.

**Ruling needed: is GR-1 a *local* gravitation paper?** If yes — and the
evidence says it is — the scope boundary should be declared explicitly in the
abstract rather than left for a reader to discover. A gravitation series paper
silent on cosmology reads as an omission; one that states "local gravitation;
cosmological solutions are pursued separately under OPEN-EU-1 and the
dark-energy programme" reads as discipline.

## §6 — What GR-1 must do that no companion does

Even granting every companion result, a series paper owes four things none of
them provide:

1. **The unifying statement**, made once: shell-broadcast SSV as a single
   mechanism whose regimes are Coulomb → Newton → weak-field → exact
   Schwarzschild, with the nonlinearity of the PSR formula as the reason one
   mechanism spans them.
2. **The scalar→vector transition, motivated rather than asserted.** c05 uses
   the SSV scalar; c07 introduces `SSV_net` as a vector. That step is where
   gravity stops resembling electrostatics, and it is currently introduced
   inside a companion rather than argued at series level.
3. **The epistemic ledger.** Which results are exact, which are correspondence
   claims, which are conditional. The companions each hedge locally — c07 and
   c08 carry six and seven limitation-flagged passages respectively — but
   nothing aggregates them, so the arc's true standing is invisible.
4. **The classical tests** (§4).

## §7 — Caution: do not inherit SR-1's status silently

The arc descends from SR-1, which carries a retracted prediction set
(Patch 2474), a class-coverage theorem withdrawn on an erroneous cap expansion
(`f^{1/2}` published, `f^{5/2}` correct), and a geometric route closed
negative-for-mechanism. GR-1 rests on the same PSR machinery.

**GR-1 must state what it inherits from SR-1 and what SR-1 withdrew.** SF-line
papers read as consolidations; if GR-1 reads that way while resting on
partially withdrawn ground, the first careful reader finds it, and finds it
after publication.

## §8 — Recommendation

**Write GR-1 as a synthesis with three declared additions**, in this order:

1. Assemble §6.1–6.3 from existing material (synthesis, no new physics).
2. Derive the three classical tests from the c08 Schwarzschild metric
   (§4 — bounded new work, and the highest-value single addition).
3. Rule on the field-equation wording (§3) and the cosmological boundary (§5).

**Hold the eight companions out of the first deposit wave.** They currently sit
in the queue as parentless SR companions. Depositing them that way mints
permanent DOIs against an identity that is about to change, and a Zenodo
preprint can only be withdrawn, never erased — leaving eight gravitation papers
publicly filed as special-relativity companions, or republished under new
identities with the old DOIs still resolving to the old framing. The other 105
papers are unaffected.

**Renumbering falls out for free.** `c8 spin_I` collides with
`c08_strong-field_GR`, and `c9 spin_II` with `c09_GW_echoes`. Moving c05 and
c07–c13 into a GR series dissolves both collisions: the spin papers keep c8/c9
in the SR line, the gravitational papers take GR-series identifiers.

**Unrelated defect found while scoping, worth fixing whoever does it:**
`series_relativity/SR_companion_papers/c08_strong-field_GR.tex` exists as BOTH
a directory and a file of the same name. Every recursive tool in this corpus
has to special-case it, and several scans in this session errored on it.

---

*Physics-picture authority remains the founder's. This assessment reports what
the corpus contains and what a series paper would owe; it rules on nothing.*
