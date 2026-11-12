# Deliverable G: Research Question Landscape

* 작성: Coordinator (Stage 3, P5 조합 생성)
* 기준일: 2026-11-12
* 입력
  * Round 1 Discussion-to-Research chain과 `outputs/future_directions.md`
  * Round 2 제안 76개(`outputs/discussion/proposals_index.csv`)와 응답
  * Round 3 검토(`outputs/discussion/round3_summary.md`)와 adversarial-reviewer 상위 10개 검토(`outputs/agents/adversarial-reviewer/round3_top10_review.md`)
  * Round 4 제안 20개(`outputs/agents/<이름>/round4.md`)
  * 무작위 조합 30개(`outputs/combinations/random_combos.csv`, 시드 20261113)
  * 전략 A~H
* 원자료와 재생성
  * 모든 조합은 `outputs/combinations/build_matrix.py` 안에 데이터로 적혀 있다. 실행하면 `matrix.csv`, `rejected.md`, `matrix_checks.md`를 만들고, 이 문서 4절의 표도 다시 쓴다.
  * 실행: `python3 -I outputs/combinations/build_matrix.py`
  * 1~3절과 5~7절은 Coordinator가 직접 썼다.

---

## 0. 요약

| 항목 | 수 |
|---|---|
| 검토한 조합 | 96개 (문헌 54, 무작위 30, 전략 12) |
| 기각한 조합 | 22개 (문헌 3, 무작위 16, 전략 3). 사유는 `outputs/combinations/rejected.md` |
| Broad Research Directions (유지한 조합) | 74개 |
| Distinct Research Questions | 60개 (문헌 45, 무작위 6, 전략 9) |
| 방향만 유지한 조합 | 14개. 다른 질문과 같거나, 방법 인프라이거나, 신호 가능성이 불확실한 경우 |
| 군집 | 10개 |
| 근거 논문 ID | 119개. 모두 `outputs/literature/literature_db.csv`의 verified 항목이다(스크립트로 점검) |
| overlap 표시 | EmoViS 9개, Emo-FilM 연구 11개, EmoBrain 6개 질문 |
| 선행 판정 | partially 41, no 10, 미확인 9 |

* **질문이 쓰는 데이터셋:** Horikawa 2020 36개, Mind captioning 33개, Emo-FilM 31개, Spacetop 16개, NSD 5개. NSD는 정서 라벨이 없어(Stage 1) 대조나 AI 추정 라벨용으로만 쓴다.
* **Axis 사용 빈도:**
  * 많이 쓰인 Axis: E 29, K 26, A 22, I 21, F 21.
  * 적게 쓰인 Axis: G(Decoding) 2, M 6.
  * Decoding이 적은 이유는 Novelty Constraint 때문이다. "정서 decoding 정확도"류 질문을 걸러 냈다. 이것이 탐색 범위의 공백인지는 Stage 4에서 다시 본다(7절).
* **모든 조합 규칙을 통과했다.**
  * 서로 다른 유형의 Axis를 3개 이상 쓴다.
  * I, J, K, L, R 중 하나 또는 외부 분야를 1개 이상 포함한다.
  * Round 2 제안 76개와 Round 4 제안 20개가 모두 어떤 조합에 매핑되었다.
  * 무작위 30개를 모두 판정했다.
  * 전략 A~H를 모두 적용했다.
  * 점검 결과는 `outputs/combinations/matrix_checks.md`에 있다.

---

## 1. 읽는 법과 공통 주의

1. **증거 수준.** 표기는 axis_encyclopedia.md 0.2절의 R0~R4를 따른다.
   * 대부분의 질문은 관찰 데이터 분석(R0)이다.
   * in-silico 단계가 있는 질문은 R1까지 간다.
   * 데이터셋 안의 실제 조작을 쓰는 질문은 R3-internal 후보다. 해당 질문은 RQ-26과 RQ-33(Mind captioning 테스트 run의 의사 무작위 순서), RQ-10(코호트 간 전향 선택)이다.
   * "판정한다"는 표현은 "어느 해석과 맞는가"로 읽는다(adversarial-reviewer 지적).
2. **라벨 출처.** 질문마다 다음 중 무엇을 쓰는지 matrix.csv의 dataset, note 열에 적었다.
   * 규범 평정(Horikawa, Mind captioning)
   * consensus 평정(Emo-FilM 별도 평정자)
   * 본인 보고(Spacetop, Mind captioning vividness, Emo-FilM 사후 평정)
   * AI 추정
3. **선행 판정.** "partially"가 많다. 검토자들이 원 제안이 놓친 선행을 계속 찾아냈기 때문이다(round3_summary.md 2절, 상위 10개 검토 8절). "no"와 "미확인"은 Stage 4 선행연구 중복 감사에서 다시 확인해야 한다.
4. **overlap.** `reference/existing_projects.md` 기준으로 겹치는 부분을 한 줄로만 표시했다. 겹친다는 이유로 질문을 빼거나 우선하지 않았다.
5. **공통 교란.**
   * 다섯 데이터셋 모두 자유 시청이다. Horikawa 2020도 자유 시청임을 원문으로 확인했다(상위 10개 검토 F1). 그래서 시선 교란이 모든 질문에 걸린다.
   * 공개 TRIBE v2는 피험자 평균 모델이다(F6).
   * Spacetop 본인 평정의 유효 표본은 완료율 0.5 이상 57명, 0.8 이상 40명이다(F4).

---

## 2. 군집 개요

### K1. 정서 신경 공간의 구조와 그 기원 (RQ-01~07)

* **핵심 물음:** 정서 관련 신경 공간은 몇 차원이고, 범주적인가 연속적인가? 그 구조는 어디서 오는가?
* **주 데이터:** Horikawa 2020 + Mind captioning. 같은 2,180개 클립을 본 11명이고, 두 코호트의 제시 순서는 독립이다.
* **세 가지 경쟁 설명.** 셋은 같은 공유 스펙트럼 분석으로 함께 답할 수 있다.
  * RQ-01: 범주 혼합 대 연속 잠재 구조.
  * RQ-07: 범주 수가 신뢰 차원 수보다 많은 sparse superposition.
  * RQ-03: 기하는 자극 집합의 분포를 반영할 뿐이다.
* **같은 공간 위의 파생 질문:**
  * RQ-02: 범주 체계의 IB 효율.
  * RQ-04: 뇌 우선 분류 체계.
  * RQ-06: 국소 대 분산(시너지).
* **RQ-05의 위치:** Spacetop에서 같은 사람의 양식 간 추상화를 본다. 데이터가 달라 독립적으로 수행할 수 있다.
* **선행 조건:** RQ-01의 0단계(원 결과 재현 V11, 정렬과 평가 자극 분리)가 RQ-02, 03, 04, 07의 공통 기반이다.
* **주요 위험:**
  * 자유 시청 시선이 공유 분산과 개인 분산 양쪽에 섞인다.
  * 피험자 쌍이 서로 독립이 아니다.
  * 두 코호트의 획득 조건(TR 2 s 대 1 s), 전처리(전역 신호 12개 회귀)가 다르다.

### K2. 정서 신호와 지각, 의미 내용의 분리 (RQ-08~14)

* **핵심 물음:** "정서 표상"으로 보고된 신호 중 시각, 의미, 상황 내용으로 환원되지 않는 부분이 있는가? 있다면 어느 방법으로 보여야 믿을 수 있는가?
* **질문 구성:**
  * RQ-08: 통계 통제, 기술 잔차.
  * RQ-09: 통계 통제와 설계 통제의 삼각 검증.
  * RQ-10: 전향 자극 선택.
  * RQ-11: 선호 자극 합성.
  * RQ-12: 상황 대 정서 편집.
  * RQ-14: 사건 의미역 구조.
* **관계:**
  * RQ-13(OT 매칭의 positivity 지도)은 이 군집과 K1에서 정서 쌍 대비를 쓰는 모든 질문의 **해석 범위**를 정한다. 매칭률이 낮은 정서 쌍의 결론은 "이 데이터로 식별 불가"로 표시해야 한다.
  * RQ-09는 RQ-08 결과 뒤의 2단계다. 순환을 피하려면 voxel 정의(Mind captioning)와 encoder 학습(Horikawa)을 코호트로 나눈다.
  * RQ-12와 RQ-14는 "정서 범주 대신 무엇이 반응을 설명하는가"라는 같은 물음에 다른 대안(상황, appraisal 구조)을 넣는다. K6의 RQ-34(행동 경향)도 같은 물음이다.
* **주요 위험:**
  * 공변량 측정 오차와 과통제를 맞교환해야 한다.
  * band 차원이 비대칭이다.
  * 편집이 저수준 통계를 바꾼다(Zhan 2026이 직접 증거).
  * EmoViS와 가장 많이 겹친다(9개 중 6개가 이 군집).

### K3. 라벨 출처와 관점 (RQ-15~20)

* **핵심 물음:** 규범, consensus, 본인, AI 라벨은 같은 것을 재는가? 뇌는 어느 출처, 어느 관점(portrayed / perceived / felt)을 따르는가?
* **질문 구성:**
  * RQ-15: AI 라벨의 두 측정(내부 표상 대 출력).
  * RQ-16: 관점 결속.
  * RQ-17: MLLM 평정자의 항목별 대체 가능성.
  * RQ-18: 출처 불변 성분과 출처 고유 성분. Round 4에서 두 에이전트가 독립 수렴했다.
  * RQ-19: rank 대역별 출처 정렬.
  * RQ-20: 데이터셋 간 축 보존.
* **관계:**
  * RQ-17의 항목별 판정이 AI 라벨을 쓰는 다른 질문(RQ-18, 19, 27, 03의 NSD 대조)에서 어떤 항목을 써도 되는지 정한다.
  * RQ-19는 RQ-01의 신뢰 부분공간 위에서 계산한다.
  * RQ-20은 Ke 2025의 "arousal 전이, valence 비전이" 결과를 라벨 출처로 설명하려 한다. K8의 RQ-50은 같은 비대칭을 신경 기하로 설명한다. 두 설명은 경쟁 관계다.
* **기각 기록:** Strategy A의 첫 시도(PPI로 본인 평정 결측 보충)는 상위 10개 검토로 전제가 무너져 기각했다(rejected.md).

### K4. 본인 경험, 개인차, 평정 불일치 (RQ-21~23)

