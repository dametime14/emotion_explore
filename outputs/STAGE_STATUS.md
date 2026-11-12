# STAGE STATUS

## Stage 1: Dataset Forensic Audit

* 상태: **완료** (2026-11-12). Stage 2는 사용자 확인 전까지 시작하지 않는다.
* 산출물: Deliverable A

| 파일 | 내용 |
|---|---|
| `outputs/stage1/dataset_intelligence_report.md` | **Deliverable A.** 4개 데이터셋 비교표, Gate 종합표, Cross-dataset Compatibility(단계형), 장점과 한계, 연구 기회, 미확인 항목 전체 목록, 검증 반영 기록 |
| `outputs/stage1/gate_decision.md` | 데이터셋별 G1/G2/G3 판정과 근거, Horikawa G1의 영향과 대안, 모델 기반 연구 가능 여부, 사용자 결정 사항 |
| `outputs/stage1/dataset_Horikawa.md` | Horikawa 감사 보고서 (8절 구조, 맨 위에 검증 반영 주석) |
| `outputs/stage1/dataset_EmoFilM.md` | Emo-FilM 감사 보고서 |
| `outputs/stage1/dataset_Spacetop.md` | Spacetop 감사 보고서 |
| `outputs/stage1/dataset_NSD.md` | NSD 감사 보고서 |
| `outputs/stage1/environment_gaps.md` | 우리 환경 정보 빈칸 목록과 실행 환경 기록 |
| `outputs/agents/dataset-auditor/literature_{Horikawa,EmoFilM,Spacetop,NSD}.jsonl` | 문헌 기록 57편 (verified 38, search_index 19) |
| `outputs/agents/adversarial-reviewer/stage1_audit.md` | 사실 검증 결과 (주장별 대조, 인용 표본 16편, 이견 기록) |

### 실행 방식 (사실 기록)

* `dataset-auditor` 4개(데이터셋별)를 병렬로, 이어서 `adversarial-reviewer` 1개를 실행했다.
* `.claude/agents/`의 커스텀 에이전트 타입이 이번 세션에 등록되지 않아(세션 시작 후 파일이 추가됨), 각 역할은 `general-purpose` 에이전트가 `CLAUDE.md`와 해당 `.claude/agents/<이름>.md`를 직접 읽고 그 지침을 따르는 방식으로 실행했다. 실제로 독립된 에이전트 5개가 실행되었다.
* 셸과 WebFetch의 외부 접근이 대부분 차단되어, 검증은 PubMed MCP(PMC 전문 포함), WebSearch, GitHub 공개 저장소 git clone(OpenNeuro 미러 메타데이터, 저자 코드)으로 했다. 대용량 데이터 본체(영상, NIfTI)는 내려받지 않았다.

### 검증된 것

* 4개 데이터셋의 서지, 피험자 수, 스캐너와 획득 파라미터, 공개 저장소 ID와 라이선스, 라벨 구조와 평정 주체 (감사 에이전트와 검증 에이전트가 각각 원 출처로 확인)
* Horikawa 원자료가 2020-04-24부터 OpenNeuro ds002425에 CC0로 공개되어 있었다는 사실 (출발점 정보의 "2026년 4월 공개"와 다름)
* Kragel 연구실 2026 연구 서지: Ma & Kragel (2026), Nat Commun 17:1518, doi:10.1038/s41467-025-68240-z (29명, 50개 항목 중 17개 사용)
* Spacetop 원본 자극의 공개 위치(git-annex 기록상 공개 S3), 생리 데이터 미공개, alignvideo 평정 구조와 결측률(응답 48.7%)
* NSD에 기본 정서 라벨이 없고 nsdmeadows 100장만 있다는 사실(2차 본문 기준)
* 인용 표본 16편: 식별자 오류 0, 내용 오류 0, 표기 오류 3 (전부 수정)

### 미확인인 것 (주요 항목, 전체는 Deliverable A 7절의 42개 항목)

* 우리 환경의 데이터 경로와 원본 자극 보유 여부 (네 데이터셋 모두)
* Horikawa 비디오 요청 양식의 이용 조건, Mendeley 예치본 내용, figshare 라이선스
* Emo-FilM 절단 정보 파일 내용, 영화별 CC 조항, 논문 Table 1과 Supplementary
* Spacetop 영상의 원 출처와 저작권, 생리와 설문의 공개 경로, N=101 산정 기준
* NSD Terms 원문, DAA 승인 방식, nsdmeadows 지시문
* Cowen & Keltner (2017), Westlin (2025), NSD 원 논문의 본문
* search_index 19편의 식별자 경로 직접 확인

### Gate 요약

