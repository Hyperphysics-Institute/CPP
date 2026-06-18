# Integration Manifest — &lt;PAPER-ID&gt; &lt;title&gt;

**Collaborator:** &lt;name&gt;  **Branch:** `collab/<paper-id>`  **Date:** &lt;YYYY-MM-DD&gt;  **Mode:** review | research

> Fill every section. Use **[suggested]** for any name/ID — the PI allocates the real one. Write "None." where nothing applies. **Do NOT edit any hot-list file yourself** — describe the change here and the PI applies it. This file lives at `<paper-folder>/INTEGRATION_MANIFEST.md`.

## 1. What landed in the paper folder (merges directly on branch merge)

- `<file>` — &lt;added / changed; one line on what&gt;
- ...

## 2. Review status

- Reviewers + verdicts: &lt;e.g., ChatGPT SHIP / Grok minor-revise / Gemini SHIP / Copilot SHIP&gt;
- Review records at: `<paper-folder>/reviews/...`
- Review package link (raw GitHub URL): &lt;url or "n/a"&gt;
- Net verdict: &lt;SHIP / revise / hold&gt;

## 3. OSF deposit

- Status: needs deposit | deposited (DOI: &lt;...&gt;)
- Files to deposit: &lt;paper `.tex` / PDF / ...&gt;

## 4. Shared-state changes requested (PI applies these — do not edit the files yourself)

For each: the file, the change, a **[suggested]** name, and the content/rationale.

- **paper_catalog.md** — add row? &lt;yes/no&gt; — [suggested] row: &lt;one-line&gt;
- **bibliography/cpp_references.bib** — add self-entry? &lt;yes/no&gt; — [suggested] key `abshier2026<id>`; content: &lt;author / title / year / note; doi pending until OSF posts&gt;
- **theorem-registry.md** — register a theorem/proposition? &lt;yes/no&gt; — [suggested] `<THEO|PROP>-<S>-N`; statement: &lt;...&gt;; source: &lt;paper, location&gt;; axioms: &lt;...&gt;; **count impact:** &lt;e.g., "+1 proposition; no theorem-total / Summary-Statistics change"&gt;
- **frontier_sectors/&lt;S&gt;.md** — open/close a problem? &lt;yes/no&gt; — [suggested] `OPEN-<S>-N`; one-line statement; status (resolved/open by this paper)
- **predictions.md** — add a prediction? &lt;yes/no&gt; — [suggested] `PRED-...`; value; comparison to data
- **INDEX.md** — nav row: &lt;one-line&gt;
- **programme_orientation.md** — mention warranted? &lt;yes/no&gt; — &lt;one-line + where it goes&gt;
- **theory-overview.md / master_glossary.md / methods_catalogue/** — &lt;as applicable, or None.&gt;

## 5. Physical-picture questions for the PI

- &lt;anything where the CPP mechanism / substrate judgment is needed; otherwise "None."&gt;

## 6. Self-check before notifying the PI

- [ ] All my writes are inside the paper folder (no hot-list file edited on the branch)
- [ ] No IDs/counts allocated by me (everything is **[suggested]**)
- [ ] No placeholder tokens left (`[TO BE WRITTEN]`, `TODO`) in deliverables
- [ ] Paper compiles (`pdflatex` clean) if a `.tex` changed
- [ ] Branch pushed; PI notified
