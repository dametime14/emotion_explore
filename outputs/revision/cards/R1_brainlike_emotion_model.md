# R1. 뇌를 닮은 장치를 하나씩 넣고 뺀 AI를 키워 보면, 사람 뇌가 장면의 정서를 다루는 방식은 어떤 장치가 있을 때 나타날까?

* 작성: brain-inspired. 기준일 2026-11-12.
* 지시: `outputs/revision/design_brief.md` 1절, 3절, 4절 R1. 양식: `reference/protocols.md` P7(14개 항목) + Safeguards 점검.
* 직접 읽은 근거 파일:
  * `outputs/revision/design_brief.md` 전체
  * `outputs/revision/feedback_round2.md` 3.1~3.5절
  * `outputs/revision/reviewer_notes.md` 3절, 4절, 7절, 8절
  * `outputs/revision/prior_overlap_audit.md` 2.2, 2.3, 2.5, 3, 7절
  * `outputs/revision/plan.md`
  * 내 `revision_round.md`(BI-RV-1~6)
  * `outputs/agents/frontier-ai/revision_round.md` FA-RV-1, 3, 4절과 0.4, 0.5, 9절
* 출발 재료:
  * BI-RV-1: 되먹임, C-05
  * BI-RV-2: brain-tuning, C-06
  * BI-RV-3: 피질하 지름길, C-07
  * BI-RV-4: 재귀 깊이, C-08
  * BI-RV-5: 지형, C-09
  * FA-RV-1, 3, 4: 학습 목표와 학습 자료, C-16, C-18, C-19
* 이 카드의 한 줄 요약: 같은 출발점의 시각 AI에 사용자가 정의한 brain-like 장치를 통제된 요인으로 넣고 뺀다. 장치는 (a) 구조 제약인 정서 판단의 되먹임과 (c) 사람 뇌 반응에 맞춘 학습(brain-tuning)이다. 그리고 사람 뇌의 정서 서명(signature)이 어느 조건에서 나타나는지로 판정한다. 판정 기준은 encoding 예측력 경쟁이 아니다.

### 이 카드에서 쓰는 말

| 말 | 뜻 |
|---|---|
| 서명(signature) | 사람 뇌에서 관찰된, 모델이 맞혀야 할 특정한 정서 조직 방식. 이 카드는 S1′(주)과 S2(보조)를 쓴다 |
| S1 위계 | 시각, 의미 내용을 통제한 뒤 남는 정서 고유 정보가 감각 영역보다 transmodal 영역에 많다는 관찰(Horikawa 2020) |
| S1′ 정서 초과 위계 | S1의 기울기에서, 같은 방식으로 잰 비정서 추상 속성(사회적 상호작용, 사람 수, 행위 강도 등)의 기울기를 뺀 값. "감각과 고차 영역의 차이 중 정서에만 있는 몫" |
| S2 해리 | 정서 개념 지식이 약해지면 좋고 나쁨(valence) 구분은 남고 부정 정서 범주끼리의 구분이 무너지는 패턴. 의미 치매(Lindquist 2014)와 의미 실어증(Souter 2021) 환자 행동에서 보고됨 |
| 위계 축 | 감각 영역에서 transmodal 영역까지 피질 영역의 순서. 휴지기 기능 연결의 주 경사(principal gradient, Margulies 2016) 값으로 정한다 |
| 모델 예측 뇌 | 각 모델의 특징으로 만든 encoding 모델이 보류 클립에 대해 예측한 ROI 반응. 서명은 실측 뇌와 모델 예측 뇌에서 같은 방식으로 계산한다 |
| brain-tuning | 시각 모델이 사람 fMRI 반응을 예측하도록 모델 자체를 미세조정하는 것. 이 카드에서는 정서와 무관한 NSD 일상 장면 반응으로만 한다 |
| 되먹임(feedback) | 정서 판단 모듈의 상태가 시각 모델의 중간층 활동을 다시 조절하는 연결. 구조 제약 (a)의 대표 |
| 끝까지 미세조정(FF-e2e) | 되먹임 없이 같은 정서 목표로 시각 모델 모든 층을 학습하는 대조 팔. 되먹임 효과를 "깊은 학습" 효과와 가르기 위한 필수 대조(C-05) |
| 논쟁 클립(controversial) | 모델 조건끼리 예측이 가장 크게 갈리는 클립. 최종 판정을 이 클립에서 한다(Golan 2020) |

---

## 1. Core Research Question

정서 영상을 볼 때 사람 뇌는 정서에만 있는 위계를 보인다. 정서 고유 정보가 감각 영역보다 transmodal 영역에 많고, 그 기울기가 비정서 추상 속성의 기울기보다 가파르다(S1′). 같은 출발점의 시각 모델에 아래 셋 중 무엇을 넣었을 때 이 위계가 모델 예측 뇌에서 재현되는가?

1. 정서 판단 모듈의 되먹임
2. 일상 장면에 대한 사람 transmodal 영역 반응에 맞춘 학습
3. 정서 라벨 학습

## 2. Scientific Motivation

* **알려진 것.** Horikawa 2020(doi:10.1016/j.isci.2020.101060)은 시각, 의미 공변량을 넘는 정서 정보가 unimodal-transmodal 경사의 끝(DMN 중심)에 많다고 보고했다. 그러나 관찰 데이터로는 이 위계가 생기는 이유를 가를 수 없다.
* **가르지 못하는 설명 넷.**
  * **일반 추상화:** 어떤 추상 속성이든 고차 영역에 많을 뿐이다. 사용자 지적("감각과 고차 영역의 차이가 전부 정서는 아닐 것")이 이것이다. 시간 통합 창의 위계(Hasson 2008, doi:10.1523/JNEUROSCI.5487-07.2008)도 같은 범주의 대안이다.
  * **개념 학습:** 정서 개념(범주 이름)을 배워야 생긴다. 구성주의의 언어, 개념 가설이다(Lindquist 2014, doi:10.1037/a0035293; Souter, Lindquist & Jefferies 2021, doi:10.1016/j.neuropsychologia.2021.108052).
  * **재진입:** 정서 판단이 감각 영역으로 되먹여야 생긴다. 대립 가설은 시각 학습 자체의 산물이라는 내재 가설이다(Liu et al. 2024, doi:10.1371/journal.pcbi.1011943 Discussion; Bo et al. 2021, doi:10.1093/cercor/bhaa411; Chen, Keil & Ding 2025, doi:10.1167/jov.25.9.1989).
  * **고차 영역의 반응 형식:** 일상 장면을 처리하는 사람 transmodal 영역의 표상 형식 자체가 장면의 정서적 의미를 담는다. 사물 표상이 일상 장면의 정서 schema를 이끈다는 결과(Gao, Ajith & Peelen 2025, doi:10.1101/2025.02.19.638854)와, 정서와 무관한 시각 모델이 정서 평정 분산 대부분을 설명한다는 결과(Conwell et al. 2025, doi:10.1073/pnas.2306025121)가 이 방향을 시사한다.
