# Round 4: Unexpected Connections, brain-inspired (Agent 11)

* 기준일: 2026-11-12. 절차: `reference/protocols.md` P4. 읽은 자료: `outputs/combinations/discussed_pairs.md`(논의되지 않은 서로 다른 유형의 2개 조합 23개, Axis별 등장 횟수), `outputs/axis_encyclopedia.md` 3절(유형표).
* 출발점: 담당 Axis V(5회 등장, 가장 적음)와 N이 들어간 미논의 쌍 F+V, J+V, K+V, M+V, N+W, O+V, P+V, Q+V, S+V, T+V를 모두 검토했다. 성립하는 연결 4개를 제안하고(1~4절), 성립하지 않거나 다른 제안에 흡수되는 쌍은 기각 사유를 적었다(5절). 다른 에이전트 담당 쌍(B+K, D+G, D+S, I+W, J+U, J+W, K+L, K+P, L+W, M+W, P+W, R+W, T+W)은 다루지 않았다.
* 각 제안은 서로 다른 유형에서 Axis를 3개 이상 쓰고, 그중 하나 이상은 Affective Neuroscience 밖의 개념이나 방법이다. 미논의 쌍이 들어 있으므로 그 쌍을 포함한 3개 조합도 discussed_pairs에 없다.
* 선행 수행 여부는 이번에 실제로 검색했다(WebSearch, api.crossref.org, export.arxiv.org; 2026-11-12). 검색 결과로 확인한 선행 논문은 식별자 경로로 확인해 `literature.jsonl`에 추가했다(11편, 총 73편). arXiv API는 단건 ID 조회만 성공했고 검색 질의는 429로 막혀 WebSearch로 대신했다(우회 없음).
* 데이터셋 5개: Horikawa 2020, Emo-FilM, Spacetop, NSD, Mind captioning(Horikawa 2025).

---

## BI-R4-1. 행동 준비는 운동 실행의 null space에 있는가

* **조합한 Axis:** K Geometry & Mathematical Structure(Structure) + V Action Readiness & Affordance(Construct) + E Neural Targets(Neural) + 외부 분야: 운동 신경과학의 집단 동역학(output-null subspace). **미논의 쌍 K+V**를 포함한다.
* **연결의 논리:** 운동 피질은 움직이기 전 준비 활동을 하지만, 그 활동은 근육 출력에 영향을 주지 않는 방향(null space)에 놓여 "움직임 없는 준비"가 가능하다(Kaufman et al. 2014, doi:10.1038/nn.3643, 제목 수준). 준비와 실행은 서로 직교하는 부분공간을 쓴다(Elsayed et al. 2016, doi:10.1038/ncomms13239, 초록). Frijda 계열의 action readiness는 "행동하지 않으면서 행동할 준비가 된 상태"다. 정서 영상을 가만히 보는 동안 전운동, 두정 피질에서 나타나는 정서 관련 활동(Goldberg et al. 2014, doi:10.1016/j.neuroimage.2013.08.032)이 바로 이 "출력 없는 준비"의 거시 판일 수 있다. 두 분야는 서로를 인용하지 않는다.
* **연구 질문:** 정서 영상을 수동 시청할 때 전운동, 두정 피질의 정서 관련 활동 패턴은 같은 사람이 실제로 움직일 때(평정 trackball 조작)의 패턴과 직교하는 부분공간에 놓이며, 그 직교 성분의 크기는 본인이 보고한 정서 강도를 따라 변하는가?
* **측정 가능한 예측:**
  1. Spacetop 참가자별로 다른 과제의 응답 구간(social, faces 과제의 평정 조작)에서 "운동 실행 부분공간"(전운동, SMA, 두정 voxel 패턴의 주성분)을 추정한다.
  2. alignvideo 시청 구간(평정 구간 이전 TR만)의 영상별 패턴을 이 부분공간에 투영한다. 예측: 실행 부분공간에 실리는 분산 비율이 같은 차원의 무작위 부분공간 기준보다 크지 않다(직교 또는 그 이하).
  3. 실행 부분공간의 여공간(null 쪽)에 남는 영상별 패턴 크기가 본인 평정(afraid, warm and tender, engaged)과 상관한다. afraid와 warm and tender는 각각 회피, 접근형 행동 준비의 대리로 둔다(라벨 해석 주의).
