# Stage 4 최종 인용 검증 (prompts/stage4_evaluation_proposals.md 6절)

* 작성: adversarial-reviewer (Agent 12). 기준일 2026-11-12. 새로 실행된 검증자이며 대상 파일 작성에 참여하지 않았다.
* 대상: `outputs/rq_cards/*.md` 10장, `outputs/final_synthesis.md`, `outputs/pilots.md`. 대상 파일은 수정하지 않았다.
* 기준: CLAUDE.md 5절. verified는 DOI, PMID, arXiv ID, 학회 proceedings URL 중 하나로 존재를 확인한 것만 센다.
* 재현 자료: `outputs/agents/adversarial-reviewer/final_citation_check/` (추출, 해석, 표본 추출 스크립트와 결과 JSON). 그 폴더에서 `python3 -I draw.py`를 실행하면 아래 (e)의 표본이 그대로 다시 뽑힌다(확인함).

## 0. 요약

| 항목 | 결과 |
|---|---|
| 고유 논문 식별자 | 140개(DOI 105, arXiv 35, PMID 표기 0). 데이터 저장소 식별자는 따로 분류 |
| DB verified 일치 | 140/140. DB에 없거나 unverified인 식별자 없음 |
| 이번 세션 직접 해석 | 140/140 해석 성공(Crossref 105, arXiv API 35). 해석된 제목과 제1저자가 DB 서지와 140/140 일치. 식별자가 다른 논문을 가리키는 경우 없음 |
| 식별자 없는 인용 | 대부분 같은 파일 다른 곳에 식별자가 있는 재언급(325회). 파일 안에 식별자가 전혀 없는 인용 13건(모두 DB verified 항목에 대응, 1건은 대응 후보가 둘). 검증 불가 1건(ISMRM 2025 학회 초록, 카드가 이미 "근거로 쓰지 않음" 표시) |
| 새로 검증해 추가 | 3편(fMRIPrep, DINOv2, Synchformer). 카드가 도구로 언급하나 식별자가 없던 것. merge.py 재실행 후 DB 526 → 529행 |
| 주장 대조 무작위 15건 | 맞음 14, 부분 1, 틀림 0 |
| 추가 표적 점검 8건(무작위 표본 밖) | 맞음 4, 부분 4, 틀림 0. 부분 판정은 모두 final_synthesis.md와 RQ-15, RQ-08의 표현 범위 문제 |
| 읽은 수준 표시 | 무작위 3건 모두 일치. 전수 51행 점검에서 기록 누락 1건(RQ-10의 Tuckute 2024) |

결론: **존재와 verified 여부 측면에서 제거해야 할 논문 인용은 없다.** 고칠 것은 (1) 식별자 보강 13건, (2) 표현 범위 수정 6건(final_synthesis.md 4곳, RQ-15 1곳, RQ-08 1곳), (3) 검증 불가 학회 초록 1건과 검색 기록 속 무식별자 언급의 처리다.

---

## (a) 파일별 식별자 수와 DB 대조

식별자는 정규식으로 DOI(`10.xxxx/...`), arXiv ID(`arXiv:NNNN.NNNNN`), PMID를 뽑았다. arXiv가 부여한 DOI(10.48550)는 arXiv ID로 바꿨다. "arXiv" 접두어 없이 쓴 맨 arXiv 번호는 없었다(별도 검색으로 확인).

| 파일 | 고유 논문 식별자 | 등장 줄 수 | DB verified 일치 | 직접 해석 성공 | 데이터 저장소 식별자 | PMC ID |
|---|---|---|---|---|---|---|
| RQ01_emotion_category_replication.md | 21 (DOI 17, arXiv 4) | 28 | 21 | 21 | ds002425, ds005191 | - |
| RQ03_stimulus_ensemble_geometry.md | 14 (DOI 10, arXiv 4) | 22 | 14 | 14 | ds002425, ds005191 | - |
| RQ08_beyond_scene_description.md | 13 (DOI 10, arXiv 3) | 23 | 13 | 13 | ds002425, ds005191 | - |
| RQ10_prospective_stimulus_selection.md | 24 (DOI 17, arXiv 7) | 36 | 24 | 24 | ds002425, ds005191 | PMC10120732 |
| RQ14_who_did_what_to_whom.md | 16 (DOI 14, arXiv 2) | 21 | 16 | 16 | ds004872 | - |
| RQ15_read_vs_ask_AI_emotion.md | 27 (DOI 8, arXiv 19) | 29 | 27 | 27 | ds005191 | - |
| RQ32_arousal_as_speed.md | 16 (DOI 16) | 21 | 16 | 16 | ds002425, ds004872, ds005191 | - |
| RQ33_natural_kuleshov.md | 22 (DOI 19, arXiv 3) | 25 | 22 | 22 | ds002425, ds005191 | - |
| RQ44_recall_reconstruction.md | 23 (DOI 20, arXiv 3) | 26 | 23 | 23 | ds005191 | PMC10230322, PMC13750827, PMC3251697 |
| RQ60_implied_sound.md | 19 (DOI 15, arXiv 4) | 21 | 19 | 19 | - | - |
| final_synthesis.md | 25 (DOI 16, arXiv 9) | 28 | 25 | 25 | - | - |
| pilots.md | 7 (DOI 2, arXiv 5) | 7 | 7 | 7 | doi:10.6084/m9.figshare.11988351, ds002425, ds005191 | - |
| **전체 고유** | **140 (DOI 105, arXiv 35)** | | **140** | **140** | | |

