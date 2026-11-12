# R1. 뇌를 닮은 장치를 하나씩 넣고 뺀 AI를 키워 보면, 사람 뇌에 장면의 정서적 의미가 놓이는 방식은 어떤 장치가 있을 때 나타날까?

* 작성: brain-inspired. 기준일 2026-11-12.
* 지시: `outputs/revision/design_brief.md` 1절, 3절, 4절 R1. 양식: `reference/protocols.md` P7(14개 항목) + Safeguards 점검.
* **수정(2026-11-12):** `outputs/revision/card_revision_orders.md` 0절(공통)과 1절(R1)을 반영했다. 근거 검토는 `card_review.md` 1절([AR])과 `card_theory_review.md` 0절, 1절([ET])이다. 무엇을 어디서 고쳤는지는 카드 끝의 '검토 반영 기록'에, 반영하지 않은 지적은 '반영하지 않은 지적' 절에 있다.
* 직접 읽은 근거 파일:
  * `outputs/revision/design_brief.md` 전체
  * `outputs/revision/feedback_round2.md` 3.1~3.5절
  * `outputs/revision/reviewer_notes.md` 3절, 4절, 7절, 8절
  * `outputs/revision/prior_overlap_audit.md` 2.2, 2.3, 2.5, 3, 7절
  * `outputs/revision/plan.md`
  * `outputs/revision/card_revision_orders.md` 0절, 1절, `card_review.md` 1절, `card_theory_review.md` 0절, 1절
  * `outputs/stage1/dataset_Horikawa.md`, `outputs/stage1/dataset_NSD.md`(해당 행)
  * 내 `revision_round.md`(BI-RV-1~6)
  * `outputs/agents/frontier-ai/revision_round.md` FA-RV-1, 3, 4절과 0.4, 0.5, 9절
* 출발 재료:
  * BI-RV-1: 되먹임, C-05
  * BI-RV-2: brain-tuning, C-06
  * BI-RV-3: 피질하 지름길, C-07
  * BI-RV-4: 재귀 깊이, C-08
  * BI-RV-5: 지형, C-09
  * FA-RV-1, 3, 4: 학습 목표와 학습 자료, C-16, C-18, C-19
* 이 카드의 한 줄 요약: 같은 출발점의 시각 AI에 사용자가 정의한 brain-like 장치를 통제된 요인으로 넣고 뺀다. 장치는 (a) 구조 제약인 정서 판단의 되먹임과 (c) 사람 뇌 반응에 맞춘 학습(brain-tuning)이다. 판정은 **모델 층 내부의 정서 초과 위계**를, 정서와 무관한 기준으로 **미리 고정한 층-영역 배정**을 거쳐 사람 뇌의 위계와 맞대어 한다. encoding 예측력 경쟁이 아니다. 사람 뇌에 정서 초과 위계가 있는지(S1′)는 1주차에 먼저 검정하며, 그 답이 이 카드의 첫 결과다.

### 이 카드에서 쓰는 말

| 말 | 뜻 |
|---|---|
| 정서 고유 정보 | **규범 정서 평정(C&K 34범주, fMRI 참가자가 아닌 별도 평정자의 집계)과 공변하는 고유 정보.** 저수준 영상 통계, 비정서 의미 내용, 묘사된 정서의 RDM을 부분 통제한 뒤 남는 몫이다. 이 카드의 "정서"는 모두 장면의 정서적 의미(규범 기준)를 뜻한다. 묘사된 정서를 가르지 못한 결과에는 '묘사된 정서 지각 포함'을 붙인다 |
| 묘사된 정서 | 화면 속 인물의 표정과 몸짓이 나타내는 정서. 평정자가 보고한 유발 정서와 구분한다. 공개 표정 모델과 VLM으로 매기며 [AI-est]로 표시한다(6절) |
| 서명(signature) | 사람 뇌에서 관찰된, 모델이 맞혀야 할 특정한 정서 조직 방식. 이 카드는 S1′(주)과 S2(보조)를 쓰고, 이중 위계(S1-cat 대 S1-aff)와 appraisal 기울기(S1-app)를 덧붙인다 |
| S1 위계 | 정서 고유 정보가 감각 영역보다 transmodal 영역에 많다는 관찰(Horikawa 2020). 이 카드에서는 사실이 아니라 1주차에 다시 검정할 가설이다 |
| S1′ 정서 초과 위계 | S1의 기울기에서, 같은 방식으로 잰 비정서 의미 고유 정보의 기울기를 뺀 값. 주 비정서 통제는 Horikawa 73차원 의미 feature의 주성분 34개다(8.1절). "감각과 고차 영역의 차이 중 정서에만 있는 몫" |
| S1-cat, S1-aff, S1-app | 정서 고유 정보를 셋으로 나눈 기울기. 범주 고유(34범주에서 valence, arousal을 뺀 부분), affect 고유(valence, arousal), appraisal 고유(certainty, control, fairness, obstruction, safety) |
| S2 해리 | 정서 개념 지식이 약해지면 좋고 나쁨(valence) 구분은 남고 부정 정서 범주끼리의 구분이 무너지는 패턴. 의미 치매(Lindquist 2014)와 의미 실어증(Souter 2021) 환자의 **얼굴 표정 분류 행동**에서 보고됨. 이 카드의 표적은 해리 자체가 아니라 "개념 유무 팔 사이 R_S2 차이의 방향이 건강한 사람 뇌의 R_S2 쪽인가"다(8.2절 7번) |
| 위계 축 | 감각 영역에서 transmodal 영역까지 피질 parcel의 순서. 휴지기 기능 연결의 주 경사(principal gradient, Margulies 2016) 값을 HCP360 parcel마다 쓴다 |
| 모델 내부 위계 | 모델 블록(ResNet-50의 conv1과 bottleneck 16개, 총 17단계) RDM에서 계산한 정서 고유 정보와 비정서 고유 정보의 깊이별 프로필. **주 서명은 여기서 계산한다** |
| 층-영역 배정 | HCP360 parcel마다 모델 블록 하나를 대응시킨 표. 정서와 무관한 기준(정서, affect, 묘사된 정서 RDM을 부분 통제한 재가중 없는 RSA)으로, 평가에 쓰지 않는 배정용 클립에서 A0로 한 번 정한다. 정서 서명을 계산하기 전에 등록하고 모든 팔에 고정한다 |
| 뇌 좌표 모델 서명 | 배정표로 각 parcel에 해당 블록의 모델 값을 채운 뒤, 실측과 같은 parcel 집합과 같은 위계 축에서 계산한 S1′ |
| 모델 예측 뇌(보조) | 각 모델의 특징으로 만든 encoding 모델이 보류 클립에 대해 예측한 parcel 반응. **보조 판으로만 쓰고 영역별 encoding R²를 공변량으로 같이 보고한다** |
| brain-tuning | 시각 모델이 사람 fMRI 반응을 예측하도록 모델 자체를 미세조정하는 것. 이 카드에서는 정서와 무관한 NSD 일상 장면 반응으로만 한다 |
| 되먹임(feedback) | 정서 판단 모듈의 상태가 시각 모델의 중간층 활동을 다시 조절하는 연결. 구조 제약 (a)의 대표 |
| 끝까지 미세조정(E-ff) | 되먹임 없이 같은 정서 목표로 시각 모델 모든 층을 학습하는 대조 팔. 되먹임 효과를 "깊은 학습" 효과와 가르기 위한 필수 대조(C-05) |
| 노출 대조(E-ff-shuf) | E-ff와 같은 EmoSet 이미지, 같은 손실과 step 수로 학습하되 이미지와 라벨의 짝을 섞은 팔. "정서 이미지에 노출된 것"과 "정서 라벨을 배운 것"을 가른다 |
| 논쟁 클립(controversial) | 모델 조건끼리 예측이 가장 크게 갈리는 클립. 쌍 대비의 최종 확인을 이 클립에서 한다(Golan 2020) |

---

## 1. Core Research Question

**조건문 질문.** 정서 영상을 볼 때, 규범 정서 평정과 공변하는 고유 정보가 감각 영역보다 transmodal 영역에 많고, 그 기울기가 같은 방식으로 잰 비정서 의미 정보의 기울기보다 가파르다면(S1′ > 0), 같은 출발점의 시각 모델에 아래 중 무엇을 넣었을 때 이 정서 초과 위계가 **모델 층 내부 위계에서 나타나고, 미리 고정한 층-영역 배정을 거쳐 사람 뇌의 위계와 같은 모양이 되는가?**

1. 정서 판단 모듈의 되먹임
2. 일상 장면에 대한 사람 transmodal 영역 반응에 맞춘 학습(brain-tuning)
3. 정서 라벨 학습(정서 이미지 노출만으로 생기는 효과와 구분)

* **전제는 1주차에 먼저 검정한다.** 실측 S1′이 0보다 큰지는 Horikawa 2020의 "transmodal 정서 위치"가 비정서 의미 정보의 위계를 넘는지를 묻는 독립된 질문이다. 그 답은 모델 팔 결과와 상관없이 이 카드의 첫 결과로 보고한다(13절, 14절).
* **S1′ ≈ 0이면** 질문은 "정서 정보의 transmodal 위치는 일반 추상화 위계의 일부다"라는 보고로 끝난다. 모델 팔은 S2와 이중 위계(S1-cat 대 S1-aff)에만 쓴다(13절 규칙).
* 결론의 "정서"는 장면의 정서적 의미(규범 기준)다. 묘사된 정서를 통제로 가르지 못하면 결론에 '묘사된 정서 지각 포함'을 붙인다.

## 2. Scientific Motivation

* **알려진 것.** Horikawa 2020(doi:10.1016/j.isci.2020.101060)은 시각, 의미 공변량을 넘는 정서 정보가 unimodal-transmodal 경사의 끝(DMN 중심)에 많다고 보고했다. 그러나 관찰 데이터로는 이 위계가 정서 고유인지, 왜 생기는지를 가를 수 없다.
* **가르지 못하는 설명 넷.**
  * **일반 추상화:** 어떤 추상 속성이든 고차 영역에 많을 뿐이다. 사용자 지적("감각과 고차 영역의 차이가 전부 정서는 아닐 것")이 이것이다. 시간 통합 창의 위계(Hasson 2008, doi:10.1523/JNEUROSCI.5487-07.2008)도 같은 범주의 대안이다. 규범 정서 평정은 장면 전체를 종합한 판단이라, 비교 속성이 구체적 지각 속성이면 "정서라서"가 아니라 "종합 판단이라서" 기울기가 생길 수 있다([ET] 1.2). 그래서 비교 속성을 추상 수준, 차원, 신뢰도에서 맞춘다(8.1절).
  * **개념 학습:** 정서 개념(범주 이름)을 배워야 생긴다. 구성주의의 언어, 개념 가설이다(Lindquist 2014, doi:10.1037/a0035293; Souter, Lindquist & Jefferies 2021, doi:10.1016/j.neuropsychologia.2021.108052). Satpute & Lindquist 2019(doi:10.1016/j.tics.2019.07.003, PubMed 초록)는 affect(valence, arousal)는 피질하와 넓은 영역에, 이산 범주의 구성은 DMN의 추상화에 둔다. 이 주장은 "범주 기울기가 affect 기울기보다 가파르다"는 검정 가능한 예측을 준다.
  * **재진입:** 정서 판단이 감각 영역으로 되먹여야 생긴다. 대립 가설은 시각 학습 자체의 산물이라는 내재 가설이다(Liu et al. 2024, doi:10.1371/journal.pcbi.1011943 Discussion; Bo et al. 2021, doi:10.1093/cercor/bhaa411; Chen, Keil & Ding 2025, doi:10.1167/jov.25.9.1989).
  * **고차 영역의 반응 형식:** 일상 장면을 처리하는 사람 transmodal 영역의 표상 형식 자체가 장면의 정서적 의미를 담는다. 사물 표상이 일상 장면의 정서 schema를 이끈다는 결과(Gao, Ajith & Peelen 2025, doi:10.1101/2025.02.19.638854)와, 정서와 무관한 시각 모델이 정서 평정 분산 대부분을 설명한다는 결과(Conwell et al. 2025, doi:10.1073/pnas.2306025121)가 이 방향을 시사한다.
