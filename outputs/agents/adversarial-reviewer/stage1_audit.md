# Stage 1 산출물 사실 검증 감사 (Adversarial Review)

* 작성: adversarial-reviewer (Agent 12, Adversarial Reviewer & Methodology Auditor). 커스텀 에이전트 타입이 세션에 등록되지 않아 general-purpose 에이전트가 `.claude/agents/adversarial-reviewer.md`와 `CLAUDE.md`를 직접 읽고 수행했다.
* 기준일: 2026-11-12
* 검토 대상: `outputs/stage1/dataset_Horikawa.md`, `dataset_EmoFilM.md`, `dataset_Spacetop.md`, `dataset_NSD.md`, `dataset_intelligence_report.md`(이하 "통합 보고서"), `outputs/agents/dataset-auditor/literature_{Horikawa,EmoFilM,Spacetop,NSD}.jsonl`(총 57편)
* 원칙: 검토 대상 파일은 수정하지 않았다. 작성자의 결론을 전제로 두지 않고 원 출처(논문 본문, 데이터 제공자 파일, 공개 코드)와 직접 대조했다. 작성자와 의견이 다른 부분은 5절에 이견으로 남긴다.

---

## 0. 요약

1. **핵심 수치는 대부분 원 출처와 일치한다.** Horikawa(5명, 61 run, TR 2 s, 무음, 단일 제시, 별도 평정자, Google Form 요청 경로, OpenNeuro 2020-04-24 공개), Emo-FilM(30명, 44명, 50항목, 0.38/0.39, TR 1.3 s, ds004892/ds004872, 영상 미포함, 생리 공개), Ma & Kragel (2026)(서지, 29명, 17항목, 주요 수치), Spacetop(12:1465, N=101 vs 117, `stimuli/` 공개, fMRIPrep 25.1.4, 평정 구조와 결측률, 생리 미공개), NSD(서지, 8명, 7T, 1.8 mm, TR 1.6 s, 100장), Sadeghi r = 0.22를 모두 독립적으로 확인했다. 수치를 뒤집는 오류는 찾지 못했다.
2. **심각도 높음 2건.**
   * **X1.** 통합 보고서 3.2절은 "규범 평정 vs 본인 보고"를 단일 데이터셋 안에서 직접 다룰 수 있는 곳으로 NSD(100장)를 들었지만, NSD에는 규범(별도 평정자) 평정이 없다(NSD 보고서 2.3절이 스스로 "공식 제공 없음"이라 씀). Stage 2에 잘못된 전제로 넘어간다.
   * **L1.** literature jsonl 12편(NSD 11, Emo-FilM 1)이 WebSearch 색인으로만 확인했는데 `verified_by`를 "arxiv", "publisher", "학회 공식 페이지"로 적었다. CLAUDE.md 5절 위반이며 Stage 2 문헌 DB로 그대로 전파된다. 통합 보고서 7.6절이 문제를 인지했지만 파일은 고쳐지지 않았다.
3. **심각도 중간 7건**: Emo-FilM G1 판정(공개 재구성 경로가 보고서보다 열려 있음, E8), NSD G1 판정(DAA는 약관 동의 절차이고 S3는 무계정 접근으로 안내됨, N5), Westlin (2025) 요약의 과장(H11), nsdmeadows 평정 주체와 지시문 불확실성의 소실(N4), Inter-rater 지표의 비교 불가능성(S10), Spacetop AI 연속 주석의 시간 타당화 공백(4.3절), 통합 0절 1번 문장(X7).
4. **인용 표본(시드 20261112, 16편)**: 식별자 오류 0/16, 내용 오류 0/16(부분 확인 1, 확인 불가 1), 표기 오류 3/16. **전체 오류율 18.8%(3/16), 모두 `verified_by`/`discussion_read` 표기 오류.**

---

## 1. 검증 방법과 접근 한계

### 1.1 사용한 경로

| 경로 | 내용 | 비고 |
|---|---|---|
| PubMed MCP 메타데이터 | Horikawa 2020, Emo-FilM 2025, Ma & Kragel 2026, Spacetop 2025, NSD 2022, Westlin 2025, Cowen & Keltner 2017, 표본 논문 10편 | PMID, DOI, 권호 확인 |
| PubMed MCP PMC 전문 | Horikawa 2020 (PMC7191651), Emo-FilM (PMC12019557), Ma & Kragel (PMC12891686), Spacetop (PMC12373947), Sadeghi 2024 (PMC11686310), Gao 2025 (PMC12053605), Du 2023 (PMC10470388), Doerig 2025 (PMC12364710), Khosla 2022 (PMC9561032), Asanuma 2025 (PMC12402258), Miao 2026 (PMC13223265), Yazdanpanah 2026 (PMC12912994) | 표와 그림, 보충자료는 PMC 텍스트에 없음 |
| 공개 저장소 git clone | 내가 새로 받은 사본만 사용. 위치: `/tmp/claude-0/-home-user-emotion-explore/4a0aeef6-c090-5f71-8a99-9b8e7c0f6d89/scratchpad/adv_review/` | 커밋은 부록 A. 받은 파일의 스크립트는 실행하지 않았고, git-annex 대용량 본체는 내려받지 않았다(메타데이터, 위치 기록만) |
| WebSearch | arXiv, bioRxiv, Mendeley, AWS Registry 등 직접 열 수 없는 출처 | 이 경로로만 확인한 사실은 표에 [검색]으로 표시 |

독립성: 다른 에이전트가 만든 `/home/user/kamitanilab/`, `/home/user/openneurodatasets/`, scratchpad의 `repos/`(Spacetop 담당이 받은 사본)는 사용하지 않았다.

### 1.2 열지 못한 출처

| 출처 | 상태 |
|---|---|
| arxiv.org | WebFetch가 `ENOTFOUND`로 실패(허용 도메인 밖). 이후 다른 호스트 시도 중단. arXiv 논문은 WebSearch 색인으로만 확인 |
| Cowen & Keltner (2017) PNAS 본문 | PMC5617253 전문이 도구에서 빈 문자열로 반환. Discussion의 "세 방향"은 확인 불가 |
| Westlin et al. (2025) 본문 | PMC12461804 전문이 빈 문자열. 초록과 검색 요약만 확인 |
| NSD 원 논문 본문, Data Manual, Terms & Conditions, AWS Registry 페이지 | PMC 사본 없음. 차단 기록이 있어 직접 열람 시도하지 않음. AWS Registry는 검색 색인 요약만 |
| Mendeley Data `10.17632/jbk2r73mzh.1`, Google Form, figshare 페이지 | 검색 색인 요약만 |
| git-annex 본체(Emo-FilM `code/FilmInfo.txt`, 평정 tsv.gz, Spacetop mp4 등) | S3 본체 다운로드는 하지 않음. 위치 기록(공개 원격 존재 여부)만 확인 |
| Emo-FilM Table 1과 보충표, Spacetop 영상 목록 표 | PMC 텍스트에서 누락 |

### 1.3 판정 기준

