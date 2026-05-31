# B-iii, sign(μ²) — Reaching the One Verdict-Moving Bit Without §14.17: a Vafa–Witten / Reflection-Positivity Route (with a Chiral-Susceptibility Backstop). Scoping

**Path:** `series_umbrella/series_substrate_chirality_arc/chirality_derivations/sketches/chir_biii_signmu2_reflection_positivity_scoping.md`
**Opened:** 30 May 2026 (Session 152 Patch 0679)
**Author:** Opus (Claude)
**Status:** Scoping at sketch level. NOT closure work, NOT a derivation, NOT a verdict move. Opens a route to the **single verdict-moving bit** — `sign(μ²)` of the B-iii ℤ₂-even Landau potential `V(η)` (`chir_biii_capacity_landau_scoping.md`, Patch 0668) — that does **not** require computing the full DSL effective action behind the F.1 §14.17 viability ceiling. The route asks whether a **Vafa–Witten-type reflection-positivity no-go** *forces* `sign(μ²) > 0` (the substrate cannot spontaneously break the det-coset parity ℤ₂ → no chiral vacuum from the substrate alone), and registers a **chiral-susceptibility computation** as the reachable computational backstop. **No claim is made that Vafa–Witten applies; whether it does is precisely the thing to determine.** Reserves the ID **THEO-CHIR-VW-1** for the eventual structural result; crystallizes nothing.
**Scope:** State the Vafa–Witten theorem and its three hypotheses; map them onto the det-coset ℤ₂ / `η` / `V(η)` of B-iii; decompose the "does VW apply to the substrate?" question into reachable structural sub-targets (VW-a..e); identify the precise way a VW no-go would settle the capacity question by principle (and the equally-informative contrapositive — which hypothesis the SM bridge breaks); register the susceptibility backstop (SUSC); record honest caps, routes, decision gates, falsifiers. Executes no dynamics; fixes no coefficient; proves no positivity.

---

## §0 Working-session firewall + anti-priorities

### §0.1 What this sketch IS

B-iii reduced the capacity question to one bit: **`sign(μ²)`** of the ℤ₂-even Landau potential `V(η) = V₀ + μ²η² + λη⁴ + …` for the det-coset order parameter `η` (the continuous precursor of `sign(n̂)` = FI-C-9), with `μ² < 0 ⇒` chiral double-well `⇒` the ℤ₂ breaks `⇒` V3→V1. The B-iii sketch pinned that bit as **"the deep core, NOT reached"** — fixed only by the DSL effective action behind §14.17. This sketch opens a route to the bit *itself* that sidesteps the full action:

- State **Vafa–Witten** (parity is not spontaneously broken in a reflection-positive, vector-like theory with no θ-term) and its three hypotheses (§3).
- Map the hypotheses onto the substrate: the det-coset ℤ₂ as a parity-type reflection, `η` as its P-odd order parameter, "capacity" as "is this parity spontaneously broken?" (§3.3).
- Decompose **"does VW apply to the substrate?"** into reachable structural sub-targets **VW-a..e** (§4): measure positivity, symmetry-class membership, the three evasion routes, the verdict map, the continuum-limit placement.
- Identify how a VW no-go would **force `sign(μ²) > 0`** and thereby settle the *spontaneous-substrate-breaking* branch of the capacity question **by principle, without §14.17** (§4.4) — and the equally-informative contrapositive: if VW is *evaded*, it is evaded only through an identifiable hypothesis-failure, and (by STATUS-2) only the SM bridge can supply it.
- Register the **chiral-susceptibility backstop SUSC** (§5): compute `sign(μ²) = sign(χ_η⁻¹)` from the connected `η`–`η` two-point function using the THEO-DSL path-enumeration + PSLQ machinery, if the VW question comes back underdetermined.
- Record routes + decision gates (§6) and falsifiers (§7).

