# SSV_net Site Inventory — LaTeX Sources (Patch 4149)

Generated inventory of **every** `SSV…net` occurrence in `.tex` sources, so that the
classification work of TODO-4142-SSVAUDIT Stage 3 proceeds against a **fixed, auditable list**
rather than a regex whose answer changed three times (3 → 138 → 162 sites; see Patch 4148 for
the first correction and §1 below for the second).

**Census: 162 sites in 28 files.** Pattern: `SSV` followed by `net` within 12
characters, case-insensitive — permissive by design, so it catches `\SSV_{\rm net}`,
`\mathbf{SSV}_{\rm net}`, the literal `SSV_net`, and label/comment forms alike.

Classification legend: **[V]** = the LSP broadcast vector (→ `V_i`); **[D]** = the GP-computed
displacement register (→ `SSV_disp`); **[—]** = not yet classified.


---

## 1. What the reading of GR-1b settles — and it reframes the whole audit

**GR-1b's LSP is the two-component, pre-LSP′ form:**

> `LSP = (x_GP, t_abs, |SSV|_abs, SSV_net)` … *"The scalar |SSV|_abs sources gravitational time
> dilation (g_tt); the vector **SSV_net** sources spatial curvature (g_ij)."*

So in GR-1b, **`SSV_net` IS the broadcast vector** — the thing A3′ later renamed `V_i` when LSP′
replaced the two-component packet with (Φ, V_i, Q_ij) at Patch 1129. Twenty-six of GR-1b's
twenty-nine sites are that broadcast component: *"extending the DI-bit broadcast to include the net
SSV vector"*, *"SSV_net broadcast → g_rr perturbation"*, *"vorticity in SSV_net encoding frame
dragging"*.

**Three of the twenty-nine are the other sense**, in the same paper:

- *"the receiver extracts SSV_net = E + S"* (the AP-4 clause) → **[D]**
- *"a CP displaced onto an occupied GP … is moved per the local SSV_net the next [Moment]"* → **[D]**
- *"a CP selects the 12-edge that maximises e_i · SSV_net"* → **[D]**

### The history this exposes

This is **not a coinage and not a cleanup of sloppy writing.** It is the completion of a rename
that A3′ began and never propagated:

1. GR-1b and the early gravitation series used `SSV_net` for the **broadcast vector**.
2. **A3′ (Patch 1129)** replaced the two-component LSP with LSP′ = (Φ, V_i, Q_ij) and renamed that
   vector **`V_i`** — but the existing papers were never updated.
3. Meanwhile **A1′/AP-3 (Patch 2982)** began using `SSV_net` for the **GP-computed displacement
   register**, a different object.

Result: **two names for one thing, and one name for two things.** Patch 4142 found the second half;
GR-1b shows the first. The retirement of `SSV_net` finishes a job left half-done five years of
patches ago, which is a better justification than the one the audit started with.

### Consequence for the plan

The gravitation series will map **predominantly to `V_i`**, not to `SSV_disp` — the opposite of the
glossary and axiom text, where every classified site was `SSV_disp`. **Anyone applying a uniform
substitution to the papers would have got 26 of GR-1b's 29 sites wrong.** Per-site reading is not
caution here; it is the difference between a correct rename and a corrupted one.

---


---

## 2. Classification round 2 (Patch 4150) — 45 more sites settled, 20 contested

**Settled, all by reading:**

| file | sites | verdict |
|---|---|---|
| `GR-1f_kerr_metric` | 13 | **[V] all 13.** Azimuthal `SSV_net` sourcing g_tφ via "the LSP vector mapping"; "rotation adds an azimuthal component to the `SSV_net` **broadcast**". |
| `GR-1c_strong_field_GR` | 12 | **[V] 11, [D] 1.** The LSP is stated as the four-component packet with mapping `SSV_net → g_ij`. The one [D]: *"same-polarity co-occupation can be forced by an external SSV_net"* — a field driving CPs. |
| `SR-2_spin_bit_axiom` | 12 | **[V] all 12.** |
| `GR-1_local_gravitation` | 8 | **[V] all 8.** The LSP as "the two-component broadcast object". |

**SR-2 is documentary proof of the history in §1.** It writes the rename out explicitly:

> `LSP′ = (x_GP, t_abs; Φ, V_i, Q_ij)`, where *"Φ ≡ SSVabs is the scalar (irrep A, l=0; sources
> g_tt), **V_i ≡ SSVnet** is the vector…"* — and its inheritance table lists *"V_i = SSVnet (irrep
> T₁) → g_ij"*.

The identity `V_i ≡ SSV_net` is stated in a published paper. §1's reconstruction was inference from
GR-1b's packet form; SR-2 states it outright. **The rename is not being invented here; it is being
finished.**

## 3. QM-1 (20 sites) — CONTESTED, and it puts a question mark on Patch 4147

QM-1 fuses both roles in one object and cannot be classified without a ruling. It says both:

- *"the A3′ register mapping … maps one-to-one onto the scalar (SSV_abs, **l=0**) and vector
  (SSV_net, **l=1**)"* — the l=1 slot, which is **`V_i`**; and
- *"each Grid Point **holds, and refreshes every Moment**, two dynamical registers (the A3′ state
  protocol): the count-like scalar SSV_abs and the vector SSV_net"* — the GP-computed register,
  which Patch 4147 classified as **`SSV_disp`**.

**These are the same object in QM-1's usage**, and the whole quantum phase identification (φ = the
orientation of that register, FI-QMRG-1) rests on it.

**The difficulty is real, not a QM-1 sloppiness.** A3′'s own definitional clause reads: the GP
*"computes, holds, and per-Moment refreshes SSV_abs and SSV_disp from Perceive-stage arrivals,
**imprints on every outgoing DI-bit**"* — so the held register is **what gets broadcast**. If the
register is what is imprinted and sent, it is broadcast content, and 4147's classification of that
clause as `SSV_disp` is questionable.

**Two readings, and they differ physically:**

1. The GP holds **one** vector register; it both broadcasts it and hands it to its CP. Then `V_i`
   and `SSV_disp` are the same register read at two moments in the cycle, and the 4142 split is a
   distinction of *role*, not of *object*.
2. The GP holds **two** vectors: the summed arrivals (what it imprints and sends — a potential) and
   the displacement it computes for its resident CP (a field, the gradient). Then the split is a
   distinction of *object*, as 4142 and GR-1a's `force = k∇(ΔSSV)` imply.

Reading 2 is what the audit has assumed throughout. **Reading 1 would not overturn the retirement**
— two names for one thing still needs fixing — **but it would change which name QM-1's phase
register takes, and it would make 4147's A3′ edit wrong.**

