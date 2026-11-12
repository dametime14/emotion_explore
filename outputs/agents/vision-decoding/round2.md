# Round 2 (Cross-Agent Exchange): vision-decoding

* 에이전트: vision-decoding (Axis B, G, W 담당, 외부 분야 Memory and Mental Imagery)
* 기준일: 2026-11-12
* 절차: `reference/protocols.md` P2 + Coordinator 위임 메시지의 추가 요구(제안 ID VD-P*, label-provenance와 evidence-level 표기, 8개 질문 답, 새로움 주장의 검색 경로)
* 읽은 파일: 다른 10개 에이전트의 `round1.md`(각 파일의 0, 1, 3, 4, 6절 중심, 필요 시 5절), `outputs/axis_encyclopedia.md`(0절, 2절, 3절), `outputs/STAGE_STATUS.md` 사용자 결정 기록(Stage 2 이후 포함), `outputs/literature/literature_db.csv`(인용 ID 존재 확인용)
* 새로 확인한 문헌 7편을 `outputs/agents/vision-decoding/literature.jsonl`에 추가했다(모두 PubMed 경로 verified, 1편 본문 Discussion 일부 확인, 6편 초록만). 이 문서에서 인용하는 나머지 ID는 모두 `literature_db.csv`에 있는 verified 논문이다.
* 표기: label-provenance는 axis_encyclopedia 0.2절 형식(대상: portrayed / perceived / felt, 주체: 참가자 본인 / peer 합의 / 별도 평정자 규범 / AI 추정). evidence-level은 R0 상관 / R1 모델 내 개입 / R2 새 행동 평정 / R3 새 fMRI 자극 조작 / R4 뇌 개입. MC는 Horikawa et al. (2025) Mind captioning 데이터(doi:10.1126/sciadv.adw1464, ds005191)의 약칭이다.

---

## 0. Round 1 이후 바뀐 것과 내 제안의 재배치

### 0.1 데이터 조건 변화
* 사용자가 MC를 보유하고 전처리까지 마쳤다고 확인했다(STAGE_STATUS 2026-11-12, Stage 2 이후). 저장소의 실제 파일(반복 클립, 회상 과제, vividness, 캡션) 세부는 아직 미확인이다.
* MC 논문 본문에서 다시 확인한 설계 사실 가운데 Round 2 제안에 쓰는 것: 3T Prisma, TR 1 s, **TE 30 ms**, MB6, 전뇌. 2,180개 클립을 **모든 피험자가 같은 순서로** 1회 시청. 테스트 72클립은 학습 세션 마지막 2 run에서 나온 것이고, 원 논문은 그 2 run을 학습 데이터에서 뺐다. 회상 cue는 그 클립의 캡션 20개 중 1개(정서를 쓰지 말라는 지시로 수집된 캡션)이며, 회상 직후 같은 비디오가 다시 제시되고 그 뒤 정확도, vividness를 평정했다. 피험자 6명은 모두 일본어 모국어 화자다.
* Horikawa 2020의 TE는 43 ms라는 systems-neuro 판정(round1 0.5.1)을 받아들이면, **피질하, 안와전두 신호 조건은 MC(TE 30 ms) 쪽이 더 유리할 가능성**이 있다. 실제 tSNR, dropout 지도로 확인해야 한다.

### 0.2 내 Round 1 chain과 다른 에이전트 제안의 겹침

| 내 chain | 겹치는 다른 제안 | 판단 |
|---|---|---|
| R1 재구성의 정서 충실도와 영역 증분 | 없음(재검색 결과는 6절) | 독자 유지. adversarial-reviewer의 측정 오차 경고(A4)와 systems-neuro의 signal-feasibility(A6)를 반영해 수정 |
| R2 회상 정서 재활성 + NEVER | 없음. 단 NEVER의 정서가 비대칭 재현은 선행 있음 | **already_done을 no에서 partially로 정정.** Kark & Kensinger 2019(doi:10.1523/JNEUROSCI.2834-18.2019)가 부정 기억의 온라인 시각감각 재현을, Cocquyt et al. 2026(doi:10.1523/JNEUROSCI.0718-25.2025)이 VVS의 부정 정서 맥락 재현 서명을 보고했다(둘 다 이번 라운드 PubMed 검색으로 발견). 남는 새로움: 자연 영상 클립 회상에서 정서, 의미, 시각 feature 수준별 재활성 비율 비교, 시행별 vividness, 두 코호트 |
| R3 정서 범주 hold-out zero-shot | geometry-info I2(CCGP를 Horikawa 34범주에 적용) | 같은 논리. geometry-info의 CCGP 틀로 합치고, 내 쪽은 회상 일반화와 projection domain shift 통제를 보탠다(VD-P2) |
| R4 정서 영역 선호 자극 합성 | generative-counterfactual CH2(의미 고정 amygdala 제어), encoding-foundation Chain 6(고처리량 screening) | **already_done partially.** NeuroVolve(arXiv:2512.00557)가 amygdala 생성 제어를 실측 fMRI로 검증했다(의미 범주 교란 있음). 독자 chain으로 두지 않고 generative-counterfactual CH2에 decoding 쪽 평가를 보태는 형태로 축소 |
| R5 공유 latent 잔차와 본인 평정 | encoding-foundation Chain 3, llm-semantics Chain 5, generative-counterfactual CH5, emotion-theory C8, geometry-info I4 | 5개 에이전트가 독립적으로 같은 Spacetop 설계를 제안했다. 내 chain은 **철회하고 공동 제안에 합류**한다. 내 쪽 고유 기여는 Horikawa + MC 11명(같은 자극)으로 개인 고유 성분의 반복 신뢰도를 먼저 정의하는 단계(VD-P2 (b)) |
| R6 정서 배제 캡션 통제 후 잔차 | llm-semantics Chain 1 | 같은 질문. llm-semantics Chain 1을 본체로 두고 내 쪽은 decoding 방향과 회상 조건을 보탠다(VD-P3) |

---

## 1. 가져온 아이디어

### A1. 결론 수준 사다리와 의미 고정 정서 편집 (generative-counterfactual)
* 출처: generative-counterfactual round1 0절(R0~R4), U1, CH2. 근거 arXiv:2512.00557(NeuroVolve: amygdala 최대화 이미지는 표정 강한 얼굴, 최소화는 건물. 실측 검증에서 자연 최상위 이미지를 넘지 못함), arXiv:2405.12661(EmoEdit은 내용을 추가해 정서를 바꿈).
* 내 쪽 적용: R4를 "정서 영역 선호 자극 합성"에서 "**얼굴, 신체, 장면 선택 영역 예측을 고정한 조건의 정서 영역 decoding 평가**"로 좁힌다. 모든 생성 경로에 null-edit 대조(같은 생성기 통과 원본)를 넣는다. 재구성 연구에 그대로 옮기면 VD-P4의 affect round-trip test가 된다.

### A2. Rank 분해 공유 스펙트럼과 추상화 기하 (geometry-info, emotion-theory)
* 출처: geometry-info round1 C1, I2, emotion-theory T1, X1. 근거 arXiv:2409.06843(cross-decomposition, 개인 간 공유 스펙트럼이 power-law), doi:10.1016/j.cell.2020.09.031(CCGP, shattering dimensionality).
* 내 쪽 적용: R3의 "zero-shot held-out-category decoding"을 CCGP로 다시 정의한다(범주 단위 hold-out이라 자극 누수가 없다). R5의 "공유 vs 개인"은 MindEye2식 공유 latent 하나가 아니라 rank별 스펙트럼으로 다룬다. MC의 반복 제시가 이 틀에 "개인 내 신뢰도"라는 빠진 조각을 준다(VD-P2).

