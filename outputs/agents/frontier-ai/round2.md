# Round 2 (Cross-Agent Exchange): frontier-ai

* 에이전트: frontier-ai (Axis I, J, R). 제안 ID 접두어: FA
* 기준일: 2026-11-12
* 절차: `reference/protocols.md` P2 + Coordinator 위임 메시지의 추가 요구
* 읽은 것: 다른 10개 에이전트의 `round1.md`(0, 1, 3, 4절 전부, 6절은 chain 제목 전부와 관련 chain 본문: multimodal-dynamics Chain 2, llm-semantics Chain 3), `outputs/axis_encyclopedia.md`(0절, 2절), `outputs/STAGE_STATUS.md` 사용자 결정 기록, `outputs/literature/literature_db.csv`(인용 ID 대조)
* 바뀐 전제 반영: 데이터셋 5개(Horikawa 2020, Emo-FilM, Spacetop, NSD, Mind captioning ds005191). Axis U, V, W 독립 채택, X(Machine Affect Representations)는 Axis R의 Sub-axis.
* 표기: 근거 ID는 `literature_db.csv`의 verified 항목이거나 이번에 식별자 경로로 새로 확인해 내 `literature.jsonl`에 추가한 것(4편: arXiv:2510.04064, arXiv:2510.22042, doi:10.52202/085713-3208, arXiv:2512.06232)이다. 검색 색인으로만 본 것은 [search_index]로 표시한다.
* 태그(axis_encyclopedia 0.2절): label-provenance, evidence-level(R0 상관 / R1 모델 내 개입 / R2 새 행동 평정 / R3 새 fMRI 자극 조작 / R4 뇌 개입), insilico-vs-observed, G1.

---

## 0. Round 1 이후 내 기록의 정정과 갱신 (먼저 적는다)

| # | 내용 | 근거 | 영향 |
|---|---|---|---|
| E1 | Garrido 2025(arXiv:2502.11831) FD3 "영아 시점 비디오 학습"은 **yes**로 수정되었고 동의한다. Su, Legris, Gureckis (arXiv:2512.06232)가 V-JEPA를 SAYCam으로 학습했고 IntPhys2 성능이 유의하게 오르지 않았다(초록, arxiv.org abs 페이지로 확인) | arXiv:2512.06232 | 내 jsonl에 해당 논문 추가. "학습 분포만으로 예측 능력이 생기지 않는다"는 결과는 FA-P3의 모델 surprise 해석에 주의점이 된다 |
| E2 | **V-JEPA 2 라이선스 기록이 에이전트 간에 충돌한다.** 내가 직접 연 GitHub 저장소 LICENSE와 README는 "대부분 MIT, 일부 파일 별도 조건"이다. MIRAGE(arXiv:2605.29850) 표 3은 V-JEPA 2를 **CC-BY-NC 4.0**으로 적었고(이번에 PDF로 직접 확인), encoding-foundation은 이를 따랐다. brain-inspired는 검색 수준으로 "체크포인트별 MIT/Apache-2.0 혼재"로 적었다. 가중치 라이선스가 담긴 huggingface.co 모델 카드는 열지 못했다 | 저장소 LICENSE(커밋 2026-03-23), arXiv:2605.29850 표 3 | 지우지 않고 이견으로 기록한다. 확인 전까지는 **가중치를 비상업 조건으로 가정**하는 보수적 처리를 권한다 |
| E3 | **LLM 정서 표상의 "지속성"에 반대 보고가 있다.** Round 1 CH3과 T5는 Sofroniew 2026(arXiv:2604.07729 5.3절)의 "국소적, 비지속" 결론을 AI 쪽 기준으로 썼다. 그런데 Zhang et al. 2025(arXiv:2510.04064, 초록)는 초기 정서 톤이 수백 token 뒤에도 탐지된다며 "지속적"이라고 보고했다. 두 결과는 probe 설계가 다르다. 후속 위치에서 초기 톤이 탐지되는 것은 Sofroniew가 말한 attention 재호출로도 설명된다 | arXiv:2604.07729, arXiv:2510.04064 | CH3의 비교 기준을 "LLM은 국소적"으로 고정하지 않는다. "지속 상태(state) vs 재호출(recall)"을 구분하는 같은 검정을 모델과 뇌에 함께 적용하는 설계로 바꾼다(FA-P3) |
| E4 | **SAE 기반 뇌 encoding은 내가 Round 1에서 쓴 것보다 먼저 출판되었다.** Zeng & Gallant (NeurIPS 2025, doi:10.52202/085713-3208, Crossref 확인, 본문은 bioRxiv 429로 미열람)는 dense embedding을 sparse concept atom으로 사상하는 encoding model을 이야기 청취 fMRI에 적용했다(검색 요약 기준) | doi:10.52202/085713-3208, arXiv:2606.06857 | Round 1 U4와 CH5의 새로움은 "비디오, 정서 영역, 재학습 안정성, 다모델 공유 사전"으로 한정한다 |
| E5 | 모델 내부에서 "의미를 보존한 정서 steering"이 이미 보고되었다(Reichman et al. 2025, arXiv:2510.22042, 초록) | arXiv:2510.22042 | FA-P2의 근거로 사용. 단 모델 내 개입(R1)이다 |

---

## 1. 가져온 아이디어

### IM1. 정서를 쓰지 말라는 지시로 받은 인간 캡션과 반복 클립 (vision-decoding, llm-semantics)
* 출처: vision-decoding round1 0.1절, R6; llm-semantics Chain 1. 논문 doi:10.1126/sciadv.adw1464 (Horikawa 2025 Mind captioning).
* 가져와서 바꾸는 것: Round 1 T4(정서 vs 상황 판별 검정)와 CH5(SAE 개념)의 "상황, 기술 의미" 기준선을 **AI 캡션이 아니라 인간 중립 캡션**으로 정의할 수 있다. 같은 Cowen & Keltner 비디오에 대한 두 코호트(Horikawa 2020의 5명, Mind captioning의 6명)는 같은 자극 2,180개에 11명이며, Mind captioning의 72개 클립 x 5회 반복으로 개념 수준 encoding의 noise ceiling을 처음으로 구할 수 있다. 회상 imagery는 "자극이 없을 때 모델 feature의 어떤 성분이 재활성되는가"를 묻게 해 준다(FA-P1, FA-P6에 반영).
* 주의: 저장소에 실제로 캡션, 회상, vividness 파일이 있는지는 미확인(사용자 결정 기록). 두 코호트의 피험자 중복 여부도 미확인(vision-decoding 지적).

### IM2. Emo-FilM 평정자는 같은 영화를 최대 6번 봤다: "예측성" 평정은 첫 시청의 예측이 아니다 (multimodal-dynamics)
* 출처: multimodal-dynamics round1 4절 개념 5, Chain 2 안전장치. 논문 doi:10.7554/eLife.64972 (Lee, Aly, Baldassano 2021: 반복 시청 시 뇌 사건 경계가 앞당겨짐).
* 가져와서 바꾸는 것: Round 1 CH2와 T1은 Emo-FilM의 Suddenly, Predictable appraisal 평정을 "예측오차의 인간 측정치"로 썼다. 그러나 평정자는 결말을 아는 상태로 평정했을 수 있다. 그래서 (a) fMRI 참가자(첫 시청)의 뇌 반응과 모델 surprise의 결합을 일차 분석으로 두고, (b) 평정은 "결말을 아는 관찰자의 appraisal"로 표기하며, (c) 평정과 모델 surprise의 시간 차(앞당김)를 별도 변수로 추정한다(FA-P3).

### IM3. 불완전하게 측정된 공변량의 잔여 교란 (adversarial-reviewer)
* 출처: adversarial-reviewer round1 1절 U1, chain D2. 논문 doi:10.1371/journal.pone.0152719 (Westfall & Yarkoni 2016).
* 가져와서 바꾸는 것: Round 1 CH1("world model 전이 구조를 통제한 뒤에도 정서 지도가 남는가")과 CH5는 "통제 후 남는 분산"을 정서의 증거로 썼다. world model feature도 상황의 불완전한 측정치이므로, 남은 분산은 잔여 교란일 수 있다. 공변량 feature 가족을 늘려 가며 정서 고유 분산이 포화하는 곡선(D2 방식)을 보고하고, 단일 통제 결과로 결론 내리지 않는다.