* **반증 조건:** (a) 시청 패턴이 실행 부분공간에 무작위 기준보다 유의하게 크게 실리고 그 적재량이 평정을 따라가면, 정서 영상 중 전운동 활동은 "출력 없는 준비"가 아니라 은밀한 운동 활성 또는 미세 움직임이다. (b) 여공간 성분이 평정과 무관하면 null space 해석은 지지되지 않는다.
* **교란과 한계:** fMRI voxel 패턴의 부분공간은 신경 집단 부분공간이 아니다. 이 검정은 거시 수준 유비이며 원 이론의 확증이 아니다(이론적으로 가능하지만 관찰 데이터로 구분할 수 없는 설명 표시). alignvideo 평정 구간은 영상 직후라 HRF가 겹치므로 같은 과제의 평정 구간으로 실행 부분공간을 추정하면 안 된다(다른 과제의 응답 구간 사용). 머리 움직임, 안구 운동 공변량. Spacetop에는 행동 경향 문항이 없어 afraid 등을 대리로 쓴다는 점이 가장 큰 구성 타당도 문제다.
* **데이터셋:** Spacetop(주: 같은 참가자의 수동 영상 시청과 여러 과제의 trackball 응답, TR 0.46 s). Emo-FilM은 운동 과제가 없어 실행 부분공간을 추정할 수 없으므로, 여기서 얻은 null 성분 축이 Emo-FilM Motivation 항목 시계열을 따르는지 보는 보조 일반화에만 쓴다(functional alignment 필요).
* **근거 논문:** doi:10.1038/nn.3643, doi:10.1038/ncomms13239, doi:10.1016/j.neuroimage.2013.08.032, doi:10.1016/j.isci.2020.101060(Discussion 2째 단락 "emotional experience (or affordances)"), doi:10.1073/pnas.2414005122
* **선행 수행 여부:** **partially.** 정서 영상이 행동 관련 배측 경로를 활성화한다는 결과(Goldberg 2014)와 정서 그림 시청이 이후 운동 출력(힘 유지)을 바꾼다는 결과는 있다(WebSearch 요약). null space나 직교 부분공간 개념을 정서 행동 준비에 적용한 연구는 찾지 못했다. 검색: WebSearch("null space orthogonal subspace preparatory activity emotion action readiness premotor fMRI passive viewing emotional videos without movement"), api.crossref.org(Goldberg 2014 서지), 2026-11-12.
* **label-provenance:** felt / 참가자 본인(Spacetop alignvideo 사후 평정). **evidence-level:** R0. **signal-feasibility:** 전운동, SMA의 tSNR 점검 필요. **G1:** 불필요(평정과 fMRI).

---

## BI-R4-2. 정서의 groove: 영화 사운드트랙은 범주보다 행동 경향을 운반하는가

* **조합한 Axis:** M Multimodal Integration(Model & Method) + V Action Readiness & Affordance(Construct) + E Neural Targets(Neural: SMA, 기저핵) + 외부 분야: 음악 인지의 groove 연구, I(오디오 표상 모델). **미논의 쌍 M+V**를 포함한다.
* **연결의 논리:** groove 연구는 "음악이 움직이고 싶게 만드는" 성질을 박 현저성과 중간 수준 syncopation으로 설명하고, 이 감각이 운동망과 보상망을 함께 쓴다고 보고했다(Janata et al. 2012, doi:10.1037/a0024208; Matthews et al. 2020, doi:10.1016/j.neuroimage.2020.116768). 영화 사운드트랙은 장면의 행동 긴장(추격, 대치, 정지)을 박과 음량 변화로 만든다. 그런데 정서 영화 연구는 소리를 "정서 범주의 추가 단서"로만 다뤄 왔다(multimodal-dynamics Round 1 Chain 3, Lettieri et al. 2024 doi:10.1126/sciadv.adk6840). 소리가 정서 범주가 아니라 행동 경향(Axis V)을 주로 운반한다는 가설은 두 분야를 이어야 생긴다.
* **연구 질문:** 영화 사운드트랙의 감각운동 특성(박 현저성, syncopation, 음량 상승 기울기)은 이산 정서 평정보다 행동 경향 평정(Move, Tackle, Stop 등)을 더 고유하게 설명하며, 그 결합은 SMA와 기저핵 반응에서 나타나는가?
* **측정 가능한 예측:**
  1. 평정 수준: Emo-FilM 1 Hz consensus에서 음향 groove 특성이 Motivation 10항목에 대해 갖는 고유 설명 분산(시각 운동, 대사 의미 통제 후)이 discrete 13항목에 대한 고유 설명 분산보다 크다. 특히 Move와 Tackle에서 크다.
  2. 신경 수준: SMA, putamen 반응에서 groove 특성과 Motivation 시계열의 상호작용(같은 groove라도 행동 경향 평정이 높은 구간에서 결합이 큼)이 discrete 정서 시계열과의 상호작용보다 크다.
  3. 대조: 무음 Horikawa에서는 같은 영역의 정서 관련 반응이 시각 운동 feature에만 의존해야 한다(탐색적, 데이터셋 차이 큼).
