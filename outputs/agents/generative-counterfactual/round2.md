# Round 2: Cross-Agent Exchange (generative-counterfactual, Agent 9)

* 작성: generative-counterfactual (Axis L Generative & Counterfactual Methods, Axis P Causality & Scientific Inference)
* 기준일: 2026-11-12
* 따른 절차: `reference/protocols.md` P2와 Coordinator 위임 메시지의 추가 요구
* 읽은 파일: 다른 10개 에이전트의 `round1.md`(emotion-theory, vision-decoding, encoding-foundation, multimodal-dynamics, frontier-ai, geometry-info, systems-neuro, llm-semantics, brain-inspired, adversarial-reviewer). 각 파일의 0, 1, 3, 4절은 전부, 6절은 chain별 New Research Question과 필요한 단계만 읽었다. `outputs/axis_encyclopedia.md` 0절과 2절, `outputs/STAGE_STATUS.md`의 사용자 결정 기록. encoding-foundation의 `literature.jsonl` 일부 항목(arXiv:2610.13558, 2605.13904, 2604.23865, 2607.01400, 2607.16292, 2604.04025, 2609.15685), `outputs/literature/literature_db.csv`의 ID 열.
* 바뀐 전제: 사용 가능한 데이터셋 5개(Horikawa 2020, Emo-FilM, Spacetop, NSD, Mind captioning ds005191). 새 독립 Axis U, V, W 채택. evidence-level(R0~R4)이 모든 질문의 필수 태그.
* 새로 확인해 `literature.jsonl`에 추가한 논문 6편(총 51편): arXiv:2610.13558(ROI-ReFT, 본문), arXiv:2608.06231(EmoWorld, 본문), arXiv:2609.02616(AffectDelta, 초록), doi:10.1016/j.neuroimage.2019.116216(Katsyri 2020, 초록), arXiv:2509.21381(초록), doi:10.1038/nn1057(Vuilleumier 2003, 초록). arXiv 논문은 export.arxiv.org API가 이번 세션 중 429와 시간 초과를 반환해 arxiv.org abs 페이지 메타데이터로 확인했다.
* 태그 표기: 각 제안에 `label-provenance`, `evidence-level`, `insilico-vs-observed`, `G1`을 단다. 라벨 출처 약칭은 llm-semantics 표기를 따른다: [Human-norm] 별도 평정자 규범, [Self] fMRI 참가자 본인, [Attrib-human] 타인 정서 귀속 판단, [AI-est] 모델 추정.

---

## 0. Round 1 이후 정정과 선행 수행 재확인

Coordinator가 전달한 교훈(Stage 2 "no" 판정의 25%가 실제로는 선행 수행됨)에 따라 내 Round 1 사슬의 새로움 주장을 다시 검색했다. 결과적으로 두 개를 "partially"로 낮추고, 하나의 사실 전제를 고친다.

| 항목 | Round 1 판단 | 정정 | 근거와 검색 경로 |
|---|---|---|---|
| CH1 의미 고정 정서 편집 + encoder | no | **partially** | ROI-ReFT(arXiv:2610.13558, 본문 확인)는 TRIBE v2 예측 반응 중 **정서 관련 ROI 변화를 편집 방향, 시각 ROI를 내용 기준**으로 쓰는 편집기를 만들었다. 즉 "예측 정서 반응은 바꾸고 예측 시각 반응은 유지하는 편집"이라는 R1 장치는 이미 있다. 다만 목적이 더 나은 편집이고, 정서 성공은 분류기 판정이며, 인간 평정과 관찰 fMRI 검증이 없고, TRIBE v2를 교사와 평가 공간으로 함께 써서 순환이다. 남는 새로움은 "관찰 fMRI로 학습한 encoder를 반증 대상으로 두고 인간 manipulation check를 붙인 과학적 사용"으로 좁아진다. 검색: arxiv.org/search 질의 "emotion editing fMRI"(1건, 이 논문), "TRIBE emotion"(2건 중 관련 1건), "semantic preserving emotion editing"(15건, 관련 도구 EmoWorld, AffectDelta 확인), WebSearch "emotion image editing brain encoding" |
| CH4 Emo-FilM 음악 stem counterfactual | partially(관찰 연구만) | **partially, 근거 추가** | arXiv:2509.21381(초록)이 LIRIS 계열 영화를 포함한 3개 데이터셋에서 음성과 배경 사운드트랙을 분리해 EEG와 행동 정서 반응을 encoding했다(관찰적 연관). stem 제거, 교체 counterfactual을 fMRI encoder로 in silico 시험한 연구는 찾지 못했다. arXiv:2604.04025는 TRIBE v2 audio-only 추론으로 생성 음악의 예측 피질 반응을 비교했지만 영화와 정서 평정이 없다. 검색: arxiv.org/search "soundtrack fMRI"(1건, arXiv:2410.17300), WebSearch "brain encoding model in silico experiment removing music soundtrack film" |
| TRIBE v2의 피질하 예측 | Round 1 M1, CH2, CH4는 TRIBE v2로 amygdala 등을 예측할 수 있다고 암묵 가정 | **정정** | encoding-foundation Round 1(0절 핵심 메시지 1)이 공개 checkpoint는 fsaverage5 피질의 평균 피험자 예측만 내고 피질하와 피험자별 readout이 없다고 기록했다(README와 arXiv:2607.01400 8절 근거). arXiv:2604.04025 초록도 fsaverage5 피질 예측만 썼다. 따라서 amygdala, pulvinar 등 피질하 in silico 반응은 **우리 데이터셋으로 직접 학습한 encoder**(Horikawa 피질하 ROI, NSD aseg amygdala, Emo-FilM raw 재전처리)로만 계산하고 systems-neuro의 signal-feasibility 태그를 붙인다 |
| U4 AI다움 confound | 생성 자극은 신기성, 현저성 효과를 섞는다 | **세분화** | Katsyri 2020(doi:10.1016/j.neuroimage.2019.116216, 초록): 정서 표정에 대한 amygdala 반응은 실제 얼굴과 CG 얼굴에서 비슷했지만, FFA 반응은 실제 얼굴이 크고 직시 시선의 amygdala 효과는 실제 얼굴에서만 나타났다. AI다움 confound는 일률적이지 않고 **속성별**(표정 vs 시선, amygdala vs FFA)로 다르다 |
| 새 도구 | 없음 | 추가 | EmoWorld(arXiv:2608.06231, 본문): Cowen & Keltner 27범주에서 영상 정서를 **분위기(전역 외관), 의미 단서(국소 내용), 시간 진행**으로 분리해 제어하고 54명 쌍비교로 지각 검증. 한계 절: 표정, 인물 행동, 서사 인과는 다루지 않음. 의미 고정 편집의 '분위기' 팔로 쓸 수 있으나 인물 중심 클립에는 표정 도구를 따로 써야 한다 |
| 고전 선행 | 언급 없음 | 추가 | 저공간주파수 공포 얼굴이 amygdala, pulvinar, 상구 반응을 키운다는 결과는 이미 자극 조작(R3 수준)으로 검증되었다(Vuilleumier 2003, doi:10.1038/nn1057, 초록). 아래 GC-P5의 새로움은 "자연 영상 전체로의 확장"에 한정된다 |

내 Round 1 `round1.md`는 기록으로 두고 고치지 않았다. 위 정정이 그 문서의 CH1, CH2, CH4, M1, U4에 우선한다.

---

## 1. 가져온 아이디어

