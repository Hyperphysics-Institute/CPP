# SF-4: Suppression Mechanism Derivation — Working Document

**Status:** ACTIVE — first substantive sub-derivation under OPEN-FP-SF-4-1
**Track:** SF-4 (Neutrino Sector Unification flagship paper) — suppression-factor derivation
**Author:** Claude Opus (analysis), Thomas Lee Abshier ND (strategic frame and physical intuition)
**Established:** 9 May 2026 (Session 40, patch 0299)
**Foundation:** [`SF-4_mechanism_selected.md`](SF-4_mechanism_selected.md) §2.5, §7.2, §8.1; [`SF-4_neutrino_sector_audit.md`](SF-4_neutrino_sector_audit.md) §3.4 (DP-type taxonomy), §4.1 (archived $\sigma = 120^{-d}$ analysis), §15 (falsifier-check)
**Scope:** Working document; sub-derivation under construction. Will accrete intermediate states across Sessions 40–42 (or longer if sub-conditions open). Captures both substantive results and dead ends. Per the four-tier discipline, this is a sketches-tier document; theorem-tier formalization happens at v0.1 SF-4 paper drafting in Sessions 45+.

---

## §1. Context and target

Per `SF-4_mechanism_selected.md` §2, the SF-4 mass formula is

$$
m_{\nu_i} = M_0 \cdot V_{\nu_i}^{2} \cdot \mathcal{T}_{\text{unbound}}
\qquad
M_0 = m_e \cdot z/\phi \approx 3.79 \text{ MeV}
\qquad
(V_{\nu_e}, V_{\nu_\mu}, V_{\nu_\tau}) = (4, 12, 30)
$$

The mass-ratio structure is fixed at zero parameters by the cage-shell assignment plus $\alpha = 2$. The absolute scale requires $\mathcal{T}_{\text{unbound}}$. Empirical target derived from the joint constraint of (a) Candidate-C predicted ratios, (b) observed $\Delta m^2_{21} = 7.39 \times 10^{-5}$ eV², (c) cosmological bound $\Sigma m_\nu < 0.072$ eV:

$$
\mathcal{T}_{\text{unbound}} \approx 1.59 \times 10^{-11}
$$

