# Round 2 (Cross-Agent Exchange): emotion-theory

* 에이전트: emotion-theory (Axis A, Q 담당, 외부 분야 Artificial Consciousness and Metacognition). 제안 ID 접두어 ET
* 기준일: 2026-11-12. 절차: `reference/protocols.md` P2
* 읽은 것: 다른 10개 에이전트의 `round1.md` 전부(0, 1, 3, 4, 6절은 전체, 나머지는 필요한 부분), `outputs/axis_encyclopedia.md` 0절과 2절, `outputs/STAGE_STATUS.md` 사용자 결정 기록, `outputs/literature/literature_db.csv`(인용 ID 대조), Stage 1 데이터셋 보고서의 Emo-FilM 항목표와 Spacetop 평정 구조
* 전제 변경 반영: 사용 가능 데이터셋 5개(Horikawa 2020, Emo-FilM, Spacetop, NSD, **Mind captioning**(Horikawa 2025, doi:10.1126/sciadv.adw1464, 같은 Cowen & Keltner 비디오, 6명, 72클립 5회 반복, 회상 imagery와 시행별 vividness, 정서 배제 인간 캡션. 저장소 실제 파일 세부는 미확인)). Axis U, V, W 독립, Y(Introspective Access)는 A의 Sub-axis, X는 R의 Sub-axis
* 인용 규칙: 근거 ID는 `literature_db.csv`의 verified 문헌이거나 이번에 식별자 경로로 새로 확인한 문헌이다. 새로 확인한 5편(10.1093/scan/nsw121, 10.1093/scan/nsae043, 10.1016/j.bpsc.2025.11.011, 10.1038/s41467-020-15763-2, 10.1162/jocn_a_00839)은 `literature.jsonl`에 추가했다(Crossref + PubMed 초록)
* 표기: 각 제안에 label-provenance(대상: portrayed / perceived / felt, 주체: 본인 / peer 합의 / 별도 평정자 규범 / AI 추정)와 evidence-level(R0 상관, R1 모델 내 개입, R2 새 행동 평정, R3 새 fMRI 자극 조작, R4 뇌 개입)을 단다. 새로움 주장에는 검색 경로와 날짜를 단다

---

## 0. 읽고 나서 본 것: 에이전트 간 수렴 지도

여러 에이전트가 독립적으로 거의 같은 설계에 도달한 지점이 다섯 군데 있다. 중복을 줄이고 각 에이전트의 고유 기여를 살리려면 Stage 3 조합 전에 묶는 것이 좋다고 본다. 아래 제안 ET-P1, P2, P4는 이 묶음을 위한 것이다.

| 수렴 지점 | 같은 설계를 낸 에이전트와 chain | 각자의 고유 기여 (내 판단) |
|---|---|---|
| Spacetop에서 "자극 기대 반응에서 벗어난 개인 뇌 반응이 본인 보고의 편차를 예측하는가" | encoding-foundation Chain 3, generative-counterfactual CH5, vision-decoding R5, llm-semantics Chain 5, geometry-info C3/C8, emotion-theory C4 | EF: TRIBE v2 규범 뇌 기준선. GC: 인과 수준(R0) 명시와 교란 목록. VD: 공유 latent와 개인 잔차. LS: LLM 관찰자 라벨(L2) 기준선. GI: 개인 기하 형질. ET: privileged access 틀, 편차 신뢰도 측정 모형, self 관련성 조절 |
| Horikawa 2020 범주 결론과 Westlin 2025 재현 실패의 분해 | systems-neuro Chain 2, adversarial-reviewer D1, geometry-info C1, emotion-theory C2 | SN: network subspace와 전역/자율신경 성분. AR: multiverse 격자와 NMI 보정 문제. GI: rank 대역. ET: 평정 독립 신뢰 부분공간과 개인 군집의 session 분할 재현성 |
| 정서 반응의 rank별 공유 스펙트럼 | geometry-info C1, emotion-theory C1 | 거의 같은 설계. GI: 대역별 내용 분할, IB 연결(C7). ET: 반복 상한 보정, 비선형 대안, Cowen & Keltner 방향 2와의 연결 |
| Emo-FilM에서 생리, 평정 성분, 자극 feature로 정서 관련 영역 분산을 분할 | encoding-foundation Chain 2, systems-neuro Chain 1, adversarial-reviewer D5, emotion-theory C3 | EF: limbic 맹점과 foundation encoder. SN: 자율신경-혈관 전역 성분. AR: 생리가 상한을 부풀리는 정도. ET: Feeling 대 Appraisal 분포를 HOT 판별 검정으로 |
| 평정 불확실성(엔트로피)과 뇌 | llm-semantics U2(LLM hyperconservatism), adversarial-reviewer D4(alt-test, PPI), emotion-theory C5 | LS: 인간, LLM, 뇌 세 엔트로피 비교. AR: AI 라벨 하류 추론 보정. ET: 불일치를 자극 모호성, 개인 특이 반응, 측정 잡음으로 분해 |

---

## 1. 가져온 아이디어

### I-1. Mind captioning의 반복 제시와 회상 vividness를 Axis Q와 Y의 측정 자원으로 (출처: vision-decoding, doi:10.1126/sciadv.adw1464)
vision-decoding이 확인한 Mind captioning 코호트는 Horikawa와 같은 비디오에 72클립 5회 반복을 갖는다(vision-decoding round1 0.1절, 논문 본문 기준). 내 Round 1 C1의 가장 큰 약점은 Horikawa에 반복이 없어 피험자 간 공유 상한만 쓸 수 있다는 점이었다. 같은 자극에서 반복 기반 상한과 피험자 간 상한을 함께 계산하면 Horikawa 2,181개에 쓸 상한의 보정 관계를 얻을 수 있다(ET-P1). 또 회상 직후 시행별 vividness는 **fMRI 참가자 본인의 주관 보고**다. Horikawa 자극 계열에서 참가자 본인이 남긴 유일한 시행 단위 주관 보고이므로 Axis A의 Introspective Access sub-axis가 쓸 수 있는 첫 데이터다(ET-P6).

