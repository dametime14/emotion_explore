# 재탐색 라운드: geometry-info (Agent 7)

* 기준일: 2026-11-12. 요청: Coordinator 재탐색 라운드 위임(`outputs/revision/plan.md`)
* 직접 읽은 자료: `outputs/revision/plan.md` 전체, `outputs/rq_landscape.md` RQ-04, `outputs/combinations/matrix.csv` STR-B1, `outputs/evaluation/scores_coordinator.csv`, `scores_reviewer.csv`, `reviewer_notes.md`(RQ-04 행), `outputs/stage1/dataset_Horikawa.md`, `dataset_NSD.md`, `horikawa_factcheck_stage4.md`, `outputs/literature/literature_db.csv`, 내 이전 산출물(round1~4, RQ-01, RQ-03 카드)
* 담당: (A) RQ-04를 깊게 다시 쓰기 → GI-RV-1. (B) 기하와 비지도 관점에서 D1, D2와 잇는 새 질문 → GI-RV-2, 3, 4.
* 표기: [본문] 본문 직접 확인, [초록] 초록만, [db] literature_db의 다른 에이전트 기록 사용, [서지] 식별자와 서지만 확인, [검색] 검색 요약만. 라이선스는 이 세션에서 GitHub raw의 LICENSE 파일이나 PyPI 메타데이터로 본 것만 "확인"으로 쓴다. 모델 가중치는 Hugging Face 접속이 막혀 있어 대부분 미확인이다.
* plan.md 4절 함정 준수: EmoNet은 C&K 프레임으로 학습되어 Horikawa와 MC에 쓰지 않는다. MC 학습 자료는 2,108개로 고정하고 시험 72개는 평가에만 쓴다. C&K 클립은 모두 무음이다. MC 보유본 전처리 형식은 미확인이다(원 논문은 4 s shift 후 블록 평균). MC 캡션은 [Human 작성, AI 교정]이다. Westlin 2025는 사람별 군집 11~14개, 범주 NMI 0.014, 세션 NMI 0.19이며 저자도 세션 NMI를 낮다고 봤다. 정서 라벨은 별도 평정자의 규범 평정이다. VLM과 MLLM은 C&K 자료를 사전학습에서 봤을 수 있다.

## 0. 한눈에 보기

| ID | 한 줄 질문 | 방향 | AI 역할(plan.md 2절 기준 1의 a, b, c) | 자체 진단: AI 기여 / 1개월 |
|---|---|---|---|---|
| GI-RV-1 (RQ-04 재작성) | 뇌가 정서 단어 없이 스스로 나눈 축을 AI로 그려 보면, 그 축은 정서일까 장면 내용일까? | 비지도 + 생성 + MLLM | (b) 축의 의미를 계산 가능하게 함, (c) 검증 가능한 가설을 생성하고 보지 않은 클립으로 시험 | 4 / 4 |
| GI-RV-2 | 뇌의 정서 구조는 보는 것만으로 생길까, 말로 배운 개념이 있어야 생길까? | D1 (학습 조건을 조작한 인공 뇌) | (a) 같은 구조, 같은 자료에서 학습 목표만 다른 모델을 비교 대상으로 제공 | 5 / 4 |
| GI-RV-3 | 뇌가 본 장면은 실제 장면보다 정서 쪽으로 기울어 있을까? | D2 (decoder + emotion head) | (b) 사람 뇌가 "본 내용"을 장면과 같은 공간에서 재는 변수를 만듦, (a) in-silico 대조 decoder | 4 / 4 |
| GI-RV-4 | 뇌처럼 배선을 아끼는 AI에서도 정서 지도가 저절로 생길까? | D1 (구조 제약을 바꾼 모델) | (a) 공간 제약만 바꾼 모델을 비교 대상으로 제공 | 4 / 3 |

* 자체 진단은 참고용이다. 채점은 Coordinator와 새 adversarial-reviewer가 한다.
* 공유 파이프라인: GI-RV-1과 GI-RV-3은 같은 시각 feature, encoding, decoding 틀을 쓴다. GI-RV-2와 GI-RV-4는 같은 모델 feature 추출과 "처리 단계별 정서 기하 지표"를 쓴다. 네 질문 모두 Horikawa 공개 전처리본(블록 평균, HCP360 ROI)으로 1주차를 시작할 수 있다.
* 담당 겹침: GI-RV-3은 vision-decoding의 D2 주담당과 도구가 겹친다. 내 쪽은 decoding 성능이나 emotion head 정확도가 아니라 "decoder 오차의 방향(기하)"을 묻는다.

---

## (A) 출발점 RQ-04 진단과 재작성

### 왜 약했는가: 새 기준 두 개로 본 진단

출발점: RQ-04 "정서 단어 없이 뇌에서 먼저 찾은 정서 축에 이름을 붙이면 어떤 분류가 나올까?" (matrix STR-B1). Stage 4 최종 점수는 합계 26.0 / 45(Falsifiability 2, Methodological Rigor 2.5, Dataset Feasibility 3, Feasibility 3)였다(scores_final.csv).

| 새 기준 | 진단 | 근거 |
|---|---|---|
| **AI-enabled Affective Neuroscience Contribution** | **약 2점.** AI(MLLM)는 사람 명명을 대신하는 도구였다. 관찰로 얻을 수 없는 비교 대상을 주지도, 측정할 수 없던 변수를 만들지도 않았다. 결과("기존 범주와 다른 이름 체계")는 서술이라 정서 기제에 대해 구체적인 것을 말하지 않는다. MLLM이 C&K 공개 지도를 학습했을 수 있어 명명이 순환적이다 | scores_reviewer.csv RQ-04 Methodological Rigor 2 근거, reviewer_notes 5절 04행 "클립이 범주 대표로 수집됨, MLLM 오염" |
| **1-month Feasibility** | **약 2점.** 사람 명명 평정을 새로 모아야 한다(IRB, 예산). 성분 정의가 RQ-01 0단계(11명 raw 재전처리)에 묶여 있었다 | scores_coordinator.csv RQ-04 Dataset Feasibility, Feasibility 근거, reviewer_notes 3절 |
| (함께 걸린 문제) 반증 조건 | "기존 범주와 다르다"의 기준(정보량, 일대다 대응)이 연속적이라 어떤 결과도 받아들일 수 있었다 | scores_reviewer.csv Falsifiability 2 |
| (함께 걸린 문제) K1 평가 | 같은 자료의 라벨 없는 구조 찾기는 Horikawa 2020(비지도 군집, gradient)과 Westlin 2025(사람별 군집 11~14개, 범주 NMI 0.014)가 이미 했다. 축에 이름만 다시 붙이면 같은 자료의 재판정이다 | plan.md 1절, arXiv:2507.00320 [본문] |
| (함께 걸린 문제) 표집 순환 | C&K 클립은 34범주를 대표하도록 모은 것이라, 축의 상위 클립 이름은 기존 범주로 돌아가기 쉽다 | reviewer_notes 5절 04행, doi:10.1073/pnas.1702247114 |

