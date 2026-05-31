# SF-4 Flavor-Basis Harmonization — Working Sketch

**Parent open problem:** OPEN-FP-SF-4-FLAVORBASIS
**Status:** OPEN — v0.1 scoping sketch
**Sector(s):** FP / SF-4 (neutrinos), cross-sector with SM-5 (K3 tribimaximal mixing)
**Closure target:** Derive the unitary map {eDP, qDP, hTetra} → {V=4, V=12, V=30} and show it equals $U_\mathrm{TBM}$ at zeroth order (THEO candidate).
**Registered:** 30 May 2026.

---

## 1. The problem, well-posed

SF-4 builds the three neutrinos as **mass / propagation eigenstates** — unbound 3D orbital ZBW cage-shell modes at vertex counts $V \in \{4, 12, 30\}$, with masses $m_i = M_0 V_i^2 \sigma_\nu$ and the forced normal-hierarchy assignment $(\nu_1\!\to\!V{=}4,\ \nu_2\!\to\!V{=}12,\ \nu_3\!\to\!V{=}30)$.

Thomas's decay-product accounting identifies three **flavor / interaction objects** — the configuration the substrate presents at a production or absorption vertex:

$$\nu_e \equiv \text{eDP}, \qquad \nu_\mu \equiv \text{qDP}, \qquad \nu_\tau \equiv \text{hTetra}.$$

These are not competing claims. They are the **two standard neutrino bases**, joined by the PMNS rotation:

$$|\nu_\alpha\rangle = \sum_{i} U_{\alpha i}\, |\nu_i\rangle, \qquad \alpha \in \{e,\mu,\tau\},\ i \in \{1,2,3\}.$$

The harmonization claim is: $U$ realized by the substrate equals SM-5's tribimaximal $U_\mathrm{TBM}$ at zeroth order. If so, the decay bookkeeping and the SF-4 mass spectrum are one PMNS structure and there is no contradiction.

## 2. Why the V=2 problem and the "ordering inversion" both dissolve

- **No definite mass for a flavor object.** A flavor eigenstate has *no* definite cage $V$ — it is a superposition of the $V=4/12/30$ mass cages. So "eDP" need not carry a $V=4/12/30$ cage of its own; the mass-formula $m = M_0 V^2 \sigma_\nu$ acts only in the mass basis. The earlier objection ("a single dipole has $V=2$, outside the taxonomy") was a basis confusion: mass lives in the propagation basis, flavor in the interaction basis.
- **No hierarchy inversion.** Under $U_\mathrm{TBM}$, $|U_{\tau 3}|^2 = 1/2$, so $\nu_\tau$-flavor is **dominantly** the $V=30$ (heaviest) mass eigenstate. Identifying the $\nu_\tau$ *interaction object* with the hTetra does not make $\nu_\tau$ light. Normal hierarchy is preserved.

## 3. The target map, and a structural hint worth testing

Tribimaximal mixing (magnitudes $|U_{\alpha i}|^2$):

| flavor \ mass | $\nu_1$ (V=4) | $\nu_2$ (V=12) | $\nu_3$ (V=30) |
|---|---|---|---|
| $\nu_e$ (eDP)    | 2/3 | 1/3 | 0   |
| $\nu_\mu$ (qDP)  | 1/6 | 1/3 | 1/2 |
| $\nu_\tau$ (hTetra) | 1/6 | 1/3 | 1/2 |

Read in the mass basis, this is geometrically suggestive — a leading structural hint (CONJECTURE-tier, not yet derived):

- $\nu_2 = (\nu_e + \nu_\mu + \nu_\tau)/\sqrt{3}$ — **flavor-democratic (trimaximal)**. The most symmetric cage, the icosahedron ($V=12$, full $I_h$), maps to the flavor-symmetric combination. *Most symmetric cage ↔ most symmetric flavor state.*
- $\nu_3 = (\nu_\mu - \nu_\tau)/\sqrt{2}$ — **$\mu$–$\tau$ antisymmetric, zero eDP content** ($U_{e3}=0$, i.e. $\theta_{13}=0$ at TBM). The largest cage ($V=30$) is the qDP–hTetra antisymmetric state, decoupled from the eDP.
- $\nu_1 = (2\,\nu_e - \nu_\mu - \nu_\tau)/\sqrt{6}$ — the remaining orthogonal, eDP-weighted combination ($V=4$).

