#!/usr/bin/env python3
"""Stage 3: tally Round 2 responses (수용/수정/반박) and mentions per proposal.

Response source : section "받은 제안에 대한 응답" of outputs/agents/*/round2.md
Mention source  : every outputs/agents/*/round2.md, counting occurrences of a proposal ID outside
                  the sender's own file. (첫 실행은 round3_reviews.md까지 세어 Round 3 배정 제안이 평균 약 1.1점을
                  더 받았다. adversarial-reviewer 지적으로 지시문 기준 "Round 2에서"에 맞게 정정. 첫 실행 재현:
                  TALLY_INCLUDE_R3=1)
Top-10 rule (prompts/stage3 2절 3번 "가장 많이 수용되거나 언급된"):
    score = (#수용) + (#수정) * 0.5 + (#distinct files mentioning, excluding sender) * 0.5
Output: outputs/discussion/responses_tally.csv, outputs/discussion/top10_for_review.md
Usage : python3 -I outputs/discussion/tally_responses.py
"""
import collections
import csv
import glob
import os
import re

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
VERDICT = {"수용": "accept", "수정": "modify", "반박": "rebut"}


def main():
    props = {r["proposal_id"]: r for r in csv.DictReader(open(os.path.join(ROOT, "outputs/discussion/proposals_index.csv"), encoding="utf-8"))}
    verdicts = collections.defaultdict(list)  # pid -> [(responder, verdict)]
    for path in glob.glob(os.path.join(ROOT, "outputs/agents/*/round2.md")):
        agent = path.split(os.sep)[-2]
        text = open(path, encoding="utf-8").read()
        m = re.search(r"(?ms)^## \d*\.?\s*받은 제안에 대한 응답.*?(?=^## |\Z)", text)
        sec = m.group(0) if m else ""
        seen = set()
        for line in sec.splitlines():
            s = line.strip()
            if not (s.startswith("#") or s.startswith("|") or s.startswith("**")):
                continue
            idm = re.search(r"\b([A-Z]{2}-P\d+)\b", s)
            v = re.search(r"(수용|수정|반박)", s)
            if not idm or not v or s.startswith("|---"):
                continue
            pid = idm.group(1)
            if pid in props and props[pid]["from"] != agent and (pid, agent) not in seen:
                seen.add((pid, agent))
                verdicts[pid].append((agent, VERDICT[v.group(1)]))
    mentions = collections.defaultdict(set)
    files = glob.glob(os.path.join(ROOT, "outputs/agents/*/round2.md"))
    if os.environ.get("TALLY_INCLUDE_R3") == "1":  # 첫 실행(정정 전) 재현용
        files += glob.glob(os.path.join(ROOT, "outputs/agents/*/round3_reviews.md"))
    for path in files:
        agent = path.split(os.sep)[-2]
        text = open(path, encoding="utf-8").read()
        for pid in set(re.findall(r"\b([A-Z]{2}-P\d+)\b", text)):
            if pid in props and props[pid]["from"] != agent:
                mentions[pid].add(f"{agent}/{os.path.basename(path)}")
    rows = []
    for pid, p in props.items():
        vs = verdicts.get(pid, [])
        c = collections.Counter(v for _, v in vs)
        score = c["accept"] + 0.5 * c["modify"] + 0.5 * len(mentions[pid])
        rows.append({"proposal_id": pid, "from": p["from"], "to": p["to"], "title": p["title"][:80],
                     "accept": c["accept"], "modify": c["modify"], "rebut": c["rebut"],
                     "responders": "; ".join(f"{a}:{v}" for a, v in vs),
                     "mention_files": len(mentions[pid]), "score": score})
    rows.sort(key=lambda r: (-r["score"], r["proposal_id"]))
    with open(os.path.join(ROOT, "outputs/discussion/responses_tally.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    tot = collections.Counter()
    for r in rows:
        tot["accept"] += r["accept"]; tot["modify"] += r["modify"]; tot["rebut"] += r["rebut"]
    no_resp = [r["proposal_id"] for r in rows if not (r["accept"] or r["modify"] or r["rebut"])]
    L = ["# Round 2 응답 집계와 상위 10개 (adversarial-reviewer 검토 대상)", "",
         "* 생성: `python3 -I outputs/discussion/tally_responses.py`",
         f"* 응답 집계: 수용 {tot['accept']}, 수정 {tot['modify']}, 반박 {tot['rebut']}. 응답이 기록되지 않은 제안: {len(no_resp)}개 {' '.join(no_resp)}",
         "* 점수 = 수용 수 + 0.5 x 수정 수 + 0.5 x (보낸 에이전트 밖에서 그 제안 ID를 언급한 파일 수). '가장 많이 수용되거나 언급된' 기준을 하나의 점수로 합친 Coordinator 규칙이다.", "",
         "## 상위 10개", "", "| 순위 | 제안 | 보낸 → 받는 | 요약 | 수용 | 수정 | 반박 | 언급 파일 수 | 점수 |", "|---|---|---|---|---|---|---|---|---|"]
    for i, r in enumerate(rows[:10], 1):
        L.append(f"| {i} | {r['proposal_id']} | {r['from']} → {r['to']} | {r['title'].replace('|', '/')} | {r['accept']} | {r['modify']} | {r['rebut']} | {r['mention_files']} | {r['score']:.1f} |")
    L += ["", "## 11~25위", "", "| 순위 | 제안 | 수용 | 수정 | 반박 | 언급 파일 수 | 점수 |", "|---|---|---|---|---|---|---|"]
    for i, r in enumerate(rows[10:25], 11):
        L.append(f"| {i} | {r['proposal_id']} | {r['accept']} | {r['modify']} | {r['rebut']} | {r['mention_files']} | {r['score']:.1f} |")
    open(os.path.join(ROOT, "outputs/discussion/top10_for_review.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")
    print("verdicts", dict(tot), "no response", len(no_resp))
    for r in rows[:12]:
        print(r["proposal_id"], r["accept"], r["modify"], r["rebut"], r["mention_files"], r["score"])


if __name__ == "__main__":
    main()
