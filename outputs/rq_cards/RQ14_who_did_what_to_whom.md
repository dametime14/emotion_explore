# RQ-14. '누가 누구에게 무엇을 했는가'라는 장면 구조가 정서 반응을 설명할까?

* 작성: llm-semantics (외부 분야 Situation Recognition in Computer Vision을 Round 1에서 제안한 에이전트). 기준일 2026-11-12. **재구성판**(`outputs/evaluation/card_review_B.md` 1절, 2.1절 반영)
* matrix: STR-A3 (경로: strategy, 전략 A Technology Transfer). 군집 K2(정서 신호와 지각, 의미 내용의 분리)
* 근거 파일: `outputs/rq_landscape.md` 4절 RQ-14, `outputs/combinations/matrix.csv` STR-A3, `outputs/evaluation/prior_overlap_audit.md` 2절 RQ-14, `outputs/evaluation/card_review_B.md`, `outputs/evaluation/reviewer_notes.md` 1.1절, 4.2절, 5절, `outputs/evaluation/selection.md` 3~5절, `outputs/stage1/dataset_EmoFilM.md`, `outputs/stage1/dataset_Horikawa.md`, `outputs/STAGE_STATUS.md` "사용자 답변, Stage 3 이후"

### 이번 재구성에서 바뀐 것 (요약)
* 목표 변수를 Agent appraisal에서 **정서 평정(분노, 경멸, 슬픔, 죄책감)** 으로 바꿨다. Agent 예측은 0단계 타당성 점검으로 내렸다.
* 무효였던 "역할 뒤바꾸기 band" 대조를 버리고, **자리 구분 있는 구조 대 자리 구분 없는 단어 묶음의 중첩 모형 비교**와 **시험 단계에서만 자리를 바꾸는 null**로 바꿨다.
* 가장 가까운 선행으로 Frankland & Greene 2015를 넣고 선행 판정을 not found에서 **partially(텍스트 문장 패러다임)** 로 바꿨다. 새로움은 "자연 영상에서 계산한 사건 구조"와 "정서, appraisal 평정과의 연결"로 좁혔다.
* 한 줄 질문 (a)는 바꾸지 않았다. 세부 질문 (b)는 목표 변수에 맞춰 고쳤다.

### 이 카드에서 쓰는 말

| 말 | 뜻 |
|---|---|
| 의미역(semantic role) | 한 사건에서 각 참여자가 맡은 역할. 행위자(누가), 대상(누구에게, 무엇을) 등 |
| situation recognition, visual semantic role labeling | 이미지나 영상에서 "어떤 행동이 일어났고 누가 행위자, 누가 대상인가"를 자동으로 뽑는 컴퓨터 비전 과제(imSitu, VidSitu) |
| 자리 구분 있는 구조 feature | 행위자 자리와 대상 자리를 따로 둔 feature. "경찰이 도둑을"과 "도둑이 경찰을"이 다른 값이 된다 |
| 자리 구분 없는 단어 묶음 feature | 같은 인물, 동작 정보를 자리 구분 없이 더한 feature. 두 문장이 같은 값이 된다. 구조 feature의 일부(구조 feature로 계산할 수 있는 값)이므로 두 모형은 중첩된다 |
| 시험 단계 자리 바꾸기 null | 원래 구조로 학습한 모형에, 시험 자료에서만 행위자와 대상 자리를 바꾼 feature를 넣는 대조. 모형이 자리 정보를 실제로 쓰면 예측이 나빠진다 |
| Agent appraisal | Emo-FilM 평정 항목 "이 일은 사람이 일으켰나, 우연히 일어났나"(HumanCaused / ChanceCaused) |
| consensus | Emo-FilM에서 항목과 영화마다 별도 평정자 3~4명의 평정을 평정자 안에서 z-score한 뒤 평균한 1 Hz 시계열 |
| 고유 분산, banded ridge | 다른 feature 묶음을 모두 넣은 모형에서 한 묶음을 빼고 다시 적합했을 때 줄어드는 예측력 / band마다 규제 강도를 따로 정하는 선형 회귀 |
| product measure | 고유 분산 대신 쓰는 보조 지표. 각 band의 예측 기여를 band 가중치와 예측의 곱으로 나눠 본다(doi:10.1016/j.neuroimage.2022.119728) |
| 영화 안 circular shift | feature 시계열을 영화 안에서 시간 순서는 유지한 채 임의 시점만큼 밀어, 시간 자기상관을 보존하는 우연 기준선 |
| AI 생성 feature | 사람이 아니라 AI 모델이 자극에서 뽑은 feature. [AI-est]로 표기하고 사람 주석과 섞지 않는다 |
| R0, R2 | 증거 수준 코드. R0 관찰 자료의 상관 분석, R2 새 행동 평정 수집 |

---

## 1. Core Research Question

* **(a) 한 줄 질문:** '누가 누구에게 무엇을 했는가'라는 장면 구조가 정서 반응을 설명할까?
* **(b) 검증 가능한 세부 질문:** 영화 속 부정적 사건에서 '누가 누구에게 무엇을 했는가'(다른 사람이 일으킴, 행위자 없음이나 우연, 주인공이 일으킴)라는 자리 구분 있는 사건 구조가, 같은 인물과 행동을 자리 구분 없이 담은 feature와 물체, 장면, 장면 설명 문장, 사회적 단서, 움직임, 대사를 모두 통제한 뒤에도 Emo-FilM 평정자의 분노, 경멸, 슬픔, 죄책감 평정과 좌측 중간 상측두, TPJ, STS, 내측 전전두, amygdala 반응을 더 설명하는가?

## 2. Scientific Motivation

