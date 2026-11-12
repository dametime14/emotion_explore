# Round 4 (Unexpected Connections): llm-semantics

* 에이전트: llm-semantics (주 담당 Axis C, 공동 담당 Axis U. 외부 분야: Social and Collective Behavior, Human-AI Representation Differences)
* 기준일: 2026-11-12
* 절차: `reference/protocols.md` P4
* 읽은 파일: `outputs/combinations/discussed_pairs.md`(미논의 2개 조합 23개), `outputs/axis_encyclopedia.md` 3절(갱신 유형표)
* 출발점으로 쓴 미논의 쌍: **J+U, R+W, I+W, D+S**. 검토 후 기각한 쌍: M+W, K+L, T+V, Q+V, J+W, P+W(독립 제안으로는 기각하고 LS-R4-2의 통제로 흡수), B+K, T+W (5절)
* 새로 확인해 `literature.jsonl`에 넣은 문헌: arXiv:2303.17548, arXiv:2310.06452, arXiv:2604.27345 (arxiv.org/abs), doi:10.1073/pnas.2313790120, doi:10.1523/JNEUROSCI.1431-18.2018, doi:10.1038/nn.4450, doi:10.1038/s41467-023-41648-1 (Crossref, PubMed 전문). 현재 57편.
* 데이터셋 5개: Horikawa 2020, Emo-FilM, Spacetop, NSD, Mind captioning(ds005191)
* 표기: label-provenance(대상 portrayed / perceived affective quality / felt, 주체 본인 / peer 합의 / 별도 평정자 규범 / AI 추정), evidence-level(R0 상관, R1 모델 내 개입, R2 새 행동 평정, R3 새 fMRI 자극 조작, R4 뇌 개입), insilico-vs-observed, G1

## 요약표

| ID | 출발 미논의 쌍 | 조합한 Axis (유형) | 외부 개념/방법 | 한 줄 질문 | 주 데이터 | evidence-level |
|---|---|---|---|---|---|---|
| LS-R4-1 | **J+U** | J(Model & Method), U(Inference), O(Neural), C(Construct) | 선호 최적화와 응답 다양성 붕괴(ML), 여론 대표성 측정(computational social science) | 학습 목표(사전학습 vs 선호 최적화)가 기계 평정자의 "관점"(개인 보고 vs 규범 평균)을 정하는가 | Spacetop narratives, alignvideo, Emo-FilM, Mind captioning | R0 + R1 |
| LS-R4-2 | **R+W** | R(Structure), W(Construct), C(Construct), I(Model & Method), U(Inference) | 기계적 해석(모델 내부 표상 투영) | MLLM이 영상에서 텍스트 cue로 넘어갈 때 보존하는 정서 표상이 사람 뇌가 회상에서 재현하는 정서를 예측하는가 | Mind captioning, Horikawa 2020 | R0 + R1 |
| LS-R4-3 | **I+W** | I(Model & Method), W(Construct), C(Construct), F(Neural) | 문화 진화의 전달 사슬(Social and Collective Behavior) | 반복 전달에서 살아남는 정서 내용(집단 기억 편향)이 개인 회상의 정서 재현(개인 기억 편향)을 예측하는가 | Mind captioning | R0 + R1, 인간 사슬 시 R2 |
| LS-R4-4 | **D+S** | D(Construct), S(Inference), C(Construct), I(Model & Method), E(Neural) | 사회적 예측의 mental model(사회심리), LLM 다음 상태 분포 | 언어에 담긴 정서 전이 지식이 보류된 영화의 신경 정서 상태 전이를 예측하는가 | Emo-FilM, Spacetop narratives | R0 |

---

## LS-R4-1. 학습 목표가 기계 평정자의 관점을 정하는가 (J+U)