* **확인**: 원 출처(논문 본문, 데이터 제공자 파일, 코드)에서 같은 내용을 직접 봄. 2차 논문 본문으로만 확인했으면 "확인(2차 본문)"으로 적음.
* **부분 확인**: 핵심은 맞으나 세부가 다르거나, 근거가 검색 색인 수준이거나, 표현이 과장됨.
* **불일치**: 출처나 다른 보고서 서술과 모순됨.
* **확인 불가**: 이번 경로로 출처에 닿지 못함.
* 심각도: **높음** = Gate 판정, 핵심 결론, 또는 Stage 2 전제를 바꿈. **중간** = 해석이나 표현을 바꿔야 하나 결론 방향은 유지. **낮음** = 정밀도, 일관성 문제.

---

## 2. 주장별 대조표

위치 약어: [H]=dataset_Horikawa.md, [E]=dataset_EmoFilM.md, [S]=dataset_Spacetop.md, [N]=dataset_NSD.md, [I]=dataset_intelligence_report.md.

### 2.1 Horikawa

| # | 주장 | 위치 | 판정 | 근거 출처 | 심각도 | 수정안 |
|---|---|---|---|---|---|---|
| H1 | 원자료는 2026년 첫 공개가 아니라 OpenNeuro ds002425에 2020-04-24부터 CC0로 공개 | [I] 0절 4, 6절; [H] Gate 전달 사항 | 확인 | ds002425 `CHANGES`("1.0.0 2020-04-24", 1.0.1 2020-05-29, 1.0.2 2022-03-21), `dataset_description.json`("License": "CC0"), 첫 DATALAD 커밋 author date 2020-04-27. Du et al. (2023) Key resources가 ds002425와 figshare 11988351.v1을 인용 | 낮음 | 유지. 단 "figshare에 2020년부터"는 이번에 날짜를 직접 보지 못했으므로 "figshare v1(2023년 논문이 인용, 공개일 미확인)"으로 완화 |
| H2 | Mendeley 예치본 2026-04-15, 내용 미확인 | [I] 1절 표; [H] 2.1 | 부분 확인 [검색] | 검색 색인: data.mendeley.com 항목, 기여자 Horikawa, Cowen, Keltner, Kamitani, 2026-04-15, "responses to all 2185 videos" | 낮음 | 현 표기 유지 |
| H3 | 5명, 8 세션, 61 run/인, TR 2 s, 2 mm, MB4, 3T Verio | [I] 1절; [H] 1.1 | 확인 | ds002425 README; `sub-01_..._bold.json`(RepetitionTime 2.0, Verio, MultibandAccelerationFactor 4); events.tsv 집계 5명 모두 61개 | 없음 | 유지 |
| H4 | 피험자당 2,196 블록, 5명 동일 순서, 10 s 블록 1,573개, 20 s 이상 87개, 최대 94 s | [H] 1.1 | 확인 | events.tsv 직접 재집계(5명 모두 동일) | 없음 | 유지 |
| H5 | 무음 제시 | [I] 1절; [H] 2.2 | 확인 | Horikawa 2020 Discussion "only visual stimuli (with no sound)"(PMC7191651); Du 2023 "the sound of the videos was removed" | 없음 | 유지 |
| H6 | 반복 제시 없음, "내용 중복 15쌍" | [I] 1절 표 "반복 제시"; [H] 1.2 | 부분 확인 | 원 논문 Discussion "each stimulus was presented only once". 코드 `emotion2020_analysis_BATCH.m`의 `p.dupidx`는 15개 label index이고 주석은 "label index of duplicated videos. These will be removed."뿐이다. 각 index가 다른 index와 쌍을 이루는지는 코드로 알 수 없다 | 낮음 | "중복으로 표시되어 분석에서 제외된 label index 15개(쌍 구조와 중복 대상은 미확인)"로 수정. [H] 1.2가 "추정"으로 단 단서를 통합 표에도 유지 |
| H7 | 고유 비디오 2,181개 | [I] 1절; [H] 1.2 | 확인 | 본문 "2,181 unique videos"; 2,196 - 15 = 2,181. 단 같은 논문 abstract는 "fMRI responses to all 2,185 videos"라고 씀 | 낮음 | 논문 내부 불일치(abstract 2,185 vs 본문 2,181)를 1.2 표에 추가 |
| H8 | 평정 주체는 fMRI 참가자가 아닌 별도 평정자 | [I] 0절 2, 1절; [H] Gate G3 | 확인 | Limitations "the emotion ratings we used were averages from multiple raters and not from the subjects of our fMRI experiment" | 없음 | 유지 |
| H9 | MTurk 853명, 비디오당 9~17명, category 선택 비율, dimension 9점 | [I] 1절; [H] 2.3 | 확인(2차 본문) | Du 2023 STAR Methods(853명 미국 영어 사용자, 34범주 100점 척도 후 이진화, 14차원 9점 Likert, 9~17명); Asanuma 2025(9~17명, 선택 비율) | 낮음 | 유지. PNAS 원문 Methods는 여전히 미열람임을 유지 |
| H10 | 원본 비디오는 Google Form 요청 경로, G1 "요청 필요" | [I] 2절; [H] Gate G1 | 확인 | ds002425 README "you can request the videos from https://goo.gl/forms/XErJw9sBeyuOyp5Q2"; Du 2023 Key resources "Video stimuli / Cowenlab / goo.gl/forms/..." | 낮음 | 판정 유지. 대안 경로 추가 권장: Cowen & Keltner (2017) abstract(PubMed)가 "our library of videos and an interactive map ... (https://s3-us-west-1.amazonaws.com/emogifs/map.html)"를 공개했다고 명시. 형식(GIF 여부), 해상도, 이용 조건은 미확인이므로 `gate_decision.md`에 "요청 승인 전 임시 경로 후보, 확인 필요"로 기록 |
| H11 | Westlin et al. (2025)은 "원래 결론과 반대되는 재분석" | [I] 0절 4, 4.1, 5.1 #1; [H] 5절 6, 8.3 | 부분 확인 | PubMed PMID 41019207 초록: 원 논문의 범주-뇌 대응을 "did not observe ... and instead observed significant variation across individuals". 검색 요약으로 대상 데이터가 Horikawa 2020(5명, 2,196 무음 영상, 61 run)임 확인. 본문은 PMC에서도 비어 있어 미열람. arXiv preprint이며 동료심사 전 | 중간 | "반대되는 결론"은 과장이다. 재현 실패와 반대 증거는 다르다. 권장 문구: "Westlin et al. (2025, arXiv preprint, 본문 미열람)은 최소 가정 분석에서 원 논문의 범주-뇌 대응을 관찰하지 못했고 개인 간 변동이 크다고 보고했다(초록 기준)." 통합 0절 요약에도 preprint 표시 |
| H12 | 2022~2026년 재분석 다수 | [I] 0절 4 | 확인 | Fu et al. 2024 TNNLS(PMID 36346867, 온라인 2022, "two visually evoked emotional datasets"), Du 2023 본문(ds002425 사용), Westlin 2025, EmoMind 2026(arXiv:2605.16739, [검색]으로 존재와 TRIBE v2 대체 실험 확인) | 없음 | 유지 |
| H13 | Cowen & Keltner Discussion의 세 방향 | [H] 8.1 | 확인 불가 | PMC5617253 전문 비어 있음(작성자와 같은 한계) | 낮음 | [H]의 "미확인" 표기 유지. Stage 2 emotion-theory 담당에게 PNAS 본문 확인을 명시적으로 넘길 것 |

