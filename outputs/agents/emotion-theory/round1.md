# Round 1 (Independent Discovery): emotion-theory

* 에이전트: emotion-theory (Agent 2, Affective Neuroscience & Emotion Theory)
* 담당: Axis A (Emotion & Affective Constructs), Axis Q (Reliability & Measurement), 외부 분야 Artificial Consciousness and Metacognition
* 기준일: 2026-11-12
* 절차: `reference/protocols.md` P1. 다른 에이전트 폴더는 읽지 않았다.
* 읽은 지침과 입력: `CLAUDE.md`, `reference/protocols.md`(P1 전체와 P2~P8 개요), `reference/axes.md`, `reference/starting_papers.md`, `reference/existing_projects.md`, `reference/datasets_and_resources.md`, `outputs/stage1/dataset_intelligence_report.md`, `outputs/stage1/gate_decision.md`, `outputs/stage1/environment_gaps.md`, `outputs/STAGE_STATUS.md`(사용자 결정 기록 포함)
* 문헌 기록: `outputs/agents/emotion-theory/literature.jsonl` (40편, 전부 식별자 경로로 확인: crossref 29, arxiv 11. 2024~2026년 12편. Affective Neuroscience 밖 11편. 본문 직접 확인 18편, 초록 직접 확인 22편)
* 표기: 논문은 DOI 또는 arXiv ID로 단다. [본문]은 내가 본문을 직접 읽은 내용, [초록]은 초록만 읽은 내용, [해석]은 내 추론이다. G1 표시는 원본 자극 필요 여부이며, 사용자 결정(2026-11-12)으로 4개 데이터셋 모두 원본 자극 보유 상태다.

---

## 0. 특별 지시 처리

### 0.1 Cowen & Keltner (2017) Discussion 원문 확인 결과

서지: Cowen AS, Keltner D (2017). Self-report captures 27 distinct categories of emotion bridged by continuous gradients. PNAS 114(38):E7900-E7909. doi:10.1073/pnas.1702247114, PMID 28874542, PMC5617253. 본문은 pmc.ncbi.nlm.nih.gov에서 직접 읽었다(Stage 1에서 실패했던 경로). SI Appendix는 pnas.org 차단으로 열지 못했다.

**Discussion 단락 지도** (그림 S6 캡션은 단락에서 제외하고 셌다)

| 단락 | 내용 요약 | 미래 방향 포함 여부 |
|---|---|---|
| 1 | 정서 의미 공간의 핵심 질문 4개 | 아니오 |
| 2 | 보고를 의미 공간의 점으로 보는 틀 | 아니오 |
| 3 | 27종의 신뢰 가능한 보고 경험, 결정적 분류체계는 아님(다른 자극, 보고 방식, 양식, 문화 필요) | 약함 |
| 4 | 군집도 균등 분포도 아닌 연속 gradient. **gradient가 정서 간 전이와 혼합 정서를 설명할 수 있다** | 예 |
| 5 | 범주가 차원을 더 잘 조직한다 | 아니오 |
| 6 | Kragel & LaBar 신경 decoding과 정합. **"New fMRI modeling approaches could fruitfully be combined with the emotion elicitation and multidimensional reliability estimation techniques introduced here to determine the number of distinct varieties of emotion that are represented by distinct patterns of neural activity."** (마지막 문장, 요지를 영어 원문 일부로 인용) | 예 (방향 1과 2) |
| 7 | **LeDoux & Brown(ref 15) higher-order theory 연결.** 참가자 간 보고 신뢰도는 공유된 상징 구조에서 나온다고 해석할 수 있고, HOT는 정서 상태가 고차 인지 영역에 표상된다고 예측하며 이는 OFC 등 고차 영역 연구(Kragel & LaBar 2016)와 정합. 이 영역들이 수십 종 정서를 어떻게 부호화하는지 묻는다 | 예 (방향 3) |
| 8 | 한계: 보고는 (i) 정서 경험 자체, (ii) 비정서적 인지/지각 경험의 채색, (iii) affective quality 지각(문화 규범상 그 상황이 일으킬 수 있거나 일으켜야 할 정서)의 혼합일 수 있다. 체계적 분리 필요 | 예 |
| 9 | 개인차: 인구통계, 성격의 median-split 효과는 작음(그림 S6, 종교성만 유의). 문화 관련 변이 검토 필요 | 예 |
| 10 | 한계 인정 후, 신경생리 연구가 valence/arousal과 기본 6정서에 치우쳤음을 지적 | 약함 |
| 11 | 결론 요약 | 아니오 |
| 12 | 음악, 일상 활동, 사회적 상호작용, 다른 문화와 언어, 말초 생리, 중추신경 반응, 비언어 표현으로 확장 | 예 |

**중요한 원문 확인 사항:** `reference/starting_papers.md`는 세 방향을 따로 나열했지만, 원문에서 방향 1(새 fMRI 모델링)과 방향 2(multidimensional reliability estimation)는 **한 문장으로 묶인 하나의 제안**이다. 그 목적은 "뇌 활동 패턴이 구분하는 정서 종류의 **수**를 결정하는 것"이다. 즉 방향 2의 핵심은 평정 데이터의 신뢰도 추정이 아니라, SH-CCA 같은 신뢰도 기반 차원 추정을 **신경 데이터에** 적용하는 것이다.

"multidimensional reliability estimation"의 실체는 Results "Evidence for 27 Distinct Varieties" 절과 Methods "SH-CCA Method" 절에 있다 [본문]. 평정자 표본을 반으로 나눠 두 반쪽의 평균 평정 사이 CCA를 하고(leave-one-stimulus-out 교차검증, 20회 반복), 유의한 canonical correlation의 수를 신뢰 차원 수로 센다. 결과는 24(P<0.05)~26(P<0.1)개이며 2,312회 시뮬레이션에서 보수적 추정이었다.

### 0.2 세 방향의 이후 수행 여부

| 방향 | 원문 위치 | 이후 수행 | 남은 부분 |
|---|---|---|---|
| 1. 새 fMRI 모델링 + 이 연구의 정서 유발 자극 | Discussion 6째 단락 마지막 문장 | **대부분 수행.** Horikawa 2020(10.1016/j.isci.2020.101060)이 같은 2,181개 비디오로 decoding, encoding, UMAP 군집 수행 [본문]. Kragel 2019(10.1126/sciadv.aaw4358)는 이 비디오 프레임으로 EmoNet을 학습 [본문]. Du 2025(arXiv:2509.24298)는 같은 fMRI에 MLLM 유사성 임베딩 적용 [본문] | 반복 제시 부재로 noise ceiling 없음(Horikawa Discussion 6째 단락). 1인칭/3인칭 혼재(Horikawa Limitations 2째 단락). 참가자 본인 보고 없음(Limitations 1째 단락). 무음 |
| 2. multidimensional reliability estimation으로 신경 패턴이 구분하는 정서 수 결정 | 같은 문장 | **부분 수행.** Koide-Majima 2020(10.1016/j.neuroimage.2020.117258)은 다른 영화로 평정-BOLD CCA를 해 약 25개(피험자별 18~36) 평정 차원이 뇌 표상에 기여한다고 보고 [초록]. Horikawa 2020은 수십 범주 decoding과 UMAP 군집을 보였지만 신뢰 차원 수는 세지 않았다 [본문, Results와 Discussion에 dimensionality 추정 없음 확인]. Westlin 2025(arXiv:2507.00320)는 참가자별 GMM 군집 11~14개 [본문]. Saarimäki 2025(10.1162/imag_a_00517)는 다른 영화로 8개 주요 차원 [본문] | **평정에 묶이지 않고, 피험자 간 신뢰도에 기반한 신경 차원 수 추정은 검색 범위 내 미발견.** SH-CCA나 PPCA를 신경 데이터에 적용한 사례도 검색되지 않았다. 피험자 간 cross-decomposition(arXiv:2409.06843)이 바로 이 빈칸을 채우는 기술이다(3절 C1) |
| 3. Higher-order theory of emotional consciousness 연결 | Discussion 7째 단락 | **부분 수행 (공포 중심).** 주관 공포 보고와 생리 반응 decoder의 신경 분리(10.1038/s41380-019-0520-3, HOT 틀로 해석) [본문], 분산된 주관 공포 signature와 편도체 단독 불충분(10.1038/s41467-021-26977-3) [본문], felt가 perceived보다 PFC, TPJ, 시상, 소뇌를 더 동원(10.1162/imag_a_00517) [본문] | 원문이 던진 질문 "고차 영역이 **수십 종** 정서를 어떻게 부호화하는가"는 미수행. 1차 내용(시각-의미, 생리)을 통제한 뒤 남는 보고 정서 정보의 위치를 다룬 연구는 미발견. PFC decoding이 경험이 아니라 지각 후 사고를 반영할 수 있다는 방법론 비판(10.1016/j.tics.2024.05.004) [초록]을 반영해야 한다 |

