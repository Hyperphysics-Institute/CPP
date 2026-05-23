# B.2.q1 — Framework Axiomatization of $P_{TI}$ Representation Theory at Layer 3

**Sub-question:** B.2.q1 — minimal algebraic realization of $\sigma_{cycle}$ via representation theory of the framework parity group $P_{TI} = \mathbb{Z}_2 \times \mathbb{Z}_2$ (Layer 2 closed at Patch 0536 §12; Layer 3 promotion opened at this Patch).

**Promotion scope:** sketch-document Layer 3 — rigorous framework axiomatization of $P_{TI}$ representation theory on finite-dimensional matter-state Hilbert spaces, with explicit identification of where finite-dimensionality enters and what extension to infinite-dimensional / history-dependent / nonlocal-temporal realizations would require. Rigorous proof of the Minimal Algebraic Realization Theorem under the finite-dimensional framework commitment. Resolution of Patch 0538 §14.2 calibration item by making the finite-dimensional scope qualifier load-bearing rather than acknowledged-but-unframed.

**Patch:** 0542, Session 140 (22 May 2026), second Layer 3 promotion in the F.1 sub-question's trajectory; opens the Priority 1 chain (Target 2 → Target 3) per Patch 0540 scoping document §4.1.

**Patch 0542 candidacy:** Target 2 per Patch 0540 scoping document §4.3 — B.2.q1 framework axiomatization. Selected as Patch 0542 per the recommended Priority 1 chain opening following Patch 0541's G.b independent-target opening at Target 1 (B.1.q4 full algebraic derivation). The chain Target 2 → Target 3 closes the two strongest cross-reviewer-convergent calibration items (§14.1 + §14.2) in coupled fashion.

---

## §0 Working-session firewall

This Patch promotes B.2.q1's sketch Layer 2 closure (Patch 0536 §12) to sketch-document Layer 3 — rigorous representation-theoretic axiomatization of $P_{TI} = \mathbb{Z}_2 \times \mathbb{Z}_2$ on finite-dimensional matter-state Hilbert spaces, with formal proof of the Minimal Algebraic Realization Theorem under explicit framework commitments and explicit scope-qualifier preservation. The promotion is per-target and trajectory-bounded per §15.7 of `F1_phase2_foundations_work.md` ("each Layer 3 promotion is its own gated trajectory") and §17.7 of `templates/operating_system.md` (status-upgrade-Patch-style scope-bounded execution applies to Layer 3 closure Patches).

This Patch opens the **Priority 1 chain** (Target 2 → Target 3 per Patch 0540 §4.1) but does NOT close it. Target 3 (B.1.q1 matter-state independent derivation Layer 3) is the next Patch in the chain; this Patch is its prerequisite, not its delivery.

### §0.1 Anti-priorities sustained at this Patch

1. **No Target 3 work.** Target 3 (B.1.q1 matter-state independent derivation Layer 3) is the next Patch in the Priority 1 chain. This Patch establishes the framework axiomatization that Target 3 uses; the matter-state-irrep enumeration and Schur-orthogonality CG factor computation belong to Target 3, not this Patch.
2. **No other sub-question Layer 3 promotion.** Targets 4–7 from Patch 0540 scoping document §2 (B.1.d substrate-locality temporal extension, B.3.q1 corollary, B.1.q3 PT propagation, B.1.q2 zero curl) remain at sketch Layer 2 status and are NOT advanced in this Patch. Each is its own gated trajectory.
3. **No F.1 sub-question status change.** F.1 status remains "SUBSTANTIVE SKETCH-LEVEL CLOSURE at Layer 2 under the minimal-local-first-order realization framework, pending Layer 3 promotion + supplementary work on the 7 open sub-questions and higher-order extensions" per Patch 0539 §15.2. B.2.q1 Layer 3 closure does NOT propagate to F.1 status until Layer 3 promotion arc completes + Layer 3 reviewer-pause cycle + Layer 3 status upgrade per §17 codified discipline.
4. **No v1.0 SHIPPED edits.** Chirality Continuum v1.0, Capotauro v2.0 v1.0, SF-2 v1.0, SM-2 v1.0, SF-4 v4.4 all `.tex` sources frozen.
5. **No Phase 1 §11 / Phase 2 §12 polished content modifications** in `F1_subquestion_pcd_orientation_link.md`. The Patch 0528 §14.17 calibrated framing is immutable per §17.8.
6. **No Patches 0531–0541a immutable content modifications** in `F1_phase2_foundations_work.md`, `F1_layer3_promotion_scoping.md`, or `F1_layer3_b1q4_algebraic_derivation.md`. Patch 0536 §12 (the Layer 2 sketch this promotion builds on) is preserved as historical record; this Layer 3 document is a separate, additive artifact in `layer3_promotion/`, not an inline edit.
7. **No reviewer-pause checkpoint modifications** at `reviewer_pause/F1_reviewer_pause_checkpoint_patches_0531_0537_v1.0.md` or `reviewer_pause/F1_reviewer_pause_feedback_record_v1.0.md` (preserved as historical records per §17.8).
8. **No F.1 flagship paper assembly trigger.** Per `templates/paper_completion_checklist.md` Reviewer-Pause Cycle Precondition section, flagship paper assembly requires Layer 3 promotion arc completion + Layer 3 reviewer-pause + Layer 3 status upgrade. This Patch closes ONE Layer 3 target; the arc is not yet complete.
9. **No infinite-dimensional extension.** The Layer 3 theorem axiomatizes the finite-dimensional framework commitment and proves the minimal algebraic realization within it. Extension to infinite-dimensional, history-dependent, or nonlocal-temporal realizations is **registered as Layer 4 territory / long-term programme target** but not engaged at this Patch. §8 identifies the formal points where finite-dimensionality is used and the open questions that remain at the infinite-dimensional boundary.
10. **No F.2 / F.3 substantive content trajectory opening.** Both remain DEFERRED at decision-gate level per Patch 0539 §15.5.
11. **No long-term programme target work** (chirality scale from polytope geometry / infinite-dimensional realization theorems). REGISTERED + DEFERRED per Patch 0528 §14.17 and Patch 0539 §15.5.

### §0.2 What this Layer 3 promotion IS

- Rigorous representation theory of $P_{TI} = \mathbb{Z}_2 \times \mathbb{Z}_2$ over $\mathbb{C}$ and over $\mathbb{R}$, with explicit character table and orthogonality relations.
- Explicit framework commitment to finite-dimensional matter-state Hilbert spaces, stated as Axiomatic Commitment AC-1 with derivation from CPP framework primitives (A1 + Reading C + first-shell-content matter-state construction).
- Maschke's theorem applied: complete reducibility of finite-dimensional $P_{TI}$-representations over $\mathbb{C}$ (and over $\mathbb{R}$ via Frobenius-Schur indicator structure).
- Minimal Algebraic Realization Theorem (B.2.q1 Layer 3) stated and proved rigorously under AC-1, with each of the four proof steps fully formalized.
- Non-multiplicative-matrix-action ruling-out via minimal-polynomial + diagonalization arguments, with explicit finite-dimensional dependencies identified.
- Cross-reference to Capotauro v2.0 spatial-sector parallel: chirality $\chi$ in I-odd irrep vs CPP $\sigma_{cycle}$ in T-odd irrep — same rep-theoretic structure in different irreps of the same parity group.
- Identification of where AC-1 finite-dimensionality is load-bearing (Step 1 polynomial reduction, Step 4 minimality, §6 non-multiplicative ruling-out), and what the theorem says outside AC-1 (nothing — explicitly out of scope).
- Resolution of Patch 0538 §14.2 calibration item: the finite-dimensional scope is now load-bearing axiomatic commitment AC-1, not ad-hoc qualifier; the theorem's domain of applicability is explicitly the AC-1 setting.

### §0.3 What this Layer 3 promotion is NOT

- NOT a derivation of finite-dimensionality of matter-state Hilbert spaces from CPP axioms A1–A11 alone (AC-1 captures the construction commitment from Reading C + first-shell-content; deriving AC-1 from deeper axioms would be Layer 4 territory).
- NOT an extension to infinite-dimensional / history-dependent / nonlocal-temporal realizations (that is the long-term programme target, deferred).
- NOT a derivation of $P_{TI}$ from A5 alone (A5.2 + A5.3 give $T^2 = I^2 = 1$ and $[T, I] = 1$ as framework commitments; the group structure $P_{TI} = \langle T, I\rangle \cong \mathbb{Z}_2 \times \mathbb{Z}_2$ is an immediate consequence but the framework-symmetry generator commutativity itself is a framework commitment).
- NOT a closure of B.2.q2 (minimal-derivative-order formalization), B.2.q3 (derivative-order-1 alternatives enumeration), or B.2.q4 (§3.4 alternatives re-examination).
- NOT a promotion of the result to programme-level Findings registry.
- NOT a flagship-paper-section draft; it is a sketch-document Layer 3 artifact in `layer3_promotion/`.

