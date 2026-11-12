# 기각한 조합과 사유

* 생성: `python3 -I outputs/combinations/build_matrix.py` (조합 원자료는 스크립트 안에 있다)
* 기각 22개(문헌 경로 3, 무작위 경로 16, 전략 경로 3). 그 밖에 Round 4 에이전트가 기각한 미논의 Axis 쌍 10개를 3절에 옮겼다.
* 다른 조합으로 통합한 경우(질문은 되지만 같은 질문)는 기각이 아니라 kept(방향만 유지)로 matrix.csv의 note에 적었다.

## 1. 문헌 경로

| 조합 | 출처 | Axis | 내용 | 기각 사유 |
|---|---|---|---|---|
| LIT-25 | SN-P5 | E+W+Q+A | Mind captioning 반복에서 amygdala 반응의 반복 비정상성 | 유형 규칙은 충족(Construct, Neural, Inference)하나 외부 분야 Axis(I, J, K, L, R 또는 외부 분야)가 없다. 독립 질문보다는 LIT-10, LIT-12의 nuisance 모형(반복 번호 x 규범 arousal)으로 흡수 |
| LIT-54 | GI-P6, LS-P6(언어 특이 판본) | K+A+C+U+O | 일본어 화자 뇌 공간에서 일본어 범주 분할이 영어 분할보다 IB 효율적인가 | adversarial-reviewer 상위 10개 검토 9.3절: 영어 화자 뇌 코호트가 없고(Horikawa 2020 참가자 언어 미확인, 같은 교토 연구실 획득), 한 뇌 공간에서 두 명명 체계를 비교하면 일본어 우위가 언어 일치 때문인지 명명 수집 절차, 범주 수, 평정자 집단 차이 때문인지 구분되지 않는다. Round 2에서 반박되었어야 할 주장. 언어 무관 판본은 LIT-18로 유지 |
| LIT-35 | FA-P8 | T+R+Q+S | 해석 도구(SAE, 정서 vector)의 검증 기준 | 유형 2개(Structure, Inference)뿐이라 조합 규칙 미충족. 질문이 아니라 검증 기준이므로 minimum-validation 태그와 adversarial-reviewer V1~V12에 반영 |

## 2. 무작위 경로 (seed 20261113)