### 2.2 Emo-FilM

| # | 주장 | 위치 | 판정 | 근거 출처 | 심각도 | 수정안 |
|---|---|---|---|---|---|---|
| E1 | fMRI 참가자 30명(여 18) | [I] 1절; [E] 1.2 | 확인 | Emo-FilM 본문 Methods(32명 모집, 2명 제외, 30명, 18 female); `participants.tsv` 30행 | 없음 | 유지 |
| E2 | 평정자 44명 | [I] 1절; [E] 1.4 | 확인 | 본문 Methods; ds004872 `sub-*` 폴더 44개 | 없음 | 유지 |
| E3 | 50개 항목(55에서 5개 제외), discrete 13 + CPM 37 | [I] 1절; [E] 2.2 | 확인 | 본문; ds004872 `derivatives/Annot_*_stim.json` Columns 50개; `constants_emo_film.py` `BAD_ITEMS` 5개 | 없음 | 유지 |
| E4 | agreement 0.38(초록) vs 0.39(본문) | [I] 1절, 6절; [E] 2.3 | 확인 | Abstract "mean inter-rater agreement of 0.38"; Technical Validation "The mean agreement across all items and films was r = 0.39" | 없음 | 유지 |
| E5 | 3T TIM Trio, TR 1.3 s, 2.5 mm, MB3 | [I] 1절; [E] 1.2 | 확인 | 본문 MRI data acquisition | 없음 | 유지 |
| E6 | OpenNeuro ds004892(fMRI, v1.0.2), ds004872(평정, v1.0.3), CC0 | [I] 1절; [E] 1.1 | 확인 | 각 `CHANGES`, `dataset_description.json`(Name "Emo-FilM", "Emo-FilM Annotations", License CC0) | 없음 | 유지 |
| E7 | 원본 영상은 공개 저장소에 없음 | [I] 2절; [E] Gate G1 | 확인 | ds004892, ds004872 파일 목록에 영상 없음. EllieMo/Emo-FilM에는 washout mp4만 | 없음 | 유지 |
| E8 | G1 "요청 필요(조건부 재구성 가능)" | [I] 0절 1, 2절; [E] Gate G1 | 부분 확인, 이견 | 본문 "The films used here are all in the public domain and thus easily available for researchers who wish to extract information from them"(같은 논문의 "Creative Commons licences" 서술과 불일치는 작성자 지적대로). 절단 정보 후보 `code/FilmInfo.txt`, `code/BBL_experiment_Movies_without_credits_exp_files.xlsx`의 git-annex 위치 기록을 확인한 결과, 두 파일 모두 공개 원격 s3-PUBLIC(openneuro.org 버킷)에 존재로 기록됨. 내용은 미열람 | 중간 | G1을 "공개 원본(CC 영화) + 공개 절단 정보 파일로 재구성 가능성 높음(파일 내용 확인 필요). 실패 시 저자 요청"으로 재표기. 근거에 annex 위치 기록 추가. 통합 0절 1번 "Spacetop만 바로"도 함께 조정(X7) |
| E9 | 생리 PPG, 호흡, EDA 1000 Hz, 모든 런, 공개 | [I] 1절; [E] 1.3 | 확인 | 본문 Physiology acquisition; `*_physio.tsv.gz` 450개; `physio.json` SamplingFrequency 1000.0, Columns PPG, EDA, RESP; 무작위 25개 파일의 annex 위치 기록 모두 s3-PUBLIC 존재 | 없음 | 유지 |
| E10 | fMRI 참가자 사후 클립 평정: 영화당 5항목, 약 20%, 파일 414개, 클립 행 8,626개, "34+13=48" 산술 불일치 | [I] 1절, 4.2; [E] 2.4 | 확인 | 본문("rated five different items", "292 clips", "20.52%", "34 items ... and 13 discrete emotion terms"를 48개라 부름); `beh/*_events.tsv` 414개, 8,626행 직접 집계 | 없음 | 유지 |
| E11 | S07 영화 3편 전처리본은 v1.0.2에서 추가 | [I] 1절 표, 6절; [E] 3절 | 확인 | git 이력: raw `sub-S07_ses-5_*_bold.nii.gz`는 2023-12-15 커밋부터 존재, `derivatives/preprocessing/sub-S07/ses-5/*`는 2026-07-27 커밋에서 추가, 태그 1.0.2(2026-08-13) | 낮음 | 통합 1절 표의 "S07은 최근 버전 전까지 일부 결측"을 "S07의 영화 3편 전처리본만 v1.0.2 이전 결측(raw는 처음부터 존재)"으로 구체화 |
| E12 | Pride(Proud~Ashamed), Regard(Regard~Contempt) 양극 척도 | [I] 3.1 | 확인 | ds004872 평정자 sidecar `Levels` | 없음 | 유지 |

### 2.3 Ma & Kragel (2026)

| # | 주장 | 위치 | 판정 | 근거 출처 | 심각도 | 수정안 |
|---|---|---|---|---|---|---|
| M1 | Nat Commun 17(1):1518, doi:10.1038/s41467-025-68240-z, 2026-01-26 | [I] 0절 5, 6절; [E] 8.1 | 확인 | PubMed PMID 41588009, PMC12891686 | 없음 | 유지 |
| M2 | Emo-FilM 29명(S07 제외) | 같음 | 확인 | Methods "We excluded participant 07 due to missing data from 3 films on OpenNeuro, leaving 29 participants" | 없음 | 유지 |
| M3 | 50항목 중 17개(discrete 13 + Good, Bad, Calm, AtEase) | 같음 | 확인 | Methods "we used all 13 items ... For valence and arousal, we selected four items (valence: good, bad; arousal: calm, at ease)" | 없음 | 유지 |
| M4 | hippocampus 0.0525 vs 0.0428, vmPFC 0.0956 vs 0.0838, Spearman .978, r 약 0.04~0.10 | [I] 6절; [E] 8.1 | 확인 | Results 해당 수치와 95% bootstrap CI | 없음 | 유지 |
| M5 | leave-one-film-out 14편 | [E] 8.1 | 확인(주석) | Results는 "13 films total"이라고 쓰나 Methods는 "trained on 13 films and tested on the left-out film ... 14 validation sets". 즉 14편. 보고서 서술에 문제 없음 | 없음 | 필요 시 원문 표현 모호성만 각주 |
| M6 | 한계와 향후 과제(effort, certainty, situational control; RL 모형 비교; phase code) | [E] 8.1; jsonl | 확인 | Discussion 한계 단락 | 없음 | 유지 |

### 2.4 Spacetop

