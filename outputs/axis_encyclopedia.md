# Deliverable B: Research Axis Encyclopedia

* 작성: Coordinator (Stage 2)
* 기준일: 2026-11-12
* 입력: `reference/axes.md`, 11개 에이전트의 `outputs/agents/<이름>/round1.md` (1절 미해결 문제, 2절 모델, 5절 Sub-axis, 7절 Axis 확장 제안), `outputs/literature/literature_db.csv` (작성 시점 verified 고유 365편, Stage 2 재점검 후 377편)
* 표기: `[에이전트]`는 제안한 에이전트, 논문은 DOI 또는 arXiv ID. 대표 논문은 해당 Axis의 담당 에이전트가 추가한 verified 논문을 우선해 `literature_db.csv`에서 뽑았다. 미해결 문제와 Sub-axis 제안의 세부 근거는 각 에이전트 round1.md의 해당 절에 있다.
* 이 문서는 Round 1(독립 탐색)의 결과다. 에이전트 간 교차 검토(Round 2~3)를 거치지 않았으므로 Sub-axis 제안은 후보이며, 겹치는 제안은 Coordinator가 묶었다.

---

## 0. 공통 기준 문헌과 횡단 쟁점

### 0.1 여러 에이전트가 독립적으로 기준점으로 삼은 문헌

| 논문 | ID | 기록한 에이전트 수 | 왜 기준점인가 |
|---|---|---|---|
| Ma & Kragel (2026) Nat Commun | doi:10.1038/s41467-025-68240-z | 11 | Emo-FilM에서 hippocampus-vmPFC의 지도형 정서 표상. "이미 수행됨" 판단의 기준. 효과 크기가 작고(r 약 0.04~0.10) TEM 환경이 대칭 유사도 위 무작위 보행이라는 한계를 여러 에이전트가 지적 |
| Horikawa et al. (2020) iScience | doi:10.1016/j.isci.2020.101060 | 8 | 1순위 데이터셋의 원 논문 |
| Du et al. (2025) | arXiv:2509.24298 | 8 | MLLM odd-one-out embedding이 규범 평정보다 뇌를 더 잘 예측한다는 주장. 비교 대상이 별도 평정자 규범 평정이고 시각 영역 기여가 섞여 있다는 비판 [emotion-theory, adversarial-reviewer] |
| Kragel et al. (2019) Sci Adv, EmoNet | doi:10.1126/sciadv.aaw4358 | 8 | **Horikawa와 같은 Cowen & Keltner 비디오 프레임으로 학습됨**(5개 에이전트가 원문 Methods로 각각 확인). Horikawa 분석에 feature나 평가기로 쓰면 학습-평가 누수 |
| Westlin et al. (2025) | arXiv:2507.00320 | 7 | Horikawa 데이터의 최소 가정 재분석, 재현 실패 보고(preprint). 군집과 scan session, run의 NMI(0.19, 0.17)가 정서 평정과의 NMI(0.014)보다 10배 이상 크다는 점을 4개 에이전트가 각자 지적 [systems-neuro, emotion-theory, geometry-info, adversarial-reviewer] |
| EmoMind (2026) | arXiv:2605.16739 | 5 | Horikawa로 정서 캡션 decoding. TRIBE v2 합성 뇌로 대체 시 정서 RSA 하락. 실측과 합성의 자극 집합이 달라 결과가 섞였다는 지적 [generative-counterfactual, encoding-foundation] |
| Horikawa et al. (2025) Sci Adv, Mind captioning | doi:10.1126/sciadv.adw1464 | 3 | **같은 Cowen & Keltner 비디오를 쓴 독립 코호트(6명)**. 72개 클립 5회 반복, 회상 imagery, 정서를 쓰지 말라는 지시로 받은 캡션이 있다(논문 본문 기준, OpenNeuro ds005191). 4개 보유 데이터셋 밖이라 사용 여부는 사용자 결정 사항 [vision-decoding, llm-semantics] |

### 0.2 모든 Axis에 걸치는 필수 태그 (여러 에이전트의 독립 제안을 통합)

Axis가 아니라 Stage 3 이후 모든 후보 질문에 붙이는 표기로 둔다.

| 태그 | 값 | 제안 | 근거 |
|---|---|---|---|
| **label-provenance** | 대상: portrayed / perceived affective quality / felt. 주체: 참가자 본인 / peer 합의 / 별도 평정자 규범 / AI 추정 | emotion-theory(S2), adversarial-reviewer, llm-semantics, generative-counterfactual(S6) | CLAUDE.md 6절. Stage 1 3.2절 |
| **evidence-level** | R0 상관 / R1 모델 내 개입 / R2 새 행동 평정 / R3 새 fMRI 자극 조작 / R4 뇌 개입 | generative-counterfactual(S5) | 우리 데이터만으로는 R0~R1, 신규 행동 평정으로 R2까지 |
| **insilico-vs-observed** | 관찰 / in-silico / 혼합 | encoding-foundation | 6절 "In-silico predictions vs observed fMRI responses" |
| **G1** | 원본 자극 필요 / 불필요 | Stage 1 | 사용자 확인으로 4개 데이터셋 모두 보유. 재배포와 파생물 제작 조건은 별도 |
| **signal-feasibility** | 표적 영역의 tSNR, dropout, TE, MB 조건 점검 여부 | systems-neuro(S3) | 피질하 표적 질문의 전제 |
| **minimum-validation** | adversarial-reviewer 7.4절의 7항목(경쟁 모델과 matched-complexity null, 상한 병기, 신뢰도 민감도, leakage 경로별 대응, 일반화 수준 명시, 라벨 출처 표시, 반증 해석 사전 기술) 충족 여부 | adversarial-reviewer | 미충족이어도 버리지 않고 표시 |

### 0.3 여러 Axis에 반복해서 나타난 공통 미해결 문제

