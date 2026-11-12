# Shortlist 선행연구 중복 감사 (adversarial-reviewer)

* 작성: adversarial-reviewer. 기준일 2026-11-12. 지시: `prompts/stage4_evaluation_proposals.md` 2절 2번, Coordinator 위임 메시지.
* 대상 13개: Shortlist 10개(RQ-08, 10, 15, 01, 03, 33, 60, 32, 43, 44)와 교체 후보 3개(RQ-14, 25, 26).
* 읽은 자료: `outputs/rq_landscape.md` 4절(13개 질문의 자세한 설명), `outputs/combinations/matrix.csv`(prior_work, note), `outputs/evaluation/gap_table.md`, `outputs/discussion/round3_summary.md` 1~2절, `outputs/agents/adversarial-reviewer/round3_top10_review.md`, `outputs/literature/literature_db.csv`(기존 verified 항목 대조), Mind captioning 본문 Methods(이전 세션 scratchpad 텍스트).
* 출발점은 matrix의 prior_work 판정과 이전 검토의 선행이다. 그러나 판정은 이번 검색으로 다시 내렸다. 질문마다 검색 질의를 2개 이상 썼고, 질의와 결과는 질문별 절과 6절에 적었다.
* 확인 경로 표기:
  * [PubMed]: PubMed 메타데이터로 PMID와 DOI를 확인했다.
  * [Crossref]: api.crossref.org로 DOI를 확인했다.
  * [arXiv]: export.arxiv.org API로 arXiv ID를 확인했다.
  * [db]: 프로젝트 literature_db.csv에 이미 verified로 있던 항목이다.
* 읽은 범위 표기: 본문(전문 일부 이상), 초록, 제목만.
* 접근하지 못한 경로: WebFetch로 arxiv.org는 DNS 오류가 났다(curl로 arXiv API와 HTML은 받았다). typeset.io와 Europe PMC는 프록시 403이 났다. 그래서 St-Laurent 2015 본문은 읽지 못했다.

---

## 0. 판정 기준

판정이 "partially"로 쏠리지 않도록 다음 기준을 미리 정하고 적용했다.

| 판정 | 기준 |
|---|---|
| done | 선행 연구가 같은 가설을 같은 종류의 증거(같은 구성개념, 같은 비교)로 이미 검정했다. 우리 판본이 더하는 것은 데이터셋 교체뿐이다 |
| partially | 선행 연구가 핵심 가설 또는 그 주요 구성 요소를 다른 자극이나 설계로 검정했다. 남는 새 부분을 한 줄로 특정할 수 있다 |
| not found | 이 검색 범위에서 핵심 가설을 검정한 연구가 없다. 방법이나 인접 구성개념의 선행만 있다 |

"not found"는 "없다"가 아니라 "이 검색 범위에서 찾지 못했다"이다. Google Scholar와 bioRxiv 전용 검색은 쓰지 못했다.

---

## 1. 요약

| RQ | 이전 판정(matrix) | 이번 판정 | 가장 가까운 선행 | 남는 새 부분(한 줄) | 권고 |
|---|---|---|---|---|---|
| RQ-08 | partially | **partially** | Du 2023(같은 Horikawa 자료, 정서 + motion energy + 73개 의미 평정의 banded ridge), Abdel-Ghaffar 2024, Horikawa 2020 | 정서 배제 인간 캡션 20개로 만든 풍부한 기술 공변량, 측정 오차 보정, 고유 분산 추정, 두 코호트 재현 | 유지. Du 2023을 V11 재현 목표에 추가 |
| RQ-10 | partially | **partially** | Tuckute 2024(언어망, 새 피험자 검증), Ratan Murty 2021(범주 영역 고반응 자극 선별), NeuroVolve(amygdala 합성의 in vivo 검증) | 정서 encoder 대 시각-의미 encoder의 controversial 선택을 정서 영역에서 코호트 간으로 시험 | 좁혀서 유지. 남는 새 부분이 작다 |
| RQ-15 | partially | **not found** | Du 2025(MLLM 출력 기반 embedding과 뇌), arXiv:2610.22706(MLLM 평정을 encoding 회귀자로), arXiv:2510.04064(LLM 정서 probe가 prompting보다 우수, 뇌 없음) | 같은 모델, 같은 forward pass의 내부 표상 대 출력을 뇌 설명력으로 직접 비교 | 유지 |
| RQ-01 | partially | **partially** | Horikawa 2020(범주), Du 2023(같은 자료, 연속 gradient), Westlin 2025(개인 특이 군집), Koide-Majima 2020(다른 자료, 25차원), EmoMind(두 코호트 결합) | 독립 두 코호트에서 재현되는 신뢰 rank 대역 안에서 세 설명(범주, 연속, 개인 특이)의 held-out 비교 | 좁혀서 유지. '차원 수' 주장은 빼기 |
| RQ-03 | no | **not found** | Stringer 2019(마우스, 자극 앙상블 차원과 지수의 이론, 실험), Gauthaman 2024(인간 fMRI scale-free 스펙트럼) | fMRI에서 같은 자극 풀의 부분집합 다양성을 조작한 스펙트럼 지수 비교, 정서 영역 대상 | 유지 |
| RQ-33 | partially | **partially** | 행동 serial dependence(Van der Burg 2021, Ortega 2023), 신경 맥락 효과(Mobbs 2006, Cao 2024, Pichon 2015) | 자연 클립 무작위 연쇄에서 정서 부분공간 표상 이동의 부호 | 좁혀서 유지. 선행이 예측하는 방향(동화)이 HRF 교란 방향과 같다 |
| RQ-60 | partially | **partially** | Meyer 2010(소리를 암시하는 무음 영상이 청각피질에 내용 특이 활동을 만든다) | V2A 생성 모델의 암시 소리 표상이 자기 시각 조건 embedding 이상으로 청각피질을 설명하는지, 그 성분이 정서를 싣는지 | 좁혀서 유지. '청각피질이 암시 소리를 표상하는가' 부분은 이미 수행됨 |
| RQ-32 | 미확인 | **not found** | Ke 2025(동적 FC가 arousal 예측, 영화 간 일반화), van der Meer 2020(영화 중 뇌 상태 동역학과 생리, 몰입), Nguyen 2026(사건 경계의 패턴 이동) | arousal을 신경 상태 변화 속도로 정의하고 위치(평균 활성)와 경쟁시키는 검정 | 유지. Ke 2025 모형을 경쟁 기준선으로 |
| RQ-43 | partially | **partially(done에 가까움)** | St-Laurent 2015(짧은 영상 회상, 재활성이 vividness 예측), Barker 2022(재활성과 vividness의 공통, 분리 성분), Bainbridge & Rissman 2018(자극 기억성 대 주관 기억 판단의 신경 해리) | vividness를 item 간(기억성)과 item 안 성분으로 나눠 본인 재활성과 연결, 정서 부분공간 | 남는 새 부분이 가장 작다. RQ-41에 흡수하거나 RQ-14와 교체 권고(구속력 없음) |
| RQ-44 | no(직접), partially | **partially** | Chen 2017(회상 패턴이 지각과 다르게 체계적으로 재구성되고 사람 간에 공유), Favila 2022(기억 반응은 지각과 다른 공간 튜닝), Spens & Burgess 2024(기억 구성의 생성 모델 이론) | cue로 생성한 영상의 encoding 예측을 '재구성 가설'의 계산 대리로 쓰고, 정서 부분공간과 시각 부분공간을 비교 | 좁혀서 유지 |
| RQ-14 | 미확인 | **not found** | Marras 2025(행동 feature 6영역 중 Agent & Object, 영화 fMRI encoding), Thornton & Tamir 2024, Mohammadi 2023 | 사건-의미역 feature가 appraisal(행위 주체) 평정과 정서 영역 반응을 물체/장면 feature 이상으로 설명하는지 | 교체 후보로 강함 |
| RQ-25 | partially | **partially** | Nguyen 2026(영화 fMRI에서 오차형 대 불확실성형 사건 경계가 서로 다른 영역과 연결), Mohammadi 2023(novelty appraisal 네트워크), Garrido 2025(V-JEPA surprise) | world model 오차 대 불확실성을 appraisal 두 유형(Suddenly 대 Predictable, Urgency)과 amygdala, insula에 대응 | 좁혀서 유지 |
| RQ-26 | partially | **partially** | Pichon 2015(영화 뒤 amygdala 위협 반응성 이월), Gaviria 2021(정서 영화 뒤 휴지기 뇌 상태 이월), Qiao-Tasserit 2017(정서 클립 뒤 수 분간 표정 판단 편향) | 수 초 단위 클립 간 이월을 무작위 연쇄에서 정서 대 시각 부분공간으로, 영역별 HRF를 보정해 검정 | 좁혀서 유지 |