* appraisal 이론에서 "누가 일으켰는가"(행위 주체, 원인 귀속)는 정서를 가르는 핵심 변수다. 나쁜 결과의 원인을 누군가의 행동에 돌릴 수 있으면 분노, 없으면 슬픔이 된다는 계산적 정식화가 있다(doi:10.1016/j.neubiorev.2022.104977, literature_db 기록).
* 타인 정서 귀속의 신경 표상(ToM 네트워크)은 valence나 arousal보다 appraisal 같은 추상적 사건 특징으로 가장 잘 설명된다. 그러나 그 특징은 사람이 문장을 읽고 매긴 평정이었고, 저자들은 평평한 특징 목록이 사건의 인과와 시간 순서를 담지 못한다고 한계로 적었다(doi:10.1016/j.cub.2015.06.009, Discussion 'Characterizing Representational Spaces' 셋째, 넷째 단락, 본 에이전트 본문 확인).
* 같은 단어로 역할만 바뀐 **문장**("아기가 할아버지를 찼다" 대 "할아버지가 아기를 찼다")에서, 좌측 중간 상측두 피질(lmSTC)이 '누가 누구에게'를 부호화하고 그 패턴이 이 정보에 의존하는 정서 관련 amygdala 반응을 예측한다는 결과가 있다(doi:10.1073/pnas.1421236112, PubMed 초록, 본 에이전트 확인).
* 그러나 이것은 통제된 텍스트 문장에서였다. 자연 영상에서는 사건 구조가 화면에 직접 쓰여 있지 않고, 물체, 사람 수, 움직임, 대사와 함께 섞여 나온다. 컴퓨터 비전의 situation recognition은 영상에서 이 구조를 **자동으로 계산**할 수단을 준다.
* **지식의 공백:** 자연 영상에서 자극으로 계산한 사건 구조가 다른 내용 feature를 넘어 정서 평정과 정서 관련 영역 반응을 설명하는지, 그리고 그 효과가 텍스트에서 보인 lmSTC와 amygdala 관계를 따르는지는 검정되지 않았다(5절).

## 3. Origin of the Idea

* **에이전트 경로:**
  * llm-semantics Round 1: 미해결 문제 P4(상황의 시간적, 인과적 구조), 모델 M8(VidSitu식 의미역, MovieGraphs식 상황 그래프), 아이디어 I2(situation recognition을 정서 encoding feature로), 새 Sub-axis S2(Situation Structure & Relational Semantics)
  * Coordinator Stage 3 전략 경로: 전략 A(Technology Transfer)의 첫 시도(STR-A1, PPI)가 전제 붕괴로 기각되어 STR-A3로 새로 적용
  * Stage 4: 선행 중복 감사 판정 not found로 RQ-43 자리를 대체해 Shortlist에 들어감(`selection.md` 3절)
  * Stage 4 카드 검토(card_review_B 2.1절): 역할 뒤바꾸기 null의 수학적 무효, Frankland & Greene 2015 선행, 목표 변수에 정서 문항 없음을 지적. 이 판에서 재구성
* **가져온 분야:** Computer Vision의 Situation Recognition(imSitu, VidSitu), 언어 신경과학의 구조 의존 문장 의미(Frankland & Greene 2015), 계산 인지과학의 원인 귀속 정식화(Emanuel & Eldar 2023)
* **조합 ID:** STR-A3. Axis C(S2), A(appraisal, 정서 범주), I(AI 모델), E(신경 표적), P(경쟁 모형 비교, 관찰 자료라 R0) + 외부 분야 Situation Recognition in Computer Vision

## 4. Prior Literature

모든 논문은 `outputs/literature/literature_db.csv`에서 verified이거나 본 에이전트 `literature.jsonl`에 식별자로 확인해 넣은 것이다.

| # | 논문 | ID | 읽은 범위 | 이 질문에 주는 기여 |
|---|---|---|---|---|
| 1 | Frankland & Greene 2015, An architecture for encoding sentence meaning in left mid-superior temporal cortex, PNAS | doi:10.1073/pnas.1421236112 | 초록(PubMed) | **가장 가까운 선행.** 같은 단어, 다른 역할 문장에서 lmSTC가 '누가 누구에게'를 부호화하고, 그 패턴이 구조에 의존하는 정서 관련 amygdala 반응을 예측. 행위자와 대상이 인접한 하위 영역에 표상. 통제된 텍스트 자극 |
| 2 | Marras et al. 2025, Neural representation of action features across sensory modalities, NeuroImage | doi:10.1016/j.neuroimage.2025.121439 | 초록(DB 기록) | 행동 feature 6영역(Agent & Object 포함)으로 영화의 시청각, 시각, 청각판 fMRI를 encoding. AON에서 Effector와 Social이 가장 크게 기여, Agent & Object는 작음(감사 기록). 수작업 주석, appraisal과 연결 안 함 |
| 3 | Thornton & Tamir 2024, Nat Commun | doi:10.1038/s41467-024-44870-7 | 초록(DB 기록) | 상황과 정신 상태의 신경 패턴이 허용하는 행동 패턴의 가중합으로 재구성됨. 행동 중심 표상의 근거 |
| 4 | Mohammadi, Van De Ville, Vuilleumier 2023, Cereb Cortex | doi:10.1093/cercor/bhad093 | 초록(DB 기록) | 영화의 정서 순간을 성분(appraisal, 행동 경향 등)으로 평정하고 성분별 네트워크 조합 보고. 자극에서 계산한 feature는 아님 |
| 5 | McMahon, Bonner, Isik 2023, Curr Biol | doi:10.1016/j.cub.2023.10.015 | 초록(PubMed) | 사회 primitive(사람 간 거리, 마주봄)와 사회 상호작용 feature의 lateral stream 위계, 의사소통 상호작용이 STS에서 고유 분산. 경쟁 설명과 표적 영역 근거 |
| 6 | Skerry & Saxe 2015, Curr Biol | doi:10.1016/j.cub.2015.06.009 | 본문 | appraisal 사건 특징이 ToM 영역의 정서 귀속 표상을 가장 잘 설명. 인과, 시간 구조를 담는 표상을 미래 과제로 |
| 7 | Emanuel & Eldar 2023, Neurosci Biobehav Rev | doi:10.1016/j.neubiorev.2022.104977 | DB 기록(본문, brain-inspired 확인) | 원인 귀속이 분노와 슬픔을 가른다는 계산적 정식화. 이 카드의 사전 등록 예측의 이론 근거 |
| 8 | Sadhu et al. 2021, VidSitu, CVPR | arXiv:2104.00990 (doi:10.1109/cvpr46437.2021.00554) | 결론 절(arXiv 본문) | 영화 10초 클립의 2초 사건별 동사, 의미역, 사건 관계 벤치마크. 사건 관계 예측은 여전히 어려움 |
| 9 | Yatskar, Zettlemoyer, Farhadi 2016, imSitu, CVPR | doi:10.1109/cvpr.2016.597 | 미열람(Crossref 서지만) | 이미지 의미역 표지(situation recognition)의 원형 |
| 10 | Morgenroth et al. 2025, Emo-FilM, Sci Data | doi:10.1038/s41597-025-04803-5 | DB 기록(본문, dataset-auditor 확인), Stage 1 보고서 | 50항목 1 Hz consensus, 평정자 일치 평균 0.38~0.39, 평정 주체는 별도 평정자. 참가자 사후 평정에 Agent와 정서 항목 포함 |
| 11 | Morgenroth et al. 2026, Emotion | doi:10.1037/emo0001619 | 초록(DB 기록) | 13개 이산 정서가 appraisal 등 성분으로 예측됨. 정서와 appraisal 평정의 공선성 경고 |
| 12 | Ruder, Uusberg, Sirts 2025, CLPsych | arXiv:2503.16883 | 본문 | GPT-4 reader 주석에서 타인 책임 같은 appraisal은 사람과 모델 모두 맞히기 어려움. LLM 추출의 한계 근거 |
| 13 | Doerig et al. 2025, Nat Mach Intell | doi:10.1038/s42256-025-01072-0 | 본문 | 캡션 언어 모형 표상이 고차 시각 반응을 잘 설명. 캡션 embedding이 구조 정보를 상당 부분 흡수할 수 있다는 공선성 근거 |
| 14 | Houlihan et al. 2023, Phil Trans R Soc A | doi:10.1098/rsta.2022.0047 | 본문 | inverse planning으로 appraisal 계산. 덜 제약된 실세계 장면을 파싱할 일반적 방법이 없다고 적음 |