* **왜 AI가 필요한가.** 사람의 학습 조건이나 경로를 바꿀 수 없다. ANN으로 "왜"를 묻는 연구 프로그램(Kanwisher, Khosla & Dobs 2023, doi:10.1016/j.tins.2022.12.008; Doerig et al. 2023, doi:10.1038/s41583-023-00705-w)은 같은 출발점에서 조건 하나만 바꾼 학습자를 만들어 이 설명들을 서로 다른 예측으로 갈라 준다.
* **왜 서명으로 판정하는가.** 표준 선형 연결은 너무 유연해서 표상이 달라도 encoding 점수가 비슷하게 나온다(Conwell et al. 2024, doi:10.1038/s41467-024-53147-y). AI 특징이 뇌를 더 잘 예측한다는 결과는 이미 흔하다(Huang 2026, arXiv:2611.13637 등, design_brief 3절). 그래서 encoding 설명량은 보조 지표로만 쓴다.

## 3. Origin of the Idea

* **에이전트 결과의 결합:**
  * brain-inspired: Round 1 P-6(정서 전용 구조는 필요한가), Chain 3과 6, Round 2 BI-P3, 재탐색 BI-RV-1~5
  * frontier-ai: FA-RV-1(학습 목표), FA-RV-3(사람 박탈), FA-RV-4(정서 단어 제거)
  * Coordinator: feedback_round2 3.4절(A + C + D 통합, 서명 S1~S3)
  * adversarial-reviewer: 결함 C-05~C-09, 공통 비판 8절
  * geometry-info R3(재현 뇌 축, 확장에서 서명으로 받음)
* **가져온 분야:** NeuroAI의 통제된 학습자(Axis N, I, J), brain-tuning(Axis J), 구성주의 정서 이론과 신경심리 해리(Axis A), 표상 기하(Axis K).
* **후보 ID:** C-05, C-06, C-07, C-08, C-09(brain-inspired), C-16, C-18, C-19, C-20(frontier-ai). matrix 조합 번호는 이번 재탐색 라운드에서 새로 매기지 않았다.

## 4. Prior Literature

### 4.1 직접 관련 선행과 기여

| 선행 | 식별자 | 확인 | 이 카드와의 관계 |
|---|---|---|---|
| Horikawa et al. 2020, iScience | doi:10.1016/j.isci.2020.101060 | Crossref, 본문 Discussion | S1의 출처. 공변량 비교로 정서 고유 정보의 transmodal 위치를 보고 |
| Kragel et al. 2019, Sci Adv (EmoNet) | doi:10.1126/sciadv.aaw4358 | Crossref, 본문 | 정서 지도 CNN과 후두엽. C&K 프레임 학습이라 이 카드에서는 쓰지 않는다(누수) |
| Liu et al. 2024, PLoS CB | doi:10.1371/journal.pcbi.1011943 | Crossref, 본문 | 물체 학습 망의 정서 선택 unit. 내재 대 재진입을 미해결로 남김. 뇌 비교 없음 |
| Gao, Ajith & Peelen 2025, bioRxiv | doi:10.1101/2025.02.19.638854 | Crossref | 일상 장면에서는 사물 학습 모델이, 정서 유발 자극에서는 정서 학습 모델이 정서 평정을 더 잘 예측. BOLD5000 LOC |
| Soderberg, Jang & Kragel 2026, SCAN | doi:10.1093/scan/nsag028 | Crossref | 표정 대 장면으로 정서를 학습한 ANN으로 pSTS, 편도체 fMRI 예측. 학습 과제를 바꾼 정서 ANN과 정서 영역 fMRI의 가장 가까운 선행 |
| Conwell et al. 2024, Nat Commun | doi:10.1038/s41467-024-53147-y | Crossref | 구조, 목표의 뇌 예측 차이는 작고 데이터가 주 요인. 선형 연결의 유연성 경고 |
| Conwell et al. 2025, PNAS | doi:10.1073/pnas.2306025121 | Crossref | 정서 없는 지각 모델이 정서 평정 분산 대부분을 설명(뇌 없음) |
| Chen, Keil & Ding 2025, J Vis (VSS) | doi:10.1167/jov.25.9.1989 | Crossref(존재), 내용은 검색 요약 | 합성 fMRI로 재진입 가설 검정. 모델에 되먹임을 넣지는 않음 |
| Liu et al. 2025, bioRxiv (VCA) | doi:10.1101/2025.10.20.683439 | Crossref 초록 | ViT + 편도체 모사 모듈(피드포워드), 편도체 fMRI 정렬 |
| Leem, Keil, Ding, Fang 2026 | arXiv:2607.19327 | arXiv, 본문 | 지름길 경로가 Pavlov 조건화에 필요. 뇌 비교 없음 |
| Méndez et al. 2022, Phil Trans B | doi:10.1098/rstb.2021.0512 | Crossref | 상구 모사 DNN, 표정 인식, 사람 SC 7T. 피질하 경로 모델의 선행 |
| Lu & Wang 2024 (ReAlnet-fMRI) | arXiv:2407.10414 | arXiv 초록 | CORnet을 사람 fMRI로 최적화해 뇌 유사도를 높임. 시각 영역, 정서 아님. brain-tuning의 시각판 선행 |
| Policzer, Braunstein & Toneva 2025 | arXiv:2511.07988 | DB | 사회 인지 영역(STS) brain-tuning, 사회 과제 성능 |
| Margalit et al. 2024, Neuron (TDANN) | doi:10.1016/j.neuron.2024.04.018 | Crossref, 본문 | 지형 제약 모델. checkpoint는 OSF(osf.io/64qv3), 코드는 GitHub(Data and Code Availability 원문) |
| Kar et al. 2019; Kietzmann et al. 2019 | doi:10.1038/s41593-019-0392-5; doi:10.1073/pnas.1905544116 | Crossref | 재귀의 필요성(물체 인식, 시각 동역학) |
| Spoerer et al. 2020, PLoS CB | doi:10.1371/journal.pcbi.1008215 | Crossref | 시간 단계가 많은 재귀 망(BLT). C-08 대안 |
| Tugsbayar et al. 2026, eLife | doi:10.7554/eLife.105953 | Crossref | top-down 되먹임 구성이 같은 연결의 모델을 기능적으로 다르게 만든다(시청각 범주화, 정서 아님) |
| Lindquist et al. 2014; Souter et al. 2021 | doi:10.1037/a0035293; doi:10.1016/j.neuropsychologia.2021.108052 | DB; Crossref | S2 해리의 출처(환자 행동) |
| Golan, Raju & Kriegeskorte 2020, PNAS | doi:10.1073/pnas.1912334117 | DB | 논쟁 자극으로 모델 판정 |

