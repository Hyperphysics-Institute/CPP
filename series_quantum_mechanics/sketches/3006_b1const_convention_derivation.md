# OPEN-QMRG-B1-CONST DISPOSITION CANDIDATE — THE COEFFICIENT DERIVED, THE PARTICIPATION RATIO QUARANTINED

**Patch 3006 (4 Aug 2026).** Disposes OPEN-QMRG-B1-CONST (registered
CONV-015 adjudication E-3; conditionality trigger T2) by the
trigger's own disjunction — DERIVE what is derivable, FORMALLY
QUARANTINE what is genuinely lattice-dependent — PANEL-PENDING.
Verify script:
`series_quantum_mechanics/code/3006_b1const_coefficient_check.py` —
EXECUTED this patch, ALL ASSERTIONS PASS, stdout in §5. Unprinted
RNG-stream sentinel included per the KEY-DESIGN RULE (next round's
KEY-J).

**The obligation (T2, GPT's formulation adopted at CONV-015 E-6):**
"derive or formally quarantine the turnover/participation constant so
that the corpus cleanly separates the proved B1 proportionality from
any exact normalization claim."

---

## §1 — The two-layer disposition

GPT's CONV-015 dissection listed the coefficient's dependencies:
peak vs RMS vs complex amplitude; per-oscillator vs per-mode;
quadrature counting; participation fraction; the definition of μ.
Read carefully, the list splits into two different kinds of unknown:

- **Convention choices** (which quantity "amplitude" names; how
  quadratures are counted): not physics unknowns — resolved by
  DECLARING the convention and DERIVING the coefficient in it.
- **One genuine substrate unknown**: the participation/turnover
  bookkeeping between the REGISTERED count ρ and the MODE occupation
  N. This is lattice physics not yet derived — quarantined by name.

## §2 — LAYER 1 (DERIVED): the coefficient is exactly 1, and the canonical ½ is the quadrature split of the rotating pattern

**Declared convention.** The bridge's object is the cycle-averaged
mean-square in-plane register displacement ⟨S_⊥²⟩. This is the
operationally natural reading: the per-Moment register samples the
rotating ZBW pattern across its cycle (P-3 temporal synchrony;
cycle-distributed arrivals per the 3002 derivation), so the sustained
register statistic IS the cycle average.

**Derivation (exact-in-regime).** For a harmonic mode, the virial
theorem gives time-averaged potential energy = E/2 exactly:
⟨½μω²S²⟩ = E/2 ⟹ **⟨S_⊥²⟩ = E/(μω²), coefficient EXACTLY 1.**
With the mode energy E = Nħω (input I-3 of the 3002 derivation):

    ⟨S_⊥²⟩ = N·ħ/(μω)          [coefficient 1, mean-square convention]

Regime: corrections O((γ/ω)²) in the turnover rate — measured (§5d):
the coefficient reads 1.000/0.996/0.987 as γ/ω spans 0.005→0.08,
exactly the quadratic drift, negligible in the weak-turnover regime
the bridge is registered for.

**The canonical ½, derived.** The ZBW pattern ROTATES in the plane:
S(t) = A(cos ωt, sin ωt). Then |S|² = A² identically while each
Cartesian quadrature time-averages to A²/2:

    ⟨S_x²⟩ = ⟨S_y²⟩ = N·ħ/(2μω)   [the canonical per-quadrature ½]

Verified to 6 decimal places (§5b). **In CPP the canonical 1/(2μω)
per quantum per quadrature is not a bookkeeping choice — it is the
two-quadrature split of a rotating phase vector.** The convention
table closes: mean-square coefficient 1; per-quadrature ½;
peak-square 2 (verified, §5c). Every entry in GPT's dependency list
except one is now a derived row of this table.

## §3 — LAYER 2 (FORMALLY QUARANTINED): the participation ratio η

**Definition (registered substrate parameter).** η ≡ ρ/N — the ratio
of the registered DI-bit count density (the SSV_abs book, AP-2) to
the coherent-mode occupation it maintains. η encodes the microscopic
turnover law (fraction of register energy re-emitted vs retained per
Moment) and the mode's participation structure; it is dimensionless,
O(1)-expected, and NOT derived here. B-QMRG-1 with its constant
therefore reads, in full honesty:

    ⟨S_⊥²⟩ = (ħ/μω) · ρ/η

with everything except η derived. **Registered checkable claim
(the quarantine's content):** η is mode-independent in the linear
weak-field regime — the claim that makes the proportionality
constant a CONSTANT. Its lattice-level derivation is the one item
this disposition leaves open, now named, isolated, and one number
deep.

**The separation is clean — verified, not asserted.** The
load-bearing check (§5d): across a turnover scan in which the stored
energy varies by ×17, the Layer-1 coefficient stays at 1. Layer 2
(how much energy the turnover lets the mode hold for given input)
does not contaminate Layer 1 (the displacement-per-stored-quantum
relation). This invariance is exactly what "formally quarantine"
must mean for the corpus to cleanly separate the proved
proportionality from normalization claims: the unknown lives in ONE
named factor, and the derived layer is provably indifferent to it.

## §4 — Status, and what this does to the CONV-015 exclusions

**OPEN-QMRG-B1-CONST status: DISPOSED (CONV-016 adjudication, Q2
5–0; Patch 3008; the E = Nħω provenance audited acyclic at
`conv016_adjudication.md` §5).** **Convention-labeling obligation
(CONV-016 amendment, GPT):** coefficient 1 = the FULL in-plane
cycle-averaged mean square; ½ = EITHER single quadrature; peak² =
2× mean-square; conversions between conventions must be explicit;
convention-INDEPENDENCE is not claimed. Original candidate framing: Under this disposition, if adjudicated:
- The E-1 exclusion "any claim that the canonical 1/(2ω) coefficient
  is fully substrate-derived" RESOLVES into precise form: the
  coefficient IS derived (virial + quadrature split, exact-in-regime)
  GIVEN mode energy E = Nħω; what is not derived is η = ρ/N. Claims
  citing the canonical normalization become admissible WITH the η
  caveat; claims of an exact ρ-calibrated amplitude remain barred
  pending η's lattice derivation.
- Trigger T2 is satisfied on its own disjunction ("derive or
  formally quarantine") — with most of it landing on the DERIVE side.
- The panel should attack: (i) whether the declared convention is
  the right operational reading of the register statistic; (ii)
  whether E = Nħω smuggles quantization (it is I-3 of the adjudicated
  3002 derivation — E = ħν_C, Tier 1 — but the panel may re-test its
  standing HERE, where the exact coefficient now leans on it); (iii)
  whether η's mode-independence claim is the right quarantine
  boundary or hides structure.

**Enactment this patch:** QM-1 → v2.6 (Grade remark: B1-CONST →
disposition candidate; the convention table and the η quarantine
stated). Bar scope and conditional note UNCHANGED — T2 moves only
through adjudication. **Both trigger items (T1 Patch 3005, T2 this
patch) are now candidates: the arc is ready for CONV-016,
potentially its terminal round.**

## §5 — Verify stdout (EXECUTED, Patch 3006)

```
--- (a) COEFFICIENT: C = <S^2> mu omega^2 / <E> ---
 omega=1.0, rate=32.0: <S^2>=7.4790e+02, <E>=7.5001e+02, C=0.997
 omega=2.0, rate=32.0: <S^2>=3.7208e+02, <E>=1.4899e+03, C=0.999
 omega=1.0, rate=128.0: <S^2>=3.3041e+03, <E>=3.3073e+03, C=0.999
 PASS: the mean-square coefficient is EXACTLY 1 (harmonic virial), all configs

--- (b) QUADRATURE SPLIT: circular rotating in-plane pattern ---
 <S_x^2>/<S^2> = 0.500001
 PASS: the canonical 1/2 IS the two-quadrature split of the rotating pattern

--- (c) PEAK CONVENTION: peak^2 / <S^2> for near-coherent motion ---
 peak^2/<S^2> = 2.0000
 PASS: the convention table's factor-2 row verified

--- (d) SEPARATION: gamma-scan — Layer-1 coefficient invariant under turnover ---
 gamma=0.005: <E>=3.2306e+03 (varies with turnover), C=1.000 (must not)
 gamma=0.02: <E>=7.6669e+02 (varies with turnover), C=0.996 (must not)
 gamma=0.08: <E>=1.9037e+02 (varies with turnover), C=0.987 (must not)
 PASS: stored energy varies x17.0 across the turnover scan; the coefficient stays 1 —
       Layer 1 (derived) is invariant under Layer 2 (quarantined eta); the separation is CLEAN

ALL ASSERTIONS PASS
```

**Ledger:** DM untouched; `data/kmem2` absent. QM: B1-CONST →
DISPOSITION CANDIDATE (panel-pending); T1 MULTILINK candidate
standing (3005); bar scope unchanged; sector CONDITIONAL; nothing
minted. NEXT: CONV-016 dispatch (T1 + T2 adjudication; KEY-I on the
3005 sentinel, KEY-J on this patch's sentinel — both compliant with
the KEY-DESIGN RULE).