* **왜 AI가 필요한가.** 사람의 학습 조건이나 경로를 바꿀 수 없다. ANN으로 "왜"를 묻는 연구 프로그램(Kanwisher, Khosla & Dobs 2023, doi:10.1016/j.tins.2022.12.008; Doerig et al. 2023, doi:10.1038/s41583-023-00705-w)은 같은 출발점에서 조건 하나만 바꾼 학습자를 만들어 이 설명들을 서로 다른 예측으로 갈라 준다.
* **왜 모델 내부 위계와 고정 배정으로 판정하는가.**
  * 표준 선형 연결은 너무 유연해서 표상이 달라도 encoding 점수가 비슷하게 나온다(Conwell et al. 2024, doi:10.1038/s41467-024-53147-y). AI 특징이 뇌를 더 잘 예측한다는 결과는 이미 흔하다(Huang 2026, arXiv:2611.13637 등, design_brief 3절).
  * encoding으로 만든 "모델 예측 뇌"에서 서명을 계산하면, transmodal parcel의 encoding 적합도가 낮은 팔은 예측 분산이 작아져 기울기가 낮아진다. 팔 간 S1′ 차이가 encoding 적합도 프로필의 차이로 설명될 수 있다([AR] 1.1-1). 그래서 주 서명은 모델 자체의 층 RDM에서 계산하고, 뇌와는 정서와 무관한 기준으로 미리 고정한 층-영역 배정으로만 맞댄다.
  * 예측 정확도 대신 관계 구조나 회복 프로필로 정렬을 평가하자는 방법론 선행이 2026년에 나왔다(Höfling et al. 2026, arXiv:2604.21780; Nakamura et al. 2026, arXiv:2605.20127). 층 위계와 피질 위계의 대응 자체도 선행이 있다(Nonaka et al. 2021, doi:10.1016/j.isci.2021.103013; Pham et al. 2021, doi:10.1101/2021.03.18.435929). 이 카드는 그 판정 방식을 정서 초과 위계와 brain-like 장치 조작에 적용한다.

## 3. Origin of the Idea

* **에이전트 결과의 결합:**
  * brain-inspired: Round 1 P-6(정서 전용 구조는 필요한가), Chain 3과 6, Round 2 BI-P3, 재탐색 BI-RV-1~5
  * frontier-ai: FA-RV-1(학습 목표), FA-RV-3(사람 박탈), FA-RV-4(정서 단어 제거)
  * Coordinator: feedback_round2 3.4절(A + C + D 통합, 서명 S1~S3), card_revision_orders.md 1절
  * adversarial-reviewer: 결함 C-05~C-09, 공통 비판 8절, 카드 검토 [AR] 1절(주 서명 위치, 판정 규칙, 비정서 통제, NSD 관문)
  * emotion-theory: 카드 검토 [ET] 1절(구성개념, S2 간극, 노출 대 라벨, 이중 위계, CPM)
  * geometry-info R3(재현 뇌 축, 확장에서 서명으로 받음)
* **가져온 분야:** NeuroAI의 통제된 학습자(Axis N, I, J), brain-tuning(Axis J), 모델-뇌 정렬 평가 방법론(Axis N, K), 구성주의 정서 이론과 신경심리 해리(Axis A), 표상 기하(Axis K).
* **후보 ID:** C-05, C-06, C-07, C-08, C-09(brain-inspired), C-16, C-18, C-19, C-20(frontier-ai). matrix 조합 번호는 이번 재탐색 라운드에서 새로 매기지 않았다.

## 4. Prior Literature

### 4.1 직접 관련 선행과 기여

| 선행 | 식별자 | 확인 | 이 카드와의 관계 |
|---|---|---|---|
| Horikawa et al. 2020, iScience | doi:10.1016/j.isci.2020.101060 | Crossref, 본문 Discussion | S1의 출처. 공변량 비교로 정서 고유 정보의 transmodal 위치를 보고 |
| Kragel et al. 2019, Sci Adv (EmoNet) | doi:10.1126/sciadv.aaw4358 | Crossref, 본문 | 정서 지도 CNN과 후두엽. C&K 프레임 학습이라 이 카드에서는 쓰지 않는다(누수). BET 쪽 예측(시각 체계 안 정서 schema)의 근거로만 인용 |
| Liu et al. 2024, PLoS CB | doi:10.1371/journal.pcbi.1011943 | Crossref, 본문 | 물체 학습 망의 정서 선택 unit. 내재 대 재진입을 미해결로 남김. 뇌 비교 없음 |
| Gao, Ajith & Peelen 2025, bioRxiv | doi:10.1101/2025.02.19.638854 | Crossref | 일상 장면에서는 사물 학습 모델이, 정서 유발 자극에서는 정서 학습 모델이 정서 평정을 더 잘 예측. BOLD5000 LOC |
| Soderberg, Jang & Kragel 2026, SCAN | doi:10.1093/scan/nsag028 | Crossref | 표정 대 장면으로 정서를 학습한 ANN으로 pSTS, 편도체 fMRI 예측. 학습 과제를 바꾼 정서 ANN과 정서 영역 fMRI의 가장 가까운 선행 |
| Conwell et al. 2024, Nat Commun | doi:10.1038/s41467-024-53147-y | Crossref | 구조, 목표의 뇌 예측 차이는 작고 데이터가 주 요인. 선형 연결의 유연성 경고 |
| Conwell et al. 2025, PNAS | doi:10.1073/pnas.2306025121 | Crossref | 정서 없는 지각 모델이 정서 평정 분산 대부분을 설명(뇌 없음) |
| Mertens et al. 2025 | arXiv:2509.21384 | arXiv 초록, DB | 인기 CNN과 valence appraisal 행동, fMRI의 정렬. CNN은 단순 시각 처리를 넘지 못하고 고차 처리를 반영하지 않는다고 보고 |
| **Höfling et al. 2026** | arXiv:2604.21780 | arXiv 초록 | 기존 정렬 벤치마크는 모델을 거의 구분하지 못한다. 영역 간 정렬 관계 프로필(alignment pattern)을 재현해야 뇌 정렬로 인정하자고 제안. **판정 방식의 방법 선행** |
| **Nakamura et al. 2026** | arXiv:2605.20127 | arXiv 초록 | NSD에서 반복 측정으로 재현 가능한 응답 차원을 찾고 그 회복 프로필로 정렬을 평가. 예측 정확도가 같아도 회복 프로필이 다를 수 있음. **판정 방식의 방법 선행** |
| **Nonaka et al. 2021, iScience (BH score)** | doi:10.1016/j.isci.2021.103013 | PubMed 초록 | DNN 층 위계와 시각 영역 위계의 대응을 점수화. 인식 성능이 높은 DNN일수록 위계 대응이 낮음. 층-영역 위계 대응의 선행 |
| **Pham et al. 2021, bioRxiv** | doi:10.1101/2021.03.18.435929 | Crossref 초록 | 그림의 미적 가치를 예측하도록 최적화한 CNN에서 얕은 층은 V1, 깊은 층은 연합 피질과 닮음. 가치(정서 인접) 과제 CNN 층과 피질 위계의 대응을 본 가장 가까운 선행. 비정서 통제와 장치 조작은 없음 |
| Chen, Keil & Ding 2025, J Vis (VSS) | doi:10.1167/jov.25.9.1989 | Crossref(존재), 내용은 검색 요약 | 합성 fMRI로 재진입 가설 검정. 모델에 되먹임을 넣지는 않음 |
| Liu et al. 2025, bioRxiv (VCA) | doi:10.1101/2025.10.20.683439 | Crossref 초록 | ViT + 편도체 모사 모듈(피드포워드), 편도체 fMRI 정렬 |
| Leem, Keil, Ding, Fang 2026 | arXiv:2607.19327 | arXiv, 본문 | Visual-Valence 모델(시각 모듈, 정서 평가 모듈, 초기 시각에서 정서 모듈로 가는 지름길). **지름길 없는 모델은 연합 정서 학습에 실패했다고 본문 Discussion 2번째 단락이 적고, 근거는 Supplementary Fig. S2와 Appendix B.1이다.** 초록에는 이 주장이 없다. 뇌 비교 없음 |
| Méndez et al. 2022, Phil Trans B | doi:10.1098/rstb.2021.0512 | Crossref | 상구 모사 DNN, 표정 인식, 사람 SC 7T. 피질하 경로 모델의 선행 |
| Lu & Wang 2024 (ReAlnet-fMRI) | arXiv:2407.10414 | arXiv 초록 | CORnet을 사람 fMRI로 최적화해 뇌 유사도를 높임. 시각 영역, 정서 아님. brain-tuning의 시각판 선행 |
| Policzer, Braunstein & Toneva 2025 | arXiv:2511.07988 | DB | 사회 인지 영역(STS) brain-tuning, 사회 과제 성능 |
| Leutenegger 2026 | arXiv:2605.30556 (정정본), 후속 arXiv:2608.12408 | arXiv 초록 | 지도 학습이 초기 시각피질 정렬을 낮춘다. **저자 정정(2026-08) 뒤에는 "시험한 모든 학습 규칙에서 V1 정렬이 낮아진다"는 부분만 유지된다.** 후속 분석은 초기 시각 RSA 비교가 평가 입력 해상도에 크게 좌우된다고 보고. E 팔에서 기울기의 감각 쪽 끝이 바뀔 수 있다는 경고로만 인용 |
| Margalit et al. 2024, Neuron (TDANN) | doi:10.1016/j.neuron.2024.04.018 | Crossref, 본문 | 지형 제약 모델. checkpoint는 OSF(osf.io/64qv3), 코드는 GitHub(Data and Code Availability 원문) |
| Kar et al. 2019; Kietzmann et al. 2019 | doi:10.1038/s41593-019-0392-5; doi:10.1073/pnas.1905544116 | Crossref | 재귀의 필요성(물체 인식, 시각 동역학) |
| Spoerer et al. 2020, PLoS CB | doi:10.1371/journal.pcbi.1008215 | Crossref | 시간 단계가 많은 재귀 망(BLT). C-08 대안 |
| Tugsbayar et al. 2026, eLife | doi:10.7554/eLife.105953 | Crossref | top-down 되먹임 구성이 같은 연결의 모델에서 **시청각 통합**의 기능 차이를 만든다(정서 아님) |
| Lindquist et al. 2014; Souter et al. 2021 | doi:10.1037/a0035293; doi:10.1016/j.neuropsychologia.2021.108052 | DB; Crossref | S2 해리의 출처(환자의 얼굴 표정 분류 행동). Lindquist 2014의 부정 범주는 anger, disgust, fear, sadness([ET] 1.2, 초록) |
| Satpute & Lindquist 2019, TiCS | doi:10.1016/j.tics.2019.07.003 | Crossref, PubMed 초록 | affect는 피질하와 넓은 영역, 이산 범주 구성은 DMN 추상화. 이중 위계(S1-cat 대 S1-aff) 예측의 출처 |
| Barrett 2017, SCAN | doi:10.1093/scan/nsw154 | DB | 구성주의의 예측 처리(개념이 위에서 아래로 지각을 형성). 되먹임 결과가 구성주의와도 양립하는 근거 |
| Scherer 2009, Cogn Emot (CPM) | doi:10.1080/02699930902928969 | DB(제목 수준) | 다수준 appraisal. S1-app 예측의 출처 |
| Westfall & Yarkoni 2016, PLoS ONE | doi:10.1371/journal.pone.0152719 | Crossref, DB(본문) | 공변량 신뢰도가 불완전하면 증분 효과 주장의 위양성률이 크게 오르고, 표본이 클수록 더 오른다. 측정 오차를 명시하는 접근이 필요. 비정서 통제의 신뢰도 보정과 민감도 분석의 근거 |
| Kiyokawa & Hayashi 2024, Sci Rep | doi:10.1038/s41598-024-71690-y | DB(Crossref, PubMed) | Horikawa 자료에서 얼굴 포함 여부로 나눈 분석(Stage 1 보고서 [2차 본문]). 묘사된 정서 통제의 인접 선행 |
| Cheong et al. 2023, Affect Sci (Py-Feat) | doi:10.1007/s42761-023-00191-4 | Crossref 초록 | 공개 얼굴 표정 분석 도구. 묘사된 정서 묶음의 표정 특징 추출 후보 |
| Allen et al. 2022, Nat Neurosci (NSD) | doi:10.1038/s41593-021-00962-x | Crossref, DB(초록) | NSD 원 논문. 3회 반복과 연속 재인 과제 설계는 Stage 1 보고서(dataset_NSD.md) 기준. B 팔 관문의 근거 |
| Zhang et al. 2017 | arXiv:1611.03530 | arXiv 초록 | 큰 망은 섞은 라벨도 외운다. E-ff-shuf가 표상을 손상시킬 수 있다는 위험과 교체 규칙(7.1절)의 근거 |
| Golan, Raju & Kriegeskorte 2020, PNAS | doi:10.1073/pnas.1912334117 | DB | 논쟁 자극으로 모델 판정 |

