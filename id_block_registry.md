# PATCH-ID BLOCK REGISTRY

**Canonical source of truth for which lane owns which patch numbers.**
Established Patch 3500, 25 August 2026, by founder ruling after DM and
DE both wrote into 3400–3499 on the same day.

**Before claiming any patch ID, run:**

```
python code/next_id.py <lane>
```

It greps the full git log, `research_frontier.md`, and every
`frontier_sectors/*.md` for the block's IDs and prints the next free one.
It is not advisory. A collision has bitten this programme three times
(3168/3169 renumbered; 3175 taken while a pointer named 3344; 3424/3425
consumed while `DMDE.md` had reserved 3424 for DM/DE).

---

## Block ownership

| Lane | Block | Status | Sector file |
|---|---|---|---|
| **DM** (dark matter) | **3500–3599** | **ACTIVE** — opened at 3500 | `frontier_sectors/DMDE.md` (DM section) |
| **DE** (dark energy) | **3400–3499** | ACTIVE — in use to 3425 | `frontier_sectors/DMDE.md` (DE section) |
| **GR** (relativity) | 3300–3399 | ACTIVE — in use to ~3347 | `frontier_sectors/GR.md` |
| cosmology (legacy) | 3100–3199 | **CONSUMED** — closed at 3199 | — |
| unallocated | 3600–3999 | reserved, unassigned | — |

**DM moved out of 3400–3499 by founder ruling (25 Aug 2026).** The DM and
DE lanes had shared a block and a pointer line while running in parallel
windows; on 25 Aug the DM window consumed 3424 and 3425 while `DMDE.md`'s
`Next patch (DM/DE)` pointer had named 3424 for the DM/DE sequence. No
content was lost, but the two lanes were writing into one number space
with one pointer, which cannot be made safe by care alone.

## Rules

1. **One block per lane. Never claim outside your block**, even if the
   number looks free.
2. **Run `next_id.py` before claiming.** Grepping by eye misses IDs that
   appear only in a sector file or only in a commit body.
3. **A pointer line is a reservation, not a suggestion.** If a sector
   file says `Next patch (X): NNNN`, that ID belongs to lane X even if no
   commit has used it yet.
4. **Each lane advances only its own pointer.** Do not edit another
   lane's `Next patch` line, even while updating a shared file.
5. **When a block is exhausted**, record it here as CONSUMED and open the
   next block by founder ruling, not unilaterally.

## The frontier-write rule (why nothing has been lost so far)

`research_frontier.md` is appended by **prepending a new
`**Last updated:**` line above the existing one and prefixing the old one
with `Earlier `**. Every correct patch shows exactly `2 insertions,
1 deletion` on that file. **Never rewrite the file wholesale, and never
edit an existing header line.** If a diff on `research_frontier.md` shows
more than one deleted line, the write is wrong — stop and re-derive it.
Verified across 3189–3199: all show 2/1.
