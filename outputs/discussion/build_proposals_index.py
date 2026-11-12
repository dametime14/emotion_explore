#!/usr/bin/env python3
"""Stage 3 Round 2: build outputs/discussion/proposals_index.md (+ .csv) from
outputs/agents/<agent>/round2.md "보내는 제안" sections.

Usage: python3 -I outputs/discussion/build_proposals_index.py
Columns (prompts/stage3 1절): 제안 ID, 보낸 에이전트, 받는 에이전트, 요약, 근거 논문
(+ 관련 Axis, 데이터셋 for later combination bookkeeping)."""
import csv
import glob
import os
import re

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
AGENTS = ["emotion-theory", "vision-decoding", "encoding-foundation", "multimodal-dynamics",
          "frontier-ai", "geometry-info", "systems-neuro", "generative-counterfactual",
          "llm-semantics", "brain-inspired", "adversarial-reviewer"]
PREFIX = {"ET": "emotion-theory", "VD": "vision-decoding", "EF": "encoding-foundation",
          "MD": "multimodal-dynamics", "FA": "frontier-ai", "GI": "geometry-info",
          "SN": "systems-neuro", "GC": "generative-counterfactual", "LS": "llm-semantics",
          "BI": "brain-inspired", "AR": "adversarial-reviewer"}
ID_RE = re.compile(r"(10\.\d{4,9}/[^\s,;\]\)]+|arXiv:\d{4}\.\d{4,5}|pmlr[:\-][\w\-]+)", re.I)
FIELDS = {"to": r"받는 에이전트", "content": r"제안 내용", "axes": r"관련 Axis",
          "evidence": r"근거(?: 논문)?(?: ID)?", "datasets": r"가능한 데이터셋",
          "objection": r"예상되는 반론"}


def field(block, label):
    m = re.search(r"(?is)\*\*\s*" + label + r"\s*[:：]?\s*\*\*\s*[:：]?\s*(.+?)(?=\n\s*[\*\-]\s+\*\*|\n#{2,4} |\Z)", block)
    if not m:
        m = re.search(r"(?im)^\s*[\*\-]?\s*" + label + r"\s*[:：]\s*(.+)$", block)
    return re.sub(r"\s+", " ", m.group(1)).strip() if m else ""


def receivers(text):
    found = []
    for a in AGENTS:
        if re.search(r"\b" + re.escape(a) + r"\b", text):
            found.append(a)
    return found


def main():
    rows = []
    for agent in AGENTS:
        path = os.path.join(ROOT, "outputs/agents", agent, "round2.md")
        if not os.path.exists(path):
            continue
        text = open(path, encoding="utf-8").read()
        for m in re.finditer(r"(?m)^#{3,4}\s+\**([A-Z]{2}-P\d+)\**[.:：)]?\s*(.*)$", text):
            pid, title = m.group(1), m.group(2).strip()
            start = m.end()
            nxt = re.search(r"(?m)^#{2,4}\s", text[start:])
            block = text[start:start + nxt.start()] if nxt else text[start:]
            to_raw = field(block, FIELDS["to"])
            main_to = to_raw.split("(")[0]
            recv = receivers(main_to) or receivers(to_raw)
            ev = field(block, FIELDS["evidence"])
            rows.append({
                "proposal_id": pid, "from": PREFIX.get(pid[:2], agent), "to": "; ".join(recv) or to_raw[:60],
                "to_raw": to_raw, "title": title, "content": field(block, FIELDS["content"]),
                "axes": field(block, FIELDS["axes"]), "evidence_ids": "; ".join(dict.fromkeys(ID_RE.findall(ev))),
                "datasets": field(block, FIELDS["datasets"]), "objection": field(block, FIELDS["objection"]),
            })
    os.makedirs(os.path.join(ROOT, "outputs/discussion"), exist_ok=True)
    cols = list(rows[0].keys()) if rows else []
    with open(os.path.join(ROOT, "outputs/discussion/proposals_index.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=cols)
        w.writeheader()
        w.writerows(rows)

    def short(s, n):
        s = s.replace("|", "/").replace("**", "").strip()
        return s if len(s) <= n else s[:n] + "..."
    L = ["# Round 2 제안 목록 (proposals_index)", "",
         "* 생성: `python3 -I outputs/discussion/build_proposals_index.py` (각 에이전트 round2.md 2절에서 추출)",
         f"* 제안 수: {len(rows)}개. 전체 서술, 예상 반론, 선행 확인은 각 round2.md 해당 제안 절에 있다.", "",
         "| 제안 ID | 보낸 에이전트 | 받는 에이전트 | 요약 | 관련 Axis | 근거 논문 |", "|---|---|---|---|---|---|"]
    for r in rows:
        summ = r["title"] or r["content"]
        L.append(f"| {r['proposal_id']} | {r['from']} | {r['to']} | {short(summ, 120)} | {short(r['axes'], 40)} | {short(r['evidence_ids'].replace('; ', ', '), 160)} |")
    recv_count = {}
    for r in rows:
        for a in r["to"].split("; "):
            recv_count[a] = recv_count.get(a, 0) + 1
    L += ["", "## 받는 에이전트별 제안 수", "", "| 받는 에이전트 | 받은 제안 수 |", "|---|---|"]
    for a in AGENTS:
        if a in recv_count:
            L.append(f"| {a} | {recv_count[a]} |")
    open(os.path.join(ROOT, "outputs/discussion/proposals_index.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")
    print("proposals", len(rows), "missing to", [r["proposal_id"] for r in rows if not r["to"]],
          "missing content", [r["proposal_id"] for r in rows if not r["content"]])


if __name__ == "__main__":
    main()