**재작성의 방향:** (1) 사람 명명을 없애고, AI가 만든 설명을 "보지 않은 실제 클립의 뇌 반응을 예측하는가"로 시험한다. 이렇게 하면 결과가 숫자로 반증된다. (2) C&K 밖의 대규모 이미지 풀에서 축을 그려 표집 순환과 C&K 오염을 줄인다. (3) 설명에서 나온 "정서만 바꾼 편집"과 "내용만 바꾼 편집"으로 축이 정서를 따르는지 내용을 따르는지 가른다. (4) 공개 전처리본과 parcel 수준으로 1주차부터 시작한다.

### [GI-RV-1] 뇌가 정서 단어 없이 스스로 나눈 축을 AI로 그려 보면, 그 축은 정서일까 장면 내용일까?

* **자세한 질문**
  * Horikawa 2020과 Mind captioning(MC)의 transmodal 영역 반응에서 라벨 없이 찾고 두 코호트 사이에서 재현되는 공유 축마다 다음을 묻는다.
  * (i) encoding 모델로 C&K 밖 대규모 이미지에서 그 축을 가장 올리고 내리는 이미지를 찾고, MLLM이 두 묶음의 차이를 말로 쓴 가설은 보지 않은 실제 클립의 축 값을 34개 범주와 14개 차원 규범 평정보다 더 잘 예측하는가?
  * (ii) 그 가설에서 나온 "정서적 의미만 바꾼 편집"과 "같은 크기로 내용만 바꾼 편집" 중 어느 쪽에 축이 더 반응하는가?
* **AI가 있어야만 가능한 이유**
  * 관찰만으로는 축의 의미를 그 축을 만든 2,180개 클립 안에서만 볼 수 있다. 그 클립은 범주를 잘 유발하도록 모은 것이라 해석이 기존 범주로 돌아간다. encoding 모델은 같은 축을 7만 장이 넘는 C&K 밖 이미지에서 계산하게 해 준다(측정할 수 없던 변수, 기준 1-b).
  * MLLM은 "두 이미지 묶음의 차이"를 사람 명명 없이 검증 가능한 문장 가설로 만든다(기준 1-c). 그 가설은 MLLM 평정으로 숫자가 되어 보지 않은 클립에서 시험된다. Generative causal testing(언어 영역, arXiv:2410.00812)의 논리를 정서 축에 옮긴 것이다.
  * 이미지 편집 모델은 자연 자극에서는 함께 움직이는 정서와 내용을 떼어 낸 최소 쌍을 만든다(통제된 비교 대상, 기준 1-a). 이 부분은 in-silico(R1)이다.
* **정서와 뇌에 대해 새로 알게 되는 것**
  * 정서 비디오를 볼 때 transmodal 영역이 실제로 쓰는 축이 정서 범주(Semantic Space Theory, Cowen & Keltner 2021), appraisal 같은 관계적 의미(예: "누군가 다치고 있다", "가까운 사람과의 친밀"), 아니면 정서와 무관한 내용(얼굴, 동물, 음식) 중 어느 쪽인지를 숫자로 가른다.
  * Horikawa 2020은 "충분히 포괄적인 appraisal 차원 집합이면 범주 모형과 같아질 수 있다"고 적었다(Discussion 4째 단락, [본문]). 이 질문은 그 집합의 후보를 뇌에서 먼저 뽑아 시험한다.
  * 결과는 새 fMRI 실험(R3)에서 바로 쓸 수 있는 자극 집합과 가설이 된다.
* **데이터**

| 항목 | 상태 | 근거 |
|---|---|---|
| Horikawa 2020 뇌 반응 | 있음. 공개 전처리본(블록 평균, native volume, HCP360 ROI 표시) | dataset_Horikawa.md G2 |
| MC 뇌 반응 | 있음(사용자 보유). 전처리 형식 미확인. 블록 평균이 아니면 raw(ds005191)에서 다시 처리해야 해 1~2주가 더 든다. 학습은 2,108개, 시험 72개(5회 반복 평균)는 평가에만 | STAGE_STATUS 16번, plan.md 4절 |
| C&K 클립 | 있음(사용자 보유, 2,185개 무음) | STAGE_STATUS 25(b) |
| 정서 라벨 | 34개 범주 비율, 14개 차원. 별도 MTurk 평정자의 규범 평정. 참가자 본인 보고 없음 | dataset_Horikawa.md G3 |
| 축을 그릴 이미지 풀 | NSD 자극 COCO 이미지 73,000장(사용자 보유). 뇌 자료는 쓰지 않고 이미지만 쓴다. COCO 이미지 이용은 Flickr 약관, NSD 약관 원문은 미열람 | dataset_NSD.md 1절 |
| 사람 명명 평정 | 필요 없음 | |

* **모델과 checkpoint**