### A3. "예측 잔차 = 평가"와 in-silico template (encoding-foundation)
* 출처: encoding-foundation round1 4절 연결 개념 1, Chain 1, Chain 3. 근거 arXiv:2605.04326(TRIBE v2: 학습, 평가 데이터에 MC, Horikawa 없음; 공개 checkpoint는 fsaverage5 피질 평균 피험자 예측).
* 내 쪽 적용: R2에서 회상 패턴을 실측 지각 패턴과만 비교하면 재활성의 내용(자극 구동 성분인지 개인 특이 성분인지)을 모른다. TRIBE v2가 예측한 같은 클립의 지각 반응을 "자극 구동 template"로 두면, 회상 패턴을 (a) 자극 구동 template와 공유하는 성분, (b) 그 피험자 실측 지각 패턴 중 template로 설명되지 않는 잔차와 공유하는 성분으로 나눌 수 있다. (b)가 회상에서 재현되면 개인 특이 지각 반응이 기억으로 넘어간다는 증거 후보다. 결과는 insilico-vs-observed "혼합"으로 표기한다.

### A4. 증분 타당도의 측정 오차 위양성과 controversial selection (adversarial-reviewer, encoding-foundation)
* 출처: adversarial-reviewer round1 U1, I3, C1. 근거 doi:10.1371/journal.pone.0152719(Westfall & Yarkoni 2016: 공변량 측정 오차가 증분 타당도 위양성을 만들고 표본이 클수록 심해짐), doi:10.1073/pnas.1912334117(controversial stimuli).
* 내 쪽 적용: R1의 "의미 충실도를 통제한 뒤 남는 정서 회복"은 정확히 이 위양성 구조다. 의미 충실도 지표를 여러 개(CLIP 유사도, 캡션 LM 유사도, 인간 평정)로 다중화하고 신뢰도 민감도 곡선을 보고한다. 또 평가 클립을 무작위로 두지 않고, 의미 충실도 모델과 정서 충실도 모델의 예측이 가장 갈리는 클립을 뇌 데이터 없이 미리 고른다.

### A5. 세 층 분해와 관찰자 관점 (llm-semantics)
* 출처: llm-semantics round1 0절(L1 기술 의미, L2 귀속, 평균 관찰자, L3 경험), U3. 근거 arXiv:2408.13718(GPT-4는 경험자 본인보다 3인칭 독자 평균과 더 일치).
* 내 쪽 적용: 재구성 이미지의 정서를 AI 평가기나 별도 인간 평정자가 판단하면 그 값은 **L2(관찰자 관점) 충실도**다. R1의 "정서 충실도"를 "L2 정서 충실도"로 이름을 고치고, label-provenance를 "perceived, AI 추정 또는 별도 평정자"로 붙인다. 원 자극의 C&K 평정(felt, 별도 평정자 규범)과 비교하는 것은 관점이 다른 두 값의 비교임을 명시한다.

### A6. Signal feasibility와 순서 이월 (systems-neuro, multimodal-dynamics)
* 출처: systems-neuro round1 0.5.1(Horikawa TE 43 ms, 피질하 신호 손실 가능), multimodal-dynamics round1 U1, Chain 1(5명 동일 순서 10 s 블록의 정서 이월과 HRF 잔여).
* 내 쪽 적용: R1의 region-additive decoding은 tSNR, dropout 지도 없이 결과를 내지 않는다. 피질하 증분은 TE가 짧은 MC에서 먼저 보고 Horikawa에서 재현한다. MC도 모든 피험자가 같은 순서로 봤으므로 두 데이터셋 모두 직전 클립의 정서 평정과 feature를 nuisance로 넣는다.

---

## 2. 보내는 제안

### VD-P1 → encoding-foundation (참조: generative-counterfactual)
* **제안 내용:** 너희 Chain 1(in-silico 정서 기하의 충실도)과 generative-counterfactual CH3("같은 자극의 짝 비교")를 우리 쪽 MC의 72클립 x 5회 반복으로 **noise ceiling 정규화된 짝 비교**로 검증할 수 있다. Horikawa 2020은 반복이 없고 Emo-FilM은 ISC 상한만 가능하지만, MC는 같은 피험자 안의 반복으로 vertex별 신뢰도를 직접 준다. 따라서 "실측 정서 RSA 가운데 신뢰할 수 있는 부분 중 TRIBE v2가 재현하는 비율"을 계산할 수 있다. 같은 72클립의 회상 imagery도 있으므로, TRIBE 예측을 회상 패턴의 자극 구동 template로 쓰는 분석(A3)을 함께 할 수 있다. Horikawa 2020 5명은 같은 클립을 1회 본 독립 코호트라 재현 검증에 쓴다.
* **관련 Axis:** F(In-silico Representational Fidelity), H, W, Q, S
* **근거:** arXiv:2605.04326(TRIBE v2 학습, 평가 목록에 MC 없음, 피질하 점수 2~3배 낮음), arXiv:2605.16739(EmoMind의 TRIBE 대체 비교는 자극 집합이 달랐음), doi:10.1126/sciadv.adw1464(MC 설계), doi:10.1523/JNEUROSCI.2406-23.2025(정서 사건은 반복 간 패턴이 더 안정적일 수 있음)
* **가능한 데이터셋:** MC(주), Horikawa 2020(재현)
* **표기:** label-provenance = felt, 별도 평정자 규범(C&K 34/14). evidence-level = R0(실측) + R1(TRIBE 예측). insilico-vs-observed = 혼합. G1 = 필요(보유). signal-feasibility = TRIBE 공개 checkpoint는 피질만이라 피질하 비교 불가, MC는 3T TE 30 ms MB6.
* **예상되는 반론:** (1) 72클립의 정서 분포가 확인되지 않았고 72개로는 34차원 RSA가 불안정하다. 14차원 또는 valence, arousal 수준으로 줄여야 할 수 있다. (2) 짧은 클립(테스트 평균 약 3.9 s)을 10 s가 될 때까지 반복 재생한 블록 구조를 TRIBE 입력에 똑같이 재현해야 한다. (3) 정서 클립이 반복 간 더 안정적이면(Krenz 2025) ceiling 자체가 정서와 공선적이다. 정서 수준별 ceiling을 따로 보고한다. (4) 회상 직후 같은 비디오가 제시되어 회상 창 끝에 HRF가 겹친다.

