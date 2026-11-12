# Literature Statistics (Deliverable C)

* 생성: `python3 -I outputs/literature/merge.py` (자동 생성 파일, 직접 고치지 말 것)
* 입력 레코드: 57개 (파싱 오류 0개), 입력 파일: `outputs/agents/*/literature*.jsonl`
* 원자료 기준 verified 표기: 38개, 미검증(search_index 등): 19개
* 중복 제거 후 고유 논문: **56편**
* **verified 고유 논문: 38편** (식별자 경로 doi.org / crossref / pubmed / arxiv / openreview / publisher로 확인된 것만)
* 미검증 고유 논문: 18편 (verified 집계에서 제외, DB에는 `verified=False`로 남김)

## Axis별 verified 논문 수 (한 논문이 여러 Axis에 속할 수 있음)

| Axis | verified | 전체(미검증 포함) |
|---|---|---|
| A | 20 | 27 |
| B | 12 | 14 |
| C | 3 | 4 |
| D | 5 | 6 |
| E | 12 | 15 |
| F | 9 | 10 |
| G | 5 | 11 |
| H | 10 | 14 |
| I | 9 | 14 |
| J | 1 | 2 |
| K | 10 | 14 |
| L | 2 | 5 |
| M | 4 | 11 |
| N | 4 | 5 |
| O | 6 | 7 |
| P | 1 | 2 |
| Q | 15 | 18 |
| R | 1 | 1 |
| S | 4 | 7 |
| T | 2 | 3 |

## 연도 분포 (verified)

| 연도 | 편수 |
|---|---|
| 2017 | 1 |
| 2019 | 1 |
| 2020 | 1 |
| 2022 | 4 |
| 2023 | 4 |
| 2024 | 6 |
| 2025 | 10 |
| 2026 | 11 |

## discussion_read 분포 (verified)

| discussion_read | 편수 |
|---|---|
| full_text | 21 |
| abstract_only | 15 |
| no | 2 |

## 담당 에이전트별 verified 고유 논문 수 (중복 논문은 기여한 모든 에이전트에 집계)

| 에이전트 | 편수 |
|---|---|
| dataset-auditor | 38 |

## 에이전트별 원 레코드 수 (중복 제거 전, 미검증 포함)

| 에이전트 폴더 | 편수 |
|---|---|
| dataset-auditor | 57 |

## future_directions의 already_done 분포 (verified 논문)

| already_done | 편수 |
|---|---|
| no | 28 |
| partially | 15 |
| 미확인 | 15 |
