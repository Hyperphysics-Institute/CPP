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

Outstanding: **MemTest86 (never run)** · CMOS battery voltage · BMC System
Event Log via the DM_LAN1 management port · single-stick isolation test ·
front-panel PWR_SW header test.

## Change log

| timestamp | change | campaign legs in flight | notes |
|---|---|---|---|
| 2026-08-17 | BIOS → factory-optimized defaults | none | auto-OC enhancer off |
| | | | |

**Recording rule:** append a row BEFORE making the change where possible, or
immediately after. The β-ladder's duplicate-seed bit-identity gate (§5) is what
makes mid-campaign hardware changes safe — a change that altered arithmetic
would break bit-identity and VOID the campaign rather than silently corrupt it.