### VD-P2 → geometry-info (참조: emotion-theory)
* **제안 내용:** 너희 C1(rank 분해 공유 스펙트럼)과 I2(CCGP)를 우리 쪽 **두 코호트 같은 자극 설계**로 확장할 수 있다. (a) Horikawa 5명 + MC 6명 = 11명이 같은 2,180클립을 봤으므로 피험자 쌍 55개를 site 내 쌍(10 + 15)과 site 간 쌍(30)으로 나눠, 공유 스펙트럼 가운데 site, 스캐너, 피험자 집단을 넘어 보존되는 rank 대역을 추정한다. (b) MC 72클립 5회 반복으로 피험자 내 반복 스펙트럼을 구하면 rank별로 "피험자 내에서는 신뢰하지만 피험자 간에는 공유되지 않는 분산"을 정의할 수 있다. Horikawa만으로는 개인 고유 성분과 잡음을 구분하지 못한다. (c) CCGP를 지각에서 회상으로 확장한다: 지각에서 범주 hold-out으로 학습한 valence, arousal decoder가 회상 imagery에서도 일반화되는가. 추상 정서 축이 top-down 재활성에서도 같은 기하를 갖는지를 묻는다.
* **관련 Axis:** K, O, Q, W, G
* **근거:** arXiv:2409.06843, doi:10.1016/j.cell.2020.09.031, doi:10.1126/sciadv.adw1464, doi:10.1038/ncomms15037(지각 학습 decoder의 imagery 범주 일반화), doi:10.3390/s23156903(zero-shot 해독의 projection domain shift)
* **가능한 데이터셋:** Horikawa 2020, MC
* **표기:** label-provenance = felt, 별도 평정자 규범(CCGP 범주 정의에만 사용; 스펙트럼 자체는 라벨 불필요). evidence-level = R0. insilico-vs-observed = 관찰. G1 = 스펙트럼, CCGP는 불필요, 시각-의미 대역 분해에는 필요(보유).
* **예상되는 반론:** (1) 두 site의 TR(2 s vs 1 s), 스캐너, 전처리 차이가 공유 스펙트럼을 깎는다. 학습 클립으로 hyperalignment한 뒤 시험 클립으로 평가하고, site 간 쌍과 site 내 쌍의 차이를 그 자체로 보고한다. (2) 72클립으로는 약 70 rank가 상한이라 고rank 개인 고유 성분은 볼 수 없다. (3) CCGP의 범주 hold-out에서는 source 범주 쪽으로 사상이 치우치는 projection domain shift가 생긴다(Akamatsu 2023). 실패를 곧바로 "추상 정서 축 없음"으로 읽지 않는다. (4) 회상 SNR이 낮아 imagery CCGP는 검정력이 약하다. (5) 두 코호트 사이 피험자 중복 여부가 미확인이다.

### VD-P3 → llm-semantics
* **제안 내용:** 너희 Chain 1(정서 배제 기술의 잔차)과 우리 R6는 같은 질문이니 너희 Chain 1을 본체로 합치자. 우리 쪽이 보탤 수 있는 것은 세 가지다. (a) MC의 인간 중립 캡션 20개는 같은 클립을 본 Horikawa 2020에도 그대로 적용되므로, "기술 잔차 정서" 지도가 두 코호트(11명)에서 재현되는지 볼 수 있다. (b) decoding 방향과 회상 조건을 더한다. 뇌 → 중립 캡션 LM feature와 뇌 → C&K 정서를 각각 해독해 회상 imagery로 일반화시키면, 기술로 환원되지 않는 정서 성분이 회상에서도 재활성되는지 볼 수 있다. 회상 cue가 정서 배제 캡션 그 자체였으므로, **정서 decoder의 회상 성공은 cue 텍스트로 설명되기 어렵고 의미 decoder의 성공은 cue 읽기로 부풀 수 있다**는 비대칭이 설계에 들어 있다. (c) MC 피험자 6명은 일본어 모국어 화자라고 본문에 적혀 있다. 너희 Chain 6(일본어 vs 영어 정서 기술)의 선결 조건(참가자 언어)이 MC에서는 충족된다. Horikawa 2020 참가자 언어는 여전히 미확인이다.
* **관련 Axis:** C(Description Residual), B(Annotation Instruction as Stimulus Descriptor), G, W, U
* **근거:** doi:10.1126/sciadv.adw1464(Subjects, Caption annotation, Imagery experiment 절), doi:10.1038/s42256-025-01072-0, arXiv:2509.24298, doi:10.1371/journal.pone.0152719
* **가능한 데이터셋:** MC(주), Horikawa 2020
* **표기:** label-provenance = 캡션은 별도 평정자의 시각 내용 기술(정서 배제 지시), 정서는 felt, 별도 평정자 규범, MLLM 기술은 AI 추정. evidence-level = R0. insilico-vs-observed = 관찰. G1 = 캡션 경로 불필요, MLLM 경로 필요(보유).
* **예상되는 반론:** (1) "정서 배제"는 지시의 속성이지 내용의 속성이 아니다. 장례식 장면의 중립 캡션도 정서를 함의한다. 결과는 "언어화된 장면 의미가 함의하는 정서를 넘는 정서"로 해석한다. (2) 캡션 embedding 평균의 측정 오차가 정서 잔차를 부풀린다(Westfall & Yarkoni). 캡션 split-half 신뢰도와 민감도 곡선을 붙인다. (3) 의미 decoder의 회상 성공에서 cue 캡션을 학습 목표에서 빼는 통제가 필요하다.

### VD-P4 → generative-counterfactual
* **제안 내용:** 너희 S7(Generator-prior and AI-ness confound audit)과 null-edit 대조를 재구성 decoding의 표준 단계로 가져오자. 구체적으로 **affect round-trip test**를 제안한다. Horikawa 원 프레임 → 정답 CLIP, VDVAE latent → NSD로 학습된 생성기(SDXL unCLIP, Versatile Diffusion)로 재생성 → C&K 비노출 정서 평가기와 소규모 인간 평정. 뇌가 개입하지 않는 이 경로의 정서 손실이 "생성기 고유 정서 중립화"의 크기다. 뇌 해독 latent 경로에서는 그 위에 더해진 손실만 뇌에 귀속한다. 너희 CH1, CH2의 의미 고정 편집도 같은 계열 생성기를 쓰면 같은 중립화가 섞이므로 이 audit가 공통 전제다. 반대 방향으로 우리 쪽은 너희 "의미 고정" 제약을 decoding 검정에 쓸 수 있다. 뇌에서 해독한 캡션(의미)은 고정하고 정서 방향만 다르게 생성한 두 후보 가운데 뇌에서 해독한 image latent에 더 가까운 쪽을 고르는 2AFC를 하면, 뇌 latent에 의미와 별개인 정서 방향 정보가 있는지 볼 수 있다.
* **관련 Axis:** L(Generator-prior Audit), G(Affective Fidelity), P, T
* **근거:** arXiv:2403.11207(SDXL unCLIP), doi:10.1038/s41598-023-42891-8(Versatile Diffusion, VDVAE), doi:10.1016/j.neunet.2025.107515(사실적 외양은 정확한 재구성을 뜻하지 않음), arXiv:2605.17198(NSD prior가 재구성 내용을 지배), arXiv:2401.04608(CLIP 공간에 정렬한 정서 공간), arXiv:2512.00557
* **가능한 데이터셋:** Horikawa(주), MC, NSD(대조: 중립 분포에서는 손실이 작아야 함)
* **표기:** label-provenance = 원 자극은 felt, 별도 평정자 규범. 재생성 이미지 평가는 perceived, AI 추정 또는 신규 별도 평정자. evidence-level = R1(모델 내), 인간 평정 추가 시 R2. insilico-vs-observed = in-silico(round-trip), 혼합(뇌 경로). G1 = 필요(보유).
* **예상되는 반론:** (1) 정답 latent로 재생성한 이미지를 상한으로 쓰는 것은 재구성 연구의 관행이라 새롭지 않다. 새로움은 정서 축으로 측정한다는 점에 한정된다. (2) 정서 평가기 자체의 편향(EmoSet은 정지 이미지, Horikawa는 영상 프레임). (3) 영상에서 프레임 하나를 고르는 순간 움직임이 운반하는 정서가 손실된다. 다중 프레임과 video 모델 경로를 함께 둔다. (4) 2AFC의 정서 방향 정의가 곧 "정서"의 조작적 정의가 된다(너희 X5). 편집 가족을 여러 개 두고 결과가 유지되는지 본다.

