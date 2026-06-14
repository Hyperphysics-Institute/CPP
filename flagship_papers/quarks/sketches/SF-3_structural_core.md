# SF-3 Structural Core — Zero-Parameter Mass Spectrum · α_s Complementarity · Quark Koide Phase

**Location:** `/CPP/flagship_papers/quarks/sketches/SF-3_structural_core.md`
**Opened:** Session 160, Patch 1308 (SF-7 grand-unification window)
**Status:** STAGING DOCUMENT — the structural-derivation core (§3–§5 of the SF-3 outline) worked out for direct `.tex` transfer. Reframing of shipped SM-7/8/9 + SS-2; no new derivation. Full `.tex` assembly + multi-AI review is the Thomas-driven next phase.
**Source (all shipped):** SM-8 v4.0 (zero-param mass formula), SM-9 (7/3 exponent + M₀), SM-7 (α_s + quark Koide phase), SS-2 (C_F=4/3).
**Sharpens:** the 1303 calibration recommendation (see Part C — no "re-grounding on derived m_c" is needed).

---

## 0. What this document delivers

The SF-3 load-bearing core, with all numbers verified:
- **Part A (→ §3):** the zero-parameter quark mass spectrum from $m_e$ alone (Route A; m_c demoted to derived).
- **Part B (→ §4):** $\alpha_s = 5/(8\phi)$ and the electroweak–strong mode complementarity.
- **Part C (→ §5):** the quark Koide phase $\theta=124.04°$ — and the **clean separation** of mass route from phase derivation that resolves the calibration question.
- **Part D (→ §6):** three generations forced; no fourth quark.
- **Part E (→ §8):** the CKM gap (inherited-open).
- **Part F:** the honest ledger.

---

## A. Zero-parameter mass spectrum (→ §3) — single $m_e$, m_c derived

**The formula (SM-8; exponent 7/3 and prefactor $M_0$ derived in SM-9):**
$$M_q = m_e\,\frac{z}{\phi}\,V^{7/3}\quad(q=s,c,b);\qquad M_t = m_e\,\frac{z}{\phi}\,V_t^{7/3}\times z\,C_F,$$
with $M_0 = m_e\,z/\phi = 3.79$ MeV, $z=12$, $C_F = 4/3$ (SS-2), and the top relay multiplier $z\,C_F = 16$. The four bonded shells of the 600-cell give the quark cage assignments:

| Quark | Shell | $V$ | multiplier | CPP mass | PDG | error |
|-------|-------|-----|-----------|----------|-----|-------|
| strange | tetrahedron | 4 | 1 | 96.3 MeV | 93.4 | +3.1% |
| charm | icosahedron | 12 | 1 | 1249 MeV | 1270 | −1.6% |
| bottom | dodecahedron | 20 | 1 | 4115 MeV | 4180 | −1.6% |
| top | icosidodecahedron | 30 | $zC_F=16$ | 169,571 MeV | 172,760 | −1.8% |

**RMS 2.1%** across four orders of magnitude, **from $m_e$ + geometry + SU(3) colour alone**. No parameters fitted.

**Calibration resolution (the 1300 §2 / 1303 question):** because this formula *predicts* $m_c = 1249$ MeV (−1.6%), **m_c is a derived quantity, not a calibration.** Adopting this route as canonical for the mass spectrum **restores the single-$m_e$ calibration** for all quark masses. The SF-7 §9 master table reads 1 calibration ($m_e$).

---

## B. α_s and electroweak–strong complementarity (→ §4)

The strong coupling is the *face-mode* fraction of the same 600-cell spectral trace that gives the Weinberg angle:
$$\alpha_s = \frac{1}{\phi}\cdot\frac{\tfrac{1}{3}\mathrm{Tr}(A^3)}{\mathrm{Tr}(A^2)+\tfrac{1}{3}\mathrm{Tr}(A^3)} = \frac{1}{\phi}\cdot\frac{2400}{3840} = \frac{5}{8\phi} \approx 0.386,$$
matching the PDG running coupling at the charm scale ($\alpha_s(m_c)\approx 0.35$–0.40). The two mode fractions are **complementary**:
$$\sin^2\theta_W + \alpha_s = \frac{3}{8\phi} + \frac{5}{8\phi} = \frac{1}{\phi} \approx 0.618,$$
with the bare (pre-$\eta$) partition $3/8 + 5/8 = 1$ and the topological ratio $\alpha_s/\sin^2\theta_W = F/E = 5/3$. **One spectral trace gives both the electroweak and the strong coupling** — a genuine substrate-level unification, and the strongest §10 thread to SF-1, SF-2, SF-5.

---

## C. The quark Koide phase (→ §5) — and why no "re-grounding" is needed

**The phase derivation (SM-7).** The base value is the K3 eigenvalue ratio (cf. SF-1 Part A): $\cos\theta_0 = -K = -2/3$. Quarks carry colour, so their K3 cage faces feel the strong coupling on all $z=12$ nearest-neighbour bonds, producing a negative isotropic shift, alongside the same electroweak shift the leptons feel:
$$\varepsilon_S = -\frac{z\,\alpha_s}{z+1} = -\frac{60}{104\phi},\qquad \varepsilon_{EW} = +\frac{3}{52\phi},\qquad \varepsilon = \varepsilon_S+\varepsilon_{EW} = -\frac{27}{52\phi}.$$
$$\cos\theta_{\rm quark} = -\frac{2}{3}\left(1 + \frac{\varepsilon}{2}\right) = -\frac{2}{3}\left(1 - \frac{27}{104\phi}\right) \approx -0.5597 \;\Rightarrow\; \boxed{\theta_{\rm quark} = 124.04°}$$
vs PDG $124.09°$ — **0.05%**.

