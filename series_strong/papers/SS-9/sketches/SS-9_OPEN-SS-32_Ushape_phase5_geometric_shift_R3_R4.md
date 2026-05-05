# SS-9 OPEN-SS-32 ↔ U-shape unification — Phase 5 geometric-shift scoping (R3, R4)

**Date:** 5 May 2026 (Session 17)
**Status:** **PASSES SCOPING** — first non-rule-out outcome in five sequential phases of the OPEN-SS-32 ↔ U-shape thread.
**Strengthening:** F1 sign analytical check was applied **first**, before computation, per the methodology lesson registered in the 0184 handover (Phase 4 close). Both R3 and R4 pass F1 by Gaussian symmetry within one paragraph; computation was for F2 magnitude capacity and F3 pattern monotonicity.
**Companion script:** `series_strong/papers/SS-9/scripts/SS-9_OPEN-SS-32_Ushape_phase5_geometric_shift_R3_R4.py`.

---

## 1. Strategy

Phase 4 (Session 16) formally closed the Gaussian-K$_3$ framework at fixed cluster geometry via the §2.4 sign theorem on $f(s) = (1+s)^{-1/2} - 1 + s/2 > 0$ for $s > 0$, combined with Rayleigh–Ritz: any perturbative or variational improvement of the harmonic K$_3$ ground-state estimate at canonical geometry produces *more* binding. The empirical U-shape needs *less* binding. The U-shape mechanism therefore cannot live within the Gaussian-K$_3$ framework at fixed cluster geometry.

Phase 5 attacks the U-shape question via the natural channel that Phase 4 left open: cluster-geometry shift mechanisms beyond R1. Two channels were registered in the Phase 4 handover (§6.1):

- **R3.** Uniform cluster-radius shift $R_\alpha(N) = R_{\rm canon} + \delta R(N)$ driven by N-dependent boundary conditions — Coulomb cluster repulsion, Pauli blocking at internal contacts, surface effects beyond R1's surface-tension form, etc.
- **R4.** Cluster shape distortion: J-solid geometry minimizes pair-K$_3$ energy assuming uniform edge length, but with anisotropic perturbations the equilibrium shape may distort with non-uniform edge lengths, breaking the rigid-J-solid assumption.

The Phase 4 lesson — registered as a methodology sharpening in the 0184 handover — is that **the analytical sign check should be F1 by default in any scoping investigation**, applied *before* computational work. Phase 4's result was decided by an analytical sign argument that could have been pre-empted in one paragraph; the same kind of argument should be the first move in any new scoping.

## 2. Pre-empted analytical sign analysis (F1)

The K$_3$ pair potential $V_{\rm pair}(\delta r) = -B_{\rm pair} \exp(-\delta r^2/(2\sigma^2))$ is **symmetric in $\delta r$ around equilibrium**. For any displacement $\delta r \neq 0$ (R3 uniform shift) or any non-zero edge distortion $\epsilon$ (R4):

$$ \boxed{\; \Delta V_{\rm edge} \;=\; B_{\rm pair} \cdot \bigl[\, 1 - \exp(-\delta r^2/(2\sigma^2)) \,\bigr] \;>\; 0 \quad \text{for any } \delta r \neq 0. \;} $$

Positive for any sign of $\delta r$ (compression or expansion), positive for any sign of $\epsilon$. The empirical J-solid range needs $\Delta E > 0$ (cluster wants to grow → empirical binding less than canonical K$_3$). **F1 PASSES universally for any geometric shift.**

### 2.1 Sign-orthogonal contrast with Phase 4

Phase 4's anharmonic $\xi^4$ correction had $\Delta E < 0$ universally by Wick's theorem ($\langle \xi^4 \rangle_0 = 3 \langle \xi^2 \rangle_0^2 > 0$ combined with negative Taylor coefficient). Phase 5's geometric shift has $\Delta E > 0$ universally by Gaussian symmetry. **The two Gaussian-K$_3$ extension classes are sign-orthogonal:** Phase 4 was forced to fail F1, Phase 5 passes F1, both by structural properties of the same Gaussian function. The closure of one class motivates the opening of the other.

### 2.2 What this analytical argument says and does not say

