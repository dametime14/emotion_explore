# 재탐색 설계 카드 R1, R2, R3 적대적 검토 (adversarial-reviewer)

* 작성: adversarial-reviewer. 기준일 2026-11-12
* 대상:
  * `outputs/revision/cards/R1_brainlike_emotion_model.md`
  * `outputs/revision/cards/R2_recall_affective_shift.md`
  * `outputs/revision/cards/R3_brain_axes_interpretation.md`
* 배경으로 읽은 것:
  * `outputs/revision/design_brief.md` 전체
  * `outputs/revision/feedback_round2.md` 전체
  * 내 `reviewer_notes.md`와 `prior_overlap_audit.md`
  * `reference/existing_projects.md`
  * Stage 1 보고서(`dataset_Horikawa.md`, `dataset_NSD.md`)의 해당 행
* **독립성:** `outputs/revision/card_theory_review.md`는 열지 않았다. emotion-theory와 의견이 다를 수 있으며 조정하지 않았다.
* 확인 경로 표기:
  * [Crossref]: api.crossref.org
  * [arXiv]: export.arxiv.org API
  * [PubMed]: PubMed 메타데이터
  * [검색만]: WebSearch 요약
  * 프록시가 거부한 호스트(openreview.net, neurips.cc, jov.arvojournals.org, visionsciences.org)는 우회하지 않았다.
* 재채점은 정수 1~5다. 근거는 한 줄이다. 기준 철자는 `scores_reviewer.csv`와 같다.

---

## 0. 요약

| 카드 | 치명적 결함(현재 판) | 예측력 경쟁으로 되돌아갔나 | 참가자 경험 주장 | 재채점 합계(55) | 권고 |
|---|---|---|---|---|---|
| R1 | **있음.** 서명 S1′을 'encoding으로 만든 모델 예측 뇌'에서 계산한다. 그래서 판정이 다시 선형 사상의 유연성과 영역별 encoding 적합도에 묶인다. 비정서 통제의 차원과 신뢰도가 정서 RDM과 맞지 않는다 | **부분적으로 그렇다.** 영역별 encoding 적합도가 모델 예측 뇌의 S1′을 기계적으로 바꾼다 | 1절 질문이 S1′ > 0을 사실처럼 전제한다(경험 주장은 없음) | 34 | 수정 후 진행. 1주차 실측 S1′ 관문 자체가 가장 값진 결과다 |
| R2 | **조건부.** 연속 시계열이 없으면 단서 읽기, 이전 시행 재시청, 같은 시행 재시청 혼입을 실측할 수 없다. 그러면 판정 불가 구역이 임의의 사전 범위(0~30%)로 정해진다 | 아니다. Δ는 측정값이고 decoder 정확도는 관문으로만 쓴다 | 제목의 "감정이 흐려질까"가 참가자 감정으로 읽힐 수 있다. 본문 주장 범위는 모범적이다 | 37 | 진행. raw 재처리(시험, 회상 run만)를 핵심 판에 넣는다 |
| R3 | **있음(고칠 수 있음).** 세 가지다. (1) CCA는 재현 신뢰도가 높은 방향, 즉 내용 쪽을 먼저 고른다. (2) 축 단위 판정이 회전에 의존한다. (3) 내용 묶음을 주성분 20개로 줄여 내용 통제가 부족해지고 U_E가 부풀려진다 | 대체로 아니다. 다만 4단계 V2는 '가설이 기존 묶음보다 더 예측하는가'다. 그래서 VLM이 규범 정서를 더 깨끗이 다시 적는 효과와 구분되지 않는다 | 없다 | 35 | 수정 후 진행. 부분공간 단위 판정을 주 판정으로 바꾼다 |

* **세 카드 공통:**
  * existing_projects 겹침 표기에서 R1과 R2가 'EmoViS'를 따로 적었다. EmoViS는 EmoBrain에 흡수되었으므로 "EmoBrain(구 EmoViS 범위)"로 통일해야 한다(STAGE_STATUS 24번 답).
  * 연구실 팀원 'TRIBE + emotion head' 작업과의 겹침 표기는 맞다. R1만 개념 인접(brain-tuning)이고, R2와 R3는 겹치지 않는다.
* **인용 표본 검증:** 카드별 7~10개를 식별자로 해석했다. 존재하지 않는 식별자는 없었다. 서술 불일치 1건(R2의 Spera 2026), 연도 불일치 1건(R2의 Cocquyt), 내 쪽에서 확인 불가 1건(R1의 Leem 2026 '지름길' 본문 주장)이다(카드별 절).

---

## 1. R1. 뇌를 닮은 장치를 넣고 뺀 AI

### 1.1 반드시 고칠 것 (우선순위순)

1. **주 서명을 '모델 예측 뇌'에서 계산하지 말고 모델 내부 위계에서 계산한다(치명).**
   * 8.1절은 팔마다 층별 특징으로 ROI별 ridge encoding을 학습한다. 그 예측 반응에서 crossnobis, 부분상관, 위계 기울기를 다시 계산한다.
   * 이 '모델 예측 뇌'는 실측 ROI 반응을 모델 특징 공간에 투영한 것이다.
     * transmodal ROI의 encoding 적합도가 낮은 팔은 그 ROI의 예측 반응 분산이 작아진다. 그러면 정서 고유 정보가 작아지고 기울기가 낮아진다.
     * 그래서 팔 사이 S1′ 차이의 상당 부분이 'ROI별 encoding 적합도 프로필'의 차이로 설명된다. design_brief 3절 3번이 금지한 예측력 경쟁이 서명의 모양으로 돌아온 것이다.
     * 층도 ROI마다 중첩 교차검증으로 고르므로 Conwell 2024가 경고한 사상 유연성이 그대로 남는다.
   * **고칠 방법:**
     * 주 판정은 8.1절 6번(모델 층 RDM에서 같은 정서 고유 정보와 비정서 통제를 계산하고 층 깊이 기울기를 보는 것)으로 올린다.
     * 뇌와의 대응은 정서와 무관한 기준으로 미리 고정한 층-영역 배정으로 한다. 예를 들어 NSD 또는 Horikawa 학습 클립에서 비정서 내용 RDM의 재가중 없는 RSA로 층을 배정한다.
     * 모델 예측 뇌 판은 보조로 내리고, 영역별 encoding R²를 공변량으로 같이 보고한다.
   * 비슷한 문제의식의 2026년 방법론 선행이 있다(5절):
     * Höfling et al. 2026(arXiv:2604.21780): 모델은 영역 간 관계 프로필을 재현해야 한다
     * Nakamura et al. 2026(arXiv:2605.20127): 예측 정확도 대신 재현 가능한 응답 차원의 회복 프로필
