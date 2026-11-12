# Agent Registry

Stage 3에서 SendMessage로 같은 에이전트를 재개할 때 쓰는 ID 목록이다. ID는 **이 Claude Code 세션 안에서만** 유효하다. 세션이 바뀌면 재개할 수 없으므로, 같은 이름의 에이전트를 새로 실행하고 "먼저 `outputs/agents/<이름>/` 안의 자기 이전 산출물을 읽을 것"을 위임 메시지에 넣는다(`prompts/stage3_discussion_combination.md` 0절).

## Stage 2 Round 1 (2026-11-12, 커스텀 에이전트 타입으로 실행)

| 에이전트 | agent ID | 담당 | 산출물 |
|---|---|---|---|
| emotion-theory | a85c474967cad849e | A, Q / Artificial Consciousness and Metacognition | `outputs/agents/emotion-theory/` |
| vision-decoding | ac253b97bb080c9b1 | B, G / Memory and Mental Imagery | `outputs/agents/vision-decoding/` |
| encoding-foundation | a1e352d659ed60d8c | F, H, S | `outputs/agents/encoding-foundation/` |
| multimodal-dynamics | ab3f5d7c66dfe0bff | D, M / Neuroaesthetics | `outputs/agents/multimodal-dynamics/` |
| frontier-ai | aab100cf89288f887 | I, J, R | `outputs/agents/frontier-ai/` |
| geometry-info | ae216f8ca9181b4e7 | K, O / Information-theoretic Neuroscience, Complex Systems | `outputs/agents/geometry-info/` |
| systems-neuro | a9168d8399dafca1e | E / Computational Psychiatry | `outputs/agents/systems-neuro/` |
| generative-counterfactual | ac45217287ea07230 | L, P | `outputs/agents/generative-counterfactual/` |
| llm-semantics | a4281de3bd21cf1c3 | C / Social and Collective Behavior, Human-AI Representation Differences | `outputs/agents/llm-semantics/` |
| brain-inspired | a33e66f5a273664cb | N / RL, Embodied, Ecological, Active Perception, Computational Ethology | `outputs/agents/brain-inspired/` |
| adversarial-reviewer (Round 1, Axis T 문헌) | a60f877c6ca18a5c0 | T | `outputs/agents/adversarial-reviewer/` |

## Stage 2 추가 실행

| 역할 | agent ID | 산출물 |
|---|---|---|
| adversarial-reviewer (인용 표본 검증 25편, 새 인스턴스) | ae6e9472df114224e | `outputs/literature/verification_sample.md` |

재점검은 위 표의 brain-inspired, emotion-theory 인스턴스와 Stage 1의 dataset-auditor (NSD) 인스턴스를 SendMessage로 재개해 수행했다.

## Stage 3 (2026-11-12)

* 10개 연구 에이전트는 위 Stage 2 Round 1의 같은 ID를 SendMessage로 재개해 Round 2 제안, 받은 제안 응답, Round 3 검토를 수행했다.
* Round 4는 frontier-ai, brain-inspired, geometry-info, llm-semantics, emotion-theory를 같은 방식으로 재개해 수행했다.
* adversarial-reviewer의 Round 2 응답(EF-P6, FA-P8, SN-P7, GC-P3, LS-P5와 검증 요건 v2)은 Round 1 인스턴스(a60f877c6ca18a5c0)를 재개해 받았다.

| 역할 | agent ID | 산출물 |
|---|---|---|
| adversarial-reviewer (상위 10개 독립 검토, 새 인스턴스. 선정 정정 후 ET-P4, EF-P4 추가 검토도 같은 인스턴스를 재개) | ad1b525711dd544aa | `outputs/agents/adversarial-reviewer/round3_top10_review.md`, `round3_top10_addendum.md` |

## Stage 4 (2026-11-12)

