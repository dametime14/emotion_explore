# emotion_explore

Affective Neuroscience 연구 질문 탐색 프로젝트에서 **현재 우선하는 두 연구 질문(R1, R3)**을 모은 곳이다. 탐색의 전 과정(Stage 1~4, 후보 28개 재탐색, 채점, 선행 감사, 보류한 R2)은 작업 브랜치 [`claude/practical-galileo-rrejhn`](https://github.com/dametime14/emotion_explore/tree/claude/practical-galileo-rrejhn)에 그대로 있다.

* 기준일: 2026-11-13
* 자료: Horikawa 2020(5명)과 Mind captioning(6명)의 같은 Cowen & Keltner 영상 클립 fMRI, 보조로 NSD
* 정서 라벨은 별도 평정자가 보고한 정서의 집계(규범 평정)다. 두 카드 모두 '장면의 정서적 의미(규범 기준)'까지만 주장하고 참가자의 정서 경험은 주장하지 않는다.

## 두 질문

| ID | 한 줄 질문 | 카드 |
|---|---|---|
| R1 | 뇌를 닮은 장치를 하나씩 넣고 뺀 AI를 키워 보면, 사람 뇌에 장면의 정서적 의미가 놓이는 방식은 어떤 장치가 있을 때 나타날까? | [`R1_brainlike_emotion_model.md`](outputs/revision/cards/R1_brainlike_emotion_model.md) |
| R3 | 뇌가 정서 단어 없이 스스로 나눈 축은 장면의 정서적 의미를 따를까, 장면 내용을 따를까, 아니면 둘을 함께 담을까? | [`R3_brain_axes_interpretation.md`](outputs/revision/cards/R3_brain_axes_interpretation.md) |

## 읽는 순서

카드가 각각 500줄 안팎이라 아래 절만 먼저 읽으면 된다.

**R1 뇌를 닮은 정서 모델**

| 순서 | 절 | 무엇을 보나 |
|---|---|---|
| 1 | 맨 위 용어 표, 1절 | S1, S1′, S2 같은 용어와 조건문으로 된 질문 |
| 2 | 2절 | 정서가 고차 영역에 놓이는 이유에 대한 네 설명(일반 추상화, 개념 학습, 재진입, 고차 반응 형식) |
| 3 | 13절 | **1주차에 실측 자료만으로 확인하는 것과, 그 결과에 따른 의사결정 규칙** |
| 4 | 7.1절 | 핵심 판 8개 모델(팔)이 각각 무엇을 바꾸는지 |
| 5 | 10절, 12절 | 결과별 의미, 반대 예측 이론, 위험 |

**R3 뇌가 스스로 나눈 축의 해석**

| 순서 | 절 | 무엇을 보나 |
|---|---|---|
| 1 | 1절, 5절 | 질문, 그리고 Horikawa 2020, Westlin 2025와 다른 점 |
| 2 | 8절 해석 절차 0~5단계 | 해석을 어떻게 하는지. 판정 기준은 결과 전에 숫자로 고정 |
| 3 | 8절 최종 판정표 | 어떤 결과를 무엇이라고 부르는지 |
| 4 | 8절 R1 전달 형식 | R3 결과가 R1에서 모델이 맞혀야 할 뇌 기준으로 넘어가는 방식 |

**두 카드의 관계:** R1 1주차(실측 자료만으로 정서 고유 위계가 있는지)와 R3 0~1단계(두 코호트에서 재현되는 부분공간이 있는지)는 같은 준비물을 쓰고 GPU 없이 같은 주에 할 수 있다.

## 이 브랜치(main)에 있는 파일

| 파일 | 내용 |
|---|---|
| `outputs/revision/cards/R1_brainlike_emotion_model.md` | R1 질문 카드(P7 14개 항목, Safeguards 점검, 검토 반영 기록) |
| `outputs/revision/cards/R3_brain_axes_interpretation.md` | R3 질문 카드(같은 구성) |
| `outputs/revision/R1_R3_reviews.md` | 두 독립 검토(방법론, 정서 이론)와 통합 수정 지시에서 R1, R3 절만 옮긴 발췌 |
| `outputs/revision/R1_R3_references.csv` | 두 카드가 인용한 문헌 67편. 모두 DOI, PMID, arXiv ID 중 하나로 존재를 확인했다. `discussion_read`는 본문 확인 수준이다 |

## 카드 안의 다른 파일 경로

카드는 작업 브랜치의 다른 파일을 근거로 인용한다. 예를 들어 `design_brief.md`, `feedback_round2.md`, `prior_overlap_audit.md`, 에이전트별 `revision_round.md`, `literature.jsonl`이 있다. 이 파일들은 main에는 없고 작업 브랜치에 있다. 경로 앞에 아래 주소를 붙이면 열린다.

`https://github.com/dametime14/emotion_explore/blob/claude/practical-galileo-rrejhn/`
