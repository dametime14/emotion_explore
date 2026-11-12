# Stage 3 Round 3 추가 검토: ET-P4, EF-P4 (adversarial-reviewer)

* 작성: adversarial-reviewer(`round3_top10_review.md`를 쓴 같은 인스턴스). 기준일 2026-11-12.
* 요청: Coordinator 추가 지시. `tally_responses.py`를 Round 2 파일만 세도록 고친 뒤의 정정 상위 10개에 새로 들어온 ET-P4(6위), EF-P4(10위)를 본 검토와 같은 형식(P3 7항목, C~G 점검, V1~V12, 판정)으로 검토하고, Coordinator의 P5 조합 처리(ET-P4 → LIT-01, EF-P4 → LIT-34)를 판정한다.
* 읽은 자료: `outputs/agents/emotion-theory/round2.md` ET-P4, `outputs/agents/encoding-foundation/round2.md` EF-P4, `outputs/agents/systems-neuro/round2.md` 3절(두 제안 응답)과 SN-P7, `outputs/agents/systems-neuro/round1.md` Chain 7, `outputs/agents/encoding-foundation/round1.md`(foundation model 표), `outputs/combinations/matrix.csv`의 LIT-01, LIT-34, `outputs/discussion/top10_for_review.md`(정정본).
* 표기: [본문], [초록], [Crossref], [search_index], [추론], [타 에이전트 확인]은 본 검토와 같다. V1과 V3는 본 검토 10절의 v3 제안(V1 방향성 null 정정, V3 사람 수준 주장의 양방향 중심화)을 반영해 판정한다.
* 이 파일 외에는 아무 파일도 고치지 않았다.

### 이해 상충 공개
ET-P4는 adversarial-reviewer Round 1의 D1(multiverse)과 U2(NMI 편향 지적)를 통합 대상으로 명시했다. adversarial-reviewer Round 2는 ET-P4를 "수용(SN-P7 격자에 흡수)"했고, SN-P7에 V11(원 결과 재현)과 주 경로 둘(H-shared, H-idio)을 더했다. 나는 그 산출물을 쓰지 않은 새 인스턴스지만, 역할의 이전 기여가 검토 대상에 들어 있다. 그래서 아래에서는 내 역할이 이전에 더한 요소도 같은 기준으로 비판한다(2.3절 E, F).

---

## 0. 요약

| 제안 | 최종 판정 | 한 줄 이유 | P5 처리 판정 |
|---|---|---|---|
| ET-P4 | **수정** | Horikawa 결론이 분석 선택에 얼마나 의존하는지 묻는 필수 전제 연구다. 그러나 (1) AMI의 상한이 없다(34범주 비율 평정을 이산 라벨로 바꾸면 달성 가능한 AMI가 낮다). (2) Horikawa는 5명이 같은 순서라 "세션"과 "클립 부분집합"이 완전히 겹친다. 순서가 독립인 Mind captioning이 이를 가를 수 있는데 설계가 이 대조를 쓰지 않는다. (3) 원 파이프라인 재현(V11)이 빠졌다 | **LIT-01 흡수는 맞다. 단 조건부.** LIT-01 분석 칸에는 개인 군집의 세션 간 재현(H-idio 주 경로), AMI와 교차검증 R², "측정 타당성" 해석 규칙, V11이 없다. 명시하지 않으면 ET-P4의 고유 기여가 사라진다 |
| EF-P4 | **재구성(연구 질문에서 검증 인프라로)** | P5 Novelty Constraint의 "기존 정서 라벨을 다른 Foundation Model로 예측"에 해당한다. 누수 통제 분할은 가치가 있다(Omni-fMRI의 정서 회귀는 무작위 블록 분할, 원문 확인). 안에 든 과학 질문 하나(피질하 token 의존도)는 시험 시점 masking의 분포 이탈과 피질하 tSNR 때문에 지금 설계로는 해석할 수 없다 | **LIT-34 처리(방향만 유지, 인프라)는 대체로 맞다.** 단 인프라라면 통과 기준(V2, V3, V5, V7)을 칸에 적어야 하고, 피질하 의존도는 matched null이 생기기 전까지 결과로 쓰지 않는다 |

---

## 1. 이번 추가 검토에서 확인한 사실