| 용도 | 후보 | 공개 / 라이선스 | GPU |
|---|---|---|---|
| 시각 feature, encoding | OpenAI CLIP ViT-L/14, DINOv2 | 코드 저장소 MIT(openai/CLIP), Apache-2.0(facebookresearch/dinov2) 확인. 가중치 표기는 미확인 | 1장, 수 시간 |
| 축 기술, 가설 평정 | 공개 VLM 하나(예: Qwen2.5-VL 7B) | 저장소 Apache-2.0(QwenLM/Qwen2.5-VL) 확인. 가중치 라이선스 미확인 | 1장(24 GB 이상), 수일 |
| 편집 | InstructPix2Pix | 저장소 허용형 라이선스 문구 확인(timothybrooks/instruct-pix2pix). 가중치 미확인 | 1장 |
| 쓰지 않음 | EmoNet(누수), TRIBE v2(무음 입력은 학습 분포 밖) | plan.md 4절 | |

* **핵심 분석**
  1. **축:** 사전 지정 transmodal parcel(IPL/TPJ, STS, PCC/precuneus, mPFC/OFC, 전측 섬엽, 측두극)의 블록 반응으로 피험자 공통 축(shared response model)을 학습 클립에서 구한다. Horikawa에서 구한 축이 MC의 보지 않은 클립에서 재현되는 것만 남긴다(기준: 클립 순서 섞기 null의 95백분위 초과). Westlin 2025에서 보듯 이 자료의 라벨 없는 구조는 사람마다 크게 다르므로 살아남는 축은 몇 개뿐일 수 있다. 대조 축으로 V1~V3 parcel의 공통 축과 transmodal 공간의 무작위 방향을 같은 절차로 만든다.
  2. **encoding:** 클립 프레임 평균 CLIP, DINOv2 feature로 각 축 값을 ridge 예측한다. MC 72개(반복 평균)에서 예측력을 noise ceiling과 함께 보고한다.
  3. **축 그리기:** encoding 모델로 COCO 7.3만 장의 축 값을 계산해 상위 50장, 하위 50장을 고른다(근접 중복 제거).
  4. **가설 만들기:** VLM에 두 묶음을 보여 주고 "무엇이 다른가"를 정서 어휘 제한 없이 쓰게 해 축마다 가설 5개를 얻는다. 대조 축(시각 축, 무작위 방향)에도 똑같이 한다.
  5. **가설 시험:** VLM이 보지 않은 C&K 클립(MC 72개와 Horikawa 보류 run)의 대표 프레임을 각 가설 문장에 대해 0~10으로 평정한다. 그 점수가 실제 축 값을 얼마나 예측하는지(Spearman)를 다음 기준선과 비교한다: (a) 학습 클립에서 고른 가장 좋은 단일 C&K 범주, (b) 34 + 14 규범 평정의 교차검증 ridge, (c) CLIP 내용 feature ridge, (d) 대조 축에서 나온 가설.
  6. **편집 시험(R1):** 상위 가설마다 VLM이 편집 지시문 두 종류를 만든다: 정서적 의미를 바꾸는 편집(예: 표정을 공포로, 다친 흔적 추가)과 CLIP embedding 변화량을 맞춘 내용 편집(옷 색, 배경 사물). encoding 모델의 축 반응 변화 비율(정서 편집 / 내용 편집)을 잰다.
  7. **관찰 보조(R0):** 캡션 embedding이 가깝지만 가설 점수가 크게 다른 자연 클립 쌍을 찾아 실제 축 값 차이를 본다(탐색).
* **예측(경쟁 설명별)**
  * 범주 설명: 살아남은 축의 가설이 C&K 범주 이름과 같고, (b)를 넘는 고유 설명력이 없다.
  * 관계적 의미 설명: 가설이 appraisal 같은 관계적 의미를 말하고, (b)와 (c)를 넣은 뒤에도 고유 설명력이 남으며, 정서 편집이 내용 편집보다 축을 크게 움직인다.
  * 내용 설명: 가설이 내용만 말하고(얼굴, 동물, 군중), 정서 편집과 내용 편집의 효과가 같다.
* **반증 조건(결과 전 고정)**
  * "뇌가 먼저 정한 정서 축"이라는 주장은 다음 중 하나면 지지되지 않는다: transmodal 축의 가설 예측력이 대조 축 가설 분포의 95백분위를 넘지 못함, (b) + (c)에 더한 고유 설명력의 클립 bootstrap 95% 구간이 0을 포함, 정서 편집 / 내용 편집 비율의 95% 구간이 1을 포함.
  * 코호트 간 재현 축이 하나도 없으면 질문 자체를 "이 자료로는 불가"로 닫는다.
* **4주 계획**
  * 1주: Horikawa 공개 전처리본으로 parcel 반응, 공통 축, 코호트 재현(MC 형식 확인 병행). 프레임 feature 추출.
  * 2주: encoding 모델과 MC 72개 검증. COCO 7.3만 장 축 값 계산, 상위/하위 묶음, VLM 가설 생성(대조 축 포함).
  * 3주: 보류 클립 VLM 평정, 기준선 비교, 고유 설명력 검정.
  * 4주: 편집 시험, 관찰 쌍 탐색, 결과 정리.
* **가장 가까운 선행과 차이**
  * Tuckute et al. 2024(doi:10.1038/s41562-023-01783-7) [db]: encoding 모델로 고른 문장이 언어망을 구동, 억제. 정서 축이 아니고 가설 생성이 없다.
  * BrainSCUBA(Luo et al. 2023, arXiv:2310.04420) [초록]: voxel별로 최대 활성 이미지의 자연어 설명을 만들어 고위 시각피질 선택성을 지도화. 시각피질 범주(사람, 몸) 대상이고, 설명을 보지 않은 자연 자극의 예측으로 시험하지 않는다.
  * Generative causal testing(Antonello et al. 2024, arXiv:2410.00812) [초록]: 언어 영역 선택성을 LLM 설명으로 만들고 생성 자극으로 시험. 언어 영역이고 정서가 아니다.
  * BrainDiVE(arXiv:2306.03089) [db], NeuroVolve(arXiv:2512.00557) [db]: 영역 구동 이미지 생성. NeuroVolve는 amygdala 최대화 이미지가 강한 표정의 얼굴이었다고 보고. 설명 가설의 보류 시험과 정서 대 내용 편집 분리는 없다.
  * Jang & Kragel 2025(doi:10.1523/JNEUROSCI.1436-24.2025) [db]: amygdala 하위영역 encoding 모델과 합성 자극. 라벨 없는 transmodal 축이 아니고, 합성 자극의 in vivo 검증은 보고되지 않았다(db 기록).
  * Khosla et al. 2022(doi:10.1016/j.cub.2022.08.009) [db]: 가설 없는 voxel 분해로 음식 성분 발견. 그 성분은 nsdmeadows valence, arousal과 상관이 없었다.
  * 검색: WebSearch "brain-guided image synthesis or natural language explanation of emotion-related brain regions amygdala fMRI generative model selectivity 2025"(2026-11-12) → 세 요소(라벨 없는 정서 관련 축, 자연어 가설, 보류 시험)를 함께 한 연구 없음. 가장 가까운 것은 Jang & Kragel 2025, BrainDiVE, NeuroVolve.
  * **차이:** 정서 비디오에 대한 transmodal 영역의 라벨 없는 공유 축을 대상으로, AI가 만든 가설을 규범 정서 어휘와 같은 기준에서 보지 않은 실제 클립으로 시험하고, 정서와 내용을 편집으로 떼어 본다.
