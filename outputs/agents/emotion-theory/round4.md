# Round 4 (Unexpected Connections): emotion-theory

* 에이전트: emotion-theory (Axis A, Q, U; 외부 분야 Artificial Consciousness and Metacognition)
* 기준일: 2026-11-12. 절차: `reference/protocols.md` P4
* 읽은 것: `outputs/combinations/discussed_pairs.md`(미논의 2개 조합 23개), `outputs/axis_encyclopedia.md` 3절(갱신 유형표: U, V, W 신규, Model-internal Emotion Representations는 R의 Sub-axis, Introspective Access는 A의 Sub-axis)
* 원칙: 미논의 쌍을 반드시 하나 이상 포함하고, 서로 다른 유형에서 3개 이상 Axis를 쓰며, 그중 하나 이상은 Affective Neuroscience 밖의 개념이나 방법이다. 연결이 성립하지 않는 쌍은 기각하고 이유를 적는다. 선행 수행은 모두 2026-11-12에 직접 검색했다.
* 새로 확인한 문헌 4편(doi:10.1038/s41562-023-01799-z, doi:10.1038/s41598-018-26467-5, arXiv:2009.02568, doi:10.1037/h0046016)은 Crossref, arXiv API, PubMed로 확인해 `literature.jsonl`에 추가했다. Campbell & Fiske(1959)는 서지만 확인했고 본문은 읽지 않았다.

## 제안 요약

| ID | 미논의 쌍 | 조합 Axis (유형) | 밖에서 온 개념 | 핵심 질문 | 데이터셋 | 선행 |
|---|---|---|---|---|---|---|
| ET-R4-1 | **R+W** | W (Construct), A의 Introspective Access (Construct), R (Structure), O (Neural), Q (Inference) | LLM introspection 검정(self- vs cross-prediction), 컴퓨터 비전의 기억성(memorability) | 회상 vividness는 본인 재활성을 보고하는가, 클립 고유 기억성을 보고하는가 | Mind captioning (+ Horikawa) | partially |
| ET-R4-2 | **Q+V** | V (Construct), Q (Inference), I (Model & Method), F (Neural) | 심리측정 MTMM, 로봇 학습의 latent action model | 행동 경향은 방법을 가로질러 정서 범주, valence와 구분되는 구성 개념인가 | Emo-FilM (+ Horikawa 일부) | no |
| ET-R4-3 | **J+U** | U (Inference), J (Model & Method), A (Construct), F (Neural) | 자기지도 학습의 view 기반 식별성 이론 | 라벨 출처를 view로 보면 출처 불변 정서 성분과 출처 특이 성분이 뇌의 다른 곳에 대응하는가 | Emo-FilM, Spacetop, Horikawa | partially |
| ET-R4-4 | **L+W**, **P+W** | W (Construct), L (Model & Method), P (Inference), H (Model & Method) | 기억의 생성 모형(VAE 기반 재구성), 생성 AI | 회상된 정서는 의미 gist로 재구성되는가, 원 자극 고유 흔적으로 남는가 | Mind captioning (+ Horikawa) | no (부분 선행 있음) |

---

## ET-R4-1. 내성 접근인가 기억성인가: 정서 비디오 회상 vividness의 출처 분해

