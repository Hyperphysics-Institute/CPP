# OPEN-FP-6-CONSTANTS — the GPT-P2 three-stage derivation path: scoping specification

**Status:** SCOPING ONLY — no computation, no numbers, no verdict bands frozen, no IDs minted. This
document executes the scoping patch called for at the 2936 CONV-001 adjudication ("FP-6-CONSTANTS
scoping patch adopting the GPT-P2 work plan," NEXT STEPS item 2) and sequenced as the canonical next
pointer by the 2946 session-close handover §1. It points to the existing registry entry
**OPEN-FP-6-CONSTANTS** (`frontier_sectors/FP.md`); it does not change that entry's OPEN status.
**Lane:** FP / SF-6 (electromagnetism), cross-window with the DM density campaign at the interfaces
noted in §4 and §6. **Author:** Opus, 2 Aug 2026, Patch 2947.
**CONV-011 position:** because this document freezes NO verdict bands and runs NO computation, it
carries no review-timing freeze itself; instead §7 BINDS every forthcoming stage prereg in this arc
to carry one, frozen before that stage's computation runs.

---

## 1. The target, in one line

Derive the electromagnetic constants **μ₀, ε₀** (hence c = 1/√(μ₀ε₀) and Z₀ = √(μ₀/ε₀)) from the
600-cell eDP dipole stiffness with **zero tuned parameters**, replacing the DP-Sea-Polarization
toy-model values (SF-6 Tier 2), with the prime theorem target being the **SSV-independent-Z₀
conjecture** (SF-6 §4): the impedance ratio is a pure geometric constant, so any SSV/density change
moves only the product μ₀ε₀ = 1/c² (the density channel), never the ratio — keeping α fixed and
confining c_eff variation to the density channel (the registered route to resolving the
Michelson–Morley falsifier).

## 2. The adopted work plan (GPT-P2, structure as adopted at 2936)

Three stages, in order, each its own prereg + patch:

> **single-DP response → collective/local-field correction → observable map;
> per-DP response fixed from non-α1 structure.**

The 2936 adjudication folded the entire vacuum-EM-response cluster (GPT P2 capacitor/susceptibility;
Copilot P1 refractive index; Copilot P3 PVLAS; the Casimir variants) into this item because all of
them require the same missing object — **the Sea's macroscopic polarization law from the single-DP
response** — which IS FP-6-CONSTANTS. The cluster observables land in Stage C.

## 3. Stage A — the single-DP response

**What:** the per-eDP polarizability α_DP(ω) (static limit α_DP(0) first) derived from registered
substrate structure. The corpus already carries the Drude/Lorentz oscillator form for the eDP
(0835 London-depth lineage; regime diagnostics at 0897): α_pol = α_c·ℏc/(μ ω₀²) with ℏω₀ = E_eDP
and μ = m_DP/4, with E_eDP and the eDP Compton size pinned. What Stage A must ADD is the
**restoring-stiffness provenance**: the spring constant must be exhibited from 600-cell cage/edge
geometry and the shipped SF-1/SF-6 structure — never fitted to reproduce ε₀. That is the operative
meaning of "fixed from non-α1 structure."

**Deliverable A:** the α_DP formula + a provenance table listing every input with its registered
source; verify script in `code/` per the reasoning-capture protocol.

**Known wall (frozen HALT rule):** if the restoring law turns out to require the undefined
substrate-thermodynamic / inter-CP-potential framework — the same wall registered at
OPEN-FP-SF-2-η and posed sharply in the Q_stiff scoping (`series_phenomena/cosmology/dark_matter/
qstiff_contact_polarizability_scoping.md` §5) — the stage HALTS and files the dependency. No
tuning is permitted to route around the wall. This is roadblock-class (see §7).

## 4. Stage B — the collective / local-field correction

**What:** the macroscopic polarization law P(E) = f(n_DP, α_DP) with the local-field correction
**derived** for the 600-cell coordination (z = 12) — a Clausius–Mossotti analog computed from the
lattice, not assumed from continuum electrostatics.

**Ledger discipline (binding):** the corpus contains **no value of n_DP**, and this arc must not
mint one. Every Stage B result stays a FORMULA with n_DP explicit. The density-dependence
factorization is precisely the bridge to the DM campaign's scarce-factor accounting — the reason
the vacuum-EM cluster surfaced in the 2936 M3 shortlist review in the first place. If Stage B/C
plus one measured observable would ever determine n_DP, that determination is its OWN prereg in
the DM lane, not a by-product here (no-motive rule, same discipline as the ξ₂ arc split at 2946).

**The structural question Stage B must answer:** which combinations of {μ₀, ε₀} are density-free?
In this language the SSV-independent-Z₀ conjecture is the statement that the n_DP-dependence
cancels in the ratio μ₀/ε₀ while surviving in the product. Stage B's deliverable is the
theorem-grade classification of density-free vs density-channel combinations, with the
cancellation (if it holds) exhibited, not asserted.

**Anti-α1 rule, inherited verbatim** (a5_disp_prereg.md §2 / a5_disp_conversion_prereg.md §2): any
parametrically small factor appearing anywhere in the chain must be exhibited as a formula whose
smallness has registered provenance — "small because we need it small" is barred.

## 5. Stage C — the observable map

**What:** the map from the Stage A/B polarization law to observables, in two groups.

**(i) The constants themselves:** μ₀, ε₀ expressed in 600-cell dipole stiffness + shell-broadcast
speed (the registry's stated solution shape); c from the product; Z₀ from the ratio; the
SSV-independent-Z₀ conjecture promoted to theorem-grade IF Stage B's cancellation holds (theorem
registration is a Stage C decision, no THEO slot minted here); the Michelson–Morley resolution
route made explicit (c_eff variation confined to the density channel).

**(ii) The folded cluster:** capacitor/vacuum susceptibility (GPT P2); optical refractive index of
the ambient Sea (Copilot P1); PVLAS vacuum birefringence (Copilot P3); Casimir variants. Frozen
consistency constraint on (ii): Patch 2940 established **γ ≡ 0 for the ambient Sea** (CASE-Q; the
physical 3D section is achiral, linear birefringence and TOF coefficients vanish identically at
O(kd)) — so the Stage C map MUST reproduce a null ambient birefringence at leading order. PVLAS
enters as a consistency check on a coefficient CPP predicts to vanish, not as a constraint on d_DP
(same inadmissibility logic frozen at 2942 §4).

**ξ₂ interface (registered dependency, not a merge):** the Stage B/C machinery — the lattice
polarization law at finite k — is the natural producer of the O(kd)² relay coefficient ξ₂ that
scales the ACTIVE d_DP ceiling (2945). The ξ₂ derivation stays its own arc with its own prereg
(future_projects.md, registered 2946, no-motive rule); this scoping records only that Stage B's
finite-k expansion is the expected substrate for it, so the two arcs must cite one another's
frozen structure rather than re-deriving.

## 6. Frozen corpus facts the derivation must respect (refutation surface)

1. **CASE-Q (2940, ratified 2944):** all O(kd) coefficients vanish in every channel; ambient 3D
   section achiral. A Stage C map producing linear dispersion or ambient birefringence is refuted
   by the corpus's own registered result — falsifier-class (see §7).
2. **SF-6 Tier-1 identities:** c = 1/√(μ₀ε₀) and Z₀ = √(μ₀/ε₀) hold algebraically
   (`code/1600_verify_sf6_core.py`); the derivation supplies values/structure, never breaks the
   identities.
3. **The ACTIVE d_DP ceiling (2945):** d_DP ≤ 3.51 × 10⁻²⁸ m · ξ₂^(−1/2). Any Stage A/B structure
   implying a mesh scale must be checked against it.
4. **Ledger:** no value of η, d_DP, or n_DP exists anywhere in the corpus, and none is minted in
   this arc.
5. **Michelson–Morley:** the toy-model c_eff(v) tension (SF-6 §9) is the standing falsifier this
   arc is expected to resolve or sharpen — a Stage C result that REPRODUCES the toy-model
   absolute-frame magnitude without the density-channel confinement is falsifier-class.

## 7. CONV-011 compliance (binding on all three stage preregs)

Read `todolist.md` CONV-011 verbatim before drafting any stage prereg. This scoping document
freezes no verdict bands and runs no computation, so it requires no timing freeze itself. Forward
requirements, frozen now as the arc's default classification (each stage prereg must confirm or
re-freeze its own before computation):

