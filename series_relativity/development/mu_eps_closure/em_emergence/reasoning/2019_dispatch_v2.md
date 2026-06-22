# Reasoning capture — Patch 2019: self-contained round-3 dispatch + CONV-001 template fix

**STATUS: verbatim (captured at-patch).** Window: 2000-band. Opus worker; integrator = Thomas.

## What went wrong, owned plainly
ChatGPT couldn't review because my 2018 dispatch put a SUMMARY of the claims + GitHub links instead of the
full finding content inline. I tested the URLs from the container: both return HTTP 200 (repo public, links
correct) -- so the failure was NOT broken links; the reviewer simply did not browse them (most chat
reviewers don't). CONV-001 already mandates full rendered content inline (template item 3); I violated it.

## The fix (two parts)
1. Rebuilt R3_panel_dispatch.md SELF-CONTAINED: both findings (2016 Z0-PARTITION-RESULT + 2017
   MU0-EMERGENCE-SCHEME) embedded IN FULL inline, under DOCUMENT 1/2 separators, with the Q1/Q2/Q3 attack +
   verdict request at the end and the URLs demoted to a supplementary reference. The reviewer fetches
   nothing; Thomas pastes one block. Fence verified (5-backtick outer, no inner collisions).
2. CONV-001 template (templates/presentation_file.md): corrected the misleading premise that reviewers
   "fetch raw URLs" -> links are a SUPPLEMENTARY reference only, most reviewers do NOT browse; and made item
   3 (full inline content) explicitly MANDATORY/load-bearing, with the multi-file DOCUMENT N of M pattern.
   This is the actual generalizable lesson, so it belongs in the template, not just this one dispatch.

## On Thomas's suggestion
Thomas proposed adding blob/raw URLs to the template. I redirected honestly: the template already had URLs;
adding more would not have fixed a "reviewer doesn't browse" failure. The real fix is inline content (which
the template already required and I failed to deliver) + correcting the template's wrong assumption that
reviewers fetch URLs. That solves Thomas's stated friction (no repo trip) directly.

## Discipline
- Owned path em_emergence/ (dispatch) + templates/presentation_file.md (shared workflow template, Thomas-
  directed workflow fix). NO THEO. Files via bash/str_replace; git status verified.

---
## Correction (Patch 2020, per ChatGPT round-2-on-the-patch)
The sentence above — "ChatGPT couldn't review because my 2018 dispatch put a SUMMARY + links instead of the
full content" — OVERSTATES the diagnosis. The missing content was *a* cause but not the only one: ChatGPT
notes its verdict on the underlying theory would likely be REVISE even with the documents present. So the
2018 failure had two independent causes (nothing to review AND an unresolved claim); embedding the content
fixes the first, not the second. Corrected to avoid implying that inline content would have changed the
verdict.
