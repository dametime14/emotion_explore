# Stage 2 Round 1 (Independent Discovery): adversarial-reviewer, Axis T

* 작성: adversarial-reviewer (Agent 12, Adversarial Reviewer & Methodology Auditor)
* 기준일: 2026-11-12
* 절차: `reference/protocols.md` P1. 이번 라운드의 역할은 다른 에이전트 검토가 아니라 Axis T(Scientific Discovery & Evaluation)와 평가 방법론, 재현성 문헌 조사다.
* 읽은 파일: `CLAUDE.md`, `reference/protocols.md`, `reference/axes.md`, `reference/starting_papers.md`, `reference/existing_projects.md`, `reference/datasets_and_resources.md`, `outputs/stage1/dataset_intelligence_report.md`, `outputs/stage1/gate_decision.md`, `outputs/STAGE_STATUS.md`(사용자 결정 기록 포함), 내 폴더의 `stage1_audit.md`.
* 독립성: 다른 에이전트 폴더(`outputs/agents/<다른 이름>/`)는 읽지 않았다.
* 전제(Stage 1 확정): 4개 데이터셋 모두 원본 자극 보유(G1 = 보유). Horikawa 1순위, Emo-FilM 병행. Horikawa 원자료는 2020-04-24부터 OpenNeuro ds002425에 공개되어 재분석이 이미 여러 편 있고, 반복 제시가 없어 noise ceiling을 직접 구할 수 없다.
* 문헌 파일: `outputs/agents/adversarial-reviewer/literature.jsonl` (38편)

### 문헌 통계

| 항목 | 값 |
|---|---|
| 전체 | 38편 |
| verified (식별자 경로 직접 확인) | 38편 (Crossref 31, arXiv API 6, PubMed 1). Han 2023은 arXiv와 PMLR 페이지 둘 다 확인 |
| 2024~2026년 | 15편 (Ma & Kragel 2026, Westlin 2025, Du 2025, Santavirta 2025, Kay 2025, Calderon 2025, VEM framework 2025/2026, Tak & Gratch 2024, Conwell 2024, Antonello & Huth 2024, Tuckute 2024, Rosenblatt 2024, REFORMS 2024, Gell 2024, Demidenko 2024) |
| Affective Neuroscience 밖 분야 | 16편 (통계, ML 과학 방법론, NLP 평가, 사회과학 방법론, 심리측정, 시각/청각/언어 NeuroAI, affective computing) |
| discussion_read | full_text 29, abstract_only 9 |

### 접근 기록 (사실)

* 사용한 경로: api.crossref.org, export.arxiv.org(API), arxiv.org(HTML, PDF), pmc.ncbi.nlm.nih.gov(HTML), proceedings.mlr.press, PubMed MCP(메타데이터, ID 변환), WebSearch(선행 수행 여부 확인용, 검색 수준), PyPI JSON(패키지 라이선스).
* 실패: www.nature.com은 프록시 403. direct.mit.edu는 403. 일부 PMC 페이지(Kragel 2019, Clark-Polner 2017, Santavirta 2025)는 자동화 차단 페이지를 반환해 재시도를 중단하고 PubMed 초록으로만 확인했다. api.semanticscholar.org는 429.
* Tuckute 2024는 출판본 대신 PMC에 실린 bioRxiv 판본(doi:10.1101/2023.04.16.537080) 본문을 읽었다.

---

## 0. 요약

1. **정서 신경과학의 핵심 주장 셋(정서 고유 분산, 범주 대 차원 판정, 정서 '지도' 계산 모델)이 모두 Axis T 관점에서 결정적으로 검증되지 않았다.** 원인은 공통적으로 (a) 내용 공변량과 라벨의 측정 오차, (b) noise ceiling 부재, (c) 대안 모델과의 식별 가능성 미검토, (d) 분석 선택 의존성이다.
2. **Horikawa 2020의 "정서 모델이 시각, 의미 모델보다 낫다"는 결과는 세 모델을 따로 적합해 성능을 비교한 것이다**(본문 확인). joint model 고유 분산이 아니며, 의미 공변량(73개 이진 항목, 영상당 12명 평정)의 측정 오차는 증분 타당도 위양성을 만든다(Westfall & Yarkoni 2016: 표본이 클수록 위양성률이 오히려 증가). 자극 2,181개는 이 문제에 불리한 조건이다.
3. **Westlin 2025의 재현 실패 보고도 결정적이지 않다.** 본문을 읽어 보니 GMM 군집과 세션의 NMI(0.188)가 정서 범주 평정과의 NMI(0.0141)보다 10배 이상 크고, NMI는 chance 보정이 없으며, 군집이 자극 구동 분산을 담는지 검증하지 않았다. 본문에 "모든 NMI < 0.01 (M = 0.0141)"이라는 내적 불일치도 있다. 두 분석 모두 가정 의존적이므로 **라벨 비의존적 중립 기준(다른 피험자의 같은 자극 반응으로 고른 voxel)을 포함한 multiverse**가 필요하다(D1).
4. **Du 2025(arXiv:2509.24298)는 MLLM 표상이 "인간 self-report"보다 Horikawa 뇌 반응을 더 잘 예측한다고 보고하지만**, 비교 대상은 본인 보고가 아닌 규범 평정이고, MLLM은 비디오 전체를 보며, 우세 영역에 고위 시각피질과 MST가 포함된다. 비정서 프롬프트 대조와 시각 전용 모델 기하 통제가 본문에서 확인되지 않았다. 신뢰도 비대칭(잡음 있는 인간 평정 대 반복 가능한 MLLM)도 통제되지 않았다.
5. **Ma & Kragel 2026의 TEM 결과는 효과 크기가 Fisher z 차이 0.005 수준이고, 대안 모델과 비교하지 않았다**(저자 스스로 RL 대안을 한계로 명시). 같은 평정 궤적의 matched-complexity 비선형 확장과 구별되는지, 영화 14편 규모에서 구별이 원리적으로 가능한지부터 시뮬레이션해야 한다(D3).
6. **AI 생성 정서 라벨의 하류 추론은 "지도가 비슷하다"(Santavirta 2025) 수준을 넘어 PPI, DSL, alt-test로 보정, 검정할 수 있다.** Emo-FilM은 평정자별 원자료가 있어 alt-test가 가능한 유일한 데이터셋이고, NSD는 무작위 인간 gold 표본을 새로 모으면 PPI가 가능하다. AI 라벨은 관찰자(규범) 관점에 가깝다는 근거(Tak & Gratch 2024)가 있어 본인 경험의 대리로 쓰면 안 된다.
7. Axis T에 **Analytic Robustness, Surrogate Label Inference, Model Identifiability, Leakage Audit, Explainable-variance Accounting, Small-N Population Inference, Pseudo-prospective Validation** 7개 Sub-axis를 제안하고, 이후 라운드에서 쓸 최소 검증 요건표를 7절에 둔다.

---

## 1. 중요한 미해결 문제

### U1. "정서 고유 분산" 주장의 측정 오차와 잔여 교란

* **문제.** 정서 라벨이 시각-의미 내용을 넘어 뇌 반응을 설명한다는 주장은 내용 공변량을 '통제'한 증분 타당도 주장이다. 공변량이 불완전하게 측정되면 잔여 교란 때문에 위양성률이 매우 높고, 표본이 클수록 증가한다(Westfall & Yarkoni 2016, Discussion 2째 단락). 반대로 정서 라벨이 내용 feature보다 잡음이 크면 banded ridge의 feature-space selection이 정서 공간을 '선택 해제'할 수 있다(Dupré la Tour 2022, 5절). 즉 결과가 신뢰도 비대칭의 방향에 따라 어느 쪽으로든 왜곡된다.
* **현 상태(확인).** Horikawa 2020 Results "Disentangling Emotional, Visual Object, and Semantic Feature Encoding" 절은 정서, VGG, 73개 의미 feature 모델을 각각 따로 적합해 비교했다. Du 2025는 MLLM embedding이 인간 평정 embedding보다 우세하다고 보고했으나 내용 통제를 본문에서 찾지 못했다. Kragel 2019는 이미지 내용만으로 정서 범주 평정을 예측할 수 있음을 보였다(초록). 즉 공선성은 크다.
* **근거 ID:** doi:10.1016/j.isci.2020.101060, doi:10.1371/journal.pone.0152719, doi:10.1016/j.neuroimage.2022.119728, doi:10.1126/sciadv.aaw4358, arXiv:2509.24298, doi:10.1016/j.conb.2019.04.002
* **CLAUDE.md 6절 연결:** Emotion representation vs visual/semantic content representation, Visual-semantic-affective feature collinearity.
* overlap: EmoViS (affective brain geometry의 sensory-semantic 기원, Horikawa 사용)

