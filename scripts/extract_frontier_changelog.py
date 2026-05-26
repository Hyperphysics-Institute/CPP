#!/usr/bin/env python3
"""
extract_frontier_changelog.py

Surgical fix for research_frontier.md's two enormous "Last updated:" lines
(lines 4 and 6, ~590KB and ~496KB) that survived the 25 May 2026 master
decomposition because line-count was the proxy, not byte-count.

Behavior:
  - Backs up research_frontier.md as research_frontier.md.pre-changelog-extraction.bak
  - Extracts line 4 as ONE block to session_logs/2026-05-24_session_142_extracted_from_frontier.md
    (line 4 lacks "Earlier Session NN" markers, so we don't split it; further
    decomposition is a TODO)
  - Extracts line 6 SPLIT on "Earlier N Month 2026 Session NN" markers into N+1
    dated session_logs/ files (head + N markers = N+1 files)
  - Replaces lines 4 and 6 in research_frontier.md with one-line pointers
  - Reports before/after sizes

Run from CPP repo root:
    python3 scripts/extract_frontier_changelog.py

Or, if python3 is not on PATH on Windows Git Bash:
    python scripts/extract_frontier_changelog.py
"""

import re
import sys
import shutil
from pathlib import Path

SOURCE = Path("research_frontier.md")
BACKUP = Path("research_frontier.md.pre-changelog-extraction.bak")
SESSION_LOGS = Path("session_logs")

MONTH_NUM = {
    "January": "01", "February": "02", "March": "03", "April": "04",
    "May": "05", "June": "06", "July": "07", "August": "08",
    "September": "09", "October": "10", "November": "11", "December": "12",
}

# ---- Preflight ----------------------------------------------------------

if not SOURCE.exists():
    sys.exit(f"ERROR: {SOURCE} not found in current directory. Run from CPP repo root.")

if not SESSION_LOGS.exists():
    sys.exit(f"ERROR: {SESSION_LOGS}/ not found. Expected existing session_logs directory.")

if BACKUP.exists():
    sys.exit(
        f"ERROR: {BACKUP} already exists. Either:\n"
        f"  - This script has already run: rm {BACKUP} to confirm and re-run if needed\n"
        f"  - Or move {BACKUP} aside before proceeding"
    )

with SOURCE.open("r", encoding="utf-8") as f:
    lines = f.readlines()

if len(lines) < 6:
    sys.exit(f"ERROR: {SOURCE} has only {len(lines)} lines, expected ~280.")

line4 = lines[3].rstrip("\n")
line6 = lines[5].rstrip("\n")

if len(line4) < 100_000:
    sys.exit(
        f"ERROR: line 4 is only {len(line4):,} chars, expected ~590,000.\n"
        f"  File may already have been processed, or structure has drifted."
    )

if len(line6) < 100_000:
    sys.exit(
        f"ERROR: line 6 is only {len(line6):,} chars, expected ~496,000.\n"
        f"  File may already have been processed, or structure has drifted."
    )

original_size = SOURCE.stat().st_size

# ---- Backup -------------------------------------------------------------

shutil.copy(SOURCE, BACKUP)

# ---- Parse line 4 header ------------------------------------------------

head4_match = re.match(
    r"\*\*Last updated:\*\* (\d+) ([A-Z][a-z]+) 2026 \(Session (\d+)",
    line4,
)
if not head4_match:
    sys.exit(f"ERROR: could not parse line 4 head. First 200 chars: {line4[:200]}")

day4, month4, sess4 = head4_match.group(1), head4_match.group(2), head4_match.group(3)
month4_num = MONTH_NUM[month4]
line4_filename = SESSION_LOGS / (
    f"2026-{month4_num}-{day4.zfill(2)}_session_{sess4.zfill(3)}_extracted_from_frontier.md"
)

# ---- Write line 4 as one block ------------------------------------------

with line4_filename.open("w", encoding="utf-8") as f:
    f.write(f"# Session {sess4} ({day4} {month4} 2026) — extracted from research_frontier.md line 4\n\n")
    f.write(f"<!-- Extracted on 25 May 2026 during research_frontier.md changelog decomposition.\n")
    f.write(f"     Original content was a single 590KB unbroken line in research_frontier.md\n")
    f.write(f"     that survived the master decomposition (line-count was the proxy, not byte-count).\n")
    f.write(f"     This file may contain multiple sessions of activity prepended as a running\n")
    f.write(f"     update log; internal structure differs from line 6 (no 'Earlier Session NN'\n")
    f.write(f"     boundary markers found by initial regex). Further decomposition into per-session\n")
    f.write(f"     files is registered as a TODO in todolist.md. -->\n\n")
    f.write(line4 + "\n")

# ---- Parse line 6 head + markers ----------------------------------------

