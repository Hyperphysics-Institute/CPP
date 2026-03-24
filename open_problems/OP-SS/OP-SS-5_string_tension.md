# OP-SS-5: String Tension $\sigma$ from sea\_strength

**Priority:** HIGH  
**Status:** PARTIAL — mechanism established; one dimensional-analysis step remaining  
**Series:** SS\#4; companion C14  
**Notebook evidence:** `notebooks/chain_fraying_dynamics.ipynb` (Stage 13),
`notebooks/zbw_magnetic_effects.ipynb` (Stage 16)  
**Last updated:** 23 March 2026

---

## Statement

Derive $\sigma \approx 0.9$~GeV/fm from sea\_strength $= 0.185$ and
600-cell geometry, without calibrating to the charmonium spectrum.

---

## What is Known

### 1. The self-consistent relation (C14, confirmed Stage 13)

$$\sigma = \frac{\alpha_s \hbar c}{r_\text{conf}^2}, \qquad
r_\text{conf} = \sqrt{\frac{\alpha_s \hbar c}{\sigma}}$$

These two equations are the same; they close self-consistently at:
$$r_\text{conf} = 0.161\ \text{fm}, \qquad \sigma = 0.900\ \text{GeV/fm}\ \checkmark$$

### 2. The bow rigidity mechanism (`chain_fraying_dynamics`, Stage 13)

The qDP chain bows transversely under separation.  The bow amplitude
is $\text{bow\_factor} \sim l_P / r_\text{chain}$.  The linear
potential $V \propto r$ arises because the bow costs energy
proportional to chain extension.

$$\sigma \sim \frac{\alpha_s \hbar c}{r_\text{conf}^2}
\quad \text{when bow becomes critical at } r = r_\text{conf}$$

### 3. The ZBW perturbation (`zbw_magnetic_effects`, Stage 16)

ZBW Lorentz forces amplify the bow by $\sim 5\text{–}10\%$:
$$\text{bow\_factor}_\text{total} = 0.15 \times (1 + \delta_\text{ZBW})
\approx 0.157\text{–}0.165$$

This is a minor correction to $\sigma$.

### 4. String breaking is sequential (Stage 22)

Outer chains break first (strength 0.4), middle chains next (0.7),
central last (1.0).  The final central break triggers pair production.
This predicts a multi-stage energy release spectrum.

---

## What Remains

**The one missing step:** Express
$$\text{bow\_factor} \sim \frac{l_P}{r_\text{conf}}$$
in terms of sea\_strength alone.  This requires showing that
$r_\text{conf}$ is determined by the condition at which the DP Sea
can no longer supply new qDP chains fast enough to self-collimate:

$$r_\text{conf} = f(\text{sea\_strength},\ l_P,\ \phi)$$

Once $r_\text{conf}$ is derived this way, $\sigma = \alpha_s \hbar c /
r_\text{conf}^2$ follows without any calibration.

**Approach:** The DP Sea chain formation rate scales as sea\_strength
$\times c / r$.  Self-collimation requires the formation rate to exceed
the separation rate.  The threshold $r_\text{conf}$ is where these
balance — a dimensional-analysis calculation.

---

## Falsifiable Predictions from Existing Work

1. **~85% central string breaking** (chain\_fraying, Stage 13) — vs.\
   QCD Schwinger uniform distribution.
2. **Multi-stage energy spectrum** (strong\_modes, Stage 22) — three
   distinct release steps.
3. **Helix signature in polarised jets** (zbw\_magnetic, Stage 16).

---

## Feeds Into

- OP-SS-7 ($\Lambda_\text{QCD}$ self-consistently from PSR)
- OP-SS-10 (nuclear binding — needs $r_\text{conf}$ as the internucleonic force range)
- OP-SS-6 (glueball mass — needs the cell-loop energy from $\sigma$)