### I1. Mind captioning의 정서 배제 인간 캡션과 72클립 x 5회 반복 (출처: vision-decoding 0.1절과 R6, llm-semantics Chain 1)
* 근거: Horikawa 2025 Mind captioning(doi:10.1126/sciadv.adw1464). vision-decoding이 본문으로 확인한 사양: Horikawa 2020과 같은 Cowen & Keltner 비디오, 6명, 72개 테스트 비디오 각 5회 반복, 비디오당 MTurk 캡션 20개를 "정서가 아니라 시각 내용만 쓰라"는 지시로 수집.
* 내 쪽으로 가져오는 방식 두 가지.
  1. **편집의 의미 불변성 척도.** 내 Round 1 CH1은 "의미를 고정한 정서 편집"을 캡션 embedding 거리로 확인하려 했지만, 그 캡션은 AI가 쓴 것이었다. 인간 중립 캡션 20개가 있으면 (a) 같은 지시로 MLLM 중립 캡션 생성기를 원본 클립에서 인간 캡션 간 변동과 같은 지표로 검증하고, (b) 편집 전후 중립 캡션 embedding 거리가 원본 클립의 인간 캡션 간 변동 범위 안에 들 때만 "의미 고정"으로 인정할 수 있다. 의미 불변성의 기준이 AI가 아니라 인간 판단 변동이 된다.
  2. **In silico 대 관찰 비교의 신뢰도 상한.** 같은 72클립 5회 반복은 내 CH3(같은 자극에서 TRIBE v2 예측과 실측의 정서 구조 비교)에 클립 수준 noise ceiling을 준다. Horikawa 2020과 Emo-FilM에는 반복이 없어 "surrogate가 놓친 구조"와 "실측 잡음"을 구분할 수 없었다.
* 주의: 두 코호트의 피험자 중복 여부는 미확인이다(vision-decoding 0.1). 중복되면 교차 코호트 비교에 subject-level leakage가 생긴다. 사용자 보유 판본의 캡션 포함 여부도 미확인이다.

### I2. Prediction-powered inference와 alt-test를 편집 자극의 manipulation check에 (출처: adversarial-reviewer I1, I2, U5)
* 근거: Angelopoulos 2023(doi:10.1126/science.adi6000), Calderon 2025 alt-test(arXiv:2501.10970).
* 내 쪽 문제: counterfactual 설계는 편집마다 "정서가 실제로 바뀌었는가"를 인간 평정(R2)으로 확인해야 하는데, 편집 수가 수천 개면 전부 평정받기 어렵다. AI 정서 추정으로 대신하면 그 자체가 [AI-est]이고 편집 방향과 같은 계열 모델을 쓰면 순환이다(ROI-ReFT의 분류기 판정이 그 예).
* 가져오는 방식: 모든 편집에 MLLM 정서 추정을 붙이고, 편집 집합 안에서 **무작위로 뽑은** 부분집합만 인간 평정을 받아 PPI로 편집 효과(편집 강도에 따른 정서 변화)를 보정 추정한다. alt-test로 "편집 자극의 정서 평정에서 MLLM이 인간 평정자를 대체할 수 있는가"를 편집 가족별로 따로 검정한다. 의미 고정 편집(분위기, 표정)과 의미 변경 편집(객체 추가)에서 대체 가능성이 다르면, 그것 자체가 MLLM 정서 판단이 의미 내용에 기대는 정도의 측정치가 된다.

### I3. 측정 오차가 만드는 잔여 교란 (출처: adversarial-reviewer U1, D2)
* 근거: Westfall & Yarkoni 2016(doi:10.1371/journal.pone.0152719): 공변량이 불완전하게 측정되면 증분 타당도 검정의 위양성률이 매우 높고 표본이 클수록 오른다. Horikawa 2020은 정서, 시각, 의미 모델을 따로 적합해 비교했다(adversarial-reviewer가 본문 확인).
* 내 쪽으로 가져오는 의미: 통계적 통제(variance partitioning)만으로는 "정서가 내용을 넘어 설명한다"를 확정할 수 없다는 독립 근거다. 내 CH1의 설계 수준 탈상관(counterfactual 편집)이 필요한 이유가 된다. 동시에 counterfactual도 "encoder feature 공간"이라는 다른 측정 도구에 의존하므로 같은 종류의 비판을 받는다. 그래서 둘을 대체가 아닌 **삼각 검증**으로 묶는다(GC-P3).

### I4. 실제 감각 판본 조작과 평정자 반복 시청 (출처: multimodal-dynamics U3, X3, 4절 5번)
* 근거: Lettieri 2024(doi:10.1126/sciadv.adk6840): 같은 영화의 시청각, 시각 전용, 청각 전용 판본과 선천 맹, 농 참가자. vmPFC는 양식 무관 범주 부호, pSTS는 양식 무관 valence를 보였지만, 유발되는 정서 자체가 판본마다 달랐고 저자는 vmPFC 추상 부호가 언어 채널에 기댈 수 있다고 썼다(multimodal-dynamics가 본문 확인).
* 가져오는 방식: 내 CH4의 stem 제거와 TRIBE v2 modality dropout은 R1이다. Lettieri의 실제 판본 조작 결과는 이 in silico 조작이 재현해야 할 **관찰 기준(benchmark)**이 된다. surrogate가 "청각 전용 판본에서 공포가 약해진다"는 관찰 결과를 재현하지 못하면, Emo-FilM 음악 stem 제거의 in silico 결과도 믿기 어렵다.
* 추가: multimodal-dynamics는 Emo-FilM 평정자가 같은 영화를 최대 6번 봤으므로 consensus가 처음 보는 fMRI 참가자보다 앞당겨진 시계열일 수 있다고 지적했다(doi:10.7554/eLife.64972 근거). 음악 단서 시작 시점을 기준점으로 평정 변화 lag와 뇌 반응 lag를 비교하는 데 쓸 수 있다.

### I5. Kuleshov 편집과 정서 대 상황 판별 (출처: llm-semantics 4절 U4와 Chain 7, frontier-ai T4)
* 근거: Mobbs 2006(doi:10.1093/scan/nsl014): 같은 얼굴이 선행 맥락에 따라 다르게 귀속되고 amygdala, STS, 측두극 반응이 달라짐. frontier-ai T4는 arXiv:2604.13466의 판별 검정 논리로 (상황 유사, 정서 상이)와 (상황 상이, 정서 유사) 자극 쌍을 고르자고 제안했다.
* 가져오는 방식: Kuleshov 쌍(같은 얼굴 클립 + 다른 선행 맥락)은 "얼굴은 고정, 맥락만 편집"이라는 내 편집 가족의 하나가 된다. frontier-ai의 쌍 선택은 자연 자극에서 이루어지는데, 공선성 때문에 (상황 유사, 정서 상이) 칸이 드물다. 그 칸을 편집으로 채우는 것이 내 쪽 기여다(GC-P6).