* **조합한 Axis:** J Learning Objectives(Model & Method), U Label Provenance & Perspective(Inference & Measurement), O Individual & Population Variation(Neural), C Context, Meaning & Narrative(Construct). 서로 다른 유형 4개.
* **외부 개념:** 선호 최적화(RLHF, DPO)가 출력 분포를 최빈 응답으로 붕괴시킨다는 ML 결과(arXiv:2310.06452), 여론조사로 LM 의견의 집단 대표성을 재는 computational social science 방법(arXiv:2303.17548).
* **미논의 쌍을 포함하는 방식:** J(학습 목표)를 독립 변수로, U(라벨 출처와 관점)를 종속 변수로 둔다. 지금까지 AI 추정 라벨은 "AI 추정"이라는 한 범주로만 다뤘고(Axis U), 그 라벨을 만든 학습 목표가 라벨의 관점(1인칭 분산 vs 3인칭 평균)을 바꾸는지는 묻지 않았다.
* **연결의 근거(왜 예상 밖인가):** 여론 연구에서 base LM은 일부 집단을 더 잘 대표하고, RLHF 모델은 한 선택지에 0.99 이상을 주는 낮은 엔트로피 분포로 붕괴했다(arXiv:2303.17548, 4절과 부록 Figure 9 서술). RLHF는 SFT보다 출력 다양성을 크게 줄인다(arXiv:2310.06452, 초록). 정서 쪽에서는 GPT-4가 경험자 본인보다 3인칭 관찰자 평균에 가깝고(arXiv:2408.13718, Study 2), zero-shot LLM은 인간 정서 판단의 불일치 분포를 포착하지 못한다(arXiv:2604.27345, 초록). Xu 2025는 RLHF 등 학습 기법별 효과를 독점 모델로는 분리할 수 없어 공개 소형 모델로 비교하라고 했다(doi:10.1038/s41562-025-02203-8, Discussion 여섯째 단락). 두 분야를 이으면 "LLM 정서 주석이 3인칭 평균이 되는 것은 언어 자체 때문인가, 선호 최적화 때문인가"라는 질문이 생긴다.
* **연구 질문:** 같은 공개 모델 계열의 사전학습(base), 지도 미세조정(SFT), 선호 최적화 판본이 내놓는 정서 평정 분포는 각각 fMRI 참가자 본인 보고의 분산, peer 합의, 별도 평정자 규범 중 어느 것에 가장 가까우며, 그 차이가 개인 뇌 반응의 개인 특이 성분을 설명하는 기준점으로서의 가치를 바꾸는가?
* **설계:**
  1. **텍스트 자극에서 시작:** Spacetop narratives(텍스트 4편, 오디오 4편, 참가자의 good-bad 감정 평정 [felt, 본인])는 원문이 텍스트라 영상 기술 단계 없이 base 모델과 instruct 모델을 같은 입력으로 비교할 수 있다. 각 판본에서 표본추출로 응답 분포를 얻는다(base는 완성형 prompt, instruct는 지시형 prompt, 둘 다 여러 표현).
  2. **영상 자극:** Mind captioning과 Horikawa는 인간 중립 캡션(L1)을 입력으로 텍스트 모델 판본을 비교하고 C&K 34/14 [felt, 별도 평정자 규범]과 대조한다. Spacetop alignvideo는 MLLM이 필요해 base 판본 비교가 제한된다(오디오와 영상 입력 가능한 base 모델이 드물다).
  3. **관점 지표:** (a) 판본별 분포의 엔트로피와 인간 본인 보고 분산의 비, (b) 판본별 최빈값과 규범 평균의 거리, (c) 개별 참가자 보고의 판본별 우도.
  4. **뇌 연결(O):** GI-P5 multiverse의 기준선 칸에 "base 분포 기준 편차"와 "선호 최적화 최빈값 기준 편차"를 각각 넣어, 어느 기준의 보고 편차가 참가자의 신경 개인 특이 잔차를 더 잘 예측하는지 본다.
* **측정 가능한 예측:**
  * P1: 선호 최적화 판본은 base보다 엔트로피가 낮고 규범 평균(C&K, Emo-FilM consensus)에 더 가깝다.
  * P2: base 판본의 표본 분포 폭은 Spacetop 본인 보고의 개인 간 분산에 더 가깝다.
  * P3: 개인 뇌 잔차는 "선호 최적화 최빈값에서의 편차"보다 "base 분포 아래에서의 본인 보고 우도(놀람)"와 더 강하게 연관된다.
