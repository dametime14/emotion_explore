# FINAL INDEX

* 프로젝트: Affective Neuroscience 연구 질문 탐색(Exploratory, Literature-Grounded, Model-Driven Research Discovery)
* 기준일: 2026-11-12
* 진행 기록: `outputs/STAGE_STATUS.md`

## 처음 읽는다면

1. `outputs/final_synthesis.md`(J): 여섯 질문에 대한 Coordinator의 답.
2. `outputs/evaluation/selection.md`: Shortlist 10개, 상위 5개, Pilot 3개가 정해진 과정.
3. `outputs/rq_cards/`(H): 질문 카드 10장. 각 카드 1절에 한 줄 질문이 있다.
4. `outputs/pilots.md`(I): 바로 시작할 Pilot 3개.
5. 전체 질문 60개를 보려면 `outputs/rq_landscape.md`(G) 4.1절의 한 줄 질문 목록을 본다.

## Deliverable A~J

| Deliverable | 파일 | 한 줄 설명 |
|---|---|---|
| A Dataset Intelligence Report | `outputs/stage1/dataset_intelligence_report.md` | 4개 데이터셋(Horikawa 2020, Emo-FilM, Spacetop, NSD)의 구조, 라벨 주체, 자극 접근성, 데이터셋 간 결합 가능성. Mind captioning은 Stage 2 이후 사용자 승인으로 추가되었다 |
| B Research Axis Encyclopedia | `outputs/axis_encyclopedia.md` | Axis A~W 정리, 필수 태그 6종, 갱신된 유형표, 채택하지 않은 Axis와 이견. V 행에 Stage 3 정정 주석 |
| C Verified Literature Database | `outputs/literature/literature_db.csv` | 에이전트별 literature.jsonl을 합친 통합 문헌 DB. 재생성은 `python3 -I outputs/literature/merge.py`. 고유 529편, verified 524편(최종 인용 검증 반영 후) |
| D Discussion & Future-Direction Mining | `outputs/future_directions.md` | 논문 Discussion과 Limitations에서 뽑은 future direction, Discussion-to-Research chain 80개 |
| E Cross-Disciplinary Opportunity Map | `outputs/opportunity_map.md` | 다른 분야에서 정서 신경과학으로 가져올 기술 82행과 역방향 11행. 5절이 Stage 3 갱신 |
| F Agent Discussion Record | `outputs/discussion_record.md` | Round 2~4의 제안과 비판, 수정된 주장, 합의 6개, 남은 이견 14개, 과정에 대한 비판적 기록(반박 0, 선정 오류) |
| G Research Question Landscape | `outputs/rq_landscape.md` | 질문 60개를 한 줄 질문과 자세한 설명으로 정리. 군집 10개, 관문 9개, 공유 파이프라인, 경쟁 설명, 용어 풀이 |
| H Top 10 Research Proposals | `outputs/rq_cards/` | Shortlist 10개의 질문 카드(P7 14개 항목, 검토 반영 기록, Safeguards 점검) |
| I Top 3 Pilot Study Plans | `outputs/pilots.md` | P1 RQ-08, P2 RQ-01(+RQ-03), P3 RQ-15. 데이터, 모델, 지표, 기준선, 계산량, 위험, 계속과 중단 기준 |
| J Coordinator's Final Synthesis | `outputs/final_synthesis.md` | 가장 큰 탐색 기회, 가져올 AI 개념, Horikawa 계열 자료의 덜 쓰인 정보, 모델 기반 방향, 위험과 현실의 균형, Pilot 순서 |

## 질문 카드 10장 (Deliverable H)

