# RQ-15. AI의 정서를 잴 때, AI 속을 들여다보는 것과 AI에게 물어보는 것 중 무엇이 사람 뇌와 더 닮았을까?

* 카드 작성: frontier-ai (기원 제안 FA-P6)
* 기준일: 2026-11-12
* 조합 ID: LIT-13 (`outputs/combinations/matrix.csv`), 군집 K3(라벨 출처와 관점)
* 선정 상태: Substantive Shortlist 3번, High-priority 2위, Recommended Pilot P3 (`outputs/evaluation/selection.md`)
* 선행 감사 판정: **not found** (`outputs/evaluation/prior_overlap_audit.md` RQ-15 절)
* 읽은 자료: CLAUDE.md 4~7절, `reference/protocols.md` P7, `outputs/evaluation/selection.md`, `outputs/rq_landscape.md` 4절 RQ-15 블록과 용어 풀이, `outputs/combinations/matrix.csv` LIT-13 행, `outputs/evaluation/prior_overlap_audit.md` RQ-15 절, `outputs/evaluation/reviewer_notes.md`(RQ-15 행, 4.4절, 5절 전제 표), `outputs/discussion_record.md`, `outputs/discussion/round3_summary.md`와 FA-P6 Round 3 검토 원문(generative-counterfactual, vision-decoding), `outputs/stage1/dataset_Horikawa.md`, `outputs/stage1/horikawa_factcheck_stage4.md`, `outputs/STAGE_STATUS.md` "사용자 답변, Stage 3 이후" 표

## 이 카드에서 쓰는 말 (쉬운 뜻)

| 용어 | 쉬운 뜻 |
|---|---|
| VLM (vision-language model) | 영상이나 이미지를 보고 글로 답하는 AI 모델 |
| 내부 표상 읽기 | 모델이 답을 내기 직전, 모델 속 숫자 상태(hidden state)를 꺼내서 미리 정해 둔 "정서 방향"에 얼마나 가까운지 재는 것 |
| 출력 묻기 | 모델에게 "이 영상에서 느껴질 정서를 0~100으로 매겨라"라고 묻고 답한 숫자를 쓰는 것 |
| 정서 방향 (emotion direction) | 모델 속 공간에서 특정 정서(예: 공포)에 해당하는 방향. 정서가 분명한 예시와 그렇지 않은 예시의 평균 차이로 구한다 |
| encoding model | 자극의 특징으로 뇌 반응을 예측하는 모델 |
| 고유 설명량 (unique variance) | 다른 특징을 모두 넣은 뒤에 어떤 특징을 더 넣었을 때 늘어나는 예측력 |
| matched-complexity null | 비교하는 특징과 개수, 형식을 똑같이 맞춘 "의미 없는" 대조 특징. 예: 같은 수의 무작위 방향 |
| 사전학습 오염 | 모델이 학습할 때 시험에 쓸 영상이나 정답을 이미 봤을 가능성 |
| noise ceiling | 잡음 때문에 어떤 모델도 넘을 수 없는 예측 상한 |

---

## 1. Core Research Question

* **(a) 한 줄 질문:** AI의 정서를 잴 때, AI 속을 들여다보는 것과 AI에게 물어보는 것 중 무엇이 사람 뇌와 더 닮았을까?
* **(b) 검증 가능한 세부 질문:** 같은 공개 VLM이 같은 정서 영상을 한 번 처리할 때, 답하기 직전 hidden state를 독립 자료로 구한 34개 정서 방향에 투영한 값(내부 표상)과 그 직후 모델이 내놓은 34개 정서 평정(출력) 중 어느 쪽이, 시각 내용과 장면 의미를 두 겹으로 통제하고 차원, 신뢰도, 형식을 맞춘 null을 넘어, 같은 영상을 본 사람의 뇌 반응을 더 많이 고유하게 설명하는가?

## 2. Scientific Motivation

* **AI 정서 라벨이 신경 분석에 빠르게 들어오고 있다.** MLLM(멀티모달 대형 언어 모델)의 출력으로 만든 정서 공간이 Horikawa 데이터의 뇌 반응을 사람 평정보다 잘 예측했다는 보고(Du 2025), MLLM 연속 평정을 encoding 회귀자로 쓴 연구(Huang 2026), GPT-4V 평정으로 만든 뇌 지도가 사람 평정 지도와 비슷하다는 보고(Santavirta 2025)가 있다. 그런데 이 연구들은 모두 **모델에게 물어본 답(출력)**만 썼다.
* **모델 속에는 답보다 많은 정서 정보가 있을 수 있다.** LLM에서는 hidden state로 읽은 정서가 zero-shot으로 물어본 답보다 정확했다(Zhang 2025). 모델 출력은 사람보다 "너무 범주적"이라는 보고도 있다(Bhattacharyya 2025). 그렇다면 출력만 쓰는 지금의 관행은 모델 정서 정보의 일부만, 그것도 범주화로 왜곡된 형태로 뇌와 비교하는 셈일 수 있다.
* **비어 있는 지식:** 같은 모델에서 두 측정 방식 중 무엇이 사람 뇌의 정서 관련 분산과 더 맞는지 비교한 연구가 없다(감사 판정 not found). 이것은 Axis U(라벨 출처)에서 "AI 추정"을 하나의 출처로 볼지, 출력과 내부 표상으로 나눠야 할지를 정하는 근거가 된다.
* **이론과의 연결(가설로만):** 내부 표상과 출력의 구분은 정서의 1차 상태와 보고 수준을 나누는 higher-order theory(HOT, LeDoux & Brown 2017)의 구분과 모양이 닮았다. 그러나 모델의 두 측정이 사람의 두 수준과 같다는 주장은 하지 않는다. 결과가 이 구분에 대해 말해 줄 수 있는 것은 "뇌의 정서 관련 분산이 보고 이전 형태의 신호와 보고된 판단 중 어느 쪽 구조에 가까운가"라는 약한 형태뿐이다.

## 3. Origin of the Idea

