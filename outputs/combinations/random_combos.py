#!/usr/bin/env python3
"""Stage 3 P5 random path: one Axis per type, 30 combinations.
Type table = outputs/axis_encyclopedia.md section 3 (after the user decision:
U, V, W adopted; X folded into R, Y folded into A).
Usage: python3 -I outputs/combinations/random_combos.py
Output: outputs/combinations/random_combos.csv"""
import csv, os, random
SEED = 20261113
TYPES = {
    "Construct": ["A", "B", "C", "D", "V", "W"],
    "Neural": ["E", "F", "O"],
    "Model & Method": ["G", "H", "I", "J", "L", "M", "N"],
    "Structure & Interpretation": ["K", "R"],
    "Inference & Measurement": ["P", "Q", "S", "T", "U"],
}
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
rng = random.Random(SEED)
rows, seen = [], set()
while len(rows) < 30:
    combo = tuple(rng.choice(v) for v in TYPES.values())
    if combo in seen:
        continue
    seen.add(combo)
    rows.append({"combo_id": f"RND-{len(rows)+1:02d}", **dict(zip(TYPES.keys(), combo)), "axes": "+".join(combo)})
with open(os.path.join(ROOT, "outputs/combinations/random_combos.csv"), "w", newline="", encoding="utf-8") as fh:
    w = csv.DictWriter(fh, fieldnames=["combo_id", *TYPES.keys(), "axes"]); w.writeheader(); w.writerows(rows)
print(f"seed={SEED}")
for r in rows: print(r["combo_id"], r["axes"])
