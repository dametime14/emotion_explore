# Round 3: Constructive Disagreement (multimodal-dynamics 검토)

* 검토자: multimodal-dynamics (Axis D, M 관점)
* 기준일: 2026-11-12
* 절차: `reference/protocols.md` P3. 배정: `outputs/discussion/round3_assignment.md`
* 배정된 제안: **GI-P1**(geometry-info → emotion-theory), **BI-P1**(brain-inspired → geometry-info), **SN-P1**(systems-neuro → encoding-foundation)
* 읽은 원문: 각 제안의 보낸 에이전트 `round2.md` 2절 해당 항목, 근거 chain(geometry-info Round 1 C1, C2와 Round 2 0.2절; brain-inspired Round 1 Chain 1; encoding-foundation Round 1 Chain 2; systems-neuro Round 1 Chain 1), 참조 제안 GI-P2
* 표기: [본문] 원문 확인, [초록] 초록만, [db] `literature_db.csv`의 다른 에이전트 기록, [검색] 검색 색인 수준, [추론] 검토자 추론. 이번 검토에서 새로 확인한 논문 5편을 `literature.jsonl`에 추가했다(10.1016/j.pneurobio.2024.102570, 10.1037/rev0000505, 10.1093/pnasnexus/pgac020, 10.1016/j.neuroimage.2024.120712, 10.1016/j.bpsgos.2026.100721).
* 검색 제약: arXiv API는 Round 2 때 429로 막혀 이번에도 쓰지 않았다(우회하지 않음). 검색은 PubMed MCP와 WebSearch다.

---

## 요약 판정

| 제안 | 이미 연구되었나 | 단순 적용인가 | 신경과학 질문 해결 | 정서 아닌 내용 decoding 위험 | 현 데이터로 검증 | 더 강한 방법 | 기대와 달라도 의미 | 종합 |
|---|---|---|---|---|---|---|---|---|
| GI-P1 | partially (방법은 시각, 영화에 선행; 정서 비디오 적용과 두 코호트 대조는 미발견) | 아니다 | 예(Horikawa vs Westlin 쟁점을 측정 수준에서 판정) | 중간(공유 차원 대부분이 시각-의미일 가능성) | 가능, 단 **두 코호트 제시 순서의 동일 여부가 설계의 성패를 가른다** | 순서, 이월 성분을 명시적 모형 성분으로 | 예 | **조건부 강함**. 순서 확인과 이월 통제를 선행 조건으로 |
| BI-P1 | partially (TEM 무작위 보행, 사고 과제 전이, 휴지기 SR 적용은 있음; 영화 정서 SR 방향성 검정은 미발견) | 아니다 | 예(지도가 유사도인가 예측인가) | 높음(서사의 장면 전이가 정서 전이로 보일 위험) | 가능하나 **방향성 지표의 정의 수정 필요** | 시간 역전 사슬, 전향 vs 후향 decoding 비대칭 | 예(대칭이면 Ma & Kragel 해석이 충분) | **수정 후 강함**. 전치 T' 대신 시간 역전 사슬, 항목별 평정 지연 통제 |
| SN-P1 | partially (공유 생리의 ISC 위험은 지적됨; 생리 반영 ceiling 분해는 미발견) | 아니다 | 예(limbic 맹점의 원인 분해) | 낮음~중간(생리 회귀가 정서 신호를 지울 위험) | 가능(Emo-FilM raw + 생리) | 생리를 자극 예측 가능 성분과 개인 성분으로 나누기, washout에서 결합 커널 추정 | 예 | **강함**. 감각 강도(소리, 휘도) 경로를 추가하면 더 정밀 |

---

## 1. GI-P1. 두 코호트 교차 공유 스펙트럼으로 Horikawa 범주 결론과 Westlin 재현 실패를 판정하기

### 제안 요약
Horikawa 2020(5명)과 Mind captioning(6명)의 55쌍에서 코호트 내 쌍과 코호트 간 쌍의 rank별 공유 스펙트럼(cross-decomposition)을 비교해 "순서, 세션, 프로토콜이 공유한 분산"을 추정하고, Mind captioning 72개 x 6회 노출로 피험자 내 신뢰 스펙트럼을 구해 "재현 가능한 개인 고유 분산"을 rank별로 분리한다. 공유 차원을 규범 정서 평정, 정서 배제 캡션, 시각 feature로 대역별 분할하고, 군집 multiverse를 세 입력 경로에서 반복한다(geometry-info round2.md GI-P1, Round 1 C1).