| 공통 문제 | 등장한 에이전트와 Axis | 대표 근거 |
|---|---|---|
| 정서 신호와 시각, 의미 내용 신호의 분리 | llm-semantics(C, description confound), frontier-ai(R, 정서 vs 상황), generative-counterfactual(L, 의미 고정 편집), adversarial-reviewer(T, 측정 오차와 잔여 교란), vision-decoding(G) | doi:10.1371/journal.pone.0152719 (Westfall & Yarkoni 2016), arXiv:2512.00557 (NeuroVolve), doi:10.1038/s42256-025-01072-0 |
| Horikawa 2020의 범주 결론과 Westlin 2025의 재현 실패가 갈리는 지점 | emotion-theory(Q), geometry-info(K, O), systems-neuro(E), adversarial-reviewer(T) | doi:10.1016/j.isci.2020.101060, arXiv:2507.00320 |
| 정서 지도는 대칭 유사도인가 방향성 전이(예측) 구조인가 | brain-inspired(N), geometry-info(K), multimodal-dynamics(D) | doi:10.1038/s41467-025-68240-z, doi:10.1038/nn.4650, doi:10.1016/j.cell.2020.10.024 |
| 라벨 주체가 바뀌면 뇌 설명력이 어떻게 달라지는가 | emotion-theory(A, Q), llm-semantics(C), systems-neuro(E), vision-decoding(G), multimodal-dynamics(D) | doi:10.1162/imag_a_00517 (perceived vs felt), doi:10.1162/imag.a.134 |
| In-silico 뇌가 정서 구조를 얼마나 보존하는가 | encoding-foundation(F, H), generative-counterfactual(L) | arXiv:2605.04326 (TRIBE v2), arXiv:2605.16739 |
| arousal 판독이 신경 신호인가 전신 자율신경 신호인가 | systems-neuro(E), encoding-foundation(H, physiology-augmented) | doi:10.1038/s41593-025-01945-y, doi:10.1371/journal.pcbi.1012994 |
| 개인 간 공유 차원과 개인 고유 변동의 위치(rank) | geometry-info(K, O), emotion-theory(Q), vision-decoding(G) | arXiv:2409.06843, arXiv:2505.12653 |

---

## 1. Axis별 정리 (A~T)

각 Axis 항목의 "추가 Sub-axis"는 Round 1 제안이며 `reference/axes.md`의 기존 Sub-axis는 유지한다(삭제 제안은 없었다).

### Construct (무엇을 묻는가)

#### Axis A. Emotion & Affective Constructs [emotion-theory]
* **추가 Sub-axis:** Affective Quality Space [emotion-theory S6], Emotion Schema and Language, Self-relevance / Self-tagging [emotion-theory 7.1], Aesthetic Engagement Dynamics(A x D) [multimodal-dynamics S9]
* **재분류 제안:** "Emotion Recognition vs Emotion Experience"를 Sub-axis에서 **모든 질문의 필수 태그(label-provenance)** 로 승격 [emotion-theory]. "Subjective Feeling"은 4개 데이터셋 어디에도 스캔 중 연속 자기보고가 없으므로 "보고"를 측정한다고 명시 [emotion-theory].
* **대표 논문:** arXiv:2502.05489, doi:10.1126/sciadv.abf7129, doi:10.1162/imag_a_00517, doi:10.1038/s41380-019-0520-3, doi:10.1038/s41598-020-77117-8, doi:10.1073/pnas.1702247114, doi:10.1073/pnas.1619316114
* **주요 모델/방법:** EmoNet(도구, 누수 주의), MLLM machine behavior + SPoSE, HMeta-d, self- vs cross-prediction 설계
* **미해결 문제:** 신뢰 가능한 정서 차원의 수와 측정 가정 의존성; 인식(귀속)과 경험(느낌)의 분기 지점; HOT 예측의 관찰 검정; 혼합 정서의 선형 중첩 여부; 정서판 reliability paradox(자극 수준 신뢰도와 개인 수준 신뢰도의 괴리); 정서 범주 표상이 느낌인가 action readiness인가 [brain-inspired P-2]
* **연결:** Q(신뢰도), C(귀속 vs 경험), O(개인 특이성), 새 Axis V(Action Readiness), Y(Metacognition)

#### Axis B. Perceptual & Stimulus Representation [vision-decoding]
* **추가 Sub-axis:** Stimulus Affect Coverage and Sampling Structure, Annotation Instruction as Stimulus Descriptor(중립 지시 캡션 vs 정서 지시 캡션), Internally Generated Stimulus Content, Synthetic / Generated Stimuli as Probes [vision-decoding], Portrayed Behavior Ethogram(외부 분야 Computational Ethology 유래) [brain-inspired S-7]
* **주석:** Audio / Music / Speech Features는 Emo-FilM, Spacetop에서만 가능(Horikawa 무음, NSD 정지 이미지) [vision-decoding]
* **대표 논문:** doi:10.1126/sciadv.adw1464, doi:10.1038/s42256-025-01072-0, doi:10.1523/jneurosci.1436-24.2025, doi:10.1038/s41467-024-49073-8, arXiv:2306.03089, doi:10.1038/s41467-024-53668-6
* **주요 모델/방법:** BrainDiVE, 편도체 encoding + 합성, EmoSet 분류기, Mind captioning
* **미해결 문제:** 정서 영역의 선호 자극이 자극 집합에 따라 달라지는가; 학습 자극 분포(NSD 중립, C&K 범주 군집)가 모델 prior와 결론에 주는 영향
* **연결:** C(기술 잔차), G(재구성), L(선호 자극 합성), M(오디오)

#### Axis C. Context, Meaning & Narrative [llm-semantics]
* **추가 Sub-axis:** Attribution-Experience Gap, Situation Structure & Relational Semantics, Description Residual, Social Primitives & Pre-reflective Inference, Collective and Cultural Emotion Semantics, Narrative Prediction Signals [llm-semantics S1~S7]
* **재분류 제안:** "Perceived Meaning vs Experienced Emotion"을 관점 문제(S1)와 내용 문제(S3)로 분할; "Emotional Expectation", "Surprise / Prediction Error"를 S7로 통합하고 계산 모델과 대상을 명시; "Causal Understanding", "Character Intentions", "Social Relationships"를 S2 아래로 [llm-semantics 7.2]. D와 역할 분담: C는 예측의 내용, D는 예측의 시간 구조 [multimodal-dynamics], N은 계산 정의 [brain-inspired S-3]
* **대표 논문:** doi:10.1126/sciadv.adw1464, doi:10.1038/s41467-026-71151-2, arXiv:2502.05489, doi:10.1038/s41598-025-14961-6, doi:10.1162/imag.a.134, doi:10.1038/s41467-019-13599-z
* **주요 모델/방법:** 공개 가중치 비디오 MLLM(Qwen2.5-VL, InternVL), 폐쇄 MLLM, SPoSE odd-one-out, Gromov-Wasserstein 정렬, Bayesian inverse planning ToM, VidSitu식 상황 표현, LLM 사건 분할
* **미해결 문제:** 귀속과 경험의 신경 분리; 정서 표상과 장면 기술 의미의 혼동; 맥락 의존과 신체 기반 정서에서의 모델 실패가 뇌의 무엇에 대응하는가; 모델 생성 라벨의 측정 타당도; 평균 관찰자 모델과 개인 특이 정서; 정서 의미의 언어, 문화 의존성
* **데이터 적합도:** Narrative Progression은 Horikawa, NSD 불가, Spacetop narratives 최적. Contextual Reinterpretation은 4개 데이터셋에 같은 자극의 다른 맥락 조건이 없어 관찰 데이터로 직접 검증 불가 [llm-semantics 7.3, 7.4]
* **연결:** A, Q(라벨 관점), D(사건 경계), N(예측 신호), R(LLM 내부 정서 표상), 새 Axis U, X