### 4.2 선행 검색 기록 (구성 요소마다 질의 2개 이상, 모두 2026-11-12)

| 구성 요소 | 질의(경로) | 결과 |
|---|---|---|
| 되먹임(재진입) | (1) WebSearch "recurrent feedback from valence or amygdala module to visual network deep learning model reentry emotional images compared with visual cortex fMRI emotion representation" (2) WebSearch "top-down feedback recurrent deep network emotional salience visual cortex representation model comparison fMRI 2025 2026 reentry hypothesis model" | 정서 모듈의 되먹임을 조작해 사람 시각피질의 정서 표상과 비교한 연구는 미발견. 인접: VCA(피드포워드), Chen 2025 VSS(합성 fMRI, 되먹임 조작 없음), Tugsbayar 2026(되먹임 구성, 시청각 통합, 정서 아님), 예측 부호화 단위를 넣은 VGG16이 고차 시각피질 정렬을 높였다는 ESANN 2025 논문(search_index, 식별자 미확인). [AR]의 추가 검색에서도 판정 유지 |
| brain-tuning | (1) WebSearch "brain-tuning fine-tune vision or video model on amygdala or emotion-related fMRI responses improves human emotion judgment alignment" (2) WebSearch "brain-tuning vision model fine-tuned on fMRI responses natural scenes improves generalization 2025 2026 NSD fine-tune backbone brain-aligned" (3) WebSearch "neural network trained to predict human brain activity then tested on emotional images affective representation emerges brain-optimized model 2024 2025 2026" | 시각 영역 brain-tuning은 있다(ReAlnet-fMRI arXiv:2407.10414; Brainformer arXiv:2312.00236). 사회 영역은 Policzer 2025, 음성은 Moussa 2024(arXiv:2410.09230). **정서와 무관한 장면 반응으로 brain-tuning한 모델이 정서 서명을 만드는지 본 연구는 미발견**([AR] arXiv 20건 검색에서도 미발견) |
| 모델 내부 위계와 층-영역 배정(신규) | (1) WebSearch "assign DNN layers to cortical regions a priori representational similarity then compare hierarchy gradient of information across layers and cortex principal gradient" (2) PubMed "Brain hierarchy score deep neural networks hierarchically brain-like Nonaka Kamitani" (3) [AR] 1.4절의 arXiv 검색 결과(Höfling 2026, Nakamura 2026) | 층-영역 위계 대응 자체는 선행이 있다(Nonaka 2021 BH score; Pham 2021, 가치 과제 CNN 층과 principal gradient 대응). 정렬을 관계 구조로 평가하자는 방법 선행도 있다(Höfling 2026, Nakamura 2026). **정서 고유 정보와 비정서 통제의 초과 기울기를 정서와 무관하게 고정한 배정으로 비교하고 장치를 조작한 연구는 미발견** |
| 노출 대 라벨 대조(신규) | (1) WebSearch "controlling image exposure versus label learning: fine-tune CNN on emotional images with shuffled labels or self-supervised, compare emotion representation with brain" (2) WebSearch "random label shuffled-label fine-tuning control network representation brain alignment fMRI shuffled labels deep network emotion OR affective images" | 정서 이미지에서 섞은 라벨 대조로 뇌 정렬을 본 연구는 미발견. 인접: brain-tuning의 표적 순열 대조(음성 모델, Moussa 2024 계열), ImageNet 망의 정서 선택 unit(Liu 2024), CNN의 valence 정렬(Mertens 2025) |
| 묘사된 정서 통제(신규) | (1) WebSearch "facial expression of people on screen (portrayed emotion) confound evoked emotion ratings Cowen Keltner videos fMRI control face expression features 2024 2025" (2) WebSearch "Horikawa emotion videos fMRI faces present versus absent analysis Kiyokawa Hayashi 2024 emotion representation facial expression in video clips" | C&K 영상 fMRI에서 인물 표정 범주를 RDM으로 통제한 연구는 미발견. 인접: Kiyokawa & Hayashi 2024(얼굴 유무로 나눈 분석, DB), 얼굴 유무 조건 차이가 없었다는 Research Square 프리프린트(rs-4309581, search_index, 저자와 식별자 미확인) |
| 피질하 두 경로 | (1) WebSearch "dual pathway subcortical cortical deep neural network model emotion amygdala superior colliculus 2024 2025 2026 fMRI comparison" (2) Round 2와 재탐색의 WebSearch 기록(BI-P3, BI-RV-3) | 2024~2026년 이중 경로 DNN과 fMRI 비교는 미발견. 가장 가까운 것은 Méndez 2022(상구 단일 경로 모델)와 Leem 2026 |
| 지형 | (1) WebSearch "topographic deep neural network emotion selectivity map emerges cortical organization emotional images face body scene patches TDANN All-TNN" (2) WebSearch "topographic neural network affective emotional stimuli spatial organization amygdala-like or valence map 2024 2025 2026" | 지형 모델의 정서 선호 지도 연구는 미발견. 인접: fMRI 정서 지형 연구(emotionotopy), 공포 조건화 지형 지도 학회 초록(search_index) |
| 서명 재현(위계) | WebSearch "deep network model reproduces unimodal-to-transmodal gradient of emotion representation brain hierarchy non-emotional abstract features control social interaction" | 음악 CNN 층 경사와 피질 경사의 대응을 본 학회 초록(TeaP 2025, OHBM 2024 포스터, search_index)만. 비정서 통제와 모델 조건 조작을 결합한 연구는 미발견 |

* "미발견"은 이 검색 경로 안의 결과다. Stage 2 표본에서 no 판정의 약 25%가 뒤집혔으므로 최종 선정 전 중복 감사를 다시 해야 한다.

## 5. Novelty

* **판정: partially(구성 요소와 판정 방식에 각각 선행이 있고, 정서 초과 위계 서명과 장치 조작의 결합이 새롭다).**
* **가장 가까운 선행과의 차이:**
  * **Höfling 2026, Nakamura 2026(판정 방식):** 예측 정확도 대신 관계 프로필이나 회복 프로필로 정렬을 평가하자는 방법론이다. 대상은 시각 영역이고 정서 서명이나 장치 조작은 없다. 이 카드는 같은 문제의식을 "비정서 통제를 뺀 정서 초과 기울기"라는 특정 서명에 적용한다. 그래서 판정 방식 자체의 새로움은 주장하지 않는다.
  * **Nonaka 2021, Pham 2021(층-영역 위계 대응):** 층 위계와 피질 위계의 대응을 보였다. Pham 2021은 가치 과제 CNN에서 principal gradient 대응을 보였다. 이 카드의 배정은 그 대응을 정서와 무관한 기준으로 고정하는 도구로만 쓰고, 판정은 그 위에서 계산한 정서 고유 정보와 비정서 고유 정보의 기울기 차이로 한다.
  * **Soderberg, Jang & Kragel 2026:** 학습 과제(표정 대 장면)를 바꾼 정서 ANN으로 정서 영역을 예측했다. 이 카드는 학습 과제가 아니라 brain-like 장치(되먹임, brain-tuning)를 통제 요인으로 넣는다. 판정도 영역별 예측력이 아니라 피질 위계 전체의 정서 초과 기울기(S1′)와 해리(S2)로 한다.
  * **Gao 2025, Conwell 2025, Mertens 2025:** 정서 학습 대 사물 학습, 정서 없는 모델의 설명력, CNN의 valence 정렬을 주로 행동 평정이나 영역별 상관으로 보였다. 이 카드는 같은 출발점에서 정서 라벨 학습 유무와 정서 이미지 노출을 따로 조작한다. 그리고 그 효과를 차원과 신뢰도를 맞춘 비정서 의미 위계로 통제해 "정서 고유"와 "일반 추상화"를 가른다.
  * **ReAlnet-fMRI, Policzer 2025:** brain-tuning의 목표가 뇌 유사도나 해당 영역 과제였다. 이 카드는 정서와 무관한 NSD 일상 장면의 transmodal 반응으로 조율한다. 그다음 다른 코호트(Horikawa, MC)의 정서 영상에서 정서 서명이 생기는지 본다. 조율과 평가의 자극 분포, 피험자, 스캐너를 모두 분리해 C-06의 순환을 피한다.
  * **Chen, Keil & Ding 2025, VCA, Leem 2026(같은 연구군):** 재진입 쟁점을 합성 fMRI나 피드포워드 모듈로 다뤘다. 이 카드는 같은 망에서 되먹임 연결 자체를 조작한다. 여기에 매개변수를 맞춘 끝까지 미세조정 팔(C-05)과 섞은 라벨 되먹임 팔로 귀속을 엄격히 한다. 다만 이 연구군이 같은 쟁점을 연속으로 다루고 있어 선점 위험이 크다.
* **연구실 팀원 'TRIBE + emotion head' 작업과의 차이(overlap: 연구실 팀원 TRIBE 작업, 개념 인접).** TRIBE도 뇌 반응에 맞춰 학습한 모델이므로 사용자 정의의 (c)와 개념이 인접한다. 차이는 다섯 가지다.
  1. **조작 대상:** TRIBE 작업은 이미 학습된 다중양식 뇌 encoder에 정서 판독을 붙인다. R1은 작은 시각 모델을 같은 초기값에서 직접 키우며 brain-tuning의 유무와 표적 영역을 통제 요인으로 조작하고, 구조 제약(되먹임)과 정서 라벨 학습 대 노출을 교차시킨다.
  2. **양식:** R1은 시각 전용이다(C&K 무음). TRIBE는 소리 있는 영화로 학습되어 무음 입력이 분포 밖이다(plan.md 4절).
  3. **조율 자료:** R1의 brain-tuning은 정서와 무관한 NSD 정지 장면의 영역별 반응이다. TRIBE는 영화 전체 뇌 반응의 피험자 평균 예측기다.
  4. **판정:** R1은 정서 판독 정확도도 encoding 예측력도 결과로 쓰지 않는다. 모델 층 내부의 정서 초과 위계가 고정 배정을 거쳐 사람 뇌 서명(S1′, S2)과 맞는지로 판정한다.
  5. **사용 모델:** R1은 TRIBE를 쓰지 않는다.

## 6. Proposed Dataset