* **조합한 Axis:** W Internally Generated Experience(Construct), A의 Sub-axis Introspective Access and Emotion Report(Construct), R Explainability & Mechanistic AI(Structure: LLM introspection 연구의 self-prediction 대 cross-prediction 논리), O Individual & Population Variation(Neural), Q Reliability & Measurement(Inference: item 성분과 개인 성분의 분산 분할). 서로 다른 유형 4개.
* **미논의 쌍 포함 방식:** **R+W.** LLM 내성 연구가 "모델이 자기 행동을 외부 관찰자보다 잘 예측하는가"로 privileged access를 조작화한 방법(arXiv:2410.13787)을 사람의 회상 보고에 옮긴다. 외부 관찰자 역할은 "다른 참가자들의 같은 클립 재활성"과 "자극 계산 기억성 모형"이 맡는다.
* **왜 예상 밖인가:** 회상 vividness와 재활성의 대응(doi:10.1162/jocn_a_00839, doi:10.1523/JNEUROSCI.3022-16.2016)은 보통 "보고가 자기 뇌 상태를 반영한다"는 증거로 읽힌다. 그러나 기억성 연구는 어떤 자극이 누구에게나 더 잘 기억되는 자극 고유 속성이 있음을 보였다(doi:10.1038/s41598-018-26467-5). vividness가 사실은 "이 클립은 기억하기 쉬운 클립이다"라는 item 속성을 보고하는 것이라면, 재활성과의 상관은 내성 접근이 아니라 공통 원인(클립 기억성)의 결과일 수 있다. 정서 각성이 vividness를 높인다는 예측(NEVER, doi:10.3758/s13423-017-1313-9)도 같은 문제를 안는다: 정서 클립이 그냥 더 기억하기 쉬운 클립일 수 있다.
* **연구 질문:** Mind captioning 회상 시행에서 참가자의 vividness 보고는 클립 고유 기억성(다른 참가자들의 vividness와 재활성, 자극 계산 기억성)을 넘어 그 참가자 자신의 그 시행 재활성을 추가로 반영하는가, 그리고 정서 각성에 따른 vividness 증가는 item 성분과 개인 성분 중 어디를 통해 일어나는가?
* **설계:**
  1. 시행별 vividness를 세 층으로 분해한다. (a) 클립 수준: leave-one-subject-out 평균 vividness, 다른 참가자의 같은 클립 재활성 평균, 비디오 기억성 모형의 자극 계산 예측(arXiv:2009.02568 계열, AI 추정), 규범 arousal과 valence. (b) 참가자 x 클립 수준: 그 참가자의 해당 클립 평균 재활성(다섯 번 회상의 평균). (c) 시행 수준: 같은 클립 다섯 번 회상 사이의 재활성 변동.
  2. **privileged access 지표** = (b)와 (c)가 (a)를 통제한 뒤 vividness에 더하는 고유 설명 분산. 재활성은 시각 부분공간과 정서 부분공간으로 나눠 따로 계산한다(ET-P6, VD-P6 통합안과 같은 정의).
  3. 신경 위치: Bainbridge & Rissman(2018)은 기억성 정보는 복측, 내측 측두에, 주관 기억 판단 정보는 전두-두정에 겹치지 않게 있다고 보고했다. 같은 해리가 정서 비디오 회상에서도 나타나는지 RSA로 본다.
* **측정 가능한 예측과 반증 조건:**
  * 예측 A(내성 접근): (b), (c)의 고유 분산이 0보다 크다. 특히 시행 수준 (c)는 같은 클립 안의 변동이므로 클립 속성으로 설명될 수 없다.
  * 예측 B(정서의 경로): arousal 효과가 (a)를 통해서만 vividness에 오면 NEVER 효과는 item 중심(정서 클립이 원래 더 기억하기 쉬움)이다. (b), (c)의 정서 부분공간 재활성을 통해 오면 개인의 정서 재활성이 보고에 들어간다.
  * 반증: (a)를 통제하면 (b), (c)의 고유 분산이 영의 신뢰구간 안에 들어간다. 그러면 vividness 보고는 이 측정에서 자기 재활성에 대한 특권적 접근을 보여 주지 못하며, 기존 vividness-재활성 상관은 클립 기억성으로 설명된다.
