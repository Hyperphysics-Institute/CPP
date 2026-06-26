# Reasoning capture — Patch 2121: Claude data-export -> transcript adapter (Option B)

**STATUS: verbatim (captured at-patch).** Window: 2100-band. Opus worker; integrator = TLA.

TLA ran a 7-day account data export. Confirmed structure: `conversations.json` = top-level LIST of conversations;
each has `uuid/name/summary/created_at/updated_at/account/chat_messages`; each message has
`uuid/text/content/sender/created_at/...`; `sender` ∈ {human, assistant}. Built `scripts/export_to_transcripts.py`
against that real shape — the verbatim source for Option B (no worker retyping, so no summarization can sneak in).

Behaviour: `--list` enumerates all conversations (index/date/msg-count/title) so TLA picks; `--keep "<kw,kw>"`
converts conversations whose TITLE matches any keyword; `--index N,M` converts by index. Maps sender human->TLA,
assistant->WORKER; prefers `text`, falls back to assembling `content` blocks; writes the transcript contract
(front matter incl. `source: claude-data-export`) to `Development/transcripts/<date>_export_<slug>.md`.
Non-selected conversations (theology, personal) stay OUT of the repo. Tested on a synthetic export with the real
structure: --list + --keep filtering + content fallback all correct.

This closes the Option-B loop: export -> adapter -> transcript -> nightly audit + fragmentation. Replaces per-turn
cap blocks as the verbatim path. cap.sh stays as a manual stopgap.

NO THEO. Owned: scripts/export_to_transcripts.py, this fragment. No status move; no canonical value changed.
Next: TLA runs --list on the real export, picks the CPP/DM conversations, converts them; then DM-1 (G1).

Track: WORKFLOW
