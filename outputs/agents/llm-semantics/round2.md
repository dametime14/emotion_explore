# Round 2 (Cross-Agent Exchange): llm-semantics

* 에이전트: llm-semantics (주 담당 Axis C. 외부 분야: Social and Collective Behavior, Human-AI Representation Differences). 제안 ID 접두어: LS
* 기준일: 2026-11-12
* 절차: `reference/protocols.md` P2와 Coordinator 위임 메시지의 추가 요구
* 읽은 파일: 다른 10개 에이전트의 `round1.md`(각 파일의 0, 1, 3, 4절 전체와 6절의 관련 chain. vision-decoding 0.1~0.3, R5, R6; emotion-theory 1, C4, C5, 8절; encoding-foundation 0, 1, Chain 2, 3, 7; multimodal-dynamics U3~U8, Chain 2, 3; frontier-ai 0, U1, U2, 4절, CH1~CH3; geometry-info 3, 4절, C7; systems-neuro U6; generative-counterfactual 0절 사다리, U1, U2, CH5; brain-inspired Chain 5; adversarial-reviewer U5, 3절 I1~I3, 7.4절), `outputs/axis_encyclopedia.md` 0절과 2절, `outputs/STAGE_STATUS.md` 사용자 결정 기록, `outputs/literature/literature_db.csv`(인용 ID 확인용)
* 새로 추가한 문헌(식별자 경로 arxiv.org/abs로 확인, 이번 라운드에 export.arxiv.org API가 429로 막혀 abs 페이지 메타데이터로 확인): arXiv:2503.16883, arXiv:2607.10238, arXiv:2607.06875, arXiv:2307.01370, arXiv:2506.20489. `literature.jsonl`에 추가했다(현재 47편, verified 46편).

### 표기
* **label-provenance**는 Deliverable B 0.2절 형식을 따른다. 대상: portrayed / perceived affective quality / felt. 주체: 본인 / peer 합의 / 별도 평정자 규범 / AI 추정.
* **evidence-level**: R0 상관, R1 모델 내 개입, R2 새 행동 평정, R3 새 fMRI 자극 조작, R4 뇌 개입 (generative-counterfactual 0절).
* **insilico-vs-observed**, **G1** 태그도 함께 단다. 사용 가능 데이터셋은 5개다(Horikawa 2020, Emo-FilM, Spacetop, NSD, Mind captioning ds005191).
* "선행 수행" 판단에는 실제 검색 경로를 적는다(부록 A). Stage 2 표본에서 "no"의 25%가 틀렸다는 교훈을 반영해, 확인하지 못한 것은 "검색 범위 내 미발견"으로만 쓴다.

---

## 0. 요약: 교차 독해에서 확인한 수렴과 충돌

1. **같은 설계가 다섯 에이전트에서 독립적으로 나왔다.** "같은 영상을 본 사람들 사이에서 집단 기대 반응에서 벗어난 개인 뇌 반응이 본인 보고의 편차를 예측하는가"(Spacetop alignvideo)를 encoding-foundation(Chain 3), generative-counterfactual(CH5), vision-decoding(R5), emotion-theory(C4), llm-semantics(Round 1 Chain 5)가 각각 제안했다. 조합 단계(P5)에서 중복 후보가 되지 않도록 LS-P2에서 하나의 통합 설계와 역할 분담을 제안한다.
2. **정서 배제 캡션 잔차는 vision-decoding R6과 llm-semantics Chain 1이 같은 질문이다.** Mind captioning 데이터 사용이 승인되어 데이터 조건이 충족되었다. LS-P1에서 두 chain을 합치고 추가 통제(캡션의 정서 누출 감사, 함축된 appraisal의 분리)를 붙인다.
3. **내 Round 1 Chain 2(귀속 vs 경험)는 부분적으로 이미 수행되었다.** emotion-theory가 기록한 Saarimäki et al. (2025, doi:10.1162/imag_a_00517)이 영화 정서의 perceived와 felt 피질 지형을 비교했고, 같은 범주 perceived-felt 공유 분산이 평균 36%라고 보고했다. Round 1에서는 "no"로 적었으므로 "partially"로 정정한다(5절). 남은 부분은 6절에 적었다.
4. **내 Round 1 Chain 6(일본어 vs 영어 정서 의미)은 설계를 바꿔야 한다.** 다국어 LM의 정서 embedding은 영어에 고정되고, GPT-4는 일본어로 물어도 서구 규범으로 답한다(arXiv:2307.01370, Conclusion). 다국어 LLM에 일본어 prompt를 주는 방식은 이 질문을 검정하지 못한다. 일본어 단일언어 모델과 일본어 화자 규범이 필요하다(LS-P6).
5. **Axis 결정은 수용한다.** U의 정의에 "모델 주석자의 관점(관찰자 모드 vs 경험자 모드)"과 "대체 가능성 인증(alt-test)"을 하위 항목으로 넣자는 보완 의견만 남긴다(4절).

---

## 1. 가져온 아이디어

### IM1. Prediction-powered inference와 Alternative Annotator Test로 AI 추정 라벨을 "쓸 수 있는 측정치"로 만들기
* **출처:** adversarial-reviewer (Round 1 U5, 3절 I1, I2). 근거 doi:10.1126/science.adi6000 (Angelopoulos 2023, PPI), arXiv:2501.10970 (Calderon 2025, alt-test), arXiv:2306.04746 (Egami 2023, DSL)
* **가져오는 내용:** 내 Round 1 부록 A의 "AI 추정 라벨 사용 규칙"은 일치도 보고에 그쳤다. adversarial-reviewer의 제안은 이를 두 가지 통계 절차로 바꾼다. (a) alt-test: 평정자별 원자료가 있는 Emo-FilM에서 MLLM이 인간 평정자 한 명을 대체할 수 있는지를 항목별로 검정한다. (b) PPI: 소량의 무작위 인간 gold 표본으로 AI 라벨이 voxel 회귀계수에 주는 편향을 보정한다.
* **내 쪽 확장:** reader-annotator와 experiencer-annotator를 구분한 Ruder et al. (2025, arXiv:2503.16883, Limitations: LLM은 experiencer 역할을 할 수 없음)과 Tak & Gratch (2024, arXiv:2408.13718, Study 2)를 결합하면, alt-test를 "관찰자 모드 prompt"와 "경험자 모드 prompt"로 각각 돌려 **어느 관점에서 대체 가능성이 성립하는지**를 볼 수 있다. Calderon 2025는 인간 불일치가 높은 주관 과제에서 검정 통과가 어렵다고 적었으므로(7 Limitations), Emo-FilM의 낮은 평정자 일치(평균 r 0.38~0.39)에서는 검정력 분석을 먼저 해야 한다.