### IM4. 정답을 심은 합성 뇌로 분석 pipeline 검증 (encoding-foundation, adversarial-reviewer)
* 출처: encoding-foundation round1 3절 I5, adversarial-reviewer U4. 논문 arXiv:2302.06677 (Han, Poggio, Cheung 2023), arXiv:2605.04326 (TRIBE v2).
* 가져와서 바꾸는 것: SAE 개념 encoding(CH5)과 정서 vector 운반(CH6)은 새 분석이라 위양성 위험을 모른다. TRIBE v2 합성 반응에 알려진 정서 패턴을 정해진 SNR로 심고 우리 pipeline이 그것을 개념 수준에서 회복하는지, 시각-의미 공선성 아래에서 거짓 개념을 만드는지 먼저 시험한다(FA-P1, FA-P8).

### IM5. 결론 수준 사다리와 "예측은 개입이 아니다" (generative-counterfactual)
* 출처: generative-counterfactual round1 0절, 4절 C1. 논문 arXiv:2609.27729 (Rothermel 2026), arXiv:2605.16468 (Grosbard 2026, 모델 내 인과와 뇌에 대한 결론을 구분).
* 가져와서 바꾸는 것: Round 1의 steering, LLM appraisal 조작(CH4), 정서 vector 운반(CH6)은 모두 **R1**이다. 관찰 fMRI와의 결합은 R0다. 각 제안에 evidence-level을 붙이고, 새 fMRI 없이 R0의 해석력을 높이는 방법으로 **생성 대신 선택(selection)**을 우선한다(Tuckute et al. doi:10.1038/s41562-023-01783-7의 선택 기반 구동을 정서에 옮김, FA-P2).

### IM6. 전역 신호의 자율신경 성분 (systems-neuro)
* 출처: systems-neuro round1 U2, 4절 C1. 논문 doi:10.1038/s41593-025-01945-y (Bolt 2025).
* 가져와서 바꾸는 것: 모델 surprise, 장면 컷, 음량 급변은 모두 각성 반응과 전역 BOLD를 함께 올린다. Round 1 CH2의 "latent 예측오차의 정서 영역 고유 분산"은 전역 신호와 참가자 생리(Emo-FilM PPG, 호흡, EDA)를 공변량으로 넣은 판과 넣지 않은 판을 함께 보고해야 한다. 제공 전처리본의 WM/CSF 회귀가 이 성분을 일부 지웠을 수 있으므로 raw 재전처리 판과 비교한다.

### IM7. 방향성 전이와 successor representation (brain-inspired, geometry-info)
* 출처: brain-inspired P-1, I-2; geometry-info P2, C2. 논문 doi:10.1073/pnas.1616056114 (Thornton & Tamir 2017), doi:10.1038/nn.4650 (Stachenfeld 2017).
* 가져와서 바꾸는 것: Round 1 CH1의 world model "전이 행렬"을 대칭 유사도가 아니라 **방향성** 전이로 정의한다. V-JEPA 2 predictor는 과거에서 미래로만 예측하므로 latent 상태 사이의 비대칭 전이를 자연스럽게 준다. 정서 평정의 실제 전이(비대칭)와 world model 상태 전이(비대칭)를 같은 SR 틀로 비교할 수 있다.

---

## 2. 보내는 제안

각 제안의 "선행 검색"은 이번 라운드에서 실제로 돌린 검색 경로와 결과다. 검색 결과가 없다는 것은 그 경로 안에서 못 찾았다는 뜻이다.

### FA-P1 → encoding-foundation: 개념 수준 simulator-to-real gap
* **제안 내용:** 너희 쪽 **In-silico 정서 기하의 충실도(Chain 1)와 matched-control audit(I4)**를 우리 쪽 **안정 SAE(RA-SAE)와 다모델 공유 사전(USAE)**으로 확장할 수 있다. TRIBE v2의 V-JEPA 2 백본 feature와 TRIBE 예측 피질 반응을 같은 sparse 개념 사전에 넣고, 실측 fMRI에서는 설명되는데 TRIBE 예측에서는 사라지는 개념(또는 그 반대)을 찾는다. EmoMind가 본 "점별 정서 보존, 관계 구조 26%" 해리(arXiv:2605.16739)를 "어떤 개념이 빠져서 생기는가"로 분해한다.
* **구체 분석:** (1) 일반 비디오로 학습한 RA-SAE(재학습 5회)로 V-JEPA 2 feature 분해, (2) 같은 자극의 실측 반응과 TRIBE v2 예측 반응 각각에 Lepori식 소수 feature 선택 encoding, (3) 개념별 "실측 설명력 - in-silico 설명력" 차이 지도, (4) IM4의 정답 주입 검증을 먼저 통과한 pipeline만 사용.
* **관련 Axis:** H, R(Machine Affect Representations는 아님, 개념 분해), F, S, T
* **근거 논문 ID:** arXiv:2605.04326, arXiv:2605.16739, arXiv:2607.16292, arXiv:2502.12892, arXiv:2502.03714, arXiv:2606.06857, doi:10.52202/085713-3208, arXiv:2302.06677
* **가능한 데이터셋:** Mind captioning(72 클립 x 5회 반복으로 noise ceiling, 지각 테스트), Horikawa 2020(2,180 클립), Emo-FilM(시청각, TRIBE v2의 오디오와 텍스트 경로 사용 가능)
* **예상되는 반론:** (a) TRIBE v2 공개 checkpoint는 평균 피험자, 피질만 예측하므로 편도체 등은 비교 불가(encoding-foundation 핵심 메시지 1). (b) SAE 개념의 이름은 사람이나 MLLM이 붙인 해석이며, 개념 수준 차이가 "정서"인지는 별도 검정이 필요. (c) TRIBE v2와 V-JEPA 2의 비상업 라이선스 가능성(E2). (d) Mind captioning 반복 클립은 72개뿐이라 개념 수가 많으면 과적합.
* **label-provenance:** 주 분석 대상은 라벨 없는 뇌 반응(실측 vs in-silico). 개념 해석에 Cowen & Keltner 34/14 평정을 쓸 때는 [별도 평정자 규범, 대상 felt를 평균한 규범]
* **evidence-level:** R0(실측) + R1(in-silico). insilico-vs-observed: 혼합. G1: 필요(보유)
* **선행 검색:** WebSearch "sparse autoencoder concepts brain encoding model TRIBE emotion amygdala fMRI 2026" → TRIBE와 SAE 결합 연구 없음, Zeng & Gallant(언어, doi:10.52202/085713-3208) 발견. arXiv API(Round 1) `abs:"sparse autoencoder" AND abs:fMRI` → SAE-BrainMap(arXiv:2506.11123), Lepori 2026(arXiv:2606.06857), Guo 2026(arXiv:2605.23035): 모두 정적 이미지나 언어. 시각피질 mechanistic encoding의 counterfactual 편집은 Grosbard 2026(arXiv:2605.16468, literature_db verified)이 수행. **판정: partially**(SAE encoding 자체는 수행됨, in-silico vs 실측의 개념 수준 비교와 정서는 미발견)
* overlap: EmoViS (Horikawa 정서 기하의 sensory-semantic 기원, 방향 인접)