### 4.2 선행 검색 기록 (구성 요소마다 질의 2개 이상, 모두 2026-11-12)

| 구성 요소 | 질의(경로) | 결과 |
|---|---|---|
| 되먹임(재진입) | (1) WebSearch "recurrent feedback from valence or amygdala module to visual network deep learning model reentry emotional images compared with visual cortex fMRI emotion representation" (2) WebSearch "top-down feedback recurrent deep network emotional salience visual cortex representation model comparison fMRI 2025 2026 reentry hypothesis model" | 정서 모듈의 되먹임을 조작해 사람 시각피질의 정서 표상과 비교한 연구는 미발견. 인접: VCA(피드포워드), Chen 2025 VSS(합성 fMRI, 되먹임 조작 없음), Tugsbayar 2026(되먹임 구성, 정서 아님), 예측 부호화 단위를 넣은 VGG16이 고차 시각피질 정렬을 높였다는 ESANN 2025 논문(search_index, 식별자 미확인) |
| brain-tuning | (1) WebSearch "brain-tuning fine-tune vision or video model on amygdala or emotion-related fMRI responses improves human emotion judgment alignment" (2) WebSearch "brain-tuning vision model fine-tuned on fMRI responses natural scenes improves generalization 2025 2026 NSD fine-tune backbone brain-aligned" (3) WebSearch "neural network trained to predict human brain activity then tested on emotional images affective representation emerges brain-optimized model 2024 2025 2026" | 시각 영역 brain-tuning은 있다(ReAlnet-fMRI arXiv:2407.10414; Brainformer arXiv:2312.00236). 사회 영역은 Policzer 2025, 음성은 Moussa 2024(arXiv:2410.09230). **정서와 무관한 장면 반응으로 brain-tuning한 모델이 정서 서명을 만드는지 본 연구는 미발견** |
| 피질하 두 경로 | (1) WebSearch "dual pathway subcortical cortical deep neural network model emotion amygdala superior colliculus 2024 2025 2026 fMRI comparison" (2) Round 2와 재탐색의 WebSearch 기록(BI-P3, BI-RV-3) | 2024~2026년 이중 경로 DNN과 fMRI 비교는 미발견. 가장 가까운 것은 Méndez 2022(상구 단일 경로 모델)와 Leem 2026 |
| 지형 | (1) WebSearch "topographic deep neural network emotion selectivity map emerges cortical organization emotional images face body scene patches TDANN All-TNN" (2) WebSearch "topographic neural network affective emotional stimuli spatial organization amygdala-like or valence map 2024 2025 2026" | 지형 모델의 정서 선호 지도 연구는 미발견. 인접: fMRI 정서 지형 연구(emotionotopy), 공포 조건화 지형 지도 학회 초록(search_index) |
| 서명 재현(위계) | WebSearch "deep network model reproduces unimodal-to-transmodal gradient of emotion representation brain hierarchy non-emotional abstract features control social interaction" | 음악 CNN 층 경사와 피질 경사의 대응을 본 학회 초록(TeaP 2025, OHBM 2024 포스터, search_index)만. 비정서 추상 속성 통제와 모델 조건 조작을 결합한 연구는 미발견 |

* "미발견"은 이 검색 경로 안의 결과다. Stage 2 표본에서 no 판정의 약 25%가 뒤집혔으므로 최종 선정 전 중복 감사를 다시 해야 한다.

## 5. Novelty

* **판정: partially(구성 요소는 각각 선행이 있고, 결합과 판정 방식이 새롭다).**
* **가장 가까운 선행과의 차이:**
  * **Soderberg, Jang & Kragel 2026:** 학습 과제(표정 대 장면)를 바꾼 정서 ANN으로 정서 영역을 예측했다. 이 카드는 학습 과제가 아니라 brain-like 장치(되먹임, brain-tuning)를 통제 요인으로 넣는다. 판정도 영역별 예측력이 아니라 피질 위계 전체의 정서 초과 기울기(S1′)와 해리(S2)로 한다.
  * **Gao 2025, Conwell 2025:** 정서 학습 대 사물 학습, 정서 없는 모델의 설명력을 행동 평정 위주로 보였다. 이 카드는 같은 출발점에서 정서 라벨 학습 유무를 조작한다. 그리고 그 효과를 비정서 추상 속성의 위계로 통제해 "정서 고유"와 "일반 추상화"를 가른다.
  * **ReAlnet-fMRI, Policzer 2025:** brain-tuning의 목표가 뇌 유사도나 해당 영역 과제였다. 이 카드는 정서와 무관한 NSD 일상 장면의 transmodal 반응으로 조율한다. 그다음 다른 코호트(Horikawa, MC)의 정서 영상 반응에서 정서 서명이 생기는지 본다. 조율과 평가의 자극 분포, 피험자, 스캐너를 모두 분리해 C-06의 순환을 피한다.
  * **Chen, Keil & Ding 2025, VCA, Leem 2026(같은 연구군):** 재진입 쟁점을 합성 fMRI나 피드포워드 모듈로 다뤘다. 이 카드는 같은 망에서 되먹임 연결 자체를 조작한다. 여기에 매개변수를 맞춘 끝까지 미세조정 팔(C-05)과 섞은 라벨 되먹임 팔로 귀속을 엄격히 한다. 다만 이 연구군이 같은 쟁점을 연속으로 다루고 있어 선점 위험이 크다.
