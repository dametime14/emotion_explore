#!/usr/bin/env python3
"""Stage 2 Deliverable C: merge all agent literature records into one database.

Usage (from the project root):
    python3 -I outputs/literature/merge.py

Inputs : outputs/agents/*/literature*.jsonl
Outputs: outputs/literature/literature_db.csv
         outputs/literature/stats.md
         outputs/literature/merge_log.md   (parse errors, duplicate groups)

Dedup keys (prompts/stage2_axes_literature.md 2절): DOI, arXiv ID, normalized title.
Records sharing any key are merged (union-find). future_directions, axes,
applicable_datasets and added_by are unioned.

Verification rule (CLAUDE.md 5절 + Stage 1 보완):
    verified  = verified_by is one of doi.org / crossref / pubmed / arxiv /
                openreview / publisher (direct identifier route)
    otherwise = not verified (e.g. "search_index", "unverified", "none ...").
A merged record is verified if any of its source records is verified.
"""
import csv
import glob
import json
import os
import re
import sys
import unicodedata
from collections import Counter, defaultdict

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUT_DIR = os.path.join(ROOT, "outputs", "literature")

VERIFIED_TOKENS = ("doi.org", "crossref", "pubmed", "arxiv", "openreview", "publisher")
DISC_RANK = {"full_text": 3, "abstract_only": 2, "search_summary": 1, "no": 0}
ALREADY_RANK = {"yes": 2, "partially": 1, "no": 0}