### 판정 1. 이미 연구되었는가 → **partially**
* 검색(2026-11-12):
  * PubMed: `(Cowen Keltner OR "emotionally evocative videos" OR "2,180 videos" OR "2185 videos") AND fMRI AND emotion AND (dimensionality OR shared OR individual OR reanalysis)`, 2020년 이후 → 정서 비디오 fMRI의 공유 스펙트럼 분석 없음(2건, 무관).
  * WebSearch: `cross-decomposition shared variance spectrum across subjects emotion fMRI power law dimensionality emotional videos individual differences` → 정서 비디오 적용 없음.
* 가장 가까운 선행:
  * 방법: 시각 피질 자연 이미지의 scale-free 공유 스펙트럼(arXiv:2409.06843, 출판본 10.1371/journal.pcbi.1013714 [db]), 영화 시청 개인차의 고차원 구조(Han & Bonner 2025, arXiv:2505.12653 [db, 검색 요약: 영화 4편, 정서 목적 선택 아님]).
  * 데이터: 두 코호트를 함께 쓴 연구는 있다. EmoMind(arXiv:2605.16739 [db])는 Mind captioning으로 학습하고 Horikawa 2020을 교차 데이터셋 평가에 썼다(vision-decoding Round 1 0.1절). 즉 "두 코호트 결합" 자체는 새롭지 않고, **공유 스펙트럼으로 코호트 내와 코호트 간 공유를 대조하는 것**이 새롭다.
  * 학회 초록 "Shared high-dimensional latent structure neural mental"(Gauthaman 2025, CCN) [검색]이 있으나 정서 비디오 여부는 미확인.

### 판정 2. 단순한 모델 적용인가 → **아니다**
코호트 간 쌍을 "순서, 세션, 프로토콜을 공유하지 않는 쌍"으로 쓰는 설계 논리가 핵심 기여다. 다만 이 논리는 **두 코호트의 제시 순서가 다를 때만** 성립한다(판정 5).

### 판정 3. 실제로 Neuroscience Question을 해결하는가 → **예, 조건부**
Horikawa 2020의 "고차원 범주 공유"와 Westlin 2025의 "개인 특이, 평정 대응 없음"(arXiv:2507.00320 [db])이 서로 다른 rank 대역을 본 것인지, 세션/run 성분(NMI 0.19, 0.17) 때문인지를 측정 수준에서 가른다. 결론이 어느 쪽이든 정서 표상의 공유 대 개인 특이 논쟁에 직접 답한다.

### 판정 4. 정서 이외의 요소를 decoding하는 것은 아닌가 → **위험 중간**
공유 스펙트럼의 상위 rank는 시각-의미 내용이 지배할 가능성이 크다. 제안은 정서 배제 캡션과 시각 feature로 대역별 분할을 하므로 방향은 맞다. 내 관점에서 두 가지가 빠져 있다.
1. **시간 feature 부재:** 비디오 자극이므로 움직임 에너지, 컷, 루프 재생(짧은 비디오 반복)이 공유 분산을 만든다. 정적 시각 feature만으로는 이 몫이 정서 쪽에 남는다. V-JEPA 2 같은 비디오 모델 feature나 움직임 에너지를 통제 변수에 넣어야 한다.
2. **이월 성분:** 같은 순서를 본 코호트 안의 피험자들은 "직전 클립의 정서와 시각 내용"까지 공유한다. 이 공유는 정서처럼 보이지만 현재 클립의 정서가 아니다(내 Round 1 Chain 1, MD-P1, GI-P3).