**Filed as TODO-4150-REGISTERCOUNT.** This is a physics question in a physical picture — *how many
vector registers does a GP hold?* — and therefore **founder territory under PD-006(a)**. QM-1's 20
sites, and the A3′ definitional clause, wait on it. Nothing is edited meanwhile.

**Running totals: 74 of 162 classified (71 [V], 3 [D]), 20 contested, 68 unread.**

---

## `series_gravitation/GR_companion_papers/GR-1b_weak_field_GR/GR-1b_weak_field_GR.tex` — 29 sites

1. **[—]** `…bstract} We derive the \emph{weak-field limit} of general relativity in Conscious Point Physics by extending the DI-bit broadcast to include the net SSV vector $\mathbf{\SSV}_{\rm net}$ alon…`

2. **[—]** `…e polarization energy $E_{\rm pol} = mc^2$ of the eDP cloud \citep{abshier2026mass}: $|\SSV|_{\rm abs} = E_{\rm pol}/V_0$ sources $g_{tt}$ (time curvature) and $\mathbf{\SSV}_{\rm net}$ sour…`

3. **[—]** `…rom the net alignment of Dipole Particles. The scalar magnitude $|\SSV|_{\rm abs}$ governs time dilation and the local Planck length. The vector component $\mathbf{SSV}_{\rm net}$ governs sp…`

4. **[—]** `…packet transmitted by each GP to its PSR shell at every Absolute Moment: \[ \LSP = \bigl(\mathbf{x}_{\rm GP},\; t_{\rm abs},\; |\SSV|_{\rm abs},\; \mathbf{SSV}_{\rm net}\bigr). \] The scalar…`

5. **[—]** `…abs},\; |\SSV|_{\rm abs},\; \mathbf{SSV}_{\rm net}\bigr). \] The scalar $|\SSV|_{\rm abs}$ sources gravitational time dilation ($g_{tt}$); the vector $\mathbf{SSV}_{\rm net}$ sources spatial…`

6. **[—]** `…r $|\SSV|_{\rm abs}$ sources gravitational time dilation ($g_{tt}$); the vector $\mathbf{SSV}_{\rm net}$ sources spatial curvature ($g_{ij}$). In flat space $\mathbf{SSV}_{\rm net}$ averages…`

7. **[—]** `…fied Patch 3032), the DI-bit payload is \{origin address, $\mathbf{E}$, $\mathbf{S}$\} — a static snapshot imprinted by the origin GP — and the receiver extracts $\SSV_{\rm net} = \mathbf{E}…`

8. **[—]** `…chwarzschild_weak} \end{equation} The scalar $|\SSV|_{\rm abs}$ accounts for $g_{tt}$ (time dilation) but not $g_{rr}$ (spatial curvature). The net SSV vector $\mathbf{\SSV}_{\rm net}$ provi…`

9. **[—]** `…ng component. The Lattice State Packet carries four components: \begin{equation} \LSP \;=\; \bigl(\mathbf{x}_{\rm GP},\; t_{\rm abs},\; |\SSV|_{\rm abs},\; \mathbf{\SSV}_{\rm net}\bigr). \la…`

10. **[—]** `…},\; t_{\rm abs},\; |\SSV|_{\rm abs},\; \mathbf{\SSV}_{\rm net}\bigr). \label{eq:LSP} \end{equation} \begin{remark}[Backward compatibility] In flat space, $\mathbf{\SSV}_{\rm net}$ averages …`

11. **[—]** `…} The two physical components of the LSP are: \begin{align} |\SSV|_{\rm abs} &\;=\; \frac{E_{\rm pol}}{V_0} \;=\; \frac{mc^2}{V_0}, \label{eq:SSV_abs}\\ \mathbf{\SSV}_{\rm net} &\;=\; \sum_{…`

12. **[—]** `…\frac{E_{\rm pol}}{V_0} \;=\; \frac{mc^2}{V_0}, \label{eq:SSV_abs}\\ \mathbf{\SSV}_{\rm net} &\;=\; \sum_{i=1}^{12} \hat{\mathbf{e}}_i\,\Delta\SSV_i, \label{eq:SSV_net} \end{align} where $E_…`

13. **[—]** `…calar component $|\SSV|_{\rm abs} = mc^2/V_0$ (red) sources the time-time perturbation $g_{tt}$, encoding gravitational time dilation. The vector component $\mathbf{\SSV}_{\rm net}$ (green) …`

14. **[—]** `…{align} g_{tt}(\mathbf{x}) &\;=\; 1 - k\,\Delta|\SSV|_{\rm abs}(\mathbf{x}), \label{eq:gtt}\\ g_{ij}(\mathbf{x}) &\;=\; \delta_{ij}\bigl(1 + k\,|\nabla\mathbf{\SSV}_{\rm net}|_{ij}(\mathbf{x…`

15. **[—]** `…SSV}_{\rm net}|_{ij}(\mathbf{x})\bigr), \label{eq:gij} \end{align} where $k = \lP^3/\EP$ is the CPP coupling constant \citep[Eq.~1]{abshier2026sr} and $|\nabla\mathbf{\SSV}_{\rm net}|_{ij}$ …`

16. **[—]** `…n} where $k = \lP^3/\EP$ is the CPP coupling constant \citep[Eq.~1]{abshier2026sr} and $|\nabla\mathbf{\SSV}_{\rm net}|_{ij}$ is the spatial gradient tensor of $\mathbf{\SSV}_{\rm net}$. \en…`

17. **[—]** `…rom LSP] \label{prop:Schwarzschild} For a static spherically symmetric mass $M$, with gravitational SSV $\Delta|\SSV|_{\rm abs}(r) = GM/(k\,r\,c^2)$ and $|\nabla\mathbf{\SSV}_{\rm net}|_{rr}…`

18. **[—]** `…In CPP the origin is transparent: \begin{itemize}[noitemsep] \item $|\SSV|_{\rm abs}$ broadcast $\to$ $g_{tt}$ perturbation $\to$ $0.875$~arcsec. \item $\mathbf{\SSV}_{\rm net}$ broadcast $\…`

19. **[—]** `…$) CPP framework recovers. The breakdown box shows that the two equal contributions --- time curvature from $|\SSV|_{\rm abs}$ and spatial curvature from $\mathbf{\SSV}_{\rm net}$ --- each c…`

20. **[—]** `…%====================================================================== At each Absolute Moment tick, a CP selects the 12-edge that maximises $\mathbf{e}_i\cdot\mathbf{\SSV}_{\rm net}$ \cite…`

21. **[—]** `…. They are the gravitational analog of photons \citep{abshier2026zdc}: a traveling perturbation of the LSP broadcast pattern, with both $|\SSV|_{\rm abs}$ and $\mathbf{\SSV}_{\rm net}$ joint…`