* **조합 ID:** LIT-13 (Axis R+U+C+F+Q).
* **기원 제안:** frontier-ai **FA-P6**(Round 2, llm-semantics에게 보낸 "내부 표상 읽기 vs 출력 묻기"). 보조 기원: FA-P5(관점 무차별 모델 기준선, 일부), GC-P9(일부).
* **결합된 결과:**
  * frontier-ai Round 1: 모델 내부 정서 vector 문헌(Sofroniew 2026, Xing 2026, Tak 2025)과 "AI 정서 표상과 뇌 정서 표상의 비교" 방향(U1, T8).
  * llm-semantics Round 1: 세 층 분해(L1 장면 기술, L2 귀속된 정서 의미, L3 경험)와 Chain 1(정서 배제 캡션의 잔차). 이 카드는 L2 층을 두 방식으로 재는 설계다.
  * Round 3 검토 두 건: generative-counterfactual(같은 모델 안 null, steering 사전 검사, 오염 점검, HOT로 재구성), vision-decoding(같은 forward pass, 차원과 신뢰도 정합, 시각 이중 통제, 회상 일반화). 수정안이 `round3_summary.md`에 하나로 정리되었다.
  * Stage 4 평가: adversarial-reviewer가 C&K 공개 지도에 의한 사전학습 오염이 출력 쪽을 유리하게 할 수 있다고 지적했다(같은 이유로 RQ-19의 Novelty도 조정).
* **가져온 분야:** mechanistic interpretability(representation reading, steering), LLM probing 연구, 사전학습 데이터 탐지(contamination detection).

## 4. Prior Literature

모든 논문은 `outputs/literature/literature_db.csv`의 verified 항목이거나 frontier-ai가 식별자로 확인해 `outputs/agents/frontier-ai/literature.jsonl`에 넣은 것이다. 읽은 수준을 [본문] / [초록] / [서지]로 표시한다.

| # | 논문 | ID | 읽은 수준 | 이 질문에 대한 기여 |
|---|---|---|---|---|
| 1 | Du et al. (2025). Bridging the behavior-neural gap | arXiv:2509.24298 | [본문] (frontier-ai 직접) | **가장 가까운 선행 1.** Qwen2-VL과 Llama-3.1의 triplet odd-one-out 판단(출력)으로 만든 30차원 정서 embedding이 Horikawa 뇌를 인간 평정 embedding보다 잘 예측. 내부 표상은 쓰지 않았다. 비정서 프롬프트 대조와 시각 전용 모델 기하 통제는 본문에서 확인되지 않았다(DB 검토자 기록) |
| 2 | Huang, Zhang, Biswal (2026). Brain-Aligned Multimodal LLMs for Social and Emotional Understanding of Cartoon Movies | arXiv:2610.22706 | [초록] (DB) | **가장 가까운 선행 2.** MLLM 연속 평정(출력)과 인간 평정을 각각 encoding 회귀자로 사용. 인간과 모델 평정의 encoding 공간 중첩은 제한적. 내부 표상 비교 없음 |
| 3 | Zhang, Zhong et al. (2025). Decoding Emotion in the Deep | arXiv:2510.04064 | [초록] | **가장 가까운 선행 3.** LLM hidden state의 정서 probe가 zero-shot prompting보다 정확. 뇌 자료 없음. 내부 > 출력이라는 사전 기대의 근거 |
| 4 | Sofroniew et al. (2026). Emotion Concepts and their Function in a Large Language Model | arXiv:2604.07729 | [본문] | 정서 개념 vector 추출(합성 이야기), steering으로 행동 인과성 확인, valence와 arousal 축. 정서 표상이 "국소적"이며 주관 경험을 함의하지 않는다는 단서. 내부 표상 읽기 방법의 근거 |
| 5 | Xing et al. (2026). Do Emotion Concepts Generalize Across Sources, Modalities, and Architectures in VLMs? | arXiv:2609.34742 | [본문] | VLM(Qwen3-VL-8B, InternVL3.5-8B 등)에서 텍스트와 이미지로 구한 정서 vector의 대응, 정서와 무관한 activation으로 추정한 정렬이 정서 대응을 운반. 정서 방향이 일반 시각-의미 기하에 실려 있다는 위험의 근거 |
| 6 | Bhattacharyya et al. (2025). Too Categorical to be Human | arXiv:2508.05880 | [본문] (Limitations) | LLM 출력 수준의 정서 개념이 인간보다 범주적이고 균질적. 출력 측정의 편향 방향에 대한 예측 근거 |
| 7 | Asanuma et al. (2025). Correspondence of high dimensional emotion structures (MLLM과 인간) | doi:10.1038/s41598-025-14961-6 | [본문] (DB) | C&K 비디오에서 MLLM 출력과 인간 평정의 RSA는 높고 개별 비디오 수준 일치는 낮음. C&K 자료가 "오디오 없는 짧은 영상"이라는 2차 근거. 출력 기반 |
| 8 | Santavirta et al. (2025). GPT-4V shows human-like social perceptual capabilities | doi:10.1162/IMAG.a.134 | [본문] (DB) | GPT-4V 출력 평정과 인간 평정의 뇌 지도 수렴. 내용 필터로 일부 자극 평정 거부. 출력 기반 |
| 9 | Tak & Gratch (2024). GPT-4 Emulates Average-Human Emotional Cognition | arXiv:2408.13718 | [본문] (DB) | LLM 출력은 개인 당사자보다 "평균 관찰자"에 가깝다. 두 측정 모두 perceived(관찰자 관점)로 표기하는 근거 |
| 10 | LeDoux & Brown (2017). A higher-order theory of emotional consciousness | doi:10.1073/pnas.1619316114 | [본문] (DB) | 1차 상태와 보고 수준 표상의 구분. 이 카드에서는 해석의 비유로만 쓴다 |
| 11 | Horikawa et al. (2020) / Horikawa (2025) Mind captioning | doi:10.1016/j.isci.2020.101060 / doi:10.1126/sciadv.adw1464 | [본문] (DB) | 같은 C&K 비디오를 본 두 코호트, 34/14 규범 평정, 정서 배제 캡션, 72클립 반복과 회상 조건 |
| 12 | Cowen & Keltner (2017) | doi:10.1073/pnas.1702247114 | [본문] (DB) | 비디오 라이브러리와 interactive map 공개. 사전학습 오염 경로의 근거 |
| 13 | Shi et al. (2023). Detecting Pretraining Data from Large Language Models | arXiv:2310.16789 | [초록] | 언어 쪽 사전학습 포함 여부 탐지(Min-K% Prob). 오염 점검 절차의 한 경로 |
| 14 | Zou et al. (2023). Representation Engineering | arXiv:2310.01405 | [본문] | 정서 reading vector와 steering. 방향 추출과 "읽힌 방향이 출력에 쓰이는가" 점검의 방법 근거 |

