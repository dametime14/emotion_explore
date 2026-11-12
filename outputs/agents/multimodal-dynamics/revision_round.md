# 재탐색 라운드: multimodal-dynamics (D3 멀티모달)

* 작성: multimodal-dynamics (Axis D 시간 역학, Axis M 멀티모달 담당)
* 기준일: 2026-11-12
* 직접 읽은 것: `outputs/revision/plan.md` 전체, `outputs/stage1/dataset_Spacetop.md`, `dataset_EmoFilM.md`, `dataset_Horikawa.md`(라벨 절), `outputs/rq_landscape.md`의 K1과 RQ-05, `reference/existing_projects.md`, `outputs/STAGE_STATUS.md`의 보유 확인 항목.
* 표기: [본문] Discussion이나 Methods를 직접 읽음, [초록] 초록만 읽음, [서지] 식별자와 서지만 확인, [계산] 이번 라운드에서 공개 파일로 직접 계산, [추론] 근거가 간접적인 판단. 용어는 처음 나올 때 괄호로 쉬운 뜻을 단다.

---

## 0. 먼저 알릴 것

### 0.1 이번 라운드에서 새로 확인한 데이터 사실 (RQ-05에 결정적)

* **Spacetop narratives는 '양식'과 '이야기'와 '시간 순서'가 완전히 묶여 있다.** [계산]
  * 방법: OpenNeuro ds005256 v1.1.0의 GitHub 미러에서 participants.tsv 앞 40명의 ses-02 narratives events.tsv(run 4개)를 내려받아 셌다. 스크립트는 `/tmp/claude-0/-home-user-emotion-explore/4a0aeef6-c090-5f71-8a99-9b8e7c0f6d89/scratchpad/mdscripts/narr_tab.py`.
  * 결과: 자료가 있는 37명 중 34명은 이야기 1~4가 글(Text), 이야기 5~8이 소리(Audio)였다. 나머지 3명은 run 일부만 있어 부분 집합(7~8번 또는 5~6번만 소리)이었다. 이야기를 양식에 따라 바꿔 배정한 사람(counterbalancing)은 없었다.
  * run 순서도 34명이 같았다. run 1에 이야기 7, 8, run 2에 5, 6, run 3에 3, 4, run 4에 1, 2가 나온다. 그래서 **소리 이야기는 항상 앞 두 run, 글 이야기는 항상 뒤 두 run**이다.
  * 제시 시간: 소리 clip 중앙값 11.3 s(3.8~54.3 s), 글 clip 중앙값 19.1 s(5.3~38.5 s).
  * 함의: "같은 이야기를 글로 읽을 때와 들을 때"를 비교할 수 없다. 양식 효과는 이야기 내용과 run 순서(피로, 세션 안 시간)와 분리되지 않는다. 이전 RQ-05는 이 점을 몰랐다(1.0절).
* **라이선스 확인(저장소 LICENSE 파일 직접 확인, 가중치 조건은 아래 표기대로).** Whisper 코드 MIT, Demucs 코드 MIT, V-JEPA 2 저장소 "대부분 MIT, 일부 Apache 2.0", LAION-CLAP 저장소 CC0, ImageBind CC BY-NC-SA 4.0, MERT Apache 2.0, emotion2vec README 배지 MIT(LICENSE 파일은 찾지 못함), **MMAudio 코드 MIT, checkpoint CC BY-NC 4.0**(README 'License' 절). 마지막 항목은 RQ-60 카드 14절의 "MMAudio 미확인"을 갱신하는 사실이다(카드는 고치지 않았다. Coordinator 판단에 맡긴다).

### 0.2 D3 진단: 이전 K10이 왜 "멀티모달을 저렇게밖에" 못 썼나

* K10 질문들(RQ-60 등)은 **무음 Horikawa 자료 안에서** 멀티모달 모델을 feature 추출기로 썼다. 소리가 실제로 있는 데이터셋(Emo-FilM, Spacetop)을 주 무대로 쓰지 않았고, 데이터셋을 잇지도 않았다.
* AI의 역할이 "encoding 회귀자 하나 더"였다. 관찰로는 얻을 수 없는 비교나 변수를 만들지 못했다(plan.md 2절 기준 (a)(b)(c) 어디에도 강하게 해당하지 않음).
* 이번 라운드의 원칙은 세 가지다.
  1. **자연 자극 안에서 섞여 있는 감각 채널을 AI로 떼어 낸다.** 한 장면의 화면, 음악, 대사, 목소리 억양이 각각 실은 정서는 사람에게 다시 평정받지 않고는 잴 수 없다(기준 (b)).
  2. **공유 자극이 없는 데이터셋들을 AI 좌표로 잇는다.** 데이터셋끼리 같은 영상을 보여 준 적이 없어서, 뇌를 맞추려면 자극으로 계산 가능한 공통 좌표가 필요하다(기준 (b)).
  3. **AI가 만든 변수는 인간 라벨이나 관찰된 뇌 반응으로 검증하고, 결론은 관찰된 뇌 반응에서 낸다.** in-silico 예측은 결론의 근거로 쓰지 않는다.

---

## 1. 출발점 RQ-05 다시 쓰기

### 1.0 왜 약했는가 (plan.md 2절의 새 기준 두 개)

| 기준 | 이전 RQ-05 | 점수 추정 | 이유 |
|---|---|---|---|
| **AI-enabled Affective Neuroscience Contribution** | AI는 "저수준 feature 회귀"에만 쓰였다. 핵심 분석(양식 A에서 학습한 valence decoder를 양식 B에 적용, CCGP)은 AI 없이 하는 고전 교차 decoding이다 | 1~2 | 관찰만으로 같은 분석을 할 수 있다. 결과도 선행이 이미 보인 것의 반복이 되기 쉽다. 감각을 넘는 valence 코드는 맛과 시각(Chikazoe 2014, 10.1038/nn.3749), 얼굴과 상황(Skerry & Saxe 2014), 얼굴, 몸, 목소리(Peelen 2010), 무음 영상과 음악(Kim 2017, 10.1016/j.neuroimage.2017.01.002), 같은 영화의 감각 판본(Lettieri 2024)에서 보고되었다. 말뜻은 듣기와 읽기에서 거의 같은 지도로 표현된다(Deniz 2019, Regev 2013) |
| **1-month Feasibility** | 데이터는 있고 계산도 가볍다 | 3 | 실행은 4주 안에 된다. 그러나 0.1절의 교란 때문에 "양식이 같은가"라는 원래 질문에 깨끗한 답을 낼 수 없다. alignvideo에는 valence 문항이 없고(7개 문항에서 유도해야 함) 평정 약 51% 결측이다 |

