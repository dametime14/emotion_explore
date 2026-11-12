# Round 3 (Constructive Disagreement): encoding-foundation 검토

* 작성: encoding-foundation
* 기준일과 검색일: 2026-11-12
* 절차: `reference/protocols.md` P3. 배정은 `outputs/discussion/round3_assignment.md`를 따른다.
* 검토 대상: **BI-P2**(brain-inspired → frontier-ai), **MD-P1**(multimodal-dynamics → geometry-info), **SN-P3**(systems-neuro → brain-inspired)
* 읽은 원문: 각 제안의 `round2.md` 해당 절, 근거 chain(brain-inspired round1 Chain 2와 Chain 3, multimodal-dynamics round1 Chain 1, geometry-info round1 C5), Mind captioning 원문 Methods(doi:10.1126/sciadv.adw1464, PMC 전문을 PubMed 도구로 열람)
* 검색 경로와 제약: PubMed(MCP `search_articles`, `get_article_metadata`), `outputs/literature/literature_db.csv`. arXiv는 export API가 429를 냈고, arxiv.org 웹 검색은 이 시점에 모든 질의에 "Sorry, your query" 응답을 내서 쓸 수 없었다. 우회하지 않았으므로 **arXiv preprint의 선행 수행 여부는 이번 검토에서 확인되지 않았다**. 새로 확인한 논문은 `literature.jsonl`에 추가했다(PubMed 경로, 대부분 abstract_only).
* 표기: evidence-level(R0~R4), label-provenance, insilico-vs-observed는 axis_encyclopedia 0.2절을 따른다.

---

## 1. BI-P2: Axis V 경쟁 검정 (정서 범주 vs 행동 경향 vs 자극 계산 affordance)

**제안 요지:** banded ridge에 band 넷을 넣는다. (a) 정서 범주(Emo-FilM discrete 13, Horikawa 34), (b) 인간 평정 행동 경향(Emo-FilM Motivation 10), (c) LAPA latent action, (d) 의미 통제(정서 배제 캡션)다. 그다음 transmodal 범주 고유 분산이 행동 경향 band로 얼마나 대체되는지 본다. 0단계는 평정 수준 공선성 확인이다.

### 1.1 이미 연구된 것은 아닌가
* **검색:** PubMed `(action tendency OR action readiness OR motivation component) AND emotion AND fMRI AND (film OR movie OR naturalistic) AND (encoding OR component process)`(2018~)과 `(Morgenroth E[Author] OR "Emo-FilM") AND (emotion OR fMRI)`(2023~), 2026-11-12.
* **결과:**
  * Morgenroth et al. 2026(doi:10.1037/emo0001619, 초록)은 Emo-FilM 평정에서 이산 정서 13개 모두가 성분(appraisal, motivation, expression, physiology, feeling)으로 잘 예측된다고 보고했다. 행동 수준이며 뇌 분석은 없다.
  * 성분 네트워크 fMRI는 Mohammadi et al. 2023(doi:10.1093/cercor/bhad093)과 Leitão et al. 2020(doi:10.1371/journal.pbio.3000900)에 있다(둘 다 DB 기록 기준 초록).
  * Chan et al. 2026(doi:10.1002/hbm.70617)은 Emo-FilM 정서 기반 gradient로 개인차를 보았고 경쟁 검정은 아니다.
  * 이산 정서 band와 행동 경향 band, 자극 계산 affordance를 같은 encoding에서 직접 경쟁시킨 연구는 찾지 못했다.
* **판정: partially.** 성분 신경 표상과 평정 수준 대체 가능성은 선행이 있다. 뇌 수준 직접 경쟁은 미발견이다(arXiv 미확인 단서).

### 1.2 단순한 모델 적용에 불과한가
* 경쟁 설계 자체는 이론 검정이라 단순 적용이 아니다.
* 그러나 (c) latent action band는 단순 적용에 가깝고, 무엇을 재는지가 불분명하다. LAPA는 조작 영상 프레임 쌍의 변화로 학습되었다(arXiv:2410.11758). 그래서 영화에서는 카메라 운동, 편집 컷, 인물의 **묘사된 행동**(portrayed action)이 latent action을 지배할 가능성이 크다. 이 band가 이기더라도 "관객의 행동 경향"이 아니라 "화면 속 운동"을 뜻할 수 있다.