## 5. Novelty

* **선행 판정: partially(텍스트 문장 패러다임).** Stage 4 감사는 not found였으나, card_review_B 2.1절이 찾은 Frankland & Greene 2015에 따라 Coordinator 지시로 partially로 바꾼다.
* **이미 있는 것(새로움으로 주장하지 않음):**
  * 같은 단어, 다른 역할 **문장**에서 '누가 누구에게'의 신경 부호화(lmSTC)와 그에 의존하는 정서 관련 amygdala 반응(Frankland & Greene 2015).
  * 행위자와 대상을 포함한 수작업 행동 feature로 영화 fMRI를 encoding(Marras 2025).
  * 사회 상호작용 feature의 STS 표상(McMahon 2023), 상황 표상의 행동 합 재구성(Thornton & Tamir 2024), 영화 정서 성분 평정의 네트워크(Mohammadi 2023).
* **남는 새 부분(좁힌 범위):**
  1. **자연 영상의 사건 구조:** 행위자-행동-대상 구조를 사람이 쓴 문장이 아니라 영화 화면에서 **자동으로 계산**한다(situation recognition 또는 MLLM).
  2. **정서와 appraisal 평정과의 연결:** 그 구조가 원인 귀속 이론이 예측하는 정서(분노, 경멸, 슬픔, 죄책감)와 정서 관련 영역 반응을 설명하는지 본다. Agent appraisal은 추출 타당성 점검으로 쓴다.
  3. **내용 통제:** 캡션 embedding, 사회 primitive, 물체, 장면, 움직임, 대사를 함께 통제하고, 자리 구분 없는 단어 묶음과의 중첩 비교로 "구조"의 몫만 잰다.
* **경쟁 예측:**
  * Frankland & Greene 2015: 텍스트에서 보인 lmSTC가 영상에서도 구조를 부호화하는가. 영상에서는 lmSTC가 아니라 시각 사회 영역(pSTS)이 그 역할을 할 수도 있다.
  * Marras 2025: Agent & Object는 AON에서 기여가 작았다. AON 효과가 작아도 이 질문의 예측과 어긋나지 않는다.

## 6. Proposed Dataset

