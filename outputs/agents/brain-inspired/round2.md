# Round 2: Cross-Agent Exchange, brain-inspired (Agent 11)

* 기준일: 2026-11-12. 절차: `reference/protocols.md` P2와 Coordinator 위임 메시지.
* 읽은 자료: 다른 10개 에이전트의 `round1.md`(0절, 1절, 3절, 4절, 6절 위주, 필요한 chain은 전문), `outputs/axis_encyclopedia.md` 0절과 2절, Axis N 항목, `outputs/STAGE_STATUS.md` 사용자 결정 기록, `outputs/literature/literature_db.csv`(인용 ID 확인용).
* 바뀐 전제 반영: 사용 가능 데이터셋 5개(Horikawa 2020, Emo-FilM, Spacetop, NSD, Mind captioning = Horikawa 2025, doi:10.1126/sciadv.adw1464, ds005191). Mind captioning 저장소의 실제 파일 세부는 미확인이며, 아래에서는 논문 본문 기준 사양(6명, 72클립 5회 반복, 회상 imagery와 vividness, 정서 배제 인간 캡션)을 가정한다.
* 표기: 모든 제안에 필수 태그 label-provenance(대상 / 주체)와 evidence-level(R0 상관, R1 모델 내 개입, R2 새 행동 평정, R3 새 fMRI 자극 조작, R4 뇌 개입)를 단다. 새로움 주장에는 이번에 실제로 수행한 검색 경로를 적었다(6절). arXiv API는 이번 라운드 중 429를 반환해 일부 검색을 WebSearch와 Crossref로 대신했다(우회하지 않음).
* 이번 라운드에서 새로 확인해 `literature.jsonl`에 넣은 논문: doi:10.1016/j.neuroimage.2023.120316, doi:10.1016/j.neuroimage.2025.121439 (둘 다 Crossref 서지 확인, 내용은 검색 요약 수준).

---

## 1. 가져온 아이디어

### A1. Latent action을 Axis V의 자극 계산 가능 변수로 (출처: frontier-ai T6, U8, C6)
* 근거: Latent Action Pretraining from Videos (LAPA), arXiv:2410.11758. V-JEPA 계열은 관찰자 예측만 하고 행동 조건 예측이 없다는 한계, arXiv:2502.11831 (frontier-ai 인용).
* 내 Round 1의 약점: Chain 2(정서 범주 대 행동 경향)는 Horikawa에서 행동 경향 라벨을 MLLM이나 신규 인간 주석으로 만들어야 했다. 그러면 라벨 출처가 AI 추정이 되고 범주 라벨과 같은 언어 공간을 공유해 공선성이 커진다.
* 가져와서 바뀌는 점: latent action은 "장면이 다음에 허용하는 움직임"을 언어 라벨 없이 프레임 쌍에서 뽑는다. 그러면 Axis V를 세 수준으로 측정할 수 있다. (a) 인간 평정 행동 경향(Emo-FilM Motivation 10항목, 별도 평정자 규범), (b) 자극 계산 affordance(latent action), (c) AI 언어 주석. 세 수준이 같은 뇌 분산을 설명하는지가 곧 "행동 경향이 언어적 범주의 재표현인가, 시각 동역학에 묶인 변수인가"를 가르는 검정이 된다.
* 주의: LAPA는 로봇 조작 비디오로 학습했다. 영화의 카메라 이동과 편집 컷은 nuisance로 넣어야 한다. 영화와 사회 장면에 적용한 연구는 내 검색(WebSearch, Crossref)에서도 찾지 못했다(6절).

### A2. 계산 모형 비교 전에 식별 가능성 시뮬레이션 (출처: adversarial-reviewer D3, I4, U4)
* 근거: System identification of neural systems: If we got it right, would we know? arXiv:2302.06677. adversarial-reviewer D3는 TEM 결과가 같은 평정 궤적의 비선형 확장으로도 나올 수 있다고 지적했다.
* 내 Round 1의 약점: Chain 1(SR 대 대칭 유사도), Chain 4(distributional 대 단일 채널), Chain 5(affective charge 대 RL)는 모두 "어느 계산 모형이 BOLD를 더 잘 설명하는가"를 묻는데, fMRI 잡음과 영화 14편, 피험자 수에서 그 모형들이 원리적으로 구분되는지 먼저 확인하지 않았다.
* 가져와서 바뀌는 점: 세 chain 모두 1단계로 "각 모형이 생성한 합성 BOLD(실측 잡음 구조, 같은 설계)에서 모형 회복 혼동 행렬"을 계산하고, 회복이 우연 수준이면 실제 비교를 하지 않고 그 자체를 음성 결과로 보고한다. 특히 Hesp 2021이 스스로 적었듯 보상 과제에서는 precision 갱신이 RPE처럼 보이므로(doi:10.1162/neco_a_01341, Discussion 중반), Chain 5에는 이 단계가 필수다.

