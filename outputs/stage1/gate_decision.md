# Stage 1 Gate 판정

* 작성: Coordinator
* 기준일: 2026-11-12
* 근거: `outputs/stage1/dataset_*.md` 4개, `outputs/stage1/dataset_intelligence_report.md`, `outputs/agents/adversarial-reviewer/stage1_audit.md`
* Gate 정의: `reference/datasets_and_resources.md` 3절 (G1 원본 자극 접근, G2 fMRI 형식과 전처리 수준, G3 라벨 접근과 평정 주체)
* 모든 판정은 **공개 경로 기준**이다. 우리 환경의 보유 여부는 `reference/datasets_and_resources.md` 1절이 비어 있어 네 데이터셋 모두 **미확인**이다.

---

## 1. 데이터셋별 판정

### 1.1 Horikawa et al. (2020)

| Gate | 판정 | 근거 |
|---|---|---|
| G1 | **요청 필요** | 원본 비디오는 OpenNeuro ds002425, figshare, KamitaniLab GitHub 어디에도 없다. 데이터 제공자의 OpenNeuro README와 GitHub README가 Cowen 연구실 Google Form(goo.gl/forms/XErJw9sBeyuOyp5Q2)으로 요청하라고 안내한다 [1차]. Du et al. (2023)의 Key resources table도 같은 경로를 적었고, 2023~2025년 여러 독립 연구진이 원본 비디오에서 feature를 뽑았으므로 요청 경로는 작동해 온 것으로 보인다(간접 증거). 양식의 이용 조건은 미확인. Mendeley 예치본(doi:10.17632/jbk2r73mzh.1)에 비디오가 들어 있는지도 미확인 |
| G2 | **사용 가능** | Raw BIDS(CC0), 5명 x 8 session x 61 run, TR 2 s, 2 mm, MB4. 전처리본은 fMRIPrep 기반 native volume을 비디오 블록당 1 sample로 평균한 HDF5, HCP360과 피질하 ROI 포함 [1차]. 표준공간 전처리본과 연속 시계열 공개 여부는 미확인 |
| G3 | **공개, 평정 주체는 별도 평정자** | 34 category 선택 비율과 14 dimension 평균이 figshare features에 있다 [1차]. 평정자는 Cowen & Keltner (2017)의 MTurk 표본이며 fMRI 참가자 본인 보고는 없다 [본문: Horikawa 2020 Limitations]. 평정자 개인 수준 자료는 비공개 |

### 1.2 Emo-FilM (Morgenroth et al., 2025)

| Gate | 판정 | 근거 |
|---|---|---|
| G1 | **요청 필요 (조건부 재구성 가능)** | ds004892, ds004872 전체 파일 목록에 영상이 없다 [1차]. 원 출처는 LIRIS-ACCEDE의 Creative Commons 단편영화이고, 연구에 쓴 판본은 앞뒤 크레딧을 잘라낸 편집본이다 [본문]. 원본을 받아 절단 지점을 재현하거나 저자에게 편집본을 요청해야 한다. 영화별 CC 조항(NC, ND 등)은 미확인 |
| G2 | **사용 가능** | BIDS raw(CC0) + FSL FEAT volume 전처리본(native, subject, MNI; 6 mm smoothing, WM/CSF/motion 회귀 적용). TR 1.3 s, 2.5 mm. 30명 x 15 런 = 450 런 [1차]. fMRIPrep, surface 산출물 없음 |
| G3 | **공개 (CC0), 평정 주체는 별도 평정자** | 44명의 50개 항목 1 Hz 연속 평정과 평정자별 원자료 [1차, 본문]. fMRI 참가자 본인 자료는 사후 클립 평정(영화당 5항목, 영화 길이의 약 20%)과 영화별 3문항, 질문지 |

### 1.3 Spacetop (Jung et al., 2025)

| Gate | 판정 | 근거 |
|---|---|---|
| G1 | **공개 다운로드 가능 (저작권 확인 필요)** | ds005256 v1.1.0 `stimuli/`에 8개 과제 자극이 있고 git-annex 기록상 대용량 파일 630개가 OpenNeuro 공개 S3에 있다 [1차]. 실제 다운로드는 네트워크 제약으로 실행하지 못했다. alignvideo, shortvideo, vicarious 통증 영상은 제3자 저작물로 보이며 원 출처와 재사용 조건이 데이터셋에 기재되어 있지 않다 |
| G2 | **사용 가능** | BIDS raw(CC0) + fMRIPrep 25.1.4 파생(ds007070, CC0), MNI152NLin2009cAsym volume과 fsLR 91k CIFTI [1차]. 논문이 기술한 21.0.2와 버전이 다르고 slice timing은 미보정 |
| G3 | **공개 (CC0), 평정 주체는 fMRI 참가자 본인** | events.tsv에 trial 단위 사후 평정. alignvideo 7차원 평정은 영상 종료 후 1회이며 약 51% 결측 [1차, 감사 에이전트 계산]. 별도 평정자 규범 평정과 연속 평정은 없다 |

