# Deliverable A: Dataset Intelligence Report

* 작성: Coordinator (Stage 1 통합)
* 기준일: 2026-11-12
* 입력: `outputs/stage1/dataset_Horikawa.md`, `dataset_EmoFilM.md`, `dataset_Spacetop.md`, `dataset_NSD.md` (dataset-auditor 4개 실행 결과), `outputs/stage1/environment_gaps.md`
* 사실 검증: `outputs/agents/adversarial-reviewer/stage1_audit.md` (검증 후 반영 내역은 문서 끝 "검증 반영 기록" 절)
* 표기: 각 사실의 세부 출처와 검증 수준([1차], [본문], [검색] 등)은 데이터셋별 보고서에 있다. 이 문서는 비교와 판정을 담고, 필요한 경우 데이터셋 보고서의 절 번호를 단다.

## 0. 요약

1. 네 데이터셋 모두 G1(원본 자극)이 "불가"는 아니다. **Spacetop은 공개 저장소에서 바로 받을 수 있고**(실제 다운로드는 미실행), **Emo-FilM은 공개 재료(CC 영화 원본, 공개 원격에 기록된 절단 정보 파일)로 재구성할 가능성이 높다**(파일 내용 확인 필요). Horikawa는 요청이 필요하고, NSD는 약관(Data Access Agreement) 동의 절차가 필요하다. 우리 환경 보유 여부는 네 데이터셋 모두 **미확인**이다(`reference/datasets_and_resources.md` 1절 공란).
2. **정서 라벨의 평정 주체가 데이터셋마다 다르다.** Horikawa와 Emo-FilM은 "별도 평정자가 자기 경험을 보고한 규범 평정", Spacetop은 "fMRI 참가자 본인의 사후 보고"다. NSD(nsdmeadows 100장)도 참가자 본인 평정으로 보이지만 근거가 2차 문헌과 검색 수준이고, 지시문이 "느낀 정서"인지 "이미지 정서 판단"인지 확인하지 못했다. 네 데이터셋 어디에도 스캔 중 연속 자기보고는 없다.
3. **라벨 정의가 직접 풀링 가능한 쌍은 없다.** 이름이 같은 일부 범주(예: fear, sadness, disgust)를 순위나 RSA 수준에서 비교하거나, 공통 모델 feature 공간을 통해 정렬하는 방식만 가능하다(3절 단계형 판정).
4. 출발점 정보와 다른 사실이 확인되었다. 가장 중요한 것은 **Horikawa 원자료가 2026년에 처음 공개된 것이 아니라 2020-04-24부터 OpenNeuro(ds002425)에 CC0로 공개되어 있었다**는 점이다. 전처리본과 라벨도 figshare에 있다(figshare 공개일은 직접 확인하지 못했으나 2023년 논문이 인용). 그래서 이 데이터의 재분석이 2022~2026년에 이미 여러 편 있다. 그중 Westlin et al. (2025, arXiv preprint, 본문 미열람)은 최소 가정 분석에서 원 논문의 범주-뇌 대응을 관찰하지 못했고 개인 간 변동이 크다고 보고했다(초록 기준). 이는 재현 실패 보고이며, 원 결론에 대한 반대 증거로 확정된 것은 아니다(6절).
5. Kragel 연구실 2026 연구의 서지가 확정되었다: Ma & Kragel (2026), *Nature Communications* 17:1518, doi:10.1038/s41467-025-68240-z. Emo-FilM 29명, 50개 항목 중 17개만 사용했다.

---

## 1. 4개 데이터셋 비교표