* **주요 위험**
  * transmodal parcel의 블록 반응은 SNR이 낮아 encoding 모델이 약할 수 있다(2주차 MC 72개 검증으로 확인).
  * 비디오로 학습한 encoding 모델을 정지 이미지에 쓰는 분포 이탈.
  * VLM 가설이 "사람이 있다" 같은 일반 문장에 머물 수 있다. 대조 축 가설이 그 기준선이다.
  * VLM이 C&K 클립을 봤을 수 있어 보류 클립 평정이 오염될 수 있다. 같은 VLM의 34범주 평정이 규범 평정과 비정상적으로 맞는지 먼저 점검한다(Asanuma 2025, doi:10.1038/s41598-025-14961-6: 범주 수준 일치, 개별 비디오 수준 제한).
  * 편집은 저수준 통계도 바꾼다. 편집 결과는 R1로만 보고한다.
  * 라벨은 규범 평정이라, "정서 축"은 "규범 정서 평정과 관계된 뇌 축"을 뜻한다.

---

## (B) 새 질문

### [GI-RV-2] 뇌의 정서 구조는 보는 것만으로 생길까, 말로 배운 개념이 있어야 생길까?

* **자세한 질문:** 같은 구조(ViT-B/16)를 같은 자료(YFCC15M)로 학습하되 목표만 다른 세 모델이 있다: 이미지끼리만 비교한 모델(SimCLR), 이미지와 캡션을 맞춘 모델(CLIP), 둘 다 쓴 모델(SLIP). 무작위 초기화 모델을 하나 더 둔다. 이 모델들의 층과 사람 뇌의 처리 단계(V1부터 VTC, STS, TPJ, 전두까지)에서 C&K 클립의 정서 기하를 같은 지표로 잰다. 그러면 (i) 정서 기하가 처음 나타나는 단계는 뇌와 모델에서 어디이며, (ii) 언어 감독이 그 단계와 강도를 바꾸는가, 특히 정서 범주 구조와 valence, arousal 구조에서 다르게 바꾸는가?
* **AI가 있어야만 가능한 이유:** 사람은 언어 없이 자라게 할 수 없다. 같은 구조와 같은 시각 경험에서 언어 감독만 빼거나 더한 "인공 뇌"를 비교하는 것은 학습 조건을 조작한 모델로만 가능하다(기준 1-a). 관찰 자료만으로는 transmodal 영역의 정서 기하가 시각 학습에서 오는지 개념, 언어 학습에서 오는지 가를 수 없다.
* **정서와 뇌에 대해 새로 알게 되는 것**
  * 구성주의의 개념 행위 이론은 정서 범주가 개념, 언어 지식에 기대고 core affect(valence, arousal)는 그렇지 않다고 본다. 이 관점이 맞다면 언어 감독은 범주 기하를 특히 transmodal 단계에서 키우고 valence, arousal 기하에는 영향이 작아야 한다.
  * "정서 schema가 시각계에 들어 있다"는 관점(Kragel 2019, doi:10.1126/sciadv.aaw4358 [db])과 "물체 인식 학습만으로 정서 선택 unit이 생긴다"는 결과(Liu 2024, doi:10.1371/journal.pcbi.1011943 [db])가 맞다면, SimCLR만으로 시각 단계의 정서 기하가 이미 나타나고 언어 감독의 추가 효과는 작아야 한다.
  * 두 예측은 같은 측정으로 서로 반대 방향을 가리킨다. 그러므로 결과가 정서 이론에 직접 말한다.
* **데이터**
  * Horikawa 2020(5명, 2,181개, 공개 블록 전처리본, HCP360 ROI)과 MC(6명, 학습 2,108개, 시험 72개).
  * C&K 클립(보유, 무음). 규범 평정 34 + 14.
  * 내용 묶음(교차 내용 일반화용): MC 캡션 embedding의 k-means. 캡션은 [Human 작성, AI 교정].
* **모델과 checkpoint**
  * SLIP 저장소(facebookresearch/SLIP): 코드 MIT 확인. README에 YFCC15M으로 학습한 ViT-S/B/L의 SimCLR, CLIP, SLIP 가중치가 나열되어 있다. 가중치 호스트(dl.fbaipublicfiles.com)는 이 세션에서 403을 돌려줘 내려받기를 확인하지 못했다(사용자 환경에서 확인 필요). 가중치에 따로 붙은 라이선스 표기는 미확인.
  * 무작위 초기화 ViT-B/16(구조 사전의 기준선).
  * GPU 1장. 2,181개 x 프레임 8장 x 모델 4개 feature 추출은 수 시간.
  * YFCC15M(Flickr 사진)은 C&K(2017, GIF 출처)와 겹칠 가능성이 웹 규모 CLIP보다 낮다. 그래도 확인은 못 한다.