| 데이터셋 | G1 원본 자극 | G2 fMRI | G3 라벨 |
|---|---|---|---|
| Horikawa | 요청 필요 (Google Form) | 사용 가능 | 공개, 별도 평정자 |
| Emo-FilM | 공개 재료로 재구성 가능성 높음 (확인 필요) | 사용 가능 | 공개, 별도 평정자 |
| Spacetop | 공개 다운로드 가능 (저작권 확인 필요) | 사용 가능 | 공개, 참가자 본인 사후 평정 |
| NSD | 약관(DAA) 동의 절차 필요 | 사용 가능 | 정서 라벨 사실상 없음 (100장) |

---

## 사용자 확인 필요 (Stage 2 시작 전)

### A. 환경 정보 (`reference/datasets_and_resources.md` 1절, 6칸 모두 공란)
1. 데이터 위치 (Horikawa, Emo-FilM, Spacetop, NSD)
2. 원본 자극 파일 보유 여부 (데이터셋별)
3. 이미 추출해 둔 feature, embedding
4. 계산 자원
5. 사용 가능한 pretrained checkpoint
6. 제약 (마감, 데이터 사용 동의 범위)

### B. Gate 관련 결정
7. **Horikawa 원본 비디오:** 연구실(EmoViS는 Horikawa 2020 사용, EmoBrain은 V-JEPA2 사용)이 이미 비디오나 추출 feature를 보유하고 있는가? 없다면 Cowen 연구실 Google Form으로 요청할 것인가?
8. **Horikawa 1순위 유지 여부:** 데이터가 2020년부터 공개되어 재분석이 여러 편 있고(Westlin 2025 preprint의 재현 실패 보고 포함), 5명, 반복 제시 없음, 무음이라는 한계가 확인되었다. Horikawa를 계속 1순위로 둘지, 모델 기반 연구의 1순위를 Spacetop 또는 Emo-FilM으로 옮길지. (Coordinator 잠정 권고: 보유 여부를 먼저 확인하고, Horikawa를 최우선으로 유지하되 Stage 2에서 질문마다 "G1 필요 여부"를 표시)
9. **NSD:** Data Access Agreement를 이미 제출했는가?
10. **Emo-FilM:** 연구실의 Emo-FilM 연구 계획이 이미 영화 편집본을 확보했는가?
11. **Spacetop 생리 데이터:** 공개본에 없는 EDA/PPG를 저자에게 요청할 것인가?

### C. 지침 파일과 실행 환경
12. **`reference/` 정정:** `datasets_and_resources.md` 2.1절의 "2026년 4월 공개", `starting_papers.md` 특별 지시의 "2026년에 공개되었으므로"를 확인된 사실(2020년 OpenNeuro 공개, 2026-04는 Mendeley 예치)로 고칠지.
13. **`reference/existing_projects.md`:** "[사용자 확인 필요]" 표시가 남아 있다. 세 프로젝트 요약이 현재 상태와 맞는지.
14. **네트워크 허용:** Stage 2는 문헌 본문 확인이 핵심인데 doi.org, arxiv.org, nature.com, openneuro.org, data.mendeley.com, naturalscenesdataset.org, cvnlab.slite.page 등이 이 클라우드 환경에서 차단되어 있다. 허용할 경우 Stage 2 시작 시 이 저장소 전용 환경을 만들거나 기존 환경에 호스트를 추가할 수 있다.
15. **문헌 표기 규칙 확장:** `verified_by: "search_index"`, `discussion_read: "search_summary"` 값을 Stage 1에서 새로 도입했다(CLAUDE.md 5절 스키마에 없음). Stage 2에서도 이 규칙을 쓸지.

---

## 사용자 결정 기록

(위 항목에 대한 결정을 여기에 적어 주세요. Stage 2 Coordinator가 이 절을 먼저 읽습니다.)

### 2026-11-12 (사용자 답변, 채팅)

| 항목 | 결정 |
|---|---|
| 2, 7, 9, 10 원본 자극과 데이터 보유 | **4개 데이터셋 모두 보유** ("다 갖고 있어. 전부 다."). Horikawa 원본 비디오, Emo-FilM 영화, Spacetop 자극, NSD 자극 모두 G1 = **보유**로 갱신. 단 Spacetop의 EDA/PPG와 설문은 공개본에 없는 자료라 "전부"에 포함되는지는 미확인으로 둔다 |
| 8 Horikawa 1순위 | **Horikawa 1순위 유지. Emo-FilM도 함께 사용 가능** |
| 14 네트워크 | **논문 사이트 허용.** Coordinator가 이 저장소 전용 클라우드 환경을 제안해 승인 절차를 진행 |
| 1, 3~6 나머지 환경 정보 (경로, feature, 계산 자원, checkpoint, 제약) | 보류. 미확인으로 두고 진행 (Stage 4 Pilot 설계 전까지 필요) |
| 11 Spacetop 생리 데이터 요청 | 보류 |
| 12 `reference/` 정정 | 보류. `reference/` 파일은 고치지 않고, Stage 2 위임 메시지에서 "Horikawa 원자료는 2020년부터 공개" 사실을 명시 |
| 13 `existing_projects.md` 확인 | 보류 |
| 15 `search_index` / `search_summary` 표기 | 별도 지시 없음. Stage 2에서도 같은 규칙 사용 |