| 항목 | Horikawa et al. (2020) | Emo-FilM (Morgenroth et al., 2025) | Spacetop (Jung et al., 2025) | NSD (Allen et al., 2022) |
|---|---|---|---|---|
| 논문 | iScience 23(5):101060, doi:10.1016/j.isci.2020.101060 | Sci Data 12:684, doi:10.1038/s41597-025-04803-5 | Sci Data 12:1465, doi:10.1038/s41597-025-05154-x | Nat Neurosci 25(1):116-126, doi:10.1038/s41593-021-00962-x |
| 공개 저장소 | OpenNeuro ds002425 (raw, CC0, 2020-04-24부터), figshare (전처리본, 라벨), Mendeley 10.17632/jbk2r73mzh.1 (2026-04-15, 내용 미확인) | OpenNeuro ds004892 (fMRI, v1.0.2), ds004872 (평정, v1.0.3), 모두 CC0 | OpenNeuro ds005256 (raw, v1.1.0), ds007070 (fMRIPrep 파생, v1.0.3), 모두 CC0 | AWS S3, Data Access Agreement 후 접근. Terms 원문 미확인 |
| 피험자 | 5명 (여 1) | 30명 (여 18). 단 S07의 영화 3편 전처리본만 v1.0.2(2026-08-13) 이전에 결측 (raw는 처음부터 존재) | 논문 N=101, 저장소 117명, 41 run 전부 보유 61명 | 8명 |
| 1인당 데이터 | 61 run, 약 8시간 functional | 영화 14편 약 2.7시간 + rest 10분 | 최대 41 run, 약 5.4시간 + 구조 영상 | 30~40 세션, 22,000~30,000 trial |
| 자극 | Cowen & Keltner 정서 유발 비디오. 제시 ID 2,196개, 코드가 중복으로 표시해 분석에서 제외한 label index 15개를 빼면 고유 2,181개(본문 기준. 같은 논문 abstract는 2,185로 표기). 평균 약 5 s, 0.15~90 s | LIRIS-ACCEDE 계열 CC 단편영화 14편 (6.7~17.1분, 합 9,600 s), 앞뒤 크레딧 절단본 | alignvideo 49편(소리 있음, 20 s~5분 39초, 합 86분), narratives 8편, faces 288개, 통증(열) 자극, vicarious 통증 영상 등 6개 과제 | COCO 자연 장면 73,000장 풀, 1인당 약 10,000장, 3 s 제시 |
| 모달리티 | **무음** 비디오 | 시청각 영화 (대사 영어로 보임) | 시청각 영상, 오디오/텍스트 이야기, 얼굴 영상, 열 통증 | 정지 이미지 |
| 반복 제시 | 없음 (중복으로 표시된 label index 15개, 쌍 구조와 중복 대상은 미확인) | 없음 (영화당 1회) | alignvideo 원칙상 1회 (tornado 중복 가능성 미확인), shortvideo가 alignvideo 인물을 재노출 | 이미지당 3회 (설계), shared1000 / shared515 |
| 정서 라벨 종류 | 34 emotion category (선택 비율), 14 affective dimension (9점 평균) | 50개 항목: discrete 13 + CPM 성분 37 (Appraisal 10, Motivation 10, Feeling 7, Expression 5, Physiology 5) | alignvideo 7차원 (personal relevance, happy, sad, afraid, disgusted, warm and tender, engaged), narratives good-bad 감정과 기대, social 통증 기대/결과, faces 표정 강도 지각, shortvideo mentalizing | 기본 정서 라벨 없음. nsdmeadows valence/arousal (shared 이미지 100+3장)만 있음 |
| 라벨 시간 해상도 | 비디오당 1개 값 | **1 Hz 연속** (consensus) | 영상/trial 종료 후 1회 | 이미지당 1개 값 (100장) |
| 평정 주체 | 별도 MTurk 평정자 (2차 출처 기준 853명, 비디오당 category 9~17명), 자기 경험 보고. fMRI 참가자 보고 없음 | 별도 평정자 44명, 항목×영화당 3~4명 consensus, 자기 경험 보고. fMRI 참가자의 부분적 사후 클립 평정 (영화당 5항목, 영화 길이의 약 20%) | **fMRI 참가자 본인**의 사후 평정 (alignvideo는 본인 경험, faces와 shortvideo는 타인 정서 지각/귀속 판단). alignvideo 평정 약 51% 결측 | **fMRI 참가자 본인으로 보임**, 스캔 종료 후 스캐너 밖. 근거는 2차 문헌(Khosla 2022의 "subject-averaged")과 검색 수준. 지시문(felt vs perceived) 미확인 |
| 라벨 신뢰도 지표 (**지표가 서로 달라 열 사이 직접 비교 불가**) | 범주별 수치 미확인. 평정자 개인 자료 비공개라 재계산 불가 | 평정자 쌍별 1 Hz 시계열 Pearson r의 평균: 0.38 (초록) / 0.39 (본문), 항목별 0.21~0.60 | 개인 대 나머지 집단 평균 상관 중앙값 0.46~0.77 (차원별). 참고: 영상당 약 51명 집단 평균의 split-half(Spearman-Brown, 49개 영상 점) 0.94~0.99. 둘 다 감사 에이전트 직접 계산, 탐색적 | 해당 없음 |
| 생리 신호 | 없음 | PPG, 호흡, EDA 1000 Hz, 모든 런, 공개 | EDA, PPG 기록 (코드 기준 2000 Hz), **공개 파일 없음** | Pulse, respiration (약 10 세션/인), eye tracking (2~4 세션/인, 품질 가변). 세부 [검색] 수준 |
| 스캐너 / 해상도 | 3T Siemens Verio, TR 2 s, 2 mm, MB4 | 3T Siemens TIM Trio, TR 1.3 s, 2.5 mm, MB3 | 3T Siemens Prisma, TR 0.46 s, 2.7 mm, MB8 | 7T Siemens, TR 1.6 s, 1.8 mm |
| 제공 전처리 | fMRIPrep 기반, native volume, 비디오당 1 sample로 블록 평균한 HDF5. HCP360 + 피질하 ROI, pycortex surface | FSL FEAT, native / subject / MNI volume, 6 mm smoothing, WM/CSF/motion 회귀 적용 상태. fMRIPrep, surface 없음 | fMRIPrep 25.1.4, MNI152NLin2009cAsym volume + fsLR 91k CIFTI. 논문 기술 버전(21.0.2)과 다름. slice timing 미보정 | GLMsingle single-trial beta (1.8 mm volume, fsaverage), 1.0 mm 업샘플 시계열, pRF/fLoc ROI |
| 원본 자극 접근 (G1) | 요청 필요 (Cowen 연구실 Google Form) | 공개 재료로 재구성 가능성 높음 (확인 필요), 실패 시 저자 요청 | 공개 다운로드 가능 (제3자 영상 저작권 미확인) | 약관(DAA) 동의 후 다운로드 (승인 심사 여부 미확인). COCO 원본은 공개 |
| 라이선스 | raw CC0, 코드 MIT. figshare, Mendeley, 비디오 조건 미확인 | 데이터 CC0, 코드 Apache-2.0, 영화는 CC (영화별 조항 미확인) | 데이터 CC0, DUA 없음 | NSD Terms 미확인. COCO annotation CC BY 4.0, 이미지는 Flickr 약관 |

---

## 2. Gate 종합표

판정은 공개 경로 기준이다. 우리 환경 보유 여부는 네 데이터셋 모두 미확인이다. 근거의 세부는 `outputs/stage1/gate_decision.md`와 데이터셋 보고서 Gate 표에 있다.

| 데이터셋 | G1 원본 자극 | G2 fMRI 형식과 전처리 | G3 라벨 접근과 평정 주체 |
|---|---|---|---|
| Horikawa | **요청 필요.** 공개 저장소에 비디오 없음. Google Form 요청 경로가 데이터 제공자 README에 명시. 2023~2025년 독립 연구진이 원본을 실제로 사용(간접 증거) | **사용 가능.** Raw BIDS(CC0) + native volume 블록 평균 전처리본. 표준공간 전처리본과 연속 시계열은 미확인 | **공개.** 별도 평정자 규범 평정(비디오당 집계값). fMRI 참가자 보고 없음. 평정자 개인 자료 비공개 |
| Emo-FilM | **공개 재료로 재구성 가능성 높음 (확인 필요), 실패 시 요청.** 공개 저장소에 편집된 영상 자체는 없다. 원본은 CC 단편영화(LIRIS-ACCEDE 계열)이고, 크레딧 절단 정보 후보 파일(`code/FilmInfo.txt`, `code/BBL_experiment_Movies_without_credits_exp_files.xlsx`)이 git-annex 기록상 OpenNeuro 공개 S3에 존재한다. 두 파일 내용과 영화별 입수 조건은 미확인. 감사 에이전트는 "요청 필요(조건부 재구성)", 검증 에이전트는 "재구성 가능성 높음"으로 판단했고 Coordinator는 후자를 채택했다(이견은 `outputs/agents/adversarial-reviewer/stage1_audit.md` 5절) | **사용 가능.** BIDS raw + FSL volume 전처리본(6 mm smoothing 적용). 정밀 분석은 raw 재전처리 권장 | **공개 (CC0).** 별도 평정자 44명의 1 Hz 연속 평정 + 평정자별 원자료. fMRI 참가자 자기보고는 부분적 |
| Spacetop | **공개 다운로드 가능.** `stimuli/`에 8개 과제 자극(git-annex 기록상 공개 S3). 실제 다운로드는 네트워크 제약으로 미실행. 제3자 영상 원 출처와 재사용 조건 미기재 | **사용 가능.** BIDS raw + fMRIPrep 파생(volume + surface) | **공개 (CC0, events.tsv).** fMRI 참가자 본인의 trial 단위 사후 평정만 있음. 규범 평정과 연속 평정 없음 |
| NSD | **약관 동의 절차 필요 (요청 범주, 승인 심사 여부 미확인).** NSD Data Access Agreement 양식 제출과 Terms 동의 후 `nsd_stimuli.hdf5`를 포함한 배포본 사용. AWS Registry 항목은 S3 버킷을 무계정(`--no-sign-request`)으로 안내한다([검색]). COCO 원본 + `cocoId`/`cropBox`로 재구성할 여지도 있다(`cropBox` 정의 미확인). 감사 에이전트는 "요청 필요(DAA)", 검증 에이전트는 "약관 동의 후 다운로드"로 판단했고 양쪽 모두 검색 수준 근거라 원문 확인이 필요하다 | **사용 가능 (고수준 전처리).** GLMsingle beta, volume과 fsaverage | **정서 라벨 사실상 없음.** nsdmeadows 100(+3)장만 참가자 본인 평정. 73k 규모 정서 라벨은 AI 추정 또는 신규 수집 필요 |