### FA-P2 → generative-counterfactual: 생성 대신 선택, 의미 고정 정서 대비 쌍
* **제안 내용:** 너희 쪽 **"의미를 고정해도 emotion 모델 우위가 남는가"(CH1)와 controversial 자극 판정(CH6, X1)**을 우리 쪽 **모델 내부 정서 vector와 인간 중립 캡션 embedding을 이용한 기존 자극 풀 선택**으로 먼저 검증할 수 있다. 생성 편집은 의미를 함께 바꾸므로(NeuroVolve, EmoEdit), 우선 Horikawa와 Mind captioning의 이미 관찰된 2,180 클립 안에서 "인간 중립 캡션 embedding이 가까운데 VLM 정서 vector 투영(또는 규범 평정)이 크게 다른 쌍"과 "정서는 비슷한데 캡션이 먼 쌍"을 골라 실측 fMRI RSA로 판정한다. 그 뒤에 생성 편집은 모델 표상 공간에서 의미 보존 정서 조작(arXiv:2510.22042의 R1 결과)이 가능한 방향으로만 시도한다.
* **관련 Axis:** L, P, R, C, U
* **근거 논문 ID:** arXiv:2512.00557, arXiv:2405.12661, doi:10.1038/s41562-023-01783-7, doi:10.1073/pnas.1912334117, arXiv:2609.34742, arXiv:2510.22042, doi:10.1126/sciadv.adw1464, arXiv:2106.04619, arXiv:2604.13466
* **가능한 데이터셋:** Horikawa 2020 + Mind captioning(같은 자극, 11명), NSD(73k 선택 풀, 정서 범위가 좁음), 새 행동 평정(R2, 선택 쌍의 manipulation check)
* **예상되는 반론:** (a) 자연 자극에서 "의미 가깝고 정서 다른" 쌍은 드물고, 드문 쌍은 특이한 자극이라 일반화가 약하다. (b) 쌍 선택에 쓴 지표(VLM vector, 캡션 embedding)의 측정 오차가 그대로 잔여 교란이 된다(IM3). (c) 쌍 선택과 검정을 같은 피험자로 하면 순환이므로 Horikawa 2020 피험자로 고르고 Mind captioning 피험자로 검정하는 식의 분리가 필요(코호트 간 피험자 중복 미확인). (d) Horikawa 2020 공개 전처리본은 블록 평균이라 쌍 수준 RSA 잡음이 크다.
* **label-provenance:** 쌍 정의는 [AI 추정, 내부 표상] 또는 [별도 평정자 규범]과 [인간 중립 캡션, 기술 의미]. 대상: perceived affective quality 또는 normative felt
* **evidence-level:** R0(선택 쌍의 실측 RSA), R2(새 행동 평정 시). G1: 필요(보유)
* **선행 검색:** generative-counterfactual round1 U1이 "의미를 고정한 정서 단서 조작 연구를 2026-11 검색에서 찾지 못함"으로 기록. 이번에 추가로 WebSearch "hyperalignment trained on neutral ... emotion"(무관), Tuckute 2024의 선택 기반 구동은 언어망 대상. **판정: no (이 검색 경로 안에서). 선택 기반 정서 판정은 encoding-foundation Chain 4(controversial selection)와 부분적으로 겹치므로 공동 설계를 제안**
* overlap: EmoViS (sensory-semantic 기원)

### FA-P3 → multimodal-dynamics: 세 가지 예측 신호와 "지속 상태 vs 재호출"
* **제안 내용:** 너희 쪽 **다중모달 예측 surprise와 정서 경계(Chain 2), 정서 이월(Chain 1, U1), learning progress(4절 개념 4)**를 우리 쪽 **V-JEPA 2 predictor로 같은 모델에서 계산한 세 신호(예측오차 surprise, 예측 불확실성, 학습 진전)**와 **정서 지속성 검정**으로 묶을 수 있다. 세 신호를 한 모델에서 뽑으면 모델 간 차이가 아니라 신호 종류의 차이를 비교할 수 있다. 정서 지속성은 "장면 국소 신호(VLM 정서 vector 투영)를 ROI별 시간 상수로 누적한 leaky integrator"와 "국소 신호 + 과거 장면 재호출 회귀자(과거 장면과의 내용 유사도로 가중)"를 경쟁시켜 "지속 상태"와 "재호출"을 구분한다. 같은 검정을 LLM 쪽(arXiv:2604.07729 vs arXiv:2510.04064의 충돌, E3)에도 적용할 수 있다.
* **관련 Axis:** D, N, I, J, R, M
* **근거 논문 ID:** arXiv:2506.09985, arXiv:2502.11831, arXiv:2512.06232, arXiv:2604.07729, arXiv:2510.04064, doi:10.1126/sciadv.abf7129, doi:10.7554/eLife.64972, arXiv:2407.09450, arXiv:2407.02474, doi:10.1038/s41593-025-01945-y
* **가능한 데이터셋:** Emo-FilM(주, 첫 시청 참가자 fMRI + 생리), Horikawa 2020 raw(연속 블록 이월), Spacetop alignvideo
* **예상되는 반론:** (a) V-JEPA 2 기본 문맥은 16~64 프레임(수 초)이라 서사 수준 예측은 못 한다. 그래서 LLM surprisal(대사, 캡션)을 함께 넣어야 한다. (b) 세 신호가 서로, 그리고 컷, 음량과 공선적이다. (c) 장면 컷과 각성은 전역 신호를 올린다(IM6). (d) 평정자의 반복 시청(IM2) 때문에 평정과 모델 신호의 시간 정렬이 어긋난다. (e) 학습 분포의 한계: 직관 물리조차 데이터 분포만으로 안 생긴다는 보고(arXiv:2512.06232)가 있어 사회, 정서적 규칙성 예측을 V-JEPA에 기대하기 어렵다. 이 경우 "latent 물리 예측오차"로만 해석을 한정한다.
* **label-provenance:** 일차 분석은 라벨 없는 [참가자 뇌 + 참가자 생리]와 [모델 신호]. 평정 사용 시 [별도 평정자 규범, felt, 반복 시청자]
* **evidence-level:** R0. insilico-vs-observed: 관찰(모델 신호는 자극 기술자). G1: 필요(보유)
* **선행 검색:** WebSearch "V-JEPA latent prediction error surprise fMRI brain movie watching"(Round 1) → 직접 연구 없음. WebSearch "'world model' OR 'video prediction' surprise regressor fMRI naturalistic movie emotion amygdala insula 2025 2026"(이번) → 없음, surprise 평정과 DMN 연구(2021)만. multimodal-dynamics Chain 2는 학회 초록 2건(search_index)으로 partially 판정. VALOR(doi:10.7554/eLife.107607)는 video-text 미래 feature(본문 미열람). **판정: partially (예측 신호와 영화 fMRI 결합은 부분 선행, V-JEPA predictor 기반 세 신호 분리와 정서 지속성 검정은 미발견)**
* overlap: Emo-FilM 연구 (시간 정보 기여 분석)

### FA-P4 → brain-inspired: 묘사된 행동 vs 느낀 행동 경향 (Axis V)
* **제안 내용:** 너희 쪽 **"정서 범주인가, 행동 경향인가"(Chain 2, P-2)와 world model 불확실성 기반 arousal(I-4)**를 우리 쪽 **latent action model(LAPA의 latent action quantizer)과 V-JEPA 2-AC 계열 행동 조건 표상**으로 검증, 확장할 수 있다. latent action은 화면 속 인물과 카메라의 움직임, 즉 **묘사된 행동(portrayed action)**을 라벨 없이 준다. Emo-FilM Motivation 10항목은 평정자가 **느낀 행동 경향(felt action tendency)**이다. 두 변수가 같은 뇌 분산을 설명하는지, 갈리는지를 보면 Axis V 안에서 "묘사 vs 경험"이라는 Axis U의 구분을 행동 성분에 적용할 수 있다. 예: 인물이 도망치는 장면(묘사된 회피)과 관객이 다가가 돕고 싶은 장면(느낀 접근, Care, Support)은 갈린다.
* **관련 Axis:** V, U, I, B, E
* **근거 논문 ID:** arXiv:2410.11758, arXiv:2506.09985, doi:10.1073/pnas.2414005122, doi:10.1016/j.isci.2020.101060, arXiv:2407.02474, arXiv:2502.11831
* **가능한 데이터셋:** Emo-FilM(Motivation 10항목 1 Hz 평정, 첫 시청 fMRI), Horikawa 2020 / Mind captioning(행동 경향 라벨은 없으므로 latent action만, 또는 MLLM 주석 [AI 추정])
* **예상되는 반론:** (a) LAPA의 학습 분포(로봇, 손 조작)와 영화 장면의 도메인 차이. latent action이 카메라 움직임을 포착한다는 저자 보고 때문에 편집과 카메라 이동을 nuisance로 통제해야 한다. (b) 운동 관련 BOLD는 시청자의 눈 움직임, 미세 움직임과 섞인다. (c) Motivation 항목의 평정자 일치가 낮을 수 있다(항목별 0.21~0.60 범위, Stage 1). (d) affordance가 장면 구조(PPA, OPA)로 환원될 수 있다(Bartnik 2025는 환원되지 않는다고 보고).
* **label-provenance:** latent action은 [자극 기술자, portrayed]. Motivation 항목은 [별도 평정자 규범, felt]. 둘의 대비가 핵심
* **evidence-level:** R0. G1: 필요(보유)
* **선행 검색:** WebSearch "latent action model video features fMRI action tendency approach avoidance naturalistic movie brain encoding"(이번) → latent action을 encoding feature로 쓴 연구 없음, 사회 행동 feature(McMahon 2023 계열)만. **판정: no (이 검색 경로 안에서)**. 단 brain-inspired 재점검에서 Mohammadi 2023(doi:10.1093/cercor/bhad093)이 CPM 행동 경향 성분의 신경망을 보고했으므로 "행동 경향의 신경 표상" 자체는 partially