### 1.4 NSD (Allen et al., 2022)

| Gate | 판정 | 근거 |
|---|---|---|
| G1 | **요청 필요 (대체 경로 있음)** | NSD Data Access Agreement 제출 후 `nsd_stimuli.hdf5` 접근 [검색]. COCO 원본 이미지는 공개되어 있어 `cocoId`, `cropBox`로 재구성할 여지가 있다(`cropBox` 정의 미확인) |
| G2 | **사용 가능 (고수준 전처리)** | GLMsingle single-trial beta(`betas_fithrf_GLMdenoise_RR`), 1.8 mm volume과 fsaverage, 7T, TR 1.6 s [본문: NSD 사용 논문들의 PMC 전문]. NSD 원 논문 본문과 Data Manual은 직접 읽지 못했다 |
| G3 | **정서 라벨 사실상 없음** | 공식 정서 관련 라벨은 nsdmeadows valence/arousal(shared 이미지 100+3장, NSD 참가자 본인, 스캔 후)뿐이다 [본문: Khosla 2022 / 평정 주체는 검색]. 73k 규모 정서 분석은 AI 추정 라벨이나 신규 인간 평정이 필요하다 |

---

## 2. Horikawa G1 = "요청 필요"의 영향과 대안

`reference/datasets_and_resources.md` 3절 규정에 따라 정리한다. G1이 "불가"는 아니지만 "요청 필요"이므로 사용자의 결정이 필요하다.

### 2.1 영향: 원본 비디오 없이 할 수 있는 것과 없는 것

| 원본 비디오 없이 가능 (figshare feature + raw BIDS) | 원본 비디오가 있어야 가능 |
|---|---|
| 34 category, 14 dimension decoding과 encoding (원 논문 baseline 재현과 확장) | 최신 video foundation model(V-JEPA 계열 등), CLIP, MLLM feature 추출 |
| 제공된 semantic 73차원, vision 1000차원 feature로 variance partitioning | 정서 vs 시각-의미 내용을 최신 모델 feature로 엄밀히 분리하는 분석 |
| 피험자 간 신뢰 가능한 정서 차원 수 추정 (Cowen & Keltner 방향 2의 남은 부분) | AI 생성 annotation (portrayed emotion, appraisal, 사람 수 등) |
| 분석 가정 민감도(multiverse) 검증: Horikawa 2020 vs Westlin 2025 | In-silico 비교 (TRIBE v2 등 encoding foundation model에 같은 자극 입력) |
| 내용 중복 15쌍과 ISC 기반 대체 noise ceiling | Generative counterfactual 자극 편집 |
| 범주 이름 텍스트 embedding과 뇌 RSM 비교 (Kiyokawa 2024 방식) | 비디오 재구성 |
| Raw BIDS를 fMRI foundation model 입력으로 사용 | |
| Emo-FilM과의 비지도 정서 공간 정렬 (라벨, 뇌 수준) | |

즉 Horikawa에서 **모델 기반 연구(최신 AI 모델로 자극을 표현하는 연구)는 원본 비디오가 있어야** 하고, **라벨과 뇌 수준의 연구는 지금도 가능**하다.

### 2.2 Horikawa 1순위 전략에 대한 추가 고려 사항 (Stage 1에서 새로 확인된 것)

1. **이 데이터는 2020년부터 공개되어 있었다.** 2026 공개 직후의 "선점 효과"는 없고, 재분석이 이미 여러 편 있다(Du 2023, Kiyokawa 2024, Westlin 2025, Asanuma 2025, EmoMind 2026 등). 새 질문은 이 기준선과의 차별성을 보여야 한다.
2. **원 결론에 반대되는 재분석이 있다.** Westlin et al. (2025)은 constructionist 관점의 재분석에서 원래의 범주-뇌 대응이 재현되지 않고 개인 간 변동이 크다고 보고했다(abstract 기준, 본문 미열람). 이 쟁점 자체가 연구 기회이자 위험이다.
3. **구조적 한계.** 피험자 5명, 반복 제시 없음(noise ceiling 불가), 무음, 참가자 보고와 생리 신호 없음. 개인차, 다감각, 주관 경험 질문에는 다른 데이터셋이 필요하다.

### 2.3 대안