---

## §1 Layer 3 promotion context

### §1.1 What Layer 2 established at Patch 0536 §12

Patch 0536 §12 closed B.2.q1 at sketch Layer 2 with:

- §12.2 formal setup with framework parity group $P_{TI} = \langle T, I\rangle \cong \mathbb{Z}_2 \times \mathbb{Z}_2$ and identification of $\sigma_{cycle}$ as the framework primitive generating the T-odd-I-even 1D irrep.
- §12.3 representation theory recap with the four 1D irreps and tensor product structure.
- §12.4 Minimal Algebraic Realization Theorem statement with three substantive content parts: (a) $\sigma_{cycle}^2 = 1$ forces affine $\sigma_{cycle}$-dependence; (b) $P_{TI}$-irrep decomposition forces multiplicative form; (c) abelian-group-structure forces 1D irreps → minimality.
- §12.5 proof in four steps: polynomial reduction modulo $\sigma_{cycle}^2 - 1$; $P_{TI}$-decomposition via character orthogonality; TI-odd operator restriction forcing $a = 0$; minimality via 1D irrep + rank-0 multiplicative action.
- §12.6 ruling out non-multiplicative matrix-action realizations via $M^2 = I$ diagonalization on finite-dimensional vector spaces.
- §12.7 $\gamma^5$ analogy made precise.
- §12.8 Phase 2 ansatz as unique minimal-algebraic-realization TI-odd spatial vector at $v_{\text{host}}$.
- §12.11 self-checkpoint flagged three places §12 could overstate, including the finite-dimensional dependence of §12.6.

### §1.2 What Layer 2 deferred to Layer 3 per Patch 0538 §14.2

Patch 0538 §14.2 narrowed B.2.q1's closure scope to "finite-dimensional realizations of $P_{TI}$ on finite-dimensional operator spaces within standard Wigner-Eckart machinery" in response to cross-reviewer-convergent feedback from ChatGPT and Copilot:

- **ChatGPT's verbatim assessment**: "The representation-theoretic argument works cleanly for: finite-dimensional realizations of $P_{TI}$. But the thermodynamic-arrow sector may naturally invite: history dependence, infinite-dimensional update structure, or nonlocal temporal operators. The document partially acknowledges this but not enough. This does NOT invalidate the theorem. But it means the theorem proves: finite-dimensional minimal algebraic realization uniqueness, not: universal uniqueness."

- **Copilot's verbatim assessment**: "But the CPP substrate operator space is not explicitly shown to be finite-dimensional. You implicitly assume: the operator acts on a finite-dimensional matter-state Hilbert space, the representation of $P_{TI}$ is finite-dimensional. Neither is established in the document."

The Patch 0538 calibration response narrowed the closure scope as a tactical fix; the Layer 3 task is to **make the finite-dimensional scope load-bearing axiomatic commitment** rather than acknowledged-but-unframed qualifier. This Layer 3 promotion:

- States the framework's finite-dimensional matter-state Hilbert space commitment as Axiomatic Commitment AC-1, traceable to Reading C + first-shell-content matter-state construction.
- Identifies the specific load-bearing points in the proof where finite-dimensionality enters (minimal polynomial, eigenspace decomposition, complete reducibility).
- Explicitly identifies the open questions outside AC-1 (infinite-dimensional / history-dependent / nonlocal-temporal realizations) as Layer 4 territory.
- Preserves the Patch 0538 §14.2 scope qualifier verbatim throughout.

### §1.3 What Layer 3 means at sketch-document level

Layer 3 at sketch-document level means: rigorous representation-theoretic statement of the theorem with all framework commitments explicit, complete proof with every step formalized (no hand-waving on "obvious" steps), explicit identification of where each framework commitment is used, and explicit scope-qualifier preservation. The "sketch" qualifier remains because this is not a flagship paper section — the document lives in `layer3_promotion/` as Layer 3 work in progress, not as a finalized flagship paper artifact. Layer 4 would be: derivation of the framework commitments (AC-1 finite-dimensionality, $P_{TI}$ structure from A5 alone, etc.) from CPP axioms A1–A11 + substrate-geometric primitives. Layer 4 is registered as deferred.

---

## §2 Primitives and conventions

### §2.1 CPP framework primitives used

- **A1 (Conscious Points)**: finite per CP; foundation for substrate-physics construction. Used in §4 as the basis for Reading C's matter-state construction.
- **A5.2 (T-asymmetry of cycle direction)**: $T: \sigma_{cycle} \to -\sigma_{cycle}$, $T^2 = 1$.
- **A5.3 (I-evenness of cycle direction)**: $I: \sigma_{cycle} \to +\sigma_{cycle}$, $I^2 = 1$.
- **A5 (framework-symmetry generator commutativity, implicit framework commitment)**: $[T, I] = 0$. This makes $P_{TI} = \langle T, I\rangle$ abelian.
- **Reading C (substrate matter-state construction)**: matter states at $v_{\text{host}}$ built from first-shell content (12 vertices); $\hat{n}$ fixed as framework chirality direction; residual $I_h$ symmetry preserves first-shell content.

### §2.2 Framework parity group $P_{TI}$

**Definition 2.2.1.** The framework parity group is $P_{TI} := \langle T, I \mid T^2 = I^2 = 1, \; TI = IT\rangle$.

By the defining relations, $P_{TI} \cong \mathbb{Z}_2 \times \mathbb{Z}_2$ (Klein four-group), an abelian group of order 4 with elements $\{1, T, I, TI\}$.

**Convention 2.2.2 (irrep labels).** Following Patch 0536 §12.3 conventions, the four 1D irreducible representations of $P_{TI}$ are labeled by their characters $(\rho(T), \rho(I)) \in \{+1, -1\}^2$:

| Label | $\rho(1)$ | $\rho(T)$ | $\rho(I)$ | $\rho(TI)$ | Convention name |
|---|---|---|---|---|---|
| $\mathbf{1}$ | $+1$ | $+1$ | $+1$ | $+1$ | TI-even, T-even, I-even (trivial) |
| $\mathbf{T}$ | $+1$ | $-1$ | $+1$ | $-1$ | T-odd, I-even ("CPP TI-odd"; CPP $\sigma_{cycle}$ irrep) |
| $\mathbf{I}$ | $+1$ | $+1$ | $-1$ | $-1$ | T-even, I-odd (Capotauro $\chi$ irrep, conventional pseudoscalar) |
| $\mathbf{TI}$ | $+1$ | $-1$ | $-1$ | $+1$ | T-odd, I-odd (product of $\sigma_{cycle}$ and $\chi$) |

**Convention 2.2.3 (CPP "TI-odd" terminology disambiguation).** The CPP-internal terminology calls the $\mathbf{T}$ irrep "TI-odd" because $\sigma_{cycle}$ — which lives in this irrep — flips sign under $T$ (the dominant framework parity operation in A5). This is distinct from the conventional pseudoscalar irrep $\mathbf{TI}$ (T-odd AND I-odd). The CPP "TI-odd" terminology is preserved throughout this document for consistency with Patch 0536 §12.

### §2.3 Framework operators and matter-state Hilbert space

**Definition 2.3.1.** The matter-state Hilbert space at $v_{\text{host}}$, denoted $\mathcal{H}_{\text{matter}}^{v_{\text{host}}}$, is the framework-constructed Hilbert space on which substrate-physics operators act. Per Reading C, $\mathcal{H}_{\text{matter}}^{v_{\text{host}}}$ is built from first-shell content at $v_{\text{host}}$ (the 12 first-shell vertices and their substrate-physics degrees of freedom).

**Definition 2.3.2.** A substrate-physics operator at $v_{\text{host}}$ is a linear operator $\mathcal{O}: \mathcal{H}_{\text{matter}}^{v_{\text{host}}} \to \mathcal{H}_{\text{matter}}^{v_{\text{host}}}$ with well-defined $P_{TI}$-transformation properties under the framework's $P_{TI}$-action on $\mathcal{H}_{\text{matter}}^{v_{\text{host}}}$.

### §2.4 The finite-dimensional framework commitment

