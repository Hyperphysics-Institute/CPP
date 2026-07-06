# A Reader's Guide to DM-1

*For the physicist encountering Conscious Point Physics cold.*

You have in front of you a dark-matter candidate paper from a framework you have probably never heard of,
carrying a claim that will strike you as too good — a zero-parameter constant landing a screening length
inside the empirically required window — wrapped in an unfamiliar vocabulary. This guide exists so that you
can evaluate the paper in about an hour without first adopting anyone's ontology. Our request is simple:
read it the way you would read a phenomenological effective-theory paper with an unusual microphysical
ansatz. Everything below tells you what is claimed, what nearly killed it, what was measured, what can still
kill it, and how to check the arithmetic yourself.

## 1. The five inputs you actually need

Conscious Point Physics (CPP) posits a discrete substrate — a lattice of bound dipoles with 600-cell
geometry, which builds the golden ratio φ into its structure. Whatever you think of that, **this paper's
results depend on only five registered inputs**, all fixed elsewhere in the programme before this campaign
began:

| Input | Value | Role here |
|---|---|---|
| lattice pitch *a* ≈ r_c | 1.0–1.3 fm | the length unit; element spacing in the rod |
| element mass m_el | 1408 MeV | sets m_rod = N·m_el ≈ 25.3 GeV at N = 18 |
| a colour-residual channel | Yukawa-screened by the medium | the interaction |
| rod–rod contact residual E_c | ≈ 0.3 MeV | normalizes the coupling |
| the constant χ | φ⁻³/6 ≈ 0.0393 | see below |

The constant χ matters most. It was **not introduced for dark matter**: it is the "Capotauro constant," the
substrate-chirality matrix element the programme derived earlier to account for the leptogenesis CP
asymmetry (a separate paper, separate data, 2% match). Its reappearance here is the paper's central event.

## 2. The claim

Dark matter is identified with the **Cross-Rod**: an aggregate of N ≈ 15–20 colour-balanced substrate
elements, mass ≈ 25.3 GeV, electromagnetically dark, self-interacting through *capture* mediated by the
screened colour-residual channel. Self-interacting dark matter phenomenology demands a screening length of
roughly 20–30 fm to put the dwarf-galaxy cross-section in the literature window [1, 5] cm²/g at 50 km/s.
The zero-parameter value

**R_s = r_c/χ = 25.4 fm — equivalently a channel gap m_s = χ·(ħc/r_c) = 7.76 MeV**

lands inside it. The same curve, with the elastic floor **measured** by rigid-body Monte Carlo at the
registered rod geometry (not fixed by convention — see §3), then passes low-surface-brightness galaxies,
the entire cluster bound ladder including the tightest bound (Andrade < 0.13 cm²/g, cleared ×2.7–4.5), and
the Bullet cluster, while **predicting** a group-scale σ/m ≈ 0.03–0.05 — an order of magnitude below the
current mild positive measurement (0.5 ± 0.2). In one sentence: *a constant this programme already owned,
for unrelated physics, sets the dark-matter interaction range correctly with nothing to tune — and sticks
its neck out at group scales.*

## 3. What nearly killed it (twice), on the record

If you check only one thing about an unfamiliar programme, check how it behaves when its own numbers turn
against it. That happened twice, and both records are in the paper's layered revision notices.

**The floor correction chain (v1.1 → v1.2).** The elastic-floor convention the programme had been carrying
overestimated transport by ×4–6; composing it with the capture term exposed a cluster-ladder violation. Four
computations in sequence — including one *retracted intermediate claim*, retained in the record — replaced
the convention with a directly measured floor. Caught in-house; the review panel was shown the entire chain.

**The baryon sector (v1.2 → v1.3).** The same rod–nucleon coupling the programme had used for a
nuclear-physics argument implies exposure to the XQC sounding-rocket calorimeter. A partial-wave
recomputation (the Born approximation fails badly here — the guide's authors solved the actual scattering
problem, validated to 0.1% in the weak-coupling limit) **excluded the naive coupling by a factor of
20–30**, and a claim the panel had ratified three days earlier was formally retracted. Survival requires
suppressing the rod–*nucleon* coupling into a narrow island, S_c ∈ [0.012, 0.05], whose center happens to be
the natural first-multipole scale R_N/R_s = 0.035. That value was adopted as an **explicitly provisional,
survival-conditional ruling — disclosed in the paper in exactly those words** — with its derivation left as
a standing target whose failure modes remain lethal (§5).

