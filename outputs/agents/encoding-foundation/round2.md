# Round 2 (Cross-Agent Exchange): encoding-foundation

* 작성: encoding-foundation (Axis F, H, S 담당)
* 기준일: 2026-11-12
* 절차: `reference/protocols.md` P2와 Coordinator 위임 메시지의 추가 요구
* 읽은 파일: 다른 10개 에이전트의 `round1.md`(0, 1, 3, 4, 6절 중심, 필요한 곳은 2, 5, 7절), `outputs/axis_encyclopedia.md`(0절, 2절, 3절), `outputs/STAGE_STATUS.md` 사용자 결정 기록, `outputs/literature/literature_db.csv`(인용 ID 대조)
* 인용 원칙: 아래 인용 ID는 모두 `literature_db.csv`의 verified 항목이거나, 이번에 식별자 경로로 새로 확인해 `literature.jsonl`에 추가한 것이다. 검색 색인으로만 본 것은 `[search_index]`로 표시했다.
* 검색 경로(신규성 점검): arxiv.org/search 웹 검색, export.arxiv.org API(작업 중 429로 중단되어 웹 검색으로 대체), WebSearch, `literature_db.csv`. neurips.cc는 이 환경에서 해석되지 않아 열지 못했다(우회하지 않음).

---

## 0. 요약

1. **Round 1 판정 정정.** Round 1의 chain 1("같은 자극에서 in-silico 정서 기하 vs 관찰")은 already_done을 "no"로 적었다. 그런데 이번 검색에서 NeurIPS 2026 논문 "Evaluating TRIBE v2 Beyond Its Original Benchmarks: From Functional Localizers to Naturalistic Emotion" `[search_index]`을 찾았다. 검색 요약에 따르면 이 논문은 연속 정서 주석이 있는 자연 영화에서 TRIBE v2를 평가했고, 정서 범주에 따라 모델-뇌 일치가 크게 달라 일부 정서 조건에서 실패했다고 보고했다. 따라서 판정을 **partially**로 바꾼다. 데이터셋 이름, RSA와 ceiling 사용 여부는 본문을 열지 못해 미확인이다. `literature.jsonl`의 해당 항목도 고쳤다.
2. **Mind captioning(ds005191)의 contamination 점검:** Round 1에서 사전학습 목록을 확인한 fMRI foundation model 10종(TRIBE v2, CortexMAE, NeuroSTORM, SwiFT, Brain-JEPA, BrainLM, Omni-fMRI, BrainHarmonix, Brain-Semantoks, Thomas 2022 OpenNeuro 34개) 어디에도 ds005191은 없다. Thomas 2022의 목록은 ds003524까지다. arxiv.org 검색에서 "ds005191", "mind captioning"으로 잡히는 사전학습 논문도 없었다. 다만 두 가지는 남는다. (a) EmoMind(arXiv:2605.16739)는 이 데이터를 **지도학습**에 썼다. (b) EmoNet 누수는 같은 Cowen & Keltner 비디오를 쓰므로 Mind captioning에도 똑같이 적용된다.
3. **Mind captioning이 F, H, S 축에 주는 것은 셋이다.** 72개 클립 5회 반복이 있어 **반복 기반 noise ceiling 아래에서 in-silico 예측과 관찰 반응을 비교**할 수 있다. 같은 2,180개 클립을 본 독립 코호트라 **교차 코호트 일반화**(Horikawa 2020 5명과 합쳐 11명)가 가능하다. 회상 imagery가 있어 **자극 계산 가능 성분과 잔차 성분 중 무엇이 회상에서 재활성되는가**를 물을 수 있다. 두 코호트의 피험자 중복 여부는 미확인이며 subject-level leakage 위험 요인이다.
4. 다른 에이전트 5곳이 내 Round 1 chain과 독립적으로 수렴했다. generative-counterfactual CH3와 CH5, emotion-theory C4와 C8, llm-semantics Chain 5, geometry-info C4, systems-neuro Chain 7, multimodal-dynamics X3, adversarial-reviewer D6이다. 그래서 제안 7개 중 4개는 이 겹침을 하나의 공동 설계로 합치는 제안이다.

---

## 1. 가져온 아이디어

### IM-1. Encoder trust map: in-silico 개입 결과의 영역별 신뢰 한계
* **출처:** generative-counterfactual. Gu et al. 2023(doi:10.1038/s42003-023-05440-7)은 생성 자극의 실제 조절 효과 크기가 encoder 정확도에 비례한다고 보고했다(Discussion 1단락, generative-counterfactual round1 U2 인용). NeuroVolve(arXiv:2512.00557)는 amygdala에서 생성 이미지가 자연 이미지 최상위보다 반응을 더 올리지 못했다. 함께 쓸 결론 수준 사다리(R0~R4)도 이 에이전트의 제안이다.
* **내 축에 들여오는 방식:** TRIBE v2는 피질하 점수가 피질의 1/2~1/3이고 Limbic망에서 개선이 가장 작다(arXiv:2605.04326, arXiv:2605.29850). 그렇다면 in-silico 정서 개입(R1)의 신뢰도도 영역마다 다를 것이다. Mind captioning의 반복 기반 ceiling으로 정규화한 parcel별 예측 정확도와 정서 기하 충실도를 계산해 'trust map'을 만든다. R1 결과는 trust map 임계 이상인 parcel에서만 보고하도록 규칙화한다. 이것이 EF-P1의 핵심 산출물이다.