| 조합 | 출처 | Axis | 내용 | 기각 사유 |
|---|---|---|---|---|
| RND-08 | random_combos.csv | B+E+I+R+T | 모델 계열별 amygdala 설명력 비교 | Novelty Constraint: 'Foundation Model로 정서 관련 반응을 예측'하는 수준. Jang & Kragel 2025가 AI 모델로 amygdala 기능을 이미 분석했고, 해석 단계는 RND-03(LIT-31)과 중복 |
| RND-11 | random_combos.csv | V+F+G+R+S | 행동 경향 decoding의 데이터셋 간 일반화 | 행동 경향 라벨이 Emo-FilM에만 있어 다른 데이터셋에서는 AI 생성 라벨로 평가해야 하므로 순환적이다(emotion-theory, frontier-ai Round 4의 S+V 기각과 같은 이유). latent action 자체의 decoding은 정서 질문이 아니다 |
| RND-12 | random_combos.csv | A+E+M+K+Q | 다중양식 통합이 정서 기하를 날카롭게 하는가 | 관찰 데이터에서 소리 유무와 자극이 함께 바뀐다(Round 3 EF-P7 검토). 같은 자극 비교는 LIT-11이 이미 다룬다 |
| RND-13 | random_combos.csv | W+O+N+K+P | 회상 재활성 충실도의 개인차 | 회상 데이터(Mind captioning)는 6명이라 개인차(O) 추론이 불가하고, 회상에 대한 개입(P)이 없다 |
| RND-15 | random_combos.csv | C+O+H+K+T | 서사 해석 개인차와 공유/특이 기하 | IS-RSA로 서사 해석 개인차와 뇌 유사성의 관계는 이미 연구되었다(Finn 2020, Chen 2020). 정서 쪽 개인차는 LIT-02가 다룬다 |
| RND-18 | random_combos.csv | W+E+N+K+P | 회상 중 successor 재활성 | 회상 클립은 서로 독립인 짧은 클립이라 전이 구조가 없고, 회상에 대한 개입도 없다(brain-inspired Round 4의 N+W successor 기각과 같은 이유) |
| RND-19 | random_combos.csv | W+O+L+K+Q | 생성 재구성으로 본 회상 정서 충실도의 개인차 | LIT-12, LIT-29와 중복이고 회상 데이터 6명으로 개인차 추론 불가 |
| RND-20 | random_combos.csv | D+O+M+K+U | 개인별 양식 가중치의 시간 변화 | RND-10과 같은 질문(이미 하위 질문으로 보류) |
| RND-21 | random_combos.csv | B+F+I+K+U | 지각 표상 기하와 라벨 출처 | RND-09와 같은 질문(지각 feature가 아니라 정서 기하가 대상일 때만 의미) |
| RND-22 | random_combos.csv | C+E+M+K+T | 대사와 음악의 정서 기하 기여 | LIT-23, LIT-11과 중복 |
| RND-23 | random_combos.csv | C+O+I+K+U | 개인 정서 기하와 모국어 LLM 정렬 | LIT-18과 중복. Horikawa 2020 참가자 언어가 확인되지 않았고 Mind captioning 6명으로 개인 수준 언어 효과 추론 불가 |
| RND-25 | random_combos.csv | B+O+I+K+P | 지각 정렬의 개인차와 인과 | LIT-17과 중복이고, 관찰 데이터만으로 인과(P) 경로가 없다 |
| RND-26 | random_combos.csv | V+E+G+R+Q | 행동 경향 decoding의 신뢰도 | RND-11과 같은 순환 라벨 문제. 측정 신뢰도는 LIT-45가 다룬다 |
| RND-27 | random_combos.csv | V+E+L+R+Q | affordance 편집의 신뢰도 | LIT-07, RND-04와 중복 |
| RND-28 | random_combos.csv | W+O+I+K+T | 회상 기하 모델 비교의 개인차 | RND-06과 중복이고 회상 6명으로 개인차 추론 불가 |
| RND-29 | random_combos.csv | B+E+I+K+U | 지각 feature 모델과 라벨 출처 | Novelty Constraint(모델 예측 비교 수준)이고 RND-08, RND-09와 중복 |

## 3. 전략 경로

| 조합 | 출처 | Axis | 내용 | 기각 사유 |
|---|---|---|---|---|
| STR-A1 | Strategy A(Technology Transfer): 통계학의 prediction-powered inference | U+Q+I+F+A | Spacetop 본인 평정 결측을 MLLM 평정으로 보충하고 PPI로 보정 | adversarial-reviewer 상위 10개 검토로 전제가 무너져 기각: (1) MLLM 평정은 같은 영상 안에서 사람마다 같아 사람 수준 편차에 정보가 없고, TRIBE와 짝지으면 가짜 연결(r 약 +0.36)을 만든다. (2) 결측은 시행/런 단위 전부-또는-없음 구조로 값 의존 결측 증거가 없어 보완의 이득이 작다. 영상 수준 질문에서 AI 라벨 활용은 LIT-15, LIT-46이 다룬다 |
| STR-A2 | Strategy A: 정서 분류 foundation model의 fMRI 정서 decoding 전이 | A+F+I+S | foundation model 전이로 정서 decoding 정확도 향상 | Novelty Constraint: '새로운 모델로 emotion classification accuracy를 높인다'에 해당. 과학적 질문 없음 |
| STR-B2 | Strategy B: 뇌에서 정서 영상 재구성 | A+G+L+F | decoding을 생성으로 뒤집어 정서 영상을 재구성 | 재구성 품질 개선은 Novelty Constraint 대상이고, 생성기 prior가 정서를 중립화하거나 주입하는 confound(VD-P4, LIT-29)가 해석을 막는다 |

## 4. Round 4에서 에이전트가 기각한 미논의 Axis 쌍

