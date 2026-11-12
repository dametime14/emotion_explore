# Round 3 (Constructive Disagreement): frontier-ai 검토

* 검토자: frontier-ai (Axis I, J, R 관점)
* 기준일: 2026-11-12
* 절차: `reference/protocols.md` P3. 배정: `outputs/discussion/round3_assignment.md`
* 배정 제안: **LS-P1** (llm-semantics → vision-decoding), **BI-P1** (brain-inspired → geometry-info), **ET-P6** (emotion-theory → vision-decoding)
* 읽은 원문: 각 제안의 보낸 에이전트 `round2.md` 2절 해당 항목, 근거 chain(llm-semantics round1 Chain 1, vision-decoding round1 R6과 R2, brain-inspired round1 Chain 1, geometry-info round1 C2, emotion-theory round2 ET-P6가 인용한 문헌), `outputs/literature/literature_db.csv`
* 선행 검색: 날짜는 모두 2026-11-12. export.arxiv.org API는 이날 계속 429를 반환해 arXiv 질의는 실행하지 못했고(우회하지 않음), WebSearch, Crossref API, PubMed MCP로 검색했다. 새로 확인한 논문 8편은 `outputs/agents/frontier-ai/literature.jsonl`에 추가했다.
* 태그 표기: label-provenance, evidence-level(R0~R4), insilico-vs-observed, G1 (axis_encyclopedia 0.2절)

## 요약 판정

