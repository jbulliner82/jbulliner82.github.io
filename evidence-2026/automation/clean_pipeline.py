#!/usr/bin/env python3
"""Evidence Portfolio: deterministic CSV normalization and quality gate.

No private/customer data or network access. Failures are quarantined with clear reasons.
"""
from __future__ import annotations
import argparse
import csv
import json
import re
from collections import Counter
from pathlib import Path

FIELDS = ('record_id', 'full_name', 'email', 'source', 'priority')
OUTPUT_FIELDS = ('record_id', 'full_name', 'email', 'source', 'priority')
EMAIL = re.compile(r'^[^\s@]+@[^\s@]+\.[^\s@]+$')


def normalize_record(row: dict[str, str]) -> tuple[dict[str, str] | None, str | None]:
    """Normalize non-sensitive demo records or give an explicit validation reason."""
    uid = str(row.get('record_id') or '').strip().upper()
    name = ' '.join(str(row.get('full_name') or '').strip().split())
    email = str(row.get('email') or '').strip().lower()
    source = str(row.get('source') or '').strip().lower()
    priority = str(row.get('priority') or '').strip().lower()
    if not uid:
        return None, 'missing_record_id'
    if not name:
        return None, 'missing_name'
    if not EMAIL.fullmatch(email):
        return None, 'invalid_email'
    if source not in {'web', 'phone', 'referral'}:
        return None, 'unsupported_source'
    if priority not in {'low', 'medium', 'high'}:
        return None, 'invalid_priority'
    return dict(record_id=uid, full_name=name, email=email, source=source, priority=priority), None


def run(input_path: Path, output_dir: Path) -> dict:
    """Process a CSV with stable first-valid-ID-wins deduplication."""
    output_dir.mkdir(parents=True, exist_ok=True)
    normalized: list[dict] = []
    quarantine: list[dict] = []
    reasons: Counter = Counter()
    seen: set[str] = set()
    with input_path.open('r', encoding='utf-8-sig', newline='') as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames or any(f not in reader.fieldnames for f in FIELDS):
            raise ValueError(f'CSV must have columns: {", ".join(FIELDS)}')
        total = 0
        for line_number, row in enumerate(reader, start=2):
            total += 1
            clean, reason = normalize_record(row)
            if reason is None and clean is not None and clean['record_id'] in seen:
                reason = 'duplicate_record_id'
            if reason:
                reasons[reason] += 1
                quarantine.append({'csv_line': line_number, 'reason': reason, 'record_id': str(row.get('record_id') or '').strip()})
            else:
                normalized.append(clean)
                seen.add(clean['record_id'])
    for filename, fields, records in [
        ('cleaned.csv', OUTPUT_FIELDS, normalized),
        ('quarantine.csv', ('csv_line', 'reason', 'record_id'), quarantine),
    ]:
        with (output_dir/filename).open('w', encoding='utf-8', newline='') as handle:
            writer = csv.DictWriter(handle, fieldnames=fields)
            writer.writeheader()
            writer.writerows(records)
    report = {
        'data_type': 'synthetic_portfolio_demo',
        'input_file': input_path.name,
        'total_rows': total,
        'accepted_rows': len(normalized),
        'quarantined_rows': len(quarantine),
        'acceptance_rate': round(len(normalized) / total, 4) if total else 0,
        'reasons': dict(sorted(reasons.items())),
        'deduplication': 'first valid record_id kept in CSV order',
    }
    (output_dir/'qa_report.json').write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    return report


def main() -> None:
    parser = argparse.ArgumentParser(description='Normalize and validate an explicitly synthetic sample CSV')
    parser.add_argument('--input', type=Path, default=Path(__file__).parent/'data'/'sample_leads.csv')
    parser.add_argument('--out', type=Path, default=Path(__file__).parent/'output')
    args = parser.parse_args()
    print(json.dumps(run(args.input,args.out),indent=2))


if __name__ == '__main__':
    main()