# Session 238 — Boot Card (23 Sep 2026, Patch 4257, EW lane → strong)

**Kickoff line (paste into a fresh window, verbatim):**
```
Bootup for Conscious Point Physics (CPP). Clone the repo and read the bootup file at https://raw.githubusercontent.com/Hyperphysics-Institute/CPP/main/bootup.md. Honor the line-1 CLONE-FIRST GATE before registering any ID, placing any file, or computing any coefficient (clone the repo and grep the registry first). Then open the handovers/ folder, sort by filename, and read the most recent dated file (named YYYY-MM-DD_session_NNN_*.md) — that newest entry is the canonical "what's next" pointer. Note: the folder is handovers/ (plural) and there is no file named handover.md; never look for either — always use the newest dated entry.
```

**Orientation (paste with the kickoff line).** Single window on the EW lane, block 4200–4299; no parallel windows active, no anti-collision run needed. The lane's state: g_A = 1.406 with zero parameters from the founder's breathing-core picture (4244), the neutral-current integers from a capacity-one centroid plus fermion exchange with both premises founder-ruled (4246, 4248, 4253), the bracelet at a working radius of 0.346 fm (4251), and the Session-237 critic queue empty. The one most important next action is the g_A residual (TODO-4234-DELTA): three untried levers, a precise target of ~20% more momentum spread per mode. Boot under the two-step protocol below; report at STEP 1 and stop.

**READ THIS FIRST. Do not read the detail file until the two-step boot is done.**

## Two-step boot (unchanged from 4237)
**STEP 1 (this window, no work):** clone (full history, no `--depth`), run `python3 code/next_id.py EW`, run the four gates, report HEAD, next free ID, suite status, and the recommended task below. **STOP** and wait for the founder's reply.
**STEP 2 (after the reply):** read `handovers/detail/2026-09-23_session_238_p4257_ew_arc_4240_4256.md`, then work.

## Facts
- **HEAD:** 4257 (Session 238 close). **Next free: EW 4258** (block 4200–4299; continuity_gate now watches it, 4241).
- **Checksum facts:** g_A = 1.406 from the breathing core, zero parameters (4244; measured 1.2754); μ_p = 2.772, μ_n = −1.829. OPEN-EW-NC route (a) complete as a mechanism, not closed (4254). Bracelet radius 0.346 fm, working (4251). TODO-4214-ONESIGN 7/7, item 2 passes in magnitude (4249). SF-2 v1.08; v1.09 owed.
- **Rulings this session (all provisional, in `founders_voice/`):** G-EW-CENTROIDTRAP-4248, G-EW-BRACELETSCALE-4251 (worker, delegated), G-EW-NCMIX-4253, G-EW-W0CHANCE-4256. Candidate: CAND-EW-4DOVERLAP-4255.

## Recommended task (in order)
1. **TODO-4234-DELTA residual** — g_A needs ~20% more momentum spread per mode than the Compton ground state; untried: Dirac-oscillator spin–orbit, the d's internal linear oscillator, excited-mode admixture. Compute, do not attribute.
2. **TODO-4251-LIFETIME** — the Sea's universal bracelet-presence rate (one number; lepton universality says host-independent); test CAND-EW-4DOVERLAP-4255 against it.
3. **SF-2 v1.09** — items (i)–(v) in `development-SF-2.md`'s Session-238 vignette; the founder recompiles.
4. Critic (next window): the exchange-antisymmetry-on-a-push-weight step (4254 R1 vs R2).

## Founder owes
23 PDF recompiles (SF-2 v1.08 among them); cage lines u, d, c, b, t (TODO-4212-CAGETABLE). No physics question outstanding.

## Process reminders
- **D-5:** never `reset --hard origin/main` mid-session; origin can lag the founder's "applied" (4256 lost and rebuilt 4255 this way).
- **D-10:** grep `founders_voice/` for the object's name before asking the founder about it (4240 miss).
