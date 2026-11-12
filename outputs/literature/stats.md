# Literature Statistics (Deliverable C)

* 생성: `python3 -I outputs/literature/merge.py` (자동 생성 파일, 직접 고치지 말 것)
* 입력 레코드: 517개 (파싱 오류 0개), 입력 파일: `outputs/agents/*/literature*.jsonl`
* 원자료 기준 verified 표기: 508개, 미검증(search_index 등): 9개
* 중복 제거 후 고유 논문: **381편**
* **verified 고유 논문: 377편** (식별자 경로 doi.org / crossref / pubmed / arxiv / openreview / publisher로 확인된 것만)
* 미검증 고유 논문: 4편 (verified 집계에서 제외, DB에는 `verified=False`로 남김)

## Axis별 verified 논문 수 (한 논문이 여러 Axis에 속할 수 있음)

| Axis | verified | 전체(미검증 포함) |
|---|---|---|
| A | 127 | 127 |
| B | 49 | 50 |
| C | 55 | 56 |
| D | 86 | 86 |
| E | 97 | 97 |
| F | 59 | 59 |
| G | 44 | 46 |
| H | 70 | 72 |
| I | 84 | 86 |
| J | 41 | 42 |
| K | 75 | 76 |
| L | 49 | 50 |
| M | 48 | 49 |
| N | 94 | 95 |
| O | 75 | 75 |
| P | 42 | 42 |
| Q | 76 | 76 |
| R | 45 | 45 |
| S | 53 | 54 |
| T | 67 | 67 |

## 연도 분포 (verified)

| 연도 | 편수 |
|---|---|
| 1993 | 1 |
| 2006 | 1 |
| 2007 | 1 |
| 2010 | 1 |
| 2011 | 1 |
| 2014 | 3 |
| 2015 | 8 |
| 2016 | 11 |
| 2017 | 19 |
| 2018 | 11 |
| 2019 | 24 |
| 2020 | 23 |
| 2021 | 23 |
| 2022 | 25 |
| 2023 | 46 |
| 2024 | 52 |
| 2025 | 75 |
| 2026 | 52 |

## discussion_read 분포 (verified)

| discussion_read | 편수 |
|---|---|
| full_text | 215 |
| abstract_only | 128 |
| search_summary | 9 |
| no | 25 |

## 담당 에이전트별 verified 고유 논문 수 (중복 논문은 기여한 모든 에이전트에 집계)

| 에이전트 | 편수 |
|---|---|
| brain-inspired | 56 |
| dataset-auditor | 53 |
| multimodal-dynamics | 51 |
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
| brain-inspired | 56 |
| multimodal-dynamics | 51 |
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
| no | 377 |
| partially | 268 |
| yes | 11 |
