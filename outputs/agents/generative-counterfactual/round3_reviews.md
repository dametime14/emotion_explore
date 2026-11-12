# Round 3 검토 (Constructive Disagreement): generative-counterfactual

* 작성: generative-counterfactual (Axis L, P 담당)
* 기준일: 2026-11-12
* 절차: `reference/protocols.md` P3. 배정은 `outputs/discussion/round3_assignment.md`(시드 20261114).
* 검토 대상: **BI-P2**(brain-inspired → frontier-ai), **MD-P1**(multimodal-dynamics → geometry-info), **FA-P6**(frontier-ai → llm-semantics)
* 읽은 원문: brain-inspired `round2.md` BI-P2와 `round1.md` P-2, Chain 2. multimodal-dynamics `round2.md` MD-P1, I-2(Mind captioning 테스트 순서), MD-P3, `round1.md` Chain 1. geometry-info `round1.md` C5. frontier-ai `round2.md` FA-P6, FA-P7, `round1.md` U1, U4, T8. llm-semantics `round1.md` 0절(세 층 분해), Chain 1. 각 제안이 인용한 논문의 기록은 해당 에이전트 `literature.jsonl`에서 확인했다.
* 선행 수행 검색(모두 2026-11-12): arxiv.org/search 웹 검색(전 필드 AND 검색. export.arxiv.org API는 이번 세션에서 429와 시간 초과라 쓰지 않음), WebSearch, Crossref 서지 검색, PubMed MCP. 검색어는 각 절에 적었다. arxiv.org/search의 "결과 0건"은 모든 단어가 함께 나온 기록이 없다는 뜻일 뿐 "선행 없음"을 보증하지 않는다.
* 새로 확인해 `literature.jsonl`에 추가한 논문: doi:10.1097/EDE.0b013e3181d61eeb(음성 대조), doi:10.7326/M16-2607(E-value), doi:10.1038/s43587-022-00341-6(Baez-Lugo 2023), doi:10.1016/j.neuroimage.2025.121439(Marras 2025, Crossref로 존재 확인, 내용은 검색 요약 수준).
* 공통 관점: 각 제안의 결론 수준(R0~R4)이 문장 표현과 맞는지, 그리고 생성 또는 counterfactual 설계로 약점을 보완할 수 있는지를 함께 본다.

---

## 1. BI-P2: Axis V 경쟁 검정, 정서 범주 대 행동 경향 대 자극 계산 affordance

### 1.1 제안 요약
brain-inspired → frontier-ai. Emo-FilM과 Horikawa 2020 + Mind captioning에서 banded ridge에 (a) 정서 범주 band(Emo-FilM discrete 13, Horikawa 34), (b) 인간 평정 행동 경향 band(Emo-FilM Motivation 10), (c) latent action band(LAPA, arXiv:2410.11758), (d) 의미 통제 band(Mind captioning 인간 중립 캡션, Emo-FilM은 MLLM 캡션)를 넣고 transmodal 영역에서 범주 고유 분산이 행동 경향 band로 얼마나 대체되는지 본다. 파일럿 0단계는 평정 수준 공선성(discrete 항목을 Motivation 항목으로 교차 예측한 R²). 원 chain은 brain-inspired Round 1 Chain 2(Horikawa 2020 Discussion 2단락 "emotional experience (or affordances)" 해석의 검증).

### 1.2 판정

**(1) 이미 연구된 것은 아닌가? 판정: partially (제안자 판정과 같음).**
* 행동 경향 성분의 신경 네트워크는 이미 보고되었다: Mohammadi 2023(doi:10.1093/cercor/bhad093, 초록)은 정서 클립에서 approach/avoidance 경향을 포함한 component별 네트워크를, Leitão 2020(doi:10.1371/journal.pbio.3000900, 초록)은 motivation 등 component의 네트워크와 동기화를 보고했다. Morgenroth 2026(doi:10.1037/emo0001619, 초록)은 Emo-FilM 평정에서 13개 이산 정서가 모두 component로 신뢰성 있게 예측된다고 보고했다.
* 인접 선행 후보: Marras 2025(doi:10.1016/j.neuroimage.2025.121439, Crossref 확인, 내용은 검색 요약 수준)는 시청각, 시각 전용, 청각 전용 영화에서 행동 특징 taxonomy(정서 영역 포함 6영역)를 multivoxel encoding과 variance partitioning으로 다뤘다. 정서 범주와 행동 경향의 경쟁 검정인지는 본문 미열람이라 확인하지 못했다.
* 직접 경쟁(같은 banded ridge에서 범주 band가 행동 경향 band로 대체되는 정도)과 영화 장면 latent action band는 찾지 못했다.
* 검색 경로: arxiv.org/search "action tendency fMRI"(0건), "action readiness emotion"(2건, 무관), "latent action fMRI"(0건), "component process model fMRI"(49건, 정서 component 경쟁 검정 없음), "affordance emotion fMRI"(0건). WebSearch "fMRI emotion category versus action tendency motivation component naturalistic film banded ridge encoding component process model"(Marras 2025, McMahon 2023 외 직접 해당 없음).

