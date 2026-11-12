# systems-neuro Round 3: Constructive Disagreement

* 작성: systems-neuro (Axis E Neural Targets, 외부 분야 Computational Psychiatry)
* 기준일: 2026-11-12
* 따른 절차: `reference/protocols.md` P3. 배정: `outputs/discussion/round3_assignment.md`(GI-P5, GC-P2, EF-P1)
* 읽은 것: 각 제안 원문(보낸 에이전트 round2.md 2절)과 근거 chain(vision-decoding R5, R6; encoding-foundation Chain 1, 3; generative-counterfactual CH1, CH3, CH5; llm-semantics Chain 1, 5)
* 이번 검토에서 새로 확인한 문헌: doi:10.1016/j.neuroimage.2020.116851(Chen 2020, PubMed MCP 전문), arXiv:2605.23895(BrainCause, arXiv API 429로 식별자 경로 확인 못 함, search_index). 둘 다 `literature.jsonl`에 추가했다(`added_round: "Round 3"`). Mind captioning 전처리의 전역 신호 회귀 여부를 원문 Methods로 새로 확인했다(아래 공통 사실).
* 표기: 판정 7항목은 P3의 순서를 따른다. 각 제안 끝에 signal-feasibility 점검과 수정안을 둔다.

## 공통 사실 (세 검토에 모두 쓰임)

1. **Mind captioning 전처리는 CSF, WM, GM 평균 신호와 그 미분, 제곱 12개를 회귀**했다(doi:10.1126/sciadv.adw1464 Methods, PubMed MCP 전문). 공개 전처리본에는 전역 자율신경 성분이 대부분 빠져 있다. Horikawa 2020 공개본의 nuisance 항목은 미확인이다.
2. 전역 fMRI 신호는 교감 매개 각성(심박, 호흡량, PPG 진폭)과 결합하며 저주파 분산의 약 25%를 차지하고, 감각운동 피질에서 먼저 나타나는 공간 구조를 가진다(doi:10.1038/s41593-025-01945-y, Discussion 2, 11, 13째 단락).
3. 영상 시청 중 심박은 자극에 동기화된다(doi:10.1093/pnasnexus/pgac020, 초록). 따라서 자율신경 성분은 '개인 잡음'이 아니라 '자극 구동 공유 성분'과 '개인 반응성 차이'를 둘 다 가진다.
4. 피질하와 내측 측두엽은 amygdala 최적화 획득에서도 tSFNR이 피질보다 낮고 dropout 개인차가 크다(doi:10.1038/s41597-026-07065-x, Technical Validation). multiband 가속은 뇌 중심부 시간 잡음을 키운다(doi:10.1016/j.neuroimage.2021.118617).

---

## 1. GI-P5 (geometry-info → vision-decoding): Spacetop "개인 잔차 대 본인 보고 편차" 제안 여섯 개를 기준선 multiverse 하나로

### 제안 요약
같은 Spacetop alignvideo 영상에서 '기대 반응(기준선)'을 뺀 개인 뇌 잔차가 그 사람의 본인 평정 편차를 예측하는지를, 다섯 에이전트가 제안한 기준선(TRIBE v2 예측, LOO 평균, MLLM 예측, peer 평균과 rank 범위, INT 개인화)으로 한꺼번에 사전등록해 돌린다. 잔차 신뢰도를 먼저 보고하고, rank 대역별로 나누며, 기준선 간 차이 자체를 결과로 본다.

### 판정 7항목