### IM2. Perceived vs felt 영화 정서의 피질 지형 (내 Chain 2의 선행 연구)
* **출처:** emotion-theory (Round 1 U3), multimodal-dynamics (U5). 근거 doi:10.1162/imag_a_00517 (Saarimäki 2025)
* **가져오는 내용:** perceived와 felt 모두 개인과 자극을 넘어 일반화되었고, felt가 perceived보다 TPJ, 내측/외측 PFC, 시상, 소뇌를 더 동원했으며, 같은 범주의 공유 분산은 평균 36%였다(DB 기록 기준, emotion-theory full_text). 한계는 평정자와 fMRI 참가자가 다르다는 점이다(4.5절).
* **내 쪽 반영:** 내 Chain 2의 질문 "TPJ, dmPFC는 귀속, insula/편도체/vmPFC는 경험을 따르는가"는 이 연구가 TPJ와 PFC에서 오히려 felt가 강하다고 보고했으므로 내 예측과 충돌한다. 예측을 고치지 않고 충돌을 기록한다. 이 결과는 내 0절 틀(L2 귀속 의미 vs L3 경험)의 단순한 영역 분리 예측이 틀릴 수 있음을 보여 준다. 남은 질문은 6절 Chain 2 재정의에 적었다.

### IM3. 관점 결속(perspective binding)과 "정서 vs 상황" 판별 검정
* **출처:** frontier-ai (Round 1 C2, U1, CH1, CH3). 근거 arXiv:2604.07729 (Sofroniew 2026, LLM 정서 표상이 사용자, 가상 인물, Assistant에 같은 기제로 작동하고 지속 상태를 유지하지 않음, 5.2~5.3절), arXiv:2604.13466 (기능적 정서 vs 상황 맥락 판별 제안), arXiv:2609.34742 (VLM 정서 vector가 정서와 무관한 정렬만으로 대응 복원)
* **가져오는 내용:** AI 쪽에서 "같은 정서 방향이 누구의 정서에 활성화되는가"를 재는 방법을 뇌로 옮기면, 내 S1(Attribution-Experience Gap)이 "어느 영역이 인물에 결속된 정서를, 어느 영역이 관점 무관 정서 개념을 표상하는가"라는 측정 가능한 변수가 된다. 또 arXiv:2609.34742의 "정서와 무관한 정렬만으로 정서 대응이 복원된다"는 결과는 내 L1(기술) 기준선이 L2(정서 의미)를 상당 부분 흡수할 수 있다는 AI 쪽 증거다.

### IM4. Supramodal 정서 코드는 언어 채널에 기대는가 (Lettieri 2024의 constructionist 단락)
* **출처:** multimodal-dynamics (Round 1 U3, Chain 3), encoding-foundation (U8, Chain 7). 근거 doi:10.1126/sciadv.adk6840 (Lettieri 2024), doi:10.1111/cogs.13343 (Kumar 2023, Bayesian surprise와 사건 분절)
* **가져오는 내용:** vmPFC의 모달리티 무관 범주 정서 코드가 모든 판본에 공통인 언어 채널(대사)에 기댈 수 있다는 저자 자신의 단서(Discussion constructionist 단락, multimodal-dynamics 기록)는 내 0절 L1/L2 구분을 대사 있는 영화로 넓힐 근거다. Emo-FilM에는 transcript가 없으므로 ASR로 대사를 만들고, 대사의 (a) 어휘 감성, (b) LLM이 추론한 정신 상태 의미를 분리한 feature로 "언어 채널 가설"을 검정할 수 있다(LS-P3).

### IM5. Mind captioning 코호트의 반복 클립과 회상 imagery, 그리고 P/N/X 구분
* **출처:** vision-decoding (Round 1 0.1, 0.3, R2, R6). 근거 doi:10.1126/sciadv.adw1464
* **가져오는 내용:** 72개 테스트 클립을 5회 반복 제시해 noise ceiling을 추정할 수 있고, 같은 클립의 회상 imagery와 vividness 평정이 있다. vision-decoding의 P(portrayed)/N(normative evoked)/X(experienced) 3수준과 L5 "회상에서 해독되는 정서는 정서 지식의 의미 기억일 수 있다"는 논리를 내 L2(귀속된 정서 의미)와 연결하면, **시각 입력이 없는 회상 조건에서 남는 정서 정보가 L2(언어화 가능한 정서 의미)로 얼마나 설명되는지**를 물을 수 있다. 회상 중 정서 정보가 정서 배제 캡션 embedding과 정서 언어 embedding 중 어느 쪽에 더 정렬되는지가 측정치다(LS-P1의 확장).

### IM6. 정서 범주 체계의 정보 병목 효율 (geometry-info가 Stage 3 재논의를 요청)
* **출처:** geometry-info (Round 1 I6, C7, 4절 U1). 근거 doi:10.1073/pnas.1800521115 (Zaslavsky 2018), arXiv:2409.06843
* **가져오는 내용:** 6, 13, 27, 34개 범주 체계를 "참값 논쟁"이 아니라 IB trade-off 모수 차이로 보는 재정식화. 색 이름 연구의 원래 강점은 **언어 간 변이**를 단일 모수로 설명했다는 점인데, C7은 영어 범주 체계만 비교한다. 내 S6(Collective and Cultural Emotion Semantics)과 Jackson 2019(doi:10.1126/science.aaw8160)를 붙이면 언어 간 비교가 가능해진다(LS-P6).

---

## 2. 보내는 제안

### LS-P1 → vision-decoding (참조: encoding-foundation, generative-counterfactual)
* **제안 내용:** 너희 쪽 **R6(정서 배제 인간 캡션을 통제한 뒤 남는 정서 분산)** 을 우리 쪽 **Chain 1(기술 잔차)과 L1/L2 분해**로 하나의 설계로 합쳐 확장할 수 있다. 구체적으로 세 가지를 더한다.
  1. **캡션의 정서 누출 감사:** "정서를 쓰지 말라"는 지시는 내용을 중립으로 만들지 않는다(너희 R6의 해석 범위 단서와 같은 입장). 캡션마다 (a) 명시적 정서 어휘 수(사전 기반), (b) LLM reader 모드로 캡션만 읽고 추정한 정서 [AI 추정, perceived affective quality]를 계산해, 캡션 embedding이 C&K 평정을 얼마나 이미 함축하는지 먼저 보고한다.
  2. **중첩 기준선 셋:** L1a 시각 feature만, L1b + 정서 배제 인간 캡션 embedding, L2 + 같은 캡션을 정서 언어로 재작성한 embedding [AI 추정]. 마지막에 C&K 34/14 [felt, 별도 평정자 규범]을 더해 각 단계의 고유 분산을 영역별로 낸다. 언어로 회복되지 않는 잔차가 어느 영역에 남는지가 결과다.
  3. **두 코호트의 역할 분리:** Mind captioning(6명)의 72개 반복 클립으로 noise ceiling 대비 비율을 내고, Horikawa 2020(5명)으로 같은 지도의 재현을 본다. 회상 imagery 조건(IM5)에서 같은 분해를 반복해 "자극 없는 정서 정보가 언어화 가능한 의미인가"를 묻는다.