### I-2. "규범 평정은 이미 3인칭이다"와 LLM 관찰자 관점 (출처: llm-semantics U3, L1~L3 층; 근거 arXiv:2408.13718)
Tak & Gratch(2024)는 GPT-4의 appraisal 판단이 저자 본인 평가보다 독자 평균과 더 일치한다고 보고했다(llm-semantics 정리, DB full_text). llm-semantics는 이를 "평균한 1인칭 보고는 평균 관찰자와 수렴한다"로 일반화했다. 내 privileged access 검정(Round 1 C4)에 그대로 들어간다: AI 관찰자 라벨은 "평균 관찰자"의 기준선이고, 본인 보고가 peer 합의와 AI 관찰자 라벨을 넘어 본인 뇌를 설명하는 몫이 1인칭 성분의 후보다(ET-P2, ET-P3).

### I-3. 원인 귀속 불확실성과 정서 분화 (출처: brain-inspired 4절 2번; 근거 doi:10.1016/j.neubiorev.2022.104977)
Emanuel & Eldar(2023)는 분노와 슬픔 중 무엇을 느낄지는 나쁜 결과를 누군가의 행동에 귀속할 수 있는지에 달렸고, 귀속이 불확실하면 분화되지 않은 부정 정서가 최선일 수 있다고 썼다(brain-inspired 정리, DB full_text). 이것은 LeDoux & Brown(2017)의 "정서 schema가 경험을 분화시킨다"(doi:10.1073/pnas.1619316114)와 emotional granularity를 **계산 불확실성**으로 설명하는 길이다. Emo-FilM의 Agent appraisal(HumanCaused / ChanceCaused) 항목과 평정자별 원자료로 검정할 수 있다(ET-P5).

### I-4. 정서 범주 체계의 정보 병목 효율 (출처: geometry-info C7, S7; 근거 doi:10.1073/pnas.1800521115)
geometry-info는 "몇 개의 정서인가"를 압축과 정확도의 trade-off(IB) 문제로 바꾸자고 했고, 나와 llm-semantics와 논의하자고 제안했다. 내 Round 1 X1(scale-free 스펙트럼이면 "27개" 논쟁이 잘못 설정된 질문)과 정확히 맞물린다. 결합 방식: 스펙트럼에 꺾임점이 없으면 범주 수는 IB의 β로만 정해지고, 꺾임점이 있으면 그 rank와 IB 최적 범주 수가 일치하는지가 검정 가능한 예측이 된다(ET-P1 (c)).

### I-5. AI 라벨의 하류 추론 보정 (출처: adversarial-reviewer I1, I2, D4; 근거 doi:10.1126/science.adi6000, arXiv:2501.10970)
PPI와 alt-test는 AI 정서 라벨로 만든 뇌 지도의 편향을 무작위 인간 표본으로 보정한다. 내 Axis Q 제안에 없던 도구다. Emo-FilM 평정자별 원자료로 alt-test가 가능하다는 지적도 받아들인다. ET-P3의 AI 관점 라벨 비교에서 "AI 라벨이 어떤 CPM 성분에서 인간 평정자를 대체할 수 있는가"를 함께 보고하도록 한다.

### I-6. 관점 결속(perspective binding) (출처: frontier-ai C2; 근거 arXiv:2604.07729)
Sofroniew et al.(2026)은 LLM 정서 표상이 사용자, 가상 인물, Assistant에 같은 기제로 작동한다고 보고했다(frontier-ai 정리, DB full_text). 내 Round 1 X3(뇌가 "화면 속 인물의 정서"와 "내 정서"를 구분해 태깅해야 한다)과 같은 질문을 AI 쪽에서 측정한 것이다. 같은 자극에서 AI와 뇌의 관점 결속을 비교하는 설계를 ET-P7로 보낸다.

### I-7. "Digital twin = 규범 평정자의 뇌" (출처: encoding-foundation 4절 4번; 근거 arXiv:2605.04326)
TRIBE v2의 unseen-subject 예측은 "규범적 뇌 반응"이므로 규범 평정, 규범 뇌(in-silico), 본인 보고, 본인 뇌의 4자 구조가 생긴다는 관찰. privileged access 검정에 "규범 뇌" 기준선을 추가한다(ET-P2).

---

## 2. 보내는 제안

### ET-P1 → geometry-info (참조: vision-decoding)
* **제안:** 너희 C1(rank 분해 공유 스펙트럼)과 C7(IB 효율)은 우리 C1(정서 관련 신경 공간의 신뢰 차원 스펙트럼)과 같은 설계다. 하나로 합쳐 너희가 K(기하)를, 우리가 Q(측정)를 맡고, 우리 쪽 측정 요소 세 가지로 확장할 수 있다.
  * (a) **상한 보정:** Mind captioning 72클립 x 5회 반복에서 반복 기반 상한과 피험자 간 공유 상한을 같은 자극으로 함께 계산해, 반복이 없는 Horikawa 2,181개에 쓸 공유 상한의 보정 관계를 추정한다. 반복은 정서 반응을 바꾸므로(Horikawa Discussion 6째 단락) 1회차만 쓴 상한도 함께 보고한다.
  * (b) **교차 코호트 스펙트럼:** Horikawa 5명 x Mind captioning 6명의 교차 코호트 쌍(같은 2,180개 비디오, 다른 스캐너와 TR)과 코호트 내 쌍을 비교해, 공유 스펙트럼 중 스캐너, 프로토콜 고유 성분을 분리한다. 공유 피험자 수가 11명이 된다.
  * (c) **모형 비교:** Gauthaman et al. 4.2절이 직접 경고한 대로 power law, 지수 절단 power law, lognormal을 비교하고 교차검증 비선형 차원 추정을 병기한다. 저자들은 "차원성을 단일 스칼라로 정량화하지 말라"고 했다. 꺾임점이 검출 한계 rank보다 앞에 있을 때만 너희 C7의 IB 최적 범주 수와 대조한다.
