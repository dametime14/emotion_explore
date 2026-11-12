# Round 3 (Constructive Disagreement) 검토: geometry-info

* 작성: geometry-info (Axis K, O 관점) / 기준일 2026-11-12 / 절차: `reference/protocols.md` P3
* 배정: LS-P1, EF-P1, SN-P3 (`outputs/discussion/round3_assignment.md`). 나는 세 제안 모두의 보낸 쪽, 받는 쪽, 참조 에이전트가 아니다.
* 읽은 원문: 각 제안의 전체 서술(llm-semantics, encoding-foundation, systems-neuro의 round2.md 2절)과 근거 chain(llm-semantics round1 Chain 1, vision-decoding round1 R6, encoding-foundation round1 Chain 1, generative-counterfactual round1 CH3, brain-inspired round1 Chain 3과 P-3, systems-neuro round1 Chain 3). 추가로 Kragel et al. 2021 전문(PMC8349850, PubMed 도구)과 Mind captioning Methods(PMC12588295)를 직접 읽었다.
* 표기: [본문], [초록], [DB](literature_db.csv verified 항목을 그 기록에 기대어 인용), [search_index](검색 색인으로만 봄, verified 아님). 판정 7개는 P3 순서를 따른다.

---

## 요약

| 제안 | 이미 연구? | 단순 적용? | 신경과학 질문 해결? | 정서 아닌 내용 decoding 위험 | 현재 데이터로 검증? | 더 강한 방법 | 기대와 달라도 유의미? | 종합 |
|---|---|---|---|---|---|---|---|---|
| LS-P1 | partially | 아니오(측정 설계) | 부분적으로 예 | 중간(과통제와 누출 양방향) | 예, 단 캡션 확보 확인 필요 | 신뢰도 보정 분할, rank별 잔차 스펙트럼, controversial 쌍 | 예 | **수정 후 채택 권고** |
| EF-P1 | partially (NeurIPS 2026 평가 논문 [search_index]) | 예에 가까움(감사 인프라) | 감사만으로는 아니오, 재구성하면 예 | 높음(backbone 기하가 곧 시각-의미 기하) | 예(피질만) | backbone 대 뇌 투영 분해, LOO 인간 기준선, rank별 충실도, 사전 결정 규칙 | 예 | **재구성 후 채택 권고** |
| SN-P3 | 게이트 설계는 no, 경로 내용 분석은 partially | 아니오(전제 조건 검사) | 게이트 자체는 아니오, 다음 단계의 전제 | 높음(상구는 시각과 안구운동 구조) | 부분적(Horikawa 3T 2 mm는 경계, Spacetop이 더 적합) | 안구운동 교란 회귀, 코호트 간 전향 적용, 반복 신뢰도 게이트 | 예 | **수정 후 채택 권고** |

---

## LS-P1. 정서 배제 캡션으로 설명하고 남는 정서 분산 (llm-semantics → vision-decoding)

**제안 요지:** vision-decoding R6과 llm-semantics Chain 1을 합친다. (1) 캡션의 정서 누출 감사(명시적 정서 어휘 수, LLM이 캡션만 읽고 추정한 정서), (2) 중첩 기준선 L1a 시각 feature → L1b 정서 배제 인간 캡션 embedding → L2 정서 언어로 재작성한 캡션 embedding [AI 추정] → C&K 34/14 규범 평정의 단계별 고유 분산, (3) Mind captioning 72개 반복으로 noise ceiling, Horikawa 2020으로 재현, 회상 조건에서 반복.

