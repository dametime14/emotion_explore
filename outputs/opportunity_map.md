# Deliverable E (초안): Cross-Disciplinary Opportunity Map

* 작성: Coordinator (Stage 2 초안). Stage 3에서 Round 2~4와 조합 결과를 반영해 갱신한다.
* 기준일: 2026-11-12
* 입력: 11개 에이전트 round1.md 3절(다른 분야 아이디어)과 6절(chain), `outputs/literature/literature_db.csv`
* 행마다 출처 에이전트와 아이디어 번호를 [에이전트 번호]로 단다. 상세 설계, 반증 조건, 주의 사항은 해당 에이전트 round1.md에 있다.

## 판정 기준

| 열 | 값 | 기준 |
|---|---|---|
| Novelty | H | 제안 에이전트의 검색 범위에서 정서 신경과학 적용 사례를 찾지 못함 |
| | M | 부분 선행 있음(다른 데이터, 다른 정서 범위, 대안 하나만 시험 등) |
| | L | 같은 방식의 선행 연구가 이미 있음 |
| Feasibility | H | 보유 데이터(4개 데이터셋 원본 자극 포함)와 공개 모델, 방법으로 가능. 신규 수집 불필요 |
| | M | 소량의 신규 인간 평정이나 주석, 큰 계산량, 도구 품질 불확실성, 4개 밖 데이터 중 하나가 필요 |
| | L | 신규 fMRI 수집이 필요 |

Novelty는 Round 1 에이전트들의 자체 검색 범위 안에서만 유효하다. Stage 3 Round 3와 Stage 4 선행연구 중복 감사에서 다시 판정한다. 결론 수준(evidence-level, R0~R4)은 Deliverable B 0.2절 태그를 따르며, 생성 모델과 in-silico 행은 대부분 R1(모델 내 결론)이다.

---

## 1. 다른 분야 → Affective Neuroscience

### 1.1 통계학, ML 평가, 메타과학

| # | Originating field | Imported technique | Target neuroscience problem | Potential dataset | Evidence for transfer | Novelty | Feasibility | 출처 |
|---|---|---|---|---|---|---|---|---|
| 1 | 통계학 (surrogate label 추론) | Prediction-powered inference, design-based supervised learning | AI 정서 라벨로 만든 voxel 정서 지도의 편향 위치와 보정 | NSD, Horikawa | doi:10.1126/science.adi6000, arXiv:2306.04746 | H | M (소량 신규 인간 평정) | [AR I1, D4] |
| 2 | NLP 평가 (LLM-as-judge) | Alternative annotator test | MLLM이 Emo-FilM 평정자를 어느 CPM 성분에서 대체할 수 있는가(성분의 관찰 가능성 지도) | Emo-FilM | arXiv:2501.10970 | H | H | [AR I2] |
| 3 | NLP perspectivism, CV human uncertainty | 평정자별 모형 head, 분포 라벨 학습 | consensus가 잃는 뇌 설명력, 평정자 불일치를 자극 모호성, 개인 반응, 잡음으로 분해 | Emo-FilM, Horikawa | doi:10.1162/tacl_a_00449, arXiv:2211.02570, arXiv:1908.07086 | H | H | [ET T2, T3; ET-C5] |
| 4 | 통계학 | random stimulus model, 2-factor bootstrap, Bayesian prevalence | 영화 14편, 피험자 5명 데이터의 일반화 추론 | Emo-FilM, Horikawa | doi:10.12688/wellcomeopenres.10298.2, doi:10.7554/eLife.82566, doi:10.7554/eLife.62461 | M | H | [ET T6, AR S6] |
| 5 | 메타과학 | multiverse, specification curve, guided multiverse | Horikawa 2020 범주 결론과 Westlin 2025 재현 실패 보고가 갈리는 분석 축 | Horikawa | doi:10.1038/s41562-020-0912-z, doi:10.1038/s41467-022-31347-8, arXiv:2507.00320 | M (Westlin은 대안 1개) | H | [AR D1] |
| 6 | ML 평가 | leakage 분류, REFORMS 체크리스트, 비디오 embedding 근접 중복 탐지 | 정서 decoding 성능 중 누수(동일 원본, 시간 자기상관, 라벨 기반 선택, 사전학습 오염) 몫 | 4개 모두 | doi:10.1016/j.patter.2023.100804, doi:10.1126/sciadv.adk3452 | H | H | [AR D7] |
| 7 | ML (model identification) | ground-truth 식별 가능성 시뮬레이션 | 14편 규모에서 TEM, SR, RL 정서 지도 모델이 원리적으로 구별되는가 | Emo-FilM | arXiv:2302.06677 | H | H | [AR I4, D3; EF I5] |
| 8 | ML 평가 | anti-collapse 분할(정서 범주, 원본 영상 단위 분할) 표준화 | 범주 군집 분류와 조합적 정서 표상의 구분 | Horikawa | doi:10.1016/j.neunet.2025.107515 | M | H | [VD I6, R3] |