* **관련 Axis:** K, Q, O (U는 대역별 분할의 라벨 해석에만)
* **근거:** arXiv:2409.06843 (4.1절 3째 단락, 4.2절; 출판본 doi:10.1371/journal.pcbi.1013714), arXiv:2505.12653 (Discussion 4째 단락), doi:10.1126/sciadv.adw1464, doi:10.1073/pnas.1702247114 (Discussion 6째 단락 마지막 문장), doi:10.1016/j.isci.2020.101060 (Discussion 6째 단락), doi:10.1073/pnas.1800521115, doi:10.1371/journal.pcbi.1006397
* **데이터셋:** Horikawa, Mind captioning (대조: NSD 공유 이미지의 시각피질 스펙트럼)
* **예상 반론:** (1) transmodal 영역 SNR이 낮아 스펙트럼 꼬리가 잡음 바닥에 묻히면 꺾임점이 생리적 한계가 아니라 측정 한계일 수 있다. 순열 null로 rank별 검출 한계를 표시해야 한다. (2) 두 코호트 모두 일본 참가자이고 피험자 중복 여부가 미확인이다(vision-decoding 0.1절). (3) Mind captioning S1은 같은 자극에 사전 노출되었다. (4) 공개 전처리본이 native volume이라 hyperalignment나 SRM이 필요하고, 정렬 학습 자극과 스펙트럼 평가 자극을 분리해야 한다. (5) 피험자 간 상한은 개인 특이 정서 신호를 잡음으로 분류한다(doi:10.1126/sciadv.abf7129).
* **label-provenance:** 스펙트럼 자체는 라벨 없음. 대역별 분할의 정서 라벨은 felt x 별도 평정자 규범(Cowen & Keltner 34/14). 시각, 의미 feature는 자극 계산
* **evidence-level:** R0
* **선행 수행 검색:** Round 1 WebSearch('cross-decomposition covariance spectrum ... emotion OR affective OR default mode OR transmodal'), Stage 2 재점검 WebSearch('power-law covariance spectrum dimensionality higher-order cortex ...'), 2026-11-12. 정서 자극 적용은 미발견. 시각피질 밖 확장은 Han & Bonner(arXiv:2505.12653)가 영화로 부분 수행

### ET-P2 → encoding-foundation (참조: generative-counterfactual, vision-decoding, llm-semantics, geometry-info)
* **제안:** 너희 Chain 3(group 예측 잔차가 본인 평정 편차를 예측하는가)은 generative-counterfactual CH5, vision-decoding R5, llm-semantics Chain 5, 우리 C4와 사실상 같은 질문이다. 하나의 "privileged access 검정"으로 묶고, 우리 쪽 Axis A의 Introspective Access sub-axis와 Axis Q의 측정 모형으로 검증 논리를 보강할 수 있다.
  * (a) **기준선 네 개를 명시한다:** B1 peer 합의(같은 영상을 본 다른 참가자들의 본인 보고 평균, leave-one-subject-out), B2 규범 뇌(TRIBE v2 group 예측), B3 AI 관찰자 라벨(MLLM, llm-semantics의 L2), B4 시청각-의미 feature. "본인 보고의 고유 설명 분산"은 B1~B4를 모두 통제한 뒤로 정의한다. 이것은 Binder et al.(2024)의 self-prediction 대 cross-prediction 논리를 인간에게 옮긴 것이다.
  * (b) **편차의 신뢰도를 먼저 추정한다:** Spacetop 개인 대 나머지 상관 중앙값은 0.46~0.77이고(Stage 1), 개인 편차는 차이 점수라 신뢰도가 더 낮다(reliability paradox, doi:10.3758/s13428-017-0935-1). 7차원 x 49영상의 계층 베이지안 모형으로 개인 반응 스타일(척도 사용) 성분을 분리한 뒤의 영상별 개인 편차를 예측 목표로 한다.
  * (c) **self 관련성 조절:** personal relevance 문항을 LeDoux & Brown(2017) HOTEC의 self 성분("no self, no emotion")의 약한 대리로 두고, 본인 보고 고유 분산이 자기 관련성이 높은 영상에서 커지는지 본다.
  * (d) **반증:** 신뢰도 보정 후 고유 분산이 0이면 "사후 본인 보고는 뇌 수준에서 peer 합의의 잡음 표본과 구분되지 않는다"로 보고한다. 이것도 Y sub-axis에 대한 정보다.
* **관련 Axis:** A(Introspective Access), U, Q, O, H
* **근거:** arXiv:2605.04326, doi:10.1126/sciadv.abf7129 (Discussion 5째 단락), arXiv:2408.13718, doi:10.1073/pnas.1619316114 (HOTEC 절, 'One implication' 단락), arXiv:2410.13787, doi:10.3758/s13428-017-0935-1, doi:10.1177/0956797620916786
* **데이터셋:** Spacetop alignvideo(주). Emo-FilM 참가자 사후 클립 평정 대 consensus(보조, 영화당 5항목, 영화 길이의 약 20%)
* **예상 반론:** (1) alignvideo 평정 약 51% 결측이고 클릭해야 저장되는 구조라 무작위 결측이 아닐 수 있다. (2) 영상 49개로 영상 단위 검정력이 낮다. (3) 평정 구간이 영상 끝 HRF와 겹친다. (4) TRIBE v2 공개 checkpoint는 피질만 예측하고 CC BY-NC다. (5) 고유 분산은 경험이 아니라 보고 행위(척도 사용, 회상 편향)일 수 있다. 보고와 경험의 구분은 이 설계로 풀리지 않는다(arXiv:2506.05068). (6) personal relevance는 self 성분의 약한 대리다.
* **label-provenance:** 목표는 felt x 본인. 기준선은 felt x peer 합의(B1), 규범 뇌(in-silico, B2), perceived x AI 추정(B3)
* **evidence-level:** R0. insilico-vs-observed: 혼합
* **선행 수행 검색:** Round 1 WebSearch('individual self-reported emotion ratings versus group-average normative ratings predicting fMRI ... own ratings'), 2026-11-12. 본인 보고의 고유 분산을 peer 합의와 AI 라벨 통제 후 검정한 연구 미발견. encoding-foundation은 자기 Chain 3을 partially(doi:10.1126/sciadv.abf7129)로 판정