* **핵심 물음:** 본인 보고는 관찰자가 얻을 수 없는 본인 뇌 정보를 반영하는가? 사람마다 다른 보고와 평정자 간 불일치는 무엇에서 오는가?
* **RQ-21(A*):**
  * 다섯 에이전트가 독립 수렴했고 Round 2 점수 1위였다.
  * 상위 10개 검토에서 "사람 수준 기준선 multiverse"가 기각되어 재구성되었다.
  * 0단계 관문(결측-상태 관계, 검정력 시뮬레이션)을 통과해야 본 분석으로 간다.
* **RQ-22:** 평정자 불일치 중 영화 시간에 고정된 성분을 자극 모호성으로 보고, 혼합 정서의 신경 형식을 묻는다.
* **RQ-23:** 연속 경험이 회고 평정으로 압축되는 규칙을 묻는다.
* **방향만 유지:** RND-10(개인별 양식 가중치), RND-17(개인별 정서-시각 feature 지도). 둘 다 RQ-21의 0단계 결과에 달려 있다.
* **주요 위험:** 유효 표본 40~57명, 사람당 영상 24~39개라 개인 수준 검정력이 약하다.

### K5. 시간 역학: 이월, 방향, 흐름, 놀람 (RQ-24~33)

* **핵심 물음:** 정서 상태는 시간 속에서 어떤 구조로 움직이는가? 관성, 방향성, 영화 간에 보존되는 흐름, 놀람과의 결합을 묻는다.
* **같은 분석 파이프라인을 공유하는 묶음:**
  * Emo-FilM 1 Hz 상태열: RQ-24(방향성), RQ-28(흐름의 휴대성), RQ-29(언어 전이 사전확률), RQ-32(arousal = 상태 변화 속도).
  * Mind captioning 의사 무작위 순서: RQ-26(관성, 감쇠)과 RQ-33(맥락에 따른 해석 이동). 같은 HRF 통제와 시각 부분공간 대조를 쓴다.
  * 궤적 곡률: RQ-30(곡률이 깨지는 순간과 놀람)과 RQ-31(정서 영역의 straightening). RQ-31은 무작위 경로, RQ-30은 Round 4에서 따로 나왔다.
  * RQ-25(world model 놀람)와 RQ-30은 모델 기반 놀람 지표와 모델 무관 놀람 지표의 비교가 된다.
* **선행 조건:**
  * RQ-24의 0단계(평정만 쓰는 순 흐름, 결합 빈도로 재정의)가 RQ-24 본 분석과 RQ-29의 전제다.
  * RQ-26의 τ 식별 가능성 시뮬레이션이 RQ-33의 HRF 통제에도 쓰인다.
* **주요 위험:**
  * 1 Hz consensus는 항목마다 다른 평정자 3~4명이 매긴 값이다. 그래서 개인이 경험한 전이가 아니다.
  * 평정자 반응 지연과 HRF 지연이 방향성을 만든다.
  * 사건 경계가 상태 속도와 곡률을 바꾼다.
  * Emo-FilM 연구와 가장 많이 겹친다.

### K6. 행동 경향과 affordance (Axis V) (RQ-34~40)

* **핵심 물음:** 정서의 행동 준비 성분은 정서 범주와 구분되는 신경 구성개념인가? 자극에서 계산할 수 있는가?
* **선행 관문 RQ-39:**
  * 인간, AI, 뇌의 multitrait-multimethod 행렬로 Emo-FilM Motivation 10개 항목이 valence의 재표현이 아닌지 먼저 검증한다.
  * 실패하면 RQ-34, 35, 37, 40은 이 데이터로 답할 수 없다.
  * RQ-36(null space)과 RQ-38(행동 조건 예측기)은 Motivation 항목에 덜 의존해 일부 진행할 수 있다.
* **동기 정정:**
  * 이 군집의 출발점이었던 "Horikawa 2020의 (or affordances)" 해석은 오독이었다(상위 10개 검토 F2). 원문의 affordance는 "장면이 특정 정서를 일으킬 것이라는 추론"이다.
  * 동기는 Frijda, component process model, Thornton & Tamir 2024로 다시 세운다.
  * Horikawa의 정서 affordance 질문은 K3(Axis U) 쪽에 속한다.
* **주요 위험:**
  * 행동 경향 라벨이 Emo-FilM에만 있다. 다른 데이터셋으로 확장하려면 AI 라벨을 써야 해 순환적이다.
  * latent action은 카메라 움직임을 잡는다.

### K7. 기억, 회상, 내성 (Axis W) (RQ-41~47)

* **핵심 물음:** 회상된 정서는 원 자극의 흔적인가 재구성인가? 회상에 대한 내성 보고(vividness)는 무엇을 반영하는가?
* **같은 파이프라인:** 모든 질문이 Mind captioning(6명)의 지각에서 회상으로의 decoder를 공유한다.
  * RQ-41이 기본 분석이다(정서 부분공간 재활성과 vividness).
  * RQ-43(내성 대 기억성)과 RQ-41은 vividness의 출처를 함께 분해한다.
  * RQ-44(생성적 재구성)는 Round 4에서 두 에이전트가 독립 수렴했다. 회상 패턴을 원 클립, 캡션, cue 생성 영상 예측으로 나누는데, 같은 정서 배제 캡션을 K2의 RQ-08과 공유한다.
  * RQ-45(언어 병목)와 RQ-46(집단 전달 편향)은 클립 수준 예측 변수를 비교하는 같은 회귀로 답할 수 있다.
  * RQ-42(우선순위 재생)와 RQ-47(학습 목표별 표상 이동)은 회상 강도와 회상 형식을 설명하는 서로 다른 축이다.
* **주요 위험:**
  * 6명이라 개인차 질문은 모두 기각했다.
  * vividness는 3~4점에 몰리고, 재시청 후 회고 평정이다.
  * cue 텍스트가 정서를 함축한다.
  * 반복 노출이 최대 11회다.

### K8. 몸, 생리, 피질하 경로 (RQ-48~50)

* **핵심 물음:** 자극 구동 모델이 limbic 영역에서 놓치는 분산은 몸 신호인가? 피질하 경로는 3T 자연 자극에서 볼 수 있는가?
* **질문 구성:**
  * RQ-48: Emo-FilM 생리로 limbic 맹점을 4원 분할한다.
  * RQ-50: arousal은 저rank 전역 모드에, valence는 고rank 개인 성분에 있는지 묻는다.
  * RQ-49: 상구-pulvinar-amygdala 경로. 데이터 내장 양성, 음성 대조 관문을 먼저 통과해야 한다.
* **관계:**
  * RQ-48과 RQ-50은 전역 자율신경 성분 분해를 공유한다.
  * RQ-50은 K5의 RQ-32(arousal = 속도)와 arousal의 두 정의로 경쟁한다.
* **이견:** 생리를 매개로 볼지 교란으로 볼지 이견이 남아 있다(discussion_record.md).

### K9. In-silico 뇌와 AI 모델의 정서 충실도 (RQ-51~56)

* **핵심 물음:** in-silico 뇌와 AI 모델은 정서 구조를 얼마나, 어디서 재현하는가? 그 차이는 학습 목표나 정렬 방식으로 설명되는가?
* **선행 관문 RQ-51:**
  * 이 군집과 다른 군집의 in-silico 단계 전부의 관문이다.
  * 해당 질문: RQ-09, 11, 12의 편집 쪽, RQ-25, 31, 33의 in-silico 재현, RQ-48, RQ-52, RQ-56.
  * RQ-51은 실측 대비 정서 충실도가 백본 대비 어느 parcel에서 떨어지는지 정한다. 그 parcel 밖에서는 in-silico 결과를 해석하지 않는다.
* **질문 구성:**
  * RQ-52: in-silico 무음 대 관찰 무음.
  * RQ-53: 저정서 정렬이 정서 기하를 운반하는가.
  * RQ-54: EmoSet 학습 모델의 창발 정서 unit.
  * RQ-55: 학습 목표만 바꾼 통제 비교.
  * RQ-56: brain-tuning의 기능적 가치.
* **주요 위험:**
  * EmoNet은 Cowen & Keltner 프레임으로 학습되어 Horikawa에 쓰면 leakage다.
  * 사전학습 데이터가 오염되었을 수 있다.
  * 구조와 데이터가 정확히 같은 공개 checkpoint 조합이 없을 수 있다.
  * EmoBrain과 겹친다(V-JEPA2, distillation).

### K10. 소리, 언어, 서사 (RQ-57~60)

* **핵심 물음:** 영화 정서에서 대사, 서사 예측, 양식 상충, 암시된 소리는 각각 무엇을 운반하는가?
* **질문 구성:**
  * RQ-57: 대사의 어휘 대 정신 상태 추론.
  * RQ-58: 서사의 단기 대 장기 예측오차.
  * RQ-59: 양식 상충과 평정 불일치. K4 RQ-22의 시간 고정 불일치 성분을 쓴다.
  * RQ-60: 무음 클립의 암시된 소리. Horikawa와 Mind captioning이 무음이라는 제약을 질문으로 바꾼 것이다.
* **방향만 유지:** LIT-21(시간 척도 위계와 양식). 소리 유무와 자극 길이가 데이터셋 간에 함께 바뀌어 독립 질문으로 두기 어렵다.

---

## 3. 군집 사이의 관계

### 3.1 선행 조건 (관문 연구)

| 관문 | 내용 | 결과에 따라 진행 여부가 달라지는 질문 |
|---|---|---|
| RQ-01 0단계 | Horikawa, Westlin 원 결과 재현(V11), 두 코호트 재전처리, 신뢰 공유 부분공간 | RQ-02, 03, 04, 07, 19, 55 |
| RQ-08 0단계 | Horikawa의 정서 대 의미 모형 비교 재현, 캡션 확보, 기술 잔차 voxel | RQ-09, 55, (RQ-44의 캡션 예측) |
| RQ-13 | 정서 쌍별 positivity 지도 | K1, K2에서 정서 쌍 대비를 쓰는 모든 질문의 해석 범위 |
| RQ-17 | MLLM 평정의 항목별 대체 가능성 | AI 라벨을 쓰는 RQ-18, 19, 27, 03(NSD 대조) |
| RQ-21 0단계 | Spacetop 결측-상태 관계, 검정력 시뮬레이션 | RQ-21 본 분석, RND-10, RND-17, (RQ-16, RQ-05의 표본 판단) |
| RQ-24 0단계 | 평정만 쓰는 π 가중 순 흐름과 엔트로피 생산 | RQ-24 본 분석, RQ-29 |
| RQ-39 | Axis V 측정 타당성(MTMM) | RQ-34, 35, 37, 40 |
| RQ-49 관문 | 피질하 신호 가능성(내장 대조) | RQ-49 본 분석, RND-01 |
| RQ-51 | in-silico 정서 충실도 지도 | RQ-09, 11, 12, 25, 31, 33, 48, 52, 56의 in-silico 단계 |

