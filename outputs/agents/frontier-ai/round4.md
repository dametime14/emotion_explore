# Round 4 (Unexpected Connections): frontier-ai

* 에이전트: frontier-ai (Axis I, J, R)
* 기준일: 2026-11-12
* 절차: `reference/protocols.md` P4. 출발점: `outputs/combinations/discussed_pairs.md`의 미논의 2개 조합 23개. Axis 유형표: `outputs/axis_encyclopedia.md` 3절.
* 원칙: 미논의 쌍을 최소 하나 포함하고, 서로 다른 유형에서 3개 이상의 Axis를 조합하며, 그중 하나 이상은 Affective Neuroscience 밖의 개념이나 방법(외부 분야 또는 I, J, K, L, R)이다. 억지로 이을 수 없는 쌍은 기각하고 이유를 적었다(4절).
* 선행 검색: 2026-11-12, WebSearch, Crossref API, arxiv.org abs 페이지, PubMed MCP. export.arxiv.org API는 이날 429로 쓰지 못했고 우회하지 않았다. 새로 확인한 논문 13편을 `literature.jsonl`에 추가했다(누적 57편).
* 태그: label-provenance, evidence-level(R0 상관 / R1 모델 내 개입 / R2 새 행동 평정 / R3 새 fMRI 자극 조작 / R4 뇌 개입), insilico-vs-observed, G1.

## 요약

| ID | 제목 | 포함한 미논의 쌍 | 조합 Axis (유형) | 외부 개념 | evidence-level |
|---|---|---|---|---|---|
| FA-R4-1 | 회상은 단서로부터의 예측인가: 생성 모델의 "상상"을 기준선으로 한 일화 고유 정서 재활성 | I+W, L+W, N+W (부분적으로 M+W, R+W) | W (Construct), I, L (Model & Method), F (Neural), N (Model & Method) | 생성형 비디오 모델, 기억의 생성 모델 이론 | R0 (+ in-silico 기술자) |
| FA-R4-2 | Empowerment: latent action world model로 계산한 "통제 가능성"은 통제 appraisal과 행동 경향의 자극 계산 대리인가 | J+V, K+V, F+V | V (Construct), J (Model & Method), K (Structure), F (Neural), U (Inference) | 강화학습의 내재 동기(empowerment), 정보이론 | R0 |
| FA-R4-3 | 라벨 출처를 "뷰"로: 식별 가능한 multi-view 학습으로 출처 불변 정서와 출처 고유 정서를 분리하고 뇌가 어느 쪽을 따르는지 | J+U | U (Inference), J (Model & Method), A (Construct), F (Neural) | 식별성 이론, 다중 평정자 학습 | R0 |
| FA-R4-4 | 표상 궤적의 굽음: straightening이 깨지는 순간이 정서적 놀람인가 | B+K, D+S | B, D (Construct), K (Structure), E (Neural), I (Model & Method), S (Inference) | 시각 과학의 perceptual straightening, 곡률 기반 SSL | R0 |

기각, 이관한 쌍: T+W, T+V, S+V, O+V, P+W, P+V, Q+V(흡수), D+G(이관), K+L, K+P(이관), M+V(이관). 이유는 4절.

---

## FA-R4-1. 회상은 단서로부터의 예측인가: 생성 모델의 "상상"을 기준선으로 한 일화 고유 정서 재활성

### 조합
* Axis: **W** Internally Generated Experience (Construct), **I** AI Model Families와 **L** Generative & Counterfactual Methods (Model & Method, 텍스트 조건 비디오 생성 모델), **N** Brain-like Computation (기억의 생성 모델 이론), **F** Brain Representation (Neural)
* 포함한 미논의 쌍: **I+W, L+W, N+W**. 회상 cue가 텍스트이고 재활성 대상이 시각 표상이므로 M+W(양식 간 재활성)도 부분적으로 포함한다. 선택적으로 SAE 개념 공간에서 재활성을 재면 R+W도 포함된다.
* 외부 개념: 생성형 비디오 모델이 텍스트에서 "상상"한 영상(arXiv:2503.20314, Wan, literature_db 등재), 기억 구성의 생성 모델 이론(doi:10.1038/s41562-023-01799-z)

### 왜 예상 밖의 연결인가
회상 중 정서 재활성 연구(ET-P6, vision-decoding R2)의 가장 큰 교란은 "회상에서 해독된 정서가 그 장면에 대한 일반 지식(schema)인가, 그 클립을 본 일화의 재현인가"이다(내 round3_reviews.md 3.4절). Spens & Burgess (2024)는 일화 기억이 고유 feature와 schema 기반 예측을 결합해 생성 모델로 재구성되며 같은 모델이 상상을 지원한다고 정식화했다(초록). 그렇다면 **cue만 보고 생성 모델이 "상상한" 영상**은 schema 예측의 구체적 대리물이 된다. 사람의 회상 재활성 중 이 상상으로 예측되는 부분과 실제 시청 패턴에만 맞는 부분을 나누면 schema와 일화를 측정 수준에서 분리할 수 있다. 생성 AI를 자극 편집(Axis L의 통상 용도)이 아니라 "기억 이론의 schema 기준선"으로 쓰는 것이 새 연결이다.