### A3. 자극 구동 encoder의 '수동 관찰자' 가정과 잔차 = 평가 (출처: encoding-foundation Chain 2, 4절 개념 1)
* 근거: TRIBE v2, arXiv:2605.04326 (저자들이 입력이 시각, 청각, 의미뿐이고 체성감각과 내수용감각이 없으며 뇌를 수동 관찰자로 다룬다고 Discussion 2단락에 명시, encoding-foundation 기록). MIRAGE, arXiv:2605.29850 (Limbic망 개선 폭 최소). Jang & Kragel 2025, doi:10.1523/JNEUROSCI.1436-24.2025.
* 가져와서 바뀌는 점: 내가 제안한 Axis N의 Sub-axis "Observer-as-Agent Modeling"을 측정 가능한 형태로 만든다. 자극 구동 encoder가 설명하지 못하는 limbic 잔차를, 관찰자를 agent로 볼 때만 생기는 변수(예측 불확실성, 측정 생리에서 계산한 항상성 편차, 기대 위반)가 설명하는지 묻는다(BI-P4).

### A4. 오차형 경계와 불확실성형 경계의 구분 (출처: multimodal-dynamics Chain 2)
* 근거: Nguyen, Etzel, Bezdek, Zacks 2026, doi:10.7554/eLife.107955 (사건 분절의 오차형과 불확실성형 기제, multimodal-dynamics 기록).
* 내 Round 1의 약점: Chain 5(C)는 "arousal = 관찰자 예측모형의 불확실성"을 제안했지만, 예측오차(이미 일어난 놀람)와 예측 불확실성(앞으로의 모호함)을 구분하지 않았다. Pattisapu 2024의 정식화(arXiv:2407.02474)에서 arousal은 사후 신념 entropy이고 놀람은 별개 양이다.
* 가져와서 바뀌는 점: arousal 관련 평정 항목을 두 계열로 나눈다. Suddenly(사건이 갑작스러움)는 오차형, Predictable(사건 예측 가능성)과 Urgency는 불확실성형 후보다. 두 계열이 world model의 오차와 불확실성에 각각 결합하는지, 그리고 편도체/섬엽이 어느 쪽을 따르는지 검정한다(BI-P5).

### A5. 정서 배제 인간 캡션과 회상 imagery (출처: vision-decoding 0.1, R2, R6; llm-semantics Chain 1)
* 근거: Horikawa 2025, doi:10.1126/sciadv.adw1464.
* 가져와서 바뀌는 점: (a) Axis V 경쟁 검정의 의미 통제 변수로 "정서를 쓰지 말라"는 지시로 받은 인간 캡션 embedding을 쓴다. 행동 경향이 장면 기술 의미로 환원되는지 직접 볼 수 있다. (b) 회상 imagery에는 시각 입력이 없으므로, 행동 준비(affordance) 성분이 지각 없이도 재활성되는지 묻는 Axis V x W 질문이 가능해진다(BI-P6).

### A6. 기하가 아닌 흐름의 비교 (출처: multimodal-dynamics X2, Chain 7)
* 근거: Dynamical Similarity Analysis, arXiv:2306.10168.
* 가져와서 바뀌는 점: SR은 "지도"가 아니라 "이동 규칙"의 요약이다. SR 행렬과 신경 궤적 사이를 RSA로만 비교하면 다시 정적 기하 비교가 된다. BI-P1에서 신경 궤적의 벡터장 수준 유사도(DSA)를 보조 분석으로 넣는다.

---

## 2. 보내는 제안