* **done 0건, partially 9건, not found 4건.**
* done이 없으므로 규칙상 교체해야 하는 질문은 없다. 그러나 남는 새 부분의 크기는 질문마다 크게 다르다. 2절에서 질문별로 적었다.
* **이전 판정과 달라진 점:**
  * RQ-15: partially에서 not found로 바꿨다. matrix가 근거로 든 Du 2025는 출력 기반 표상만 다룬다. 내부 표상 대 출력의 직접 비교는 찾지 못했다.
  * RQ-08: 판정은 같다. 그러나 가장 가까운 선행인 Du 2023이 matrix와 이전 검토 모두에서 빠져 있었다. Du 2023은 같은 Horikawa 자료에 정서, motion energy, 73개 의미 평정을 banded ridge로 함께 넣었다.
  * RQ-43: 판정은 같다. 그러나 St-Laurent 2015와 Bainbridge & Rissman 2018 때문에 done에 가깝다.
  * RQ-33: 판정은 같다. 그러나 행동 serial dependence 문헌이 예측하는 방향(동화)이 HRF 잔여가 만드는 가짜 효과의 방향과 같다. 그래서 설계 수정이 필요하다.

---

## 2. 질문별 감사

### RQ-08. 장면 기술 의미를 빼고도 정서 신호가 남는가

**(a) 가장 가까운 선행**
1. Du C, Fu K, Wen B, He H (2023). Topographic representation of visually evoked emotional experiences in the human cerebral cortex. iScience 26:107571. doi:10.1016/j.isci.2023.107571, PMID 37664621 [PubMed]. **본문**(PMC10470388의 Methods와 Limitations 확인).
   * 같은 Horikawa 자료(5명, 2,196 sample)에 banded ridge를 썼다. band는 정서 범주 평정, motion energy 6,555차원, "73개의 비교적 구체적인 의미 개념 평정"이다. 목적은 시각, 의미 정보와의 가짜 상관을 지우는 것이었다.
   * Limitations 셋째 항목: banded ridge로 통제해도 시각, 의미 feature의 교란이 남을 수 있고, 이를 배제할 더 나은 패러다임이 필요하다고 적었다.
2. Horikawa T et al. (2020). iScience 23:101060. doi:10.1016/j.isci.2020.101060 [db, PubMed 전문은 이전 검토가 확인]. **본문**(이전 검토 기준). 정서 모형과 73개 의미 모형을 따로 적합해 transmodal 영역에서 정서 모형이 우세하다고 보고했다. joint 분할은 아니다.
3. Abdel-Ghaffar SA et al. (2024). Nat Commun. doi:10.1038/s41467-024-49073-8 [db]. **초록**(이전 검토 기준). 정서 이미지에서 후두-측두 피질이 의미와 정서 feature에 함께 tuning되어 있음을 보였다.

**(b) 판정: partially.** 같은 자료에서 정서와 의미 공변량을 함께 넣은 분석은 이미 있다(Du 2023). 남는 새 부분은 다음 넷이다.
* 공변량이 사람이 쓴 정서 배제 장면 기술 20개라는 풍부한 의미 표상이다. 73개 개념 평정보다 풍부하다.
* 캡션 split-half로 공변량 측정 오차를 보정한다.
* 고유 분산을 명시적으로 추정한다. Du 2023은 고유 분산을 보고하지 않았다.
* 독립 코호트(Mind captioning)에서 재현한다.

**(c) 좁히는 방법**
* 0단계 재현 목표(V11)에 Du 2023의 banded ridge 결과를 추가한다. 73개 의미 band만으로 얻는 정서 고유 분산을 먼저 재현하고, 캡션 band로 바꿨을 때 그 값이 얼마나 줄어드는지를 주 산출물로 둔다.
* 이렇게 하면 "의미 공변량을 풍부하게 하고 측정 오차를 보정하면 정서 고유 분산은 얼마나 남는가"라는 질문만 남는다. 이것은 Du 2023의 Limitations가 직접 요구한 다음 단계다.
* "정서 표상이 의미와 구분된다"를 처음 보이는 연구로 쓰지 않는다.

### RQ-10. 정서 encoder의 전향 선택이 새 피험자에서도 맞는가