22. **[—]** `…eq:GW} \end{equation} Solutions propagate at $c$, consistent with the LIGO/Virgo/KAGRA observations of \citet{abbott2016}. These observations confirm that the $\mathbf{\SSV}_{\rm net}$ compo…`

23. **[—]** `…ed to neighboring GPs'' is superseded by the founder's replacement mechanism: a CP displaced onto an occupied GP superimposes for one Moment and is moved per the local $\SSV_{\rm net}$ the n…`

24. **[—]** `…========= Every element of the GR framework reuses established CPP machinery: \begin{itemize}[noitemsep] \item \emph{LSP}~\eqref{eq:LSP_explicit}: adds $\mathbf{\SSV}_{\rm net}$ to the broad…`

25. **[—]** `…interior behind a horizon, but a horizonless maximally compact body at the Buchdahl radius.]} \textbf{(3) Kerr metric.} Rotating bodies require vorticity in $\mathbf{\SSV}_{\rm net}$, encodi…`

26. **[—]** `…ng as angular momentum of the SSV field. \emph{[Status note added Patch 3294 (W-D), 20 Aug 2026. DELIVERED by companion GR-1f (18 Mar 2026): the azimuthal component $k(\SSV_{\rm net})_\phi =…`

27. **[—]** `…Packet provides a natural weak-field general relativity in CPP: \begin{enumerate} \item \textbf{LSP} \citep{abshier2026mass,abshier2026grav} (rigorous): $\mathbf{\SSV}_{\rm net}$ derived fro…`

28. **[—]** `…itep{abshier2026sr}. \item \textbf{Weak-field Schwarzschild} \citep[Eq.~2]{einstein1915} (rigorous): $g_{tt}$ from $|\SSV|_{\rm abs}$, $g_{rr}$ from $\mathbf{\SSV}_{\rm net}$, equal magnitud…`

29. **[—]** `…oughout the companion series. The key conceptual advance in this paper --- extending the Lattice State Packet broadcast to include the net SSV vector component $\mathbf{SSV}_{\rm net}$ along…`


## `series_quantum_mechanics/papers/QM-1_schrodinger_emergence.tex` — 20 sites

1. **[—]** `…qm1_phase_provenance_audit.md). The site field % is re-grounded on FI-QMRG-1 (phi = orientation % of the GP's SSV_net directional content in the % distinguished ZBW plane; rho = the count-li…`

2. **[—]** `…(A3$'$) already holds --- $\rho_i$ is the count-like scalar register ($\SSV_{\rm abs}$; DI-bit number density), and $\phi_i$ is the orientation of the vector register ($\SSV_{\rm net}$) in t…`

3. **[—]** `…bar\partial_t\psi = [-\hbar^2\nabla^2/(2m) + V]\psi$. The imaginary unit is grounded in the geometry of the phase register: multiplication by $-i$ is a quarter-turn of $\SSV_{\rm net}$ in th…`

4. **[—]** `…da)^2$ and unobservable at laboratory wavelengths. \end{abstract} \medskip\noindent \textbf{Keywords:} Schrödinger equation, 600-cell lattice, Sea-polarization pattern, SSV\_net phase regist…`

5. **[—]** `…ct is that each Grid Point holds, and refreshes every Moment, two dynamical registers (the A3$'$ state protocol): the count-like scalar $\SSV_{\rm abs}$ and the vector $\SSV_{\rm net}$ --- t…`

6. **[—]** `…e grounding layer: the phase now lives where the audit's registered candidate placed it --- at the level of the Sea-polarization \emph{pattern}, in the Grid-Point-held $\SSV_{\rm net}$ regis…`

7. **[—]** `…scalar register (the DI-bit number density held as $\SSV_{\rm abs}$, per AP-2's count-like magnitude clause), and $\phi_i$ is the orientation angle of the Grid Point's $\SSV_{\rm net}$ direc…`

8. **[—]** `…and $\phi_i$ is the orientation angle of the Grid Point's $\SSV_{\rm net}$ directional content in the distinguished plane (FI-QMRG-1). The microscopic contributors to $\SSV_{\rm net}$ are th…`

9. **[—]** `…protocol). \emph{The identification carries two explicit conditions (CONV-014 panel amendment, enacted v2.1):} \textbf{C-i} the in-plane magnitude tracks the count, $|\SSV_{{\rm net},\perp}|…`

10. **[—]** `…f{The A3$'$ register mapping.} The Madelung content of the site field, $(\sqrt{\rho},\phi)$, maps one-to-one onto the scalar ($\SSV_{\rm abs}$, $l=0$) and vector ($\SSV_{\rm net}$, $l=1$) re…`

11. **[—]** `…tude--count bridge (B-QMRG-1).} The identification $|\psi_i|^2 = \rho_i$ requires that the squared amplitude of the net planar polarization track the count register: $|\SSV_{{\rm net},\perp}…`

12. **[—]** `…er limit occupies. \medskip \noindent\textbf{The distinguished plane.} The orientation angle is read in the plane swept by the periodic (Zitterbewegung) component of $\SSV_{\rm net}$: a mass…`

13. **[—]** `…ber arrows indicate the direction of coherent DI-bit messenger flow. The lower dashed curve shows the phase oscillation $e^{i\phi}$ --- the rotation of each site's $\SSV_{\rm net}$ orientati…`

14. **[—]** `…ment is deterministic and invertible (A1--A9 rules; the substrate has no diffusive or stochastic process), so the per-Moment map is invertible. (iii)~\emph{Linearity:} $\SSV_{\rm net}$ is by…`

15. **[—]** `…the coherent weak-field regime (B-QMRG-1) the per-Moment refresh therefore acts linearly on the site fields, and superposition of patterns is vector addition of their $\SSV_{\rm net}$ contri…`

16. **[—]** `…exactly the tight-binding form~\eqref{eq:evolution}. Under FI-QMRG-1 the imaginary unit has a concrete substrate meaning: multiplication by $-i$ is a quarter-turn of $\SSV_{\rm net}$ in the …`

17. **[—]** `…y the conditional note naming MULTILINK + B1-CONST. Historical framing of the obligations as first registered: \emph{OPEN-QMRG-B1 (original registration)} The bridge $|\SSV_{{\rm net},\perp}…`

18. **[—]** `…atically; the A3$'$ per-Moment reset makes the register a driven steady state; each messenger transfers the mode quantum $\hbar\omega$ ($E=\hbar\nu_C$). Balance gives $|\SSV_{{\rm net},\perp…`

19. **[—]** `…ntum pressure $Q$ in~\eqref{eq:HJ} is the geometric interference effect of Sea-polarization pattern contributions arriving from regions of different density --- planar $\SSV_{\rm net}$ vecto…`