| 필요한 것 | 있는가 | 근거와 주의 |
|---|---|---|
| Emo-FilM 영화 원본(feature 추출용) | 있음(사용자 보유) | G1 필요. 보유본이 연구에 쓴 크레딧 절단 판본과 같은지 **미확인**. 영화별 CC 라이선스 조항 미확인(feature 추출만 하고 영상은 배포하지 않는다). 영화 길이 405~1,028 s |
| Emo-FilM fMRI(30명, 영화 14편, TR 1.3 s, 2.5 mm) | 있음 | 제공 전처리본은 6 mm smoothing과 WM/CSF 회귀 적용 상태. lmSTC 하위 영역과 amygdala 분석은 raw 재전처리를 권장(Stage 1). 이 질문은 연속 시계열을 쓴다(제공본이 연속 시계열이라 충족) |
| 정서 항목 consensus 1 Hz: Anger, Sad, Guilt, Regard(Regard~Contempt 양극), Bad, Good | 있음(CC0) | **평정 주체는 별도 평정자 44명 중 항목, 영화마다 3~4명**이며 fMRI 참가자가 아니다. 평정자 안 z-score라 상대 변화량. 평정자는 같은 영화를 최대 6번 봤다. 문항은 1인칭 경험형("You felt ...") |
| appraisal 항목 consensus: Agent(#9), PleasantOther, GoalsOther, Controlled | 있음(CC0) | Agent는 0단계 타당성 점검에, PleasantOther는 부정 사건 조절 변수 후보로 쓴다 |
| 항목별 평정자 일치도 | 계산 가능(평정자별 원자료 공개) | 항목별 값은 Supplementary에 있고 미열람. 원자료로 재계산한다. 일치도가 0.20보다 낮은 항목, 영화는 목표로 쓰지 않는다(저자 권고 기준) |
| fMRI 참가자 본인의 사후 평정 | 있음(부분) | **Agent(#9)와 정서 항목 포함**(48개 중 Heartrate, Warm만 제외, Stage 1 2.2절). 영화당 5항목이라 영화마다 참가자 3~4명, 클립 약 21개. 규범 평정과 참가자 평정의 일치를 보조 점검으로 쓴다 [Self] |
| 대사 transcript | 없음 | ASR로 생성 [AI 생성 전사] |
| 사람이 단 의미역 주석(Emo-FilM) | 없음 | 소규모 인간 주석(R2)을 새로 받아 추출 품질 점검에 쓴다 |
| VidSitu/VidSRL 공개 checkpoint | **존재와 성능 미확인** | GitHub 접근이 이 세션에서 막혀 확인하지 못했다(reviewer_notes 4.2절과 같은 상태) |
| 장면 캡션 | 없음(Emo-FilM) | MLLM으로 정서 배제 지시 캡션 생성 [AI 생성] |
| 사회 primitive(사람 수, 얼굴 유무, 마주봄) | 없음 | 검출기 또는 MLLM으로 생성 [AI 생성] |
| 생리 신호(PPG, 호흡, EDA, 참가자) | 있음 | 각성 교란 점검(민감도 분석)에만 |
| 보조 재현: Horikawa 2020 + Mind captioning | 있음 | Agent와 정서 문항(분노, 슬픔 등)은 C&K 34범주에 Anger, Sadness 등이 있어 목표로 쓸 수 있다. 사건 구조는 정서 배제 캡션 20개/클립 **[Human 작성, AI 교정]** 에서 텍스트 의미역으로 뽑는다. Mind captioning 학습 자료는 58 run(2,108클립)으로 고정하고 72 시험 클립은 평가에만 쓴다(시험 클립이 학습 마지막 두 run에도 제시됨, 원문 Methods). Mind captioning 원 논문 전처리는 상수, 추세, 머리 움직임 24개, 전역 신호 12개 회귀, 4 s shift, despike, 블록 안 평균, run 안 z-score이고 보유본은 미확인 |

## 7. Proposed Computational Framework

* **Pretrained model**(공개 모델 먼저, 새로 학습하지 않음)
  * 영상 의미역: VidSitu 계열 공개 모델. checkpoint 존재, 성능, 라이선스 모두 **미확인**.
  * 대안: 공개 비디오 MLLM(예: Qwen2.5-VL 7B)에 2초 사건마다 "동사, 행위자, 대상, 각각이 사람인가, 주인공인가"를 정해진 형식으로 답하게 한다. 결과는 **[AI 생성 feature]**. 라이선스 **미확인**.
  * 텍스트 의미역 분석기: ASR 전사와 (보조 재현에서) 사람 캡션에 적용. 도구와 라이선스 **미확인**.
  * 대조 feature: 물체 검출, 장면 분류 모형, 문장 encoder(캡션 embedding), motion energy. 라이선스 **미확인**.
* **Input representation**
  * **자리 구분 있는 구조 band:** 2초 사건마다 [행위자 유형; 대상 유형; 동사 범주]를 이어 붙인 벡터. 행위자와 대상 유형은 "다른 사람", "주인공", "행위자 없음 또는 우연", "동물", "사물"로 나눈다. 직전 사건과의 관계(원인, 반응)도 넣는다.
  * **자리 구분 없는 단어 묶음 band:** 같은 사건에서 [행위자 유형 + 대상 유형; 동사 범주]로 자리 구분 없이 더한 벡터. 구조 band로 계산할 수 있는 값이라 두 모형은 중첩된다. 차원 차이는 무작위 feature를 덧붙여 맞춘다.
  * **부정 사건 조절 변수:** (주) Bad consensus 또는 PleasantOther의 낮은 극. (민감도) 자극에서 계산한 "해를 끼치는 동사" 범주 [AI 생성]. 평정자 공유 분산에 따른 순환을 줄이기 위해 두 판을 함께 보고한다.
  * 통제 band: 물체와 장면 범주, 캡션 embedding(차원 맞춤), 사회 primitive, motion energy, 대사 텍스트 feature.
  * 모든 band는 1 Hz와 TR(1.3 s)로 다시 표본화하고, 뇌 분석에서는 HRF 지연(FIR)을 둔다.
* **Output / target representation:**
  * 행동 목표(주): 정서 consensus 1 Hz 시계열 Anger, Regard(경멸 쪽 극), Sad, Guilt.
  * 행동 목표(0단계 점검): Agent consensus.
  * 뇌 목표: voxel 또는 parcel BOLD 시계열.
* **Training or adaptation strategy:** 모델은 모두 고정. MLLM은 몇 개 예시만 주는 prompt로 쓴다. 추출 품질을 먼저 점검한다(8절 0a). 회귀는 영화 하나를 남기는 교차검증(leave-one-film-out, 14 fold)으로 학습하고, 규제 강도 같은 하이퍼파라미터는 학습 영화 안의 **중첩 교차검증**으로 정한다.
* **Relevant brain regions / networks:** 좌측 중간 상측두 피질(lmSTC, Frankland & Greene 2015. 정확한 parcel 목록은 원문 좌표를 확인해 시작 전에 고정, 현재 미확인), TPJ, pSTS(lateral social stream), dmPFC와 vmPFC, 쐐기앞소엽, amygdala(신호 품질 점검 후 탐색적). 경쟁 영역: AON(전운동, 두정내구; Marras 2025). 음성 대조: 초기 시각피질.
* **Loss function or statistical objective:** banded ridge의 제곱 오차. 평가는 보류 영화에서 예측과 실측의 상관과 설명 분산. 주 통계량은 (1) 구조 band의 단어 묶음 band 대비 고유 분산(중첩 모형 비교), (2) 구조 x 부정 사건 상호작용의 고유 분산, (3) 시험 단계 자리 바꾸기에 따른 예측 감소량. 행동 목표는 항목별 평정자 일치도(상한) 대비 비율도 보고한다.
* **Interpretability method:** 구조 성분별 가중치(어떤 구조가 어떤 정서를 움직이는가), 거꾸로 나눈 variance partitioning과 product measure, 구조 band와 캡션 band의 정준상관(공선성 크기), 역할을 바꾼 캡션 문장의 encoder 거리(캡션 band가 구조에 민감한가).

## 8. Proposed Analyses

### 0단계 (전제 확인)
* **0a. 추출 품질 관문.**
  * 공개 VidSitu 계열 checkpoint를 구할 수 있으면 그것과 MLLM 추출을 VidSitu 검증 자료의 사람 주석에 견준다(검증 자료 접근 가능 여부 미확인).
  * Emo-FilM에서 무작위로 뽑은 약 100개 사건에 사람 두 명이 행위자 유형, 대상 유형, 동사를 단다(R2). 사람끼리의 일치와 모델-사람 일치를 함께 계산한다.
  * 행위자 유형 일치가 사전에 정한 기준(Cohen's kappa 0.6)에 못 미치면 뇌 분석으로 가지 않는다.
* **0b. 텍스트 구조 민감도 점검(Frankland & Greene식).** 역할만 바꾼 캡션 문장 쌍을 만들어 문장 encoder 표상이 얼마나 달라지는지 잰다. 거의 같다면 캡션 band는 구조를 담지 못하는 것이고, 크게 다르다면 캡션 band가 구조를 일부 흡수할 수 있으므로 공선성 해석을 미리 조정한다.
* **0c. 목표 신뢰도.** 평정자별 원자료로 Anger, Regard, Sad, Guilt, Agent, Bad의 영화별 평정자 쌍 상관을 다시 계산한다. 평균이 0.20 미만인 항목, 영화는 목표에서 뺀다.
* **0d. Agent 타당성 점검.** 구조 band의 "행위자 = 사람" 성분이 Agent consensus를 예측하는지 본다. 정의상 거의 같은 내용이라 예측되는 것이 당연하다. 예측되지 않으면 추출이나 시간 정렬에 문제가 있다는 신호다. 참가자 사후 Agent 평정과 규범 Agent의 일치도도 함께 본다.
* **0e. 공선성 진단.** 구조 band와 캡션, 사회 primitive band의 정준상관을 보고한다.

### 1단계 (행동: 구조가 정서 평정을 설명하는가)
* **사전 등록 예측(원인 귀속 정식화, doi:10.1016/j.neubiorev.2022.104977):** 부정 사건에서
  * "다른 사람이 행위자, 사람이 대상" 구조는 Anger와 경멸(Regard의 낮은 극)을 높인다.
  * "행위자 없음 또는 우연" 구조는 Sad를 높인다.
  * "주인공이 행위자, 다른 사람이 피해" 구조는 Guilt를 높인다(관객의 주인공 동일시를 가정한 약한 예측, 탐색적).
* **주 검정:** 보류 영화에서 (통제 band + 단어 묶음) 모형 대비 (통제 band + 단어 묶음 + 구조 + 구조 x 부정 사건) 모형의 예측력 증가. 기준선: 차원 맞춘 무작위 band.
* **시험 단계 자리 바꾸기 null:** 원래 구조로 학습한 모형에 보류 영화의 행위자와 대상 자리를 바꾼 feature를 넣어 예측 감소량을 잰다.

### 2단계 (뇌: 구조가 정서 관련 영역을 설명하는가)
* voxel과 parcel별 banded ridge. 표적 ROI에서 구조 band의 단어 묶음 대비 고유 분산, 구조 x 부정 사건 상호작용의 고유 분산, 시험 단계 자리 바꾸기 감소량.
* lmSTC 경쟁 예측: 텍스트에서 보인 lmSTC가 영상에서도 구조 고유 분산을 보이는가, 아니면 pSTS 쪽에서만 보이는가.
* 구조와 정서의 연결: 뇌 분산 중 정서 평정이 설명하는 부분이 구조 band와 얼마나 겹치는가(공통 분할).

### 3단계 (보조 재현)
* Horikawa 2020 + Mind captioning: 사람 캡션에서 텍스트 의미역을 뽑아, C&K 34범주의 Anger, Sadness 등과 14차원 중 Control, Fairness, Obstruction, 그리고 뇌 반응을 같은 방식으로 분석한다. 클립이 짧고 자극이 무음이라 약한 재현이다.

### 비교 조건, baseline, ablation
* baseline: 통제 band만의 모형, 통제 + 단어 묶음 모형, 차원 맞춘 무작위 band.
* 보조 null: 사건의 무작위 절반만 자리를 바꾼 band(학습 단계 적용), 역할을 바꾼 캡션 문장을 문장 encoder로 다시 부호화한 band.
* ablation: 구조 성분 하나씩 빼기(행위자 유형, 대상 유형, 사람→사람 여부, 주인공 여부, 사건 관계), 추출 방법(VidSitu 계열 대 MLLM), 캡션 encoder 종류, 부정 사건 조절 변수의 두 판(평정 기반 대 자극 기반).
* 민감도: 추출 확신도(confidence)를 공변량으로, 크레딧 절단 판본 차이가 있으면 시간 정렬 오차 보정, 생리 신호와 전역 신호 공변량.

### 통계 검정과 검증 전략
* leave-one-film-out(14 fold), 하이퍼파라미터는 중첩 교차검증, 영화 고정효과.
* 우연 기준선은 영화 안 circular shift 또는 위상 무작위화(시간 자기상관 보존). 영화 길이가 405~1,028 s로 달라 영화 사이를 맞바꾸는 순열은 쓰지 않는다.
* 피험자별 결과와 유병률(30명 중 몇 명), parcel FDR.
* 분석 계획을 시작 전에 고정한다. 0a 관문 기준(kappa 0.6)과 0c 신뢰도 기준(r 0.20)도 미리 적는다.

### 반증 조건 (Falsifiability)
* **가설이 지지되지 않는 경우:**
  * 행동: 보류 영화에서 구조와 구조 x 부정 사건 band가 단어 묶음 모형 대비 정서 평정 예측력을 차원 맞춘 무작위 band 기준선보다 늘리지 못하고, 시험 단계 자리 바꾸기로 예측이 줄지 않는다.
  * 뇌: 표적 ROI(lmSTC, TPJ, pSTS, 내측 전전두) 어디에서도 구조 band의 단어 묶음 대비 고유 분산이 무작위 band 기준선과 circular shift null을 넘지 않는다.
  * 사전 등록 방향 예측(분노는 타인 행위자, 슬픔은 행위자 없음)이 반대로 나오면 원인 귀속 예측은 기각한다.
  * 효과가 중립 구간과 부정 사건 구간에서 같고 AON과 초기 시각피질에서만 크면, 구조가 운반하는 것은 정서가 아니라 행동 지각 정보라는 해석이 된다.
* **판정 불가:** 0a 추출 품질 관문을 통과하지 못하거나, 0c에서 목표 정서 항목의 평정자 일치가 기준에 못 미치면 결론을 내지 않는다. 0e에서 구조 band와 캡션 band가 거의 같으면 "구조 정보는 캡션 의미에 이미 들어 있다"까지만 보고한다.

## 9. Competing Explanations

| 대안 해석 | 그것을 가르는 분석 |
|---|---|
| 효과는 구조가 아니라 "사람이 나오는가, 몇 명인가, 얼굴이 보이는가" 같은 사회 primitive다 | 사회 primitive band를 통제 band에 넣는다(McMahon 2023의 primitive 목록 참고) |
| 효과는 구조가 아니라 어떤 인물, 동작이 나오는가(단어 수준 내용)다 | 자리 구분 없는 단어 묶음과의 중첩 모형 비교, 시험 단계 자리 바꾸기 null |
| 캡션 embedding이 이미 구조를 담고 있다 | 0b 역할을 바꾼 캡션 쌍의 encoder 거리, 0e 공선성 진단, 공유 분산 보고 |
| 정서와 무관한 행위 주체성 지각(누가 무엇을 하는지 보는 것) 자체다 | 같은 구조 feature의 고유 분산을 정서적으로 중립인 구간(Good과 Bad 모두 낮음)과 부정 사건 구간에서 비교. 중립 구간에서도 같으면 정서 해석은 지지되지 않는다 |
| 행동의 운동학(움직임)이다 | motion energy와 영상 모형 band 통제 |
| 대사 내용(누가 누구를 탓하는가) 때문이다 | ASR 전사 텍스트 band 통제 |
| 부정 사건 조절 변수(Bad, PleasantOther)와 정서 평정이 같은 평정자군에서 나와 순환이 생긴다 | 자극에서 계산한 "해를 끼치는 동사" 조절 변수로 같은 분석을 반복 |
| 정서 평정은 장면 구조가 아니라 평정자가 반복 시청으로 아는 줄거리를 반영한다 | 현재와 직전 사건 구조만 쓰는 모형과 영화 전체 맥락 모형의 비교, 평정 시점 지연 분석 |
| MLLM 추출 오류가 어둡거나 빠른 장면(공포, 각성)에 몰려 정서와 섞인다 | 추출 확신도 공변량, 영화별 추출 정확도(0a) |
| 영화 수준 교란(영화 14편의 장르, 음악) | leave-one-film-out, 영화 고정효과 |
| 각성이나 몸 상태가 TPJ, amygdala 신호를 만든다 | 생리 신호(참가자 PPG, 호흡, EDA)와 전역 신호를 공변량으로 한 민감도 분석 |

## 10. Potential Findings

1. **구조와 구조 x 부정 사건이 단어 묶음을 넘어 분노, 슬픔 평정과 lmSTC 또는 pSTS, TPJ 반응을 설명하고, 방향이 원인 귀속 예측과 맞는다.** 텍스트에서 보인 '누가 누구에게'의 정서적 효과가 자연 영상에서 자극으로 계산한 구조로도 나타난다는 관찰 증거(R0). 원인 귀속 이론의 예측이 자연 자극 평정에서 지지된다.
2. **행동(정서 평정)에는 효과가 있으나 뇌에는 없다.** 평정자가 판단할 때 쓰는 구조 정보가 fMRI 참가자의 해당 영역 신호로는 보이지 않는다. 평정 주체가 다르다는 점(별도 평정자 대 참가자)과 함께 해석한다.
3. **효과가 단어 묶음과 같다(구조 몫 없음).** 자연 영상에서는 "누가 누구에게"보다 "누가, 무엇이 나오는가"가 중요하다. Frankland & Greene 2015의 텍스트 결과가 자연 영상으로 일반화되지 않거나, 현재 추출로는 잡히지 않는다.
4. **효과가 중립 구간에서도 같고 AON에서 크다.** 구조가 행동 지각을 운반한다. Marras 2025와 부합하며 정서 해석은 지지되지 않는다.
5. **캡션 embedding이 구조를 다 흡수한다.** 구조 정보는 언어 표상 안에 이미 있다. RQ-08과 같은 방향의 결과로, "장면 의미"의 범위에 구조도 포함해야 한다는 정보가 된다.
6. **lmSTC가 아니라 pSTS에서만 나타난다.** 영상에서 구조를 다루는 곳이 텍스트와 다르다는 정보다. 다만 두 영역이 인접해 공간 해상도(2.5 mm, smoothing)의 한계를 함께 적는다.

## 11. Scientific Contribution

* appraisal 이론의 원인 귀속 변수를 **자극에서 계산 가능한 사건 구조**로 바꿔, 평정에 기대던 appraisal 신경 연구를 한 단계 객관화한다. 원인 귀속이 분노와 슬픔을 가른다는 예측을 자연 자극의 평정과 뇌 반응으로 시험한다.
* 텍스트 문장에서 보인 구조 의존 의미의 신경 부호화(Frankland & Greene 2015)가 자연 영상에서도 같은 영역과 같은 정서 연결을 보이는지 묻는다.
* 정서 대 의미 분리 논의(K2)를 "무엇이 있는가"와 "누가 누구에게 무엇을 했는가"로 세분한다.
* 방법 면의 기여(구조 대 단어 묶음 중첩 비교, 시험 단계 자리 바꾸기 null)는 이 카드의 수정된 정의에 한해서 주장한다. 이전 판의 "역할 뒤바꾸기 band"는 선형 모형에서 원 feature와 같은 예측을 내므로 대조가 아니었다.

## 12. Limitations & Risks

* **AI 생성 feature:** 의미역, 캡션, 사회 primitive, 전사가 모두 모델 산출물이다. 사람 주석 점검(0a)은 일부 사건만 덮는다.
* **추출 정확도:** 공개 VidSitu 계열 모형의 존재와 성능이 미확인이다. VidSitu 논문도 사건 관계 예측이 어렵다고 적었다. MLLM은 타인 책임 같은 appraisal을 맞히기 어렵다(arXiv:2503.16883). "주인공" 판정은 특히 불확실하다.
* **평정 주체:** 정서와 Agent 평정은 별도 평정자 3~4명의 consensus이고 fMRI 참가자가 아니다. 평정자 내 z-score라 절대 수준이 아니다. 평정자는 같은 영화를 여러 번 봤다. 참가자 사후 평정은 영화당 5항목, 약 21클립으로 희소하다.
* **관객 관점과 인물 관점:** 정서 문항은 평정자 자신의 경험("You felt ...")이다. 인물의 정서가 아니다. Guilt 예측은 관객이 주인공과 동일시한다는 가정에 기댄다.
* **영화 14편:** 영화 수준 교란과 낮은 검정력.
* **전처리와 해상도:** 제공본은 6 mm smoothing. lmSTC 하위 영역과 pSTS의 구분, amygdala 신호는 재전처리 후에도 3T, 2.5 mm에서 제한된다.
* **관찰 자료:** R0. 구조가 정서를 일으킨다는 인과 결론은 없다.
* **판본 차이:** 보유 영화가 크레딧 절단 판본과 다르면 시간 정렬 오차가 생긴다.
* **라이선스:** checkpoint 라이선스 미확인, 영화별 CC 조항 미확인.

## 13. Pilot Experiment

* **가장 작은 분석(순서대로):**
  1. 0b 텍스트 구조 민감도: 역할만 바꾼 캡션 문장 쌍 수십 개로 문장 encoder 거리 측정(영상 불필요, 수 분).
  2. Emo-FilM 영화 2편에서 MLLM 의미역 추출과 사람 주석 50개 사건 비교(0a).
  3. 정서 항목과 Agent의 평정자 일치 재계산(0c), Agent 타당성 점검(0d).
  4. 보류 영화 1편으로 Anger, Sad 예측: 통제 + 단어 묶음 대 + 구조 + 구조 x 부정 사건, 시험 단계 자리 바꾸기 감소량.
* **필요한 것:** 영화 원본 2편, ds004872 평정자 원자료, 공개 MLLM 1개, 문장 encoder 1개, 사람 주석자 2명(몇 시간).
* **계산:** GPU 1장으로 2초 사건 수백 개 추출이 가능하다고 추정(영화 14편 전체 약 2.7시간이면 약 4,800 사건). 계산 자원 **미확인**, GPU 1~4장 가정.
* **진행 기준:** 행위자 유형 일치가 기준을 넘고, 행동 수준에서 구조가 단어 묶음보다 정서 평정을 더 잘 예측하면 뇌 분석으로 간다. 행동 수준에서 차이가 없으면 뇌 분석은 탐색으로만 하고 우선순위를 낮춘다.

## 14. Feasibility & Priority

* **점수(`outputs/evaluation/scores_final.csv`, 1~5):** Novelty 4, Neuroscientific Importance 4, AI / Modeling Contribution 4, Dataset Feasibility 3.5, Methodological Rigor 3, Falsifiability 4, Interpretability 3.5, Generalizability 3, Feasibility 3.5. **합계 32.5(공동 7위)**, 과학 기준 5개 합 18.5. 이번 재구성으로 점수는 바꾸지 않았다.
* **선행 판정 변경의 영향:** 감사 판정이 not found에서 partially로 바뀌므로 Novelty 4는 과대일 수 있다(card_review_B). `selection.md` 5절은 32.5 동점에서 not found를 우선해 이 질문을 상위 5개에 넣었는데, 이제 그 근거 대신 과학 기준 5개 합(RQ-14 18.5, RQ-33 18.0, RQ-60 17.0)으로 동점을 가리게 된다. 점수가 그대로면 순서는 같다. 최종 판단은 Coordinator 몫이다.
* **순위:** Substantive Shortlist 10번(RQ-43 대체, 군집 K2 3번째로 다양성 규칙의 예외), High-priority Candidates 5위. Pilot에는 들지 않았고 Emo-FilM 쪽 다음 후보다(`selection.md` 6절). 카드 검토 판정: 재구성 필요(질문은 유지 가능) → 이 판에서 재구성.
* **계산 자원:** 미확인. GPU 1~4장 가정.
* **overlap:**
  * **EmoBrain(구 EmoViS 범위):** 부분 겹침. 정서 대 의미 내용 분리라는 물음이 같다. 이 질문은 사건 구조와 원인 귀속으로 범위를 좁힌다.
  * **Emo-FilM 연구:** 부분 겹침. 같은 Emo-FilM 자료에서 사전학습 모형으로 정서 맥락의 기여를 분석한다는 점이 같다. 이 질문은 맥락 전체가 아니라 행위자-대상 구조와 원인 귀속 정서에 한정한다.

---

## 반영하지 않은 지적

| 지적 또는 원안 요소 | 출처 | 반영하지 않은 이유 | 결론 범위에 주는 영향 |
|---|---|---|---|
| 보조 데이터 "Horikawa 2020(정적 장면 판본)", 즉 정지 프레임에 이미지 의미역(imSitu식)을 적용 | `matrix.csv` STR-A3 dataset 열 | 정지 프레임은 행동과 사건 관계를 잃는다. 대신 Mind captioning의 사람 캡션 20개에서 텍스트 의미역을 뽑는 방식으로 바꿨다(3단계). card_review_B도 사유가 타당하다고 판정했다 | 보조 재현은 사람 문장에서 뽑은 구조라, 영상에서 계산한 구조의 재현이 아니라 "같은 구조 개념의 텍스트판 재현"으로만 해석한다 |

---

## Safeguards 점검

| 항목 | 이 질문에서의 처리 |
|---|---|
| 참가자 경험 vs 자극에 묘사된 정서 | 목표는 별도 평정자가 자기 관점에서 매긴 정서와 appraisal 평정이다. 참가자 경험이 아니며 인물 정서도 아니다. 구조 feature는 자극에 묘사된 사건 구조다 |
| 인간 평정 vs 모델 생성 평정 | 구조, 캡션, 사회 primitive, 전사, 해를 끼치는 동사 범주는 [AI 생성 feature]. 목표 변수는 인간 평정만. 사람 주석 점검(R2) 결과를 함께 보고 |
| 본인 보고 vs 규범 평정 | 목표는 규범(consensus) 평정. 참가자 사후 평정(Agent와 정서 항목 포함, 희소)은 보조 점검 [Self] |
| 정서 표상 vs 시각, 의미 내용 표상 | 물체, 장면, 캡션, 사회 primitive, 움직임, 대사 band 통제, 단어 묶음과의 중첩 비교, 중립 구간 대조 |
| encoding 정확도 vs 설명적 적절성 | 고유 분산이 있어도 "구조를 표상한다"가 아니라 "구조 feature가 추가로 예측한다" |
| decodability vs 표상 vs 인과 | R0. 인과 주장 없음 |
| in-silico vs 관찰 | 관찰. MLLM은 feature 추출 도구 |
| 공유 표상 vs 데이터셋 특이 교란 | 주 데이터 하나(Emo-FilM). Horikawa + Mind captioning 보조 재현은 약함 |
| 탐색 vs 확인 | 0a 관문 통과 후 사전 등록 예측(분노, 슬픔)과 사전 지정 ROI는 확인, Guilt 예측과 그 밖은 탐색 |
| HRF 지연과 시간 자기상관 | FIR 지연, 영화 안 circular shift와 위상 무작위화 null |
| 자극, 영화, 피험자 단위 누수 | leave-one-film-out, 하이퍼파라미터 중첩 교차검증. 같은 영화의 시간 구간을 학습과 시험에 나누지 않음. 보조 재현에서 Mind captioning 72 시험 클립은 학습에서 제외(58 run, 2,108클립) |
| 반복 자극 교란 | 영화당 1회 시청(fMRI 참가자). 평정자는 반복 시청(한계) |
| 평정자 일치와 라벨 잡음 | 목표 항목의 평정자 일치를 원자료로 재계산해 상한과 제외 기준으로 사용 |
| 시각-의미-정서 공선성 | 공선성 진단(0e), 차원 맞춘 band, 거꾸로 나눈 분할, 0b 텍스트 구조 민감도 |
| 시공간 해상도 | TR 1.3 s, 2.5 mm, 1 Hz 평정. 2초 사건 단위. lmSTC와 pSTS 구분에 한계 |
| ROI 선택과 순환 추론 | ROI는 문헌으로 사전 지정(lmSTC parcel 목록은 시작 전 고정), 결과로 다시 고르지 않음 |
| 다중 비교 | parcel FDR, 피험자 유병률, 사전 등록 예측의 수 제한 |
| 자료 접근, checkpoint 라이선스 | 자료 보유. VidSitu 계열 checkpoint 존재와 라이선스, MLLM 라이선스 미확인 |
| 사전학습 오염 | Emo-FilM 영화(LIRIS-ACCEDE 계열 CC 영화)가 MLLM 학습 자료에 들어갔을 가능성 등록. 줄거리 기억이 추출에 섞일 수 있음 |
| 데이터셋 간 주석 비호환 | Emo-FilM 50항목과 C&K 34범주 + 14차원은 다른 척도. 보조 재현은 이름이 대응하는 범주의 순위 수준 비교로만 |
| **label-provenance** | 목표: 대상 felt(정서), appraisal(원인 귀속), 주체 별도 평정자 규범(consensus). 보조: 참가자 본인 사후 평정. feature: AI 추정(구조, 캡션, primitive, 전사). Mind captioning 캡션은 [Human 작성, AI 교정]. 사람 주석 점검은 별도 인간 주석자(R2) |
| **evidence-level** | R0(사람 주석 점검은 R2) |
| **insilico-vs-observed** | 관찰 |
| **G1** | 필요(영화 원본 보유, 판본 확인 필요) |
| **signal-feasibility** | 피질 ROI 양호. amygdala는 3T, 2.5 mm, 제공본 6 mm smoothing이라 재전처리 후 tSNR 점검, 탐색적 |
| **minimum-validation (7항목)** | ○ = 충족, △ = 부분 충족. (1) 경쟁 모형과 차원 맞춘 null: 단어 묶음 중첩 비교, 무작위 band, 시험 단계 자리 바꾸기 ○ (2) 원 정확도와 상한: 항목별 평정자 일치 상한 ○ (3) 내용 지표 다중화와 신뢰도 민감도: 캡션 encoder 여러 개, 추출 확신도, 조절 변수 두 판 △ (4) 누수 경로별 대응: 영화 단위 fold, 중첩 교차검증, 사전학습 오염 등록 ○ (5) 일반화 수준: 같은 사람 새 영화와 피험자 유병률 ○ (6) 라벨 출처 표시 ○ (7) 반증 해석 사전 기술 ○ |

---

## 검토 반영 기록

출처: `outputs/evaluation/card_review_B.md` 2.1절(번호 1~9)과 1절 공통 지적, Coordinator 공통 데이터 사실.

| 지적 | 등급 | 처리 | 위치 |
|---|---|---|---|
| 1. 역할 뒤바꾸기 band가 선형 모형에서 원 feature와 같은 예측을 내 반증 조건이 늘 성립. 판별력 있는 대조로 교체 | 필수 | 반영. 주 검정을 구조 대 단어 묶음 중첩 비교로, null을 시험 단계 자리 바꾸기로 바꾸고, 무작위 절반 바꾸기와 문장 재부호화를 보조 null로 둠. 이전 판의 방법론 기여 주장 철회 | 용어표, 7절 Input과 Loss, 8절 1, 2단계, 보조 null, 반증 조건, 11절 넷째 항목 |
| 2. Frankland & Greene 2015 선행. 판정을 partially로, 새로움을 좁히고 lmSTC를 표적과 경쟁 예측에 추가 | 필수 | 반영 | 2절, 4절 #1, 5절, 7절 ROI, 8절 2단계, 10절 결과 6, 14절 |
| 3. 목표 변수에 정서 문항이 없음. 정서 문항을 목표로, 원인 귀속 예측 사전 등록, Agent는 0단계 점검으로 | 필수 | 반영. Anger, Regard(경멸), Sad, Guilt를 목표로, 구조 x 부정 사건 상호작용을 주 검정으로, Agent 예측을 0d로 내림 | 1절 (b), 6절, 7절 Output, 8절 0d와 1단계, 10절 |
| 4. 참가자 사후 평정에 Agent 포함(Stage 1 2.2절) | 권장 | 반영 | 6절 참가자 사후 평정 행, 8절 0d, Safeguards |
| 5. 영화 단위 순열을 영화 안 circular shift 또는 위상 무작위화로 | 권장 | 반영 | 용어표, 8절 통계 검정, Safeguards |
| 6. 정서와 무관한 행위 주체성 지각 대안 추가, 중립 구간 대 부정 사건 구간 비교 | 권장 | 반영 | 9절 넷째 행, 8절 반증 조건, 10절 결과 4 |
| 7. 하이퍼파라미터 중첩 교차검증 명시 | 권장 | 반영 | 7절 Training, 8절 통계 검정, Safeguards |
| 8. 설명 없는 용어(product measure, R0/R2, ○ △)에 풀이 | 선택 | 반영 | 용어표, Safeguards minimum-validation 행 |
| 9. Frankland & Greene식 텍스트 점검을 Pilot 첫 단계로 | 선택 | 반영 | 8절 0b, 13절 1번 |
| 공통 1.2: Emo-FilM 평정 주체와 생리 서술 유지, Agent 포함 정정 | 공통 | 반영 | 6절 |
| 공통 사실: Mind captioning 학습 58 run(2,108클립) 고정, 72 시험 클립 학습 제외 | 공통 | 반영(보조 재현에 적용) | 6절 보조 재현 행, Safeguards 누수 |
| 공통 사실: Mind captioning 캡션 [Human 작성, AI 교정] | 공통 | 반영 | 6절 보조 재현 행, Safeguards label-provenance |
| 공통 사실: Mind captioning 원 논문 전처리 순서와 보유본 미확인 | 공통 | 반영 | 6절 보조 재현 행 |
| 공통 사실: 연속 시계열이 필요한 분석은 데이터 표에 명시 | 공통 | 반영(주 분석은 Emo-FilM 연속 시계열을 쓰며 제공본이 연속 시계열이라 충족) | 6절 fMRI 행 |
