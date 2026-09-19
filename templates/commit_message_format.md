# Commit Message Format (registered Patch 4144)

**Rule.** Every commit message is a **short subject line**, then a **blank line**, then the body.

    NNNN <short title, <= 72 chars, starting with the 4-digit patch number>
    <blank line>
    <full reasoning body — as long as the patch needs>

**Why this is a rule and not a preference.** Patches 4132–4143 were committed as a single `-m`
string with no newline, so the whole reasoning body became the *subject*. Measured on the last
three: **4,488 / 3,967 / 4,579 characters**. `git log --oneline -3` then emits ~13,000 characters
of wrapped text into the pager, and the founder has to hold Enter through several screens and
press `q` to get his prompt back after every single apply. That is a real ergonomic cost imposed
on every patch delivery, and it was entirely self-inflicted.

**Gate compatibility — checked, not assumed.**

| gate | reads | effect of this rule |
|---|---|---|
| `code/deferral_gate.py` | `--format=%B` (full message) | unaffected — body still scanned |
| `code/next_id.py` | `--format=%s%n%b` (subject + body) | unaffected |
| `code/continuity_gate.py` | `--format=%s` (**subject only**) | **requires the subject to begin with the 4-digit patch number** — which this rule mandates |

The `continuity_gate` constraint is why the subject must **lead** with `NNNN`. Nothing else about
the subject matters to any gate.

**Delivery block.** The apply-and-push block given to the founder ends with
`git --no-pager log --oneline -3`. The `--no-pager` is belt-and-braces: with short subjects the
pager would not trigger anyway, but a future long-subject lapse should degrade to ugly-but-usable
rather than to a stuck terminal.

**Not retroactive.** Commits 4132–4143 are pushed and are not being rewritten; history is
append-only. `git --no-pager log --oneline -3 | cut -c1-100` reads them tolerably if needed.