### VD-P5 → systems-neuro (참조: brain-inspired)
* **제안 내용:** 너희 Chain 3(colliculus-pulvinar-amygdala 경로)과 brain-inspired Chain 3(경로가 싣는 표상 내용)을 우리 쪽 **region-additive latent decoding**으로 검증할 수 있다. 경로 ROI 또는 amygdala voxel만으로 저수준 latent(VDVAE, 저공간주파수 feature)와 고수준 latent(CLIP)를 각각 해독해 "해독 가능한 정보의 수준 비율"을 비교하고, 시각피질 해독에 이 voxel을 더했을 때 저수준과 고수준 latent 중 어디서 증분이 생기는지 본다. "조잡한 shortcut" 가설은 저수준 증분이 고수준 증분보다 크다고 예측한다. 측정은 latent 상관으로 하고 재구성 이미지는 시각화로만 쓰며, shuffled-brain 기준선을 함께 보고한다. 편도체 → 복측 시각피질 effective connectivity가 불쾌 decoding 정확도를 예측했다는 보고(Bo 2021)가 있어, 시각피질 해독의 정서 정보 일부가 재진입에서 왔을 가능성도 같은 틀로 다룬다.
* **관련 Axis:** E(Visual Subcortical Routes), G(Region-additive Decoding), N, B
* **근거:** doi:10.1016/j.neuron.2021.06.001, doi:10.1038/s41598-023-42891-8(ROI별 VDVAE vs CLIP 가중치), doi:10.1093/cercor/bhaa411, arXiv:2607.19327, doi:10.1016/j.neunet.2025.107515
* **가능한 데이터셋:** Spacetop alignvideo(Kragel 2021과 같은 획득 조건, 소리 있음), MC(TE 30 ms), Horikawa(TE 43 ms 주의), NSD(해상도 최고, 반복과 기억 과제 교란)
* **표기:** label-provenance = 해독 목표는 자극 feature(라벨 아님). 정서 해석 시 felt, 별도 평정자 규범(Horikawa, MC) 또는 felt, 참가자 본인(Spacetop). evidence-level = R0. insilico-vs-observed = 관찰. G1 = 필요(보유). signal-feasibility = **필수**(상구, pulvinar, amygdala tSNR과 dropout 지도 선행).
* **예상되는 반론:** (1) 작은 ROI의 낮은 SNR 때문에 latent 해독이 거의 0이면 재구성은 생성 prior만 보여 준다. latent 상관과 shuffled 기준선이 1차 결과다. (2) MPathI의 경로는 다변량 패턴이지 voxel 집합이 아니므로 ROI 정의가 원 개념과 다르다. (3) fMRI로는 속도(latency)를 말할 수 없고 표상 내용만 다룬다(brain-inspired P-3과 같은 한계). (4) 블록 평균(Horikawa, MC)은 시간 정보를 지운다.

### VD-P6 → emotion-theory
* **제안 내용:** 너희 S3(이제 Axis A의 Sub-axis "Introspective Access and Emotion Report")와 C4(privileged access 검정)는 우리 데이터에 직접 측정이 없다고 했다. 그런데 MC 회상 과제의 **시행별 vividness, accuracy 평정**은 5개 데이터셋 중 유일한 시행 단위 내성 보고다. 같은 시행의 지각-회상 신경 재활성 정도(객관 지표)와 vividness(내성 보고)의 대응을 HMeta-d류 지표로 정량화하면 "심상에 대한 내성 접근의 민감도"를 구할 수 있다. 그 민감도가 회상 대상 클립의 규범 정서(valence, arousal)에 따라 달라지는지 묻는다. 비정서 자극에서 vividness와 지각-심상 중첩의 대응은 이미 보고되었으므로(Dijkstra 2017), 새로움은 정서에 따른 조절에 한정된다.
* **관련 Axis:** A(Introspective Access), W, Q
* **근거:** doi:10.1523/JNEUROSCI.3022-16.2016, doi:10.1016/j.cub.2024.09.062(V1 감각 표상과 주관 심상의 해리), doi:10.1093/nc/nix007(HMeta-d), doi:10.1126/sciadv.adw1464(회상 시행 설계)
* **가능한 데이터셋:** MC(유일)
* **표기:** label-provenance = vividness는 참가자 본인의 내성 보고(대상은 심상의 질이지 정서가 아님). 정서는 felt, 별도 평정자 규범. evidence-level = R0. insilico-vs-observed = 관찰. G1 = 불필요(평정 + 뇌), 재활성 지표를 feature 수준별로 나누면 필요(보유).
* **예상되는 반론:** (1) vividness 평정은 회상 직후 실제 비디오를 본 뒤에 이루어져, 순수 내성 보고가 아니라 "기억과 실물의 비교 판단"이다. 원 설계의 한계로 명시한다. (2) 정서를 보고한 것이 아니므로 결과는 정서 내성이 아니라 "정서 기억의 심상에 대한 내성"이다. (3) 1인당 360 시행(72클립 x 5회)으로 metacognitive 지표를 추정할 수 있으나 클립 간 정서 분포가 치우쳤으면 정서 조절 검정력이 약하다.

### VD-P7 → brain-inspired
* **제안 내용:** 너희 Chain 6(정서 전용 하위체계는 최적화에서 생기는가)은 Cowen & Keltner와 독립인 공개 정서 학습 데이터를 찾지 못했다고 했다. **EmoSet**(ICCV 2023)이 후보다. 330만 장 중 118,102장에 인간 정서 주석이 있고, 범주와 함께 밝기, 채도, 장면 유형, 물체, 표정, 행동 속성이 주석되어 있다. 속성 주석이 있어 "창발한 정서 unit이 저수준 속성과 의미 속성 중 무엇에 의존하는가"를 lesion 분석과 함께 볼 수 있다. 우리도 재구성 이미지 정서 평가기를 같은 데이터로 학습할 계획이라 학습 분할과 오염 점검(C&K GIF와의 지각 해시 중복 검사)을 공유하자.
* **관련 Axis:** N, I, B, S(Pretraining Contamination)
* **근거:** arXiv:2307.07961, doi:10.1126/sciadv.aaw4358(EmoNet 학습 자료 = Horikawa 자극), doi:10.1371/journal.pcbi.1011943(물체 학습 CNN의 정서 unit 창발)
* **가능한 데이터셋:** 학습은 EmoSet, 신경 평가는 Horikawa, MC, NSD
* **표기:** label-provenance = EmoSet은 perceived, 별도 평정자(이미지가 일으킬 정서에 대한 평정자 판단). Horikawa 평가는 felt, 별도 평정자 규범. evidence-level = R0(신경 예측), R1(lesion). insilico-vs-observed = 혼합. G1 = 필요(보유).
* **예상되는 반론:** (1) EmoSet은 Mikels 8범주라 C&K 34범주와 대응이 불완전하다. (2) 소셜 미디어 정지 이미지와 영상 프레임의 domain shift. (3) EmoSet 데이터와 가중치의 공개 조건은 이번 라운드에서 확인하지 못했다.