* **반증 조건:** groove 특성의 고유 설명량이 Motivation과 discrete 항목에서 같거나 discrete 쪽이 크면 "소리는 행동 경향을 우선 운반한다"는 가설은 기각된다. SMA, 기저핵 결합이 음악 음량 같은 저수준 각성 신호만으로 설명되면(음량 통제 후 소멸) groove가 아니라 각성 경로다.
* **교란과 한계:** 음악은 정서적 장면에 몰려 영화 수준 교란이 크다(leave-one-film-out, 영화 확률효과). 혼합 음향에서 음악 성분을 분리해야 groove 특성이 대사와 효과음에 오염되지 않는다(음원 분리 도구는 이번에 확인하지 않음). Motivation 항목의 평정자 일치가 낮다(항목별 0.21~0.60, Stage 1)는 점이 설명 분산의 상한을 낮춘다. 평정은 별도 평정자 규범이고 fMRI 참가자 것이 아니다.
* **데이터셋:** Emo-FilM(주: 소리 있음, Motivation 1 Hz, 30명), Spacetop alignvideo(소리 있음, 영상 단위 본인 평정으로 신경 결합만 재현), Horikawa 2020과 Mind captioning(무음 대조).
* **근거 논문:** doi:10.1037/a0024208, doi:10.1016/j.neuroimage.2020.116768, doi:10.1126/sciadv.adk6840, doi:10.1037/emo0001619(이산 정서와 component의 공선성), doi:10.1093/cercor/bhad093
* **선행 수행 여부:** **no(이 검색 경로 안에서).** groove의 운동, 보상망 관여는 실험실 리듬으로만 확인되었고, 영화 사운드트랙이나 자연주의 영화 음향에 groove를 적용하거나 행동 경향 평정과 연결한 연구는 찾지 못했다. 검색: WebSearch("music groove sensorimotor features film soundtrack action tendency emotion fMRI premotor SMA naturalistic movie sound drives urge to move"), 2026-11-12. multimodal-dynamics Round 1 Chain 3의 선행 기록(음원 분리와 정서 항목별 모달리티 의존성 미발견)과도 일치한다.
* **label-provenance:** felt / 별도 평정자 규범(Emo-FilM Motivation, discrete). 음향 feature는 계산된 자극 기술자. **evidence-level:** R0. **G1:** 필요(보유).

---

## BI-R4-3. 행동을 추론하도록 학습한 모델이 정서의 행동 성분을 더 잘 설명하는가