이 관문들은 대부분 저비용이다. 평정만 쓰거나, 기존 결과를 재현하거나, 시뮬레이션이다. Stage 4에서 우선순위를 매길 때 "관문 먼저" 원칙을 제안한다.

### 3.2 같은 분석으로 함께 답할 수 있는 질문

| 공유 자원 | 질문 |
|---|---|
| Horikawa + Mind captioning 재전처리, 공유 스펙트럼 | RQ-01, 02, 03, 07, 19 (+ RQ-08, 10과 전처리 공유) |
| Mind captioning 의사 무작위 순서 | RQ-26, RQ-33 |
| Mind captioning 지각에서 회상으로의 decoder | RQ-41~47 |
| 정서 배제 인간 캡션 | RQ-08, 09, 44 |
| Emo-FilM 1 Hz 상태열 | RQ-22, 24, 28, 29, 32, 59 |
| Emo-FilM 생리 분해 | RQ-32(EDA), 48, 50 |
| Emo-FilM Motivation 평정 | RQ-34, 35, 37, 39, 40 |
| 궤적 곡률 계산 | RQ-30, 31 |
| Spacetop 같은 참가자 다과제 | RQ-05, 16, 21 |

### 3.3 서로 경쟁하는 설명 (같은 현상, 다른 군집)

| 현상 | 경쟁하는 질문 |
|---|---|
| Horikawa와 Westlin 결과의 불일치 | RQ-01(범주 대 연속), RQ-07(superposition), RQ-03(자극 분포) |
| 정서 범주로 설명되는 신경 분산의 정체 | RQ-34(행동 경향), RQ-14(appraisal 의미역), RQ-12(상황), RQ-08(언어 기술) |
| arousal 판독의 일반성 | RQ-50(저rank 전역 모드), RQ-32(상태 변화 속도), RQ-20(라벨 출처) |
| 정서적 놀람 | RQ-25(world model 예측오차), RQ-30(모델 무관 곡률), RQ-58(서사 예측오차) |
| 회상된 정서의 형식 | RQ-44(생성적 재구성), RQ-41(흔적 재활성), RQ-45(언어 병목), RQ-47(학습 목표별 이동) |
| limbic 영역의 encoder 실패 | RQ-48(몸, 평가), RQ-51(모델 결함) |

### 3.4 군집을 가로지르는 축: Introspective Access

내성 보고를 다루는 질문이 세 군집에 흩어져 있다.

* RQ-21(K4): 본인 정서 평정.
* RQ-43, RQ-41(K7): 회상 vividness.
* RQ-15(K3): 기계의 1차 상태 대 보고.

셋 다 "보고는 보고자의 내부 상태에 대한 특권적 정보를 담는가"를 서로 다른 보고자와 대상으로 묻는다. 이론 연결(Stage 4 이후)에서 하나의 묶음으로 다룰 수 있다. 다만 adversarial-reviewer의 지적이 있다. "privileged access" 해석은 RQ-21에서 기준선 구조 때문에 약해졌다. 그래서 이 축의 질문들은 "보고와 뇌의 관계가 자극과 평균 관찰자로 설명되지 않는가"라는 약한 형태로 쓴다.

---

## 4. 질문 목록 (군집별)

표는 `build_matrix.py`가 matrix.csv의 kept 조합에서 생성한다.

* 경로: literature는 Round 2~4 제안, random은 무작위 조합, strategy는 전략 A~H에서 왔다.
* 상세 열(구성 개념, 가져온 개념, AI 모델, 신경 표적, 분석과 예측, 기여, note)은 matrix.csv에 있다.

<!-- RQ_TABLE_START -->

### K1. 정서 신경 공간의 구조와 그 기원 (질문 7개)

| RQ | 연구 질문 | Axis 조합 | 경로 (조합 ID, 출처) | 근거 논문 ID | 가능한 데이터셋 | 선행 판정 | overlap |
|---|---|---|---|---|---|---|---|
| RQ-01 | Horikawa 2020의 '범주형 정서 표상' 결론은, 같은 2,180개 클립을 본 두 독립 코호트(Horikawa 2020 5명, Mind captioning 6명)에서 피험자 간에 재현되는 신뢰 rank 대역으로 한정해도 유지되는가, 아니면 Westlin 2025가 보고한 저차원 연속 구조로 수렴하는가? | A+O+K+Q+T (+외부: Complex Systems (scale-free 공분산 스펙트럼)) | literature (LIT-01; GI-P1, ET-P1, ET-P4, SN-P7, VD-P2; Round 3 GI-P1 검토; 상위 10개 검토(GI-P1, ET-P4)) | 10.1016/j.isci.2020.101060; arXiv:2507.00320; arXiv:2409.06843; arXiv:2505.12653; 10.1126/sciadv.adw1464 | Horikawa 2020 + Mind captioning(같은 자극 11명, MC 반복으로 신뢰도) | partially: EmoMind(arXiv:2605.16739)가 두 코호트를 결합했으나 공유 스펙트럼 비교는 없음(Round 3 검토, adversarial-reviewer 상위 10개 검토) | overlap: EmoBrain(구 EmoViS 범위 포함): Horikawa 2020 정서 기하와 같은 데이터, 대상, 34차원 정서 profile 사용 |
| RQ-02 | 두 코호트의 공유 신경 정서 공간 위에서, 기존 정서 범주 체계(27/34 범주)는 같은 수의 무작위 분할이나 신경 공간 군집보다 Information Bottleneck 효율 경계에 더 가까운가, 각 범주는 신경 공간에서 볼록한 영역을 이루는가? | K+A+C+U+O (+외부: Information-theoretic Neuroscience (Information Bottleneck)) | literature (LIT-18; GI-P6, LS-P6) | 10.1073/pnas.1800521115; 10.1126/science.aaw8160; 10.1126/sciadv.adw1464; 10.1038/s41598-025-14961-6 | Horikawa 2020+Mind captioning | 미확인: Round 2 제안에서 직접 선행 없음으로 보고, Stage 4에서 재확인 | 없음 |
| RQ-03 | 정서 신경 기하는 자극 집합의 구조를 반영하는가: 같은 2,180개 클립에서 시각 다양성과 정서 다양성을 따로 줄인 부분집합을 만들면, 영역별 공유 신경 스펙트럼의 감쇠 지수는 어느 쪽 다양성을 따라 바뀌는가? | B+K+E+Q (+외부: Complex Systems (power-law 스펙트럼 이론, Stringer 2019)) | literature (LIT-36; GI-R4-1) | 10.1038/s41586-019-1346-5; arXiv:2409.06843; arXiv:2505.12653; 10.1126/sciadv.adw1464; 10.1016/j.isci.2020.101060 | Horikawa 2020+Mind captioning(주), NSD(정서 범위가 좁은 시각 대조, 정서는 AI 추정 표기) | no(geometry-info Round 4 검색, 2026-11-12) | overlap: EmoBrain(구 EmoViS 범위): Horikawa 정서 기하의 sensory-semantic 기원과 직접 겹침 |
| RQ-04 | 라벨 없이 뇌에서 찾은 신뢰 공유 성분을 먼저 정하고, 각 성분을 가장 강하게 구동하는 자연 클립(또는 생성 자극)을 사람과 MLLM에게 이름 붙이게 하면, 그 이름 체계는 Cowen & Keltner의 27/34 범주와 어떻게 다른가? | A+K+L+C+T | strategy (STR-B1; Strategy B(Methodological Inversion): 라벨에서 뇌로 가는 decoding을 뇌에서 자극, 이름으로 뒤집기) | 10.1038/s41562-023-01783-7; arXiv:2512.00557; arXiv:2409.06843; 10.1073/pnas.1702247114 | Horikawa 2020+Mind captioning(선택), 명명은 새 평정 | partially: 구동/억제 선택은 언어망에서 수행(Tuckute 2024), 정서 성분에는 미확인 | 없음 |
| RQ-05 | 같은 참가자가 텍스트로 읽은 이야기, 오디오로 들은 이야기, 영상에서 느낀 정서의 좋음-나쁨은 같은 추상 부호(교차 조건 일반화)를 쓰는가, 공유되는 영역과 양식 특이 영역은 어디인가? | A+E+M+K+S | strategy (STR-C1; Strategy C(Representation Comparison): Shared vs Modality-specific) | 10.1016/j.cell.2020.09.031; 10.1523/JNEUROSCI.1676-14.2014; 10.1162/imag_a_00517 | Spacetop(같은 참가자의 narratives 텍스트/오디오, alignvideo) | partially: 지각과 추론 정서의 공통 부호(Skerry & Saxe 2014) | 없음 |
| RQ-06 | 정서 범주 정보는 amygdala와 피질 영역 사이에 중복으로 실리는가 시너지로만 나타나는가, 그 비율은 시각 범주 정보와 다른가? | A+E+K+T (+외부: Information-theoretic Neuroscience (partial information decomposition)) | strategy (STR-D1; Strategy D(Scale Bridging): 국소 활성에서 분산 시스템으로) | 10.1038/s41593-022-01070-0; 10.1016/j.isci.2020.101060; 10.1126/sciadv.adw1464 | Horikawa 2020+Mind captioning, Emo-FilM(보조) | 미확인: Stage 4에서 확인 | 없음 |
| RQ-07 | 뇌의 정서 표상은 신뢰 차원 수보다 많은 정서 범주를 sparse superposition으로 담는가: 드물게 나타나는 정서 범주일수록 전용 차원 없이 중첩되고, 흔한 범주일수록 전용 차원을 갖는가? | A+K+R+Q+F | strategy (STR-H2; Strategy H(Reverse Inspiration, AI -> 뇌): mechanistic interpretability의 superposition) | arXiv:2209.10652; arXiv:2502.12892; 10.1016/j.isci.2020.101060; arXiv:2507.00320 | Horikawa 2020+Mind captioning | 미확인: Stage 4에서 확인 | overlap: EmoBrain(구 EmoViS 범위): Horikawa 정서 기하 대상 겹침(방법은 다름) |