**(2) 단순한 모델 적용에 불과한가? 판정: 부분적으로 그렇다.**
banded ridge 분산 분할은 표준 도구이고, 새로움은 질문(범주 대 행동 경향의 경쟁)에 있다. latent action band는 단순 적용 위험이 크다. LAPA는 로봇과 사람 조작 비디오로 학습되었고, 원 논문이 latent action이 카메라 움직임도 포착한다고 적었다(arXiv:2410.11758, brain-inspired 기록). 영화에서는 카메라 운동과 편집 컷이 지배할 가능성이 높아, 이 band는 "행동 affordance"가 아니라 "화면 운동"을 측정할 수 있다.

**(3) 실제로 Neuroscience Question을 해결하는가? 판정: 질문은 중요하나 이 설계로는 부분적으로만.**
Horikawa 2020의 "(or affordances)" 해석을 시험한다는 점에서 질문 자체는 정서 이론(기능주의적 action readiness 대 범주적 느낌)에 직결된다. 그러나 banded ridge의 고유 분산은 "어느 feature 공간이 예측에 추가 기여하는가"를 말할 뿐 "그 영역이 무엇을 표상하는가"를 말하지 않는다(feature fallacy, doi:10.1016/j.conb.2019.04.002). 또 "대체된다"는 표현은 인과적 대체처럼 읽히지만 R0의 통계적 분할이다.

**(4) 정서 이외의 요소를 decoding하는 것은 아닌가? 판정: 위험이 크다.**
* Motivation 항목(Oppose, Tackle, Move 등)은 화면 속 행위(싸움, 추격)를 따라가는 경향이 있어 portrayed action의 의미 내용을 재표현할 수 있다. 의미 통제 band가 이를 일부 막지만, Emo-FilM 쪽 통제는 MLLM 캡션(AI 추정)이라 인간 중립 캡션보다 약하다.
* latent action band는 위 (2)처럼 시각 운동 정보일 가능성이 크다.
* 두 평정 band는 모두 별도 평정자 규범 평정이라 "참가자의 행동 준비 상태"가 아니라 "평정자가 장면에서 읽은 행동 경향"이다(label-provenance: felt 보고이지만 주체는 별도 평정자).

**(5) 현재 Dataset으로 검증할 수 있는가? 판정: Emo-FilM은 가능, Horikawa 확장은 조건부.**
Emo-FilM에 Motivation 10항목 1 Hz 평정이 있어 핵심 분석은 가능하다(30명, 14편). 다만 영화 14편이라 영화 수준 공선성이 크다. Horikawa 2020 + Mind captioning에는 행동 경향 평정이 없어 새 주석(인간 또는 AI 추정)이 필요하고, AI 주석이면 [AI-est]로 표기하고 소량 인간 평정으로 PPI 보정해야 한다(doi:10.1126/science.adi6000).

**(6) 더 강력한 모델이나 분석 방법이 있는가? 판정: 있다.**
* **신뢰도 반영 분할.** Emo-FilM은 평정자별 원자료가 있으므로 항목별 split-half 신뢰도로 band를 감쇠 보정하고, 잠재변수 모형으로 공변량 측정 오차를 반영한다(adversarial-reviewer D2, doi:10.1371/journal.pone.0152719). 그렇지 않으면 신뢰도가 낮은 band가 분할에서 체계적으로 불리하다(doi:10.1016/j.neuroimage.2022.119728).
* **counterfactual 자극.** 위협 대상과 정서 범주는 그대로 두고 회피 affordance(출구, 거리, 장애물)만 바꾼 편집 자극을 만들어 encoder 예측(R1)과 인간 평정(R2: 위협, 공포, 도망 가능성 분리)을 보면, 자연 자극의 공선성을 설계로 깬다(내 GC-P8). Bartnik 2025(doi:10.1073/pnas.2414005122)가 affordance 표상이 물체, layout으로 환원되지 않는다고 보인 장면 영역(PPA, OPA)이 표적이 된다.
* **영역 간 일반화를 인과 후보 선별 기준으로.** Emo-FilM에서 학습한 band 가중치가 Horikawa(AI 주석)나 Spacetop으로 일반화되는지를 함께 보면 데이터셋 특이 공선성과 구분된다(doi:10.1162/jocn_a_01623).
* **latent action 대안.** 인간 신체 자세 기반 행동 분할(brain-inspired I-7의 ethogram)과 카메라 운동, optical flow nuisance band를 둔다.