#### Axis D. Temporal Dynamics [multimodal-dynamics]
* **추가 Sub-axis:** Affective Carry-over vs Hemodynamic Spillover, Affective Timescale Hierarchy, Online-to-Retrospective Integration, Affective Dynamics Comparison(D x K), Temporal Alignment & Lag Estimation(D x Q), Emotional Event Boundaries(C에서 교차 등재) [multimodal-dynamics S1~S4, S8, S10]
* **재분류 제안:** "Static vs Dynamic Representations"를 "자극 단위 요약 표상 vs 시간 분해 표상"으로 좁힘 [multimodal-dynamics]. K와 경계: K는 동역학의 기하, 위상 속성(시간상수, 차원), D는 시간 구성 개념(onset, peak, 전이 시점) [geometry-info]
* **대표 논문:** arXiv:2602.07570, doi:10.7554/elife.107955, arXiv:2506.09985, arXiv:2509.21381, doi:10.1371/journal.pcbi.1012994, doi:10.1126/sciadv.abf7129, doi:10.64898/2026.09.26.754452
* **주요 모델/방법:** V-JEPA 2, TRIBE, Qwen2.5-Omni, MERT, LAION-CLAP, ImageBind, EM-LLM, Event segmentation HMM, DSA, twRSA, rSLDS
* **미해결 문제:** Horikawa의 10 s 연속 블록(5명 동일 순서)에서 신경 이월과 HRF 잔여가 분리되지 않음; 정서 동역학이 이산 상태 전이인가 연속 drift인가; 정서마다 다른 시간 척도; 순간 경험이 회고 평정으로 압축되는 규칙(Emo-FilM 1 Hz vs Spacetop 사후 1회가 양 끝); AI 연속 주석의 시간축 타당화
* **연결:** K(attractor, 이완), N(SR, 예측), C(사건 경계), M(문맥 길이), E(network 상태 전이)

### Neural (뇌의 어디, 어떤 형식)

#### Axis E. Neural Targets [systems-neuro]
* **추가 Sub-axis:** Pathway/Circuit-level Targets, Brain-Body Interface Targets, Network State Landscape, Idiographic Network Targets, Visual Subcortical Routes(SC-pulvinar-amygdala), Cortical and Subcortical Gradients [systems-neuro 7.1]
* **재분류 제안:** FC는 E(어떤 연결이 표적인가)와 F(FC를 표상 형식으로 쓰는 방식)로 역할 분리; "Visual and Auditory Cortex"를 "Sensory Cortices as Affective Targets"로; Insula, vmPFC 등을 "Allostatic-Interoceptive System" 아래 두는 안은 특정 이론(EPIC) 반영이라 **이견 가능 지점**으로 표시 [systems-neuro 7.2]
* **사용 조건:** "Amygdala and Subcortical Systems"는 데이터셋별 신호 판정 없이 결과를 보고하지 않는다. 판정 요지: Spacetop은 Kragel 2021이 경로를 찾은 것과 같은 계열의 3T 설정이라 선례가 있다; NSD는 해상도가 가장 좋으나 반복 제시와 기억 과제가 amygdala 반응을 왜곡; Emo-FilM은 raw 재전처리 필요; Horikawa는 생리 기록이 없고 TE 43 ms(신호 손실은 추론) [systems-neuro]
* **대표 논문:** doi:10.1038/s41593-025-01945-y, doi:10.64898/2026.06.08.730730, doi:10.64898/2026.09.26.754452, doi:10.1371/journal.pcbi.1012994, doi:10.1016/j.neuron.2021.06.001
* **주요 모델/방법:** MPathI, arousal CPM, Brain-JEPA, energy landscape, rSLDS, homological scaffold, 전역 신호-생리 결합 모델, Tian subcortex atlas, ICA-FIX
* **미해결 문제:** 정서 신호가 whole-brain 분산의 어느 subspace에 있는가; network arousal 판독이 신경인가 전신 자율신경-혈관 신호인가; 피질하 경로가 자연 자극에서 기능하고 측정 가능한가; transmodal 위치가 정서 고유 속성인가 시간 적분 위계의 부산물인가; 규범 평정과 본인 경험 중 무엇이 network 신호를 결정하는가
* **연결:** A(Interoception), H(physiology-augmented), K(고차 위상), O(idiographic), D(상태 전이)

#### Axis F. Brain Representation [encoding-foundation]
* **추가 Sub-axis:** In-silico Representational Fidelity, Representation Coverage(피질 전용 vs 피질하 포함), Residual / Idiosyncratic Representations, Self-supervised Brain Foundation Latents, Flat-map / Surface Video Representations [encoding-foundation]
* **재분류 제안:** "Shared Latent Representations"와 "Subject-specific Representations"는 F(형식, coverage)와 O(개인차의 의미)로 역할 분리; 모든 F 결과에 insilico-vs-observed 태그 [encoding-foundation 7]
* **대표 논문:** arXiv:2605.04326, doi:10.1126/sciadv.abf7129, arXiv:2403.11207, doi:10.1038/s41467-024-49073-8, arXiv:2510.13768
* **주요 모델/방법:** TRIBE v2(공개 checkpoint는 fsaverage5 피질 평균 피험자 예측만, 피질하와 피험자별 readout 없음, CC BY-NC 4.0), CortexMAE, NeuroSTORM, SwiFT, Brain-JEPA, BrainLM, Omni-fMRI, Brain-Mamba
* **미해결 문제:** in-silico 예측이 정서 표상의 관계 기하를 재현하는가(EmoMind의 RSA 하락은 같은 자극의 실측과 짝지은 비교가 아님); 뇌 입력 foundation latent의 정서 구조를 누수 통제하에 평가한 benchmark 부재
* **Contamination 점검 결과:** TRIBE v2, CortexMAE, NeuroSTORM 등의 fMRI 사전학습 데이터에 우리 4개 데이터셋은 없다. NSD는 일부 모델의 평가에 쓰였고 TRIBE v2 코드에 NSD 분기가 있어 내부 사용 여부는 미확인 [encoding-foundation]
* **연결:** H, S, L(surrogate audit), O, K

