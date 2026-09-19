# TEST-A3G-3 — EM Parity. PASSES, and the protection is structural.

**Patch:** 4124. **Lane:** EW. **Second falsifier run** of the three authorized at 4115.
**Discharges:** TODO-4123-A3G3. **Corrects:** my own bound at 4123.
**Verify:** `series_standard_model/code/4124_a3g3_em_parity.py`.

---

## 1. First, a correction to 4123

At 4123 I modelled the field-induced spin tilt as a **fixed direction** and derived
δ_field < ~10⁻¹⁰ rad. That model is not the physical response. A field acts on a spin by
**torque**, and δA ~ A × B is **perpendicular to A** — hence A-dependent, not a fixed direction.

Re-running with the physical forms:

| tilt model | net R/N at δ = 0.05 | |
|---|---|---|
| fixed direction (my 4123 model) | +0.05 | survives — but unphysical |
| **magnetic torque, δA ~ A × B** | **0.00000** | **cancels exactly** |
| EDM alignment, δA ~ A × (A × B) | +0.049 | survives |

**Ordinary magnetism does not threaten F2 at all.** The torque tilts A perpendicular to itself,
so its effect on A·V is odd in A and sums to zero over the isotropic spin distribution —
0.00000 at every δ tested, from 0.002 to 0.2.

## 2. What survives is an EDM — and EDMs are severely bounded

The one channel that survives is the term that **aligns** the spin along the field,
~ d(A·Ê). A P-odd alignment of a spin along a field direction is precisely an **electric
dipole moment**. The relevant limit is among the tightest in physics:

> |d_e| < 4.1 × 10⁻³⁰ e·cm (ACME/JILA)

So the real bound on the amendment was never the 10⁻¹⁰ rad I wrote — it is twenty orders
tighter.

## 3. But χ₄'s own structure forbids that channel

| | P | T |
|---|---|---|
| A (axial spin) | +1 | −1 |
| V (polar displacement) | −1 | −1 |
| **b = A·V** | **−1** | **+1** |
| A·Ê (the EDM term) | −1 | **−1** |

An EDM coupling is P-odd **and T-odd** — that is the textbook reason EDM searches are
T-violation searches. χ₄'s response is **linear in b** (B3, Patch 4076), and **b is T-EVEN**
(F6, Patch 4085). A linear response built from a T-even quantity cannot produce a T-odd term.

> **Required by the surviving channel: T = −1. Supplied by χ₄'s bit: T = +1. Mismatch — the
> coupling is forbidden at linear order.**

**A3G-3 PASSES.** Both channels that could have violated EM parity are closed: the magnetic
one geometrically, the EDM one by T-parity.

## 4. Why this counts for something

The protection is **not a tuning and not a calibration**. F6 was derived from CPT at Patch
4085, weeks before this test existed and for entirely unrelated reasons, and it is F6 that
closes the channel. The axiom is protected by structure it already had.

It is also worth noting that b's P-odd/T-even signature was **independently reproduced** by
the A·V construction at Patch 4111. The same signature now does load-bearing work here. That
is two separate uses of one derived fact, which is the kind of thing a real structure does and
an ad-hoc one does not.

## 5. Honest caveat

**This is a linear-order argument.** A response *quadratic* in b would be T-even × T-even =
T-even, and is not excluded by this reasoning. B3 established the response is linear, so the
argument holds exactly where B3 does; a higher-order term would need separate treatment. Filed
as **TODO-4124-QUADRATIC**.

## 6. Status

- **A3G-1** (vacuum magnetisation): does not fire (4121, refined 4122/4123)
- **A3G-3** (EM parity): **PASSES structurally** — this patch
- **A3G-2** (spin-dependent fifth force): still unrun, now the last live falsifier

No verdict moved. χ₄ remains provisionally adopted; **F5 remains the blocker.**
