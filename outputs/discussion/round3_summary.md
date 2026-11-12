# Round 3 요약: Constructive Disagreement

* 작성: Coordinator (Stage 3)
* 기준일: 2026-11-12
* 입력: 10개 연구 에이전트의 `outputs/agents/<이름>/round3_reviews.md`(제안 15개 x 검토자 2명), 받는 에이전트의 응답(각 `round2.md` 3절), `outputs/discussion/round3_assignment.md`, `outputs/discussion/responses_tally.csv`
* 이 문서는 각 검토 파일의 "판정 7항목"과 "수정안"을 요약한다. 판정 근거, 검색 경로와 날짜, 인용 ID는 각 검토 파일에 있다.
* adversarial-reviewer의 상위 10개 독립 검토는 6절에 덧붙인다.

---

## 0. 한눈에 보기

* **15개 제안 모두 "이미 연구된 것은 아닌가"에서 partially 이상으로 판정되었다.** 완전히 새롭다고 판정된 제안은 없다. 검토자들은 원 제안이 놓친 가장 가까운 선행연구를 여럿 새로 찾았다(2절).
* **기각된 제안은 없다.** 30개 검토 모두 "수정 후 진행" 또는 "조건부 지지"다. 다만 FA-P3은 "둘로 나눈 뒤에만 지지"(emotion-theory), VD-P4는 "과학적 질문이 아니라 방법 인프라"(emotion-theory, brain-inspired), EF-P1은 "감사만으로는 benchmark에 가깝다"(geometry-info)처럼 범위를 크게 좁힌 판정이 있다.
* **Round 2 응답 96건(받은 제안 + 참조 제안) 중 반박 0건, 수용 51, 수정 45.** 받는 쪽 응답에는 반박이 없었지만 제3자 검토에서는 실질적인 비판이 많이 나왔다. 합의 쏠림 여부는 adversarial-reviewer가 따로 판단한다(6절).
* **가장 자주 나온 비판:** 제안이 측정하려는 "정서" 신호가 실제로는 지각, 의미, 시선, 각성, 몸 신호일 수 있다는 점(거의 모든 검토).

## 1. 데이터에 관해 Round 2~3에서 새로 확인된 사실

| 사실 | 확인한 에이전트와 경로 | 영향 |
|---|---|---|
| Mind captioning과 Horikawa 2020의 제시 순서는 사실상 독립(Spearman -0.03) | vision-decoding, 공개 미러 events.tsv 직접 계산 | 두 코호트 교차 분석(GI-P1)이 순서 효과를 통제할 수 있다. multimodal-dynamics가 제기한 조건이 해소됨 |
| Mind captioning 72개 테스트 클립은 학습 세션 포함 **최대 11회** 노출(제안들이 6회로 셈), 학습 순서의 끝에 몰림 | vision-decoding(events.tsv), encoding-foundation(Methods) | 반복 번호를 실제 노출 수로 모형화해야 함. 반복 억제와 친숙도 효과 |
| Mind captioning 테스트 세트는 run 안에서 의사 무작위 순서 | multimodal-dynamics, generative-counterfactual(Methods) | 직전 클립 효과를 데이터셋 안의 실제 조작으로 볼 수 있음(evidence-level R3-internal 후보) |
| Mind captioning 전처리는 전역 신호 12개(CSF, WM, GM 평균과 미분, 제곱)를 회귀 | systems-neuro(Methods) | Horikawa 2020 공개 전처리와 파이프라인이 다를 수 있음. 코호트 비교에서 분리해야 함 |
| Mind captioning 획득: 3T, TR 1 s, TE 30 ms, 2 mm, MB 6, 생리 기록 언급 없음 | systems-neuro(Methods) | Horikawa 2020(TR 2 s, TE 43 ms)과 같은 자극, 다른 획득 조건 |
| Mind captioning 피험자 6명 모두 일본어 모국어 화자, 라이선스 CC0 | geometry-info(Methods), vision-decoding(미러) | 문화, 언어 질문(GI-P6, LS Chain 6)의 전제 |
| 회상 vividness는 3~4점에 몰림. 일부 피험자는 강약 이진 분할 불가 | vision-decoding(events.tsv) | ET-P6의 type-2 설계를 서수 혼합모형으로 바꾼 이유 |
| 회상 cue는 정서 배제 캡션 중 하나(영어, 일본어) | llm-semantics(본문) | 회상 해독 결과에서 cue가 함축하는 정서를 통제해야 함 |

