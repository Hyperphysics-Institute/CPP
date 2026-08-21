You are one of five independent reviewers (ChatGPT, Grok, Copilot, Gemini,
DeepSeek) on the Conscious Point Physics (CPP) review panel.
IDENTITY (mandatory): in the §8 REVIEWER field put YOUR OWN actual
model/provider name; never echo another seat's name.
INDEPENDENCE (mandatory): your own analysis only.
COUNT-LINE (mandatory): if you execute the §7 script, paste its OWN final
count line VERBATIM ("N/N PASS").
OWN-RUN (mandatory, new this round per CONV-030 §5): SCRIPT-EXECUTED means
YOUR OWN execution. Quoting the package's reference run is INSPECTED and
must be labeled as such — a quoted reference line claimed as
SCRIPT-EXECUTED will be reclassified in the seat ledger.
Please review CONV-031 — the modernization round for **QM-3** ("Bell
Inequality and Entanglement from the Nexus", V3.2): the paper that
answers whether CPP has properly derived quantum entanglement. QM-3's
three theorems have never had a five-seat round (its basis is a
March-2026 internal + three-seat review — the same coverage-debt class
GR-1c's theorems carried before CONV-030 discharged them). Under review:
(A) the three theorems (non-separability; E = −cosθ ⇒ CHSH = 2√2;
no-signaling); (B) the paper's explicit RETRACTION of its own v1
shared-bit-pool argument; (C) the ε-hierarchy reconciliation with the
superdeterminism (SD) series; (D) post-re-ground consistency (the
CONV-014/015/016 arc re-founded the phase variable QM-3's helix encoding
rests on). Everything needed is inline; your steer is in §6; the NEW
verify script is in §7 (7 checks, written Patch 3315 — the paper's
first). Tier every claim (INSPECTED / INDEPENDENTLY RECOMPUTED /
SCRIPT-EXECUTED); answer in the §8 skeleton.

File (provenance; inline content authoritative):
  raw: https://raw.githubusercontent.com/Hyperphysics-Institute/CPP/main/series_quantum_mechanics/conv031_qm3_entanglement_review_package_v1.0.md

---

# CONV-031 Review Package v1.0 — QM-3: entanglement, Bell violation, and the honest retraction

**Dispatched:** 20 Aug 2026, Session 155-equivalent, Patch 3316.
Founder-initiated (query: "Have we properly written about and justified
entanglement?").
**Responses land in:** `series_quantum_mechanics/reviews-CONV-031.md`.
**Settled, out of scope:** the QM re-grounding arc's own verdicts
(CONV-014/015/016: FI-QMRG-1 confirmed-with-amendments; B-QMRG-1
proportionality closed; plane stability closed for the shipped class;
sector CONDITIONAL → RESOLVED), the Born-rule companion c03, the SD
series' own open problems (OPEN-SD-1..4 remain open by design).
**Under review here:** QM-3's theorems and framing as shipped at V3.2.

## §1 Context (cold-start, condensed)

QM-3 derives entanglement from: (i) the spin-½ qubit as a two-component
pattern state whose phase is the ZBW helix angle — under the ratified
re-grounding, φ = orientation of the GP's SSV_net directional content in
the ZBW plane (FI-QMRG-1), so the helix encoding is the spin-qubit
specialization of the sector's one ontology; (ii) a total-spin-zero pair
whose joint pattern state is NON-SEPARABLE (Theorem nonsep) — it cannot
be written as a product of single-particle states; the Nexus maintains
this joint state globally each Absolute Moment tick, enforcing total
DI-bit conservation across all Grid Points regardless of separation;
(iii) the Born rule (companion c03) applied to the non-separable state,
giving E(â,b̂) = −cosθ, hence |CHSH| = 2√2 at optimal angles (Theorem
chsh) — the Tsirelson bound, no super-quantum excess; (iv) no-signaling
(Theorem nosig): each party's marginal is exactly ½ independent of the
other's setting. The paper states its own history plainly: **"The
previous CPP argument was wrong"** — v1 treated the singlet as two
particles sharing a fixed DI-bit pool set at emission, which is an LHV
model capped by Bell at |CHSH| ≤ 2; the retraction is in the shipped
text, anti-erasure.

The SD reconciliation (March 2026 three-seat review, recorded in
`reviews-QM-3.md` + `philosophy-QM-3.md`): the Nexus is a global
atemporal constraint that IS superdeterministic in the strict Bell sense
(measurement independence is violated), but the SD corrections are
O(ε) ~ 10⁻²⁶; at the operational level (ε = 0) QM-3's theorems hold
exactly and Bell violation comes from the non-separable amplitude
structure, not from setting correlations. The SD series carries the
substrate-level correlation machinery (K₀(λ)) as open problems.

## §2 The three theorems (claim chain)

- **T-A (nonsep).** Singlet coefficient matrix C = [[0,1],[−1,0]]/√2 has
  Schmidt rank 2 (det = 1/2 ≠ 0); any product state has rank 1. The
  physical bearer: the Nexus-maintained joint pattern, not per-particle
  properties.
- **T-B (chsh).** ⟨ψ|(â·σ)⊗(b̂·σ)|ψ⟩ = −â·b̂ = −cosθ exactly (general
  unit vectors); CHSH at 0°/90° vs 45°/135° settings = 2√2 exactly;
  a dense scan attains and never exceeds it (Tsirelson respected — CPP
  predicts NO super-quantum violations; this is itself falsifiable
  content).
- **T-C (nosig).** P_A(+|â) = P_B(+|b̂) = 1/2 symbolically,
  setting-independent — the Nexus enforces a constraint, not a channel.
- **Lattice corrections:** O((l_P/λ)²), unobservable at laboratory
  scales (stated, not load-bearing).

## §3 The retraction, made machine-checkable (new, Patch 3315)

The v1 shared-bit-pool model is an LHV. The new verify script's check 5
enumerates ALL 16 deterministic local strategies for the CHSH settings
and finds max |S| = 2 exactly — the retraction was not a stylistic
choice but MATHEMATICALLY FORCED: the old argument could never have
produced the observed 2√2. The panel is asked (Q3) whether the shipped
retraction language adequately reflects this.

## §4 Post-re-ground consistency

QM-3 predates the re-grounding arc but was swept through it (v1.2 at
Patch 2998: attribution relocated to pattern level; v1.3 at 3033: AP-4
payload; V3.2 at 3213: identifier appendix). The helix-phase encoding is
now the FI-QMRG-1 identification specialized to the spin qubit, and the
new script's check 6 verifies the two properties the encoding needs:
same-basis perfect anticorrelation and SU(2) invariance of the singlet
(general symbolic U ⊗ U). The panel is asked (Q4) whether any residual
retired-ontology language survives in the V3.2 text that the sweeps
missed.

## §5 Not claimed / residues

(i) The substrate-level correlation function K₀(λ) and the many-body K
(OPEN-SD-1..4) — the mechanism-level account of HOW the Nexus computes
the joint constraint remains the SD series' open work; QM-3 claims the
operational level only. (ii) Entanglement decoherence threshold
(OPEN-QM-5, ~10¹⁵ eV) untouched. (iii) The linearity/superposition leg
(R-2) was closed-in-regime by B-QMRG-1 at CONV-015/016 with the
convention-labeling obligation standing; QM-3 inherits, does not
re-litigate. (iv) No claim that ε-level setting correlations are
observable; the 10⁻²⁶ estimate's own derivation lives in SD-4.

## §6 Reviewer steers (read your own row)

- **ChatGPT:** independently re-derive E(â,b̂) = −â·b̂ from the singlet
  + Born rule, and verify the CHSH optimal-angle arithmetic; then
  scrutinize T-A's bearer claim — does "the Nexus maintains the joint
  state" add physical content beyond the Hilbert-space statement, or is
  it (acceptably) an interpretive label at this paper's level?
- **Grok:** run §7 and paste the count line verbatim (OWN run — see the
  mandate). Physics steer: attack the ε-hierarchy — is "superdeterministic
  in the strict Bell sense but operationally QM at ε = 0" a coherent
  position or a have-it-both-ways evasion? Rule COHERENT / EVASIVE with
  reasons.
- **Copilot:** archival seat: verify the quoted retraction language
  against the repo .tex (raw link in header); check the March-2026
  review record's ε-hierarchy summary against `philosophy-QM-3.md`; and
  audit that the V3.2 sweeps left no retired per-bit-phase ontology in
  the shipped text. If you run §7, OWN-RUN rules apply.
- **Gemini:** constants/limits seat: the O((l_P/λ)²) lattice-correction
  claim and the O(ε) ~ 10⁻²⁶ figure — check each is stated at the right
  grade (estimate vs derivation) and flag any place the paper's prose
  outruns its warrant.
- **DeepSeek:** recompute checks 0/1/2 by hand if you cannot execute;
  steer: the Tsirelson RESPECT claim (no super-quantum violations) —
  confirm CPP's structure gives exactly the quantum bound and not more,
  and state what experimental result would falsify QM-3 specifically
  (as opposed to falsifying QM generally).
- **All seats:** the round's biggest question is Q5 — is this, at
  modern corpus standards, a PROPER justification of entanglement?

## §7 Verify script (`series_quantum_mechanics/code/3315_qm3_bell_verify.py`, 7 checks)

Run if you can (OWN run); paste the final count line verbatim.
Expected output ends: `7/7 PASS`.

```python
#!/usr/bin/env python3
"""
Patch 3315 verify — QM-3 (Bell inequality and entanglement) machine
verification, written 5 months post-ship to bring the paper up to the
corpus's computation-before-claims standard ahead of its first
five-seat CONV round (CONV-031).

Checks (all exact-symbolic unless noted):
  0. NON-SEPARABILITY (Thm nonsep): the singlet's coefficient matrix has
     Schmidt rank 2 (det = +1/2 != 0); a product state has rank 1.
  1. CORRELATOR (input to Thm chsh): E(a,b) = <psi| (a.sigma)x(b.sigma)
     |psi> = -cos(theta) exactly, for symbolic unit vectors.
  2. CHSH AT OPTIMAL ANGLES (Thm chsh): S = E(a,b) - E(a,b') + E(a',b)
     + E(a',b') = 2*sqrt(2) exactly at the standard 0/45/22.5/67.5 deg
     settings.
  3. TSIRELSON CEILING (numeric): a dense scan over coplanar settings
     never exceeds 2*sqrt(2) (tolerance 1e-9) and attains it.
  4. NO-SIGNALING (Thm nosig): Alice's marginal P(+1|a) = 1/2 exactly,
     symbolically independent of Bob's setting b (and vice versa).
  5. DETERMINISTIC-LHV BOUND (the corrected-away argument): exhaustive
     enumeration of all 16 deterministic local strategies gives
     max |S| = 2 — the shared-bit-pool model QM-3 v1 used, and v3
     explicitly retracted, is an LHV and could never have produced
     2*sqrt(2). The retraction was mathematically forced.
  6. HELIX-PHASE ENCODING CONSISTENCY (FI-QMRG-1 hook): the same-basis
     anticorrelation P(same outcome | theta=0) = 0 exactly, and the
     singlet is basis-invariant (U x U |psi> = det(U)^... -> state
     invariant up to phase for U in SU(2)); checked symbolically for a
     general SU(2) rotation.
"""
import itertools

import numpy as np
import sympy as sp

PASS = []


def check(name, ok, detail=""):
    PASS.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))


# Pauli matrices, symbolic
sx = sp.Matrix([[0, 1], [1, 0]])
sy = sp.Matrix([[0, -sp.I], [sp.I, 0]])
sz = sp.Matrix([[1, 0], [0, -1]])
I2 = sp.eye(2)

# Singlet |psi> = (|01> - |10>)/sqrt(2)
psi = sp.Matrix([0, 1, -1, 0]) / sp.sqrt(2)

# ---------------------------------------------------------------- check 0
C = sp.Matrix([[0, 1], [-1, 0]]) / sp.sqrt(2)     # coefficient matrix c_ij
detC = sp.simplify(C.det())
prod = sp.Matrix([1, 0]) * sp.Matrix([[1, 0]])    # any product state: rank 1
check("0. non-separability: Schmidt rank 2 (det C = 1/2 != 0); product rank 1",
      detC == sp.Rational(1, 2) and C.rank() == 2 and prod.rank() == 1,
      f"det C = {detC}")


def n_sigma(theta, phi):
    return (sp.sin(theta) * sp.cos(phi) * sx
            + sp.sin(theta) * sp.sin(phi) * sy
            + sp.cos(theta) * sz)


def kron(A, B):
    return sp.Matrix(sp.kronecker_product(A, B))


def E_ab(ta, pa, tb, pb):
    Op = kron(n_sigma(ta, pa), n_sigma(tb, pb))
    return sp.simplify((psi.T.conjugate() * Op * psi)[0, 0])


# ---------------------------------------------------------------- check 1
ta, tb = sp.symbols("theta_a theta_b", real=True)
E_general = E_ab(ta, 0, tb, 0)                    # coplanar; general phi below
val = sp.simplify(E_general + sp.cos(ta - tb))
# full generality: symbolic phis too
pa, pb = sp.symbols("phi_a phi_b", real=True)
E_full = E_ab(ta, pa, tb, pb)
# a.b for the two unit vectors:
adotb = (sp.sin(ta) * sp.cos(pa) * sp.sin(tb) * sp.cos(pb)
         + sp.sin(ta) * sp.sin(pa) * sp.sin(tb) * sp.sin(pb)
         + sp.cos(ta) * sp.cos(tb))
val_full = sp.simplify(E_full + adotb)
check("1. correlator E(a,b) = -a.b = -cos(theta) exactly (symbolic, general)",
      val == 0 and val_full == 0,
      "E + a.b == 0 identically")

# ---------------------------------------------------------------- check 2
deg = sp.pi / 180
S_opt = sp.simplify(
    E_ab(0, 0, 45 * deg, 0) - E_ab(0, 0, 135 * deg, 0)
    + E_ab(90 * deg, 0, 45 * deg, 0) + E_ab(90 * deg, 0, 135 * deg, 0))
check("2. CHSH at optimal angles = 2*sqrt(2) exactly (Tsirelson attained)",
      sp.simplify(sp.Abs(S_opt) - 2 * sp.sqrt(2)) == 0,
      f"S = {S_opt}")

# ---------------------------------------------------------------- check 3
angles = np.linspace(0, np.pi, 61)
maxS = 0.0
for a1 in angles:
    for a2 in angles:
        for b1 in angles:
            for b2 in angles:
                S = (-np.cos(a1 - b1) + np.cos(a1 - b2)
                     - np.cos(a2 - b1) - np.cos(a2 - b2))
                maxS = max(maxS, abs(S))
check("3. Tsirelson ceiling: dense scan max |S| <= 2*sqrt(2), attained",
      maxS <= 2 * np.sqrt(2) + 1e-9 and maxS > 2 * np.sqrt(2) - 1e-3,
      f"scan max = {maxS:.9f} vs 2*sqrt(2) = {2*np.sqrt(2):.9f}")

# ---------------------------------------------------------------- check 4
# Alice's marginal for outcome +1 along a, jointly with Bob measuring b:
Pa_plus = sp.simplify(
    (psi.T.conjugate()
     * kron((I2 + n_sigma(ta, pa)) / 2, I2)
     * psi)[0, 0])
Pb_plus = sp.simplify(
    (psi.T.conjugate()
     * kron(I2, (I2 + n_sigma(tb, pb)) / 2)
     * psi)[0, 0])
check("4. no-signaling: both marginals = 1/2 exactly, setting-independent",
      Pa_plus == sp.Rational(1, 2) and Pb_plus == sp.Rational(1, 2),
      f"P_A(+) = {Pa_plus}, P_B(+) = {Pb_plus}")

# ---------------------------------------------------------------- check 5
# Deterministic LHV: A(a) in {+-1} for each of 2 settings; same for B.
settings_a = [0.0, np.pi / 2]
settings_b = [np.pi / 4, 3 * np.pi / 4]
best = 0.0
for Amap in itertools.product([1, -1], repeat=2):
    for Bmap in itertools.product([1, -1], repeat=2):
        S = (Amap[0] * Bmap[0] - Amap[0] * Bmap[1]
             + Amap[1] * Bmap[0] + Amap[1] * Bmap[1])
        best = max(best, abs(S))
check("5. deterministic-LHV bound: max |S| over all 16 strategies = 2 "
      "(the retracted shared-bit-pool model could never reach 2*sqrt(2))",
      abs(best - 2.0) < 1e-12, f"LHV max = {best}")

# ---------------------------------------------------------------- check 6
# Same-basis perfect anticorrelation + SU(2) invariance of the singlet.
P_same = sp.simplify(
    (psi.T.conjugate()
     * (kron((I2 + sz) / 2, (I2 + sz) / 2)
        + kron((I2 - sz) / 2, (I2 - sz) / 2))
     * psi)[0, 0])
al, be = sp.symbols("alpha beta", real=True)
U = sp.Matrix([[sp.cos(al) + sp.I * sp.sin(al) * sp.cos(be),
                sp.I * sp.sin(al) * sp.sin(be)],
               [sp.I * sp.sin(al) * sp.sin(be),
                sp.cos(al) - sp.I * sp.sin(al) * sp.cos(be)]])
UU_psi = sp.simplify(kron(U, U) * psi)
diff = sp.simplify(UU_psi - psi * sp.simplify((U.det())))
# For SU(2), det U = 1 and U x U |singlet> = |singlet>:
detU = sp.simplify(U.det())
invariant = all(sp.simplify(x) == 0 for x in (UU_psi - psi))
check("6. helix-encoding hooks: P(same|theta=0) = 0 exact; singlet SU(2)-invariant",
      P_same == 0 and sp.simplify(detU - 1) == 0 and invariant,
      f"P_same = {P_same}; det U = {detU}; U x U singlet == singlet: {invariant}")

print()
print(f"{sum(PASS)}/{len(PASS)} PASS")
raise SystemExit(0 if all(PASS) else 1)
```

Reference run (Patch 3315 environment; quoting it is INSPECTED, not
SCRIPT-EXECUTED):

```
[PASS] 0. non-separability: Schmidt rank 2 (det C = 1/2 != 0); product rank 1 — det C = 1/2
[PASS] 1. correlator E(a,b) = -a.b = -cos(theta) exactly (symbolic, general) — E + a.b == 0 identically
[PASS] 2. CHSH at optimal angles = 2*sqrt(2) exactly (Tsirelson attained) — S = -2*sqrt(2)
[PASS] 3. Tsirelson ceiling: dense scan max |S| <= 2*sqrt(2), attained — scan max = 2.828427125 vs 2*sqrt(2) = 2.828427125
[PASS] 4. no-signaling: both marginals = 1/2 exactly, setting-independent — P_A(+) = 1/2, P_B(+) = 1/2
[PASS] 5. deterministic-LHV bound: max |S| over all 16 strategies = 2 (the retracted shared-bit-pool model could never reach 2*sqrt(2)) — LHV max = 2
[PASS] 6. helix-encoding hooks: P(same|theta=0) = 0 exact; singlet SU(2)-invariant — P_same = 0; det U = 1; U x U singlet == singlet: True

7/7 PASS
```

## §8 Frozen questions + response skeleton

Answer ALL of Q1–Q6; use the verdict vocabulary given.

- **Q1 (theorems).** Are T-A/T-B/T-C SOUND / SOUND-WITH-GAPS / UNSOUND
  as proved? (One verdict per theorem.)
- **Q2 (physical bearer).** Is the Nexus-maintenance framing of the
  non-separable state ADEQUATE-AT-LEVEL (an honest interpretive label
  for the operational content) / OVERCLAIMED (asserts unearned
  mechanism) / UNDERCLAIMED?
- **Q3 (retraction).** Does the shipped retraction of the v1 LHV
  argument, now backed by the check-5 enumeration, meet the corpus's
  anti-erasure standard — ADEQUATE / NEEDS-STRENGTHENING (say what)?
- **Q4 (ε-hierarchy + sweeps).** Is the SD reconciliation COHERENT /
  EVASIVE? Did the re-ground sweeps leave residual retired ontology in
  V3.2 — CLEAN / RESIDUE-FOUND (cite lines)?
- **Q5 (the founder's question).** At modern corpus standards, is QM-3
  a PROPER justification of entanglement — PROPER /
  PROPER-WITH-NAMED-DEBTS (name them) / NOT-PROPER?
- **Q6 (coverage + residues).** COVERAGE-DISCHARGED for QM-3's
  theorems — YES/NO? Is the §5 residue list COMPLETE / MISSING-ITEMS?

```
REVIEWER: <your own model/provider name>
TIER LEGEND USED: INSPECTED / INDEPENDENTLY RECOMPUTED / SCRIPT-EXECUTED
Q1: <T-A verdict; T-B verdict; T-C verdict> [<tier>] — <2-6 sentences>
Q2: <verdict> [<tier>] — <2-6 sentences>
Q3: <verdict> [<tier>] — <2-6 sentences>
Q4: <COHERENT/EVASIVE; CLEAN/RESIDUE-FOUND> [<tier>] — <2-6 sentences>
Q5: <verdict + named debts if any> — <2-6 sentences>
Q6: <YES/NO; COMPLETE/MISSING-ITEMS> — <1-4 sentences>
SCRIPT: <SCRIPT-EXECUTED (own run) + verbatim final count line |
         INSPECTED (reference run) | NOT-EXECUTED + reason>
DEFECTS/OBJECTIONS: <numbered list or NONE>
```