## 5. Novelty

* **이미 된 것(새로움으로 주장하지 않음):**
  * MLLM 출력으로 만든 정서 표상과 뇌의 비교: Du 2025(같은 Horikawa 비디오), Huang 2026, Santavirta 2025, Asanuma 2025(행동 수준).
  * hidden state probe와 prompting의 비교: Zhang 2025(LLM, 뇌 없음).
  * hidden state를 뇌 encoding 회귀자로 쓰는 것 자체: 언어, 시각 encoding에서 표준이다.
  * VLM 정서 vector의 추출과 steering: Sofroniew 2026, Xing 2026.
* **남는 새 부분(감사의 "남는 새 부분"):** **같은 모델, 같은 forward pass**에서 얻은 내부 표상과 출력을, 차원, 신뢰도, 형식을 맞추고 같은 모델 안의 null과 시각 이중 통제를 둔 상태에서, **사람 뇌의 정서 관련 분산을 고유하게 얼마나 설명하는지**로 직접 비교하는 것. 여기에 (i) 사전학습 오염이 두 측정에 다르게 작용하는지를 점검하는 절차, (ii) 지각에서 학습한 대응이 Mind captioning 회상 조건으로 일반화되는지를 두 측정에서 비교하는 것을 더한다.
* **가장 가까운 선행과의 차이:** Du 2025는 출력(odd-one-out)만, 다른 모델 계열로, 비정서 대조 없이 했다. 이 카드는 같은 모델의 두 측정을 쌍으로 비교하므로 "모델 차이"가 아니라 "측정 방식 차이"를 분리한다. Du 2025 결과는 다른 모델이라 기준선으로 재사용하지 않는다.

## 6. Proposed Dataset

**주 데이터: Horikawa 2020 + Mind captioning (같은 C&K 비디오, 두 독립 코호트)**

| 필요한 것 | 있는가 | 근거와 비고 |
|---|---|---|
| 원본 자극(C&K 비디오) | **있음** | 사용자 보유 확인(2,185개, 모두 무음). 제시 조건이 무음이라는 점은 Horikawa 2020, Mind captioning 본문과 Asanuma 2025가 일치(`horikawa_factcheck_stage4.md`). Mind captioning은 2,196개 중 중복 16개를 뺀 2,180개, Horikawa 2020은 중복 표시 label index 15개를 뺀 2,181개라 **두 코호트의 클립 ID 대응표를 먼저 만들어야 한다**(미확인) |
| Horikawa 2020 fMRI | **있음** | 5명, TR 2 s, 2 mm, 3T Verio. 공개 전처리본은 native volume, 비디오 블록당 1 sample, HCP360과 피질하 ROI 포함. raw BIDS(CC0)도 있음(Stage 1). 반복 제시 없음 |
| Mind captioning fMRI | **있음(전처리 완료, 형식 세부 미확인)** | 6명, TR 1 s, 2 mm, 3T Prisma. 지각 학습 2,180클립 1회(60 run, 6명 모두 같은 의사 무작위 순서), 지각 테스트 72클립 x 5회, 회상 72클립 x 5회(reviewer_notes 4.4) |
| 두 코호트의 피험자 독립 | **있음(사용자 확인)** | 원문에는 언급 없음. 장소, 스캐너, 윤리위원회는 다름 |
| 정서 라벨(C&K 34범주 선택 비율, 14차원 평균) | **있음** | 별도 평정자(MTurk) 규범 평정, 비디오당 집계값. 평정자 개인 자료 없음. 이 카드에서 라벨은 해석과 "C&K 평정 너머의 고유 설명량" 분석에만 쓴다. 뇌 비교의 목표는 뇌 반응 자체다 |
| fMRI 참가자 본인의 정서 보고 | **없음** | 두 코호트 모두 없다. 그래서 "참가자가 느낀 정서"에 대한 결론은 내지 않는다 |
| 정서 배제 인간 캡션 | **있음** | Mind captioning, 클립당 20개(사용자 확인). 시각 이중 통제의 한 축 |
| 회상 조건과 vividness | **있음(논문 기준, 파일 세부 미확인)** | cue는 20개 캡션 중 하나로 고정, 별도 준비 block 후 눈 감고 심상, 원 영상 재시청 후 vividness 5점(reviewer_notes 4.4) |
| VLM 출력과 hidden state | **새로 만든다** | 공개 VLM 추론으로 생성(7절) |
| 정서 방향을 구할 독립 자료 | **새로 만든다** | C&K 클립을 쓰지 않는다. 34개 범주명마다 LLM으로 만든 짧은 정서 이야기(텍스트)와, 일부 범주는 EmoSet(arXiv:2307.07961, DB 등재) 이미지로 확인. EmoSet은 8개 범주라 34범주 전체를 덮지 못한다 |
| 오염 대조용 "라벨이 공개되지 않은" 자극 | **일부 있음** | Spacetop alignvideo 49편(공개 데이터셋에 정서 규범 라벨이 없음, 소리는 끄고 사용), NSD shared 이미지(COCO, 정서 라벨 공개 없음, 정지 이미지). 둘 다 C&K와 분포가 다르다는 한계 |