**(7) 결과가 기대와 다를 때도 과학적으로 유의미한가? 판정: 조건부로 예.**
범주 고유 분산이 남으면 범주가 행동 준비로 환원되지 않고, 행동 경향 band가 흡수하면 affordance 해석이 유리하다. 그러나 공선성이 크면 가장 가능성 높은 결과는 "공유 분산이 대부분이고 두 고유 분산이 모두 0 근처"다. 이 결과는 사전에 "이 데이터로는 분리 불가"로 정의해 두지 않으면 해석이 자의적이 된다. 사전 정의해 두면, counterfactual 단계(위 (6))로 넘어가야 할 근거라는 의미가 생긴다.

### 1.3 결론 수준 점검
* evidence-level = R0(제안자 표기와 같음). 다만 본문의 "대체"는 "예측 분산의 중첩"으로 바꿔 써야 한다.
* label-provenance: 범주와 Motivation 모두 felt 보고, 별도 평정자 규범. Horikawa 확장 주석은 [AI-est] 또는 신규 별도 평정자.
* insilico-vs-observed: 관찰(latent action은 자극 feature).

### 1.4 수정안
1. **0단계 판정 규칙을 사전 등록.** discrete를 Motivation으로 교차 예측한 R²가 두 평정의 신뢰도 상한(split-half)에 가까우면 분산 분할을 중단하고 3단계(counterfactual)로 간다. 상한보다 충분히 낮을 때만 2단계로 간다.
2. **분할 결과를 세 성분으로 보고.** 범주 고유, 행동 경향 고유, 공유 분산을 모두 내고, 공유 분산의 크기 자체를 결과로 해석한다. 신뢰도 감쇠 보정과 의미 통제 band의 신뢰도 민감도 곡선을 붙인다.
3. **latent action band 교체 또는 보강.** LAPA 대신 또는 함께 인체 자세 기반 행동 feature를 쓰고, 카메라 운동과 컷을 nuisance band로 둔다. latent action이 nuisance 투입 후 남는 분산이 없으면 이 band는 결론에서 뺀다.
4. **counterfactual 3단계(R1 + R2).** 정서 범주를 고정하고 회피 affordance만 바꾼 편집 자극으로 encoder 예측과 인간 평정을 본다(GC-P8). layout 변화량을 맞춘 비-affordance 대조 편집(출구가 아닌 창문 추가 등)을 함께 둔다.
5. **Horikawa 확장의 주석 규칙.** 행동 경향 AI 주석은 [AI-est]로 표기하고, 무작위 부분집합 인간 평정으로 PPI 보정 또는 alt-test(arXiv:2501.10970)로 대체 가능성을 먼저 판정한다.

**종합:** 질문은 Axis V의 대표 질문으로 가치가 크다. 그대로는 공선성 때문에 "분리 불가"로 끝날 위험이 높으므로 1, 2번 사전 규칙과 4번 counterfactual 단계를 붙이는 조건으로 유지를 권고한다.

---

## 2. MD-P1: 클립 사이 이월과 washout 이완을 하나의 이완 모형으로

### 2.1 제안 요약
multimodal-dynamics → geometry-info. 같은 정서 잠재 차원(규범 평정으로 정의)에 대해 (a) Horikawa 2020, Mind captioning의 2 s 휴지 사이 클립 이월(초 단위)과 (b) Emo-FilM 영화 전후 90 s washout 이완(수십 초)을 하나의 leaky integrator 또는 line-attractor식 이완 모형으로 적합한다. 두 척도에서 같은 영역의 시간상수가 일관되면 "정서 관성 차원"의 근거, 짧은 간격에서만 보이면 HRF 잔여나 시각 적응. Mind captioning 테스트 세트(72클립 x 5회, 런 안 pseudorandom 순서, multimodal-dynamics가 원 논문 Methods로 확인)가 같은 클립의 선행 클립을 바꿔 Horikawa 2020의 고정 순서 교란을 깬다는 점을 지렛대로 쓴다. 원 chain은 multimodal-dynamics Round 1 Chain 1(Horikawa 이월)과 geometry-info Round 1 C5(washout 이완 시간상수).