## 2. 검토자들이 새로 찾은 가장 가까운 선행연구

원 제안의 "선행 없음" 판단을 낮춘 연구들이다(세부와 ID는 각 검토 파일).

| 제안 | 새로 찾은 선행 | 찾은 검토자 |
|---|---|---|
| ET-P6 (회상 정서 재활성) | Saarimäki 2016(지각에서 심상으로의 정서 decoding 일반화, doi:10.1093/cercor/bhv086), Kim & Kim 2025, Curko 2026 | llm-semantics, frontier-ai |
| BI-P1 (정서 지도 방향성) | Li 2024(휴지기 뇌 상태에 SR 적용), Ekman 2023(시각 순서에서 방향성 SR) | multimodal-dynamics, frontier-ai |
| MD-P1 (이월과 washout 이완) | Pichon 2015 | encoding-foundation |
| GC-P2 (통계 통제 vs 설계 통제) | Cao 2024(Kuleshov 효과 fMRI) | emotion-theory |
| GI-P5 (개인 잔차 vs 본인 보고) | Chen 2020(형질 선호와 뇌 유사성), Chang 2021(doi:10.1126/sciadv.abf7129), Finn 2020 | systems-neuro, brain-inspired |
| FA-P3 (예측 신호와 지속 vs 재호출) | Tambini 2017(doi:10.1038/nn.4468) | llm-semantics |
| EF-P7 (in-silico 감각 박탈) | Lettieri 2024(doi:10.1126/sciadv.adk6840, 같은 영화의 판본 비교) | llm-semantics, brain-inspired |
| LS-P1 (기술 잔차) | Horikawa 2020의 73개 의미 항목 비교, Du 2025(arXiv:2509.24298) | geometry-info |
| EF-P1 (surrogate 충실도) | NeurIPS 2026 "Evaluating TRIBE v2 Beyond Its Original Benchmarks"(검색 색인으로만 확인) | systems-neuro, geometry-info |
| BI-P2 (Axis V 경쟁) | Morgenroth 2026(doi:10.1037/emo0001619, 평정 수준에서만) | encoding-foundation |
| SN-P3 (피질하 경로) | Kragel 2021(doi:10.1016/j.neuron.2021.06.001) 전문 재확인: 3T에서 표적과 교차 연결 차이가 0.055로 작음 | geometry-info |

## 3. 제안별 검토 요약과 수정된 제안