### 1.3 실제로 Neuroscience Question을 해결하는가
* 질문("transmodal 정서 분산은 범주인가, 행동 준비인가")은 Horikawa 2020 Discussion 2째 단락의 "emotional experience (or affordances)" 해석을 직접 겨냥하므로 의미가 있다(doi:10.1016/j.isci.2020.101060).
* 다만 두 band가 모두 별도 평정자 규범 평정이라, 결과는 "규범적 범주 기술과 규범적 행동 경향 기술 중 어느 쪽이 뇌 분산을 더 운반하는가"에 대한 답이다. 관객 본인의 행동 준비 상태에 대한 답은 아니다.
* Morgenroth 2026이 보인 높은 상호 예측성 때문에 질문이 **식별 불가능**할 위험이 있다. 이것이 가장 큰 약점이다.

### 1.4 정서 이외의 요소(visual, semantic)를 decoding하는 것은 아닌가
* 위험이 높다. 위협 장면이 있으면 회피 경향 평정이 오르므로 Motivation 평정은 장면 내용과 강하게 공선적이다.
* (d) 의미 통제는 Mind captioning 쪽에서는 인간 중립 캡션, Emo-FilM 쪽에서는 MLLM 캡션(AI 추정)이라 두 데이터셋의 통제 수준이 다르다.
* 측정 오차가 있는 의미 공변량은 증분 타당도 위양성을 만든다(doi:10.1371/journal.pone.0152719). 의미 통제가 불완전하면 "행동 경향 고유 분산"이 의미 잔여를 대신 운반할 수 있다.

### 1.5 현재 Dataset으로 검증할 수 있는가
* **Emo-FilM: 가능.** Motivation 10항목이 있고 30명, 14편이며 leave-one-film-out으로 분할한다. 다만 항목별로 평정자 집단과 신뢰도가 다르므로(평정자 쌍 상관 항목별 0.21~0.60, Stage 1) band 간 신뢰도 비대칭을 보정해야 한다.
* **Horikawa와 Mind captioning:** 행동 경향 라벨이 없다. 신규 인간 평정(R2 비용)이나 MLLM 주석(AI 추정)이 필요하므로 2순위로 둔다.

### 1.6 더 강력한 모델이나 분석 방법
1. **판별 자극 선택(controversial selection):** 전체 시계열 분산 분할보다, 범주와 행동 경향이 갈리는 구간을 골라 검정하는 편이 식별력이 높다(doi:10.1038/s41467-024-53147-y Discussion의 controversial selection, doi:10.1073/pnas.1912334117). 예를 들어 같은 부정 valence에서 접근형(anger)과 회피형(fear) 구간, 같은 긍정에서 접근 욕구형과 비접근형(awe, 감탄) 구간을 Emo-FilM 평정으로 뽑는다. 범주 이론은 범주 간 차이를, 행동 경향 이론은 접근 대 회피 축의 차이를 예측한다.
2. **자극 계산 기준선을 latent action 대신 TRIBE v2 예측으로:** 장면 운동과 의미를 함께 담는 in-silico 예측 반응(arXiv:2605.04326)을 nuisance로 먼저 넣는다. 그 위에서 범주 band와 행동 경향 band의 증분을 비교한다. latent action은 선택 band로만 남긴다.
3. **신뢰도 반영 분할:** 평정자별 원자료로 항목 신뢰도를 추정하고, 신뢰도로 감쇠를 보정한 비교를 한다(adversarial-reviewer D2 논리).

### 1.7 결과가 기대와 달라도 의미가 있는가
* 행동 경향 band가 범주 고유 분산을 흡수하면, 기능주의 action-readiness 해석이 유리해진다.
* 범주 band가 남으면, 범주가 행동 준비로 환원되지 않는다는 근거가 된다.
* 두 band 모두 TRIBE 기준선 위에서 증분이 없으면, transmodal '정서' 분산이 자극 계산 가능하다는 결과가 된다.
* 0단계에서 공선성이 매우 높아(예: 교차 예측 R²가 평정 신뢰도 상한에 근접) 판별이 불가능하면, 그것 자체가 "Emo-FilM 평정 체계로는 두 이론을 구별할 수 없다"는 측정 결과다.
* 모두 의미가 있다. 단 마지막 경우는 사전에 판정 기준을 정해 두어야 한다.