* **반증 조건:** 판본 간 엔트로피와 규범 거리 차이가 프롬프트 변형 간 차이보다 작으면 P1, P2를 기각한다. 이 경우 3인칭 평균 성향은 선호 최적화가 아니라 사전학습 텍스트 자체에서 온다는 해석이 남으며(TakGratch2024와 일치), 이것도 Axis U에 정보가 된다. P3는 두 기준선의 예측력 차이가 영상 단위 순열 null과 구분되지 않으면 기각한다.
* **가능한 데이터셋:** Spacetop narratives(주), Spacetop alignvideo(MLLM 판본 비교 가능 범위에서), Mind captioning, Horikawa 2020, Emo-FilM(평정자별 원자료로 인간 분산 기준 계산)
* **근거 논문 ID:** arXiv:2303.17548, arXiv:2310.06452, arXiv:2604.27345, arXiv:2408.13718, arXiv:2402.01908, doi:10.1038/s41562-025-02203-8, arXiv:2508.05880(LLM 정서 개념이 인간보다 더 범주적, frontier-ai 기록)
* **선행 수행 검색:** WebSearch "base versus instruction-tuned RLHF language model emotion annotation distribution diversity human annotator disagreement self-report vs observer"(2026-11-12). 결과: 정서 분포와 인간 불일치 비교는 arXiv:2604.27345(zero-shot 지시 모델만, base 판본 비교 없음, 본인 보고 vs 관찰자 비교 없음), 지시 튜닝 데이터의 불일치 원천 연구(Dsouza & Kovatchev 2025, CoMeDi, aclanthology 접근 불가로 search_index). 정서 평정에서 base와 선호 최적화 판본을 본인 보고 대 규범으로 비교하고 뇌 잔차와 연결한 연구는 검색 범위 내 미발견. **판정: partially** (분포 격차 자체는 선행).
* **label-provenance:** 표적 felt / 본인(Spacetop), felt / 별도 평정자 규범(C&K, Emo-FilM). AI 라벨은 AI 추정에 학습 목표 태그(base, SFT, 선호 최적화)를 붙인다. 이 태그를 Axis U의 하위 기록 항목으로 제안한다.
* **evidence-level:** R0(뇌, 행동 비교) + R1(학습 판본 비교는 모델 쪽 조작) / **insilico-vs-observed:** 혼합 / **G1:** narratives 텍스트는 필요(보유), 캡션 경로는 Mind captioning 캡션 필요(보유)
* **위험:** 판본 간 비교는 prompt 형식 차이(완성형 vs 지시형)와 섞인다. 여러 표현과 같은 완성형 형식을 양쪽에 함께 쓴다. 공개 모델 계열 중 base, SFT, 선호 최적화 판본을 모두 공개한 계열이 있어야 한다(라이선스와 checkpoint는 Stage 4 전에 확인). Spacetop narratives의 원 출처가 공개 이야기라면 사전학습 오염이 있다.
* **overlap:** 없음

---

## LS-R4-2. 기계 재현과 뇌 재현: 언어 병목을 통과하는 정서 (R+W)

* **조합한 Axis:** R Explainability & Mechanistic AI(Structure), W Internally Generated Experience(Construct), C Context, Meaning & Narrative(Construct), I AI Model Families(Model & Method), U Label Provenance & Perspective(Inference). 서로 다른 유형 4개.
* **외부 개념:** 모델 내부 표상 투영(정서 방향, arXiv:2604.07729, arXiv:2609.34742 방식)으로 측정하는 "기계 재현"
* **미논의 쌍을 포함하는 방식:** R(모델 내부 표상의 해석)을 W(회상, 심상)에 직접 붙인다. 지금까지 R은 지각 조건의 모델 표상과 뇌 비교에만 쓰였고, 회상 조건에서 "무엇이 남는가"를 모델 내부 표상으로 예측한 제안은 없다.
* **연결의 근거:** Mind captioning에서 회상 준비 구간 cue는 같은 클립의 정서 배제 캡션 중 하나(영어와 일본어 번역)였다(doi:10.1126/sciadv.adw1464, Materials and Methods 'Imagery experiment'). 같은 연구에서 의미 feature가 시각 feature보다 회상으로 더 잘 일반화되었다(같은 논문 Discussion 둘째 단락). 영화 회상 중 장면 특이 재활성은 지각 패턴에서 체계적으로 변환되며 그 변환 크기가 기억성을 예측했다(doi:10.1038/nn.4450, Discussion 첫 단락). 기억은 시간에 따라 의미 요지로 변환되고 그 변환은 부정 정서 자료에서 더 강했다(doi:10.1038/s41467-023-41648-1, Discussion 첫 단락). 여기서 MLLM은 하나의 "순수 언어 병목" 기억 모형이 된다. 같은 MLLM에 (a) 비디오, (b) cue 캡션 텍스트만 넣으면, (b)에서 다시 나타나는 정서 표상은 언어로 운반 가능한 정서(내 L2)의 상한이다.
* **연구 질문:** Mind captioning 72개 클립에서, MLLM이 비디오를 볼 때의 내부 정서 표상이 cue 캡션 텍스트만 받았을 때 얼마나 재현되는가(기계 재현 지수)가, 참가자 뇌가 같은 클립을 회상할 때 정서 부분공간을 재현하는 정도를 클립별로 예측하는가?
* **설계:**
  1. 기계 재현 지수: 공개 비디오 MLLM의 중간층 hidden state를 우리 데이터와 독립인 자료로 추출한 정서 방향에 투영한다(FA-P6 수정안). 클립별로 (a) 비디오 입력 투영과 (b) cue 텍스트 입력 투영의 유사도를 계산한다. 대조로 의미 방향(정서와 무관한 장면 의미)의 재현 지수도 같은 방식으로 만든다.
  2. 뇌 재현 지수: 지각 데이터(Mind captioning 5회 반복, Horikawa 2020)로 시각, 의미, 정서 band encoding model을 학습하고, 회상 반응에서 정서 band의 고유 예측력 또는 정서 부분공간 encoding-retrieval similarity를 클립별로 계산한다(ET-P6 검토 수정안의 순방향 분석).
  3. 통제: cue 함축 정서(LLM reader 추정과 소규모 인간 reader 평정), 의미 재현 지수, 준비 구간 반응(cue 읽기만 한 구간, P+W 쌍의 "입력 제거" 통제를 여기서 쓴다), vividness와 정확도 평정.