| 제안 | 검토자 | 공통 비판 | 수정된 제안(핵심) |
|---|---|---|---|
| **GI-P1** 두 코호트 교차 공유 스펙트럼으로 Horikawa vs Westlin 판정 | vision-decoding, multimodal-dynamics | 자유 시청이라 개인별 시선 패턴이 "재현되는 개인 고유 분산"으로 잡힐 수 있다. 노출 횟수 오산(최대 11회). 범주 판정에는 혼합 모형과 연속 잠재 모형 비교가 필요. EmoMind가 두 코호트를 이미 결합했으나 공유 스펙트럼 비교는 없음 | 시선 추정(fMRI 기반) 회귀, 노출 수별 층화, 이월과 시간 feature 통제, 혼합 대 연속 잠재 모형 비교. 받는 쪽 emotion-theory는 SN-P7(통합 multiverse)과 한 프로그램으로 묶음 |
| **GI-P5** Spacetop 개인 잔차 대 본인 보고 편차의 기준선 multiverse | systems-neuro, brain-inspired | 잔차가 정서가 아니라 몸 반응성, 시선, 몰입, 평정 스타일, 각성일 수 있다. 기준선 5개는 많다 | 사전 등록 관문 3개(잔차 신뢰도 먼저), 기준선 3개, 계층 모형, 영상 단위 IS-RSA를 1차 분석으로, engaged 평정과 시선을 공변량으로, 전역 신호 제거판 병행 |
| **LS-P1** 정서 배제 캡션으로 설명하고 남는 정서 분산 | frontier-ai, geometry-info | 캡션 측정 오차가 잔차를 부풀리고, 반대로 과통제가 정서 신호를 지울 수 있다. AI 재작성 캡션 단계는 결론을 흐린다 | 캡션 20개로 측정 오차 보정, 교차 적합 잔차화, 역방향 분할, 잔차의 rank별 공유 스펙트럼, controversial 쌍 검정, 다중 text encoder. AI 재작성 단계는 주 결론에서 분리 |
| **GC-P2** 통계 통제와 설계 통제를 같은 voxel에서 맞대기 | systems-neuro, emotion-theory | "정서 대 의미"가 "정서 대 지각"으로 미끄러진다. 편집이 저수준 통계를 바꾸고 통계 쪽이 전역 각성을 잡을 수 있다. 두 방법은 같은 관찰 데이터와 겹치는 feature 공간을 써서 실패 방식이 독립이 아니다(adversarial-reviewer 응답) | Mind captioning 반복으로 만든 신뢰도 mask, 영역 수준 먼저, 저수준 통계를 맞춘 편집과 비정서 지각 편집 대조, 자연 클립 controversial selection을 세 번째 축으로, 의미 지표 다중화. 결론 수준은 둘이 일치해도 R1 |
| **EF-P1** surrogate 충실도 감사를 in-silico 결과의 관문으로 | systems-neuro, geometry-info | trust map이 관찰 잡음과 몸 없는 surrogate의 구조적 결핍을 섞는다. 감사만으로는 benchmark에 가깝다 | 관찰 신뢰도로 정규화, trust = 뇌 투영 충실도 - V-JEPA 2 백본 충실도, leave-one-out 인간 기준선, rank별 충실도, 전역 신호 유무 두 판, 사전 결정 규칙. 다른 in-silico 제안보다 먼저 수행 |
| **BI-P1** 정서 지도의 방향성(successor geometry) | multimodal-dynamics, frontier-ai | 전이 행렬의 단순 전치 비교는 "어떤 정서가 자주 나오는가"를 방향으로 오인한다. 방향성이 서사 전이, HRF 지연, 평정자 반응 지연에서 생길 수 있다 | 시간 역전 마르코프 사슬로 비교, 지연 sweep, 장면 내용 상태 SR 경쟁 모형, 시각피질 음성 대조, "뇌 패턴이 과거보다 미래 정서를 더 잘 예측하는가" 검정. GI-P2(반대칭 흐름, 비가역성)를 0단계로 통합 |
| **BI-P2** Axis V 경쟁 검정(정서 범주 vs 행동 경향 vs affordance) | encoding-foundation, generative-counterfactual | 범주 평정과 행동 경향 평정이 공선적이라 "분리 불가"로 끝날 위험. latent action band가 화면 운동을 잴 위험 | 접근/회피가 갈리는 구간 선택, 공선성 판정 규칙 사전 등록, 고유와 공유 분산 모두 보고, TRIBE v2 예측 먼저 통제, 운동 nuisance, 정서 고정 affordance 편집 단계(R1+R2) |
| **SN-P1** 생리 반영 noise ceiling과 전역 자율신경 성분으로 limbic 맹점 분해 | multimodal-dynamics, vision-decoding | 생리는 교란이 아니라 매개일 수 있어 회귀하면 평가 경로까지 지운다. 저수준 시청각 자극이 생리와 BOLD를 함께 구동한다 | 생리를 자극 예측 가능 성분과 개인 성분으로 분리, 생리-BOLD 결합은 휴지 구간에서 추정, 감각 강도를 네 번째 성분으로, 4원 분할과 사전 지정 추정량, Mind captioning 반복 ceiling 보정 |
| **FA-P3** 세 예측 신호와 지속 상태 vs 재호출 | emotion-theory, llm-semantics | 영화에서는 지속과 재호출이 같은 예측을 낸다. 상황 모델의 지속과 비슷한 내용의 재등장이 정서 지속으로 오인된다 | 질문을 둘로 분리, Horikawa 고정 순서에서 비슷한 클립이 긴 간격으로 재등장하는 구조를 검정에 사용, 가짜 재호출 귀무 회귀자, MLLM 상황 그래프 지속 경쟁자, 인간 consensus와 생리 채널에서도 재현 요구, Emo-FilM은 50 s high-pass 없이 재전처리 |
| **MD-P1** 클립 사이 이월과 washout 이완을 한 이완 모형으로 | encoding-foundation, generative-counterfactual | 두 시간 척도를 τ 하나로 맞추면 모형이 잘못 지정된다(받는 쪽 geometry-info). 자극으로 설명되는 이월을 먼저 빼야 한다 | HRF 성분과 느린 성분의 2성분 모형, TRIBE v2 "자극 설명 이월" 기준선을 1차 통제로, τ 식별 가능성 시뮬레이션, 정서와 시각 부분공간 대조. **Mind captioning 테스트 세트의 무작위 순서를 실제 조작으로 사용(R3-internal)** |
| **EF-P7** in-silico 감각 박탈 vs 관찰된 무음 | llm-semantics, brain-inspired | 같은 영화의 판본 비교는 Lettieri 2024가 이미 했다. Emo-FilM과 Horikawa 대조는 자극이 달라 교란이 크다. 결론은 뇌가 아니라 모델 타당성에 관한 것이고 공개 checkpoint에 피질하가 없다 | 같은 자극(Horikawa, Mind captioning)의 관찰 대 in-silico 비교를 1차로, 정서 기하는 의미를 제거한 뒤 정의, 화면 기술 텍스트 입력 조건 추가, 관찰-관찰 전이 대조 |
| **ET-P6** 회상 vividness와 정서 부분공간 재활성(W, Introspective Access) | llm-semantics, frontier-ai | Saarimäki 2016 등 선행이 빠졌다. vividness는 재시청 후 회고 평정이고 분포가 치우쳤다. type-2 틀은 이 데이터에 맞지 않다 | cue가 함축하는 정서 통제, 순방향 banded ridge와 서수 혼합모형, 회상 시점 의미 해독 통제, 72개 클립 정서 분포 파일럿. 받는 쪽 vision-decoding은 VD-P6과 합침 |
| **FA-P6** 모델 내부 표상 읽기 vs 출력 묻기 | generative-counterfactual, vision-decoding | 두 feature 집합의 점수 비교로 끝날 위험. VLM hidden state에 시각, 의미 내용이 섞인다 | 같은 forward pass에서 읽기와 묻기, 차원과 신뢰도 맞추기, 같은 모델 안 matched-complexity null과 무작위, 비정서 방향 null, 시각 feature 이중 통제, HOT의 1차 대 보고 수준으로 재구성, 회상 일반화 검정 |
| **SN-P3** 피질하 경로 분석의 signal-feasibility 관문 | geometry-info, encoding-foundation | 상구의 안구운동(자유 시청)과 시각 운동 에너지가 빠졌다. Kragel 2021의 효과가 작다 | 관문 데이터를 Mind captioning(반복 신뢰도, TE 30 ms)으로, fMRI 기반 시선 회귀, looming 대조로 상구 확인, 코호트 간 전향 적용, 주 데이터는 Spacetop |
| **VD-P4** 생성기의 정서 중립화 round-trip audit | emotion-theory, brain-inspired | CLIP 거리로 고르는 2AFC는 정서 진단적 시각 정보를 보일 뿐 정서 표상을 보이지 않는다. 텍스트 프롬프트로 정의한 정서 방향은 의미를 검정한다 | 방법 인프라로 범위 축소, 생성 없는 latent probe를 0단계로, 비정서 시각 속성만 다른 대조 쌍, 정서 방향은 인간 규범 평정으로 정의, guidance 강도 곡선, R2 인간 평정으로 평가기 보정, 라벨 대상(portrayed / perceived / felt) 명시 |

