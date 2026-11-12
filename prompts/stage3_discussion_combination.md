# Stage 3: Agent Discussion & Combinatorial Question Generation

너는 이 프로젝트의 Coordinator다. 이번 실행에서는 **Stage 3만** 수행하고 멈춘다. 산출물은 Deliverable F, G와 E의 갱신본이다.

이 단계에서는 반드시 에이전트들이 서로의 결과를 활용해야 한다. 개별 리포트를 단순히 합치는 방식은 허용하지 않는다.

## 0. 준비
1. `outputs/STAGE_STATUS.md`, `outputs/agent_registry.md`, `outputs/axis_encyclopedia.md`, `outputs/future_directions.md`, `outputs/opportunity_map.md`를 읽는다.
2. `outputs/discussion/`과 `outputs/combinations/` 폴더를 만든다.

**에이전트 재개 방법:**
* 가능하면 agent_registry.md의 agent ID로 SendMessage를 보내 Stage 2의 에이전트를 재개한다.
* 재개가 불가능하면 같은 이름의 에이전트를 새로 실행하되, "먼저 `outputs/agents/<이름>/` 안의 자기 이전 산출물을 읽을 것"을 위임 메시지에 넣는다.

## 1. Round 2: Cross-Agent Exchange
1. 10개 연구 에이전트(dataset-auditor와 adversarial-reviewer 제외)에게 `reference/protocols.md`의 **P2**를 따르게 한다. P2에 있는 Coordinator 질문 8개를 위임 메시지에 그대로 넣는다.
2. 모든 round2.md를 읽고 `outputs/discussion/proposals_index.md`를 만든다. 열은 다음과 같다.
   * 제안 ID
   * 보낸 에이전트
   * 받는 에이전트
   * 요약
   * 근거 논문
3. 받는 에이전트마다 자신에게 온 제안 목록을 전달한다. 각 제안에 수용, 수정, 반박 중 하나로 응답하게 한다. 응답은 각자의 round2.md 하단에 추가한다.

## 2. Round 3: Constructive Disagreement
1. 각 연구 에이전트에게 **다른 에이전트가 만든** 제안 3개씩을 배정한다. 같은 제안이 서로 다른 분야의 에이전트 두 명에게 검토받도록 배정한다.
2. 배정받은 에이전트는 `reference/protocols.md`의 **P3**을 따른다.
3. `adversarial-reviewer`에게는 Round 2에서 가장 많이 수용되거나 언급된 제안 상위 10개를 별도로 검토시킨다.
4. 비판과 수정된 제안을 `outputs/discussion/round3_summary.md`에 기록한다.

## 3. Round 4: Unexpected Connections
1. Round 1~3에서 이미 논의된 Axis 조합(2개 조합, 3개 조합)을 `outputs/combinations/discussed_pairs.md`에 정리한다.
2. 관점이 서로 먼 에이전트 5개 이상(예: frontier-ai, brain-inspired, geometry-info, llm-semantics, emotion-theory)에게 `reference/protocols.md`의 **P4**를 따르게 한다.

## 4. Combinatorial Research Question Generation
`reference/protocols.md`의 **P5**를 Coordinator가 직접 수행한다.
1. **문헌 경로:** Round 1의 Discussion-to-Research chain, `outputs/future_directions.md`, Round 2~4 제안에서 조합을 뽑는다.
2. **무작위 경로:** 갱신된 Axis 유형표(axis_encyclopedia.md)에서 유형마다 Axis 하나씩 무작위로 뽑아 30개 조합을 만든다. 스크립트로 생성하고 시드를 기록한다. 각 조합이 연구 질문이 되는지 판정한다.
3. **전략 경로:** Strategy A~H를 각각 최소 한 번 적용한다.
4. 모든 조합을 `outputs/combinations/matrix.csv`에, 기각한 조합과 사유를 `outputs/combinations/rejected.md`에 기록한다.
5. Novelty Constraint를 적용하고 `reference/existing_projects.md`로 overlap을 표시한다.
6. 최소 수량을 채운다.
   * Broad Research Directions 40개 이상
   * Distinct Research Questions 30개 이상

## 5. Deliverable G: Research Question Landscape
`outputs/rq_landscape.md`를 작성한다.
* 30개 이상의 연구 질문. 질문마다 다음을 단다.
  * Axis 조합
  * 조합 경로
  * 근거 논문 ID
  * 가능한 데이터셋
  * overlap
* 질문을 단순 나열하지 말고 영역별로 군집화한다.
* 군집 사이의 관계도 설명한다. 어떤 질문이 다른 질문의 선행 조건인지, 같은 분석으로 함께 답할 수 있는지 등이다.

## 6. Deliverable F: Agent Discussion Record
`outputs/discussion_record.md`를 작성한다. 다음을 담는다.
* 에이전트들이 서로 제안하고 비판한 주요 내용
* 수정된 주장
* 최종 합의
* **남아 있는 의견 차이**. 실제 의견 충돌은 지우지 않는다.

## 7. Deliverable E 갱신
Round 2~4와 조합 결과를 반영해 `outputs/opportunity_map.md`를 갱신한다.

## 8. 마무리
`outputs/STAGE_STATUS.md`에 Stage 3 결과를 추가한다.
* 질문 수
* 군집 수
* 주요 미해결 이견
* 사용자 확인 필요 항목

그다음 멈추고 사용자에게 요약해서 보여준다. Stage 4로 넘어가지 않는다.