20. **[—]** `…field reads the two registers the Grid-Point state protocol already holds: the count ($\rho \leftrightarrow \SSV_{\rm abs}$) and the orientation ($\phi \leftrightarrow \SSV_{\rm net}$ direct…`


## `series_gravitation/GR_companion_papers/GR-1f_kerr_metric_from_rotational_SSV/GR-1f_kerr_metric.tex` — 13 sites

1. **[—]** `…document} \maketitle \noindent\textbf{Keywords:} Conscious Point Physics, Kerr metric, rotating black hole, frame-dragging, Lense-Thirring, ergosphere, Boyer-Lindquist, SSV-net azimuthal com…`

2. **[—]** `…n. In CPP, rotation adds a new component to the SSV broadcast. A rotating mass drags the surrounding Dipole Sea in the azimuthal direction, producing a net azimuthal $\SSV_{\rm net}$ compone…`

3. **[—]** `…=================== \begin{abstract} We derive the CPP origin of the Kerr metric for a rotating mass. A rotating source with angular momentum $J$ produces an azimuthal $\SSV_{\rm net}$ compo…`

4. **[—]** `…CPP origin of the Kerr metric for a rotating mass. A rotating source with angular momentum $J$ produces an azimuthal $\SSV_{\rm net}$ component: \begin{equation} k\,(\SSV_{\rm net})_\phi \;=…`

5. **[—]** `…ses from the off-diagonal $g_{t\phi}$ component of the Kerr metric~\cite{kerr1963}. In CPP, the mechanism is transparent. Rotation adds an azimuthal component to the $\SSV_{\rm net}$ broadca…`

6. **[—]** `…energy alone, not angular momentum. \subsection{Azimuthal vector component: frame-dragging source} Angular momentum $J$ produces an additional azimuthal component of $\SSV_{\rm net}$. A rota…`

7. **[—]** `…erical shells at distance $r$ and colatitude $\theta$ (the same shell-broadcast geometry used for the scalar component in companion~5~\cite{c5}): \begin{equation} k\,(\SSV_{\rm net})_\phi(r,…`

8. **[—]** `…= The off-diagonal metric component is sourced by the azimuthal SSV via the LSP vector mapping (companion~7, Proposition~2.1): \begin{equation} g_{t\phi} \;=\; -2k\,(\SSV_{\rm net})_\phi\cdo…`

9. **[—]** `…ch gives Eq.~\eqref{eq:ergosphere}. \end{proof} \begin{remark}[CPP mechanism for the ergosphere] In the CPP picture, the ergosphere is the surface where the azimuthal $\SSV_{\rm net}$ drag v…`

10. **[—]** `…iance channel (bounded; growth-time bounds committed under the amended OPEN-GR-RCORE-3).]} In CPP, the mechanism is transparent. Inside the ergosphere, the azimuthal $\SSV_{\rm net}$ compone…`

11. **[—]** `…h{12-edge selection rule} and shell-broadcast geometry for the azimuthal SSV are from companion~7~\cite{c7}, §4. \item The \emph{LSP off-diagonal metric mapping} $\SSV_{\rm net} \to g_{t\phi…`

12. **[—]** `…chanism. The complete derivation requires showing that the nonlinear PSR formula with total SSV magnitude $|\Delta\SSV|^2 = |\Delta\SSV|_{\rm scalar}^2 + |(\SSV_{\rm net})_\phi|^2$ generates…`

13. **[—]** `…================================================ \begin{enumerate} \item \textbf{Azimuthal SSV source} (exact, §\ref{sec:source}): a rotating mass $J$ sources $k(\SSV_{\rm net})_\phi = GJ\si…`


## `series_gravitation/GR_companion_papers/GR-1c_strong_field_GR/GR-1c_strong_field_GR.tex` — 12 sites

1. **[—]** `…Throughout, we use the notation of companion~7: the Lattice State Packet (LSP) is the four-component broadcast packet $(x_{\rm GP},\, t_{\rm abs},\, |\SSV|_{\rm abs},\, \SSV_{\rm net})$ emit…`

2. **[—]** `…},\, t_{\rm abs},\, |\SSV|_{\rm abs},\, \SSV_{\rm net})$ emitted by each Grid Point each Absolute Moment tick. The metric mapping is $|\SSV|_{\rm abs} \to g_{tt}$ and $\SSV_{\rm net} \to g_{…`

3. **[—]** `…ht). \label{eq:gtt_final} \end{equation} This is the isotropic Schwarzschild $g_{tt}$~\cite{wald1984}. The spatial components $g_{ij} = (1+\vrho)^4\delta_{ij}$ are the SSV-net contribution~\…`

4. **[—]** `…, \texttt{theorem-registry.md}), under which co-occupation is not forbidden but lasts one Absolute Moment, and same-polarity co-occupation can be forced by an external $\SSV_{\rm net}$ (foun…`

5. **[—]** `…hawking}). \subsection{Gravitational wave polarisation modes} \label{subsec:gw} The LSP is a four-component packet: $(x_{\rm GP},\, t_{\rm abs},\, |\SSV|_{\rm abs},\, \SSV_{\rm net})$. Gravi…`

6. **[—]** `…al wave has two tensor polarisation modes ($+$ and $\times$). The additional LSP components permit, in principle, scalar ($|\SSV|_{\rm abs}$ perturbation) and vector ($\SSV_{\rm net}$ longit…`

7. **[—]** `…its 12 nearest neighbours (the 12-edge selection rule of companion~7~\cite{c7}). The net azimuthal SSV at distance $r$ and colatitude $\theta$ is: \begin{equation} (\SSV_{\rm net})_\phi \;=\…`

8. **[—]** `…ctromagnetic case of companion~2~\cite{c2}). The metric cross term is sourced by this azimuthal component via the LSP mapping: \begin{equation} g_{t\phi} \;=\; -2k\,(\SSV_{\rm net})_\phi \cd…`

9. **[—]** `…kerr_total} The nonlinear PSR reduction applies to the total SSV magnitude: \begin{equation} |\Delta\SSV|_{\rm total}^2 \;=\; |\Delta\SSV|_{\rm scalar}^2 \;+\; |(\SSV_{\rm net})_\phi|^2. \la…`

10. **[—]** `…\end{proof} \begin{remark}[Verification in limits] Three consistency checks hold exactly: \begin{enumerate}[noitemsep] \item \textbf{Zero rotation} ($a=0$, $J=0$): $(\SSV_{\rm net})_\phi=0$,…`

11. **[—]** `…dcast source} $k\,\Delta|\SSV| = GM/rc^2$ is from companion~5~\cite{c5}, §3, proved exact. \item The \emph{LSP metric mapping} $|\SSV|_{\rm abs} \to g_{tt}$, $\SSV_{\rm net} \to g_{ij}$ is f…`

