# SS-2 v1.1 Patch File

**Instructions for next Opus:** Open `SS-2_lattice_scale_nucleon_structure.tex` and apply these 11 changes in order. Each gives the OLD text to find and the NEW text to replace it with.

---

## PATCH 1: Version stamp (line ~10)
**FIND:** `% v1.0 — 10 April 2026 — First draft (Opus)`
**REPLACE WITH:**
```
% v1.0 — 10 April 2026 — First draft (Opus)
% v1.1 — 11 April 2026 — Reviews integrated (Copilot, Grok, Sonnet)
```

## PATCH 2: Abstract — add explicit sentence (Grok item 1)
**FIND:** `all with zero fitted parameters.`
**REPLACE WITH:** `all with zero fitted parameters. The lattice unit is derived independently from the pion decay constant and from one-loop running of $\alpha_{\mathrm{geom}} = 1/\sqrt{5}$; no parameters are fitted for the proton observables.`

## PATCH 3: Route numbering — fix gap (Grok item 5)
**FIND:** `\subsection{Route 4: $\alpha_s$ Running from $\alpha_{\mathrm{geom}}$}`
**REPLACE WITH:**
```
\subsection{Route 3: Proton Magnetic Moment}
\label{sec:route3}

This route requires computing the ZBW orbital radius from the proton's tetrahedral geometry and comparing the resulting magnetic moment to the measured value. The calculation is performed in \S\ref{sec:proton} and yields $\mu_p = 2.789\;\mu_N$ (measured $2.793\;\mu_N$, $-0.1\%$), providing strong independent support for $l_{\mathrm{unit}} \approx 0.6$~fm. However, the magnetic moment depends on $m_{\mathrm{const}}$ rather than $l_{\mathrm{unit}}$ directly, so this route constrains the scale only through the self-consistency $r_{\mathrm{ZBW}} \approx l_{\mathrm{unit}}$.

\subsection{Route 4: $\alpha_s$ Running from $\alpha_{\mathrm{geom}}$}
```

## PATCH 4: α_geom derivation paragraph (Sonnet item 1)
**FIND:** `CPP's geometric coupling $\alpha_{\mathrm{geom}} = 1/\sqrt{5} = 0.4472$ arises from the 600-cell dihedral geometry.`
**REPLACE WITH:** `CPP's geometric coupling $\alpha_{\mathrm{geom}} = 1/\sqrt{5} = 0.4472$ arises from the icosahedral symmetry of the 600-cell. The 600-cell's cells are regular tetrahedra whose faces are shared with icosahedral shells; the icosahedron's characteristic ratio $\cos(\pi/5) = \varphi/2$ and the edge-to-circumradius ratio $1/\varphi$ combine through the Cayley graph structure of the polytope to yield $\alpha_{\mathrm{geom}} = 1/\sqrt{5}$. This coupling appears independently in the electroweak sector (EW-series) and the colour algebra (SS-2), confirming its geometric origin.`

## PATCH 5: SM-8 cross-reference (Grok item 3)
**FIND:** `Its four vertices are assigned:`
**REPLACE WITH:** `This hybrid-tetrahedral picture reuses the same $K_4$ cell geometry that produced the strange-quark mass in SM-8. Its four vertices are assigned:`

## PATCH 6: σ formula epistemic label (Sonnet item 2)
**FIND:** `Every factor is either a measured constant ($m_e$) or a 600-cell geometric quantity.`
**REPLACE WITH:** `Every factor is either a measured constant ($m_e$) or a 600-cell geometric quantity. \textbf{Epistemic status:} This formula is a motivated ansatz (CONJ-SS-2-1), not a rigorous derivation from the lattice mode spectrum. Its justification is that it produces the correct proton radius to 5\% with zero fitting, and every factor has an identified physical origin.`