* **측정 가능한 예측:**
  * P1: 정서 의미가 언어로 운반된다면, 의미 재현과 cue 함축 정서를 통제한 뒤에도 기계 정서 재현 지수가 뇌 정서 재현을 클립 간에 양의 방향으로 예측한다.
  * P2: 그 예측은 DMN과 의미 영역에서 강하고 insula, 편도체에서 약하다.
  * P3: 뇌 정서 재현은 높은데 기계 재현은 낮은 클립(언어 병목을 통과하지 못한 정서)은 Asanuma 2025가 MLLM 실패로 보고한 신체 기반, 맥락 반전 유형에 몰린다(doi:10.1038/s41598-025-14961-6, Discussion 후반).
* **반증 조건:** 기계 재현 지수의 프롬프트, 모델 간 신뢰도가 낮으면(지수 자체가 불안정) 분석을 중단한다. 신뢰도가 충분한데도 통제 후 뇌 정서 재현과 무관하면, 회상의 정서 재현은 언어 병목으로 운반되는 정서 의미와 독립적이라는 결론이다(P1 기각). 이는 비언어적 정서 기억 성분의 간접 증거로 해석할 수 있으나 decoding 잡음 가능성을 함께 적는다.
* **가능한 데이터셋:** Mind captioning(주), Horikawa 2020(지각 encoding 보강)
* **근거 논문 ID:** doi:10.1126/sciadv.adw1464, doi:10.1038/nn.4450, doi:10.1038/s41467-023-41648-1, arXiv:2604.07729, arXiv:2609.34742, doi:10.1038/s41598-025-14961-6, doi:10.1093/cercor/bhv086(지각-심상 교차 일반화, 부분 선행)
* **선행 수행 검색:** WebSearch "multimodal language model representation of video versus text description compared to brain encoding-retrieval similarity during recall fMRI"(2026-11-12). 결과: 영화 시청 중 MLLM 정렬 연구(arXiv:2507.17958 등, search_index)만 있고 회상 fMRI와 비교한 연구 없음. 지각에서 심상으로의 정서 분류 일반화는 doi:10.1093/cercor/bhv086이 보고. **판정: no (검색 범위 내), 단 정서 재활성 자체는 partially**
* **label-provenance:** 뇌 쪽 정서 부분공간은 felt / 별도 평정자 규범(C&K)으로 정의. vividness는 참가자 본인(심상, 재시청 후 회고). 기계 재현은 AI 추정, 내부 표상
* **evidence-level:** R0(클립 간 상관) + R1(MLLM 입력 조작) / **insilico-vs-observed:** 혼합 / **G1:** 필요(보유)
* **위험:** 72클립이라 클립 간 상관의 검정력이 제한된다. 참가자 6명, 클립 72개의 계층 모형을 쓴다. MLLM에 일본어 cue를 줄지 영어 cue를 줄지에 따라 결과가 달라질 수 있다(참가자는 둘 다 봤다). 둘 다 계산해 차이를 보고한다.
* **overlap:** 없음