head6_match = re.match(
    r"\*\*Last updated:\*\* (\d+) ([A-Z][a-z]+) 2026 \(Session (\d+)",
    line6,
)
if not head6_match:
    sys.exit(f"ERROR: could not parse line 6 head. First 200 chars: {line6[:200]}")

head6_day, head6_month, head6_sess = head6_match.group(1), head6_match.group(2), head6_match.group(3)
head6_month_num = MONTH_NUM[head6_month]

# Find all "Earlier" boundary markers in line 6
marker_pattern = re.compile(r"Earlier (\d+) ([A-Z][a-z]+) 2026 Session (\d+)")
earlier_markers = list(marker_pattern.finditer(line6))

if len(earlier_markers) == 0:
    sys.exit("ERROR: expected at least one 'Earlier Session' marker in line 6, found none.")

# Build segment list: (start_byte, day, month, session, label_for_first_segment)
# First segment is from byte 0 (head) to the first Earlier marker
segments = []
segments.append((0, head6_day, head6_month, head6_sess, "head"))
for m in earlier_markers:
    segments.append((m.start(), m.group(1), m.group(2), m.group(3), "earlier"))

# Slice each segment
line6_extracted_count = 0
for i, seg in enumerate(segments):
    start_offset = seg[0]
    end_offset = segments[i + 1][0] if i + 1 < len(segments) else len(line6)
    day, month, sess = seg[1], seg[2], seg[3]
    seg_kind = seg[4]
    block = line6[start_offset:end_offset]

    month_num = MONTH_NUM[month]
    filename = SESSION_LOGS / (
        f"2026-{month_num}-{day.zfill(2)}_session_{sess.zfill(3)}_extracted_from_frontier.md"
    )

    if filename.exists():
        sys.exit(f"ERROR: target file already exists, refusing to overwrite: {filename}")

    with filename.open("w", encoding="utf-8") as f:
        f.write(f"# Session {sess} ({day} {month} 2026) — extracted from research_frontier.md line 6\n\n")
        f.write(f"<!-- Extracted on 25 May 2026 from line 6 of research_frontier.md during\n")
        f.write(f"     changelog decomposition. Line 6 was a 496KB unbroken line holding {len(segments)}\n")
        f.write(f"     sessions of running update log. This segment is {'the head' if seg_kind == 'head' else 'an Earlier-marked block'}\n")
        f.write(f"     ({len(block):,} chars). -->\n\n")
        f.write(block.strip() + "\n")

    line6_extracted_count += 1

# ---- Build pointer replacement lines ------------------------------------

# Line 4 pointer
new_line4 = (
    f"**Last updated:** {day4} {month4} 2026 (Session {sess4}, F.1 / SS-9 / Capotauro thread). "
    f"Prior session-by-session running-update log extracted to "
    f"[`{line4_filename.as_posix()}`]({line4_filename.as_posix()}) "
    f"on 25 May 2026 (changelog decomposition).\n"
)

# Line 6 pointer
new_line6 = (
    f"**Last updated:** {head6_day} {head6_month} 2026 (Session {head6_sess}, "
    f"OPEN-SS-35 / SS-9 closure-programme thread). "
    f"Prior session-by-session running-update log ({line6_extracted_count} sessions, "
    f"head Session {head6_sess} plus {len(earlier_markers)} Earlier-marked blocks) extracted "
    f"to dated `session_logs/2026-05-*_session_*_extracted_from_frontier.md` files on 25 May 2026.\n"
)

# ---- Rewrite research_frontier.md ---------------------------------------

lines[3] = new_line4
lines[5] = new_line6

with SOURCE.open("w", encoding="utf-8") as f:
    f.writelines(lines)

new_size = SOURCE.stat().st_size

# ---- Report -------------------------------------------------------------

print("Extraction complete.")
print()
print(f"  Line 4 ({len(line4):>9,} bytes) -> 1 file:")
print(f"      {line4_filename}")
print()
print(f"  Line 6 ({len(line6):>9,} bytes) -> {line6_extracted_count} files in {SESSION_LOGS}/:")
for seg in segments:
    fn = SESSION_LOGS / f"2026-{MONTH_NUM[seg[2]]}-{seg[1].zfill(2)}_session_{seg[3].zfill(3)}_extracted_from_frontier.md"
    print(f"      {fn}")
print()
print(f"  research_frontier.md size:")
print(f"      before: {original_size:>10,} bytes")
print(f"      after:  {new_size:>10,} bytes")
print(f"      ratio:  {new_size * 100 // original_size}% of original")
print()
print(f"  Backup: {BACKUP}")
print()
print("Next steps:")
print("  1. git status                    (review what changed)")
print("  2. ls session_logs/2026-05-*_extracted_from_frontier.md")
print("  3. Inspect a few extracted files to verify content")
print("  4. git add session_logs/ research_frontier.md && git commit && git push")
print("  5. After confirmation, rm research_frontier.md.pre-changelog-extraction.bak")