### K2. 정서 신호와 지각, 의미 내용의 분리 (질문 7개)

| RQ | 연구 질문 | Axis 조합 | 경로 (조합 ID, 출처) | 근거 논문 ID | 가능한 데이터셋 | 선행 판정 | overlap |
|---|---|---|---|---|---|---|---|
| RQ-08 | 사람이 정서 단어 없이 쓴 장면 기술 20개의 의미를 측정 오차까지 보정해 통제한 뒤에도, 규범 정서 평정이 고유하게 설명하는 뇌 반응이 남는가, 남는다면 어느 영역인가? | C+F+H+U+I | literature (LIT-03; LS-P1, VD-P3; Round 3 LS-P1 검토) | 10.1126/sciadv.adw1464; 10.1038/s42256-025-01072-0; arXiv:2509.24298; 10.1371/journal.pone.0152719; 10.1016/j.isci.2020.101060; 10.1038/s41467-024-49073-8 | Mind captioning(정서 배제 인간 캡션 20개/클립, 주), Horikawa 2020(재현) | partially: Horikawa 2020의 73개 의미 항목 비교, Abdel-Ghaffar 2024(의미-정서 공동 tuning, 상위 10개 검토가 찾음), Du 2025 | overlap: EmoBrain(구 EmoViS 범위): 정서 기하의 sensory-semantic 기원 분석과 직접 겹침 |
| RQ-09 | 통계 통제(기술 잔차)와 설계 통제(의미 고정 편집, 자연 클립 controversial 쌍)는 같은 voxel에서 같은 결론을 내는가, 불일치한다면 그 패턴이 어느 가정(공변량 완전성, 편집의 의미 누출)이 깨졌는지 알려 주는가? | C+L+P+F+U | literature (LIT-04; GC-P2, GC-P3, FA-P2; Round 3 GC-P2 검토) | 10.1371/journal.pone.0152719; 10.1073/pnas.1912334117; arXiv:2610.13558; arXiv:2512.00557; 10.1126/sciadv.adw1464 | Horikawa 2020+Mind captioning(통계 쪽, 자연 쌍), 편집 자극은 encoder 예측만(R1) | partially(제안자 인식보다 넓게): Zhan 2026(arXiv:2610.13558)이 TRIBE v2로 정서 편집 400쌍을 분석해 편집기 표상이 정서 영역보다 시각 영역 예측과 더 대응한다고 보고(R1 팔의 부분 선행, adversarial-reviewer 상위 10개 검토). Cao 2024, Mobbs 2006 | overlap: EmoBrain(구 EmoViS 범위): 정서 vs sensory-semantic 내용 분리 겹침 |
| RQ-10 | Horikawa 2020 5명으로 학습한 정서 encoder가 '이 영역을 가장 강하게 구동할 것'으로 미리 고른 클립은, 선택을 기록한 뒤 Mind captioning 새 피험자 6명에서도 그 영역을 구동하는가, 시각-의미 encoder의 선택보다 더 잘 맞는가? | A+F+H+R+P+S | literature (LIT-30; EF-P6, FA-P2) | 10.1073/pnas.1912334117; 10.1038/s41562-023-01783-7; 10.1126/sciadv.adw1464; 10.1016/j.isci.2020.101060; arXiv:2604.07729 | Horikawa 2020(선택) -> Mind captioning(검증, 같은 클립 풀) | partially: 언어망 구동/억제 선택(Tuckute 2024) | overlap: EmoBrain(구 EmoViS 범위): 정서 대 시각-의미 모델 비교 겹침 |
| RQ-11 | 정서 유발 영상으로 학습한 amygdala encoder가 가장 선호하는 합성 자극은 얼굴, 표정 같은 의미 범주로 환원되는가, 그리고 FFA, EBA, PPA 예측을 고정한 제약 아래에서도 amygdala 예측을 움직이는 편집이 남는가? | L+G+E+H+B | literature (LIT-31; GC-P7; 무작위 RND-03 수렴) | arXiv:2512.00557; 10.1523/JNEUROSCI.1436-24.2025; 10.1038/s41562-023-01783-7 | Horikawa 2020(encoder 학습), NSD(정지 이미지 encoder 비교) | partially: NeuroVolve에서 amygdala 최대화 = 표정 얼굴 | 없음 |
| RQ-12 | 자연 영상에서 공선적인 '상황'과 '정서'를 편집으로 떼어 놓으면(같은 상황 다른 정서, 다른 상황 같은 정서), 영역별 표상 유사도는 상황 유사도와 정서 유사도 중 어느 쪽을 따르는가? | C+L+I+E+P | literature (LIT-32; GC-P6) | arXiv:2604.13466; 10.1093/scan/nsl014; 10.1371/journal.pone.0308295; arXiv:2512.00557 | Horikawa 2020, Emo-FilM(자연 쌍 R0), 편집 쌍은 encoder 예측(R1) | partially: 모델 쪽 판별 검정(Peiris 2026), Kuleshov fMRI(Mobbs 2006, Cao 2024) | overlap: EmoBrain(구 EmoViS 범위): 정서 vs 의미 분리 겹침 |
| RQ-13 | 자연 클립 라이브러리에서 정서와 시각, 의미 내용은 어느 정서 쌍에서 분리 가능한가: unbalanced optimal transport로 내용이 맞는 클립만 짝지을 때 짝을 못 찾는 비율은 정서 쌍마다 얼마이고, 짝지은 쌍에서도 transmodal 영역의 정서 차이가 남는가? | K+P+B+E (+외부: 계량경제학의 OT 인과 매칭) | literature (LIT-37; GI-R4-2) | arXiv:2112.04398; arXiv:2503.07811; 10.1371/journal.pone.0152719; 10.1073/pnas.1912334117 | Horikawa 2020+Mind captioning(주), Emo-FilM(장면 창, MLLM 캡션은 AI 생성 표기), NSD(AI 추정 정서 대조) | no(geometry-info Round 4 검색) | overlap: EmoBrain(구 EmoViS 범위): 정서 기하와 sensory-semantic 내용의 분리 문제 겹침 |
| RQ-14 | 영화 장면에서 '누가 누구에게 무엇을 했는가'를 추출하는 video semantic role labeling 표상은, 물체와 장면 범주 표상보다 Emo-FilM의 행위 주체, 원인 appraisal 평정과 정서 관련 영역(TPJ, vmPFC, amygdala) 반응을 더 고유하게 설명하는가? | C+A+I+E+P (+외부: Situation Recognition in Computer Vision) | strategy (STR-A3; Strategy A(Technology Transfer): Computer Vision의 situation recognition(visual semantic role labeling)) | 10.1109/cvpr.2016.597; 10.1109/cvpr46437.2021.00554; 10.1038/s41467-024-44870-7; 10.1016/j.neubiorev.2022.104977; 10.1038/s41597-025-04803-5 | Emo-FilM(Agent appraisal 1 Hz, 주), Horikawa 2020(정적 장면 판본) | 미확인: Stage 4에서 확인 | overlap: EmoBrain(구 EmoViS 범위): 정서 대 의미 내용 분리 겹침 |

방향만 유지한 조합: RND-03(amygdala encoding의 해석 가능한 feature 귀속)

### K3. 라벨 출처와 관점 (질문 6개)

| RQ | 연구 질문 | Axis 조합 | 경로 (조합 ID, 출처) | 근거 논문 ID | 가능한 데이터셋 | 선행 판정 | overlap |
|---|---|---|---|---|---|---|---|
| RQ-15 | 같은 공개 VLM에서 답하기 전 hidden state를 정서 방향에 투영한 값(내부 표상)과 모델이 내놓은 정서 평정(출력) 중 무엇이 사람 뇌의 정서 관련 분산을 더 고유하게 설명하는가? | R+U+C+F+Q | literature (LIT-13; FA-P6, FA-P5(일부), GC-P9(일부); Round 3 FA-P6 검토) | arXiv:2604.07729; arXiv:2509.24298; arXiv:2609.34742; 10.1073/pnas.1619316114; arXiv:2408.13718 | Horikawa 2020+Mind captioning | partially: Du 2025(출력 기반 embedding과 뇌) | 없음 |
| RQ-16 | 뇌의 정서 표상은 '누구의 정서인가'를 결속하는가: 같은 참가자의 자기 경험 과제에서 학습한 정서 축이 인물 정서 귀속 과제와 표정 지각 과제로 일반화되는 정도는 영역마다 다른가, 관점 무차별적인 LLM 정서 표상과 비교하면 어떤가? | U+A+R+F+S | literature (LIT-14; ET-P3, ET-P7, LS-P4, FA-P5) | arXiv:2604.07729; 10.1162/imag_a_00517; 10.1523/JNEUROSCI.1676-14.2014; arXiv:2408.13718 | Spacetop(alignvideo 본인 경험, shortvideo 인물 귀속, faces 표정 지각; 같은 참가자) | partially: Skerry & Saxe 2014(지각 vs 추론 정서 공통 부호) | 없음 |
| RQ-17 | MLLM을 '관찰자로서 상황 판단' 모드와 '시청자로서 느낄 정서 보고' 모드로 돌렸을 때, Emo-FilM 50개 항목 중 어느 항목에서 인간 평정자를 대체할 수 있고, 대체 불가 항목은 뇌 encoding 지도에서 어디서 인간 라벨과 갈라지는가? | U+Q+C+I+F (+외부: Statistics of Surrogate Labels (alt-test)) | literature (LIT-15; LS-P5) | arXiv:2501.10970; arXiv:2408.13718; arXiv:2503.16883; 10.1038/s41598-025-14961-6 | Emo-FilM(평정자별 1 Hz 원자료) | partially: 행동 수준 MLLM 평정 타당도(Ruder 2025, Tak & Gratch 2024) | 없음 |
| RQ-18 | 평정자, 참가자 본인, MLLM(관찰자, 경험자) 같은 라벨 출처를 서로 다른 'view'로 두고 식별 가능한 multi-view 학습으로 출처 불변 정서 성분과 출처 고유 성분을 분리하면, 뇌 반응은 어느 성분을 따르고 출처 고유 성분은 어디에 지도화되는가? | U+J+A+F | literature (LIT-46; ET-R4-3, FA-R4-3(두 에이전트 독립 수렴)) | arXiv:2106.04619; arXiv:2303.09166; arXiv:2509.24298; 10.1162/imag.a.134; arXiv:2501.10970 | Emo-FilM(주), Spacetop(본인 view), Horikawa 2020(축소판) | partially: Du 2025, Santavirta 2025가 인간과 AI 평정의 공유를 보고. 출처 고유 성분의 뇌 지도는 없음 | 없음 |
| RQ-19 | 뇌의 개인 간 공유 정서 스펙트럼에서 인간 규범 평정의 정서 기하와 AI 추정 평정의 정서 기하는 각각 어느 rank 대역과 맞는가: AI 기하는 상위 공유 대역에만 맞고 하위 대역에서 인간보다 먼저 무너지는가? | C+F+I+K+U | random (RND-09; random_combos.csv) | arXiv:2409.06843; arXiv:2509.24298; 10.1038/s41598-025-14961-6; arXiv:2408.13718 | Horikawa 2020+Mind captioning | 미확인: Du 2025는 전체 RSA만 보고(Stage 4에서 확인) | 없음 |
| RQ-20 | Horikawa 규범 평정으로 정의한 정서 축을 자극 기반 encoder를 다리로 삼아 Emo-FilM consensus와 Spacetop 본인 보고로 옮기면 어느 축이 살아남는가, 실패는 자극 차이보다 라벨 출처 차이로 더 잘 설명되는가? | A+U+F+S+K | strategy (STR-F1; Strategy F(Cross-Dataset Discovery): 규범 라벨 공간에서 본인 보고 공간으로) | 10.1016/j.isci.2020.101060; arXiv:2605.04326; 10.1371/journal.pcbi.1012994; 10.1038/s41597-025-04803-5 | Horikawa 2020(규범), Emo-FilM(consensus), Spacetop(본인) | partially: Ke 2025(arousal 전이, valence 비전이) | 없음 |