### VD-P8 → frontier-ai
* **제안 내용:** 너희 U7, T2("정서와 무관한 정렬이 정서 기하를 운반하는가")를 **뇌 decoding 모델의 공유 latent**에서 직접 시험할 수 있다. MindEye2의 4096차원 shared-subject latent와 Brain-IT의 brain token은 NSD 중립 장면에서 정서와 무관한 시각 목표로만 학습되었다. 이 모델을 Horikawa나 MC 피험자에 적응시킨 뒤(MindEye2는 피험자별 ridge, Brain-IT는 voxel embedding만 학습) 공유 latent에 C&K 정서 probe를 붙이면, 정서 기하가 "정서와 무관한 시각 정렬"만으로 얼마나 운반되는지 잴 수 있다. 같은 피험자의 원 voxel 공간 probe가 상한, 무작위 사상 latent가 하한이다. VLM 사이의 정서 vector 운반(arXiv:2609.34742)의 뇌 버전이다.
* **관련 Axis:** R(Machine Affect Representations, 정렬 운반), G, F, O
* **근거:** arXiv:2609.34742, arXiv:2405.07987, arXiv:2403.11207, arXiv:2510.25976
* **가능한 데이터셋:** Horikawa, MC(적응 데이터), NSD(사전학습 출처)
* **표기:** label-provenance = felt, 별도 평정자 규범. evidence-level = R0. insilico-vs-observed = 관찰(모델 latent에 실측 fMRI 입력). G1 = 적응 단계에 필요(보유).
* **예상되는 반론:** (1) 적응 단계의 학습 목표가 원 자극 CLIP latent라면 정서 정보가 CLIP 쪽에서 들어온다. 적응 목표를 정서와 무관한 저수준 목표로 바꾼 대조가 필요하다. (2) 체크포인트와 라이선스 위치가 검색 수준이다(round1 2.1절). (3) Brain-IT의 transfer learning 학습 코드는 미공개 항목으로 남아 있다는 검색 결과가 있다.

---

## 3. 받은 제안에 대한 응답

### 3.0 응답에 쓴 새 사실 (2026-11-12 확인)
MC 공개 저장소(OpenNeuro ds005191 GitHub 미러, git 메타데이터만 shallow clone, 실행 없음)와 Horikawa 2020 미러(ds002425, Stage 1에서 받은 사본)의 `events.tsv`, `README`, `dataset_description.json`을 직접 읽었다. 사용자 보유 사본도 같은 파일일 것으로 보지만 확인하지는 않았다.
* **MC 라이선스는 CC0**(`dataset_description.json`).
* **회상 시행별 vividness와 accuracy가 events.tsv에 있다.** 피험자당 360시행(72클립 x 5회). 전체 vividness 분포는 1점 12, 2점 373, 3점 997, 4점 704, 5점 74다. 피험자별로 크게 치우쳐 있다. sub-01은 2점 9회와 5점 5회를 빼면 3, 4점뿐이고, sub-06은 360회 중 282회가 3점이다.
* **회상 시행의 순서**는 준비(cue) → 회상(눈 감음, 12 s 등) → 휴지 2 s → 같은 비디오 제시 → 휴지 → accuracy, vividness 평정이다. 평정은 비디오를 다시 본 뒤에 한다.
* **72 테스트 클립의 노출 횟수**: 학습 세션 1회(MC 학습 순서의 2,108~2,179번째, 즉 마지막 72블록), 테스트 세션 5회, 회상 세션에서 회상 직후 재제시 5회. 최대 11회다(세션 간 간격은 미확인).
* **제시 순서**: Horikawa 2020은 5명 모두 같은 순서(2,196블록)다. MC는 6명 중 4명이 같은 순서이고, sub-04와 sub-06은 일부 run 순서만 다르다(학습 순서 Spearman 0.996, 0.9997). **두 코호트의 순서는 사실상 독립이다**(같은 비디오 파일 번호 기준 Spearman -0.03). 72 테스트 클립은 MC에서는 학습 순서 끝에 몰려 있고, Horikawa에서는 흩어져 있다.
* MC 피험자는 지각 시 "fixation 없이" 자유 시청했다(논문 Methods). Horikawa 2020의 시청 지시는 확인하지 못했다.

### 3.1 나에게 온 제안

| 제안 | 판정 | 요지 |
|---|---|---|
| ET-P6 (emotion-theory) | **수정** | VD-P6과 하나로 합친다. 시각 대 정서 부분공간의 type-2 비교는 채택한다. 단 vividness 분포가 치우쳐 이진 분할이 불가능한 피험자가 있고, 부분공간 decoder의 신뢰도를 먼저 맞춰야 한다 |
| EF-P2 (encoding-foundation) | **수용** | 이미 A3으로 가져온 설계다. 노출 횟수, 눈 감은 회상, 자유 시청 사실을 반영한 보완 3개를 더한다 |
| GI-P5 (geometry-info) | **수정** | 통합 multiverse에 동의한다. 1차 기준선을 하나로 사전 지정하고, Spacetop의 잔차 신뢰도 추정법은 고친다. 내 쪽은 기준선을 하나 더 추가하지 않는다 |
| SN-P5 (systems-neuro) | **수정** | 반복 x arousal의 amygdala 모형을 채택한다. 반복 번호를 테스트 5회가 아니라 최대 11회의 실제 노출 이력으로 다시 정의하고, 블록 안 반복 재생도 모형에 넣는다 |
| GC-P7 (generative-counterfactual) | **수용** | R4를 이미 너희 CH2에 합쳤다. 합성 전 encoder 신뢰도 관문과 VD-P4 round-trip audit을 붙인다 |
| LS-P1 (llm-semantics) | **수용** | 너희 Chain 1을 본체로 둔다. 회상 cue 캡션 처리와 코호트 간 순서 차이 활용을 더한다 |
| BI-P6 (brain-inspired) | **수정** | 행동 경향 band는 C&K 클립에 인간 라벨이 없어 AI 추정 라벨이 된다. Emo-FilM Motivation 10항목으로 먼저 타당화하고, 통합 W 파이프라인의 선택 band로 둔다 |

**ET-P6 → 수정.**
* 채택: 재활성을 시각 부분공간과 정서 부분공간(시각, 의미 feature로 잔차화한 34/14 규범 decoder)으로 나누고 vividness의 type-2 민감도를 비교하는 설계. 내 VD-P6과 같은 데이터, 같은 질문이므로 하나로 합친다.
* 선행 범위: 비디오 회상 재활성과 vividness의 대응(doi:10.1162/jocn_a_00839)과 feature 수준별 재활성 및 vividness의 관계(doi:10.1038/s41467-020-15763-2, 저수준과 고수준 재활성 모두 vividness와 상관)는 이미 있다. 따라서 내 R2의 "feature 수준별 재활성 비율" 부분도 partially로 낮춘다. 남는 새로움은 정서 부분공간 추가와 정서가에 따른 차이다.
* 수정 1, 척도: vividness가 피험자마다 3~4점에 몰려 있어 "강, 약" 이진 분할은 일부 피험자에서 불가능하다. 피험자 내 서열 type-2 지표(서열 수준 AUROC 또는 누적 로짓)로 하고, 피험자별 결과를 모두 보고하고 유병률(prevalence)로 요약한다.
* 수정 2, 신뢰도 정합: 정서 부분공간 decoder는 시각 부분공간 decoder보다 잡음이 커서, 그대로 비교하면 정서 쪽 type-2가 구조적으로 낮게 나온다. MC 테스트 5회 반복으로 두 부분공간 decoder의 반복 신뢰도를 먼저 구한다. 시각 쪽 feature 수를 줄이거나 잡음을 더해 신뢰도를 맞춘 뒤 비교한다.
* 수정 3, 보고의 성격: vividness와 accuracy는 비디오를 다시 본 뒤에 평정했다. 두 평정을 모두 쓰고, "실물과 비교한 사후 판단"이라는 한계를 명시한다.
* (b) "보고되지 않은 정서 재활성"은 탐색적으로 유지한다. V1 감각 표상과 주관 심상의 해리(doi:10.1016/j.cub.2024.09.062)가 같은 구조의 선례다. 저vividness 시행이 극히 적은 피험자는 이 분석에서 뺀다.

