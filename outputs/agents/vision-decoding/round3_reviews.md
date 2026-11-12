# Round 3 (Constructive Disagreement): vision-decoding의 검토

* 검토자: vision-decoding (brain-ml 분야)
* 기준일: 2026-11-12
* 절차: `reference/protocols.md` P3. 배정: `outputs/discussion/round3_assignment.md`
* 배정 제안: **GI-P1**(geometry-info → emotion-theory), **SN-P1**(systems-neuro → encoding-foundation), **FA-P6**(frontier-ai → llm-semantics)
* 읽은 원문: 각 제안의 round2.md 해당 절, 그 근거 chain(geometry-info round1 C1과 round2 0.2절, A1~A6; systems-neuro round1 Chain 1, Chain 2와 encoding-foundation round1 Chain 2; llm-semantics round1 0절, Chain 1과 frontier-ai round2 4절), `literature_db.csv`의 관련 항목
* 표기: [본문] 직접 확인, [초록], [DB](다른 에이전트가 verified로 기록한 항목을 그 기록에 기대어 인용), [미러](OpenNeuro GitHub 미러의 events.tsv 등을 직접 읽음). label-provenance와 evidence-level은 axis_encyclopedia 0.2절 형식.

---

## 0. 검토 전에 직접 확인한 데이터 사실

GI-P1과 SN-P1의 전제를 확인하려고 두 코호트의 공개 메타데이터를 직접 읽었다. MC 미러(ds005191)는 git 메타데이터만 shallow clone했고, Horikawa 미러(ds002425)는 Stage 1에서 받은 사본이다. 아무것도 실행하지 않고 텍스트만 읽었다.

| 사실 | 값 | 영향 |
|---|---|---|
| 코호트 간 제시 순서 | Horikawa 2020은 5명 모두 같은 순서(2,196블록). MC는 4명이 같은 순서이고 sub-04, sub-06은 일부 run 순서만 다르다(학습 순서 Spearman 0.996, 0.9997). **두 코호트 순서의 상관은 Spearman -0.03**(같은 비디오 파일 번호 1~2,196 기준) | GI-P1의 "코호트 간 쌍은 순서 효과를 공유하지 않는다"는 전제가 사실로 확인된다. geometry-info는 이를 "미확인"으로 두었다 |
| 72 테스트 클립의 위치 | MC 학습 순서의 2,108~2,179번째(마지막 72블록). Horikawa에서는 흩어져 있다 | 72클립 기반 분석에서는 두 코호트의 노출 시점 교란이 다르다 |
| 72 테스트 클립 노출 횟수 | 학습 1회 + 테스트 5회 + 회상 세션의 회상 직후 재제시 5회 = 최대 11회 | GI-P1의 "72개 x 6회"는 회상 세션 노출을 빠뜨렸다 |
| 시청 방식 | MC 지각은 "fixation 없이" 자유 시청(논문 Methods), 회상은 눈 감음. Horikawa 2020의 시청 지시는 미확인 | 개인별 시선 패턴이 "신뢰할 수 있는 개인 고유 분산"을 만들 수 있다 |
| 회상 평정 | events.tsv에 시행별 vividness, accuracy가 있다. 분포가 3~4점에 몰려 있다 | GI-P1과는 무관, ET-P6 응답에 반영(round2.md 3.0) |
| MC 라이선스 | CC0(`dataset_description.json`) | 재분석 제약 없음 |

---

## 1. GI-P1: 두 코호트 교차 공유 스펙트럼으로 Horikawa 범주 결론과 Westlin 재현 실패를 판정