## 4. What was measured — the effective-theory turn

Rather than pretend the substrate's depths are understood, the programme adopted (and registered as
convention) a measured-coefficient discipline: claim the structure, let data fix the coefficients — Galileo
before Newton. Under it, m_s and S_c are the substrate's first two *measured* quantities, and inverting the
full data set through registered-structure forward maps yields the first empirical portrait of the medium:
colour coupling α_q ≈ 0.9; channel ladder α_e/α_q ≈ 6×10⁻³; **colour-channel cancellation
C_r ≈ 2.4×10⁻⁴** (the quiescent medium cancels the channel to parts in 10⁴); occupancy f_occ ≈ 0.1 — a
sparse lattice. The under-determined directions are flagged as prior-shaped in the table itself; the
counting (6 hard equations, 8 unknowns) is printed, not hidden; and the inversion carried a pre-registered
kill-condition — an empty solution region would have structurally falsified the candidate. It did not fire.

## 5. What can still kill it

This model is unusually killable, on purpose. In rough order of nearness:

- **Group scale (F1):** the model predicts σ/m ≈ 0.03–0.05 at ~1150 km/s, sitting 2.3σ *below* a published
  mild detection. If group-scale analyses firm up 0.5 with systematics controlled, the model dies.
- **An XQC-class reflight (F5):** predicted 8–50 recoil events (median ~17) against an instrument whose
  2007 flight recorded 527 — a factor ~30 in sensitivity. A modern flight is a direct test.
- **The derivation kill-branches (F3′):** the provisional coupling ruling must eventually *derive* to first
  multipole order. Zeroth order → excluded by XQC. Second order → excluded by LZ. The escape hatch is a
  coin with three faces and two of them lethal.
- **np-scattering precision (F2), the dSph grazing tension, the deep-Earth thermalized population (F6)** —
  each documented with its current margin.

## 6. How to check the numbers (a 30-minute audit path)

Every load-bearing number has a runnable verification (Python, stdlib/numpy) and a verbatim reasoning
fragment. From the repo root:

1. `python3 code/1865_empirical_dwarf_pin_recalibration.py` — the literature pin and the χ landing.
2. `python3 code/1871_soft_rod_mc_pinned_geometry.py` — the measured floor (worker mode; results JSON included).
3. `python3 code/1879_xqc_recomputation.py` — the exclusion that forced the retraction (partial-wave solver
   + full Erickcek-2007 exposure model; the Born-limit validation prints first).
4. `python3 code/1888_si2_scan_and_predictions.py` — the substrate portrait and the no-refit predictions.

The chronological lab notebook is `OPEN-SS-43_Rs_derivation.md` (§§1–31). The three adversarial review
cycles — five independent frontier AI systems per cycle, verbatim returns archived — are in `DM-1/review/`;
if you read one, read the v1.3 cycle, in which the panel unanimously ratified the retraction of a claim it
had itself ratified days earlier.

## 7. What this is not, and the objections we agree with

It is not a derivation of χ from the substrate — that remains open, and the paper says so. The AI review
panel is not community peer review: it audits internal consistency, arithmetic, and honesty of claims, not
the framework's validity — that job is yours. The substrate portrait is a constrained region, not a unique
solution. A pairwise-additivity assumption (tagged J4 throughout) underlies the coupling structure. And the
survival-conditional ruling of §3 is exactly what it sounds like — which is why it is stated in the paper
rather than smuggled.

The skeptical posture we would adopt in your position: ignore the ontology, treat the paper as an EFT with
pre-registered falsifiers, and shoot at F1 and F5. If the model is wrong, one of them should kill it. If
they keep missing, the constant that set the range — φ⁻³/6, derived for the matter–antimatter asymmetry —
will need an explanation from somebody.

*Corpus: github.com/Hyperphysics-Institute/CPP · OSF parent DOI 10.17605/OSF.IO/JXE8D · Hyperphysics
Institute, Thomas Lee Abshier, ND. The wider programme claims 100+ zero-parameter results across other
sectors; this guide deliberately defends only the paper in front of you.*