### I6. 피질하 신호 가능성과 amygdala 반복 감쇠 (출처: systems-neuro 0.5절, Chain 4)
* 근거: systems-neuro 0.5.1 판정표(Horikawa TE 43 ms, Emo-FilM 6 mm smoothing 제공본, NSD 반복과 기억 과제), Dense Amygdala(doi:10.1038/s41597-026-07065-x)의 amygdala tSNR과 dropout 개인차, Abdel-Ghaffar 2024(doi:10.1038/s41467-024-49073-8) Discussion 6단락의 amygdala 신기성 민감성.
* 가져오는 방식: (a) 내 CH2(범주 고정 amygdala 제어)의 모든 amygdala in silico 결과에 signal-feasibility 태그를 붙이고, 개인별 dropout 마스크를 encoder 학습 전에 적용한다. (b) NSD 반복에 따른 amygdala 감쇠는 "신기성 1단위가 amygdala를 얼마나 움직이는가"의 보정 곡선이 될 수 있다. 생성 자극의 AI다움이 amygdala 예측을 올리는 정도를 이 곡선으로 상한 추정할 수 있다(GC-P5).

### I7. 행동 경향과 장면 affordance (출처: brain-inspired P-2, I-3, 4절 3번, 새 Axis V)
* 근거: Bartnik 2025(doi:10.1073/pnas.2414005122): 장면 affordance 표상은 물체, layout으로 환원되지 않고 DNN feature는 affordance보다 물체 쪽에 정렬된다. Horikawa 2020 Discussion 2단락의 "emotional experience (or affordances)".
* 가져오는 방식: 위협 대상은 고정하고 회피 affordance(출구, 거리, 장애물)만 바꾸는 편집은 정서 범주와 행동 경향의 공선성을 깨는 자극을 만든다(GC-P8).

---

## 2. 보내는 제안

### GC-P1 → encoding-foundation: "in silico 정서 기하 충실도"를 하나의 관문 연구로 합치고, 편집 자극을 분포 밖 시험 세트로 제공

* **제안 내용.** 너희 Chain 1(관찰 정서 기하 중 group encoder가 재현하는 부분), Chain 3(group 예측 잔차와 개인 정서 보고)은 내 Round 1 CH3, CH5와 같은 질문이다. 이를 하나의 **관문(gate) 연구**로 합치자. 우리 쪽 counterfactual 편집 자극으로 검증하거나 확장할 수 있다.
  1. **같은 자극 비교와 신뢰도 상한.** Horikawa 2020(5명), Mind captioning(6명, 72클립 5회 반복), Emo-FilM(30명)에서 같은 자극의 실측과 TRIBE v2 예측(피질)을 비교한다. Mind captioning 반복으로 클립별 신뢰도 상한을 먼저 구해 "재현되지 않는 정서 구조"가 잡음인지 surrogate 결함인지 구분한다. EmoMind(arXiv:2605.16739)의 RSA 손실(ρ 0.635에서 0.166)은 자극 집합이 달라 이 구분을 못 했다.
  2. **편집 민감도 일치 검정.** 우리 쪽 2x2 편집 자극(정서 단서만 변경 / 의미만 변경)을 분포 밖 시험 세트로 제공한다. (a) Horikawa 또는 Mind captioning 실측으로 학습한 voxelwise encoder와 (b) TRIBE v2가 **같은 편집에 같은 방향의 예측 변화**를 내는지 본다. 두 surrogate가 편집 방향에서 갈리면 그 편집에 대한 모든 R1 결론이 모델 의존적이라는 뜻이다. 일치해도 같은 backbone(V-JEPA 2)을 쓰면 같이 틀릴 수 있으므로 backbone이 다른 encoder 쌍을 둔다.
  3. **정답 신호 심기를 편집 분석에도.** 너희 I5(합성 뇌에 알려진 정서 신호를 심고 pipeline이 회복하는지)를 우리 2x2 분석에 적용한다. 정서 단서에만 반응하는 가짜 voxel과 의미에만 반응하는 가짜 voxel을 심었을 때 우리 분석이 둘을 구분하는지가 CH1의 최소 검증이다.
* **관련 Axis:** H, L, S, T, U
* **근거 논문 ID:** arXiv:2605.04326, arXiv:2605.16739, doi:10.1126/sciadv.adw1464, arXiv:2302.06677, arXiv:2607.01400, arXiv:2610.13558
* **가능한 데이터셋:** Horikawa 2020, Mind captioning, Emo-FilM
* **예상되는 반론.** (a) 공개 TRIBE v2는 피질 평균 피험자만 예측하므로 amygdala와 개인 잔차 비교는 불가하다. 맞다. 피질하와 개인 수준은 우리 데이터 학습 encoder로만 하고, TRIBE 비교는 피질 group 수준으로 한정한다. (b) Horikawa 공개 전처리본은 비디오당 블록 평균이라 TRIBE 시계열과 형식이 다르다. TRIBE 예측을 같은 HRF 지연과 블록 평균으로 변환해 맞추고, raw 재전처리판으로 민감도 분석을 한다. (c) Mind captioning과 Horikawa 2020의 피험자 중복 여부가 미확인이다. 중복 확인 전에는 두 코호트를 독립 반복으로 세지 않는다. (d) 편집 자극은 두 encoder 모두의 분포 밖이라 일치 자체가 타당성을 보장하지 않는다. 그래서 2번은 "필요조건 검사"로만 쓴다.
* **태그:** label-provenance = [Human-norm](Horikawa, Mind captioning 쪽 정서 평정은 Horikawa 2020의 Cowen & Keltner 규범 평정 재사용, Emo-FilM consensus), 대상 felt 보고의 집단 평균. evidence-level = R0(관문 비교) + R1(편집 민감도). insilico-vs-observed = 혼합. G1 = 필요(보유).

### GC-P2 → llm-semantics (참조: vision-decoding): 기술 잔차(통계 통제)와 의미 고정 편집(설계 통제)을 같은 voxel에서 맞대기

* **제안 내용.** 너희 Chain 1(정서 배제 캡션 LLM embedding을 통제한 뒤 남는 규범 정서 고유 분산)과 vision-decoding R6은 R0 수준의 통계적 통제다. 우리 쪽 의미 고정 편집(R1 + R2)으로 같은 질문을 설계 수준에서 검증하거나 확장할 수 있다.
  1. **역할 분담.** 너희 쪽 정서 배제 캡션 생성기를 Mind captioning 인간 중립 캡션으로 검증한 뒤(I1), 우리 편집 자극의 의미 불변성 척도로 쓴다. 너희 Chain 1이 "기술 잔차가 남는 voxel"을 내면, 우리는 같은 voxel에서 "의미 고정 정서 편집에 예측이 반응하는가"를 본다.
  2. **판정표(사전 등록).** 두 결과가 모두 양성이면 정서 고유 신호의 근거가 강해진다. 기술 잔차는 양성인데 편집 민감도는 음성이면 (a) 캡션이 놓친 의미(중위 시각 특징 등)가 잔차를 만들었거나, (b) encoder feature 공간이 편집을 보지 못한 것이다. 편집별 feature 변위로 (b)를 먼저 배제한다. 반대 조합이면 잔차 분석의 검정력 부족이나 과통제(정서 정보를 담은 묘사까지 통제)를 의심한다.
  3. **Kuleshov 자극 생성.** 너희 Chain 7과 4절 U4의 Kuleshov형 맥락/인물 분리를 우리가 실제 자극으로 만든다(같은 얼굴 클립 + 선행 맥락 교체, 인물 제거 프레임). MLLM 회귀자(in silico)에 더해 R2로 관점을 나눈 인간 평정("인물이 느끼는 정서"와 "당신이 느끼는 정서")을 따로 받으면, 너희 P1(귀속 vs 경험)을 같은 자극에서 행동 수준으로 먼저 분리할 수 있다.