### 연구 질문
정서 비디오 클립을 텍스트 cue로 회상할 때 재활성되는 신경 표상(시각, 의미, 정서 부분공간) 중 얼마가 cue만으로 예측 가능한 schema 성분(텍스트 조건 생성 모델의 상상과 cue→feature 회귀로 추정)이고 얼마가 그 클립에 고유한 일화 성분이며, 정서 부분공간은 시각 세부보다 schema 쪽에 더 치우치는가?

### 설계
1. 지각 encoding model: Mind captioning 각 피험자의 지각 학습 자료(2,180 클립 1회)로 feature 공간별(저수준 DNN, V-JEPA 2, 중립 캡션 LM, VLM 정서 vector [AI 추정, 내부 표상], C&K 34/14 [별도 평정자 규범]) voxel encoding model을 학습한다.
2. 세 개의 "기대 패턴"을 회상 클립마다 만든다. (a) 실제 패턴: 같은 클립 지각 테스트(5회 반복) 평균. (b) 생성 상상 패턴: 회상 cue 텍스트로 생성 비디오 모델이 만든 영상(시드 여러 개)의 feature를 encoding model에 넣은 예측 패턴. (c) 회귀 schema 패턴: 다른 클립에서 학습한 cue 텍스트→feature 회귀로 예측한 feature의 encoding 예측 패턴.
3. 회상 시행마다 feature 부분공간별로 회상 패턴과 (a), (b), (c)의 유사도를 잰다. **일화 고유 지수 = 유사도(a) - max(유사도(b), 유사도(c))**, 부분공간별로 계산.
4. 시행별 vividness(참가자 본인)와 일화 고유 지수의 결합을 서수 혼합모형으로 추정한다.

### 측정 가능한 예측과 반증 조건
* 예측 A(schema 우세 가설): 정서 부분공간의 일화 고유 지수가 시각 저수준 부분공간보다 작다. 즉 회상의 정서는 장면 지식으로 대부분 예측된다.
* 예측 B(정서 강화 기억 가설, NEVER 계열, doi:10.3758/s13423-017-1313-9): 부정 정서가가 높은 클립에서 정서와 시각 부분공간 모두의 일화 고유 지수가 크다.
* 두 예측은 서로 경쟁한다. 반증 조건: 모든 부분공간에서 일화 고유 지수가 클립 순서를 섞은 null과 구분되지 않으면 "회상 재활성은 schema 재구성으로 충분하다"고 결론하고 일화 성분 주장을 철회한다. 생성 상상(b)과 회귀(c)가 서로 크게 다르면 schema 기준선 자체가 불안정한 것이므로 해석을 보류한다.

### 가능한 데이터셋
* **Mind captioning**(주): 회상 72클립 x 5회 x 6명, 시행별 vividness, 지각 학습 2,180 클립, 지각 테스트 72클립 x 5회(논문 기준. 사용자 보유본에 회상, vividness, cue 텍스트 파일이 실제로 있는지는 미확인).
* Horikawa 2020: 지각 encoding의 feature 공간 선택과 재현(피험자가 달라 회상 분석에는 쓰지 않음).

### 근거 논문 ID
doi:10.1126/sciadv.adw1464, doi:10.1038/s41562-023-01799-z, arXiv:2503.20314, doi:10.1162/jocn_a_00839, doi:10.1038/s41467-020-15763-2, doi:10.1016/j.bandc.2025.106296, doi:10.1523/ENEURO.0146-26.2026, doi:10.3758/s13423-017-1313-9, doi:10.1016/j.neunet.2025.107515(생성 prior가 재구성 내용을 지배하는 문제, vision-decoding 인용)

### 선행 수행 여부: **no (이 검색 경로 안에서), 이론과 구성 요소는 partially**
* WebSearch "memory recall fMRI reinstatement predicted from cue semantic knowledge versus episodic specific generative model imagination baseline"(2026-11-12) → 생성 모델로 회상의 schema 기준선을 만든 연구 없음. 관련: 기억 공고화의 생성 모델 이론(doi:10.1038/s41562-023-01799-z, Crossref 확인), 상상에서의 해마 세부 재활성(검색 요약, 서지 미확인), 단어 cue 장면 회상의 변형된 재활성(검색 요약, 서지 미확인).
* Round 3에서 실행한 PubMed 검색(회상 + 정서 + fMRI + 비디오)에서 회상 중 valence 재활성(doi:10.1016/j.bandc.2025.106296)과 DMN 하위망의 정서/지각 해리(doi:10.1523/ENEURO.0146-26.2026)를 확인. schema 대 일화 분리는 없음.

