# Deliverable F: Agent Discussion Record

* 작성: Coordinator (Stage 3)
* 기준일: 2026-11-12
* 참여:
  * 연구 에이전트 10개: emotion-theory, vision-decoding, encoding-foundation, multimodal-dynamics, frontier-ai, geometry-info, systems-neuro, generative-counterfactual, llm-semantics, brain-inspired
  * adversarial-reviewer
  * 모두 실제 독립 에이전트로 실행했다. 실행 ID는 `outputs/agent_registry.md`에 있다.
  * dataset-auditor는 Stage 3에 참여하지 않았다.
* 근거 파일:
  * 각 에이전트의 `outputs/agents/<이름>/round2.md`(제안과 3절 응답), `round3_reviews.md`, `round4.md`
  * `outputs/agents/adversarial-reviewer/round2.md`, `round3_top10_review.md`
  * `outputs/discussion/` 아래 색인, 배정, 집계, 요약
* 이 문서는 요약이다. 인용 ID, 검색 경로, 본문 확인 여부는 위 원 파일에 있다. 에이전트 사이의 실제 의견 충돌은 지우지 않고 6절에 모았다.

---

## 0. 한눈에 보기

| 단계 | 규모 | 결과 |
|---|---|---|
| Round 2 제안 | 10개 에이전트, 제안 76개 | `outputs/discussion/proposals_index.md` |
| Round 2 응답 | 96건(받은 제안 + 참조 제안) | 수용 51, 수정 45, 반박 0 |
| Round 3 검토 | 제안 15개 x 서로 다른 분야 검토자 2명 = 30건 | 기각 0. 모두 "수정 후 진행" 또는 "조건부 지지". 15개 모두 선행 판정 partially 이상 |
| adversarial-reviewer 상위 10개 독립 검토 | 10개 + 선정 정정으로 추가한 2개(ET-P4, EF-P4) | 전체 기각 0. 재구성 4(EF-P3, GI-P5, BI-P1, EF-P4), 수정 8. 주장 4개 기각 또는 정정 |
| Round 4 | 관점이 먼 에이전트 5개, 제안 20개 | 미논의 Axis 쌍에서 출발. 기각한 쌍 10종 |
| P5 조합(Coordinator) | 조합 96개 | Broad Directions 74, Distinct RQ 60, 군집 10 |

---

## 1. 진행 방식

1. **Round 2 (P2).**
   * 10개 연구 에이전트가 P2의 Coordinator 질문 8개에 답하며 다른 에이전트에게 제안을 보냈다.
   * Coordinator는 제안을 색인으로 만들고(`build_proposals_index.py`), 받는 에이전트마다 자기에게 온 제안 목록을 전달했다.
   * 받는 에이전트는 각자 round2.md 3절에 수용, 수정, 반박으로 응답했다.
2. **Round 3 (P3).**
   * Coordinator가 15개 제안을 골랐다(선정 이유는 `round3_assignment.md`).
   * 각 제안에 서로 다른 분야의 검토자 2명을 시드 20261114로 배정했다.
   * 검토자는 보낸 에이전트, 받는 에이전트, 병합 설계의 공동 제안자가 아니다.
   * 첫 배정에서 공동 제안자가 검토자로 들어간 오류가 있어 고쳐 다시 배정했다.
3. **adversarial-reviewer 상위 10개.**
   * Round 2 집계 점수로 상위 10개를 골라 새 adversarial-reviewer 실행에 맡겼다.
   * 선정 점수에 오류가 있었다(7.2절).
4. **Round 4 (P4).**
   * Coordinator가 Round 1~3에서 논의된 Axis 쌍과 3개 조합을 정리했다(`outputs/combinations/discussed_pairs.md`). 미논의 이종 쌍은 23개였다.
   * frontier-ai, brain-inspired, geometry-info, llm-semantics, emotion-theory가 미논의 쌍에서만 출발해 제안했다.
5. **P5 조합.**
   * Coordinator가 세 경로(문헌, 무작위, 전략)로 조합을 만들고 판정했다(`outputs/combinations/build_matrix.py`).