* **관련 Axis:** C, L, P, U
* **근거 논문 ID:** doi:10.1126/sciadv.adw1464, doi:10.1038/s42256-025-01072-0, doi:10.1093/scan/nsl014, arXiv:2408.13718, arXiv:2610.13558, arXiv:2608.06231
* **가능한 데이터셋:** Horikawa 2020, Mind captioning, Emo-FilM(Kuleshov 맥락 편집은 시간 맥락이 있는 Emo-FilM 장면이 더 적합)
* **예상되는 반론.** (a) "정서 배제" 캡션도 "장례식"처럼 정서 함의가 큰 묘사를 담는다. 정서를 쓰지 않은 것이지 정서 정보가 없는 것이 아니다. 이 경우 기술 잔차는 과소 추정되고(과통제), 편집 설계가 그 공백을 보완한다. (b) MLLM 캡션 생성기가 정서 편집에 둔감하거나 과민할 수 있다. 원본에서의 인간 대비 검증(I1)과 편집 가족별 alt-test(I2)로 점검한다. (c) Horikawa는 무음 짧은 클립이라 Kuleshov 맥락 편집에 맞지 않는다. 동의한다. Kuleshov는 Emo-FilM 장면으로, 의미 고정 편집은 Horikawa로 나눈다. Emo-FilM 영화별 CC 조항이 파생물을 막으면 인간 평정용 시청 자체가 제한될 수 있다. (d) 새 R2 평정은 fMRI 참가자의 경험이 아니다.
* **태그:** label-provenance = 원 데이터 [Human-norm](felt 보고 평균) + 신규 R2 평정(별도 평정자, 지시문으로 perceived/attributed와 felt를 분리) + [AI-est](MLLM 캡션과 정서 추정). evidence-level = R0 + R1 + R2. insilico-vs-observed = 혼합. G1 = 필요(보유).

### GC-P3 → adversarial-reviewer: 통계 통제와 설계 통제의 사전 등록 삼각 검증, affective metamer 통합, PPI 기반 manipulation check

* **제안 내용.** 너희 쪽 측정 오차와 식별 가능성 비판을 우리 쪽 counterfactual 설계로 검증하거나 확장할 수 있다.
  1. **삼각 검증.** 너희 D2(시각-의미 내용을 여러 지표의 잠재 구성개념으로 통제하고 신뢰도를 반영한 정서 고유 분산 포화 곡선)와 우리 CH1(2x2 counterfactual)은 같은 주장("정서가 내용을 넘어 설명한다")을 서로 다른 가정으로 시험한다. D2는 공변량 지표 집합의 완전성과 신뢰도 추정에 기대고, CH1은 encoder feature 공간이 편집을 볼 수 있다는 것과 편집의 의미 누출, AI다움 통제에 기댄다. **실패 방식이 다르므로**, 같은 voxel 집합과 같은 데이터 분할에서 두 결론의 일치표를 사전 등록하자. 둘 다 정서 고유 신호를 지지할 때만 강한 주장으로 쓰고, 불일치하면 어느 가정이 깨졌는지 진단 항목으로 쓴다.
  2. **Affective metamer 통합.** 너희 I6과 내 Round 1 X2가 독립적으로 같은 제안을 했다(Feather 2023, doi:10.1038/s41593-023-01442-0). 생성(정서 모델 또는 encoder 정서 voxel의 활성을 맞춘 자극, 의미 embedding은 같고 예측 정서만 다른 자극)은 우리가 맡고, 반증 해석 기준(통과는 충분조건이 아니고 실패가 표상 부재를 뜻하지 않음)과 matched-complexity null은 너희가 정하자.
  3. **편집 자극의 PPI와 alt-test.** 너희 I1, I2를 편집 자극의 manipulation check에 쓴다(I2 참조). PPI의 전제(인간 평정 표본이 같은 분포의 무작위 표본)를 지키기 위해 인간 평정 부분집합은 편집 집합 안에서 층화 무작위로 뽑는다.
* **관련 Axis:** T, P, L, Q, U
* **근거 논문 ID:** doi:10.1371/journal.pone.0152719, doi:10.1016/j.neuroimage.2022.119728, doi:10.1038/s41593-023-01442-0, doi:10.1126/science.adi6000, arXiv:2501.10970, arXiv:2302.06677
* **가능한 데이터셋:** Horikawa 2020(주), Mind captioning(신뢰도), NSD(metamer 이미지와 nsdmeadows 100장 기준점)
* **예상되는 반론.** (a) 삼각 검증의 판정 규칙이 사후에 정해지면 분석 자유도만 늘어난다. 그래서 판정표와 voxel 선택 분할을 데이터 분석 전에 고정한다. (b) 편집 자극에서 encoder 예측이 바뀌는 것은 뇌 증거가 아니다. 맞다. CH1의 결론은 R1이며, D2와 일치해도 "encoder와 통계 통제가 같은 voxel을 가리킨다"까지만 말한다. (c) metamer 생성은 최적화가 metamer 집합을 균일 표집하지 않는다(Feather 2023 Limitations). 시작점을 여러 개 두고 표집 다양성을 보고한다.
* **태그:** label-provenance = [Human-norm] + 신규 R2 평정 + [AI-est](PPI 보정 대상). evidence-level = R0(D2) + R1(CH1, metamer) + R2(평정). insilico-vs-observed = 혼합. G1 = 필요(보유).

### GC-P4 → multimodal-dynamics: 소리 분해의 관찰 분할(R0)을 stem counterfactual(R1)로 확장하고 실제 판본 조작으로 surrogate를 검증

* **제안 내용.** 너희 Chain 3((a) 정서 항목별 대사, 음악, 효과음, 영상 feature의 고유 설명량, (b) 언어, 음악 feature 제거 후 vmPFC와 hippocampus 정서 decoding이 남는가)을 우리 쪽 stem counterfactual로 검증하거나 확장할 수 있다.
  1. **두 수준의 같은 질문.** 같은 3-stem 분리(arXiv:2110.09958) 결과로 (a) 너희 R0 variance partitioning의 "고유 설명량"과 (b) 우리 R1의 "그 stem을 지웠을 때 TRIBE v2 예측 변화량"을 정서 항목별로 함께 계산한다. 두 지표가 같은 정서 항목(예: 공포, 긴장)에서 크면 음악 의존성의 근거가 겹친다. 고유 설명량은 큰데 제거 효과가 작으면 surrogate가 음악을 다른 채널로 대신 예측하거나(공선성), 고유 설명량이 공선성으로 부풀었을 수 있다.
  2. **관찰 기준으로 surrogate 검증.** Lettieri 2024(doi:10.1126/sciadv.adk6840)의 실제 판본 조작 결과(시청각, 시각 전용, 청각 전용에서 유발 정서 차이)를 TRIBE v2 modality dropout이 재현하는지 먼저 본다. 재현하지 못하면 Emo-FilM stem 제거의 in silico 결과는 보고하지 않거나 "검증 실패 surrogate"로 표기한다.
  3. **평정 lag와 음악 단서.** 너희 4절 5번(평정자 반복 시청에 따른 예측적 앞당김)을 음악 stem 시작 시점으로 시험한다. 음악 시작 대비 consensus 평정 변화 lag가 fMRI 참가자 뇌 반응 lag보다 짧으면 앞당김 가설을 지지한다.