**재현과 확장(선택):** Emo-FilM(1 Hz 연속 평정, 시청각, 30명)에서 시간 창 단위로 같은 비교. Emo-FilM 영화는 LIRIS-ACCEDE 공개 주석이 있어 오염 점검이 별도로 필요하다.

## 7. Proposed Computational Framework

* **Pretrained model (공개 모델 우선):**
  * 주 모델: **Qwen3-VL-8B**(arXiv:2511.21631). Xing 2026이 같은 모델에서 정서 vector를 추출해 비교 기준이 있다.
  * 재현 모델(다른 계열): **InternVL3.5-8B**(arXiv:2508.18265).
  * 대안: Qwen2.5-VL-7B(arXiv:2502.13923, Du 2025가 쓴 Qwen2-VL의 후속), LLaVA-OneVision-7B(arXiv:2408.03326).
  * 라이선스: 코드 저장소는 Qwen3-VL, Qwen2.5-VL Apache-2.0, InternVL MIT(일부 구성 요소는 원 라이선스), LLaVA-NeXT Apache-2.0(체크포인트는 원 라이선스를 따른다는 고지)로 **LICENSE 파일을 직접 확인했다.** **가중치 라이선스는 huggingface.co 모델 카드에 있어 확인하지 못했다(미확인).** 연구 목적 사용 가능 여부를 pilot 전에 확인한다.
  * 시각 통제용: V-JEPA 2(arXiv:2506.09985, 코드 MIT, 가중치 라이선스 이견 있음: 저장소 MIT 대 MIRAGE 표 3의 CC-BY-NC 4.0) 또는 CLIP image encoder. 캡션 통제용: 문장 encoder 2종 이상.
* **Input representation:**
  * 클립마다 고정 개수 프레임(예: 16장, 짧은 클립은 반복, 긴 클립은 균등 추출) + 고정 프롬프트. 프롬프트는 "이 영상을 보는 사람이 느낄 정서를 34개 범주 각각 0~100으로 답하라" 형식이며 표현을 바꾼 3개 판을 둔다.
  * 같은 프레임 입력으로 비정서 질문(예: "34개 장면, 사물 속성이 있는 정도를 답하라")도 돌린다(같은 모델 안 내용 통제).
* **Output / target representation:**
  * 모델 쪽 특징 두 가지, 둘 다 34차원:
    * **내부 표상:** 프롬프트 마지막 입력 token(답 생성 직전)의 여러 층 hidden state를 34개 정서 방향에 투영한 값.
    * **출력:** 생성된 34개 숫자. 반복 표집(예: 5회)의 평균과, 숫자 token 확률로 계산한 기댓값 두 판.
  * 뇌 쪽 목표: Horikawa 2020은 비디오별 voxel 반응(블록 평균), Mind captioning은 지각 학습 run의 클립별 반응과 지각 테스트 72클립의 5회 평균, 회상 72클립 반응.
* **Training or adaptation strategy:**
  * VLM은 미세조정하지 않는다.
  * 정서 방향은 **우리 데이터와 독립인 자료**로만 구한다: 범주별 정서 이야기(정서 단어를 직접 쓰지 않게 생성)와 대조 이야기의 평균 차이(Representation Engineering 방식, arXiv:2310.01405). 방향이 비디오 입력에서도 같은 뜻인지는 C&K가 아닌 이미지(EmoSet 일부 범주)에서 held-out 대응으로 점검한다(Xing 2026 방식).
  * 뇌 encoding은 피험자별 voxel ridge(banded ridge, 특징 묶음마다 다른 규제). 층 선택은 중첩 교차검증 안에서 한다.
* **Relevant brain regions / networks:**
  * 전뇌(volume 또는 HCP360 parcel). 사전 지정 ROI 묶음: transmodal(TPJ, IPL, vmPFC, precuneus, 측두극), 고차 시각(LOC, MT/MST, FFA 주변), 피질하(편도체, 해마).
  * 고차 시각 ROI는 "정서가 아니라 시각 내용을 설명하는가"를 보는 대조 영역이다. Du 2025의 우세 영역에 고위 시각피질과 MST가 포함되었기 때문이다.
  * 피질하는 3T, 2 mm에서 신호가 약하므로 결과를 따로 보고한다(signal-feasibility).
* **Loss function or statistical objective:**
  * 교차검증 예측 상관(또는 R²)과 특징 묶음별 고유 설명량(중첩 모형의 차이).
  * 핵심 통계량: Δ = 고유 설명량(내부) - 고유 설명량(출력), 각각 같은 모델의 null 대비 초과분으로 계산.
  * 검정: 클립 묶음 단위 순열(같은 원본에서 나온 클립은 같은 묶음), 피험자별 검정 + Bayesian prevalence(doi:10.7554/eLife.62461, DB)로 11명 중 몇 명에서 나타나는지 추정. ROI와 층에 대해 FDR 보정.
* **Interpretability method:**
  * Representation reading(정서 방향 투영)과 그 방향이 출력에 실제로 쓰이는지 보는 **steering 점검**(방향을 더하면 해당 정서 평정이 오르는가, R1 모델 내부 개입).
  * 구조 비교: 내부, 출력, 뇌 RDM(자극 간 유사도 행렬) 사이의 RSA와 범주성 지표(Bhattacharyya 2025 방식으로 범주 안 다양성과 범주 간 거리).
  * 특징별 고유 설명량 지도.

## 8. Proposed Analyses