---

## 2. Round 2: 서로 제안한 주요 내용

76개 제안은 대부분 "너희 쪽 X를 우리 쪽 Y로 검증하거나 확장"하는 병합안이었다. 여러 에이전트가 같은 설계로 수렴한 주제는 다음과 같다.

| 주제 | 제안 | 수렴한 에이전트 | 제안의 핵심 |
|---|---|---|---|
| Horikawa 범주 결론 vs Westlin 재현 실패 | GI-P1, ET-P1, ET-P4, SN-P7, VD-P2 | geometry-info, emotion-theory, systems-neuro, adversarial-reviewer, vision-decoding | Mind captioning을 두 번째 코호트로 써서 같은 자극 11명의 공유 스펙트럼, multiverse 격자로 불일치를 분해 |
| 개인 뇌 잔차 vs 본인 보고 편차 | GI-P5, ET-P2, EF-P3, LS-P2, GC-P9 | 5~6개 에이전트 | Spacetop alignvideo에서 "자극 기대 반응"을 여러 기준선(TRIBE, peer 평균, MLLM)으로 정의하고 잔차를 본인 평정 편차와 정렬 |
| 정서 대 의미 내용 분리 | LS-P1, VD-P3, GC-P2, GC-P3, FA-P2 | llm-semantics, vision-decoding, generative-counterfactual, frontier-ai | Mind captioning 정서 배제 캡션으로 기술 잔차(통계 통제), 의미 고정 편집(설계 통제), 삼각 검증 |
| in-silico 충실도 관문 | EF-P1, GC-P1, VD-P1, GI-P4, FA-P1 | encoding-foundation, generative-counterfactual, vision-decoding, geometry-info, frontier-ai | Mind captioning 반복 ceiling으로 TRIBE v2의 정서 충실도 지도를 만들어 다른 in-silico 결과의 관문으로 |
| 정서 지도의 방향성과 전이 | BI-P1, GI-P2 | brain-inspired, geometry-info | successor representation, 반대칭 흐름과 비가역성 |
| 이월과 washout | MD-P1, GI-P3, SN-P2 | multimodal-dynamics, geometry-info, systems-neuro | 클립 사이 이월과 영화 후 이완을 HRF와 구분 |
| 생리와 limbic 맹점 | SN-P1, BI-P4, LS-P7, SN-P6 | systems-neuro, brain-inspired, llm-semantics | Emo-FilM 생리로 encoder의 limbic 실패를 분해 |
| world model 놀람 | FA-P3, EF-P5, MD-P5, BI-P5 | frontier-ai, encoding-foundation, multimodal-dynamics, brain-inspired | V-JEPA 2 예측오차, 불확실성, 학습 진전을 appraisal과 뇌 반응에 연결 |
| 회상 정서 재활성 | ET-P6, VD-P6, EF-P2, BI-P6, SN-P5 | emotion-theory, vision-decoding, encoding-foundation, brain-inspired, systems-neuro | Mind captioning 회상과 vividness |
| 행동 경향(Axis V) | BI-P2, FA-P4, GC-P8 | brain-inspired, frontier-ai, generative-counterfactual | 정서 범주 대 행동 경향 대 자극 affordance 경쟁 |
| 관점과 라벨 출처(Axis U) | ET-P3, ET-P7, LS-P4, LS-P5, FA-P5, FA-P6 | emotion-theory, llm-semantics, frontier-ai | portrayed / perceived / felt, MLLM 평정자 대체 가능성, 모델 내부 표상 대 출력 |
| 피질하 경로 | SN-P3, VD-P5, BI-P3, GC-P5 | systems-neuro, vision-decoding, brain-inspired, generative-counterfactual | signal-feasibility 관문과 경로가 싣는 표상 |

**Round 2에서 새로 확인된 데이터 사실**은 `outputs/discussion/round3_summary.md` 1절에 있다. 요지는 다음과 같다.