| # | 사실 | 근거 | 영향 |
|---|---|---|---|
| A1 | Azari et al. 2020 Discussion 2째 단락: 감독 분류는 우연 이상인데 비지도 군집은 라벨과 대응하지 않았고, 정서 관련 신호가 다른 신호보다 작으면 군집이 "time of day" 같은 부수 특징을 따를 수 있다고 적었다. 같은 논문은 합성 fMRI 자료로 GMM 민감도를 SNR별로 검증했다 | doi:10.1038/s41598-020-77117-8 [본문, PMC7679385] | ET-P4의 인용은 정확하다. 합성 자료 회복 검사의 선례가 이미 같은 연구진에 있으므로 V5를 바로 적용할 수 있다 |
| A2 | Omni-fMRI의 정서 검출은 StudyForrest의 블록을 7:1:2 **무작위 분할**로 3회 반복했다 | arXiv:2601.23090 4.2절, 부록 B.2 [arxiv.org HTML 본문] | EF-P4의 "유일한 정서 회귀는 무작위 블록 분할" 주장은 맞다 |
| A3 | CortexMAE 논문은 자체 평가 묶음(Brainmarks)에서 "형질 예측에서는 어떤 모델도 단순 FC 기준선을 뚜렷이 넘지 못했다"고 보고했다. 상태 예측(HCP 과제, NSD)은 별도 고정 분할 | arXiv:2510.13768 초록, 5절 [arxiv.org HTML 본문] | EF-P4의 FC 기준선은 형식이 아니라 실제로 이기기 어려운 기준선이다. 정서 과제는 Brainmarks에 없다 |
| A4 | Ke et al. 2025: 동적 FC로 영화 중 순간 arousal을 예측하는 모형이 다른 참가자, 다른 영화의 두 추가 데이터셋으로 일반화되었고, valence는 일반화되지 않았다 | doi:10.1371/journal.pcbi.1012994 [Crossref 초록] | 영화 단위 보류 일반화는 FC 모형에서는 이미 수행되었다. EF-P4의 새로움은 foundation model에 같은 엄밀성을 적용하는 데 한정된다 |
| A5 | Brain-JEPA 입력은 450 ROI(Schaefer-400 + Tian-50) x 160 시점, UK Biobank 휴지기로 사전학습 | arXiv:2409.19407 초록 [arxiv.org], 구조 세부는 encoding-foundation Round 1 표 [타 에이전트 확인] | 160 시점은 Emo-FilM(TR 1.3 s)에서 208 s, Spacetop(TR 0.46 s)에서 74 s다. 2.2절 D, E 참조 |
| A6 | Horikawa 2020 PMC 전문의 Methods는 "All methods can be found in the accompanying" Supplemental로 넘어간다. 원 voxel 선택 절차는 이번에도 1차 자료로 확인하지 못했다 | doi:10.1016/j.isci.2020.101060 [본문] | ET-P4의 "평정 기반 voxel 선택(Horikawa)" 수준을 정의하려면 보충 자료나 KamitaniLab 코드 확인이 먼저다(V11) |
| A7 | Horikawa 2020은 5명 모두 같은 제시 순서(2,196블록), Mind captioning과의 순서 상관은 Spearman -0.03 | vision-decoding Round 3 [계산, 타 에이전트 확인] | Horikawa 안에서는 "세션"과 "그 세션의 클립 부분집합"이 모든 피험자에게 같다. 2.1절 |

---

## 2. ET-P4: Horikawa/Westlin 불일치의 multiverse 격자 통합

### 2.0 제안 요약
요인 A 입력 공간(전뇌 PCA / fold 안 평정 기반 voxel 선택 / network subspace / 평정 독립 피험자 간 신뢰 부분공간) x 요인 B 전역, 세션, run 분산 처리 x 요인 C 군집 수 선택(BIC / 고정 27 / DP-GMM) x 요인 D 지표(AMI + 순열 기준, 군집 지시변수로 연속 평정을 예측하는 교차검증 R²). 추가로 Westlin 개인 군집의 피험자 내 세션 분할 재현성, "규범 평정과 대응하는 신경 구조의 측정 타당성"이라는 해석 규칙, Mind captioning 외부 재현. 받는 쪽 systems-neuro는 수용하며 코호트 요인과 파이프라인 요인 분리, network별 tSNR 공변량을 더했다.