1. **이미 연구되었는가: partially.**
   * 검색: WebSearch "intersubject representational similarity analysis individual variation affective experience movie fMRI idiosyncratic brain response predicts self-report"(2026-11-12) → Chen 2020(doi:10.1016/j.neuroimage.2020.116851)과 Finn 2020 idiosynchrony 개관(doi:10.1016/j.neuroimage.2020.116828). WebSearch "Spacetop dataset alignvideo individual ratings idiosyncratic brain response residual hyperalignment self-report deviation 2025 2026"(2026-11-12) → Spacetop 데이터 논문과 hyperalignment 배경만, 같은 분석 미발견.
   * Chen 2020은 26명의 **특성 선호**(설문 항목 벡터) 개인 간 거리와 뇌 동역학 개인 간 유사도를 IS-RSA로 연결했고, 성애 영상에서만 보상, DMN, mentalizing network에서 대응을 보였다(전문 확인). 영상별 **본인 평정 편차**를 예측한 것은 아니다. Chang 2021(doi:10.1126/sciadv.abf7129)은 vmPFC 개인 고유 상태를 보였지만 평정은 별도 표본이다. 따라서 '자극 단위 보고 편차'는 미발견이고, '개인 뇌 변이와 개인 경험 변이의 연결'이라는 질문 자체는 선행이 있다.
2. **단순한 모델 적용인가: 아니다.** 질문이 분명하고(개인 특이 신경 신호가 개인 경험 보고를 담는가), 기준선 간 차이를 결과로 보는 설계는 새롭다. 다만 기준선 5종 x rank 대역 x ROI 표가 커지면 '어떤 기준선이 가장 잘 맞나'라는 방법 비교로 흐를 위험이 있다.
3. **Neuroscience Question을 해결하는가: 조건부.** 결과가 양성이면 '규범과 다른 개인 경험이 신경 수준에서 읽힌다'는 Axis U의 핵심 질문(본인 보고의 고유 설명력)에 답한다. 그러나 잔차의 구성(신경 개인차, 개인 자율신경 반응성, 시선, 움직임)을 분해하지 않으면 양성 결과도 '무엇이' 보고를 예측했는지 말할 수 없다.
4. **정서가 아닌 것을 decoding하는가: 위험이 크다.**
   * 개인 자율신경 반응성: 같은 영상에 심박이 더 크게 반응하는 사람은 전역 BOLD 잔차도 크고(공통 사실 2, 3), 각성 관련 문항(afraid, engaged)을 더 높게 보고할 수 있다. 이 경로는 '신체 반응이 보고를 바꾼다'는 의미 있는 결과일 수도 있지만 '정서의 신경 표상'은 아니다. Spacetop 공개본에는 생리가 없다.
   * 시선: Spacetop에는 eye tracking이 없어 개인별 시각 입력 차이가 시각 피질 잔차를 만든다(Horikawa 2020 Limitations 3째 단락이 같은 문제를 지적).
   * 평정 반응 양식: 척도 사용 습관(항상 높게 주는 사람)은 보고 편차를 만들지만 정서 경험 차이가 아니다.
   * 평정 구간과 영상 끝 HRF 중첩, 평정 행위의 운동 신호(제안자도 인정).
5. **현재 데이터로 검증 가능한가: 가능하나 검정력이 낮다.** 영상 49개, 평정 약 51% 결측이면 한 사람당 유효 영상이 25개 안팎이다. 잔차-편차 상관의 개인 내 추정이 매우 불안정하다. 참가자 약 100명은 사람 간 풀링(위계 모형)에는 충분하다.
   * **signal-feasibility:** TR 0.46 s, MB8, 2.7 mm. 피질하 잔차는 신뢰도가 낮을 가능성이 크다(공통 사실 4). vmPFC, OFC는 TE 27.2 ms라 Horikawa(43 ms)보다 유리하지만 dropout 지도로 확인 필요. 공개 생리 없음, 호흡성 pseudo-motion이 FD를 부풀린다(Stage 1).
6. **더 강력한 방법이 있는가: 있다.**
   * 잔차를 먼저 뽑고 편차와 상관시키는 2단계 대신, **영상 x 사람 무선효과를 갖는 위계 모형으로 뇌 잔차와 보고 편차를 함께 모형화**하면 측정 오차로 인한 감쇠를 줄이고 결측을 모형 안에서 다룰 수 있다.
   * 기준선이 필요 없는 대안으로 **영상 단위 IS-RSA**(Chen 2020의 방법을 특성 대신 영상별 평정 벡터에 적용)를 병행한다.
   * 잔차에서 **사람별 전역 성분과 저rank 대역을 분리**한 판을 따로 돌린다(GI-P7, SN-P1과 같은 진단).