**EF-P2 → 수용.** 내 A3과 같은 설계라 그대로 받는다. 보완 세 가지를 더한다. (1) TRIBE v2 head fine-tuning은 MC 학습 순서의 마지막 72블록(= 테스트 클립)을 뺀 2,108블록으로 한다(위 3.0 확인). (2) "반복 신뢰 잔차"에는 최대 11회 노출에 따른 친숙도와 적응이 섞인다. 학습 세션의 첫 노출과 테스트 반복에서 잔차를 따로 구해 안정성을 비교한다. (3) 지각은 자유 시청, 회상은 눈 감음이다. 그래서 개인별 시선 패턴이 만든 지각 잔차는 회상에서 같은 방식으로 재현될 수 없다. 초기 시각피질의 잔차 재활성이 낮게 나올 것으로 예상되므로 이를 내장 대조로 쓴다. cue 텍스트를 TRIBE v2 텍스트 입력으로 예측해 nuisance로 빼는 방법은 그대로 채택한다.

**GI-P5 → 수정.** 다섯 기준선을 한 multiverse로 묶는 데 동의하고, 내 R5는 이미 철회했다(0.2절). 수정은 세 가지다. (1) 1차 기준선을 leave-one-subject-out peer 평균으로 사전 지정하고 나머지 넷은 민감도 분석으로 둔다. 기준선 간 일치도는 따로 보고한다. 이렇게 하면 다중비교 부담이 줄고 "기준선 간 차이"가 탐색 결과임이 분명해진다. (2) Spacetop은 영상마다 1회 시청이라 "영상 절반 분할" 잔차 신뢰도는 영상 안 자기상관으로 부풀려진다. 두 절반 사이에 HRF와 자기상관 길이 이상의 간격을 두거나, 서로 다른 영상에서 잔차 방향의 일관성으로 신뢰도를 정의한다. (3) 너희 5번(캡션 잔차의 공유 스펙트럼)은 LS-P1과 GI-P1 3단계와 같은 분석이므로 그쪽에서 한 번만 수행한다. MindEye2식 공유 latent는 공유 자극이 없을 때 장점이 있는 방법이라, 모두가 같은 영상을 본 Spacetop에서는 기준선을 더하지 않는다. 내 쪽 기여는 decoding 방향의 보조 판독(뇌 → 본인 평정 편차 decoder)으로 한정한다.

**SN-P5 → 수정.** amygdala 반복 비정상성을 측정 대상으로 바꾸는 발상과 규범 arousal에 따른 감쇠 기울기 검정은 채택한다. 3.0의 사실에 따라 설계를 고친다. (1) 반복 번호를 "테스트 1~5회"가 아니라 실제 노출 이력(학습 세션 1회 → 테스트 5회 → 회상 세션 재제시 5회, 최대 11회)으로 정의한다. 학습 세션의 첫 노출이 진짜 1회차다. (2) 10 s 미만 클립은 블록 안에서 반복 재생되었으므로(테스트 클립 평균 약 3.9 s) 블록 안 빠른 적응이 블록 간 감쇠와 섞인다. 블록 단위 모형에 "블록 내 재생 횟수"를 공변량으로 넣는다. (3) MC 기본 전처리는 테스트 5회를 평균하므로, 반복별 반응은 run 단위나 raw에서 다시 추출해야 한다(사용자 전처리본의 형태는 미확인). (4) Horikawa 2020은 같은 72클립을 흩어진 위치에서 1회만 봤으므로 "1회 노출" 기준선이 된다. 너희가 제안한 amygdala split-half 신뢰도 관문(낮으면 중단)은 그대로 둔다.

**GC-P7 → 수용.** R4는 이미 너희 CH2에 합쳤다(0.2절). 두 단계 설계와 생성 쪽 prior-vs-evidence 분해(무작위 encoder 가중치 목표, 다른 영역 목표)를 받는다. 더할 것은 두 가지다. (1) 합성 전 관문: amygdala encoder를 MC(학습 2,108클립, TE 30 ms)와 Horikawa(2,181클립, TE 43 ms)로 따로 학습하고, MC 테스트 반복으로 각 encoder의 예측 신뢰도를 확인한 뒤에만 합성한다. (2) VD-P4의 affect round-trip audit로 생성기 자체의 기본 정서를 먼저 재고, brain-guided 합성 결과에서 그 몫을 뺀다. 평가기는 C&K 비노출 모델(EmoSet 계열)과 신규 인간 평정(R2)을 쓴다. 주의: C&K 비디오는 요청 양식으로 받은 자료라, 이 비디오로 학습한 모델이 만든 이미지를 공개할 때의 조건은 미확인이다.

**LS-P1 → 수용.** 너희 Chain 1을 본체로 두고 캡션 누출 감사와 L1a, L1b, L2 중첩 기준선을 그대로 받는다. 더할 것은 세 가지다. (1) 회상 조건에서는 cue로 쓰인 캡션 하나를 L1b 캡션 집합에서 빼거나 별도 회귀자로 둔다. 그렇지 않으면 의미 decoder의 회상 성공이 cue 읽기로 부풀고 정서 잔차는 과소 추정된다. 어떤 캡션이 cue였는지는 events.tsv에 없으므로 원 저자 자료나 코드로 확인해야 한다. (2) 72 테스트 클립은 MC에서는 학습 순서 끝에, Horikawa에서는 흩어진 위치에 있다(3.0). 같은 지도가 두 코호트에서 재현되면 순서와 시점 교란에 강한 결과가 된다. (3) MC 라이선스는 CC0다. figshare에는 전처리 fMRI와 "semantic features"가 있다고 README에 적혀 있으나 캡션 원문 포함 여부는 미확인이다.

**BI-P6 → 수정.** 회상에서 band별 보존을 비교하는 틀은 ET-P6, EF-P2와 같은 파이프라인이라 함께 돌릴 수 있다. 그러나 행동 경향 band에는 문제가 있다. (1) C&K 클립에는 행동 경향의 인간 라벨이 없고, latent action model(arXiv:2410.11758)은 조작 비디오로 학습되었다. 이 band는 AI 추정 라벨이 된다. 먼저 Emo-FilM의 Motivation 10항목(별도 평정자 1 Hz)에서 MLLM 행동 경향 추정의 타당도를 확인한 뒤에 C&K 클립에 적용한다. (2) MC 회상 시행에서 평정 버튼 반응은 비디오 재제시 뒤에 있으므로(3.0) 회상 구간의 운동 영역 활성이 버튼 준비 때문일 가능성은 낮다. 다만 눈 감기와 회상 노력은 남는다. 지각 대조와 vividness 공변량을 쓴다. (3) band별 decoder의 신뢰도를 ET-P6 수정 2처럼 맞춘다. (4) 우선순위는 ET-P6, EF-P2보다 뒤에 두고 같은 파이프라인의 선택 band로 둔다.

### 3.2 참조로 언급된 제안 (짧게)