**제안 요약.** Horikawa 2020 5명과 MC 6명(같은 2,180클립)의 피험자 쌍 55개를 쓴다. 코호트 내 쌍과 코호트 간 쌍의 rank별 공유 스펙트럼을 비교하고, MC 72클립 반복으로 피험자 내 신뢰 스펙트럼을 구해 "재현 가능한 개인 고유 분산"을 분리한다. 공유 차원을 규범 평정, 정서 배제 캡션, 시각 feature로 대역별 분할하고, 군집 multiverse를 세 입력 경로로 돌린다. 근거 chain은 geometry-info round1 C1이고, emotion-theory C1/C2, systems-neuro Chain 2, adversarial-reviewer D1과 수렴했다.

### 판정

| 항목 | 판정 | 근거 |
|---|---|---|
| 1. 이미 연구되었는가 | **partially** | 방법은 시각(NSD, THINGS)에서 cross-decomposition으로 수행되었고(arXiv:2409.06843 [DB]), 영화 시청의 rank별 개인차도 보고되었다(arXiv:2505.12653 [DB], 시각 경험). 정서 영역에서는 occipital hyperalignment 후 affect decoding(Chan et al. 2020, doi:10.1016/j.neuroimage.2020.116618 [DB, Crossref 서지 확인])과 정서 영화의 dynamic hyperalignment-HMM(doi:10.1007/s12021-022-09568-5 [geometry-info 초록])이 있다. **정서 반응에 rank별 공유 스펙트럼을 적용하거나, 같은 자극을 본 두 코호트로 순서와 프로토콜 공유 분산을 분리한 연구는 찾지 못했다.** 검색 경로는 3절 |
| 2. 단순한 모델 적용인가 | **아니다(조건부)** | 방법 이전이지만 판정 논리(코호트 간 vs 코호트 내, 피험자 내 반복 vs 피험자 간)가 Westlin의 session NMI 문제를 정량화한다. 다만 "범주 결론 판정"이라는 이름에 비해 공유 스펙트럼은 범주와 연속의 구분을 직접 검정하지 않는다(6번 참조) |
| 3. Neuroscience Question을 해결하는가 | **부분적으로** | "정서 반응 분산 중 개인 간 공유와 개인 고유는 어느 rank에 있는가", "Westlin의 개인 특이성은 재현 가능한 구조인가 세션 잡음인가"에는 직접 답한다. "정서 표상이 범주적인가"에는 4단계 군집 multiverse만 답하는데, 그 단계는 Westlin과 같은 고분산 군집 문제를 그대로 안는다 |
| 4. 정서가 아닌 visual/semantic을 decoding하는가 | **위험이 크다** | 같은 비디오를 본 사람들 사이의 공유 분산은 대부분 자극 구동 시각, 의미 성분이다. 정서 고유 대역을 주장하려면 분할이 필요한데, 규범 평정과 캡션 embedding 모두 측정 오차가 있어 증분 타당도 위양성이 생긴다(doi:10.1371/journal.pone.0152719 [DB]). 개인 고유 쪽도 문제다. **MC는 자유 시청이므로 개인별 시선 패턴이 반복 간에 일관된 개인 고유 시각 반응을 만든다.** 이 성분은 "재현 가능한 개인 고유 분산"으로 잡히지만 정서가 아니다. 눈 추적 자료가 없다 |
| 5. 현재 Dataset으로 검증 가능한가 | **가능, 단 전처리 통일이 전제** | 두 코호트 raw가 모두 공개 CC0다(0절). MC 전처리본은 GM 전역 신호를 회귀했고 Horikawa 공개 전처리본의 전역 처리는 미확인이다(geometry-info 0.2절). raw에서 같은 파이프라인으로 다시 처리해야 한다. 72클립 반복 스펙트럼의 상한은 약 71 rank다. 피험자 중복 여부는 여전히 미확인이다 |
| 6. 더 강력한 방법이 있는가 | **있다** | (a) 범주 대 연속 판정에는 공유 부분공간 안의 교차검증 모형 비교가 더 직접적이다. 혼합 모형(이산 군집)과 연속 잠재 모형(확률적 PCA, 요인 모형)의 held-out 우도를 비교한다. (b) 개인 고유 성분의 시선 교란에는 saliency, 시선 예측 모형(axis_encyclopedia Axis N 모델 목록에 이름이 오른 DeepGaze 계열 등. 논문은 이번에 검증하지 않았다)의 예측을 공변량으로 넣는다. 초기 시각피질의 개인 고유 비율을 기준 대조로 둔다. (c) 측정 오차를 반영한 분할(feature 신뢰도 민감도 곡선)과 controversial subset(정서와 시각-의미 예측이 갈리는 클립을 뇌 데이터 없이 선택, doi:10.1073/pnas.1912334117 [DB]) |
| 7. 결과가 기대와 달라도 유의미한가 | **그렇다** | 코호트 간 공유가 거의 사라지면 공유 정서 기하의 상당 부분이 프로토콜 특이적이라는 뜻이다. 반복 신뢰 개인 고유 분산이 없으면 Westlin의 개인 특이성은 잡음 쪽으로 기운다. 정서 고유 대역이 분할 후 남지 않으면 "고차원 정서 표상"은 시각-의미 공유로 환원된다. 모두 해석 가능하다 |

