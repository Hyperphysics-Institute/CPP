# CORRECTION to Patch 4109 — LSP′ Cannot Carry b, and the Axiom Amendment IS Required

**Patch:** 4110. **Lane:** EW. **Corrects:** Patch 4109 (mine, shipped one turn ago).
**Verify:** `series_standard_model/code/4110_lsp_pseudoscalar_refutation.py`.
**Result: 4109's headline is INVERTED. The founder's instinct was right.**

---

## 1. What 4109 claimed, and the error

4109 claimed the helicity bit needs no new broadcast channel because LSP′ = (Φ, V_i, Q_ij)
already contains the pseudoscalar det[V, QV, Q²V]. Its check C4 reported that quantity nonzero
"in 5000/5000 anisotropic draws," concluding it was "available exactly where the weak sector
needs it."

**That check used random symmetric matrices — which are generically triaxial. It never tested
a single actual CPP structure.** An unrepresentative test population, and the conclusion does
not survive contact with the real ones.

## 2. The determinant's actual condition

In Q's eigenbasis, with eigenvalues (a,b,c) and V = (x,y,z):

> det[V, QV, Q²V] = x·y·z · (b−a)(c−a)(c−b)

It is a **Vandermonde**. It vanishes whenever **any two eigenvalues coincide** — i.e. on any
spherically or **axially** symmetric configuration. It needs Q fully **triaxial**.

## 3. Every named CPP structure kills it

| structure | Q eigenvalues | distinct | max \|b\| |
|---|---|---|---|
| isotropic sea | (0,0,0) | 1 | 0 |
| icosahedral 12-shell (Z cage) | (0,0,0) | 1 | 0 |
| dodecahedral 20-shell (H cage) | (0,0,0) | 1 | ~1e−80 |
| tetrahedral 4-shell | (0,0,0) | 1 | 0 |
| octahedral 6-shell | (0,0,0) | 1 | 0 |
| **W bracelet (D6 ring)** | (−1, ½, ½) | **2** | **~1e−14** |

The W bracelet is the fatal row. **V−A parity violation is maximal there**, and the candidate
gives exactly zero. Icosahedral symmetry has no invariant l=2 tensor at all, so the cages give
Q ≡ 0; D6 forces two equal eigenvalues. Nothing in CPP is triaxial.

## 4. And the pseudoscalar is unique, which makes this general

A pseudoscalar needs exactly one ε tensor. Contracting ε against the available slots:
ε_ijk V_i Q_jk ≡ 0 and ε_ijk Q_ia Q_ja ≡ 0 (antisymmetric ε against symmetric slots, verified
to machine zero). The only surviving form is det of three vectors, and by **Cayley–Hamilton**
the only vectors buildable are V, QV, Q²V (verified: Q³ reduces, residual 4.5×10⁻¹⁶).

> **det[V, QV, Q²V] is the UNIQUE pseudoscalar of LSP′, up to a P-even factor.**

So this is not a failure of one candidate. **No pseudoscalar built from A3′'s ratified content
is nonzero on any CPP structure.**

## 5. The conclusion, which is firmer than 4109's was

> **A3′ DOES need amending to carry χ₄'s helicity bit.**

The founder wrote: *"The CP carrying the 4D element/Helicity bit is a new concept that has
never been used."* He was right, and he was right for a reason stronger than intuition — it is
forced. 4109's claim to the contrary is **withdrawn in full**.

This raises χ₄'s cost back up, and prices it honestly for the first time: **the axiom requires
a new irrep channel in a ratified axiom (A3′), not merely a new interpretation of existing
content.**

## 6. What goes with it

- 4109's "F2 by a second route" is **withdrawn**. F2 reverts to holding under **DP-CAL-1**
  (Patch 4107, the founder's calibration).
- The F3-by-cage-symmetry result I was pursuing when this surfaced is **also withdrawn** — it
  rested on the same refuted carrier. F3 reverts to R-F3 (Patches 4101/4108), still open.
- **TODO-4109-4071 is effectively answered, affirmatively for 4071.** Patch 4071 found a CP
  needs ≥4 independent internal directions to carry a pseudoscalar. This patch reaches the
  same wall from the LSP′ side: (V, Q) cannot do it on any symmetric structure. The two
  results agree, and 4071's conclusion — *"internal structure IS an axiom rather than an
  alternative to one"* — is **corroborated, not threatened**.

## 7. Method note

This is the second time in this session that a claim of mine failed on the test population
rather than the mathematics (the first: the invented "generation-transition structure" at
4096, caught at 4102). The pattern is specific and worth naming: **a check run on generic
random inputs is not a check on the corpus's actual objects.** CPP's structures are highly
symmetric by construction, and symmetry is exactly what kills invariants — so random-matrix
tests will systematically over-report availability.

No verdict moved. F5 remains χ₄'s blocker; χ₄'s cost is now higher than 4109 recorded.