12. **[—]** `…nd are undetectable by current instruments. \item \textbf{Frame-dragging} (Proposition~\ref{prop:kerr}): the Kerr $g_{t\phi}$ term arises from the azimuthal $\SSV_{\rm net}$ curl; the Lense-…`


## `series_relativity/papers/SR-2_spin_bit_axiom_quadrupole_formula.tex` — 12 sites

1. **[—]** `…Paper-specific macros --- \newcommand{\Qij}{Q_{ij}} \newcommand{\TF}{\mathrm{TF}} \newcommand{\TT}{\mathrm{TT}} \newcommand{\SSVabs}{|\SSV|_{\mathrm{abs}}} \newcommand{\SSVnet}{\SSV_{\mathrm…`

2. **[—]** `…ecific macros --- \newcommand{\Qij}{Q_{ij}} \newcommand{\TF}{\mathrm{TF}} \newcommand{\TT}{\mathrm{TT}} \newcommand{\SSVabs}{|\SSV|_{\mathrm{abs}}} \newcommand{\SSVnet}{\SSV_{\mathrm{net}}} …`

3. **[—]** `…(CPP) recovers the static and gravitomagnetic sectors of General Relativity from a Lattice State Packet (LSP) broadcast carrying one scalar ($\SSVabs$) and one vector ($\SSVnet$) degree of f…`

4. **[—]** `…SP) to its Planck-Shell-Radius neighbors, and the packet's dynamical content is one scalar, $\SSVabs$ (sourcing gravitational time dilation, $g_{tt}$), and one vector, $\SSVnet$ (sourcing sp…`

5. **[—]** `…mismatch. Einstein's equation is a tensor (10 components); c08's is a single scalar equation. The metric map is explicit (c07/c08): $\SSVabs \to g_{tt}$ (a scalar) and $\SSVnet \to g_{ij}$ (…`

6. **[—]** `…opagating tensor polarizations. For a plane wave propagating along $z$, the most general symmetric spatial perturbation a scalar $S$ ($=\SSVabs$) and a vector $V_i$ ($=\SSVnet$) can build, u…`

7. **[—]** `…{-51}$, forcing flat (absolute-frame) carriage.} \label{fig:assaults} \end{figure} \subsection{First assault --- amplitude polynomials in $(\Phi, V)$} A transverse $\SSVnet$ plane wave $V=(a…`

8. **[—]** `…propagates at $c$ as the $+/\times$ modes. What the lattice does \emph{not} provide is the degree of freedom itself. The LSP state $(x_{\mathrm{GP}}, t_{\mathrm{abs}}, \SSVabs, \SSVnet)$ is …`

9. **[—]** `…ement; the Nexus timing pulse) carries an $l=2$ channel. The candidate sources each reduce to content already counted: the Dipole-Sea polarization \emph{is} the vector $\SSVnet$; the constit…`

10. **[—]** `…& Packet content & Sector it unlocked \\ \midrule 1 & DI-bit: scalar $\SSVabs$ & Special relativity; time dilation ($g_{tt}$) \\ 2 & LSP: scalar $+$ vector $\SSVnet$ & Weak-field GR statics;…`

11. **[—]** `…= \big(\,x_{\mathrm{GP}},\, t_{\mathrm{abs}}\,;\ \Phi,\ V_i,\ Q_{ij}\,\big), \] where $\Phi\equiv\SSVabs$ is the scalar (irrep $A$, $l=0$; sources $g_{tt}$), $V_i\equiv\SSVnet$ is the vector…`

12. **[—]** `…CPP object & GR / observational counterpart & Status \\ \midrule $\Phi=\SSVabs$ (irrep $A$) & $g_{tt}$ / Newtonian potential & Recovered (c07/c08) \\ $V_i=\SSVnet$ (irrep $T_1$) & $g_{ij}$ s…`


## `series_gravitation/papers/GR-1_local_gravitation_from_SSV_shell_broadcast.tex` — 8 sites

1. **[—]** `…09) gravitational-wave echoes \\ \quad$\hookrightarrow$ GR-1e (c10) Hawking evaporation with a Planck remnant \\ \quad$\hookrightarrow$ GR-1f (c11) Kerr from azimuthal $\SSV_{\rm net}$ \\ \q…`

2. **[—]** `…solar limb, and the measured value is $1.75''$. c07 resolves this by extending the DI-bit broadcast to carry, alongside the scalar, the \emph{net} SSV vector $\mathbf{\SSV}_{\rm net}$, whose…`

3. **[—]** `…the spatial components $g_{ij}$. The Lattice State Packet (LSP) is the two-component broadcast object: $|\SSV|_{\rm abs} = E_{\rm pol}/V_0$ sources $g_{tt}$; $\mathbf{\SSV}_{\rm net}$ source…`

4. **[—]** `…vector component is the minimal directional content the broadcast can carry. Everything downstream of c07 --- the exact static metric of c08, the rotational (azimuthal $\SSV_{\rm net}$) exte…`

5. **[—]** `…avitational-wave echo predictions of c09 and the modified (remnant-terminated) Hawking evaporation of c10. \item \textbf{The rotating and charged families.} Azimuthal $\SSV_{\rm net}$ yields…`

6. **[—]** `…that distinction. \textbf{This paper claims the solutions. The general field-equation derivation --- expected to proceed from the deeper DI-bit / $\SSV_{\rm abs}$ / $\SSV_{\rm net}$ / DP Sea…`

7. **[—]** `…is set by SR-1; the inheritance is stated in full in Section~\ref{sec:inheritance}. \item c09--c13 inherit c08's exactness claim; where they add mechanisms (azimuthal $\SSV_{\rm net}$ for ro…`

8. **[—]** `…d at V0: derive the general CPP field equations (and their consequences: Birkhoff-type uniqueness, the CPP energy-momentum object) from the DI-bit / $\SSV_{\rm abs}$ / $\SSV_{\rm net}$ / DP …`


## `flagship_papers/electromagnetism/SF-8/sf-8_emergent_electrostatics.tex` — 5 sites

1. **[—]** `…--- Paper-specific macros --- \newcommand{\eDP}{e\mathrm{DP}} \newcommand{\ZBW}{\mathrm{ZBW}} \newcommand{\AM}{\mathrm{AM}} \newcommand{\PSR}{\mathrm{PSR}} \newcommand{\SSVnet}{\SSV_{\mathrm…`

2. **[—]** `…r-specific macros --- \newcommand{\eDP}{e\mathrm{DP}} \newcommand{\ZBW}{\mathrm{ZBW}} \newcommand{\AM}{\mathrm{AM}} \newcommand{\PSR}{\mathrm{PSR}} \newcommand{\SSVnet}{\SSV_{\mathrm{net}}} …`