* **연구실 팀원 'TRIBE + emotion head' 작업과의 차이(overlap: 연구실 팀원 TRIBE 작업, 개념 인접).** TRIBE도 뇌 반응에 맞춰 학습한 모델이므로 사용자 정의의 (c)와 개념이 인접한다. 차이는 다섯 가지다.
  1. **조작 대상:** TRIBE 작업은 이미 학습된 다중양식 뇌 encoder에 정서 판독을 붙인다. R1은 작은 시각 모델을 같은 초기값에서 직접 키우며 brain-tuning의 유무와 표적 영역을 통제 요인으로 조작하고, 구조 제약(되먹임)과 교차시킨다.
  2. **양식:** R1은 시각 전용이다(C&K 무음). TRIBE는 소리 있는 영화로 학습되어 무음 입력이 분포 밖이다(plan.md 4절).
  3. **조율 자료:** R1의 brain-tuning은 정서와 무관한 NSD 정지 장면의 영역별 반응이다. TRIBE는 영화 전체 뇌 반응의 피험자 평균 예측기다.
  4. **판정:** R1은 정서 판독 정확도를 결과로 쓰지 않는다. 사람 뇌 서명(S1′, S2)이 어느 조건에서 나타나는지로 판정한다.
  5. **사용 모델:** R1은 TRIBE를 쓰지 않는다.

## 6. Proposed Dataset

| 자료 | 쓰는 곳 | 실제로 있는 것(Stage 1, plan.md 4절 기준) | 관문, 주의 |
|---|---|---|---|
| Horikawa 2020 | 서명 계산(실측), 모델 예측 뇌의 encoding 학습과 평가 | 5명, 고유 2,181클립(무음, 평균 약 5 s) 단일 제시. 블록 평균 native volume HDF5에 HCP360과 피질하 ROI 포함. C&K 34범주와 14차원 규범 평정. 원본 비디오 보유(사용자 확인) | 반복 없음(noise ceiling 없음). pulvinar ROI 없음. TE 43 ms(피질하 신호 약함). 같은 원본에서 잘린 클립의 movie-level leakage 미확인 |
| Mind captioning(MC) | 같은 서명의 독립 코호트 재현, noise ceiling | 6명, 학습 2,108클립 고정, 시험 72클립 x 5회(plan.md 4절). 정서 배제 지시로 받은 사람 캡션(GPT-3.5 교정). 전처리 완료 보유본 | **관문: 보유본 전처리 형식 미확인.** 원 논문 방식(4 s shift 후 블록 평균)으로 맞출 수 있는지 1주차 확인. 시험 72클립은 학습 세션 마지막 두 run에도 나왔다(학습은 2,108로 고정) |
| NSD | brain-tuning 표적(정서와 무관한 자극 분포) | 8명, 7T, 1인당 약 1만 장 COCO, GLMsingle beta. pRF, fLoc, streams, nsdgeneral ROI(Stage 1) | transmodal 표적은 공개 HCP-MMP 주석을 fsaverage beta에 대응시켜 정의한다. 대응 절차는 미확인. NSD 이미지 정서가는 대체로 중립(의도한 성질) |
| EmoSet-118K | 정서 라벨 학습 | 118,102장, Mikels 8범주(긍정 4, 부정 4: anger, disgust, fear, sadness), 별도 평정자의 perceived 라벨(arXiv:2307.07961, DB) | 이미지와 라벨 이용 조건 미확인(frontier-ai: 코드 저장소 MIT 확인). C&K 프레임, Horikawa/MC 프레임, NSD 이미지와 지각 해시 중복 검사 |
| MC 캡션에서 뽑은 비정서 속성 | S1′의 비정서 통제 | 사람 수, 사회적 상호작용 유무와 강도, 행위 강도, 실내외, 동물 유무 | 사람이 쓴 캡션에서 규칙과 공개 언어 모델로 추출(AI 추정 표기). 캡션의 정서 표현은 드물다(plan.md 4절) |

* **쓰지 않는 자료와 이유:**
  * Emo-FilM과 Spacetop: 소리 있는 영상이라 무음 시각 모델의 서명 비교와 맞지 않는다. 확장에서 R3 축이나 다른 코호트 재현에만 검토한다.
  * EmoNet: 누수.
  * TRIBE v2: 분포 밖이고 팀원 작업과 구분해야 한다.
  * 웹 규모 VLM: C&K 오염 가능성.
* **라벨 주체:** C&K 평정은 별도 평정자가 영상을 보고 보고한 정서의 집계다. 주장은 "장면의 정서적 의미(규범 기준)"까지만 한다(design_brief 3절 5번).

## 7. Proposed Computational Framework

### 7.1 4주 핵심 판(core): 요인 2개 + 대조 팔

모든 팔은 같은 출발점(ImageNet 사전학습 ResNet-50, torchvision 공개 가중치)에서 시작한다. 각 팔은 seed 3개로 학습한다.

