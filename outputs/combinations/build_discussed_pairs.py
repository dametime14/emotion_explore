#!/usr/bin/env python3
"""Stage 3 3절 1번: outputs/combinations/discussed_pairs.md

Axis combinations already discussed in Rounds 1~3:
  * Round 1: Discussion-to-Research chains (outputs/literature/chains_index.csv), axes
    assigned per Deliverable D theme (THEME_AXES below, Coordinator mapping) plus the
    sending agent's primary axes.
  * Round 2: proposals' "관련 Axis" (outputs/discussion/proposals_index.csv).
  * Round 3: revised proposals' axes if reviewers wrote "관련 Axis" lines in
    outputs/agents/*/round3_reviews.md.
Only the 25 axis letters A~W (X, Y folded into R, A) are counted.

Usage: python3 -I outputs/combinations/build_discussed_pairs.py
"""
import collections
import csv
import glob
import itertools
import os
import re

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
VALID = set("ABCDEFGHIJKLMNOPQRSTUVW")
TYPE = {**{a: "Construct" for a in "ABCDVW"}, **{a: "Neural" for a in "EFO"},
        **{a: "Model & Method" for a in "GHIJLMN"}, **{a: "Structure" for a in "KR"},
        **{a: "Inference" for a in "PQSTU"}}
PRIMARY = {"emotion-theory": "AQ", "vision-decoding": "BG", "encoding-foundation": "FHS",
           "multimodal-dynamics": "DM", "frontier-ai": "IJR", "geometry-info": "KO",
           "systems-neuro": "E", "generative-counterfactual": "LP", "llm-semantics": "C",
           "brain-inspired": "N", "adversarial-reviewer": "T"}
# Deliverable D 주제별로 chain이 다룬 Axis (Coordinator mapping)
THEME_AXES = {
    "T1": "AKOQT", "T2": "BCHLP", "T3": "DKNE", "T4": "UOAQ", "T5": "EAH",
    "T6": "FHLS", "T7": "MDCN", "T8": "WGE", "T9": "QTS",
}


def axes_of(text):
    text = re.sub(r"\([^)]*\)", "", text or "")
    return sorted({c for c in re.findall(r"\b([A-W])\b", text) if c in VALID})


def chain_themes():
    """map chain key -> theme from build_future_directions.THEMES"""
    src = open(os.path.join(ROOT, "outputs/literature/build_future_directions.py"), encoding="utf-8").read()
    themes = {}
    for tid, _, ks in re.findall(r'\("(T\d)", "([^"]+)",\s*"([^"]+)"\)', src):
        for k in ks.split():
            themes[k] = tid
    return themes