* **핵심 분석**
  * 정서 기하 지표 두 개를 결과 전에 고정한다.
    * I1 정서 특이 RSA: 표상의 클립 간 거리 행렬과 규범 정서(34 + 14) 거리 행렬의 부분 상관. 저수준 영상 통계 거리 행렬을 통제한다(보조 판: 캡션 내용 거리도 통제).
    * I2 교차 내용 일반화: 한 내용 묶음에서 학습한 선형 readout(valence, arousal, 범주 쌍)이 다른 내용 묶음에서도 맞는가(leave-one-cluster-out).
  * 단계 곡선: 뇌는 ROI 위계 순서, 모델은 층 순서로 I1, I2를 그린다. "출현 단계"는 내용 묶음 구조를 보존한 라벨 순열 null의 95백분위를 처음 넘는 단계다.
  * 주 대비: 같은 층에서 Δ = I(CLIP) - I(SimCLR), 그리고 모델 층별 곡선과 뇌 단계 곡선의 일치. 일반 정렬(전체 RSA)도 함께 보고해, 언어 감독의 이득이 정서에 특이한지 본다. Conwell 2024는 다른 조건을 같게 하면 순수 시각 대조 학습과 시각-언어 정렬의 뇌 예측력이 거의 같다고 보고했다.
  * 추론 단위: 피험자 bootstrap과 클립 bootstrap.
* **예측과 반증 조건**
  * 개념 행위 이론 쪽 예측: 범주 I1에서 Δ > 0이고 transmodal 단계와 맞는 층에서 가장 크며, valence, arousal I2에서는 Δ ≈ 0.
  * 시각 schema 쪽 예측: SimCLR 곡선이 이미 뇌의 VTC 단계 정서 기하와 맞고, 범주와 core affect 모두에서 Δ ≈ 0.
  * 반증: 범주 I1의 Δ에 대한 피험자, 클립 bootstrap 95% 구간이 모든 transmodal 대응 층에서 0을 포함하면 "언어 감독이 정서 범주 기하를 만든다"는 가설은 이 자료에서 지지되지 않는다. 무작위 초기화 모델이 같은 수준이면 효과는 구조 사전에서 온 것이다.
* **4주 계획**
  * 1주: 가중치 확보, 프레임 feature 추출, Horikawa ROI 블록 반응 정리, 내용 묶음 만들기.
  * 2주: I1, I2를 모델 층과 뇌 ROI에서 계산, null 분포.
  * 3주: 단계 곡선과 Δ 비교, MC로 재현.
  * 4주: 보조 판(캡션 통제), 일반 정렬 대비, 정리.
* **가장 가까운 선행과 차이**
  * Wang et al. 2023(doi:10.1038/s42256-023-00753-y) [서지, 선행 preprint doi:10.1101/2022.09.27.508760 초록]: 자료 크기와 다양성을 통제한 비교에서 언어 피드백과 다양한 자료가 고위 시각피질 반응 설명에 중요. 정서 아님, 정지 이미지.
  * Conwell et al. 2024(doi:10.1038/s41467-024-53147-y) [초록]: 224개 모델 통제 비교. 구조와 목표(순수 시각 대조 학습 대 시각-언어 정렬)는 다른 조건을 같게 하면 뇌 예측력이 거의 같고, 학습 자료가 가장 크게 작용. 표준 연결 방법이 너무 유연할 수 있다고 경고.
  * Chen et al. 2025(arXiv:2501.13628) [초록]: CLIP이 같은 ResNet-50 구조의 지도 학습, MoCo 모델보다 VOTC 표상에서 고유 분산을 설명하고 좌반구 편향. 시각-언어 경로 손상 환자에서 그 대응이 줄었다. 정서 아님.
  * Liu et al. 2024 [db]: 물체 인식 DNN에 정서 선택 unit이 출현. 신경 기록과 비교하지 않았다.
  * Du et al. 2025(arXiv:2509.24298) [db]: 같은 2,180개 비디오에서 MLLM 정서 embedding이 인간 평정 기반 embedding보다 뇌와 잘 정렬. 학습 목표를 통제한 비교는 아니다.
  * 검색: WebSearch "language supervision CLIP versus self-supervised vision model emotion representation alignment human brain fMRI emotional videos controlled training objective"(2026-11-12) → 정서 비디오 fMRI에서 학습 목표를 통제해 정서 기하를 비교한 연구 없음.
  * **차이:** 일반 예측력이 아니라 정서 기하(범주 대 core affect)와 그 출현 단계를, 학습 목표만 다른 모델과 정서 비디오 fMRI로 비교하고, 정서 이론의 상반된 예측에 연결한다.
* **주요 위험**
  * YFCC15M ViT-B 모델은 성능이 높지 않아 정서 기하가 약하게 나올 수 있다(보조로 CC3M/CC12M CLIP과 SLIP도 README에 있음).
  * Conwell 2024의 경고처럼 지표가 유연하면 차이가 지표 선택에서 생길 수 있다. 지표 두 개만 사전 고정한다.
  * 모델의 언어는 영어, 규범 평정자는 미국 영어 사용자, 두 코호트는 일본인이다. 결과는 "영어 캡션 감독"의 효과로 한정한다.
  * 프레임 평균 feature라 비디오의 움직임 정보가 빠진다.
  * 라벨은 규범 평정이다.

### [GI-RV-3] 뇌가 본 장면은 실제 장면보다 정서 쪽으로 기울어 있을까?