* **관련 Axis:** C(S3 Description Residual), B, F, H, U, W
* **근거 논문 ID:** doi:10.1126/sciadv.adw1464 (Materials and Methods "Caption annotation", Discussion 한계 첫 단락), doi:10.1038/s42256-025-01072-0 (Discussion 첫째, 둘째 단락), arXiv:2509.24298 (Discussion 첫째 단락), arXiv:2609.34742, doi:10.1371/journal.pone.0152719 (측정 오차가 고유 분산을 부풀리는 문제, adversarial-reviewer 기록)
* **가능한 데이터셋:** Mind captioning(주), Horikawa 2020(재현), NSD(COCO 캡션은 정서 배제 지시가 없으므로 대조군)
* **예상되는 반론:** (1) 캡션 embedding이 정서를 이미 함축하므로 "정서 고유 분산 0"은 "정서 없음"이 아니라 "정서가 장면 의미로 운반된다"는 뜻이다. 동의하며, 그래서 결과를 "언어화된 장면 의미가 함축하는 정서"와 "그 외"로만 해석한다. (2) 시각, 캡션, 평정의 공선성 때문에 고유 분산 추정이 불안정하다. 내용 지표를 여러 모델로 다중화하고 신뢰도 민감도를 함께 보고한다(adversarial-reviewer 7.4절 3번). (3) 두 코호트 사이 피험자 중복 여부가 미확인이다(vision-decoding 0.1).
* **label-provenance:** 대상 felt, 주체 별도 평정자 규범(C&K). 재작성 캡션과 캡션 기반 정서 추정은 대상 perceived affective quality, 주체 AI 추정
* **evidence-level:** R0 (재작성 embedding 비교는 R1 성격의 모델 쪽 조작이 섞인 R0)
* **insilico-vs-observed:** 관찰 / **G1:** 캡션만 쓰면 불필요, 시각 feature와 MLLM에는 필요(보유)
* **선행 수행:** 검색 범위 내 미발견 (부록 A의 S1, S2). EmoMind(arXiv:2605.16739)는 같은 캡션으로 정서 캡션 생성을 했으나 분산 분할은 하지 않았다.
* **overlap:** EmoViS (affective brain geometry의 sensory-semantic 기원)

### LS-P2 → encoding-foundation (참조: generative-counterfactual, vision-decoding, emotion-theory)
* **제안 내용:** 너희 쪽 **Chain 3(Group 예측 잔차와 개인 정서 경험)** 을 우리 쪽 **"평균 관찰자 기준점" 행동 잔차**로 확장해, 다섯 에이전트가 따로 낸 같은 설계를 하나로 합칠 수 있다. 통합 설계는 두 잔차의 정렬이다.
  * **신경 잔차:** 관찰 BOLD에서 자극 구동 기대 반응을 뺀 값. 기대 반응은 두 가지로 만든다. TRIBE v2 group 예측(in-silico), leave-one-subject-out peer 평균(관찰).
  * **보고 잔차:** 본인 평정에서 기대 보고를 뺀 값. 기대 보고도 두 가지다. leave-one-subject-out peer 평균, 그리고 MLLM의 관찰자 모드 예측 [AI 추정].
  * **우리 쪽 기여:** MLLM 기대 보고는 그 참가자 집단에 의존하지 않는 외부 기준점이라 peer 평균의 순환(같은 표본에서 기준과 편차를 함께 정의) 우려를 줄인다. 다만 MLLM이 peer 평균과 같다면 추가 정보가 없다. 그래서 먼저 alt-test(IM1)로 MLLM이 peer 평균을 대체할 수 있는지 보고, 대체 가능하면 MLLM을 결측 영상 보간과 외부 기준점으로만 쓰고 결론은 peer 기준으로 낸다. 또 MLLM은 평탄화된 평균을 낸다(arXiv:2402.01908)는 점이 오히려 "평균 관찰자"라는 기준점 정의에 맞는다.
  * **역할 분담 제안:** encoding-foundation(신경 기대 반응과 잔차, ceiling), generative-counterfactual(결론 수준 R0 표기와 무측정 교란 처리), vision-decoding(공유 latent와 개인 잔차의 분해), emotion-theory(본인 보고의 privileged access 해석과 신뢰도 보정), llm-semantics(보고 기대치와 라벨 출처 관리).
* **관련 Axis:** O, U, H, A(Introspective Access Sub-axis), C(S1)
* **근거 논문 ID:** arXiv:2605.04326, arXiv:2607.01400, doi:10.1126/sciadv.abf7129 (Discussion 5단락), arXiv:2408.13718 (Study 2), arXiv:2402.01908 (Discussion), arXiv:2501.10970
* **가능한 데이터셋:** Spacetop alignvideo(주), Emo-FilM 사후 클립 평정(보조, 부분)
* **예상되는 반론:** (1) alignvideo 평정 약 51% 결측, 클릭 저장 구조라 무작위 결측이 아닐 수 있다. 결측 기제를 먼저 확인한다. (2) 49개 영상의 작은 독립 표본. (3) 평정 구간과 영상 끝 HRF 겹침(Stage 1). (4) 보고 편차가 정서가 아니라 몰입도(engaged)나 주의 차이에서 올 수 있다(generative-counterfactual CH5의 경쟁 설명). (5) MLLM에 소리 있는 영상을 넣을 때 오디오 처리 능력이 모델마다 다르다.
* **label-provenance:** 대상 felt, 주체 본인(보고 잔차의 기준), peer 합의, AI 추정(기대 보고)
* **evidence-level:** R0 / **insilico-vs-observed:** 혼합(TRIBE 기대 반응은 in-silico) / **G1:** 필요(보유)
* **선행 수행:** partially (doi:10.1126/sciadv.abf7129가 vmPFC 개인 특이 상태와 별도 표본 평정을 연결. 자극 구동 기대 반응과 MLLM 기대 보고를 함께 쓴 두 잔차 정렬은 검색 범위 내 미발견, 부록 A의 S5)
* **overlap:** 없음 (EmoBrain의 cross-subject decoding과는 목표가 반대 방향)