### 판정 5. 현재 Dataset으로 검증할 수 있는가 → **가능, 단 선결 확인 2개**
* (a) **두 코호트의 학습 세션 제시 순서가 같은가.** Mind captioning 논문 Methods는 "2,180개를 pseudorandom 순서로 1회, 이 순서는 모든 피험자에게 같다"고만 적었고 Horikawa 2020과의 관계는 적지 않았다(내가 PMC 전문으로 확인, 10.1126/sciadv.adw1464). 같은 저자이므로 같은 순서를 재사용했을 가능성이 있다. **같은 순서라면 코호트 간 쌍도 순서 효과를 공유하므로, "코호트 내 - 코호트 간" 차이는 순서가 아니라 스캐너, 세션 날짜, 전처리 차이만 반영한다.** 사용자가 두 데이터셋을 모두 보유하므로 events 파일 대조로 바로 확인할 수 있다. 두 코호트 순서가 달라도 Mind captioning에는 평가 블록이 무작위로 끼어 있고 짧은 비디오의 반복 재생 기준(Mind captioning 10 s, Horikawa 2020 8 s)이 달라 국소 순서와 간격이 다르다.
* (b) **피험자 중복 여부**(제안자가 이미 지적). 
* 그 밖: Mind captioning 72개 테스트 클립은 학습 세션 1회 + 테스트 5회 = 6회 노출이다. 피험자 내 신뢰 스펙트럼은 **반복 노출 상태**에서 추정되고, 피험자 간 공유 스펙트럼(학습 세션)은 첫 노출 상태다. 정서 반응은 반복에 따라 습관화되므로 두 스펙트럼의 차이에 "노출 횟수" 효과가 섞인다(axis 태그 제안: 시청 이력, 내 round2.md 5절).

### 판정 6. 더 강력한 모델이나 분석 방법이 있는가 → **있다 (보완)**
1. **순서와 이월을 명시적 성분으로:** 공유 분산을 (현재 클립 성분) + (이월 성분: t-1, t-2 클립 feature와 라벨) + (세션, run drift)로 나누는 모형을 같이 적합한다. 이월 성분은 Mind captioning 테스트 세트(같은 클립, 다른 선행 클립)에서 식별된다.
2. **노출 횟수 층화:** 72개 테스트 클립의 신뢰 스펙트럼을 반복 1~2회와 4~5회로 나눠 추정하고, 개인 고유 성분이 반복에 따라 줄어드는지 본다.
3. **동역학 쪽 대조(선택):** 공유 스펙트럼은 블록 평균 공간 패턴의 기하다. 같은 rank 대역에서 블록 내 시간 경과(TR 1 s인 Mind captioning)의 공유 정도를 함께 보면 "공유 기하 + 개인별 시점" 가설(geometry-info Round 1 P4)과 연결된다.

### 판정 7. 결과가 기대와 달라도 과학적으로 유의미한가 → **예**
* 코호트 간에서도 정서 고유 공유 차원이 남으면 Horikawa 2020 결론의 가장 강한 지지(순서, 세션 무관).
* 코호트 간에서 정서 고유 공유가 사라지면 "정서 공유"의 상당 부분이 프로토콜, 순서 성분이라는 결론이며 Westlin 2025 해석을 지지한다.
* 개인 고유 재현 성분이 없으면 Westlin의 "구조화된 개인 변동"이 잡음일 가능성. 어느 쪽이든 정서 fMRI 분석 관행에 직접 영향.

### 수정안
1. **선행 단계 0 추가:** 두 코호트 events 파일로 학습 세션 순서, 블록 길이, 평가 블록 위치를 대조하고 결과에 따라 설계를 분기한다. 순서가 같으면 "코호트 간 = 순서 통제"라는 해석을 버리고 "코호트 간 = 스캐너, 프로토콜, 전처리 통제"로 이름을 바꾼다. 순서 효과는 대신 Mind captioning 테스트 세트의 무작위 순서로 추정한다.
2. 대역별 분할의 통제 변수에 비디오 시간 feature(움직임 에너지, 컷, 루프 반복 수, 비디오 모델 feature)와 이월 회귀자(t-1, t-2)를 추가한다.
3. 피험자 내 신뢰 스펙트럼을 노출 횟수별로 층화해 보고한다.
4. 두 코호트를 raw에서 같은 전처리로 맞춘다(Mind captioning 전처리본은 회백질 전역 신호를 회귀했다; geometry-info round2.md 0.2절). Bolt 2025의 자율신경성 전역 성분(10.1038/s41593-025-01945-y [db])이 한 코호트에서만 제거되면 코호트 간 공유가 인위적으로 달라진다.
* 태그: label-provenance 스펙트럼 자체는 라벨 비의존, 해석 단계는 perceived/felt 혼합 / 별도 평정자 규범(MTurk), 캡션은 기술 의미 / 별도 평정자(정서 배제 지시). evidence-level R0. G1 핵심 분석 불필요, 시간 feature 통제는 필요(보유). overlap: EmoViS (부분), EmoBrain (약함).