* **가능한 데이터셋:** Mind captioning(주: 6명, 72클립 x 5회 회상, 시행별 vividness). Horikawa 2020 지각 데이터는 같은 클립 decoder 학습을 보강한다.
* **근거 논문:** doi:10.1126/sciadv.adw1464, arXiv:2410.13787, doi:10.1038/s41598-018-26467-5, arXiv:2009.02568, doi:10.1162/jocn_a_00839, doi:10.1523/JNEUROSCI.3022-16.2016, doi:10.3758/s13423-017-1313-9, doi:10.1016/j.cub.2024.09.062
* **선행 수행 검색:** WebSearch "memorability versus subjective vividness recall fMRI item-level memorability confound reinstatement individual trial vividness emotional videos", 2026-11-12. 결과: 반복 회상으로 item 안 변동과 item 간 차이를 분리할 수 있는 설계(doi:10.1162/jocn_a_00839)와 얼굴에서 기억성과 주관 판단의 신경 해리(doi:10.1038/s41598-018-26467-5)는 있다. 정서 비디오에서 vividness를 item 기억성과 개인 재활성으로 분해하고 정서 효과의 경로를 가른 연구는 찾지 못했다. **partially.**
* **label-provenance:** vividness = 참가자 본인 보고(대상은 심상의 질, 정서 아님). 클립 기억성 = 다른 참가자 보고(peer 합의)와 AI 추정(자극 계산 모형). 정서 = felt x 별도 평정자 규범.
* **evidence-level:** R0.
* **주의:** vividness는 회상 직후 실제 비디오를 다시 본 뒤 평정되어 비교 판단이 섞인다(VD-P6 반론). 6명이라 참가자 x 클립 성분 추정이 불안정할 수 있다. 기억성 모형 가중치와 라이선스는 미확인이고, Cowen & Keltner 클립이 Memento10k에 포함되었는지 오염 점검이 필요하다. 결과는 "보고와 신경 재활성의 대응"에 관한 것이며 정서 경험의 존재에 관한 것이 아니다(arXiv:2506.05068).
* **overlap:** 없음.

## ET-R4-2. Axis V의 측정 타당성: 행동 경향을 인간, AI, 뇌 세 방법으로 MTMM 검증하기

* **조합한 Axis:** V Action Readiness & Affordance(Construct), Q Reliability & Measurement(Inference: multitrait-multimethod 수렴, 변별 타당도), I AI Model Families(Model & Method: latent action model, MLLM 평정), F Brain Representation(Neural). 서로 다른 유형 4개.
* **미논의 쌍 포함 방식:** **Q+V.** 새 Axis V는 거의 전적으로 Emo-FilM의 Motivation 10항목(Stop, Undo, Repeat, Oppose, Tackle, Command, Support, Move, Care, Attention)에 기대고 있다. 그런데 이 항목들이 정서 범주나 valence와 구분되는 구성 개념을 재는지(변별 타당도)는 아무도 확인하지 않았다. Axis V를 조합에 쓰기 전에 Q가 맡아야 할 측정 문제다.
* **왜 예상 밖인가:** 심리측정의 고전 틀(MTMM, doi:10.1037/h0046016)에서 "방법"은 보통 자기보고, 관찰자 평정, 생리다. 여기서는 방법 자리에 **AI 모델**을 넣는다. 로봇 학습의 latent action model(arXiv:2410.11758)은 라벨 없이 "장면이 다음에 허용하는 움직임"을 표상하므로, 인간 평정과 공통 방법 분산을 공유하지 않는 행동 경향의 독립 측정치가 된다. 뇌는 셋째 방법이다.
* **연구 질문:** Emo-FilM에서 행동 경향은 인간 평정, AI 추정(latent action feature, MLLM 평정), 뇌 반응이라는 세 방법을 가로질러, 같은 방법 안의 정서 범주와 valence 상관보다 더 강하게 수렴하는가?
* **설계:**
  1. 특성(trait): 행동 경향(Motivation 10항목의 공통 요인), 이산 정서(13항목), appraisal(10항목), 느낌 valence(Feeling 항목의 Good/Bad).
  2. 방법(method): 인간 consensus 1 Hz(별도 평정자 규범), MLLM의 같은 항목 1 Hz 평정(AI 추정), 자극 계산 latent action feature를 각 특성 축에 사상한 값(AI 모델 내부), 뇌(특성별 교차검증 encoding 예측 시계열).
  3. 영화 단위 교차검증(leave-one-film-out)으로 MTMM 행렬을 만들고, 항목별 평정자 일치도(0.21~0.60, Stage 1)로 상관을 감쇠 보정한다. bifactor 모형으로 일반 valence 요인을 분리한 뒤 행동 경향 요인이 남는지 본다.
  4. Horikawa에서는 14차원 중 approach 차원 하나만으로 축소판(approach 대 valence)을 돌린다.