### LS-P3 → multimodal-dynamics
* **제안 내용:** 너희 쪽 **Chain 3(소리가 만드는 정서)의 (b) "vmPFC 정서 decoding은 대사 언어 feature를 빼도 남는가"** 를 우리 쪽 **대사 의미의 2층 분해(L1 어휘 내용 vs L2 추론된 정신 상태 의미)** 로 정밀하게 만들 수 있다. 대사 feature를 한 덩어리로 빼면 "언어 채널"이 어휘 감성인지, 인물의 의도와 믿음 추론인지 구분되지 않는다. ASR 전사 [AI 생성 전사]에서 (a) 어휘 감성과 문장 embedding, (b) 공개 LLM의 hidden state에서 appraisal 방향(arXiv:2502.05489)과 belief-tracking 신호(arXiv:2309.01660)를 각각 뽑아 따로 제거한다. 또 너희 Chain 2(다중모달 예측 surprise와 정서 사건 경계)에 우리 S7의 **belief-inconsistent surprise**(LLM의 서사 예측 분포에서 인물 운명에 대한 믿음이 뒤집히는 순간, Antony 2021의 구분을 서사로 이전)를 surprise 유형 하나로 추가할 수 있다.
* **관련 Axis:** M, C(S7), D, E
* **근거 논문 ID:** doi:10.1126/sciadv.adk6840 (Discussion constructionist 단락), doi:10.1111/cogs.13343 (Discussion 4.2), doi:10.1016/j.neuron.2020.10.029, arXiv:2502.05489, arXiv:2309.01660
* **가능한 데이터셋:** Emo-FilM(주, 대사 있음, transcript 없음), Spacetop narratives(텍스트판으로 ASR 오류 없는 기준), Horikawa(무음 대조)
* **예상되는 반론:** (1) ASR 오류와 화자 분리 실패. Spacetop narratives 텍스트판으로 같은 분석을 먼저 해 상한을 본다. (2) Emo-FilM 대사가 영어로 보이는지는 Stage 1 기준 확인 필요. (3) 영화 14편이라 영화 수준 confound. (4) LLM hidden state의 appraisal 방향이 선형 표상 가정에 의존(arXiv:2502.05489 Limitations).
* **label-provenance:** 대상 felt(Emo-FilM 평정), 주체 별도 평정자 규범. LLM 유래 feature는 대상 portrayed(인물 정신 상태), 주체 AI 추정
* **evidence-level:** R0 / **insilico-vs-observed:** 관찰 / **G1:** 필요(보유, Emo-FilM 판본 일치 여부 미확인)
* **선행 수행:** partially (너희 Chain 3이 기록한 arXiv:2410.17300, arXiv:2509.21381. 대사 의미를 어휘와 정신 상태 추론으로 나눈 fMRI 분해는 검색 범위 내 미발견)
* **overlap:** Emo-FilM 연구 (사전학습 멀티모달 encoding으로 정서 맥락 기여 분석)

### LS-P4 → frontier-ai
* **제안 내용:** 너희 쪽 **CH3(정서 신경 표상의 국소성, 지속성, 관점 결속)와 C2(functional emotions의 인물 무차별성)** 를 우리 쪽 **관점 조건부 MLLM 주석과 Spacetop의 관점별 과제**로 검증할 수 있다. 순서는 모델 먼저, 뇌 나중이다.
  1. **모델 단계(R1):** 공개 VLM에 같은 영상을 (a) 장면 기술, (b) 특정 인물의 정서 판단, (c) 시청자로서 느낄 정서 판단 지시로 넣고, arXiv:2609.34742 방식의 정서 vector 투영이 세 조건에서 같은 방향을 쓰는지 본다. 같다면 모델에는 관점 결속이 없다(arXiv:2604.07729의 주장과 일치).
  2. **뇌 단계(R0):** Spacetop 같은 참가자의 alignvideo(본인 경험 [felt, 본인]), shortvideo(인물 mentalizing [portrayed, 본인 판단]), faces(표정 지각 [perceived, 본인])에서 정서 관련 영역의 반응 방향이 공유되는지 본다. 모델에서는 공유되는데 뇌에서는 분리된다면, 그 차이가 "AI 정서 표상과 뇌 정서 표상의 구조적 차이"의 구체적 측정치가 된다.
* **관련 Axis:** R(Model-internal Emotion Representations Sub-axis), C(S1), U, E
* **근거 논문 ID:** arXiv:2604.07729 (5.2~5.3절), arXiv:2609.34742, arXiv:2604.13466, arXiv:2408.13718, doi:10.1523/JNEUROSCI.1676-14.2014 (MPFC에서 지각과 추론 정서의 공통 valence 코드), doi:10.1162/imag_a_00517
* **가능한 데이터셋:** Spacetop(주), Emo-FilM(인물 정서 [AI 추정] vs 관객 경험 [규범] 비교)
* **예상되는 반론:** (1) Spacetop 세 과제는 자극 종류가 달라(긴 영상, 짧은 영상, 얼굴) 방향 공유 여부가 자극 차이와 섞인다. 과제 간 공통 feature를 nuisance로 넣고 과제 내 split-half 신뢰도를 기준선으로 쓴다. (2) LLM 정서 vector 연구는 텍스트 중심이며 video MLLM 확장은 미래 과제로 남아 있다(arXiv:2609.34742 Appendix G.2, frontier-ai 기록). (3) 모델 내부 표상을 주관 경험으로 해석하지 않는다는 단서(Axis R Sub-axis 정의)를 유지한다.
* **label-provenance:** felt/본인(alignvideo), portrayed/본인 판단(shortvideo), perceived/본인(faces), 모델 쪽은 AI 추정
* **evidence-level:** 모델 단계 R1, 뇌 단계 R0 / **insilico-vs-observed:** 혼합 / **G1:** 필요(보유)
* **선행 수행:** 검색 범위 내 미발견 (부록 A의 S3). 뇌 쪽 귀속-경험 비교 자체는 partially(doi:10.1162/imag_a_00517, doi:10.1523/JNEUROSCI.1676-14.2014)
* **overlap:** 없음

### LS-P5 → adversarial-reviewer (참조: emotion-theory)
* **제안 내용:** 너희 쪽 **I2(MLLM 정서 평정자의 대체 가능성 검정, Emo-FilM)** 를 우리 쪽 **관점 조작과 reader/experiencer 구분**으로 확장할 수 있다. 같은 MLLM을 "관찰자로서 화면 속 상황을 판단"과 "시청자로서 느낄 정서를 보고" 두 모드로 돌려 50개 항목 각각에 alt-test를 적용한다. 예측(Tak & Gratch 2024, Ruder 2025에서 유도): Appraisal 성분은 관찰자 모드에서 대체 가능성이 높고, Physiology와 Motor expression 성분은 어느 모드에서도 대체되지 않는다(내 Round 1 U1 "정서의 Molyneux 문제"). 이 결과는 Axis U에 "성분별 대체 가능성 지도"로 들어가고, 이후 모든 AI 라벨 사용 제안의 사전 조건표가 된다. 대체되지 않는 성분에 대해서는 내 Round 1 Chain 4(인간-MLLM 잔차가 fMRI 참가자 생리와 insula를 예측하는가)를 이어서 돌린다.
* **관련 Axis:** U, Q, A, C
* **근거 논문 ID:** arXiv:2501.10970 (7 Limitations: 주관 과제와 높은 불일치에서의 한계), arXiv:2503.16883 (Limitations), arXiv:2408.13718, doi:10.1038/s41598-025-14961-6 (신체 기반 정서 실패, Discussion 후반), doi:10.1038/s41562-025-02203-8 (감각운동 차원 불일치), arXiv:2502.04379 (시간 연속 주석 실패)
* **가능한 데이터셋:** Emo-FilM(유일하게 평정자별 1 Hz 원자료가 있음)
* **예상되는 반론:** (1) 평정자 내 z-score 평정이라 절대 수준 비교 불가. alt-test는 순위나 상관 기반 지표로 한다. (2) 항목x영화당 평정자 3~4명이라 leave-one-rater-out 표본이 작다. (3) 평정자는 같은 영화를 최대 6번 봤다(Stage 1). MLLM은 한 번 "본다". 반복 시청 효과가 인간 쪽에만 있다. (4) 시간 해상도별로 결과가 다를 수 있어 1 s, 5 s, 장면 단위를 따로 보고한다(내 Round 1 I7). (5) 검정력이 부족하면 "대체 가능성 판단 불가"로 기록한다.
* **label-provenance:** felt, 별도 평정자 규범(인간 기준). MLLM은 AI 추정, 관점 모드 표기
* **evidence-level:** R0 (측정 타당도 검정, 뇌 결론 없음) / **insilico-vs-observed:** 해당 없음(행동 측정) / **G1:** 필요(보유)
* **선행 수행:** 검색 범위 내 미발견 (부록 A의 S4: appraisal 텍스트 주석의 reader-annotator 비교는 arXiv:2503.16883이 수행, 연속 영화 평정 성분별 alt-test는 미발견)
* **overlap:** 없음

