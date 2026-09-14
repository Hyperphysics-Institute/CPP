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
| **DM** (dark matter) | **3500–3599** | **ACTIVE** — opened at 3500; highest used 3512 (12 Sep 2026, OPEN-DM-PAIRING-KINETICS-1: charter 3508, founder answers 3509–3511, transition graph 3510, fork ruling 3511, **residue computation 3512**, **founder reply on the repulsive era / trio 3513**, **edited rendering + spoken-material rule 3514**, **essence 3515**, **crushing-contraction worry answered from the corpus 3516**, **motive-forces reply + thermal-freeze idea 3517**, **exclusion-rule question answered 3518**, **qDP-bond-breakable ruling / thermal residue 3519**, **thermal residue computation, D1 read, C-5 fails 3520**, **asymmetry-is-the-real-issue exchange 3521**, **sequestration picture / bottom-kaon question 3522**, **keyhole: hDP-A/B asymmetry direction 3523**, **sign-chain correction 3524**, **centre is the quark not the pair / dressing-selectivity reading 3525**, **which sign dresses better 3526**, **dressing-selectivity ruling + OPEN-DM-SIGN-SELECTION-1 charter 3527**, **E1 dressing sign computed 3528**, **induced lepton asymmetry rules 3529**, **down-quark composition fork 3530**, **fork resolved + E3 bookkeeping 3531**, **E1 downgraded to OPEN 3532**, **E1 sharpened: case (a) excluded 3533**, **session 227 close 3534**, **deferrals audit 3535**, **all written from an EU-lane window under PD-006** — recorded per the 3426 precedent; next free 3536) | `frontier_sectors/DMDE.md` (DM section) |
| **DE** (dark energy) | **3400–3499** | ACTIVE — in use to 3425 | `frontier_sectors/DMDE.md` (DE section) |
| **GR** (relativity) | **3600–3699** | **EXHAUSTED at 3699** (G-GR-BLOCK-3600, founder, 3 Sep 2026) | `frontier_sectors/GR.md` |
| **GR** (relativity) | **3700–3799** | **ACTIVE** — opened at 3700 (**G-GR-BLOCK-3700**, founder ruling 8 Sep 2026: "3700-3799 series open, I think. If it is, then dedicate to GR lane"); first use Patch 3700 (GR-2 V2.8); `next_id.py` taught the block at Patch 3800 (it had still reported 3600–3699 EXHAUSTED) | `frontier_sectors/GR.md` |
| GR (first block) | 3300–3399 | **CONSUMED** — highest used 3398; 3399 left UNUSED as the block's terminal | `frontier_sectors/GR.md` |
| cosmology (legacy) | 3100–3199 | **CONSUMED** — closed at 3199 | — |
| **EU** (early universe / cosmology) | **3800–3899** | **ACTIVE** — opened at 3800 (**G-EU-BLOCK-3800**, founder ruling 8 Sep 2026: "Please use the 3800 series for EU"); first use Patch 3800 (this registration). The DE (3400s) and DM (3500s) blocks remain active and separate (founder, same ruling). Sector file: EU items live in `research_frontier.md` (OPEN-EU-*) until an `EU.md` sector file is warranted. ****EU BLOCK 3900–3999 ALLOCATED** (founder, 11 Sep 2026) on exhaustion of 3800–3899. Session 226 close (12 Sep, Patch 3940 handover): highest used 3940; next free 3941. **Master handover written at window turnover (D-8); it supersedes every individual handover of Patches 3816–3932.** **D-8 enacted: the §15 close now fires at WINDOW turnover, not per turn — expect far fewer close patches.**
Earlier — Session 208 (11 Sep): highest used 3899; EU BLOCK 3800–3899 EXHAUSTED.
| **CHIR** (substrate chirality arc) | **0900–0999** | **ACTIVE** — lane predates this registry (opened Session 148, Patch 0632; arc theorems 0632–0692, CAPACITY-1 at 0927, flagship scope 0933, magnetism EVAL 0935 on 18 Jun 2026); **entered in the registry at 0936 (13 Sep 2026)**: highest used **0959** (13 Sep 2026: 0959 review-turn economy resolved — final round cut to 2 seats, R-1/R-2 enacted; 0958 three corrections + final round with stop rule; 0957 addendum returns 5/5 + joint corner; 0956 proposal amended + addendum written; 0955 partial returns 3/5 + gap closure, reversal-odd second harmonic found; 0954 CONV-048 reformatted re-dispatch package; 0953 CONV-047 adjudicated — quorum failed 2/5, not enacted, A-domain adopted; 0952 CONV-047 five-slot panel dispatched for the CAPACITY-1 conditionality restatement; 0951 C3 K_lift recompute — clears, all three CAPACITY-1 conditions robust, panel owed; 0950 V3 re-read against the L4-A residual; 0949 L4-A discharged at first harmonic, residual named (Fable); 0948 W⁰ alternating order adopted as structural assignment on founder's choice; 0947 W⁰ ring order narrowed to achiral on the empirics criterion; 0946 founder's W⁰ chirality question answered — P-even vs P-odd, ring-arrangement question raised; 0945 SM-2 charge defect CLOSED — W edits written on the founder's confirmation, zero residuals, OPEN-EW-5 registered; 0944 W ring harmonisation vs the Weak Sector lane; 0943 SM-2 full charge audit — s/b extension on founder ruling, W residual found; 0942 SM-2 composition corrigendum written — cross-lane, SM holds no block; 0941 L4-C discharged; 0940 L4-B discharged; 0939 deferral gate + D-9; 0938 TODO-0937-CHIR registered in `todolist.md`; 0937 OPEN-CHIR-QDP-4STATE-1 RESOLVED, C-W46 flags F1–F3 closed; 0936 cross-lane E1 response, item registered); next free **0960**. Commit subjects in this lane are bare-numbered (`0935 EVAL …`, no `Patch` prefix) and carry `Lane=09xx`; `next_id.py` taught the leading-zero bare-number form at 0936 (it had reported the block empty). Companion band 08xx = DSL/F.1 window (`problem_histories/PH-OPEN-CHIR-1d-beta.md`), not entered here. | `frontier_sectors/CHIR.md` |
| unallocated | 3900–3999 | reserved, unassigned | — |

**DM moved out of 3400–3499 by founder ruling (25 Aug 2026).** The DM and
DE lanes had shared a block and a pointer line while running in parallel
windows; on 25 Aug the DM window consumed 3424 and 3425 while `DMDE.md`'s
`Next patch (DM/DE)` pointer had named 3424 for the DM/DE sequence. No
content was lost, but the two lanes were writing into one number space
with one pointer, which cannot be made safe by care alone.

## Rules

1. **One block per lane. Never claim outside your block**, even if the
   number looks free.
2. **Run `next_id.py` before claiming — against freshly-fetched origin**
   (`git fetch origin && git reset --hard origin/main` first). Grepping by
   eye misses IDs that appear only in a sector file or only in a commit
   body, and the gate run against a stale clone validates against a stale
   number space (this is how 3426 happened — see Anomalies).
3. **A pointer line is a reservation, not a suggestion.** If a sector
   file says `Next patch (X): NNNN`, that ID belongs to lane X even if no
   commit has used it yet.
4. **Each lane advances only its own pointer.** Do not edit another
   lane's `Next patch` line, even while updating a shared file.
5. **When a block is exhausted**, record it here as CONSUMED and open the
   next block by founder ruling, not unilaterally.
6. **A block-opening patch updates `code/next_id.py`'s `BLOCKS` table in
   the same commit** (added Patch 3807). Between 3700 and 3800 the gate
   lagged this registry by one block and reported GR 3600–3699 EXHAUSTED
   on a fresh clone; a gate that disagrees with the registry is worse
   than no gate, because it is trusted.

## The frontier-write rule (why nothing has been lost so far)

`research_frontier.md` is appended by **prepending a new
`**Last updated:**` line above the existing one and prefixing the old one
with `Earlier `**. Every correct patch shows exactly `2 insertions,
1 deletion` on that file. **Never rewrite the file wholesale, and never
edit an existing header line.** If a diff on `research_frontier.md` shows
more than one deleted line, the write is wrong — stop and re-derive it.
Verified across 3189–3199: all show 2/1.

## Anomalies (recorded, not precedents)

- **3426 — DM-lane content in DE's block.** Founder registration
  (ring 16-planes convention + memoryless-substrate/KE statement,
  `founders_voice/`). Claimed 25–26 Aug by a DM-lane window whose clone
  predated the Patch 3500 lane split, under the pre-split "cosmology
  3400–3499" guidance; verified free by grep against that stale clone.
  No collision resulted; DE's sequence continues past it. Stays where it
  is — renumbering pushed history is forbidden. Registered so block
  audits don't read it as a live collision. (Patch 3503.)
