# Round 4 (Unexpected Connections): geometry-info

* 작성: geometry-info (Axis K, O 담당) / 기준일 2026-11-12 / 절차: `reference/protocols.md` P4
* 입력: `outputs/combinations/discussed_pairs.md`(미논의 다른 유형 쌍 23개), `outputs/axis_encyclopedia.md` 3절(유형표), Stage 1 데이터셋 보고서, 내 Round 1~3 산출물
* 대상 쌍: 내 담당 Axis K가 들어간 미논의 쌍 B+K, K+P, K+V와, K와 묶이는 D+S. 이미 논의된 쌍만으로 이루어진 조합은 쓰지 않았다.
* 문헌: 이번 라운드에서 3편을 새로 식별자 경로로 확인해 `literature.jsonl`에 추가했다(arXiv:2112.04398, arXiv:2503.07811은 arxiv.org 초록 페이지, doi:10.1162/jocn.2009.21317은 Crossref와 PubMed). 나머지 근거는 내 jsonl 또는 `outputs/literature/literature_db.csv`의 verified 항목이다([DB]로 표시).
* 데이터셋 표기: Horikawa 2020(5명), Mind captioning(MC, 6명, 같은 2,180개 클립, 72개 x 6회 노출), Emo-FilM(30명), Spacetop(약 100명), NSD(8명).

## 요약

| ID | 조합(유형) | 포함한 미논의 쌍 | 한 줄 질문 | 선행 |
|---|---|---|---|---|
| GI-R4-1 | B(Construct) x K(Structure) x E(Neural) x Q(Inference), 외부: 통계물리식 스펙트럼 이론 | **B+K** | 자극 앙상블의 시각 차원과 정서 차원을 따로 바꾸면 영역별 공유 신경 스펙트럼은 어느 쪽을 따르는가 | no |
| GI-R4-2 | K(Structure) x P(Inference) x B(Construct) x E(Neural), 외부: 계량경제학의 최적 수송 매칭 | **K+P, B+K** | 정서 범주 사이에서 내용이 맞는 클립만 OT로 짝지으면 이 라이브러리에서 정서와 내용은 어디까지 분리되며, 분리된 쌍에서 정서 차이는 남는가 | no (방법은 있음, 정서 fMRI 적용 미발견) |
| GI-R4-3 | V(Construct) x K(Structure) x E(Neural) x A(Construct), 외부: 원숭이 전기생리의 추상화 기하(CCGP) | **K+V** | 자연 영화에서 동기 방향(맞섬 대 멈춤)은 valence와 독립된 추상 형식으로 표상되는가 | partially (과제 fMRI의 단변량 선행) |
| GI-R4-4 | D(Construct) x S(Inference) x K(Structure) x E(Neural), 외부: 동역학 유사도 분석(DSA) | **D+S** | 영화를 바꿔도 정서 잠재 공간의 흐름(이완, 회전, 비대칭)은 좌표 사상보다 더 잘 보존되는가 | partially (MD Chain 7과 방법 일부 겹침) |

기각: K+L, O+V(보류), P+W. 이유는 5절.

---

## GI-R4-1. 자극 앙상블의 기하가 신경 정서 기하를 만드는가: 시각 차원과 정서 차원의 분리 조작