**0단계: 측정 준비와 점검 (뇌 분석 전)**
1. **정서 방향 타당성:** 독립 자료에서 구한 방향이 held-out 이미지에서 해당 범주를 구분하는가. 구분하지 못하는 범주는 표시하고 주 분석에서 뺀다.
2. **steering 점검(R1):** 각 방향을 hidden state에 더했을 때 출력 평정의 해당 범주가 오르는가. 읽히지만 출력에 쓰이지 않는 방향은 "출력과 연결되지 않은 내부 표상"으로 따로 표기한다.
3. **차원과 신뢰도 맞추기:** 두 특징 모두 34차원. 신뢰도는 프롬프트 판(3개) 사이, 프레임 표집 사이, 출력 반복 표집 사이의 split-half로 잰다. 출력은 표집 잡음 때문에 신뢰도가 낮을 수 있으므로 (a) 반복 평균, (b) token 확률 기댓값, (c) 신뢰도 보정(감쇠 보정) 결과를 함께 보고한다. 내부 표상도 프롬프트와 프레임 표집에 따른 변동을 같은 방식으로 잰다.
4. **사전학습 오염 점검**(아래 별도 절차).

**1단계: 핵심 비교 (R0)**
* 특징 묶음: [시각 전용 모델 feature] + [정서 배제 인간 캡션 embedding] + [같은 모델의 비정서 질문 hidden state와 출력] + [내부 34] + [출력 34].
* 핵심 지표: 앞의 세 묶음(시각 이중 통제와 같은 모델 내용 통제)을 넣은 뒤 내부 34와 출력 34 각각의 고유 설명량, 그리고 둘의 공유 설명량.
* **matched-complexity null(같은 모델 안):** (i) 같은 층의 무작위 방향 34개 투영, (ii) 비정서 개념 방향 34개(사물, 장면 범주) 투영, (iii) 비정서 질문의 출력 34개. 정서 특징의 고유 설명량은 이 null 분포를 넘는 부분만 인정한다.
* **C&K 평정 너머:** C&K 34/14 규범 평정을 공변량으로 더 넣었을 때 두 특징의 고유 설명량이 남는가. 출력이 C&K 평정을 외워서 낸 값이라면 이때 출력의 고유 설명량이 사라진다.
* Mind captioning 지각 테스트 72클립 x 5회로 noise ceiling을 구해 정규화한다. Horikawa 2020은 반복이 없으므로 피험자 간 예측 상한으로 대신한다.

**2단계: 구조와 일반화**
* RSA와 범주성: 내부, 출력, 뇌 RDM의 범주성 지표를 같은 방법으로 비교한다.
* 코호트 간 재현: Horikawa 2020에서 얻은 결과 방향이 Mind captioning에서 다시 나오는가(같은 클립, 다른 사람).
* **회상 일반화:** 지각 데이터로 학습한 encoding 가중치로 회상 72클립의 뇌 반응을 예측할 때, 내부와 출력 중 어느 쪽이 더 잘 버티는가. cue 캡션의 embedding을 별도 회귀자로 넣는다(cue 읽기 반응이 회상 초반에 섞일 수 있음, reviewer_notes 4.4).

**ablation:** 층별(초기, 중간, 후기), 프레임 수(1장 대 16장), 프롬프트 판별, 모델별(Qwen3-VL 대 InternVL3.5), 출력 판(표집 평균 대 token 확률 기댓값).

**사전학습 오염 점검 절차** (C&K 클립과 범주 라벨이 공개 웹 interactive map에 있어 생기는 위험. 평가자 지적과 RQ-19 조정 근거)
1. **기억 탐침:** 클립만 주고 "이 영상은 어떤 데이터셋에서 왔나", "이 영상의 공식 정서 범주는 무엇인가"를 묻는다. 데이터셋 이름이나 C&K 범주 이름을 우연 이상으로 맞히면 기억 신호로 본다.
2. **변형 안정성:** 좌우 반전, 가장자리 자르기, 프레임 순서 섞기, 색 변환을 가한 클립에서 출력과 내부 표상이 얼마나 바뀌는지 본다. 기억에 기댄 답은 변형에도 비정상적으로 안정하고, C&K 평정과의 일치가 변형 전후로 같게 유지되는 경향이 있다.
3. **라벨 없는 자극과의 비교:** 같은 절차를 정서 규범 라벨이 공개되지 않은 자극(Spacetop alignvideo 무음판, NSD shared 이미지)에 적용해 "인간 평정과의 일치도"가 C&K에서만 유난히 높은지 본다(Spacetop은 참가자 본인 평정, NSD는 nsdmeadows 100장이 비교 대상이다).
4. **언어 쪽 membership 점검:** 범주명과 클립 서술 조합 텍스트에 대해 Min-K% Prob(arXiv:2310.16789)로 사전학습 포함 신호를 본다. 이것은 텍스트만 다루며 영상 자체의 포함 여부는 알려 주지 않는다.
5. **판정 규칙:** 1~3 중 둘 이상에서 오염 신호가 나오면 출력 쪽 결과에 "오염 가능"을 표시하고, C&K 평정 너머 분석(1단계)과 라벨 없는 자극의 결과를 우선 해석한다. 오염 점검으로 오염이 없다고 증명할 수는 없다(한계).

**반증 조건 (Falsifiability)**
* **H-pre(내부가 뇌와 더 닮았다)가 지지되지 않는 경우:** 신뢰도를 맞춘 뒤 내부 34의 고유 설명량이 같은 모델 null(무작위 방향, 비정서 방향) 분포의 95% 범위 안에 있거나, 출력보다 작거나 같다. 또는 두 모델 중 한 모델에서만 나타난다.
* **H-verb(출력이 더 닮았다)가 지지되지 않는 경우:** 출력 34의 고유 설명량이 비정서 질문 출력 null을 넘지 못하거나, C&K 평정을 공변량으로 넣으면 사라지거나, 오염 점검에서 오염 신호가 있는 클립을 빼면 사라진다.
* **"측정 방식이 뇌 설명에 차이를 만든다"는 주장 자체가 지지되지 않는 경우:** Δ의 신뢰구간이 0을 포함하고 두 코호트 모두에서 같다. 이 경우 Axis U의 "AI 추정"을 두 하위 출처로 나눌 필요가 없다는 결론이 된다.
* **정서 신호 자체가 없는 경우:** 시각 이중 통제와 같은 모델 내용 통제 뒤 두 특징 모두 null과 구분되지 않는다. 이 경우 Du 2025류 결과의 정서 해석이 약해진다.