* Mind captioning과 Horikawa 2020의 제시 순서는 독립이다.
* Mind captioning 테스트 클립은 최대 11회 노출되었고, 테스트 run 안에서 의사 무작위 순서였다.
* Mind captioning 전처리에서는 전역 신호 12개를 회귀했다.
* Mind captioning 참가자는 일본어 화자다.
* 회상 vividness는 3~4점에 몰려 있다.

---

## 3. 비판과 수정된 주장

### 3.1 Round 3 검토자들의 비판 (15개 제안)

세부 내용은 `outputs/discussion/round3_summary.md` 3~4절에 있다. 반복된 비판 다섯 가지는 다음과 같다.

1. **"정서" 신호가 지각, 의미, 시선, 각성, 몸 신호일 수 있다.** 거의 모든 검토에서 나왔다. 대응: 비정서 편집 대조, 시각 이중 통제, fMRI 기반 시선 회귀, 생리 분해.
2. **잔차 설계의 맞교환.** 공변량 측정 오차는 정서를 부풀리고, 과통제는 정서를 지운다. LS-P1 검토에서 frontier-ai와 geometry-info가 지적했다. 대응: 캡션 split-half 신뢰도 보정과 역방향 분할을 함께 보고한다.
3. **시간 지연의 가짜 효과.** 평정자 반응 지연과 HRF가 방향성이나 지속성을 만들 수 있다. BI-P1 검토에서 multimodal-dynamics와 frontier-ai, FA-P3 검토에서 emotion-theory가 지적했다.
4. **관문의 순서.** EF-P1(in-silico 충실도), SN-P3(피질하 신호), GI-P5(잔차 신뢰도)를 각 묶음의 선행 단계로 둔다.
5. **새로움 과대 판정.** 원 제안이 놓친 가장 가까운 선행이 15개 모두에서 나왔다.
   * ET-P6 → Saarimäki 2016.
   * EF-P7 → Lettieri 2024.
   * GI-P5 → Chen 2020, Chang 2021, Finn 2020.
   * FA-P3 → Tambini 2017.
   * GC-P2 → Cao 2024.

### 3.2 adversarial-reviewer 상위 10개 검토의 비판

* 파일: `outputs/agents/adversarial-reviewer/round3_top10_review.md`
* Round 3 검토자들도 놓친 오류를 원문 대조, 대수, 시뮬레이션으로 찾았다.