### 1.8 수정안
* 0단계(평정 수준): 항목별 split-rater 신뢰도와 discrete↔Motivation 교차 예측 R²를 함께 계산한다. 교차 예측 R²가 신뢰도 상한의 90%를 넘으면 뇌 수준 분할을 중단하고 1단계로 간다.
* 1단계(판별 구간): Emo-FilM에서 valence와 arousal을 맞추고 접근 대 회피가 갈리는 구간 쌍을 미리 고정한다. 영역별 RSA로 범주 구조와 접근-회피 구조를 맞대 비교한다.
* 2단계(분할): nuisance로 TRIBE v2 예측을 먼저 넣고, 범주, 행동 경향, 의미 band의 중첩 증분을 낸다. latent action은 탐색 band로 두고 "portrayed action feature"로 표기한다.
* label-provenance: 범주와 Motivation은 felt / 별도 평정자 규범, latent action과 캡션은 자극 feature(portrayed), MLLM 캡션은 AI 추정. evidence-level: R0. insilico-vs-observed: 혼합(TRIBE 기준선).

---

## 2. MD-P1: 클립 사이 이월과 washout 이완을 하나의 이완 모형으로

**제안 요지:** 짧은 간격 이월(Horikawa 2020, Mind captioning, 초 단위)과 영화 후 washout 이완(Emo-FilM, 수십 초)을 같은 정서 잠재 차원 위의 leaky integrator 또는 line-attractor식 이완 모형으로 적합한다. 두 척도의 시간상수가 일관되면 '정서 관성 차원'의 증거로 본다.

### 2.1 이미 연구된 것은 아닌가
* **검색:** PubMed `(carry-over OR carryover OR spillover OR lingering OR inertia) AND (emotion OR emotional OR affective) AND fMRI AND (film OR movie OR clips OR video)`(2010~), 2026-11-12.
* **결과:** 분 단위 이월에는 선행이 있다.
  * Pichon et al. 2015(doi:10.1093/scan/nsu044, 초록): 정서 영화 클립 중 편도체 누적 반응이 이후 공포 얼굴에 대한 편도체 반응 변화를 예측했다. 부정은 증가, 긍정은 감소였다. 제안자의 인용 목록에 없던 논문이다.
  * Gaviria et al. 2021(doi:10.1002/hbm.25277)과 2021(doi:10.1016/j.neuroimage.2021.118377): 영화 후 휴지기 CAP 이월.
  * Borchardt et al. 2018(doi:10.1093/cercor/bhx290): 슬픈 영화 후 FC 이월.
  * Tambini et al. 2017(doi:10.1038/nn.4468): 정서 상태의 기억 부호화 이월.
  * 초 단위 클립 간 이월을 HRF 잔여와 분리해 측정하고, 두 시간척도를 하나의 이완 모형으로 적합한 연구는 찾지 못했다.
* **판정: partially.** 제안자의 판정과 같다. 다만 Pichon 2015는 "누적 활성이 이후 반응성을 예측"하는 편도체 수준의 관성 증거이므로 근거 목록에 추가해야 한다.

### 2.2 단순한 모델 적용에 불과한가
* 아니다. 측정 모형 설계다.
* 다만 'line attractor'라는 표현은 과하다. 마우스 VMHvl의 근거(doi:10.1038/s41586-024-07915-x)는 인과 교란이 있는 세포 수준 결과이고, BOLD에 leaky integrator를 적합한 것은 기술 모형이다. 결론은 "느린 이완 차원의 존재"로 한정해야 한다(geometry-info C5의 주의와 같음).

### 2.3 실제로 Neuroscience Question을 해결하는가
* 해결한다. 정서 관성의 신경 시간척도는 정서 동역학 이론(관성, 기분)의 핵심 측정량이다.
* 부수 효과도 있다. Horikawa 블록 평균 decoding이 직전 클립 정서로 오염되었는지를 판정하므로, 기존 결론(Horikawa 2020, Westlin 2025)의 해석 기준선이 바뀐다.