### Gate 갱신 (사용자 보유 확인 반영)

| 데이터셋 | G1 (갱신) | 비고 |
|---|---|---|
| Horikawa | **보유** | 모델 기반 연구 가능. `gate_decision.md` 2절의 대안 검토는 불필요해짐 |
| Emo-FilM | **보유** | 크레딧 절단본 여부는 미확인 (보유 파일이 연구 판본과 같은지 확인 필요) |
| Spacetop | **보유** | |
| NSD | **보유** | |

---

## Stage 2: Axis Discovery & Literature Review (Round 1)

* 상태: **완료** (2026-11-12). Stage 3는 사용자 확인 전까지 시작하지 않는다.
* 산출물: Deliverable B, C, D, E(초안)

| 파일 | 내용 |
|---|---|
| `outputs/literature/literature_db.csv` | **Deliverable C.** 고유 381편, **verified 377편**. 생성 스크립트 `outputs/literature/merge.py` |
| `outputs/literature/stats.md` | Axis별, 연도별, discussion_read, 에이전트별 통계 |
| `outputs/literature/verification_sample.md` | 인용 표본 검증 25편 (시드 20261112) |
| `outputs/axis_encyclopedia.md` | **Deliverable B.** Axis A~T 정리, 새 Axis U~Y, 필수 태그 6종, 갱신된 유형표, 이견 기록 |
| `outputs/future_directions.md` | **Deliverable D.** Discussion-to-Research chain 80개를 9개 주제로 정리, 두 논문의 limitation 연결 질문 15개. 생성 스크립트 `outputs/literature/build_future_directions.py` |
| `outputs/literature/future_directions_all.csv`, `chains_index.csv` | 전체 future direction 656개, chain 80개의 구조화 목록 |
| `outputs/opportunity_map.md` | **Deliverable E 초안.** 다른 분야 → 정서 65행, 역방향 8행 |
| `outputs/agents/<이름>/round1.md`, `literature.jsonl` | 11개 에이전트의 Round 1 결과 |
| `outputs/agent_registry.md` | Stage 3 재개용 agent ID (이 세션 안에서만 유효) |

### 실행 방식 (사실 기록)
* 11개 에이전트를 커스텀 에이전트 타입으로 병렬 실행했다(emotion-theory, vision-decoding, encoding-foundation, multimodal-dynamics, frontier-ai, geometry-info, systems-neuro, generative-counterfactual, llm-semantics, brain-inspired, adversarial-reviewer). 에이전트당 약 25~29분, 36만~47만 토큰.
* 네트워크: 사용자 승인으로 이 저장소 전용 환경 "emotion_explore"를 만들어 논문 사이트 20곳을 허용했다. 그래도 nature.com(봇 차단 403), PMC 웹(reCAPTCHA), Semantic Scholar와 bioRxiv(429), huggingface.co, GitHub 웹 일부, ojs.aaai.org, sas-space.sas.ac.uk 등은 열리지 않았다. PMC 전문은 PubMed 도구로 읽었다.
* verified 고유 논문이 100편을 넘었으므로(377편) 추가 조사(2절 4번)는 하지 않았다.

### 검증 결과
* **인용 표본 25편:** 식별자 오류 0, verified_by 표기 오류 0, 본문을 읽지 않고 Discussion에서 가져온 것처럼 쓴 경우 0. 내용(한계 단락 위치) 오류 1건.
* **already_done 오판:** "no"로 적힌 판정 20개를 재검색하니 5개(25%)가 실제로는 선행 수행되어 있었다.
* **재점검 (지침 3절):** brain-inspired(already_done 전체 재검색, unknown 45개 해소, no → partially 6건, round1.md 과대 서술 15곳 범위 축소), emotion-theory(full_text 18편 점검, 판정 7건 변경, 한계 출처 7건 수정, chain C3 no → partially), dataset-auditor NSD(미확인 15개 해소, search_index 11편을 식별자 경로로 재확인). 나머지 5개 에이전트의 개별 판정 5건은 Coordinator가 수정했다. 이제 already_done 값은 no 377, partially 268, yes 11이며 비표준 값은 없다.
* 재점검을 하지 않은 에이전트(adversarial-reviewer, encoding-foundation, frontier-ai, generative-counterfactual, geometry-info, llm-semantics, multimodal-dynamics, systems-neuro, vision-decoding)의 "no" 판정에도 같은 수준(약 25%)의 과대 판정 위험이 남아 있다. Stage 3 Round 3("이미 연구된 것은 아닌가")와 Stage 4 선행연구 중복 감사에서 실제로 쓰이는 항목마다 다시 확인한다.

