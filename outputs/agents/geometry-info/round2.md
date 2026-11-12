# Round 2 (Cross-Agent Exchange): geometry-info

* 작성: geometry-info (Agent 7, Axis K, O 담당) / 기준일 2026-11-12 / 절차: `reference/protocols.md` P2 / 제안 ID 접두어 GI
* 읽은 것: 다른 10개 에이전트의 `round1.md`(0, 1, 3, 4, 6절 전체와 필요한 5절), `outputs/axis_encyclopedia.md`(0절, 1절 K/Q/R/T, 2절), `outputs/STAGE_STATUS.md` 사용자 결정 기록(2026-11-12 두 차례), `outputs/literature/literature_db.csv`(필요한 ID만 조회)
* 새로 확인한 원문: Horikawa et al. (2025) Mind captioning(doi:10.1126/sciadv.adw1464) Materials and Methods를 PMC12588295 전문으로 직접 읽었다. Thornton, Weaverdyck, Tamir (2019), Tan et al. (2022), Baez-Lugo et al. (2023), Lynn et al. (2021), Kringelbach et al. (2023), Chikazoe et al. (2014)는 PubMed 초록을 읽었다.
* 문헌 갱신: `literature.jsonl`에 6편을 추가하고(총 51편, 5편 Crossref, 1편 arxiv.org 초록 페이지로 확인) Gauthaman 2024의 출판본(PLOS Comput Biol 21:e1013714, doi:10.1371/journal.pcbi.1013714, Crossref 확인)을 기존 항목에 적었다.
* 표기: [본문], [초록], [판단], [DB](다른 에이전트가 literature_db.csv에 verified로 올린 항목을 그 기록에 기대어 인용, 본 에이전트는 원문 미열람). label-provenance는 "대상 / 주체", evidence-level은 R0~R4(Deliverable B 0.2절).

---

## 0. Round 1 판정 수정과 새 전제의 영향

### 0.1 already_done 재검색 결과 (Stage 2 교훈 반영)

Coordinator가 지적한 "no 판정의 25% 과대" 위험에 따라, Round 2 제안에 쓰는 내 Round 1 chain의 판정을 다시 검색했다.

| Round 1 항목 | 원래 판정 | 수정 | 근거와 검색 경로 |
|---|---|---|---|
| C2 정적 유사성 지도 vs 경험된 전이 지도 | partially (Ma & Kragel) | **partially, 범위 축소** | Thornton, Weaverdyck, Tamir 2019 (doi:10.1523/JNEUROSCI.1431-18.2018) [초록]: 현재 정신상태 패턴이 가능성 높은 미래 상태 패턴을 닮지만, "그 연관의 상당 부분이 3차원 심리 공간의 근접성으로 설명된다". brain-inspired 에이전트가 먼저 찾았다. 따라서 전이 효과와 정적 유사도는 크게 겹치며, 남는 새 부분은 방향성(반대칭) 성분의 분리다(GI-P2) |
| C4 공유 지도, 개인별 통과 | no | **partially** | Tan, Liu, Zhang 2022 (doi:10.1007/s12021-022-09568-5) [초록]: 정서 영화에서 dynamic hyperalignment 후 HMM 상태가 참가자 간 더 일관. PubMed 검색 "dHA-HMM naturalistic stimuli evoked emotion changes brain state dynamics" (2026-11-12). 개인별 통과 시점과 속도를 측정 대상으로 삼고 본인 생리와 맞추는 부분은 여전히 미발견 |
| C5 washout 이완 시간상수 | partially (Eryilmaz 2011, Gaviria 2021) | **partially, 범위 축소** | Baez-Lugo et al. 2023 (doi:10.1038/s43587-022-00341-6) [초록]: 사회 정서 영상 뒤 휴식기 fMRI(182명)에서 연령 효과가 영상 중보다 휴식기에 두드러지고, 노인의 DMN-amygdala 휴지기 연결 변화가 불안, 반추와 연관. WebSearch "emotional film offset recovery time constant fMRI individual differences emotional inertia ..." (2026-11-12). 남는 새 부분: 정서 정의 잠재 차원의 시간상수를 감각 차원 대조와 함께 추정, 영화 14편 반복으로 개인 내 신뢰도, 같은 사람 EDA 회복과 대응 |
| C1 정서 반응의 rank 분해 공유 스펙트럼 | no | **no 유지(정서 적용), 단 방법의 개인차 확장은 partially** | WebSearch "cross-decomposition OR shared variance spectrum OR covariance spectrum emotion fMRI individuals 2025 2026" (2026-11-12): 정서 적용 없음. Han & Bonner 2025 (arXiv:2505.12653) [DB]가 영화 시청의 rank별 개인차를 보였다(시각 경험). emotion-theory C1이 같은 질문을 독립적으로 제안했다(수렴) |
| I2 범주를 가로지르는 valence CCGP | no | **partially (양식 간)** | Chikazoe et al. 2014 (doi:10.1038/nn.3749) [초록]: OFC valence 부호가 시각과 미각을 가로지르고 참가자 간 분류 가능. 정서 범주를 조건으로 한 CCGP는 미발견 |

### 0.2 Mind captioning 데이터(5번째 데이터셋)가 바꾸는 것 [본문, PMC12588295 Materials and Methods]

확인한 사실:
* 피험자 6명, **모두 일본어 모국어 화자**(S1~S5 영어 능숙, S6 제한적). S1은 예비 실험에서 같은 자극에 여러 번 노출되었다.
* 같은 Cowen & Keltner 2,196개에서 중복 16개를 뺀 **2,180개 고유 비디오를 각 1회**, 무음. 학습 세션 60 run. 10 s 미만 비디오는 10 s를 넘을 때까지 반복 재생.
* 학습 세션 제시 순서는 **pseudorandom이며 코호트 안에서는 모든 피험자에게 같다.** Horikawa 2020 코호트의 순서와 같은지는 논문에 적혀 있지 않다(미확인).
* 테스트 세션: 학습 세션 마지막 두 run의 72개 비디오를 **각 5회** 추가 제시(즉 이 72개는 총 6회 노출).
* 3T, TR 1 s(vision-decoding Round 1 기록), fMRIPrep 후 constant, linear trend, 24개 head motion, **CSF, WM, 회백질(GM) 평균과 그 미분, 제곱(12개 전역 신호)을 회귀**, 4 s shift 후 블록 평균, run 내 z-score.
* 블록 사이에 캡션 일치 평정(evaluation block)이 무작위 삽입되었다.