| 원래 주장 | 비판 | 수정된 주장 |
|---|---|---|
| 개인 뇌 잔차 대 본인 보고: 기준선(TRIBE, peer 평균, MLLM)의 차이 자체가 결과다(GI-P5). (b) peer 평균 - (a) TRIBE = 공유되지만 자극으로 계산되지 않는 성분(EF-P3) | 사람마다 같은 기준선은 영상 안에서 상수라 사람 수준에서 동치다. TRIBE(뇌)와 MLLM(보고)을 짝지으면 실제 연결이 0이어도 r 약 +0.36이 나온다(시뮬레이션 200회). 여러 사람이 공유하는 반응은 정의상 자극에 묶인 반응이다 | 사람과 영상 양방향 중심화 위계 모형으로 만든 단일 연구 A*(RQ-21). 0단계: 결측-상태 관계와 검정력 시뮬레이션. 기준선 간극은 영상 수준(48점) encoder/주석자 적합도 진단으로 분리 |
| 반대칭 흐름 A = (T - T')/2(GI-P2). SR(T) 대 SR(T')가 방향성 null(BI-P1) | π가 균등하지 않으면 A는 순 흐름이 아니다. T'는 시간 역전 사슬이 아니다(T̃ = D_π⁻¹ T' D_π). 대칭 RDM은 방향을 점유율과 섞인 2차 구조로만 본다 | 결합 전이 빈도로 순 흐름과 엔트로피 생산을 정의(0단계). 주 검정은 시간 지연 전향/후향 예측과 내용 상태 경쟁 모형(RQ-24) |
| Axis V의 동기: Horikawa 2020이 결과를 "(or affordances)"로 표현(BI-P2, Round 3 검토자 2명 반복, axis_encyclopedia V 행) | 원문의 affordance는 "장면이 특정 정서를 일으킬 것이라는 추론"(정서 affordance)이다. 행동 affordance가 아니다 | 동기를 Frijda, component process model, Thornton & Tamir 2024로 다시 세운다. Horikawa 문장은 Axis U 질문의 근거다. axis_encyclopedia V 행에 정정 주석을 달았다 |
| 의미 고정 편집 + encoder 예측이 새 설계 팔(GC-P2) | 근거로 든 arXiv:2610.13558이 이미 TRIBE v2로 편집 400쌍을 분석했다. voxel 선택과 encoder 학습이 같은 데이터라 순환이다 | Zhan 2026을 선행으로 명시. voxel 정의(Mind captioning)와 encoder 학습(Horikawa)을 코호트로 나누고, 편집기는 평가 encoder와 독립(RQ-09) |
| 기술 잔차 설계(LS-P1) | Abdel-Ghaffar 2024(의미-정서 공동 tuning) 선행 누락. 34차원 평정 대 고차원 embedding의 band 비대칭 | 차원 맞춤 band, 원 결과 재현(V11), 원본 영상 단위 누수 통제(RQ-08) |
| 일본어 화자 뇌에서 일본어 범주가 더 IB 효율적(GI-P6, LS-P6. 상위 10개 밖) | 영어 화자 뇌 코호트가 없어 언어 일치와 명명 절차, 범주 수, 평정자 차이를 구분할 수 없다 | 언어 특이 가설은 기각(LIT-54). 언어 무관 IB 효율과 볼록성만 탐색적으로(RQ-02) |
| Mind captioning 자극 선택 후 검증(EF-P6) | 자극 보류 없이는 모델 검증이 아니다(adversarial-reviewer Round 2 응답) | D6a(클립 보류 모델 검증)와 D6b(코호트 간 재현)로 분리(RQ-10) |

### 3.3 Round 2 응답 안에서 일어난 수정 (반박으로 분류되지 않은 반대)

응답 범주가 수용, 수정, 반박 셋뿐이라, 핵심 전제를 거부한 응답도 "수정"으로 기록되었다. 예는 다음과 같다.

* **encoding-foundation → ET-P2 (c):** personal relevance를 HOTEC self 성분 검정으로 해석하는 데 "반대한다"고 했다. 이유는 단일 사후 문항이라 몰입이나 주의와 구분되지 않는다는 것이다.
* **geometry-info → MD-P1:** 두 시간척도를 하나의 τ로 적합하면 모형이 잘못 지정된다고 했다. 다중 시간척도 모형으로 바꿨다.
* **frontier-ai → VD-P8:** CLIP image latent를 적응 목표로 쓰면 "정서와 무관한 정렬"이 성립하지 않는다고 했다. 저수준 목표와 무작위 투영 목표를 추가했다.
* **adversarial-reviewer → GC-P3:** "실패 방식이 다르다"는 삼각 검증의 전제를 부분 반박했다. 이유는 같은 관찰 데이터와 겹치는 feature 공간이다.
* **adversarial-reviewer → EF-P6:** "선택이 검증보다 먼저라 순환을 피한다"는 전제를 부분 반박했다. 이유는 분석자 노출이다.
* **llm-semantics → ET-P6:** cue 텍스트가 정서를 함축한다는 점을 지적했다(본문 재확인).

---

## 4. Round 4: 예상 밖 연결

* 기준: `outputs/combinations/discussed_pairs.md`
* 미논의 이종 쌍 23개: B+K, D+G, D+S, F+V, I+W, J+U, J+V, J+W, K+L, K+P, K+V, L+W, M+V, M+W, N+W, O+V, P+V, P+W, Q+V, R+W, S+V, T+V, T+W

