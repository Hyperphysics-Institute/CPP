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


## H-CORETEMP **REFUTED** — and the fault is LOAD-INDEPENDENT (25 Aug 2026)

**The hypothesis is dead in its strong form.** Kila6 rebooted uncleanly
on 25 Aug at 11:41:28 with **Core Temp not installed and not running**,
after two consecutive multi-day campaigns without it. The ring-0 driver
mechanism was sound as a mechanism and wrong as the explanation. Recorded
as a worker error: it accounted for the missing crash evidence too neatly,
and that elegance was given more weight than it had earned.

**LOAD-INDEPENDENCE — the new, load-bearing finding.** File mtimes place
the last Phase 1B leg at **10:11:24**; the crash was **11:41:28**. The
campaign had finished and Python had exited **90 minutes earlier**. The
machine died **at idle**, after ~75 h at 100% on 32 threads.

Consequence: explanations requiring current draw, thermal stress, or
transient load demand are **eliminated or badly damaged** — VRM stress
under load, PSU sag under load, inadequate cooling. Whatever this is does
not care what the CPU is doing. (Note the earlier reading was backwards:
the clean long runs were taken as evidence that load was safe, when the
machine simply spends most wall-clock time idle.)

### Event history (Windows System log, Ids 41 / 6008 / 1001)

| Date | Events | Note |
|---|---|---|
| 17 Aug | 4 (07:22, 12:43, ~13:29, 17:29) | pre-BIOS-reset rate: hours |
| 18 Aug | 1 (20:56) | |
| 19–24 Aug | **0** | ~135 h near-continuous 100% load, 2 campaigns |
| 25 Aug | 1 (11:41:28) | **at idle**, 90 min after load ended |

**ZERO Event 1001 across all eight events.** Every one is a bare 41/6008
pair — no bugcheck, no minidump, no software crash path entered. Windows
never got the chance to record anything: the signature of power being cut,
not of an OS or driver fault. This survives H-CORETEMP's death.

**The BIOS factory-default reset (17 Aug) did not cure the fault but
changed its rate by ~2 orders of magnitude** — from every few hours to
roughly weekly. Real effect; not a fix. Recorded as such.

**Discounted, deliberately:** the 6008 seconds fields cluster (:27, :27,
:28, :29). This is an artifact — 6008 reports Windows' last periodic
"alive" write, quantized near one-minute intervals, not the true crash
instant. Noted so a later reader does not mistake it for a signature.

## H-USB-RAIL: a second symptom on a different subsystem (25 Aug 2026)

**Founder observation:** a Bluetooth dongle repeatedly stops working and
does not recover; moving it between **front-panel and rear-panel** USB
ports does not fix it — it fails again by next use.

Failure across **both** front and rear ports exonerates any single port
and most likely the dongle. What front and rear share is the USB
controller and the **+5V / +5VSB rails**.

**Why this matters for the shutdown fault:** two independent faults would
be a coincidence; **one upstream power-delivery problem producing both is
simpler**, and it fits a load-independent, instant, logless shutdown. This
**raises PSU / power-rail health above the front-panel PWR_SW header** in
the suspect ordering — a marginal power switch would not affect USB at all.

### Suspect list, re-ranked on the 25 Aug evidence

1. **PSU or power-rail fault** (raised) — explains both symptoms; consistent
   with load-independence and with the absent bugcheck.
2. **Front-panel PWR_SW header** (still live, now second) — explains the
   shutdowns but not the USB symptom. **Free test:** unplug PWR_SW from
   the board entirely, start by briefly bridging the pins with a
   screwdriver; if shutdowns stop over a week, it is the switch.
3. **CMOS battery voltage** — unmeasured.

### Owed diagnostics (none yet performed)

- **BMC System Event Log via the DM_LAN1 management port.** Now the
  highest-value read on the list: the BMC runs on its own power rail and
  records **rail voltage faults, power-good failures and thermal trips
  the host can never log.** Outstanding since Patch 3173, still unread.
- +5V / +5VSB readings in BIOS or via the BMC.
- Whether the dongle fails specifically during idle/sleep periods
  (matching the crash timing).