### 1. 이미 연구된 것은 아닌가? → **partially**
* Horikawa 2020은 정서 모델, 시각 객체 모델(1000차원), 의미 모델(인간 주석 73차원)의 encoding을 비교했다(doi:10.1016/j.isci.2020.101060, Results "Disentangling..." 절 [DB, 본문]). 다만 세 모델을 따로 적합해 비교했고(adversarial-reviewer U1 기록), 의미 feature는 LLM 캡션 embedding이 아니라 73개 이진 항목이었다.
* Du 2025는 MLLM, 캡션만 입력한 LLM, 인간 평정 표상의 뇌 설명력을 비교했다(arXiv:2509.24298 [본문, 내 Round 1에서 Limitations까지 읽음]). 정서 배제 캡션을 nuisance로 둔 잔차 분해는 아니다.
* Kiyokawa & Hayashi 2024(doi:10.1038/s41598-024-71690-y [DB])는 범주 이름 텍스트 embedding과 뇌 RSM을 범주 수준에서 비교했다.
* Doerig 2025(doi:10.1038/s42256-025-01072-0 [DB])는 캡션 LLM embedding이 고차 시각 영역을 잘 예측함을 보였지만 정서는 다루지 않았다.
* **검색 경로:** WebSearch "emotion ratings unique variance beyond caption language model embeddings fMRI variance partitioning scene description emotional videos" (2026-11-12). 정서 배제 인간 캡션을 기준선으로 쓴 정서 고유 분산 분할은 찾지 못했다. 가장 가까운 것은 Du 2025였다. arXiv:2508.09337은 제목이 비슷하지만 fMRI가 없는 텍스트 기반 영역 사상이라 무관하다(arxiv.org 초록 확인).
* 판정: 같은 질문의 거친 판(73개 의미 항목, 개별 적합)은 원 논문이 했고, 정서 배제 인간 캡션 기준선과 단계별 분할은 미발견이다.

### 2. 단순한 모델 적용에 불과한가? → **아니오, 다만 핵심은 측정 설계다**
banded ridge 분산 분할 자체는 표준 도구다. 새로움은 "정서를 쓰지 말라"는 지시로 받은 인간 캡션이라는 드문 자극 기술 변수와 캡션 누출 감사에 있다. 모델 성능 경쟁이 아니라 "언어로 기술되는 장면 의미가 정서 관련 신경 분산을 얼마나 운반하는가"를 묻는다.

### 3. 실제로 Neuroscience Question을 해결하는가? → **부분적으로 예**
"transmodal 영역의 정서 관련 분산이 언어화된 장면 의미를 넘는가"는 구성주의(개념 지식이 정서를 구성)와 정서 고유 표상 주장 사이의 구체적 쟁점이다. 그러나 제안 스스로 인정하듯 "고유 분산 0"은 "정서 없음"이 아니라 "정서가 장면 의미로 운반된다"는 뜻이라, 결과가 한쪽으로 나와도 이론을 판정하지는 못한다. 해결하는 것은 "정서 평정과 공변하는 신경 구조 중 언어 기술로 회복되지 않는 몫의 크기와 위치"까지다.

### 4. Emotion 이외의 요소를 decoding하는 것은 아닌가? → **위험이 양방향으로 있다**
* **과소 통제 쪽:** C&K 규범 평정 단계의 고유 분산은 캡션이 놓친 시각 세부(움직임, 얼굴 표정, 색)를 대신 담을 수 있다. L1a 시각 feature의 선택(어떤 비디오 모델, 어느 층)에 결과가 크게 의존한다.
* **과통제 쪽:** 캡션 embedding은 장면 의미와 함께 함축된 정서를 담는다. 정서와 의미가 인과적으로 얽힌 경우 캡션 회귀가 정서 신호를 지운다(generative-counterfactual Axis P의 과통제 경고, Deliverable B 1절).
* **측정 오차 비대칭:** 캡션 embedding은 20개 평균, 정서 평정은 9~17명 평균이다. 공변량에 측정 오차가 있으면 증분 고유 분산이 위양성으로 나온다(doi:10.1371/journal.pone.0152719 [DB]). 제안이 신뢰도 민감도를 보고하겠다고 했지만 구체 절차가 없다.
* **L2 단계:** AI가 재작성한 정서 캡션은 LLM의 정서 지식을 주입한다. L2와 C&K의 비교는 "정서 단어가 들어간 의미 표상 대 인간 규범 평정"이라 정서와 언어 형식이 섞인다.

### 5. 현재 Dataset으로 검증할 수 있는가? → **예, 조건부**
* Mind captioning 6명과 Horikawa 2020 5명은 같은 2,180개 비디오를 봤다(doi:10.1126/sciadv.adw1464 Visual stimuli 절 [본문]). 캡션은 비디오당 20개다. 다만 **캡션이 사용자가 보유한 공개 파생물(figshare)에 들어 있는지 미확인**이다(vision-decoding 0.1절).
* noise ceiling은 Mind captioning 72개 반복 클립에서만 구할 수 있고, 이 72개는 평균 3.94 s로 전체 평균 6.70 s보다 짧다([본문]). 2,181개 전체의 ceiling은 피험자 간 상한으로 대체해야 하며, 72개에서 얻은 비율을 전체로 옮길 때 길이 편향이 생긴다.
* 언어 불일치: 캡션 작성자는 MTurk(영어), Mind captioning 참가자는 일본어 모국어 화자다(같은 절). 캡션 embedding이 참가자의 장면 의미 표상을 대표한다는 가정이 약해진다.
* 회상 조건: 회상 cue가 바로 정서 배제 캡션이라 cue 구간의 언어 반응이 회상 창에 섞인다.