### 태그
* label-provenance: 정서 부분공간은 [felt, 별도 평정자 규범](C&K) 또는 [AI 추정, 내부 표상](VLM vector). vividness는 [참가자 본인, 심상 보고]. cue 텍스트와 생성 영상은 자극 기술자이며 라벨이 아니다.
* evidence-level: R0. 생성 영상은 개입이 아니라 schema 예측의 in-silico 기술자다. insilico-vs-observed: 혼합. G1: 필요(보유).
* overlap: 없음(기존 프로젝트 요약 기준). ET-P6, vision-decoding R2와 같은 자료를 쓰므로 공동 설계 대상.

### 위험
생성 모델의 학습 분포와 내용 필터가 정서적 장면(폭력, 성적 내용) 생성을 왜곡해 정서 부분공간의 schema 기준선이 편향될 수 있다. cue 텍스트가 짧으면 생성의 분산이 커서 (b)의 신뢰도가 낮다(시드 다중화와 (c)와의 일치로 점검). 회상 직후 비디오 재제시와의 HRF 겹침(vision-decoding R2 교란 목록).

---

## FA-R4-2. Empowerment: latent action world model로 계산한 "통제 가능성"은 통제 appraisal과 행동 경향의 자극 계산 대리인가

### 조합
* Axis: **V** Action Readiness & Affordance (Construct), **J** Learning Objectives (Model & Method: 내재 동기 목표인 empowerment), **K** Geometry & Mathematical Structure (Structure: 정보이론의 channel capacity), **F** Brain Representation (Neural), **U** Label Provenance (Inference: 평정자 appraisal vs 자극 계산량)
* 포함한 미논의 쌍: **J+V, K+V, F+V**
* 외부 개념: 강화학습과 인공생명의 empowerment(행동에서 미래 감각으로의 channel capacity, doi:10.1109/CEC.2005.1554676, arXiv:1310.1863). 외부 분야 목록의 "Reinforcement Learning / Computational Value"에 해당.

### 왜 예상 밖의 연결인가
Component Process Model의 appraisal에는 "통제 가능성(control/coping potential)"이 있고(doi:10.1080/02699930902928969), Emo-FilM은 이를 **Controlled**(EventControlled / Uncontrolled) 항목으로 1 Hz 평정했다(Stage 1 dataset_EmoFilM.md 항목표). 그러나 통제 가능성을 자극에서 계산하는 모델은 없었다. 한편 AI 쪽에는 "행위자가 자기 행동으로 미래를 얼마나 바꿀 수 있는가"를 정보이론으로 정의한 empowerment가 있고, 라벨 없는 영상에서 latent action과 그 조건부 미래 예측기를 학습하는 모델(LAPA의 latent action quantizer, arXiv:2410.11758; Genie, arXiv:2402.15391)이 생겼다. latent action 조건 forward model 위에서 "장면에서 가능한 행동들이 만드는 미래의 다양성"을 계산하면 **장면 수준 empowerment**가 되고, 이것을 통제 appraisal과 행동 경향의 자극 계산 대리로 시험할 수 있다. 신경과학 쪽에서는 통제 가능성이 접근/회피 편향을 조절한다는 계산 근거(doi:10.1038/s41467-019-13737-7)와 통제 가능성 추론 모형(doi:10.1038/s41562-022-01306-w)이 있다.

### 연구 질문
자연 영화에서 latent action 조건 world model로 계산한 장면 수준 empowerment는 평정자의 통제 가능성 appraisal(Controlled)과 행동 경향(Motivation 10항목 중 Tackle, Command, Oppose 대 Stop, Undo)을 움직임 에너지, 장면 컷, 일반 예측오차를 넘어 설명하며, 그 시계열이 통제 가능성 추론과 관련된 뇌 영역 반응을 평정보다 먼저 또는 평정과 독립적으로 설명하는가?

### 설계
1. 프레임 t에서 LAPA의 latent action quantizer(현재 프레임 + latent action → 다음 프레임 복원) 디코더로 codebook의 모든 latent action에 대한 예측 다음 프레임을 만들고, 그 표상(V-JEPA 2 feature)의 분산 또는 Blahut-Arimoto로 근사한 channel capacity를 empowerment E_t로 둔다. 1-step과 다단계(H step) 판을 만든다.
2. 통제 변수: optical flow 크기, 장면 컷, V-JEPA 2 surprise(FA-P3), 인물 수와 얼굴 크기, 카메라 운동.
3. 1단계(평정 수준, G1 필요): E_t가 Controlled, Agent, Urgency와 Motivation 항목을 통제 변수 위에서 설명하는가(평정 지연 보정, 영화 단위 교차검증).
4. 2단계(뇌 수준): E_t, Controlled 평정, 통제 변수를 banded ridge에 넣어 ROI(통제 가능성 추론 문헌에서 사전 지정, 사전 지정 목록은 Ligneul 2022 등 본문 확인 후 확정)와 전뇌에서 고유 분산을 추정한다.