7. **기대와 다른 결과도 의미 있는가: 잔차 신뢰도 게이트를 통과했을 때만.** 신뢰할 만한 잔차가 보고 편차를 예측하지 못하면 '이 해상도에서 개인 신경 편차는 보고 편차와 무관'이라는 의미 있는 null이다. 잔차 신뢰도가 낮은 상태의 null은 정보가 없다. 제안자가 신뢰도 선보고를 규칙으로 둔 점은 좋다.

### 수정안
1. **게이트 3단계를 사전등록:** (A) ROI x rank 대역별 잔차 split-half 신뢰도(영상 절반 분할), (B) 보고 편차의 신뢰도(같은 사람의 비슷한 영상 간 일관성, 척도 양식 보정 후), (C) 잔차의 혼입 지표(사람 x 영상별 전역 신호 크기, FD, 영상 끝 HRF 구간). 셋 다 통과한 ROI와 대역만 1차 분석에 넣는다.
2. **기준선을 3개로 줄인다:** LOO 사람 평균(경험적 기준), TRIBE v2 예측(자극 계산 기준, in-silico), MLLM 예측(평균 관찰자 기준, AI 추정). peer 평균과 rank 범위는 LOO 평균의 변형, INT 개인화는 정렬 방식의 선택이므로 민감도 분석으로 둔다. 다중비교를 줄이고 해석을 단순화한다.
3. **1차 분석은 위계 모형:** 뇌 잔차(ROI, 대역)와 보고 편차를 사람 x 영상 수준에서 함께 모형화하고, 공변량으로 전역 신호 크기, FD, engaged 문항, 사람별 척도 평균을 넣는다.
4. **기준선 없는 대조:** 영상 단위 IS-RSA를 같은 분할로 병행해, 기준선 선택에 결과가 의존하는지 본다.
5. **해석 규칙:** 전역 성분을 제거하면 사라지는 예측은 '개인 신체 반응성 경로'로, 남는 예측은 '국소 신경 편차 경로'로 나눠 보고한다. Spacetop 생리가 입수되면(사용자 결정 11번 보류 중) 이 분리를 직접 검정한다.
6. 캡션 통제 부분(제안 5번, Horikawa + Mind captioning)은 Mind captioning이 전역 신호 회귀본이라는 점을 공통 사실 1에 따라 표기한다.

### 종합
과학적 질문은 Axis U의 핵심이며 통합 방향은 옳다. 그러나 현재 설계로는 양성 결과가 나와도 '개인 신체 반응성'과 '개인 신경 표상'을 구분하지 못한다. 위 게이트와 위계 모형, 전역 성분 분리를 넣으면 진행을 권한다. **판정: 수정 후 진행.**

---

## 2. GC-P2 (generative-counterfactual → llm-semantics): 기술 잔차(통계 통제)와 의미 고정 편집(설계 통제)을 같은 voxel에서 맞대기

### 제안 요약
Horikawa에서 정서 배제 캡션 embedding을 통제한 뒤 정서 고유 분산이 남는 voxel(R0, llm-semantics Chain 1, vision-decoding R6)을 찾고, 같은 voxel에서 encoder 예측이 '의미를 고정하고 정서 단서만 바꾼 편집'에 반응하는지(R1, generative-counterfactual CH1)를 본다. 2x2 결과 판정표를 사전등록한다. Kuleshov형 맥락/인물 분리 자극을 만들고 관점을 나눈 신규 인간 평정(R2)을 받는다.

### 판정 7항목

1. **이미 연구되었는가: partially (방법), no (정서 적용).**
   * 검색: WebSearch "counterfactual image editing encoding model fMRI emotion semantic content held constant caption embedding residual voxelwise"(2026-11-12) → MINE(arXiv:2605.16468, DB 수록)과 BrainCause(arXiv:2605.23895, search_index, arXiv API 429로 식별자 경로 미확인). 둘 다 encoding model voxel의 counterfactual 편집 검정이지만 정서도, 캡션 잔차도 다루지 않는다(검색 요약 기준).
   * 정서 쪽 선행: Du 2025(arXiv:2509.24298)는 MLLM과 인간 평정의 뇌 설명력을 비교했지만 정서 배제 기술을 nuisance로 둔 잔차 분석은 없었다(llm-semantics Chain 1 기록). Kuleshov 효과의 fMRI는 Mobbs 2006(doi:10.1093/scan/nsl014)이 있다.
   * 같은 voxel에서 두 통제를 맞댄 정서 연구는 이번 검색에서 미발견.