### LS-P6 → geometry-info
* **제안 내용:** 너희 쪽 **C7(정서 범주 체계의 정보 병목 효율)** 을 우리 쪽 **S6(Collective and Cultural Emotion Semantics)** 으로 언어 간 비교로 확장할 수 있다. 영어 범주 체계끼리만 비교하면 IB의 핵심 강점(언어 간 변이를 한 모수로 설명)을 쓰지 못한다. 일본어 정서 어휘 분할과 영어 분할을 같은 "공유 신경 정서 공간" 위의 IB 평면에 놓고, Japanese 화자 뇌(Mind captioning 6명은 일본어 모국어 화자. Horikawa 2020 참가자 언어는 미확인)에서 어느 분할이 효율 경계에 더 가까운지 본다. 분할을 얻는 방법은 다국어 LLM이 아니라 일본어 화자 규범이어야 한다. 다국어 LM의 정서 embedding은 영어에 고정되고 GPT-4는 일본어로 물어도 서구 규범으로 답하기 때문이다(arXiv:2307.01370 Conclusion). 일본어 80범주 평정(Koide-Majima 2020, Asanuma 2025가 사용)은 우리 데이터셋 밖이므로, 최소한 Mind captioning 72개 테스트 클립에 일본어 정서 범주 평정을 새로 모으는 R2 단계가 필요하다.
* **관련 Axis:** K(IB Sub-axis), C(S6), O, U
* **근거 논문 ID:** doi:10.1073/pnas.1800521115, doi:10.1126/science.aaw8160 (colexification의 언어 계통 변이와 보편 valence/활성화 축), arXiv:2307.01370, arXiv:2506.20489 (언어 무관 공유 개념 공간, 귀무가설 쪽 근거), doi:10.1038/s41598-025-14961-6
* **가능한 데이터셋:** Mind captioning(주, 일본어 화자 확인됨), Horikawa 2020(참가자 언어 확인 후)
* **예상되는 반론:** (1) C&K 비디오는 영어 34범주를 기준으로 큐레이션되어 자극 분포 p(m)이 영어 체계에 유리하다(geometry-info C7의 주의와 같음). (2) 6명 표본으로는 언어 효과와 개인차를 분리하기 어렵다. 효과 크기 추정 중심으로 쓴다. (3) 신규 평정 수집(R2)에 IRB가 필요하다. (4) 공유 신경 공간에 시각-의미 성분이 섞여 있으면 IB 평가가 장면 범주 체계를 평가하게 된다. LS-P1의 기술 잔차 공간을 쓰는 것이 대안이다.
* **label-provenance:** felt, 별도 평정자 규범(미국 C&K)과 새 일본어 화자 규범(수집 필요). LLM은 쓰지 않거나 AI 추정 대조군으로만
* **evidence-level:** R0, 신규 평정이 들어가면 R2 / **insilico-vs-observed:** 관찰 / **G1:** 신규 평정에 필요(보유)
* **선행 수행:** 검색 범위 내 미발견 (부록 A의 S6. 정서 어휘의 IB 적용은 geometry-info도 미발견으로 기록)
* **overlap:** EmoViS (Horikawa 정서 기하, 약함)

### LS-P7 → systems-neuro (참조: encoding-foundation)
* **제안 내용:** 너희 쪽 **U2와 Chain 1(network arousal 판독에서 자율신경 성분 분리)** 그리고 encoding-foundation **Chain 2(Limbic 맹점의 분해)** 를 우리 쪽 **"언어화 가능한 정서" 기준선**으로 보강할 수 있다. 두 chain은 자극 구동 encoder(TRIBE v2)나 생리로 설명되지 않는 분산을 찾는다. 여기에 "MLLM이 같은 50항목을 얼마나 맞히는가"를 항목별, 시점별로 더하면, 인간 규범 평정 중 언어와 시각으로 추론 가능한 부분(L2)과 그렇지 않은 부분의 시계열을 만들 수 있다. 예측: 인간-MLLM 잔차는 평정자 split 간 잔차(라벨 잡음 귀무분포)보다 fMRI 참가자의 심박, EDA와 insula, 뇌간 BOLD를 더 잘 예측한다. 반대로 잔차가 귀무분포 수준이면 "MLLM이 놓치는 정서는 라벨 잡음"이라는 결론이 되고, 이는 encoding-foundation Chain 2의 "feature 결핍" 가설에 불리한 증거가 된다.
* **관련 Axis:** E, H, C(S3), U, A
* **근거 논문 ID:** doi:10.1162/imag.a.1300 (Gemini 특징이 insula를 거의 설명 못함, Conclusions), arXiv:2605.16739 (합성 뇌에서 클립 간 정서 구조 손실), doi:10.1371/journal.pcbi.1012994 (arousal 판독과 자율신경 문제), arXiv:2605.04326 (피질하 점수 저하)
* **가능한 데이터셋:** Emo-FilM(참가자 PPG, 호흡, EDA 1000 Hz, 평정자별 1 Hz 원자료)
* **예상되는 반론:** (1) 평정자와 fMRI 참가자가 다른 사람이다(Stage 1). 잔차는 "규범 평정 중 언어화되지 않는 성분"이지 참가자 개인 경험이 아니다. (2) 생리 회귀가 BOLD 생리 잡음 제거와 혼동된다. RETROICOR 적용 여부를 조건으로 둔다(encoding-foundation Chain 2의 주의). (3) 피질하 신호 품질(signal-feasibility 태그, systems-neuro 제안)을 먼저 점검한다. (4) MLLM의 1 Hz 시간 타당도가 확인되지 않은 척도는 쓰지 않는다(LS-P5의 결과에 의존).
* **label-provenance:** felt, 별도 평정자 규범(인간). MLLM은 AI 추정. 생리는 fMRI 참가자 본인 측정
* **evidence-level:** R0 / **insilico-vs-observed:** 관찰(MLLM 예측은 feature로만 사용) / **G1:** 필요(보유)
* **선행 수행:** 검색 범위 내 미발견 (부록 A의 S7)
* **overlap:** Emo-FilM 연구 (부분: 같은 데이터, 정서 맥락 기여)

