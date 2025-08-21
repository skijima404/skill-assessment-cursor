#!/usr/bin/env bash
set -euo pipefail

say() { printf "[verify] %s\n" "$*"; }
fail() { printf "[verify][FAIL] %s\n" "$*" >&2; exit 1; }

need() { command -v "$1" >/dev/null 2>&1 || fail "$1 is required"; }
need jq

extract_json() {
  local file="$1"
  local start end
  start=$(grep -n '```json' "$file" | head -n1 | cut -d: -f1 || true)
  [[ -n "${start:-}" ]] || fail "no ```json block in $file"
  end=$(tail -n +$((start+1)) "$file" | grep -n '```' | head -n1 | cut -d: -f1 || true)
  [[ -n "${end:-}" ]] || fail "no closing fence after ```json in $file"
  end=$((start + end - 1))
  sed -n "$((start+1)),${end}p" "$file"
}

check_template() {
  local file="$1"
  say "checking $file"
  local json
  json=$(extract_json "$file") || fail "cannot extract JSON from $file"

  # Required keys exist
  echo "$json" | jq -e 'has("score") and has("risks") and has("deltas") and has("next_steps") and has("evidence")' >/dev/null \
    || fail "missing required keys in $file"

  # Score keys exist and within ranges; avg>=3 and each>=2
  echo "$json" | jq -e '(.score|has("design") and has("code") and has("tests")) and \
      ([.score.design,.score.code,.score.tests] | (add/3) >= 3 and all(. >= 2))' >/dev/null \
    || fail "score thresholds not satisfied in $file"

  # next_steps at least 1
  echo "$json" | jq -e '.next_steps | length >= 1' >/dev/null \
    || fail "next_steps must have >=1 item in $file"

  # evidence non-empty strings
  echo "$json" | jq -e '.evidence | length >= 1 and (all(.[]; type=="string" and (.|gsub("\\s+";"")|length)>0))' >/dev/null \
    || fail "evidence must contain non-empty strings in $file"

  say "OK: $file"
}

main() {
  shopt -s nullglob
  local files=(docs/templates/*.md)
  if (( ${#files[@]} == 0 )); then
    say "no templates found under docs/templates/ — skipping (OK for early stage)"
    exit 0
  fi
  for f in "${files[@]}"; do
    check_template "$f"
  done
  say "all checks passed"
}

main "$@"