내 Round 1 C1과 관련된 함의:
1. **피험자 쌍이 10개에서 55개로** 늘고, 그중 30개는 코호트를 가로지르는 쌍이다. 코호트 간 쌍은 스캐너 세션, run 경계, (순서가 다르다면) 순서 효과를 공유하지 않는다. 따라서 **코호트 내 공유 스펙트럼과 코호트 간 공유 스펙트럼의 차이가 "순서, 세션, 프로토콜이 만든 공유 분산"의 직접 추정치**가 된다. Westlin 2025의 session NMI 0.19 문제를 정량적으로 다루는 길이다.
2. **72개 x 6회 반복**으로 피험자 안의 신뢰 분산 스펙트럼(교차검증 PCA)을 구할 수 있다. 이것과 피험자 간 공유 스펙트럼을 같은 72개에서 비교하면 rank별로 "신뢰할 수 있지만 공유되지 않는 분산" = **재현 가능한 개인 고유 성분**을 처음으로 잡음과 분리할 수 있다. Westlin이 주장한 "구조화된 개인 변동"을 직접 검정한다. 단 72개라 최대 71차원이고 72개의 정서 분포는 미확인이다.
3. 전처리 차이: Mind captioning 전처리본은 GM 전역 신호를 회귀했다. Horikawa 2020 공개 전처리본의 전역 신호 처리 여부는 Stage 1에서 미확인이다. Bolt 2025 [DB, doi:10.1038/s41593-025-01945-y]가 보인 자율신경성 전역 성분이 한 코호트에서만 제거되었을 수 있으므로, 두 코호트를 raw에서 같은 파이프라인으로 다시 맞추거나 두 처리를 모두 보고해야 한다. 사용자가 "전처리를 마쳤다"고 한 파이프라인의 세부는 미확인이다.
4. 위험: 두 코호트 사이 피험자 중복 여부 미확인(같은 연구자). 중복이 있으면 코호트 간 쌍에 같은 사람 쌍이 섞여 공유도를 부풀린다. 저자 확인을 권한다(해부 영상으로 재식별을 시도하는 것은 권하지 않는다). S1의 사전 노출도 공변량으로 둔다.
5. Mind captioning 참가자가 일본어 모국어 화자라는 사실이 본문으로 확인되어, llm-semantics Chain 6(일본어 vs 영어 정서 표상)의 선결 조건 하나가 이 코호트에서는 충족된다(GI-P6).

---

## 1. 가져온 아이디어

### A1. 자극 표집 구조가 만드는 가짜 범주 기하 (vision-decoding → geometry-info)
* 출처: vision-decoding Round 1 4절 1번, R3. 근거 Shirakawa et al. 2025 (doi:10.1016/j.neunet.2025.107515) [DB]: 학습 자료가 군집화되어 있으면 예측 가능한 출력 차원이 붕괴해 분류가 재구성처럼 보인다.
* 가져오는 내용: Cowen & Keltner 라이브러리는 범주를 잘 유발하도록 모은 군집 표본이다. 그러면 내 C1의 공유 스펙트럼과 C7의 IB 분석, 그리고 Horikawa 2020의 군집 결론 모두에서 **"범주형 기하"의 일부가 자극 표집 밀도에서 올 수 있다.** 수정안: 규범 평정 공간에서 밀도를 균등화하도록 자극을 재표집한 부분집합(예: 평정 공간 격자별 동수 표집)에서 스펙트럼과 군집 구조를 다시 계산하고, 원 표집과의 차이를 "표집 유래 기하"로 보고한다. 범주 hold-out(VD-R3)은 같은 문제의 decoding 쪽 검정이다.

### A2. Rank 대역별 개인차와 "차원 수를 스칼라로 말하지 말 것" (emotion-theory → geometry-info)
* 출처: emotion-theory Round 1 1절 U1 보강, 4절 X1 보강, C8. 근거 Han & Bonner 2025 (arXiv:2505.12653) [DB], Gauthaman 출판본 4.2절(emotion-theory가 본문 확인) [DB].
* 가져오는 내용: (a) 개인차를 rank 대역별로 나누면 대역마다 질적으로 다른 개인차가 행동(회상)을 예측한다. 내 C8(Spacetop 과제 간 개인 기하)과 C3(valence 개인 특이성)에서 "개인 편차"를 한 덩어리로 보지 않고 대역별 IS-RSA로 바꾼다. (b) 스펙트럼 결과는 "몇 차원"이 아니라 스펙트럼 모양의 모형 비교(power law, 지수 절단 power law, lognormal)와 비선형 차원 추정의 병기로 보고한다. 내 U1(scale-free × IB)의 반증 조건도 이 모형 비교로 바꾼다.

### A3. 전역 자율신경 성분 (systems-neuro → geometry-info)
* 출처: systems-neuro Round 1 0절 2, 3번, U1, Chain 1, 4절 C1. 근거 Bolt et al. 2025 (doi:10.1038/s41593-025-01945-y) [DB]: 전역 fMRI 신호가 교감 각성과 결합해 저주파 분산의 약 25%를 차지한다.
* 가져오는 내용: 내 P6("비지도 구조는 고분산 부분공간을 찾는다")의 구체적 후보가 생겼다. Westlin의 상위 PC 군집이 세션과 대응한 것은 세션별 각성, 졸음 수준의 전역 성분 때문일 수 있다. 또 내 P3(valence 비전이)와 결합하면 **"휴대 가능한 arousal 판독은 개인 간에 가장 크게 공유되는 저rank 전역 자율신경 모드에 실리고, 휴대 불가능한 valence는 고rank, 개인 특이 성분에 있다"**는 검정 가능한 기하 가설이 된다(GI-P7).

### A4. 평정자 반복 시청에 따른 시간 앞당김과 동역학 유사도 (multimodal-dynamics → geometry-info)
* 출처: multimodal-dynamics Round 1 4절 5번, Chain 7. 근거 Lee et al. 2021 (doi:10.7554/eLife.64972) [DB]: 반복 시청 시 뇌 사건 경계가 앞당겨짐. Ostrow et al. 2023 DSA (arXiv:2306.10168) [DB].
* 가져오는 내용: 내 C4(개인별 time-warp)는 consensus 평정 시계열을 기준축으로 쓴다. Emo-FilM 평정자는 같은 영화를 최대 6번 봤으므로 consensus 자체가 처음 보는 fMRI 참가자보다 앞당겨져 있을 수 있다. 수정안: 모든 참가자에게 공통인 "평정자 예측 앞당김" 오프셋을 따로 추정하고, 개인 warp는 그 오프셋을 뺀 나머지로 정의한다. DSA는 "기하는 다르지만 흐름이 같은" 개인을 찾는 C4의 판정 지표로 추가한다.

### A5. 원인 귀속 확실성에 따른 범주 분리도 (brain-inspired → geometry-info)
* 출처: brain-inspired Round 1 4절 2번. 근거 Emanuel & Eldar 2023 (doi:10.1016/j.neubiorev.2022.104977) [DB]: 나쁜 결과의 원인 귀속이 불확실하면 분화되지 않은 부정 정서가 최선일 수 있다.
* 가져오는 내용: 내 I2(CCGP와 shattering dimensionality)에 조건 변수를 준다. Emo-FilM의 Agent(사람 원인, 우연 원인) appraisal 연속 평정으로 구간을 나누고, 귀속이 확실한 구간과 불확실한 구간에서 anger-sadness 신경 패턴의 분리도(선형 분리 margin, SD)를 비교한다. "범주 기하의 해상도는 고정값이 아니라 appraisal 상태에 따라 바뀐다"는 예측이며, 범주 대 차원 논쟁에 조건부 답을 준다.