---

## 2. BI-P1. 정서 지도의 방향성 검정: successor geometry 통합안

### 제안 요약
Emo-FilM 1 Hz consensus에서 영화별 방향성 전이 행렬 T를 추정하고, 뇌(전후 hippocampus, vmPFC)가 SR(T)를 SR(T')(전치)보다 더 잘 따르면 "예측 방향" 증거로 본다. 식별 가능성 시뮬레이션 → 실제 비교 → 할인율 γ의 장축 위계 순서로 geometry-info와 공동 사전등록한다(brain-inspired round2.md BI-P1, Round 1 Chain 1; geometry-info Round 1 C2).

### 판정 1. 이미 연구되었는가 → **partially**
* 검색(2026-11-12):
  * PubMed: `"successor representation" AND (emotion OR emotional OR affective OR mood OR valence)` → 2건. Li et al. 2024 (10.1016/j.pneurobio.2024.102570 [초록]): **휴지기 fMRI 뇌 상태 전이에 SR 모형을 적용**, 예측적 전이가 정서 평가와 공변. Zhou et al. 2025 (10.1037/rev0000505 [초록]): TCM-SR 이론 모형(정서 조절 포함, 시뮬레이션).
  * WebSearch: `successor representation emotion transitions hippocampus vmPFC fMRI predictive map affective states 2025 2026` → Ma & Kragel(TEM)과 그 preprint, 시각 서열 학습의 SR fMRI(bioRxiv 2022, [검색])만.
* 선행 지도: Ma & Kragel 2026은 TEM을 대칭 상관-MDS 위 균등 무작위 보행으로 학습했다(10.1038/s41467-025-68240-z Methods [본문, 내 Round 1 확인]). Thornton, Weaverdyck, Tamir 2019(10.1523/JNEUROSCI.1431-18.2018 [db])는 정신상태 사고 과제에서 현재 패턴이 가능성 높은 미래 상태를 닮는다고 보고했다. Li 2024는 SR을 fMRI 상태 전이에 적용한 **방법 수준 선행**이지만 정서 내용 상태와 영화 자극은 아니다.
* 결론: "영화 정서 전이로 만든 SR과 그 방향성 대조로 hippocampus-vmPFC 정서 표상을 검정"한 연구는 찾지 못했다. 판정은 제안자와 같은 partially.

### 판정 2. 단순한 모델 적용인가 → **아니다**
대칭 성분을 같게 둔 방향성 대조는 Ma & Kragel의 해석(전이 통계 학습)을 직접 반증 가능하게 만드는 설계다.

### 판정 3. 실제로 Neuroscience Question을 해결하는가 → **예**
"해마-전전두 정서 지도는 대칭 유사도 구조인가, 미래 정서의 예측 구조인가"는 Round 1에서 3개 에이전트가 독립적으로 꼽은 공통 미해결 문제다(axis_encyclopedia 0.3절).

### 판정 4. 정서 이외의 요소를 decoding하는 것은 아닌가 → **위험 높음**
영화에서 정서 전이는 **서사의 장면 전이**와 강하게 묶여 있다. 뇌가 SR(T)를 더 잘 따르는 이유가 "정서 상태의 예측"이 아니라 "장면, 사건 순서의 예측"일 수 있다. Lee 2021(10.7554/eLife.64972 [본문])은 사건 패턴 자체의 예측 앞당김을 보였다. 정서 상태 대신 **내용 상태(장면 caption embedding이나 비디오 feature를 같은 수로 군집화한 상태)로 만든 SR**을 경쟁 모형에 넣어야 한다.

### 판정 5. 현재 Dataset으로 검증할 수 있는가 → **가능, 단 방향성 지표 정의와 평정 지연 문제를 먼저 풀어야**
1. **전치 T'는 시간 역전 사슬이 아니다 [추론, 표준 Markov 연쇄 성질].** 행 정규화된 전이 행렬 T의 전치는 일반적으로 확률 행렬이 아니며, T와 T'의 차이는 방향성 흐름뿐 아니라 **상태 점유율(정상분포 π)의 비균등**에서도 생긴다. 시간 역전 사슬은 T̃ = D_π⁻¹ T' D_π (D_π = diag(π))다. 사슬이 detailed balance를 만족하면 T̃ = T이고 SR(T) = SR(T̃)라서 방향성 검정은 원리적으로 0의 차이를 내야 한다. 즉 SR(T) 대 SR(T')의 차이는 "자주 나오는 정서와 드문 정서"의 차이를 방향성으로 오인할 수 있다. 비교 대상은 SR(T̃)여야 하고, 방향성의 크기는 GI-P2의 반대칭 흐름과 엔트로피 생산으로 먼저 측정해야 한다.
2. **항목별 평정 지연이 가짜 방향성을 만든다.** Emo-FilM에서 각 항목은 서로 다른 평정자 조합 3~4명이 평정했다(평정자 1명당 항목 6개 무작위 배정, Ma & Kragel Methods [본문]). 항목마다 평정 반응 지연이 다르면(예: Fear 평정자가 Relief 계열 평정자보다 빠르면) 같은 순간의 사건이 consensus에서는 "Fear → 안도"라는 순서로 나타난다. 이것은 경험된 전이가 아니라 측정 지연의 산물이다. 평정자 반복 시청(최대 6회)에 따른 예측적 앞당김(Lee 2021)도 항목마다 다를 수 있다.
3. 전이 행렬은 **어떤 한 사람의 경험된 전이도 아니다.** 시점 t의 상태 벡터가 항목별로 다른 평정자 집단의 consensus로 조합되기 때문이다(제안자는 "fMRI 참가자 경험이 아니다"까지만 적었다).
4. HRF는 인과적이고 비대칭인 커널이라 BOLD 궤적에 방향성을 더한다(GI-P2 반론 (a)와 같음).