| 대안 | 내용 | 장점 | 단점 |
|---|---|---|---|
| A. 즉시 요청 | Cowen 연구실 Google Form으로 비디오 요청 | 비용이 낮고, 다른 연구진의 사용 사례로 보아 승인 가능성이 있다 | 이용 조건, 승인 기간 미확인 |
| B. 기존 보유분 확인 | 연구실의 기존 프로젝트(EmoViS는 Horikawa 2020 사용, EmoBrain은 V-JEPA2 사용)가 이미 비디오나 추출 feature를 갖고 있는지 확인 | 이미 있다면 G1 문제가 사라진다 | 사용자 확인 필요 |
| C. 승인 전 병행 | 2.1절 왼쪽 열의 분석을 먼저 설계 | 대기 시간 활용 | 모델 기반 연구는 늦어진다 |
| D. Mendeley 예치본 확인 | 사용자가 브라우저로 doi:10.17632/jbk2r73mzh.1의 파일 목록 확인 (이 세션에서는 차단) | 비디오가 들어 있다면 바로 해결 | 들어 있지 않을 가능성이 높다(추정, 근거 없음) |
| E. 모델 기반 우선순위 이동 | 원본 자극을 바로 받을 수 있는 Spacetop, 또는 CC 영화로 재구성 가능한 Emo-FilM을 모델 기반 연구의 1순위로 두고 Horikawa는 라벨과 뇌 수준 분석에 쓴다 | 차단 요인 없음 | Horikawa의 장점(자극 수, 34 범주)을 모델 기반 연구에 못 쓴다 |

Coordinator 권고: **B를 먼저 확인하고, 없으면 A와 C를 병행한다.** Stage 2는 Horikawa를 계속 최우선으로 두되, 각 연구 질문에 "G1 필요 여부"를 표시해 원본 비디오가 없어도 진행할 수 있는 질문과 구분한다. 이 권고는 사용자 결정 전까지 잠정적이다.

---

## 3. 모델 기반 연구 가능 여부

"모델 기반 연구"는 AI 모델로 원본 자극의 feature를 추출하는 연구를 뜻한다(`reference/datasets_and_resources.md` 3절).

| 데이터셋 | 모델 기반 연구 | 조건 | 원본 자극 없이 가능한 연구 |
|---|---|---|---|
| Spacetop | **가능 (현재 유일하게 공개 경로로 즉시 가능)** | 실제 다운로드 확인 필요. 제3자 영상 저작권 범위 확인 필요(feature 추출은 연구 목적, 프레임 재배포는 별도) | 참가자 본인 평정 기반 decoding, 과제 간 비교, functional alignment |
| Emo-FilM | **조건부 가능** | LIRIS-ACCEDE에서 원본을 받아 크레딧 절단 재현, 또는 저자 요청. 영화별 CC 조항 확인 | 1 Hz 연속 평정 기반 decoding과 동역학, 생리-뇌 결합, label reliability 분석 |
| Horikawa | **조건부 가능** | Google Form 요청 승인, 또는 연구실 기존 보유분 | 2.1절 왼쪽 열 |
| NSD | **조건부 가능 (정서 연구로는 제한적)** | DAA 승인 또는 COCO 경로 재구성. 정서 라벨은 AI 추정이나 신규 수집 필요 | 기억 판단과 정서 관련 분석은 AI 라벨 없이는 nsdmeadows 100장으로 제한 |

네 데이터셋 모두 "불가"는 아니다. 다만 우리 환경 보유 여부가 확인되면 이 표가 바뀔 수 있다.

---

## 4. 사용자가 결정하거나 확인해야 할 사항

1. **환경 정보 입력:** `reference/datasets_and_resources.md` 1절 6개 칸 (데이터 경로, 원본 자극 보유, 추출 feature, 계산 자원, checkpoint, 제약).
2. **Horikawa 원본 비디오:** 연구실(EmoViS, EmoBrain)이 이미 보유하고 있는가? 없다면 Google Form 요청을 진행할 것인가?
3. **Horikawa 1순위 유지 여부:** 2.2절 사항(2020년부터 공개, Westlin 2025 반대 재분석, 5명, 무음)을 고려해 Horikawa를 1순위로 유지할지, 모델 기반 연구의 1순위를 Spacetop 또는 Emo-FilM으로 옮길지.
4. **NSD 접근:** DAA 승인을 이미 갖고 있는가?
5. **Emo-FilM 편집본:** 연구실의 Emo-FilM 연구 계획이 이미 영화 편집본을 확보했는가?
6. **Spacetop 생리 데이터:** 공개본에 없는 EDA/PPG를 저자에게 요청할 것인가?
7. **`reference/` 파일 정정:** `datasets_and_resources.md` 2.1절의 "2026년 4월 공개"와 `starting_papers.md`의 "Horikawa 데이터. 2026년에 공개되었으므로" 서술을 확인된 사실로 고칠지. Coordinator는 사용자 소유 지침 파일이라 직접 고치지 않았다.
