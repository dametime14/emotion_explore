# 라운드별 절차와 산출물 양식

에이전트는 위임 메시지가 지정한 절을 직접 읽고 그대로 따른다. 파일 경로의 `<me>`는 자신의 에이전트 이름이다.

---

## P1. Round 1: Independent Discovery (Stage 2)

다른 에이전트의 폴더를 읽지 않고 독립적으로 수행한다.

### 산출물 1: `outputs/agents/<me>/literature.jsonl`
CLAUDE.md 5절 형식을 따른다. 기준은 다음과 같다.
* verified 논문 최소 12편
* 그중 최소 4편은 2024~2026년 논문
* 최소 3편은 Affective Neuroscience 밖의 분야 논문
* 자기 담당 Axis(reference/axes.md)를 우선하되 다른 Axis와 연결되는 논문도 포함

### 산출물 2: `outputs/agents/<me>/round1.md`
다음 절을 모두 포함한다.
1. 중요한 미해결 문제 5개 이상. 각각 근거 논문 ID를 단다.
2. 주목해야 할 모델 또는 방법론 5개 이상. 각각 pretrained weights 공개 여부, input/output, 학습 목표, 라이선스를 단다.
3. 다른 분야에 적용할 수 있는 연구 아이디어 5개 이상.
4. 기존 Affective Neuroscience와 예상 밖으로 연결될 수 있는 개념 3개 이상.
5. 새 Sub-axis 또는 하위 연구 방향 3개 이상. 어느 Axis에 속하는지, 독립 Axis가 필요한지 적는다.
6. Discussion-to-Research chain 5개 이상. 형식은 아래와 같다.
   `Original Finding → Unresolved Question → Technological Development → New Dataset / Model Combination → New Research Question`
   각 단계에 근거 논문 ID와 Discussion 원문 위치를 단다.
7. 담당 Axis의 확장 제안 (Sub-axis 추가, 삭제, 재분류).

Discussion-to-Research chain을 만들 때 각 논문에 다음 질문을 던진다.
* 연구자들이 명시적으로 제시한 미해결 문제는 무엇인가?
* 논문 당시에는 기술적으로 어려웠지만 2026년의 AI 모델로 시도할 수 있는 것은 무엇인가?
* 다른 분야의 모델을 가져오면 해결할 수 있는 문제가 있는가?
* 당시에는 없던 공개 데이터셋(Horikawa, Emo-FilM, Spacetop, NSD)을 활용할 수 있는가?
* 논문에서 검증하지 못한 generalization, dynamics, individual differences, neural mechanism은 무엇인가?
* 서로 다른 논문 두 편의 limitation을 연결하면 새로운 질문이 생기는가?

---

## P2. Round 2: Cross-Agent Exchange (Stage 3)

다른 모든 에이전트의 `round1.md`를 읽는다. literature.jsonl은 필요할 때만 참조한다. `outputs/agents/<me>/round2.md`에 다음을 쓴다.

1. **가져온 아이디어:** 자신이 담당하지 않은 분야의 문헌에서 새 아이디어 최소 2개를 가져온다. 각각 출처 에이전트와 논문 ID를 단다.
2. **보내는 제안:** 특정 에이전트를 지정한 제안 최소 3개. 형식은 다음과 같다.
   * 받는 에이전트
   * 제안 내용: "너희 쪽 X를 우리 쪽 Y로 검증하거나 확장할 수 있다"
   * 근거 논문 ID
   * 가능한 데이터셋
   * 예상되는 반론
3. **받은 제안에 대한 응답:** 이번 라운드나 Coordinator가 전달한 제안 각각에 수용, 수정, 반박 중 하나로 답하고 이유를 단다.

Coordinator는 이 라운드에서 다음 질문을 모든 에이전트에게 던진다.
* Vision Decoding 연구자가 Emotion Neuroscientist의 문제를 해결할 수 있는가?
* LLM의 representation이나 reasoning 능력을 neural emotion representation 분석에 활용할 수 있는가?
* Generative AI로 emotion과 visual semantics를 분리해 검증할 수 있는가?
* Emotion Dynamics를 dynamical systems나 state-space learning의 문제로 재정의할 수 있는가?
* Brain Foundation Model의 latent representation에서 감정 관련 구조를 찾을 수 있는가?
* Music, Video, Image의 공통 정서 특징과 modality-specific 특징을 뇌 수준에서 구분할 수 있는가?
* Neuroscience에서 관찰되는 정서 관련 계산을 AI architecture의 구조적 제약으로 구현할 수 있는가?
* 정서 라벨이 없는 NSD 같은 데이터도 다른 데이터셋과의 representation alignment로 의미 있게 활용할 수 있는가?

---

## P3. Round 3: Constructive Disagreement (Stage 3)