### 2.1 핵심 문제 두 가지 (기존 응답에 없던 것)
1. **AMI에는 상한이 없다.** Cowen & Keltner 평정은 클립마다 34범주 선택 비율이다. AMI를 계산하려면 클립마다 이산 라벨(예: 최빈 범주)이 필요한데, 혼합 정서 클립이 많고 경계가 연속적이라 최빈 라벨 자체가 잡음이다. 따라서 "신경 군집과 평정의 AMI가 낮다"는 결과는 (a) 범주 구조가 없거나 (b) 라벨 이산화와 fMRI SNR 때문에 달성 가능한 AMI가 원래 낮은 경우를 가르지 못한다. Westlin의 평정 NMI 0.014(내 Round 1 기록)도 이 상한과 비교해야 의미가 있다. 평정자별 원자료가 비공개라 평정 split-half로 상한을 낼 수 없다(Stage 1). 대안은 **합성 자료 상한**이다. 실제 34차원 평정을 선형으로 투영한 신호에 실측 잡음(위상 무작위화 잔차)을 실측 SNR로 더해, 같은 파이프라인이 낼 수 있는 AMI 분포를 구한다. Azari 2020이 같은 원리로 GMM 민감도를 검증했다(A1). 교차검증 R²(요인 D)는 연속 평정을 쓰므로 이 문제가 덜하지만, 그 상한도 같은 합성 절차로 낸다.
2. **Horikawa의 "세션 대응"은 시간 효과와 클립 내용 효과가 섞여 있고, Mind captioning이 이를 가를 수 있다.** 5명이 같은 순서로 봤으므로(A7) 세션 s에 들어간 클립 집합은 모든 피험자에게 같다. Westlin의 군집-세션 NMI 0.19는 (i) 세션별 전역 드리프트, 각성, 장비 상태(시간 효과)일 수도 있고 (ii) 그 세션 클립 집합의 내용 차이일 수도 있다. Mind captioning은 순서가 독립이라 같은 클립이 다른 세션에 들어간다. 그러므로 **Mind captioning 자료로 만든 군집이 Mind captioning 자신의 세션과 대응하는지(시간 효과), Horikawa 세션의 클립 집합과 대응하는지(내용 효과)** 를 나란히 보면 둘을 직접 가를 수 있다. ET-P4는 Mind captioning을 "외부 재현"으로만 두어 이 판별력을 쓰지 않는다. GI-P1의 코호트 간 쌍 논리와 같은 원리를 군집 multiverse에 적용하는 것이다.

### 2.2 P3 판정과 추가 점검

