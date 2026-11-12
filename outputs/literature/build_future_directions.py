#!/usr/bin/env python3
"""Stage 2 Deliverable D builder: outputs/future_directions.md

Usage (project root):
    python3 -I outputs/literature/export_future_directions.py
    python3 -I outputs/literature/export_chains.py
    python3 -I outputs/literature/build_future_directions.py

IDs, Discussion locations, datasets, overlap and research questions are copied
from outputs/literature/chains_index.csv (parsed from each agent's round1.md).
The theme and the short "why now possible" reason per chain are Coordinator
judgements written in THEMES / REASON below.
"""
import collections
import csv
import os
import re

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
AB = {"adversarial-reviewer": "AR", "brain-inspired": "BI", "emotion-theory": "ET",
      "encoding-foundation": "EF", "frontier-ai": "FA", "generative-counterfactual": "GC",
      "geometry-info": "GI", "llm-semantics": "LS", "multimodal-dynamics": "MD",
      "systems-neuro": "SN", "vision-decoding": "VD"}

THEMES = [
    ("T1", "Horikawa 결론의 검증과 해부 (범주 결론, 재현 실패, 차원 수)",
     "AR-D1 ET-C1 ET-C2 GI-C1 SN-Chain2 FA-CH8 ET-C6 ET-C7 GI-C7 MD-Chain1 MD-Chain8"),
    ("T2", "정서 신호와 시각, 의미 내용 신호의 분리",
     "AR-D2 LS-Chain1 VD-R6 GC-CH1 EF-Chain4 FA-CH5 FA-CH6 BI-Chain2 BI-Chain3 BI-Chain6 LS-Chain7 EF-Chain6 GC-CH6"),
    ("T3", "정서 지도, 전이, 동역학 (Ma & Kragel 2026 이후)",
     "BI-Chain1 GI-C2 AR-D3 FA-CH1 BI-Chain7 MD-Chain7 GI-C5 SN-Chain5 MD-Chain4 SN-Chain6 FA-CH3 FA-CH4 GI-C4 GI-C6"),
    ("T4", "라벨 주체와 개인 경험 (본인 보고, peer 합의, 규범, AI)",
     "ET-C4 ET-C5 ET-C8 EF-Chain3 GC-CH5 LS-Chain5 VD-R5 GI-C3 GI-C8 LS-Chain2 MD-Chain5 AR-D4 LS-Chain6"),
    ("T5", "몸과 생리 (자율신경, 내수용, 보고된 생리)",
     "SN-Chain1 LS-Chain4 EF-Chain2 ET-C3"),
    ("T6", "In-silico 뇌와 foundation model의 정서 충실도",
     "EF-Chain1 GC-CH3 EF-Chain7 EF-Chain5 SN-Chain7 FA-CH7 GC-CH7 GC-CH2 VD-R4 VD-R1 AR-D6"),
    ("T7", "소리, 서사, 예측 신호",
     "MD-Chain2 MD-Chain3 GC-CH4 FA-CH2 LS-Chain3 BI-Chain5 BI-Chain4 MD-Chain6"),
    ("T8", "기억, 심상, 반복 제시",
     "VD-R2 VD-R3 SN-Chain4 SN-Chain3"),
    ("T9", "방법론 인프라 (상한, leakage)",
     "AR-D5 AR-D7"),
]

