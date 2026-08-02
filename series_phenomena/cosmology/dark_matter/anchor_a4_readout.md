# ANCHOR A4 READOUT — BLOCKED BEHIND OPEN-FP-6-CONSTANTS

**Patch 2932 (1 Aug 2026). Executes the first step of the charter's
§6 plan (A4 first). Grep-and-read only; nothing derived, nothing
computed. Sources: `flagship_papers/electromagnetism/
sf-6_electromagnetism.tex` (shipped v1.0), read at lines bearing on
ε₀'s provenance.**

## §1 — WHAT SF-6 ACTUALLY PROVIDES

SF-6's own rigor ledger is explicit and consistent throughout the
paper: the quantitative constants μ₀, ε₀, c (and γ(v)) are **Tier-2
toy-model results, reached "by tuning parameters"**, and the paper
"does not present μ₀, ε₀, c as zero-parameter results; it registers
OPEN-FP-6-CONSTANTS (first-principles EM constants without parameter
tuning) and inherits the gap honestly." The Tier-1 content is the
structural relation c = 1/√(μ₀ε₀), Z₀ = √(μ₀/ε₀) and the E–B lock
(common eDP-stiffness origin) — algebraic identities among CODATA
values, verified as such by `code/1600_verify_sf6_core.py`, which the
paper itself labels "not first-principles CPP derivations of those
constants."

## §2 — THE A4 VERDICT

**A4 is NOT currently an anchor.** The charter's question — does the
corpus's ε₀ expression resolve n_DP separately from the per-DP
polarizability, or only their product? — has answer: **neither.** No
corpus expression ε₀ = f(n_DP, α_DP, …) with independently registered
inputs exists; the tuned Tier-2 values carry no extractable density
information. A4 converts into a usable anchor **only by closing
OPEN-FP-6-CONSTANTS** (first-principles μ₀, ε₀ from the 600-cell
dipole stiffness and shell-broadcast speed), which SF-6 registered at
ship time and which remains open.

**Structural note preserved for the eventual anchor:** the c06
conjecture (SF-6 §classical) that Z₀ = √(μ₀/ε₀) is an
SSV-independent pure 600-cell geometric constant would, if proven,
place the Sea-state (density) channel **entirely in the product**
μ₀ε₀ = 1/c² — i.e., the first-principles A4 anchor would constrain
the local Sea through the local light speed, with the ratio (and α)
density-blind. This is the same conjecture that gates SF-6's
Michelson–Morley falsifier discussion. Unproven; recorded as the
shape the anchor takes if and when FP-6-CONSTANTS closes.

## §3 — CONSEQUENCE FOR THE TRIANGLE (STATED PLAINLY)

Post-2930/2931/2932 state of the anchor set:

| leg | status |
|---|---|
| A1 + A2 + A3 (ZBW ancestry, one leg) | bounds-only for A1/A2; A3 independence audit PENDING |
| A4 (ε₀/Z₀) | **BLOCKED behind OPEN-FP-6-CONSTANTS** |
| A5 class / new channels | none proposed yet |

**The triangle cannot currently be closed from the shipped corpus.**
The release-critical dependency graph therefore now runs, in part,
**through OPEN-FP-6-CONSTANTS** — a cross-sector fact worth stating
plainly: an EM-sector open problem registered at SF-6 ship time is
now load-bearing for the dark-matter OSF deposit. Remaining
possibilities for closing the triangle: (i) the A3 audit finds an
α1-independent conversion (pending, next patch); (ii)
OPEN-FP-6-CONSTANTS closes; (iii) the panel proposes genuinely new
channels (A5 class) at the CONV-001 cycle. Per the charter's failure
criterion, "the triangle cannot be closed from the current corpus"
is itself a fileable finding, and this readout is its first half.

## §4 — LEDGER

Untouched: six of seven; PR7 PARTIAL; B7 holds; Candidate (B) 79.5%;
2855 PROVISIONAL. No value of η, d_DP, or n_DP computed or implied.