* 질문 카드 작성과 수정은 Stage 2의 같은 연구 에이전트 ID를 재개해 수행했다.
  * geometry-info: RQ-01, 03
  * llm-semantics: RQ-08, 14
  * encoding-foundation: RQ-10
  * frontier-ai: RQ-15
  * multimodal-dynamics: RQ-33, 60
  * systems-neuro: RQ-32
  * emotion-theory: RQ-44
* Horikawa 사실 확인은 Stage 1의 dataset-auditor(Horikawa, abd7d0ed9ea164848)를 재개했다.

| 역할 | agent ID | 산출물 |
|---|---|---|
| adversarial-reviewer (독립 P6 채점, Coordinator 점수 미열람. 같은 인스턴스가 이어서 선행연구 중복 감사) | ae1b7a2f9497fc052 | `outputs/evaluation/scores_reviewer.csv`, `reviewer_notes.md`, `prior_overlap_audit.md` |
| adversarial-reviewer (카드 검토 묶음 A) | ab40f5ef611bb5025 | `outputs/evaluation/card_review_A.md` |
| adversarial-reviewer (카드 검토 묶음 B) | aa91a97af3b14b90e | `outputs/evaluation/card_review_B.md` |
| adversarial-reviewer (최종 인용 검증, 새 인스턴스) | a0f758bf975ed612c | `outputs/evaluation/final_citation_check.md` |

## 재탐색 라운드 (2026-11-12, Stage 4 이후 사용자 지시)

탐색은 Stage 2 Round 1의 같은 인스턴스 7개를 SendMessage로 재개해 수행했다. 평가는 새 adversarial-reviewer 인스턴스가 Coordinator 점수를 보지 않고 채점했고, 같은 인스턴스가 이어서 선행연구 중복 감사를 했다.

| 역할 | agent ID | 산출물 |
|---|---|---|
| vision-decoding (D2 주담당, 출발점 RQ-53) | ac253b97bb080c9b1 | `outputs/agents/vision-decoding/revision_round.md` |
| encoding-foundation (출발점 RQ-51) | a1e352d659ed60d8c | `outputs/agents/encoding-foundation/revision_round.md` |
| brain-inspired (D1 주담당, 출발점 RQ-54, 56) | a33e66f5a273664cb | `outputs/agents/brain-inspired/revision_round.md` |
| frontier-ai (출발점 RQ-55, 19) | aab100cf89288f887 | `outputs/agents/frontier-ai/revision_round.md` |
| geometry-info (출발점 RQ-04) | ae216f8ca9181b4e7 | `outputs/agents/geometry-info/revision_round.md` |
| emotion-theory (출발점 RQ-22, 12) | a85c474967cad849e | `outputs/agents/emotion-theory/revision_round.md` |
| multimodal-dynamics (D3, 출발점 RQ-05) | ab3f5d7c66dfe0bff | `outputs/agents/multimodal-dynamics/revision_round.md` |
| adversarial-reviewer (독립 채점, Coordinator 점수 미열람. 이어서 선행연구 중복 감사) | a6168bf8e2364c8ad | `outputs/revision/scores_reviewer.csv`, `reviewer_notes.md`, `prior_overlap_audit.md` |

## Stage 1 (참고, general-purpose 에이전트가 정의 파일을 읽고 수행)

| 역할 | agent ID | 산출물 |
|---|---|---|
| dataset-auditor (Horikawa) | abd7d0ed9ea164848 | `outputs/stage1/dataset_Horikawa.md` |
| dataset-auditor (Emo-FilM) | afde86f079676036f | `outputs/stage1/dataset_EmoFilM.md` |
| dataset-auditor (Spacetop) | afa356234d5b13c0c | `outputs/stage1/dataset_Spacetop.md` |
| dataset-auditor (NSD) | a49d484778e473def | `outputs/stage1/dataset_NSD.md` |
| adversarial-reviewer (Stage 1 사실 검증) | a5b3ba325b0b0801e | `outputs/agents/adversarial-reviewer/stage1_audit.md` |