* **관련 Axis:** M, D, L, B, P
* **근거 논문 ID:** doi:10.1126/sciadv.adk6840, arXiv:2110.09958, arXiv:2509.21381, arXiv:2605.04326, doi:10.7554/eLife.64972, arXiv:2604.04025
* **가능한 데이터셋:** Emo-FilM(주), Spacetop alignvideo(소리 있음, 본인 평정), Horikawa 2020(무음 대비)
* **예상되는 반론.** (a) stem 분리 잡음이 결과를 지배할 수 있다. 원 stem을 다시 섞은 재구성판을 대조로 두고, 재구성판과 원본의 예측 차이가 음악 제거 효과보다 크면 해석을 멈춘다. (b) TRIBE v2의 음향 feature 추출기가 음악에 대해 분포 밖일 수 있다. 음악 전용 feature(MERT 등)를 넣은 우리 데이터 학습 encoder와 결과를 비교한다. (c) Emo-FilM 정서 평정은 별도 평정자 것이고 fMRI 참가자 경험이 아니다. (d) Emo-FilM 영화별 CC 조항(특히 NoDerivatives)이 확인되기 전에는 counterfactual 판본을 외부 평정자에게 보여주는 R2를 하지 않는다. arXiv:2509.21381은 LIRIS 계열에서 음성과 사운드트랙을 분리해 정서 encoding을 이미 했다(EEG, 관찰). 우리 쪽 새로움은 fMRI encoder의 in silico 제거 효과와 관찰 기준 검증이다.
* **태그:** label-provenance = [Human-norm](Emo-FilM 1 Hz consensus, felt 보고) + [Self](Spacetop). evidence-level = R0(너희) + R1(우리). insilico-vs-observed = 혼합. G1 = 필요(보유, 판본 일치 미확인).

### GC-P5 → systems-neuro (참조: brain-inspired Chain 3): 자연 영상의 공간주파수 counterfactual과 AI다움 보정 곡선

* **제안 내용.** 너희 Chain 3(상구-pulvinar-amygdala 경로가 자연 영상의 저공간주파수, looming 같은 위협 동역학을 따르는가)과 Chain 4(NSD amygdala 반복 감쇠)를 우리 쪽 counterfactual로 검증하거나 확장할 수 있다.
  1. **공간주파수 counterfactual.** Horikawa와 Spacetop 클립의 저역통과, 고역통과, 위상 무작위화 판본을 만들어 데이터셋 학습 amygdala, pulvinar encoder의 예측 변화를 본다(R1). 저주파 공포 얼굴이 amygdala, pulvinar, 상구 반응을 키운다는 결과는 통제 얼굴로 이미 검증되었다(Vuilleumier 2003, doi:10.1038/nn1057). 남은 질문은 자연 영상 전체에서 "어떤 장면 내용이 저주파로 살아남아 amygdala encoder를 움직이는가"다. 이 조작은 생성 모델이 필요 없는 고전 필터라 AI다움 confound가 없다는 장점이 있다.
  2. **AI다움 보정 곡선.** NSD에서 반복 횟수에 따른 amygdala 감쇠 기울기를 "신기성 1단위의 효과"로 정의하면, 생성 자극의 신기성(사실감 평정 또는 video world model surprise)이 amygdala 예측과 실측을 얼마나 올릴 수 있는지 상한을 추정할 수 있다. NeuroVolve(arXiv:2512.00557)의 생성 이미지가 자연 이미지보다 V4, V8과 일부 OFC를 더 활성화한 결과, Katsyri 2020(doi:10.1016/j.neuroimage.2019.116216)의 속성별 차이(표정은 같고 시선, FFA는 다름)를 함께 보면 AI다움은 영역과 속성마다 달라 보인다.
  3. **필수 태그 선적용.** 모든 피질하 in silico 결과에 너희 signal-feasibility 판정(Horikawa TE 43 ms, Emo-FilM 6 mm 제공본 등)을 먼저 붙이고, 판정이 "부적합"인 영역은 encoder를 학습하지 않는다.
* **관련 Axis:** E, B, L, P, Q
* **근거 논문 ID:** doi:10.1016/j.neuron.2021.06.001, doi:10.1038/nn1057, doi:10.1038/s41467-024-49073-8, doi:10.1016/j.neuroimage.2019.116216, arXiv:2512.00557, doi:10.1038/s41597-026-07065-x
* **가능한 데이터셋:** Horikawa 2020, Spacetop(Kragel 2021과 같은 획득 조건), NSD(반복 감쇠)
* **예상되는 반론.** (a) 피질하 encoder의 예측력이 낮으면 counterfactual 예측 변화도 잡음 수준이다(Gu 2023 doi:10.1038/s42003-023-05440-7: 조절 효과는 encoder 정확도에 비례). 예측력 하한을 정해 넘는 피험자와 영역만 보고한다. (b) 경로 수준 분석(MPathI)은 패턴 기반이라 영역별 encoder로 근사하기 어렵다. 동의한다. 1번은 영역 수준 encoder로 한정하고 경로 주장은 하지 않는다. (c) NSD 반복 감쇠는 기억 과제와 섞여 있어 순수 신기성 지표가 아니다. 상한 추정에만 쓴다.
* **태그:** label-provenance = Horikawa [Human-norm], Spacetop [Self], NSD 정서 라벨은 [AI-est] 또는 nsdmeadows 100장. evidence-level = R1(필터 counterfactual) + R0(반복 감쇠). insilico-vs-observed = 혼합. signal-feasibility = 필수 점검. G1 = 필요(보유).

### GC-P6 → frontier-ai: 정서 대 상황 판별 검정의 빈 칸을 편집으로 채우고, 정서 기대 위반 쌍을 생성

* **제안 내용.** 너희 T4(상황 유사·정서 상이 쌍과 상황 상이·정서 유사 쌍으로 ROI별 RSA 판별)와 T9(정서적 기대 위반 영상 쌍으로 world model surprise 평가)를 우리 쪽 편집으로 검증하거나 확장할 수 있다.
  1. **T4의 빈 칸.** 자연 자극에서는 상황과 정서가 공선적이라 "상황 유사·정서 상이" 쌍이 드물고, 고르더라도 남는 차이가 작다. 같은 장면에 분위기 편집(EmoWorld식, arXiv:2608.06231)이나 표정 편집을 가하면 이 칸을 체계적으로 채울 수 있다. 자연 쌍(관찰, R0)과 편집 쌍(R1)에서 같은 ROI가 같은 쪽 유사도를 따르는지 비교하면 편집 자극 고유의 효과를 분리할 수 있다.
  2. **T9 위반 쌍의 교차 설계.** "장례식 + 웃음" 같은 위반 편집은 웃음이라는 내용을 추가하므로 정서만 바꾼 것이 아니다. 그래서 맥락(장례식 / 결혼식) x 표정(웃음 / 울음)의 2x2를 같은 편집량으로 만들고, V-JEPA 2 surprise(arXiv:2502.11831 방식)가 상호작용(위반 칸)에서만 커지는지 본다. 주효과(웃음 추가 자체의 surprise)를 상호작용과 분리하는 것이 핵심이다. 인간 놀람 평정(R2)과 맞춘다.
  3. **너희 CH6의 공선성 없는 시험.** "정서와 무관한 정렬이 정서 기하를 운반하는가"는 자연 고정서 자극에서는 정서와 내용이 함께 달라 판단이 섞인다. 의미 고정 정서 편집 쌍에서 VLM 정서 벡터를 사상에 통과시킨 예측 차이가 encoder 예측 차이와 맞는지 보면 정서 성분만의 운반을 볼 수 있다.