* **측정 가능한 예측과 반증 조건:**
  * 예측(V가 독립 구성 개념): 행동 경향의 같은 특성 다른 방법 상관(인간 ↔ latent action ↔ 뇌)이, 인간 평정 안에서 행동 경향과 valence의 상관보다 크다. 일반 valence 요인을 뺀 뒤에도 행동 경향 고유 요인이 방법 간에 수렴한다.
  * 반증: 행동 경향 항목이 일반 valence 요인에 대부분 적재되고 방법 간 수렴이 valence 수렴과 구분되지 않으면, Emo-FilM의 Motivation 항목은 valence의 재표현이다. 그러면 Axis V 질문은 이 데이터로 답할 수 없고 새 측정(행동 준비 과제, 근전도 등)이 필요하다는 결론이 된다. 이 결과는 brain-inspired Chain 2와 BI-P2의 해석 전제를 바꾼다.
* **가능한 데이터셋:** Emo-FilM(주, 행동 경향 평정이 있는 유일한 데이터). Horikawa 2020(approach 차원으로 축소판).
* **근거 논문:** doi:10.1037/h0046016, arXiv:2410.11758, doi:10.1038/s41597-025-04803-5, doi:10.1037/emo0001619, doi:10.1093/cercor/bhad093, doi:10.1371/journal.pbio.3000900, doi:10.1073/pnas.2414005122, doi:10.1016/j.isci.2020.101060 (Discussion 2째 단락 "emotional experience (or affordances)"), arXiv:2501.10970
* **선행 수행 검색:** WebSearch "multitrait multimethod emotion component process action tendency discriminant validity ratings fMRI machine learning features", 2026-11-12. 결과: 성분 모형 fMRI는 성분별 네트워크를 보고했지만(doi:10.1093/cercor/bhad093, doi:10.1371/journal.pbio.3000900) 방법 간 변별 타당도 검정은 아니다. Emo-FilM 계열 행동 연구(doi:10.1037/emo0001619)는 성분으로 이산 정서를 예측했다. AI 모델을 방법으로 넣은 MTMM은 찾지 못했다. **no.**
* **label-provenance:** 인간 평정 = 대상 felt(행동 경향 보고) x 별도 평정자 규범. MLLM = perceived x AI 추정. latent action = AI 모델 내부 표상(라벨 아님). 뇌 = 관찰.
* **evidence-level:** R0.
* **주의:** Emo-FilM은 평정자당 6항목만 배정되어 행동 경향 항목과 정서 항목의 평정자가 다를 수 있다. 이는 MTMM에서 같은 방법 안의 평정자 공유 분산을 줄여 변별 타당도 검정을 오히려 깨끗하게 하지만, "같은 사람 안의 구분"은 말하지 못한다. 평정은 평정자 내 z-score다. latent action model은 조작 비디오로 학습되어 영화 장면에 대한 도메인 이동이 크다(frontier-ai U8). 영화 14편이라 영화 단위 자유도가 작다.
* **overlap:** Emo-FilM 연구 (같은 데이터셋, 멀티모달 encoding 방법 일부).

## ET-R4-3. 라벨 출처를 view로: 출처 불변 정서 성분과 출처 특이 성분의 식별과 뇌 지도