`outputs/combinations/discussed_pairs.md`의 미논의 쌍 가운데 Round 4 에이전트가 검토 후 질문으로 만들지 않은 것이다. 근거는 각 `outputs/agents/<이름>/round4.md`의 기각 절.

| 쌍 | 기각한 에이전트 | 사유 |
|---|---|---|
| K+L | geometry-info, llm-semantics | 지금 가능한 것은 encoder 위 R1뿐이고 EF-P1(LIT-05) 관문을 통과하지 않았다. affective metamer와 같은 질문(geometry-info). 서사 8편 encoder로는 in-silico 예측을 믿기 어렵다(llm-semantics) |
| P+W | geometry-info, frontier-ai, llm-semantics(흡수) | 회상은 cue 텍스트와 재제시 때문에 깨끗한 개입이 아니다. llm-semantics는 LS-R4-2(LIT-49)의 통제 조건으로 흡수 |
| O+V | geometry-info(보류), brain-inspired, emotion-theory, frontier-ai | 개인 수준 행동 경향 측정이 없다. Emo-FilM BIS/BAS는 30명으로 r 약 0.49 이상만 검출 가능(brain-inspired) |
| P+V | brain-inspired, frontier-ai | 데이터 안의 실제 개입(Spacetop 기만 cue)에는 행동 경향 측정이 없고, 편집 기반 검정은 GC-P8(LIT-07)로 이미 논의 |
| T+V | brain-inspired, frontier-ai, llm-semantics | minimum-validation 태그를 넘는 별도 질문이 없다 |
| T+W | emotion-theory, frontier-ai | benchmark로 환원된다 |
| S+V | emotion-theory, frontier-ai | 행동 경향 라벨이 Emo-FilM에만 있어 데이터셋 간 검정은 AI 라벨에 기대 순환적이다 |
| M+W | emotion-theory, llm-semantics | 소리 있는 회상 데이터가 없고, cue가 두 언어로 동시에 제시되어 효과를 분리할 수 없다 |
| J+W | llm-semantics | 억지 연결(RND-02가 무작위 경로에서 W+J를 다른 형태로 채택) |
| Q+V | llm-semantics, frontier-ai, brain-inspired(흡수) | LS-P5, BI-P2에서 이미 다룸. 측정 타당성은 ET-R4-2(LIT-45)가 맡음 |

## 5. Novelty Constraint로 기각하거나 범위를 줄인 조합

* LIT-34 (kept): 방향만 유지: Novelty Constraint상 benchmark 성격(adversarial-reviewer 추가 검토: 재구성, 연구 질문에서 검증 인프라로). 인프라 통과 기준 V2, V3, V5, V7, V11. 첫 산출물은 Omni-fMRI의 무작위 블록 분할 결과를 재현한 뒤 영화 단위 분할로 바꿔 누수 크기를 보이는 것. 피질하 token 의존도는 같은 수의 피질 token masking 같은 matched null이 생기기 전까지 결과로 쓰지 않는다(시험 때만 지우면 입력 분포 이동과 정보 손실이 구분되지 않음). Brain-JEPA 입력 160시점은 Emo-FilM 208 s, Spacetop 74 s라 라벨 시간 해상도와 맞지 않음
* RND-08 (rejected): Novelty Constraint: 'Foundation Model로 정서 관련 반응을 예측'하는 수준. Jang & Kragel 2025가 AI 모델로 amygdala 기능을 이미 분석했고, 해석 단계는 RND-03(LIT-31)과 중복
* RND-24 (kept): 구조와 데이터가 정확히 같은 공개 checkpoint 조합이 없을 수 있다(확인 필요)
* RND-29 (rejected): Novelty Constraint(모델 예측 비교 수준)이고 RND-08, RND-09와 중복
* STR-A2 (rejected): Novelty Constraint: '새로운 모델로 emotion classification accuracy를 높인다'에 해당. 과학적 질문 없음
* STR-B2 (rejected): 재구성 품질 개선은 Novelty Constraint 대상이고, 생성기 prior가 정서를 중립화하거나 주입하는 confound(VD-P4, LIT-29)가 해석을 막는다
