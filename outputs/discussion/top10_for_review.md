# Round 2 응답 집계와 상위 10개 (adversarial-reviewer 검토 대상)

* 생성: `python3 -I outputs/discussion/tally_responses.py`
* 응답 집계: 수용 51, 수정 45, 반박 0. 응답이 기록되지 않은 제안: 0개 
* 점수 = 수용 수 + 0.5 x 수정 수 + 0.5 x (보낸 에이전트 밖에서 그 제안 ID를 언급한 파일 수). '가장 많이 수용되거나 언급된' 기준을 하나의 점수로 합친 Coordinator 규칙이다.

## 상위 10개

| 순위 | 제안 | 보낸 → 받는 | 요약 | 수용 | 수정 | 반박 | 언급 파일 수 | 점수 |
|---|---|---|---|---|---|---|---|---|
| 1 | EF-P3 | encoding-foundation → emotion-theory | "기대 반응"의 네 가지 정의와 그 잔차가 본인 보고 편차를 예측하는가 (공동 설계) | 3 | 0 | 0 | 5 | 5.5 |
| 2 | ET-P2 | emotion-theory → encoding-foundation |  | 2 | 1 | 0 | 5 | 5.0 |
| 3 | GI-P5 | geometry-info → vision-decoding | Spacetop "잔차 대 본인 보고 편차" 제안 여섯 개를 기준선 multiverse 하나로 | 1 | 1 | 0 | 7 | 5.0 |
| 4 | LS-P1 | llm-semantics → vision-decoding |  | 2 | 0 | 0 | 6 | 5.0 |
| 5 | BI-P1 | brain-inspired → geometry-info | 정서 지도의 방향성 검정: successor geometry 통합안 | 2 | 0 | 0 | 5 | 4.5 |
| 6 | GI-P1 | geometry-info → emotion-theory | 두 코호트 교차 공유 스펙트럼으로 Horikawa 범주 결론과 Westlin 재현 실패를 판정하기 | 1 | 1 | 0 | 6 | 4.5 |
| 7 | LS-P2 | llm-semantics → encoding-foundation |  | 2 | 1 | 0 | 4 | 4.5 |
| 8 | GC-P2 | generative-counterfactual → llm-semantics | 기술 잔차(통계 통제)와 의미 고정 편집(설계 통제)을 같은 voxel에서 맞대기 | 2 | 0 | 0 | 4 | 4.0 |
| 9 | GI-P2 | geometry-info → brain-inspired | 정서 전이의 방향성 성분: SR(T) 대 SR(T')를 넘어 반대칭 흐름과 비가역성으로 | 2 | 0 | 0 | 4 | 4.0 |
| 10 | BI-P2 | brain-inspired → frontier-ai | Axis V 경쟁 검정: 정서 범주 대 행동 경향 대 자극 계산 affordance | 1 | 0 | 0 | 5 | 3.5 |

## 11~25위

| 순위 | 제안 | 수용 | 수정 | 반박 | 언급 파일 수 | 점수 |
|---|---|---|---|---|---|---|
| 11 | EF-P1 | 1 | 1 | 0 | 4 | 3.5 |
| 12 | EF-P7 | 1 | 1 | 0 | 4 | 3.5 |
| 13 | ET-P1 | 2 | 0 | 0 | 3 | 3.5 |
| 14 | ET-P4 | 2 | 0 | 0 | 3 | 3.5 |
| 15 | EF-P4 | 2 | 0 | 0 | 2 | 3.0 |
| 16 | GI-P3 | 1 | 0 | 0 | 4 | 3.0 |
| 17 | GI-P4 | 2 | 0 | 0 | 2 | 3.0 |
| 18 | VD-P1 | 2 | 0 | 0 | 2 | 3.0 |
| 19 | ET-P6 | 0 | 1 | 0 | 4 | 2.5 |
| 20 | FA-P3 | 0 | 1 | 0 | 4 | 2.5 |
| 21 | SN-P1 | 1 | 0 | 0 | 3 | 2.5 |
| 22 | SN-P3 | 1 | 0 | 0 | 3 | 2.5 |
| 23 | SN-P7 | 1 | 1 | 0 | 2 | 2.5 |
| 24 | FA-P6 | 0 | 1 | 0 | 3 | 2.0 |
| 25 | FA-P7 | 1 | 0 | 0 | 2 | 2.0 |