**(a) 가장 가까운 선행**
1. Tuckute G et al. (2024). Driving and suppressing the human language network using large language models. Nat Hum Behav. doi:10.1038/s41562-023-01783-7, PMID 38172630 [PubMed, db]. **초록**(db 기록은 본문). 모델이 고른 문장이 새 개인에게서 실제로 언어망 반응을 높이거나 낮췄다. 새 fMRI를 수집한 검증이다.
2. Ratan Murty NA, Bashivan P, Abate A, DiCarlo JJ, Kanwisher N (2021). Computational models of category-selective brain regions enable high-throughput tests of selectivity. Nat Commun 12:5540. doi:10.1038/s41467-021-25409-6, PMID 34545079 [PubMed]. **초록**. FFA, PPA, EBA encoding model이 새 이미지 반응을 예측했고, 고반응 예측 이미지를 선별, 합성해 범주 선택성 주장을 강하게 시험했다.
3. NeuroVolve, arXiv:2512.00557 [db]. **초록**(db 기준). amygdala 최대화 생성 이미지를 in vivo로 검증했다. High 조건은 Natural Zero보다 높았지만 Natural High보다 높지 않았다.

**(b) 판정: partially.** "encoder로 고른 자극을 새 피험자에서 검증한다"는 논리는 언어망과 범주 영역에서 이미 수행되었다. amygdala에서는 생성 자극으로 수행되었다. 남는 새 부분은 정서 encoder와 시각-의미 encoder가 서로 다른 클립을 고르는 경우(controversial 선택)에 정서 영역에서 어느 쪽이 맞는지를 코호트 간으로 보는 것이다.

**(c) 좁히는 방법**
* 주 산출물을 "정서 encoder 대 시각-의미 encoder의 controversial 클립에서의 승패"(Golan 2020 논리) 하나로 줄인다.
* 단순 구동/억제 성공률은 보조로 둔다. Tuckute 2024와 Ratan Murty 2021이 이미 보인 종류의 결과이기 때문이다.
* 검증 코호트가 이미 수집되고 전처리된 자료라서 새 fMRI 검증보다 약하다는 점을 명시한다. 선택 목록과 코드는 해시와 시점 기록으로 봉인한다.
* 남는 새 부분이 작으므로 Shortlist 우선순위는 중간 이하로 본다.

### RQ-15. AI 내부 표상 대 AI 출력 중 무엇이 뇌와 더 맞는가

**(a) 가장 가까운 선행**
1. Du C et al. (2025). Bridging the behavior-neural gap. arXiv:2509.24298 [db, arXiv]. **본문**(db 기록). MLLM triplet 판단(출력)에서 만든 embedding이 인간 평정보다 정서 영역 fMRI를 잘 예측했다. 출력만 다룬다.
2. Huang Y, Zhang Z, Biswal B (2026). Brain-Aligned Multimodal LLMs for Social and Emotional Understanding of Cartoon Movies. arXiv:2610.22706 [arXiv]. **초록**. MLLM의 연속 평정(출력)과 인간 평정을 각각 encoding 회귀자로 썼다. 공간 중첩은 주로 MLLM끼리였다.
3. Zhang J, Zhong L et al. (2025). Decoding Emotion in the Deep. arXiv:2510.04064 [arXiv]. **초록**. LLM hidden state의 정서 probe가 zero-shot prompting보다 정확했다. 뇌 자료는 없다.

**(b) 판정: not found.** 출력 기반 표상과 뇌의 비교(1, 2), 내부 표상과 출력의 행동 수준 비교(3)는 각각 있다. 같은 모델, 같은 forward pass에서 내부 표상과 출력 중 무엇이 뇌의 정서 분산을 더 고유하게 설명하는지를 비교한 연구는 찾지 못했다. matrix의 "partially(Du 2025)"는 인접 선행을 직접 선행으로 센 것이라 고친다.

**(c)** 질문을 좁힐 필요는 없다. 다만 다음을 대조로 넣는다.
* Asanuma 2025(doi:10.1038/s41598-025-14961-6, db)와 Santavirta 2025(bioRxiv, db)도 출력 기반이다.
* C&K 클립과 라벨이 공개 웹 지도에 있어 출력이 기억에 기댈 수 있다. 이것이 내부 표상 대 출력의 차이를 만들 수 있으므로 오염 대조(라벨 없는 다른 자극에서의 같은 비교)를 둔다.

### RQ-01. 범주 구조가 다른 코호트에서도 재현되는가

**(a) 가장 가까운 선행**
1. Du C et al. (2023). doi:10.1016/j.isci.2023.107571 [PubMed]. **본문**. 같은 Horikawa 자료에서 encoding weight의 PCA로 affective space를 추정했다. 정서 범주 표상이 피질 위에서 넓게 겹치고 부드러운 gradient를 이룬다고 보고했다. 연속 쪽 해석이다.
2. Westlin C et al. (2025). arXiv:2507.00320 [db]. **본문**(db 기록). 같은 자료의 비지도 군집이 피험자마다 11~14개였다. 범주와의 NMI는 0.014였고 세션과의 NMI는 0.19였다.
3. Koide-Majima N, Nakai T, Nishimoto S (2020). Distinct dimensions of emotion in the human brain and their representation on the cortical surface. NeuroImage 222:117258. doi:10.1016/j.neuroimage.2020.117258, PMID 32798681 [PubMed, Crossref]. **제목, 서지만**(db 기록은 bioRxiv판 본문). 다른 자료(시청각 영화 클립, 80범주)에서 25개 정서 차원을 보고했다.
* 보조 선행:
  * EmoMind(arXiv:2605.16739 [arXiv], HTML 본문 일부 확인): Mind captioning 6명(학습 2,036, 시험 72)과 Horikawa 5명을 함께 썼다. Horikawa는 교차 데이터셋 평가에만 썼다. 피험자 특이 정서 구조가 전달된다고 보고했지만 공유 스펙트럼이나 범주 대 연속 비교는 하지 않았다.
  * Azari 2020(doi:10.1038/s41598-020-77117-8, db): 비지도 군집이 범주 라벨과 대응하지 않았다.

**(b) 판정: partially.** 같은 자료에서 범주(Horikawa 2020), 연속 gradient(Du 2023), 개인 특이 군집(Westlin 2025)의 세 해석이 이미 각각 나왔다. 남는 새 부분은 두 가지다.
* 독립 코호트 간에 재현되는 신뢰 대역으로 범위를 제한한다.
* 그 대역 안에서 세 해석을 같은 held-out 기준으로 맞대 비교한다.

**(c) 좁히는 방법**
* 주 산출물을 "코호트 간 재현 대역 안에서 세 모형(범주 혼합, 연속 잠재, 개인 특이 군집)의 held-out 우도 순위" 하나로 정한다.
* "정서 신경 공간의 차원 수"를 새 발견처럼 쓰지 않는다. Cowen & Keltner 2017과 Koide-Majima 2020이 이미 보고했다.
* 0단계 재현 대상에 Du 2023의 affective space 결과를 추가한다.

### RQ-03. 정서 기하는 자극 집합의 산물인가