### 판정 6. 더 강력한 모델이나 분석 방법이 있는가 → **있다**
1. **SR(T) 대 SR(T̃)** 비교로 바꾸고, 방향성 크기(반대칭 흐름, 엔트로피 생산, GI-P2)가 0과 구분될 때만 신경 비교로 넘어간다.
2. **전향 vs 후향 decoding 비대칭(SR 비의존 검정):** hippocampus, vmPFC 패턴(HRF 정렬 후)으로 t+k의 정서 상태를 decoding한 성능과 t-k를 decoding한 성능을, 현재 상태 t를 통제한 뒤 비교한다. 같은 k에서 미래 쪽이 일관되게 높으면 예측 부호화 증거다. 평정 지연과 HRF는 두 방향에 같은 이동을 주므로 ±k 대칭 비교가 일부 상쇄한다. SR 모형 가정(γ, 상태 이산화)에 의존하지 않는다는 장점이 있다.
3. **내용 SR 대조:** 정서 상태 SR, 내용 상태 SR, 둘의 결합을 같은 상태 수로 경쟁시킨다(판정 4).
4. **지연 정렬:** 항목별 평정 지연을 공통 자극 사건(컷, 음악 stem onset, 효과음)에 대한 교차상관으로 추정해 정렬한 consensus와 정렬하지 않은 consensus 양쪽에서 T를 추정하고, 방향성 결과가 정렬에 견고한지 보고한다.