REASON = {
    "AR-D1": "multiverse, specification curve 방법이 정착했고 Westlin 2025 재분석이 비교 대상으로 나옴. raw BIDS가 CC0",
    "AR-D2": "banded ridge와 SEM 신뢰도 보정 방법, 2024~2026 비디오와 VLM feature(원본 보유로 추출 가능)",
    "AR-D3": "ground truth 기반 식별 가능성 점검과 matched-complexity baseline 방법(2023~2024)",
    "AR-D4": "PPI(2023), DSL, alt-test(2025) 등 surrogate 라벨 보정 통계와 MLLM 주석",
    "AR-D5": "피험자 간 상한과 GSN 방법, Emo-FilM 생리 공개, NSD 반복 자료로 보정 가능",
    "AR-D6": "예측 극값 선택, controversial selection, prevalence 추론(2023~2025)",
    "AR-D7": "leakage 분류(2023)와 REFORMS 체크리스트, 원본 보유로 비디오 근접 중복 탐지 가능",
    "BI-Chain1": "successor representation과 경험적 전이 그래프 TEM 재학습. Emo-FilM 1 Hz 50항목 평정으로 방향성 전이 추정 가능",
    "BI-Chain2": "action-conditioned world model(V-JEPA 2), MLLM 행동 경향 주석. Emo-FilM Motivation 10항목",
    "BI-Chain3": "MPathI, DNN 층 분할, recurrent 시각 모형. 원본 보유",
    "BI-Chain4": "distributional TD와 비대칭 PE 신경 분석(2025). Spacetop cue 조작이 공개 데이터에 있음",
    "BI-Chain5": "pymdp, HBI 모형 비교, video world model 예측 분산. 정서 계산 이론의 인간 benchmark가 비어 있음",
    "BI-Chain6": "이중 과제 학습과 lesion, MoE 사전지식(2025~2026)",
    "BI-Chain7": "momentum Kalman filter, leaky integrator. 1 Hz 연속 평정",
    "ET-C1": "반복 없이 피험자 간 cross-decomposition으로 rank별 신뢰 분산 추정(2024), rank별 개인차(2025)",
    "ET-C2": "피험자 간 신뢰 부분공간 추출, GLMsingle 재추정, 2-factor 교차검증",
    "ET-C3": "고차원 시청각-의미 feature(원본 보유)와 Emo-FilM 참가자 생리 공개",
    "ET-C4": "self vs cross-prediction 설계(2024), 신뢰도 보정 논리, Spacetop peer 합의 활용",
    "ET-C5": "분포 라벨과 평정자별 모형. Emo-FilM 평정자별 원자료 공개",
    "ET-C6": "범주 점수 encoding을 가산성 검정으로 전환, 선택 비율 분포 라벨",
    "ET-C7": "crossnobis와 2-factor 추론, 스펙트럼 smoothness 지표",
    "ET-C8": "rank 범위별 신뢰 가능한 개인차 방법(2025). Spacetop 본인 평정",
    "EF-Chain1": "TRIBE v2 공개(2026), modality dropout으로 무음 자극 입력 가능",
    "EF-Chain2": "3모달 비선형 encoder와 피질하 학습 스크립트, Emo-FilM 생리",
    "EF-Chain3": "TRIBE v2의 새 피험자 예측과 짧은 fine-tuning, hyperalignment",
    "EF-Chain4": "기존 자극에서 모델 예측이 갈리는 하위집합을 고르는 controversial selection(2024), 최신 foundation feature",
    "EF-Chain5": "CortexMAE 공개 가중치와 재현 가능한 평가, NeuroSTORM prompt tuning",
    "EF-Chain6": "수백만 자극 screening으로 선택성 검정, RNC의 탐색과 in vivo 검증 결합(2025)",
    "EF-Chain7": "TRIBE v2 modality dropout과 모달리티 ablation 지도",
    "FA-CH1": "정서 라벨 없이 학습한 latent world model(V-JEPA 2), LLM 정서 표상의 인물 모델링 보고(2026)",
    "FA-CH2": "V-JEPA 2 predictor surprise 추출 공개 코드, LLM surprisal nuisance 틀(2026)",
    "FA-CH3": "open VLM 정서 vector와 다모델 공유 정서 부분공간(2026), RepE",
    "FA-CH4": "LLM 내부 appraisal 조작(2025), SAE 인과 feature",
    "FA-CH5": "안정 SAE(RA-SAE), 시공간 contrastive SAE, Universal SAE(2025~2026)",
    "FA-CH6": "정서 무관 정렬로 정서 vector를 운반하는 절차(2026)",
    "FA-CH7": "brain-tuning 절차(2025)",
    "FA-CH8": "식별 가능한 multi-view contrastive, 조건부 contrastive",
    "GC-CH1": "참조 고정 최소 편집(BrainACTIV), Concept Sliders, LivePortrait. 원본 보유",
    "GC-CH2": "RNC 영역 간 공동 제어(2025), NeuroVolve 다중 목표(2025)",
    "GC-CH3": "TRIBE v2 공개, 학습 목록에 4개 데이터셋 없음(같은 자극으로 실측-예측 비교 가능)",
    "GC-CH4": "영화 음향 3-stem 분리, 음향 입력 whole-brain encoder",
    "GC-CH5": "in-silico 기대 반응(TRIBE v2)과 fold 내 교란 회귀",
    "GC-CH6": "controversial stimuli, 결정 경계 표집, model metamer",
    "GC-CH7": "연속 편집과 참조 고정 편집, in-silico 국소 타당성 논의(2026)",
    "GI-C1": "cross-decomposition과 hyperalignment 스펙트럼(2024)",
    "GI-C2": "SR과 다중 할인율, Emo-FilM 1 Hz 전이 추정",
    "GI-C3": "warp hyperalignment / INT, Gromov-Wasserstein 정렬, Spacetop 본인 평정",
    "GI-C4": "rSLDS, Hyper-HMM, CEBRA",
    "GI-C5": "rSLDS 시간상수 추정, CEBRA. Emo-FilM 90 s washout과 EDA",
    "GI-C6": "PID / ΦID로 시너지 직접 정량, SRM",
    "GI-C7": "IB 최적 경계 계산, 공유 정서 부분공간",
    "GI-C8": "INT 개인 tuning, shape metric. Spacetop 다과제",
    "LS-Chain1": "정서 배제 지시로 받은 인간 캡션(Mind captioning 2025), LLM embedding 뇌 정렬(2025)",
    "LS-Chain2": "MLLM 사회 특징 주석(인간 평균과 r 0.79, 2025), 관점 조건부 prompt",
    "LS-Chain3": "공개 LLM probe와 steering, LLM appraisal 파서. Spacetop narratives 텍스트 보유",
    "LS-Chain4": "MLLM 시간 연속 주석, 평정자별 원자료로 라벨 noise 귀무분포",
    "LS-Chain5": "MLLM 평균 관찰자 예측, functional alignment",
    "LS-Chain6": "다국어 LLM / MLLM, GWOT",
    "LS-Chain7": "비디오 분할과 inpainting, MLLM 정서 추정",
    "MD-Chain1": "기술보다 데이터 구조 문제. 블록 길이 변이를 이용한 FIR, 개인 HRF, 순차 HMM",
    "MD-Chain2": "V-JEPA 2, 오디오-비디오 정렬 MLLM, 무학습 surprise 분절(2024)",
    "MD-Chain3": "음원 분리, wav2vec, MERT, 단일모달 정보 제거 residual(2025)",
    "MD-Chain4": "멀티모달 모델의 문맥 길이 sweep(2026), surprise 메모리",
    "MD-Chain5": "Emo-FilM으로 시간축을 검증한 AI 연속 정서 추정, 정서 경계 검출",
    "MD-Chain6": "비디오, 오디오 예측 모델의 불확실성과 놀람, 동적 ISC",
    "MD-Chain7": "동역학 수준 비교 DSA, DynAffect",
    "MD-Chain8": "시각 특징 분해, V-JEPA 2 층별 feature, MLLM 정서 기하",
    "SN-Chain1": "전역 fMRI 신호와 자율신경 결합(2025), 공개 arousal CPM 가중치",
    "SN-Chain2": "전역 성분의 자율신경 기원(2025), 상태 기반 틀, 피질하 atlas",
    "SN-Chain3": "Spacetop 획득 조건, 원본에서 looming 등 프레임 feature 추출, 피질하 atlas",
    "SN-Chain4": "NSD 반복 번호와 간격, 7T amygdala 세분, VLM 정서 추정(AI 추정 라벨)",
    "SN-Chain5": "상태 의존 전환 rSLDS, 정서 관성 메타분석",
    "SN-Chain6": "chronotopic 지도, principal gradient, HCP360으로 데이터셋 결합",
    "SN-Chain7": "휴지기 사전학습 Brain-JEPA, 공개 arousal CPM 기준선",
    "VD-R1": "전뇌 foundation 해독(WAVE), Brain-IT 1시간 적응, C&K와 겹치지 않는 정서 평가기",
    "VD-R2": "지각 decoder의 imagery 일반화(2025~2026). 단 Mind captioning 회상 데이터는 4개 보유 데이터셋 밖",
    "VD-R3": "정서 공간과 CLIP 공간 정렬, 34차원 연속 정서 해독(2026)",
    "VD-R4": "encoder gradient로 diffusion을 유도하는 BrainDiVE",
    "VD-R5": "공유-개인 사상 구조(MindEye2, Brain-IT)",
    "VD-R6": "정서를 쓰지 말라는 지시로 받은 중립 캡션(Mind captioning), 정서 조건 캡션 재작성",
}