| 제안 | 이미 연구됨? | 판정 | 핵심 지적 | 핵심 수정 |
|---|---|---|---|---|
| LS-P1 | partially | **수정 후 유지 (우선순위 높음)** | 고유 분산이 캡션 encoder 선택과 공변량 측정오차에 크게 의존. 72개 반복 클립만으로는 고유 분산 신뢰구간이 넓음 | 20개 캡션을 이용한 측정오차 보정, 교차 적합 잔차화, video 동역학 feature 추가, 다중 text encoder 민감도 |
| BI-P1 | partially (방향성 SR 검정은 시각 순서에서 수행됨) | **수정 후 유지 (전제 조건부)** | 정서 전이의 방향성이 서사, 장면 전이의 방향성으로 설명될 수 있음. HRF 지연과 평정 지연의 오추정이 가짜 방향성을 만든다 | 내용 SR 경쟁 모형, 지연 sweep과 음성 대조 영역, Ekman식 successor-vs-predecessor 패턴 검정 |
| ET-P6 | partially (회상 중 valence 재활성과 망 수준 지각/정서 분리가 보고됨) | **수정 후 유지 (범위 축소)** | type-2(meta-d') 틀이 이 자료에 맞지 않음. 회상의 정서 해독이 cue의 의미 지식일 수 있음 | 서수 혼합모형, 회상 시점 의미 해독을 시행별로 통제, feature 공간별 재활성(FSIC)과 지각 신뢰도 정규화 |

---

## 1. LS-P1: 정서 배제 인간 캡션으로 설명하고 남는 정서 분산 (기술 잔차) 통합 설계

**원 제안 요약:** vision-decoding R6과 llm-semantics Chain 1을 합친다. (1) 캡션의 정서 누출 감사(정서 어휘 수, LLM reader 추정 [AI 추정]), (2) 중첩 기준선 L1a 시각 feature → L1b + 정서 배제 인간 캡션 embedding → L2 + 정서 언어로 재작성한 캡션 embedding [AI 추정] → C&K 34/14 [felt, 별도 평정자 규범]의 영역별 고유 분산, (3) Mind captioning 72클립 x 5회로 noise ceiling, Horikawa 2020으로 재현, 회상 조건에서 반복. label-provenance와 evidence-level(R0) 표기 있음.

### 1.1 이미 연구된 것은 아닌가: **partially**
* 검색 경로(2026-11-12):
  * WebSearch "emotion unique variance fMRI after controlling caption language model embeddings scene descriptions video emotion ratings variance partitioning" → Du et al. 2025(arXiv:2509.24298)는 같은 비디오의 캡션을 LLM 입력으로 써 LLM, MLLM, 인간 평정 표상의 뇌 설명력을 비교했지만 캡션 embedding을 nuisance로 둔 잔차 분석은 아니다. EmoMind(arXiv:2605.16739)는 중립 캡션을 decoding에 썼고 분산 분할은 하지 않았다.
  * PubMed `(emotion[Title/Abstract]) AND (fMRI[Title/Abstract]) AND (caption*[Title/Abstract] OR "language model"[Title/Abstract]) AND (video*[Title/Abstract] OR movie*[Title/Abstract])`, 2022년 이후 → 0건.
  * literature_db 대조: Doerig 2025(doi:10.1038/s42256-025-01072-0)는 캡션 LLM embedding의 고차 시각피질 정렬(정서 없음). Horikawa 2020(doi:10.1016/j.isci.2020.101060)은 정서, 시각, 의미(73 이진 항목) 모델을 따로 적합해 비교. adversarial-reviewer D2(신뢰도 반영 정서 고유 분산의 포화 곡선)가 방법론적으로 인접.
* 판정 근거: 구성 요소(캡션 embedding encoding, 정서 대 의미 모델 비교)는 있고, "정서 배제 지시로 쓴 인간 캡션을 기준선으로 둔 중첩 분할"은 이 검색 경로에서 찾지 못했다.

### 1.2 단순한 모델 적용에 불과한가: **아니다. 다만 encoder 하나로 하면 그렇게 된다**
측정 설계 질문이라는 점에서 단순 적용이 아니다. 그러나 결과(고유 분산의 크기와 위치)는 캡션을 어떤 text encoder로 embedding하느냐에 크게 좌우된다. LLM embedding은 정서 함의를 다르게 실어 나르며(arXiv:2510.22042는 LLM hidden state에 언어와 데이터셋을 넘는 정서 부분공간이 있다고 보고, 초록 기준), 한 encoder 결과만 보고하면 "그 모델이 정서 함의를 얼마나 실었는가"를 잰 셈이 된다.

### 1.3 실제로 Neuroscience Question을 해결하는가: **그렇다, 단 질문 범위를 정확히 써야 한다**
* 해결하는 질문: Horikawa 계열 데이터에서 "규범 정서 신호가 언어로 기술 가능한 장면 의미로 환원되는가, 어느 영역에서 환원되지 않는가". 구성주의의 "개념 지식이 정서를 구성한다" 주장과 지각, appraisal 기반 설명을 가르는 데 쓸 수 있고, Horikawa 2020의 "정서 모델 우위"(따로 적합한 비교, adversarial-reviewer U1)를 직접 재검정한다.
* 해결하지 못하는 질문: 잔차는 "참가자가 느낀 정서"가 아니다. 잔차에는 (a) 사람이 이름 붙이기 어려운 시각 정서 feature(Kragel 2019 Discussion 둘째 단락, doi:10.1126/sciadv.aaw4358), (b) 규범 평정의 측정 잡음, (c) 캡션이 놓친 비정서 내용이 섞인다. 결론은 "언어화된 장면 의미가 함축하는 규범 정서 vs 그 외"로 한정해야 한다(제안자 반론 1의 대응과 같은 방향이며 동의한다).

### 1.4 Emotion 이외의 요소를 decoding하는 것은 아닌가: **설계 목적이 바로 그것을 가르는 것이지만, 두 구멍이 있다**
1. **L1a 시각 feature의 범위:** 정지 이미지 DNN만 쓰면 움직임, 속도, looming 같은 동역학 정서 단서가 "정서 잔차"로 넘어간다. Horikawa는 비디오다. video 모델(V-JEPA 2, arXiv:2506.09985, 또는 VideoMAE) feature를 L1a에 넣어야 "시각"이 동역학까지 덮는다.
2. **L2 재작성 캡션의 provenance:** 정서 언어로 재작성한 캡션 [AI 추정]의 추가 설명력은 클립 고유 정서가 아니라 LLM의 일반 정서 prior(장면 유형별 전형 정서)일 수 있다. 같은 재작성을 클립 순서를 섞은 캡션에 적용한 null(재작성 prior만 남는 조건)을 둬야 한다.

### 1.5 현재 Dataset으로 검증할 수 있는가: **가능, 단 통계 단위가 작다**
* Mind captioning: 학습용 2,180 클립은 1회 제시, noise ceiling은 72클립 x 5회 반복에서만 나온다. 고유 분산을 noise ceiling 대비 비율로 내면 72개 점의 비율이라 신뢰구간이 넓다. 사전 검정력 계산(클립 bootstrap)이 필요하다.
* 20개 캡션 파일이 사용자 보유본에 있는지 미확인(사용자 결정 기록, vision-decoding 0.1절). Horikawa 2020 공개 전처리본은 블록 평균, 5명. 두 코호트 피험자 중복 미확인.
* label-provenance: C&K 34/14 [felt, 별도 평정자 규범], 인간 중립 캡션 [기술 의미, 인간], 재작성 캡션과 LLM reader 추정 [perceived affective quality, AI 추정]. evidence-level: R0. G1: 시각, video feature에 필요(보유).

### 1.6 더 강력한 모델이나 분석 방법이 있는가: **있다**
1. **캡션 측정오차 보정:** 클립당 20개 캡션이 있으므로 캡션을 10개씩 나눈 split-half로 캡션 embedding의 신뢰도를 차원별로 추정하고, errors-in-variables 보정(SIMEX나 신뢰도 기반 disattenuation)을 적용한다. 불완전하게 측정된 공변량의 잔여 교란(Westfall & Yarkoni 2016, doi:10.1371/journal.pone.0152719)을 정면으로 다루는 방법이며, 이 데이터셋에만 있는 이점(다중 독립 캡션)을 쓴다.
2. **교차 적합 잔차화:** 캡션 embedding(과 시각 feature)으로 C&K 평정을 예측하는 모형을 클립 그룹 교차 적합으로 학습하고, 예측 성분("언어가 함축하는 규범 정서")과 잔차 성분("언어화되지 않는 규범 정서")을 각각 뇌 encoding에 넣는다. 분산 분할과 같은 질문이지만 두 성분을 직접 지도로 그릴 수 있어 해석이 명확하다.
3. **다중 text encoder 민감도:** 문장 encoder, LLM 여러 층, 다국어 모델(llm-semantics Chain 6)로 L1b를 반복하고 결과의 범위를 보고한다.
4. **rank 대역별 분할:** 개인 간 cross-decomposition 스펙트럼(arXiv:2409.06843)의 rank 대역마다 잔차 성분의 설명력을 보면 "정서 잔차가 상위 공유 차원에 있는가, 개인 특이 고rank에 있는가"를 함께 답한다(geometry-info C1과 연결).
5. **leakage:** 같은 원본 영상에서 잘린 클립을 같은 fold에 묶는다(adversarial-reviewer D7).

### 1.7 결과가 기대와 다를 때도 과학적으로 유의미한가: **그렇다, 사전 기술 조건 하나**
* 잔차 약 0: Horikawa 계열의 규범 정서 신호는 기술 가능한 장면 의미로 운반된다. Horikawa 2020 결론의 해석을 직접 바꾼다.
* 잔차가 시각피질에만: 언어화되지 않는 지각적 정서 feature(EmoNet 계열 주장)를 지지.
* 잔차가 transmodal(vmPFC, 섬엽, 편도체)에: 기술 의미 너머의 정서 신호. 다만 경험의 증거는 아니다.
* 조건: 잔차 0이 검정력 부족 때문이 아님을 보이려면 양성 대조(예: 저수준 시각 feature의 고유 분산이 같은 절차로 검출되는지)와 신뢰구간을 사전 기술해야 한다.

### 1.8 수정안
1. L1a에 video 동역학 feature(V-JEPA 2 또는 VideoMAE)를 정지 DNN feature와 함께 넣는다.
2. 20개 캡션 split-half로 캡션 embedding 신뢰도를 추정하고 errors-in-variables 보정 결과를 보정 전 결과와 나란히 보고한다.
3. 분산 분할과 별도로 교차 적합 잔차화(언어 함축 성분 vs 비언어 성분)를 일차 산출물로 둔다.
4. L1b text encoder를 3종 이상으로 반복하고, L2 재작성 단계에는 클립을 섞은 null을 둔다.
5. 72클립 noise ceiling 분석 전에 클립 bootstrap 검정력 계산과 양성 대조를 사전 등록한다.
6. (선택) FA-P6와 결합: L2를 재작성 캡션 embedding [AI 추정, 출력] 대신 VLM 내부 정서 vector 투영 [AI 추정, 내부 표상]으로도 정의해 두 측정을 비교한다.
* overlap: EmoViS (affective brain geometry의 sensory-semantic 기원)

---

## 2. BI-P1: 정서 지도의 방향성 검정 (successor geometry 통합안)

**원 제안 요약:** geometry-info C2(정적 유사성 지도 vs 경험된 전이 지도, 해마 장축의 할인율 γ 위계)를 brain-inspired의 방향성 대조 SR(T) vs SR(T')와 가치 가중 SR로 확장. 순서: (1) 식별 가능성 시뮬레이션(SR(T), SR(T'), 정적 RDM, TEM-무작위, TEM-경험 전이, random-feature null), (2) 실제 데이터 비교, (3) γ 장축 위계. Emo-FilM 주, Horikawa는 음성 대조. label-provenance: felt / 별도 평정자 규범(z-score). evidence-level: R0.