| 제안 | 판정 | 이유 |
|---|---|---|
| ET-P1 (→ geometry-info) | 수용 | 내 VD-P2와 같은 설계다. GI-P1로 통합되었고, 나는 Round 3에서 GI-P1을 검토한다 |
| ET-P2 (→ encoding-foundation) | 수용 | R5를 철회하고 이 통합 설계에 합류한다(0.2절) |
| EF-P1 (→ generative-counterfactual) | 수용 | MC 반복 ceiling 기반 trust map에 동의한다. 72 테스트 클립이 MC 학습 순서 끝에 몰려 있고 노출이 최대 11회라는 점(3.0)을 ceiling 해석에 반영해야 한다 |
| EF-P3 (→ emotion-theory) | 수용 | "(b) - (a)", 즉 공유되지만 자극으로 계산되지 않는 성분이라는 분해는 내 R1의 "시각-의미로 환원되지 않는 정서"와 같은 논리의 집단 수준 판이다 |
| GC-P2 (→ llm-semantics) | 수용 | LS-P1의 통계 통제와 편집에 의한 설계 통제를 같은 voxel에서 맞대는 삼각 검증에 동의한다. 편집 자극 평가 전에 VD-P4 round-trip audit을 공통 전제로 둘 것을 제안한다 |
| LS-P2 (→ encoding-foundation) | 수정 | 통합에 동의한다. 다만 나에게 배정된 "공유 latent와 개인 잔차의 분해"는 hyperalignment를 맡은 encoding-foundation, geometry-info와 겹친다. 내 역할은 decoding 방향의 보조 판독으로 줄인다(GI-P5 응답과 같음) |

---

## 4. Coordinator 질문에 대한 답

**Q1. Vision Decoding 연구자가 Emotion Neuroscientist의 문제를 해결할 수 있는가?**
일부는 해결할 수 있다. (a) region-additive decoding으로 "시각-의미 정보를 넘어 어느 영역이 정서 정보를 더하는가"를 정보량 단위로 잴 수 있다(arXiv:2403.11207, doi:10.1038/s41598-023-42891-8). (b) 지각 학습 decoder를 회상에 적용하는 cross-decoding으로 자극 없이 생성된 정서 표상을 다룰 수 있다(doi:10.1126/sciadv.adw1464, arXiv:2506.06898). (c) 재구성은 가설 생성용 시각화로 쓸 수 있다. 해결하지 못하는 것: 해독된 정서는 P/N 수준 정보이며 참가자 경험(X)의 증거가 아니다. 생성 prior가 정서 외양을 만들어 낼 수 있다(doi:10.1016/j.neunet.2025.107515).

**Q2. LLM의 representation이나 reasoning을 neural emotion representation 분석에 쓸 수 있는가?**
쓸 수 있다, 단 관점을 표시해야 한다. 정서 배제 인간 캡션의 LM embedding은 "언어화된 장면 의미" 통제 변수로 강하다(doi:10.1038/s42256-025-01072-0, doi:10.1126/sciadv.adw1464). 뇌에서 해독한 의미 feature를 정서 채널과 분리해 다루는 것도 가능하다(arXiv:2605.16739). 그러나 LLM 정서 판단은 평균 관찰자 관점에 가깝다(arXiv:2408.13718). 그래서 LLM 기반 정서 회귀자나 평가기는 L2(귀속) 수준이고 경험의 대리가 아니다.

**Q3. Generative AI로 emotion과 visual semantics를 분리해 검증할 수 있는가?**
부분적으로만 가능하다. 정서를 편집하면 의미가 함께 바뀐다(arXiv:2512.00557, arXiv:2405.12661). decoding 쪽에서 가능한 것은 두 가지다. (a) 생성기 자체의 정서 중립화를 뇌 없이 먼저 재는 round-trip audit(VD-P4). (b) 뇌 해독 의미(캡션)를 고정하고 정서 방향만 다른 후보 중 뇌 latent에 가까운 쪽을 고르는 2AFC. 둘 다 R1~R2 수준이며 실제 뇌의 인과 결론(R3)에는 새 fMRI가 필요하다.

**Q4. Emotion Dynamics를 dynamical systems나 state-space learning 문제로 재정의할 수 있는가?**
내 담당 범위에서는 제한적이다. Horikawa와 MC 공개 전처리본은 블록 평균이라 클립 내 동역학이 없다. 기여할 수 있는 지점은 두 가지다. (a) 회상은 "자극 없는 궤적의 재생"이므로, 회상 중 정서 상태가 지각과 같은 순서와 속도로 재생되는지(시간 압축, 순서 보존)를 MC 시계열(TR 1 s)에서 물을 수 있다. (b) 장면 전환에서 재구성이 실패한다는 동영상 decoding의 한계(arXiv:2410.19452)는 정서 전이 시점의 신호가 불연속적이라는 뜻일 수 있어, Emo-FilM 상태공간 모형의 전이 시점 추정과 대조할 수 있다. 본격적 재정의는 multimodal-dynamics, geometry-info 담당이다.

**Q5. Brain Foundation Model의 latent representation에서 감정 관련 구조를 찾을 수 있는가?**
찾을 수 있는 후보는 있다. 재구성 모델의 공유 latent(MindEye2 4096 공유 공간, Brain-IT brain token)와 전뇌 foundation 해독 모델(WAVE, arXiv:2411.07121)이 그것이다. 다만 이들은 시각 목표로 학습되었으므로 거기서 정서 구조가 보이면 "정서와 무관한 정렬이 정서를 운반한다"는 뜻이다(VD-P8). 정서 고유 구조를 주장하려면 원 voxel 상한, 무작위 latent 하한, 시각-의미 통제를 함께 보고해야 한다. 누수 통제 정서 benchmark가 없다는 encoding-foundation의 지적(arXiv:2601.23090 관련)에 동의한다.

**Q6. Music, Video, Image의 공통 정서 특징과 modality-specific 특징을 뇌 수준에서 구분할 수 있는가?**
image와 video는 우리 데이터로 부분적으로 가능하다. NSD(정지 이미지)로 학습한 decoder를 Horikawa, MC(무음 영상) 프레임과 Emo-FilM, Spacetop(소리 있는 영상)에 적용하면 "시각만으로 복원되는 정서"와 "소리가 있어야 생기는 정서"의 차이를 decoding 손실의 차이로 볼 수 있다. MC 회상은 "자극이 없는" 네 번째 조건을 더한다. music은 Emo-FilM 사운드트랙뿐이라 내 범위에서 직접 다루기 어렵다. 라벨 비호환(Stage 1 수준 2~3) 때문에 비교는 공통 feature 공간이나 RSA 수준으로 한정된다.

**Q7. 정서 관련 계산을 AI architecture의 구조적 제약으로 구현할 수 있는가?**
가능한 설계가 있다. Brain-IT은 기능 군집을 token으로 두는 뇌 영감 구조다(arXiv:2510.25976). 여기에 편도체, 섬엽, OFC 군집을 별도 stream으로 두고 시각 token에 cross-attention으로 연결하면, Kragel 2021의 low road, high road, top-down 3성분(doi:10.1016/j.neuron.2021.06.001)을 구조적 사전으로 넣은 decoder가 된다. attention 맵이 "어느 stream이 어떤 이미지 feature를 공급하는가"를 해석 지표로 준다. 다만 이것은 decoder 설계이지 뇌의 계산 증명이 아니다. imagery 일반화에는 선형, 저차원 구조가 유리하다는 MIRAGE 결과(arXiv:2605.17198)도 구조 제약의 한 예다.

