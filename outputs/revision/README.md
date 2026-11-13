# 재탐색 라운드: 지금 읽을 것

* 기준일: 2026-11-13
* 사용자 결정: **R1과 R3를 우선한다.** R2(회상)는 원자료 재처리 때문에 시간이 오래 걸려 보류한다.
* 두 카드 모두 P7 14개 항목과 검토 반영 기록을 갖췄다. 카드가 길어서(각 500줄 안팎) 아래 순서로 필요한 절만 읽으면 된다.

## 1. R1 뇌를 닮은 정서 모델

파일: [`cards/R1_brainlike_emotion_model.md`](cards/R1_brainlike_emotion_model.md)

> 뇌를 닮은 장치를 하나씩 넣고 뺀 AI를 키워 보면, 사람 뇌에 장면의 정서적 의미가 놓이는 방식은 어떤 장치가 있을 때 나타날까?

| 순서 | 절 | 무엇을 보나 |
|---|---|---|
| 1 | 맨 위 '이 카드에서 쓰는 말' 표 | S1, S1′, S2, 모델 내부 위계 같은 용어 |
| 2 | 1절 Core Research Question | 조건문으로 바꾼 질문 |
| 3 | 2절 Scientific Motivation | 정서가 고차 영역에 놓이는 이유에 대한 네 설명(일반 추상화, 개념 학습, 재진입, 고차 반응 형식) |
| 4 | 13절 Pilot Experiment | **1주차 실측 확인과 의사결정 규칙.** 결과에 따라 2주차 계획이 어떻게 바뀌는지 |
| 5 | 7.1절 4주 핵심 판 | 8개 모델(팔)이 각각 무엇을 바꾸는지 |
| 6 | 10절 Potential Findings | 결과별 의미와 반대를 예측하는 이론 |
| 7 | 12절 Limitations & Risks | 가장 큰 위험 |
| 필요 시 | 8.2~8.4절 | 서명 계산과 판정 규칙의 세부 |

## 2. R3 뇌가 스스로 나눈 축의 해석

파일: [`cards/R3_brain_axes_interpretation.md`](cards/R3_brain_axes_interpretation.md)

> 뇌가 정서 단어 없이 스스로 나눈 축은 장면의 정서적 의미를 따를까, 장면 내용을 따를까, 아니면 둘을 함께 담을까?

| 순서 | 절 | 무엇을 보나 |
|---|---|---|
| 1 | 맨 위 '이 카드에서 쓰는 말' 표 | 재현 부분공간, U_E, U_C, U_P 같은 용어 |
| 2 | 1절, 5절 Novelty | 질문과, Horikawa 2020, Westlin 2025와 무엇이 다른지 |
| 3 | 8절 '해석 절차' 0~5단계 | **"해석을 어떻게 하나"에 대한 답.** 단계마다 판정 기준이 숫자로 미리 정해져 있다 |
| 4 | 8절 '최종 판정표' | 어떤 결과가 나오면 무엇이라고 부르는지 |
| 5 | 8절 'R1 전달 형식' | R3 결과가 R1의 뇌 기준으로 넘어가는 방식 |
| 6 | 10절, 13절 | 결과별 의미, 1~2주차 첫 분석 |

## 3. R1과 R3의 관계

* 1주차에 같은 준비물을 쓴다. Horikawa와 MC 전처리, 캡션 기반 속성, 73차원 의미 특징, ROI 묶음, 화면 속 인물 정서 특징이다.
* R1 1주차(실측 자료만으로 정서 고유 위계가 있는지)와 R3 0~1단계(두 코호트에서 재현되는 부분공간이 있는지)는 GPU 없이 같은 주에 할 수 있다.
* R3에서 재현된 부분공간은 R1에서 모델이 맞혀야 할 뇌 기준으로 쓴다.

## 4. 비판과 배경 (필요할 때)

| 파일 | 내용 |
|---|---|
| [`card_review.md`](card_review.md) 1절, 3절 | 방법론 검토(R1, R3) |
| [`card_theory_review.md`](card_theory_review.md) 1절, 3절 | 정서 이론 검토(R1, R3) |
| [`card_revision_orders.md`](card_revision_orders.md) | 두 검토를 합친 수정 지시. 카드 끝 '검토 반영 기록'과 대조 |
| [`feedback_round2.md`](feedback_round2.md) | A, C, D를 하나로 묶은 근거, C-21 해석 절차의 출발점 |
| [`design_brief.md`](design_brief.md) | 사용자 결정과 카드 공통 규칙 |
| [`selection.md`](selection.md), [`prior_overlap_audit.md`](prior_overlap_audit.md) | 28개 후보에서 여기까지 온 과정 |

## 5. 보류

* R2([`cards/R2_recall_affective_shift.md`](cards/R2_recall_affective_shift.md)): MC 시험, 회상 run 원자료 재처리가 필요해 보류.
