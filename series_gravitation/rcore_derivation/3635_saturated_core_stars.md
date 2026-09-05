# OPEN-GR-SATURATED-CORE-1 rung 1: stars with a saturated core, computed under a working postulate the founder has not yet pictured (P-PINNED-CORE-IS-FLAT: 3375's over-demanded interior read inside a star). Two results: the ordinary neutron-star branch ENDS at central lapse ½ — its maximum mass is the threshold mass, 0.5–15 % below GR's TOV maximum for Γ = 2–3 — and a DISCONNECTED flat-core branch exists at lower core pressures, mostly core, up to C ≈ 0.34 and 1.2–2.4× GR's maximum, stability not established. Reading (b) (only the clocks capped) is GR unchanged. The founder's picture decides between them; both are tests against measured masses

**Patch 3635, Session 162, 5 Sep 2026.** Verify `code/3635_saturated_core_stars_verify.py` (6/6). Reasoning `reasoning/3635.md`. No paper touched. CONV-042 held.

## §1 The postulate and the model
**P-PINNED-CORE-IS-FLAT** (Claude's working postulate, pending the founder's picture asked in 3634): where the register has reached the cap, the lattice is flat at lapse ½ — no gravity inside the core, so pressure and density are uniform at their boundary values; the core's count `M_c = ε_c (4π/3) r_c³` appears to the envelope as `m(r_c) = M_c` (the shell bookkeeping of 3624); the envelope is TOV matter outside `r_c`; the core radius is fixed by the register condition `N(r_c) = ½`. One-parameter family in the core pressure `p_c`, like TOV's. Below the threshold (TOV central lapse > ½) the CPP star is the TOV star (checked to 10⁻¹⁰).

## §2 Result 1 — the ordinary branch is truncated
`N(r_c)` decreases monotonically with `r_c` (a flat core at the boundary density carries *more* count than TOV's compressed interior, and deepens the lapse outside it). So **no flat-core equilibrium exists at core pressures above the TOV threshold**: the TOV sequence simply ends where its central lapse reaches ½. Under (a) the maximum mass of ordinary neutron stars is the **threshold mass**:

| Γ | M_thr / M_max^GR |
|---|---|
| 2.0 | 0.995 |
| 2.5 | 0.923 |
| 3.0 | 0.852 |

For realistic (stiff) EOS this is a 10–15 % reduction of the maximum mass — **a test against the heaviest measured pulsars** (2.08 M☉ at C ≈ 0.25 is at or past the threshold, 3634).

## §3 Result 2 — a disconnected flat-core branch
At core pressures *below* the threshold, the register condition has a second solution with `r_c > 0`: stars that are mostly flat core under a thin TOV envelope. On a 36-point scan the branch is narrow (7/3/2 members for Γ = 2/2.5/3) and reaches:

| Γ | M_max (branch) / M_max^GR | C | r_c/R | M_c/M |
|---|---|---|---|---|
| 2.0 | 2.40 | 0.34 | 0.89 | 0.85 |
| 2.5 | 1.56 | 0.33 | 0.85 | 0.74 |
| 3.0 | 1.16 | 0.31 | 0.75 | 0.55 |

These are the continuum between neutron stars and the R-core (C → 0.375 as the envelope thins). **Their stability is not established** (the turning-point criterion does not carry to a two-branch family without a radial-mode analysis). If stable, they populate the 2.5–5 M☉ gap; if not, they are transients on the way to an R-core.

## §4 Standing
- Reading (b) — the cap touches only the clock rate, the matter's support is GR's — leaves every mass unchanged; reading (a) gives §2 and §3. **The founder's picture (3634's question) decides, and either answer is a prediction confrontable with existing data.**
- Owed if (a): a radial-stability analysis of the flat-core branch; the same computation with a realistic EOS (SLy/APR-class piecewise polytrope) to put M_thr in solar masses against PSR J0740 and J0952.
- Owed if (b): nothing here; OPEN-GR-SATURATED-CORE-1 closes as "clock-only".
- The labels: every number in §2–§3 carries P-PINNED-CORE-IS-FLAT. Not a corpus claim; no paper touched; no panel.