**Q8. 정서 라벨이 없는 NSD도 representation alignment로 의미 있게 쓸 수 있는가?**
쓸 수 있다. 가장 직접적인 다리는 NSD로 학습된 재구성 모델이다. MindEye2는 공유 자극 없이 새 피험자를 공유 latent에 선형 정렬한다(arXiv:2403.11207, 2.1절). 이를 Horikawa, MC에 적응시키면 NSD의 대규모 시각 사전학습을 정서 라벨이 있는 데이터에서 읽을 수 있다. NSD-Imagery는 같은 피험자의 imagery 조건을 준다(arXiv:2506.06898). 주의할 점: NSD의 amygdala는 반복 제시와 기억 과제로 비정상적이다(doi:10.1038/s41467-024-49073-8, Discussion 6째 단락). AI 추정 정서 라벨로 NSD 지도를 만들면 무작위 인간 gold 표본으로 PPI 보정이 필요하다(doi:10.1126/science.adi6000). COCO는 대다수 VLM 학습 분포 안에 있어 사전학습 오염 위험이 있다.

---

## 5. Axis 결정에 대한 의견

* **W 채택에 동의한다.** 사용자가 MC를 보유해 데이터 조건이 충족되었다. 하위 구성으로 다음을 제안한다. (1) Perception-to-Imagery Cross-decoding(G에서 이동, G에는 교차 표시), (2) Recall Reinstatement Fidelity and Vividness, (3) Valence-dependent Recapitulation(NEVER 계열, doi:10.3758/s13423-017-1313-9, doi:10.1523/JNEUROSCI.2834-18.2019, doi:10.1523/JNEUROSCI.0718-25.2025), (4) Cued vs Spontaneous Generation(MC는 cued만 있음을 표시), (5) Repetition and Re-exposure(MC 5회 반복, NSD 3회 반복, Spacetop shortvideo 재노출, doi:10.1523/JNEUROSCI.2406-23.2025).
* **U에 "annotation instruction"을 provenance 속성으로 넣자고 제안한다.** 같은 별도 평정자라도 "시각 내용만 써라"(MC 캡션)와 "느낀 정서를 써라"(C&K 평정)는 다른 라벨을 만든다. 내 Round 1 S6(Annotation Instruction as Stimulus Descriptor)은 B에 두되, U의 provenance 표기 항목에 "지시문"을 추가하는 것이 일관적이다.
* **Y를 A의 Sub-axis로 둔 결정에는 이견이 없다.** 다만 MC의 시행별 vividness가 Y의 유일한 시행 단위 데이터이므로(VD-P6), axis_encyclopedia 2.2절 Y 행의 "데이터 제약" 문구에 "MC 회상 vividness(심상의 질에 대한 내성 보고, 정서 보고는 아님)"를 추가하기를 권한다.
* **X를 R의 Sub-axis로 둔 결정에도 이견이 없다.** VD-P8은 X(Machine Affect Representations)에 "뇌 decoding 모델의 공유 latent"를 비교 대상으로 추가한다.

---

## 6. 새로움 주장의 검색 경로

Stage 2 표본에서 "no" 판정의 25%가 과대였다는 교훈에 따라, 이 문서에서 새로움을 주장하거나 판정을 바꾼 항목의 검색 경로를 적는다(2026-11-12).

| 항목 | 검색 경로와 질의 | 결과 | 판정 |
|---|---|---|---|
| R1 재구성 이미지의 정서 충실도 평가 | WebSearch "brain decoding image reconstruction emotion evaluation valence of reconstructed images fMRI 2026"; WebSearch "fMRI decoding amygdala insula voxels added to visual cortex reconstruction ... emotional images"; PubMed `(image reconstruction[tiab] OR reconstructed images[tiab]) AND fMRI AND (emotion*[tiab] OR affective[tiab] OR valence[tiab])` (2022~); Round 1의 arXiv API 질의 2건. arXiv API는 이번 라운드에 rate limit으로 재질의 실패 | 재구성 이미지 정서를 평가한 연구 없음. 가장 가까운 것은 EmoMind(캡션, arXiv:2605.16739). Bo 2021(doi:10.1093/cercor/bhaa411)은 시각피질 정서 decoding과 편도체 재진입(재구성 아님) | no (검색 범위 내) 유지 |
| R2 정서가에 따른 재현(NEVER) | PubMed `(encoding-retrieval similarity OR recapitulation OR "pattern reinstatement") AND (negative OR valence OR emotional) AND fMRI` (2013~), PubMed `(mental imagery OR recall) AND (reinstatement OR cross-decoding OR "perception and imagery") AND (emotion* OR valence) AND fMRI` (2016~) | Kark & Kensinger 2019, Cocquyt 2026, Bowen & Kensinger 2017(Neuroreport, 존재만 확인), Riegel 2022(NeuroImage, 존재만 확인) | **no → partially** 정정. 자연 영상 회상의 feature 수준별 비교는 미발견 |
| VD-P6 vividness와 재활성 | PubMed `vividness AND imagery AND (neural overlap OR perception) AND decoding AND fMRI` (2015~), PubMed 저자 질의 Dijkstra N | Dijkstra 2017(비정서), Cabbai 2024, Koenig-Robert & Pearson 2019(Sci Rep, 존재만 확인) | 기본 대응은 yes(선행). 정서에 따른 조절은 no (검색 범위 내) |
| R3/VD-P2 정서 범주 hold-out zero-shot | WebSearch "zero-shot decoding unseen emotion categories fMRI held-out emotion category generalization semantic space"; geometry-info round1 I2의 검색 기록 | 시각 범주 zero-shot(Akamatsu 2023 등)만 있음 | no (검색 범위 내). geometry-info 판정과 일치 |
| R4 정서 영역 생성 제어 | `literature_db.csv`의 NeuroVolve 기록(generative-counterfactual 확인) | 실측 검증까지 수행, 의미 교란 | partially |
| VD-P4 생성기 정서 중립화 audit | 별도 검색하지 않음 | | 새로움은 "정서 축으로 측정"에 한정하고 주장 수위를 낮춤 |

---

## 7. 검증된 것과 미확인 사항

### 검증됨
* MC 설계 사실(TE 30 ms, 동일 순서, 회상 cue가 캡션, 회상 직후 비디오 재제시, 일본어 모국어 피험자): MC 논문 본문(Round 1에서 내려받은 PMC 전문)에서 재확인.
* 새로 추가한 7편: PubMed 메타데이터로 서지와 초록 확인. Kark & Kensinger 2019는 Discussion 앞부분 본문 확인.
* 이 문서에서 인용한 다른 에이전트 출처 ID(arXiv:2512.00557, arXiv:2409.06843, doi:10.1016/j.cell.2020.09.031, arXiv:2605.04326, doi:10.1371/journal.pone.0152719, arXiv:2408.13718, arXiv:2405.12661, doi:10.1016/j.neuron.2021.06.001, arXiv:2609.34742, arXiv:2405.07987, doi:10.1093/nc/nix007, doi:10.1371/journal.pcbi.1011943, arXiv:2607.19327, doi:10.1126/science.adi6000, doi:10.1073/pnas.1912334117)가 `literature_db.csv`에 있음을 확인.

### 미확인
* 사용자 보유 MC 파일의 실제 구성(테스트 반복 데이터, 회상 시행별 vividness 값, 캡션 20개 포함 여부).
* MC 72 테스트 클립의 C&K 정서 분포(VD-P1, VD-P2, VD-P6 검정력의 전제).
* Horikawa 2020과 MC 사이 피험자 중복 여부.
* Horikawa 2020의 실제 TE와 영역별 tSNR(systems-neuro 판정 인용, 직접 계산 안 함).
* EmoSet 데이터와 학습 가중치의 공개 조건, MindEye2와 Brain-IT checkpoint 라이선스.
* arXiv API 재질의는 rate limit으로 이번 라운드에 실패했다. R1의 "no" 판정은 WebSearch와 PubMed 기준이다.