### 2.1 이미 연구된 것은 아닌가: **partially**
* 검색 경로(2026-11-12):
  * WebSearch "successor representation emotion transitions hippocampus vmPFC fMRI asymmetric emotion transition predictive map" → Ma & Kragel bioRxiv(doi:10.1101/2025.06.03.657722)와 보도 자료, 그리고 **Ekman, Kusch, de Lange (2023, eLife, doi:10.7554/eLife.78904, Crossref 확인, 초록)**: 시각 순서 학습 후 단일 항목 제시에서 V1이 successor 위치에서만 활성되고 predecessor 위치에서는 활성되지 않았으며 해마는 시간 거리에 민감했다. **SR의 방향성(후속 vs 선행)을 인간 fMRI에서 직접 검정한 선례**다.
  * Crossref query "Thornton Tamir mental state transitions neural predictive" → Thornton, Weaverdyck, Tamir 2019(doi:10.1523/JNEUROSCI.1431-18.2018, literature_db verified, 제안자가 이미 인용), Thornton et al. PsyArXiv 2020 "Transition dynamics shape mental state concepts"(doi:10.31234/osf.io/kbcsj, 행동, preprint, 존재만 확인), Thornton & Tamir 2024(doi:10.1038/s41467-024-44870-7).
  * PubMed `("successor representation" OR "transition probabilit*") AND emotion* AND (fMRI OR hippocamp*)`, 2017년 이후 → 12건, 모두 정신질환의 휴지기 HMM 상태 전이 연구. 정서 지식의 SR 연구 없음.