## 9. Competing Explanations

| 대안 해석 | 가르는 분석 |
|---|---|
| 내부 표상이 이기는 것은 정서 때문이 아니라 hidden state에 시각, 장면 정보가 많기 때문이다(정서 방향이 일반 시각-의미 기하에 실려 있음, Xing 2026) | 같은 층의 무작위 방향과 비정서 개념 방향 34개를 null로 둔다. 시각 전용 모델 feature와 인간 캡션 embedding을 먼저 넣는다. 고차 시각 ROI와 transmodal ROI의 결과를 나눠 본다 |
| 출력이 이기는 것은 모델이 C&K 공개 지도의 평정을 기억하기 때문이다 | 오염 점검 절차 1~5. C&K 평정을 공변량으로 넣은 고유 설명량. 라벨 없는 자극에서의 같은 비교 |
| 출력이 지는 것은 표집 잡음으로 신뢰도가 낮기 때문이다 | 반복 표집 평균, token 확률 기댓값, 감쇠 보정 결과를 함께 보고 |
| 차이는 프롬프트 표현 때문이다 | 프롬프트 3개 판의 결과 범위를 보고. 방향이 판에 따라 뒤집히면 결론을 내지 않는다 |
| 독립 자료(텍스트 이야기)로 구한 정서 방향이 비디오 입력에서 같은 뜻이 아니다 | 0단계 방향 타당성 점검(held-out 이미지 대응), steering 점검. 실패한 범주는 제외 |
| 차이는 특정 모델의 성질이다 | 다른 계열 모델(InternVL3.5)에서 재현 |
| 차이는 C&K 영상 분포(범주가 잘 유발되도록 모은 군집 표본)의 특성이다 | 회상 일반화와 라벨 없는 자극(Spacetop)에서 방향이 유지되는가 |
| 내부 표상이 "보고 이전의 1차 정서"에 해당한다 | 이 해석은 검정하지 않는다. 결과는 측정 방식의 차이로만 쓰고 HOT 연결은 가설로만 둔다 |

## 10. Potential Findings

* **내부 > 출력 (null과 시각 통제를 넘어서):** 뇌의 정서 관련 분산은 모델의 보고 이전 형태 신호와 더 맞는다. AI 라벨을 신경 분석에 쓸 때 출력만 쓰면 정보를 잃는다. 출력의 범주화(Bhattacharyya 2025)가 뇌와 어긋나는 쪽이라는 해석과 맞는다.
* **출력 > 내부 (오염 점검과 C&K 평정 통제를 넘어서):** 뇌의 정서 관련 분산은 언어로 범주화된 판단 구조와 더 맞는다. 규범 평정이 잘 맞는 뇌 분산이 "평균 관찰자의 언어화된 판단"과 같은 성격이라는 해석을 지지한다. 단 오염 신호가 있으면 이 결과는 해석하지 않는다.
* **차이 없음:** 측정 방식은 결론을 바꾸지 않는다. Axis U에서 AI 추정 라벨을 나눌 필요가 없다는 실용적 결론.
* **둘 다 null과 구분되지 않음:** 시각 내용과 장면 의미를 넘는 정서 정보가 이 모델들의 어느 측정에도 없다. Du 2025류 결과의 정서 해석을 약화시킨다(RQ-08의 캡션 잔차 결과와 함께 읽는다).
* **영역별로 갈림:** 예컨대 transmodal 영역은 내부, 고차 시각은 출력과 맞는다면, 두 측정이 서로 다른 정보(보고 이전 연속 신호 대 범주화된 판단)를 싣는다는 지도가 된다.

## 11. Scientific Contribution

* **측정 방법(Axis U, Q):** AI 추정 정서 라벨을 신경 분석에 쓸 때 "어떻게 읽었는가"가 결과를 바꾸는지 처음으로 직접 판정한다. 결과에 따라 label-provenance 태그의 "AI 추정"을 [AI 추정, 출력]과 [AI 추정, 내부 표상]으로 나누는 근거가 된다(frontier-ai Round 2 제안).
* **AI 해석(Axis R, Machine Affect Representations Sub-axis):** 모델 내부 정서 표상을 사람 뇌라는 외부 기준으로 평가한다. 지금까지 모델 정서 vector의 타당성은 합성 자극과 모델 행동으로만 검증되었다(Sofroniew 2026, Xing 2026).
* **정서 이론(가설로만):**
  * 범주 대 연속 논쟁: 뇌의 정서 기하가 범주화된 출력과 더 맞는지, 연속적인 내부 신호와 더 맞는지는 Horikawa 2020의 "범주적" 결론과 Westlin 2025 재분석(arXiv:2507.00320)의 엇갈림을 읽는 또 하나의 관점이 된다.
  * HOT: 1차 상태와 보고의 구분과 모양이 닮았다는 점만 기록한다. 모델의 두 측정이 사람의 두 수준과 같다는 주장은 하지 않는다.
  * 모델 내부 표상을 주관 경험으로 해석하지 않는다(Axis R Sub-axis 정의의 단서).

## 12. Limitations & Risks

* **데이터:** fMRI 참가자 본인 정서 보고가 없다. 라벨은 별도 평정자 규범이다. Horikawa 2020은 5명, 반복 없음, 블록 평균. Mind captioning은 6명이고 지각 학습 순서가 6명 모두 같다(코호트 안 피험자 쌍 비교에 순서 효과가 섞일 수 있음). 클립 ID 대응표가 필요하다. 영상이 무음이라 소리 관련 정서 정보는 없다.
* **모델:** 정서 방향은 연구자가 정한 추출 절차에 의존한다. 범주 34개 중 일부는 방향이 잘 서지 않을 수 있다. 내용 필터로 일부 클립(성적, 혈액 장면)에서 출력이 거부되거나 왜곡될 수 있다(Santavirta 2025 Limitations). 가중치 라이선스 미확인.
* **오염:** 오염 점검은 오염이 없음을 증명하지 못한다. 시각 입력의 사전학습 포함 여부는 알 수 없다.
* **통계:** 11명은 집단 일반화에 작다. 피험자별 검정과 prevalence 추정으로 보완하지만 효과 크기 추정 중심이다. 특징 묶음 사이 공선성이 높아 고유 설명량 추정이 불안정할 수 있다.
* **해석:** "내부 > 출력"은 모델에 대한 사실과 뇌에 대한 사실이 섞인 결과다. 뇌가 무엇을 "표상한다"는 결론이 아니라 "어느 측정과 더 맞는다"는 결론만 낸다(decodability, representation, causality 구분).

