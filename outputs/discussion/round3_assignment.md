# Round 3 검토 배정

* 작성: Coordinator (Stage 3). 배정 스크립트 `outputs/discussion/assign_round3.py` (시드 20261114), 결과 `outputs/discussion/round3_assignment.csv`
* 규칙(`prompts/stage3_discussion_combination.md` 2절): 연구 에이전트 10개가 다른 에이전트의 제안 3개씩 검토한다. 같은 제안은 서로 다른 분야의 에이전트 두 명이 검토한다. 검토자는 보낸 에이전트, 받는 에이전트, 받는 쪽 줄에 "참조"로 언급된 에이전트(합친 설계의 공동 제안자)가 아니다.
* 분야 구분: theory(emotion-theory), brain-ml(vision-decoding, encoding-foundation), multimodal(multimodal-dynamics), ai(frontier-ai), math(geometry-info), systems(systems-neuro), generative(generative-counterfactual), language(llm-semantics), computation(brain-inspired)

## 검토 대상 15개와 선정 이유

Round 2 제안은 76개다. 30개 검토 자리로 15개를 고르면서 (1) 여러 에이전트가 같은 설계로 수렴한 주제에서는 가장 통합적인 제안 하나, (2) 주제가 겹치지 않게, (3) 10개 에이전트가 모두 보낸 쪽으로 한 번 이상 들어가게 했다.

| 제안 | 보낸 → 받는 | 주제 | 선정 이유 | 검토자 |
|---|---|---|---|---|
| GI-P1 | geometry-info → emotion-theory | Horikawa 범주 결론 vs Westlin 재현 실패를 두 코호트 교차 공유 스펙트럼으로 판정 | 4개 에이전트(ET, SN, AR, GI)가 독립 수렴한 쟁점의 통합안. Mind captioning 코호트 추가 | vision-decoding, multimodal-dynamics |
| GI-P5 | geometry-info → vision-decoding | Spacetop "개인 잔차 대 본인 보고 편차" 6개 제안의 기준선 multiverse 통합 | 가장 많은 에이전트(5~6개)가 수렴한 설계 | systems-neuro, brain-inspired |
| LS-P1 | llm-semantics → vision-decoding | 정서 배제 캡션으로 설명하고 남는 정서 분산(기술 잔차) 통합 설계 | VD R6과 LS Chain 1의 수렴, Mind captioning 캡션 활용 | frontier-ai, geometry-info |
| GC-P2 | generative-counterfactual → llm-semantics | 통계 통제(기술 잔차)와 설계 통제(의미 고정 편집)를 같은 voxel에서 맞대기 | 정서 vs 의미 분리 문제의 방법 간 삼각 검증 | systems-neuro, emotion-theory |
| EF-P1 | encoding-foundation → generative-counterfactual | 같은 자극 surrogate 충실도 감사를 모든 in-silico 결과의 관문으로 | in-silico 결과 전체의 전제 조건 | systems-neuro, geometry-info |
| BI-P1 | brain-inspired → geometry-info | 정서 지도의 방향성 검정(successor geometry) | Ma & Kragel 2026 이후의 핵심 빈칸, BI와 GI의 수렴 | multimodal-dynamics, frontier-ai |
| BI-P2 | brain-inspired → frontier-ai | Axis V 경쟁 검정: 정서 범주 vs 행동 경향 vs 자극 계산 affordance | 새 Axis V의 대표 질문 | generative-counterfactual, encoding-foundation |
| SN-P1 | systems-neuro → encoding-foundation | 생리 반영 noise ceiling과 전역 자율신경 성분으로 limbic 맹점 분해 | 4개 에이전트가 수렴한 Emo-FilM 생리 분할 주제 | multimodal-dynamics, vision-decoding |
| FA-P3 | frontier-ai → multimodal-dynamics | 세 가지 예측 신호와 지속 상태 vs 재호출 | world model surprise를 정서 예측오차 위계로 | llm-semantics, emotion-theory |
| MD-P1 | multimodal-dynamics → geometry-info | 클립 사이 이월과 washout 이완을 하나의 이완 모형으로 | 정서 관성의 측정 문제(HRF 잔여 분리) | generative-counterfactual, encoding-foundation |
| EF-P7 | encoding-foundation → multimodal-dynamics | in-silico 감각 박탈과 관찰된 무음 조건의 대조 | 소리의 정서 기여, in-silico vs observed | llm-semantics, brain-inspired |
| ET-P6 | emotion-theory → vision-decoding | 회상 vividness가 정서 부분공간 재활성을 따르는가(Axis W, Introspective Access) | 새 Axis W의 대표 질문 | llm-semantics, frontier-ai |
| FA-P6 | frontier-ai → llm-semantics | 내부 표상 읽기 vs 출력 묻기(L2 층의 두 측정) | AI 추정 라벨의 측정 방식(Axis U, R) | generative-counterfactual, vision-decoding |
| SN-P3 | systems-neuro → brain-inspired | 피질하 경로 분석의 signal-feasibility 관문과 데이터 내장 대조 | 피질하 표적 질문의 전제 | geometry-info, encoding-foundation |
| VD-P4 | vision-decoding → generative-counterfactual | 생성기의 정서 중립화를 재는 affect round-trip audit | 생성 decoding과 편집의 공통 confound | emotion-theory, brain-inspired |

## 에이전트별 배정

| 에이전트 | 검토할 제안 |
|---|---|
| emotion-theory | GC-P2, FA-P3, VD-P4 |
| vision-decoding | GI-P1, SN-P1, FA-P6 |
| encoding-foundation | BI-P2, MD-P1, SN-P3 |
| multimodal-dynamics | GI-P1, BI-P1, SN-P1 |
| frontier-ai | LS-P1, BI-P1, ET-P6 |
| geometry-info | LS-P1, EF-P1, SN-P3 |
| systems-neuro | GI-P5, GC-P2, EF-P1 |
| generative-counterfactual | BI-P2, MD-P1, FA-P6 |
| llm-semantics | FA-P3, EF-P7, ET-P6 |
| brain-inspired | GI-P5, EF-P7, VD-P4 |

배정 스크립트의 첫 실행은 GI-P5에 llm-semantics(공동 제안자)를 배정했다. 참조로 언급된 에이전트를 제외하도록 고쳐 다시 배정했다.

검토하지 않는 61개 제안도 받는 에이전트의 응답(각 round2.md 3절)을 거치며, adversarial-reviewer가 Round 2에서 가장 많이 수용되거나 언급된 상위 10개를 따로 검토한다.
