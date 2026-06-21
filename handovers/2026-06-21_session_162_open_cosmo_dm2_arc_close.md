# Session 162 — OPEN-COSMO-DM-2 Arc Close (Patches 2001–2005, 2000-band window)

**Date:** 2026-06-21 · **Window:** 2000-band (Opus worker; Thomas integrator) · **Work item:** OPEN-COSMO-DM-2
**One-line:** The programme's stated #1 falsification risk (OPEN-COSMO-DM-2, "CPP does not reproduce P(k)")
is **substantially resolved** — the registry verdict was stale; the EU-1 arc had already supplied the
seeds. Four residuals stress-tested; none is a live framework threat. Registry reconciled.

---

## What this arc did (in consequence order)

The "SERIOUS TENSION" verdict (Patch 0725) predated the EU-1 arc (0738–0785). OPEN-COSMO-DM-2 splits into
Q1 (growth→P(k), *always inherited* given seeds) and Q2 (seed origin, *the only barrier*). At 0725 the
sole seed candidate was the causal swirl mechanism (fails the cosmic-string wall). EU-1 then resolved Q2
by a different route — **VSL horizon** (high early c_eff; not de Sitter, so 0729 is not contradicted) +
**ZBW-stack δN spectrum** → n_s=0.9649 (PRED-C-96, shipped EU-1 v1.0). The registry never absorbed this.

**Residual ledger (post-arc):**
- **R1 — explicit P(k): DONE (2001).** `pk_closure/scripts/2001_pk_from_eu1.py` feeds EU-1's *own*
  spectrum (n_s=0.9649, α_s=−0.0006, A_s=2.1e-9) through EH98 transfer + CPT growth. 5/5 gates: turnover
  k_eq≈0.021 h/Mpc, low-k slope ≈n_s, high-k steepening to n_s−4, red tilt visible vs HZ, σ₈ O(1).
  Amplitude honest: A_s adopted = Planck value, so precise σ₈=0.811 is by-construction (CAMB).
- **R2 — VSL μ↔ε falsifier: PASS-conditional (2002).** The whole falsifier reduces to "is Z₀=√(μ₀/ε₀)
  geometric?" (0740: Δα/α=Δln Z₀). 2002 derives it via the **harmonic virial mechanism**: single-oscillator
  (c06/0743) ⇒ ⟨KE⟩=⟨PE⟩ ⇒ C cancels in Z₀ (A=0, PASS) but survives in μ₀ε₀=1/c² (c varies=gravity).
  Independent magnetic inertia ⇒ Z₀∝C, A~O(1), FAIL by ~6 orders. **Clean-kill exposure removed; the
  load-bearing residual is the single-oscillator structure (currently a physical cartoon, not a corpus
  derivation).** This is the next hardening target.
- **R3 — A_s: adopted; characterized (2003) + derive-κ attempted (2004).** Poisson/shot-noise normalization
  EXCLUDED (~67 orders + white shape) → curvature is the collective H_eff mode. A_s ∝ (κ·kT)²; n_s is
  κ-invariant (log-derivative) which is *why* A_s is undetermined (κ-orthogonality). Deriving A_s ≡ deriving
  the boost coupling κ — which is the magnitude of the H-engine boost law, carried as a **posited** axiom
  constant ("constant by axiom, NOT derived", brick4). Smallness localized to κ (kT~E_Pl pinned; f_sup~1).
  Target κ~2×10⁻⁷; α³ flagged as a non-evidence where-to-look hint only. **A_s stays adopted; parity with
  inflation; not a tension.**
