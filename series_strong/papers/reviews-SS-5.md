# Reviews: SS-5 — Deuteron Binding Energy from Open-Vertex Tetrahedral Bonding

**Paper:** SS-5 v0.1
**Last updated:** 16 April 2026
**Document type:** External reviews and response-to-reviewer record

---

## Review status

| Reviewer | Status | Date | Output |
|---|---|---|---|
| Grok (xAI) | Not yet submitted | — | Pending |
| Copilot (Microsoft) | Not yet submitted | — | Pending |
| Claude Sonnet (Anthropic) | Not yet submitted | — | Pending hostile review pass |
| ChatGPT (OpenAI) | Not yet submitted | — | Optional third-opinion, post-Grok |

This stub is the placeholder for the v0.1 review cycle. No formal reviews have been received yet; the entries below mark the specific items on which external review is requested.

---

## Part 1 — Specific questions for reviewers

### For Grok (xAI) — targeted verification

Grok's strength is rapid verification via independent numerical/algebraic checks. Please verify:

1. **The $\eta^2$ prefactor argument (§4.2).** $B_d = M_0/\varphi = m_e z/\varphi^2 = 2.343$ MeV uses two factors of $\eta = 1/\varphi$: one implicit in $M_0$, one explicit for bond-delivery propagation across the dangling edge. Is the second factor physically justified, or is it double-counting (i.e., was it already implicit in $M_0$)?
   - **Alternative 1:** Only one $\eta$ → $B_d = M_0 = 3.79$ MeV ($+70\%$ error). Falsified.
   - **Alternative 2:** Three $\eta$ → $B_d = M_0/\varphi^2 = 1.45$ MeV ($-35\%$ error). Falsified.
   - Status quo: two $\eta$ → 2.343 MeV ($+5.3\%$). Inside residual band.

2. **Residual identification.** The $+5.3\%$ residual: is this within the generic CPP stereographic band $\varphi^{1/z} - 1 = 4.1\%$? The paper argues the upper bound for single-edge oscillators is $(1 + \varphi^{1/z})^2 - 1 = 8.4\%$. Is this upper bound the right quantity?

3. **Numerical sanity check.** $m_e = 0.510999$ MeV; $z = 12$; $\varphi = 1.61803$. Compute $m_e z/\varphi^2$ and confirm 2.3422 MeV to 4 significant figures.

4. **Alternative formulas to rule out.** Scan the space of $B_d = m_e \cdot (\text{rational combination of } z, \varphi)$ that land within the residual band. Are there competing formulas with equal or better physical motivation? (E.g., $M_0 \cdot (3/5) = 2.274$ MeV has smaller residual but no nuclear-sector rationale for the 3/5 ratio.)

### For Copilot (Microsoft) — referee-grade review

Copilot's strength is referee-grade assessment of the overall argument. Please evaluate:

1. **Layer A/B/C separation (§3).** Is B1 (mode-sum prefactor rule) genuinely Layer B, or is it a Layer A consequence of A1–A11 that I have misclassified? Specifically: does the existence of the $\eta$ factor in $M_0$ already force $B_d$ to carry an additional $\eta$ for bond delivery, or is this an independent imported rule?

2. **Qualitative consequences (§6).** The argument that pp and nn are unbound from polarity pairing (Proposition 2.3) — is it genuinely structural, or does it rely implicitly on imported Pauli-principle content? Specifically: does the statement "two same-polarity CPs cannot form a qDP chain" follow from CPP axioms A1–A11, or is it an additional rule that needs to be made explicit?

3. **Comparison with standard nuclear physics.** Is the paper's claim that "the SM does not predict $B_d$" fair and accurate? (Chiral EFT fits it to scattering data; lattice QCD has not reached precision on the deuteron; is there a standard-model result I am overlooking?)

4. **The "first star shot in a new sector" claim.** Under the swarm-validation doctrine, the paper's epistemic weight depends on its independence from existing CPP anchors. Has the paper correctly identified and argued its independence? Are there hidden Layer B imports that correlate it with SS-3/SM-3?

### For Claude Sonnet — hostile review

Sonnet's strength is adversarial review. Please find the strongest plausible attack on:

1. **The $\eta^2$ prefactor** — is it reverse-engineered from the target $+5\%$ residual band, rather than derived from CPP first principles?