### 2.2 판정

**(1) 이미 연구된 것은 아닌가? 판정: partially (제안자 판정과 같음).**
* 정서 자극 후 휴식기 이월은 집단 수준에서 여러 번 보고되었다: Eryilmaz 2011(doi:10.1016/j.neuroimage.2010.10.021, 초록: 정서 후 휴식기 ACC, insula 활동과 결합 증가, 점진적 회복), Gaviria 2021(doi:10.1016/j.neuroimage.2021.118377, 초록: 부정 영화 후 휴식기 DMN 발현 증가), Tambini 2017(doi:10.1038/nn.4468, 초록: 정서 뇌 상태의 중립 부호화로의 이월), Baez-Lugo 2023(doi:10.1038/s43587-022-00341-6, 초록: 부정 사회 장면 후 휴식기 DMN-amygdala 연결 강화가 노인에서만, 불안, 반추와 연관). vmPFC 패턴의 수십 초 지속은 Chang 2021(doi:10.1126/sciadv.abf7129)이 보고했다.
* 정서 잠재 차원별 이완 시간상수를 두 시간 척도(초 단위 클립 이월, 수십 초 washout)에서 한 모형으로 추정하고 HRF 잔여와 분리한 연구는 찾지 못했다.
* 검색 경로: arxiv.org/search "emotional carry-over fMRI"(1건, 무관), "emotional inertia fMRI"(0건), "affective hysteresis"(223건, 물리학 위주, 관련 없음). WebSearch "emotional carry-over between consecutive video clips fMRI hemodynamic spillover emotional inertia time constant neural 2024 2025"(Gaviria, Baez-Lugo, 영화 클립 spillover 연구 등, 시간상수 추정은 없음). Crossref 서지 검색으로 Baez-Lugo 2023 확인, PubMed로 초록 확인.

**(2) 단순한 모델 적용에 불과한가? 판정: 아니다.**
leaky integrator 자체는 단순하지만 핵심은 측정 설계(두 시간 척도의 결합, 선행 클립 변이를 이용한 교란 분리)다. 모델 적용 연구가 아니라 측정 문제 연구다.

**(3) 실제로 Neuroscience Question을 해결하는가? 판정: 예, 단 "무엇이 이완하는가"의 정체 확인이 전제다.**
정서 관성의 신경 수준 측정은 정서 동역학 이론(관성, 이월)과 정신의학적 개인차에 직결된다. 그러나 정서 잠재 차원을 규범 평정으로 정의한 뒤 washout에 투사하면, 그 축이 담는 모든 느린 신호(시각-의미 공변량, 자율신경, 주의, 졸음)의 이완을 재게 된다. 축의 정체를 먼저 보증해야 "정서"의 관성이 된다.

**(4) 정서 이외의 요소를 decoding하는 것은 아닌가? 판정: 위험이 크다.**
* 짧은 간격: 짧은 클립을 10 s까지 반복 재생하는 블록 구조라 반복 억제와 시각 적응이 섞이고, 선행 클립의 시각, 의미 내용이 다음 블록에 프라이밍으로 남을 수 있다.
* 긴 간격: washout 이완은 전역 자율신경 성분(전역 신호가 심박, 호흡, PPG와 결합, doi:10.1038/s41593-025-01945-y)과 섞인다. Emo-FilM 제공 전처리본은 WM/CSF 회귀가 적용되어 이 성분을 영역마다 다르게 지우거나 주입할 수 있다(systems-neuro Round 1 4절 C1). 정서 축은 시각-의미 공변량을 회귀한 뒤 정의하거나, 시각 내용을 decoding하지 않음을 확인한 축이어야 한다.

**(5) 현재 Dataset으로 검증할 수 있는가? 판정: 가능, 단 raw 재전처리 필수.**
Horikawa 2020 raw BIDS(연속 시계열), Mind captioning(TR 1 s, 테스트 세트 순서 변이), Emo-FilM(영화 전후 90 s washout, PPG, 호흡, EDA)이 모두 있다. 공개 블록 평균본은 이월을 이미 섞었고, Emo-FilM 제공본의 high-pass(sigma 50 s, geometry-info C5)는 수십 초 이완을 왜곡하므로 raw 재전처리가 필요하다. 라벨은 규범 평정이라 결론은 "자극 정서 정보의 신경 이월"로 한정된다(제안자도 같은 입장).