#### Axis O. Individual & Population Variation [geometry-info]
* **추가 Sub-axis:** Shared vs Private Subspace Spectrum, Individualized Representational Geometry(WHA/INT), Traversal Idiosyncrasy(개인별 시점, 속도, time-warp), Geometric Idiosyncrasy Metrics, Label-subject Mismatch as Individual-difference Signal, Sample-size Regime [geometry-info 7]
* **재분류 제안:** "Trait-dependent Representation"은 우리 데이터에서 확증 불가(Spacetop 설문 미공개, Emo-FilM 30명)이므로 "탐색적"으로 표시하고 개인 내 결합을 우선 [geometry-info, doi:10.1038/s41586-022-04492-9 근거]
* **대표 논문:** arXiv:2409.06843, doi:10.1371/journal.pbio.3003795, doi:10.1371/journal.pcbi.1012994, doi:10.1162/imag_a_00032, doi:10.1126/sciadv.abf7129
* **주요 모델/방법:** cross-decomposition 스펙트럼 + hyperalignment, Warp hyperalignment / INT, SRM, Hyper-HMM, (Fused Unbalanced) Gromov-Wasserstein, generalized shape metrics
* **미해결 문제:** 개인 간 공유 차원 수와 개인 고유 변동의 rank; vmPFC 개인 특이성이 "다른 지도"인가 "같은 지도의 다른 통과"인가; valence가 영화와 데이터셋을 넘어 전이되지 않는 이유
* **피험자 수 조건:** Horikawa(5명)는 개인 고유 구조의 존재와 재현성, Spacetop(약 100명)은 분포와 과제 간 일관성을 묻는다 [geometry-info 0.2]
* **연결:** K, Q(spectral reliability), F, E(idiographic), 외부 분야 Computational Psychiatry

### Model & Method (무엇으로 푸는가)

#### Axis G. Decoding [vision-decoding]
* **추가 Sub-axis:** Affective Fidelity of Generative Decoding, Perception-to-Imagery Affect Cross-decoding, Shared vs Private Decoding Latents, Held-out-category Zero-shot Emotion Decoding, Region-additive Decoding, Affective Captioning [vision-decoding]
* **재분류 제안:** "Generative Reconstruction"을 측정으로서의 재구성과 시각화로서의 재구성으로 분리(doi:10.1016/j.neunet.2025.107515 근거); "Brain-conditioned Generation"의 1차 소속을 L에서 G로 [generative-counterfactual]
* **Novelty 표시:** "Emotion Category Decoding", "Dimensional Affect Decoding"은 기준선 항목이며 단독으로는 최종 후보에서 제외 [vision-decoding, protocols.md P5]
* **대표 논문:** doi:10.1126/sciadv.adw1464, arXiv:2510.25976, doi:10.1016/j.neunet.2025.107515, arXiv:2403.11207, doi:10.1038/s41598-023-42891-8
* **주요 모델/방법:** MindEye2, Brain-IT, Brain-Diffuser, MIRAGE, Mind captioning, EmoMind, NeuroClips, MindBridge, WAVE
* **미해결 문제:** 재구성 파이프라인의 정서 정보 손실 단계(MindEye2, Brain-IT는 입력이 시각피질에 한정되고 생성 prior가 중립적인 NSD 이미지로 학습; 이 계열 재구성 논문 본문에는 정서 평가가 없었다); 해독된 정서가 규범인가 경험인가; "분류 + 환각"인가 조합적 표상의 복원인가; 회상과 심상에서 정서 표상 재활성
* **연결:** B, L, F(입력 영역), O(공유 latent), 새 Axis W

#### Axis H. Encoding [encoding-foundation]
* **추가 Sub-axis:** Residual Encoding(관찰 - foundation 예측), Foundation Encoder Auditing, Physiology-augmented Encoding, Inverse Use of Encoders, Zero-shot Group vs Fine-tuned Individual Encoding [encoding-foundation]
* **병합 제안:** "Brain Foundation Model Encoding"과 "Brain Response Simulation"을 "Foundation Encoders & In-silico Simulation"으로. "Emotion Feature-to-Brain"은 라벨 출처별(규범, 본인, AI)로 하위 구분
* **대표 논문:** arXiv:2605.04326, doi:10.1038/s41562-025-02252-z, arXiv:2507.22229, doi:10.1523/jneurosci.1436-24.2025, doi:10.1038/s41467-024-53147-y
* **미해결 문제:** "limbic 맹점"(amygdala, insula, vmPFC에서 자극 구동 encoder가 약한 이유가 잡음인지, 내수용과 생리 입력 부재인지); group 예측 잔차에 개인 정서 경험이 담기는가; 정서 encoding의 설명적 적절성(Conwell 2024는 구조가 다른 모델들이 비슷한 예측력을 보임); in-silico 정서 영역 제어 결과의 생체 검증 공백
* **연결:** F, S, L, E(생리), T(variance partitioning)

#### Axis I. AI Model Families [frontier-ai]
* **추가 Sub-axis:** World-model Predictors(V-JEPA 2 encoder와 predictor 분리), Latent Action Models / VLA, Open-weight vs API-only MLLM 구분, Brain-tuned Models [frontier-ai 7]
* **재분류 제안:** "Brain-inspired / Neuromorphic Models"는 N으로 이동, I에는 교차 표시만; "Graph Neural Networks" 우선순위 하향
* **대표 논문:** arXiv:2502.11831, arXiv:2602.07570, arXiv:2502.05489, arXiv:2506.09985, arXiv:2502.03714
* **주요 모델:** V-JEPA 2 / 2.1(코드 MIT), TopK / Archetypal SAE, RepE 정서 vector, LAPA, BraInCoRL, Label-free CBM. 라이선스 위험: TRIBE v2와 jepa-intuitive-physics는 CC-BY-NC, DINOv3는 자체 라이선스 [frontier-ai, LICENSE 파일 직접 확인]
* **미해결 문제:** world-model 예측오차(surprise)를 정서적 놀람, suddenness appraisal 회귀자로 쓴 연구를 찾지 못함 [frontier-ai, 검색 범위 내]
* **연결:** J, R, N(예측 부호화), D