그 밖의 원문 미래 방향의 수행 여부는 `literature.jsonl`의 해당 항목 `future_directions`에 기록했다. 요약하면 4째 단락(전이와 혼합)은 부분 수행(10.1038/s41467-025-68240-z, 10.1093/cercor/bhae122), 8째 단락(보고 3요소 분리)은 felt vs perceived 수준에서만 부분 수행(10.1162/imag_a_00517), 12째 단락은 음악과 문화 비교가 수행됨(10.1073/pnas.1910704117).

### 0.3 LeDoux & Brown (2017) 서지 확정

* **LeDoux JE, Brown R (2017). A higher-order theory of emotional consciousness. PNAS 114(10):E2016-E2025. doi:10.1073/pnas.1619316114. PMID 28202735. PMC5347624.** 온라인 2017-02-15, 인쇄 2017-03-07. Crossref와 PMC 본문으로 확인했다(Cowen & Keltner 참고문헌 15번과 일치).
* 본문에서 확인한 검증 가능한 주장 [본문, "A Higher-Order Theory of Emotional Consciousness" 절]:
  1. 정서 경험과 비정서 경험은 같은 피질 일반 인지망(GNC)에서 생기고, 차이는 입력의 종류다.
  2. 1차 피질하 회로(방어 생존 회로, 신체 감지 회로) 손상은 공포 느낌을 약화하지만 제거하지 않는다.
  3. 정서 schema와 언어가 경험을 분화시킨다(fright, startle, panic, dread 구분). [해석] 이것은 emotional granularity의 HOT 버전이다.
  4. 자기(self) 표상이 필수다(no self, no emotion). 타인 고통에 대한 정서는 공감적 자기 관련으로 설명한다.
  5. 정서는 무의식일 수 없고, 자신이 느끼는 정서에 대해 틀릴 수 없다(1인칭 권위).
* 연구 질문 목록은 SI Appendix Box 10에 있다고 본문이 밝히지만 pnas.org 차단으로 **미열람**이다.

---

## 1. 중요한 미해결 문제

**U1. 뇌가 신뢰성 있게 구분하는 정서 관련 차원은 몇 개이며, 그 "수"는 측정 가정에 얼마나 의존하는가.**
같은 계열 연구가 서로 다른 수를 보고한다: 평정 SH-CCA 24~26 (10.1073/pnas.1702247114), 평정-BOLD CCA 약 25(피험자별 18~36, 10.1016/j.neuroimage.2020.117258), 참가자별 GMM 군집 11~14 (arXiv:2507.00320), 영화 정서 8개 주요 차원 (10.1162/imag_a_00517). [해석] 이 수들은 서로 다른 것을 센다. SH-CCA는 선형 신뢰 차원 수, GMM은 이산 군집 수, CCA는 평정 공간에 묶인 차원 수다. 시각피질에서는 신뢰 공유 분산이 scale-free power-law로 분포해 "차원 수"가 데이터 크기에만 제한된다는 결과가 있다 (arXiv:2409.06843, 4절 Discussion). 정서 영역에서도 그렇다면 "27개냐 아니냐" 논쟁 자체가 잘못 설정된 질문일 수 있다.

**U2. 정서 라벨의 주체와 대상이 바뀌면 뇌 설명력은 얼마나 달라지는가 (본인 보고 vs 동료 합의 vs 별도 평정자 규범 vs AI 추정).**
Horikawa Limitations 1째 단락은 라벨이 fMRI 참가자 보고가 아님을 한계로 들었고 (10.1016/j.isci.2020.101060), Westlin Discussion 6째 단락은 개인 수준 평정 부재를 결정적 한계로 들었다 (arXiv:2507.00320). Du 2025는 MLLM 임베딩이 인간 평정 임베딩보다 뇌 RSA에서 우세하다고 했지만 인간 기준은 평정에서 시뮬레이션한 것이고 우세 영역에 MST와 고차 시각피질이 포함된다 (arXiv:2509.24298, Results와 Limitations) [본문]. [해석] 측정 잡음(비디오당 9~17명 평정)과 시각-의미 내용 공유를 통제하지 않으면 "AI가 인간 보고보다 뇌의 정서 기하에 가깝다"는 결론은 "AI가 뇌의 시각-의미 기하에 가깝다"와 구분되지 않는다.

**U3. 정서 인식(지각, 귀속)과 정서 경험(느낌)의 신경 표상은 어디서 갈라지는가.**
Horikawa의 정서 우세 영역(IPL, VMPFC)이 ToM 네트워크와 겹쳐 1인칭/3인칭이 섞일 수 있다 (10.1016/j.isci.2020.101060, Limitations 2째 단락). 타인 정서 귀속은 mentalizing 영역의 추상 사건 특징으로 표상된다 (10.1016/j.cub.2015.06.009) [초록]. felt는 perceived보다 TPJ, PFC, 시상, 소뇌를 더 동원하고 같은 범주 perceived-felt 공유 분산은 평균 36%다 (10.1162/imag_a_00517, 4.4절) [본문]. 그러나 두 연구 모두 별도 평정자 보고라 참가자 본인 경험은 아니다.

**U4. Higher-order theory의 핵심 예측을 관찰 데이터로 어떻게 검정할 것인가.**
LeDoux & Brown은 정서 경험이 고차 피질 표상이라 하고 (10.1073/pnas.1619316114), 주관 보고 decoder는 외측/배내측 PFC, 생리 decoder는 편도체/섬엽/vmPFC로 분리된다 (10.1038/s41380-019-0520-3, Discussion 1~2째 단락) [본문]. 반면 주관 공포는 분산 표상이고 '의식 네트워크' 단독 예측은 낮다 (10.1038/s41467-021-26977-3, Discussion 3~4째 단락) [본문]. PFC decoding은 경험이 아니라 지각 후 사고를 반영할 수 있다 (10.1016/j.tics.2024.05.004) [초록]. 미해결: 1차 내용(감각-의미 feature, 측정 생리)을 통제한 뒤 남는 보고 정서 정보는 어디 있는가, 그리고 그것이 '경험'인지 '개념화'인지 관찰 데이터로 구분할 수 있는가.

**U5. 평정자 불일치는 잡음인가 신호인가.**
Emo-FilM 평정자 일치는 평균 0.38~0.39, 항목별 0.21~0.60이다 (Stage 1 `dataset_intelligence_report.md` 1절). 보고는 경험, 인지 채색, affective quality 지각의 혼합일 수 있다 (10.1073/pnas.1702247114, Discussion 8째 단락). ML에서는 인간 판단 분포를 학습 목표로 쓰면 강건성이 오르고 (arXiv:1908.07086, Discussion) [본문], 평정자별 모형의 불확실성이 실제 불일치와 대응한다 (10.1162/tacl_a_00449) [초록]. 미해결: 자극 수준 불일치가 자극 모호성, 개인 특이 반응, 측정 잡음 중 무엇인지 뇌 데이터로 분해할 수 있는가.

**U6. 혼합 정서는 구성 정서 패턴의 선형 중첩인가, 별도 상태인가.**
gradient가 혼합 정서를 설명할 수 있다는 제안 (10.1073/pnas.1702247114, Discussion 4째 단락), 섬엽은 단일 valence 상태에만 일관된 signature를 갖고 ACC/vmPFC는 혼합에도 갖는다는 결과 (10.1093/cercor/bhae122) [초록]. 가산성 encoding 검정은 검색 범위 내 미발견.