* **조합한 Axis:** U Label Provenance & Perspective(Inference), J Learning Objectives(Model & Method: 다중 view 학습과 식별성), A Emotion & Affective Constructs(Construct), F Brain Representation(Neural). 서로 다른 유형 4개.
* **미논의 쌍 포함 방식:** **J+U.** 자기지도 학습 이론은 "여러 view 사이에 늘 보존되는 것이 content이고 view마다 바뀌는 것이 style"이며, 적절한 조건에서 content 블록을 식별할 수 있다고 보였다(arXiv:2106.04619, 다중양식 확장 arXiv:2303.09166). 이 학습 목표의 논리를 라벨 출처에 적용한다: 같은 자극에 대한 별도 평정자 규범, peer 합의, 본인 보고, AI 추정(관찰자 프롬프트, 경험자 프롬프트)을 서로 다른 view로 본다.
* **왜 예상 밖인가:** Axis U의 질문("라벨 주체가 바뀌면 뇌 설명력이 어떻게 달라지는가")은 지금까지 출처별로 따로 encoding해 성능을 비교하는 식으로 다뤄졌다(Du 2025, Santavirta 2025). 식별성 이론을 쓰면 비교가 아니라 **분해**가 된다. 출처 불변 성분은 "누가 보고하든 같은 정서 내용", 출처 특이 성분은 "관점"의 조작적 정의가 되고, 각 성분이 뇌의 어디에 대응하는지 물을 수 있다.
* **연구 질문:** 같은 영화 시점에 대한 인간 규범 평정과 AI 평정(관찰자, 경험자 프롬프트), 그리고 참가자 본인 보고를 다중 view로 두고 view 불변 성분과 view 특이 성분을 분리하면, 인간 특이 성분과 AI 특이 성분은 서로 다른 뇌 영역의 분산을 설명하는가?
* **설계:**
  1. Emo-FilM(주): view 1 = 별도 평정자 consensus 1 Hz(이산 13 + Feeling), view 2 = MLLM 관찰자 프롬프트 1 Hz, view 3 = MLLM 경험자 프롬프트 1 Hz, 보조 view = fMRI 참가자 사후 클립 평정(부분). 약 9,600개 시점에서 선형 다중 view 모형(generalized CCA, 식별성 이론의 선형 특수 경우)으로 불변 블록과 view 특이 잔차를 추정한다. 인간 view의 측정 잡음은 평정자 split-half로 보정한다.
  2. 각 블록을 banded ridge로 뇌에 encoding한다(영화 단위 교차검증).
  3. Spacetop(재현): view = 본인 보고, leave-one-subject-out peer 합의, MLLM 평정(영상 49개). 본인 특이 성분이 Emo-FilM의 인간 특이 성분과 같은 영역에 대응하는지 본다.
  4. Horikawa(축소판): view = 규범 34/14, MLLM 34/14.
* **측정 가능한 예측과 반증 조건:**
  * 예측: 불변 블록은 여러 연구에서 정서 decoding이 보고된 transmodal 영역(DMN, vmPFC)에 대응한다. 인간 특이 잔차는 신체 기반 정서와 관련된 섬엽, 체성감각 영역에(MLLM이 신체 정서에서 실패한다는 doi:10.1038/s41598-025-14961-6), AI 특이 잔차는 고차 시각 영역과 MST에(MLLM 우위 영역, arXiv:2509.24298) 대응한다.
  * 반증 1: 측정 잡음 보정 후 인간 특이 잔차가 불변 블록을 넘어 뇌 분산을 설명하지 못하면, 뇌와 관련된 라벨 정보는 AI 라벨이 모두 담는다(AI 대체 가능성 지지).
  * 반증 2: 불변 블록이 각 단일 view보다 뇌를 덜 설명하면, 출처들이 같은 구성 개념을 재지 않는다는 뜻이다(Axis U의 출처 간 측정 불변성 실패).
