#!/usr/bin/env python3
"""Stage 2 3절: draw 25 random verified papers NOT added by adversarial-reviewer.
Usage: python3 -I outputs/literature/draw_verification_sample.py   (seed fixed below)"""
import csv, os, random
SEED = 20261112
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
rows = list(csv.DictReader(open(os.path.join(ROOT, "outputs/literature/literature_db.csv"), encoding="utf-8")))
pool = [r for r in rows if r["verified"] == "True" and "adversarial-reviewer" not in r["added_by"]]
pool.sort(key=lambda r: r["uid"])
random.seed(SEED)
sample = random.sample(pool, 25)
print(f"seed={SEED} pool={len(pool)} sample=25")
for i, r in enumerate(sample, 1):
    print(f"{i}\t{r['uid']}\t{r['added_by']}\t{r['discussion_read']}\t{r['citation'][:90]}")