| # | 주장 | 위치 | 판정 | 근거 출처 | 심각도 | 수정안 |
|---|---|---|---|---|---|---|
| S1 | Scientific Data 12:1465, doi:10.1038/s41597-025-05154-x | [I] 1절, 6절 | 확인 | PubMed PMID 40846708 | 없음 | 유지 |
| S2 | 논문 N=101 vs 저장소 117명, 성별 표기 불일치, 41 run 전부 보유 61명 | [I] 1절, 4.3, 6절; [S] 1.1 | 확인 | 본문 Participants "101 adult participants ... 69 males, 45 females, 2 others"(합 116); `participants.tsv` 117행(F 70, M 45, O 2); BOLD 4,178개, 41 run 보유 61명 직접 집계. Yazdanpanah 2026 본문 "111 ... 68 females, 41 males, and 2 others" | 없음 | 유지 |
| S3 | `stimuli/` 공개, G1 "공개 다운로드 가능" | [I] 0절 1, 2절; [S] Gate G1 | 확인(alignvideo 기준) | 본문 Data Records "a stimuli/ directory hosts all the stimuli presented in the functional tasks"; ds005256 tag 1.1.0 `stimuli/` 8개 과제 폴더; alignvideo mp4 49개 전부 annex 위치 기록상 s3-PUBLIC(e5f1e780) 존재(`s3-PUBLIC-dead` 원격과 구분해 재확인). 다른 과제의 annex 파일은 이번에 점검하지 않음 | 낮음 | 판정 유지. "실제 다운로드 미실행", 제3자 저작권 단서 유지 |
| S4 | ds007070 v1.0.3(2026-04-06), fMRIPrep 25.1.4, 117명, 4,178 run, MNI + fsLR 91k; 논문은 21.0.2 | [I] 1절; [S] 1.4 | 확인 | `dataset_description.json` GeneratedBy fMRIPrep 25.1.4; `CHANGES`; `code/run`(`fmriprep_25_1_4.sif`); MNI preproc 4,178개, dtseries 4,178개; 논문 "fMRIPrep 21.0.2" | 없음 | 유지 |
| S5 | alignvideo: 영상 후 7차원 각 5초, 클릭해야 저장 | [I] 4.3; [S] 2.2 | 확인 | 본문 task-alignvideo; `task-alignvideo_events.json`; spatialtopology/task-alignvideos `scripts/rating_scale.m`(`button(1)`일 때만 `ratings(i)` 기록, 4.5 s 경과 시 종료) | 없음 | 유지 |
| S6 | alignvideo 평정 약 51% 결측 | [I] 1절, 2절; [S] Gate G3 | 확인 | 직접 재계산: 평정 이벤트 35,896개 중 값 있음 17,491개(48.7%), 참가자 중앙 완료율 0.477, 값이 하나라도 있는 참가자 109/116 | 없음 | 유지 |
| S7 | 생리(EDA, PPG) 기록했으나 공개 파일 없음 | [I] 1절, 6절; [S] 2.3 | 확인 | ds005256 tag 1.1.0과 ds007070에 `*physio*` 파일 0개; 본문은 "concurrent fMRI and physiological recordings of skin conductance and photoplethysmography"; 코드 기본 샘플링 2000 Hz(`qc01_outlierdetection.py`) | 없음 | 유지 |
| S8 | 행렬 64×64(논문) vs 82(JSON) | [I] 4.3; [S] 1.2 | 확인 | 본문 "64 × 64 matrix"; `task-*_acq-mb8_bold.json` BaseResolution 82 | 없음 | 유지 |
| S9 | tornado 두 파일 | [S] 2.2 | 확인 | `ses-02_..._content-tornado.mp4`(약 25.3 MB), `ses-04_..._content-tornado.mp4`(약 20.9 MB), annex 키 상이 | 없음 | 유지 |
| S10 | Inter-rater 지표 표: Emo-FilM "평균 r 0.38" 옆에 Spacetop "split-half 0.94~0.99" | [I] 1절 표 | 확인 불가(재계산 안 함) + 비교 문제 | 두 값은 다른 지표다. Emo-FilM은 개인 평정자 쌍별 1 Hz 시계열 Pearson r의 평균, Spacetop은 영상당 약 51명 집단 평균의 Spearman-Brown split-half(49개 영상 점) | 중간 | 표에 "지표가 달라 직접 비교 불가"를 명시하고, 개인 수준 비교값으로 Spacetop의 "개인 대 나머지 집단 상관 중앙값 0.46~0.77"([S] 2.2)을 함께 기재 |

### 2.5 NSD

| # | 주장 | 위치 | 판정 | 근거 출처 | 심각도 | 수정안 |
|---|---|---|---|---|---|---|
| N1 | Nat Neurosci 25(1):116-126, doi:10.1038/s41593-021-00962-x, PMID 34916659 | [I] 1절, 6절 | 확인 | PubMed 메타데이터(PMC 없음) | 없음 | 유지 |
| N2 | 8명, 7T, 1.8 mm, TR 1.6 s, 30~40 세션, 9,000~10,000장, 3회, shared 1,000/515 | [I] 1절; [N] 1절 | 확인(2차 본문) | Doerig 2025 Methods(PMC12364710) 해당 문장 전부; Pennock 2023 초록("8 participants ... up to 30,000 trials") | 낮음 | 원 논문 미열람 표시 유지 |
| N3 | nsdmeadows valence/arousal 100장 | [I] 1절, 2절; [N] 2.2 | 확인(2차 본문) | Khosla 2022(PMC9561032) "These ratings were released for a total of 100 images from the shared image set viewed by all NSD participants"; Sadeghi 2024 "A small subset of images (n = 100) were rated on valence". "+3장"은 [검색] | 없음 | 유지 |
| N4 | 평정 주체는 NSD 참가자 본인(스캔 후) | [I] 0절 2, 1절, 3.2; [N] Gate G3 | 부분 확인 | Khosla 2022의 "subject-averaged valence and subject-averaged arousal ratings" 표현이 참가자 평정을 시사. 원문, 지시문(felt vs perceived)은 미확인 | 중간 | [N]은 [B] 등급으로 단서를 달았지만 [I] 0절 2와 3.2 표는 단정형이다. "[2차 근거], 지시문 미확인으로 '느낀 정서'인지 '이미지 정서 판단'인지 구분 불가"를 [I] 0절 2와 3.2에 그대로 옮길 것 |
| N5 | DAA 요구, G1 "요청 필요" | [I] 0절 1, 2절; [N] Gate G1 | 부분 확인, 이견 | 검색 색인의 AWS Registry 항목: "AWS CLI Access (No AWS account required)" `aws s3 ls --no-sign-request s3://natural-scenes-dataset/`와 "To receive access to the NSD Data Manual, please fill out the NSD Data Access Agreement Form"이 함께 나타남. 제3자 미러(Hugging Face NSD-Flat LICENSE)가 판매, 수익화 금지 조항을 보여 주나 공식 원문과의 일치는 미확인 | 중간 | "요청 필요"는 승인 대기를 함의한다. "약관(DAA) 양식 제출과 동의 후 다운로드. S3 버킷은 무계정 접근으로 안내됨([검색]). 승인 심사 여부 미확인"으로 재표기. 약관 동의 의무는 그대로 강조 |
| N6 | NSD 이미지 valence는 대체로 중립 | [I] 4.4; [N] 2.4 | 확인 | Sadeghi 2024 "Images were selected from various categories but were largely neutral in valence" | 없음 | 유지 |