---

## 3. Cross-dataset Compatibility

점검 항목: (a) 평정 주체가 같은 종류인가, (b) 척도와 형식(범주 선택 비율, 단극/양극 강도, 상대 배치)이 같은가, (c) 시간 해상도가 같은가, (d) 자극 모달리티가 같은가, (e) 항목 이름과 정의가 대응하는가.

**단계형 판정** (검증 에이전트 제안 X3 반영):
* **수준 1, 라벨 풀링 가능:** 두 데이터셋의 라벨을 같은 변수로 합쳐 학습하거나 평가할 수 있다.
* **수준 2, 이름 대응 항목의 순위/RSA 비교 가능:** 라벨을 합칠 수는 없지만 이름이 대응하는 항목을 골라 자극 간 순위나 유사도 구조를 비교할 수 있다(필요하면 시간 집계 후).
* **수준 3, 공통 모델 feature 공간 경유만 가능:** 대응하는 라벨이 없거나 너무 달라서, 같은 AI 모델 feature 공간이나 비지도 정렬을 거쳐야만 연결된다.

### 3.1 쌍별 판정

| 쌍 | 판정 (수준) | 근거 |
|---|---|---|
| Horikawa ↔ Emo-FilM | **수준 2.** 라벨 풀링 불가. 이름 대응 범주의 순위/RSA 수준 비교 가능 | (a) 둘 다 별도 평정자의 1인칭 경험 보고라는 점은 같다. (b) Horikawa는 범주 선택 비율과 9점 Likert 평균, Emo-FilM은 평정자 내 z-score된 연속 강도라 척도가 다르다. (c) 비디오당 1개 값 vs 1 Hz. (d) 무음 짧은 클립 vs 소리 있는 단편영화. (e) 이름이 겹치는 범주(fear, anger, disgust, anxiety, surprise, satisfaction, guilt, pride 등)도 Emo-FilM 쪽 일부는 양극 척도(Pride는 Proud~Ashamed, Regard는 Regard~Contempt)라 정의가 다르다. 근거: dataset_Horikawa.md 2.3, 7절; dataset_EmoFilM.md 2.2, 7절 |
| Horikawa ↔ Spacetop | **수준 3** (이름은 일부 대응하지만 평정 주체가 달라 순위 비교의 해석이 어렵다) | (a) 별도 평정자 규범 평정 vs fMRI 참가자 본인 보고로 주체가 다르다. (b) 선택 비율 vs 0~100 강도. (d) 무음 vs 소리 있음. (e) happy/sad/afraid/disgusted가 Horikawa의 joy/sadness/fear/disgust와 이름 수준으로 대응하지만 측정 대상(타인 집단의 규범 vs 본인 경험)이 다르다. 결합하려면 Spacetop 영상에 Cowen & Keltner식 규범 평정을 새로 모으거나 공통 모델 feature 공간을 거쳐야 한다. 근거: dataset_Spacetop.md 7절 |
| Horikawa ↔ NSD | **수준 3** | NSD에 정서 라벨이 사실상 없다. 이름이 같은 Valence, Arousal 차원도 Horikawa는 별도 평정자의 9점 Likert 평균, NSD nsdmeadows는 참가자 본인의 상대 배치값이라 척도와 주체가 다르다. 정지 이미지 vs 비디오. 연결 경로는 in-silico 적용(NSD 학습 encoding model에 Horikawa 프레임 입력)이나 Cowen & Keltner 자극 기반 모델(EmoNet 등)을 NSD에 적용하는 것이며, 그 결과는 AI 추정 라벨이다. 근거: dataset_NSD.md 7절 |
| Emo-FilM ↔ Spacetop | **수준 2 (시간 집계 후).** 라벨 풀링 불가. 단 평정 주체가 달라(별도 평정자 vs 본인) 비교 결과에 주체 차이가 섞인다 | (a) 별도 평정자 vs 참가자 본인. (c) 1 Hz vs 영상 종료 후 1회. 둘 다 소리 있는 영상이고 생리 기록이 있다는 공통점은 있다(Spacetop 생리는 미공개). Emo-FilM 연속 평정을 구간 단위로 집계하면 Happiness, Sad, Fear, Disgust, WarmHeartedness가 Spacetop의 happy, sad, afraid, disgusted, warm and tender와 이름 수준으로 대응한다. 근거: dataset_EmoFilM.md 7절; dataset_Spacetop.md 7절 |
| Emo-FilM ↔ NSD | **수준 3** | 연속 영화 vs 정지 이미지, 3T vs 7T, 수동 시청 vs 기억 과제. Emo-FilM에는 valence, arousal 항목이 직접 없고(Ma & Kragel은 Good/Bad, Calm/AtEase를 대리 지표로 사용), NSD는 100장뿐이다. 공통 모델 공간(VLM 정서 평정 축 등)에서 비교하는 방식만 현실적이다. 근거: dataset_EmoFilM.md 2.2, 7절; dataset_NSD.md 7절 |
| Spacetop ↔ NSD | **수준 3** | 겹치는 자극과 구성 개념이 없다. 공통 AI feature(CLIP 등) 공간을 통한 encoding 전이만 가능하다. 근거: dataset_Spacetop.md 7절; dataset_NSD.md 7절 |