corresponding to $m_{\nu_e} \approx 0.96$ meV (with $m_{\nu_\mu} \approx 8.65$ meV, $m_{\nu_\tau} \approx 54.1$ meV, $\Sigma m_\nu \approx 63.7$ meV — within cosmological bound, predicted $\Delta m^2_{32}$ overshoots observed by 13% per the audit's known structural residual).

Per Q8 of the mechanism-selection conversation, the priority first-attempt route is to derive $\mathcal{T}_{\text{unbound}}$ from substrate primitives via the form $\sigma = N^{-d_{\text{eff}}}$ inherited from the archived $\sigma = 120^{-d}$ exploratory work, where $N$ is a substrate-information count and $d_{\text{eff}}$ is a walk-dimension-style channel count. The archived $d = 3$ choice produced $\sigma = 120^{-3} \approx 5.79 \times 10^{-7}$ — too weak by 4 orders of magnitude. This document derives a corrected $d_{\text{eff}}$ from a more careful enumeration of substrate-information channels.

---

## §2. Walk-dimension framework

### §2.1 Definition

In CPP, an unbound ZBW configuration propagating through the substrate must coherently maintain its mode characteristics across each absolute moment. Each moment, the mode interacts with the surrounding 600-cell substrate via DI-bit exchanges; each interaction samples a finite set of substrate options, with the mode's next state stochastically distributed across those options.

A **walk channel** is an independent substrate-information degree of freedom whose state must be coherently maintained per absolute moment. Each channel contributes a multiplicative dilution factor $1/N_{\text{channel}}$ to the mode's coherence per moment, where $N_{\text{channel}}$ is the substrate-information count for that channel.

The **walk dimension** $d_{\text{eff}}$ is the count of independent walk channels for the mode. Under the simplifying assumption that all channels share a common substrate-count base $N$ (provisional — see §2.4), the total per-moment suppression is

$$
\sigma = N^{-d_{\text{eff}}}
$$

This is the formal structure for the suppression factor that the archived $\sigma = 120^{-d}$ work was reaching toward; the present work makes the channel enumeration explicit and re-derives $d_{\text{eff}}$ from CPP primitives.

### §2.2 Boundary conditions: bound vs unbound

**Bound modes** (charged leptons, quarks): the mode sits in a cage of CPs that pins its state. The cage-resonance condition locks ZBW phase, the C3 / icosahedral / 600-cell symmetry of the cage locks orbital orientation, and the central CP locks spatial position. None of the channels samples the substrate freely — all are substrate-locked. Therefore $d_{\text{eff}} = 0$ and $\sigma = 1$ for bound modes. ✓ (matches the archived framework's bound-mode prediction and is consistent with quarks/charged-leptons receiving full mass at $M_0 \cdot V^{7/3}$ scale without additional suppression).

**Unbound modes** (neutrinos): no central CP anchor, no rigid cage. Each channel samples the substrate freely per moment. The walk dimension is the count of these free channels. The work below enumerates them for the specific case of an unbound 3D orbital ZBW configuration.

### §2.3 Note on substrate-count base $N$

The archived framework took $N = |V_{600}| = 120$ (the 600-cell vertex count) as a single base for all channels. Whether this is exactly right per channel — vs. e.g., $N_{\text{channel}} = z = 12$ (the coordination number) per channel, or $N_{\text{channel}} = z^2 = 144$ per channel from two-sided coupling — is itself open. §4 returns to this question after the channel enumeration; an empirically striking pattern at $N = z^2 = 144$ suggests the question is non-trivial.

For provisional analysis, we proceed with $N = 120$ (the archived choice) and note residuals that may indicate the true base lies elsewhere.

---

## §3. Channel enumeration for an unbound 3D orbital ZBW mode

### §3.1 Spatial position channels (3)

An unbound 3D orbital ZBW mode propagates through 3-dimensional space. Its spatial position is unconstrained by any cage. Each spatial axis (x, y, z) is an independent channel: per absolute moment, the mode's position along that axis is stochastically distributed across the substrate-information set for that direction.

**Channel count: 3.**

This count is essentially definitional — "3D orbital" means three spatial dimensions of free position, by hypothesis. Per the audit §3.4, neutrinos are identified with unbound orbital ZBW configurations of dipole-pair structures with no central CP anchor; this identification carries forward into the strict-C SF-4 framework and underwrites the spatial-channel count of 3.

### §3.2 ZBW oscillation phase channel (1)

The ZBW (Zitterbewegung) oscillation has an angular phase $\theta$ that advances per absolute moment. For a bound mode, the phase is locked to the cage-resonance condition: the cage-CPs supply the boundary structure that fixes $\theta$ at substrate-coherent values, and the mode's phase is not free to sample the substrate. For an unbound mode, no such boundary exists: the phase is sampled from the substrate's phase-information content per moment.

**Channel count: 1.**

Subtlety worth flagging: in the standard quantum-mechanical free-particle picture, the phase advances *deterministically* at $\omega = mc^2/\hbar$ — there is no stochastic sampling. In the CPP picture, the deterministic-looking advance is the coarse-grained outcome of substrate-internal DI-bit exchanges that *do* sample the substrate per moment; the phase is not in the strict sense "decided" per moment but is "transmitted" through substrate channels that contribute to coherence dilution. This is the relevant sense in which it counts as a walk channel. A rigorous derivation closing this requires CPP-internal accounting of phase-information transmission per absolute moment; queued as a Sessions 41+ refinement (§5.2).

### §3.3 Orbital orientation channel (1)

The ZBW orbital plane (equivalently, the angular-momentum direction) is the geometric orientation of the unbound mode's circulation. For a bound mode, orientation is locked by the cage symmetry: in a tetrahedral cage, orientation aligns with the tetrahedron's principal axes; in a 600-cell-coordinated configuration, orientation aligns with the substrate's directional structure. For an unbound mode, the orbital plane orients freely and samples substrate orientation states per moment.

**Channel count: 1.**

In CPP, fermion spin arises from the inner ZBW orbital at twice the outer-orbital frequency (per existing CPP postulate set, P-5a-style). Spin and orbital orientation are physically the same channel — the inner-outer 2:1 frequency relationship locks them to a single geometric direction. Counting them as one channel rather than two is the right discipline.

The substrate-information count for orientation is the angular structure of the 600-cell. The 120 vertices uniformly tile the 3-sphere $S^3$ (equivalently, the unit-quaternion group), providing a natural orientation basis; this is the substrate-information set the orientation channel samples per moment. Provisionally, $N_{\text{orientation}} = 120$ (same as spatial channels), pending the §2.4 question of whether all channels truly share one base.

### §3.4 Total walk dimension

$$
d_{\text{eff}} = 3 \text{ (spatial)} + 1 \text{ (ZBW phase)} + 1 \text{ (orientation)} = 5
$$

This is a **leading-order count from integer-channel-enumeration**. Sub-leading contributions may arise from:

- Partial-binding effects (the K3-eigenstructure constraint partially aligns one channel with substrate eigenmodes; see OPEN-FP-SF-4-2)
- Finer channel decomposition (e.g., separating orbital orientation from intrinsic spin if they partially decouple in the unbound regime)
- Substrate-count-base refinements (if different channels have different $N$, the simple $\sigma = N^{-d}$ form is an approximation)

These sub-leading effects are queued for Sessions 41+ work (§5).

---

## §4. First-principles result and comparison to target

### §4.1 Numerical result with $N = 120$

With $N = 120$ and $d_{\text{eff}} = 5$:

$$
\sigma = 120^{-5} = 4.02 \times 10^{-11}
$$

Predicted neutrino masses:

$$
m_{\nu_e} = M_0 \cdot V_{\nu_e}^2 \cdot \sigma = 3.79 \text{ MeV} \cdot 16 \cdot 4.02 \times 10^{-11} = 2.44 \text{ meV}
$$
$$
m_{\nu_\mu} = 9.00 \cdot m_{\nu_e} = 22.0 \text{ meV}
$$
$$
m_{\nu_\tau} = 56.25 \cdot m_{\nu_e} = 137 \text{ meV}
$$
$$
\Sigma m_\nu = 161 \text{ meV}
$$

### §4.2 Comparison to empirical constraints

| Quantity | Predicted ($N=120, d=5$) | Empirical | Ratio |
|----------|--------------------------|-----------|-------|
| $\sigma$ | $4.02 \times 10^{-11}$ | $1.59 \times 10^{-11}$ (target) | 2.5× too large |
| $m_{\nu_e}$ | 2.44 meV | $\le 5$ meV (cosmological) | within bound, but 2.5× target |
| $\Sigma m_\nu$ | 161 meV | $\le 72$ meV (cosmological) | **OVERSHOOTS BY 2.2×** |

**This is a real tension**, not just a factor-of-2 cosmetic issue. The integer-channel result with $N=120$ predicts a sum of neutrino masses incompatible with cosmological observation ($\Sigma m_\nu \le 0.072$ eV from DESI/Planck combined analyses).

**Comparison to archived framework:** the archived $\sigma = 120^{-3}$ predicted $m_{\nu_e} \sim 35$ eV (factor $\sim 3.5 \times 10^4$ too large — $\Sigma m_\nu$ in the keV range, vastly violating cosmological bounds and the much weaker KATRIN bound). The Session 40 result is 4 orders of magnitude tighter than the archived framework but still 2.5× from the precise target.

### §4.3 Numerical observation: $N = z^2 = 144$ produces near-exact agreement

A striking pattern emerges if we ask what substrate-count base $N$ gives exact integer-$d_{\text{eff}}$ agreement:

$$
N_{\text{required for } d=5 \text{ exact}} = \mathcal{T}_{\text{target}}^{-1/5} = 144.5
$$

This is **strikingly close to $z^2 = 144$** (the square of the 600-cell coordination number), with which:

$$
\sigma = 144^{-5} = z^{-10} = 1.62 \times 10^{-11}
$$

— matching the empirical target $1.59 \times 10^{-11}$ to within 2%. Equivalently, $\sigma = z^{-2 d_{\text{eff}}}$ with $z = 12$ and $d_{\text{eff}} = 5$.

Predicted neutrino masses with $N = 144, d = 5$:

| Quantity | Predicted ($N=144, d=5$) | Empirical | Ratio |
|----------|--------------------------|-----------|-------|
| $\sigma$ | $1.62 \times 10^{-11}$ | $1.59 \times 10^{-11}$ | 1.02× (within 2%) |
| $m_{\nu_e}$ | 0.98 meV | $\sim 0.96$ meV (Candidate-C-implied) | within 2% |
| $\Sigma m_\nu$ | 63.7 meV | $\le 72$ meV (cosmological) | within bound ✓ |

This is the level of agreement the empirical target $\mathcal{T}_{\text{unbound}}$ was designed to test. **It is not yet derived** — the question is whether $N = z^2$ rather than $N = |V_{600}| = 120$ is the right substrate-count base, and if so, why.

### §4.4 Interpretation and honest scope

The Session 40 result is twofold:

1. **Leading-order result with $N = 120$**: integer-channel enumeration gives $d_{\text{eff}} = 5$, producing $\sigma = 4.02 \times 10^{-11}$ — within factor 2.5 of the empirical target (4 orders of magnitude tighter than the archived $d=3$ work) but **inconsistent with the cosmological bound on $\Sigma m_\nu$**.

2. **Numerical observation**: switching the substrate-count base from $N = 120$ to $N = z^2 = 144$ produces near-exact agreement at the same integer $d_{\text{eff}} = 5$, **within cosmological bounds**. Equivalently, the formula $\sigma = z^{-2 d_{\text{eff}}}$ with $z = 12, d_{\text{eff}} = 5$ matches empirical to 2%.

This is suggestive but not yet a derivation. Three honest possibilities:

- **(a)** The right base is $z^2$, and there is a CPP-internal reason (yet to be identified) for each walk channel to contribute $z^2$ rather than $|V|$ states per moment. Working hypothesis sketched in §5.1.
- **(b)** The right base is $|V| = 120$, the integer count $d_{\text{eff}} = 5$ is correct as far as it goes, and there are sub-leading corrections that account for the factor 2.5. Working hypothesis sketched in §5.2.
- **(c)** A combination — different channels have different bases, or there are corrections of multiple types.

The Session 40 stop-point is to have the leading-order result and the observation cleanly stated. Resolving (a) vs (b) vs (c) is Session 41+ work.

---

## §5. Open sub-questions for Sessions 41+

### §5.1 Why might the substrate-count base be $z^2$ rather than $|V|$?

A possible CPP-internal interpretation: each walk channel involves **two-sided substrate coupling per absolute moment**. Per moment, each CP/DP exchanges DI-bits with its $z = 12$ nearest neighbors; for a given walk channel, the mode's coherence across the moment depends on a *correlated* from-vertex / to-vertex selection — i.e., $z$ "from" options × $z$ "to" options = $z^2 = 144$ per channel.

Alternative interpretation: each absolute moment contains two ZBW half-cycles (the inner and outer orbital cycles in the 2:1 fermion-spin convention); each half-cycle samples $z$ neighbors independently, giving $z^2$ per channel per moment.

Neither interpretation is yet rigorous from CPP axioms A1–A11. If either is closed in Sessions 41+, the formula

$$
\sigma = z^{-2 d_{\text{eff}}}
$$

with $z = 12, d_{\text{eff}} = 5$ becomes the SF-4 suppression-factor result at zero parameters, with empirical agreement to 2% (well within the structural residuals of the splitting predictions, which match to 4% / 11%).

### §5.2 Sub-leading corrections to $d_{\text{eff}}$ at $N = 120$

If instead the right base is $|V| = 120$ (preserving the archived framework's choice), the integer $d_{\text{eff}} = 5$ leaves a factor 2.5 to account for. Corrections to consider:

- **Partial-binding effects.** The K3-eigenstructure constraint (audit §6) partially aligns one channel (orientation?) with substrate eigenmodes; this reduces the effective freedom of that channel and may add a fractional contribution. Sign check: partial binding *reduces* $d_{\text{eff}}$, predicting a *larger* $\sigma$ — wrong direction. Unlikely route.
- **Additional decoupled channels.** If spin and orbital orientation partially decouple in the unbound regime (against the bound-mode 2:1 frequency-locking), spin becomes a separate channel and $d_{\text{eff}} \to 6$. Result: $\sigma = 120^{-6} = 3.35 \times 10^{-13}$ — overshoots by factor $\sim 200$ (wrong direction in the other extreme). Unlikely as primary correction.
- **Internal substrate degrees of freedom.** The 600-cell has internal structure beyond vertex connectivity (faces, cells, walk-paths through the polytope). A walk dimension counting that includes face- or cell-level information might land at a fractional value $d_{\text{eff}} \approx 5.2$ for $N = 120$. Plausible but requires explicit derivation.

The factor-2.5 residual is not obviously closed by any single correction at $N = 120$. The $N = z^2$ alternative (§5.1) gives cleaner structure and is the priority Session 41+ investigation.

### §5.3 K3-eigenstructure consistency check

Whichever substrate-count base is used, the suppression factor must commute with the K3-eigenstructure for the SM-5 PMNS derivation to survive (per audit §6 Constraints K1/K2/K3 and `SF-4_mechanism_selected.md` §4). The candidate $\sigma = N^{-d_{\text{eff}}}$ form is *flavor-blind* — it scales all three flavors uniformly — so it satisfies the constraint by construction at zeroth order. Higher-order flavor-dependent corrections to $\sigma$ would need explicit K3-consistency verification; this is queued as part of OPEN-FP-SF-4-2.

### §5.4 Rigorous derivation of channel count from CPP axioms

The integer count $d_{\text{eff}} = 5 =$ {3 spatial + 1 ZBW phase + 1 orientation} is a heuristic enumeration based on physical reasoning about which mode characteristics sample substrate freely. A rigorous derivation from axioms A1–A11 would:

- Define "substrate-information channel" formally
- Prove the count for an unbound 3D orbital ZBW mode is exactly 5 (or whichever value)
- Prove the substrate-count base for each channel (whether $|V|$, $z^2$, or other) from CPP primitives
- Establish the formula $\sigma = N^{-d_{\text{eff}}}$ as a theorem rather than ansatz

This is the SF-4 paper §4 derivation work for v0.1 drafting (Sessions 45+). The Session 40 result is the leading-order channel enumeration and the observational basis for further work; rigorous closure is downstream.

---

## §6. What this session establishes

**Established at Session 40 close (this document):**

- Walk-dimension framework defined: $\sigma = N^{-d_{\text{eff}}}$ where $d_{\text{eff}}$ counts independent substrate-information channels per absolute moment for an unbound mode
- Bound vs unbound boundary clarified: bound modes have $d_{\text{eff}} = 0$ from cage-pinning of all channels; unbound modes have $d_{\text{eff}}$ equal to the count of free channels
- Channel enumeration for unbound 3D orbital ZBW mode: **integer leading-order $d_{\text{eff}} = 5 =$ {3 spatial + 1 ZBW phase + 1 orientation}**
- Leading-order result with $N = |V_{600}| = 120$: $\sigma = 4.02 \times 10^{-11}$, predicting $m_{\nu_e} = 2.44$ meV — **4 orders of magnitude tighter than archived $\sigma = 120^{-3}$ work**, but factor 2.5 from empirical target and inconsistent with cosmological $\Sigma m_\nu$ bound
- Numerical observation: $N = z^2 = 144$ at integer $d_{\text{eff}} = 5$ produces $\sigma = z^{-10} \approx 1.62 \times 10^{-11}$ — within 2% of the empirical target and within cosmological bounds. **Suggestive, not yet derived.**

**Not established at Session 40 close:**

- Whether the correct substrate-count base is $|V| = 120$ or $z^2 = 144$ or something else
- The CPP-axiomatic basis for whichever base is correct
- Whether sub-leading corrections at $N = 120$ produce the factor 2.5 (alternative to $N = z^2$)
- Rigorous theorem-level closure of $d_{\text{eff}} = 5$ from axioms A1–A11
- The K3-eigenstructure consistency proof (deferred to OPEN-FP-SF-4-2; Sessions 43+)

**Forward priority for Session 41:**

Investigate the $z^2$ vs $|V|$ substrate-count question. Specifically: derive from CPP DI-bit exchange dynamics whether per-channel substrate sampling is $|V|^{-1}$ (one-sided), $z^{-1}$ (single-neighbor), or $z^{-2}$ (two-sided / two-half-cycle) per absolute moment. The $z^{-2}$ hypothesis from §5.1 is the leading conjecture given empirical 2% agreement; testing it is the first Session 41 sub-task. If $z^{-2}$ closes from primitives, OPEN-FP-SF-4-1 advances to PARTIAL CLOSURE pending only the K3-consistency check (OPEN-FP-SF-4-2) and the rigorous theorem-level derivation of $d_{\text{eff}} = 5$.

---

*Working document established at Session 40 (patch 0299). Captures opening sub-derivation under OPEN-FP-SF-4-1. Next session appends new sections rather than rewriting earlier content; this document grows monotonically across Sessions 40–42 (or longer) until OPEN-FP-SF-4-1 closes. Strategic source: Session 39 mechanism-selection conversation (`SF-4_mechanism_selected.md`); Session 37 audit conversation (`SF-4_neutrino_sector_audit.md` §3.4 DP-type taxonomy and §4.1 archived $\sigma = 120^{-d}$ analysis).*