**U7. 자극 수준에서 신뢰로운 정서 신호가 개인 수준에서도 신뢰로운가 (정서판 reliability paradox).**
과제 fMRI ROI 신뢰도는 평균 ICC 0.397 (10.1177/0956797620916786) [초록]. 견고한 실험 효과는 개인 간 분산이 작아서 개인차 신뢰도가 낮다 (10.3758/s13428-017-0935-1) [초록]. vmPFC는 정렬 후에도 개인 특이적이며, ISC나 기능 정렬처럼 공통 반응을 가정하는 방법은 이를 잘못 특성화할 수 있다 (10.1126/sciadv.abf7129, Discussion 5째 단락) [본문]. [해석] 평정자 일치가 높은 자극만 고른 정서 데이터셋(Cowen & Keltner는 비디오의 75%가 유의한 일치)은 구조적으로 개인차 신호를 억제한다.

**U8. 정서의 주관적 유사성 구조(quality space)는 어느 영역의 신경 판별성으로 구현되는가.**
quality space 가설은 주관적 유사성이 신경 활성 유사성으로 설명된다고 보고 (10.1016/j.tics.2024.06.007) [초록], HOT 지표 HOT-4는 sparse하고 smooth한 부호가 quality space를 만든다고 본다 (arXiv:2308.08708, 2.3.3절) [본문]. 집단 부호의 power-law 스펙트럼은 smoothness 제약과 연결된다 (10.1038/s41586-019-1346-5) [초록]. 정서에 대한 경험적 검정은 검색 범위 내 미발견(철학 논문만 검색됨).

---

## 2. 주목할 모델과 방법론

담당 Axis가 A, Q라서 대형 AI 모델보다 측정 방법이 중심이다. 라이선스는 내가 저장소 LICENSE 파일을 직접 확인한 것만 확정으로 적었다(얕은 git clone, 실행하지 않음).

| # | 모델/방법 | Pretrained weights / 코드 | Input | Output | 학습 목표 / 통계 목표 | 라이선스 | 근거 |
|---|---|---|---|---|---|---|---|
| M1 | **SH-CCA** (split-half CCA) | weights 해당 없음. 원 코드 공개 여부 미확인(Methods로 재구현 가능) | 자극 x 항목 평정(자극당 반복 평정자) | 신뢰 차원 수, 각 canonical variate의 p | 두 반쪽 평균 평정 간 CCA, leave-one-stimulus-out, 이전 variate 통제 | 해당 없음 | 10.1073/pnas.1702247114 Methods [본문] |
| M2 | **Cross-decomposition 스펙트럼** | 코드 공개(BonnerLab/scale-free-visual-cortex) | 같은 자극을 본 두 피험자(또는 두 반복)의 자극 x voxel 반응 | rank별 교차검증 공유 분산 Σk, 피험자 간 상관 rk | 훈련 자극 교차공분산 SVD, 시험 자극에서 공유 분산 평가, hyperalignment | **GPL-3.0** (LICENSE 확인) | arXiv:2409.06843 3.1, 5.2절 [본문]; 개인차 확장 arXiv:2505.12653 [본문] |
| M3 | **GLMsingle** | 코드 공개 (MATLAB, Python) | fMRI 시계열 + 설계행렬 | single-trial beta | voxel별 HRF 라이브러리 선택, 교차검증 잡음 회귀자, voxel별 ridge | **BSD-3-Clause** (LICENSE 확인) | 10.7554/eLife.77599 [초록] |
| M4 | **분포 라벨 / 평정자별 모형** (soft label, multi-annotator head) | weights 불필요(학습 방법). CIFAR-10H 데이터와 Davani 코드 라이선스 미확인 | 자극별 평정 분포 또는 평정자별 라벨 | 평정자별 예측, 예측 불확실성 | soft-label cross-entropy/KL, 평정자별 multitask | 미확인 | arXiv:1908.07086 [본문], 10.1162/tacl_a_00449 [초록] |
| M5 | **HMeta-d** | MATLAB 코드 공개 | 자극, 반응, 확신도 빈도 | meta-d', M-ratio 사후분포 | 신호탐지 기반 계층 베이지안 | **MIT** (LICENSE 확인) | 10.1093/nc/nix007 [초록] |
| M6 | **MLLM machine behavior + SPoSE** | Qwen2-VL 계열 공개 weights(모델 크기별 라이선스 미확인), SPoSE 코드 라이선스 미확인 | 비디오 triplet + 프롬프트 | odd-one-out 선택 수백만 건에서 30차원 sparse positive 임베딩 | triplet 선택 우도 + sparsity | 미확인 | arXiv:2509.24298 [본문] |
| M7 | **EmoNet** | weights 공개(github.com/canlab, 논문 Data availability) | RGB 프레임(AlexNet 구조) | 20개 정서 범주 확률 | AlexNet 마지막 층을 Cowen & Keltner 프레임 137,482장의 규범 범주로 재학습 | 미확인 | 10.1126/sciadv.aaw4358 [본문]. **Horikawa에 쓰면 학습 누수(같은 자극, 같은 라벨)** |
| M8 | **Random stimulus model** | 코드 공개 여부 미확인 | 자극 x 피험자 반응 | 자극 일반화를 반영한 효과 추정 | 자극을 확률효과로 둔 베이지안 혼합모형 | 미확인 | 10.12688/wellcomeopenres.10298.2 [초록] |
| M9 | **rsatoolbox 2-factor CV/bootstrap** | Python 공개 | 자극 x 채널 반응, 모델 RDM | 피험자와 조건 모두로 일반화하는 모델 비교, noise ceiling | 2-factor 교차검증, 2-factor bootstrap | 미확인 | 10.7554/eLife.82566 [초록] |
| M10 | **Self- vs cross-prediction (introspection 검정 설계)** | 실험 설계 | 자기 행동 예측 과제 | 자기 예측과 타자 예측 정확도 차이 | fine-tuning으로 자기 행동 속성 예측 | 해당 없음 | arXiv:2410.13787 [초록] |

---

## 3. 다른 분야에서 가져와 적용할 수 있는 연구 아이디어

**T1. 물리학식 스펙트럼 분석 → 정서 신경 공간의 신뢰 차원 (Visual neuroscience → Affective).**
cross-decomposition은 반복 없이 두 피험자만 있어도 rank별 신뢰 공유 분산을 준다 (arXiv:2409.06843). Horikawa는 5명이 같은 2,181개 비디오를 봤으므로 피험자 쌍 10개로 적용할 수 있다. Cowen & Keltner Discussion 6째 단락 방향 2의 신경 버전이다. G1 불필요(기본 분석).

**T2. NLP perspectivism → 평정자별 정서 encoding (NLP → Affective).**
다수결 대신 평정자별 head를 두는 모형 (10.1162/tacl_a_00449, arXiv:2211.02570). Emo-FilM은 평정자별 1 Hz 원자료가 공개되어 있어 "consensus가 뇌 설명력을 얼마나 잃는가", "어떤 평정자의 시계열이 fMRI 참가자 뇌와 더 맞는가"를 물을 수 있다. G1 불필요.

**T3. Computer vision의 human uncertainty 라벨 → 자극별 정서 모호성 (CV → Affective).**
CIFAR-10H처럼 판단 분포를 목표로 학습한다 (arXiv:1908.07086). Horikawa 34범주 선택 비율은 이미 분포 라벨이다. 평정 엔트로피와 뇌 decoder 예측 엔트로피의 대응을 볼 수 있다. G1 불필요.

**T4. LLM introspection의 privileged access 검정 → 인간 정서 보고 (AI → Affective).**
"M1이 자기 행동을 M1 행동으로 학습한 M2보다 잘 예측하면 introspection" (arXiv:2410.13787). 인간판: 본인 정서 보고가 peer 합의, 규범, AI 추정보다 본인 뇌 반응의 고유 분산을 더 설명하는가. LeDoux & Brown의 1인칭 권위 주장 (10.1073/pnas.1619316114)을 신경 수준에서 검정 가능한 형태로 바꾼다. 단 이 검정은 보고와 뇌의 인과적 연결(introspection)만 다루며 경험의 존재(phenomenal)는 다루지 않는다 (arXiv:2506.05068).