### 측정 가능한 예측과 반증 조건
* 예측 1: E_t는 Controlled 평정과 양의 관계를 보이며, 이 관계는 움직임 에너지와 surprise를 통제해도 남는다.
* 예측 2: 높은 E_t 구간에서 Motivation의 접근, 대결 항목(Tackle, Command, Oppose)이 높고 철회 항목(Stop, Undo)이 낮다(통제 가능성이 접근 편향을 늘린다는 계산 예측과 같은 방향).
* 반증: E_t가 움직임 에너지나 카메라 운동의 재표현에 불과하면(통제 후 고유 설명력 0) "자극 계산 통제 가능성" 가설은 기각된다. E_t가 평정은 설명하나 뇌 고유 분산이 없으면 통제 appraisal은 평정자의 사후 판단 구성물이며 시청 중 신경 계산의 직접 대응물이 아니라는 해석이 지지된다.

### 가능한 데이터셋
* **Emo-FilM**(주): Controlled, Agent, Urgency appraisal과 Motivation 10항목 1 Hz 별도 평정자 평정, 첫 시청 참가자 fMRI와 생리.
* Spacetop alignvideo: 평정은 영상 단위 사후 평정뿐이라 뇌 수준 재현(E_t 시계열과 BOLD)만.
* Horikawa 2020, Mind captioning: 짧은 무음 클립이라 E_t 계산은 가능하나 통제 appraisal 라벨이 없어 보조.

### 근거 논문 ID
doi:10.1109/CEC.2005.1554676, arXiv:1310.1863, arXiv:2410.11758, arXiv:2402.15391, doi:10.1080/02699930902928969, doi:10.1038/s41467-019-13737-7, doi:10.1038/s41562-022-01306-w, doi:10.1073/pnas.2414005122(장면 affordance, literature_db 등재), arXiv:2506.09985

### 선행 수행 여부: **no (이 검색 경로 안에서)**
* WebSearch "empowerment intrinsic motivation emotion appraisal controllability computational model brain fMRI"(2026-11-12) → empowerment, 정서 appraisal, fMRI를 결합한 연구 없음. 통제 가능성 추론 fMRI 연구(다중 행위자 통제 가능성 추론, 사회적 통제 가능성의 vmPFC 가치 투영 등, 검색 요약 수준)와 empowerment의 제어 이론 연구(검색 요약 수준)는 따로 있음.
* Round 2 검색(latent action을 encoding feature로 쓴 fMRI 연구 없음)과 일치.

### 태그
* label-provenance: Controlled, Motivation은 [felt, 별도 평정자 규범, 반복 시청자]. E_t는 자극 계산 기술자(라벨 아님). 해석상 E_t는 화면 속 장면의 통제 가능성(portrayed 쪽)이고 평정은 평정자가 느낀 통제 appraisal(felt 쪽)이라는 대비를 유지한다.
* evidence-level: R0. insilico-vs-observed: 관찰(E_t는 자극 기술자). G1: 필요(보유).
* overlap: 없음(기존 프로젝트 요약 기준). brain-inspired BI-P2(Axis V 경쟁 설계)에 E_t를 하나의 band로 추가하는 형태로 결합 가능.

### 위험
LAQ는 로봇, 손 조작 영상으로 학습되어 영화 장면에서 latent action의 의미가 불명확하다(LAPA 6절 한계: 조작 비디오 밖 미탐색). Codebook이 카메라 운동을 주로 표상하면 E_t는 "카메라가 얼마나 움직일 수 있는가"가 된다. 그래서 카메라 성분을 제거한 판과 인물 영역 마스크 판을 함께 만든다. 장면 수준 empowerment는 특정 인물의 통제 가능성이 아니므로 "누구의 통제인가"는 답하지 못한다. 정보이론 추정량의 편향(코드북 크기, 시드)도 보고해야 한다.

---

## FA-R4-3. 라벨 출처를 "뷰"로: 식별 가능한 multi-view 학습으로 출처 불변 정서와 출처 고유 정서를 분리하고 뇌가 어느 쪽을 따르는지