### 2.4 정서 이외의 요소(visual, semantic)를 decoding하는 것은 아닌가
* 위험이 크다. 직전 클립의 규범 정서는 그 클립의 시각-의미 내용과 공선적이다. 그래서 "정서 이월"이 시각 적응이나 의미 맥락의 이월일 수 있다. 제안자는 직전 클립의 시각 feature를 nuisance로 넣지만, 비선형 시간 통합까지 포함한 자극 구동 이월은 선형 nuisance로 다 잡히지 않는다.
* **핵심 보완(in-silico null):** TRIBE v2는 연속 영화로 학습되어 HRF 지연과 자극 시계열의 시간 통합을 학습했다. 같은 클립 시퀀스를 넣으면 "자극으로 계산 가능한 이월"(HRF 잔여 + 시각, 의미 맥락 효과)의 예측을 준다(arXiv:2605.04326, 5.3절, 5.8절의 5 s 지연 처리). 관찰 이월에서 TRIBE 예측 이월을 뺀 부분만 '정서 신경 관성' 후보로 남기면, HRF 꼬리와 자극 맥락을 한 번에 통제하는 강한 null이 된다. 단 공개 checkpoint는 피질만 예측하므로, 편도체와 피질하 이월에는 이 null을 쓸 수 없다.

### 2.5 현재 Dataset으로 검증할 수 있는가
Mind captioning 원문 Methods로 확인한 사실과 그 함의는 다음과 같다.
* **학습 세션:** 2,180개 비디오가 모든 피험자에게 같은 pseudorandom 순서로 제시되었다. Horikawa 2020처럼 직전 클립이 고정되어 있다.
* **테스트 세션:** 72개 비디오가 run 안 pseudorandom 순서로 5회 제시된다. 같은 클립의 선행 클립이 바뀌는 자연 변이가 있으므로 제안자의 판단은 맞다.
* 다만 테스트의 혼입 요인이 셋 있다.
  * 테스트 클립은 학습 세션 마지막 두 run에서 이미 1회 본 것이라 총 6회 노출이다. 반복 억제와 친숙도가 이월과 상호작용한다.
  * run마다 평가 블록 3~4개(문장 읽기와 버튼 반응)가 무작위로 끼어 있다. 평가 블록 직후 블록에는 읽기와 운동 활동의 이월이 섞인다.
  * 테스트 비디오 평균이 3.94 s라 10 s 블록 안에서 2~3회 반복 재생된다. 블록 내 반복 억제가 블록 길이와 공선적이다.
* **교차 코호트 자연 실험(미확인):** Mind captioning 학습 순서가 Horikawa 2020의 순서와 다르다면, 같은 클립이 두 코호트에서 다른 선행 클립 뒤에 놓인다. 그러면 2,180개 전체에서 선행 정서를 바꾼 비교가 가능해진다. 두 데이터셋의 events 파일로 순서를 대조해야 하며, 현재는 확인하지 못했다.
* **Emo-FilM washout:** 제공본 high-pass(sigma 50 s) 때문에 raw 재전처리가 필수다(geometry-info C5). 생리 동기화 성분(doi:10.1038/s41593-025-01945-y)이 이완 곡선에 섞이므로 생리 회귀 전후 판을 모두 보고한다.

### 2.6 더 강력한 모델이나 분석 방법
1. **TRIBE v2 in-silico 이월 null**(2.4절): 피질 영역에 대해 가장 강한 단일 통제다.
2. **개인 HRF 추정:** Mind captioning은 TR 1 s이고 같은 클립 반복이 있어, 피험자와 영역별 HRF를 반복 블록에서 직접 추정할 수 있다. 이것을 Horikawa 2020 deconvolution의 사전분포로 쓴다.
3. **모형 비교:** (i) HRF만, (ii) HRF + 시각 feature 적분기, (iii) HRF + 정서 잠재 차원 적분기, (iv) (iii) + TRIBE 예측 이월을 교차검증 우도로 비교한다. 시간상수는 영역별 계층 모형으로 추정한다.
4. **washout 쪽 in-silico 대조:** 영화 종료 후 빈 화면과 무음을 TRIBE v2에 넣어 '자극 계산 이완'을 예측하고, 관찰 이완과 비교한다.