### 2.6 2차 문헌 주장

| # | 주장 | 위치 | 판정 | 근거 출처 | 심각도 | 수정안 |
|---|---|---|---|---|---|---|
| L2 | Sadeghi et al. (2024) VV 모델과 nsdmeadows valence r = 0.22 | [N] 2.4(d), 부록 A | 확인 | PMC11686310: "t(98) = 2.23, p = 0.028, r = 0.22, 95% confidence interval = (0.02, 0.39)". 저수준 VV 모델 예측과 100장 평정의 상관. Sadeghi 본문은 100장의 평정 주체를 쓰지 않음 | 없음 | 유지. "평정 주체는 Sadeghi가 아니라 다른 출처 근거"임을 각주로 |
| L3 | Gao et al. (2025): 일상 장면 정서 평정은 객체 표상으로 "대부분 예측된다" | [I] 4.4; [N] 6절 | 부분 확인 | PMC12053605: 300명이 BOLD5000 4,913장에 20개 범주 판단. AlexNet(fc8)이 EmoNet보다 정서 판단 예측이 높음(차이 0.115, EmoNet 정확도 0.292, permutation p < 0.001). Cowen & Keltner 자극에서는 EmoNet이 우위. LOC가 시각 영역 중 최고 | 낮음~중간 | "대부분 예측"은 근거 없는 크기 진술이다. "객체 인식 모델이 정서 특화 모델보다 20범주 정서 판단을 더 잘 예측했다(20-way 분류 정확도 기준, 절대 설명량은 크지 않음)"로 수정. [N] 2.4(d)의 표현은 정확하므로 그 문장으로 통일 |
| L4 | Westlin et al. (2025) | H11 참조 | 부분 확인 | | 중간 | H11 수정안 |
| L5 | Du et al. (2025) arXiv:2509.24298: MLLM 표상이 인간 평정보다 뇌를 더 잘 예측 | [H] 8.3, 8.4; [E] 4절 | 확인 [검색] | 검색 색인: 2025-09-29 제출, 저자 Du, Lu, Huang, Sun, Zhou, Qin, He; 2,180 영상, odd-one-out, 30차원 embedding | 낮음 | 내용 유지. [E] jsonl의 저자 표기("Du C, He H, 외")와 `verified_by` 표기는 3절 참조 |
| L6 | "Higher-order topology ..." bioRxiv 2026 | [E] 8.2 | 확인 [검색] | Sciety 색인: DOI 10.64898/2026.09.26.754452, 14편 2.5시간 이상, 50개 affective feature(즉 Emo-FilM), homological scaffold, pairwise는 arousal | 낮음 | 통합 5.2절 #5(동역학 모형)와 #1(appraisal 공간)에 "partially 겹침 가능, 미검증 preprint" 표시 |

### 2.7 통합 판정과 문서 간 일관성

| # | 주장 | 위치 | 판정 | 근거 | 심각도 | 수정안 |
|---|---|---|---|---|---|---|
| X1 | "규범 평정 vs 본인 보고가 뇌 반응을 얼마나 다르게 설명하는가"는 단일 데이터셋 안에서 Emo-FilM(부분)과 NSD(100장)에서만 직접 다룰 수 있다 | [I] 3.2 | **불일치** | NSD 보고서 2.3 "별도 평정자의 규범적 평정: NSD 공식 제공 없음". Khosla 2022, Sadeghi 2024 어디에도 NSD 100장의 별도 규범 평정은 없다. 같은 통합 보고서 3.2 표에서도 NSD는 "참가자 본인" 칸에만 있다 | **높음** | NSD는 단일 데이터셋 안에서 "본인 보고 vs AI 추정"만 가능하고 "규범"은 신규 수집이 전제라고 수정. 연동 수정: 5.4 #2와 5.5 #1에 "신규 규범 평정 수집 필요" 명시. Emo-FilM 쪽도 본인 보고가 "스캔 후 클립 재시청 회고 평정, 항목×영화당 3~4명, 영화 길이의 약 20%"라 참가자 개인 수준 비교가 어렵다는 제약을 같은 문장에 적을 것 |
| X2 | 3.2 표가 "Spacetop (alignvideo 7차원 등)"을 "fMRI 참가자 본인" 칸에 묶음 | [I] 3.2 | 부분 불일치 | [S] 2.1은 faces(타인 표정 강도), shortvideo(인물 정서 귀속)를 "참가자의 타인 지각/귀속 판단"으로 따로 구분했다. "등"이 이 구분을 지운다 | 낮음~중간 | 3.2 표에 "참가자의 타인 정서 지각/귀속" 행이나 열을 추가하고 faces, shortvideo를 옮긴다 |
| X3 | 3.1 판정 기준 "다섯 가지 중 하나라도 크게 다르면 직접 결합 불가" | [I] 3.1 | 논리 점검 | 이 기준이면 모든 쌍이 같은 판정이 되어 판정이 쌍을 구별하지 못한다. 실제 근거 열은 쌍마다 가능한 수준(순위/RSA, 집계 후 이름 대응, 공통 모델 공간)을 다르게 적고 있다 | 낮음 | 단계형 판정 열 추가: (1) 라벨 풀링 가능, (2) 이름 대응 항목의 순위/RSA 비교 가능, (3) 공통 모델 feature 공간 경유만 가능. 예: Horikawa-Emo-FilM (2), Emo-FilM-Spacetop (2, 집계 후), 나머지 (3) |
| X4 | 데이터셋 보고서 간 판정 불일치 | [E] 7절 "Spacetop 부분 결합 가능", [H] 7절 "Spacetop 미확인" vs [I] 3.1 "직접 결합 불가" | 불일치(문서 간) | 각 보고서 원문 | 낮음 | 통합 판정을 채택하더라도 데이터셋 보고서에 "통합 보고서 3.1이 대체함"을 주석으로 남기고, 판정 차이를 이견으로 기록(CLAUDE.md 4절 "실제 의견 충돌은 지우지 않고 기록") |
| X7 | "Spacetop만 공개 저장소에서 바로 받을 수 있고" | [I] 0절 1 | 부분 확인 | 자극 기준으로는 맞다. 그러나 E8대로 Emo-FilM도 공개 원본과 공개 절단 정보로 재구성할 가능성이 높다 | 중간 | E8 반영 시 "Spacetop은 바로, Emo-FilM은 공개 재료로 재구성 가능성 높음(확인 필요)"으로 |

---

## 3. 인용 표본 검증

### 3.1 표본 추출