* 판정 근거: 방향성 검정 논리(Ekman 2023)와 정신상태의 미래 상태 예측(Thornton 2019)은 있다. 자연 영화의 정서 전이로 만든 SR(T) vs SR(T')를 해마-vmPFC에 적용한 연구는 이 검색 경로에서 찾지 못했다. 제안의 새로움은 "정서 도메인, 자연 전이, TEM과의 경쟁"이며, 방향성 검정 자체를 새로움으로 내세우면 안 된다.

### 2.2 단순한 모델 적용에 불과한가: **아니다**
식별 가능성 시뮬레이션을 먼저 두고 대칭 성분이 같은 SR(T)와 SR(T')를 대조하는 설계는 "모델을 붙여 보기"가 아니라 가설 판별 설계다. Ma & Kragel이 검정하지 않은 해석("지도는 사건 전이의 통계 학습에서 온다", Discussion 다섯째 단락)을 직접 시험한다.

### 2.3 실제로 Neuroscience Question을 해결하는가: **그렇다**
해마-vmPFC 정서 지도가 유사도 지도인지 예측 지도인지는 정서의 cognitive map 이론과 예측 처리 이론을 잇는 질문이다. 다만 2.4의 내용 교란을 통제하지 않으면 "정서 지도"가 아니라 "서사 지도"의 방향성을 잴 위험이 있다.

### 2.4 Emotion 이외의 요소를 decoding하는 것은 아닌가: **핵심 위험이 여기 있다**
* 영화에서 정서 전이는 장면, 서사 전이와 함께 일어난다. 서사에는 강한 방향성이 있다(도입 → 갈등 → 절정 → 해소). 따라서 정서 평정으로 만든 T의 비대칭은 서사, 장면 내용 전이의 비대칭을 상당 부분 물려받는다. 해마가 사건 순서(내용)의 예측 지도를 가진다면 SR(T) > SR(T')는 정서와 무관하게 나올 수 있다.
* 필요한 통제: **내용 SR 경쟁 모형.** 같은 시간축에서 시각-의미 상태(V-JEPA 2 latent나 장면 캡션 embedding을 군집화한 상태)의 전이 행렬 T_c로 SR(T_c)와 SR(T_c')를 만들고, 정서 SR의 방향성 이점이 내용 SR의 방향성 이점을 통제한 뒤에도 남는지 본다. V-JEPA 2 predictor는 과거에서 미래로만 예측하므로 내용 쪽 방향성 표상을 자연스럽게 준다(arXiv:2506.09985, 내 round2 IM7).

### 2.5 현재 Dataset으로 검증할 수 있는가: **가능하지만 두 시간 교란이 방향성 검정을 직접 오염시킨다**
1. **HRF 지연 오추정이 가짜 방향성을 만든다.** 시점 t의 BOLD 패턴이 실제로는 t-δ의 상태를 반영하는데 지연을 짧게 잡으면 뇌 패턴이 "앞선 상태"와 더 닮아 보이고(predecessor 쪽), 길게 잡으면 "다음 상태"와 더 닮아 보인다(successor 쪽). SR(T) vs SR(T')의 차이는 정확히 이 방향의 비대칭이므로 지연 오추정에 민감하다. 대응: 영역별 지연을 독립 자료(다른 영화, 또는 시각 feature encoding)로 추정하고, 지연을 sweep해 방향성 이점이 지연에 견고한지 보고하며, 시각피질을 음성 대조 영역으로 둔다(정서 SR 방향성이 시각피질에서도 같은 크기면 지연 인공물 의심).
2. **평정 시계열의 지연과 앞당김.** Emo-FilM consensus는 평정자 반응 지연(수 초)을 포함하고, 평정자가 같은 영화를 최대 6번 봐서 예측적 앞당김이 생길 수 있다(doi:10.7554/eLife.64972, multimodal-dynamics 개념 5). T의 방향 추정 자체가 이 이동에 영향을 받는다. 대응: 평정 시계열과 자극 feature의 교차상관으로 평정 지연을 추정해 보정하고, 보정 전후의 T를 모두 쓴다.
* 기타: 14편 leave-one-film-out, 영화 정체성 혼입(제안자 반론 2), 작은 효과 크기(r 약 0.04~0.10). label-provenance: felt / 별도 평정자 규범(z-score). G1: 내용 SR에는 필요(보유).

### 2.6 더 강력한 모델이나 분석 방법이 있는가: **있다**
1. **Ekman식 패턴 기반 방향성 검정:** RDM 모델 비교 대신, 시점 t의 신경 패턴이 "다음에 올 정서 상태의 전형 패턴"과 "직전 정서 상태의 전형 패턴" 중 어느 쪽을 더 닮는지를 직접 비교한다(전형 패턴은 학습 영화에서 추정). 대칭 성분이 자동으로 상쇄되어 SR(T) vs SR(T') 대비보다 검정력이 높을 수 있다(doi:10.7554/eLife.78904의 successor vs predecessor 논리).
2. **동역학 비교:** 지도의 기하가 아니라 흐름을 비교하는 DSA(arXiv:2306.10168)로 평정 동역학과 신경 동역학의 벡터장 유사도를 보고, 내용 동역학(V-JEPA 2 latent)과의 유사도와 경쟁시킨다.
3. **encoding 판:** SR feature(현재 상태의 할인된 미래 점유)를 시간 회귀자로 쓰는 encoding으로 γ를 영역별로 적합하면 RDM 수준보다 시간 정보를 덜 버린다.
4. **시뮬레이션의 확장:** 제안의 1단계 시뮬레이션에 "HRF 지연 오추정"과 "평정 지연"을 넣어, 이 두 교란만으로 가짜 방향성이 얼마나 생기는지 정량화한다(Han 2023식 정답 기반 검증, arXiv:2302.06677).

### 2.7 결과가 기대와 다를 때도 과학적으로 유의미한가: **그렇다, 지연 견고성 조건부**
* SR(T) ≈ SR(T'): Ma & Kragel의 지도는 유사도 구조로 충분하다(제안자의 반증 조건). 의미 있는 결과다.
* SR(T') > SR(T): 해마가 미래가 아니라 지난 정서의 흔적(회고적 지도)을 담는다는 결과로 이것도 해석 가능하다.
* 정서 방향성 이점이 내용 SR 통제 후 사라짐: "정서 지도의 예측성은 서사 지도의 예측성"이라는 결과로, 정서 특이 계산이 아니라 범용 사건 예측의 일부라는 해석을 지지한다(내 Round 1 CH1, U1과 같은 질문).
* 단, 방향성 결과가 지연 sweep에서 뒤집히면 어떤 결과도 해석하지 않는다는 규칙을 사전 기술해야 한다.

### 2.8 수정안
1. 선행 목록에 Ekman 2023(doi:10.7554/eLife.78904)을 넣고, 새로움을 "정서 도메인, 자연 전이, TEM 경쟁"으로 한정한다.
2. 내용 SR 경쟁 모형(V-JEPA 2 latent 또는 캡션 embedding 상태의 SR(T_c), SR(T_c'))을 필수 대조로 추가한다.
3. 영역별 HRF 지연을 독립 자료로 추정하고 지연 sweep, 시각피질 음성 대조를 넣는다. 평정 지연도 추정, 보정한다.
4. 1단계 시뮬레이션에 지연 교란 시나리오를 추가한다.
5. RDM 대조와 함께 Ekman식 successor-vs-predecessor 패턴 검정을 일차 분석 후보로 둔다.
* overlap: Emo-FilM 연구 (Emo-FilM 시간 정보 기여, 약함)

---

## 3. ET-P6: 회상 vividness가 정서 부분공간 재활성을 따르는가 (Axis W, Introspective Access)

**원 제안 요약:** vision-decoding R2(같은 클립 회상의 정서 재활성, NEVER 검증)를 Axis A의 Introspective Access와 Axis W로 확장. (a) 재활성을 시각 부분공간(저수준 DNN decoder)과 정서 부분공간(34/14 규범 decoder를 시각, 의미 feature로 잔차화)으로 나누고, vividness가 어느 쪽을 더 잘 가르는지 type-2 민감도(ROC, meta-d' 논리)로 비교, (b) vividness가 낮은 시행에서도 정서 재활성이 남는가. Mind captioning 회상(주), Horikawa 2020 지각(보강). 선행: 비정서 비디오 재생의 재활성-vividness(doi:10.1162/jocn_a_00839), feature 수준별(doi:10.1038/s41467-020-15763-2)은 partially.

### 3.1 이미 연구된 것은 아닌가: **partially (제안자가 적은 것보다 넓게)**
* 검색 경로(2026-11-12):
  * WebSearch "emotional video recall imagery fMRI reactivation emotion decoding vividness trial-wise affective memory reinstatement" → St-Laurent 2015(doi:10.1162/jocn_a_00839, 비정서), Park & Kim 2025 bioRxiv(doi:10.1101/2025.11.22.689961, Crossref 확인, 초록): fNIRS 전전두에서 정서 비디오 시청과 회상 사이 valence, arousal 교차 분류 성공.
  * WebSearch "metacognition mental imagery vividness ratings track neural reactivation strength fMRI decoding type-2 sensitivity" → vividness와 재활성 상관 연구들(Bone 2020 등)은 있으나 type-2(meta-d')와 decoding을 짝지은 연구는 찾지 못함.
  * PubMed `(recall OR "mental imagery" OR reinstatement OR reactivation) AND emotion* AND fMRI AND (video* OR film* OR movie*) AND (vividness OR decoding OR multivariate)`, 2015년 이후 → 6건. 관련 2건: **Kim & Kim 2025**(Brain and Cognition, doi:10.1016/j.bandc.2025.106296, PubMed 확인, 초록): 영화 시청-회상 fMRI(Chen 2017 자료)에서 valence 표상이 하측두, 방추회에서 시청과 회상 사이에 일관. **Curko et al. 2026**(eNeuro, doi:10.1523/ENEURO.0146-26.2026, PubMed 확인, 초록): 정서 뉴스 비디오 회상에서 배내측 DMN 하위망은 기억의 정서가와, 내측두 하위망은 지각 세부와 연관되고 패턴 안정성도 같은 해리.
* 판정 근거: "회상 중 정서(valence) 재활성"은 fMRI에서 이미 보고되었고(Kim & Kim 2025), "지각 세부 vs 정서 톤의 회상 기여 분리"도 망 수준에서 보고되었다(Curko 2026). 남은 새로움은 (i) 34범주 수준의 정서 부분공간, (ii) 같은 클립의 반복 지각 대비 재활성 비율, (iii) 시행별 vividness와 부분공간별 재활성의 결합이다.

### 3.2 단순한 모델 적용에 불과한가: **아니다. 다만 type-2 틀은 이 자료에 맞지 않는다**
* meta-d'와 HMeta-d(doi:10.1093/nc/nix007)는 1차 과제의 정답/오답이 있는 이진 판단에 대한 확신도의 민감도를 잰다. 이 제안에서 "1차 정답"은 decoder가 낸 재활성 강도(연속값, 잡음 큼)이고 vividness는 심상의 생생함 보고다. 즉 참가자는 정서에 대한 판단을 하지 않았고, vividness가 "정서 재활성"을 보고하라는 지시도 없었다. 이를 metacognitive sensitivity라 부르면 측정 대상을 과장한다(제안자 반론 5와 6이 일부를 인식).
* 권고: "vividness와 부분공간별 재활성의 결합(coupling)"으로 이름을 바꾸고, 서수 혼합모형으로 추정한다. Introspective Access와의 연결은 "생생함 보고가 감각 재활성과 정서 재활성 중 무엇에 접근하는가"라는 약한 형태로만 쓴다.

### 3.3 실제로 Neuroscience Question을 해결하는가: **부분적으로 그렇다**
* 해결하는 질문: 주관적 생생함이 감각 재활성과 정서 재활성 중 어느 것에 결합하는가(NEVER 모델의 "부정 정서가 감각 재현을 강화" 예측, doi:10.3758/s13423-017-1313-9), 정서 재활성이 생생한 심상 없이도 일어나는가.
* 약한 부분: (b)를 LeDoux & Brown(doi:10.1073/pnas.1619316114)의 "무의식 정서" 논쟁 증거로 쓰는 것은 vividness가 정서 자각 보고가 아니므로 성립하기 어렵다(제안자도 탐색적으로만 쓴다고 명시). 이 연결은 빼거나 부록으로 내리는 것이 낫다.

### 3.4 Emotion 이외의 요소를 decoding하는 것은 아닌가: **회상에서는 그럴 위험이 지각보다 크다**
* 회상은 텍스트 cue로 시작한다. 지각 시점에 시각, 의미 feature로 잔차화한 정서 decoder를 회상에 적용해도, 회상 시점에 cue가 불러온 **의미 지식**(이 클립은 장례식 장면이다)이 정서 decoder 출력을 움직일 수 있다. 지각 시점 잔차화는 회상 시점 의미 인출을 제거하지 못한다.
* 필요한 통제: (1) 회상 시점에 의미 decoder(중립 캡션 LM feature)와 시각 decoder 출력을 시행별로 함께 내고, 정서 decoder 출력에서 이 둘을 회귀로 제거한 "회상 시점 잔차 정서 재활성"을 쓴다. (2) cue 텍스트 자체의 정서 함축(LLM reader 추정 [AI 추정])을 공변량으로 넣어 cue가 직접 유발한 정서를 분리한다. (3) Mind captioning 원 논문이 보인 의미 재활성(회상 캡션 생성)을 양성 대조로 둔다.

### 3.5 현재 Dataset으로 검증할 수 있는가: **가능하지만 (b)는 검정력이 걱정된다**
* Mind captioning 회상: 72클립 x 5회 x 6명, 시행별 vividness 5점(논문 기준, 사용자 보유본의 파일 존재는 미확인). 비디오 재생 vividness 연구에서는 평정이 상단에 몰리는 경향이 있어(Bone 2020 계열 자료의 분포가 높은 값에 몰렸다는 검색 요약, [search_index]) "낮은 vividness 시행"이 적을 수 있다. (b)는 시행 수를 먼저 세고 결정해야 한다.
* 회상 직후 비디오 재제시와 HRF 겹침, S1 사전 노출(vision-decoding R2 교란 목록). 지각 decoder는 Horikawa 2020(5명)과 Mind captioning 학습 2,180 클립으로 학습 가능하나 두 코호트 피험자 중복 미확인.
* label-provenance: decoder 목표 [felt, 별도 평정자 규범], vividness [참가자 본인, 심상 보고]. evidence-level: R0. G1: 필요(보유).

### 3.6 더 강력한 모델이나 분석 방법이 있는가: **있다**
1. **feature 공간별 재활성(FSIC 방식):** decoder 대신 Bone 2020(doi:10.1038/s41467-020-15763-2)의 feature-specific informational connectivity처럼, 여러 feature 공간(저수준 DNN, 캡션 LM, video 모델, VLM 내부 정서 vector [AI 추정, 내부 표상])별로 지각 패턴과 회상 패턴의 대응을 같은 틀에서 잰다. 규범 decoder를 잔차화하는 것보다 부분공간 정의가 안정적이고, frontier-ai의 모델 내부 정서 vector를 정서 부분공간의 한 정의로 쓸 수 있다.
2. **지각 신뢰도 정규화:** Mind captioning 지각 테스트의 72클립 x 5회 반복으로 클립별 지각 패턴 신뢰도(noise ceiling)를 구하고, 재활성 강도를 그 신뢰도로 나눈다. 정서 부분공간이 원래 신뢰도가 낮아 재활성이 작아 보이는 문제를 줄인다.
3. **서수 혼합모형:** vividness(서수) ~ 시각 재활성 + 정서 재활성 + 의미 재활성 + (피험자, 클립 무선효과). meta-d'보다 자료 구조에 맞고 개인 내 척도 사용 차이(제안자 반론 6)를 무선효과로 흡수한다.
4. **망 수준 대조:** Curko 2026이 보고한 배내측 DMN(정서) vs 내측두(지각) 해리를 같은 자료에서 재현하는 것을 1단계로 두면, 부분공간 분석의 해석 기준이 생긴다.

### 3.7 결과가 기대와 다를 때도 과학적으로 유의미한가: **대체로 그렇다**
* vividness가 시각 재활성에만 결합하고 정서 재활성은 독립: 생생함 보고는 감각 재현에 대한 접근이며 정서 재활성은 별도 경로라는 해석(Curko 2026의 망 해리와 정합).
* vividness가 정서 재활성에도 결합: NEVER의 정서-감각 결합 예측을 지지.
* 정서 재활성이 전혀 없음: 정서 재활성 부재와 decoder 감도 부족을 구분할 수 없다. 양성 대조(의미 재활성)와 지각 신뢰도 정규화가 있어야 의미 있는 음성 결과가 된다.

### 3.8 수정안
1. 선행 목록에 Kim & Kim 2025(doi:10.1016/j.bandc.2025.106296)와 Curko 2026(doi:10.1523/ENEURO.0146-26.2026), Park & Kim 2025(doi:10.1101/2025.11.22.689961)를 넣고 새로움을 34범주 부분공간, 같은 클립 반복 지각 대비, 시행별 vividness 결합으로 한정한다.
2. type-2/meta-d' 대신 "vividness-재활성 결합"을 서수 혼합모형으로 추정한다. Introspective Access 연결은 약한 형태로만 쓰고 LeDoux & Brown 연결은 부록으로 내린다.
3. 회상 시점의 의미, 시각 decoder 출력과 cue 텍스트 정서 함축을 시행별 공변량으로 넣어 "회상 시점 잔차 정서 재활성"을 쓴다.
4. feature 공간별 재활성(FSIC 방식)으로 부분공간을 정의하고, VLM 내부 정서 vector를 정서 부분공간의 대안 정의로 포함한다(frontier-ai FA-P6와 공유 도구).
5. 지각 테스트 반복으로 재활성 강도를 정규화하고, (b)는 낮은 vividness 시행 수를 확인한 뒤 진행 여부를 정한다.
* overlap: 없음(기존 프로젝트 요약 기준)

---

## 4. 검증 상태

* 이 문서에서 근거로 쓴 ID는 `literature_db.csv`의 verified 항목이거나, 이번에 Crossref, PubMed, arxiv.org abs 페이지로 확인해 `literature.jsonl`에 추가한 것이다: doi:10.7554/eLife.78904, doi:10.1038/s41467-024-44870-7, doi:10.1101/2025.11.22.689961, doi:10.1016/j.bandc.2025.106296, doi:10.1523/ENEURO.0146-26.2026, doi:10.1162/jocn_a_00839, doi:10.1038/s41467-020-15763-2(이번 추가분은 모두 초록 수준). doi:10.31234/osf.io/kbcsj와 doi:10.1101/2025.06.03.657722는 Crossref와 검색 결과로 존재만 보았고 근거로 쓰지 않았다.
* Bone 2020 계열 vividness 분포가 높은 값에 몰린다는 서술은 검색 요약 [search_index] 수준이다.
* export.arxiv.org API는 검색 당일 429를 반환해 arXiv 질의를 하지 못했다. "partially" 판정은 위 검색 경로 안의 판단이며, Stage 4 선행연구 중복 감사에서 arXiv 경로로 다시 확인해야 한다.