**T5. 의식 과학의 quality space → 정서 quality space (Consciousness science → Affective).**
주관적 유사성 = 신경 판별성의 역 (10.1016/j.tics.2024.06.007; arXiv:2308.08708 2.3.3절). Horikawa 비디오 쌍의 평정 프로파일 거리와 영역별 crossnobis 거리를 비교해 정서 유사성 구조가 시각피질에 있는지 transmodal 영역에 있는지 본다.

**T6. 통계학의 random stimulus model → 적은 영화 수 데이터 (Statistics → Affective).**
Emo-FilM은 영화 14편이라 영화 수준 confound와 정서가 공선적일 수 있다 (Stage 1 4.2절). 영화를 확률효과로 두면 정서 효과의 일반화 검정이 50~200% 부풀려지는 문제를 줄일 수 있다 (10.12688/wellcomeopenres.10298.2).

**T7. (역방향) 정서 이론 → AI 평가: MLLM이 '묘사된 정서'와 '유발될 정서'를 구분하는가 (Affective → AI).**
Cowen & Keltner 8째 단락의 보고 3요소 구분과 HOT-2(신호 출처 monitoring)를 MLLM 평가 기준으로 쓴다. 같은 비디오에 "인물이 느끼는 정서", "보통 사람이 느낄 정서", "이 장면이 문화적으로 일으켜야 할 정서"를 따로 묻고, 세 답의 차이가 인간 felt/perceived 차이(10.1162/imag_a_00517의 공유 분산 36%)와 같은 구조인지 본다. AI 추정 라벨을 쓰는 모든 질문의 전처리 검증 단계로도 쓸 수 있다. 여기에 LLM 자기 확신도 보정(arXiv:2207.05221)을 더해, AI 라벨의 확신도가 인간 평정자 불일치(라벨 불확실성)와 대응하는지 점검한다. 대응하지 않으면 AI 라벨의 확신은 정서 모호성 정보가 아니다.

**T8. LLM 내부 appraisal 방향 → appraisal 연속 평정과 뇌 (LLM interpretability → Affective).**
LLM 중간층에서 appraisal 개념 방향을 찾아 조작하면 출력 정서가 예측 가능하게 바뀐다 (arXiv:2502.05489, 9~10절) [본문]. 같은 방향을 Emo-FilM 대사 전사본에 적용해 얻은 시계열을 Emo-FilM appraisal 평정(Predictable, Controlled, Urgency 등)과 뇌 반응에 정렬할 수 있다. 단 LLM은 서술에서 정서를 추론하는 "인식" 모델이므로 결과는 경험 질문이 아니라 appraisal 인식 질문으로만 해석한다. G1 필요(보유, 전사본 생성 필요).

---

## 4. Affective Neuroscience와 예상 밖으로 연결될 수 있는 개념

**X1. Scale-free 스펙트럼과 "정서는 몇 종인가" 논쟁.**
시각피질 신뢰 공유 분산은 거의 4자릿수 차원에 걸친 power-law다 (arXiv:2409.06843). 정서 영역도 그렇다면 27(10.1073/pnas.1702247114), 25(10.1016/j.neuroimage.2020.117258), 11~14(arXiv:2507.00320), 8(10.1162/imag_a_00517)이라는 서로 다른 숫자는 **데이터 크기와 방법이 정한 절단점**일 뿐이다. 반대로 정서 관련 영역에서 스펙트럼이 특정 rank에서 꺾인다면, 그것이 "유한한 정서 종류"의 첫 신경 증거가 된다. 범주 대 차원 논쟁을 스펙트럼 지수와 꺾임점의 문제로 바꾼다.

**X2. Quality space(HOT-4) = Cowen & Keltner gradient = Stringer smoothness.**
세 분야가 같은 대상을 다른 말로 부른다. 의식 과학은 "sparse, smooth 부호가 quality space를 만든다" (arXiv:2308.08708), 시스템 신경과학은 "스펙트럼이 1/n보다 느리게 감쇠하면 부호가 매끄럽지 않다" (10.1038/s41586-019-1346-5), 정서 과학은 "범주가 연속 gradient로 연결된다" (10.1073/pnas.1702247114). 정서의 gradient가 신경 부호의 smoothness로 구현되는 영역을 찾으면, 그곳이 정서 quality space의 후보다.

**X3. Reality monitoring과 '묘사된 정서 vs 유발된 정서' 태깅.**
PRM은 지각 신호가 세계에 대한 것인지(실재) 상상/잡음인지 태깅하는 monitoring이 의식의 조건이라 본다 (arXiv:2308.08708 2.3.3절). LeDoux & Brown은 self 표상이 정서의 필수 요소라 한다 (10.1073/pnas.1619316114). [해석] 영화 시청 중 뇌는 "화면 속 인물의 정서"(perceived)와 "내 정서"(felt)를 구분해 태깅해야 한다. felt에서 추가로 동원되는 TPJ/PFC (10.1162/imag_a_00517)를 self-tagging monitoring으로 재해석할 수 있다. 정서 연구의 perceived/felt 구분이 의식 과학의 source monitoring 문제와 같은 구조다.

**X4. Reliability paradox와 규범 정서 자극 설계.**
견고한 집단 효과는 개인 간 분산이 작아서 생긴다 (10.3758/s13428-017-0935-1). 평정자 일치가 높은 비디오를 선별한 정서 라이브러리는 자극 수준 신뢰도를 극대화하는 대신 개인차를 억제한다. 그래서 Horikawa 원 분석(자극 수준)과 Westlin 재분석(개인 수준)은 같은 데이터에서 서로 다른 신뢰도 축을 본 것일 수 있다 [해석].

**X5. NLP의 human label variation = constructionist의 'populations of instances'.**
Plank는 라벨 변동을 잡음이 아닌 실재 변동으로 보자고 하고 (arXiv:2211.02570), Barrett 계열은 정서 범주를 변이가 큰 사례 집단으로 본다 (10.1038/s41598-020-77117-8 Discussion 3째 단락). 두 분야가 같은 측정 문제를 다른 이론 언어로 다룬다. NLP 쪽의 평정자별 모형 도구를 정서 이론 논쟁의 판별 실험에 쓸 수 있다.

---

## 5. 새 Sub-axis 또는 하위 연구 방향

| # | 제안 | 소속 Axis | 독립 Axis 필요성 | 근거 |
|---|---|---|---|---|
| S1 | **Rank-resolved (spectral) reliability:** 신뢰 공유 분산을 rank별로 추정하고 스펙트럼 지수, 꺾임점, 피험자 간 공유 정도를 정서 이론 검정에 쓴다 | Q (K와 교차) | 불필요 | arXiv:2409.06843, arXiv:2505.12653, 10.1073/pnas.1702247114 |
| S2 | **Rating target x Rater taxonomy:** 라벨을 대상(portrayed / perceived affective quality / felt)과 주체(참가자 본인 / peer 합의 / 별도 평정자 규범 / AI 추정)의 격자로 표기하고, 격자 칸 간 뇌 설명력 차이를 연구 대상으로 삼는다 | A와 Q 공동 | 불필요. 단 모든 RQ에 필수 태그로 붙이자고 제안 | 10.1073/pnas.1702247114 Discussion 8째 단락, 10.1162/imag_a_00517, 10.1016/j.isci.2020.101060 Limitations |
| S3 | **Introspective access and emotion report (metacognitive layer):** 정서 보고의 privileged access, 보고 확신도와 재평정 일관성, 정서 schema와 언어의 역할, 보고 행위가 경험에 주는 영향 | A | **독립 Axis 후보.** A(구성 개념), N(계산), R(AI 자기보고)에 걸쳐 있고 외부 분야 Artificial Consciousness and Metacognition의 핵심이다. 가칭 "Axis U: Metacognition & Introspective Report". Coordinator 판단 요청 | 10.1073/pnas.1619316114, 10.1016/j.tics.2019.06.009 (HOT를 confidence와 동일시하지 말 것), arXiv:2410.13787, arXiv:2506.05068, 10.1093/nc/nix007, 10.1016/j.biopsycho.2014.11.004 |
| S4 | **Disagreement-as-signal:** 평정자 불일치를 자극 모호성, 개인 특이 반응, 측정 잡음으로 분해하는 신경 검정 | Q | 불필요 | arXiv:1908.07086, 10.1162/tacl_a_00449, arXiv:2211.02570 |
| S5 | **Validity of unsupervised structure:** 비지도 군집과 차원을 '분산'이 아니라 '신뢰 분산'에서 구하고, nuisance(session, run) 대응을 필수 보고 | Q (T와 교차) | 불필요 | arXiv:2507.00320, 10.1038/s41598-020-77117-8 Discussion 2째 단락 |
| S6 | **Affective quality space:** 주관적 유사성과 신경 판별성의 대응, smoothness | A (K와 교차) | 불필요 | 10.1016/j.tics.2024.06.007, arXiv:2308.08708, 10.1038/s41586-019-1346-5 |