## 13. Pilot Experiment

가장 작은 비용으로 핵심 전제(두 측정이 서로 다르고, 그 차이가 null을 넘어 뇌와 관련되는가)를 먼저 본다.

1. **모델 하나:** Qwen3-VL-8B(가중치 라이선스 확인 후). 대안 Qwen2.5-VL-7B.
2. **오염 탐침 먼저(약 1일):** 무작위 100클립에 오염 점검 1, 2를 적용. 강한 기억 신호가 나오면 모델을 바꾸거나 설계를 "C&K 평정 너머" 분석 중심으로 바꾼다.
3. **정서 방향:** 34범주 텍스트 이야기로 추출, held-out 이미지 점검은 EmoSet과 겹치는 범주만.
4. **특징 추출:** 2,180클립 x 프롬프트 1판 x 출력 표집 3회, 중간층 3개. 비정서 질문 1판.
5. **뇌 분석:** Mind captioning 지각 테스트 72클립(5회 평균, noise ceiling 있음)과 지각 학습 2,180클립으로 피험자별 encoding. HCP360 parcel 수준에서 내부 34, 출력 34, 무작위 방향 null의 고유 설명량.
6. **계속, 수정, 중단 기준:**
   * 계속: 두 특징 중 하나 이상이 같은 모델 null을 넘는 고유 설명량을 6명 중 4명 이상에서 보이고, 두 특징의 상관이 0.9 미만(두 측정이 실제로 다름).
   * 수정: 두 특징의 상관이 0.9 이상이면 출력 판(token 확률)과 층을 바꿔 다시 본다.
   * 중단: 두 특징 모두 시각 이중 통제 뒤 null과 구분되지 않으면 본 연구를 RQ-08(캡션 잔차)의 하위 분석으로 축소한다.

## 14. Feasibility & Priority

* **점수(조정된 최종, 9개 기준):** Novelty 3.0, Neuroscientific Importance 3.0, AI / Modeling Contribution 4.5, Dataset Feasibility 4.5, Methodological Rigor 3.5, Falsifiability 4.0, Interpretability 3.0, Generalizability 4.0, Feasibility 4.0. **합계 33.5**(Coordinator 34, 평가자 33), 과학 기준 5개 합 16.5 (`outputs/evaluation/scores_final.csv`).
* **순위:** 전체 3위(동점), Substantive Shortlist 3번, **High-priority Candidates 2위**, **Recommended Pilot P3**(`selection.md`). 감사 판정 not found.
* **Novelty, Impact, Feasibility 요약:** Novelty 중간(출력 쪽 선행이 있어 새로움은 "같은 모델 쌍 비교"로 좁음). Impact 중간(AI 라벨을 쓰는 모든 정서 신경 연구의 측정 방식에 영향, 인간 정서에 대한 새 지식은 간접적). Feasibility 높음(새 fMRI 불필요, 공개 VLM 추론과 기존 encoding 파이프라인).
* **계산 자원(미확인, 가정: GPU 1~4장, A100 80GB급):**
  * 8B VLM 추론, 클립당 프레임 16장 기준 한 번의 forward pass와 34개 숫자 생성에 수 초로 추정.
  * 전체 설계(2,180클립 x 프롬프트 3판 x 출력 표집 5회 + 비정서 질문 + 오염 변형 4종): 모델 하나에 약 70~100 GPU 시간, 모델 두 개면 약 150~200 GPU 시간(추정, 실측 아님). GPU 4장이면 2~3일.
  * Pilot(프롬프트 1판, 표집 3회, 모델 하나): 약 15~25 GPU 시간.
  * hidden state 저장: 층 3~6개 x 2,180클립 x 반복 수 규모로 수 GB 이내. encoding은 CPU나 GPU 1장으로 충분.
* **선행 관문:** RQ-17(어느 정서 항목에서 AI가 사람 평정을 대신할 수 있는가, Emo-FilM)을 참고 관문으로 둔다. RQ-15 결과가 "출력 대신 내부"를 지지하면 RQ-17의 alt-test도 두 측정으로 나눠 해야 한다.
* **overlap:**
  * **EmoBrain(구 EmoViS 범위 포함): 부분 겹침 가능.** Horikawa 34차원 정서 profile과 시각-의미 기원 통제를 다루는 부분이 겹친다. 핵심 비교(같은 모델의 내부 표상 대 출력)는 겹치지 않는다.
  * **Emo-FilM 연구: 없음.** Emo-FilM은 선택적 확장으로만 쓴다.

---

## 반영하지 않은 지적

| 지적 | 출처 | 반영하지 않은 이유 |
|---|---|---|
| 의미를 고정하고 정서만 바꾼 영상 편집과, 정서를 고정하고 의미만 바꾼 편집에 두 측정이 어떻게 반응하는지 보는 사전 검사 | generative-counterfactual Round 3 FA-P6 검토 수정안 3(b) | Pilot과 본 연구 1단계에는 넣지 않고 후속 단계로 미룬다. 비디오 정서 편집은 의미를 함께 바꾸는 문제가 이미 보고되어(NeuroVolve arXiv:2512.00557, EmoEdit arXiv:2405.12661, 모두 DB 등재) 편집 자체의 검증이 별도 연구가 된다. 같은 목적(정서 방향이 의미 대리물인지)은 같은 모델 안 비정서 방향 null과 시각 이중 통제로 먼저 다룬다 |
| 비디오 입력에서 정서 방향의 의미를 소규모 인간 평정(R2)으로 점검 | vision-decoding Round 3 FA-P6 검토 수정안 2 | Pilot에서는 held-out 이미지 대응과 steering 점검으로 대신한다. 새 인간 평정은 IRB와 비용이 필요해 pilot 결과가 "계속"일 때 2단계에서 수집한다 |
| 뇌에서 모델 공간으로 가는 decoding 방향 분석과 GW 정렬 | vision-decoding 수정안 (d), generative-counterfactual 수정안의 뇌 비교 지표 | 핵심 질문이 "어느 측정이 뇌 분산을 고유하게 설명하는가"라서 encoding과 고유 설명량을 주 분석으로 둔다. decoding과 GW 정렬은 2단계 구조 분석의 선택 항목으로만 남긴다 |

