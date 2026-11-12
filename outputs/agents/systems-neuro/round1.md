# systems-neuro Round 1: Independent Discovery

* 작성: systems-neuro (Agent 8, Systems & Network Neuroscience)
* 기준일: 2026-11-12
* 담당: 주 Axis **E Neural Targets**, 외부 분야 **Computational Psychiatry**
* 따른 절차: `reference/protocols.md` P1
* 읽은 파일: `CLAUDE.md`, `reference/protocols.md`, `reference/axes.md`, `reference/starting_papers.md`, `reference/existing_projects.md`, `reference/datasets_and_resources.md`, `outputs/stage1/dataset_intelligence_report.md`, `outputs/stage1/gate_decision.md`, `outputs/STAGE_STATUS.md`(사용자 결정 기록 포함), 데이터셋별 보고서 4개의 피질하, 생리 관련 절. 다른 에이전트 폴더는 읽지 않았다.
* 문헌: `outputs/agents/systems-neuro/literature.jsonl` 42편. 전부 식별자 경로(Crossref 39, arXiv 2, PMLR 1)로 존재 확인. 본문(Discussion/Limitations 등) 직접 열람 19편, 초록 원문 21편, 미열람 2편. 2024~2026년 19편. Affective Neuroscience 밖 분야 15편 이상(신경영상 생리, MR 방법, network neuroscience, 계산정신의학, ML).
* 접근 제약(사실 기록): PMC 웹은 연속 요청 후 reCAPTCHA를 반환해 이후 PubMed MCP 전문 도구로 읽었다. nature.com 직접 열람은 하지 않았다. bioRxiv는 429, OpenReview PDF는 403이라 해당 preprint 2편(Zaffina 2026, Bhattacharyya 2026)과 BrainLM은 초록 수준 이하로만 다뤘다(BrainLM은 문헌 기록에서 제외).
* 표기: 문헌 ID는 `literature.jsonl`의 `id`. 원본 자극 필요 여부는 사용자 결정(4개 데이터셋 모두 보유)에 따라 "G1 필요(보유)"로 표시한다.

---

## 0. 요약

1. **피질하 분석 가능성은 데이터셋마다 다르고, 어느 것도 '그대로' 충분하지 않다.** NSD(7T, 1.8 mm)가 해상도는 가장 좋지만 반복 제시와 기억 과제가 amygdala 신호를 비정상적으로 만든다. Spacetop은 Kragel 2021이 colliculus-pulvinar-amygdala 경로를 찾은 3T 프로토콜과 **획득 조건이 같다**(TR 0.46 s, MB8, 2.7 mm, TE 27.2 ms). Emo-FilM은 유일하게 공개 생리 신호가 있지만 제공 전처리본(6 mm smoothing, WM/CSF 회귀)으로는 피질하와 신체-뇌 질문을 다룰 수 없다. Horikawa는 생리가 없고 TE가 길다(43 ms). 0.5절에 판정표를 둔다.
2. **network 수준 arousal 판독이 신경 신호인지 전신 자율신경-혈관 신호인지 분리되지 않았다.** Ke 2025(공개 가중치)와 Zaffina 2026(preprint)은 FC가 arousal을 데이터셋 간에 잘 옮긴다고 보고했고, Bolt 2025는 전역 fMRI 신호가 교감 각성과 결합해 저주파 분산의 약 25%를 차지함을 보였다. Bhattacharyya 2026(preprint)이 '공유'를 보였지만 '분리'는 남아 있다. Emo-FilM 생리 신호로 직접 검증 가능하다(체인 1).
3. **Horikawa 2020과 Westlin 2025의 불일치는 network subspace 문제로 재정의할 수 있다.** Westlin의 whole-brain 비지도 군집은 정서 평정보다 session/run과 10배 이상 더 많은 정보를 공유했다(NMI 0.19 vs 0.014). 전역/감각 분산을 분리한 network별 분석으로 두 결론이 갈리는 지점을 찾을 수 있다(체인 2).
4. **계산정신의학의 energy landscape 연구는 모두 휴지기다.** 정서 영화라는 '통제된 맥락'에서 상태 전이의 관성(inertia)을 측정하는 질문은 미수행이다(체인 5).
5. Discussion-to-Research chain 7개, 새 Sub-axis 6개, Axis E 재구성안을 제시한다.

---

## 0.5 데이터 조건 점검: 피질하 구조와 생리 신호

근거: Stage 1 데이터셋 보고서의 획득 파라미터, 아래 문헌. 직접 tSNR이나 dropout을 계산하지는 않았으므로 모든 판정은 **조건부**이며, 첫 작업은 raw로 영역별 tSNR, dropout 지도를 만드는 것이다.

### 0.5.1 피질하(amygdala 등) 분석 적합성

| 데이터셋 | 관련 획득 조건 (Stage 1) | 피질하에 유리한 점 | 불리한 점 | 판정 |
|---|---|---|---|---|
| Horikawa | 3T Verio, 2 mm, TR 2 s, **TE 43 ms**, MB4, 전뇌. 공개 전처리본은 비디오 블록 평균, native volume, 피질하 ROI 10개(amygdala, hypothalamus, brainstem 등) 포함 | 1인당 약 8시간이라 개인 수준 정밀 분석이 가능(Dense Amygdala 2026이 3명으로 같은 전략). 원 논문이 amygdala 포함 피질하 10개 중 9개에서 범주 모델 우세를 보고(doi:10.1016/j.isci.2020.101060 Results) | 3T에서 TE 43 ms는 흔한 30 ms 안팎보다 길어 감수성 신호 손실(안와전두, 측두극, amygdala 인접부)이 커질 수 있다(**물리 원리 기반 추론, 이 데이터에서 미확인**). 생리 신호가 없어 심장, 호흡 잡음 보정 불가(Bolt 2025, Tyszka 2026이 보인 혈관성 혼입 위험). 블록 평균이라 시계열 경로 분석 불가(raw 재전처리 필요) | amygdala **ROI 수준은 조건부 가능**(개인별 dropout 확인 후). SC, pulvinar, brainstem 핵 수준은 **부적합에 가까움** |
| Emo-FilM | 3T TIM Trio, 2.5 mm, TR 1.3 s, TE 30 ms, MB3. 제공 전처리본은 6 mm smoothing + WM/CSF/motion 회귀 | 공개 생리(PPG, 호흡, EDA 1000 Hz, 전 런)로 RETROICOR류 보정과 생리 결합 분석 가능. 낮은 MB 계수 | 6 mm smoothing은 amygdala와 hippocampus 경계 신호를 섞는다. Ma & Kragel 2026은 이 전처리본을 썼고 entorhinal 신호가 약했다(영상화 어려움 가능성, Discussion 3째 단락). 제공본에 생리 회귀자 파일이 없다(Stage 1) | raw 재전처리(작은 smoothing, 생리 회귀) 시 **amygdala ROI 수준 가능**. 소핵 수준은 어려움 |
| Spacetop | 3T Prisma, 2.7 mm, **TR 0.46 s, MB8**, TE 27.2 ms. fMRIPrep 파생본(volume + CIFTI) | **Kragel 2021 Expt2와 같은 획득 조건**에서 MPathI가 SC-pulvinar-amygdala 경로를 식별했다(doi:10.1016/j.neuron.2021.06.001). 짧은 TR로 심장 aliasing이 BOLD 대역과 떨어진다(Tyszka 2026의 TR 0.556 s 논리 준용) | 높은 MB 계수는 뇌 중심부 시간 잡음을 키워 피질하 검출력을 떨어뜨린다(Srirangarajan 2021). Kragel 2021도 amygdala 효과 크기가 가장 작았다. 공개 생리 없음. 호흡성 pseudo-motion이 FD를 부풀림(Stage 1) | 영역 평균 연결성은 **취약**, 패턴 기반 경로 분석은 **선례가 있어 가능** |
| NSD | 7T, 1.8 mm, TR 1.6 s. GLMsingle single-trial beta. TE는 Stage 1에서 미확인 | 해상도 최고. Tian 2020은 7T로 amygdala, hippocampus 세분을 보였다(doi:10.1038/s41593-020-00711-6 초록) | 이미지당 3회 반복 + old/new 과제. amygdala처럼 novelty 민감 영역은 반복에서 반응이 비정상적이어서 voxel-wise 모델 적합이 어렵다(doi:10.1038/s41467-024-49073-8 Discussion 6째 단락). 7T 감수성 왜곡 확인 필요. NSD amygdala 정서 분석 선행 미발견(Stage 1) | **해상도는 충분, 해석 confound가 큼**. 반복 감쇠 자체를 모델링하는 질문에 적합(체인 4) |