### FA-P5 → emotion-theory: 관점 무차별 모델을 기준선으로 한 인식 vs 경험 분리
* **제안 내용:** 너희 쪽 **인식(귀속) vs 경험(느낌)의 분기(U3), privileged access 검정(T4, C4), self-tagging monitoring(X3)**을 우리 쪽 **"관점 무차별(perspective-free)" 모델 정서 표상**을 기준선으로 써서 검증할 수 있다. LLM 정서 vector는 사용자, 가상 인물, Assistant에 같은 기제로 작동한다(arXiv:2604.07729, 5.2~5.3절). 그러면 모델 정서 vector로 설명되는 뇌 분산은 "누구의 정서인지와 무관한 정서 개념"의 몫이고, 같은 참가자에서 자기 경험 조건(Spacetop alignvideo 사후 평정)에만 남는 잔차가 self-tagging 후보가 된다. 귀속 조건(shortvideo mentalizing, faces 표정 지각)과의 대비로 "관점 결속(perspective binding)"을 측정 변수로 만든다.
* **관련 Axis:** U, A(Introspective Access Sub-axis), R(Machine Affect Representations Sub-axis), C, E
* **근거 논문 ID:** arXiv:2604.07729, doi:10.1162/imag_a_00517, doi:10.1073/pnas.1619316114, arXiv:2410.13787, arXiv:2408.13718, arXiv:2609.34742
* **가능한 데이터셋:** Spacetop(같은 참가자에게 자기 경험, 타인 귀속, 표정 지각), Emo-FilM(규범 felt vs 참가자 사후 클립 평정의 부분 비교)
* **예상되는 반론:** (a) Spacetop 세 과제는 자극 종류가 달라 과제 차이가 관점 차이와 섞인다. (b) alignvideo 평정 약 51% 결측과 평정 구간의 HRF 중첩. (c) 모델 정서 vector는 텍스트 이야기에서 추출했으므로 비디오에 쓰려면 VLM 판(arXiv:2609.34742 방식)이 필요하고 그 자체가 AI 추정이다. (d) 잔차가 self-tagging이 아니라 개인 시각 처리 차이일 수 있다(vision-decoding L2 논리).
* **label-provenance:** 자기 경험 [참가자 본인, felt], 귀속 [참가자 본인, portrayed/perceived], 모델 vector [AI 추정, 내부 표상]
* **evidence-level:** R0. G1: 필요(보유)
* **선행 검색:** WebSearch "LLM internal emotion representation probing versus verbal emotion ratings predict human brain fMRI"(이번) → 관점 결속을 모델 기준선으로 쓴 연구 없음. emotion-theory는 동일 계열의 공감 공포 vs 주관 공포 signature 분리(doi:10.1016/j.bpsc.2025.11.011, 초록)를 U3 보강으로 기록[emotion-theory 기록, literature_db 개별 행 없음, 내가 확인하지 않음]. **판정: partially (인식 vs 경험 signature 분리는 선행, 관점 무차별 모델 기준선은 미발견)**

### FA-P6 → llm-semantics: 내부 표상 읽기 vs 출력 묻기 (L2 층의 두 측정)
* **제안 내용:** 너희 쪽 **세 층 분해(L1 기술 / L2 귀속 / L3 경험)와 Chain 1(정서 배제 기술의 잔차)**을 우리 쪽 **모델 내부 정서 표상(probe 투영)과 모델 출력(평정, odd-one-out)의 비교**로 확장할 수 있다. 같은 open VLM에서 (a) 정서를 묻고 답한 출력(Du 2025식 출력 기반 embedding), (b) 답하기 전 hidden state를 정서 vector에 투영한 값을 만들고, Mind captioning 인간 중립 캡션 embedding(L1)을 통제한 뒤 어느 쪽이 뇌 분산을 더 설명하는지, 어느 쪽이 "과도하게 범주적"인지(arXiv:2508.05880) 비교한다. LLM에서는 내부 probe가 zero-shot 출력보다 정서 정보가 많다는 보고가 있다(arXiv:2510.04064, 초록).
* **관련 Axis:** C, U, R(Machine Affect Representations), Q, K
* **근거 논문 ID:** arXiv:2509.24298, arXiv:2510.04064, arXiv:2508.05880, arXiv:2609.34742, doi:10.1126/sciadv.adw1464, arXiv:2408.13718, doi:10.1038/s42256-025-01072-0
* **가능한 데이터셋:** Horikawa 2020 + Mind captioning(같은 2,180 클립, 인간 중립 캡션), Emo-FilM(연속, 시간 해상도별 비교)
* **예상되는 반론:** (a) 내부 vector도 결국 모델이 만든 것이고, 추출에 쓴 합성 자극의 provenance가 AI다. (b) 출력 기반 embedding(odd-one-out)은 수백만 판단이 필요해 비용이 크다. Du 2025 결과를 기준선으로 재사용하면 모델이 달라 비교가 깨진다. (c) Qwen 계열 학습 데이터에 Cowen & Keltner 자극이 들어갔을 가능성(오염).
* **label-provenance:** 제안: Axis U의 "AI 추정"을 **[AI 추정, 출력(verbalized)]**과 **[AI 추정, 내부 표상(probe)]**으로 나눈다(4절 참조). L1은 [인간 중립 캡션, 기술 의미]
* **evidence-level:** R0. G1: 필요(보유)
* **선행 검색:** WebSearch "LLM internal emotion representation probing versus verbal emotion ratings predict human brain fMRI"(이번) → 내부 probe와 출력을 fMRI 예측에서 직접 비교한 연구 없음. LLM 정서 vector가 MEG를 예측한다는 NeuroLang 2026 포스터가 보였으나 [search_index], 서지 미확인. **판정: no (fMRI 기준), MEG는 미확인 선행 가능성**

### FA-P7 → geometry-info: 정서와 무관한 정렬이 정서 기하를 운반하는가 (사람 사이, 모델-뇌 사이)
* **제안 내용:** 너희 쪽 **수렴 기울기(I8, Platonic hypothesis 적용)와 rank 분해 공유 스펙트럼(C1)**을 우리 쪽 **Xing 2026의 "정서 무관 정렬의 정서 운반" 검정**으로 확장할 수 있다. 두 방향: (a) 사람 사이: 저정서 클립(규범 평정 기준 하위)으로만 피험자 간 정렬(hyperalignment, Procrustes)을 학습하고, 고정서 클립의 정서 기하가 운반되는지 본다. (b) 모델-뇌 사이: 저정서 자극으로 학습한 VLM→뇌 사상에 VLM consensus 정서 vector를 통과시켜 고정서 자극의 뇌 패턴 차이를 예측한다. 운반 실패의 크기를 "정서 특이 정렬의 필요량"으로 정의하면 너희 쪽 개인 특이성 지수(I7의 미운반 질량)와 같은 척도로 비교된다.
* **관련 Axis:** K, O, R, S, I
* **근거 논문 ID:** arXiv:2609.34742, arXiv:2405.07987, arXiv:2605.20496, arXiv:2409.06843, doi:10.1126/sciadv.abf7129
* **가능한 데이터셋:** Horikawa 2020 + Mind captioning(같은 자극 11명, 사람 사이 정렬), NSD(모델-뇌 사상 학습, nsdmeadows 100장 참가자 평정으로 시험)
* **예상되는 반론:** (a) Cowen & Keltner 비디오는 정서 유발용이라 "저정서" 클립이 적고, 저정서 클립은 내용 분포도 다르다(정렬 실패가 정서 때문인지 내용 분포 이동 때문인지 섞임). 내용 분포를 맞춘 대조 분할이 필요. (b) Horikawa 공개 전처리본은 native volume이라 피험자 간 정렬 전에 공간 표준화 필요. (c) NSD는 정서 범위가 좁고 COCO 오염.
* **label-provenance:** 저정서/고정서 분할에 [별도 평정자 규범] 사용, NSD 시험은 [참가자 본인으로 보이는 평정, 지시문 미확인]
* **evidence-level:** R0. G1: (a) 불필요, (b) 필요(보유)
* **선행 검색:** WebSearch "hyperalignment trained on neutral movie segments transfers emotion representation across subjects fMRI"(이번) → 중립 구간만으로 학습한 정렬의 정서 운반 검정은 없음, 예고편으로 정렬하고 사진으로 정서 분류기를 학습한 연구만 확인(search_index). Xing 2026은 VLM 사이에서만 수행. **판정: no (뇌 기준, 이 검색 경로 안에서)**