* 요약: 이전 판은 **AI가 필요 없는 질문**이었고, **설계상 답할 수 없는 대조**(같은 이야기의 양식 비교)를 전제했다.
* 다시 쓰는 방향: 양식 비교를 버리지 않되, 질문을 "공통 신호가 **무엇에서** 오는가"로 바꾼다. 소리로 들은 이야기에는 **말뜻**과 **목소리 억양(prosody)**이라는 두 정서 경로가 섞여 있다. AI만이 같은 문장에서 이 둘을 따로 잴 수 있다. 그리고 **글로만 학습한 뇌 축**은 억양을 한 번도 본 적이 없으므로, 억양이 그 축에 들어오는지를 보는 깨끗한 탐침이 된다.

### [MD-RV-1] 읽고, 듣고, 볼 때 공통으로 생기는 뇌의 '좋고 나쁨' 신호는 이야기의 뜻에서 올까, 목소리의 느낌에서 올까?

* **자세한 질문**
  1. 같은 사람이 **글로 읽은** 이야기 조각에서 학습한 뇌의 좋고-나쁨 축(본인 평정으로 학습)에, **소리로 들은** 이야기 조각을 투영한 점수는 말뜻의 valence(대본 기준)만 따르는가, 아니면 말뜻을 통제한 뒤에도 목소리 억양의 valence를 따르는가?
  2. 그 억양 효과는 참가자 본인의 느낌 보고를 거쳐서만 나타나는가(보고를 통제하면 사라지는가)?
  3. (확장) 같은 축은 소리 있는 영상(alignvideo)에도 통하는가, 통한다면 영상의 화면, 배경 소리, 대사 중 어느 채널의 정서를 따르는가?
* **AI가 있어야만 가능한 이유**
  * 자연스럽게 낭독된 이야기에서 **말뜻의 정서와 억양의 정서를 따로 잰 인간 평정은 없다.** 새로 받으려면 내용을 지운 음성(저역 통과 필터)과 대본을 따로 평정하게 하는 새 수집이 필요하다.
  * AI는 이것을 계산 가능한 변수로 만든다(기준 (b)). (i) 음성 인식으로 대본을 얻고(Whisper), (ii) 언어 모델로 대본의 valence를 매기고, (iii) 음성 정서 모델(emotion2vec)과 음향 지표(F0, 강도, 속도)로 억양의 valence를 매긴다. 억양 쪽은 원 음성 값에서 대본 valence를 회귀로 뺀 잔차와, 내용을 지운 음성에서 잰 값 두 가지를 쓴다.
  * 뇌 분석 자체(교차 decoding)는 AI가 아니다. AI의 몫은 **공통 신호의 출처를 가르는 두 변수**를 만드는 것이다. 이 점을 과장하지 않는다.
* **정서와 뇌에 대해 새로 알게 되는 것**
  * 감각을 넘는 valence 코드(vmPFC, OFC, pSTS)가 **개념적 의미에서 계산된 값**인지, **감각 정서 신호(억양)도 같은 좌표에 쓰이는지**를 가른다.
  * 정서를 의미 평가와 개념화의 산물로 보는 입장(appraisal, 구성주의 계열)은 억양 효과가 말뜻과 보고를 거쳐서만 들어온다고 예측한다. 감각 정서 신호가 개념과 독립적으로 정동(core affect)에 들어간다고 보는 입장은 말뜻을 통제한 뒤에도 억양 효과가 남는다고 예측한다. 다만 **억양 효과가 보고를 거쳐 들어오는 결과는 두 입장 모두 허용**할 수 있어 가르지 못한다. 가를 수 있는 것은 "말뜻과 보고를 모두 통제한 뒤에도 남는 억양 효과"의 유무다.
  * 통제된 문장 연구는 억양과 어휘 정서가 충돌하면 전두 통제망이 동원된다고 보였다(Mitchell 2013, 10.1016/j.cortex.2012.07.010). 자연 이야기에서, 그리고 감각 공통 축 위에서 두 경로가 어떻게 합쳐지는지는 보고되지 않았다(5절 검색 기록).
* **데이터** (Stage 1 보고서, plan.md 4절, 0.1절 기준)
  * Spacetop narratives: 이야기 8편 x 9 clip = 72 clip. 글 36개(이야기 1~4), 소리 36개(이야기 5~8). clip마다 참가자 본인의 느낌(Good~Bad 2차원 척도의 좌표)과 기대 평정, 응답률 0.98. 자료가 있는 참가자 106명, 전 run 보유 105명[Stage 1]. 원문 txt 36개, mp3 36개 공개. 소리 clip의 대본 파일이 따로 있는지는 미확인(없으면 Whisper로 만든다). narratives에는 생리 기록이 없다(코드 기준 추정)[Stage 1].
  * Spacetop alignvideo: 영상 49편(소리 있음), 모든 참가자 같은 순서, 영상 후 본인 평정 7개(personal relevance, happy, sad, afraid, disgusted, warm and tender, engaged), **valence 문항 없음**, 약 51% 결측[Stage 1]. 같은 참가자를 functional alignment(사람 사이 뇌 반응 맞추기)하는 공유 자극으로 쓴다.
  * 형식: fMRIPrep 25.1.4 파생본(MNI volume, fsLR 91k CIFTI) 공개[Stage 1]. 사용자 보유본은 공개판과 같을 것으로 추정(STAGE_STATUS 25(d)). 파생본까지 보유했는지는 미확인.
  * 라벨 출처: 느낌 평정은 **fMRI 참가자 본인의 clip 후 사후 보고**. 말뜻 valence와 억양 valence는 **AI 추정(R1)**.
  * 교란(0.1절): 양식 = 이야기 묶음 = run 순서.
* **모델과 checkpoint**
  * Whisper(arXiv:2212.04356): 공개, 코드 MIT 확인. GPU 1장, 36 clip이라 수 분.
  * emotion2vec(arXiv:2312.15185): 공개, README 배지 MIT(가중치 조건 미확인). 범주 확률을 valence로 바꾸는 사상은 사전 등록. GPU 1장 수 분.
  * 대본 valence: 공개 instruction LLM 1개(7B급, 라이선스 미확인)와 문장 embedding의 valence 투영을 함께 써서 서로 검증. GPU 1장.
  * 음향 지표(F0, 강도, 말 속도): 결정적 계산이라 모델 의존이 없다.
  * (확장) alignvideo 채널 분리: Demucs(arXiv:2211.08553, 코드 MIT)로 대사와 배경 소리를 나누고, 화면 정서는 [MD-RV-2]의 Cowen & Keltner 무음 평정 head를 쓴다.