### 2.7 결과가 기대와 달라도 의미가 있는가
* TRIBE와 HRF null을 넘는 이월이 없으면, 두 가지 결론이 나온다. Horikawa 블록 decoding은 이월로 크게 왜곡되지 않았다(기존 결과에 대한 안심 근거). 그리고 초 단위 정서 관성은 BOLD로 검출되지 않는다.
* washout에서만 느린 이완이 보이면 시간척도가 분리되어 있다는 뜻이다(짧은 클립 패러다임의 한계).
* 둘 다 보이고 시간상수가 일관되면 '정서 관성 차원'의 강한 기술적 증거다.
* 세 결과 모두 해석 가능하다.

### 2.8 수정안
* 근거에 Pichon 2015를 추가하고, 결론 표현을 "느린 이완 차원"으로 한정한다.
* 피질 영역에는 TRIBE v2 in-silico 이월 null을 1차 통제로 넣는다. 피질하는 Mind captioning 반복으로 추정한 개인 HRF + 시각 feature 적분기 null을 쓴다.
* Mind captioning 테스트 분석에서는 반복 순서(1~5회째), 평가 블록 인접 여부, 블록 내 반복 재생 횟수를 공변량으로 둔다.
* Horikawa 2020과 Mind captioning 학습 순서의 차이를 먼저 확인한다. 순서가 다르면 2,180개 전체를 이용한 교차 코호트 선행 정서 대조를 주 분석으로 승격한다(피험자 중복 확인 전제).
* label-provenance: 정서 차원은 felt / 별도 평정자 규범(결론은 "자극 정서 정보의 신경 이월"). evidence-level: R0. insilico-vs-observed: 혼합(TRIBE null 사용 시).

---

## 3. SN-P3: 피질하 경로 분석의 signal-feasibility 관문과 데이터 내장 대조

**제안 요지:** brain-inspired Chain 3(Horikawa에서 상구-pulvinar-편도체 경로가 싣는 정서 정보의 내용) 전에 관문 두 개를 둔다. 관문 1은 Kragel 2021의 내장 대조로, 무음 Horikawa에서 LGN-V1은 교차 연결보다 강하고 MGN-A1은 교차 수준이어야 한다. 관문 2는 SC voxel 수, tSNR, pulvinar 부분 용적이다. 통과하면 Horikawa 경로 내용 분석으로 가고, Spacetop과 Mind captioning으로 재현한다.

### 3.1 이미 연구된 것은 아닌가
* **검색:** PubMed `colliculus pulvinar amygdala pathway human fMRI`(2021~)와 `(superior colliculus OR pulvinar) AND amygdala AND fMRI AND (naturalistic OR movie OR film OR video) AND (pathway OR connectivity)`(2015~), 2026-11-12.
* **결과:**
  * Kragel et al. 2021(doi:10.1016/j.neuron.2021.06.001): MPathI를 7T(n=56)와 3T(n=48)에서 알려진 시상피질 경로로 먼저 검증했다. 그다음 상구-pulvinar-편도체 경로가 부정 **이미지와 소리**의 규범 정서 강도를 부호화한다고 보고했다(초록).
  * Zou et al. 2026(doi:10.1162/IMAG.a.1432): 고해상도 fMRI에서 SC 표층-PBGN-중심내측 편도체가 주의할 때만 충돌 궤적에 민감했다.
  * Kosteletou-Kassotaki et al. 2026(doi:10.1523/JNEUROSCI.1431-25.2026, DWI): 청각 하구-MGB-편도체 경로를 보고했다.
  * Sangchooli et al. 2026(doi:10.1002/hbm.70626, DWI): pulvinar-편도체 경로가 null 대비 지지되었다.
  * 자연 영상 fMRI에서 MPathI 경로를 재현하거나 내장 대조로 관문을 둔 연구는 찾지 못했다.
* **판정:** 관문 설계 자체는 Kragel 2021 검증 절차의 이식이다. 자연 영상 데이터에 적용한 것은 **no(PubMed 범위 내, arXiv 미확인)**.