**종합:** 수정 후 진행 권고. 주제의 중요성과 데이터 적합성은 높다. 그러나 "개인 고유 = 정서적 개인차"로 가는 해석에 시선 교란이, "공유 정서 대역"에 측정 오차 위양성이 끼어든다.

### 수정안
1. **순서 사실을 반영한다.** 코호트 간 순서 독립성은 이제 확인된 사실이다(0절). 추가로 MC 안에서 run 순서가 일부 다른 sub-04, sub-06을 "코호트 내 순서 불일치 쌍"으로 따로 표시하면, 순서 효과의 작은 내부 검정이 하나 더 생긴다.
2. **노출 이력을 정확히 쓴다.** 72클립은 최대 11회 노출되었다. 피험자 내 신뢰 스펙트럼은 테스트 5회로만 계산하고, 학습 세션의 첫 노출과 회상 세션 재제시는 반복 적응 공변량으로 둔다. 72클립은 MC에서 학습 순서 끝에 몰려 있으므로, Horikawa의 같은 72클립(흩어진 위치)과 비교해 시점 교란을 따로 추정한다.
3. **시선 교란 대조를 넣는다.** 시선 예측 모형의 출력(클립별 예측 시선 분포와 그 엔트로피)을 공변량으로 둔다. 영역별로 "재현 가능한 개인 고유 분산"의 비율을 V1~V3, 고차 시각, transmodal에서 비교한다. 개인 고유 비율이 초기 시각피질에서 가장 크고 transmodal로 갈수록 줄면 시선 기원 해석이 유력하다. 그 반대라면 시선만으로는 설명하기 어렵다.
4. **범주 판정 단계를 명시적 모형 비교로 바꾼다.** 4단계 군집 multiverse에 더해, 공유 부분공간(코호트 간 공유 상위 rank)과 개인 고유 부분공간에서 각각 혼합 모형 대 연속 잠재 모형의 held-out 우도를 비교한다. geometry-info A1의 밀도 균등화 재표집 부분집합에서도 반복한다. 이렇게 해야 "범주 결론"에 대한 판정이 된다.
5. **측정 오차를 반영한 분할.** 규범 평정(비디오당 평정자 9~17명), 캡션 embedding(캡션 20개의 split-half), 시각 feature 각각의 신뢰도를 추정하고, 정서 고유 공유 분산이 신뢰도 가정에 얼마나 민감한지 곡선으로 보고한다.
6. **유병률 보고.** 11명(또는 중복 확인 후 남는 수)에서 피험자별로 검정하고 Bayesian prevalence로 요약한다(geometry-info A6과 일치).
* 수정 후 표기: label-provenance = 스펙트럼은 라벨 비의존, 해석 라벨은 felt / 별도 평정자 규범, 캡션은 기술 의미 / 별도 평정자(정서 배제 지시). evidence-level = R0. G1 = 핵심 분석 불필요, 시각 feature와 시선 예측에는 필요(보유).