* **핵심 분석, 예측, 반증 조건**
  1. **0단계 관문(결과를 보기 전에 판정):** (a) 소리 clip 36개의 억양 valence가 대본 valence와 얼마나 겹치는가. 상관이 0.9를 넘으면 두 경로를 가를 수 없으므로 중단한다. (b) 억양 valence의 clip 간 분산이 음향 잡음 수준보다 큰가(낭독이 평탄하면 중단). (c) 대본 valence가 **글 clip**의 집단 평균 느낌을 예측하는가(언어 모델 valence의 타당화. 글 clip에는 억양이 없어 깨끗하다).
  2. **행동 분석(fMRI 없이 먼저):** 소리 clip의 본인 느낌 ~ 대본 valence + 억양 valence + clip 길이 + (참가자, clip 무작위 효과). 억양이 경험한 느낌을 바꾸는지 먼저 본다.
  3. **뇌의 글 학습 축:** 참가자별 clip 단위 반응(LSS 단일 시행 추정, 평정 구간은 별도 회귀자)을 사전 등록 ROI(vmPFC 묶음, 오른쪽 pSTS 묶음, Glasser 아틀라스)에서 뽑는다. alignvideo로 학습한 functional alignment로 사람들을 맞춘 뒤, 글 clip 36개 x 참가자에서 느낌 평정을 예측하는 ridge 축을 학습한다.
  4. **주 검정(사전 등록):** 소리 clip 반응을 이 축에 투영한 점수 s ~ 대본 valence + 억양 valence + clip 길이 + run 위치 + (참가자, clip 무작위 효과). 주 통계량은 **억양 valence 계수**다. 판정은 clip 36개 단위 bootstrap 95% 구간, 두 ROI에 Holm 보정.
  5. **매개 검정:** 4번 모형에 본인 느낌을 넣고 억양 계수가 남는지 본다.
  6. **양식 벌점(기술 통계):** 글 → 소리 전이 정확도와, 같은 양식 안에서 다른 이야기로의 전이(글 이야기 1, 2 → 3, 4, 소리 5, 6 → 7, 8)를 비교한다. 이야기가 바뀌는 효과를 같은 크기로 맞춘 비교다. run 순서 교란은 이것으로도 남는다.
  * **예측:** 의미 중심 입장이면 억양 계수 ≈ 0, 대본 계수 > 0. 감각 수렴 입장이면 억양 계수 > 0(대본 계수와 같은 부호)이고 5번에서도 남는다. pSTS는 목소리 정서에 민감하다는 선행(Grandjean 2005, 10.1038/nn1392)대로 억양 계수가 vmPFC보다 클 것으로 예상한다.
  * **반증 조건:** 억양 계수의 95% 구간이 0을 포함하면 "억양 정서가 감각 공통 축에 들어간다"는 가설은 그 ROI에서 지지되지 않는다. 이 판정은 대본 계수가 0보다 클 때만 유효하다. 대본 계수도 0이면 "글 축이 소리로 전이되지 않음(판정 불가)"으로 보고한다. 0단계 (a), (b) 관문에서 멈추면 이 질문은 이 데이터로 답할 수 없다고 보고한다.
* **4주 계획**
  * 1주: narratives와 alignvideo 파생본 확보, events 정리, 느낌 척도 좌표를 valence와 강도로 변환(척도 중심 좌표 확인), Whisper 대본, 대본 valence, 억양 valence, 음향 지표. 0단계 관문 판정.
  * 2주: 행동 분석(분석 2). clip 단위 LSS 반응 추정(CPU), alignvideo 기반 functional alignment.
  * 3주: 글 학습 축, 주 검정, 매개 검정, 양식 벌점. 참가자별 결과와 prevalence(모집단에서 효과를 가진 사람 비율 추정).
  * 4주: (확장) alignvideo 49편에 같은 축 적용, 채널별 정서와 대조. 민감도 분석(억양 추정 두 방식, LLM 교체). 정리.
  * 판정: **한 달 안 가능.** 새 수집과 모델 학습이 없다. 가장 무거운 일은 약 105명 x 4 run의 단일 시행 GLM과 alignvideo 정렬이며 CPU로 1주 안팎(추정, 미검증).
* **가장 가까운 선행과 차이** (5절 질의 1~4, 2026-11-12)
  * Deniz et al. 2019 (10.1523/JNEUROSCI.0675-19.2019) [초록]: 같은 이야기를 듣기와 읽기로 제시했을 때 의미 조율이 거의 같다. 정서와 억양은 다루지 않았다.
  * Regev et al. 2013 (10.1523/JNEUROSCI.1580-13.2013) [초록]: 같은 이야기의 말과 글에서 STG, IFG 반응 시간 경과가 비슷하다. 정서 없음.
  * Peelen et al. 2010, Skerry & Saxe 2014, Chikazoe 2014, Kim et al. 2017 [초록]: 감각과 단서를 넘는 정서 또는 valence 코드(MPFC, OFC, STS). 통제된 짧은 자극이고, 공통 코드가 무엇에서 오는지(의미 대 감각 신호)는 가르지 않았다.
  * Mitchell 2013 (10.1016/j.cortex.2012.07.010) [초록]: 억양과 어휘 정서가 충돌하는 통제 문장. 자연 이야기와 감각 공통 축은 아님.
  * Miao et al. 2026 (10.1038/s41467-026-71151-2) [Stage 1, 이번 라운드 미재확인]: 같은 Spacetop narratives로 사회적 상호작용과 ToM을 분석했다. 정서 아님.
  * 차이: 자연 낭독 이야기에서 AI로 말뜻과 억양의 정서를 따로 재고, **억양을 본 적 없는 글 학습 축**으로 억양이 감각 공통 코드에 들어가는지 검정하는 연구는 찾지 못했다.
* **주요 위험**
  * 소리 clip이 36개뿐이라 억양 효과는 사실상 36개 항목 수준에서 추정된다. 항목 수준 상관 약 0.33 이상만 검출 가능하다(추정). 105명은 이 한계를 풀어 주지 못한다.
  * 낭독이 평탄하면 억양 분산이 작다(0단계 (b)).
  * 억양 추정은 AI다. emotion2vec는 연기된 정서 음성 위주로 학습되었고 저역 통과 음성에서는 분포 밖이다. 음향 지표로 교차 확인한다.
  * 양식 = 이야기 = run 순서 교란(0.1절). 결론은 "이 이야기 묶음에서"로 한정된다.
  * 느낌 평정은 clip 직후 사후 보고이며 평정 구간의 운동, 결정 활동이 clip 끝 반응과 겹친다.

---

## 2. [MD-RV-2] 영화에서 화면과 음악이 서로 다른 감정을 말할 때, 뇌와 사람은 어느 쪽을 따라갈까?

* **자세한 질문**
  1. 소리 있는 단편영화를 볼 때 매 순간의 정서를 **화면만의 정서, 배경 소리(음악, 효과음)만의 정서, 대사만의 정서**로 나누면, 별도 평정자의 연속 정서 평정(consensus)과 뇌 반응은 각 채널을 얼마나 따르는가?
  2. 세 채널이 **같은 정서를 말하는 공통 성분**과 **채널 고유 성분**은 뇌의 어디에 표현되는가? (감각 공통 영역 대 감각 피질)
  3. 화면과 배경 소리가 **반대 정서**를 말하는 순간에, 정서 관련 영역의 반응은 어느 채널을 따르는가? 그 선택은 각 채널의 신뢰도(음악의 두드러짐, 화면의 정보량)에 따라 달라지는가(신뢰도 가중 통합)? 평정자의 선택과 같은가?