## 4. 검토에서 반복된 공통 비판 (질문 생성 단계의 점검 항목으로 사용)

1. **정서 대 비정서 신호:** 지각(저수준 시청각), 의미, 시선, 각성, 몸 신호가 정서로 오인될 위험. 모든 질문에 대응하는 대조(비정서 편집, 시각 이중 통제, 시선 회귀, 생리 분해)를 둔다.
2. **시선:** 다섯 데이터셋 모두 자유 시청이며 Horikawa와 Mind captioning에는 eye tracking이 없다. fMRI 기반 시선 추정 같은 대리 지표가 필요하다.
3. **과통제와 측정 오차의 맞교환:** 잔차 설계는 공변량 측정 오차로 정서를 부풀리거나, 의미와 정서가 인과로 얽힌 경우 과통제로 정서를 지운다. 신뢰도 보정과 역방향 분할을 함께 보고한다.
4. **시간 지연의 가짜 효과:** 평정자 반응 지연, HRF, 반복 시청에 따른 예측 앞당김이 방향성, 지속성, 불일치를 만든다. 지연 sweep과 시간 역전 대조를 둔다.
5. **관문 연구의 순서:** surrogate 충실도(EF-P1), 피질하 신호 관문(SN-P3), 잔차 신뢰도(GI-P5)를 각 묶음의 선행 단계로 둔다.
6. **새로움 과대 판정:** 15개 모두 partially 이상이었다. Stage 4 선행연구 중복 감사에서 다시 확인한다.