**(a) 가장 가까운 선행**
1. Stringer C et al. (2019). High-dimensional geometry of population responses in visual cortex. Nature. doi:10.1038/s41586-019-1346-5 [db]. **db 기록**. 마우스 V1에서 자극 앙상블의 차원이 낮을수록 power-law 지수가 커진다고 예측했고 실험으로 확인했다.
2. Gauthaman RM, Ménard B, Bonner MF (2024). arXiv:2409.06843 [db]. **본문**(db 기록). 인간 fMRI(NSD)에서 개인 간 공유되는 scale-free 스펙트럼을 보고했다. 자극 부분집합 조작은 하지 않았다.
3. 해당 없음(검색에서 정서 fMRI의 자극 집합 조작 연구를 찾지 못함).

**(b) 판정: not found.** 인간 fMRI에서 같은 자극 풀의 부분집합 다양성을 조작해 스펙트럼 지수가 무엇을 따라 바뀌는지 본 연구는 찾지 못했다. 정서 영역 대상 연구도 찾지 못했다.

**(c)** 유지한다. Stringer 2019의 이론 예측("앙상블 차원이 낮으면 지수가 커진다")을 사전 등록 예측으로 쓰면 반증 가능성이 높아진다.

### RQ-33. 앞 장면이 같은 장면의 정서 표상을 끌어당기는가, 밀어내는가

**(a) 가장 가까운 선행**
1. Van der Burg E, Toet A, Brouwer AM, van Erp JBF (2021). Serial Dependence of Emotion Within and Between Stimulus Sensory Modalities. Multisens Res. doi:10.1163/22134808-bja10064 [PubMed]. **초록**. 무작위 순서의 정서 소리와 이미지에서 valence, arousal 평정이 직전 자극 쪽으로 끌렸다(양의 serial dependence). 직전 시행을 수동으로 보기만 해도 나타났다. 저자는 이를 정서 네트워크의 잔여 활성으로 해석했다.
2. Ortega J, Chen Z, Whitney D (2023). Serial dependence in emotion perception mirrors the autocorrelations in natural emotion statistics. J Vis 23(3):12. doi:10.1167/jov.23.3.12 [PubMed]. **초록**. 영화의 정서 자기상관을 측정했다. 정서 지각이 약 12초 이상에 걸쳐 평활되었다.
3. Mobbs 2006(doi:10.1093/scan/nsl014, db)과 Cao 2024(doi:10.1371/journal.pone.0308295, db): 통제된 얼굴-장면 설계에서 정서 맥락이 중립 얼굴의 해석과 뇌 반응을 바꿨다. 보조로 Pichon 2015(RQ-26 참조).

**(b) 판정: partially.** 직전 정서 맥락이 현재 자극의 정서 판단과 뇌 반응을 바꾼다는 것은 행동(동화 방향)과 통제된 fMRI 설계에서 확립되어 있다. 남는 새 부분은 자연 클립의 무작위 연쇄에서 신경 정서 부분공간 표상이 이동하는 부호다.

**(c) 좁히는 방법**
* 이번 검색으로 설계상 중요한 점을 찾았다. 선행이 예측하는 방향은 동화다. 그런데 Mind captioning에서 block 사이 휴지는 2 s이고, HRF 잔여가 만드는 가짜 효과도 동화 방향이다. Ortega 2023의 평활 시간척도(약 12 s)도 block 길이(10 s 이상 + 2 s)와 겹친다.
* 따라서 "동화가 나왔다"는 결과만으로는 정서 효과와 HRF를 구분할 수 없다. 다음 둘을 주 검정으로 둔다.
  * 영역별 HRF로 예측한 동화량을 넘는 초과분.
  * 정서 부분공간과 시각 부분공간의 차이.
* 대비 방향 결과는 진단력이 있다. 그러므로 대비를 예측하는 조건(예: 정서 차이가 큰 쌍)을 사전 등록해 따로 본다.

### RQ-60. 무음 영상의 암시된 소리가 청각피질에서 정서를 싣는가

**(a) 가장 가까운 선행**
1. Meyer K, Kaplan JT, Essex R, Webber C, Damasio H, Damasio A (2010). Predicting visual stimuli on the basis of activity in auditory cortices. Nat Neurosci 13:667-668. doi:10.1038/nn.2533, PMID 20436482 [PubMed]. **초록**. 소리를 암시하는 무음 영상을 볼 때 초기 청각피질 활동이 동물, 악기, 사물의 소리 종류를 구분했다.
2. Man K, Kaplan JT, Damasio A, Meyer K (2012). Sight and sound converge to form modality-invariant representations in temporoparietal cortex. J Neurosci. doi:10.1523/JNEUROSCI.2342-12.2012, PMID 23175818 [PubMed]. **초록**. 후측 STS가 보기와 듣기에 걸쳐 내용 특이적이고 양식 불변인 표상을 가졌다.
3. 해당 없음. V2A 생성 모델 feature와 뇌의 연결은 찾지 못했다.

**(b) 판정: partially.** 질문의 앞부분("무음 시청 때 청각피질이 암시된 소리를 표상하는가")은 Meyer 2010이 이미 보였다. 남는 새 부분은 두 가지다.
* V2A 생성 모델이 계산한 암시 소리 표상이 자연 무음 클립의 청각피질 분산을 그 모델 자신의 시각 조건 embedding 이상으로 설명하는가.
* 그 성분이 정서 정보를 싣는가.

**(c) 좁히는 방법**
* 질문 문장에서 "청각피질은 암시된 소리를 표상하는가"를 발견으로 쓰지 않는다. Meyer 2010을 전제로 인용한다.
* 주 검정은 "V2A 시각 조건 embedding 위에서 생성 소리 feature의 고유 분산"과 "그 고유 성분의 정서 해독력" 둘로 한정한다.

### RQ-32. 각성은 뇌 상태의 위치인가, 변화 속도인가

**(a) 가장 가까운 선행**
1. Ke J, Song H, Bai Z, Rosenberg MD, Leong YC (2025). Dynamic brain connectivity predicts emotional arousal during naturalistic movie-watching. PLoS Comput Biol 21:e1012994. doi:10.1371/journal.pcbi.1012994, PMID 40215238 [PubMed]. **초록**. 동적 FC로 순간 arousal을 예측했다. 이 예측은 다른 참가자, 다른 영화로 일반화되었고 valence는 일반화되지 않았다.
2. van der Meer JN, Breakspear M, Chang LJ, Sonkusare S, Cocchi L (2020). Movie viewing elicits rich and reliable brain state dynamics. Nat Commun 11:5004. doi:10.1038/s41467-020-18717-w, PMID 33020473 [PubMed]. **초록**. HMM 뇌 상태의 발현이 생리 상태(심박, 동공)와 주관적 몰입과 공변했다.
3. Nguyen TT, Etzel JA, Bezdek MA, Zacks JM (2026). Multiple event segmentation mechanisms in the human brain. eLife. doi:10.7554/eLife.107955 [Crossref, db]. **초록**(db 기록). 사건 경계 주변에서 영역별 패턴 이동이 일어났다.