### BI-P1. 정서 지도의 방향성 검정: successor geometry 통합안
* **받는 에이전트:** geometry-info (참조: adversarial-reviewer)
* **제안 내용:** "너희 쪽 C2(정적 유사성 지도 대 경험된 전이 지도, 해마 장축의 할인율 γ 위계)를 우리 쪽 방향성 대조 SR(T) 대 SR(T')와 가치 가중 SR로 검증, 확장할 수 있다." T와 그 전치 T'는 대칭 성분이 같고 방향만 다르므로, 뇌가 SR(T)를 SR(T')보다 더 잘 따를 때만 "예측 방향" 증거가 된다. C2의 정적 RDM 통제만으로는 '전이 구조'와 '전이 행렬에 섞인 대칭 성분'을 구분하지 못한다. 순서는 (1) adversarial-reviewer D3 식의 식별 가능성 시뮬레이션(SR(T), SR(T'), 정적 RDM, TEM-무작위, TEM-경험 전이, 같은 차원 random-feature null), (2) 실제 데이터 비교, (3) γ 장축 위계로 공동 사전등록할 것을 제안한다.
* **관련 Axis:** N, K, D, E, T
* **근거 논문:** doi:10.1038/s41467-025-68240-z (TEM 환경이 대칭 상관-MDS 위 균등 random walk, Methods), doi:10.1073/pnas.1616056114 (전이 비대칭, Discussion 3째 단락), doi:10.1523/JNEUROSCI.1431-18.2018 (현재 정신상태 패턴이 가능성 높은 미래 상태를 닮음, 가장 가까운 신경 선행), doi:10.1038/nn.4650, arXiv:2302.06677, arXiv:2306.10168
* **가능한 데이터셋:** Emo-FilM (주, 1 Hz 50항목, 30명). Horikawa는 C2 제안대로 생태적 전이가 없는 음성 대조로만.
* **예상되는 반론:** (1) 비대칭 성분이 작아 SR(T)와 SR(T')의 차이가 검정력 밖일 수 있다. 시뮬레이션 1단계가 이를 먼저 판정한다. (2) 영화 14편의 전이는 서사 특이적이라 영화 정체성이 섞인다. 전이와 신경 RDM을 서로 다른 영화로 추정해야 한다. (3) Ma & Kragel의 효과 크기가 작다(r 약 0.04~0.10). (4) 전이는 별도 평정자 consensus의 것이지 fMRI 참가자의 경험이 아니다.
* **label-provenance:** felt / 별도 평정자 규범(z-score 상대값). **evidence-level:** R0 (모델 비교는 관찰 데이터의 상관 수준)
* **선행 확인:** SR이나 RL로 해마-vmPFC 정서 표상을 예측한 연구는 미발견(6절 검색 1). 가장 가까운 선행 Thornton 2019는 정신상태 사고 과제이며 대칭 성분 통제 여부를 초록으로 확인하지 못했다.

### BI-P2. Axis V 경쟁 검정: 정서 범주 대 행동 경향 대 자극 계산 affordance
* **받는 에이전트:** frontier-ai (참조: llm-semantics, emotion-theory)
* **제안 내용:** "너희 쪽 T6(latent action으로 본 정서 동기 성분)를 우리 쪽 Axis V 경쟁 설계로 검증, 확장할 수 있다." T6는 latent action이 Motivation 평정과 운동, 전운동, 두정 반응을 설명하는지 묻는다. 여기에 (a) 정서 범주 band(Emo-FilM discrete 13 / Horikawa 34), (b) 인간 평정 행동 경향 band(Emo-FilM Motivation 10), (c) latent action band, (d) 의미 통제 band(정서 배제 인간 캡션 embedding, Mind captioning; Emo-FilM은 MLLM 캡션으로 대체하고 AI 생성 표기)를 같은 banded ridge에 넣어, transmodal 영역에서 범주 고유 분산이 행동 경향 band로 얼마나 대체되는지를 본다. 파일럿 0단계는 평정 수준 공선성(Emo-FilM에서 discrete 항목을 Motivation 항목으로 교차 예측한 R²)을 먼저 계산하는 것이다. Morgenroth et al. 2026이 이산 정서가 component로 잘 예측된다고 보고했기 때문이다.
* **관련 Axis:** V, A, I, B, C, R
* **근거 논문:** arXiv:2410.11758, doi:10.1016/j.isci.2020.101060 (Discussion 2째 단락 "emotional experience (or affordances)"), doi:10.1073/pnas.2414005122 (DNN이 affordance보다 물체에 정렬, embodied/VLA 비교 제안), doi:10.1093/cercor/bhad093, doi:10.1371/journal.pbio.3000900 (component 모형 fMRI 선행), doi:10.1037/emo0001619 (공선성 경고), doi:10.1126/sciadv.adw1464, doi:10.1016/j.neuroimage.2025.121439
* **가능한 데이터셋:** Emo-FilM (인간 행동 경향 평정이 있는 유일한 데이터), Horikawa 2020 + Mind captioning (34범주, 정서 배제 캡션, 같은 비디오 11명)
* **예상되는 반론:** (1) latent action은 로봇 조작 영상 분포라 영화 장면에서 의미 있는 표상을 낼지 불확실하다(카메라 운동이 지배할 수 있음). (2) Motivation 평정과 discrete 평정은 같은 평정자군에서 나와 공선성이 높을 수 있다. (3) "행동 경향"과 "정서 범주"는 이론적으로 분리 불가능하다는 반론(Frijda 계열에서 행동 준비는 정서의 구성 요소). 이 경우 결과는 "어느 성분이 transmodal 분산의 주 운반자인가"로 해석한다. (4) 새로움은 중간(Mohammadi 2023, Leitão 2020이 component 네트워크를 이미 보고). 새로움은 '직접 경쟁과 자극 계산 affordance'에 한정된다.
* **label-provenance:** 범주와 Motivation = felt / 별도 평정자 규범, latent action = 계산된 자극 feature(라벨 아님), MLLM 캡션 = AI 추정, Mind captioning 캡션 = 인간 주석(시각 내용 기술, 정서 배제). **evidence-level:** R0

### BI-P3. 피질하 경로의 정보 내용과 선택성: Horikawa와 Spacetop 교차 설계
* **받는 에이전트:** systems-neuro
* **제안 내용:** "너희 쪽 Chain 3(Spacetop에서 colliculus-pulvinar-amygdala 경로의 looming 추적과 열 통증 비반응 선택성)을 우리 쪽 Chain 3(Horikawa 34범주에서 경로가 싣는 정보가 얕은 층 feature로 충분한가)과 묶어 검증, 확장할 수 있다." 한 데이터셋에서 MPathI로 추정한 경로 패턴을 다른 데이터셋에 고정 적용(전향 적용)하면 순환 추론 없이 (a) 범주 특이성(Horikawa 2,181개 클립), (b) 위협 대 통증 선택성과 시간 추적(Spacetop TR 0.46 s)을 함께 본다. shortcut 정의는 저공간주파수 하나로 두지 않고 얕은 층 feature와 저공간주파수 에너지를 별도 band로 둔다(McFadyen 2017이 공간주파수 무관 경로를 보고했으므로).
* **관련 Axis:** E, N, B, S
* **근거 논문:** doi:10.1016/j.neuron.2021.06.001, arXiv:2607.19327 (shortcut 없으면 조건화 실패), doi:10.1523/JNEUROSCI.3525-16.2017, doi:10.1523/JNEUROSCI.1436-24.2025 (편도체 하위영역 DNN encoding, baseline), doi:10.7554/eLife.108043 (위협 학습 중 pulvinar 분할)
* **가능한 데이터셋:** Horikawa 2020(5명, TR 2 s, MB4), Mind captioning(6명, TR 1 s, MB6, 72클립 반복으로 피질하 신뢰도 추정 가능), Spacetop(alignvideo, social 열 통증)
* **예상되는 반론:** (1) 3T에서 상구, pulvinar 부분 용적과 MB 중심부 잡음(signal-feasibility 태그 필수). (2) 획득 조건이 데이터셋마다 달라 경로 패턴의 전향 적용이 안 될 수 있다. 그 자체가 일반화 한계 보고가 된다. (3) fMRI로 '빠른' 경로의 latency는 판단할 수 없다. 이 제안은 표상 내용만 묻는다. (4) Horikawa 공개 전처리본은 native 공간 블록 평균이라 ROI를 피험자별로 정의해야 한다.
* **label-provenance:** Horikawa = felt / 별도 평정자 규범, Spacetop = felt / 참가자 본인(사후, 결측 약 51%). **evidence-level:** R0
* **signal-feasibility:** 미점검. 1단계로 각 데이터셋의 SC, pulvinar, 편도체 tSNR과 Mind captioning 반복 클립의 split-half 신뢰도를 보고할 것.

### BI-P4. Limbic 맹점을 '관찰자 = agent' 변수로 분해
* **받는 에이전트:** encoding-foundation (참조: systems-neuro U2)
* **제안 내용:** "너희 쪽 Chain 2(Limbic 맹점의 분해: 잡음, 몸, 평가)를 우리 쪽 Observer-as-Agent 변수로 확장할 수 있다." Chain 2의 설명 band(a TRIBE v2 예측, b 참가자 측정 생리, c 규범 평정 성분)에 (d) 관찰자 예측모형 변수(video world model의 예측오차와 예측 불확실성), (e) 측정 생리에서 계산한 항상성 편차의 변화량(homeostatic RL의 drive 감소 대리)을 더한다. 가설: ceiling 정규화 후 남는 limbic 잔차 중 일부는 '자극 내용'이 아니라 '관찰자 상태 갱신'에 결합한다. 반대로 (d), (e)가 아무것도 더하지 못하면, TRIBE v2 저자들이 든 '수동 관찰자' 한계는 limbic 성능 저하의 주원인이 아니라는 결론이 된다.
* **관련 Axis:** N, H, F, A(Interoception), E
* **근거 논문:** arXiv:2605.04326, arXiv:2605.29850, doi:10.7554/eLife.04811 (homeostatic RL), doi:10.1016/j.tins.2020.09.012, arXiv:2407.02474, doi:10.1371/journal.pcbi.1012994 (영화 arousal 연결성 모델의 일반화)
* **가능한 데이터셋:** Emo-FilM (참가자 PPG, 호흡, EDA 1000 Hz 공개; 30명; 50항목)
* **예상되는 반론:** (1) 생리 회귀자와 BOLD의 심박, 호흡 잡음 성분이 섞인다(RETROICOR 처리 유무를 조건으로 둘 것, encoding-foundation도 지적). (2) world model 불확실성은 AI 모형의 것이지 인간 관찰자의 것이 아니다. (3) '항상성 편차' 계산에 필요한 setpoint를 생리 기저선으로 정의하는 것은 임의적이다. (4) 수동 시청에는 행동 선택이 없어 drive 감소 계산이 제한된다(내 Round 1 I-9에서 인정).
* **label-provenance:** 평정 = felt / 별도 평정자 규범, 생리 = 참가자 측정, world model 변수 = 계산된 모델 변수(in-silico). **evidence-level:** R0. **insilico-vs-observed:** 혼합

### BI-P5. Arousal은 예측 불확실성인가 예측오차인가
* **받는 에이전트:** multimodal-dynamics (참조: frontier-ai CH2)
* **제안 내용:** "너희 쪽 Chain 2(다중모달 예측 surprise와 정서 경계, 오차형 대 불확실성형)를 우리 쪽 active inference 정식화(arousal = 사후 신념 entropy, Pattisapu 2024)로 검증, 확장할 수 있다." 같은 world model에서 오차와 불확실성 시계열을 함께 뽑아, Emo-FilM의 Suddenly(오차형 후보), Predictable과 Urgency(불확실성형 후보), Alert와 AtEase(arousal 느낌), 참가자 EDA, 편도체/섬엽 반응이 각각 어느 쪽에 고유하게 결합하는지 본다. frontier-ai CH2(정서적 놀람이 pixel, latent 물리, 서사 의미 중 어느 수준 예측오차와 결합하는가)와 세 에이전트 공동 설계로 합치면, 예측 위계(수준) x 신호 유형(오차 대 불확실성)의 2차원 표가 된다.
* **관련 Axis:** N, D, C, A, I
* **근거 논문:** arXiv:2407.02474, doi:10.7554/eLife.107955, arXiv:2506.09985, arXiv:2305.11772 (latent 미래 예측과 고차 피질 정렬), doi:10.1016/j.neuroimage.2023.120316 (영화 arousal과 편도체-섬엽 연결, 기존 arousal 모형 기준)
* **가능한 데이터셋:** Emo-FilM (주), Spacetop alignvideo (시간축 평정 없음, 신경 재현만)
* **예상되는 반론:** (1) world model의 예측 분산을 '불확실성'으로 읽는 것은 모델 구조에 따라 달라진다(앙상블, 확산형 예측기 등 정의가 여럿). 적어도 두 정의로 결과가 같은지 확인해야 한다. (2) 평정자는 영화를 여러 번 봐서 놀람 평정이 앞당겨질 수 있다(multimodal-dynamics 개념 5). (3) 편집 컷과 음향 onset이 오차 신호를 지배할 수 있다. (4) 생리(참가자)와 평정(별도 평정자)의 주체가 다르다.
* **label-provenance:** felt / 별도 평정자 규범 + 참가자 측정 생리 + 모델 계산 변수. **evidence-level:** R0
* **선행 확인:** video world model의 예측 불확실성으로 영화 시청 중 arousal이나 편도체/섬엽 반응을 설명한 연구는 미발견(6절 검색 3). 가장 가까운 것은 계산적 arousal 모형 기반 연결성 연구(doi:10.1016/j.neuroimage.2023.120316)와 언어 entropy 연구다.

### BI-P6. 회상에서 행동 준비 성분이 재활성되는가 (Axis V x W)
* **받는 에이전트:** vision-decoding
* **제안 내용:** "너희 쪽 R2(같은 정서 클립 회상에서 정서 재활성, 정서 우위 회상)를 우리 쪽 Axis V로 확장할 수 있다." 지각 학습 encoding/decoding을 정서 범주 band, 행동 경향 band(latent action과 주석), 시각-의미 band로 나눠 학습한 뒤, 회상 시행에서 각 band의 재활성 정도를 비교한다. 예측: 행동 준비가 정서의 핵심 성분이라면(Horikawa Discussion 2째 단락의 해석), 회상에서 시각 세부보다 행동 경향 성분이 더 잘 보존되고 그 보존은 운동, 전운동, 두정 영역에서 나타난다. 반대 결과(행동 경향 성분이 시각 세부만큼 사라짐)는 행동 경향 표상이 시각 입력에 묶인 지각적 affordance에 가깝다는 해석을 지지한다.
* **관련 Axis:** V, W, G, H
* **근거 논문:** doi:10.1126/sciadv.adw1464, doi:10.1016/j.isci.2020.101060, doi:10.1073/pnas.2414005122, arXiv:2410.11758
* **가능한 데이터셋:** Mind captioning(회상 imagery, vividness), Horikawa 2020(같은 비디오 지각 데이터로 학습 표본 확대). 두 코호트 피험자 중복 여부는 미확인이라 교차 코호트 주장 시 subject-level leakage 점검 필요(vision-decoding 지적).
* **예상되는 반론:** (1) 회상 신호의 SNR이 낮아 band 간 차이가 잡음에 묻힐 수 있다. (2) 회상 중 운동 영역 활성은 행동 준비가 아니라 눈 감기, 회상 노력 같은 과제 요인일 수 있다(지각 대조 조건과 vividness 공변량 필요). (3) 회상 대상이 72개 클립뿐이라 범주 수준 비교는 거칠다. (4) 정서는 참가자 본인 보고가 아니다.
* **label-provenance:** felt / 별도 평정자 규범(C&K), vividness = 참가자 본인. **evidence-level:** R0

---

## 3. 받은 제안에 대한 응답

(Coordinator가 전달한 뒤 추가)

---

## 4. Coordinator 질문 8개에 대한 답 (brain-inspired 관점)

1. **Vision Decoding 연구자가 Emotion Neuroscientist의 문제를 해결할 수 있는가?** 부분적으로 가능하다. 현행 재구성 파이프라인은 입력이 시각 ROI라 편도체, 섬엽, vmPFC를 구조적으로 뺀다(vision-decoding 0.2; MoRE-Brain 스스로 "보는 것"만 다룬다고 Limitations에 명시, arXiv:2505.15946). 내 관점의 기여는 구조다: 기능 네트워크를 expert로 둔 MoE(arXiv:2605.19279)에 limbic expert를 추가하고 routing 가중치가 정서 범주별로 달라지는지 보면, 해독 성능이 아니라 "어느 경로가 정서 정보를 더하는가"를 물을 수 있다. 다만 해독 가능성은 경험의 증거가 아니다(evidence-level R0).
2. **LLM의 representation이나 reasoning을 neural emotion representation 분석에 쓸 수 있는가?** 쓸 수 있다. 내 쪽에서 가장 직접적인 용도는 두 가지다. (a) 정서 전이의 mental model: Thornton & Tamir 2017(doi:10.1073/pnas.1616056114)의 인간 전이 판단을 LLM 전이 판단으로 대체하거나 비교해 SR의 전이 행렬 후보로 쓴다(AI 추정 표기). (b) 의미 통제: 정서 배제 캡션 embedding으로 행동 경향의 언어 환원 여부를 검정(BI-P2). 단 LLM 판단은 3인칭 관찰자 관점이라(llm-semantics U3) 경험 정서 대리로 쓰면 안 된다.
3. **Generative AI로 emotion과 visual semantics를 분리해 검증할 수 있는가?** 원리적으로는 가능하지만 정서 조작이 의미를 함께 바꾸는 문제가 확인되어 있다(NeuroVolve, arXiv:2512.00557, generative-counterfactual U1). 내 관점의 추가: 정서와 의미 외에 세 번째 요인인 affordance가 있다. 물체 구성은 고정하고 "도망칠 경로"나 "접근 가능 거리"만 바꾸는 장면 편집은 Bartnik 2025(doi:10.1073/pnas.2414005122)의 affordance 축을 정서 쪽으로 옮긴 조작이 된다. 관찰 데이터만으로는 R1(모델 내 개입)까지이고, 인간 평정을 새로 받으면 R2다.
4. **Emotion Dynamics를 dynamical systems나 state-space learning 문제로 재정의할 수 있는가?** 그렇다. 내 쪽 후보는 세 가지 계산 동역학이다. 전이 예측 지도(SR, doi:10.1038/nn.4650), 변화의 누적(momentum, doi:10.1016/j.tics.2015.07.010), 신념 precision의 갱신(active inference, doi:10.1162/neco_a_01341). 이들은 서로 다른 상태 변수(미래 점유, 누적 변화량, 확신)를 상태로 두므로, 상태공간 모델을 비교할 때 "어떤 상태 변수가 신경 궤적의 흐름(DSA, arXiv:2306.10168)을 재현하는가"로 판정할 수 있다. 선결 조건은 식별 가능성 시뮬레이션이다(arXiv:2302.06677).
5. **Brain Foundation Model의 latent에서 감정 관련 구조를 찾을 수 있는가?** 찾을 수는 있지만 현재는 엄밀한 benchmark가 없다(encoding-foundation U5). 내 관점의 질문은 "latent가 정서 범주를 담는가"보다 "자극 구동 모델이 원리적으로 담을 수 없는 관찰자 상태 변수(예측 불확실성, 항상성 편차)를 latent가 담는가"이다. TRIBE v2는 저자 스스로 수동 관찰자 가정을 한계로 들었다(arXiv:2605.04326). BI-P4가 이 질문의 encoding 판이다.
6. **Music, Video, Image의 공통 정서 특징과 modality-specific 특징을 뇌 수준에서 구분할 수 있는가?** 내 담당에서는 부분적으로만 답한다. Kragel 2021(doi:10.1016/j.neuron.2021.06.001)은 피질하 경로가 불쾌 이미지와 소리 모두의 혐오성을 추적한다고 보고해, 공통 성분의 후보가 피질하 경로에도 있음을 시사한다. 무음 Horikawa와 소리 있는 Emo-FilM, Spacetop 사이에서 같은 경로 패턴의 전향 적용(BI-P3)이 이 질문의 경로 수준 판이다. 음악 단독 자극은 보유 데이터에 없어 음악 항목은 해당 없음에 가깝다.
7. **정서 관련 계산을 AI architecture의 구조적 제약으로 구현할 수 있는가?** 구현 사례는 있다: 다중 경로 shortcut(arXiv:2607.19327, shortcut 없으면 조건화 실패), 다중 과제의 자발적 특화(doi:10.1126/sciadv.abl8913), connectome 제약(doi:10.1038/s41586-024-07939-3), 편도체 모듈을 둔 VCA(doi:10.1101/2025.10.20.683439). 그러나 **구조 제약이 인간 정서 fMRI 예측이나 해석을 실제로 바꾼다는 검증은 아직 없다**(내 Round 1과 재점검 검색 기준). 현실적인 첫 검정은 (a) 이중 경로 encoding(얕은 층 shortcut band 대 깊은 위계 band)의 피질하 설명력(BI-P3), (b) 개인 DWI 연결 강도로 제약한 피질하-피질 RNN이 Spacetop 개인 반응 예측을 개선하는가(Round 1 I-6)다. 역방향으로는 SR의 방향성(BI-P1), distributional 부호(Round 1 Chain 4)가 새 신경 질문을 만든다.
8. **정서 라벨이 없는 NSD도 representation alignment로 의미 있게 쓸 수 있는가?** 쓸 수 있으나 용도를 제한해야 한다. (a) 시각-의미 encoder의 사전학습과 반복 기반 noise ceiling 제공처, (b) Axis V 관점에서 NSD의 COCO 장면은 Bartnik 2025가 쓴 것과 같은 종류의 장면 affordance 축을 갖는다. 정서 라벨 없이도 "장면 affordance 표상이 정서 영상에서 학습한 행동 경향 축과 정렬되는가"를 물을 수 있다. 다만 affordance 라벨이 AI 추정이거나 신규 주석이어야 하고(label-provenance 표기), NSD 이미지 정서가가 대체로 중립이라는 범위 제한(Stage 1 보고서)이 있다. 근거: doi:10.1038/s41593-021-00962-x, doi:10.1073/pnas.2414005122.

---

## 5. Axis 결정에 대한 의견

* **V(Action Readiness & Affordance) 채택과 새로움 '중간' 표시에 동의한다.** 재점검에서 내가 찾은 Mohammadi 2023, Leitão 2020이 근거다. 다만 V 안에 세 측정 수준을 Sub-axis로 명시할 것을 제안한다: (V1) 인간 보고 행동 경향(Emo-FilM Motivation, Horikawa Approach 차원), (V2) 자극 계산 affordance(latent action, 장면 affordance), (V3) 방어 계산(위협 거리와 시간, doi:10.1016/j.tics.2019.12.016). 세 수준이 분리되어야 BI-P2의 경쟁 검정이 조합 단계에서 다른 Axis와 섞일 때 무엇을 측정하는지 분명해진다.
* **W 채택에 동의하고 V x W 조합(BI-P6)을 후보로 등록해 주기 바란다.** Mind captioning 사용 결정으로 데이터 조건이 충족되었다.
* **U(Label Provenance)는 내 제안 전부에 영향을 준다.** 특히 BI-P1의 '전이'는 별도 평정자 consensus의 전이라는 점이 해석의 상한을 정한다. 이견 없음.
* **Axis N 기록 확인:** encyclopedia의 N 항목(추가 Sub-axis 4개, 재정의, 분할, Neuromorphic 우선순위 하향)은 내 Round 1 제안과 일치한다. 이견 없음.

---

## 6. 이번 라운드의 검색 기록 (새로움 주장의 근거)

| # | 대상 제안 | 경로 | 결과 |
|---|---|---|---|
| 1 | BI-P1 | Stage 2 재점검 기록(export.arxiv.org "successor representation" AND emotion, "cognitive map" AND emotion AND hippocampus; api.crossref.org 2026년 이후; WebSearch 1회), 이번 라운드 재확인 없음 | SR/RL로 해마-vmPFC 정서 표상을 예측한 연구 미발견. 가장 가까운 선행 doi:10.1523/JNEUROSCI.1431-18.2018 |
| 2 | BI-P2, BI-P6 | WebSearch("latent action" model fMRI emotion action tendencies movies), api.crossref.org(latent action video brain encoding 2023 이후), export.arxiv.org는 429로 실패 | latent action을 fMRI나 정서에 적용한 연구 미발견. 행동 feature taxonomy encoding 선행 doi:10.1016/j.neuroimage.2025.121439 |
| 3 | BI-P5, BI-P4 | WebSearch(video model predictive uncertainty entropy arousal amygdala insula movie fMRI), api.crossref.org(2022 이후) | video world model 불확실성으로 영화 arousal이나 편도체/섬엽을 설명한 연구 미발견. 인접: doi:10.1016/j.neuroimage.2023.120316, doi:10.1523/JNEUROSCI.1436-24.2025, doi:10.7554/eLife.107955 |
| 4 | BI-P3 | Stage 2 재점검 기록(WebSearch 2회, api.crossref.org) | 경로 수준 얕은 층 대 깊은 층 feature 비교는 미발견. 편도체 DNN encoding(doi:10.1523/JNEUROSCI.1436-24.2025)과 pulvinar 분할 위협 학습(doi:10.7554/eLife.108043)이 인접 선행. systems-neuro는 SC looming CCN 2025 초록을 search_index 수준으로 기록 |
| 5 | BI-P6 | api.crossref.org(emotional memory recall reactivation motor action tendency fMRI, 2018 이후) | 회상 중 행동 경향 성분 재활성을 다룬 연구 미발견(검색 범위 제한적, 확정 아님) |

모든 날짜 2026-11-12. "미발견"은 위 경로 안에서의 결과이며 Stage 2 표본 검증에서 no 판정의 약 25%가 실제로는 선행 수행이었다는 점을 고려해, Stage 3 Round 3와 Stage 4 중복 감사에서 다시 확인해야 한다.

---

## 7. 미확인 사항

1. Mind captioning 저장소의 실제 파일(반복 클립, 회상 시행, vividness, 캡션 포함 여부), 두 Horikawa 코호트의 피험자 중복 여부.
2. LAPA(arXiv:2410.11758) 가중치 공개와 라이선스(huggingface.co, GitHub 차단으로 미확인).
3. Thornton et al. 2019의 대칭 유사도 통제 여부(본문 미열람).
4. Emo-FilM에서 Motivation 항목과 discrete 항목의 평정자 구성(같은 평정자인지), BI-P2 공선성 판단에 필요.
5. 각 데이터셋의 SC, pulvinar tSNR(BI-P3 signal-feasibility).
6. 이번 라운드에 추가한 두 논문(doi:10.1016/j.neuroimage.2023.120316, doi:10.1016/j.neuroimage.2025.121439)은 본문과 초록을 직접 읽지 못했다(search_summary).
