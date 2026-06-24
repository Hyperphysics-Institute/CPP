#!/usr/bin/env bash
# Regression harness for overnight_extraction_audit.sh (§4.3). Builds an isolated
# scratch repo, exercises every deterministic path, asserts staged outputs + heartbeat.
set -uo pipefail
MACRO="$(cd "$(dirname "$0")" && pwd)/overnight_extraction_audit.sh"
SCRATCH="$(mktemp -d)"; trap 'rm -rf "$SCRATCH"' EXIT
PASS=0; FAIL=0
ck() { if eval "$2"; then PASS=$((PASS+1)); echo "  ok: $1"; else FAIL=$((FAIL+1)); echo "  FAIL: $1"; fi; }

cd "$SCRATCH"
git init -q && git config user.email t@t && git config user.name t
mkdir -p templates Development/transcripts Registries_pending
touch templates/capture_and_audit_protocol.md
printf '# audit heartbeat log\n## Runs\n' > Development/audit_log.md
# canonical founders_vision with a known quote (dedup target)
printf '> This is an ALREADY PROMOTED founder quote about the lattice.\n' > founders_vision.md

D=2026-06-24
# structured transcript: 1 novel founder (AUTO), 1 duplicate (REVIEW), 1 malformed (REVIEW)
cat > "Development/transcripts/${D}_0900_p850_dm-1.md" <<EOF
---
window-slug: dm-1
patch: 850
opened: $D 09:00 UTC
format: structured
---

### [1] TLA
A brand-new insight: @@FOUNDER: "Dark matter is the Sea's residual SSV." | context: DM-1 identification
And a dup: @@FOUNDER: "This is an ALREADY PROMOTED founder quote about the lattice." | context: dup test
And a malformed one: @@FOUNDER: "no context here"

### [2] WORKER
Acknowledged.
EOF
# raw transcript -> freeform_pending
cat > "Development/transcripts/${D}_0905_p851_notes.md" <<EOF
---
window-slug: notes
patch: 851
opened: $D 09:05 UTC
format: raw
---
some raw unstructured notes
EOF
# malformed transcript: structured but no turns
cat > "Development/transcripts/${D}_0906_p852_broken.md" <<EOF
---
window-slug: broken
patch: 852
opened: $D 09:06 UTC
format: structured
---
no turn headers here
EOF
# pending deltas: 1 valid, 1 bad-registry (schema reject)
cat > "Registries_pending/dm-1.md" <<EOF
---
window-slug: dm-1
---
# Pending registry deltas — dm-1
- registry=predictions | action="+3 zero-parameter PRED-DM-1-{1,2,3}" | paper=DM-1 | patch=850
- registry=not-a-registry | action="bogus" | paper=DM-1 | patch=850
EOF
git add -A && git commit -qm fixtures

echo "== DRY-RUN =="
bash "$MACRO" --date "$D" >/tmp/dry.out 2>&1; DRC=$?
ck "dry-run exits 0"            '[ $DRC -eq 0 ]'
ck "dry-run wrote nothing"      '[ -z "$(git status --porcelain)" ]'
ck "dry-run flags malformed"    'grep -q "MALFORMED" /tmp/dry.out'
ck "dry-run plans AUTO founder" 'grep -q "founder \[AUTO\]" /tmp/dry.out'
ck "dry-run plans DUPLICATE"    'grep -q "REVIEW:DUPLICATE" /tmp/dry.out'
ck "dry-run plans MALFORMED fnd" 'grep -q "REVIEW:MALFORMED" /tmp/dry.out'
ck "dry-run plans valid delta"  'grep -q "registry \[predictions\]" /tmp/dry.out'
ck "dry-run plans schema review" 'grep -q "REVIEW:SCHEMA" /tmp/dry.out'

echo "== APPLY =="
bash "$MACRO" --apply --date "$D" >/tmp/app.out 2>&1; ARC=$?
ck "apply staged founders file" '[ -s "Development/staging/$D/founders/${D}_founders.md" ]'
ck "founders has AUTO label"     'grep -q "\[AUTO\]" "Development/staging/$D/founders/${D}_founders.md"'
ck "founders has DUPLICATE"      'grep -q "REVIEW:DUPLICATE" "Development/staging/$D/founders/${D}_founders.md"'
ck "founders_vision untouched"   '[ "$(wc -l < founders_vision.md)" -eq 1 ]'
ck "registry delta staged"       'grep -q "PRED-DM-1" "Development/staging/$D/registry/predictions.delta"'
ck "schema reject staged"        'grep -q "REVIEW:SCHEMA" "Development/staging/$D/registry/_REVIEW.txt"'
ck "pending cleared"             '! grep -q "PRED-DM-1" Registries_pending/dm-1.md'
ck "freeform pending listed"     '[ -s "Development/staging/$D/freeform_pending/${D}_pending.txt" ]'
ck "heartbeat appended"          'grep -q "^$D .* run=OK" Development/audit_log.md'
ck "heartbeat reports malformed" 'grep -q "malformed:1" Development/audit_log.md'
ck "heartbeat open_review>=2"    'grep -qE "open_review=[2-9]" Development/audit_log.md'
ck "apply exits 0"               '[ $ARC -eq 0 ]'

echo ""
echo "RESULT: PASS=$PASS FAIL=$FAIL"
[ $FAIL -eq 0 ]