방향만 유지한 조합: LIT-48(학습 목표(base, SFT, 선호 최적화)가 기계 평정자의 관점을 정하는가); RND-05(뇌에서 LLM 내부 정서 공간으로의 decoding)

### K4. 본인 경험, 개인차, 평정 불일치 (질문 3개)

| RQ | 연구 질문 | Axis 조합 | 경로 (조합 ID, 출처) | 근거 논문 ID | 가능한 데이터셋 | 선행 판정 | overlap |
|---|---|---|---|---|---|---|---|
| RQ-21 | 같은 영상을 본 Spacetop 참가자(유효 40~57명)에서, 영상 효과와 사람 평균을 함께 제거한 뒤 남는 개인 뇌 반응 편차(vmPFC, insula)는 척도 사용 성분을 분리한 본인 정서 평정의 잠재 편차를 예측하는가, 그 관계는 신체 반응성(전역 성분)을 제거해도 남는가? | A+O+H+U+Q+I | literature (LIT-02; GI-P5, ET-P2, EF-P3, LS-P2, GC-P9; Round 3 GI-P5 검토) | 10.1038/ncomms14211; 10.1016/j.bandc.2024.106260; 10.1126/sciadv.abf7129; 10.1016/j.neuroimage.2020.116851; 10.7554/eLife.62461; 10.1038/s41597-025-05154-x | Spacetop alignvideo(주), Emo-FilM 사후 평정, Horikawa 2020+Mind captioning(보조) | partially: Woo 2017(SIIPS1, 자극 너머 통증 보고를 예측하는 뇌 신호), Li 2025(공유 대 개인 특이 경험), Chen 2020, Chang 2021(자기보고는 fMRI 참가자가 아닌 독립 표본). 같은 사람의 본인 보고로 정서 영상에서 검정한 것은 새로움 | 없음 |
| RQ-22 | Emo-FilM 평정자 불일치가 영화 시간에 고정되어 커지는 순간(자극 모호성)에 신경 패턴은 두 정서 패턴의 선형 중첩인가 별도의 혼합 상태인가, 원인 귀속(사람 탓 vs 우연)이 불확실한 순간에는 분노와 슬픔 패턴의 분리도가 줄어드는가? | A+Q+D+E+K (+외부: Computational Psychiatry (정서를 계산으로 보는 관점)) | literature (LIT-19; MD-P7, ET-P5; 무작위 RND-16 수렴) | 10.1093/cercor/bhae122; 10.1073/pnas.1702247114; 10.1016/j.neubiorev.2022.104977; 10.1038/s41597-025-04803-5 | Emo-FilM(평정자별 원자료, Agent appraisal) | partially: Vaccaro 2024(혼합 정서 fMRI) | 없음 |
| RQ-23 | 영화 한 편의 연속 정서 경험은 어떤 규칙으로 회고 평정에 압축되는가(정점, 끝, 평균, 끝 시점 momentum), 그리고 그 규칙은 영화 끝의 느린 뇌 상태로 더 잘 예측되는가? | D+A+N+U+O (+외부: Reinforcement Learning / Computational Value (mood as momentum)) | literature (LIT-20; MD-P8) | 10.1037/0022-3514.65.1.45; 10.1016/j.tics.2015.07.010; 10.1126/sciadv.abf7129 | Emo-FilM(consensus + 참가자 사후 평정), Spacetop alignvideo(본인 사후 평정) | partially: 행동 수준 peak-end(Fredrickson & Kahneman 1993) | 없음 |

방향만 유지한 조합: RND-10(개인별 양식 가중치의 영화 간 안정성); RND-16(원인 귀속 계산과 정서 패턴 분리도); RND-17(개인별 정서-시각 feature 가중치 지도)

### K5. 시간 역학: 이월, 방향, 흐름, 놀람 (질문 10개)

| RQ | 연구 질문 | Axis 조합 | 경로 (조합 ID, 출처) | 근거 논문 ID | 가능한 데이터셋 | 선행 판정 | overlap |
|---|---|---|---|---|---|---|---|
| RQ-24 | 정서 지도는 방향을 갖는가: Emo-FilM 정서 상태 흐름에 점유율로 설명되지 않는 순 흐름(비가역성)이 있는가, 그리고 뇌 패턴은 과거 정서보다 미래 정서를 더 잘 예측하는가(시간 지연 전향/후향 예측, 같은 상태 수의 장면 내용 상태 경쟁 모형 통제 후)? | D+N+K+E+T (+외부: Reinforcement Learning (successor representation), Complex Systems (비가역성)) | literature (LIT-06; BI-P1, GI-P2; Round 3 BI-P1 검토) | 10.1038/s41467-025-68240-z; 10.1073/pnas.2109889118; 10.1038/nn.4650; 10.1073/pnas.1616056114; 10.1523/JNEUROSCI.1431-18.2018 | Emo-FilM(1 Hz 50항목 consensus, 30명) | partially: Li 2024(휴지기 SR), Ekman 2023(시각 순서 방향성 SR)(Round 3 검토) | overlap: Emo-FilM 연구: Emo-FilM 시간 정보 분석과 부분 겹침 |
| RQ-25 | 영화 속 정서적 놀람은 어느 수준의 예측 실패에 묶이는가: video world model의 예측오차와 예측 불확실성이 TRIBE v2 예측을 통제한 뒤에도 Suddenly(오차형)와 Predictable, Urgency(불확실성형) appraisal 및 amygdala, insula 반응을 서로 다르게 설명하는가? | D+N+I+J+E (+외부: Active Perception (active inference)) | literature (LIT-09; FA-P3, EF-P5, MD-P5, BI-P5; Round 3 FA-P3 검토) | arXiv:2506.09985; arXiv:2502.11831; arXiv:2407.02474; 10.7554/eLife.107955; arXiv:2605.04326 | Emo-FilM(첫 시청, appraisal 1 Hz, 주), Spacetop | partially: Tambini 2017(정서 상태 지속)(Round 3 검토) | overlap: Emo-FilM 연구: Emo-FilM 시간 정보와 사전학습 encoder 겹침 / EmoBrain: V-JEPA2 사용 |
| RQ-26 | 정서 상태는 HRF로 설명되지 않는 관성을 갖는가: Mind captioning 테스트 run의 의사 무작위 순서를 실제 조작으로 쓸 때, 직전 클립의 정서는 현재 클립의 정서 부분공간 반응을 시각 부분공간보다 더 오래 바꾸는가? | D+K+E+P+Q (+외부: Complex Systems (line attractor, Nair 2023)) | literature (LIT-10; MD-P1, GI-P3, SN-P2; Round 3 MD-P1 검토) | 10.1016/j.cell.2022.11.027; 10.1038/s41586-024-07915-x; 10.1038/nn.4468; 10.1126/sciadv.adw1464; 10.1038/s41593-025-01945-y | Mind captioning(의사 무작위 순서, 주), Horikawa 2020(고정 순서), Emo-FilM(washout) | partially: Pichon 2015, Tambini 2017(Round 3 검토) | overlap: Emo-FilM 연구: Emo-FilM washout 구간 사용 부분 겹침 |
| RQ-27 | 단일 프레임으로는 정서가 맞지 않고 클립 전체를 봐야 맞는 클립(MLLM 단일 프레임 평정과 전체 클립 평정의 차이로 정의)에서, 정서 정보는 긴 시간 수용창 영역에서만 해독되는가? | C+D+U+I+F | literature (LIT-22; MD-P6) | 10.1038/s41598-025-14961-6; arXiv:2501.10970; 10.1016/j.isci.2020.101060 | Horikawa 2020, Mind captioning | partially: MLLM 단일 프레임 평정의 한계는 보고, 뇌 수준 검정은 없음 | 없음 |
| RQ-28 | 정서 상태의 좌표 배치는 영화마다 달라도 상태 사이의 흐름은 보존되는가: DSA로 본 영화 간 동역학 유사도가 좌표 사상(정렬) 유사도보다 높은가? | D+S+K+E (+외부: Complex Systems (dynamical similarity analysis)) | literature (LIT-39; GI-R4-4) | arXiv:2306.10168; 10.1371/journal.pcbi.1012994; 10.64898/2026.09.26.754452 | Emo-FilM(영화 14편), washout 구간 대조 | partially: Zaffina 2026(상대 기하 보존) | overlap: Emo-FilM 연구: Emo-FilM 시간 정보 분석과 부분 겹침 |
| RQ-29 | 언어(LLM과 인간 mental model)에서 얻은 정서 전이 사전확률은, 그 영화를 쓰지 않고도 보류된 Emo-FilM 영화의 신경 정서 상태 전이를 예측하는가? | D+S+C+I+E | literature (LIT-51; LS-R4-4) | 10.1073/pnas.1616056114; 10.1523/JNEUROSCI.1431-18.2018; 10.1038/s41467-025-68240-z | Emo-FilM(보류 영화) | partially: Thornton 2019(통제 과제에서 같은 논리) | overlap: Emo-FilM 연구: Emo-FilM 시간 정보 분석과 부분 겹침 |
| RQ-30 | 모델 latent와 뇌의 표상 궤적이 곧게 펴지는 성질(straightening)이 깨지는 순간은 정서적 놀람과 amygdala 반응을 컷, 자기회귀 구조를 통제한 뒤에도 예측하는가? | B+D+K+E+I | literature (LIT-53; FA-R4-4) | 10.1038/s41593-019-0377-4; 10.1038/s41467-021-25939-z; arXiv:2506.09985; 10.7554/eLife.107955 | Spacetop(TR 0.46 s), Emo-FilM | no(정서 기준), straightening 자체는 수행(frontier-ai Round 4 검색) | 없음 |
| RQ-31 | 정서 관련 영역은 자연 영화의 표상 궤적을 시각피질보다 더 곧게 펴는가, encoding 모델의 예측 궤적은 관찰된 곡률을 재현하는가? | D+F+H+K+T | random (RND-14; random_combos.csv; Round 4 FA-R4-4(LIT-53)와 독립 수렴) | 10.1038/s41593-019-0377-4; arXiv:2605.04326; arXiv:2306.10168 | Spacetop(짧은 TR), Emo-FilM | 미확인: 인간 fMRI straightening 선행은 Stage 4에서 확인 | 없음 |
| RQ-32 | 정서의 각성은 신경 상태 공간의 위치가 아니라 속도인가: HRF, 움직임, 전역 신호, 사건 경계를 통제한 뒤 신경 상태 변화 속도가 국소 평균 활성보다 arousal 평정과 EDA를 더 잘 추적하는가? | D+A+E+K+Q | strategy (STR-E1; Strategy E(Dynamics and Geometry): 정서를 위치가 아니라 궤적으로) | 10.1371/journal.pcbi.1012994; 10.1038/s41593-025-01945-y; arXiv:2306.10168; 10.7554/eLife.107955 | Emo-FilM(arousal 1 Hz consensus, 참가자 EDA), Spacetop | 미확인: Stage 4에서 확인 | 없음 |
| RQ-33 | 같은 클립이 서로 다른 직전 클립 뒤에 제시된 Mind captioning 반복 노출에서, 직전 클립의 정서는 현재 클립의 정서 표상을 그쪽으로 끌어당기는가(동화) 밀어내는가(대비), 두 클립을 이어 넣은 in-silico 예측은 관찰된 맥락 효과를 재현하는가? | C+P+D+E+L | strategy (STR-G1; Strategy G(Counterfactual Neuroscience): 데이터셋 안의 실제 순서 변이를 반사실 조작으로) | 10.1093/scan/nsl014; 10.1371/journal.pone.0308295; 10.1126/sciadv.adw1464; arXiv:2605.04326 | Mind captioning(의사 무작위 순서, 최대 11회 노출) | partially: Mobbs 2006, Cao 2024(통제된 얼굴-장면 설계) | 없음 |