### 1.2 시각 신경과학, NeuroAI

| # | Originating field | Imported technique | Target neuroscience problem | Potential dataset | Evidence for transfer | Novelty | Feasibility | 출처 |
|---|---|---|---|---|---|---|---|---|
| 9 | 시각 신경과학 | 피험자 간 cross-decomposition 공유 스펙트럼 | 반복 없이 신뢰 정서 차원 수 추정, Horikawa vs Westlin 판별 | Horikawa, Emo-FilM | arXiv:2409.06843, arXiv:2505.12653 | H | H | [ET T1, C1; GI I1, C1] |
| 10 | NeuroAI 모델 비교 | controversial selection / stimuli | 정서 평정 모델 vs 최신 시각-의미 모델 중 뇌가 따르는 쪽 | Horikawa, NSD | doi:10.1073/pnas.1912334117, doi:10.1038/s41467-024-53147-y | H | H (기존 자극 선택), M (합성) | [AR I3, EF I2, GC X1] |
| 11 | 청각, 시각 NeuroAI | model metamer → affective metamer | 정서 모델의 불변성이 인간 정서 판단의 불변성과 같은가 | NSD, Horikawa | doi:10.1038/s41593-023-01442-0 | H | M (신규 행동 평정) | [AR I6, GC X2] |
| 12 | 시각 NeuroAI | relational neural control, 고처리량 선택성 screening | amygdala, vmPFC, insula의 "정서 범주 선택성"이 screening을 견디는가 | NSD, Horikawa | doi:10.1038/s41562-025-02252-z, doi:10.1038/s41467-021-25409-6 | H | H (screening), L (in vivo 검증) | [EF I2, I6] |
| 13 | 언어 신경과학 | 모델 기반 drive/suppress 자극 선택(pseudo-prospective) | 정서 모델이 고른 자극이 새 피험자의 정서 영역을 실제로 구동하는가 | Horikawa, Emo-FilM, Spacetop | doi:10.1038/s41562-023-01783-7 | H | M (기존 데이터 내 검증), L (실측) | [AR D6, GC X6] |
| 14 | 원숭이 전기생리 | 추상화 기하(CCGP, shattering dimensionality) | 기본정서이론 vs 구성주의의 기하 예측 판정 | Horikawa | doi:10.1016/j.cell.2020.09.031 | H | H | [GI I2] |
| 15 | 공간 항해 | hexadirectional grid 분석 | 자연주의 정서 궤적의 grid-like 부호(통제 과제 결과의 확장) | Emo-FilM, Horikawa | doi:10.1371/journal.pbio.3003795 | H | M (방향 추정 잡음, 내용 공선성) | [GI I3] |
| 16 | 신경동물행동학 | line attractor 시간상수(rSLDS) | 영화 후 washout에서 정서 잠재 차원의 이완 | Emo-FilM | doi:10.1038/s41586-024-07915-x | H | H | [GI I5, C5] |
| 17 | 해마 계산 | successor representation | 정서 지도는 대칭 유사도인가 방향성 전이 예측인가 | Emo-FilM | doi:10.1038/nn.4650, doi:10.1016/j.cell.2020.10.024 | M (TEM으로 부분 수행) | H | [BI I-2, Chain 1; GI C2] |
| 18 | 마우스 digital twin | functional barcode | encoder readout 가중치로 vertex 정서 tuning 예측 | Horikawa, Emo-FilM | doi:10.1038/s41586-025-08829-y | H | M | [EF I1] |
| 19 | simulation-based inference | simulator-to-real calibration gap | in-silico 뇌(TRIBE v2)가 놓친 정서 정보의 영역 지도 | Emo-FilM, Spacetop | arXiv:2604.23865 | H | M (계산량) | [EF I3] |
| 20 | NeuroAI 감사 | matched-control audit | 예측 피질 feature가 백본 대비 정서 구조를 더하는가 | Horikawa, Emo-FilM | arXiv:2607.16292 | H | H | [EF I4] |