## 5. 남은 이견 (지우지 않음)

| 쟁점 | 한쪽 | 다른 쪽 |
|---|---|---|
| VD-P4는 과학적 질문인가 | vision-decoding: 생성 decoding의 정서 충실도 자체가 질문 | emotion-theory, brain-inspired: 방법 인프라이며 과학적 질문은 의미 고정 2AFC 쪽 |
| GC-P2 두 축의 독립성 | generative-counterfactual: 통계 통제와 설계 통제는 실패 방식이 달라 삼각 검증이 된다 | adversarial-reviewer(응답): 같은 관찰 데이터와 겹치는 feature 공간이라 일부 반박, 일치해도 R1 |
| SN-P1에서 생리의 지위 | systems-neuro: 전역 자율신경 성분을 분리하는 nuisance | vision-decoding: 생리는 매개일 수 있어 회귀하면 평가 경로를 지움 |
| MD-P1의 이완 모형 | multimodal-dynamics: 짧은 이월과 washout을 하나의 이완 모형으로 | geometry-info(받는 쪽): 시간 척도가 달라 2성분 모형이 필요 |
| FA-P3의 지속 vs 재호출 | frontier-ai: 세 예측 신호로 한 번에 다룸 | emotion-theory: 영화에서는 둘이 같은 예측을 내므로 분리해야만 지지 |
| EF-P1의 지위 | encoding-foundation: 모든 in-silico 결과의 관문 | geometry-info: 감사만으로는 benchmark에 가깝고, 백본 대비 차이로 재정의해야 과학적 질문이 됨 |

## 6. adversarial-reviewer 상위 10개 독립 검토

* 파일: `outputs/agents/adversarial-reviewer/round3_top10_review.md`
* 검토 대상: EF-P3, ET-P2, GI-P5, LS-P2, LS-P1, GC-P2, GI-P1, GI-P2, BI-P1, BI-P2
* 이 검토는 Round 3 검토자들과 독립적으로, 새 adversarial-reviewer 실행으로 수행했다.

### 6.1 판정

| 제안 | 판정 | 핵심 |
|---|---|---|
| EF-P3, GI-P5 | 재구성 | 사람마다 같은 기준선(TRIBE, LOO peer 평균, MLLM)은 영상 안에서 상수라 사람 수준 질문에서 동치다. TRIBE(뇌)와 MLLM(보고)을 짝지으면 실제 연결이 0이어도 r 약 +0.36이 나온다(시뮬레이션 200회). 사람과 영상 양방향 중심화로 고친 단일 연구 A*로 재구성(RQ-21) |
| ET-P2, LS-P2 | 수정 | 본인 보고의 측정 모형은 채택. "privileged access" 해석과 MLLM 결측 보간은 폐기. 가장 가까운 선행 Woo 2017(SIIPS1), Li 2025가 빠져 있었다 |
| LS-P1 | 수정, 우선순위 높음 | Abdel-Ghaffar 2024 선행 누락, band 차원 비대칭, 원본 영상 단위 누수, 원 결과 재현(V11) 보완 |
| GC-P2 | 수정 | 근거로 든 arXiv:2610.13558(Zhan 2026)이 이미 TRIBE v2로 정서 편집 400쌍을 분석했다(R1 팔의 부분 선행). voxel 선택과 encoder 학습의 순환, encoder 유도 편집의 순환을 막아야 한다 |
| GI-P1 | 수정, 우선순위 높음 | 순서 독립 확인으로 설계가 성립한다. 원 파이프라인 재현(V11), 피험자 쌍 의존성, 자극 구동 시선이 공유 분산을 부풀리는 반대 방향 교란을 보완 |
| GI-P2 | 수정 | A = (T - T')/2는 정상분포가 균등하지 않으면 순 흐름이 아니다. 결합 전이 빈도로 재정의 |
| BI-P1 | 재구성 | T'는 시간 역전 사슬이 아니고(T̃ = D_π⁻¹ T' D_π), 대칭 RDM은 방향을 점유율과 섞인 2차 구조로만 본다. 주 검정을 시간 지연 전향/후향 예측으로 |
| BI-P2 | 수정 | 동기로 든 Horikawa 2020의 "(or affordances)"는 행동 affordance가 아니라 정서 affordance(장면이 특정 정서를 일으킬 것이라는 추론)다. Round 3 검토자 두 명도 이 오독을 반복했다 |