| 팔 | brain-tuning (c) | 정서 학습과 구조 (a) | 역할 |
|---|---|---|---|
| A0 | 없음 | 없음 | 출발점. 일반 추상화 가설의 기준 |
| B-tm | NSD transmodal ROI | 없음 | "사람 고차 영역의 반응 형식"이 정서 서명을 만드는가 |
| B-vis | NSD 시각 ROI | 없음 | 대조: 조율 자체의 효과 |
| B-rand | 신뢰도를 B-tm 표적에 맞춘 무작위 비시각 parcel | 없음 | 대조: transmodal이라서가 아니라 신호 품질 때문인지 |
| E-ff | 없음 | EmoSet 8범주 + valence, 모든 층 학습, 입력을 끈 같은 크기 gain 모듈 포함 | 끝까지 미세조정 팔(C-05 대조) |
| E-fb | 없음 | 같은 목표, 정서 모듈의 되먹임이 중간층(layer2, layer3)을 채널별 gain으로 조절, 두 번 통과 | 재진입 구조 제약 |
| E-fb-shuf | 없음 | E-fb와 같은 구조, 라벨 섞음 | 대조: 되먹임의 용량 효과 |
| B-tm → E-ff | NSD transmodal ROI 다음 | E-ff | 상호작용 |
| B-tm → E-fb | NSD transmodal ROI 다음 | E-fb | 상호작용 |

* **판별력이 가장 높다고 본 이유.**
  * 일반 추상화, 개념 학습, 재진입, 고차 반응 형식이라는 네 설명이 이 9개 팔에서 서로 다른 패턴을 예측한다(10절 표).
  * 학습 자료 조작(사람 제거, 정서 단어 제거)은 Conwell 2024로 보면 큰 요인이다. 그러나 이 중심 질문에서는 개념 학습 가설의 세부 검정에 해당하므로 확장으로 둔다(7.2절).
* **입력:** C&K 클립마다 균등 간격 프레임 8장, 224 px. 무음이라 시각만 쓴다. 정지 프레임 평균은 움직임 정보를 잃는 공통 불리함이 있다(reviewer_notes 8절 3번). 모든 팔에 같게 작용하므로 팔 간 비교는 유지된다.
* **출력과 손실:**
  * 정서 학습: EmoSet 8범주 교차엔트로피 + valence(긍정/부정) 보조 손실
  * brain-tuning: NSD 피험자별 선형 readout으로 ROI beta 예측, voxel별 상관 손실. 표적 피험자 4명(세션 수가 가장 많은 피험자, 목록은 1주차에 Stage 1 보고서와 대조), 학습/검증은 이미지 단위 분할
  * 되먹임: 정서 모듈 은닉 벡터에서 선형층을 거쳐 layer2, layer3 출력에 (1 + tanh) gain을 곱한다. 첫 통과로 정서 상태를 만들고 두 번째 통과에서 적용한다. E-ff에는 같은 크기의 gain 모듈을 두되 입력을 상수로 고정해 매개변수 수를 맞춘다
* **학습 성공 확인:** EmoSet 보류 정확도, NSD 보류 이미지의 ROI 예측 상관, ImageNet 보류 정확도(물체 표상이 무너지지 않았는지).
* **관련 뇌 영역과 위계 축:**
  * HCP360 parcel을 Margulies 2016 주 경사(doi:10.1073/pnas.1608282113) 값으로 정렬한다. parcel별 경사 값의 공개 자료는 1주차에 확보한다(미확인).
  * 사전 지정 묶음: 초기 시각(V1~V3), 고차 시각(LOC, VTC, MT 주변), 측두-두정 연합(TPJ, STS), transmodal(PCC/precuneus, mPFC, 측두극).
  * 피질하는 핵심 판에서 판정에 쓰지 않는다(C-07).
* **통계 목표와 해석 방법:** 서명 계산(8.1절), 무게를 다시 주지 않는 RSA와 가중 RSA 병기(Conwell 2024 경고 반영), 논쟁 클립 판정, 모델 내 lesion(되먹임 차단, brain-tuning 전후 비교).
* **GPU 추정(미검증, 실측 아님):**
  * EmoSet 미세조정: 회당 약 1~2 GPU 시간(약 118만 장 처리)
  * NSD brain-tuning: 회당 약 1~2 GPU 시간
  * 27회 합계 약 30~60 GPU 시간. GPU 2~4장이면 2주차 안에 끝난다
  * encoding과 서명 계산은 CPU

### 7.2 확장(4주 이후, 핵심 판 결과에 따라)

| 확장 | 내용 | 연결된 결함 | 전제 |
|---|---|---|---|
| X1 피질하 두 경로 | 저공간주파수, 초기층 지름길에서 정서 모듈로 가는 경로를 켜고 끈다(Leem 2026 구조) | C-07: Horikawa ROI에 pulvinar 없음, 편도체 신호 약함(3T, TE 43 ms). Méndez 2022 선행 | MC 반복으로 편도체 신뢰도 관문 통과 시에만. 시상은 전체 ROI로만 |
| X2 재귀 깊이와 S3 | 시간 단계가 많은 재귀 망(BLT, Spoerer 2020)으로 클립별 정서 판독 재귀 요구량을 계산하고 클립별 정서 정보 위치(S3)를 예측 | C-08: CORnet-S는 재귀 단계가 적다 | BLT 가중치 공개와 이용 조건 미확인. 없으면 같은 구조를 ImageNet 하위 집합으로 직접 학습(무거움) |
| X3 지형 | TDANN 공개 checkpoint에서 정서 선호 단위의 공간 군집과 얼굴, 신체, 장면 구역과의 관계를 분석하고 MC fLoc 지도와 비교 | C-09: 학습이 무겁고 LICENSE가 없다(Coordinator 확인). checkpoint는 OSF에 공개(Margalit 2024 원문) | 이용 조건을 저자에게 확인한 뒤 분석만 한다(재학습 없음) |
| X4 학습 자료 | 정서 단어 제거(Affection 자료, FA-RV-4), 사람 제거(COCO, FA-RV-3) | 핵심 판에서 개념 학습 가설이 지지될 때 S2 해리의 원인을 좁히는 검정 | Affection 이용 조건 미확인 |
| X5 R3 재현 축 | geometry-info R3가 넘겨 주는 재현 뇌 축(축 정의, 클립 점수, 신뢰도)을 추가 서명으로 쓴다 | 없음 | R3 결과 |

## 8. Proposed Analyses

### 8.1 서명 계산 (실측 뇌와 모델 예측 뇌에서 같은 절차)