외부 기준선: Dense Amygdala(doi:10.1038/s41597-026-07065-x)는 amygdala 최적화 slab(2.0 mm, TR 556 ms)에서도 피질하 median tSFNR이 약 15~30으로 피질(약 30)보다 낮고, amygdala dropout의 개인차가 가장 컸다(Technical Validation). 이보다 불리한 조건인 우리 네 데이터셋에서 amygdala 결과를 낼 때는 **개인별 dropout 마스크와 tSNR 보고가 최소 조건**이다.

### 0.5.2 생리 신호와 신체 상태-뇌 결합 질문 적합성

| 데이터셋 | 생리 신호 | 결합 질문 사용 가능성 | 주의 |
|---|---|---|---|
| Emo-FilM | PPG, 호흡, EDA 1000 Hz, 전 런, 공개. peakdet 처리 객체와 QC 있음 | **가능 (네 데이터셋 중 유일하게 즉시 가능)** | 생리는 fMRI 참가자, 정서 평정은 별도 평정자(주체 불일치). 평정 항목 중 Heartrate, Breathing, Muscle 등 '보고된 생리'는 평정자의 것. EDA 전처리 서술 없음. 생리 파일의 StartTime 부호가 BIDS 관례와 달라 정렬 확인 필요(Stage 1) |
| Spacetop | EDA, PPG 기록(2000 Hz), **공개본에 없음** | 조건부. 사용자가 "전부 보유"라고 답했으나 생리 포함 여부는 미확인(STAGE_STATUS 결정 기록) | 입수되면 같은 참가자의 본인 평정 + 열 통증 + 영상 + 생리라는 드문 조합 |
| NSD | pulse, 호흡(참가자당 약 10 세션), eye tracking 일부. [검색] 수준 | 조건부. 세션 일부만 | 기억 과제의 각성 신호와 정서 각성이 섞임 |
| Horikawa | 없음 | 불가 | 체인 2처럼 '생리 대체 지표'로 전역 신호를 쓰는 분석만 가능하며, 그것은 생리 측정이 아니다 |

---

## 1. 중요한 미해결 문제

### U1. 정서 신호는 whole-brain 분산의 어느 subspace에 있는가 (localized vs distributed의 측정 문제)
* Horikawa 2020은 정서가 DMN 중심의 분산 network에서 정서마다 다른 'mode'로 표상된다고 결론냈다(Discussion 2~3째 단락). Westlin 2025는 whole-brain PCA(279성분) + GMM에서 그 대응을 관찰하지 못했고, 군집은 session(NMI 0.188), run(0.172)과 정서 평정(0.014)보다 훨씬 많은 정보를 공유했다(Results).
* Bolt 2025는 전역 성분이 저주파 fMRI 분산의 약 25%이며 감각운동 피질에서 먼저 나타난다고 보였다(Discussion 11, 13째 단락). whole-brain 최대 분산 축이 정서와 무관한 전역, 감각, 세션 성분으로 채워질 가능성은 검증되지 않았다.
* 근거: doi:10.1016/j.isci.2020.101060, arXiv:2507.00320, doi:10.1038/s41593-025-01945-y, doi:10.1162/imag_a_00138, doi:10.1126/sciadv.abf7129

### U2. network 수준 arousal 판독은 신경 정서 신호인가, 전신 자율신경-혈관 신호인가
* Ke 2025: dynamic FC CPM이 arousal을 4개 영화 데이터셋 간에 일반화, valence는 실패. 정서 arousal과 각성도, 자율 arousal의 관계는 불명이라고 명시(Discussion 9째 단락).
* Zaffina 2026(preprint, 초록): pairwise FC가 '이식 가능한 arousal 판독', 세밀한 정서 profile은 higher-order topology.
* Young 2017(초록): salience network 응집이 심박과 단조 증가. 생리 잡음 처리 방식은 초록에서 확인 불가.
* Bolt 2025: 전역 신호와 심박, 호흡량, PPG 진폭이 정해진 순서로 공변. Bhattacharyya 2026(preprint, 초록): 정서, 자율, 각성도 arousal 모델의 교차 일반화. **공유는 보였지만 정서 특이 성분이 남는지는 미해결.**
* 근거: doi:10.1371/journal.pcbi.1012994, doi:10.64898/2026.09.26.754452, doi:10.1523/JNEUROSCI.1759-16.2016, doi:10.1038/s41593-025-01945-y, doi:10.64898/2026.06.08.730730

### U3. 피질하 정서 경로는 자연 자극에서도 기능하는가, 그리고 측정할 수 있는가
* Kragel 2021: SC-pulvinar-amygdala 경로가 이미지, 소리의 규범적 혐오도를 추적하지만 통증, 긍정 자극에는 반응하지 않음. 영역 평균 연결성으로는 보이지 않음. 의식 경험과의 관계는 추가 연구 필요(Results 말미 'multiple roads' 단락).
* Morgenroth 2023: film fMRI network 분석은 표면 기반 피질 중심이라 피질하를 소홀히 하며, 기술 개발이 필요(한계 절).
* Abdel-Ghaffar 2024: 반복 제시에서 amygdala 반응이 비정상적이라 voxel-wise 모델 적합이 어렵다(Discussion 6째 단락). Srirangarajan 2021: multiband가 중심부 피질하 검출력을 떨어뜨림.
* 근거: doi:10.1016/j.neuron.2021.06.001, doi:10.1093/scan/nsad063, doi:10.1038/s41467-024-49073-8, doi:10.1016/j.neuroimage.2021.118617, doi:10.1038/s41597-026-07065-x

