# CONV-033 — Review package: GR-2 "The Echo Falsifier" V0 (assembly round)

**Round ID:** CONV-033 (registered Patch 3330, 21 Aug 2026)
**Under review:** `series_gravitation/papers/GR-2_echo_falsifier.tex` (V0, Patch 3329)
**Verify script:** `series_gravitation/code/3329_gr2_template_verify.py` — 9/9 PASS reference run; **FAST subset 4/4** (seconds-scale, own count line — you can own-run it with `--fast`)
**Receiver:** `series_gravitation/review/reviews-CONV-033.md` (0/5)
**Repo:** https://github.com/Hyperphysics-Institute/CPP

**One-paragraph intro.** GR-2 is the gravitation series' second paper and its first *assembly* paper: it derives nothing new, and instead packages the reviewed echo chain — horizonless hard surface (F-R1, CONV-030), |R| = 1 with zero free parameters (GR-1d V3), the Schwarzschild delay closed form, and the derived Kerr exclusion surface with its censorship theorem and prograde-ring burial (Patch 3320; CONV-032 closed 5/5) — into one search-facing falsifier document: the retrograde-keyed template Δt(M, χ), the quantified error budget, the 5% parameter-free amplitude, the pro/retro discriminator against horizon-anchored ECO templates, and the explicit kill conditions (PRED-O-39). Its inputs are reviewed; its ASSEMBLY is not — that is this round's object. One new quantitative finding rides in: the template saturates in spin above burial onset (dΔt/dχ = 0.299 GM/c³ at χ = 0.68 ⇒ ±0.1 in χ moves Δt only ±0.35%; mass ±6.5% dominates ~20×), making the remnant-population template effectively mass-only.

---

## §1 Cold-start context (self-contained)

Conscious Point Physics (CPP) derives gravitation from a messenger census on an absolute lattice. The exterior metric is exactly isotropic Schwarzschild (GR-1c, panel-ratified); the interior is censored by the Exclusion floor (per-point register capacity), so the compact object that forms is a horizonless, hard-surfaced body at exactly the Buchdahl radius, areal (9/8) r_S, with surface lapse 1/3 — the sector's founder-ratified standing reading F-R1 (CONV-030, 5/5). Gravitational-sector reflectivity is derived: |R| = 1 exactly, phase π, zero free parameters (GR-1d V3). Such an object must produce GW echoes: ringdown energy leaks through the photon-sphere barrier, reflects off the wall, and returns as a delayed, damped pulse train.