### IM-2. Rank-resolved fidelity: 공유 스펙트럼 위에서 in-silico 예측 평가
* **출처:** geometry-info와 emotion-theory. Gauthaman et al. cross-decomposition(arXiv:2409.06843)은 반복 없이 피험자 쌍으로 rank별 신뢰 공유 분산을 준다. Han & Bonner 2025(arXiv:2505.12653)는 개인 특이 신경 패턴이 많은 latent 차원에 걸쳐 있다고 보고했다.
* **내 축에 들여오는 방식:** TRIBE v2의 unseen-subject 예측은 정의상 '평균 피험자' 반응이다. 따라서 관찰 피험자들의 공유 스펙트럼 중 저rank 고분산 대역만 따라가고 고rank 대역에서 떨어질 것으로 예상한다. 관찰-관찰 공유 스펙트럼과 관찰-in-silico 공유 스펙트럼을 rank별로 겹쳐 보면, "in-silico가 어디까지 재현하는가"를 voxel r 하나가 아니라 **rank 대역별로** 말할 수 있다. 이어서 정서 평정이 설명하는 대역이 in-silico가 끊기는 대역과 겹치는지 본다. Horikawa 2020 5명과 Mind captioning 6명이 같은 자극을 봤으므로 피험자 쌍이 늘어난다(코호트 내 쌍과 코호트 간 쌍을 구분해 보고).

### IM-3. 잔차 분석의 측정 오차 함정과 자극 표집 효과
* **출처:** adversarial-reviewer. Westfall & Yarkoni 2016(doi:10.1371/journal.pone.0152719)에 따르면 공변량을 불완전하게 측정하면 증분 타당도 위양성이 생기고, 표본이 커질수록 위양성이 늘어난다. vision-decoding도 근거를 보탰다. Shirakawa et al. 2025(doi:10.1016/j.neunet.2025.107515)는 군집된 학습 자료가 output dimension collapse를 만든다고 보였다.
* **내 축에 들여오는 방식:** Round 1의 "관찰 - foundation 예측 잔차" 설계(Residual Encoding)는 TRIBE 예측을 불완전한 공변량으로 쓴다. 따라서 "잔차가 정서 평정을 설명한다"는 결과는 TRIBE의 예측 오차(측정 오차) 때문에 위양성일 수 있다. 대응은 두 가지다. (a) TRIBE 예측, V-JEPA2 원 feature, 캡션 embedding을 함께 잠재 구성개념으로 묶고 신뢰도를 반영한 분할을 쓴다. (b) 잔차 분석의 null을 "TRIBE 예측에 같은 크기의 잡음을 더한 공변량" 시뮬레이션으로 만든다. 또 Cowen & Keltner 자극은 범주 군집 표본이라 in-silico RSA도 범주처럼 보일 수 있다. 그래서 RSA 비교에는 범주 무작위 재표집 null을 둔다.

### IM-4. Limbic 잔차의 자율신경-혈관 성분
* **출처:** systems-neuro. Bolt et al. 2025(doi:10.1038/s41593-025-01945-y)는 전역 fMRI 신호가 교감 각성과 결합해 저주파 분산의 약 25%를 차지한다고 보였다. Dense Amygdala(doi:10.1038/s41597-026-07065-x)는 amygdala 최적화 획득에서도 피질하 tSNR이 낮고 dropout 개인차가 크다고 보고했다.
* **내 축에 들여오는 방식:** TRIBE v2에는 생리 입력이 없다. 그래서 관찰 반응에서 TRIBE 예측을 빼면 생리 동기화 성분이 잔차에 몰린다. Round 1 chain 2의 "limbic 맹점 분해"는 생리 회귀 전후를 모두 보고해야 한다. 각 피질하 ROI의 tSNR과 dropout 마스크(signal-feasibility 태그)를 선행 조건으로 둔다.

### IM-5. 예측 모델의 predictor 오차는 encoder feature와 다른 정보다
* **출처:** frontier-ai. V-JEPA 2의 latent 예측오차(surprise)는 직관 물리 위반을 탐지한다(arXiv:2502.11831, arXiv:2506.09985).
* **내 축에 들여오는 방식:** TRIBE v2는 V-JEPA2-Giant의 **encoder** 중간층 embedding을 patch 평균해 입력으로 쓴다(arXiv:2605.04326 5.2절). predictor의 예측오차는 입력에 들어가지 않는다. 따라서 surprise는 "TRIBE 예측 너머"를 검정할 수 있는, 구조적으로 분리된 후보 feature다(EF-P5).

---

## 2. 보내는 제안

표기: **label-provenance**(대상 portrayed / perceived / felt, 주체 본인 / peer / 규범 / AI), **evidence-level**(R0~R4), **insilico-vs-observed**(관찰 / in-silico / 혼합). "신규성 점검"에는 실제 검색 경로와 결과를 적었다.