| 항목 | 판정 | 근거 |
|---|---|---|
| P3-1 이미 연구 | **partially** | Westlin 2025(arXiv:2507.00320, 초록: 최소 가정 재분석에서 원 대응 미관찰, 개인 간 변동) 자체가 한 갈래의 대안 분석이다. Azari 2020(A1)은 세 데이터셋에서 감독 대 비지도 불일치를 보였다. 감정 fMRI의 multiverse는 Bloom et al. 2022(편도체-mPFC 발달, specification curve, WebSearch 결과 [search_index], 식별자 미확인이라 근거로 세지 않음)가 있으나 정서 범주 군집은 아니다. Horikawa 데이터의 multiverse나 specification curve는 내 검색(WebSearch, 2026-11-12)과 emotion-theory, systems-neuro 검색 모두에서 미발견 |
| P3-2 단순 적용 | 아니다. 메타과학(Axis T) 설계 | |
| P3-3 Neuroscience Q | 조건부 예. 직접 답하는 것은 "Horikawa의 범주 군집 결론이 어떤 분석 선택에 기대는가"이고, 정서 이론(범주 대 구성)에는 "측정 타당성" 수준으로만 말한다(제안의 해석 규칙에 동의). Horikawa 기반 다른 질문(LS-P1, GI-P1, GC-P2)의 전제 점검이라는 점이 가장 큰 가치다 | |
| P3-4 정서 아닌 요소 | 높음. 세션/클립 부분집합 교락(2.1), 전역 자율신경 성분(systems-neuro), 두 코호트 모두 자유 시청이라 시선(본 검토 F1), 클립 길이와 반복 재생 횟수 | |
| P3-5 데이터 | 가능. Horikawa raw(CC0)와 Mind captioning 보유. 원 voxel 선택 절차는 보충 자료 확인 필요(A6). Mind captioning 공개 전처리본은 12개 전역 신호 회귀본(systems-neuro)이라 raw에서 같은 파이프라인 재처리가 전제 | |
| P3-6 더 강력한 방법 | (1) 합성 자료 상한(2.1-1). (2) Mind captioning 시간 대 내용 판별(2.1-2). (3) 개인 군집 재현은 세션 간 군집 중심 대응(Hungarian)보다 **예측 강도(prediction strength)** 방식이 낫다. 한 세션 묶음으로 학습한 군집 모형이 다른 세션 묶음의 배정을 얼마나 재현하는지 보는 것이다. 세션 묶음은 클립도 다르므로 "클립을 넘는 개인 구조의 재현"을 직접 잰다. (4) 범주 대 연속 판정은 혼합 모형 대 연속 잠재 모형의 held-out 우도 비교(vision-decoding 제안, LIT-01에 반영됨) | |
| P3-7 기대와 다를 때 | 의미 있다. 단 "어떤 경로에서도 범주 대응 없음"이 상한 대비 해석되어야 하고, "개인 구조 재현 없음"은 예측 강도의 null 분포(라벨 순열이 아니라 같은 SNR의 무구조 합성 자료) 대비 해석되어야 한다 | |
| C 순환과 누수 | (1) 평정 기반 voxel 선택을 fold 안에서 한다는 점은 원 분석의 순환 가능성을 직접 시험하는 좋은 수준이다. 원 경로(전체 자료로 선택)와 fold 안 경로의 차이가 곧 "선택 순환이 범주 구조를 얼마나 만들었는가"의 추정치다. (2) 신뢰 부분공간은 다른 피험자의 같은 클립으로 학습하되, 군집을 평가하는 클립과 부분공간을 학습하는 클립을 나눠야 한다(GI-P1과 같은 원칙). (3) Mind captioning 피험자 중복 미확인 | |
| D 인과 | 제안 스스로 R0와 측정 타당성으로 한정했다. 문제 없음 | |
| E 규모 | 내 역할이 Round 2에서 제안한 상한 "81 명세/피험자"와 guided multiverse에도 문제가 있다. guided multiverse는 결과 공간의 극단을 능동적으로 찾는 표집이라, 결과 열람 전 고정(V10) 없이 쓰면 선택 보고의 통로가 된다. 전체 격자를 먼저 고정하고 표집 규칙도 사전등록해야 한다. 계산량 자체는 현실적(5 + 6명, 블록 평균 자료) | 자기 비판 |
| F 통계 | 11명. 피험자별 판정 + 유병률(doi:10.7554/eLife.62461). specification curve의 결합 검정은 명세끼리 강하게 의존하므로 순열 기반이어야 한다(doi:10.1038/s41562-020-0912-z). 내 Round 2가 제안한 "주 경로 둘(H-shared, H-idio)" 각각에 다중비교 보정을 따로 둔다 | |
| G 인용 | 3절 | |

### 2.3 V1~V12 (현재 → 개선 후)

| 요건 | 현재 | 개선 후 | 메모 |
|---|---|---|---|
| V1 경쟁 설명, matched null | △ | ○ | 세션 구조 보존 순열(run 안 순환 이동), 세션 안 클립 라벨 셔플, 무구조 합성 자료 |
| V2 상한과 신뢰도 | × | △ | 합성 자료 AMI, R² 상한. 평정자 원자료 비공개라 실측 상한은 불가 |
| V3 chance 보정, 의존 구조 null (v3) | ○ | ○ | AMI와 순열 기준이 이미 제안됨. 사람 수준 주장(H-idio)은 피험자별 판정 후 유병률 |
| V4 신뢰도 민감도 | △ | ○ | 교차검증 R²의 평정 신뢰도 가정 sweep |
| V5 회복 검사 | × | ○ | Azari 2020식 합성 자료, 실측 잡음 기반 |
| V6 학습 무작위성 | △ | ○ | 재초기화 안정성과 세션 간 재현을 구분(제안에 있음), 예측 강도로 정식화 |
| V7 누수 경로 | △ | ○ | fold 안 선택, 부분공간 학습/평가 클립 분리, 피험자 중복 확인 |
| V8 일반화 수준 | △ | ○ | 클립 일반화(세션 간), 피험자 유병률, 코호트 일반화를 따로 |
| V9 라벨 출처 | ○ | ○ | felt x 별도 평정자 규범, AI 라벨 없음 |
| V10 사전 고정 | △ | ○ | 주 경로 둘, 격자와 표집 규칙 고정 |
| V11 원 결과 재현 | × | ○ | Horikawa 원 경로(보충 자료 확인 후)와 Westlin 원 경로로 원 수치 회복 |
| V12 반증 해석 | ○ | ○ | 해석 규칙 있음, 상한 대비 해석 추가 |
| S1~S3 | S3 준수 | S2 가능 | Mind captioning 재현이 S2 조건 |