**문서 간 판정 차이 기록 (X4):** 데이터셋 보고서 일부는 다른 판정을 적었다. dataset_EmoFilM.md 7절은 Emo-FilM ↔ Spacetop을 "부분 결합 가능", dataset_Horikawa.md 7절은 Horikawa ↔ Spacetop을 "미확인"으로 적었다(당시 Spacetop 감사 결과가 없었음). 위 단계형 판정이 이를 대체하지만, Emo-FilM 감사의 "부분 결합 가능"은 생리 신호 리샘플링 비교까지 포함한 넓은 의미였고 라벨 수준에서는 수준 2와 같은 내용이다.

### 3.2 평정 주체로 본 구조

| | 별도 평정자 (규범) | fMRI 참가자 본인: 자기 경험 보고 | fMRI 참가자 본인: 타인 정서 지각/귀속 판단 |
|---|---|---|---|
| 연속 시간 평정 | Emo-FilM (1 Hz, 50항목) | 없음 | 없음 |
| 자극/trial 단위 평정 | Horikawa (34 + 14) | Spacetop alignvideo (7차원), Spacetop narratives, Emo-FilM 사후 클립 회고 평정 (부분), NSD nsdmeadows (100장, 지시문 미확인이라 이 칸 배치는 잠정) | Spacetop faces (표정 강도), Spacetop shortvideo (인물 mentalizing) |

"규범 평정 vs 본인 보고가 뇌 반응을 얼마나 다르게 설명하는가"라는 질문을 **현재 공개 자료만으로 한 데이터셋 안에서** 직접 다룰 수 있는 곳은 **Emo-FilM뿐**이다. 그마저 본인 보고가 스캔 후 클립 재시청 회고 평정이고, 항목×영화당 3~4명, 영화 길이의 약 20%만 덮어 참가자 개인 수준 비교가 어렵다. **NSD에는 별도 평정자의 규범 평정이 없다**(dataset_NSD.md 2.3절). NSD에서 이 질문을 다루려면 shared 이미지에 규범 평정을 새로 수집해야 하고, 현재 자료로는 "본인 보고 vs AI 추정"만 비교할 수 있다. Spacetop도 영상에 규범 평정을 새로 모으면 같은 비교가 가능해진다.

### 3.3 공통 결합 경로 (라벨을 직접 합치지 않는 방법)

1. **공통 모델 feature 공간.** 각 데이터셋의 자극을 같은 video/vision/audio/language 모델로 표현하고 뇌 반응을 그 공간에 encoding한다. 라벨 정의 차이를 피하지만 G1(원본 자극)이 필요하다.
2. **순위/RSA 수준 비교.** 이름 대응 범주만 골라 자극 간 유사도 구조를 비교한다. 척도 차이에 덜 민감하다.
3. **비지도 공간 정렬.** Gromov-Wasserstein 같은 방법으로 각 데이터셋의 정서 공간을 라벨 대응 없이 정렬한다(Horikawa 보고서 8.4절 7번이 제안).
4. **공통 프로토콜로 신규 평정 수집.** 예: Spacetop 영상이나 NSD shared1000에 같은 문항으로 규범 평정을 수집. 비용이 들지만 라벨 비호환을 근본적으로 줄인다.
5. **공간 표준화.** Horikawa 공개 전처리본은 native volume이라 voxel 결합이 불가하다. HCP360 parcel 수준이나 raw 재전처리 후 결합해야 한다.

모든 경로에서 AI가 만든 라벨은 "AI 추정 정서"로 따로 표기하고, 인간 평정을 대체하는 근거로 쓰지 않는다(CLAUDE.md 6절).

---

## 4. 데이터셋별 고유 장점과 방법론적 한계

### 4.1 Horikawa

| 고유 장점 | 방법론적 한계 |
|---|---|
| 고유 비디오 2,181개로 정서 fMRI 중 조건 수가 매우 많다 | 피험자 5명. 개인차와 집단 일반화에 약하다 |
| 1인당 약 8시간 deep sampling | 반복 제시가 없어 noise ceiling을 구할 수 없다 (원 논문 Discussion이 명시) |
| 같은 자극에 34 category와 14 dimension이 함께 있다 | 라벨은 타인 집단 평균이며 fMRI 참가자 보고, 생리, eye tracking이 없다. decoding 결과를 참가자 주관 경험으로 해석할 수 없다 |
| Raw CC0, 전처리본, 재현 코드(MIT), ROI 정의 공개 | 무음이라 청각, 음악, 음성 질문에 쓸 수 없다 |
| 원 논문(2020), Du 2023, Kiyokawa 2024, Westlin 2025, EmoMind 2026 등 비교 기준선 축적 | 블록의 약 72%가 10 s라 비디오 내 동역학 분석 여지가 작다 |
| categorical 해석(원 논문)과 최소 가정 재분석의 재현 실패 보고(Westlin 2025, preprint, 초록 기준)가 같은 데이터에 공존해 분석 가정 민감도 검증의 시험대가 된다 | 5명이 같은 자극 순서. 중복으로 표시된 label index 15개 처리 필요. 같은 원본에서 잘린 클립 여부(movie-level leakage) 미확인 |
| | 평정자(미국 MTurk)와 fMRI 참가자(일본 촬영)의 문화권 불일치 가능성 |

### 4.2 Emo-FilM