#### Axis J. Learning Objectives [frontier-ai]
* **추가 Sub-axis:** Joint-Embedding Predictive(latent 예측)를 Masked Modeling과 구분, Identifiable Multi-view Objectives, Brain-tuning, In-context / Meta-learned Encoding, Sparse Dictionary Learning Objectives
* **재분류 제안:** "Disentangled Representation Learning"을 "Identifiability-based Disentanglement"로 좁힘(비지도 disentanglement는 귀납 편향 없이 식별되지 않는다는 결과 근거, arXiv:1811.12359는 존재만 확인)
* **대표 논문:** arXiv:2502.11831, arXiv:2506.09985, arXiv:2511.07988, arXiv:2410.11758, arXiv:2303.09166
* **연결:** I, R, P(뷰 설계를 가설로)

#### Axis L. Generative & Counterfactual Methods [generative-counterfactual]
* **추가 Sub-axis:** Semantics-clamped Affective Counterfactuals, Relational/Joint Neural Control of Affective Regions, Surrogate-brain Fidelity Audit for Affect, Temporal/Auditory/Narrative Counterfactuals for Film, Generator-prior and AI-ness Confound Audit, Stimulus Selection as Weak Intervention [generative-counterfactual]
* **재분류 제안:** "Generative Experimental Design"을 오프라인 in-silico 선택/합성과 온라인 closed-loop로 분리(우리 데이터로는 전자만). L과 P 경계: L은 "어떻게 counterfactual을 만드는가", P는 "무엇을 결론할 수 있는가"
* **대표 논문:** arXiv:2605.04326, arXiv:2512.00557, doi:10.1038/s41562-025-02252-z, doi:10.1073/pnas.1912334117, arXiv:2609.27729
* **주요 모델/방법:** TRIBE v2, NeuroVolve, BrainACTIV, RNC, Concept Sliders, LivePortrait, FLUX.1 Kontext, Wan, 영화 음향 3-stem 분리(DnR, HT Demucs), EmoEdit, EmotiCrafter, interchange intervention
* **핵심 공백:** 생성 모델로 정서를 조작하면 의미 내용이 같이 바뀐다. NeuroVolve(arXiv:2512.00557)는 실제 fMRI에서 amygdala를 움직였지만 최대화 이미지는 표정이 강한 얼굴, 최소화 이미지는 건물이었다. 의미를 고정한 정서 편집이 비어 있다 [generative-counterfactual]
* **연결:** P, H, G, B, C, 새 Axis X

#### Axis M. Multimodal Integration [multimodal-dynamics]
* **추가 Sub-axis:** Modality Dependence of Emotion, Audio Source Decomposition for Affect, Cross-modal Affective Congruence and Reliability Weighting, Temporal Context Length in Multimodal Models [multimodal-dynamics]
* **재분류 제안:** "Image / Video / Music Integration"을 "Audio-Visual Integration"에 통합하고 "Language-Perception Alignment" 아래 대사 vs 자막 vs 비언어 소리 구분; "Modality Invariance"를 "Supramodal vs Modality-specific Affect Coding"으로
* **대표 논문:** arXiv:2602.07570, doi:10.1093/scan/nsag090, arXiv:2507.22229, arXiv:2509.21381, doi:10.1162/imag.a.134, doi:10.1126/sciadv.adk6840
* **미해결 문제:** 어떤 정서가 소리에 의존하며 vmPFC의 "모달리티 독립" 부호가 대사(언어 의미)로 운반되는가; 영화 간 arousal 신호가 음량과 움직임의 재표현인가
* **데이터 제약:** Horikawa 무음, Emo-FilM과 Spacetop alignvideo 소리 있음 → 데이터셋 대비 자체가 한 축
* **연결:** B, D, S(cross-modal transfer), L(음향 counterfactual)

#### Axis N. Brain-like Computation [brain-inspired]
* **추가 Sub-axis:** Predictive Affective Maps(SR, TEM, graph vs map), Distributional / Multi-channel PE Codes, Observer-as-Agent Modeling, Homeostatic / Interoceptive Control Models [brain-inspired]
* **재정의, 분할:** Biologically Constrained Learning, Specialized Pathways, Neural Routing을 "Structural Priors & Normative Specialization Tests"로 묶음; "Emotion as Computational Value / Salience"를 Value-based Emotion Taxonomy와 Precision / Uncertainty as Affect로 분할; Neuromorphic Systems는 유지하되 fMRI와 직접 연결 불가로 우선순위 하향
* **대표 논문:** doi:10.1073/pnas.2414005122, arXiv:2607.19327, doi:10.1073/pnas.2513856123, doi:10.1016/j.neubiorev.2022.104977, doi:10.1016/j.neuron.2021.06.001, doi:10.1038/nn.4650, doi:10.1016/j.cell.2020.10.024
* **주요 모델/방법:** SR과 value-weighted SR, TEM, distributional TD, pymdp, HBI, MPathI, Visual-Valence + Shortcut, MoRE-Brain, DeepGaze IIE, TDANN
* **미해결 문제:** 정서 지도가 유사도인가 전이 예측인가; 정서 계산 모형(active inference, RL)이 인간 데이터로 거의 검증되지 않음; confirmation-biased learning의 신경 구현(Spacetop social); 정서 전용 구조의 필요성; 순간 정서와 누적 정서(momentum)
* **확인 사항:** 에이전트 정의가 조사 후보로 지정한 "EmoPathway"는 arXiv, Crossref, Semantic Scholar, WebSearch에서 찾지 못해 근거로 쓰지 않았다(사용자 확인 필요). 가장 가까운 확인된 모형은 arXiv:2607.19327의 shortcut pathway 모형 [brain-inspired 0.3]
* **연결:** D, K, E, 새 Axis V

### Structure & Interpretation (어떤 구조로 보는가)

#### Axis K. Geometry & Mathematical Structure [geometry-info]
* **추가 Sub-axis:** Rank-resolved Sharedness / Spectral Geometry, Abstraction Geometry(CCGP, shattering dimensionality), Relaxation and Persistence Dynamics, Metric Choice(Euclidean, geodesic, successor metric), Higher-order Interaction and Synergy, Information-theoretic Efficiency of Affective Categories(IB), Representational Metric Spaces(shape metrics) [geometry-info]
* **재정의:** "Distributional Representations"를 확률적 표상과 분포 간 정렬(OT에 통합)로 분리; "Manifold Learning"에는 단순 시각화가 P5 Novelty Constraint 대상이라는 경고 문구
* **대표 논문:** arXiv:2409.06843, doi:10.1016/j.cell.2020.09.031, doi:10.1371/journal.pbio.3003795, doi:10.64898/2026.09.26.754452, doi:10.1038/s41598-025-14961-6
* **미해결 문제:** "공유 정서 기하"의 순환성(Ma & Kragel의 참가자 간 0.978은 같은 consensus 표적으로 학습한 decoder 출력의 기하라 표적 구조를 물려받았을 수 있음); 비지도 구조 발견이 고분산 부분공간을 찾는가 정서 부분공간을 찾는가; 정서 관성의 기하 정의; 고차 위상 정보가 시너지인가 차원 폭인가
* **연결:** O, D, N, Q, E