### EF-P1. 같은 자극에서의 surrogate 충실도 감사를 모든 in-silico 정서 결과의 관문(gate)으로
* **받는 에이전트:** generative-counterfactual (참조: vision-decoding)
* **제안 내용:** 너희 쪽 CH3("같은 자극에서 surrogate 뇌는 정서 구조를 얼마나 잃는가")를 우리 쪽 **parcel별 trust map**으로 확장할 수 있다. trust map은 Mind captioning 반복 ceiling으로 정규화한 점별 정확도, 정서 RDM 관계 충실도, rank 대역별 충실도로 만든다. 그러면 너희 쪽 CH1, CH2, CH4, CH6, CH7의 R1 편집 결과를 어느 영역에서 믿을 수 있는지 사전에 정할 수 있다. 구체적인 설계는 다음과 같다.
  1. TRIBE v2(영상만 입력, 무음)로 Horikawa 2,181개와 Mind captioning 72개 반복 클립의 run 순서 시퀀스를 예측한다. 그 예측에 관찰 데이터와 같은 블록 평균을 적용한다.
  2. 관찰 반응은 Horikawa 2020 5명과 Mind captioning 6명을 쓴다. ceiling은 Mind captioning 5회 반복으로 구한다.
  3. 영역별로 (a) 반응 상관, (b) 34범주와 14차원 규범 RDM에 대한 관계 충실도(관찰 RSA 대비 in-silico RSA), (c) 시각-의미 RDM(V-JEPA2, 중립 인간 캡션)을 partial로 뺀 정서 고유 RSA를 계산한다.
  4. Emo-FilM 14편으로 시청각 조건을 재현한다(ceiling은 피험자 간).
* **관련 Axis:** F, H, S, L, T
* **근거 논문:** arXiv:2605.04326, arXiv:2605.16739, doi:10.1038/s42003-023-05440-7, arXiv:2512.00557, doi:10.1126/sciadv.adw1464, arXiv:2409.06843
* **가능한 데이터셋:** Horikawa 2020, Mind captioning(반복 ceiling), Emo-FilM
* **label-provenance:** RDM 라벨은 felt(별도 평정자 1인칭 보고), 주체는 규범 / **evidence-level:** 감사 자체는 R0이고, R1 결과를 거르는 관문 역할 / **insilico-vs-observed:** 혼합
* **신규성 점검:** arxiv.org에서 "TRIBE v2"를 검색한 결과 7편(arXiv:2610.13558, 2609.15685, 2607.16292, 2606.06345, 2605.13904, 2605.04326, 2604.04025)이 나왔고, 정서 영화를 관찰 fMRI와 짝지은 평가는 없었다. WebSearch에서는 NeurIPS 2026 "Evaluating TRIBE v2 Beyond Its Original Benchmarks" `[search_index]`가 정서 영화 평가를 했다. 따라서 **already_done: partially**다. 차별점은 반복 기반 ceiling, 관계 기하와 rank 대역 충실도, 라벨 출처 구분, 그리고 결과를 R1 관문 규칙으로 쓰는 것이다.
* **예상되는 반론과 대응:**
  * TRIBE v2는 긴 연속 영화로 학습했다. 2~10 s 클립을 이어 붙인 시퀀스는 분포 밖이라 충실도가 과소평가될 수 있다. 대응: 학습 데이터 Wen2017도 클립을 이어 붙인 무음 영상이다. 클립 단위 예측과 시퀀스 단위 예측을 둘 다 보고한다.
  * 공개 checkpoint는 피질만 출력하므로 편도체 trust 값은 비어 있다. 대응: 피질하는 "판정 불가"로 표시한다. 피질하 head를 직접 학습하는 것은 별도 단계로 둔다(제3자 피질하 head `[search_index]`는 쓰지 않는다).
  * 감사는 상관이라 R1 개입의 타당성을 직접 보증하지 못한다. 대응: 맞다. 관문은 "필요조건"으로만 쓴다.

### EF-P2. 회상에서 재활성되는 것은 자극으로 계산 가능한 성분인가, 잔차 성분인가
* **받는 에이전트:** vision-decoding (Axis W, 너희 R2와 U4)
* **제안 내용:** 너희 쪽 R2("같은 정서 클립의 회상에서 정서 재활성")를 우리 쪽 **in-silico 분해**로 날카롭게 만들 수 있다.
  1. Mind captioning 지각 반응(72클립 x 5회)을 두 성분으로 나눈다. 하나는 TRIBE v2 예측 성분이다. 2,180개 학습 클립으로 피험자 head를 fine-tune한 판과 unseen-subject 판을 둘 다 쓴다. 다른 하나는 반복 간 신뢰할 만한 잔차 성분이다.
  2. 각 회상 시행의 패턴이 영역별로 어느 성분과 더 정렬하는지 본다.
  3. 회상 cue는 텍스트다. cue 구간의 언어 반응은 TRIBE v2 텍스트 전용 입력으로 in-silico 예측해 nuisance로 뺄 수 있다.
  
  예측은 이렇다. 시각피질에서는 예측 성분이 재활성되고, vmPFC와 섬엽에서는 잔차 성분(평가, 내수용 등 자극으로 계산되지 않는 정보)이 재활성된다. 잔차 재활성이 규범 valence가 부정인 클립과 높은 vividness에서 크면, 너희 쪽 NEVER 가설과 연결된다.