### U2. 같은 데이터에서 범주형 결론과 재현 실패가 공존하는 이유를 판정할 수 없다

* **문제.** Horikawa 2020은 범주형, 고차원 구조를, Westlin 2025는 개인 특이 구조와 평정 대응 부재를 보고했다. Westlin의 서술에 따르면 Horikawa 군집 분석은 평정으로 잘 예측된 voxel만 골라 K = 27로 고정했고(라벨 의존 선택), Westlin은 whole-brain PCA + GMM + BIC를 썼다(라벨 비의존이지만 자극 비의존).
* **검토자 판단(본문 대조).** Westlin의 군집은 세션과 NMI 0.188, run과 0.172로 정서 범주(0.0141), 차원(0.0019), 의미(0.026)보다 훨씬 크다. NMI는 범주 수가 많을수록 chance 수준이 높아지는 편향이 있어 세션(8개), run(61개)과 연속 평정을 직접 비교하기 어렵지만, 적어도 "군집이 자극 구동 분산을 반영한다"는 증거는 제시되지 않았다. 따라서 Westlin의 '개인 특이 구조'는 개인 특이 정서 경험과 세션/잡음 구조를 구분하지 못한다. 반대로 Horikawa의 라벨 기반 voxel 선택은 군집이 라벨 구조를 재현하도록 편향될 수 있다.
* **미확인.** Horikawa 원 논문 Methods의 군집 전 voxel 선택 절차는 Westlin의 서술로만 확인했다. 원문 대조가 필요하다.
* **근거 ID:** doi:10.1016/j.isci.2020.101060, arXiv:2507.00320, doi:10.1038/s41586-020-2314-9, doi:10.1177/1745691616658637, doi:10.1038/s41562-020-0912-z, doi:10.1093/scan/nsz037
* overlap: EmoViS (같은 데이터의 정서 기하, 부분)

### U3. 반복 제시 없는 정서 fMRI에서 "얼마나 설명했는가"의 분모가 없다

* **문제.** Horikawa(Discussion 6째 단락), Emo-FilM(영화당 1회), Spacetop alignvideo(1회)는 반복이 없어 표준 noise ceiling을 구할 수 없다. 반복이 있는 NSD에는 정서 라벨이 사실상 없다. 그래서 정서 모델 성능을 explainable variance 대비로 평가한 연구가 거의 없고, "높다/낮다"의 판정이 자의적이다.
* **세부.** Ma & Kragel 2026은 posterior-anterior 차이 Δz = 0.0052(d = 0.99)처럼 절대 크기가 매우 작은 효과를 보고했고 상한이 없어 해석 범위를 알 수 없다. Lage-Castellanos 2019는 정규화 정확도만 보고하는 관행을 비판하고 원 정확도와 NC를 함께 보고하라고 권한다(Discussion 6째 단락). 피험자 간 상한(ISC 기반)은 공유 반응만 담아 개인 특이 반응을 상한에서 뺀다(Nastase 2019). 정서 자극은 호흡을 동기화하므로 ISC 상한 자체가 생리 잡음으로 부풀 수 있다(Nastase 2019 Limitations 2째 단락).
* **근거 ID:** doi:10.1016/j.isci.2020.101060, doi:10.1371/journal.pcbi.1006397, doi:10.1371/journal.pcbi.1012092, doi:10.1093/scan/nsz037, doi:10.1038/s41467-025-68240-z
* overlap: Emo-FilM 연구 (생리, 부분)

### U4. 정서 계산 모델들은 현재 데이터로 서로 식별 가능한가

* **문제.** NSD에서 질적으로 다른 수백 개 모델의 예측력 차이가 매우 작고 linking 방법에 따라 결론이 크게 바뀐다(Conwell 2024: cRSA 약 31% 대 veRSA 약 79.5%). ground truth 모델을 target에 놓아도 linear encoding, CKA가 올바른 모델을 안정적으로 찾지 못한다(Han 2023). 모델이 뇌에 맞는다고 뇌가 그 목적함수를 쓴다고 추론할 수 없다(Antonello & Huth 2024). 정서 분야에서 TEM(Ma & Kragel 2026), 범주 대 차원(Horikawa 2020), MLLM 기하(Du 2025)의 우열 주장은 대안 모델 대비 식별 가능성을 점검하지 않았다.
* **근거 ID:** doi:10.1038/s41467-024-53147-y, arXiv:2302.06677, doi:10.1162/nol_a_00087, doi:10.1038/s41467-025-68240-z, doi:10.7554/eLife.82566, doi:10.1016/j.conb.2019.04.002

### U5. AI 생성 정서 라벨로 얻은 뇌 지도는 어떤 방향으로 편향되며 어떻게 보정하는가