**(6) 더 강력한 모델이나 분석 방법이 있는가? 판정: 있다. 세 가지가 결론 수준을 올린다.**
* **Mind captioning 선행 클립 변이를 설계 수준 조작으로 쓰기.** 테스트 세트에서 같은 클립이 런 안 pseudorandom 순서로 서로 다른 선행 클립 뒤에 나온다면, 선행 클립(과 그 정서)은 실험자가 무작위로 배정한 변수다. 그러면 "선행 자극의 정서 → 현재 블록 반응"의 효과는 관찰 상관이 아니라 데이터셋 내부의 실제 조작에 대한 효과로 추정할 수 있다(내 round2 5절의 R3-internal 제안). 단 선행 클립의 시각 내용도 함께 무작위 배정되므로, 선행 클립의 정서와 시각-의미 feature를 같은 회귀에 넣어 분리해야 한다. pseudorandom 제약(예: 같은 클립 연속 금지)과 피험자 간 순서 동일 여부는 events 파일로 확인이 필요하다.
* **In silico 이월 기준선.** TRIBE v2에 실제 제시 순서를 그대로 넣어 예측한 반응은 "자극 구동 반응 + 학습된 혈역학"이 만드는 이월을 담는다. 관찰 이월에서 이 예측 이월을 뺀 초과분이 "자극 구동과 HRF로 설명되지 않는 신경 이월"의 후보가 된다. TRIBE v1의 비디오 입력 창은 직전 4 s라(arXiv:2507.22229 2.3절, multimodal-dynamics MD-P3 기록) 창을 넘는 내생 누적은 설계상 예측하지 못한다는 점이 오히려 이 기준선을 깨끗하게 만든다. 공개 TRIBE v2는 피질만이므로 피질 parcel에 한정한다.
* **식별 가능성 시뮬레이션 선행.** TR 2 s(Horikawa), 2 s 휴지, 블록 10 s 구조에서 "HRF만" 대 "HRF + 신경 누출(τ)" 모형을 실제 잡음 수준으로 시뮬레이션해 τ가 몇 초 이상일 때 회복 가능한지 먼저 확인한다(adversarial-reviewer I4, D3의 식별 가능성 논리, arXiv:2302.06677). 회복 불가능한 τ 범위의 결과는 보고하지 않는다.
* 그 밖에 감각 영역(V1) 이완을 HRF 대조로, 참가자 EDA 회복 시간상수를 신체 대조로 두는 것은 제안자, geometry-info C5와 같다.

**(7) 결과가 기대와 다를 때도 과학적으로 유의미한가? 판정: 예.**
두 척도에서 일관된 τ가 나오면 정서 관성 차원, 짧은 척도에서만 나오면 HRF 잔여나 적응, 긴 척도에서만 나오면 자율신경이나 각성 같은 느린 신체 상태 또는 마음 방황, 어느 쪽도 없으면 Horikawa 블록 decoding이 이월에 오염되지 않았다는 방법론 결과다. 마지막 결과도 Horikawa 기반 다른 질문들의 기준선을 정당화하므로 가치가 있다.

### 2.3 결론 수준 점검
* 제안자 표기는 R0, 관찰. Mind captioning 선행 클립 효과에 한해서는 순서 무작위화가 확인되면 **R3-internal**(데이터셋 안의 실제 조작)로 올릴 수 있다. Horikawa 2020(5명 동일 순서)과 Emo-FilM washout은 R0에 머문다.
* label-provenance: 정서 축 정의는 felt 보고, 별도 평정자 규범. 이완 측정 자체는 라벨 비의존.
* insilico-vs-observed: 관찰. TRIBE 이월 기준선을 넣으면 혼합.