2. **단순한 모델 적용인가: 아니다.** 통계 통제와 설계 통제의 삼각 검증이라는 방법론적 기여가 있고, 2x2 판정표가 결과 해석을 미리 정한다.
3. **Neuroscience Question을 해결하는가: 부분적으로.** 'Horikawa의 정서 고유 분산이 측정되지 않은 의미의 대리인가'(adversarial-reviewer U1의 잔여 교란 문제)를 직접 겨냥한다. 다만 편집 쪽은 encoder 예측(R1)이라 '뇌가 그렇게 반응한다'가 아니라 '이 데이터로 학습한 encoder가 정서 단서를 쓴다'까지만 말한다(제안자도 결론 수준을 명시).
4. **정서가 아닌 것을 decoding하는가: 두 경로 모두 위험이 있다.**
   * 편집 쪽: 표정, 조명/색, 동작 속도 편집은 휘도, 색, 공간주파수 같은 저수준 통계를 바꾼다. amygdala encoder는 붉은색과 고주파 성분에 반응했다(Jang & Kragel 2025, generative-counterfactual CH2 인용, doi:10.1523/JNEUROSCI.1436-24.2025). '정서 편집 민감도'가 저수준 변화 민감도일 수 있다.
   * 통계 쪽: Horikawa 공개본은 블록 z-score 반응이며 전역 신호 처리 여부가 미확인이다(공통 사실 1). 각성 관련 범주(공포, 놀람)의 '정서 고유 분산'에 전역 자율신경 성분이 섞일 수 있다(공통 사실 2). 이 경우 고유 분산은 캡션으로 설명되지 않는 '신체 상태'이지 '정서 표상'이 아니다.
   * 캡션 쪽(제안자 반론 a): '장례식'처럼 정서 함의가 큰 중립 캡션은 과통제를 만든다.
5. **현재 데이터로 검증 가능한가: 대부분 가능, 일부 조건부.**
   * Horikawa(관찰, 반복 없음)와 Mind captioning(같은 자극, 반복 있음)이 있다. 인간 중립 캡션이 Mind captioning 공개 저장소에 들어 있는지는 미확인(vision-decoding 0.1절). Kuleshov 편집용 Emo-FilM 장면은 영화별 CC 조항 미확인. R2 평정은 새 수집이 필요하다.
   * **signal-feasibility:** "같은 voxel" 비교의 전제는 그 voxel의 encoder가 신뢰할 만하다는 것이다. Horikawa는 TE 43 ms라 vmPFC, OFC, 측두극 voxel에서 신호 손실 가능성이 있고(추론, 미측정), 반복이 없어 voxel 신뢰도를 Horikawa 안에서 정할 수 없다. 피질하 voxel은 판정 불가에 가깝다.
6. **더 강력한 방법이 있는가: 있다.**
   * **voxel 신뢰도를 독립 코호트로 정의:** Mind captioning 72클립 5회 반복으로 parcel, voxel별 신뢰도를 계산해 '비교 가능 voxel' 마스크를 Horikawa와 독립적으로 만든다. 같은 데이터에서 선택하면 순환이다.
   * **voxel 대신 ROI 패턴 수준:** 정서 정보는 분산 패턴일 가능성이 커서(Horikawa 2020 Discussion 2~3째 단락) 단일 voxel 맞대기는 검정력이 낮다. ROI 패턴 encoding이나 RSA 수준을 1차로, voxel 지도는 2차로 둔다.
   * **관찰 뇌로 하는 셋째 다리:** encoding-foundation Chain 4의 controversial selection(캡션 예측과 정서 평정 예측이 크게 갈리는 자연 클립 쌍을 고르고 보류 피험자의 실측 RDM이 어느 쪽을 따르는지)은 편집 없이 실측 뇌로 같은 질문을 검정한다(R0지만 관찰 뇌). 두 다리(잔차, 편집)에 이 다리를 더하면 R1 결과의 외적 검증이 생긴다.
   * 편집 대조: 휘도, 대비, 공간주파수 스펙트럼을 원본과 맞춘 편집과 맞추지 않은 편집을 함께 두어 저수준 경로를 분리한다.