### ET-P3 → llm-semantics
* **제안:** 너희 L1/L2/L3 층과 비교 형식 3(관점 조작)을 우리 S2 격자, 즉 Axis U의 "대상" 축(portrayed / perceived / felt)을 검증하는 측정 실험으로 쓸 수 있다.
  * 같은 Horikawa, Emo-FilM 자극을 MLLM에 세 관점으로 주석시킨다: (i) portrayed(인물이 드러내는 정서), (ii) perceived affective quality(이 장면이 일반적으로 불러일으킬 정서), (iii) felt-simulated(이 장면을 보는 "나"가 느낄 정서).
  * 1단계(행동): 세 AI 라벨의 차이 구조가 인간 perceived-felt 차이의 범주별 패턴(Saarimäki 2025: 같은 범주 공유 분산 평균 36%, 사랑, 자부심, 공포, 슬픔은 높고 지루함, 흥미, 분노는 낮음)과 순위가 맞는지 본다. 우리 데이터에는 인간 perceived 평정이 없으므로 보고된 범주별 패턴과의 순위 비교만 가능하다.
  * 2단계(뇌): 각 관점 라벨의 고유 설명 분산이 다른 영역에 있는가(Saarimäki 2025: felt에서 TPJ, 내측/외측 PFC, 시상, 소뇌 추가 동원).
  * Tak & Gratch(2024)대로 AI가 관찰자 관점에 머문다면 (iii)이 (ii)와 거의 같을 것이다. 그 결과 자체가 "AI 라벨은 felt를 대리하지 못한다"는 Axis U의 측정 증거다. adversarial-reviewer의 alt-test(arXiv:2501.10970)로 Emo-FilM 평정자 대체 가능성을 관점별로 함께 보고한다.
* **관련 Axis:** U, C, A, R
* **근거:** arXiv:2408.13718, doi:10.1162/imag_a_00517 (4.4절), arXiv:2509.24298 (Limitations: 프롬프트 민감도), doi:10.1162/imag.a.134, doi:10.1093/scan/nsae043, arXiv:2501.10970
* **데이터셋:** Horikawa, Emo-FilM (Spacetop 본인 보고는 3단계 외부 기준으로만)
* **예상 반론:** (1) "felt" 프롬프트로 얻은 라벨도 AI 추정이며 경험이 아니다. 해석은 "관점 지시가 AI 라벨의 뇌 설명 위치를 바꾸는가"로 한정해야 한다. (2) 프롬프트 표현에 민감하다. 표현 변형 여러 개의 분산을 보고해야 한다. (3) 성적, 폭력 내용은 내용 필터로 결측된다(llm-semantics P5). (4) Cowen & Keltner 비디오와 지도가 웹에 공개되어 있어 사전학습 오염 가능성이 있다.
* **label-provenance:** AI 추정 x portrayed / perceived / felt-simulated
* **evidence-level:** 뇌 분석 R0, 모델 쪽 프롬프트 조작 R1
* **선행 수행 검색:** WebSearch('LLM prompted as experiencer versus observer emotion ratings perceived versus felt emotion annotation brain encoding fMRI'), 2026-11-12. Tak & Gratch(2024)가 felt 대 perceived 문제를 개념적으로 제기했고, GPT-4V 평정을 fMRI stimulus model로 쓴 연구(doi:10.1162/imag.a.134)는 관찰자 관점만 썼다. 두 관점 조건의 직접 비교는 미발견

### ET-P4 → systems-neuro (참조: adversarial-reviewer, geometry-info)
* **제안:** 너희 Chain 2(network subspace로 Horikawa와 Westlin의 불일치 분해)는 adversarial-reviewer D1(multiverse), geometry-info C1, 우리 C2와 같은 질문을 다른 축으로 자른 것이다. 하나의 multiverse 격자로 통합할 수 있다.
  * 요인 A 입력 공간: 분산 기준 전뇌 PCA(Westlin) / 평정 기반 voxel 선택(Horikawa, fold 안에서) / network subspace(너희) / 평정 독립 피험자 간 신뢰 부분공간(우리)
  * 요인 B 전역, 세션, run 분산 처리(너희)
  * 요인 C 군집 수 선택: BIC / 고정 27 / DP-GMM
  * 요인 D 대응 지표: NMI 대신 chance 보정 지표(AMI)와 순열 기준. 연속 평정에는 군집 지시변수로 평정을 예측하는 교차검증 R²를 병기(adversarial-reviewer U2의 NMI 편향 지적 반영)
  * 우리 쪽 추가: Westlin 개인 군집의 **피험자 내 session 분할 재현성**(재초기화 안정성 Rand 0.85와 구분), 그리고 결과를 "정서 경험의 구조"가 아니라 "규범 평정과 대응하는 신경 구조의 측정 타당성"으로 서술하는 해석 규칙. Mind captioning 지각 데이터(같은 비디오, 다른 6명)로 외부 재현.
* **관련 Axis:** Q, T, K, E, O
* **근거:** arXiv:2507.00320 (Results; Discussion 6째 단락), doi:10.1016/j.isci.2020.101060, doi:10.1038/s41598-020-77117-8 (Discussion 2째 단락: 정서 신호가 작으면 비지도 군집은 부수 특징을 따른다), doi:10.1038/s41593-025-01945-y, arXiv:2409.06843, doi:10.1126/sciadv.adw1464
* **데이터셋:** Horikawa raw(CC0), Mind captioning 지각 데이터
* **예상 반론:** (1) 조합 수가 폭발한다. 요인 수준을 사전등록으로 줄이고 specification curve로 보고해야 한다. (2) 5명이라 참가자별 결과를 모두 보고해야 한다. (3) 전역 신호 제거가 정서 관련 분산도 지울 수 있다(systems-neuro의 Safeguards). (4) 신뢰 부분공간 경로는 공유 성분만 남겨 Westlin이 본 개인 특이 구조를 정의상 지운다. 그래서 개인 특이 구조는 (a) 경로의 session 분할 재현성으로 따로 평가해야 한다.
* **label-provenance:** felt x 별도 평정자 규범
* **evidence-level:** R0
* **선행 수행 검색:** WebSearch('multiverse analysis emotion categories fMRI decoding analytic choices typological versus constructionist reanalysis 2024 2025 2026'), 2026-11-12. Horikawa 데이터의 multiverse, specification-curve 분석 미발견

