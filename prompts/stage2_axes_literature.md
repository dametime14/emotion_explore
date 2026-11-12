# Stage 2: Axis Discovery & Literature Review (Round 1)

너는 이 프로젝트의 Coordinator다. 이번 실행에서는 **Stage 2만** 수행하고 멈춘다. 산출물은 Deliverable B, C, D와 E의 초안이다.

## 0. 준비
1. `outputs/STAGE_STATUS.md`를 읽는다. Stage 1에서 사용자가 결정해야 했던 항목이 미해결로 남아 있으면 사용자에게 먼저 묻는다.
2. `outputs/stage1/dataset_intelligence_report.md`와 `outputs/stage1/gate_decision.md`를 읽는다.
3. `reference/axes.md`를 읽는다.

## 1. Round 1: Independent Discovery (병렬)
아래 11개 에이전트를 동시에 실행한다. 각 에이전트의 담당 Axis는 `reference/axes.md` 1절의 표를 따른다.
* emotion-theory
* vision-decoding
* encoding-foundation
* multimodal-dynamics
* frontier-ai
* geometry-info
* systems-neuro
* generative-counterfactual
* llm-semantics
* brain-inspired
* adversarial-reviewer. 이 라운드에서는 Axis T, 평가 방법론, 재현성 연구에 대한 문헌 조사를 맡긴다.

위임 메시지에는 다음을 반드시 포함한다.
* "`reference/protocols.md`의 **P1**을 직접 읽고 그대로 따를 것"
* 읽을 파일: `reference/axes.md`, `reference/starting_papers.md`, `outputs/stage1/dataset_intelligence_report.md`
* 이번 라운드는 독립 탐색이므로 다른 에이전트의 폴더를 읽지 말 것
* 산출물 경로: `outputs/agents/<이름>/literature.jsonl`, `outputs/agents/<이름>/round1.md`
* 응답은 15줄 이내 요약만

각 에이전트의 agent ID를 `outputs/agent_registry.md`에 기록한다. Stage 3에서 SendMessage로 같은 에이전트를 재개할 때 쓴다.

## 2. 문헌 통합: Deliverable C
1. 모든 `outputs/agents/*/literature*.jsonl`을 합쳐 `outputs/literature/literature_db.csv`를 만든다. 스크립트로 처리하고, 스크립트는 `outputs/literature/merge.py`로 남긴다.
2. DOI, arXiv ID, 정규화한 제목 기준으로 중복을 제거한다. 중복 논문의 future_directions와 axes는 합친다.
3. 통계를 `outputs/literature/stats.md`에 쓴다.
   * verified 고유 논문 수
   * Axis별 논문 수
   * 연도 분포
   * discussion_read 분포
   * 담당 에이전트별 수
4. **verified 고유 논문이 100편 미만이면:** 논문이 적은 Axis를 찾아 담당 에이전트를 SendMessage로 재개해 추가 조사를 맡긴다. 100편 이상이 될 때까지 반복하되, 관련성 낮은 논문으로 채우지 않는다.

## 3. 인용 표본 검증
`adversarial-reviewer`를 새로 실행한다. 자신이 추가하지 않은 논문 중 무작위 25편(난수 시드 기록)을 골라 다음을 확인하게 한다.
* 식별자가 실제로 해당 논문으로 연결되는가
* 기록된 Discussion 내용이 원문과 맞는가

결과는 `outputs/literature/verification_sample.md`에 저장한다. 오류율이 높으면 해당 에이전트에게 자기 문헌 전체를 재점검시킨다.

## 4. Deliverable B: Research Axis Encyclopedia
`outputs/axis_encyclopedia.md`를 작성한다.
* 각 에이전트의 round1.md에 있는 Axis 확장 제안을 반영한 전체 Axis와 Sub-axis 트리
* Axis마다: 대표 논문 ID, 주요 모델, 미해결 문제, 다른 Axis와의 연결 지점
* 새로 추가된 독립 Axis와 그 근거
* `reference/axes.md` 1절의 유형 분류도 새 Axis까지 포함해 갱신한 표

## 5. Deliverable D: Discussion & Future-Direction Mining
`outputs/future_directions.md`를 작성한다.
* 모든 논문의 future_directions 수집
* already_done이 "no" 또는 "partially"인 것 중, 2026년 모델이나 보유 데이터셋으로 새로 해결 가능한 것을 선별
* 선별 항목마다 다음을 적는다.
  * 원 논문
  * Discussion 위치
  * 지금 가능해진 이유 (모델, 데이터)
  * 적용 데이터셋
* 서로 다른 논문 두 편의 limitation을 연결해 생긴 질문을 따로 모은 절

## 6. Deliverable E 초안: Cross-Disciplinary Opportunity Map
`outputs/opportunity_map.md`에 표로 작성한다. 열은 다음과 같다.
* Originating field
* Imported technique
* Target neuroscience problem
* Potential dataset
* Evidence for transfer (논문 ID)
* Novelty
* Feasibility

## 7. 마무리
`outputs/STAGE_STATUS.md`에 Stage 2 결과를 추가한다.
* 고유 문헌 수
* 산출물 경로
* 검증 표본 결과
* 미해결 사항
* 사용자 확인 필요 항목

그다음 멈추고 사용자에게 요약해서 보여준다. Stage 3으로 넘어가지 않는다.
