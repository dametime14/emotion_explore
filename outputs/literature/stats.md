# Literature Statistics (Deliverable C)

* 생성: `python3 -I outputs/literature/merge.py` (자동 생성 파일, 직접 고치지 말 것)
* 입력 레코드: 714개 (파싱 오류 0개), 입력 파일: `outputs/agents/*/literature*.jsonl`
* 원자료 기준 verified 표기: 702개, 미검증(search_index 등): 12개
* 중복 제거 후 고유 논문: **521편**
* **verified 고유 논문: 516편** (식별자 경로 doi.org / crossref / pubmed / arxiv / openreview / publisher로 확인된 것만)
* 미검증 고유 논문: 5편 (verified 집계에서 제외, DB에는 `verified=False`로 남김)

## Axis별 verified 논문 수 (한 논문이 여러 Axis에 속할 수 있음)

| Axis | verified | 전체(미검증 포함) |
|---|---|---|
| A | 173 | 174 |
| B | 71 | 72 |
| C | 79 | 80 |
| D | 115 | 115 |
| E | 150 | 150 |
| F | 76 | 77 |
| G | 51 | 52 |
| H | 83 | 87 |
| I | 108 | 110 |
| J | 53 | 54 |
| K | 104 | 105 |
| L | 56 | 57 |
| M | 66 | 66 |
| N | 117 | 118 |
| O | 90 | 90 |
| P | 48 | 49 |
| Q | 103 | 103 |
| R | 50 | 50 |
| S | 57 | 59 |
| T | 73 | 74 |
| U | 13 | 13 |
| V | 16 | 16 |
| W | 30 | 30 |

## 연도 분포 (verified)

| 연도 | 편수 |
|---|---|
| 1959 | 1 |
| 1993 | 1 |
| 1995 | 1 |
| 2003 | 1 |
| 2004 | 1 |
| 2005 | 4 |
| 2006 | 2 |
| 2007 | 1 |
| 2009 | 1 |
| 2010 | 4 |
| 2011 | 1 |
| 2012 | 3 |
| 2013 | 1 |
| 2014 | 13 |
| 2015 | 11 |
| 2016 | 15 |
| 2017 | 27 |
| 2018 | 16 |
| 2019 | 28 |
| 2020 | 30 |
| 2021 | 33 |
| 2022 | 33 |
| 2023 | 60 |
| 2024 | 66 |
| 2025 | 96 |
| 2026 | 66 |

## discussion_read 분포 (verified)

| discussion_read | 편수 |
|---|---|
| full_text | 232 |
| abstract_only | 224 |
| search_summary | 17 |
| no | 43 |

## 담당 에이전트별 verified 고유 논문 수 (중복 논문은 기여한 모든 에이전트에 집계)

| 에이전트 | 편수 |
|---|---|
| multimodal-dynamics | 76 |
| brain-inspired | 72 |
| adversarial-reviewer | 63 |
| frontier-ai | 63 |
| geometry-info | 60 |
| llm-semantics | 60 |
| emotion-theory | 57 |
| generative-counterfactual | 55 |
| dataset-auditor | 54 |
| systems-neuro | 52 |
| encoding-foundation | 49 |
| vision-decoding | 38 |
| coordinator | 8 |

## 에이전트별 원 레코드 수 (중복 제거 전, 미검증 포함)

| 에이전트 폴더 | 편수 |
|---|---|
| multimodal-dynamics | 76 |
| brain-inspired | 73 |
| adversarial-reviewer | 63 |
| frontier-ai | 63 |
| llm-semantics | 61 |
| geometry-info | 60 |
| dataset-auditor | 57 |
| emotion-theory | 57 |
| generative-counterfactual | 55 |
| systems-neuro | 53 |
| encoding-foundation | 50 |
| vision-decoding | 38 |
| coordinator | 8 |

## future_directions의 already_done 분포 (verified 논문)

| already_done | 편수 |
|---|---|
| no | 394 |
| partially | 283 |
| yes | 11 |
| 미확인(검색하지 | 2 |