### 조합
* Axis: **U** Label Provenance & Perspective (Inference & Measurement), **J** Learning Objectives (Model & Method: 식별 가능한 multi-view contrastive), **A** Emotion & Affective Constructs (Construct), **F** Brain Representation (Neural). 보조로 Q(신뢰도).
* 포함한 미논의 쌍: **J+U**
* 외부 개념: 다중 모달 contrastive learning의 block 식별성(arXiv:2303.09166), 뷰 설계가 content를 정의한다는 원리(arXiv:2106.04619), 서로 다른 평정자가 서로 다른 부분집합을 주석한 경우의 contrastive 회귀(arXiv:2112.15411), NLP의 human label variation(arXiv:2211.02570, literature_db 등재)

### 왜 예상 밖의 연결인가
라벨 출처 문제(Axis U)는 지금까지 "어느 출처의 라벨이 뇌를 더 잘 설명하는가"라는 경쟁 비교로 다뤄졌다(emotion-theory C4, adversarial-reviewer D4). 식별성 이론은 다른 틀을 준다. 같은 자극 시점에 대한 여러 출처의 평정(평정자 1, 평정자 2, ..., fMRI 참가자 본인, AI)을 **같은 잠재 정서의 서로 다른 뷰**로 보면, contrastive 학습은 모든 뷰에 공통인 block(출처 불변 성분)을 식별하고 뷰마다 변하는 성분(출처 고유 성분)은 style로 남긴다. 이렇게 나눈 두 성분 중 어느 쪽이 뇌 반응을 설명하는가는 "뇌의 정서 신호는 공유된 정서인가, 특정 관점의 정서인가"라는 질문을 출처를 경쟁시키지 않고 분해해서 묻는다.

### 연구 질문
Emo-FilM에서 평정자별 1 Hz 평정, fMRI 참가자의 사후 클립 평정, MLLM 연속 주석을 같은 잠재 정서의 뷰로 둔 식별 가능한 multi-view 학습으로 출처 불변 성분과 출처 고유 성분을 분리할 때, 편도체, 섬엽, vmPFC 반응은 출처 불변 성분으로 충분히 설명되는가, 아니면 fMRI 참가자 본인 평정의 고유 성분이 그 참가자의 뇌를 추가로 설명하는가?

### 설계
1. 뷰 정의: Emo-FilM 항목 x 영화마다 3~4명의 별도 평정자(disjoint 주석, arXiv:2112.15411의 상황), fMRI 참가자의 사후 클립 평정(영화당 5항목, 영화 길이의 약 20%), MLLM 연속 주석([AI 추정, 출력]과 [AI 추정, 내부 표상] 두 판).
2. 학습: 시점 단위로 뷰 간 contrastive 정렬, encoding 차원을 sweep하며 공유 block 크기를 추정(arXiv:2303.09166의 content 요인 수 추정 논리). 출처 고유 성분은 각 뷰에서 공유 block을 제거한 잔차로 둔다.
3. 식별성 사전 점검: 알려진 공유, 고유 구조를 심은 합성 평정 자료로 block이 회복되는지 시뮬레이션(정답 기반 검증, arXiv:2302.06677의 논리).
4. 뇌 분석: 공유 block, 별도 평정자 고유 성분, 참가자 본인 고유 성분, AI 고유 성분을 banded ridge에 넣고 영화 단위 교차검증으로 영역별 고유 분산을 추정한다.

### 측정 가능한 예측과 반증 조건
* 예측 1: 정서 관련 영역의 설명 분산은 대부분 출처 불변 block에 있다(규범 평정이 뇌를 잘 설명한다는 기존 결과와 정합).
* 예측 2(privileged access의 약한 검정): fMRI 참가자 본인 평정의 고유 성분이 그 참가자의 뇌에서만 고유 분산을 가지며, 다른 참가자의 뇌에서는 갖지 않는다.
* 예측 3: AI 고유 성분은 시각, 의미 영역에서만 고유 분산을 갖는다(AI가 장면 내용을 평정에 섞는다는 가설).
* 반증: 공유 block이 무작위 projection과 같은 크기의 뇌 설명력밖에 없으면 "출처 불변 정서" 개념이 이 자료에서 뇌와 연결되지 않는다. 예측 2에서 본인 고유 성분이 다른 참가자의 뇌도 같은 정도로 설명하면 그것은 개인 고유 경험이 아니라 평정 형식 차이(사후 클립 재시청)다.

### 가능한 데이터셋
* **Emo-FilM**(주): 평정자별 원자료가 공개된 유일한 데이터셋, fMRI 참가자 사후 클립 평정(부분).
* **Spacetop** alignvideo(보조): 참가자 본인 평정과 나머지 참가자 평균(규범 대리), MLLM 주석. 시간 연속 평정이 없어 영상 단위 분석만.
* Horikawa 2020, Mind captioning, NSD: 평정자 개인 자료가 없어 해당 없음.

