#!/usr/bin/env bash
set -euo pipefail

file="${1:-FPF-Spec.md}"

if [[ ! -f "$file" ]]; then
  echo "error: file not found: $file" >&2
  exit 2
fi

awk '
BEGIN { current=""; errors=0 }
{
  if ($0 ~ /^## /) {
    if (match($0, /^## ([A-G]\.[0-9A-Za-z]+(\.[0-9A-Za-z]+)*)/, m)) {
      current = m[1]
    }
  }

  if ($0 ~ /^### [A-G]\.[0-9A-Za-z]+(\.[0-9A-Za-z]+)*:End$/) {
    if (match($0, /^### ([A-G]\.[0-9A-Za-z]+(\.[0-9A-Za-z]+)*):End$/, m)) {
      end_id = m[1]
      if (current == "") {
        printf("%s:%d: end marker %s appears before any section heading\n", FILENAME, NR, end_id)
        errors++
      } else if (end_id != current) {
        printf("%s:%d: end marker %s does not match current section %s\n", FILENAME, NR, end_id, current)
        errors++
      }
    }
  }
}
END {
  if (errors > 0) {
    exit 1
  }
}
' "$file"

echo "OK: section end markers match current section IDs in $file"