---

## 6. Discussion-to-Research chain

형식: Original Finding → Unresolved Question → Technological Development → New Dataset / Model Combination → New Research Question. 각 chain 끝에 반증 조건, 주의점, 기존 수행 여부, G1, overlap을 단다.

### C1. 정서 관련 신경 공간의 신뢰 차원 스펙트럼

* **Original Finding:** 평정 SH-CCA로 24~26개 신뢰 차원 (10.1073/pnas.1702247114, Results "Evidence for 27 Distinct Varieties" 절, Discussion 3째 단락). 같은 자극 fMRI에서 범주 모델이 차원 모델보다 우세, 정서 표상은 transmodal 영역 (10.1016/j.isci.2020.101060, Discussion 1, 4째 단락).
* **Unresolved Question:** 뇌가 구분하는 정서 종류의 수 (10.1073/pnas.1702247114, Discussion 6째 단락 마지막 문장). 반복 제시가 없어 설명되지 않은 체계적 분산 추정 불가 (10.1016/j.isci.2020.101060, Discussion 6째 단락). 평정-뇌 CCA 차원 수가 피험자마다 18~36으로 흔들림 (10.1016/j.neuroimage.2020.117258, 초록).
* **Technological Development:** 피험자 간 cross-decomposition으로 반복 없이 rank별 신뢰 공유 분산 추정, 시각피질 power-law 발견. 원저자는 "덜 풍부한 자극에서도 같은지, 고차 영역에서 차원성이 달라지는지"를 미해결로 남김 (arXiv:2409.06843, 4.1절 4째 단락). rank 범위별 개인차 (arXiv:2505.12653, Discussion 1~3째 단락).
* **New Dataset / Model Combination:** Horikawa 5명, 피험자 쌍 10개 cross-decomposition. ROI: 초기/고차 시각피질, DMN과 transmodal, 피질하(HCP360 + 피질하 ROI는 공개 전처리본에 있음). 공유 차원 각각을 34범주, 14차원, 공개 시각 1000차원과 의미 73차원 feature로 설명하고, G1 보유분으로 최신 video/MLLM feature도 추가. Emo-FilM(소리 있는 영화)에서 재현.
* **New Research Question:** "정서 관련 transmodal 영역에서 피험자 간 신뢰 공유 신경 차원의 스펙트럼은 시각피질처럼 scale-free인가, 특정 rank에서 꺾이는가? 그리고 공유 차원 중 시각-의미 feature로는 설명되지 않고 정서 평정으로만 설명되는 차원은 몇 개인가?"
* **반증 조건:** transmodal 스펙트럼이 시각피질과 같은 지수의 power-law이고 정서 고유 차원이 0~수 개라면 "고차원 범주 정서 표상"은 시각-의미 표상의 재기술일 가능성이 커진다. 정서 고유 차원이 20개 안팎이고 그 근처에서 스펙트럼이 꺾이면 Semantic Space Theory를 지지한다.
* **주의:** 공유 차원만 센다(개인 특이 정서 신호는 제외됨, 10.1126/sciadv.abf7129). 5명이라 피험자 일반화는 약하다. 블록의 약 72%가 10 s 블록 평균이라 비디오 길이 차이 공변량 필요(Stage 1 4.1절).
* **기존 수행:** no (검색 범위 내). **G1:** 기본 분석 불필요, 최신 모델 feature는 필요(보유). **overlap: EmoViS** (affective brain geometry의 sensory-semantic 기원과 부분 겹침, 단 이 질문의 핵심은 평정 독립 신뢰 스펙트럼).

### C2. 이론 의존 관찰의 화해: 신뢰 부분공간에서의 비지도 구조

* **Original Finding:** UMAP에서 범주 군집과 gradient (10.1016/j.isci.2020.101060, Results "Distribution of Brain Activity Patterns" 절, Discussion 4째 단락). 반대로 참가자별 GMM 군집 11~14개, 참가자 간 trial 겹침 평균 7.3%, 규범 평정과 NMI < 0.02 (arXiv:2507.00320, Results, Discussion 2~3째 단락).
* **Unresolved Question:** 차이가 이론 차이인가 측정 선택 차이인가. Westlin은 multiverse 분석을 제안 (arXiv:2507.00320, Discussion 4째 단락). Azari 2020은 정서 신호가 다른 출처 신호보다 작으면 비지도 군집이 부수 특징을 따른다고 스스로 인정 (10.1038/s41598-020-77117-8, Discussion 2째 단락) [본문]. [해석] Westlin 표에서 군집과 session의 NMI는 0.188, run은 0.172로, 정서 평정 NMI(평균 0.014)보다 한 자릿수 크다. 저자는 이를 "낮다"고 해석했지만, PCA를 분산 95% 기준으로 고른 전뇌 성분이 session 수준 nuisance를 담았을 가능성을 배제하지 못한다(탐색적 관찰, NMI는 라벨 수에 따라 편향되므로 정식 비교 필요).
* **Technological Development:** 피험자 간 신뢰 부분공간 추출(cross-decomposition, hyperalignment; arXiv:2409.06843), single-trial 재추정(10.7554/eLife.77599), 자극 확률효과(10.12688/wellcomeopenres.10298.2), 2-factor 교차검증(10.7554/eLife.82566).
* **New Dataset / Model Combination:** Horikawa raw BIDS. 같은 군집 알고리즘을 세 입력 경로에 적용하는 multiverse: (a) Westlin식 분산 기준 PCA, (b) Horikawa식 평정 기반 voxel 선택, (c) 평정을 쓰지 않는 피험자 간 신뢰 부분공간. 각 경로에서 군집-평정 NMI, 군집-session/run NMI, 피험자 내 session 분할 간 군집 재현성, 피험자 간 군집 대응을 보고.
* **New Research Question:** "평정 정보를 쓰지 않되 피험자 간 신뢰 가능한 신경 부분공간으로 입력을 제한하면, Horikawa 정서 비디오 반응의 비지도 구조는 규범 정서 범주와 대응하는가? 그리고 Westlin이 보고한 개인 특이 군집은 피험자 내 session 간 재현되는 신뢰 가능한 개인차인가, session/run nuisance 구조인가?"
* **반증 조건:** (c)에서도 평정 대응이 낮고 개인 군집이 session 분할 간 재현되며 nuisance와 무관하면 constructionist 해석(개인 특이 구조)이 강화된다. (c)에서 평정 대응이 회복되고 (a)의 개인 군집이 nuisance와 대응하면 Westlin 결과는 측정 산물이다. 둘 다 아니면 "공유 구조는 범주적, 개인 구조는 별도로 신뢰 가능"이라는 혼합 결론.
* **주의:** 이 질문은 정서 경험의 구조가 아니라 **규범 평정과 대응하는 신경 구조의 측정 타당성**을 다룬다. 결과는 exploratory로 표시하고 분석 경로를 사전 등록할 것을 권한다.
* **기존 수행:** no (검색 범위 내). **G1:** 불필요. **overlap:** 없음 (EmoViS와 데이터만 공유).

### C3. HOT의 관찰 수준 검정: 1차 내용 통제 후 남는 보고 정서 정보의 위치