* **문제.** GPT-4V 주석으로 만든 stimulus model이 인간 주석 기반과 비슷한 사회 지각 네트워크를 보인다(Santavirta 2025, 초록). 그러나 '비슷한 지도'는 계수 편향이나 신뢰구간 타당성을 보장하지 않는다. LLM 정서 판단은 당사자 자기 귀속보다 관찰자 판단에 가깝다(Tak & Gratch 2024). 예측 라벨을 하류 추론에 쓰면 편향이 생기며, 소량 gold 라벨로 보정하는 PPI, DSL이 있다(Angelopoulos 2023, Egami 2023). 인간 주석자 대체 정당화에는 주석자 단위 alt-test가 있지만 주관 과제와 높은 불일치에서 한계가 명시되어 있다(Calderon 2025, 7절).
* **데이터 제약(Stage 1).** Emo-FilM만 평정자별 원자료가 공개되어 alt-test가 가능하다. NSD nsdmeadows 100장은 무작위 표본인지 미확인이라 PPI gold로 바로 쓰기 어렵다. Spacetop 영상 내 시간축 AI 주석은 인간 검증 경로가 없다(Stage 1 보고서 5.3 #3).
* **근거 ID:** doi:10.1162/IMAG.a.134, arXiv:2408.13718, doi:10.1126/science.adi6000, arXiv:2306.04746, arXiv:2501.10970, arXiv:2509.24298

### U6. 정서 naturalistic fMRI 고유의 leakage와 작은 일반화 단위

* **문제.** Kapoor & Narayanan 2023의 분류에 비추면 정서 fMRI에는 같은 원본에서 잘린 클립(L1.4, L3.2: Horikawa 중복 표시 15개, 동일 원본 여부 미확인), 영화 내 시간 자기상관(L3.2), 라벨 기반 voxel 선택(L1.3), 사전학습 데이터 오염(NSD/COCO, 공개 연구 자극을 본 LLM)이 있다. leakage 영향은 효과가 약하고 표본이 작을수록 크다(Rosenblatt 2024, Discussion 6~7째 단락). Emo-FilM leave-one-film-out의 독립 단위는 영화 14편이라 오차 막대가 크다(Varoquaux 2018).
* **근거 ID:** doi:10.1016/j.patter.2023.100804, doi:10.1038/s41467-024-46150-w, doi:10.1016/j.neuroimage.2017.06.061, doi:10.1126/sciadv.adk3452

### U7. 피험자 5명과 자극 2,181개에서 무엇을 모집단으로 일반화할 수 있는가

* **문제.** Horikawa의 "피험자 간 일관" 주장과 Westlin의 "개인 특이" 주장은 둘 다 5명에 근거한다. 모집단 평균 추론은 불가능하지만, 개인 내 검정 + Bayesian prevalence로 모집단 유병률을 추론할 수 있다(Ince 2021: 5명 중 3명 유의는 전역 null 하 p = 0.00003 수준). 자극 일반화는 조건 bootstrap이 필요하다(Schütt 2023, Discussion 'Generalizing...' 절).
* **근거 ID:** doi:10.7554/eLife.62461, doi:10.7554/eLife.82566, arXiv:2507.00320, doi:10.1016/j.isci.2020.101060

### U8. Decodability, 표상, 인과, 주관 경험의 구분이 설계 수준에서 처리되지 않는다

* **문제.** 자극 기반 설계의 encoding만 모호하지 않은 인과 해석을 지지한다(Weichwald 2015, 초록). 그러나 정서 라벨은 조작 변수가 아니라 자극의 규범 평정이라 '라벨과 공변하는 자극 속성'까지만 지지한다. classifier는 조건별 beta 추정 가능성 차이만으로도 위양성을 낸다(Hebart & Baker 2018). Horikawa는 8 s 미만 클립을 반복 재생하고 긴 클립은 한 번 재생했다(Westlin 2025 Methods 기술). 클립 길이와 반복 횟수가 범주와 상관되면 반복 억제와 추정 가능성 차이가 범주 decoding에 섞일 수 있다(미검증 가설). decoding 성공은 본질적 '지문'이 아니다(Clark-Polner 2017).
* **근거 ID:** doi:10.1016/j.neuroimage.2015.01.036, doi:10.1016/j.neuroimage.2017.08.005, doi:10.1093/cercor/bhw028, doi:10.1016/j.conb.2019.04.002, arXiv:2507.00320

---

## 2. 주목할 모델 또는 방법론

Axis T의 '모델'은 주로 평가, 추론 도구다. pretrained weight가 없는 통계 도구는 "해당 없음"으로 적는다. 라이선스는 직접 확인한 것만 적고 나머지는 미확인으로 둔다.

| ID | 방법 | 근거 | 공개 코드 / weights | Input → Output | 학습 목표 / 추정 원리 | 라이선스 | 우리 데이터 적용 조건 |
|---|---|---|---|---|---|---|---|
| M1 | Banded ridge + product measure (himalaya) | doi:10.1016/j.neuroimage.2022.119728 | PyPI `himalaya` 0.4.11. weights 해당 없음 | 여러 feature space 행렬 + voxel 반응 → voxel별 예측, feature space별 분산 분해 | feature space별 정규화 계수를 교차검증으로 학습, 예측 분해 | BSD 3-clause (PyPI 메타데이터) | 정서 라벨, VGG, CLIP, 비디오 모델, 캡션 embedding을 한 모델에. 음수 product measure와 신뢰도 비대칭 해석 주의(U1) |
| M2 | RSA 통계 추론 (rsatoolbox) | doi:10.7554/eLife.82566 | PyPI `rsatoolbox` 0.3.2 | 뇌 RDM, 모델 RDM 집합 → 모델 성능과 차이의 신뢰구간 | 2-factor bootstrap(피험자 x 조건), 유연 모델 교차검증 | MIT (PyPI) | Horikawa는 조건 bootstrap 위주(피험자 5명). Emo-FilM은 영화 단위 bootstrap 필요 |
| M3 | GSN 신호-잡음 생성 모형 | doi:10.1371/journal.pcbi.1012092 | 코드 공개 여부, 라이선스 이번에 미확인 | 반복 측정 반응 → 신호, 잡음 공분산, noise ceiling, 유효 차원 | 가산 독립 잡음 가정의 다변량 정규 생성 모형, shrinkage | 미확인 | 반복이 있는 NSD에 직접. Horikawa, Emo-FilM에는 반복이 없어 직접 적용 불가(피험자를 반복으로 보는 변형은 강한 가정) |
| M4 | Bayesian prevalence | doi:10.7554/eLife.62461 | 코드(여러 언어) 공개로 서술, 라이선스 미확인 | 피험자별 검정 결과 → 모집단 prevalence 사후분포 | 이항 모형 기반 Bayesian 추정 | 미확인 | Horikawa 5명의 일관성 주장, 개인 특이 주장 모두에 적용 |
| M5 | PPI (prediction-powered inference) | doi:10.1126/science.adi6000 | PyPI `ppi-python` 0.2.3 | 대량 예측 라벨 + 소량 gold 라벨 → 편향 보정 신뢰구간 | rectifier(예측 오차 편향)를 gold로 추정해 보정 | 미확인 (PyPI에 표기 없음) | NSD 73k AI 정서 라벨 + 새 무작위 인간 표본. gold는 관심 분포의 무작위 표본이어야 함 |
| M6 | DSL (design-based supervised learning) | arXiv:2306.04746 | 저자 코드 존재로 알려짐, 이번에 미확인 | 대리 라벨 + 설계 확률로 뽑은 gold → 회귀계수와 신뢰구간 | doubly robust 보정 | 미확인 | AI 정서 주석을 회귀 설명/결과 변수로 쓸 때. gold 표본 추출 확률을 미리 설계 |
| M7 | Alternative Annotator Test (alt-test) | arXiv:2501.10970 | 코드 공개로 서술, 이번에 미확인 | 인간 주석자별 라벨 + LLM 라벨 → winning rate, 대체 가능 판정 | leave-one-annotator-out paired 검정, 비용 ε | 미확인 | 평정자별 원자료가 있는 Emo-FilM만 가능. 평균 일치도 0.38이라 IAA 보고, 작은 ε 필수 |
| M8 | Controversial stimuli / controversial selection | doi:10.1073/pnas.1912334117, doi:10.1038/s41467-024-53147-y | 해당 없음(설계 원리) | 경쟁 모델 2개 이상 + 자극 풀 → 모델 간 예측이 가장 어긋나는 자극 부분집합 | 모델 간 불일치 최대화 (또는 사후분포 엔트로피 감소) | 해당 없음 | Horikawa 2,181개, Emo-FilM 시점에서 기존 자극 선택만으로 가능(신규 fMRI 불필요) |
| M9 | Model metamers | doi:10.1038/s41593-023-01442-0 | 코드 공개 여부 이번에 미확인 | 모델 + 자연 자극 → 특정 layer 활성을 맞춘 합성 자극 | gradient 기반 활성 일치 최적화 | 미확인 | 이미지 정서 모델(EmoNet 등)에 우선 적용, 인간 평정은 온라인 행동 실험으로 |
| M10 | Multiverse / specification curve / guided multiverse | doi:10.1177/1745691616658637, doi:10.1038/s41562-020-0912-z, doi:10.1038/s41467-022-31347-8 | 해당 없음 | 분석 선택 공간 → 결론 분포, 결정적 선택, 결합 검정 | 전수 또는 GP 능동 탐색 | 해당 없음 | Horikawa raw(CC0)와 전처리본으로 즉시 가능 |
| M11 | SEM 기반 신뢰도 보정 증분 타당도 | doi:10.1371/journal.pone.0152719 | 웹 앱(ivy) 서술. 해당 없음 | 공변량, 관심 변수의 신뢰도 가정 → 구성개념 수준 증분 효과 | 잠재변수 모형 | 해당 없음 | 정서 고유 분산의 신뢰도 민감도 분석. Emo-FilM 평정자 원자료로 라벨 신뢰도 직접 추정 |
| M12 | Pseudo-prospective selection (closed-loop 설계의 기존 데이터 판) | doi:10.1038/s41562-023-01783-7 | 원 연구 encoding은 GPT2-XL 기반(공개 모델), 라이선스 이번에 미확인 | 학습 피험자 encoding model → 대상 영역을 구동/억제할 자극 순위 → 미사용 피험자의 관찰 반응 | 예측 극값 선택 후 관찰 검증 | 해당 없음 | Horikawa(같은 자극을 5명이 봄), Emo-FilM(30명). 자극과 피험자 동시 보류 필요 |
| M13 | EmoNet (도구로서의 정서 CNN) | doi:10.1126/sciadv.aaw4358 | weights 공개로 알려짐, 이번에 직접 확인 못함 | 이미지 → 11개 정서 범주 확률 | 지도학습 분류(AlexNet 기반 전이) | 미확인 | 정서 모델의 '반증 대상'으로 쓰기 적합(M8, M9). 정서 고유 분산 주장의 근거로 쓰면 안 됨(U1) |

---

## 3. 다른 분야 아이디어의 이전 (연구 아이디어)

각 아이디어에 출처 분야, 정서 신경과학에서의 형태, 데이터셋, 원본 자극(G1) 필요 여부를 단다. G1은 4개 데이터셋 모두 보유로 확인되었다.

### I1. Prediction-powered 정서 뇌 지도 (통계학 → 정서 신경과학)
* 출처: Angelopoulos 2023 (doi:10.1126/science.adi6000), Egami 2023 (arXiv:2306.04746)
* 형태: NSD 전체 이미지에 VLM 정서(valence, arousal, 범주) 라벨을 붙이고, 무작위로 뽑은 소량 이미지에 인간 평정을 새로 모아 gold로 쓴다. voxel별 정서 회귀계수를 naive(AI 라벨 그대로) 대 PPI 보정으로 추정해 결론이 바뀌는 영역을 지도화한다.
* 과학적 질문: AI 라벨이 만든 '정서 부호화 영역'의 편향은 어디에 몰리는가(예: 시각 내용과 공선적인 고위 시각피질 대 vmPFC).
* 데이터셋: NSD(주), Horikawa(AI portrayed emotion 라벨 + 소량 인간 표본). G1 필요(보유). 신규 인간 평정 비용 발생.
* 선행 수행: PPI의 fMRI 적용은 WebSearch 범위에서 찾지 못함(search 수준).

### I2. MLLM 정서 평정자의 대체 가능성 검정 (NLP 평가 → 정서 측정)
* 출처: Calderon 2025 (arXiv:2501.10970)
* 형태: Emo-FilM 50개 항목 x 14편에 MLLM 1 Hz 평정을 만들고, 평정자별 원자료로 leave-one-rater-out alt-test를 항목별로 수행한다. appraisal, motivation, physiology, feeling 성분별로 대체 가능성이 갈리는지 본다.
* 과학적 질문: 어떤 정서 성분은 관찰 가능한 화면 정보로 규범 판단이 가능하고(대체 가능), 어떤 성분은 평정자 고유 경험에 의존하는가(대체 불가). 이는 CPM 성분의 '관찰 가능성' 지도다.
* 데이터셋: Emo-FilM. G1 필요(보유, 크레딧 절단본 일치 여부 확인 필요).
* 선행 수행: 정서 연속 평정 대상 alt-test는 검색 범위 내 없음.

### I3. Controversial selection으로 정서 이론 판정 (시각 NeuroAI → 정서 이론)
* 출처: Golan 2020 (doi:10.1073/pnas.1912334117), Conwell 2024 Discussion 'Model-to-Brain linking methods' 3째 단락 (doi:10.1038/s41467-024-53147-y)
* 형태: Horikawa 2,181개 비디오에서 범주 모델, 차원 모델, appraisal 모델, 시각-의미 모델의 RDM이 서로 가장 어긋나는 부분집합을 고르고, 그 부분집합에서만 뇌 RDM과 비교한다. 선택은 뇌 데이터를 보지 않고 모델만으로 하므로 순환이 없다.
* 데이터셋: Horikawa, Emo-FilM(시점 선택). G1: 시각-의미 모델 feature에 필요(보유).
* 선행 수행: 정서 영역 검색 범위 내 없음.

### I4. 식별 가능성 시뮬레이션을 모델 비교 앞에 두기 (ML → 정서 계산 모델)
* 출처: Han 2023 (arXiv:2302.06677)
* 형태: 실제 Emo-FilM 평정 궤적과 실제 잡음 수준으로 TEM, SR, RL, matched random-feature 모델 각각에서 가짜 BOLD를 생성하고, 같은 분석 파이프라인이 생성 모델을 맞히는지 혼동 행렬을 만든다. 맞히지 못하면 실제 데이터의 모델 우열 주장은 정당화되지 않는다.
* 데이터셋: Emo-FilM, Horikawa. G1 불필요.

### I5. Prompt ablation을 'machine behavior' 정서 표상의 통제 조건으로 (ML 평가 → 정서 신경과학)
* 출처: Du 2025 (arXiv:2509.24298)의 한계, Antonello & Huth 2024 (doi:10.1162/nol_a_00087)의 representational generality 논리
* 형태: 같은 MLLM, 같은 triplet 과제를 "정서적으로 가장 다른 것", "시각적으로 가장 다른 것", "장면 의미가 가장 다른 것", "무작위 기준" 지시로 반복해 embedding을 만들고, 지시 간 뇌 정렬 차이와 고유 분산을 비교한다. 정서 지시의 우위가 시각/의미 지시를 통제한 뒤에도 남는 영역만 '정서 기하 정렬'로 해석한다.
* 데이터셋: Horikawa(주), Emo-FilM. G1 필요(보유). 계산량: triplet 판단 수백만 건(원 연구 규모), 축소 설계 가능.
* 선행 수행: Du 2025 본문 검색 범위에서 비정서 지시 대조 없음(Extended Data 미확인).

### I6. Affective metamer (청각/시각 NeuroAI → 정서 모델 반증)
* 출처: Feather 2023 (doi:10.1038/s41593-023-01442-0)
* 형태: EmoNet 같은 이미지 정서 모델의 후기 layer 활성을 원 이미지와 같게 맞춘 합성 이미지를 만들고, 인간 평정자가 같은 정서를 보고하는지 온라인 실험으로 검사한다. 반대로 내용이 크게 다른데 모델 정서 출력이 같은 '정서 불변성'이 인간과 일치하는지 본다.
* 과학적 질문: 정서 모델이 인간의 정서 판단 불변성을 공유하는가. fMRI 없이도 정서 모델을 반증할 수 있다.
* 데이터셋: NSD 이미지, Horikawa 프레임. G1 필요(보유). 신규 행동 데이터 필요.

### I7. Pseudo-prospective drive/suppress 검증 (언어 신경과학 → 정서)
* 출처: Tuckute 2024 (doi:10.1038/s41562-023-01783-7)
* 형태: 6절 D6 참조.

### I8. (역방향) 정서 데이터셋을 '라벨 관점' 벤치마크로 (정서 신경과학 → NLP/ML 평가)
* 출처: Calderon 2025 Appendix D.4(주관 과제 대안 요구), Tak & Gratch 2024
* 형태: 같은 자극에 별도 평정자 규범(Horikawa, Emo-FilM), 본인 보고(Spacetop alignvideo, Emo-FilM 사후 클립), 타인 지각(Spacetop faces)이 있는 구조를 LLM-as-judge 평가에서 '어느 관점을 대체하는가'를 검정하는 벤치마크로 제공한다.
* 데이터셋: Emo-FilM, Spacetop, Horikawa.

---

## 4. 기존 Affective Neuroscience와 예상 밖으로 연결될 수 있는 개념

### C1. 잔여 교란(역학) × 정서 특이 표상
역학의 residual confounding과 심리측정의 incremental validity 문제(Westfall & Yarkoni 2016)는 "정서가 내용을 넘어 설명한다"는 신경 encoding 주장과 수학적으로 같은 구조다. 자극 수가 많을수록 위양성률이 오른다는 반직관적 결과는 '대규모 자극 = 더 확실한 정서 특이성'이라는 직관을 뒤집는다. 정서 신경과학에서 이 문제를 신뢰도 민감도 곡선으로 보고한 연구는 검색 범위에서 찾지 못했다.

### C2. 신호 의존 잡음 × 정서 각성
GSN 등 noise ceiling 방법은 잡음이 신호와 독립이라고 가정한다(Kay 2025 Limitations). 정서 자극은 호흡, 심박을 자극에 동기화하므로(Nastase 2019 Limitations 2째 단락) 정서 연구에서 '잡음'은 정서와 상관된 신호가 된다. 이 경우 ISC 상한과 정서 encoding 성능이 함께 부풀고, 각성 decoding의 일부가 신경 표상이 아닌 생리 artefact일 수 있다. noise ceiling 이론의 가정 위반이 정서 연구에서 가장 크게 나타날 수 있다는 점이 예상 밖 연결이다. Emo-FilM 생리 기록(fMRI 참가자, 공개)으로 정량화 가능하다.

### C3. Theory-ladenness와 forking paths × 정서 이론 논쟁
Westlin 2025가 제기한 이론 의존 관찰 문제를 many-analysts(Botvinik-Nezer 2020)와 specification curve(Simonsohn 2020) 틀로 옮기면, semantic space theory 대 구성주의 논쟁의 일부가 '데이터가 이론을 판정할 힘(theory-adjudication power)'의 문제로 재정의된다. 즉 "어느 이론이 맞는가" 이전에 "이 자극 집합과 이 분석 공간에서 두 이론이 구별되는가"를 물어야 한다(Han 2023의 식별 가능성 논리와 결합).

### C4. LLM의 관찰자 관점 × 규범 평정
LLM 정서 판단이 평균 관찰자 판단에 가깝다는 결과(Tak & Gratch 2024)는 AI 라벨을 '세 번째 평정 주체'로 보게 한다. Horikawa 규범 평정과 AI 라벨은 같은 관점(관찰자)일 가능성이 높고, Spacetop 본인 보고와는 다를 것이라는 검증 가능한 예측이 나온다. CLAUDE.md 6절의 "참가자 본인 보고 vs 규범 평정 vs 모델 생성 annotation" 구분을 측정 가능한 변수(label provenance)로 바꾼다.

### C5. Model metamer와 불변성 × 정서의 불변 구조
정서 판단이 어떤 변환(인물 교체, 색, 시점, 배경)에 불변이고 어떤 변환에 민감한지는 정서 이론마다 다르게 예측된다(appraisal은 상황 구조 보존 시 불변, 지각 기반 설명은 시각 feature에 민감). Feather 2023의 metamer 논리는 이 '정서 불변성'을 새로운 실험 대상으로 만든다.

---

## 5. 새 Sub-axis 또는 하위 연구 방향

| ID | 이름 | 소속 Axis | 내용 | 근거 |
|---|---|---|---|---|
| S1 | Analytic Robustness & Multiverse | T | 분석 선택 공간 전체에 대한 결론 분포, 결정적 선택, 결합 검정. 라벨 비의존 중립 파이프라인 포함 | doi:10.1177/1745691616658637, doi:10.1038/s41562-020-0912-z, doi:10.1038/s41467-022-31347-8, doi:10.1038/s41586-020-2314-9, arXiv:2507.00320 |
| S2 | Surrogate Label Validity & Downstream Inference | T (Q와 연결) | AI 생성 라벨의 대체 가능성 검정(alt-test), 하류 추론 보정(PPI, DSL), 라벨 관점(provenance) 명시 | doi:10.1126/science.adi6000, arXiv:2306.04746, arXiv:2501.10970, arXiv:2408.13718, doi:10.1162/IMAG.a.134 |
| S3 | Model Identifiability & Adjudicating Stimulus Design | T (K, L과 연결) | 식별 가능성 시뮬레이션, controversial selection/stimuli, metamer, matched-complexity null | arXiv:2302.06677, doi:10.1073/pnas.1912334117, doi:10.1038/s41593-023-01442-0, doi:10.1038/s41467-024-53147-y, doi:10.1162/nol_a_00087 |
| S4 | Leakage Audit & Evaluation Hygiene | T (S와 연결) | 정서 fMRI 고유 leakage(동일 원본 클립, 시간 자기상관, 라벨 기반 선택, 사전학습 오염)의 정량화와 보고 | doi:10.1016/j.patter.2023.100804, doi:10.1038/s41467-024-46150-w, doi:10.1126/sciadv.adk3452 |
| S5 | Explainable-variance Accounting without Repeats | T (Q와 연결) | 피험자 간 상한의 반복 기반 상한 대비 보정, 생리 동기화 잡음 분리, 원 정확도와 상한 병기 | doi:10.1371/journal.pcbi.1006397, doi:10.1371/journal.pcbi.1012092, doi:10.1093/scan/nsz037 |
| S6 | Small-N Population & Stimulus-population Inference | T (O, S와 연결) | prevalence 추론, 2-factor bootstrap, 일반화 수준 명시 | doi:10.7554/eLife.62461, doi:10.7554/eLife.82566, doi:10.1016/j.neuroimage.2017.06.061 |
| S7 | Pseudo-prospective Validation of In-silico Predictions | T (H, L과 연결) | 기존 데이터에서 피험자와 자극을 함께 보류해 모델 예측 극값을 관찰로 검증, 사전 등록 가능 | doi:10.1038/s41562-023-01783-7, doi:10.1016/j.conb.2019.04.002 |

**독립 Axis 후보:** "Label Provenance & Perspective"(본인 경험 / 별도 평정자 규범 / 타인 지각 판단 / AI 추정). A(Emotion Recognition vs Experience), Q(Subjective vs Normative Labels), T(S2)에 흩어져 있지만 CLAUDE.md 6절 안전장치의 절반이 이 변수에 걸려 있고, 데이터셋 간 결합(Stage 1 3.2절)도 이 변수로 판정된다. 독립 Axis로 둘지는 Q 담당(emotion-theory)과 Coordinator의 판단에 맡기며, 이견이 생기면 그대로 기록하자고 제안한다.

---

## 6. Discussion-to-Research chains

형식: Original Finding → Unresolved Question → Technological Development → New Dataset / Model Combination → New Research Question. 각 단계에 근거 ID와 원문 위치를 단다.

### D1. 범주 결론과 재현 실패를 가르는 분석 선택의 지도 (Horikawa multiverse)

* **Original Finding.** 정서 범주가 차원보다 뇌 반응을 더 설명하고, 비지도 군집이 범주와 연관된다 [doi:10.1016/j.isci.2020.101060, Discussion 1째, 4째 단락].
* **Unresolved Question.** 같은 데이터의 최소 가정 재분석은 피험자별 군집 11~14개, 평정과 거의 무관한 군집을 보고하고 "이론 대 이론 비교와 multiverse 분석"을 요구한다 [arXiv:2507.00320, Discussion 'Future studies should thus investigate...' 단락]. 그러나 그 군집은 세션 NMI 0.188로 정서 평정 NMI 0.0141보다 세션 구조와 더 관련되며, 자극 구동 분산 검증이 없다 [arXiv:2507.00320, Results 'Run and Session Ordering'; 검토자 판단].
* **Technological Development.** specification curve와 결합 추론 [doi:10.1038/s41562-020-0912-z, 초록], guided multiverse의 능동 탐색 [doi:10.1038/s41467-022-31347-8, Discussion 마지막 단락], 여러 파이프라인 분석 권고 [doi:10.1038/s41586-020-2314-9, Discussion 3째 단락], ISC 기반 feature 선택 [doi:10.1093/scan/nsz037, 'Interpreting ISC results'], prevalence 추론 [doi:10.7554/eLife.62461, Discussion 1~2째 단락].
* **New Dataset / Model Combination.** Horikawa raw BIDS(ds002425, CC0) + 공개 전처리본. 선택 축: (1) voxel 선택: 없음 / 라벨 기반(nested CV 내부) / **라벨 비의존 leave-one-subject-out ISC**(같은 비디오에 대한 다른 4명 반응과의 상관으로 선택하므로 라벨과 해당 피험자 모두에 비의존), (2) 평정: 이진화 평균 / 연속 평균, (3) 군집: k-means K 고정 / GMM BIC / 군집 없음(encoding만), (4) 공간: native / MNI, (5) smoothing, (6) 단일 trial 추정: LSA / LSS / GLMsingle, (7) 클립 길이, 반복 재생 횟수 nuisance 포함 여부. 결과 지표: 범주 대 차원 encoding 우위, chance 보정 지표(AMI) + permutation null, 피험자 간 군집 대응, 세션 대응(통제 지표), prevalence.
* **New Research Question.** "Horikawa 데이터에서 '범주형, 고차원' 결론과 '개인 특이, 평정 무관' 결론은 분석 선택 공간의 어느 축에서 갈리며, 피험자 간 재현되는 자극 구동 분산만 남기면 어느 구조가 유지되는가?"
* **반증 기준.** 라벨 비의존 선택과 연속 평정 조건에서도 범주 우위가 명세의 대다수에서 유지되면 semantic space theory의 예측이 생존한다. 라벨 기반 선택에서 비의존 선택으로 바꿀 때만 사라지면 원 결론은 선택 순환에 의존한다. GMM 군집이 자극보다 세션을 더 추적하면 Westlin의 '개인 특이 구조'는 잡음 구조로 설명된다.
* G1 불필요. 선행 수행: partially (Westlin 2025는 대안 1개). overlap: EmoViS (같은 데이터의 정서 기하, 부분)

### D2. 신뢰도를 반영한 정서 고유 분산: 포화 곡선 검정

* **Original Finding.** 정서 모델이 VGG 시각 객체 모델과 73개 의미 모델보다 IPL, TE, DLPFC, DMPFC, VMPFC, OFC에서 예측이 높다 [doi:10.1016/j.isci.2020.101060, Results 'Disentangling...'; 세 모델 개별 적합 비교임을 본문 확인]. MLLM 정서 embedding이 인간 평정 embedding보다 TPJ, IPL, 고위 시각피질, MST에서 뇌와 더 정렬한다 [arXiv:2509.24298, Results 'Bridging the behavior-neural gap...'].
* **Unresolved Question.** 라벨이 참가자 보고가 아니고 1인칭/3인칭이 섞인다 [doi:10.1016/j.isci.2020.101060, Limitations 1~2째 단락]. 측정 오차가 있는 공변량을 통제한 증분 타당도는 구성개념 수준 잠재변수 접근 없이는 위양성 위험이 크고 표본이 클수록 커진다 [doi:10.1371/journal.pone.0152719, Discussion 2~3째 단락]. 이미지 내용만으로 정서 범주 예측이 가능하다 [doi:10.1126/sciadv.aaw4358, 초록].
* **Technological Development.** banded ridge와 product measure [doi:10.1016/j.neuroimage.2022.119728, 2.5~2.7절, 5절], 단일 지표 SEM 신뢰도 가정 분석 [doi:10.1371/journal.pone.0152719, Discussion 3째 단락], 2024~2026년 비디오, VLM feature(원본 비디오 보유로 추출 가능).
* **New Dataset / Model Combination.** Horikawa: 내용 지표를 VGG(원 논문), CLIP 계열, 비디오 자기지도 모델, 캡션 embedding, 원 73개 의미 feature로 점차 늘려 가며 정서 범주 공간의 고유 기여를 banded ridge로 추정. 평정자별 자료가 없으므로 라벨 신뢰도는 가정 범위로 sweep. Emo-FilM: 평정자별 원자료로 라벨 신뢰도를 직접 추정해 같은 분석을 반복하고, I5(prompt ablation) embedding을 추가 지표로.
* **New Research Question.** "시각-의미 내용을 여러 지표의 잠재 구성개념으로 통제하고 각 feature 공간의 신뢰도를 반영하면, 정서 범주의 고유 설명 분산은 내용 지표 수에 따라 0으로 수렴하는가, 아니면 특정 영역(예: vmPFC, IPL)에서 0보다 큰 plateau를 유지하는가?"
* **반증 기준.** 지표를 늘릴수록 고유 분산이 단조 감소해 0의 신뢰구간에 들어가면 그 영역의 정서 특이 주장은 지지되지 않는다. 모든 합리적 신뢰도 가정에서 plateau가 남는 영역만 '정서 고유'로 보고한다. 이 결과는 어느 쪽이든 정서 표상 대 내용 표상(CLAUDE.md 6절) 논쟁에 직접 답한다.
* G1 필요(보유). 선행 수행: partially (Horikawa는 개별 모델 비교, Du 2025는 MLLM 대 인간 평정). 신뢰도 보정 판은 검색 범위 내 없음. overlap: EmoViS (sensory-semantic 기원), Emo-FilM 연구 (정서 맥락 기여 분석)

### D3. 정서 '지도' 모델의 식별 가능성: TEM은 대안과 구별되는가

* **Original Finding.** hippocampus가 TEM layer p를, vmPFC가 대규모 layer g를 상대적으로 잘 decoding하며, TEM p를 통제하면 범주 평정 decoding이 줄어든다(Δz = 0.0042) [doi:10.1038/s41467-025-68240-z, Results 'Structural abstraction...' 및 Fig. 5 설명].
* **Unresolved Question.** 저자는 TEM이 유일한 hippocampus 모델이 아니며 RL 모델이 더 잘 예측하는지 검토해야 한다고 쓴다. 2차원(valence, arousal)만 썼다는 한계도 명시한다 [doi:10.1038/s41467-025-68240-z, Discussion 8째 단락 'Several limitations...']. 검토자 추가: TEM 입력이 평정 궤적이므로 TEM decoding은 같은 궤적의 임의 비선형 확장으로도 나올 수 있다. 절대 효과가 매우 작고 noise ceiling이 없다.
* **Technological Development.** ground truth 기반 식별 가능성 점검 [arXiv:2302.06677, 5. Discussion 'Glass half empty'], representational generality와 matched baseline 논리 [doi:10.1162/nol_a_00087, Discussion 1~2째 단락], 유연 모델 교차검증과 조건 bootstrap [doi:10.7554/eLife.82566, Discussion 'Generalizing...'], 소표본 CV 오차 막대 [doi:10.1016/j.neuroimage.2017.06.061, 초록].
* **New Dataset / Model Combination.** Emo-FilM 30명(v1.0.2 이후), 50개 항목 중 appraisal 포함. 후보 모델: TEM, 이산화한 정서 상태의 successor representation, TD value 모델, 같은 궤적의 random-feature 확장(동일 차원, 동일 입력), 다중 시간척도 평활. 1단계: 실제 궤적과 실측 잡음으로 각 모델에서 BOLD를 생성해 식별 혼동 행렬 계산. 2단계: 실제 데이터에서 영화 단위 bootstrap으로 비교.
* **New Research Question.** "Emo-FilM의 hippocampal-prefrontal 신호는 TEM의 구조 추상화에 특이적인가, 아니면 같은 평정 궤적의 matched-complexity 비선형 확장이나 RL 계열 모델과 통계적으로 구별되지 않는가? 그리고 영화 14편 규모에서 이 구별은 원리적으로 가능한가?"
* **반증 기준.** 1단계에서 식별이 우연 수준이면 이 데이터로는 cognitive map 계산 모델 간 우열을 주장할 수 없다(그 자체가 보고 가치가 있는 음성 결과). 식별 가능한데 TEM이 matched null을 이기지 못하면 '구조 추상화' 해석은 지지되지 않는다.
* G1 불필요. 선행 수행: partially (Ma & Kragel의 partial correlation 분석). overlap: Emo-FilM 연구 (부분). 이 체인은 geometry-info, systems-neuro 담당 Axis와 겹치므로 Round 2에서 그쪽 제안과 대조가 필요하다.

### D4. AI 정서 라벨의 하류 추론 보정과 관점 검정

* **Original Finding.** GPT-4V 사회 지각 주석으로 만든 stimulus model이 인간 주석 기반과 매우 비슷한 뇌 네트워크를 드러낸다 [doi:10.1162/IMAG.a.134, 초록]. GPT-4는 저자 자기평가보다 평균 독자 판단에 더 가깝다 [arXiv:2408.13718, IV General Discussion 3째, 6째 단락].
* **Unresolved Question.** 인간 불일치가 높으면 대체 검정 통과가 어렵고 주관 과제에는 대안 방법이 필요하다 [arXiv:2501.10970, 7 Limitations 'High disagreement', Appendix D.4]. gold 표본의 최적 추출이 미해결이다 [arXiv:2306.04746, Future Work]. Spacetop 영상 내 시간축 AI 주석은 인간 검증 경로가 없다(Stage 1 보고서 5.3 #3).
* **Technological Development.** PPI [doi:10.1126/science.adi6000, 1.1절], DSL [arXiv:2306.04746, 4절], alt-test [arXiv:2501.10970, 3절].
* **New Dataset / Model Combination.** (a) Emo-FilM: MLLM 1 Hz 50항목 평정 + 평정자별 원자료로 항목별 alt-test. (b) NSD: VLM 정서 라벨 전체 + 새로 뽑은 무작위 이미지의 인간 평정(설계 확률 기록) → voxel별 회귀계수 naive 대 PPI. (c) Spacetop: AI 라벨이 본인 보고보다 규범 평정(새로 수집 시)에 더 가까운지 검정.
* **New Research Question.** "AI 정서 라벨로 만든 voxel 수준 정서 지도는 어느 영역, 어느 정서 성분에서 편향되며, 무작위 인간 표본으로 PPI 보정하면 '정서 부호화 영역' 결론이 바뀌는가? 그리고 MLLM은 Emo-FilM 평정자를 어떤 CPM 성분에서 대체할 수 있고 어떤 성분에서 대체할 수 없는가?"
* **과학적 기여.** 라벨 출처(본인, 규범, AI)에 불변인 뇌-정서 관계와 관찰자 관점 라벨에만 나타나는 관계를 분리한다(CLAUDE.md 6절 human vs model annotation).
* G1 필요(보유). NSD는 신규 인간 평정 비용. 선행 수행: partially (Santavirta 2025는 지도 유사성 수준). PPI의 fMRI 적용은 검색 범위 내 없음. overlap: 확인 필요 (EmoBrain의 multimodal teacher-student distillation이 AI 생성 정서 표적을 쓰는지 미확인)

### D5. 반복 없는 정서 fMRI의 설명 가능 분산과 생리 동기화 잡음

* **Original Finding.** 각 자극을 한 번만 제시해 모델이 설명하지 못한 체계적 분산 비율을 추정할 수 없었고, 정서 반응이 반복으로 변하기 때문에 반복을 피했다 [doi:10.1016/j.isci.2020.101060, Discussion 6째 단락].
* **Unresolved Question.** 원 정확도와 NC를 함께 보고해야 하며 집단 수준 NC는 별도 방법이 필요하다 [doi:10.1371/journal.pcbi.1006397, Discussion 6째, 마지막 단락]. 잡음의 신호 독립 가정을 완화하고 신경 잡음과 생리 잡음을 구분해야 한다 [doi:10.1371/journal.pcbi.1012092, 'Limitations of GSN and future directions' 1째, 마지막 단락]. 자극 동기화 호흡이 ISC에 기여할 수 있다 [doi:10.1093/scan/nsz037, Limitations 2째 단락].
* **Technological Development.** 피험자 간 공유 반응 상한, GSN, 생리 회귀자.
* **New Dataset / Model Combination.** NSD(이미지당 3회 반복, 8명): 같은 이미지에서 반복 기반 within-subject NC와 피험자 간 상한을 함께 계산해 보정 함수를 추정. Emo-FilM(30명, fMRI 참가자의 PPG, 호흡, EDA 공개): 생리 회귀자 유무에 따른 ISC 상한과 정서 encoding 성능 변화를 정서 항목별(특히 arousal 대리 항목)로 측정. Horikawa: 보정된 피험자 간 상한 적용(생리 없음, 한계 명시).
* **New Research Question.** "반복이 없는 정서 fMRI에서 정서 모델이 설명 가능한 분산의 몇 %를 설명하는지 추정할 수 있는가? 피험자 간 상한은 반복 기반 상한을 얼마나 과소 또는 과대 추정하며(NSD 보정), 정서와 동기화된 생리 신호는 상한과 정서 encoding을 얼마나 부풀리는가(Emo-FilM)?"
* **반증 기준.** 생리 회귀 후 arousal 관련 encoding이 크게 줄고 범주 encoding은 유지되면, 기존 각성 decoding의 일부는 생리 artefact로 해석된다. 줄지 않으면 각성 신경 표상의 증거가 강화된다.
* G1 불필요. 선행 수행: partially (ISC 상한은 일반적 관행이나 정서 생리 오염 정량화는 검색 범위 내 없음). overlap: Emo-FilM 연구 (생리, 부분)

### D6. 기존 데이터 안의 의사 전향적 검증: 정서 모델이 고른 비디오가 새 피험자의 영역을 구동하는가

* **Original Finding.** LLM 기반 encoding model이 고른 문장이 새 개인의 언어 네트워크 반응을 실제로 높이거나 낮춘다 [doi:10.1038/s41562-023-01783-7, bioRxiv 판본 Discussion 1~2째 단락].
* **Unresolved Question.** 저자는 특정 하위 영역만 선택적으로 구동하는 자극 탐색과 in silico 대비 생성을 제안한다 [같은 문헌, Discussion 'A few limitations and future directions' 및 결론 단락]. 정서 영역에서는 in-silico 예측과 관찰 fMRI의 구분(CLAUDE.md 6절)을 검증한 사례를 검색 범위에서 찾지 못했다. 표상 해석에는 추가 가정이 필요하다 [doi:10.1016/j.conb.2019.04.002, 'Representational interpretations require additional assumptions'].
* **Technological Development.** 예측 극값 선택(M12), controversial selection(M8), prevalence(M4).
* **New Dataset / Model Combination.** Horikawa: 4명과 자극 80%로 학습, 남은 자극 20% 중 vmPFC, IPL 등을 가장 강하게/약하게 구동할 것으로 예측된 비디오를 (a) 정서 feature 모델, (b) 시각-의미 모델로 각각 선정하고, 선정 목록을 봉인한 뒤 5번째 피험자 관찰 반응으로 판정. 5회 반복 후 prevalence. Emo-FilM: 같은 방식으로 보류 영화의 시간 구간 선정.
* **New Research Question.** "정서 feature encoding model이 특정 영역을 가장 강하게 구동하거나 억제한다고 예측한 비디오는 학습에 쓰지 않은 피험자와 자극에서 실제로 그렇게 작동하는가? 정서 모델과 시각-의미 모델이 서로 다른 비디오를 고를 때 어느 선택이 관찰 반응과 맞는가?"
* **한계.** 데이터가 이미 수집되어 진정한 전향 실험이 아니다. 선정 목록 봉인과 분석 코드 사전 등록으로 보완한다. 자극 보류가 없으면 '새 피험자 일반화'만 검증하므로 자극과 피험자를 동시에 보류해야 한다.
* G1 필요(시각-의미 모델 feature, 보유). 선행 수행: no (검색 범위 내. 가장 가까운 것은 관찰 반응으로 자극을 고른 arXiv:2410.00047과 amygdala in-silico 통제를 다룬 JNeurosci 2025 논문이며 둘 다 검색 색인 수준으로만 봄, jsonl 미포함). overlap: EmoBrain (cross-subject 일반화 측면만, 부분)

### D7. 정서 naturalistic fMRI leakage audit (방법론 인프라)

* **Original Finding.** feature leakage와 subject leakage는 예측 성능을 크게 부풀리고, 효과가 약하고 표본이 작을수록 영향이 크다 [doi:10.1038/s41467-024-46150-w, Discussion 1~3째, 6~7째 단락].
* **Unresolved Question.** 각 분야가 도메인 지식으로 고유 leakage를 식별하고 효과를 정량화하라 [같은 문헌, Discussion 9째 단락]. 정서 데이터에서는 동일 원본 클립 여부(Stage 1 보고서 7.2 #9), 중복 표시 15개, 영화 내 자기상관, Spacetop shortvideo의 alignvideo 인물 재노출, NSD/COCO 사전학습 오염이 미정량 상태다.
* **Technological Development.** leakage 분류 [doi:10.1016/j.patter.2023.100804, 'Toward a solution' L1~L3], REFORMS 체크리스트 [doi:10.1126/sciadv.adk3452, 초록], 비디오 embedding 근접 중복 탐지(원본 보유로 가능).
* **New Research Question.** "정서 decoding 성능 보고값 중 얼마가 동일 원본 클립, 시간 자기상관, 라벨 기반 voxel 선택, 사전학습 오염에서 오는가?"
* **검토자 판단.** 단독 연구 질문으로는 Neuroscientific Contribution이 약하다(P5 Novelty Constraint). 모든 후보 질문의 전제 조건(인프라)으로 쓰는 것을 권고한다. G1 필요(근접 중복 탐지). overlap: 없음

---

## 7. Axis T 확장 제안

### 7.1 현재 Sub-axis에 대한 의견

| 현재 Sub-axis | 제안 | 이유 |
|---|---|---|
| Hypothesis Generation | 유지 | Stage 3 조합 단계의 출발점 |
| Model Comparison | 유지하되 "Model Comparison with Identifiability Check"로 강화 | 식별 가능성 점검 없는 비교는 결론을 내지 못함(Han 2023, Conwell 2024) |
| Falsifiable Predictions | 유지 | 모든 후보에 반증 기준을 요구 |
| Controlled Baselines + Ablation Studies | **병합**: "Controlled Baselines & Matched-Complexity Nulls" | 정서 연구에서 핵심 baseline은 같은 입력과 같은 차원의 무작위 확장, 비정서 프롬프트, 시각 전용 모델(Antonello & Huth 2024, Du 2025 한계) |
| Benchmarking | **재정의**: "Benchmarking with Ceilings and Reliability" | 정확도 개선 자체는 Novelty Constraint 대상. 상한과 라벨 신뢰도 대비 보고만 허용 |
| Variance Partitioning | 유지하되 "Reliability-aware Variance Partitioning"으로 강화 | 측정 오차와 신뢰도 비대칭이 결과를 양방향으로 왜곡(Westfall & Yarkoni 2016, Dupré la Tour 2022) |
| Model-to-Brain / Model-to-Behavior Evaluation | 유지 | linking 방법 의존성 명시(Conwell 2024) |
| Replication and External Validation | 유지, S6, S7과 연결 | 재현의 단위(측정, 피험자, 자극)를 명시 |

### 7.2 추가 Sub-axis
5절의 S1~S7을 T에 추가한다. 독립 Axis 후보 "Label Provenance & Perspective"는 Coordinator 판단 사항으로 남긴다.

### 7.3 재분류 제안
* Q의 "Neural Noise Ceilings"는 Q에 두되, 반복 없는 데이터의 상한 보정(S5)은 T에서 다룬다. Q 담당과 경계를 Round 2에서 확인한다.
* S의 "Cross-subject Generalization"과 T의 S6(prevalence)은 겹친다. S는 '일반화되는가', T는 '그 일반화 주장을 어떤 추론으로 정당화하는가'로 나눈다.

### 7.4 이후 라운드에서 쓸 최소 검증 요건 (adversarial-reviewer 제안)
Stage 3~4의 후보 질문마다 아래 항목을 표시하자고 제안한다. 충족하지 못해도 버리지 않고 '미충족'으로 표시한다.

1. 경쟁 모델 2개 이상과 matched-complexity null이 정의되어 있는가 (U4)
2. 원 정확도와 상한(또는 라벨 신뢰도)을 함께 보고할 계획이 있는가 (U3)
3. 정서 고유 분산 주장이 있다면 내용 지표 다중화와 신뢰도 민감도가 있는가 (U1)
4. leakage 경로(동일 원본, 시간, 라벨 기반 선택, 사전학습 오염)별 대응이 있는가 (U6)
5. 일반화 수준(측정, 피험자, 자극)과 추론 방법(prevalence, bootstrap)이 명시되어 있는가 (U7)
6. 라벨 출처(본인, 규범, 타인 지각, AI)가 표시되어 있는가 (U5, C4)
7. 결과가 기대와 반대일 때의 해석이 미리 적혀 있는가 (반증 기준)

---

## 8. 문헌 간 이견과 검토자 판단 기록

* **'예측 = 표상' 해석 규칙.** VEM framework 초록은 "feature space가 뇌 활동을 선형 예측하면 뇌가 그 feature를 명시적으로 표상한다고 본다"고 쓴다(doi:10.31234/osf.io/nt2jq). Kriegeskorte & Douglas 2019는 같은 공간을 여러 기저가 생성할 수 있어 이것이 feature fallacy라고 본다(doi:10.1016/j.conb.2019.04.002, 'The feature fallacy' 절). 두 입장은 해소되지 않았으며, 정서 encoding 결과 해석 시 후자의 기준(대안 기저 비교)을 최소 요건으로 쓰자는 것이 검토자 의견이다.
* **Horikawa 2020 대 Westlin 2025.** 어느 쪽도 결정적이지 않다고 판단한다(U2). Westlin은 반대 증거가 아니라 분석 가정 민감도의 신호로 다룬다(Stage 1 판정 유지). 추가로 Westlin 본문의 NMI 서술 불일치("all < 0.01"과 M = 0.0141)는 저자 확인이 필요한 오류로 기록한다.
* **Du 2025의 'self-reports' 표기.** Horikawa Limitations 1째 단락이 밝히듯 해당 평정은 fMRI 참가자가 아닌 별도 평정자의 평균이다. Du 2025의 "인간 self-report보다 정확"이라는 제목 주장은 "별도 평정자 규범 평정 기반 embedding보다 정렬이 높다"로 읽어야 한다.
* **정규화 정확도 보고 관행.** Lage-Castellanos 2019는 NC로 나눈 정확도만 보고하는 관행을 논쟁적이라고 보고 원 정확도 병기를 권한다. 이 프로젝트의 후보 질문은 병기를 기본으로 하자고 제안한다.
* **Stage 1 판단과의 관계.** Stage 1 보고서 5.1 #5(내용 중복 15쌍과 ISC 기반 대체 noise ceiling)는 D5와 같은 방향이다. 내 제안은 NSD로 보정하고 생리 오염을 정량화하는 단계를 더한 것이다.

---

## 9. 검증된 것과 미확인 사항

### 검증됨
* literature.jsonl 38편 전부 식별자 경로(Crossref, arXiv API, PubMed)로 존재 확인. 29편은 본문(Discussion, Limitations 또는 해당 절)을 직접 읽었고 9편은 초록만 읽었다.
* Horikawa 2020의 내용 모델 비교가 개별 모델 비교라는 점, Discussion 6째 단락의 noise ceiling 서술, Limitations 3개 단락(본문 확인).
* Westlin 2025의 NMI 수치, 군집 수, 전처리, PCA 279 성분, Discussion의 미래 방향(본문 확인).
* Ma & Kragel 2026의 PLS, leave-one-film-out, sign-flip permutation, 효과 크기, Discussion 한계 단락(본문 확인).
* Du 2025의 모델(Qwen2-VL 7B, Llama-3.1 70B), 인간 판단 시뮬레이션, 한계 절(본문 확인).
* 패키지 라이선스: himalaya BSD 3-clause, rsatoolbox MIT, brainiak Apache 2.0 (PyPI 메타데이터).

### 미확인
* Horikawa 원 논문 Methods의 군집 전 voxel 선택 절차(Westlin의 서술로만 확인).
* Horikawa에서 클립 길이와 반복 재생 횟수가 정서 범주와 상관되는지(U8의 가설, 데이터로 확인 필요).
* Du 2025 Extended Data에 시각 전용 모델 기하와 뇌 정렬 비교가 있는지.
* GSN, ppi-python, DSL, alt-test, Bayesian prevalence 코드, model metamer 코드, EmoNet weights의 라이선스와 공개 상태.
* Kragel 2019, Clark-Polner 2017, Santavirta 2025, VEM framework, Weichwald 2015, Steegen 2016, Simonsohn 2020, Varoquaux 2018, REFORMS의 본문(초록만 읽음).
* Calderon 2025의 학회 게재 여부.
* D6에서 언급한 arXiv:2410.00047과 JNeurosci 2025 amygdala encoding 논문(doi:10.1523/JNEUROSCI.1436-24.2025)은 WebSearch 결과로만 보았고 식별자 경로로 확인하지 않아 jsonl에 넣지 않았다.
* PPI의 fMRI 적용, 정서 영역 controversial selection, 정서 fMRI 신뢰도 보정 variance partitioning이 "없다"는 판단은 WebSearch와 Crossref 검색 범위 내 판단이다.