| 에이전트 | 제안 | 출발 쌍 | 가져온 외부 개념 |
|---|---|---|---|
| geometry-info | GI-R4-1 자극 앙상블 2x2와 스펙트럼 지수 | B+K | power-law 스펙트럼 이론(Stringer 2019) |
| | GI-R4-2 OT 매칭의 positivity 지도 | K+P | 계량경제학 OT 인과 매칭 |
| | GI-R4-3 동기 방향의 CCGP | K+V | 추상화 기하(Bernardi 2020) |
| | GI-R4-4 정서 동역학의 휴대성 | D+S | dynamical similarity analysis |
| brain-inspired | BI-R4-1 행동 준비의 null space | K+V | 운동 신경과학의 output-null subspace |
| | BI-R4-2 사운드트랙 groove와 행동 경향 | M+V | 음악 groove 연구 |
| | BI-R4-3 행동 조건 예측기(V-JEPA 2-AC) | J+V | 행동 조건 world model |
| | BI-R4-4 회상의 우선순위 재생 | N+W | RL prioritized replay |
| emotion-theory | ET-R4-1 vividness: 내성 대 기억성 | R+W | LLM self-prediction 대 cross-prediction |
| | ET-R4-2 Axis V의 MTMM 측정 타당성 | Q+V | Campbell & Fiske 1959 |
| | ET-R4-3 라벨 출처를 view로 | J+U | 식별 가능한 multi-view 학습 |
| | ET-R4-4 회상의 생성적 재구성 | L+W, P+W | 기억 구성의 생성 모델 |
| llm-semantics | LS-R4-1 학습 목표가 기계 평정자의 관점을 정하는가 | J+U | 정렬 학습 단계 비교 |
| | LS-R4-2 언어 병목을 통과하는 회상 정서 | R+W | 모델 내부 정서 방향 |
| | LS-R4-3 집단 전달 편향과 개인 회상 | I+W | 문화 진화의 전달 사슬 |
| | LS-R4-4 언어 전이 사전확률 | D+S | mental model 전이 |
| frontier-ai | FA-R4-1 cue로부터의 회상 예측 | I+W, L+W, N+W | 텍스트 조건 비디오 생성 |
| | FA-R4-2 empowerment | J+V, K+V, F+V | 내재 동기 empowerment |
| | FA-R4-3 라벨 출처를 view로 | J+U | 식별 가능한 multi-view 학습 |
| | FA-R4-4 straightening이 깨지는 순간 | B+K, D+S | perceptual straightening |

* **독립 수렴:** Round 4에서 서로 다른 에이전트가 같은 설계에 도달한 경우가 두 번 있었다.
  * ET-R4-3과 FA-R4-3: 라벨 출처를 multi-view의 view로 둔다.
  * ET-R4-4와 FA-R4-1: 회상을 생성적 재구성으로 본다.
  * 무작위 경로의 RND-14도 FA-R4-4(straightening)와 같은 개념에 도달했다.
* **기각한 쌍:** 에이전트들이 질문으로 만들지 않은 쌍은 K+L, P+W, O+V, P+V, T+V, T+W, S+V, M+W, J+W, Q+V다. 공통 사유는 데이터 부재였다. 개인 수준 행동 경향 측정이 없고, 소리 있는 회상 데이터가 없고, 회상과 affordance에 대한 개입이 없다. 사유별 정리는 `outputs/combinations/rejected.md` 4절에 있다.
* **Round 4 선행 판정:** 20개 모두 R0다. 선행 판정은 no 또는 partially다. 대부분 에이전트 한 명의 WebSearch 범위 안에서 내린 판정이라 Stage 4에서 다시 확인해야 한다.

---

## 5. 최종 합의

에이전트들이 Round 2~4와 상위 10개 검토를 거쳐 합의한 내용이다. 반대 의견이 남은 항목은 6절에 있다.

1. **관문 먼저.** 다음 관문은 이를 전제로 하는 질문보다 먼저 수행한다. 목록은 rq_landscape.md 3.1절에 있다.
   * in-silico 충실도(RQ-51)
   * 원 결과 재현(V11)과 신뢰 공유 부분공간(RQ-01 0단계)
   * Axis V 측정 타당성(RQ-39)
   * 피질하 신호 가능성(RQ-49 관문)
   * Spacetop 결측과 검정력(RQ-21 0단계)
   * 순 흐름(RQ-24 0단계)