| 카드 | 한 줄 질문 | 우선순위 |
|---|---|---|
| `RQ08_beyond_scene_description.md` | 장면을 말로 설명한 내용을 빼고 나도 뇌에 정서 신호가 남을까? | 상위 1, Pilot P1 |
| `RQ15_read_vs_ask_AI_emotion.md` | AI가 영상의 정서를 판단할 때, AI 속 상태를 읽은 값과 AI가 말한 답 중 어느 쪽이 사람 뇌 반응과 더 잘 맞을까? | 상위 2, Pilot P3 |
| `RQ01_emotion_category_replication.md` | 뇌의 정서 반응은 범주로 나뉠까, 끊김 없이 이어질까, 그리고 그 답은 다른 그룹에서도 같을까? | 상위 3, Pilot P2 |
| `RQ03_stimulus_ensemble_geometry.md` | 뇌의 정서 지도는 영상의 정서가 다양해서 생길까, 겉모습이 다양해서 생길까? | 상위 4(P2 확장) |
| `RQ14_who_did_what_to_whom.md` | '누가 누구에게 무엇을 했는가'라는 장면 구조가 정서 반응을 설명할까? | 상위 5 |
| `RQ10_prospective_stimulus_selection.md` | 정서를 기준으로 고른 영상과 장면 내용을 기준으로 고른 영상 중 어느 쪽이 처음 보는 사람의 정서 관련 뇌 영역을 더 잘 움직일까? | Shortlist |
| `RQ33_natural_kuleshov.md` | 같은 장면도 앞에 무엇을 봤느냐에 따라 뇌가 그 장면의 정서를 다르게 표현할까? | Shortlist |
| `RQ60_implied_sound.md` | 소리 없는 영상을 볼 때 뇌는 '들릴 법한 소리'를 표현하고, 그 소리가 정서를 실을까? | Shortlist |
| `RQ32_arousal_as_speed.md` | 흥분(각성)은 뇌 활동의 '세기'로 나타날까, 뇌 활동 패턴이 바뀌는 '빠르기'로 나타날까? | Shortlist |
| `RQ44_recall_reconstruction.md` | 장면을 떠올릴 때 뇌에 다시 나타나는 정서 정보는 원래 장면의 흔적일까, 장면 설명을 바탕으로 다시 만든 것일까? | Shortlist |

## 보조 산출물

| 위치 | 내용 |
|---|---|
| `outputs/stage1/` | 데이터셋별 감사 보고서, gate 판정, Stage 4 사실 확인(`horikawa_factcheck_stage4.md`) |
| `outputs/literature/` | 문헌 통합 스크립트(`merge.py`), 통계, 인용 표본 검증, future direction 목록 |
| `outputs/discussion/` | Round 2 제안 색인, 응답 집계, Round 3 배정과 요약 |
| `outputs/combinations/` | 조합 원자료와 생성 스크립트(`build_matrix.py`), `matrix.csv`(조합 96개), `rejected.md`, 무작위 조합, 논의된 Axis 쌍 |
| `outputs/evaluation/` | 독립 채점 2종과 대조(`scores_*`), 평가 노트, 선행연구 중복 감사, 선정, 카드 검토 2종, 최종 인용 검증 |
| `outputs/agents/<이름>/` | 에이전트별 Round 1~4 산출물과 literature.jsonl |
| `outputs/agent_registry.md` | 실행한 에이전트 ID(이 세션 안에서만 유효) |

## 재탐색 라운드 (Stage 4 이후)

| 파일 | 내용 |
|---|---|
| `outputs/revision/plan.md` | 사용자 지시, 새 평가 기준 2개, 에이전트 배정 |
| `outputs/revision/candidates.md` | 후보 28개와 한 줄 질문 |
| `outputs/revision/scores_reconciled.md` | 두 독립 채점의 대조와 조정 |
| `outputs/revision/prior_overlap_audit.md` | 상위 7개 묶음 선행연구 중복 감사 |
| `outputs/revision/selection.md` | 선정 규칙, 상위 5개 묶음(A~E), 예비 후보, 사용자 방향에 대한 정정 |
| `outputs/revision/feedback_round2.md` | 선정 결과에 대한 사용자 피드백과 답(A, C, D 통합 근거, B 주장 범위, C-21 해석 절차) |
| `outputs/revision/design_brief.md` | R1~R3 설계 지시서(사용자 결정, 공통 규칙) |
| `outputs/revision/cards/` | **R1 뇌를 닮은 정서 모델, R2 떠올린 장면의 정서 이동, R3 뇌가 스스로 나눈 축의 해석** 카드(P7 + 검토 반영 기록) |
| `outputs/revision/card_review.md`, `card_theory_review.md`, `card_revision_orders.md` | 카드의 두 독립 검토와 통합 수정 지시 |