### Round 1의 주요 발견 (요약)
1. **EmoNet 누수:** Kragel 2019 EmoNet은 Horikawa와 같은 Cowen & Keltner 비디오로 학습되었다(5개 에이전트가 원문 Methods로 각각 확인). Horikawa 분석의 feature나 평가기로 쓰면 안 된다.
2. **사전학습 데이터 겹침 없음:** TRIBE v2, CortexMAE 등 fMRI foundation model의 사전학습 데이터에 우리 4개 데이터셋은 없다(NSD는 일부 평가에만 쓰였다). 같은 자극으로 실측과 in-silico 예측을 비교할 수 있다.
3. **Westlin 2025 재분석의 해석:** 4개 에이전트가 독립적으로, 군집이 scan session과 run에 더 강하게 대응한다는 점(NMI 0.19, 0.17 vs 정서 평정 0.014)을 지적했다. "재현 실패"가 분석 가정과 잡음 구조 때문일 가능성이 있다(에이전트 해석, 검증 필요).
4. **Horikawa 2020 결론의 약점:** 정서, 시각, 의미 모델을 따로 적합해 비교했으므로 의미 공변량의 측정 오차가 정서 고유 기여를 부풀릴 수 있다(doi:10.1371/journal.pone.0152719).
5. **Ma & Kragel 2026의 빈칸:** TEM 환경이 대칭 유사도 위 무작위 보행이라 실제 정서 전이 방향이 모형에 없고, 효과 크기가 작으며(r 약 0.04~0.10), appraisal 항목과 참가자 생리를 쓰지 않았다.
6. **생성 모델의 공백:** 정서를 조작하면 의미 내용도 함께 바뀐다(NeuroVolve 2025: amygdala 최대화가 얼굴, 최소화가 건물). 의미를 고정한 정서 편집이 비어 있다.

### 미확인과 미해결 사항
* chain에 인용되었지만 DB에 없는 식별자 2개(arXiv:2111.14232, arXiv:2204.00673)
* 모델 checkpoint와 코드 라이선스 다수(huggingface.co, GitHub 차단으로 검색 수준)
* Cowen & Keltner (2017) 외 일부 고전 논문의 SI(pnas.org SI 접근 실패), LeDoux & Brown (2017) SI Box 10
* Stage 1의 미확인 항목(Deliverable A 7절)은 사용자의 데이터 보유 확인으로 G1 관련 항목이 대부분 해소되었고, 나머지는 그대로다

---

## 사용자 확인 필요 (Stage 3 시작 전)

### 꼭 필요한 것
16. **Horikawa 2025 Mind captioning 데이터(OpenNeuro ds005191) 사용 여부.** Horikawa 2020과 같은 Cowen & Keltner 비디오를 본 독립 코호트(6명)다. 72개 클립 5회 반복(noise ceiling 추정 가능), 같은 클립 회상 imagery와 vividness 평정, "정서를 쓰지 말라"는 지시로 받은 인간 캡션이 있다(논문 본문 기준, 저장소 내용 미확인). 4개 보유 데이터셋 밖이다. 사용하면 Axis W(Internally Generated Experience)와 chain VD-R2, LS-Chain1, VD-R6이 강해진다. 이미 갖고 계신지, 써도 되는지 알려 주세요.
17. **새 Axis U~Y 채택 확인.** Coordinator가 U(Label Provenance & Perspective), V(Action Readiness & Affordance), W(Internally Generated Experience, 조건부), X(Machine Affect Representations), Y(Metacognition & Introspective Report)를 채택했고, Acquisition & Signal Physics 등은 태그나 Sub-axis로 두었다(근거와 이견은 Deliverable B 2절). Stage 3의 무작위 조합은 이 유형표를 쓰므로 바꾸실 것이 있으면 알려 주세요.