#### Axis R. Explainability & Mechanistic AI [frontier-ai]
* **추가 Sub-axis:** Model-internal Emotion Vectors(또는 새 Axis X로 승격), Universal Concept Dictionaries including Brain, Stability and Temporal-coherence Audits, Augmented Sparse Encoding, Discriminating Tests between Representational Hypotheses, In-silico Causal Intervention as Hypothesis Generator [frontier-ai]
* **재분류 제안:** "Model Disagreement"는 T와 중복되므로 R에서는 "모델 간 개념 불일치 분석"으로 좁힘
* **대표 논문:** arXiv:2604.07729, arXiv:2609.34742, arXiv:2502.05489, arXiv:2502.03714, arXiv:2604.03919
* **미해결 문제:** SAE 기반 fMRI 해석의 재학습 불안정성과 비디오 시간 일관성 파괴; 뇌-자극 정렬 latent에서 정서를 원리적으로 분리하는 방법 부재; 정서와 무관한 정렬이 정서 기하를 운반하는가(수렴의 상한, arXiv:2405.07987)
* **연결:** I, J, C, X, T

### Inference & Measurement (어떻게 검증하는가)

#### Axis P. Causality & Scientific Inference [generative-counterfactual]
* **추가 Sub-axis:** Evidence-level Ladder(R0~R4) 표기 의무화, Rater-structure Causal Graphs, Dataset-internal Real Interventions Inventory(예: Spacetop cue 조작), Distributional Robustness as Causal Screening, Over-control and Collider Risk [generative-counterfactual]
* **핵심 판단:** 평정자가 fMRI 참가자가 아닌 데이터(Horikawa, Emo-FilM 주 라벨)에서는 "뇌 → 평정" 매개 구조가 원리적으로 성립하지 않는다 [generative-counterfactual]. 정서와 의미가 인과적으로 얽힌 경우 교란 회귀가 신호를 지우는 과통제 위험
* **대표 논문:** arXiv:2512.00557, doi:10.1038/s41562-025-02252-z, doi:10.1073/pnas.1912334117, arXiv:2609.27729, doi:10.1038/s41467-024-53668-6
* **연결:** L, T, Q, 새 Axis U

#### Axis Q. Reliability & Measurement [emotion-theory]
* **추가 Sub-axis:** Rank-resolved / Spectral Reliability, Disagreement-as-signal, Validity of Unsupervised Structure, Disattenuation for Brain-Behavior and Brain-AI Comparison, Stimulus Sampling and Generalization, Rater Population Mismatch [emotion-theory 7.2]
* **병합, 명확화:** "Hierarchical Bayesian Models"를 "Psychometric Measurement Models"의 방법으로 병합; "Neural Noise Ceilings"를 반복 기반(NSD)과 피험자 간 공유 성분 기반(Horikawa, Emo-FilM)으로 구분. 후자는 개인 특이 정서 신호를 잡음으로 분류하므로 정서 영역에서는 "공유 성분의 상한"이다(doi:10.1126/sciadv.abf7129) [emotion-theory]
* **데이터셋별 사전 점검표:** emotion-theory round1.md 7.3절(라벨 주체, 반드시 보고할 신뢰도, 대표 위험)
* **대표 논문:** arXiv:2505.12653, arXiv:2409.06843, doi:10.1126/sciadv.abf7129, doi:10.1162/imag_a_00517, doi:10.1073/pnas.1702247114
* **Cowen & Keltner (2017) Discussion 원문 확인:** "새 fMRI 모델링"과 "multidimensional reliability estimation"은 Discussion 6째 단락 마지막 한 문장(두 제안이 아니라 하나). 뇌 활동 패턴이 구분하는 정서 종류의 수를 세는 것이 목적. higher-order theory 연결은 7째 단락. 평정과 무관하게 뇌 간 일치만으로 차원 수를 센 연구는 찾지 못함(Koide-Majima 2020은 평정에 묶인 약 25차원) [emotion-theory 0.1, 0.2]
* **연결:** A, T, K, O, 새 Axis U

#### Axis S. Generalization & Robustness [encoding-foundation]
* **추가 Sub-axis:** Pretraining Contamination & Stimulus Provenance, Leakage-controlled Splits(stimulus/movie/subject/temporal block), Synthetic-to-Real Generalization, Preprocessing & Space Shift, Cross-paradigm Generalization [encoding-foundation]
* **구체화:** "Invariance / Equivariance"를 모달리티 불변성(초감각성)과 맥락 불변성으로
* **대표 논문:** arXiv:2605.04326, arXiv:2507.22229, doi:10.1126/sciadv.adk6840, arXiv:2403.11207, arXiv:2607.16292
* **미해결 문제:** Omni-fMRI 정서 benchmark가 무작위 블록 분할과 portrayed 라벨로 보여 누수 가능성 [encoding-foundation, 라벨 출처 미확인]
* **연결:** T(leakage audit), F, H, M

#### Axis T. Scientific Discovery & Evaluation [adversarial-reviewer]
* **추가 Sub-axis:** Analytic Robustness & Multiverse, Surrogate Label Validity & Downstream Inference(PPI, DSL, alt-test), Model Identifiability & Adjudicating Stimulus Design, Leakage Audit & Evaluation Hygiene, Explainable-variance Accounting without Repeats, Small-N Population & Stimulus-population Inference, Pseudo-prospective Validation of In-silico Predictions [adversarial-reviewer S1~S7]
* **재정의:** Controlled Baselines와 Ablation Studies를 "Controlled Baselines & Matched-Complexity Nulls"로 병합; Benchmarking을 "Benchmarking with Ceilings and Reliability"로; Variance Partitioning을 "Reliability-aware Variance Partitioning"으로 강화
* **대표 논문:** doi:10.1126/science.adi6000, doi:10.1073/pnas.1912334117, doi:10.1371/journal.pone.0152719, arXiv:2501.10970, doi:10.1162/imag.a.134
* **핵심 비판(방법론):** Horikawa 2020의 "정서 모델이 시각, 의미 모델보다 낫다"는 세 모델을 따로 적합해 비교한 결과이며, 의미 공변량에 측정 오차가 있으면 정서 고유 기여가 위양성으로 나올 수 있다(doi:10.1371/journal.pone.0152719). Westlin 2025도 NMI에 chance 보정이 없고 본문 수치가 서로 맞지 않는다("모든 NMI < 0.01"인데 평균 0.0141). Ma & Kragel의 효과는 Fisher z 차이 약 0.005로 작고 TEM을 대안 모델과 비교하지 않았다 [adversarial-reviewer]
* **연결:** 모든 Axis. 0.2절 minimum-validation 태그의 출처