### K6. 행동 경향과 affordance (Axis V) (질문 7개)

| RQ | 연구 질문 | Axis 조합 | 경로 (조합 ID, 출처) | 근거 논문 ID | 가능한 데이터셋 | 선행 판정 | overlap |
|---|---|---|---|---|---|---|---|
| RQ-34 | 접근과 회피가 갈리는 영화 구간에서, 정서 범주 평정, 인간 행동 경향 평정, latent action model이 계산한 자극 affordance는 전운동, 두정, amygdala 반응을 각각 얼마나 고유하게 설명하는가? | V+A+I+E+P+R (+외부: Embodied Cognition / Affordances) | literature (LIT-07; BI-P2, FA-P4, GC-P8; Round 3 BI-P2 검토) | arXiv:2410.11758; 10.1038/s41467-024-44870-7; 10.1073/pnas.2414005122; 10.1093/cercor/bhad093; 10.1037/emo0001619 | Emo-FilM(Motivation 10항목, 주), Horikawa 2020 | partially: Thornton & Tamir 2024(상황과 정신상태 패턴이 허용 행동 패턴의 가중합), Morgenroth 2026(평정 수준) | 없음 |
| RQ-35 | 동기 방향(맞서기 대 멈추기)은 valence와 독립된 추상 축인가: 같은 valence 안에서 학습한 동기 방향 decoder가 다른 valence로 일반화되는가(교차 조건 일반화)? | V+K+E+A | literature (LIT-38; GI-R4-3) | 10.1016/j.cell.2020.09.031; 10.1162/jocn.2009.21317; 10.1093/cercor/bhad093; 10.1037/emo0001619 | Emo-FilM(Motivation 평정) | partially: 과제 기반 단변량 분리(Berkman & Lieberman 2010) | 없음 |
| RQ-36 | 정서 영상을 가만히 볼 때 전운동, 두정 피질의 행동 준비 활동은 같은 사람이 실제로 움직일 때의 패턴과 직교하는 부분공간에 놓이는가? | K+V+E (+외부: 운동 신경과학의 output-null subspace(Kaufman 2014)) | literature (LIT-40; BI-R4-1) | 10.1038/nn.3643; 10.1073/pnas.2414005122; 10.1016/j.isci.2020.101060 | Spacetop(수동 시청 + 다른 과제의 trackball 응답 구간) | partially: 정서 영상의 배측 경로 활성(Goldberg 2014) | 없음 |
| RQ-37 | 영화 사운드트랙의 groove 특성은 이산 정서 범주보다 행동 경향 평정과 SMA, 기저핵 반응을 더 잘 설명하는가? | M+V+E+I (+외부: Aesthetics / Neuroaesthetics (음악 groove)) | literature (LIT-41; BI-R4-2) | 10.1037/a0024208; 10.1126/sciadv.adk6840; 10.1037/emo0001619; 10.1038/s41597-025-04803-5 | Emo-FilM(주), Horikawa 2020(무음 대조) | no(brain-inspired Round 4 검색) | overlap: Emo-FilM 연구: Emo-FilM 소리의 정서 기여 분석과 부분 겹침 |
| RQ-38 | 같은 V-JEPA 2 encoder에서 행동 조건 예측기(V-JEPA 2-AC)가 행동 없는 예측기보다 정서 영상의 행동 경향 관련 뇌 분산을 더 고유하게 설명하는가, 그 이득은 데이터셋을 넘어 유지되는가? | J+V+H+E+S | literature (LIT-42; BI-R4-3) | arXiv:2506.09985; arXiv:2410.11758; 10.1073/pnas.2414005122; arXiv:2605.19352 | Emo-FilM, Horikawa 2020, Spacetop | partially: 게임 플레이 fMRI의 행동 모형 정렬(Oota 2026) | overlap: EmoBrain: V-JEPA2 사용 겹침 |
| RQ-39 | Emo-FilM의 Motivation 10개 항목은 정서 범주, valence와 구분되는 구성개념을 재는가: 인간 평정, AI(latent action, MLLM 평정), 뇌 반응 세 방법의 multitrait-multimethod 행렬에서 수렴 타당도와 변별 타당도가 성립하는가? | V+Q+I+F | literature (LIT-45; ET-R4-2) | 10.1037/h0046016; arXiv:2410.11758; 10.1038/s41597-025-04803-5; 10.1037/emo0001619; 10.1093/cercor/bhad093 | Emo-FilM | no(emotion-theory Round 4 검색) | 없음 |
| RQ-40 | latent action world model로 계산한 장면의 empowerment(행동이 미래에 미치는 통제력)는 Emo-FilM의 통제 가능성 appraisal, Motivation 평정, 관련 뇌 반응의 자극 계산 대리인가? | V+J+K+F (+외부: Embodied Cognition (empowerment, 내재 동기)) | literature (LIT-52; FA-R4-2) | arXiv:1310.1863; arXiv:2410.11758; 10.1080/02699930902928969; 10.1073/pnas.2414005122 | Emo-FilM | no(frontier-ai Round 4 검색) | 없음 |

방향만 유지한 조합: RND-04(affordance 편집과 latent action 내부 표상)

### K7. 기억, 회상, 내성 (Axis W) (질문 7개)