* **관련 Axis:** I, R, C, L, D
* **근거 논문 ID:** arXiv:2604.13466, arXiv:2502.11831, arXiv:2608.06231, arXiv:2609.34742, doi:10.1093/scan/nsl014, arXiv:2506.09985
* **가능한 데이터셋:** Horikawa 2020, Emo-FilM, NSD
* **예상되는 반론.** (a) 편집 쌍은 분포 밖이라 RSA 차이가 편집 인공물에서 올 수 있다. null-edit(편집 없이 같은 파이프라인 통과) 쌍을 기준으로 둔다. (b) 생성 영상 모델과 V-JEPA 2가 비슷한 인터넷 영상 분포에서 학습되어 surprise가 생성 인공물에 민감할 수 있다. 위반 효과를 상호작용 항으로만 해석하는 것이 이 문제를 줄인다. (c) 현재 데이터셋에 위반 쌍에 대한 실측 fMRI가 없다. 이 부분은 R1 + R2이며 실측은 신규 수집 계획으로만 남긴다.
* **태그:** label-provenance = [Human-norm](원 자극) + 신규 R2 + [AI-est](VLM 정서 벡터). evidence-level = R0 + R1 + R2. insilico-vs-observed = 혼합. G1 = 필요(보유).

### GC-P7 → vision-decoding: 정서 영역 선호 자극 합성(R4)과 범주 고정 amygdala 제어(내 CH2)를 합치고, prior-vs-evidence 분해를 생성 쪽에도 적용

* **제안 내용.** 너희 R4(정서 유발 영상으로 학습한 amygdala, 섬엽, vmPFC encoder의 선호 합성 이미지가 저수준, 의미 범주, 둘 다 아닌 것 중 무엇으로 환원되는가)는 내 Round 1 CH2와 거의 같다. 우리 쪽 범주 고정 목표와 AI다움 통제로 검증하거나 확장할 수 있다.
  1. **두 단계 설계.** 1단계(너희 R4): 제약 없는 선호 자극 합성과 환원 분석. NeuroVolve(arXiv:2512.00557)의 amygdala 결과(최대화 = 표정 얼굴, 최소화 = 건물)가 Horikawa 학습 encoder에서도 재현되는지. 2단계(우리): FFA, EBA, PPA 예측을 고정하는 다중 영역 제약 아래에서도 amygdala 예측을 움직이는 편집이 있는지. 1단계에서 의미 범주로 환원되고 2단계에서 움직이는 편집이 없으면 "이 encoder의 amygdala 선호는 범주 선호"라는 결론이 R1 수준에서 서고, 움직이는 편집이 있으면 그 편집의 정서 내용을 R2로 확인한다.
  2. **생성 쪽 prior-vs-evidence 분해.** 너희 I2(재구성 출력 정서 중 뇌 증거 몫과 생성 prior 몫)를 brain-guided 생성에도 쓴다. 같은 목표를 무작위 encoder 가중치나 다른 영역 목표로 바꿔 생성했을 때도 나오는 내용(예: 밝은 색, 얼굴)은 생성 prior의 몫이다. Rothermel 2026(arXiv:2609.27729)은 diffusion 단계가 valence steering 효과를 약화하거나 바꾼다고 보고했다.
* **관련 Axis:** G, L, E, H
* **근거 논문 ID:** arXiv:2512.00557, doi:10.1523/JNEUROSCI.1436-24.2025, doi:10.1038/s41562-025-02252-z, arXiv:2609.27729, doi:10.1126/sciadv.adw1464, arXiv:2605.13904
* **가능한 데이터셋:** Horikawa 2020(정서 영상 학습), NSD(정지 이미지 학습, amygdala aseg), Mind captioning(반복으로 encoder 신뢰도 확인)
* **예상되는 반론.** (a) TRIBE v2 feature visualization은 실제 얼굴의 약 4배 예측 FFA를 내는 adversarial super-stimulus를 만든다(arXiv:2605.13904). 선호 자극은 encoder의 성질이지 뇌의 성질이 아니다. 동의하며, 그래서 2단계를 "제약 하 존재 여부"로만 해석한다. (b) EmoNet feature를 쓰면 Horikawa에서 라벨 누수다. Horikawa encoder는 EmoNet 없이 학습한다.
* **태그:** label-provenance = Horikawa [Human-norm], NSD [AI-est] 또는 nsdmeadows, 신규 R2. evidence-level = R1 + R2. insilico-vs-observed = in silico(실측은 학습 자료에만). signal-feasibility = amygdala 필수. G1 = 필요(보유).

### GC-P8 → brain-inspired: 정서 범주는 같고 행동 경향만 다른 자극을 편집으로 만들어 Axis V 경쟁 검정

* **제안 내용.** 너희 P-2와 Chain 2(정서 범주 모델이 설명하는 transmodal 분산 중 얼마가 행동 경향 모델로 대체되는가), 4절 3번(장면 affordance와 공포)을 우리 쪽 편집으로 검증하거나 확장할 수 있다. 위협 대상(예: 다가오는 동물)은 고정하고 회피 affordance(출구 유무, 거리, 장애물)만 바꾼 편집 자극을 만든다. (a) 데이터셋 학습 encoder의 PPA, OPA와 amygdala 예측이 affordance 편집에 따라 어떻게 바뀌는지(R1), (b) 인간 평정으로 "위협", "공포", "도망 가능성"을 따로 받는다(R2). 정서 범주 평정은 같은데 행동 경향 평정만 바뀌는 편집 쌍을 얻으면, 너희 Chain 2의 경쟁 검정을 자연 자극의 공선성 없이 encoder 수준에서 할 수 있다.
* **관련 Axis:** V, L, E, B
* **근거 논문 ID:** doi:10.1073/pnas.2414005122, doi:10.1016/j.isci.2020.101060, arXiv:2410.11758, arXiv:2608.06231, doi:10.1016/j.tics.2019.12.016
* **가능한 데이터셋:** NSD(장면 이미지, PPA/OPA encoder), Horikawa 프레임, Emo-FilM Motivation 10항목(관찰 비교용)
* **예상되는 반론.** (a) affordance 편집은 장면 layout을 바꾸므로 PPA, OPA 예측 변화가 자명하다. layout 변화량을 맞춘 비-affordance 대조 편집(출구가 아닌 창문 추가 등)을 둔다. (b) 정지 이미지의 affordance와 영상 속 방어 계산은 다르다. 정지 이미지 단계는 예비 검사로 한정한다. (c) Mobbs 2020(doi:10.1016/j.tics.2019.12.016)은 DB에서 본문 미열람 상태라 방어 계산 세부 근거로는 약하다.
* **태그:** label-provenance = 신규 R2(별도 평정자, 정서와 행동 경향 문항 분리) + [Human-norm](Emo-FilM Motivation). evidence-level = R1 + R2. insilico-vs-observed = in silico + 관찰(Emo-FilM 비교). G1 = 필요(보유).

### GC-P9 → emotion-theory: privileged access 검정(C4)과 내 CH5를 통합하고, HOT 관찰 검정(C3)의 전제를 편집으로 먼저 확인