The spin sector (Patch 3320, reviewed at CONV-032, 5/5): a two-component census — scalar s = 2(1−α)/(1+α) (the ratified log-lapse dictionary, exact at a = 0) plus rotational v = ωϖ/α (ZAMO dragging speed) composed in quadrature (assumptions A1–A3) — yields the Kerr-analog exclusion surface {s² + v² = 1}. The exact Kerr identity g_tt = −α²(1 − v²) makes the ergosphere the v = 1 surface identically, forcing F = s² + 1 > 1 there: the surface lies STRICTLY OUTSIDE the ergosphere at every spin and latitude (censorship theorem — no ergoregion instability at any spin or reflectivity), and the prograde equatorial photon ring is buried inside the surface for χ ≳ 0.55, so the surviving eikonal echo cavity is RETROGRADE-ring keyed. All spin-sector statements are derivation-conditional on A1–A3; the substrate derivation of the census functional is OPEN-GR-RCORE-4 (minted from the CONV-032 GPT dissent, whose γ-weighted-norm counterexample — F = s² + γv², γ < 1, preserves the static sector yet can de-censor the ergosphere — established that A3's unweighted norm is load-bearing).

Benchmark (GW150914, M = 62 ± 4 M_⊙, χ = 0.68): Δt_ret = 8.592 GM/c³ = 2.624 ms; f_echo ≈ 381 Hz; first-echo amplitude ~5% of ringdown. Published echo searches target 0.1–0.3 s delays; the ms band is unsearched.

## §2 What this round reviews — and the out-of-scope fence

**IN SCOPE:** the GR-2 V0 assembly: input-provenance fidelity, the template equation/table and its error budget, the new spin-saturation finding, claim discipline (conditionality prose), the falsifier set and discriminator framing, completeness as a search-facing citable paper, and the ship-path question.

**OUT OF SCOPE (settled at their own grades; do not re-adjudicate):** A1–A3 themselves and the censorship theorem's mathematics (CONV-032, 5–0; the open path is RCORE-4); |R| = 1 (GR-1d V3, RCORE derivation); F-R1 and the Buchdahl placement (CONV-030, founder-ratified); the classical tests (GR-1i/CONV-029); T-1/R-CSTAR-MAP. If you believe an out-of-scope item is WRONG (not merely conditional), say so in DEFECTS — but the frozen questions do not ask about them.

## §3 Claim chain under review

- **C-1** §2 provenance table cites each input at its ratified strength — no silent upgrades (e.g., "unique" was withdrawn at CONV-032; the paper says "minimal"), no silent downgrades.
- **C-2** Eq. (1): Δt_ret = 2∫[r_surf, r_ph^ret] (√g_rr / α) dr, equatorial eikonal; retrograde ring r_ph^ret = 2M(1 + cos((2/3) arccos(+χ))).
- **C-3** The template table (χ = 0 → 0.95): 7.045 / 8.261 / 8.538 / 8.592 / 8.619 / 8.630 / 8.632 GM/c³; χ = 0 row equals the closed form (3/2 + 8 ln 2); monotone in χ.
- **C-4** Error budget: mass linear ⇒ ±6.5% at ±4 M_⊙; **spin saturation** dΔt/dχ = 0.299 GM/c³ at χ = 0.68 ⇒ ±0.35% at ±0.1 (the mandated CONV-032 rider, quantified — the worker's prior 3–10% guess failed the script's own first run and is recorded in the script header); eikonal-grade systematic named as unquantified, with finite-(ℓ,m) + surface co-rotation committed under amended RCORE-3 and required to PRECEDE search templates.
- **C-5** Amplitude ~5% of ringdown, parameter-free, spin-independent (inherited GR-1d V3; presented as a strike condition, not a fit knob).
- **C-6** Pro/retro discriminator: the prograde ring is inside the wall at remnant spins (χ = 0.68: ring 2.050 M vs wall 2.267 M), so retrograde keying is structural, not a fit choice; a prograde-keyed comb at χ > 0.55 falsifies CPP specifically.
- **C-7** Kill set (§6): (i) ergoregion-instability signature anywhere (with the interpretation calibration); (ii) prograde-keyed comb at χ > 0.55 (quantitative only after RCORE-3); (iii) the ergoregion + horizonless conjunction in one object; plus the null-search condition subject to the selection-function caveat (RCORE-2(viii)).
- **C-8** No new predictions; PRED-O-39 is the paper's single quantitative content; the saturation finding sharpens its error budget without a separate count; swarm count unchanged.

## §4 Triage — where the worker thinks this paper is weakest (attack here)

1. **"Effectively mass-only" (C-4/§3).** The saturation claim is computed at eikonal grade on the equatorial ring. Could finite-(ℓ, m) barrier structure or surface co-rotation restore an O(few %) spin dependence, making "mass-only" an overclaim at the phenomenology level even if correct at eikonal grade?
2. **The provenance table's compression (C-1).** Any inherited claim quietly stated above its source grade? The most dangerous candidates: the amplitude's "zero free parameters" (the barrier transmissivity's 5% is argument-level in GR-1d); the "in-band"/"unsearched" framing (is the 0.1–0.3 s characterization of published searches accurate and current?).
3. **The discriminator's strength (C-6).** Is "structural, not a fit choice" fair when horizon-ECO templates have their own parameter freedom? Could an ECO model mimic retrograde keying?
4. **The null-result framing (C-7).** Does the RCORE-2(viii) caveat under-commit — i.e., does the paper make a null search too easy to explain away?
5. **V0 assembly honesty (C-8).** Anything in the paper that is neither inherited nor script-verified?

## §5 Seat mandates (ALL SEATS — read before answering)

- **IDENTITY (mandatory):** in the §7 REVIEWER field put YOUR OWN actual model/provider name; never echo another seat's name, even if a name appears in text you were given.
  - **Gemini seat:** you have previously self-labeled as "ChatGPT" six times. State your identity as Gemini.
  - **DeepSeek seat:** at CONV-032 you self-labeled as "ChatGPT" (founder-confirmed identity-echo) while quoting this very mandate. State your identity as DeepSeek.
- **OWN-RUN:** SCRIPT-EXECUTED may be claimed ONLY for your own execution. Quoting the package's reference run is INSPECTED and will be reclassified if misclaimed.
- **COUNT-LINE:** if you execute, paste the script's own final count line verbatim ("9/9 PASS", or "FAST: 4/4 PASS" for a fast-only run).
- **FAST MODE (new, adopted at CONV-032):** `python 3329_gr2_template_verify.py --fast` runs four seconds-scale core checks with their own count line. A fast-only own run is a legitimate SCRIPT-EXECUTED claim scoped to those checks — say so.
- **INDEPENDENT-HARNESS (new category, adopted at CONV-032):** your own implementation + your own count line + an explicit statement of consistency or divergence vs the reference. Ranks between SCRIPT-EXECUTED and INSPECTED; claimable only with the harness described.
- **TIER LEGEND:** INSPECTED / INDEPENDENTLY RECOMPUTED / SCRIPT-EXECUTED / INDEPENDENT-HARNESS.

## §6 Per-seat steers

- **ChatGPT:** independently recompute the template table (any two rows) and the saturation slope; attack the "effectively mass-only" framing (triage 1). Your two rounds of own-run friction motivated FAST mode — please try it.
- **Grok:** own-run (full, fast, or independent harness — your CONV-032 harness is now legal vocabulary); audit the eikonal-grade honesty: is the unquantified eikonal systematic handled with adequate prominence for a search-facing paper?
- **Gemini:** audit the full error budget against the script (6.5%, 0.35%, 381 Hz, 21.96%); does §3 satisfy the error-bar mandate YOU set at CONV-032? Identity line above applies.
- **Copilot:** line-level discipline audit — every number in the prose against the script output and the provenance table against the cited sources; audit C-8 (no smuggled predictions; swarm discipline).
- **DeepSeek (falsifier seat):** is §6 the complete kill set? Is the ms-band-unsearched framing accurate against the published search literature you know? What would let a null result be explained away too easily? Identity line above applies.

## §7 Frozen questions + response skeleton

Answer ALL of Q1–Q7 with the given vocabulary.

- **Q1 (provenance).** Is the §2 input table FAITHFUL / MISSTATED(specify) to each source's ratified grade?
- **Q2 (template).** Eq. (1) + the table + the Schwarzschild limit: CORRECT / CORRECT-WITH-CAVEATS / INCORRECT?
- **Q3 (saturation finding).** dΔt/dχ = 0.299 GM/c³, ±0.35% at ±0.1: CONFIRMED / NOT-CONFIRMED — and is "effectively mass-only" CALIBRATED / OVERCLAIMED?
- **Q4 (claim discipline).** Conditionality prose (A1–A3, eikonal, W2/PSR), no-new-predictions posture: DISCIPLINED / OVERCLAIMS(specify).
- **Q5 (falsifiers + discriminator).** §5–6: SOUND / NEEDS(specify).
- **Q6 (completeness).** As the search-facing citable paper: COMPLETE / MISSING-ITEMS(list).
- **Q7a (assembly verdict).** PROPER / PROPER-WITH-REVISIONS / NOT-PROPER as a falsifier paper. **Q7b (ship path).** V1.0-PREP-CLEAR / RESTATE-REQUIRED / BLOCK.

**Binding rules:** majority per question; Q7b governs the status move; a sustained verdict-flipper on Q2 BLOCKS Q7b until a restate; Q4 OVERCLAIMS by majority forces RESTATE-REQUIRED regardless of Q7b tally.

**Skeleton:**
```
REVIEWER: <your own model name>
TIER LEGEND USED: INSPECTED / INDEPENDENTLY RECOMPUTED / SCRIPT-EXECUTED / INDEPENDENT-HARNESS
Q1: <verdict> [<tier>] — <2-6 sentences>
Q2: <verdict> [<tier>] — <2-6 sentences>
Q3: <CONFIRMED/NOT; CALIBRATED/OVERCLAIMED> [<tier>] — <2-6 sentences>
Q4: <verdict> [<tier>] — <2-6 sentences>
Q5: <verdict> — <2-6 sentences>
Q6: <verdict> — <1-4 sentences>
Q7a: <verdict>  Q7b: <verdict> — <1-3 sentences>
SCRIPT: <SCRIPT-EXECUTED (own run) + verbatim count line / INDEPENDENT-HARNESS (described) + own count line / INSPECTED (reference run) / NOT-EXECUTED (say why)>
DEFECTS/OBJECTIONS: <numbered list or NONE>
```

## §8 The paper under review (full source, V0)

```latex
% ==================================================================
% GR-2: The Echo Falsifier
% Millisecond Gravitational-Wave Echoes from Horizonless CPP Compact
% Objects: the Complete Retrograde-Keyed Template and What Kills It
% Second series paper of the CPP gravitation series (parent GR-1)
% V0 (Patch 3329, 21 Aug 2026): assembled on the founder-ratified
%   CONV-032 adjudication (5/5) with the complete input set: |R| = 1
%   (GR-1d V3, spin-independent), the Schwarzschild closed form
%   (3/2 + 8 ln 2) GM/c^3 (CONV-030), the derived Kerr exclusion
%   surface + ergoregion-censorship theorem (Patch 3320, conditional
%   on A1-A3), the prograde-burial finding (onset chi ~ 0.55), and
%   the binding error-bar rider. Verify script
%   series_gravitation/code/3329_gr2_template_verify.py, 9/9 PASS
%   (FAST subset 4/4 -- first enactment of the CONV-032 FAST-mode
%   adoption). Spin-saturation finding surfaced by the script's own
%   first run: dDt/dchi = 0.299 GM/c^3 at the benchmark, so the
%   +/-0.1 spin bar is +/-0.35% -- mass dominates ~20x.
% ==================================================================

\documentclass[12pt]{article}

\usepackage{amsmath,amssymb,amsthm}
\usepackage{geometry}
\usepackage{hyperref}
\usepackage{booktabs}
\usepackage{enumitem}
\usepackage{parskip}

\geometry{letterpaper, margin=1in}

\newtheorem{theorem}{Theorem}[section]
\newtheorem{proposition}[theorem]{Proposition}
\newcommand{\SSV}{\mathrm{SSV}}
\newcommand{\Msun}{M_\odot}

\title{\textbf{The Echo Falsifier:\\
Millisecond Gravitational-Wave Echoes from Horizonless\\
CPP Compact Objects}\\[6pt]
{\large Second series paper of the Conscious Point Physics
gravitation series (parent: GR-1)}}
\author{Thomas Lee Abshier, ND\\Hyperphysics Institute}
\date{21 August 2026 --- Version~0 (assembly draft)}

\begin{document}
\maketitle

\begin{abstract}
Conscious Point Physics predicts that black-hole merger remnants are
horizonless, hard-surfaced, maximally compact bodies whose surface
sits at exactly the Buchdahl radius (areal $\tfrac{9}{8}r_S$;
sector standing reading F-R1, founder-ratified CONV-030), with
gravitational-sector reflectivity $|R| = 1$ derived with zero free
parameters (GR-1d~V3).  Such objects \emph{must} echo.  This paper
assembles the complete falsifier: the echo-delay template
$\Delta t(M,\chi)$ at eikonal grade, keyed --- distinctively --- to
the \emph{retrograde} photon ring, because the derived Kerr exclusion
surface buries the prograde ring for remnant spins
$\chi \gtrsim 0.55$; the parameter-free first-echo amplitude
($\sim$5\% of ringdown); the observational discriminators separating
CPP from horizon-anchored exotic-compact-object templates; and the
explicit kill conditions.  Benchmark: for GW150914
($M = 62 \pm 4\,\Msun$, $\chi = 0.68$),
$\Delta t_{\rm ret} = 8.59\,GM/c^3 = 2.62$~ms
$\pm\,6.5\%$~(mass)~$\pm\,0.35\%$~(spin)~$\pm$~eikonal-grade
systematic, echo-comb spacing $f \approx 381$~Hz --- in the LIGO
band, in a delay range that published echo searches
($0.1$--$0.3$~s) have not examined.  A supporting result of the same
construction, the ergoregion-censorship theorem, removes the
ergoregion-instability objection to rapidly spinning horizonless
reflectors at every spin and reflectivity.  \textbf{Conditionality
stated first:} the spin sector of the template and the censorship
theorem are derivation-conditional on three stated census assumptions
A1--A3 (OPEN-GR-RCORE-4 carries their substrate derivation); the
delay is eikonal-grade pending finite-$\ell$ wall spectroscopy
(OPEN-GR-RCORE-3); and the whole chain inherits the W2/PSR
conditionality of the parent series.  Registered prediction:
PRED-O-39.
\end{abstract}

%======================================================================
\section{Introduction: a theory that hands over its own executioner}
\label{sec:intro}
%======================================================================

A physical theory earns credibility by exposing itself.  The CPP
gravitational arc reproduces the classical tests of general
relativity by construction (GR-1i) --- those results discriminate CPP
from Newton, not from GR, and the arc has said so plainly.  The place
where CPP \emph{departs} from GR is the compact-object interior: the
Exclusion floor censors the horizon, so the object that forms is a
horizonless, hard-surfaced body whose exterior is GR-identical but
whose surface reflects rather than absorbs.  Everything observable
about that departure funnels into one phenomenon: gravitational-wave
echoes, at a specific delay, a specific amplitude, and --- this
paper's central new content --- a specific \emph{keying} to the
retrograde photon ring.

This paper is the falsifier's handbook.  It contains no new
derivations; every input is inherited from a reviewed source, cited
at its ratified strength, and every number is reproduced by the
paper's verify script
(\texttt{code/3329\_gr2\_template\_verify.py}, 9/9~PASS; a FAST
subset of four core checks runs in seconds).  What is new is the
assembly: the template, the error budget, the discriminators, and
the kill conditions in one citable place, aimed at archived
LIGO/Virgo/KAGRA data.

%======================================================================
\section{Inputs and their provenance}
\label{sec:inputs}
%======================================================================

\begin{center}
\begin{tabular}{p{5.6cm}p{5.2cm}p{3.6cm}}
\toprule
\textbf{Input} & \textbf{Source and grade} & \textbf{Status}\\
\midrule
Horizonless hard surface at areal $\tfrac98 r_S$ (F-R1) &
GR-1c V2.3 + RCORE (Patch 3297); CONV-030 5/5; founder-ratified &
Sector standing reading\\
$|R| = 1$, phase $\pi$, zero free parameters &
GR-1d V3 (RCORE derivation); spin-independent &
Derived\\
Schwarzschild delay $(3/2 + 8\ln 2)\,GM/c^3$ &
CONV-030 (GPT seat independent re-derivation) &
Ratified\\
Kerr exclusion surface $\{s^2 + v^2 = 1\}$ &
Patch 3320; CONV-032 5/5 &
Derivation-conditional on A1--A3\\
Ergoregion censorship at every spin &
Patch 3320 theorem; CONV-032 Q4 CORRECT 5--0 &
Same conditionality\\
Prograde-ring burial, onset $\chi \approx 0.55$ &
Patch 3320 finding; CONV-032 Q5 CONFIRMED 5--0 &
Same conditionality\\
Error-bar rider (mass, spin, eikonal) &
CONV-032 Q5 binding adoption &
Mandatory, applied \S\ref{sec:template}\\
\bottomrule
\end{tabular}
\end{center}

The census assumptions, stated in full because they are the
conditionality: \textbf{A1} the scalar census is the ratified
log-lapse dictionary, $s = 2(1-\alpha)/(1+\alpha)$, exact at
$a = 0$ (a \emph{minimal} extension --- the CONV-032 round withdrew
the word ``unique'': static-limit exactness cannot force the
spinning extension); \textbf{A2} the rotational census is the ZAMO
dragging speed $v = \omega\varpi/\alpha$ in local reach units;
\textbf{A3} the demands compose in unweighted quadrature,
$F = s^2 + v^2$.  The panel's registered counterexample --- a
weighted law $F = s^2 + \gamma v^2$, $\gamma < 1$, preserves the
entire static sector yet can de-censor the ergosphere --- is why
A2/A3 are named load-bearing and why OPEN-GR-RCORE-4 (derive the
census functional from register dynamics) is the item that would
upgrade every spin-sector statement below from a theorem of the
census model to a physical theorem of CPP.

%======================================================================
\section{The delay template $\Delta t(M, \chi)$, retrograde-keyed}
\label{sec:template}
%======================================================================

The echo cavity is bounded inside by the reflecting surface and
outside by the photon-ring potential barrier.  At remnant spins the
derived surface swallows the \emph{prograde} equatorial ring
($\chi \gtrsim 0.55$; script check~7 puts the onset at
$\chi = 0.555$), so the surviving eikonal cavity is set by the
\emph{retrograde} ring: the round-trip delay is
\begin{equation}
\Delta t_{\rm ret}(M,\chi)
 = 2\int_{r_{\rm surf}(\chi)}^{r_{\rm ph}^{\rm ret}(\chi)}
   \frac{\sqrt{g_{rr}}}{\alpha}\,dr ,
\qquad
r_{\rm ph}^{\rm ret} = 2M\Bigl(1 + \cos\tfrac{2}{3}
  \arccos(+\chi)\Bigr),
\label{eq:delay}
\end{equation}
evaluated equatorially at eikonal grade, with the $\chi \to 0$ limit
machine-recovered against the closed form
$(3/2 + 8\ln 2)\,GM/c^3$ to four decimals (check~F1).

\begin{center}
\begin{tabular}{cccc}
\toprule
$\chi$ & $\Delta t_{\rm ret}$ [$GM/c^3$] &
$\Delta t_{\rm ret}$ [ms, $62\,\Msun$] & note\\
\midrule
0.00 & 7.045 & 2.151 & Schwarzschild closed form\\
0.30 & 8.261 & 2.523 & \\
0.55 & 8.538 & 2.607 & prograde-burial onset\\
\textbf{0.68} & \textbf{8.592} & \textbf{2.624} &
\textbf{GW150914 benchmark}\\
0.80 & 8.619 & 2.632 & \\
0.90 & 8.630 & 2.635 & \\
0.95 & 8.632 & 2.636 & \\
\bottomrule
\end{tabular}
\end{center}

\textbf{Error budget (the CONV-032 binding rider, quantified).}
The delay is exactly linear in $M$: the GW150914 mass uncertainty
$\pm 4\,\Msun$ gives $\pm 6.5\%$ (check~F4).  The spin bar was
mandated at $\pm\Delta\chi \sim 0.1$; \emph{quantifying it produced
this paper's one new finding}: above burial onset the template
\textbf{saturates in spin} --- $d\Delta t/d\chi = 0.299\,GM/c^3$ at
the benchmark, so $\pm 0.1$ in $\chi$ moves the delay only
$\pm 0.35\%$ (check~6).  The mass uncertainty dominates the spin
uncertainty by a factor $\sim\!20$.  The strong spin lever lives
\emph{below} onset ($2.151 \to 2.607$~ms across
$\chi = 0 \to 0.55$), which is observationally convenient: for the
merger-remnant population ($\chi \approx 0.6$--$0.75$) the template
is nearly a one-parameter (mass-only) family.  The remaining,
unquantified systematic is the eikonal grade itself: the
finite-$\ell$, $m$-dependent Kerr barrier is not the equatorial
ring, and the surface's own co-rotation $\omega(r_{\rm surf})$ is
not yet in the integrand --- both are committed work under the
amended OPEN-GR-RCORE-3 and \emph{must precede} any
matched-filter search template built from this paper.

The echo-comb spacing at the benchmark is
$f = 1/\Delta t \approx 381$~Hz (check~8) --- in-band, and in a
delay range (milliseconds) that the published echo searches, which
target $0.1$--$0.3$~s delays, have not examined.

%======================================================================
\section{Amplitude: five percent, no knobs}
\label{sec:amplitude}
%======================================================================

The first-echo amplitude is $|T_{\rm barrier}|^2 \approx 5\%$ of the
ringdown amplitude, inherited from GR-1d~V3 with \emph{zero free
parameters}: the wall reflectivity is $|R| = 1$ exactly (absorption
forbidden three ways: no register headroom at the Exclusion floor;
AP-4 DI-bit conservation; GR-1e fixed-point stability), and the
barrier transmissivity is fixed by the same geometry that fixes the
delay.  The $|R| = 1$ derivation is spin-independent, so the
amplitude carries over to the spinning template unchanged.  There is
nothing to tune: if ms-band echoes exist at the predicted delay but
at, say, $0.05\%$ amplitude, that is a strike against this chain,
not a fit opportunity.

%======================================================================
\section{The pro/retro discriminator}
\label{sec:discriminator}
%======================================================================

Horizon-anchored exotic-compact-object templates key their echo
delay to near-horizon crossing times and, where spin enters, to the
prograde ring.  CPP's cavity is retrograde-keyed at remnant spins
because the prograde ring is \emph{inside the wall} --- there is no
exterior prograde cavity to echo (check~9: at $\chi = 0.68$ the
prograde ring sits at $2.050\,M$ against a wall at $2.267\,M$).
The keying is therefore not a fit choice but a structural
discriminant: a detected comb whose spacing tracks the prograde
delay across a population of remnant spins would falsify CPP
specifically while remaining compatible with horizon-ECO models,
and vice versa.

%======================================================================
\section{What kills this theory}
\label{sec:falsifiers}
%======================================================================

Adopted at CONV-032 (Q6, closed by the designated falsifier seat,
with the GPT seat's interpretive calibrations):

\begin{enumerate}[label=(\roman*)]
  \item \textbf{An ergoregion-instability signature} ---
    exponentially growing GW emission tied to trapped
    negative-energy modes --- from any compact-object candidate.
    The censorship theorem predicts this never occurs, at any spin
    or reflectivity.  \emph{Calibration:} the interpretation must
    establish the source is the horizonless reflective body CPP
    predicts; rapid spin alone proves nothing.
  \item \textbf{A prograde-keyed echo comb at $\chi > 0.55$.}  CPP
    buries that ring; a robust comb demanding a persistent exterior
    prograde cavity contradicts the surface ordering directly.
    \emph{Calibration:} OPEN-GR-RCORE-3 must first make the
    finite-$\ell$ version of this statement quantitative.
  \item \textbf{The conjunction} of an independently established
    exterior ergoregion \emph{and} independently localized
    horizonless surface in the same object --- the strongest prong,
    since CPP forbids the ergoregion precisely when the surface is
    where CPP puts it.
\end{enumerate}

And the standing one: \textbf{a sufficiently sensitive ms-band echo
search that finds nothing} at the predicted delay and amplitude in
events where the template applies constrains the chain directly ---
subject to the search-systematics caveat registered as
OPEN-GR-RCORE-2(viii): the falsifier is only as sharp as the
search's selection function, and the published searches' selection
functions were built for delays two orders of magnitude longer.

%======================================================================
\section{Honest limits}
\label{sec:limits}
%======================================================================

(1)~Every spin-sector statement is conditional on A1--A3;
OPEN-GR-RCORE-4 is the discharge path, and until it lands the
censorship theorem and the burial finding are theorems of the census
model.  (2)~Eikonal grade: finite-$(\ell,m)$ wall spectroscopy and
surface co-rotation (amended OPEN-GR-RCORE-3) precede search
templates.  (3)~The Zel'dovich \emph{surface}-superradiance channel
(rotating-reflector amplification without an ergoregion) survives
censorship; growth-time bounds are committed under RCORE-3 ---
censorship of an exterior ergoregion does not dispose of
rotating-boundary amplification.  (4)~The chain inherits the parent
series' W2/PSR conditionality.  (5)~This paper is V0, not yet
panel-reviewed; its inputs are reviewed, its assembly is not.

%======================================================================
\section{Conclusion}
\label{sec:conclusion}
%======================================================================

CPP's compact objects must echo, at $2.62$~ms $\pm 6.5\%$ for
GW150914, at $5\%$ of ringdown, keyed to the retrograde ring, with
no ergoregion instability at any spin --- and the data that can
convict or acquit this chain is already on disk.  The template is
effectively mass-only for the remnant population (the spin
saturation finding), the band is unsearched, and the discriminator
against horizon-anchored alternatives is structural.  Archived data
can convict this theory.  That is the point.

%======================================================================
\section*{Keywords}
%======================================================================
gravitational-wave echoes; horizonless compact objects; Buchdahl
radius; exclusion surface; ergoregion censorship; retrograde photon
ring; prograde-ring burial; echo template; LIGO ringdown;
Conscious Point Physics

%======================================================================
\section*{Plain Language Summary}
%======================================================================
In this theory, a ``black hole'' is not a bottomless pit but a solid
object compressed to the absolute limit of space, with a surface
that reflects gravitational waves like a mirror.  When two of them
merge, the ringing of the merged object should be followed by faint
echoes --- arriving about $2.6$ thousandths of a second apart for an
event like GW150914, each about $5\%$ as loud as the ring itself.
Because the object spins, the echo timing is set by light circling
\emph{against} the spin (the with-spin path is swallowed inside the
surface) --- a fingerprint that distinguishes this theory from other
``no-horizon'' proposals.  Searches to date have looked for echoes
hundreds of times slower than this; the millisecond band predicted
here is unexplored, and the recordings that could prove or disprove
the prediction already exist.

%======================================================================
\section*{CP/GP Signature}
%======================================================================
The echo exists because the Exclusion floor --- the per-GP register
capacity that no census may exceed --- censors the horizon and
presents a full-register wall to incoming gravitational
perturbations ($|R| = 1$: no headroom to absorb, DI-bit conservation
forbids deletion, the GR-1e fixed point forbids restructuring).  The
spin sector adds the circulation register: the frame-dragging demand
$v = \omega\varpi/\alpha$ fills the register azimuthally, and where
$v = 1$ (the would-be ergosphere) circulation alone saturates it, so
total saturation --- the wall --- must stand outside.  The echo delay
is the round-trip light time in the cavity between that wall and the
retrograde ring, measured in the lattice's own reduced-reach steps.

%======================================================================
\section*{Mechanism Bridge}
%======================================================================
GR language: a horizonless ultracompact object with a reflective
surface at the Buchdahl radius supports a photon-sphere cavity;
perturbations leak through the potential barrier as delayed,
damped echo pulses.  CPP mechanism: the same cavity is the region
between the census-saturation surface and the unstable circular
null geodesic of the (exterior-exact) metric; reflectivity is
register conservation, not a material property; the spin correction
is the circulation census, not an independent postulate.

%======================================================================
\section*{Swarm-Validation Statement}
%======================================================================
This paper registers no new predictions.  Its single quantitative
content is PRED-O-39 (registered Patch 3326 on the founder-ratified
CONV-032 adjudication): the retrograde-keyed ms echo comb with the
error budget of \S\ref{sec:template}.  The spin-saturation finding
(\S\ref{sec:template}) sharpens PRED-O-39's error budget but is not
counted separately.  Swarm count unchanged.

%======================================================================
\section*{Verification}
%======================================================================
\texttt{series\_gravitation/code/3329\_gr2\_template\_verify.py} ---
9/9 PASS.  FAST subset (4/4, seconds-scale, own count line; first
enactment of the CONV-032 FAST-mode dispatch adoption): Schwarzschild
closed-form recovery; the GW150914 benchmark
($8.592\,GM/c^3$, $2.624$~ms, $+21.96\%$); censorship and burial at
$\chi = 0.68$; mass linearity.  Full run adds: the template table;
the spin-saturation quantification ($d\Delta t/d\chi = 0.299$,
$\pm 0.35\%$ at $\pm 0.1$); burial onset $\chi = 0.555$;
$f_{\rm echo} = 381$~Hz; the absent-prograde-cavity discriminator.
The script's own first run corrected the worker's prior expectation
of a $3$--$10\%$ spin bar --- recorded in the script header per
computation-before-claims.

%======================================================================
\begin{thebibliography}{9}
%======================================================================
\bibitem{gr1} T.~L.~Abshier, ``Local Gravitation from SSV Shell
Broadcast'' (GR-1, V1.0), CPP gravitation series parent, 2026.
\bibitem{gr1c} T.~L.~Abshier, ``Strong-Field GR'' (GR-1c, V2.3.1),
2026 --- exact isotropic Schwarzschild; horizonless reading
(CONV-030 ratified).
\bibitem{gr1d} T.~L.~Abshier, ``Gravitational-Wave Echoes''
(GR-1d, V3), 2026 --- $|R| = 1$ derived; Schwarzschild delay
closed form.
\bibitem{gr1f} T.~L.~Abshier, ``The Kerr Metric from Rotational
SSV'' (GR-1f, V1.2), 2026.
\bibitem{gr1h} T.~L.~Abshier, ``Superradiance'' (GR-1h, V1.2),
2026 --- ergoregion-instability item resolved by censorship.
\bibitem{kerr3320} CPP Patch 3320, ``The Kerr Exclusion Surface and
the Ergoregion-Censorship Theorem,''
\texttt{rcore\_derivation/3320\_kerr\_surface\_derivation.md};
CONV-032 adjudication v1.0 (5/5).
\end{thebibliography}

\end{document}
```

## §9 The verify script (full source)

Also delivered to execution-capable seats as a separate `.py` file per the CONV-031 dispatch-design adoption. Reference run: 9/9 PASS; FAST: 4/4 PASS.

```python
#!/usr/bin/env python3
"""3329_gr2_template_verify.py — GR-2 "The Echo Falsifier" V0 verify.

Computation-before-claims for every number quoted in GR-2 V0:
the retrograde-keyed echo-delay template Dt(M, chi), its Schwarzschild
limit, the GW150914 benchmark, the mass/spin error-bar quantification
(the CONV-032 binding rider), the prograde-burial onset, and the
echo-comb frequency.

FAST MODE (CONV-032 adoption, first enactment): checks tagged [FAST]
run in seconds and emit their own count line, so a time-boxed review
seat can own-run the core identities without the full scan.
    python 3329_gr2_template_verify.py --fast
Full run appends the scan-grade checks and the final count line.

Machinery inherited from code/3320_kerr_surface_derivation_verify.py
(Boyer-Lindquist, G = c = M = 1; equatorial eikonal grade).
"""
import sys
import numpy as np

FAST_ONLY = "--fast" in sys.argv

PASS, FASTPASS = [], []


def check(name, ok, detail="", fast=False):
    (FASTPASS if fast else PASS).append(bool(ok))
    tag = "[FAST]" if fast else "      "
    print(f"{tag}[{'PASS' if ok else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))


# ---------------------------------------------------------------- geometry
def alpha_n(r, a, th=np.pi / 2):
    D = r * r - 2 * r + a * a
    S = r * r + a * a * np.cos(th) ** 2
    Aa = (r * r + a * a) ** 2 - D * a * a * np.sin(th) ** 2
    return np.sqrt(max(D * S / Aa, 0.0))


def v_n(r, a, th=np.pi / 2):
    D = r * r - 2 * r + a * a
    S = r * r + a * a * np.cos(th) ** 2
    Aa = (r * r + a * a) ** 2 - D * a * a * np.sin(th) ** 2
    om = 2 * a * r / Aa
    gpp = Aa * np.sin(th) ** 2 / S
    al2 = D * S / Aa
    return om * np.sqrt(gpp / al2) if al2 > 0 else np.inf


def F_n(r, a, th=np.pi / 2):
    al = alpha_n(r, a, th)
    s = 2 * (1 - al) / (1 + al)
    return s * s + v_n(r, a, th) ** 2


def r_E(a, th=np.pi / 2):
    return 1 + np.sqrt(max(1 - a * a * np.cos(th) ** 2, 0.0))


def r_surface(a, th=np.pi / 2):
    lo, hi = r_E(a, th) * (1 + 1e-10), 60.0
    if F_n(lo, a, th) <= 1:
        return None
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if F_n(mid, a, th) > 1:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def r_ph(a, prograde=True):
    sgn = -1 if prograde else +1
    return 2 * (1 + np.cos(2.0 / 3.0 * np.arccos(sgn * a)))


def delay(a, r_in, r_out, n=200_000):
    rs = np.linspace(r_in, r_out, n)
    grr = rs * rs / (rs * rs - 2 * rs + a * a)
    al = np.array([alpha_n(r, a) for r in rs])
    integ = np.sqrt(np.maximum(grr, 0)) / np.maximum(al, 1e-12)
    return 2 * np.trapezoid(integ, rs)


GM_c3_per_Msun = 4.92549e-6  # seconds
M0, dM = 62.0, 4.0           # GW150914 remnant, GR-1d V3 error-bar mandate
CHI0 = 0.68


def dt_ret(a, M=M0):
    rs = r_surface(max(a, 1e-9))
    return delay(max(a, 1e-9), rs, r_ph(max(a, 1e-9), prograde=False)) * M * GM_c3_per_Msun


# ============================== FAST GROUP ==============================
# F1: Schwarzschild closed form recovered
dt_schw_num = delay(1e-9, 2.25, 3.0)
dt_schw_exact = 1.5 + 8 * np.log(2)
check("F1. Schwarzschild limit: numeric eikonal = (3/2 + 8 ln 2) GM/c^3",
      abs(dt_schw_num - dt_schw_exact) < 0.01,
      f"{dt_schw_num:.4f} vs {dt_schw_exact:.4f}", fast=True)

# F2: GW150914 benchmark — the PRED-O-39 numbers
dt68_geo = delay(CHI0, r_surface(CHI0), r_ph(CHI0, False))
dt68_ms = dt68_geo * M0 * GM_c3_per_Msun * 1e3
spin_corr = dt68_geo / dt_schw_exact - 1
check("F2. GW150914 benchmark: Dt_ret(0.68) = 8.59 GM/c^3 = 2.62 ms; +22% spin correction",
      abs(dt68_geo - 8.59) < 0.02 and abs(dt68_ms - 2.62) < 0.02
      and abs(spin_corr - 0.22) < 0.005,
      f"{dt68_geo:.3f} GM/c^3; {dt68_ms:.3f} ms; +{100*spin_corr:.2f}%", fast=True)

# F3: censorship spot-check at the benchmark spin
rsurf68, rE68 = r_surface(CHI0), r_E(CHI0)
check("F3. censorship at chi=0.68: surface strictly outside the ergosphere; prograde ring buried",
      rsurf68 > rE68 and r_ph(CHI0, True) < rsurf68,
      f"r_surf={rsurf68:.3f} M > r_E={rE68:.3f} M; r_ph_pro={r_ph(CHI0, True):.3f} M inside",
      fast=True)

# F4: mass-linearity + the +/-6.5% mass error bar
lin = dt_ret(CHI0, M0 + dM) / dt_ret(CHI0, M0)
mass_frac = dM / M0
check("F4. mass linearity: Dt proportional to M; +/-4 Msun => +/-6.5%",
      abs(lin - (1 + mass_frac)) < 1e-6 and abs(mass_frac - 0.0645) < 0.001,
      f"ratio {lin:.5f} vs {1+mass_frac:.5f}; fractional {100*mass_frac:.2f}%", fast=True)

print(f"FAST: {sum(FASTPASS)}/{len(FASTPASS)} PASS")
if FAST_ONLY:
    raise SystemExit(0 if all(FASTPASS) else 1)

# ============================== FULL GROUP ==============================
# 5: the Dt(chi) template table quoted in GR-2 Table 1
table_chis = [0.0, 0.30, 0.55, 0.68, 0.80, 0.90, 0.95]
rows = []
for chi in table_chis:
    g = delay(max(chi, 1e-9), r_surface(max(chi, 1e-9)), r_ph(max(chi, 1e-9), False))
    rows.append((chi, g, g * M0 * GM_c3_per_Msun * 1e3))
    print(f"      table: chi={chi:.2f}  Dt_ret={g:7.3f} GM/c^3  = {rows[-1][2]:.3f} ms @ 62 Msun")
mono = all(rows[i + 1][1] > rows[i][1] for i in range(len(rows) - 1))
check("5. template table computed; Dt_ret monotone increasing in chi; chi=0 row = Schwarzschild",
      mono and abs(rows[0][1] - dt_schw_exact) < 0.01,
      f"chi=0 row {rows[0][1]:.4f} vs closed form {dt_schw_exact:.4f}")

# 6: spin error bar for the binding rider — dDt/dchi at the benchmark.
# FINDING (this script's own first run): the worker's prior expectation was a
# 3-10% band; the computed slope is 0.299 GM/c^3 per unit chi, i.e. +/-0.1 in
# chi moves Dt by only ~0.3% — the template SATURATES in spin above burial
# onset (table rows: 8.538 -> 8.632 across chi = 0.55 -> 0.95). The mass
# uncertainty (+/-6.5%) therefore DOMINATES the spin uncertainty by ~20x at
# the benchmark; the strong spin lever lives BELOW onset (2.151 -> 2.607 ms
# across chi = 0 -> 0.55). Check re-pointed to the computed behavior;
# original expectation recorded here per computation-before-claims.
eps = 0.02
slope = (delay(CHI0 + eps, r_surface(CHI0 + eps), r_ph(CHI0 + eps, False))
         - delay(CHI0 - eps, r_surface(CHI0 - eps), r_ph(CHI0 - eps, False))) / (2 * eps)
dchi = 0.10
spin_bar = slope * dchi / dt68_geo
check("6. spin error bar QUANTIFIED: template saturates above onset; +/-0.1 in chi => sub-percent band",
      0.05 < slope < 1.0 and spin_bar < 0.01,
      f"dDt/dchi = {slope:.3f} GM/c^3 per unit chi; +/-0.1 => +/-{100*spin_bar:.2f}% "
      f"(mass bar +/-6.5% dominates ~20x)")

# 7: prograde-burial onset
a_pb = None
for a in np.linspace(0.01, 0.998, 300):
    rs_ = r_surface(a)
    if rs_ is not None and r_ph(a, True) <= rs_:
        a_pb = a
        break
check("7. prograde-burial onset chi ~ 0.55 (retrograde keying begins)",
      a_pb is not None and abs(a_pb - 0.55) < 0.02, f"onset chi = {a_pb:.3f}")

# 8: echo-comb frequency in the LIGO band
f_echo = 1.0 / (dt68_ms * 1e-3)
check("8. echo-comb spacing f = 1/Dt ~ 380 Hz at the benchmark — IN the LIGO band",
      abs(f_echo - 380) < 10 and 20 < f_echo < 2000, f"f_echo = {f_echo:.1f} Hz")

# 9: pro/retro discriminator margin — the buried-ring counterfactual delay
dt_pro_cf = delay(CHI0, r_surface(CHI0), r_ph(CHI0, True) if r_ph(CHI0, True) > r_surface(CHI0)
                  else r_surface(CHI0) * 1.0001)
check("9. discriminator: the prograde-ring cavity is ABSENT (ring inside the wall) — "
      "a prograde-keyed comb at this spin is a falsifier, not a fit option",
      r_ph(CHI0, True) < r_surface(CHI0) and dt_pro_cf < 0.1,
      f"prograde ring {r_ph(CHI0, True):.3f} M vs wall {r_surface(CHI0):.3f} M; "
      f"no exterior prograde cavity exists")

allpass = FASTPASS + PASS
print(f"{sum(allpass)}/{len(allpass)} PASS")
raise SystemExit(0 if all(allpass) else 1)
```