### LS-P8 → brain-inspired
* **제안 내용:** 너희 쪽 **Chain 5 (B) Spacetop narratives의 단기 PE와 장기 기대 불일치 분리**를 우리 쪽 **LLM 서사 모델의 예측 분포**로 계산할 수 있다. 참가자의 "다음 전개 기대" 평정은 clip 단위로만 있으므로, 문장 단위로 (a) LLM이 다음 사건에 거는 확률 분포의 엔트로피(불확실성), (b) 실제 다음 문장의 surprisal(단기 PE), (c) 이야기 초반 상태에서 예측한 결말 분포와 현재 상태 사이의 KL(장기 기대 갱신)을 계산해 너희 RL, active inference 모형의 입력 변수로 쓴다. 이렇게 하면 모형 비교가 평정 해상도(clip)에 묶이지 않는다. 동시에 우리 Chain 3(LLM appraisal 궤적과 ToM 네트워크)의 nuisance로도 쓸 수 있다.
* **관련 Axis:** N, C(S7), D, V
* **근거 논문 ID:** doi:10.1162/neco_a_01341, arXiv:2407.02474, doi:10.1016/j.neuron.2020.10.029, doi:10.1111/cogs.13343, doi:10.3758/s13428-024-02569-z, doi:10.1038/s41467-026-71151-2
* **가능한 데이터셋:** Spacetop narratives(텍스트 4편, 오디오 4편, 본인 good-bad 감정과 기대 평정)
* **예상되는 반론:** (1) LLM의 예측은 참가자의 예측이 아니다(in-silico vs observed). (2) 공개된 유명 이야기라면 LLM이 결말을 학습 중에 봤을 수 있다(사전학습 오염). 이야기 출처를 확인하고, 결말을 모르게 하는 prompt만으로는 오염을 막지 못하므로 결말 예측 정확도 자체를 오염 지표로 기록한다. (3) 이야기 8편이라 이야기 수준 일반화가 약하다.
* **label-provenance:** felt와 기대, 본인(Spacetop narratives 평정). LLM 신호는 AI 추정(계산 변수)
* **evidence-level:** R0 / **insilico-vs-observed:** 혼합 / **G1:** 서사 텍스트 필요(보유)
* **선행 수행:** partially (doi:10.1111/cogs.13343이 LLM surprise와 사건 분절을 연결. 정서 평정과 RL/active inference 모형 비교의 입력으로 쓴 것은 검색 범위 내 미발견)
* **overlap:** 없음

---

## 3. 받은 제안에 대한 응답

(Coordinator가 전달한 뒤 추가)

---

## 4. Axis 결정에 대한 의견

* **U (Label Provenance & Perspective) 채택: 수용.** 보완 의견 두 가지. (1) 하위 항목에 **"모델 주석자의 관점 모드"**(관찰자, 경험자, persona)를 명시한다. 같은 모델도 지시에 따라 portrayed, perceived, felt 중 무엇을 추정하는지 달라지며(arXiv:2408.13718, arXiv:2503.16883), 이 차이를 기록하지 않으면 AI 추정 라벨의 대상이 불명확해진다. (2) **"대체 가능성 인증"**(alt-test, PPI 보정)을 U의 절차 항목으로 둔다(IM1). (3) 새 라벨 출처 후보로 **집단 관객 반응**(소셜 미디어 댓글 분포, arXiv:2607.06875)을 기록해 둔다. 우리 데이터셋에 해당 자료가 있는지는 미확인이라 지금은 후보로만 둔다.
* **X를 R의 Sub-axis로 둔 결정: 수용, 단서 하나.** AI 내부 정서 표상과 뇌 정서 표상을 비교하는 질문(LS-P4)은 R 안에 있어도 되지만, 비교 변수인 **관점 결속**은 R이 아니라 C(S1)와 U에 걸친다. 조합 단계에서 R과 C를 함께 뽑을 수 있도록 Axis C의 S1 설명에 "AI 쪽 대응: Model-internal Emotion Representations"를 교차 표시하기를 제안한다.
* **Y를 A의 Sub-axis로 둔 결정: 수용.** emotion-theory C4와 LS-P2의 "본인 보고의 고유 설명력"이 이 Sub-axis의 데이터 가능 부분이다.
* **Information-theoretic Efficiency of Affective Categories를 K의 Sub-axis로 둔 결정: 수용.** 단 언어 간 비교 방향(LS-P6)은 C(S6)와 교차 표시한다.
* **"Recognition vs Experience" 처리(Axis U + 필수 태그 동시 채택): 수용.** Round 1에서 독립 Axis를 주장했지만, 태그로도 유지하면 모든 질문에서 점검된다는 emotion-theory의 논리가 타당하다. 이견을 철회한다.

---

## 5. Round 1 기록의 정정

| 항목 | Round 1 | 정정 | 근거 |
|---|---|---|---|
| Chain 2 (귀속 vs 경험) 선행 수행 | no | **partially** | doi:10.1162/imag_a_00517 (perceived vs felt 영화 정서 피질 지형, 별도 평정자). 또 TPJ, PFC에서 felt가 더 강하다는 결과가 내 영역 분리 예측과 충돌함을 기록 |
| Chain 6 (일본어 vs 영어 정서 의미) 설계 | 다국어 MLLM에 일본어 prompt | **일본어 단일언어 모델 + 일본어 화자 규범**으로 변경, Mind captioning(일본어 모국어 화자 확인)을 주 데이터로 | arXiv:2307.01370 (Conclusion, Future Research Directions) |
| Chain 1 데이터 조건 | 캡션 접근 미확인 | Mind captioning 사용 승인으로 충족(저장소 내 캡션 포함 여부는 여전히 미확인). vision-decoding R6과 통합(LS-P1) | STAGE_STATUS 사용자 결정 16 |
| Chain 5 | 단독 제안 | 다섯 에이전트 수렴 설계로 통합(LS-P2) | 0절 1번 |
| Melhart 2025(arXiv:2502.04379) FD1 | no | partially (arXiv:2603.18480, Coordinator 수정 반영. 본 에이전트는 해당 논문을 직접 확인하지 않았다) | `literature.jsonl` 갱신 |
| 문헌 추가 | | arXiv:2503.16883, arXiv:2607.10238, arXiv:2607.06875, arXiv:2307.01370, arXiv:2506.20489 | 부록 A |

---

## 6. Round 1 Chain 2의 재정의 (선행 수행 반영)

Saarimäki 2025가 perceived와 felt를 이미 비교했으므로, 남은 질문을 다음 세 가지로 좁힌다.

