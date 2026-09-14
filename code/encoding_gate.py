#!/usr/bin/env python3
"""encoding_gate.py -- refuse a patch that introduces invalid UTF-8 into a text file.

WHY THIS EXISTS. At Patch 4013 a heredoc mangled "E₈" into the bytes  E 0x82 0x88  --
the ASCII 'E' followed by the tail of U+2088 with its lead byte lost. The result was
invisible in every rendered view and in `git show`. Nothing caught it. It surfaced only
because code/deferral_gate.py CRASHED with UnicodeDecodeError while reading the diff.

Two lessons, both mechanized here rather than written down:
  1. A gate that crashes on bad input is a gate that is not run. deferral_gate.py now
     decodes with errors="replace" and this gate reports the corruption instead.
  2. The crash was the ONLY signal. Silent mojibake in a corpus is the worst class of
     error -- it does not fail, it does not render wrong enough to notice, and it
     survives every review. The same sweep found a SECOND, older instance
     ("Eötvös" -> E\\xb6tv\\xc3\\xb6s) that had been sitting in a DM-lane file unnoticed.

Binary files are skipped by extension. Anything text-like must decode as UTF-8.

USAGE:  python3 code/encoding_gate.py [--all | <commit-ish>]     (default HEAD)
EXIT:   0 pass, 1 invalid UTF-8 in a text file.
"""
import os, subprocess, sys

BINARY = {".pdf",".png",".jpg",".jpeg",".gif",".gz",".zip",".pkl",".lnk",".ico",
          ".woff",".woff2",".ttf",".eot",".xlsx",".docx",".pptx",".npy",".npz"}

def is_text(p): return os.path.splitext(p)[1].lower() not in BINARY

def check(paths):
    bad=[]
    for f in paths:
        if not (os.path.isfile(f) and is_text(f)): continue
        b=open(f,"rb").read()
        try: b.decode("utf-8")
        except UnicodeDecodeError as e:
            ctx=b[max(0,e.start-45):e.start+15]
            bad.append((f,e.start,repr(ctx)))
    return bad

def main():
    arg = sys.argv[1] if len(sys.argv)>1 else "HEAD"
    if arg=="--all":
        out=subprocess.run(["git","ls-files","-z"],capture_output=True).stdout
        paths=[p for p in out.decode("utf-8","replace").split("\0") if p]
        scope="every tracked file"
    else:
        paths=subprocess.run(["git","show","--name-only","--format=",arg],
                             capture_output=True,text=True,errors="replace").stdout.split("\n")
        paths=[p for p in paths if p.strip()]
        scope=f"files touched by {arg}"
    bad=check(paths)
    print(f"encoding_gate: {scope} — {len(paths)} path(s) considered, "
          f"{len(bad)} with invalid UTF-8")
    for f,pos,ctx in bad:
        print(f"  {f} @ byte {pos}\n    {ctx}")
    if bad:
        print("\nFAIL — invalid UTF-8 in a text file. This does not render wrong enough to")
        print("notice and survives review; repair the bytes, do not reword around them.")
        return 1
    print("PASS")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