| 고유 장점 | 방법론적 한계 |
|---|---|
| CPM 성분 37개 + discrete 13개의 1 Hz 연속 평정 | 주 라벨은 3~4명 별도 평정자의 consensus. 평균 agreement 0.38~0.39로 낮고 항목별 편차가 크다 |
| 평정자별 원자료 공개로 label noise와 reliability 천장을 직접 계산 가능 | 평정을 평정자 내 z-score해 절대 강도가 아닌 상대 변화량이다 |
| 소리 있는 완결 서사, 영화당 6.7~17.1분 | 영화 14편뿐이라 leave-one-film-out fold가 14개이고 영화 수준 confound와 정서가 공선적일 수 있다 |
| PPG, 호흡, EDA 1000 Hz 공개 | 평정자는 같은 영화를 최대 6번 봤다 (항목 블록 설계) |
| fMRI 참가자의 부분 자기보고로 consensus 타당성 점검(평균 0.41) | 제공 전처리본은 6 mm smoothing과 WM/CSF 회귀가 적용된 상태. slice timing, distortion correction 서술 없음 |
| CC0, 영화가 CC 라이선스라 자극 재구성 경로가 열려 있다 | 생리는 fMRI 참가자, 평정은 별도 평정자라 주체가 다르다 |
| | 문서 불일치(0.38 vs 0.39, 검증 항목 산술 34+13≠48, "public domain"과 "Creative Commons" 혼용), `LeassonLearned` 중복 의심 파일 |

### 4.3 Spacetop

| 고유 장점 | 방법론적 한계 |
|---|---|
| 같은 참가자에게서 본인 경험(alignvideo), 타인 표정 지각(faces), 인물 정서 귀속(shortvideo), 통증 기대와 경험(social)을 함께 측정 | 정서 라벨이 영상 종료 후 1회라 영상 내 정서 변화와 BOLD를 대응시킬 수 없다 |
| 열 통증이라는 생리적으로 통제된 정동 자극 + 기만 cue로 기대와 예측오차 분리 | alignvideo 평정 약 51% 결측(클릭해야 저장되는 코드 구조), 세션 전체 결측 23~28명 |
| 원본 자극 공개, CC0, DUA 없음 | 라벨 독립 표본이 영상 49(또는 48)개 |
| TR 0.46 s, fsLR 91k CIFTI 제공 | 7개 차원 중 2개(personal relevance, engaged)는 정서 범주가 아니고 valence/arousal 문항이 없다. 부정 정서 바닥 효과 |
| 모든 참가자 같은 영상, 같은 순서 (functional alignment 설계) | 영상 직후 평정 구간이 붙어 있어 평정 행위가 영상 끝부분 HRF와 겹친다 |
| 소리 있는 영상 | 생리, 설문, 원시 행동 로그 미공개. 시선, 호흡 미기록 |
| | 논문 N=101 vs 저장소 117명 vs 전체 run 61명, 성별 표기 오류 의심, 행렬 크기 표기 불일치(64 vs 82) |

### 4.4 NSD

| 고유 장점 | 방법론적 한계 |
|---|---|
| 1인당 약 10,000장, 3회 반복, 7T 1.8 mm single-trial beta | 정서 유발 목적 자극이 아니며 이미지 valence가 대체로 중립(범위 제한, Sadeghi 2024) |
| shared515로 noise ceiling 추정 가능 | 정서 라벨이 nsdmeadows 100장뿐. 73k 규모 정서 분석은 AI 추정 라벨에 의존 |
| fMRI 참가자 본인으로 보이는 valence/arousal 평정(100장, 지시문 미확인) | 일상 장면(BOLD5000)에서 객체 인식 모델(AlexNet)이 정서 특화 모델(EmoNet)보다 20개 범주 정서 판단을 더 잘 예측했다(Gao 2025, 20-way 분류 정확도 기준, 절대 설명량은 크지 않음). 정서 라벨이 의미 내용의 재표현이 될 위험 |
| trial 단위 recognition 판단으로 정서와 기억 상호작용 연구 가능 | 반복 제시와 old/new 과제 때문에 novelty, 친숙도 신호가 각성 성격 신호와 섞인다 |
| 캡션, 객체 범주, segmentation으로 의미 내용 통제 변수 확보 용이 | COCO가 대다수 VLM 학습 분포 안에 있어 사전학습 오염 위험. NSD로 사전학습된 모델을 NSD 분석에 쓰면 누수 |
| NSD-synthetic, NSD-Imagery 확장, encoding/decoding/generative 모델 생태계 | 피험자 8명. 원 논문 본문, Data Manual, Terms 원문을 이번 감사에서 직접 읽지 못해 다수 사양이 [검색] 수준 |

---

## 5. 데이터셋별 연구 기회 목록 (Stage 2 에이전트 참고)

아래는 탐색 후보이며 확정 질문이 아니다. 선행 수행 여부는 Stage 1 검색 범위 안의 판단이다. 상세 근거는 각 보고서의 8절에 있다. 겹침은 `reference/existing_projects.md` 기준으로 표시만 했다.

### 5.1 Horikawa (dataset_Horikawa.md 8.4절)
1. 분석 가정 민감도(multiverse) 검증: 원 논문의 categorical 결론과 Westlin 2025(preprint, 초록 기준)의 재현 실패 보고가 어떤 분석 선택에서 갈리는가. Westlin 2025는 반대 증거가 아니라 "분석 가정 민감도의 시험대" 근거로만 쓴다. G1 불필요.
2. 피험자 간 신뢰 가능한 정서 차원 수 추정: Cowen & Keltner Discussion 방향 (2)의 남은 부분. G1 불필요.
3. 최신 video foundation model, MLLM feature를 nuisance로 넣은 정서 vs 시각-의미 분리. G1 필요. overlap: EmoViS (affective brain geometry의 sensory-semantic 기원).
4. 인간 규범 평정 vs AI 추정 평정의 뇌 설명력 비교. G1 필요.
5. 내용 중복 15쌍과 ISC를 이용한 대체 noise ceiling 추정. G1 불필요.
6. In-silico 예측(TRIBE v2 등 합성 뇌)과 실제 fMRI의 정서 표상 차이. G1 필요.
7. Horikawa와 Emo-FilM 정서 공간의 비지도 정렬(Gromov-Wasserstein). G1 불필요.
8. Portrayed vs evoked 정서 분리를 위한 신규 주석. G1 필요.
* Horikawa 데이터에 대한 34차원 정서 profile decoding 자체는 overlap: EmoBrain (34차원 정서 profile, cross-subject decoding).