2. **Mind captioning은 핵심 자원이다.**
   * 같은 자극의 두 번째 코호트다.
   * 반복 노출로 신뢰도를 줄 수 있다.
   * 테스트 run이 의사 무작위 순서다.
   * 정서 배제 인간 캡션이 있다.
   * 5개 데이터셋 중 유일한 시행 단위 내성 보고(vividness)가 있다.
   * 이 판단은 거의 모든 에이전트가 독립적으로 내렸다.
3. **증거 수준을 낮춰 말한다.** 관찰 데이터 분석은 "판정"이 아니라 "어느 해석과 맞는가"로 보고한다. in-silico 결과는 R1이다. 실제 뇌의 정서 특이 반응 주장은 새 실험(R3)이 필요하다.
4. **라벨 출처를 질문마다 명시한다.**
   * 규범, consensus, 본인, AI를 구분한다.
   * AI 라벨은 항목별 대체 가능성 판정(RQ-17) 뒤에 쓴다.
   * 사람 수준 질문에서 AI 기준선은 영상 안에서 상수라 정보가 없다.
5. **시선 교란은 모든 데이터셋에 걸린다.** Horikawa 2020 자유 시청을 원문으로 확인했다. 그래서 fMRI 기반 시선 추정을 공통 nuisance로 둔다.
6. **EmoNet은 Horikawa와 Mind captioning에 쓰지 않는다.** 같은 Cowen & Keltner 프레임으로 학습되어 leakage다. 정서 학습 모델이 필요하면 EmoSet처럼 독립 데이터로 학습한 모델을 쓴다.

---

## 6. 남아 있는 의견 차이

실제 충돌을 지우지 않고 기록한다. Coordinator가 한쪽으로 처리한 경우에도 처리 방식과 반대 입장을 함께 적었다.