### 있으면 좋은 것
18. **EmoPathway 출처.** brain-inspired 에이전트 정의(`.claude/agents/brain-inspired.md`)가 지정한 "EmoPathway" 모델을 arXiv, Crossref, Semantic Scholar, 웹 검색에서 찾지 못했다. 논문명이나 링크를 알면 알려 주세요. 모르면 정의 파일에서 빼는 것을 권한다.
19. **already_done 전체 재검색 여부.** 재점검하지 않은 9개 에이전트의 "no" 판정을 지금 일괄 재검색할지(에이전트 9개 추가 실행, 토큰 많이 듦), Stage 3~4에서 쓰이는 항목만 확인할지. Coordinator 권고는 후자다.
20. **추가 네트워크 허용.** huggingface.co(모델 카드, 라이선스), aclanthology.org(NLP 논문) 등을 더 허용할지. 허용하면 Stage 3 시작 때 환경 변경을 제안한다.
21. **Emo-FilM 보유 파일 판본.** 보유한 영화 파일이 연구에 쓴 크레딧 절단 판본과 같은지.
22. Stage 1에서 보류한 항목(1, 3~6 환경 정보, 11 Spacetop 생리, 12 reference 정정, 13 existing_projects 확인)은 그대로 보류 중이다.

### Stage 3 비용 참고
Stage 3는 10개 연구 에이전트의 Round 2(교차 교환), 제안 응답, Round 3(교차 비판, 제안 3개씩), adversarial-reviewer 상위 10개 검토, Round 4(5개 이상 에이전트), 조합 생성으로 이어진다. 같은 세션에서 에이전트를 재개하면 각 에이전트의 이전 맥락을 이어 쓸 수 있다.

### 2026-11-12 (사용자 답변, Stage 2 이후)

| 항목 | 결정 |
|---|---|
| 16 Horikawa 2025 Mind captioning (OpenNeuro ds005191) | **사용 가능. 사용자가 이미 보유하고 전처리까지 완료.** 사용 가능 데이터셋은 5개(Horikawa 2020, Emo-FilM, Spacetop, NSD, Mind captioning)로 늘어남. 이에 따라 chain VD-R2(회상 정서 재활성), LS-Chain1, VD-R6(정서 배제 캡션)과 Axis W의 데이터 조건이 충족됨. 저장소에 실제로 들어 있는 파일(반복 클립, 회상 과제, vividness, 캡션)의 세부는 미확인 |
| 17 새 Axis U~Y | 설명 후 사용자 답변 "일단 진행해"(선택지 미지정). Coordinator 권장안 적용: **U, V, W 독립 Axis 채택, X는 R의 Sub-axis, Y는 A의 Sub-axis**. 사용자가 다른 안을 고르면 수정. Stage 3 시작 지시로 봄 |

---

## Stage 3: Agent Discussion & Combinatorial Question Generation

* 상태: **완료** (2026-11-12). Stage 4는 사용자 확인 전까지 시작하지 않는다.
* 산출물: Deliverable F, G, E(갱신본)

| 파일 | 내용 |
|---|---|
| `outputs/discussion_record.md` | **Deliverable F.** Round 2~4의 제안과 비판, 수정된 주장, 최종 합의 6개, 남은 이견 14개(D1~D14), 과정에 대한 비판적 기록 |
| `outputs/rq_landscape.md` | **Deliverable G.** 연구 질문 60개, 군집 10개, 관문 9개와 공유 파이프라인, 경쟁 설명, 질문별 Axis 조합, 경로, 근거 ID, 데이터셋, 선행 판정, overlap |
| `outputs/opportunity_map.md` | **Deliverable E 갱신본.** 5절 추가: Stage 2 행 65개의 Stage 3 사용처와 판정 변화, 새 수입 기술 17행(66~82), 역방향 3행(R9~R11) |
| `outputs/combinations/matrix.csv` | 조합 96개(문헌 54, 무작위 30, 전략 12). P5 형식 13열 + 출처, 외부 분야, 군집, RQ ID, 선행 판정, Novelty 점검, note |
| `outputs/combinations/rejected.md` | 기각 22개와 사유, Round 4에서 에이전트가 기각한 Axis 쌍 10종, Novelty Constraint 적용 목록 |
| `outputs/combinations/build_matrix.py` | 조합 원자료와 점검 스크립트. matrix.csv, rejected.md, rq_table.md, matrix_checks.md를 만들고 rq_landscape.md 4절의 표를 다시 쓴다 |
| `outputs/combinations/matrix_checks.md` | 조합 규칙(유형 3개 이상, 외부 Axis), 근거 ID verified 여부, 제안 매핑 누락, 무작위 판정 누락, 전략 A~H 적용 점검. 위반 0 |
| `outputs/combinations/random_combos.csv`, `random_combos.py` | 무작위 조합 30개(시드 20261113) |
| `outputs/combinations/discussed_pairs.md`, `discussed_sets.csv` | Round 1~3에서 논의된 Axis 조합, 미논의 이종 쌍 23개(Round 4 입력) |
| `outputs/discussion/proposals_index.md`, `.csv` | Round 2 제안 76개 색인 |
| `outputs/discussion/responses_tally.csv`, `top10_for_review.md` | 응답 집계(수용 51, 수정 45, 반박 0)와 상위 10개(정정판) |
| `outputs/discussion/round3_assignment.md`, `.csv` | Round 3 검토 배정(시드 20261114)과 선정 이유 |
| `outputs/discussion/round3_summary.md` | Round 3 검토 요약, 새 데이터 사실, 남은 이견, 상위 10개 독립 검토와 선정 정정 |
| `outputs/agents/<이름>/round2.md`, `round3_reviews.md`, `round4.md` | 에이전트별 원 산출물 |
| `outputs/agents/adversarial-reviewer/round3_top10_review.md`, `round3_top10_addendum.md` | 상위 10개(+2개) 독립 검토 |
| `outputs/agents/coordinator/literature.jsonl` | Coordinator가 조합 근거로 새로 식별자 확인한 7편(Crossref, arXiv) |