---

## 2. SN-P1: 생리 반영 noise ceiling과 전역 자율신경 성분으로 limbic 맹점 분해

**제안 요약.** Emo-FilM에서 raw BOLD와 생리 회귀 BOLD로 ISC ceiling을 각각 구해 차이를 "자극 구동 생리 성분"으로 보고한다. 생리의 역할을 (a) 잡음 회귀, (b) 전신 상태 예측자(지연 반응함수), (c) 둘을 뺀 신경 분산으로 나눈다. 제공 전처리본(WM/CSF 회귀)은 쓰지 않고, 영역별 dropout과 tSFNR을 함께 보고한다. 근거 chain은 encoding-foundation Chain 2(limbic 맹점: 잡음인가, 몸인가, 평가인가)와 systems-neuro Chain 1이다.

### 판정

| 항목 | 판정 | 근거 |
|---|---|---|
| 1. 이미 연구되었는가 | **partially** | 전제는 선행이 있다. 공통 자극에 심박과 시선이 피험자 간 동기화되고(doi:10.1093/pnasnexus/pgac020 [초록]), ISC 지침은 정서 자극에서 말초 생리가 동기화되어 ISC를 부풀릴 수 있다고 적었다(doi:10.1093/scan/nsz037 [DB]). 전역 fMRI 신호가 교감 각성과 결합한다(doi:10.1038/s41593-025-01945-y [DB]). **정서 영화 fMRI에서 ISC ceiling을 생리 성분으로 분해해 limbic encoding 성능을 재정규화한 연구는 찾지 못했다.** 검색 경로는 3절 |
| 2. 단순한 모델 적용인가 | **아니다** | 측정 타당도 절차다. 다만 그 자체로는 전처리 비교라서, 결과를 limbic 맹점의 세 설명(잡음, 몸, 평가) 중 하나로 연결하는 사전 해석표가 있어야 과학적 질문이 된다 |
| 3. Neuroscience Question을 해결하는가 | **부분적으로, 핵심 함정이 있다** | 생리 반응은 정서 반응의 일부이고, 같은 평가(appraisal)가 일으키는 결과일 수 있다. 그러면 생리는 교란 변수가 아니라 매개 변수다. 생리를 회귀하면 "몸"뿐 아니라 "평가가 몸을 통해 만든 신경 신호"까지 지울 수 있어, "몸인가 평가인가"를 이 설계만으로 가르지 못한다. 제안의 "과잉 보정" 반론 대응(전후 모두 보고)은 해석 기준이 아니라 보고 방식이다 |
| 4. 정서가 아닌 visual/semantic을 다루는가 | **다른 방향의 위험** | vision 쪽에서 보면, 피험자 간에 동기화된 생리와 BOLD는 정서가 아니라 **저수준 시청각 자극**(장면 밝기 변화, 움직임 에너지, 음량)으로도 함께 구동된다. 밝기와 움직임은 시각피질과 전역 신호를, 음량은 놀람 반응과 심박을 동시에 움직인다. Madsen & Parra는 동기화가 주의 관여의 산물이라고 보았다(doi:10.1093/pnasnexus/pgac020 [초록]). 따라서 "자극 구동 생리 성분 = 정서 성분"으로 읽으면 안 된다. 또 생리를 뺀 뒤 limbic 영역에 남는 "신경" 분산도 얼굴, 사람 같은 의미 범주 구동일 수 있다(amygdala의 얼굴 선호, arXiv:2512.00557 [DB]) |
| 5. 현재 Dataset으로 검증 가능한가 | **Emo-FilM에서만 완전히 가능** | Emo-FilM은 참가자 PPG, 호흡, EDA를 1000 Hz로 공개한 유일한 데이터다(Stage 1). raw 재전처리가 필요하다(계산 부담 큼). 30명, 영화 14편이라 leave-one-film-out이다. MC와 Horikawa에는 생리가 없어 반복 기반 ceiling 비교만 가능하다. 평정은 별도 평정자, 생리는 참가자라 주체가 다르다 |
| 6. 더 강력한 방법이 있는가 | **있다** | (a) 생리 회귀 여부의 이분법보다 **인과 그래프에 따른 추정량 명시**가 낫다. "자극 → 저수준 feature → 생리 → BOLD", "자극 → 평가 → 생리 → BOLD", "자극 → 평가 → BOLD"를 구분하고, 총효과와 생리 경로를 뺀 효과를 각각 정의한 뒤 둘을 다 보고한다(generative-counterfactual의 rater-structure causal graph와 같은 틀). (b) 생리 ISC를 BOLD ISC에서 부분화하는 partial ISC로 "생리로 설명되지 않는 공유 신경 반응"을 직접 정의한다. (c) MC의 반복 기반 ceiling(생리 없음)과 피험자 간 ISC ceiling을 같은 클립에서 비교해, ISC 기반 ceiling이 무엇을 과대, 과소 추정하는지 보정 관계를 만든다(emotion-theory ET-P1 (a)와 같은 아이디어) |
| 7. 결과가 기대와 달라도 유의미한가 | **그렇다, 단 해석표가 사전에 있어야 한다** | ceiling이 거의 안 바뀌면 limbic 맹점은 생리 때문이 아니다. 크게 바뀌면 기존 limbic encoding 주장의 일부가 몸 신호 주장이었다는 뜻이다. 다만 3번의 매개 문제 때문에 "크게 바뀜"이 "정서가 몸이다"와 "생리 잡음이 컸다" 중 어느 쪽인지는 저수준 feature 분할과 Bolt 2025의 혈관성 시공간 표지(WM/CSF 반대 부호, 지연 구조)로만 갈린다 |