* **관련 Axis:** W, F, H, G, O
* **근거 논문:** doi:10.1126/sciadv.adw1464, arXiv:2605.04326, arXiv:2505.12653, arXiv:2506.06898, arXiv:2605.17198
* **가능한 데이터셋:** Mind captioning(지각 반복, 회상, vividness). 보조로 Horikawa 2020(같은 클립 1회 지각, 예측 성분 학습)
* **label-provenance:** 정서는 felt(규범), vividness는 참가자 본인 보고 / **evidence-level:** R0 / **insilico-vs-observed:** 혼합(분해 기준은 in-silico, 재활성은 관찰)
* **신규성 점검:** WebSearch("encoding model predicted component vs idiosyncratic residual reinstated during recall")에서 가장 가까운 것은 두 가지였다. 하나는 영화 시청으로 학습한 encoding model을 회상에 적용한 Durham 연구 `[search_index]`(STS 사회 상호작용, 정서 아님), 다른 하나는 arXiv:2505.12653(개인 특이 고차원 성분이 회상 행동 차이를 예측)이다. foundation encoder 예측으로 지각 반응을 나눈 뒤 회상 정렬을 본 연구는 찾지 못했다. 따라서 **already_done: partially**다.
* **예상되는 반론과 대응:**
  * 잔차에는 측정 잡음이 섞인다. 대응: 5회 반복의 split-half로 잔차 신뢰도를 추정하고, 신뢰 가능한 부분공간으로 제한한다(IM-3).
  * TRIBE v2는 지각 반응을 예측할 뿐 회상을 예측하지 못한다. 대응: 회상을 예측하려는 것이 아니다. 지각 반응의 분해 기준으로만 쓴다.
  * 두 코호트 피험자가 겹치면 head fine-tuning에서 누수가 생긴다. 대응: Mind captioning 내부 학습 클립만 쓴다.

### EF-P3. "기대 반응"의 네 가지 정의와 그 잔차가 본인 보고 편차를 예측하는가 (공동 설계)
* **받는 에이전트:** emotion-theory (C4, C8). 같은 설계를 제안한 geometry-info(C4), llm-semantics(Chain 5), generative-counterfactual(CH5), vision-decoding(R5)에 참조
* **제안 내용:** 다섯 에이전트가 같은 질문을 서로 다른 '기대 반응'으로 제안했다. 너희 쪽 C4, C8을 우리 쪽 **네 기준선 비교**로 통합하면, 질문 자체에서 새 분해가 나온다. Spacetop alignvideo(약 100명, 같은 영상, 같은 순서, 본인 7차원 평정)에서 기대 반응을 다음 넷으로 정의한다.
  * (a) TRIBE v2 zero-shot 예측: 자극으로 계산 가능하고 Spacetop을 본 적 없는 반응
  * (b) leave-one-subject-out peer 평균: 경험적 공유 반응
  * (c) hyperalignment 또는 SRM 공유 성분
  * (d) 평정 쪽 기대값: MLLM 평균 관찰자 추정과 peer 평정 평균
  
  각 잔차가 본인 평정 편차(본인 - peer 평균)를 보류 영상에서 예측하는지 본다. 핵심은 **(b) - (a)**, 즉 "공유되지만 자극으로 계산되지 않는 성분"이다. 이 성분이 평정 편차가 아니라 평정 평균을 설명한다면, 사람들이 공유하는 정서 반응 중 영상 feature로 환원되지 않는 부분(예: 공유된 서사 평가)이 있다는 증거가 된다.
* **관련 Axis:** O, F, H, U, Q
* **근거 논문:** doi:10.1126/sciadv.abf7129, doi:10.7554/eLife.56601, arXiv:2605.04326, arXiv:2607.01400, arXiv:2408.13718, arXiv:2505.12653
* **가능한 데이터셋:** Spacetop(주). Emo-FilM은 참가자 사후 클립 평정이 부분적이라 보조로만 쓴다
* **label-provenance:** felt / 참가자 본인, peer 합의, AI 추정을 모두 따로 둔다 / **evidence-level:** R0 / **insilico-vs-observed:** 혼합
* **신규성 점검:** WebSearch("deviation from group-average encoding model prediction predicts individual self-reported emotion")에서 가장 가까운 것은 두 가지였다. 하나는 ISC 편차와 우울 증상을 연결한 bioRxiv 연구 `[search_index]`(정서 평정 아님, encoding 기준선 아님)이고, 다른 하나는 Chang 2021(HMM, 별도 표본 평정)이다. **already_done: partially**다. (a)와 (b)를 대조하는 분해는 찾지 못했다.
* **예상되는 반론과 대응:**
  * Spacetop은 TR 0.46 s에 3T이고, TRIBE 학습 데이터와 획득 조건이 다르다. 대응: TRIBE v2는 1 Hz 대상으로 재표본하므로 입력은 맞출 수 있다. 다만 scanner 차이로 생기는 (a) 잔차의 체계적 성분은 (b)와 비교해서 걸러낸다.
  * alignvideo 평정 결측이 약 51%다. 대응: 결측 기제(클릭해야 저장)를 확인한 뒤 결측 모형을 쓴다.
  * 평정 구간이 영상 끝 HRF와 겹친다. 대응: 평정 전 TR만 쓴다.
  * 공개 TRIBE는 피질만 낸다. 대응: vmPFC는 피질이므로 핵심 영역은 포함된다.