### 1.3 Frontier AI (SSL, world model, interpretability)

| # | Originating field | Imported technique | Target neuroscience problem | Potential dataset | Evidence for transfer | Novelty | Feasibility | 출처 |
|---|---|---|---|---|---|---|---|---|
| 21 | 발달심리 → video SSL | V-JEPA 2 latent surprise(violation-of-expectation) | 정서적 놀람과 suddenness, predictability appraisal이 pixel, latent 물리, 서사 의미 중 어느 예측오차와 결합하는가 | Emo-FilM, Horikawa, Spacetop | arXiv:2502.11831, arXiv:2506.09985 | H | H (surprise 코드 CC-BY-NC) | [FA T1, CH2] |
| 22 | 표상 수렴 연구 | 정서 무관 정렬로 VLM 정서 vector 운반 | 뇌 정서 기하가 정서와 무관한 일반 정렬로 운반되는가 | Horikawa, NSD | arXiv:2609.34742, arXiv:2405.07987 | H | H | [FA T2, CH6] |
| 23 | Mechanistic interpretability | Universal SAE(뇌를 한 모델로 포함), 안정 SAE | 정서 ROI에 뇌 고유 개념이 남는가, SAE 개념이 재학습에 안정한가 | Horikawa, NSD | arXiv:2502.03714, arXiv:2502.12892 | H | M (Horikawa 표본 작음) | [FA T3, CH5] |
| 24 | LLM 정렬 연구 | 표상 가설 판별 검정 | 뇌 정서 표상이 상황 표상의 투영인가(정서 vs 상황 판별) | Horikawa, Emo-FilM | arXiv:2604.13466 | H | M (캡션 자료 필요) | [FA T4, CH1] |
| 25 | LLM 정서 표상 연구 | 정서 vector의 국소성 측정 + leaky integrator | 장면 국소 정서 신호 vs 지속 정서 상태 | Emo-FilM, Spacetop | arXiv:2604.07729 | H | H | [FA T5, CH3] |
| 26 | 로봇 학습, VLA | latent action 표상 | 정서의 동기 성분(action tendency)의 자극 계산 모델 | Emo-FilM | arXiv:2410.11758 | H | M | [FA T6] |
| 27 | speech, 다모달 모델 | brain-tuning(뇌 반응을 학습 목표로) | 정서 ROI 표적 tuning이 정서 특이 귀납 편향을 넣는가 | Emo-FilM → Horikawa, Spacetop | arXiv:2511.07988 | H | M (GPU) | [FA T7, CH7] |
| 28 | Mechanistic interpretability | LLM 내부 appraisal 방향 probe, steering, ablation | appraisal → emotion 인과 방향, ToM 네트워크 하위 과정 | Emo-FilM, Spacetop narratives | arXiv:2502.05489 | H | H (텍스트), M (전사본 생성) | [ET T8, LS I5, FA CH4, LS Chain 3] |
| 29 | 식별 가능한 표상 학습 | block-identifiable multi-view contrastive | 피험자 간 공유 정서 latent 차원 수 | Horikawa, Emo-FilM | arXiv:2303.09166, arXiv:2106.04619 | H | M | [FA CH8, GC X5] |
| 30 | LLM introspection 연구 | self vs cross-prediction 검정 | 본인 정서 보고의 privileged access(본인 보고가 peer 합의보다 본인 뇌를 더 설명하는가) | Spacetop, Emo-FilM | arXiv:2410.13787 | H | H | [ET T4, C4] |
| 31 | 의식 과학 | quality space(주관 유사성과 신경 판별성) | 정서 주관 유사성 구조의 신경 위치 | Horikawa | doi:10.1016/j.tics.2024.06.007, arXiv:2308.08708 | H | H | [ET T5, C7] |