**종합:** 수정 후 진행 권고. 측정 쪽 기여는 크다. 다만 생리를 교란으로 두는 기본 가정과 저수준 시청각 동기화 누락을 고쳐야 "잡음인가, 몸인가, 평가인가"에 답하는 설계가 된다.

### 수정안
1. **4원 분할로 바꾼다.** 설명 변수를 (i) 저수준 시청각 feature(프레임 밝기, 움직임 에너지, 음량 RMS, 장면 전환), (ii) 자극 구동 고수준 feature(TRIBE v2 예측 또는 그 백본), (iii) 참가자 생리(지연 반응함수), (iv) 규범 평가(Emo-FilM Appraisal, Feeling 항목)로 두고, 영역별 고유 분산과 공통 분산을 보고한다. (i)이 생리 ISC와 BOLD ISC의 공통 원인인 정도를 먼저 정량화한다.
2. **추정량을 미리 정한다.** 인과 그래프를 사전 등록하고 "총 설명력"과 "생리 경로를 제외한 설명력"을 각각 정의한다. limbic 맹점의 판정은 두 추정량의 차이 패턴으로 한다. 예를 들어 총효과와 제외 효과가 모두 낮으면 잡음 또는 해상도, 총효과만 높으면 몸 경로, 둘 다 높으면 평가 경로를 지지한다.
3. **혈관성 성분의 독립 표지.** Bolt 2025의 시공간 패턴(WM/CSF와 회백질의 반대 부호, 생리 순서 지연)을 템플릿으로 혈관성 전역 성분을 표지하고, 신경성 생리 결합과 따로 다룬다(제안의 반론 대응을 해석 단계로 격상).
4. **MC로 ceiling 보정.** MC 72클립에서 반복 기반 ceiling과 피험자 간 ISC ceiling을 같은 영역에서 비교해 보정 관계를 만들고, Emo-FilM ISC ceiling 해석에 쓴다. 단 72클립의 노출 이력(최대 11회)과 블록 내 반복 재생을 공변량으로 둔다(0절).
5. **signal-feasibility 관문은 그대로 유지한다.** 영역별 dropout과 tSFNR을 결과 옆에 두고, amygdala 소핵 수준 주장은 하지 않는다.
* 수정 후 표기: label-provenance = 평가 항목은 felt / 별도 평정자 규범, 생리는 참가자 본인 측정(라벨 아님). evidence-level = R0. insilico-vs-observed = 관찰, TRIBE 분할 포함 시 혼합. signal-feasibility = 필수.