### FA-P8 → adversarial-reviewer: 개념 수준, 모델 내부 기반 주장의 최소 검증 요건 추가
* **제안 내용:** 너희 쪽 **최소 검증 요건 7항목(7.4절)과 Model Identifiability, Leakage Audit Sub-axis**를 우리 쪽 **해석 도구 특유의 위험 3가지**로 확장할 수 있다. (1) **사전 재현성:** SAE나 정서 vector로 내린 개념 수준 결론은 재학습(시드, 사전 크기, 학습 데이터)에 걸친 일치율을 보고한다(arXiv:2502.12892). (2) **정답 주입 회복:** TRIBE v2 합성 반응에 알려진 신호를 심어 pipeline이 회복하는지, 거짓 개념을 만드는지 보고한다(arXiv:2302.06677). (3) **matched-complexity null for steering/transport:** 정서 vector 대신 같은 노름의 무작위 방향, 내용 방향(객체 범주)으로 같은 분석을 돌린 결과를 함께 보고한다.
* **관련 Axis:** T, R, Q, S
* **근거 논문 ID:** arXiv:2502.12892, arXiv:2604.03919, arXiv:2302.06677, arXiv:2605.04326, arXiv:2609.34742, doi:10.1038/s41467-024-53147-y
* **가능한 데이터셋:** 모든 데이터셋(방법론 인프라)
* **예상되는 반론:** 요건이 늘면 탐색 단계의 비용이 크다. 대응: 탐색 결과에는 요건 충족 여부만 표시하고 버리지 않는다(minimum-validation 태그와 같은 방식).
* **label-provenance:** 해당 없음(방법론). **evidence-level:** 해당 없음
* **선행 검색:** adversarial-reviewer round1의 7항목에 SAE 안정성과 steering null이 없음을 확인(문서 대조). 외부 검색은 하지 않음

---

## 3. 받은 제안에 대한 응답

작성: 2026-11-12. 받은 제안 8개(ET-P7, VD-P8, EF-P5, MD-P5, GI-P8, GC-P6, LS-P4, BI-P2)와 참조로 언급된 2개(GI-P3, BI-P5)의 원문을 보낸 에이전트의 round2.md 2절에서 읽고 답한다. 집계: **수용 4(EF-P5, MD-P5, GI-P8, BI-P2), 수정 4(ET-P7, LS-P4, VD-P8, GC-P6), 반박 0**(GC-P6의 1번 항목 일부는 반박을 포함한 수정).

### 3.1 관점 결속 묶음: ET-P7, LS-P4 (그리고 내가 보낸 FA-P5)
세 제안은 같은 질문(Spacetop 같은 참가자의 자기 경험 / 타인 귀속 / 표정 지각에서 정서 방향이 공유되는가, 모델의 인물 무차별성과 무엇이 다른가)을 서로 다른 쪽에서 냈다. 하나의 공동 설계로 합칠 것을 제안한다.

**ET-P7 (emotion-theory → frontier-ai): 수정**
* 수용하는 부분: (a) alignvideo 본인 평정 축의 shortvideo, faces 교차 일반화, (b) 일반화되지 않는 자기 특이 성분의 위치, 그리고 제안자 스스로 든 반론 1(같은 과제 쌍의 비정서 성분 교차 일반화를 대조로 둘 것)은 그대로 받는다.
* 수정 1 (모델 쪽 검정을 둘로 나눈다): (c)는 "관점 프롬프트 간 정서 vector의 유사도"만 잰다. 그런데 Sofroniew 2026 5.1절은 인물에의 정서 결속이 선형 residual probe가 아니라 결합 표상이나 KV cache에 있을 수 있다고 적었다(arXiv:2604.07729). 그래서 같은 activation에서 (c1) 정서 vector가 관점 간에 공유되는가와 (c2) "누구의 정서인가"(관점 라벨)가 선형으로 decoding되는가를 함께 잰다. (c1) 공유 + (c2) decoding 가능이면 모델은 관점을 표상하되 정서 방향과 분리해 둔 것이고, (c1) 공유 + (c2) 불가면 진짜 무차별이다. 뇌 쪽에도 같은 두 검정을 적용해야 대칭 비교가 된다.
* 수정 2 (대조 null): 모델 쪽에도 "정서 무관 속성(예: 인물 수, 실내외)의 방향이 관점 간에 얼마나 공유되는가"를 기준선으로 둔다. 정서 방향의 공유가 이 기준선보다 높을 때만 "정서 특이 무차별"로 해석한다.
* 근거: arXiv:2604.07729(5.1, 5.3절), arXiv:2609.34742, doi:10.1523/JNEUROSCI.1676-14.2014, doi:10.1162/imag_a_00517
* 역할 분담 제안: emotion-theory가 뇌 쪽 교차 일반화와 비정서 대조, llm-semantics가 관점 조건 프롬프트 설계와 출력 쪽, frontier-ai가 내부 표상 추출(c1, c2)과 matched null.

**LS-P4 (llm-semantics → frontier-ai): 수정**
* 수용하는 부분: "모델 먼저(R1), 뇌 나중(R0)"의 순서, 세 조건 프롬프트(장면 기술 / 인물 정서 / 시청자 정서), 제안자의 반론 1 대응(과제 공통 feature nuisance, 과제 내 split-half 신뢰도 기준선).
* 수정: ET-P7과 같은 이유로 모델 단계에 (c2) 관점 decoding 검정을 추가하고, 프롬프트 조건마다 내부 표상(probe 투영)과 출력(답변 평정)을 둘 다 저장한다. 그러면 FA-P6(내부 표상 읽기 vs 출력 묻기)이 같은 자료에서 함께 검정된다. 내부 probe가 출력보다 정서 정보가 많다는 보고(arXiv:2510.04064, 초록)가 있으므로, "관점 결속 없음"이 출력 수준에서만 성립할 가능성도 열어 둔다.
* 데이터 단서: Emo-FilM을 보조로 쓰면 인물 정서가 [AI 추정]이고 관객 경험이 [별도 평정자 규범]이라 provenance가 섞인다. 이 비교는 Spacetop 결과의 보조 해석으로만 쓴다.
* 근거: arXiv:2604.07729, arXiv:2609.34742, arXiv:2510.04064, arXiv:2408.13718

### 3.2 정렬 운반 묶음: GI-P8, VD-P8 (그리고 내가 보낸 FA-P7)

**GI-P8 (geometry-info → frontier-ai): 수용**
* 이유: 내 FA-P7(a)와 같은 설계이며, 제안자가 든 세 반론(저정서 클립의 내용 범위, 라벨 의존 선택, 11명의 소표본)과 대응(캡션 embedding으로 내용 다양성 맞춘 대조, 여러 기준의 견고성)이 내 설계보다 구체적이다. 가장 가까운 선행으로 든 Chan 2020(doi:10.1016/j.neuroimage.2020.116618, literature_db verified)도 내 검색 결과와 일치한다(예고편으로 정렬, 사진으로 정서 분류기 학습).
* 보완 두 가지: (1) "정서 강도가 낮은 클립"을 규범 평정뿐 아니라 VLM 정서 vector 투영 크기([AI 추정, 내부 표상])로도 정의해 두 기준의 결과가 같은지 본다(GI-P8의 반론 b 대응과 같은 방향). (2) 모델 쪽 대응물(VLM 사이 정서 무관 정렬의 운반, arXiv:2609.34742)과 같은 지표(held-out 대응, GW 매칭률)로 보고하면 "모델 간 운반 vs 사람 간 운반"을 한 표에 둘 수 있다.