This is the **B-iii analog of what BRIDGE-1 did for the ℤ₂-match**: take a deferred deep question and find the reachable *structural* handle on it. Here the handle is a no-go criterion, not the dynamics it would constrain.

### §0.2 Anti-priorities sustained at this Patch

Per the scope-sketch discipline (0637/0643/0646/0652/0662/0668/0669):

1. **NO derivation; NO dynamics; NO coefficient fixed; NO positivity proved.** `sign(μ²)` is **not** computed. Reflection-positivity of the DSL measure is **not** established — whether it holds is sub-target VW-a, explicitly *open*. This sketch sets up a route and its tests; it does not run them.
2. **NO verdict move.** FI-C-9 stays **V3**, `sign(δ)` stays **W3**. A VW no-go *would* settle the capacity question, but this sketch does not deliver one; it scopes the path to one.
3. **NO claim that Vafa–Witten applies.** The whole point is that "does VW apply to the substrate?" is the open question; both outcomes (applies → no-go; evaded → which hypothesis fails) are informative and neither is asserted here.
4. **NO new programme-level Open-Problem registration / NO header count change.** This refines the *route structure* of an existing target (B-iii-(i) = 1d-β-ii = OPEN-SM-4 (a)). It adds no problem and no conjecture. One reserved theorem ID (THEO-CHIR-VW-1); no theorem-registry body-table row (CHIR changelog-style registration, per the sub-corpus precedent).
5. **NO modification of the closed theorems** (STATUS-1/2, TARROW-1, BRIDGE-1, MERGE-1/2, CHI-1, CAP-1, PCD-ORIENTATION-1, CONT-1/2/3) or of the OPEN-SM-4 / Capotauro / F.1 / DSL sources. They are *consumed*, not edited.
6. **NO erosion of BRIDGE-1's honest cap.** The ℤ₂-skeleton this builds on is **kinematic only**, conditional on premise **P2** (OPEN-SM-4's ℤ₂ read as the enantiomorph ℤ₂). That tag rides every downstream statement.
7. **NO conflation of capacity with value.** VW addresses *capacity* (does parity break spontaneously — `sign(μ²)`). STATUS-2's V2-exclusion addresses *value* (can the sign be fixed at the axiom level — the V1-vs-V2 pin). They are distinct bits; §4.5 keeps them apart even though both wear "no-go" clothing.

### §0.3 What this sketch IS NOT

Not a proof that the substrate measure is reflection-positive; not a Vafa–Witten no-go; not a computation of the susceptibility or of `sign(μ²)`; not a derivation that the chiral vacuum does or does not form; not an OPEN-SM-4 / 1d-β-ii closure; not a theorem registration. It is the structural map of a reachable route to the one bit B-iii pinned as gated, plus a computational backstop — nothing run.

---

## §1 Purpose and structure

### §1.1 Why scope this now

After the Session-151 close, the chirality status is fully classified and review-hardened (V3 spatial / W3 temporal), the CHIR↔EW bridge's three reachable faces are mapped, and the programme's own logic says the verdict moves *only* when `sign(μ²)` is fixed — which B-iii pinned behind §14.17. Taken literally, that leaves no reachable verdict-moving work. But "fix the full DSL effective action, then read off `μ²`" is the *brute-force* route to the bit. The verdict needs only the **sign**, and a sign can sometimes be forced by a *principle* (a no-go theorem) or extracted from a *single correlator*, neither of which requires the whole action. This sketch opens the two such routes that are native to the programme's existing assets:

- a **Vafa–Witten reflection-positivity** argument (a principle that can force `sign(μ²) > 0`), which leans on STATUS-2's already-established V2-exclusion and on CONT-1's continuum-limit map; and
- a **chiral-susceptibility computation** (a single correlator's sign), which leans on the THEO-DSL-4..12 path-enumeration + PSLQ machinery.

Doing the reachable structural half today keeps the programme from stalling on the §14.17 ceiling, in exactly the spirit of the B-iii / STATUS-2 / BRIDGE-1 scope-then-charge pattern.

### §1.2 The one-line logic

> Capacity ⟺ `sign(μ²)` (B-iii, 0668). A Vafa–Witten no-go, *if its hypotheses hold for the substrate*, forces `sign(μ²) > 0` — the det-coset parity ℤ₂ **cannot** break spontaneously — settling the *spontaneous-substrate-breaking* branch by principle, with no §14.17. If a hypothesis fails, VW is evaded, and (by STATUS-2) only the SM bridge can supply the failure — which sharpens, rather than stalls, the emergent/primitive question.

---

## §2 Inputs consumed (all review-hardened or registered)

- **B-iii Landau reduction (Patch 0668):** capacity ⟺ `sign(μ²)` of the ℤ₂-even `V(η)`; `η` the continuous det-coset order parameter, ℤ₂: `η ↦ −η`; the ℤ₂-even form is *forced* (no axiom-level pseudoscalar source → no odd term). **This sketch takes `V(η)` and its reduction as given and asks only: what fixes the sign of μ²?**
- **STATUS-2 (F2, 3/3):** the breaking chain is H₄ → H₄⁺ (index-2 ℤ₂ = the det-coset); order parameter the pseudoscalar `sign(n̂)` = FI-C-9; **axiom-level V2-exclusion** — fixing the sign needs a P-odd pseudoscalar, and the only primitive one is FI-C-9 itself, so *no axiom-level source exists*. **This is already a Vafa–Witten-flavored statement** (see §4.5): the symmetric substrate has no internal handle to break/select parity; an *external* (cross-sector) pseudoscalar is required.
- **BRIDGE-1 (Patch 0663/0665, 3/3) — kinematic only, premise P2:** the det-coset ℤ₂ = the OPEN-SM-4 activation ℤ₂ (same object); the P/T-face dictionary (FI-C-9 ↔ EW V−A; `sign(δ)` ↔ δ_CP), CPT-unified. Supplies the *candidate evasion channel* for VW-c (the SM chiral content + CP phase).
- **CONT-1 (theorem #65):** the continuum-limit map **Φ** (Wilson–Fisher block-spin renormalization at the substrate cutoff `Λ_sub = ℓ_edge⁻¹`), under which substrate group-theoretic structure projects to the continuum EFT. **This is where a thermodynamic/continuum limit lives** — and VW is a statement about that limit (§4.5, VW-e).
- **THEO-DSL-4..12 (SD section):** closed-form substrate current/correlator coefficients on the 600-cell by directed-path enumeration (`12^k` paths) + `mpmath.pslq` in `ℚ[φ]` (extended basis `{1, φ, √3, √3φ}`), verified to machine precision and multi-AI confirmed. **This is the validated pipeline the susceptibility backstop (SUSC, §5) would reuse.**

---

## §3 The Vafa–Witten theorem and its map to the substrate

### §3.1 The theorem (as used here)

Vafa & Witten (1984), *Parity Conservation in QCD* / *Restrictions on Symmetry Breaking in Vector-Like Gauge Theories*: in a Euclidean theory whose path-integral measure is **real and positive** (reflection / Osterwalder–Schrader positive) and whose matter content is **vector-like** (non-chiral), with **no θ-term** (CP-conserving measure), **parity and vectorial reflection symmetries are not spontaneously broken in the vacuum** — the parity-symmetric configuration minimizes the free energy, and the expectation value of any parity-odd order parameter vanishes. The argument is a positivity bound: with a positive measure, an explicit parity-breaking perturbation can only *raise* the free energy, so the symmetric point is a minimum.

**The three hypotheses** (all three are required; failure of any one voids the conclusion):
- **(H1) Reflection positivity** — the Euclidean measure / Boltzmann weight is real and positive (no sign problem).
- **(H2) Vector-like (non-chiral)** — the symmetry in question is a genuine *reflection/parity* (vectorial), not an *axial/chiral* symmetry (VW does **not** forbid axial breaking — that is precisely chiral condensation).
- **(H3) No θ-term** — no CP-odd topological term in the action (or θ = 0).

### §3.2 Why this is the right tool for `sign(μ²)`

`μ² > 0` is exactly the statement "the symmetric vacuum `η = 0` is stable — parity is *not* spontaneously broken." That is the **conclusion** of Vafa–Witten. So **if** (H1)+(H2)+(H3) hold for the substrate's `η`-dynamics, VW delivers `μ² > 0` *as a theorem*, with no need to compute `μ²` from the DSL action. The bit B-iii pinned as gated would be **forced by principle**.

### §3.3 The map

| VW object | substrate counterpart |
|---|---|
| parity / reflection symmetry | the det-coset ℤ₂ (orientation-reversing, det = −1; enantiomorph exchange) |
| parity-odd order parameter | `η` (the continuous det-coset pseudoscalar; `⟨η⟩ ≠ 0` ⟺ spontaneous parity breaking) |
| "parity not broken" (VW conclusion) | `μ² > 0` (symmetric vacuum stable; no chiral vacuum from the substrate) |
| positive measure (H1) | reflection-positivity of the DSL Euclidean measure / PCD-cycle Boltzmann weight |
| vector-like (H2) | the det-coset ℤ₂ is a true reflection (vectorial), not an axial symmetry |
| no θ-term (H3) | no CP-odd topological term in the DSL action; `sign(δ)` = W-arrow not yet an action term |

The map is clean because the det-coset ℤ₂ **is** a parity (it is the orientation-reversing coset, det = −1) — VW is built for exactly this symmetry class. The work is in checking the three hypotheses, not in forcing the analogy.

---

## §4 Decomposition into reachable sub-targets (VW-a..e)

| sub-target | content | reachable now? |
|---|---|---|
| **VW-a** | (H1) reflection-positivity of the DSL measure: is the PCD-cycle Boltzmann weight real and positive (no sign problem)? | **criteria + first-pass: yes**; a complete proof may need the DSL action (partial gate) |
| **VW-b** | (H2) symmetry-class membership: confirm the det-coset ℤ₂ is a *vectorial reflection* in VW's scope, **not** an axial/chiral symmetry (which VW would *not* protect) | **structural: yes** |
| **VW-c** | (H3) + evasion audit: are any of {chiral content, θ-term, complex measure} present in the *bare substrate*, and which (if any) does the **SM bridge** supply? | **structural classification: yes** |
| **VW-d** | the verdict map: assemble VW-a/b/c into either a no-go (`μ²>0` forced) or a named evasion | **assembly: yes** once a/b/c land |
| **VW-e** | continuum-limit placement: pose VW on the **Φ-continuum EFT** (CONT-1), where SSB and VW are well-defined (a finite 600-cell can only *select*, not spontaneously break) | **structural: yes** |

### §4.1 VW-a — reflection-positivity of the DSL measure (H1)

The decisive and hardest hypothesis. Reflection positivity (Osterwalder–Schrader) is the Euclidean encoding of unitarity / a positive transfer matrix; concretely it asks whether the DSL Euclidean weight `e^{−S_DSL}` is real and positive, i.e. whether the PCD-cycle dynamics (**P**erceive, **C**ompute, **D**isplace) define a real, positive Boltzmann weight or carry a phase (a sign problem). **What is reachable now:** (i) writing down the OS-positivity *criteria* for the DSL action's structure; (ii) a first-pass assessment from the *known* structural features of the DSL (the net DI-bit current ∥ `n̂`, the Mechanism-A rate function, the `ℚ[φ]`-valued real coefficients of THEO-DSL-4..12 — all *real*, a positive sign). **What is gated:** a complete positivity *proof* may require the DSL action's explicit form (the §14.17 object). So VW-a is *partially* reachable: criteria + a first-pass real-measure assessment now; full proof possibly gated. Crucially, even a *first-pass* "the measure is manifestly real and the obvious phase sources are absent" would shift the burden onto VW-c (find an evasion) rather than VW-a.

### §4.2 VW-b — the det-coset ℤ₂ is a vectorial reflection (H2)

VW protects *vectorial* (parity) symmetries; it does **not** protect *axial* (chiral) symmetries — axial breaking is the QCD chiral condensate, which VW explicitly permits. So the analysis must confirm the det-coset ℤ₂ is genuinely a **reflection on configuration space** (det = −1 isometry, enantiomorph exchange — which STATUS-2 establishes it is), **not** an axial rotation acting on a chiral field doublet. STATUS-2's chain (H₄ → H₄⁺, the *rotation* subgroup, with the coset generated by a *reflection*) is exactly the data needed: the broken ℤ₂ is the reflection coset, vectorial by construction. **Reachable now** as a short structural lemma. (Subtlety to handle: under the bridge, FI-C-9 ↔ the V−A axial structure of the SM — so the *same* ℤ₂ that is vectorial on the substrate is the one whose SM image touches chiral content. That is not a contradiction; it is the seam where VW-c looks for the evasion.)

### §4.3 VW-c — the evasion audit (H3 and the negatives of H1/H2)

VW fails iff at least one of: **(a)** chiral (non-vector-like) content, **(b)** a θ-like CP-odd topological term, **(c)** a complex/non-positive measure. Audit each against the bare substrate and against the bridge:
- **(a) chiral content:** the bare substrate is achiral (the 600-cell hosts no intrinsic handedness; STATUS-2). Chiral content enters *only* through the SM image (V−A; E26) — i.e. **via the bridge**, not intrinsically.
- **(b) θ-term:** is there a CP-odd topological term in the DSL action? The temporal arrow `sign(δ)` (W-side) is the candidate, but TARROW-1 places it at W3 and it is *not* currently an action term — flag as the precise thing to check against the DSL once available.
- **(c) complex measure:** the candidate phase is the SM CP phase `δ_CP` (CPT-linked to `sign(δ)` via BRIDGE-1's dictionary). In the bare substrate the THEO-DSL coefficients are real (`ℚ[φ]`); a phase, if any, is a **bridge** import.
**The pattern (to be confirmed, not asserted):** every evasion route appears to enter through the SM bridge, not the bare substrate — which is exactly STATUS-2's V2-exclusion in VW language (the substrate alone cannot break/select parity; an external cross-sector input is required). **Reachable now** as a structural classification; the conclusions about the bridge inherit BRIDGE-1's "kinematic, P2" cap.

### §4.4 VW-d — the verdict map

Assemble:
- **If (H1) ∧ (H2) ∧ (H3) hold for the bare substrate** → VW forces `μ² > 0` → the det-coset ℤ₂ **does not spontaneously break in the substrate** → the substrate generates *no* handedness dynamically. Then the observed FI-C-9 ≠ 0 is **either** a genuine primitive input (**V3 by principle** — a strictly stronger statement than today's "V3 = not yet derived": the spontaneous-mechanism branch is *closed*, not merely unbuilt) **or** explicitly sourced by the SM bridge (emergent **via the bridge**, i.e. *explicit* breaking, not spontaneous substrate breaking). This is the candidate **THEO-CHIR-VW-1** no-go: *spontaneous substrate parity-breaking is excluded; capacity, if realized at all, is bridge-sourced.* It would **settle the spontaneous-substrate branch without §14.17** and reduce the whole emergent question to B-iii-(ii) (the EWSB-identification / CONJ-CHIR-1).
- **If a hypothesis fails (evasion)** → VW is silent, `sign(μ²)` is genuinely dynamical and needs the DSL/bridge — *but* VW-c will have **named which hypothesis** fails and (per §4.3) shown it enters through the bridge. That is itself a result: it pins the emergence channel.
- **If VW-a is underdetermined** (measure positivity neither establishable nor refutable from current DSL structure) → fall through to the **SUSC backstop** (§5).

**Caveat carried throughout:** the spontaneous-vs-explicit distinction is load-bearing. VW forbids *spontaneous* parity breaking; it says nothing against an *explicit* P-odd source. STATUS-2 already shows there is no *axiom-level* explicit source — so within the substrate axioms, VW-protection would force `η = 0` outright, which (since FI-C-9 ≠ 0 is used) would push FI-C-9 to genuine-primitive-input status. The only escape is an explicit source from *outside* the substrate axioms — the SM bridge. This is the precise content to be made rigorous, not asserted here.

### §4.5 VW-e — the continuum-limit placement (and the STATUS-2 connection)

Strict spontaneous symmetry breaking requires a thermodynamic/continuum limit; a *finite* 600-cell cannot spontaneously break a symmetry, it can only *select* one of two degenerate vacua. So the VW analysis is sharpest **not** on the bare finite substrate but on its **Φ-continuum image** (CONT-1's Wilson–Fisher block-spin EFT), where "SSB", "free energy", and "reflection positivity" are standard, well-defined notions and where VW is a textbook tool. Conveniently, Φ is also where the SM chirality the bridge connects to actually lives — so VW-a/b/c are all most naturally posed on the Φ-EFT. **Connection to STATUS-2:** STATUS-2's axiom-level V2-exclusion (no internal pseudoscalar can fix the sign; an external one is needed) is the *value*-side shadow of the *capacity*-side statement VW would make. Naming them as two faces of one reflection-positivity structure — V2-exclusion (value) + VW no-go (capacity) — is itself a clarifying structural result and a natural first artifact under THEO-CHIR-VW-1.

---

## §5 The chiral-susceptibility backstop (SUSC) — sign(μ²) from one correlator

If VW-a returns underdetermined, `sign(μ²)` is still reachable computationally without the full potential. In Landau theory the quadratic coefficient is the **inverse zero-momentum susceptibility** of the order parameter in the symmetric phase:

> `μ² ∝ χ_η⁻¹`, where `χ_η = ∫ ⟨η(x) η(0)⟩_c` (the connected, zero-momentum `η`–`η` two-point function).

So `sign(μ²) = sign(χ_η⁻¹)`: a **positive, finite** susceptibility ⟺ `μ² > 0` (stable symmetric vacuum, V3); a **divergent/negative** susceptibility ⟺ `μ² ≤ 0` (instability toward chiral ordering, V3→V1). One does not need `V(η)` in full — only the sign/divergence of one correlator.

**The reachable computation:** `η` is the det-coset pseudoscalar built from the substrate orientation field; its connected two-point function on the 600-cell is exactly the class of object the **THEO-DSL-4..12 pipeline** already computes in closed form — directed-path enumeration (`12^k` paths) + `mpmath.pslq` in the extended `ℚ[φ]` basis, machine-precision-verified, multi-AI-confirmed. Pointing that validated pipeline at the `η`–`η` susceptibility is a **single-bit target in the programme's native zero-parameter style**, and it would produce a reviewable artifact (a verify script + reasoning fragment) even at partial rigor. **Honest cap on SUSC:** a finite-lattice susceptibility sign is suggestive but not a proof of the *continuum* `sign(μ²)` (the §4.5 limit caveat applies); the right statement is the *trend* of `χ_η` under the Φ block-spin flow (growing → instability; bounded → stability), which the THEO-DSL machinery is already set up to probe order-by-order. SUSC is the computational backstop, not the primary; it carries a verify script when it lands.

---

## §6 Routes, decision gates, recommendation

**Routes:**
- **Route VW (recommended):** VW-e placement → VW-b (quick structural confirm) → VW-a first-pass (real-measure assessment + OS criteria) → VW-c evasion audit → VW-d assembly. Best first artifact: the **V2-exclusion ↔ VW-no-go unification** (§4.5) — a structural lemma that needs no new dynamics and would crystallize THEO-CHIR-VW-1 at the reachable (criteria + first-pass) level, explicitly flagging the residual (full H1 proof) as the part that may still touch §14.17.
- **Route SUSC (backstop):** if VW-a is underdetermined, compute `sign(χ_η⁻¹)` via the THEO-DSL pipeline; report the finite-lattice sign + the block-spin trend, with the continuum caveat.

**Decision gates:**
- **DG-1:** reserve **THEO-CHIR-VW-1** for the structural reflection-positivity result (the V2-exclusion↔VW-no-go unification + the VW-a/b/c characterization). *Recommended; deferred to the first substantive sub-target patch* (per the STATUS-1 ID-reservation precedent at 0653).
- **DG-2:** Route VW before Route SUSC (a principle that could *force* the bit beats a finite-lattice computation that only *suggests* it). SUSC opens only if VW-a stalls.
- **DG-3:** any VW-d no-go (THEO-CHIR-VW-1 reaching a verdict-bearing statement) **requires multi-AI review** before any verdict language changes — it would be the first thing in the programme that could move V3 off "not yet derived", so the honesty bar is maximal.
- **DG-4:** keep capacity (VW / `sign(μ²)`) and value (STATUS-2 / V2-exclusion) as distinct bits in all downstream text, even though both are no-gos.

**Recommendation:** open Route VW with the §4.5 unification as the first artifact; hold SUSC as the backstop; do not touch verdict language until DG-3 is satisfied.

---

## §7 Honest caps and falsifiers

**Honest caps.** (1) Reflection-positivity of the DSL measure is **assumed nowhere** and **proved nowhere** here — it is the open hypothesis VW-a. (2) A VW no-go would close the *spontaneous-substrate-breaking* branch only; *explicit* bridge-sourced breaking is untouched (and is exactly B-iii-(ii) / CONJ-CHIR-1). (3) All bridge-side statements inherit BRIDGE-1's **kinematic / premise-P2** cap. (4) The continuum-limit caveat (§4.5) applies to both routes; finite-600-cell statements are suggestive, not continuum-final. (5) No verdict moves at this patch; V3/W3 stand.

**Falsifiers (of this *route*, not of any result):**
- **VW-F1:** the det-coset ℤ₂ turns out to be an *axial* symmetry in the relevant EFT (VW-b fails) → VW does not apply; the route is void (but that itself reclassifies the symmetry, informatively).
- **VW-F2:** the DSL measure is provably *non*-positive / has a genuine sign problem (VW-a fails in the negative) → VW does not apply; `sign(μ²)` is genuinely dynamical and §14.17-gated.
- **VW-F3:** an axiom-level (substrate-intrinsic) θ-term or chiral content is found (VW-c finds an intrinsic, non-bridge evasion) → contradicts STATUS-2's achiral/V2-exclusion result; would force re-examination of STATUS-2.
- **VW-F4:** the susceptibility backstop returns a sign that *contradicts* a VW conclusion reached on the same EFT → a genuine inconsistency requiring resolution (most likely a continuum-vs-finite-lattice artifact per §4.5).

---

## §8 Next

Per Thomas's choice: open **Route VW** with the **§4.5 V2-exclusion ↔ VW-no-go unification** as the first reachable artifact (structural lemma; crystallizes THEO-CHIR-VW-1 at the criteria + first-pass level; flags the residual full-positivity proof as the part that may still touch §14.17), routing any verdict-bearing outcome to multi-AI review (DG-3) before any verdict language changes; hold **Route SUSC** as the computational backstop if VW-a stalls. Either way the deliverable is reachable now and verdict-neutral until DG-3 is satisfied.