### 5.2 Emo-FilM (dataset_EmoFilM.md 8.3절)
1. Appraisal 공간(Predictable, Controlled, Suddenly, Urgency, Agent)에서의 지도 구조. Ma & Kragel (2026)이 한계로 든 차원을 직접 다룬다. 주의: "Higher-order topology uncovers the multidimensional dynamics of naturalistic emotion"(bioRxiv 2026, doi:10.64898/2026.09.26.754452, 미검증 preprint)이 Emo-FilM 50개 항목 기반 정서 프로파일을 다뤄 1번과 5번에 부분 겹칠 수 있다.
2. 정서 vs 시청각-의미 내용의 variance partitioning. G1 필요. overlap: Emo-FilM 연구 (사전학습 멀티모달 뇌 인코딩으로 정서 맥락 기여 분석).
3. 규범 평정 vs fMRI 참가자 본인 사후 보고의 차이가 뇌 신호로 예측되는가 (탐색적, 표본 작음).
4. 보고된 생리(평정자의 Heartrate, Muscle 등) vs 측정된 생리(참가자 PPG, 호흡, EDA)와 뇌-몸 결합.
5. 실제 정서 전이 통계로 학습한 state-space, successor representation, RL 모형과 TEM 비교 (Ma & Kragel partially).
6. 평정자별 원자료로 계산한 reliability 천장 대비 decoding 정규화, label noise 모형.
7. MLLM 50항목 연속 평정을 human-human 일치도와 같은 지표로 비교. G1 필요.
8. 같은 영화의 외부 주석(LIRIS-ACCEDE continuous V/A, aesthetic highlight)과 교차 타당화.

### 5.3 Spacetop (dataset_Spacetop.md 8절)
1. 경험 정서 vs 지각/귀속 정서의 공유 표상 (alignvideo, faces, shortvideo, functional alignment 후 비교).
2. 통증 기대와 정서의 공통 계산 (cue 기반 기대, 예측오차의 신경 분석).
3. AI 생성 연속 정서 annotation을 이용한 time-resolved encoding. **타당화 경로 주의 (검증 지적 반영):** Spacetop의 영상별 평정(49개 점)은 영상 단위 집계값만 검증할 수 있고 영상 안 시간축의 타당성은 검증하지 못한다. 시간축 타당성은 먼저 Emo-FilM의 1 Hz 인간 consensus로 검증하고(데이터셋 간 도메인 차이를 기록), Spacetop에서 얻은 시간축 결과는 "미검증 AI 추정 시계열"로 표기한다. overlap: Emo-FilM 연구 (방법 일부), EmoBrain (V-JEPA2 feature 사용 가능성).
4. 개인 고유 정서 반응(idiosyncrasy): hyperalignment 후 남는 개인 특이 반응이 개인 평정 편차를 예측하는가.
5. 이야기의 다중 시간척도 정서 (narratives 위계 + LLM surprisal + Miao 2026 연속 ToM 평정).
6. 소리의 정서 기여 (오디오 vs 비디오 feature 고유 설명량). Horikawa(무음)와 대비.
7. Brain Foundation Model latent의 정서 정보 (시각-의미 통제 후).
8. 정서 에피소드의 재노출과 기억 (shortvideo).
9. (조건부) EDA/PPG 입수 시 생리, 자기보고, 뇌의 3자 관계.

### 5.4 NSD (dataset_NSD.md 8절)
1. 정서의 고유 분산 검정: 여러 출처 AI 정서 라벨을 LLM 캡션 embedding, 객체 범주 통제 후 voxel별 고유 설명 분산으로 추정. shared1000 신규 인간 평정으로 보정. overlap: EmoViS (sensory-semantic 기원 질문과 방향 겹침).
2. 참가자 본인 평정 vs AI 평정의 뇌 정렬 비교 (100장, 효과 크기 추정 중심). **규범 평정과의 비교는 NSD에 규범 평정이 없으므로 shared 이미지에 대한 신규 규범 평정 수집이 전제다.** nsdmeadows 지시문(felt vs perceived) 확인도 선행되어야 한다.
3. 정서(각성)와 기억의 상호작용: trial 단위 recognition, 반복 억제.
4. In-silico 정서 탐침과 생성적 검증 (NSD 학습 encoding model에 IAPS, OASIS, Cowen & Keltner 프레임 입력).
5. 사회적 장면 valence의 계층 분리 (장면 맥락 vs 인물 상호작용).
6. NSD(중립, 대규모)와 Horikawa(정서 풍부, 소규모)의 공통 encoding 공간 결합.

### 5.5 데이터셋을 가로지르는 기회
1. **평정 주체 효과:** 3.2절 표를 이용해 규범 평정, 본인 보고, 타인 지각 판단, AI 추정 라벨이 같은 뇌 영역을 얼마나 다르게 설명하는지 비교. 현재 공개 자료로 한 데이터셋 안에서 규범 vs 본인을 비교할 수 있는 곳은 Emo-FilM(부분 자료)뿐이며, NSD와 Spacetop에서는 신규 규범 평정 수집이 전제다.
2. **소리의 유무:** Horikawa(무음) vs Emo-FilM, Spacetop(소리 있음)에서 같은 이름의 정서가 다른 표상을 갖는가.
3. **시간 해상도:** Emo-FilM(1 Hz)에서 학습한 동역학이 Spacetop의 영상 단위 사후 평정(peak-end 등)을 설명하는가.
4. **Label reliability를 통제 변수로:** Emo-FilM 평정자 원자료와 Spacetop 집단 신뢰도를 이용해 decoding 성능을 라벨 신뢰도 천장 대비로 비교.

---

## 6. 출발점 정보와 다르게 확인된 사실 (`reference/` 파일 대비)