### U4. 정서 정보의 transmodal 위치는 정서 고유 속성인가, 시간 적분 위계의 부산물인가
* Horikawa 2020: 시각에서 의미, 정서로 principal gradient를 따라 표상이 이동(Discussion 5째 단락).
* Ma & Kragel 2026: vmPFC가 큰 척도 layer g를 더 잘 읽는 것은 긴 시간 적분 창과 부합(Discussion 3째 단락). 사랑, 만족, 죄책감은 전측 hippocampus에서 더 잘 decoding되며 더 긴 시간 척도와 관련될 수 있음(4째 단락).
* Chang 2021: vmPFC 패턴은 수십 초~분 단위로 안정(Discussion 3째 단락). Lettieri 2021(초록): chronotopic 연결 지도.
* 정서 정보의 gradient 위치와 정서 항목 자체의 시간 척도가 교락되어 있는지 직접 검증한 연구는 이번 검색에서 찾지 못했다(Lettieri 2021이 부분 선행).
* 근거: doi:10.1016/j.isci.2020.101060, doi:10.1038/s41467-025-68240-z, doi:10.1126/sciadv.abf7129, doi:10.1093/scan/nsab112, doi:10.1073/pnas.1608282113

### U5. 소표본 정서 fMRI에서 계산정신의학적 표현형을 어떻게 얻는가
* Marek 2022(초록): 표본 중앙값 약 25명 수준의 뇌-행동 상관은 재현되기 어렵다. Horikawa 5명, Emo-FilM 30명.
* Finn 2018, Gruskin 2020, Chan 2026, Scatolin 2026, Kirk 2026은 자연 정서 자극이 개인차(편집증, 우울, 불안, 내재화)를 드러낸다고 보고. Gruskin 2020은 효과가 **덜 정서적인 순간**에 더 컸다.
* Hitchcock 2022: 정신건강 문제는 맥락 속 시간 동역학으로 모델링해야 한다(3절). 그런데 energy landscape 기반 정신의학 연구(Ishida 2024, Wang 2026)는 모두 휴지기이고, 영화 energy landscape(Liu 2025 preprint)는 정서 변수를 쓰지 않았다.
* 근거: doi:10.1038/s41586-022-04492-9, doi:10.1038/s41467-018-04387-2, doi:10.1016/j.neuroimage.2019.116217, doi:10.1002/hbm.70617, doi:10.1146/annurev-psych-021621-124910, doi:10.1016/j.nicl.2024.103574, doi:10.1016/j.jad.2026.121407, doi:10.64898/2025.11.30.691450

### U6. 규범 평정과 참가자 본인 경험 중 무엇이 network 신호를 결정하는가
* Ke 2025: valence 실패의 한 원인으로 별도 집단 평균 평정이 개인 경험을 대표하지 못할 가능성(Discussion 10째 단락).
* Kragel 2021: 경로 mediation은 규범 혐오도에서는 이미지와 소리 모두, 본인 실시간 평정에서는 소리만 유의.
* Horikawa 2020 Limitations 1째 단락, Ma & Kragel 2026 Discussion 2째 단락(독립 관찰자 평정).
* 근거: doi:10.1371/journal.pcbi.1012994, doi:10.1016/j.neuron.2021.06.001, doi:10.1016/j.isci.2020.101060, doi:10.1038/s41467-025-68240-z

### U7. 정서 관련 network 동역학은 drift인가, 이산 상태 전환인가
* Chang 2021: vmPFC가 점진적으로 drift하는지 state-like인지 구분 불가, hybrid 모델 필요(Discussion 4째 단락).
* Ma & Kragel 2026: graph-like와 map-like 표상의 관계는 열린 문제(Discussion 6째 단락).
* Tambini 2017(초록): 정서 뇌 상태가 수십 분 이월된다. Houben 2015(초록): 정서 관성은 낮은 안녕과 관련.
* 근거: doi:10.1126/sciadv.abf7129, doi:10.1038/s41467-025-68240-z, doi:10.1038/nn.4468, doi:10.1037/a0038822, pmlr:v54/linderman17a

---

## 2. 주목할 모델 또는 방법론

| # | 모델/방법 | 근거 ID | Pretrained weights | Input | Output | 학습 목표 | 라이선스 |
|---|---|---|---|---|---|---|---|
| M1 | **MPathI** (Multivariate Pathway Identification) | doi:10.1016/j.neuron.2021.06.001 | 학습형 대형 모델은 아님. 논문이 MATLAB 코드 공개를 명시. 경로 패턴(가중치) 공개 여부 **미확인** | 두 영역의 voxel 패턴(single-trial beta 또는 시계열) | 영역별 latent 패턴, 교차검증 경로 연결 강도 | PLS(SIMPLS)로 두 블록 공분산 최대화, leave-one-subject-out | 미확인 |
| M2 | **arousal CPM** (dynamic FC connectome predictive model) | doi:10.1371/journal.pcbi.1012994 | **공개**(논문 Discussion 3째 단락: 학습 가중치와 스크립트 공개) | 122 parcel BOLD의 45초 tapered window dynamic FC | 순간 arousal 예측 시계열 | edge 선택 + 선형 회귀 | 미확인(저장소 미열람) |
| M3 | **Brain-JEPA** | arXiv:2409.19407 | 코드 GitHub 공개 명시. 체크포인트 공개 여부 **미확인** | 450 ROI(Schaefer-400 + Tian-Scale III) x 160 timestep | ROI/시간 패치 latent | JEPA 잠재 예측, gradient 위치 부호화, spatiotemporal masking. UK Biobank 휴지기 사전학습 | 미확인 |
| M4 | **Energy landscape** (pairwise maximum entropy) | doi:10.1016/j.nicl.2024.103574, doi:10.1016/j.jad.2026.121407, doi:10.64898/2025.11.30.691450 | 해당 없음 | 이진화한 network 활성 벡터 | 상태 에너지, attractor basin, 전이 경로 비용 | 최대 엔트로피 적합 | 해당 없음 |
| M5 | **rSLDS** (recurrent switching linear dynamical system) | pmlr:v54/linderman17a | 해당 없음 | 저차원 잠재 시계열(network 성분) | 이산 상태열 + 상태별 선형 동역학, 상태 의존 전환 확률 | 베이지안 추론(Polya-gamma MCMC) | 구현 라이브러리 라이선스 미확인 |
| M6 | **Higher-order topology** (homological scaffold) | doi:10.64898/2026.09.26.754452 | 해당 없음 | 시변 fMRI | 고차 상호작용 scaffold 시계열 | 위상 계산 | 미확인 (preprint) |
| M7 | **전역 신호-생리 결합 모델** (complex PCA, PPG 진폭 교차상관, multi-echo T2*/S0) | doi:10.1038/s41593-025-01945-y | 해당 없음 | BOLD + 심박, 호흡량, PPG 진폭, EDA | 전역 시공간 성분과 지연 구조 | CPCA | 해당 없음 |
| M8 | **Tian subcortex atlas** (S1~S4, 7T 세분) | doi:10.1038/s41593-020-00711-6 | atlas 공개(Brain-JEPA가 Scale III를 사용) | - | 피질하 parcel, 피질하 gradient | 연결 gradient | 미확인 |
| M9 | **HMM 상태 분할 + 공간 자기상관** | doi:10.1126/sciadv.abf7129 | 해당 없음 | ROI 공간 패턴 시계열 | 개인별 잠재 상태, 상태 동기화 | HMM | 해당 없음 |
| M10 | **ICA-FIX 기반 생리 잡음 분류** | doi:10.1038/s41597-026-07065-x | 데이터 특이 분류기(공개 여부는 ds006947 코드 폴더 기준, 미열람) | 런별 ICA 성분 | 신경혈관 vs 잡음 성분 | 수동 분류 학습 | CC0(데이터) |

---