* **AI가 있어야만 가능한 이유**
  * 자연 영화에서 화면, 음악, 대사는 동시에 들어온다. **채널을 떼어 낸 인간 평정은 없다.** 새로 받으려면 무음판, 음악만, 대사만 판본을 만들어 평정을 새로 수집해야 한다(Lettieri 2024는 이런 판본 fMRI를 따로 찍었다).
  * AI는 이 분해를 계산으로 해 준다(기준 (b)). 음원 분리로 대사와 배경 소리를 나누고(Demucs), 영상만 보는 모델로 화면 정서를, 오디오 모델로 배경 소리 정서를, 음성 인식과 언어 모델로 대사 정서를 매긴다.
  * 화면 정서는 **사람이 소리 없이 보고 매긴 평정으로 학습한다.** Cowen & Keltner 클립의 규범 평정(valence, arousal 포함 14 차원)은 평정자가 무음으로 보고 매긴 것이다[Stage 1, horikawa_factcheck_stage4]. 이 평정으로 학습한 영상 모델 head는 "소리 없이 화면만 본 사람이 매길 정서"의 추정기이고, Horikawa 데이터셋의 라벨을 Emo-FilM으로 옮기는 다리가 된다(데이터셋 간 연결).
  * AI는 또 **채널이 충돌하는 순간**을 찾아 준다(기준 (c), 검증 가능한 가설의 대상 생성). 통제 실험에서는 연구자가 충돌을 만들지만(Bravo 2024), 자연 영화에서는 AI 없이 이런 순간을 체계적으로 찾을 수 없다.
* **정서와 뇌에 대해 새로 알게 되는 것**
  * 감각 공통 정서 코드(pSTS, vmPFC, amygdala, Gao 2019 메타분석)와 감각 특이 코드(초기 감각 피질, Lettieri 2024)의 구분을, 판본을 따로 찍지 않은 자연 시청에서 시험한다.
  * 시청각 정서 통합의 규칙을 가른다. Gao et al. 2026 (10.1093/scan/nsag090) 리뷰는 "신뢰도에 따른 통합(감각-pSTC 상호작용)"과 "가치에 따른 통합(amygdala와 전전두 추가 동원)"이라는 이중 경로 가설을 내고 직접 검증이 필요하다고 했다[초록]. 충돌 순간에 뇌가 따르는 채널이 신뢰도에 따라 바뀌면 전자, 정서 강도나 부정성에 따라 바뀌면 후자를 지지한다.
  * 신경미학(영화 음악) 쪽에서는 "음악이 장면의 정서를 다시 쓴다"는 주장(Bravo 2024의 불협화음 조작)이 자연 영화의 여러 장면에서도 성립하는지, 그리고 뇌와 평정자가 같은 규칙을 쓰는지를 본다.
* **데이터** (Stage 1 보고서, plan.md 4절 기준)
  * Emo-FilM fMRI(ds004892): 30명, 단편영화 14편(오디오 포함, 각 1회), TR 1.3 s, 제공 전처리본 MNI(6 mm smoothing, WM, CSF, motion 회귀), 생리(PPG, 호흡, EDA 1000 Hz) 공개[Stage 1]. S07 영화 3편 전처리본은 v1.0.2에서 추가되어 30명 전원 사용 가능성 있음(본체 미검증).
  * 주 라벨: **별도 평정자 44명 중 항목 x 영화당 3~4명의 1 Hz consensus**, 50항목, 평정자 쌍 평균 r 0.38~0.39[Stage 1]. **valence, arousal 문항은 없다.** Good, Bad를 valence 대리로 쓴다(Ma & Kragel 2026 방식). Calm, AtEase는 반대 극이 Restless, Nervous라 각성과 부정 긴장이 섞인다(card_review_B 2.2절)는 점을 표시한다.
  * fMRI 참가자 본인 자료: 사후 클립 평정(영화당 5항목, 전체의 약 20%), 영화별 몰입, 즐거움, 흥미[Stage 1]. 보조 검증에만 쓴다.
  * 원본 영화: 사용자 보유. 연구에 쓴 크레딧 절단판과 같은지는 미확인(STAGE_STATUS 21).
  * Cowen & Keltner 클립 2,185개(무음, 보유)와 규범 평정(34 범주, 14 차원): 화면 정서 head의 학습 자료. **EmoNet은 쓰지 않는다**(plan.md 4절, Cowen & Keltner 프레임으로 학습되어 누수 위험).
  * 라벨 출처 표기: consensus = 별도 평정자의 경험 보고(1인칭 문항), 화면 정서 head = 별도 평정자의 무음 시청 규범 평정으로 학습한 AI 추정, 배경 소리와 대사 정서 = AI 추정(R1).
* **모델과 checkpoint**
  * V-JEPA 2(arXiv:2506.09985): 저장소 대부분 MIT(직접 확인), 가중치 조건은 저장소 기준 미세 확인 필요. 영상만 입력. GPU 1장, 약 9,600 s 영화를 1~2 fps로 수 시간(추정).
  * Demucs(HT Demucs, arXiv:2211.08553): 코드 MIT. 대사(vocals)와 나머지(음악, 효과음) 분리. CPU 또는 GPU로 수 시간.
  * 배경 소리 표현: LAION-CLAP(저장소 CC0)과 MERT(Apache 2.0). 정서 추정은 (i) CLAP 정서 텍스트 프롬프트 유사도(AI 추정, 인간 검증 없음), (ii) 영화 하나씩 빼는 교차검증으로 consensus를 배경 소리 feature만으로 예측한 값, 두 가지를 함께 쓴다.
  * 대사: Whisper(MIT) + 공개 LLM(라이선스 미확인)으로 발화 단위 valence.
  * 사전학습 오염: Emo-FilM 영화는 CC 공개 영화(Sintel, Big Buck Bunny 등 포함)라 모델 학습 자료에 들어 있을 수 있다. 정서 라벨이 아니라 feature 추출에만 쓰므로 영향은 추정 품질 쪽으로 한정된다.
