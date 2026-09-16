# Chirality Axiom — Maturation Document (living; pre-panel)

**Status:** MATURATION, not a proposal. No AP number minted. Founder direction 16 Sep 2026: *"explore what the
axiom would be deeply and be fully convinced about the specifics and nature of the axiom before we ask the panel
for either permission, or whether we should do it."* This file is the working object; every patch in the arc
updates it. It goes to the panel only when §6's readiness criteria are all met.

**Lane:** EW (40xx). **Opened:** Patch 4072.

---

## 1. Why an axiom at all (established)

Four routes to a parity-odd source inside the present nine axioms are closed: n̂ static (4046), Mechanism A's
δ-tilt (4068 — breaks T, not P), EM/DP-sea magnetism (4069/4070 — P-even, and a convention), internal vector
structure (4071). A1′ gives a CP exactly three attributes — polarity ±, type, position — none P-odd.
**CPP's axiom set contains no parity-odd element.**

## 2. What kind of object can carry handedness (established at 4072)

**2a. "n̂ versus −n̂" is not a handedness in four dimensions.** In ℝ⁴, det(−I) = +1: point inversion is a proper
rotation, and it preserves the 600-cell. So (600-cell, n̂) and (600-cell, −n̂) are congruent by a rotation — the
same configuration turned around, not mirror images. The 3D intuition (where inversion *is* parity) does not
carry over. **Consequence:** FI-C-9, *as worded* in the CAP-1 scope ("which of {n̂, −n̂} is physical"), names no
chirality. If FI-C-9 is instead read as an orientation of ℝ⁴ itself, it is P-odd — but then it is a global sign
with no physical carrier. §3 supplies the carrier.

**2b. One rotation suffices, if it is a double rotation.** 4071's threshold (four independent directions) is
correct for *vector* attributes. A 4D rotation is a *bivector* B, and a bivector has its own pseudoscalar,
B∧B (the Pfaffian):

| rotation | B∧B | handedness |
|---|---|---|
| simple — one plane (the 3D-like spin) | identically 0 | none |
| double — two orthogonal planes | ≠ 0 | exists |
| isoclinic, one relative sense (self-dual) | +2 | left |
| isoclinic, other relative sense (anti-self-dual) | −2 | right |

B∧B is invariant under every proper rotation (1.4×10⁻¹⁴) and flips exactly under every reflection. **A single
double rotation is a genuine P-odd object**, native to a theory whose CPs already rotate (the ZBW).

## 2c. Founder answers (16 Sep 2026, verbatim, filed at 4073)

> *"I don't know the answer to 1 and 2. That would be an axiomatic declaration.*
> *3) the CP antiparticles have been defined exactly as you describe. If there is an additional reversal, such as a spin, that would be axiomatic, and is not defined by CPP.*
> *1) there is no second parameter to be turning other than if it had a spin direction/pole, which would be an axiomatic addition.*
> *2) There is no known second plane of rotation, and no second parameter to be rotating in. This is an axiomatic addition to add an additional variable, such as spin."*

**Consequences.** **F9 RESOLVED** — a CPP antiparticle is the same CP with opposite polarity, and nothing else
reverses. **Q1/Q2 RESOLVED** — a CP has no second plane or second rotating parameter; any such thing is an
axiomatic addition.

**CORRECTION to §3 as drafted at 4072.** χ was described as "adds no attribute; specifies the existing ZBW." The
founder's answers show the ZBW has no second plane to specify. **χ adds a variable.** It is not native; it is one
instance of location L2 below.

## 2d. What composites can and cannot do (established at 4073, S1 conditional on F1a)

- **S1 — composites confined to 3-space are never handed.** B∧B is a 4-form and needs all four dimensions. Any
  rotation *or any sum of rotations* — any number of orbits, captured DPs, colour planes — confined to a
  3-dimensional subspace has B∧B ≡ 0 (verified exactly, up to five superposed rotations). SPIN-1's captured-DP
  orbit, the ZBW transverse plane and the qDP colour planes therefore cannot supply handedness **if** they all lie
  in the 3-space perpendicular to n̂. *Conditional on F1a.*
- **S2 — handedness needs a rotation into the fourth axis, and it is helicity-shaped.** Writing B = n̂∧e + b,
  B∧B = 2 e·ω exactly (3.6×10⁻¹⁵), where ω is the 3D spin axis of b and e the partner of a rotation in a plane
  containing n̂. The pseudoscalar is the alignment of a spin axis with a fourth-axis rotation.
- **S3 — the substrate's symmetry already contains both hands.** The 600-cell's vertices are the unit
  quaternions of 2I; left and right quaternion multiplication each preserve the 600-cell, carry opposite
  duality (B∧B = ±0.789568), and are exchanged by conjugation (det −1). H4⁺ = (2I × 2I)/ℤ₂ is split into a left
  and a right factor, and nothing in the axioms prefers either.

## 2e. Where the axiom can live — three locations (the real decision)