- **R4 — OPEN-EU-1 derivation depth: unchanged.** A1–A11 homogeneity + ZRP; shared with standard cosmology.
  Deriving the H-axiom constant (R3's κ) is naturally part of this layer.
- **Owed (low priority, surfaced 2003):** EU-1 tensor ratio r — spectator mechanism decouples r from ε, so
  `r=16ε` does *not* apply; r is an undetermined separate CPP quantity, NOT a clean tension.

## Patches in this arc
- **2001** R1 P(k) closure — `pk_closure/` (+ finding/reasoning).
- **2002** R2 Z₀ virial — `mu_eps_closure/` (+ finding/reasoning).
- **2003** R3 A_s κ-orthogonality — `as_amplitude_closure/` (+ finding/reasoning).
- **2004** R3 derive-κ (honest negative) — `as_amplitude_closure/kappa/` (+ finding/reasoning).
- **2005** REMEDIATION — restored the 8 finding/reasoning docs that 2001–2004 omitted (a tool path error
  had committed only the verify scripts). Repo now whole; reasoning-capture rider satisfied retroactively.
- **2006** (this consolidation) — CONJ.md reconciliation + 0740 update + this handover.

## Registry edits MADE in 2006 (this consolidation patch)
- `frontier_sectors/CONJ.md`: OPEN-COSMO-DM-2 status OPEN → **SUBSTANTIALLY RESOLVED** (superseding header,
  history preserved); CONJ-COSMO-1 status "structure-formation CONDITIONAL FALSE" → **conditional-PASS
  RESTORED** (the 0729 kill applied only to the swirl route; EU-1 supplies the seeds). History preserved.
- `series_relativity/development/dp_sea_mu_eps_symmetry.md` (0740): appended the 2002 Z₀-virial update.

## Registry edits STILL PROPOSED (for the integrator's discretion — NOT made here, higher-traffic files)
- `predictions.md` PRED-C-96 / `frontier_sectors` OPEN-EU-1: note that A_s is adopted because it carries
  the boost-coupling prefactor (κ·kT)² that n_s's log-derivative cancels (κ-orthogonality, 2003/2004);
  shot-noise excluded; deriving A_s ≡ deriving the posited H-axiom constant κ. Optionally register the
  low-priority owed EU-1 tensor-r item.
- `c06` future-work (μ₀,ε₀ from C,c): annotate that the deliverable is now specifically "is the DP magnetic
  response the kinetic channel of one oscillator (PASS) or independent (FAIL)?" with the 2002 virial
  mechanism as the test.
- SR.md frontier (if it carries the Δc/μ↔ε line): update R2 from "open falsifier" to "PASS-conditional
  (2002)".

## Next: harden R2 (Thomas-directed)
R2 is the remaining *conditional* kill, so it outranks R3/A_s by consequence. The single-oscillator
structure (c06/0743) is the load-bearing claim. Two routes: (a) dispatch the now-crisp fork to the review
panel via CONV-001 single-block ("is the DP magnetic response the kinetic channel of one oscillator, or
independent? — PASS/FAIL"); (b) attempt the formal EM-sector (EW-1/c06) derivation directly. Recommended:
panel-dispatch first (the question is decidable and sharp), then formalize whichever way it lands.

## Discipline notes for the next window
- Owned paths this arc: `pk_closure/`, `mu_eps_closure/`, `as_amplitude_closure/` (+`kappa/`) — all
  greenfield, disjoint. 2000-band patches 2001–2006 used; 2007+ free.
- **TOOL HAZARD (learned 2005):** in this container the file-creation tool wrote to a stray
  `/home/claude/CPP_work` while git operated on `/root/CPP_work`. Create repo files via bash (`cat >`) or
  verify `git status` shows them before committing. (Caused the 2005 remediation.)

---

## Addendum — R2 hardening sub-arc (Patches 2007–2010, same session)

After the consolidation (2006), R2 was hardened directly:
- **2007** — single-response structure (B=∇×P) shown corpus-derived (c06 line 91 / EW-5), not cartoon;
  excludes the independent-magnetic-field horn. CONV-001 panel dispatch built.
- **2008** — C-vs-K stiffness locking derived from shared Coulomb origin (0739): both C=U''(d_DP) and
  K=U''(a) are curvatures of one Coulomb potential → both ∝ Q → K/C exactly Q-invariant. K∝C at leading
  order; circularity discipline held (absolute Z₀ NOT attempted).
- **2009** — ChatGPT round-1 REVIEW (REVISE) answered: rebut the elastic-lattice counterexample (its
  independent-spring premise fails in the DP Sea); residual narrowed to scale-dependent screening +
  full-action derivation; re-dispatched.
- **2010** — ChatGPT round-2 verdict recorded: **CONFIRM (leading order)** on K∝C; **REVISE** on full PASS
  (scale-dependent screening unbounded; full lattice-EM action curl-coefficient outstanding). Canonical R2
  status in `mu_eps_closure/R2-STATUS.md`.

**R2 pickup point for the next window:** REVISE, leading-order CONFIRMed. Two closure conditions, in order:
(1) the c06 full lattice-EM action — derive μ₀(C), ε₀(C) and the curl coefficient from one action; (2) with
that in hand, bound the scale-dependent screening correction < 10⁻⁶. **Do NOT build a lattice-EM action to
taste — cancellations can survive at pair-potential level and vanish in the field theory (ChatGPT's caution);
that is the cancellation-by-construction trap.** Round-3 panel re-review after (1). 2000-band patches
2001–2010 used; 2011+ free.