* **가능한 데이터셋:** Emo-FilM(주), Spacetop(본인 view 재현), Horikawa 2020(축소판).
* **근거 논문:** arXiv:2106.04619, arXiv:2303.09166, arXiv:2509.24298, doi:10.1162/imag.a.134, arXiv:2408.13718, doi:10.1162/tacl_a_00449, doi:10.1038/s41598-025-14961-6, doi:10.1162/imag_a_00517
* **선행 수행 검색:** WebSearch "human emotion ratings and AI model ratings shared versus unique components canonical correlation brain mapping label source multi-view emotion annotation fMRI", 2026-11-12. 결과: Du 2025(arXiv:2509.24298)는 인간과 AI 임베딩의 공유, 고유, 혼합 성분을 보고하고 뇌와 RSA로 비교했으며, Santavirta 2025(doi:10.1162/imag.a.134)는 GPT-4V와 인간 stimulus model의 뇌 지도를 비교했다. 라벨 출처를 view로 두고 출처 특이 잔차를 뇌에 따로 사상한 연구는 찾지 못했다. **partially.**
* **label-provenance:** 설계상 여러 출처를 함께 쓴다. 별도 평정자 규범(felt 보고), peer 합의(Spacetop, felt), 본인 보고(felt), AI 추정(관찰자 프롬프트는 perceived, 경험자 프롬프트는 felt-simulated).
* **evidence-level:** R0. AI view의 프롬프트 관점 조작은 모델 쪽 R1.
* **주의:** 식별성 결과는 view가 공유 latent와 view 특이 latent에서 충분한 변동을 가지고 생성된다는 가정 아래 성립한다. 라벨 view는 저차원이고 잡음이 커서 이론의 조건을 다 만족하지 않을 수 있으므로, 결과는 "선형 공유 부분공간"으로만 서술한다. 인간 consensus는 3~4명 평균이라 AI view보다 잡음이 커서, 보정하지 않으면 AI view가 뇌와 더 맞아 보이는 인공물이 생긴다(Du 2025에 대한 내 Round 1 비판과 같은 문제). MLLM은 성적, 폭력 내용에서 결측이 생긴다.
* **overlap:** 확인 필요 (EmoBrain의 multimodal teacher-student distillation이 AI 정서 표적을 쓰는지 미확인).

## ET-R4-4. 기억은 생성적 재구성인가: 회상된 정서는 의미 gist를 따르는가, 원 자극의 고유 흔적을 따르는가

* **조합한 Axis:** W Internally Generated Experience(Construct), L Generative & Counterfactual Methods(Model & Method: 캡션에서 재생성한 "gist" 자극), P Causality & Scientific Inference(Inference: 같은 클립의 지각 대 회상이라는 데이터셋 내부 과제 조작), H Encoding(Model & Method). 서로 다른 유형 3개(Construct, Model & Method, Inference).
* **미논의 쌍 포함 방식:** **L+W**와 **P+W.** 생성 모델을 "기억 재구성의 모형"으로 쓰고(L+W), 자극이 있을 때와 없을 때를 같은 참가자, 같은 클립에서 대비한다(P+W).
* **왜 예상 밖인가:** Spens & Burgess(2024)는 일화기억을 해마 replay가 학습시킨 생성 모형(VAE)의 재구성으로 정식화했다. 예측 가능한 개념 요소는 신피질 schema로 재생성되고, 새롭고 고유한 감각 요소는 해마에 저장되며, schema 기반 왜곡이 생긴다. 생성 AI 쪽에서는 캡션(의미)만으로 이미지를 다시 만드는 경로가 "의미 gist"를 정확히 구현한다. 이 둘을 붙이면 정서 이론의 오래된 질문을 계산 형태로 쓸 수 있다: 회상된 정서는 **schema로 재구성되는가**(LeDoux & Brown 2017의 schema 기반 정서 구성, doi:10.1073/pnas.1619316114), 아니면 **정서적 세부가 고유 흔적으로 남는가**(NEVER, doi:10.3758/s13423-017-1313-9)?
* **연구 질문:** Mind captioning에서 같은 클립을 회상할 때의 정서 관련 신경 패턴은 원 클립의 encoding 예측보다 그 클립의 의미 gist(정서 배제 인간 캡션)의 encoding 예측에 더 가까운가, 그리고 gist가 담지 못하는 원 클립 고유의 정서 성분은 회상에서 사라지는가?
* **설계:**
  1. 72개 테스트 클립마다 세 가지 예측 패턴을 만든다. (a) P_원본: 지각 데이터(Horikawa + Mind captioning)로 학습한 encoder에 원 프레임을 넣은 예측. (b) P_gist: 정서 배제 인간 캡션(클립당 20개)의 문장 embedding을 encoder 입력 공간으로 사상한 예측(생성 없음, 1차 분석). (c) P_gist-이미지: 캡션에서 text-to-image로 재생성한 이미지의 예측(2차 분석). (c)에는 VD-P4의 round-trip으로 추정한 생성기 중립화를 보정한다.
  2. 회상 패턴(클립당 5회)과 각 예측의 유사도를 시각 부분공간과 정서 부분공간에서 따로 잰다.
  3. 원 클립 고유 정서 성분 = 원 클립의 규범 정서 중 캡션 embedding으로 예측되지 않는 잔차. 이 잔차가 회상 패턴의 정서 부분공간에서 decoding되는지 본다.
  4. 대조: 정서 단어를 허용한 MLLM 캡션(AI 추정)으로 만든 두 번째 gist. 정서 언어가 들어간 gist가 회상 정서를 더 잘 예측하면 회상 정서는 언어화된 개념 지식을 따른다는 뜻이다.