### 2.4 판정: **수정**
* 개선안 요약: 0단계 V11 재현 → 합성 자료 상한 → 격자(요인 A~D + 코호트, 파이프라인 요인) → 주 경로 둘(H-shared: 신뢰 부분공간, H-idio: 예측 강도 기반 세션 간 재현) → Mind captioning 시간 대 내용 판별.
* **P5 처리(LIT-01) 판정:** 같은 질문이므로 흡수는 맞다. 그러나 LIT-01의 `measurable_prediction_or_analysis` 칸은 공유 스펙트럼과 범주 대 연속 비교 중심이고, ET-P4 고유 요소(H-idio 주 경로, AMI와 교차검증 R², 측정 타당성 해석 규칙)와 V11, 2.1의 두 문제가 적혀 있지 않다. 이 넷을 LIT-01에 명시하는 조건으로 처리를 지지한다.

---

## 3. EF-P4: 뇌 입력 foundation model 정서 latent의 누수 통제 benchmark

### 3.0 제안 요약
(i) leave-one-film-out과 leave-subject-out, 시간 블록 사이 HRF와 자기상관 길이 이상의 buffer, (ii) coverage 대조(CortexMAE-F 피질만, CortexMAE-P + Tian, Brain-JEPA의 Tian 피질하 token masking, NeuroSTORM volume), (iii) 기준선 FC, 원시 parcel 시계열, TRIBE v2 자극 예측, (iv) Spacetop 본인 평정 head와 Emo-FilM 규범 평정 head 분리, (v) 피질하 ROI tSNR, dropout 보고. 받는 쪽 systems-neuro는 수용하며 생리 회귀 전후 반복, Mind captioning 전역 신호 회귀본 표기, tSNR 기준 통과 피험자에서만 masking 해석을 더했다.

### 3.1 핵심 문제 세 가지 (기존 응답에 없던 것)
1. **시험 시점 token masking은 정보 의존도가 아니라 분포 이탈을 잰다.** 사전학습과 probe 학습 때 늘 있던 피질하 50개 token을 시험 때만 지우면 입력 분포가 바뀐다. 성능이 떨어져도 "피질하에 정서 정보가 있다"인지 "모델이 낯선 입력에 약하다"인지 구분되지 않는다. 필요한 대조: (a) **matched null**: 같은 수(50개)의 피질 token을 tSNR이 비슷한 것으로 골라 지운 판, (b) probe를 masking 입력으로 다시 학습한 판(정보 손실만 남김), (c) 피질하 token을 같은 피험자의 다른 시점 값으로 바꾼 판(분포 유지, 정보 제거). systems-neuro의 tSNR 조건은 필요조건일 뿐 이 혼동을 풀지 못한다.
2. **시간 창과 라벨 해상도가 맞지 않는다.** Brain-JEPA 입력 160 시점은 Emo-FilM에서 208 s, Spacetop에서 74 s다(A5). Emo-FilM 영화당 6.7~17.1분이라 창을 겹치지 않게 자르면 피험자당 약 46개 창이고, 1 Hz 평정을 208 s로 평균하면 정서 변화의 대부분이 사라진다. Spacetop alignvideo는 20 s~5분 39초라 74 s 창이 짧은 영상에서는 평정 구간(운동 반응)이나 다음 영상까지 넘어간다. 창을 영상 안으로 제한하고, 풀링 latent 대신 시간 patch 단위 출력에 probe를 붙이며, 창이 평정 구간을 포함하지 않게 하는 규칙이 필요하다. TR이 사전학습(UK Biobank)과 다른 데이터에서의 시간 재표본 방식도 결과를 바꾼다.
3. **Spacetop 본인 평정 head는 본 검토 2.2절의 퇴화 문제를 그대로 안는다.** 영상 단위 본인 평정을 latent로 예측하면 성능의 대부분은 영상 사이 차이(48점)에서 온다. 그 경우 "본인 평정 head"와 "규범 head"의 차이는 라벨 주체의 차이가 아니라 같은 영상 수준 신호의 두 잡음 판이다. 본인 평정 head는 영상 안 사람 간 성분(양방향 중심화, V3 v3)과 영상 사이 성분을 나눠 보고해야 라벨 head 분리(iv)가 의미를 갖는다.

