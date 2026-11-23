#!/usr/bin/env python3
"""Recompute a matched 2x2 prediction table from explicit CSV inputs.

No network, archive extraction, or implicit path discovery is performed.
"""
import argparse
import csv
import json
from collections import Counter


def load_carve(path):
    rows = {}
    with open(path, newline="", encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            key = row["id"]
            if key in rows:
                raise ValueError(f"duplicate CARVE id: {key}")
            rows[key] = (int(row["label"]), int(row["predicted_label"]))
    return rows


def load_lr(path, strategy):
    rows = {}
    with open(path, newline="", encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            if row["model"] != strategy:
                continue
            key = row["id"]
            if key in rows:
                raise ValueError(f"duplicate LR id for {strategy}: {key}")
            rows[key] = (int(row["gold"]), int(row["prediction"]))
    return rows


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--carve", required=True, help="carve_predictions.csv")
    p.add_argument("--lr-oof", required=True, help="OOF_PREDICTIONS.csv")
    p.add_argument("--strategy", default="pooled_strict_lr")
    args = p.parse_args()

    carve, lr = load_carve(args.carve), load_lr(args.lr_oof, args.strategy)
    if carve.keys() != lr.keys():
        raise SystemExit(
            f"ID sets differ: CARVE={len(carve)}, LR={len(lr)}, "
            f"intersection={len(carve.keys() & lr.keys())}"
        )
    cells = Counter()
    label_mismatches = 0
    carve_correct = lr_correct = 0
    for key in sorted(carve):
        gold_c, pred_c = carve[key]
        gold_l, pred_l = lr[key]
        label_mismatches += gold_c != gold_l
        cc, lc = pred_c == gold_c, pred_l == gold_l
        carve_correct += cc
        lr_correct += lc
        cells[(cc, lc)] += 1
    if label_mismatches:
        raise SystemExit(f"gold labels disagree for {label_mismatches} IDs")
    result = {
        "n": len(carve),
        "carve_correct": carve_correct,
        "lr_correct": lr_correct,
        "carve_accuracy": carve_correct / len(carve),
        "lr_accuracy": lr_correct / len(lr),
        "both_correct": cells[(True, True)],
        "carve_only_correct": cells[(True, False)],
        "lr_only_correct": cells[(False, True)],
        "both_wrong": cells[(False, False)],
        "gold_label_mismatches": label_mismatches,
        "strategy": args.strategy,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

