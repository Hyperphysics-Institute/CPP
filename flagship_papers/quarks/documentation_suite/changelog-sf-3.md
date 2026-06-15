# SF-3 Changelog — Quark Sector Flagship

**Location:** `/CPP/flagship_papers/quarks/documentation_suite/changelog-sf-3.md`
**Paper:** `flagship_papers/quarks/sf-3_quarks.tex`
**Convention:** Canonical version-archaeology record (per `operating_system.md` version-archaeology architecture rule). The `.tex` title block shows only the current version; per-version history lives here.

---

## v0.1 — 14 June 2026 (Session 161, Patches 1500/1501; 1500-band SF-3 window)

First complete pre-review draft. Assembled from the SF-3 structural core (Patch 1308) and outline (Patch 1303) to the 16-section paper-formatting standard. Synthesis/reframing of shipped results — **no new derivation**. (Drafted at Patch 1500 with an over-claiming "v1.0" title-block label; relabelled to v0.1 at Patch 1501 to match the SF-2 drafting precedent, where v1.0 is reserved for the post-review SHIP. No content change.)

**Content established:**
- §3 Zero-parameter heavy-quark mass spectrum, Route A (SM-8/SM-9): $M_q = m_e(z/\phi)V^{7/3}$, top relay $\times z C_F$; RMS 2.1% (s/c/b/t); $m_c$ demoted to derived.
- §4 Strong coupling $\alpha_s = 5/(8\phi)$ as face-mode fraction; exact complementarity $\sin^2\theta_W + \alpha_s = 1/\phi$; ratio $F/E = 5/3$ (SM-7/SM-6).
- §5 Quark Koide phase $\theta_{\rm quark} = 124.04^\circ$ (0.05%); **Proposition 5.1 (phase–mass independence)** — the one in-paper result: phase depends on $\{\alpha_s, \sin^2\theta_W, z\}$ only, so no re-grounding on derived $m_c$ is needed (sharpens the 1303 wording).
- §6 Three generations forced; no fourth quark (SM-8).
- §7 Calibration ledger: Route-A adjudication (single $m_e$; $m_c$ derived).
- §8 OPEN-FP-3-CKM registered in-paper (mixing/quark $CP$ phase undelivered); SF-4-$\delta_{CP}$ parallel.
- §10 §4.1A CP/GP Signature; §11 mapping table; §13 §4.1B Swarm-Validation Contribution + Problem Status.

**Verification:** `code/1500_verify_sf3_core.py` reproduces all numerics from first inputs — ALL CHECKS PASS. Two-pass pdflatex: 11 pages, 0 errors, 0 undefined references.

**Deferred to ship (flagged integration patch, after refresh against origin/main):** OPEN-FP-3-CKM registration in `frontier_sectors/`; `predictions.md` swarm-counter update; bibliography migration from inline `thebibliography` to master `cpp_references.bib`.

**Not yet done:** multi-AI review cycle (CONV-001 panel package); documentation suite companion files; figures (none in v1.0).