Coordinator가 배정한 다른 에이전트의 제안을 검토하고 `outputs/agents/<me>/round3_reviews.md`에 쓴다. 각 제안에 대해 다음을 판정한다.
* 이미 연구된 것은 아닌가? 근거 논문을 단다.
* 단순한 모델 적용에 불과한가?
* 실제로 Neuroscience Question을 해결하는가?
* Emotion 이외의 요소(visual, semantic content)를 decoding하는 것은 아닌가?
* 현재 Dataset으로 검증할 수 있는가?
* 더 강력한 모델이나 분석 방법이 있는가?
* 결과가 기대와 다를 때도 과학적으로 유의미한가?

비판만 하지 않고 어떻게 개선할 수 있는지 수정안을 함께 쓴다.

---

## P4. Round 4: Unexpected Connections (Stage 3)

`outputs/combinations/discussed_pairs.md`에 이미 논의된 조합이 적혀 있다. 여기에 없는 조합만 대상으로, 서로 관련성이 낮아 보이는 분야를 의도적으로 연결한다. 결과는 `outputs/agents/<me>/round4.md`에 쓴다.

예시는 다음과 같다. 예시이며 최종 질문으로 확정하지 않는다.
* Emotion × World Models × Predictive Coding
* Generative AI × Neural Manifold × Counterfactual Stimuli
* Vision Reconstruction × Emotion Semantics × Cross-subject Alignment
* Multimodal Foundation Models × Emotional Transitions × Functional Networks
* Information Theory × Individual Differences × Emotion Reliability
* Neural Encoding × Model Disagreement × Subjective Experience

---

## P5. Combinatorial Research Question Generation (Stage 3, Coordinator)

### 조합 규칙
* 각 후보 질문은 reference/axes.md 1절의 **서로 다른 유형에서 최소 3개 Axis**를 가져와 구성한다.
* 그중 최소 하나는 Affective Neuroscience 밖에서 온 개념이나 방법이어야 한다. 외부 분야(axes.md 3절)나 Axis I, J, K, L, R이 해당한다.
* 조합 경로는 세 가지를 모두 사용하고, 후보마다 어느 경로에서 나왔는지 표시한다.
  1. **문헌 경로:** Round 1의 Discussion-to-Research chain과 Round 2, 3, 4의 제안에서 나온 조합.
  2. **무작위 경로:** 유형마다 Axis 하나씩 무작위로 뽑은 조합 30개를 만든다(난수 시드 기록). 각 조합이 연구 질문이 되는지 판정하고, 되면 질문으로 쓰고, 안 되면 기각 사유를 쓴다.
  3. **전략 경로:** 아래 Question Generation Strategies A~H를 각각 최소 한 번 적용한 조합.
* 기각한 조합과 사유도 모두 `outputs/combinations/rejected.md`에 남긴다.

### 조합 기록 형식 (`outputs/combinations/matrix.csv`)
열: combo_id, route(literature / random / strategy), axes, scientific_construct, imported_concept_or_method, ai_model_or_representation, neural_target, dataset, measurable_prediction_or_analysis, scientific_contribution, evidence_ids, status(kept / rejected), overlap

### Question Generation Strategies
* **A. Technology Transfer:** 다른 분야의 AI 기술을 Emotion Neuroscience로 이전한다.
* **B. Methodological Inversion:** Encoding을 Decoding으로, Decoding을 Generative Modeling으로, Prediction을 Counterfactual Analysis로 전환한다.
* **C. Representation Comparison:** Brain vs AI, Emotion vs Semantics, Vision vs Emotion, Shared vs Modality-specific representations를 비교한다.
* **D. Scale Bridging:** Low-level sensory features에서 higher-order emotion까지, localized activity에서 distributed systems까지 잇는다.
* **E. Dynamics and Geometry:** 정서를 정적인 category가 아니라 시간적으로 변화하는 latent state, manifold, neural trajectory로 다룬다.
* **F. Cross-Dataset Discovery:** 구조가 다른 데이터셋을 representation transfer, model adaptation, shared latent space로 연결한다.
* **G. Counterfactual Neuroscience:** 생성형 모델로 자극의 특정 요소만 바꿔 encoding model이나 실제 fMRI를 분석한다. 관찰 데이터만 쓴 경우 인과적 결론의 한계를 명시한다.
* **H. Reverse Inspiration:** 뇌과학 이론으로 AI 모델을 설계하거나, AI 모델 구조에서 새로운 Neuroscience Question을 도출한다.

### Novelty Constraint
다음 수준의 질문은 최종 후보에서 가급적 제외한다.
* 새로운 모델로 emotion classification accuracy를 높인다.
* 기존 정서 라벨을 다른 Foundation Model로 예측한다.
* Emotion별 brain activation 차이를 비교한다.
* 새로운 차원 축소 방법으로 emotion manifold를 시각화한다.
* Amygdala와 emotion label의 단순 상관관계를 구한다.