def norm_text(s):
    s = unicodedata.normalize("NFKC", str(s or "")).lower()
    s = re.sub(r"[^0-9a-z가-힣]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def is_verified(vb):
    v = str(vb or "").strip().lower()
    if not v or "search" in v or "unverified" in v or v.startswith("none"):
        return False
    return any(v.startswith(t) or v == t for t in VERIFIED_TOKENS)


DOI_RE = re.compile(r"10\.\d{4,9}/[^\s\"<>|]+", re.I)
ARXIV_RE = re.compile(r"(?:arxiv[:/\s]*|abs/|pdf/)(\d{4}\.\d{4,5})(?:v\d+)?", re.I)
ARXIV_BARE_RE = re.compile(r"^(\d{4}\.\d{4,5})(?:v\d+)?$")


def extract_keys(rec):
    """Return (doi, arxiv) found in id / url fields."""
    doi, arx = None, None
    for field in ("id", "url", "doi"):
        val = str(rec.get(field) or "")
        if not doi:
            m = DOI_RE.search(val)
            if m:
                d = m.group(0).rstrip(".,;)").lower()
                # arXiv-assigned DOIs map to the arXiv ID
                m2 = re.match(r"10\.48550/arxiv\.(\d{4}\.\d{4,5})", d)
                if m2:
                    arx = arx or m2.group(1)
                else:
                    doi = d
        if not arx:
            m = ARXIV_RE.search(val) or ARXIV_BARE_RE.match(val.strip())
            if m:
                arx = m.group(1)
    if not arx:
        # published versions sometimes cite their preprint inside the citation text,
        # e.g. "... similarly to humans (arXiv:2301.10297)"
        m = re.search(r"arxiv[:\s]*(\d{4}\.\d{4,5})", str(rec.get("citation") or ""), re.I)
        if m:
            arx = m.group(1)
    return doi, arx


def title_from_citation(cit):
    """citation format is '저자, 연도, 제목' (CLAUDE.md 5절)."""
    cit = str(cit or "")
    m = re.search(r"(?:^|[,(\s])((?:19|20)\d{2})[a-z]?\)?\s*[,.:]\s*(.+)$", cit)
    title = m.group(2) if m else cit
    title = re.split(r"\.\s+(?:[A-Z][A-Za-z ]+\s\d|In |Proc)", title)[0]
    return norm_text(title)


def as_list(v):
    if v is None:
        return []
    if isinstance(v, list):
        return [x for x in v if x not in (None, "")]
    if isinstance(v, str):
        return [x.strip() for x in re.split(r"[;,/]", v) if x.strip()]
    return [v]


def as_num(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def load_records():
    recs, errors = [], []
    pattern = os.path.join(ROOT, "outputs", "agents", "*", "literature*.jsonl")
    for path in sorted(glob.glob(pattern)):
        agent_dir = os.path.basename(os.path.dirname(path))
        rel = os.path.relpath(path, ROOT)
        with open(path, encoding="utf-8") as fh:
            for ln, line in enumerate(fh, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    r = json.loads(line)
                except json.JSONDecodeError as e:
                    errors.append(f"{rel}:{ln}: {e}")
                    continue
                if not isinstance(r, dict):
                    errors.append(f"{rel}:{ln}: not an object")
                    continue
                r["_src"] = f"{rel}:{ln}"
                r["_agent_dir"] = agent_dir
                recs.append(r)
    return recs, errors


class DSU:
    def __init__(self, n):
        self.p = list(range(n))

    def find(self, x):
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            self.p[rb] = ra


def merge_group(group):
    group = sorted(group, key=lambda r: (not is_verified(r.get("verified_by")),
                                         -DISC_RANK.get(str(r.get("discussion_read")), -1)))
    base = group[0]
    out = {}
    dois = sorted({k for r in group for k in [extract_keys(r)[0]] if k})
    arxs = sorted({k for r in group for k in [extract_keys(r)[1]] if k})
    out["uid"] = (f"doi:{dois[0]}" if dois else f"arxiv:{arxs[0]}" if arxs
                  else f"title:{title_from_citation(base.get('citation'))[:80]}")
    out["id"] = base.get("id", "")
    out["all_ids"] = "; ".join(sorted({str(r.get("id")) for r in group if r.get("id")}))
    out["doi"] = "; ".join(dois)
    out["arxiv"] = "; ".join(arxs)
    for f in ("citation", "venue", "url", "domain", "original_question", "dataset_paradigm",
              "model_method", "main_findings", "whats_new", "limitations",
              "transfer_to_affective_neuro"):
        vals = [str(r.get(f) or "").strip() for r in group]
        out[f] = next((v for v in vals if v), "")
    years = [as_num(r.get("year")) for r in group if as_num(r.get("year"))]
    out["year"] = int(years[0]) if years else ""
    out["verified"] = any(is_verified(r.get("verified_by")) for r in group)
    vbs = [str(r.get("verified_by")) for r in group if r.get("verified_by")]
    out["verified_by"] = "; ".join(sorted(set(vbs)))
    disc = max((str(r.get("discussion_read", "no")) for r in group),
               key=lambda d: DISC_RANK.get(d, -1))
    out["discussion_read"] = disc
    axes = sorted({str(a).strip().upper() for r in group for a in as_list(r.get("axes"))})
    out["axes"] = "; ".join(axes)
    ds = sorted({str(a).strip() for r in group for a in as_list(r.get("applicable_datasets"))})
    out["applicable_datasets"] = "; ".join(ds)
    agents = sorted({str(r.get("added_by") or r["_agent_dir"]).strip() for r in group}
                    | {r["_agent_dir"] for r in group})
    out["added_by"] = "; ".join(agents)
    fds, seen = [], set()
    for r in group:
        for fd in (r.get("future_directions") or []):
            if isinstance(fd, str):
                fd = {"text": fd, "section": "", "already_done": ""}
            if not isinstance(fd, dict):
                continue
            key = norm_text(fd.get("text"))[:200]
            if key and key not in seen:
                seen.add(key)
                fd = dict(fd)
                fd["from"] = r["_agent_dir"]
                fds.append(fd)
    out["future_directions"] = json.dumps(fds, ensure_ascii=False)
    out["n_future_directions"] = len(fds)
    for f in ("relevance", "novelty", "feasibility"):
        nums = [as_num(r.get(f)) for r in group if as_num(r.get(f)) is not None]
        out[f] = max(nums) if nums else ""
    out["n_sources"] = len(group)
    out["sources"] = "; ".join(r["_src"] for r in group)
    return out


def main():
    recs, errors = load_records()
    n = len(recs)
    dsu = DSU(n)
    idx_by_key = {}
    for i, r in enumerate(recs):
        doi, arx = extract_keys(r)
        title = title_from_citation(r.get("citation"))
        keys = []
        if doi:
            keys.append(("doi", doi))
        if arx:
            keys.append(("arxiv", arx))
        if title and len(title) >= 20:
            keys.append(("title", title))
        for k in keys:
            if k in idx_by_key:
                dsu.union(idx_by_key[k], i)
            else:
                idx_by_key[k] = i
    groups = defaultdict(list)
    for i, r in enumerate(recs):
        groups[dsu.find(i)].append(r)
    merged = [merge_group(g) for g in groups.values()]
    merged.sort(key=lambda m: (not m["verified"], str(m["year"]), m["uid"]))

    os.makedirs(OUT_DIR, exist_ok=True)
    cols = ["uid", "id", "all_ids", "doi", "arxiv", "citation", "year", "venue", "url",
            "verified", "verified_by", "discussion_read", "axes", "domain",
            "original_question", "dataset_paradigm", "model_method", "main_findings",
            "whats_new", "limitations", "n_future_directions", "future_directions",
            "transfer_to_affective_neuro", "applicable_datasets", "relevance", "novelty",
            "feasibility", "added_by", "n_sources", "sources"]
    with open(os.path.join(OUT_DIR, "literature_db.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=cols)
        w.writeheader()
        for m in merged:
            w.writerow({c: m.get(c, "") for c in cols})

    ver = [m for m in merged if m["verified"]]
    axis_c = Counter(a for m in ver for a in m["axes"].split("; ") if a)
    axis_all = Counter(a for m in merged for a in m["axes"].split("; ") if a)
    year_c = Counter(m["year"] for m in ver)
    disc_c = Counter(m["discussion_read"] for m in ver)
    agent_c = Counter(a for m in ver for a in m["added_by"].split("; ") if a)
    agent_raw = Counter(r["_agent_dir"] for r in recs)
    vb_raw = Counter("verified" if is_verified(r.get("verified_by")) else "not verified" for r in recs)
    fd_status = Counter()
    for m in ver:
        for fd in json.loads(m["future_directions"]):
            s = str(fd.get("already_done", "")).split(" ")[0].strip().lower() or "(blank)"
            fd_status[s] += 1

    def table(counter, head, keyorder=None):
        keys = keyorder or sorted(counter, key=lambda k: (-counter[k], str(k)))
        rows = [f"| {head} | 편수 |", "|---|---|"]
        rows += [f"| {k} | {counter[k]} |" for k in keys if counter.get(k)]
        return "\n".join(rows)

    axes_order = [chr(c) for c in range(ord("A"), ord("T") + 1)]
    extra_axes = sorted(k for k in axis_all if k not in axes_order)
    lines = [
        "# Literature Statistics (Deliverable C)",
        "",
        "* 생성: `python3 -I outputs/literature/merge.py` (자동 생성 파일, 직접 고치지 말 것)",
        f"* 입력 레코드: {n}개 (파싱 오류 {len(errors)}개), 입력 파일: `outputs/agents/*/literature*.jsonl`",
        f"* 원자료 기준 verified 표기: {vb_raw['verified']}개, 미검증(search_index 등): {vb_raw['not verified']}개",
        f"* 중복 제거 후 고유 논문: **{len(merged)}편**",
        f"* **verified 고유 논문: {len(ver)}편** (식별자 경로 doi.org / crossref / pubmed / arxiv / openreview / publisher로 확인된 것만)",
        f"* 미검증 고유 논문: {len(merged) - len(ver)}편 (verified 집계에서 제외, DB에는 `verified=False`로 남김)",
        "",
        "## Axis별 verified 논문 수 (한 논문이 여러 Axis에 속할 수 있음)",
        "",
        "| Axis | verified | 전체(미검증 포함) |",
        "|---|---|---|",
    ]
    lines += [f"| {a} | {axis_c.get(a, 0)} | {axis_all.get(a, 0)} |" for a in axes_order + extra_axes]
    lines += ["", "## 연도 분포 (verified)", "",
              table(year_c, "연도", sorted(year_c, key=lambda y: str(y))), "",
              "## discussion_read 분포 (verified)", "",
              table(disc_c, "discussion_read", ["full_text", "abstract_only", "search_summary", "no"]
                    + sorted(k for k in disc_c if k not in DISC_RANK)), "",
              "## 담당 에이전트별 verified 고유 논문 수 (중복 논문은 기여한 모든 에이전트에 집계)", "",
              table(agent_c, "에이전트"), "",
              "## 에이전트별 원 레코드 수 (중복 제거 전, 미검증 포함)", "",
              table(agent_raw, "에이전트 폴더"), "",
              "## future_directions의 already_done 분포 (verified 논문)", "",
              table(fd_status, "already_done"), ""]
    with open(os.path.join(OUT_DIR, "stats.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))

    dup_groups = [g for g in groups.values() if len(g) > 1]
    log = ["# merge log", "", f"* parse errors: {len(errors)}"]
    log += [f"  * {e}" for e in errors]
    log += ["", f"* duplicate groups merged: {len(dup_groups)}", ""]
    for g in dup_groups:
        log.append("* " + " | ".join(f"{r.get('id')} ({r['_agent_dir']})" for r in g))
    with open(os.path.join(OUT_DIR, "merge_log.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(log) + "\n")

    print(f"records={n} parse_errors={len(errors)} unique={len(merged)} verified_unique={len(ver)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