**(b) 판정: not found.** arousal을 상태 공간의 위치(평균 활성)가 아니라 TR 간 패턴 변화 속도로 정의하고, 둘을 경쟁 회귀자로 arousal 평정과 EDA에 맞대는 검정은 찾지 못했다. 위 셋은 각각 연결성 패턴, 상태 발현, 경계 이동을 다룬다.

**(c)** 유지한다. 두 가지를 반드시 넣는다.
* Ke 2025의 공개 동적 FC 모형을 경쟁 기준선으로 둔다. 속도가 동적 FC보다 arousal을 더 잘 추적해야 새 주장이 된다.
* Nguyen 2026식 사건 경계 이동을 통제한다.

### RQ-43. vividness 보고는 내성인가, 기억성인가

**(a) 가장 가까운 선행**
1. St-Laurent M, Abdi H, Buchsbaum BR (2015). Distributed Patterns of Reactivation Predict Vividness of Recollection. J Cogn Neurosci 27:2000-2018. doi:10.1162/jocn_a_00839, PMID 26102224 [PubMed, Crossref]. **초록**.
   * 짧은 영상을 보고 머릿속으로 다시 재생하게 했다.
   * 지각으로 학습한 분류기의 회상 시 정확도가 vividness와 양의 상관을 보였다.
   * 회상 영상과 무관하게 vividness와 분류기 강도를 함께 예측하는 영역도 찾았다.
   * 본문에 접근하지 못해 영상 수와 영상당 반복 횟수(item 안 분석 여부)는 확인하지 못했다.
2. Barker RM, St-Laurent M, Buchsbaum BR (2022). Neural reactivation and judgements of vividness reveal separable contributions to mnemonic representation. NeuroImage 255:119205. doi:10.1016/j.neuroimage.2022.119205, PMID 35427774 [PubMed]. **초록**. 데이터셋 4개를 합쳐 재활성과 vividness의 공통 기반과 분리 성분을 보였다. vividness에는 선조체와 배측 주의망이 더 관여했다.
3. Bainbridge WA, Rissman J (2018). Dissociating neural markers of stimulus memorability and subjective recognition during episodic retrieval. Sci Rep 8:8679. doi:10.1038/s41598-018-26467-5, PMID 29875370 [PubMed]. **초록**. 자극 기억성(item 중심)과 개인 기억 판단(관찰자 중심)이 서로 겹치지 않는 영역에 표상되었다.

**(b) 판정: partially(done에 가까움).** "재활성이 vividness를 예측한다"(1, 2)와 "item 기억성과 주관 판단은 신경적으로 분리된다"(3)가 이미 있다. 남는 새 부분은 셋이다.
* 같은 클립 반복 회상(5회)으로 vividness를 item 간 성분과 item 안 성분으로 나눈다.
* 각 성분이 본인 재활성을 따르는지 직접 본다.
* 정서 부분공간을 쓴다.
* 1번 연구가 이미 item 안 분석을 했다면 남는 부분은 더 줄어든다. 확인이 필요하다.

**(c) 좁히는 방법과 권고**
* 질문을 "item 간 성분(타인 vividness로 예측)을 통제한 뒤에도 item 안 vividness 변동이 본인 정서 재활성을 따르는가" 하나로 줄인다.
* Mind captioning은 6명이고 vividness가 3~4점에 몰려 있다. 이 축소판의 검정력은 낮다.
* 남는 새 부분이 13개 중 가장 작다. 독립 Shortlist 자리보다 RQ-41(정서 재활성과 vividness)의 하위 분석으로 흡수하는 것을 권고한다. 빈 자리는 교체 후보 중 not found인 RQ-14로 채우는 것을 권고한다(구속력 없음).

### RQ-44. 회상된 정서는 흔적인가, 재구성인가

**(a) 가장 가까운 선행**
1. Chen J, Leong YC, Honey CJ, Yong CH, Norman KA, Hasson U (2017). Shared memories reveal shared structure in neural activity across individuals. Nat Neurosci 20:115-125. doi:10.1038/nn.4450, PMID 27918531 [PubMed]. **초록**. 영화 회상 때 사건별 패턴이 재현되었다. 많은 고차 영역에서 같은 사건을 회상하는 사람끼리의 패턴이 회상과 지각 사이보다 더 비슷했다. 저자는 이를 지각이 기억으로 체계적으로 재구성되는 것으로 해석했다.
2. Favila SE, Kuhl BA, Winawer J (2022). Perception and memory have distinct spatial tuning properties in human visual cortex. Nat Commun 13:5864. doi:10.1038/s41467-022-33161-8, PMID 36257949 [PubMed]. **초록**. 기억 반응의 공간 튜닝이 지각과 체계적으로 달랐다.
3. Spens E, Burgess N (2024). A generative model of memory construction and consolidation. Nat Hum Behav. doi:10.1038/s41562-023-01799-z [db]. **초록**(db 기록). 기억의 예측 가능한 요소는 생성 모형(schema)으로 재구성된다는 이론이다.

**(b) 판정: partially.** 회상 표상이 지각의 복제가 아니라 재구성된다는 핵심 주장은 1, 2가 이미 보였다. Mind captioning 원 논문도 지각 학습 decoder가 회상 내용 기술로 일반화됨을 보였다. 남는 새 부분은 두 가지다.
* cue에서 생성한 영상의 encoding 예측을 재구성 가설의 계산 대리로 쓴다.
* 정서 부분공간과 시각 부분공간에서 원 클립 예측과 재구성 예측의 상대 근접성을 비교한다.

**(c) 좁히는 방법**
* "회상은 재구성인가"를 묻지 않는다(이미 지지됨). "정서 부분공간이 시각 부분공간보다 schema(캡션, cue 생성 영상) 쪽에 더 가까운가"로 좁힌다.
* cue가 곧 캡션이라 세 예측이 공선적이다. 차이 검정은 부분상관과 판정 불가 구역을 사전에 정의해 수행한다.

### RQ-14. '누가 누구에게 무엇을 했는가' 구조가 정서 반응을 설명하는가