---

## LS-R4-3. 집단 전달 편향과 개인 회상의 정서 재현 (I+W)

* **조합한 Axis:** I AI Model Families(Model & Method), W Internally Generated Experience(Construct), C Context, Meaning & Narrative(Construct), F Brain Representation(Neural). 서로 다른 유형 3개 이상.
* **외부 분야:** Social and Collective Behavior(문화 진화의 전달 사슬, transmission chain)
* **미논의 쌍을 포함하는 방식:** I(LLM)를 문화 전달 사슬의 "전달자"로 쓰고, 그 전달에서 살아남는 정서 내용을 W(개인 회상)의 신경 재현과 비교한다. I와 W를 잇는 제안은 지금까지 없었다.
* **연결의 근거:** 문화 진화 연구는 사람이 부정, 사회, 위협 관련 내용을 더 잘 기억하고 전달한다고 보고했고, ChatGPT-3도 같은 전달 사슬에서 같은 편향을 보였으며 모호한 진술을 부정으로 해소했다(doi:10.1073/pnas.2313790120, Discussion 첫째, 셋째 단락). 저자들은 이 편향이 인간이 만든 학습 자료가 이미 문화 진화를 거친 산물이기 때문이라고 해석했다(같은 논문 Discussion 셋째 단락). 개인 기억 쪽에서는 부정 정서 기억이 감각 재현을 강화한다는 NEVER 모델(doi:10.3758/s13423-017-1313-9)과 부정 정서 기억이 더 빨리 의미 요지로 변환된다는 결과(doi:10.1038/s41467-023-41648-1)가 있다. 두 분야를 이으면 "집단 수준에서 살아남는 정서 내용과 개인 뇌에서 재현되는 정서 내용은 같은 편향을 공유하는가"라는 질문이 생긴다.
* **연구 질문:** Mind captioning 72개 클립의 기술문을 LLM 전달 사슬(그리고 소규모 인간 전달 사슬)에 통과시켰을 때 정서 내용이 보존되거나 명시화되는 정도(집단 전달 편향)가, 같은 클립을 회상하는 참가자 뇌에서 정서 성분이 시각 세부보다 상대적으로 더 재현되는 정도(개인 기억 편향)를 클립별로 예측하는가?
* **설계:**
  1. 출발 텍스트: 각 클립의 정서 배제 인간 캡션 여러 개를 합친 기술문(L1). 정서 단어가 없는 상태에서 출발하므로, 사슬에서 정서 어휘가 생기거나 강해지는 정도("정서 명시화")와 장면 세부가 사라지는 정도를 클립별로 잴 수 있다.
  2. 사슬: 공개 LLM 여러 개, 여러 prompt(요약, 다시 말하기)로 5단계 사슬. Acerbi & Stubbersfield는 변환 대부분이 첫 단계에서 일어났다고 보고했으므로 1단계와 5단계를 따로 기록한다(같은 논문 Discussion 여섯째 단락).
  3. 인간 사슬(R2): 72클립 중 일부에서 사람 전달 사슬을 받아 LLM 사슬과의 일치를 alt-test로 확인한다. LLM 사슬만으로 결론을 내지 않는다.
  4. 뇌: 회상 중 정서 band와 시각 band의 재현 비(ET-P6 수정안의 순방향 분석).
* **측정 가능한 예측:**
  * P1: 전달 사슬에서 정서 명시화가 큰 클립일수록 회상 중 정서 재현 대 시각 재현의 비가 크다.
  * P2: 이 관계는 부정 valence 클립(C&K 규범)에서 더 강하다(NEVER, Krenz 2023과 같은 방향).
  * P3: 위협, 사회 관련 클립에서 LLM 사슬과 인간 사슬의 정서 보존이 가장 잘 일치한다(Acerbi & Stubbersfield의 편향 범주).