---

## 2. 새 독립 Axis

### 2.1 Coordinator 판정 기준
`reference/axes.md`는 "새로운 Axis를 발견하면 기존 분류에 무리하게 넣지 말고 독립 Axis로 추가한다"고 정한다. 동시에 조합 단계(P5)의 무작위 경로는 유형마다 Axis 하나를 뽑으므로, 내용이 겹치는 Axis가 많아지면 조합이 중복된다. 그래서 다음 기준으로 판정했다.
1. 기존 Axis 어느 하나에 넣으면 그 Axis의 정의가 바뀌거나 시야가 좁아지는가
2. 서로 다른 에이전트가 독립적으로 비슷한 제안을 했는가
3. 4개 데이터셋(또는 사용자가 쓸 수 있는 데이터)에서 질문을 만들 수 있는가
4. 같은 개념이 "모든 질문에 붙는 태그"로 더 잘 다뤄지는가

### 2.2 채택한 새 Axis

> **사용자 결정 반영 (2026-11-12, Stage 3 시작 전):** 사용자가 "일단 진행해"라고 답해 선택지를 고르지 않았으므로 Coordinator 권장안을 적용했다. **U, V, W는 독립 Axis로 채택**하고, **X는 Axis R의 Sub-axis "Model-internal Emotion Representations"로, Y는 Axis A의 Sub-axis "Introspective Access and Emotion Report"로 조정**했다. 이유: 4개를 모두 Construct 유형에 넣으면 무작위 조합이 새 Axis로 쏠리고, Y는 데이터에 직접 측정이 없으며, X는 대상이 뇌가 아니라 AI라 하위 항목으로도 내용이 보존된다. W의 데이터 조건은 사용자가 Horikawa 2025 Mind captioning 데이터(ds005191, 전처리 완료)를 쓸 수 있다고 확인해 충족되었다. 사용자가 다른 안을 고르면 다시 고친다.

| Axis | 이름 | 유형 | 제안 | 판정 근거 | 대표 근거 |
|---|---|---|---|---|---|
| **U** | **Label Provenance & Perspective** (라벨 출처와 관점: 본인 경험, peer 합의, 별도 평정자 규범, 타인 지각 판단, AI 추정; 대상 portrayed / perceived / felt) | Inference & Measurement | adversarial-reviewer(독립 Axis 후보), llm-semantics(S4 Machine Raters & Annotation Provenance), emotion-theory(S2 격자, 필수 태그로 제안), generative-counterfactual(S6) | 4개 에이전트가 독립적으로 제안. A, C, Q, T에 흩어져 있고 Stage 1의 데이터셋 결합 판정(3절)도 이 변수로 결정된다. NSD 정서 분석은 거의 전적으로 AI 추정 라벨에 의존. **동시에 0.2절의 필수 태그로도 유지한다**(emotion-theory 의견 반영) | arXiv:2501.10970, doi:10.1126/science.adi6000, doi:10.1162/imag.a.134, doi:10.1162/imag_a_00517, arXiv:2408.13718 |
| **V** | **Action Readiness & Affordance** (행동 경향, 방어 계산, 장면 affordance) | Construct | brain-inspired(S-6), frontier-ai(U8 정서의 동기 성분, Latent Action) | 정서 범주(A)와 경쟁하는 구성 개념이며 지각(B)도 계산(N)도 아니다. Horikawa 원 저자가 결과를 "emotional experience (or affordances)"로 표현했고, Emo-FilM에 Motivation 10개 항목이 있다. **[Stage 3 정정]** adversarial-reviewer가 Horikawa 2020 원문(PMC7191651 서론 마지막 단락)을 대조한 결과, 이 affordance는 행동 affordance가 아니라 "장면이 특정 정서를 일으킬 것이라는 시각적 추론"(정서 affordance)이었다. 이 문장은 Axis V의 근거가 아니라 Axis U 쪽 질문의 근거다. Axis V의 근거는 Frijda의 action readiness, component process model, Thornton & Tamir 2024(doi:10.1038/s41467-024-44870-7)와 Emo-FilM Motivation 항목으로 다시 세운다(`outputs/agents/adversarial-reviewer/round3_top10_review.md` F2). 측정 타당성은 RQ-39(MTMM)에서 먼저 검증한다 | doi:10.1073/pnas.2414005122, arXiv:2410.11758, doi:10.1016/j.isci.2020.101060 |
| **W** | **Internally Generated Experience** (Memory, Imagery, Recall) | Construct | vision-decoding(조건부 제안) | 외부 분야 Memory and Mental Imagery가 조합 규칙에서 Axis로 쓰이게 한다. **조건부:** 정서 imagery 전용 데이터가 없고, 가장 적합한 데이터(Horikawa 2025 mind captioning의 회상 과제)는 4개 보유 데이터셋 밖이다. NSD-Imagery, NSD recognition 판단, Spacetop shortvideo 재노출로 부분적으로 가능 | doi:10.1126/sciadv.adw1464, arXiv:2506.06898 |
| **X (R의 Sub-axis로 조정)** | **Machine Affect Representations** (AI 내부 정서 표상: 정서 vector 기하, 국소성 vs 지속성, 관점 결속, appraisal 회로, 행동 인과성) | Construct | frontier-ai(독립 Axis 제안), llm-semantics(LLM 내부 appraisal 방향 chain) | 2025~2026년 AI 연구가 모델 내부 정서 표상을 측정 대상으로 다루기 시작했다. I(모델 종류)나 R(해석 방법)에 두면 "AI 정서 표상과 뇌 정서 표상이 어디서 같고 다른가"라는 비교 대상이 사라진다. **정의에 "모델 내부 표상을 주관 경험으로 해석하지 않는다"는 단서를 포함**(arXiv:2604.07729 저자들의 단서) | arXiv:2604.07729, arXiv:2609.34742, arXiv:2502.05489, arXiv:2310.01405 |
| **Y (A의 Sub-axis로 조정)** | **Metacognition & Introspective Report** (정서 보고의 privileged access, 보고 확신도, 정서 schema와 언어, 보고 행위의 영향) | Construct | emotion-theory(S3) | 외부 분야 Artificial Consciousness and Metacognition의 핵심이며 A, N, R에 걸친다. **데이터 제약:** 4개 데이터셋에 보고 확신도나 재평정 일관성 측정이 없다. 대신 Spacetop의 본인 보고 vs peer 합의 비교, Emo-FilM의 consensus vs 참가자 사후 평정 비교로 "본인 보고의 고유 설명력"(privileged access의 약한 검정)을 다룰 수 있다 | doi:10.1073/pnas.1619316114, doi:10.1016/j.tics.2019.06.009 |