2. **"재현"의 판정 규칙을 바꾼다.**
   * 지금은 "모델 S1′이 실측 S1′의 95% 구간 안"이면 재현이다. 실측 구간이 넓으면(11명, Horikawa 반복 없음) 여러 팔이 동시에 '재현'된다.
   * 더 큰 문제도 있다. 모델 예측 반응은 잡음이 거의 없는 예측값이다. 그래서 같은 crossnobis 척도라도 실측(잡음 있는 반복)과 크기가 다르다.
   * 고칠 방법:
     * 팔마다 실측 S1′과의 거리를 seed와 피험자 bootstrap으로 낸다.
     * 사전 등록한 쌍 대비 세 개(E-ff 대 A0, E-fb 대 E-ff, B-tm 대 B-rand)의 거리 차이로 판정한다.
     * 척도는 잡음 천장(MC 반복)이나 순위 기반 지표로 맞춘다.
3. **비정서 통제의 차원과 신뢰도를 정서 쪽과 맞춘다.**
   * 정서 RDM은 34범주와 14차원 규범 평정에서 나온다. 비정서 RDM은 캡션에서 AI로 뽑은 속성 몇 개(사람 수, 사회적 상호작용, 행위 강도)에서 나온다.
   * 이렇게 차원 수와 측정 신뢰도가 다르면 "정서 기울기 - 비정서 기울기"(S1′)는 정서 고유성보다 측정 속성 차이를 잴 수 있다.
   * 고칠 방법:
     * Horikawa figshare의 73차원 의미 feature(Stage 1 보고서에 있음, 평정 주체는 미확인)를 주성분 34개로 줄여 주 비정서 통제로 쓴다.
     * AI 추출 속성은 보조로 둔다.
     * 두 RDM의 split-half 신뢰도를 함께 보고한다.
   * R2도 같은 73차원 feature를 비정서 방향으로 쓰므로 두 카드가 맞춰진다.
4. **NSD transmodal brain-tuning의 관문을 둔다.**
   * NSD는 정지 이미지 3회 반복과 연속 재인(old/new) 과제다. 그래서 transmodal(PCC, mPFC, 측두극) beta에는 친숙도와 재인 신호가 크게 섞인다(dataset_NSD.md 209행).
   * transmodal 영역의 자극 구동 신뢰도도 시각 영역보다 훨씬 낮을 것이다.
   * 그대로 조율하면 B-tm은 '고차 장면 의미'가 아니라 '기억, 신기성 신호'에 맞춰지거나 잡음에 맞춰진다. 신뢰도를 맞춘 B-rand도 같이 잡음일 수 있다.
   * 고칠 방법:
     * 1주차에 표적 ROI의 NSD 잡음 천장(ncsnr)을 확인한다.
     * 첫 제시 beta만 쓰거나, 3회 평균 뒤 재인 반응 회귀자를 뺀 beta를 쓴다.
     * 천장이 사전 기준 미만이면 B 팔을 핵심 판에서 뺀다.
   * HCP-MMP 대응은 NSD 공개 atlas 목록에 HCP_MMP1이 피험자 공간으로 들어 있다고 알고 있다. 이번 세션에서 확인하지 못했으므로 1주차에 확인하면 '대응 절차 미확인'이 해소될 수 있다.
5. **팔 수를 줄인다.**
   * 9팔 x seed 3에서 10절 결과 지도처럼 깨끗한 "X만 재현" 패턴이 나올 가능성은 낮다. 상호작용 두 팔(B-tm → E-ff, B-tm → E-fb)은 4주 핵심 판의 판별력을 거의 늘리지 않으면서 비교 수만 늘린다.
   * 핵심 판은 7팔(A0, B-tm, B-vis, B-rand, E-ff, E-fb, E-fb-shuf)로 하고 상호작용은 확장으로 옮긴다.
6. **1절 질문의 전제를 고친다.**
   * "사람 뇌는 정서에만 있는 위계를 보인다(S1′)"를 사실처럼 쓰고 있다. 그러나 이것은 13절의 1주차 관문에서 처음 검정할 가설이다.
   * 질문을 "보인다면, 어떤 장치가 있을 때 재현되는가"의 조건문으로 바꾼다.

### 1.2 고치면 좋은 것

* **S2의 표적을 분명히 한다.**
  * S2 해리는 개념 지식이 약해진 환자의 행동 패턴이다. 실측 대상인 건강한 사람 뇌에서는 해리가 아니라 정상 R_S2가 표적이다.
  * 정서 라벨 없는 팔이 환자형(valence 보존, 부정 범주 붕괴)을 보이고 E 팔이 실측 R_S2에 가까워지는지가 예측이다. 이 논리를 한 문장으로 적는다.
* **위계 기울기를 parcel 단위로 계산한다.** 묶음 4개의 점 4개로 회귀하면 기울기가 불안정하다. HCP360 parcel의 Margulies 경사 값을 써서 parcel 단위로 계산하고, 묶음은 보고용으로만 쓴다.
* **E 팔의 미세조정이 초기 시각 정렬을 낮출 수 있다는 점을 적는다.**
  * 학습이 V1 정렬을 낮춘다는 보고가 있다(Leutenegger 2026, arXiv:2605.30556. 단 저자 정정본이 있고, '모든 학습 규칙에서 V1 정렬이 낮아진다'는 부분만 유지된다).
  * 기울기의 감각 쪽 끝이 바뀌면 S1′이 바뀐다. 층별 변화량(C-20)과 함께 보고한다.
* **Leem 2026 근거를 확인한다.** 4.1절은 "지름길 경로가 Pavlov 조건화에 필요"를 [본문]으로 적었다. 내가 확인한 arXiv 초록(저자 Leem, Keil, Ding, Fang)에는 '지름길'이 없다. 본문 절 번호를 적어 두면 좋다. X1 확장의 근거라 핵심 판에는 영향이 없다.
* **선행 표에 넣을 것:**
  * Höfling 2026, Nakamura 2026(판정 방식의 방법론 선행)
  * Tugsbayar 2026의 정확한 서술: "top-down feedback이 시청각 통합에서 기능 차이를 만든다"(eLife 2026, [Crossref]). 카드의 "시청각 범주화, 정서 아님"은 대체로 맞다.

### 1.3 그대로 둬도 되는 것

* E-ff(매개변수 맞춤 gain 모듈)와 E-fb-shuf로 되먹임 귀속을 통제한 설계(C-05 지적 반영)
* NSD로 조율하고 Horikawa/MC로 평가해 C-06 순환을 끊은 원칙(관문 4번만 더하면 된다)
* 피질하, 재귀, 지형, 학습 자료 조작을 확장으로 뺀 판단과 그 근거(C-07~C-09)
* 13절의 1주차 의사결정 규칙. 특히 "실측 S1′ ≈ 0이면 일반 추상화 위계로 보고"는 사용자 지적에 대한 직접 답이 된다
* 주장 범위(규범 기준, R1 + R0, 충분성)와 Safeguards 표

### 1.4 선행 판정 점검