**The sharpening (resolves the 1303 wording).** Patch 1303 recommended "re-grounding SM-7's phase machinery on the derived m_c." Worked out, **that step is unnecessary**: the phase $\theta_{\rm quark}$ is built **entirely from $\alpha_s$, $\sin^2\theta_W$, and $z$** (the isotropic-shift structure) — it does **not** depend on the mass amplitude or on m_c at all. m_c entered SM-7 only as the *mass-amplitude* calibration $A_q$; the *phase* is a clean derived structural observable independent of the mass route.

So the clean SF-3 synthesis is **simpler** than 1303's hybrid:
> **Masses** come entirely from SM-8 (Route A, single $m_e$). **The quark Koide phase $\theta_{\rm quark}=124.04°$ and $\alpha_s=5/(8\phi)$** come from SM-7 as **derived structural observables independent of any mass calibration.** No re-grounding, no hybrid, no m_c calibration anywhere — masses from the cage formula, phase from the shift structure.

The phase is itself a zero-parameter prediction (0.05%) checkable against the PDG-quark-mass-extracted phase, and it stands whichever mass route is used.

---

## D. Three generations (→ §6)

The four bonded shells $V\in\{4,12,20,30\}$ exhibit palindrome symmetry, and **antipodal identification in the tessellated lattice limits the Standard Model to exactly three generations.** This forces three generations (not assumed) and predicts **no fourth quark** — a zero-parameter structural prediction and a clean falsifier.

---

## E. The CKM gap (→ §8) — inherited-open

There is **no CKM-matrix derivation anywhere in the quark corpus** (SM-10 is the FEM scaling-*mechanism* paper, not a mixing paper). Register **OPEN-FP-3-CKM** and inherit. This is the structural **analog of SF-4's open δ_CP**: SF-3 ships the quark masses + generation count at zero parameters with CKM mixing deferred. State the parallel explicitly — it gives the SF-line a uniform "masses derived, mixing-sector open" posture. Candidate forward route (flag, do not pursue): a quark-sector cage-mixing structure analogous to SM-5's K3 → TBM derivation of PMNS.

*Note:* CKM is **not** window-5 territory (window 5 = neutrino δ_CP); the quark CP phase inside CKM is a separate object.

---

## F. Honest calibration / inheritance ledger (→ §7–§8)

- **Calibration:** one constant, $m_e$. **Zero shape parameters.** m_c, m_s, m_b, m_t all derived (SM-8). α_s and $\theta_{\rm quark}$ derived (SM-7).
- **Inherited-open:** **OPEN-FP-3-CKM** (quark mixing); SM-10's first-principles cascade derivation still calibrated (4 params/4 data) pending GPU closure — the *mass values* do not depend on it (they come from SM-8/SM-9), so this is a mechanism-depth caveat, not a mass-prediction caveat.
- **Accuracy honesty:** RMS 2.1% on masses (single $m_e$). The Koide-route (SM-7) gave slightly better b/t (1.4–1.7%) but at the cost of an m_c calibration; the single-calibration spine is worth the ~0.3% trade (per 1303 §1).
- **Structural wins to foreground:** the $\alpha_s$/$\sin^2\theta_W$ complementarity (1/φ), the quark phase at 0.05%, and the forced three-generation count.

---

## G. Forward note (next phase — Thomas-driven)

Ready to transfer into `sf-3_quarks.tex`. Remaining work is **assembly + review**:
1. Wrap §1 (the quark mass problem) and §2 (substrate + four shells + SU(3) colour) around this core.
2. Add §7 calibration ledger (the route adjudication), §8 CKM honesty, §9 falsifiers (4th-generation, α_s running), §10 SF-line placement.
3. Compile, then run the multi-AI review cycle.
4. Register OPEN-FP-3-CKM via a flagged integration patch at ship time.

Estimated 5–7 sessions to v1.0 from this core, per `sf-3_outline.md` §8.

---

## H. Collision-coordination

New staging file under `flagship_papers/quarks/sketches/` — **no shared-registry edits, no other window's files touched, no δ_CP/window-5 adjacency** (CKM ≠ neutrino δ_CP), **no window-2 adjacency**. Pure reframing of shipped SM-7/8/9 + SS-2. Collision-free. OPEN-FP-3-CKM registration deferred to SF-3 ship via a flagged integration patch.

---

*Patch 1308 — SF-3 structural-derivation core (zero-param spectrum + α_s complementarity + quark Koide phase + 3 generations + CKM gap). Reframing of shipped SM-7/8/9 + SS-2; sharpens the 1303 calibration recommendation (no re-grounding needed). No new derivation; no physics verdicts moved; no registries touched. New file under `flagship_papers/quarks/sketches/`, collision-free.*