The sign theorem for R3/R4 says: *if* the cluster equilibrium shifts by $\delta R(N) \neq 0$ from canonical, the K$_3$ Gaussian binding component decreases — sign-compatible with empirical U-shape. It does *not* say which $\delta R(N)$ is physically realized; that depends on the **driving physics** $V_{\rm other}$ that, together with K$_3$, sets the cluster equilibrium. Phase 5 scoping addresses sign and magnitude *capacity*; the next phases must specify $V_{\rm other}$ from CPP first principles.

## 3. Computational scoping

### 3.1 R3 with empirical $R_{\rm pct}$ values (R3-emp)

Direct test: use the empirical $R_{\rm pct}$ values from Session 12 (R1 inversion of $\hbar\omega^*$ scaling) as $\delta R(N) = (R_{\rm pct}/100) \cdot R_{\rm canon}$ and compute K$_3$ binding loss.

| $N$ | sym | $\lvert E\rvert$ | $R_{\rm pct}$ % | $\delta R$ [fm] | $\delta R/\sigma$ | $\Delta E_{R3}$ [MeV] | $\Delta E/\alpha$ [MeV] | $\Delta E/B_{K3}$ % |
|-----|-----|------|------|--------|-------|---------|---------|---------|
|  4 | $T_d$    |  6 | $-10.40$ | $-0.247$ | $-0.147$ | $0.150$ | $0.038$ |  $1.07$ |
|  5 | $D_{3h}$ |  9 | $+14.60$ | $+0.346$ | $+0.206$ | $0.442$ | $0.088$ |  $2.10$ |
|  6 | $O_h$    | 12 | $+12.70$ | $+0.301$ | $+0.179$ | $0.448$ | $0.075$ |  $1.59$ |
|  7 | $D_{5h}$ | 15 | $+19.10$ | $+0.453$ | $+0.269$ | $1.253$ | $0.179$ |  $3.57$ |
|  8 | $D_{2d}$ | 18 | $+21.10$ | $+0.500$ | $+0.298$ | $1.827$ | $0.228$ |  $4.33$ |
|  9 | $D_{3h}$ | 21 | $+22.30$ | $+0.529$ | $+0.315$ | $2.375$ | $0.264$ |  $4.83$ |
| 10 | $D_{4d}$ | 24 | $+22.70$ | $+0.538$ | $+0.320$ | $2.810$ | $0.281$ |  $5.00$ |
| 12 | $I_h$    | 30 |  $-0.70$ | $-0.017$ | $-0.010$ | $0.003$ | $0.000$ |  $0.01$ |

R3-emp ratios in the J-solid range against $|d_{\rm emp}|$ are **0.04–0.15** — R3-emp delivers only $\sim 10$–15 % of the prior-thread $-d_{\rm emp}$ scale. This is **expected and not a falsifier**: the $-d_{\rm emp}$ scale was originally derived from inversion of empirical $\hbar\omega^*$ scaling and represents an $\hbar\omega^*$-equivalent dimensionless shift, not a binding deficit. The K$_3$ binding-loss signal from R3-emp is in a different normalization than $-d_{\rm emp}$ and the two should not be expected to numerically agree; the comparison nonetheless shows that R3 with the $\hbar\omega^*$-derived $R_{\rm pct}$ values does *not* produce binding shifts of the $-d_{\rm emp}$ magnitude.

### 3.2 R3 magnitude capacity

The maximum K$_3$ binding loss at $N = 10$ is $|E| \cdot B_{\rm pair} = 24 \cdot 2.342 = 56.2$ MeV total = $5.62$ MeV/α, achieved when $\delta R \to \infty$ and the K$_3$ Gaussian is driven to zero. Empirical alpha-cluster binding deficit is on the order of $\sim 1$ MeV/α. **R3 magnitude capacity is far larger than the empirical signal**; the bottleneck is which $\delta R(N)$ is physically realized, not whether R3 has enough magnitude.

### 3.3 R3 with linear-in-N parameterization (R3-lin)

Calibrated parameterization $\delta R(N) = \alpha (N - 4)$ with $\alpha$ chosen so that $\Delta E/\alpha = 1$ MeV at $N = 10$. Solving: $24 B_{\rm pair} (1 - \exp(-\delta R^2/(2\sigma^2))) / 10 = 1$ gives $\alpha = 0.1753$ fm/(N-4 unit), i.e. $\delta R(10) = 1.05$ fm $= 44.4$% of $R_{\rm canon}$.