**불일치 목록: 없음.**
* DB의 unverified 5건(EmoGrowth, Modeling dynamic social vision, arXiv:2605.23895, arXiv:2606.09770, Evaluating TRIBE v2)은 대상 파일 어디에도 인용되지 않았다(제목, ID 검색으로 확인).
* 해석 결과와 DB 서지의 대조: 해석된 제목 단어의 70% 이상이 DB 서지에 있고 제1저자 성이 일치하는지 140건 모두 확인했다. 연도 차이는 온라인 선공개와 권호 연도 차이뿐이었다(예: Chen 2016/2017 Nat Neurosci, Bowen 2017/2018 PBR, Gaviria 2020/2021 HBM). 인용 오류로 보지 않는다.
* 줄 단위 점검: 식별자가 있는 줄에 해석된 제1저자 성이 없는 경우 45건을 눈으로 확인했다. 모두 모델명이나 방법명(DeepMReye, V-JEPA 2, TRIBE v2, Mind captioning, controversial stimuli 등)으로 부른 정상 인용이었다.

**데이터 저장소 식별자(논문 아님, 따로 분류)**

| 식별자 | 확인 경로 | 결과 | 사용 위치 |
|---|---|---|---|
| doi:10.6084/m9.figshare.11988351 (figshare, Horikawa 전처리본과 라벨) | doi.org handle API | 존재(responseCode 1) | pilots.md 15행 |
| OpenNeuro ds002425 (Horikawa raw) | doi.org handle API로 DataCite DOI 10.18112/openneuro.ds002425.v1.0.1, v1.0.2 | 존재 | 카드 7장, pilots |
| OpenNeuro ds005191 (Mind captioning raw) | 10.18112/openneuro.ds005191.v1.0.0~v1.0.2 | 존재 | 카드 8장, pilots |
| OpenNeuro ds004872 (Emo-FilM 평정 원자료) | 10.18112/openneuro.ds004872.v1.0.0~v1.0.2 | 존재 | RQ-14 230행, RQ-32 99행 |

* openneuro.org 자체는 이번 세션에서 접근이 막혀(프록시 403) 데이터셋 내용은 열지 않았다. 존재만 DataCite DOI로 확인했다.
* ds004872는 Emo-FilM의 **평정** 저장소다. fMRI 저장소는 ds004892다(Stage 1 `outputs/stage1/dataset_EmoFilM.md` 42행). RQ-14와 RQ-32는 둘 다 평정자 원자료 용도로 ds004872를 쓰므로 맞게 쓴 것이다.

**PMC ID 대응 확인(PubMed ID 변환 도구)**

| PMC ID | 대응 DOI | 카드에서 가리키는 논문 | 판정 |
|---|---|---|---|
| PMC10120732 | 10.1101/2023.04.16.537080 | RQ-10 76행 Tuckute 2024의 bioRxiv 판 | 일치 |
| PMC13750827 | 10.1523/ENEURO.0146-26.2026 | RQ-44 88행 Curko 2026 | 일치 |
| PMC10230322 | 10.1016/j.cub.2020.04.014 | RQ-44 85행 Breedlove 2020 | 일치 |
| PMC3251697 | 10.1016/j.neuroimage.2011.08.076 | RQ-44 96행 Mumford 2012 | 일치 |

**DB 구조 관련 부수 발견(인용 오류 아님)**
* VidSitu(Sadhu 2021)가 DB에 두 행으로 나뉘어 있다: `arxiv:2104.00990`(llm-semantics, full_text)과 `doi:10.1109/cvpr46437.2021.00554`(coordinator, discussion_read no). merge.py가 preprint와 학회판을 묶지 못했다. RQ-14 68행은 두 ID를 함께 적어 문제는 없다. Gauthaman 2024/2025는 한 행으로 잘 묶였다.

---

## (b) 식별자 없는 인용과 그 대응

"저자 연도" 형태(예: `Horikawa 2020`, `Ma & Kragel 2026`)를 정규식으로 모두 뽑고, 첫 저자 성과 연도로 DB 항목을 찾은 뒤, 그 항목의 식별자가 **같은 파일 어딘가에** 있는지 봤다. 여러 저자를 나열한 표 행에서 마지막 저자가 잡힌 경우(예: `Frey, Nau, Doeller 2021`의 "Doeller 2021")는 같은 줄에 식별자가 있어 제외했다. `Woo 2017` 형태의 인용은 대상 파일에 없었다.

### B1. 같은 파일 안 재언급(식별자가 그 파일 다른 곳에 있음): 문제 없음
* 총 325회. RQ01 50, RQ03 32, RQ08 20, RQ10 24, RQ14 19, RQ15 34, RQ32 45, RQ33 19, RQ44 27, RQ60 45, final_synthesis 8, pilots 2.
* 예: RQ-01의 `Ma & Kragel 2026`(163, 279, 298행)은 90행의 doi:10.1038/s41467-025-68240-z에 대응한다. DB에는 Ma & Kragel 2026이 두 편(Nat Commun, PLoS Biol) 있으나 RQ-01은 Nat Commun만 식별자로 적어 모호하지 않다.

### B2. 파일 안에 식별자가 전혀 없는 인용: 식별자 보강 권고(13건)