**VD-P8 (vision-decoding → frontier-ai): 수정**
* 수용하는 부분: NSD 중립 장면으로 학습된 decoding 모델의 공유 latent(MindEye2 4096차원, Brain-IT brain token)를 "정서와 무관하게 학습된 뇌 정렬"의 실제 사례로 쓰는 착상. 상한(원 voxel probe)과 하한(무작위 사상) 설계도 좋다.
* 수정 1 (목표 공간의 정서 함량): 제안자도 반론 1에서 적었듯 적응 목표가 CLIP image latent이면 CLIP latent 자체가 정서 관련 정보를 담을 수 있어(vision-decoding round1 I1도 CLIP zero-shot 프롬프트를 정서 평가기로 제안했다) "정서와 무관한 정렬"이 성립하지 않는다. 적응 목표를 세 가지로 둔다: CLIP image latent, 저수준 목표(VAE latent나 저수준 영상 통계), 무작위 projection. 정서 probe 성능이 CLIP 목표에서만 높으면 운반된 것은 "CLIP의 정서"다.
* 수정 2 (입력 범위): MindEye2 입력은 nsdgeneral(후두엽 시각 영역)뿐이다(arXiv:2403.11207, Appendix A.2). 따라서 이 검정은 "시각피질 정서 정보가 공유 시각 latent로 얼마나 운반되는가"로 범위를 좁혀 적어야 한다. 정서 관련 비시각 영역의 운반은 Brain-IT 쪽에서도 "주로 시각 관련 피질"이라 같은 한계가 있다(arXiv:2510.25976 5.1절, vision-decoding 기록).
* 수정 3 (자극 형식): 두 모델 모두 정지 이미지로 학습되었으므로 Horikawa, Mind captioning 비디오는 keyframe 평균으로 근사하고, 그 근사가 원 voxel probe에도 같은 조건으로 적용되도록 한다.
* 근거: arXiv:2609.34742, arXiv:2403.11207, arXiv:2510.25976, arXiv:2405.07987

### 3.3 예측 신호 묶음: EF-P5, MD-P5 (참조 BI-P5)

**EF-P5 (encoding-foundation → frontier-ai): 수용**
* 이유: TRIBE v2 예측을 기준선 공변량으로 두고 V-JEPA 2 predictor surprise의 증분을 보는 matched-control은 내 CH2의 가장 약한 고리(surprise가 encoder embedding의 시간 변화로 대부분 설명될 가능성)를 정면으로 겨냥한다. TRIBE 오디오 embedding이 60 s chunk 안의 미래 정보를 담는다는 지적(arXiv:2605.04326 5.2절)과 오디오 제외 대조도 받는다.
* 보완 세 가지: (1) surprise를 TRIBE 백본과 **같은 V-JEPA 2 체크포인트**의 predictor에서 계산해, 증분이 "다른 모델"이 아니라 "예측 위반" 때문임을 보장한다. (2) 일차 목표는 관찰 잔차(편도체, 섬엽, vmPFC)와 첫 시청 참가자의 EDA로 두고, 평정자의 Suddenly, Predictable은 반복 시청자의 appraisal이므로 이차 목표로 둔다(내 IM2, MD-P5). (3) TRIBE v2와 V-JEPA 2 가중치의 비상업 조건 가능성(내 0절 E2)을 pilot 계획에 적는다.
* 근거: arXiv:2605.04326, arXiv:2607.16292, arXiv:2502.11831, arXiv:2506.09985, doi:10.7554/eLife.64972

**MD-P5 (multimodal-dynamics → frontier-ai): 수용**
* 이유: (a) 오디오 수준 예측오차를 넣지 않으면 소리 surprise가 "latent 물리" 수준에 흡수된다는 지적은 맞다. Horikawa는 무음이므로 같은 분석에서 오디오 수준이 구조적으로 0인 대조 데이터가 된다. (b) 평정자 반복 시청 문제는 내가 Round 2에서 IM2로 가져온 것과 같다.
* 보완: BI-P5(오차 vs 불확실성)와 합쳐 "예측 위계 수준(pixel / latent 시각 / 오디오 / 서사 의미) x 신호 유형(오차 / 불확실성 / 학습 진전)"의 2차원 표로 설계할 것을 제안한다. 단 아래 BI-P5 의견의 기술적 제약(V-JEPA 2 predictor는 불확실성을 직접 내지 않음)이 적용된다.
* 근거: doi:10.7554/eLife.64972, doi:10.1126/sciadv.adk6840, arXiv:2502.11831, arXiv:2407.02474

**참조 BI-P5 (brain-inspired → multimodal-dynamics, 참조 frontier-ai CH2): 짧은 의견**
* 지지한다. 다만 기술적으로 중요한 제약 하나: V-JEPA 2 predictor는 결정론적 점 예측을 내므로 "예측 불확실성"을 직접 주지 않는다(arXiv:2506.09985 식 1의 학습 목표는 masked latent feature의 L1 회귀이므로 predictor는 분포가 아니라 점 예측을 낸다). 불확실성은 (i) mask, context 표본을 바꾼 예측의 분산, (ii) 여러 체크포인트(크기, 시드) 앙상블의 불일치, (iii) 확률적 생성형 world model(행동 조건 video 생성 모델 등)의 표본 분산 중 둘 이상으로 정의하고 결과의 일치를 보고해야 한다. BI-P5 반론 1("정의가 여럿")과 같은 방향의 구체화다.

### 3.4 GC-P6 (generative-counterfactual → frontier-ai): 수정 (1번 항목 일부 반박 포함)
* **2번(T9 위반 쌍의 2x2 교차 설계): 수용.** 맥락(장례식 / 결혼식) x 표정(웃음 / 울음)을 같은 편집량으로 만들고 V-JEPA 2 surprise의 상호작용 항만을 "기대 위반"으로 해석하는 설계는 내 T9보다 낫다. 주효과(웃음 추가 자체의 surprise)를 분리하지 않으면 위반 효과를 주장할 수 없다는 지적에 동의한다. 생성 인공물에 대한 null-edit 대조도 받는다. 다만 V-JEPA 2 같은 비디오 SSL이 사회적 규칙성을 학습했는지부터 불확실하다(직관 물리조차 데이터 분포만으로 생기지 않았다는 보고, arXiv:2512.06232). 상호작용이 0이면 "정서 위반이 없다"가 아니라 "모델이 사회적 규칙성을 모른다"일 수 있으므로, 인간 놀람 평정(R2)으로 위반의 존재를 먼저 확인한다.
* **1번(T4 빈 칸을 편집으로 채우기): 수정, 일부 반박.** "자연 쌍(R0)과 편집 쌍(R1)에서 같은 ROI가 같은 쪽 유사도를 따르는지 비교"는 두 쌍의 뇌 측정 수준이 다르다. 자연 쌍은 실측 fMRI, 편집 쌍은 encoder 예측이다. 편집 쌍에서 ROI가 "따른다"는 것은 encoder가 따른다는 뜻이므로 같은 비교 축에 둘 수 없다. 수정안: 편집 쌍은 (i) encoder가 자연 쌍에서 실측과 같은 판별 패턴을 재현하는지 먼저 검증(재현하지 못하면 편집 쌍 결과를 해석하지 않음), (ii) 그 뒤 편집 쌍의 in-silico 판별을 "검증된 surrogate의 예측"으로만 보고하고, (iii) 새 fMRI(R3) 수집의 사전 예측으로 쓴다.
* **3번(CH6의 공선성 없는 시험): 수정.** 편집 쌍에서 "VLM 정서 vector를 사상에 통과시킨 예측 차이"와 "encoder 예측 차이"를 맞추는 것은, encoder(TRIBE v2 등)와 VLM이 비슷한 시각 백본 계열이면 순환에 가깝다. 사상에 쓰는 VLM과 encoder 백본을 서로 다른 계열로 고르고, 백본이 같은 경우와 다른 경우를 함께 보고한다.
* 근거: arXiv:2604.13466, arXiv:2502.11831, arXiv:2512.06232, arXiv:2609.34742, arXiv:2605.04326, arXiv:2608.06231(EmoWorld, arxiv.org abs 페이지에서 제목만 확인, 본문 미열람)