* **핵심 분석, 예측, 반증 조건**
  1. **0단계(결과 보기 전 판정):** (a) 화면 정서 head를 Cowen & Keltner 안에서 교차검증(valence, arousal 예측력). (b) Emo-FilM에서 세 채널 정서 시계열을 만들고, 화면과 배경 소리의 valence가 반대 부호이면서 둘 다 |z| > 1인 구간이 4 s 이상 이어지는 **충돌 구간**의 수를 센다. 영화 14편 합쳐 20개 미만이면 충돌 분석(4번)은 연속 모형(전 시간에서 채널 x 신뢰도 상호작용)으로 바꾼다.
  2. **평정 수준 분해(뇌 없이):** consensus Good, Bad를 세 채널 정서 + 내용 feature로 설명하고(영화 단위 교차검증) 채널별 고유 설명량을 구한다. 충돌 구간에서 consensus가 어느 채널을 따르는지 **소리 추종 지수**(배경 소리 계수 / (|배경 소리 계수| + |화면 계수|))를 계산한다.
  3. **뇌 수준 분해:** parcel마다 banded ridge encoding(feature 묶음마다 다른 정규화). 묶음은 내용(영상, 소리, 언어 feature의 주성분), 공통 정서 성분(세 채널 정서 추정의 첫 주성분), 채널 고유 성분(각 채널에서 공통 성분을 뺀 나머지), consensus에서 세 채널로 설명되지 않는 나머지(서사 맥락 등 통합 성분 후보). 고유 설명량을 영화 단위 교차검증으로 구한다.
  4. **충돌 추종(사전 등록 주 검정):** consensus로 학습한 뇌 decoder(영화 단위 교차검증)의 출력이 충돌 구간에서 어느 채널을 따르는지 사전 등록 ROI 묶음(vmPFC, pSTS, amygdala)에서 소리 추종 지수를 구한다. 주 통계량은 **소리 추종 지수와 상대 신뢰도(배경 소리 에너지의 두드러짐 - 화면 정서 head의 확신도)의 기울기**다.
  * **예측:**
    * 감각 공통 코드 가설: 공통 정서 성분의 고유 설명량이 pSTS, vmPFC에서 크고, 채널 고유 성분은 각 감각 피질에서 크다.
    * 신뢰도 가중 통합: 충돌 구간의 소리 추종 지수가 상대 신뢰도와 양의 기울기를 갖는다. 평정자의 지수와 뇌의 지수가 같은 방향이다.
    * 가치 우선 통합: 소리 추종 지수가 신뢰도가 아니라 어느 채널이 더 부정적인가에 따라 바뀐다(부정 채널 우세).
  * **반증 조건:** (i) 기울기의 영화 단위 bootstrap 95% 구간이 0을 포함하면 신뢰도 가중 통합은 이 데이터에서 지지되지 않는다. (ii) 공통 정서 성분의 고유 설명량이 pSTS와 vmPFC에서 내용 묶음 위로 0과 구분되지 않으면, 감각 공통 정서 코드를 내용과 분리해 보였다고 주장하지 않는다. (iii) 0단계 (a)에서 화면 정서 head의 교차검증 예측력이 낮으면(valence r < 0.3) 채널 분해 전체를 "AI 추정 신뢰 불가"로 보고 멈춘다.
* **4주 계획**
  * 1주: 영화 판본 확인, Demucs, Whisper, V-JEPA 2(영화와 Cowen & Keltner 클립), CLAP, MERT feature 추출. 화면 정서 head 학습과 0단계 (a).
  * 2주: 세 채널 정서 시계열, 충돌 구간 계수(0단계 (b)), 평정 수준 분해(분석 2).
  * 3주: 30명 parcel 시계열(Schaefer 400 + 피질하), banded ridge encoding과 분해(분석 3).
  * 4주: consensus decoder와 충돌 추종 검정(분석 4), 민감도(배경 소리 정서 추정 두 방식, 충돌 기준), 정리.
  * 판정: **한 달 안 가능.** 새 수집, 모델 학습 없음(head는 ridge). GPU 1~2장. 가장 큰 불확실성은 계산이 아니라 배경 소리 정서 추정의 타당성이다.
* **가장 가까운 선행과 차이** (5절 질의 5~8, 2026-11-12)
  * Bravo et al. 2024, PNAS (10.1073/pnas.2320378121) [초록]: 같은 단편영화에 협화, 불협화 음악을 바꿔 붙인 통제 조작. 불협화가 정서 추론을 부정 쪽으로 옮기고 V1을 움직였다. 한 영화, 연구자 조작.
  * Lettieri et al. 2024 (10.1126/sciadv.adk6840) [본문]: 같은 영화를 시청각, 시각, 청각 판본으로 따로 찍었다. 판본 촬영이 필요했다.
  * Marras et al. 2025, NeuroImage (10.1016/j.neuroimage.2025.121439) [초록]: 같은 영화의 세 판본에서 행위 feature(정서 영역 포함)의 encoding과 분산 분할. 정서 채널 분해와 충돌은 아님.
  * Pehrs 2014, Bezdek 2017, Eldar 2007 [초록]: 영화 음악과 장면 정서의 통제 설계.
  * Ma & Kragel 2026 (10.1038/s41467-025-68240-z) [본문]: Emo-FilM으로 정서 지도. 감각 채널 분해 없음.
  * Pan et al. 2025 (arXiv:2509.21381) [본문]: EEG에서 목소리와 사운드트랙의 정서 encoding 차이. fMRI, 화면 채널, 충돌은 다루지 않음.
  * 차이: 자연 영화에서 AI로 화면, 배경 소리, 대사의 정서를 분리하고, **사람이 무음으로 매긴 평정으로 화면 채널을 고정**한 뒤, 자연 충돌 순간에서 뇌와 평정자의 통합 규칙을 비교하는 연구는 찾지 못했다.
* **주요 위험**
  * 배경 소리 정서는 인간 평정으로 검증되지 않은 AI 추정이다. 영화 단위 교차검증으로 consensus를 예측한 판본은 화면과 함께 나온 소리의 정서를 학습해 채널이 섞일 수 있다. 두 방식이 다른 답을 주면 결론을 내리지 않는다.
  * 화면 정서 head는 짧은 무음 클립(Cowen & Keltner)에서 학습해 애니메이션이 많은 Emo-FilM 영화로 옮긴다(영역 이동).
  * consensus는 3~4명 평균이라 잡음이 크다. 평정자별 원자료로 천장을 계산해 함께 보고한다.
  * 영화 14편이라 영화 수준 교란(장르, 애니메이션 여부)이 크다.
  * 공통 성분과 내용 feature가 공선적이다. 내용 묶음을 넣으면 정서 고유 설명량이 작게 나올 수 있다.
  * overlap: **Emo-FilM 연구**(같은 데이터에서 사전학습 멀티모달 encoding으로 정서 맥락을 분석하는 계획과 데이터, 방법이 겹친다. 차이는 채널 분해와 충돌 순간의 통합 규칙 검정). **EmoBrain**: V-JEPA 2를 Cowen & Keltner 자료에 쓰는 도구만 겹친다.

---

## 3. [MD-RV-3] 다른 영화를 다른 사람이 보고 다른 방식으로 보고한 정서도, 뇌 속에서는 같은 축 위에 있을까?