* **조합한 Axis:** B Perceptual & Stimulus Representation(Construct) x K Geometry(Structure) x E Neural Targets(Neural) x Q Reliability & Measurement(Inference). 외부 개념: 집단 부호의 power-law 스펙트럼 이론(시스템 신경과학, 통계물리식 분석).
* **미논의 쌍 포함 방식:** B+K. "자극 표상의 기하"(B)를 독립 변수로, "신경 표상 스펙트럼의 기하"(K)를 종속 변수로 놓는다. 지금까지 B는 encoding feature나 nuisance로만, K는 신경 쪽 측정으로만 쓰였다.
* **배경:** Stringer et al. 2019는 마우스 V1에서 더 저차원인 자극 앙상블이 더 큰 스펙트럼 감쇠 지수를 낳는다는 이론 예측을 실험으로 확인했다(doi:10.1038/s41586-019-1346-5 [초록]). Gauthaman et al.은 인간 시각 피질의 scale-free 스펙트럼이 자극 다양성에 얼마나 의존하는지, 상위 영역에서 달라지는지를 미해결로 남겼다(arXiv:2409.06843, 4 Discussion 4.1 [본문]; 출판본 doi:10.1371/journal.pcbi.1013714). 같은 분야의 후속 보고는 지수가 추정기와 실험에 따라 달라진다고 했다(검색 요약, 아래 선행 검색). vision-decoding은 Cowen & Keltner 라이브러리가 범주 유발용 군집 표본이라 "범주 기하"가 표집에서 생길 수 있다고 지적했다(doi:10.1016/j.neunet.2025.107515 [DB]).
* **연구 질문:** "Horikawa와 Mind captioning이 공유하는 2,180개 클립에서 시각 feature 공간의 유효 차원과 규범 정서 평정 공간의 유효 차원을 서로 독립으로 바꾼 부분집합을 만들면, 각 영역의 개인 간 공유 신경 스펙트럼의 감쇠 지수와 공유 rank 폭은 어느 쪽 차원을 따라 바뀌는가?"
* **설계:** 2 x 2 부분집합(시각 차원 높음/낮음 x 정서 차원 높음/낮음), 각 같은 수(예: 400개). 선택은 자극 수준 정보만 쓴다: 시각 차원은 비디오 모델 feature의 유효 rank, 정서 차원은 34 + 14 규범 평정의 유효 rank. 한쪽 차원을 바꿀 때 다른 쪽의 유효 rank와 평균 강도(arousal)를 맞춘다. 뇌 자료는 선택에 쓰지 않으므로 순환이 없다. 각 부분집합에서 11명(코호트 내 쌍과 코호트 간 쌍 분리)의 교차 스펙트럼을 V1~V4, LOC, TPJ, vmPFC, 섬엽에서 계산한다(GI-P1의 파이프라인).
* **측정 가능한 예측:** (1) 초기 시각 피질의 지수는 시각 차원 조작에 따라 바뀌고 정서 차원 조작에는 둔감하다(Stringer 예측의 인간 재현). (2) transmodal 영역 중 정서 차원 조작(시각 차원 고정)에 지수나 공유 rank 폭이 반응하는 영역이 있다면, 그 영역의 표상 스펙트럼은 자극의 정서 다양성에 맞춰져 있다("정서 조율 스펙트럼").
* **반증 조건:** transmodal 영역도 시각 차원 조작에만 반응하면, 그 영역의 "정서 기하"는 자극 시각 기하의 상속이다. 어느 영역도 어느 조작에도 반응하지 않으면 스펙트럼은 앙상블 불변(보편)이며, 이 경우 "정서 차원 수" 논쟁은 앙상블과 무관한 신경 속성의 문제가 된다. 지수 차이가 추정기(교차검증 PCA, cross-decomposition, 대역 절단 방식)를 바꾸면 사라지면 결론을 내리지 않는다.
* **가능한 데이터셋:** Horikawa 2020 + MC(주). NSD shared 이미지는 정서 범위가 좁아 "정서 차원 낮음" 극단의 시각 대조로만 쓴다(정서는 AI 추정 표기). Emo-FilM, Spacetop은 자극 수가 적어 부적합.
* **근거:** doi:10.1038/s41586-019-1346-5, arXiv:2409.06843, arXiv:2505.12653 [DB], doi:10.1016/j.neunet.2025.107515 [DB], doi:10.1126/sciadv.adw1464
* **선행 수행:** no. WebSearch "stimulus ensemble dimensionality effect on neural covariance spectrum power-law exponent fMRI human higher-order cortex stimulus diversity" (2026-11-12): 상위 피질에서 자극 다양성을 조작 변수로 둔 연구 미발견. Gauthaman 계열이 이를 열린 문제로 남겼고, 검색 요약에 지수의 추정기, 실험 의존성(CCN 2024 초록, search_index)이 나왔다.
* **주의:** 부분집합 400개면 추정 가능한 rank가 줄어 지수 비교 범위가 좁아진다. 정서 평정은 9~17명 평균이라 정서 차원 추정에 잡음이 크다. 시각 차원과 정서 차원을 완전히 독립으로 만들 수 있는지(가능한 부분집합의 범위)를 먼저 센다.
* **label-provenance:** 정서 차원은 대상 felt / 주체 별도 평정자 규범(MTurk). 시각 차원은 계산된 자극 feature. **evidence-level:** R0(자극 선택 설계, 관찰 자료). **G1:** 시각 feature 추출에 필요(보유). **overlap:** EmoViS (Horikawa 정서 기하의 sensory-semantic 기원과 부분 겹침)