### 판정 7. 결과가 기대와 달라도 과학적으로 유의미한가 → **예**
* SR(T)와 SR(T̃)가 구분되지 않으면(그리고 시뮬레이션상 검정력이 충분하면) "Ma & Kragel의 지도는 대칭 유사도 구조로 충분하다"는 결론이 되고, 이는 TEM의 "전이 학습" 해석을 약화한다.
* 평정 consensus 자체에 방향성이 거의 없으면(detailed balance에 가까우면) 영화 평정 데이터로는 정서 전이의 방향성 질문을 다룰 수 없다는 **측정 수준의 결론**이 나온다. 이 경우 같은 참가자의 경험 표집이 필요하다는 근거가 된다(Thornton & Tamir 2017, 10.1073/pnas.1616056114 [db]의 일상 전이 데이터가 대안).

### 수정안
1. 방향성 대조를 SR(T) 대 **SR(T̃, 시간 역전 사슬)**로 바꾼다. 단계 0으로 consensus 전이의 반대칭 흐름과 엔트로피 생산을 bootstrap 구간과 함께 보고한다(GI-P2와 통합).
2. 항목별 평정 지연 추정과 정렬을 전처리 단계로 넣고, 정렬 전후 결과를 함께 보고한다. 평정자별 원자료에 평정 순서(첫 시청 여부)가 기록되어 있으면 첫 시청 평정자만으로 만든 전이도 비교한다.
3. SR 비의존 검정으로 **전향 vs 후향 decoding 비대칭**을 1차 결과로 두고, SR 모형 비교는 2차로 둔다.
4. 내용 상태 SR을 경쟁 모형에 추가한다.
5. Horikawa를 음성 대조로 쓰자는 원안은 유지하되, Horikawa는 클립 순서가 무작위라 "생태적 전이 없음"의 대조이지 "전이 없음"의 대조는 아니다(인접 클립 사이 이월은 있을 수 있다, MD-P1).
* 태그: label-provenance perceived/felt 혼합 / 별도 평정자 규범(z-score 상대값, 항목마다 다른 평정자, 반복 시청자). evidence-level R0. G1: 정서 SR은 불필요, 내용 SR 대조는 필요(보유). overlap: Emo-FilM 연구 (시간 정보, 약함).

---

## 3. SN-P1. 생리 반영 noise ceiling과 전역 자율신경 성분으로 limbic 맹점 분해

### 제안 요약
encoding-foundation Chain 2(자극 구동 encoder의 limbic 맹점이 잡음인가, 몸인가, 평가인가)를 (1) Emo-FilM ISC 상한을 raw BOLD와 생리 회귀 BOLD 두 판으로 계산해 '자극 구동 생리 성분'을 분리하고, (2) 생리의 역할을 잡음 회귀, 전신 상태 예측자, 남는 신경 분산으로 셋으로 나누고, (3) 제공 전처리본의 WM/CSF 회귀를 쓰지 않고, (4) 영역별 dropout과 tSFNR을 보고해 검증, 확장한다(systems-neuro round2.md SN-P1).

### 판정 1. 이미 연구되었는가 → **partially**
* 검색(2026-11-12):
  * PubMed: `(intersubject correlation OR inter-subject correlation OR "noise ceiling") AND (heart rate OR cardiac OR physiological OR respiration) AND fMRI AND (movie OR film OR naturalistic)`, 2018년 이후 → 9건. 관련: Bacha-Trams 2024 (10.1016/j.neuroimage.2024.120712 [초록]): 관계 친밀도에 따른 ISC 차이가 안구 운동, 정서 경험, 생리 활동 유사도로 설명되지 않음. Koch 2026 (10.1016/j.bpsgos.2026.100721 [초록]): 사회불안 집단의 동적 ISC 차이가 자율 각성, 동공 차이 없이 나타남. 생리 반영 ceiling 분해는 없음.
  * WebSearch: `intersubject correlation physiological noise cardiac respiration shared stimulus-locked inflate ISC naturalistic fMRI RETROICOR emotional movie` → 정서 자극에서 말초 생리가 피험자 간 동기화될 수 있어 ISC를 부풀릴 수 있다는 지적(Nastase 2019, 10.1093/scan/nsz037 [db, 검색])은 있으나 RETROICOR 전후 ISC 비교는 없음.
