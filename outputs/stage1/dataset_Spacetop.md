# Dataset Forensic Audit: Spacetop (Jung et al., 2025)

* 작성: dataset-auditor (Agent 1, Dataset & Metadata Specialist), 기준일 2026-11-12
* 대상 논문: Jung H, ..., Lindquist MA, Wager TD (2025). Spacetop: A multimodal fMRI dataset unifying naturalistic processes with a rich array of experimental tasks. *Scientific Data* 12:1465. [doi:10.1038/s41597-025-05154-x](https://doi.org/10.1038/s41597-025-05154-x), PMID 40846708, PMC12373947
* 원시 데이터: OpenNeuro ds005256 v1.1.0 (2025-03-13), [doi:10.18112/openneuro.ds005256.v1.1.0](https://doi.org/10.18112/openneuro.ds005256.v1.1.0), <https://openneuro.org/datasets/ds005256>
* 전처리 데이터: OpenNeuro ds007070 v1.0.3 (2026-04-06), "fMRIPrep Derivatives for SpaceTop", [doi:10.18112/openneuro.ds007070.v1.0.3](https://doi.org/10.18112/openneuro.ds007070.v1.0.3)
* 우리 환경의 데이터 경로: **미확인** (`reference/datasets_and_resources.md` 1절이 비어 있음)

## 확인 경로와 한계 (먼저 읽을 것)

| 경로 | 무엇을 확인했나 | 상태 |
|---|---|---|
| PubMed MCP로 PMC12373947 전문 열람 | Methods, Data Records, Technical Validation, Usage Notes 본문 | 열람함. 단 **Table과 Figure는 PMC 텍스트에서 누락**(영상 목록 표, 획득 파라미터 표, consort diagram 미열람) |
| OpenNeuro ds005256의 GitHub 미러 <https://github.com/OpenNeuroDatasets/ds005256> (git clone, tag 1.1.0) | 파일 목록 전체, `dataset_description.json`, `participants.tsv`, 모든 `*_events.tsv`, sidecar JSON, `stimuli/` 목록, git-annex 위치 기록 | 직접 확인. 대용량 파일 본체(NIfTI, mp4)는 내려받지 않음 |
| OpenNeuro ds007070의 GitHub 미러 <https://github.com/OpenNeuroDatasets/ds007070> (partial clone) | fMRIPrep 산출물 구조, 실행 스크립트 `code/run` | 직접 확인 |
| 과제 코드 <https://github.com/spatialtopology> (`spacetop-prep`, `task-alignvideos`, `task-social`, `task-faces`, `task-narratives`, `task-fractional`) | 평정 코드, 생리 기록 코드, 자극 출처 README | 직접 확인 |
| `spatialtopology/d_beh` (ds005256의 `sourcedata/d_beh` 서브모듈, 원시 행동 데이터) | | **접근 불가**(인증 요구, 비공개로 추정) |
| WebFetch: doi.org, openneuro.org, nature.com | | **접속 불가**(세션 네트워크 허용 목록 밖). OpenNeuro 웹페이지의 용량, 다운로드 수 등은 직접 확인 못함 |

이하에서 "[repo]"는 ds005256 GitHub 미러를 직접 열어 확인한 사실, "[paper]"는 PMC 전문, "[code]"는 spatialtopology 저장소, "[deriv]"는 ds007070 미러, "[계산]"은 본 감사에서 events.tsv로 직접 계산한 탐색적 수치, "[추정]"은 근거가 간접적인 판단이다.

---

## Gate 판정 요약

| Gate | 판정 | 핵심 근거 |
|---|---|---|
| **G1 원본 자극** | **공개 경로 기준: 공개 다운로드 가능(요청 불필요)**. 우리 환경 보유 여부: **미확인**. 단 alignvideo/shortvideo 영상과 vicarious pain 영상은 제3자 저작물로 보이며 원 출처와 재사용 조건이 데이터셋에 기재되어 있지 않음 | [repo] `stimuli/`에 8개 과제 폴더(1,872개 파일). git-annex 위치 기록상 annex 파일 630개(alignvideo 49, faces 415, shortvideo 21, social 135, narratives 9, tomspunt 1)가 모두 OpenNeuro 공개 S3 원격(`s3-PUBLIC`, bucket openneuro.org)에 존재로 기록됨. 나머지 소형 파일은 git에 직접 포함. [paper] Data Records: "a stimuli/ directory hosts all the stimuli presented in the functional tasks" |
| **G2 fMRI 형식, 전처리** | **raw BIDS + fMRIPrep 25.1.4 파생 데이터 모두 공개(CC0)**. volume(MNI152NLin2009cAsym)과 surface(fsLR 91k CIFTI) 둘 다 있음. 논문이 기술한 fMRIPrep 21.0.2 산출물의 공개 여부는 미확인. GLM beta, denoised timeseries, parcellation timeseries는 없음 | [repo] 117명, BOLD run 4,178개, BIDS 1.9.0. [deriv] ds007070 v1.0.3, fMRIPrep 25.1.4, `--cifti-output 91k --ignore slicetiming --dummy-scans 6`, 117명 4,178 run 모두 `space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz`와 `space-fsLR_den-91k_bold.dtseries.nii` 보유 |
| **G3 라벨 접근, 평정 주체** | **접근 가능(CC0, events.tsv)**. 평정 주체는 **fMRI 참가자 본인**의 trial-wise 사후 평정뿐. 영상에 대한 별도 평정자 규범(normative) 평정, 연속 시간 평정은 데이터셋에 **없음**. alignvideo 평정은 약 **51% 결측** | [repo] `task-alignvideo_events.json`: 영상 후 7개 차원(personal relevance, happy, sad, afraid, disgusted, warm and tender, engaged)을 0~100으로 각 5초 내 평정. [계산] 평정 이벤트 35,896개 중 17,491개만 값 있음 |

### G1 과제별 상세

| 과제 | 자극 내용 | 공개 파일 [repo] | 공개 경로 기준 | 우리 환경 | 저작권, 접근 주의 |
|---|---|---|---|---|---|
| task-alignvideo | 49개 정서 유발 영상, 20 s ~ 5 min 39 s, 총 86분 9초 [paper]. 소리 있음(HED: Visual-presentation, Auditory-presentation) | mp4 49개, 약 7.9 GB(annex key 크기 합) | 공개 다운로드 가능 | 미확인 | 원 제목, 출처 URL, 저작권자 미기재. 파일명은 `content-<약칭>`만 있음(예: harrymetsally, freesolo, planetearth, wanderers, angrygrandpa). 약칭으로 보아 상업 영화, 다큐멘터리, 온라인 영상 발췌로 **추정**. 데이터셋 라이선스 CC0는 제3자 영상 저작권을 해소하지 않으므로, 연구 목적 feature 추출 범위는 기관 확인 필요 |
| task-shortvideo | alignvideo 영상에서 특정 인물을 잘라낸 4.1~6.9 s 클립 [paper] | mp4 21개 | 공개 다운로드 가능 | 미확인 | alignvideo와 동일 |
| task-narratives | 연구실 제작 이야기 8편 x 9 clip(Polti의 36 dramatic situations 기반), 4편 audio, 4편 text [paper; Miao 2026] | mp3 36개, txt 36개(clip별 원문 텍스트 포함) | 공개 다운로드 가능 | 미확인 | 자체 제작으로 저작권 부담이 적을 것으로 [추정] |
| task-faces | animated dynamic faces 1.3~2.1 s, 8 표정(happy, surprise, fear, disgust, anger, sad, pain, pleasure) x 성별 x 인종(EA, WC, African) x 연령 [paper] | mp4 480개(5 model x 96), 실제 사용 288개 [계산] | 공개 다운로드 가능 | 미확인 | 얼굴 생성 도구와 원 출처 미확인([code] README에 Google Drive 링크만 있음) |
| task-social: vicarious | UNBC-McMaster Shoulder Pain Expression Archive의 환자 영상에서 새로 만든 클립, 사전 규준 평정으로 L/M/H 강도 분류 [paper; code] | mp4 72개(파일명 끝 `_L/_M/_H`) | 공개 다운로드 가능 | 미확인 | 원 데이터베이스의 이용 조건 확인 필요(본 감사에서 미확인) |
| task-social: cognitive | Ganis & Kievit (2015) mental rotation 3D 도형, 회전 50/100/150도 [paper] | jpg 384개 | 공개 다운로드 가능 | 미확인 | 원 자극 세트 라이선스 미확인 |
| task-social: cue | 다른 참가자 평정처럼 보이게 만든 high/low cue 이미지(실제는 무작위) | png 336개 + 척도 이미지 3개 | 공개 다운로드 가능 | 미확인 | 기만(deception) 설계 |
| task-social: pain | 열 자극 48/49/50 °C, TSA2(Medoc), 16 mm Peltier, 왼쪽 전완, 5 s plateau, 총 9 s [paper] | 파일 아님. events.tsv에 강도 수준, TTL 4개 시점, 전달 성공 여부 | 해당 없음(물리 자극). 파라미터는 공개 | 해당 없음 | 6,704개 pain trial 모두 `success` [계산] |
| task-fractional | memory clip-art, Spunt why/how 사진, Saxe false belief 텍스트, Posner 도형 | png 348, jpg 67, txt 40 | 공개 다운로드 가능 | 미확인 | Spunt 자극은 논문이 Zenodo 경로를 인용 |

**주의:** 공개 판정은 git-annex 위치 기록(`*.log`에서 `s3-PUBLIC` 원격 status 1)에 근거한다. 실제 mp4 다운로드는 이 세션의 네트워크 제약으로 실행해 보지 못했다.

---

## 1. Verified Dataset Specification

### 1.1 참가자

| 항목 | 값 | 출처 |
|---|---|---|
| 논문 표기 N | 101명, 나이 24.7 +- 5.5세, "69 males, 45 females, 2 others" | [paper] Participants |
| OpenNeuro 실제 폴더 | **117명**(sub-0001 ~ sub-0133 중 117개 ID). `participants.tsv` 117행: F 70, M 45, O 2, 나이 평균 24.2, SD 5.4 [계산] | [repo] |
| 불일치 | 논문 성별 수치 합은 116이고, participants.tsv와 비교하면 남녀가 뒤바뀐 것으로 보임. Yazdanpanah et al. (2026)도 같은 표본을 "68 females, 41 males, 2 others"(111명)로 기술. N=101의 산정 기준은 **미확인**(Table/consort diagram 미열람) | [paper], [repo], [doi:10.1073/pnas.2513856123](https://doi.org/10.1073/pnas.2513856123) |
| 세션 완료 | 4개 세션 모두: 99명, 3개: 3명, 2개: 4명, 1개: 11명 | [계산] |
| 41개 BOLD run 모두 보유 | 61명 | [계산] |
| 모집 | 2020-12 ~ 2022-07, Dartmouth Brain Imaging Center. 건강한 오른손잡이 성인, 만성 통증 없음 | [paper] |
| 윤리 | Dartmouth IRB CPHS STUDY00031937, 공개 공유 동의 | [paper], [repo] `dataset_description.json` |

### 1.2 스캐너와 획득 파라미터

| 항목 | 값 | 출처 |
|---|---|---|
| 스캐너 | 3T Siemens MAGNETOM Prisma, 32채널 head coil | [paper], [repo] JSON `ManufacturersModelName: Prisma`, `ReceiveCoilName: Head_32` |
| BOLD 시퀀스 | CMRR `mbep2d_bold`, TR 0.46 s, TE 27.2 ms, flip 44도, multiband 8, 2.7 mm 등방, 56 slices, FOV 220 mm, PE P>>A | [paper], [repo] `task-*_acq-mb8_bold.json` |
| 행렬 크기 | 논문은 "64 x 64 matrix"로 기술하나 JSON은 `BaseResolution 82`, `AcquisitionMatrixPE 82`. 220/82 = 2.68 mm이므로 **82 x 82가 맞고 논문 표기는 오류로 판단** | [paper] vs [repo] |
| SBRef | run마다 single-band reference 있음(4,122개) | [repo] |
| Field map | AP/PA spin-echo EPI 쌍(1,941개 파일) | [repo] |
| T1w | MPRAGE 0.8 mm 등방, TR 2 s, TI 1 s, flip 8도. ses-01에서만 | [repo] JSON |
| DWI | 96방향 + 6 b0, b 약 500/1000/2000/3000(multi-shell), MB3, 1.7 mm, TR 4.11 s. 116명 | [repo] `.bval`, JSON |
| 시선 추적 | 없음(관련 파일 없음) | [repo] |
| 원 DICOM | 공개 시 삭제(`sourcedata/README`) | [repo] |

### 1.3 세션 구조와 과제별 스캔 시간

TR 0.46 s 기준. run 수와 참가자 수는 [계산], TR 수는 [paper].

| 세션 | 과제(run 수) |
|---|---|
| ses-01 | T1w, DWI, alignvideo(4 run, 14편), social(6 run) |
| ses-02 | alignvideo(4 run, 16편), narratives(4 run), faces(3 run) |
| ses-03 | alignvideo(3 run, 11편), social(6 run), shortvideo(1 run) |
| ses-04 | alignvideo(2 run, 8편), social(6 run), fractional(2 run) |

| 과제 | 1인 run 수 | run당 길이 | 1인 총 스캔(약) | 데이터 있는 참가자 | 전체 run 보유 |
|---|---|---|---|---|---|
| alignvideo | 13 | 영상 구성에 따라 다름 | 영상 86분 9초 + 영상당 평정 약 35 s(49편 x 35 s = 약 29분), 합 약 115분 [추정] | 116 | 87 |
| social | 18(세션당 pain, vicarious, cognitive 각 2) | 872 TR(6분 41초), 12 trial | 약 120분 | 116 | 69 |
| narratives | 4 | 967/1098/1298/1156 TR(7분 25초 ~ 9분 57초) | 약 35분 | 106 | 105 |
| faces | 3 | 914 TR(약 7분), 96 trial | 약 21분 | 106 | 103 |
| shortvideo | 1 | 1616 TR(12분 23초) | 약 12분 | 99 | 99 |
| fractional | 2(4개 하위과제 중 2개 배정) | 1322 TR(10분 8초) | 약 20분 | 100 | 100 |

* 41 run x 6개 과제 합은 약 5.4시간이며 구조 영상을 더하면 논문의 "6 hours"와 대체로 맞는다 [추정].
* fractional 하위과제별 run 수: tomsaxe 51, tomspunt 48, posner 49, memory 52 [계산]. 논문 표기(posner 48, memory 52, tomsaxe 51, tomspunt 47)와 1~2개 차이.
* 논문은 "120 minutes of naturalistic movie data and audio narratives"와 "90 minutes of movie data"를 함께 쓴다. alignvideo 영상 자체는 86분 9초이며, 본 감사의 events 기준 영상별 중앙 길이 합은 86.6분 [계산].

### 1.4 전처리 데이터와 표현 공간

| 항목 | 내용 | 출처 |
|---|---|---|
| 논문 기술 | fMRIPrep 21.0.2(Nipype 1.6.1), FreeSurfer 6.0.1 recon-all, MNI152NLin2009cAsym와 MNI152NLin6Asym, fsaverage 경유 CIFTI 91k, 0.9 mm FD 또는 1.5 표준화 DVARS 기준 outlier 표시 | [paper] |
| 실제 공개 파생 | **ds007070 v1.0.3**, fMRIPrep **25.1.4**, 2026-04 공개, 117명, BOLD 4,178 run | [deriv] `dataset_description.json`, `CHANGES` |
| 실행 옵션 | `--cifti-output 91k --ignore slicetiming --dummy-scans 6` | [deriv] `code/run` |
| func 산출물 | `space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz`(res 표기 없음, BOLD 원 해상도로 추정), `space-fsLR_den-91k_bold.dtseries.nii`, `desc-confounds_timeseries.tsv`, brain mask, boldref, 변환 행렬 | [deriv] |
| anat 산출물 | preproc T1w, dseg, ribbon, MNI2009c/MNI6 변환, FreeSurfer 기반 GIFTI surface(white, pial, midthickness, fsLR 32k, sphere, sulc, thickness) | [deriv] |
| 차이 | 논문이 기술한 21.0.2 산출물과 공개 25.1.4 산출물은 버전이 다름. 논문 결과 재현 시 주의 | [paper] vs [deriv] |
| 없는 것 | denoised timeseries, GLM beta/contrast, parcellated timeseries, functional alignment 결과 | [deriv] |
| 품질 | 과제별 median FD < 0.2 mm, tSNR 지도 균질 | [paper] Technical Validation |

### 1.5 라이선스와 사용 조건

* ds005256, ds007070 모두 `License: CC0` [repo], [deriv]. 별도 DUA 없음. 인용 요청(`HowToAcknowledge`)만 있음.
* 공개 파일에는 식별 정보를 제거했고 날짜는 1918년대로 이동되어 있음(`scans.tsv`의 acq_time) [repo].
* 데이터셋 전체 용량은 WebSearch 요약에서 "약 2.03 TB, 23,509 files"로 보였으나 OpenNeuro 페이지를 직접 열지 못해 **미확인**.
* `spacetop-prep/spacetop_prep/nda/`에 NIMH Data Archive 제출용 스크립트가 있음 [code]. NDA 컬렉션 존재와 그 내용(생리, 설문 포함 여부)은 **미확인**.

---

## 2. Complete Metadata & Annotation Inventory

### 2.1 정서 정보의 출처 구분 (Safeguard)

| 구분 | Spacetop에 있는가 | 구체 내용 |
|---|---|---|
| **실제 관찰된 정서**(행동, 생리 관찰) | 기록은 했으나 **공개 파일 없음** | 피부전도(EDA)와 PPG를 BIOPAC으로 fMRI와 동시 기록 [paper; code]. ds005256 v1.1.0과 ds007070에 `_physio` 파일 0개 [repo; deriv]. 참가자 얼굴 영상, 시선 추적 없음 |
| **fMRI 참가자 본인 보고** | 있음 | alignvideo 영상별 7차원 사후 평정, narratives clip별 good-bad 감정과 다음 전개 기대, social 기대/결과 평정(통증, vicarious pain, 인지 노력). 모두 trial 단위 사후 평정이며 시청 중 연속 평정은 없음 |
| **참가자의 타인 지각/추론 판단** | 있음 | faces 표정 강도(타인 표정의 지각), shortvideo 인물에 대한 유사성, 호감, mentalizing 질문("Was the character feeling angry?" 등 7종). 본인 정서가 아니라 **타인에게 귀속한 정서**임 |
| **별도 평정자의 규범적 평정** | 데이터셋 안에는 **없음** | vicarious 영상의 L/M/H 강도는 UNBC-McMaster의 사전 규준(환자 자기 보고, 관찰자 추정)으로 정함 [paper]. tomspunt `normative_response`는 정서가 아닌 정답 규준. 외부: Miao et al. (2026)이 narratives에 대해 별도 온라인 평정자 231명의 연속 사회적 상호작용/ToM 평정을 수집(정서 아님, 공개 여부 미확인) |
| **자극에 표현된 정서** | 일부 | faces의 8개 표정 범주(설계상 라벨), vicarious 환자의 통증 표정 강도, narratives의 Polti 상황 라벨(예: "Necessity of sacrificing loved ones")과 장소 맥락. alignvideo 영상에는 범주 라벨이나 내용 라벨이 **없음**(약칭 파일명만) |
| **AI가 추정한 정서** | 없음 | 데이터셋에 모델 기반 annotation 없음 |

### 2.2 과제별 라벨 상세

#### task-alignvideo (핵심 정서 과제)

| 항목 | 내용 | 출처 |
|---|---|---|
| 평정 주체 | fMRI 참가자 본인 | [paper], [repo] |
| 문항 | "In relation to the previous video, how do you feel?" + 7개 키워드: personal relevance, happy, sad, afraid, disgusted, warm and tender, engaged. 순서 고정 | [code] README, [paper] |
| 척도 | 좌 "Barely at all" ~ 우 "Strongest imaginable" 선형 삼각형 척도, 0~100. MR trackball | [repo] `task-alignvideo_events.json` |
| 시간 해상도 | **영상당 1회(영상 종료 후)**. 7개 평정 각 5초, 영상 후 약 35초 평정 구간 | [repo] events onset 간격 약 5.03 s |
| 기록 방식 | 매 문항 커서를 왼쪽 끝으로 초기화(`SetMouse(lb)`), 4.5초 안에 **클릭해야만** 값 저장. 클릭이 없으면 rating=0, RT=0으로 저장되고 BIDS 변환 시 n/a 처리. 커서 궤적은 공개 events에 없음 | [code] `scripts/rating_scale.m`, `spacetop_prep/events/bidsify_alignvideos_ENH.py` |
| 결측 | 평정 이벤트 35,896개 중 17,491개(48.7%)만 값 있음. 참가자별 완료율 중앙값 0.47, 하위 25% 0.05. 세션별 완료율 0.44/0.48/0.52/0.56. 세션 단위 전부 결측: ses-01 26명, ses-02 23명, ses-03 28명, ses-04 28명. 값이 하나라도 있는 참가자 109명 | [계산] |
| 결측 무작위성 점검 | 부분 결측 참가자에서 결측된 (영상, 차원)의 집단 평균 강도 23.2 vs 응답된 것 22.6. 강도에 따른 선택적 결측의 강한 증거는 없음(탐색적) | [계산] |
| 분포 | 평균(중앙값): afraid 16.6(4.7), disgusted 9.9(1.9), sad 15.6(5.5), warm 22.5(8.8), happy 28.0(20.3), relevance 22.4(14.0), engaged 44.8(45.0). 부정 정서에 강한 바닥 효과 | [계산] |
| 신뢰도 | 영상 수준 집단 평균의 split-half(Spearman-Brown, 200회 무작위 분할): afraid 0.99, warm 0.98, sad 0.98, happy 0.98, disgusted 0.97, engaged 0.94, relevance 0.94. 개인 대 나머지 집단 평균 상관 중앙값: afraid 0.77, sad 0.74, warm 0.75, happy 0.70, disgusted 0.70, engaged 0.51, relevance 0.46. (영상-차원당 응답자 중앙값 51명) | [계산] |
| 표본 단위 | 고유 영상 49개(또는 48개, 아래 tornado 참고). 정서 라벨의 독립 표본 수가 영상 수로 제한됨 | [paper], [repo] |
| 반복 | 논문은 "Each video was played once, with no repetitions". 그러나 `content-tornado`가 ses-02와 ses-04에 각각 있음(약 27 s, 파일 해시 다름). arXiv:2606.09770 검색 요약은 "48 unique video identities"로 기술. 동일 영상의 재인코딩인지 **미확인** | [paper], [repo], WebSearch |
| 영상 순서 | 모든 참가자에게 동일 순서(functional alignment 목적) | [paper] |

**2차 문헌의 오기 주의:** Sadil et al. (2026, [doi:10.64898/2026.07.23.739855](https://doi.org/10.64898/2026.07.23.739855))은 alignvideo를 "continuous affective ratings"로 기술하지만, 원 데이터와 코드는 영상 후 7회 사후 평정이다.

#### task-social (통증, vicarious pain, 인지 노력)

| 항목 | 내용 |
|---|---|
| 설계 | 2 cue(high/low, 무작위 기만 cue) x 3 강도(low/med/high). trial: cue 1 s, 기대 평정 4 s, 자극 5 s(통증은 9 s 중 5 s plateau), 결과 평정 4 s. run당 12 trial [paper; repo] |
| 평정 주체 | 참가자 본인. 기대(expectation)와 결과(outcome) 모두 |
| 척도 | 반원형 gLMS, `rating_value`는 0~180도. 라벨 No sensation ~ Strongest sensation of any kind [repo] |
| 결측 | 클릭 기준 응답률 0.86~0.90, 마우스 궤적으로 채운 `rating_value_fillna` 기준 0.96~0.99 [계산] |
| 참가자, trial | 각 run_type 115명. pain 6,704 trial, vicarious 7,440, cognitive 7,455 [계산] |
| 추가 열 | 통증 TTL 4개 시점, 전달 성공 여부, cognitive 정답/반응/정확도 [repo] |

#### task-narratives

| 항목 | 내용 |
|---|---|
| 자극 | 이야기 8편 x 9 clip, 각 이야기 1분 36초 ~ 3분 29초. 상황(situation), 장소(context: park, hospital, prison, town, city, beach, forest, swamp), modality(Audio/Text) 라벨 [paper; repo] |
| 평정 | clip 후 "feeling"(지금 느낌)과 "expectation"(다음 전개가 좋을지 나쁠지). 2차원 척도: 좌상단 Bad, 우상단 Good, 중앙에서 멀수록 강도. `response_x`, `response_y` 픽셀 좌표 [repo] |
| 주체, 해상도 | 참가자 본인, clip 단위 |
| 결측 | 응답률 0.98(클릭 없으면 궤적 마지막 위치로 대체) [계산; repo] |
| 외부 연속 평정 | Miao et al. (2026): 온라인 별도 표본 231명이 같은 이야기에 대해 사회적 상호작용과 ToM 관여를 moment-by-moment 연속 평정, 230 ms로 리샘플. 정서 평정은 아님 [doi:10.1038/s41467-026-71151-2](https://doi.org/10.1038/s41467-026-71151-2) |

#### task-faces

| 항목 | 내용 |
|---|---|
| 자극 라벨 | expression 8종, sex, race, age(설계상 라벨, 자극에 표현된 정서) [repo] |
| 평정 | run마다 한 차원: 나이(young-old), 성별(male-female), 표정 강도(neutral-strongest imaginable). 0~1 선형, 1.875 s [paper; repo] |
| 사용량 | 참가자당 288 trial(표정당 36), 그중 표정 강도 평정은 1개 run(96 trial) [계산] |
| 결측 | 응답률 0.96 [계산] |

#### task-shortvideo

| 항목 | 내용 |
|---|---|
| 평정 | 블록별 likeability, similarity, mentalizing. mentalizing 문항 7종: angry, calm, danger, enjoy, heights, remember, tired [repo] |
| 척도 | 반원형 gLMS 변형, `response_angle` 0~180 [repo] |
| 결측 | 응답률 0.99, 99명 [계산] |
| 특성 | alignvideo에서 본 인물을 수일 뒤 다시 제시(기억 재활성화, 반복 자극) [paper] |

#### task-fractional

정서 평정 없음. 정확도, 반응 시간, old/new, why/how, false belief/photo 응답 [repo].

### 2.3 생리 데이터

| 항목 | 내용 | 출처 |
|---|---|---|
| 종류 | 피부전도(EDA), photoplethysmography(PPG), MR trigger 채널 | [paper], [code] `c01_bidsifysort.py`의 `recording-ppg-eda-trigger` |
| 장비, 샘플링 | BIOPAC AcqKnowledge(.acq), 2000 Hz(코드 기본값과 README 기준) | [code] `physio/README.md`, `sandbox/qc01_outlierdetection.py` |
| 포함 과제 | 코드에 BIOPAC 제어가 있는 과제: alignvideo, social, faces. narratives, fractional 코드에는 BIOPAC 참조 없음 | [code] (코드 기준 추정) |
| 호흡 | 호흡 벨트 기록은 논문, 코드에서 확인되지 않음 | [paper], [code] |
| 공개 여부 | **ds005256 v1.1.0, ds007070 어디에도 없음**. 공개 경로 **미확인**(NDA 또는 저자 요청 가능성은 미확인) | [repo], [deriv] |

### 2.4 설문

참가 전 집에서 심리사회 설문 배터리를 수행(REDCap) [paper; code `redcap/`]. ds005256에는 `phenotype/` 폴더가 없고 `participants.tsv`는 나이, 성별, group만 있음 [repo]. 설문 데이터 공개 경로 **미확인**.

---

## 3. Available vs Missing Information

| 정보 | 상태 | 비고 |
|---|---|---|
| raw BOLD, SBRef, fmap, T1w, DWI | 있음(공개) | ds005256 |
| fMRIPrep volume + CIFTI | 있음(공개) | ds007070, fMRIPrep 25.1.4 |
| 논문 기술 fMRIPrep 21.0.2 산출물 | 미확인 | |
| events.tsv(onset, duration, 평정, 자극 파일) | 있음(공개) | HED 태그 포함 |
| 원본 자극 파일 | 있음(공개) | 8개 과제 폴더 |
| alignvideo 영상 원 제목, 출처, 저작권 | **없음/미확인** | 논문 Table 미열람 |
| alignvideo 영상 내용 라벨(장면, 객체, 자막, 대사) | 없음 | 새로 만들어야 함 |
| alignvideo 연속 정서 평정 | 없음 | 참가자, 별도 평정자 모두 없음 |
| alignvideo 별도 평정자 규범 평정 | 없음 | |
| alignvideo 결측 평정의 원시 커서 위치 | 없음 | 코드상 저장 안 됨, d_beh 비공개 |
| narratives 텍스트 원문 | 있음 | txt 36개, mp3 36개 |
| narratives 별도 평정자 연속 평정(사회/ToM) | 외부 논문에 존재, 공개 여부 미확인 | Miao et al. 2026 |
| faces 표정 범주, 인구통계 라벨 | 있음 | 설계 라벨 |
| social 통증 강도, cue, 기대/결과 평정 | 있음 | |
| 생리(EDA, PPG) | **공개 파일 없음** | |
| 호흡, 시선 추적 | 없음 | |
| 설문(성격, 정서 특성 등) | 공개 파일 없음 | |
| 원시 행동 로그(d_beh) | 비공개(접근 불가) | |
| 참가자 N=101 산정 기준 | 미확인 | 폴더는 117명 |

---

## 4. Potential Modeling Tasks

| 과제 유형 | 가능 여부와 조건 |
|---|---|
| Vision decoding | 영상 49편(약 86분, 같은 영상 1회 시청)과 faces 288개로 가능. 반복 시청이 없어 개인 내 noise ceiling을 반복 기반으로 추정할 수 없고, 대신 참가자 간 ISC 기반 ceiling을 써야 함. NSD식 이미지 재구성에는 자극 수와 반복이 부족 |
| Emotion decoding | 정서 라벨은 **영상 단위**(참가자당 최대 49개 표본, 결측 고려 시 더 적음). time-resolved 정서 decoding에는 라벨이 없음. faces 8범주 표정(지각) decoding과 social의 통증 강도 decoding은 trial 수가 충분 |
| Semantic decoding | 영상, 이야기 텍스트로 자막/캡션/LLM embedding을 생성해 가능. narratives는 원문 텍스트가 있어 단어/문장 수준 정렬 가능(audio onset은 clip 단위로만 제공) |
| Encoding | TR 0.46 s의 고시간해상도와 영상 원본이 있어 frame/audio feature 기반 voxel/vertex-wise encoding 가능. fsLR 91k CIFTI 제공 |
| Multimodal alignment | alignvideo는 소리 있음. 비디오, 오디오, 대사(전사 필요), 참가자 평정, 뇌 반응을 같은 시간축에 정렬 가능 |
| Brain Foundation Model adaptation | 117명 x 최대 41 run, 4,178 run의 표준 공간 데이터. 정서 평정과 통증 평정을 downstream 라벨로 쓸 수 있음 |
| Temporal representation | 영상 연속 신경 반응은 있으나 정서 라벨은 영상 끝 1회. narratives의 situation/context/narrative 3단계 시간 구조, shortvideo의 수일 후 재노출 |
| Generative modeling | 원본 영상으로 counterfactual 편집(소리 제거, 장면 대체) 자극 생성 후 in-silico 예측 가능. 실제 fMRI 검증은 새 수집 필요 |
| Cross-subject transfer | 모든 참가자 동일 영상, 동일 순서로 functional alignment에 적합(데이터셋의 설계 목적) |
| Cross-dataset transfer | 아래 7절 참고. 라벨 정의가 다른 데이터셋과 직접 호환되지 않음 |
| 추가 AI-generated annotation | 가능성: 공개 영상, 오디오, 이야기 텍스트에 VLM/ALM/LLM으로 연속 정서, appraisal, 장면 라벨 생성. **타당성 검증 근거**: 참가자 본인 영상별 7차원 평정(영상-차원당 약 51명, 집단 평균 split-half 0.94~0.99 [계산])을 외부 기준으로 쓸 수 있음. 단 영상 단위 49개 점으로만 검증되고, 모델이 추정하는 것은 "자극에 표현된/유발될 것으로 예상되는 정서"이지 참가자 경험이 아님. 유명 영화 발췌가 사전학습 데이터에 포함됐을 가능성(contamination) [추정] |

---

## 5. Unique Advantages

1. **같은 참가자 안에서 경험 정서, 타인 정서 지각, 통증을 함께 측정.** alignvideo(본인 정서), faces(타인 표정 강도), shortvideo(인물 mental state 귀속), social(통증 경험과 기대)이 같은 100여 명에게 있다. 경험 정서 vs 지각/귀속 정서의 신경 표상을 개인 내에서 비교할 수 있는 드문 구조다.
2. **통증이라는 생리적으로 통제된 정동 자극.** 48/49/50 °C 열 자극과 cue 조작으로 기대, 예측오차, 지각을 분리할 수 있고, vicarious pain과 인지 노력이 같은 설계로 대조군 역할을 한다 [doi:10.1073/pnas.2513856123](https://doi.org/10.1073/pnas.2513856123).
3. **자극 원본 공개.** 영상, 오디오, 텍스트, 얼굴 클립이 모두 공개되어 AI feature 추출이 바로 가능하다(G1).
4. **빠른 TR(0.46 s)과 surface 데이터.** CIFTI fsLR 91k까지 공개되어 HCP 계열 surface 분석과 바로 연결된다.
5. **functional alignment 설계.** 모든 참가자가 같은 순서로 약 86분 영상을 본다.
6. **소리 있는 영상.** 무음 자극 데이터셋(Horikawa, 출발점 정보 기준)과 달리 음악, 대사가 포함되어 청각, 언어 정서 질문에 쓸 수 있다.
7. **CC0, DUA 없음.** 데이터 접근 장벽이 낮다.

---

## 6. Methodological Limitations

1. **정서 라벨의 시간 해상도가 영상 단위다.** 시청 중 연속 평정이 없으므로 영상 내 정서 변화와 BOLD를 직접 대응시킬 수 없다. 영상 길이가 20 s ~ 5분 39초로 달라 "영상 전체에 대한 사후 평정"이 영상 내 어느 순간을 반영하는지 알 수 없다(peak-end 등 회상 편향 가능).
2. **평정 구간이 영상 직후에 붙어 있다.** 영상 종료 직후 약 35초 평정 구간의 운동, 의사결정 활동이 영상 끝부분의 지연된 HRF와 겹친다. 영상 수준 정서 decoding에서 평정 행위 자체가 혼입될 수 있다.
3. **alignvideo 평정 결측 약 51%.** 클릭해야만 저장되는 코드 구조 때문이며 원시 커서 위치는 공개 데이터에 없다. 결측이 참가자/세션 단위로 몰려 있어(세션 전체 결측 23~28명) 개인 수준 분석 가능 인원이 줄어든다. 강도에 따른 선택적 결측의 강한 증거는 탐색 분석에서 보이지 않았다.
4. **정서 차원이 7개뿐이고 그중 2개(personal relevance, engaged)는 정서 범주가 아니다.** valence, arousal을 명시적으로 묻지 않았다. 부정 정서(afraid, disgusted, sad)는 바닥 효과가 크다.
5. **라벨의 독립 표본이 49(또는 48)개 영상이다.** visual-semantic-affective feature collinearity를 49개 점으로 분리하기 어렵고, 영상 단위 cross-validation에서 stimulus-level leakage(같은 영상의 TR이 train/test에 섞임)를 막아야 한다.
6. **영상 순서가 모든 참가자에게 같다.** 영상 내용과 세션/run 위치, 피로, 시간 효과가 교란된다. 세션 간 1주 간격이라 세션 효과도 섞인다.
7. **반복 자극.** alignvideo는 원칙적으로 1회 시청이나 tornado 중복 가능성이 있고, shortvideo는 alignvideo 영상을 다시 보여준다(repeated stimulus confound, 기억 효과).
8. **생리 데이터 미공개, 호흡과 시선 미기록.** 자율신경 지표를 정서의 관찰 증거로 쓰려면 별도 입수가 필요하다. TR 0.46 s에서 호흡성 pseudo-motion이 FD를 부풀린다는 보고가 있다 [doi:10.64898/2026.07.23.739855](https://doi.org/10.64898/2026.07.23.739855). 시선 차이로 인한 시각 입력 혼입을 통제할 수 없다.
9. **MB8, slice timing 미보정.** 공개 파생은 `--ignore slicetiming`이다. 고가속 multiband의 volume당 SNR 저하가 있다.
10. **참가자 수 표기 불일치.** 논문 N=101, 폴더 117명, 전체 run 보유 61명. 분석 표본 정의를 직접 해야 한다.
11. **자극 저작권 미기재.** 영상의 원 출처와 라이선스가 없어 파생물(프레임, 캡션) 재배포에 제약이 있을 수 있다.
12. **사전학습 오염.** 유명 영화, 다큐멘터리 발췌로 보이는 영상은 대형 비디오/언어 모델의 학습 데이터에 포함됐을 수 있다 [추정].
13. **기만 cue.** social의 cue는 무작위인데 다른 참가자 평정이라고 제시됐다. 해석 시 설계 의도를 반영해야 한다.

---

## 7. Cross-dataset Compatibility notes

다른 데이터셋의 사양은 `reference/datasets_and_resources.md` 출발점 정보이며 각 담당 에이전트가 확인할 대상이다.

| 쌍 | 라벨 직접 결합 | 근거와 조건 |
|---|---|---|
| Spacetop vs Horikawa (2020) | **불가(이름 수준 부분 대응만 가능)** | Horikawa 라벨은 Cowen & Keltner 별도 평정자의 규범 평정(34 범주, 14 차원), Spacetop은 fMRI 참가자 본인의 7차원 사후 평정. 평정 주체, 척도, 문항이 다르다. happy/sad/afraid/disgusted는 범주 이름이 겹치지만 측정 대상(자극 규범 vs 개인 경험)이 다르다. Horikawa는 무음(출발점 정보), Spacetop은 소리 있음. 결합하려면 공통 AI feature 공간 또는 Spacetop 영상에 대한 Cowen & Keltner식 규범 평정 신규 수집이 필요 |
| Spacetop vs Emo-FilM | **불가(변환 필요)** | Emo-FilM은 별도 평정자 44명의 50개 항목 연속 평정(출발점 정보), Spacetop은 참가자 본인의 영상당 1회 7개 항목. 시간 해상도(연속 vs 영상 단위)와 주체가 다르다. Emo-FilM 연속 평정을 영상 단위로 집계하면 discrete emotion 일부 항목과 이름 수준 비교는 가능. 두 데이터셋 모두 생리 기록이 있으나 Spacetop 생리는 미공개 |
| Spacetop vs NSD | **해당 없음(NSD 정서 라벨 없음, 출발점 정보)** | 정적 이미지 7T vs 영상 3T. 공통 AI feature(CLIP 등) 공간을 통한 encoding 전이만 가능 |
| 획득 호환성 | 부분적 | Spacetop은 3T, TR 0.46 s, 2.7 mm, fsLR 91k CIFTI 제공. 다른 데이터셋과 결합 시 surface 공간(fsLR) 정렬과 TR 리샘플링, HRF 차이 처리가 필요 |
| 데이터셋 내 과제 간 | 가능 | 같은 참가자, 같은 세션 체계, 같은 획득 파라미터. alignvideo로 학습한 alignment를 faces, social, narratives에 적용 가능 |

---

## 8. Research Opportunities

각 항목은 Stage 2 탐색을 위한 후보이며 아직 검증된 결론이 아니다. 기존 프로젝트와 겹치면 `overlap:`으로 표시한다.

1. **경험 정서 vs 지각/귀속 정서의 공유 표상.** alignvideo(본인 경험), faces(타인 표정 강도), shortvideo mentalizing(인물 정서 귀속)을 functional alignment 후 같은 공간에서 비교. 필요: alignvideo 결측을 고려한 표본 정의. 주의: 라벨 출처가 서로 다름을 분석 단위로 유지.
2. **통증 기대와 정서의 공통 계산.** social의 cue 기반 기대, 예측오차, confirmation-biased learning [doi:10.1073/pnas.2513856123](https://doi.org/10.1073/pnas.2513856123)을 fMRI로 확장하고, 같은 참가자의 영상 정서 평정 개인차와 연결. 행동 모델은 이미 있으나 신경 분석은 미발견.
3. **AI 생성 연속 정서 annotation의 외부 타당화.** 공개 영상/오디오에 VLM, ALM으로 시간 연속 정서, appraisal 라벨을 만들고, 참가자 영상별 7차원 평정(집단 평균 신뢰도 0.94~0.99)으로 영상 단위 타당화한 뒤 time-resolved encoding에 사용. 반드시 "AI 추정 정서"로 표기. overlap: Emo-FilM 연구(사전학습 멀티모달 뇌 인코딩으로 영화 정서 맥락 분석하는 계획과 방법 일부 겹침), overlap: EmoBrain(V-JEPA2 feature 사용 가능성).
4. **개인 고유 정서 반응(idiosyncrasy).** 개인 대 집단 평정 상관이 0.46~0.77로 개인차가 크다 [계산]. hyperalignment 후 남는 개인 특이 신경 반응이 개인의 평정 편차를 예측하는지 검증. 필요: 영상 수준 cross-validation으로 leakage 차단.
5. **이야기의 다중 시간척도 정서.** narratives의 situation/context/narrative 위계와 clip별 good-bad 평정, 원문 텍스트의 LLM surprisal/sentiment, Miao et al. (2026)의 별도 평정자 연속 ToM 평정을 결합해 정서 개념과 시각 심상(V3/V4, ITC 활성의 해석)을 분리 [doi:10.1038/s41467-026-71151-2](https://doi.org/10.1038/s41467-026-71151-2).
6. **소리의 정서 기여.** alignvideo는 소리 있는 영상이므로 오디오 feature와 비디오 feature의 고유 설명량을 variance partitioning으로 분리. 무음 데이터셋(Horikawa)과 대비하는 cross-dataset 질문의 한 축.
7. **Brain Foundation Model latent의 정서 정보.** 4,178개 표준 공간 run으로 BFM을 적응시키고, latent가 시각-의미 feature를 통제한 뒤에도 영상 정서 평정, 통증 평정을 설명하는지 검증. 공개 fMRI foundation model 사전학습에 ds005256이 이미 포함됐는지는 **미확인**(데이터 오염 점검 필요).
8. **정서 에피소드의 재노출과 기억.** shortvideo가 수일 뒤 alignvideo 인물 장면을 다시 보여주므로, 처음 시청 시 정서 강도가 재노출 시 신경 재활성과 인물 판단(호감, 유사성)을 예측하는지 검증.
9. **(조건부) 자율신경 지표 결합.** EDA/PPG를 입수할 수 있으면 "실제 관찰된 정서 생리"와 자기 보고, 뇌 반응의 3자 관계를 분석. 현재 공개 경로 미확인.

### 부록 A. Spacetop을 사용한 2024~2026 연구 (상세는 literature_Spacetop.jsonl)

| 연구 | 사용 과제 | 확인 | 본문 |
|---|---|---|---|
| Jung et al. 2025, Sci Data [doi:10.1038/s41597-025-05154-x](https://doi.org/10.1038/s41597-025-05154-x) (preprint 2024, [doi:10.1101/2024.06.21.599974](https://doi.org/10.1101/2024.06.21.599974)) | 데이터 기술 | PubMed | 출판본 전문 |
| Miao et al. 2026, Nat Commun [doi:10.1038/s41467-026-71151-2](https://doi.org/10.1038/s41467-026-71151-2) | narratives(fMRI 90명) + 별도 온라인 평정 | PubMed | 전문 |
| Yazdanpanah et al. 2026, PNAS [doi:10.1073/pnas.2513856123](https://doi.org/10.1073/pnas.2513856123) | social 행동 데이터(Spacetop으로 추정, 본문 텍스트에 이름 미확인) | PubMed | 전문 |
| Sadil et al. 2026, bioRxiv [doi:10.64898/2026.07.23.739855](https://doi.org/10.64898/2026.07.23.739855) | 전 과제 head motion | PubMed | 전문 |
| AlKhamissi et al. 2026, arXiv:2606.09770 (Topo-Omni) | alignvideo 83명(검색 요약 기준) | **미검증**(WebSearch만) | 미열람 |

검색했으나 Spacetop 사용이 확인되지 않아 제외: Jung et al. 2026 PNAS "Action features dominate cortical representation during natural vision"(1시간 자연 다큐멘터리, 본문 미열람), Jang et al. 2026 bioRxiv BLA 연구(Emo-FilM의 Chatter 사용), Thieu et al. 2026 Cell Rep(자체 영상), Sun et al. 2025/2026 bioRxiv 상상 통증(N=9 별도 수집). 외부 연구실의 Spacetop 기반 정서 분석 논문은 검색 범위에서 찾지 못했다.

### 부록 B. 미확인 항목

1. 우리 환경의 Spacetop 데이터 경로와 자극 보유 여부
2. alignvideo 49편의 원 제목, 출처, 저작권자, 재사용 조건(논문 Table 미열람)
3. `content-tornado` 두 파일이 같은 영상인지(고유 영상 49 vs 48)
4. faces 자극의 생성 도구와 출처, UNBC-McMaster 및 Ganis & Kievit 자극의 재배포 조건
5. 생리(EDA, PPG) 데이터의 공개 경로, 생리 기록 과제의 확정 목록
6. 설문 데이터의 공개 경로, NDA 컬렉션 존재 여부
7. 논문 N=101의 산정 기준
8. 논문이 기술한 fMRIPrep 21.0.2 산출물의 공개 여부
9. Miao et al. (2026) 별도 평정자 연속 평정 데이터의 공개 여부
10. OpenNeuro 페이지의 데이터 용량, 다운로드 경로 실제 작동(네트워크 제약으로 미실행)
11. arXiv:2606.09770 본문 내용, 공개 fMRI foundation model 사전학습 데이터에 ds005256 포함 여부