1. **모델 예측 뇌 만들기.**
   * 각 팔의 층별 특징으로 피험자, ROI별 ridge encoding을 학습한다. Horikawa는 클립 단위 5겹 교차검증, MC는 2,108 학습 / 72 평가다.
   * 층은 학습 클립 안의 중첩 교차검증으로 고른다.
   * 그 결과로 보류 클립의 예측 반응을 만든다.
2. **정서 고유 정보.**
   * 각 ROI에서 C&K 지배 범주별로 클립을 두 반으로 나눠 범주 중심 간 교차검증 거리(crossnobis)를 구한다.
   * 이 거리 행렬과 34차원 규범 평정 RDM의 부분 상관을 계산한다. 통제 RDM은 저수준 영상 통계(밝기, 대비, 색, 움직임 에너지)와 캡션 명사에서 만든 사물, 장면 RDM이다.
   * 비정서 속성 RDM도 함께 통제한다.
3. **비정서 추상 속성의 고유 정보.** 같은 절차를 사람 수, 사회적 상호작용, 행위 강도 RDM에 적용한다. 정서 RDM을 통제한다(상호 통제).
4. **S1 기울기와 S1′.**
   * ROI별 고유 정보를 위계 축 값에 회귀한 기울기를 구한다.
   * S1′ = 기울기(정서) − 기울기(비정서 평균)이다.
   * 신뢰구간은 클립 bootstrap으로 구한다.
5. **S2.**
   * transmodal 묶음과 초기 시각 묶음에서 긍정 대 부정 중심 거리(valence 분리)를 잰다.
   * 부정 범주끼리(anger, anxiety, disgust, fear, horror, sadness, empathic pain 중 클립 수가 충분한 것)의 평균 중심 거리를 잰다.
   * 둘의 비율 R_S2를 구한다.
6. **모델 자체 공간의 병기.**
   * 무게를 다시 주지 않는 RSA로 모델 층 RDM에서 같은 정서 고유 정보를 계산한다.
   * 층 깊이에 따른 기울기를 함께 보고한다.
   * 선형 연결의 유연성에 덜 기대는 판정이다.

### 8.2 판정과 비교

* **1차 지표:** 각 팔의 모델 예측 뇌 S1′이 실측 S1′의 95% 구간 안에 드는가. ROI별 정서 고유 정보 프로필이 실측과 상관하는가(피험자별, 코호트별).
* **비교 조건과 기준선:**
  * A0, 무작위 초기화 ResNet-50(구조만의 기준선)
  * 피험자 간 상한: 다른 피험자의 실측 프로필로 예측한 값
  * MC noise ceiling
* **ablation:**
  * E-fb의 시험 시점 되먹임 차단
  * E-fb 대 E-fb-shuf, E-fb 대 E-ff(매개변수 맞춤)
  * B-tm 대 B-rand 대 B-vis
* **통계:**
  * 팔 간 차이는 seed 3개 x 피험자 11명의 계층 모형으로 본다.
  * 동등성 한계(seed 간 변동의 95% 범위)를 사전 등록해 "차이 없음"을 해석 가능하게 만든다(reviewer_notes 8절 4번).
  * ROI 묶음 4개 x 서명 2개의 다중 비교는 Holm 보정한다.
* **논쟁 클립 판정:** 핵심 팔 쌍(E-fb 대 E-ff, B-tm 대 B-rand, B-tm 대 A0)의 예측이 가장 갈리는 클립을 MC 학습 클립 안에서 미리 고른다. 그 클립에서 실측 뇌가 어느 쪽을 따르는지로 최종 판정한다(Golan 2020).
* **검증 전략:** Horikawa에서 발견하고 MC에서 확인한다. 두 코호트는 스캐너가 달라(Verio 대 Prisma) 코호트 안에서 따로 분석한다. encoding 설명량(R²)과 R² 대비 비율은 보조 표로만 낸다.

## 9. Competing Explanations

| 대안 설명 | 무엇이 같은 결과를 만드나 | 가르는 분석 |
|---|---|---|
| 일반 추상화 위계 | 어떤 추상 속성이든 고차 영역에 많다 | S1′(비정서 속성 기울기 빼기). 사람에서 S1′ ≈ 0이면 이 설명이 이긴다 |
| 시간 통합 창 위계(Hasson 2008) | 고차 영역의 긴 통합 창이 긴 맥락 속성을 담는다 | 블록 평균 자료로는 가를 수 없다. 이론적으로 가능하지만 관찰 데이터로 구분할 수 없는 설명으로 표시한다 |
| 학습량, 용량 | 정서 학습 팔이 그냥 더 많이 학습했다 | 모든 팔의 step 수 고정, 매개변수 맞춘 gain 모듈, E-fb-shuf |
| 조율 표적의 신호 품질 | transmodal 표적이 신뢰도가 높아서가 아니라 조율 자체 효과 | B-rand(신뢰도 맞춤), B-vis |
| 의미 내용 누출 | 캡션 통제가 놓친 사회 내용이 정서처럼 보인다 | 비정서 속성 상호 통제, 논쟁 클립, 사람 수 층화 |
| 시선, 주의 이득 | 정서 클립에서 시선이 다르다 | MR 기반 시선 추정(DeepMReye, doi:10.1038/s41593-021-00947-w)은 촬영 범위 확인 후 공변량으로(확장) |
| 라벨 측정 오차 | 34범주 평정의 잡음이 정서 고유 정보를 낮춘다 | 모든 팔에 같게 작용하므로 팔 간 비교에는 영향이 작다. 절대값은 해석하지 않는다 |
| 학습 자료 오염 | ImageNet, EmoSet에 C&K 유사 이미지 | 지각 해시 중복 검사, 중복 제거 판 재학습 |

## 10. Potential Findings

사전 등록할 결과 지도다. "재현"은 8.2절 1차 지표 기준이다.

