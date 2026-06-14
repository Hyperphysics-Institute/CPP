# SF-1 Structural Core — K3 Theorem · Weinberg Intermediate · Koide Phase Arc

**Location:** `/CPP/flagship_papers/charged_leptons/sketches/SF-1_structural_core.md`
**Opened:** Session 160, Patch 1307 (SF-7 grand-unification window)
**Status:** STAGING DOCUMENT — the structural-derivation core (§3–§5 of the SF-1 outline) worked out for direct transfer into `sf-1_charged_leptons.tex`. This is the "first drafting move" recommended in `sf-1_outline.md` §8: draft the K3 theorem + Weinberg + phase arc as the load-bearing core, then assemble the framing sections around it. **The full `.tex` assembly + multi-AI panel review is the next (Thomas-driven) phase** — this document does the hard reframing so that phase starts from a solid core.
**Source (all shipped):** SM-3 v6 (K3 spectral theorem), SM-4 (mass formulae + θ impossibility), SM-6 v3 (Weinberg + phase derivation).

---

## 0. What this document delivers

The three sections that carry SF-1's flagship weight, with exact equations and honest epistemic grading:
- **Part A (→ §3):** the K3 Spectral Theorem giving Koide $K=2/3$, with the Layer A/B/C decomposition.
- **Part B (→ §4):** the Weinberg angle $\sin^2\theta_W=3/(8\phi)$ as an intermediate spectral-trace result.
- **Part C (→ §5):** the Koide phase as a **closed SM-4→SM-6 arc** — the one piece that needs careful narrative, and the highest-value reframing in the paper.
- **Part D (→ §6):** the mass spectrum assembled from A+B+C.
- **Part E:** the honest calibration/inheritance ledger.

Everything here is reframing of shipped results; no new derivation.

---

## A. The K3 Spectral Theorem (→ §3) — Koide $K = 2/3$

**Setup.** The three colour-cage base vertices $\{V_1,V_2,V_3\}$ form the complete graph $K_3$ (equilateral triangle, the tetrahedral cage base). The ZBW Hamiltonian on this base is
$$\hat{H} = \hbar\omega_0\, A_{K_3},$$
where $A_{K_3}$ is the $K_3$ adjacency matrix. Its spectrum is $\{+2, -1, -1\}$ — bonding eigenvalue $\lambda_{\max}=+2$, antibonding doublet $\lambda=-1$. The eigenvalue-magnitude ratio is
$$\frac{\lambda_{\max}}{|\lambda_{\min}|} = \frac{2}{1} = 2.$$

**The Koide chain.** With $m_i \propto |\psi_i|^2$ and the C3-symmetric eigenstate structure, the Lorentz modulation depth is fixed by the eigenvalue ratio: $\rho = \sqrt{2}$. The Koide quantity then follows exactly:
$$K \equiv \frac{\sum_i m_i}{\left(\sum_i \sqrt{m_i}\right)^2} = \frac{1+\rho^2/2}{3} = \frac{1 + 1}{3} = \frac{2}{3}.$$
Equivalently $K=2/3 \Leftrightarrow \rho=\sqrt2 \Leftrightarrow \lambda_{\max}/|\lambda_{\min}|=2$. **Specific to $K_3$:** only the three-colour cage ($N=3$) yields $2/3$. The theorem is **leptons-only** — quarks carry strong-sector contributions that break Koide by 10–27%.

**Epistemic grading (Layer A/B/C — carry this verbatim into §3 for credibility).**
- **(P1) Layer A:** $\hat{H}=\hbar\omega_0 A_{K_3}$ derived from C3 cage symmetry + SSV hopping. *Geometric input — solid.*
- **(P2) Layer A:** $m_i \propto |\psi_i|^2$ derived from the CPP DI-bit visit rate. *Solid.*
- **(P3) Layer B:** equal eigenstate occupation from thermal equilibration with the DP Sea in the high-$T$ limit ($kT_P/\hbar\omega_0 \sim 10^{20}$). Gibbs formalism is standard; the **system–bath coupling model (Caldeira–Leggett) is imported from open-quantum-systems theory** — this is the one Layer-B assumption. Resolution path: **SS-4**. Register as **OPEN-FP-1-P3** and inherit (do not close).
- **(Layer C):** under P1–P3, $K=2/3$ follows exactly.