* **측정 가능한 예측과 반증 조건:**
  * schema 재구성 예측: 회상의 정서 부분공간 패턴은 P_원본보다 P_gist에 상대적으로 가깝고(지각 때보다 그 차이가 커지고), 원 클립 고유 정서 잔차는 회상에서 decoding되지 않는다. vmPFC와 DMN에서 두드러진다.
  * 고유 흔적 예측(NEVER): 원 클립 고유 정서 잔차가 회상에서도 decoding되며, 부정 정서가 클립에서 더 강하다.
  * 반증(schema 재구성 가설): 원 클립 고유 정서 잔차가 회상 정서 부분공간에서 유의하게 decoding되고 그 크기가 시각 고유 잔차보다 크다.
* **가능한 데이터셋:** Mind captioning(주: 회상, 인간 중립 캡션). Horikawa 2020(encoder 학습 보강, 같은 비디오).
* **근거 논문:** doi:10.1038/s41562-023-01799-z, doi:10.1126/sciadv.adw1464, doi:10.3758/s13423-017-1313-9, doi:10.1073/pnas.1619316114, doi:10.1038/s41467-022-33161-8, arXiv:2506.06898, doi:10.1038/ncomms15037, doi:10.1093/cercor/bhv086
* **선행 수행 검색:** WebSearch "generative model memory construction recall gist semantic reconstruction emotional content retained fMRI recall of videos predicted by gist images versus originals"와 "emotion representation perception versus recall of the same video clips fMRI cross-decoding stimulus-independent emotion regions higher-order schema 2023 2024 2025", 2026-11-12. 결과: 회상의 gist 대 원본 예측을 비교한 연구는 찾지 못했다. 지각과 회상의 정서 표상 일관성은 fNIRS preprint(검색 요약만, 식별자 미확인이라 근거로 쓰지 않음)와 영화 시청 대 상상의 정서 교차 분류(doi:10.1093/cercor/bhv086, 같은 클립 회상은 아님)가 부분 선행이다. **no (부분 선행 있음).**
* **label-provenance:** 원 클립 정서 = felt x 별도 평정자 규범. gist = 기술 의미 x 별도 평정자(정서 배제 지시). 두 번째 gist = AI 추정. 회상 패턴 = 관찰 신경 반응(라벨 없음).
* **evidence-level:** 정서 결론은 R0. encoder 예측과 재생성 이미지는 R1(in-silico). 지각 대 회상 대비는 데이터셋 내부의 과제 조작이지만 정서 변수 자체를 조작한 것은 아니므로 정서에 대한 인과 수준을 올리지 않는다.
* **주의:** 회상 cue가 텍스트라 회상이 설계상 gist 쪽으로 기울 수 있다(vision-decoding R2 교란). 이 교란은 schema 재구성 가설에 유리한 방향이므로 cue 구간을 별도 모델링하고 해석을 보수적으로 한다. 정서 배제 캡션의 gist는 의도적으로 정서가 빈약하므로, P_gist의 정서 예측이 거의 중립이면 "회상 정서가 gist를 따른다"는 결과가 나올 수 없다. 그래서 두 번째 gist(정서 언어 허용)가 필요하다. 회상 직후 비디오 재제시와 HRF 겹침, 6명, 72클립 정서 분포 미확인.
* **overlap:** 없음. vision-decoding R2(회상 정서 재활성, NEVER)와 데이터와 일부 가설을 공유하지만, 이 제안의 핵심인 gist 대 원본 비교와 생성 모형 틀은 R2에 없다.