| $N$ | sym | $\delta R$ [fm] | $\delta R/\sigma$ | $\Delta E_{R3}$ [MeV] | $\Delta E/\alpha$ [MeV] | $\Delta E/B_{K3}$ % |
|-----|-----|--------|-------|---------|---------|---------|
|  4 | $T_d$    | $0.000$ | $0.000$ |  $0.000$ | $0.000$ |  $0.00$ |
|  5 | $D_{3h}$ | $0.175$ | $0.104$ |  $0.114$ | $0.023$ |  $0.54$ |
|  6 | $O_h$    | $0.350$ | $0.209$ |  $0.605$ | $0.101$ |  $2.15$ |
|  7 | $D_{5h}$ | $0.526$ | $0.313$ |  $1.679$ | $0.240$ |  $4.78$ |
|  8 | $D_{2d}$ | $0.701$ | $0.417$ |  $3.515$ | $0.439$ |  $8.34$ |
|  9 | $D_{3h}$ | $0.876$ | $0.522$ |  $6.256$ | $0.695$ | $12.72$ |
| 10 | $D_{4d}$ | $1.052$ | $0.626$ | $10.000$ | $1.000$ | $17.79$ |
| 12 | $I_h$    | $1.402$ | $0.835$ | $20.664$ | $1.722$ | $29.41$ |

The $44.4$ % relative shift at $N = 10$ is large but not unphysical — the actual cluster radii of alpha-cluster nuclei *do* change significantly with $A$, and a $44$ % equilibrium shift is consistent with strong-Coulomb-driven expansion in a $\sim 2$ fm scale. **R3-lin is a viable parameterization**; what remains is to derive $\alpha$ from CPP physics.

### 3.4 R4 with constant $\epsilon_{\rm rms}$ (R4-flat)

Each edge gets independent Gaussian-distributed displacement $\epsilon$ with $\langle \epsilon^2 \rangle = \epsilon_{\rm rms}^2$ constant across all polytopes. Per-edge averaged binding loss:

$$ \langle \Delta V_{\rm edge} \rangle_{\rm Gauss} \;=\; B_{\rm pair} \cdot \biggl[\, 1 - \frac{1}{\sqrt{1 + \epsilon_{\rm rms}^2/\sigma^2}} \,\biggr]. $$

For $\epsilon_{\rm rms} = 0.10 \cdot R_{\rm canon} = 0.237$ fm:

| $N$ | sym | $\langle \Delta E_{R4} \rangle$ [MeV] | $\langle \Delta E/\alpha \rangle$ [MeV] | $\langle \Delta E/B_{K3} \rangle$ % |
|-----|-----|--------|--------|--------|
|  4 | $T_d$    | $0.138$ | $0.034$ | $0.98$ |
|  5 | $D_{3h}$ | $0.207$ | $0.041$ | $0.98$ |
|  6 | $O_h$    | $0.276$ | $0.046$ | $0.98$ |
|  7 | $D_{5h}$ | $0.345$ | $0.049$ | $0.98$ |
|  8 | $D_{2d}$ | $0.413$ | $0.052$ | $0.98$ |
|  9 | $D_{3h}$ | $0.482$ | $0.054$ | $0.98$ |
| 10 | $D_{4d}$ | $0.551$ | $0.055$ | $0.98$ |
| 12 | $I_h$    | $0.689$ | $0.057$ | $0.98$ |

The fractional shift $\langle \Delta E/B_{K3} \rangle = 0.98$% is **constant across all polytopes** — universal R4 distortion produces a per-edge effect, with cluster-total scaling as $|E| \cdot \langle \Delta V \rangle$ purely. The total $\langle \Delta E \rangle$ is monotonic in $N$ via $(3N-6)$ scaling; per-alpha $\langle \Delta E/\alpha \rangle = (3N-6)/N \cdot \langle \Delta V \rangle$ is also monotonic in $N$ but slowly increasing (factor $1.8 \to 2.4$ across the J-solid range).

R4-flat with $\epsilon_{\rm rms} = 0.237$ fm gives $\sim 0.05$ MeV/α at $N = 10$, $\sim 20\times$ smaller than the typical empirical deficit $\sim 1$ MeV/α. Larger $\epsilon_{\rm rms}$ would close the gap; e.g. $\epsilon_{\rm rms} = 1$ fm (42% of $R_{\rm canon}$) gives roughly $1$ MeV/α at $N = 10$.