## 3. 다른 분야에서 가져와 적용할 수 있는 연구 아이디어

* **I1. Affective normative modeling (계산정신의학 → 정서 신경과학).** 규범 모델링(doi:10.1038/s41380-019-0441-1, 본문 미열람)의 틀로 같은 영상에 대한 network 궤적의 집단 규범 분포를 만들고, 개인 편차 점수를 표현형으로 쓴다. Spacetop(약 100명, 같은 영상, 같은 순서)은 참가자 본인 평정이 있어 '뇌 편차가 평정 편차를 예측하는가'를 검증할 수 있다. 근거: doi:10.1146/annurev-psych-021621-124910, doi:10.1038/s41467-018-04387-2.
* **I2. 휴지기 정신의학 energy landscape → 자극 유발 정서 landscape.** 정서 주석이 있는 Emo-FilM에서 landscape를 적합하고, 정서 장면이 어떤 basin과 전이 경로를 쓰는지 기술한다. 근거: doi:10.1016/j.nicl.2024.103574, doi:10.1016/j.jad.2026.121407, doi:10.64898/2025.11.30.691450.
* **I3. 동물 회로 수준 경로 식별 → 자연 영상.** MPathI를 Spacetop 영상에 전향 적용하고 같은 참가자의 열 통증을 음성 대조로 쓴다. 근거: doi:10.1016/j.neuron.2021.06.001.
* **I4. 전역 신호 생리학 → 정서의 '신체 상태 채널'.** 전역 성분과 생리 결합 지표를 nuisance가 아니라 정서 상태 feature로 다룬다. 근거: doi:10.1038/s41593-025-01945-y, doi:10.1038/s41562-017-0069, doi:10.1162/imag_a_00138.
* **I5. 임상용 brain foundation model → 정서 상태 탐침.** 휴지기 사전학습 latent에 정서 정보가 있는지, 피질하 토큰 의존도가 어떤지 본다. 근거: arXiv:2409.19407.
* **I6. ML의 switching dynamical system → 정서 관성.** rSLDS의 상태 의존 전환 확률로 '부정 정서 상태에서 빠져나오기 어려움'을 정량화한다. 근거: pmlr:v54/linderman17a, doi:10.1037/a0038822.
* **I7. (정서 신경과학 → 정신의학, 바깥 방향) 정서 주석 기반 '진단적 순간' 설계.** Emo-FilM 1 Hz 규범 주석으로 개인차가 최대가 되는 순간의 appraisal 특성을 찾아, 임상 영화 fMRI 'stress test' 자극 설계 원리로 제공한다. 근거: doi:10.1002/hbm.70617, doi:10.1016/j.neuroimage.2019.116217, doi:10.1038/s41467-018-04387-2.
* **I8. (바깥 방향) 획득 물리 감사.** multiband와 TE에 따른 영역별 검출력 지도를 '어디에 표상되는가' 주장의 표준 보고 항목으로 만든다. 정서 외 cross-dataset network 연구 전반에 적용 가능. 근거: doi:10.1016/j.neuroimage.2021.118617, doi:10.1038/s41597-026-07065-x.

---

## 4. 기존 Affective Neuroscience와 예상 밖으로 연결될 수 있는 개념

* **C1. 전처리가 지우는 신호가 정서의 신체 성분일 수 있다.** Emo-FilM 제공 전처리본은 WM/CSF 평균 신호를 회귀했다(Stage 1). Bolt 2025는 PPG 진폭 감소 때 WM과 CSF 신호가 회백질과 반대 부호로 움직이는 자율신경성 시공간 패턴을 보였다(Discussion 5~6째 단락). 즉 표준 nuisance 회귀가 교감 각성 성분을 부분적으로, 그리고 영역마다 다르게 제거하거나 반대로 주입할 수 있다. 이 데이터로 나온 정서 결과(예: Ma & Kragel 2026)의 일부가 전처리 선택에 의존할 가능성은 검증된 적이 없다. 근거: doi:10.1038/s41593-025-01945-y, doi:10.1038/s41467-025-68240-z, doi:10.1038/s41562-017-0069.
* **C2. 획득 물리가 '정서 지형'의 일부를 만든다.** 피질하와 안와전두의 낮은 tSNR(TE, MB 계수, 코일 거리)은 '정서는 transmodal 피질에 분산되어 있고 피질하 기여는 작다'는 결론과 같은 방향으로 작용한다. 예측: parcel별 tSNR과 '정서 고유 설명 분산'의 상관이 데이터셋 간 MB 계수 차이에 따라 달라진다면 위치 주장 일부는 측정 산물이다. 근거: doi:10.1016/j.neuroimage.2021.118617, doi:10.1038/s41597-026-07065-x, doi:10.1016/j.isci.2020.101060.
* **C3. arousal 오귀인(misattribution)의 신경 기반과 불안의 내수용 오해석.** Ke 2025는 arousal 표상이 맥락 간 같다는 결과가 Schachter-Singer류 오귀인의 신경 기반일 수 있다고 제안했다(Discussion 4째 단락). Bhattacharyya 2026(preprint)은 정서, 자율, 각성도 arousal이 FC 공간을 공유한다고 보고했다. 계산정신의학에서 공황과 불안은 신체 신호의 위협적 해석으로 설명된다. 연결 가설: 자율 arousal 판독과 정서 arousal 판독의 결합 강도가 개인마다 다르고, 결합이 강할수록 신체 각성이 정서로 쉽게 전환된다. 근거: doi:10.1371/journal.pcbi.1012994, doi:10.64898/2026.06.08.730730, doi:10.1038/s41562-017-0069.
* **C4. 정서의 '지도' 위의 '지형'.** Ma & Kragel의 hippocampus-vmPFC 정서 지도는 관계 기하이고, 정신의학 energy landscape는 상태의 안정성과 전이 비용이다. 같은 정서 공간 좌표 위에 dwell time과 전이 에너지를 덧씌우면 '어느 정서 위치가 깊은 basin인가'를 물을 수 있다. 근거: doi:10.1038/s41467-025-68240-z, doi:10.1016/j.jad.2026.121407.
* **C5. 통증을 정서 경로의 개인 내 음성 대조로.** Kragel 2021의 low road는 열 통증에 반응하지 않았다. Spacetop은 같은 참가자가 열 통증과 정서 영상을 모두 겪어, 경로 선택성을 개인 내에서 검증할 수 있는 드문 설계다. 근거: doi:10.1016/j.neuron.2021.06.001, Stage 1 dataset_Spacetop.md.

---

## 5. 새 Sub-axis 또는 하위 연구 방향