def main():
    sets = []  # (source, id, axes)
    themes = chain_themes()
    AB = {"adversarial-reviewer": "AR", "brain-inspired": "BI", "emotion-theory": "ET", "encoding-foundation": "EF",
          "frontier-ai": "FA", "generative-counterfactual": "GC", "geometry-info": "GI", "llm-semantics": "LS",
          "multimodal-dynamics": "MD", "systems-neuro": "SN", "vision-decoding": "VD"}
    for r in csv.DictReader(open(os.path.join(ROOT, "outputs/literature/chains_index.csv"), encoding="utf-8")):
        m = re.match(r"([A-Za-z\-]*\s?\d+)", r["chain"])
        key = f"{AB[r['agent']]}-{m.group(1).replace(' ', '') if m else r['chain'][:6]}"
        ax = set(PRIMARY[r["agent"]]) | set(THEME_AXES.get(themes.get(key, ""), ""))
        sets.append(("R1", key, sorted(ax & VALID)))
    for r in csv.DictReader(open(os.path.join(ROOT, "outputs/discussion/proposals_index.csv"), encoding="utf-8")):
        ax = axes_of(r["axes"])
        if ax:
            sets.append(("R2", r["proposal_id"], ax))
    for path in glob.glob(os.path.join(ROOT, "outputs/agents/*/round3_reviews.md")):
        agent = path.split(os.sep)[-2]
        for i, m in enumerate(re.finditer(r"(?im)관련 Axis[^:：\n]*[:：]\s*(.+)$", open(path, encoding="utf-8").read())):
            ax = axes_of(m.group(1))
            if len(ax) >= 2:
                sets.append(("R3", f"{agent}#{i+1}", ax))
    pair_c, tri_c = collections.Counter(), collections.Counter()
    pair_src = collections.defaultdict(set)
    for src, sid, ax in sets:
        for p in itertools.combinations(ax, 2):
            pair_c[p] += 1
            pair_src[p].add(src)
        for t in itertools.combinations(ax, 3):
            tri_c[t] += 1
    all_pairs = list(itertools.combinations(sorted(VALID), 2))
    undiscussed = [p for p in all_pairs if p not in pair_c]
    cross_type_undiscussed = [p for p in undiscussed if TYPE[p[0]] != TYPE[p[1]]]
    L = ["# 이미 논의된 Axis 조합 (discussed_pairs)", "",
         "* 생성: `python3 -I outputs/combinations/build_discussed_pairs.py`",
         f"* 입력: Round 1 chain {sum(1 for s in sets if s[0]=='R1')}개(주제별 Axis 매핑, Coordinator 판단), Round 2 제안 {sum(1 for s in sets if s[0]=='R2')}개(제안의 '관련 Axis'), Round 3 수정안 {sum(1 for s in sets if s[0]=='R3')}개",
         "* Axis는 A~W 23개(X는 R, Y는 A에 포함). Round 1 chain의 Axis는 chain이 속한 Deliverable D 주제와 보낸 에이전트의 담당 Axis로 근사했으므로 과대 집계될 수 있다.", "",
         f"## 요약", "",
         f"* 가능한 2개 조합 {len(all_pairs)}개 중 논의된 것 {len(pair_c)}개, 논의되지 않은 것 {len(undiscussed)}개(그중 서로 다른 유형끼리 {len(cross_type_undiscussed)}개)",
         f"* 논의된 3개 조합: {len(tri_c)}개", "",
         "## 논의되지 않은 2개 조합 (서로 다른 유형, Round 4 후보)", "",
         ", ".join(f"{a}+{b}" for a, b in cross_type_undiscussed) or "(없음)", "",
         "## 가장 많이 논의된 2개 조합 (상위 40)", "", "| 조합 | 횟수 | 등장 라운드 |", "|---|---|---|"]
    for p, c in pair_c.most_common(40):
        L.append(f"| {p[0]}+{p[1]} | {c} | {', '.join(sorted(pair_src[p]))} |")
    L += ["", "## 적게 논의된 2개 조합 (1~2회)", "",
          ", ".join(f"{a}+{b}({c})" for (a, b), c in sorted(pair_c.items()) if c <= 2) or "(없음)", "",
          "## 가장 많이 논의된 3개 조합 (상위 40)", "", "| 조합 | 횟수 |", "|---|---|"]
    for t, c in tri_c.most_common(40):
        L.append(f"| {'+'.join(t)} | {c} |")
    L += ["", "## Axis별 등장 횟수", "", "| Axis | 유형 | 등장한 조합 수 |", "|---|---|---|"]
    ax_c = collections.Counter(a for _, _, ax in sets for a in ax)
    for a in sorted(VALID):
        L.append(f"| {a} | {TYPE[a]} | {ax_c[a]} |")
    with open(os.path.join(ROOT, "outputs/combinations/discussed_pairs.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(L) + "\n")
    with open(os.path.join(ROOT, "outputs/combinations/discussed_sets.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["round", "id", "axes"])
        for s in sets:
            w.writerow([s[0], s[1], "+".join(s[2])])
    print("sets", len(sets), "pairs discussed", len(pair_c), "undiscussed cross-type", len(cross_type_undiscussed))


if __name__ == "__main__":
    main()