### 3.5 R4 with N-linear $\epsilon_{\rm rms}(N)$ (R4-Nlin)

If shape complexity grows with $N$, distortion amplitude can grow too. Parameterize $\epsilon_{\rm rms}(N) = \beta (N - 4)/6$ with $\beta = 0.237$ fm so that $\epsilon_{\rm rms}(10) = 0.237$ fm (10 % of $R_{\rm canon}$).

In this parameterization, the per-alpha shift grows substantially in N (small clusters feel little distortion, large clusters feel more). Numerically: $\langle \Delta E_{R4}/\alpha \rangle$ grows from $0$ at $N = 4$ to $\sim 0.055$ MeV/α at $N = 10$ — same magnitude as R4-flat at $N = 10$ but with sharper N-dependence.

### 3.6 F3 pattern analysis

| $N$ | R3-lin $\Delta E/\alpha$ [MeV] | R4-flat $\langle \Delta E/\alpha \rangle$ [MeV] |
|-----|----------------------|-------------------------|
|  5 | 0.023 | 0.041 |
|  7 | 0.240 | 0.049 |
|  8 | 0.439 | 0.052 |
|  9 | 0.695 | 0.054 |
| 10 | 1.000 | 0.055 |

Both **R3-lin** ($N$-driven $\delta R$) and **R4-flat** (constant $\epsilon_{\rm rms}$, $|E|$-driven via $(3N-6)/N$) produce monotonically increasing $|\Delta E/\alpha|$ across the J-solid range. **F3 PASSES for both.** The functional shape differs (R3-lin grows faster because $\delta R$ grows linearly with $N$; R4-flat grows slowly because only $(3N-6)/N$ matters), and matching the empirical N-dependence will discriminate between them at the next level of investigation.

## 4. Verdict — POSITIVE SCOPING

### 4.1 Three falsifier outcomes

- **F1 (sign): PASSES** universally and analytically by Gaussian symmetry. R3 and R4 both pass F1 by the same mechanism that closed Phase 4 — symmetry of the K$_3$ Gaussian about its peak. Sign-orthogonal to Phase 4's anharmonic ξ⁴ closure.
- **F2 (magnitude capacity): PASSES**. Both R3 and R4 have ample magnitude capacity within the K$_3$ framework. R3's maximum binding loss capacity is $5.62$ MeV/α at $N = 10$, well above empirical $\sim 1$ MeV/α scale. R4 with reasonable $\epsilon_{\rm rms}$ delivers $\sim 0.05$–$1$ MeV/α. The bottleneck is which $\delta R(N)$ or $\epsilon_{\rm rms}(N)$ is physically realized by CPP physics, *not* whether magnitude is achievable.
- **F3 (pattern): PASSES** for any monotonic $\delta R(N)$ or $\epsilon_{\rm rms}(N)$ parameterization. Both R3-lin and R4-flat give monotonic-in-$N$ patterns within the J-solid range.

### 4.2 First non-rule-out outcome in five sequential phases

This is the **first non-rule-out outcome in five sequential phases** of the OPEN-SS-32 ↔ U-shape investigation:

| Phase | Mechanism | Status |
|-------|-----------|--------|
| Phase 2 | Uniform-only zero-point softening | RULED OUT (Session 13) |
| Phase 3A | Naive full-Hessian | RULED OUT (Session 13) |
| Phase 3B-A | Fixed-dim belt subspace | RULED OUT (Session 14) |
| Phase 3B-B | Full $C_n$ IRREP decomposition | RULED OUT — R2 FORMALLY CLOSED (Session 15) |
| Phase 4 | Anharmonic $\xi^4$ + all-orders Gaussian | RULED OUT — Gaussian-K$_3$ framework at fixed geometry FORMALLY CLOSED (Session 16) |
| **Phase 5** | **Geometric shift R3 + R4** | **PASSES SCOPING (Session 17)** |

Phases 2–4 systematically eliminated all mechanisms within the Gaussian-K$_3$ framework at fixed canonical geometry. Phase 5 advances to the natural complement: cluster-geometry shift channels. The fact that the channels Phase 4 left open turn out to pass scoping at F1/F2/F3 levels is **structurally consistent with the closure pattern** — the Gaussian symmetry that forced Phase 4's closure (negative ΔE) forces Phase 5's positive ΔE in the geometric-shift framing.