| # | 제안 | 소속 Axis | 독립 Axis 필요 여부 | 근거 ID |
|---|---|---|---|---|
| S1 | **Pathway/Circuit-level Targets**: 영역도 network도 아닌 '영역 간 집단 대 집단 연결'을 표적으로 하는 수준 | E (F와 연결) | 불필요. E 안의 새 해상도 수준 | doi:10.1016/j.neuron.2021.06.001, doi:10.1016/j.neuroimage.2021.118800 |
| S2 | **Brain-Body Interface Targets**: 전역 자율신경 성분, 알로스타시스/내수용 시스템, 신경혈관 결합을 표적으로 | E (A의 Interoception과 공동) | 불필요하나 A와 E 사이 교차 표시 필요 | doi:10.1038/s41593-025-01945-y, doi:10.1038/s41562-017-0069, doi:10.1093/scan/nsag050 |
| S3 | **Signal-feasibility Map**: 영역별 tSNR, dropout, MB 계수, TE가 '그 영역을 표적으로 삼을 수 있는가'를 결정 | E와 Q 교차 | **독립 Axis 후보("Acquisition & Signal Physics")**. 모든 neural target 주장과 cross-dataset 비교를 제약하므로 Q의 하위로 두면 E 쪽 판단에서 누락되기 쉽다 | doi:10.1016/j.neuroimage.2021.118617, doi:10.1038/s41597-026-07065-x |
| S4 | **Network State Landscape**: attractor, dwell time, 전이 에너지, 관성 | E의 Dynamic Network Reconfiguration 세분 (D, K와 연결) | 불필요 | doi:10.1016/j.nicl.2024.103574, doi:10.1016/j.jad.2026.121407, pmlr:v54/linderman17a |
| S5 | **Idiographic Network Targets**: 개인 고유 상태 레퍼토리, 개인별 분할, 정밀 매핑 | E와 O 교차 | 불필요 | doi:10.1126/sciadv.abf7129, arXiv:2507.00320, doi:10.1038/s41597-026-07065-x |
| S6 | **Computational Psychiatry Phenotyping from Evoked Dynamics**: 규범 편차, 진단적 순간, 신경 정서 관성 | 현재 O에 들어갈 수 있음 | **독립 Axis 후보**. O는 '개인차의 표상'을 다루고, 이 방향은 '임상 표현형을 만드는 측정 설계'를 다룬다. 외부 분야(axes.md 3절)에서 들어온 축이므로 조합 단계(P5)에서 외부 개념 요건을 채우는 단위로도 유용 | doi:10.1146/annurev-psych-021621-124910, doi:10.1038/s41586-022-04492-9, doi:10.1002/hbm.70617 |

---

## 6. Discussion-to-Research chains

형식: `Original Finding → Unresolved Question → Technological Development → New Dataset / Model Combination → New Research Question`. 각 단계에 근거 ID와 원문 위치를 단다. 원문 위치가 '초록'인 것은 본문을 읽지 못한 경우다.

### Chain 1. network arousal 판독에서 자율신경 성분 분리 (Emo-FilM)

* **Original Finding:** dynamic FC 기반 arousal 모델은 영화와 표본을 넘어 일반화되고 valence는 실패한다(doi:10.1371/journal.pcbi.1012994, Discussion 1째 단락). pairwise FC가 이식 가능한 arousal 판독이다(doi:10.64898/2026.09.26.754452, 초록). salience network 응집이 심박을 따른다(doi:10.1523/JNEUROSCI.1759-16.2016, 초록).
* **Unresolved Question:** 영화 중 정서 arousal이 각성도, 자율 arousal과 어떻게 관련되는지 불명(Ke 2025 Discussion 9째 단락). 같은 참가자의 평정이 없어 개인 고유 표상을 못 봄(Discussion 7째 단락).
* **Technological Development:** 전역 fMRI 신호는 교감 매개 생리 순서(심박, 호흡량 증가 후 PPG 진폭 감소)와 결합하며 저주파 분산의 약 25%(doi:10.1038/s41593-025-01945-y, Discussion 2째, 13째 단락). 세 종류 arousal의 FC 모델이 교차 일반화(doi:10.64898/2026.06.08.730730, 초록, 부분 선행). Ke 2025 가중치 공개(Discussion 3째 단락).
* **New Dataset / Model Combination:** Emo-FilM raw BOLD(제공 전처리본의 WM/CSF 회귀를 쓰지 않는 분기 포함) + 참가자 PPG, 호흡, EDA(1000 Hz)에서 심박, 호흡량, PPG 진폭, 피부전도 수준 + 별도 평정자 1 Hz 규범 항목(Feeling: Calm, AtEase, Intense, Alert 등) + Ke 2025 공개 CPM 가중치(전향 적용) + pairwise vs higher-order 지표(Zaffina 2026 방식, 재구현 필요).
* **New Research Question:** **"정서 영화 시청 중 network 수준 arousal 판독에서 참가자 자율신경-혈관성 전역 성분을 제거한 뒤에도 규범적 정서 arousal과 appraisal(Suddenly, Urgency 등)을 예측하는 신경 성분이 남는가, 남는다면 어느 연결에 있는가?"**
* **분석과 판정 기준:** (1) Ke 가중치 그대로 적용한 예측 arousal을 규범 평정과 참가자 생리에 각각 회귀하고 commonality 분석. (2) 생리 regressor(지연 반응함수 포함)와 전역 신호를 제거한 BOLD로 CPM 재학습(leave-one-film-out). (3) 잔여 판독이 appraisal 항목을 arousal 이상으로 예측하는지. 지지: 생리 제거 후에도 규범 arousal 예측이 유의하고 SN, DMN-FPN 연결에 남음. 반증: 예측 분산 대부분이 생리 모델로 설명되고 제거 후 우연 수준. 어느 쪽이든 정서 network 연구의 해석을 바꾼다.
* **Safeguards:** 슬라이딩 창과 HRF 합성곱이 만드는 자기상관 때문에 위상 무작위화 또는 circular shift null 필요. 평정자와 참가자, 평정자가 '보고한 생리'와 참가자 '측정 생리'의 주체 불일치. movie-level leakage는 leave-one-film-out. 다중비교는 network 쌍 수준 요약으로 제한. decodability를 '정서 경험 판독'으로 해석하지 않는다.
* G1: 불필요. already_done: partially (doi:10.64898/2026.06.08.730730는 공유를 보였고 분리는 보이지 않음, 초록 기준). overlap: Emo-FilM 연구 (같은 데이터셋. 정서 맥락, 시간 정보 기여 분석과 일부 겹칠 수 있음).

### Chain 2. Horikawa와 Westlin의 불일치를 network subspace로 분해 (Horikawa)