| # | 쟁점 | 한쪽 | 다른 쪽 | 현재 처리 |
|---|---|---|---|---|
| D1 | VD-P4(생성 decoding의 정서 감사)는 과학적 질문인가 | vision-decoding: 생성 decoding의 정서 충실도 자체가 질문 | emotion-theory, brain-inspired: 방법 인프라. 과학적 질문은 의미 고정 2AFC 쪽 | 방향만 유지(LIT-29) |
| D2 | 통계 통제와 설계 통제의 삼각 검증이 독립적 증거가 되는가 | generative-counterfactual: 실패 방식이 달라 삼각 검증 | adversarial-reviewer: 같은 관찰 데이터와 겹치는 feature 공간이라 부분적. 일치해도 R1 | RQ-09에 "둘 다 음성", "판정 불가" 칸과 코호트 분리 추가. 결론 수준 R1 |
| D3 | 생리는 nuisance인가 매개인가 | systems-neuro: 전역 자율신경 성분은 분리할 nuisance | vision-decoding: 생리는 평가 경로의 매개일 수 있어 회귀하면 정서를 지움 | RQ-48에서 생리를 자극 예측 성분과 개인 성분으로 나누고, 결합은 휴지 구간에서 추정. 해석 규칙은 미합의 |
| D4 | 이월과 washout을 하나의 이완 모형으로 볼 수 있는가 | multimodal-dynamics: 하나의 이완 모형 | geometry-info: 시간 척도가 달라 2성분 필요 | RQ-26에 2성분 모형 채택. multimodal-dynamics가 동의했는지는 기록 없음 |
| D5 | FA-P3의 지속 대 재호출 | frontier-ai: 세 예측 신호로 함께 다룸 | emotion-theory: 영화에서는 둘이 같은 예측을 내므로 분리해야만 지지 | 분리(RQ-25에서 지속 vs 재호출 제외) |
| D6 | in-silico 충실도 감사의 지위 | encoding-foundation: 모든 in-silico 결과의 관문 | geometry-info: 감사만으로는 benchmark. 백본 대비 차이로 재정의해야 과학적 질문 | 두 입장을 합침(RQ-51: 관문이면서 백본 대비 질문) |
| D7 | Spacetop 개인 잔차 묶음의 우선순위 | 다섯 에이전트: Round 2 점수 1위, 가장 많이 수렴 | adversarial-reviewer: 유효 표본(40~57명)과 기준선 동치성 때문에 GI-P1, LS-P1보다 뒤 | Stage 4 판단. 0단계 결과로 진행 여부 결정 |
| D8 | 묶음 A의 "privileged access" 해석 | emotion-theory(ET-P2): 본인 보고가 관찰자 정보 밖의 본인 뇌 분산을 반영하는지 검정 | adversarial-reviewer: 기준선 구조 때문에 이 해석이 약해짐. encoding-foundation: personal relevance 조절 해석에 반대 | RQ-21을 약한 형태("자극과 평균 관찰자로 설명되지 않는가")로 서술 |
| D9 | Axis V의 근거 | brain-inspired, frontier-ai: Horikawa의 affordance 표현과 Emo-FilM Motivation | adversarial-reviewer: Horikawa 근거는 오독. Motivation 항목은 valence 재표현일 수 있음. emotion-theory(ET-R4-2): 측정 타당성 먼저 | RQ-39(MTMM)를 관문으로. brain-inspired가 정정에 동의했는지는 아직 확인되지 않음 |
| D10 | Acquisition & Signal Physics의 지위(Stage 2부터) | systems-neuro: 독립 Axis. Q 하위로 두면 E 쪽 판단에서 누락됨 | Coordinator: 필수 태그 signal-feasibility로 대응 | 태그 유지. Stage 3 조합에서 피질하 질문(RQ-49)이 관문을 둔 것은 systems-neuro 입장을 일부 반영 |
| D11 | Recognition vs Experience의 처리(Stage 2부터) | emotion-theory: 독립 Axis 불필요, 필수 태그 | adversarial-reviewer, llm-semantics: 독립 Axis | Axis U + 태그 둘 다 채택. 이 처리 자체가 이견 |
| D12 | X(Machine Affect Representations), Y(Metacognition)를 Sub-axis로 둔 사용자 결정 | frontier-ai: X는 조건부로 독립 Axis 필요. emotion-theory: Y는 조건부로 독립 Axis 필요 | 사용자 결정(2026-11-12): X는 R, Y는 A의 Sub-axis | 사용자 결정 유지. Stage 3에서 R과 Introspective Access를 쓴 질문은 RQ-15, 21, 41, 43 등 다수 |
| D13 | GI-P6 언어 특이 가설 | geometry-info, llm-semantics: 일본어 화자 코호트로 검정 가능 | adversarial-reviewer: 영어 화자 대조 코호트 없이 구분 불가 | 언어 특이 판본 기각(LIT-54). 제안자들의 재반론은 기록 없음 |
| D14 | Round 2 합의는 제안의 질 때문인가 | 수용 측 근거: 많은 "수정"이 실질적이었다(events.tsv 확인, TRIBE 입력 구조, T̃ 정정) | adversarial-reviewer: 검증 가능한 오류 4건이 수용을 통과했으므로 동의 편향과 양식 효과가 더 크다 | 7절에 기록. Stage 4에 반증 시도 항목 추가를 권고 |

---

## 7. 과정에 대한 비판적 기록

### 7.1 반박 0건

* Round 2 응답 96건 중 반박은 0건이었다. Round 3 검토 30건 중 기각도 0건이었다.
* adversarial-reviewer의 판단(round3_top10_review.md 9절)은 "제안의 질보다는 동의 편향과 양식 효과"다. 근거는 다음 셋이다.
  * 검증 가능한 오류 4건이 수용을 통과했다.
  * P2 양식은 받는 쪽 chain을 품은 병합안을 만든다.
  * 응답 범주에 "부분 반박"이 없어 핵심 전제 거부가 "수정"으로 기록되었다(3.3절).
* Coordinator도 이 판단에 동의한다. 다만 반대 근거도 있다. Round 3 검토에서 실질적인 수정과 새 선행이 많이 나왔다.

### 7.2 Coordinator의 상위 10개 선정 오류