| 관찰 패턴 | 해석 | 정서 이론에 주는 말 |
|---|---|---|
| 사람 S1′ ≈ 0(1주차 관문) | Horikawa의 위계는 일반 추상화 위계다 | 사용자 지적이 맞다. "정서의 고차 위치"는 정서 고유 주장이 아니다. 핵심 판은 축소하고 결과를 보고한다 |
| 사람 S1′ > 0이고 A0이 재현 | 정서 초과 위계가 일반 시각 학습만으로 생긴다 | 내재 가설과 지각 우선(Conwell 2025) 쪽 |
| E-ff와 E-fb만 재현, B 팔은 못 함 | 정서 개념 라벨 학습이 필요하다 | 구성주의의 개념 학습 가설과 정합. S2도 E 팔에서만 재현되면 Lindquist 해리와 같은 방향 |
| E-fb만 재현, E-ff는 못 함(매개변수 맞춤) | 정서 판단의 되먹임이라는 구조가 필요하다 | 재진입 가설과 정합(표상 내용 수준. 시간 순서 증거는 아님) |
| B-tm만 재현(정서 라벨 없이), B-rand와 B-vis는 못 함 | 일상 장면에 대한 사람 고차 영역의 반응 형식이 정서적 의미의 조직을 이미 담는다 | 정서적 의미가 장면 이해의 일반 고차 표상 안에 놓인다는 해석(Gao 2025 방향). 정서 전용 학습 없이 생긴다 |
| B-tm → E-fb에서만 재현 | 고차 반응 형식과 되먹임이 함께 필요하다 | 두 기제의 결합 |
| 어느 팔도 재현 못 함 | 시각 학습자와 이 장치들로는 사람의 정서 초과 위계를 만들 수 없다 | 시각 밖 요인(신체 상태, 평가, 언어 맥락)이 필요하다는 음성 결과. 동등성 한계로 해석한다 |

## 11. Scientific Contribution

* **질문의 성격.** Affective Neuroscience의 "정서는 뇌에서 어디에, 왜 그렇게 놓이는가"를 관찰이 아니라 통제된 인공 학습자로 묻는다. plan.md 2절 (a)에 해당한다(학습 조건을 조작한 인공 뇌, 구조 제약을 바꾼 모델).
* **이론적 기여 세 갈래.**
  1. 정서의 고차 위치가 정서 고유인지 일반 추상화인지(사용자 지적에 대한 직접 답)
  2. 구성주의 개념 학습 가설과 지각 우선 가설의 대립에 학습자 수준의 판정을 준다
  3. 시각피질 정서 정보의 재진입 대 내재 논쟁에 표상 내용 수준의 판정을 준다
* **다른 연구와의 구분.** 결론은 "어떤 장치가 있어야 사람 뇌의 정서 서명이 나타나는가"다. AI 특징의 예측력 순위가 아니다.
* **결론의 범위.**
  * "뇌가 실제로 그 장치를 쓴다"는 증명이 아니라 "그 장치가 있는 학습자가 사람 뇌와 닮는다"다(evidence-level R1 + R0).
  * 정서 라벨이 규범 평정이므로 결론은 장면의 정서적 의미에 대한 것이다.

## 12. Limitations & Risks

| 위험 | 내용 | 대응 또는 명시 |
|---|---|---|
| C-05 되먹임 귀속 | 끝까지 미세조정만으로도 시각층 정서 성분이 생길 수 있다 | **해결:** E-ff(매개변수 맞춤) 팔과 E-fb-shuf. 일반적인 미세조정은 주로 후기 층을 바꾼다는 점(C-20)은 층별 변화량으로 함께 보고 |
| C-06 brain-tuning 순환 | 같은 C&K 분포에서 조율, 평가하면 영역-정서 상관을 옮길 뿐이다 | **해결:** 조율은 NSD(정지 일상 장면, 7T, 다른 피험자)로만, 평가는 Horikawa/MC의 C&K 정서 영상으로만. C&K 라벨과 반응은 조율에 쓰지 않는다. B-rand, B-vis 대조 |
| C-07 피질하 | Horikawa ROI에 pulvinar 없음, 편도체 신호 약함(3T, TE 43 ms). Méndez 2022 선행 | **한계로 명시하고 확장(X1)으로 뺀다.** 핵심 판 판정에 피질하를 쓰지 않는다 |
| C-08 재귀 단계 | CORnet-S는 재귀 단계가 적어 클립별 계산 깊이 해상도가 낮다 | **확장(X2)으로 뺀다.** BLT(시간 단계 많음, 가중치 이용 조건 미확인)를 우선 검토 |
| C-09 지형 | TDANN 학습이 무겁고 LICENSE가 없다 | **확장(X3), 분석 전용.** 공개 checkpoint(OSF)는 있다. 이용 조건을 저자에게 확인하기 전에는 쓰지 않는다 |
| 선점 | Ding, Keil 연구군이 재진입 쟁점을 연속으로 다룸(VCA, Leem 2026, VSS 2025) | 되먹임 팔은 E-ff 대조와 S1′ 판정으로 차별화. 선점되면 B 팔(brain-tuning)이 주 기여로 남도록 요인을 교차했다 |
| 작은 표본 | 11명, Horikawa 반복 없음 | MC로 재현, 피험자 간 상한, 계층 모형 |
| null 결과 | Conwell 2024처럼 팔 간 차이가 작을 수 있다 | 동등성 한계 사전 등록, 결과 지도(10절)에 null 해석 포함 |
| 도메인 차이 | EmoSet 정지 이미지 대 C&K 영상, NSD 정지 장면 | 모든 팔에 공통. 절대 성능은 비교하지 않는다 |
| 이용 조건 | EmoSet 이미지, torchvision 가중치, HCP-MMP 주석, BLT, TDANN | 1주차 확인 목록. 확인 안 되면 대체 자료(FindingEmo 등)로 바꾼다(frontier-ai 0.4절) |
| MC 형식 | 보유본 전처리 형식 미확인 | 1주차 관문. 맞지 않으면 raw(ds005191)에서 원 논문 절차로 다시 만든다(1주 추가 위험) |
| 비정서 속성 추출 | 캡션에서 AI로 추출한 속성의 타당성 | 소표본 사람 확인(연구자 본인 100클립 점검), AI 추정 표기 |

## 13. Pilot Experiment (1주차, GPU 거의 불필요)