| | location | what it adds | strength | risk |
|---|---|---|---|---|
| **L1** | a primitive chirality label on each CP (like polarity) | a new binary variable | minimal, clean | no geometric content; the PD-007 "added attribute" concern |
| **L2** | a rotation into the fourth axis (founder's "spin direction/pole"; χ is an instance) | a new rotational variable | pseudoscalar is naturally a helicity (S2), which is what the weak force selects | heaviest; must be shown not to enter EM (F2) |
| **L3** | a rule selecting one of H4⁺'s two existing factors — e.g. the W⁰ catalytic step acts by left-isoclinic transformation only | **no new variable**; a law, not an attribute | matches the Standard Model, where chirality lives in the *coupling*, not in a particle property; uses a split already in the substrate (S3) | may be W-specific ⇒ must be shown to reach K3 Δp_LR and baryogenesis, or it fails F8 |

**Claude's recommendation (PD-006): explore L3 first, L2 second, L1 last.** L3 adds no variable, which the
founder's answers make the heaviest kind of addition; it puts chirality where the Standard Model puts it; and it
uses structure the 600-cell already has. Its specific danger is single-use, and F8 is the test that decides it.

## 3. The candidate axiom (leading form)

> **Axiom candidate χ (draft).** The ZBW of a Conscious Point is a *double* rotation — circulation in two
> orthogonal planes at once — whose relative sense (self-dual or anti-self-dual) is fixed by the CP's polarity:
> self-dual for one polarity, anti-self-dual for the other.

**What it adds:** no new particle, field, attribute, or lattice change. It *specifies* the ZBW (a second plane)
and ties that plane's relative sense to polarity (an existing attribute).

**What it would do, structurally (checked at 4072 as a truth table, not derived):** under **P** the geometry
mirrors and duality flips, polarity does not → rule violated. Under **C** polarity flips, geometry does not →
violated. Under **CP** both flip → **obeyed**. So P and C each broken, CP conserved — the weak sector's pattern
falls out of the rule's form. *Caveat: this is a consistency property of the rule, not a derivation of V−A.*

**What it would give FI-C-9:** a meaning. The corpus's "one substrate sign" becomes the duality of the ZBW double
rotation — a local, dynamical carrier for what is currently a global sign.

**Alternative form (weaker, kept for comparison):** a primitive binary chirality label on each CP, P-odd by
definition. Rejected as leading because it is an *added* attribute with no geometric content — the thing PD-007
warns against — whereas χ reads handedness off a rotation CPP already has.

## 4. Non-negotiable filters (the axiom must pass all)

| # | filter | source | χ status |
|---|---|---|---|
| F1 | P-odd under **physical** parity | definition | passes (2b) — *pending F1a* |
| F1a | physical parity defined precisely in CPP's 4D setting — incl. where physical 3-space sits relative to n̂ | open | **UNDEFINED — blocking; S1 depends on it** |
| F2 | EM stays P-even | 4069/4070, experiment | must show the double rotation does not enter the EM force law |
| F3 | strong interaction stays P-even | experiment | untested |
| F4 | weak: P and C maximal, CP ≈ conserved | experiment | pattern passes (§3); **maximality** not shown |
| F5 | small CP violation has a source | CKM phase | χ gives CP *exactly* conserved; needs a second source — candidate sign(δ) via CPT, untested |
| F6 | CPT exact | theorem | untested |
| F7 | no new tunable parameter | PD-007 | passes in form (duality is binary) |
| F8 | load-bearing in ≥ 3 disjoint sectors | PD-007, 4071 | targets named (K3 Δp_LR, W V−A, baryogenesis); none derived |
| F9 | antiparticle = opposite polarity in CPP | founder 16 Sep | **RESOLVED (4073)** — confirmed, nothing else reverses |

## 5. Physics questions for the founder (picture form)

- **Q1 — ANSWERED 4073 (see 2c).** When a CP performs its ZBW, does it circulate in *one* plane only, or is there simultaneously a
  circulation in a second plane at right angles to the first — so that the CP is turning in two ways at once?
- **Q2 — ANSWERED 4073.** If two, do a positive and a negative CP turn the same way in the second plane relative to the first,
  or opposite ways?
- **Q3 — ANSWERED 4073.** Is the antiparticle of a CP simply the same CP with opposite polarity, or is more reversed than that?

## 6. Readiness criteria for the panel (all must hold)

1. F1a resolved (physical parity defined).
2. ~~Q1–Q3 answered~~ **DONE 4073.** Location chosen among L1/L2/L3 (§2e), by the founder, on a matured comparison.
3. F2 and F3 shown (the axiom leaves EM and strong P-even), not assumed.
4. At least one of the three F8 targets derived far enough to show a non-trivial number or sign.
5. ~~F9 verified~~ **DONE 4073.**
6. Falsifiers written (§7).

## 7. Falsifiers (draft)

- An observed P-odd EM or strong effect at a level the axiom predicts to be zero.
- The double rotation, once specified, feeding into the EM force law (would make EM P-odd — excluded).
- K3 Δp_LR computed under χ disagreeing with its established magnitude.
- CPP antiparticles shown not to be polarity-reversed (breaks §3's CP argument).

## 8. Log

- **4073** — founder answers filed (2c); F9 resolved; §3's "native" claim corrected (χ adds a variable); S1 (3-space composites never handed, conditional on F1a), S2 (handedness = helicity-shaped rotation into the 4th axis), S3 (H4⁺ already split into left/right factors) established; three axiom locations L1/L2/L3 laid out with recommendation L3 → L2 → L1.
- **4072** — document opened; 2a (n̂ vs −n̂ is not a chirality in ℝ⁴) and 2b (a double rotation carries a
  pseudoscalar; simple rotation does not) established; candidate χ drafted; filters, founder questions,
  readiness criteria and falsifiers written.
