# R2 — VSL μ↔ε Falsifier: Z₀ Geometric via the Harmonic Virial Mechanism

**Patch:** 2002 (21 June 2026) · **Window:** 2000-band · **Work item:** OPEN-COSMO-DM-2 residual R2
(the VSL μ↔ε-symmetry / Δc-LPI falsifier; the last clean-kill candidate for the EU-1 horizon mechanism)
**Status of result:** **R2 advanced from "reduced to is-Z₀-geometric" (0740) to a DERIVED conditional
PASS, with the mechanism identified and the load-bearing fork made explicit and falsifiable.**
**Verify:** `scripts/2002_z0_impedance_fork.py` (Reading A: A=0 exact; Reading B: A~O(1) fail)
**Discipline:** worker patch; owned greenfield path `series_relativity/development/mu_eps_closure/`;
no shared-registry / c06 / frontier edit here (proposed cross-refs in §6 for the integrator's batch).

---

## 1. What R2 is, and why it is the last clean-kill candidate

The EU-1 horizon resolution is **VSL**: early high `c_eff` solves causal contact, so no de Sitter phase
is needed (consistent with the Patch-0729 no-de-Sitter result). The genuine falsifier (Patch 0739): a
density-dependent `c_eff` could drag the fine-structure constant α with it, violating the tight
varying-constants bounds. In CPP the DP Sea is the EM medium, so `c = 1/√(μ₀ε₀)` (product) and
`α ∝ √(μ₀/ε₀) = Z₀` (impedance/ratio). Patch 0740 sharpened this **exactly**:

> `Δα/α = Δ ln Z₀`, and `A ≡ (d_μ−d_ε)/(d_μ+d_ε) = −dZ/dc`.

So the entire μ↔ε falsifier collapses to one question: **does the vacuum impedance Z₀ move under an SSV
perturbation?** `A=0` (Z₀ geometric) → c-variation is pure metric = gravity (c07) → α fixed → **PASS**;
`A~O(1)` (Z₀ ∝ stiffness C) → `k_α~1` → falsified by the atomic-clock LPI bound `|k_α|≲10⁻⁶` by **~6
orders → KILL**. This is the one place a clean kill of the VSL horizon mechanism — hence a reopening of
OPEN-COSMO-DM-2 — could still come from.

**What 0740 did and did not do.** 0740 correctly reduced the problem to "is Z₀ geometric?" and offered
three corpus *arguments* for yes (B is the curl of the polarization, not an independent susceptibility;
GPs are fixed/eternal; all four DP species couple equally). But it explicitly **did not prove it** — it
deferred to an owed c06 computation ("express μ₀, ε₀ in terms of stiffness C and broadcast speed c; check
whether Z₀ comes out C-independent"). That owed computation is R2. This patch does it.

## 2. The decidable computation (this patch)

Model the DP as a charged harmonic oscillator: stiffness `C` (the SSV-variable quantity, c02:
`C = α_geom·E_P/l_P³`), inertia `m`, charge `q`, density `n`, and ZBW frequency `ω_ZBW ~ 1/t_P` —
**fixed by the Absolute Moment, geometric, not a function of C** (c02). The electric response is the
**potential** (displacement) channel; the magnetic response is the **kinetic** (rotational/velocity)
channel. Whether these are *one* oscillation or *two* is the entire question, and it splits into a sharp
fork (`scripts/2002_z0_impedance_fork.py`):

**Reading A — single oscillator (the c06/0743 cartoon: "B is the rotation of the same DP whose radial
displacement is E").** Then ε₀ and μ₀ are the potential and kinetic faces of *one* response χ(C):
`ε₀ = g_E·χ`, `μ₀ = g_M·χ`, with `g_E, g_M` pure 600-cell geometric projection factors. The
**mechanism is the harmonic virial theorem**:

> `U_kinetic / U_potential = m·ω_ZBW² / C = 1` exactly (because `ω_ZBW² = C/m`).

The magnetic (kinetic) and electric (potential) energies are *equal and carry identical C-dependence*, so
**C cancels in the ratio** `Z₀ = √(μ₀/ε₀) = √(g_M/g_E)` (a pure lattice-geometric constant) **while it
survives in the product** `μ₀ε₀ = 1/c²` (so `c²` moves with C — the metric/gravity channel). Numerically,
across a 4× swing in C: **Z₀ flat to 0.00e+00 (A=0), c² moves by +2.1** → **PASS, α fixed.**

**Reading B — two independent oscillators (the magnetic response has its own inertia).** With `ω_ZBW`
fixed, `m = C/ω_ZBW² ∝ C`, so the magnetic inertia (inductance, μ₀) tracks C while ε₀ ∝ 1/C →
`Z₀ ∝ √(C/(1/C)) = C¹`. Numerically: **d ln Z₀ / d ln C = +1.00, A~O(1) → FAIL by ~6 orders.**

**The two readings give opposite verdicts.** This is the real content: Z₀-geometric is *not* automatic
from "μ and ε share a stiffness" (0740's phrasing) — it is a **virial consequence of the single-oscillator
structure**, and the alternative is a clean kill. The c06/0743 single-motion cartoon is therefore
**load-bearing**: it is literally the difference between PASS and a ~6-order falsification.

## 3. The mechanism, stated cleanly

The cancellation 0740 hoped for is now grounded in one line of physics. For a harmonic oscillator the
time-averaged kinetic and potential energies are equal (virial). In the DP Sea those two energies *are*
the magnetic and electric field energies of the propagating ZDC pattern. Their equality forces the
electric-to-magnetic energy ratio — hence the impedance Z₀ — to be set by the oscillator's geometry, not
its stiffness. An SSV perturbation rescales the stiffness (and with it `c`, the propagation reach: stiffer
→ faster, `c ∝ √C`, the right sign for the VSL early-universe high-`c_eff`), but it rescales the kinetic
and potential channels *identically*, so Z₀ — and therefore α — does not move. **This is why a
density/SSV-dependent `c_eff` is purely gravitational: it moves the product (c) but not the virial-locked
ratio (Z₀).**

## 4. Falsification-first verdict — and the residual that keeps it honest

- **R2 PASSES, conditional on the single-oscillator structure (Reading A = the c06/0743 cartoon).** The
  PASS is now *derived* (virial mechanism), not asserted (0740's three corpus facts). The VSL horizon
  mechanism survives the μ↔ε / Δc-LPI falsifier.
- **The PASS is conditional, and the condition is a real, decidable, currently-unproven structural claim.**
  Reading B (independent magnetic inertia) is a clean ~6-order kill. The c06/0743 single-motion picture is
  presently logged as a *physical cartoon, explicitly not in the corpus as a derivation*
  (`series_electroweak/development/b_field_as_rotating_dp_physical_cartoon.md`). So R2 is **not closed
  outright** — it is reduced to one formally-establishable EM-sector claim: *the DP magnetic response is
  the kinetic channel of the same oscillation that gives the electric response (one stiffness), with no
  independent magnetic inertia.* Establishing this (EW-1 Maxwell derivation / c06 magnetic-component
  derivation) closes R2 to an unconditional PASS; refuting it (independent inertia) is a kill.
- **Anharmonic residual (quantified).** The virial KE=PE is exact only at harmonic order; a cubic
  anharmonicity `ε_anh` shifts the ratio by `~ε_anh × (displacement strain)²`, giving `A ~ ε_anh × strain²`.
  For the **tight local clock-LPI bound**, the relevant strain is the local gravitational potential
  `~10⁻⁶`, so `A ~ 10⁻¹²·ε_anh ≪ 10⁻⁶` — comfortably safe for any reasonable anharmonicity. (The
  cosmological large-Δc regime faces only the weaker quasar/white-dwarf α-variation bounds and is governed
  by `Δα/α = A·(Δc/c) ≈ 0` at harmonic order.)

## 5. Consequence for OPEN-COSMO-DM-2

R2 was named (in the 2001 finding) as "the last thing standing between *substantially resolved* and
*closed*." It is no longer a clean *independent* kill: it is reduced to a single load-bearing structural
claim (the c06 single-oscillator picture) with a derived PASS via the virial mechanism and a bounded
anharmonic residual. OPEN-COSMO-DM-2's residual ledger updates to:
- **R2 → PASS-conditional** (was: open falsifier). Residual = formalize the single-oscillator structure
  (EM-sector) + the bounded anharmonic term. Clean-kill exposure removed; conditional remains.
- R3 (A_s adopted), R4 (OPEN-EU-1 depth) unchanged.

## 6. Proposed cross-refs — FOR THE INTEGRATOR'S BATCHED PATCH (not edited here)

Worker discipline: I do not touch shared registries or c06. Proposed for Thomas's batch:

> **`series_relativity/development/dp_sea_mu_eps_symmetry.md` (0740) — append a status line:** "Patch 2002
> derives the Z₀-geometric result via the harmonic virial mechanism (KE=PE ⇒ C cancels in the ratio,
> survives in the product) and makes the fork explicit: single-oscillator (c06/0743) ⇒ A=0 PASS;
> independent magnetic inertia ⇒ Z₀∝C, A~O(1) FAIL. Reduces the residual to formalizing the
> single-oscillator structure. See `mu_eps_closure/R2-Z0-VIRIAL-CLOSURE.md`."

> **`c06` future-work item (μ₀,ε₀ from C,c):** annotate that the cosmology payoff is now sharpened — the
> deliverable is specifically to establish whether the magnetic response is the kinetic channel of the
> same oscillator (PASS) or independent (FAIL); the virial mechanism (2002) is the test.

> **`frontier_sectors/CONJ.md` OPEN-COSMO-DM-2 residual ledger** (and/or the SR.md OPEN-SR Δc note):
> update R2 from "open VSL falsifier" to "PASS-conditional on the single-oscillator structure (Patch
> 2002, virial mechanism); residual = formal EM-sector derivation + bounded anharmonic A."

NO THEO (structural derivation conditional on the single-oscillator structure; no new axiom/term/counted
prediction — consistent with the no-THEO-for-conditional discipline and with how 0740 was scoped).
