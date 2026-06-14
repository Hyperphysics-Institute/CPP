# SF-5 Structural Core — SU(3) Exact · Eight Gluons · Confinement · Nuclear Cascade

**Location:** `/CPP/flagship_papers/strong/sketches/SF-5_structural_core.md`
**Opened:** Session 160, Patch 1309 (SF-7 grand-unification window)
**Status:** STAGING DOCUMENT — the structural-derivation core (§3–§7 of the SF-5 outline) assembled for `.tex` transfer. Reframing of shipped SS corpus; no new derivation. Full `.tex` + multi-AI review is the Thomas-driven next phase.
**Source (all shipped):** SS-1b (SU(3) algebra), SS-1c (8 gluons), SS-1d (confinement/β), SS-3 (SU(3) uniqueness), SS-4 (string tension), SS-5 (light-nuclei cascade), SS-7 (alpha-cluster 3N−6 formula), SM-7 (α_s), SS-2 (C_F).
**Corrects:** the deuteron figure carried in 1304/1306 (see Part E — honest fix).

---

## 0. What this delivers + one honest correction

The SF-5 load-bearing core, with the gluon-counting emphasis decided in 1304 (lead with shipped theorem-level results). **One correction to earlier patches:** 1304/1306 listed the deuteron as "2.222 MeV, ~0.1%." That conflated the zero-parameter binding quantum with the NLO-corrected physical value. The honest figures are in Part E — the zero-parameter prediction is $B_{\rm pair}=M_0/\phi = 2.342$ MeV, and the 5.3% residual to the physical 2.224 MeV is an **open** NLO problem (SS-5 rejected the candidate derivation as not validated). Flagship credibility depends on stating this correctly.

---

## A. SU(3) exact and unique (→ §3)

**Exact (SS-1b).** Eight DI-bit hopping operators $T^a$ ($a=1,\dots,8$) on the tetrahedral cage base $\{V_1,V_2,V_3\}$ — six colour-changing (real/imaginary hopping along the three base edges) + two diagonal (phase differences) — satisfy
$$T^a = \lambda^a/2,\qquad [T^a,T^b] = if^{abc}T^c$$
with the **standard SU(3) structure constants** $f^{abc}$. SU(3)$_c$ is *derived*, not postulated.

**Unique (SS-3).** SU(3) emerges *uniquely* from the tetrahedral cage — the answer to "why SU(3) and not another gauge group." Together SS-1b + SS-3 are the strongest single result in the strong sector and the right flagship headline.

---

## B. The eight gluons (→ §4) — Picture 1, theorem-level

The eight gluons (SS-1c) are transient hDP configurations on the three base edges: **6 colour-changing** (hDP propagating along the three edges) + **2 colour-neutral diagonal** (phase-difference modes) = 8, 1-to-1 with the SU(3) octet. Properties derived from cage geometry:
- **Masslessness:** gluons are transient open-path hDP pairs with no confining closed subgraph → zero SSV compression energy → zero mass (exact parallel to the photon, the $\lambda=0$ DP-Sea mode).
- **Spin-1:** each base edge has a definite 3D orientation vector; the emitted hDP carries it.

**Gluon-counting recommendation (from 1304, restated):** lead with this Picture 1. Treat **CONJ-SS-Gluon-4Vertex** (8-as-dressing of a 4-vertex structure) as a flagged forward-looking conjecture in the open-work section — its own falsification route (a) collapses it to "SM restated" if enumeration yields 8, and Picture 1 arguably is that enumeration. Register attempts as OPEN-FP-5-GLUON.

---

## C. α_s and electroweak–strong complementarity (→ §6)

The strong coupling is the face-mode fraction of the same 600-cell spectral trace that gives the Weinberg angle (cf. SF-3 core Part B, SF-1 core Part B):
$$\alpha_s = \frac{1}{\phi}\cdot\frac{2400}{3840} = \frac{5}{8\phi}\approx 0.386,\qquad \sin^2\theta_W+\alpha_s=\frac{3}{8\phi}+\frac{5}{8\phi}=\frac{1}{\phi},\qquad \frac{\alpha_s}{\sin^2\theta_W}=\frac{F}{E}=\frac{5}{3}.$$
**One spectral trace, both couplings** — the substrate-level electroweak–strong unification. This is the strongest §10 thread binding SF-1/SF-2/SF-3/SF-5.

---

## D. Confinement and string tension (→ §5)