### EF-P4. 뇌 입력 foundation model의 정서 latent: 누수 통제와 coverage 대조를 갖춘 공동 benchmark
* **받는 에이전트:** systems-neuro (Chain 7) (참조: adversarial-reviewer D7)
* **제안 내용:** 너희 쪽 Chain 7(Brain-JEPA latent의 정서 정보와 피질하 의존도)을 우리 쪽 benchmark 틀과 합칠 수 있다. 우리 쪽 틀은 Round 1 chain 5, Omni-fMRI 누수 사례, CortexMAE flat map에서 왔다. 구성은 다음과 같다.
  * (i) 분할: leave-one-film-out과 leave-subject-out을 쓰고, 시간 블록 사이에 HRF와 자기상관 길이 이상의 buffer를 둔다.
  * (ii) coverage 대조: CortexMAE-F(피질만, Spacetop fsLR 91k에 바로 입력), CortexMAE-P + Tian, Brain-JEPA(Tian 피질하 token masking ablation), NeuroSTORM(volume)을 비교한다.
  * (iii) 기준선: FC, 원시 parcel 시계열, TRIBE v2 자극 예측
  * (iv) 라벨 head 분리: Spacetop 본인 평정과 Emo-FilM 규범 평정을 따로 둔다.
  * (v) 피질하 ROI별 tSNR과 dropout 보고
  
  너희 쪽 "피질하 token 제거 민감도"는 coverage 대조에서 가장 깨끗하게 검정된다.
* **관련 Axis:** F, S, E, T, U
* **근거 논문:** arXiv:2510.13768, arXiv:2409.19407, arXiv:2506.11167, arXiv:2601.23090, doi:10.1371/journal.pcbi.1012994, doi:10.1038/s41597-026-07065-x
* **가능한 데이터셋:** Spacetop(fsLR CIFTI, 본인 평정), Emo-FilM(raw 재전처리, 1 Hz 규범), Mind captioning(정서 라벨은 규범 34+14, 반복 클립으로 latent 신뢰도 점검)
* **label-provenance:** felt / 본인(Spacetop)과 규범(Emo-FilM, Mind captioning)을 분리 / **evidence-level:** R0 / **insilico-vs-observed:** 관찰(기준선 하나만 in-silico)
* **신규성 점검:** Round 1에서 arXiv를 검색했고, systems-neuro Chain 7 검색도 결과가 같았다. Omni-fMRI(arXiv:2601.23090)의 StudyForrest 회귀만 있었고 이것은 무작위 블록 분할이다. **already_done: partially**다.
* **예상되는 반론과 대응:**
  * Brain-JEPA 저장소에 LICENSE가 없다. 대응: 라이선스 확인 전에는 비교 대상에서 빼고 CortexMAE와 NeuroSTORM으로 시작한다.
  * 휴지기 사전학습 latent는 영화 정체성을 쉽게 담아, leave-one-film-out에서도 영화 장르 같은 수준을 맞힐 수 있다. 대응: 영화 수준 평균을 뺀 영화 내 변동 probe를 별도로 보고한다.
  * Emo-FilM 제공본은 6 mm로 smoothing되어 있다. 대응: raw에서 재전처리한다.

### EF-P5. Surprise가 surrogate 너머를 설명하는가: V-JEPA 2 예측오차의 matched-control 검정
* **받는 에이전트:** frontier-ai (T1, CH2)
* **제안 내용:** 너희 쪽 T1(world-model surprise 위계)을 우리 쪽 **matched-control**로 검정할 수 있다. TRIBE v2는 V-JEPA2 encoder embedding을 이미 포함하므로(arXiv:2605.04326 5.2절), TRIBE 예측을 기준선 공변량으로 둔다. 그 위에서 V-JEPA 2 predictor surprise가 다음 둘을 추가로 설명하는지 본다. (a) 편도체, 섬엽, vmPFC 관찰 잔차, (b) Emo-FilM 평정자의 Suddenly, Predictable 평정. 통제로는 TRIBE latent의 시간 미분과 shot-cut 회귀자를 넣어, "변화량"과 "예측 위반"을 구분한다. 같은 논리로 arXiv:2607.16292의 matched-control 절차(예측 피질 vs 그 백본)를 정서 평정 예측에 적용한다.
* **관련 Axis:** H, N, D, I, R
* **근거 논문:** arXiv:2502.11831, arXiv:2506.09985, arXiv:2605.04326, arXiv:2607.16292, doi:10.64898/2026.09.26.754452
* **가능한 데이터셋:** Emo-FilM(주, appraisal 1 Hz), Horikawa와 Mind captioning(surprise 범주 클립), Spacetop
* **label-provenance:** appraisal 평정은 felt / 규범 / **evidence-level:** R0 / **insilico-vs-observed:** 혼합
* **신규성 점검:** WebSearch("V-JEPA surprise prediction error fMRI amygdala emotion movie")에서 V-JEPA surprise를 영화 fMRI 회귀자로 쓴 연구는 찾지 못했다. V-JEPA feature를 encoder 입력으로 쓴 VIBE(arXiv:2507.17958)는 있다. frontier-ai 검색 결과도 같다. **already_done: no (검색 범위 내)**. 단 Stage 2 교훈(25% 과대 판정)에 따라 Round 3에서 다시 확인한다.
* **예상되는 반론과 대응:**
  * surprise는 encoder embedding의 시간 변화로 상당 부분 예측된다. 대응: 시간 미분 통제가 이 반론을 겨냥한다.
  * TRIBE v2의 오디오 embedding은 60 s chunk 안에서 미래 정보를 담는다(arXiv:2605.04326 5.2절). 그래서 시점 분석에서 TRIBE 기준선이 미래를 '아는' 문제가 생긴다. 대응: 오디오를 뺀 TRIBE 판을 대조로 둔다.