| 출발점 서술 | 확인된 사실 | 출처 |
|---|---|---|
| Horikawa 공개 데이터: Mendeley, "2026년 4월 공개" (datasets_and_resources.md 2.1, starting_papers.md 특별 지시) | Raw BIDS는 OpenNeuro ds002425에 2020-04-24(v1.0.0)부터 CC0로 공개(감사 에이전트와 검증 에이전트가 각각 `CHANGES`로 확인). 전처리본과 라벨은 figshare에 있으며 2023년 논문(Du et al.)이 인용(figshare 공개일은 직접 확인 못 함). 2026-04-15는 Mendeley 예치본의 날짜. 따라서 "2026 공개 이후 첫 사용"이라는 틀은 맞지 않고 2022~2026년 재분석이 여러 편 있다 | dataset_Horikawa.md Gate 전달 사항, 2.1절; stage1_audit.md H1 |
| Horikawa "약 2,180개 비디오" | 제시 ID 2,196개, 중복으로 표시된 label index 15개 제외 시 고유 2,181개(본문), 같은 논문 abstract는 "all 2,185 videos", Cowen & Keltner 라이브러리 2,185개. 2,196과 2,185의 대응은 미확인 | dataset_Horikawa.md 1.2절; stage1_audit.md H6, H7 |
| Emo-FilM 평균 inter-rater agreement 0.38 | 초록 0.38, 본문 Technical Validation r = 0.39. 항목별 0.21~0.60 | dataset_EmoFilM.md 2.3절 |
| Emo-FilM 참가자 30명 | 30명이 맞지만 S07의 영화 3편 전처리본은 2026-08-13(v1.0.2)에 추가됨. 그 전 버전을 쓴 Ma & Kragel (2026)은 29명 사용 | dataset_EmoFilM.md 3절 |
| Spacetop 101명 | 논문 N=101, 저장소 117명(participants.tsv), 41 run 전부 보유 61명. N=101 산정 기준 미확인 | dataset_Spacetop.md 1.1절 |
| Spacetop "생리 데이터가 있다" | 기록은 했으나 공개 저장소(ds005256, ds007070)에 생리 파일 없음 | dataset_Spacetop.md 2.3절 |
| Spacetop "Scientific Data" (권호 미기재) | Scientific Data 12:1465 | dataset_Spacetop.md 머리말 |
| NSD "확인 필요" 서지 | Nat Neurosci 25(1):116-126, doi:10.1038/s41593-021-00962-x, PMID 34916659 | dataset_NSD.md 머리말 |
| Kragel 연구실 2026 연구 "서지 확인 필요" | Ma Y, Kragel PA (2026). Map-like representations of emotion knowledge in hippocampal-prefrontal systems. Nat Commun 17:1518. doi:10.1038/s41467-025-68240-z. 29명, discrete 13 + Feeling 4 항목, PLS ROI decoding, TEM. hippocampus는 범주, vmPFC는 2D affective space를 상대적으로 잘 decoding(효과 크기 r 약 0.04~0.10) | dataset_EmoFilM.md 8.1절 |

---

## 7. 미확인 항목 전체 목록

### 7.1 우리 환경 (사용자 입력 필요)
1. 네 데이터셋의 로컬 데이터 경로
2. 원본 자극 보유 여부: Horikawa 비디오, Emo-FilM 편집본, Spacetop `stimuli/`, NSD `nsd_stimuli.hdf5`
3. NSD Data Access Agreement 승인 보유 여부
4. 이미 추출한 feature/embedding, 계산 자원, pretrained checkpoint, 제약(마감, 데이터 사용 동의 범위)

### 7.2 Horikawa
5. Google Form 비디오 요청의 이용 조건(연구 목적 제한, 재배포, 라이선스, 승인 기간)과 개인 수준 평정 제공 여부
6. Mendeley 예치본의 파일 목록, 형식, 라이선스, 비디오 포함 여부
7. figshare 두 레코드의 라이선스
8. 2,196 제시 ID와 2,185개 라이브러리의 대응
9. 같은 원본 영상에서 잘린 클립 존재 여부(movie-level leakage)
10. 비디오당 dimension 평정자 수, 범주별 inter-rater reliability, category 평정 형식 원문 확인
11. Cowen & Keltner (2017) Discussion 세 방향의 원문 위치와 표현 (PNAS 본문 미열람)
12. vision 1000차원 feature의 DNN 이름, semantic 73 항목 목록
13. 표준공간 전처리본, 전처리 연속 시계열 존재 여부
14. fMRI 참가자 국적, 모국어
15. ds002425의 fMRI foundation model 사전학습 포함 여부
16. Fu 2024, EmoGrowth 2025, Shariatpanahi 2025의 Horikawa 데이터 사용 직접 서술

### 7.3 Emo-FilM
17. 논문 Table 1, Supplementary Table(항목별 agreement 등), Usage Notes 내용 (출판사 페이지 차단)
18. 최고·최저 agreement 항목명, 제외 항목과 영화의 r 값 대응
19. 영화별 CC 라이선스 조항, LIRIS-ACCEDE 입수 조건, 크레딧 절단 지점(`code/FilmInfo.txt`)
20. 평정, 생리 수치 분포와 결측 (annex 본체 미다운로드)
21. HBI, RV 회귀자 공개 여부, slice timing과 distortion correction 적용 여부
22. `LeassonLearned` 파일의 성격
23. Chan 2026, Morgenroth 2026 (Emotion), David 2025의 Emo-FilM 사용 본문 확인
24. "Higher-order topology ..." bioRxiv 2026 preprint의 저자와 본문, Radchenko preprint의 존재

### 7.4 Spacetop
25. alignvideo 49편의 원 제목, 출처, 저작권, 재사용 조건 (논문 Table 미열람)
26. `content-tornado` 두 파일의 동일 여부 (고유 영상 49 vs 48)
27. faces 자극 생성 출처, UNBC-McMaster와 Ganis & Kievit 자극 재배포 조건
28. 생리(EDA, PPG)와 설문의 공개 경로, NDA 컬렉션 존재 여부
29. 논문 N=101 산정 기준
30. 논문 기술 fMRIPrep 21.0.2 산출물 공개 여부
31. Miao 2026 별도 평정자 연속 평정 데이터 공개 여부
32. OpenNeuro 실제 다운로드 작동 여부 (네트워크 제약으로 미실행), arXiv:2606.09770 본문

### 7.5 NSD
33. NSD 원 논문 본문, Data Manual, Terms & Conditions 원문 (상업적 사용, 재배포, 파생 라벨 공유 조건)
34. DAA 승인 방식과 기간
35. nsdmeadows 지시문(felt vs perceived), 참가자별 원점수 배포 여부, 평정 주체 원문 확인
36. 나머지 4명의 세션 수, RT 형식, 생리 샘플링과 세션 목록, pupil 사용 가능성
37. 보류 세션의 현재 공개 상태, `cropBox` 정의, 이미지 픽셀 해상도, MNI 판 제공 여부
38. NSD 이미지와 BOLD5000, SentiCap의 COCO ID 중복