- **Confinement + β-function:** SS-1d derives the confinement mechanism and the QCD β-function from the cage structure (colour-charged objects cannot exist in isolation because the open-path hDP structure has no isolated-colour stable configuration).
- **String tension (SS-4):** from the 600-cell face-mode multiplicity,
$$\sigma = \frac{M_0\,z^2}{\phi\,\ell_{\rm edge}} \approx 926.5~\text{MeV/fm},$$
consistent with the lattice-QCD range. (This corrected SS-2's earlier heuristic $\sigma = M_0 z\pi/(\phi\,\ell_{\rm edge})$.)

---

## E. The nuclear-binding cascade (→ §7) — honest figures

The recurring **binding quantum** is
$$B_{\rm pair} = M_0/\phi = 2.342~\text{MeV}$$
(built from $M_0=m_e z/\phi$ and the $1/\phi$ propagation efficiency; **zero parameters**). It recurs across scales (SS-5/7/8 Pattern-6 scale recurrence). Honest sector results:

- **Deuteron (SS-5):** zero-parameter prediction $B_d = (M_0/\phi)(1-\epsilon_d)$ with leading order $M_0/\phi = 2.342$ MeV. The physical $B_d = 2.224$ MeV implies $\epsilon_d \approx 0.053$ — a **5.3% NLO residual registered as an open problem** (the candidate prolate-cage-distortion derivation was explored and **rejected as not validated** in SS-5 Appendix B). **Do not present the deuteron as a ~0.1% hit** — the zero-parameter content is the $2.342$ MeV binding quantum, with an honest 5.3% open residual.
- **Twelve N=Z alpha-chain nuclei (SS-7):** the closed alpha-polytope has $3N_\alpha-6$ edges, each contributing one $B_{\rm pair}$; the $3N_\alpha-6$ edge formula gives **twelve zero-parameter concurrent predictions** for strict-$N{=}Z$ nuclei at $N_\alpha\in[3,14]$, agreeing **below 1.5%** against AME 2020. This is the strong-sector's headline empirical anchor and is genuinely zero-parameter.

The honest summary: the *cascade* (twelve nuclei < 1.5%) is the strong zero-parameter result; the *deuteron* carries an open 5.3% NLO residual. Foreground the cascade, state the deuteron residual openly.

---

## F. Open items (→ §8) — inherit, do not headline

- **OPEN-SS-6 (glueball):** lightest scalar glueball as a closed tetrahedral hDP loop ($f_{\rm geom}$ on a closed loop); register OPEN-FP-5-GLUEBALL and inherit if not closed at SS-level.
- **SS-9 conditionality:** the simplicial-connectivity theorem is conditional on sub-conditions C5–C8 (OPEN-SS-29/30/33/37); inherit as conditional, do **not** present as unconditional.
- **Deuteron 5.3% NLO residual:** honest open (Part E).
- **CONJ-SS-Gluon-4Vertex:** flagged conjecture, not closed (Part B).

---

## G. Honest ledger (→ §7–§8)

- **Calibration:** $M_0 = m_e z/\phi$ anchors the nuclear-mass scale — single $m_e$, consistent with all other sectors. SU(3)/gluons/α_s carry **zero** mass parameters.
- **Strongest results to foreground:** SU(3) exact+unique; the twelve-nucleus cascade (<1.5%); α_s complementarity (1/φ).
- **Honest residuals:** deuteron 5.3% NLO (open); glueball (open); SS-9 conditionality; gluon-counting conjecture flagged.

---

## H. Forward note (next phase — Thomas-driven)

Ready to transfer into `sf-5_strong.tex`. Remaining work is **assembly + review** (+ optionally an OPEN-SS-6 glueball sub-derivation): wrap §1 (strong-sector problems) and §2 (tetrahedral cage substrate) around this core; add §9 falsifiers + §10 SF-line placement; compile; run the multi-AI review cycle. Estimated 5–8 sessions to v1.0 per `sf-5_outline.md` §8.

---

## I. Collision-coordination

New staging file under `flagship_papers/strong/sketches/` — **no shared-registry edits, no other window's files touched, no δ_CP/window-2/window-5 adjacency**. Pure reframing of shipped SS corpus. Collision-free. The deuteron-figure correction is internal to this window's own SF-5/map artifacts (a map fix can ride a later flagged patch if desired); no registry value was ever written for it.

---

*Patch 1309 — SF-5 structural-derivation core (SU(3) exact+unique + 8 gluons + α_s complementarity + confinement/string tension + nuclear cascade). Reframing of shipped SS corpus; corrects the 1304/1306 deuteron figure (zero-param = B_pair = M_0/φ = 2.342 MeV; physical 2.224 carries 5.3% open NLO). No new derivation; no physics verdicts moved; no registries touched. New file under `flagship_papers/strong/sketches/`, collision-free.*
