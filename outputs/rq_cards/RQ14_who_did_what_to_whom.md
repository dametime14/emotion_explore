# RQ-14. '누가 누구에게 무엇을 했는가'라는 장면 구조가 정서 반응을 설명할까?

* 작성: llm-semantics (외부 분야 Situation Recognition in Computer Vision을 Round 1에서 제안한 에이전트). 기준일 2026-11-12
* matrix: STR-A3 (경로: strategy, 전략 A Technology Transfer). 군집 K2(정서 신호와 지각, 의미 내용의 분리)
* 근거 파일: `outputs/rq_landscape.md` 4절 RQ-14, `outputs/combinations/matrix.csv` STR-A3, `outputs/evaluation/prior_overlap_audit.md` 2절 RQ-14, `outputs/evaluation/reviewer_notes.md` 1.1절, 4.2절, 5절, `outputs/evaluation/selection.md` 3~5절, `outputs/stage1/dataset_EmoFilM.md`, `outputs/stage1/dataset_Horikawa.md`, `outputs/STAGE_STATUS.md` "사용자 답변, Stage 3 이후"

### 이 카드에서 쓰는 말

| 말 | 뜻 |
|---|---|
| 의미역(semantic role) | 한 사건에서 각 참여자가 맡은 역할. 행위자(누가), 대상(누구에게, 무엇을), 도구, 장소 등 |
| situation recognition, visual semantic role labeling | 이미지나 영상에서 "어떤 행동(동사)이 일어났고 누가 행위자, 누가 대상인가"를 자동으로 뽑는 컴퓨터 비전 과제(imSitu, VidSitu) |
| Agent appraisal | Emo-FilM의 평정 항목. "이 일은 사람이 일으켰나, 우연히 일어났나"(HumanCaused / ChanceCaused)를 1초마다 연속 평정 |
| consensus | Emo-FilM에서 항목과 영화마다 별도 평정자 3~4명의 평정을 평정자 안에서 z-score한 뒤 평균한 시계열 |
| 역할 뒤바꾸기 null | 같은 단어(같은 사람, 같은 동사)를 유지하되 행위자와 대상의 자리를 바꾼 가짜 feature. "구조"의 효과와 "단어"의 효과를 가른다 |
| 고유 분산, banded ridge | RQ-08 카드와 같은 뜻(다른 feature 묶음을 모두 넣은 모형에서 한 묶음만 설명하는 부분 / band마다 규제 강도를 따로 정하는 회귀) |
| AI 생성 feature | 사람이 아니라 AI 모델이 자극에서 뽑은 feature. [AI-est]로 표기하고 사람 주석과 섞지 않는다 |

---

## 1. Core Research Question

* **(a) 한 줄 질문:** '누가 누구에게 무엇을 했는가'라는 장면 구조가 정서 반응을 설명할까?
* **(b) 검증 가능한 세부 질문:** 영화 장면마다 행위자, 행동, 대상을 뽑은 사건 구조 feature가 물체와 장면 범주, 장면 설명 문장의 의미, 저수준 움직임, 대사를 통제한 뒤에도 Emo-FilM의 Agent appraisal 평정과 TPJ, STS, 내측 전전두, amygdala 반응을 따로 설명하는가, 그리고 그 설명력은 행위자와 대상의 자리를 바꾼 구조에서는 사라지는가?

## 2. Scientific Motivation

* appraisal 이론에서 "누가 일으켰는가"(행위 주체, 원인 귀속)는 핵심 변수다. 나쁜 결과의 원인을 누군가의 행동에 돌릴 수 있느냐가 분노와 슬픔을 가른다는 계산적 정식화가 있다(doi:10.1016/j.neubiorev.2022.104977, literature_db 기록).
* 타인 정서 귀속의 신경 표상(ToM 네트워크)은 valence나 arousal보다 추상적인 사건 특징(appraisal)으로 가장 잘 설명된다. 그러나 그 특징은 사람이 문장을 읽고 매긴 평정이었고, 저자들은 평평한 특징 목록이 사건의 인과와 시간 순서를 담지 못한다고 한계로 적었다(doi:10.1016/j.cub.2015.06.009, Discussion 'Characterizing Representational Spaces' 셋째, 넷째 단락, 본 에이전트 본문 확인).
* 컴퓨터 비전은 영상에서 "누가 누구에게 무엇을 했는가"를 의미역 구조로 뽑는 과제와 벤치마크를 만들었다(imSitu, VidSitu). 이 구조는 appraisal의 행위 주체 변수를 **자극에서 계산 가능한 형태**로 만든다.
* 정서와 의미 내용의 분리(K2) 논의에서 지금까지의 대안 설명은 "장면에 무엇이 있는가"(물체, 장면, 캡션 의미)였다. "무엇이 있는가"와 "누가 누구에게 무엇을 했는가"는 다르다. 같은 단어로 구조만 바뀐 장면(경찰이 도둑을 잡음 vs 도둑이 경찰을 잡음)이 다른 정서를 낸다는 직관을 뇌 자료로 시험한 연구는 없다.
* **지식의 공백:** 사건 의미역 구조가 물체, 장면 feature와 캡션 의미를 넘어 appraisal 평정과 정서 관련 영역 반응을 설명하는지 검정한 연구는 감사 검색 범위에서 찾지 못했다(아래 5절).