### 4.3 What "PASSES SCOPING" means and does not mean

**Phase 5 does not claim to derive the U-shape mechanism.** It establishes only that R3 and R4 are *channel-compatible* — sign matches, magnitude capacity is sufficient, and pattern is monotonic in $N$ for natural parameterizations. **The actual physics that sets $\delta R(N)$ or $\epsilon_{\rm rms}(N)$ from CPP first principles is not specified in Phase 5** and is the subject of subsequent multi-session investigations.

In the scoping methodology of the OPEN-SS-35 closure programme (cf. `templates/operating_system.md` §15), passing scoping advances a candidate to multi-session derivation status without rule-out; subsequent sessions specify, compute, and test against more stringent empirical constraints (e.g., quantitative pattern matching, not just monotonicity).

## 5. Programme implications

### 5.1 Negative-result count and OPEN-SS-35 trajectory

No new negative result in Session 17. The cumulative count remains **10 programme-level negative results** (Phase 4 was the tenth, Session 16). OPEN-SS-35 stages preserved at 6. Pattern 6 K$_3$ scale-recurrence at 7 confirmed instances unchanged. R2 remains formally closed (Session 15). Gaussian-K$_3$ framework at fixed cluster geometry remains formally closed (Session 16).

OPEN-SS-35 sub-question (a) A-scaling closure now has Phase 5 R3 and R4 channels under active scoping investigation — the first time since Session 12's R1 closure that the sub-question has a non-ruled-out candidate.

### 5.2 Constructive content from Phase 5

Phase 5's content is constructive in three ways:

- **Sign-orthogonal closure pattern.** Phase 4 closed negative-ΔE mechanisms (perturbative correction at any order in the Gaussian expansion); Phase 5 opens positive-ΔE mechanisms (geometric shift at any non-zero $\delta R$). The two are both consequences of the same Gaussian function — its symmetry. The closure of one class systematically opens the other.
- **Magnitude capacity of R3 / R4.** $5.62$ MeV/α maximum at $N = 10$, far above empirical $\sim 1$ MeV/α. The Gaussian-K$_3$ framework's geometric-shift response has plenty of energetic room; CPP physics constraints (e.g., realistic Coulomb / Pauli driving forces) will typically realize a much smaller fraction of this maximum, but the framework permits any required value.
- **R3-lin calibration as scale.** $\alpha = 0.175$ fm/(N-4 unit) gives $\delta R(N=10) = 1.05$ fm $= 44.4$% of $R_{\rm canon}$ to deliver $1$ MeV/α at $N = 10$. This sets the natural scale of $\delta R$ that the V$_{\rm other}$ physics must produce — substantially larger than the $\hbar\omega^*$-derived $R_{\rm pct}$ values (which gave $\delta R(10) = 0.54$ fm). The Phase 5 calibration gives a target for any future first-principles derivation.

### 5.3 Methodology lesson reinforced

The Phase 4 lesson — **F1 sign analytical check first, before computation** — was applied in Phase 5 from the outset. The analytical sign argument took one paragraph and decided F1 universally before any code was written. The computational scoping was for F2 magnitude capacity and F3 pattern monotonicity only.

This methodology should be the default for any future scoping investigation in the programme. For Gaussian-K$_3$-framework-related questions specifically: any positive-ΔE candidate passes F1 trivially via the Gaussian-symmetry argument; any negative-ΔE candidate is ruled out by Phase 4's sign theorem. **The Gaussian function's symmetry has effectively partitioned the OPEN-SS-32 candidate space into "ruled out" (Phase 4 closure) and "open at scoping" (Phase 5 channels) by sign.**

## 6. Forward pointers

### 6.1 New Priority 1 (multi-session derivation)

**Identify $\delta R(N)$ functional form from CPP first principles.** Candidate physics, each requiring multi-session derivation:

- **(R3-Coulomb)** Cluster Coulomb repulsion: $V_C \sim Z^2/A^{1/3}$ pushes $R_\alpha$ outward. CPP-derivable from charge structure of alpha clusters on the 600-cell lattice. Predicts $\delta R(N)$ pattern via dependence on $Z(N) = 2N$ and overall cluster geometry.
- **(R3-Pauli)** Pauli blocking at internal alpha-alpha contacts: scales with edge count, monotonic in $N$. CPP-derivable from Pauli operator on alpha-cluster wavefunctions.
- **(R3-surface)** Surface-density form (NOT R1 surface-tension form, which was ruled out Session 12). Alternative surface-coupling mechanisms remain.
- **(R4-shape)** Spin-orbit cluster contributions with shape dependence; or other anisotropic mechanisms that drive non-uniform edge distortion.

Each is a multi-session derivation. The natural Session 18 first move is **R3-Coulomb scoping**: compute the Coulomb-driven equilibrium $\delta R(N)$ using a simplified CPP charge model, compare to the Phase 5 R3-lin calibration ($\delta R(10) \approx 1$ fm), and assess whether Coulomb alone, Pauli alone, or both together come close.

### 6.2 New Priority 2 (parallel, registered)

**Inelastic / out-of-framework channels** — Hoyle-state mixing, surface-energy shape dependence, Coulomb cluster-arrangement effects at the level of electromagnetic geometry beyond uniform repulsion. These were registered in the Phase 4 handover §6.2 and remain on the table; less natural Priority 1 than R3-physics-derivation because the geometric-shift channel (R3, R4) is more direct and has known sign/magnitude/pattern compatibility from Phase 5 scoping.

### 6.3 Anti-priorities (sharpened from Phase 4)

- Do **not** initiate SS-9 v0.3 → v0.1 `.tex` conversion (OPEN-ORG-012). §7 needs reformulation reflecting Phase 5's positive scoping result on top of Phase 4's framework closure on top of Phase 3B-B's R2 closure. **§7 has now shifted seven times in the OPEN-SS-32 ↔ U-shape thread** (Phase 1 prior-art read; Phase 2 ruled out; Phase 3A ruled out + bracketing; Phase 3B-A ruled out + pattern-shape constraint; Phase 3B-B ruled out + R2 formal closure; Phase 4 ruled out + Gaussian-K$_3$ framework closure via sign theorem; **Phase 5 PASSES SCOPING + R3/R4 channels open + multi-session derivation pending**).
- Do **not** pursue further perturbative anharmonic refinement within Gaussian-K$_3$ at fixed geometry — universally closed by Phase 4 §2.4 sign theorem.
- Do **not** pursue further belt-IRREP-projection variants — closed Phase 3B-B.
- Do **not** pursue full point group $D_{nh}/D_{nd}$ extension — closed Phase 3B-B.
- Do **not** pursue further $V_{\rm SO}$ refinement within simple K$_3$ + HO + L·S framework.
- Do **not** pursue further $R_\alpha(A)$ in the specific surface-tension form (R1, Session 12).
- Do **not** parameterize $\delta R(N)$ phenomenologically without grounding in CPP physics. The Phase 5 R3-lin calibration is a target for first-principles derivation, not a model to be fit.

## 7. Summary

Phase 5 applied the F1 analytical sign check first, per the methodology lesson registered in the Phase 4 (Session 16) handover. Both R3 (uniform $R_\alpha$ shift) and R4 (cluster shape distortion) **pass F1 universally** by Gaussian symmetry of the K$_3$ pair potential — sign-orthogonal to Phase 4's $\Delta E < 0$ closure, with the same Gaussian function generating both signs in different framings. Computational scoping established F2 magnitude capacity (well in excess of empirical $\sim 1$ MeV/α scale) and F3 pattern monotonicity (passes for any monotonic $\delta R(N)$ or $\epsilon_{\rm rms}(N)$).

**First positive scoping result in five sequential phases.** R3 and R4 advance to multi-session derivation status. The next investigation is to identify $\delta R(N)$ from CPP physics — Coulomb, Pauli, surface-effects, spin-orbit cluster — and check whether the predicted geometric shift matches empirical sign / magnitude / pattern at quantitative level.

Programme state otherwise unchanged: 10 programme-level negative results; R2 formally closed; Gaussian-K$_3$ framework at fixed cluster geometry formally closed; Decoupling Theorem intact; sub-question (b) layer 3 gap-strength closure unaffected; Pattern 6 K$_3$ scale-recurrence at 7 instances unchanged.