### ET-P5 → brain-inspired
* **제안:** 너희가 정리한 Emanuel & Eldar(2023)의 "원인 귀속이 불확실하면 분화되지 않은 부정 정서" 가설을 우리 쪽 Axis A(정서 분화, LeDoux & Brown의 schema 분화)와 Axis Q(평정자 불일치)로 검증할 수 있다. Emo-FilM에는 Agent appraisal(HumanCaused / ChanceCaused) 1 Hz 평정, Anger와 Sad 이산 항목, 평정자별 원자료가 있다(Stage 1 항목표).
  * (a) 행동 수준: Agent 평정의 평정자 간 불일치(귀속 불확실성)가 큰 시점에서 Anger와 Sad consensus가 함께 오르는(미분화) 경향이 있는가.
  * (b) 신경 수준: 같은 시점에서 Anger 대 Sad의 교차검증 신경 판별성(crossnobis)이 낮아지는가.
  * (c) 분화 방향: Agent가 HumanCaused로 명확할 때 Anger 쪽, ChanceCaused로 명확할 때 Sad 쪽 신경 패턴으로 이동하는가(타인 행위 귀속이 분노를, 비인격적 상황 귀속이 슬픔을 가른다는 appraisal 행동 결과의 신경 버전).
  * 너희 Chain 2(정서 범주 vs 행동 경향)와 같은 banded ridge 틀에 Agent 불확실성을 조절변수로 넣으면 된다.
* **관련 Axis:** A, N, Q (V와 교차)
* **근거:** doi:10.1016/j.neubiorev.2022.104977, doi:10.1073/pnas.1619316114 (emotion schema 단락), doi:10.1093/cercor/bhad093, doi:10.1037/emo0001619, doi:10.1038/s41597-025-04803-5
* **데이터셋:** Emo-FilM
* **예상 반론:** (1) Agent 항목의 평정자 불일치는 귀속 불확실성이 아니라 측정 잡음일 수 있다. 항목별 평정자 일치도로 정규화하고 영화 수준 confound를 확률효과로 둔다. (2) 평정자당 6개 항목만 배정되어 Agent 평정자와 Anger/Sad 평정자가 다른 사람일 수 있다. 그러면 결과는 "같은 사람 안의 귀속-정서 연결"이 아니라 "자극 수준 연결"이다. (3) 영화 14편이라 Anger가 강한 장면이 소수 영화에 몰릴 수 있다. (4) 평정은 평정자 내 z-score라 절대 강도가 아니다.
* **label-provenance:** felt x 별도 평정자 규범(consensus), 그리고 평정자 간 변동 자체를 측정치로 사용
* **evidence-level:** R0
* **선행 수행 검색:** WebSearch('appraisal of agency credit assignment uncertainty anger sadness differentiation neural pattern fMRI emotion differentiation naturalistic'), 2026-11-12. 행동 수준 appraisal 연구(타인 행위 귀속과 분노, 상황 귀속과 슬픔)는 검색 요약으로만 확인했고 식별자 미확인. 자연 자극 fMRI에서 귀속 불확실성과 정서 신경 분화를 연결한 연구는 미발견