### 7.6 문헌 기록 관련
39. **(Stage 1에서 수정 완료)** 감사 에이전트들의 `verified_by` 표기 기준이 서로 달랐다. 검증 에이전트 지적(L1)에 따라 WebSearch 색인으로만 확인한 19편을 `verified_by: "search_index"`로 통일했고(원래 값은 `verified_by_original`에 보존), 검색 요약만 본 항목의 `discussion_read`를 `"search_summary"`로 바꿨다. 현재 dataset-auditor 문헌 57편 중 verified(PubMed 경로 확인) 38편, search_index 19편이다. `search_index`와 `search_summary`는 CLAUDE.md 5절 스키마에 없는 값이므로 Stage 2 에이전트에게도 같은 규칙을 알려야 한다. search_index 항목은 arxiv.org, doi.org 등이 허용되면 식별자 경로로 재확인한다.
40. Westlin et al. (2025) 본문, Cowen & Keltner (2017) PNAS 본문 (PMC 전문이 도구에서 빈 문자열로 반환). Cowen & Keltner Discussion 세 방향의 원문 확인은 Stage 2 emotion-theory 담당에게 넘긴다.
41. Cowen & Keltner (2017) abstract가 공개했다고 밝힌 비디오 라이브러리와 interactive map(s3-us-west-1.amazonaws.com/emogifs/map.html)의 형식(GIF 여부), 해상도, 이용 조건. Horikawa 비디오 요청 승인 전 임시 경로 후보다.
42. Emo-FilM 절단 정보 파일(`code/FilmInfo.txt`, xlsx)의 실제 내용과 공개 S3 다운로드 작동 여부.

---

## 8. 실행 환경 제약 (사실 기록)

* 셸의 외부 HTTP 접근은 egress proxy 정책으로 대부분 차단되었다. WebFetch도 doi.org, nature.com, openneuro.org, data.mendeley.com, pmc.ncbi.nlm.nih.gov, naturalscenesdataset.org, cvnlab.slite.page, registry.opendata.aws 등에서 실패했다.
* 감사 에이전트들은 PubMed MCP(PMC 전문 포함), WebSearch, 그리고 GitHub의 공개 저장소(OpenNeuroDatasets 미러, KamitaniLab, EllieMo/Emo-FilM, spatialtopology)를 git으로 읽는 방식으로 검증했다. OpenNeuro 미러는 메타데이터 텍스트만 읽었고 대용량 파일 본체는 내려받지 않았다.
* Horikawa 감사 에이전트가 검증용으로 공개 저장소를 프로젝트 폴더 밖(`/home/user/kamitanilab/`, `/home/user/openneurodatasets/ds002425`)에 clone했다. 이 사본은 저장소에 커밋되지 않으며 원격 컨테이너가 회수되면 사라진다.
* `.claude/agents/`의 커스텀 에이전트 타입은 이번 세션에 등록되지 않아, 각 역할은 general-purpose 에이전트가 해당 정의 파일을 직접 읽고 수행했다.

---

## 검증 반영 기록

검증: `outputs/agents/adversarial-reviewer/stage1_audit.md` (adversarial-reviewer 역할, 공개 저장소를 새로 받아 독립 대조, PMC 전문 12편 열람).

**결과 요약:** 결론과 Gate 판정을 뒤집는 수치 오류는 없었다. 핵심 수치(Horikawa 5명, 61 run, TR 2 s, 2020-04-24 OpenNeuro 공개; Emo-FilM 30명, 44명, 50항목, 0.38/0.39; Ma & Kragel 서지와 수치; Spacetop N=101 vs 117, 결측 48.7% 응답; NSD 서지와 사양; Sadeghi r = 0.22)는 독립적으로 확인되었다. 인용 표본 16편(시드 20261112)에서 식별자 오류 0, 내용 오류 0, 표기 오류 3(18.8%).

| 지적 | 심각도 | 반영 |
|---|---|---|
| X1: 3.2절이 NSD를 "규범 vs 본인" 비교 가능 데이터셋으로 서술 (NSD에는 규범 평정 없음) | 높음 | 반영. 3.2절, 5.4 #2, 5.5 #1 수정 |
| L1: 검색 색인 확인을 verified로 표기한 jsonl 항목 | 높음 | 반영. 19편을 `search_index`로 재표기, `discussion_read` 기준 통일, arXiv:2509.24298 저자 표기 통일 (7.6절 39번) |
| E8, X7: Emo-FilM G1 | 중간 | 반영. "공개 재료로 재구성 가능성 높음(확인 필요)"으로 재표기, 이견 병기 |
| N5: NSD G1 | 중간 | 반영. "약관 동의 절차 필요(승인 심사 여부 미확인)"로 재표기, 양쪽 근거가 검색 수준임을 병기 |
| H11: Westlin 2025 "반대 결론" 과장 | 중간 | 반영. preprint, 초록 기준, 재현 실패 보고로 수정 (0절, 4.1, 5.1) |
| N4: nsdmeadows 평정 주체 단정 | 중간 | 반영. 0절 2번, 1절 표, 3.2절에 근거 수준과 지시문 미확인 명시 |
| S10: 서로 다른 신뢰도 지표를 한 행에 나란히 둠 | 중간 | 반영. 비교 불가 명시, Spacetop 개인 수준 값 병기 |
| 4.3: Spacetop AI 연속 주석의 시간 타당화 공백 | 중간 | 반영. 5.3 #3에 Emo-FilM 1 Hz consensus 선검증 경로 명시 |
| L3: Gao 2025 "대부분 예측" 과장 | 낮음~중간 | 반영. 4.4 표현 수정 |
| X2, X3, X4: 3.2 표의 지각/귀속 혼합, 이분법 판정, 문서 간 판정 차이 | 낮음~중간 | 반영. 3.2 표에 타인 지각/귀속 열 추가, 3.1에 단계형 판정 도입, 판정 차이 기록 |
| H6, H7, E11: 중복 15개 표현, abstract 2,185, S07 결측 범위 | 낮음 | 반영. 1절 표, 6절 |
| H10: Horikawa G1 대안 후보(공개 interactive map) | 낮음 | 반영. `gate_decision.md` 2.3절, 7.6절 41번 |
| L6: Higher-order topology preprint 부분 겹침 | 낮음 | 반영. 5.2 #1 |

**채택한 이견:** Emo-FilM G1, NSD G1, Westlin 위상, `verified_by` 즉시 수정, 단계형 판정 모두 검증 에이전트 의견을 채택했다. 다만 Emo-FilM G1과 NSD G1은 검증 에이전트의 근거도 파일 위치 기록과 검색 색인 수준이라 확정이 아니며, 감사 에이전트의 원래 판정과 함께 기록해 두었다(`stage1_audit.md` 5절).

**데이터셋 보고서 반영:** 각 `dataset_*.md` 맨 위에 "Coordinator 주석 (Stage 1 검증 반영)" 블록을 두어 이 문서와 달라진 판정과 표현을 표시했다. 데이터셋 보고서 본문은 감사 당시 기록으로 남긴다.
