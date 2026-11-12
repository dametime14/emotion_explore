# Literature Statistics (Deliverable C)

* 생성: `python3 -I outputs/literature/merge.py` (자동 생성 파일, 직접 고치지 말 것)
* 입력 레코드: 675개 (파싱 오류 0개), 입력 파일: `outputs/agents/*/literature*.jsonl`
* 원자료 기준 verified 표기: 663개, 미검증(search_index 등): 12개
* 중복 제거 후 고유 논문: **490편**
* **verified 고유 논문: 485편** (식별자 경로 doi.org / crossref / pubmed / arxiv / openreview / publisher로 확인된 것만)
* 미검증 고유 논문: 5편 (verified 집계에서 제외, DB에는 `verified=False`로 남김)

## Axis별 verified 논문 수 (한 논문이 여러 Axis에 속할 수 있음)

| Axis | verified | 전체(미검증 포함) |
|---|---|---|
| A | 169 | 170 |
| B | 62 | 63 |
| C | 75 | 76 |
| D | 110 | 110 |
| E | 142 | 142 |
| F | 71 | 72 |
| G | 50 | 51 |
| H | 79 | 83 |
| I | 102 | 104 |
| J | 53 | 54 |
| K | 96 | 97 |
| L | 56 | 57 |
| M | 62 | 62 |
| N | 112 | 113 |
| O | 89 | 89 |
| P | 47 | 48 |
| Q | 91 | 91 |
| R | 50 | 50 |
| S | 56 | 58 |
| T | 70 | 71 |
| U | 13 | 13 |
| V | 16 | 16 |
| W | 27 | 27 |

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
| 2012 | 2 |
| 2013 | 1 |
| 2014 | 7 |
| 2015 | 10 |
| 2016 | 15 |
| 2017 | 26 |
| 2018 | 16 |
| 2019 | 27 |
| 2020 | 29 |
| 2021 | 31 |
| 2022 | 32 |
| 2023 | 57 |
| 2024 | 65 |
| 2025 | 90 |
| 2026 | 65 |

## discussion_read 분포 (verified)

| discussion_read | 편수 |
|---|---|
| full_text | 226 |
| abstract_only | 202 |
| search_summary | 16 |
| no | 41 |

## 담당 에이전트별 verified 고유 논문 수 (중복 논문은 기여한 모든 에이전트에 집계)

| 에이전트 | 편수 |
|---|---|
| brain-inspired | 72 |
| adversarial-reviewer | 63 |
| multimodal-dynamics | 63 |
| frontier-ai | 57 |
| llm-semantics | 56 |
| generative-counterfactual | 55 |
| dataset-auditor | 54 |
| geometry-info | 54 |
| emotion-theory | 52 |
| encoding-foundation | 49 |
| systems-neuro | 48 |
| vision-decoding | 38 |
| coordinator | 7 |

## 에이전트별 원 레코드 수 (중복 제거 전, 미검증 포함)

| 에이전트 폴더 | 편수 |
|---|---|
| brain-inspired | 73 |
| adversarial-reviewer | 63 |
| multimodal-dynamics | 63 |
| dataset-auditor | 57 |
| frontier-ai | 57 |
| llm-semantics | 57 |
| generative-counterfactual | 55 |
| geometry-info | 54 |
| emotion-theory | 52 |
| encoding-foundation | 50 |
| systems-neuro | 49 |
| vision-decoding | 38 |
| coordinator | 7 |

## future_directions의 already_done 분포 (verified 논문)

| already_done | 편수 |
|---|---|
| no | 390 |
| partially | 276 |
| yes | 11 |