* **자세한 질문:** MC 6명(학습 2,108개, 시험 72개 5회 평균)과 Horikawa 5명(run 단위 교차검증)에서 fMRI로부터 이미지 embedding(CLIP, 대조로 DINOv2)을 복원하는 decoder를 만든다. 실제 장면 embedding으로 학습한 emotion head를 복원된 embedding과 실제 embedding에 똑같이 적용했을 때, 복원된 장면의 정서 값은 decoder 자체의 쏠림(in-silico 대조)을 빼고도 실제 장면보다 그 클립의 정서 방향으로 더 극단적인가? 그 쏠림은 어느 영역의 voxel에서 오는가(초기 시각 / 고위 시각 / transmodal)?
* **AI가 있어야만 가능한 이유**
  * 사람이 장면을 "어떻게 봤는지"를 장면과 같은 표상 공간에서 재는 변수는 decoder가 있어야 생긴다(기준 1-b). 관찰 자료로는 뇌 반응과 장면이 다른 공간에 있어 "기울어짐"을 정의할 수 없다.
  * decoder는 원래 평균 쪽으로 줄이거나 학습 자료의 원형 쪽으로 끌어당기는 쏠림을 가진다(Shirakawa 2025, doi:10.1016/j.neunet.2025.107515 [db]). 시각 feature만 쓰는 encoding 모델로 만든 합성 뇌 반응을 같은 decoder에 넣으면 "뇌의 정서 없이 decoder만으로 생기는 쏠림"을 잴 수 있다(통제된 비교 대상, 기준 1-a). 이 대조는 모델로만 만들 수 있다.
* **정서와 뇌에 대해 새로 알게 되는 것**
  * affective realism은 정서가 지각 자체를 바꾼다고 본다. 행동 연구에서는 의식하지 못한 정서 이미지가 중립 얼굴을 더 웃거나 찡그린 것으로 보이게 했다(Siegel et al. 2018, doi:10.1177/0956797617741718 [초록]).
  * 이 질문은 같은 주장을 자연 영상과 뇌 표상에서 시험한다. 초기, 고위 시각 voxel만으로 복원한 장면이 정서 쪽으로 기울면, 시각 표상 자체가 정서에 따라 바뀐다는 쪽(affective realism, 시각계의 정서 schema)과 맞는다. transmodal voxel을 넣을 때만 기울면, 정서는 시각 표상 뒤에 더해지고 시각 표상은 장면에 충실하다는 쪽과 맞는다.
* **데이터**
  * MC: 학습 2,108개, 시험 72개(5회 평균으로 신뢰도 확보). 보유본 형식 미확인(블록 평균이 아니면 raw 재처리). MC 원문에서 자극 block은 고정점 없이 봤다.
  * Horikawa: 공개 블록 전처리본, run 6-fold.
  * C&K 클립(보유), 규범 평정 34 + 14.
  * 시선: 두 코호트 모두 자유 시청이라 정서적 부분을 더 오래 보는 시선 효과가 섞인다. 눈알이 EPI에 들어 있으면 DeepMReye(doi:10.1038/s41593-021-00947-w)로 일부 통제한다(raw 필요).
* **모델과 checkpoint**
  * decoder: voxel → embedding ridge(scikit-learn, BSD-3). 시각화가 필요하면 MindEye2(저장소 MIT 확인, 가중치는 Hugging Face pscotti/mindeyev2, 라이선스 미확인. README: 단일 GPU로 40 session 사전학습과 fine-tune 각 약 1일, 1 session fine-tune 가능)를 MC에 fine-tune한다. 핵심 분석에는 필요 없다.
  * embedding: OpenAI CLIP ViT-L/14(저장소 MIT), DINOv2(저장소 Apache-2.0). 가중치 표기 미확인.
  * emotion head: 실제 embedding → 규범 평정 ridge. 출력은 "AI 추정 정서(규범 평정에 맞춘)"로 표시한다.
  * GPU 1장(feature 추출). 나머지는 CPU.
* **핵심 분석**
  * 시험 클립마다 실제 embedding t와 복원 embedding d를 구한다. emotion head h로 h(t), h(d)를 계산한다.
  * 과장 기울기 β: 학습 평균을 뺀 h(d)를 h(t)에 회귀한 기울기. 같은 계산을 in-silico 대조 decoder 출력(시각 encoding 예측 + 실측 잔차 잡음)에도 한다.
  * 주 지표(결과 전 고정): 정서 특이 과장 지수 = (β_뇌,정서 - β_대조,정서) - (β_뇌,비정서 - β_대조,비정서). 비정서 속성은 캡션에서 뽑은 사람 수, 실내/실외, 동물 유무처럼 정서와 무관한 속성이다. 일반적인 복원 충실도 차이를 빼기 위한 것이다.
  * voxel 집합 비교: 초기 시각, 고위 시각, transmodal, 전체.
  * embedding 공간 비교: CLIP(언어 정렬)과 DINOv2(시각만). 정서 방향을 정의하는 공간 자체의 편향을 점검한다.
* **예측과 반증 조건**
  * affective realism 예측: 고위 시각 voxel decoder에서 정서 특이 과장 지수 > 0, 특히 arousal이 높은 클립에서 크다.
  * 충실한 시각 표상 예측: 시각 voxel decoder에서는 지수 ≈ 0이고 transmodal voxel을 넣을 때만 > 0.
  * 반증: 시각 voxel decoder의 지수에 대한 피험자, 클립 bootstrap 95% 구간이 0을 포함하면 "시각 표상 수준의 정서 쏠림"은 이 자료에서 지지되지 않는다. in-silico 대조에서도 같은 크기의 지수가 나오면 효과는 decoder의 원형 쏠림으로 본다.
* **4주 계획**
  * 1주: MC 형식 확인, Horikawa로 decoder와 emotion head 구축, 시험 클립 복원.
  * 2주: 시각 encoding 모델과 in-silico 대조 decoder, 비정서 속성 추출.
  * 3주: 지수 계산, voxel 집합과 embedding 공간 비교, MC 재현.
  * 4주: 시선 통제(가능한 경우), 선택적 MindEye2 시각화, 정리.
* **가장 가까운 선행과 차이**
  * Siegel et al. 2018 [초록]: 행동 수준 affective realism. 뇌 표상 측정 없음.
  * MindEye2(arXiv:2403.11207) [db], Brain-IT(arXiv:2510.25976) [db]: 정지 이미지 복원 성능. 정서 방향의 오차 분석 없음.
  * Shirakawa 2025 [db]: 복원이 학습 자료 원형 쪽으로 쏠리는 문제. 이 질문의 in-silico 대조가 다루는 교란이다.
  * Horikawa 2025 MC(doi:10.1126/sciadv.adw1464) [db]: 같은 자료에서 뇌로부터 장면 설명 문장을 생성. 정서 쏠림은 보지 않았다.
  * 검색: WebSearch "fMRI visual reconstruction decoded image bias toward emotional content affective realism decoding error emotional images"(2026-11-12) → 복원 오차의 정서 쏠림을 시험한 연구 없음.
  * **차이:** decoder를 성능 도구가 아니라 "뇌가 본 장면"을 재는 계측기로 쓰고, decoder 자체의 쏠림을 in-silico 대조로 빼서, 정서가 시각 표상을 기울이는지를 영역별로 시험한다.