## 3. Origin of the Idea

* **에이전트 경로:**
  * llm-semantics Round 1: 미해결 문제 P4(상황의 시간적, 인과적 구조), 모델 M8(VidSitu식 의미역, MovieGraphs식 상황 그래프), 아이디어 I2(situation recognition을 정서 encoding feature로), 새 Sub-axis S2(Situation Structure & Relational Semantics)
  * Coordinator Stage 3 전략 경로: 전략 A(Technology Transfer)의 첫 시도(STR-A1, PPI)가 전제 붕괴로 기각되어 STR-A3로 새로 적용
  * Stage 4: 선행 중복 감사 판정 not found로 RQ-43 자리를 대체해 Shortlist에 들어감(`selection.md` 3절)
* **가져온 분야:** Computer Vision의 Situation Recognition(imSitu, VidSitu), 계산 인지과학의 inverse planning ToM(Houlihan 2023)
* **조합 ID:** STR-A3. Axis C(S2), A(appraisal), I(AI 모델), E(신경 표적), P(경쟁 모형 비교, 관찰 자료라 R0) + 외부 분야 Situation Recognition in Computer Vision

## 4. Prior Literature

모든 논문은 `outputs/literature/literature_db.csv`에서 verified이거나 본 에이전트 `literature.jsonl`에 식별자로 확인해 넣은 것이다.