| 카드 판정 | 점검 결과 |
|---|---|
| ReAlnet-fMRI(arXiv:2407.10414): CORnet을 사람 fMRI로 최적화, 시각 영역, 정서 아님 | [arXiv] 맞음(Lu & Wang 2024) |
| Brainformer(arXiv:2312.00236): 시각 brain-tuning 선행 | [arXiv] 맞음. fMRI 패턴으로 시각 모델에 뇌 기능을 모사하는 틀 |
| Tugsbayar 2026 eLife(doi:10.7554/eLife.105953) | [Crossref] 맞음. top-down feedback, 시청각 통합 |
| Spoerer 2020(doi:10.1371/journal.pcbi.1008215) | [Crossref] 맞음 |
| "정서와 무관한 장면 반응으로 brain-tuning한 모델이 정서 서명을 만드는지 본 연구는 미발견" | 내 검색(arXiv brain-tuned/brain-aligned 20건, WebSearch 1건)에서도 미발견. **판정 유지** |
| "되먹임 조작 + 사람 시각피질 정서 비교 미발견" | WebSearch 1건 추가. 정서 아닌 top-down feedback 모델과 사람 fMRI의 dlPFC-V1 되먹임만 있다. **판정 유지** |
| 판정 방식(서명 재현)의 새로움 | **부분 수정 필요.** 서명이나 관계 프로필로 정렬을 평가하자는 방법론 선행이 2026년에 나왔다(Höfling 2026, Nakamura 2026). 정서 서명에 적용한 것은 새롭다 |

### 1.5 인용 표본 검증 (8개)

| ID | 카드 서술 | 결과 |
|---|---|---|
| arXiv:2407.10414 | ReAlnet-fMRI, CORnet + 사람 fMRI | [arXiv] 일치 |
| arXiv:2312.00236 | Brainformer, 시각 brain-tuning | [arXiv] 일치 |
| doi:10.7554/eLife.105953 | Tugsbayar 2026, top-down feedback | [Crossref] 일치 |
| doi:10.1371/journal.pcbi.1008215 | Spoerer 2020, BLT | [Crossref] 일치 |
| doi:10.1073/pnas.1608282113 | Margulies 2016 주 경사 | [Crossref] 일치 |
| doi:10.1038/s41583-023-00705-w | Doerig 2023 | [Crossref] 일치(neuroconnectionist research programme) |
| doi:10.1523/JNEUROSCI.5487-07.2008 | Hasson 2008 시간 수용 창 위계 | [Crossref] 일치(무음 영화, 정방향, 역방향, 뒤섞기) |
| arXiv:2607.19327 | Leem, Keil, Ding, Fang 2026, "지름길 경로가 조건화에 필요" | 저자와 존재는 [arXiv] 일치. '지름길' 주장은 초록에 없어 내 쪽에서 미확인 |

### 1.6 겹침

* 연구실 팀원 TRIBE 작업: 카드 5절의 '개념 인접'과 다섯 가지 차이가 맞다. TRIBE를 쓰지 않는다.
* existing_projects:
  * "overlap: EmoViS"와 "overlap: EmoBrain"을 따로 적었다. **"overlap: EmoBrain(구 EmoViS 범위)" 하나로 고친다.**
  * brain-tuning을 EmoBrain의 '뇌 정서 정보를 모델 학습에 쓰는 발상'과 겹친다고 본 것은 약하다. R1의 조율 자료는 정서와 무관한 NSD이므로 겹침은 'Horikawa 정서 기하의 기원' 질문(구 EmoViS 범위)뿐이다.

### 1.7 정서와 뇌에 대해 새로 말해 주는 것

* **말해 주는 것:**
  * 1주차 실측 S1′은 그 자체로 정서와 뇌에 대한 결과다. Horikawa 2020의 'transmodal 정서 위치'가 비정서 추상 속성의 위계를 넘는지를 처음 묻는다. 비정서 통제를 고치면(1.1절 3번) 이 판정은 견고해진다.
  * 모델 팔 결과는 "어떤 장치가 있으면 사람 뇌와 같은 정서 초과 위계가 생긴다"는 충분성 증거다.
* **수렴 위험:**
  * 1.1절 1번을 고치지 않으면 팔 간 차이가 encoding 적합도 차이로 설명된다. 그러면 결론이 모델에 대한 것으로 수렴한다.
  * 고치면, 남는 결론(예: "정서 라벨 학습 없이도 위계가 생긴다", "되먹임이 필요하다")은 정서 이론의 쟁점(내재 대 재진입, 개념 학습)에 닿는다.

### 1.8 재채점

| 기준 | 점수 | 근거 |
|---|---|---|
| Novelty | 3 | 구성 요소(Soderberg 2026, Gao 2025, ReAlnet, Chen 2025)와 서명 기반 평가(Höfling 2026)가 각각 있다. 정서 초과 위계 서명과 분포를 분리한 brain-tuning의 결합만 새롭다 |
| Neuroscientific Importance | 4 | 1주차 S1′ 관문만으로도 'transmodal 정서 위치가 일반 추상화를 넘는가'에 답한다 |
| AI / Modeling Contribution | 4 | 매개변수를 맞춘 되먹임 대조와 신뢰도 맞춘 무작위 조율 대조가 있는 통제 학습자 계열이다 |
| Dataset Feasibility | 3 | NSD transmodal 신뢰도와 재인 과제 혼입, MC 형식, EmoSet 이용 조건이 미확인이다 |
| Methodological Rigor | 2 | 주 서명이 encoding 예측 뇌에서 계산되어 사상 유연성이 돌아오고, 비정서 통제의 차원과 신뢰도가 맞지 않는다 |
| Falsifiability | 3 | 결과 지도와 동등성 한계는 있으나 '실측 구간 안이면 재현' 규칙은 판별력이 약하다 |
| Interpretability | 2 | 9팔의 연속적 차이를 결과 지도의 깨끗한 패턴으로 읽기 어렵고 결론이 충분성 수준이다 |
| Generalizability | 3 | 두 코호트 재현은 있으나 같은 C&K 자극, 같은 규범 라벨이다 |
| Feasibility | 3 | GPU는 충분하나 9팔 구현, 서명 계산, 관문을 한 사람이 하기에 무겁다 |
| AI-enabled Affective Neuroscience Contribution | 4 | 관찰로 만들 수 없는 장치 조작이 정서 위치의 기원 쟁점에 닿는다(1.1절 1번을 고치는 조건) |
| 1-month Feasibility | 3 | 학습 27회는 2주 안에 가능하지만 MC 형식과 NSD 관문, 구현량 때문에 4주가 빠듯하다 |
| **합계** | **34** | |

---

## 2. R2. 떠올린 장면은 본 장면보다 감정 쪽으로 기울까, 흐려질까

### 2.1 반드시 고칠 것 (우선순위순)

