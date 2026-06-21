# Development — TP-1: The Truncated Photon

Development history. Full per-patch reasoning in `../reasoning/1700…1708.md`.

## Version timeline
- **v0.1 (Patch 1700)** — triggered by a popular-science write-up of Rukan–Gulla–Skaar, "A truncated photon" (PRL 2026, arXiv:2510.21636). Compatibility analysis against CPP postulates; regularization sketch.
- **v0.2 (Patch 1701)** — divergence class derived logarithmic from the RGS kernel; OPEN-TP-1 OPEN → PARTIAL.
- **Review (Patches 1702–1705)** — self-contained package; 4-reviewer panel (Grok, Gemini, Copilot, ChatGPT); attribution correction (Grok ≠ ChatGPT on review 1); v0.3 consolidation of all calibrations.
- **v0.4 (Patch 1706)** — OPEN-TP-1 advance: cutoff grounded as the intrinsic 600-cell band top $\omega_{\max} = \sqrt{12}/t_P$.
- **v1.0 (Patch 1708)** — bib-gate clearance + Phase-5 registry integration; SHIPPED.

## Key decisions (with alternatives)
1. **Embed, do not explain.** Decision: frame the compatibility map as an embedding of the structures RGS assume, not a CPP derivation of the effect. *Alternative considered:* claim CPP "explains" the truncated photon — rejected as overreach (CPP accommodates RGS; standard QFT already permits it). Driver: ChatGPT/Copilot convergent critique.
2. **Cutoff = intrinsic band top, not imposed $1/t_P$.** Decision: derive the cutoff from QM-5's dispersion and $\lambda_{\max} = z = 12$, giving $\omega_{\max} = \sqrt{12}/t_P$. *Alternative:* leave the cutoff as a renamed Planck-scale regulator — rejected because it left the result "thin" (reviewer caveat). Driver: the OPEN-TP-1 pivot computation (Patch 1706).
3. **Ship v1.0 framework-conditional with OPEN-TP-1 open.** Decision: ship on the EU-1 precedent rather than gate on pinning $C$. *Alternative:* do the HS mode sum first — deferred as the post-v1.0 arc (uncertain, bounded computation; should not block a 4/4-reviewed result).

## Dead ends
- v0.1 phrasing "finite for every physical shutter" — *rejected* (Copilot/ChatGPT): the lattice regularizes only the unphysical instantaneous limit; realistic shutters self-regularize via the RGS gradual bound. Replaced by the two-regime statement.
- Draft patch 1703/1704 mis-attribution (Grok logged as ChatGPT) and an add-vs-modify collision on `reviews-TP-1.md` — *recovered* by rebuilding 1705 as a clean modify.
- Per-paper `TP-1_refs.bib` (drafted at v0.1) — *removed* at v1.0 ship (OS §10 BLOCKING gate); refs migrated to the master bibliography.

## Contributor roles
- **Thomas Lee Abshier, ND** — directed the work and the framework; ship decisions.
- **Claude Opus (Anthropic)** — compatibility analysis, divergence-class derivation, band-top computation, drafting, registry integration.
- **Review panel** — Grok, Gemini, Copilot, ChatGPT (4/4 SHIP, zero physics objections).

## Transcript references
Working-session transcript curated in `transcript-TP-1.md`; per-patch Tier-4 reasoning in `../reasoning/1700…1708.md`.