### 실행 방식 (사실 기록)
* Round 2, 응답, Round 3, Round 4는 Stage 2의 같은 에이전트를 SendMessage로 재개해 실제 독립 에이전트로 수행했다(`outputs/agent_registry.md`). 상위 10개 검토는 새 adversarial-reviewer 인스턴스가 수행했다.
* Round 4는 5개 에이전트(frontier-ai, brain-inspired, geometry-info, llm-semantics, emotion-theory)가 미논의 이종 쌍 23개에서만 출발해 제안 20개를 냈다.
* P5 조합은 Coordinator가 직접 수행했다. 조합 원자료를 스크립트에 데이터로 적어 재생성할 수 있게 했다.
* 문헌 DB는 Round 3~4 추가분과 Coordinator 확인분을 합쳐 고유 483편, verified 478편이 되었다(`python3 -I outputs/literature/merge.py`).
* **Coordinator 오류와 정정:**
  1. Round 3 첫 배정에서 공동 제안자를 검토자로 넣었다. 고쳐 다시 배정했다.
  2. 응답 집계 스크립트가 표, 굵은 글씨, 제목 형식 응답을 놓쳤다. 줄 단위 파싱으로 고쳤다.
  3. 상위 10개 선정 점수에 Round 3 검토 파일의 언급까지 셌다. 지시문 기준("Round 2에서")과 어긋났고, adversarial-reviewer가 지적했다. Round 2만 세도록 고쳤고, 빠졌던 ET-P4와 EF-P4를 추가 검토했다.

### 결과 수치
* **Broad Research Directions 74개, Distinct Research Questions 60개**(최소 기준 40개, 30개 충족).
  * 경로별 질문 수: 문헌 45, 무작위 6, 전략 9.
  * 방향만 유지한 조합은 14개다.
* **군집 10개:**

| 군집 | 질문 수 |
|---|---|
| K1 정서 공간 구조 | 7 |
| K2 정서 대 내용 분리 | 7 |
| K3 라벨 출처와 관점 | 6 |
| K4 본인 경험과 개인차 | 3 |
| K5 시간 역학 | 10 |
| K6 행동 경향 | 7 |
| K7 기억과 회상 | 7 |
| K8 몸과 피질하 | 3 |
| K9 in-silico 충실도 | 6 |
| K10 소리와 서사 | 4 |

* **기각 22개:**
  * 경로별: 문헌 3, 무작위 16, 전략 3.
  * 주된 사유: 중복, Mind captioning 6명으로 개인차 추론 불가, 순환 라벨, Novelty Constraint.
* **근거 논문 ID 119개, 모두 verified.**
* **질문별 선행 판정:** partially 41, no 10, 미확인 9.
* **overlap 표시:** EmoViS 9, Emo-FilM 연구 11, EmoBrain 6.
* **질문이 쓰는 데이터셋:** Horikawa 2020 36, Mind captioning 33, Emo-FilM 31, Spacetop 16, NSD 5.

