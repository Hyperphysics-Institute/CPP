# A_i's Source Coefficient Is G — and That Explains the Whole Session

> **⚠ §§2–5 WITHDRAWN AT PATCH 4174. The Einstein–Cartan identification they rest on FAILED.**
> **EC torsion is non-propagating** — an algebraic field equation, tied point-by-point to local spin
> density, no independent degrees of freedom — while **A3′ has every channel *"propagating at
> c = l_P/t_P"*** and the amendment adds A_i as a fourth channel of that packet. **A propagating
> axial field is not torsion.** So: the coefficient is **not** shown to be G (TODO-4172-SOURCEEQ
> reopens), the contact-term smallness does **not** explain A_i's emptiness, and the early-universe
> redirection is withdrawn. §1's dimensional analysis stands on its own. §6 predicted this.
> Retained verbatim. See `4174_torsion_identification_fails.md`.

**Patch:** 4173. **Lane:** EW/GR. **Session:** 234.
**Discharges:** TODO-4172-SOURCEEQ.
**Verify:** `series_standard_model/code/4173_source_equation.py`.

---

## 1. The dimensional question, and the answer

A3′: *"Q_ij sourced by −(16πG/c⁴) T_ij^{TF}."* T_ij is an energy density; **spin density s_i carries
one factor of time more.** So the same coefficient cannot act on s_i directly. The natural bridge is
one factor of c over a length —

  **source_A = c (∇ × s)**  [J/m³, matching T_ij]

— which is the construction magnetisation already uses to source a magnetic field (B from ∇×M).
**No new constant is introduced.**

## 2. The coefficient is not a new parameter

In Einstein–Cartan, **spin sources torsion with the same κ = 8πG/c⁴ = 2.08×10⁻⁴³ m/J that sources
curvature.** Torsion introduces no new coupling. If A_i is CPP's torsion channel (4172 §4), the
amendment inherits that, and:

> **The missing coefficient is G, which A3′ already carries. The zero-parameter claim survives.**

That is the good outcome TODO-4172-SOURCEEQ was asking about, and it is the one I did not expect.

## 3. And Einstein–Cartan tells us how big — the answer has been known since the 1970s

EC torsion is **non-propagating**: it gives a **contact spin–spin term** of energy density ~ (κ/2)s².
Evaluated at real spin densities:

| system | n (m⁻³) | s = nħ | u (J/m³) | vs system scale |
|---|---|---|---|---|
| polarised iron | 8.5×10²⁸ | 9.0×10⁻⁶ | 8.4×10⁻⁵⁴ | 8×10⁻⁵⁹ |
| nuclear matter | 1.7×10⁴⁴ | 1.8×10¹⁰ | 3.3×10⁻²³ | 3×10⁻⁵⁵ |
| neutron-star core | 5.0×10⁴⁴ | 5.3×10¹⁰ | 2.9×10⁻²² | 3×10⁻⁵⁶ |

**Everywhere accessible the term is ~55 orders too small.** That is the standard EC result, **and it
is not a CPP failing.**

## 4. The consilience — it reframes the session

**Four independent routes today found A_i empirically empty:**

- 4155 §4 — no distinctive signature; only magnetism;
- 4165 §6 — b does not read the register;
- 4170 §3 — spin-mixing bounded at ε ≤ 5×10⁻⁴⁷ per Moment;
- 4171 §1 — neither identified job is a prediction.

**If A_i is the torsion channel, that is the expected answer, not a defect.** Torsion is famously
unobservable at accessible densities. **The amendment was being judged by a standard its own physics
does not meet and was never going to.** Four patches of mounting suspicion, and the suspicion was
misdirected.

I want to be careful about how much this rescues. It does **not** make A_i predictive; it explains
*why* it is not, and moves the emptiness from "unexplained deficiency" to "known property of this
kind of channel." That is a real improvement in understanding and **no improvement at all in
testability.**

## 5. Where A_i would matter — a genuine redirection

EC torsion becomes significant at the **Cartan density**, n ~ mc²/(κħ²) ≈ **6.5×10¹⁰⁰ m⁻³** —
**3.8×10⁵⁶ times nuclear density.** So **not** the laboratory, and **not neutron-star cores either**.
**Only the early universe reaches it** — which is exactly where the EC literature puts torsion:
singularity avoidance, bouncing cosmologies.

**CPP has an early-universe lane, and none of this session's work looked at it.** That is where this
channel should be tested. Filed as **TODO-4173-EARLYUNIVERSE**.

## 6. PD-008 — the convenient branch, marked

This patch is the most favourable result of the session for χ₄ and I want the caveats attached, not
trailing. **The whole of §2–§5 is conditional on 4172 §4's Einstein–Cartan identification, which is
my proposal and is not in the corpus.** If A_i is *not* torsion, the coefficient is unknown again and
the zero-parameter claim is back in question. I have written §2 as "if", and the next window should
check whether the identification is earned or merely attractive — it is attractive precisely because
it resolves four separate problems at once, which is exactly when a proposal deserves more scrutiny,
not less.

## 7. Status

TODO-4172-SOURCEEQ discharged **conditionally on the torsion identification**. No verdict moved. χ₄
provisionally adopted. **F5 remains the blocker.**