**Axiomatic Commitment AC-1 (finite-dimensional matter-state Hilbert space).** The matter-state Hilbert space at $v_{\text{host}}$ satisfies $\dim_{\mathbb{C}} \mathcal{H}_{\text{matter}}^{v_{\text{host}}} < \infty$.

**Derivational status of AC-1.** AC-1 is **derived from Reading C + first-shell-content construction**: matter states at $v_{\text{host}}$ are constructed from first-shell substrate content, which is finite (12 vertices, each carrying finitely-many CPP primitive degrees of freedom per A1). The construction is summed over a finite index set, producing a finite-dimensional Hilbert space. Layer 4 derivation of AC-1 from CPP axioms A1–A11 alone (without Reading C as a framework-construction commitment) is deferred.

**Out-of-scope alternatives.** AC-1 does NOT hold for:
- History-dependent matter-state constructions (matter states indexed by sequences of past Absolute Moments rather than instantaneous first-shell content).
- Nonlocal temporal operators (operators acting on substrate content across multiple Absolute Moments).
- Graph-holonomy / coarse-grained transport tensor / delayed-cycle operator structures.

The theorem proved in this document operates entirely within AC-1; alternative constructions outside AC-1 remain logically available as future framework extensions, registered as Layer 4 territory / long-term programme target.

### §2.5 The framework $P_{TI}$-action on $\mathcal{H}_{\text{matter}}^{v_{\text{host}}}$

**Definition 2.5.1.** The framework's $P_{TI}$-action on $\mathcal{H}_{\text{matter}}^{v_{\text{host}}}$ is a representation $\pi: P_{TI} \to GL(\mathcal{H}_{\text{matter}}^{v_{\text{host}}})$ specified by $\pi(T)$ and $\pi(I)$ — linear operators on $\mathcal{H}_{\text{matter}}^{v_{\text{host}}}$ satisfying $\pi(T)^2 = \pi(I)^2 = \mathbb{1}$ and $\pi(T)\pi(I) = \pi(I)\pi(T)$, induced from the framework-symmetry action on first-shell content.

**Convention 2.5.2.** Under AC-1 (finite-dimensional $\mathcal{H}_{\text{matter}}^{v_{\text{host}}}$) and with $\pi(T), \pi(I)$ satisfying these relations, $\pi$ is a finite-dimensional unitary representation of $P_{TI}$ on $\mathcal{H}_{\text{matter}}^{v_{\text{host}}}$.

---

## §3 Rigorous representation theory of $P_{TI}$

### §3.1 Character table and orthogonality

The complete character table of $P_{TI} = \{1, T, I, TI\}$ on its four 1D irreps:

| | $1$ | $T$ | $I$ | $TI$ |
|---|---|---|---|---|
| $\chi_{\mathbf{1}}$ | $+1$ | $+1$ | $+1$ | $+1$ |
| $\chi_{\mathbf{T}}$ | $+1$ | $-1$ | $+1$ | $-1$ |
| $\chi_{\mathbf{I}}$ | $+1$ | $+1$ | $-1$ | $-1$ |
| $\chi_{\mathbf{TI}}$ | $+1$ | $-1$ | $-1$ | $+1$ |

**Character orthogonality relations (rows):**

$$\frac{1}{|P_{TI}|}\sum_{g \in P_{TI}} \chi_\rho(g)^* \chi_\sigma(g) = \delta_{\rho\sigma}$$

Direct verification on the character table: each row has $|P_{TI}| = 4$ entries of $\pm 1$, and inner products between distinct rows vanish (each $\pm 1$ pairing produces an equal number of $+$ and $-$ contributions summing to zero).

**Column orthogonality (irreps complete):**

$$\sum_\rho \chi_\rho(g)^* \chi_\rho(g') = |P_{TI}| \cdot \delta_{[g],[g']}$$

For $P_{TI}$ abelian, conjugacy classes are singletons so $[g] = \{g\}$, and column orthogonality reduces to checking distinct group elements give orthogonal columns. Direct verification on the character table confirms this. The four 1D irreps $\{\mathbf{1}, \mathbf{T}, \mathbf{I}, \mathbf{TI}\}$ are therefore a COMPLETE set of irreducible representations of $P_{TI}$.

### §3.2 Complete reducibility (Maschke's theorem)

**Theorem 3.2.1 (Maschke for $P_{TI}$).** Every finite-dimensional complex representation $\pi: P_{TI} \to GL(V)$ of $P_{TI}$ on a finite-dimensional vector space $V$ is completely reducible: $V$ decomposes as a direct sum of $P_{TI}$-irreducible subrepresentations,

$$V = V_\mathbf{1} \oplus V_\mathbf{T} \oplus V_\mathbf{I} \oplus V_\mathbf{TI}$$

where each $V_\rho$ is the $\rho$-isotypic component (sum of all subrepresentations isomorphic to $\rho$).

**Proof.** Maschke's theorem applies to any finite group representation over a field of characteristic zero (here $\mathbb{C}$); $P_{TI}$ is a finite group of order 4 and $\text{char}(\mathbb{C}) = 0$. For abelian groups all irreps are 1D, so the isotypic decomposition is into 1D irrep components.

Explicit construction of the projectors: the projector onto the $\rho$-isotypic component is

$$P_\rho = \frac{1}{|P_{TI}|}\sum_{g \in P_{TI}} \chi_\rho(g)^* \pi(g) = \frac{1}{4}\sum_{g \in P_{TI}} \chi_\rho(g)^* \pi(g).$$

For $P_{TI} = \{1, T, I, TI\}$:

- $P_\mathbf{1} = \frac{1}{4}[\mathbb{1} + \pi(T) + \pi(I) + \pi(TI)]$ — projector onto $\rho(T) = \rho(I) = +1$ subspace.
- $P_\mathbf{T} = \frac{1}{4}[\mathbb{1} - \pi(T) + \pi(I) - \pi(TI)]$ — projector onto $\rho(T) = -1, \rho(I) = +1$ (CPP "TI-odd", $\sigma_{cycle}$ irrep).
- $P_\mathbf{I} = \frac{1}{4}[\mathbb{1} + \pi(T) - \pi(I) - \pi(TI)]$ — projector onto $\rho(T) = +1, \rho(I) = -1$ (Capotauro $\chi$ irrep).
- $P_\mathbf{TI} = \frac{1}{4}[\mathbb{1} - \pi(T) - \pi(I) + \pi(TI)]$ — projector onto $\rho(T) = -1, \rho(I) = -1$ (conventional pseudoscalar).

Verification: $\sum_\rho P_\rho = \mathbb{1}$, $P_\rho P_\sigma = \delta_{\rho\sigma} P_\rho$, $P_\rho^\dagger = P_\rho$ (under unitary $\pi$). Therefore $V = \bigoplus_\rho V_\rho$ with $V_\rho := P_\rho V$. $\square$

**Remark 3.2.2 (where finite-dimensionality enters).** Maschke's theorem as stated above requires $V$ to be finite-dimensional OR the representation to be unitary; under AC-1 + framework unitarity convention (2.5.2), both are satisfied. The projector construction does NOT rely on finite-dimensionality directly (the sums over $P_{TI}$ are finite since $|P_{TI}| = 4 < \infty$), but the diagonalizability of operators on $V$ — used implicitly in writing $V = \bigoplus V_\rho$ as a direct sum — does require finite-dimensionality OR a Hilbert-space spectral theorem. Under AC-1 this is automatic; relaxing AC-1 requires the spectral theorem on Hilbert spaces (which holds for unitary operators on separable complex Hilbert spaces but introduces spectral integrals rather than direct sums for continuous spectrum cases).

### §3.3 Tensor product structure

**Lemma 3.3.1.** Tensor products of 1D irreps of $P_{TI}$ are 1D irreps with characters given by pointwise multiplication of factor characters.

**Proof.** For 1D irreps $\rho, \sigma$ with characters $\chi_\rho, \chi_\sigma$, the tensor product representation $\rho \otimes \sigma$ acts on $\mathbb{C} \otimes \mathbb{C} \cong \mathbb{C}$ by $(\rho \otimes \sigma)(g) v = \chi_\rho(g)\chi_\sigma(g) v$. The character of $\rho \otimes \sigma$ is therefore $\chi_{\rho \otimes \sigma}(g) = \chi_\rho(g)\chi_\sigma(g)$, which matches one of the four characters in the table. $\square$

**Tensor product multiplication table:**