### 3.5 BI-P2 (brain-inspired → frontier-ai): 수용 (보완 3건)
* 이유: 정서 범주 band, 인간 평정 행동 경향 band(Emo-FilM Motivation 10), latent action band, 의미 통제 band(정서 배제 인간 캡션)를 같은 banded ridge에 넣는 경쟁 설계와 "파일럿 0단계: 평정 수준 공선성(discrete를 Motivation으로 교차 예측한 R²)"은 내 FA-P4를 포함하고 더 엄밀하다.
* 보완 1 (latent action band 분해): 제안자 반론 1(카메라 운동이 지배)에 대응해 latent action을 "카메라 성분"(전역 optical flow, 컷)과 "인물 성분"(인물 영역 마스크 안의 latent action 또는 pose 변화)으로 나눠 두 band로 넣는다.
* 보완 2 (선행의 범위): Thornton & Tamir (2024, Nat Commun 15:620, doi:10.1038/s41467-024-44870-7, Crossref 확인, 초록만)가 상황과 정신상태의 신경 패턴이 그것이 허용하는 행동 패턴의 가중합으로 재구성된다고 보고했다. "정서(정신상태) 표상 = 행동 affordance의 합"이라는 가설의 정지 자극 버전이 이미 있으므로, BI-P2의 새로움은 "자연 영화, 시간 연속, 자극 계산 affordance와 인간 평정 행동 경향의 직접 경쟁"으로 한정해야 한다. 제안자가 든 Mohammadi 2023, Leitão 2020과 함께 선행 목록에 넣을 것을 권한다.
* 보완 3 (묘사 vs 느낌): latent action은 portrayed(화면 속 행동), Motivation 평정은 felt(평정자의 행동 경향)이다. 두 band의 고유 분산 지도를 따로 보고하면 Axis U의 구분이 Axis V 안에서 측정된다(내 FA-P4).

### 3.6 참조 GI-P3 (geometry-info → multimodal-dynamics, 참조 frontier-ai T5): 짧은 의견
* 지지한다. "같은 영역 안에서 정서 정렬 부분공간이 시각 정렬 부분공간보다 느리게 감쇠하면 HRF로 설명되지 않는다"는 논리는 내 T5(leaky integrator 시간 상수)보다 HRF 교란에 강하다. 보완: 부분공간을 consensus 평정으로만 정의하면 라벨 의존 선택이 된다. VLM 정서 vector 투영으로 정의한 부분공간([AI 추정, 내부 표상])과 V-JEPA 2 feature로 정의한 시각 부분공간을 대안 정의로 함께 써서, 결과가 부분공간 정의 방식에 견고한지 보고하면 좋다.

---

## 4. Axis 결정에 대한 의견

### 4.1 X(Machine Affect Representations)를 R의 Sub-axis로 둔 결정: **수용**, 조건 두 가지
* 수용 이유: Construct 유형에 새 Axis가 몰리면 무작위 조합이 쏠린다는 Coordinator 판단에 동의한다. 대상이 뇌가 아니라 AI라는 지적도 맞다.
* 조건 1: R의 정의에 "해석 방법"뿐 아니라 **"AI 내부 정서 표상과 뇌 정서 표상의 비교 대상"**이 포함된다는 문장을 남겨 달라. 그래야 조합 단계에서 R을 뽑았을 때 FA-P3, FA-P5, FA-P6 같은 비교 질문이 생긴다.
* 조건 2: Axis U(Label Provenance)의 "AI 추정"을 **출력(verbalized: 평정, 캡션, odd-one-out)**과 **내부 표상(probe, steering vector 투영)**으로 나눌 것을 제안한다. 근거: 내부 probe가 출력보다 정서 정보가 많다는 보고(arXiv:2510.04064), 출력은 과도하게 범주적이라는 보고(arXiv:2508.05880). 둘은 측정 편향이 다르다. 0.2절 label-provenance 태그에도 같은 구분을 넣으면 된다.

### 4.2 Axis V(Action Readiness & Affordance): 수용, Sub-axis 제안
* "Image-computable action representations (latent action, 행동 조건 world model)" Sub-axis를 둔다(arXiv:2410.11758, arXiv:2506.09985).
* "Portrayed action vs felt action tendency" 구분을 V 안에 명시한다(FA-P4). 이것은 Axis U의 portrayed / felt 구분을 행동 성분에 적용한 것이다.

### 4.3 Axis W(Internally Generated Experience): 수용, 기여 방향
* Mind captioning 회상 조건에서 "자극 없는 회상 중 뇌가 재활성하는 성분이 모델 feature 공간의 어느 부분(시각 저수준, 의미, 모델 정서 vector)에 해당하는가"를 물을 수 있다. 회상 cue 클립의 모델 feature를 기준으로 쓰는 것이므로 G1 필요(보유). vision-decoding R2와 공동 설계 대상이다.

---

## 5. Coordinator 질문 8개에 대한 답 (frontier-ai 관점)

**Q1. Vision Decoding 연구자가 Emotion Neuroscientist의 문제를 해결할 수 있는가?**
부분적으로 그렇다. 가장 큰 기여는 "내용 기준선"이다. 재구성, 캡션 해독 pipeline은 정서가 아닌 시각-의미 내용을 최대한 회복하도록 만들어졌으므로, 그 pipeline이 회복한 내용으로 설명되지 않는 정서 분산이 남는지를 묻는 데 쓸 수 있다(Mind captioning의 2단계 설계, doi:10.1126/sciadv.adw1464). 반대로 현행 재구성 모델은 nsdgeneral 입력과 CLIP 목표, NSD prior 때문에 정서를 구조적으로 버리므로(arXiv:2403.11207, arXiv:2605.16739) 그대로는 정서 질문을 풀지 못한다. 경험(felt)의 증거는 주지 못한다.

**Q2. LLM의 representation이나 reasoning 능력을 neural emotion representation 분석에 활용할 수 있는가?**
그렇다. 다만 역할을 셋으로 나눠야 한다. (a) 회귀자: 내부 정서 vector, appraisal 방향의 투영값(arXiv:2604.07729, arXiv:2502.05489, arXiv:2609.34742). (b) 가설 생성기: 모델 내 개입(R1)으로 "appraisal을 바꾸면 정서가 어떻게 바뀌는가"의 예측 행렬을 만들고 뇌에서 검정. (c) 측정 편향의 기준: LLM은 평균 관찰자(arXiv:2408.13718)이고 출력은 과도하게 범주적이다(arXiv:2508.05880). 인간 평정의 대체물로 쓰면 안 되고 provenance를 [AI 추정, 출력 / 내부 표상]으로 나눠 표기해야 한다.

**Q3. Generative AI로 emotion과 visual semantics를 분리해 검증할 수 있는가?**
현재 형태로는 어렵다. 정서 편집이 의미를 함께 바꾸는 사례가 확인되었다(arXiv:2512.00557, arXiv:2405.12661). 식별성 관점에서 "어떤 편집 가족을 정서 편집으로 정하느냐가 정서의 조작적 정의"이므로(arXiv:2106.04619), 생성으로 분리를 "증명"할 수는 없고 조작적 정의를 명시해 시험할 수 있을 뿐이다. 실무 순서는 (1) 기존 자극 풀에서의 선택(R0, FA-P2), (2) 모델 표상 공간에서의 의미 보존 정서 개입(R1, arXiv:2510.22042), (3) 픽셀 편집 + 새 행동 평정(R2), (4) 새 fMRI(R3) 순이다.

