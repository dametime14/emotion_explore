#!/usr/bin/env python3
"""Extract revision-round questions from outputs/agents/*/revision_round.md into a compact table.
Usage: python3 -I outputs/revision/extract_candidates.py > /dev/null  (writes outputs/revision/candidates_raw.md)"""
import os, re
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
AG = ["vision-decoding", "brain-inspired", "encoding-foundation", "frontier-ai", "geometry-info", "emotion-theory", "multimodal-dynamics"]
KEYS = [("AI", r"AI가 있어야"), ("NEW", r"새로 알게"), ("DATA", r"^\W*데이터"), ("MODEL", r"모델과 checkpoint"),
        ("TEST", r"핵심 분석"), ("PLAN", r"4주 계획"), ("PRIOR", r"가장 가까운 선행"), ("RISK", r"주요 위험")]
out = ["# 재탐색 후보 원자료 (자동 추출, 각 항목 앞부분만)", "", "원문은 `outputs/agents/<이름>/revision_round.md`.", ""]
for a in AG:
    t = open(os.path.join(ROOT, "outputs/agents", a, "revision_round.md"), encoding="utf-8").read()
    heads = list(re.finditer(r"(?m)^#{2,4} .*?\[([A-Z]{2}-RV-[0-9A-Z]+)\]\s*(.+)$", t))
    for i, h in enumerate(heads):
        body = t[h.end(): heads[i + 1].start() if i + 1 < len(heads) else len(t)]
        body = re.split(r"(?m)^## (?!\d+\.\s*\[)", body)[0]
        out.append(f"## {h.group(1)} ({a}) {h.group(2).strip()}")
        lines = body.splitlines()
        for key, pat in KEYS:
            for j, ln in enumerate(lines):
                if re.search(pat, re.sub(r"[*#|]", "", ln).strip()):
                    chunk = " ".join(x.strip() for x in lines[j:j + 4])
                    chunk = re.sub(r"\s+", " ", re.sub(r"[*#]", "", chunk))
                    out.append(f"* {key}: {chunk[:300]}")
                    break
        out.append("")
open(os.path.join(ROOT, "outputs/revision/candidates_raw.md"), "w", encoding="utf-8").write("\n".join(out) + "\n")
print(len([l for l in out if l.startswith('## ')]))