### 1.4 생성 모델, 인과 추론, 신호 처리

| # | Originating field | Imported technique | Target neuroscience problem | Potential dataset | Evidence for transfer | Novelty | Feasibility | 출처 |
|---|---|---|---|---|---|---|---|---|
| 32 | Controllable generation | 의미 고정 최소 편집(BrainACTIV), Concept Sliders, LivePortrait | Horikawa의 emotion 우위가 의미를 고정해도 남는가 | Horikawa | arXiv:2311.12092, arXiv:2407.03168 | H | M (편집 품질, R1, 저작권) | [GC CH1] |
| 33 | 인과 ML | counterfactual invariance stress test | 정서 decoder의 의미 shortcut 검출 | Horikawa | arXiv:2106.00545 | H | M (R1, surrogate 경로) | [GC X3] |
| 34 | Mechanistic interpretability | interchange intervention | in-silico 뇌가 정서 같은 변수를 경유해 정서 영역을 예측하는가 | Emo-FilM | arXiv:2106.02997 | H | M | [GC X4] |
| 35 | 음향 신호 처리 | 영화 사운드트랙 3-stem 분리(대사, 음악, 효과음) | 정서별 소리 의존성, 음악 counterfactual | Emo-FilM, Spacetop | arXiv:2110.09958, arXiv:2211.08553 | H | H | [GC X7, CH4; MD Chain 3] |
| 36 | 실시간 fMRI | neuroadaptive Bayesian optimization | amygdala와 시각피질 반응을 최대 분리하는 자극 탐색 | 신규 수집 | doi:10.1038/s41467-018-03657-3 | H | L | [GC X8] |

### 1.5 시스템 신경과학, 계산정신의학

| # | Originating field | Imported technique | Target neuroscience problem | Potential dataset | Evidence for transfer | Novelty | Feasibility | 출처 |
|---|---|---|---|---|---|---|---|---|
| 37 | 계산정신의학 | normative modeling | 같은 영상에 대한 network 궤적의 개인 편차가 본인 평정 편차를 예측하는가 | Spacetop | doi:10.1146/annurev-psych-021621-124910, doi:10.1038/s41467-018-04387-2 | H | H | [SN I1] |
| 38 | 정신의학 휴지기 연구 | energy landscape | 자극 유발 정서 landscape와 basin 전이 | Emo-FilM | doi:10.1016/j.nicl.2024.103574, doi:10.1016/j.jad.2026.121407 | H | H | [SN I2] |
| 39 | 동물 회로 연구 | multivariate pathway identification(MPathI) | 자연 영상에서 colliculus-pulvinar-amygdala 경로, 열 통증 음성 대조 | Spacetop | doi:10.1016/j.neuron.2021.06.001 | M (학회 초록 부분 선행) | H | [SN I3, Chain 3] |
| 40 | 전역 신호 생리학 | 전역 fMRI 성분과 교감 생리 결합 모형 | network arousal 판독에서 자율신경 성분 분리 | Emo-FilM | doi:10.1038/s41593-025-01945-y | H | H | [SN I4, Chain 1] |
| 41 | ML switching dynamics | rSLDS 상태 의존 전환 | 신경 수준 정서 관성 | Emo-FilM, Spacetop | pmlr:v54/linderman17a | H | H | [SN I6, Chain 5] |

### 1.6 멀티모달, 미학, 서사