* **조합한 Axis:** J Learning Objectives(Model & Method) + V Action Readiness & Affordance(Construct) + H Encoding(Model & Method) + E Neural Targets(Neural) + S Generalization & Robustness(Inference). I(AI 모델 계열)를 함께 쓴다. **미논의 쌍 J+V와 S+V**를 포함한다.
* **연결의 논리:** NeuroAI의 핵심 방법은 구조를 고정하고 학습 목표만 바꿔 뇌 정렬이 어떻게 변하는지 보는 것이다(Yamins & DiCarlo 2016, doi:10.1038/nn.4244). 장면 affordance는 물체 분류 목표의 모델에 잘 정렬되지 않았다(Bartnik et al. 2025, doi:10.1073/pnas.2414005122, Discussion 6~7째 단락). V-JEPA 2는 같은 encoder 위에 행동 없는 예측기와, 로봇 영상으로 사후 학습한 행동 조건 예측기(V-JEPA 2-AC)를 함께 갖는다(arXiv:2506.09985, 초록에서 확인). 즉 encoder를 고정한 채 "행동을 넣어 미래를 예측하는 목표"의 효과를 볼 수 있는 드문 쌍이다. 정서의 행동 성분에 이 비교를 쓴 적은 없다.
* **연구 질문:** 같은 영상 encoder에서 행동 조건 예측 목표(V-JEPA 2-AC 예측기, latent action)를 쓴 표상은 행동 없는 예측 목표 표상보다 정서 영상 중 행동 경향 관련 뇌 분산(전운동, 두정, transmodal)을 더 고유하게 설명하며, 그 이득은 데이터셋을 넘어 일반화되는가?
* **측정 가능한 예측:**
  1. Emo-FilM에서 banded ridge: band A = 공유 encoder 표상, band B = 행동 없는 예측기 상태, band C = 행동 조건 예측기 상태(가능하지 않으면 LAPA latent action, arXiv:2410.11758). 예측: band C의 고유 분산이 band B보다 크고, 그 차이는 Motivation 시계열과 결합한 voxel에 집중된다.
  2. 특이성: 시각 피질과 장면 영역(PPA, OPA)에서는 band B와 C의 차이가 작다.
  3. 일반화(S+V): Emo-FilM에서 학습한 band C 기반 encoder를 Horikawa와 Mind captioning에 라벨 없이 적용했을 때, 접근/회피 관련 범주 클립에서 예측 이득이 유지된다(라벨 정의가 데이터셋마다 달라도 자극 계산 feature는 공통이므로).
* **반증 조건:** band C가 band B보다 낫지 않거나, 이득이 모든 영역에 고르게 나타나면(일반 용량 차이) "행동 추론 목표가 정서의 행동 성분을 포착한다"는 가설은 지지되지 않는다. 데이터셋 간 일반화가 사라지면 이득은 Emo-FilM 영화 특이적이다.
* **교란과 한계:** V-JEPA 2-AC는 로봇 조작 영상(Droid)으로 사후 학습되어 영화의 인물 행동과 도메인이 다르다. 공개 체크포인트에 예측기 가중치가 포함되는지 미확인이다(frontier-ai Round 1 기록). 예측기 상태의 차원과 파라미터 수를 맞춘 matched-complexity null(같은 차원의 무작위 사상)을 함께 보고한다(adversarial-reviewer 최소 검증 요건). 카메라 운동은 nuisance band로 통제한다.
* **데이터셋:** Emo-FilM(주), Horikawa 2020과 Mind captioning(일반화 검정, 무음), Spacetop alignvideo(일반화 검정, 소리 있음).
* **근거 논문:** doi:10.1038/nn.4244, arXiv:2506.09985, arXiv:2410.11758, doi:10.1073/pnas.2414005122, arXiv:2305.11772(latent 미래 예측 모형과 고차 피질 정렬), doi:10.1038/s41467-024-53147-y(통제된 모델 비교의 원칙, DB 수록)
* **선행 수행 여부:** **partially.** Oota et al. 2026(arXiv:2605.19352)이 게임 플레이 fMRI에서 VLM과 large-action model 표상의 뇌 정렬을 연구했고(초록), 행동 모형 쪽 이득이 전두-두정과 운동 계획 영역에서 크다고 보고했다(WebSearch 요약). 그러나 상호작용 과제이고, encoder를 고정한 행동 조건 예측기 대 행동 없는 예측기 비교도, 정서의 행동 성분과의 결합도 아니다. 검색: WebSearch("action-conditioned or inverse dynamics video model representations versus observation-only self-supervised models brain alignment fMRI premotor parietal 2025 2026"), export.arxiv.org(arXiv:2605.19352, arXiv:2506.09985 ID 조회), 2026-11-12.
* **label-provenance:** felt / 별도 평정자 규범(Motivation 항목), 모델 표상은 계산된 변수(in-silico 아님, 관찰 fMRI 예측). **evidence-level:** R0. **G1:** 필요(보유).