7. **기대와 다른 결과도 의미 있는가: 그렇다.** 2x2 판정표가 네 경우의 해석을 미리 정했고, 편집 무감각을 'feature 공간 맹시'와 구분하려고 feature 변위를 보고하는 점이 좋다. 단 판정표에 '신호 품질 부족으로 판정 불가' 칸을 추가해야 한다(게이트 미통과 voxel).

### 수정안
1. **신호 게이트 추가:** Mind captioning 반복으로 정한 신뢰도 마스크와 Horikawa raw로 계산한 dropout 마스크를 통과한 ROI와 voxel만 비교한다. 판정표에 '판정 불가' 칸을 둔다.
2. **통계 쪽 민감도:** Horikawa raw를 전역 신호 회귀 유무 두 판으로 재전처리하고, 정서 고유 분산이 각성 범주에서만 회귀에 민감한지 보고한다. Mind captioning(이미 회귀본)과의 차이도 이 축으로 설명한다.
3. **분석 수준:** ROI 패턴 encoding과 RSA를 1차, voxel 맞대기를 2차로 둔다.
4. **편집 쪽 저수준 대조:** 저수준 통계 정합 편집과 비정합 편집, 그리고 모든 조건이 같은 생성 파이프라인을 통과하는 null-edit(generative-counterfactual CH2의 방식)를 함께 둔다.
5. **셋째 다리:** controversial selection으로 고른 자연 클립 쌍에서 보류 피험자의 실측 뇌가 어느 쪽을 따르는지를 함께 보고한다(encoding-foundation Chain 4와 결합).
6. Kuleshov 자극은 Emo-FilM 영화별 CC 조항 확인 뒤에만 만들고, R2 평정 지시문은 felt와 attributed를 분리한다(제안대로).

### 종합
정서와 의미의 분리라는 팀 공통 문제(axis_encyclopedia 0.3절)에 가장 직접적인 삼각 검증 설계다. 피질하와 안와전두의 신호 게이트, 전역 성분 민감도, 패턴 수준 분석을 넣으면 신뢰할 만하다. **판정: 수정 후 진행(우선순위 높음).**

---

## 3. EF-P1 (encoding-foundation → generative-counterfactual): 같은 자극에서의 surrogate 충실도 감사를 모든 in-silico 정서 결과의 관문으로

### 제안 요약
TRIBE v2(무음 영상 입력)로 Horikawa 2,181개와 Mind captioning 반복 클립의 run 순서 시퀀스를 예측하고 관찰과 같은 블록 평균을 적용한 뒤, parcel별로 (a) 반응 상관, (b) 34+14 규범 RDM에 대한 관계 충실도, (c) 시각-의미 RDM을 partial로 뺀 정서 고유 RSA를 계산해 'trust map'을 만든다. ceiling은 Mind captioning 5회 반복. 이 지도로 in-silico 편집 결과(R1)를 어느 영역에서 믿을지 정한다.

### 판정 7항목

1. **이미 연구되었는가: partially.**
   * 검색: WebSearch "TRIBE v2 evaluation naturalistic emotion movie fMRI in silico predicted versus observed representational similarity emotion categories"(2026-11-12) → NeurIPS 2026 "Evaluating TRIBE v2 Beyond Its Original Benchmarks: From Functional Localizers to Naturalistic Emotion"(search_index, 본문 미열람). 검색 요약 기준으로 정서 범주마다 모델-뇌 대응이 크게 달랐고 일부 정서 조건에서 선택적 실패가 있었다. RSA나 반복 기반 ceiling을 썼는지는 확인하지 못했다.
   * EmoMind(arXiv:2605.16739)는 TRIBE v2 대체 시 클립 간 정서 RSA가 크게 줄었다고 보고했으나 실측과 대체의 자극이 달랐다(encoding-foundation Chain 1, generative-counterfactual CH3 기록).
   * 같은 자극, 반복 ceiling, 관계 충실도, rank 대역 충실도를 결합한 parcel trust map은 미발견(제안자 검색 + 이번 검색).