---

## GI-R4-2. 정서와 내용의 분리 가능성 지도: unbalanced optimal transport 매칭을 자연 자극의 positivity 진단으로

* **조합한 Axis:** K Geometry(Structure, Optimal Transport) x P Causality & Scientific Inference(Inference, 매칭과 overlap) x B Perceptual & Stimulus Representation(Construct) x E Neural Targets(Neural). 외부 개념: 계량경제학의 OT 기반 인과 매칭.
* **미논의 쌍 포함 방식:** K+P(OT를 인과 추정의 매칭 도구로), B+K(자극 내용 분포 사이의 수송).
* **배경:** 관찰 연구의 공변량 매칭을 다중 주변 unbalanced OT로 하면 좋은 짝만 남기고 짝이 없는 개체는 버리며, 정합 거리 기반 가중치를 해석할 수 있다(Gunsilius & Xu, arXiv:2112.04398 [초록]). 인과 추론의 많은 식별 가정이 암묵적으로 OT 원리에 기대어 있다(Gunsilius, arXiv:2503.07811 [초록]). 정서 fMRI 쪽에서는 내용 통제를 회귀(banded ridge, LS-P1)나 생성 편집(GC-P2), controversial 선택(EF Chain 4)으로 다뤄 왔다. 회귀는 정서 범주 사이에 내용이 겹치지 않는 영역(positivity 위반)에서도 선형 외삽으로 "정서 고유 분산"을 낸다(Westfall & Yarkoni의 측정 오차 문제와 별개의 문제, doi:10.1371/journal.pone.0152719 [DB]).
* **연구 질문:** "정서 범주 쌍마다 시각-의미 내용 분포 사이의 unbalanced OT 매칭으로 내용이 맞는 클립 쌍만 남기면, 이 자극 라이브러리에서 어느 범주 쌍이 내용과 분리 가능하며(overlap), 분리 가능한 쌍에서 transmodal 영역의 정서 차이는 남는가?"
* **설계:** 내용 표상 = MC 정서 배제 인간 캡션 20개의 LLM embedding 평균 + 비디오 모델 feature + 저수준 시각 통계. 범주 배정은 34범주 규범 선택 비율(최고 범주 또는 연속 가중). 범주 쌍마다 unbalanced OT 결합을 풀어 (a) 미매칭 질량 비율 = "이 라이브러리에서 그 범주 쌍은 내용으로부터 분리될 수 없는 정도"(positivity 지도), (b) 비용이 낮은 짝들의 신경 패턴 차이를 피험자와 코호트를 가로질러 교차검증한다. 같은 범주 안에서 내용으로 짝지은 쌍의 차이를 null로 둔다. 회귀 기반 추정(LS-P1식 분할)과 매칭 기반 추정을 같은 표에 둔다.
* **측정 가능한 예측:** (1) 범주 쌍 대부분에서 미매칭 질량이 크다면(예: awe와 disgust는 내용 분포가 거의 겹치지 않음), Horikawa 자극으로는 어떤 방법으로도 그 쌍의 내용 독립 정서 효과를 식별할 수 없다. (2) overlap이 있는 쌍에서 정서가 실제로 내용 너머에 표상된다면, 매칭 쌍 차이가 transmodal 영역에서 같은 범주 null보다 크고 시각 피질에서는 null 수준으로 줄어든다.
* **반증 조건:** 매칭 쌍 차이가 transmodal 영역에서도 null과 구분되지 않으면, 측정된 내용으로 설명되지 않는 정서 효과는 이 자료에서 지지되지 않는다. 회귀 추정은 정서 고유 효과를 내는데 매칭 추정은 내지 못하면, 회귀 결과가 overlap 밖 외삽에서 왔을 가능성이 크다.
* **가능한 데이터셋:** Horikawa 2020 + MC(주, 캡션 보유 여부 확인 필요). Emo-FilM(장면 창 단위, 내용은 MLLM 캡션으로 대체하고 AI 생성 표기). NSD(AI 추정 정서 라벨, 정서 범위가 좁아 overlap이 어떻게 나오는지 대조).
* **근거:** arXiv:2112.04398, arXiv:2503.07811, doi:10.1371/journal.pone.0152719 [DB], doi:10.1126/sciadv.adw1464, doi:10.1016/j.isci.2020.101060, doi:10.1073/pnas.1912334117 [DB]
* **선행 수행:** no(정서 fMRI 적용). WebSearch "optimal transport matching covariate balance stimuli confound fMRI naturalistic emotion content-matched pairs causal" (2026-11-12): OT 인과 매칭 방법(arXiv:2112.04398, arXiv:2503.07811)과, BCI에서 자극 속성 균형의 필요성을 다룬 연구(PMC9731219, search_index)는 있으나 정서 fMRI의 OT 매칭과 positivity 진단은 미발견.
* **주의:** 매칭은 측정된 내용에만 균형을 준다. 측정되지 않은 내용(서사 맥락, 문화 의미)은 남는다. 결론은 "측정된 내용 조건부"로만 쓴다. 매칭 쌍 수가 적은 범주 쌍은 검정력이 낮다. 캡션 작성자(영어 MTurk)와 MC 참가자(일본어 화자)의 언어 불일치.
* **label-provenance:** 범주는 대상 felt / 주체 별도 평정자 규범. 내용은 별도 평정자의 시각 내용 기술(정서 배제 지시)과 계산 feature. Emo-FilM 대체 캡션은 AI 추정. **evidence-level:** R0(설계 기반 관찰 추정, 인과 보장 없음). **G1:** 비디오 feature에 필요(보유). **overlap:** EmoViS (sensory-semantic 기원, 부분)

