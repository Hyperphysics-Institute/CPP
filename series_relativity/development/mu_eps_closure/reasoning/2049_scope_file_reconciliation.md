# Reasoning capture — Patch 2049: OPEN-SR-9 scope-file stale-note reconciliation

**STATUS: verbatim (captured at-patch).** Window: 2049-band (SR-9). Opus worker; integrator = Thomas.

Booted the SR-9 window off the canonical 2044 `OPEN-SR-9_handover.md`. On orientation, confirmed the
landmine Patch 2047 had already named: the `OPEN-SR-9_em_emergence_scope.md` progress log stops at the 2021
"leaning FAIL" downgrade and was never carried forward, while the canonical `R2-STATUS.md` ladder had run
2024→2041 to conditional-PASS. 2047 fixed the *downstream* CONJ.md brackets but explicitly left this scope
file's own log owed an update, flagged for the SR-9 window — which is this window. Thomas approved folding the
reconciliation in as a cleanup.

This patch appends four notes (2024 supersession, 2025 recovery, 2027→2031 sharpening, 2037/2038+2041 tail)
plus a net-state line, each cross-checked against the R2-STATUS.md ladder rather than re-derived — applying
the exact discipline 2047 prescribed (a sector scope file can lag the verdict ladder; the ladder is canonical;
cross-check the scope file's verdict claim against it). Added a RECONCILIATION banner making explicit that
R2-STATUS.md is authoritative and this scope file is not, so a future window can't be misled by the scope file
the way 2045 was.

No physics moved. This is a documentation-truth patch: it does not change R2's status (still conditional-PASS
at field-content level) or OPEN-SR-9's status (still genuinely OPEN, the from-substrate route). The substantive
SR-9 work — the cold-from-c06 EM-emergence construction (budget-vs-phonon kinetic-term split; whether the
transverse photon mode inherits the curl-stiffness tensor K_ij or is set purely by the scalar PSR budget) —
was presented inline for founder adjudication and is NOT in this patch; it captures as its own patch after
TLA signs off on the mode-2 kinetic-term claim.

NO THEO (documentation reconciliation; no new axiom/term/counted prediction; no status move). Tier: the edited
file is in the owned `mu_eps_closure/` SR-9 subtree (private-lane for this window), NOT a root registry. Owned
greenfield reasoning fragment. Collision-clean against HEAD 2048.