1. **연속 시계열 확보를 관문이 아니라 핵심 판의 작업으로 넣는다(조건부 치명).**
   * 회상 창에는 두 혼입이 있다. 앞에는 단서 읽기(정서 배제 캡션, 중앙값 6 s, sub-05와 sub-06은 30% 안팎이 3 s 이하) 반응이, 끝에는 재시청 시작 반응이 걸친다.
   * 블록 평균만으로는 두 혼입의 크기를 잴 수 없다. 카드는 G4에서 "0~30%" 사전 범위를 심어 판정 불가 구역을 정한다. 이 범위는 근거가 없고, 주 결과의 판정 여부가 이 임의 범위에 달린다.
   * 단서 읽기 혼입은 H-(중립 쪽) 방향으로 작용한다. 그래서 이 혼입을 실측하지 못하면 H- 지지는 해석할 수 없다.
   * **고칠 방법:**
     * MC raw(ds005191, CC0)에서 **시험 지각 run과 회상 run만** 원 논문 절차로 다시 처리한다.
     * 다시 만든 지각 시험 블록과 보유본 블록의 상관(예: voxel 평균 r ≥ 0.9)을 확인해 학습 자료(보유본)와 호환성을 검증한다.
     * 그다음 LS-S로 준비, 회상, 재시청을 따로 추정한다.
     * 학습 2,108샘플은 보유본을 그대로 쓰면 되므로 재처리 범위가 작아진다.
2. **이전 시행의 재시청과 평정 반응이 다음 회상 창 앞부분에 남는 혼입을 추가한다(카드에 없음).**
   * 시행 순서는 재시청(10 s 이상) → 평정 → 다음 단서 읽기(중앙값 6 s) → 회상이다. 4 s 이동 블록 평균에서는 이전 클립 재시청의 HRF 꼬리가 다음 회상 창 초반에 남는다.
   * 이것은 다른 클립의 지각 신호다. 클립 순서가 의사 무작위면 편향보다 잡음이지만, 확인하지 않으면 모른다.
   * 블록 평균만 있어도 할 수 있는 대응이 있다. 클립별 Δ_emo 회귀에 '이전 시행 클립의 해독 벡터를 현재 클립 정서 방향에 사영한 값'을 nuisance로 넣는다.
3. **voxel 선택과 측정에 같은 지각 시험 자료를 쓰지 않는다.**
   * 7절은 voxel을 "지각 시험 반복 신뢰도"로 고르고, 같은 지각 시험 패턴으로 E(지각)와 합성 null을 만든다.
   * 그러면 지각 쪽 해독 충실도가 회상 쪽보다 체계적으로 유리해진다(선택 편향). 이 편향은 정서와 비정서 방향에 같게 작용한다는 보장이 없다.
   * 고칠 방법(둘 중 하나):
     * 지각 시험 5회 중 2회로 voxel을 고르고 나머지 3회로 측정한다.
     * 학습 run 자료만으로 정한 기준(예: 학습 클립 encoding 성능)으로 고른다.
4. **합성 회상 null의 사양을 구체화한다.**
   * (a) voxel별 감쇠 a를 '회상 신뢰도 / 지각 신뢰도'로 추정한다. 그런데 회상 신뢰도가 0 근처나 음수인 voxel이 많을 것이라 a가 불안정하다. 0~1로 자르고 공간 평활 같은 정칙화를 사전 등록한다.
   * (b) E(회상)가 회상 5회 평균인지 단일 시행인지 정하고, null의 잡음 크기를 같은 평균 횟수로 맞춘다.
   * (c) 회상이 '약한 지각'이 아니라 체계적으로 다른 공간이라는 증거가 있다.
     * Spera 2026(arXiv:2604.15374): 심상 반응을 지각 decoder의 조건 공간으로 옮기는 정렬 모듈이 심상 해독을 개선했다
     * Koide-Majima 2023(doi:10.1016/j.neunet.2023.11.024): 심상 재구성은 의미 정보에 더 기댄다
   * 이것은 9절의 대안 5, 6과 같다. Δ_non을 고르는 기준에 '표상 수준'(저수준 대 의미)을 지각 해독도, κ와 함께 명시적으로 맞추는 항목으로 넣는다.
5. **제목을 고친다.** "감정이 흐려질까"는 참가자의 감정이 흐려진다는 뜻으로 읽힐 수 있다. 예: "떠올린 장면은 본 장면보다 그 장면이 주는 정서적 의미 쪽으로 더 기울까, 덜 기울까?" 본문의 주장 범위 절과 맞춘다.
6. **인용 서술을 고친다.**
   * Spera 2026은 "심상 decoding의 피험자 간 정렬"이 아니다. [arXiv] 초록에 따르면 심상 반응을 지각 decoder(DynaDiff)의 조건 공간에 맞추는 잠재 기능 정렬(LFA)이다. 이 차이는 위 4번의 근거가 되므로 중요하다.
   * Cocquyt et al.은 Crossref 발행일이 2025-11-19다. 연도를 2025로 고친다(doi:10.1523/JNEUROSCI.0718-25.2025).

### 2.2 고치면 좋은 것

* **G2 통과 기준을 숫자로 적는다.** 지금은 "원 논문이 보고한 피험자별 경향과 어긋나지 않음"이다. 예를 들어 '72개 중 회상 식별 정확도가 피험자 안 순열 null의 95백분위 초과'처럼 고친다.
* **선행 표에 Cheng et al. 2023을 넣는다**(Sci Adv, doi:10.1126/sciadv.adj3906, [PubMed] PMID 37967184).
  * 자연 이미지로 학습한 decoder가 착시 자극에서 물리 자극에 없는 선과 색(주관적 내용)을 복원했다.
  * 'decoder를 자극과 다른 내부 내용의 계측기로 쓴다'는 R2의 측정 논리에 가장 가까운 선행이다. 정서는 아니다.
* **Koide-Majima 2023을 대안 5의 근거로 넣는다.** 심상이 의미 정보를 더 쓴다는 주장의 근거다.
* **A3 vividness 해석을 묶는다.** vividness는 재시청 뒤 비교 평정이고 3~4점에 몰린다(카드에 있음). 그러므로 A3 결과는 주 결론에 넣지 않는다고 명시한다.
* **단서 캡션 번호 문의를 1주차 첫날에 보낸다.** 번호를 얻으면 8.2절 3(c)의 범위 분석이 필요 없어진다.

### 2.3 그대로 둬도 되는 것

* 지각 대 회상이라는 자극 고정 대조. C-01의 치명 결함(자극 모델 불완전)을 정확히 피한다.
* 정서 특이 초과 이동(Δ_emo - Δ_non)과 κ, 지각 해독도를 맞춘 비정서 방향
* 양방향 사전 등록(H+, H-, H0)과 동등성 한계, 판정 불가 구역을 결과 범주로 둔 것
* 주장 범위 절. design_brief 3절 5번과 feedback_round2 3.6절을 가장 정확히 따른다
* RQ-44 흡수표. 흡수할 것과 남길 것의 구분이 명확하다
* decoder 정확도를 관문으로만 쓰는 원칙
* overlap 판단. TRIBE 작업과 겹치지 않는다는 것이 맞다

### 2.4 선행 판정 점검