---

## GI-R4-3. 동기 방향은 valence와 독립된 추상 축인가: 자연 영화의 교차조건 일반화

* **조합한 Axis:** V Action Readiness & Affordance(Construct) x K Geometry(Structure, Abstraction Geometry) x E Neural Targets(Neural) x A Emotion & Affective Constructs(Construct). 외부 개념: 원숭이 해마, 전전두 집단 기록에서 나온 cross-condition generalization performance와 shattering dimensionality(doi:10.1016/j.cell.2020.09.031).
* **미논의 쌍 포함 방식:** K+V. 행동 경향(V)이 범주를 가로지르는 추상 형식으로 표상되는지를 기하(K)로 측정한다. 지금까지 V는 banded ridge의 설명 band(BI-P2)로만 다뤄졌다.
* **배경:** 과제 fMRI에서 배외측 전전두의 비대칭은 자극 valence와 무관하게 접근 행동을 따랐다(Berkman & Lieberman 2010, doi:10.1162/jocn.2009.21317 [초록]). 영화 클립의 CPM 성분 평정으로 approach/avoidance를 포함한 기능 과정의 네트워크가 보고되었다(Mohammadi et al. 2023, doi:10.1093/cercor/bhad093 [DB, 초록]). Emo-FilM에는 Motivation 10항목(Stop, Undo, Repeat, Oppose, Attention, Tackle, Command, Support, Move, Care)의 1 Hz 연속 평정이 있다(Stage 1 dataset_EmoFilM.md 항목표). 추상화 기하는 같은 변수가 다른 조건 쌍으로 학습한 decoder에 일반화되는지(CCGP)로 측정된다(Bernardi 2020 [본문]).
* **연구 질문:** "자연 영화 시청 중 vmPFC, 편도체, 배외측 전전두, 운동전과 두정 영역에서 동기 방향(맞서기 Oppose 대 멈추기 Stop)은 valence와 독립된 추상 형식으로 표상되는가, 아니면 valence에 묶여 있는가?"
* **설계:** Emo-FilM consensus로 TR 단위 조건을 정의한다: 부정-맞섬(Bad 높음 + Oppose 높음, 분노형), 부정-멈춤(Bad 높음 + Stop 높음, 공포형), 긍정-지속(Good 높음 + Repeat 높음), 가능하면 긍정-멈춤. HRF를 반영한 상태 지시변수로 영역 패턴을 만들고 leave-one-film-out으로 (a) 부정 안에서 학습한 동기 방향 decoder를 긍정 쪽 대응 쌍에 적용, (b) 맞섬 조건 안에서 학습한 valence decoder를 멈춤 조건에 적용, (c) 조건 dichotomy 전체의 shattering dimensionality를 계산한다. 0단계로 Motivation 항목과 discrete 항목의 평정 수준 공선성(BI-P2의 파일럿)과 조건별 TR 수를 센다.
* **측정 가능한 예측:** V가 A와 별개의 구성 개념이라면 적어도 한 영역(배외측 전전두나 운동전-두정)에서 동기 방향의 CCGP가 우연보다 높고, vmPFC에서는 valence CCGP가 높다(Ma & Kragel의 vmPFC affective space와 정합, doi:10.1038/s41467-025-68240-z). 두 변수가 모두 높은 CCGP를 가지면 "valence와 동기 방향이 직교하는 추상 축"이라는 factorized 기하다.
* **반증 조건:** 동기 방향이 같은 valence 안에서는 decoding되지만 valence를 건너서는 우연 수준이면, 동기 방향은 valence에 묶인 범주 특이 성분이다(Axis V를 독립 구성 개념으로 둔 판단에 불리한 증거). 0단계에서 Motivation 평정이 discrete 평정으로 거의 완전히 예측되면 이 데이터로는 분리할 수 없다고 보고하고 중단한다.
* **가능한 데이터셋:** Emo-FilM(주, 인간 행동 경향 평정이 있는 유일한 데이터). Horikawa 2020 + MC로 확장하려면 34범주에 동기 방향을 새로 평정해야 한다(R2). MLLM으로 매기면 AI 추정으로 표기하고 보조로만 쓴다.
* **근거:** doi:10.1016/j.cell.2020.09.031, doi:10.1162/jocn.2009.21317, doi:10.1093/cercor/bhad093 [DB], doi:10.1038/s41467-025-68240-z, doi:10.1037/emo0001619 [DB]
* **선행 수행:** partially. WebSearch "approach avoidance motivational direction dissociated from valence fMRI multivariate pattern anger fear cross-classification abstract representation" (2026-11-12): 과제 기반 단변량 ROI 분리(Berkman & Lieberman 2010)와 접근-회피 갈등 과제 연구는 있으나, 자연 자극에서 동기 방향의 교차조건 일반화를 본 연구는 미발견. 내 Round 2 기록상 정서 범주를 조건으로 한 CCGP도 미발견(양식 간 valence 일반화는 doi:10.1038/nn.3749).
* **주의:** 동기 평정은 3~4명 consensus이며 항목별 일치도가 낮을 수 있다(Emo-FilM 평균 0.38~0.39, 항목별 0.21~0.60). 조건 정의에 평정 임계값이 들어가므로 여러 임계값으로 견고성을 본다. 영화 14편이라 조건이 특정 영화에 몰리면 영화 정체성이 섞인다(영화 내 균형 확인). 표상된 "동기"는 별도 평정자가 보고한 행동 경향이지 fMRI 참가자의 행동 준비가 아니다.
* **label-provenance:** 대상 felt(평정자의 "you felt/wanted ..." 1인칭 문항) / 주체 별도 평정자 consensus. **evidence-level:** R0. **G1:** 불필요. **overlap:** Emo-FilM 연구 (같은 데이터, 정서 맥락 기여와 약하게 겹침)