---

## 3. FA-P6: 내부 표상 읽기 vs 출력 묻기 (L2 층의 두 측정)

**제안 요약.** 같은 open VLM에서 (a) 정서를 묻고 받은 출력 기반 embedding(Du 2025식)과 (b) 답하기 전 hidden state를 정서 vector에 투영한 값을 만든다. MC 인간 중립 캡션(L1)을 통제한 뒤 어느 쪽이 뇌 분산을 더 설명하는지, 어느 쪽이 더 범주적인지 비교한다. label-provenance의 "AI 추정"을 출력(verbalized)과 내부 표상(probe)으로 나누자고 제안한다. 근거는 llm-semantics Chain 1과 L1/L2/L3 분해, frontier-ai의 모델 내부 정서 표상 문헌이다.

### 판정

| 항목 | 판정 | 근거 |
|---|---|---|
| 1. 이미 연구되었는가 | **partially** | 출력 기반 MLLM embedding이 Horikawa 뇌를 인간 평정 embedding보다 잘 예측한다는 결과가 있다(arXiv:2509.24298 [DB]). LLM에서는 내부 probe가 zero-shot prompting보다 정서 정보가 많다(arXiv:2510.04064 [frontier-ai, 초록]), LLM 출력은 인간보다 범주적이다(arXiv:2508.05880 [DB]). 언어-뇌 연구에서 hidden state를 회귀자로 쓰는 것 자체는 표준이다(예: doi:10.1038/s42256-025-01072-0 [DB, 본문]). **같은 모델의 정서 내부 표상과 정서 출력을 fMRI 설명력으로 직접 비교한 연구는 찾지 못했다**(frontier-ai의 검색과 내 검색 일치, 3절) |
| 2. 단순한 모델 적용인가 | **위험이 있다** | 이대로면 두 feature 집합의 encoding 점수 비교, 즉 벤치마크에 가깝다. "뇌의 정서 기하가 모델의 언어화 이전 상태에 가까운가, 언어화된 보고에 가까운가"라는 가설로 묶어야 과학적 질문이 된다. 이 가설은 인간의 경험과 보고의 구분(Axis A Introspective Access)과 범주 대 연속 논쟁에 연결된다 |
| 3. Neuroscience Question을 해결하는가 | **간접적으로** | 결과는 모델과 뇌의 유사도(L2, 관찰자 관점)에 관한 것이다(arXiv:2408.13718 [DB]). 인간 경험이나 보고 과정에 대한 직접 증거는 아니다. "뇌 정서 기하가 언어화로 범주화된 구조인가"에 대한 약한 증거는 된다 |
| 4. 정서가 아닌 visual/semantic을 decoding하는가 | **위험이 크다** | 비디오를 처리한 VLM hidden state에는 시각 세부와 장면 의미가 가득하다. 정서 vector에 투영해도 그 vector가 정서와 상관된 의미 방향을 실을 수 있다. 정서 vector가 합성 텍스트 이야기로 추출되었다면(arXiv:2604.07729 [DB]의 방식) 비디오 token에서 같은 방향이 같은 뜻인지도 보장되지 않는다. L1 캡션 통제는 언어화된 의미만 빼고 캡션에 안 담긴 시각 정보는 남긴다. 출력 쪽도 같은 문제가 있다. Du 2025는 비정서 프롬프트 대조가 없었다(adversarial-reviewer 기록 [DB]) |
| 5. 현재 Dataset으로 검증 가능한가 | **가능** | Horikawa와 MC 비디오를 보유했고, MC는 CC0이며 72클립 반복 ceiling과 회상 조건이 있다. open VLM(Qwen 계열 등)의 hidden state 추출은 2,180클립 규모에서 현실적이다. triplet odd-one-out 수백만 건은 비싸므로 출력은 34차원 직접 평정으로 바꾸는 것이 현실적이다. 사전학습 오염(C&K GIF가 웹에 공개됨)은 점검할 수 없고 누출 탐침으로만 다룬다 |
| 6. 더 강력한 방법이 있는가 | **있다** | (a) **같은 forward pass에서 읽고 묻기.** 정서를 묻는 프롬프트의 마지막 입력 token에서 hidden state를 읽고 이어서 생성 출력을 받으면, "읽기 vs 묻기"가 같은 입력, 같은 계산에서 비교된다. (b) **차원과 신뢰도 정합.** 출력 34차원 평정과 내부 표상의 34개 정서 방향 투영을 맞추고, 출력은 여러 번 표집해 신뢰도를 재서 내부 표상(결정적)과의 신뢰도 비대칭을 보정한다. (c) **matched-complexity null.** 무작위 방향, 비정서 개념 방향(물체, 장면 범주)에 같은 차원으로 투영한 값을 기준선으로 둔다. (d) **decoding 방향과 일반화 검정.** 뇌 → 모델 공간 사상의 교차검증 정확도를 MC 반복 ceiling으로 정규화하고, 지각에서 학습한 사상이 MC 회상 imagery로 일반화되는지 본다. 자극 없는 조건에서 어느 표상이 더 잘 버티는지는 encoding 점수와 다른 정보를 준다 |
| 7. 결과가 기대와 달라도 유의미한가 | **그렇다, 단 결론 범위는 모델-뇌 유사도** | 출력이 이기면 뇌 정서 기하가 범주화된 보고 구조에 가깝다는 뜻이다. 내부 표상이 이기면 언어화 이전의 연속 구조에 가깝다는 뜻이다. 둘 다 L1 통제 후 0이면 뇌의 "정서" 분산이 언어화된 장면 의미로 환원된다는 뜻이다(llm-semantics Chain 1과 같은 결론). 어느 쪽이든 Axis U의 AI 추정 라벨 하위 구분(출력 vs 내부)의 필요성에 대한 근거가 된다 |