| # | 논문 | ID | 읽은 범위 | 이 질문에 주는 기여 |
|---|---|---|---|---|
| 1 | Marras et al. 2025, Neural representation of action features across sensory modalities, NeuroImage | doi:10.1016/j.neuroimage.2025.121439 | 초록(DB 기록) | **가장 가까운 선행 1.** 행동 feature를 Space, Effector, Agent & Object, Social, Emotion, Linguistic으로 나눠 영화의 시청각, 시각, 청각판 fMRI를 encoding과 variance partitioning으로 분석. AON에서 Effector와 Social이 가장 크게 기여, Agent & Object는 작음(감사 기록). 수작업 주석, appraisal과 연결 안 함 |
| 2 | Thornton & Tamir 2024, Nat Commun | doi:10.1038/s41467-024-44870-7 | 초록(DB 기록) | **가장 가까운 선행 2.** 상황과 정신 상태의 신경 패턴이 그것이 허용하는 행동 패턴의 가중합으로 재구성됨. 행동 중심 표상의 근거 |
| 3 | Mohammadi, Van De Ville, Vuilleumier 2023, Cereb Cortex | doi:10.1093/cercor/bhad093 | 초록(DB 기록) | **가장 가까운 선행 3.** 영화의 정서 순간을 성분(appraisal, 행동 경향 등)으로 평정하고 성분별 네트워크 조합을 보고. 자극에서 계산한 feature는 아님 |
| 4 | McMahon, Bonner, Isik 2023, Curr Biol | doi:10.1016/j.cub.2023.10.015 | 초록(PubMed) | 사회 primitive(사람 간 거리, 마주봄)와 사회 상호작용 feature가 lateral stream을 따라 위계적으로 표상, 의사소통 상호작용이 STS에서 고유 분산. 이 질문의 경쟁 설명과 표적 영역 근거 |
| 5 | Skerry & Saxe 2015, Curr Biol | doi:10.1016/j.cub.2015.06.009 | 본문 | appraisal 사건 특징이 ToM 영역의 정서 귀속 표상을 가장 잘 설명. 텍스트에서 특징을 직접 추론하고 인과, 시간 구조를 담으라는 미래 과제 |
| 6 | Sadhu et al. 2021, VidSitu, CVPR | arXiv:2104.00990 (doi:10.1109/cvpr46437.2021.00554) | 결론 절(arXiv 본문) | 영화 10초 클립의 2초 사건별 동사, 의미역, 사건 관계 벤치마크. 사건 관계 예측은 여전히 어려움 |
| 7 | Yatskar, Zettlemoyer, Farhadi 2016, imSitu, CVPR | doi:10.1109/cvpr.2016.597 | 미열람(Crossref 서지만) | 이미지 의미역 표지(situation recognition)의 원형 |
| 8 | Morgenroth et al. 2025, Emo-FilM, Sci Data | doi:10.1038/s41597-025-04803-5 | DB 기록(본문, dataset-auditor 확인), Stage 1 보고서 | Agent를 포함한 50항목 1 Hz consensus, 평정자 일치 평균 0.38~0.39, 평정 주체는 별도 평정자 |
| 9 | Morgenroth et al. 2026, Emotion | doi:10.1037/emo0001619 | 초록(DB 기록) | 13개 이산 정서가 appraisal 등 성분으로 예측됨. appraisal 평정이 정서 평정과 공선적일 수 있다는 경고의 근거 |
| 10 | Emanuel & Eldar 2023, Neurosci Biobehav Rev | doi:10.1016/j.neubiorev.2022.104977 | DB 기록(본문, brain-inspired 확인) | 정서를 계산으로 정식화. 원인 귀속이 정서를 가른다는 이론적 동기 |
| 11 | Ruder, Uusberg, Sirts 2025, CLPsych | arXiv:2503.16883 | 본문 | GPT-4 reader 주석에서 타인 책임(Others' Responsibility) 같은 appraisal은 사람과 모델 모두 맞히기 어려움. LLM 추출의 한계 근거 |
| 12 | Doerig et al. 2025, Nat Mach Intell | doi:10.1038/s42256-025-01072-0 | 본문 | 캡션 언어 모형 표상이 고차 시각 반응을 잘 설명. 캡션 embedding이 구조 정보를 상당 부분 흡수할 수 있다는 공선성 근거 |
| 13 | Houlihan et al. 2023, Phil Trans R Soc A | doi:10.1098/rsta.2022.0047 | 본문 | inverse planning으로 appraisal을 계산. 덜 제약된 실세계 장면을 파싱할 일반적 방법이 없다고 적음(Discussion) |

## 5. Novelty

* **감사 판정: not found**(`prior_overlap_audit.md` 2절 RQ-14). "not found"는 감사 검색 범위에서 찾지 못했다는 뜻이다.
* **이미 있는 것(새로움으로 주장하지 않음):**
  * 행위자와 대상을 포함한 수작업 행동 feature로 영화 fMRI를 encoding한 연구(Marras 2025).
  * 사회 상호작용 feature의 STS 표상(McMahon 2023).
  * 상황 표상이 행동 표상의 합으로 재구성된다는 결과(Thornton & Tamir 2024).
  * 영화 정서 순간의 성분 평정과 네트워크(Mohammadi 2023).
* **남는 새 부분:**
  1. 행위자-행동-대상 구조를 사람 주석이 아니라 **영상에서 계산**한다(situation recognition 또는 MLLM).
  2. 그 구조를 appraisal의 행위 주체 평정(Agent)과 직접 맞대 본다.
  3. **역할 뒤바꾸기 null**로 "구조"의 효과를 "단어(누가, 무엇이 나오는가)"의 효과와 가른다.
  4. 캡션 embedding과 사회 primitive를 함께 통제한다.
* **경쟁 예측(감사 권고):** Marras 2025에서 Agent & Object 영역은 AON에서 기여가 작았다. 이 질문은 AON이 아니라 TPJ, STS, 내측 전전두를 표적으로 하며, AON에서 효과가 작다는 결과는 예측과 어긋나지 않는다.

## 6. Proposed Dataset

| 필요한 것 | 있는가 | 근거와 주의 |
|---|---|---|
| Emo-FilM 영화 원본(feature 추출용) | 있음(사용자 보유) | G1 필요. 보유본이 연구에 쓴 크레딧 절단 판본과 같은지 **미확인**. 영화별 CC 라이선스 조항 미확인(feature 추출만 하고 영상은 배포하지 않는다) |
| Emo-FilM fMRI(30명, 영화 14편, TR 1.3 s, 2.5 mm) | 있음 | 제공 전처리본은 6 mm smoothing과 WM/CSF 회귀 적용 상태. 피질하와 세밀한 영역 분석은 raw 재전처리 권장(Stage 1) |
| Agent appraisal consensus 1 Hz | 있음(CC0) | **평정 주체는 별도 평정자 44명 중 항목, 영화마다 3~4명**이며 fMRI 참가자가 아니다. 평정자 안에서 z-score한 상대 변화량이다. 평정자는 같은 영화를 최대 6번 봤다 |
| Agent 항목의 평정자 일치도 | 계산 가능(평정자별 원자료 공개) | 항목별 값은 Supplementary에 있고 미열람. 원자료로 재계산한다. 일치도가 0.20보다 낮으면(저자 권고 기준) 행동 목표로 쓰지 않는다 |
| 다른 appraisal 항목(Controlled, PleasantOther, GoalsOther, SocialNorms, Standards) | 있음 | 보조 목표. PleasantOther, GoalsOther만 타인에 대한 평가 문항 |
| fMRI 참가자 본인의 Agent 평정 | 사실상 없음 | 참가자 사후 클립 평정은 영화당 5항목, 영화 길이의 약 20%이며 Agent 포함 여부 미확인 |
| 대사 transcript | 없음 | ASR로 생성 [AI 생성 전사] |
| 사람이 단 의미역 주석(Emo-FilM) | 없음 | 소규모 인간 주석(R2)을 새로 받아 추출 품질 점검에 쓴다 |
| VidSitu/VidSRL 공개 checkpoint | **존재와 성능 미확인** | GitHub 접근이 이 세션에서 막혀 확인하지 못했다(reviewer_notes 4.2절과 같은 상태) |
| 장면 캡션 | 없음(Emo-FilM) | MLLM으로 정서 배제 지시 캡션 생성 [AI 생성] |
| 사회 primitive(사람 수, 얼굴 유무, 마주봄) | 없음 | 검출기 또는 MLLM으로 생성 [AI 생성] |
| 생리 신호(PPG, 호흡, EDA) | 있음 | 이 질문의 주 분석에는 쓰지 않음. 각성 교란 점검에만 |
| 보조 재현: Horikawa 2020 + Mind captioning | 있음 | Agent 평정은 없다. C&K 14차원 중 Control, Fairness, Obstruction이 약한 대리. 사람이 쓴 캡션 20개/클립에서 텍스트 의미역을 뽑을 수 있다 |

## 7. Proposed Computational Framework

* **Pretrained model**(공개 모델 먼저, 새로 학습하지 않음)
  * 영상 의미역: VidSitu 계열 공개 모델. checkpoint 존재, 성능, 라이선스 모두 **미확인**.
  * 대안: 공개 비디오 MLLM(예: Qwen2.5-VL 7B)에 2초 사건마다 "동사, 행위자, 대상, 행위자와 대상이 사람인가"를 정해진 형식으로 답하게 한다. 결과는 **[AI 생성 feature]** 로 표기한다. 라이선스 **미확인**.
  * 텍스트 의미역 분석기: ASR 전사와 (보조 재현에서) 사람 캡션에 적용. 도구와 라이선스 **미확인**.
  * 대조 feature: 물체 검출, 장면 분류 모형, 문장 encoder(캡션 embedding), motion energy. 라이선스 **미확인**.
* **Input representation**
  * 의미역 band: 2초 사건마다 동사 범주, 행위자 유형(사람, 동물, 사물, 없음), 대상 유형, 사람이 사람에게 한 행동인지, 자기 자신에게 한 행동인지, 직전 사건과의 관계(원인, 반응). 행위자 자리와 대상 자리를 따로 둔 구조 벡터(자리마다 다른 embedding)로 만든다.
  * 단어 묶음 band(대조): 같은 단어 embedding을 자리 구분 없이 더한 벡터.
  * 역할 뒤바꾸기 band(null): 행위자와 대상 자리를 바꾼 구조 벡터.
  * 통제 band: 물체와 장면 범주, 캡션 embedding(차원 맞춤), 사회 primitive, motion energy, 대사 텍스트 feature.
  * 모든 band는 1 Hz와 TR(1.3 s)로 다시 표본화하고, 뇌 분석에서는 HRF 지연(FIR)을 둔다.
* **Output / target representation:** (1) 행동 목표: Agent consensus 1 Hz 시계열. (2) 뇌 목표: voxel 또는 parcel BOLD 시계열.
* **Training or adaptation strategy:** 모델은 모두 고정. MLLM은 몇 개 예시만 주는 prompt로 쓴다. 추출 품질을 먼저 점검한다(8절 0단계). 회귀는 영화 하나를 남기는 교차검증(leave-one-film-out, 14 fold)으로 학습한다.
* **Relevant brain regions / networks:** TPJ, pSTS(lateral social stream), dmPFC와 vmPFC, 쐐기앞소엽, amygdala(신호 품질 점검 후 탐색적). 경쟁 영역: AON(전운동, 두정내구; Marras 2025). 음성 대조: 초기 시각피질.
* **Loss function or statistical objective:** banded ridge의 제곱 오차. 평가는 보류 영화에서 예측과 실측의 상관과 설명 분산. 고유 분산은 전체 모형에서 의미역 band를 뺐을 때의 감소량. 행동 목표는 Agent의 평정자 간 일치도(상한) 대비 비율도 보고한다.
* **Interpretability method:** 양방향 variance partitioning과 product measure, 의미역 성분별 가중치(어떤 구조, 예: "사람이 사람에게 해를 끼침"이 Agent 평정과 TPJ를 움직이는가), 역할 뒤바꾸기와의 차이, 의미역 band와 캡션 band의 정준상관(공선성 크기).

## 8. Proposed Analyses

### 0단계 (전제 확인)
* **0a. 추출 품질 관문.**
  * 공개 VidSitu 계열 checkpoint를 구할 수 있으면 그것과 MLLM 추출을 VidSitu 검증 자료의 사람 주석에 견준다(검증 자료 접근 가능 여부 미확인).
  * Emo-FilM에서 무작위로 뽑은 약 100개 사건에 사람 두 명이 행위자 유형, 대상 유형, 동사를 단다(R2). 사람끼리의 일치와 모델-사람 일치를 함께 계산한다.
  * 행위자 유형 일치가 사전에 정한 기준(예: Cohen's kappa 0.6)에 못 미치면 뇌 분석으로 가지 않는다.
* **0b. Agent 평정 신뢰도.** 평정자별 원자료로 Agent의 영화별 평정자 쌍 상관을 다시 계산한다. 평균이 0.20 미만인 영화는 행동 분석에서 뺀다.
* **0c. 공선성 진단.** 의미역 band와 캡션 band, 사회 primitive band의 정준상관을 보고한다. 둘이 거의 같다면 고유 분산이 0에 가까운 것이 당연하므로 해석을 미리 조정한다.

### 1단계 (행동: 의미역 구조가 Agent 평정을 설명하는가)
* 보류 영화에서 Agent consensus를 예측한다. 비교 모형: 통제 band만 / 통제 + 단어 묶음 / 통제 + 의미역 구조 / 통제 + 역할 뒤바꾸기.
* 핵심 지표: "의미역 구조 - 역할 뒤바꾸기"의 예측력 차이. 영화 단위 순열로 유의성.

### 2단계 (뇌: 의미역 구조가 정서 관련 영역을 설명하는가)
* voxel과 parcel별 banded ridge. 표적 ROI에서 의미역 band 고유 분산, 역할 뒤바꾸기 band와의 차이, 차원 맞춘 무작위 band와의 차이.
* 공통 분할: 뇌 분산 중 Agent 평정이 설명하는 부분이 의미역 band와 얼마나 겹치는가(평정과 자극 구조가 같은 뇌 성분을 설명하는가).

### 3단계 (보조 재현)
* Horikawa 2020 + Mind captioning: 사람 캡션에서 텍스트 의미역을 뽑아 14차원 중 Control, Fairness, Obstruction과 뇌 반응을 같은 방식으로 분석한다. 클립이 짧고 Agent 평정이 없어 약한 재현이다.

### 비교 조건, baseline, ablation
* baseline: 통제 band만의 모형, 차원 맞춘 무작위 band, 역할 뒤바꾸기 band.
* ablation: 의미역 성분 하나씩 빼기(행위자 유형, 대상 유형, 사람→사람 여부, 사건 관계), 추출 방법(VidSitu 계열 대 MLLM), 캡션 encoder 종류.
* 민감도: 추출 확신도(confidence)를 공변량으로, 크레딧 절단 판본 차이가 있으면 시간 정렬 오차 보정.

### 통계 검정과 검증 전략
* leave-one-film-out(14 fold), 영화 고정효과, 영화 단위 순열과 bootstrap.
* 피험자별 결과와 유병률(30명 중 몇 명), parcel FDR.
* 분석 계획을 시작 전에 고정한다. 0a 관문 통과 여부와 기준도 미리 적는다.

### 반증 조건 (Falsifiability)
* **가설이 지지되지 않는 경우:**
  * 행동: 보류 영화에서 의미역 구조의 Agent 예측력이 역할 뒤바꾸기 band보다 낫지 않다.
  * 뇌: 표적 ROI(TPJ, pSTS, 내측 전전두) 어디에서도 의미역 band 고유 분산이 역할 뒤바꾸기와 무작위 band 기준선보다 크지 않다.
  * 효과가 AON과 초기 시각피질에서만 나타나면, 구조가 운반하는 것은 appraisal이 아니라 행동 지각 정보라는 해석이 된다.
* **판정 불가:** 0a 추출 품질 관문을 통과하지 못하면 결론을 내지 않는다. 0c에서 의미역 band와 캡션 band가 거의 같으면(정준상관이 매우 높음) "구조 정보는 캡션 의미에 이미 들어 있다"까지만 보고한다.

## 9. Competing Explanations

| 대안 해석 | 그것을 가르는 분석 |
|---|---|
| 효과는 구조가 아니라 "사람이 나오는가, 몇 명인가, 얼굴이 보이는가" 같은 사회 primitive다 | 사회 primitive band를 통제 band에 넣는다(McMahon 2023의 primitive 목록 참고) |
| 효과는 구조가 아니라 어떤 단어(사람, 동사)가 나오는가다 | 단어 묶음 band와 역할 뒤바꾸기 null |
| 캡션 embedding이 이미 구조를 담고 있다 | 공선성 진단(0c), 공유 분산 보고. 역할을 뒤바꾼 캡션 문장을 encoder에 넣어 encoder 표상이 구조에 민감한지 확인 |
| 행동의 운동학(움직임)이다 | motion energy와 영상 모형 band 통제 |
| 대사 내용(누가 누구를 탓하는가) 때문이다 | ASR 전사 텍스트 band 통제 |
| Agent 평정은 장면 구조가 아니라 평정자가 반복 시청으로 아는 줄거리를 반영한다 | 현재 사건과 직전 사건의 구조만 쓰는 모형과 영화 전체 맥락 모형의 비교, 평정 시점 지연 분석 |
| MLLM 추출 오류가 어둡거나 빠른 장면(공포, 각성)에 몰려 정서와 섞인다 | 추출 확신도 공변량, 영화별 추출 정확도(0a) |
| 영화 수준 교란(영화 14편의 장르, 음악) | leave-one-film-out, 영화 고정효과 |
| 각성이나 몸 상태가 TPJ, amygdala 신호를 만든다 | 생리 신호(참가자 PPG, 호흡, EDA)와 전역 신호를 공변량으로 한 민감도 분석 |

## 10. Potential Findings

1. **의미역 구조가 Agent 평정과 TPJ, pSTS 반응을 역할 뒤바꾸기보다 더 설명한다.** appraisal의 행위 주체 변수가 자극의 사건 구조에서 계산 가능하고, ToM 영역이 그 구조를 추적한다는 관찰 증거(R0). Skerry & Saxe 2015가 요구한 "인과, 시간 구조를 담는 표상"의 자연 영화판 근거가 된다.
2. **행동(Agent 평정)에는 효과가 있으나 뇌에는 없다.** 평정자가 판단할 때 쓰는 구조 정보가 fMRI 참가자의 해당 영역 신호로는 보이지 않는다. 평정 주체가 다르다는 점(별도 평정자 대 참가자)과 함께 해석한다.
3. **효과가 단어 묶음과 같다(구조 효과 없음).** "누가 누구에게"보다 "누가, 무엇이 나오는가"가 중요하다. 정서 대 의미 분리 논의에서 구조 수준이 내용 수준을 넘지 않는다는 결과다.
4. **효과가 AON에서만 나타난다.** 구조가 행동 지각을 운반한다. Marras 2025와 부합하며 appraisal 해석은 지지되지 않는다.
5. **캡션 embedding이 구조를 다 흡수한다.** 구조 정보는 언어 표상 안에 이미 있다. RQ-08과 같은 방향의 결과로, "장면 의미"의 범위에 구조도 포함해야 한다는 정보가 된다.

## 11. Scientific Contribution

* appraisal 이론의 핵심 변수인 행위 주체와 원인 귀속을 **자극에서 계산 가능한 구조**로 바꿔, 평정에 기대던 appraisal 신경 연구를 한 단계 객관화한다.
* 정서 대 의미 분리 논의(K2)를 "무엇이 있는가"와 "누가 누구에게 무엇을 했는가"로 세분한다. 결과 1이면 정서 관련 영역 신호의 일부는 사건 구조로 설명되고, 결과 3, 5이면 구조는 내용이나 언어 의미를 넘지 않는다.
* 사회 인지(ToM) 연구와 정서 연구를 같은 자극 계산으로 잇는다. Thornton & Tamir 2024의 행동 중심 표상, McMahon 2023의 사회 상호작용 위계와 같은 틀에서 비교할 수 있다.
* 방법 면에서 역할 뒤바꾸기 null은 "구조" 주장에 대한 간단하고 재사용 가능한 통제다.

## 12. Limitations & Risks

* **AI 생성 feature:** 의미역, 캡션, 사회 primitive, 전사가 모두 모델 산출물이다. 사람 주석 점검(0a)은 일부 사건만 덮는다.
* **추출 정확도:** 공개 VidSitu 계열 모형의 존재와 성능이 미확인이다. VidSitu 논문도 사건 관계 예측이 어렵다고 적었다. MLLM은 타인 책임 같은 appraisal을 맞히기 어렵다(arXiv:2503.16883).
* **평정 주체:** Agent 평정은 별도 평정자 3~4명의 consensus이고 fMRI 참가자가 아니다. 평정자 내 z-score라 절대 수준이 아니다. 평정자는 같은 영화를 여러 번 봤다.
* **Agent 항목의 범위:** "사람이 일으켰나, 우연인가"는 "누가 누구에게"의 일부(행위자의 존재)만 잰다. 대상과 피해 방향은 평정에 없다.
* **영화 14편:** 영화 수준 교란과 낮은 검정력.
* **전처리:** 제공본은 6 mm smoothing. amygdala 등 작은 영역은 재전처리 후에도 3T, 2.5 mm에서 신호가 약할 수 있다.
* **관찰 자료:** R0. 구조가 정서를 일으킨다는 인과 결론은 없다.
* **판본 차이:** 보유 영화가 크레딧 절단 판본과 다르면 시간 정렬 오차가 생긴다.
* **라이선스:** checkpoint 라이선스 미확인, 영화별 CC 조항 미확인.

## 13. Pilot Experiment

* **가장 작은 분석:** Emo-FilM 영화 2편에서 (1) MLLM 의미역 추출과 사람 주석 50개 사건 비교(0a), (2) Agent 평정자 일치 재계산(0b), (3) 보류 영화 1편으로 Agent 평정 예측(의미역 구조 대 역할 뒤바꾸기 대 단어 묶음).
* **필요한 것:** 영화 원본 2편, ds004872 평정자 원자료, 공개 MLLM 1개, 사람 주석자 2명(몇 시간).
* **계산:** GPU 1장으로 2초 사건 수백 개 추출이 가능하다고 추정(영화 전체 14편, 약 2.7시간이면 약 4,800 사건). 계산 자원 **미확인**, GPU 1~4장 가정.
* **진행 기준:** 행위자 유형 일치가 기준을 넘고, 행동 수준에서 의미역 구조가 역할 뒤바꾸기보다 Agent를 더 잘 예측하면 뇌 분석으로 간다. 행동 수준에서 차이가 없으면 뇌 분석은 탐색으로만 하고 우선순위를 낮춘다.

## 14. Feasibility & Priority

* **점수(`outputs/evaluation/scores_final.csv`, 1~5):** Novelty 4, Neuroscientific Importance 4, AI / Modeling Contribution 4, Dataset Feasibility 3.5, Methodological Rigor 3, Falsifiability 4, Interpretability 3.5, Generalizability 3, Feasibility 3.5. **합계 32.5(공동 7위)**, 과학 기준 5개 합 18.5.
* **순위:** Substantive Shortlist 10번(RQ-43 대체, 군집 K2 3번째로 다양성 규칙의 예외), High-priority Candidates 5위. Pilot에는 들지 않았고 Emo-FilM 쪽 다음 후보다(`selection.md` 6절).
* **계산 자원:** 미확인. GPU 1~4장 가정.
* **overlap:**
  * **EmoBrain(구 EmoViS 범위):** 부분 겹침. 정서 대 의미 내용 분리라는 물음이 같다. 이 질문은 사건 구조와 appraisal로 범위를 좁힌다.
  * **Emo-FilM 연구:** 부분 겹침. 같은 Emo-FilM 자료에서 사전학습 모형으로 정서 맥락의 기여를 분석한다는 점이 같다. 이 질문은 맥락 전체가 아니라 행위자-대상 구조와 Agent appraisal에 한정한다.

---

## 반영하지 않은 지적

| 지적 또는 원안 요소 | 출처 | 반영하지 않은 이유 |
|---|---|---|
| 보조 데이터 "Horikawa 2020(정적 장면 판본)", 즉 정지 프레임에 이미지 의미역(imSitu식)을 적용 | `matrix.csv` STR-A3 dataset 열 | 정지 프레임은 행동과 사건 관계를 잃는다. 대신 Mind captioning의 사람 캡션 20개에서 텍스트 의미역을 뽑는 방식으로 바꿨다(3단계). 사람이 쓴 문장이라 AI 영상 추출보다 오류가 적고, 그래도 Agent 평정이 없어 약한 재현에 그친다 |

---

## Safeguards 점검

| 항목 | 이 질문에서의 처리 |
|---|---|
| 참가자 경험 vs 자극에 묘사된 정서 | Agent는 별도 평정자가 자기 관점에서 매긴 appraisal 평정이다. 참가자 경험이 아니며, 의미역 feature는 자극에 묘사된 사건 구조다 |
| 인간 평정 vs 모델 생성 평정 | 의미역, 캡션, 사회 primitive, 전사는 [AI 생성 feature]. 목표 변수는 인간 평정만 쓴다. 사람 주석 점검(R2) 결과를 함께 보고 |
| 본인 보고 vs 규범 평정 | 목표는 규범(consensus) 평정. 참가자 본인 Agent 평정은 사실상 없음 |
| 정서 표상 vs 시각, 의미 내용 표상 | 물체, 장면, 캡션, 사회 primitive, 움직임 band 통제와 역할 뒤바꾸기 null |
| encoding 정확도 vs 설명적 적절성 | 고유 분산이 있어도 "구조를 표상한다"가 아니라 "구조 feature가 추가로 예측한다" |
| decodability vs 표상 vs 인과 | R0. 인과 주장 없음 |
| in-silico vs 관찰 | 관찰. MLLM은 feature 추출 도구 |
| 공유 표상 vs 데이터셋 특이 교란 | 주 데이터 하나(Emo-FilM). Horikawa + Mind captioning 보조 재현은 약함 |
| 탐색 vs 확인 | 0a 관문 통과 후 사전 고정한 ROI 검정은 확인, 그 밖은 탐색 |
| HRF 지연과 시간 자기상관 | FIR 지연, 영화 단위 순열과 bootstrap(시간 구조 보존) |
| 자극, 영화, 피험자 단위 누수 | leave-one-film-out. 같은 영화의 시간 구간을 학습과 시험에 나누지 않음 |
| 반복 자극 교란 | 영화당 1회 시청(fMRI 참가자). 평정자는 반복 시청(한계) |
| 평정자 일치와 라벨 잡음 | Agent 항목의 평정자 일치를 원자료로 재계산하고 상한으로 사용 |
| 시각-의미-정서 공선성 | 공선성 진단(0c), 차원 맞춘 band, 양방향 분할 |
| 시공간 해상도 | TR 1.3 s, 2.5 mm, 1 Hz 평정. 2초 사건 단위 |
| ROI 선택과 순환 추론 | ROI는 사전 지정(문헌 기반), 결과로 다시 고르지 않음 |
| 다중 비교 | parcel FDR, 피험자 유병률 |
| 자료 접근, checkpoint 라이선스 | 자료 보유. VidSitu 계열 checkpoint 존재와 라이선스, MLLM 라이선스 미확인 |
| 사전학습 오염 | Emo-FilM 영화(LIRIS-ACCEDE 계열 CC 영화)가 MLLM 학습 자료에 들어갔을 가능성 등록. 줄거리 기억이 추출에 섞일 수 있음 |
| 데이터셋 간 주석 비호환 | Agent(Emo-FilM)와 C&K 14차원(Horikawa)은 다른 척도. 보조 재현은 순위 수준 비교로만 |
| **label-provenance** | 목표: 대상 appraisal(사건의 원인 귀속), 주체 별도 평정자 규범(consensus). feature: AI 추정(의미역, 캡션, primitive), 사람 주석 점검은 별도 인간 주석자(R2) |
| **evidence-level** | R0(사람 주석 점검은 R2) |
| **insilico-vs-observed** | 관찰 |
| **G1** | 필요(영화 원본 보유, 판본 확인 필요) |
| **signal-feasibility** | 피질 ROI 양호. amygdala는 3T, 2.5 mm, 제공본 6 mm smoothing이라 재전처리 후 tSNR 점검, 탐색적 |
| **minimum-validation (7항목)** | (1) 경쟁 모형과 차원 맞춘 null: 단어 묶음, 역할 뒤바꾸기, 무작위 band ○ (2) 원 정확도와 상한: Agent 평정자 일치 상한 ○ (3) 내용 지표 다중화와 신뢰도 민감도: 캡션 encoder 여러 개, 추출 확신도 △ (4) 누수 경로별 대응: 영화 단위 fold, 사전학습 오염 등록 ○ (5) 일반화 수준: 같은 사람 새 영화(leave-one-film-out)와 피험자 유병률 ○ (6) 라벨 출처 표시 ○ (7) 반증 해석 사전 기술 ○ |