* **반증 조건:** 사슬 정서 명시화 지수와 뇌 정서/시각 재현 비가 C&K 정서 강도와 valence를 통제한 뒤 무관하면 P1을 기각한다. 이 경우 집단 전달 편향과 개인 회상의 정서 재현은 공통 기제를 공유하지 않는다는 결과이며, "LLM 출력은 인간 문화의 편향을 반영한다"는 해석이 개인 기억까지 확장되지 않는다는 정보가 된다. LLM 사슬과 인간 사슬이 일치하지 않으면 LLM 사슬 결과는 보고하되 결론에서 뺀다.
* **가능한 데이터셋:** Mind captioning(주), Horikawa 2020(지각 encoding 보강)
* **근거 논문 ID:** doi:10.1073/pnas.2313790120, doi:10.3758/s13423-017-1313-9, doi:10.1038/s41467-023-41648-1, doi:10.1038/nn.4450, doi:10.1126/sciadv.adw1464, arXiv:2501.10970(alt-test)
* **선행 수행 검색:** WebSearch "transmission chain serial reproduction emotional content retention predicts neural reinstatement memory recall fMRI video clips"(2026-11-12). 결과: 전달 사슬과 fMRI 회상 재현을 결합한 연구 없음. 정서와 회상 세부의 관계(eNeuro 2026 원고, search_index), 기억의 의미 변환(doi:10.1038/s41467-023-41648-1)만 확인. **판정: no (검색 범위 내)**
* **label-provenance:** 사슬 텍스트의 정서 명시화는 perceived affective quality / AI 추정(LLM 사슬) 또는 별도 인간(인간 사슬, R2). 뇌 쪽 정서 band는 felt / 별도 평정자 규범(C&K)
* **evidence-level:** R0(클립 간 연관) + R1(LLM 사슬) + R2(인간 사슬) / **insilico-vs-observed:** 혼합 / **G1:** 캡션만 쓰면 불필요, 시각 band에는 필요(보유)
* **위험:** LS-R4-2와 같은 72클립, 6명 검정력 한계. 출발 텍스트가 정서 배제 캡션이므로 사슬에서 생기는 정서 어휘는 모델의 추론(L2)이자 편향이다. 이 둘을 구분하지 않고 "집단 기억"으로 부르지 않는다. 인간 사슬 수집에는 IRB가 필요하다.
* **overlap:** 없음
* **LS-R4-2와의 관계:** LS-R4-2는 한 단계의 언어 병목(비디오 → 텍스트)에서 모델 내부 표상이 보존하는 정서를, LS-R4-3은 여러 단계의 사회적 전달에서 텍스트 출력에 남는 정서를 잰다. 두 지수가 같은 클립 순위를 내면 하나로 합친다.

---

## LS-R4-4. 언어에 담긴 정서 전이 지식은 보류된 영화의 신경 상태 전이를 예측하는가 (D+S)

* **조합한 Axis:** D Temporal Dynamics(Construct), S Generalization & Robustness(Inference), C Context, Meaning & Narrative(Construct), I AI Model Families(Model & Method), E Neural Targets(Neural). 서로 다른 유형 4개.
* **외부 개념:** 사회적 예측의 mental model(사회심리, Thornton & Tamir), LLM의 다음 상태 확률 분포
* **미논의 쌍을 포함하는 방식:** D(정서 전이)를 S(교차 영역 일반화)의 문제로 바꾼다. 지금까지 정서 전이 제안(BI-P1, GI-P2, GI C2)은 Emo-FilM 평정에서 얻은 경험적 전이를 같은 데이터의 신경 전이와 비교했다. 여기서는 전이 사전확률을 **영화와 무관한 언어 지식**에서 가져와, 보류된 영화의 신경 전이로 일반화되는지를 묻는다.
* **연결의 근거:** 사람의 정서 전이 mental model은 실제 경험 표집 자료의 전이율을 정확히 예측하고, 정적 정서 지식만으로 설명되지 않는 동역학 정보를 담는다(doi:10.1073/pnas.1616056114, 초록). 현재 정신 상태의 신경 패턴은 전이 가능성이 높은 미래 상태의 패턴을 닮는다(doi:10.1523/JNEUROSCI.1431-18.2018, 초록). Ma & Kragel 2026은 지도 구조가 사건 전이의 통계적 규칙성 학습에서 올 수 있다고 썼다(frontier-ai CH1이 인용한 Discussion 다섯째 단락). LLM은 대규모 텍스트에서 "이 정서 다음에는 무엇이 오는가"의 분포를 학습했을 수 있다.
* **연구 질문:** LLM이 텍스트 지식에서 추정한 정서 전이 확률과 인간 mental model은, Emo-FilM 평정의 경험적 전이를 통제한 뒤에도 보류된 영화에서 fMRI 정서 상태 전이를 예측하는가?
* **설계:**
  1. 전이 사전확률 세 종: (a) LLM 다음 정서 분포(base 판본의 표본 분포를 우선, LS-R4-1과 연결) [AI 추정], (b) 인간 mental model(Thornton & Tamir 방식 평정, 공개 자료 접근 확인 필요, 없으면 R2 소규모 수집), (c) Emo-FilM 평정의 경험적 전이(학습 영화에서만 계산).
  2. 신경 전이: 정서 항목 encoding으로 시점별 정서 패턴을 얻고, 시점 t의 패턴이 시점 t+k의 패턴을 예측할 때 각 사전확률로 가중한 혼합이 얼마나 도움이 되는지 본다(Thornton 2019의 "현재 패턴이 미래 상태 패턴을 닮는다" 논리를 시계열로 이전).
  3. 일반화(S): leave-one-film-out. (c)는 학습 영화에서만, (a)와 (b)는 영화와 무관하다. Spacetop narratives 텍스트판으로 같은 분석을 반복해 매체 간 일반화를 본다.