| 자료 | 쓰는 곳 | 실제로 있는 것(Stage 1, plan.md 4절 기준) | 관문, 주의 |
|---|---|---|---|
| Horikawa 2020 | 실측 서명, 층-영역 배정(배정용 절반), 모델 서명 평가(평가용 절반) | 5명, 고유 2,181클립(무음, 평균 약 5 s) 단일 제시. 블록 평균 native volume HDF5에 HCP360과 피질하 ROI 포함. C&K 34범주와 14차원 규범 평정. **73차원 의미 feature**(Horikawa 2020 Results에 crowdsourcing 인간 주석으로 기술, Stage 1 보고서 116행). 원본 비디오 보유(사용자 확인) | 반복 없음(직접 잡음 천장 없음, 피험자 간 상한으로 대신). pulvinar ROI 없음. TE 43 ms(피질하 신호 약함). 같은 원본에서 잘린 클립의 movie-level leakage 미확인. 의미 feature의 평정자 수와 개인 자료는 미확인. principal gradient 값이 figshare MATLAB판 파일 목록에 있다고 Stage 1이 적었으나 figshare 페이지는 미열람 |
| Mind captioning(MC) | 같은 서명의 독립 코호트 확인, parcel RDM 잡음 천장 | 6명, 학습 2,108클립 고정, 시험 72클립 x 5회(plan.md 4절). 정서 배제 지시로 받은 사람 캡션(GPT-3.5 교정). 전처리 완료 보유본 | **관문: 보유본 전처리 형식과 parcel 정보 미확인.** 원 논문 방식(4 s shift 후 블록 평균)으로 맞출 수 있는지 1주차 확인. 시험 72클립은 학습 세션 마지막 두 run에도 나왔다(학습은 2,108로 고정) |
| NSD | brain-tuning 표적(정서와 무관한 자극 분포), 층-영역 배정의 강건성 판 | 8명, 7T, 1인당 약 1만 장 COCO, GLMsingle beta. pRF, fLoc, streams, nsdgeneral ROI(Stage 1). 3회 반복 제시와 연속 재인(old/new) 과제(Allen 2022) | **관문(13절):** 표적 ROI 잡음 천장(ncsnr), 재인 반응 혼입, HCP_MMP1 피험자 공간 atlas 유무. transmodal beta에 친숙도와 재인 신호가 섞인다(dataset_NSD.md 209행). NSD 이미지 정서가는 대체로 중립(의도한 성질) |
| EmoSet-118K | E 팔의 정서 라벨 학습, E-ff-shuf의 노출 대조 | 118,102장, Mikels 8범주(긍정 4, 부정 4: anger, disgust, fear, sadness), 별도 평정자의 perceived 라벨(arXiv:2307.07961, DB) | 이미지와 라벨 이용 조건 미확인(frontier-ai: 코드 저장소 MIT 확인). C&K 프레임, Horikawa/MC 프레임, NSD 이미지와 지각 해시 중복 검사. EmoSet 라벨도 이미지 속 표정과 강하게 상관할 수 있다([ET] 1.4) |
| 비정서 통제(주) | S1′의 비정서 기울기, 모든 정서 서명의 내용 통제 | Horikawa 73차원 의미 feature를 주성분 34개로 줄인 것. 차원 수를 34범주 정서 RDM과 맞춘다. 이름이 정서어인 개념이 있으면 등록 전에 뺀다 | R2 카드도 같은 feature를 비정서 방향으로 쓴다. 주성분 계산 절차(전체 2,181클립에서 한 번, 표준화 방식)는 R2와 1주차에 맞춘다 |
| 비정서 통제(보조) | S1′의 강건성 | (1) MC 사람 캡션에서 규칙과 공개 언어 모델로 뽑은 속성: 사람 수, 사회적 상호작용 유무와 강도, 행위 강도, 실내외, 동물 유무. (2) 같은 캡션으로 LLM이 매긴 비정서 종합 판단: 사건의 이례성, 목표 지향 행위, 마음 상태 추론 요구([ET] 1.2 제안) | 모두 [AI-est]. 서로 다른 두 모델로 두 번 추출해 추출 간 일치도를 신뢰도로 쓴다. 연구자 본인 100클립 점검 |
| 묘사된 정서 묶음(신규) | 모든 정서 서명의 통제 | 프레임마다 (1) 얼굴 수와 얼굴 크기(화면 비율), (2) 공개 표정 모델(Py-Feat, doi:10.1007/s42761-023-00191-4)의 기본 표정 확률과 AU, (3) 공개 가중치 VLM 하나로 매긴 인물 몸짓, 자세의 정서 범주(모델과 이용 조건은 1주차에 정해 기록). 클립 단위로 평균 | [AI-est]. **오염 점검:** VLM에는 프레임만 주고 파일명, 클립 번호를 주지 않는다. 인물을 가린 프레임에도 같은 질문을 해, 표정 없이 장면 내용만으로 나오는 판단의 비율을 잰다. 표정 모델의 학습 자료가 C&K와 다른지 문서로 확인한다. 연구자 100클립 점검과의 일치도를 보고한다 |

* **쓰지 않는 자료와 이유:**
  * Emo-FilM과 Spacetop: 소리 있는 영상이라 무음 시각 모델의 서명 비교와 맞지 않는다. 확장에서 R3 축이나 다른 코호트 재현에만 검토한다.
  * EmoNet: 누수.
  * TRIBE v2: 분포 밖이고 팀원 작업과 구분해야 한다.
  * 웹 규모 VLM을 정서 라벨 원천으로 쓰는 것: C&K 오염 가능성. VLM은 묘사된 정서 묶음(통제 변수)에만 쓰고 오염 점검을 붙인다.
* **라벨 주체:** C&K 평정은 별도 평정자가 영상을 보고 보고한 정서의 집계다. 주장은 "장면의 정서적 의미(규범 기준)"까지만 한다(design_brief 3절 5번).

## 7. Proposed Computational Framework

### 7.1 4주 핵심 판(core): 8팔

모든 팔은 같은 출발점(ImageNet 사전학습 ResNet-50, torchvision 공개 가중치)에서 시작한다. A0을 뺀 각 팔은 seed 3개로 학습한다(7팔 x 3 = 21회).

| 팔 | brain-tuning (c) | 정서 학습과 구조 (a) | 역할 |
|---|---|---|---|
| A0 | 없음 | 없음 | 출발점. 일반 추상화 가설의 기준. 층-영역 배정을 정하는 모델 |
| B-tm | NSD transmodal ROI | 없음 | "사람 고차 영역의 반응 형식"이 정서 서명을 만드는가 |
| B-vis | NSD 시각 ROI | 없음 | 대조: 조율 자체의 효과 |
| B-rand | 신뢰도를 B-tm 표적에 맞춘 무작위 비시각 parcel | 없음 | 대조: transmodal이라서가 아니라 신호 품질 때문인지 |
| E-ff | 없음 | EmoSet 8범주 + valence, 모든 층 학습, 입력을 끈 같은 크기 gain 모듈 포함 | 정서 라벨 학습. 끝까지 미세조정 팔(C-05 대조) |
| **E-ff-shuf(신규)** | 없음 | E-ff와 같은 이미지, 손실, step 수, gain 모듈. 이미지와 라벨의 짝을 섞는다(범주 비율 유지, valence 보조 라벨도 같이 섞음) | 대조: 정서 이미지 노출만의 효과. E-ff와의 차이가 "라벨 학습"의 몫 |
| E-fb | 없음 | E-ff와 같은 목표, 정서 모듈의 되먹임이 중간층(layer2, layer3)을 채널별 gain으로 조절, 두 번 통과 | 재진입 구조 제약 |
| E-fb-shuf | 없음 | E-fb와 같은 구조, 라벨 섞음 | 대조: 되먹임의 용량 효과 |

* **무엇을 남기고 왜 남겼나.**
  * A0, B 셋, E-ff, E-fb, E-fb-shuf: 네 설명(일반 추상화, 고차 반응 형식, 개념 학습, 재진입)을 가르는 최소 집합이다. [AR] 1.1-5의 7팔 제안과 같다.
  * E-ff-shuf를 더했다([ET] 1.5-2, 수정 지시 5번). Conwell 2024가 학습 자료를 가장 큰 요인으로 보고했으므로, 이 팔 없이는 E 팔의 성공을 "라벨 학습"으로 해석할 수 없다. E-fb-shuf는 되먹임의 용량 대조라 이 역할을 대신하지 못한다.
  * 상호작용 두 팔(B-tm → E-ff, B-tm → E-fb)은 확장 X6으로 옮겼다. 4주 판의 판별력은 거의 늘리지 않으면서 비교 수만 늘린다([AR] 1.1-5).
* **E-ff-shuf 교체 규칙(사전 등록).** 큰 망은 섞은 라벨도 외우며(Zhang et al. 2017, arXiv:1611.03530), 그 과정에서 표상이 손상될 수 있다. ImageNet 보류 top-1 정확도가 E-ff보다 10%p 넘게 떨어지면 노출 대조를 EmoSet 이미지 자기지도 학습 팔(같은 step 수의 대조 학습)로 바꾼다. 바꾸면 그 사실과 이유를 보고한다.
* **입력:** C&K 클립마다 균등 간격 프레임 8장, 224 px. 모든 팔을 학습 해상도와 같은 224 px로 평가한다(초기 시각 RSA가 평가 해상도에 좌우된다는 arXiv:2608.12408의 경고). 무음이라 시각만 쓴다. 정지 프레임 평균은 움직임 정보를 잃는 공통 불리함이 있다(reviewer_notes 8절 3번). 모든 팔에 같게 작용하므로 팔 간 비교는 유지된다.
* **출력과 손실:**
  * 정서 학습: EmoSet 8범주 교차엔트로피 + valence(긍정/부정) 보조 손실
  * brain-tuning: NSD 피험자별 선형 readout으로 ROI beta 예측, voxel별 상관 손실. 표적 피험자 4명(세션 수가 가장 많은 피험자, 목록은 1주차에 Stage 1 보고서와 대조), 학습/검증은 이미지 단위 분할. **shared1000 이미지는 조율에서 뺀다**(배정 강건성 판에 쓰기 때문). beta는 재인 반응을 회귀한 판을 쓴다(13절 관문)
  * 되먹임: 정서 모듈 은닉 벡터에서 선형층을 거쳐 layer2, layer3 출력에 (1 + tanh) gain을 곱한다. 첫 통과로 정서 상태를 만들고 두 번째 통과에서 적용한다. E-ff와 E-ff-shuf에는 같은 크기의 gain 모듈을 두되 입력을 상수로 고정해 매개변수 수를 맞춘다
* **학습 성공 확인:** EmoSet 보류 정확도(E-ff-shuf는 우연 수준이어야 한다), NSD 보류 이미지의 ROI 예측 상관, ImageNet 보류 정확도(물체 표상이 무너지지 않았는지).
* **서명 계산 단위:** ResNet-50의 conv1과 bottleneck 블록 16개(총 17단계) 출력. 공간 지도를 펼친 뒤 고정 seed의 희소 무작위 사영으로 4,096차원으로 줄인다(전역 평균 풀링 판은 강건성). 분류 head는 서명 계산에서 뺀다. E 팔의 마지막 블록에 정서 정보가 많은 것은 학습 목표의 직접 결과이므로, 판정은 마지막 블록 값이 아니라 배정된 블록 전체의 프로필로 한다.
* **관련 뇌 영역과 위계 축:**
  * HCP360 cortical parcel마다 Margulies 2016 주 경사(doi:10.1073/pnas.1608282113) 값을 쓴다. 기울기는 parcel 단위로 계산한다([AR] 1.2).
  * 사전 지정 묶음(초기 시각 V1~V3, 고차 시각 LOC, VTC, MT 주변, 측두-두정 연합 TPJ, STS, transmodal PCC/precuneus, mPFC, 측두극)은 그림과 보고용으로만 쓴다.
  * 피질하는 핵심 판에서 판정에 쓰지 않는다(C-07).
* **GPU 추정(미검증, 실측 아님):**
  * EmoSet 미세조정: 회당 약 1~2 GPU 시간(약 118만 장 처리)
  * NSD brain-tuning: 회당 약 1~2 GPU 시간
  * 21회 합계 약 25~45 GPU 시간. GPU 2~4장이면 2주차 안에 끝난다. B 팔이 관문에서 빠지면 12회
  * RDM, 서명, encoding 계산은 CPU

### 7.2 확장(4주 이후, 핵심 판 결과에 따라)

| 확장 | 내용 | 연결된 결함 | 전제 |
|---|---|---|---|
| X1 피질하 두 경로 | 저공간주파수, 초기층 지름길에서 정서 모듈로 가는 경로를 켜고 끈다(Leem 2026 구조. 지름길 없는 모델의 학습 실패는 본문 Discussion 2단락과 Supplementary Fig. S2, Appendix B.1) | C-07: Horikawa ROI에 pulvinar 없음, 편도체 신호 약함(3T, TE 43 ms). Méndez 2022 선행 | MC 반복으로 편도체 신뢰도 관문 통과 시에만. 시상은 전체 ROI로만 |
| X2 재귀 깊이와 S3 | 시간 단계가 많은 재귀 망(BLT, Spoerer 2020)으로 클립별 정서 판독 재귀 요구량을 계산하고 클립별 정서 정보 위치(S3)를 예측 | C-08: CORnet-S는 재귀 단계가 적다 | BLT 가중치 공개와 이용 조건 미확인. 없으면 같은 구조를 ImageNet 하위 집합으로 직접 학습(무거움) |
| X3 지형 | TDANN 공개 checkpoint에서 정서 선호 단위의 공간 군집과 얼굴, 신체, 장면 구역과의 관계를 분석하고 MC fLoc 지도와 비교 | C-09: 학습이 무겁고 LICENSE가 없다(Coordinator 확인). checkpoint는 OSF에 공개(Margalit 2024 원문) | 이용 조건을 저자에게 확인한 뒤 분석만 한다(재학습 없음) |
| X4 학습 자료 | 정서 단어 제거(Affection 자료, FA-RV-4), 사람 제거(COCO, FA-RV-3). 정서 단어 제거는 구성주의 언어 가설에 가장 가까운 조작이다([ET] 1.6-4) | 핵심 판에서 라벨 학습 효과가 나올 때 S2의 원인을 좁히는 검정. **4주 계획의 조건부 분기(14절)** | Affection 이용 조건 미확인 |
| X5 R3 재현 축 | geometry-info R3가 넘겨 주는 재현 뇌 축(축 정의, 클립 점수, 신뢰도)을 추가 서명으로 쓴다 | 없음 | R3 결과 |
| X6 상호작용(핵심 판에서 이동) | B-tm → E-ff, B-tm → E-fb | 핵심 판에서 B-tm과 E 팔이 모두 단독으로 실측에 가까워질 때만 의미가 있다 | NSD 관문 통과, 핵심 판 결과 |
| X7 자기지도 노출 대조 | EmoSet 이미지 자기지도 학습 팔 | E-ff-shuf가 교체 규칙에 걸리지 않았을 때 노출 대조의 두 번째 판 | 핵심 판 결과 |