3. **[—]** `…ress Vector] The \emph{Space Stress Vector} $\SSV$ at a Grid Point is the running vector bookkeeping of DI-bit arrivals at that point. Two reductions of it are used: \[ \SSVnet \;=\; \sum_i …`

4. **[—]** `…ec{s}_i , \qquad \SSVabs \;=\; \sum_i \lVert \vec{s}_i \rVert , \] the vector sum and the scalar magnitude-sum of the contributions $\vec{s}_i$ arriving at that point. $\SSVnet$ is direction…`

5. **[—]** `…r the respecification. \end{remark} \subsection{The displacement law} Having tallied arrivals, each Conscious Point displaces by \begin{equation} d \;=\; \frac{\lVert \SSVnet \rVert}{\SSVabs…`


## `series_gravitation/GR_companion_papers/GR-1b_weak_field_GR/duplicates/weak field GR.tex` — 5 sites

1. **[—]** `…tored in the eDP cloud surrounding any mass (\(E_{\rm pol} = mc^2\), ZBW Mass companion). Scalar \(|\SSV|_{\rm abs}\) encodes time-dilation (\(g_{tt}\)), while vector \(\SSV_{\rm net}\) enco…`

2. **[—]** `…The LSP at any Grid Point \(\mathbf{x}\) and Absolute Moment \(t_{\rm abs}\) is the four-component object \[ \LSP = \bigl(\mathbf{x},\ t_{\rm abs},\ |\SSV|_{\rm abs},\ \SSV_{\rm net}\bigr), …`

3. **[—]** `…onent object \[ \LSP = \bigl(\mathbf{x},\ t_{\rm abs},\ |\SSV|_{\rm abs},\ \SSV_{\rm net}\bigr), \] where \(|\SSV|_{\rm abs}\) is the scalar compressive magnitude and \(\SSV_{\rm net}\) is t…`

4. **[—]** `…e compressive polarization energy stored in the eDP cloud (ZBW Mass companion, Proposition 4.1): \[ |\SSV|_{\rm abs} = \frac{E_{\rm pol}}{V_0} = \frac{mc^2}{V_0}, \] \[ \SSV_{\rm net} = \sum…`

5. **[—]** `…component \(|\SSV|_{\rm abs}\) contracts the timelike interval: \[ g_{tt} = -\left(1 + 2\Phi\right), \qquad \Phi = -k \cdot |\SSV|_{\rm abs}. \] The vector component \(\SSV_{\rm net}\) contr…`


## `series_gravitation/GR_companion_papers/GR-1b_weak_field_GR/duplicates/weak_field_general_relativity.tex` — 5 sites

1. **[—]** `…tored in the eDP cloud surrounding any mass (\(E_{\rm pol} = mc^2\), ZBW Mass companion). Scalar \(|\SSV|_{\rm abs}\) encodes time-dilation (\(g_{tt}\)), while vector \(\SSV_{\rm net}\) enco…`

2. **[—]** `…The LSP at any Grid Point \(\mathbf{x}\) and Absolute Moment \(t_{\rm abs}\) is the four-component object \[ \LSP = \bigl(\mathbf{x},\ t_{\rm abs},\ |\SSV|_{\rm abs},\ \SSV_{\rm net}\bigr), …`

3. **[—]** `…onent object \[ \LSP = \bigl(\mathbf{x},\ t_{\rm abs},\ |\SSV|_{\rm abs},\ \SSV_{\rm net}\bigr), \] where \(|\SSV|_{\rm abs}\) is the scalar compressive magnitude and \(\SSV_{\rm net}\) is t…`

4. **[—]** `…e compressive polarization energy stored in the eDP cloud (ZBW Mass companion, Proposition 4.1): \[ |\SSV|_{\rm abs} = \frac{E_{\rm pol}}{V_0} = \frac{mc^2}{V_0}, \] \[ \SSV_{\rm net} = \sum…`

5. **[—]** `…component \(|\SSV|_{\rm abs}\) contracts the timelike interval: \[ g_{tt} = -\left(1 + 2\Phi\right), \qquad \Phi = -k \cdot |\SSV|_{\rm abs}. \] The vector component \(\SSV_{\rm net}\) contr…`


## `series_gravitation/GR_companion_papers/GR-1g_kerr_newman_charged_rotating_BH/GR-1g_kerr_newman.tex` — 5 sites

1. **[—]** `…Schwarzschild metric with $\Dlt_S = r^2 - 2Mr$. \subsection{Azimuthal SSV from rotation: Kerr frame-dragging} From companion~11~\cite{c11}, §2: \begin{equation} k\,(\SSV_{\rm net})_\phi(r,\t…`

2. **[—]** `…11. \subsection{Radial SSV from charge: Coulomb contribution} From companion~2~\cite{c2}, the electromagnetic SSV broadcast of a charge $Q$ is: \begin{equation} k\,(\SSV_{\rm net})_r(r) \;=\…`

3. **[—]** `…\item The \emph{azimuthal SSV and Kerr frame-dragging} from angular momentum $J$ are from companion~11, §2--4~\cite{c11}. \item The \emph{radial charge SSV} $k(\SSV_{\rm net})_r = \rQ^2/r^2$…`

4. **[—]** `…N}$.} The full Kerr-Newman metric requires showing that the nonlinear PSR formula with total SSV magnitude $|\Delta\SSV|^2 = |\Delta\SSV|_{\rm scalar}^2 + |(\SSV_{\rm net})_\phi|^2 + |(\SSV_…`

5. **[—]** `…etric requires showing that the nonlinear PSR formula with total SSV magnitude $|\Delta\SSV|^2 = |\Delta\SSV|_{\rm scalar}^2 + |(\SSV_{\rm net})_\phi|^2 + |(\SSV_{\rm net})_r|^2$ generates t…`


## `series_gravitation/GR_companion_papers/GR-1g_kerr_newman_charged_rotating_BH/development/Claude_Kerr-Newman.tex` — 5 sites

1. **[—]** `…Schwarzschild metric with $\Dlt_S = r^2 - 2Mr$. \subsection{Azimuthal SSV from rotation: Kerr frame-dragging} From companion~11~\cite{c11}, §2: \begin{equation} k\,(\SSV_{\rm net})_\phi(r,\t…`

2. **[—]** `…11. \subsection{Radial SSV from charge: Coulomb contribution} From companion~2~\cite{c2}, the electromagnetic SSV broadcast of a charge $Q$ is: \begin{equation} k\,(\SSV_{\rm net})_r(r) \;=\…`