* **측정 가능한 예측:**
  * P1: 언어 유래 전이(a)가 유사도만 쓴 모형(정적 정서 지식, 대칭)보다 보류 영화의 신경 전이를 더 잘 예측한다.
  * P2: (a)의 추가 예측력은 hippocampus와 vmPFC에서 크고 감각 영역에서 작다.
* **반증 조건:** (a)와 (b)가 (c)와 대칭 유사도 모형을 넘는 예측력을 보이지 않으면 기각한다. 이 경우 신경 정서 전이는 영화 특이 사건 구조로 설명되며 일반 전이 지식의 증거가 없다는 결론이다.
* **가능한 데이터셋:** Emo-FilM(주, 13 discrete + Feeling 항목 1 Hz), Spacetop narratives(텍스트, 매체 간 확장)
* **근거 논문 ID:** doi:10.1073/pnas.1616056114, doi:10.1523/JNEUROSCI.1431-18.2018, doi:10.1038/s41467-025-68240-z, doi:10.3758/s13428-024-02569-z(LLM 사건 분할의 규범 근사)
* **선행 수행 검색:** WebSearch "language model emotion transition probabilities predict neural state transitions naturalistic movie fMRI mental state prediction"(2026-11-12). 결과: LLM embedding으로 참가자 정서 해석을 fMRI에 사상한 학회 포스터(NeuroLang 2025, search_index), LLM 연속 감성 라벨 decoding(arXiv:2606.07707), HMM 상태 전이 연구(정서 사전확률 없음). Thornton 2019는 통제 과제에서 전이 예측 패턴을 보고. 자연 영화에서 언어 유래 전이 사전확률의 보류 영화 일반화는 검색 범위 내 미발견. **판정: partially** (Thornton 2019가 통제 과제에서 핵심 논리를 보임)
* **label-provenance:** 신경 전이의 정서 축은 felt / 별도 평정자 규범(Emo-FilM). 전이 사전확률은 AI 추정(LLM), 별도 평정자(mental model 평정), 규범 평정의 경험적 통계
* **evidence-level:** R0 / **insilico-vs-observed:** 관찰(LLM 분포는 예측 변수) / **G1:** 불필요(평정과 fMRI만), 단 영화별 사건 구조 nuisance를 MLLM으로 만들면 필요(보유)
* **위험:** 1 Hz 평정은 반복 시청 평정자의 것이라 전이 시점이 앞당겨질 수 있다(multimodal-dynamics 지적). 영화 14편이라 fold가 14개다. BI-P1, GI-P2(전이 방향성)와 discussed 3개 조합(D+K+N)에 가까우므로 Round 3 검토에서 차별점(언어 유래 사전확률과 보류 영화 일반화)을 다시 확인해야 한다.
* **overlap:** Emo-FilM 연구 (Emo-FilM에서 시간 정보 기여 분석과 인접)

---

## 5. 검토했으나 기각한 미논의 쌍

