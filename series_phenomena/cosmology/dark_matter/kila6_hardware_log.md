# KILA6 HARDWARE LOG

Required by `beta_ladder_prereg.md` §6. Every hardware or firmware change to
Kila6 during a running campaign is logged here with its timestamp, so any
post-hoc question about which legs ran on which configuration is answerable.

**Machine:** ASUS Pro WS W680-ACE IPMI · assembled Aug 2026 · parts purchased
Jun 2026 · 32 logical cores · 850 W PSU · KLEVV CRAS V DDR5 64 GB (2×32 GB,
KD5BGUA80-64A320G, non-ECC, rated 6400 CL32) in slots A2/B2 · XMP NEVER
ENABLED (modules run at JEDEC baseline).

## Open fault (unresolved as of 17 Aug 2026)

Eight unclean shutdowns in ~48 h, at idle and under load alike. **No WHEA
events, no minidumps, no bugcheck codes** across all eight — consistent with
power loss rather than an OS crash. BIOS reset to factory-optimized defaults
did not resolve it. Auto-overclock enhancer disabled earlier extended clean
uptime from ~8 h to ~36 h but did not eliminate the fault.

Ruled out: AsIO.sys (no such service registered); RAM slot placement (A2/B2 is
correct); XMP instability (never enabled); PSU capacity (850 W against ~300 W
draw); standoff short (founder verified); USB overcurrent (BT dongle draw is
~50–100 mA, and the M525 2.4 GHz dongle in the same host is reliable — the BT
enumeration failures are most likely a consequence of unclean shutdowns, not a
cause).

Outstanding: CMOS battery voltage · BMC System Event Log via the DM_LAN1
management port · front-panel PWR_SW header test. (Single-stick isolation
test: no longer indicated — memory tested clean, below.)

## MemTest86 result (18 Aug 2026)

**PASSED — 4 complete passes, 0 errors** (founder-reported; no screenshot
retained). Consequences:

1. **The β-ladder prereg §5.4 acceptance condition is SATISFIED.** The
   campaign, when run, is NOT provisional — no downstream label required.
2. **RAM is ruled out as a silent-corruption source.** The Route C
   integrity sweep's known gap (files verified to parse and pair, but
   arithmetic unverifiable) is now closed on the memory side for future
   campaigns; the duplicate-seed bit-identity gate (§5.1–5.3) remains in
   force as the in-campaign arithmetic check.
3. **Diagnostic bonus for the shutdown fault:** the machine survived the
   full multi-hour test (4 passes on 64 GB) with no spontaneous reboot,
   running outside Windows with no drivers loaded. Combined with the
   zero-WHEA / zero-minidump signature, the fault profile continues to
   point at power delivery or front-panel/PSU hardware, not memory, not
   the OS. The remaining outstanding checks above are the live suspects.

## Change log

| timestamp | change | campaign legs in flight | notes |
|---|---|---|---|
| 2026-08-17 | BIOS → factory-optimized defaults | none | auto-OC enhancer off |
| 2026-08-18 | MemTest86 free edition, USB boot — 4 passes, 0 errors | none | prereg §5.4 acceptance SATISFIED; no spontaneous reboot during the test |
| 2026-08-18→21 | β-ladder campaign: ~60 h at 100% on all 32 threads | 1024 legs | ZERO unclean shutdowns; **Core Temp NOT running** |
| | | | |

**Recording rule:** append a row BEFORE making the change where possible, or
immediately after. The β-ladder's duplicate-seed bit-identity gate (§5) is what
makes mid-campaign hardware changes safe — a change that altered arithmetic
would break bit-identity and VOID the campaign rather than silently corrupt it.


## H-CORETEMP: the leading suspect for the shutdown fault (21 Aug 2026)

**Founder observation, which prompted this entry:** every crashing period
had Core Temp running; the uninterrupted 60-hour β-ladder campaign did
not.

**Why it fits the signature.** Core Temp reads CPU MSRs through a
ring-0 kernel driver (ALSysIO64.sys class). A fault at that privilege
level can halt the machine below the layer that records bugchecks —
producing exactly this fault's otherwise-baffling profile: **no WHEA
events, no minidumps, no bugcheck codes across all eight events**, which
had been read as "consistent with power loss." A ring-0 driver fault is
indistinguishable from power loss from the outside. It also explains
crashes at idle AND under load alike (a polling driver runs the same
either way) and why BIOS factory defaults did not resolve it.

**Evidence for:** 60 h continuous at 100% on 32 threads — a harsher
thermal and electrical stress, sustained longer, than any crashing
period — with zero events and Core Temp absent.

**CONFOUND, stated plainly so this is not later read as settled:** the
auto-overclock enhancer was disabled earlier (which had already extended
uptime ~8 h → ~36 h). Two changes overlap. H-CORETEMP is the LEADING
hypothesis, not a demonstrated cause; the overclock enhancer remains an
unexcluded partial contributor.

**Test:** keep Core Temp uninstalled through the next multi-day campaign.
Two independent clean long runs would make the case. For temperature
monitoring without a third-party ring-0 driver on this board: the BIOS
hardware monitor, or the ASUS BMC/IPMI via DM_LAN1 (out-of-band, no OS
driver at all). HWiNFO64 is better-behaved than Core Temp but uses the
same mechanism class and is not risk-free.

**Status of the older reading:** the "power delivery" localization
recorded at Patch 3173 is DEMOTED, not retired — CMOS battery voltage,
the BMC event log, and the front-panel PWR_SW header remain unchecked and
still explain a no-minidump shutdown equally well.
