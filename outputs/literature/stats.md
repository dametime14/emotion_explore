# Literature Statistics (Deliverable C)

* 생성: `python3 -I outputs/literature/merge.py` (자동 생성 파일, 직접 고치지 말 것)
* 입력 레코드: 698개 (파싱 오류 0개), 입력 파일: `outputs/agents/*/literature*.jsonl`
* 원자료 기준 verified 표기: 686개, 미검증(search_index 등): 12개
* 중복 제거 후 고유 논문: **509편**
* **verified 고유 논문: 504편** (식별자 경로 doi.org / crossref / pubmed / arxiv / openreview / publisher로 확인된 것만)
* 미검증 고유 논문: 5편 (verified 집계에서 제외, DB에는 `verified=False`로 남김)

## Axis별 verified 논문 수 (한 논문이 여러 Axis에 속할 수 있음)

| Axis | verified | 전체(미검증 포함) |
|---|---|---|
| A | 171 | 172 |
| B | 68 | 69 |
| C | 78 | 79 |
| D | 115 | 115 |
| E | 148 | 148 |
| F | 73 | 74 |
| G | 50 | 51 |
| H | 82 | 86 |
| I | 108 | 110 |
| J | 53 | 54 |
| K | 99 | 100 |
| L | 56 | 57 |
| M | 63 | 63 |
| N | 117 | 118 |
| O | 89 | 89 |
| P | 47 | 48 |
| Q | 94 | 94 |
| R | 50 | 50 |
| S | 57 | 59 |
| T | 72 | 73 |
| U | 13 | 13 |
| V | 16 | 16 |
| W | 30 | 30 |

## 연도 분포 (verified)

| 연도 | 편수 |
|---|---|
| 1959 | 1 |
| 1993 | 1 |
| 2003 | 1 |
| 2004 | 1 |
| 2005 | 1 |
| 2006 | 2 |
| 2007 | 1 |
| 2009 | 1 |
| 2010 | 4 |
| 2011 | 1 |
| 2012 | 2 |
| 2013 | 1 |
| 2014 | 10 |
| 2015 | 10 |
| 2016 | 15 |
| 2017 | 26 |
| 2018 | 16 |
| 2019 | 28 |
| 2020 | 30 |
| 2021 | 32 |
| 2022 | 33 |
| 2023 | 60 |
| 2024 | 66 |
| 2025 | 95 |
| 2026 | 66 |

## discussion_read 분포 (verified)

| discussion_read | 편수 |
|---|---|
| full_text | 230 |
| abstract_only | 216 |
| search_summary | 16 |
| no | 42 |

## 담당 에이전트별 verified 고유 논문 수 (중복 논문은 기여한 모든 에이전트에 집계)

| 에이전트 | 편수 |
|---|---|
| brain-inspired | 72 |
| multimodal-dynamics | 71 |
| adversarial-reviewer | 63 |
| frontier-ai | 62 |
| llm-semantics | 58 |
| emotion-theory | 56 |
| generative-counterfactual | 55 |
| dataset-auditor | 54 |
| geometry-info | 54 |
| systems-neuro | 52 |
| encoding-foundation | 49 |
| vision-decoding | 38 |
| coordinator | 7 |

## 에이전트별 원 레코드 수 (중복 제거 전, 미검증 포함)

| 에이전트 폴더 | 편수 |
|---|---|
| brain-inspired | 73 |
| multimodal-dynamics | 71 |
| adversarial-reviewer | 63 |
| frontier-ai | 62 |
| llm-semantics | 59 |
| dataset-auditor | 57 |
| emotion-theory | 56 |
| generative-counterfactual | 55 |
| geometry-info | 54 |
| systems-neuro | 53 |
| encoding-foundation | 50 |
| vision-decoding | 38 |
| coordinator | 7 |

## future_directions의 already_done 분포 (verified 논문)

| already_done | 편수 |
|---|---|
| no | 393 |
| partially | 282 |
| yes | 11 |