### 2.3 독립 Axis로 채택하지 않은 제안 (이견 기록)

| 제안 | 제안 에이전트 | Coordinator 판정 | 이유 | 이견 |
|---|---|---|---|---|
| Acquisition & Signal Physics | systems-neuro | 독립 Axis 대신 **필수 태그 signal-feasibility**(0.2절)와 E, Q의 Sub-axis | 연구 질문의 대상이라기보다 모든 neural target 주장의 전제 조건이다. 태그로 두면 매 질문에서 점검된다 | systems-neuro는 "Q의 하위로 두면 E 쪽 판단에서 누락된다"며 독립 Axis를 주장. 태그화로 누락 우려에 대응했으나 이견으로 남긴다 |
| Computational Psychiatry Phenotyping | systems-neuro | O의 Sub-axis + 외부 분야 표시 | 임상 표본이 없고 설문(Spacetop 미공개, Emo-FilM DASS 등 30명)이 제한적이다 | systems-neuro는 "O는 개인차의 표상, 이 방향은 임상 표현형을 만드는 측정 설계"라며 구분을 주장. Stage 3 조합에서 외부 개념 요건 단위로 쓸 수 있도록 외부 분야 목록에는 유지 |
| Information-theoretic Efficiency of Affective Categories | geometry-info | K의 Sub-axis | 제안자 스스로 "우선 K의 sub-axis로 두고 Round 2에서 논의"를 제안 | Stage 3에서 llm-semantics, emotion-theory와 재논의 |
| Aesthetic & Value Experience | multimodal-dynamics | A, D, N 교차 Sub-axis | 제안자 스스로 문헌량이 적어(7편) Stage 3 조합 빈도를 보고 결정하자고 제안 | Stage 3에서 재검토 |
| In-silico vs Observed | encoding-foundation | 필수 태그 insilico-vs-observed | 제안자도 독립 Axis는 불필요, 태그로 추적하자고 제안 | 없음 |
| Recognition vs Experience | emotion-theory | Axis U에 흡수 + 필수 태그 label-provenance | emotion-theory는 Axis가 아니라 필수 태그를 제안 | emotion-theory는 독립 Axis 불필요 입장, adversarial-reviewer와 llm-semantics는 독립 Axis 입장. Coordinator는 둘 다 채택(Axis U + 태그). 이 처리 자체가 이견 지점 |

---

## 3. 갱신된 Axis 유형표 (`reference/axes.md` 1절 갱신본)

조합 단계(P5)의 무작위 경로는 이 표를 쓴다. X(Machine Affect Representations)는 R의 Sub-axis, Y(Metacognition & Introspective Report)는 A의 Sub-axis로 두었다(2.2절 사용자 결정 반영). `reference/axes.md` 원본은 사용자 지침 파일이라 고치지 않았다.

| 유형 | Axis | 주 담당 에이전트 |
|---|---|---|
| Construct (무엇을 묻는가) | A Emotion & Affective Constructs | emotion-theory |
| | B Perceptual & Stimulus Representation | vision-decoding |
| | C Context, Meaning & Narrative | llm-semantics |
| | D Temporal Dynamics | multimodal-dynamics |
| | **V Action Readiness & Affordance** (신규) | brain-inspired |
| | **W Internally Generated Experience** (신규, 데이터 조건 충족: Mind captioning) | vision-decoding |
| Neural (뇌의 어디, 어떤 형식) | E Neural Targets | systems-neuro |
| | F Brain Representation | encoding-foundation |
| | O Individual & Population Variation | geometry-info |
| Model & Method (무엇으로 푸는가) | G Decoding | vision-decoding |
| | H Encoding | encoding-foundation |
| | I AI Model Families | frontier-ai |
| | J Learning Objectives | frontier-ai |
| | L Generative & Counterfactual Methods | generative-counterfactual |
| | M Multimodal Integration | multimodal-dynamics |
| | N Brain-like Computation | brain-inspired |
| Structure & Interpretation (어떤 구조로 보는가) | K Geometry & Mathematical Structure | geometry-info |
| | R Explainability & Mechanistic AI | frontier-ai |
| Inference & Measurement (어떻게 검증하는가) | P Causality & Scientific Inference | generative-counterfactual |
| | Q Reliability & Measurement | emotion-theory |
| | S Generalization & Robustness | encoding-foundation |
| | T Scientific Discovery & Evaluation | adversarial-reviewer |
| | **U Label Provenance & Perspective** (신규) | emotion-theory, llm-semantics (공동), adversarial-reviewer (검토) |

**모든 질문에 붙는 필수 태그:** label-provenance, evidence-level, insilico-vs-observed, G1, signal-feasibility, minimum-validation (0.2절)

**외부 분야 목록 갱신** (`reference/axes.md` 3절에 추가 제안): Computational Psychiatry Phenotyping(systems-neuro), Information Bottleneck / Rate-distortion(geometry-info), Statistics of Surrogate Labels(PPI, alt-test; adversarial-reviewer), Situation Recognition in Computer Vision(llm-semantics), Game Affective Computing(llm-semantics), Model Metamers(adversarial-reviewer)

---

## 4. 이 문서의 한계

* Round 1은 독립 탐색이므로 Sub-axis 제안 간 중복과 충돌을 에이전트들이 서로 검토하지 않았다. 묶음과 채택 판정은 Coordinator 판단이며 Stage 3 Round 2~3에서 수정될 수 있다.
* 대표 논문은 DB의 relevance 점수와 담당 에이전트 기준으로 자동 선별했다. relevance는 각 에이전트의 자기 평가 점수다.
* 대표 논문 선별은 Round 1 시점 `literature_db.csv`(고유 377편, verified 365편) 기준이다. Stage 2 재점검 후 DB는 고유 381편, verified 377편이다. 인용 표본 검증 결과는 `outputs/literature/verification_sample.md`에 있다.