1. Horikawa 5명과 MC 6명에서 **실측 S1, S1′, S2**를 계산한다. 이를 위해 비정서 속성을 캡션에서 추출하고, 위계 축을 정하고, 범주 중심 crossnobis를 구한다.
2. A0(ImageNet ResNet-50)의 모델 예측 뇌에서 같은 서명을 계산한다.
3. **의사결정 규칙(사전 등록):**
   * 실측 S1′의 95% 구간이 두 코호트 모두에서 0을 포함하면, 핵심 판을 "일반 추상화 위계" 보고로 축소한다. 모델 팔은 A0와 E-ff만 남긴다.
   * 실측 S1′ > 0이고 A0이 이미 재현하면, 주 질문은 "무엇이 그 재현을 깨는가"(lesion, 자료 박탈 X4)로 옮긴다.
   * 실측 S1′ > 0이고 A0이 재현하지 못하면, 계획대로 2주차 27회 학습으로 간다.
   * MC 형식이 맞지 않으면 Horikawa로만 진행하고 MC 재생성을 병행한다.

## 14. Feasibility & Priority

| 항목 | 자체 판단 | 근거 |
|---|---|---|
| Novelty | 3.5/5 | 구성 요소는 선행이 있다(Soderberg 2026, Gao 2025, ReAlnet, Chen 2025). brain-like 장치의 교차 조작, 비정서 통제 서명 판정, 분포를 분리한 brain-tuning의 결합은 검색 범위에서 미발견 |
| AI-enabled Affective Neuroscience Contribution | 4/5 | 관찰로 만들 수 없는 통제 학습자를 쓰고, 결론이 정서 이론 세 쟁점에 직접 닿는다. 결론 범위는 R1 + R0 |
| Neuroscientific Importance | 4/5 | Horikawa의 핵심 결과를 다시 판정하지 않는다. 그 결과가 "정서 고유인가, 왜 생기는가"를 묻는다 |
| 1-month Feasibility | 4/5 | 공개 가중치, 작은 모델, 새 수집 없음. 위험은 MC 형식과 EmoSet 이용 조건 |
| 전체 권고 | **R1 핵심 판을 1순위 후보로 둔다** | 1주차 관문(13절)이 실패해도 사용자 지적에 대한 답이라는 정보가 남는다 |

* **4주 계획:**
  * 1주: 관문(MC 형식, 이용 조건, 중복 검사), 실측 서명, A0 파일럿(13절)
  * 2주: 9개 팔 x seed 3 학습, 학습 성공 확인
  * 3주: 모델 예측 뇌, 서명, 무게를 다시 주지 않는 RSA, 모델 내 lesion
  * 4주: 논쟁 클립 판정, MC 재현, 동등성 검정, 보고
* **overlap:**
  * overlap: 연구실 팀원 TRIBE 작업. 뇌 반응에 맞춰 학습한 모델이라는 개념이 인접한다. 차이는 5절.
  * overlap: EmoViS(정서 기하의 감각-의미 기원 질문과 부분 겹침. R1은 모델 조건 조작으로 접근).
  * overlap: EmoBrain(뇌 정서 정보를 모델 학습에 쓰는 발상과 부분 겹침. R1의 brain-tuning은 정서와 무관한 NSD로 한다).

---

## Safeguards 점검 (CLAUDE.md 6절)

| 항목 | 상태 |
|---|---|
| 참가자가 경험한 정서 vs 자극에 묘사된 정서 | C&K 평정은 별도 평정자가 보고한 정서의 집계. 주장은 장면의 정서적 의미(규범)까지 |
| 사람 주석 vs 모델 생성 주석 | 비정서 속성은 사람 캡션에서 AI로 추출(AI 추정 표기). 정서 라벨은 사람 평정만 |
| 본인 보고 vs 규범 평정 | 본인 보고 없음. 해석 범위 제한 |
| 정서 표상 vs 시각/의미 내용 표상 | 저수준 통계, 사물/장면 RDM 통제, 비정서 속성 상호 통제(S1′) |
| encoding 정확도 vs 설명적 적절성 | 판정은 서명 재현. R²는 보조 |
| decodability vs 표상 vs 인과 | 모델 내 조작은 R1, 뇌 대응은 R0. 뇌의 인과 주장 없음 |
| in-silico vs 실측 | 모델 예측 뇌와 실측 뇌를 같은 절차로 따로 계산해 비교 |
| shared vs dataset-specific | 두 코호트 재현, 코호트 안 분석 |
| exploratory vs confirmatory | 1주차 관문과 판정 규칙, 동등성 한계를 사전 등록 |
| HRF와 자기상관 | 블록 평균 클립 반응(Horikawa 제공본, MC는 원 논문 4 s shift). 시간 동역학 주장 없음 |
| stimulus/movie/subject leakage | MC 72 시험 클립 학습 제외, 2,108 고정. 같은 원본에서 잘린 클립 여부는 미확인이라 클립 분할 시 원본 ID가 확인되면 묶어서 나눈다 |
| 반복 자극 교란 | MC 시험 반복은 noise ceiling에만 사용 |
| 평정자 일치와 라벨 잡음 | 34범주 절대값 해석 안 함. 팔 간 비교만 |
| 시각-의미-정서 공선성 | 상호 통제와 논쟁 클립. 가를 수 없으면 그렇게 보고 |
| 시공간 해상도 | 블록 평균, 3T와 7T 혼재. 피질하 판정 제외 |
| ROI 선택과 순환 추론 | ROI와 위계 축은 해부 parcel과 휴지기 경사로 사전 정의(라벨과 독립) |
| 다중 비교 | Holm 보정, 사전 지정 묶음 |
| 자료, checkpoint 이용 조건 | EmoSet, torchvision, HCP-MMP, BLT, TDANN 미확인(1주차 목록) |
| 사전학습 오염 | EmoNet 미사용, 웹 규모 VLM 미사용, 지각 해시 중복 검사 |
| 데이터셋 간 라벨 비호환 | EmoSet 8범주는 학습에만, 판정은 C&K 34범주. 매핑하지 않음 |