| # | Originating field | Imported technique | Target neuroscience problem | Potential dataset | Evidence for transfer | Novelty | Feasibility | 출처 |
|---|---|---|---|---|---|---|---|---|
| 42 | LLM 장문맥 메모리 | EM-LLM Bayesian surprise 사건 분절 | 정서 에피소드 경계와 hippocampus 경계 반응, 회고 평정 | Emo-FilM | arXiv:2407.09450 | H | H | [MD X1] |
| 43 | RNN 동역학 비교 | Dynamical Similarity Analysis | 평정, 뇌, 모델의 정서 동역학(이완, 어트랙터, 관성) 비교 | Emo-FilM | arXiv:2306.10168 | H | H | [MD X2, Chain 7] |
| 44 | 다중모달 encoding | modality dropout | 소리를 지운 in-silico 예측 vs 무음 Horikawa 관찰 | Emo-FilM, Spacetop, Horikawa | arXiv:2507.22229, doi:10.1126/sciadv.adk6840 | M (일반 모달 기여 지도는 있음) | H | [MD X3, EF Chain 7] |
| 45 | 계산사회과학 | 서사 정서 arc 분해 | 서사 내 위치와 vmPFC, hippocampus 상태 | Emo-FilM, Spacetop narratives | doi:10.1140/epjds/s13688-016-0093-1 | H | H | [MD X4] |
| 46 | 멀티미디어 | 관객 생리 동기화 기반 미적 하이라이트 | 미적 순간과 정서 강도의 분리 | Emo-FilM | doi:10.1145/3175497 | H | M (외부 주석 접근 미확인) | [MD X5, Chain 6] |
| 47 | 음악 인지 | 정보이론 기대(불확실성 x 놀람), 학습 진전 | 영화의 정서, 미적 순간 예측 | Emo-FilM, Spacetop | doi:10.1016/j.cub.2019.09.067, doi:10.1037/rev0000337 | H | M | [MD X6] |
| 48 | 음악 인지 | time-warped RSA | 보고된 생리(평정 항목)와 측정된 생리(PPG, EDA)의 시간 구조 비교 | Emo-FilM | doi:10.1016/j.isci.2025.114072 | H | H | [MD X7] |
| 49 | 장문맥 MLLM | 문맥 길이 sweep | 정서 항목별 시간 수용창 지도 | Emo-FilM, Spacetop | arXiv:2602.07570 | H | M | [MD X8, Chain 4] |

### 1.7 LLM, 의미, 사회 인지

| # | Originating field | Imported technique | Target neuroscience problem | Potential dataset | Evidence for transfer | Novelty | Feasibility | 출처 |
|---|---|---|---|---|---|---|---|---|
| 50 | 계산사회과학 | silicon sample → silicon rater, 평탄화 지수 | 관점 조건부 AI 주석의 분산과 개인 보고 분산 비교 | Spacetop, Emo-FilM | arXiv:2402.01908, arXiv:2408.13718 | H | H | [LS I1] |
| 51 | 컴퓨터 비전 상황 인식 | VidSitu, MovieGraphs식 관계 그래프 | 장면 관계 구조가 ToM 네트워크와 정서 영역 분산을 설명하는가 | Horikawa, Emo-FilM | arXiv:2104.00990, arXiv:1712.06761 | H | M | [LS I2] |
| 52 | 색 지각 연구 | Gromov-Wasserstein 비지도 정렬 | 뇌, 규범 평정, LLM의 3자 정서 구조 정렬 | Horikawa | doi:10.1038/s41598-024-65604-1, doi:10.1038/s41598-025-14961-6 | M (평정-MLLM 정렬은 수행됨) | H | [LS I3] |
| 53 | 사건 인지, 스포츠 분석 | belief-consistent / inconsistent surprise | 주인공 운명에 대한 믿음 갱신과 서사 정서 | Spacetop narratives | doi:10.1016/j.neuron.2020.10.029, doi:10.3758/s13428-024-02569-z | H | H | [LS I4] |
| 54 | 게임 정동 컴퓨팅 | 시간 해상도별 연속 주석 일치도 곡선 | AI 연속 정서 주석을 뇌 분석에 쓸 수 있는 최소 시간 척도 | Emo-FilM | arXiv:2502.04379 | H | H | [LS I7] |

### 1.8 RL, 체화 인지, 생태 심리, 정보이론

