# Stage 1 준비: 우리 환경 정보 빈칸 목록

기준일: 2026-11-12
대상 파일: `reference/datasets_and_resources.md` 1절 "우리 환경"

Stage 1 시작 시점에 1절의 모든 칸이 템플릿 상태(`[채워 넣기: ...]`)로 비어 있었다. 데이터 경로가 적혀 있지 않으므로 실제 폴더 구조(파일 종류, 자극 파일 존재 여부)는 직접 확인하지 못했다. 모든 감사 보고서에서 "우리 환경" 관련 항목은 **미확인**으로 처리했다.

| 칸 | 상태 | Stage 1에 미친 영향 |
|---|---|---|
| 데이터 위치 (Horikawa, Emo-FilM, Spacetop, NSD) | 비어 있음 | 실제 파일 구조 확인 불가. G1, G2는 "공개 경로 기준"으로만 판정 |
| 원본 자극 파일 보유 여부 | 비어 있음 | G1의 "우리 환경 보유" 판정 불가. 공개 경로 기준 판정과 분리해 기록 |
| 이미 추출해 둔 feature / embedding | 비어 있음 | 미리 계산된 feature로 G1 제약을 우회할 수 있는지 판단 불가 |
| 계산 자원 | 비어 있음 | Stage 4 Pilot 실행 가능성 판단에 필요 |
| 사용 가능한 pretrained checkpoint | 비어 있음 | Stage 2 이후 모델 선택에 필요 |
| 제약 (마감, 데이터 사용 동의 범위) | 비어 있음 | DUA 범위에 따라 파생 라벨 생성, 재배포 가능 여부가 달라짐 |

## 실행 환경 관련 기록 (사실)

* 이 작업은 Claude Code 원격 컨테이너에서 실행되었다. 사용자 로컬 데이터 폴더(`claude --add-dir`)는 연결되지 않았다.
* 컨테이너 셸의 외부 HTTP 접근은 egress proxy 정책으로 대부분 차단되었다 (doi.org, data.mendeley.com, openneuro.org, api.crossref.org, arxiv.org 등 curl 접속 거부). 문헌과 저장소 확인은 WebSearch, WebFetch, PubMed 도구로 수행했다.
* `.claude/agents/`의 커스텀 에이전트 정의는 세션 시작 이후에 저장소에 추가되어 에이전트 타입으로 등록되지 않았다. 그래서 각 역할은 `general-purpose` 에이전트가 `CLAUDE.md`와 해당 `.claude/agents/<이름>.md`를 직접 읽고 그 지침을 따르는 방식으로 실행했다. 다음 세션부터는 저장소 루트에서 시작하면 커스텀 타입이 등록될 것으로 예상되지만, 확인되지 않았다.