---

## 기각한 미논의 쌍과 이유

| 쌍 | 검토한 연결 | 기각 이유 |
|---|---|---|
| **M+W** | 소리와 영상이 회상에서 어떻게 다시 결합되는가 | 회상 데이터(Mind captioning)는 무음 비디오의 회상이고, Emo-FilM과 Spacetop에는 회상 과제가 없다. 다중양식 회상을 검정할 데이터가 없어 질문이 추측에 머문다 |
| **S+V** | 행동 경향 표상의 데이터셋 간 일반화 | 행동 경향 라벨은 Emo-FilM에만 있다. 다른 데이터셋의 행동 경향을 AI로 추정하면 AI가 라벨과 평가 기준을 함께 정의하게 되어 일반화 검정이 순환한다. ET-R4-2로 V의 측정 타당성을 먼저 확인한 뒤 재검토할 쌍이다 |
| **O+V** | 행동 경향의 개인차와 뇌 | 개인 수준 행동 경향 자료가 없다. Emo-FilM 평정은 별도 평정자 규범이고, Spacetop에는 동기 문항이 없다. 새 수집 없이는 측정할 수 없다 |
| **T+W** | 회상 decoding 벤치마크 | 성립은 하지만 벤치마크 구축에 그쳐 Novelty Constraint(P5)의 "정확도 개선" 범주에 가깝다. 과학 질문은 ET-R4-1과 ET-R4-4가 더 직접 다룬다 |

## 다른 미논의 쌍에 대한 메모 (내 담당 밖, 검토만)

* **K+V**(기하 x 행동 경향): ET-R4-2의 MTMM이 V의 변별 타당도를 확인하면, 행동 경향 공간의 기하(정서 범주 공간과의 정렬, CCGP)는 geometry-info가 다룰 만한 후속 질문이다. 변별 타당도 확인 전에는 V 공간의 기하가 valence 축의 재기술일 위험이 있다.
* **P+V**(인과 x 행동 경향): Spacetop 통증 과제의 기만 cue처럼 데이터셋 내부 조작이 있는 과제에는 행동 경향 측정이 없어, 내 관점에서는 현재 데이터로 성립하지 않는다.

## 검색 기록

* WebSearch 5건(2026-11-12): 각 제안의 "선행 수행 검색" 항목에 질의를 적었다.
* 식별자 확인: Crossref(doi:10.1038/s41562-023-01799-z, doi:10.1038/s41598-018-26467-5, doi:10.1037/h0046016), arXiv API(arXiv:2009.02568), PubMed 초록(앞의 두 편).
* 검색 요약에만 나와 근거로 쓰지 않은 것: 지각과 회상의 정서 표상을 비교한 fNIRS preprint, SemVideo(gist 우선 decoding 방법).