* 방법: Python `random.seed(20261112)` 후 파일마다 `random.sample(range(n), 4)`. 파일 순서 Horikawa, EmoFilM, Spacetop, NSD. 총 16편(파일당 4편).
* 추출 결과(0부터 센 줄 번호): Horikawa [3, 6, 8, 11], EmoFilM [1, 3, 9, 10], Spacetop [1, 2, 3, 5], NSD [6, 7, 15, 17].
* 점검 항목: (a) 식별자가 실제 그 논문으로 연결되는가, (b) main_findings, future_directions, section이 원문과 맞는가, (c) `verified_by`와 `discussion_read`가 CLAUDE.md 5절 기준에 맞는가.

### 3.2 결과

| # | 파일:줄 | 식별자 | (a) 식별자 | (b) 내용 | (c) 표기 | 판정 |
|---|---|---|---|---|---|---|
| 1 | Horikawa:3 | 10.1109/TNNLS.2022.3217767 (Fu 2024) | 확인: PMID 36346867, TNNLS 35(7):9026-9040 | 확인: 초록 "two visually evoked emotional datasets", 기존보다 우수 | 맞음(pubmed, abstract_only) | 정확 |
| 2 | Horikawa:6 | arXiv:2507.00320 (Westlin 2025) | 확인: PMID 41019207, PMC12461804 | 확인: 초록과 일치 | 맞음(pubmed, abstract_only. PMC 전문이 비어 있어 타당) | 정확 |
| 3 | Horikawa:8 | 10.1038/s41598-025-14961-6 (Asanuma 2025) | 확인: PMID 40890212 | 확인(전문): 9~17명, 선택 비율을 강도로 해석, 참가자 수준 자료 비공개, 모델당 비디오별 단일 응답, "Towards more human-like emotional understanding" 절의 interoceptive 신호와 새 평가 틀 | 맞음(pubmed, full_text) | 정확 |
| 4 | Horikawa:11 | arXiv:2503.13981 (Shariatpanahi 2025) | 확인 [검색]: arXiv 목록, 2025-03-18, q-bio.NC | 확인 [검색]: 5명, 2,185 영상, 평균 r 약 0.7 | 투명 표기("arxiv (search index only)"). 단 CLAUDE.md 5절상 verified로 세면 안 됨 | 정확(검색 수준) |
| 5 | EmoFilM:1 | 10.1038/s41467-025-68240-z (Ma & Kragel 2026) | 확인 | 확인(전문): 수치, 한계, RL 비교, 절 위치 | 맞음 | 정확 |
| 6 | EmoFilM:3 | 10.1016/j.neubiorev.2025.106089 (Ma, Vafaie, Kragel 2025) | 확인: PMID 40057255, NBR 172:106089 | 확인: 초록의 circumplex 전이 학습 가설 | 맞음 | 정확 |
| 7 | EmoFilM:9 | 10.64898/2026.09.26.754452 (Higher-order topology) | 확인 [검색]: Sciety 색인 | 확인 [검색]: scaffold, VAD 축소 시 이점 감소, pairwise는 arousal | 투명 표기("none ...") | 정확(미검증 표기 정확) |
| 8 | EmoFilM:10 | arXiv:2509.24298 (Du 2025) | 확인 [검색] | 확인 [검색] | **오류**: limitations에 "존재는 검색 결과의 arxiv.org 항목으로 확인"이라 쓰고 `verified_by`는 "arxiv". 같은 논문을 Horikawa 파일은 "arxiv (search index only)"로 적어 파일 간 불일치. citation 저자 "Du C, He H, 외"도 불완전(실제 Du, Lu, Huang, Sun, Zhou, Qin, He) | 표기 오류 |
| 9 | Spacetop:1 | 10.1101/2024.06.21.599974 (Jung 2024 preprint) | 확인: PMID 38979212, PMC11230225 | 확인: 초록 | 맞음(pubmed, no) | 정확 |
| 10 | Spacetop:2 | 10.1038/s41467-026-71151-2 (Miao 2026) | 확인: PMID 41935085 | 확인(전문): split-half 0.98, 0.92, 상관 0.32, fMRI 90명, Limitations 첫째 항목(집단 수준 추론), V3/V4 단락의 향후 과제 | 맞음 | 정확 |
| 11 | Spacetop:3 | 10.1073/pnas.2513856123 (Yazdanpanah 2026) | 확인: PMID 41662518 | 확인(전문): 111명(68 F, 41 M, 2 O), precision 가중치 변화 미반영 한계 | 맞음 | 정확 |
| 12 | Spacetop:5 | arXiv:2606.09770 (Topo-Omni) | 확인 [검색]: 2026-06-08, AlKhamissi 외 | **확인 불가**: 내 검색 결과는 "four human subjects"의 fMRI 선택성 지도만 언급하고 Spacetop 사용을 보여 주지 않음 | 투명 표기("unverified") | 내용 확인 불가(오류 아님) |
| 13 | NSD:6 | 10.1016/j.cub.2022.11.063 (Pennock 2023) | 확인: PMID 36574774 | 확인: 초록 | 맞음 | 정확 |
| 14 | NSD:7 | 10.1038/s42003-023-04546-2 (Jain 2023) | 확인: PMID 36792693 | 확인: 초록 | 맞음 | 정확 |
| 15 | NSD:15 | arXiv:2508.14214 (Ogg 2025) | 확인 [검색]: 2025-08-19, cs.AI | 부분 확인 [검색]: 다수 조건에서 r ≥ 0.9, arousal 정렬 최약, LLM 평정 균질 확인. 기록된 valence 0.89, arousal 0.81 수치는 내 검색에서 확인 못 함 | **오류**: main_findings가 "검색 요약 기준"인데 `verified_by` "arxiv", `discussion_read` "abstract_only" | 표기 오류 |
| 16 | NSD:17 | arXiv:2403.11207 (MindEye2) | 확인 [검색] | 확인 [검색]: "full 40 sessions of NSD data, which was not released until the recent completion of the 2023 Algonauts challenge" | **오류**: main_findings가 본문 서술을 인용하면서 `discussion_read` "abstract_only", `verified_by` "arxiv"인데 실제 경로는 검색 요약 | 표기 오류 |

### 3.3 오류율

| 구분 | 건수 | 비율 |
|---|---|---|
| 식별자 오류(다른 논문으로 연결, 존재하지 않음) | 0/16 | 0% |
| 내용 오류(원문과 모순) | 0/16 | 0% (부분 확인 1, 확인 불가 1) |
| 표기 오류(`verified_by`, `discussion_read`, citation) | 3/16 | 18.8% |
| **하나 이상 오류가 있는 항목** | **3/16** | **18.8%** |

데이터셋별: Horikawa 0/4, EmoFilM 1/4, Spacetop 0/4, NSD 2/4.

### 3.4 전수 점검: 검색 색인 확인을 verified로 표기한 항목

표본 밖까지 57편 전체의 `verified_by`를 훑었다.