### 3.2 P3 판정과 추가 점검

| 항목 | 판정 | 근거 |
|---|---|---|
| P3-1 이미 연구 | **partially** | 정서 회귀를 한 foundation model 평가는 Omni-fMRI(무작위 블록 분할, A2). 평가 묶음 자체는 Brainmarks(A3)와 Omni-fMRI benchmark(11개 데이터셋)가 있다. 영화 단위 보류 일반화는 FC 모형에서 Ke 2025(A4). NeurIPS 2026 "When Audio Residuals Are Still Visible: A Faithfulness Audit for Foundation-Model-Based fMRI Decoding"은 우회 경로 감사라는 인접 주제다([search_index], 식별자 미확인, 근거로 세지 않음). foundation model에 영화 단위 보류와 buffer를 적용한 정서 benchmark는 내 검색(WebSearch, PubMed, 2026-11-12)에서 미발견 |
| P3-2 단순 적용 | **그렇다에 가깝다.** P5 Novelty Constraint가 명시한 "기존 정서 라벨을 다른 Foundation Model로 예측"이다. 누수 통제와 coverage 대조가 방법론적 기여지만, 과학 질문은 피질하 의존도 하나이고 그것은 3.1-1 때문에 지금 설계로 답하지 못한다 | |
| P3-3 Neuroscience Q | 현재로는 아니오. 재구성하면 "휴지기 사전학습이 영화 중 정서 관련 상태 구조를 FC 이상으로 압축하는가"(표상 학습 질문)는 답할 수 있으나, 정서 경험의 신경 표상에 대해 새로 알게 되는 것은 적다 | |
| P3-4 정서 아닌 요소 | 높음. 휴지기 latent가 가장 쉽게 담는 것은 전역 자율신경 성분과 각성(systems-neuro), 영화 정체성과 장르(제안자 인정), 시청각 내용 강도(TRIBE 기준선이 일부만 통제). Ke 2025에서 일반화된 것이 arousal뿐이라는 점(A4)은 latent가 정서 범주보다 각성 축을 주로 담을 가능성을 시사한다 | |
| P3-5 데이터 | Emo-FilM raw 재전처리, Spacetop CIFTI는 가능. Horikawa 공개본은 블록 평균이라 시계열 모델에 쓸 수 없고 raw가 필요하다. Mind captioning 공개 전처리본(전역 신호 회귀)은 사전학습 전처리와 달라 분포 이탈이 생긴다. Brain-JEPA LICENSE 미확인(제안자 인정), NeuroSTORM 라이선스 표기 불일치(encoding-foundation Round 1) | |
| P3-6 더 강력한 방법 | (1) 3.1-1의 matched null. (2) 같은 차원으로 맞춘 linear probe(FM latent, FC, raw parcel 모두 PCA 동수)로 probe 용량 차이를 없앤다. (3) 정서 특이성 대조로 같은 영화의 비정서 주석(예: 장면 밝기, 대사 유무, 인물 수)을 같은 probe로 예측해, latent가 정서를 특별히 담는지 일반 내용을 담는지 비교 | |
| P3-7 기대와 다를 때 | FM이 FC를 못 넘어도(Brainmarks 형질 결과처럼) 의미 있는 음성 결과다. 다만 그것은 인프라 결과이지 정서 이론 결과가 아니다 | |
| C 순환과 누수 | 분할과 buffer는 좋다. 추가: (1) 사전학습 목록 확인은 encoding-foundation이 했다고 기록했으나[타 에이전트 확인], CortexMAE "2.1K hours of open fMRI"의 구성에 OpenNeuro의 Emo-FilM(ds004892), Spacetop(ds005256)이 들어 있는지는 판본별로 다시 확인한다. (2) 창이 평정 구간을 포함하면 운동 반응이 라벨과 섞인다(Spacetop). (3) 영화 내 변동 probe(제안자)는 좋은 장치다 | |
| D 인과 | "피질하 의존도"는 masking 실험이라 개입처럼 보이지만 모델 안 개입(R1)이다. 뇌 피질하의 역할로 해석하지 않는다 | S3 |
| E 규모 | 모델 4종 x 데이터셋 2~3개 x 라벨 head 2 x 분할 2 x 생리/전역 처리 2. GPU 추론은 현실적이나 비교 표가 커서 "가장 좋은 모델" 보고로 흐르기 쉽다 | |
| F 통계 | 1 Hz 라벨 자기상관 때문에 시간 단위 표본 수를 독립으로 세면 안 된다. 영화 단위(14개) 신뢰구간, 순환 이동 null. 비교 수가 많아 사전 지정 주 대비 하나(FM latent 대 FC, 같은 probe 용량, 영화 단위 보류)만 확증, 나머지는 탐색 | |
| G 인용 | 3절 | |

