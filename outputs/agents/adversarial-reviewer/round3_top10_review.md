# Stage 3 Round 3: 상위 10개 제안 검토 (adversarial-reviewer)

* 작성: adversarial-reviewer의 새 인스턴스. 검토 대상 10개(EF-P3, ET-P2, GI-P5, LS-P1, BI-P1, GI-P1, LS-P2, GC-P2, GI-P2, BI-P2) 중 어느 것도 만들지 않았다. 기준일 2026-11-12.
* 절차: `prompts/stage3_discussion_combination.md` 2절 3번, `reference/protocols.md` P3(판정 7개), CLAUDE.md 6절. 요건표는 `outputs/agents/adversarial-reviewer/round2.md` 2절의 V1~V12와 S1~S3.
* 읽은 자료: 각 제안 원문(보낸 에이전트 round2.md 2절), 받는 에이전트 응답(round2.md 3절), Round 3 검토(systems-neuro, brain-inspired의 GI-P5 / frontier-ai, geometry-info의 LS-P1 / multimodal-dynamics, frontier-ai의 BI-P1 / vision-decoding, multimodal-dynamics의 GI-P1 / systems-neuro, emotion-theory의 GC-P2 / generative-counterfactual, encoding-foundation의 BI-P2), `outputs/discussion/top10_for_review.md`, `round3_assignment.md`, `responses_tally.csv`, `tally_responses.py`, `outputs/stage1/dataset_intelligence_report.md`, `dataset_Spacetop.md`, `outputs/STAGE_STATUS.md`.
* 일부러 읽지 않은 것: `outputs/discussion/round3_summary.md`(Coordinator 요약). 독립 판단을 위해 열지 않았다.
* 표기: [본문] 원문 직접 확인, [초록] 초록만, [Crossref] 서지만, [계산] 공개 데이터로 직접 계산, [시뮬레이션] 이번에 돌린 모의실험, [추론], [타 에이전트 확인]. 근거 ID는 식별자 경로로 확인한 것만 쓴다.
* 이 파일 외에는 아무 파일도 고치지 않았다. 새로 확인한 문헌은 12절에 목록으로만 둔다(literature.jsonl 갱신은 이번 지시 범위 밖).

---

## 0. 요약

### 0.1 최종 판정

