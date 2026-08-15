# D-SUBPSR-FIELD FIRST PASS — the Version B cascade computed inside the PSR: (1) the founder's question answered provisionally — the signal MAXIMIZES inward, following near-1/s² with a DERIVED ~20% softening at the adjacent shell (no saturation, no diminishment); (2) the dwell-exit kick = exactly 1/12 of the source's per-Moment emission (the even split, by rule); (3) THE SHELL-THICKNESS LAW: thickness/radius is NOT constant — it falls as ≈ 0.9/√N (diffusive spreading), matching the founder's ~10% figure IF the hop count to the PSR is N ≈ 80 — a consonance condition posed back to the examination; GATE HONESTY: the implementation's outward-criterion reading shows ±8–10% directional anisotropy vs AUTOMATON-2's ±0.4% reference — the reading needs reconciliation and all read-outs carry that flag

**Patch 3133 (14 Aug 2026). First pass of D-SUBPSR-FIELD
(OPEN-SUBPSR-1, the founder's examination). Instrument:
`scripts/3133_subpsr_cascade.py` — the ruled Version B relay
(even-split outward among the 12, one volley per GP per Moment,
stateless DI-bits) on the FCC lattice, R ≤ 26. "Turnaround"
terminology ratified by the founder this session (both reversals of
the CP constituents) — adopted corpus-wide.**

## §1 — Gate, stated first

The declared validation gate — reproduce AUTOMATON-2's ±0.4%
pointwise inverse-square at mid radii — **FAILS at this pass:** the
implementation's "outward = strictly increasing Euclidean radius"
reading yields ±8–10% direction-dependent flux structure (r²·flux
oscillating 0.19–0.23 across shells). The reading is therefore NOT
yet the AUTOMATON-2 kernel; reconciliation (the equal-hop-count
geodesic structure vs the radius-increase criterion) is the pass-2
task, and every finding below carries the IMPLEMENTATION-PROVISIONAL
flag. The findings reported are those robust ACROSS the anisotropy.

## §2 — (Q2) The founder's question: diminish or maximize inward?

**MAXIMIZE — with a derived softening.** The steady-state flux grows
monotonically inward as 1/s²-class all the way to the adjacent
shell; the small-s kernel runs mildly BELOW the exact inverse-square
continuation: (s²·flux)/norm ≈ 0.98 at s ≈ 3–5, 0.89 at s ≈ 2.4,
**0.80 at the adjacent shell** — a ~20% softening at closest
approach, no saturation plateau, no inward diminishment, no
divergence beyond the lattice floor. If pass 2 confirms, this is the
DERIVED replacement for the instruments' max(r, 1) assumption — and
notably it is close to what that assumption already does. Bonus
structure: the DIRECTED fraction of the arriving flux is 1.000 at
the adjacent shell (the near field perfectly directional) and falls
to ~0.56 at large radius — the cascade's angular spread accumulating
with distance (provisional; implementation-sensitive).

## §3 — (Q3) The dwell-exit kick (FQ-12's derivable branch)

At the adjacent shell the receiver's per-Moment arrival is **exactly
1/12 of the partner's emission** — the even split among the source's
twelve outward members, straight from the ruled rule. The kick
amplitude in instrument units then follows from the per-Moment
emission normalization (the coupling), which is the pass-2
quantitative target; the STRUCTURE of FQ-12's answer under this
branch is now concrete: kick = (emission)/12 × the derived
adjacent-shell geometry.

## §4 — (Q1) The shell-thickness law — the robust headline

A single volley's occupied shell at hop count N:

| N | ⟨r⟩ | rms | thickness/⟨r⟩ |
|---|---|---|---|
| 6 | 5.65 | 0.73 | 0.305 |
| 10 | 8.79 | 0.99 | 0.264 |
| 14 | 11.87 | 1.19 | 0.236 |
| 18 | 14.93 | 1.37 | 0.215 |
| 22 | 17.97 | 1.52 | 0.199 |

The rms grows ≈ √N (diffusive path-length spread) while ⟨r⟩ grows
≈ 0.82·N·|step| — so **thickness/radius is NOT a constant: it falls
as ≈ 0.9/√N.** The founder's prior ~10% figure is reproduced at
**N ≈ 80 hops to the PSR** — the consonance condition posed back to
the examination: does the corpus's derivation of the 10% shell fix
the hop count near 80, or does the founder's picture use a different
N (in which case the two derivations disagree and the panel/founder
adjudicates)? Also derived: the front's effective radial speed
settles at ≈ 0.82 lattice units per Moment (the geometric cost of
even-split spreading — sub-unit, asymptoting).

## §5 — Pass-2 charter

(i) Reconcile the outward criterion with the AUTOMATON-2 kernel
(gate must PASS); (ii) re-derive §2–§4 under the reconciled rule;
(iii) quantify the kick in array-instrument units (the σ_n
decomposition's component (b), closing FQ-12's derivable branch);
(iv) test the max(r, 1) replacement in one array cell (does the
d_s = 2.0 anomaly respond?). All flagged provisional until then.
Kila6 Route C and the DM ledger untouched; arrival still trumps all.

---

**SUPERSESSION BANNER (appended 14 Aug 2026, Patch 3134; original
above unaltered):** R-RADIAL-AFTER-FIRST (founder ruling) corrects
the relay reading: the even split is the FIRST SUBMOMENT ONLY,
purely radial thereafter. The pass-1 findings derived from
re-splitting every hop — the ~20% softening, the 0.9/√N thickness
law, the 0.82 front speed, the declining directed fraction — are
RETIRED as protocol artifacts (as was F-E2-3's ~10% band, months
older, same cause). The surviving results: exact 1/s² to the
adjacent GP; kick = E/12. See `subpsr_pass2_radial_resolution.md`.
