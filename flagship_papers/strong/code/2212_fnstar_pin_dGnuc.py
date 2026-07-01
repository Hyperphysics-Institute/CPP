#!/usr/bin/env python3
"""
OPEN-SS-41a (patch 2212, strong/geometry lane): pin (f, n*) -> dG*_nuc = (n*-1)*|ln f|*kT_form.
================================================================================================
Executes the 2211 handover: derive f (exposed-core spine-face fraction) and n* (critical nucleus) to turn the
2209 dG*_nuc bracket into a pinned number. Win 6.0-6.9 kT_form; kill <~4 (under-cored) or >~9 (over-cored).

RESULT (honest, partial close): n* ~ 2-4 IS pinnable (0863: cross forms 'within a few moiety additions', hTetra
chaperone barrierless; + cooperative-stability of the soft-hinge axial seed). But f is NOT pinnable from the current
corpus: f = (exposed-core spine-face solid angle)/4pi needs the DM element cross-section SHAPE (8qCP core polyhedron,
eCP-coat corner coverage, which face presents the axial E_qq spine), which the corpus gives only qualitatively. The
window needs f ~ 0.04-0.11 (pinned n*); the plausible exposed-core range f~0.05-0.20 BRACKETS the window but also
reaches both kill bands (3.2 kT under-cored, 9.0 kT over-cored), so window-vs-kill is NOT decided. dG*_nuc is NOT
pinned; the dwarf branch stays REACHABLE / plausibly non-tuned (2209 bracket confirmed, not upgraded to a pinned
prediction). The genuine last-mile is the DM ELEMENT CROSS-SECTION geometry (exposed-core f) -- one derivation beyond
the currently-pinned corpus. Did NOT manufacture the in-window f. Cluster sigma/m ~ 1/v^2 branch stands.
"""