| # | 파일:행 | 인용 표기 | 대응 DB 항목(모두 verified) | 비고 |
|---|---|---|---|---|
| 1 | RQ14:107, 157, 250 | Horikawa 2020 | doi:10.1016/j.isci.2020.101060 | |
| 2 | RQ32:112 | Horikawa 2020 | doi:10.1016/j.isci.2020.101060 | |
| 3 | RQ33:28, 41, 97, 99, 106, 120 | Horikawa 2020 | doi:10.1016/j.isci.2020.101060 | 핵심 전제 논문인데 카드에 식별자가 한 번도 없음 |
| 4 | RQ44:143, 176, 416 | Horikawa 2020 | doi:10.1016/j.isci.2020.101060 | |
| 5 | pilots:14, 41, 49, 63, 68, 76 | Horikawa 2020 | doi:10.1016/j.isci.2020.101060 | 15행의 figshare DOI는 데이터셋이지 논문이 아님 |
| 6 | pilots:63, 68 | Westlin 2025 | arXiv:2507.00320 | P2의 재현 대상 |
| 7 | RQ08:203 | Westlin 2025 | arXiv:2507.00320 | |
| 8 | RQ60:93 | Du 2023 | doi:10.1016/j.isci.2023.107571 | |
| 9 | RQ01:69 | Stringer 2019 | doi:10.1038/s41586-019-1346-5 | |
| 10 | RQ03:190 | Bolt 2025 | doi:10.1038/s41593-025-01945-y | |
| 11 | RQ44:454 | Gauthaman 2025 | doi:10.1371/journal.pcbi.1013714 | |
| 12 | RQ15:46 | Tak 2025 | arXiv:2502.05489 (Tak et al. 2025, Mechanistic Interpretability of Emotion Inference in LLMs) | DB에 Tak 2025는 이것 하나 |
| 13 | final_synthesis:87 | Nguyen 2026 | **대응 후보 둘:** doi:10.7554/elife.107955 (Nguyen, Etzel, Bezdek, Zacks, 사건 분절 기제)와 arXiv:2607.06875 (Nguyen T 외, Video2Reaction) | 문맥(RQ-25, 오차형 대 불확실성형 사건 경계, `rq_landscape.md` 691행)으로 보면 eLife 논문. **모호하므로 식별자 필수** |

### B3. 논문 식별자가 없는 비논문 또는 검색 기록 속 언급

| 파일:행 | 내용 | 상태 | 권고 |
|---|---|---|---|
| RQ32:75 | "동공 고각성 집단의 빠른 상태 전이를 보고한 ISMRM 2025 학회 초록(식별자 확인 못 함, 근거로 쓰지 않음)" | **검증 불가.** 검색 색인에서 후보 1건을 찾음: ISMRM 2025 program #3705, Can E, Öner B, Özbay PS, "Effects of Arousal Level and Data-Driven Cardiac Signal Regression on Dynamic Functional Connectivity"(archive.ismrm.org/2025/3705.html). 그러나 proceedings 페이지가 이번 세션에서 차단되어(DNS 실패, 프록시 403) 직접 확인하지 못했다. 검색 요약상 휴지기 fMRI이며 영화 시청 자료가 아니다 | (d) 참조 |
| RQ44:113~114 | PubMed 검색 결과로 "외상 영상 침투 기억의 TMS 연구", "시점 이동 리뷰", "정서 schema 연합 기억"을 식별자 없이 언급 | 검색 기록 표의 결과 요약이며 근거로 쓰지 않음 | 선행 판정(not found)의 근거이므로 PMID를 표에 붙이면 재현이 쉬워진다. 필수는 아님 |

### B4. 도구와 모델 이름만 있고 식별자가 없는 언급(인용 보강 권고, 필수 아님)

| 도구 | 위치 | 대응 식별자 | DB 상태 |
|---|---|---|---|
| fMRIPrep | RQ01:145, 188; RQ03:132; RQ10:135; RQ32:122, 259; RQ33:129 | doi:10.1038/s41592-018-0235-4 | **이번에 검증해 추가**(c) |
| DINOv2 | RQ01:142; RQ03:128 | arXiv:2304.07193 | **이번에 검증해 추가**(c) |
| Synchformer | RQ60:110 (MMAudio의 시각 조건 feature) | arXiv:2401.16423 | **이번에 검증해 추가**(c) |
| hyperalignment (neuroboros) | RQ01:19, 145, 149, 201; RQ03:6, 132, 136 | doi:10.7554/elife.56601 (Haxby 외 2020) | DB verified |
| brainiak SRM | RQ01:145; RQ03:132 | NeurIPS 2015 proceedings URL (Chen PH 외, A Reduced-Dimension fMRI Shared Response Model) | DB verified(publisher) |

---

## (c) 새로 검증해 추가한 문헌

`outputs/agents/adversarial-reviewer/literature.jsonl`에 CLAUDE.md 5절 형식으로 3편을 추가했다(63 → 66행). 이후 `python3 -I outputs/literature/merge.py`를 다시 실행했다. DB는 526 → 529행, verified_unique 524. 기존 행은 하나도 바뀌지 않았다(실행 전후 CSV를 행 단위로 비교해 확인).

| ID | 서지 | 확인 경로 | discussion_read | 추가 이유 |
|---|---|---|---|---|
| doi:10.1038/s41592-018-0235-4 | Esteban O 외, 2019, fMRIPrep: a robust preprocessing pipeline for functional MRI, Nat Methods 16:111-116 | Crossref, PubMed(PMID 30532080) | abstract_only | 카드 4장과 재전처리 단계가 언급 |
| arXiv:2304.07193 | Oquab M 외, 2023, DINOv2: Learning Robust Visual Features without Supervision | arXiv API | abstract_only | RQ-01, RQ-03 시각 교란 feature 후보 |
| arXiv:2401.16423 | Iashin V, Xie W, Rahtu E, Zisserman A, 2024, Synchformer: Efficient Synchronization from Sparse Cues | arXiv API | abstract_only | RQ-60 MMAudio 구성 요소 |