**(a) 가장 가까운 선행**
1. Marras L et al. (2025). Neural representation of action features across sensory modalities: A multimodal fMRI study. NeuroImage 319:121439. doi:10.1016/j.neuroimage.2025.121439, PMID 40897257 [PubMed]. **초록**. 행동 feature를 Space, Effector, Agent & Object, Social, Emotion, Linguistic의 6영역으로 나눴다. 같은 영화의 시청각, 시각, 청각판 fMRI를 encoding과 variance partitioning으로 분석했다. AON 예측에는 Effector와 Social이 가장 크게 기여했다. 수작업 주석이고 appraisal과는 연결하지 않았다.
2. Thornton MA, Tamir DI (2024). Nat Commun. doi:10.1038/s41467-024-44870-7 [db]. **초록**(db 기록). 상황과 정신상태의 신경 패턴이 그것이 허용하는 행동 패턴의 가중합으로 재구성되었다.
3. Mohammadi G, Van De Ville D, Vuilleumier P (2023). Brain networks subserving functional core processes of emotions identified with componential modeling. Cereb Cortex. doi:10.1093/cercor/bhad093 [Crossref, db]. **초록**(db 기록). 영화의 정서 순간을 32개 성분으로 평정했고, appraisal과 행동 경향 과정을 담당하는 네트워크 조합을 보고했다.

**(b) 판정: not found.** 행위자, 대상 feature로 영화 fMRI를 encoding한 연구(1)와 appraisal 성분의 네트워크 연구(3)는 있다. 사건-의미역 표상(VidSitu 계열)이 appraisal(행위 주체, 원인) 평정과 정서 관련 영역 반응을 물체/장면 feature와 캡션 embedding 이상으로 설명하는지를 검정한 연구는 찾지 못했다.

**(c)** 질문을 유지한다. Marras 2025의 Agent & Object 영역 결과(AON에서 기여가 작음)를 경쟁 예측으로 인용한다. 교체 후보 셋 중 Novelty 면에서 가장 강하다. RQ-43 자리에 넣는 것을 권고한다.

### RQ-25. 영화 속 놀람은 어떤 예측 실패에 묶이는가

**(a) 가장 가까운 선행**
1. Nguyen TT, Etzel JA, Bezdek MA, Zacks JM (2026). Multiple event segmentation mechanisms in the human brain. eLife. doi:10.7554/eLife.107955 [Crossref, db]. **초록**(db 기록). 영화 fMRI에서 예측오차형 사건 경계는 복외측 전전두의 이른 패턴 이동과, 불확실성형 경계는 배측 주의망 두정 이동과 연결되었다. 오차 대 불확실성의 신경 해리가 영화 자료에서 이미 보고된 것이다.
2. Mohammadi 2023(doi:10.1093/cercor/bhad093 [Crossref]). **초록**(db 기록). novelty를 포함한 appraisal 성분이 영화 fMRI의 네트워크와 연결되었다.
3. Garrido Q et al. (2025). arXiv:2502.11831 [db]. **본문**(db 기록). V-JEPA의 surprise 지표가 물리적으로 불가능한 영상에서 커졌다. 모델 수준 연구다.

**(b) 판정: partially.** 영화 fMRI에서 오차형과 불확실성형 예측 신호가 다른 영역과 연결된다는 해리는 이미 보고되었다(1). 남는 새 부분은 두 가지다.
* world model의 오차와 불확실성을 정서 appraisal 두 유형(Suddenly 대 Predictable, Urgency)에 대응시킨다.
* amygdala, insula 반응과 연결한다.

**(c) 좁히는 방법**
* Nguyen 2026의 두 경계 유형을 경쟁 회귀자로 넣는다. 그 위에서 정서 appraisal과 정서 영역에 남는 고유 설명량만 주장한다.
* Tambini 2017만 선행으로 적은 matrix 판정은 가장 가까운 선행을 놓쳤다.

### RQ-26. 앞 영상의 정서는 다음 영상까지 남는가

**(a) 가장 가까운 선행**
1. Pichon S, Miendlarzewska EA, Eryilmaz H, Vuilleumier P (2015). Cumulative activation during positive and negative events and state anxiety predicts subsequent inertia of amygdala reactivity. Soc Cogn Affect Neurosci 10:180-190. doi:10.1093/scan/nsu044, PMID 24603023 [PubMed]. **초록**. 정서 영화 뒤 무관한 과제의 공포 얼굴에 대한 amygdala 반응이 영화의 valence에 따라 커지거나 줄었다. 그 크기는 영화 중 누적 amygdala 활성으로 예측되었다.
2. Gaviria J et al. (2021). Brain functional connectivity dynamics at rest in the aftermath of affective and cognitive challenges. Hum Brain Mapp 42:1054-1069. doi:10.1002/hbm.25277, PMID 33231916 [PubMed]. **초록**. 부정 정서 영화 뒤 휴지기의 DMN 공활성 패턴 시간 지표가 바뀌었다. 그 변화가 주관 정서 변화를 예측했다.
3. Qiao-Tasserit E et al. (2017). Transient emotional events and individual affective traits affect emotion recognition in a perceptual decision-making task. PLoS One 12:e0171375. doi:10.1371/journal.pone.0171375, PMID 28151976 [PubMed]. **초록**. 부정 클립 뒤 수 분 동안 모호한 얼굴을 공포로 분류하는 경향이 커졌다(행동).

**(b) 판정: partially.** 정서 상태가 자극 뒤에 남아 후속 처리를 바꾼다는 관성은 분에서 수십 분 척도로 확립되어 있다(1, 2, 3, Tambini 2017). 남는 새 부분은 두 가지다.
* 수 초 척도의 클립 간 이월을 데이터셋 안의 무작위 순서로 본다.
* 정서 부분공간과 시각 부분공간의 감쇠를 영역별 HRF 보정 뒤 비교한다.

**(c) 좁히는 방법**
* "정서 관성이 있는가"가 아니라 "HRF와 시각 이월로 설명되지 않는 수 초 척도의 정서 부분공간 이월이 있는가"로 좁힌다.
* 선행이 보인 분 단위 효과(Pichon 2015, Qiao-Tasserit 2017)를 예측 상한으로 쓴다.
* RQ-33과 같은 자료, 같은 HRF 문제를 공유하므로 둘 중 하나만 Shortlist에 두는 것이 효율적이다.

---

## 3. 교체 권고

* **done 판정이 없으므로 규칙상 의무 교체는 없다.**
* **권고(구속력 없음):** RQ-43을 RQ-41의 하위 분석으로 흡수하고, 빈 자리를 RQ-14로 채운다.
  * RQ-43은 남는 새 부분이 가장 작다(St-Laurent 2015, Barker 2022, Bainbridge & Rissman 2018).
  * Mind captioning 6명과 좁은 vividness 분포로는 그 남는 부분의 검정력도 낮다.
  * RQ-14는 이번 검색에서 not found였다.
* **우선순위 하향 검토:**
  * RQ-10: 남는 새 부분이 controversial 선택 하나이고, 검증이 기존 자료라 Tuckute 2024보다 약하다.
  * RQ-33과 RQ-26은 같은 자료와 같은 HRF 문제를 공유한다. 둘 다 Shortlist에 두면 실제 독립 연구 단위는 하나다. Shortlist에는 RQ-33만 있으므로 현재 구성은 문제없다.

