#!/usr/bin/env python3
"""next_id.py — the mechanical CLONE-FIRST GATE check for patch IDs.

Established Patch 3500 after DM and DE both wrote into 3400-3499.

    python code/next_id.py dm            # next free DM id
    python code/next_id.py de --check 3424   # is 3424 free for DE?
    python code/next_id.py --all         # block occupancy summary

Greps EVERY place an ID can hide, because grepping by eye has missed
three collisions in this programme:
  1. git log --all  (commit subjects AND bodies; a patch can be
     mentioned in another patch's message before it is written)
  2. research_frontier.md
  3. frontier_sectors/*.md          <- where 3424 was reserved and missed
  4. handovers/*.md                 <- "Next patch" pointers live here too

A "Next patch (X): NNNN" pointer counts as TAKEN. A pointer is a
reservation, not a suggestion (id_block_registry.md rule 3).
"""
import argparse, glob, os, re, subprocess, sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, '..'))

BLOCKS = {                       # keep in sync with id_block_registry.md
    'dm': (3500, 3599),
    'de': (3400, 3499),
    'gr': (3300, 3399),
    'legacy-cosmology': (3100, 3199),
}


def _texts():
    out = []
    # Patch 3501: decode git output as UTF-8 EXPLICITLY. Without this,
    # Python on Windows decodes subprocess output with the locale codec
    # (cp1252), and this corpus's commit messages are full of non-cp1252
    # characters (beta, arrows, em-dashes). The reader thread then dies,
    # .stdout comes back None, and the gate crashes on the one machine
    # that matters. Second occurrence of this defect class -- the first
    # was --analyze crashing under redirection, fixed at 3175. errors=
    # 'replace' because a mangled character must never stop the check:
    # an unreadable byte is not a reason to leave an ID unverified.
    try:
        r = subprocess.run(
            ['git', '-C', ROOT, 'log', '--all', '--format=%s%n%b'],
            capture_output=True, timeout=120)
        out.append((r.stdout or b'').decode('utf-8', errors='replace'))
    except Exception as e:
        print(f"WARNING: could not read git log ({e}); "
              f"result is NOT authoritative.", file=sys.stderr)
    for pat in ('research_frontier.md', 'frontier_sectors/*.md',
                'handovers/*.md', 'id_block_registry.md'):
        for f in glob.glob(os.path.join(ROOT, pat)):
            try:
                out.append(open(f, encoding='utf-8', errors='replace').read())
            except OSError:
                pass
    return '\n'.join(t for t in out if isinstance(t, str))


def taken(lo, hi, blob):
    """An id counts as taken if it appears as 'Patch NNNN', as a
    'Next patch...: NNNN' reservation, or as a reasoning/<NNNN>.md path."""
    hits = set()
    for m in re.finditer(r'Patch(?:es)?\s+(\d{4})', blob):
        hits.add(int(m.group(1)))
    for m in re.finditer(r'Next patch[^:\n]*:\s*(\d{4})', blob):
        hits.add(int(m.group(1)))
    for m in re.finditer(r'reasoning/(\d{4})\.md', blob):
        hits.add(int(m.group(1)))
    return sorted(i for i in hits if lo <= i <= hi)


def recommend(lo, hi, t):
    """Recommend HIGHEST-USED + 1, never a gap in the middle of a used
    range. Gaps exist (renumberings, abandoned drafts) but claiming one
    makes the history read as though a patch were inserted into the past,
    and a gap is often a reservation whose pointer we failed to parse.
    Always move forward."""
    if not t:
        return lo
    nxt = t[-1] + 1
    return nxt if nxt <= hi else None


def gaps(lo, hi, t):
    return [i for i in range(lo, (t[-1] if t else lo)) if i not in t]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('lane', nargs='?', help=' | '.join(BLOCKS))
    ap.add_argument('--check', type=int, help='is this specific id free?')
    ap.add_argument('--all', action='store_true')
    a = ap.parse_args()
    blob = _texts()

    if a.all or not a.lane:
        print(f"{'lane':<20}{'block':<14}{'used':>6}{'next free':>11}")
        for name, (lo, hi) in BLOCKS.items():
            t = taken(lo, hi, blob)
            nxt = recommend(lo, hi, t)
            print(f"{name:<20}{f'{lo}-{hi}':<14}{len(t):>6}"
                  f"{(nxt if nxt else 'EXHAUSTED'):>11}")
        print("\nSee id_block_registry.md. Never claim outside your block.")
        return

    lane = a.lane.lower()
    if lane not in BLOCKS:
        sys.exit(f"unknown lane {lane!r}; known: {', '.join(BLOCKS)}")
    lo, hi = BLOCKS[lane]
    t = taken(lo, hi, blob)

    if a.check is not None:
        if not (lo <= a.check <= hi):
            sys.exit(f"*** {a.check} IS OUTSIDE the {lane} block "
                     f"({lo}-{hi}). Do not claim it. ***")
        if a.check in t:
            sys.exit(f"*** {a.check} IS TAKEN (or reserved by a "
                     f"'Next patch' pointer). Do not claim it. ***")
        print(f"{a.check} is FREE for {lane}.")
        return

    nxt = recommend(lo, hi, t)
    if nxt is None:
        sys.exit(f"*** {lane} block {lo}-{hi} is EXHAUSTED. Opening a new "
                 f"block is a founder ruling, not a unilateral choice. ***")
    print(f"lane {lane}  block {lo}-{hi}  used {len(t)}  "
          f"NEXT FREE: {nxt}")
    if t:
        print(f"  highest used: {t[-1]}")
        g = gaps(lo, hi, t)
        if g:
            print(f"  unused gaps (do NOT claim; may be unparsed "
                  f"reservations): {g[:12]}{' ...' if len(g) > 12 else ''}")


if __name__ == '__main__':
    main()
