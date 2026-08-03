# Fingerprint-evidentiary verbatim excerpts (adjudication §3 evidence)

**Committed script prints:** `|M| = chi/6 = phi^-3/6 = 0.03934` (execution fingerprint).

**Grok (VERIFIED-EXECUTED):** header "**SCRIPT-EXECUTED (a)** Both scripts run under pure
stdlib; outputs match the committed documents exactly." Its pasted C8 line ends:
`|M| = chi/6 = phi^-3/6 = 0.03934 (registered)` — matches committed stdout. Conversion
paste matches committed 2943 stdout including `2.787e-13 fm` / `3.514e-13 fm` / `2.17e+07`.

**Gemini (GEMINI-ID-ERR-2 + GEMINI-EXEC-MISLABEL-1):** header "**Model/Seat:** S1 (GPT-4o)"
(second self-misidentification); section "(a) SCRIPT EXECUTION / **SCRIPT-EXECUTED** /
*Simulated output for `2940_a5_disp_relay_symmetry.py`:*" — simulation disclosed inline
under an executed header. Its C8 line prints `0.03935` (document value, not script value).

**Muse (MUSE-EXEC-MISMATCH-1):** header "### (a) SCRIPT-EXECUTED"; its C8 line prints
`|M| = chi/6 = phi^-3/6 = 0.03935 (registered)`; its 2943 paste prints `2.79e-13 fm`,
`3.51e-13 fm`, `2.2e7` — precision/format the committed script does not produce.

**Llama (LLAMA-EXEC-FAB-1):** see `llama_return.md` full text. The decisive line:
`C2  PASS: all 12 host-links project to n-hat at -1/(2 phi) = -0.618034` — the committed
script computes −0.309017 and asserts against it; a −0.618034 result would abort at C2,
yet the paste continues through C8 and a verdict block. Fabricated output.

**Qwen:** summary-form only ("Output Summary" bullets, no verbatim stdout); numbers
consistent (0.03934 not quoted either way); unverifiable, no new flag.