**Robustness.** Finite-$T$ departures from $K=2/3$ are $O(\hbar\omega_0/kT_P)\sim 10^{-20}$, nine orders below the 11 ppm experimental precision. So P3 is *epistemically* Layer B but *empirically* harmless — state both plainly.

---

## B. The Weinberg angle as intermediate (→ §4) — $\sin^2\theta_W = 3/(8\phi)$

**Mode counting on the 600-cell adjacency $A$.** Two spectral traces partition the lattice mode capacity:
$$\mathrm{Tr}(A^2) = 2E = 1440 \quad \text{(abelian edge modes, U(1)}_Y),$$
$$\tfrac{1}{3}\mathrm{Tr}(A^3) = 2F = 2400 \quad \text{(non-abelian face-circulation modes, SU(2)}_L).$$
The bare topological mixing ratio is
$$\frac{\mathrm{Tr}(A^2)}{\mathrm{Tr}(A^2) + \tfrac{1}{3}\mathrm{Tr}(A^3)} = \frac{1440}{1440+2400} = \frac{1440}{3840} = \frac{3}{8}.$$
This $3/8$ is **unique to the 600-cell** among the six regular 4-polytopes (the dual 120-cell gives $5/8$), and equals the SU(5) GUT-scale Weinberg angle. The physical value applies the edge-propagation efficiency $\eta = \ell_{\rm edge}/R_{\rm circ} = 1/\phi$ (SSV/PSR metric correction):
$$\boxed{\;\sin^2\theta_W = \frac{1}{\phi}\cdot\frac{3}{8} = \frac{3}{8\phi} \approx 0.2318\;}$$
vs PDG $0.23121$ — **0.24%**. (The $0.24\%$ residual is the zero-temperature lattice prediction vs the running low-energy value.)

**Framing note (carry into §4):** in CPP the Weinberg angle is *not* defined via gauge couplings $g,g'$. The denominator is the fixed topological mode capacity (3840); only the numerator carries the $1/\phi$ metric correction (linear prefactor, not a quadratic coupling ratio). This departure from the SM definition is forced by the lattice and is the conceptual key.

---

## C. The Koide phase arc (→ §5) — the closed SM-4 → SM-6 derivation (HIGH-VALUE)

This is the section that needs the most careful narrative. Present it as a **completed arc, not a contradiction.**

**Step 1 — SM-4's impossibility theorem.** The individual masses are parametrised by the Koide phase $\theta$:
$$\sqrt{m_i} = A\left(1 + \sqrt{2}\cos\!\left(\theta + \tfrac{2\pi i}{3}\right)\right).$$
SM-4's structural theorem (`thm:theta_free`) proves that the C3 symmetry of $K_3+$SSV leaves $\theta$ **undetermined** — $\theta$ cannot be fixed from the cage-face structure *alone*. SM-4 extracts $\theta = 132.73°$ from PDG and labels its derivation the principal open problem gating the electroweak series (**OP-SM-7d**). *This is the motivation, not a failure: it proves an electroweak ingredient is necessary.*

**Step 2 — SM-6 supplies the electroweak ingredient.** The base value is the $K_3$ eigenvalue ratio (from Part A): $\cos\theta_0 = -K = -2/3$. The electroweak isotropic shift on the $K_3$ cage face shifts all eigenvalues without breaking C3:
$$\varepsilon = \frac{2\sin^2\theta_W}{z+1} = \frac{2\cdot 3/(8\phi)}{13} = \frac{3}{52\phi}.$$
This gives
$$\cos\theta_{\rm Koide} = -\frac{2}{3}\left(1 + \frac{\sin^2\theta_W}{z+1}\right) = -\frac{2}{3}\left(1 + \frac{3}{104\phi}\right),$$
yielding
$$\boxed{\;\theta = 132.731°\;}$$
vs PDG $132.732°$ — **0.003%**.