| 쌍 | 검토한 연결 | 기각 이유 |
|---|---|---|
| M+W | 회상 cue의 다중 양식(영어 텍스트 + 일본어 번역)과 회상 중 양식 통합 | Mind captioning은 cue를 두 언어로 동시에 보여 줘 언어나 양식별 효과를 분리할 수 없다. 회상은 시각 심상만 요구했고 청각 회상 조건이 없다. 데이터로 검정할 대비가 없다 |
| K+L | LLM appraisal 방향을 steering한 반사실 서사를 encoding model에 넣어 예측 뇌 변위의 기하(선형성, 직교성)를 보는 설계 | Spacetop narratives 8편으로 학습한 encoding model은 in-silico steering 예측을 신뢰할 만큼 강하지 않다. 강한 사전학습 encoder를 쓰면 결론이 뇌가 아니라 그 encoder의 성질이 된다. R1에 머무는 결과를 정서 신경과학 질문으로 포장하는 것은 억지 연결이라 판단 |
| T+V | LLM이 생성한 행동 경향 가설을 자동 평가하는 과학적 발견 파이프라인 | 행동 경향 측정은 Emo-FilM Motivation 10항목뿐이고, 가설 생성 평가의 대상이 될 독립 검증 자료가 없다. 억지 연결 |
| Q+V | 행동 경향 항목의 평정 신뢰도와 기계 대체 가능성 | 연결은 성립하지만 이미 LS-P5(CPM 성분별 alt-test, Motivation 포함)와 BI-P2(Axis V 경쟁 검정)로 다뤄진다. 예상 밖 연결이 아니다 |
| J+W | 기억 보강 모델의 학습 목표와 인간 회상 비교 | 우리 데이터의 회상 과제(눈 감고 심상, 72클립)와 연결할 구체적 학습 목표 대비가 없다. 억지 연결 |
| P+W | 회상 준비 구간을 "입력 제거" 자연 실험으로 보는 인과 해석 | 준비 구간은 cue 텍스트 입력이 있는 구간이라 입력 제거가 아니다. 독립 제안으로는 기각하고, cue 읽기 대조 조건으로 LS-R4-2에 흡수했다 |
| B+K, T+W | 지각 표상의 기하, 회상 평가 체계 | 내 담당(Axis C, U)과 연결되는 고리를 억지 없이 만들지 못했다. 담당 에이전트(vision-decoding, geometry-info, adversarial-reviewer)에게 맡긴다 |

## 부록. 검색 기록

| 날짜 | 경로 | 질의 | 대상 | 결과 요약 |
|---|---|---|---|---|
| 2026-11-12 | WebSearch | base versus instruction-tuned RLHF language model emotion annotation distribution diversity human annotator disagreement self-report vs observer | LS-R4-1 | arXiv:2604.27345(확인, 추가), Dsouza & Kovatchev 2025(search_index). base vs 선호 최적화의 본인 보고 대 규범 비교 미발견 |
| 2026-11-12 | arxiv.org/abs | 2303.17548, 2310.06452, 2604.27345 | LS-R4-1 | 서지 확인, Santurkar 2023 본문 Limitations와 4절 확인 |
| 2026-11-12 | WebSearch | multimodal language model representation of video versus text description compared to brain encoding-retrieval similarity during recall fMRI | LS-R4-2 | 회상 fMRI와 MLLM 비교 연구 미발견 |
| 2026-11-12 | Crossref, PubMed 전문 | doi:10.1038/nn.4450, doi:10.1038/s41467-023-41648-1 | LS-R4-2, 3 | Discussion 확인 |
| 2026-11-12 | WebSearch | transmission chain serial reproduction emotional content retention predicts neural reinstatement memory recall fMRI video clips | LS-R4-3 | 결합 연구 미발견 |
| 2026-11-12 | Crossref, PubMed 전문 | doi:10.1073/pnas.2313790120 | LS-R4-3 | Discussion 전체 확인 |
| 2026-11-12 | WebSearch | language model emotion transition probabilities predict neural state transitions naturalistic movie fMRI mental state prediction | LS-R4-4 | NeuroLang 2025 포스터(search_index), arXiv:2606.07707, HMM 연구. 언어 유래 전이 사전확률 일반화 미발견 |
| 2026-11-12 | Crossref | doi:10.1523/JNEUROSCI.1431-18.2018 | LS-R4-4 | 서지와 초록 확인(PMC 전문 비어 있음) |