### 3.3 V1~V12 (현재 → 개선 후)

| 요건 | 현재 | 개선 후 | 메모 |
|---|---|---|---|
| V1 경쟁 설명, matched null | △ | ○ | FC, raw parcel, TRIBE 기준선은 있음. masking matched null과 비정서 주석 대조 추가 |
| V2 상한과 신뢰도 | × | △ | Emo-FilM 평정자 원자료로 라벨 신뢰도 상한(평정자 쌍 r 0.21~0.60, Stage 1) |
| V3 chance 보정, 의존 구조 null (v3) | × | ○ | 순환 이동 null, 영화 단위 신뢰구간, Spacetop 본인 평정 head는 양방향 중심화로 성분 분리 |
| V4 신뢰도 민감도 | NA | NA | 증분 고유 분산 주장이 아님 |
| V5 회복 검사 | × | ○ | 실측 자료에 알려진 정서 관련 신호를 심어 probe 회복률과 분할별 누수 크기를 잰다 |
| V6 학습 무작위성 | △ | △ | 사전학습 시드는 통제 불가, probe 시드와 창 위치 변형만 |
| V7 누수 경로, 등록부 | ○ | ○ | 분할과 buffer 있음. 창-평정 구간 겹침, 사전학습 판본 재확인 추가 |
| V8 일반화 수준 | △ | ○ | 새 피험자와 새 영화를 따로 보고 |
| V9 라벨 출처 | ○ | ○ | head 분리 |
| V10 사전 고정 | × | ○ | 주 대비 하나 |
| V11 원 결과 재현 | × | ○ | Omni-fMRI 무작위 분할 결과를 같은 데이터(StudyForrest 공개)로 재현한 뒤 영화 단위 분할로 바꿔 누수 크기를 직접 보인다. 이것이 benchmark의 가장 설득력 있는 첫 결과다 |
| V12 반증 해석 | △ | ○ | FM이 FC 이하일 때의 해석을 사전 기술 |

### 3.4 판정: **재구성(연구 질문에서 검증 인프라로)**
* 인프라로서의 산출물: (1) foundation model 기반 정서 주장을 위한 분할, buffer, 창 규칙, 사전학습 판본 확인 절차(V7의 FM용 구현), (2) Omni-fMRI 재현과 수정 분할 비교(V11), (3) 같은 용량 probe의 FM 대 FC 비교표. 이것을 다른 FM 기반 질문의 관문으로 쓴다.
* 피질하 의존도 질문은 3.1-1의 세 대조가 갖춰지고 SN-P3 signal-feasibility 관문을 통과한 뒤에만 별도 탐색 질문으로 다룬다.
* **P5 처리(LIT-34) 판정:** "방향만 유지, 검증 인프라로 사용"은 대체로 맞다. 다만 LIT-34의 `measurable_prediction_or_analysis`와 `scientific_contribution` 칸이 비어 있고 상태가 일반 후보와 같은 `kept`다. 인프라라면 통과 기준(V2, V3, V5, V7, V11)을 칸에 적고, 피질하 의존도는 matched null 전까지 결과로 쓰지 않는다는 조건을 `note`에 넣을 것을 권한다.

---

## 4. 인용 표본 점검