| $\otimes$ | $\mathbf{1}$ | $\mathbf{T}$ | $\mathbf{I}$ | $\mathbf{TI}$ |
|---|---|---|---|---|
| $\mathbf{1}$ | $\mathbf{1}$ | $\mathbf{T}$ | $\mathbf{I}$ | $\mathbf{TI}$ |
| $\mathbf{T}$ | $\mathbf{T}$ | $\mathbf{1}$ | $\mathbf{TI}$ | $\mathbf{I}$ |
| $\mathbf{I}$ | $\mathbf{I}$ | $\mathbf{TI}$ | $\mathbf{1}$ | $\mathbf{T}$ |
| $\mathbf{TI}$ | $\mathbf{TI}$ | $\mathbf{I}$ | $\mathbf{T}$ | $\mathbf{1}$ |

The table verifies $P_{TI}$'s irrep ring is the group ring of $\mathbb{Z}_2 \times \mathbb{Z}_2$ itself — each irrep is self-inverse ($\rho \otimes \rho = \mathbb{1}$), and the irreps form a group isomorphic to $P_{TI}$.

**Cross-reference:** $\chi_\mathbf{T} \otimes \chi_\mathbf{I} = \chi_\mathbf{TI}$ confirms Patch 0536 §12.3's key rep-theoretic fact: $\sigma_{cycle} \cdot \chi$ transforms in the conventional pseudoscalar irrep (T-odd AND I-odd).

### §3.4 Real-vs-complex structure (Frobenius-Schur indicators)

For $P_{TI}$ abelian, the four 1D irreps over $\mathbb{C}$ have characters in $\{+1, -1\} \subset \mathbb{R}$. Each irrep therefore has Frobenius-Schur indicator $+1$ (real type), meaning the complex irrep descends to a real irrep without modification. The character orthogonality relations and Maschke's theorem hold identically over $\mathbb{R}$ for these irreps, with the same projector formulas.

**Consequence:** the representation theory of $P_{TI}$ used throughout this document is identical over $\mathbb{R}$ and $\mathbb{C}$. No quaternionic-type modifications, no complex-conjugate-pair-of-real-irreps complications. (Contrast: the icosahedral group $I_h$ used in B.1.q4 Layer 3 also has Frobenius-Schur indicator $+1$ on its 3D vector irrep, but $I_h$ has higher-dimensional irreps where the real-vs-complex distinction would matter.)

---

## §4 Statement of the Minimal Algebraic Realization Theorem at Layer 3

**Theorem 4.0 (Minimal Algebraic Realization, B.2.q1 Layer 3).**

Let $\mathcal{F}$ be a CPP framework satisfying:

- **A5.2 + A5.3 + A5-commutativity** giving framework parity group $P_{TI} = \langle T, I \mid T^2 = I^2 = 1, [T,I] = 1\rangle \cong \mathbb{Z}_2 \times \mathbb{Z}_2$.
- **A5-binarity** giving framework primitive $\sigma_{cycle}$ with $\sigma_{cycle}^2 = 1$ identically.
- **$P_{TI}$-covariance of $\sigma_{cycle}$**: $\sigma_{cycle}$ transforms as the $\mathbf{T}$ 1D irrep of $P_{TI}$ (T-odd, I-even).
- **AC-1**: matter-state Hilbert space $\mathcal{H}_{\text{matter}}^{v_{\text{host}}}$ at $v_{\text{host}}$ is finite-dimensional.

Let $\mathcal{O}: \mathcal{H}_{\text{matter}}^{v_{\text{host}}} \to \mathcal{H}_{\text{matter}}^{v_{\text{host}}}$ be a substrate-physics operator depending on the A5-cyclicity content $\sigma_{cycle}$. Then:

**(I) Polynomial form.** $\mathcal{O}$ admits a unique decomposition

$$\mathcal{O} = a\,\mathcal{O}_+ + b\,\sigma_{cycle}\,\mathcal{O}_-,$$

where $\mathcal{O}_+$ and $\mathcal{O}_-$ are linear operators on $\mathcal{H}_{\text{matter}}^{v_{\text{host}}}$ independent of $\sigma_{cycle}$, and $a, b \in \mathbb{C}$ (or $\mathbb{R}$, by §3.4).

**(II) Irreducible-component identification.** Under the $P_{TI}$-action,

$$\mathcal{O} = P_\mathbf{1}\mathcal{O} + P_\mathbf{T}\mathcal{O} + P_\mathbf{I}\mathcal{O} + P_\mathbf{TI}\mathcal{O}$$

is the unique $P_{TI}$-isotypic decomposition (per Theorem 3.2.1), where each $P_\rho \mathcal{O}$ is the $\rho$-irreducible component of $\mathcal{O}$.

**(III) TI-odd restriction.** If $\mathcal{O}$ is required to transform in the $\mathbf{T}$ (CPP TI-odd, T-odd, I-even) irrep, then necessarily

$$\mathcal{O} = b\,\sigma_{cycle}\,\mathcal{O}_-, \quad \text{where}\quad \mathcal{O}_-\;\text{is}\;P_{TI}\text{-trivial (i.e., }\mathcal{O}_- \in V_\mathbf{1}\text{)}.$$

**(IV) Minimality and uniqueness.** The multiplicative TI-odd realization $\mathcal{O} = b\,\sigma_{cycle}\,\mathcal{O}_-$ is the **unique minimal algebraic realization** of A5-cyclicity in the TI-odd channel: it uses the lowest-rank tensor operation (rank-0 multiplicative) on the lowest-dimensional non-trivial irrep (1D, since $P_{TI}$ is abelian). Any alternative realization of $\sigma_{cycle}$'s TI-odd content in $\mathcal{O}$ either coincides with this form (up to scalar multiple) or requires a higher-dimensional $P_{TI}$-irrep, which does not exist for the abelian group $P_{TI}$.

---

## §5 Proof of the Minimal Algebraic Realization Theorem

The proof is structured as four steps, each identifying the framework commitments (A5 commitments + AC-1) used.

### §5.1 Step 1 — Polynomial reduction modulo $\sigma_{cycle}^2 - 1$

**Claim.** Any operator polynomial $p(\sigma_{cycle})$ in $\sigma_{cycle}$ reduces uniquely to an affine polynomial $a + b\sigma_{cycle}$ when $\sigma_{cycle}^2 = 1$.

