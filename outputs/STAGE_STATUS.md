# STAGE STATUS

## Stage 1: Dataset Forensic Audit

* 상태: **완료** (2026-11-12). Stage 2는 사용자 확인 전까지 시작하지 않는다.
* 산출물: Deliverable A

| 파일 | 내용 |
|---|---|
| `outputs/stage1/dataset_intelligence_report.md` | **Deliverable A.** 4개 데이터셋 비교표, Gate 종합표, Cross-dataset Compatibility(단계형), 장점과 한계, 연구 기회, 미확인 항목 전체 목록, 검증 반영 기록 |
| `outputs/stage1/gate_decision.md` | 데이터셋별 G1/G2/G3 판정과 근거, Horikawa G1의 영향과 대안, 모델 기반 연구 가능 여부, 사용자 결정 사항 |
| `outputs/stage1/dataset_Horikawa.md` | Horikawa 감사 보고서 (8절 구조, 맨 위에 검증 반영 주석) |
| `outputs/stage1/dataset_EmoFilM.md` | Emo-FilM 감사 보고서 |
| `outputs/stage1/dataset_Spacetop.md` | Spacetop 감사 보고서 |
| `outputs/stage1/dataset_NSD.md` | NSD 감사 보고서 |
| `outputs/stage1/environment_gaps.md` | 우리 환경 정보 빈칸 목록과 실행 환경 기록 |
| `outputs/agents/dataset-auditor/literature_{Horikawa,EmoFilM,Spacetop,NSD}.jsonl` | 문헌 기록 57편 (verified 38, search_index 19) |
| `outputs/agents/adversarial-reviewer/stage1_audit.md` | 사실 검증 결과 (주장별 대조, 인용 표본 16편, 이견 기록) |

### 실행 방식 (사실 기록)

* `dataset-auditor` 4개(데이터셋별)를 병렬로, 이어서 `adversarial-reviewer` 1개를 실행했다.
* `.claude/agents/`의 커스텀 에이전트 타입이 이번 세션에 등록되지 않아(세션 시작 후 파일이 추가됨), 각 역할은 `general-purpose` 에이전트가 `CLAUDE.md`와 해당 `.claude/agents/<이름>.md`를 직접 읽고 그 지침을 따르는 방식으로 실행했다. 실제로 독립된 에이전트 5개가 실행되었다.
* 셸과 WebFetch의 외부 접근이 대부분 차단되어, 검증은 PubMed MCP(PMC 전문 포함), WebSearch, GitHub 공개 저장소 git clone(OpenNeuro 미러 메타데이터, 저자 코드)으로 했다. 대용량 데이터 본체(영상, NIfTI)는 내려받지 않았다.

### 검증된 것

* 4개 데이터셋의 서지, 피험자 수, 스캐너와 획득 파라미터, 공개 저장소 ID와 라이선스, 라벨 구조와 평정 주체 (감사 에이전트와 검증 에이전트가 각각 원 출처로 확인)
* Horikawa 원자료가 2020-04-24부터 OpenNeuro ds002425에 CC0로 공개되어 있었다는 사실 (출발점 정보의 "2026년 4월 공개"와 다름)
* Kragel 연구실 2026 연구 서지: Ma & Kragel (2026), Nat Commun 17:1518, doi:10.1038/s41467-025-68240-z (29명, 50개 항목 중 17개 사용)
* Spacetop 원본 자극의 공개 위치(git-annex 기록상 공개 S3), 생리 데이터 미공개, alignvideo 평정 구조와 결측률(응답 48.7%)
* NSD에 기본 정서 라벨이 없고 nsdmeadows 100장만 있다는 사실(2차 본문 기준)
* 인용 표본 16편: 식별자 오류 0, 내용 오류 0, 표기 오류 3 (전부 수정)

### 미확인인 것 (주요 항목, 전체는 Deliverable A 7절의 42개 항목)