* **주요 위험**
  * 3T 비디오 자료에서 복원 정확도가 낮아 검정력이 부족할 수 있다(MC 72개 반복 평균으로 완화).
  * 라벨은 규범 평정이라 참가자 본인의 정서가 아니다. "그 장면이 보통 일으키는 정서 방향"으로의 쏠림만 말할 수 있다.
  * 시선 차이(정서적 부분을 더 봄)는 affective realism의 기전일 수도 있고 교란일 수도 있다. 가를 수 없으면 그렇게 보고한다.
  * emotion head가 쓰는 CLIP 공간이 C&K를 봤을 수 있다. 정확도에는 영향을 주지만 뇌 대 in-silico 대비는 같은 head를 쓰므로 영향이 작다.
  * vision-decoding(D2 주담당)과 도구가 겹친다.

### [GI-RV-4] 뇌처럼 배선을 아끼는 AI에서도 정서 지도가 저절로 생길까?

* **자세한 질문:** 시각 학습과 "가까운 unit끼리 비슷하게 반응하라"는 공간 제약만으로 학습한 topographic 모델(TDANN)에 C&K 클립 프레임을 보여 주면, 모델의 가상 피질 면에 valence, arousal, 정서 범주 선호의 지도(얼룩, 기울기)가 생기는가? 그 지도는 사람 VTC의 정서 선호 지도와 같은 방식으로 얼굴, 몸, 장면 지도에 얹혀 있는가? 공간 제약이 없는 같은 모델과 비교하면 무엇이 달라지는가?
* **AI가 있어야만 가능한 이유:** 뇌에서 배선 비용만 없애 볼 수는 없다. 공간 제약의 세기만 바꾼 모델은 "정서 지도가 시각 학습과 배선 절약만으로 생기는가"를 시험할 비교 대상을 준다(기준 1-a).
* **정서와 뇌에 대해 새로 알게 되는 것**
  * 정서 관련 피질 지도(Lettieri 2019의 TPJ emotionotopy, doi:10.1038/s41467-019-13599-z; Du 2023의 피질 gradient, doi:10.1016/j.isci.2023.107571; Abdel-Ghaffar 2024의 후두-측두 정서 tuning, doi:10.1038/s41467-024-49073-8)가 정서 전용 조직인지, 일반 시각 지도가 배선 절약으로 배치될 때 따라오는 부산물인지를 가른다.
  * 사람 VTC의 정서 선호 지도가 모델 예측을 넘어서면(예: 얼굴, 몸 지도로 설명되지 않는 arousal 기울기), 시각계 바깥(편도체 등)에서 오는 정서 신호나 정서 특이 조직의 후보가 된다. 넘지 못하면 "시각계의 정서 지도"는 시각 지도에 얹힌 것이다.
* **데이터**
  * Horikawa(voxel 좌표, pycortex surface 자료 공개), MC(원문에 VWFA, FFA, PPA, EBA 등 기능 국재 ROI 서술. 보유본 포함 여부 미확인).
  * C&K 클립(보유), 규범 평정. 얼굴, 몸, 장면 선호 비교용 기준 자극은 TDANN 자료(OSF)에 포함된 것을 쓴다(세부 미확인).
  * VTC, 후두-측두 영역에 한정한다(TDANN은 복측 시각 경로 모델).
* **모델과 checkpoint**
  * TDANN(Margalit et al. 2024, doi:10.1016/j.neuron.2024.04.018): 저장소 README에 가중치를 OSF(osf.io/64qv3)에서 받는다고 적혀 있다. 저장소 LICENSE 파일은 찾지 못했다(404) → 라이선스 미확인. 공간 제약 세기가 다른 가중치들이 공개되어 있는지 미확인.
  * 비교: 공간 제약 없는 같은 구조, 무작위 초기화.
  * GPU 1장.
* **핵심 분석**
  * 모델: 가상 피질 면의 unit마다 규범 정서 평정과의 부분 상관(얼굴, 몸, 장면 선호 통제)을 구해 정서 선호 지도를 만들고, 지도 지표(거리별 선호 상관의 감쇠 길이, 얼룩 수, 범주 지도와의 겹침)를 잰다.
  * 뇌: Horikawa VTC voxel에서 같은 지도와 지표를 cortical mm 단위로 계산한다.
  * 비교: (i) 정서 지도가 범주 지도에 얹힌 정도(겹침)가 모델과 뇌에서 같은가, (ii) 공간 제약을 없앤 모델에서 정서 지도 지표가 사라지는가, (iii) 뇌 정서 지도 중 모델의 범주 지도 기반 예측으로 설명되지 않는 부분의 크기.
* **예측과 반증 조건**
  * 부산물 가설: 모델에서 정서 지도가 범주 지도에 얹혀 생기고, 뇌의 겹침 정도가 모델과 같으며, 공간 제약을 없애면 지도가 사라진다.
  * 정서 특이 조직 가설: 뇌의 정서 지도 지표가 모델의 95% 범위(무작위 시드, 제약 세기)를 넘고, 범주 지도로 설명되지 않는 부분이 피험자 bootstrap에서 0보다 크다.
  * 반증: 모델에 정서 선호 지도가 아예 생기지 않으면(null 수준) 부산물 가설은 이 모델로 시험할 수 없다고 보고한다.
* **4주 계획**
  * 1주: 가중치 확보, 모델 feature, 기준 자극으로 범주 지도 재현.
  * 2주: 모델 정서 지도와 지표, 제약 없는 모델 대조.
  * 3주: Horikawa VTC 지도와 지표, 범주 ROI와 겹침.
  * 4주: 비교와 정리. MC는 ROI가 있으면 재현에 쓴다.