* 전제 수준 선행: 심박의 자극 동기화(Madsen & Parra 2022, 10.1093/pnasnexus/pgac020 [초록 일부]), 전역 신호의 자율신경 결합(Bolt 2025, 10.1038/s41593-025-01945-y [db]).
* 결론: 제안자 판정(전제는 선행, 분해는 no → partially)에 동의한다. 다만 Bacha-Trams 2024처럼 "생리 유사도가 ISC 차이를 설명하지 않았다"는 결과가 있으므로, **보정 효과가 작을 수 있다는 반대 증거**를 예상 결과에 넣어야 한다.

### 판정 2. 단순한 모델 적용인가 → **아니다**
noise ceiling의 정의 자체를 생리 성분에 따라 둘로 나누는 측정론적 기여다. encoder 성능의 '분모'를 바꾸므로 encoding-foundation U2의 핵심(잡음 대 feature 결핍)을 직접 다룬다.

### 판정 3. 실제로 Neuroscience Question을 해결하는가 → **예**
limbic 영역에서 자극 구동 encoder가 약한 이유가 (a) 낮은 SNR, (b) 몸 상태 정보 부재, (c) 규범적 평가 정보 부재 중 무엇인지는 TRIBE v2 이후 in-silico 정서 연구 전체의 전제다. 결과는 정서 encoding 모형에 생리 입력이 필요한지(Physiology-augmented Encoding Sub-axis)를 결정한다.

### 판정 4. 정서 이외의 요소를 decoding하는 것은 아닌가 → **위험 낮음~중간, 방향이 반대**
이 제안의 위험은 정서 아닌 것을 정서로 읽는 쪽이 아니라 **생리 회귀가 정서 관련 신경 신호까지 지우는 과잉 보정** 쪽이다(제안자 반론 1). 내 관점에서 한 가지 경로가 더 있다: 영화의 **갑작스러운 소리와 밝기 변화**는 (i) 놀람 반응으로 심박, EDA를 움직이고 (ii) 감각 피질과 각성 관련 BOLD를 직접 움직인다. 생리를 회귀하면 이 감각 구동 BOLD 일부가 함께 빠지고, 생리를 회귀하지 않으면 감각 강도가 '몸' 성분으로 보인다. 감각 강도를 별도 경로로 넣지 않으면 세 성분 분해가 섞인다(내 round2.md SN-P2 응답 2번과 같은 논리).

### 판정 5. 현재 Dataset으로 검증할 수 있는가 → **가능**
Emo-FilM은 raw BOLD와 fMRI 참가자 PPG, 호흡, EDA(1000 Hz, 전 런)가 공개되어 있다(Stage 1). 주의:
* TR 1.3 s라 심장 신호는 aliasing된다. RETROICOR류 위상 회귀는 가능하나, 심박 변화율, 호흡량 같은 느린 생리 회귀자는 지연 반응함수와 함께 넣어야 한다(제안 2(b)).
* 제공 전처리본의 high-pass(sigma 50 s, geometry-info C5)는 느린 전신 성분을 이미 일부 제거했다. raw 재전처리가 맞다(제안 3).
* Mind captioning 반복 기반 상한은 생리가 없어 비교 대상이 다르다(자극과 획득 조건이 모두 다름). 보조 결과로만 둔다.
* 생리는 fMRI 참가자, 50항목 평정은 별도 평정자라 주체가 다르다(제안자 명시).

### 판정 6. 더 강력한 모델이나 분석 방법이 있는가 → **있다 (보완 두 가지)**
1. **생리를 '자극 예측 가능 성분'과 '개인 성분'으로 먼저 나누기:** 참가자 심박, EDA 시계열을 자극 feature(음량, 음악, 음성, 효과음 stem 에너지, 휘도, 움직임 에너지, 컷)로 예측하는 encoder를 참가자 간 교차검증으로 학습한다. 예측되는 몫은 '자극이 만든 공유 생리'(ISC 상한을 부풀리는 성분), 남는 몫은 '개인 몸 상태'다. 그러면 ceiling 보정은 앞쪽 성분만, 잔차 분석의 '몸' 설명 변수는 뒤쪽 성분만 쓴다. 이렇게 해야 Chain 2의 '몸'이 "자극으로 계산 불가능한 몸 상태"라는 뜻을 갖는다.
2. **결합 커널을 자극 없는 구간에서 추정하기:** 생리 → BOLD 전달 함수(지연 반응함수)를 Emo-FilM의 영화 전후 90 s washout(고정점, 무음)에서 추정하고, 영화 중에는 그 커널로 예측한 성분만 제거한다. 영화 중에 커널을 추정하면 자극이 생리와 BOLD를 동시에 움직여 커널에 자극 효과가 섞이는 순환 문제가 생긴다. washout은 geometry-info GI-P3, 내 MD-P1에서도 쓰므로 같은 전처리를 공유할 수 있다.