* **Original Finding:** 정서는 DMN 중심 분산 network의 서로 다른 mode로 표상되고, 표상은 principal gradient를 따라 시각, 의미, 정서로 이동한다(doi:10.1016/j.isci.2020.101060, Discussion 2~3째, 5째 단락).
* **Unresolved Question:** 최소 가정 whole-brain 비지도 분석에서는 범주 대응이 관찰되지 않고 개인별 군집 수가 11~14로 다르다. 군집은 정서(NMI 0.014)보다 session(0.188), run(0.172)과 더 많은 정보를 공유한다(arXiv:2507.00320, Results). 저자들은 multiverse와 대안 모델 비교를 요청했다(Discussion 'Future studies' 단락). 평정 주체 불일치(Horikawa Limitations 1째 단락).
* **Technological Development:** 전역 성분의 자율신경 기원과 감각운동 피질 선행(doi:10.1038/s41593-025-01945-y, Discussion 11, 13째 단락). transmodal 영역의 개인 고유 상태를 다루는 상태 기반 틀(doi:10.1126/sciadv.abf7129, Discussion 5째 단락). 피질하를 라벨과 독립적으로 정의하는 atlas(doi:10.1038/s41593-020-00711-6, 초록).
* **New Dataset / Model Combination:** Horikawa ds002425 raw(CC0) 재전처리. network별(시각, 체감각운동, DAN, SN/VAN, FPN, DMN 하위계, Tian 피질하) subspace에서 Westlin 파이프라인(PCA→GMM, BIC)과 Horikawa 파이프라인(지도 encoding/decoding)을 같은 CV로 실행. multiverse 요인: 전역 신호 제거 여부, session/run 평균 제거 여부, voxel 선택 없음 vs 학습 fold 내 선택, 군집 수 BIC vs 고정. 대안 설명 변수로 video foundation model feature(G1 보유) 추가.
* **New Research Question:** **"Horikawa 데이터에서 정서 범주 구조가 관찰되는지는 어느 network subspace를 보는가와 전역/세션 분산을 어떻게 다루는가에 따라 체계적으로 달라지는가, 그리고 전역/감각 분산을 분리한 transmodal subspace에서는 비지도 군집도 규범 정서 평정과 정렬되는가?"**
* **판정 기준:** 지지(화해 가설): 전역+세션 제거 후 DMN, SN subspace에서 정서 NMI가 크게 오르고 시각 network 군집은 시각 feature를 따름. 반증: 모든 subspace에서 정서 NMI가 0 근처로 유지되면 Westlin 결론이 강화되고, 원 논문의 지도 학습 대응은 '군집형 유형'이 아닌 약한 분산 신호들의 합으로 재해석해야 함.
* **Safeguards:** voxel 선택은 학습 fold 안에서만(circular inference). 5명이므로 참가자별 결과를 모두 보고. 반복 제시가 없어 noise ceiling 대신 중복 15쌍과 ISC 대체 지표(Stage 1). 라벨은 규범 평정. 전역 신호 제거 자체가 정서 관련 분산을 지울 수 있으므로 제거 전후를 모두 보고.
* G1: 핵심 분석 불필요, 대안 feature는 필요(보유). already_done: no (Westlin은 whole-brain만, 이번 검색에서 network별 재분석 미발견). overlap: EmoViS (Horikawa 2020 사용, affective brain geometry의 기원 질문과 일부 겹침).

### Chain 3. colliculus-pulvinar-amygdala 경로의 자연 영상 전이와 개인 내 선택성 (Spacetop)

* **Original Finding:** SC-pulvinar-amygdala 경로는 이미지와 소리의 규범 혐오도를 추적하지만 열, 기계 통증과 긍정 이미지에는 반응하지 않으며, 영역 평균 연결성으로는 보이지 않는다. 3T MB8 TR 460 ms에서도 식별(doi:10.1016/j.neuron.2021.06.001, Results와 Methods Expt2).
* **Unresolved Question:** 경로와 의식적 정서 경험의 관계, 그리고 경로들이 함께 주관 경험에 어떻게 관여하는지는 추가 연구 필요(같은 논문, 'multiple roads' 단락과 마지막 요약 단락). film fMRI는 피질하를 소홀히 했다(doi:10.1093/scan/nsad063, 'White noise' 절 마지막 2단락).
* **Technological Development:** Spacetop이 Expt2와 같은 획득 조건(Stage 1 dataset_Spacetop.md 1절). 원본 영상 보유로 프레임 단위 운동, 확장 흐름(looming), 저공간주파수 에너지를 추출 가능. 피질하 atlas(doi:10.1038/s41593-020-00711-6). multiband 중심부 잡음 진단 절차(doi:10.1016/j.neuroimage.2021.118617, Discussion 6째 단락).
* **New Dataset / Model Combination:** Spacetop alignvideo(자연 영상, 본인 사후 평정) + social 과제 열 통증 + faces, 같은 참가자. MPathI 재추정(Kragel 패턴 공개 시 전향 적용) + 영상 feature 시계열 + 본인 'afraid', 'disgusted' 평정.
* **New Research Question:** **"같은 참가자 안에서 colliculus-pulvinar-amygdala 경로 활동은 자연 영상의 위협 관련 시각 동역학(looming, 저공간주파수 운동)을 시간 단위로 따라가면서 열 통증에는 반응하지 않는 선택성을 유지하는가, 그리고 영상 단위 본인 공포 평정을 예측하는가?"**
* **판정 기준:** 지지: 영상 feature 추적 + 열 통증 무반응. 반증 1: 열 통증에도 반응하면 경로는 위협 특이가 아니라 현저성(salience) 일반 신호. 반증 2: looming은 추적하나 본인 평정은 예측 못 하면 감각 수준 경로라는 Kragel의 규범/본인 해리와 합치.
* **Safeguards:** Spacetop 평정은 영상 종료 후 1회이고 약 51% 결측이라 시간 단위 검증은 AI 추출 feature에만 의존한다(시각 feature는 AI 추정이 아니라 계산된 물리량이지만 '위협성' 같은 의미 라벨을 쓰면 AI 추정으로 표기). MB8 중심부 tSNR을 먼저 보고. 생리 미공개라 호흡 pseudo-motion 통제 제한. mediation은 인과가 아니다. ROI는 atlas로 라벨과 독립 정의.
* G1: 필요(보유). already_done: partially (자연 영상에서 SC의 looming 부호화를 보고한 CCN 2025 초록 Thieu et al., search_index 수준. 경로 선택성의 개인 내 검증은 미발견). overlap: 없음.

### Chain 4. amygdala 'encoding 실패'를 반복 비정상성으로 재정의 (NSD)

* **Original Finding:** OTC는 의미 범주와 정서가를 결합 표상하지만 amygdala는 반복 제시에서 반응이 비정상적이어서 voxel-wise 모델 적합이 어렵다(doi:10.1038/s41467-024-49073-8, Discussion 6째 단락). 반복이 없는 Horikawa에서는 amygdala에서도 범주 모델이 차원 모델보다 우세(doi:10.1016/j.isci.2020.101060, Results).
* **Unresolved Question:** 이 실패가 amygdala에 정서 정보가 없어서인지, 정보가 '반복에 따른 변화'에 실려 있어서인지 구분되지 않았다. MTL fMRI의 저SNR, 혈관 confound, 분할 문제(doi:10.1038/s41597-026-07065-x, Usage Notes 마지막 단락).
* **Technological Development:** NSD 7T 1.8 mm single-trial beta와 이미지별 반복 번호, 간격(Stage 1). 7T 기반 amygdala 세분(doi:10.1038/s41593-020-00711-6, 초록). 원본 이미지 보유로 VLM 기반 정서 추정 가능(AI 추정 라벨).
* **New Dataset / Model Combination:** NSD + 반복 번호, 직전 제시 간격, old/new 판단을 포함한 encoding 모델 + AI 추정 각성, 사회 내용 라벨(nsdmeadows 100장의 참가자 평정으로 일부 점검) + amygdala 세분 ROI vs OTC 비교.
* **New Research Question:** **"amygdala의 첫 제시 대비 반복 감쇠량은 이미지의 (AI 추정) 각성과 사회적 내용에 따라 달라지는가, 즉 amygdala의 정서 관련 정보는 반응 크기보다 반복에 따른 변화에 실려 있는가?"**
* **판정 기준:** 지지: 감쇠 기울기가 각성/사회 내용으로 예측되고 OTC에서는 그렇지 않음. 반증: 감쇠가 정서 라벨과 무관하고 novelty와 기억 판단으로만 설명됨.
* **Safeguards:** 기억 과제의 친숙도, novelty 신호와 각성의 혼입(Stage 1 NSD 4.4절). AI 라벨은 'AI 추정 정서'로 표기하고 인간 평정 대체 근거로 쓰지 않음. NSD 이미지 valence 범위 제한. 8명. COCO 사전학습 오염(라벨 모델이 COCO로 학습되었을 가능성).
* G1: 필요(보유). already_done: partially (반복에 따른 amygdala 감쇠는 일반 문헌에 있음, search_index 수준. NSD에서 정서 라벨과 결합한 분석은 미발견). overlap: 없음.