### 2.4 수정안
1. **Mind captioning 순서 확인과 R3-internal 분석을 1단계로.** events 파일로 테스트 세트 순서의 무작위화 구조를 확인하고, 같은 클립 내에서 선행 클립 정서의 효과를 선행 클립 시각-의미 feature와 함께 추정한다. 이 단계가 HRF 잔여(정서와 무관)와 정서 내용 의존 이월을 가르는 가장 깨끗한 검정이다.
2. **정서 축의 정체 보증.** 축을 시각-의미 feature(V-JEPA 2, 인간 중립 캡션)를 회귀한 뒤의 규범 평정 공간에서 정의하고, 그 축으로 시각 내용이 decoding되지 않음을 확인한 뒤 washout에 투사한다.
3. **TRIBE v2 이월 기준선**(피질)을 넣어 "관찰 이월 - 자극 구동 예측 이월"을 1차 지표로 쓴다.
4. **식별 가능성 시뮬레이션을 τ 추정 전에.** 회복 가능한 τ 범위를 사전 등록한다.
5. **Emo-FilM 생리 처리.** RETROICOR류 생리 회귀를 한 판본과 안 한 판본에서 τ를 함께 보고하고, EDA 회복 τ와 비교한다. 생리 회귀로 τ가 사라지는 영역은 "자율신경 이완"으로 분류한다.

**종합:** 측정 설계가 정교하고 결과가 어느 쪽이든 의미가 있다. Mind captioning 순서 변이를 실제 조작으로 쓰면 결론 수준을 R0에서 R3-internal로 올릴 수 있다는 점을 가장 중요한 보완으로 제안한다. 유지를 권고한다.

---

## 3. FA-P6: 내부 표상 읽기 대 출력 묻기 (L2 층의 두 측정)

### 3.1 제안 요약
frontier-ai → llm-semantics. 같은 open VLM에서 (a) 정서를 묻고 답한 출력(Du 2025식 출력 기반 embedding)과 (b) 답하기 전 hidden state를 정서 vector에 투영한 값을 만들고, Mind captioning 인간 중립 캡션 embedding(L1)을 통제한 뒤 어느 쪽이 뇌 분산을 더 설명하는지, 어느 쪽이 "과도하게 범주적"인지(arXiv:2508.05880) 비교한다. 근거로 LLM에서 내부 probe가 zero-shot 출력보다 정서 정보가 많다는 보고(arXiv:2510.04064, 초록)를 든다. Axis U의 [AI-est]를 출력과 내부 표상으로 나누자고 제안한다. 원 맥락은 llm-semantics Round 1 0절의 세 층 분해(L1 기술 / L2 귀속 / L3 경험)와 Chain 1(기술 잔차), frontier-ai Round 1 U1(정서 대 상황), T8(뇌를 AI 정서 표상의 외부 타당도 기준으로).

### 3.2 판정

**(1) 이미 연구된 것은 아닌가? 판정: partially (구성 요소는 있음), 직접 비교는 no (이 검색 경로 안에서).**
* 출력 기반 embedding으로 Horikawa 뇌를 예측한 연구: Du 2025(arXiv:2509.24298)가 Qwen2-VL과 Llama-3.1의 triplet odd-one-out으로 만든 embedding이 인간 평정 embedding보다 정서 네트워크를 더 잘 예측한다고 보고했다.
* 내부 probe 대 prompting: LLM 내부 정서 기하가 zero-shot prompting보다 probe 성능이 높다는 보고(arXiv:2510.04064, 초록)가 있으나 뇌 비교는 없다. 모델 내부 정서 vector의 인과적 기능(arXiv:2604.07729), VLM 간 정서 개념 일반화(arXiv:2609.34742)도 뇌 비교는 없다.
* 같은 모델의 내부 probe 투영과 출력 평정을 fMRI 예측에서 직접 비교한 연구는 찾지 못했다(제안자의 MEG 포스터 언급은 search_index 수준이라 판단 보류).
* 검색 경로: arxiv.org/search "emotion probing fMRI language model hidden states"(0건), "emotion vector brain encoding"(5건, EEG 정서 인식 등 무관). WebSearch "vision-language model hidden state emotion probe versus verbal emotion ratings predicting fMRI brain responses comparison"(Du 2025만 해당, probe 비교 없음).

**(2) 단순한 모델 적용에 불과한가? 판정: 질문을 다시 짜지 않으면 그렇다.**
같은 모델의 두 판독을 encoding 성능으로 비교하는 것은 모델 측정 방법 비교에 가깝다. 신경과학적 질문으로 만들려면 두 판독을 이론적 대립에 대응시켜야 한다. 예: 내부 표상(보고 이전) 대 언어화된 판단(보고) = 정서의 1차 표상 대 보고 수준 표상(HOT, doi:10.1073/pnas.1619316114), 또는 암묵적 정서 판단 대 명시적 판단. 이 대응을 명시하면 "뇌의 정서 관련 분산은 보고 이전 표상과 보고된 판단 중 어느 쪽 구조에 가까운가"라는 질문이 된다.

