# Literature Statistics (Deliverable C)

* 생성: `python3 -I outputs/literature/merge.py` (자동 생성 파일, 직접 고치지 말 것)
* 입력 레코드: 789개 (파싱 오류 0개), 입력 파일: `outputs/agents/*/literature*.jsonl`
* 원자료 기준 verified 표기: 777개, 미검증(search_index 등): 12개
* 중복 제거 후 고유 논문: **576편**
* **verified 고유 논문: 571편** (식별자 경로 doi.org / crossref / pubmed / arxiv / openreview / publisher로 확인된 것만)
* 미검증 고유 논문: 5편 (verified 집계에서 제외, DB에는 `verified=False`로 남김)

## Axis별 verified 논문 수 (한 논문이 여러 Axis에 속할 수 있음)

| Axis | verified | 전체(미검증 포함) |
|---|---|---|
| A | 196 | 197 |
| B | 82 | 83 |
| C | 84 | 85 |
| D | 118 | 118 |
| E | 163 | 163 |
| F | 86 | 87 |
| G | 54 | 55 |
| H | 90 | 94 |
| I | 119 | 121 |
| J | 63 | 64 |
| K | 114 | 115 |
| L | 60 | 61 |
| M | 77 | 77 |
| N | 126 | 127 |
| O | 92 | 92 |
| P | 50 | 51 |
| Q | 109 | 109 |
| R | 54 | 54 |
| S | 61 | 63 |
| T | 76 | 77 |
| U | 17 | 17 |
| V | 16 | 16 |
| W | 31 | 31 |

## 연도 분포 (verified)

| 연도 | 편수 |
|---|---|
| 1959 | 1 |
| 1993 | 1 |
| 1995 | 1 |
| 2000 | 1 |
| 2003 | 2 |
| 2004 | 1 |
| 2005 | 5 |
| 2006 | 3 |
| 2007 | 1 |
| 2008 | 1 |
| 2009 | 1 |
| 2010 | 5 |
| 2011 | 3 |
| 2012 | 3 |
| 2013 | 4 |
| 2014 | 14 |
| 2015 | 13 |
| 2016 | 15 |
| 2017 | 29 |
| 2018 | 17 |
| 2019 | 33 |
| 2020 | 32 |
| 2021 | 36 |
| 2022 | 37 |
| 2023 | 67 |
| 2024 | 73 |
| 2025 | 105 |
| 2026 | 67 |

## discussion_read 분포 (verified)

| discussion_read | 편수 |
|---|---|
| full_text | 238 |
| abstract_only | 262 |
| search_summary | 20 |
| no | 51 |

## 담당 에이전트별 verified 고유 논문 수 (중복 논문은 기여한 모든 에이전트에 집계)

| 에이전트 | 편수 |
|---|---|
| multimodal-dynamics | 94 |
| brain-inspired | 78 |
| frontier-ai | 76 |
| geometry-info | 73 |
| adversarial-reviewer | 66 |
| encoding-foundation | 62 |
| emotion-theory | 61 |
| llm-semantics | 60 |
| generative-counterfactual | 55 |
| dataset-auditor | 54 |
| systems-neuro | 52 |
| vision-decoding | 42 |
| coordinator | 8 |

## 에이전트별 원 레코드 수 (중복 제거 전, 미검증 포함)

| 에이전트 폴더 | 편수 |
|---|---|
| multimodal-dynamics | 94 |
| brain-inspired | 79 |
| frontier-ai | 76 |
| geometry-info | 74 |
| adversarial-reviewer | 66 |
| encoding-foundation | 63 |
| emotion-theory | 61 |
| llm-semantics | 61 |
| dataset-auditor | 57 |
| generative-counterfactual | 55 |
| systems-neuro | 53 |
| vision-decoding | 42 |
| coordinator | 8 |

## future_directions의 already_done 분포 (verified 논문)

| already_done | 편수 |
|---|---|
| no | 402 |
| partially | 287 |
| yes | 11 |
| 미확인(검색하지 | 2 |
| 미확인(이번 | 1 |