### 6. 더 강력한 모델이나 분석 방법이 있는가? → **예, 세 가지**
* **신뢰도 보정 분할:** 캡션 20개를 10/10으로 나눈 split-half 신뢰도와 평정자 수 기반 평정 신뢰도로 두 공변량을 disattenuate하거나, 여러 캡션 encoder를 지표로 둔 잠재변수 접근을 쓴다(adversarial-reviewer D2의 포화 곡선 검정과 같은 논리). 공변량 지표를 늘릴수록 고유 분산이 0으로 수렴하는지 plateau를 유지하는지를 보면 측정 오차 위양성을 직접 다룬다.
* **rank별 잔차 공유 스펙트럼(geometry-info GI-P1, GI-P5):** 캡션 embedding으로 예측한 반응을 뺀 잔차에 대해 11명 사이 교차 스펙트럼을 계산하면, "기술 의미 밖에 남는 공유 신경 차원이 몇 rank에 걸쳐 있는가"를 라벨 없이 셀 수 있다. 그다음에 그 잔차 공유 차원을 C&K 평정에 투사한다. 이렇게 하면 결론이 C&K 평정의 측정 오차에 덜 의존한다.
* **controversial 쌍:** 캡션 유사도와 정서 평정 유사도가 크게 갈리는 클립 쌍(frontier-ai T4, encoding-foundation Chain 4의 논리)만 골라 뇌 RDM이 어느 쪽을 따르는지 보는 판별 검정이 전체 평균 분할보다 검정력이 높다. 선택은 한 코호트, 검정은 다른 코호트에서 해 순환을 막는다.

### 7. 결과가 기대와 다를 때도 과학적으로 유의미한가? → **예**
고유 분산이 0에 수렴하면 "Horikawa의 분산된 정서 표상은 언어화된 장면 의미의 재표현"이라는 강한 결과다(EmoViS와 직결). 특정 영역(insula, amygdala, vmPFC)에만 plateau가 남으면 비언어적 정서 성분의 위치 후보가 된다. MLLM 정서 지도와 인간 규범 잔차 지도가 갈리면 L2와 L3의 공간적 분리 증거다. 어느 결과든 보고 가치가 있다.

### 수정안
1. **0단계 (선행 확인):** 보유 파생물에 캡션 20개/클립이 있는지, 두 코호트의 피험자 중복 여부를 확인한다.
2. **누출 감사 확장:** 정서 어휘 수와 LLM reader 추정 외에, 캡션 embedding만으로 C&K 34범주를 교차 예측한 R²(클립 단위 hold-out)를 "캡션의 정서 함축량"으로 보고한다. 이 값이 해석의 기준선이다.
3. **분할 방식 변경:** 개별 적합 비교 대신 joint banded ridge와 commonality 분석을 쓰고, 정서 → 캡션 방향의 역분할도 함께 보고한다(대칭 보고로 과통제와 과소 통제를 동시에 노출).
4. **신뢰도 보정:** 캡션 split-half와 평정 신뢰도로 disattenuation하고, 캡션 encoder를 2~3개로 늘린 포화 곡선을 그린다.
5. **L2 단계 분리:** AI 재작성 캡션 비교는 "모델 쪽 조작(R1 성격)"으로 별도 표에 두고 주 결론에서 뺀다.
6. **잔차 스펙트럼 추가:** 잔차의 11명 교차 스펙트럼(코호트 내와 코호트 간 분리)을 주 지표 중 하나로 둔다.
7. **회상 조건:** cue 캡션 embedding encoding으로 cue 반응을 nuisance로 빼고, 회상 창 앞부분을 절단한 판도 보고한다.
8. **표기:** label-provenance는 캡션 = 별도 평정자의 시각 내용 기술(정서 배제 지시), 정서 = felt / 별도 평정자 규범(C&K), 재작성 캡션 = AI 추정. evidence-level R0. overlap: EmoViS.