2. **단순한 모델 적용인가: 기반 시설에 가깝다.** 감사 자체는 연구 질문이라기보다 다른 질문의 전제 조건이다. 그 가치는 인정하지만, '어떤 정서 구조가 자극으로 계산 가능한가'라는 과학 질문으로 결과를 함께 보고해야 단순 benchmark를 넘는다.
3. **Neuroscience Question을 해결하는가: 부분적으로.** 관찰에서 정서 고유 RSA가 남고 in-silico에서 사라지는 parcel은 '자극 계산 불가 정서 성분'의 후보다. 그러나 그 잔여가 신체 상태인지, 개인 특이 반응인지, 잡음인지 분해하지 않으면 신경과학적 해석으로 이어지지 않는다.
4. **정서가 아닌 것을 decoding하는가: 체계적 위험이 하나 있다.** TRIBE v2는 몸이 없는 자극 구동 모델이다(저자들이 내수용, 체성감각 입력 부재를 한계로 명시, encoding-foundation Chain 2 인용). 관찰 데이터에는 자극에 동기화된 자율신경 전역 성분이 들어 있을 수 있다(공통 사실 2, 3). 그러면 각성 관련 범주에서 '관찰에는 있고 surrogate에는 없는 정서 구조'가 생기는데, 이것은 정서 표상이 아니라 신체 경로다. 반대로 Mind captioning 관찰본은 전역 신호 회귀본이라(공통 사실 1) 이 성분이 빠져 있어, **코호트에 따라 trust map이 달라질 수 있다.**
5. **현재 데이터로 검증 가능한가: 가능.** Horikawa 2,181개, Mind captioning 72x5 반복, Emo-FilM이 있고 사전학습 데이터 겹침이 없다(encoding-foundation 2.2절). 제약: 공개 TRIBE v2 checkpoint는 fsaverage5 피질만 출력하므로 피질하는 판정 불가(제안자도 명시).
   * **signal-feasibility:** Horikawa와 Mind captioning 공개본은 native volume이므로 fsaverage5와 비교하려면 표면 투사가 필요하다. TE 43 ms(Horikawa) 데이터의 안와전두, 측두극 꼭짓점은 투사 후에도 신뢰도가 낮을 수 있다. 관찰 신뢰도가 낮은 parcel에서 충실도가 낮게 나오면 그것은 surrogate 실패가 아니라 관찰 잡음이다. 두 코호트는 TE(43 vs 30 ms)와 MB(4 vs 6)가 달라 parcel별 관찰 신뢰도 지형도 다르다.
6. **더 강력한 방법이 있는가: 있다.**
   * **충실도를 관찰 RDM 신뢰도로 정규화:** Mind captioning 5회 반복으로 parcel별 관찰 RDM의 split-half 신뢰도(RSA noise ceiling)를 구하고, 충실도 = in-silico-관찰 RDM 상관 / 관찰 RDM 신뢰도로 정의한다. 정규화하지 않으면 신호가 약한 parcel이 '낮은 trust'로 잘못 표시된다.
   * **학습된 비교 encoder:** V-JEPA2 feature를 Horikawa로 ridge 학습한 encoder(보류 피험자, 보류 클립)를 같이 감사한다. TRIBE v2만 감사하면 'TRIBE의 실패'와 '자극 계산 가능성의 한계'를 구분할 수 없다.
   * **전역 성분 민감도:** 예측과 관찰 모두에 전역 신호 회귀 유무 두 판을 만들어 충실도를 비교한다.
   * 제안의 rank 대역 충실도는 저rank 대역에 전역 성분이 몰릴 가능성(GI-P7)과 함께 해석한다.