### 판정 7. 결과가 기대와 달라도 과학적으로 유의미한가 → **예**
* 생리 반영 전후 ceiling이 거의 같으면: limbic 맹점은 공유 생리 때문이 아니다. 남는 후보는 SNR(dropout, tSFNR)과 평가 정보 부재로 좁혀진다.
* ceiling이 크게 줄면: 지금까지 보고된 limbic 정서 encoding의 일부가 자극 동기화 생리를 실어 왔다는 측정 수준의 경고가 된다.
* 생리의 개인 성분이 limbic 잔차를 설명하면 Physiology-augmented Encoding이 필요하다는 근거, 설명하지 못하면 '몸' 가설의 약화. 어느 쪽이든 결론이 선다.

### 수정안
1. 단계 0: 생리 시계열을 자극 feature encoder로 '자극 예측 가능 성분'과 '개인 성분'으로 분해하고, 각 성분의 참가자 간 ISC를 보고한다.
2. 생리-BOLD 결합 커널은 washout에서 추정해 영화 구간에 적용한다(순환 방지). 영화 중 추정 커널과의 차이도 보고한다.
3. 감각 강도 경로(음원별 음량, 휘도, 움직임 에너지)를 세 성분 분해에 넣어 네 성분(감각 강도, 자극 구동 생리, 개인 생리, 남는 신경)으로 확장한다.
4. 예상 결과에 "보정 효과가 작을 수 있다"(Bacha-Trams 2024, Koch 2026)를 명시하고, 효과가 작을 때의 해석(맹점은 SNR이나 평가 정보 쪽)을 사전 등록한다.
5. 결과를 영역별 dropout 마스크, tSFNR과 함께 보고하자는 원안 4번을 유지하고, TRIBE v2 공개판이 피질 전용이라는 점(encoding-foundation Round 1 0절) 때문에 in-silico 비교는 피질 limbic 인접 영역(섬엽, vmPFC, ACC)으로 한정한다.
* 태그: label-provenance 50항목 perceived/felt 혼합 / 별도 평정자 규범, 생리는 참가자 본인 측정(라벨 아님). evidence-level R0, TRIBE v2 예측 비교는 insilico-vs-observed 혼합. signal-feasibility 필수(raw 재전처리, 개인별 amygdala dropout). G1: 감각 강도 feature 추출에 필요(보유). overlap: Emo-FilM 연구 (부분).

---

## 4. 세 제안을 가로지르는 공통 관찰

1. **세 제안 모두 Emo-FilM의 washout, raw 재전처리, 생리 처리를 공유한다.** GI-P3, MD-P1, SN-P1, SN-P2가 같은 전처리 분기(raw, high-pass 완화, WM/CSF 회귀 없음, 생리 커널은 washout에서 추정)를 필요로 하므로 공통 전처리 한 벌을 만들 것을 Coordinator에게 제안한다.
2. **평정 consensus의 측정 출처가 세 제안의 공통 약점이다.** 항목마다 다른 평정자 조합, 평정자 내 z-score, 최대 6회 반복 시청은 BI-P1(가짜 방향성), GI-P1(해석 단계), SN-P1(평가 성분)에 각각 다른 방식으로 작용한다. Axis U(Label Provenance)에 "시청 이력"과 "평정 시점" 속성을 추가하자는 내 round2.md 5절 제안의 구체적 사례다.
3. **Horikawa 2020과 Mind captioning의 제시 순서 대조**는 GI-P1, MD-P1, FA-P3 세 제안의 공통 선결 조건이다. 사용자 보유 데이터의 events 파일 대조만으로 확인할 수 있으므로 Stage 4 이전에 먼저 처리할 것을 권한다.
