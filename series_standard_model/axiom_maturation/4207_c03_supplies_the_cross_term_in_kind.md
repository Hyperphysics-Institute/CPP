# c03 Supplies Interference in Kind: SSV Contributions Add as Vectors Before Selection

**Patch:** 4207. **Lane:** EW. **Session:** 236.
**Verify:** `series_standard_model/code/4207_refill_amplitudes_from_lambda.py`.
**Works:** the c03 check owed at 4206. **Result:** the mechanism exists in the corpus as a
conjecture; the number λ maps onto it cleanly; the Fermi-limit repair needs more than c03 gives.

---

## 1. What c03 says (read at lines 137–160 and 296–340)

- **Proposition (two-system superposition):** the "indefinite" state is the organised aggregate's
  SSV plus the Sea's fluctuating SSV, superimposed at each tick.
- **Conjecture (two-quadrature Born rule):** at each tick the net SSV at the GP is the **vector sum**
  of the aggregate's contribution for each outcome (fixed direction, amplitude A_i) and the Sea's
  two-quadrature ZBW fluctuation; the fraction of ticks in which the 12-edge selection points to
  outcome i is ∝ A_i². Stated as *suggestive, not rigorous* — "the most important open problem in
  the CPP program."

**So the refill fits c03's shape exactly:** a Sea DP is drawn into the core's orbit; the two
candidate senses are two SSV contributions at the core's GP; **they add as vectors before the
selection fires**, and the outcome probability is the squared magnitude of the sum — **which
contains the cross term 2 A_same·A_opposite.** Interference is not something the model must add;
it is what c03's mechanism does whenever two outcome contributions coexist at one GP. **4206's
"classical alternatives" was my modelling, not the corpus's.**

## 2. λ in c03's language — rows verbatim (D-11)

```
measured lambda = -1.2754
amplitude ratio |A_opposite| / |A_same|   = 1.2754
probability of the opposite sense (GT)     = 3 l^2/(1+3 l^2) = 0.830   (per-state l^2/(1+l^2) = 0.619)
4203's f in amplitude language             = (l^2-1)/(l^2+1) = 0.239   (per-state)
relative sign of the two amplitudes         = opposite  (lambda < 0 in the convention where the cross term in A is +2|l|)
cross-term share of A                       = 2|l| / (2 l^2 + 2|l|)... i.e. A = [-2 l^2 + 2|l|]/(1+3 l^2) = -0.119
```

The measured g_A/g_V is then **the ratio of the two refill-sense SSV amplitudes at the core's GP**,
with the opposite sense 1.275× the same sense and the two **anti-phased**. 4203's f = 0.24 is the same
statement in probability language. **This is what would be computed** once the DP-arc / persistence
input exists (4203): the arcs left by the departed DP are the "aggregate contribution" that biases
the refill, and c03 says to square the vector sum.

## 3. What c03 does not give

The Fermi-limit failure (4206 §3) is about **spin**, not about which sense wins: a singlet gives
neither lepton a definite spin. c03's amplitudes are SSV *directions* at one GP; the lepton pair's
spin correlation needs the ejection of two leptons to be one coherent event across two GPs (the
electron's and the Sea partner's). Reproducing the full a, A, B — that is, **V−A itself** — from CPP
amplitudes is the same job as deriving the weak-vertex structure, and it is the arc this session
has been circling since 4193. **It is a window's work, not a patch's.**

## 4. Handover recommendation (PD-006: mine to decide; recorded, not executed — founder prefers
long sessions)

The arc 4191–4207 has a clean statement now. A next window should take it as **one derivation**:
(i) c03 amplitude sum at the refill → λ as a computed ratio, blocked only on DP-arc persistence;
(ii) two-GP coherent ejection → the singlet, hence the Fermi limit and V−A. The F5/CKM scoping
(TODO-4188) is the same vertex and should be read alongside. I will keep going in this window
until the founder ends it, but the detail handover will point here.

## 5. PD-008

Convenient branch: "it reduces to c03" — flagged at 4206, still true; c03's mechanism is a
conjecture, so this patch rests a model on an open problem. Attack: §1's identification of the two
senses with two c03 outcomes assumes both senses are *simultaneously present* as SSV contributions
at the core's GP; if the Sea supplies one DP with one sense at a time, there is nothing to add.
