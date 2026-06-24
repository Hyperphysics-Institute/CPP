#!/usr/bin/env bash
# PENDING regression test for the §6.1 temporary-THEO-handle permanentize stage.
# Ratified by Patch 2116; the stage it exercises is a build item (Patch 2117) NOT
# yet present in overnight_extraction_audit.sh. This file is therefore NOT wired
# into test_overnight_audit.sh and is self-skipping: it probes the macro for the
# §6.1 alias-map contract and exits 0 (PENDING) until the stage exists, at which
# point it activates automatically. When 2117 lands, move this case into
# test_overnight_audit.sh so it counts toward the heartbeat total.
#
# Contract under test (the one design property): two windows that mint the SAME
# optimistic display guess in the SAME family on DIFFERENT patches must
# permanentize to DISTINCT numbers with ZERO change orders — because the handle
# is keyed on the patch-anchored TMP segment, not the guessed integer.
set -uo pipefail
MACRO="$(cd "$(dirname "$0")" && pwd)/overnight_extraction_audit.sh"

# --- capability probe: skip cleanly until the 2117 stage is built ----------
if [ ! -f "$MACRO" ] || ! grep -q 'theo_alias_map' "$MACRO" 2>/dev/null; then
  echo "PENDING: §6.1 temp-handle permanentize stage not yet built into overnight_extraction_audit.sh (Patch 2117). Skipping."
  exit 0
fi

SCRATCH="$(mktemp -d)"; trap 'rm -rf "$SCRATCH"' EXIT
PASS=0; FAIL=0
ck() { if eval "$2"; then PASS=$((PASS+1)); echo "  ok: $1"; else FAIL=$((FAIL+1)); echo "  FAIL: $1"; fi; }

cd "$SCRATCH"
git init -q && git config user.email t@t && git config user.name t
mkdir -p templates Development/transcripts Registries_pending series_a series_b
touch templates/capture_and_audit_protocol.md
printf '# audit heartbeat log\n## Runs\n' > Development/audit_log.md
# seed registry: DS family currently tops out at 6
printf 'THEO-DS-6 : established\n' > theorem-registry.md

# Two windows, SAME family (DS), SAME optimistic guess (7), DIFFERENT patches.
# Each cites its handle in a paper file AND claims it in its own pending file.
H1='THEO-DS-7-TMP-p0849'   # window dm-1
H2='THEO-DS-7-TMP-p1012'   # window cc-u
printf 'Result: by %s the Sea residual is inert.\n' "$H1" > series_a/dm1_paper.md
printf 'Lemma %s gives the uniform-Sea cancellation.\n' "$H2" > series_b/ccu_paper.md
printf -- '- %s | family:DS | patch:0849 | "Sea-residual SSV is gravitationally inert."\n' "$H1" > Registries_pending/dm-1.md
printf -- '- %s | family:DS | patch:1012 | "Uniform-Sea impedance cancels at leading order."\n' "$H2" > Registries_pending/cc-u.md

"$MACRO" >/dev/null 2>&1 || true

# 1) two DISTINCT permanent DS numbers registered (7 and 8), zero change orders
ck "two distinct permanent DS numbers registered" \
   'test "$(grep -oE "THEO-DS-[0-9]+ " theorem-registry.md | sort -u | wc -l)" -ge 3'
ck "no change-order artifact emitted" \
   '! ls change_order* CHANGE-ORDER* 2>/dev/null | grep -q .'
# 2) both papers rebound — no TMP handle survives anywhere in the corpus
ck "no TMP handle survives in series_a paper" '! grep -q "TMP-" series_a/dm1_paper.md'
ck "no TMP handle survives in series_b paper" '! grep -q "TMP-" series_b/ccu_paper.md'
# 3) alias map carries both temp->permanent entries (grace-window resolution)
ck "alias map has both temp handles" \
   'grep -q "$H1" Development/theo_alias_map.md && grep -q "$H2" Development/theo_alias_map.md'
# 4) the two papers resolved to DIFFERENT permanent numbers (the core property)
ck "the two handles permanentized to distinct numbers" \
   'test "$(grep -oE "THEO-DS-[0-9]+" series_a/dm1_paper.md series_b/ccu_paper.md | sort -u | wc -l)" -eq 2'
# 5) pending claims cleared after merge
ck "pending claims cleared" '! ls Registries_pending/*.md 2>/dev/null | grep -q .'

echo "temp-handle permanentize: PASS=$PASS FAIL=$FAIL"
[ "$FAIL" -eq 0 ]