3. **[—]** `…\item The \emph{azimuthal SSV and Kerr frame-dragging} from angular momentum $J$ are from companion~11, §2--4~\cite{c11}. \item The \emph{radial charge SSV} $k(\SSV_{\rm net})_r = \rQ^2/r^2$…`

4. **[—]** `…N}$.} The full Kerr-Newman metric requires showing that the nonlinear PSR formula with total SSV magnitude $|\Delta\SSV|^2 = |\Delta\SSV|_{\rm scalar}^2 + |(\SSV_{\rm net})_\phi|^2 + |(\SSV_…`

5. **[—]** `…etric requires showing that the nonlinear PSR formula with total SSV magnitude $|\Delta\SSV|^2 = |\Delta\SSV|_{\rm scalar}^2 + |(\SSV_{\rm net})_\phi|^2 + |(\SSV_{\rm net})_r|^2$ generates t…`


## `series_gravitation/GR_companion_papers/GR-1h_superradiance/GR-1h_superradiance.tex` — 5 sites

1. **[—]** `…========================= A spinning black hole stores rotational energy in the frame-dragging of surrounding spacetime. In CPP, this frame-dragging is the azimuthal $\SSV_{\rm net}$ broadca…`

2. **[—]** `…face, and the c-vs-$c_*$ question, are OPEN-GR-RCORE-2.]} In CPP, the mechanism is transparent at the level of the SSV broadcast. The rotating black hole's azimuthal $\SSV_{\rm net}$ field r…`

3. **[—]** `…r horizon (companion~11, §3--4~\cite{c11}). A wave couples to this SSV broadcast. When the wave's phase velocity at the horizon is less than the SSV rotation rate, the SSV does net work on t…`

4. **[—]** `…wave is absorbed if $\omega > m\Oplus$, and propagates without exchange if $\omega = m\Oplus$ (co-rotation). \end{theorem} \begin{proof}[CPP derivation] The azimuthal $\SSV_{\rm net}$ at the…`

5. **[—]** `…er the energy balance over one wave cycle at the horizon: \begin{itemize}[noitemsep] \item If $\omega/m < \Oplus$: the SSV field rotates faster than the wave. The SSV exerts a net tangential…`


## `flagship_papers/electromagnetism/sf-6_electromagnetism.tex` — 4 sites

1. **[—]** `…n is not a discrete object in transit between Grid Points; it is a phase-coherent $\SSV$ distribution across the $\GP$ network --- the phase borne by the GP registers ($\SSV_{\rm net}$ orien…`

2. **[—]** `…ies bremsstrahlung (rapid dissociation of the decelerated electron's arc cohort), synchrotron radiation (centripetal acceleration dissociating the cohort from fore/aft $\SSV_{\rm net}$ recap…`

3. **[—]** `…V_{\rm net}$ recapture, its broad spectrum reflecting that no level structure constrains aggregation --- only statistical opportunity), driven antenna current ($\partial\SSV_{\rm net}/\parti…`

4. **[—]** `…cal opportunity), driven antenna current ($\partial\SSV_{\rm net}/\partial t$ severing the arcs from the moving charge), and intranuclear gamma production (large $\Delta\SSV_{\rm net}$ in sm…`


## `series_gravitation/papers/GR-2_echo_falsifier.tex` — 4 sites

1. **[—]** `…IVERSAL + residual xi_t); % a=0 even features at M omega 0.412 / 0.604, displacement PROVISIONAL % pending complex poles; axial sector registered in the uncapped % SSV_net -> NOT refused, en…`

2. **[—]** `…the ``clamped register'' is a misnomer --- the founder's replacement boundary is a one-sided, one-Moment-delay compliant surface (superimpose one Moment, displace per $\SSV_{\rm net}$ the ne…`

3. **[—]** `…sector is not governed by SSV$_{\rm abs}$ alone: a shear must be registered to interact (founder ruling R-SHEAR-MUST-BE-REGISTERED), and it is registered in the uncapped SSV$_{\rm net}$ vect…`

4. **[—]** `…3v/2)\,H_2 + 2K = 0$ --- a kinematic relation; the boundary's own dynamics is not modelled (OPEN-GR-SURFACE-DYNAMICS-1). The axial sector, registered in the uncapped $\SSV_{\rm net}$, transm…`


## `series_gravitation/GR_companion_papers/GR-1c_strong_field_GR/development/strong_field_GR.tex` — 3 sites

1. **[—]** `…explicitly as the integrated compressive SSV field sourced by polarization energy \(E_{\rm pol} = mc^2\) (ZBW Mass companion). Scalar \(|\SSV|_{\rm abs}\) and vector \(\SSV_{\rm net}\) compo…`

2. **[—]** `…rcing compressive SSV and modified PSR altering SSV propagation yields the CPP analog of \(G_{\mu\nu} = 8\pi G/c^4 T_{\mu\nu}\). Kerr solutions emerge from rotational \(\SSV_{\rm net}\) curl…`

3. **[—]** `…mu\nu}\) is the LSP energy-momentum density. This closes the loop without new postulates. \section{Kerr Metric from Rotational SSV Curl} Rotating sources add angular \(\SSV_{\rm net}\) compo…`


## `series_gravitation/GR_companion_papers/GR-1i_classical_tests/GR-1i_classical_tests.tex` — 3 sites

1. **[—]** `…s structural, not accidental: the scalar broadcast $|\SSV|_{\rm abs}$ sources $g_{tt}$ only, and GR-1b's extension of the LSP broadcast to carry the net vector $\mathbf{\SSV}_{\rm net}$ --- …`

2. **[—]** `…ear separately: $g_{tt} = -[(1-\vrho)/(1+\vrho)]^2$ carries the scalar ($|\SSV|_{\rm abs}$) content, and the conformal factor $(1+\vrho)^4$ carries the vector ($\mathbf{\SSV}_{\rm net}$) con…`

3. **[—]** `…the Schwarzschild solution \\ Scalar broadcast $|\SSV|_{\rm abs}$ (clock-rate gradient) & $g_{tt}$; gravitational time dilation / redshift \\ Vector broadcast $\mathbf{\SSV}_{\rm net}$ (Sea …`


## `series_gravitation/GR_companion_papers/GR-1j_field_equations/GR-1j_field_equations.tex` — 3 sites

1. **[—]** `…xtbf{GPs} (fixed lattice sites, 600-cell geometry, zero configuration freedom) execute Perceive (integrate DI-bit arrivals) and Compute (refresh their $\SSV_{\rm abs}$/$\SSV_{\rm net}$ regis…`

2. **[—]** `…(refresh their $\SSV_{\rm abs}$/$\SSV_{\rm net}$ registers); \textbf{CPs} (charge-bearers composing matter) execute Displace, once per Moment, per their GP's computed $\SSV_{\rm net}$; \text…`

