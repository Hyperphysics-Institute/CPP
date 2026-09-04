# GWTC-3, in hand: the echo search deliberately starts after the ringdown — so the CPP cavity is outside it by construction — and the measured GW150914 ringdown (f₂₂₀ = 254.6 +16.1/−12.2 Hz, τ₂₂₀ = 4.51 +1.10/−0.99 ms) narrows the wall's impedance to a sliver just softer than Neumann, β ≈ −0.02 … −0.03. Provisional edges; firm conclusion

**Patch 3616, Session 161, 4 Sep 2026.** Verify `code/3616_ringdown_band_gwtc3_verify.py` (4/4). Source: GWTC-3 TGR (arXiv:2112.06861) §VIII.B and Table XIII, pasted by the founder. Reasoning `reasoning/3616.md`.

## §1 What the GWTC-3 echo search is — and what it excludes
- **Morphology-independent** (BayesWave, combs of decaying sine–Gaussians; Δt prior `[0, 0.7] s`, Q ∈ [2, 40]); p-values uniform, no evidence.
- **The analysis window starts at `t_event + 3τ₂₂₀`** — "safely beyond the plausible duration of the ringdown" — and background trials are chosen "to avoid the presence of putative echoes signals." So the search is designed to look **after** the ringdown has died. A CPP cavity with a 0.7 ms round trip produces a *modified ringdown* during exactly the epoch the search excludes. **The echo searches, by construction, do not test the CPP wall.** (3615's inference, now from the paper's own words.)

## §2 The measurement that does — Table XIII (pSEOBNRv4HM ringdown), GW150914
`f₂₂₀ = 254.6 +16.1/−12.2 Hz` → 90% fractional interval **[−4.8%, +6.3%]**; `τ₂₂₀ = 4.51 +1.10/−0.99 ms` → **[−22%, +24%]**. (Other loud events: GW200129 `246.4 +14.5/−18.1`, `4.68 +1.01/−0.97` — similar precision.)

## §3 The band
The 3615 wall poles (prograde (2,2), χ = 0.68, wall at 2.734 M) against the Kerr reference `0.528 − 0.082i`:

| β | δf | δτ | inside GW150914's box? |
|---|---|---|---|
| 0 (Neumann) | −2.0% | −27.2% | no (τ just outside −22%) |
| −0.01 | −2.7% | −23.9% | no (marginal) |
| **−0.02** | **−3.5%** | **−20.4%** | **yes** |
| **−0.03** | **−4.2%** | **−16.5%** | **yes** |
| −0.04 | −5.0% | −12.3% | no (f just outside −4.8%) |
| −0.05 | −5.8% | −7.7% | no |
| +0.05…+0.10 | +2…+5% | −40…−51% | no |
| hard wall (shipped) | ~+45% | — | far outside |

**A surface at 1.33 r_S is compatible with GW150914's measured ringdown for a wall impedance in a sliver just softer than Neumann: `β ≈ −0.02 … −0.03` at the ringdown frequency** (in units of 1/M). Exact Neumann is marginal (damping 27% short). Hard walls, soft walls, and anything stiffer than +0.05 are out.

**Provisional, in the edges only:** the deviations are measured against the literature Kerr value at a ≈ 0.7 rather than against the event's own IMR-inferred (M, χ); the pSEOB fractional-deviation intervals (δf̂₂₂₀, δτ̂₂₂₀) in the same paper would place the box exactly and combine events. The *conclusion* — a narrow near-Neumann band, with hard and soft walls excluded — does not depend on that.

## §4 What the band means for the theory
- The shipped `X = 0` (GR-2 V1.6 basis) is **excluded by the ringdown**: it would have shifted GW150914's frequency by tens of percent.
- The theory's own derived laws (3384 odd; 3391 even, RW-gauge) were Neumann-like at the mode frequency — inside or adjacent to the band. The unexplained "Neumann crossing at the barrier top" (3383) is the requirement the ringdown imposes.
- The lattice-frame (C5) law must land in this sliver. That is now a **numerical target for OPEN-GR-LATTICE-FRAME-1**, and a falsifier: if the C5 wall gives `β` outside `[−0.05, +0.05]` at the ringdown frequency, the R-core at 1.33 r_S is ruled out by an existing measurement.
- **S-EMPIRICS-ARBITER is fulfilled without waiting for an echo:** the calibration object β(ω) is pinned at the ringdown frequency by the ringdown. What the echo (if ever seen) would add is β's *frequency dependence* — the second line and the interior return.

## §5 GR-2 V2.0, in shape
The two impedance maps (3613, 3614), the barrier transmission, the ringdown band (this patch, with the exact pSEOB box when supplied), and the statements: *the echo searches exclude the ringdown epoch by design and do not test a 0.7 ms cavity; the observed ringdown confines a 1.33 r_S surface to a near-Neumann impedance; the hard wall of V1.6 is excluded.*

## §6 Requests (edges only)
The pSEOB deviation table (δf̂₂₂₀, δτ̂₂₂₀ 90% intervals, GW150914 and combined) from the same paper's §VIII.A; and, for the record, Lo et al.'s delay prior.