---

## 4. 동의 편향 점검

* 판정 분포는 partially 9, not found 4, done 0이다.
* done에 가장 가까웠던 경우는 셋이다.
  * RQ-43: 재활성과 vividness, 기억성과 주관 판단의 해리가 각각 있다.
  * RQ-10: 같은 논리가 두 영역에서 새 데이터로 검증되었다.
  * RQ-60: 질문 앞부분은 Meyer 2010이 수행했다.
* 셋을 done으로 판정하지 않은 이유는 0절 기준의 "같은 가설을 같은 종류의 증거로"가 충족되지 않았기 때문이다. 정서 구성개념이나 비교 구조가 다르다.
* 반대로 이전 판정을 partially에서 not found로 올린 경우도 하나 있다(RQ-15). 이번 판정이 모두 한 방향(새로움 하향)으로만 움직이지는 않았다.
* matrix와 이전 검토가 놓친 가장 가까운 선행을 이번에 찾은 경우:
  * RQ-08: Du 2023.
  * RQ-01: Du 2023.
  * RQ-25: Nguyen 2026. 근거 ID 목록에는 있었지만 선행 판정에 쓰이지 않았다.
  * RQ-43: St-Laurent 2015, Barker 2022.
  * RQ-44: Chen 2017, Favila 2022.
  * RQ-33: 행동 serial dependence 문헌.
  * RQ-10: Ratan Murty 2021.
  * RQ-26: Gaviria 2021, Qiao-Tasserit 2017.

---

## 5. 미확인 사항

* St-Laurent 2015 본문: 영상 수와 영상당 회상 반복 수, item 안 분석 여부. 프록시가 403을 반환했다. RQ-43 판정이 done 쪽으로 더 갈 수 있다.
* Ratan Murty 2021이 선별 이미지를 새 fMRI로 측정했는지는 초록만으로 확정하지 못했다.
* Koide-Majima 2020, Tuckute 2024, Mohammadi 2023, Nguyen 2026, Stringer 2019, Gauthaman 2024, Westlin 2025, Spens & Burgess 2024의 내용은 이번 세션에서 직접 읽지 않았고 literature_db 기록에 기댔다. 식별자는 PubMed, Crossref, 또는 db로 확인했다.
* bioRxiv 전용 검색과 Google Scholar는 쓰지 못했다. 2025~2026년 bioRxiv 전용 preprint는 놓쳤을 수 있다.
* WebSearch 결과 요약에 나온 다음 항목은 식별자를 확인하지 않아 근거로 쓰지 않았다.
  * Čeko 2022.
  * Peter, Kim, DiCarlo 2026 preprint.
  * Sherlock DMN surprise 연구.
  * CCN 학회 초록들.

---

## 6. 검색 기록 (모두 2026-11-12)