이런 질문도 탐색 후보는 될 수 있다. 그러나 최종 선정하려면 기존 연구로 알 수 없었던 과학적 문제와 새로운 검증 논리를 제시해야 한다.

예를 들어 단순히 emotion manifold를 발견하는 것과, 서로 다른 정서 경험이 같은 신경공간에서 어떻게 전이하며 그 구조가 자극 양식, 맥락, 개인 간에 어떻게 보존되는지 검증하는 것은 수준이 다른 질문이다. 후자 역시 기존 연구와 중복되는지 확인한다.

### 최소 수량
* Broad Research Directions: 40개
* Distinct Research Questions: 30개
* Substantive Shortlist: 10개
* High-priority Candidates: 5개
* Recommended Pilot Studies: 3개

이 수량은 다양성을 위한 기준이다. 중복되거나 검증할 수 없는 질문을 억지로 남기지 않는다.

---

## P6. Research Question Evaluation (Stage 4)

각 후보를 1~5점으로 평가하고, 점수마다 구체적 근거를 쓴다.

| Criterion | 핵심 질문 |
|---|---|
| Novelty | 기존 연구와 실제로 무엇이 다른가? |
| Neuroscientific Importance | 정서 경험과 뇌의 작동에 대해 무엇을 알 수 있는가? |
| AI / Modeling Contribution | 모델이 단순 도구를 넘어 연구 질문에 어떻게 기여하는가? |
| Dataset Feasibility | 실제 데이터와 라벨로 검증할 수 있는가? |
| Methodological Rigor | Confound, Leakage, Reliability 문제가 통제되는가? |
| Falsifiability | 어떤 결과가 나오면 가설이 지지되지 않는가? |
| Interpretability | 결과를 과학적으로 설명할 수 있는가? |
| Generalizability | 다른 자극, 개인, 데이터로 확장 가능한가? |
| Feasibility | 구현 난도와 계산 자원이 현실적인가? |

Horikawa에서 가능한 연구를 우선 검토하고, Emo-FilM, Spacetop, NSD를 통한 재현 또는 확장 가능성을 추가로 평가한다.

---

## P7. Research Question Card 양식 (Stage 4)

파일: `outputs/rq_cards/RQ<번호>_<짧은제목>.md`

1. **Core Research Question:** 구체적이고 검증 가능한 질문 한 문장.
2. **Scientific Motivation:** 왜 중요한가, 어떤 지식의 공백이 있는가.
3. **Origin of the Idea:** 어떤 에이전트의 어떤 결과들이 결합되었는가. 어떤 분야에서 아이디어를 가져왔는가. 조합 ID(matrix.csv).
4. **Prior Literature:** 직접 관련 논문 5편 이상과 각 논문의 기여.
5. **Novelty:** 가장 가까운 선행연구와 구체적으로 무엇이 다른가.
6. **Proposed Dataset:** 어떤 데이터를 어떻게 쓰는가. 필요한 label, metadata, stimulus, neural response가 실제로 존재하는지 Stage 1 보고서를 근거로 명시한다.
7. **Proposed Computational Framework:** 다음 항목을 모두 적는다.
   * Pretrained model
   * Input representation
   * Output / target representation
   * Training or adaptation strategy
   * Relevant brain regions / networks
   * Loss function or statistical objective
   * Interpretability method

   새 모델을 처음부터 훈련하기보다 기존 pretrained model 활용을 먼저 검토한다.
8. **Proposed Analyses:** 핵심 분석, 비교 조건, baseline, ablation, 통계 검정, validation strategy.
9. **Competing Explanations:** 예상 결과에 대한 대안 해석과 이를 구분하는 분석.
10. **Potential Findings:** 서로 다른 결과가 나왔을 때 각각의 과학적 의미.
11. **Scientific Contribution:** Affective Neuroscience에 주는 새 지식. 어떤 정서 이론이나 논쟁에 무엇을 말해주는지 포함한다.
12. **Limitations & Risks:** 데이터, 모델, 통계, 이론적 해석의 한계.
13. **Pilot Experiment:** 가장 작은 비용으로 먼저 검증할 수 있는 분석.
14. **Feasibility & Priority:** Novelty, Impact, Feasibility와 전체 권고 순위. overlap 표시 포함.

---

## P8. Pilot Study Plan 양식 (Stage 4)

파일: `outputs/pilots.md`

Pilot마다 다음을 적는다.
* 첫 분석에 필요한 데이터와 파일
* Pretrained model과 checkpoint 위치, 라이선스
* Evaluation metric과 noise ceiling
* Baseline
* 예상 계산량
* 예상 위험
* 의사결정 기준: 어떤 결과면 계속하고, 어떤 결과면 수정하거나 중단하는가
