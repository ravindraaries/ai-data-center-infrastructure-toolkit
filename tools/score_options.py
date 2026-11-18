#!/usr/bin/env python3
"""Weighted decision matrix scoring. Standard library only."""
import argparse
import csv
from collections import defaultdict
from pathlib import Path

REQUIRED = {"option", "criterion", "weight", "rating", "evidence", "notes"}


def score(path):
    grouped = defaultdict(list)
    with path.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames or not REQUIRED.issubset(reader.fieldnames):
            raise ValueError(f"CSV requires columns: {', '.join(sorted(REQUIRED))}")
        for line, row in enumerate(reader, start=2):
            option = (row["option"] or "").strip()
            criterion = (row["criterion"] or "").strip()
            if not option or not criterion:
                raise ValueError(f"Line {line}: option and criterion are required")
            try:
                weight = float(row["weight"])
                rating = float(row["rating"])
            except (ValueError, TypeError):
                raise ValueError(f"Line {line}: weight and rating must be numeric; blank ratings are not scored") from None
            if not (0 <= weight <= 100 and 1 <= rating <= 5):
                raise ValueError(f"Line {line}: weight must be 0-100 and rating 1-5")
            if any(existing[0] == criterion for existing in grouped[option]):
                raise ValueError(f"Line {line}: duplicate criterion '{criterion}' for '{option}'")
            grouped[option].append((criterion, weight, rating))
    if not grouped:
        raise ValueError("No candidate rows found")
    criteria_sets = {frozenset(item[0] for item in rows) for rows in grouped.values()}
    if len(criteria_sets) != 1:
        raise ValueError("All candidates must use the same criteria")
    weights_by_criterion = {}
    results = []
    for option, rows in grouped.items():
        total_weight = sum(w for _, w, _ in rows)
        if abs(total_weight - 100) > 0.00001:
            raise ValueError(f"{option}: weights total {total_weight:g}, expected 100")
        for criterion, weight, _ in rows:
            if criterion in weights_by_criterion and abs(weights_by_criterion[criterion] - weight) > 0.00001:
                raise ValueError(f"Inconsistent weight for '{criterion}' across candidates")
            weights_by_criterion[criterion] = weight
        weighted = sum(w * r for _, w, r in rows) / 100
        results.append((option, weighted, rows))
    for rank, (option, weighted, rows) in enumerate(sorted(results, key=lambda item: item[1], reverse=True), 1):
        print(f"{rank}. {option}: {weighted:.2f}/5 ({weighted * 20:.1f}/100)")
        for criterion, weight, rating in rows:
            print(f"   {criterion}: {rating:g}/5 x {weight:g}% = {rating * weight / 100:.2f}")
    print("\nReminder: scores are decision aids, not qualification or safety approval.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv_path", type=Path, help="CSV decision matrix")
    args = parser.parse_args()
    try:
        score(args.csv_path)
    except (OSError, ValueError) as error:
        parser.exit(1, f"Error: {error}\n")


if __name__ == "__main__":
    main()
