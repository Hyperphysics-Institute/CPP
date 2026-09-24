# The u–d Exchange: Zero if the Down Quark Keeps Its Seat, g_A 1.272 if Colour Antisymmetry Runs Over All Three

**Patch:** 4269. **Lane:** EW → strong (TODO-4234-DELTA item (ii)). **Session:** 239.
**Verify:** `series_standard_model/code/4269_ud_exchange_two_limits.py`.

## 1. Two founder statements, two limits

**(L1) Flavour pinned to seat.** Founder 4262: *"The down quark is bound to the plus qCP vertex"*; the ups sit on the
two minus vertices. The u–d-exchanged configuration would put a d on a minus vertex, and that configuration is not
in the state, so the u–d exchange vanishes. Only 4262's u–u exchange acts.

**(L2) Colour antisymmetry over all three seats.** The founder's SU(3) story
(`founders_voice/phenomenon_su3_colour_and_quark_switching.md`) says colour is which vertex a quark sits on, and
hops move quarks among *"three labelled vertices, fully connected"*, with *"a new seat means new forces"*. The colour
singlet is antisymmetric over all three seats. With the spin–flavour part symmetric and factored out (the SU(6) 56
that 4240's 5/3 rests on), the *space* part is a 3-orbital Slater determinant of the seat orbitals. Every quark then
sees the same one-body density, so R_u = R_d.

L2 is computed with two approximations: each seat's orbital does not depend on which quark occupies it, and the
shapes are Gaussian. With u–d overlaps of 0.72, these are coarser than L1's.

## 2. Rows verbatim (D-11)

```
overlaps, u-seats: [[1.0, 0.35], [0.35, 1.0]]
  (L1) flavour pinned: u-u exchange only       R_u=0.7782 R_d=0.8151  g_A=1.3093 ( +2.7%)  mu_p=2.675 ( -4.2%)  m_q(mu_p)=299.6  mu_n then -1.883 ( -1.6%)
overlaps, three seats (u1,u2,d): [[1.0, 0.35, 0.715], [0.35, 1.0, 0.715], [0.715, 0.715, 1.0]]
  (L2) full colour antisymmetry, 3 seats       R_u=0.7628 R_d=0.7628  g_A=1.2713 ( -0.3%)  mu_p=2.646 ( -5.3%)  m_q(mu_p)=296.3  mu_n then -1.862 ( -2.7%)

-> The u-d exchange is zero if the d never leaves the +qCP seat (L1, 1.310) and brings g_A to 1.272 (-0.3%) if
   colour antisymmetry runs over all three seats (L2).  Which holds is a physical question (4269 s4).
```

## 3. Result

- **L1: g_A = 1.310 (+2.7%).** With m_q fitted to μ_p, μ_n = −1.883 (−1.6%).
- **L2: g_A = 1.271 (−0.3%).** μ_n = −1.862 (−2.7%), because with R_u = R_d the ratio μ_n/μ_p is forced back to
  the naive −2/3.

L2 closes g_A and worsens μ_n, so it is not a free improvement. Which limit holds is a physical question about the
seats, not something the calculation can decide.

## 4. Founder question (a physical picture)

As the colour hops move quarks from vertex to vertex, **does the down quark ever take a turn on one of the minus
vertices, with an up quark on the plus qCP vertex, so that over time every quark sits in every seat? Or does each
vertex's charge keep the down quark on the plus qCP vertex always, so that the hops only ever trade the two ups
between the two minus vertices?**

- If every quark visits every seat (L2): g_A = 1.271.
- If the down keeps its seat (L1): g_A = 1.310.
- If the down visits the minus seats only part of the time, the answer lies between.

## 5. PD-008

L2 is the convenient branch, at −0.3%. It is not adopted ahead of the founder's picture, and its cruder
approximations and worse μ_n are recorded beside it.