* **Original Finding:** 보고 신뢰도와 고차 영역 표상에 대한 HOT 해석 (10.1073/pnas.1702247114, Discussion 7째 단락). 정서는 GNC의 고차 표상 (10.1073/pnas.1619316114, HOTEC 절). 주관 공포 decoder(외측/배내측 PFC)와 생리 decoder(편도체, 섬엽, vmPFC)의 분리 (10.1038/s41380-019-0520-3, Discussion 1째 단락).
* **Unresolved Question:** 주관 보고가 생리의 후기 readout인가 (10.1038/s41380-019-0520-3, Discussion 2째 단락). 고차 영역이 수십 종 정서를 어떻게 부호화하는가 (10.1073/pnas.1702247114, Discussion 7째 단락 마지막 문장). 주관 공포는 분산 표상이라 고차 영역 단독 설명이 약함 (10.1038/s41467-021-26977-3, Discussion 3~4째 단락). PFC decoding은 지각 후 사고일 수 있음 (10.1016/j.tics.2024.05.004).
* **Technological Development:** 고차원 시청각-의미 feature로 1차 내용을 통제하는 variance partitioning. 선례는 Horikawa의 정서/시각/의미 encoding 비교(10.1016/j.isci.2020.101060, Results "Disentangling Emotional, Visual Object, and Semantic Feature Encoding" 절)이며 당시 feature는 시각 1000차원과 의미 73차원이었다. 최신 모델 선택은 다른 에이전트 담당 영역이다. 시각 정서 schema 기준선으로 EmoNet(10.1126/sciadv.aaw4358, Discussion 1~2째 단락: 정서 정보가 시각 특징에 내재)을 쓰되 Horikawa에는 쓰지 않는다. 측정 생리는 회귀자로 넣는다.
* **New Dataset / Model Combination:** Emo-FilM. 같은 시간축에 (1) 시청각-의미 feature, (2) fMRI 참가자 본인의 측정 생리(PPG, EDA, 호흡), (3) 평정자의 보고 Physiology 항목, (4) Appraisal 항목, (5) Feeling 항목, (6) discrete 항목. 영역별로 (5)의 고유 설명 분산을 (1)+(2) 통제 후 추정하고 (4)와 비교.
* **New Research Question:** "시청각-의미 feature와 참가자 측정 생리를 모두 통제한 뒤 남는 '보고된 느낌(Feeling)' 고유 설명 분산은 PFC와 TPJ에 집중되는가(HOT 정합), 섬엽과 편도체에 남는가(1차 이론 정합), 아니면 넓게 분산되는가(분산 표상 정합)? 그리고 이 분포는 인지 평가(Appraisal) 항목의 분포와 다른가?"
* **반증 조건:** Feeling 고유 분산이 PFC/TPJ에 없고 섬엽, 체성감각에만 있으면 HOT의 관찰적 예측은 지지되지 않는다. PFC에 있더라도 Appraisal 분포와 같다면 '느낌'이 아니라 '평가 개념화'를 본 것일 수 있다(Block 비판).
* **주의:** 보고는 별도 평정자 consensus이며 참가자 본인 느낌이 아니다. 관찰 데이터로 HOT와 constructionist를 판별할 수 없다. 결과는 "정서 경험의 위치"가 아니라 "1차 내용 밖에 있는 보고 정서 정보의 위치"로만 서술한다. 영화 14편이라 영화를 확률효과로 둔다.
* **기존 수행:** no (검색 범위 내). **G1:** 필요(보유, 단 보유 파일이 크레딧 절단 연구 판본인지 미확인). **overlap: Emo-FilM 연구** (사전학습 멀티모달 encoding으로 정서 맥락 기여 분석과 방법 일부 겹침).

### C4. Privileged access 검정: 본인 보고, peer 합의, 규범, AI 추정의 고유 설명력

* **Original Finding:** 라벨이 참가자 보고가 아님 (10.1016/j.isci.2020.101060, Limitations 1째 단락). 개인 수준 평정이 없어 개인 군집을 설명하지 못함 (arXiv:2507.00320, Discussion 6째 단락). MLLM 임베딩이 인간 평정보다 뇌 RSA에서 우세 (arXiv:2509.24298, Results "Bridging" 절, Discussion "Bridging the behavior-neural gap" 단락), 단 인간 기준은 평정 시뮬레이션 (같은 논문 Limitations 2째 단락). 자기 정서에 대해 틀릴 수 없다 (10.1073/pnas.1619316114, HOTEC 절).
* **Unresolved Question:** 본인 보고는 타인 보고가 갖지 못한 본인 뇌 정보를 담는가. AI의 우세는 측정 잡음 차이인가 시각-의미 공유인가.
* **Technological Development:** self- vs cross-prediction 설계 (arXiv:2410.13787). 설명 가능 분산과 신뢰도 보정 논리 (10.1177/1529100619850176, "Toward a Future Science" 절). 2-factor bootstrap (10.7554/eLife.82566).
* **New Dataset / Model Combination:** **Spacetop alignvideo**: 같은 영상 49개를 다수 참가자가 보고 본인 7차원 평정을 남김(Stage 1 4.3절). 각 참가자에 대해 (a) 본인 평정, (b) **leave-one-subject-out peer 평균**(같은 영상을 본 다른 fMRI 참가자들의 본인 보고 평균), (c) MLLM 추정 평정, (d) 시청각-의미 feature. Emo-FilM에서는 consensus vs 참가자 사후 클립 평정(부분)으로 보조 검정, Horikawa에서는 규범 vs MLLM만(본인 없음).
* **New Research Question:** "같은 영상에 대해 참가자 본인의 정서 보고는 peer 합의, AI 추정, 시청각-의미 feature가 설명하지 못하는 그 참가자 뇌 반응의 고유 분산을 설명하는가? 고유 분산이 있다면 어느 영역(vmPFC, TPJ, 섬엽)에 있으며 측정 신뢰도 보정 후에도 남는가?"
* **반증 조건:** 신뢰도 보정 후 본인 보고 고유 분산이 0이면, 사후 개인 보고는 뇌 수준에서 peer 합의의 잡음 섞인 표본과 구분되지 않는다. 고유 분산이 시청각 feature 통제 전에만 있으면 개인 주의 차이로 설명될 수 있다.
* **주의:** Stage 1 보고서는 "규범 vs 본인 비교가 한 데이터셋 안에서 가능한 곳은 Emo-FilM뿐"이라 했다. Spacetop의 (b)는 **별도 평정자 규범이 아니라 fMRI 참가자 집단의 peer 합의**라서 같은 개념이 아니지만, "본인 vs 타인 합의" 비교는 가능하다는 점을 보완 제안한다. alignvideo 평정 약 51% 결측, 영상 49개, 영상 종료 후 1회 평정, 평정 구간과 영상 끝 HRF 겹침(Stage 1)을 통제해야 한다. 보고는 경험 자체가 아니다.
* **기존 수행:** no (검색 범위 내). **G1:** (c), (d)에 필요(보유). **overlap:** 없음.

### C5. 평정자 불일치의 신경 분해: 자극 모호성 vs 개인 특이 반응 vs 측정 잡음

* **Original Finding:** 보고는 경험, 인지 채색, affective quality 지각의 혼합 (10.1073/pnas.1702247114, Discussion 8째 단락). 비디오의 75%만 유의한 일치, 평균 일치 54% (같은 논문 Results "Emotion Elicitation" 절). Emo-FilM 평정자 일치 평균 0.38~0.39 (Stage 1 1절).
* **Unresolved Question:** 불일치의 출처를 뇌 데이터로 구분할 수 있는가. ML은 인간 불확실성의 대부분이 약 30% 자극에 집중되고 분포 라벨이 유용하다고 보고 (arXiv:1908.07086, Discussion), 그러나 신경 데이터와 연결되지 않았다.
* **Technological Development:** 분포 라벨 학습과 평정자별 모형 (arXiv:1908.07086; 10.1162/tacl_a_00449), 피험자 간 패턴 일치.
* **New Dataset / Model Combination:** Horikawa: 자극별 34범주 선택 비율의 엔트로피(평정자 수 9~17에 따른 편향 보정), 피험자별 분포 decoder의 예측 엔트로피, 피험자 간 패턴 상관. Emo-FilM: 평정자별 1 Hz 원자료로 시점별 평정자 불일치, 시점별 피험자 간 패턴 ISC.
* **New Research Question:** "평정자들이 서로 다르게 보고하는 자극이나 시점에서 fMRI 피험자들의 정서 관련 신경 패턴은 (a) 피험자 안에서 모호해지는가(decoder 엔트로피 증가), (b) 피험자 사이에서 갈라지는가(패턴 일치 감소), (c) 변하지 않는가? 이 세 패턴의 비율로 평정 불일치를 자극 모호성, 개인 특이 반응, 측정 잡음으로 분해할 수 있는가?"
* **반증 조건:** 정서 강도와 시각 복잡도를 통제하면 (a)와 (b) 모두 사라질 때, 평정 불일치는 뇌 수준 대응이 없는 보고 단계 잡음으로 본다.
* **주의:** 강도가 낮은 비디오는 신경 신호가 약해 엔트로피가 오른다. 강도와 평정자 수를 공변량으로 둔다. 별도 평정자 불일치와 fMRI 피험자 신경 변동은 다른 사람들의 것이다.
* **기존 수행:** no (검색 범위 내). **G1:** 불필요. **overlap:** 없음.