| 카드 판정 | 점검 결과 |
|---|---|
| 핵심 가설(회상 표상의 정서 방향 이동) not found | 내 WebSearch 1건(2025~2026 회상, 심상 정서 decoding 비교)과 이전 감사 10건에서도 미발견. **판정 유지** |
| Park & Kim 2025 bioRxiv(doi:10.1101/2025.11.22.689961): 시청과 회상의 valence, arousal 공유 차원과 단계 고유 차원 | [Crossref] 초록 일치(fNIRS, 전전두, 4개 정서 상태) |
| Kim & Kim 2025(doi:10.1016/j.bandc.2025.106296) | [Crossref] 일치(부호화와 회상의 일관된 valence 표상) |
| Bradley 2022: 반복 억제가 정서가와 무관 | [PubMed] 일치("pleasant and unpleasant ... did not differ as a function of repetition") |
| Curko 2026: 정서가는 배내측, 지각 세부는 내측두 하위망 | [PubMed] 일치. "정서 정보가 추상 표상과 묶인다"는 카드의 해석은 초록의 "dorsomedial subnetwork provides an affective frame"에 가깝다. 과장 없음 |
| SNR 맞춘 합성 null은 미발견, 합성 반응 null 논리는 Chen, Keil, Ding 2025 | 맞음. Spera 2026의 서술만 고친다(2.1절 6번) |
| 놓친 선행 | Cheng 2023(decoder로 주관 내용 복원), Koide-Majima 2023(심상의 의미 의존). 둘 다 방법과 대안 설명 쪽이며 핵심 판정을 바꾸지 않는다 |

### 2.5 인용 표본 검증 (10개)

| ID | 카드 서술 | 결과 |
|---|---|---|
| doi:10.1101/2025.11.22.689961 | Park & Kim 2025 fNIRS | [Crossref] 일치 |
| doi:10.1016/j.bandc.2025.106296 | Kim & Kim 2025 | [Crossref] 일치 |
| doi:10.1523/JNEUROSCI.0718-25.2025 | "Cocquyt 2026" | [Crossref] 존재 일치, **발행 2025-11-19**(연도 불일치) |
| doi:10.1523/ENEURO.0146-26.2026 | Curko 2026 | [PubMed] 일치 |
| doi:10.1016/j.neuropsychologia.2022.108203 | Bradley 2022 | [PubMed] 일치 |
| arXiv:2604.15374 | "Spera 2026, 심상 decoding의 피험자 간 정렬" | [arXiv] 존재 일치, **서술 불일치**(심상-지각 잠재 정렬) |
| arXiv:2506.06898 | NSD-Imagery, 심상 SNR 낮음 | [arXiv] 일치 |
| arXiv:2605.17198 | MIRAGE | [arXiv] 일치 |
| doi:10.1038/s41467-022-34075-1 | Bainbridge & Baker 2022, 정서 아님 | [Crossref] 일치. 초록에 정서(emotions)가 기억 특징 중 하나로 나온다. 카드의 '정서 아님'은 '정서 방향 이동은 아님'으로 고치는 것이 정확하다 |
| doi:10.7554/eLife.62461 | 유병률 추론 | [Crossref] 일치(Ince 2021) |

### 2.6 겹침

* 연구실 팀원 TRIBE 작업: 겹침 없음. 맞다.
* existing_projects:
  * 'EmoBrain: 부분', 'EmoViS: 없음'으로 적었다. 표기를 "EmoBrain(구 EmoViS 범위 포함): 부분(뇌에서 정서 정보를 읽는 도구)"로 통일한다.
  * Emo-FilM 연구와는 겹침이 없다. 맞다.

### 2.7 정서와 뇌에 대해 새로 말해 주는 것

* NEVER, affective realism(과장)과 기억 흐려짐(Cooper 2019) 사이의 방향 논쟁을 '장면의 정서적 의미'의 신경 표상 수준에서 하나의 수치로 판정한다. 이것은 기억과 정서에 대한 결론이고 decoder에 대한 결론이 아니다.
* 위험은 결론보다 판정 가능성에 있다. 1번과 2번 혼입을 실측하지 못하면 '판정 불가'로 끝날 가능성이 크다. 그 경우에도 최소 판정 효과 크기가 다음 실험의 근거로 남는다(카드 12절). 이 설계는 정직하다.

### 2.8 재채점

| 기준 | 점수 | 근거 |
|---|---|---|
| Novelty | 4 | 회상 표상의 정서 방향 이동을 신호 감소를 뺀 뒤 잰 연구는 없다. 측정 논리는 Cheng 2023, null 논리는 Chen 2025에 있다 |
| Neuroscientific Importance | 4 | 과장 대 흐려짐이라는 기억, 정서 이론의 방향 논쟁에 수치를 준다. 결론은 익힌 클립의 즉시 회상과 규범 수준이다 |
| AI / Modeling Contribution | 3 | ridge decoder와 고정 head는 측정 장치로 적절하다. 모델 자체의 새로움은 작다 |
| Dataset Feasibility | 3 | MC 6명뿐이고 연속 시계열, 단서 번호, 보유본 형식이 미확인이다 |
| Methodological Rigor | 3 | 비정서 대조, κ 맞춤, 회복 시뮬레이션은 좋다. 혼입 크기가 임의 사전 범위이고 voxel 선택에 측정 자료를 쓴다 |
| Falsifiability | 4 | H+, H-, H0의 양방향 예측과 동등성 한계, 판정 불가 구역이 사전에 고정되어 있다 |
| Interpretability | 3 | H-는 단서 당김과 null 오사양과 겹친다. 시계열 없이는 판정 불가 가능성이 크다 |
| Generalizability | 2 | 단일 자료, 6명, 최대 11회 노출과 연습을 거친 클립의 즉시 회상이다 |
| Feasibility | 4 | CPU 위주이고 GPU 1장이면 된다 |
| AI-enabled Affective Neuroscience Contribution | 4 | 관찰로 정의할 수 없던 '회상 표상의 정서 방향' 변수(b)와 합성 회상 반사실(a)을 만든다 |
| 1-month Feasibility | 3 | raw 재처리를 시험, 회상 run으로 좁혀도 1~2주가 들어 4주가 빠듯하다 |
| **합계** | **37** | |

---

## 3. R3. 뇌가 스스로 나눈 축은 정서를 따를까, 장면 내용을 따를까

### 3.1 반드시 고칠 것 (우선순위순)