3. **[—]** `…xactly \{origin address, $E$, $S$\}, emitted at fixed per-GP count each Moment, delivered in a thin band at the PSR shell, then reset and reused. Receiver GPs compute $\SSV_{\rm net}$ and $\…`


## `series_quantum_mechanics/papers/QM-6_capstone.tex` — 3 sites

1. **[—]** `…Points, and DI-bit messengers; A1$'$), the 600-cell lattice, the Grid-Point-held Sea-polarization pattern state (count register $\SSV_{\rm abs}$ + orientation register $\SSV_{\rm net}$; A3$'…`

2. **[—]** `…'$)}: each Grid Point holds two dynamical registers refreshed every Moment from Perceive-stage arrivals --- the count-like scalar $\SSV_{\rm abs}$ and the vector $\SSV_{\rm net}$ (the sum of…`

3. **[—]** `…rlying dipole orientations). The complex site field $\psi = \sqrt{\rho}\,e^{i\phi}$ reads these two registers: $\rho$ is the count, $\phi$ is the orientation of $\SSV_{\rm net}$ in the disti…`


## `series_relativity/SR_companion_papers/c03_born_rule/c03_born_rule.tex` — 3 sites

1. **[—]** `…oportional to the local DI-bit number density $\rho$, with $|\psi|^2 = \rho$ — a proof that consumes only the count register. Under the B-QMRG-1 coherent-mode bridge ($|\SSV_{{\rm net},\perp…`

2. **[—]** `…nt for Conjecture~\ref{conj:born} in more detail to clarify what a rigorous proof would require. At each tick, the net SSV at the aggregate's GP is: \begin{equation} \SSV_{\rm net}(t) \;=\; …`

3. **[—]** `…onents, each of amplitude $\sim \lP/\tP$ and oscillating at $\nu_{\rm ZBW}$. The 12-edge selection rule chooses the lattice edge $i^*$ that maximizes $\mathbf{e}_i\cdot\SSV_{\rm net}$. Over …`


## `series_relativity/papers/SR-1_special_relativity_emergence.tex` — 3 sites

1. **[—]** `…aternion structure of $2I$ and the definition of nearest neighbors; it requires no external tabulation. \subsection{SSV-Induced Distortion} Excess stress $\Delta\text{SSV}$ from kinetic or g…`

2. **[—]** `…ativistic kinetic energy. The energy-momentum bridge (Eq.~\ref{eq:bridge}) is not a new postulate; it follows from the definition of $k$, the definition of $\Delta\text{SSV}$ as kinetic ener…`

3. **[—]** `…undertakes the deeper question: can the exact Lorentz factor be recovered from the 600-cell Voronoi geometry alone, without invoking the physical content of $\Delta\text{SSV}$ as kinetic ene…`


## `series_gravitation/GR_companion_papers/GR-1e_hawking_radiation_planck_remnant/GR-1e_hawking_radiation.tex` — 2 sites

1. **[—]** `…n the same Absolute Moment tick, they do not stack. On the immediately following tick, each CP moves outward along the PSR shell in the direction defined by the local $\SSV_{\rm net}$ vector…`

2. **[—]** `…classical expectations. \item The Planck remnant retains the quantum information encoded in its internal CP configuration — specifically, the pattern of $\SSV_{\rm net}$ vectors and CP posit…`


## `series_gravitation/GR_companion_papers/GR-1e_hawking_radiation_planck_remnant/development/Claude_Hawking_Radiation.tex` — 2 sites

1. **[—]** `…n the same Absolute Moment tick, they do not stack. On the immediately following tick, each CP moves outward along the PSR shell in the direction defined by the local $\SSV_{\rm net}$ vector…`

2. **[—]** `…classical expectations. \item The Planck remnant retains the quantum information encoded in its internal CP configuration — specifically, the pattern of $\SSV_{\rm net}$ vectors and CP posit…`


## `series_relativity/SR_companion_papers/c01_absolute_moment_postulate/absolute_moment_postulate.tex` — 2 sites

1. **[—]** `…tination GP in the Displace phase. It is determined by the \emph{net} SSV (the vector sum, including direction): \begin{equation} \mathbf{d} \;=\; d(\text{SSV}_{\rm net})\,\hat{\mathbf{n}}_{…`

2. **[—]** `…ts absolute SSV magnitude $|\text{SSV}|_{\rm abs}$ from the register sum, and hence its own PSR via Eq.~\eqref{eq:PSR-def}; \item the net SSV vector $\text{SSV}_{\rm net}$ (vector sum over a…`


## `series_relativity/SR_companion_papers/c06_DP_chaining_as_mass_and_EM_substrate/c06_dipole_chain_patterns_as_mass_EM_subtrate.tex` — 2 sites

1. **[—]** `…n] A photon is not a discrete object in transit between Grid Points. It is a phase-coherent SSV distribution across the GP network — the phase borne by the GP registers (SSV\(_{\rm net}\) or…`

2. **[—]** `…no per-messenger phase variable; panel-endorsed at CONV-013, founder-ratified Patch 3032). Under the ratified ontology (FI-QMRG-1), phase is the orientation of the GP's SSV\(_{\rm net}\) reg…`


## `flagship_papers/electroweak/sf-2_electroweak.tex` — 1 sites

1. **[—]** `…\emph{Bearer note (v1.02, Patch 3039, F-SW-8 sweep).} The field $\psi_v$ of this theorem is the PATTERN-LEVEL vertex register content (FI-QMRG-1: phase $=$ the vertex $\SSV_{\rm net}$ orient…`


## `series_quantum_mechanics/papers/QM-4_measurement_problem.tex` — 1 sites

1. **[—]** `…d decoherence~\cite{zeh1970,zurek1981}: the pattern state couples to the thermal DP~Sea, whose random phase kicks --- bath-interaction rotations acting on the system's $\SSV_{\rm net}$ orien…`


## `series_quantum_mechanics/papers/QM-5_qft_emergence.tex` — 1 sites

1. **[—]** `…on modes of the complex Sea-polarization site field on the 600-cell lattice. The site field $\psi_i = \sqrt{\rho_i}\,e^{i\phi_i}$ (QM-1 v2.0: count register $\rho_i$, $\SSV_{\rm net}$-orient…`


## `series_relativity/SR_companion_papers/c04_ZBW_hbar_mass_units/c04_ZBW_hbar_mass_units.tex` — 1 sites

1. **[—]** `…the dressed pair's \emph{stored DP arc field}: the pair's two arc stores have opposite rotation senses and cancel at co-location, zeroing the inertia-associated $\mathrm{SSV}_{\rm net}$ --- …`