### ET-P6 → vision-decoding
* **제안:** 너희 R2(같은 클립 회상에서의 정서 재활성, NEVER 검증)를 우리 Axis A의 Introspective Access sub-axis와 Axis W로 확장할 수 있다. Mind captioning의 시행별 vividness는 fMRI 참가자 본인의 주관 보고다.
  * (a) 재활성을 시각 부분공간(저수준 DNN feature decoder)과 정서 부분공간(34/14 규범 decoder를 시각, 의미 feature로 잔차화)으로 나누고, vividness가 어느 쪽 재활성을 더 잘 가르는지 **type-2 민감도**(vividness로 재활성 강, 약 시행을 판별하는 ROC 면적, meta-d' 논리)로 비교한다.
  * (b) vividness가 낮은 시행에서도 정서 부분공간 재활성이 남는가(보고되지 않은 정서 재활성). 남는다면 LeDoux & Brown의 "정서는 무의식일 수 없다"와 1차 이론 사이 논쟁에 대한 약한 관찰 증거가 된다. 단 vividness는 심상의 생생함 보고이지 정서 자각 보고가 아니므로 이 해석은 탐색적으로만 쓴다.
  * 비디오 재생에서 재활성과 vividness의 관계는 이미 확립되어 있다(St-Laurent 2015, Bone 2020). 따라서 새로운 부분은 정서 부분공간의 분리와 type-2 비교로 한정한다.
* **관련 Axis:** W, A(Introspective Access), Q, G
* **근거:** doi:10.1126/sciadv.adw1464, doi:10.3758/s13423-017-1313-9, doi:10.1162/jocn_a_00839, doi:10.1038/s41467-020-15763-2, doi:10.1073/pnas.1619316114, doi:10.1093/nc/nix007
* **데이터셋:** Mind captioning 회상(주), Horikawa 2020 지각 데이터(decoder 학습 보강)
* **예상 반론:** (1) 회상 직전 텍스트 cue가 의미 정보를 준다. (2) 회상 직후 비디오 재제시와 HRF가 겹친다(너희 R2 교란 목록). (3) 회상에서 해독되는 정서는 경험이 아니라 정서 지식일 수 있다(너희 0.3절 L5). (4) 72클립의 정서 분포와 vividness 분포가 미확인이라 검정력 계산이 먼저다. (5) type-2 분석의 "정답"이 decoder 출력이라 decoder 잡음이 metacognitive 비효율처럼 보일 수 있다. 시각 부분공간 비교가 이 잡음의 대조 조건 역할을 한다. (6) vividness 척도 사용의 개인차가 있어 개인 내 순위로 분석해야 한다.
* **label-provenance:** decoder 목표는 felt x 별도 평정자 규범. vividness는 본인 보고(심상)
* **evidence-level:** R0
* **선행 수행 검색:** WebSearch('trial-wise imagery vividness predicts decoding strength reactivation fMRI emotional memory recall vividness affective reactivation'), 2026-11-12. 비정서 비디오 재생의 재활성-vividness 대응(doi:10.1162/jocn_a_00839)과 feature 수준별 대응(doi:10.1038/s41467-020-15763-2)은 수행됨(partially). 정서 부분공간을 분리한 분석은 미발견

### ET-P7 → frontier-ai
* **제안:** 너희 C2(functional emotion의 인물 무차별성, perspective binding)를 우리 X3(자기 태깅)와 Spacetop의 같은 참가자 다과제 설계로 검증할 수 있다. 같은 참가자가 alignvideo(자기 경험 보고), shortvideo(인물 정서 귀속), faces(표정 지각)를 모두 했다.
  * (a) alignvideo 본인 평정으로 학습한 정서 축이 shortvideo, faces의 타인 정서 판단으로 얼마나 교차 일반화되는가(관점 무차별 성분).
  * (b) 일반화되지 않는 자기 특이 성분은 어디(mPFC 하위영역, TPJ)에 있는가.
  * (c) 같은 자극을 LLM/VLM에 인물 관점과 관찰자 관점 프롬프트로 넣어 정서 vector의 관점 간 유사도를 재고, 이것을 뇌의 교차 일반화 패턴과 대조한다. Sofroniew 2026의 "인물 무차별"이 뇌에서는 부분적으로만 성립한다면, 그 차이가 AI 정서 표상과 뇌 정서 표상의 구분점이 된다.
* **관련 Axis:** U, A, R(Model-internal Emotion Representations), E
* **근거:** arXiv:2604.07729, doi:10.1523/JNEUROSCI.1676-14.2014, doi:10.1162/imag_a_00517, doi:10.1016/j.bpsc.2025.11.011, doi:10.1073/pnas.1619316114
* **데이터셋:** Spacetop
* **예상 반론:** (1) 과제, 자극, 반응 형식이 모두 달라 교차 일반화 실패가 관점이 아니라 과제 차이일 수 있다. 정서 무관 대조(같은 과제 쌍의 비정서 성분 교차 일반화)를 둬야 한다. (2) shortvideo는 mentalizing 판단이라 정서 강도 평정과 형식이 다를 수 있다(Stage 1). (3) faces 자극의 출처와 재배포 조건이 미확인이다. (4) alignvideo 결측. (5) AI vector 쪽은 모델 내부 표상이며 경험으로 해석하지 않는다(encyclopedia X 단서).
* **label-provenance:** felt x 본인(alignvideo), perceived(타인 정서 귀속, 표정 지각) x 본인(shortvideo, faces), AI 모델 내부 vector
* **evidence-level:** 뇌 분석 R0, 모델 vector R1
* **선행 수행 검색:** WebSearch('same participants self-experienced emotion and attributed emotion to others cross-decoding shared neural representation fMRI videos perspective'), 2026-11-12. Skerry & Saxe(2014)가 MPFC에서 추론된 정서 → 경험 사건 일반화를 보고(partially, 문장 자극). 같은 참가자, 영상 자극, AI 관점 vector 비교를 결합한 연구는 미발견. 같은 연구 계열에서 공감적 공포와 주관 공포 signature를 분리한 사례(doi:10.1016/j.bpsc.2025.11.011)는 있음

---

## 3. 받은 제안에 대한 응답

(Coordinator가 전달한 뒤 추가)

---

## 4. Coordinator 질문 8개에 대한 답 (emotion-theory 관점)

**Q1. Vision Decoding 연구자가 Emotion Neuroscientist의 문제를 해결할 수 있는가?**
일부는 해결한다. 시각-의미 내용(llm-semantics의 L1)을 정밀하게 통제하는 feature, 재구성의 정서 충실도 측정, 그리고 Mind captioning 반복 제시로 얻는 noise ceiling(doi:10.1126/sciadv.adw1464)은 Horikawa의 "분모가 없다" 문제(adversarial-reviewer U3)를 직접 줄인다. 그러나 해독된 정서는 정의상 portrayed나 규범 수준 정보이며 참가자 경험의 증거가 아니다(vision-decoding 0.3절 L1~L6과 같은 판단). 또 output dimension collapse(doi:10.1016/j.neunet.2025.107515)는 "범주적 정서 표상" 결론이 군집화된 자극 표본의 인공물일 수 있다는 경고를 정서 쪽에 준다. 그래서 답은 "측정 문제는 해결에 기여하고, 경험 문제는 해결하지 못한다"이다.

**Q2. LLM의 representation이나 reasoning 능력을 neural emotion representation 분석에 활용할 수 있는가?**
활용할 수 있지만 역할을 정해야 한다. LLM 판단은 평균 관찰자(3인칭) 관점에 가깝다(arXiv:2408.13718). 따라서 LLM 출력은 귀속, 지각 정서의 회귀자이자 privileged access 검정의 기준선으로 가장 유용하고, 경험 정서의 대리로는 약하다(ET-P2, ET-P3). LLM 내부 appraisal 방향(arXiv:2502.05489)은 appraisal 인식 질문에 쓸 수 있다. 정서 단어 처리 영역이 정서 경험 decoding 영역과 겹친다는 결과(doi:10.1093/scan/nsae043)는 반대로 경고다. 뇌 decoding 성공이 개념, 언어 처리를 읽은 것일 수 있으므로 LLM feature를 넣은 분석은 "경험"과 "개념화"의 구분을 해석 단계에서 명시해야 한다.

**Q3. Generative AI로 emotion과 visual semantics를 분리해 검증할 수 있는가?**
우리 데이터만으로는 R1(모델 내 개입)까지, 새 행동 평정을 모으면 R2까지 가능하다. Axis Q 관점의 추가 조건이 둘 있다. (1) 편집 자극의 정서는 다시 인간이 평정해야 한다. 그렇지 않으면 "편집 후 정서"는 AI 추정 라벨이다. (2) 원본과 편집본에 같은 평정 도구를 쓸 때 측정 불변성(편집 아티팩트가 평정 척도 사용을 바꾸는지)을 점검해야 한다. 정서를 조작하면 의미도 함께 바뀐다는 문제(arXiv:2512.00557)가 있으므로, 생성 없이 쓸 수 있는 자연 통제(Mind captioning의 정서 배제 인간 캡션, vision-decoding R6)를 먼저 쓰는 것이 비용 대비 낫다고 본다.

**Q4. Emotion Dynamics를 dynamical systems나 state-space learning의 문제로 재정의할 수 있는가?**
가능하다. 단 측정 층을 모형에 넣어야 한다. Emo-FilM 연속 평정은 항목당 3~4명 consensus이고 평정자 내 z-score이며 항목별 일치도가 0.21~0.60이다(Stage 1). 관측 잡음이 항목마다 다른 목표에 상태공간 모형을 맞추면 잡음 차이가 "동역학 차이"로 보인다. 평정자별 관측 모형을 둔 계층 상태공간 모형이 필요하다. 또 상태 대 drift 문제(doi:10.1126/sciadv.abf7129, Discussion 4째 단락)와 지도형 표상의 전이 구조(doi:10.1038/s41467-025-68240-z)는 신경 쪽 동역학이고, 보고 쪽 동역학(연속 경험이 회고 보고로 요약되는 규칙, multimodal-dynamics Chain 5)은 Introspective Access sub-axis의 질문이다. 둘을 같은 모형의 두 관측 채널로 두는 것을 제안한다.

**Q5. Brain Foundation Model의 latent representation에서 감정 관련 구조를 찾을 수 있는가?**
현재 근거로는 미정이다. 유일한 정서 회귀는 시간 블록 무작위 분할과 portrayed 라벨로 보인다(arXiv:2601.23090, encoding-foundation Chain 5 판단). 우리 쪽 제안은 평가 기준을 바꾸는 것이다. decoding 정확도 대신 (1) latent가 피험자 간 신뢰 공유 스펙트럼(ET-P1)을 얼마나 보존하는지, (2) 라벨 출처별(본인, 규범, AI) 성능 차이를 보고하는지, (3) 라벨 신뢰도 상한 대비 성능을 쓰는지로 판정한다. 피질 전용 표상이면 피질하 정서 정보는 구조적으로 빠진다는 점도 함께 표시해야 한다(arXiv:2510.13768).

**Q6. Music, Video, Image의 공통 정서 특징과 modality-specific 특징을 뇌 수준에서 구분할 수 있는가?**
부분적으로만 가능하다. 음악 단독 fMRI 데이터가 없고(Emo-FilM 사운드트랙 분해만 가능), 데이터셋 간 라벨은 직접 합칠 수 없다(Stage 1 3절 수준 2~3). 행동 수준에서 음악 경험은 13차원(doi:10.1073/pnas.1910704117), 비디오 경험은 24~27차원(doi:10.1073/pnas.1702247114)이었다. 그래서 라벨이 아니라 **양식별 신뢰 차원 스펙트럼**(ET-P1 방법을 데이터셋별로 적용)을 비교하는 것이 라벨 비호환을 피하는 길이라고 본다. vmPFC의 양식 무관 범주 부호(doi:10.1126/sciadv.adk6840)는 공통 성분의 후보다. 단 그 연구도 지적했듯 양식마다 유발되는 정서 자체가 달라서, 공통 성분 추정에는 양식별 정서 분포 차이를 통제해야 한다.

**Q7. Neuroscience에서 관찰되는 정서 관련 계산을 AI architecture의 구조적 제약으로 구현할 수 있는가?**
의식 이론 쪽에서 두 가지 구조 제약을 제안할 수 있다. (1) HOT-2식 출처 monitoring 모듈: 정서 신호가 "묘사된 인물"에 관한 것인지 "관찰자 자신"에 관한 것인지 태깅하는 층(arXiv:2308.08708 2.3.3절). AI 정서 vector가 관점 무차별이라는 결과(arXiv:2604.07729)가 이 모듈이 없는 상태로 볼 수 있다. (2) HOT-4식 quality space 제약: 정서 임베딩에 smooth하고 sparse한 부호를 강제하는 정규화(Stringer 2019의 smoothness, doi:10.1038/s41586-019-1346-5). 두 제약을 넣은 모델과 뺀 모델의 뇌 정렬을 비교할 수 있다. 단 이것은 계산 지표 비교이며 AI의 정서 의식에 대한 주장이 아니다.

**Q8. 정서 라벨이 없는 NSD 같은 데이터도 다른 데이터셋과의 representation alignment로 의미 있게 활용할 수 있는가?**
측정 쪽으로는 의미가 크고, 정서 구성 개념 쪽으로는 약하다. NSD는 이미지당 3회 반복이 있어 반복 기반 상한과 피험자 간 상한의 관계를 보정하는 데 정서 라벨 없이 쓸 수 있다(adversarial-reviewer D5와 같은 방향, ET-P1의 대조 조건). 반면 NSD에서 "정서"라는 말을 쓰려면 라벨 출처가 AI 추정이거나(PPI로 보정하려면 새 인간 표본 필요, doi:10.1126/science.adi6000) 다른 데이터셋에서 학습한 encoder의 in-silico 예측이어야 한다. NSD 이미지 정서가는 대체로 중립이라(Stage 1) 정서 범위도 좁다. 정렬 결과는 "NSD 뇌가 다른 데이터셋 정서 공간과 같은 기하를 갖는다"가 아니라 "정서 데이터셋에서 정의한 부분공간이 NSD 반응에서 어떤 분산을 갖는가"로 서술해야 한다.

---

## 5. Axis 결정에 대한 의견

* **Introspective Access를 A의 Sub-axis로 둔 결정:** 수용한다. 조건 두 가지를 제안한다.
  1. Sub-axis는 무작위 경로(P5)에서 거의 뽑히지 않으므로, 전략 경로 H(Reverse Inspiration)나 C(Representation Comparison)에서 최소 한 번 명시적으로 쓰도록 Coordinator가 지정해 주기 바란다. 그렇지 않으면 외부 분야 Artificial Consciousness and Metacognition이 조합에서 사라진다.
  2. encyclopedia 2.2절의 "데이터 제약: 4개 데이터셋에 보고 확신도나 재평정 일관성 측정이 없다"는 갱신이 필요하다. Mind captioning의 시행별 vividness(본인 주관 보고), Spacetop의 본인 보고 대 peer 합의, Emo-FilM의 참가자 사후 평정 대 consensus로 데이터 조건이 부분 충족된다(ET-P2, ET-P6).
* **Axis U(Label Provenance & Perspective)를 독립 Axis와 필수 태그로 함께 둔 결정:** 동의한다. 값 목록에 "AI 추정"을 프롬프트 관점별로 나누는 표기(관찰자 / 경험자 시뮬레이션 / 인물)를 추가하자고 제안한다(ET-P3). 같은 AI라도 관점 지시에 따라 대상 축 값이 달라지기 때문이다.
* **Axis W:** 지지한다. Mind captioning의 vividness는 W와 A(Introspective Access)를 잇는 드문 변수라는 점을 encyclopedia W 항목에 덧붙이기를 제안한다.
* **X를 R의 Sub-axis로 둔 결정:** 이견 없다.
* **"Recognition vs Experience"의 이중 처리(Axis U + 태그):** 이견 없다. Round 1에서 나는 독립 Axis가 불필요하다고 했지만, 무작위 조합에서 U가 뽑혔을 때 이 구분이 질문의 중심이 되는 효과가 있으므로 현재 처리가 낫다고 본다.

---

## 6. 내 Round 1 chain의 갱신 (5개 데이터셋과 Round 2 수렴 반영)

| Round 1 chain | 갱신 |
|---|---|
| C1 신뢰 차원 스펙트럼 | geometry-info C1과 통합 제안(ET-P1). Mind captioning으로 반복 상한 보정과 교차 코호트 검정 추가 |
| C2 신뢰 부분공간 비지도 구조 | systems-neuro Chain 2, adversarial-reviewer D1과 하나의 multiverse로 통합 제안(ET-P4) |
| C3 HOT 관찰 검정 (Emo-FilM, Stage 2에서 partially) | encoding-foundation Chain 2, systems-neuro Chain 1, adversarial-reviewer D5와 같은 분할 틀을 공유할 수 있다. 내 고유 부분은 Feeling 대 Appraisal 분포 비교를 HOT 판별 검정으로 쓰는 것이다. Mind captioning 정서 배제 인간 캡션을 1차 의미 내용 통제로 추가할 수 있다(Horikawa 자극에 한해) |
| C4 privileged access | 다섯 에이전트의 같은 설계와 통합 제안(ET-P2). 기준선 네 개와 편차 신뢰도 모형 추가 |
| C5 평정 불일치의 신경 분해 | llm-semantics U2(인간, LLM, 뇌 세 엔트로피)와 adversarial-reviewer D4(alt-test)와 결합 가능. Mind captioning 반복 데이터가 있으면 "같은 사람의 반복 간 신경 변동"을 측정 잡음 기준으로 쓸 수 있어 분해가 쉬워진다 |
| C6 혼합 정서 가산성 | 변경 없음. frontier-ai C3(sparse 중첩 vs 연속 좌표)와 같은 판별 논리를 공유 |
| C7 정서 quality space | ET-P6과 연결: vividness가 정서 유사성 구조를 따라 오류를 내는지(유사한 정서의 클립을 혼동하는지)로 개인 수준 quality space의 약한 지표를 얻을 수 있다(탐색 아이디어, 검색하지 않음) |
| C8 개인 고차 rank와 보고 편차 | geometry-info C8(개인 기하 형질), encoding-foundation Chain 3과 ET-P2 안에서 함께 다룬다 |

---

## 7. 검색 기록과 미확인 사항

* **이번 라운드 검색(모두 2026-11-12):** WebSearch 4건(ET-P3, P5, P6, P7 선행 확인), Crossref 4건과 PubMed 4건(새 인용 5편 확인). 이전 라운드 검색을 재사용한 제안은 ET-P1, P2, P4이며 각 제안에 원 검색 질의를 적었다.
* **새 인용 문헌의 검증 수준:** 5편 모두 Crossref로 서지를 확인하고 PubMed 초록을 읽었다(abstract_only). 본문은 읽지 않았다.
* **미확인:** Mind captioning 저장소의 실제 파일(반복 클립, 회상 과제, vividness, 캡션 포함 여부)은 사용자 보유본 기준으로 확인되지 않았다(ET-P1, P6, Q1, Q3 전제). Horikawa와 Mind captioning 피험자 중복 여부도 미확인이다. Emo-FilM에서 Agent 항목과 Anger, Sad 항목의 평정자 배정이 겹치는지(ET-P5 반론 2)는 평정자별 원자료로 확인해야 한다.
* **검색 요약 수준으로만 본 것:** ET-P5의 행동 appraisal 근거(타인 행위 귀속과 분노, 상황 귀속과 슬픔)는 검색 요약에서만 봤고 식별자로 확인하지 않아 근거 ID로 쓰지 않았다.
* **다른 에이전트 Round 1 판정에 대한 메모:** 내가 읽은 범위에서 vision-decoding R5와 encoding-foundation Chain 3도 Spacetop의 "나머지 참가자 평균"을 규범 대리로 쓴다. 이것은 별도 평정자 규범이 아니라 fMRI 참가자 집단의 peer 합의이므로, Axis U 표기에서 "peer 합의"로 구분해 적어야 한다(Stage 1 3.2절의 "규범" 정의와 다름).