---

## EF-P1. 같은 자극에서 surrogate 충실도 감사를 모든 in-silico 결과의 관문으로 (encoding-foundation → generative-counterfactual)

**제안 요지:** TRIBE v2(영상만, 무음)로 Horikawa 2,181개와 Mind captioning 72개 반복 클립의 run 시퀀스를 예측하고, 관찰과 같은 블록 평균을 적용한다. 영역별로 (a) 반응 상관(Mind captioning 반복 ceiling으로 정규화), (b) 34범주, 14차원 규범 RDM에 대한 관계 충실도, (c) 시각-의미 RDM(V-JEPA2, 중립 캡션)을 partial로 뺀 정서 고유 RSA를 계산해 parcel별 trust map을 만들고, generative-counterfactual의 R1 편집 결과를 거르는 관문으로 쓴다. Emo-FilM으로 시청각 재현.

### 1. 이미 연구된 것은 아닌가? → **partially (선행 가능성 높음, 확인 필요)**
* EmoMind(arXiv:2605.16739 [DB])는 TRIBE v2 예측으로 실측을 대체했을 때 클립 간 정서 RSA가 약 26%로 떨어진다고 보고했지만, 실측(Mind captioning)과 대체(Emo-FilM 자극)의 자극이 달랐다(generative-counterfactual CH3 기록).
* WebSearch '"TRIBE v2" evaluation emotion movie observed fMRI fidelity in-silico emotional stimuli benchmark 2026'(2026-11-12)에서 NeurIPS 2026 "Evaluating TRIBE v2 Beyond Its Original Benchmarks: From Functional Localizers to Naturalistic Emotion"이 검색되었다 **[search_index]**. 검색 요약에 따르면 "연속 정서 주석이 있는 자연주의 정서 영화 자극"에서 모델-뇌 대응이 정서 범주마다 크게 달랐다. neurips.cc와 api2.openreview.net이 이 환경에서 열리지 않아 데이터셋(Emo-FilM일 가능성)과 지표를 확인하지 못했다. encoding-foundation도 같은 논문을 search_index로 기록하고 partially로 판정했다.
* 판정: EF-P1 4단계(Emo-FilM 재현)는 이 논문과 겹칠 가능성이 높다. Horikawa 2,181개와 Mind captioning 반복 ceiling, 관계 기하와 rank 대역 충실도는 미발견이다.

### 2. 단순한 모델 적용에 불과한가? → **예에 가깝다(감사 인프라)**
제안은 공개 모델을 새 자극에 돌려 충실도를 재는 평가이며, 그 자체로는 새로운 신경과학 질문이 아니다. P5 Novelty Constraint의 "벤치마크" 쪽에 가깝다. 다만 in-silico 결과를 쓰는 다른 제안(generative-counterfactual CH1, CH2, CH4, CH6, CH7, encoding-foundation Chain 7, frontier-ai CH6 등)의 전제 조건이라는 점에서 팀 전체에 필요한 인프라다.

### 3. 실제로 Neuroscience Question을 해결하는가? → **감사로서는 아니오, 재구성하면 예**
"어느 parcel에서 TRIBE를 믿을 수 있는가"는 공학 질문이다. 그러나 같은 분석을 "관찰된 정서 기하 중 자극으로 계산 가능한 부분과 그렇지 않은 부분은 어디에 있는가"(generative-counterfactual CH3의 residual affect)로 재구성하면 정서 표상 대 시각-의미 표상 쟁점(CLAUDE.md 6절)에 직접 답하는 질문이 된다. 제안문은 관문 역할만 강조하고 이 과학적 산출물을 명시하지 않았다.

### 4. Emotion 이외의 요소를 decoding하는 것은 아닌가? → **위험 높음**
* TRIBE v2의 영상 feature backbone은 V-JEPA 2다(encoding-foundation round1 0절). 따라서 (c)에서 V-JEPA2 RDM을 partial로 빼면 관찰 RDM과 예측 RDM 모두에서 같은 성분을 빼게 되어, 남는 예측 RDM의 구조는 "backbone 위에 TRIBE의 뇌 투영이 더한 변환"뿐이다. 이것은 의도한 "정서 고유 RSA"와 다른 양이다. 반대로 partial을 빼지 않은 (b)의 높은 관계 충실도는 대부분 시각-의미 기하의 재현일 수 있다(C&K 34범주 RDM 자체가 시각 내용과 공선적).
* 34범주 규범 RDM은 별도 평정자의 평균이라 "정서 기하 충실도"는 "규범 평정과 공변하는 신경 기하의 충실도"로 서술해야 한다.

