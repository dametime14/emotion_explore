# Round 2 응답 집계와 상위 10개 (adversarial-reviewer 검토 대상)

* 생성: `python3 -I outputs/discussion/tally_responses.py`
* 응답 집계: 수용 51, 수정 45, 반박 0. 응답이 기록되지 않은 제안: 0개 
* 점수 = 수용 수 + 0.5 x 수정 수 + 0.5 x (보낸 에이전트 밖에서 그 제안 ID를 언급한 파일 수). '가장 많이 수용되거나 언급된' 기준을 하나의 점수로 합친 Coordinator 규칙이다.

## 상위 10개

| 순위 | 제안 | 보낸 → 받는 | 요약 | 수용 | 수정 | 반박 | 언급 파일 수 | 점수 |
|---|---|---|---|---|---|---|---|---|
| 1 | EF-P3 | encoding-foundation → emotion-theory | "기대 반응"의 네 가지 정의와 그 잔차가 본인 보고 편차를 예측하는가 (공동 설계) | 3 | 0 | 0 | 5 | 5.5 |
| 2 | ET-P2 | emotion-theory → encoding-foundation |  | 2 | 1 | 0 | 5 | 5.0 |
| 3 | LS-P2 | llm-semantics → encoding-foundation |  | 2 | 1 | 0 | 4 | 4.5 |
| 4 | GI-P5 | geometry-info → vision-decoding | Spacetop "잔차 대 본인 보고 편차" 제안 여섯 개를 기준선 multiverse 하나로 | 1 | 1 | 0 | 5 | 4.0 |
| 5 | BI-P1 | brain-inspired → geometry-info | 정서 지도의 방향성 검정: successor geometry 통합안 | 2 | 0 | 0 | 3 | 3.5 |
| 6 | ET-P4 | emotion-theory → systems-neuro |  | 2 | 0 | 0 | 3 | 3.5 |
| 7 | GI-P1 | geometry-info → emotion-theory | 두 코호트 교차 공유 스펙트럼으로 Horikawa 범주 결론과 Westlin 재현 실패를 판정하기 | 1 | 1 | 0 | 4 | 3.5 |
| 8 | GI-P2 | geometry-info → brain-inspired | 정서 전이의 방향성 성분: SR(T) 대 SR(T')를 넘어 반대칭 흐름과 비가역성으로 | 2 | 0 | 0 | 3 | 3.5 |
| 9 | LS-P1 | llm-semantics → vision-decoding |  | 2 | 0 | 0 | 3 | 3.5 |
| 10 | EF-P4 | encoding-foundation → systems-neuro | 뇌 입력 foundation model의 정서 latent: 누수 통제와 coverage 대조를 갖춘 공동 benchmark | 2 | 0 | 0 | 2 | 3.0 |

## 11~25위

| 순위 | 제안 | 수용 | 수정 | 반박 | 언급 파일 수 | 점수 |
|---|---|---|---|---|---|---|
| 11 | ET-P1 | 2 | 0 | 0 | 2 | 3.0 |
| 12 | GC-P2 | 2 | 0 | 0 | 2 | 3.0 |
| 13 | GI-P4 | 2 | 0 | 0 | 2 | 3.0 |
| 14 | VD-P1 | 2 | 0 | 0 | 2 | 3.0 |
| 15 | BI-P2 | 1 | 0 | 0 | 3 | 2.5 |
| 16 | EF-P1 | 1 | 1 | 0 | 2 | 2.5 |
| 17 | EF-P7 | 1 | 1 | 0 | 2 | 2.5 |
| 18 | GI-P3 | 1 | 0 | 0 | 3 | 2.5 |
| 19 | SN-P7 | 1 | 1 | 0 | 2 | 2.5 |
| 20 | LS-P7 | 1 | 0 | 0 | 2 | 2.0 |
| 21 | MD-P2 | 1 | 0 | 0 | 2 | 2.0 |
| 22 | VD-P2 | 1 | 0 | 0 | 2 | 2.0 |
| 23 | BI-P4 | 0 | 1 | 0 | 2 | 1.5 |
| 24 | BI-P5 | 0 | 1 | 0 | 2 | 1.5 |
| 25 | EF-P2 | 1 | 0 | 0 | 1 | 1.5 |