2. **The deuteron charge radius coincidence** — does the paper's §5.1 framing actually rescue the $R_\text{cl} \approx r_d^{\text{exp}}$ match from being over-claimed, or is it still a rhetorical sleight-of-hand?

3. **The cascade preview** — if naive bond-counting gets ${}^3$H and ${}^4$He wrong by factors 2 and 6, is this the paper's signature that the mechanism is *actually wrong for $A \geq 3$* (not just "needs cavity-mode combinatorics")?

4. **The zero-parameter claim** — is $m_e$ genuinely a non-nuclear calibration, or does it sneak in the electron mass through a back door (e.g., via the SM-8 DP energy quantum derivation that uses $m_e$ in a way that is coupled to nuclear phenomena)?

---

## Part 2 — Frequently anticipated questions (FAQ)

### Q: Why $m_e$? The deuteron has nothing to do with electrons.

A: $m_e$ is the CPP programme's single non-geometric calibration constant. It appears in $M_0 = m_e z/\varphi$ (SM-8) because $m_e$ sets the absolute energy scale of the lattice mode sums. Every CPP prediction for particle masses uses $m_e$ as the scale: the quark masses $M_q = m_e (z/\varphi) V^{7/3}$ (SM-8), the leptonic masses via Koide (SM-6), and now the deuteron binding energy. The electron mass is *not* a nuclear datum — its appearance here is a consequence of the lattice setting the universal energy scale.

### Q: How does this connect to QCD?

A: Structurally, not literally. The open-vertex bond is the CPP analog of the residual-strong-force exchange in QCD (pion-exchange tail, one-gluon-exchange short-range). The quark-level content is different: QCD's nuclear force is colour-singlet meson exchange; CPP's is an open-vertex qDP chain. The predictions agree at the observable level (2.343 vs 2.224 MeV binding), but the underlying picture differs.

### Q: Why only one qDP chain? Why not multiple?

A: Each nucleon has exactly one open vertex (the 4th vertex of its hybrid tetrahedron). So only one chain can form per nucleon-nucleon pair. This is why the binding scales with $M_0$, not $4 M_0$ (which would be the case if each internal edge also formed a cross-link). The single-chain, single-mode structure is geometrically forced, not assumed.

### Q: What about diproton/dineutron as scattering resonances?

A: The paper claims pp and nn are unbound — i.e., no bound ground state. Scattering resonances (like the dineutron virtual state) are perfectly consistent with this: a virtual state is in the continuum, not a bound state. The paper's claim is specifically about whether a bound deuteron-like nucleus exists for pp or nn, and the empirical answer is no.

### Q: Is there a way to falsify the theory quickly?

A: Yes. Three specific falsification routes:
1. Show mathematically that the second factor of $\eta$ is double-counted. This pushes the prediction to $M_0 = 3.79$ MeV ($+70\%$ error), falsifying.
2. Show that the $M_0/\varphi$ formula, applied to pion-exchange-like sub-systems, gives predictions incompatible with measured cross-sections.
3. Discover a bound diproton or dineutron. (No experiment in 70+ years has found one, but the theoretical possibility is a falsification route in principle.)

### Q: The magnetic moment prediction is 9.8% off. Isn't that bad?

A: Yes, but it's inherited from SS-2. The SS-2 neutron magnetic moment has a $-3.4\%$ residual; taking $\mu_d = \mu_p + \mu_n$ propagates that error. Additionally, the paper neglects D-wave admixture ($\sim 4\%$ of the wavefunction), which standard nuclear physics must also include for precision. Presented as a consistency check, not a precision prediction.

### Q: What is the next paper in the cascade?

A: SS-6 (or later) targeting the light-nuclei binding curve. Registered as OPEN-SS-17. The mechanism extends naturally but requires multi-bond cavity-mode combinatorics for $A \geq 3$.

---

## Part 3 — Response-to-reviewer template (for v0.2)

*To be populated after external reviews are received.*

```
### Reviewer X, Comment 1: [quote]
Response: [specific change made or defended]
Location in v0.2: [section/line]

### Reviewer X, Comment 2: [quote]
Response: ...
```

---

## Version history notes

- **v0.1 (16 April 2026):** Initial draft, pre-external-review. This file created as a stub for the review cycle.
- **v0.2 (expected):** Will incorporate Grok and Copilot reviews. Key target: verify the $\eta^2$ prefactor argument either as validated or as requiring revision.
- **v0.3+ (expected):** Sonnet hostile review pass; residual cleanup; OSF registration.