1. **판정 단위를 부분공간으로 바꾼다(치명, 고칠 수 있음).**
   * 1단계의 CCA는 두 코호트 사이 상관이 가장 큰 방향을 순서대로 고른다. 자극 구동 신뢰도가 가장 높은 성분은 시각, 의미 내용(얼굴, 사람, 동물, 장면 유형)일 가능성이 크다.
   * 그래서 상위 정준변량은 내용 쪽으로 쏠린다. "내용 축만 나옴"이라는 결과가 '정서 공유 축이 없다'가 아니라 '재현성 순서로 고른 결과'일 수 있다.
   * 또 d ≥ 2인 부분공간 안의 개별 축은 회전에 따라 달라진다. 카드는 '부분공간 단위로 먼저 판단'한다고 적었지만 2~5단계의 라벨은 축 단위다.
   * **고칠 방법:**
     * 2단계 몫 분할을 재현 부분공간 전체에 대한 다변량 R²(차원 합 또는 reduced-rank 회귀)로 먼저 한다.
     * '정서 예측 방향(집합 A에서 E ridge가 예측하는 성분)이 재현 부분공간 안에 얼마나 들어오는가'(B에서의 사영 비율)를 표적 검정으로 더한다.
     * 축 단위 라벨은 탐색으로 내린다.
2. **내용 통제 부족으로 U_E가 부풀려지는 경로를 막는다.**
   * 세 묶음을 각각 주성분 20개로 줄이면 캡션 embedding(수백 차원)과 DINOv2 feature(1,024차원)의 내용 정보가 많이 버려진다.
   * 내용 통제가 부족하면 그만큼 U_E가 커진다. 정서 축 판정이 쉬워지는 방향의 편향이다.
   * 고칠 방법:
     * 주 분석은 원래 차원의 banded ridge(himalaya가 묶음별 정칙화를 지원한다)로 한다.
     * 차원 맞춤 판은 민감도로 내린다.
     * 캡션 수 외삽은 외삽 모형(예: 1/n 선형)을 사전 등록하고 보정값이 아니라 민감도로 보고한다. 점이 4개(5, 10, 15, 20개)라 외삽이 불안정하다.
3. **라벨이 판정 가능한지를 미리 시뮬레이션한다.**
   * 재현 기준의 하한 r = 0.2에서 축 신뢰도 ρ(Spearman-Brown)는 약 0.33이다. 이때 "U_E ≥ 천장의 0.10"은 원래 R² 약 0.03이다.
   * 집합 B 약 430클립의 bootstrap에서 P(U_E > U_C) ≥ 0.95를 얻기 어렵다. 그러면 대부분의 축이 '혼합', '가를 수 없음', '설명 안 됨'으로 갈 수 있다.
   * R2의 G4처럼, 알려진 U_E와 U_C를 심은 합성 축으로 ρ 수준별 판정 가능 최소 효과를 결과 전에 계산해 라벨 기준과 함께 등록한다.
4. **VLM 가설의 '새 변수' 판정에 같은 평정자 기준선을 넣는다.**
   * V2는 가설 점수가 E∪S∪V를 넘어 축을 예측하는지 본다. 그런데 S(캡션)는 지시상 정서가 거의 없고, E는 9~17명 집계 비율이라 잡음이 크다.
   * 그러면 VLM이 매긴 "누군가 다치고 있는가" 같은 점수는 새 변수가 아니라 규범 정서를 더 깨끗이 다시 적은 값이어도 V2를 통과한다.
   * 고칠 방법:
     * 같은 VLM이 같은 입력으로 C&K 34범주와 14차원을 평정한 값(VLM-E)과 일반 내용 묘사 점수를 기준선에 넣는다.
     * 가설이 이것까지 넘을 때만 '기존 주석에 없는 새 변수'라고 부른다.
5. **오염 점검 방식을 바꾼다.**
   * "VLM 34범주 평정과 규범 평정의 클립별 평균 상관 > 0.8이면 기억"이라는 기준은 시각 정서 이해 능력과 기억을 섞는다.
   * Asanuma 2025는 범주 수준 일치는 높고 개별 비디오 수준 일치는 제한적이었다. 0.8 기준은 실제 오염을 거의 잡지 못하거나, 능력이 좋은 모델을 오염으로 잘못 몰 수 있다.
   * 대안(둘 중 하나):
     * 같은 클립의 변형 프레임(좌우 반전, 잘라내기, 다시 인코딩)과 원 프레임 사이의 평정 차이를 본다.
     * C&K 밖의 비슷한 정서 영상에서의 일치도와 비교한다.
6. **집합 B의 클립 소속을 두 코호트에서 맞춘다.**
   * B는 'Horikawa 마지막 10 run의 클립 + MC 시험 72개'다. 클립 하나는 두 코호트 모두에서 B여야 한다.
     * MC 72개에 대한 Horikawa 반응이 A 쪽 run에 있으면 그 블록을 Horikawa A에서 빼야 한다.
     * Horikawa 마지막 10 run 클립에 대한 MC 학습 run 반응은 MC의 SRM, CCA 학습에서 빼야 한다.
   * 카드에는 앞부분만 적혀 있다. 이 규칙을 명시한다.

### 3.2 고치면 좋은 것

* **선행 표에 넣을 것(모두 [arXiv] 또는 [PubMed]로 확인):**
  * **Benara et al. 2024, QA-Emb(arXiv:2405.16714).** LLM에 yes/no 질문을 해 얻은 답을 해석 가능한 특징으로 써서 언어 fMRI voxel을 예측했다. R3의 3~4단계("가설을 평정 질문 형태로 받아 점수화")와 같은 기제다. 그래서 5절의 "AI의 역할이 다르다"는 언어 영역에서는 이미 된 것이다. 차이는 정서 비디오의 transmodal 공유 축이 대상이라는 점이다.
  * **Hari et al. 2026(arXiv:2604.24942).** 한 부분집합에서 성분을 먼저 분해하고 독립 자료에서 LLM 특징으로 성분을 예측해 해석한다. '성분 먼저, 해석 나중'의 언어판 선행이다.
  * **Chang et al. 2021(Sci Adv, doi:10.1126/sciadv.abf7129, PMID 33893106).** 드라마 시청 중 vmPFC의 자료 기반 상태 전이가 정서 경험에 대응했다. 사람마다 다른 시점에 전이하다가 정서가 강한 사건에서 정렬이 늘었다. 'transmodal 정서 관련 공유 성분'의 가장 가까운 정서 쪽 선행이다. 공유 축이 정서가 큰 순간에만 나타날 수 있다는 예측도 준다.
  * Nakamura 2026(arXiv:2605.20127, 재현 가능한 응답 차원), Kolling & Toneva 2026(arXiv:2610.21508, 해석 가능 특징과의 분산 분할에서 공유 몫이 지배적).
* **Westlin 대비 문장을 다듬는다.**
  * 1단계가 거의 확실히 d > 0을 낼 것이라는 점을 예상 결과로 적는다. 초기 시각과 고위 시각 내용 성분은 코호트 사이에 강하게 재현된다.
  * 닫힘 규칙(d = 0)이 실제로 걸릴 가능성은 transmodal 묶음에서도 낮다. "Westlin과 맞는 정보"로 끝날 가능성을 과대평가하지 않는다.
* **두 사람 표시를 구체화한다.** 3단계의 '연구자와 동료 1명'이 필요하므로 1인 4주 자원 가정에 맞지 않는다. 동료가 없으면 사전 등록한 어휘 규칙(정서, 평가 단어 목록)으로 자동 표시하고 연구자 1명이 점검하는 판을 대안으로 적는다.