---

## BI-R4-4. 반복 회상의 우선순위: 정서 클립 재활성은 각성이 아니라 '이득'을 따르는가

* **조합한 Axis:** N Brain-like Computation(Model & Method: 강화학습의 우선순위 재생) + W Internally Generated Experience(Construct) + Q Reliability & Measurement(Inference: 반복 회상 간 재활성 일관성) + E Neural Targets(Neural: hippocampus, 감각 피질). 외부 분야: 강화학습의 prioritized replay. **미논의 쌍 N+W**를 포함한다.
* **연결의 논리:** RL 이론은 어떤 기억을 다시 꺼낼지를 need(곧 쓸 가능성)와 gain(꺼냈을 때 가치 추정이 바뀌는 정도)의 곱으로 정한다(Mattar & Daw 2018, doi:10.1038/s41593-018-0232-z). 인간 fMRI에서도 휴지기 재생이 약하게 학습된 항목을 우선한다(Schapiro et al. 2018, doi:10.1038/s41467-018-06213-1). 놀라운 보상(부호 없는 예측오차)은 기억을 따로 강화한다(Rouhani et al. 2018, doi:10.1037/xlm0000518). 정서 기억 연구는 재활성의 우선순위를 주로 각성(arousal)으로 설명해 왔다(de Voogd et al. 2016, doi:10.1016/j.neuroimage.2016.04.026, 제목 수준). 두 설명은 다른 예측을 낸다: 각성 설명은 강한 정서 클립을, gain 설명은 "기대를 많이 바꾼" 클립을 우선한다.
* **연구 질문:** Mind captioning의 반복 회상에서 클립별 정서 재활성 강도는 규범 각성보다 gain 대리 변수(부호 없는 예측오차, 가치 변화 크기)로 더 잘 예측되는가?
* **측정 가능한 예측:**
  1. 재활성 강도: Horikawa 2020 + Mind captioning 지각 데이터로 학습한 encoder/decoder를 회상 시행에 적용해 클립별, 회차별 지각-회상 유사도를 계산한다.
  2. 예측 변수: (a) 각성: C&K 14차원 중 Arousal, (b) gain 대리: Surprise 범주 평정, Upswing의 중립점 이탈 크기, video world model의 클립 내 latent 예측오차(모델 계산), (c) 통제: vividness(참가자 본인), 클립 길이, 시각 기억성(측정 방법은 이번에 확인하지 않음).
  3. 예측: (b)가 (a)를 통제한 뒤에도 재활성 강도를 고유하게 예측한다. 회차가 진행될수록 (b)가 높은 클립의 재활성은 유지되고 낮은 클립은 감소한다.
* **반증 조건:** 각성만으로 재활성 강도가 포화되고 gain 대리가 고유 분산을 더하지 못하면 RL 우선순위 설명은 이 데이터에서 지지되지 않는다. gain 대리 세 개가 서로 다른 방향을 내면 "gain"을 이 데이터에서 조작적으로 정의할 수 없다는 결론이다(그 자체가 보고 가치).
* **교란과 한계:** 회상은 텍스트 cue로 시작되어 의미 정보가 섞인다. Mind captioning 설계상 회상 직후 실제 비디오가 다시 제시되므로(vision-decoding Round 1 0.1절) 매 회차가 재부호화를 포함한다. 따라서 "회차별 감쇠" 예측은 약하고, 1차 결과는 회차 평균 재활성으로 둔다. 클립은 72개, 피험자 6명이라 클립 수준 회귀의 자유도가 작다(사전등록과 계층 모형). 정서 라벨은 참가자 본인 보고가 아니다. 두 Horikawa 코호트의 피험자 중복 여부는 미확인이다.
* **데이터셋:** Mind captioning(주: 72클립 x 5회 회상, vividness), Horikawa 2020(지각 decoder 학습 보강).
* **근거 논문:** doi:10.1038/s41593-018-0232-z, doi:10.1038/s41467-018-06213-1, doi:10.1037/xlm0000518, doi:10.1016/j.neuroimage.2016.04.026, doi:10.1126/sciadv.adw1464
* **선행 수행 여부:** **no(이 검색 경로 안에서).** 우선순위 재생 이론을 정서 기억에, 또는 gain 대 각성 대비를 자연주의 클립의 반복 회상에 적용한 연구는 찾지 못했다. 인접 선행은 비정서 물체의 휴지기 재생 우선순위(Schapiro 2018)와 정서 기억의 깨어 있는 재활성(de Voogd 2016)이다. 검색: WebSearch("prioritized replay gain need theory predicts emotional memory recall reactivation fMRI surprise versus arousal video clips repeated recall"), api.crossref.org(인접 선행 서지), 2026-11-12.
* **label-provenance:** felt / 별도 평정자 규범(C&K 범주와 차원), vividness는 참가자 본인, world model 예측오차는 모델 계산 변수. **evidence-level:** R0. **G1:** 모델 기반 gain 대리에만 필요(보유).