## 8. Proposed Analyses

### 8.1 공통 재료: feature RDM과 신뢰도

* **클립 분할.** Horikawa는 클립을 배정용 절반과 평가용 절반으로 나누고 역할을 바꿔 한 번 더 한다(2겹). 같은 원본에서 잘린 클립은 원본 ID가 확인되면 같은 쪽에 둔다. MC는 학습 2,108클립에서 같은 2겹을 쓰고, 시험 72클립 x 5회는 parcel RDM의 잡음 천장 추정에만 쓴다.
* **feature RDM(클립 단위):**
  * F_emo: C&K 34범주 점수 프로필 사이 거리(주 정서 RDM)
  * F_cat: 34범주 점수에서 valence, arousal을 회귀로 뺀 잔차의 거리
  * F_aff: valence, arousal(14차원 중 2개)의 거리
  * F_app: certainty, control, fairness, obstruction, safety(14차원 중 5개)의 거리
  * F_sem: 73차원 의미 feature의 주성분 34개 거리(주 비정서 통제)
  * F_ai: AI 추출 속성과 LLM 비정서 종합 판단의 거리(보조 비정서 통제)
  * F_por: 묘사된 정서 묶음의 거리
  * F_low: 저수준 영상 통계(밝기, 대비, 색, 움직임 에너지)의 거리
* **신뢰도 보고와 보정([AR] 1.1-3, [ET] 1.2).**
  * 통제 변수의 신뢰도가 낮으면 고유 효과가 부풀려진다(Westfall & Yarkoni 2016). 그래서 F_emo, F_sem, F_ai, F_por의 split-half 신뢰도를 보고한다.
  * 평정자 개인 자료가 있으면 평정자를 반으로 나눠 계산한다. Horikawa figshare에는 클립당 집계값만 있다(Stage 1 G3). 그래서 1주차에 C&K 2017 원 자료와 Horikawa 의미 feature의 개인 자료를 찾는다. 찾지 못하면 실제 신뢰도 대신 민감도 분석으로 바꾼다. 두 RDM의 신뢰도 비를 0.5~2배 범위에서 가정해 감쇠를 보정하고, S1′의 부호가 유지되는 범위를 보고한다.
  * AI 특징(F_ai, F_por)은 서로 다른 두 모델로 추출한 판 사이의 일치도를 신뢰도로 쓴다.

### 8.2 실측 뇌 서명

1. **parcel RDM.** 피험자마다 HCP360 cortical parcel별로 평가용 클립의 voxel 패턴 사이 상관 거리를 구한다(재가중 없음).
2. **고유 정보(상호 통제).**
   * U_emo(p) = parcel RDM과 F_emo의 부분 Spearman 상관(F_sem, F_low, F_por 통제)
   * U_sem(p) = parcel RDM과 F_sem의 부분 Spearman 상관(F_emo, F_low, F_por 통제)
   * 보조: F_sem 대신 F_ai로 같은 계산
3. **잡음 정규화.** U를 parcel RDM의 상한으로 나눈다. Horikawa는 반복이 없으므로 피험자 간 상한(다른 피험자 평균 RDM과의 상관)을 쓴다. MC는 시험 72클립 x 5회의 split-half 상한을 함께 보고한다.
4. **S1과 S1′.**
   * 위계 축 값 g(p)에 대한 기울기를 parcel 단위(360점)로 구한다. S1′ = 기울기(U_emo) − 기울기(U_sem).
   * **순위 판(주 판정용, 척도에 무관):** S1′_rank = Spearman(g, U_emo) − Spearman(g, U_sem).
   * 강건성: parcel마다 π(p) = U_emo / (U_emo + U_sem)의 기울기. parcel별 잡음 감쇠가 두 U에 같은 비율로 걸리면 π에서는 상쇄된다.
   * 신뢰구간은 클립 bootstrap과 피험자 bootstrap으로 구한다.
5. **이중 위계(S1-cat 대 S1-aff)와 appraisal 기울기(S1-app).** F_emo 대신 F_cat, F_aff, F_app로 같은 계산을 한다. 각각 F_sem, F_low, F_por와 나머지 둘을 통제한다. 비용 없이 같은 절차로 얻는다([ET] 1.7-1, 1.7-3).
6. **묘사된 정서의 몫.** U_emo를 F_por 통제 유무로 두 번 계산해 차이를 보고한다. F_por와 F_emo의 RDM 상관이 높아(사전 기준: Spearman 0.6 이상) 통제 뒤 U_emo가 불안정하면, 그 결과에 '묘사된 정서 지각 포함'을 붙인다.
7. **S2(내용 통제 위, [ET] 1.5-1).**
   * voxel 패턴에서 내용 특징(F_low, F_sem, F_por의 원 특징)을 회귀로 뺀다. 회귀 가중치는 배정용 절반에서 학습해 평가용 절반에 적용한다.
   * 남은 패턴에서 범주마다 클립을 두 반으로 나눠 범주 중심 사이 crossnobis 거리를 구한다.
   * **주 판:** 부정 범주는 anger, disgust, fear, sadness 넷이다. EmoSet 부정 4범주, Lindquist 2014의 부정 범주와 같다. 지배 클립이 20개 미만인 범주는 범주 점수로 가중한 중심을 쓴다(1주차에 범주별 클립 수를 센다).
   * **일반화 판:** horror, anxiety, empathic pain을 더한다.
   * R_S2 = (부정 범주끼리 평균 중심 거리) / (긍정 대 부정 중심 거리). 긍정과 부정은 C&K valence 차원의 상위와 하위 삼분위로 나눈다.
   * 강건성: 서로 다른 부정 범주에서 의미 주성분 공간의 최근접 클립 쌍을 골라 쌍 안에서만 거리를 잰다.
   * **표적:** 건강한 사람 뇌의 R_S2 값 자체를 "재현"하는 것이 아니다. 개념 없는 팔(A0, B 셋, E-ff-shuf, E-fb-shuf)이 환자형(valence 분리 유지, 부정 범주 간 거리 축소, 낮은 R_S2)을 보이고, 라벨을 배운 E 팔의 R_S2가 사람 뇌의 R_S2 쪽으로 움직이는지가 예측이다([AR] 1.2, [ET] 1.2 간극 2).

### 8.3 모델 서명(주 서명)

1. **모델 블록 RDM.** 각 팔, seed, 블록 l(17단계)에서 평가용 클립의 프레임 평균 활성 사이 상관 거리를 구한다(재가중 없음).
2. **모델 내부 고유 정보.** U_emo(l), U_sem(l)을 8.2절 2번과 같은 feature RDM과 같은 부분 통제로 계산한다. 모델 RDM에는 측정 잡음이 없으므로 잡음 정규화는 하지 않는다.
3. **모델 내부 S1′.** S1′_int = Spearman(블록 깊이, U_emo) − Spearman(블록 깊이, U_sem). 깊이별 프로필 전체를 함께 보고한다. 이것은 뇌와 무관하게 "그 모델에 정서 초과 위계가 있는가"를 답한다.
4. **층-영역 배정(정서 서명 계산 전에 등록).**
   * A0에서, 배정용 클립만으로, parcel p마다 l*(p) = argmax_l [parcel RDM과 블록 RDM의 부분 Spearman 상관(F_emo, F_aff, F_por 통제)]을 정한다. 정서 관련 RDM을 통제하므로 배정 기준은 정서와 무관한 내용 구조다.
   * 피험자 평균 RDM으로 정하고 결과표를 저장해 모든 팔에 고정한다. 배정용 클립과 평가용 클립은 겹치지 않는다(순환 추론 방지).
   * 배정의 질을 보고한다: Spearman(l*(p), g(p)). Nonaka 2021, Pham 2021과 같은 위계 대응이 나오는지의 확인이다. 두 코호트 모두에서 0.3 미만이면 뇌 좌표 비교가 약하다고 보고, 주 판정을 S1′_int와 실측 S1′_rank의 부호, 순위 일치로 낮춘다(사전 등록).
   * 강건성 판: (a) NSD shared 이미지(조율에서 뺀 이미지)에서 A0 블록과 NSD parcel의 재가중 없는 RSA로 정한 배정. 자극이 대체로 중립이라 정서와 무관한 기준이 더 엄격하다. (b) 팔마다 다시 정한 배정.
5. **뇌 좌표 모델 서명.** parcel p에 U(l*(p))를 채우고, 실측과 같은 parcel 집합과 g(p)로 S1′_rank를 계산한다. S1-cat, S1-aff, S1-app, R_S2도 같은 배정으로 계산한다.
6. **층별 변화량.** 각 블록에서 팔과 A0의 표상 차이(CKA)를 보고한다. 일반적인 미세조정은 주로 후기 층을 바꾼다는 점(C-20)과, 학습이 초기 시각 정렬을 낮출 수 있다는 점(Leutenegger 2026 정정본)을 함께 본다. 기울기의 감각 쪽 끝이 바뀌어 S1′이 바뀐 것인지 가르기 위해서다.
7. **보조 판: 모델 예측 뇌.** 각 팔의 블록 특징으로 피험자, parcel별 ridge encoding을 학습해(층은 학습 클립 안 중첩 교차검증으로 선택) 보류 클립 예측 반응을 만들고 같은 서명을 계산한다. **parcel별 encoding R²를 공변량으로 같이 보고한다.** 팔 간 S1′ 차이를 팔 간 R² 기울기 차이에 회귀해, 적합도 프로필로 설명되는 몫을 밝힌다.

### 8.4 판정과 비교

* **거리.** 각 팔 a에서 D(a) = |모델 S1′_rank(a, 뇌 좌표) − 실측 S1′_rank|. seed(3개), 피험자, 클립 bootstrap으로 분포를 낸다. 순위 판이라 모델(잡음 없음)과 실측(잡음 있음)의 척도 차이에 덜 민감하다. MC에서는 잡음 천장으로 정규화한 기울기 판을 함께 낸다.
* **사전 등록한 쌍 대비 4개(주 판정).** ΔD = D(앞) − D(뒤). 음수면 앞 팔이 실측에 더 가깝다.
  1. C1: E-ff 대 A0(정서 라벨 학습)
  2. C2: E-ff 대 E-ff-shuf(라벨 학습 대 이미지 노출)
  3. C3: E-fb 대 E-ff(되먹임, 매개변수 맞춤)
  4. C4: B-tm 대 B-rand(transmodal 조율 대 신호 품질)
  * 보조 대비: B-tm 대 B-vis, E-fb 대 E-fb-shuf, B-tm 대 A0, E-ff-shuf 대 A0(노출만의 효과).
* **판정 규칙.**
  * "앞 팔이 더 가깝다": Horikawa(발견)에서 ΔD의 95% 구간이 0 아래이고 MC(확인)에서 같은 부호.
  * "차이 없음": ΔD의 95% 구간이 사전 등록한 동등성 한계 안. 한계는 E-ff 세 seed 사이 D 차이를 피험자 bootstrap과 합친 분포의 95% 범위로 정한다. seed가 셋뿐이라 seed 변동만으로는 범위를 잡기 어렵기 때문이다. 2주차 학습 직후, 팔 간 서명 비교 전에 고정한다(reviewer_notes 8절 4번).
  * 그 밖은 "판정 보류".
  * 주 대비 4개는 Holm 보정한다.
* **보조 지표.** parcel 프로필 일치도: Spearman(모델 Δ(p), 실측 Δ(p)), Δ = U_emo − U_sem. 척도에 무관하다. S1-cat 대 S1-aff, S1-app, R_S2도 같은 쌍 대비로 보고하되 주 판정에는 넣지 않는다.
* **기준선.** A0, 무작위 초기화 ResNet-50(구조만의 기준선), 피험자 간 상한, MC 잡음 천장.
* **모델 내 lesion.** E-fb의 시험 시점 되먹임 차단, brain-tuning 전후 비교.
* **논쟁 클립 확인.** C2, C3, C4 쌍의 블록 RDM이 가장 갈리는 클립을 모델 출력만으로(뇌 자료를 보지 않고) MC 평가용 클립에서 미리 고른다. 그 클립들의 실측 parcel RDM이 어느 쪽 모델을 따르는지로 쌍 대비 결과를 확인한다(Golan 2020).
* **검증 전략.** Horikawa에서 발견하고 MC에서 확인한다. 두 코호트는 스캐너가 달라(Verio 대 Prisma) 코호트 안에서 따로 분석한다.

## 9. Competing Explanations