### 5. 현재 Dataset으로 검증할 수 있는가? → **예(피질만)**
* Horikawa 2020과 Mind captioning은 같은 2,180개 클립이라 짝 비교가 가능하다(doi:10.1126/sciadv.adw1464 [본문]). 원본 비디오는 보유(사용자 결정).
* 공개 TRIBE v2 checkpoint는 fsaverage5 피질만 예측하고 CC BY-NC 4.0이다(encoding-foundation 기록). 편도체, 피질하 trust는 "판정 불가"다.
* Mind captioning 반복 ceiling은 72개 짧은 클립에만 있다. Horikawa는 TR 2 s, 최소 블록 8 s, Mind captioning은 TR 1 s, 최소 블록 10 s라 블록 평균 방식을 각각 맞춰야 한다.
* 클립을 이어 붙인 시퀀스는 TRIBE 학습 분포(긴 연속 영화)와 다르다는 반론과 대응(클립 단위와 시퀀스 단위 둘 다 보고)은 적절하다.

### 6. 더 강력한 모델이나 분석 방법이 있는가? → **예**
* **backbone 대 뇌 투영 분해:** 같은 probe로 V-JEPA2 backbone feature와 TRIBE 예측 피질을 각각 관찰 기하와 비교한다(encoding-foundation 자신의 I4 matched-control audit, arXiv:2607.16292 [DB]의 논리). trust는 "TRIBE의 뇌 투영이 backbone보다 관찰 기하에 더 가까운가"로 정의해야 in-silico 편집 결과의 해석에 쓸모가 있다.
* **공정한 인간 기준선과 rank별 충실도(GI-P4):** TRIBE 예측은 잡음 없는 group 평균이므로, 비교 기준은 개별 피험자가 아니라 "해당 피험자를 뺀 나머지 인간의 평균"(LOO 의사 피험자)이어야 한다. TRIBE와 LOO 평균을 각각 의사 피험자로 두고 11명과의 교차 스펙트럼을 rank별로 비교하면, 어느 rank 대역의 공유 분산이 자극으로 계산되지 않는지 알 수 있다(arXiv:2409.06843).
* **수준별 기하 대응:** GW로 클립 단위와 범주 단위 매칭률을 나누면(doi:10.1038/s41598-025-14961-6) RSA 상관 하나보다 실패 지점이 분명해진다.
* **RSA 추론:** 자극 bootstrap을 포함한 2-factor 추론(doi:10.7554/eLife.82566 [DB])으로 parcel별 신뢰구간을 낸다.

### 7. 결과가 기대와 다를 때도 과학적으로 유의미한가? → **예**
모든 transmodal parcel에서 관계 충실도가 낮으면 in-silico 정서 편집 결과는 그 영역에서 해석할 수 없다는 강한 음성 결과다(팀의 R1 제안들에 즉시 영향). 높으면 관찰된 정서 기하가 자극으로 계산 가능하다는 뜻이고, 이는 "정서 표상이 시각-의미 표상의 재기술인가"에 대한 증거다. 특정 rank 대역에서만 결손이 나면 residual affect의 위치가 정해진다.

### 수정안
1. **산출물을 둘로 명시:** (a) 관문용 trust map(공학), (b) "관찰 정서 기하 중 자극 계산 가능 비율"의 parcel별, rank별 지도(과학). (b)를 주 결과로 둔다.
2. **trust 정의 변경:** trust = TRIBE 예측 피질의 관찰 기하 충실도 - backbone feature의 관찰 기하 충실도(같은 probe, 같은 ceiling 정규화). backbone을 partial로 빼는 (c)는 이 차이로 대체한다.
3. **기준선:** LOO 인간 평균 의사 피험자를 모든 지표의 상한 기준으로 둔다.
4. **사전 결정 규칙:** 관문 통과 조건(예: 관계 충실도 하한 신뢰구간이 LOO 기준의 일정 비율 이상)을 R1 결과를 보기 전에 등록한다. 규칙 없이 trust map을 사후에 쓰면 관문이 아니라 해석의 자유도를 늘린다.
5. **선행 확인:** NeurIPS 2026 평가 논문의 데이터셋과 지표를 식별자 경로로 확인한 뒤 Emo-FilM 단계의 새로움을 다시 판정한다.
6. **표기:** label-provenance: RDM 라벨은 felt / 별도 평정자 규범. insilico-vs-observed: 혼합. evidence-level: R0(감사), 관문은 R1 결과의 필요조건일 뿐 충분조건이 아님을 명시. overlap: Emo-FilM 연구(Emo-FilM 단계).