* **자세한 질문**
  1. 공유 자극이 전혀 없는 두 데이터셋(Emo-FilM과 Spacetop alignvideo)의 뇌를 AI 공통 좌표로 맞추면, 한 데이터셋에서 학습한 정서 decoder가 다른 데이터셋의 정서를 읽어 내는가?
  2. 이전 연구에서 각성은 데이터셋을 넘어 일반화되었지만 valence는 실패했다(Ke 2025). 그 실패는 (i) 사람과 데이터셋마다 뇌 지도가 달라서인가(정렬 문제), (ii) valence 코드가 상황(내용)마다 달라서인가(맥락 의존), (iii) 라벨을 매긴 주체가 달라서인가(라벨 출처)?
  3. (확장) 무음 영상 데이터셋(Mind captioning, Horikawa 2020)까지 같은 좌표에 넣으면, 소리 있는 영화에서 학습한 정서 축이 무음 시청 뇌에서도 통하는가?
* **AI가 있어야만 가능한 이유**
  * 데이터셋끼리 같은 영상을 보여 준 적이 없다. 고전 hyperalignment(Haxby 2011, 10.1016/j.neuron.2011.08.026)는 같은 자극에 대한 반응이 필요하다. AI 없이는 해부 좌표(MNI)로만 비교할 수 있고, Ke 2025가 valence에서 실패한 것이 바로 그 방식이다.
  * 영상과 소리를 함께 읽는 사전학습 모델은 모든 자극을 한 좌표에 놓는다. 피험자마다 encoding 모델(자극 feature에서 뇌 반응을 예측)을 학습하면, **같은 탐침 자극 묶음에 대한 예측 반응**을 모든 피험자에게서 얻을 수 있다. 이것으로 공유 자극 없이 뇌를 맞춘다(기준 (b)). 이 정렬 방식 자체는 Wang et al. 2024(arXiv:2403.11517)가 시각 재구성용으로 보였다. 그 논문 Discussion은 이 방식을 시각 feature 밖의 인지 상태로 넓히는 것을 향후 과제로 들었다[본문].
  * 정렬은 AI 예측으로 하지만 **decoder 학습과 평가는 관찰된 뇌 반응**으로 한다. in-silico 예측은 정렬 변환을 만드는 데에만 쓴다.
* **정서와 뇌에 대해 새로 알게 되는 것**
  * "모든 사람에게 공통인 valence 코드가 있는가"는 core affect 계열(보편적 쾌-불쾌 축, Chikazoe 2014의 사람 간 OFC 코드)과 구성주의 계열(정서 표상은 상황과 개념에 따라 달라짐)이 다르게 답하는 질문이다. Ke 2025의 valence 실패는 맥락 의존 쪽 증거처럼 읽히지만, 저자들도 원인(개인 특이성, 연결 기반 방법의 한계, 맥락 특이성)을 가르지 못했다[본문 Discussion].
  * 이 연구는 그 셋을 분리한다. 정렬 후 전이가 살아나면 "공통 코드는 있고 사람마다 지도가 다를 뿐"이다. 정렬 후에도 실패하는데 같은 데이터셋 안에서는 사람 사이 전이가 되면 "상황이나 라벨 출처에 묶인 코드"다. 이어서 AI로 내용을 맞춘 부분집합(예: 사람 사이 상호작용 장면끼리)에서 전이가 살아나는지 보면 맥락 의존을 직접 시험한다.
  * 이름이 같은 정서 항목(행복, 슬픔, 공포, 혐오, 따뜻함)이 별도 평정자 consensus(Emo-FilM)와 본인 사후 보고(Spacetop)에서 같은 뇌 축으로 이어지는지도 함께 본다. 라벨 출처가 다른데 같은 축이면, 그 축은 평정 방식이 아니라 공유된 정서 상태를 반영할 가능성이 커진다(그래도 '경험의 직접 판독'으로 해석하지 않는다).
* **데이터** (Stage 1 보고서, plan.md 4절 기준)
  * Emo-FilM: 30명, 14편, TR 1.3 s, MNI 제공 전처리본(6 mm). 라벨: 별도 평정자 consensus 1 Hz. 이름이 대응하는 항목 Happiness, Sad, Fear, Disgust, WarmHeartedness와 valence 대리 Good, Bad.
  * Spacetop alignvideo: 영상 49편, 모든 참가자 같은 순서, TR 0.46 s, fMRIPrep MNI와 CIFTI. 라벨: **본인 사후 평정** happy, sad, afraid, disgusted, warm and tender(이름 대응 5개), 영상당 1회, 약 51% 결측, 결측이 사람과 세션 단위로 몰림[Stage 1]. valence는 유도 지표(happy + warm - sad - afraid - disgusted)로만 만든다.
  * (확장) Mind captioning: 학습 2,108개 클립으로 고정(시험 72개 제외, plan.md 4절), 무음, 규범 평정(valence, arousal 포함 14 차원). 보유본 전처리 형식 미확인(원 논문은 4 s shift 후 블록 평균). Horikawa 2020: 5명, 무음.
  * 라벨 출처 표기: Emo-FilM = 별도 평정자 consensus(경험 문항), Spacetop = fMRI 참가자 본인 보고, Cowen & Keltner = 별도 평정자 규범(무음 시청).
* **모델과 checkpoint**
  * 공통 좌표: V-JEPA 2 영상 feature(저장소 MIT 확인) + CLAP 오디오 feature(저장소 CC0). 무음 확장 판본은 영상 feature만 쓴다. 대안으로 ImageBind(영상, 소리를 한 공간에 둠)는 CC BY-NC-SA 4.0이라 비상업 연구에만 쓸 수 있다.
  * 정렬: 피험자별 ridge encoding → 탐침 자극 묶음(두 데이터셋 자극 구간의 합집합, 수천 구간)의 예측 반응 → 템플릿으로 Procrustes(회전) 정렬. 학습은 선형이라 GPU가 거의 필요 없다. feature 추출에 GPU 1장.