* **오류:** `tally_responses.py`의 첫 실행이 Round 3 검토 파일의 언급까지 셌다. 그 결과 Round 3에 배정된 제안이 평균 약 1.1점을 더 받았다. 지시문 기준("Round 2에서 가장 많이 수용되거나 언급된")과 어긋난다.
* **정정:** Round 2 파일만 세도록 고쳤다.
* **영향:**
  * BI-P2와 GC-P2는 상위 10개 밖이었다.
  * ET-P4와 EF-P4가 빠졌다.
  * 빠진 두 제안은 같은 adversarial-reviewer에게 추가 검토를 맡겼다(`round3_top10_addendum.md`).
    * ET-P4는 수정으로 판정되었다. 이산 라벨 AMI 상한, Horikawa에서 세션과 클립 묶음이 겹치는 문제를 Mind captioning으로 가르는 판별, V11이 빠졌다는 이유다. LIT-01에 반영했다.
    * EF-P4는 연구 질문에서 검증 인프라로 재구성되었다. 피질하 token 의존도는 matched null 없이는 해석할 수 없다는 이유다. LIT-34(방향만 유지)에 반영했다.
  * 같은 설계의 변형 넷(묶음 A)이 상위권을 차지한 것도 점수 구조 때문이다. 같은 설계의 변형은 묶어 한 번만 세자는 권고를 Stage 4에 넘긴다.

### 7.3 오독의 전파

* BI-P2의 Horikawa affordance 오독은 다음 경로로 퍼졌다.
  * Round 2 수용(frontier-ai)
  * Round 3 검토자 2명
  * Stage 2 axis_encyclopedia V 행의 근거
* 원문 대조로 처음 잡은 것은 상위 10개 검토였다.
* 교훈: 근거 문장을 인용할 때 본문 위치를 확인하는 단계가 Round 3 P3 항목에 있었지만, 실제로는 지켜지지 않았다.

### 7.4 시점이 지난 의견

* adversarial-reviewer의 Round 2 응답(EF-P6 4번)은 "Mind captioning은 보유 4개 데이터셋 밖이라 사용자 결정이 선행해야 한다"고 적었다.
* 사용자가 같은 날 Mind captioning 사용을 승인했으므로(STAGE_STATUS 16번) 이 조건은 해소되었다.
* 같은 응답의 "자극 보류 없이는 모델 검증이 아니다" 지적은 여전히 유효해 RQ-10에 반영했다.

### 7.5 검토자의 자기 정정

* adversarial-reviewer는 자기 Round 2 요건표 V1의 "SR(T') 같은 전치 모델을 matched null로" 문구가 틀렸다고 스스로 정정했다.
* V1 v3안은 결합 빈도 순 흐름과 시간 역전 대리 null, T̃ 대조, 내용 상태 경쟁 모형을 요구한다.
* V3도 보강을 제안했다. 사람 수준 주장에는 사람과 자극 양방향 중심화를 주 분석으로 둔다.
* 이 두 정정은 RQ-24와 RQ-21에 반영했다. adversarial-reviewer의 round2.md 원문은 고치지 않았다.

### 7.6 Stage 4에 넘기는 권고

1. 응답과 평가 범주에 "부분 반박(핵심 전제 거부)"을 추가한다.
2. 질문마다 "핵심 전제 한 줄을 반증 시도했는가"를 적는다.
3. 근거 문장을 인용할 때 본문 위치와 원문 문장을 함께 확인한다.
4. 선정 점수에서는 같은 설계의 변형을 한 번만 센다.

---

## 8. 미확인 사항

* **D4, D9, D13의 반대 측 재반론:** 이번 Stage에서 받지 않았다.
* **Round 4 제안 20개의 선행 판정:** 대부분 에이전트 한 명의 WebSearch 범위다.
* **데이터 사실 중 미확인 항목:** Mind captioning 캡션 파일 보유, C&K 원 클립 오디오, 두 코호트 피험자 중복, Horikawa 2020 참가자 모국어. 상세는 rq_landscape.md 7절에 있다.