| 대안 설명 | 무엇이 같은 결과를 만드나 | 가르는 분석 |
|---|---|---|
| 일반 추상화 위계 | 어떤 추상 속성이든 고차 영역에 많다 | S1′(차원을 맞춘 비정서 의미 기울기 빼기). 사람에서 S1′ ≈ 0이면 이 설명이 이긴다 |
| 라벨의 추상 수준(종합 판단) | 규범 정서 평정은 장면 전체의 종합 판단이라 기울기가 가파르다 | 주 비정서 통제를 인간 주석 73개 의미 개념으로, 보조를 LLM 비정서 종합 판단으로 둔다. 둘 다에서 S1′ > 0이어야 정서 초과로 읽는다 |
| 측정 신뢰도 차이 | 비정서 RDM의 신뢰도가 낮아 비정서 기울기가 낮게 나온다 | split-half 신뢰도 보고, 감쇠 보정 또는 신뢰도 비 민감도 분석(8.1절) |
| 묘사된 정서 | 인물 표정, 몸짓(STS, TPJ 처리)이 "정서 고유 정보"의 일부를 만든다 | F_por 통제와 통제 전후 차이(8.2절 6번). 못 가르면 '묘사된 정서 지각 포함' |
| encoding 적합도 프로필 | transmodal 적합도가 낮은 팔은 예측 뇌의 기울기가 낮다 | 주 서명을 모델 블록 RDM과 고정 배정으로 계산(8.3절). 예측 뇌 판은 R² 공변량과 함께 보조로만 |
| 시간 통합 창 위계(Hasson 2008) | 고차 영역의 긴 통합 창이 긴 맥락 속성을 담는다 | 블록 평균 자료로는 가를 수 없다. 이론적으로 가능하지만 관찰 데이터로 구분할 수 없는 설명으로 표시한다 |
| 정서 이미지 노출 | 라벨이 아니라 정서 이미지 분포를 본 것만으로 생긴다 | C2(E-ff 대 E-ff-shuf) |
| 학습량, 용량 | 정서 학습 팔이 그냥 더 많이 학습했다 | 모든 팔의 step 수 고정, 매개변수 맞춘 gain 모듈, E-fb-shuf |
| 조율 표적의 신호 품질 | transmodal 표적이 신뢰도가 높아서가 아니라 조율 자체 효과 | B-rand(신뢰도 맞춤), B-vis, NSD 잡음 천장 관문 |
| 재인과 친숙도 신호 | B-tm이 장면 의미가 아니라 NSD의 old/new 신호에 맞춰진다 | 재인 회귀자를 뺀 beta, 첫 제시 beta 강건성 판(13절) |
| 초기 층 정렬 변화 | E 팔 학습이 감각 쪽 끝을 바꿔 기울기가 바뀐다 | 블록별 CKA 변화량, 같은 해상도 평가(8.3절 6번) |
| 의미 내용 누출 | 의미 통제가 놓친 사회 내용이 정서처럼 보인다 | 상호 통제, 보조 비정서 통제, 논쟁 클립, 사람 수 층화 |
| 시선, 주의 이득 | 정서 클립에서 시선이 다르다 | MR 기반 시선 추정(DeepMReye, doi:10.1038/s41593-021-00947-w)은 촬영 범위 확인 후 공변량으로(확장) |
| 학습 자료 오염 | ImageNet, EmoSet에 C&K 유사 이미지 | 지각 해시 중복 검사, 중복 제거 판 재학습 |

## 10. Potential Findings

사전 등록할 결과 지도다. "더 가깝다"는 8.4절 쌍 대비 규칙 기준이다. 표시 열은 그 결과를 반대로 예측하는 이론이 있는지에 따른다. 반대 예측이 없으면 [양립]이다([ET] 1.1, 공통 2). 모든 해석의 "정서"는 장면의 정서적 의미(규범 기준)이고, 8.2절 6번에서 묘사된 정서를 가르지 못하면 '묘사된 정서 지각 포함'이 붙는다.

| 관찰 패턴 | 해석 | 정서 이론에 주는 말 | 반대를 예측하는 이론 | 표시 |
|---|---|---|---|---|
| 사람 S1′ ≈ 0(1주차, 첫 결과) | Horikawa의 위계는 일반 추상화 위계다 | 사용자 지적이 맞다. "정서의 고차 위치"는 정서 고유 주장이 아니다. 구성주의의 영역 일반 주장(Satpute & Lindquist 2019) 쪽으로 약하게 기운다 | 없음. BET는 전용 회로를 주로 피질하에 두므로 반대를 예측하지 않는다 | [양립], 약한 구성주의 쪽 |
| 사람 S1′ > 0(1주차, 첫 결과) | 규범 정서 정보가 차원을 맞춘 비정서 의미 정보보다 더 transmodal에 몰린다 | 구성주의(DMN의 범주 개념화), appraisal(내측 전전두의 추상 평가), BET의 피질 판본 모두 허용 | 없음 | [양립] |
| 사람 S1-cat 기울기 > S1-aff 기울기 | 범주 정보가 affect 정보보다 더 transmodal 쪽이다 | 구성주의 예측(Satpute & Lindquist 2019)과 맞는다 | BET는 범주 정보도 감각 쪽에 상당량 있다고 예측한다(Kragel 2019 방향) | 판별적 |
| 사람 S1-app 기울기가 S1-cat보다 완만(중간 수준에도 appraisal 정보) | appraisal 정보가 여러 수준에 걸쳐 있다 | CPM의 다수준 appraisal 예측과 맞는다. 단 규범 appraisal 평정이지 appraisal 과정이 아니다 | 범주 중심 관점은 범주와 같은 transmodal 집중을 예측한다 | 약한 판별 |
| S1′ > 0이고 A0의 D가 동등성 한계 안 | 정서 초과 위계가 일반 시각 학습만으로 생긴다 | "이산 정서 구조는 정서 개념 지식이 있어야 생긴다"는 강한 구성주의 주장에 반하는 증거. 지각 우선(Conwell 2025), 내재 가설 쪽. 단 A0도 사물 개념(ImageNet 라벨)을 배웠다 | 강한 구성주의(개념 필요) | 판별적(조건부) |
| C1에서 E-ff가 더 가깝고, C2에서 E-ff-shuf보다도 더 가깝다 | 정서 범주 감독 학습(이미지와 라벨의 연합)이 필요하다 | 정서 범주 감독 학습이 필요하다. 구성주의와 BET 모두와 양립하며(BET도 범주 인식 학습을 예측), 이미지 노출 대조를 통과했으므로 노출이 아니라 라벨 학습으로 좁혀진다. 언어 개념 자체인지는 X4가 가린다 | 지각 우선, 내재 가설(라벨 없이 생긴다고 예측) | BET 대 구성주의는 [양립], 지각 우선에 대해서는 판별적 |
| C2에서 차이 없음(E-ff-shuf도 E-ff만큼 가깝다) | 정서 이미지 분포에 노출된 것만으로 생긴다 | 라벨 없는 통계 학습으로 충분하다. 개념 학습 가설에 반한다 | 개념 학습 가설(구성주의의 언어, 개념 판본) | 판별적 |
| C3에서 E-fb가 더 가깝다(매개변수 맞춤) | 정서 판단의 되먹임 구조가 필요하다 | 재진입 대 내재 쟁점에서 재진입 쪽(표상 내용 수준. 시간 순서 증거는 아님). 정서 이론 사이에서는 편도체 되먹임(BET), 예측 처리(구성주의, Barrett 2017), 반복 appraisal(CPM)이 모두 되먹임을 예측한다 | 내재 가설(Liu 2024가 미해결로 남긴 대안) | 재진입 대 내재는 판별적, 정서 이론 사이는 [양립] |
| C4에서 B-tm이 더 가깝고 B-vis보다도 가깝다 | 일상 장면에 대한 사람 고차 영역의 반응 형식이 정서적 의미의 조직을 이미 담는다 | 정서적 의미가 장면 이해의 일반 고차 표상 안에 놓인다는 해석(Gao 2025 방향). 영역 일반 관점(구성주의, 장면 의미의 appraisal) 쪽 | 전용 정서 학습이 필요하다는 관점. BET의 피질하 판본과는 양립 | 약한 판별 |
| 어느 팔도 실측에 가까워지지 않는다 | 시험한 장치로는 부족하다 | 무엇이 필요한지는 이 결과로 말할 수 없다. 학습 자료, 영상 대 정지 이미지, EmoSet 대 C&K 범주 불일치 등 대안이 많다 | 해당 없음 | 이론적 함의 없음 |
| S2: 개념 없는 팔(A0, B, E-ff-shuf, E-fb-shuf)은 환자형, E 팔의 R_S2는 사람 뇌 쪽으로 이동(내용 통제 뒤) | 정서 라벨 학습이 부정 범주 구분을 만든다 | 구성주의 방향(Lindquist 2014, Souter 2021). 문장 범위는 "장면의 규범 정서 범주 구조가 개념 학습 없이는 생기지 않는다"까지 | BET(개념 없이도 범주 구조) | 판별적 |
| S2: A0가 내용 통제 뒤에도 사람처럼 부정 범주를 나눈다 | 개념 없이도 범주 구조가 생긴다 | 지각 쪽, BET와 양립 | 강한 구성주의 | 판별적 |
| E 팔에서만 S1-cat이 S1-aff보다 가파르고 실측과 같은 방향 | 범주 학습이 범주 정보를 위로 밀어 올린다 | 구성주의의 이중 위계 예측을 학습자 수준에서 지지 | BET(범주 정보의 감각 쪽 존재) | 판별적 |

## 11. Scientific Contribution

* **질문의 성격.** Affective Neuroscience의 "장면의 정서적 의미는 뇌에서 어디에, 왜 그렇게 놓이는가"를 관찰이 아니라 통제된 인공 학습자로 묻는다. plan.md 2절 (a)에 해당한다(학습 조건을 조작한 인공 뇌, 구조 제약을 바꾼 모델).
* **첫 결과(모델과 무관).** 1주차 실측 S1′은 Horikawa 2020의 transmodal 정서 위치가 차원과 신뢰도를 맞춘 비정서 의미 정보의 위계를 넘는지를 처음 묻는다. 같은 절차로 범주 대 affect 이중 위계와 appraisal 기울기도 나온다. 이 셋은 모델 팔이 실패해도 남는다.
* **이론적 기여 네 갈래.**
  1. 정서의 고차 위치가 정서 고유인지 일반 추상화인지(사용자 지적에 대한 직접 답)
  2. 구성주의 개념 학습 가설과 지각 우선 가설의 대립에 **학습자 수준의 제약 조건을 준다.** 노출 대조(C2)가 있어 "라벨 학습"과 "정서 이미지 노출"을 가른다. 다만 BET와 구성주의를 가르는 것은 S2와 이중 위계뿐이다
  3. 시각피질 정서 정보의 재진입 대 내재 논쟁에 **표상 내용 수준의 제약 조건을 준다**
  4. 범주 대 affect 이중 위계(Satpute & Lindquist 2019)와 CPM의 다수준 appraisal 예측을 같은 서명 절차로 시험한다
* **다른 연구와의 구분.** 결론은 "어떤 장치가 있어야 사람 뇌의 정서 초과 위계가 모델 내부 위계에서 나타나는가"다. AI 특징의 예측력 순위가 아니다.
* **결론의 범위.**
  * "뇌가 실제로 그 장치를 쓴다"는 증명이 아니라 "그 장치가 있는 학습자가 사람 뇌와 닮는다"는 충분성 증거다(evidence-level R1 + R0).
  * 정서 라벨이 규범 평정이므로 결론은 장면의 정서적 의미에 대한 것이다. 묘사된 정서를 못 가르면 그 결론에 '묘사된 정서 지각 포함'을 붙인다.

## 12. Limitations & Risks

