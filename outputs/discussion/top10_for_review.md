# Round 2 응답 집계와 상위 10개 (adversarial-reviewer 검토 대상)

* 생성: `python3 -I outputs/discussion/tally_responses.py`
* 응답 집계: 수용 21, 수정 25, 반박 0. 응답이 기록되지 않은 제안: 30개 GI-P5 EF-P1 ET-P2 BI-P4 EF-P5 ET-P7 GI-P8 LS-P1 LS-P2 LS-P4 LS-P5 MD-P5 SN-P1 VD-P4 VD-P8 BI-P6 EF-P2 EF-P6 ET-P6 FA-P1 FA-P2 FA-P8 GC-P1 GC-P3 GC-P7 GI-P4 MD-P3 MD-P4 SN-P5 VD-P1
* 점수 = 수용 수 + 0.5 x 수정 수 + 0.5 x (보낸 에이전트 밖에서 그 제안 ID를 언급한 파일 수). '가장 많이 수용되거나 언급된' 기준을 하나의 점수로 합친 Coordinator 규칙이다.

## 상위 10개

| 순위 | 제안 | 보낸 → 받는 | 요약 | 수용 | 수정 | 반박 | 언급 파일 수 | 점수 |
|---|---|---|---|---|---|---|---|---|
| 1 | GI-P3 | geometry-info → multimodal-dynamics | 입력이 꺼진 구간의 흐름: washout 이완으로 HRF 잔여와 정서 관성을 가르기 | 1 | 0 | 0 | 4 | 3.0 |
| 2 | BI-P1 | brain-inspired → geometry-info | 정서 지도의 방향성 검정: successor geometry 통합안 | 1 | 0 | 0 | 3 | 2.5 |
| 3 | BI-P2 | brain-inspired → frontier-ai | Axis V 경쟁 검정: 정서 범주 대 행동 경향 대 자극 계산 affordance | 1 | 0 | 0 | 3 | 2.5 |
| 4 | EF-P3 | encoding-foundation → emotion-theory | "기대 반응"의 네 가지 정의와 그 잔차가 본인 보고 편차를 예측하는가 (공동 설계) | 1 | 0 | 0 | 3 | 2.5 |
| 5 | GI-P1 | geometry-info → emotion-theory | 두 코호트 교차 공유 스펙트럼으로 Horikawa 범주 결론과 Westlin 재현 실패를 판정하기 | 1 | 0 | 0 | 3 | 2.5 |
| 6 | GI-P2 | geometry-info → brain-inspired | 정서 전이의 방향성 성분: SR(T) 대 SR(T')를 넘어 반대칭 흐름과 비가역성으로 | 1 | 0 | 0 | 3 | 2.5 |
| 7 | ET-P4 | emotion-theory → systems-neuro |  | 1 | 0 | 0 | 2 | 2.0 |
| 8 | GC-P2 | generative-counterfactual → llm-semantics | 기술 잔차(통계 통제)와 의미 고정 편집(설계 통제)을 같은 voxel에서 맞대기 | 1 | 0 | 0 | 2 | 2.0 |
| 9 | GI-P5 | geometry-info → vision-decoding | Spacetop "잔차 대 본인 보고 편차" 제안 여섯 개를 기준선 multiverse 하나로 | 0 | 0 | 0 | 4 | 2.0 |
| 10 | GI-P7 | geometry-info → systems-neuro | 휴대 가능한 arousal은 저rank 전역 자율신경 모드인가 | 1 | 0 | 0 | 2 | 2.0 |

## 11~25위

| 순위 | 제안 | 수용 | 수정 | 반박 | 언급 파일 수 | 점수 |
|---|---|---|---|---|---|---|
| 11 | MD-P2 | 1 | 0 | 0 | 2 | 2.0 |
| 12 | SN-P2 | 1 | 0 | 0 | 2 | 2.0 |
| 13 | SN-P3 | 1 | 0 | 0 | 2 | 2.0 |
| 14 | VD-P2 | 1 | 0 | 0 | 2 | 2.0 |
| 15 | VD-P5 | 0 | 1 | 0 | 3 | 2.0 |
| 16 | BI-P5 | 0 | 1 | 0 | 2 | 1.5 |
| 17 | EF-P4 | 1 | 0 | 0 | 1 | 1.5 |
| 18 | EF-P7 | 0 | 1 | 0 | 2 | 1.5 |
| 19 | ET-P1 | 1 | 0 | 0 | 1 | 1.5 |
| 20 | FA-P3 | 0 | 1 | 0 | 2 | 1.5 |
| 21 | FA-P4 | 1 | 0 | 0 | 1 | 1.5 |
| 22 | FA-P7 | 1 | 0 | 0 | 1 | 1.5 |
| 23 | GC-P5 | 0 | 1 | 0 | 2 | 1.5 |
| 24 | GI-P6 | 0 | 1 | 0 | 2 | 1.5 |
| 25 | LS-P3 | 1 | 0 | 0 | 1 | 1.5 |