If the substrate overlaps $\langle V{=}12\,|\,\text{eDP}\rangle = \langle V{=}12\,|\,\text{qDP}\rangle = \langle V{=}12\,|\,\text{hTetra}\rangle = 1/\sqrt{3}$ fall out of the icosahedron's symmetry, half the matrix is fixed by geometry alone.

## 4. Dynamics: oscillation, not a one-way cascade

Observed flavor change is **oscillation** (periodic in $L/E$), so the momentum-transfer picture must be **coherent and bidirectional**, not a stochastic relay (a rate-based cascade relaxes to equilibrium; only amplitude-coherent evolution sustains oscillation). In fact, *no extra transfer mechanism is needed*: with the interaction basis misaligned from the propagation (energy) eigenbasis, free evolution

$$|\nu_\alpha(t)\rangle = \sum_i U_{\alpha i}\, e^{-i E_i t}\,|\nu_i\rangle, \qquad E_i \simeq E + \frac{m_i^2}{2E},\quad m_i^2 \propto V_i^4,$$

*already* oscillates, with periods set by the cage-mass splittings $\Delta m_{ij}^2 = M_0^2\sigma_\nu^2 (V_i^4 - V_j^4)$. Thomas's eDP⇄qDP⇄hTetra momentum transfer is then the **substrate-mechanistic realization of the off-diagonal terms** — *why* the interaction basis is rotated relative to the mass cages — and CPP already supplies coherent, deterministic, reversible substrate evolution (ZBW partner-switching; the PCD cycle is deterministic, not stochastic), so it has a natural home.

## 5. Closure sub-questions

- **SC-1 (common state space).** Construct the single $\mathbb{C}^3$ in which {eDP, qDP, hTetra} and {V=4, V=12, V=30} are two orthonormal bases. The objects differ in geometric "size," so the basis vectors are abstract interaction/propagation eigenstates whose *labels* encode substrate realization; establish that this is well-defined.
- **SC-2 (the map = TBM).** Compute the substrate overlaps $U_{\alpha i} = \langle \nu_i | \nu_\alpha \rangle$ and show $U = U_\mathrm{TBM}$ at zeroth order. **Route:** identify {eDP, qDP, hTetra} with SM-5's K3-vertex flavor states so the *same* $S_3 \to S_2$ branching that yields TBM in SM-5 (and the THEO-SF-4-5 forcing $|\phi_-^{(1)}\rangle\!\to\!V{=}4$, $|\phi_-^{(2)}\rangle\!\to\!V{=}30$) yields this map. Closure = THEO candidate. **This is the load-bearing step.**
- **SC-3 (dynamics).** Show §4 reproduces oscillation with the SF-4 mass splittings, and cast the momentum-transfer kinematics as the off-diagonal coupling.
- **SC-4 (tetrahedron double-assignment).** The tetrahedron is both the $\nu_\tau$ *flavor object* (hTetra) and the $\nu_1$/$V{=}4$ *mass cage*. Disambiguate: is the coincidence forced (limited substrate polytope vocabulary), or does it constrain $U$ away from a generic unitary? Resolve before SC-2 is declared closed.
- **SC-5 (species assignment).** Justify eDP↔$\nu_e$, qDP↔$\nu_\mu$, hTetra↔$\nu_\tau$ from the decay-product accounting (the foundational input). Note: charge/colour are consistent — eDP and qDP are both net-neutral dipoles, and the neutrino is a neutral fermion, so no charge obstruction; the open question is purely *which species pairs with which flavor*, which the bookkeeping supplies.

## 6. Falsifier / decision gate

If the substrate overlap matrix comes out $= U_\mathrm{TBM}$ → harmonization succeeds and CPP gains a **mechanistic derivation of PMNS** (a new result, beyond SM-5's spectral derivation). If it comes out $\neq U_\mathrm{TBM}$ → genuine conflict with SF-4/SM-5 requiring reconciliation (revise the flavor-object identification, or treat the decay-bookkeeping objects as an approximate/effective basis). Either outcome is informative; the matrix computation in SC-2 is the gate.

## 7. What this does NOT touch

SF-4's shipped content is untouched by registering this: the mass basis ($V=4/12/30$), the mass formula, $\sigma_\nu = z^{-10}$, normal hierarchy, and the TBM mixing all stand. This problem adds a *mechanistic interpretation layer* (the flavor-basis substrate objects) and a derivation target (PMNS from substrate kinematics). No deposit-paper edits are implied unless SC-2 closes as $\neq$ TBM.