**(3) 실제로 Neuroscience Question을 해결하는가? 판정: 위 재구성 시에만 부분적으로.**
재구성하지 않으면 결과는 주로 Axis U(라벨 출처)와 Axis R(모델 내부 정서 표상)에 대한 측정 정보다. 그것도 가치가 있다. AI 추정 라벨을 쓰는 모든 질문에 "어느 판독을 썼는가"가 결과를 바꾸는지 알려 주기 때문이다. 하지만 정서 경험의 신경 표상에 대한 새 지식은 재구성 후에만 나온다.

**(4) 정서 이외의 요소를 decoding하는 것은 아닌가? 판정: 두 판독 모두 위험이 크고, 위험의 종류가 다르다.**
* 내부 투영: hidden state는 장면 내용을 풍부하게 담고, 정서 vector와 일반 표상이 얽혀 있다. Xing 2026(arXiv:2609.34742)은 정서와 무관한 ImageNet activation으로 추정한 변환만으로 정서 vector 대응과 인과 전이가 복원된다고 보고했다. 즉 정서 방향은 일반 시각-의미 기하에 실려 있다. 투영값이 뇌를 잘 예측해도 내용 정보일 수 있다.
* 출력 판독: odd-one-out 판단은 비디오 전체를 보고 하므로 시각 유사도가 섞인다. adversarial-reviewer Round 1 0절은 Du 2025의 우세 영역에 고위 시각피질과 MST가 포함된다고 지적했다.
* 통제의 비대칭: L1 통제(인간 중립 캡션의 text embedding)는 VLM hidden state와 다른 모델, 다른 양식이다. 내부 판독은 같은 모델의 시각 내용과 함께 오므로 다른 모델의 캡션 embedding으로는 충분히 통제되지 않는다.

**(5) 현재 Dataset으로 검증할 수 있는가? 판정: 가능, 비용과 오염 점검이 조건.**
Horikawa 2020 + Mind captioning(같은 2,180 클립, 11명, 인간 중립 캡션, 72클립 반복 ceiling)은 적합하다(Mind captioning 보유 판본의 캡션 포함 여부는 미확인). 출력 기반 odd-one-out은 수백만 판단이 필요해(FA-P6 반론 (b)) 34범주 직접 평정 출력으로 대체하는 축소판이 현실적이다. Cowen & Keltner 비디오와 평정은 2017년부터 공개되어(llm-semantics Round 1 P5) open VLM 학습 데이터 오염 가능성이 있다. 오염은 출력 판독(평정 문자열 암기 가능)에 더 크게 작용할 수 있어 두 판독의 비교 자체를 편향시킨다.

**(6) 더 강력한 모델이나 분석 방법이 있는가? 판정: 있다.**
* **matched-complexity null.** 내부 투영과 같은 차원 수의 무작위 방향, 그리고 정서와 무관한 내용 방향(객체 범주, 장면 범주 probe) 투영을 같은 모델에서 만들어 기준선으로 둔다. 정서 투영이 이 기준선을 넘는 분산만 "정서 판독의 기여"로 인정한다. 같은 모델 안에서 통제하므로 (4)의 통제 비대칭을 줄인다.
* **판독이 모델 안에서 쓰이는지 확인(R1-m).** 정서 방향을 steering했을 때 출력 평정이 그 방향으로 바뀌는지 본다(arXiv:2604.07729, arXiv:2310.01405 방식). 읽히기만 하고 출력에 쓰이지 않는 방향이면 "내부 표상 대 출력" 비교의 의미가 달라진다(읽힘과 쓰임의 구분, arXiv:2106.02997).
* **counterfactual 자극으로 판독의 정체 판별.** 의미 고정 정서 편집(분위기만 바꾼 편집, 표정만 바꾼 편집)과 정서 고정 의미 편집에 대해 두 판독이 각각 어떻게 반응하는지 본다. 의미 편집에만 반응하는 판독은 의미 대리물이다. 이것은 자연 자극의 공선성 없이 판독의 성격을 판정하는 검정이며, 뇌 데이터가 필요 없는 R1-m 사전 검사로 쓸 수 있다.
* **뇌 비교 지표.** Mind captioning 반복 ceiling으로 정규화하고, 분산 분할에서 공유 분산을 함께 보고하며, 항목 수준 대응은 GW 정렬로 본다(llm-semantics I3 방식).