| RQ | # | 경로 | 질의 | 결과 |
|---|---|---|---|---|
| 01 | 1 | WebSearch | Horikawa 2020 emotion fMRI dataset reanalysis categorical versus continuous latent shared response across subjects 2025 2026 arXiv | Westlin 2025만. SRM, 범주 대 연속 비교 없음 |
| 01 | 2 | PubMed | emotion categories fMRI individual differences clustering hyperalignment naturalistic videos (2020~) | 0건 |
| 01 | 3 | arXiv API | abs:"Cowen" AND abs:fMRI | 0건 |
| 01 | 4 | PubMed | "Topographic representation of visually evoked emotional experiences in the human cerebral cortex" | PMID 37664621(Du 2023), PMC 본문 확인 |
| 01 | 5 | PubMed(평가 단계) | Koide-Majima[Author] AND emotion AND cortical | PMID 32798681 |
| 08 | 1 | PubMed | (emotion* OR affective) AND (caption* OR "language model" OR "semantic features" OR "semantic content") AND ("variance partitioning" OR "unique variance" OR "encoding model") AND (video* OR movie* OR film*) AND fMRI (2019~) | 0건 |
| 08 | 2 | WebSearch | emotion representation beyond semantic description captions fMRI unique variance Cowen Keltner videos language model embeddings 2025 2026 | Horikawa 2020, Du 2025, EmoMind, Westlin. 캡션 고유 분산 분석 없음 |
| 08 | 3 | arXiv API | abs:emotion AND abs:fMRI AND (abs:caption OR abs:captions) | 1건(EmoMind) |
| 08 | 4 | PubMed 전문 | PMC10470388(Du 2023) Methods, Limitations | 73개 의미 평정 band 확인 |
| 10 | 1 | WebSearch | encoding model selects stimuli to drive or suppress amygdala emotion regions validated in new participants fMRI model-guided stimulus selection | Jang & Kragel 2025 등. 정서 영역의 새 피험자 검증 없음 |
| 10 | 2 | PubMed | ("encoding model" OR "neural network model") AND (drive OR suppress OR "model-selected" OR "predicted to") AND (amygdala OR emotion OR affective) AND fMRI AND (new participants OR independent OR prospective) (2019~) | 0건 |
| 10 | 3 | PubMed | Ratan Murty[Author] AND category-selective AND computational models | PMID 34545079 |
| 10 | 4 | PubMed | Tuckute G[Author] AND language network AND drive suppress | PMID 38172630 |
| 15 | 1 | arXiv API | all:"emotion" AND all:"fMRI" AND (hidden states OR probe OR probing) AND (language model OR MLLM) | 1건(EmoMind) |
| 15 | 2 | WebSearch | LLM internal emotion representations probing hidden states align with human brain fMRI compared to model self-reported emotion ratings | Du 2025, arXiv:2510.04064 등. 직접 비교 없음 |
| 15 | 3 | arXiv API | abs:emotion AND abs:fMRI AND (LLM OR vision-language OR multimodal), 최신순 | arXiv:2610.22706, 2606.07707 |
| 15 | 4 | WebSearch | "prompting" versus "probing" language model internal representations versus verbal judgments alignment with human brain or human similarity judgments emotion | 직접 비교 없음 |
| 03 | 1 | PubMed | ("stimulus set" OR "stimulus sampling" OR "stimulus selection" OR "stimulus ensemble") AND ("representational geometry" OR dimensionality OR "representational similarity") AND fMRI AND (emotion* OR affective OR valence) (2015~) | 1건(무관한 논평) |
| 03 | 2 | WebSearch | dependence of neural representational dimensionality on stimulus distribution emotion videos fMRI subsampling visual diversity emotional diversity | 없음 |
| 03 | 3 | WebSearch(평가 단계) | fMRI eigenspectrum power-law exponent depends on stimulus set diversity subsampling | 없음(Stringer 2019, 데이터셋 간 지수 차이만) |
| 33 | 1 | PubMed | ("serial dependence" OR carryover OR "carry-over" OR spillover OR "context effect") AND (emotion OR emotional OR affective) AND fMRI AND (film OR video OR clip OR movie) (2010~) | 1건(Gaviria 2021) |
| 33 | 2 | WebSearch | Kuleshov effect fMRI preceding emotional context naturalistic video sequence neural representation assimilation contrast current clip | Mobbs 2006, Cao 2024, Calbi 2019(EEG) |
| 33 | 3 | PubMed | "serial dependence" AND (emotion* OR "facial expression" OR affective) (2014~) | 12건(Van der Burg 2021, Ortega 2023, Liberman 2018 등, 모두 행동) |
| 33 | 4 | PubMed | neutral faces preceded by emotional pictures amygdala fMRI affective context valence of preceding picture | 0건 |
| 60 | 1 | PubMed | (silent OR "sound-implying" OR "implied sound" OR "implied auditory") AND ("auditory cortex" OR "auditory cortices") AND (video* OR movie* OR film*) AND (fMRI OR MVPA OR multivariate) (2008~) | 2건(무관) |
| 60 | 2 | WebSearch | video-to-audio generated sound features predict auditory cortex fMRI responses silent videos encoding model implied sound 2024 2025 2026 | 없음 |
| 60 | 3 | PubMed | Meyer K[Author] AND Damasio[Author] AND auditory cortex | Meyer 2010, Man 2012, Man 2015 |
| 60 | 4 | arXiv API | (abs:"video-to-audio" OR abs:"silent video") AND (abs:fMRI OR abs:brain OR abs:"auditory cortex") | 8건, 관련 없음 |
| 32 | 1 | WebSearch | "neural speed" OR "trajectory speed" OR "rate of change" brain state fMRI arousal pupil emotional intensity movie event boundaries pattern shift | 사건 분할(Nguyen 2026)만. arousal-속도 없음 |
| 32 | 2 | PubMed | ("pattern similarity" OR "neural pattern" OR "state transitions") AND (arousal OR "skin conductance" OR pupil) AND (movie OR film OR narrative OR naturalistic) AND fMRI (2015~) | 1건(무관) |
| 32 | 3 | PubMed | (emotional arousal OR arousal) AND ("event boundar*" OR "neural state" OR "brain state") AND (movie OR film OR naturalistic) AND fMRI (2015~) | 0건 |
| 32 | 4, 5 | PubMed, WebSearch(평가 단계) | arousal speed brain state fMRI movie | 0건, van der Meer 2020 인접 |
| 43 | 1 | PubMed | vividness AND (reactivation OR reinstatement) AND (memorability OR "item effects" OR "trial-by-trial" OR "within-item" OR "across items") AND fMRI (2012~) | 0건 |
| 43 | 2 | WebSearch | subjective vividness tracks trial-specific neural reinstatement or stimulus memorability; separating item-level and within-item variance in recollection fMRI metacognition | St-Laurent 2015, Bone 2020, Barker 2022. item 분해 없음 |
| 43 | 3 | PubMed | (St-Laurent M[Author] AND vividness AND reactivation) OR (Bone MB[Author] AND feature-specific reactivation) | 6건 |
| 43 | 4 | PubMed | memorability AND (vividness OR "subjective memory" OR metamemory OR "memory confidence") AND (fMRI OR neural) (2015~) | Bainbridge & Rissman 2018 |
| 43 | 5 | WebSearch | St-Laurent 2015 설계 세부(영상 수, 반복) | 미해결 |
| 44 | 1 | PubMed | (recall OR retrieval) AND (movie OR video OR film) AND (schema OR gist OR semantic) AND (reinstatement OR reactivation) AND (emotion* OR emotional) AND fMRI (2015~) | 0건 |
| 44 | 2 | WebSearch | memory recall neural patterns closer to semantic gist or caption model than to perceptual encoding model fMRI generative reconstruction naturalistic video recall transformation | gist 쪽 재구성 연구들, 모형 비교 없음 |
| 44 | 3 | arXiv API | (recall OR imagery OR memory) AND fMRI AND ("text-to-video" OR "video generation" OR "generative model") | 10건, 직접 없음 |
| 44 | 4 | PubMed | (Chen J AND Hasson U AND shared memories) OR (Favila SE AND perception AND memory AND visual cortex) | Chen 2017, Favila 2022 |
| 44 | 5 | WebSearch(평가 단계) | video recall fMRI reactivation compared to text-to-video generated from cue schema reconstruction | 없음 |
| 14 | 1 | PubMed | appraisal AND (agency OR "causal attribution" OR "other-caused" OR "human caused" OR "intentional harm") AND fMRI AND (movie OR film OR naturalistic OR video) (2012~) | 0건 |
| 14 | 2 | WebSearch | "who did what to whom" event roles agent patient representation fMRI encoding model naturalistic video action semantic structure 2024 2025 | Marras 2025, McMahon 2023 |
| 14 | 3 | PubMed | Marras[Author] AND action AND movie AND encoding (2024~) | PMID 40897257 |
| 14 | 4 | WebSearch(평가 단계) | situation recognition semantic role labeling video features fMRI encoding | 없음 |
| 25 | 1 | WebSearch | video world model prediction error V-JEPA surprise fMRI movie amygdala appraisal suddenness unpredictability encoding 2025 2026 | 직접 없음 |
| 25 | 2 | PubMed | ("prediction error" OR surprise OR unpredictab*) AND ("deep neural network" OR "video prediction" OR "predictive model" OR "self-supervised") AND fMRI AND (movie OR film OR naturalistic) (2018~) | 0건 |
| 25 | 3 | arXiv API | (abs:surprise OR abs:"prediction error") AND abs:fMRI AND (abs:movie OR abs:video OR abs:film) | 0건 |
| 25 | 4 | arXiv API | (abs:V-JEPA OR abs:JEPA) AND (abs:fMRI OR abs:brain) | 25건, surprise-정서 없음 |
| 26 | 1 | PubMed | ("emotional inertia" OR "affective inertia" OR lingering OR persistence OR "emotional aftereffect") AND (amygdala OR "brain state") AND fMRI AND (film OR video OR picture OR pictures) (2010~) | 3건(관련 약함) |
| 26 | 2 | WebSearch | emotional carryover between consecutive stimuli fMRI preceding trial valence affects neural response to current stimulus randomized sequence emotional inertia amygdala | Pichon 2015 등 |
| 26 | 3 | PubMed | Qiao-Tasserit[Author] AND emotional | 3건 |
| 26 | 4 | PubMed | Pichon[Author] AND amygdala AND movies AND threat | PMID 24603023 |
| 공통 | | Crossref API | 10.7554/eLife.107955, 10.1093/cercor/bhad093, 10.1016/j.neuroimage.2020.117258, 10.1162/jocn_a_00839 | 4건 모두 존재 확인 |