- **Falsifier-class branches** (pre-action review required): a Stage C map contradicting CASE-Q
  (§6.1); a Stage C map reproducing the toy-model absolute-frame magnitude (§6.5); a Stage B
  result showing the Z₀ density-dependence does NOT cancel (kills the conjecture and the
  Michelson–Morley route — the arc's own CASE-L analog).
- **Roadblock-class** (panel convenes per standing economy convention): the Stage A HALT on the
  substrate-thermodynamic wall (§3).
- **Conservative/bound-type branches** (combined completed-package review permitted): formula-only
  results with n_DP explicit; the density-free/density-channel classification when the
  cancellation HOLDS; consistency-check confirmations in Stage C(ii).

Discretion over review timing after a branch is revealed is removed (CONV-011, verbatim).

## 8. Sequencing and scale estimate

Stage A: 1–2 sessions (analytic derivation + verify script + prereg). Stage B: 1–2 sessions.
Stage C: 1 session + one CONV-001 panel cycle on the completed package (or earlier per §7 if a
falsifier-class branch fires). Queue position: this scoping discharges 2946 handover §1; the DM
lane's A5-SHOT / A5-LENS preregs remain at queue position 2 and are untouched; FP-6 stage work
proceeds in the SF-6 lane at founder-mechanical convenience.

## 9. What this document does NOT do

No registry IDs minted; no THEO slots reserved; no numbers computed or quoted for any open
quantity; no verdict bands frozen; OPEN-FP-6-CONSTANTS remains OPEN; the DM ledger is untouched
(six of seven; PR7 PARTIAL; B7 holds; Candidate (B) 79.5%; 2855 PROVISIONAL; d_DP ceiling ACTIVE).