### C6. 혼합 정서: 선형 중첩인가 창발 상태인가

* **Original Finding:** gradient가 혼합 정서를 설명할 수 있다 (10.1073/pnas.1702247114, Discussion 4째 단락 마지막 문장). 범주 판단의 56%는 1개, 27%는 2개, 11%는 3개 범주 선택 (같은 논문 Methods "Estimating Significance" 절). 섬엽은 단일 valence에만, ACC/vmPFC는 혼합에도 일관된 signature (10.1093/cercor/bhae122, 초록).
* **Unresolved Question:** 혼합 상태의 신경 패턴이 구성 범주 패턴의 가중합으로 예측되는가, 영역마다 다른가.
* **Technological Development:** 범주 점수 기반 voxel-wise encoding(10.1016/j.isci.2020.101060, Results "Encoding Models Predicting Brain Activity from Emotional Scores" 절)을 가산성 검정으로 바꾼다: 단일 범주 우세 자극으로 학습하고 혼합 자극에서 선형 결합 예측과 상호작용 항 모델을 비교한다. 목표 라벨은 argmax가 아니라 선택 비율 분포를 쓴다(arXiv:1908.07086, Discussion 1째 단락).
* **New Dataset / Model Combination:** Horikawa 비디오를 선택 비율로 '단일 범주 우세'와 '두 범주 동시 유의'로 나눔. Emo-FilM에서 같은 평정자 안의 동시 상승(예: Happiness와 Sad)을 평정자별 원자료로 확인(평정자당 6항목 배정 제약 있음).
* **New Research Question:** "단일 정서 비디오로 학습한 선형 encoding 모델은 혼합 정서 비디오의 반응을 영역별로 얼마나 예측하며, 비가산성(예측 실패)은 섬엽과 편도체 같은 영역과 vmPFC와 ACC 같은 영역 중 어디에 집중되는가?"
* **반증 조건:** 모든 영역에서 선형 결합이 혼합 반응을 ceiling 수준으로 예측하면 '혼합 정서 고유 상태' 가설은 지지되지 않는다.
* **주의:** Horikawa의 다중 선택은 '한 사람이 동시에 느낌'과 '평정자 간 분산'을 구분하지 못한다(평정자 개인 자료 비공개). 이것은 규범 평정의 혼합이지 참가자 경험의 혼합이 아니다.
* **기존 수행:** partially (10.1093/cercor/bhae122: 일관성 수준. 가산성 encoding 검정은 미발견). **G1:** 불필요. **overlap: EmoBrain** (34차원 정서 profile decoding을 쓰는 경우 일부).

### C7. 정서 quality space의 위치

* **Original Finding:** 범주 간 연속 gradient (10.1073/pnas.1702247114, Discussion 4째 단락). HOT-4: sparse, smooth 부호가 quality space를 만든다 (arXiv:2308.08708, 2.3.3절). 주관적 유사성은 신경 유사성으로 설명될 수 있다 (10.1016/j.tics.2024.06.007, 초록).
* **Unresolved Question:** 정서의 유사성 구조는 어느 영역의 신경 판별성으로 가장 잘 설명되는가. 그 영역의 부호는 smooth한가.
* **Technological Development:** crossnobis 기반 신경 판별성과 2-factor 추론 (10.7554/eLife.82566), 스펙트럼 smoothness 지표 (10.1038/s41586-019-1346-5).
* **New Dataset / Model Combination:** Horikawa 비디오 쌍의 34차원 평정 프로파일 거리(주관 유사성의 집단 대리)와 영역별 crossnobis 거리, 시각-의미 feature 거리 partial. 국소 거리 보존(이웃 비디오 순위 일치)으로 smoothness 측정.
* **New Research Question:** "정서 평정의 유사성 구조는 시각-의미 feature 유사성을 통제한 뒤 어느 영역의 신경 판별성으로 설명되며, 그 영역의 신경 공간은 평정 gradient를 국소적으로 보존하는 smooth한 부호를 보이는가?"
* **반증 조건:** 통제 후 설명력이 시각피질에만 남으면, 정서 유사성은 감각 유사성의 재기술이며 고차 quality space 가설은 지지되지 않는다.
* **주의:** 평정 유사성은 집단 규범이지 개인 주관 유사성이 아니다. quality space 이론은 판별을 개인 수준에서 정의하므로 이 분석은 집단 수준 근사다.
* **기존 수행:** no (검색 범위 내, 철학 논문만 검색됨). **G1:** 기본 분석 불필요. **overlap: EmoViS** (affective brain geometry, 부분).

### C8. 개인 특이 고차 rank 신경 성분과 본인 정서 보고의 편차

* **Original Finding:** 인구통계와 성격은 보고 분산의 작은 부분 (10.1073/pnas.1702247114, Discussion 9째 단락, 그림 S6). 같은 비디오에도 참가자별 뇌 군집이 다름 (arXiv:2507.00320, Discussion 2, 5째 단락). vmPFC 개인 특이 상태 (10.1126/sciadv.abf7129, Discussion 1, 5째 단락).
* **Unresolved Question:** 누가 누구와 비슷하게 경험하는지를 구조화하는 요인 (arXiv:2507.00320, Discussion 5째 단락). 개인 정서 보고의 편차는 신경 개인차의 어느 rank 범위에 있는가.
* **Technological Development:** rank 범위별 신뢰 가능한 개인차와 행동 예측 (arXiv:2505.12653, Discussion 1~3째 단락; 원저자는 특정 차원 범위가 자극의 해석 가능한 특징에 대응하는지를 미래 과제로 둠, Discussion 4째 단락).
* **New Dataset / Model Combination:** Spacetop alignvideo 다수 참가자. 참가자 쌍마다 rank 범위별 신경 유사성과 본인 7차원 평정 프로파일의 유사성(peer 평균 대비 편차)을 IS-RSA로 연결.
* **New Research Question:** "같은 영상을 본 참가자들 중 본인 정서 보고가 서로 비슷한 쌍은 어느 신경 rank 범위에서 서로 비슷한가? 정서 보고 유사성은 저차 고분산 성분(공유된 시각-의미 반응)이 아니라 고차 저분산 성분에 실려 있는가?"
* **반증 조건:** 정서 보고 유사성이 어떤 rank 범위와도 관계없거나 저차 성분에서만 나타나면, 보고 개인차는 신경 표상 개인차가 아니라 보고 단계 차이(척도 사용, 결측 패턴)일 가능성이 크다.
* **주의:** 개인 수준 신경 지표 신뢰도(split-session)를 먼저 보고해야 한다 (10.1177/0956797620916786). 평정 결측(약 51%)이 개인 편차를 왜곡할 수 있다. 정서 경험이 아니라 사후 보고의 개인차를 다룬다.
* **기존 수행:** no (정서 적용은 검색 범위 내 미발견). **G1:** 기본 분석 불필요. **overlap:** 없음.

---

## 7. 담당 Axis 확장 제안

### 7.1 Axis A (Emotion & Affective Constructs)