---

## GI-R4-4. 지도는 영화마다 바뀌어도 흐름은 보존되는가: 정서 동역학의 휴대성

* **조합한 Axis:** D Temporal Dynamics(Construct) x S Generalization & Robustness(Inference) x K Geometry(Structure, Dynamical Attractors, Latent Trajectories) x E Neural Targets(Neural). 외부 개념: 동역학 유사도 분석(DSA, arXiv:2306.10168 [DB]), Koopman 선형화.
* **미논의 쌍 포함 방식:** D+S. 정서 동역학(D)의 "일반화"(S)를 지도(좌표 사상)와 흐름(벡터장)으로 나눠 묻는다. 이전 라운드의 일반화 논의는 decoder와 encoder의 전이(S+H, S+G)였고, 동역학의 전이는 다루지 않았다.
* **배경:** dynamic FC 기반 arousal 판독은 영화와 데이터셋을 넘어 전이되지만 valence는 전이되지 않았다(Ke et al. 2025, doi:10.1371/journal.pcbi.1012994 [본문]). Emo-FilM 고차 위상 연구는 valence 비전이에도 정서 상태의 상대 기하는 데이터셋 간 보존된다고 보고했다(Zaffina et al. 2026, doi:10.64898/2026.09.26.754452, Discussion 4째 단락 [본문]). DSA는 기하가 달라도 동역학이 같을 수 있음을 비교하는 도구다. multimodal-dynamics Chain 7은 같은 영화 안에서 평정, 뇌, MLLM 궤적의 동역학을 비교하자고 제안했다(D+K, 논의됨).
* **연구 질문:** "Emo-FilM에서 영화를 바꾸면 정서 정렬 잠재 공간의 흐름(이완 속도, 회전 성분, 방향 비대칭)은 valence 좌표 사상보다 더 잘 보존되는가, 그리고 그 보존은 자극 동역학(편집 속도, 서사 전개)으로 설명되는가?"
* **설계:** 학습 영화의 consensus로 정서 정렬 부분공간을 정의하고(시각 정렬 부분공간을 대조로 함께 정의), 보류 영화에서 참가자별 잠재 궤적을 얻는다. 영화별로 선형 동역학(Koopman/DMD) 모형을 적합해 DSA 거리를 계산한다. 비교 세 가지: (a) 영화 간 흐름 거리, (b) 영화 간 기하 거리(shape metric, arXiv:2110.14739), (c) valence decoder의 영화 간 전이 성능. 대조 둘: 시각 정렬 부분공간의 흐름, 그리고 평정 궤적을 HRF로 합성한 "자극 구동 대리 궤적"의 흐름. 입력이 없는 영화 후 90 s washout 구간의 흐름을 가장 깨끗한 내재 동역학으로 함께 본다(GI-P3과 연결).
* **측정 가능한 예측:** 정서가 자극에 대한 매핑이 아니라 뇌 고유의 동역학이라면, 정서 부분공간의 흐름은 영화 간에 기하나 decoder 사상보다 더 보존되고, 자극 구동 대리 궤적의 흐름 차이보다 영화 간 차이가 작다. 시각 부분공간 흐름은 영화 편집 속도에 따라 더 크게 바뀐다.
* **반증 조건:** 정서 부분공간 흐름의 영화 간 차이가 자극 구동 대리 궤적의 차이와 같으면 흐름은 자극에서 상속된 것이다. 정서 부분공간과 시각 부분공간의 흐름 보존이 같으면 정서 고유 동역학의 증거가 아니다. HRF 합성 대리 자료와 위상 무작위화 null로도 같은 보존이 나오면 BOLD 자기상관의 산물이다.
* **가능한 데이터셋:** Emo-FilM(주, 14편, 30명, washout과 생리). Spacetop alignvideo는 영상이 20 s~5분이라 동역학 추정이 짧고 연속 평정이 없어 신경 전용 보조 분석(같은 참가자들의 SRM 공간에서 영상 간 흐름 비교)으로만 쓴다. Horikawa와 MC는 블록 평균 짧은 클립이라 부적합.
* **근거:** arXiv:2306.10168 [DB], doi:10.1371/journal.pcbi.1012994, doi:10.64898/2026.09.26.754452, doi:10.1126/sciadv.abf7129, doi:10.1038/s41586-024-07915-x, arXiv:2110.14739
* **선행 수행:** partially. WebSearch "dynamical similarity analysis generalization across movies neural dynamics emotion fMRI flow field transfer across stimuli latent dynamics portable" (2026-11-12): DSA를 영화 정서 fMRI에 적용하거나 흐름의 영화 간 전이를 검정한 연구 미발견. 같은 팀의 multimodal-dynamics Chain 7이 Emo-FilM DSA를 이미 제안했으므로(평정-뇌-MLLM 비교) 방법 일부가 겹치고, 새 부분은 영화 간 휴대성(S)과 자극 구동 대리 궤적 대조다.
* **주의:** TR 1.3 s와 HRF 평활이 빠른 동역학을 지운다. 영화 길이가 6.7~17.1분으로 달라 동역학 추정의 정밀도가 영화마다 다르다. 제공 전처리본의 high-pass(sigma 50 s)는 느린 흐름을 왜곡하므로 raw 재전처리가 필요하다. 정서 부분공간 정의가 별도 평정자 consensus에 의존한다.
* **label-provenance:** 부분공간 정의는 대상 felt / 주체 별도 평정자 consensus. 흐름 자체는 라벨 없음. **evidence-level:** R0. **G1:** 시각 부분공간 정의에 필요(보유). **overlap:** Emo-FilM 연구 (Emo-FilM 시간 정보 기여, 부분)