### Stage 3의 주요 발견 (요약)
1. **관문 연구가 먼저다.** 질문 다수의 해석 가능성이 저비용 관문 9개에 달려 있다. 관문 목록은 rq_landscape.md 3.1절에 있다.
   * in-silico 충실도(RQ-51)
   * 원 결과 재현과 신뢰 공유 부분공간(RQ-01 0단계)
   * Axis V 측정 타당성(RQ-39)
   * 정서 쌍별 positivity(RQ-13)
   * MLLM 항목별 대체 가능성(RQ-17)
   * Spacetop 결측과 검정력(RQ-21 0단계)
   * 순 흐름(RQ-24 0단계)
   * 피질하 신호(RQ-49)
   * 기술 잔차(RQ-08 0단계)
2. **Mind captioning이 핵심 자원이 되었다.** 다음을 함께 제공한다.
   * 같은 자극의 두 번째 코호트
   * 반복 신뢰도
   * 테스트 run의 의사 무작위 순서(R3-internal 후보)
   * 정서 배제 인간 캡션
   * 유일한 시행 단위 내성 보고
3. **상위 10개 독립 검토가 Round 2~3에서 수용된 오류 4건을 잡았다.**
   * 개인 잔차 묶음의 기준선 동치성. 가짜 r 약 +0.36이 시뮬레이션으로 확인되었다.
   * 방향성 묶음의 수학 오류 두 건(π 가중, 시간 역전 사슬).
   * Horikawa 2020 "affordances"의 오독. 이 오독은 Stage 2 axis_encyclopedia V 행까지 퍼졌고, 정정 주석을 달았다.
4. **Novelty가 체계적으로 하향되었다.** Round 3 검토 15개 모두에서 원 제안이 놓친 선행이 나왔다. 상위 10개 검토는 검토자들도 놓친 선행 4편을 더 찾았다(Woo 2017, Abdel-Ghaffar 2024, Zhan 2026, Li 2025).
5. **독립 수렴이 있었다.**
   * Round 4에서 두 에이전트씩 같은 설계에 도달한 경우가 2건이다.
     * 라벨 출처를 multi-view의 view로 둔다(RQ-18).
     * 회상을 생성적 재구성으로 본다(RQ-44).
   * 무작위 경로가 문헌 경로와 같은 질문에 도달한 경우가 4건이다.

### 주요 미해결 이견 (상세는 discussion_record.md 6절)
* **D3 생리의 지위:** nuisance인가 매개인가(systems-neuro 대 vision-decoding). RQ-48의 해석 규칙이 아직 합의되지 않았다.
* **D7 Spacetop 개인 잔차 묶음의 우선순위:** 다섯 에이전트가 수렴한 Round 2 점수 1위 주제다. 그러나 adversarial-reviewer는 유효 표본 40~57명과 기준선 문제 때문에 뒤로 미뤄야 한다고 본다.
* **D2 통계 통제와 설계 통제 삼각 검증의 독립성:** generative-counterfactual 대 adversarial-reviewer.
* **D9 Axis V의 근거:** 측정 타당성이 먼저라는 입장(emotion-theory, adversarial-reviewer)이 있다. 근거 정정에 brain-inspired가 동의했는지는 아직 확인되지 않았다.
* **D14 Round 2 합의(반박 0)의 성격:** 질 때문인가, 동의 편향 때문인가. adversarial-reviewer는 동의 편향 쪽으로 판단했다.
* **D10~D12 Axis 처리:**
  * signal-feasibility를 태그로 둘지 독립 Axis로 둘지.
  * Recognition vs Experience를 어떻게 처리할지.
  * X, Y를 Sub-axis로 둔 결정.
  * 셋 모두 Stage 2부터 이어진 이견이다.

### 미확인 사항
* Stage 3에서 새로 생긴 데이터 확인 항목은 rq_landscape.md 7절에 있다.
* Round 4 제안의 선행 판정은 대부분 에이전트 한 명의 WebSearch 범위다.
* 질문별 "no"(10개)와 "미확인"(9개) 판정은 Stage 4 선행연구 중복 감사가 필요하다.

## 사용자 확인 필요 (Stage 4 시작 전)

### 꼭 필요한 것
23. **Stage 4 진행 지시.** Stage 4는 질문 평가, Shortlist 10개, High-priority 5개, Pilot 3개를 만든다.
24. **`reference/existing_projects.md` 확인(Stage 1의 13번, 보류 중).** Stage 3에서 질문 24개에 overlap을 표시했다(프로젝트별로 세면 EmoViS 9, Emo-FilM 연구 11, EmoBrain 6. 두 프로젝트와 겹치는 질문이 있어 합이 24보다 크다). 프로젝트 요약이 현재와 다르면 overlap 표시가 틀린다. Stage 4 평가 전에 확인이 필요하다.
25. **데이터 보유 상태 확인.** 각 항목이 영향을 주는 질문을 괄호에 적었다.
    * (a) Mind captioning 보유본에 클립별 정서 배제 인간 캡션(20개)이 있는가(RQ-08, 09, 44, 45의 전제)
    * (b) Cowen & Keltner 원 클립의 오디오가 있는가(RQ-52)
    * (c) Horikawa 2020과 Mind captioning 피험자가 겹치는지 아는가(RQ-01)
    * (d) 보유한 Spacetop이 OpenNeuro ds005256 공개판과 같은 판본인가(RQ-21의 결측 구조 계산 근거)
    * (e) Horikawa 2020 참가자의 모국어를 아는가(RQ-02)

