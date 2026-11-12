#!/usr/bin/env python3
"""Stage 2 Deliverable D helper: flatten future_directions of verified papers.
Usage: python3 -I outputs/literature/export_future_directions.py
Output: outputs/literature/future_directions_all.csv (one row per future direction)"""
import csv, json, os, re
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
rows = list(csv.DictReader(open(os.path.join(ROOT, "outputs/literature/literature_db.csv"), encoding="utf-8")))
out = []
for r in rows:
    for fd in json.loads(r["future_directions"] or "[]"):
        ad = str(fd.get("already_done", "")).strip()
        status = (ad.split()[0].lower() if ad else "blank").strip("(),.:;")
        out.append({"uid": r["uid"], "citation": r["citation"][:160], "year": r["year"],
                    "verified": r["verified"], "discussion_read": r["discussion_read"],
                    "fd_text": fd.get("text", ""), "section": fd.get("section", ""),
                    "already_done": ad, "status": status, "from_agent": fd.get("from", ""),
                    "applicable_datasets": r["applicable_datasets"], "axes": r["axes"]})
cols = list(out[0].keys())
with open(os.path.join(ROOT, "outputs/literature/future_directions_all.csv"), "w", newline="", encoding="utf-8") as fh:
    w = csv.DictWriter(fh, fieldnames=cols); w.writeheader(); w.writerows(out)
print("rows", len(out))