* **제안 내용.** (a) 너희 C4(본인 보고가 peer 합의, AI 추정, 시청각-의미 feature가 설명하지 못하는 본인 뇌 고유 분산을 설명하는가)는 내 CH5(자극 기대 반응에서 벗어난 개인 뇌 편차가 본인 보고 편차를 예측하는가), encoding-foundation Chain 3, vision-decoding R5, llm-semantics Chain 5와 같은 골격이다. 다섯 제안을 하나로 묶고, "자극 기대 반응"을 세 가지(TRIBE v2 피질 예측, leave-one-out 집단 평균, MLLM 평균 관찰자 예측)로 정의해 결론이 정의에 따라 바뀌는지를 1차 결과로 삼자. (b) 너희 C3(1차 내용 통제 후 남는 보고 정서의 위치)는 관찰 통제다. 그 전에 "1차 내용(장면 의미)을 고정하고도 보고 정서가 바뀌는 자극이 존재하는가"를 우리 의미 고정 편집 + R2 평정으로 확인할 수 있다. 의미 고정 편집이 보고 정서를 거의 바꾸지 못하면, C3가 찾는 "내용 통제 후 남는 정서 신호"는 이 자극 세트에서 자극 쪽 변동으로 분리하기 어렵다는 사전 경고가 된다.
* **관련 Axis:** A(Introspective Access Sub-axis), U, O, L, P
* **근거 논문 ID:** doi:10.1073/pnas.1619316114, arXiv:2410.13787, doi:10.1126/sciadv.abf7129, arXiv:2605.04326, arXiv:2408.13718
* **가능한 데이터셋:** Spacetop alignvideo([Self], 약 51% 결측), Emo-FilM 사후 클립 평정(부분), Horikawa(편집 + R2)
* **예상되는 반론.** (a) 개인 뇌 편차와 보고 편차의 상관은 각성 상태, 주의, 머리 움직임 같은 무측정 교란을 남긴다(R0). (b) Spacetop 평정 구간이 영상 끝 HRF와 겹친다(Stage 1 4.3절). 평정 구간 이전 TR만 쓴다. (c) 편집 + R2는 별도 평정자의 보고라 privileged access 자체를 검정하지 않는다. (b)번 제안은 C3의 전제 점검으로만 쓴다.
* **태그:** label-provenance = [Self] vs [Human-norm] vs [AI-est] 비교가 핵심. evidence-level = R0(Spacetop) + R2(편집 평정). insilico-vs-observed = 혼합(기대 반응 정의 하나가 in silico). G1 = 필요(보유).

---

## 3. 받은 제안에 대한 응답

(Coordinator가 전달한 뒤 추가)

---

## 4. Coordinator 질문 8개에 대한 답 (생성, counterfactual, 인과 추론 관점)

**Q1. Vision Decoding 연구자가 Emotion Neuroscientist의 문제를 해결할 수 있는가?**
부분적으로, 그리고 도구 쪽에서. 현행 재구성 파이프라인은 입력이 시각 영역(nsdgeneral)이고 생성 prior가 정서 중립적인 COCO 분포라 정서를 구조적으로 잃는다(vision-decoding 0.2절, arXiv:2403.11207). 재구성 이미지의 정서는 정의상 이미지 속성이라 portrayed 또는 normative 정서에 관한 정보이고 참가자 경험의 증거가 아니다. 반면 decoding 쪽 도구는 정서 연구의 가설 생성기로 쓸 만하다. 생성 출력에서 뇌 증거 몫과 prior 몫을 나누는 분해(doi:10.1126/sciadv.adw1464 Discussion), brain-guided 선호 자극 합성(arXiv:2512.00557)이 그 예다. 다만 "더 선명한 생성 이미지가 더 강한 신경 충실도의 증거는 아니다"(arXiv:2609.27729 Discussion 5.1)라는 원칙 아래에서 쓰고, 결론은 R1, 인간 평정을 붙이면 R2까지다.

**Q2. LLM의 representation이나 reasoning 능력을 neural emotion representation 분석에 활용할 수 있는가?**
세 가지 용도로 가능하다. (a) 측정 도구: 정서 배제 캡션 embedding을 편집 자극의 의미 불변성 척도로 쓴다. 단 Mind captioning 인간 중립 캡션으로 먼저 검증한다(doi:10.1126/sciadv.adw1464). (b) 관점별 회귀자: LLM 정서 판단은 평균 관찰자에 가깝다(arXiv:2408.13718). 귀속(L2) 회귀자로는 쓸 수 있지만 경험(L3)의 대리로 쓰면 안 된다(llm-semantics 0절). (c) 모델 내부 개입: appraisal 방향 조작(arXiv:2502.05489)이나 interchange intervention(arXiv:2106.02997)은 "어떤 모델 정보가 뇌 예측에 필요한가"에 대한 모델 쪽 인과(R1)만 준다. 뇌의 인과가 아니다.

**Q3. Generative AI로 emotion과 visual semantics를 분리해 검증할 수 있는가?**
조건부로 가능하며, 분리 기준을 연구자가 편집 가족으로 정의해야 한다. 현행 정서 편집기는 정서를 주로 내용을 바꿔서 유발하고(arXiv:2405.12661), 그 hidden state는 정서 관련 ROI보다 시각 ROI 예측과 더 맞는다(arXiv:2610.13558). 분위기와 의미 단서를 분리하는 생성기가 나왔지만(arXiv:2608.06231) 표정과 서사는 다루지 않는다. 분리 검증에 필요한 최소 조건은 다섯이다: (1) 편집 가족 사전 명시(augmentation 선택이 content를 정의한다는 arXiv:2106.04619의 경고), (2) 인간 manipulation check(R2, PPI 보정 가능), (3) 인간 판단 변동 기준의 의미 불변성 측정, (4) null-edit 대조, (5) 속성별 AI다움 점검(doi:10.1016/j.neuroimage.2019.116216). 이 조건을 갖추어도 결론은 encoder(R1)와 행동(R2) 수준이다. 뇌 수준 분리는 편집 자극을 새 fMRI로 측정하는 R3가 필요하고, 그 경우도 "자극 속성 → BOLD"의 인과이지 "영역 → 경험"의 인과(R4)는 아니다.

**Q4. Emotion Dynamics를 dynamical systems나 state-space learning의 문제로 재정의할 수 있는가?**
재정의는 가능하지만, 관찰 데이터만으로는 동역학 모형의 핵심 모수(이월, 관성)가 HRF 잔여, 순서 효과와 식별되지 않는 경우가 많다. Horikawa는 5명이 같은 자극 순서를 봐서 신경 이월과 순서 효과가 설계상 분리되지 않는다(multimodal-dynamics Chain 1, 내 Round 1 0절). 내 쪽 기여는 시간 counterfactual이다. 긴 문맥을 받는 encoder(TRIBE v2)에 장면 순서를 바꾸거나 음악을 지운 판본을 넣으면 "다른 순서였다면 예측 반응이 얼마나 달랐는가"를 R1로 추정할 수 있다. 이는 이월 크기의 모델 기반 사전 예측이며, 관찰 데이터의 이월 추정치와 비교할 기준선이 된다. Rothermel 2026은 정적 surrogate에서 동역학적 제어로 가려면 신경 동역학과 입력-반응 인과 사상이 필요하다고 썼다(arXiv:2609.27729 Discussion 마지막 절).

**Q5. Brain Foundation Model의 latent representation에서 감정 관련 구조를 찾을 수 있는가?**
찾을 수 있지만 그것은 모델의 구조다. 자극 구동 encoder(TRIBE v2)에서는 interchange intervention으로 정서 정렬 latent가 정서 관련 parcel 예측을 매개하는지(R1-모델) 볼 수 있고, simulation-based inference로 합성 뇌에서 valence, arousal이 회복된다는 결과도 있다(arXiv:2604.23865, 합성 반응만 사용). 그러나 공개 TRIBE v2는 피질 평균 피험자만 예측하고(encoding-foundation 0절), 같은 자극 비교 전에는 정서 구조 보존 정도를 모른다(EmoMind의 RSA 손실은 자극 불일치로 섞임). 뇌 입력 foundation model(CortexMAE 등)에는 누수 통제된 정서 benchmark가 없다(encoding-foundation U5). 그래서 GC-P1의 관문 연구가 먼저다.