### 3.2 단순한 모델 적용에 불과한가
관문은 연구 질문이 아니라 전제 조건 검사이므로, '적용'이라는 비판 대상이 아니다. 오히려 다른 피질하 질문(systems-neuro Chain 3, brain-inspired Chain 3, vision-decoding R4의 편도체 encoding)에도 공통으로 필요한 인프라다. 가치가 있다.

### 3.3 실제로 Neuroscience Question을 해결하는가
관문 자체는 해결하지 않는다. 관문 이후의 질문("경로가 혐오성 단일 축만 싣는가, 범주 정보를 싣는가")이 neuroscience 질문이다. 관문은 그 질문의 결과를 해석할 수 있게 해 준다. 단 관문 1 통과(LGN-V1 특이성)는 **시상피질 수준의 측정 가능성**을 보일 뿐이다. 상구(SC) 자체의 측정 가능성을 보장하지 않는다. SC는 2 mm에서 voxel이 매우 적고 CSF와 혈관 부분 용적이 크다. 관문 1과 SC 측정 가능성 사이에 논리적 간극이 있다.

### 3.4 정서 이외의 요소(visual, semantic)를 decoding하는 것은 아닌가
* 경로 활동은 운동 에너지, looming, 휘도 대비 같은 저수준 시각 신호를 따를 가능성이 크다. 이것들은 위협 장면과 공선적이다. brain-inspired Chain 3이 얕은 층과 깊은 층 feature를 비교하므로 이 위험은 설계에 반영되어 있다.
* 추가로 두 가지가 있다. Zou 2026은 SC-편도체 looming 민감성이 **주의 의존적**이라고 보고했으므로, 수동 시청 데이터에서 경로 신호가 약한 것은 측정 문제가 아니라 과제 문제일 수 있다. 또 Kragel 2021의 경로는 소리에도 반응했고 청각 low road도 별도로 보고되었다(Kosteletou-Kassotaki 2026). 따라서 소리 있는 재현(Spacetop)에서는 청각 경로가 섞인다.
* feature 모델로 EmoNet은 쓸 수 없다. Horikawa와 Mind captioning 자극으로 학습되었기 때문이다(doi:10.1126/sciadv.aaw4358).

### 3.5 현재 Dataset으로 검증할 수 있는가
* **Horikawa 2020:** TE 43 ms(3T)는 편도체와 내측 측두 신호 손실에 불리하다. 공개 전처리본의 피질하 ROI 10개에 SC, LGN, MGN, pulvinar가 따로 있는지 확인되지 않았으므로 raw 재전처리와 피험자 native 공간 atlas 정합이 필요하다.
* **Mind captioning이 관문 데이터로 더 낫다.** TE 30 ms, TR 1 s, 같은 자극이고, 72클립 x 5회 반복이 있다(원문 Methods). 그래서 SC, pulvinar, 편도체 voxel의 **반복 간 신뢰도**를 직접 계산할 수 있다. tSNR보다 직접적인 signal-feasibility 지표다. 다만 MB6이고 피험자 S1이 예비 노출되었다.
* **Spacetop:** Kragel 2021 Expt2와 같은 획득 조건이라는 장점이 있다. 그러나 MB8은 피질하 검출력을 낮춘다(doi:10.1016/j.neuroimage.2021.118617). 같은 참가자의 열 통증 음성 대조는 좋은 설계다.

### 3.6 더 강력한 모델이나 분석 방법
1. **노드 특이 기능 양성 대조:** LGN-V1 특이성 대신(또는 추가로), SC 자체에 알려진 기능을 대조로 쓴다. 클립의 운동 에너지와 확대(looming) 지표를 계산해 SC 반응이 이를 따르는지 본다(Zou 2026). 이 대조가 실패하면 경로 '내용' 분석은 해석할 수 없다.
2. **반복 신뢰도 관문:** Mind captioning 반복으로 영역별 split-half 신뢰도와 noise ceiling을 낸다. 신뢰도 하한을 사전에 정한다.
3. **in-silico 보완의 한계 명시:** 공개 TRIBE v2는 피질만 예측하므로 이 질문에 in-silico null을 줄 수 없다. 피질하는 데이터 학습 encoder로만 다룬다. 이 점은 EF-P1 trust map에서 "판정 불가"로 표시한다.
4. **전역 생리 성분:** 블록 간 공분산은 전역 자율신경-혈관 성분(doi:10.1038/s41593-025-01945-y)이 채울 수 있다. 시상과 편도체처럼 큰 혈관 근처 구조에서 특히 그렇다. 교차 연결 기준선이 이를 일부 상쇄하지만, 전역 신호 처리 multiverse(제거/유지)를 관문 결과와 함께 보고한다.

