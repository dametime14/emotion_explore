# Stage 1 Dataset Forensic Audit: Horikawa et al. (2020)

* 작성: dataset-auditor (Agent 1, Dataset & Metadata Specialist). general-purpose 에이전트가 `.claude/agents/dataset-auditor.md` 지침을 직접 읽고 수행함.
* 기준일: 2026-11-12
* 대상 논문: Horikawa, Cowen, Keltner, Kamitani (2020). The Neural Representation of Visually Evoked Emotion Is High-Dimensional, Categorical, and Distributed across Transmodal Brain Regions. iScience 23(5):101060. [doi:10.1016/j.isci.2020.101060](https://doi.org/10.1016/j.isci.2020.101060), PMID 32353765, [PMC7191651](https://pmc.ncbi.nlm.nih.gov/articles/PMC7191651/)
* 우리 환경의 데이터 경로: **미확인** (`reference/datasets_and_resources.md` 1절이 비어 있음)

## 검증 수준 표기

| 표기 | 뜻 |
|---|---|
| **[1차]** | 데이터 제공자가 직접 낸 파일을 이 감사에서 직접 열어 확인함 (OpenNeuro ds002425 GitHub 미러의 README, dataset_description.json, *_bold.json, *_events.tsv; KamitaniLab GitHub 저장소의 README, 코드, LICENSE) |
| **[본문]** | 해당 논문 본문을 PubMed Central 전문(PubMed MCP 도구)으로 직접 읽음 |
| **[2차 본문]** | 이 데이터를 재사용한 다른 논문의 본문을 직접 읽고 그 서술을 확인함 (원 데이터 제공자 서술이 아님) |
| **[검색]** | WebSearch 결과 요약 또는 스니펫으로만 확인함. 원 페이지는 열지 못함 |
| **미확인** | 확인하지 못함 |

접근 제약: 이 세션에서 WebFetch는 pmc.ncbi.nlm.nih.gov, data.mendeley.com 모두 DNS 차단되어 이후 웹 페이지 직접 열람을 시도하지 않았다. figshare, OpenNeuro 웹 페이지, Google Form, Cowen & Keltner (2017) PNAS 본문은 열지 못했다. 대신 공개 GitHub 저장소를 git으로 읽었다 (부록 B).

---

## Gate 판정

| Gate | 판정 | 근거 요약 | 핵심 출처 |
|---|---|---|---|
| **G1 원본 자극 접근** | **공개 경로 기준: 요청 필요.** 우리 환경 보유 여부: **미확인** | 원본 비디오는 어떤 공개 저장소(OpenNeuro, figshare, GitHub)에도 포함되어 있지 않다. 데이터 제공자는 Cowen & Keltner 쪽 Google Form으로 비디오를 요청하라고 안내한다. 요청 양식의 이용 조건(연구 목적 제한, 재배포 금지, 라이선스)은 양식을 열지 못해 **미확인**이다. 비디오는 인터넷에서 수집한 것이라 제3자 저작권이 걸려 있을 가능성이 높다(추정). 여러 독립 연구진(2023~2025)이 원본 비디오를 실제로 써서 feature를 뽑거나 MLLM에 입력했으므로 요청 경로는 실제로 작동해 온 것으로 보인다(간접 증거). Mendeley 예치본(doi:10.17632/jbk2r73mzh.1)에 비디오가 들어 있는지는 **미확인**. | [1차] OpenNeuro README "you can request the videos from https://goo.gl/forms/XErJw9sBeyuOyp5Q2"; [1차] GitHub README "You can request the videos with emotion ratings from the following URL"; [2차 본문] Du et al. 2023 Key resources table "Video stimuli / Cowenlab / goo.gl/forms/XErJw9sBeyuOyp5Q2"; [본문] Horikawa 2020 Discussion: Cowen & Keltner가 인터넷의 자극을 활용해 자극 세트를 구성 |
| **G2 fMRI 형식과 전처리 수준** | **Raw와 전처리본 모두 공개.** Raw: BIDS(NIfTI, CC0). 전처리본: fMRIPrep 기반, **native volume 공간**, 비디오 1개당 1 sample로 평균된 block-level 응답(HDF5, BrainDecoderToolbox2 형식). 표준공간(MNI/fsaverage) 전처리본과 전처리된 연속 time series 공개 여부는 **미확인** | Raw: 5명 x 8 session x 61 run, TR 2 s, 2 mm isotropic, MB 4, 3T Siemens Verio. 전처리본: 4 s shift 후 블록 평균, nuisance regression, despike, z-score. Voxel 좌표와 ROI 마스크(HCP360 360 영역, subcortical 10 영역 등) 포함. pycortex surface 파일 제공. 코드 MIT 라이선스 | [1차] ds002425 README, *_bold.json, dataset_description.json ("License": "CC0"); [1차] EmotionVideoNeuralRepresentationPython config `EmotionMovie_fmriprep_volume_native`, data/files.json; [1차] MATLAB 코드 prepare_roidata.m; [2차 본문] Du et al. 2023 STAR Methods 전처리 서술 |
| **G3 라벨 접근과 평정 주체** | **라벨 공개(figshare features). 평정 주체는 fMRI 참가자가 아니라 Cowen & Keltner (2017)의 별도 MTurk 평정자 표본(규범적 평정).** fMRI 참가자 본인 보고: **없음**. 평정자 개인 수준 데이터: **비공개**(비디오당 집계값만 공개) | 34 emotion category 점수(비디오당 해당 범주를 고른 평정자 비율), 14 affective dimension 점수(9점 척도 평균), semantic 73차원(crowdsourcing 인간 주석), vision 1000차원(사전학습 DNN 출력). 비디오당 1개 벡터이며 시간 해상도 없음 | [본문] Horikawa 2020 Limitations "ratings ... were averages from multiple raters and not from the subjects of our fMRI experiment"; [1차] BIDS events.tsv 열은 onset, duration, trial_type, stimulus_name, stim_index뿐(응답 열 없음); [1차] Python data/README의 features 구조와 34, 14 열 이름; [2차 본문] Asanuma et al. 2025 "only the average frequency ... was publicly available, and no participant-level data were disclosed" |

### Gate 관련 Coordinator 전달 사항
* G1이 "불가"는 아니지만 "요청 필요"이므로 `datasets_and_resources.md` 3절 규정상 Coordinator가 영향과 대안을 정리해야 한다. 대안 후보: (1) 즉시 Google Form 요청 제출, (2) 요청 승인 전까지는 figshare의 미리 계산된 feature(category, dimension, semantic 73, vision 1000)와 raw BIDS만으로 가능한 분석을 먼저 설계, (3) Mendeley 예치본 내용을 사용자가 브라우저로 직접 확인(이 세션에서는 차단됨).
* `datasets_and_resources.md` 2.1절의 "2026년 4월 공개" 표현은 오해 소지가 있다. Raw BIDS는 OpenNeuro에 **2020-04-24**(v1.0.0)부터, 전처리본과 라벨은 figshare에 2020년부터 공개되어 있었다 [1차: ds002425 CHANGES]. 2026-04-15는 Mendeley 예치본 v1의 공개일로 검색 색인에 표시된 날짜다 [검색]. 따라서 "2026 공개 이후 첫 사용 연구"라는 틀은 맞지 않으며, 2022년부터 이미 여러 재분석이 있다(8.3절).

---

## 1. Verified Dataset Specification

### 1.1 Acquisition & Structure (A)

| 항목 | 값 | 출처 / 검증 수준 |
|---|---|---|
| 피험자 수 | 5명 (sub-01 ~ sub-05) | [1차] ds002425 README, 디렉터리 구조 |
| 피험자 인구통계 | 여성 1명, 23~34세, 정상 또는 교정 시력, ATR 윤리위원회 승인 | [2차 본문] Du et al. 2023 STAR Methods. 원 논문 Transparent Methods는 미열람 |
| 피험자 국적, 모국어, 문화권 | **미확인** (촬영은 일본에서 수행. 평정자는 미국 영어 사용자) | 평정자 정보는 [2차 본문] Du et al. 2023 |
| 세션 | 피험자당 8 functional session (ses-01~ses-08) + 별도 anatomy session | [1차] README, 디렉터리 |
| Run | 피험자당 61 run. 세션당 run 수는 세션마다 다름(예: sub-01 = 6, 8, 8, 8, 8, 8, 8, 7) | [1차] events.tsv 집계 |
| Run 구조 | 시작 휴지 32 s, 자극 블록 36개, 종료 휴지 6 s. Run 길이 414~588 s (평균 475.7 s). 피험자당 총 functional 시간 약 484분 | [1차] events.tsv 집계 (sub-01) |
| 자극 블록 | 피험자당 2,196 블록 = 61 run x 36 블록 | [1차] events.tsv |
| 블록 길이 | 10 s가 1,573개(71.6%), 10 s 초과 623개, 20 s 이상 87개, 최대 94 s | [1차] events.tsv 집계 |
| 블록 구성 | 8 s보다 짧은 비디오는 총 제시 시간이 8 s를 넘을 때까지 반복 재생. 모든 블록 뒤에 2 s 휴지 | [2차 본문] Du et al. 2023. 블록 길이 분포(최소 10 s)와 일치 |
| 과제 | 자유 시청(free viewing). 응시점 고정 없음. 반응 과제 없음 | [2차 본문] Du et al. 2023; [본문] Horikawa 2020 Limitations("allowed the subjects to freely view") |
| 자극 순서 | 5명 모두 **동일한 자극 순서** | [1차] events.tsv 비교 |
| Scanner | 3T Siemens MAGNETOM Verio | [1차] *_bold.json (Manufacturer SIEMENS, ManufacturersModelName Verio, MagneticFieldStrength 3.0) |
| 촬영 장소 | Kyoto University Kokoro Research Center | [검색] bioRxiv 872192 스니펫. 미열람 |
| EPI | TR 2000 ms, TE 43 ms, flip angle 80°, voxel 2 x 2 x 2 mm, FOV 192 x 192 mm, 76 slices, slice gap 0 mm, multiband 4, 전뇌 커버 | [1차] README, *_bold.json |
| 해부 영상 | T1w MPRAGE 1 mm isotropic(TR 2250 ms, TE 3.06 ms, TI 900 ms, FA 9°), pydeface 처리. 세션별 inplane T2 (0.75 x 0.75 x 2.0 mm) | [1차] README |
| Raw 형식 | BIDS (BIDSVersion 1.0.2 표기), NIfTI-1. 파일 구성: bold.nii.gz 305개, bold.json 305개, events.tsv 305개, inplaneT2 40개, T1w 5개 | [1차] 파일 집계 |
| Raw 라이선스 | CC0 | [1차] dataset_description.json |
| Raw 버전 | v1.0.0 (2020-04-24), v1.0.1 (2020-05-29, README 수정), v1.0.2 (2022-03-21, anatomy 재업로드). DOI 10.18112/openneuro.ds002425.v1.0.2 | [1차] CHANGES, dataset_description.json |
| 생리 신호, eye tracking, 행동 반응, participants.tsv | **없음** (BIDS에 해당 파일 없음) | [1차] 파일 집계 |
| 전처리 | fMRIPrep 기반 motion correction, slice timing correction, T1 coregistration 후 원래(native) 공간으로 resampling. 이후 nuisance regression, 4 s shift, despike, 블록 내 평균(비디오 제시 + 휴지 포함), 블록 간 z-score. 피험자당 2,196 sample | [2차 본문] Du et al. 2023; [본문] Horikawa 2020 Results("shifted by 4 s and averaged"); [1차] Python config 이름 `EmotionMovie_fmriprep_volume_native` |
| 전처리본 형식 | HDF5 (BrainDecoderToolbox2 형식). 데이터 행렬과 metadata(VoxelData 플래그, voxel_x/y/z 좌표, Session, Run, Block, Label, ROI 플래그) | [1차] MATLAB `prepare_roidata_individual.m` |
| ROI | HCP360 cortical parcellation 360 영역, subcortical 10 영역(thalamus, hippocampus, hypothalamus, pallidum, brainstem, caudate, putamen, nucleus accumbens, amygdala, cerebellum), 개별 ROI 13개 | [1차] MATLAB 코드, Python `config/roi_set/wholebrain.yaml`; [본문] Horikawa 2020 |
| Surface | 피험자별 pycortex surface 파일(figshare 제공). 분석은 volume에서 수행 | [1차] Python data/README, files.json |
| 표준공간(MNI, fsaverage) 전처리본 | **미확인** (공개 파일 목록에서 보지 못함) | |
| 전처리된 연속 time series | **미확인** (공개본은 블록 평균 sample로 보임) | |
| Train/test 분할 | 공식 분할 없음. 원 논문은 run 단위 6-fold CV (run 1-10, 11-20, 21-30, 31-40, 41-50, 51-61). Python 설정은 `exclusive_key: stimulus_name` | [1차] MATLAB `p.run2FoldAssignIdx`, Python config |

### 1.2 자극 수 불일치 정리

| 숫자 | 의미 | 출처 |
|---|---|---|
| 2,185 | Cowen & Keltner (2017) 비디오 라이브러리 크기 | [본문] Cowen & Keltner 2017 abstract (PubMed) |
| 2,196 | fMRI에서 제시한 stimulus_name 개수(0001~2196, 각 1회 제시) | [1차] events.tsv |
| 2,181 | 내용이 중복된 비디오 15개 label index를 제거한 고유 비디오 수. 원 논문 분석 단위 | [1차] MATLAB `p.dupidx = [1,4:8,11,859,866,1673,2157,2187,2188,2194,2195]` 주석 "duplicate index ... These will be removed"; [본문] Horikawa 2020 |
| 2,180 | Du et al. (2025, arXiv:2509.24298) 서술 | [검색] |

2,196과 2,185의 차이(11개), 2,181과 2,185의 관계는 **미확인**이다. 중복 15개는 같은 내용이 다른 ID로 두 번 제시되었다는 뜻으로 해석되며(코드 주석 기준 추정), 이 15쌍이 유일한 반복 제시다.

---

## 2. Complete Metadata & Annotation Inventory

### 2.1 공개 저장소별 실제 내용

| 경로 | 내용 | 라이선스 | 검증 |
|---|---|---|---|
| OpenNeuro [ds002425](https://openneuro.org/datasets/ds002425) | Raw BIDS: 5명 x 8 session x 61 run의 EPI, T1w, inplane T2, events.tsv(onset, duration, trial_type, stimulus_name, stim_index). 비디오 없음, 평정 없음, 생리 없음 | CC0 | [1차] GitHub 미러 OpenNeuroDatasets/ds002425 (commit 3f94b2b, 2022-03-21)의 메타데이터 파일. 영상 본체(git-annex)는 내려받지 않음 |
| figshare [10.6084/m9.figshare.11988351](https://doi.org/10.6084/m9.figshare.11988351) (MATLAB판) | 피험자 5명의 전처리 fMRI(`fmri_SubjectN_SessionM.h5` 형식), ratings/features(category, dimension, visual object, semantic), ROI 정보, principal gradient 값 | **미확인** | [1차] GitHub README와 MATLAB 코드가 요구하는 파일 목록. figshare 페이지 미열람 |
| figshare [26633035](https://figshare.com/articles/dataset/The_neural_representation_of_visually_evoked_emotion_is_high-dimensional_categorical_anddistributed_across_transmodal_brain_regions_Python_version/26633035) (Python판) | `fmri_Subject1~5.h5`, `fmri_Subject1_for_tutorial.h5`, `features.zip`(features/amt/mean_score_concat/{category, dimension, semantic, vision}, 비디오당 1개 .mat), `pycortex_Subject1~5.zip` | **미확인** | [1차] Python 저장소 `data/files.json`(md5 포함), `data/README.md` |
| GitHub [KamitaniLab/EmotionVideoNeuralRepresentation](https://github.com/KamitaniLab/EmotionVideoNeuralRepresentation) | 재현용 MATLAB 코드, UMAP notebook, `data/fmri/misc/roiInf.mat` | MIT (Copyright 2024 Kamitani Lab) | [1차] clone (commit 8fe23a0, 2024-08-21) |
| GitHub [KamitaniLab/EmotionVideoNeuralRepresentationPython](https://github.com/KamitaniLab/EmotionVideoNeuralRepresentationPython) | Python 재현 코드(nested CV 하이퍼파라미터 탐색은 미구현이라고 명시), 다운로드 스크립트, 34/14 열 이름 | 저장소 LICENSE 파일 존재, 종류는 미확인 | [1차] clone (commit 451236c, 2025-11-19) |
| Mendeley Data [10.17632/jbk2r73mzh.1](https://doi.org/10.17632/jbk2r73mzh.1) | 설명문에 "fMRI responses to all 2185 videos" 표현. v1 공개일 2026-04-15로 색인됨. 2020년 논문의 Data and Code Availability가 이 DOI를 OpenNeuro, figshare와 함께 열거한다는 검색 요약이 있음. **파일 목록, 형식, 라이선스, 비디오 포함 여부 모두 미확인** | 미확인 | [검색]만. data.mendeley.com 접근 차단 |
| KamitaniLab/OpenData 포털 | 이 데이터셋 항목에 OpenNeuro(raw)와 figshare(전처리본, features)만 열거. BrainLiner, Mendeley 항목 없음 | | [1차] clone |
| BrainLiner | 이 데이터셋 항목 **발견 못함**. README의 연락처만 brainliner-admin@atr.jp | | [1차] README |
| 원본 비디오 | Google Form 요청: https://goo.gl/forms/XErJw9sBeyuOyp5Q2 ("request the videos with emotion ratings") | 미확인 | [1차] README 두 곳; 양식 내용은 미열람 |

### 2.2 Stimulus Metadata (B)

| 항목 | 내용 | 출처 |
|---|---|---|
| 시각 내용 | 인터넷에서 수집한 짧은 정서 유발 비디오. 폭넓은 상황(예: 풍경, 부상, 성적 내용, 동물, 아기 등) | [본문] Horikawa 2020 Discussion; [2차 본문] Asanuma 2025 사례 서술 |
| 길이 | 0.15~90 s, 평균 약 5 s | [2차 본문] Du 2023 (범위), Asanuma 2025 (평균) |
| 제시 크기 | 가로세로 최대 12도, 회색 배경 중앙 | [2차 본문] Du 2023 |
| 오디오, 음악, 음성 | **fMRI 제시 시 소리 제거(무음).** Cowen & Keltner 평정 시에도 오디오 없음 | [본문] Horikawa 2020 Discussion "only visual stimuli (with no sound)"; [2차 본문] Du 2023 "the sound of the videos was removed"; [2차 본문] Asanuma 2025 "containing no audio" |
| Captions, transcripts | 공개본에 **없음** | [1차] 파일 목록 |
| Object, scene, semantic feature | semantic 73차원: 개념(예: cats, indoor, sports)을 crowdsourcing으로 인간이 주석. vision 1000차원: 물체 인식용 사전학습 DNN 출력(망 이름 **미확인**, 1000차원이라 ImageNet 클래스 출력으로 추정) | [본문] Horikawa 2020 Results; [1차] Python Tutorial "semantic features (73 feat), and vision features (1000 feat)" |
| 시간 정렬 | 비디오(블록) 단위 onset, duration만 있음. 프레임 단위 정렬 정보 없음. 반복 재생된 짧은 비디오의 재생 횟수 정보 없음 | [1차] events.tsv |
| 원본 자극 가용성 (G1) | 요청 필요 (Gate 표 참조) | |
| 저작권, 접근 제한 | 요청 양식 조건 **미확인**. 인터넷 수집 영상이라 재배포 제한 가능성 높음(추정). 우리 쪽 산출물에 프레임이나 클립을 싣는 것은 별도 확인 필요 | |
| 같은 자극의 공개 시각화 | Cowen & Keltner가 비디오 라이브러리와 interactive map을 공개했다고 abstract에 명시. 지도에 실린 형태(GIF 등)와 이용 조건은 **미확인** | [본문] Cowen & Keltner 2017 abstract |

### 2.3 Labels & Annotations (C)

| 항목 | 내용 | 출처 |
|---|---|---|
| Emotion category | 34개: admiration, adoration, aesthetic_appreciation, amusement, anger, anxiety, awe, awkwardness, boredom, calmness, confusion, contempt, craving, disappointment, disgust, empathic_pain, entrancement, envy, excitement, fear, guilt, horror, interest, joy, nostalgia, pride, relief, romance, sadness, satisfaction, sexual_desire, surprise, sympathy, triumph | [1차] Python data/README |
| Affective dimension | 14개: Approach, Arousal, Attention, Certainty, Commitment, Control, Dominance, Effort, Fairness, Identity, Obstruction, Safety, Upswing, Valence | [1차] Python data/README |
| 파생 라벨 | 코드에 `dim28continuous`(14 dimension을 중립 5 기준 양수부와 음수부로 나눈 28열), `dim28binary`, `categcontinuous`, `dim_cat` 존재. figshare 포함 여부는 MATLAB판 기준 **미확인** | [1차] MATLAB 코드 |
| Category 평정 방식 | 평정자가 34개 중 느낀 범주를 하나 이상 자유롭게 선택. 공개 점수는 비디오별로 해당 범주를 선택한 평정자 비율 | [2차 본문] Asanuma 2025 (Cowen & Keltner 인용). Du 2023은 "100-point scale 후 이진화"로 서술해 표현이 다름. 원문 PNAS 미열람 |
| Dimension 평정 방식 | 9점 Likert. 중립 5 | [2차 본문] Du 2023; [본문] Horikawa 2020 "after 5 [neutral] was subtracted" |
| 평정자 표본 | Amazon Mechanical Turk, 미국 영어 사용자 853명. fMRI 실험 비참여자 | [2차 본문] Du 2023. 853명 수치는 보도 기사로도 [검색] 확인 |
| 비디오당 평정자 수 | Category: 9~17명. Dimension: **미확인** | [2차 본문] Asanuma 2025; [검색] PNAS PDF 스니펫 |
| 평정 주체 | 별도 평정자의 규범적(normative) 집계 평정. fMRI 참가자 본인 평정 **없음** | [본문] Horikawa 2020 Limitations; [1차] BIDS에 응답 데이터 없음 |
| 평정 문항의 관점 | 평정자 자신이 느낀 정서(self-report of felt emotion)를 묻는 방식으로 서술됨. 즉 평정자에게는 1인칭 보고이지만 fMRI 참가자에게는 타인의 보고 | [2차 본문] Asanuma 2025 "Self-reported selection of multiple felt emotions"; [본문] Cowen & Keltner abstract "reported emotional experience" |
| Appraisal, subjective report | 14 dimension 일부가 appraisal 성격(Certainty, Control, Fairness, Obstruction, Effort 등). 별도 appraisal 질문지나 fMRI 참가자 주관 보고는 없음 | [1차] 열 이름 |
| Social, cognitive label | semantic 73차원 일부만 해당. 별도 social label(사람 수, 얼굴 유무 등) 공개본 **없음**. Kiyokawa & Hayashi (2024)는 얼굴 포함 여부를 직접 나눠 분석함 | [2차 본문] Kiyokawa 2024 |
| 시간 해상도 | 비디오당 1개 벡터. 시간 연속 평정 없음 | [1차] features 구조 |
| Free response | Cowen & Keltner 연구에 자유 응답 과제가 있었다는 보도가 있으나 공개본 포함 여부 **미확인** | [검색] |
| 평정자 개인 수준 데이터 | 비공개(비디오별 평균 빈도만 공개) | [2차 본문] Asanuma 2025 |
| Inter-rater reliability, noise ceiling | Cowen & Keltner는 27개 범주가 신뢰할 만하게 구분된다고 보고(abstract). 범주별 reliability 수치는 PNAS 본문 미열람으로 **미확인**. 개인 수준 데이터가 없어 우리가 split-half reliability를 다시 계산할 수 없다. fMRI 쪽은 단일 제시라 voxel noise ceiling 추정 불가(원 논문 명시) | [본문] Cowen & Keltner abstract; [본문] Horikawa 2020 Discussion 6째 단락 |
| 결측, 불균형 | envy, contempt, guilt는 어느 영역에서도 5명 일관되게 decoding되지 않음. 저자는 해당 범주를 유발한 비디오 비율이 낮은 점을 원인 일부로 봄. Du 2023도 범주별 비디오 수 불균형을 한계로 명시 | [본문] Horikawa 2020 Results; [2차 본문] Du 2023 Limitations |

### 2.4 정서 출처의 엄격한 구분

| 정서의 종류 | 이 데이터셋에 있는가 | 설명 |
|---|---|---|
| 실제 관찰된 정서 (생리, 표정, 행동) | **없음** | BIDS에 physio, eye tracking, 얼굴 영상, 행동 반응 없음 [1차] |
| fMRI 참가자가 보고한 정서 | **없음** | 자유 시청, 반응 과제 없음. 원 논문 Limitations가 명시 [본문] |
| 별도 평정자의 규범적 평정 | **있음 (유일한 인간 정서 라벨)** | Cowen & Keltner MTurk 평정자의 비디오별 집계값. 평정자 자신은 felt emotion을 보고했지만 fMRI 참가자 입장에서는 타인의 집단 평균이며 문화권도 다를 수 있다 |
| 자극에 표현된 정서 (portrayed) | **별도 라벨 없음** | 34 범주 점수는 "유발된(evoked) 정서" 평정이지 "등장인물이 표현한 정서" 라벨이 아니다. 둘이 섞여 있을 수 있음(원 논문의 first-person vs third-person confound) |
| AI가 추정한 정서 | **공개본에 없음.** 외부 연구가 생성함 | Asanuma 2025 (Gemini, GPT-4.1, Molmo의 34 범주 추정), Du et al. 2025 arXiv (Qwen2-VL, Llama-3.1 odd-one-out 판단으로 30차원 embedding), EmoMind 2026 (DeBERTa 기반 CK34 scorer) |

원 저자 스스로 결과를 "emotional experience (or affordances)"로 표현했다 [본문 Horikawa 2020 Introduction, Results]. 즉 이 데이터에서 decoding되는 것은 "이 비디오가 사람들에게 평균적으로 불러일으키는 정서" 또는 "정서적 affordance"이며, 스캐너 안 참가자의 주관 경험을 직접 읽었다고 해석할 수 없다.

---

## 3. Available vs Missing Information

| 범주 | 있음 | 없음 또는 미확인 |
|---|---|---|
| 뇌 데이터 | Raw BIDS(CC0), 전처리 block-level sample(native volume), ROI 마스크, pycortex surface, T1w | 표준공간 전처리본(미확인), 전처리 연속 time series(미확인), 반복 제시 기반 noise ceiling(없음) |
| 자극 | stimulus_name(0001~2196), 블록 onset과 duration | 원본 비디오(요청 필요), 비디오 실제 길이와 반복 재생 횟수, 출처 URL, 같은 원본 영상에서 잘린 클립 여부(미확인) |
| 정서 라벨 | 34 category 비율, 14 dimension 평균, 파생 라벨 | 평정자 개인 수준 데이터, 비디오당 dimension 평정자 수, 범주별 reliability 수치(미확인), 시간 연속 평정, fMRI 참가자 보고 |
| 기타 라벨 | semantic 73, vision 1000 | caption, transcript, 얼굴/사람 수 등 social label, 사용된 DNN 이름(미확인) |
| 참가자 정보 | 5명, 성별 1F/4M, 연령 범위(2차 출처) | participants.tsv, 문화권, 성격, 정서 특성 척도 |
| 생리, 행동 | 없음 | 심박, 호흡, 피부전도, eye tracking, 반응 |
| 코드 | MATLAB 원 재현 코드(MIT), Python 간이판 | Python판 nested CV 미구현(저장소 명시) |

---

## 4. Potential Modeling Tasks (D)

각 과제에 G1 의존 여부를 표시한다. "G1 불필요"는 figshare feature와 raw BIDS만으로 가능함을 뜻한다.

| 과제 | 내용 | G1 의존 | 근거 |
|---|---|---|---|
| Emotion decoding | 34 category, 14 dimension 연속 점수 회귀. 원 논문 baseline(ROI별 ridge, ensemble)이 있음 | 불필요 | Horikawa 2020 |
| Semantic decoding | semantic 73차원 decoding | 불필요 | Horikawa 2020 |
| Vision decoding (feature) | vision 1000차원 decoding. 최신 video model feature decoding은 G1 필요 | 부분 | Horikawa 2020 |
| 비디오 재구성 | 짧은 무음 클립, 단일 제시라 평가 설계가 어려움. 원본 비디오 필요 | 필요 | 추론 |
| Encoding (기존 feature) | category, dimension, semantic, vision banded ridge, variance partitioning | 불필요 | Horikawa 2020, Du 2023 |
| Encoding (최신 모델) | CLIP, V-JEPA 계열, MLLM embedding으로 encoding 비교 | 필요 | Du et al. 2025 arXiv, Kiyokawa 2024 (범주 이름 텍스트 embedding만 쓰면 G1 불필요) |
| Multimodal alignment | 범주 이름 text embedding과 뇌 RSM 비교(G1 불필요), 비디오-텍스트-뇌 3자 정렬(G1 필요) | 부분 | Kiyokawa 2024 |
| Brain Foundation Model adaptation | raw BIDS를 fMRI foundation model 입력으로 사용, emotion probe 학습 | 불필요 | ds002425가 FM 사전학습에 포함되었는지 **미확인**이라 contamination 점검 필요 |
| Temporal representation | 대부분 8 s 이하 루프 재생 블록이라 비디오 내 동역학 분석 여지가 작음. 20 s 이상 블록 87개만 시간 분석 후보 | 부분 | [1차] 블록 길이 분포; Du 2023 Limitations |
| Generative modeling | decoded emotion vector로 caption, 이미지, 비디오 생성 조건화 | 부분 | EmoMind 2026 |
| Cross-subject transfer | 5명 동일 자극, 동일 순서, 각 2,196 sample이라 functional alignment(hyperalignment, shared response) 시험에 적합 | 불필요 | 추론. Westlin 2025는 개인 간 변동이 크다고 보고 |
| Cross-dataset transfer | 34 범주 decoder를 Emo-FilM 등에 적용, 또는 반대 방향 | 불필요(라벨 수준), 필요(자극 feature 수준) | EmoMind 2026이 Horikawa를 cross-dataset 평가에만 사용 |
| AI-generated annotation 추가 | MLLM으로 비디오별 34 범주, appraisal, portrayed emotion, 사람 수 등 생성 | 필요 | Asanuma 2025: 범주 수준 구조는 인간과 강하게 일치하나 개별 비디오 수준 일치는 제한적. 따라서 AI 라벨은 "AI 추정 정서"로 따로 표기하고 인간 평정을 대체하는 근거로 쓰지 않는다 |

---

## 5. Unique Advantages

1. **자극 수.** 고유 비디오 2,181개로, 정서 fMRI 데이터 중 조건 수가 가장 많은 축에 속한다. 원 저자도 "richest set of emotional visual stimuli investigated to date in neuroscience"라고 서술 [본문 Horikawa 2020 Discussion].
2. **피험자당 데이터 양.** 1인당 61 run, 약 8시간 functional 데이터 [1차]. 소수 피험자 고밀도(deep sampling) 설계로 개인 내 모델링에 유리하다.
3. **세분화된 정서 분류 체계.** 34 category와 14 dimension을 같은 자극에 동시에 갖고 있어 category vs dimension 비교, 표현 기하(geometry) 분석에 직접 쓸 수 있다.
4. **개방성.** Raw CC0, 전처리본, 재현 코드(MIT), ROI 정의, surface 파일까지 공개 [1차].
5. **비교 기준선의 축적.** 원 논문(2020), Du 2023, Kiyokawa 2024, Westlin 2025(반대 해석), EmoMind 2026 등 같은 데이터에 대한 여러 분석이 있어 새 방법의 비교 기준과 "이미 수행됨" 판단 근거가 풍부하다.
6. **이론적 쟁점의 시험대.** 같은 데이터로 categorical 해석(Horikawa 2020)과 constructionist 재분석(Westlin 2025)이 충돌하므로 분석 가정이 결론을 바꾸는지 검증하는 메타과학적 연구에 쓸 수 있다.

---

## 6. Methodological Limitations

| 문제 (CLAUDE.md 6절) | 이 데이터셋의 상태 | 근거 |
|---|---|---|
| 참가자 경험 vs 자극 정서 | 참가자 보고 없음. 라벨은 타인의 집단 평균. first-person vs third-person 혼재 가능 | [본문] Horikawa 2020 Limitations |
| 인간 평정 vs 모델 평정 | 공개 라벨은 모두 인간 평정. AI 라벨을 추가하면 반드시 별도 표기 | |
| Emotion vs visual/semantic representation | 정서 점수와 semantic feature가 상관됨. 원 논문은 emotion model이 semantic model보다 "조금이라도" 나은 영역을 정서 부호화로 간주한다고 명시. Du 2023도 banded ridge 후에도 confound 가능성을 한계로 명시 | [본문] Horikawa 2020; [2차 본문] Du 2023 |
| Encoding accuracy vs explanatory adequacy | 단일 제시라 설명 가능 분산 상한(noise ceiling)을 모름 | [본문] Horikawa 2020 Discussion |
| Decodability vs representation vs causality | 상관 데이터만 있음. 인과 조작 없음 | |
| HRF와 temporal autocorrelation | 고정 4 s shift 후 블록 평균. 블록에 2 s 휴지 포함. 10 s 블록이 연속되어 인접 블록 응답이 섞일 수 있음 | [2차 본문] Du 2023; [1차] 블록 길이 |
| Leakage | (1) 내용 중복 15쌍은 반드시 같은 fold에 두거나 제거. (2) 같은 원본 영상에서 잘린 클립이 여러 개인지 **미확인**이라 movie-level leakage 가능성 점검 필요. (3) 5명 동일 순서라 cross-subject 분석 시 순서, 피로 효과가 공유됨 | [1차] 코드, events.tsv |
| Repeated stimulus confound | 반복 제시 거의 없음(15쌍 추정). 대신 noise ceiling을 못 구함 | |
| Inter-rater agreement, label noise | 비디오당 9~17명 평정의 비율값이라 범주별 잡음이 큼. 개인 수준 데이터가 없어 재추정 불가. Du 2023은 dimension 평정이 category보다 잡음이 클 수 있어 직접 비교가 category에 유리할 수 있다고 지적 | [2차 본문] Asanuma 2025, Du 2023 Discussion |
| 공선성 | category, dimension, semantic, vision feature 간 상관 | [본문] Horikawa 2020 |
| 시공간 해상도 | TR 2 s, 2 mm. 짧은 비디오가 대부분이라 비디오 내 동역학 분석 제한 | [1차] |
| ROI 선택과 circular inference | 원 논문은 학습 fold 안에서만 voxel(ROI당 500개)을 고르고, ensemble decoder의 ROI는 nested CV로 선택. 재사용 시 같은 원칙 유지 필요 | [1차] 코드 `nSelectVoxels = 500`; [본문] Horikawa 2020 Results; [2차 본문] Kiyokawa 2024 Methods |
| Multiple comparisons | 370 ROI, voxel 수준 다중비교. 원 논문은 Bonferroni 사용 | [본문] |
| 접근성, 라이선스 | Raw CC0, 코드 MIT. figshare와 Mendeley 라이선스, 비디오 이용 조건 미확인 | |
| 사전학습 모델 contamination | 비디오가 인터넷 출처이고 2017년부터 interactive map이 공개되어 대형 모델 학습 데이터에 포함됐을 가능성(추정). ds002425의 fMRI foundation model 사전학습 포함 여부 미확인 | |
| Cross-dataset annotation incompatibility | 7절 참조 | |
| 피험자 수 | 5명이라 개인차, 집단 일반화 주장에 약함. Westlin 2025는 개인 간 변동이 크고 원래의 범주-뇌 대응이 재현되지 않는다고 보고 | Westlin 2025 abstract (PubMed 메타데이터로 확인, 본문 미열람) |
| 문화, 언어 불일치 | 평정자는 미국 영어 사용자, fMRI 참가자는 일본 촬영(국적 미확인) | [2차 본문] Du 2023 |
| Gaze | 자유 시청이며 eye tracking 없음. 원 논문이 gaze 영향 가능성을 한계로 명시 | [본문] Horikawa 2020 Limitations |
| 무음 | 청각, 음악, 음성 정서 질문에 직접 쓸 수 없음 | [본문] |

---

## 7. Cross-dataset Compatibility Notes

| 대상 | 라벨 결합 가능성 | 근거와 주의점 |
|---|---|---|
| Emo-FilM (Morgenroth et al., 2025) | **직접 결합 불가, 부분 매핑만 가능.** | Emo-FilM은 별도 평정자 44명이 50개 항목(discrete emotion과 CPM 성분)을 시간 연속으로 평정 (`datasets_and_resources.md` 출발점 정보; Emo-FilM 담당 감사로 재확인 필요). Horikawa는 비디오당 1개 집계값(선택 비율). 평정 형식(선택 비율 vs 연속 강도), 시간 해상도(클립 vs 초 단위), 자극(무음 클립 vs 소리 있는 영화)이 모두 다르다. 이름이 같은 범주(fear, anger, sadness 등)만 순위나 RSA 수준에서 비교하는 것이 안전. EmoMind 2026이 두 데이터셋을 함께 썼으나 Horikawa는 cross-dataset 평가용으로만 사용 [검색] |
| Spacetop (Jung et al., 2025) | **미확인** | Spacetop의 정서 평정 종류가 확인되어야 판단 가능 |
| NSD (Allen et al., 2022) | **라벨 직접 결합 불가** | NSD는 정지 이미지, 7T이며 기본 정서 라벨 여부는 NSD 감사 결과를 따른다. Horikawa에서 학습한 34 범주 예측기를 NSD 이미지에 적용하면 그것은 AI 추정 라벨이다 |
| Koide-Majima et al. (2020) 데이터 (우리 4개 밖) | 범주 체계 다름(80개 일본어 범주, 초 단위 강도, 소리 있음) | Asanuma 2025 표 1 [2차 본문]. 같은 계열 연구와 비교할 때 참고 |
| 공간 표준화 | 공개 전처리본이 native volume이라 다른 데이터셋과 voxel 수준 결합 불가. raw BIDS와 T1w로 재전처리하거나 HCP360 parcel 수준에서 결합해야 함 | [1차] |
| 뇌 영역 정의 | HCP360 parcellation은 다른 데이터셋에도 적용 가능해 ROI 수준 비교의 공통 기준이 될 수 있음 | [1차] |

---

## 8. Research Opportunities

### 8.1 Cowen & Keltner (2017) Discussion의 세 방향과 Horikawa (2020)의 수행 범위

주의: 아래 세 방향은 `reference/starting_papers.md` 특별 지시의 서술이다. Cowen & Keltner (2017) PNAS 본문(Discussion)은 이번 감사에서 직접 열지 못했다(PMC 전문이 도구에서 비어 있었고 웹 접근 차단). 따라서 세 방향의 원문 표현과 단락 위치는 **미확인**이다.

| 방향 | Horikawa (2020)가 이미 한 것 | 남은 것 |
|---|---|---|
| (1) 새로운 fMRI 모델링과 이 논문의 정서 유발 방법 결합 | 같은 2,181개 자극으로 전뇌 decoding, voxel-wise encoding, 비지도 clustering, UMAP 수행. category가 dimension보다 우월, transmodal 영역 중심, 범주 cluster와 gradient 구조 보고 [본문] | (a) fMRI 참가자 본인 보고와의 연결(데이터에 없음). (b) 반복 제시 기반 noise ceiling. (c) 시간 동역학(짧은 클립 한계). (d) 소리 포함, 다감각(원 저자도 제안). (e) 최신 video/MLLM feature와의 정밀한 분리. (f) 결과의 분석 가정 의존성 검증(Westlin 2025가 반대 결과를 보고해 쟁점이 열려 있음) |
| (2) multidimensional reliability estimation 기법 활용 | 원 논문은 ROI 패턴의 피험자 간 일관성(identification), k-means 27 cluster를 사용했지만, 행동 쪽에서 쓴 방식처럼 뇌 응답에서 "신뢰할 만하게 구분되는 차원 수"를 피험자 간 split-half로 추정하지는 않았다 [본문, 해당 분석 부재 확인] | 부분 수행: Du 2023이 encoding weight의 PCA로 저차원 affective space(상위 4개 PC)를 추정 [2차 본문]. Du et al. 2025 arXiv가 30차원 MLLM embedding 제시 [검색]. 남은 것: 5명 간 신뢰 가능한 공유 차원 수를 cross-subject 방식으로 추정하고 행동 27차원과 대응시키는 분석 |
| (3) higher-order theory of emotional consciousness와 연결 | 수행 안 함. 원 논문은 first-person vs third-person 혼재 가능성만 한계로 언급 [본문] | 전부 남음. 다만 이 데이터는 참가자 보고, 메타인지 측정, 의식 조작이 없어 이 방향을 **직접 검증할 수 없다**. 다른 데이터셋이나 새 실험이 필요 |

### 8.2 원 논문 Discussion과 Limitations의 future direction과 선행 수행 여부

| Future direction (요약) | 위치 | 이후 수행 여부 |
|---|---|---|
| 청각 내용, 개인적으로 의미 있는 자극, 행동 참여 과제 포함 | Discussion 7째 단락 | partially (Emo-FilM 등 audiovisual 데이터는 있으나 같은 34 범주 체계는 아님) |
| 지각된 정서 decoder를 꿈, mind wandering 등 자발적 정서로 일반화 | Discussion 8째 단락 | partially (Afrasiyabi et al. 2024, arXiv:2410.00047: 정서 라벨 텍스트로 유도한 심상 decoding, 같은 비디오로 피험자 3명 추가 [검색]) |
| 더 풍부한 정서 모델로 cross-modal 신경 표상 연구 | Discussion 9째 단락 | partially (Kiyokawa & Hayashi 2024 [2차 본문]: 얼굴, 언어, CLIP 표상과 뇌 RSM 비교) |
| 참가자 개인 변수(문화, 성별, 나이, 성격) 반영 | Limitations 1째 단락 | no (이 데이터로는 불가) |
| 생리 측정 등으로 1인칭 경험과 3인칭 추론 분리 | Limitations 2째 단락 | no (이 데이터로는 불가) |
| 정서가 gaze 패턴에 미치는 영향 모델링 | Limitations 3째 단락 | no |
| 반복 제시 부재로 설명 안 된 체계적 분산 추정 불가 | Discussion 6째 단락 | no |

### 8.3 이 데이터 또는 같은 Cowen & Keltner 자극을 쓴 연구 (상세는 literature_Horikawa.jsonl)

| 연구 | 연도 | 사용 확인 수준 | 핵심 |
|---|---|---|---|
| Du, Fu, Wen, He. iScience 26:107571. [doi:10.1016/j.isci.2023.107571](https://doi.org/10.1016/j.isci.2023.107571) | 2023 | 본문 확인(Key resources에 ds002425, figshare 명시) | voxel-wise encoding, 저차원 affective space, 원본 비디오에서 motion energy 6,555차원 추출(즉 비디오 입수) |
| Fu, Du, Wang, He. IEEE TNNLS 35(7):9026-9040. [doi:10.1109/TNNLS.2022.3217767](https://doi.org/10.1109/TNNLS.2022.3217767) | 2024 (온라인 2022) | abstract만. 두 visually evoked emotion 데이터셋 중 하나가 Horikawa로 추정(제3자 요약의 "MEMO27, 5명, 27 범주") | multi-view multi-label 정서 decoding |
| Kiyokawa, Hayashi. Sci Rep 14:20992. [doi:10.1038/s41598-024-71690-y](https://doi.org/10.1038/s41598-024-71690-y) | 2024 | 본문 확인 | 얼굴, 언어, CLIP 정서 표상 vs 360 영역 뇌 RSM. visio-linguistic 표상이 가장 넓게 일치 |
| Afrasiyabi et al. arXiv:2410.00047 | 2024 | 검색 요약 | 같은 Cowen & Keltner 비디오로 3명 추가 촬영, 정서 라벨 기반 심상 decoding. 추가 데이터 공개 여부 미확인 |
| Shariatpanahi et al. arXiv:2503.13981 | 2025 | 검색 요약. "5명, 2,185 비디오" 서술로 Horikawa 데이터 추정 | controllability 관점 |
| Westlin, Singh, Erdogmus, Stratis, Barrett. arXiv:2507.00320, PMID 41019207 | 2025 | abstract | constructionist 재분석. 원래 매핑 재현 안 됨, 개인 간 변동 큼 |
| Asanuma et al. Sci Rep 15:32175. [doi:10.1038/s41598-025-14961-6](https://doi.org/10.1038/s41598-025-14961-6) | 2025 | 본문 확인 (fMRI 아님, 같은 자극과 평정) | MLLM 정서 추정이 범주 수준 구조와는 일치, 개별 비디오 수준은 제한적 |
| Fu et al. EmoGrowth. ICML 2025, PMLR 267:17746-17763 | 2025 | 공개 코드 설정에 dataset "iScience", 27 class (Horikawa로 추정) | incremental multi-label 정서 decoding |
| Du, Lu, Huang, Sun, Zhou, Qin, He. arXiv:2509.24298 | 2025 | 검색 요약 ("five subjects", 2,180 clips) | MLLM odd-one-out embedding이 인간 평정보다 뇌 정서 네트워크를 더 잘 예측 |
| Mohammed, Gu, Fang. EmoMind. arXiv:2605.16739 | 2026 | 검색 요약 (Horikawa를 cross-dataset 평가에만 사용) | fMRI에서 34차원 정서 벡터 decoding 후 affective caption 생성. TRIBE v2 합성 뇌 대체 시 RSA 크게 하락 |

2026-04 Mendeley 예치 이후 이 데이터를 쓴 연구로 확인된 것은 EmoMind(2026-05)뿐이며, 그마저 사용 데이터 경로(OpenNeuro, figshare, Mendeley 중 무엇인지)는 **미확인**이다. Kragel 연구실 2026 연구(Ma & Kragel, bioRxiv 2025.06.03.657722)는 Emo-FilM을 사용하며 Horikawa 데이터는 쓰지 않은 것으로 검색됨 [검색].

### 8.4 연구 기회 (Stage 2 참고용)

1. **분석 가정 민감도 검증.** 같은 데이터에서 categorical(Horikawa 2020) 결론과 constructionist(Westlin 2025) 결론이 갈린다. 여러 분석 파이프라인(ROI 선택, 정규화, CV 방식)을 체계적으로 바꿔 결론이 어디서 갈리는지 multiverse 방식으로 보는 연구. G1 불필요. 근거: 10.1016/j.isci.2020.101060, arXiv:2507.00320.
2. **피험자 간 신뢰 가능한 정서 차원 수 추정.** 5명 동일 자극, 동일 순서를 이용해 cross-subject split-half 또는 shared response 방식으로 뇌 쪽 정서 공간의 신뢰 가능 차원 수를 추정하고 행동 27차원과 비교. Cowen & Keltner 방향 (2)의 남은 부분. G1 불필요. 근거: 10.1073/pnas.1702247114, 10.1016/j.isci.2023.107571.
3. **정서 vs 시각-의미 feature의 엄밀한 분리.** 최신 video foundation model과 MLLM feature를 nuisance로 넣은 banded ridge, variance partitioning으로 "semantic보다 조금 나은" 기준을 강화. G1 필요. 근거: Horikawa 2020 Results, Du 2023 Limitations, arXiv:2509.24298.
4. **인간 규범 평정과 AI 추정 평정의 뇌 설명력 비교와 그 의미.** MLLM이 비디오별 정서를 추정하면 "AI 추정 정서"와 "타인의 규범 평정" 중 무엇이 뇌를 더 잘 설명하는지, 그리고 그 차이가 sensory grounding 때문인지 검증. AI 라벨은 별도 표기. G1 필요. 근거: 10.1038/s41598-025-14961-6, arXiv:2509.24298.
5. **반복 없는 단일 시행 데이터의 신뢰도 상한 추정 방법.** 내용 중복 15쌍과 피험자 간 상관(inter-subject correlation)을 이용한 대체 noise ceiling 추정. G1 불필요. 근거: Horikawa 2020 Discussion 6째 단락.
6. **In-silico 예측과 실제 fMRI의 정서 표상 차이.** EmoMind가 보인 합성 뇌(TRIBE v2) 대체 시 RSA 하락을 체계적으로 분석해 encoding foundation model이 정서 구분을 놓치는 지점을 찾기. G1 필요. 근거: arXiv:2605.16739.
7. **Cross-dataset 정서 공간 정렬.** Horikawa(무음 클립, 34 범주)와 Emo-FilM(소리 있는 영화, 50 항목)의 정서 공간을 Gromov-Wasserstein 같은 비지도 정렬로 비교해 공유 구조와 데이터셋 특이 구조를 분리. 라벨 직접 결합 불가라는 7절 판정과 일관됨. G1 불필요(라벨, 뇌 수준). 근거: 10.1038/s41598-025-14961-6 (GWOT 방법), arXiv:2605.16739.
8. **Portrayed vs evoked 정서 분리.** MLLM이나 인간 주석으로 "등장인물이 표현한 정서" 라벨을 새로 만들어 기존 evoked 평정과 대비하고, theory-of-mind 영역과의 관계를 시험. 원 논문의 first-person vs third-person 한계에 대응. G1 필요. 근거: Horikawa 2020 Limitations 2째 단락.

---

## 부록 A. 미확인 항목 전체 목록

1. 우리 환경의 데이터 경로, 원본 비디오 보유 여부, 추출해 둔 feature (`datasets_and_resources.md` 1절 비어 있음)
2. Google Form 비디오 요청의 이용 조건(연구 목적 제한, 재배포, 라이선스, 승인 소요 기간), 양식이 개인 수준 평정도 주는지
3. Mendeley 예치본(doi:10.17632/jbk2r73mzh.1)의 파일 목록, 형식, 라이선스, 비디오 포함 여부, 2020년 논문 인용과의 관계
4. figshare 두 레코드의 라이선스
5. 2,196 제시 ID와 Cowen & Keltner 2,185개 라이브러리의 대응, 2,181과 2,185의 차이
6. 같은 원본 영상에서 잘린 클립 존재 여부(movie-level leakage)
7. 비디오당 dimension 평정자 수, 범주별 inter-rater reliability 수치, category 평정 형식(선택 vs 100점 척도 후 이진화) 원문 확인
8. Cowen & Keltner (2017) Discussion 세 방향의 원문 위치와 표현
9. vision 1000차원 feature를 만든 DNN 이름, semantic 73 항목 목록과 주석 절차
10. 공개 전처리본의 표준공간 버전과 연속 time series 존재 여부
11. fMRI 참가자의 국적, 모국어
12. ds002425가 fMRI foundation model 사전학습 데이터에 포함되었는지
13. Afrasiyabi et al. (2024) 추가 3명 데이터의 공개 여부
14. Fu et al. (2024 TNNLS), EmoGrowth (2025), Shariatpanahi et al. (2025)가 Horikawa 데이터를 썼다는 직접 서술 (현재는 추정)
15. 촬영 장소(Kokoro Research Center)와 Transparent Methods의 세부 서술

## 부록 B. 이번 감사에서 실제로 사용한 검증 경로

* PubMed MCP: Horikawa 2020 전문(PMC7191651, Methods는 보충자료라 미포함), Du 2023 전문(PMC10470388), Kiyokawa 2024 전문(PMC11385795), Asanuma 2025 전문(PMC12402258), Cowen & Keltner 2017은 메타데이터와 abstract만(PMC 전문 반환 안 됨), Westlin 2025와 Fu 2024는 메타데이터와 abstract.
* git으로 읽은 공개 저장소 (프로젝트 폴더 밖, 읽기 전용):
  * `/home/user/openneurodatasets/ds002425` (OpenNeuroDatasets/ds002425, commit 3f94b2b). 메타데이터 텍스트 파일만 읽었고 영상 본체는 내려받지 않음
  * `/home/user/kamitanilab/emotionvideoneuralrepresentation` (commit 8fe23a0)
  * `/home/user/kamitanilab/emotionvideoneuralrepresentationpython` (commit 451236c)
  * scratchpad의 KamitaniLab/OpenData, ChangdeDu/EmoGrowth clone
* WebSearch: 그 밖의 항목. 검색 요약만으로 확인한 사실은 본문에 [검색]으로 표시.
* 차단: WebFetch로 pmc.ncbi.nlm.nih.gov, data.mendeley.com 접근 실패(DNS). 이후 다른 웹 페이지 직접 열람은 시도하지 않음.