### 6.2 새로 확인한 데이터 사실

* Horikawa 2020 참가자도 자유 시청했다. 원문 Discussion에서 확인했다. 따라서 시선 교란은 두 코호트 모두에 걸린다.
* Spacetop alignvideo 결측은 시행/런 단위로 통째로 빠지는 구조다. 값에 따라 선택적으로 빠진다는 증거는 없다.
* Spacetop 유효 표본은 완료율 0.5 이상 57명, 0.8 이상 40명이다.
* 공개 TRIBE v2는 피험자 평균 모델이다.

### 6.3 합의 쏠림 판단

검토자의 결론은 "제안의 질보다는 동의 편향과 양식 효과가 크다"다.

* **수용을 통과한 오류:** Round 2에서 원문 대조나 대수로 확인되는 오류 4건이 수용을 통과했다.
* **양식 효과:** P2 양식은 받는 쪽의 chain을 품은 병합안을 만든다. 받는 쪽은 자기 아이디어가 들어간 안을 평가하게 된다.
* **반박 0의 일부는 분류 관행 때문이다:** "수정" 응답 안에 핵심 전제를 거부한 사례가 약 15곳 있다. 예는 MD-P1의 단일 τ, ET-P2 (c)의 HOTEC 대리다.
* **놓친 반박:** 상위 10개 밖의 GI-P6 언어 특이 가설도 반박되었어야 했다. Coordinator는 이를 LIT-54로 기각하고 언어 무관 판본만 RQ-02로 남겼다.

### 6.4 Coordinator 선정 오류와 정정

* **오류:** 상위 10개 선정 점수에 Round 3 검토 파일의 언급까지 들어갔다. 그 결과 Round 3에 배정된 제안이 평균 약 1.1점을 더 받았다. 지시문 기준은 "Round 2에서"다.
* **정정:**
  * `tally_responses.py`를 Round 2 파일만 세도록 고쳤다. 첫 실행은 `TALLY_INCLUDE_R3=1`로 재현할 수 있다.
  * 다시 계산한 상위 10개는 EF-P3, ET-P2, LS-P2, GI-P5, BI-P1, ET-P4, GI-P1, GI-P2, LS-P1, EF-P4다. 검토자의 계산과 같았다.
* **추가 검토:** 빠졌던 ET-P4와 EF-P4는 같은 adversarial-reviewer에게 추가 검토를 맡겼다(`round3_top10_addendum.md`). 이미 검토한 GC-P2와 BI-P2의 결과는 그대로 유지한다.
  * ET-P4: 수정. 이산 라벨 AMI 상한, 세션과 클립 묶음의 혼동(Mind captioning으로 판별), V11이 빠져 있다.
  * EF-P4: 재구성(연구 질문에서 검증 인프라로). 피질하 token 의존도는 matched null 없이는 해석할 수 없다. 첫 산출물로는 Omni-fMRI 무작위 블록 분할을 재현한 뒤 영화 단위 분할로 누수 크기를 보이는 것이 가장 설득력 있다.
* **검토자의 자기 정정:** 검토자는 자기 Round 2 요건표 V1(SR(T')를 방향성 null로 둔 문구)도 정정했다. V1 v3안은 다음 셋을 요구한다.
  * 결합 빈도 기반 순 흐름과 시간 역전 대리 null.
  * T̃ 기반 대조.
  * 내용 상태 경쟁 모형.

### 6.5 조합 단계 반영

모든 정정은 `outputs/combinations/build_matrix.py`의 해당 조합에 반영했다.

| 조합 | 반영 내용 |
|---|---|
| LIT-01 | 0단계 V11 재현, 쌍 의존성, 시선 band 추가 |
| LIT-02 | A*로 재구성 |
| LIT-03 | Abdel-Ghaffar 2024 선행, 차원 맞춤 band |
| LIT-04 | Zhan 2026 선행, 순환 방지 설계 |
| LIT-06 | 수학 정정 |
| LIT-07 | 동기 정정 |
| LIT-18 | 언어 무관 판본으로 축소 |
| STR-A1 | 전제가 무너져 기각하고 STR-A3로 대체 |
| `axis_encyclopedia.md` V 행 | 정정 주석 추가 |