### 근거 논문 ID
arXiv:2303.09166, arXiv:2106.04619, arXiv:2112.15411, arXiv:2211.02570, arXiv:2501.10970(alt-test, literature_db 등재), arXiv:2508.05880, arXiv:2510.04064, doi:10.1038/s41597-025-04803-5(Emo-FilM 데이터 논문, literature_db 등재), arXiv:2302.06677

### 선행 수행 여부: **no (뇌 기준, 이 검색 경로 안에서), ML 구성 요소는 있음**
* WebSearch "annotator-invariant shared latent multi-view contrastive learning multiple label sources emotion ratings brain fMRI"(2026-11-12) → 평정자 불변 contrastive 회귀(arXiv:2112.15411, 비뇌), 뇌 반구를 뷰로 둔 multi-view 정서 decoding(arXiv:2211.02629, 라벨 출처를 뷰로 쓰지 않음), 다중 평정자 연속 정서 주석이 있는 StudyForrest 기반 연구(검색 요약 수준). 라벨 출처를 뷰로 두고 뇌가 따르는 성분을 분해한 연구는 없음.

### 태그
* label-provenance: 이 제안의 핵심 변수 자체가 출처다. [felt, 별도 평정자 규범, 개별 평정자], [felt, 참가자 본인, 사후 재시청], [AI 추정, 출력 / 내부 표상]. 대상은 모두 felt 문항(평정자 자신의 경험 보고)이며 MLLM은 그 문항에 대한 추정.
* evidence-level: R0. insilico-vs-observed: 관찰. G1: MLLM 주석에만 필요(보유).
* overlap: Emo-FilM 연구 (부분, 같은 데이터셋의 정서 맥락 분석)

### 위험
항목 x 영화당 평정자가 3~4명뿐이라 공유 block 추정의 분산이 크다. 참가자 사후 평정은 영화 길이의 약 20%만 덮어 예측 2의 검정력이 낮다(사전 검정력 계산 필수). 평정자 내 z-score로 절대 수준 정보가 없다. contrastive 학습은 용량 제한이 없으면 공유되는 모든 것을 인코딩하므로(arXiv:2303.09166 7절), "공유"에는 평정 형식의 공통 편향(예: 영화 시작부 기준선 이동)도 들어간다.

---

## FA-R4-4. 표상 궤적의 굽음: straightening이 깨지는 순간이 정서적 놀람인가

### 조합
* Axis: **B** Perceptual & Stimulus Representation과 **D** Temporal Dynamics (Construct), **K** Geometry & Mathematical Structure (Structure: 궤적 곡률), **E** Neural Targets (Neural), **I** AI Model Families (Model & Method: video SSL 표상), **S** Generalization & Robustness (Inference: 라벨 없는 지표의 데이터셋 간 일반화)
* 포함한 미논의 쌍: **B+K, D+S**
* 외부 개념: 시각 과학의 perceptual straightening(doi:10.1038/s41593-019-0377-4)과 V1의 신경 궤적 straightening(doi:10.1038/s41467-021-25939-z), 곡률을 줄이는 SSL 목표(arXiv:2411.01777), 모델의 straightening 조건(arXiv:2308.13870)

### 왜 예상 밖의 연결인가
시각 과학은 뇌가 자연 비디오의 표상 궤적을 곧게 만들어 선형 외삽으로 미래를 예측하게 한다는 가설을 세웠다. 그렇다면 **궤적이 갑자기 굽는 순간**은 선형 외삽이 실패하는 순간, 곧 표상 수준의 예측 위반이다. 이 지표는 특정 예측 모델(V-JEPA predictor 등, FA-P3)이 필요 없고, 모델 latent뿐 아니라 **뇌의 다변량 궤적 자체**에서 계산할 수 있다. 정서 연구의 놀람, suddenness appraisal을 표상 기하의 국소 곡률로 정의하면, "뇌가 스스로 예측 위반을 표시하는 순간"을 라벨 없이 찾고 그것이 정서 라벨과 맞는지 묻는 새로운 경로가 생긴다.

### 연구 질문
자연 영화 시청 중 모델 latent와 뇌 다변량 궤적의 국소 곡률 급증은 장면 컷, 움직임, HRF 자기상관을 통제한 뒤에도 정서적 놀람(Suddenly, Predictable appraisal, Surprise 범주)과 편도체, 섬엽 반응을 예측하며, 곡률 급증이 감각 영역보다 transmodal 영역에서 정서 순간에 선택적으로 나타나는가?

