# Literature Statistics (Deliverable C)

* 생성: `python3 -I outputs/literature/merge.py` (자동 생성 파일, 직접 고치지 말 것)
* 입력 레코드: 898개 (파싱 오류 0개), 입력 파일: `outputs/agents/*/literature*.jsonl`
* 원자료 기준 verified 표기: 884개, 미검증(search_index 등): 14개
* 중복 제거 후 고유 논문: **626편**
* **verified 고유 논문: 621편** (식별자 경로 doi.org / crossref / pubmed / arxiv / openreview / publisher로 확인된 것만)
* 미검증 고유 논문: 5편 (verified 집계에서 제외, DB에는 `verified=False`로 남김)

## Axis별 verified 논문 수 (한 논문이 여러 Axis에 속할 수 있음)

| Axis | verified | 전체(미검증 포함) |
|---|---|---|
| A | 207 | 207 |
| B | 96 | 97 |
| C | 88 | 89 |
| D | 127 | 127 |
| E | 170 | 170 |
| F | 101 | 101 |
| G | 62 | 63 |
| H | 105 | 108 |
| I | 124 | 126 |
| J | 67 | 68 |
| K | 127 | 129 |
| L | 63 | 64 |
| M | 81 | 81 |
| N | 143 | 144 |
| O | 92 | 92 |
| P | 51 | 52 |
| Q | 109 | 109 |
| R | 55 | 55 |
| S | 77 | 78 |
| T | 90 | 91 |
| U | 17 | 17 |
| V | 16 | 16 |
| W | 35 | 35 |

## 연도 분포 (verified)

| 연도 | 편수 |
|---|---|
| 1959 | 1 |
| 1991 | 1 |
| 1993 | 1 |
| 1995 | 1 |
| 2000 | 1 |
| 2003 | 3 |
| 2004 | 1 |
| 2005 | 5 |
| 2006 | 3 |
| 2007 | 1 |
| 2008 | 2 |
| 2009 | 1 |
| 2010 | 6 |
| 2011 | 4 |
| 2012 | 4 |
| 2013 | 5 |
| 2014 | 14 |
| 2015 | 13 |
| 2016 | 15 |
| 2017 | 31 |
| 2018 | 18 |
| 2019 | 35 |
| 2020 | 34 |
| 2021 | 39 |
| 2022 | 42 |
| 2023 | 74 |
| 2024 | 77 |
| 2025 | 110 |
| 2026 | 79 |

## discussion_read 분포 (verified)

| discussion_read | 편수 |
|---|---|
| full_text | 239 |
| abstract_only | 302 |
| search_summary | 21 |
| no | 59 |

## 담당 에이전트별 verified 고유 논문 수 (중복 논문은 기여한 모든 에이전트에 집계)

| 에이전트 | 편수 |
|---|---|
| adversarial-reviewer | 116 |
| brain-inspired | 105 |
| multimodal-dynamics | 94 |
| geometry-info | 77 |
| frontier-ai | 76 |
| emotion-theory | 67 |
| encoding-foundation | 63 |
| llm-semantics | 60 |
| generative-counterfactual | 55 |
| vision-decoding | 55 |
| dataset-auditor | 54 |
| systems-neuro | 52 |
| coordinator | 16 |

## 에이전트별 원 레코드 수 (중복 제거 전, 미검증 포함)

| 에이전트 폴더 | 편수 |
|---|---|
| adversarial-reviewer | 118 |
| brain-inspired | 105 |
| multimodal-dynamics | 94 |
| geometry-info | 78 |
| frontier-ai | 76 |
| emotion-theory | 67 |
| encoding-foundation | 63 |
| llm-semantics | 61 |
| dataset-auditor | 57 |
| generative-counterfactual | 55 |
| vision-decoding | 55 |
| systems-neuro | 53 |
| coordinator | 16 |

## future_directions의 already_done 분포 (verified 논문)

| already_done | 편수 |
|---|---|
| no | 403 |
| partially | 288 |
| yes | 11 |
| 미확인(검색하지 | 2 |
| 미확인(이번 | 1 |