### Chain 5. 자극 유발 network landscape와 신경 수준 정서 관성 (Emo-FilM, Spacetop)

* **Original Finding:** 휴지기 energy landscape의 attractor 안정성과 전이 경직성이 정신장애, 자살 위험과 관련(doi:10.1016/j.nicl.2024.103574, doi:10.1016/j.jad.2026.121407, 초록). 영화 시청에도 landscape가 존재하고 전이가 ISC를 예측하지만 정서 변수는 쓰지 않았다(doi:10.64898/2025.11.30.691450, 초록).
* **Unresolved Question:** 계산정신의학은 맥락 속 시간 동역학을 모델링해야 한다(doi:10.1146/annurev-psych-021621-124910, 3절 서두). vmPFC가 drift인지 state-like인지는 hybrid 모델이 필요(doi:10.1126/sciadv.abf7129, Discussion 4째 단락). graph-like와 map-like 표상의 관계(doi:10.1038/s41467-025-68240-z, Discussion 6째 단락).
* **Technological Development:** 상태 의존 전환 확률을 갖는 rSLDS(pmlr:v54/linderman17a, 6. Discussion). 행동 수준 정서 관성과 안녕의 메타분석 관계(doi:10.1037/a0038822, 초록). 정서 뇌 상태의 이월(doi:10.1038/nn.4468, 초록).
* **New Dataset / Model Combination:** Emo-FilM(30명, 14편, 1 Hz 50항목 규범 궤적, 참가자 질문지: Chan 2026 초록 기준 상태 불안, 개방성) + Spacetop(약 100명, 같은 영상 순서, 본인 평정). network 수준 시계열(Schaefer + Tian)에 rSLDS를 적합하고, 규범 정서 궤적을 외부 입력으로 넣어 '자극이 요구하는 전이'를 설명한 뒤 남는 dwell을 신경 관성으로 정의.
* **New Research Question:** **"정서 영화 시청 중 network 상태가 자극 정서 궤적이 요구하는 시점보다 늦게 이전 상태를 벗어나는 정도(신경 정서 관성)는 부정 정서 장면 이후에 커지는가, 영화를 바꿔도 개인 안에서 안정적인가?"** (개인 특성과의 상관은 효과 크기 추정 수준의 탐색으로 한정)
* **판정 기준:** 지지: 부정, 고각성 구간 이후 잔여 dwell 증가 + 영화 분할 간 개인 내 신뢰도 양호. 반증: 잔여 dwell이 HRF와 자기상관 null 분포와 구분되지 않음.
* **Safeguards:** HRF 지연과 평활이 인공 관성을 만든다(HRF 명시 모델링과 시계열 대리 null 필수). leave-one-film-out. Emo-FilM 30명, 특성 상관은 확증 불가(doi:10.1038/s41586-022-04492-9). 반대 관점으로 doi:10.1038/s41593-022-01110-9(본문 미열람, Round 2 전 확인 필요). 정서 궤적은 별도 평정자 규범값.
* G1: 불필요. already_done: no (정서 주석과 결합한 자극 유발 landscape 관성은 미발견. 영화 landscape 자체는 Liu 2025 preprint가 partially). overlap: Emo-FilM 연구 (데이터셋 겹침).

### Chain 6. transmodal 정서 위치와 시간 척도의 교락 (Horikawa x Emo-FilM)

* **Original Finding:** 정서 고유 설명 영역은 principal gradient의 transmodal 끝에 있고 표상은 시각, 의미, 정서 순으로 이동(doi:10.1016/j.isci.2020.101060, Discussion 5째 단락).
* **Unresolved Question:** vmPFC의 큰 척도 정서 신호는 긴 시간 적분 창과 부합하고(doi:10.1038/s41467-025-68240-z, Discussion 3째 단락), 사랑, 만족, 죄책감은 더 긴 시간 척도와 관련될 수 있다(4째 단락). 정서와 성분마다 시간 척도가 다르다(doi:10.1093/scan/nsad063, 'A space odyssey: temporality' 절). cross-modal 정서 표상의 심화 필요(Horikawa Discussion 9째 단락).
* **Technological Development:** chronotopic 연결 지도(doi:10.1093/scan/nsab112, 초록, 부분 선행). principal gradient 좌표(doi:10.1073/pnas.1608282113, 초록). 피질하 gradient(doi:10.1038/s41593-020-00711-6, 초록). 공통 parcel(HCP360)로 두 데이터셋 결합(Stage 1 3.3절).
* **New Dataset / Model Combination:** Emo-FilM 50항목의 주석 자기상관으로 항목별 고유 시간 척도 추정(빠른: Suddenly, Surprise / 느린: Love, WarmHeartedness 등) + parcel별 encoding + gradient 위치. Horikawa(2~10초 클립, 모든 정서가 짧은 창)와 이름 대응 범주(수준 2 비교)의 gradient 위치 비교.
* **New Research Question:** **"정서 정보가 transmodal 끝에 위치하는 정도는 정서 항목의 고유 시간 척도로 예측되는가, 같은 이름의 정서가 짧은 무음 클립(Horikawa)에서는 gradient 중간에, 긴 소리 있는 영화(Emo-FilM)에서는 transmodal 끝에 표상되는가?"**
* **판정 기준:** 지지(교락 가설): 항목 시간 척도가 gradient 위치를 예측하고 데이터셋 간 위치 이동이 자극 길이로 설명됨. 반증: 시간 척도를 통제해도 정서 항목이 transmodal 끝에 남으면 정서 고유 추상화.
* **Safeguards:** 데이터셋 간 참가자, 스캐너, 라벨 척도가 달라(수준 2) 위치 비교는 순위 수준으로 제한. 시간 척도와 의미 내용의 공선성. ROI는 gradient 좌표로 사전 정의. 소리 유무가 함께 바뀌는 교락.
* G1: 핵심 분석 불필요. already_done: partially (doi:10.1093/scan/nsab112 chronotopic 지도, 초록 기준). overlap: EmoViS (Horikawa의 sensory-semantic gradient 기원과 부분 겹침), Emo-FilM 연구 (시간 정보 기여).

### Chain 7. 휴지기 사전학습 brain foundation model의 정서 정보와 피질하 의존도 (Emo-FilM, Spacetop)