**(7) 결과가 기대와 다를 때도 과학적으로 유의미한가? 판정: 예.**
내부 > 출력이면 보고 이전 정서 정보가 뇌 구조에 더 가깝다는 근거(단 내용 기준선을 넘을 때만), 출력 > 내부면 규범 평정이 걸린 뇌 분산이 언어화된 평균 관찰자 판단과 더 맞는다는 근거, 둘이 같으면 판독 방식이 결론에 영향이 없다는 실용적 결과, 둘 다 캡션 기준선과 같으면 기술 의미를 넘는 정서 정보가 이 모델 판독에 없다는 결과다. 어느 결과든 Axis U에서 [AI-est]를 판독 방식별로 나눌지 결정하는 근거가 된다.

### 3.3 결론 수준 점검
* 제안자 표기는 R0. 뇌 비교는 R0가 맞다. steering 단계를 넣으면 그 부분은 R1-m(모델에 관한 인과)이며 뇌에 관한 인과가 아니다.
* label-provenance: 두 판독 모두 [AI-est]. 비교 대상 뇌 분산에 걸린 라벨은 felt 보고, 별도 평정자 규범. 제안자의 [AI-est, 출력] / [AI-est, 내부 표상] 분리에 동의하며, steering을 거친 판독은 [AI-est, 내부 표상, 개입 검증]으로 따로 표기하자고 제안한다.
* insilico-vs-observed: 관찰(모델 판독은 회귀자).

### 3.4 수정안
1. **질문 재구성.** "뇌의 정서 관련 분산은 보고 이전 표상(내부)과 보고된 판단(출력) 중 어느 쪽 구조에 가까운가"로 쓰고, HOT의 1차 대 고차 구분에 대응시킨다. 단 모델의 두 판독이 인간의 두 수준과 같은 것이라는 주장은 하지 않고 비유로만 둔다.
2. **같은 모델 안의 matched-complexity null**(무작위 방향, 내용 방향)을 1차 기준선으로 둔다. 인간 중립 캡션 embedding 통제는 2차 기준선으로 유지한다.
3. **R1-m 사전 검사 두 개.** (a) steering으로 판독의 쓰임 확인, (b) 의미 고정 편집과 의미 편집에 대한 두 판독의 반응 비교. 의미 편집에만 반응하는 판독은 뇌 비교에서 "의미 대리물"로 표기한다.
4. **오염 점검.** 출력 판독이 Cowen & Keltner 평정을 암기했는지 클립 변형(좌우 반전, 자르기, 프레임 순서)에 대한 출력 안정성과 원 평정 일치도의 비정상적 상승으로 점검한다. 내부 판독도 같은 변형에서 비교한다.
5. **비용 축소.** odd-one-out 대신 34범주 직접 평정 출력으로 출력 판독을 만들고, Du 2025 결과는 다른 모델이므로 기준선으로 재사용하지 않는다.

**종합:** Axis U와 R에 실용적 가치가 분명하다. 신경과학 질문으로서의 가치는 1번 재구성과 2, 3번 기준선에 달려 있다. 수정 후 유지를 권고한다.

---

## 4. 세 제안 요약 판정

| 제안 | 이미 연구 | 단순 적용 | 신경과학 질문 | 비정서 decoding 위험 | 현재 데이터 | 더 강한 방법 | 의외 결과의 의미 | 결론 수준 | 권고 |
|---|---|---|---|---|---|---|---|---|---|
| BI-P2 | partially | 부분적(latent action band) | 질문은 중요, 설계는 부분적 | 큼(행위 의미, 화면 운동) | Emo-FilM 가능, Horikawa 조건부 | 신뢰도 보정 분할, counterfactual affordance 편집, 일반화 기준 | 조건부(분리 불가 결과 사전 정의 필요) | R0 ("대체" 표현 수정) | 수정 후 유지 |
| MD-P1 | partially | 아니다 | 예(축 정체 보증 전제) | 큼(적응, 자율신경) | 가능(raw 재전처리 필수) | Mind captioning 순서 무작위화, TRIBE 이월 기준선, 식별 가능성 시뮬레이션 | 예 | R0, Mind captioning 선행 효과는 R3-internal 가능 | 유지(보완 권고) |
| FA-P6 | partially / 직접 비교 no | 재구성 없으면 그렇다 | 재구성 시 부분적 | 큼(내용, 시각 유사도) | 가능(비용, 오염 점검 조건) | 같은 모델 null, steering, counterfactual 판독 판별 | 예 | R0 (+ R1-m) | 수정 후 유지 |