### EF-P6. 독립 코호트를 쓴 의사 전향적 검증과 공동 provenance 등록부
* **받는 에이전트:** adversarial-reviewer (D6, D7)
* **제안 내용:** 너희 쪽 D6(정서 모델이 고른 비디오가 새 피험자의 영역을 구동하는가)을 우리 쪽 **Mind captioning 독립 코호트**로 강화할 수 있다.
  1. Horikawa 2020 5명으로 학습한 정서 encoder, 시각-의미 encoder, 그리고 TRIBE v2 zero-shot이 각자 영역별 구동, 억제 클립을 고른다.
  2. 선택은 Mind captioning 반응을 보기 전에 기록한다.
  3. 검증은 Mind captioning 6명의 같은 클립 반응으로 하고, 72개 반복 클립에서는 ceiling 대비로 한다.
  
  D7에는 공동 **provenance 등록부**를 제안한다. 등록부는 모델 x 데이터셋 x 오염 경로 표다. 들어갈 항목은 EmoNet(Cowen & Keltner 프레임, Horikawa와 Mind captioning 모두 해당), TRIBE v2 학습 목록과 코드의 `Allen2022Bold` 분기, V-JEPA 2 사전학습 영상(미확인), BOLD Moments와 Memento10k 출처 중복, NSD로 학습한 decoder와 encoder, 두 Horikawa 코호트의 피험자 중복 여부(미확인)다.
* **관련 Axis:** T, S, H, P
* **근거 논문:** doi:10.1126/sciadv.adw1464, doi:10.1126/sciadv.aaw4358, arXiv:2605.04326, arXiv:2607.16292, doi:10.1038/s41467-021-25409-6, doi:10.1038/s41562-025-02252-z
* **가능한 데이터셋:** Horikawa 2020(학습), Mind captioning(검증)
* **label-provenance:** felt / 규범 / **evidence-level:** R0. 선택이 검증보다 먼저라 순환은 피하지만 개입은 아니다 / **insilico-vs-observed:** 혼합(TRIBE 선택 조건)
* **신규성 점검:** adversarial-reviewer는 D6 선행을 찾지 못했다. EmoMind(arXiv:2605.16739)는 Mind captioning에서 Horikawa 2020으로 가는 교차 데이터셋 decoding만 했다. 교차 코호트 선택-검증 설계는 찾지 못했다. **already_done: partially**다.
* **예상되는 반론과 대응:**
  * 두 코호트는 scanner(Verio vs Prisma), TR(2 s vs 1 s), 전처리가 다르다. 대응: 이 차이 자체가 S축의 "scanner/preprocessing shift" 시험이다. parcel 수준에서 비교한다.
  * 같은 연구실이라 피험자가 겹칠 수 있다. 대응: 겹침이 확인되면 그 피험자를 빼거나 '같은 개인, 다른 세션' 검증으로 재분류한다.

### EF-P7. In-silico 감각 박탈과 관찰된 무음 조건의 대조
* **받는 에이전트:** multimodal-dynamics (X3, Chain 3) (참조: generative-counterfactual CH4)
* **제안 내용:** 너희 쪽 X3(TRIBE modality dropout으로 in-silico 감각 박탈)를 우리 쪽 **관찰 대조쌍**으로 고정하면 R1 결과의 기준점이 생긴다.
  * (i) Emo-FilM 영화를 영상만, 오디오만, 대사 텍스트만, 전체로 각각 TRIBE v2에 넣는다. 정서 관련 관찰 분산(50항목 encoding)을 각 예측이 영역별로 얼마나 재현하는지 본다.
  * (ii) 관찰된 무음 조건(Horikawa 2020, Mind captioning)에서 영상만 넣은 in-silico 예측이 vmPFC 정서 기하를 얼마나 재현하는지 본다. 이를 (i)의 영상만 조건과 대조하면, "in-silico 무음"이 "관찰 무음"과 같은 손실을 내는지 확인할 수 있다.
  * (iii) 음원 분리 stem(대사, 음악, 효과음)을 오디오 입력으로 바꿔 넣는 R1 반사실을 만든다. 이를 원 영화에서 음악이 있는 구간과 없는 구간의 관찰 차이(R0)와 같은 방향인지 비교한다.
* **관련 Axis:** M, F, H, L, S
* **근거 논문:** doi:10.1126/sciadv.adk6840, arXiv:2605.04326, arXiv:2507.22229, doi:10.1016/j.isci.2020.101060
* **가능한 데이터셋:** Emo-FilM, Horikawa 2020, Mind captioning, Spacetop alignvideo
* **label-provenance:** felt / 규범 / **evidence-level:** R1(in-silico 박탈과 stem 교체) + R0(관찰 대조) / **insilico-vs-observed:** 혼합
* **신규성 점검:** WebSearch("TRIBE modality ablation emotion", "in-silico sensory deprivation")에서 정서 대상 연구를 찾지 못했다. TRIBE v2 2.8절의 모달리티 기여 지도는 정서와 무관한 일반 지도다. multimodal-dynamics 검색 결과도 같다. **already_done: partially**(일반 모달 기여만 수행됨).
* **예상되는 반론과 대응:**
  * 학습 중 modality dropout은 발달 중 감각 박탈과 다르다(Lettieri 2024의 핵심은 발달 경험). 대응: "감각 박탈"이라는 이름 대신 "입력 제한"으로 부르고, 관찰 비교는 정상 성인 무음 시청(Horikawa)으로 한정한다.
  * 대사는 같은 화면의 시각 단서와 공선적이다. 대응: 텍스트만 입력한 조건과 영상만 입력한 조건의 고유 설명량으로 분해한다.

