# Literature Statistics (Deliverable C)

* 생성: `python3 -I outputs/literature/merge.py` (자동 생성 파일, 직접 고치지 말 것)
* 입력 레코드: 646개 (파싱 오류 0개), 입력 파일: `outputs/agents/*/literature*.jsonl`
* 원자료 기준 verified 표기: 634개, 미검증(search_index 등): 12개
* 중복 제거 후 고유 논문: **479편**
* **verified 고유 논문: 474편** (식별자 경로 doi.org / crossref / pubmed / arxiv / openreview / publisher로 확인된 것만)
* 미검증 고유 논문: 5편 (verified 집계에서 제외, DB에는 `verified=False`로 남김)

## Axis별 verified 논문 수 (한 논문이 여러 Axis에 속할 수 있음)

| Axis | verified | 전체(미검증 포함) |
|---|---|---|
| A | 162 | 163 |
| B | 60 | 61 |
| C | 71 | 72 |
| D | 105 | 105 |
| E | 135 | 135 |
| F | 68 | 69 |
| G | 50 | 51 |
| H | 77 | 81 |
| I | 98 | 100 |
| J | 53 | 54 |
| K | 95 | 96 |
| L | 56 | 57 |
| M | 60 | 60 |
| N | 112 | 113 |
| O | 86 | 86 |
| P | 47 | 48 |
| Q | 89 | 89 |
| R | 50 | 50 |
| S | 56 | 58 |
| T | 70 | 71 |
| U | 11 | 11 |
| V | 15 | 15 |
| W | 25 | 25 |

## 연도 분포 (verified)

| 연도 | 편수 |
|---|---|
| 1959 | 1 |
| 1993 | 1 |
| 2003 | 1 |
| 2005 | 1 |
| 2006 | 1 |
| 2007 | 1 |
| 2009 | 1 |
| 2010 | 4 |
| 2011 | 1 |
| 2012 | 1 |
| 2013 | 1 |
| 2014 | 7 |
| 2015 | 10 |
| 2016 | 14 |
| 2017 | 24 |
| 2018 | 16 |
| 2019 | 27 |
| 2020 | 28 |
| 2021 | 29 |
| 2022 | 31 |
| 2023 | 56 |
| 2024 | 64 |
| 2025 | 89 |
| 2026 | 65 |

## discussion_read 분포 (verified)

| discussion_read | 편수 |
|---|---|
| full_text | 226 |
| abstract_only | 193 |
| search_summary | 17 |
| no | 38 |

## 담당 에이전트별 verified 고유 논문 수 (중복 논문은 기여한 모든 에이전트에 집계)

| 에이전트 | 편수 |
|---|---|
| brain-inspired | 72 |
| multimodal-dynamics | 63 |
| frontier-ai | 57 |
| llm-semantics | 56 |
| generative-counterfactual | 55 |
| dataset-auditor | 54 |
| geometry-info | 54 |
| emotion-theory | 52 |
| encoding-foundation | 49 |
| systems-neuro | 48 |
| adversarial-reviewer | 38 |
| vision-decoding | 38 |
| coordinator | 3 |

## 에이전트별 원 레코드 수 (중복 제거 전, 미검증 포함)

| 에이전트 폴더 | 편수 |
|---|---|
| brain-inspired | 73 |
| multimodal-dynamics | 63 |
| dataset-auditor | 57 |
| frontier-ai | 57 |
| llm-semantics | 57 |
| generative-counterfactual | 55 |
| geometry-info | 54 |
| emotion-theory | 52 |
| encoding-foundation | 50 |
| systems-neuro | 49 |
| adversarial-reviewer | 38 |
| vision-decoding | 38 |
| coordinator | 3 |

## future_directions의 already_done 분포 (verified 논문)

| already_done | 편수 |
|---|---|
| no | 388 |
| partially | 276 |
| yes | 11 |