### 설계
1. 모델 곡률: V-JEPA 2, DINO 계열 이미지 모델, straightening 목표 모델의 프레임 표상 궤적에서 연속 세 시점 벡터의 각도로 국소 곡률을 계산한다(doi:10.1038/s41467-021-25939-z의 정의). 모델 간 기준선 차이(arXiv:2308.13870)가 있으므로 모델마다 z-점수화.
2. 뇌 곡률: ROI별 다변량 BOLD 궤적에서 같은 곡률을 계산. **Spacetop은 TR 0.46 s**라 곡률 추정에 가장 유리하고, Emo-FilM(TR 1.3 s)은 평정 대응, Horikawa(TR 2 s, 짧은 클립)는 클립 경계 사이 곡률만.
3. HRF와 자기상관 통제: fMRI에서 곡률은 AR(1) 계수와 관련된다는 보고가 있으므로(언어 fMRI의 학회 초록, [search_index]) 각 ROI 시계열의 국소 AR 구조를 맞춘 위상 무작위화 대리 자료로 null 분포를 만든다. 장면 컷, 음량 급변, 광류 크기를 회귀한다.
4. 일반화(S): 곡률-정서 관계를 Emo-FilM에서 추정하고 라벨 없이 Spacetop과 Horikawa에서 같은 ROI의 곡률-편도체 반응 관계가 재현되는지 본다.

### 측정 가능한 예측과 반증 조건
* 예측 1: 모델 곡률 급증 시점에서 Emo-FilM Suddenly 평정이 높고 Predictable이 낮다(평정자 반복 시청으로 인한 앞당김은 지연 추정으로 보정).
* 예측 2: 뇌 곡률 급증은 감각 영역에서는 장면 컷에 주로 묶이고, transmodal 영역(vmPFC, 측두극)에서는 컷을 통제한 뒤에도 정서적 놀람 순간에 남는다.
* 예측 3: 모델 곡률과 transmodal 뇌 곡률의 상관이 감각 영역보다 높다(고차 표상 수준의 예측 위반 공유).
* 반증: 뇌 곡률 효과가 AR 구조를 맞춘 대리 자료 null과 구분되지 않거나 컷, 광류 통제 후 사라지면 "곡률 = 정서적 예측 위반" 가설은 기각된다. 모델 곡률이 V-JEPA surprise로 완전히 설명되면 곡률은 독립 지표가 아니라 surprise의 재표현이다(그 자체로 FA-P3에 대한 검증 결과).

### 가능한 데이터셋
* **Emo-FilM**(평정 대응, 생리), **Spacetop** alignvideo(TR 0.46 s, 뇌 곡률), **Horikawa 2020**(무음 짧은 클립, 클립 내 모델 곡률과 Surprise 범주 평정). NSD는 정지 이미지라 해당 없음, Mind captioning은 Horikawa와 같은 자극이라 보조.

### 근거 논문 ID
doi:10.1038/s41593-019-0377-4, doi:10.1038/s41467-021-25939-z, arXiv:2411.01777, arXiv:2308.13870, arXiv:2506.09985, arXiv:2502.11831, doi:10.7554/eLife.107955(사건 경계의 오차형, 불확실성형, literature_db 등재), doi:10.7554/eLife.64972

### 선행 수행 여부: **no (정서 기준, 이 검색 경로 안에서), straightening 자체는 수행됨**
* WebSearch "trajectory curvature straightening fMRI naturalistic movie neural trajectory surprise event boundary emotion"(2026-11-12) → straightening은 원숭이 V1(doi:10.1038/s41467-021-25939-z), 인간 지각(doi:10.1038/s41593-019-0377-4), 모델(arXiv:2308.13870), 언어 이야기 fMRI의 곡률 추정(CCN 2025 초록, [search_index])에서 보고되었다. 곡률을 정서, 놀람과 연결한 영화 fMRI 연구는 없음. 사건 경계의 패턴 변화 연구(doi:10.7554/eLife.107955)는 곡률이 아니라 오차와 불확실성 기반.

### 태그
* label-provenance: Suddenly, Predictable은 [felt, 별도 평정자 규범, 반복 시청자], Horikawa Surprise는 [felt, 별도 평정자 규범]. 곡률은 라벨이 아닌 표상 지표.
* evidence-level: R0. insilico-vs-observed: 관찰(모델 곡률은 자극 기술자, 뇌 곡률은 관찰). G1: 모델 곡률에 필요(보유), 뇌 곡률만이면 불필요.
* signal-feasibility: 피질하(편도체) 다변량 궤적 곡률은 voxel 수와 tSNR이 낮아 추정이 불안정할 수 있다. 편도체는 곡률 계산 대상이 아니라 반응 대상으로 쓴다.
* overlap: 없음(기존 프로젝트 요약 기준). multimodal-dynamics Chain 2, FA-P3과 같은 질문군이므로 같은 통제 변수 집합을 공유.

---

## 4. 기각하거나 다른 에이전트로 넘긴 쌍