---

## 5. 검토했으나 기각하거나 흡수한 쌍

| 쌍 | 판정 | 이유 |
|---|---|---|
| **O+V** | 기각 | Emo-FilM 참가자에게 BIS/BAS 질문지가 있어(`dataset_EmoFilM.md` 질문지 항목) "접근/회피 성향이 행동 경향 신경 민감도를 예측하는가"는 자연스러운 연결이다. 그러나 30명에서 피험자 간 상관은 80% 검정력으로 약 r = 0.49 이상만 검출할 수 있고, 뇌-형질 연관은 대개 이보다 훨씬 작다(Marek et al. 2022, doi:10.1038/s41586-022-04492-9, DB 수록). 피험자 내 형태로 바꾸면 O가 빠지고 BI-P2와 같아진다. 데이터 규모 때문에 질문으로 성립하지 않는다 |
| **P+V** | 기각 | 데이터 안의 실제 개입은 Spacetop social의 기만 cue뿐인데 행동 경향 측정이 없다. 편집 기반 인과 검정은 L+V(GC-P8)로 이미 논의되었다. 새 연결이 생기지 않는다 |
| **F+V** | 흡수 | 단독으로는 "V의 뇌 표상 형식"이라 BI-P2(V, A, I, B, C, R)와 BI-R4-1(K+V+E의 부분공간 형식)에 이미 포함된다 |
| **Q+V** | 흡수 | Motivation 항목의 낮은 평정자 일치(0.21~0.60)는 중요하지만 독립 질문이 아니라 BI-R4-2와 BI-P2의 설명 분산 상한을 정하는 게이트다. 각 제안의 한계에 넣었다 |
| **T+V** | 기각 | V의 평가와 benchmark는 minimum-validation 필수 태그로 다뤄지며, 이를 넘어서는 별도 과학 질문을 만들지 못했다 |
| **S+V** | 포함 | BI-R4-3의 일반화 검정(자극 계산 affordance feature가 데이터셋 간 라벨 비호환을 우회하는가)에 넣었다 |
| **J+V** | 포함 | BI-R4-3 |
| **K+V** | 포함 | BI-R4-1 |
| **M+V** | 포함 | BI-R4-2 |
| **N+W** | 포함 | BI-R4-4. 다른 형태(회상 중 successor 상태 재활성)도 검토했으나 Mind captioning 클립이 서로 독립이고 길이가 짧아(Cowen & Keltner 클립 평균 약 5 s, Stage 1 Horikawa 기준) 전이 구조가 없으므로 기각했다 |

## 6. 이번 라운드에서 literature.jsonl에 추가한 항목 (11편, 모두 식별자 경로 확인)

doi:10.1038/nn.3643, doi:10.1038/ncomms13239, doi:10.1037/a0024208, doi:10.1016/j.neuroimage.2020.116768, doi:10.1038/s41593-018-0232-z, doi:10.1037/xlm0000518, doi:10.1038/nn.4244, doi:10.1016/j.neuroimage.2013.08.032, doi:10.1038/s41467-018-06213-1, doi:10.1016/j.neuroimage.2016.04.026, arXiv:2605.19352. 이 중 본문을 읽은 것은 없다. 초록 또는 WebSearch 요약 수준이며 각 항목의 `discussion_read`에 표시했다.