### 3.3 그대로 둬도 되는 것

* 라벨을 축을 정한 뒤에만 쓰는 원칙, 집합 A/B 분리, 가설은 A만 보고 생성하는 규칙
* 비재현 방향 가설을 null로 두어 '일반 문장' 위험을 숫자로 잡는 설계
* "가를 수 없음"을 T1~T3로 결과 전에 정의한 것. feedback_round2 3.7절 5단계의 요구를 정확히 구현했다
* 전역 신호 처리 multiverse를 재현 기준에 넣은 것(Bolt 2025 대응)
* COCO 축 그리기와 편집 시험을 확장으로 뺀 판단
* R1 전달 형식(축 정의, 클립 점수, 신뢰도, 사용 규칙)
* 5절의 'Horikawa 2020과 Westlin 2025를 다시 하지 않는다' 표. 사용자 비판을 피하는 구분이 명확하다

### 3.4 선행 판정 점검

| 카드 판정 | 점검 결과 |
|---|---|
| LLM 설명 생성과 보류 검증의 조합: 정서 영역 대상 없음 | 맞음. 다만 **QA-Emb(LLM 질문 답을 특징으로 fMRI 예측)를 놓쳤다.** 3~4단계 기제의 직접 선행이다 |
| 정서 fMRI의 데이터 기반 분해: 2024~2025 해석 가능한 라벨 없는 분해 없음 | 부분 수정. Chang 2021(vmPFC 상태, 2021)을 놓쳤다. 2024~2026 범위에서는 내 arXiv 검색(25건)에서도 정서 대상은 없었다 |
| 코호트 간 공유 성분 + 정서, 의미, 시각 분할: 없음 | 맞음. 인접은 Nakamura 2026(재현 차원), Hari 2026(성분 먼저) |
| 종합 판정 | **partially**(카드의 Novelty 3.5 서술과 같은 방향). 기제(QA-Emb, GCT, LaVCa, SASC)와 정서 쪽 자료 기반 성분(Chang 2021)이 각각 있다. 두 코호트 재현 축의 정서 대 내용 판정만 새롭다 |

### 3.5 인용 표본 검증 (8개)

| ID | 카드 서술 | 결과 |
|---|---|---|
| arXiv:2502.13606 | LaVCa, 시각피질 voxel 캡션 | [arXiv] 일치 |
| arXiv:2305.09863 | SASC, 블랙박스 모듈의 자연어 설명, fMRI에도 적용 | [arXiv] 일치(초록이 "fitted model of a brain region"을 명시) |
| arXiv:2505.12653 | Han & Bonner 2025 | [arXiv] 존재 일치. 영화 시청 중 개인 특이 패턴이 고차원에 걸쳐 남는다는 연구다. 카드 검색 기록의 '인접' 표기는 맞다 |
| doi:10.1038/s41593-025-01945-y | Bolt 2025, 전역 신호와 자율신경 | [Crossref] 일치 |
| doi:10.1371/journal.pcbi.1013714 | Gauthaman 2025, 사람 간 공유 성분 | [Crossref] 존재 일치. 초록은 시각피질의 scale-free 공유 스펙트럼이다. 카드의 "cross-decomposition과 hyperalignment로 추정"은 본문 수준 서술로 보이며 초록에서는 확인 불가 |
| doi:10.1016/j.neuron.2012.10.014 | Huth 2012 | [Crossref] 일치 |
| doi:10.1038/s41598-025-14961-6 | Asanuma 2025, MLLM과 사람 정서 구조 | [Crossref] 존재 일치(제목: 영상 정서 고차원 구조의 사람-MLLM 대응) |
| arXiv:2410.00812 | GCT | [arXiv] 일치(이전 라운드 확인) |

### 3.6 겹침

* 연구실 팀원 TRIBE 작업: 겹침 없음. 맞다.
* existing_projects: "EmoBrain(구 EmoViS 범위 포함)" 표기와 그 근거가 맞다. Emo-FilM 연구는 확장에서만 자료가 겹친다. 맞다.

### 3.7 정서와 뇌에 대해 새로 말해 주는 것

* **말해 주는 것:** 두 독립 코호트가 공유하는 transmodal 자극 고정 성분이 장면의 정서적 의미를 따르는지 내용을 따르는지, 이 자료로 가를 수 없는지. 정서 신경표상 연구에서 '집단 공통 정서 축'이라는 전제의 범위를 정해 주는 결과다.
* **수렴 위험:**
  * 3.1절 1~3번을 고치지 않으면 "내용 축 우세"나 "가를 수 없음"이 방법의 성질(재현성 순 선택, 내용 통제 부족, 낮은 ρ)에서 나온다. 그러면 결론이 분해 방법에 대한 것이 된다.
  * 4번을 고치지 않으면 "새 변수" 결론이 VLM의 평정 품질에 대한 것이 된다.

### 3.8 재채점

| 기준 | 점수 | 근거 |
|---|---|---|
| Novelty | 3 | QA-Emb, GCT, LaVCa, SASC, Hari 2026과 Chang 2021이 각 구성 요소를 했다. 두 코호트 재현 축의 정서 대 내용 판정만 새롭다 |
| Neuroscientific Importance | 3 | '공통 정서 축' 전제의 범위를 정하지만 결과가 '가를 수 없음'으로 갈 가능성이 크고 Horikawa + MC 재분석이다 |
| AI / Modeling Contribution | 3 | VLM 가설 생성과 평정은 기제상 QA-Emb의 정서판이다. 검증은 회귀다 |
| Dataset Feasibility | 4 | Horikawa 공개 전처리본, 캡션, 원본 영상이 있고 연속 시계열이 필요 없다(MC 형식만 미확인) |
| Methodological Rigor | 3 | 숫자 기준, null 방향, T1~T3는 좋다. 재현성 순 선택, 주성분 20개 내용 통제, 오염 점검 기준이 약하다 |
| Falsifiability | 4 | 각 단계 판정이 결과 전에 숫자로 고정되어 있다 |
| Interpretability | 3 | 축 단위 라벨이 회전에 의존하고 낮은 ρ에서 라벨 판정력이 미지수다 |
| Generalizability | 3 | 두 코호트 재현만 인정하지만 C&K 안의 결과다 |
| Feasibility | 3 | 단계가 많고 VLM 약 13만 회 호출, 두 사람 표시가 필요하다 |
| AI-enabled Affective Neuroscience Contribution | 3 | 가설 생성(c)과 새 변수 계산(b)이지만 VLM-E 기준선 없이는 새 변수 주장이 부풀려진다 |
| 1-month Feasibility | 3 | 재현 축이 없으면 2주에 닫히지만 있으면 4주가 빠듯하다 |
| **합계** | **35** | |

---

## 4. 세 카드 비교와 권고

