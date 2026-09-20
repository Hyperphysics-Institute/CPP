# How Many GPs Are in the PSR Shell? Exactly Twelve — and Why

**Patch:** 4167. **Lane:** EW/GR. **Session:** 234.
**Answers the founder's question (20 Sep) on the PSR-shell population.**
**Verify:** `series_standard_model/code/4167_psr_shell_count.py`.

---

## 1. The question

> *"This statement implies that only the 12 closest neighbors contribute DI-Bits to a GP_origin. Of
> course, the number is much more than 12 because every GP at a PSR radius (in a 10% band) will
> contribute. So the number will likely be vastly greater than 12 neighbors."*

**The reasoning is right; the premise it needs is not available.** It would hold whenever PSR ≫ l_P.
But `master_glossary`, verbatim:

> **Planck Sphere Radius (PSR):** *the effective displacement a CP can achieve per Absolute Moment.
> **In the rest frame, PSR = l_P** (Planck length). When SSV_abs increases … the Voronoi cell volume
> **shrinks**…*

**PSR is one lattice spacing, and it shrinks — never grows.** So the shell sits at the
nearest-neighbour distance, and the question becomes geometric: how many 600-cell vertices lie
within ±10% of it?

## 2. Computed on the actual 600-cell

The 600-cell built from the 120 unit quaternions of the binary icosahedral group 2I. Shell structure
from any vertex:

| chord distance | count | ratio to nearest |
|---|---|---|
| **0.618034** | **12** | **1.000000** |
| 1.000000 | 20 | **1.618034** |
| 1.175571 | 12 | 1.902114 |
| 1.414214 | 30 | 2.288246 |
| … | | |

**The next shell out is a factor φ = 1.618034 away** — the golden ratio, exactly, as the 600-cell's
own geometry requires. A ±10% band spans [0.556, 0.680]; the second shell is at 1.000.

> **GPs in the PSR band: 12.** Not an approximation, not a nearest-neighbour truncation — **it is
> exactly what a 10% band around PSR = l_P contains.** The band would have to widen to **±24%**
> before a single second-shell vertex entered.

That the gap is φ is worth noting on its own: the 600-cell gives the widest possible margin for a
nearest-neighbour-only rule, and the corpus's 10% band sits comfortably inside it rather than at
its edge.

## 3. When the founder's reading would be right

It holds whenever PSR ≫ l_P, since then N ≈ 4πR²(0.1R) ≈ 1.26(R/l_P)³:

| PSR | N |
|---|---|
| 1 l_P | ~1 |
| 10 l_P | ~1.3×10³ |
| 10³ l_P | ~1.3×10⁹ |
| 10⁶ l_P | ~1.3×10¹⁸ |

**So this is not a geometric question but a physical one: can the PSR ever much exceed l_P?** On the
glossary's reading it cannot — it equals l_P at rest and shrinks under SSV_abs. If that is wrong,
or if there is a regime the glossary does not cover, the count changes by many orders and several
results scale with it.

## 4. Consequence for Patch 4166 — and it cuts both ways

4166 used N = 12 and got corr(register, own spin) = 0.154, i.e. V−A at ~15% of maximal if b read the
register. **That stands.**

**And had the objection held, it would have strengthened the result it was aimed at.** The dilution
goes as 1/√N, so a vastly larger shell makes the register's correlation with the particle's own spin
vastly *smaller* — V−A at 0.003% rather than 15% — and the conclusion that **b reads the CP's own A**
becomes more forced, not less.

**Either way the verdict is unchanged. Only the number moves, and only if PSR can exceed l_P.**

## 5. PD-008 — the convenient branch, marked

The convenient branch was available and is worth naming: I could have accepted the correction. It
came from the founder, it was confidently put, and §4 shows it would have *helped* my conclusion — a
rare case where conceding costs nothing and gains goodwill. I checked it instead, and it does not
hold on the glossary's definition of PSR. **The one thing I have not checked is whether that
definition is complete** — §3 is written so that if PSR can exceed l_P somewhere in the corpus I
have not read, the founder is right and the numbers are recomputable from the table.

## 6. Status

No verdict moved. χ₄ provisionally adopted. **F5 remains the blocker.**
