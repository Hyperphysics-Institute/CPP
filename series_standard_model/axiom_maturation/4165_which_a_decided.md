# Which A Enters b — Decided, and the Asymmetry It Exposes

**Patch:** 4165. **Lane:** EW. **Session:** 234.
**Closes:** TODO-4154-WHICHA.
**Verify:** `series_standard_model/code/4165_which_a.py`.

---

## 1. Three readings, and the corpus does not say which

b = A·V_i. The A could be:

- **(i)** the CP's **own** axial attribute — A1′ as amended (4120): *"CPs carry the attribute"*;
- **(ii)** the GP's **A_i register** — the summed axial field from DI-bit arrivals, what the GP broadcasts;
- **(iii)** the A carried by an **individual arriving DI-bit** (AP-4 payload).

4154 argued (i) from what F3 needs. This patch decides it.

## 2. The decisive structural fact, from the founder's own cycle description

Patch 4152, verbatim: *"The GPs populate their register by computing/summing the DI-bits **arriving
from GPs** at a PSR distance."*

**The register is built from arrivals. A GP's resident CP does not send itself a DI-bit.** So the
resident CP's own A is **not in its own GP's register**. Under reading (ii), b would be built from
the axial field of the *neighbourhood*, with the particle's own spin absent from it.

## 3. What that costs — computed

Under (ii), A_register is a sum of N arriving axial contributions from a sea with no net
polarisation. Its magnitude grows as √N; its **direction is random**:

| N arrivals | \|Σ A\| / √N | correlation with the CP's own spin |
|---|---|---|
| 12 | 1.599 | 0.011 |
| 60 | 1.596 | 0.002 |
| 600 | 1.597 | 0.002 |
| 6000 | 1.597 | 0.003 |

**Zero correlation at every N.** So under (ii), for a free particle in an unpolarised sea, b carries
**no information about that particle's helicity** and ⟨b⟩ over the ensemble is 0.

**Reading (ii) does not weaken V−A. It abolishes it.** Reading (iii) is (ii) with N = 1 — the same
defect with worse statistics, and the N = 1 row Patch 4161 already showed is not the physical regime.

## 4. And (i) is what every standing result already assumed

4134 (the nucleon's ⟨b⟩ = 0 by the L = 0 s-wave average of the **cage's own** spins), 4135 (the
bracelet's 64 spin assignments), 4157 (THEO-CHIR-1: *"positions, charges **and spins**"* of the
configuration), 4158 (⟨b⟩ = (v/c)cos θ, where A is the **decaying particle's own** spin axis). If
(ii) were right, all four would need redoing and 4158's agreement with the measured polarisation law
would be a coincidence.

## 5. The verdict, and the asymmetry it exposes

> **A in b = A·V_i is the CP's own axial attribute — reading (i).**

Decided by §2 + §3, not merely argued: the register is built from arrivals, the resident CP does not
send itself a DI-bit, so under (ii) the particle's own spin is absent from its own bit.

**The structural point worth keeping:** b contracts a **CP-local attribute** with a **GP-held
register**. It is not a contraction of two register components, nor of two CP attributes. **The two
factors come from different objects in the cycle** — which is exactly why both are present at the CP
at the Moment of displacement (the GP stamps V_i on it; it carries its own A), and why the bit is
locally constructible at all.

## 6. What this leaves open, and it is not comfortable

**If b does not read the GP's A_i register, what does the register do?** It still exists — A3′
broadcasts it, AP-4 transports it. On the evidence of Patch 4155's coupling census it sources the
**A₁·A₂ spin–spin term, i.e. ordinary magnetism**, and nothing else identified.

**That is a thin job for a broadcast channel.** The amendment's case at 4120 was that A_i *completes*
A3′ over the full point group I_h — a structural argument, which stands. But its dynamical content,
now that b is known not to read it, reduces to reproducing magnetism the corpus already had. Worth
asking whether the channel earns its place. Filed as **TODO-4165-CHANNELJOB**.

## 7. PD-008 — the convenient branch, marked

Reading (i) is the convenient one: it is what four standing patches assumed, and adopting it costs
nothing. I have tried to decide it on the cycle's structure rather than on that convenience — §2 is
the argument, and it would have gone the other way had the register included its own resident CP.
§6 is the price of winning: ruling b out of the A_i register leaves that register with almost
nothing to do.

## 8. Status

TODO-4154-WHICHA **closed**. No verdict moved. χ₄ provisionally adopted. **F5 remains the blocker.**