* **핵심 분석, 예측, 반증 조건**
  1. **기준선 세 개:** (a) 해부 좌표(parcel)에서 데이터셋 간 전이(Ke 2025식, 실패 예상), (b) 같은 데이터셋 안에서 사람 간 전이(상한), (c) 자극만으로 전이(뇌 없이 모델 feature에서 정서를 예측하는 head를 다른 데이터셋에 적용. 내용만으로 얼마나 되는지).
  2. **주 검정(사전 등록):** AI 정렬 공간에서 Emo-FilM으로 학습한 decoder(이름 대응 5개 항목, valence 대리)를 Spacetop 영상에 적용한다. 영상 평균 출력과 본인 평정의 상관을 참가자별로 구하고 prevalence로 요약한다. 반대 방향(Spacetop → Emo-FilM 시계열)도 한다. 주 통계량은 **정렬 공간 전이 - 해부 좌표 전이**(valence 대리 기준).
  3. **내용 넘어서기:** 관찰 반응에서 encoding 예측분(내용으로 설명되는 부분)을 뺀 잔차로 같은 전이를 한다. 정렬 변환이 내용에서 배운 것이므로, 잔차 전이가 되면 내용 밖의 공유 정서 성분이 있다는 뜻이다.
  4. **원인 분해:** 정렬 후에도 valence가 실패하면, AI 캡션으로 내용 범주(사람 사이 상호작용, 자연 풍경, 위험 상황 등)를 맞춘 부분집합 안에서만 전이를 다시 본다. 각성 대리와 내용 변수(얼굴 있음, 말소리 있음)를 양성 대조로 둔다.
  * **예측:** 정렬 문제 가설이면 정렬 공간 전이가 해부 좌표 전이보다 크고 잔차에서도 남는다. 맥락 의존 가설이면 정렬 후에도 전체 전이는 낮고 내용 맞춘 부분집합에서만 오른다. 라벨 출처 가설이면 같은 데이터셋 안에서도 라벨 종류를 바꾸면(Emo-FilM consensus 대 참가자 사후 클립 평정, Spacetop 본인 대 다른 참가자 평균) 전이가 떨어진다.
  * **반증 조건:** 정렬 공간 전이와 해부 좌표 전이의 차이가 참가자 bootstrap 95% 구간에서 0을 포함하고, 양성 대조(얼굴, 말소리)의 전이는 정렬로 개선되면, "valence 실패는 정렬 문제"라는 가설은 기각된다. 양성 대조도 개선되지 않으면 정렬 자체가 실패한 것이라 판정 불가로 보고한다.
* **4주 계획 (축소판)**
  * 1주: 두 데이터셋을 같은 parcel(Schaefer 400 + 피질하)로, 공간 smoothing 맞추기(Spacetop을 6 mm로), 같은 시간 단위(2 s 구간)로. feature 추출. 라벨 정리(Spacetop 결측 구조, Emo-FilM 항목).
  * 2주: 피험자별 encoding, 탐침 자극 예측, Procrustes 정렬. 양성 대조로 정렬 품질 확인.
  * 3주: 기준선 세 개와 주 검정, 잔차 전이.
  * 4주: 원인 분해(내용 맞춘 부분집합, 라벨 출처 교체), 정리.
  * 판정: **전체판(세 데이터셋 이상, voxel 수준, 비선형 정렬)은 한 달 안 불가.** 형식이 다른 네 데이터셋의 전처리를 맞추는 데만 2주 이상 걸릴 것으로 추정한다. **축소판(Emo-FilM과 Spacetop alignvideo 둘, parcel 수준, 선형 정렬)은 가능.** 무음 확장은 축소판 결과를 본 뒤 다음 단계로 둔다.
* **가장 가까운 선행과 차이** (5절 질의 9~12, 2026-11-12)
  * Ke et al. 2025, PLOS Comput Biol (10.1371/journal.pcbi.1012994) [본문]: 동적 연결로 각성은 데이터셋을 넘어 일반화, valence는 실패. 원인 미결.
  * Chan et al. 2020, NeuroImage (10.1016/j.neuroimage.2020.116618) [초록]: 같은 참가자들이 본 영화 예고편으로 hyperalignment한 뒤 사람 간 valence, arousal decoding. 공유 자극이 있는 한 데이터셋 안의 정렬이다.
  * Wang et al. 2024 (arXiv:2403.11517) [본문 Discussion]: 공유 자극 없이 DNN feature(content loss)로 사람과 사이트를 넘는 뇌 변환. 시각 재구성이 목적이고 정서는 다루지 않았다. 저자들은 content 기반 정렬이 사람마다 다른 자극 반응(idiosyncratic) 성분을 덜 담는다고 썼다. 이것은 정서 코드가 정렬 뒤 사라질 수 있다는 이 질문의 위험이기도 하다.
  * Tang et al. 2023, NeurIPS (arXiv:2305.12248) [본문 Discussion]: 멀티모달 transformer feature로 이야기와 영화 사이 encoding 전이. 정서 아님.
  * Kragel & LaBar 2015 (10.1093/scan/nsv032) [초록]: 음악과 영화로 유도한 정서 범주의 다변량 표지. 한 데이터셋 안.
  * 차이: 공유 자극 없는 두 정서 데이터셋을 AI 좌표로 맞추고, Ke 2025가 남긴 valence 일반화 실패의 원인(정렬, 맥락, 라벨 출처)을 가르는 연구는 찾지 못했다.
* **주요 위험**
  * Spacetop 라벨은 영상 49개 점이고 결측이 많다. 영상 단위 평가라 검정력이 낮다.
  * 정렬이 내용에서 학습되므로 내용 성분만 맞고 정서 성분은 맞지 않을 수 있다(Wang 2024의 지적). 잔차 전이(분석 3)가 그 판정이다.
  * 반대로 모델 feature에 정서 관련 방향이 들어 있으면 정렬이 정서를 '들여올' 수 있다. 정서 예측 방향을 모델 feature에서 뺀 판본으로 정렬을 다시 해 비교한다.
  * 스캐너, TR, 전처리, smoothing 차이. 영화 길이와 장르 차이.
  * 라벨이 모두 다르다(별도 평정자 1 Hz 대 본인 영상 후 1회). 전이 실패를 라벨 차이로만 설명하게 될 수 있다.
  * overlap: **EmoBrain**(사람 간 정서 decoding이라는 목표가 일부 겹친다. 차이는 공유 자극 없는 데이터셋 간 정렬과 valence 일반화 실패의 원인 분해). **Emo-FilM 연구**(데이터 겹침).

---

## 4. 비교 요약

| 질문 | AI 기여(plan.md 기준) | 한 달 판정 | 핵심 데이터 | 가장 큰 위험 |
|---|---|---|---|---|
| MD-RV-1 뜻 대 목소리 | (b) 말뜻 valence와 억양 valence를 같은 발화에서 분리. 뇌 분석 자체는 고전적 | 가능 | Spacetop narratives, alignvideo(정렬) | 소리 clip 36개, 양식 = 이야기 = run 순서 교란, 억양 추정 타당성 |
| MD-RV-2 화면 대 음악 | (b) 채널 분리, Horikawa 무음 평정으로 화면 채널 고정, (c) 자연 충돌 순간 생성 | 가능 | Emo-FilM, Cowen & Keltner 라벨 | 배경 소리 정서 추정에 인간 검증 없음, 영화 14편 |
| MD-RV-3 데이터셋 간 공통 축 | (b) 공유 자극 없는 데이터셋 간 정렬 | 전체판 불가, 축소판 가능 | Emo-FilM, Spacetop alignvideo (확장: MC) | 영상 49개 라벨, 정렬이 내용만 맞출 위험 |

