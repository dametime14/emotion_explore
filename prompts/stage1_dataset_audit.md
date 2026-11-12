# Stage 1: Dataset Forensic Audit

너는 이 프로젝트의 Coordinator다. 이번 실행에서는 **Stage 1만** 수행하고 멈춘다. 산출물은 Deliverable A다.

## 0. 준비
1. `reference/datasets_and_resources.md`와 `reference/starting_papers.md`를 읽는다.
2. `reference/datasets_and_resources.md` 1절(우리 환경)에 비어 있는 칸이 있으면 목록으로 정리한다. 데이터 경로가 적혀 있고 접근 가능하면, 실제 폴더 구조(파일 종류, 자극 파일 존재 여부)를 직접 확인해 감사에 반영한다.
3. `outputs/stage1/` 폴더를 만든다.

## 1. 데이터셋별 감사 (병렬)
`dataset-auditor` 에이전트를 데이터셋마다 하나씩, 총 4개를 동시에 실행한다. 대상은 Horikawa, Emo-FilM, Spacetop, NSD다.

위임 메시지에는 다음을 명시한다.
* 담당 데이터셋 이름
* 우리 환경의 해당 데이터 경로 (있으면)
* 산출물 경로: `outputs/stage1/dataset_<이름>.md`, `outputs/agents/dataset-auditor/literature_<이름>.jsonl`
* Gate G1(원본 자극 접근)을 가장 먼저 판정할 것
* 참가자가 보고한 정서, 별도 평정자의 정서, 자극에 표현된 정서, AI 추정 정서를 구분할 것
* 응답은 15줄 이내 요약만

Horikawa 감사가 가장 중요하다. Horikawa 담당 에이전트에게는 공개 데이터(Mendeley, doi:10.17632/jbk2r73mzh.1)에 무엇이 들어 있는지, 원본 비디오와 평정 데이터를 어떻게 입수하는지를 특히 자세히 확인하게 한다.

## 2. 통합: Deliverable A
네 보고서를 읽고 `outputs/stage1/dataset_intelligence_report.md`를 작성한다.
* 4개 데이터셋 비교표: 피험자, 자극, 모달리티, 라벨 종류와 시간 해상도, 평정 주체, 생리 신호, 전처리, 접근성
* Gate G1, G2, G3 종합표
* **Cross-dataset Compatibility:** 데이터셋 간 정서 라벨 정의가 직접 결합 가능한지 쌍마다 판정한다. 근거를 단다.
* 데이터셋별 고유 장점과 방법론적 한계
* 데이터셋별 연구 기회 목록 (Stage 2 에이전트들이 참고할 것)
* 미확인 항목 전체 목록

## 3. 사실 검증
`adversarial-reviewer`를 실행해 `outputs/stage1/` 보고서들의 주요 수치와 주장을 출처와 대조하게 한다. 결과는 `outputs/agents/adversarial-reviewer/stage1_audit.md`에 저장한다. 지적된 오류를 반영해 보고서를 고친다.

## 4. Gate 판정
`outputs/stage1/gate_decision.md`를 작성한다.
* 데이터셋별 G1, G2, G3 판정과 근거
* Horikawa의 G1이 "불가" 또는 "요청 필요"이면: Horikawa 1순위 전략에 미치는 영향, 대안, 사용자가 결정해야 할 사항
* 모델 기반 연구가 가능한 데이터셋과 그렇지 않은 데이터셋

## 5. 마무리
`outputs/STAGE_STATUS.md`를 만들고 다음을 기록한다.
* Stage 1 완료 여부와 산출물 경로
* 검증된 것과 미확인인 것
* **사용자가 확인하거나 결정해야 할 항목** (빈 환경 정보, Gate 관련 결정)

그다음 멈추고, 사용자에게 STAGE_STATUS.md의 "사용자 확인 필요" 항목을 요약해서 보여준다. Stage 2로 넘어가지 않는다.