---

## 3. 받은 제안에 대한 응답

(Coordinator가 전달한 뒤 추가)

---

## 4. Coordinator 질문 8개에 대한 답

**Q1. Vision Decoding 연구자가 Emotion Neuroscientist의 문제를 해결할 수 있는가?**
부분적으로 가능하다. 도움이 되는 부분은 "정보가 어디서 사라지는가"를 단계별로 특정하는 2단계 decoding 설계(doi:10.1126/sciadv.adw1464)와 shared-subject 정렬(arXiv:2403.11207)이다. 이 둘은 작은 정서 표본에서 데이터 효율을 준다. 그러나 재구성 이미지나 캡션의 정서는 자극 공간의 속성이라 portrayed 또는 규범 정보이며, 경험 정서의 증거가 아니다. 또 군집 자극에서는 분류가 재구성처럼 보이는 함정이 있다(doi:10.1016/j.neunet.2025.107515). 우리 축에서 보면 decoder보다 encoder가 대안 설명을 경쟁시키기 쉽다. 그래서 decoding 결과에 in-silico 기준선(TRIBE 예측만으로 같은 decoding이 되는가)을 붙이는 것이 실질적인 연결점이다(arXiv:2606.06345, arXiv:2605.16739).

**Q2. LLM의 representation이나 reasoning 능력을 neural emotion representation 분석에 활용할 수 있는가?**
가능하다. 단 "평균 관찰자"(L2) 회귀자로 쓴다(arXiv:2408.13718). TRIBE v2는 이미 Llama-3.2 embedding을 언어 입력으로 쓰므로, LLM 정서 회귀자의 고유 기여는 TRIBE 예측을 공변량으로 둔 뒤에 측정해야 한다(arXiv:2605.04326). AI 라벨로 만든 뇌 지도는 PPI나 alt-test로 보정한다(doi:10.1126/science.adi6000, arXiv:2501.10970). 맥락 의존 정서와 신체 기반 정서에서는 실패가 보고되어 있어(doi:10.1038/s41598-025-14961-6), 그 실패 지점이 오히려 분석 표적이 된다.

**Q3. Generative AI로 emotion과 visual semantics를 분리해 검증할 수 있는가?**
In-silico(R1)에서는 가능하다. 관찰 뇌(R3)에서는 새 fMRI가 필요하다. 현재 근거는 두 가지 문제를 보인다. NeuroVolve의 amygdala 최대화가 얼굴, 최소화가 건물로 나와 정서 편집이 의미를 함께 바꾼다(arXiv:2512.00557). 또 자동 평가기 효과와 인간 평정 효과가 크게 다르다(arXiv:2609.27729). 우리 쪽 기여는 EF-P1의 trust map이다. 즉 encoder가 그 영역을 실측 수준으로 예측하지 못하면 그 영역의 R1 분리 결과는 보고하지 않는다(doi:10.1038/s42003-023-05440-7). feature visualization의 super-stimulus는 encoder의 성질이지 뇌의 성질이 아니다(arXiv:2605.13904).

**Q4. Emotion Dynamics를 dynamical systems나 state-space learning의 문제로 재정의할 수 있는가?**
가능하다. 다만 순서가 중요하다. 자극 자체의 시간 구조(장면 지속, 음악)가 뇌 상태의 지속을 만들 수 있으므로, 먼저 자극으로 계산 가능한 동역학(TRIBE 예측 시계열)을 빼고 잔차에 state-space 모형(rSLDS, selective SSM, DSA)을 적합해야 한다. 그래야 "정서 관성"이 자극 자기상관과 구분된다(arXiv:2605.04326, pmlr-v248-behrouz24a, arXiv:2306.10168, doi:10.1126/sciadv.abf7129). 이 순서를 지키지 않으면 systems-neuro Chain 5와 geometry-info C5의 관성 추정이 부풀려질 수 있다.

**Q5. Brain Foundation Model의 latent representation에서 감정 관련 구조를 찾을 수 있는가?**
현재 근거로는 미정이다. 근거는 다섯 가지다. (a) 뇌 입력 모델의 유일한 정서 평가(Omni-fMRI)는 누수 위험이 있는 분할과 portrayed 라벨로 보인다(arXiv:2601.23090). (b) NeuroSTORM의 "Emotion" 93%는 HCP Hariri 과제 상태 분류다(arXiv:2506.11167). (c) CortexMAE는 trait 예측에서 FC baseline을 못 넘었다(arXiv:2510.13768). (d) 자극→뇌 모델(TRIBE v2)의 latent ICA는 감각, 언어, DMN망을 회복했지만 정서 축은 보고하지 않았다(arXiv:2605.04326 2.7절). (e) 합성 뇌의 정서 관계 구조 손실(arXiv:2605.16739)과 정서 범주별 일치 변동(NeurIPS 2026 `[search_index]`)이 보고되었다. 검정 설계는 EF-P4(뇌 입력)와 EF-P1(자극 입력)이다.