* 사용자가 말한 세 방향과의 대응: 양식 간 정서 전이 = MD-RV-1(글 → 소리 → 영상), MD-RV-2(채널 사이); 정서의 공통 성분 = MD-RV-2의 공통 성분, MD-RV-1의 감각 공통 축; 데이터셋 간 공유 공간 = MD-RV-3, MD-RV-2의 Cowen & Keltner → Emo-FilM 다리.
* 내 판단으로 가장 먼저 해 볼 것: **MD-RV-2**. 데이터 교란이 가장 작고, AI가 하는 일(채널 분리와 충돌 탐지)이 관찰로 대체되지 않으며, 인간 무음 평정이라는 독립 기준이 있다. MD-RV-1은 0단계 관문(억양과 말뜻의 분리 가능성)을 1주 안에 판정할 수 있으므로 병행할 수 있다.

---

## 5. 검색 기록 (모두 2026-11-12)

| # | 도구 | 질의 | 결과 |
|---|---|---|---|
| 1 | WebSearch | fMRI valence decoding generalizes across spoken and written narratives prosody semantic content supramodal | 말과 글의 정서 전이, 억양 분리 연구 없음. Deniz 2019, Regev 2013, Lettieri 2024 등 인접 연구만 |
| 2 | WebSearch | speech emotion recognition model prosody features fMRI encoding naturalistic story listening valence 2024 2025 | fMRI에서 음성 정서 모델로 억양을 쓴 이야기 연구 없음. 텍스트 BERT 정서 feature 연구, MEG 포스터, EEG(arXiv:2509.21381)만 |
| 3 | PubMed | (prosody OR prosodic) AND (semantic OR lexical) AND emotion AND (multivariate OR MVPA OR decoding OR "representational similarity") AND fMRI, 2015~ | 8건. 통제 문장 연구(Mitchell 2013 포함), 뇌졸중, fNIRS. 자연 이야기와 감각 공통 축 연구 없음 |
| 4 | WebSearch | Miao 2026 Nature Communications Spacetop narratives theory of mind social interaction | Miao 2026은 사회적 상호작용과 ToM. 정서 아님 |
| 5 | WebSearch | film music changes emotion of visual scene fMRI naturalistic movie soundtrack visual affect separate contribution encoding model | Bravo 2024(통제 조작)가 가장 가까움. 채널별 정서 분산 분할 연구 없음 |
| 6 | PubMed | Bravo F[Author] dissonant music early visual processing | PMID 39008675, 10.1073/pnas.2320378121 확인 |
| 7 | WebSearch | Emo-FilM audio visual language features emotion fMRI encoding variance partitioning 2025 2026 | Emo-FilM에서 채널 분해 연구 없음. Marras 2025(행위 feature, 판본별 촬영) |
| 8 | WebSearch | audiovisual emotional incongruence naturalistic movie fMRI music visual conflicting valence which modality dominates | 자연 영화의 충돌 우세 검정 없음. 그림-음악 일치 미학 연구(2025)와 Bravo 2024 |
| 9 | WebSearch | cross-dataset emotion decoding fMRI shared latent space foundation model features no shared stimuli alignment different movies | Ke 2025(각성만 일반화), 비정서 공유 manifold, EEG 도메인 적응 |
| 10 | WebSearch | valence representation fails to generalize across movies datasets arousal generalizes fMRI context-dependent valence | Ke 2025 확인. 맥락 의존 설명은 직접 검정되지 않음 |
| 11 | WebSearch | functional alignment across subjects without shared stimuli using encoding model predicted responses hyperalignment different datasets fMRI | Wang 2024(arXiv:2403.11517), 연결 기반 정렬. 정서 적용 없음 |
| 12 | WebSearch, PubMed | hyperalignment improves between-subject emotion valence decoding naturalistic fMRI | Chan 2020(PMID 32036021), 한 데이터셋 안 공유 자극 정렬 |
| 13 | WebSearch | Spacetop alignvideo emotion fMRI 2026 multimodal foundation model valence self-report decoding | Spacetop 정서 decoding 연구 없음. "Evaluating TRIBE v2 ... Naturalistic Emotion"(NeurIPS 2026) 제목만 보임. neurips.cc는 이 세션 네트워크에서 열리지 않아(호스트 해석 실패) **미확인** |
| 14 | WebSearch | Tang Du Huth 2023 brain encoding models multimodal transformers transfer across language and vision | arXiv:2305.12248, NeurIPS 2023 확인 |
| 15 | WebSearch | negatively correlated concept tuning visual cortex ... inverted tuning follow-up | Tang 2023의 향후 과제(시각피질 반전 조율)를 설명한 후속 없음 |
| 16 | Crossref, PubMed, arXiv API | 식별자 확인: 10.1038/nn.3749, 10.1523/JNEUROSCI.1676-14.2014, 10.1523/JNEUROSCI.2161-10.2010, 10.1523/JNEUROSCI.1580-13.2013, 10.1523/JNEUROSCI.0675-19.2019, 10.1093/scan/nsv032, 10.1038/nn1392, 10.1016/j.neuron.2011.08.026, 10.1016/j.neuroimage.2017.01.002, 10.1016/j.cortex.2012.07.010, 10.1016/j.neuroimage.2025.121439, arXiv:2403.11517, 2305.12248, 2312.15185, 2211.08553, 2212.04356 | 모두 존재 확인 |
| 17 | GitHub raw | OpenNeuro ds005256 v1.1.0 participants.tsv, 앞 40명 ses-02 narratives events.tsv | 0.1절 계산 |
| 18 | GitHub raw | 모델 저장소 LICENSE와 README | 0.1절 라이선스 |

---

## 6. 미확인 사항

* Spacetop: 0.1절 계산은 앞 40명(자료 있는 37명) 기준이다. 나머지 참가자도 같은 배정인지는 전수 계산이 필요하다. 소리 clip 대본 파일 유무, 느낌 척도의 중심 좌표와 valence 변환 방식, 사용자의 fMRIPrep 파생본(ds007070) 보유 여부.
* Emo-FilM: 보유 영화 파일이 크레딧 절단판과 같은지, S07 자료 본체.
* 모델: emotion2vec과 V-JEPA 2의 가중치 사용 조건(저장소 문서 기준 MIT로 보이나 가중치 파일 조건은 미세 확인 필요), 사용할 LLM의 라이선스, 배경 소리 정서를 사람 평정으로 학습한 공개 checkpoint의 존재.
* 선행: "Evaluating TRIBE v2 Beyond Its Original Benchmarks: From Functional Localizers to Naturalistic Emotion"(NeurIPS 2026)의 데이터와 내용(호스트 접근 불가). Miao 2026 출판본 내용(이번 라운드 미재확인).
* 계산 자원: GPU 1~4장 가정. 보유 자원은 미기재(`reference/datasets_and_resources.md` 1절).