**종합:** 수정 후 진행 권고. Axis U의 AI 추정 라벨을 출력과 내부 표상으로 나누자는 제안에는 동의한다. 다만 비교가 벤치마크로 끝나지 않으려면 가설을 정하고, 차원, 신뢰도, 시각 내용 통제를 맞춰야 한다.

### 수정안
1. **가설을 먼저 고정한다.** "뇌 정서 기하는 언어화 이전 표상에 가깝다(H-pre)" 대 "범주화된 보고에 가깝다(H-verb)". H-verb는 출력 우위와 함께 범주성 지표(뇌 RDM의 군집도, arXiv:2508.05880의 범주성 측정)에서도 출력과 뇌가 가깝다고 예측한다.
2. **같은 forward pass에서 읽고 묻는다.** 정서 질문 프롬프트의 마지막 입력 token hidden state(내부)와 그 직후 생성 평정(출력)을 같은 입력에서 얻는다. 정서 방향은 C&K 자극과 겹치지 않는 텍스트, 이미지 대비 쌍으로 추출하고, 비디오 입력에서 방향의 의미가 유지되는지 소규모 인간 평정으로 점검한다(R2).
3. **차원, 신뢰도, 복잡도를 맞춘다.** 34차원 대 34방향으로 맞추고, 출력은 반복 표집 평균과 그 신뢰도를 보고한다. 무작위 방향과 비정서 개념 방향 투영을 null로 둔다.
4. **시각 내용 통제를 두 겹으로 한다.** L1 인간 중립 캡션 embedding과 함께 시각 전용 모델 feature(V-JEPA 2 또는 CLIP image)를 통제하고, 비정서 질문("장면에 몇 명이 있는가")의 hidden state와 출력도 대조 조건으로 둔다(adversarial-reviewer I5의 prompt ablation과 같은 논리).
5. **ceiling과 회상 일반화.** MC 72클립 반복으로 ceiling을 정규화하고, 지각에서 학습한 사상을 MC 회상에 적용해 두 표상의 일반화를 비교한다. 회상 cue 캡션은 별도 회귀자로 둔다(round2.md LS-P1 응답).
6. **표기.** 제안대로 label-provenance를 [AI 추정, 출력]과 [AI 추정, 내부 표상]으로 나누고, 둘 다 perceived(관찰자 관점)임을 명시한다.
* 수정 후 표기: evidence-level = R0(뇌 비교), 정서 방향 추출과 투영은 R1 성격의 모델 쪽 조작. insilico-vs-observed = 관찰. G1 = 필요(보유).

