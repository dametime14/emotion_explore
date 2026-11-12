#!/usr/bin/env python3
"""Revision round (plan.md 3절 3번): reconcile Coordinator and reviewer scores, 11 criteria.

Inputs : outputs/revision/scores_coordinator.csv, scores_reviewer.csv (cand_id,criterion,score,reason)
         outputs/revision/adjustments.csv (cand_id,criterion,final_score,who_moved,reason), written by the
         Coordinator after reading both reasons for every pair that differs by >= 2 points.
Rule   : final score = mean of the two scores, unless an adjustment row exists for that pair.
         Pairs that differ by >= 2 and have no adjustment row are listed as unresolved.
Output : outputs/revision/scores_final.csv, outputs/revision/gap_table.md (for scores_reconciled.md)
Usage  : python3 -I outputs/revision/reconcile.py
"""
import collections
import csv
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
E = os.path.join(ROOT, "outputs/revision")
CRIT = ["Novelty", "Neuroscientific Importance", "AI / Modeling Contribution", "Dataset Feasibility",
        "Methodological Rigor", "Falsifiability", "Interpretability", "Generalizability", "Feasibility",
        "AI-enabled Affective Neuroscience Contribution", "1-month Feasibility"]


def load(name):
    d = {}
    for r in csv.DictReader(open(os.path.join(E, name), encoding="utf-8")):
        d[(r["cand_id"].strip(), r["criterion"].strip())] = (float(r["score"]), r["reason"])
    return d


def main():
    c, r = load("scores_coordinator.csv"), load("scores_reviewer.csv")
    keys = sorted(set(c) | set(r), key=lambda k: (int(k[0][2:]), CRIT.index(k[1])))
    missing = [k for k in keys if k not in c or k not in r]
    adj = {}
    p = os.path.join(E, "adjustments.csv")
    if os.path.exists(p):
        for a in csv.DictReader(open(p, encoding="utf-8")):
            adj[(a["cand_id"], a["criterion"])] = a
    rows, gaps = [], []
    for k in keys:
        if k in missing:
            continue
        sc, sr = c[k][0], r[k][0]
        d = sr - sc
        if k in adj:
            final, status = float(adj[k]["final_score"]), "adjusted"
        else:
            final = (sc + sr) / 2
            status = "unresolved" if abs(d) >= 2 else "mean"
        rows.append({"cand_id": k[0], "criterion": k[1], "coordinator": sc, "reviewer": sr, "diff": d,
                     "final": final, "status": status})
        if abs(d) >= 2:
            gaps.append((k, sc, sr, c[k][1], r[k][1], adj.get(k)))
    with open(os.path.join(E, "scores_final.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    tot = collections.defaultdict(lambda: [0, 0, 0])
    for x in rows:
        t = tot[x["cand_id"]]
        t[0] += x["coordinator"]; t[1] += x["reviewer"]; t[2] += x["final"]
    L = ["| 순위 | 후보 | Coordinator 합계 | Reviewer 합계 | 최종 합계 | 최종 AI 기여 | 최종 1개월 |", "|---|---|---|---|---|---|---|"]
    fin = {(x["cand_id"], x["criterion"]): x["final"] for x in rows}
    for i, (rq, t) in enumerate(sorted(tot.items(), key=lambda x: (-x[1][2], int(x[0][2:]))), 1):
        L.append(f"| {i} | {rq} | {t[0]:.0f} | {t[1]:.0f} | {t[2]:.1f} | {fin[(rq, CRIT[9])]:.1f} | {fin[(rq, CRIT[10])]:.1f} |")
    G = ["| 후보 | 기준 | Coord | Reviewer | Coordinator 근거 | Reviewer 근거 | 처리 |", "|---|---|---|---|---|---|---|"]
    for k, sc, sr, rc, rr, a in gaps:
        proc = f"조정 {a['final_score']} ({a['who_moved']}): {a['reason']}" if a else "미조정(이견 유지)"
        G.append(f"| {k[0]} | {k[1]} | {sc:.0f} | {sr:.0f} | {rc} | {rr} | {proc} |")
    open(os.path.join(E, "gap_table.md"), "w", encoding="utf-8").write(
        "## 합계 순위\n\n" + "\n".join(L) + "\n\n## 2점 이상 차이\n\n" + "\n".join(G) + "\n")
    agree = sum(1 for x in rows if abs(x["diff"]) <= 1) / len(rows)
    print(f"pairs={len(rows)} missing={len(missing)} gaps>=2={len(gaps)} "
          f"adjusted={sum(1 for x in rows if x['status']=='adjusted')} unresolved={sum(1 for x in rows if x['status']=='unresolved')} "
          f"agree(|d|<=1)={agree:.2f}")
    bycrit = collections.Counter(k[1] for k, *_ in gaps)
    print("gaps by criterion", dict(bycrit))


if __name__ == "__main__":
    main()