### 있으면 좋은 것
26. **우선순위 의견.** adversarial-reviewer는 GI-P1 + LS-P1(RQ-01, RQ-08) 묶음을 1순위로 권했다. 다음은 평정만 쓰는 저비용 관문(RQ-24 0단계, RQ-39)이다. 사용자가 군집이나 데이터셋에 선호가 있으면(예: Horikawa 1순위 유지) Stage 4 평가 가중치에 반영한다.
27. **계산 자원과 환경 정보(Stage 1의 1, 3~6번, 보류 중).** Stage 4의 Pilot Study Plan에는 GPU, 저장 공간, 모델 checkpoint 접근 정보가 필요하다. TRIBE v2, V-JEPA 2, video MLLM 실행이 해당한다. 정보가 없으면 Pilot은 "자원 미확인"으로 표시한다.
28. Stage 2 이후 보류 항목 18~22(EmoPathway 출처, already_done 일괄 재검색, 추가 네트워크 허용, Emo-FilM 판본)는 그대로 보류 중이다.

### 2026-11-12 (사용자 답변, Stage 3 이후)

| 항목 | 결정과 처리 |
|---|---|
| 23 Stage 4 진행 | **진행 지시.** Stage 4 시작 |
| 24 `existing_projects.md` | **EmoViS는 EmoBrain으로 흡수되었고, 나머지 요약은 현재 상태와 맞다.** `reference/existing_projects.md`에 확인 표시를 달았다(파일이 사용자 확인을 요청한 부분만 고침). matrix.csv의 겹침 표시를 "EmoBrain(구 EmoViS 범위)"로 바꿨다. 겹침이 있는 질문은 EmoBrain 14개, Emo-FilM 연구 11개다 |
| 25(a) Mind captioning 캡션 | **보유.** 클립별 정서 배제 캡션 20개. RQ-08, 09, 44, 45의 데이터 전제 충족 |
| 25(b) Cowen & Keltner 오디오 | **보유 클립 2,185개 모두 무음.** RQ-52의 "같은 클립 관찰 무음 대 in-silico 유음" 설계는 불가능해 Emo-FilM 안의 R0 대 R1 일치도로 축소했다. 원문 재확인: 평정자와 fMRI 참가자가 소리 없이 봤다는 점은 Horikawa 2020 본문("with no sound"), Mind captioning 본문("presented ... without sound"), Asanuma 2025가 일치한다. 원 영상에 소리가 있었는지는 Du 2023("removed")과 Asanuma 2025("containing no audio")가 엇갈리고, C&K 2017 Methods/SI는 열지 못했다. 어느 쪽이든 사용 가능한 판본은 무음이다 |
| 25(c) 두 코호트 피험자 중복 | **겹치지 않음(사용자 확인).** Mind captioning 본문에는 중복 여부 언급이 없다(장소, 스캐너, 윤리위원회는 다름: 도쿄대 3T Prisma, NTT). 사용자 확인을 근거로 RQ-01의 독립 코호트 전제를 충족한 것으로 둔다 |
| 25(d) Spacetop 판본 | **공개판 ds005256과 같을 것(사용자 추정).** adversarial-reviewer의 결측 구조 계산을 보유본에도 적용 가능한 것으로 둔다. 판본 차이가 발견되면 다시 계산 |
| 25(e) Horikawa 2020 참가자 모국어 | 사용자: "참가자는 일본인". 원문 재확인 결과(`outputs/stage1/horikawa_factcheck_stage4.md`): 열람 가능한 Horikawa 2020 본문과 같은 데이터를 쓴 Du 2023의 피험자 기술("Five healthy subjects ... ATR 윤리위원회 승인")에 국적이나 모국어 기재가 없다. Transparent Methods 보충자료는 PMC 웹 차단으로 열지 못했다. **사용자 확인을 따라 일본인으로 둔다(원문 미기재).** 결과: 두 코호트 모두 일본어 화자라 영어 화자 대조 코호트가 없다. 그래서 LIT-54(언어 특이 가설) 기각 사유가 확정된다 |
