# Changelog — GR-1e: Hawking Radiation and the Planck Remnant

**Paper:** `series_gravitation/GR_companion_papers/GR-1e_hawking_radiation_planck_remnant/GR-1e_hawking_radiation.tex`
**Convention:** canonical filename never carries a version suffix.

**STATUS: reconstructed.** No changelog was kept; entries below come
from git history, the .tex date line, and the August 2026 patch record.

---

## V1 — 18 March 2026

Authoring history not recorded contemporaneously.

## Re-identification — 19 August 2026, Patch 3230 (Session 149)

Moved into `series_gravitation/GR_companion_papers/` and re-identified
**c10 → GR-1e** (OPEN-ORG-023 Item 2, founder-approved layout).

## PD-001 formatting — 20 August 2026, Patches 3273–3274 (Session 150)

W-A: CP/GP Signature subsection added. **W-A2: a legacy compile defect
repaired** — the macro `\TH` collided with LaTeX's built-in thorn
character; renamed `\THaw` at its definition and all six uses. Compile:
0 errors.

## Documentation suite — 20 August 2026, Patch 3287 (Session 152)

OPEN-GR-PPP-1 W-B row 8: ten-file suite produced; this changelog
created. **No staleness finding** — all four of this paper's open
problems remain genuinely open (all require quantum-field or
strong-field-interior treatment the programme has not attempted).
**Forward pointer registered** (see `reasoning-GR-1e.md`):
NOTE-GR-CSTAR-STRONGFIELD, minted at CONV-027 and flagged explicitly for
the GR-1d/GR-1e lane, has never been folded into this paper. No .tex
change.

## V1.1 — 20 August 2026 (Patch 3303) — Ratified amendment: horizonless reading

**Review basis:** CONV-030 (AMEND 5–0; F-R1 CORRECT-family 5–0);
founder-ratified 20 Aug 2026.

**Changes (anti-erasure; no equations changed, no silent re-derivation):**
- Amendment Notice added: (i) r_core is the isotropic radius, areal image
  (9/8) r_S, outside the never-formed horizon; (ii) horizon-based
  emission language superseded at the interpretive level — the emission
  mechanism for the horizonless hard-surfaced body (surface temperature,
  spectrum, termination argument in surface form) is RE-OPENED under
  OPEN-GR-RCORE-2, not silently re-derived; (iii) Proposition
  prop:stability UNAFFECTED and PROMOTED — load-bearing pillar of the
  |R|=1 derivation (GR-1d V3); (iv) the remnant-endpoint census logic
  stands.
- Dated notes at the intro r_core mention and Open Problem 1 (inner
  boundary now the derived-Dirichlet exclusion surface; problem widened
  honestly).
- Header amendment block; version line → 1.1.

**Compile:** pdflatex ×2, 0 errors, no undefined refs, 9 pages.