| RQ | 연구 질문 | Axis 조합 | 경로 (조합 ID, 출처) | 근거 논문 ID | 가능한 데이터셋 | 선행 판정 | overlap |
|---|---|---|---|---|---|---|---|
| RQ-41 | Mind captioning 회상 시행에서 정서 부분공간의 재활성은 시각, 의미 부분공간의 재활성과 별개로 그 시행의 vividness 보고를 예측하는가(cue가 함축하는 정서 통제 후)? | W+A+G+K+Q (+외부: Memory and Mental Imagery) | literature (LIT-12; ET-P6, VD-P6, EF-P2, BI-P6, SN-P5(일부); Round 3 ET-P6 검토) | 10.1126/sciadv.adw1464; 10.1093/cercor/bhv086; 10.3758/s13423-017-1313-9; 10.1523/JNEUROSCI.3022-16.2016; 10.1093/nc/nix007 | Mind captioning(유일한 회상 데이터) | partially: Saarimäki 2016(지각에서 심상으로의 정서 decoding 일반화)(Round 3 검토) | 없음 |
| RQ-42 | 반복 회상에서 정서 클립의 재활성 강도는 각성 자체보다 우선순위 재생 이론의 이득(gain) 대리 변수(놀람, 가치 변화)를 따르는가? | N+W+Q+E (+외부: Reinforcement Learning (prioritized replay, Mattar & Daw 2018)) | literature (LIT-43; BI-R4-4) | 10.1038/s41593-018-0232-z; 10.1126/sciadv.adw1464; 10.3758/s13423-017-1313-9 | Mind captioning(회상), Horikawa 2020(지각 encoder 보강) | no(brain-inspired Round 4 검색) | 없음 |
| RQ-43 | 회상 vividness 보고는 그 시행의 개인 재활성을 읽은 내성 보고인가, 모두에게 기억하기 쉬운 클립이라는 기억성의 반영인가: 반복 회상으로 item 안 변동과 item 간 차이를 분리하면 어느 쪽이 vividness를 설명하는가? | W+A+R+O+Q (+외부: Artificial Consciousness and Metacognition (LLM self-prediction vs cross-prediction)) | literature (LIT-44; ET-R4-1) | arXiv:2410.13787; 10.1038/s41598-018-26467-5; 10.1126/sciadv.adw1464; 10.3758/s13423-017-1313-9 | Mind captioning(6명, 72클립 반복 회상, 시행별 vividness) | partially(emotion-theory Round 4 검색) | 없음 |
| RQ-44 | 회상된 정서는 원 자극의 고유 흔적인가, 의미 요약이나 cue에서 생성적으로 재구성된 것인가: 회상 패턴은 원 클립 encoding 예측과 정서 배제 캡션(또는 cue만으로 생성한 영상) encoding 예측 중 어느 쪽에 가까우며, 정서 부분공간은 시각 세부보다 schema 쪽에 치우치는가? | W+L+N+H+P+I (+외부: Memory and Mental Imagery (기억의 생성 모델)) | literature (LIT-47; ET-R4-4, FA-R4-1(두 에이전트 독립 수렴)) | 10.1038/s41562-023-01799-z; 10.1126/sciadv.adw1464; 10.1073/pnas.1619316114; 10.3758/s13423-017-1313-9; arXiv:2503.20314 | Mind captioning(회상, 주), Horikawa 2020(지각 encoder 보강) | no(직접 검정), 이론과 구성 요소는 partially(emotion-theory, frontier-ai Round 4 검색) | 없음 |
| RQ-45 | MLLM 내부 정서 표상이 비디오에서 cue 캡션 텍스트로 넘어갈 때 보존되는 정도(기계 재현 지수)는 클립별로 뇌 회상의 정서 재현 정도를 예측하는가: 회상 정서는 언어 병목을 통과해 운반되는가? | R+W+C+I+U | literature (LIT-49; LS-R4-2) | arXiv:2604.07729; 10.1126/sciadv.adw1464; 10.1038/nn.4450; 10.1093/cercor/bhv086 | Mind captioning(주), Horikawa 2020 | no(llm-semantics Round 4 검색) | 없음 |
| RQ-46 | 사람과 LLM의 전달 사슬에서 클립 기술의 정서 내용이 보존되는 정도(집단 편향)는, 개인 회상에서 정서 재현과 시각 재현의 비(개인 편향)를 클립별로 예측하는가? | I+W+C+F (+외부: Social and Collective Behavior (문화 진화의 전달 사슬)) | literature (LIT-50; LS-R4-3) | 10.1073/pnas.2313790120; 10.1038/s41467-023-41648-1; 10.1126/sciadv.adw1464 | Mind captioning(주), Horikawa 2020 | no(llm-semantics Round 4 검색) | 없음 |
| RQ-47 | 회상 중 재활성된 패턴은 어떤 학습 목표로 만든 표상 공간에 더 가까워지는가: 지각 때 예측형 video 목표(V-JEPA 2) 공간에 가까운 영역이 회상 때는 언어 정렬 목표(CLIP, LLM) 공간 쪽으로 옮겨 가는가, 그 이동은 정서 관련 영역과 시각피질에서 다른가? | W+E+J+K+U | random (RND-02; random_combos.csv) | 10.1126/sciadv.adw1464; arXiv:2506.09985; 10.1038/s42256-025-01072-0; arXiv:2506.06898 | Mind captioning | partially: NSD-Imagery의 심상 decoding 모델 비교(Kneeland 2025) | 없음 |

방향만 유지한 조합: RND-06(회상 기하를 가장 잘 설명하는 모델 계열)

### K8. 몸, 생리, 피질하 경로 (질문 3개)

| RQ | 연구 질문 | Axis 조합 | 경로 (조합 ID, 출처) | 근거 논문 ID | 가능한 데이터셋 | 선행 판정 | overlap |
|---|---|---|---|---|---|---|---|
| RQ-48 | 자극 구동 encoder가 limbic 영역에서 놓치는 분산은 잡음, 몸, 평가 중 무엇인가: 생리를 자극 예측 가능 성분과 개인 성분으로 나누고 감각 강도와 평정을 더한 4원 분할에서 각 성분의 몫은 얼마인가? | A+E+H+Q+N (+외부: Reinforcement Learning / Computational Value (항상성 RL)) | literature (LIT-08; SN-P1, BI-P4, LS-P7, SN-P6; Round 3 SN-P1 검토) | 10.1038/s41593-025-01945-y; arXiv:2605.04326; 10.1162/imag.a.1300; 10.1371/journal.pcbi.1012994; 10.1038/s41597-025-04803-5 | Emo-FilM(참가자 PPG, 호흡, EDA, 주), Mind captioning(반복 ceiling 보정) | partially: 전역 자율신경 결합(Bolt 2025)은 보고, limbic encoding 잔차 분해는 없음 | overlap: Emo-FilM 연구: Emo-FilM과 사전학습 encoder 사용 겹침 |
| RQ-49 | 3T 자연 영상 fMRI에서 상구-pulvinar-amygdala 경로 신호는 분석 가능한가(내장 양성, 음성 대조 관문), 통과한다면 이 경로는 고수준 의미보다 저공간주파수 위협 feature와 looming을 더 싣는가? | E+B+N+L+P | literature (LIT-16; SN-P3, VD-P5, BI-P3, GC-P5; Round 3 SN-P3 검토) | 10.1016/j.neuron.2021.06.001; 10.1523/JNEUROSCI.1436-24.2025; arXiv:2607.19327; 10.1126/sciadv.adw1464 | Mind captioning(관문, 반복 신뢰도), Spacetop(주), Horikawa 2020 | partially: Kragel 2021(3T에서 표적과 교차 연결 차이 0.055로 작음)(Round 3 검토) | 없음 |
| RQ-50 | 왜 arousal 판독은 영화와 데이터셋을 넘어 전이되고 valence는 전이되지 않는가: arousal 정보는 개인 간 가장 크게 공유되는 저rank 전역 모드(전역 자율신경 성분과 겹치는)에 실리고, valence 정보는 고rank 개인 특이 성분에 실리는가? | O+K+E+S+A | literature (LIT-27; GI-P7) | 10.1371/journal.pcbi.1012994; 10.64898/2026.09.26.754452; 10.1038/s41593-025-01945-y; arXiv:2409.06843 | Emo-FilM(주, 생리 있음), Horikawa 2020+Mind captioning(보조) | partially: Ke 2025, Zaffina 2026이 전이 비대칭만 보고 | 없음 |

방향만 유지한 조합: LIT-26(정서 상태 위상 구조의 전역 자율신경 성분 불변성); RND-01(얕은 경로 기하의 데이터셋 간 전이)

### K9. In-silico 뇌와 AI 모델의 정서 충실도 (질문 6개)

| RQ | 연구 질문 | Axis 조합 | 경로 (조합 ID, 출처) | 근거 논문 ID | 가능한 데이터셋 | 선행 판정 | overlap |
|---|---|---|---|---|---|---|---|
| RQ-51 | TRIBE v2 같은 in-silico 뇌는 같은 자극의 실측 fMRI에 비해 정서 구조를 시각 구조보다 더 많이 잃는가, 그 손실은 어느 parcel과 rank 대역에 몰리며 백본(V-JEPA 2) feature 자체의 한계로 설명되는가? | F+H+S+T+K | literature (LIT-05; EF-P1, GC-P1, VD-P1, GI-P4; Round 3 EF-P1 검토) | arXiv:2605.04326; arXiv:2605.16739; 10.1126/sciadv.adw1464; arXiv:2302.06677; arXiv:2409.06843 | Mind captioning(반복 ceiling, 주), Horikawa 2020, Emo-FilM | partially: EmoMind RSA 0.635 -> 0.166 보고, NeurIPS 2026 TRIBE v2 평가(검색 색인만 확인) | overlap: Emo-FilM 연구: 사전학습 멀티모달 뇌 encoding 모델 사용 부분 겹침 |
| RQ-52 | Emo-FilM에서 음악, 대사 stem을 지운 in-silico 예측(TRIBE v2)이 바꾸는 정서 항목과 영역은, 관찰 데이터에서 소리 feature가 고유하게 설명하는 정서 항목과 영역과 일치하는가? | M+F+H+L+S | literature (LIT-11; EF-P7, MD-P3, GC-P4, MD-P4; Round 3 EF-P7 검토) | 10.1126/sciadv.adk6840; arXiv:2605.04326; arXiv:2110.09958; 10.1016/j.isci.2020.101060 | Emo-FilM(소리 있음, 주) | partially: Lettieri 2024(같은 영화의 판본 비교)(Round 3 검토) | overlap: Emo-FilM 연구: 사전학습 멀티모달 encoder로 Emo-FilM의 양식 기여 분석과 겹침 |
| RQ-53 | 정서와 무관한 저정서 클립만으로 학습한 피험자 간 정렬은 고정서 클립의 정서 기하까지 운반하는가, 운반되지 않는 정서 성분이 있다면 그것은 별도의 정렬 차원을 요구하는가? | O+K+R+S+I | literature (LIT-17; FA-P7, GI-P8, VD-P8) | arXiv:2609.34742; arXiv:2405.07987; 10.7554/eLife.56601; arXiv:2403.11207; arXiv:2409.06843 | Horikawa 2020+Mind captioning(site 간 쌍), NSD(사전학습 출처) | partially: 모델 사이에서는 Xing 2026 | overlap: EmoBrain: cross-subject 정렬과 정서 decoding 겹침 |
| RQ-54 | 정서 전용 하위체계는 최적화에서 창발하는가: Cowen & Keltner와 독립인 EmoSet으로 정서를 학습한 모델에서 창발한 정서 unit은 저수준 속성과 의미 속성 중 무엇으로 설명되고, 비정서 학습 모델보다 정서 관련 영역 분산을 고유하게 설명하는가? | N+I+B+S+F | literature (LIT-28; VD-P7) | arXiv:2307.07961; 10.1126/sciadv.aaw4358; 10.1523/JNEUROSCI.1436-24.2025 | 학습 EmoSet, 평가 Horikawa 2020, Mind captioning, NSD | partially: EmoNet(Kragel 2019) | 없음 |
| RQ-55 | 구조와 학습 데이터를 고정하고 학습 목표만 바꾼 video 모델(예측형, 마스킹 재구성형, 언어 정렬형) 중 어느 목표가 정서 기술 잔차(LIT-03)로 정의한 신뢰 정서 부분공간을 가장 잘 설명하는가? | C+E+J+K+Q | random (RND-24; random_combos.csv) | arXiv:2506.09985; 10.1038/s42256-025-01072-0; arXiv:2302.06677; arXiv:2409.06843 | Horikawa 2020+Mind captioning | 미확인: Stage 4에서 확인 | overlap: EmoBrain: V-JEPA2 사용 부분 겹침 |
| RQ-56 | video 모델을 정서 관련 영역의 fMRI를 예측하도록 미세조정하면, 시각피질로 미세조정한 경우보다 보류된 자극에서 인간 정서 판단과의 정렬이 더 좋아지는가? | I+J+F+A+S | strategy (STR-H1; Strategy H(Reverse Inspiration, 뇌 -> AI): brain-tuning) | arXiv:2511.07988; arXiv:2605.04326; arXiv:2408.13718; 10.1016/j.isci.2020.101060 | Horikawa 2020+Mind captioning(학습), Emo-FilM, Spacetop(인간 판단 평가) | partially: 사회 인지 brain-tuning(Policzer 2025) | overlap: EmoBrain: V-JEPA2와 teacher-student distillation으로 뇌 정서 정보 활용 겹침 |