**Q6. Music, Video, Image의 공통 정서 특징과 modality-specific 특징을 뇌 수준에서 구분할 수 있는가?**
관찰 데이터의 데이터셋 간 비교(Horikawa 무음 vs Emo-FilM 소리)는 양식뿐 아니라 자극 길이, 라벨 형식, 피험자가 함께 달라 양식 효과를 분리하지 못한다(Stage 1 3절). 같은 데이터셋 안의 stem 제거와 modality dropout(R1)은 양식 효과를 분리하지만 surrogate 안의 결론이다. 실제 판본 조작(Lettieri 2024, doi:10.1126/sciadv.adk6840)을 관찰 기준으로 삼아 surrogate를 먼저 검증하는 순서를 제안한다(GC-P4). 뇌 수준의 확정에는 같은 참가자에게 판본을 바꿔 보여 주는 R3가 필요하다.

**Q7. Neuroscience에서 관찰되는 정서 관련 계산을 AI architecture의 구조적 제약으로 구현할 수 있는가?**
주 담당(brain-inspired) 영역이라 내 관점의 한 가지만 적는다. 생성 모델 쪽에서 이미 "뇌 예측을 생성의 제약으로 쓰는" 시도가 나왔다(ROI-ReFT, arXiv:2610.13558: 예측 정서 ROI 변화를 편집 방향으로). 이는 구조 제약이 아니라 학습 신호이며, 같은 surrogate를 교사와 평가에 함께 써서 순환이다. 반대로 분위기와 의미 단서를 분리한 생성기 구조(arXiv:2608.06231)는 정서의 이중 경로 가설(저수준 생태 통계 경로 vs 의미 경로, doi:10.1038/s41467-024-53668-6)과 형식이 같다. 이 생성기의 두 operator가 각각 다른 뇌 영역 encoder 예측(초기 시각 vs transmodal)을 움직이는지 보면, AI 구조의 분해가 뇌의 경로 분해와 대응하는지 R1에서 시험할 수 있다.

**Q8. 정서 라벨이 없는 NSD 같은 데이터도 다른 데이터셋과의 representation alignment로 의미 있게 활용할 수 있는가?**
가능하며, 내 관점에서 NSD의 가장 큰 가치는 encoder 학습장이다. 7T, 3회 반복, 1인당 약 10,000장, aseg amygdala로 학습한 encoder는 brain-guided 생성과 counterfactual 평가의 기반이 된다(arXiv:2512.00557, doi:10.1038/s41467-024-53668-6가 NSD로 학습). 정서 의미는 다른 데이터셋이나 새 평정에서 와야 한다. NSD 이미지의 AI 추정 정서는 소량 무작위 인간 평정으로 PPI 보정할 수 있다(doi:10.1126/science.adi6000). 위험은 세 가지다. NSD 정서가는 대체로 중립이라 정서 범위가 좁고(Stage 1 4.4절), COCO는 대다수 VLM과 생성 모델 학습 분포 안이라 오염되어 있으며, amygdala 반응은 반복과 기억 과제로 비정상적이다(systems-neuro Chain 4).

---

## 5. Axis 결정과 필수 태그에 대한 의견

* **U, V, W 독립 Axis 채택:** 동의한다. U(Label Provenance)는 내 Round 1 U5(평정 주체가 허용하는 인과 구조)의 상위 개념이며, 인과 질문의 식별 가능성이 라벨 주체에 따라 갈린다는 점에서 P와 짝을 이룬다. V는 GC-P8처럼 편집으로 정서 범주와 분리해 조작할 수 있어 L과 조합하기 좋다. W는 Mind captioning 회상 데이터로 조건이 충족되었다.
* **X를 R의 Sub-axis, Y를 A의 Sub-axis로 둔 결정:** 이견 없다.
* **evidence-level 태그 채택에 대한 보완 제안 두 가지.**
  1. **R1을 둘로 나누자.** R1-s(자극 편집 → encoder 예측 변화)와 R1-m(모델 내부 latent 개입, 예: interchange intervention, appraisal steering). R1-s는 "encoder가 이 자극 속성에 민감한가"를 말하고 R3 설계로 이어진다. R1-m은 모델 자체에 대한 결론이며 R3로 바로 이어지지 않는다. 두 수준을 한 이름으로 묶으면 R1-m 결과가 뇌 자극 실험의 근거처럼 읽힐 위험이 있다.
  2. **데이터셋 내부의 실제 조작에는 "R3-internal" 표시를 쓰자.** Spacetop 통증 과제의 무작위 기만 cue처럼 이미 수집된 데이터 안에 실험 조작이 있으면, 그 조작 변수에 한해 R3 수준 결론이 가능하다(내 Round 1 0절). 이것을 R0로 표기하면 근거 수준을 과소 평가한다.
* **minimum-validation에 편집 타당성 항목 추가 제안:** Axis L을 쓰는 모든 질문에 (a) 편집 가족 사전 명시, (b) 인간 manipulation check 또는 PPI 보정 계획, (c) 의미 불변성 측정, (d) null-edit 대조, (e) 속성별 AI다움 점검을 붙이자. 기존 adversarial-reviewer 7항목과 겹치지 않는 L 전용 항목이다.

---

## 6. 검증 상태와 미확인 사항

**검증된 것.**
* 새로 추가한 6편 모두 식별자 경로로 존재 확인(arXiv 4편은 arxiv.org abs 페이지 메타데이터, Crossref와 PubMed 2편).
* ROI-ReFT(arXiv:2610.13558)와 EmoWorld(arXiv:2608.06231)는 arXiv HTML 본문에서 방법, 결과, 결론(EmoWorld는 Limitations 절과 인간 지각 검증 부록)을 직접 읽었다. ROI-ReFT에는 별도 Limitations 절이 없어 한계는 본 에이전트 판단으로 적었다.
* 다른 에이전트 결과의 인용(예: TRIBE v2 공개 checkpoint의 피질 전용, Mind captioning 사양, Lettieri 2024 결과)은 각 에이전트 round1.md의 기록에 기댔다. 원문을 내가 다시 열지 않은 항목은 출처 에이전트를 함께 적었다.

**미확인.**
* Mind captioning 보유 판본의 실제 파일(캡션, 반복 클립, 회상 과제)과 Horikawa 2020 코호트와의 피험자 중복.
* TRIBE v2 공개 checkpoint의 출력 공간은 encoding-foundation 기록에 의존한다(huggingface.co 접근 불가).
* Emo-FilM 영화별 CC 조항(NoDerivatives 여부). 편집 판본을 외부 평정자에게 보여 주는 R2의 전제다.
* arXiv:2509.21381, arXiv:2609.02616, doi:10.1016/j.neuroimage.2019.116216, doi:10.1038/nn1057은 초록만 읽었다.
* 이번 재검색은 arxiv.org 웹 검색(전 필드 AND 검색이라 결과 0건이 "없음"을 뜻하지 않을 수 있음)과 WebSearch에 기댔다. export.arxiv.org API는 이번 세션 중 시간 초과와 429를 반환했다.