---

## SN-P3. 피질하 경로 분석의 signal-feasibility 관문과 데이터 내장 대조 (systems-neuro → brain-inspired)

**제안 요지:** brain-inspired Chain 3(Horikawa 34범주에서 상구-pulvinar-편도체 경로가 싣는 정보)을 하기 전에 (1) Kragel 2021의 대조 분석(LGN-V1 vs MGN-A1과 교차 연결)을 Horikawa에 돌려 무음 자극에서 LGN-V1은 교차보다 강하고 MGN-A1은 교차 수준인지 보는 내장 양성/음성 대조, (2) 피험자별 SC voxel 수, tSNR, pulvinar 부분 용적 보고, (3) 통과 시 경로 내용 분석, Spacetop과 Mind captioning으로 재현, (4) 해석은 내용만(속도 아님).

### 1. 이미 연구된 것은 아닌가? → **게이트 설계는 no, 경로 내용 분석은 partially**
* Kragel et al. 2021은 MPathI로 7T(56명)와 3T(48명)에서 LGN-V1, MGN-A1을 표적 경로로, 교차 연결을 음성 대조로 써서 경로 식별을 검증했다(doi:10.1016/j.neuron.2021.06.001 [본문, PMC8349850]). 즉 대조 논리 자체는 원 논문의 것이다. **3T 결과는 표적 r = 0.547, 교차 r = 0.492로 차이가 작았다(Δ 0.055, 정확도 76%, AUROC 0.783).** 3T에서도 쓸 만하다는 근거이자, 3T 게이트의 판별력이 크지 않다는 근거다.
* 무음 자극 데이터에서 MGN-A1을 음성 대조로 쓰는 설계는 찾지 못했다.
* 편도체 하위영역의 DNN encoding은 영화 fMRI에서 이미 수행되었다(Jang & Kragel 2025, doi:10.1523/JNEUROSCI.1436-24.2025 [DB]). 경로 수준(MPathI)을 자연 영상에 적용한 연구는 찾지 못했다.
* **검색 경로:** WebSearch "superior colliculus pulvinar amygdala pathway MPathI replication naturalistic video fMRI 2024 2025 2026 LGN V1 control"(2026-11-12): 2024~2026 재현이나 자연 영상 경로 분석 없음, 2019~2021 문헌만(McFadyen 2019 eLife 백질 경로 등). PubMed "(superior colliculus OR pulvinar) AND amygdala AND (pathway OR connectivity) AND (movie OR naturalistic OR video) AND fMRI"(2026-11-12): 관련 최근 결과 없음. systems-neuro Round 1의 Thieu 2025 CCN 초록(SC looming)은 search_index 수준이다.

### 2. 단순한 모델 적용에 불과한가? → **아니오, 전제 조건 검사다**
기존 방법(MPathI)의 대조 분석을 새 데이터에 돌리는 것이지만 목적은 모델 성능이 아니라 측정 가능성 판정이다. 새 데이터 특성(무음)을 음성 대조로 바꾸는 발상은 좋은 설계다.

### 3. 실제로 Neuroscience Question을 해결하는가? → **게이트 자체는 아니오, 다음 단계의 필수 전제**
게이트는 "Horikawa에서 시상 수준 경로를 해석할 수 있는가"에 답한다. 신경과학 질문("low road가 34범주 정서에서 무엇을 싣는가", brain-inspired P-3)은 게이트 통과 후 단계에서 다뤄진다. 게이트가 실패해도 "어느 데이터로 피질하 경로 질문을 할 수 있는가"라는 팀 차원의 결정 정보를 준다.