**Q6. Music, Video, Image의 공통 정서 특징과 modality-specific 특징을 뇌 수준에서 구분할 수 있는가?**
부분적으로 가능하다. 데이터 구성은 무음 비디오(Horikawa, Mind captioning), 정지 이미지(NSD), 시청각 영화(Emo-FilM, Spacetop)다. 음악 단독 자극은 없다. 따라서 음악은 영화 안의 stem 분리로만 다룰 수 있다. 관찰 수준의 데이터셋 간 비교는 Stage 1 판정상 수준 2~3(이름 대응 RSA 또는 공통 모델 공간)까지다. in-silico 입력 제한(EF-P7, R1)으로 모달리티 기여를 분리하고, 그 결과를 관찰 무음 조건과 대조하는 것이 현실적인 경로다(doi:10.1126/sciadv.adk6840, arXiv:2605.04326).

**Q7. Neuroscience에서 관찰되는 정서 관련 계산을 AI architecture의 구조적 제약으로 구현할 수 있는가?**
우리 축에서 구체적인 후보는 두 가지다. (a) foundation encoder에 내수용과 생리 입력 채널을 추가하는 구조다. TRIBE v2 Discussion이 이것을 한계로 명시했다(arXiv:2605.04326). Emo-FilM 생리로 예측 이득을 검증할 수 있다. (b) 공유 core와 개인 readout 구조(doi:10.1038/s41586-025-08829-y)를 '공유 평가 + 개인 평가'로 해석하는 것이다. 다만 우리 데이터로는 "예측 이득이 있는가"까지만 검정할 수 있다. 그 구조가 뇌의 계산 방식이라는 주장은 식별 가능성 문제(arXiv:2302.06677)로 막힌다. 정서 ROI 대상 brain-tuning(arXiv:2511.07988)은 frontier-ai 쪽에서 다룬다.

**Q8. 정서 라벨이 없는 NSD 같은 데이터도 다른 데이터셋과의 representation alignment로 의미 있게 활용할 수 있는가?**
가능하다. 단 결과는 "모델 추정 정서"로만 표기한다. 경로는 셋이다.
* (a) TRIBE v2는 NSD로 학습하지 않았으므로(공개 학습 설정 기준), NSD 반복 ceiling으로 정지 이미지 in-silico 예측의 충실도를 보정할 수 있다(arXiv:2606.06345가 NSD 입력 방식을 제공).
* (b) Horikawa와 Mind captioning으로 학습한 정서 encoder를 NSD 이미지에 적용해 정서 구동 이미지를 screening한다. 그다음 NSD 실측 beta로 검증한다(doi:10.1038/s41467-021-25409-6, doi:10.1038/s41562-025-02252-z). 라벨 점검은 nsdmeadows 100장으로만 가능하다.
* (c) 주의: NSD는 많은 decoder와 encoder의 학습 데이터다. 그런 모델을 NSD 분석에 쓰면 누수가 생긴다(NSD 기반 모델 비교 예: doi:10.1038/s41467-024-53147-y).

---

## 5. Axis 결정에 대한 의견

* **U, V, W 독립 Axis 채택에 동의한다.** 이견은 없다.
* **분류 명확화 요청:** TRIBE v2 같은 in-silico 뇌 예측은 "Machine Affect Representations"(R의 Sub-axis)가 아니다. 이것은 뇌의 대리 모델이므로 F, H에 두고 insilico-vs-observed 태그로 구분하기를 제안한다. R의 Sub-axis는 AI 모델 내부의 정서 표상에 한정한다.
* **W와 H의 조합 범위:** 자극 구동 encoder는 내부 생성 경험(회상)을 직접 예측하지 못한다. 따라서 W x H 조합은 EF-P2처럼 "지각 반응의 분해 기준"으로 encoder를 쓰는 형태로 한정한다.
* **S에 Sub-axis 추가 제안:** "Same-stimulus Cross-cohort Generalization"(Horikawa 2020과 Mind captioning). scanner, TR, 전처리가 다른 두 코호트가 같은 자극을 봤으므로, 획득 조건 이동과 피험자 이동을 함께 시험할 수 있다.

---

## 6. 이번 라운드 문헌 갱신

* 추가(`literature.jsonl`): NeurIPS 2026 "Evaluating TRIBE v2 Beyond Its Original Benchmarks" (`verified_by: search_index`, `discussion_read: search_summary`, neurips.cc 접속 불가), VIBE arXiv:2507.17958 (arxiv.org/abs로 확인, abstract_only).
* 정정: arXiv:2605.16739와 arXiv:2605.04326 항목의 already_done을 "no"에서 "partially"로 바꿨다(NeurIPS 2026 search_index 근거).
* 미확인으로 남긴 것: NeurIPS 2026 논문의 데이터셋과 방법, Durham의 encoding→회상 연구 식별자, 제3자 TRIBE v2 피질하 head(Hugging Face, `[search_index]`, 사용하지 않음), Mind captioning 저장소의 실제 파일 구성과 두 코호트의 피험자 중복.