| 파일 | 항목(줄 번호: 식별자) | 현재 `verified_by` | 실제 확인 경로(보고서 자체 서술 기준) |
|---|---|---|---|
| NSD | 15: arXiv:2508.14214, 16: arXiv:2301.03198, 17: arXiv:2403.11207, 18: arXiv:2506.06898, 19: arXiv:1405.0312, 20: arXiv:1504.00325, 24: arXiv:2404.19438 | "arxiv" | WebSearch 색인([N] 부록 B "WebSearch 색인으로만 확인 10편(arXiv 7, ...)") |
| NSD | 21: arXiv:1510.01431(SentiCap, AAAI), 23: 10.1101/2025.05.08.651182, 27: 10.1101/2025.09.18.677029 | "publisher" | WebSearch 색인(같은 서술의 "bioRxiv 2, AAAI 1") |
| NSD | 22: VSS2025-presentation-1989 | "학회 공식 페이지 (visionsciences.org)" | [N] 2.4(b)가 "[B, 학회 초록만 확인]"으로 등급 표기. [B]는 WebSearch 색인. 의심 항목 |
| EmoFilM | 10: arXiv:2509.24298 | "arxiv" | limitations에 "검색 결과의 arxiv.org 항목으로 확인" |
| Horikawa | 5, 7, 9, 11(arXiv), 10(PMLR) | "arxiv (search index only)", "publisher (PMLR page via search index only)" | 투명 표기. 단 다른 파일과 형식이 달라 기계적으로 집계하면 verified로 잘못 셀 위험 |
| Spacetop | 5: arXiv:2606.09770 | "unverified (...)" | 투명 표기 |

결론: **12편(NSD 11, EmoFilM 1)이 검색 색인 확인을 "arxiv", "publisher", "학회 공식 페이지"로 적어 verified처럼 보이게 했다.** 보고서 본문([N] 부록 B)은 정직하게 구분했으므로 날조는 아니지만, jsonl은 Stage 2 `literature_db.csv`의 입력이라 CLAUDE.md 5절 위반이 그대로 전파된다. 또한 검색 요약만 본 항목 다수(NSD 15~21, 23, 27; Horikawa 5, 7, 9, 10, 11)가 `discussion_read: "abstract_only"`인데, 초록 원문을 연 것이 아니라 검색 요약을 본 것이다.

수정안(L1, 심각도 높음):
1. `verified_by` 값에 `search_index`를 추가하고 위 12편과 Horikawa 5편, Spacetop 1편을 모두 `search_index`로 통일한다. verified 집계에서 제외한다.
2. `discussion_read`에 `search_summary`를 추가하거나, 초록 원문을 직접 연 경우만 `abstract_only`로 쓴다.
3. 같은 논문(arXiv:2509.24298)이 두 파일에 다른 표기로 들어간 것을 하나로 맞추고 저자를 완전히 적는다.
4. arXiv 항목은 arxiv.org가 허용되면 재확인하고, 그 전까지 Stage 2 근거로 쓸 때 "[검색]" 표시를 유지한다.

---

## 4. 판정 논리와 Safeguards 점검

### 4.1 Gate 판정

| 데이터셋 | Gate | 작성자 판정 | 내 판단 | 근거 |
|---|---|---|---|---|
| Horikawa | G1 | 요청 필요 | **동의** | README와 Du 2023의 요청 경로. 대안 경로(공개 interactive map)는 H10대로 후보로 추가 |
| Horikawa | G2 | 사용 가능 | 동의 | raw BIDS 직접 확인. 전처리본 형식은 코드와 2차 본문 근거 |
| Horikawa | G3 | 공개, 별도 평정자 | 동의 | H8, H9 |
| Emo-FilM | G1 | 요청 필요(조건부 재구성) | **이견**(E8) | 공개 CC 영화 + 공개 원격에 있는 절단 정보 후보 파일. "재구성 가능성 높음, 확인 필요"가 더 정확 |
| Emo-FilM | G2 | 사용 가능 | 동의 | 제공 전처리본의 6 mm smoothing, WM/CSF 회귀 상태 서술 확인 |
| Emo-FilM | G3 | 공개, 별도 평정자 44명 | 동의 | E2, E3. consensus가 평정자 내 z-score 상대값이라는 단서 유지 |
| Spacetop | G1 | 공개 다운로드 가능 | 동의(alignvideo 기준 확인) | S3. 제3자 영상 저작권 단서 유지 |
| Spacetop | G2 | 사용 가능 | 동의 | S4 |
| Spacetop | G3 | 공개, 참가자 본인 사후 평정 | 동의 | S5, S6 |
| NSD | G1 | 요청 필요(DAA) | **이견**(N5) | DAA는 약관 동의 절차이고 S3는 무계정 접근으로 안내됨([검색]) |
| NSD | G2 | 고수준 전처리 | 동의(2차 근거) | N2 |
| NSD | G3 | 정서 라벨 사실상 없음, 100장 본인 평정 | 대체로 동의 | N3, N4(평정 주체와 지시문 불확실성 유지 필요) |

어느 이견도 "불가"를 만들지 않는다. 모델 기반 연구 가능성 결론은 바뀌지 않고, Emo-FilM과 NSD는 오히려 접근 장벽이 작성자 판단보다 낮을 수 있다.

### 4.2 Cross-dataset Compatibility(통합 3절)

* "모든 쌍 직접 결합 불가" 결론 자체는 근거와 맞다. 평정 주체, 척도, 시간 해상도, 모달리티가 쌍마다 실제로 다르다(H8, E3, S5, N3 확인).
* 다만 판정 기준이 이분법이라 정보가 없다(X3). 단계형 판정을 권한다.
* 3.2절의 NSD 서술은 사실 오류다(X1, 높음).
* 3.2 표의 "본인" 칸이 본인 경험 보고와 타인 지각 판단을 섞는다(X2).
* 데이터셋 보고서와 통합 보고서의 판정 차이를 기록 없이 덮었다(X4).

### 4.3 Safeguards(CLAUDE.md 6절) 점검