| # | Originating field | Imported technique | Target neuroscience problem | Potential dataset | Evidence for transfer | Novelty | Feasibility | 출처 |
|---|---|---|---|---|---|---|---|---|
| 55 | 강화학습 | distributional TD(채널별 비대칭 PE) | 통증 기대의 confirmation bias가 단일 채널 gain인가 다중 채널인가 | Spacetop social | doi:10.1038/s41586-019-1924-6, doi:10.1073/pnas.2513856123 | H | H | [BI I-1, Chain 4] |
| 56 | 생태 심리, 체화 AI | affordance, action readiness | 정서 범주 표상 vs 행동 경향 표상 | Emo-FilM, Horikawa | doi:10.1073/pnas.2414005122 | H | H (Emo-FilM Motivation 항목), M (Horikawa 신규 주석) | [BI I-3, Chain 2] |
| 57 | active inference + world model | 관찰자 예측모형의 불확실성을 arousal로 정의 | Predictable, Suddenly, Alert 평정과 EDA, insula 반응 | Emo-FilM, Spacetop | arXiv:2407.02474, arXiv:2305.11772 | H | M | [BI I-4, Chain 5] |
| 58 | 계산 인지신경과학 | 다중 과제 최적화와 특화 창발, lesion | 정서 전용 하위체계가 최적화에서 생기는가 | Horikawa | doi:10.1126/sciadv.abl8913, doi:10.1371/journal.pcbi.1011943 | H | M (C&K와 독립인 정서 학습 자료 필요) | [BI I-5, Chain 6] |
| 59 | Connectomics | connectome-constrained 모형 | 개인 DWI 제약이 정서 경로 반응 예측을 개선하는가 | Spacetop (DWI) | doi:10.1038/s41586-024-07939-3 | H | M | [BI I-6] |
| 60 | 계산 동물행동학 | pose 기반 자동 ethogram | 화면 속 행동(portrayed)과 유발 정서(evoked)의 feature 수준 분리 | Horikawa, Emo-FilM, Spacetop | doi:10.1016/j.neuron.2021.05.021, doi:10.7554/eLife.75027 | H | H | [BI I-7] |
| 61 | 능동 지각 | 예측 saliency 모델 | Horikawa 원 저자가 남긴 시선 교란 통제 | Horikawa, NSD | arXiv:2105.12441 | H | H | [BI I-8] |
| 62 | 항상성 RL | homeostatic 편차 모형 | 생리 기반 정서와 사회, 미적 정서의 구분 | Emo-FilM | doi:10.7554/eLife.04811 | H | H | [BI I-9] |
| 63 | 언어학, 정보이론 | information bottleneck 명명 효율 | 정서 범주 체계(6, 13, 27, 34개)가 뇌 공유 정서 공간에 대해 IB 최적인가 | Horikawa, Emo-FilM | doi:10.1073/pnas.1800521115 | H | H | [GI I6, C7] |
| 64 | 최적 수송 | unbalanced Gromov-Wasserstein | 개인 특이성 지수(미운반 질량), 무음 vs 소리 데이터셋 고유 영역 | Spacetop, Horikawa x Emo-FilM | arXiv:2206.09398 | H | M | [GI I7] |
| 65 | 생성 모델 평가 | prior-vs-evidence 분해 | 재구성, 캡션 출력의 정서 중 뇌 증거 몫과 생성 prior 몫 | Horikawa | doi:10.1126/sciadv.adw1464 | H | M | [VD I2] |

---

## 2. Affective Neuroscience → 다른 분야 (역방향)