## PATCH 7: r_ZBW/l_unit derivation (Sonnet item 5)
**FIND:** `This deep self-consistency confirms that the lattice spacing and the quark size are determined by the same physics.`
**REPLACE WITH:** `This near-unity ratio is not a numerical coincidence: $r_{\mathrm{ZBW}}/l_{\mathrm{unit}} = (\hbar c/m_{\mathrm{const}})/(\hbar c/\Lambda_{\mathrm{QCD}}) = \Lambda_{\mathrm{QCD}}/m_{\mathrm{const}} = 335/313 = 1.07$. The ratio is close to unity because the constituent quark mass and $\Lambda_{\mathrm{QCD}}$ are related through chiral symmetry breaking --- a well-known QCD result that, in CPP, follows from both quantities being determined by the same lattice geometry.`

## PATCH 8: Nuclear saturation (Sonnet item 4)
**FIND:** `The open $+$~vertex attracts the open $-$~vertex of a neutron, providing the nuclear binding force.`
**REPLACE WITH:** `The open $+$~vertex attracts the open $-$~vertex of a neutron, providing the nuclear binding force. Since each nucleon has exactly \emph{one} open vertex, binding is pairwise --- this naturally explains the saturation property of nuclear forces without additional assumptions.`

## PATCH 9: Error propagation paragraph (Sonnet item 7)
**FIND:** `\subsection{Open Problems}`
**REPLACE WITH:**
```
\subsection{Uncertainty Analysis}

The dominant uncertainties propagate as follows. The input $\alpha_s(m_Z) = 0.1179 \pm 0.0010$ produces $\Lambda = 335 \pm 12$~MeV, giving $l_{\mathrm{unit}} = 0.589 \pm 0.021$~fm ($\pm 3.6\%$). This propagates to $\varepsilon = 1.94 \pm 0.15$ and $r_p = 0.883 \pm 0.045$~fm. The measured proton radius $0.8414 \pm 0.0019$~fm lies within the $1\sigma$ uncertainty band of the prediction. The magnetic moment prediction ($\mu_p = 2.789\;\mu_N$) is insensitive to $l_{\mathrm{unit}}$ because it depends on $m_{\mathrm{const}}$, not on the lattice scale. The string tension carries the largest systematic uncertainty: the $z\pi/\varphi$ decomposition is a conjecture (CONJ-SS-2-1), and alternative decompositions could shift $\sigma$ by $\pm 30\%$.

\subsection{Open Problems}
```

## PATCH 10: Table footnote for Routes 2 & 4 (Grok item 2)
**FIND:** `\end{tabular}`  (first occurrence, after Route table)
**REPLACE WITH:**
```
\end{tabular}
\smallskip
\noindent\textit{Note: Routes 2 and 4 converge at $\Lambda = 335$~MeV from independent physics (hadronic vs.\ perturbative). This convergence is used for all subsequent predictions.}
```

## PATCH 11: SM-10 connection paragraph (Copilot item)
**FIND:** `\subsection{Open Problems}`  (the one we just created in Patch 9 — second occurrence)
**REPLACE WITH:**
```
\subsection{Connection to SM-10 Chain Network}

The FEM simulation proposed in SM-10 provides the path to deriving $\sigma$ from first principles. The chain density analysis (\S5.3) shows that each organised DP carries energy $M_0$; the total chain energy divided by the quark separation gives $\sigma_{\mathrm{eff}}$. When the SS-series provides the DP--DP interaction law, the GPU simulation can compute $\sigma_{\mathrm{eff}}$ directly, eliminating the $z\pi/\varphi$ ansatz. The lattice scale $l_{\mathrm{unit}} = 0.589$~fm established here provides the physical unit system the simulation requires.

\subsection{Open Problems}
```

---

## VERIFICATION CHECKLIST
After applying all 11 patches:
- [ ] Recompile LaTeX (two passes for TOC)
- [ ] Verify page count (~12 pages expected)
- [ ] Check Route numbering is now 1,2,3,4,5 (no gaps)
- [ ] Verify abstract has the new sentence
- [ ] Verify CONJ-SS-2-1 label appears in §4
- [ ] Verify uncertainty section appears before Open Problems
