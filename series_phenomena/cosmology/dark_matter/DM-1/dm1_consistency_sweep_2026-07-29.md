# DM-1 CONSISTENCY SWEEP — NO CONTRADICTION; THE STABILITY CLOCK WAS RESET

**Patch 2871, 29 July 2026. P3 of the 2861 sequence, executed. The
contradiction the worker reported at 2859 §7 does not exist. A real and
more consequential finding replaces it.**

---

## §1 — RETRACTED: DM-1 does not contradict itself

2859 §7 claimed:

> ~~"§(i) records the founder's CONV-004 ruling that the debt language is
> *superseded*… §(vi) still reads 'two explicit derivation debts as
> promotion gates.' **The paper contradicts itself on whether its own
> promotion is gated.**"~~

**It does not.** The v1.4 revision notice handles this explicitly, twice:

- §(iii) opens its governance clause with *"**Governance (revised,
  superseding the v1.3 sentence)**"* and states the replacement
  conditions (overdetermination maintained; stability cycle; standing
  derivation target open).
- The notice closes: *"**The v1.3 notice below is retained per house
  discipline, with its governance items superseded as stated.**"*

§(vi) is explicitly labelled *Governance* and therefore falls under that
supersession. **The stacked-notice structure with explicit supersession
markers is house discipline, correctly applied.** The worker read two
notices as concurrent when the later one says in terms that it replaces
the earlier.

**This is the fifth claim this session asserted without adequate
checking** (C23 gloss; PR7 "unexamined"; the 2814 audit impugned;
2869 §4's Stage B/C contradiction; this). **No new mitigation is
proposed — three have been written and none held. What changed the rate
was the 2865 standing order to search before forming a position, and
this patch is what that order looks like when it works: the claim was
checked and died before reaching the founder as an action.**

## §2 — THE REAL FINDING: v1.4's stability clock was broken three days after it started

v1.4's status line reads: *"the stability-cycle clock starts at Patch
1890; **OSF on its completion**."* (6 July 2026.)

**Every subsequent commit to `DM-1_substrate_dark_matter_candidate.tex`:**

| patch | date | subject |
|---|---|---|
| **1890** | 6 Jul | DM-1 v1.4 SHIPPED — clock starts |
| 2360 | 9 Jul | **DM-1 v1.5** |
| 2362 | 9 Jul | joint-round adjudication + **executed repairs** (five returns) |
| 2365 | 9 Jul | F-DM3-4 rate computation stage 1 — conditional |
| **2369** | 9 Jul | **THE SECOND KILL, FOUNDER-ATTESTED — ARC PIVOT** |

**A founder-attested kill and an arc pivot are load-bearing corrections
by any reading.** The clock that v1.4 made the OSF condition was reset
on 9 July, three days after it started, and **nothing in the paper
records that the clock was reset.** The v1.4 status line still reads as
though the condition were running.

## §3 — Current DM-1 state, and what it means for the critical path

**The paper has not been touched since 9 July — twenty days quiet.**
That is *not* a completed stability cycle, for a specific reason: **the
current text is at v1.5 and has never been ratified.** DM-1 v1.5 carries
its own marker, *"NOT YET RE-SHIPPED: panel round pending per the R2
split release."*

> **A stability cycle requires a ratified version to be stable. Twenty
> quiet days on an unratified draft is not a cycle; it is a draft
> nobody has reviewed.**

**Consequence for the 2859 §5 critical path, confirmed rather than
changed:**

- **Item 5 (fresh panel round) is DM-1's actual next action.** Not
  optional, not deferred — the paper's own text says it is pending.
- **Item 6 (fresh stability cycle) cannot begin until item 5
  completes.** Any clock started before the v1.5 ratification is void.
- **v1.4's "OSF on its completion" is stale** and should not be read as
  a live release condition. B7 (Patch 2684) is the governing hold.

## §4 — PROCESS FINDING: the shallow clone produced a false provenance log

The worker's first attempt at §2 used the bootup clone, made with
`--depth 50`. That log reported **exactly one** commit touching DM-1's
`.tex` — Patch 2804, 26 July — which would have supported the opposite
conclusion (clock intact, one recent touch).

**That was an artifact.** Patch 2804 was the shallow boundary commit,
and a shallow boundary appears to introduce every file in the tree. The
four commits of §2 were invisible.

**Registered, and it touches the CLONE-FIRST GATE directly:** the gate
requires cloning before registering an ID, placing a file, or computing
a coefficient. **It does not currently require a clone deep enough to
answer provenance questions**, and a shallow clone silently answers
history questions *wrongly* rather than refusing to answer them. **Any
claim about when a file changed, who changed it, or whether a clock has
run requires `--unshallow` or a full clone first.** The worker caught
this only because the single-commit answer looked implausible.

## §5 — Position

**Retracted:** the DM-1 self-contradiction (§1). No fix required; the
paper is correct as written.

**New, and load-bearing:** v1.4's stability clock is void (§2); DM-1 sits
at an unratified v1.5 (§3); the panel round is confirmed as the next
action on the release path.

**No paper edit is made in this patch.** The only candidate edit — a note
that v1.4's clock was reset — belongs in the v1.5 re-ship notice, which
is the panel round's own work product, not a drive-by amendment to a
shipped notice.

**1B OPEN. Six of seven. B7 holds. 79.5% untouched.**
