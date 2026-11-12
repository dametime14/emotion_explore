#!/usr/bin/env python3
"""Stage 2 Deliverable D helper: parse Discussion-to-Research chains from round1.md.
Usage: python3 -I outputs/literature/export_chains.py
Output: outputs/literature/chains_index.csv"""
import csv, glob, os, re
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
LABELS = {"orig": r"Original Finding", "unres": r"Unresolved Question", "tech": r"Technological Development",
          "combo": r"New Dataset\s*/\s*Model Combination", "rq": r"New Research Question"}
ID_RE = re.compile(r"(10\.\d{4,9}/[^\s,;\]\)]+|arXiv:\d{4}\.\d{4,5}|pmlr[:\-][\w\-]+)", re.I)
DS = ["Horikawa", "Emo-FilM", "Spacetop", "NSD"]
rows = []
for f in sorted(glob.glob(os.path.join(ROOT, "outputs/agents/*/round1.md"))):
    agent = f.split(os.sep)[-2]
    text = open(f, encoding="utf-8").read()
    m = re.search(r"(?ms)^## 6\..*?(?=^## 7\.|\Z)", text)
    if not m:
        continue
    for ch in re.split(r"(?m)^### ", m.group(0))[1:]:
        title = ch.splitlines()[0].strip()
        rec = {"agent": agent, "chain": title}
        for k, lab in LABELS.items():
            mm = re.search(r"(?is)\*?\*?" + lab + r"\*?\*?\s*[:：.]\*?\*?\s*(.+?)(?=\n\s*[\*\-]\s+\*\*|\n\n|\Z)", ch)
            rec[k] = re.sub(r"\s+", " ", mm.group(1)).strip() if mm else ""
        rec["orig_ids"] = "; ".join(dict.fromkeys(i.rstrip(".") for i in ID_RE.findall(rec["orig"])))
        rec["unres_ids"] = "; ".join(dict.fromkeys(i.rstrip(".") for i in ID_RE.findall(rec["unres"])))
        rec["tech_ids"] = "; ".join(dict.fromkeys(i.rstrip(".") for i in ID_RE.findall(rec["tech"])))
        rec["datasets"] = "; ".join(d for d in DS if d.lower() in (title + rec["combo"]).lower())
        g1 = re.search(r"(?i)G1[^\n]{0,120}", ch)
        rec["g1"] = g1.group(0).strip() if g1 else ""
        rec["overlap"] = "; ".join(sorted(set(re.findall(r"overlap:\s*([A-Za-z\-]+(?: 연구)?)", ch))))
        rows.append(rec)
cols = ["agent", "chain", "orig_ids", "unres_ids", "tech_ids", "datasets", "overlap", "g1", "orig", "unres", "tech", "combo", "rq"]
with open(os.path.join(ROOT, "outputs/literature/chains_index.csv"), "w", newline="", encoding="utf-8") as fh:
    w = csv.DictWriter(fh, fieldnames=cols); w.writeheader(); w.writerows(rows)
print("chains", len(rows), "missing rq", sum(1 for r in rows if not r["rq"]), "missing orig", sum(1 for r in rows if not r["orig"]))