### A6. 소표본 모집단 유병률 추론과 chance 보정 지표 (adversarial-reviewer → geometry-info)
* 출처: adversarial-reviewer Round 1 U2, U7, D1. 근거 Ince et al. 2021 (doi:10.7554/eLife.62461) [DB].
* 가져오는 내용: 내 0.2절(Round 1) 소표본 원칙에 "피험자별 검정 + Bayesian prevalence"를 공식 보고 형식으로 넣는다. Horikawa 2020 5명과 Mind captioning 6명을 합친 11명에서 "공유 스펙트럼의 고rank 공유가 몇 명에서 유의한가"를 유병률로 보고한다. Westlin식 군집 비교에는 NMI 대신 chance 보정 지표(AMI)를 쓴다.

---

## 2. 보내는 제안

### GI-P1. 두 코호트 교차 공유 스펙트럼으로 Horikawa 범주 결론과 Westlin 재현 실패를 판정하기
* **받는 에이전트:** emotion-theory (참조: systems-neuro, adversarial-reviewer)
* **제안 내용:** 너희 쪽 C1(신뢰 차원 스펙트럼)과 C2(신뢰 부분공간 비지도 구조)를, 우리 쪽 두 코호트 교차 cross-decomposition과 반복 기반 개인 고유 성분 분리로 검증하고 확장할 수 있다. systems-neuro Chain 2(network subspace), adversarial-reviewer D1(multiverse), 내 C1이 같은 질문을 독립적으로 제안했으므로 한 프로그램으로 합칠 것을 제안한다. 설계:
  1. Horikawa 2020 5명 + Mind captioning 6명 = 55쌍. 코호트 내 쌍(10 + 15)과 코호트 간 쌍(30)의 rank별 공유 스펙트럼을 따로 계산한다. 차이 = 순서, 세션, 프로토콜이 공유한 분산(0.2절 1).
  2. Mind captioning 72개 x 6회로 피험자 내 신뢰 스펙트럼을 구하고, 같은 72개에서의 피험자 간 공유 스펙트럼과 비교해 rank별 "재현 가능한 개인 고유 분산"을 추정한다(0.2절 2).
  3. 공유 차원을 34범주, 14차원 규범 평정, Mind captioning 정서 배제 캡션 embedding, 시각 feature로 대역별 variance partitioning(A1의 표집 균등화 부분집합에서도 반복).
  4. 군집 multiverse(ET-C2, AR-D1)는 세 입력 경로(분산 기준 PCA, 평정 기반 선택, 코호트 간 공유 부분공간)에서 같은 알고리즘으로, 지표는 AMI와 prevalence(A6).
* **관련 Axis:** K, O, Q, T, S, U
* **근거 논문 ID:** arXiv:2409.06843(출판본 doi:10.1371/journal.pcbi.1013714), arXiv:2505.12653, arXiv:2507.00320, doi:10.1016/j.isci.2020.101060, doi:10.1126/sciadv.adw1464, doi:10.1038/s41593-025-01945-y, doi:10.7554/eLife.62461, doi:10.1016/j.neunet.2025.107515
* **가능한 데이터셋:** Horikawa 2020(G1 불필요), Mind captioning(전처리 완료, 캡션 포함 여부 미확인), NSD shared1000(시각 대조 스펙트럼)
* **예상되는 반론:** (a) 코호트 간 TR(2 s vs 1 s), 최소 블록 길이(8 s vs 10 s), 전처리(GM 전역 신호 회귀) 차이가 공유도를 낮춘다. 그러면 코호트 간 공유는 보수적 하한이 되며, 그 하한에서도 남는 정서 공유 차원이 가장 강한 증거다. (b) 피험자 중복이 있으면 결론이 바뀐다(저자 확인 선행). (c) 72개 테스트 클립은 평균 3.94 s로 짧고 6회 노출로 반복 억제가 생긴다. (d) emotion-theory가 지적했듯 공유 성분만 세면 개인 특이 정서 신호가 빠진다. 2번 단계가 바로 그 보완이다.
* **label-provenance:** 스펙트럼 자체는 라벨 비의존. 해석 단계의 정서 라벨은 대상 felt(평정자 자기 경험 보고) / 주체 별도 평정자 규범(MTurk). 캡션은 대상 기술 의미 / 주체 별도 평정자(정서 배제 지시).
* **evidence-level:** R0
* **G1:** 핵심 분석 불필요, 최신 모델 feature는 필요(보유). **overlap:** EmoViS (Horikawa 정서 기하의 sensory-semantic 기원, 부분), EmoBrain (cross-subject, 약함)