| 위험 | 내용 | 대응 또는 명시 |
|---|---|---|
| 주 서명의 encoding 의존([AR] 치명) | 예측 뇌에서 계산하면 팔 간 차이가 적합도 프로필 차이가 된다 | **해결:** 주 서명을 모델 블록 RDM과 고정 배정으로 옮겼다. 예측 뇌는 R² 공변량과 함께 보조 |
| 배정의 불안정 | 부분 RSA의 argmax가 잡음에 흔들리거나 위계와 무관할 수 있다 | 피험자 평균 RDM, 배정 질 보고, 0.3 미만이면 주 판정을 부호, 순위 일치로 낮춤(사전 등록). NSD 배정과 팔별 재배정 강건성 판 |
| 배정 기준의 정서 독립성 | 정서 RDM을 부분 통제해도 비선형 정서 정보가 배정에 남을 수 있다 | NSD 중립 이미지 배정(강건성 판 a)과 결과 비교 |
| 비정서 통제의 신뢰도 자료 부재 | C&K와 의미 feature의 평정자 개인 자료가 없을 수 있다 | 신뢰도 비 민감도 분석. 결과에 "신뢰도 미측정" 표시 |
| 묘사된 정서 분리 실패 | F_por와 F_emo의 공선성이 높을 수 있다(empathic pain, sympathy 등) | 통제 전후 차이 보고, 기준 초과 시 '묘사된 정서 지각 포함' |
| AI 특징의 오염 | VLM이 C&K를 학습 중에 보았을 수 있다 | 프레임만 입력, 인물 가림 대조, 연구자 점검, VLM은 통제 변수에만 사용 |
| C-05 되먹임 귀속 | 끝까지 미세조정만으로도 시각층 정서 성분이 생길 수 있다 | **해결:** E-ff(매개변수 맞춤)와 E-fb-shuf. 층별 변화량(C-20) 보고 |
| 노출과 라벨의 혼입([ET]) | E 팔 성공이 정서 이미지 분포 노출 때문일 수 있다 | **해결:** E-ff-shuf(C2). 표상 손상 시 자기지도 팔로 교체(사전 등록) |
| C-06 brain-tuning 순환 | 같은 C&K 분포에서 조율, 평가하면 영역-정서 상관을 옮길 뿐이다 | **해결:** 조율은 NSD로만, 평가는 Horikawa/MC로만. B-rand, B-vis 대조 |
| NSD transmodal 신호([AR]) | 재인, 친숙도 신호 혼입과 낮은 잡음 천장 | 1주차 관문(13절). 미달이면 B 팔을 핵심 판에서 뺀다 |
| C-07 피질하 | Horikawa ROI에 pulvinar 없음, 편도체 신호 약함 | **한계로 명시하고 확장(X1)으로 뺀다** |
| C-08 재귀 단계 | CORnet-S는 재귀 단계가 적다 | **확장(X2)** |
| C-09 지형 | TDANN 학습이 무겁고 LICENSE가 없다 | **확장(X3), 분석 전용** |
| 초기 층 정렬 변화 | 학습이 V1 정렬을 낮출 수 있다(Leutenegger 2026 정정본) | 블록별 CKA 보고, 같은 해상도 평가 |
| 선점 | Ding, Keil 연구군이 재진입 쟁점을 연속으로 다룸(VCA, Leem 2026, VSS 2025) | 되먹임 팔은 E-ff 대조와 S1′ 판정으로 차별화. 선점되면 B 팔과 노출 대조가 주 기여로 남는다 |
| 작은 표본 | 11명, Horikawa 반복 없음 | MC로 확인, 피험자 간 상한, bootstrap |
| null 결과 | Conwell 2024처럼 팔 간 차이가 작을 수 있다 | 동등성 한계 사전 등록, 결과 지도(10절)에 null 해석 포함 |
| 도메인 차이 | EmoSet 정지 이미지 대 C&K 영상, NSD 정지 장면 | 모든 팔에 공통. 절대 성능은 비교하지 않는다 |
| 이용 조건 | EmoSet 이미지, torchvision 가중치, HCP-MMP 주석, Py-Feat, VLM, BLT, TDANN | 1주차 확인 목록. 확인 안 되면 대체 자료(FindingEmo 등)로 바꾼다(frontier-ai 0.4절) |
| MC 형식 | 보유본 전처리 형식 미확인 | 1주차 관문. 맞지 않으면 raw(ds005191)에서 원 논문 절차로 다시 만든다(1주 추가 위험) |
| 구현량 | 서명, 배정, 관문, 8팔을 한 사람이 하기에 무겁다([AR]) | 서명 코드는 실측과 모델에 같은 함수를 쓴다. 1주차 관문 결과에 따라 팔을 줄이는 규칙(13절) |

## 13. Pilot Experiment (1주차, GPU 거의 불필요)

**1주차의 관문 결과는 그 자체로 이 카드의 첫 결과다.** 실측 S1′, 이중 위계, appraisal 기울기, 실측 R_S2는 모델 팔과 무관하게 보고서 한 편으로 묶는다.

1. **관문 G1, 실측 서명(첫 결과).** Horikawa 5명과 MC 6명에서 S1, S1′(F_sem 주, F_ai 보조), S1-cat, S1-aff, S1-app, R_S2(주 판, 일반화 판)를 계산한다. 이를 위해 73차원 의미 feature 주성분, AI 추출 속성, 묘사된 정서 묶음, 위계 축 값, 신뢰도(또는 민감도 분석)를 먼저 만든다.
2. **관문 G2, NSD.**
   * HCP_MMP1이 NSD에 피험자 공간 atlas로 있는지 확인한다([AR]은 있다고 보았으나 이번 세션 검색으로는 공식 문서를 확인하지 못했다). 없으면 fsaverage 주석을 피험자 surface로 옮기는 표준 절차로 만든다.
   * B-tm 표적 parcel voxel의 잡음 천장을 NSD가 제공하는 ncsnr로 계산한다. ncsnr 파일의 위치와 잡음 천장 계산식은 NSD 자료 설명서에서 1주차에 확인한다(이번 세션에서는 미확인, 다른 NSD 연구들이 ncsnr 기준으로 voxel을 고른 사례만 검색 요약으로 확인).
   * 재인 혼입: 시행 단위 beta에서 반복 순서, old/new 반응, 정답 여부를 회귀로 뺀 뒤 3회 평균한다(주 판). 첫 제시 beta만 쓴 판은 강건성으로 둔다.
   * **사전 기준:** 재인 회귀 뒤 표적 voxel의 잡음 천장 중앙값이 10% 미만이거나 shared 이미지 split-half 신뢰도가 0과 다르지 않으면 B 팔 셋을 핵심 판에서 뺀다. 그러면 핵심 판은 A0, E-ff, E-ff-shuf, E-fb, E-fb-shuf 5팔이 되고 C4는 보고하지 않는다.
3. **관문 G3, 층-영역 배정 등록.** A0와 배정용 클립으로 배정표를 만들고, 배정 질을 확인한 뒤, 정서 서명을 모델에서 계산하기 전에 저장한다.
4. **관문 G4, 묘사된 정서 묶음과 오염 점검.** F_por와 F_emo의 공선성을 계산해 8.2절 6번 기준을 적용할지 미리 판단한다.
5. **관문 G5, MC 형식, 이용 조건, 중복 검사.**
6. **A0 파일럿.** A0의 모델 내부 S1′_int와 뇌 좌표 S1′_rank를 계산한다.
7. **의사결정 규칙(사전 등록):**
   * 실측 S1′_rank의 95% 구간이 두 코호트 모두에서 0을 포함하면: 첫 결과를 "정서의 transmodal 위치는 일반 추상화 위계의 일부"로 보고한다. 모델 판은 A0, E-ff, E-ff-shuf로 줄이고 S2와 이중 위계만 시험한다.
   * 실측 S1′ > 0이고 A0의 D가 이미 동등성 한계 안이면: 주 질문을 "무엇이 그 재현을 깨는가"(lesion, 자료 박탈 X4)로 옮긴다. 동등성 한계는 아직 없으므로 이 판정은 2주차 E-ff seed 변동으로 한계를 정한 뒤 확정한다.
   * 실측 S1′ > 0이고 A0이 멀면: 계획대로 2주차에 핵심 판(8팔 또는 G2 결과에 따라 5팔)을 학습한다.
   * MC 형식이 맞지 않으면 Horikawa로만 진행하고 MC 재생성을 병행한다. 이때 확인 코호트 결과는 4주 안에 나오지 않을 수 있다고 보고한다.

## 14. Feasibility & Priority

| 항목 | 자체 판단 | 근거 |
|---|---|---|
| Novelty | 3/5 | 구성 요소(Soderberg 2026, Gao 2025, ReAlnet, Chen 2025)와 판정 방식(Höfling 2026, Nakamura 2026), 층-위계 대응(Nonaka 2021, Pham 2021)에 각각 선행이 있다. 정서 초과 위계 서명, 노출 대 라벨 대조, 분포를 분리한 brain-tuning의 결합만 새롭다([AR] 재채점과 같은 판단) |
| AI-enabled Affective Neuroscience Contribution | 4/5 | 관찰로 만들 수 없는 통제 학습자를 쓰고, 결론이 정서 이론 쟁점에 닿는다. 결론 범위는 R1 + R0, 충분성 |
| Neuroscientific Importance | 4/5 | 1주차 실측 S1′만으로도 "transmodal 정서 위치가 일반 추상화를 넘는가"에 답한다 |
| 1-month Feasibility | 3/5 | 공개 가중치, 작은 모델, 새 수집 없음. 그러나 MC 형식, NSD 관문, 신뢰도 자료, 구현량 때문에 4주가 빠듯하다([AR]과 같은 판단) |
| 전체 권고 | **R1 핵심 판을 1순위 후보로 두되, 1주차 관문 결과를 먼저 독립 결과로 보고한다** | 관문이 실패해도(S1′ ≈ 0) 사용자 지적에 대한 답이 남는다. 관문을 통과하면 모델 팔이 그 위계의 기원을 묻는다 |

* **첫 결과의 위치.** 1주차 실측 S1′, 이중 위계, appraisal 기울기, 실측 R_S2는 그 자체로 정서와 뇌에 대한 결과다. 모델 학습 전에 보고서로 묶어 Coordinator에게 넘긴다.
* **4주 계획:**
  * 1주: 관문 G1~G5(13절). 첫 결과 보고서, 배정표 등록, A0 파일럿
  * 2주: 핵심 판 학습(8팔이면 21회, 5팔이면 12회), 학습 성공 확인, E-ff-shuf 교체 규칙 적용, 동등성 한계 고정
  * 3주: 모델 내부 서명, 뇌 좌표 서명, 쌍 대비, S2, 이중 위계, 층별 변화량, 보조 예측 뇌 판(R² 공변량)
  * 4주: 논쟁 클립 확인, MC 확인, 동등성 검정, 보고
  * **조건부 분기(4주차):** C2에서 E-ff가 E-ff-shuf보다 실측에 가깝고 S2가 구성주의 방향(개념 없는 팔은 환자형, E 팔은 사람 뇌 쪽)으로 나오면, X4(정서 단어 제거) 학습을 바로 이어 붙인다. Affection 이용 조건이 확인된 경우에만 하며, 4주 안에는 학습 시작과 학습 성공 확인까지만 약속한다. 그렇지 않으면 X4는 보류한다.
* **overlap:**
  * overlap: 연구실 팀원 TRIBE 작업. 뇌 반응에 맞춰 학습한 모델이라는 개념이 인접한다. 차이는 5절.
  * overlap: EmoBrain(구 EmoViS 범위). Horikawa 정서 기하의 기원을 묻는 질문과 부분 겹침. R1은 모델 조건 조작으로 접근한다. R1의 brain-tuning은 정서와 무관한 NSD로 하므로 "뇌 정서 정보를 모델 학습에 쓰는 발상"과의 겹침은 주장하지 않는다.

---

## Safeguards 점검 (CLAUDE.md 6절)