* 세 편 모두 초록만 읽었다. Limitations 절은 읽지 않았으므로 future_directions는 비워 두었다.
* DINOv2 학습 데이터에 Cowen & Keltner 클립 프레임이 들어갔는지는 확인하지 못했다(사전학습 오염 미확인으로 jsonl에 기록).
* ISMRM 2025 초록은 확인하지 못했으므로 추가하지 않았다.

---

## (d) 제거 또는 대체가 필요한 인용

### D1. 존재 미확인으로 제거 또는 대체 필요

| 파일:행 | 인용 | 이유 | 권고 |
|---|---|---|---|
| RQ32:75 | ISMRM 2025 학회 초록 | 식별자도 proceedings URL도 확인하지 못함. 카드가 이미 "근거로 쓰지 않음"이라고 적었지만 verified 규칙상 검증되지 않은 인용이다 | 문장을 지우거나, Coordinator 환경에서 archive.ismrm.org/2025/3705.html을 열어 확인한 뒤 URL을 붙인다. 붙이더라도 "휴지기 fMRI, 학회 초록, 동료 심사 전"을 함께 적는다 |

### D2. 식별자 보강 필요(존재는 확인됨)
* (b) B2의 13건. 특히 **final_synthesis.md 87행 Nguyen 2026**은 DB 대응 후보가 둘이라 식별자 없이는 어느 논문인지 알 수 없다. doi:10.7554/eLife.107955를 붙인다.
* RQ-33은 핵심 전제인 Horikawa 2020을 6곳에서 쓰면서 식별자를 한 번도 적지 않았다.

### D3. 원문과 맞지 않는 표현(범위 확대, 과장): 문장 수정 필요

| 파일:행 | 현재 표현 | 원문 확인 결과 | 수정 제안 |
|---|---|---|---|
| final_synthesis.md:41 | "정서 신경과학에서 쓰는 AI 정서는 거의 모두 출력이다. 평정(Tak & Gratch 2024, arXiv:2408.13718)…" | Tak & Gratch 2024는 신경 연구용 자극(Skerry & Saxe 계열)에 대한 GPT-4 판단을 사람 판단과 비교한 행동 연구다. 뇌 자료를 쓰지 않았다(arXiv 초록) | 신경 분석에 AI 평정을 쓴 예로 Santavirta 외 2025 GPT-4V(doi:10.1162/imag.a.134)나 Huang 2026(arXiv:2610.22706)을 들고, Tak & Gratch는 "출력 기반 평정의 행동 수준 예"로 낮춘다 |
| final_synthesis.md:19 | Westlin 2025 군집이 "정서 범주(NMI 0.014)보다 스캔 세션(NMI 0.19)과 더 맞았다" | 수치는 맞다(평정 NMI M = 0.0141, 세션 NMI M = 0.1882, 군집 수 11~14, Rand 0.85; arXiv PDF Results). 그러나 저자는 세션 NMI도 "again quite low"라고 해석했고, 세션과 run이 군집마다 이질적으로 섞였다고 보고했다. 범주 수가 다른 라벨 사이의 NMI는 우연 기대치가 달라 크기를 바로 비교하기 어렵다 | "정서 범주와의 NMI는 0.014로 거의 0이었다. 스캔 세션과의 NMI(0.19)도 저자는 낮다고 해석했다"로 고친다. 시간 효과 주장은 RQ-01 P2의 검증 대상으로 남긴다 |
| final_synthesis.md:22 | Mind captioning에 "클립마다 **정서 단어를 빼고 쓴** 인간 캡션 20개" | 원문은 작업자에게 "정서 반응 같은 주관적 측면보다 시각 내용에 집중하라"고 지시했고, 그 결과 캡션이 정서를 "드물게(rarely)" 반영했다고 적었다(Discussion). 정서 단어를 명시적으로 뺀 것은 아니다 | "정서 반응 대신 시각 내용에 집중하라는 지시로 받은 캡션 20개(정서 표현은 드묾)"로 고친다. 62행 "정서 배제"도 같은 뜻으로 단서를 단다 |
| RQ08:30 | "사람이 **정서 단어 없이** 쓴 장면 설명" | 위와 같음. 카드 본문은 38행, 98행에서 정확하게 적었고 145행에서 정서 어휘 비율을 세는 분석도 두었다 | 30행만 38행 표현에 맞춘다. 용어 "정서 배제 캡션"은 "정서 배제 지시 캡션"이 더 정확하다 |
| final_synthesis.md:48 | Daunhawer 2023이 "여러 view에서 공통 성분과 고유 성분을 원리적으로 분리하는 이론" | 원문(arXiv 초록)은 multimodal contrastive learning이 modality 사이 **공유 잠재 요인을 block 단위로 식별**함을 증명한다. modality 고유 잠재 변수는 생성 과정에 넣었지만 복원을 보장하지 않는다 | "공유 성분을 block 단위로 식별할 수 있음을 보인 이론"으로 고친다. RQ-18에서 라벨 출처 고유 성분을 따로 추정하려면 별도 방법이 필요하다고 덧붙인다 |
| RQ15:35 | "GPT-4V 평정으로 만든 뇌 지도가 사람 평정 지도와 비슷하다는 보고(Santavirta 2025)"를 "AI **정서** 라벨이 신경 분석에 들어오는" 예로 듦 | 이 논문은 정서 범주가 아니라 **사회 지각 feature 138개**를 GPT-4V로 평정했다(PMC 전문, Abstract와 Methods). 일부 feature만 정서와 관련된다 | "사회 지각 feature(일부 정서 관련)"라고 범위를 적거나, DB에 있는 정서 전용 후속 Santavirta 외 2025 bioRxiv(doi:10.1101/2025.09.18.677029, DB verified, abstract_only)를 함께 인용한다 |

