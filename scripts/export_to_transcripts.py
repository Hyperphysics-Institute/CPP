#!/usr/bin/env python3
"""
export_to_transcripts.py -- adapter: Claude account data export -> transcript contract.

Reads conversations.json from a Claude data export (Settings > Privacy > Export data),
filters to the conversations you choose, and writes each as a verbatim transcript in the
Capture-and-Audit format contract under Development/transcripts/. The nightly audit + a
fragmentation pass then split them. Non-selected conversations are left out of the repo.

Workflow:
  1) python scripts/export_to_transcripts.py --list
        -> shows all conversations (index, date, msg count, title) so you can pick.
  2) python scripts/export_to_transcripts.py --keep "cpp,dark matter,dm-1,capture,conscious point,lattice"
        -> converts every conversation whose TITLE matches any keyword (case-insensitive),
     and/or:
     python scripts/export_to_transcripts.py --index 0,3,7
        -> converts specific conversations by their --list index.
"""
import json, argparse, re, os, sys

def slugify(name):
    s = re.sub(r'[^A-Za-z0-9._-]+', '-', (name or '').strip().lower()).strip('-')
    return (s or 'untitled')[:50]

def msg_text(m):
    t = (m.get('text') or '').strip()
    if t:
        return t
    parts = []
    for b in (m.get('content') or []):
        if isinstance(b, dict) and b.get('text'):
            parts.append(b['text'])
    return '\n'.join(parts).strip()

def role(m):
    s = (m.get('sender') or m.get('role') or '').lower()
    return 'TLA' if s in ('human', 'user') else 'WORKER'

def load_convos(path):
    with open(path, encoding='utf-8') as fh:
        data = json.load(fh)
    return data if isinstance(data, list) else [data]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--export', default=os.path.expanduser('~/Downloads/claude_export/conversations.json'))
    ap.add_argument('--out', default=os.path.expanduser('~/Documents/GitHub/CPP/Development/transcripts'))
    ap.add_argument('--list', action='store_true', help='list conversations and exit')
    ap.add_argument('--keep', default='', help='comma-separated title keywords to convert')
    ap.add_argument('--index', default='', help='comma-separated --list indices to convert')
    args = ap.parse_args()

    if not os.path.exists(args.export):
        sys.exit(f"export not found: {args.export}\n(point --export at your unzipped conversations.json)")

    convos = load_convos(args.export)
    convos.sort(key=lambda c: c.get('created_at') or '')   # stable index order

    if args.list or (not args.keep and not args.index):
        print(f"{len(convos)} conversations in export:\n")
        for i, c in enumerate(convos):
            n = len(c.get('chat_messages') or [])
            d = (c.get('created_at') or '')[:10]
            print(f"  [{i:2d}]  {d}  {n:5d} msgs  {c.get('name', '(untitled)')}")
        if not args.list:
            print('\nNothing converted. Re-run with --keep "cpp,dark matter,..." or --index 0,3,7')
        return

    sel = set()
    if args.index:
        sel |= {int(x) for x in args.index.split(',') if x.strip().isdigit()}
    kws = [k.strip().lower() for k in args.keep.split(',') if k.strip()]
    if kws:
        for i, c in enumerate(convos):
            if any(k in (c.get('name') or '').lower() for k in kws):
                sel.add(i)

    if not sel:
        print("No conversations matched. Run --list to see titles, then use --index or --keep.")
        return

    os.makedirs(args.out, exist_ok=True)
    written = 0
    for i in sorted(sel):
        c = convos[i]
        msgs = sorted(c.get('chat_messages') or [], key=lambda m: m.get('created_at') or '')
        date = (c.get('created_at') or '0000-00-00')[:10]
        slug = slugify(c.get('name') or f'convo-{i}')
        f = os.path.join(args.out, f"{date}_export_{slug}.md")
        n = 0
        with open(f, 'w', encoding='utf-8', newline='\n') as out:
            out.write('---\n')
            out.write(f"window-slug: {slug}\n")
            out.write("patch: 0\n")
            out.write(f"opened: {c.get('created_at', '')}\n")
            out.write("source: claude-data-export\n")
            out.write("format: structured\n")
            out.write('---\n\n')
            for m in msgs:
                txt = msg_text(m)
                if not txt:
                    continue
                n += 1
                out.write(f"### [{n}] {role(m)}\n{txt}\n\n")
        print(f"wrote  {os.path.basename(f)}  ({n} turns)")
        written += 1
    print(f"\n{written} transcript(s) -> {args.out}")

if __name__ == '__main__':
    main()