**The arc closes.** SM-4 says "θ needs EW input"; SM-6 says "here is the EW input ($\varepsilon \propto \sin^2\theta_W$), and θ follows." OP-SM-7d is **resolved for the charged-lepton phase**. *Narrative discipline:* lead with SM-4's impossibility theorem (why the EW correction is necessary), then deliver SM-6's correction (what supplies it). Do **not** present these as competing claims.

**Cross-sector hook (for SF-7 §10):** the $\varepsilon$ that fixes $\theta$ is built from $\sin^2\theta_W=3/(8\phi)$ — the **same** Weinberg-angle spectral-trace quantity SF-2 inherits. This is the SF-1↔SF-2 §10 thread.

---

## D. The mass spectrum (→ §6)

With $K=2/3$ ($\rho=\sqrt2$, Part A), $\theta=132.731°$ (Part C), and the amplitude fixed by the electron calibration,
$$A = \frac{\sqrt{m_e}}{1+\sqrt2\cos\theta},$$
the muon and tau masses follow:
$$m_\mu = \left(A + \sqrt2\,A\cos\!\left(\theta+\tfrac{2\pi}{3}\right)\right)^2 = 105.47~\text{MeV}\quad(\text{PDG }105.66,\ 0.18\%),$$
$$m_\tau = \left(A + \sqrt2\,A\cos\!\left(\theta+\tfrac{4\pi}{3}\right)\right)^2 = 1774.1~\text{MeV}\quad(\text{PDG }1776.9,\ 0.15\%).$$
The electron mass is the calibration; $m_\mu, m_\tau$ are predictions at zero shape parameters.

---

## E. Honest calibration / inheritance ledger (→ §7–§8)

- **Calibration:** one constant, $m_e$ (equivalently $\mathrm{SSV}_0 = m_e c^2/2$). **Zero shape parameters.** SF-1 is the **cleanest single-$m_e$ sector** in the corpus — no $m_c$ quark caveat (SF-3), no $\eta$ boson caveat (SF-2). State this plainly; it is the strongest single-calibration anchor for the SF-line.
- **Inherited-open:** **OPEN-FP-1-P3** (the Layer-B thermal-equilibration / Caldeira–Leggett system–bath model; resolution path SS-4). Empirically harmless ($\sim 10^{-20}$).
- **Scope boundary:** leptons only; quarks break Koide (10–27%). This boundary cleanly separates SF-1 from SF-3.
- **Derived as bonus:** $\sin^2\theta_W=3/(8\phi)$ (Part B) — an intermediate result, not a charged-lepton observable, but a strong zero-parameter correspondence to foreground.

---

## F. Forward note (next phase — Thomas-driven)

This core is ready to transfer into `sf-1_charged_leptons.tex`. The remaining work is **assembly + review, not derivation**:
1. Wrap §1 (the charged-lepton mass problem) and §2 (substrate + axioms + tetrahedral cage) around this core.
2. Add §9 falsifiers and §10 SF-line placement (hooks to SF-2 via shared $\sin^2\theta_W$; SF-4 via shared $M_0$ + OP-SM-7d).
3. Compile, then run the multi-AI review cycle (ChatGPT/Grok/Copilot) per SF-line discipline.
4. Register OPEN-FP-1-P3 via a flagged integration patch at ship time.

Estimated 3–5 sessions to v1.0 from this core, consistent with `sf-1_outline.md` §8.

---

## G. Collision-coordination

New staging file under `flagship_papers/charged_leptons/sketches/` — **no shared-registry edits, no other window's files touched, no δ_CP/window-5 adjacency, no window-2 adjacency**. Pure reframing of shipped SM-3/4/6. Collision-free. OPEN-FP-1-P3 registration is deferred to SF-1 ship via a flagged integration patch.

---

*Patch 1307 — SF-1 structural-derivation core (K3 theorem + Weinberg intermediate + Koide phase arc + mass spectrum). Reframing of shipped SM-3/4/6; no new derivation; no physics verdicts moved; no registries touched. New file under `flagship_papers/charged_leptons/sketches/`, collision-free.*