방향만 유지한 조합: LIT-29(생성 decoding의 정서 중립화(affect round-trip audit)); LIT-33(in-silico 뇌가 잃는 개념); LIT-34(leakage 감사를 포함한 정서 encoding benchmark)

### K10. 소리, 언어, 서사 (질문 4개)

| RQ | 연구 질문 | Axis 조합 | 경로 (조합 ID, 출처) | 근거 논문 ID | 가능한 데이터셋 | 선행 판정 | overlap |
|---|---|---|---|---|---|---|---|
| RQ-57 | 영화 대사가 운반하는 정서는 어휘 감성인가 인물의 정신 상태 추론인가: vmPFC 정서 decoding은 어휘 수준 대사 feature를 지워도 남고 추론된 정신 상태 의미를 지우면 사라지는가? | M+C+D+E+I | literature (LIT-23; LS-P3) | 10.1126/sciadv.adk6840; 10.1111/cogs.13343; 10.1016/j.neuron.2020.10.029 | Emo-FilM(대사 있음, 전사 없음, 주), Spacetop narratives | partially: Lettieri 2024(양식별 기여) | overlap: Emo-FilM 연구: Emo-FilM 양식 기여 분석과 부분 겹침 |
| RQ-58 | 서사를 들을 때 문장 단위 단기 예측오차(LLM surprisal)와 이야기 초반에 형성된 장기 기대의 불일치는 서로 다른 영역과 본인 정서 평정을 설명하는가? | N+C+D+I+E (+외부: Reinforcement Learning (예측오차)) | literature (LIT-24; LS-P8) | 10.1162/neco_a_01341; arXiv:2407.02474; 10.1016/j.neuron.2020.10.029; 10.1111/cogs.13343 | Spacetop narratives(텍스트 4편, 오디오 4편, 본인 기대 평정) | partially: 서사 surprise와 사건 경계(Kumar 2023) | 없음 |
| RQ-59 | 영화의 순간마다 encoder 예측에서 오디오와 영상 기여가 상충할 때 평정자 간 정서 불일치도 커지는가, 그 순간 정서 관련 영역의 반응은 어느 양식을 따르는가? | D+F+M+R+Q | random (RND-07; random_combos.csv) | 10.1126/sciadv.adk6840; arXiv:2605.04326; 10.1038/s41597-025-04803-5 | Emo-FilM(평정자별 1 Hz 원자료) | 미확인: Stage 4에서 확인 | overlap: Emo-FilM 연구: 사전학습 멀티모달 encoder로 Emo-FilM 양식 기여 분석 겹침 |
| RQ-60 | 무음 정서 클립을 볼 때 청각피질은 '암시된 소리'를 표상하는가: video-to-audio 생성 모델이 만든 그럴듯한 소리의 오디오 feature가 무음 시청의 청각피질 반응을 설명하는가, 그 암시된 소리는 정서 정보를 싣는가? | B+F+M+R+T+L | random (RND-30; random_combos.csv) | 10.1038/nn.2533; arXiv:2412.15322; 10.1016/j.isci.2020.101060; 10.1126/sciadv.adw1464 | Horikawa 2020+Mind captioning(무음 시청) | partially: 소리를 암시하는 무음 영상이 청각피질 내용 특이 활동을 만든다(Meyer 2010). 정서와의 연결은 미확인 | 없음 |

방향만 유지한 조합: LIT-21(정서 정보의 시간 척도 위계와 양식 의존)

<!-- RQ_TABLE_END -->

---

## 5. 경로별 기여와 독립 수렴

* **문헌 경로(45개):**
  * Round 2의 수렴 제안 묶음과 Round 4의 미논의 쌍 제안이 대부분이다.
  * Round 4의 20개 제안 중 17개가 독립 질문이 되었다.
  * 나머지 3개 중 둘은 두 에이전트의 중복 수렴이라 하나로 합쳤고(RQ-18, RQ-44), 하나(LS-R4-1)는 방향만 유지했다.
* **무작위 경로(30개 중 질문 6, 방향 8, 기각 16):**
  * 무작위 조합이 문헌 경로와 독립적으로 같은 질문에 도달한 경우가 넷 있다.
    * RND-14와 FA-R4-4: straightening.
    * RND-16과 ET-P5: 원인 귀속과 정서 분화.
    * RND-03과 GC-P7: amygdala feature 귀속.
    * RND-01과 SN-P3: 피질하 경로 기하.
  * 기각 사유별 개수:
    * 다른 질문과의 중복: 9개. 그중 RND-19, RND-28은 Mind captioning 6명이라 개인차를 추론할 수 없다는 문제도 있다.
    * Novelty Constraint: 2개.
    * 순환 라벨: 2개.
    * 개인차 추론 불가와 개입 없음: 1개(RND-13).
    * 이미 수행된 연구: 1개(RND-15).
    * 전이 구조 없음: 1개(RND-18).
* **전략 경로(12개 중 질문 9, 기각 3):**
  * 각 전략이 만든 질문:
    * A: RQ-14. 첫 시도인 PPI는 기각.
    * B: RQ-04.
    * C: RQ-05.
    * D: RQ-06.
    * E: RQ-32.
    * F: RQ-20.
    * G: RQ-33.
    * H: RQ-56과 RQ-07.
  * 문헌 경로 질문과 데이터나 분석을 공유하지 않는 새 질문은 RQ-04, 06, 07, 14, 32다.
  * 나머지 넷(RQ-05, 20, 33, 56)은 문헌 경로 질문과 데이터를 공유하지만 묻는 것이 다르다.
* **독립 수렴의 해석:** 서로 다른 경로나 에이전트가 같은 질문에 도달한 것은 그 질문이 자연스러운 다음 단계라는 신호다. 동시에 그만큼 다른 연구실도 하고 있을 가능성이 높다는 신호이기도 하다. 그래서 Stage 4 선행연구 감사에서 이런 질문을 먼저 확인한다.

---

## 6. Novelty Constraint 적용 결과

* **기각:**
  * RND-08과 RND-29: 모델 계열별 amygdala 예측 비교.
  * STR-A2: foundation model 전이로 정서 decoding 정확도 향상.
  * STR-B2: 정서 영상 재구성.
* **방향만 유지:**
  * LIT-34: leakage 감사를 포함한 benchmark.
  * LIT-29: 생성 decoding의 정서 감사.
  * 둘 다 다른 질문의 검증 인프라로 쓴다.
* **범위를 조정해 유지:**
  * RQ-55: 모델 비교이지만 학습 목표만 바꾼 통제 비교이고, 대상이 정서 고유 부분공간이다.
  * RQ-51: 감사만으로는 benchmark라 백본 대비 차이를 과학적 질문으로 삼았다.
  * RQ-01: manifold 시각화가 아니라 경쟁 가설의 판정 규칙을 둔다.
  * RQ-10: 정확도가 아니라 전향 선택의 성공률을 본다.
* **남은 위험:** "Emotion별 activation 차이 비교"에 가까워질 위험이 가장 큰 질문은 RQ-49와 RQ-11이다. 둘 다 피질하 또는 amygdala 중심이다. RQ-49는 관문 통과 여부가, RQ-11은 범주 고정 제약 아래의 결과가 새 검증 논리다.

---

## 7. 한계와 미확인

1. **선행 판정은 아직 잠정적이다.**
   * 60개 중 partially가 41개다.
   * "no" 10개와 "미확인" 9개는 이번 Stage에서 체계적으로 검색하지 않았다. 각 질문을 낸 에이전트의 Round 2~4 검색 범위만 반영되어 있다.
   * Stage 4의 중복 감사가 필요하다.
2. **데이터 보유 상태가 미확인인 항목:**
   * Mind captioning 보유본의 캡션 파일 포함 여부.
   * Cowen & Keltner 원 클립의 오디오 보유 여부(RQ-52).
   * C&K 클립의 원본 영상 단위 중복.
   * 두 코호트의 피험자 중복.
   * Horikawa 2020 참가자의 모국어.
   * Spacetop 사용자 보유본이 공개 미러와 같은 판본인지.
3. **Decoding Axis(G)가 2개 질문에만 쓰였다.** Novelty Constraint 때문이다. "decoding을 과학적 질문으로 만드는 방법"(예: 전향 decoding, decoding 실패의 구조)이 충분히 탐색되었는지 Stage 4에서 점검한다.
4. **질문 수 60개는 최소 기준(30개)의 두 배다.** 군집 안 질문 다수가 같은 파이프라인을 공유하므로, 실제 독립 연구 단위는 3.2절의 공유 자원 수(약 9~12개)에 가깝다.
5. **Round 2 합의 쏠림의 영향.** Round 2 응답에는 반박이 0건이었다. 상위 10개 검토는 Round 2에서 수용된 검증 가능한 오류 4건을 찾았다. 검토받지 않은 Round 2 기반 질문에도 같은 종류의 오류가 남아 있을 수 있다. Stage 4 평가에서 질문마다 "핵심 전제 한 줄을 반증 시도했는가"를 적용한다(adversarial-reviewer 9.4절 권고).