| # | Target field | Exported asset | 내용 | Potential dataset | Evidence | Novelty | Feasibility | 출처 |
|---|---|---|---|---|---|---|---|---|
| R1 | NLP, LLM 평가 | 라벨 관점 벤치마크 | 같은 자극에 별도 평정자 규범, 본인 보고, 타인 지각이 있는 구조로 LLM-as-judge가 어느 관점을 대체하는지 검정 | Emo-FilM, Spacetop, Horikawa | arXiv:2501.10970, arXiv:2408.13718 | H | H | [AR I8] |
| R2 | AI 평가 | MLLM의 portrayed / 보통 사람 felt / 규범 정서 구분 평가 | 세 질문의 답 차이가 인간 felt-perceived 차이 구조와 같은지 | Horikawa, Emo-FilM | doi:10.1162/imag_a_00517, doi:10.1073/pnas.1702247114 | H | H | [ET T7] |
| R3 | AI interpretability | 뇌 기반 외부 타당도 | AI 정서 vector의 타당성을 뇌 반응 예측력과 범주성 지표로 평가 | Horikawa, Emo-FilM | arXiv:2508.05880, arXiv:2604.07729 | H | H | [FA T8; LS I6] |
| R4 | World model 평가 | 정서 기대 위반(VoE) 벤치마크 | world model이 사회, 정서적 규칙성을 학습하는가 | 신규 자극 편집과 수집 | arXiv:2502.11831 | H | L | [FA T9] |
| R5 | NeuroAI benchmark | 정서를 OOD 축으로 한 encoder 일반화 평가 | foundation encoder의 일반화 실패가 정서 내용에 집중되는가 | Horikawa, Emo-FilM | arXiv:2501.00504 | H | H | [EF I7] |
| R6 | 뇌 해독, BCI 평가 | 재구성 정서 충실도 지표 | 의미, 저수준 지표뿐인 재구성 평가에 정서 평가기와 평가기 간 불일치 추가 | Horikawa, NSD | arXiv:2403.11207, arXiv:2307.07961 | H | H | [VD I1] |
| R7 | 계산정신의학 | 정서 주석 기반 "진단적 순간" 설계, 회상 재활성 기준선 | 개인차가 최대인 순간의 appraisal 특성으로 임상 영화 fMRI 자극 설계 원리 제공 | Emo-FilM (임상군 없음, 기준선 단계) | doi:10.1002/hbm.70617, arXiv:2506.06898 | H | M | [SN I7; VD I3] |
| R8 | fMRI 방법론 일반 | 획득 물리 감사 표준 | MB, TE에 따른 영역별 검출력 지도를 "어디에 표상되는가" 주장의 표준 보고 항목으로 | 4개 모두 | doi:10.1016/j.neuroimage.2021.118617 | M | H | [SN I8] |

---

## 3. 관찰과 Stage 3로 넘길 점

1. **가장 많이 겹친 수입 기술:** controversial selection(행 10, 12, 13), 피험자 간 공유 스펙트럼(행 9, 29), successor representation과 동역학 비교(행 16, 17, 41, 43), surrogate 라벨 통계(행 1, 2, 54). 여러 에이전트가 독립적으로 같은 기술을 제안했으므로 Stage 3 Round 2에서 한 질문으로 합치거나 역할을 나눌 후보다.
2. **Novelty H이면서 Feasibility H로 시작하는 행이 73개 중 39개다.** 4개 데이터셋 원본을 모두 보유한다는 사용자 확인 덕분이다. 그러나 Novelty는 Round 1 검색 범위 기준이므로 Stage 4 선행연구 중복 감사가 반드시 필요하다.
3. **신규 수집이 필요한 행(Feasibility L)은 3개뿐이다**(행 12의 in vivo 검증, 행 36, R4). 대부분의 기회는 기존 데이터 재분석과 in-silico 모델 실험(R0~R1)이며, 인과 결론(R3 이상)으로 가려면 신규 fMRI가 필요하다는 점을 질문 단계에서 명시해야 한다(Deliverable B 0.2절 evidence-level).
4. **누수 경고:** EmoNet(doi:10.1126/sciadv.aaw4358)을 Horikawa 분석의 feature나 평가기로 쓰는 행은 없도록 했다. 행 11, 58은 EmoNet과 독립인 정서 학습 자료가 필요하다.
5. **라이선스:** TRIBE v2(CC BY-NC 4.0), jepa-intuitive-physics(CC-BY-NC) 등 비상업 조건이 있다. 연구 목적 사용은 가능하나 산출물 공개 조건을 확인해야 한다(Deliverable B, frontier-ai round1.md 2절).
