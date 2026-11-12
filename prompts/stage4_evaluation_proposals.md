# Stage 4: Evaluation, Question Cards, Pilots, Final Synthesis

너는 이 프로젝트의 Coordinator다. 이번 실행에서는 **Stage 4만** 수행한다. 산출물은 Deliverable H, I, J다.

## 0. 준비
1. `outputs/STAGE_STATUS.md`, `outputs/rq_landscape.md`, `outputs/combinations/matrix.csv`, `outputs/discussion_record.md`, `outputs/stage1/dataset_intelligence_report.md`를 읽는다.
2. 사용자가 Stage 3 이후 남긴 지시(제외하거나 우선할 질문)가 있으면 STAGE_STATUS.md에서 확인하고 반영한다.
3. `outputs/evaluation/`과 `outputs/rq_cards/` 폴더를 만든다.

## 1. 독립 평가 (Phase VI)
1. Coordinator가 rq_landscape.md의 모든 질문을 `reference/protocols.md`의 **P6** 기준으로 평가한다. 결과는 `outputs/evaluation/scores_coordinator.csv`에 쓴다.
2. `adversarial-reviewer`를 새로 실행해 Coordinator 점수를 보지 않은 상태로 같은 평가를 하게 한다. 결과는 `outputs/evaluation/scores_reviewer.csv`에 쓴다.
3. 두 점수를 합쳐 `outputs/evaluation/scores_reconciled.md`를 만든다. 같은 항목에서 2점 이상 차이 나는 경우는 이유를 기록하고 조정한다. 조정되지 않은 이견은 그대로 남긴다.
4. Horikawa에서 가능한 연구를 우선 검토한다. 그다음 Emo-FilM, Spacetop, NSD를 통한 재현 또는 확장 가능성을 평가에 반영한다.

## 2. 선정
1. **Substantive Shortlist 10개를 선정한다.** 선정 이유와 탈락한 상위 후보의 탈락 이유를 `outputs/evaluation/selection.md`에 쓴다.
2. **선행연구 중복 감사를 수행한다.** `adversarial-reviewer`에게 10개 각각의 가장 가까운 선행연구를 직접 검색하게 한다. 이미 수행된 연구로 판정되면 교체 후보로 대체한다.
3. **High-priority Candidates 5개와 Recommended Pilot Studies 3개를 표시한다.**

## 3. Deliverable H: Top 10 Research Question Cards
1. 각 질문의 기원이 된 에이전트(matrix.csv와 discussion_record.md 기준)에게 Question Card 작성을 맡긴다. 병렬로 실행한다.
   * 형식은 `reference/protocols.md`의 **P7**을 따른다.
   * 파일은 `outputs/rq_cards/RQ<번호>_<짧은제목>.md`다.
   * Proposed Dataset 항목은 반드시 Stage 1 보고서를 근거로 쓰게 한다.
2. `adversarial-reviewer`가 10개 카드를 모두 검토한다. 검토 내용은 다음과 같다.
   * Competing Explanations와 Falsifiability가 실질적인가
   * Safeguards 위반이 없는가 (CLAUDE.md 6절)
   * 데이터에 실제로 그 라벨과 자극이 있는가
3. 지적 사항을 반영해 카드를 수정한다. 반영하지 않은 지적은 카드 하단에 이유와 함께 남긴다.

## 4. Deliverable I: Top 3 Pilot Study Plans
`outputs/pilots.md`에 3개 Pilot을 작성한다. 형식은 `reference/protocols.md`의 **P8**을 따른다. 각 Pilot은 `reference/datasets_and_resources.md`의 우리 환경 정보로 실행 가능해야 한다. 환경 정보가 비어 있으면 필요한 조건을 명시한다.

## 5. Deliverable J: Coordinator's Final Synthesis
`outputs/final_synthesis.md`에 다음 질문에 답한다. 모든 주장에 근거 논문이나 산출물 경로를 단다.
1. 현재 Affective Neuroscience에서 가장 큰 탐색 기회는 무엇인가?
2. 다른 AI 분야에서 가져와야 할 가장 중요한 연구 개념은 무엇인가?
3. Horikawa 데이터셋에서 아직 충분히 활용되지 않은 정보는 무엇인가?
4. 가장 강력한 모델 기반 연구 방향은 무엇인가?
5. 가장 독창적이지만 위험한 방향과, 현실적으로 성공 가능성이 높은 방향은 각각 무엇인가?
6. 어떤 세 가지 Pilot부터 시작하는 것이 가장 합리적인가?

## 6. 최종 인용 검증
`adversarial-reviewer`를 새로 실행한다. rq_cards와 final_synthesis.md에 인용된 모든 논문 ID가 literature_db.csv에 있고 verified인지 확인하게 한다. 없는 인용은 검증하거나 제거한다. 결과는 `outputs/evaluation/final_citation_check.md`에 저장한다.

## 7. 마무리
1. `outputs/FINAL_INDEX.md`에 Deliverable A~J의 파일 경로와 한 줄 설명을 정리한다.
2. `outputs/STAGE_STATUS.md`에 Stage 4 완료를 기록한다.
3. 사용자에게 다음을 요약해 보여준다.
   * 상위 5개 질문
   * 3개 Pilot
   * 남은 이견
   * 미확인 사항

| Deliverable | 파일 |
|---|---|
| A Dataset Intelligence Report | outputs/stage1/dataset_intelligence_report.md |
| B Research Axis Encyclopedia | outputs/axis_encyclopedia.md |
| C Verified Literature Database | outputs/literature/literature_db.csv |
| D Discussion & Future-Direction Mining | outputs/future_directions.md |
| E Cross-Disciplinary Opportunity Map | outputs/opportunity_map.md |
| F Agent Discussion Record | outputs/discussion_record.md |
| G Research Question Landscape | outputs/rq_landscape.md |
| H Top 10 Research Proposals | outputs/rq_cards/ |
| I Top 3 Pilot Study Plans | outputs/pilots.md |
| J Coordinator's Final Synthesis | outputs/final_synthesis.md |
