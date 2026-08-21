# Changelog — GR-1d: Gravitational-Wave Echoes from the Planck Core

**Paper:** `series_gravitation/GR_companion_papers/GR-1d_gravitational_wave_echoes/GR-1d_GW_echoes.tex`
**Convention:** canonical filename never carries a version suffix.

**STATUS: reconstructed.** No changelog was kept; entries below come
from git history, the .tex date line, and the August 2026 patch record.

---

## V1 – V2 (merged) — 18 March 2026

Authoring history not recorded contemporaneously. The `\date` line reads
"Version 2 (merged)", indicating a consolidation of earlier drafts whose
content deltas were not captured.

## Re-identification — 19 August 2026, Patch 3230 (Session 149)

Moved into `series_gravitation/GR_companion_papers/` and re-identified
**c09 → GR-1d** (OPEN-ORG-023 Item 2, founder-approved layout).

## PD-001 formatting — 20 August 2026, Patch 3273 (Session 150)

W-A: CP/GP Signature subsection added. Compile clean.

## Documentation suite — 20 August 2026, Patch 3286 (Session 152)

OPEN-GR-PPP-1 W-B row 7: ten-file suite produced; this changelog
created. **Status note:** this paper's own open problems are, unusually
for the arc, all still open — its item 1 (Planck-core reflectivity)
depends on the strong-field interior, which the field-equation programme
did not reach (`op:einstein`). No staleness finding. No .tex change.

## V3 — 20 August 2026 (Patch 3302) — Ratified amendment: surface location, delay, reflectivity

**Review basis:** CONV-030 — HALT-GR-1D-DELAY WARRANTED 5–0; delay grade
BOTH-WITH-DICTIONARY-CAVEAT 4–1; |R|=1 SOUND-family 5–0. Founder-ratified
20 Aug 2026. Machine record: `code/3297_rcore_verify.py` (9/9; three
seats SCRIPT-EXECUTED).

**What changed (anti-erasure: all V2 text preserved verbatim with dated
supersession notes):**
- V2 Theorem (Δt = (4GM/c³) ln(2GM/c² l_P) ≈ 112 ms) SUPERSEDED — its
  premise (reflecting surface at r_S + l_P) rests on the areal reading
  corrected by GR-1c V2.3; the exclusion surface sits at isotropic
  r̄ = μ, areal (9/8) r_S, outside the never-formed horizon.
- New §Amendment: corrected surface (Buchdahl radius, lapse 1/3, z = 2);
  reflectivity DERIVED not assumed (honest restatement — one
  conservation/storage argument + one dynamical constraint; V2 Open
  Problem 1 CLOSED with phase/frequency refinements at RCORE-2(ii)/(vi));
  both delay closed forms with the dictionary question stated INLINE,
  Level-A benchmark (Δt_A = (3/2 + 8 ln 2) GM/c³), finite-ℓ honesty
  (8.60 vs 8.20 GM/c³); GW150914 numbers WITH ERROR BARS
  (2.15 ± 0.14 ms / 0.91 ± 0.06 ms at 62 ± 4 M_⊙, linear-in-M stated);
  amended predictions table (f_echo now IN the LIGO band for
  stellar-mass events — the prediction more exposed, not less).
- PLS amendment paragraph; amplitude-section note (5% now
  parameter-free); Open Problems items 1 (CLOSED note) and 4 (template
  formula amended; systematics → RCORE-2(viii)).
- Header amendment block; version line → Version 3.

**Compile:** pdflatex ×2, 0 errors, no undefined refs, 13 pages.