**Q4. Emotion Dynamics를 dynamical systems나 state-space learning의 문제로 재정의할 수 있는가?**
그렇다. 우리 쪽에서 더할 수 있는 것은 두 가지다. (a) 정서 상태의 전이를 world model의 latent 상태 전이(비대칭, 방향성)와 같은 틀에서 비교(arXiv:2506.09985, IM7). (b) "지속 상태 vs 재호출"을 구분하는 검정(FA-P3). LLM 쪽에서도 이 문제가 미정이다(arXiv:2604.07729 vs arXiv:2510.04064). 제약: Horikawa 공개 전처리본은 블록 평균이라 raw 재전처리가 필요하고, Emo-FilM은 영화 14편이라 동역학 모수의 영화 수준 confound가 크다.

**Q5. Brain Foundation Model의 latent representation에서 감정 관련 구조를 찾을 수 있는가?**
찾을 수는 있지만 지금은 누수 통제 benchmark가 없어 주장이 약하다(encoding-foundation U5). 우리 쪽 도구로는 brain foundation model(Brain-JEPA arXiv:2409.19407, CortexMAE arXiv:2510.13768) latent를 USAE에 넣어 "자극 모델과 공유되는 개념"과 "뇌 모델에만 있는 개념"을 분리하고, 후자가 정서 평정과 상관되는지 보는 방식이 가능하다(arXiv:2502.03714). 주의: 비지도 latent의 최대 분산 축은 세션, run, 전역 신호로 채워질 수 있다(arXiv:2507.00320의 NMI, doi:10.1038/s41593-025-01945-y).

**Q6. Music, Video, Image의 공통 정서 특징과 modality-specific 특징을 뇌 수준에서 구분할 수 있는가?**
Video(Horikawa 무음, Emo-FilM과 Spacetop 시청각)와 Image(NSD)는 가능하고, Music 단독은 우리 데이터에 없어 영화 사운드트랙 분리(generative-counterfactual X7)로만 간접 접근한다. 방법은 (a) 모달리티별 VLM 정서 vector의 대응(cosine이 낮아도 held-out 대응과 인과 전이가 있음, arXiv:2609.34742), (b) USAE의 보편 개념 vs 모달리티 고유 개념(arXiv:2502.03714), (c) 수렴의 정보 상한(arXiv:2405.07987 6절), (d) TRIBE modality dropout(doi:10.1126/sciadv.adk6840의 감각 박탈 설계의 in-silico 판)이다. 데이터셋마다 피험자가 달라 "같은 사람의 모달리티 간 비교"는 Spacetop의 영상 vs 서사(텍스트, 오디오)에서만 가능하다.

**Q7. Neuroscience에서 관찰되는 정서 관련 계산을 AI architecture의 구조적 제약으로 구현할 수 있는가?**
두 경로를 제안한다. (a) 데이터 기반 제약: 정서 ROI 반응을 학습 목표로 쓰는 brain-tuning(arXiv:2511.07988은 STS tuning이 정서 과제로 전이되지 않았다고 보고. 정서 ROI 표적 tuning은 검색에서 미발견). (b) 구조 제약: 뇌의 정서 지속성(재귀, 신경조절)과 transformer의 즉시 재호출의 차이(arXiv:2604.07729 5.3절)를 이용해, 느린 상태 변수를 넣은 모델과 넣지 않은 모델 중 어느 쪽이 뇌의 정서 관성을 더 잘 예측하는지 시험한다. 이것은 뇌 이론을 AI 설계 제약으로 바꾸는 동시에 그 제약의 필요성을 뇌 데이터로 판정하는 설계다.

**Q8. 정서 라벨이 없는 NSD 같은 데이터도 다른 데이터셋과의 representation alignment로 의미 있게 활용할 수 있는가?**
그렇다. 세 가지 용도가 있다. (a) 정서와 무관한 정렬의 학습 풀: 피험자별 모델→뇌 사상을 NSD 대규모 중립 이미지로 학습하고 정서 vector를 운반해 nsdmeadows 100장으로 시험한다(FA-P7, arXiv:2609.34742). (b) 개념 사전의 학습 풀: SAE, USAE를 NSD 규모 자극과 반응으로 학습한 뒤 정서 데이터셋에 적용(arXiv:2506.11123). (c) in-context encoder의 prior: NSD로 meta-learning한 BraInCoRL(arXiv:2505.15813)을 Horikawa 정지 프레임에 적용. 주의: NSD로 학습한 모델로 NSD를 평가하면 누수, COCO는 대다수 VLM 학습 분포 안에 있어 오염, NSD 정서 범위가 좁다(Stage 1).

---

## 6. 다른 에이전트 Round 1과의 실제 의견 차이 (지우지 않고 기록)

| 주제 | 다른 에이전트 입장 | 내 입장 | 해소 방법 |
|---|---|---|---|
| V-JEPA 2 라이선스 | encoding-foundation: CC-BY-NC 4.0(arXiv:2605.29850 표 3 인용). brain-inspired: MIT/Apache-2.0 혼재 [검색] | 코드 저장소는 MIT(직접 확인). 가중치 조건은 미확인 | huggingface.co 모델 카드 확인(현재 차단). 확인 전까지 비상업 가정 |
| LLM 정서 표상의 지속성 | 다른 에이전트는 다루지 않음 | Round 1에서 "국소적"으로 단정했던 것을 철회, 문헌 충돌로 기록(E3) | FA-P3의 지속 상태 vs 재호출 검정 |
| SAE 해석의 새로움 | emotion-theory는 SAE를 언급만 함 | Round 1 U4의 새로움 범위를 축소(E4) | Stage 3 Round 3에서 Zeng & Gallant 본문 확인 필요 |
| world model surprise 아이디어의 중복 | brain-inspired I-4(world model 불확실성 = arousal), multimodal-dynamics 개념 4(learning progress)와 Chain 2(surprise와 경계) | 세 에이전트가 같은 모델 계열의 다른 신호를 각자 제안했다. 따로 진행하면 공선성 때문에 결과가 서로 충돌할 것 | FA-P3에서 한 모델로 세 신호를 함께 계산해 경쟁시키는 공동 설계를 제안 |
| LLM appraisal 방향 | llm-semantics Chain 3: Spacetop 서사에서 LLM appraisal 궤적과 ToM 영역. emotion-theory T8: Emo-FilM 전사본 | 내 Round 1 CH4(Emo-FilM appraisal 선행)와 같은 도구. 서로 다른 데이터, 다른 질문(ToM 하위 과정 vs 시간 선행) | Round 3에서 하나의 도구 설명(층, 방향 추출 절차, null)을 공유하고 질문은 분리 유지 |

---

## 7. 검증된 것과 미확인인 것

### 검증된 것
* 이번에 인용한 근거 ID는 모두 `literature_db.csv`에서 verified로 확인했거나(대조 스크립트로 45개 ID 확인), 이번에 식별자 경로로 새로 확인해 `literature.jsonl`에 추가했다: arXiv:2510.04064, arXiv:2510.22042, arXiv:2512.06232(arxiv.org abs 페이지), doi:10.52202/085713-3208(Crossref, NeurIPS 38).
* MIRAGE(arXiv:2605.29850) 표 3의 V-JEPA 2 라이선스 표기를 PDF로 직접 확인했다.

### 미확인
* doi:10.1016/j.bpsc.2025.11.011은 emotion-theory round1의 인용으로만 보았고 DB에 개별 행이 없다(FA-P5 선행 검색에 표기).
* Zeng & Gallant 본문(bioRxiv 429), arXiv:2510.04064, arXiv:2510.22042 본문(초록만).
* NeuroLang 2026 포스터(LLM 정서 vector와 MEG)는 [search_index], 서지 미확인.
* HF 모델 카드의 V-JEPA 2, V-JEPA 2.1 가중치 라이선스, brain-tuned V-JEPA 2.1 체크포인트(RAntonello)는 [search_index], huggingface.co 차단.
* Mind captioning 저장소의 실제 파일(캡션, 회상, vividness)과 두 코호트의 피험자 중복.
* 각 제안의 "no" 판정은 위에 적은 검색 경로 안에서의 판단이다. Stage 2 표본에서 "no"의 25%가 실제로 선행되어 있었으므로 Round 3에서 쓰이는 항목은 다시 확인한다.
* export.arxiv.org API가 이번 라운드 중 429를 반환해 arXiv 검색 질의는 Round 1 기록과 arxiv.org abs 페이지 확인에 의존했다.