* **Original Finding:** Brain-JEPA는 UK Biobank 휴지기만으로 학습해 인구통계, 특성, 질환 예측에서 우수하고 linear probing도 강하다. 입력에 Tian 피질하 50 ROI 포함(arXiv:2409.19407, Conclusion과 데이터 절).
* **Unresolved Question:** attention으로 피질과 피질하를 비교하는 세밀한 해석, 과제와 질환을 포함한 사전학습 다양화가 남음(arXiv:2409.19407, 6절 2)와 3)).
* **Technological Development:** 공개 arousal CPM이 비교 기준선 역할(doi:10.1371/journal.pcbi.1012994, Discussion 3째 단락). 규범 1 Hz 다항목 정서 주석(Emo-FilM).
* **New Dataset / Model Combination:** Emo-FilM, Spacetop 영화 런을 450 ROI로 parcellation해 Brain-JEPA latent 추출(체크포인트 공개 여부 확인 전제) + linear probe로 규범 정서 profile 예측 + 피질하 토큰 masking ablation + Ke CPM 및 parcel 선형 모델과 비교.
* **New Research Question:** **"휴지기만으로 사전학습된 brain dynamics foundation model의 latent는 영화 중 규범 정서 profile을 parcel 기반 선형 모델보다 더 담고 있으며, 그 정보는 피질하 토큰 제거에 민감한가?"**
* **판정 기준:** 지지: probe 성능이 기준선보다 높고 피질하 masking 시 특정 항목(공포, 각성 관련)만 하락. 반증: 기준선 이하 또는 피질하 무관.
* **Safeguards:** decodability는 표상이나 인과가 아니다. 사전학습 TR, 전처리와 영화 데이터의 차이(미확인)로 인한 domain shift. 전역 성분 통제(Chain 1) 없이는 latent가 생리 성분을 읽을 수 있음. 사전학습 데이터에 우리 데이터가 들어 있는지 확인(오염).
* G1: 불필요. already_done: no (Brain-JEPA, BrainLM의 정서 탐침은 이번 검색에서 미발견. 자극 기반 encoding FM의 정서 평가는 별도 존재, search_index 수준). overlap: 없음 (EmoBrain은 자극 모델 V-JEPA2 사용으로 다름).

---

## 7. Axis E 확장 제안

### 7.1 추가
* **Pathway/Circuit-level Targets** (S1). 기존 'Subcortical-Cortical Interactions'를 영역 평균 수준과 패턴 경로 수준으로 나눈다. Saarimäki 2022에서 피질하 연결로 분류가 실패한 것과 Kragel 2021에서 영역 평균은 실패하고 패턴 경로는 성공한 대비가 근거다.
* **Brain-Body Interface Targets** (S2). 전역 자율신경 성분, 알로스타시스/내수용 시스템.
* **Network State Landscape** (S4)와 **Idiographic Network Targets** (S5).
* **Visual Subcortical Routes** (SC-pulvinar-amygdala)를 'Amygdala and Subcortical Systems' 아래 명시.
* **Cortical Gradients**를 **Cortical and Subcortical Gradients**로 확장(Tian 2020의 피질하 gradient, cortico-subcortical 축).

### 7.2 재분류
* 'Functional Connectivity'가 E와 F에 중복된다. **E는 '어떤 연결, 경로, network가 표적인가'**, **F는 'FC를 표상 형식으로 쓰는 방식'**으로 나눈다.
* 'Insula / Salience Network'와 'vmPFC / OFC / ACC'를 상위 범주 **Allostatic-Interoceptive System**(Kleckner 2017) 아래 두는 선택지를 제안한다. 단 이것은 특정 이론(EPIC)을 분류에 반영하는 것이므로 대안 이론과의 비교가 Stage 3에서 필요하다(이견 가능 지점).
* 'Visual and Auditory Cortex'를 **Sensory Cortices as Affective Targets**로 바꾸어, OTC의 의미-정서 결합 표상(Abdel-Ghaffar 2024)처럼 감각 피질이 정서 표적이 되는 경우를 포함한다.

### 7.3 독립 Axis 후보
* **Acquisition & Signal Physics** (S3): tSNR, dropout, MB, TE, 생리 잡음. 모든 neural target 주장의 전제 조건이므로 Q의 하위가 아니라 독립 축으로 두어 조합 단계에서 매번 점검되게 할 것을 제안.
* **Computational Psychiatry Phenotyping** (S6): 외부 분야에서 온 축. O와 겹치는 부분은 표시.

### 7.4 삭제
* 삭제 제안 없음. 다만 'Amygdala and Subcortical Systems' 항목에는 "데이터셋별 판정(0.5절) 없이 결과를 보고하지 않는다"는 사용 조건을 붙일 것을 제안.

---

## 8. 검증된 것과 미확인 사항

### 검증
* 42편 전부 식별자 경로 확인. 본문 열람 19편의 Discussion/Limitations 위치는 각 항목 `future_directions.section`에 기록.
* Spacetop과 Kragel 2021 Expt2의 획득 파라미터 일치(TR 0.46 s, MB8, 2.7 mm, TE 27.2 ms, 56 slices): Kragel 2021 Methods(PMC 전문)와 Stage 1 dataset_Spacetop.md 1절을 대조.
* Westlin 2025의 NMI 수치와 전처리(fMRIPrep 20.0.6, CSF/WM/motion 회귀, PCA 279성분): arXiv PDF 본문.
* Ma & Kragel 2026이 제공 FEAT 전처리본(6 mm smoothing, WM/CSF/motion 회귀)을 사용: PMC 전문 Methods.
* Ke 2025 가중치 공개 서술: PMC 전문 Discussion 3째 단락.

### 미확인
* 네 데이터셋의 실제 영역별 tSNR, dropout(계산하지 않음). Horikawa TE 43 ms의 감수성 손실 영향은 추론.
* MPathI 경로 패턴, Ke CPM, Brain-JEPA 체크포인트의 실제 공개 위치와 라이선스(저장소 미열람).
* Zaffina 2026, Bhattacharyya 2026, Park 2025, Liu 2025 본문(preprint, 초록만). Zaffina 2026이 생리 신호를 처리했는지.
* Chan 2026이 Emo-FilM을 썼는지(초록에 데이터셋명 없음, Stage 1은 강한 추정). Emo-FilM 참가자 질문지 항목 전체.
* Spacetop 생리와 설문 보유 여부(사용자 '전부 보유'에 포함되는지).
* Rosenberg & Finn 2022, Marquand 2019 본문.
* Ke 2025가 사용한 데이터셋 이름(본문 추출 시 이탤릭 이름이 빠져 확인 못 함). Emo-FilM이 포함되지 않았는지 Round 2 전 확인 필요.

---

## 9. 문헌 사이의 실제 의견 충돌 (지우지 않고 기록)

* **valence의 연결성 표상:** Lettieri 2021(초록)은 정서 극성이 DMN과 control network 연결성과 관련된다고 보고했고, Ke 2025는 dynamic FC로 valence를 예측하지 못했다(Discussion 10~11째 단락). 측정 방식(ISFC vs CPM), 평정 주체, 일반화 기준이 다르므로 직접 모순은 아니지만, 'valence가 연결에 있는가'에 대한 문헌 간 불일치다.
* **Horikawa 2020 vs Westlin 2025:** 같은 데이터에서 범주 대응 존재 vs 부재. 체인 2의 해석(session/전역 분산 지배)은 이 에이전트의 추론이며 Westlin 저자들의 주장이 아니다. Westlin은 자신들의 가정이 타당하다면 결론이 유지된다고 명시했다.
* **amygdala의 정서 정보:** Horikawa는 amygdala에서도 범주 모델 우세, Ma & Kragel은 amygdala 범주 decoding이 후측 hippocampus보다 낮음, Kragel 2021은 경로 중 amygdala 효과 크기가 가장 작음. 데이터셋과 지표가 달라 직접 비교는 불가하지만, 'amygdala가 정서 표적으로 얼마나 정보적인가'는 측정 조건에 따라 결론이 달라지는 열린 문제다.