### 4. Emotion 이외의 요소를 decoding하는 것은 아닌가? → **위험 높음, 제안에 빠진 교란이 있다**
* **안구운동:** 상구는 시각 구조이자 saccade 생성 구조다. Horikawa와 Mind captioning 모두 **응시점 고정 없는 자유 시청**이다(Mind captioning Video presentation experiment 절 "viewed the stimuli without fixation" [본문]; Horikawa 2020 Limitations of the Study 3째 단락 [본문]). 정서 범주마다 탐색 시선 패턴이 다르면 SC 패턴과 SC-pulvinar 공분산이 정서 대신 안구운동을 따를 수 있다. 제안의 게이트(LGN-V1 대 MGN-A1)는 이 교란을 검출하지 못한다.
* **시각 저수준 특징:** SC와 pulvinar는 움직임, 대비, looming에 반응한다. 34범주 클립 사이 경로 공분산이 정서보다 시각 운동 에너지를 추적할 가능성이 크다. brain-inspired Chain 3은 얕은 층 feature를 band로 두었지만 SN-P3 게이트에는 없다.
* **공통 구동:** 블록 단위 공분산은 정서와 무관한 공통 구동(전역 신호, 각성 수준)에 크게 좌우된다. Kragel 3T의 교차 연결 r 0.492는 이 공통 성분이 크다는 뜻이다. 제안의 반론 2 대응("MGN-A1이 교차보다 강하면 경고 신호")은 맞지만, 그 반대(LGN-V1만 강함)도 시각 구동 공통 성분 때문일 수 있다.

### 5. 현재 Dataset으로 검증할 수 있는가? → **부분적으로**
* Horikawa: 3T Verio, 2 mm, TR 2 s, MB4, TE 43 ms(systems-neuro 기록), 5명, 블록 평균 공개 전처리본은 native 공간이다. Kragel 3T는 group 수준 학습과 leave-one-subject-out 검증(48명)이었는데 Horikawa 5명으로는 group 학습이 어렵다. 대신 피험자당 2,196 블록으로 피험자 내 교차검증(Kragel 7T 실험 1처럼 피험자별 모형)이 가능하다. SC는 2 mm에서 수십 voxel 수준이라 부분 용적이 크다.
* Mind captioning: 같은 자극, 3T Prisma, TR 1 s, MB6(vision-decoding 기록). 72개 x 6회 반복으로 **SC, pulvinar 반응의 반복 간 신뢰도**를 직접 잴 수 있다. 이것이 tSNR보다 강한 게이트다.
* Spacetop: Kragel 3T 실험 2와 획득 조건이 같고(systems-neuro Round 1), 같은 참가자의 열 통증이 실제 음성 대조다. 경로 질문의 주 데이터로는 Horikawa보다 Spacetop이 적합하다.

### 6. 더 강력한 모델이나 분석 방법이 있는가? → **예**
* **반복 신뢰도 게이트:** Mind captioning 72개 반복에서 SC, pulvinar, 편도체 패턴의 split-half 신뢰도와 noise ceiling을 먼저 낸다(brain-inspired BI-P3도 같은 점검을 1단계로 제안). 신뢰도가 바닥이면 Horikawa 분석은 중단한다.
* **안구운동 교란 회귀:** eye tracker가 없으므로 MR 영상의 안구 신호로 시선을 추정하는 DeepMReye(doi:10.1038/s41593-021-00947-w [DB], brain-inspired I-8 보완)로 saccade 빈도와 시선 분산 회귀자를 만들고, 경로 공분산과 정서 추적을 이 회귀자 통제 전후로 보고한다. 전제는 Horikawa raw의 촬영 범위에 안구가 들어 있는지 확인하는 것이다.
* **코호트 간 전향 적용:** Horikawa 피험자로 추정한 경로 가중치를 Mind captioning 피험자(같은 자극, 다른 스캐너)에 고정 적용하면, 경로가 특정 스캐너, 순서의 공통 구동이 아니라는 증거가 된다(GI-P1의 코호트 간 논리).
* **선택성 대조의 정서판:** Kragel의 통증 음성 대조에 해당하는 것을 Horikawa 안에서 만든다. 시각 운동 에너지를 맞춘 상태에서 부정 고각성 범주(fear, horror, disgust)와 긍정 고각성 범주(excitement, amusement)의 경로 추적을 비교한다. Kragel은 경로가 쾌 이미지에 반응하지 않았다고 보고했으므로(doi:10.1016/j.neuron.2021.06.001 [본문]), 같은 선택성이 나오면 "현저성 일반 신호" 해석과 구분된다.
* **잔차 공간에서 추정:** 블록 공분산의 최상위 공유 성분(전역, 공통 시각 구동)을 제거한 뒤 MPathI를 추정해 교차 연결 기준선을 낮춘다. 단 이 제거가 경로 신호를 지우는지 LGN-V1 표적-교차 차이로 함께 점검한다.

