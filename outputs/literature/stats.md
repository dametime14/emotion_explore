# Literature Statistics (Deliverable C)

* 생성: `python3 -I outputs/literature/merge.py` (자동 생성 파일, 직접 고치지 말 것)
* 입력 레코드: 511개 (파싱 오류 0개), 입력 파일: `outputs/agents/*/literature*.jsonl`
* 원자료 기준 verified 표기: 491개, 미검증(search_index 등): 20개
* 중복 제거 후 고유 논문: **377편**
* **verified 고유 논문: 365편** (식별자 경로 doi.org / crossref / pubmed / arxiv / openreview / publisher로 확인된 것만)
* 미검증 고유 논문: 12편 (verified 집계에서 제외, DB에는 `verified=False`로 남김)

## Axis별 verified 논문 수 (한 논문이 여러 Axis에 속할 수 있음)

| Axis | verified | 전체(미검증 포함) |
|---|---|---|
| A | 120 | 124 |
| B | 47 | 50 |
| C | 54 | 56 |
| D | 84 | 84 |
| E | 92 | 93 |
| F | 59 | 59 |
| G | 43 | 46 |
| H | 68 | 72 |
| I | 81 | 85 |
| J | 41 | 42 |
| K | 75 | 76 |
| L | 49 | 50 |
| M | 44 | 49 |
| N | 90 | 91 |
| O | 75 | 75 |
| P | 42 | 42 |
| Q | 74 | 76 |
| R | 45 | 45 |
| S | 53 | 54 |
| T | 66 | 67 |

## 연도 분포 (verified)

| 연도 | 편수 |
|---|---|
| 1993 | 1 |
| 2006 | 1 |
| 2007 | 1 |
| 2010 | 1 |
| 2011 | 1 |
| 2014 | 2 |
| 2015 | 7 |
| 2016 | 10 |
| 2017 | 19 |
| 2018 | 11 |
| 2019 | 23 |
| 2020 | 22 |
| 2021 | 23 |
| 2022 | 25 |
| 2023 | 44 |
| 2024 | 51 |
| 2025 | 71 |
| 2026 | 52 |

## discussion_read 분포 (verified)

| discussion_read | 편수 |
|---|---|
| full_text | 215 |
| abstract_only | 124 |
| search_summary | 3 |
| no | 23 |

## 담당 에이전트별 verified 고유 논문 수 (중복 논문은 기여한 모든 에이전트에 집계)

| 에이전트 | 편수 |
|---|---|
| multimodal-dynamics | 51 |
| brain-inspired | 50 |
| dataset-auditor | 45 |
| generative-counterfactual | 45 |
| geometry-info | 45 |
| systems-neuro | 42 |
| encoding-foundation | 41 |
| llm-semantics | 41 |
| emotion-theory | 40 |
| adversarial-reviewer | 38 |
| frontier-ai | 32 |
| vision-decoding | 28 |

## 에이전트별 원 레코드 수 (중복 제거 전, 미검증 포함)

| 에이전트 폴더 | 편수 |
|---|---|
| dataset-auditor | 57 |
| multimodal-dynamics | 51 |
| brain-inspired | 50 |
| generative-counterfactual | 45 |
| geometry-info | 45 |
| llm-semantics | 42 |
| systems-neuro | 42 |
| encoding-foundation | 41 |
| emotion-theory | 40 |
| adversarial-reviewer | 38 |
| frontier-ai | 32 |
| vision-decoding | 28 |

## future_directions의 already_done 분포 (verified 논문)

| already_done | 편수 |
|---|---|
| no | 366 |
| partially | 239 |
| unknown | 23 |
| 미확인 | 14 |
| yes | 10 |