---

## 5. 기각하거나 보류한 쌍

| 쌍 | 시도한 연결 | 판정 | 이유 |
|---|---|---|---|
| K+L | 생성 모델의 잠재 보간 경로로 뇌 정서 공간의 곡률(측지선과 직선의 차이)을 측정 | **기각** | 새 fMRI 없이 가능한 것은 encoder 예측 위의 R1뿐인데, 정서 영역에서 encoder가 충실하다는 전제가 아직 없다(EF-P1 관문 미통과). 기하 성분은 generative-counterfactual의 affective metamer(Round 1 X2)와 사실상 같은 질문이라 새 연결이 아니다. EF-P1 관문 통과 후 또는 R3 수집 계획이 생기면 다시 본다 |
| O+V | 행동 경향(접근 동기)의 개인차가 개인 정서 기하를 바꾸는가 | **보류** | 개인 수준 행동 경향 측정이 없다. Spacetop alignvideo 7차원에는 동기 문항이 없고, Emo-FilM Motivation 평정은 별도 평정자 consensus다. Emo-FilM fMRI 참가자 질문지에 접근/회피 특성 척도가 있는지 확인되면 30명 탐색 분석으로 재검토한다(Berkman & Lieberman 2010은 특성 접근 동기가 비대칭을 조절한다고 보고, doi:10.1162/jocn.2009.21317) |
| P+W | Mind captioning 회상을 "감각 입력 제거"라는 자연 개입으로 보고 지각-회상 기하 차이를 인과적으로 해석 | **기각** | 회상은 깨끗한 개입이 아니다. 회상 cue가 정서 배제 캡션 텍스트이고 회상 직후 같은 비디오가 재제시된다(doi:10.1126/sciadv.adw1464, Imagery experiment 절). 인과 틀을 붙여도 evidence-level은 R0를 넘지 못하며, 회상 재활성 질문은 vision-decoding R2, emotion-theory ET-P6, encoding-foundation EF-P2와 내 VD-P2 응답(기하 보존 지표)이 이미 다룬다 |

---

## 6. 검색 기록 (2026-11-12)

| 제안 | 경로와 질의 | 결과 |
|---|---|---|
| GI-R4-1 | WebSearch "stimulus ensemble dimensionality effect on neural covariance spectrum power-law exponent fMRI human higher-order cortex stimulus diversity" | 상위 피질 자극 다양성 조작 미발견. 지수의 추정기, 실험 의존성(검색 요약, search_index) |
| GI-R4-2 | WebSearch "optimal transport matching covariate balance stimuli confound fMRI naturalistic emotion content-matched pairs causal"; arxiv.org 초록 페이지 2건 확인 | OT 인과 매칭 방법만 있고 정서 fMRI 적용 미발견 |
| GI-R4-3 | WebSearch "approach avoidance motivational direction dissociated from valence fMRI multivariate pattern anger fear cross-classification abstract representation"; PubMed 메타데이터(PMID 19642879) | 과제 기반 단변량 선행만. 자연 자극 CCGP 미발견 |
| GI-R4-4 | WebSearch "dynamical similarity analysis generalization across movies neural dynamics emotion fMRI flow field transfer across stimuli latent dynamics portable" | 정서 영화 DSA, 흐름 전이 미발견. 팀 내 MD Chain 7과 방법 일부 겹침 |
