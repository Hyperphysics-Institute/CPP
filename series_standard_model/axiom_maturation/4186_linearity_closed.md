# The Shell-Sum Is Linear — and It Was Already Proved

**Patch:** 4186. **Lane:** GR/EW. **Session:** 234.
**Closes:** TODO-4185-LINEARITY. **Grounds:** Patch 4184's ε = a/r.

---

## 1. The answer, from GR-1j

**Lemma (Census linearity), GR-1j**, verbatim:

> *"Fixed per-GP emission + static-snapshot payload + reset-at-delivery ⇒ the per-Moment computed
> state at a GP is a **linear shell-sum** of origin-GP registers one hop away."*

**Lemma (The kernel):** *"One hop = one Moment = one PSR: the elementary operator is the **shell mean**
M_R(x)."*

**Theorem (Exact statics):** *"Static self-consistency u = M_R(x)[u] at every vacuum GP is, for ANY
PSR profile, **exactly flat-lattice Laplace**: ∇²_lattice u = 0 (the mean-value property holds at
every radius simultaneously; verified numerically at 10⁻⁹…)."*

> **The shell-sum is linear, it is the shell mean, and in statics the census is exactly Laplacian.**

## 2. The premises hold for the A channel

The lemma's three premises are all satisfied for A_i as A3′ and AP-4 state them:

| premise | satisfied by |
|---|---|
| fixed per-GP emission | A3′: *"all channels obeying the same icosahedral shell-sum"* |
| static-snapshot payload | AP-4c: *"imprint invariant in transit"* |
| reset-at-delivery | AP-4c: *"deposit once at the shell, reset at delivery"* |

So the linearity result carries to the axial channel, not merely to the scalar one it was proved
for.

## 3. What that grounds

**Exactly Laplacian statics ⇒ a 1/r Green's function for a point source.** That is precisely the
falloff Patch 4184 assumed when it wrote **ε = a/r** — the assumption I flagged as imported at 4185.
**It is now grounded in an existing theorem rather than asserted**, and the ratio stands:
ε = 1.6×10⁻⁵⁰ (nearest spin a fermi away) to 1.6×10⁻⁶⁵ (a metre), all below the 5.4×10⁻⁴⁷
observational cap.

## 4. A second lemma settles TODO-4183-SEASPIN outright

**Lemma (Homogeneous cancellation), GR-1j**, verbatim:

> *"The equal-influence invariant ⇒ the **uniform Sea** (including the uniformly distributed
> DP-Entity background) **cancels identically**; the dynamics closes on u."*

**A uniform Sea contributes nothing.** So the question of whether Sea DPs are spin-paired or
independent does not merely fail to close the 10⁵⁰ gap (4184) — **for a uniform Sea it contributes
zero either way.** TODO-4183-SEASPIN is **closed**, not merely mooted. What would matter is a
*non-uniform* Sea, which is a different question and not one the mixing ratio depends on.

## 5. D-10 working, for once in the right direction

**This is the fourth time this session that the corpus already held the answer.** The difference is
that this time **I searched before asserting**, which is what D-10 was enacted for at 4169. The
three earlier cases (4138, 4161, 4168) were found *after* a claim had shipped. **One data point is
not a trend, but it is the right data point.**

## 6. PD-008 — the convenient branch, marked

The convenient branch was to leave LINEARITY open. It was my own flag, nobody was chasing it, and
finding the answer merely confirms a number I had already reported — no new result, just an
assumption retired. **That is exactly the kind of item that goes stale**, and the session has spent
a great deal of effort on assumptions that were flagged and never checked (D-4's second cost record,
4167→4168). §4 was the unexpected return.

## 7. Status

TODO-4185-LINEARITY **closed**. TODO-4183-SEASPIN **closed**. Patch 4184's ε = a/r **grounded**. No
verdict moved. **F5 remains the blocker.**