* 우리 환경의 데이터 경로와 원본 자극 보유 여부 (네 데이터셋 모두)
* Horikawa 비디오 요청 양식의 이용 조건, Mendeley 예치본 내용, figshare 라이선스
* Emo-FilM 절단 정보 파일 내용, 영화별 CC 조항, 논문 Table 1과 Supplementary
* Spacetop 영상의 원 출처와 저작권, 생리와 설문의 공개 경로, N=101 산정 기준
* NSD Terms 원문, DAA 승인 방식, nsdmeadows 지시문
* Cowen & Keltner (2017), Westlin (2025), NSD 원 논문의 본문
* search_index 19편의 식별자 경로 직접 확인

### Gate 요약

| 데이터셋 | G1 원본 자극 | G2 fMRI | G3 라벨 |
|---|---|---|---|
| Horikawa | 요청 필요 (Google Form) | 사용 가능 | 공개, 별도 평정자 |
| Emo-FilM | 공개 재료로 재구성 가능성 높음 (확인 필요) | 사용 가능 | 공개, 별도 평정자 |
| Spacetop | 공개 다운로드 가능 (저작권 확인 필요) | 사용 가능 | 공개, 참가자 본인 사후 평정 |
| NSD | 약관(DAA) 동의 절차 필요 | 사용 가능 | 정서 라벨 사실상 없음 (100장) |

---

## 사용자 확인 필요 (Stage 2 시작 전)

### A. 환경 정보 (`reference/datasets_and_resources.md` 1절, 6칸 모두 공란)
1. 데이터 위치 (Horikawa, Emo-FilM, Spacetop, NSD)
2. 원본 자극 파일 보유 여부 (데이터셋별)
3. 이미 추출해 둔 feature, embedding
4. 계산 자원
5. 사용 가능한 pretrained checkpoint
6. 제약 (마감, 데이터 사용 동의 범위)

### B. Gate 관련 결정
7. **Horikawa 원본 비디오:** 연구실(EmoViS는 Horikawa 2020 사용, EmoBrain은 V-JEPA2 사용)이 이미 비디오나 추출 feature를 보유하고 있는가? 없다면 Cowen 연구실 Google Form으로 요청할 것인가?
8. **Horikawa 1순위 유지 여부:** 데이터가 2020년부터 공개되어 재분석이 여러 편 있고(Westlin 2025 preprint의 재현 실패 보고 포함), 5명, 반복 제시 없음, 무음이라는 한계가 확인되었다. Horikawa를 계속 1순위로 둘지, 모델 기반 연구의 1순위를 Spacetop 또는 Emo-FilM으로 옮길지. (Coordinator 잠정 권고: 보유 여부를 먼저 확인하고, Horikawa를 최우선으로 유지하되 Stage 2에서 질문마다 "G1 필요 여부"를 표시)
9. **NSD:** Data Access Agreement를 이미 제출했는가?
10. **Emo-FilM:** 연구실의 Emo-FilM 연구 계획이 이미 영화 편집본을 확보했는가?
11. **Spacetop 생리 데이터:** 공개본에 없는 EDA/PPG를 저자에게 요청할 것인가?

### C. 지침 파일과 실행 환경
12. **`reference/` 정정:** `datasets_and_resources.md` 2.1절의 "2026년 4월 공개", `starting_papers.md` 특별 지시의 "2026년에 공개되었으므로"를 확인된 사실(2020년 OpenNeuro 공개, 2026-04는 Mendeley 예치)로 고칠지.
13. **`reference/existing_projects.md`:** "[사용자 확인 필요]" 표시가 남아 있다. 세 프로젝트 요약이 현재 상태와 맞는지.
14. **네트워크 허용:** Stage 2는 문헌 본문 확인이 핵심인데 doi.org, arxiv.org, nature.com, openneuro.org, data.mendeley.com, naturalscenesdataset.org, cvnlab.slite.page 등이 이 클라우드 환경에서 차단되어 있다. 허용할 경우 Stage 2 시작 시 이 저장소 전용 환경을 만들거나 기존 환경에 호스트를 추가할 수 있다.
15. **문헌 표기 규칙 확장:** `verified_by: "search_index"`, `discussion_read: "search_summary"` 값을 Stage 1에서 새로 도입했다(CLAUDE.md 5절 스키마에 없음). Stage 2에서도 이 규칙을 쓸지.

---

## 사용자 결정 기록

(위 항목에 대한 결정을 여기에 적어 주세요. Stage 2 Coordinator가 이 절을 먼저 읽습니다.)

*