| Safeguard | 상태 | 지적 |
|---|---|---|
| 참가자 경험 vs 자극 정서 | 대체로 잘 구분. Horikawa [H] 2.4, Emo-FilM [E] 2.5, Spacetop [S] 2.1, NSD [N] 2.3 모두 다섯 출처 표가 있다 | X2(3.2 표에서 지각/귀속 판단이 본인 보고에 섞임), N4(nsdmeadows 지시문 미확인인데 요약은 "본인 보고"로 단정) |
| 인간 vs 모델 라벨 | 모든 보고서가 AI 라벨을 "AI 추정 정서"로 따로 표기 | **Spacetop AI 연속 주석 타당화 공백(중간)**: [I] 5.3 #3과 [S] 8 #3은 AI가 만든 연속 정서 주석을 영상 단위 평정(49개 점)으로 타당화한 뒤 time-resolved encoding에 쓰자고 한다. 영상 단위 집계값은 영상 안 시간 축의 타당성을 검증하지 못한다. 수정안: 시간 타당성은 Emo-FilM 1 Hz 인간 consensus로 먼저 검증하고(도메인 차이 기록), Spacetop에서는 영상 단위 집계값만 검증 대상으로 명시. 시간 축 결과는 "미검증 AI 추정 시계열"로 표기 |
| 규범 vs 본인 보고 | 데이터셋별 구분은 정확 | X1(NSD에 규범 평정 없음) |
| 정서 vs 시각-의미 표상 | 공선성 문제를 각 보고서가 인지 | L3(Gao 2025 결과를 "대부분 예측"으로 과장) |
| Decodability vs representation | Ma & Kragel 해석에서 "independent observers" 평정임을 명시([E] 6절 1) | 문제 없음 |
| Inter-rater agreement, label noise | Emo-FilM 0.38/0.39와 항목별 범위 정확 | S10(다른 지표를 같은 열에 나란히 둠) |
| Repeated stimulus, leakage | Horikawa 중복 index, Spacetop tornado와 shortvideo, NSD 3회 반복 모두 기록 | H6(중복 "쌍" 표현은 추정) |
| Exploratory vs confirmatory | Spacetop 신뢰도 계산에 "탐색적" 표시 | H11(preprint 초록 하나를 요약 4번의 헤드라인으로 승격) |
| Data access, license | 대부분 "미확인"을 정직하게 표시 | E8, N5(G1 범주가 실제 접근 경로보다 보수적일 수 있음) |
| Pretrained contamination | 모든 보고서가 언급 | 문제 없음 |

---

## 5. 이견 기록(작성자와 다른 판단)

합의를 서두르지 않고 그대로 남긴다. Coordinator가 채택 여부를 정하고, 채택하지 않더라도 이 기록은 지우지 않기를 권한다.

1. **Emo-FilM G1.** 작성자: "요청 필요(조건부 재구성 가능)". 리뷰어: "공개 재료로 재구성 가능성 높음(확인 필요)". 근거는 E8(논문의 공개 서술, 절단 정보 후보 파일이 s3-PUBLIC에 존재). 리뷰어도 파일 내용은 보지 못했으므로 확정은 아니다.
2. **NSD G1.** 작성자: "요청 필요(DAA)". 리뷰어: "약관 동의 후 다운로드, 승인 심사 여부 미확인". 리뷰어 근거도 검색 색인 수준(N5)이라 양쪽 모두 원문 확인이 필요하다.
3. **Westlin (2025)의 위상.** 작성자: 원래 결론과 "반대되는" 재분석, 요약 4번의 핵심 사실. 리뷰어: 재현 실패를 보고한 preprint이며 본문 미열람. 반대 증거로 쓰지 말고 "분석 가정 민감도의 시험대" 근거로만 쓰는 것이 적절하다.
4. **`verified_by` 문제의 처리 시점.** 작성자(통합 7.6): Stage 2 문헌 통합 전에 필드 통일. 리뷰어: Stage 1 산출물 자체가 CLAUDE.md 5절을 어기므로 지금 고쳐야 한다.
5. **Cross-dataset 판정 방식.** 작성자: 이분법(하나라도 다르면 불가). 리뷰어: 단계형 판정이 Stage 2에 더 유용하다. 결론(직접 결합 불가)에는 동의한다.

---

## 6. Coordinator 수정 체크리스트(우선순위 순)

| 순위 | 대상 | 조치 | 항목 |
|---|---|---|---|
| 1 | [I] 3.2, 5.4 #2, 5.5 #1 | NSD에는 규범 평정이 없음을 반영해 문장 수정, "신규 규범 평정 수집 전제" 명시 | X1 |
| 2 | literature jsonl 4개 | `search_index` 값 도입, 12편 재표기, `discussion_read` 기준 통일, arXiv:2509.24298 중복 표기 통일 | L1, 3.4 |
| 3 | [I] 0절 1, 2절, `gate_decision.md` | Emo-FilM, NSD G1 문구 재표기(이견 병기) | E8, N5, X7 |
| 4 | [I] 0절 4, 4.1, 5.1 #1; [H] 8.3 | Westlin을 preprint, 초록 기준, "재현 실패"로 표현 | H11 |
| 5 | [I] 0절 2, 3.2 | nsdmeadows 평정 주체와 지시문 불확실성 명시 | N4 |
| 6 | [I] 1절 표 | Inter-rater 지표 비교 불가 명시, Spacetop 개인 수준 값 병기 | S10 |
| 7 | [I] 5.3 #3; [S] 8 #3 | AI 연속 주석의 시간 타당화 경로 수정 | 4.3 |
| 8 | [I] 4.4; [N] 6절 | Gao 2025 표현 수정 | L3 |
| 9 | [I] 3.1, 3.2 | 단계형 판정 열, 지각/귀속 행 추가, 문서 간 판정 차이 주석 | X2, X3, X4 |
| 10 | [I] 1절 표, [H] 1.2 | 중복 15개 표현, S07 결측 범위, abstract 2,185 vs 본문 2,181 | H6, H7, E11 |
| 11 | `gate_decision.md` | Horikawa G1 대안 후보(공개 interactive map) 기록 | H10 |
| 12 | [I] 5.2 | Higher-order topology preprint와의 부분 겹침 표시 | L6 |

---

## 부록 A. 재현 정보

내가 새로 받은 저장소(모두 `/tmp/claude-0/-home-user-emotion-explore/4a0aeef6-c090-5f71-8a99-9b8e7c0f6d89/scratchpad/adv_review/` 아래, `git clone --filter=blob:limit`):

| 저장소 | 커밋 | 날짜 |
|---|---|---|
| OpenNeuroDatasets/ds002425 | 3f94b2b | 2022-03-21 |
| OpenNeuroDatasets/ds004892 | cdf68fe44 (tag 1.0.2) | 2026-08-13 |
| OpenNeuroDatasets/ds004872 | e9b1bf0b | 2024-04-05 |
| OpenNeuroDatasets/ds005256 | 3740e41a98 (tag 1.1.0) | 2025-03-13 |
| OpenNeuroDatasets/ds007070 | f24817ca463 | 2026-04-06 |
| EllieMo/Emo-FilM | 8a358f8 | 2024-04-13 |
| KamitaniLab/EmotionVideoNeuralRepresentation | 8fe23a0 | 2024-08-21 |
| KamitaniLab/EmotionVideoNeuralRepresentationPython | 451236c | 2025-11-19 |
| spatialtopology/task-alignvideos | 0fffba3 | 2025-10-02 |
| spatialtopology/spacetop-prep | 94edba0 | 2025-03-03 |

git-annex 공개 여부 판정 방법: `origin/git-annex` 브랜치의 `remote.log`에서 `name=s3-PUBLIC`(ds005256은 e5f1e780, ds004892는 aced8ee0) UUID를 찾고, 해당 키의 `.log`에서 그 UUID의 최신 상태가 1인지 확인했다. 이는 "공개 원격에 존재로 기록됨"을 뜻하며 실제 다운로드 성공을 뜻하지 않는다.

PMC 전문에서 뽑은 텍스트는 같은 폴더의 `txt/`에 있다(horikawa2020, makragel2026, sadeghi2024, gao2025, du2023, doerig2025, khosla2022, asanuma2025, miao2026, yazdanpanah2026).