| 쌍 | 판정 | 이유 |
|---|---|---|
| T+W | 기각 | T(검증, 평가 방법)를 W에 붙이면 "회상 자료에 표준 검증 절차를 적용"하는 것 이상의 새 질문이 생기지 않는다. 최소 검증 요건(minimum-validation 태그)은 모든 질문에 이미 붙는다 |
| T+V | 기각 | T+W와 같은 이유. Axis V 질문의 검증 설계는 BI-P2와 내 round3 수정안(평정 수준 공선성 파일럿)으로 충분하다 |
| S+V | 기각 | 행동 경향 라벨은 Emo-FilM(Motivation 10, 별도 평정자)에만 있다. 다른 데이터셋으로의 일반화는 AI 추정 라벨의 일반화가 되어 Axis V 자체의 일반화를 검증하지 못한다. 자극 계산 지표(FA-R4-2의 E_t)는 데이터셋 간 계산은 되지만 일반화를 판정할 라벨이 없다 |
| O+V | 기각 | 행동 경향을 fMRI 참가자 본인이 보고한 자료가 없다(Emo-FilM은 별도 평정자, Spacetop은 행동 경향 문항 없음). 개인차 질문은 신규 수집 없이는 성립하지 않는다 |
| P+W | 기각 | 회상 자료에는 조작이 없다(cue는 클립마다 하나로 고정). 내적 경험에 대한 인과 주장은 R0를 넘을 수 없고, P의 고유 기여(식별 가능한 인과 질문의 지도)를 붙일 대상이 없다 |
| P+V | 기각 | 4개 데이터셋 어디에도 affordance나 행동 가능성을 조작한 조건이 없다. Spacetop 통증 cue는 기대 조작이지 행동 가능성 조작이 아니다. 새 자극 조작(R3)이 필요한 설계라 현재 범위 밖 |
| Q+V | 흡수 | Motivation 항목의 평정자 간 신뢰도는 BI-P2의 파일럿 0단계에서 다루는 하위 단계이며 별도의 예상 밖 연결이 아니다 |
| D+G | 이관 (multimodal-dynamics, vision-decoding) | 시간 해상 decoding은 표준 방법이며 이 쌍이 미논의로 남은 것은 Round 1 chain의 Axis 매핑 근사 때문일 가능성이 크다. 내 담당에서 새로 더할 것이 없다 |
| K+L, K+P | 이관 (geometry-info, generative-counterfactual) | 편집 자극 공간의 기하나 기하 지표의 인과 해석은 두 에이전트의 전문 영역이다. 내 쪽에서 근거 있는 연결안을 만들지 못했다 |
| M+V | 이관 (multimodal-dynamics, brain-inspired) | 시청각 looming이 방어적 행동 준비를 유발한다는 연결은 성립할 수 있으나, 이번 라운드에서 근거로 쓸 verified looming 문헌을 확보하지 못했다. 근거 없이 쓰지 않는다 |
| M+W, R+W | FA-R4-1에 부분 포함 | 텍스트 cue → 시각 회상(양식 간), SAE 개념 공간에서의 재활성을 FA-R4-1의 선택 분석으로 둔다 |
| F+V | FA-R4-2에 포함 | |

## 5. 검증 상태
* 근거 ID는 `literature_db.csv` verified 항목이거나 이번에 Crossref 또는 arxiv.org abs 페이지로 확인해 `literature.jsonl`에 추가한 13편이다: doi:10.1038/s41593-019-0377-4, doi:10.1038/s41467-021-25939-z, arXiv:2411.01777, arXiv:2308.13870, doi:10.1109/CEC.2005.1554676, arXiv:1310.1863, doi:10.1080/02699930902928969, doi:10.1038/s41467-019-13737-7, doi:10.1038/s41562-022-01306-w, doi:10.1038/s41562-023-01799-z, arXiv:2112.15411, arXiv:2211.02629, arXiv:2402.15391. 이 중 Hénaff 2019, Klyubin 2005, Scherer 2009는 서지만 확인했고(초록 미제공) 나머지는 초록 수준이다.
* 검색 요약으로만 본 항목([search_index]): 언어 fMRI 곡률 학회 초록, 통제 가능성 fMRI 연구들의 세부, 상상 중 해마 재활성 연구.
* "no" 판정은 위에 적은 검색 경로 안의 판단이다. arXiv API 경로를 쓰지 못했으므로 Stage 4 중복 감사에서 다시 확인한다.
* 데이터 조건 미확인: Mind captioning 회상, vividness, cue 텍스트 파일의 실제 존재(FA-R4-1), Emo-FilM Controlled 항목의 정확한 문항 지시문(Stage 1 표는 극 이름만 기록, FA-R4-2), Emo-FilM MLLM 주석은 새로 만들어야 함(FA-R4-3).
