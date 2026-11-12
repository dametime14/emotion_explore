# Dataset Audit: Natural Scenes Dataset (NSD)

* 작성: dataset-auditor (Agent 1, Dataset & Metadata Specialist). 독립 에이전트 타입이 등록되지 않아 general-purpose 에이전트가 `.claude/agents/dataset-auditor.md` 지침을 직접 읽고 수행함.
* 기준일: 2026-11-12
* 원 논문: Allen EJ, St-Yves G, Wu Y, ... Naselaris T, Kay K (2022). A massive 7T fMRI dataset to bridge cognitive neuroscience and artificial intelligence. *Nature Neuroscience* 25(1):116-126. doi:[10.1038/s41593-021-00962-x](https://doi.org/10.1038/s41593-021-00962-x), PMID [34916659](https://pubmed.ncbi.nlm.nih.gov/34916659/) (온라인 게재 2021-12-16). Preprint: bioRxiv doi:[10.1101/2021.02.22.432340](https://doi.org/10.1101/2021.02.22.432340)
* 우리 환경의 데이터 경로: **미확인** (`reference/datasets_and_resources.md` 1절이 비어 있음)

> **Coordinator 주석 (Stage 1 검증 반영, `outputs/agents/adversarial-reviewer/stage1_audit.md`)**
> * N5 (이견 병기): 검색 색인의 AWS Registry 항목은 S3 버킷을 무계정(`--no-sign-request`)으로 안내하면서 Data Manual 접근에 DAA 양식을 요구한다. 그래서 통합 보고서와 `gate_decision.md`는 G1을 "약관 동의 절차 필요(요청 범주, 승인 심사 여부 미확인)"로 표기한다. 감사 판정과 검증 의견 모두 검색 수준 근거라 Terms 원문 확인이 필요하다.
> * N4: nsdmeadows 평정 주체가 NSD 참가자라는 근거는 Khosla 2022의 "subject-averaged" 표현과 검색 요약이다. 지시문(felt vs perceived) 미확인이므로 "본인 보고"는 잠정 분류다.
> * X1: NSD에는 별도 평정자의 규범 평정이 없다. 8절 2번의 "규범 평정" 비교는 shared 이미지에 대한 신규 규범 평정 수집이 전제다.
> * L3: 6절 표의 "일상 장면의 정서 평정은 객체 표상으로 대부분 예측됨"은 과장이다. 2.4절 (d)의 표현처럼 "객체 인식 모델(AlexNet)이 정서 특화 모델(EmoNet)보다 20개 범주 정서 판단을 더 잘 예측했다(20-way 분류 정확도 기준, 절대 설명량은 크지 않음)"로 읽는다.
> * 문헌 기록: `literature_NSD.jsonl`에서 WebSearch 색인으로만 확인한 11편(arXiv 7, bioRxiv 2, AAAI 1, VSS 초록 1)을 `verified_by: "search_index"`로 재표기했고, 검색 요약만 본 항목은 `discussion_read: "search_summary"`로 바꿨다.
> * Stage 2 재점검(같은 감사 에이전트, 네트워크 허용 후): 위 11편은 arXiv API(8편)와 Crossref(3편)로 존재를 직접 확인해 verified로 되돌렸다. 부록 A와 B의 "VSS 2025 초록, DOI 없음"은 사실과 다르며 DOI는 10.1167/jov.25.9.1989다. already_done "미확인" 15개는 모두 재검색해 partially 8, no 7로 판정했다.

## Gate 판정

| Gate | 판정 (공개 경로 기준) | 우리 환경 보유 여부 | 핵심 근거 |
|---|---|---|---|
| **G1** 원본 자극 접근 | **요청 필요.** NSD Data Access Agreement 양식을 제출해야 Data Manual과 배포본(AWS S3)에 접근하는 구조이며, 배포본에 제시 이미지 73,000장을 담은 `nsd_stimuli.hdf5`가 있다 [B]. 승인 방식(자동 또는 심사)과 소요 기간은 미확인. 별도 경로로 COCO 원본 이미지는 공개되어 있어 `cocoId`와 `cropBox` 메타데이터로 제시 영상을 재구성할 수 있을 것으로 보인다 [B] (`cropBox` 정의는 미확인, 메타데이터 파일 자체는 NSD 배포본에 있음). 따라서 "불가"는 아니다. | **미확인** | AWS Registry 요약 [B], Algonauts 2023 포럼 [B], NSD 제시 이미지가 COCO의 정사각형 crop이라는 서술 (Doerig et al. 2025) [A] |
| **G2** fMRI 형식과 전처리 수준 | **고수준 전처리 완료.** 원시 데이터(BIDS)와 prepared data 제공 [B]. 전처리 시계열은 1.8 mm (1.333 s 재표집)와 1.0 mm 업샘플 (1.0 s) 두 종류 [A]. GLMsingle 계열 single-trial beta (version 3 = `betas_fithrf_GLMdenoise_RR`, 단위 % signal change)가 1.8 mm volume과 fsaverage surface로 제공 [A]. pRF/fLoc 기반 ROI 제공 [A]. | **미확인** | Gifford et al. 2026 [A], Doerig et al. 2025 [A], Prince et al. 2022 [A] |
| **G3** 라벨과 평정 주체 | **정서 라벨은 기본 제공되지 않는다** (core 실험 기준). 유일한 공식 정서 관련 라벨은 `nsdmeadows`의 valence/arousal 평정으로, shared 이미지 100장 (+3장)에 대해 **NSD 참가자 본인이 스캔 종료 후 스캐너 밖에서** 1차원 drag-and-drop 배치로 평정했다 [A: 100장, 공식 배포, 참가자 평균 사용 / B: 평정 주체와 방식]. 그 밖의 라벨은 COCO captions (이미지당 5개, 크라우드 작업자 작성, NSD 참가자 아님) [A]와 COCO object category [A]. 73k 규모의 정서 라벨은 외부 모델 추정(AI) 또는 신규 인간 평정 수집이 필요하다. | **미확인** | Khosla et al. 2022 [A], Sadeghi et al. 2024 [A], Doerig et al. 2025 [A], NSD 원문 구절 [B] |

### 근거 등급과 검증 경로의 한계

* **[A]** PubMed 메타데이터 또는 PMC 전문에서 직접 확인한 사실.
* **[B]** WebSearch 색인 요약으로만 확인한 사실. 원문 페이지를 직접 열지 못했다.
* **[C]** 위 사실들로부터의 계산 또는 추론. 원문 확인이 아니다.
* 이번 세션에서 WebFetch가 `naturalscenesdataset.org`, `cvnlab.slite.page`(NSD Data Manual, Terms & Conditions), `registry.opendata.aws`, `www.nature.com` 모두에서 차단되었다 (호스트 미해석). 따라서 **NSD 원 논문 본문, Data Manual, Terms & Conditions 원문을 직접 읽지 못했다.** NSD 원문 PMC 사본도 없다 (PMID 34916659에 PMCID 없음). NSD 사양 수치는 (i) PubMed 초록, (ii) NSD를 기술한 PMC 전문 논문들 (Doerig 2025, Gifford 2026, Khosla 2022, Sadeghi 2024, Pennock 2023), (iii) WebSearch 요약에 근거한다. 사용자가 위 호스트를 허용하면 [B] 항목을 원문으로 재검증해야 한다.

---

## 1. Verified Dataset Specification

| 항목 | 값 | 출처 | 등급 |
|---|---|---|---|
| 참가자 | 8명 (건강한 성인) | Doerig et al. 2025, Nat Mach Intell, doi:[10.1038/s42256-025-01072-0](https://doi.org/10.1038/s42256-025-01072-0) Methods; Pennock et al. 2023 초록 | A |
| 세션 | 참가자당 NSD core 30~40 세션, 약 1년에 걸쳐 수집 | Doerig 2025; Sadeghi et al. 2024, doi:[10.1038/s41467-024-53668-6](https://doi.org/10.1038/s41467-024-53668-6) | A |
| 40 세션 완료자 | subj01, 02, 05, 07 (decoding 연구가 관례적으로 이 4명만 사용) | 다수 NSD 사용 논문 (WebSearch 요약) | B |
| 나머지 4명 세션 수 | 미확인 (30~32로 알려져 있으나 원문 미확인). 원문 구절의 "행동 응답 누락 2/3,408 run"이 run 총수 3,408이면, 세션당 12 run 가정 시 총 284 세션이 되어 40+40+32+30+40+32+40+30과 정합 | WebSearch 요약 + 계산 | B/C |
| 스크리닝 세션 | 7T `prffloc` 세션 (pRF, fLoc localizer) | NSD 원문 구절 (WebSearch) | B |
| Trial 수 | 참가자당 22,000~30,000 trial; "up to 30,000 trials" | NSD 원문 초록 구절 (WebSearch) [B]; Pennock et al. 2023, Curr Biol, doi:[10.1016/j.cub.2022.11.063](https://doi.org/10.1016/j.cub.2022.11.063) [A] | A/B |
| 고유 이미지 | 참가자당 9,000~10,000장, 이미지당 3회 반복 제시 설계; 전체 풀 73,000장 | Doerig 2025 | A |
| 실제 제시된 고유 이미지 총수 | 70,566장 (일부 참가자가 세션을 다 채우지 못함) | NSD 원문 구절 (WebSearch) | B |
| Shared 이미지 | 1,000장 (`shared1000`)을 전 참가자가 공유, 나머지는 참가자 간 상호 배타. 8명 모두 3회씩 본 이미지는 515장 (`shared515`) | Doerig 2025; Gifford et al. 2026, Nat Commun, doi:[10.1038/s41467-026-69345-9](https://doi.org/10.1038/s41467-026-69345-9) | A |
| 자극 제시 | 3 s ON, 1 s OFF, rapid event-related | Doerig 2025; Gifford 2026 | A |
| 자극 크기 | 중앙 8.4° x 8.4° | Gifford 2026 (NSD-core 자극 크기 언급) | A |
| 이미지 처리 | COCO 이미지의 정사각형 crop. 픽셀 해상도는 미확인 | Doerig 2025 Methods | A |
| 과제 | Long-term continuous recognition: 각 이미지가 처음 본 것(new)인지 이전에 본 것(old)인지 버튼으로 판단, 중앙 fixation 유지 | Doerig 2025; Gifford 2026 | A |
| 스캐너 | 7T Siemens Magnetom (passively shielded), 32-channel receive head coil (Nova Medical), CMRR, University of Minnesota | Gifford 2026 (NSD-synthetic 세션 기술, 동일 참가자와 장비) | A |
| EPI | Gradient-echo, whole-brain, 1.8 mm isotropic, TR 1.6 s | Doerig 2025 (NSD-core) | A |
| EPI 세부 | 84 axial slices, TE 22.0 ms, partial Fourier 7/8, iPAT 2, multiband 3 | Gifford 2026 (NSD-synthetic 세션 기준. NSD-core 동일 여부는 원문 미확인) | A |
| 전처리 | 1회 temporal resampling (slice timing) + 1회 spatial resampling (motion, EPI distortion, gradient nonlinearity). 1.8 mm 판(1.333 s)과 1.0 mm 업샘플 판(1.000 s) | Gifford 2026 Methods | A |
| Single-trial beta | GLMsingle 방법(HRF library, GLMdenoise, ridge regression). version 3 = `betas_fithrf_GLMdenoise_RR` (% signal change). version 1, 2의 정확한 파일명은 미확인 | Prince et al. 2022, eLife, doi:[10.7554/eLife.77599](https://doi.org/10.7554/eLife.77599); Gifford 2026; Doerig 2025 | A |
| 표상 공간 | Volume: 1.8 mm (Doerig 2025 사용), 1.0 mm; Surface: fsaverage (Gifford 2026 사용), FreeSurfer native surface. MNI 판 제공 여부 미확인 | Gifford 2026; Doerig 2025 | A |
| ROI | pRF/fLoc 기반 V1, V2, V3, hV4, EBA, FFA, PPA, VWFA 등; `streams` ROI; `nsdgeneral` mask | Gifford 2026 [A]; Doerig 2025 [A]; WebSearch [B: nsdgeneral] | A/B |
| 기타 MRI | Resting-state, diffusion 포함 | PubMed 초록 | A |
| 해부 영상 | T1, T2, diffusion, SWI, TOF | NSD 원문 구절 (WebSearch) | B |
| 생리 신호 | Pulse oximeter, respiratory belt. 참가자당 약 10 세션 | NSD 원문 구절 (WebSearch) | B |
| Eye-tracking | EyeLink 1000, 참가자당 2~4 세션, pupil contrast 문제로 품질이 고르지 않음 | NSD 원문 구절 (WebSearch) [B]; Gifford 2026 (NSD-core 논문 참조와 품질 경고) [A] | A/B |
| 행동 응답 누락 | 3,408 run 중 2 run (0.06%) | NSD 원문 구절 (WebSearch) | B |
| 보류 세션 | 초기 공개 시 참가자별 마지막 3 세션(약 8.4%) 보류, Algonauts 2023 test set으로 사용 | NSD 원문 구절 (WebSearch); Gifford et al. 2023, arXiv:[2301.03198](https://arxiv.org/abs/2301.03198) | B |
| 보류 세션 공개 | MindEye2 본문이 "Algonauts 2023 종료 후 전체 데이터 공개"를 서술. 공식 changelog는 미확인 | Scotti et al. 2024, arXiv:[2403.11207](https://arxiv.org/abs/2403.11207) (WebSearch 요약) | B |
| 추가 데이터셋 1 | **NSD-synthetic**: 같은 8명, 1 세션, 합성 이미지 284장 (8 class, 71 subclass), 2 s ON / 2 s OFF, fixation task와 one-back task를 run마다 교대 (총 8 run), beta = `nsdsyntheticbetas_fithrf_GLMdenoise_RR` | Gifford 2026 | A |
| 추가 데이터셋 2 | **NSD-Imagery**: 같은 8명의 7T 심상 과제 데이터 (vision, imagery, attention 조건), CVPR 2025 | Kneeland et al. 2025, arXiv:[2506.06898](https://arxiv.org/abs/2506.06898) (WebSearch 요약) | B |
| 추가 데이터셋 3 | **nsdmeadows**: 스캔 종료 후 Meadows 웹 플랫폼 행동 과제. valence/arousal 평정 (아래 2절) | Khosla et al. 2022 [A]; NSD 원문 구절 [B] | A/B |
| 접근 절차 | NSD Data Access Agreement 양식 제출 후 Data Manual 접근, 데이터는 AWS S3 호스팅, 사용은 NSD Terms & Conditions에 따름 | AWS Registry ([registry.opendata.aws/nsd](https://registry.opendata.aws/nsd)) 요약 | B |
| 라이선스 (NSD) | Terms & Conditions 원문 미열람. **상업적 사용 제한, 재배포 제한 조항은 미확인** | ([cvnlab.slite.page](https://cvnlab.slite.page) 접근 차단) | 미확인 |
| 라이선스 (COCO) | Annotation은 CC BY 4.0. COCO Consortium은 이미지 저작권을 보유하지 않으며 이미지 사용은 Flickr Terms of Use를 따름 | cocodataset.org Terms of Use의 2차 사본 (WebSearch) | B |

## 2. Complete Metadata & Annotation Inventory

### 2.1 자극 메타데이터

| 항목 | 존재 | 내용 | 작성 주체 | 출처 | 등급 |
|---|---|---|---|---|---|
| 시각 자극 | 있음 | COCO 자연 장면 73,000장 (정사각형 crop, 컬러) | COCO (Flickr 수집) | Doerig 2025; Lin et al. 2014, arXiv:[1405.0312](https://arxiv.org/abs/1405.0312) | A |
| 오디오, 음악, 음성 | 해당 없음 | 정지 이미지 자극 | - | Doerig 2025 (과제 기술) | A |
| Captions | 있음 | 이미지당 COCO 캡션 5개 | 크라우드 작업자 (NSD 참가자 아님) | Doerig 2025; Chen et al. 2015, arXiv:[1504.00325](https://arxiv.org/abs/1504.00325) | A/B |
| Caption과 제시 영상 불일치 | 주의 | NSD 제시 시 crop으로 원 캡션, bounding box가 실제 제시 영상과 어긋나는 경우가 있어 재주석한 연구가 있음 | - | Neuro-Vision to Language, arXiv:[2404.19438](https://arxiv.org/abs/2404.19438) (WebSearch 요약) | B |
| Object category | 있음 | COCO category label (multi-hot), instance segmentation | COCO 주석자 | Doerig 2025 (multi-hot 사용) | A |
| 메타데이터 파일 | 있음 | 73,000행 stimulus info CSV: `cocoId`, `cropBox`, `shared1000` 플래그 등 | NSD 팀 | hulacon MMMData 문서, Algonauts 포럼 (WebSearch) | B |
| 시간 정렬 | 있음 | trial 단위 (3 s 제시) 설계 정보, single-trial beta로 이미 정렬됨 | NSD 팀 | Doerig 2025; Gifford 2026 | A |

### 2.2 행동, 평정, 생리 데이터

| 항목 | 존재 | 범위 | 평정/측정 주체 | 시간 해상도 | 출처 | 등급 |
|---|---|---|---|---|---|---|
| Recognition 판단 (old/new) | 있음 | 모든 NSD core trial | fMRI 참가자 본인 | trial 단위 | Doerig 2025; Gifford 2026 | A |
| 반응시간 | 버튼 응답 존재. RT 배포 형식은 미확인 | - | 참가자 | trial | - | 미확인 |
| **nsdmeadows valence** | 있음 | shared 이미지 100장 (+515 세트에서 3장 추가) | **NSD 참가자 본인**, 스캔 종료 후 | 이미지 단위 (스캔 중 아님) | Khosla 2022 [A: 100장, 공식 배포, "subject-averaged" 사용]; NSD 원문 구절 [B: 참가자, 방법] | A/B |
| **nsdmeadows arousal** | 있음 | 위와 동일 | 위와 동일 | 위와 동일 | 위와 동일 | A/B |
| 평정 방식 | - | 차원별로 따로, 작은 묶음의 이미지를 low~high 1차원 축 위에 drag-and-drop으로 자유 배치 | - | - | NSD 원문 구절 (WebSearch) | B |
| 평정 지시문 (느낀 정서 vs 이미지의 정서 판단) | **미확인** | - | - | - | - | 미확인 |
| 참가자별 원점수 배포 여부 | **미확인** (Khosla 2022는 참가자 평균값 사용) | - | - | - | Khosla 2022 | A/미확인 |
| Meadows 유사도 배치 과제 | 존재하는 것으로 보임 ("similar interface"라는 원문 구절). 세부 미확인 | - | 참가자 | - | WebSearch | B |
| 스캔 후 최종 기억 검사 | **미확인** | - | - | - | - | 미확인 |
| Pulse, respiration | 있음 | 참가자당 약 10 세션 | 생리 측정 | 연속 신호 (샘플링 미확인) | WebSearch | B |
| Eye-tracking / pupil | 있음 | 참가자당 2~4 세션, 품질 가변 | 생리 측정 | 연속 신호 | WebSearch [B]; Gifford 2026 [A] | A/B |
| Resting-state | 있음 | 세션 배치, run 수 미확인 | - | TR 1.6 s | PubMed 초록 | A |

### 2.3 정서 정보의 출처 구분 (CLAUDE.md 6절)

| 구분 | NSD에서의 상태 | 비고 |
|---|---|---|
| **실제 관찰된 정서** (스캔 중 측정한 행동, 생리 지표) | **직접 지표 없음.** 간접 후보는 pulse/respiration (약 10 세션/인)과 pupil (2~4 세션/인, 품질 가변) | 생리 신호와 이미지 정서의 관계를 검증한 NSD 연구는 이번 검색에서 찾지 못함. 과제가 기억 과제이므로 각성 지표는 novelty, 기억 부하와 섞인다 |
| **fMRI 참가자 본인이 보고한 정서** | nsdmeadows valence/arousal, 100(+3)장, 스캔 후 스캐너 밖 | 스캔 중 trial 단위 보고는 없음. 같은 참가자의 뇌 반응과 연결 가능한 유일한 정서 자기보고. 지시문이 "느낀 정서"인지 "이미지의 정서적 속성 판단"인지 미확인이므로 felt vs perceived 구분 불가 |
| **별도 평정자의 규범적 평정** | NSD 공식 제공 없음 | 외부 후보: Gao et al. 2025는 BOLD5000 이미지 4,913장(COCO 2,000장 포함)에 20개 정서 범주 평정 수집. NSD 이미지와의 COCO ID 중복 여부 미확인. Khosla 2022의 salience 평정(얼굴, 장면, 글자, 신체, 음식)은 별도 평정자 자료지만 정서 평정이 아님 |
| **자극에 표현된 정서** | 별도 주석 없음 | COCO 캡션에 정서 어휘가 섞일 수 있으나 빈도 미확인. 얼굴 표정 주석 없음. SentiCap (Mathews et al. 2016)이 COCO 일부 이미지의 캡션을 긍정/부정 문체로 다시 쓴 자료가 있으나 NSD 이미지와의 중복 미확인 |
| **AI가 추정한 정서** | 공식 제공 없음. 선행연구 사례: Sadeghi 2024의 visual valence (VV) 모델 예측값을 NSD 전체 이미지에 적용 | EmoNet (Kragel et al. 2019), VLM/LLM 평정 (GPT-4 계열) 적용 가능. NSD 이미지 전체에 LLM/VLM 정서 주석을 붙인 동료심사 논문은 이번 검색 범위에서 찾지 못함 |

### 2.4 정서 라벨 파생 가능성 (위임 메시지 3번 항목)

**(a) COCO 캡션과 객체 라벨에서 파생.** 기술적으로 가능하다 (텍스트 sentiment 분석, LLM 평정, 객체 범주별 정서 사전). 그러나 근거가 약하다. Doerig 2025는 NSD 캡션에서 형용사, 부사의 뇌 정렬이 매우 낮았고 NSD 캡션은 주로 명사, 동사로 내용을 기술한다고 보고했다 [A]. 즉 캡션은 정서 어휘가 희박한 "사실 기술"이며, 캡션 기반 정서 점수는 의미 내용(semantic content)의 재표현이 될 위험이 크다. 또한 crop 때문에 캡션이 실제 제시 영상과 어긋날 수 있다 [B].

**(b) 외부 모델로 affective annotation을 만든 선행연구.**
* NSD에 직접 적용: Sadeghi et al. 2024 (Nat Commun). 저수준 이미지 통계 기반 VV 모델(약 8,000장의 정서 사진으로 학습)을 NSD 이미지에 적용하고, 8명 group 분석에서 VV가 주로 시각 영역에 표상된다고 보고. 같은 NSD로 학습된 NeuroGen으로 VV+/VV- 영상을 합성 [A].
* NSD로 학습한 encoding model을 정서 자극에 역적용 (in-silico): Chen, Keil, Ding, VSS 2025 초록. NSD 학습 encoding model로 IAPS 장면을 넣었을 때 early visual cortex에서 정서 vs 중립 decoding 불가, AffectNet 얼굴은 가능 [B, 학회 초록만 확인].
* NSD 외 데이터에서 LLM 주석의 뇌 수준 타당성: Santavirta et al. 2025 (Imaging Neurosci)는 GPT-4V의 138개 사회적 특징 평정이 인간 평균과 r = 0.79, 이를 이용한 fMRI 모델이 인간 평정 기반 모델과 유사한 뇌 지도를 낸다고 보고 [A].

**(c) NSD 이미지에 대한 인간 정서 평정 공개 자료.** 공식 자료는 nsdmeadows (100+3장, NSD 참가자)뿐이다. 그 외 NSD 이미지 대상 valence/arousal 규범 평정 자료는 이번 검색에서 찾지 못했다. BOLD5000의 COCO 부분 이미지에 대한 정서 범주 평정(Gao et al. 2025)은 NSD와 중복 여부를 COCO ID로 확인해야 한다 (미확인).

**(d) 파생 라벨 타당성의 찬반 근거.**

| 방향 | 근거 | 등급 |
|---|---|---|
| 지지 | GPT-4o 평정이 OASIS 인간 평정과 valence r ≈ 0.89, arousal r ≈ 0.81 (Ogg et al. 2025, arXiv:2508.14214) | B |
| 지지 | GPT-4가 GAPED 영상의 valence/arousal을 zero-shot으로 인간 평정에 근접하게 분류 (Alrasheed et al. 2025, PLoS ONE) | A |
| 지지 | GPT-4V 사회적 특징 주석이 인간 주석과 r = 0.79, 뇌 지도 수준에서도 수렴 (Santavirta et al. 2025) | A |
| 지지 | EmoNet이 영상 내용만으로 규범 정서 범주와 valence를 예측 (Kragel et al. 2019) | A |
| 지지 (약함) | VV 모델 예측이 nsdmeadows valence 100장과 r = 0.22, p = 0.028 (Sadeghi 2024) | A |
| 반박/제약 | **NSD 이미지는 대부분 valence가 중립에 가깝다** (Sadeghi 2024의 서술). 범위 제한으로 AI 라벨의 신뢰도와 검정력이 낮아진다 | A |
| 반박/제약 | 일상 장면의 정서 평정은 객체 범주 표상(AlexNet)이 정서 특화 모델(EmoNet)보다 더 잘 예측. 정서 정보가 객체 인식 체계에 실려 있음 (Gao et al. 2025, BOLD5000). NSD 같은 일상 장면에서 AI 정서 라벨은 의미 내용과 공선성이 높을 가능성 | A |
| 반박/제약 | LLM 평정은 인간보다 균질하고, arousal 정렬이 가장 약함 (Ogg 2025) | B |
| 반박/제약 | GPT-4V는 낮은 강도, 추상적, 추론적 특징에서 인간 일치도가 낮고, 성적/폭력 내용은 content filter로 평정 거부 (Santavirta 2025) | A |
| 반박/제약 | 미묘한 정서 단서 분류에 어려움 (Alrasheed 2025) | A |
| 반박/제약 | 복잡한 사회적 장면의 valence는 시각 특징이나 장면 맥락만으로 설명되지 않음. 시각 모델은 장면 맥락 valence에 의존 (Yargholi et al. 2025, bioRxiv) | B |
| 반박/제약 | NSD의 음식 선택적 성분이 nsdmeadows valence/arousal과 유의한 상관이 없었음 (Khosla 2022, n = 100). 시각 범주 선택성과 정서가 같은 것이 아님 | A |

**결론:** AI 파생 정서 라벨은 정서 사진 세트(IAPS, OASIS, GAPED, NAPS)에서 검증되었고, **COCO 일상 장면이나 NSD 이미지에서 인간 평정으로 검증된 사례는 nsdmeadows 100장(r = 0.22, 저수준 VV 모델)뿐이다.** 따라서 NSD에서 AI 정서 라벨은 "AI가 추정한 자극의 정서적 속성"으로만 해석해야 하며, 참가자의 경험 정서로 해석하면 안 된다.

## 3. Available vs Missing Information

### 있는 것
* 대규모 single-trial 7T 반응 (참가자당 최대 30,000 trial), 반복 3회, shared515로 noise ceiling 추정 가능 [A]
* COCO 캡션 5개, 객체 범주, segmentation [A]
* 참가자 본인의 old/new 기억 판단 (trial 단위) [A]
* 참가자 본인의 valence/arousal 평정 (100+3장, 스캔 후) [A/B]
* 생리 신호 (일부 세션), eye-tracking (일부 세션) [B]
* Resting-state, diffusion, 해부 영상 [A/B]
* OOD 확장: NSD-synthetic [A], NSD-Imagery [B]

### 없는 것
* 스캔 중 trial 단위 정서 자기보고 (없음)
* 73k 이미지에 대한 정서 범주, valence/arousal 규범 평정 (없음)
* 이산 정서 범주 라벨, appraisal 라벨 (없음)
* 오디오, 음악, 언어 자극 (해당 없음)
* 정서 유발을 목적으로 한 자극 선택 (없음. 이미지는 대체로 정서적으로 중립)
* 연속 시간 정서 동역학 (정지 이미지, 3 s 제시)

### 미확인
* 우리 환경의 데이터 경로, 원본 자극 보유 여부, 추출된 feature
* NSD Terms & Conditions 원문 (상업적 사용 제한, 재배포 제한, 파생 데이터 공유 조건)
* Data Access Agreement 승인 방식과 소요 기간
* nsdmeadows 평정 지시문, 참가자별 원점수 배포 여부, 평정 척도 변환 방식, 3장 추가 이미지의 용도
* 나머지 4명의 정확한 세션 수, 세션당 run/trial 수
* 반응시간 배포 형식, 스캔 후 최종 기억 검사 존재 여부
* 생리 신호 샘플링 속도와 세션 목록, pupil 데이터 사용 가능성
* Resting-state run 배치
* MNI 공간 판 제공 여부, beta version 1과 2의 파일명
* 보류 세션의 현재 공개 상태 (공식 확인)
* NSD 이미지와 BOLD5000, SentiCap 이미지의 COCO ID 중복
* 이미지 픽셀 해상도, `cropBox` 정의와 좌표 규약

## 4. Potential Modeling Tasks

| 과제 | NSD에서의 가능성 | 필요한 것 | 주된 위험 |
|---|---|---|---|
| Vision decoding / reconstruction | 매우 높음. 이 분야의 표준 benchmark (MindEye2 등) | 공개 beta | 정서와 무관 |
| Emotion decoding | **제한적.** 참가자 보고 라벨은 100장뿐. 73k 규모는 AI 라벨 decoding이 되며 이는 "모델이 정의한 정서 축의 decodability"에 불과 | AI 라벨 + 인간 검증 | 범위 제한, semantic 공선성, decoding을 경험 정서로 과해석 |
| Semantic decoding | 높음. LLM 캡션 embedding으로 brain-to-caption 가능 (Doerig 2025) | 캡션 | crop 불일치 |
| Encoding (정서 특징 고유 분산) | 가능. affect 특징(AI 라벨)과 의미 특징(LLM caption embedding, 객체 범주)을 함께 넣은 variance partitioning | AI 라벨, LLM embedding | 공선성, 다중비교, ROI 순환추론 |
| Multimodal alignment | 높음. 이미지, 캡션, 뇌 3자 정렬. VLM 정서 평정을 같은 공간에 투영 | VLM 접근 | pretrained 모델의 COCO 학습 오염 |
| Brain Foundation Model adaptation | 높음. NSD는 다수 모델의 사전학습/평가 데이터 | 체크포인트 | NSD로 사전학습된 모델을 NSD 정서 분석에 쓰면 누수 |
| Temporal representation | 낮음. 정지 이미지 3 s, TR 1.6 s. 다만 세션에 걸친 반복(기억) 시간축은 있음 | 설계 정보 | HRF 중첩, 반복 억제 |
| Generative modeling | 가능. NeuroGen, BrainDiVE 류의 뇌 유도 영상 합성을 정서 목적 함수로 확장 (Sadeghi 2024가 VV로 일부 수행) | encoding model, generator | in-silico 예측을 관찰 결과로 혼동 |
| Cross-subject transfer | 높음. shared1000/515 | - | n = 8 |
| Cross-dataset transfer | 가능. NSD 학습 encoding model을 IAPS, Horikawa 자극, Emo-FilM 프레임에 적용 (in-silico) | 타 데이터셋 자극 | 도메인 이동, 과제 차이 |
| AI-generated annotation | 가능성 높고 저비용. 73k 이미지 VLM 평정 + shared1000 인간 평정으로 보정 | VLM, 평정자 모집 | 2.4절 (d)의 타당성 제약 |

## 5. Unique Advantages

1. **규모와 품질:** 참가자당 약 10,000장, 3회 반복, 7T 1.8 mm 단일 trial 반응 [A]. 정서 효과가 작아도 이미지 수로 검정력을 확보할 여지가 있다.
2. **같은 참가자의 뇌 반응과 자기보고 valence/arousal의 연결:** 100장으로 작지만, 별도 평정자가 아닌 fMRI 참가자 본인의 평정이라는 점이 드물다 [A/B].
3. **기억 과제:** trial 단위 recognition 판단이 있어 정서(특히 arousal)와 기억의 상호작용을 연구할 수 있다. NSD로 recognition memory 신경기제를 다룬 최근 연구가 활발하다 (Sheng et al. 2026 PNAS; Bai & Coutanche 2026 NeuroImage) [A].
4. **풍부한 비정서 메타데이터:** 캡션, 객체 범주, segmentation 덕분에 정서와 의미 내용을 통계적으로 분리하는 통제 변수를 바로 만들 수 있다 [A].
5. **OOD와 심상 확장:** NSD-synthetic, NSD-Imagery로 정서 관련 encoding model의 일반화나 심상 조건을 시험할 수 있다 [A/B].
6. **모델 생태계:** encoding, decoding, generative 모델(NeuroGen, MindEye2 등)이 NSD 위에 이미 구축되어 있어 in-silico 실험 비용이 낮다 [A/B].

## 6. Methodological Limitations

| CLAUDE.md 6절 항목 | NSD에서의 구체적 문제 | 근거 |
|---|---|---|
| Emotion experienced vs portrayed | 스캔 중 정서 경험 측정이 없다. 모든 73k 규모 정서 분석은 "자극 속성" 수준이다 | 2.3절 |
| Human vs model annotation | 73k 규모 라벨은 AI 추정뿐. 인간 검증은 100장 | Sadeghi 2024 |
| 참가자 보고 vs 규범 평정 | nsdmeadows는 참가자 평정이지만 스캔 후, 비교 배치 방식이라 척도가 상대적이다. 지시문 미확인 | [B] |
| Emotion vs visual/semantic content | 일상 장면에서 객체 인식 모델(AlexNet)이 정서 특화 모델(EmoNet)보다 20개 범주 정서 판단을 더 잘 예측함 (Gao 2025, 20-way 분류 정확도 기준, 절대 설명량은 크지 않음). OTC는 animacy와 affect를 함께 부호화 (Abdel-Ghaffar et al. 2024). 정서 축이 의미 축의 재표현일 가능성 | [A] |
| 범위 제한 | 이미지가 대체로 중립 (Sadeghi 2024) | [A] |
| Repeated stimulus confound | 각 이미지가 수 세션에 걸쳐 3회 제시되며 과제가 old/new 판단. 반복 억제, 친숙도, novelty 반응이 arousal 성격의 신호와 섞인다. Abdel-Ghaffar 2024는 amygdala처럼 novelty에 민감한 영역은 반복 제시 기반 voxel-wise 모델 적합이 어렵다고 지적 | [A] |
| HRF와 autocorrelation | 4 s 간격 rapid design. GLMsingle이 인접 trial 상관을 줄이지만 완전 제거는 아님 | Prince 2022 [A] |
| Leakage | shared 이미지가 참가자 간 공통. COCO로 학습된 CLIP, VLM, 캡션 모델을 쓰면 이미지 수준 오염. Doerig 2025는 RCNN 학습에서 NSD 73k를 제외해 이를 통제함 | [A] |
| Pretrained model 오염 | COCO는 대다수 VLM의 학습 분포 안에 있다. VLM 정서 평정이 캡션 기억에 기대는지 확인 필요 | 추론 |
| Session-specific 효과 | Gifford 2026은 세션별 시각, 각성, 인지 상태 차이가 응답 분포를 바꿀 수 있다고 경고. 정서 분석에서 세션 내 z-score 등 필요 | [A] |
| 피험자 수 | 8명. 개인차와 일반화에 약함 (Sadeghi 2024도 지적) | [A] |
| 피질하 영역 | NSD의 amygdala 분석 연구를 이번 검색에서 찾지 못함. 7T에서 피질하 SNR과 coverage 확인 필요 | 미확인 |
| ROI 순환추론 | VV와 상관된 voxel로 마스크를 정의한 뒤 같은 데이터로 합성 영상 해석 시 순환 위험 (Sadeghi 2024 Study 5 해석 시 주의) | 추론 |
| 라이선스 | NSD Terms 원문 미확인. COCO 이미지는 Flickr 약관 | [B] |
| 과제 의존성 | Doerig 2025는 continuous recognition 과제가 내부 캡셔닝을 유도했을 가능성을 배제할 수 없다고 명시. 정서 표상도 같은 과제 의존성 문제를 가진다 | [A] |

## 7. Cross-dataset Compatibility Notes

* **Horikawa (Cowen & Keltner 비디오, 별도 평정자 34 범주/14 차원):** NSD는 정서 풍부 자극이 없고 Horikawa는 정서 풍부하지만 피험자 5명이다. 공통 다리는 (i) Cowen & Keltner 프레임으로 학습된 EmoNet (Kragel 2019)을 NSD 이미지에 적용, (ii) NSD 학습 encoding model을 Horikawa 프레임에 in-silico 적용. Gao 2025는 EmoNet이 정서 유발 영상에는 강하지만 일상 장면에는 AlexNet보다 약하다고 보고하므로, 축의 이전 가능성 자체가 검증 대상이다.
* **Emo-FilM (연속 평정, 3T 영화):** 정지 이미지 vs 연속 영화, 7T vs 3T, 기억 과제 vs 수동 시청. 직접 결합보다는 공통 모델 공간(예: VLM 정서 평정 축)에서 비교하는 방식이 현실적이다. 별도 평정자 체계(CPM 성분)와 NSD의 참가자 valence/arousal은 척도가 다르다.
* **Spacetop:** 직접 겹치는 자극 없음. 정서 과제(통증 등)의 개인 내 반응과 NSD의 자극 기반 반응은 구성 개념이 다르다.
* **BOLD5000:** COCO 2,000장 포함, GLMsingle 처리판 존재 (Gao 2025가 TYPED-FITHRF-GLMDENOISE-RR 사용), 참가자가 trial마다 like/neutral/dislike를 판단, Gao 2025가 4,913장에 20개 정서 범주 평정 공개 연구. NSD와 처리 파이프라인이 유사해 조화가 쉬운 편이다. NSD와 COCO ID 중복 여부 미확인.
* **Annotation 비호환:** nsdmeadows는 상대 배치 기반 연속값, Horikawa는 범주 판단 비율과 Likert형 차원, Emo-FilM은 연속 시간 평정. 공통 척도로 옮기려면 rank 기반 비교나 잠재 공간 정렬이 필요하다.

## 8. Research Opportunities

각 항목에 선행 수행 여부를 단다. 모두 Exploratory 단계의 후보이며, decoding 성능을 경험 정서의 직접 판독으로 해석하지 않는다.

1. **정서의 고유 분산 검정 (Affect beyond semantics).** 73k 이미지에 여러 출처의 정서 라벨(VLM 평정, EmoNet, VV 모델)을 붙이고, LLM 캡션 embedding (Doerig 2025)과 객체 범주를 통제한 뒤 정서 라벨의 고유 설명 분산을 voxel별로 추정한다. shared1000에 신규 인간 평정을 모아 AI 라벨을 보정하고 nsdmeadows로 참가자 수준 검증을 한다. 선행: partially (Sadeghi 2024는 저수준 VV만, Gao 2025는 BOLD5000에서 객체 표상 우위). 고차 의미 통제와 다중 라벨 비교는 미수행으로 보임 (이번 검색 기준).
2. **참가자 본인 평정 vs 규범 평정 vs AI 평정의 뇌 정렬 비교.** 같은 100장에서 세 출처의 valence가 각 참가자 뇌 반응과 얼마나 정렬되는지 비교한다. 100장이라 검정력이 낮으므로 효과 크기 추정 중심의 탐색 분석으로 설계해야 한다. 선행: 이번 검색에서 미발견.
3. **정서(각성)와 기억의 상호작용.** AI 추정 arousal과 negative valence가 trial 단위 recognition 정확도, hippocampus/perirhinal 반응, 반복 억제 크기를 예측하는지 본다. NSD 기억 연구 (Sheng 2026, Bai & Coutanche 2026)는 정서를 다루지 않았다 (초록 기준). 선행: 이번 검색에서 미발견.
4. **In-silico 정서 탐침과 생성적 검증.** NSD 학습 encoding model에 IAPS, OASIS, Cowen & Keltner 프레임을 넣어 예측 반응을 얻고, 정서 목적 함수로 뇌 유도 영상 합성 후 인간 평정으로 검증한다. 선행: partially (Sadeghi 2024의 NeuroGen VV 합성, Chen et al. VSS 2025 초록). in-silico 예측과 관찰 fMRI를 반드시 구분해야 한다.
5. **사회적 장면 valence의 계층 분리.** COCO에는 사람이 많은 장면이 많다. VLM으로 "장면 맥락 valence"와 "인물 상호작용 valence"를 따로 주석해 NSD 뇌 반응에서 분리 가능한지 검정한다. Yargholi et al. 2025가 소규모 자체 자극으로 시각 영역은 맥락 valence를, 연합피질은 상호작용 valence를 반영한다고 보고했으므로 NSD 규모 재현이 의미 있다. 선행: partially (NSD 규모는 미수행으로 보임).
6. **범위 제한 보완을 위한 데이터셋 결합.** NSD (중립 위주, 대규모)와 Horikawa (정서 풍부, 소규모)를 공통 encoding 공간으로 결합해 정서 축이 데이터셋 간에 이전되는지 검정한다. 선행: 이번 검색에서 미발견.

### Coordinator 참고: G1이 미치는 영향
NSD의 G1은 "요청 필요"이고 대체 경로(COCO 공개 이미지)가 있어 모델 기반 연구의 차단 요인이 아니다. 다만 우리 환경 보유 여부가 미확인이므로, 사용자가 (i) NSD 접근 승인 보유 여부와 (ii) 로컬 경로를 `reference/datasets_and_resources.md`에 기입해야 한다. 라이선스 원문(상업적 사용, 파생 라벨 재배포)은 연구 산출물 공개 계획 전에 반드시 확인해야 한다.

---

## 부록 A. NSD로 정서 또는 정서 인접 주제를 다룬 연구 (2022~2026, 이번 검색 범위)

| 연구 | 정서 관련 내용 | NSD 사용 방식 | 라벨 출처 | 등급 |
|---|---|---|---|---|
| Khosla, Ratan Murty, Kanwisher 2022, Curr Biol, doi:[10.1016/j.cub.2022.08.009](https://doi.org/10.1016/j.cub.2022.08.009) | 음식 선택 성분이 valence/arousal과 무관함을 통제 분석으로 확인 | voxel decomposition | nsdmeadows (참가자 평균) | A |
| Sadeghi et al. 2024, Nat Commun, doi:[10.1038/s41467-024-53668-6](https://doi.org/10.1038/s41467-024-53668-6) | 저수준 visual valence의 시각 영역 표상, NeuroGen 합성 | group 분석 + 생성 모델 | AI (VV 모델), nsdmeadows로 r = 0.22 검증 | A |
| Chen, Keil, Ding, VSS 2025 초록 ([visionsciences.org](https://visionsciences.org/presentation/?id=1989)) | NSD 학습 encoding model로 IAPS, AffectNet in-silico decoding | encoding model 학습원 | IAPS 규범, AffectNet | B |
| Pennock et al. 2023, Curr Biol; Jain et al. 2023, Commun Biol, doi:[10.1038/s42003-023-04546-2](https://doi.org/10.1038/s42003-023-04546-2) | 음식 선택 영역 (정서 인접: 욕구, 가치) | univariate, 선택성 | 자극 속성 | A |
| Sheng et al. 2026, PNAS, doi:[10.1073/pnas.2603685123](https://doi.org/10.1073/pnas.2603685123); Bai & Coutanche 2026, NeuroImage, doi:[10.1016/j.neuroimage.2026.122266](https://doi.org/10.1016/j.neuroimage.2026.122266) | 정서 아님. recognition memory 기제 (정서-기억 연구의 기반) | trial 단위 기억 판단 | 참가자 행동 | A |

## 부록 B. 이번 감사에서 사용한 주요 출처

* NSD 원 논문 PubMed: https://pubmed.ncbi.nlm.nih.gov/34916659/
* NSD 공식 사이트 (접근 차단, 미열람): https://naturalscenesdataset.org/
* NSD Data Manual, Terms & Conditions (접근 차단, 미열람): https://cvnlab.slite.page/
* AWS Registry (접근 차단, WebSearch 요약만): https://registry.opendata.aws/nsd
* COCO Terms of Use (2차 사본만 확인): https://cocodataset.org/#termsofuse
* 문헌 기록: `outputs/agents/dataset-auditor/literature_NSD.jsonl` (28편. PubMed로 직접 확인 17편, WebSearch 색인으로만 확인 10편(arXiv 7, bioRxiv 2, AAAI 1), 학회 초록 1편(VSS 2025, DOI 없음). 본문을 실제로 읽은 `full_text`는 PMC 전문 9편이며, NSD 원 논문은 `discussion_read: "no"`)
