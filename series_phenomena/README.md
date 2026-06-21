# `series_phenomena/` — Empirical Phenomena Explained from CPP Axioms

**Established:** 31 May 2026 (Session 149, Patch 0700), opening the tetra-gravity dark-matter arc as its first member.
**Purpose:** the **home of record** for any empirical phenomenon of nature that the CPP programme attempts to explain by derivation from its axioms and theorems — at *any* maturity, from first sketch through shipped result. A phenomenon matures **in place** here; it is not migrated on completion.

---

## Why this tier exists (the three-container boundary)

CPP's paper containers serve three distinct roles. Keeping them distinct is what prevents the "same paper, two plausible homes" failure mode.

| Container | Role | Maturity |
|---|---|---|
| `series_<sector>/` (SM, EW, QM, SR, SS, SD) | **Foundational machinery** — the theory sectors that build the axioms→theorems apparatus. | Theory development |
| **`series_phenomena/`** (this tier) | **Phenomenon derivations** — applying the machinery to explain a specific observation in nature. Home of record, any maturity. | Sketch → gated conjecture → shipped |
| `flagship_papers/` + `series_umbrella/` | **Apex / unification** — `flagship_papers/` holds the legacy SF-line apex presentations; `series_umbrella/` holds problem-arc containers (e.g. the substrate chirality arc, the F-line foundational flagships). | Apex / cross-sector synthesis |

**Boundary rule (going forward):** new single-phenomenon work lands in `series_phenomena/`. `flagship_papers/` and `series_umbrella/` are **not extended with new per-phenomenon papers**; they remain in place for their existing SF-line / F-line / unification contents. Existing `flagship_papers/` subfolders (`neutrinos`, `quarks`, `charged_leptons`, …) pre-date this decision and are **not migrated** — that inconsistency is historical, not a model to copy. *(This cross-tier boundary is pending formalization as a `programmatic_decisions/PD-###` record; see the DM-arc handover discussion.)*

The label "flagship" is thereby kept top-tier (apex / unification), rather than diluted by becoming the home for "pretty much every phenomenon," which is what `series_phenomena/` now absorbs.

---

## Directory template

```
series_phenomena/
└── <domain>/                      ← a domain of phenomena (cosmology, …)
    └── <phenomenon>/              ← one phenomenon (dark_matter, …); each is its own umbrella
        ├── reasoning/             ← per-patch reasoning fragments (reasoning/<patch>.md)
        ├── scripts/               ← physics verification scripts (scripts/<patch>.py) — only once a step computes
        ├── <phenomenon>.tex       ← the paper — ONLY after the phenomenon's falsification gates survive
        └── documentation_suite/   ← companion suite — only at/after paper SHIP
```

**Grow the tree as phenomena are actually worked.** Do **not** pre-create empty domain folders (`mechanics/`, `field/`, `kinetic/`, `information/`, …) speculatively — that is the structure-ahead-of-content anti-pattern the programme's "accumulate-then-group" discipline (programme_orientation Ch. 35.6) exists to avoid. A domain folder appears when its first phenomenon does.

**Maturity discipline (falsification-first):** a phenomenon that is still a gated conjecture populates only `reasoning/` (and `scripts/` once a step computes). No paper draft, anthology framing, or `documentation_suite/` until the phenomenon's own falsification gates survive. For dark matter, that gate is "Steps 1 and 2 computed and survive" (see the arc handover).

---

## Relationship to the frontier sector codes

The folder **domain** is not always 1:1 with a frontier **sector code**. Phenomenon domains group by *what is being explained*; sector codes group by *which physics drives the registry entry*.

- `cosmology/` (domain) ↔ **COSMO** (sector code) — clean match for the DM phenomenon (CONJ-COSMO-1 / OPEN-COSMO-DM-1).
- **DPS** (dipole-sea population) is a substrate *mechanism* feeding DM, not a phenomenon in its own right — its conjectures (CONJ-DPS-1/2/3) stay registry-only in `frontier_sectors/CONJ.md` and do **not** get a `series_phenomena/` folder.

When in doubt: if it's an observation in nature, it gets a phenomenon folder; if it's a mechanism the framework uses, it stays in the sector machinery and the registry.

---

## Current members

| Domain | Phenomenon | Status | Frontier home |
|---|---|---|---|
| `cosmology/` | `early_universe/` (paper **EU-1**) | **SHIPPED v1.0** (6 Jun 2026, 3/3 panel) — primordial scalar spectral index $n_s = 1 - 2/N_* \approx 0.9649$ (PRED-C-96) + running $\alpha_s \approx -0.0006$ (PRED-O-34); zero-new-axiom, framework-conditional. Paper at `cosmology/early_universe/EU-1/`. | `frontier_sectors/SR.md` (OPEN-EU-1); n_s arc Patches 0742–0783. |
| `quantum_optics/` | `photon_truncation/` (paper **TP-1**) | **SHIPPED v1.0** (20 Jun 2026, 4/4 panel) — the Rukan–Gulla–Skaar truncated photon (PRL 2026) embedded in CPP: compatibility (QM-4/QM-5) + foundational regularization; divergence class derived, cutoff grounded as the intrinsic 600-cell band top $\omega_{\max}=\sqrt{12}/t_P$ ($\lambda_{\max}=z=12$). NO THEO, NO PRED; PROP-TP-1-1. Paper at `quantum_optics/photon_truncation/TP-1/`. | `frontier_sectors/QM.md` (OPEN-TP-1); `frontier_sectors/PROP.md` (PROP-TP-1-1); TP arc Patches 1700–1708. |
| `cosmology/` | `dark_matter/` | Far-frontier gated conjecture (CONJ-COSMO-1); falsification-first sequence Steps 0–5. | `frontier_sectors/CONJ.md` (OPEN-COSMO-DM-1 + CONJ-COSMO-1); arc handover in `handovers/`. |