### 7. 결과가 기대와 다를 때도 과학적으로 유의미한가? → **예**
게이트 실패는 "Horikawa 획득 조건에서 시상 수준 경로는 해석 불가"라는 팀 결정 정보이며, 피질하 표적 질문을 Spacetop, Mind captioning으로 옮기는 근거가 된다. 게이트 통과 후 경로가 시각 운동이나 안구운동만 추적하면 "자연 영상에서 low road는 감각 수준 신호"라는 결과이고, Kragel 2021이 이미지에서 본 자기보고 매개 부재(Results, mediation 단락 [본문])와 합치하는 의미 있는 결과다. 정서 선택성이 남으면 자연 영상으로의 첫 경로 수준 확장이다.

### 수정안
1. **게이트를 셋으로 확장:** G1 내장 대조(LGN-V1 대 MGN-A1과 교차, 제안 그대로) + G2 Mind captioning 반복 신뢰도(SC, pulvinar, 편도체 split-half) + G3 안구운동 교란 가능성(DeepMReye 적용 가능 여부와 saccade 회귀자의 경로 설명력). G1의 판정 기준은 Kragel 3T의 표적-교차 차이(Δ 약 0.055)와 비교해 미리 정한다.
2. **피험자 내 모형:** Horikawa 5명은 group 학습 대신 피험자별 MPathI와 run 단위 교차검증을 쓰고, 결과를 피험자별로 모두 보고하며 prevalence로 요약한다(doi:10.7554/eLife.62461 [DB]).
3. **전향 적용:** Horikawa → Mind captioning(같은 자극, 다른 코호트), Spacetop 내부(alignvideo → 열 통증 음성 대조).
4. **교란 band:** 경로 내용 분석 단계에서 시각 운동 에너지, 저공간주파수 에너지, 얕은 층 feature, saccade 회귀자를 각각 band로 넣는다(brain-inspired Chain 3과 정합).
5. **주 데이터 재배치:** 경로 선택성 질문의 주 데이터는 Spacetop(Kragel 획득 조건 일치, 같은 참가자 통증 대조), Horikawa와 Mind captioning은 34범주 내용 분석과 코호트 간 재현으로 역할을 나눈다.
6. **표기:** signal-feasibility: 제안의 핵심. label-provenance: Horikawa, Mind captioning = felt / 별도 평정자 규범, Spacetop = felt / 참가자 본인(사후, 결측 약 51%). evidence-level: R0. overlap: EmoViS(brain-inspired Chain 3 기록 그대로, 부분).

---

## 검토에 쓴 검색 경로 (2026-11-12)

| 제안 | 경로와 질의 | 결과 |
|---|---|---|
| LS-P1 | WebSearch "emotion ratings unique variance beyond caption language model embeddings fMRI variance partitioning scene description emotional videos" | 정서 배제 캡션 기준선의 분할 미발견. Du 2025가 가장 가까움. arXiv:2508.09337은 fMRI 없는 텍스트 연구(arxiv.org 초록 확인)라 무관 |
| EF-P1 | WebSearch '"TRIBE v2" evaluation emotion movie observed fMRI fidelity in-silico emotional stimuli benchmark 2026'; neurips.cc, api2.openreview.net 접근 시도(차단) | NeurIPS 2026 TRIBE v2 정서 영화 평가 논문 [search_index], 데이터셋 미확인 |
| SN-P3 | WebSearch "superior colliculus pulvinar amygdala pathway MPathI replication naturalistic video fMRI 2024 2025 2026 LGN V1 control"; PubMed "(superior colliculus OR pulvinar) AND amygdala AND (pathway OR connectivity) AND (movie OR naturalistic OR video) AND fMRI"; Kragel 2021 전문(PMC8349850) | 자연 영상 경로 분석 미발견. Kragel 2021 3T 대조 수치 확인 |