1. **인물 단위 귀속:** Saarimäki의 perceived는 "영화에서 지각한 정서"로 인물을 구분하지 않는다(DB 기록 기준, 본문의 문항 문구는 본 에이전트 미확인). 같은 장면에 인물이 여럿일 때 **누구의 정서인가**를 MLLM 인물별 주석 [portrayed, AI 추정]으로 나누고, 소규모 인간 인물별 귀속 평정 [portrayed, 별도 평정자, 수집 필요, R2]으로 검증한다.
2. **불일치 구간:** 인물 정서와 관객 경험이 어긋나는 시점(인물은 공포, 관객은 서스펜스나 연민)에 한정해, 어느 영역이 어느 쪽을 따르는지 본다. 평균 공유 분산 36%라는 결과는 대부분의 시간에 두 신호가 공변한다는 뜻이므로, 진단력은 불일치 구간에 있다.
3. **데이터셋 확장:** Emo-FilM(1 Hz 별도 평정자 felt)과 Spacetop(같은 참가자의 felt와 귀속 판단)으로 두 형태의 재현을 본다.

예측 수정: TPJ와 PFC가 felt에서 더 강하다는 선행 결과를 받아들여, "귀속은 TPJ, 경험은 insula/편도체"라는 단순 분리 예측은 철회한다. 대신 "불일치 구간에서 TPJ는 두 신호 모두에 반응하고, insula와 편도체는 경험 쪽에만 반응한다"는 비대칭 예측으로 바꾼다. 반증 조건: 불일치 구간에서 insula와 편도체가 귀속 신호를 경험 신호만큼 따르면 비대칭 예측은 기각된다.

* label-provenance: felt/별도 평정자 규범(Emo-FilM), portrayed/AI 추정 + 별도 평정자(검증용, 수집 필요)
* evidence-level: R0, 검증 평정 수집 시 R2 / G1: 필요(보유) / overlap: Emo-FilM 연구

---

## 7. Coordinator 질문 8개에 대한 답 (llm-semantics 관점)

**Q1. Vision Decoding 연구자가 Emotion Neuroscientist의 문제를 해결할 수 있는가?**
부분적으로 그렇다. 해결하는 것은 "무엇이 기술되는가"의 문제다. Mind captioning은 정서를 배제한 캡션으로 시청과 회상 내용을 문장화했고(doi:10.1126/sciadv.adw1464), 이것이 정서 연구에 없던 L1 기준선(정서 아닌 장면 의미)을 준다. 해결하지 못하는 것은 정서 쪽이다. 현행 재구성 파이프라인은 시각피질 voxel만 입력으로 써서 편도체, 섬엽, vmPFC를 배제하고 정서 중립 prior를 가진다(vision-decoding Round 1 0.2). 정서 캡션 decoding(arXiv:2605.16739)도 정서 벡터는 별도 경로로 붙였다. 결론: vision decoding은 정서 신경과학의 **통제 변수를 제공**하는 방식으로 기여한다(LS-P1).

**Q2. LLM의 representation이나 reasoning 능력을 neural emotion representation 분석에 활용할 수 있는가?**
그렇다. 다만 세 역할로 한정한다. (1) **기술 기준선(L1):** 캡션 embedding이 고차 시각 반응을 설명한다(doi:10.1038/s42256-025-01072-0). (2) **관찰자 의미 모델(L2):** LLM은 3인칭 평균 관찰자 판단에 가깝고(arXiv:2408.13718), reader-annotator로서 appraisal을 인간 reader 수준으로 평정하며(arXiv:2503.16883), 내부에 조작 가능한 appraisal 방향이 있다(arXiv:2502.05489). (3) **측정 도구:** alt-test와 PPI를 거친 AI 추정 라벨(IM1). 쓰면 안 되는 역할은 **경험 대리**다. 신체 기반 정서, 맥락 반전 장면에서 MLLM이 실패하고(doi:10.1038/s41598-025-14961-6), Gemini 특징은 insula를 설명하지 못한다(doi:10.1162/imag.a.1300).

**Q3. Generative AI로 emotion과 visual semantics를 분리해 검증할 수 있는가?**
비디오 생성 편집만으로는 어렵다. 정서를 바꾸면 내용도 바뀐다(EmoEdit arXiv:2405.12661, NeuroVolve arXiv:2512.00557, generative-counterfactual U1). LLM 쪽에서 쓸 수 있는 대안은 두 가지다. (1) **텍스트 수준 반사실:** 서사에서 사건 순서만 바꾸거나 appraisal 방향을 steering해 내용 단어는 고정하고 appraisal만 바꾼 입력을 만든다. Skerry & Saxe가 요구한 "같은 사건, 다른 순서" 대비(doi:10.1016/j.cub.2015.06.009, Discussion 'Characterizing' 넷째 단락)를 계산할 수 있다. 결론은 R1(in-silico)이다. (2) **정보원 분해 회귀자:** 인물 제거와 배경 제거 입력에 대한 MLLM 추정으로 맥락 정서와 표정 정서를 나눈다(doi:10.1073/pnas.1812250116, Round 1 Chain 7). 이는 R0다. 실제 분리 검증은 R2(편집 자극 행동 평정) 이상이 필요하다.

**Q4. Emotion Dynamics를 dynamical systems나 state-space learning의 문제로 재정의할 수 있는가?**
그렇다. 다만 내 관점에서 핵심 경쟁 가설은 "관찰된 정서 전이 구조가 정서 고유의 동역학인가, 서사 사건 구조의 투영인가"다. 사람은 정서 전이에 대한 정확한 mental model을 가지고(doi:10.1073/pnas.1616056114), LLM은 사건 경계를 합의 수준으로 분할한다(doi:10.3758/s13428-024-02569-z). 따라서 state-space 모형을 적합할 때 **LLM이 계산한 서사 사건 전이와 예측 분포를 nuisance 동역학**으로 넣어야 정서 고유 동역학을 주장할 수 있다. frontier-ai CH1(정서 지도 vs 상황 지도)과 같은 논리이며, 텍스트가 있는 Spacetop narratives가 가장 깨끗한 시험대다(LS-P8).

**Q5. Brain Foundation Model의 latent representation에서 감정 관련 구조를 찾을 수 있는가?**
찾을 수는 있지만 정서 구조라고 부르려면 기술 의미를 통제해야 한다. TRIBE v2 같은 자극 구동 모델은 LLM과 비디오 feature 위에 학습되어 L1과 L2를 상당 부분 담을 것이다. 실제로 TRIBE 합성 뇌는 클립별 정서 정보는 보존했으나 클립 간 정서 관계 구조는 크게 잃었다(arXiv:2605.16739, encoding-foundation 기록 rho 0.635에서 0.166). 제안: BFM latent에서 정서 구조를 찾을 때 **정서 배제 캡션 embedding으로 설명되는 성분을 먼저 제거**하고 남는 구조를 본다(LS-P1의 기준선을 BFM latent에 적용).