| | R1 | R2 | R3 |
|---|---|---|---|
| 재채점 합계 | 34 | 37 | 35 |
| AI-enabled + 1-month | 7 | 7 | 6 |
| 가장 큰 수정 | 서명 계산을 모델 내부 위계와 고정 사상으로 옮긴다 | 시험, 회상 run raw 재처리와 LS-S | 부분공간 단위 판정, 원래 차원의 내용 통제, VLM-E 기준선 |
| 수정 뒤 기대 | 1주차 S1′만으로도 사용자 질문에 답한다 | 기억, 정서 방향 논쟁에 수치 | R1에 줄 정서 라벨 없는 표적 |

* **실행 순서 의견:**
  * R2를 먼저 권한다. 자극 고정 대조라 결함이 가장 적고, 남은 결함이 자료 처리 문제다.
  * R1은 1주차 S1′ 관문(실측만, GPU 불필요)을 R3의 1단계와 같은 주에 하면 Horikawa 전처리, 캡션 속성, HCP360 묶음을 공유한다.
  * R1의 모델 팔은 1.1절 1번 수정이 끝난 뒤 시작한다.
* emotion-theory의 이론 검토와 내 결론이 다르면 조정하지 않고 두 기록을 함께 보고하기를 권한다.

## 5. 새로 찾은 선행 (이번 검토, 식별자 확인)

| 선행 | 식별자 | 확인 | 관련 카드 |
|---|---|---|---|
| Höfling et al. 2026, Only Brains Align with Brains: Cross-Region Alignment Patterns Expose Limits of Normative Models | arXiv:2604.21780 | [arXiv] 초록 | R1(서명 기반 평가의 방법론 선행) |
| Nakamura et al. 2026, Beyond Prediction Accuracy: Target-Space Recovery Profiles for Evaluating Model-Brain Alignment | arXiv:2605.20127 | [arXiv] 초록 | R1, R3 |
| Leutenegger 2026, Supervised Training Rapidly Degrades Early Visual Cortex Alignment(정정본 있음) | arXiv:2605.30556 | [arXiv] 초록(정정 주석 포함) | R1(학습이 V1 정렬을 낮춤, 정정 뒤에도 유지되는 부분만) |
| Cheng et al. 2023, Reconstructing visual illusory experiences from human brain activity, Sci Adv | doi:10.1126/sciadv.adj3906, PMID 37967184 | [PubMed] | R2(decoder로 주관 내용 측정) |
| Koide-Majima, Nishimoto, Majima 2023, Mental image reconstruction from human brain activity, Neural Netw | doi:10.1016/j.neunet.2023.11.024, PMID 38016230 | [PubMed] | R2(심상은 의미 정보에 더 기댐, 대안 5) |
| Spera et al. 2026, Seeing the imagined: latent functional alignment in visual imagery decoding | arXiv:2604.15374 | [arXiv] 초록 | R2(서술 정정, 심상-지각 체계적 이동) |
| Benara et al. 2024, Crafting Interpretable Embeddings by Asking LLMs Questions(QA-Emb) | arXiv:2405.16714 | [arXiv] 초록 | R3(가설 질문 점수화의 직접 선행) |
| Hari et al. 2026, Independent-Component-Based Encoding Models of Brain Activity During Story Comprehension | arXiv:2604.24942 | [arXiv] 초록 | R3 |
| Kolling & Toneva 2026, Decomposing Brain-LLM Alignment with Interpretable Semantic Representations | arXiv:2610.21508 | [arXiv] 초록 | R3(분산 분할에서 공유 몫 지배) |
| Chang et al. 2021, Endogenous variation in vmPFC state dynamics during naturalistic viewing reflects affective experience, Sci Adv | doi:10.1126/sciadv.abf7129, PMID 33893106 | [PubMed] | R3(자료 기반 정서 관련 상태와 사건 시 정렬) |

## 6. 검색 기록 (모두 2026-11-12)

| 카드 | # | 경로 | 질의 | 결과 |
|---|---|---|---|---|
| R1 | 1 | arXiv API | ("brain-tuned" OR "brain-tuning" OR "brain-aligned" OR "fMRI-guided") AND (vision OR visual OR image) | 20건. 정서 서명 평가 없음. Höfling 2026, Nakamura 2026, Leutenegger 2026 발견 |
| R1 | 2 | arXiv API | ("principal gradient" OR "cortical hierarchy" OR "sensory-to-transmodal" OR "unimodal to transmodal") AND ("neural network" OR layers OR model) AND fMRI | 4건, 정서 없음 |
| R1 | 3 | WebSearch | deep neural network top-down feedback gain modulation emotional salience model compared with human visual cortex fMRI emotional images 2025 2026 | 정서 되먹임 모델과 fMRI 비교 없음(Tugsbayar 2026, 사람 dlPFC-V1 되먹임 연구만) |
| R1 | 4 | arXiv API, Crossref | 인용 표본 8개 | 1.5절 |
| R2 | 1 | WebSearch | fMRI decoding recalled or imagined emotional video content valence decoded from recall compared with perception same stimuli 2025 2026 | 회상 대 지각 정서 비교 없음(EmoMind, Afrasiyabi 2024, Ma 2025 CCN만) |
| R2 | 2 | PubMed | (Cheng FL AND Kamitani Y AND illusory) OR (Koide-Majima N AND mental image reconstruction) OR (Chang LJ AND vmPFC state dynamics ...) | Cheng 2023, Koide-Majima 2023, Chang 2021 |
| R2 | 3 | PubMed | (Curko AND Kensinger) OR (Bradley MM AND repeated retrieval emotional autobiographical) | Curko 2026, Bradley 2022 초록 확인 |
| R2 | 4 | arXiv API, Crossref | 인용 표본 10개 | 2.5절 |
| R3 | 1 | arXiv API | (LLM OR "language model") AND (explain OR explanation OR hypotheses OR interpret) AND fMRI AND (components OR axes OR dimensions OR selectivity) | 25건. QA-Emb, Hari 2026, Kolling & Toneva 2026 발견. 정서 대상 없음 |
| R3 | 2 | PubMed | Chang LJ ... vmPFC state dynamics naturalistic affective experience(R2 2번과 같은 질의) | Chang 2021 |
| R3 | 3 | arXiv API, Crossref | 인용 표본 8개 | 3.5절 |

## 7. 미확인 사항

1. NSD 공개 atlas에 HCP_MMP1이 피험자 공간으로 있는지와 NSD transmodal ROI의 ncsnr(R1 1.1절 4번)
2. Leem 2026 본문의 '지름길' 결과(R1 확장 X1의 근거)
3. Horikawa figshare 73차원 의미 feature의 평정 주체와 방식(R1, R2 공통 비정서 통제)
4. MC 회상 시행의 평정 구간 길이(R2 2.1절 2번 이전 시행 혼입의 크기 추정에 필요)
5. Gauthaman 2025 본문에 cross-decomposition과 hyperalignment 절차가 있는지(R3 인용 서술)
