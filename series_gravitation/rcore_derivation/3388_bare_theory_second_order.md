# Mercury from the bare theory: no special rule — the census self-enhances through the HOP LENGTH already in AP-4 + the PSR law; the second-order coefficient is a computation, and Mercury says it must be ½

**Patch 3388, Session 161, 2 Sep 2026.** Founder constraint C-NO-SPECIAL-RULE. Supersedes 3387 §3's phrasing ("heavier messages") — that mechanism is withdrawn as an AP-4 change. Reasoning `reasoning/3388.md`.

## §1 The founder's objection, sustained

"Heavier registers broadcast heavier messages" is a change to AP-4: the DI-bit payload is a **static snapshot** of the origin GP's registers, imprinted once, invariant in transit, and the receiver's SSV_abs is **count-like** (more DI-bits ⇒ larger register). T-1 (C-i) records the consequence: the per-Moment census is a *linear* functional of the origin registers one hop away. There is no payload weighting in the bare theory and none is added. Withdrawn.

## §2 What the bare theory already contains at second order

Two registered facts:
1. A DI-bit advances **one PSR per Moment** (AP-4c; P-SALTATORY-HOPS).
2. `PSR_eff = l_P/(1 + u)` — the hop is **shorter where the register is larger**.

Consequence, with nothing added: a conserved DI-bit flux crossing a region of small PSR is deposited more densely there — more hops per unit distance, one deposit per hop. The register is a per-Moment deposit count. So the census **self-enhances through its own propagation**: schematically `u = v·(1 + u)^p`, where `v = μ/r̄` is the bare (CP-sourced, 1/r-kernel) census and `p` is the exponent with which the deposit density scales with the inverse hop length. This is "gravity gravitates" *by the mechanism the theory already has* — the field slows and shortens its own messengers — not by a rule.

## §3 What the exponent decides (symbolic)

`u = v + p·v² + …`; with the founder's clock mechanism `N = 1/(1 + u)`:

| p (deposit-density exponent) | register | PPN β | perihelion vs GR | Mercury |
|---|---|---|---|---|
| 0 (no enhancement — the corpus's linear register) | `v` | 3/2 | 5/6 | 35.8″ — **fails** |
| **½** | `v + v²/2 + …` = `v/(1 − v/2)` | **1** | **1** | **43.0″ — passes**; `N` = the ratified log-lapse exactly |
| 1 (naive: deposits ∝ 1/PSR) | `v + v² + …` | 1/2 | 7/6 | 50.1″ — **fails** |

**β = 3/2 − p.** Mercury requires `p = ½` — and `p = ½` is exactly the value at which the founder's clock mechanism reproduces the ratified log-lapse. So the bare theory *can* compute Mercury, and the question "is it the bare theory?" becomes a single number the relay recursion must return.

## §4 Why ½ is not arbitrary — the shape of the computation

The naive count (deposits per GP per Moment ∝ 1/PSR) gives `p = 1`. But the register is not the deposit count alone: it is the count *summed over the PSR shell* the receiving GP perceives, and that shell's volume also shrinks with the PSR (∝ PSR³ in GP number at fixed lattice; ∝ PSR in the radial direction relevant to a 1/r relay). A deposit density ∝ 1/PSR integrated over a perception depth ∝ PSR^{1/2}… — the honest statement is that **`p` is the relay recursion's second-order coefficient and must be computed from T-1's kernel with the PSR-dependent hop**, not read off a dimensional argument. That computation is the deliverable: **OPEN-GR-CENSUS-P**. If it returns ½: Mercury is derived from the bare theory, the log-lapse is derived, the clock mechanism is confirmed, and the R-core surface moves to `N = ½` (1.33 r_S, 3387 §4) — all from AP-4 + PSR law + the founder's clock. If it returns anything else: the bare theory fails Mercury at second order, and *that* is the finding.

## §5 The near/far-side idea

The relativistic perihelion advance is a test-particle effect: it comes from the second-order term in `g_tt` (β) and the first-order term in `g_ij` (γ) along Mercury's *centre-of-mass* orbit. Mercury's finite size and the differential (tidal) field across it contribute of order `(R_Mercury/a)² ~ 10⁻⁹` of the orbit — negligible — and the Sun's quadrupole `J₂` gives ~0.03″/century, already accounted for in the 42.98″. So a near/far-side effect *on Mercury* cannot supply the missing 7″. But the founder's instinct that "something differential is being missed" is right in a different place: the *census's* propagation is differential across the orbit — the hop length varies with `v`, and that is the `p` term. The differential effect is in the messengers, not the planet.

## §6 What stands after this patch
- 3387 (A) local `c` by local clocks: stands. (B) the linear register fails Mercury: stands. (C) the *form* `v/(1 − v/2)`: stands as the required result; its *mechanism* is re-attributed from payload (withdrawn) to hop-length self-enhancement (bare theory). (D) the surface at 1.33 r_S etc.: conditional on `p = ½`.
- **Owed:** OPEN-GR-CENSUS-P — the second-order coefficient of the T-1 relay recursion with PSR-dependent hop. The single number on which "Mercury from the bare theory" now rests.
