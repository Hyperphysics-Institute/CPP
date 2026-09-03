# The Kerr test, indicative: at χ = 0.68 the free-surface lines are 193 Hz and 291 Hz — within 1% of GR-2's shipped 191 and 288.5 — and nearly spin-insensitive. The coincidence survives spin. Under an ansatz, stated.

**Patch 3392, Session 161, 3 Sep 2026.** Verify `code/3392_kerr_indicative_free_surface_verify.py` (7/7; 3359 SN machinery reused, X and dX/dr* returned). Reasoning `reasoning/3392.md`. Founder instruction: "let's run [the Kerr test] before we write the result into the paper."

**Standing:** INDICATIVE. Two ansätze are used and named. The controlled Kerr recompute (OPEN-GR-KERRWALL-1, reconstruction) remains open.

## §1 What was done

1. **Self-check at a = 0.** The free-surface even law (3391) is mapped to the odd sector by the *exact* a = 0 Chandrasekhar transformation (3377): `β⁻ = [β⁺W − W′ − 12(V⁻ − ω²)]/(W − 12β⁺)`. Imposed on the RW/SN function at a = 0 it reproduces 3391's even poles to 10⁻⁵ (ℓ = 2: 0.37487 − 0.00190i; ℓ = 3: 0.55964 − 0.00008i). Transformation and solver are consistent.
2. **Ansatz A — the Kerr surface.** 3320's saturation criterion `F_n = s² + v² = 1` (which places the a = 0 surface at 9M/4, lapse 1/3) is rescaled to the ratified lapse ½: `F_n = 4/9`. At a = 0 this gives 8M/3 by construction; at χ = 0.68 (equatorial) it gives `r_w = 2.734 M` (old: 2.267 M).
3. **Ansatz B — the Kerr wall law.** The a = 0 Robin law `β⁻(ω)` (free-surface coefficients b₀, b₂ at v = 2/3, mapped) is imposed on the Sasaki–Nakamura function at the Kerr surface. This is the "Kerr–Zerilli route" CONV-039 rated literature-heavy; here it is used as an *indicator*, not a derivation.

## §2 Results (χ = 0.68, 62 M_⊙)

| line | shipped (V1.6: X = 0 at 2.267 M) | X = 0 at the new surface 2.734 M | **free-surface law at 2.734 M (ansatz)** | a = 0 free-surface (3391) |
|---|---|---|---|---|
| (2,−2) | 0.36694 − 0.0878i → **191.3 Hz**, Q 2.1 | 0.3497 − 0.148i → 182 Hz | **0.37052 − 0.00540i → 193.1 Hz, Q 34** | 195 Hz |
| (3,−3) | 0.55333 − 0.0652i → **288 Hz**, Q 4.2 | — | **0.55920 − 0.00038i → 291 Hz, Q 736** | 292 Hz |

Two readings: (i) **the free-surface lines are nearly spin-insensitive** — a = 0 → χ = 0.68 moves (2,−2) by 1.2% (the X = 0 line moved 18%); (ii) **they land within 1% of the numbers GR-2 shipped in August from an assumed wall at a different radius.** The surface move alone (X = 0 at 2.734 M) would have lowered the line to 182 Hz; the derived law brings it back to 193.

## §3 What this is and is not

It is the test the founder asked for, at the level the corpus can currently run: the a = 0 coincidence (3391 §4) is **not killed by spin**, and both lines survive it. It is **not** the controlled Kerr recompute: Ansatz A rescales a criterion derived under the old floor; Ansatz B carries an a = 0 boundary law into Kerr through a transformation that is exact only at a = 0. Either could be wrong at the several-percent level at χ = 0.68 — and the agreement is at the one-percent level, which is the reason to state both plainly rather than quietly.

The physical picture that would make the spin-insensitivity natural: the free-surface mode is a **trapped cavity mode** whose frequency is set by the wall's Neumann crossing sitting at the barrier top (3383 regularity), and both the crossing and the barrier top move together with spin. That is a conjecture, recorded as such (OPEN-GR-CROSSING-1).

## §4 Recommendation to the founder (his call)
The a = 0 derived set (even 195/292, odd 208) is solid and can be written. The Kerr numbers can be written **only** as "indicative, ansätze A and B, controlled recompute open" — and if written, the paper's V1.6 numbers (191, 288.5) acquire a status they never had: reproduced within 1% by a derived chain. The worker's read under the economy protocol: this is now a **win candidate** (trigger 1) — a derived chain reproducing the flagship at both spins — and the right next move is a panel round scoped as a *win-check* (the free-surface law; the two ansätze; the coincidence), not another unilateral patch. Dispatch is the founder's.