7. **기대와 다른 결과도 의미 있는가: 그렇다, 신호 마스크가 있을 때.** 충실도가 대부분 높으면 '이 데이터의 정서 구조는 자극으로 계산 가능하다'는 중요한 결론이 되고, 특정 parcel에서만 낮으면 후보 영역이 생긴다. 다만 관찰 신뢰도가 낮은 parcel의 낮은 충실도는 해석 불가로 표시해야 한다.

### 수정안
1. **trust map 정의 변경:** 충실도를 관찰 RDM 신뢰도(Mind captioning 반복 split-half)로 정규화하고, parcel별 tSNR, dropout 마스크(코호트별)를 함께 표시한다. 관찰 신뢰도가 기준 미만인 parcel은 '판정 불가'.
2. **두 surrogate:** TRIBE v2(zero-shot)와 Horikawa 학습 encoder(V-JEPA2 ridge)를 함께 감사해 surrogate 특이 실패와 자극 계산 한계를 나눈다.
3. **전역 성분 축:** 관찰과 예측 모두 전역 신호 회귀 유무 두 판으로 계산하고, Horikawa 2020 공개본의 nuisance 항목을 먼저 확인한다(Mind captioning은 12개 전역 신호 회귀본).
4. **Emo-FilM 단계에서 생리 분해:** 시청각 조건 재현 단계(제안 4번)에서는 참가자 생리를 회귀한 관찰과 하지 않은 관찰을 각각 TRIBE 예측과 비교해, 'surrogate가 놓치는 정서 구조' 중 신체 경로 몫을 직접 잰다(SN-P1과 결합).
5. **보고 형식:** trust map을 'R1 결과의 필요조건'으로만 쓰는 제안자 원칙을 유지하고, 과학 결과로는 '자극 계산 가능 정서 구조의 지도'를 따로 보고한다.

### 종합
모든 in-silico 정서 결과의 해석 범위를 정하는 데 꼭 필요한 관문이다. 다만 현재 정의로는 '관찰 잡음'과 '몸 없는 surrogate의 구조적 결핍'이 낮은 trust로 섞인다. 관찰 신뢰도 정규화, 비교 encoder, 전역 성분 축을 넣으면 관문으로서 신뢰할 수 있다. **판정: 수정 후 진행(다른 in-silico 제안보다 먼저 실행 권고).**

---

## 검색 경로 요약

| 제안 | 검색(2026-11-12) | 결과 | 판정 |
|---|---|---|---|
| GI-P5 | WebSearch "intersubject representational similarity analysis individual variation affective experience movie fMRI idiosyncratic brain response predicts self-report"; WebSearch "Spacetop dataset alignvideo individual ratings idiosyncratic brain response residual hyperalignment self-report deviation 2025 2026"; Crossref 서지 검색과 PubMed MCP 전문으로 Chen 2020 확인 | 특성 기반 IS-RSA(Chen 2020), idiosynchrony 개관(Finn 2020). Spacetop 보고 편차 분석 없음 | partially |
| GC-P2 | WebSearch "counterfactual image editing encoding model fMRI emotion semantic content held constant caption embedding residual voxelwise"; arXiv API 확인 시도(429, 우회하지 않음) | MINE, BrainCause(정서 아님). 정서 적용 없음 | partially(방법), no(정서) |
| EF-P1 | WebSearch "TRIBE v2 evaluation naturalistic emotion movie fMRI in silico predicted versus observed representational similarity emotion categories" | NeurIPS 2026 TRIBE v2 정서 평가(search_index), EmoMind | partially |

## 미확인 사항
* Horikawa 2020 공개 전처리본의 nuisance 회귀 항목(전역 신호 포함 여부). KamitaniLab 코드나 원문 Methods로 확인 필요.
* NeurIPS 2026 TRIBE v2 정서 평가의 지표와 데이터(본문 미열람).
* BrainCause(arXiv:2605.23895)의 저자와 본문(arXiv API 429).
* Mind captioning 공개 저장소에 인간 중립 캡션과 생리 파일이 있는지.