### 3.7 결과가 기대와 달라도 의미가 있는가
* 관문 실패: "이 데이터로는 피질하 경로 주장을 할 수 없다"는 결과가 다른 에이전트의 피질하 질문 여럿을 미리 걸러 준다. 방법론적으로 가치가 크다.
* 관문 통과 후 경로가 얕은 feature로만 설명되면 '조잡한 shortcut' 내용 가설이 지지된다.
* 깊은 feature나 범주 정보가 남으면 그 가설에 반하는 증거다.
* MGN-A1이 교차 연결보다 강하게 나오면, 블록 간 공분산이 공통 구동(전역 신호, 각성)으로 채워졌다는 경고다(제안자도 이 해석을 적었다).
* 모두 의미가 있다.

### 3.8 수정안
* 관문 데이터를 Horikawa 2020에서 **Mind captioning(주) + Horikawa 2020(재현)** 으로 바꾼다. 반복 신뢰도를 관문 2의 주 지표로 둔다.
* 관문 1에 SC 노드 특이 양성 대조(운동 에너지, looming)를 더한다. LGN-V1/MGN-A1 대조는 유지한다.
* 전역 신호 처리 multiverse와 피험자별 dropout 마스크를 결과 옆에 둔다(signal-feasibility 태그).
* 소리 있는 재현(Spacetop)에서는 청각 경로 혼입을 해석 단서로 명시한다.
* 근거에 Zou 2026, Kosteletou-Kassotaki 2026을 추가한다.
* label-provenance: Horikawa와 Mind captioning은 felt / 별도 평정자 규범, Spacetop은 felt / 본인. evidence-level: R0. insilico-vs-observed: 관찰(공개 in-silico 모델은 피질하 미지원).

---

## 4. 검토 요약표

| 제안 | 이미 연구됨 | 단순 적용 | Neuro 질문 해결 | 시각/의미 decoding 위험 | 현재 데이터 검증 | 더 강한 방법 | 기대와 달라도 의미 | 종합 |
|---|---|---|---|---|---|---|---|---|
| BI-P2 | partially (Morgenroth 2026 평정 수준, 성분 fMRI 선행) | 경쟁 설계는 아님, latent action band는 적용에 가까움 | 조건부(규범 평정 간 경쟁, 식별 불가 위험) | 높음 | Emo-FilM 가능, Horikawa는 신규 라벨 필요 | 판별 구간 선택, TRIBE 기준선, 신뢰도 보정 | 예(식별 불가도 결과) | **수정 후 진행** |
| MD-P1 | partially (분 단위 이월 다수, Pichon 2015 추가) | 아님 | 예 | 높음(시각, 의미 맥락 이월) | 가능(Mind captioning 테스트의 자연 변이, 단 반복, 평가 블록 혼입) | TRIBE in-silico 이월 null, 개인 HRF, 모형 비교 | 예 | **수정 후 진행, 우선순위 높음** |
| SN-P3 | 자연 영상 적용 no (PubMed 범위) | 관문은 인프라 | 관문 자체는 아님, 후속 질문의 전제 | 중간(저수준 시각, 주의 의존) | Mind captioning이 더 적합 | SC 노드 특이 대조, 반복 신뢰도 관문 | 예(실패도 유용) | **수정 후 진행(공통 인프라로)** |

미확인으로 남긴 것: arXiv preprint 범위의 선행 수행(API와 웹 검색 모두 사용 불가), Mind captioning과 Horikawa 2020의 제시 순서 차이와 피험자 중복, Horikawa 공개 전처리본에 SC, LGN, MGN, pulvinar ROI가 따로 있는지.