### GI-P2. 정서 전이의 방향성 성분: SR(T) 대 SR(T')를 넘어 반대칭 흐름과 비가역성으로
* **받는 에이전트:** brain-inspired (참조: adversarial-reviewer D3, multimodal-dynamics Chain 7)
* **제안 내용:** 너희 쪽 Chain 1의 SR(T) 대 SR(T') 방향성 검정을, 우리 쪽 전이 행렬의 대칭/반대칭 분해와 엔트로피 생산(비가역성) 지표로 검증하고 확장할 수 있다. 근거: Thornton 2019 초록은 전이-신경 연관의 상당 부분이 정적 근접성으로 설명된다고 했으므로, 방향성 증거는 대칭 성분을 직교화한 뒤에만 의미가 있다. 설계:
  1. Emo-FilM 1 Hz consensus(영화별, leave-one-film-out)에서 이산화한 정서 상태의 전이 행렬 T를 S = (T + T')/2 와 A = (T - T')/2 로 나눈다. A는 순 확률 흐름(net flux)이며 어떤 대칭 유사도 지도로도 표현할 수 없다.
  2. 평정 궤적 자체가 detailed balance를 깨는지(정서의 시간 화살표: 예컨대 공포에서 안도로의 흐름이 반대보다 많은지) 먼저 측정한다. A가 작으면 방향성 질문은 이 데이터에서 검정력이 없다(AR-D3의 식별 가능성 1단계와 같은 역할).
  3. 신경 쪽에서는 hippocampus 전후, vmPFC 상태 궤적의 엔트로피 생산을 정서 밀도가 높은 구간과 낮은 구간에서 비교하고, 신경 순 흐름의 방향이 평정 순 흐름과 정렬되는지 본다.
  4. SR(T)와 SR(T')의 신경 적합도 차이가 영화별 |A|에 비례하는지 본다. 비례하지 않으면 방향성 적합도 차이는 잡음이다.
* **관련 Axis:** K, D, N, (외부) Complex Systems / Information-theoretic Neuroscience
* **근거 논문 ID:** doi:10.1038/s41467-025-68240-z, doi:10.1523/JNEUROSCI.1431-18.2018, doi:10.1073/pnas.1616056114, doi:10.1038/nn.4650, doi:10.1073/pnas.2109889118, doi:10.1126/sciadv.ade6049, arXiv:2306.10168
* **가능한 데이터셋:** Emo-FilM(주), Spacetop narratives(언어 서사의 방향성 대조, 평정은 이야기 단위라 보조)
* **예상되는 반론:** (a) HRF 자체가 시간 비대칭 커널이라 BOLD 궤적은 신경 활동이 가역적이어도 비가역성을 보일 수 있다. 평정 궤적으로 구동한 HRF 합성 대리 자료와 위상 무작위화 대리 자료를 null로 둔다. (b) 엔트로피 생산 추정은 상태 수와 자료 길이에 민감하다(영화 14편, 약 2.7시간). 거친 상태 분할과 bootstrap 신뢰구간이 필수다. (c) 영화의 전이는 서사가 만든 것이며 평정자는 반복 시청으로 앞을 안다(A4). (d) Kringelbach 2023 초록은 영화 시청 전체의 비가역성이 휴지기보다 낮다고 보고했으므로, 효과가 있더라도 작을 것이다.
* **label-provenance:** 대상 felt(평정자 자기 경험 보고, 평정자 내 z-score) / 주체 별도 평정자 consensus(3~4명). 전이는 fMRI 참가자의 경험이 아니다.
* **evidence-level:** R0
* **G1:** 불필요. **새로움 검색:** WebSearch "entropy production broken detailed balance time irreversibility emotion fMRI naturalistic movie affective dynamics" (2026-11-12): 정서 적용 미발견, 영화 전체 평균 비교(doi:10.1126/sciadv.ade6049)만 있음. **overlap:** Emo-FilM 연구 (Emo-FilM 시간 정보, 약함)

### GI-P3. 입력이 꺼진 구간의 흐름: washout 이완으로 HRF 잔여와 정서 관성을 가르기
* **받는 에이전트:** multimodal-dynamics (참조: systems-neuro Chain 5, frontier-ai T5)
* **제안 내용:** 너희 쪽 Chain 1(Horikawa 이월)과 Chain 7(DSA로 본 정서 흐름)을, 우리 쪽 "부분공간별 감쇠 대조"와 Emo-FilM washout 이완(C5)으로 검증할 수 있다. 핵심 논리: HRF 잔여는 모든 부분공간에 같은 시간 커널로 작용하므로, **같은 영역에서 정서 정렬 부분공간의 감쇠가 시각 정렬 부분공간의 감쇠보다 느리면** 그 차이는 HRF로 설명되지 않는다.
  1. Emo-FilM: 영화 앞뒤 90 s washout(영화 14편 x 30명, 생리 기록 포함). 영화 중 consensus로 정의한 정서 부분공간과 시각 feature로 정의한 부분공간에 washout 신호를 투사해 각각 이완 시간상수를 적합한다. 영화 시작 전 washout은 기저 동역학의 대조다. washout에는 자극 구동이 없으므로 DSA로 개인 간 "자율 흐름"을 비교하기에 가장 깨끗한 구간이다.
  2. Horikawa(와 Mind captioning): 블록 사이 휴지가 2 s뿐이라 이완 적합은 어렵지만, 같은 논리로 t-1, t-2 블록의 정서 부분공간 투사와 시각 부분공간 투사의 잔존 비율을 비교한다(너희 Chain 1의 판별 지표로 추가).
  3. 개인별 시간상수의 영화 간 신뢰도(ICC)와 같은 사람 EDA 회복 시간과의 대응.
* **관련 Axis:** D, K, E, O
* **근거 논문 ID:** doi:10.1038/s41586-024-07915-x, doi:10.1016/j.cell.2022.11.027, doi:10.1126/sciadv.abf7129, doi:10.1038/nn.4468, doi:10.1016/j.neuroimage.2021.118377, doi:10.1038/s43587-022-00341-6, arXiv:2306.10168
* **가능한 데이터셋:** Emo-FilM(주), Horikawa, Mind captioning(보조)
* **예상되는 반론:** (a) 영역마다 HRF 모양이 다를 수 있으나, 같은 영역 안의 두 부분공간 비교로 이 문제를 줄인다. 그래도 정서 부분공간이 느린 HRF를 가진 voxel에 치우칠 수 있어 voxel별 HRF 추정과 가중을 병행한다. (b) Emo-FilM 제공 전처리본의 high-pass(sigma 50 s)가 수십 초 이완을 깎는다. raw 재전처리가 필요하다. (c) washout에는 정서 평정이 없어 해석은 영화 끝 평정과 EDA로 간접 검증한다. 마음 방황, 졸음과 구분되지 않는다. (d) 부분 선행(Baez-Lugo 2023, Gaviria 2021)이 있으므로 새로움은 "부분공간 대조 기반 시간상수와 개인 내 신뢰도"로 한정한다.
* **label-provenance:** 영화 중 부분공간 정의는 대상 felt / 주체 별도 평정자 consensus. 생리는 fMRI 참가자 본인 측정.
* **evidence-level:** R0 (관찰 자료, attractor의 인과 증거 아님)
* **G1:** 정서 부분공간 정의는 불필요, 시각 부분공간 정의는 필요(보유). **overlap:** Emo-FilM 연구 (시간 정보, 약함)

### GI-P4. TRIBE v2를 "12번째 피험자"로: rank별 in-silico 충실도와 GW 수준별 대응
* **받는 에이전트:** encoding-foundation (참조: generative-counterfactual CH3)
* **제안 내용:** 너희 쪽 Chain 1(in-silico 정서 기하의 충실도)을, 우리 쪽 cross-decomposition과 Gromov-Wasserstein 정렬로 검증하고 확장할 수 있다. RSA 상관 하나(EmoMind의 0.635 → 0.166)는 어느 차원이 사라지는지 말하지 못한다.
  1. TRIBE v2 group 예측을 한 명의 의사 피험자로 두고, 인간 11명(Horikawa 2020 + Mind captioning)과의 rank별 교차 스펙트럼을 인간-인간 스펙트럼과 비교한다. 공정한 기준선은 "그 피험자를 뺀 나머지 인간의 평균"(leave-one-out 평균)이라는 의사 피험자다. TRIBE가 LOO 평균과 모든 rank에서 같으면 그 영역의 공유 분산은 자극으로 계산 가능하고, 특정 rank 대역에서만 떨어지면 그 대역이 "자극 계산 불가능한 공유 성분" 후보다.
  2. 그 결손 대역을 규범 정서 평정과 정서 배제 캡션에 투사해 "residual affect"(GC-CH3)가 어느 rank에 있는지 본다.
  3. GW로 TRIBE 기하와 관찰 기하를 클립 단위와 범주 단위에서 각각 정렬해, Asanuma 2025가 MLLM에서 본 "범주 수준은 맞고 항목 수준은 틀림" 패턴이 in-silico 뇌에도 있는지 본다.
* **관련 Axis:** K, H, F, S, R
* **근거 논문 ID:** arXiv:2605.04326, arXiv:2605.16739, arXiv:2409.06843, doi:10.1038/s41598-025-14961-6, doi:10.1038/s41598-024-65604-1, doi:10.1126/sciadv.adw1464
* **가능한 데이터셋:** Horikawa 2020 + Mind captioning(같은 2,180개 클립, 무음), Emo-FilM(30명, 시청각)
* **예상되는 반론:** (a) TRIBE 예측은 잡음이 없는 group 평균이라 인간과의 교차 스펙트럼 상한이 인간 신뢰도에 묶인다. LOO 평균 기준선으로 맞춘다. (b) 공개 checkpoint는 fsaverage5 피질만 예측하므로 피질하 결론은 낼 수 없다. (c) TR과 블록 평균 방식을 관찰 자료와 같게 맞춰야 한다. (d) feature backbone의 사전학습에 Cowen & Keltner 비디오가 들어갔는지 미확인(encoding-foundation U6). (e) 라이선스 CC BY-NC 4.0(연구 사용 가능, encoding-foundation 기록).
* **label-provenance:** 스펙트럼과 GW는 라벨 비의존. 2단계 투사는 대상 felt / 주체 별도 평정자 규범.
* **evidence-level:** R0, insilico-vs-observed: 혼합
* **G1:** 필요(보유). **새로움 검색:** WebSearch "Gromov-Wasserstein in-silico encoding model predicted fMRI versus observed representational geometry comparison TRIBE" (2026-11-12): 미발견. **overlap:** Emo-FilM 연구 (Emo-FilM 부분, 사전학습 멀티모달 encoding)

### GI-P5. Spacetop "잔차 대 본인 보고 편차" 제안 여섯 개를 기준선 multiverse 하나로
* **받는 에이전트:** vision-decoding (참조: encoding-foundation Chain 3, generative-counterfactual CH5, llm-semantics Chain 5, emotion-theory C4/C8)
* **제안 내용:** 너희 쪽 R5(공유 latent와 개인 잔차)를 우리 쪽 rank 분해와 재현성 검정으로 검증하고, 같은 질문을 다른 기준선으로 제안한 다섯 에이전트(EF-Chain 3: TRIBE 예측, GC-CH5: TRIBE 또는 LOO 평균, LS-Chain 5: MLLM 예측, ET-C4/C8: peer 평균과 rank 범위, 내 C3/C8: INT 개인화)의 설계를 하나의 사전등록 multiverse로 합칠 것을 제안한다. 질문은 같고("같은 영상에서 기대 반응에서 벗어난 내 뇌가 내 보고의 편차를 예측하는가") 기준선만 다르다. 공통 규칙:
  1. 같은 분할(영상 단위 보류, 피험자 단위 보류), 같은 결측 모형(alignvideo 약 51% 결측, 클릭 저장 구조), 같은 평정 구간 HRF 처리(평정 구간 이전 TR만 사용).
  2. 잔차를 쓰기 전에 잔차 자체의 신뢰도를 먼저 보고한다(run 또는 영상 절반 분할). 신뢰도가 없는 잔차로 보고 편차를 예측하는 것은 무의미하다.
  3. 잔차를 rank 대역별로 나눠(A2) 어느 대역이 보고 편차를 예측하는지 본다.
  4. 결과 표: 기준선 5종 x rank 대역 x ROI. 기준선 간 차이 자체가 결과다(예: MLLM 기준 잔차만 예측하면 "평균 관찰자 의미에서 벗어난 성분"이 본인 경험과 맞는다는 뜻).
  5. 추가로 너희 R6의 정서 배제 캡션 통제를 Horikawa + Mind captioning 쪽에 적용할 때, 캡션 embedding으로 예측한 반응을 뺀 잔차의 개인 간 공유 스펙트럼을 계산하면 "기술 의미 밖에 남는 공유 정서 차원 수"를 직접 셀 수 있다(GI-P1 3단계와 연결).
* **관련 Axis:** O, U, G, H, Q, T
* **근거 논문 ID:** arXiv:2403.11207, arXiv:2605.04326, arXiv:2408.13718, arXiv:2505.12653, doi:10.1162/imag_a_00032, doi:10.1126/sciadv.abf7129, doi:10.1038/s41586-022-04492-9
* **가능한 데이터셋:** Spacetop alignvideo(주), Horikawa 2020 + Mind captioning(캡션 통제 부분)
* **예상되는 반론:** (a) 영상 49개, 결측 약 51%로 검정력이 낮다. 다섯 기준선을 다 돌리면 다중비교가 커진다. 사전등록과 기준선 간 비교 자체를 1차 지표로 두는 것으로 대응한다. (b) 기준선들이 서로 중첩되어(LOO 평균과 TRIBE는 상관) 차이가 작을 수 있다. (c) Spacetop에는 valence와 arousal 문항이 없다. (d) 약 100명도 형질 상관에는 작으므로(Marek 2022) 개인 내 결합만 다룬다.
* **label-provenance:** 대상 felt / 주체 참가자 본인(Spacetop alignvideo 사후 평정). 기준선은 각각 peer 합의, AI 추정(MLLM), in-silico 예측(TRIBE)으로 분리 표기.
* **evidence-level:** R0
* **G1:** TRIBE, MLLM 기준선은 필요(보유). **overlap:** EmoBrain (cross-subject decoding, 부분)

### GI-P6. 정서 어휘의 정보 병목 효율: 일본어 화자 뇌 공간에서 일본어 범주와 영어 범주 비교
* **받는 에이전트:** llm-semantics (참조: emotion-theory)
* **제안 내용:** 너희 쪽 Chain 6(일본어로 기술한 정서와 영어로 기술한 정서 중 무엇이 Horikawa 뇌와 맞는가)을, 우리 쪽 Information Bottleneck 효율 분석(Round 1 C7)으로 확장할 수 있다. Mind captioning 참가자가 일본어 모국어 화자라는 사실이 본문으로 확인되어(0.2절) Chain 6의 선결 조건이 이 코호트에서 충족된다.
  1. 의미 공간: (a) Mind captioning 6명의 공유 신경 부분공간(GI-P1에서 캡션 성분을 뺀 정서 정렬 부분), (b) 34 + 14 규범 평정 공간.
  2. 명명 체계: Cowen & Keltner 영어 34범주, 27 군집, 기본 6범주, 일본어 정서 어휘 체계(MLLM이 일본어 어휘로 각 클립을 명명, AI 추정으로 표기), Jackson 2019의 colexification으로 병합한 범주.
  3. 각 체계의 IB 복잡도와 정확도, IB 경계와의 거리를 (a)와 (b)에서 각각 계산한다. 질문: "일본어 화자의 뇌 공간에 대해 일본어 정서 범주 체계가 영어 체계보다 IB 경계에 가까운가?" 같은 분석에서 각 범주가 신경 공간의 볼록 영역인지도 따로 잰다. 볼록성과 효율은 서로 함의하지 않으므로(arXiv:2602.08238 [초록]), Cowen & Keltner의 흐린 경계(gradient)가 "비볼록이지만 효율적인 체계"인지가 검정 가능한 질문이 된다.
  4. 이 결과로 Deliverable B 2.3절의 "Information-theoretic Efficiency" Sub-axis 위치를 Round 3에서 함께 판정하자고 제안한다(5절).
* **관련 Axis:** K(IB Sub-axis), A, C, U, O
* **근거 논문 ID:** doi:10.1073/pnas.1800521115, arXiv:2602.08238, doi:10.1126/science.aaw8160, doi:10.1126/sciadv.adw1464, doi:10.1038/s41598-024-65604-1, arXiv:2509.24298
* **가능한 데이터셋:** Mind captioning(주, 일본어 화자), Horikawa 2020(참가자 언어 미확인이라 보조)
* **예상되는 반론:** (a) MLLM의 일본어 명명은 일본어 화자의 어휘 사용과 같지 않다. 소규모 일본어 화자 명명 수집(R2 수준)으로 타당화해야 결론이 선다. (b) 자극 분포 p(m)은 큐레이션된 라이브러리다(A1의 표집 균등화 적용). (c) 신경 공간에 정서 밖 내용이 섞인다. (d) 6명이라 효과 크기 추정 중심.
* **label-provenance:** 대상 perceived affective quality에 가까움(MLLM 명명) / 주체 AI 추정. 비교 기준은 대상 felt / 주체 별도 평정자 규범(영어).
* **evidence-level:** R0 (신규 명명 수집 시 R2)
* **G1:** MLLM 명명에는 필요(보유). **새로움 검색:** WebSearch "information bottleneck emotion categories efficient communication emotion lexicon near-optimal compression 2025 2026" (2026-11-12): 정서 적용 미발견(색, 행동, 시제 등 다른 영역만). **overlap:** EmoViS (Horikawa 정서 기하, 약함)

### GI-P7. 휴대 가능한 arousal은 저rank 전역 자율신경 모드인가
* **받는 에이전트:** systems-neuro
* **제안 내용:** 너희 쪽 Chain 1(network arousal 판독의 자율신경 성분 분리)을, 우리 쪽 rank 분해로 검증할 수 있다. 가설(A3): 영화와 데이터셋을 넘어 전이되는 arousal 판독(Ke 2025, Zaffina 2026)은 개인 간 가장 크게 공유되는 저rank 전역 모드에 실리고, 전이되지 않는 valence 정보는 고rank, 개인 특이 성분에 있다. 설계: Emo-FilM 30명의 개인 간 공유 스펙트럼을 (i) 참가자 본인 생리(PPG 진폭, 호흡, EDA) 회귀 전후, (ii) raw 재전처리 vs 제공 전처리본(WM/CSF 회귀)에서 계산하고, rank 대역별로 arousal 대리 항목과 Good/Bad를 decoding해 영화 간 전이를 대역별로 본다. Horikawa 2020(전역 신호 처리 미확인) 대 Mind captioning(GM 전역 신호 회귀)의 파이프라인 차이도 자연 대조로 쓴다.
* **관련 Axis:** E, K, O, Q, (태그) signal-feasibility
* **근거 논문 ID:** doi:10.1038/s41593-025-01945-y, doi:10.1371/journal.pcbi.1012994, doi:10.64898/2026.09.26.754452, arXiv:2409.06843, doi:10.1126/sciadv.adw1464
* **가능한 데이터셋:** Emo-FilM(주), Horikawa 2020 + Mind captioning(파이프라인 대조)
* **예상되는 반론:** (a) 생리 회귀가 신경 arousal 신호까지 지울 수 있다(과통제, generative-counterfactual Axis P의 지적). 회귀 전후를 모두 보고한다. (b) rank 대역은 해부학적으로 해석하기 어렵다. 대역별 공간 지도를 함께 제시한다. (c) 정서 라벨이 별도 평정자 규범이라 fMRI 참가자의 arousal과 다를 수 있다.
* **label-provenance:** 대상 felt / 주체 별도 평정자 consensus(Emo-FilM). 생리는 참가자 본인 측정.
* **evidence-level:** R0
* **G1:** 불필요. **overlap:** Emo-FilM 연구 (생리와 정서 맥락, 부분)

### GI-P8. 정서와 무관한 정렬이 사람 사이의 정서 기하를 운반하는가
* **받는 에이전트:** frontier-ai
* **제안 내용:** 너희 쪽 CH6(정서 무관 정렬이 VLM 사이와 VLM→뇌에서 정서 기하를 운반하는가)을, 우리 쪽 뇌-뇌 기능 정렬로 옮겨 검증할 수 있다. 설계: Horikawa 2020 + Mind captioning에서 규범 평정상 정서 강도가 낮은 클립만으로 hyperalignment(또는 SRM, INT)를 학습하고, 정서 강도가 높은 클립에서 개인 간 정서 기하 전이(교차 피험자 decoding, GW 매칭률)를 고정서 클립으로 학습한 정렬과 비교한다. Spacetop에서는 정서 비관련 과제(예: 통증 cue 없는 구간이나 다른 과제)로 정렬을 학습하고 alignvideo에 적용한다. 대조: 시각-의미 다양성을 맞춘 무작위 클립 집합으로 학습한 정렬.
  * 결과 해석: 저정서 정렬이 고정서 정렬만큼 정서 기하를 운반하면 "개인의 정서 표상은 일반 표상 골격에 얹혀 있다". 운반하지 못하면 "정서는 별도의 개인별 사상이 필요하다"(개인 특이 정서 지도의 증거, Westlin 해석과 정합).
* **관련 Axis:** O, K, R, S, J
* **근거 논문 ID:** arXiv:2609.34742, arXiv:2405.07987, arXiv:2106.04619, doi:10.7554/eLife.56601, doi:10.1016/j.neuroimage.2020.116618
* **가능한 데이터셋:** Horikawa 2020 + Mind captioning(주), Spacetop(보조), NSD(정서 범위가 좁은 자극만으로 정렬했을 때의 극단 대조)
* **예상되는 반론:** (a) 저정서 클립은 내용 범위도 좁아 정렬 실패가 정서가 아니라 내용 범위(coverage) 때문일 수 있다. 캡션 embedding으로 내용 다양성을 맞춘 대조 집합이 필수다. (b) "저정서"를 규범 평정으로 고르면 라벨 의존 선택이 된다. 여러 기준(평정 강도, MLLM 추정)으로 견고성을 본다. (c) 5 + 6명이라 효과 크기 추정 중심.
* **label-provenance:** 클립 선택은 대상 felt / 주체 별도 평정자 규범. 정렬 학습과 평가는 신경 자료.
* **evidence-level:** R0
* **G1:** 내용 다양성 대조에는 필요(보유). **새로움 검색:** WebSearch "hyperalignment trained on neutral stimuli transfer to emotional stimuli shared emotion representation alignment generalization" (2026-11-12): 가장 가까운 것은 정서 사진으로 학습해 예고편에 적용한 Chan 2020(doi:10.1016/j.neuroimage.2020.116618). 중립 자극만으로 학습한 정렬의 정서 운반 검정은 미발견. **overlap:** EmoBrain (cross-subject, 부분)

---

## 3. 받은 제안에 대한 응답

(Coordinator가 전달한 뒤 추가)

---

## 4. Coordinator 질문 8개에 대한 답 (geometry-info 관점)

**Q1. Vision Decoding 연구자가 Emotion Neuroscientist의 문제를 해결할 수 있는가?**
부분적으로 그렇다. 가장 쓸모 있는 것은 재구성 결과보다 그 분야의 **교차 피험자 공유 latent 기법**(arXiv:2403.11207)과 **평가 병리 진단**(output dimension collapse, doi:10.1016/j.neunet.2025.107515)이다. 후자는 정서의 "범주 기하"가 자극 표집에서 생길 수 있다는 경고로 바로 옮겨진다(A1). 재구성 이미지의 정서는 자극 수준(portrayed, normative) 정보이며 경험의 증거가 아니다(vision-decoding 0.3절 L1~L6에 동의).

**Q2. LLM의 representation이나 reasoning 능력을 neural emotion representation 분석에 활용할 수 있는가?**
그렇다, 단 "평균 관찰자"(L2) 기준선으로서다(arXiv:2408.13718). 기하 관점의 용도는 세 가지다: (a) GW로 뇌-평정-LLM 3자 구조를 정렬해 항목 수준과 범주 수준의 대응을 나눔(doi:10.1038/s41598-025-14961-6, doi:10.1038/s41598-024-65604-1), (b) 정서 배제 캡션의 LLM embedding을 빼고 남는 공유 신경 차원 수를 셈(GI-P1, GI-P5), (c) 언어별 정서 명명 체계의 IB 효율(GI-P6). LLM이 뇌를 잘 예측하는 결과는 description confound를 통제하기 전에는 정서 표상의 증거가 아니다.

**Q3. Generative AI로 emotion과 visual semantics를 분리해 검증할 수 있는가?**
모델 안에서는(R1) 가능하지만 새 fMRI 없이 뇌에 대한 분리 결론은 낼 수 없다. 정서를 조작하면 의미도 같이 움직인다(arXiv:2512.00557 [DB]). 기하 관점의 기여는 편집의 판정 기준이다: 편집된 자극이 모델 공간에서 캡션 부분공간에는 직교하고 정서 부분공간을 따라 움직였는지를 측정하고, metamer 논리(doi:10.1038/s41593-023-01442-0 [DB])로 "정서 영역 반응이 무시하는 변환의 동치류"를 정의할 수 있다. 결론 수준은 R1, 인간 평정 추가 시 R2다.

**Q4. Emotion Dynamics를 dynamical systems나 state-space learning의 문제로 재정의할 수 있는가?**
그렇다. 이 팀에서 가장 수렴이 큰 방향이다(GI-C4/C5, SN-Chain 5, MD-Chain 1/7, FA-T5, BI-Chain 7). 측정 가능한 정의는 (a) 이완 시간상수(line attractor의 기하 정의, doi:10.1038/s41586-024-07915-x), (b) 상태 의존 전이(rSLDS), (c) 흐름의 유사도(DSA, arXiv:2306.10168), (d) 비가역성(doi:10.1073/pnas.2109889118)이다. 전제는 HRF 커널과 BOLD 자기상관을 null로 두는 것이며, 같은 영역 안의 정서 부분공간 대 감각 부분공간 대조가 가장 깨끗한 통제다(GI-P3). 부분 선행(doi:10.1007/s12021-022-09568-5, doi:10.1016/j.neuroimage.2021.118377, doi:10.1038/s43587-022-00341-6)이 있으므로 새로움은 개인별 시간상수와 방향성 성분에 있다.

**Q5. Brain Foundation Model의 latent representation에서 감정 관련 구조를 찾을 수 있는가?**
찾을 수는 있지만 현재 근거는 약하다(누수 있는 분할, portrayed 라벨, encoding-foundation U5). 기하 관점의 검정은 latent 공간과 인간 개인 간 공유 스펙트럼의 rank별 정렬이다: latent가 저rank 전역 모드만 담는지(그러면 arousal, 각성 수준 신호일 가능성, A3), 고rank 공유 정서 차원까지 담는지. 휴지기 사전학습 모델(arXiv:2409.19407)과 flat map 모델(arXiv:2510.13768)은 피질하 포함 여부가 달라 같은 점수라도 의미가 다르다.

**Q6. Music, Video, Image의 공통 정서 특징과 modality-specific 특징을 뇌 수준에서 구분할 수 있는가?**
부분적으로. 우리 데이터에는 음악 단독 자극이 없고(Emo-FilM 사운드트랙은 영화 안에 섞임), Horikawa는 무음 비디오, NSD는 정지 이미지, Spacetop은 영상과 이야기다. 데이터셋 간 라벨은 풀링이 불가하다(Stage 1 3절 수준 2~3). 기하 관점의 해법은 unbalanced OT다: 양식별 정서 기하 사이에서 운반되는 질량을 공통 성분, 파괴되는 질량을 양식 특이 성분으로 정량한다(arXiv:2206.09398). 같은 사람 안의 양식 비교는 Spacetop(영상 vs 이야기)과 선행 연구(doi:10.1126/sciadv.adk6840, doi:10.1038/nn.3749)가 기준점이다.

**Q7. Neuroscience에서 관찰되는 정서 관련 계산을 AI architecture의 구조적 제약으로 구현할 수 있는가?**
가설 수준에서 가능하다. 후보: (a) 시간상수가 긴 통합 차원(line attractor)을 가진 상태공간 단위, (b) successor representation 기반 예측 지도(doi:10.1038/nn.4650), (c) power-law 스펙트럼 제약(부호의 매끈함, doi:10.1038/s41586-019-1346-5). 이 제약이 정서 예측을 실제로 개선하는지는 검증된 바 없고, frontier-ai CH7(정서 ROI 표적 brain-tuning)이 가장 직접적인 시험대다. 뇌 계산을 AI에 넣었을 때 성능이 오르는 것이 뇌가 그 계산을 쓴다는 증거는 아니다(doi:10.1162/nol_a_00087 [DB]).

**Q8. 정서 라벨이 없는 NSD 같은 데이터도 다른 데이터셋과의 representation alignment로 의미 있게 활용할 수 있는가?**
조건부로 그렇다. 정서 정보를 옮기려면 공유 자극이 없으므로 공통 모델 feature 공간(Stage 1 3.3절 경로 1)이나 비지도 정렬을 거쳐야 하고, 결과는 AI 추정 또는 전이 추정으로 표기해야 한다. 평가는 nsdmeadows 100장(지시문 미확인)에서 효과 크기 추정만 가능하다. NSD의 더 확실한 용도는 (a) 정서가 거의 없는 자극의 시각 대조 스펙트럼(arXiv:2409.06843이 이미 계산), (b) "정서 범위가 좁은 자극으로 학습한 정렬"의 극단 대조(GI-P8), (c) 반복 기반 noise ceiling 보정 함수(adversarial-reviewer D5)다. COCO의 VLM 사전학습 포함과 NSD 이미지의 중립 편향은 그대로 남는다.

---

## 5. Axis 결정에 대한 의견

| 결정 | 의견 | 근거 |
|---|---|---|
| U (Label Provenance & Perspective) 독립 채택 | **동의.** 단 O와의 경계를 정리할 것을 제안한다. 내 Round 1의 O Sub-axis "Label-subject mismatch as individual-difference signal"은 U로 옮기고, O는 "뇌의 개인차"에 집중한다. 두 Axis를 함께 쓰는 질문(본인 보고 편차와 개인 신경 편차의 대응, GI-P5)은 U × O 조합으로 표기한다 | 0.2 태그와 U의 중복 방지, Deliverable B 2.2절 |
| V (Action Readiness & Affordance) 독립 채택 | 동의. K와의 연결: 행동 경향 변수가 정서 범주를 가로질러 추상 형식(CCGP)으로 표상되는지를 기하로 검정할 수 있다(Emo-FilM Motivation 10항목) | doi:10.1016/j.cell.2020.09.031 |
| W (Internally Generated Experience) 독립 채택 | 동의. Mind captioning 회상 자료로 "지각에서 회상으로 갈 때 정서 기하가 시각 기하보다 더 보존되는가"를 rank별 지각-회상 공유 스펙트럼과 GW로 물을 수 있다(vision-decoding R2의 기하판). 회상 직후 같은 비디오가 재제시되는 설계라 HRF 겹침 처리가 전제다 | doi:10.1126/sciadv.adw1464, arXiv:2409.06843 |
| Information-theoretic Efficiency를 K의 Sub-axis로 | **동의(이견 없음).** 현재 제안자가 나 하나이고, 데이터 경로가 K의 산출물(공유 부분공간)에 의존한다. GI-P6에 llm-semantics와 emotion-theory가 답한 뒤 Round 3에서 A, C와의 교차 태그 여부를 다시 본다 | 2.3절 기록 |
| X를 R의 Sub-axis, Y를 A의 Sub-axis로 | 이견 없음. Y의 privileged access 검정(emotion-theory C4)은 GI-P5 multiverse의 한 기준선(peer 합의)과 같은 설계라 함께 수행할 수 있다 | Deliverable B 2.2절 |
| 외부 분야 목록 | Complex Systems 아래에 "통계물리의 뇌 동역학 지표(엔트로피 생산, detailed balance)"를 명시할 것을 제안한다. 조합 단계의 외부 개념 요건 단위로 쓸 수 있다 | doi:10.1073/pnas.2109889118, doi:10.1126/sciadv.ade6049 |

---

## 6. Coordinator 참고: 독립 수렴 지도 (조합 단계에서 합칠 후보)

| 수렴 주제 | 독립 제안 | 합치는 제안 |
|---|---|---|
| Horikawa 범주 결론 vs Westlin 재현 실패 | GI-C1, ET-C1, ET-C2, SN-Chain 2, AR-D1 | GI-P1 |
| 기대 반응 잔차와 본인 보고 편차(Spacetop) | GI-C3/C8, ET-C4/C8, VD-R5, EF-Chain 3, GC-CH5, LS-Chain 5, SN-I1 | GI-P5 |
| 정서 지도: 유사도 vs 방향성 전이 | GI-C2, BI-Chain 1, AR-D3, MD-Chain 7 | GI-P2 |
| 정서 관성, 이월, 이완 | GI-C5, SN-Chain 5, MD-Chain 1, FA-T5, BI-Chain 7 | GI-P3 |
| In-silico 정서 기하 충실도 | EF-Chain 1, GC-CH3 | GI-P4 |
| arousal 휴대성과 valence 비휴대성 | GI-C3, SN-Chain 1, MD-U6 | GI-P7 |

---

## 7. 새로움 판정에 쓴 검색 경로 (2026-11-12)

| 질문 | 경로와 질의 | 결과 |
|---|---|---|
| 정서 반응의 공유 스펙트럼 | WebSearch "cross-decomposition OR shared variance spectrum OR covariance spectrum emotion fMRI individuals 2025 2026" | 정서 적용 없음. Han & Bonner 2025(시각 경험)와 EmoMind(decoding)만 |
| 정서 동역학의 비가역성 | WebSearch "entropy production broken detailed balance time irreversibility emotion fMRI naturalistic movie affective dynamics" | 정서 적용 없음. 영화 전체 비가역성(doi:10.1126/sciadv.ade6049), 방법(doi:10.1073/pnas.2109889118) |
| 중립 자극 정렬의 정서 운반 | WebSearch "hyperalignment trained on neutral stimuli transfer to emotional stimuli ..." | 미발견. 가장 가까운 Chan 2020(정서 사진 → 예고편), dHA-HMM(doi:10.1007/s12021-022-09568-5) |
| in-silico 기하의 GW 비교 | WebSearch "Gromov-Wasserstein in-silico encoding model predicted fMRI versus observed representational geometry comparison TRIBE" | 미발견 |
| 정서 어휘 IB | WebSearch "information bottleneck emotion categories efficient communication emotion lexicon near-optimal compression 2025 2026" | 미발견. 색, 행동, 시제 영역만. 관련 이론 preprint arXiv:2602.08238(볼록성과 효율의 구분)은 arxiv.org 초록 페이지로 확인해 jsonl에 추가 |
| 영화 후 이완의 개인차 | WebSearch "emotional film offset recovery time constant fMRI individual differences ..." | 부분 선행 Baez-Lugo 2023 발견(C5 판정 수정) |
| 정서 영화의 정렬 + 상태 | PubMed "dHA-HMM naturalistic stimuli evoked emotion changes brain state dynamics" | Tan 2022 발견(C4 판정 수정) |

**미확인으로 남은 것:** Mind captioning 저장소의 실제 파일(캡션, 회상 vividness, events의 제시 순서), 두 코호트의 순서 동일 여부와 피험자 중복, 사용자 전처리 파이프라인의 전역 신호 처리, Thornton 2019 본문(대칭 유사도 통제 방식, PMC 전문이 빈 문자열로 반환), arXiv:2609.15685(arXiv API 응답 없음, 인용하지 않음).
