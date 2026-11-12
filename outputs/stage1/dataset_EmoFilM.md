# Dataset Forensic Audit: Emo-FilM (Morgenroth et al., 2025)

* 작성: dataset-auditor (Agent 1, Dataset & Metadata Specialist). general-purpose 에이전트가 `.claude/agents/dataset-auditor.md` 지침을 직접 읽고 수행함.
* 기준일: 2026-11-12
* 대상 논문: Morgenroth E, Moia S, Vilaclara L, Fournier R, Muszynski M, Ploumitsakou M, Almató-Bellavista M, Vuilleumier P, Van De Ville D. (2025) Emo-FilM: A multimodal dataset for affective neuroscience using naturalistic stimuli. *Scientific Data* 12:684. [doi:10.1038/s41597-025-04803-5](https://doi.org/10.1038/s41597-025-04803-5), PMID 40268934, [PMC12019557](https://pmc.ncbi.nlm.nih.gov/articles/PMC12019557/). Preprint: [doi:10.1101/2024.02.26.582043](https://doi.org/10.1101/2024.02.26.582043)
* 우리 환경의 데이터 경로: **미확인** (`reference/datasets_and_resources.md` 1절이 비어 있음)

## 0. 검증 방법과 한계 (먼저 읽을 것)

| 확인 경로 | 무엇을 확인했나 | 상태 |
|---|---|---|
| PubMed / PMC 전문 (PMC12019557) | 논문 Background, Methods, Data Records, Technical Validation | 읽음. 단 PMC 추출본에서 **이탤릭 항목명과 영화명이 빠져 있고**, Table 1, Supplementary Table, Usage Notes, Code availability 절이 보이지 않음 |
| OpenNeuro GitHub 미러 `OpenNeuroDatasets/ds004892` (v1.0.2, commit cdf68fe, 2026-08-13) | fMRI 데이터 전체 파일 목록, sidecar JSON, events TSV, participants.tsv, 사후 검증 평정 TSV, CHANGES, dataset_description | git 메타데이터를 직접 읽음 (git-annex 대용량 파일 본체는 받지 않음) |
| OpenNeuro GitHub 미러 `OpenNeuroDatasets/ds004872` (v1.0.3, commit e9b1bf0, 2024-04-05) | 평정자 44명의 원자료 파일 목록, 55개 항목 정의 JSON, consensus 파일 목록 | 위와 같음. 평정 시계열(.tsv.gz) 본체는 annex라 수치는 미열람 |
| 저자 코드 [github.com/EllieMo/Emo-FilM](https://github.com/EllieMo/Emo-FilM) (commit 8a358f8, 2024-04-13, Apache-2.0) | `constants_emo_film.py`의 영화 길이, 항목 목록, CPM 범주, 제외 항목과 영화 | 직접 읽음 |
| nature.com, miplab.epfl.ch | 출판사 원문, 저자 PDF | **이 세션 네트워크에서 차단되어 접근 실패**. Table 1, Supplementary Table, Usage Notes는 미확인 |

---

## Gate 판정

| Gate | 판정 | 근거 요약 |
|---|---|---|
| **G1: 원본 자극 접근** | **공개 경로 기준: 요청 필요 (조건부로 공개 재구성 가능)**<br>**우리 환경 보유 여부: 미확인** | (1) OpenNeuro ds004892 v1.0.2와 ds004872 v1.0.3의 전체 파일 목록에 영상 파일이나 `stimuli/` 폴더가 없다(직접 확인). 저자 GitHub 코드에도 washout 영상(`washout_90.mp4`)만 있고 영화 파일은 없으며, 실험 스크립트 Readme는 "영화 위치 경로를 로컬에서 지정"하라고만 쓴다. (2) 원 출처는 **LIRIS-ACCEDE 데이터베이스(continuous 30편 컬렉션)** 의 Creative Commons 단편영화다. 논문은 "All selected films are free to share under Creative Commons licences"라고 쓰고, 동시에 "public domain"이라고도 써서 표현이 불일치한다. (3) 연구에 쓴 판본은 **앞뒤 크레딧을 잘라낸 편집본**이며 이 편집본 자체는 공개 저장소에 없다. 크레딧 절단 정보가 들어 있을 가능성이 있는 `code/FilmInfo.txt`, `code/BBL_experiment_Movies_without_credits_exp_files.xlsx`가 ds004892에 있으나 annex 파일이라 내용은 미확인. (4) 따라서 frame 단위 정렬이 필요한 모델 기반 연구는 LIRIS-ACCEDE 또는 각 영화 원 배포처에서 원본을 받아 절단 지점을 재현하거나, 저자에게 편집본을 요청해야 한다. 같은 연구실의 David et al. (2025)은 영화 frame을 입력으로 썼으므로 연구실은 편집본을 보유한 것으로 보인다(추정). (5) 일부 영화는 CC BY-NC 계열로 알려져 있어(예: Spaceman, CC BY-NC 3.0, LIRIS-ACCEDE credits 검색 결과 기준) 파생물(편집, 생성형 counterfactual) 제작과 재배포 조건을 영화별로 확인해야 한다. |
| **G2: fMRI 형식과 전처리 수준** | **사용 가능. BIDS raw + FSL FEAT 기반 volume 전처리본 제공. fMRIPrep, surface, parcellation 산출물은 없음** | BIDS 1.7.0, CC0. 3T Siemens TIM Trio, TR 1.3 s, 2.5 mm 등방성, MB3. 30명 × (영화 14 런 + rest 1 런) = 450 런 전부 raw와 전처리본 존재(v1.0.2 기준 직접 집계). 전처리본은 `space-orig_desc-prepro`, `space-subject_desc-ppres`, `space-MNI_desc-ppres` 세 종류이며 모두 6 mm FWHM smoothing, high-pass(sigma 50 s), WM/CSF/motion 회귀가 적용된 상태다. Fieldmap(magnitude/phasediff)은 raw에 있으나 전처리 서술에 distortion correction이 없다. MRIQC 0.16.1 보고서 포함. |
| **G3: 라벨 접근성과 평정 주체** | **접근 가능 (CC0, OpenNeuro ds004872). 주 라벨의 평정 주체는 fMRI 참가자가 아닌 별도 평정자 44명** | 50개 항목(최종) consensus 시계열 1 Hz × 14편, 평정자별 원자료(55개 항목 × 16편) 공개. 평정자는 1인칭 경험 문항("You felt ...")으로 **자신의 경험**을 평정했으므로 이는 "별도 평정자의 규범적(normative) 경험 평정"이다. fMRI 참가자 본인의 평정은 (a) 스캔 후 클립 단위 회고 평정(영화당 5개 항목, 영화 길이의 약 20%), (b) 영화별 몰입, 즐거움, 흥미 3문항, (c) 성격 및 정서 질문지뿐이다. |

---

## 1. Verified Dataset Specification

### 1.1 구성 개요

| 구분 | 내용 | 출처 |
|---|---|---|
| 공개 저장소 | fMRI 연구: OpenNeuro **ds004892** (현재 v1.0.2, [doi:10.18112/openneuro.ds004892.v1.0.2](https://doi.org/10.18112/openneuro.ds004892.v1.0.2)); 평정 연구: OpenNeuro **ds004872** (현재 v1.0.3, [doi:10.18112/openneuro.ds004872.v1.0.3](https://doi.org/10.18112/openneuro.ds004872.v1.0.3)) | 각 `dataset_description.json` 직접 확인 |
| 라이선스 | 두 데이터셋 모두 CC0. 코드는 Apache-2.0 | `dataset_description.json`, 코드 LICENSE |
| 버전 이력 | ds004892: 1.0.0 (2024-02-26 업로드), 1.0.1 (2025-02-20, QC 추가), **1.0.2 (2026-08-13, "uploaded some missing preprocessed data")**. ds004872: 1.0.0~1.0.3 (2024-02-26~2024-04-05, derivatives 소폭 수정) | 각 `CHANGES` 직접 확인 |
| 자금, 윤리 | SNSF Sinergia CRSII5_180319; Geneva Cantonal Commission 2018-02006 | `dataset_description.json`, 논문 Methods |

### 1.2 A. Acquisition & Structure (fMRI 연구, ds004892)

| 항목 | 값 | 출처 |
|---|---|---|
| 참가자 | 32명 모집, 2명 제외(스캐너 불내성 1, 치아 교정기 artefact 1) → **30명** (여 18), 18~35세(평균 25.83, SD 3.60), 오른손잡이, 영어 이해 수준 높음, 정상 색각. ID는 S01~S32 중 S12, S18 결번 | 논문 Methods; `participants.tsv` 30행 직접 집계 |
| 평정 연구와의 관계 | fMRI 참가자 중 평정 연구 참여자 없음("none of which partook in the annotation study") | 논문 Methods |
| 세션 | 1인당 4회(각 약 2시간), 세션당 영화 2~5편, 유사 무작위 순서. **S07과 S28은 ses-5가 있음** (S07은 ses-5에 영화 3편: BetweenViewings, Spaceman, ToClaireFromSonny) | 논문; 파일 목록 직접 집계 |
| 런 구조 | 영화 런마다 90 s washout(고정점, 무음) → 영화(오디오 포함, in-ear plug) → 90 s washout. 예: sub-S01 BigBuckBunny events는 rest onset 2.80 s / film onset 93.84 s, 길이 490.0 s / rest 584.89 s | 논문; `*_task-scan_acq-*_events.tsv` 직접 확인 |
| Rest | 첫 세션 10분 eyes-open rest 1회(460 volumes) | 논문 |
| 런 수 | 30명 × 14편 + rest 30 = 450 BOLD 런(raw, 전처리본 모두 450) | 파일 목록 직접 집계 |
| 반복 제시 | 각 영화는 참가자당 **1회만** 제시(반복 없음). 단, 스캔 후 사후 평정 과제에서 영화 일부 클립(평균 7 s)을 다시 봄 | 논문 |
| 스캐너 | 3T Siemens Magnetom TIM Trio, 32채널 헤드코일, Geneva BBL | 논문; bold sidecar |
| BOLD | CMRR MB-EPI, **TR 1.3 s**, TE 30 ms, flip 64°, MB 3, 54 slices, FoV 210 mm, **2.5 mm 등방성**, PE AP(`j-`), echo spacing 0.57 ms, total readout 0.0473 s, slice timing은 sidecar에 있음 | 논문; `sub-S01_ses-1_task-BigBuckBunny_bold.json` 직접 확인 |
| T1w | MPRAGE 1 mm 등방성, TR 1.9 s, pydeface로 defacing | 논문 |
| Fieldmap | 세션마다 magnitude1/2, phasediff 존재 | 파일 목록 |
| 전처리 (제공본) | FSL FEAT 6.00: MCFLIRT, BET, FLIRT 정합, **6 mm FWHM smoothing**, grand-mean scaling, high-pass(sigma 50 s); FAST로 WM/CSF 평균 시계열과 motion 6개 회귀. 공간: `space-orig`(native), `space-subject`(각자 rest 런 volume에 정합해 세션 간 정렬), `space-MNI` | 논문; derivatives sidecar JSON 직접 확인 |
| 없는 것 | fMRIPrep 산출물, FreeSurfer, surface(GIFTI/CIFTI), parcellated time series, 생리 잡음 회귀가 반영된 BOLD 전처리본(논문에는 HBI, RV 계산이 서술되나 해당 회귀자 파일은 확인되지 않음), slice timing correction과 fieldmap 기반 distortion correction 적용 서술 | 파일 목록 전수 확인, 논문 서술 |
| QC | MRIQC 0.16.1 (group, 개별 HTML). 평균 FD 0.16 mm (0.09~0.55), 영화 런 FD가 rest보다 유의하게 큼. 품질로 제외한 참가자 없음. EFC 높은 런: S29 전체, S20 The Secret Number; S16 T1 일부 voxel; S21 rest outlier | 논문 Technical Validation; `derivatives/mriqc` |
| 자극 onset 검증 | Schaefer 100 parcellation의 시각 영역 parcel 평균 BOLD로 onset/offset 시각 검증(5 s 지연 가정) | `derivatives/onset_validation/README.txt` |

### 1.3 생리 신호

| 항목 | 값 | 출처 |
|---|---|---|
| 장비 | BIOPAC MP150, AcqKnowledge 4.4 | 논문 |
| 채널 | 심장: PPG(TSD200-MRI + PPG100C); 호흡: 흉부 pneumatic belt(TSD221-MRI + RSP100C); 피부전도: EDA(EDA100C-MRI) | 논문; `*_physio.json` Columns |
| 샘플링 | **1000 Hz**, 전 스캔 구간 기록, phys2bids로 BIDS 변환, 런 앞뒤 9 s 여유 포함 | 논문; `*_physio.json`(`SamplingFrequency: 1000.0`, `StartTime: 9.003`). StartTime의 부호가 BIDS 관례(음수)와 다르므로 정렬 시 확인 필요 |
| 파일 | raw `*_physio.tsv.gz` 450개(런마다 1개); derivatives에 peakdet 처리 심장, 호흡 객체(`desc-cardiac_physio.phys`, `desc-resp_physio.phys`)와 `derivatives/physioqc`(EDA, PPG, Ventilation QC CSV) | 파일 목록 직접 확인 |
| 처리 서술 | 심장, 호흡을 40 Hz로 다운샘플, 저역 통과(8 Hz, 2 Hz), peak 검출(수동 감독), phys2denoise로 HBI(6 s 창), RV(8 s 창) 산출. **EDA의 전처리 서술은 없음** | 논문 Methods |

### 1.4 평정 연구 (ds004872)

| 항목 | 값 | 출처 |
|---|---|---|
| 평정자 | **44명** (여 23), 20~39세(평균 25.31), Geneva 지역 모집, 원격 온라인 평정(자기 컴퓨터), 2020-11~2021-02 (보충 2명은 2022-01, 2022-10) | 논문 Methods; 폴더 44개 직접 확인 |
| 영화 | 평정 단계 16편 → reliability 기준으로 2편(DamagedKungFu, RidingTheRails) 제외 → fMRI는 14편 | 논문; `constants_emo_film.py`의 `BAD_MOVIES` |
| 항목 | 평정 단계 55개(이산 정서 13 + CoreGRID 기반 42) → agreement가 낮은 5개(Jaw, EyesOpen, Breathing, Movement, Consequences) 제외 → **최종 50개** | 논문; `BAD_ITEMS` |
| 도구, 해상도 | CARMA 개조판, 마우스로 단위 없는 막대를 연속 조작, **1 Hz**, 0~100 저장 | 논문; JSON `SamplingFrequency: 1.0` |
| 배정 설계 | 평정자 1명이 항목 6개 × 16편(=96 과제)을 항목 블록 단위로 평정(한 항목을 16편 전부 무작위 순서로 본 뒤 다음 항목). 즉 **평정자는 같은 영화를 최대 6번 시청**. 항목×영화 조합마다 4명 배정 | 논문 Procedure |
| 실제 완료량 | 평정자별 파일 수가 10~204개로 크게 다름(204개 20명, 202개 5명, 194개 3명, 192개 4명, 그 외 12명은 10~188개). 중도 미완료자 보충으로 44명이 됨 | 파일 목록 직접 집계 |
| Consensus 계산 | 평정자 내 영화 전체에 걸쳐 z-score → 결측 보간 → 상수 시계열, \|z\|>15 시계열 제거 → 포함 시 평균 r을 0.20 넘게 낮추는 시계열 제거 → 5개일 때 최저 1개 제거 → 평균. 각 consensus는 **3~4명 평균** (700개 영화×항목 중 154개는 3명) | 논문; 코드 `MakeMasterfile.py` |
| 파일 | `derivatives/Annot_<Film>_stim.tsv.gz`(14편, 50열) + `C_Annot_FILMS_stim.tsv.gz`(연결본); 평정자별 `sub-<id>/beh/*_recording-<Item>_stim.tsv.gz` | 파일 목록 직접 확인 |

### 1.5 영화 목록과 길이

길이는 저자 코드 `constants_emo_film.py`의 `ALL_MOVIES` 값(초)이며, BigBuckBunny 490 s가 events의 film duration 490.0 s와 일치함을 확인했다. 장르, 감독, 영화별 라이선스, 런별 volume 수는 논문 Table 1에 있으나 **미열람(미확인)**.

| 영화 (BIDS task 이름) | 길이 (s) | 길이 (분:초) | fMRI 사용 |
|---|---|---|---|
| AfterTheRain | 496 | 8:16 | O |
| BetweenViewings | 808 | 13:28 | O |
| BigBuckBunny | 490 | 8:10 | O |
| Chatter | 405 | 6:45 | O |
| FirstBite | 599 | 9:59 | O |
| LessonLearned | 667 | 11:07 | O |
| Payload | 1008 | 16:48 | O |
| Sintel | 722 | 12:02 | O |
| Spaceman | 805 | 13:25 | O |
| Superhero | 1028 | 17:08 | O |
| TearsOfSteel | 588 | 9:48 | O |
| TheSecretNumber | 784 | 13:04 | O |
| ToClaireFromSonny | 402 | 6:42 | O |
| YouAgain | 798 | 13:18 | O |
| DamagedKungFu | 922 | 15:22 | X (평정 단계에서 제외) |
| RidingTheRails | 794 | 13:14 | X (평정 단계에서 제외) |

14편 합계 9,600 s(2시간 40분), 평균 685.7 s(11분 26 s)로 논문 서술("over 2½ hours", 평균 11분 26초)과 일치.

---

## 2. Complete Metadata & Annotation Inventory

### 2.1 B. Stimulus Metadata

| 항목 | 상태 | 근거 |
|---|---|---|
| 시각 내용 | 실사, 애니메이션 단편 혼합. BigBuckBunny, Sintel, TearsOfSteel은 Blender Foundation 공개 영화로 알려져 있음(일반 지식, 이번에 URL 확인 안 함). 영화별 장르, 내용 요약은 Table 1에 있으나 미열람 | 논문 Table 1 언급 |
| 오디오, 음악, 대사 | **포함**. 영화는 오디오와 함께 in-ear plug로 제시. 참가자 선발 조건에 "high level of English language comprehension" → 대사 언어는 영어로 보임. Leipold et al. (2026)은 자극을 "complete narratives and spoken language"로 기술 | 논문 Procedure; [doi:10.1162/IMAG.a.1400](https://doi.org/10.1162/IMAG.a.1400) |
| 자막, transcript | **제공 안 됨** (저장소에 없음) | 파일 목록 전수 확인 |
| 객체, 장면, 의미 feature | **제공 안 됨** | 파일 목록 전수 확인 |
| 저수준 feature (밝기, 음량 등) | **제공 안 됨** | 파일 목록 전수 확인 |
| 시간 정렬 | events TSV에 런 기준 film onset과 길이(ms 단위 정밀도) 존재. 평정 시계열은 film onset을 0으로 하는 1 Hz(`StartTime: 0`). 사후 평정 클립 onset은 "Onset of clip relative to full film file"(초) | events/JSON 직접 확인 |
| 원본 자극 접근 (G1) | 위 Gate 표 참조. 공개 저장소에 영상 없음 | 파일 목록 전수 확인 |
| 저작권 | 논문: 모두 CC 라이선스(동시에 "public domain"이라는 부정확한 표현 병존). 영화별 라이선스 종류(BY, BY-NC, BY-NC-SA, BY-ND 등)는 미확인. Spaceman은 CC BY-NC 3.0 Unported로 LIRIS-ACCEDE credits에 표기(검색 결과 기준) | 논문; 웹 검색 |
| 같은 영화의 외부 주석 | 논문에 따르면 16편은 이전에 valence, arousal(LIRIS-ACCEDE continuous; Baveye et al., ACII 2015, HAL hal-01193144)과 aesthetic highlight(Muszynski et al., 2018, ACM TOMM, doi:10.1145/3175497)로 주석된 영화임. 이 두 DOI와 서지는 검색 결과 기준이며 doi.org 직접 확인은 하지 않음 | 논문 Background; 웹 검색 |

### 2.2 C. Labels & Annotations: 55개 항목 전체 표

* CPM 범주는 저자 코드 `ITEM_CATS`(최종 50개 기준)에서 확인했다. 제외된 5개 항목의 범주는 코드의 `ALL_ITEMS` 순서상 위치로 추정했다.
* high / low 표지는 ds004872 평정자 sidecar JSON의 `Levels` 값을 그대로 옮겼다(오탈자 포함).
* 범주별 최종 개수: Appraisal 10, Expression 5, Motivation 10, Feeling 7, Physiology 5, Discrete emotion 13 (= 50).

| # | 항목 (BIDS 이름) | CPM 범주 | 척도 high / low 표지 | 최종 50개 포함 | fMRI 참가자 사후 검증 포함 |
|---|---|---|---|---|---|
| 1 | Standards | Appraisal | MyStandards / NotMyStandards | 포함 | 포함 |
| 2 | PleasantSelf | Appraisal | Pleasant For Me / Unpleasant Me | 포함 | 포함 |
| 3 | SocialNorms | Appraisal | SocialNorms / NotSocialNorms | 포함 | 포함 |
| 4 | PleasantOther | Appraisal | PleasantOthers / UnpleasantOthers | 포함 | 포함 |
| 5 | GoalsOther | Appraisal | MeetOthersGoals / NotOthersGoals | 포함 | 포함 |
| 6 | Controlled | Appraisal | EventControlled / Uncontrolled | 포함 | 포함 |
| 7 | Predictable | Appraisal | EventPredictable / Unpredictable | 포함 | 포함 |
| 8 | Suddenly | Appraisal | EventSuddenly / Not Suddenly | 포함 | 포함 |
| 9 | Agent | Appraisal | HumanCaused / ChanceCaused | 포함 | 포함 |
| 10 | Urgency | Appraisal | Situation Urgent / Not Urgent | 포함 | 포함 |
| 11 | Consequences | Appraisal (추정) | ResultPredictable / Unpredictable | 제외 (agreement 낮음) | 해당 없음 |
| 12 | Lips | Expression | Press Lips / Relax Lips | 포함 | 포함 |
| 13 | Tears | Expression | Tears In My Eyes / Dry Eyes | 포함 | 포함 |
| 14 | Jaw | Expression (추정) | Feel Jaw Drop / Jaw Closed | 제외 (agreement 낮음) | 해당 없음 |
| 15 | Eyebrows | Expression | BrowsRaised / BrowsRelaxed | 포함 | 포함 |
| 16 | Smile | Expression | Smiled / Did Not Smile | 포함 | 포함 |
| 17 | Frown | Expression | Frowned / Did Not Frown | 포함 | 포함 |
| 18 | EyesOpen | Expression (추정) | OpenEyesWide / Close Eyes | 제외 (agreement 낮음) | 해당 없음 |
| 19 | Movement | Expression (추정) | Move Abpruptly / Sat Very Still | 제외 (agreement 낮음) | 해당 없음 |
| 20 | Stop | Motivation | Want Stop Event / Don't Want Stop | 포함 | 포함 |
| 21 | Undo | Motivation | Want Undo Event / Don't Want Undo | 포함 | 포함 |
| 22 | Repeat | Motivation | WantLastRepeat / NotWantRepeat | 포함 | 포함 |
| 23 | Oppose | Motivation | Want To Oppose / NotWantOppose | 포함 | 포함 |
| 24 | Attention | Motivation | Captured / Disinterested | 포함 | 포함 |
| 25 | Tackle | Motivation | WantDoSth / NotDoSomething | 포함 | 포함 |
| 26 | Command | Motivation | WantCommand / Don'tWant | 포함 | 포함 |
| 27 | Support | Motivation | WantHelp / Don'tWantHelp | 포함 | 포함 |
| 28 | Move | Motivation | Want To Move / Don't Want Move | 포함 | 포함 |
| 29 | Care | Motivation | WantToCareFor / NotCareFor | 포함 | 포함 |
| 30 | Bad | Feeling | Feel Bad / Feel Bad (sidecar 오기) | 포함 | 포함 |
| 31 | Good | Feeling | Feel Good / Not Feel Good | 포함 | 포함 |
| 32 | Calm | Feeling | Feel Calm / Feel Restless | 포함 | 포함 |
| 33 | Strong | Feeling | Feel Strong / Feel Weak | 포함 | 포함 |
| 34 | IntenseEmotion | Feeling | Intense Emotion / No Intense Emoti (sidecar에서 잘림) | 포함 | 포함 |
| 35 | Alert | Feeling | Feel Alert / Feel Tired | 포함 | 포함 |
| 36 | AtEase | Feeling | Feel At Ease / Feel Nervous | 포함 | 포함 |
| 37 | Muscle | Physiology | Muscles Tense / Muscles Relax | 포함 | 포함 |
| 38 | Heartrate | Physiology | Heartbeat Faster / Heartbeat Slower | 포함 | **미포함** |
| 39 | Breathing | Physiology (추정) | Breathing Faster / Breathing Slower | 제외 (agreement 낮음) | 해당 없음 |
| 40 | Throat | Physiology | Lump In Throat / Throat Clear | 포함 | 포함 |
| 41 | Stomach | Physiology | Stomach Unwell / Stomach Normal | 포함 | 포함 |
| 42 | Warm | Physiology | Felt Warm / Felt Cold | 포함 | **미포함** |
| 43 | Anger | Discrete emotion | Angry / Not Angry | 포함 | 포함 |
| 44 | Guilt | Discrete emotion | Guilty / Not Guilty | 포함 | 포함 |
| 45 | WarmHeartedness | Discrete emotion | WarmHearted / NotWarmHeart | 포함 | 포함 |
| 46 | Disgust | Discrete emotion | Disgusted / Not Disgusted | 포함 | 포함 |
| 47 | Happiness | Discrete emotion | Happy / Not Happy | 포함 | 포함 |
| 48 | Fear | Discrete emotion | Fearful / Not Fearful | 포함 | 포함 |
| 49 | Regard | Discrete emotion | Regard / Contempt | 포함 | 포함 |
| 50 | Anxiety | Discrete emotion | Anxious / Not Anxious | 포함 | 포함 |
| 51 | Satisfaction | Discrete emotion | Satisfied / Dissatisfied | 포함 | 포함 |
| 52 | Pride | Discrete emotion | Proud / Ashamed | 포함 | 포함 |
| 53 | Surprise | Discrete emotion | Surprised / Not Surprised | 포함 | 포함 |
| 54 | Love | Discrete emotion | Love / No Love | 포함 | 포함 |
| 55 | Sad | Discrete emotion | Sad / Not Sad | 포함 | 포함 |

항목 정의에서 주의할 점(직접 확인):
* **문항 관점:** 거의 모든 문항이 1인칭 경험형이다("You felt ...", "You smiled", "You had tears in your eyes"). Appraisal 문항도 평정자 자신의 관점에서 사건을 평가하게 한다("It was unpleasant for you", "It was incongruent with your standards"). 따라서 consensus는 **자극에 표현된(portrayed) 정서가 아니라 별도 평정자가 보고한 경험 정서**다. 단, PleasantOther, GoalsOther는 타인에 대한 평가다.
* **양극 척도:** Regard(Regard~Contempt), Pride(Proud~Ashamed), Calm(Calm~Restless), AtEase(At ease~Nervous), Strong(Strong~Weak), Alert(Alert~Tired), PleasantSelf, PleasantOther 등은 양극이고, Anger, Fear 등은 단극이다. "Pride" 열은 Pride-Shame 축이다.
* **Description 필드의 반대 극 표기:** 일부 sidecar의 `Description`이 낮은 극을 적고 있다(예: Predictable: "The event was unpredictable", Urgency: "There was no urgency", Alert: "You felt tired"). 방향은 `Levels`와 `Instructions`로 판단해야 한다.
* **Valence, arousal 항목은 직접 없음.** Ma & Kragel (2026)은 Good, Bad를 valence, Calm, AtEase를 arousal 대리 지표로 사용했다.

### 2.3 Inter-rater agreement (원문 재확인)

| 지표 | 값 | 출처와 비고 |
|---|---|---|
| 초록의 평균 agreement | **0.38** | 논문 Abstract |
| Technical Validation의 최종 평균 | **r = 0.39** (14편, 50개 항목) | 논문 Technical Validation. 초록 0.38과 **0.01 불일치** (계산 시점 차이로 추정, 원인 미확인) |
| 지표 정의 | 영화×항목마다 평정자 쌍별 Pearson r(4명이면 6쌍)의 평균 | 논문 |
| 제외 전 항목 범위 | 최고 r = 0.58, 최저 r = −0.01; 영화 평균 0.21~0.49 | 논문. 해당 항목명은 PMC 추출본에서 빠져 **미확인** |
| 제외 기준 | 영화 전체 평균 r < 0.15 항목 5개 제거(r = 0.14, 0.11, 0.07, 0.06, −0.01); 항목 전체 평균 r < 0.25 영화 2편 제거(r = 0.21, 0.24). 저자는 평균 r < 0.20 항목은 신뢰할 수 없다고 권고 | 논문. 제외 항목과 영화의 이름은 코드로 확인했으나 **각 r 값과 이름의 대응은 미확인** |
| 최종 범위 | 영화별(항목 평균) r = 0.29~0.54, 항목별(영화 평균) r = 0.21~0.60 | 논문 |
| 시계열 제거 | 2,840개 중 상수 구간 2, \|z\|>15 outlier 48, deviant 126, 5개 중 최저 18 제거 | 논문 |
| 항목별 분포 | Supplementary Table에 있음. **미열람(미확인)**. ds004872 원자료와 `MakeMasterfile.py`로 재계산 가능 | |
| fMRI 표본의 검증 일치도 | fMRI 참가자 사후 평정(보간, z-score, 평균)과 consensus의 상관 평균 **0.41**, 항목 평균 범위 0.08~0.70(해당 항목명 미확인), 항목별 IRA와 검증 일치도의 상관 r = .63 | 논문 Technical Validation |

### 2.4 fMRI 참가자 본인 자료 (ds004892)

| 자료 | 내용 | 확인 |
|---|---|---|
| 사후 클립 평정 (`beh/*_events.tsv`) | 스캔 후 같은 영화의 클립(평균 7 s, 영화당 약 21개, 전체의 20.52%)을 다시 보고 **영화당 5개 항목**을 0~100으로 평정. 항목별로 영화마다 3~4명만 평정. 사용 항목은 48개(50개 중 Heartrate, Warm 제외). 논문의 "34 CPM + 13 discrete = 48"은 산술이 맞지 않으며 실제 데이터는 CPM 35 + 이산 13 = 48 | 직접 집계: 파일 414개(30×14=420 중 S02, S03, S05(2), S07, S08, S10, S13 결측, S14, S17은 15개), 클립 행 8,626개 |
| 영화별 3문항 | 런 종료 직후 몰입(Absorbed), 즐거움(Enjoyed), 흥미(Interested) 0~100 | `participants.tsv` 열 42개 확인 |
| 질문지 | DASS(우울, 불안, 스트레스), BIS/BAS, ERQ, BFI, 자체 COVID 스트레스 척도(미타당화), 키, 몸무게 | `participants.json` |

### 2.5 정서 출처 구분 (Safeguard)

| 구분 | Emo-FilM에서의 해당 자료 | 비고 |
|---|---|---|
| 실제 관찰된 정서(행동, 생리 측정) | fMRI 참가자의 PPG, 호흡, EDA (1000 Hz) | 정서 자체가 아니라 자율신경 지표. 표정, 시선 기록은 없음 |
| fMRI 참가자가 보고한 정서 | 사후 회고 클립 평정(5항목/영화, 약 20% 구간), 영화별 몰입, 즐거움, 흥미 | 스캔 중 연속 자기보고는 **없음** |
| 별도 평정자의 규범적 평정 | 44명의 1 Hz 연속 평정과 3~4명 consensus (50항목) | 주 라벨. 1인칭 경험형 문항이지만 fMRI 참가자의 경험은 아님 |
| 자극에 표현된(portrayed) 정서 | **직접 라벨 없음** | 등장인물 정서 주석이 필요하면 새로 만들어야 함 |
| AI가 추정한 정서 | **없음** | 원 논문은 "현재 AI로 시청각 내용에서 경험 정서를 신뢰성 있게 자동 추출할 수 없다"고 서술(Background & Summary 1단락) |

---

## 3. Available vs Missing Information

| 정보 | 상태 |
|---|---|
| raw BOLD, T1w, fieldmap, events | 있음 |
| Volume 전처리본(native, subject, MNI) | 있음 (6 mm smoothing, nuisance 회귀 적용 상태) |
| fMRIPrep, surface, parcellation, denoised(생리 회귀) BOLD | 없음 |
| 생리 raw(PPG, RESP, EDA 1000 Hz), peakdet 객체, QC 지표 | 있음 |
| HBI, RV 회귀자 파일 | 확인 못 함(논문 서술만 있음) |
| 평정자별 원 평정(55항목×16편), consensus(50항목×14편) | 있음 (수치 본체는 annex, 이 세션에서 미열람) |
| 항목별 inter-rater agreement 표 | 논문 Supplementary에 있음, **미열람** |
| fMRI 참가자 연속 자기보고 | 없음 |
| fMRI 참가자 사후 클립 평정 | 있음(부분적) |
| 원본 영상, 편집 절단 정보 | 공개 저장소에 영상 없음. 절단 정보 파일 후보(`code/FilmInfo.txt`, xlsx)는 있으나 미열람 |
| 대사 transcript, 자막, 시각, 의미 feature, 저수준 feature | 없음 |
| 등장인물(portrayed) 정서 주석 | 없음 |
| 같은 영화의 외부 V/A, aesthetic highlight 주석 | LIRIS-ACCEDE, Muszynski et al. 쪽에 있음(Emo-FilM 저장소 밖, 접근 조건 미확인) |
| 논문 Table 1(장르, 볼륨 수), Usage Notes, Code availability | 출판사 페이지 차단으로 **미확인**. 단 Code availability가 `github.com/EllieMo/Emo-FilM`을 가리킨다는 검색 결과 있음 |

데이터 이상치(직접 확인):
* ds004872에 오탈자 영화명 `LeassonLearned` 파일 342개(35명)가 `LessonLearned`와 별도로 존재. 평정자당 파일 204개(=6항목×17)가 나오는 원인으로 보이며, 중복인지 다른 판본인지 **확인 필요**.
* ds004892 derivatives의 S07 ses-5 파일명이 `sub-S07-ses-5_task-BetweenViewing_...`로 BIDS 규칙(밑줄, 복수형 s)과 다름. raw는 `BetweenViewings`.
* S07의 영화 3편 전처리본은 v1.0.2(2026-08-13)에서 추가됨. **Ma & Kragel (2026)은 "OpenNeuro에서 3편 결측"을 이유로 S07을 제외(29명)**, Leipold et al. (2026)도 결측으로 2명 제외(28명). 현재 버전으로는 30명 전원 사용이 가능할 수 있음(데이터 본체 미검증).
* `participants.tsv`의 일부 몰입, 즐거움, 흥미 값이 n/a.

---

## 4. Potential Modeling Tasks (D. Modeling Opportunities)

G1이 "요청 필요"이므로 자극 feature가 필요한 과제와 필요 없는 과제를 나눈다.

| 과제 | 자극 영상 필요 | 가능성과 조건 | 근거 |
|---|---|---|---|
| Emotion decoding (consensus 50항목, 1 Hz → TR 1.3 s) | 아니오 | 바로 가능. Ma & Kragel (2026)이 13개 이산 정서 + 4개 Feeling 항목으로 hippocampus, vmPFC, entorhinal, amygdala ROI decoding을 이미 수행(r ≈ 0.04~0.10) | [doi:10.1038/s41467-025-68240-z](https://doi.org/10.1038/s41467-025-68240-z) |
| Appraisal, motivation, expression, physiology 성분 decoding/encoding | 아니오 | 37개 비이산 항목은 fMRI 분석에서 덜 쓰임. 평정만으로 이산 정서를 성분으로 예측한 연구는 있음(Morgenroth et al., 2026, Emotion) | [doi:10.1037/emo0001619](https://doi.org/10.1037/emo0001619) |
| Vision decoding, 영상 재구성 | 예 | 같은 연구실이 CNN encoder-decoder로 시각 피질 voxel 예측과 frame 재구성 수행(David et al., 2025) | [doi:10.1109/EMBC58623.2025.11254034](https://doi.org/10.1109/EMBC58623.2025.11254034), arXiv:2507.12009 |
| Semantic decoding, 언어 모델 기반 encoding | 예 (transcript 필요) | transcript 없음. 영상 확보 후 ASR로 생성해야 함 | 파일 목록 |
| 다중 feature encoding과 variance partitioning (시각, 청각, 언어, 정서) | 예 | 정서와 시각-의미 내용의 공선성을 분리하는 핵심 과제. 현재 Emo-FilM 사용 연구 중 이를 체계적으로 한 것은 확인 못 함(미확인) | 3절 |
| Multimodal alignment (video-audio-text foundation model ↔ 뇌 ↔ 평정) | 예 | 영상 확보가 전제 | |
| Brain Foundation Model 적응 | 아니오 (BOLD만) | volume, TR 1.3 s, 30명 × 약 2.7시간 영화 + 10분 rest. Surface 기반 모델이면 재전처리 필요 | 1.2절 |
| 시간 동역학, 상태 공간, 전이 구조 | 아니오 | 1 Hz 연속 평정이 장점. Ma & Kragel은 TEM 기반 무작위 보행으로 전이를 모델링. 고차 위상(topology) 접근 preprint 존재(미검증) | 8절 |
| Brain-body coupling (PPG, RESP, EDA ↔ BOLD ↔ 평정) | 아니오 | 1000 Hz 생리 + 평정자의 Heartrate, Muscle, Throat, Stomach, Warm 문항 존재. 다만 생리는 fMRI 참가자, 평정은 별도 평정자라는 주체 불일치 | 1.3, 2.2절 |
| 개인차 (성격, 정서 질문지 ↔ 뇌) | 아니오 | 30명이라 검정력 제한. 저자도 개인차가 아닌 보편 과정용으로 설계했다고 명시. emotion-informed gradient로 불안, 개방성 예측 연구 있음(Chan et al., 2026) | 논문 Background; [doi:10.1002/hbm.70617](https://doi.org/10.1002/hbm.70617) |
| Cross-subject 정렬 (hyperalignment, SRM) | 아니오 | 영화당 1회 제시라 within-subject 반복 없음. Leipold et al.이 향후 과제로 제시 | [doi:10.1162/IMAG.a.1400](https://doi.org/10.1162/IMAG.a.1400) |
| Generative / counterfactual 자극 조작 | 예 | 영화별 CC 라이선스(ND, NC 조항)로 파생물 제작 허용 여부 확인 필요 | 2.1절 |
| AI-generated annotation 추가 | 예 | 평정자별 원자료가 있으므로 human-human 천장(3~4명) 대비 MLLM 평정의 일치도를 같은 지표로 비교 가능. 타당성 근거: 원 논문은 AI 추출의 신뢰성을 부정적으로 서술했고, Du et al. (2025, arXiv:2509.24298)은 다른 자극(2,180개 영상)에서 MLLM 표상이 인간 평정보다 뇌 활동을 더 잘 예측한다고 보고(본문 미열람). 사전학습 데이터 오염 위험: LIRIS-ACCEDE, Blender 영화는 인터넷에 널리 공개 | 논문 Background; arXiv:2509.24298 |

---

## 5. Unique Advantages

1. **CPM 성분 50개 항목의 1 Hz 연속 평정.** 이산 정서 13개에 더해 appraisal 10, motivation 10, expression 5, physiology 5, feeling 7개가 같은 시간축에 있다. Valence-arousal 중심 데이터셋에는 없는 구조다(논문; 코드 `ITEM_CATS`).
2. **평정자별 원자료 공개.** consensus뿐 아니라 44명의 개별 시계열이 있어 label noise, 항목별 reliability, leave-one-rater-out 천장을 직접 계산할 수 있다.
3. **오디오 포함 자연 시청 + 서사 구조.** 14편 각 6.7~17.1분의 완결된 단편이라 장시간 맥락, 서사 의존 정서를 다룰 수 있다.
4. **1000 Hz 생리 신호(PPG, 호흡, EDA)가 모든 런에 있음.**
5. **참가자당 약 2.7시간 영화 fMRI, TR 1.3 s.** 개인 내 모델 학습 데이터가 비교적 많다.
6. **fMRI 참가자의 부분적 자기보고**로 consensus의 타당성을 점검한 설계(검증 일치도 평균 0.41).
7. **CC0 공개, 저자 코드(Apache-2.0) 공개, 영화는 CC 라이선스**라 다른 독점 영화 데이터셋보다 자극 재구성 경로가 열려 있다.

---

## 6. Methodological Limitations

1. **평정 주체 불일치.** 주 라벨은 다른 사람(3~4명)의 경험 평정 평균이다. fMRI 참가자의 순간 정서를 직접 반영하지 않는다. Ma & Kragel도 Discussion에서 decoding 대상이 "independent observers"의 평정이라고 명시했다. 뇌 decoding 성능을 참가자의 주관 경험을 읽은 것으로 해석하면 안 된다(CLAUDE.md 6절).
2. **낮고 불균일한 label reliability.** 평균 r ≈ 0.38~0.39, 항목별 0.21~0.60. 평정자 수가 항목×영화당 3~4명뿐이라 consensus 자체의 잡음이 크다. 저자 권고: 평균 r < 0.20 항목은 신뢰 불가.
3. **상대 척도.** 평정을 평정자 내 영화 전체로 z-score했으므로 consensus는 절대 강도가 아니라 상대 변화량이다. 영화 간 절대 수준 비교에 주의.
4. **반복 시청 효과.** 평정자는 같은 영화를 최대 6번 보았다(항목마다 1회). 저자는 영향이 미미하다고 주장하나 서사 예측 가능성(Predictable, Suddenly, Surprise)에는 영향이 있을 수 있다(추론, 미검증).
5. **통제되지 않은 온라인 평정 환경.** 각자 컴퓨터, 오디오 장치, 2020~2021 COVID 시기.
6. **영화 수 14편.** leave-one-film-out fold가 14개뿐이고, 영화 수준 confound(장르, 밝기, 음량, 애니메이션 여부)와 정서가 공선적일 수 있다. Leipold et al. (2026)은 Emo-FilM에서도 ISC가 영화마다 유의하게 다르다(F(13,169) = 2.59, p = .003)고 보고했다.
7. **반복 제시 없음.** 영화를 한 번만 보여 within-subject noise ceiling을 반복으로 추정할 수 없다. 사후 클립 재시청은 별도 과제다.
8. **제공 전처리본의 제약.** 6 mm smoothing과 WM/CSF 회귀가 이미 적용되어 미세 패턴 분석, 피질하 구조 분석에 불리하다. 생리 잡음 회귀, slice timing 보정, distortion correction 적용 여부가 서술되지 않았다. 정밀 분석은 raw에서 재전처리를 권장한다.
9. **표본.** 30명, 18~35세, Geneva 지역, 영어 이해 수준 높은 참가자(모국어 미확인). 저자 스스로 "개인차가 아닌 보편 과정 연구에 맞춘" 설계라고 밝혔다.
10. **시간 해상도.** fMRI 한계와 함께, 평정 1 Hz는 빠른 성분(Suddenly, Surprise)과 느린 정서(Love)의 시간 척도 차이를 담기 어렵다(Morgenroth et al., 2023, SCAN, "A space odyssey: temporality" 절).
11. **문서 불일치와 파일 이상치.** 초록 0.38 vs 본문 0.39, 검증 항목 산술(34+13≠48), "public domain"과 "Creative Commons" 혼용, `LeassonLearned` 중복 의심, S07 파일명 비규칙, 사후 평정 파일 414/420.
12. **원 논문 Usage Notes:** PMC 전문에 Usage Notes 절이 보이지 않고 출판사 페이지에 접근하지 못해 **미확인**. 본문 안에서 확인한 사용 권고는 (a) 평균 agreement r < 0.20 항목 비신뢰, (b) 개인차보다 보편 과정 연구용 설계, (c) 영화는 CC로 공개되어 연구자가 정보를 추출하거나 확장 수집에 쓸 수 있음, 세 가지다.

---

## 7. Cross-dataset Compatibility Notes

| 대상 | 결합 가능성 | 근거와 주의 |
|---|---|---|
| Horikawa et al. (2020) | **직접 결합 불가, 정렬 필요** | Horikawa 쪽은 Cowen & Keltner 평정자의 무음 짧은 영상 단위 평정(범주, 차원), Emo-FilM은 오디오 포함 장편 단편의 1 Hz 연속 평정. 이름이 같은 이산 정서(예: Anger, Anxiety, Fear, Disgust, Surprise, Sadness, Satisfaction)도 정의, 척도(단극/양극), 평정 지시(경험)와 시간 단위가 다르다. Horikawa 쪽 정의는 해당 감사 보고서와 대조할 것 |
| Spacetop (Jung et al., 2025) | 부분 결합 가능 | 둘 다 영화 시청 fMRI + 생리. 영화가 달라 자극 수준 결합은 불가. 생리 신호는 리샘플링 후 비교 가능. Spacetop 평정 종류는 해당 감사 보고서 참조 |
| NSD (Allen et al., 2022) | 라벨 결합 불가 | 정지 이미지, 정서 라벨 없음. Representation alignment 경로만 가능 |
| LIRIS-ACCEDE continuous V/A, Muszynski aesthetic highlight | **같은 영화에 대한 외부 주석** | 다른 평정자 집단(LIRIS: 프랑스 참가자 16명이라는 검색 결과, 미검증)의 valence, arousal. Emo-FilM 항목과 교차 타당화 가능. 접근 조건 미확인 |
| 공간, 시간 형식 | | Emo-FilM은 MNI volume 2.5 mm, TR 1.3 s. surface 기반 데이터셋과 결합하려면 재전처리 필요 |

---

## 8. Research Opportunities

### 8.1 "이미 수행됨" 기준점: Kragel 연구실 2026 연구 (확정)

* **서지:** Ma Y, Kragel PA. (2026) Map-like representations of emotion knowledge in hippocampal-prefrontal systems. *Nature Communications* 17(1):1518. [doi:10.1038/s41467-025-68240-z](https://doi.org/10.1038/s41467-025-68240-z), PMID 41588009, PMC12891686. 출판일 2026-01-26. PubMed와 PMC 전문으로 확인.
* **이전 판:** bioRxiv preprint "The representation of emotion knowledge in hippocampal-prefrontal systems" ([doi:10.1101/2025.06.03.657722](https://doi.org/10.1101/2025.06.03.657722), 검색 결과로만 확인), CCN 2025 초록 "Structural abstraction of emotion knowledge in hippocampal-prefrontal systems"(2025.ccneuro.org, 검색 결과로만 확인). Emory 보도 "How the brain charts emotion in a map-like way"(news.emory.edu, 2026년 3월).
* **데이터:** Emo-FilM fMRI 29명(S07 제외), FSL 전처리, consensus 평정 중 이산 정서 13개 + Feeling 4개(Good, Bad = valence; Calm, AtEase = arousal). 나머지 33개 성분 항목은 쓰지 않음.
* **방법:** 이산 정서 평정 시계열의 상관(1−r)에 MDS를 적용해 2차원 affective space를 만들고 시계열을 투영. ROI(hippocampus와 entorhinal: Julich-Brain; 전후 hippocampus: MNI y = −21 분할; vmPFC: BA 10, 11, 14, 24, 25, 32; amygdala)와 searchlight(보충). PLS 회귀(20 components), HRF convolution 후 TR로 리샘플, leave-one-film-out CV. 선형 혼합 모형 + sign-flip permutation. Tolman-Eichenbaum Machine(TEM)을 11×11 격자에서 학습한 뒤 MDS 기반 정서 환경에서 무작위 보행시켜 layer p(hippocampus 유사)와 g(entorhinal 유사) 활성 시계열을 만들고 이를 BOLD에서 decoding.
* **결과:** hippocampus는 이산 범주(r = 0.0525)를 affective space(r = 0.0428)보다 잘 decoding, vmPFC는 반대(0.0956 vs 0.0838)로 이중 해리. 후측 hippocampus가 세밀한 범주에 유리. 예측 시계열의 유사도 구조는 참가자 간 매우 안정적(Spearman ρ = .978). TEM layer p는 hippocampus에서 작은 척도로, layer g는 vmPFC에서 큰 척도로 잘 decoding. entorhinal 신호는 약함.
* **저자가 밝힌 한계와 향후 과제(Discussion 마지막 단락 등, 전문 확인):** valence-arousal 2차원은 단순화이며 effort, certainty, situational control 같은 다른 차원이 필요함; fMRI로는 phase code를 볼 수 없음(설치류, 인간 iEEG 필요); TEM 외 강화학습 기반 모델 비교 필요; 정서 개념이 공유된 통계 규칙인지 개인 경험으로 구성된 ad hoc 범주인지 미해결; graph형과 map형 표상의 관계 미해결.
* **같은 연구실 관련 연구:** Ma & Kragel (2026) PLOS Biology, vmPFC의 grid-like(hexadirectional) 정서 공간 부호화. 얼굴 morph와 문구 과제이며 **Emo-FilM 미사용** ([doi:10.1371/journal.pbio.3003795](https://doi.org/10.1371/journal.pbio.3003795)). Ma, Vafaie & Kragel (2025) 가설 리뷰 ([doi:10.1016/j.neubiorev.2025.106089](https://doi.org/10.1016/j.neubiorev.2025.106089)).

### 8.2 Emo-FilM을 사용한 다른 2024~2026 연구

| 연구 | 확인 수준 | 무엇을 했나 |
|---|---|---|
| Morgenroth et al. (2026) *Emotion* 26(5):1133-1147, [doi:10.1037/emo0001619](https://doi.org/10.1037/emo0001619) | PubMed, 초록만 | 평정 자료만으로 이산 정서와 성분의 관계. 이산 정서가 valence와 self-relevance appraisal로 위계적으로 조직되고, 13개 이산 정서가 성분으로 예측됨. Emo-FilM 평정 사용은 초록 내용과 저자로 강하게 추정 |
| Chan et al. (2026) *Human Brain Mapping* 47(11):e70617, [doi:10.1002/hbm.70617](https://doi.org/10.1002/hbm.70617) | PubMed, 초록만 | 정서 평정으로 frame을 골라 만든 emotion-informed functional gradient(피질, 피질하)로 불안, 개방성 예측. Emo-FilM 사용은 저자, 설계로 강하게 추정(본문 미확인) |
| David et al. (2025) EMBC, [doi:10.1109/EMBC58623.2025.11254034](https://doi.org/10.1109/EMBC58623.2025.11254034), arXiv:2507.12009 | PubMed, 초록만 (Emo-FilM 사용은 arXiv 요약 기준) | 시간 합성곱 CNN encoder-decoder로 시각 피질 voxel 예측과 frame 재구성. 정서 라벨 미사용 |
| Leipold et al. (2026) *Imaging Neuroscience* 4, [doi:10.1162/IMAG.a.1400](https://doi.org/10.1162/IMAG.a.1400) | PubMed, 전문(관련 절) | Emo-FilM을 반복검증 데이터로 사용(28명, 제공 전처리본, Brainnetome). ISC와 ISC-성격 연관이 영화마다 다름 |
| "Higher-order topology uncovers the multidimensional dynamics of naturalistic emotion" (bioRxiv 2026, doi:10.64898/2026.09.26.754452) | **미검증** (검색 결과의 bioRxiv, Sciety URL만, 저자 미확인) | 고차 위상(homological scaffold)이 50개 항목 기반 세밀한 정서 프로파일을 pairwise connectivity보다 잘 예측, pairwise는 arousal에 강하고 3개 데이터셋에 전이 |
| Radchenko (2026) spherical affective space preprint | **미검증** (2차 집계 사이트만) | Ma & Kragel의 MDS 궤적을 구면 좌표로 재분석했다는 요약. 원문 미확인으로 근거로 쓰지 않음 |

### 8.3 남은 기회 (Ma & Kragel 대비 차별점 표시)

각 항목은 탐색 후보이며 확정 질문이 아니다. 선행 수행 여부는 이번 검색 범위 안에서의 판단이다.

1. **Appraisal 공간의 지도 구조.** Ma & Kragel이 한계로 든 "certainty, situational control" 차원이 Emo-FilM에 Predictable, Controlled, Suddenly, Urgency, Agent로 이미 있다. 이 항목으로 만든 공간에서도 hippocampus-vmPFC 이중 해리나 grid-like 구조가 나오는지 검증. 선행: 확인 못 함(no로 추정). 근거: [doi:10.1038/s41467-025-68240-z](https://doi.org/10.1038/s41467-025-68240-z) Discussion 한계 단락; 논문 항목 정의.
2. **정서 대 시청각-의미 내용의 분리.** 영상, 오디오, 언어 foundation model feature를 경쟁 encoding 모형으로 넣고 variance partitioning을 해, hippocampus, vmPFC의 "정서 정보"가 내용 feature로 설명되는 부분을 제거. G1 해결 필요. 선행: Emo-FilM에서는 확인 못 함.
3. **규범 평정 대 본인 보고.** fMRI 참가자의 사후 클립 평정(5항목/영화)이 consensus에서 벗어나는 정도가 뇌 신호로 예측되는지. 표본과 커버리지가 작아 탐색적. 선행: 확인 못 함.
4. **보고된 생리 대 측정된 생리.** 평정자의 Heartrate, Muscle, Throat, Stomach 항목과 fMRI 참가자의 PPG, 호흡, EDA를 같은 시간축에서 비교하고 뇌-몸 결합(insula 등)을 검증. 생리 잡음과 신경 신호의 구분 필요. 선행: 확인 못 함.
5. **실제 전이 통계 기반 동역학 모델.** Ma & Kragel의 TEM은 MDS 격자 위 무작위 보행으로 학습. 영화의 실제 정서 전이 통계(1 Hz, 50항목)로 학습한 state-space, successor representation, RL 모형과 비교. 저자가 RL 모형 비교를 향후 과제로 제시. 선행: partially (Ma & Kragel).
6. **Label noise를 반영한 decoding.** 평정자별 원자료로 항목별 reliability 천장을 계산하고, decoding 성능을 천장 대비로 정규화하거나 잡음 모형을 학습에 포함. 선행: 확인 못 함.
7. **AI 평정의 검증 기준으로 사용.** MLLM이 만든 50항목 연속 평정을 human-human 일치도(3~4명)와 같은 지표로 비교하고, AI 평정이 뇌 신호를 consensus만큼 설명하는지 검정. G1 필요, 사전학습 오염 점검 필요. 선행: Emo-FilM에서는 확인 못 함. 다른 자극에서는 Du et al. (2025, arXiv:2509.24298).
8. **같은 영화의 외부 주석과 교차 타당화.** LIRIS-ACCEDE continuous V/A, aesthetic highlight(관객 EDA 동기화)와 Emo-FilM 항목, fMRI 참가자 EDA를 비교. 접근 조건 미확인.

---

## 9. 미확인 항목 목록

* 우리 환경의 데이터 경로, 원본 영상 보유 여부, 추출 feature, 계산 자원 (`reference/datasets_and_resources.md` 1절 공란)
* 논문 Table 1(영화별 장르, 내용, 런별 volume 수), Supplementary Table(항목 설명, 항목별 agreement, 평정자 배정표, 질문지 기술통계), Usage Notes 절의 존재와 내용 (출판사 페이지 차단)
* 최고(0.58)·최저(−0.01) agreement 항목명, 제외 항목 5개와 제외 영화 2편 각각의 r 값 대응, 검증 일치도 최저(0.08)·최고(0.70) 항목명
* 영화별 CC 라이선스 종류와 파생물 허용 여부, LIRIS-ACCEDE 다운로드 조건(동의서 필요 여부), 크레딧 절단 지점(`code/FilmInfo.txt`, xlsx 내용)
* 평정 시계열과 생리 신호의 실제 수치 분포, 결측, 불균형 (annex 본체 미다운로드)
* HBI, RV 회귀자의 공개 여부, slice timing과 distortion correction 적용 여부
* `LeassonLearned` 파일의 성격(중복인지 다른 판본인지)
* 참가자 모국어, 대사 언어의 영화별 구성
* "Higher-order topology ..." preprint의 저자와 본문, Radchenko preprint의 존재
* Chan et al. (2026), Morgenroth et al. (2026, Emotion), David et al. (2025)의 Emo-FilM 사용 여부를 본문으로 확정하지 못함(초록과 저자 기준 추정)
* LIRIS-ACCEDE 관련 서지(Baveye et al. 2015 IEEE TAC doi:10.1109/TAFFC.2015.2396531; ACII 2015)와 Muszynski et al. (2018, doi:10.1145/3175497)의 doi.org 직접 확인

## 10. 출처 목록

* Emo-FilM 논문: [doi:10.1038/s41597-025-04803-5](https://doi.org/10.1038/s41597-025-04803-5) (PubMed 40268934, PMC12019557)
* OpenNeuro ds004892: [openneuro.org/datasets/ds004892](https://openneuro.org/datasets/ds004892), GitHub 미러 [github.com/OpenNeuroDatasets/ds004892](https://github.com/OpenNeuroDatasets/ds004892)
* OpenNeuro ds004872: [openneuro.org/datasets/ds004872](https://openneuro.org/datasets/ds004872), GitHub 미러 [github.com/OpenNeuroDatasets/ds004872](https://github.com/OpenNeuroDatasets/ds004872)
* 저자 코드: [github.com/EllieMo/Emo-FilM](https://github.com/EllieMo/Emo-FilM)
* Ma & Kragel (2026) Nat Commun: [doi:10.1038/s41467-025-68240-z](https://doi.org/10.1038/s41467-025-68240-z)
* Ma & Kragel (2026) PLOS Biol: [doi:10.1371/journal.pbio.3003795](https://doi.org/10.1371/journal.pbio.3003795)
* Ma, Vafaie & Kragel (2025) NBR: [doi:10.1016/j.neubiorev.2025.106089](https://doi.org/10.1016/j.neubiorev.2025.106089)
* Morgenroth et al. (2026) Emotion: [doi:10.1037/emo0001619](https://doi.org/10.1037/emo0001619)
* Chan et al. (2026) HBM: [doi:10.1002/hbm.70617](https://doi.org/10.1002/hbm.70617)
* David et al. (2025) EMBC: [doi:10.1109/EMBC58623.2025.11254034](https://doi.org/10.1109/EMBC58623.2025.11254034)
* Leipold et al. (2026) Imaging Neuroscience: [doi:10.1162/IMAG.a.1400](https://doi.org/10.1162/IMAG.a.1400)
* Morgenroth et al. (2023) SCAN: [doi:10.1093/scan/nsad063](https://doi.org/10.1093/scan/nsad063)
* Emory 보도(2026년 3월): [news.emory.edu](https://news.emory.edu/features/2026/03/esc_feature_brain_charts_emotion_10-03-2026/index.html)
