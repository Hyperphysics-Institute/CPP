# Does the A_i Channel Break Its Own Protection? — TODO-4134-SPINORIENT

**Patch:** 4136. **Lane:** EW/SS. **Session:** 234.
**Answers:** TODO-4134-SPINORIENT (partially — the split is the result).
**Verify:** `series_standard_model/code/4136_spinorient.py`.

---

## 1. The question, and why it was the one to take

4134 derived B_tot = **n·W** and found F3 holds because an L = 0 ground state's internal frame
is isotropically distributed relative to its spin axis: ⟨n·W⟩ = 0. **R-F3-ISO** names the
requirement — no frame–spin correlation above ~10⁻⁷. 4135 then found R-F3-ISO carries *both*
sectors: satisfied by a nucleon ground state (P-even), violated by construction in a bracelet
scattering event (P-odd). So if the amendment's own A_i channel generates that correlation, it is
not a correction to F3 — it is F3's failure mode, and it takes the weak sector's mechanism with
it. That is why this outranked the cage-moment refinement.

## 2. What a correlation actually requires

⟨n·W⟩ ≠ 0 is **polar order**: the distribution over cage orientations must distinguish **+n from
−n**. That needs an energy term **odd** under n → −n, i.e. (axial)·(polar). Four routes exist in
the broadcast content, and the A3G-2 table (4125) already classifies three of them.

**E1 — a linear axial·polar term is not protected, and is bounded instead.** With E = −g (n·Ŵ),
the correlation is the Langevin function: ε = L(g) → g/3. Exactly proportional to the coupling;
nothing cancels. Inverting through B_tot = ε|W| with |W| = 1.1654 (the SU(6) proton, 4134) and
the ~10⁻⁷ hadronic PV bound gives **ε ≤ 8.6×10⁻⁸ and g ≤ 2.6×10⁻⁷** in units of the confining
scale. A coupling of ordinary strength is excluded by seven orders — so these routes have to be
closed structurally, not by smallness.

**E2 — and here is the positive result. The quadratic loophole does *not* open this one.**
TODO-4124-QUADRATIC records that a response quadratic in b is T-even × T-even and is excluded by
neither A3G-2's nor A3G-3's argument. Applied here: with E = −c (n·Ŵ)², the alignment does
respond — ⟨cos²θ⟩ moves from 1/3 to 0.89 at c = 10 — but **⟨cos θ⟩ stays exactly zero at every
strength**, analytically, because exp(c u²) is even in u. The quadratic term makes *nematic*
order, not *polar* order, and a pseudoscalar needs polar order.

So the loophole that reopens A3G-2 and A3G-3 does **not** reopen R-F3-ISO. This protection is
strictly better than theirs in exactly the respect the 4125 caveat names — and it is independent
of F6 and B3, resting only on the parity of the exponent.

## 3. The census, and the one route that stays open

| route | P | T | status |
|---|---|---|---|
| A·r̂ (monopole–dipole) | −1 | −1 | **closed** by F6 (b is T-even) + B3 (linear) |
| A·v (spin–velocity) | −1 | −1 | **closed**, same fact |
| (A·V)² (quadratic in b) | +1 | +1 | **closed** by E2, independently of F6/B3 |
| **A·V (= b itself)** | **−1** | **+1** | **NOT closed, and not closeable this way** |

The fourth route cannot be closed by T-parity **because b is T-even by F6 — which is precisely
why it is available as a carrier at all.** An A·V term in the nucleon's internal energy is a
P-odd term in the strong Hamiltonian, and that *is* hadronic parity violation, the thing bounded
at 10⁻⁷. Excluding it by assumption would be circular, and I will not write it down as a closure.

The right reading: for that route R-F3-ISO is **not an independent protection — it is F3
restated.** F3 is therefore *self-consistent* here rather than newly threatened. That is a weaker
and less satisfying answer than "the amendment cannot break it," and it is the true one.

## 4. The cost, stated plainly

The two T-parity closures use the **same F6 + B3 premise** that already carries A3G-2 and A3G-3.
The premise concentration the 4125 caveat flagged, and that the 4128 audit narrowed, now carries
a **third** result. If F6 fails, A3G-2, A3G-3, and two of R-F3-ISO's four routes reopen
*together*.

This is the honest headline of the patch, and it cuts against the work: I set out to test whether
the amendment undermines F3, and the answer is "not by three of four routes" — but two of those
three lean on a premise that was already carrying more than its share. **The suite is less
independent after this patch than it looked before it**, even though nothing fired.

## 5. PD-008 — the convenient branch, marked

The convenient result was a clean closure: the amendment provably cannot generate the forbidden
correlation, F3 secured, nothing owed. I have three of four routes and one that reduces to the
question itself, plus worsened premise concentration. The convenient branch was to call the
A·V route "excluded because b is the bit, not an energy" — the corpus's own A3G-2 table says
exactly that (*"this is the local bit, not a force between masses"*), and I could have cited it.
I did not, because the bit is read by *something*, and whatever reads it contributes to the
energy; the table's parenthesis is a scoping remark about two-body potentials, not a proof that
b is absent from the internal Hamiltonian. The next window should check whether I was right to
refuse that citation.

## 6. Status

F3 unchanged and self-consistent. **TODO-4134-SPINORIENT answered for three of four routes;
the A·V route is filed as TODO-4136-BINENERGY** — does the thing that reads b contribute to a
structure's internal energy, and if so at what order? That question is upstream of F3, A3G-2 and
A3G-3 alike. No verdict moved. χ₄ provisionally adopted. **F5 remains the blocker.**