| 제안 | 묶음 | 최종 판정 | 한 줄 이유 |
|---|---|---|---|
| EF-P3 | A | **재구성** | 핵심 성분 "(b) peer 평균 - (a) TRIBE 예측 = 공유되지만 자극으로 계산되지 않는 성분"은 해석이 틀렸다. 여러 사람이 공유하는 반응은 정의상 자극에 묶인 반응이고, 이 차이는 TRIBE의 오적합과 영역 이동이다. 영상 수준(49점) encoder 적합도 진단으로 옮긴다 |
| ET-P2 | A | **수정** | 본인 보고 편차의 측정 모형(척도 사용 분리, 신뢰도 보고, 반증 기술)은 통합 설계의 핵심으로 채택. "privileged access" 해석과 B1~B4 순차 통제 논리는 고친다(2.2절) |
| GI-P5 | A | **재구성** | 중심 전제 "기준선 간 차이 자체가 결과"가 사람 수준 질문에서 성립하지 않는다. 사람마다 같은 기준선(TRIBE, LOO peer 평균, MLLM)은 영상 고정효과 아래 수학적으로 동치다. 잔차 신뢰도 관문과 rank 대역 부분공간만 남긴다 |
| LS-P2 | A | **수정** | 두 잔차 정렬은 유지. 그러나 TRIBE(뇌)와 MLLM(보고) 기준선을 짝지으면 사람 수준 연결이 0이어도 r 약 +0.36의 가짜 효과가 나온다[시뮬레이션]. MLLM으로 결측 평정을 보간하는 안은 폐기 |
| LS-P1 | 단독(GC-P2와 연결) | **수정, 우선순위 높음** | 질문과 데이터 적합성은 가장 좋다. 가장 가까운 선행 Abdel-Ghaffar 2024(의미-정서 공동 tuning)가 빠졌고, 차원 비대칭 분할, 출처 영상 단위 누수, 원 결과 재현(V11)을 보완해야 한다 |
| GC-P2 | 단독(LS-P1의 2단계) | **수정** | 제안이 근거로 든 arXiv:2610.13558이 이미 TRIBE v2로 정서 편집 400쌍의 영역별 예측 반응을 분석했다(R1 팔의 부분 선행). 같은 데이터로 voxel을 고르고 encoder를 학습하는 순환, encoder 유도 편집의 순환을 막아야 한다 |
| GI-P1 | 단독 | **수정, 우선순위 높음** | 두 코호트 순서 독립(Spearman -0.03)으로 설계 논리가 살아났다. Horikawa 2020도 자유 시청임을 원문으로 확인했으므로 시선 교란은 두 코호트 모두에 걸린다. 원 파이프라인 재현(V11)과 쌍 의존성 처리가 빠졌다 |
| GI-P2 | B | **수정** | A = (T - T')/2는 정상분포가 균등하지 않으면 순 확률 흐름이 아니다. 결합 전이 빈도로 흐름과 엔트로피 생산을 다시 정의하면 저비용 관문으로 유지 |
| BI-P1 | B | **재구성** | SR(T) 대 SR(T')는 시간 역전 사슬이 아니고(multimodal-dynamics 지적), 대칭 RDM으로는 방향을 M M'와 M' M의 차이로만 간접 관측한다. 주 검정을 시간 지연 전향/후향 예측과 내용 상태 경쟁 모형으로 바꾼다 |
| BI-P2 | 단독 | **수정** | 동기로 든 Horikawa 2020의 "(or affordances)"는 행동 affordance가 아니라 "특정 정서를 일으킬 것이라는 시각적 추론"이다[본문]. 동기를 Frijda/CPM과 Thornton & Tamir 2024로 다시 세우고 0단계 공선성 관문을 둔다 |

상위 10개 중 전체 기각은 없다. 다만 다음 네 주장은 기각(또는 정정)한다: EF-P3의 (b)-(a) 해석, GI-P5의 "사람 수준 기준선 multiverse", BI-P2의 Horikawa affordance 근거, GI-P2의 A = 순 흐름 정의.

### 0.2 가장 중요한 지적 3개

1. **묶음 A의 기준선 multiverse는 대부분 퇴화되어 있고, 짝짓기에 따라 가짜 효과를 만든다(2.2절).** 사람마다 같은 기준선은 같은 영상 안에서 상수라 사람 간 비교에서 서로 구별되지 않는다. 차이는 영상 수준(49점)에서만 생기고, 두 모델의 영상 수준 오적합이 서로 상관하면 사람 수준 연결이 없어도 within-person r 약 +0.36이 나온다[시뮬레이션, 200회]. 사람과 영상 양방향 중심화(또는 영상 고정효과)를 주 분석으로 고정하면 사라진다. 가장 가까운 선행 Woo et al. 2017(SIIPS1, 자극 강도 너머의 통증 보고를 예측하는 뇌 신호)이 네 제안 어디에도 없다.
2. **방향성 묶음(GI-P2, BI-P1)에 수학 오류가 둘 있고, 그중 하나는 내 Round 2 요건표(V1)에도 들어가 있다(3절, 10절).** T의 반대칭 부분은 순 흐름이 아니며(π 가중 필요), 전치 T'는 시간 역전 사슬이 아니다. adversarial-reviewer Round 2는 SR(T')를 "깨끗한 matched null"로 받아들여 V1 문구에 넣었다. 정정한다.
3. **인용 표본 점검에서 근거 오독 1건, 근거 안에 숨은 선행 1건(8절).** BI-P2는 Horikawa 2020의 "(or affordances)"를 행동 affordance로 읽었고 Round 3 검토자 두 명도 그대로 반복했다. GC-P2가 근거로 든 arXiv:2610.13558은 GC-P2의 R1 팔과 겹치는 선행이다.

### 0.3 합의 쏠림 판단(9절)
Round 2 응답 96건 반박 0건, Round 3 검토 30건 기각 0건이다. 수용률이 제안의 질을 반영한다고 보기 어렵다. (1) 검증 가능한 오류 4건이 수용을 통과했다(EF-P3 (b)-(a), GI-P2의 A, BI-P1의 T', BI-P2의 affordance 근거). (2) P2 양식이 "너희 쪽 X를 우리 쪽 Y로"라서 받는 쪽은 자기 아이디어가 들어간 병합안을 받는다. (3) 상위 10개 선정 점수에 Round 3 검토 파일의 언급이 들어가, Round 3에 배정된 제안은 이 항목으로 평균 약 1.1점(미배정은 약 0.07점)을 더 받았다[계산]. Round 2 파일만 세면 BI-P2와 GC-P2는 상위 10개 밖이다. 판단: 제안의 질보다는 양식 효과와 동의 편향이 크다. 반대 근거(실질적 수정이 많았다는 점)도 함께 적었다.

---

## 1. 이번 검토에서 새로 확인한 사실

| # | 사실 | 근거와 수준 | 영향 |
|---|---|---|---|
| F1 | **Horikawa 2020 참가자도 자유 시청했다.** "we allowed the subjects to freely view presented video stimuli", 시선 차이가 뇌 자료에 영향을 줄 수 있다고 저자가 한계로 적음 | doi:10.1016/j.isci.2020.101060 Discussion 마지막 단락 [본문, PubMed 도구 PMC7191651] | vision-decoding은 "Horikawa 시청 지시 미확인"으로 두었다. 시선 교란은 두 코호트 모두에 걸린다(GI-P1, LS-P1) |
| F2 | **Horikawa 2020의 "affordances"는 정서 affordance다.** "these regions encode either emotional experience or visual affordances for specific emotional experiences (e.g., the inference that a landscape is likely to inspire awe)". PMC 전문에서 affordance는 서론 마지막 단락에만 두 번 나온다 | 같은 논문 [본문] | BI-P2가 "Discussion 2째 단락"으로 인용한 근거의 내용과 위치가 모두 맞지 않는다(7절, 8절) |
| F3 | **Spacetop alignvideo 결측은 시행/런 단위 전부-또는-없음 구조이며, 값에 따른 선택적 결측의 증거는 없다.** 부분 결측 참가자 42명의 (참가자, 영상) 1,813개 중 0개 결측 616, 7개 모두 결측 741. 차원별 결측률 0.504~0.524로 바닥 효과 항목(disgusted 중앙값 1.9)과 engaged(중앙값 45)가 같다. 혼합 시행에서 결측 항목과 응답 항목의 peer 평균 차이 없음. 응답값 중 1 이하 비율 disgusted 0.39, afraid 0.30(시작점에서 바로 클릭하는 응답이 흔함) | OpenNeuro ds005256 events.tsv 1,369개, 116명 [계산, 스크립트는 12절] | 나는 "커서가 'Barely at all'에서 시작하고 클릭해야 저장되므로 낮은 값이 선택적으로 빠진다"는 가설을 세웠으나 **계산으로 지지되지 않았다.** 남는 위험은 시행 단위 결측이 졸음, 이탈 같은 상태와 묶일 가능성이다 |
| F4 | **Spacetop 유효 표본.** 완료율 0.5 이상 57명, 0.8 이상 40명, 하나라도 있음 109명. 49개 시청 슬롯 모두 모든 참가자에게 같은 영상, 고유 영상 내용 48개(tornado 2회) | [계산] | 묶음 A의 개인 수준 분석은 실질적으로 약 40~57명, 사람당 약 24~39개 영상이다 |
| F5 | Spacetop 원 논문은 다른 과제(task-social, shortvideo)에 "시작점 편향을 줄이려고" 반원형 gLMS를 썼고, alignvideo는 "Barely at all~Strongest imaginable" 선형 척도를 썼다. 생리(EDA, PPG)는 동시 기록되었다 | doi:10.1038/s41597-025-05154-x Methods [본문, PMC12373947] | 척도 시작점 편향은 alignvideo에만 남아 있다(F3에서 결측과는 무관함을 확인). 생리는 미공개(Stage 1) |
| F6 | **공개 TRIBE 모델은 피험자 평균 모델이다.** "unavailable from the subject-averaged released model" | arXiv:2607.01400 초록 [arxiv.org abs] | EF-P3의 (a) 기준선은 Spacetop과 다른 모집단, 다른 장비의 "평균 피험자"다(2.4절) |
| F7 | Ma & Kragel 2026의 TEM 환경은 13개 discrete 항목 상관 비유사도의 MDS를 11 x 11 격자로 이산화한 뒤 무작위 보행했다. Emo-FilM 평정자는 한 항목을 모든 영화에 대해 평정한 뒤 다음 항목으로 넘어갔다. Discussion은 RL 모형 검정을 future research로 적었다 | doi:10.1038/s41467-025-68240-z Methods, Discussion [본문, PMC12891686] | BI-P1의 "대칭 환경" 지적은 맞다. 항목마다 평정자 집합과 지연이 다르다는 multimodal-dynamics 지적도 원문과 맞는다 |
| F8 | Chang 2021의 자기보고(Study 4, MTurk 192명)와 얼굴 표정(Study 3, 20명)은 fMRI 참가자가 아닌 독립 표본이다 | doi:10.1126/sciadv.abf7129 Results, Methods [본문, PMC8064646] | 묶음 A의 "같은 사람의 본인 보고" 부분은 Chang 2021 대비 새롭다. 다만 다른 선행이 있다(2.3절) |

---

## 2. 묶음 A: Spacetop "개인 뇌 잔차 대 본인 보고 편차" (EF-P3, ET-P2, GI-P5, LS-P2)

### 2.1 통합 설계 요약
Spacetop alignvideo(48개 고유 영상, 같은 순서, 영상 뒤 7차원 본인 평정)에서 사람 i, 영상 v의 뇌 반응 y_iv(평정 전 TR 창)와 평정 x_iv를 두고, 기대 반응 b_v(TRIBE v2 예측, LOO peer 평균, SRM/hyperalignment 공유 성분, INT 개인화 예측)를 뺀 뇌 잔차 r_iv와, 기대 보고 c_v(LOO peer 평균, MLLM 평균 관찰자 추정)를 뺀 보고 편차 d_iv의 관계를 보류 영상에서 검정한다. EF-P3은 (b)-(a) 성분을, ET-P2는 privileged access 틀과 측정 모형을, GI-P5는 multiverse와 신뢰도 우선 규칙, rank 대역을, LS-P2는 MLLM 기대 보고와 역할 분담을 더했다.

### 2.2 구조 문제: 사람마다 같은 기준선은 사람 수준 질문에서 서로 구별되지 않는다
* **항등식[추론, 대수].** 기준선 b_v가 사람과 무관하면(TRIBE v2 집단 예측, MLLM 기대 보고, 전체 평균) r_iv = y_iv - b_v는 같은 영상 안에서 y_iv를 상수만큼 옮긴 것이다. LOO 평균도 r_iv = n/(n-1) x (y_iv - ȳ_v)라서 같은 영상 안에서는 y_iv의 아핀 변환이다. 보고 쪽 c_v도 같다. 따라서
  1. 같은 영상 안에서 사람 간 통계(상관, IS-RSA, 사람 순열 검정)는 사람 불변 기준선 전부에서 **값이 똑같다.**
  2. 영상 고정효과를 넣거나 사람과 영상 양방향으로 중심화하면 b_v, c_v는 모형에서 사라진다.
  3. 기준선 사이 차이는 **영상 사이 성분(48~49점)** 에서만 생긴다. 이 성분은 사람 수준 질문이 아니라 영상 수준 질문이다.
* **가짜 효과[시뮬레이션].** 사람 60명, 영상 48개, 사람 수준 연결 β = 0으로 두고, TRIBE와 MLLM이 같은 영상 수준 요인(예: 정서 강도)을 비슷하게 놓친다고 가정했다(오적합 계수 0.8, 잡음 0.3, 200회 반복, 시드 20261112).

  | 분석 | 평균 r (SD) |
  |---|---|
  | LOO/LOO, 풀링 | -0.002 (0.020) |
  | TRIBE(뇌)/MLLM(보고), 풀링 | **+0.356** (0.048) |
  | TRIBE/MLLM, 사람 안 영상 간 상관의 평균 | **+0.361** (0.049) |
  | TRIBE/MLLM, 영상 안 사람 간 상관의 평균 | -0.002 (0.020) |
  | TRIBE/MLLM, 양방향 중심화 | -0.002 (0.020) |

  LS-P2가 제안한 짝(신경 기대 = TRIBE, 보고 기대 = MLLM)과 GI-P5의 "기준선 5종" 교차 조합은 이 함정에 그대로 걸린다. MLLM이 평균을 평탄화한다는 근거(arXiv:2402.01908)와 TRIBE의 정서 조건별 실패 보고[search_index, encoding-foundation 기록]를 합치면 두 모델의 오적합이 같은 방향(강한 정서 영상의 과소 예측)일 가능성은 낮지 않다.
* **의미 있는 대비는 하나뿐이다.** 사람마다 다른 기준선(공유 반응을 각자의 지형으로 되돌린 W_i s_v, INT 개인화 예측)만 같은 영상 안의 잔차 순위를 바꾼다. 실질적 비교는 "사람 불변 기준선 대 사람 특이 기준선"이다. rank 대역 투영은 y_iv 자체를 거르는 연산이라 "편차의 어느 부분공간이 보고를 따르는가"라는 정당한 변형으로 남는다.
* **각 제안에 주는 함의.** GI-P5의 "기준선 간 차이 자체가 결과"는 사람 수준에서 성립하지 않는다. ET-P2의 "B1~B4를 모두 통제한 뒤의 본인 보고 고유 분산"은 B1~B4가 모두 영상 수준 변수라 결국 "영상 고정효과 뒤 영상 안 분산"과 같고, encoding-foundation이 제안한 B4 → B2 → B1 → B3 순서는 사람 수준 질문에 영향을 주지 않는다. LS-P2의 "MLLM 기준은 peer 평균의 순환 우려를 줄인다"는 전제도 맞지 않는다. LOO peer 평균은 순환이 아니며, 영상 안에서는 MLLM 기준과 결과가 같다.
* Round 3 검토자(systems-neuro, brain-inspired)는 기준선을 셋으로 줄이자고 했지만, 셋이 사람 수준에서 동치라는 점은 다루지 않았다.

### 2.3 P3 판정과 추가 점검

| 항목 | 판정 | 근거 |
|---|---|---|
| P3-1 이미 연구되었는가 | **partially** | (1) **Woo et al. 2017** (doi:10.1038/ncomms14211, PubMed 초록): 통증 평정 중 자극 강도와 NPS로 설명되지 않는 시행별 변동을 예측하는 뇌 signature(SIIPS1). "자극으로 기대되는 반응 너머의 주관 보고를 뇌가 담는가"라는 논리 구조가 같고, Spacetop을 만든 연구실의 선행이다. 네 제안 모두 인용하지 않았다. (2) **Li et al. 2025** (doi:10.1016/j.bandc.2024.106260, 초록): 짧은 영상 90개를 본 참가자 본인의 쾌감, 기대 평정과 ISC, 개인 특이 분석으로 공유 경험과 개인 선호의 신경 기반을 나눴다. (3) **Sachs et al. 2020** (doi:10.1016/j.neuroimage.2019.116512, 초록): 같은 참가자의 스캔 후 연속 평정이 동적 ISC를 예측. (4) Chen et al. 2020 (doi:10.1016/j.neuroimage.2020.116851, 초록): 선호 벡터의 IS-RSA. (5) Vallorani et al. 2026 (doi:10.1162/IMAG.a.1403, 초록): 클립마다 본인 정서 평정, 정서 유사성과 뇌 간 신경 유사성. (6) Chang 2021: 보고는 독립 표본(F8). **남는 새로움:** 100명 규모 x 48개 영상의 본인 사후 평정, 사람 불변 대 사람 특이 기준선의 명시적 대비, 정서 영역의 영상 고정효과 설계 |
| P3-2 단순 모델 적용인가 | 아니다. 그러나 현재 문안은 2.2절 때문에 같은 결과를 여러 번 계산하는 multiverse가 되어 방법 비교로 흐른다 | |
| P3-3 Neuroscience Question | 조건부 예. "같은 영상에서 내 신경 편차가 내 보고 편차와 공변하는가"는 Axis U와 A(Introspective Access)의 질문이다. 그러나 양성 결과는 "본인 보고의 사람 특이 성분이 같은 사람의 신경 편차와 공변한다"(R0)까지다. "privileged access"(ET-P2)는 내성으로만 접근 가능한 정보를 뜻하는데, 이 설계는 공통 원인(각성, 주의)을 배제하지 못하므로 그 이름을 쓰면 과잉 해석이다 | CLAUDE.md 6절, S3 |
| P3-4 정서 아닌 요소 | **위험 높음.** systems-neuro와 brain-inspired가 든 자율신경 반응성, 시선, 움직임, 척도 습관, 몰입에 더해: (a) **사람 특이 기능 지형과 정합 오차**는 영상 사이에 일정하므로 사람 중심화를 하지 않으면 사람 수준 척도 습관과 상관해 가짜 효과가 된다. (b) **모든 참가자 같은 순서**(F4)라 사람 x 시청 위치(피로, 졸음)의 상호작용이 전역 BOLD와 engaged, 시행 단위 결측에 동시에 작용할 수 있다. (c) 평정은 영상 끝 뒤 5 s x 7의 **회고 보고**라 마지막 장면의 기억 편향이 섞인다 | F3, F4 |
| P3-5 현재 데이터로 검증 가능한가 | 가능하나 유효 표본은 약 40~57명이다(F4). 결측은 값 의존이 아니라 시행/런 단위다(F3). 시행 단위 결측이 그 시행의 전역 신호, FD와 관련되는지는 뇌 자료로 확인해야 한다(미확인). 생리 미공개라 자율신경 경로를 직접 분리할 수 없다(사용자 결정 11번 보류) | |
| P3-6 더 강력한 방법 | (1) 양방향 중심화 위계 모형, 영상 안 사람 순열 null. (2) 영상별 IS-RSA(brain-inspired 제안과 같음). (3) 사람 특이 기준선은 alignvideo 밖 자료(다른 과제, 또는 보류 영상을 뺀 run)로 학습. (4) **교차 사람 null**: 같은 영상에서 i의 뇌 편차가 i의 보고 편차를 j의 보고 편차보다 더 잘 예측하는가(Binder et al. 2024 arXiv:2410.13787의 self vs cross prediction을 사람에게 옮긴 형태로, ET-P2의 틀을 실제 검정 가능한 형태로 만든다) | |
| P3-7 기대와 다를 때 | 신뢰도 관문과 검정력 시뮬레이션(V5)을 통과한 null만 정보가 있다. 양성은 engaged 특이성 대조와 전역 성분 강건성을 통과해야 해석한다 | |
| C 순환과 누수 | (1) SRM/hyperalignment를 시험 영상까지 포함한 alignvideo 전체로 학습하면 시험 영상 반응이 공유 성분에 새어 든다. 영상 단위 중첩 교차검증 안에서 학습하거나 다른 과제로 학습. (2) Spacetop 영상은 상업 영화, 다큐 발췌로 보인다(파일명 harrymetsally, freesolo 등, Stage 1). MLLM이 장면과 관객 반응을 이미 알 수 있다. (3) encoding-foundation은 TRIBE v2 사전학습 **데이터셋**에 Spacetop이 없음을 확인했지만, 사전학습 **자극**(유명 영화)과 Spacetop 영상의 겹침은 확인하지 않았다. 둘 다 provenance 등록부(V7)에 넣는다 | |
| D 과도한 인과 해석 | EF-P3 "자극으로 계산되지 않는 공유 정서 반응", ET-P2 "privileged access"는 R0 자료에 비해 강하다 | S3 |
| E 규모 | 계산량은 현실적(영상 86분, TRIBE 추론 1회). 통계 규모는 빠듯하다(유효 40~57명, 영상 48개) | F4 |
| F 통계 불확실성 | 관측 상관 ≈ 참 상관 x √(뇌 편차 신뢰도 x 보고 편차 신뢰도). 1회 시청이라 두 신뢰도 모두 재검사로 추정할 수 없다. 개인 대 나머지 상관 중앙값 0.46~0.77(Stage 1)은 개인 편차에 잡음이 많음을 뜻한다. 예: 두 신뢰도가 0.3이면 관측 상관은 참값의 0.3배. 7차원 x ROI x 대역 x 기준선의 다중비교. 주 결과를 사전에 좁혀야 한다(2.6절) | |
| G 인용 | 8절. arXiv:2607.01400(EF-P3, LS-P2)은 존재하지만 내용이 "TRIBE 예측 신호가 행동(재시청)을 예측하지 못함"이라 근거라기보다 경고다. arXiv:2402.01908(LS-P2)은 인구집단 정체성 평탄화 연구라 영상 정서 평정으로의 확장은 외삽이다 | |

### 2.4 각 제안의 고유 기여와 판정

| 제안 | 고유 기여 | 남는가 | 판정 |
|---|---|---|---|
| EF-P3 | (b) LOO peer 평균 - (a) TRIBE 예측을 "공유되지만 자극으로 계산되지 않는 성분"으로 해석 | **해석은 기각.** 같은 영상을 본 여러 사람이 공유하는 반응은 ISC 논리상 자극에 묶인 반응이다. 계산되지 않는 것은 "특정 모델로"일 뿐이다. 이 차이에는 TRIBE의 모델 오차, 장비 차이(Prisma MB8 TR 0.46 s), 피험자 평균 모델(F6), 모집단 차이, fsaverage5 대 fsLR 표면 차이가 섞인다. "평정 평균을 설명하면 공유 서사 평가의 증거"라는 판정도 48점 상관이고 영상 속성(대사, 얼굴, 음악)과 교락된다. **검정 가능한 형태:** 같은 TRIBE feature로 Spacetop 안에서 영상 단위 교차검증 선형 encoder를 학습해 간극이 닫히면 영역 이동, 닫히지 않고 LLM appraisal feature를 더해야 닫히면 "언어화 가능한 서사 평가"(llm-semantics 제안)로 해석 | **재구성.** 묶음 A에서 빼서 영상 수준 encoder 적합도 진단(GI-P4, EF-P1과 같은 계열)으로 옮긴다 |
| ET-P2 | 본인 보고 편차의 측정 모형(사람 x 차원 척도 사용 분리, 편차 신뢰도 보고), 반증 조건 기술 | 남는다. 통합 설계의 측정 핵심 | **수정.** privileged access 대신 "본인 보고의 사람 특이 신경 공변". B1~B4 순차 통제는 영상 고정효과로 대체. personal relevance 조절은 탐색적(encoding-foundation의 반대 의견에 동의) |
| GI-P5 | 사전등록 우산, 잔차 신뢰도 우선, rank 대역 | 신뢰도 관문과 부분공간 변형만 남는다 | **재구성.** multiverse 축을 "기준선 5종"에서 "사람 불변 대 사람 특이 기준선 x 부분공간"으로 바꾼다 |
| LS-P2 | 신경 잔차와 보고 잔차의 정렬, MLLM 평균 관찰자 기준, alt-test 선행 | 정렬 자체는 핵심 설계와 같다. MLLM 기준은 영상 수준 질문(사람들의 평균이 평균 관찰자 추론과 어디서 갈리는가)으로만 남는다 | **수정.** MLLM으로 결측 평정을 보간하는 안은 폐기한다. 사람 불변 값으로 채우면 그 칸의 편차가 0이 되어 편차를 0쪽으로 끌고 결측 구조와 엮인다 |

### 2.5 V1~V12 충족 여부 (현재 문안 → 2.6 개선안 적용 후)

| 요건 | 현재 | 개선 후 | 메모 |
|---|---|---|---|
| V1 경쟁 설명, matched null | △ | ○ | engaged를 비정서 대조 결과변수로, 교차 사람 null, 영상 안 사람 순열 |
| V2 상한과 신뢰도 | △ | △ | 1회 시청이라 상한 없음. 다지표 잠재 편차의 내적 일관성으로 하한만 |
| V3 chance 보정, 의존 구조 null | × | ○ | 영상 안 사람 순열(영상 구조 보존), 사람 블록 보존 |
| V4 신뢰도 민감도 | △ | ○ | 신뢰도 가정 sweep |
| V5 회복 검사 | × | ○ | 실제 결측 구조와 감쇠를 넣은 주입 시뮬레이션, 2.2절의 가짜 효과 재현을 음성 대조로 |
| V6 학습 무작위성 | △ | ○ | SRM 초기화, MLLM 프롬프트 변형 |
| V7 누수 경로, 등록부 | △ | ○ | 정렬 학습 중첩, TRIBE 사전학습 자극 겹침, MLLM 오염 |
| V8 일반화 수준 | △ | ○ | "같은 사람, 새 영상"과 사람 유병률을 분리 보고 |
| V9 라벨 출처, AI 라벨 | △ | ○ | MLLM은 영상 수준 분석에만, alt-test 후 |
| V10 사전 고정 | △ | ○ | 주 경로 하나(2.6) |
| V11 원 결과 재현 | NA | NA | 재분석 대상 원 결과 없음 |
| V12 반증 해석 | ○ | ○ | ET-P2 (d), 신뢰도 관문 null |
| S1~S3 | S3 위반 문구 2건 | S3 준수 | R0 |

### 2.6 개선안: 단일 연구 A*로 재구성
* **0단계(관문, 저비용).** (a) 시행 단위 결측이 그 시행의 FD, 전역 신호 진폭, 세션 내 위치와 관련되는지 확인. (b) 검정력 시뮬레이션: 유효 표본(완료율 0.5 이상 57명)과 실제 결측 패턴에 사람 수준 효과를 심고 회복률을 본다. (c) 보고 편차의 잠재변수: 긍정(happy, warm), 부정(sad, afraid, disgusted)으로 묶고 사람 x 차원 척도 사용을 위계 모형으로 분리. 부정 항목 바닥 효과(sad, afraid, disgusted 응답의 49~67%가 5 이하, F3)는 순서형 또는 0 과팽창 모형으로.
* **1단계(주 분석, 사전등록).** 뇌 특징: alignvideo 밖 자료로 학습한 정렬 공간의 ROI 패턴(vmPFC 주, insula 부, amygdala 탐색적). 결과: 잠재 긍정/부정 편차, 대조 결과 engaged. 모형: 사람과 영상 양방향 중심화 위계 모형, 공변량 FD, 전역 신호 진폭, 세션 내 위치. 추론: 영상 단위 보류 교차검증 + 사람 유병률(doi:10.7554/eLife.62461). null: 영상 안 사람 순열, 교차 사람 null.
* **2단계.** 사람 특이 기준선(SRM, INT) 대 사람 불변 기준선, rank 대역 부분공간. 전역 성분 제거 전후를 함께 보고하고, 제거로 사라지는 효과는 "신체 반응성 경로"로 분류(systems-neuro 해석 규칙에 동의).
* **별도 영상 수준 연구(48점).** EF-P3의 TRIBE 간극과 LS-P2의 MLLM 대 peer 간극. encoder/주석자 적합도 진단으로 명명하고 GI-P4, EF-P1과 함께 묶는다.
* **우선순위 의견.** 묶음 A는 Round 2 점수 1위지만, 유효 표본과 신뢰도 제약 때문에 과학적 우선순위는 GI-P1과 LS-P1보다 뒤라고 본다. 0단계 관문 결과를 보고 진행 여부를 정하자.

### 2.7 기존 Round 3 검토자가 놓친 점 (GI-P5 검토: systems-neuro, brain-inspired)
1. 사람 불변 기준선의 동치성과 TRIBE/MLLM 짝의 가짜 효과(2.2).
2. Woo 2017, Li 2025, Sachs 2020, Vallorani 2026 선행(2.3).
3. 정렬 학습의 시험 영상 누수, TRIBE 사전학습 자극 겹침 미점검(2.3 C).
4. EF-P3 (b)-(a) 해석 오류와 LS-P2의 MLLM 보간 편향(2.4).
5. 결측 구조의 실제 모양(F3). 두 검토자 모두 "클릭 저장 구조라 무작위 결측이 아닐 수 있다"는 일반론에 머물렀다. 계산해 보면 값 의존 결측의 증거는 없고 시행/런 단위 결측이 주다.
* 동의하는 점: 위계 모형, IS-RSA 병행, 비정서 공변량, 신뢰도 관문(두 검토자 공통).

---

## 3. 묶음 B: 정서 전이의 방향성 (GI-P2, BI-P1)

### 3.0 GI-P1과의 관계
GI-P2와 BI-P1은 서로 수용해 하나의 사전등록안(0단계 GI-P2 → 식별 가능성 시뮬레이션 → BI-P1 모형 비교 → γ 장축 위계)으로 합쳐졌다. **GI-P1은 이 묶음이 아니다.** 같은 에이전트(geometry-info)의 기하 도구를 쓰지만 질문(공유 대 개인 특이 분산, Horikawa 대 Westlin)과 데이터(Horikawa + Mind captioning)가 다르다. 연결점은 하나다. GI-P1이 정서 관련 공유 부분공간을 찾으면 그 부분공간을 방향성 분석의 신경 상태공간으로 쓸 수 있다. GI-P1은 4절에서 따로 판정한다.

### 3.1 수학 점검
1. **GI-P2의 A = (T - T')/2는 순 확률 흐름이 아니다[추론, 표준 Markov 연쇄 성질].** 행 정규화 전이 행렬 T에서 순 흐름은 J_ij = π_i T_ij - π_j T_ji, 즉 결합 행렬 P = D_π T의 반대칭 부분이다. detailed balance(J = 0)가 성립해도 π가 균등하지 않으면 T - T' ≠ 0이다. 따라서 |A|는 "자주 나오는 정서와 드문 정서"의 점유율 차이를 방향성으로 읽는다. 결합 전이 빈도 N_ij(i → j 횟수)의 반대칭 부분 N - N'을 쓰고, 엔트로피 생산도 결합 확률로 계산해야 한다(Lynn et al. 2021, doi:10.1073/pnas.2109889118의 틀). multimodal-dynamics는 BI-P1의 T' 문제를 짚었지만 GI-P2의 A는 그대로 "반대칭 흐름"으로 받아들였다.
2. **BI-P1의 SR(T) 대 SR(T')는 이중으로 약하다.** (a) 시간 역전 사슬은 T̃ = D_π⁻¹ T' D_π이다(multimodal-dynamics 지적에 동의). (b) 신경 RDM은 대칭이다. 상태 s의 표상을 M = (I - γT)⁻¹의 s행으로 두면 모형 유사도는 M M'이고, T'에서는 M' M이다. 둘은 고유값(M의 특이값 제곱)이 같고 특이벡터만 다르다. 차이는 M의 비정규성에서 오는데, 비정규성은 방향성뿐 아니라 비균등 π에서도 생긴다. 즉 RDM 비교는 방향을 2차 구조로만, 그것도 점유율과 섞인 채로 본다. T̃로 바꿔도 이 간접성은 남는다.
3. **추정 문제.** 1 Hz consensus는 자기상관이 강해 대부분의 전이가 자기 전이다. 비자기 전이가 적으면 엔트로피 생산 추정치는 위로 치우친다. 상태 수를 줄이고, 자기상관 길이 이상의 지연에서 전이를 세며, 시계열을 뒤집은 대리 자료에서 같은 추정량의 분포를 null로 둔다. 관측된 거친 상태의 엔트로피 생산은 하한이므로 0이 "가역"을 뜻하지 않는다.
4. **측정 출처.** 항목마다 다른 3~4명이 한 항목씩 모든 영화를 평정했다(F7). 항목별 반응 지연이 다르면 consensus에 가짜 순서가 생긴다(multimodal-dynamics). 전이는 어떤 한 사람의 경험된 전이도 아니다.

### 3.2 P3 판정과 추가 점검

| 항목 | 판정 | 근거 |
|---|---|---|
| P3-1 이미 연구 | **partially** | Ma & Kragel 2026(F7, 대칭 환경), Thornton et al. 2019(doi:10.1523/JNEUROSCI.1431-18.2018, 초록: 현재 상태 패턴이 가능성 높은 미래 상태를 닮으며 3차원 근접성이 상당 부분 설명), Thornton & Tamir 2017(doi:10.1073/pnas.1616056114, 초록: 행동 수준 전이 정확도), Ekman et al. 2023(doi:10.7554/eLife.78904, Crossref: successor 대 predecessor, frontier-ai가 찾음), Li et al. 2024(doi:10.1016/j.pneurobio.2024.102570, Crossref: 자발 뇌 상태의 SR, multimodal-dynamics가 찾음). **추가로 찾은 선행:** Kragel, Hariri, LaBar 2022(doi:10.1162/jocn_a_01787, PubMed 초록): 휴지기 fMRI에서 정서 뇌 상태를 분류한 뒤 이산 시간 Markov 과정으로 모형화, neutral hub, 정신병리에서 관성 증가. 정서 뇌 상태 전이 행렬 자체는 이미 추정된 적이 있다. 정서 consensus의 detailed balance 위반, 정서 SR의 방향성 검정은 검색 범위 안에서 미발견 |
| P3-2 단순 적용 | 아니다. 가설 판별 설계 | |
| P3-3 Neuroscience Q | 예. "해마-vmPFC 정서 지도는 유사도 지도인가 예측 지도인가"는 Ma & Kragel이 남긴 빈칸이다(Discussion, RL 모형) | F7 |
| P3-4 정서 아닌 요소 | 높음. 서사, 장면 전이의 방향성(frontier-ai, multimodal-dynamics 지적에 동의). 평정 지연 차이. HRF 비대칭 | |
| P3-5 데이터 | Emo-FilM 14편, 30명. 가능하나 GI-P2 0단계(평정만 쓰는 저비용 분석)에서 결합 흐름이 0과 구분되지 않으면 신경 단계로 가지 않는다 | |
| P3-6 더 강력한 방법 | (1) 시간 지연 전향 대 후향 예측(현재 상태 통제, ±k 대칭): multimodal-dynamics와 frontier-ai(Ekman식) 제안을 **주 검정**으로. (2) 내용 상태(비디오 latent, 캡션 embedding 군집)로 같은 수의 상태를 만든 경쟁 모형. (3) SR 모형 적합은 2차. (4) Kragel 2022식으로 신경 쪽 정서 상태 전이 행렬을 만들어 신경 자체의 결합 흐름도 본다 | |
| P3-7 기대와 다를 때 | 결합 흐름이 없으면 "영화 consensus로는 방향성 질문을 다룰 수 없다"는 측정 결론. 방향성이 내용 통제 뒤 사라지면 "정서 지도의 예측성은 서사 예측성"이라는 결론. 둘 다 의미 있다 | |
| C 순환과 누수 | leave-one-film-out 유지. γ를 평정 자기상관으로 추정하고 시간 척도도 평정에서 추정하면 일치가 자명하다는 brain-inspired의 지적(MD-P8 응답)이 여기에도 적용된다 | |
| D 인과 | "예측 지도"는 R0 관찰 상관. 해마가 예측을 "계산한다"는 표현은 쓰지 않는다 | S3 |
| E 규모 | 작다. 평정 9,600 s, 13개 항목. 계산 부담 낮음 | |
| F 통계 | 효과 크기 작음(Ma & Kragel r 약 0.04~0.10, 내 Round 1 기록), 영화 14개가 일반화 단위. 엔트로피 생산 추정 편향. 사전 검정력 시뮬레이션 필수 | |
| G 인용 | Ma & Kragel 환경 서술 [본문 확인], Kringelbach 2023 "영화 시청의 비가역성이 휴지기, 과제보다 낮다" [초록 확인], Lynn 2021 [초록 확인]. BI-P1의 "Thornton & Tamir 2017 전이 비대칭, Discussion 3째 단락"은 PMC 전문이 비어 있고 Europe PMC가 403이라 **확인하지 못했다** | 8절 |

### 3.3 판정
* **GI-P2: 수정.** 순 흐름과 엔트로피 생산을 결합 빈도로 다시 정의하고, 편향 보정 추정과 시간 역전 대리 null을 넣어 저비용 관문으로 유지한다.
* **BI-P1: 재구성.** 주 검정을 RDM 기반 SR(T) 대 SR(T')에서 시간 지연 전향/후향 예측 + 내용 상태 경쟁으로 바꾼다. SR(T) 대 SR(T̃) 적합은 2차. 식별 가능성 시뮬레이션에 평정 지연, HRF 지연 오추정, 비균등 점유율 시나리오를 넣는다. Ma & Kragel TEM 결과의 재현(V11)을 먼저 한다.

### 3.4 V1~V12 (현재 → 개선 후)

| V1 | V2 | V3 | V4 | V5 | V6 | V7 | V8 | V9 | V10 | V11 | V12 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| △ → ○ (T' null은 잘못, T̃와 내용 SR로) | △ → △ (Emo-FilM 반복 없음, ISC 상한만) | △ → ○ (시간 역전 대리, HRF 합성 null) | NA | △ → ○ (지연 시나리오 추가) | △ → ○ (상태 이산화 변형) | ○ (영화 단위 보류) | △ → ○ (영화 단위 일반화 명시) | △ (consensus, 항목별 평정자) | ○ | × → ○ (Ma & Kragel 재현) | ○ |

### 3.5 기존 Round 3 검토자가 놓친 점 (BI-P1 검토: multimodal-dynamics, frontier-ai)
1. GI-P2의 A가 π 가중 없는 반대칭 부분이라는 오류(multimodal-dynamics는 T'만 지적).
2. 대칭 RDM으로는 방향을 M M' 대 M' M으로만 본다는 구조적 약점.
3. Kragel 2022 JOCN 선행.
4. 엔트로피 생산 추정 편향과 시간 역전 대리 null.
5. V11(Ma & Kragel 재현) 부재.
* 동의: 내용 SR 경쟁, 평정 지연 정렬, 전향/후향 decoding(두 검토자 공통).

---

## 4. GI-P1: 두 코호트 교차 공유 스펙트럼

| 항목 | 판정 | 근거 |
|---|---|---|
| P3-1 이미 연구 | **partially** | 방법은 시각 영역 cross-decomposition(arXiv:2409.06843, 초록 확인: hyperalignment 후 대부분 공유되는 scale-free 스펙트럼), 영화 개인차(arXiv:2505.12653). 두 코호트 결합 자체는 EmoMind(arXiv:2605.16739, 초록: "two independent emotion fMRI datasets")가 했다. 내 검색(WebSearch, 2026-11-12)에서 이 자극의 공유/개인 특이 스펙트럼 재분석은 미발견 |
| P3-2 단순 적용 | 아니다. 코호트 내 쌍 대 코호트 간 쌍의 대비가 핵심 기여. 순서 독립이 확인되어(Spearman -0.03, vision-decoding [계산]) 이 논리가 성립한다 | |
| P3-3 Neuroscience Q | 예, 단 "범주 결론 판정"은 스펙트럼만으로 안 된다(vision-decoding 지적에 동의). 혼합 대 연속 잠재 모형의 held-out 우도 비교가 필요 | |
| P3-4 정서 아닌 요소 | 중간~높음. **두 코호트 모두 자유 시청(F1)** 이라 개인 특이 시선이 "재현 가능한 개인 고유 분산"을 만든다. 반대로 자극 구동 시선(saliency)은 모든 사람에게 공유되어 "공유" 분산으로 잡힌다. 시선 예측 band를 공유 쪽과 개인 쪽 모두에 넣어야 한다 | F1 |
| P3-5 데이터 | 가능. 72개 클립은 최대 11회 노출, MC 학습 순서 끝에 몰림(vision-decoding). Mind captioning 전처리본은 전역 신호 12개 회귀(systems-neuro), Horikawa 공개본은 미확인이라 raw에서 같은 파이프라인 재처리가 전제 | |
| P3-6 더 강력한 방법 | (1) 정렬 학습 자극과 스펙트럼 평가 자극을 분리(geometry-info도 ET-P1 응답에서 수용). (2) 혼합 대 연속 모형 비교. (3) 이월(t-1, t-2) 성분 명시 | |
| P3-7 기대와 다를 때 | 모두 해석 가능(코호트 간 공유 소실 = 프로토콜 특이, 개인 고유 재현 없음 = Westlin 개인 변동은 잡음 쪽) | |
| C 순환과 누수 | (1) 정렬과 평가 자극 분리. (2) 피험자 중복 미확인(저자 확인 필요). (3) 코호트 내 쌍은 순서뿐 아니라 장비, 전처리, 세션 구조를 함께 공유하므로 "코호트 내 - 코호트 간"을 순서 효과로만 읽지 않는다 | |
| D 인과 | "판정하기"라는 제목은 R0 기술 분석에 비해 강하다. "어느 해석과 맞는가"로 | |
| E 규모 | 두 코호트 raw 재전처리(5명 x 61 run, 6명 x 60+ run)는 크지만 현실적 | |
| F 통계 | **쌍 의존성.** 55쌍은 독립이 아니다(각 피험자가 10쌍에 들어감). 쌍 수준 검정은 과신이다. 피험자 단위 재표집 또는 피험자별 검정 + 유병률. 72개 클립 스펙트럼은 최대 71 rank | |
| G 인용 | arXiv:2409.06843, arXiv:2507.00320(초록: 원 대응 미관찰, 개인 간 변동), doi:10.7554/eLife.62461 모두 주장과 맞음 | 8절 |

* **기존 검토자(vision-decoding, multimodal-dynamics)가 놓친 점:** (1) V11 부재. 군집 multiverse 단계는 Horikawa 원 경로와 Westlin 원 경로로 원 수치를 먼저 회복해야 한다(내 Round 2 SN-P7 수정 1과 같은 요구). (2) Horikawa 2020 자유 시청(F1). vision-decoding은 미확인으로 두었다. (3) 쌍 의존성. (4) 자극 구동 시선이 공유 분산을 부풀리는 반대 방향 교란.
* **V1~V12:** V1 △(위상 무작위화, 자극 셔플 쌍 null 추가), V2 ○, V3 △(AMI는 있음, 쌍 의존 null 필요), V4 △, V5 ×(서로 다른 TR, 전처리에서 공유/개인 스펙트럼 회복 시뮬레이션 필요), V6 △, V7 △, V8 ○, V9 NA(스펙트럼은 라벨 비의존), V10 △, V11 ×, V12 ○.
* **판정: 수정, 우선순위 높음.** Horikawa 내부 단계(재현 + 스펙트럼)부터.

---

## 5. LS-P1: 정서 배제 캡션으로 설명하고 남는 정서 분산

| 항목 | 판정 | 근거 |
|---|---|---|
| P3-1 이미 연구 | **partially** | (1) Horikawa 2020 [본문, 초록]: 정서 범주 모형이 시각, 의미 공변량보다 transmodal 영역에서 우세. 의미 공변량은 사람 주석 의미 feature, 모형은 따로 적합. (2) **Abdel-Ghaffar et al. 2024** (doi:10.1038/s41467-024-49073-8, PubMed 초록): 정서 자연 이미지 1,620장에서 후두-측두 피질이 의미 범주와 정서 feature에 공동 tuning, 상위 성분이 animacy, arousal, 그 상호작용. 정서-의미 분리 질문의 직접 선행인데 LS-P1과 두 검토자 모두 인용하지 않았다(systems-neuro와 vision-decoding은 다른 맥락에서 인용). (3) Du 2025(arXiv:2509.24298, 초록: MLLM triplet embedding이 인간 평정보다 뇌를 잘 예측). (4) Doerig 2025(doi:10.1038/s42256-025-01072-0, Crossref 초록: 캡션 LLM embedding이 고차 시각 피질 반응을 특성화). 정서 배제 인간 캡션을 기준선으로 쓴 중첩 분할은 미발견 |
| P3-2 단순 적용 | 아니다. 측정 설계 | |
| P3-3 Neuroscience Q | 예. Horikawa 2020 결론의 가장 약한 고리(의미 공변량 측정 오차, 내 Round 1 U1)를 직접 다룬다 | |
| P3-4 정서 아닌 요소 | 양방향(과소 통제, 과통제), frontier-ai와 geometry-info 지적에 동의. 추가: 두 코호트 자유 시청(F1)이라 클립별 시선 분포 차이가 "정서 잔차"에 남는다 | |
| P3-5 데이터 | 가능. 보유본에 캡션 20개/클립이 있는지 미확인 | |
| P3-6 더 강력한 방법 | 검토자들의 제안(캡션 split-half 오차 보정, 교차 적합 잔차화, 다중 text encoder, 비디오 동역학 feature, controversial 쌍)에 동의. **추가:** banded ridge 분할은 band 차원에 민감하다. 34차원 평정 대 768~4,096차원 embedding이면 고차원 band가 분산을 더 흡수한다. 차원을 맞춘 판(PCA 동수)과 교차 적합 잔차화를 주 산출물로 | |
| P3-7 기대와 다를 때 | 의미 있음. 단 양성 대조(저수준 feature 고유 분산이 같은 절차로 검출되는가)를 사전에 | |
| C 순환과 누수 | (1) C&K 클립이 같은 원본 영상에서 잘렸는지 미확인(Stage 1). 지각 해시로 근접 중복을 묶어 같은 fold에. (2) 비디오/VLM feature 모델이 C&K 공개 interactive map(GIF와 범주 라벨)을 사전학습에서 봤을 가능성은 등록부에. (3) 회상 조건 cue 캡션(검토자 지적에 동의) | |
| D 인과 | "남는 분산 = 비언어적 정서"가 아니라 "언어 기술로 회복되지 않는 규범 정서 공변" | S3 |
| E 규모 | 현실적 | |
| F 통계 | 72개 클립 ceiling 대비 비율의 넓은 구간(frontier-ai). 영역별 다중비교, 클립 단위 bootstrap | |
| G 인용 | doi:10.1038/s42256-025-01072-0, arXiv:2509.24298, doi:10.1371/journal.pone.0152719 모두 존재하고 인용 취지와 맞음 | 8절 |

* **기존 검토자(frontier-ai, geometry-info)가 놓친 점:** Abdel-Ghaffar 2024 선행, band 차원 비대칭, 원 결과 재현(V11: Horikawa 2020의 정서 대 시각 객체 대 73차원 의미 모형 비교를 먼저 재현해 기준점으로), 원본 영상 단위 누수.
* **V1~V12:** V1 △(차원 맞춘 무작위 feature null 추가), V2 △, V3 △, V4 △ → ○(캡션 split-half), V5 ×(정서 고유 신호를 심은 회복 검사), V6 △, V7 △, V8 ○(두 코호트), V9 △(재작성 캡션은 AI 추정 표기됨), V10 ×, V11 ×, V12 ○.
* **판정: 수정, 우선순위 높음.** GI-P1과 전처리, 캡션 확보를 공유하므로 같은 첫 단계로 묶을 수 있다.

---

## 6. GC-P2: 기술 잔차(통계 통제)와 의미 고정 편집(설계 통제)의 맞대기

| 항목 | 판정 | 근거 |
|---|---|---|
| P3-1 이미 연구 | **partially, 제안자 인식보다 넓게** | **Zhan, Gu, Fang 2026 (arXiv:2610.13558, arxiv.org 초록):** TRIBE v2로 8개 정서의 편집 원본-목표 400쌍을 분석했고, 편집기 hidden state가 정서 관련 영역보다 시각 영역의 예측 반응과 더 대응한다고 보고했다. 이어 예측된 정서 영역 반응 변화를 편집 방향으로 쓰는 ROI-ReFT를 제안했다. GC-P2는 이 논문을 근거 ID로 들었지만 선행으로 다루지 않았고, emotion-theory 검토도 "시각 쪽으로 미끄러질 위험의 근거"로만 썼다. **R1 팔(편집 자극에 대한 encoder 예측 변화)은 부분적으로 이미 수행되었다.** 그 밖에 MINE(arXiv:2605.16468, 방법), Jang & Kragel 2025(doi:10.1523/JNEUROSCI.1436-24.2025, 편도체 encoder 합성), Mobbs 2006(doi:10.1093/scan/nsl014), Cao 2024(emotion-theory가 찾음). 같은 voxel에서 통계 잔차와 설계 편집을 맞대는 판정표는 미발견 |
| P3-2 단순 적용 | 아니다. 삼각 검증 | |
| P3-3 Neuroscience Q | 부분적. R1은 "이 데이터로 학습한 encoder가 정서 단서를 쓴다"까지 | |
| P3-4 정서 아닌 요소 | 높음. 편집은 저수준 통계(휘도, 색, 공간주파수)를 바꾼다(emotion-theory, systems-neuro). Zhan 2026의 결과가 그 위험의 직접 증거 | |
| P3-5 데이터 | R0, R1 가능. R2(새 평정)는 IRB, 평정자 예산, C&K 비디오 요청 양식의 파생물 공개 조건(미확인)에 달림. 편집 대상이 비디오라 시간 일관 편집이 필요하다(encoding-foundation 지적). arXiv:2608.06231(EmoWorld)은 비디오 **생성** 도구라 기존 클립 **편집**과 다르다 | |
| P3-6 더 강력한 방법 | 검토자 제안(자연 controversial selection 선행, 지각 대조 편집, 다중 encoder 합의)에 동의 | |
| P3-7 기대와 다를 때 | 판정표가 있음. "둘 다 음성" 칸과 "판정 불가" 칸 추가(두 검토자와 같음) | |
| C 순환과 누수 | **두 가지 순환이 빠져 있다.** (1) R0 잔차로 voxel을 고르는 데이터와 R1 encoder를 학습하는 데이터가 같다(Horikawa). 정서 관련 feature의 고유 가중치가 큰 voxel을 골랐으니 그 voxel에서 encoder가 정서 편집에 민감한 것은 부분적으로 구성상 보장된다. voxel 정의는 Mind captioning, encoder 학습은 Horikawa처럼 코호트를 나누거나 클립을 나눈다. (2) 편집을 encoder로 유도하거나 고르면(ROI-ReFT처럼) 같은 encoder로 평가하는 것은 순환이다. 편집기는 평가 encoder와 독립이어야 하고, 평가는 encoder 여럿(Horikawa 학습, TRIBE v2, NSD 학습)으로 | |
| D 인과 | R0 + R1 + R2. 실제 뇌의 정서 특이 반응 주장은 R3 필요(내 Round 2 GC-P3 응답과 같은 입장) | S1, S3 |
| E 규모 | 중간~높음(비디오 편집 + 새 평정) | |
| F 통계 | voxel 수준 맞대기의 검정력 낮음(systems-neuro), alt-test 최소 조건(평정자 3명 이상, 사례 30개 이상) | |
| G 인용 | arXiv:2610.13558은 존재하고 인용 취지와 맞지만 선행으로 다뤄야 한다. doi:10.1093/scan/nsl014 맞음. arXiv:2608.06231은 생성 도구 | 8절 |

* **기존 검토자(systems-neuro, emotion-theory)가 놓친 점:** Zhan 2026을 선행으로 다루지 않은 점, voxel 선택과 encoder 학습의 순환, encoder 유도 편집의 순환.
* **V1~V12:** V1 △(null-edit, 지각 대조), V2 △, V3 ×, V4 △, V5 △(2 x 2 편집 정답 심기, GC-P1에서 수용됨), V6 △, V7 × → ○(코호트 분리, 독립 편집기), V8 △, V9 △(R2 alt-test 계획), V10 ○, V11 NA, V12 △(둘 다 음성 칸 없음).
* **판정: 수정.** LS-P1 결과가 나온 뒤의 2단계로 둔다.

---

## 7. BI-P2: Axis V 경쟁 검정

| 항목 | 판정 | 근거 |
|---|---|---|
| P3-1 이미 연구 | **partially** | Thornton & Tamir 2024 (doi:10.1038/s41467-024-44870-7, PubMed 초록: 상황과 정신상태의 신경 패턴이 그것이 허용하는 행동 패턴의 가중합으로 재구성, frontier-ai가 찾음), Mohammadi 2023, Leitão 2020, Morgenroth 2026(doi:10.1037/emo0001619, 초록: 13개 discrete 모두 성분으로 신뢰성 있게 예측). 자연 영화에서 범주 band와 행동 경향 band, 자극 계산 affordance의 직접 경쟁은 내 검색(WebSearch 2026-11-12)에서도 미발견 |
| P3-2 단순 적용 | latent action band는 단순 적용에 가깝다. LAPA 원문은 latent action이 카메라 움직임을 잡는다고 적고 조작 영상 밖 적용은 탐색하지 않았다고 한계에 적었다(arXiv:2410.11758, HTML 본문 Limitations와 Appendix E 확인) | |
| P3-3 Neuroscience Q | 질문은 정서 이론(action readiness 대 범주 느낌)에 직결된다. 그러나 **동기의 출발점이 오독이다.** BI-P2는 이 검정이 Horikawa 2020의 "(or affordances)" 해석을 시험한다고 했지만, 원문의 affordance는 "장면이 특정 정서를 일으킬 것이라는 시각적 추론"(정서 affordance)이다(F2). 이는 Axis U(지각된 정서 특성 대 느낀 정서)의 질문이지 Axis V가 아니다. 두 Round 3 검토자도 이 문장을 그대로 반복했다 | F2 |
| P3-4 정서 아닌 요소 | 높음. Motivation 항목이 화면 속 행위를 재표현, latent action은 카메라 운동(검토자들과 같음) | |
| P3-5 데이터 | Emo-FilM은 가능. Horikawa 확장은 행동 경향 인간 라벨이 없어 AI 추정(alt-test 선행) | |
| P3-6 더 강력한 방법 | 검토자 제안(0단계 판정 규칙, 판별 구간 RSA, TRIBE 기준선 nuisance, 자세 기반 행동 feature, counterfactual 3단계)에 동의 | |
| P3-7 기대와 다를 때 | 공선성이 크면 "분리 불가"가 가장 가능성 높은 결과. 사전 정의 필요(검토자 공통) | |
| C 순환과 누수 | leave-one-film-out. 0단계 공선성 계산과 2단계 분할이 같은 평정을 쓰므로, 0단계 판정 기준(예: 교차 예측 R²가 신뢰도 상한의 90% 초과 시 중단)을 결과 열람 전에 고정 | V10 |
| D 인과 | "범주 고유 분산이 행동 경향으로 대체된다"는 "예측 분산이 겹친다"로(generative-counterfactual 지적에 동의) | S3 |
| E 규모 | Emo-FilM 단계는 현실적 | |
| F 통계 | 항목별 신뢰도 0.21~0.60의 비대칭이 분할을 왜곡. 감쇠 보정 필수 | |
| G 인용 | Horikawa 2020 근거 오독(내용과 위치 모두). LAPA 카메라 주장, Morgenroth 2026, Bartnik 2025(doi:10.1073/pnas.2414005122, Crossref 초록: 보행 affordance가 물체, 재질, 장면 범주와 독립적으로 표상) 맞음 | 8절 |

* **기존 검토자(generative-counterfactual, encoding-foundation)가 놓친 점:** Horikawa affordance 근거 오독. 또한 BI-P2는 Round 3 배정 덕분에 상위 10개에 들었다(9절).
* **V1~V12:** V1 △, V2 △ → ○(감쇠 보정), V3 △, V4 △, V5 ×, V6 △, V7 △, V8 △, V9 ×(Horikawa 확장의 AI 행동 라벨), V10 △ → ○(0단계 규칙 고정), V11 NA, V12 △ → ○.
* **판정: 수정.** 동기를 Frijda/CPM과 Thornton & Tamir 2024로 다시 세우고, Horikawa 2020의 정서 affordance 해석은 Axis U 쪽 질문(LS-P1, ET-P3 계열)으로 넘긴다.

---

## 8. 인용 표본 점검 (제안당 2~3개)

| 제안 | ID | 존재 확인 경로 | 주장된 내용과 일치하는가 |
|---|---|---|---|
| EF-P3 | doi:10.7554/eLife.56601 | Crossref | ○ Haxby 2020 hyperalignment 개관, (c) 기준선 근거로 맞음 |
| EF-P3 | arXiv:2607.01400 | arxiv.org abs | △ 존재. 내용은 "TRIBE 예측 전역 신호가 YouTube 재시청 히트맵을 예측하지 못함", 공개 모델은 피험자 평균. 근거라기보다 TRIBE 기반 행동 예측에 대한 경고 |
| EF-P3, LS-P2 | arXiv:2408.13718 | arxiv.org abs | ○ GPT-4가 3인칭 평균 관찰자 관점에 가깝다 |
| ET-P2 | doi:10.3758/s13428-017-0935-1 | Crossref | ○ reliability paradox |
| ET-P2 | arXiv:2410.13787 | arxiv.org abs | ○ self-prediction이 cross-prediction보다 나은가로 내성 정의. 사람으로 옮기는 것은 유추 |
| ET-P2 | doi:10.1177/0956797620916786 | Crossref | ○ 과제 fMRI 측정치의 낮은 재검사 신뢰도 |
| GI-P5 | doi:10.1162/imag_a_00032 | Crossref | ○ INT 모형 |
| GI-P5 | doi:10.1038/s41586-022-04492-9 | Crossref | ○ BWAS에는 수천 명 필요 |
| LS-P2 | arXiv:2402.01908 | arxiv.org abs | △ LLM이 정체성 집단을 평탄화. 영상 정서 평정으로의 확장은 외삽 |
| LS-P1 | doi:10.1038/s42256-025-01072-0 | Crossref 초록 | ○ 캡션 LLM embedding이 고차 시각 피질 반응을 특성화 |
| LS-P1 | arXiv:2509.24298 | arxiv.org abs | ○ 2,180개 비디오의 MLLM triplet embedding이 인간 평정보다 뇌 예측이 높음 |
| LS-P1 | doi:10.1371/journal.pone.0152719 | Crossref | ○ 제목 일치(Statistically Controlling for Confounding Constructs Is Harder than You Think). 내용은 내 Round 1 기록 |
| GC-P2 | doi:10.1093/scan/nsl014 | Crossref | ○ Kuleshov 효과 |
| GC-P2 | arXiv:2610.13558 | arxiv.org abs | △ 존재, 인용 취지와 맞음. 그러나 R1 팔의 부분 선행이라 선행으로 다뤄야 함 |
| GC-P2 | arXiv:2608.06231 | arxiv.org abs | △ 비디오 생성(대기감, 의미 단서, 시간 분리). 기존 클립 편집 도구는 아님 |
| GI-P1 | arXiv:2409.06843 | arxiv.org abs | ○ |
| GI-P1 | arXiv:2507.00320 | arxiv.org abs | ○ 원 대응 미관찰, 개인 간 변동 |
| GI-P1 | doi:10.7554/eLife.62461 | Crossref 초록 | ○ Bayesian prevalence |
| GI-P2 | doi:10.1073/pnas.2109889118 | Crossref 초록 | ○ 뇌가 거시 규모에서 detailed balance를 깨며 부하와 함께 증가 |
| GI-P2 | doi:10.1126/sciadv.ade6049 | PubMed 초록 | ○ 영화 시청의 비가역성이 휴지기, 과제보다 낮음 |
| BI-P1 | doi:10.1038/s41467-025-68240-z | PubMed 전문 | ○ TEM 환경이 MDS 격자 위 무작위 보행(Methods) |
| BI-P1 | doi:10.1073/pnas.1616056114 | PubMed 초록 | △ 존재, 행동 전이 정확도 연구. "전이 비대칭, Discussion 3째 단락"은 본문 미열람으로 **미확인** |
| BI-P2 | doi:10.1016/j.isci.2020.101060 | PubMed 전문 | **× 오독.** "(or affordances)"는 정서 affordance이고 위치도 Discussion이 아니라 서론 마지막 단락(F2) |
| BI-P2 | arXiv:2410.11758 | arxiv.org abs, HTML 본문 | ○ latent action이 카메라 움직임을 포착, 조작 영상 밖 미탐색(Limitations) |
| BI-P2 | doi:10.1037/emo0001619 | PubMed 초록 | ○ 13개 discrete 모두 성분으로 예측 |

요약: 25개 중 식별자 오류 0, 내용 오독 1(BI-P2), 미확인 1(BI-P1의 Thornton & Tamir 2017 위치 주장), 근거로서 약하거나 외삽 3(arXiv:2607.01400, arXiv:2402.01908, arXiv:2608.06231), 선행으로 다뤄야 할 근거 1(arXiv:2610.13558).

---

## 9. 합의 쏠림 점검

### 9.1 관찰된 사실
* Round 2: 응답 96건(수용 51, 수정 45, 반박 0). 1차 수신자 응답만 보면 76건(수용 34, 수정 42)[계산, responses_tally.csv].
* Round 3: 검토 30건에서 "기각", "반박"이라는 판정은 한 번도 쓰이지 않았다(모든 round3_reviews.md 검색). 모두 "수정 후 진행/유지/채택".
* "수정" 응답 안에는 핵심 전제에 대한 실제 반대가 섞여 있다. 각 round2.md 응답 절에서 "반대", "부분 반박", "성립하지 않" 같은 표현이 약 15곳 나온다(예: encoding-foundation의 ET-P2 (c) HOTEC 해석 "반대한다", geometry-info의 MD-P1 단일 τ "잘못 지정", frontier-ai의 GC-P6 "반박을 포함한 수정"). 즉 반박 0은 일부는 분류 관행 때문이다.

### 9.2 질 때문인가, 동의 편향 때문인가
**동의 편향과 양식 효과 쪽 근거가 더 강하다.**
1. **검증 가능한 오류가 수용을 통과했다.** EF-P3의 (b)-(a) 해석(emotion-theory 수용, "내 설계에 없던 새 분해"), GI-P2의 A = 순 흐름(brain-inspired 수용), BI-P1의 T' 대조(geometry-info 수용, **adversarial-reviewer Round 2도 "깨끗한 matched null"로 수용**), BI-P2의 Horikawa affordance 근거(frontier-ai 수용, Round 3 검토자 2명 반복). 이것들은 취향 문제가 아니라 원문 대조나 대수로 확인되는 오류다.
2. **양식 효과.** P2 양식은 "너희 쪽 X를 우리 쪽 Y로 검증하거나 확장"이다. 거의 모든 제안이 받는 쪽의 chain을 품고 있어, 받는 쪽은 자기 아이디어가 들어간 병합안을 평가했다. 묶음 A의 네 제안은 같은 5~6개 에이전트의 chain을 서로 다른 이름으로 다시 묶은 것이다.
3. **선정 점수의 구조.** 점수 = 수용 + 0.5 x 수정 + 0.5 x 언급 파일 수인데, `tally_responses.py`는 언급을 round2.md와 **round3_reviews.md** 에서 센다. Round 3 배정 제안은 검토 파일 2개에서 언급되어 언급 파일이 평균 2.2개 늘었고(미배정 0.15개), 점수가 평균 약 1.1점 올랐다(미배정은 약 0.07점)[계산]. 상위 10개 중 6개가 Round 3 배정 제안이다. Round 2 파일만 세면 상위 10개는 EF-P3, ET-P2, LS-P2, GI-P5, BI-P1, ET-P4, GI-P1, GI-P2, LS-P1, EF-P4(10위 동점 EF-P4, ET-P1, GC-P2 중 ID 순)이고 **BI-P2(2.5점)와 GC-P2(3.0점, 10위 동점 중 ID 순 밖)는 빠진다.** 지시문 기준("Round 2에서 가장 많이 수용되거나 언급된")과도 어긋난다. 또 병합안은 병합된 모든 에이전트가 언급하므로 같은 설계의 변형 네 개가 1, 2, 3, 7위를 차지했다. 점수는 질이 아니라 병합 범위를 잰다.
4. **반대 근거(질 쪽).** 많은 "수정"이 실질적이었다(vision-decoding의 events.tsv 확인, encoding-foundation의 TRIBE 입력 구조, multimodal-dynamics의 T̃ 정정). Round 1 chain은 이미 문헌 검증을 거쳤고, 제안 다수가 그것들의 병합이라 수렴 자체는 자연스럽다. 그러나 이것은 "반박할 필요가 없었다"가 아니라 "반박 대신 수정으로 처리했다"를 보여 준다.

### 9.3 반박되어야 했던 제안 (상위 10개 밖 포함)
| 제안 | 반박되어야 했던 부분 | 이유 |
|---|---|---|
| EF-P3 | (b)-(a) = 자극으로 계산되지 않는 공유 성분 | 2.4절 |
| GI-P5 | 사람 수준 기준선 multiverse | 2.2절 |
| GI-P2 | A = 순 확률 흐름 | 3.1절 |
| BI-P1 | SR(T')를 방향성 null로 | 3.1절 |
| BI-P2 | Horikawa 2020 affordance 근거 | F2 |
| **GI-P6** (상위 10개 밖) | "일본어 화자 뇌 공간에서 일본어 범주 체계가 영어 체계보다 IB 효율적인가"의 언어 특이 해석 | 영어 화자 뇌 코호트가 없다(Horikawa 2020 참가자 언어 미확인, 같은 교토 연구실 획득). 한 뇌 공간에서 두 명명 체계를 비교하면, 일본어 체계의 우위가 "언어 일치" 때문인지 명명 수집 절차, 범주 수, 평정자 집단 차이 때문인지 구분되지 않는다. llm-semantics는 "수정 후 수용"으로 명명 출처만 바꿨다. 언어 특이 가설은 기각하고, 언어 무관한 IB 효율과 볼록성 질문만 탐색적으로 남기는 것이 맞다고 본다 |
| ET-P2 (c) | personal relevance를 HOTEC self 성분의 대리로 | encoding-foundation이 사실상 반박함(몰입, 주의와 구분 불가). "수정"이 아니라 "부분 반박"으로 기록해야 한다 |
| MD-P1 | 단일 τ 이완 모형 | geometry-info가 모형 오지정을 지적함. 사실상 핵심 모형 반박 |

### 9.4 권고
* 응답 범주에 "부분 반박(핵심 전제 거부)"을 추가하고, 이미 기록된 "수정" 중 핵심 전제를 거부한 것을 재분류한다.
* Round 4와 Stage 4에서는 수용하는 제안마다 "핵심 전제 한 줄을 반증 시도했는가"를 적게 한다.
* 상위 N개 선정 점수는 Round 2 파일만 세고, 같은 설계의 변형은 묶어 한 번만 센다.

---

## 10. 자기 정정: V1의 SR(T') 문구
내 Round 2 요건표 V1은 "방향성 주장은 전치 모델(예: SR(T'))처럼 대칭 성분이 같은 null 포함"이라고 적었고, 1.6절에서 BI-P1을 "깨끗한 matched null"로 수용했다. 3.1절에 따라 이것은 틀렸다. V1의 해당 문구를 다음으로 바꾸기를 Coordinator에게 제안한다(이번 지시상 round2.md는 고치지 않았다).
* **V1 (v3 제안):** 방향성 주장은 (a) 결합 전이 빈도의 반대칭 부분(π 가중 순 흐름)과 시간 역전 대리 null, (b) 시간 역전 사슬 T̃ = D_π⁻¹ T' D_π 기반 대조, (c) 같은 상태 수의 내용 상태 경쟁 모형을 포함한다.
* **V3 보강 제안:** 사람 수준 주장(개인 편차, 개인 특이성)은 사람과 자극 양방향 중심화 또는 자극 고정효과를 주 분석으로 하고, 자극 수준 기준선 선택이 결과를 바꾸지 않음을 보인다(2.2절의 동치성 점검).

---

## 11. 우선순위 의견 (Coordinator 참고, 구속력 없음)
1. **GI-P1 Horikawa 내부 단계 + LS-P1**: 같은 전처리와 캡션 확보를 공유하고, 원 결과 재현(V11)을 기준점으로 삼을 수 있다.
2. **GI-P2 0단계와 BI-P2 0단계**: 둘 다 평정만 쓰는 저비용 관문(consensus 순 흐름, discrete와 Motivation의 교차 예측). 결과로 BI-P1과 BI-P2 본 분석 진행 여부를 정한다.
3. **묶음 A***: 0단계(결측-상태 관계, 검정력 시뮬레이션) 통과 후.
4. **GC-P2**: LS-P1 결과 뒤.

---

## 12. 검색과 계산 기록 (모두 2026-11-12)

| 대상 | 경로와 질의 | 결과 |
|---|---|---|
| 묶음 A | PubMed `(idiosyncratic OR "individual differences" OR "intersubject representational similarity") AND (emotion* OR affective) AND (movie OR film OR naturalistic OR music) AND fMRI AND (self-report* OR rating*)`, 2015~ | 16건. Li 2025(Brain Cogn), Vallorani 2026, Chang 2021 확인 |
| 묶음 A | PubMed 제목 검색(Chen 2020 IS-RSA, Woo 2017 SIIPS1, Sachs 2020) | 3건 메타데이터 확인 |
| 묶음 A | WebSearch "Spacetop alignvideo fMRI individual ratings idiosyncratic neural response predicts own emotion rating deviation from group" | 같은 분석 미발견 |
| 묶음 A | PubMed 전문 PMC8064646(Chang 2021), PMC12373947(Spacetop) | F5, F8 |
| 묶음 A | Spacetop events.tsv 1,369개 계산(이 세션 scratchpad에 이미 있던 OpenNeuro ds005256 git 미러, CC0). 스크립트 `/tmp/claude-0/-home-user-emotion-explore/4a0aeef6-c090-5f71-8a99-9b8e7c0f6d89/scratchpad/ar_scripts/spacetop_missing.py` | F3, F4 |
| 묶음 A | 기준선 동치성 시뮬레이션 `/tmp/claude-0/-home-user-emotion-explore/4a0aeef6-c090-5f71-8a99-9b8e7c0f6d89/scratchpad/ar_scripts/baseline_sim.py` (시드 20261112, 200회) | 2.2절 표 |
| 묶음 B | WebSearch "successor representation emotion transitions fMRI hippocampus vmPFC asymmetric 2026" | Ma & Kragel만 |
| 묶음 B | PubMed `("entropy production" OR "detailed balance" OR "temporal irreversibility" OR ...)[tiab] AND (emotion* OR mood OR affective OR movie* OR film*)[tiab]` | 정서 적용 없음(물리, 박막 연구) |
| 묶음 B | WebSearch "time irreversibility emotion dynamics fMRI OR experience sampling detailed balance affect transitions asymmetry" | Kragel 2022 JOCN(Markov 정서 뇌 상태), detailed balance 검정 없음 |
| 묶음 B | WebSearch "forward versus backward decoding predictive representation upcoming emotion naturalistic movie fMRI" | 미발견 |
| 묶음 B | PubMed 전문 PMC12891686(Ma & Kragel). PMC5468631(Thornton & Tamir 2017), PMC6325264(Thornton 2019)는 전문이 빈 문자열. Europe PMC REST는 프록시 403(우회하지 않음) | F7, BI-P1 인용 미확인 |
| LS-P1 | PubMed `(affective OR emotion*) AND (semantic OR caption* OR "language model") AND (variance partitioning OR "unique variance" OR encoding) AND (natural images OR videos OR movies) AND fMRI AND (occipital OR visual cortex OR temporal)`, 2019~; WebSearch Abdel-Ghaffar 2024 | Abdel-Ghaffar 2024 |
| GI-P1 | WebSearch "Cowen Keltner 2185 videos fMRI reanalysis shared idiosyncratic emotion representation across individuals hyperalignment 2025 2026" | 재분석 미발견 |
| GC-P2 | WebSearch "emotion editing images semantic content preserved fMRI encoding model amygdala in silico counterfactual 2025 2026"; arxiv.org abs arXiv:2610.13558 | MINE, Jang & Kragel; Zhan 2026이 부분 선행 |
| BI-P2 | WebSearch "action tendency versus emotion category neural representation naturalistic film fMRI encoding approach avoidance motivation component 2025 2026"; PubMed 전문 PMC7191651(Horikawa 2020); arxiv.org HTML arXiv:2410.11758 | 직접 경쟁 미발견, F2, LAPA 카메라 주장 확인 |
| 인용 점검 | arxiv.org abs 13건, api.crossref.org 19건, PubMed 메타데이터 | 8절 |

**이번에 새로 확인한 문헌(literature.jsonl 미추가):** doi:10.1038/ncomms14211 (Woo 2017), doi:10.1016/j.bandc.2024.106260 (Li 2025), doi:10.1162/IMAG.a.1403 (Vallorani 2026), doi:10.1162/jocn_a_01787 (Kragel 2022), doi:10.1038/s41467-024-49073-8 (Abdel-Ghaffar 2024, 다른 에이전트 jsonl에는 있음), arXiv:2607.01400, arXiv:2610.13558, arXiv:2608.06231, arXiv:2402.01908 (모두 존재 확인, 초록 수준). discussion_read: Ma & Kragel 2026, Horikawa 2020, Chang 2021, Spacetop 2025는 full_text, 나머지는 abstract_only.

---

## 13. 미확인 사항
* Thornton & Tamir 2017의 "전이 비대칭" 서술 위치(본문 미열람).
* Li 2025, Vallorani 2026, Abdel-Ghaffar 2024의 본문(분산 분할 여부 등). 초록만 읽었다.
* Spacetop 시행 단위 결측과 그 시행의 FD, 전역 신호의 관계(뇌 자료 필요).
* TRIBE v2 사전학습 자극 목록과 Spacetop 영상 출처의 겹침.
* Horikawa 2020 참가자의 모국어, 두 코호트 피험자 중복.
* Mind captioning 보유본의 캡션 파일 포함 여부, C&K 클립의 원본 영상 단위 중복.
* 사용자 보유 Spacetop 사본이 이번에 계산한 공개 미러와 같은 판본인지.