| 항목 | 상태 |
|---|---|
| 참가자가 경험한 정서 vs 자극에 묘사된 정서 | C&K 평정은 별도 평정자가 보고한 유발 정서의 집계. 묘사된 정서는 F_por로 따로 매겨 통제한다([AI-est]). 못 가르면 '묘사된 정서 지각 포함'. 주장은 장면의 정서적 의미(규범)까지 |
| 사람 주석 vs 모델 생성 주석 | 정서 라벨과 주 비정서 통제(73개 의미 개념)는 사람 주석. 보조 비정서 통제와 묘사된 정서는 AI 추정([AI-est]) |
| 본인 보고 vs 규범 평정 | 본인 보고 없음. 해석 범위 제한 |
| 정서 표상 vs 시각/의미 내용 표상 | 저수준 통계, 차원을 맞춘 의미 통제, 묘사된 정서 통제, 상호 통제(S1′). S2도 내용 회귀 뒤 계산 |
| encoding 정확도 vs 설명적 적절성 | 주 서명은 모델 블록 RDM과 고정 배정. encoding 예측 뇌는 R² 공변량과 함께 보조 |
| decodability vs 표상 vs 인과 | 모델 내 조작은 R1, 뇌 대응은 R0. 뇌의 인과 주장 없음 |
| in-silico vs 실측 | 모델 서명과 실측 서명을 같은 함수로 따로 계산해 비교 |
| shared vs dataset-specific | 두 코호트 확인, 코호트 안 분석 |
| exploratory vs confirmatory | 1주차 관문, 배정표, 쌍 대비, 동등성 한계를 사전 등록 |
| HRF와 자기상관 | 블록 평균 클립 반응(Horikawa 제공본, MC는 원 논문 4 s shift). 시간 동역학 주장 없음 |
| stimulus/movie/subject leakage | 배정용 클립과 평가용 클립 분리. MC 72 시험 클립은 잡음 천장에만. 같은 원본에서 잘린 클립은 원본 ID가 확인되면 같은 쪽에 둔다. NSD shared 이미지는 조율에서 제외 |
| 반복 자극 교란 | MC 시험 반복은 잡음 천장에만. NSD 반복과 재인 신호는 회귀자로 제거, 첫 제시 강건성 판 |
| 평정자 일치와 라벨 잡음 | split-half 신뢰도 보고, 자료가 없으면 민감도 분석. 34범주 절대값 해석 안 함 |
| 시각-의미-정서 공선성 | 상호 통제, 묘사된 정서 공선성 기준, 논쟁 클립. 가를 수 없으면 그렇게 보고 |
| 시공간 해상도 | 블록 평균, 3T와 7T 혼재. 피질하 판정 제외 |
| ROI 선택과 순환 추론 | parcel과 위계 축은 해부 parcel과 휴지기 경사로 사전 정의. 층-영역 배정은 정서 관련 RDM을 통제한 기준으로, 평가와 겹치지 않는 클립에서 정한다 |
| 다중 비교 | 주 쌍 대비 4개 Holm 보정. 보조 대비와 보조 서명은 탐색으로 표시 |
| 자료, checkpoint 이용 조건 | EmoSet, torchvision, HCP-MMP, Py-Feat, VLM, BLT, TDANN 미확인(1주차 목록) |
| 사전학습 오염 | EmoNet 미사용, VLM은 통제 변수에만 쓰고 오염 점검, 지각 해시 중복 검사 |
| 데이터셋 간 라벨 비호환 | EmoSet 8범주는 학습에만, 판정은 C&K 34범주. 매핑하지 않음. S2 주 판의 네 부정 범주 이름만 일치시킨다 |

---

## 반영하지 않은 지적

| 지적 | 출처 | 처리 | 근거 |
|---|---|---|---|
| 핵심 판을 7팔로 줄인다 | [AR] 1.1-5 | 8팔로 둔다(부분 반영) | 상호작용 두 팔은 확장으로 옮겼다. 그 자리에 [ET] 1.5-2와 수정 지시 5번이 요구한 노출 대조 E-ff-shuf를 넣었다. 수정 지시 6번의 상한(8팔 이하) 안이다 |
| 노출 대조로 EmoSet 자기지도 팔을 쓴다 | [ET] 1.5-2(대안 중 하나) | 핵심 판에는 넣지 않고 교체 규칙과 확장 X7로 둔다 | 섞은 라벨 팔은 E-ff와 손실, step 수, 출력 구조가 같아 "라벨과 이미지의 연합"만 다르다. 자기지도 팔은 목표 함수까지 바뀐다. 섞은 라벨 학습이 표상을 손상시키는 경우에만 바꾼다(7.1절) |
| 두 RDM의 split-half 신뢰도를 보고하고 보정한다 | [AR] 1.1-3, [ET] 1.5-3 | 자료가 있으면 그대로, 없으면 민감도 분석으로 대신한다(부분 반영) | Horikawa figshare에는 클립당 집계값만 있다(Stage 1 G3). 평정자 개인 자료 없이 split-half를 계산할 수 없다. 없는 값을 추정해 보정하지 않고, 신뢰도 비 가정 범위에서 결론의 부호가 유지되는지를 보고한다 |
| S2를 BET 대 구성주의의 판별 서명으로 승격한다 | [ET] 1.7-2 | 이론적 역할은 10절과 11절에 적었지만 주 판정 서명으로 올리지 않는다 | 대상(얼굴 대 장면), 수준(행동 결손 대 건강한 뇌의 신경 비율), 개념의 조작(의미 지식 대 8범주 감독 신호)의 세 간극이 내용 통제로도 다 닫히지 않는다([ET] 1.2). 주 판정은 S1′ 쌍 대비로 두고 S2는 보조 서명으로 같은 쌍 대비를 보고한다 |
| 첫 제시 beta만 쓴다 | [AR] 1.1-4(두 안 중 하나) | 주 판은 재인 회귀자 제거 뒤 3회 평균, 첫 제시 판은 강건성 | 첫 제시만 쓰면 시행 수가 3분의 1이 되어 이미 낮은 transmodal 잡음 천장이 더 낮아진다. 두 판의 B-tm 결과가 다르면 그 차이를 보고한다 |
| 비정서 비교 속성을 종합 판단 수준(LLM 비정서 종합 판단)으로 바꾼다 | [ET] 1.2, 1.5-3 | 주 통제는 인간 주석 73개 의미 개념, LLM 종합 판단은 보조 | 주 통제를 AI 추정으로 두면 정서 쪽(사람 평정)과 측정 주체가 달라진다. 수정 지시 3번도 73차원 feature를 주 통제로 정했다. 두 통제 모두에서 S1′ > 0일 때만 정서 초과로 읽는다(9절) |

---

## 검토 반영 기록

| 지적 | 출처 | 처리 | 카드 위치 |
|---|---|---|---|
| 주 서명을 모델 내부 위계로 옮기고, 정서와 무관한 기준으로 미리 고정한 층-영역 배정으로 뇌와 맞댄다. 예측 뇌는 보조로 내리고 R²를 공변량으로 | [AR] 1.1-1, 수정 지시 1번 | 반영 | 머리 요약, 용어 표, 2절 마지막 항목, 8.3절 1~7번, 9절, 12절 첫 행, Safeguards |
| Höfling 2026, Nakamura 2026을 방법 선행으로 인용 | [AR] 1.1-1, 1.2, 1.4 | 반영(arXiv로 확인). 층-위계 대응 선행 Nonaka 2021, Pham 2021도 추가 | 2절, 4.1절, 4.2절 신규 행, 5절, 14절 |
| "실측 95% 구간 안" 규칙을 버리고 사전 등록 쌍 대비의 거리 차이로 판정. 척도는 순위나 잡음 천장으로 | [AR] 1.1-2, 수정 지시 2번 | 반영. 노출 대조 C2를 더해 주 대비 4개 | 8.4절 |
| 비정서 통제를 추상 수준, 차원, 신뢰도에서 맞춤(73차원 주성분 34개 주 통제, AI 속성 보조, split-half 신뢰도) | [AR] 1.1-3, [ET] 1.2, 1.5-3, 수정 지시 3번 | 반영(신뢰도는 자료 유무에 따라 민감도 분석, '반영하지 않은 지적' 참조) | 용어 표, 6절, 8.1절, 9절 |
| R2의 비정서 방향과 맞춤 | [AR] 1.1-3, 수정 지시 3번 | 반영(같은 feature, 주성분 절차는 1주차에 R2와 맞춤) | 6절 비정서 통제(주) 행 |
| S2를 내용 통제 위에서 계산(내용 회귀 뒤 crossnobis, 내용이 가까운 클립 쌍) | [ET] 1.5-1, 수정 지시 4번 | 반영 | 8.2절 7번 |
| S2 주 판을 anger, disgust, fear, sadness로 한정, 나머지는 일반화 판 | [ET] 1.2, 1.6-2, 수정 지시 4번 | 반영 | 용어 표, 8.2절 7번 |
| S2의 표적을 "개념 유무 팔 사이 차이의 방향"으로 | [AR] 1.2, [ET] 1.2 간극 2, 1.6-3 | 반영 | 용어 표, 8.2절 7번, 10절 |
| 정서 이미지 노출과 라벨 학습을 가르는 팔 | [ET] 1.5-2, 수정 지시 5번 | 반영(E-ff-shuf, 교체 규칙, X7) | 7.1절, 7.2절, 8.4절 C2, 10절 |
| 상호작용 두 팔을 확장으로, 핵심 판 8팔 이하, 남긴 이유 | [AR] 1.1-5, [ET] 1.5-2, 수정 지시 6번 | 반영(8팔) | 7.1절 "무엇을 남기고 왜 남겼나", 7.2절 X6 |
| NSD 관문(ncsnr, 재인 반응, HCP_MMP1, 미달 시 B 팔 제외) | [AR] 1.1-4, 수정 지시 7번 | 반영 | 6절 NSD 행, 7.1절 출력과 손실, 13절 G2, 12절 |
| 1절 질문을 조건문으로 | [AR] 1.1-6, [ET] 1.3(41줄), 수정 지시 8번 | 반영 | 1절 |
| 1주차 실측 S1′ 관문이 그 자체로 첫 결과 | [AR] 1.7, 수정 지시 8번 | 반영 | 머리 요약, 1절, 11절, 13절 첫 문단과 G1, 14절 |
| 10절 이론 열 수정, 행마다 반대 예측 이론과 [양립] 표시 | [ET] 1.1, 1.5-4, 공통 2, 수정 지시 9번, 0절 2번 | 반영 | 10절 |
| "구성주의 개념 학습 가설과 정합"을 고침 | [ET] 1.3(252줄), 수정 지시 9번 | 반영(지시된 문안 사용) | 10절 C1, C2 행 |
| S1을 범주 기울기와 valence, arousal 기울기로 나눔 | [ET] 1.2, 1.7-1, 수정 지시 9번 | 반영(S1-cat 대 S1-aff) | 용어 표, 2절, 8.2절 5번, 10절, 11절 |
| 묘사된 정서 묶음을 통제로(공개 표정 모델, VLM, [AI-est], 오염 점검, 못 가르면 명시) | [ET] 공통 1, 1.4, 1.6-1, 수정 지시 0절 1번 | 반영 | 용어 표, 1절, 6절 신규 행, 8.2절 6번, 9절, 10절 머리, 13절 G4, Safeguards |
| 라벨 상한: 제목 "다루는 방식" | [ET] 1.3(1줄), 0절 3번 | 반영("정서적 의미가 놓이는 방식") | 제목 |
| 라벨 상한: "정서 고유 정보"의 정의 | [ET] 1.3(27, 195, 209줄), 0절 3번 | 반영(규범 평정 기준, 묘사된 정서 통제 후로 정의) | 용어 표 |
| 라벨 상한: "시각 밖 요인이 필요하다" | [ET] 1.3(256줄), 0절 3번 | 반영("시험한 장치로는 부족하다. 무엇이 필요한지는 이 결과로 말할 수 없다") | 10절 "어느 팔도" 행 |
| 라벨 상한: "학습자 수준의 판정을 준다" | [ET] 1.3(263~264줄), 0절 3번 | 반영("제약 조건을 준다") | 11절 |
| 겹침 표기를 "EmoBrain(구 EmoViS 범위)"로 통일, brain-tuning 겹침 주장 삭제 | [AR] 1.6, 0절 4번 | 반영 | 14절 overlap |
| CPM 다수준 appraisal 연결 | [ET] 공통 3, 1.7-3, 0절 5번 | 반영(S1-app) | 용어 표, 8.2절 5번, 10절, 11절 |
| 위계 기울기를 parcel 단위로, 묶음은 보고용 | [AR] 1.2 | 반영 | 7.1절 위계 축, 8.2절 4번 |
| E 팔 미세조정이 초기 시각 정렬을 낮출 수 있음(Leutenegger 2026, 정정본) | [AR] 1.2 | 반영(정정 내용과 후속 해상도 분석까지 적고, 블록별 CKA와 같은 해상도 평가로 대응) | 4.1절, 7.1절 입력, 8.3절 6번, 9절, 12절 |
| Leem 2026 지름길 주장의 본문 위치 | [AR] 1.2, 1.5 | 반영(본문 Discussion 2단락, Supplementary Fig. S2, Appendix B.1을 저장된 본문에서 다시 확인) | 4.1절, 7.2절 X1 |
| Tugsbayar 2026 서술을 "시청각 통합"으로 | [AR] 1.2 | 반영 | 4.1절, 4.2절 |
| X4(정서 단어 제거)를 4주 계획의 조건부 분기로 | [ET] 1.6-4 | 반영 | 7.2절 X4, 14절 4주 계획 |
| S2를 BET 대 구성주의 판별 서명으로 승격 | [ET] 1.7-2 | 부분 반영(이론 역할만, 주 판정 아님) | 10절, 11절, '반영하지 않은 지적' |
| 재채점(Novelty 3, 1-month 3) | [AR] 1.8 | 반영 | 14절 |
| 묘사된 정서 통제와 경험 대 묘사 구분 | [ET] 1.4 | 반영 | Safeguards 첫 행 |