| 제안 | ID | 존재 확인 경로 | 주장된 내용과 일치하는가 |
|---|---|---|---|
| ET-P4 | doi:10.1038/s41598-020-77117-8 | PubMed 전문 | ○ Discussion 2째 단락의 "정서 신호가 작으면 비지도 군집은 부수 특징을 따른다"와 일치(A1) |
| ET-P4 | arXiv:2507.00320 | arxiv.org abs | ○ 초록 수준 일치. 인용된 "Results; Discussion 6째 단락"의 세부 위치는 arxiv.org HTML 판이 없어 이번에 확인하지 못함 |
| ET-P4 | doi:10.1038/s41593-025-01945-y | Crossref | ○ 제목(Autonomic physiological coupling of the global fMRI signal) 일치. 내용은 systems-neuro 원문 확인[타 에이전트 확인] |
| EF-P4 | arXiv:2601.23090 | arxiv.org HTML 본문 | ○ 정서 검출은 StudyForrest 무작위 7:1:2 분할(A2) |
| EF-P4 | arXiv:2510.13768 | arxiv.org HTML 본문 | ○ CortexMAE, flat map, Brainmarks. 형질 예측에서 FC 기준선을 넘기 어렵다는 결과도 있어 EF-P4의 기준선 설계를 지지(A3) |
| EF-P4 | arXiv:2409.19407 | arxiv.org abs | ○ Brain-JEPA, 인구통계, 질환, 형질 예측과 linear probing. 정서 평가는 없음 |
| EF-P4 | doi:10.1371/journal.pcbi.1012994 | Crossref 초록 | ○ 동적 FC arousal 모형의 데이터셋 간 일반화(A4). 이 논문은 EF-P4의 새로움 범위를 좁히는 선행이기도 하다 |
| EF-P4 | arXiv:2506.11167 | arxiv.org abs | ○ NeuroSTORM. "state classification"이 하위 과제에 있음(encoding-foundation은 그 "Emotion"이 HCP Hariri 과제 상태 분류라고 기록) |

요약: 8개 중 식별자 오류 0, 내용 오독 0, 위치 미확인 1(Westlin 세부 위치).

---

## 5. 정정 상위 10개 전체에 대한 덧붙임
* 정정 목록에서 빠진 GC-P2, BI-P2 검토는 지시대로 본 검토에 그대로 둔다.
* 정정 상위 10개 중 ET-P4와 GI-P1은 같은 프로그램(LIT-01)이고, EF-P3, ET-P2, LS-P2, GI-P5는 같은 설계(묶음 A)다. 정정 후에도 10자리 중 6자리가 두 설계에 쓰인다. 같은 설계의 변형을 한 번만 세자는 본 검토 9.4절 권고를 다시 적는다.

---

## 6. 검색 기록 (모두 2026-11-12)

| 대상 | 경로와 질의 | 결과 |
|---|---|---|
| ET-P4 | WebSearch `multiverse OR "specification curve" analysis emotion category fMRI clustering reanalysis analytic choices 2024 2025 2026` | 정서 범주 군집 multiverse 미발견. 편도체-mPFC 발달 multiverse(Bloom 2022, search_index) |
| ET-P4 | PubMed 검색과 전문 PMC7679385(Azari 2020), PMC7191651(Horikawa 2020) | A1, A6 |
| ET-P4 | arxiv.org HTML arXiv:2507.00320 | HTML 판 없음(596자 응답), 세부 위치 미확인 |
| EF-P4 | WebSearch `fMRI foundation model emotion decoding naturalistic movie benchmark data leakage leave-one-movie-out Brain-JEPA NeuroSTORM 2025 2026` | FM의 영화 단위 보류 정서 benchmark 미발견. Ke 2025, TRIBE v2 정서 평가와 faithfulness audit(둘 다 NeurIPS 2026, search_index) |
| EF-P4 | PubMed `("foundation model" OR "pretrained" OR "self-supervised") AND fMRI AND (emotion* OR affective OR arousal OR valence) AND (decoding OR prediction) AND (movie OR naturalistic OR film)`, 2023~ | 1건, 무관 |
| EF-P4 | arxiv.org abs 4건(2510.13768, 2409.19407, 2506.11167, 2601.23090), HTML 본문 2건(2510.13768, 2601.23090), api.crossref.org 4건 | A2~A5, 4절 |

## 7. 미확인 사항
* Horikawa 2020 원 voxel 선택 절차(보충 자료), Westlin 2025의 NMI 수치와 Discussion 6째 단락 위치(내 Round 1 기록에 의존).
* CortexMAE 사전학습 판본에 Emo-FilM, Spacetop이 들어 있는지(판본별 재확인 필요).
* Brain-JEPA, NeuroSTORM 가중치 라이선스.
* Bloom 2022, NeurIPS 2026 faithfulness audit의 식별자.