---

## 4. 검색 경로 (2026-11-12)

| 제안 | 검색 | 결과 |
|---|---|---|
| GI-P1 | PubMed `(hyperalignment OR "shared response model" OR cross-decomposition OR "shared variance") AND (emotion* OR affective) AND (dimensionality OR spectrum OR "individual differences") AND fMRI` (2018~): 1건, 공포 습득 개인차 연구(doi:10.1038/s41598-020-72007-5)로 무관. WebSearch "shared dimensionality across individuals emotion fMRI cross-decomposition hyperalignment idiosyncratic reliable variance repeated movie clips": Chan 2020(doi:10.1016/j.neuroimage.2020.116618, Crossref 서지 확인), INT 모형, Haxby 2020 | 정서에 rank별 공유 스펙트럼, 두 코호트 설계 적용은 미발견 → partially |
| SN-P1 | PubMed `(physiological noise OR RETROICOR OR cardiac OR respiration) AND (intersubject correlation OR noise ceiling) AND (movie OR film OR naturalistic) AND fMRI` (2015~): 0건. WebSearch "intersubject correlation fMRI emotional movie physiological noise heart rate respiration correction noise ceiling amygdala encoding": ISC 지침, 영화 fMRI의 생리 잡음 제거(DRIFTER), 정서 영화 ISC 초기 연구. Crossref로 Madsen & Parra 2022와 Nastase 2019 서지 확인 | 전제(생리 동기화)는 선행, ceiling 분해는 미발견 → partially |
| FA-P6 | WebSearch "vision language model hidden state probing versus generated verbal ratings predict fMRI brain responses emotion comparison internal representation output": Du 2025(출력 기반)만 해당, 내부 표상과 비교하지 않음. frontier-ai의 별도 검색(MEG 포스터, search_index)은 서지 미확인 | fMRI 기준 미발견 → partially(구성 요소는 선행) |

arXiv API는 이번 라운드에도 rate limit(429)이 걸려 쓰지 못했다(우회하지 않음).

---

## 5. 검증과 미확인

* 검증: 0절의 데이터 사실(공개 미러 텍스트 직접 읽음), 이 문서에 인용한 ID는 `literature_db.csv` 또는 내 `literature.jsonl`의 verified 항목(이번 라운드에 Bone 2020, St-Laurent 2015, Madsen & Parra 2022를 추가)이거나 다른 에이전트 jsonl의 verified 항목(arXiv:2510.04064, frontier-ai), Crossref로 서지를 확인한 항목(Chan 2020).
* 미확인: Horikawa 2020의 시청 지시(fixation 여부), 두 코호트 피험자 중복, MC 회상 cue로 쓰인 캡션 번호(events.tsv에 없음), 사용자 보유 MC 전처리본의 형태, 시선 예측 모형(DeepGaze 계열 등)의 서지와 비디오에서의 정확도.