## Safeguards 점검

| 항목 (CLAUDE.md 6절, 필수 태그) | 이 카드의 처리 |
|---|---|
| 참가자가 경험한 정서 vs 자극에 묘사된 정서 | 참가자 본인 보고가 없어 경험에 대한 결론은 내지 않는다. 모델 두 측정은 "보는 사람이 느낄 정서"를 묻지만 관찰자 관점(perceived) 추정으로 표기 |
| 인간 정서 주석 vs 모델 생성 주석 | 모델 두 측정은 모두 AI 추정. C&K 평정은 인간 규범. 같은 표에 섞지 않고 변수명으로 구분 |
| 참가자 본인 보고 vs 별도 평정자 규범 | C&K는 별도 평정자 규범(집계값). 본인 보고 없음 |
| 정서 표상 vs 시각/의미 내용 표상 | 시각 전용 모델 feature, 인간 정서 배제 캡션, 같은 모델 비정서 질문의 세 겹 통제와 비정서 방향 null |
| encoding 정확도 vs 설명적 적절성 | 결과는 "어느 측정과 더 맞는가"로만 쓴다. 높은 설명량을 정서 표상의 증거로 쓰지 않는다 |
| decodability vs representation vs causality | 뇌 쪽은 R0 상관. steering은 모델 내부의 인과(R1)이며 뇌의 인과가 아님 |
| in-silico 예측 vs 관찰 fMRI | 모델 특징은 자극 기술자이고 뇌 반응은 실측. in-silico 뇌는 쓰지 않음 |
| 공유 표상 vs 데이터셋 특이 교란 | 두 코호트 재현, 두 모델 계열 재현, 라벨 없는 자극(Spacetop, NSD)에서의 비교 |
| 탐색적 결과 vs 확증적 증거 | Pilot은 탐색. 본 분석의 가설(H-pre, H-verb), null, 반증 조건, 층 선택 규칙을 pilot 뒤 사전 등록 |
| HRF 지연과 시간 자기상관 | Horikawa는 블록 평균 1 sample. Mind captioning은 블록 단위 추정. 회상은 cue 읽기 반응의 HRF 혼입을 cue 회귀자로 통제 |
| stimulus, movie, subject 수준 leakage | 같은 원본에서 나온 클립은 같은 교차검증 묶음. 정서 방향은 C&K와 독립인 자료로 추출. 층 선택은 중첩 교차검증 안에서 |
| 반복 자극 교란 | Mind captioning 지각 테스트의 5회 반복은 평균해 쓰고, 학습 세트(1회)와 분리 |
| 평정자 간 일치와 라벨 잡음 | C&K 평정자 개인 자료가 없어 라벨 신뢰도를 직접 잴 수 없음. 라벨은 공변량과 해석에만 사용 |
| 시각-의미-정서 feature 공선성 | banded ridge와 고유 설명량, 공유 설명량을 함께 보고 |
| 시간, 공간 해상도 한계 | 피질하 결과는 따로 보고. 클립 내부 시간 변화는 다루지 않음 |
| ROI 선택과 순환 추론 | ROI는 HCP360 등 독립 atlas로 사전 지정 |
| 다중 비교 | ROI와 층에 대해 FDR, 피험자별 결과와 prevalence 함께 보고 |
| 데이터 접근, checkpoint, 라이선스 | 데이터 모두 보유. VLM 코드 라이선스 확인, 가중치 라이선스 미확인(pilot 전 확인) |
| 사전학습 데이터 오염 | 오염 점검 절차 1~5, C&K 평정 너머 분석, 라벨 없는 자극 비교 |
| 데이터셋 간 주석 비호환 | 주 분석은 같은 자극, 같은 라벨의 두 코호트. Spacetop, NSD는 오염 대조로만 쓰고 라벨을 합치지 않음 |
| **label-provenance** | C&K: [felt 문항, 별도 평정자 규범]. 모델 출력: [AI 추정, 출력(verbalized), perceived]. 모델 내부: [AI 추정, 내부 표상(probe), perceived]. steering을 거친 방향: [AI 추정, 내부 표상, 개입 검증] |
| **evidence-level** | 뇌 비교 R0. 방향 추출과 steering 점검은 R1(모델 내부) |
| **insilico-vs-observed** | 관찰(모델 특징은 자극 기술자) |
| **G1** | 원본 자극 필요(보유) |
| **signal-feasibility** | 3T, 2 mm. 피질하(편도체, 해마)는 tSNR이 낮을 수 있어 결과를 분리 보고. 사전 tSNR 지도 확인 필요(미수행) |
| **minimum-validation** (adversarial-reviewer 7항목) | 경쟁 모델과 matched-complexity null: 충족(같은 모델 무작위, 비정서 방향, 비정서 질문 출력). 상한 병기: 충족(Mind captioning noise ceiling). 신뢰도 민감도: 충족(출력 표집, 프롬프트 판, 감쇠 보정). leakage 경로별 대응: 충족(위 표). 일반화 수준 명시: 충족(같은 자극 다른 사람, 다른 모델 계열, 회상). 라벨 출처 표시: 충족. 반증 해석 사전 기술: 충족(8절 반증 조건) |