틀린 인용(원문과 반대이거나 존재하지 않는 내용)은 찾지 못했다.

---

## (e) 주장 대조 15건

### 표본 추출 절차
* 시드 **20261112**, Python `random.Random(20261112)`. 스크립트: `final_citation_check/draw.py`, 결과: `draw_out.txt`.
* 모집단 1: final_synthesis.md의 고유 식별자 25개(첫 등장 줄 기준, figshare 제외). 여기서 5개를 먼저 뽑았다.
* 모집단 2: 상위 5개 카드(RQ-01, 03, 08, 14, 15)의 4절 Prior Literature 표에서 식별자가 있는 행(18, 13, 13, 14, 15행). 카드마다 2개씩 10개를 뽑았다(카드 이름순).
* 원문 확인 수준은 표에 적었다. "본문"은 이번 세션에서 전문을 직접 열어 해당 대목을 찾은 것이다.

| # | 파일:행 | 논문 | 카드나 종합의 주장(요약) | 확인한 원문 | 판정 | 이유 |
|---|---|---|---|---|---|---|
| 1 | final_synthesis:40 | Sofroniew 외 2026, [arXiv:2604.07729](https://arxiv.org/abs/2604.07729) | LLM 안에 정서 개념 방향이 있고, 출력과 다르게 작동할 수 있다 | 본문(arXiv HTML) | 맞음 | 정서 vector가 출력에 인과 영향을 줌(초록). "desperate" steering이 눈에 띄는 정서 흔적 없이 reward hacking을 늘림, emotion deflection vector 실험(본문) |
| 2 | final_synthesis:41 | Tak & Gratch 2024, [arXiv:2408.13718](https://arxiv.org/abs/2408.13718) | 정서 신경과학에서 쓰는 AI 정서의 예: 평정(출력) | 초록 | **부분** | 출력 기반 평정이라는 점은 맞다. 그러나 뇌 자료가 없는 행동 연구라 "정서 신경과학에서 쓰는" 예로는 범위 확대. (d) D3 참조 |
| 3 | final_synthesis:49 | Elhage 외 2022, [arXiv:2209.10652](https://arxiv.org/abs/2209.10652) | 적은 차원에 많은 특징이 겹쳐 담기는 superposition | 초록 | 맞음 | 희소 feature를 superposition으로 저장한다는 정의와 일치. 뇌 적용은 종합이 "가설(RQ-07)"로 표시했다. 원 논문은 인공 신경망의 희소 feature 조건을 전제로 하므로 그 조건을 함께 적으면 더 정확하다 |
| 4 | final_synthesis:67 | Cowen & Keltner 2017, [doi:10.1073/pnas.1702247114](https://doi.org/10.1073/pnas.1702247114) | 규범 평정의 비율 분포, 범주 경계가 흐림 | 초록(PubMed) | 맞음 | "boundaries between categories of emotion are fuzzy rather than discrete", 연속 gradient |
| 5 | final_synthesis:110 | Westfall & Yarkoni 2016, [doi:10.1371/journal.pone.0152719](https://doi.org/10.1371/journal.pone.0152719) | 측정 오차를 다루는 통계 논리가 확립됨 | 초록(PubMed) | 맞음 | 측정 신뢰도를 무시한 증분 타당도 주장의 1종 오류 증가를 보이고, 이를 통제하는 SEM 접근을 검토 |
| 6 | RQ01:84 | Cowen & Keltner 2017, [doi:10.1073/pnas.1702247114](https://doi.org/10.1073/pnas.1702247114) | 2,185개 클립 자기보고에서 27개 범주. 범주 라벨이 차원보다 보고를 잘 포착하나 경계는 흐림 | 초록(PubMed) | 맞음 | 세 요소 모두 초록에 있음 |
| 7 | RQ01:88 | Gauthaman, Ménard, Bonner 2025, [doi:10.1371/journal.pcbi.1013714](https://doi.org/10.1371/journal.pcbi.1013714) | 공유 스펙트럼이 넓은 rank 범위에서 power law, hyperalignment 뒤 고rank까지 공유, 3.2.2절 단일 숫자 요약 금지, 3.2.1절 비선형 방법이면 낮은 차원 가능 | 본문(PMC12654933) | 맞음 | 약 네 자릿수 rank에 걸친 power law, 기능 정렬 뒤 공유 차원 증가(S3 Fig), 3.2.1 Linear methods에 비선형 사상 가능성, 3.2.2 Alternative heavy-tailed distributions에 "single scalar value로 차원을 정량화하지 말아야" 문장. 절 번호까지 일치 |
| 8 | RQ03:76 | Cowen & Keltner 2021, [doi:10.1016/j.tics.2020.11.004](https://doi.org/10.1016/j.tics.2020.11.004) | 넓은 자연 자극과 열린 통계 기법으로 25가지 이상의 정서가 고차원, 범주적, 혼합적으로 드러남 | 초록(PubMed) | 맞음 | "Upwards of 25 distinct varieties", "high-dimensional, categorical, and often blended". "범주 쪽 이론도 자극 다양성 의존을 예측"은 카드의 해석이며 카드도 그렇게 썼다 |
| 9 | RQ03:77 | Gao 외 2017, [doi:10.1101/214262](https://doi.org/10.1101/214262) | 과제 복잡도가 신경 차원과 동역학 복원 정확도를 정한다는 이론 | 초록(Crossref) | 맞음 | "task complexity governs both neural dimensionality and accurate recovery of dynamic portraits" |
| 10 | RQ08:62 | Abdel-Ghaffar 외 2024, [doi:10.1038/s41467-024-49073-8](https://doi.org/10.1038/s41467-024-49073-8) | 후두측두 피질이 의미와 정서 feature에 함께 tuning, mid-level 구조 feature는 통제하지 않았다고 저자가 적음 | 본문(PMC11233618) | 맞음 | "many OTC voxels are co-tuned to semantic and affective information". Discussion에 "we did not investigate mid-level structural features" |
| 11 | RQ08:67 | Frey, Nau, Doeller 2021, [doi:10.1038/s41593-021-00947-w](https://doi.org/10.1038/s41593-021-00947-w) | 안구 MR 신호로 시선 추정, 기존 자료에도 적용, 추정 시선이 넓은 영역 활동을 설명 | 초록(PubMed) | 맞음 | "works even in existing datasets", "Decoded eye movements explain network-wide brain activity" |
| 12 | RQ14:64 | Mohammadi, Van De Ville, Vuilleumier 2023, [doi:10.1093/cercor/bhad093](https://doi.org/10.1093/cercor/bhad093) | 영화의 정서 순간을 성분으로 평정, 성분별 네트워크 조합, 자극에서 계산한 feature는 아님 | 초록(PubMed) | 맞음 | 20명, 40개 클립, 119개 순간, 32개 성분 평정, valuation appraisal 등 네트워크 |
| 13 | RQ14:69 | Yatskar, Zettlemoyer, Farhadi 2016, [doi:10.1109/cvpr.2016.597](https://doi.org/10.1109/cvpr.2016.597) | 이미지 의미역 표지(situation recognition)의 원형 | 서지(Crossref 제목만) | 맞음 | 제목 "Situation Recognition: Visual Semantic Role Labeling for Image Understanding"과 일치. 카드도 "미열람(서지만)"으로 표시했다. 초록 이상은 확인하지 못했다 |
| 14 | RQ15:61 | Sofroniew 외 2026, [arXiv:2604.07729](https://arxiv.org/abs/2604.07729) | Claude Sonnet 4.5에서 합성 이야기로 정서 vector 추출, steering으로 인과성, valence와 arousal 축, 표상이 국소적이며 주관 경험을 함의하지 않음 | 본문(arXiv HTML) | 맞음 | Sonnet 4.5가 쓴 이야기로 vector 추출(Methods), 상위 PC가 valence와 arousal, "locally scoped"(2.2.3절), "do not imply ... subjective experience"(초록) |
| 15 | RQ15:65 | Santavirta 외 2025, [doi:10.1162/imag.a.134](https://doi.org/10.1162/imag.a.134) | GPT-4V 답 평정과 인간 평정의 뇌 지도 수렴, 내용 필터로 일부 자극 평정 거부 | 본문(PMC12410153) | 맞음 | 성적, 혈액 장면에서 평정 거부(Methods와 Discussion). 단 같은 카드 35행의 "정서 라벨" 표현은 범위 확대((d) D3) |

**집계: 맞음 14, 부분 1, 틀림 0.** final_synthesis.md에서 5건, 상위 5개 카드에서 10건이다.

### 추가 표적 점검(무작위 표본 밖, 집계에 넣지 않음)
위험이 큰 주장이나 Coordinator가 예로 든 항목을 따로 확인했다.

| 파일:행 | 논문 | 주장 | 확인한 원문 | 판정 | 이유 |
|---|---|---|---|---|---|
| RQ15:62, 80, 108 | Xing 외 2026, [arXiv:2609.34742](https://arxiv.org/abs/2609.34742) | 세 VLM(Qwen3-VL-8B, InternVL3.5-8B, Ministral-3-8B)에서 Ekman 6개 정서 vector, ImageNet activation으로 추정한 모델 간 변환 | 본문(arXiv HTML) | 맞음 | 세 모델과 6개 정서가 본문 1절, 3절과 일치. 검토 반영(card_review_A 4절)이 제대로 들어갔다 |
| final_synthesis:19 | Westlin 외 2025, [arXiv:2507.00320](https://arxiv.org/abs/2507.00320) | 군집 11~14개, 정서 NMI 0.014보다 세션 NMI 0.19와 "더 맞았다" | 본문(arXiv PDF) | **부분** | 수치와 군집 수, Rand 0.85는 일치. 해석은 저자 해석을 넘음((d) D3) |
| final_synthesis:22 | Horikawa 2025, [doi:10.1126/sciadv.adw1464](https://doi.org/10.1126/sciadv.adw1464) | 6명, 정서 단어를 뺀 캡션 20개, 시험 클립 반복, 회상과 vividness | 본문(PMC12588295) | **부분** | 일본어 모국어 6명, 캡션 20개(GPT-3.5 교정), 72개 클립 5회, 회상 후 정확도와 vividness 5점 평정은 일치. "정서 단어를 빼고"는 과장((d) D3) |
| final_synthesis:20, RQ08:60 | Du 외 2023, [doi:10.1016/j.isci.2023.107571](https://doi.org/10.1016/j.isci.2023.107571) | motion energy 6,555, 평균 21% voxel, TPJ 43~62%, banded ridge, 고유 분산 미보고 | 본문(PMC10470388) | 맞음 | 수치 모두 일치. 본문에 unique variance나 variance partitioning 보고 없음. Limitations에 "such features still confound the results" 가능성 명시 |
| RQ14:41 | Frankland & Greene 2015, [doi:10.1073/pnas.1421236112](https://doi.org/10.1073/pnas.1421236112) | lmSTC가 누가 누구에게를 부호화하고 그 패턴이 이 정보에 의존하는 amygdala 반응을 예측 | 초록(PubMed) | 맞음 | "predict affect-related amygdala responses that depend on this information" |
| RQ15:58 | Du 외 2025, [arXiv:2509.24298](https://arxiv.org/abs/2509.24298) | MLLM과 LLM의 triplet 판단으로 30차원 embedding, 인간 평정보다 뇌 예측이 좋음 | 초록 | 맞음 | 초록과 일치. 모델명(Qwen2-VL, Llama-3.1)은 초록에 없어 DB 본문 기록에 의존 |
| final_synthesis:48 | Daunhawer 외 2023, [arXiv:2303.09166](https://arxiv.org/abs/2303.09166) | 공통 성분과 고유 성분을 원리적으로 분리하는 이론 | 초록 | **부분** | 공유 요인의 block 식별만 증명((d) D3) |
| RQ15:35 | Santavirta 외 2025, [doi:10.1162/imag.a.134](https://doi.org/10.1162/imag.a.134) | AI 정서 라벨이 신경 분석에 쓰인 예 | 본문(PMC12410153) | **부분** | 대상은 사회 지각 feature 138개((d) D3) |

### 판정의 한계
* 표본은 Prior Literature 표와 final_synthesis의 식별자 붙은 문장에서 뽑았다. 카드 본문(8~12절)의 서술형 주장은 위 표적 점검 8건 외에는 대조하지 않았다.
* 13번(imSitu)은 제목 수준만 확인했다. CVF 페이지 등 초록 이상은 열지 않았다.
* PubMed 정보는 PubMed MCP 도구로 받았다(According to PubMed). DOI 링크는 표에 붙였다.

---

## (f) 읽은 수준 표시 점검

### 무작위 3건
* 모집단: 10개 카드 4절 표에서 읽은 수준 칸이 "본문"이고 DB나 다른 에이전트 기록에 기대지 않는다고 표시한 행 51개.
* 시드 20261112+5(위 15건 표본과 겹치지 않게 별도 시드), 스크립트 `final_citation_check/readlvl.py`.

| 카드:행 | 논문 | 카드 표시 | 카드 작성 에이전트 jsonl의 discussion_read | 판정 |
|---|---|---|---|---|
| RQ08:63 | Horikawa 2025 Mind captioning (doi:10.1126/sciadv.adw1464) | 본문 | llm-semantics: full_text (future_directions 출처 "Discussion, 한계 논의 첫째, 둘째 단락") | 일치 |
| RQ01:82 | Du 외 2023 (doi:10.1016/j.isci.2023.107571) | [본문] | geometry-info: full_text ("Limitations of the study 1~2째 단락") | 일치 |
| RQ10:77 | Ratan Murty 외 2021 (doi:10.1038/s41467-021-25409-6) | [본문-직접] | encoding-foundation: full_text ("Discussion 5, 6단락") | 일치 |

### 전수 보조 점검(51행 전체, `readlvl_all.py`)
* **기록 누락 1건:** RQ10:76 Tuckute 외 2024(doi:10.1038/s41562-023-01783-7). 카드는 "[본문-직접] bioRxiv 판(PMC10120732)의 Results와 Discussion 첫 단락"이라고 적었으나, 카드 작성자 encoding-foundation의 literature.jsonl에는 이 논문 기록이 없다. DB에는 다른 에이전트(adversarial-reviewer, generative-counterfactual)의 full_text 기록이 있고, PMC10120732는 이 논문의 bioRxiv 판이 맞다(ID 변환으로 확인). 내용 문제는 아니고 기록 문제다. encoding-foundation jsonl에 항목을 추가하거나 카드 표시를 "[본문, 다른 에이전트 DB 기록과 대조]"로 바꾸면 된다.
* 오탐 1건 설명: RQ14:68 VidSitu는 CVPR DOI로 찾으면 기록이 없지만, llm-semantics jsonl에 arXiv:2104.00990 full_text로 있다. (a)의 DB 중복 행 문제와 같은 원인이다.
* "DB 기록(본문)"으로 표시한 행은 모두 DB discussion_read가 full_text였다.

---

## (g) 검색과 확인 기록(2026-11-12)

| 도구 또는 경로 | 질의 또는 대상 | 결과 |
|---|---|---|
| 로컬 스크립트 | 대상 12개 파일에서 DOI, arXiv, PMID, PMC, OpenNeuro 번호 추출(`extract_ids.py`) | 고유 141개(논문 140, figshare 1) |
| Crossref REST API `api.crossref.org/works/{DOI}` | 대상 DOI 105개 + figshare 1개 | 첫 요청 429(속도 제한), 1.2초 간격으로 재시도 후 105/105 해석. figshare는 Crossref 404라 doi.org로 확인 |
| doi.org handle API | 10.6084/m9.figshare.11988351; 10.18112/openneuro.ds002425, ds005191, ds004872의 v1.0.0~v2.0.0 | 모두 존재 확인 |
| arXiv API `export.arxiv.org/api/query` | 대상 arXiv 35개 일괄; 초록 확인용 2604.07729, 2408.13718, 2209.10652, 2609.34742, 2509.24298, 2605.16739, 2507.00320, 2303.09166, 2304.07193, 2401.16423 | 35/35 해석, 초록 확보 |
| arXiv HTML | 2609.34742 (Xing), 2604.07729 (Sofroniew) | 전문 확보 |
| arXiv PDF | 2507.00320 (Westlin), pdftotext로 변환 | 전문 확보 |
| PubMed MCP ID 변환 | 주장 대조 대상 DOI 11개, PMC ID 4개 | 대응 확인 |
| PubMed MCP 메타데이터 | PMID 28874542, 34750593, 36950720, 27031707, 33349547, 26305927, 30532080 | 초록 확보 |
| PubMed MCP 검색 | `Semantic Space Theory computational approach to emotion[Title] AND Cowen[Author]` | PMID 33349547 |
| PubMed MCP 인용 조회 | Esteban, Nat Methods, 2019, 16:111 | PMID 30532080 |
| PubMed MCP 전문 | PMC12654933 (Gauthaman), PMC11233618 (Abdel-Ghaffar), PMC12410153 (Santavirta GPT-4V), PMC12588295 (Mind captioning), PMC10470388 (Du 2023) | 전문 확보 |
| WebSearch | `ISMRM 2025 abstract pupil arousal brain state transitions faster fMRI` | 후보 archive.ismrm.org/2025/3705.html, 1583.html(검색 색인 요약만) |

**접근이 막힌 경로(우회하지 않음)**
* journals.plos.org: DNS 실패(세션 허용 도메인 밖). PMC 전문으로 대체.
* www.ebi.ac.uk (Europe PMC): 프록시 403.
* eutils.ncbi.nlm.nih.gov: 프록시 403. PubMed MCP로 대체.
* openneuro.org: 프록시 403. DataCite DOI로 존재만 확인.
* archive.ismrm.org: 프록시 403, WebFetch DNS 실패. ISMRM 초록은 미확인으로 남김.
* direct.mit.edu: 403.
* pmc.ncbi.nlm.nih.gov 웹페이지 직접 내려받기: 세션 권한 정책이 거부하여 시도를 중단했다. PubMed MCP 전문 도구로 대체했다.

## 검증된 것과 미확인 사항
* **검증됨:** 140개 논문 식별자 존재와 서지 일치, 4개 데이터 저장소 식별자 존재, 4개 PMC ID 대응, 주장 대조 23건(무작위 15 + 표적 8), 읽은 수준 표시 3건 + 전수 51행.
* **미확인:** ISMRM 2025 초록의 존재와 내용. OpenNeuro 데이터셋 내용(존재만 확인). imSitu 초록 이상. DINOv2 학습 데이터의 C&K 프레임 포함 여부. 카드 본문 8~12절 서술 주장 대부분.

---

## Coordinator 반영 기록 (2026-11-12)

| 항목 | 처리 |
|---|---|
| B2 식별자 없는 인용 13건 | 각 파일의 첫 언급에 식별자를 붙였다. 대상: RQ14, RQ32, RQ33, RQ44, pilots의 Horikawa 2020. pilots, RQ08의 Westlin 2025. RQ60의 Du 2023. RQ01의 Stringer 2019. RQ03의 Bolt 2025. RQ44의 Gauthaman 2025. RQ15의 Tak 2025. final_synthesis의 Nguyen 2026(doi:10.7554/eLife.107955) |
| D1 ISMRM 2025 학회 초록(RQ32) | 삭제하고, 삭제 사실을 카드에 남겼다 |
| D3 final_synthesis Westlin 해석 | 범주 NMI는 거의 0, 세션 NMI도 저자는 낮다고 해석, NMI 직접 비교의 한계를 적고 시간 효과는 RQ-01 검증 대상으로 남겼다 |
| D3 Mind captioning 캡션 표현 | final_synthesis, RQ08 1절을 "정서 대신 시각 내용에 집중하라는 지시, 정서 표현은 드묾"으로 고쳤다. rq_landscape 용어 풀이에 단서를 달았다 |
| D3 Tak & Gratch 2024 | 행동 수준 예로 낮추고, 뇌 분석 예로 Huang 2026, Santavirta 2025를 들었다 |
| D3 Daunhawer 2023 | "공유 성분을 block 단위로 식별"로 고치고, 고유 성분 복원은 보장하지 않는다는 단서를 붙였다 |
| D3 RQ15 Santavirta 2025 | "사회 지각 feature 138개(일부만 정서 관련)"로 범위를 적었다 |
| (f) RQ10 Tuckute 2024 읽은 수준 기록 누락 | 카드에 "jsonl 기록 없음" 표시를 달았다 |
| 반영 후 재점검 | 카드 10장, final_synthesis, pilots의 논문 식별자를 다시 추출했다. DB verified와 불일치는 0건이다(데이터 저장소 DOI 1건 제외) |