* **재분류:** 현재 Sub-axis "Emotion Recognition vs Emotion Experience"를 일반 Sub-axis 하나로 두지 말고, **모든 RQ에 붙는 필수 태그**로 승격한다. 태그 값은 5절 S2의 격자(대상: portrayed / perceived affective quality / felt, 주체: 본인 / peer 합의 / 별도 평정자 규범 / AI 추정)를 쓴다.
* **추가:** "Affective Quality Space" (S6), "Emotion Schema and Language" (LeDoux & Brown의 schema, granularity와 연결), "Self-relevance / Self-tagging" (HOTEC의 self 요소, X3).
* **추가 (독립 Axis 후보):** "Introspective Access and Emotion Report" (S3). A 안에 두면 구성 개념과 측정이 섞이므로, 가칭 Axis U "Metacognition & Introspective Report"로 독립시키는 안을 Coordinator에게 제안한다. 유형은 Construct와 Inference & Measurement 사이다.
* **명확화:** "Subjective Feeling"은 데이터셋에서 직접 측정되지 않는다. 4개 데이터셋 모두 스캔 중 연속 자기보고가 없다(Stage 1 0절). Subjective Feeling을 다루는 RQ는 "보고"를 측정한다고 명시하게 한다.

### 7.2 Axis Q (Reliability & Measurement)

* **추가:** "Rank-resolved / Spectral Reliability" (S1), "Disagreement-as-signal" (S4), "Validity of Unsupervised Structure" (S5), "Disattenuation for Brain-Behavior and Brain-AI Comparison" (C4, Du 2025 비판), "Stimulus Sampling and Generalization" (random stimulus model, 2-factor CV), "Rater Population Mismatch" (Horikawa 평정자 미국 MTurk vs fMRI 참가자 일본, Saarimäki 핀란드 여성 평정자).
* **병합:** "Hierarchical Bayesian Models"는 "Psychometric Measurement Models"의 방법으로 병합한다(구성 개념이 아니라 추정 기법).
* **명확화:** "Neural Noise Ceilings"를 두 종류로 나눈다. (a) 반복 기반 ceiling(NSD, 10.1371/journal.pcbi.1006397 방식), (b) 피험자 간 공유 성분 ceiling(Horikawa, Emo-FilM, ISC 10.1093/scan/nsz037 또는 cross-decomposition arXiv:2409.06843). (b)는 개인 특이 정서 신호를 잡음으로 분류하므로 정서 영역에서는 상한이 아니라 공유 성분의 상한이다 (10.1126/sciadv.abf7129).

### 7.3 데이터셋별 Axis Q 사전 점검 항목 (다른 에이전트 제안 검토 시 사용)

| 데이터셋 | 라벨 주체와 대상 (S2 격자) | 반드시 보고할 신뢰도 | 대표 위험 |
|---|---|---|---|
| Horikawa | 별도 평정자 규범, felt(평정자 자신) | 피험자 간 공유 분산(반복 없음), 평정 엔트로피 | 1인칭/3인칭 혼재, EmoNet 학습 누수, 5명 |
| Emo-FilM | 별도 평정자 consensus(3~4명), felt; 참가자 사후 클립 평정(부분) | 항목별 평정자 일치(0.21~0.60)로 decoding 정규화 | 영화 14편 공선성, z-score된 상대 강도 |
| Spacetop | 참가자 본인 felt(alignvideo), perceived/attributed(faces, shortvideo) | 개인 수준 split-session 신뢰도, 평정 결측 패턴 | 약 51% 결측, 사후 1회 평정 |
| NSD | nsdmeadows 100장(주체 본인으로 보이나 지시문 미확인), AI 추정 | 반복 기반 ceiling | AI 라벨을 인간 정서로 해석하는 위험 |

---

## 8. 인식(recognition) 질문과 경험(experience) 질문의 구분 규칙 (팀 공용 제안)

다른 에이전트의 제안을 검토할 때 다음을 확인하겠다.

1. **라벨이 무엇을 재는가:** 자극 속 인물의 정서(portrayed), 자극이 가진 정서적 성질의 지각(perceived affective quality), 누군가가 느낀 정서(felt) 중 무엇인가. MLLM 라벨은 기본적으로 portrayed 또는 perceived에 가깝다.
2. **누가 보고했는가:** fMRI 참가자 본인인가, 다른 사람인가, AI인가. Horikawa와 Emo-FilM consensus의 felt는 "다른 사람이 느낀 정서"이므로, 이를 예측하는 뇌 신호는 참가자의 경험이 아니라 "규범적으로 유발될 정서에 대한 참가자 뇌의 반응"이다.
3. **결론의 동사:** "정서를 decoding했다"는 "규범 평정과 공변하는 신경 정보를 찾았다"로 바꿔 쓴다. "경험을 읽었다"는 본인 보고 데이터에서도 피한다(보고 ≠ 경험, arXiv:2506.05068).
4. **PFC/TPJ 결과의 해석:** 정서 개념화, 타인 정서 추론(ToM), 지각 후 사고일 가능성(10.1016/j.tics.2024.05.004, 10.1016/j.cub.2015.06.009)을 대안 설명으로 반드시 적는다.
5. **시각-의미 통제:** 정서 라벨 효과는 고차원 시각-의미 feature 통제 후에 보고한다. 통제 feature 모델이 정서 라벨로 학습되었는지(EmoNet 등) 확인한다.

---

## 9. 기존 프로젝트와의 겹침 (`reference/existing_projects.md`, 표시만)

* C1, C7: overlap: EmoViS (Horikawa 정서 기하의 sensory-semantic 기원과 부분 겹침)
* C3: overlap: Emo-FilM 연구 (멀티모달 encoding으로 정서 맥락 기여 분석과 방법 일부)
* C6: overlap: EmoBrain (34차원 정서 profile decoding을 쓰는 경우)
* C2, C4, C5, C8: 겹침 없음

---

## 10. 검증되지 않은 사항과 접근 제약 (사실 기록)

* **열지 못한 원문:** Cowen & Keltner (2017)와 LeDoux & Brown (2017)의 SI Appendix(pnas.org 접속 거부, 본문은 PMC로 읽음). LeDoux & Brown SI Box 10의 연구 질문 목록 미열람. Fleming & Shea (2024) 본문(cell.com 403, 저자 저장소 sas-space.sas.ac.uk는 이 세션 네트워크에서 해석 실패, 허용 필요). Vaccaro (2024) 본문(academic.oup.com 403). Davani (2022) 출판사 PDF(direct.mit.edu 403, arXiv 초록으로 대체). NCBI E-utilities는 차단되어 PubMed MCP로 대체.
* **라이선스:** GitHub API는 이 세션에서 차단되어, 공개 저장소 3개를 얕게 clone해 LICENSE 파일만 확인했다(GPL-3.0, BSD-3-Clause, MIT). 나머지(EmoNet, SPoSE, Qwen2-VL, rsatoolbox, Han & Bonner 코드)는 미확인.
* **내 해석으로 표시한 주장:** Westlin 군집-session/run NMI가 정서 NMI보다 크다는 관찰은 논문이 보고한 수치를 내가 비교한 것이다. NMI는 라벨 범주 수에 따라 편향되므로 정식 비교(예: 조정 NMI, 순열 기준)가 필요하다. Du 2025의 뇌 RSA 비교에서 인간 평정 RDM 신뢰도 보정 여부는 본문에서 확인하지 못했다(행동 수준 비교에는 Rajalingham 보정을 썼다고 적혀 있음).
* **수치 불일치 기록:** Horikawa 고유 비디오 수가 문헌마다 다르다. Horikawa 본문 2,181, Du 2025는 16개 중복 제거 후 2,180, Westlin 2025는 제시 2,196을 그대로 분석, Cowen & Keltner 라이브러리 2,185. Stage 1은 중복 표시 label index 15개를 기록했다. 분석 시 중복 처리 규칙을 통일해야 한다.
* **"already_done" 판정 범위:** 각 판정은 이번 세션의 WebSearch, PubMed, arXiv 검색 범위 내 판단이다. 특히 C1(정서 영역 cross-decomposition), C4(본인 보고 고유 분산), C5(평정 불일치와 신경 변동)의 "no"는 Round 3 검토 때 재검색을 권한다.
* **preprint:** Westlin 2025, Du 2025, Gauthaman 2024, Han & Bonner 2025, Binder 2024, Comsa & Shanahan 2025, Butlin 2023은 arXiv 판으로 확인했으며 동료 심사 여부는 확인하지 않았다(Tak 2025는 arXiv comment에 ACL 2025 camera-ready로 표기, Peterson 2019는 ICCV 2019, Plank 2022는 EMNLP 2022로 표기).