**Q6. Music, Video, Image의 공통 정서 특징과 modality-specific 특징을 뇌 수준에서 구분할 수 있는가?**
구분 자체는 가능하지만, "공통" 성분이 **언어로 매개된 개념**일 가능성을 먼저 배제해야 한다. vmPFC의 모달리티 무관 범주 코드에 대해 원 저자가 언어 채널 의존 가능성을 남겼다(doi:10.1126/sciadv.adk6840, multimodal-dynamics 기록). Kiyokawa 2024는 시각-언어(CLIP) 정서 RSM이 뇌 전반과 가장 유사하다고 보고했다(doi:10.1038/s41598-024-71690-y, Discussion 첫째 단락). 제안: 모달리티 간 공통 성분을 찾은 뒤, 그것이 L2 언어 의미 feature로 설명되는 정도를 보고한다(LS-P3). 데이터 제약: 순수 음악 자극은 5개 데이터셋 어디에도 없고 Emo-FilM 사운드트랙이 유일한 음악원이다. Horikawa와 Mind captioning은 무음 비디오, NSD는 정지 이미지다.

**Q7. Neuroscience에서 관찰되는 정서 관련 계산을 AI architecture의 구조적 제약으로 구현할 수 있는가?**
내 담당에서는 제한적으로만 답한다. LLM 정서 표상은 인물 무차별이고 지속 상태가 없다고 보고되었다(arXiv:2604.07729, 5.3절). 뇌에서 관점 결속과 정서 관성이 확인되면(LS-P4, frontier-ai CH3), "경험자 상태"를 별도로 유지하는 구조 제약이 하나의 설계 후보가 된다. 다만 이 프로젝트의 목표는 정서 신경표상에 대한 새 지식이므로, 우선순위는 구조 제약 구현보다 **뇌 유래 정서 기하를 AI 정서 표상의 평가 기준으로 쓰는 방향**(Round 1 I6, frontier-ai T8)이 높다고 본다.

**Q8. 정서 라벨이 없는 NSD 같은 데이터도 다른 데이터셋과의 representation alignment로 의미 있게 활용할 수 있는가?**
조건부로 그렇다. 조건은 세 가지다. (1) NSD의 정서 라벨은 전부 AI 추정이므로 PPI 보정을 위한 소량 무작위 인간 gold 표본이 필요하다(doi:10.1126/science.adi6000, adversarial-reviewer I1). nsdmeadows 100장은 무작위 표본 여부가 미확인이다. (2) NSD 고차 시각 반응은 캡션 LLM embedding이 이미 잘 설명하므로(doi:10.1038/s42256-025-01072-0), 정서 주장은 캡션 embedding을 넘는 잔차로만 한다. (3) **정렬 경로로 기술 층을 쓴다.** NSD(COCO 캡션)와 Mind captioning(정서 배제 캡션)은 둘 다 장면 기술 캡션을 가지므로, 같은 문장 encoder 공간에서 두 데이터셋을 정렬하고, Mind captioning 쪽에만 있는 C&K 정서 축을 그 공간에 투영해 NSD에서 "기술 공간 위의 정서 방향"을 정의할 수 있다. 이 방향으로 NSD 뇌 반응을 설명하는 결과는 "정서 라벨 전이"가 아니라 "기술 공간에 투영된 규범 정서 축의 전이"로 표기한다. COCO 캡션은 정서 배제 지시가 없으므로 캡션 정서 누출 감사(LS-P1의 1번)가 선행되어야 한다.

---

## 부록 A. 선행 수행 판단을 위한 검색 기록

| ID | 대상 제안 | 검색 경로와 질의 | 결과 |
|---|---|---|---|
| S1 | LS-P1 | WebSearch "fMRI emotion unique variance after controlling caption embeddings language model emotion neutral captions video 2025 2026" | 해당 분석 미발견. 가장 가까운 것은 EmoMind(arXiv:2605.16739, 생성 파이프라인)와 Zhang 2026(arXiv:2606.07707, LLM 라벨 decoding) |
| S2 | LS-P1 | vision-decoding Round 1 R6의 독립 검색 결과와 대조 | 같은 공백을 독립적으로 기록함(근거 수준은 검색 범위 내) |
| S3 | LS-P4, Chain 2 | WebSearch "character portrayed emotion versus viewer felt emotion fMRI movie multimodal LLM annotation temporoparietal 2025" | fMRI 연구 미발견. AI 쪽 시청자 관점 데이터셋 2편 발견(arXiv:2607.10238, arXiv:2607.06875, 추가). 뇌 쪽 perceived vs felt는 emotion-theory 기록 doi:10.1162/imag_a_00517로 partially |
| S4 | LS-P5 | WebSearch "alternative annotator test LLM continuous emotion ratings film appraisal components human raters 2025 2026" | 텍스트 appraisal의 reader-annotator 비교(arXiv:2503.16883, 추가)와 연속 engagement(arXiv:2502.04379)만 발견. 영화 연속 평정 성분별 alt-test 미발견 |
| S5 | LS-P2 | encoding-foundation, generative-counterfactual, vision-decoding, emotion-theory Round 1의 각 검색 결과 대조 | 네 에이전트 모두 "자극 구동 기대 반응 잔차 x 본인 보고 편차" 설계를 미발견으로 기록. MLLM 기대 보고를 더한 형태도 미발견 |
| S6 | LS-P6, Chain 6 | WebSearch "language-specific emotion concepts Japanese English language model embeddings brain fMRI alignment cross-linguistic emotion representation" | 일본어-영어 정서 의미와 fMRI를 함께 쓴 연구 미발견. 다국어 LM의 영어 고정(arXiv:2307.01370, 추가)과 언어 간 공유 개념 공간(arXiv:2506.20489, 추가) 발견 |
| S7 | LS-P7, Round 1 Chain 4 | WebSearch "residual between human emotion ratings and AI model predictions explains physiological arousal heart rate skin conductance or insula fMRI" | 잔차 분석 미발견. 가장 가까운 것은 SantavirtaE2025(doi:10.1101/2025.09.18.677029, 잔차나 자율신경 분석 없음, 초록 기준) |
| S8 | IM1, Q8 | WebSearch "prediction-powered inference fMRI encoding AI-generated labels neuroimaging bias correction 2025" | PPI의 fMRI 적용 미발견(adversarial-reviewer I1의 판단과 일치) |
| 참고 | | export.arxiv.org API 키워드 검색 5건을 시도했으나 429로 실패. arxiv.org/abs 페이지로 식별자만 확인했다 | 키워드 기반 arXiv 검색은 미실시 |

"미발견"은 위 검색 범위 안의 판단이며, Stage 3 Round 3와 Stage 4의 중복 감사에서 다시 확인해야 한다.

## 부록 B. 이 라운드의 미확인 사항

* Mind captioning 저장소(ds005191, figshare)에 캡션 파일이 실제로 들어 있는지, 두 코호트(Horikawa 2020과 Mind captioning) 사이 피험자 중복 여부
* Horikawa 2020 참가자의 모국어(LS-P6의 Horikawa 부분의 선결 조건)
* Emo-FilM 대사 언어와 보유 영상 판본(LS-P3)
* Saarimäki 2025의 perceived 문항이 인물을 지정했는지(6절 1번의 전제, emotion-theory DB 기록에 의존)
* Spacetop narratives 이야기의 원 출처(LS-P8의 사전학습 오염 판단)
* arXiv:2607.10238(DAR)의 주석 주체와 절차(초록만 확인)