* **가장 가까운 선행과 차이**
  * Margalit et al. 2024 [초록]: TDANN이 여러 시각 영역의 기능 조직을 예측. 과제 일반 표상과 공간 매끄러움의 균형. 정서는 다루지 않았다.
  * Liu et al. 2024 [db]: 물체 인식 DNN의 정서 선택 unit. 공간 배치는 없다.
  * Abdel-Ghaffar et al. 2024 [db], Du 2023 [본문], Lettieri 2019 [본문]: 사람 피질의 정서 관련 tuning과 지도. 모델 비교는 없다.
  * 검색: WebSearch "topographic deep neural network emotion selectivity map emergence affective images ventral temporal cortex wiring cost valence arousal topography"(2026-11-12) → topographic 모델에서 정서 지도를 본 연구 없음. 가장 가까운 것은 Liu 2024.
  * **차이:** 정서 지도의 원천을 공간 제약을 조작한 모델로 시험한다.
* **주요 위험**
  * 가중치 라이선스와 내려받기(OSF) 미확인. 1개월 가능성이 여기에 달려 있다(자체 진단 3점의 이유).
  * TDANN은 ImageNet 정지 이미지로 학습되어 정서 선호가 약할 수 있다.
  * 모델 면과 피질의 축척을 맞추는 규칙이 임의적이다. 지표를 상대값(범주 지도 대비)으로 쓴다.
  * VTC에 한정되어 transmodal 정서 지도(TPJ)는 다루지 못한다.
  * 라벨은 규범 평정이다.

---

## 1. 공통 주의와 다른 담당과의 관계

* **"Horikawa가 이미 다룬 것"과의 거리:** 네 질문 모두 같은 자료의 범주성 재판정이 아니다. GI-RV-1은 축의 의미를 AI로 시험하고, GI-RV-2와 4는 학습 조건과 구조 제약을 조작한 모델을 비교 대상으로 쓰며, GI-RV-3은 decoder로 새 변수를 만든다.
* **증거 수준:** GI-RV-1의 편집 시험은 R1(in-silico), 나머지 분석은 R0이다. 어떤 결과도 실제 뇌의 정서 특이 반응에 대한 인과 주장(R3)이 아니다.
* **D2 주담당(vision-decoding)과의 경계:** GI-RV-3은 decoder 오차의 기하만 다룬다. emotion head 성능 경쟁은 하지 않는다.
* **이전 RQ-01, RQ-03 카드와의 관계:** 두 카드의 무거운 0단계(11명 raw 재전처리)를 이번 질문들은 전제로 하지 않는다. 공개 전처리본과 parcel 수준으로 시작하고, MC 형식 확인 결과에 따라 MC를 더한다.

## 2. 이번 라운드에서 literature.jsonl에 새로 추가한 문헌 (8편)

| ID | 확인 경로 | 읽은 수준 |
|---|---|---|
| arXiv:2310.04420 (BrainSCUBA) | arxiv.org abs | 초록 |
| arXiv:2410.00812 (Generative causal testing) | arxiv.org abs | 초록 |
| arXiv:2112.12750 (SLIP) | arxiv.org abs, GitHub README | 초록과 README(가중치 목록, MIT 표기) |
| doi:10.1038/s42256-023-00753-y (Wang 2023) | Crossref | 서지, preprint(doi:10.1101/2022.09.27.508760) 초록 |
| doi:10.1038/s41467-024-53147-y (Conwell 2024) | PubMed PMID 39477923 | 초록 |
| arXiv:2501.13628 (Chen 2025) | arxiv.org abs | 초록 |
| doi:10.1177/0956797617741718 (Siegel 2018) | Crossref | 초록 |
| doi:10.1016/j.neuron.2024.04.018 (Margalit 2024, TDANN) | PubMed PMID 38733985 | 초록, GitHub README(가중치 위치) |

## 3. 검색 기록 (모두 2026-11-12)

| # | 경로 | 질의 | 결과 | 쓴 곳 |
|---|---|---|---|---|
| 1 | WebSearch | brain-guided image synthesis or natural language explanation of emotion-related brain regions amygdala fMRI generative model selectivity 2025 | 세 요소를 함께 한 연구 없음. Jang & Kragel 2025, BrainDiVE, NeuroVolve가 가장 가까움 | GI-RV-1 |
| 2 | WebSearch | language supervision CLIP versus self-supervised vision model emotion representation alignment human brain fMRI emotional videos controlled training objective | 정서 비디오 fMRI의 통제 비교 없음. 인접: Chen 2025(arXiv:2501.13628), Wang 2023 preprint | GI-RV-2 |
| 3 | WebSearch | fMRI visual reconstruction decoded image bias toward emotional content affective realism decoding error emotional images | 복원 오차의 정서 쏠림 연구 없음 | GI-RV-3 |
| 4 | WebSearch | topographic deep neural network emotion selectivity map emergence affective images ventral temporal cortex wiring cost valence arousal topography | topographic 모델의 정서 지도 연구 없음. 가장 가까운 것은 Liu 2024 | GI-RV-4 |
| 5 | WebSearch | TDANN topographic deep artificial neural network Margalit 2024 pretrained weights code release github | 저장소 위치 확인 | GI-RV-4 |
| 6 | Crossref 서지 질의 | Wang 2023, Conwell 2024, Siegel 2018, Margalit 2024, GCT 제목 | DOI 확인 | 2절 |
| 7 | arxiv.org abs | 2112.12750, 2310.04420, 2410.00812, 2501.13628 | 존재와 초록 확인 | 2절 |
| 8 | GitHub raw | facebookresearch/SLIP, MedARC-AI/MindEyeV2, neuroailab/TDANN, openai/CLIP, facebookresearch/dinov2, timothybrooks/instruct-pix2pix, QwenLM/Qwen2.5-VL의 LICENSE와 README | 코드 라이선스와 가중치 위치 확인. TDANN LICENSE 없음. SLIP 가중치 호스트는 이 세션에서 403 | 모델과 checkpoint 항목 |