**Proof.** By polynomial division in $\mathbb{C}[x]$ (or $\mathbb{R}[x]$): $p(x) = q(x)(x^2 - 1) + r(x)$ with $\deg(r) \leq 1$, so $r(x) = a + bx$. Substituting $x = \sigma_{cycle}$ and using $\sigma_{cycle}^2 = 1$ (the A5-binarity commitment) gives $p(\sigma_{cycle}) = a + b\sigma_{cycle}$. Uniqueness: if $a + b\sigma_{cycle} = a' + b'\sigma_{cycle}$ as operators on a space where $\sigma_{cycle}$'s action is non-trivial (i.e., $\sigma_{cycle}$ does NOT act as $\pm\mathbb{1}$ on the whole space), then $(a - a')\mathbb{1} + (b - b')\sigma_{cycle} = 0$. Acting on a $\sigma_{cycle}$-eigenvector $v_\pm$ with $\sigma_{cycle} v_\pm = \pm v_\pm$ gives $(a - a') \pm (b - b') = 0$ for both signs, hence $a = a'$ and $b = b'$.

If $\sigma_{cycle}$ acts as $+\mathbb{1}$ on the whole space (degenerate case), $a + b\sigma_{cycle} = (a + b)\mathbb{1}$ and the decomposition is non-unique; but this is the trivial case where the framework's TI-odd content is identically zero on $\mathcal{H}_{\text{matter}}^{v_{\text{host}}}$. Under the framework's commitment that $\sigma_{cycle}$ is a non-trivial framework primitive (per A5), this case is excluded.

**Where AC-1 enters:** Step 1 does NOT require AC-1 directly — the polynomial reduction is purely algebraic. However, the uniqueness argument uses the existence of $\sigma_{cycle}$-eigenvectors, which under AC-1 + Maschke is automatic via §3.2. Without AC-1, eigenvector existence requires the spectral theorem for unitary operators on Hilbert space.

### §5.2 Step 2 — $P_{TI}$-irreducible decomposition

**Claim.** The unique decomposition $\mathcal{O} = a\,\mathcal{O}_+ + b\,\sigma_{cycle}\,\mathcal{O}_-$ from Step 1 coincides with the $P_{TI}$-isotypic decomposition under appropriate identification of components.

**Proof.** Applying the projectors from §3.2:

$$P_\mathbf{1}\mathcal{O} = \frac{1}{4}[\mathcal{O} + \pi(T)\mathcal{O}\pi(T)^{-1} + \pi(I)\mathcal{O}\pi(I)^{-1} + \pi(TI)\mathcal{O}\pi(TI)^{-1}]$$

For $\mathcal{O} = a + b\sigma_{cycle}$ (treating $a, b$ as scalars and $\mathcal{O}_+ = \mathcal{O}_- = \mathbb{1}$ for clarity, and noting $\pi(T)\sigma_{cycle}\pi(T)^{-1} = -\sigma_{cycle}$ by A5.2, $\pi(I)\sigma_{cycle}\pi(I)^{-1} = +\sigma_{cycle}$ by A5.3):

$$P_\mathbf{1}(a + b\sigma_{cycle}) = \frac{1}{4}[(a + b\sigma_{cycle}) + (a - b\sigma_{cycle}) + (a + b\sigma_{cycle}) + (a - b\sigma_{cycle})] = a$$

$$P_\mathbf{T}(a + b\sigma_{cycle}) = \frac{1}{4}[(a + b\sigma_{cycle}) - (a - b\sigma_{cycle}) + (a + b\sigma_{cycle}) - (a - b\sigma_{cycle})] = b\sigma_{cycle}$$

$$P_\mathbf{I}(a + b\sigma_{cycle}) = \frac{1}{4}[(a + b\sigma_{cycle}) + (a - b\sigma_{cycle}) - (a + b\sigma_{cycle}) - (a - b\sigma_{cycle})] = 0$$

$$P_\mathbf{TI}(a + b\sigma_{cycle}) = \frac{1}{4}[(a + b\sigma_{cycle}) - (a - b\sigma_{cycle}) - (a + b\sigma_{cycle}) + (a - b\sigma_{cycle})] = 0$$

So for scalar operators ($\mathcal{O}_\pm = \mathbb{1}$): $a$ is in the $\mathbf{1}$ irrep, $b\sigma_{cycle}$ is in the $\mathbf{T}$ irrep, and the $\mathbf{I}$ and $\mathbf{TI}$ components vanish.

For general operators with $\mathcal{O}_+, \mathcal{O}_-$ non-trivial, the decomposition generalizes: $\mathcal{O}_+$ and $\mathcal{O}_-$ carry their own $P_{TI}$-transformation properties, and the full $P_{TI}$-isotypic decomposition of $\mathcal{O}$ is a tensor product of $\{a, b\sigma_{cycle}\}$ structure (in §3.3's tensor table) with $\{\mathcal{O}_+, \mathcal{O}_-\}$'s $P_{TI}$-types.

**Where AC-1 enters:** Step 2 uses Maschke's theorem (§3.2) to write $\mathcal{O}$ as a sum of $P_{TI}$-isotypic components. Maschke's theorem in §3.2 was stated for finite-dimensional representations; under AC-1 this is automatic. Without AC-1, the isotypic decomposition requires a Hilbert-space variant of Maschke.

### §5.3 Step 3 — TI-odd restriction forces $a = 0$ and $\mathcal{O}_-$ trivial

**Claim.** If $\mathcal{O}$ is required to transform in the $\mathbf{T}$ irrep (T-odd, I-even, CPP "TI-odd"), then in the decomposition $\mathcal{O} = a\,\mathcal{O}_+ + b\,\sigma_{cycle}\,\mathcal{O}_-$ we must have $a\mathcal{O}_+ \in V_{\not= \mathbf{T}}$ (orthogonal to $\mathbf{T}$) and $\mathcal{O}_-$ is $P_{TI}$-trivial.

**Proof.** The $\mathbf{T}$-isotypic component of $\mathcal{O}$ is $P_\mathbf{T}\mathcal{O}$. For $\mathcal{O}$ to transform purely in $\mathbf{T}$ (i.e., $\mathcal{O} \in V_\mathbf{T}$), we need $P_\mathbf{T}\mathcal{O} = \mathcal{O}$ and $P_\rho\mathcal{O} = 0$ for $\rho \neq \mathbf{T}$.

The constant term $a\mathcal{O}_+$: if $\mathcal{O}_+$ transforms in irrep $\rho_+$, then $a\mathcal{O}_+ \in V_{\rho_+}$. By tensor structure (§3.3), $\sigma_{cycle}\cdot\mathcal{O}_- \in V_{\mathbf{T} \otimes \rho_-}$ where $\rho_-$ is $\mathcal{O}_-$'s irrep.

For $\mathcal{O} = a\mathcal{O}_+ + b\sigma_{cycle}\mathcal{O}_-$ to be in $V_\mathbf{T}$, we need:

- $\rho_+ = \mathbf{T}$ and $a\mathcal{O}_+$ part already in $V_\mathbf{T}$: then $\mathcal{O}_+ \in V_\mathbf{T}$ is itself a multiple of $\sigma_{cycle}$ (since $\sigma_{cycle}$ spans $V_\mathbf{T}$ in the $\sigma_{cycle}$-multiplicative sense). So $\mathcal{O}_+ = c\sigma_{cycle}$ for some constant $c$, and $a\mathcal{O}_+ = ac\sigma_{cycle}$. This is now absorbed into the $b\sigma_{cycle}\mathcal{O}_-$ form via $b' = ac + b$ and $\mathcal{O}_-$ updated accordingly. So we can WLOG take $\rho_+ = \mathbf{1}$ (trivial) and $a\mathcal{O}_+$ part is in $V_\mathbf{1}$.
- With $\rho_+ = \mathbf{1}$: $a\mathcal{O}_+ \in V_\mathbf{1}$, which is orthogonal to $V_\mathbf{T}$. For $\mathcal{O} \in V_\mathbf{T}$, we need this $V_\mathbf{1}$ component to vanish: $a = 0$.
- Then $\mathcal{O} = b\sigma_{cycle}\mathcal{O}_-$, with $\mathcal{O} \in V_\mathbf{T}$ requiring $\mathbf{T} \otimes \rho_- = \mathbf{T}$, hence $\rho_- = \mathbf{1}$ (trivial). $\mathcal{O}_-$ is therefore $P_{TI}$-trivial.

$\square$

**Where AC-1 enters:** Step 3 uses the orthogonality of distinct isotypic components ($V_\mathbf{1} \perp V_\mathbf{T}$ etc.), which is a consequence of Maschke + character orthogonality (§3.1, §3.2) under AC-1.

### §5.4 Step 4 — Minimality

**Claim.** The realization $\mathcal{O} = b\sigma_{cycle}\mathcal{O}_-$ from Step 3 is the unique minimal algebraic realization in the following precise sense:

(a) **Lowest-rank tensor operation:** the multiplicative product $\sigma_{cycle}\cdot\mathcal{O}_-$ is a rank-$0 \times$ rank-$n$ tensor product where $n = \text{rank}(\mathcal{O}_-)$. No lower-rank operation exists for a non-trivial product structure.

(b) **Lowest-dimensional irrep:** $\sigma_{cycle}$ generates the 1D $\mathbf{T}$-irrep. Since $P_{TI}$ is abelian, all its irreps are 1D (§3.1 character table); there is no lower-dimensional non-trivial irrep available.

(c) **Uniqueness up to scalar:** within the 1D $\mathbf{T}$-irrep, any other $\mathbf{T}$-transforming framework primitive is a scalar multiple of $\sigma_{cycle}$ (Schur's lemma on 1D irrep). The framework's choice of $\sigma_{cycle}$ as the primitive sets the scale; any other choice would give a scalar-multiple realization.

**Proof of (a)–(c).** All three are immediate from the rep theory:

- (a) is a definitional property of tensor products: rank-0 (scalar) times rank-$n$ is the lowest-rank possible non-trivial product.
- (b) follows from $P_{TI}$ being abelian + character theory of abelian groups (irreps of abelian groups are all 1D over $\mathbb{C}$, since by Schur's lemma irreducible commuting matrices on a finite-dimensional space are scalar multiples of identity, and an abelian group has all its elements mutually commuting).
- (c) follows from Schur's lemma applied to the 1D $\mathbf{T}$ irrep: any operator commuting with all $\pi(g)$ for $g \in P_{TI}$ on a 1D irrep is a scalar multiple of identity, hence any element of $V_\mathbf{T}$ is a scalar multiple of any fixed non-zero element.

**Where AC-1 enters:** Step 4 uses Schur's lemma (part (c)) and the finite-group character theory (part (b)). Schur's lemma applies on finite-dimensional irreps; under AC-1 this is automatic. The character-theory argument that abelian-finite-group irreps are 1D over $\mathbb{C}$ also holds in infinite-dimensional settings via the Gelfand-Naimark theorem for abelian C*-algebras, but the simpler finite-dimensional argument suffices here.

### §5.5 Conclusion of proof

Combining Steps 1–4: any substrate-physics operator $\mathcal{O}$ on the finite-dimensional matter-state Hilbert space $\mathcal{H}_{\text{matter}}^{v_{\text{host}}}$ (under AC-1) with TI-odd transformation under $P_{TI}$ admits the unique decomposition $\mathcal{O} = b\,\sigma_{cycle}\,\mathcal{O}_-$ with $\mathcal{O}_-$ $P_{TI}$-trivial. The multiplicative TI-odd pseudoscalar realization is the unique minimal algebraic realization, with minimality in (a) rank, (b) irrep dimension, and (c) up-to-scalar uniqueness. $\square$

---

## §6 Ruling out non-multiplicative matrix realizations under AC-1

The Patch 0536 §12.6 argument that "non-multiplicative matrix-action realizations reduce to multiplicative pseudoscalar action" is restated rigorously at Layer 3.

**Theorem 6.1.** Let $V$ be a finite-dimensional complex vector space (under AC-1) and $M: V \to V$ a linear operator satisfying $M^2 = \mathbb{1}_V$. Then $M$ is diagonalizable with eigenvalues in $\{+1, -1\}$, and $V$ decomposes as $V = V_+ \oplus V_-$ where $M|_{V_+} = +\mathbb{1}$ and $M|_{V_-} = -\mathbb{1}$.

**Proof.** The minimal polynomial of $M$ divides $x^2 - 1 = (x-1)(x+1)$, which has distinct roots in $\mathbb{C}$. By the standard result that linear operators with separable minimal polynomial are diagonalizable, $M$ is diagonalizable. The eigenvalues are roots of $x^2 - 1$, hence $\pm 1$. The eigenspaces $V_+, V_-$ for eigenvalues $\pm 1$ direct-sum to $V$ since the minimal polynomial splits. $\square$

**Where AC-1 enters (load-bearing):** the diagonalizability claim relies on the finite-dimensionality of $V$. In infinite-dimensional settings, $M^2 = \mathbb{1}$ does NOT automatically imply diagonalizability — the operator can have continuous spectrum or fail to be diagonalizable without the spectral theorem on Hilbert spaces. Under AC-1, diagonalizability is immediate from the minimal polynomial argument.

**Corollary 6.2 (non-multiplicative-reduces-to-multiplicative).** Any matrix-action realization of $\sigma_{cycle}$ on a finite-dimensional vector space $V$ (under AC-1) is unitarily equivalent to a multiplicative realization on the eigenspace decomposition $V = V_+ \oplus V_-$, with $\sigma_{cycle}$ acting as $\pm \mathbb{1}$ on each component.

**Proof.** Apply Theorem 6.1 with $M = \pi_V(\sigma_{cycle})$ (the action of $\sigma_{cycle}$ on $V$). The eigenspace decomposition gives the multiplicative action. $\square$

**Conclusion.** The multiplicative pseudoscalar realization is not just minimal among alternatives — it is the **essential** realization under AC-1, since the only "alternative" realizations (non-multiplicative matrix actions) reduce to multiplicative form via the eigenspace decomposition. There are no genuinely-distinct algebraic realizations of $\sigma_{cycle}$'s $\mathbb{Z}_2$ structure at the rep-theoretic level within the AC-1 framework.

---

## §7 Cross-reference: Capotauro v2.0 spatial-sector parallel

The minimal algebraic realization theorem applies UNIFORMLY to both CPP $\sigma_{cycle}$ (T-odd-I-even, $\mathbf{T}$ irrep) and Capotauro chirality $\chi$ (T-even-I-odd, $\mathbf{I}$ irrep) — the same theorem with different choice of irrep.

**Capotauro v2.0 spatial-sector statement (mirror of Theorem 4.0 with $\mathbf{T} \to \mathbf{I}$):**

Let $\chi$ be the Capotauro chirality primitive with $\chi^2 = 1$, transforming in the $\mathbf{I}$ irrep of $P_{TI}$ (T-even, I-odd). Then any substrate-physics operator $\mathcal{O}$ on $\mathcal{H}_{\text{matter}}^{v_{\text{host}}}$ (under AC-1) with I-odd-T-even transformation under $P_{TI}$ admits the unique decomposition $\mathcal{O} = b\,\chi\,\mathcal{O}_-$ with $\mathcal{O}_-$ $P_{TI}$-trivial.

The proof is identical to §5 with $\mathbf{T} \to \mathbf{I}$ swap throughout.

**Programme structural payoff.** Both CPP $\sigma_{cycle}$ and Capotauro $\chi$ realize $\mathbb{Z}_2$ chirality content as rank-0 multiplicative scalars in 1D parity irreps. The Substrate-Locality Unification (B.3.Move-1, Patch 0534 §10.7) provides the geometric foundation: both sectors operate on the same first-shell geometric structure via substrate-locality theorems. §7's rep-theoretic parallel provides the algebraic foundation: both chirality contents are minimally realized as multiplicative pseudoscalars in the same parity group $P_{TI}$'s rep theory. Together they provide the structural foundation for Case A.1 $\delta = \chi$ identification (Patch 0526 §13).

**Dirac $\gamma^5$ analogy (§12.7 mirror).** The Dirac $\gamma^5$ chirality structure is the conventional I-odd-T-even realization — same irrep as Capotauro $\chi$. The CPP-internal "TI-odd" terminology (per Convention 2.2.3) puts $\sigma_{cycle}$ in the T-odd-I-even irrep, which is structurally distinct from but rep-theoretically parallel to the conventional I-odd-T-even $\gamma^5$ / Capotauro $\chi$ irrep. The minimal algebraic realization theorem applies uniformly across all three (Dirac $\gamma^5$, Capotauro $\chi$, CPP $\sigma_{cycle}$) — rank-0 multiplicative scalar in a 1D parity irrep — with the choice of irrep depending on physics.

---

## §8 Extension to infinite-dimensional realizations — formal scope of the theorem

AC-1 (finite-dimensionality of $\mathcal{H}_{\text{matter}}^{v_{\text{host}}}$) is load-bearing at three points in the proof:

### §8.1 Where AC-1 is used

1. **§5.1 Step 1 (polynomial reduction):** uniqueness of the $a + b\sigma_{cycle}$ decomposition relies on existence of $\sigma_{cycle}$-eigenvectors, which under AC-1 + Maschke is automatic. Without AC-1, this requires the spectral theorem on Hilbert space.

2. **§5.2 Step 2 + §3.2 (Maschke's theorem):** finite-dimensionality + finite group representation gives complete reducibility via the projector formulas. In infinite-dimensional settings, Maschke's theorem holds for unitary representations of finite groups on Hilbert spaces, with isotypic decomposition into closed subspaces; this is a non-trivial extension but available.

3. **§6 Theorem 6.1 (diagonalizability of $M^2 = \mathbb{1}$):** the minimal polynomial argument relies on finite-dimensionality. In infinite-dimensional settings, $M^2 = \mathbb{1}$ with $M$ bounded on a Hilbert space gives spectral measure $\mu$ supported in $\{+1, -1\}$ via the spectral theorem; the eigenspace decomposition becomes a direct integral, with multiplicative action on the spectral decomposition.

### §8.2 What breaks for infinite-dimensional realizations

The theorem's CONCLUSION (multiplicative pseudoscalar realization on eigenspace decomposition) extends to bounded $M^2 = \mathbb{1}$ on separable Hilbert space via the spectral theorem, BUT:

- **Discrete eigenvalues become spectral decomposition:** the eigenspace decomposition $V = V_+ \oplus V_-$ becomes a direct integral over spectral measure supported on $\{\pm 1\}$. The conclusion "multiplicative action on eigenspaces" still holds in the spectral-theorem sense.
- **History-dependent operators:** if $\sigma_{cycle}$ is realized as a history-dependent operator (acting on sequences of past states rather than instantaneous states), the framework's matter-state space itself becomes infinite-dimensional, and the AC-1 commitment is violated. The theorem does not speak to this case — the framework's commitment to Reading C + first-shell-content + AC-1 excludes history-dependent realizations as a framework-construction choice.
- **Nonlocal temporal operators:** similar — operators acting across multiple Absolute Moments would require an enlarged matter-state space, violating AC-1.

### §8.3 What would be needed for full extension

A Layer 4 extension of the theorem to infinite-dimensional realizations would require:

- Replacing AC-1 with a weaker commitment (e.g., separable Hilbert space + bounded $P_{TI}$-action).
- Replacing finite-dimensional Maschke with the unitary representation theory of finite groups on Hilbert spaces (available via the standard machinery of induced representations and spectral theorems).
- Replacing minimal-polynomial diagonalization with spectral-theorem decomposition for $M^2 = \mathbb{1}$ on Hilbert space.
- Identifying which framework-construction choices (Reading C, first-shell-content matter-state construction) would survive under enlarged matter-state spaces.

This is a substantive extension requiring its own programme-level work; it is Layer 4 territory and is NOT engaged at this Patch.

### §8.4 Connection to the long-term programme target

The chirality-scale-from-polytope-geometry long-term programme target may eventually require engagement with infinite-dimensional or history-dependent realizations of $\sigma_{cycle}$ (e.g., if the polytope-geometric derivation of chirality scale introduces nonlocal temporal structures). The §4–§5 Layer 3 theorem provides the finite-dimensional anchor; the Layer 4 extension would generalize to the framework's full operational scope.

The Layer 3 theorem's finite-dimensional scope does NOT pre-empt this engagement — it provides the rigorous finite-dimensional anchor that any future extension must reduce to in the finite-dimensional limit. This is the standard pattern in physics framework extensions: prove the finite case rigorously, then identify which structural elements survive into the full case.

### §8.5 Patch 0538 §14.2 calibration item — substantively resolved

Patch 0538 §14.2 narrowed B.2.q1's closure scope to "finite-dimensional realizations of $P_{TI}$ on finite-dimensional operator spaces within standard Wigner-Eckart machinery". This Layer 3 promotion **makes that scope load-bearing axiomatic commitment AC-1** rather than ad-hoc qualifier:

- AC-1 is stated as a derived consequence of Reading C + first-shell-content matter-state construction.
- The proof identifies the three load-bearing points where AC-1 is used (§5.1 Step 1, §5.2 Step 2 + §3.2, §6 Theorem 6.1).
- Extension to non-AC-1 settings is explicitly identified as Layer 4 territory with the technical machinery required spelled out.

The cross-reviewer-convergent ChatGPT + Copilot calibration concern is substantively addressed at sketch-document Layer 3: the theorem's finite-dimensional scope is now load-bearing axiomatic commitment, not ad-hoc acknowledgment.

---

## §9 Connection to Phase 2 ansatz and §13 B.1.q1 work

### §9.1 Phase 2 ansatz uniqueness (Patch 0536 §12.8 mirror)

Under the Layer 3 Theorem 4.0 + AC-1, the Phase 2 ansatz

$$\vec{\omega}_{PCD}(v_{\text{host}}) = \sigma_{cycle}\cdot\hat{j}_{DI}^{net}(v_{\text{host}})/|\hat{j}|_0$$

is the unique minimal-algebraic-realization TI-odd spatial vector at $v_{\text{host}}$ constructible from A5-cyclicity content + substrate currents, with:

- $\sigma_{cycle}$ in $\mathbf{T}$ irrep (T-odd, I-even, the unique 1D realization of A5's TI-odd content under AC-1).
- $\hat{j}_{DI}^{net}(v_{\text{host}})$ in the trivial $P_{TI}$ irrep $\mathbf{1}$ (TI-even spatial vector — geometric).
- Tensor product $\mathbf{T} \otimes \mathbf{1} = \mathbf{T}$ — the construction transforms TI-oddly as required.

Higher-derivative-order alternatives (B.2.q2/B.2.q3 territory) remain available outside the rank-0 multiplicative scope; under AC-1 they are constructible but receive separate treatment. The Layer 3 theorem here does NOT close B.2.q2/B.2.q3 — those are independent Layer 3 targets.

### §9.2 Cross-target dependency: Target 2 → Target 3 (Priority 1 chain)

Per Patch 0540 scoping document §3 + §4.1, Target 3 (B.1.q1 matter-state independent derivation Layer 3) depends on Target 2 (this Patch) because B.1.q1's matter-state $I_h$-covariance Layer 3 derivation benefits from B.2.q1's framework axiomatization of $P_{TI}$ rep theory done first. The dependency operates at the framework-axiomatization level:

- Target 2 (this Patch) axiomatizes the $P_{TI}$ rep theory on AC-1 finite-dimensional matter-state Hilbert space. This is the algebraic framework foundation.
- Target 3 (next Patch in chain) will use AC-1 + this Patch's rep-theoretic machinery to derive matter-state $I_h$-covariance INDEPENDENTLY rather than by inheritance from Reading C framework homogeneity (per Patch 0538 §14.1).

The chain Target 2 → Target 3 closes the two strongest cross-reviewer-convergent calibration items (§14.1 + §14.2) in coupled fashion. This Patch (Target 2) provides the foundation; Target 3 builds the matter-state-irrep-enumeration + Schur-orthogonality CG factor on top of it.

### §9.3 What Target 3 will do (preview, not committed at this Patch)

Target 3 will (per Patch 0540 scoping document §2.3):

- Enumerate the matter-state $I_h$-irreps via explicit decomposition of the 12-vertex first-shell permutation representation under $I_h$.
- Compute Schur-orthogonality CG factor for matter-state-substrate-operator coupling.
- Derive matter-state $I_h$-covariance INDEPENDENTLY from Reading C framework homogeneity (i.e., from the explicit irrep enumeration, not as inheritance).

This depends on Target 2's $P_{TI}$ framework axiomatization (this Patch) for the algebraic foundation. Each is its own gated trajectory per §15.7; Target 3 will require Thomas's authorization at the Patch 0543+ boundary.

---

## §10 Connection to Layer 2 work

### §10.1 Patch 0536 §12 immutable record

Patch 0536 §12 (the Layer 2 sketch closure of B.2.q1) is preserved as immutable historical record per §17.8 of `templates/operating_system.md`. The Layer 3 document here is an ADDITIVE artifact in `layer3_promotion/`, not an inline edit to §12.

### §10.2 Patch 0538 §14.2 calibration substantively resolved

The Patch 0538 §14.2 calibration concern (finite-dimensional scope acknowledgment) is **substantively resolved** at sketch-document Layer 3 here: the finite-dimensional scope is now load-bearing axiomatic commitment AC-1 (§2.4), not ad-hoc qualifier. The proof identifies where AC-1 is used (§8.1), and extension to non-AC-1 settings is registered as Layer 4 territory (§8.3). The cross-reviewer-convergent ChatGPT + Copilot concern is addressed via formalization rather than qualifier-tagging.

### §10.3 What this Layer 3 promotion does NOT promote

- Does NOT promote $\sigma_{cycle}$'s rank-0 multiplicative form to programme-level Findings registry (intermediate rep-theoretic result, anti-priority sustained per §9.12 of Patch 0533 mirror).
- Does NOT trigger F.1 sub-question status change (sustained at Patch 0539 framing per §0.1 anti-priority 3).
- Does NOT trigger flagship paper assembly (Layer 3 promotion arc not yet complete; reviewer-pause cycle precondition not satisfied).
- Does NOT promote B.2.q1 to higher-than-sketch-Layer-3 status (Layer 4 framework axiomatization derivation from CPP axioms A1–A11 alone is deferred).

---

## §11 Layer 3 vs Layer 4 distinction

### §11.1 What Layer 3 establishes (this Patch)

- Rigorous representation theory of $P_{TI} = \mathbb{Z}_2 \times \mathbb{Z}_2$ on finite-dimensional matter-state Hilbert spaces under AC-1.
- Minimal Algebraic Realization Theorem (Theorem 4.0) proved rigorously under AC-1.
- Non-multiplicative-matrix-action ruling-out (Theorem 6.1, Corollary 6.2) under AC-1.
- Identification of where AC-1 is load-bearing in the proof (§8.1).
- Cross-reference parallel to Capotauro v2.0 chirality $\chi$ rep theory (§7).
- Patch 0538 §14.2 calibration item substantively resolved.

### §11.2 What Layer 4 would require (deferred)

- Derivation of AC-1 (finite-dimensionality of matter-state Hilbert space) from CPP axioms A1–A11 + substrate-geometric primitives alone, without Reading C as a framework-construction commitment.
- Derivation of $P_{TI}$ commutativity $[T, I] = 0$ from A5 framework primitives alone (currently a framework commitment).
- Extension of Theorem 4.0 to non-AC-1 settings (infinite-dimensional realizations, history-dependent operators, nonlocal temporal structures) — per §8.3, with the spectral-theorem machinery + induced-representation generalization spelled out.
- Connection to long-term programme target (chirality scale from polytope geometry): if the polytope-geometric chirality scale derivation introduces nonlocal temporal structures, Layer 4 extension becomes load-bearing.

### §11.3 Layer 3 → Layer 4 promotion path (for future reference)

When Layer 4 work on B.2.q1 opens (deferred behind F.1 / F.2 / F.3 stabilization per Patch 0539 §15.5), it will:

1. Take this Layer 3 document as the rigorous finite-dimensional anchor.
2. Identify which CPP axioms could derive AC-1 (e.g., CP-finiteness from A1 + finite first-shell content + finite-degrees-of-freedom-per-CP).
3. Extend the theorem to non-AC-1 settings using spectral-theorem machinery if needed for long-term programme target.
4. Engage with infinite-dimensional realizations as alternative framework constructions (graph-holonomy, coarse-grained transport tensor, delayed-cycle operators).

These are substantial extensions warranting their own Patches; this Layer 3 document does NOT prejudge their direction.

---

## §12 Self-checkpoint — three places §0–§11 could overstate

### §12.1 "Rigorous framework axiomatization" framing

The "framework axiomatization" framing in §0.2 + §1.3 reads as strong claim. The reality is: AC-1 (§2.4) is a derived framework commitment from Reading C + first-shell-content matter-state construction, not a fundamental axiom. The theorem's domain of applicability is tied to AC-1; framework constructions outside AC-1 (per §2.4 out-of-scope alternatives) require their own treatment. The "axiomatization" framing should be read as "rigorous statement of the framework's finite-dimensional commitment as load-bearing within Theorem 4.0's domain," not as "axiomatization of $P_{TI}$ from CPP axioms A1–A11 alone." Layer 4 would address the latter.

### §12.2 "Substantively resolves Patch 0538 §14.2" framing

§8.5 + §10.2 frame the Layer 3 promotion as substantively resolving Patch 0538 §14.2's finite-dimensional-scope concern. The resolution is: making the finite-dimensional scope load-bearing axiomatic commitment AC-1, identifying where it's used in the proof, and registering Layer 4 extension as deferred. This is a Layer-3-appropriate resolution; full resolution at Layer 4 would require deriving AC-1 from CPP axioms alone OR extending the theorem to non-AC-1 settings. The current Patch does the former part (axiomatize the scope) but not the latter (derive or extend). The Patch 0538 §14.2 concern is substantively addressed at Layer 3; full resolution remains Layer 4.

### §12.3 "Theorem 4.0 proved rigorously" framing

The "proved rigorously" framing in §11.1 covers the proof in §5 + §6 under AC-1 + the framework commitments stated in Theorem 4.0's hypothesis. The proof uses standard finite-group rep theory machinery (Maschke's theorem, character orthogonality, Schur's lemma, minimal polynomial of $M^2 = \mathbb{1}$), each established at standard rep-theory-textbook rigor. The Layer 3 "rigorous" framing should be read as "every proof step formalized at standard finite-group-rep-theory-textbook rigor," not as "proved from first principles independent of framework commitments." The framework commitments (A5.2, A5.3, $P_{TI}$ commutativity, AC-1) are explicit hypotheses of the theorem and are themselves Layer 4 derivation targets.

---

## §13 Programme state after this Layer 3 promotion

### §13.1 What changed at programme level

- B.2.q1 promoted from sketch Layer 2 closure (Patch 0536 §12, with Patch 0538 §14.2 finite-dim scope qualifier) to sketch-document Layer 3 closure under AC-1 framework commitment.
- Patch 0538 §14.2 calibration item substantively resolved at sketch-document Layer 3.
- Priority 1 chain Target 2 → Target 3 OPENED (this Patch is Target 2; Target 3 is the next Patch in the chain).
- Second Layer 3 promotion in F.1 trajectory (Patch 0541 was the first, on Target 1 B.1.q4).

### §13.2 What did NOT change

- F.1 sub-question status UNCHANGED at Patch 0539 framing.
- No new Findings registered.
- No sub-question reopenings.
- No v1.0 SHIPPED edits.
- No Phase 1 §11 / Phase 2 §12 polished content modifications.
- No Patches 0531–0541a immutable content modifications.
- No reviewer-pause checkpoint modifications.
- No flagship paper assembly trigger.
- No F.2/F.3 substantive content trajectory opening.
- No long-term programme target (Layer 4) work.
- No bundling of multiple Layer 3 promotion targets.

### §13.3 Forward queue post-Patch 0542

(A) **Patch 0543+ candidacy — Target 3 (B.1.q1 matter-state independent derivation Layer 3)**. This Patch (Target 2) is Target 3's prerequisite; Target 3 closes the Priority 1 chain Target 2 → Target 3 by deriving matter-state $I_h$-covariance independently of Reading C framework homogeneity. Estimated 2–3 sessions.

(B) Subsequent Patches close Targets 4, 5, 6, 7 per Patch 0540 §4.1 priority ordering. Aggregate remaining timeline 6–17 sessions for full Layer 3 promotion arc completion.

(C) Layer 3 reviewer-pause cycle Patch when load-bearing Layer 3 arc completes.

(D) Layer 3 status upgrade Patch when reviewer-pause completes positively.

(E) F.1 flagship paper assembly DEFERRED behind (C) + (D).

(F) F.2 / F.3 substantive content trajectories DEFERRED at decision-gate level.

(G) Long-term programme target — chirality scale from polytope geometry (Layer 4) — REGISTERED + DEFERRED.

(H) Layer 4 extension of B.2.q1 to non-AC-1 settings (per §8.3 + §11.2) — REGISTERED + DEFERRED behind F.1/F.2/F.3 stabilization.

(I) JUNO peer-review update integration when published.

(J) Future reviewer-pause cycles available on-demand at future Layer 3 closure milestones per §17 discipline.

### §13.4 Anti-priorities sustained going forward

All anti-priorities from §0.1 of this document, cumulative from all prior Patches in Sessions 139–140 (0537–0541a). Plus this Patch's additional anti-priorities:

- No infinite-dimensional extension at this Patch (deferred to Layer 4).
- No derivation of AC-1 from CPP axioms A1–A11 alone (deferred to Layer 4).
- No derivation of $P_{TI}$ commutativity from A5 alone (framework commitment).
- No closure of B.2.q2, B.2.q3, B.2.q4 (each its own gated trajectory).
- No matter-state-irrep enumeration (Target 3 territory, next Patch in chain).

---

## §14 Closing summary

Patch 0542 closes B.2.q1 at sketch-document Layer 3 under the framework commitment AC-1 (finite-dimensionality of matter-state Hilbert space at $v_{\text{host}}$). The Layer 3 promotion makes the finite-dimensional scope load-bearing axiomatic commitment rather than ad-hoc qualifier, substantively resolving the Patch 0538 §14.2 cross-reviewer-convergent calibration item. The rigorous representation theory of $P_{TI} = \mathbb{Z}_2 \times \mathbb{Z}_2$ is developed in §3 (character table, Maschke's theorem with explicit projectors, tensor product structure, Frobenius-Schur indicator $+1$ giving real-irrep structure). The Minimal Algebraic Realization Theorem (Theorem 4.0) is proved rigorously in §5 in four formalized steps, each identifying the framework commitments used. Non-multiplicative-matrix-action ruling-out (Theorem 6.1 + Corollary 6.2) is restated rigorously in §6. Cross-reference parallel to Capotauro v2.0 chirality $\chi$ rep theory in §7. Extension to non-AC-1 settings registered as Layer 4 territory in §8 with technical machinery spelled out.

The Layer 3 promotion opens the Priority 1 chain Target 2 → Target 3 per Patch 0540 §4.1. Target 3 (B.1.q1 matter-state independent derivation Layer 3) is the next Patch in the chain; this Patch is its prerequisite. The chain closes the two strongest cross-reviewer-convergent calibration items (§14.1 + §14.2) in coupled fashion.

F.1 sub-question status UNCHANGED at Patch 0539 framing. Findings registry UNCHANGED. v1.0 SHIPPED edits NONE. Patches 0531–0541a immutable content UNCHANGED. Reviewer-pause checkpoint UNCHANGED. Flagship paper assembly NOT triggered. F.2/F.3 trajectories NOT opened. Long-term programme target REGISTERED + DEFERRED.

Second Layer 3 promotion in F.1 trajectory complete. Priority 1 chain Target 2 → Target 3 opened; Target 3 closure is next gated trajectory at Patch 0543+ candidacy.