def key(r):
    m = re.match(r"([A-Za-z\-]*\s?\d+)", r["chain"])
    cid = m.group(1).replace(" ", "") if m else r["chain"][:6]
    return f"{AB[r['agent']]}-{cid}"


def loc_of(orig):
    locs = re.findall(r"[\[(]([^\[\]()]*?(?:Discussion|Limitations|Conclusion|Results|Methods|Future|단락|절)[^\[\]()]*)[\])]", orig)
    s = "; ".join(locs)
    return (s[:160] + "...") if len(s) > 160 else s


def clean(s, n):
    s = re.sub(r"\*\*|\"|\|", "", s).strip()
    return (s[:n] + "...") if len(s) > n else s


def main():
    chains = list(csv.DictReader(open(os.path.join(ROOT, "outputs/literature/chains_index.csv"), encoding="utf-8")))
    fds = list(csv.DictReader(open(os.path.join(ROOT, "outputs/literature/future_directions_all.csv"), encoding="utf-8")))
    db = {r["uid"]: r for r in csv.DictReader(open(os.path.join(ROOT, "outputs/literature/literature_db.csv"), encoding="utf-8"))}
    bykey = {key(r): r for r in chains}
    assigned = [k for _, _, ks in THEMES for k in ks.split()]
    missing_theme = sorted(set(bykey) - set(assigned))
    unknown_keys = sorted(set(assigned) - set(bykey))
    dup = [k for k, v in collections.Counter(assigned).items() if v > 1]

    st = collections.Counter((r["verified"], r["discussion_read"], r["status"]) for r in fds)
    n_all = len(fds)
    n_cand = sum(v for (ver, dr, s), v in st.items() if ver == "True" and dr == "full_text" and s in ("no", "partially"))
    n_yes = sum(v for (ver, dr, s), v in st.items() if s == "yes")
    n_unk = sum(v for (ver, dr, s), v in st.items() if s in ("unknown", "미확인", "blank"))
    n_nofull = sum(v for (ver, dr, s), v in st.items() if dr != "full_text")

    def norm(i):
        i = i.strip().lower().replace("doi:", "")
        return ("arxiv:" + i.split(":")[1]) if i.startswith("arxiv:") else "doi:" + i
    orig_c = collections.Counter(); unres_c = collections.Counter()
    for r in chains:
        for i in set(filter(None, r["orig_ids"].split("; "))):
            orig_c[norm(i)] += 1
        for i in set(filter(None, r["unres_ids"].split("; "))):
            unres_c[norm(i)] += 1
    not_in_db = sorted(k for k in set(orig_c) | set(unres_c) if k not in db and re.match(r"(doi:10\.|arxiv:\d)", k) and not re.search(r"[^\x00-\x7f]", k))

    L = []
    L += ["# Deliverable D: Discussion & Future-Direction Mining", "",
          "* 작성: Coordinator (Stage 2). 이 파일은 `outputs/literature/build_future_directions.py`가 만든다. 표의 원 논문 ID, Discussion 위치, 데이터셋, overlap, 질문은 각 에이전트 round1.md 6절에서 추출했고(`outputs/literature/chains_index.csv`), 주제 분류와 \"지금 가능해진 이유\" 요약은 Coordinator 판단이다.",
          "* 기준일: 2026-11-12",
          "* 입력: `outputs/literature/literature_db.csv`의 future_directions(논문별), 11개 에이전트의 Discussion-to-Research chain",
          "",
          "## 0. 요약과 선별 방법", "",
          f"1. **전체 future direction:** 문헌 DB의 future_directions는 {n_all}개다(`outputs/literature/future_directions_all.csv`, 한 줄에 하나). 그중 verified 논문이고 본문(full_text)을 읽었으며 already_done이 no 또는 partially인 후보는 **{n_cand}개**다. already_done = yes는 {n_yes}개(제외), unknown이나 미확인은 {n_unk}개, 본문을 읽지 않은 논문에서 나온 항목은 {n_nofull}개다. 본문을 읽지 않은 항목은 CLAUDE.md 5절에 따라 future direction으로 쓰지 않는다.",
          f"2. **선별:** {n_cand}개를 하나씩 재판단하는 대신, 11개 에이전트가 P1 6절에서 만든 **Discussion-to-Research chain {len(chains)}개**를 선별 결과로 쓴다. chain은 \"원 논문 Discussion의 미해결 문제 → 그 뒤의 기술 발전 → 보유 데이터셋 조합 → 새 질문\" 형식이며 원문 위치를 달고 있어, 지침의 선별 기준(2026년 모델이나 보유 데이터셋으로 새로 해결 가능)과 같은 판단을 이미 거쳤다. Coordinator는 chain을 주제 9개로 묶고 \"지금 가능해진 이유\"를 한 줄로 요약했다.",
          "3. **선행 수행 여부:** chain의 already_done 판단은 각 에이전트의 검색 범위 안에서만 유효하다. Stage 3 Round 3와 Stage 4 선행연구 중복 감사에서 다시 확인한다.",
          "4. **데이터:** 사용자 확인으로 4개 데이터셋의 원본 자극을 모두 보유하므로 G1 필요 chain도 실행 가능하다. 단 VD-R2는 4개 보유 데이터셋 밖의 Horikawa 2025 Mind captioning 데이터(OpenNeuro ds005191)가 필요하다.",
          ""]
    if missing_theme or unknown_keys or dup:
        L += [f"> 생성 점검: 주제 미배정 {missing_theme}, 존재하지 않는 키 {unknown_keys}, 중복 배정 {dup}", ""]

    L += ["## 1. 어떤 논문의 미해결 문제가 가장 많이 이어졌는가", "",
          "chain의 Original Finding(출발 논문)과 Unresolved Question(미해결 문제 근거)에 인용된 횟수다. 한 chain이 같은 논문을 여러 번 인용해도 1로 센다.", "",
          "| 논문 | 출발 논문으로 쓴 chain 수 | 미해결 문제 근거로 쓴 chain 수 |", "|---|---|---|"]
    top = sorted(set(orig_c) | set(unres_c), key=lambda k: -(orig_c[k] + unres_c[k]))[:15]
    for k in top:
        cit = db.get(k, {}).get("citation", "(DB에 없음)")
        L.append(f"| {clean(cit, 70)} ({k}) | {orig_c[k]} | {unres_c[k]} |")
    L += ["", "Horikawa 2020(1순위 데이터셋 원 논문), Ma & Kragel 2026(Emo-FilM의 '이미 수행됨' 기준점), Cowen & Keltner 2017, Westlin 2025가 가장 많이 이어졌다. Kragel 2019(EmoNet)는 출발점보다 미해결 문제 근거로 더 많이 쓰였는데, 대부분 Horikawa와 같은 자극으로 학습된 누수 문제를 지적하는 맥락이다.", ""]

    L += ["## 2. 선별한 future direction (주제별)", "",
          "열 설명: **원 논문과 Discussion 위치**는 chain의 Original Finding에 적힌 출처, **지금 가능해진 이유**는 원 논문 당시에는 어려웠지만 2024~2026년 모델, 방법, 공개 데이터로 가능해진 점, **데이터셋**은 chain이 쓰는 4개 데이터셋, **overlap**은 `reference/existing_projects.md`와의 겹침 표시다. 질문은 원문을 줄였으며 전체 문장과 반증 조건은 해당 에이전트 round1.md 6절에 있다.", ""]
    for tid, tname, ks in THEMES:
        L += [f"### {tid}. {tname}", "",
              "| chain | 원 논문과 Discussion 위치 | 지금 가능해진 이유 | 데이터셋 | 질문 (요약) | overlap |",
              "|---|---|---|---|---|---|"]
        for k in ks.split():
            r = bykey.get(k)
            if not r:
                continue
            ids = r["orig_ids"].replace("; ", ", ")
            loc = loc_of(r["orig"])
            L.append(f"| {k} | {ids}{(' / ' + loc) if loc else ''} | {REASON.get(k, '')} | {r['datasets'] or '-'} | {clean(r['rq'], 230)} | {r['overlap'] or '-'} |")
        L.append("")

    L += ["## 3. 서로 다른 논문 두 편의 limitation을 연결해 생긴 질문", "",
          "아래는 chain 중에서 **한 논문의 결과나 한계와 다른 논문의 한계가 맞물려** 질문이 생긴 경우를 Coordinator가 골라 정리한 것이다. 각 쌍의 출처는 해당 chain의 Original Finding과 Unresolved Question 항목이다.", "",
          "| # | 논문 1의 결과 또는 한계 | 논문 2의 한계 | 둘을 연결하면 생기는 질문 | chain |",
          "|---|---|---|---|---|",
          "| 1 | Horikawa 2020 (doi:10.1016/j.isci.2020.101060): 평정이 fMRI 참가자가 아닌 별도 평정자 평균이라는 Limitations 1째 단락 | Westlin 2025 (arXiv:2507.00320): 개인 간 변동이 크다(preprint, 초록과 결과 기준) | 같은 자극에서 본인 보고가 타인 평균보다 그 사람 뇌를 더 잘 설명하는가. 개인 특이 신경 성분이 본인 보고의 편차를 예측하는가 | ET-C4, ET-C8, VD-R5, GC-CH5, EF-Chain3 |",
          "| 2 | Horikawa 2020: emotion 모델이 visual, semantic 모델보다 transmodal 반응을 잘 설명(Discussion 5단락) | Abdel-Ghaffar 2024 (doi:10.1038/s41467-024-49073-8): 의미 효과가 중위 구조 특징일 수 있어 탈상관 자극이 필요(Discussion 4단락) | 의미를 고정하고 정서 단서만 바꾼 편집에서도 emotion 우위 voxel의 반응이 따라 변하는가 | GC-CH1 |",
          "| 3 | Horikawa 2020: 세 모델을 따로 적합해 비교(Results 본문 확인) | Westfall & Yarkoni 2016 (doi:10.1371/journal.pone.0152719): 공변량 측정 오차가 증분 타당도 위양성을 만든다 | 내용 지표를 늘리고 신뢰도를 반영하면 정서 고유 분산은 0으로 수렴하는가, plateau를 유지하는가 | AR-D2 |",
          "| 4 | Ma & Kragel 2026 (doi:10.1038/s41467-025-68240-z): TEM 환경이 대칭 유사도(MDS) 위 균등 무작위 보행(Methods) | doi:10.1073/pnas.1616056114: 정서 전이는 비대칭이며 유사도로 설명되지 않는다(Discussion, 에이전트 인용 기준) | hippocampus-vmPFC 정서 지도는 대칭 유사도가 아니라 방향성 전이 예측(successor representation)을 담는가 | BI-Chain1, GI-C2 |",
          "| 5 | Doerig 2025 (doi:10.1038/s42256-025-01072-0): LLM 캡션 embedding이 고위 시각 반응과 정렬(Discussion 1단락) | Horikawa 2025 Mind captioning (doi:10.1126/sciadv.adw1464): 정서를 쓰지 말라는 지시로 받은 캡션이 있고 의미 feature 해독이 시각 feature보다 강함 | 정서 배제 캡션을 통제한 뒤에도 C&K 규범 정서의 고유 분산이 남는가, 언어로 회복되지 않는 시각 정서 성분이 있는가 | LS-Chain1, VD-R6 |",
          "| 6 | Kragel 2021 (doi:10.1016/j.neuron.2021.06.001): colliculus-pulvinar-amygdala 경로가 혐오 정보를 부호화 | Leem 2026 (arXiv:2607.19327): shortcut 경로가 없으면 조건화가 재현되지 않음(Discussion 2단락) | 피질하 경로는 범주 특이 정보를 싣는가, 그 정보는 얕은 층(저공간주파수) feature로 충분한가 | BI-Chain3 |",
          "| 7 | EmoMind 2026 (arXiv:2605.16739): TRIBE v2 합성 뇌로 대체하면 정서 RSA가 하락(실측과 합성의 자극 집합이 다름) | TRIBE v2 (arXiv:2605.04326): 학습 목록에 4개 데이터셋이 없고 피질하와 개인 readout이 없음 | 같은 자극에서 실측과 in-silico 예측의 정서 구조가 어느 영역, 어느 정서에서 갈라지며 잔차가 정서 평정을 추가로 설명하는가 | GC-CH3, EF-Chain1 |",
          "| 8 | Lettieri 2024 (doi:10.1126/sciadv.adk6840): vmPFC의 모달리티 독립 범주 부호(감각 박탈 집단) | Horikawa 2020: 무음 자극이라 소리 기여를 볼 수 없음(Discussion 마지막 단락) | vmPFC, hippocampus 정서 신호는 대사 언어와 음악 feature를 제거해도 남는가, 무음과 소리 있는 데이터의 정서 RSA는 어떻게 다른가 | MD-Chain3, EF-Chain7 |",
          "| 9 | Chang 2021 (doi:10.1126/sciadv.abf7129): vmPFC 상태의 개인 특이성 | Ma & Kragel 2026: 예측 시계열 유사도 구조가 참가자 간 매우 안정(같은 consensus 표적으로 학습) | vmPFC 개인차는 다른 지도인가, 같은 지도를 지나는 시점과 속도의 차이인가 | GI-C4 |",
          "| 10 | Ke 2025 (doi:10.1371/journal.pcbi.1012994): dynamic FC로 정서 arousal 예측 | Bolt 2025 (doi:10.1038/s41593-025-01945-y): 전역 fMRI 신호가 교감 매개 생리와 결합 | network arousal 판독에서 자율신경-혈관 전역 성분을 빼도 규범 arousal과 appraisal을 예측하는 신경 성분이 남는가 | SN-Chain1 |",
          "| 11 | Jang & Kragel 2025 (doi:10.1523/JNEUROSCI.1436-24.2025): 편도체 encoding model로 자극 합성 | NeuroVolve 2025 (arXiv:2512.00557): amygdala 최대화가 얼굴, 최소화가 건물로 의미 범주 조절이었음 | 얼굴, 신체, 장면 영역 반응을 고정한 제약 아래에서도 amygdala를 움직이는 편집이 있는가 | GC-CH2 |",
          "| 12 | Yazdanpanah 2026 (doi:10.1073/pnas.2513856123): cue 기반 confirmation bias를 행동 수준에서 모델링 | distributional TD (doi:10.1038/s41586-019-1924-6): 비대칭 PE가 채널 집단으로 구현될 수 있음 | confirmation bias는 단일 채널 gain 조절인가, 비대칭 채널 읽기인가, pain과 vicarious pain에서 공유되는가 | BI-Chain4 |",
          "| 13 | Kumar 2023 (doi:10.1038/s41467-023-42241-2), doi:10.1111/cogs.13343: 사건 경계와 예측 오차 | Nguyen 2026 (doi:10.7554/elife.107955): 오차형과 불확실성형 경계의 신경 순서 | 영화의 정서 경계는 다중모달 예측 surprise로 환원되는가, hippocampus 경계 반응을 추가로 설명하는가 | MD-Chain2 |",
          "| 14 | Du 2025 (arXiv:2509.24298): 영어 기반 MLLM 정서 표상(Limitations 2째 단락) | doi:10.1038/s41598-024-65604-1: 정서 의미의 언어 의존성 | 일본어로 판단한 MLLM 정서 표상과 영어로 판단한 표상 중 어느 쪽이 Horikawa 뇌와 더 정렬되는가(참가자 언어는 미확인) | LS-Chain6 |",
          "| 15 | Horikawa 2020 (Discussion 6째 단락): 반복 제시 부재로 설명 안 된 분산 추정 불가 | NSD 반복 자료와 피험자 간 상한 방법(doi:10.1371/journal.pcbi.1006397, doi:10.1093/scan/nsz037) | 피험자 간 상한은 반복 기반 상한을 얼마나 과소, 과대 추정하며 정서 동기 생리가 상한을 얼마나 부풀리는가 | AR-D5 |",
          ""]

    L += ["## 4. 전체 future direction 목록과 상태", "",
          "* 전체 목록: `outputs/literature/future_directions_all.csv` (열: uid, citation, discussion_read, fd_text, section, already_done, status, from_agent, applicable_datasets, axes)",
          "* already_done 상태 분포 (verified 논문, 원 기록 기준):", "",
          "| verified | discussion_read | already_done | 개수 |", "|---|---|---|---|"]
    for (ver, dr, s), v in sorted(st.items(), key=lambda x: -x[1]):
        L.append(f"| {ver} | {dr} | {s} | {v} |")
    L += ["", "* unknown과 미확인으로 남은 항목은 선행 수행 검색을 하지 못한 것이다. Stage 3에서 해당 future direction을 쓰는 조합이 나오면 그때 검색한다.", ""]

    L += ["## 5. 주의와 한계", "",
          "* chain의 질문은 Round 1 독립 탐색 결과다. 서로 비슷한 질문(예: 본인 보고 vs 타인 평균 비교는 ET-C4, ET-C8, EF-Chain3, GC-CH5, LS-Chain5, VD-R5가 각각 제안)은 Stage 3 Round 2에서 합치거나 차별화한다.",
          "* \"지금 가능해진 이유\"의 연도와 모델은 각 chain의 Technological Development 항목에 근거한다. 라이선스(TRIBE v2는 CC BY-NC 4.0 등)는 Deliverable B와 각 에이전트 round1.md 2절을 따른다.",
          "* Westlin 2025는 arXiv preprint이며 재현 실패 보고다. 반대 증거로 확정해 쓰지 않는다.",
          "* EmoNet은 Horikawa와 같은 Cowen & Keltner 비디오로 학습되었으므로 Horikawa 분석에서 feature나 평가기로 쓰는 chain은 누수 통제 조건으로만 쓴다(여러 chain이 이미 명시).",
          f"* chain에 인용되었지만 문헌 DB에 없는 식별자: {', '.join(not_in_db) if not_in_db else '없음'}. 이 식별자는 verified로 확인되지 않았으므로 근거로 쓸 때 재확인이 필요하다.",
          ""]
    with open(os.path.join(ROOT, "outputs/future_directions.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(L))
    print("written; chains", len(chains), "assigned", len(assigned), "missing_theme", missing_theme, "unknown", unknown_keys, "dup", dup, "not_in_db", not_in_db)


if __name__ == "__main__":
    main()
