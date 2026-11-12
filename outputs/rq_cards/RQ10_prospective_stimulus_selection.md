# RQ-10. 정서 모델이 미리 고른 영상은 처음 보는 사람의 뇌에서도 그 영역을 움직일까?

* 작성: encoding-foundation (기원 EF-P6, 공동 FA-P2)
* 기준일: 2026-11-12
* 조합 ID: LIT-30 (`outputs/combinations/matrix.csv`), 군집 K2
* 선행 감사 판정: **partially, 남는 새 부분이 작음** (`outputs/evaluation/prior_overlap_audit.md` RQ-10 절)
* 읽고 반영한 자료: `reference/protocols.md` P7, `outputs/evaluation/selection.md`, `outputs/rq_landscape.md` 4절(RQ-10, RQ-51 블록과 용어 풀이), matrix.csv LIT-30 행, `outputs/evaluation/prior_overlap_audit.md`, `outputs/evaluation/reviewer_notes.md`(RQ-10 행, 4.3절, 4.4절), `outputs/discussion_record.md`, `outputs/discussion/round3_summary.md`, `outputs/agents/adversarial-reviewer/round2.md` 1.2절(EF-P6 응답), `outputs/agents/frontier-ai/round2.md` FA-P2, `outputs/stage1/dataset_Horikawa.md`, `outputs/stage1/horikawa_factcheck_stage4.md`, `outputs/STAGE_STATUS.md` "사용자 답변, Stage 3 이후" 표, Mind captioning 원문 Methods(PMC 전문, PubMed 도구)

---

## 1. Core Research Question

* **(a) 한 줄 질문:** 정서 모델이 "이 영상이 이 뇌 영역을 움직일 것"이라고 미리 고르면, 처음 보는 사람에게서도 맞을까? 그리고 그 선택은 장면 내용만 보는 모델의 선택보다 더 잘 맞을까?
* **(b) 검증 가능한 세부 질문:** Horikawa 2020 피험자 일부와 클립 일부로만 학습한 정서 encoder와 시각-의미 encoder가 정서 관련 영역(amygdala, 앞쪽 insula, vmPFC/OFC, TPJ)에 대해 서로 다른 클립을 "가장 강하게 움직일 것"으로 고를 때(controversial 클립), 선택 목록과 분석 코드를 봉인한 뒤 측정한 학습 미사용 Horikawa 피험자와 Mind captioning 6명의 실제 반응은 어느 encoder의 선택을 따르는가?

---

## 2. Scientific Motivation

**왜 중요한가.**
* Horikawa 2020은 정서 평정 모델이 시각 객체 모델과 의미 모델보다 여러 transmodal 영역을 더 잘 설명한다고 보고했다(doi:10.1016/j.isci.2020.101060).
* 하지만 이 비교는 세 모델을 따로 맞춘 뒤 성능을 비교한 것이다. 의미 공변량에 측정 오차가 있으면 정서 고유 기여가 실제보다 크게 보일 수 있다(doi:10.1371/journal.pone.0152719).
* 또 구조가 크게 다른 모델들도 자연 자극 전체에 대한 예측력은 거의 같게 나온다. 그래서 전체 예측 정확도만으로는 어느 모델이 맞는지 가리기 어렵다(doi:10.1038/s41467-024-53147-y Discussion, arXiv:2302.06677).

**어떤 공백이 있는가.**
* 두 모델이 **서로 다른 예측을 하는 자극**을 골라 보는 것(controversial stimuli, doi:10.1073/pnas.1912334117)이 모델을 가리는 가장 강한 방법이다. 정서 영역에서 정서 모델과 시각-의미 모델을 이렇게 맞붙인 연구는 감사 범위에서 없었다.
* "모델이 고른 자극이 새 사람에게서 실제로 그 영역을 움직이는가"라는 전향 검증은 언어망(Tuckute 2024), 범주 선택 영역(Ratan Murty 2021), amygdala 생성 이미지(NeuroVolve)에서 이미 새 fMRI로 수행되었다. 이 부분은 새롭지 않다.
* 남는 공백은 하나다. 같은 자극을 본 두 독립 코호트(Horikawa 2020 5명, Mind captioning 6명)가 있으므로, 새 촬영 없이 "정서 모델 대 시각-의미 모델의 controversial 선택"을 코호트를 건너 시험할 수 있다.

---

## 3. Origin of the Idea

* **조합 ID:** LIT-30 (문헌 경로).
* **결합된 결과:**
  * encoding-foundation EF-P6(Round 2): 독립 코호트를 쓴 의사 전향 검증과 provenance 등록부.
  * adversarial-reviewer의 EF-P6 응답(Round 2, 1.2절): 클립도 보류해야 "모델 검증"이 되므로 D6a(모델 검증)와 D6b(코호트 간 재현)로 나눌 것. 분석자 노출 때문에 "선택이 먼저라 순환이 없다"는 전제를 부분 반박.
  * frontier-ai FA-P2(Round 2): 생성 대신 기존 자극 풀에서 선택, 모델 내부 정서 vector와 인간 중립 캡션 embedding으로 대비 쌍 선택.
  * adversarial-reviewer Round 1 D6(의사 전향 검증), encoding-foundation Round 1 I2와 I6(controversial selection, 고처리량 선택성 검정).
* **가져온 분야:**
  * 시각과 언어 NeuroAI의 neural control과 controversial stimuli(Golan 2020, Ratan Murty 2021, Tuckute 2024, Gifford 2025).
  * 메타과학의 분석 유연성(forking paths)과 사전 등록(Botvinik-Nezer 2020, Simonsohn 2020).
  * ML 평가의 누수(leakage) 분류(Kapoor & Narayanan 2023).

---

## 4. Prior Literature

읽은 수준 표기: [본문-직접]은 본 에이전트가 본문을 읽음, [DB-본문]은 다른 에이전트가 본문을 읽은 DB 기록을 사용함, [DB-초록]은 DB에 초록 수준으로 기록됨.

| # | 논문 | ID | 읽은 수준 | 이 질문에 대한 기여 |
|---|---|---|---|---|
| 1 | Tuckute et al. (2024) Driving and suppressing the human language network using large language models | doi:10.1038/s41562-023-01783-7 | [본문-직접] bioRxiv 판(PMC10120732)의 Results와 Discussion 첫 단락 | **가장 가까운 선행.** 5명 x 1,000문장으로 학습한 GPT2-XL encoder가 고른 구동/억제 문장이 새 문장, 새 참가자 3명에서 실제로 언어망 반응을 높이고 낮췄다. 같은 논리를 새 fMRI로 검증했다 |
| 2 | Ratan Murty et al. (2021) Computational models of category-selective brain regions enable high-throughput tests of selectivity | doi:10.1038/s41467-021-25409-6 | [본문-직접] | **가장 가까운 선행.** FFA, PPA, EBA 모델로 수백만 이미지를 걸러 고반응 예측 이미지가 모두 선호 범주인지 시험했다. 맥락으로 정의되는 자극에서는 예측이 약하다고 한계를 적었다 |
| 3 | Chen et al. (2025) NeuroVolve | arXiv:2512.00557 | [DB-본문] | amygdala 최대화 생성 이미지를 새 참가자 fMRI로 검증했다. 생성 High는 Natural Zero보다 높았지만 Natural High보다 높지 않았고, 최대화 이미지는 표정이 강한 얼굴이었다(정서와 의미 범주가 분리되지 않음) |
| 4 | Golan, Raju, Kriegeskorte (2020) Controversial stimuli | doi:10.1073/pnas.1912334117 | [DB-본문] | 두 모델이 다르게 예측하는 자극에서는 적어도 하나가 틀리므로 강한 판별 검정이 된다. 이 카드의 주 산출물 논리 |
| 5 | Conwell et al. (2024) Inductive biases shaping high-level visual representation | doi:10.1038/s41467-024-53147-y | [본문-직접] | 넓게 표집한 자연 자극에서는 거의 모든 모델이 비슷한 예측력을 보인다. Discussion이 기존 데이터에서 모델 차이를 드러내는 하위집합을 고르는 "controversial selection"을 제안했다 |
| 6 | Gifford et al. (2025) In silico discovery of representational relationships across visual cortex | doi:10.1038/s41562-025-02252-z | [본문-직접] | in-silico 탐색과 독립 피험자 in vivo 검증을 닫힌 고리로 묶었다. 한계로 encoder 예측이 분포 밖에서 불완전하다고 적었다 |
| 7 | Horikawa et al. (2020) | doi:10.1016/j.isci.2020.101060 | [본문-직접] | 선택 단계의 학습 데이터. 정서 모델 우위 보고, 라벨은 별도 평정자 규범(Limitations 1단락), 반복 없음(Discussion 6단락) |
| 8 | Horikawa (2025) Mind captioning | doi:10.1126/sciadv.adw1464 | [본문-직접] Methods와 Discussion 해당 단락 | 검증 코호트. 같은 클립, 6명, 학습 세션 2,180개 클립은 6명 모두 같은 순서, 테스트 72개 x 5회, 10 s 미만 클립 반복 재생, 평가 블록 무작위 삽입 |
| 9 | Mohammed, Gu, Fang (2026) EmoMind | arXiv:2605.16739 | [본문-직접] | Mind captioning 6명으로 34차원 정서 벡터를 decoding했고 Horikawa 2020은 교차 데이터셋 평가에만 썼다. **분석자 노출의 출처**: 이 코호트의 정서 관련 반응이 이미 분석, 공개되었다 |
| 10 | Jang & Kragel (2025) Understanding Human Amygdala Function with Artificial Neural Networks | doi:10.1523/JNEUROSCI.1436-24.2025 | [본문-직접] | amygdala 하위영역 encoding과 합성 자극. 생체 검증은 보고하지 않았고, 다른 자극으로 일반화 검사가 필요하다고 적었다(Discussion 8단락) |
| 11 | Gu et al. (2023) Human brain responses are modulated when exposed to optimized natural images or synthetically generated images | doi:10.1038/s42003-023-05440-7 | [DB-본문] | 실제 조절 효과 크기가 encoder 정확도에 비례한다. 예측력이 낮은 정서 영역에서는 선택 성공률도 낮을 것이라는 예측 근거 |
| 12 | Schütt et al. (2023) Statistical inference on representational geometries; Ince et al. (2021) Bayesian inference of population prevalence | doi:10.7554/eLife.82566; doi:10.7554/eLife.62461 | [DB-본문] | 피험자와 클립을 함께 일반화하는 2-factor bootstrap, 소수 피험자에서의 prevalence 추론 |
| 13 | Botvinik-Nezer et al. (2020); Kapoor & Narayanan (2023) | doi:10.1038/s41586-020-2314-9; doi:10.1016/j.patter.2023.100804 | [DB-본문] | 분석 경로 유연성과 누수 경로 분류. 봉인 절차의 근거 |
| 14 | d'Ascoli et al. (2026) TRIBE v2 | arXiv:2605.04326 | [본문-직접] | zero-shot 선택 팔(arm)의 모델. 공개 checkpoint는 피질 평균 피험자 예측만 낸다. 무음 짧은 클립 시퀀스는 학습 분포 밖이다 |
| 15 | Kragel et al. (2019) EmoNet | doi:10.1126/sciadv.aaw4358 | [본문-직접] | Cowen & Keltner 비디오 프레임으로 학습되었으므로 이 카드에서 **사용 금지**(학습-평가 누수) |

---

## 5. Novelty

* **이미 수행된 부분(새로움으로 주장하지 않음):**
  * encoder가 고른 자극이 새 사람에게서 그 영역을 구동하거나 억제하는지 보는 전향 검증. 언어망(Tuckute 2024), 범주 영역(Ratan Murty 2021), amygdala 생성 자극(NeuroVolve)에서 새 fMRI로 이미 수행되었다.
  * 단순 구동/억제 성공률은 보조 결과로만 보고한다.
* **남는 새 부분(감사 판정의 범위):**
  * **정서 encoder 대 시각-의미 encoder의 controversial 선택을, 정서 관련 영역에서, 코호트를 건너 시험한다.** 두 모델이 서로 다른 클립을 고를 때 실제 반응이 어느 쪽을 따르는지가 주 산출물 하나다.
* **가장 가까운 선행과의 차이:**
  * Tuckute 2024: 한 모델의 구동/억제 선택. 영역은 언어망, 검증은 새 fMRI.
  * 이 카드: 두 모델의 경쟁. 영역은 정서 관련 영역, 검증은 이미 수집된 독립 코호트다.
* **이 카드가 Tuckute 2024보다 약한 점(명시):**
  * 검증 데이터가 새로 수집된 것이 아니라 이미 전처리된 자료다. 그래서 분석자 노출을 봉인 절차로 막아야 한다(8.5절).
  * 증거 수준도 R3가 아니라 사전 등록된 R0다(Safeguards 점검 참조).

---

## 6. Proposed Dataset

| 필요한 것 | 있는가 | 근거와 주의 |
|---|---|---|
| Horikawa 2020 fMRI (선택용 학습) | **있음.** 5명, 61 run, TR 2 s, 2 mm, TE 43 ms. Raw BIDS(CC0)와 블록 평균 전처리본(native volume, HCP360 360개 + 피질하 10개 ROI) | `dataset_Horikawa.md` G2와 2.2절. 5명 모두 **같은 자극 순서**. 내용 중복 15개 label index |
| Horikawa 2020 클립 원본 | **있음(사용자 보유).** 2,185개 모두 무음 | `STAGE_STATUS.md` 25(b). 클립 원래 길이와 반복 재생 횟수는 events.tsv에 없으므로 영상 파일에서 계산한다 |
| 규범 정서 평정 34범주 + 14차원 | **있음.** 별도 평정자(MTurk) 평균 | `dataset_Horikawa.md` G3. fMRI 참가자 본인 보고는 **없음** |
| Mind captioning fMRI (검증용) | **있음(사용자 보유, 전처리 완료).** 6명, TR 1 s, 2 mm, TE 30 ms, MB6, 3T Prisma | Mind captioning Methods. 보유 전처리본의 공간(native/표준)과 형식은 **미확인** |
| Mind captioning 학습 세션 반응 | **있음.** 2,180개 고유 클립 각 1회, **6명 모두 같은 pseudorandom 순서** | Methods. 코호트 안 피험자들은 순서 효과를 공유한다 |
| Mind captioning 테스트 반응 | **있음.** 72개 클립 x 5회, run 안 pseudorandom | Methods. 이 72개는 학습 세션 마지막 두 run에서도 1회 제시되어 **총 6회 노출**이다 |
| Mind captioning 클립 블록 구조 | **있음.** 10 s 미만 클립은 10 s가 넘도록 반복 재생, 블록 뒤 2 s 휴지, run마다 평가 블록 3~4개 무작위 삽입 | Methods, `reviewer_notes.md` 4.4절. Horikawa 2020은 8 s 미만 클립을 8 s가 넘도록 반복 재생했다(`dataset_Horikawa.md` 2절). 같은 클립이라도 두 코호트의 반복 재생 횟수가 다를 수 있다 |
| 인간 중립 캡션(정서 배제) | **있음(사용자 보유).** 클립당 20개 | `STAGE_STATUS.md` 25(a). 시각-의미 encoder의 의미 feature로 쓴다 |
| 두 코호트 피험자 비중복 | **사용자 확인. 원문에는 언급 없음** | `horikawa_factcheck_stage4.md` 3절 |
| 두 코호트 클립 ID 대응표 | **미확인.** 두 연구 모두 2,196개 제시 ID지만 중복 제외 수가 다르다(15개 대 16개) | 영상 파일 해시나 embedding 일치로 대응표를 만든다(0단계) |
| 두 코호트 학습 순서가 서로 다른지 | **미확인** | events 파일을 대조한다. 다르면 코호트 간 순서 효과가 독립이다 |
| 참가자 본인 정서 보고, 생리, 시선 | **없음**(두 코호트 모두) | 자유 시청이라 시선 교란이 남는다(`rq_landscape.md` 1절 5번) |
| 피질하 신호 품질 | **미확인.** Horikawa TE 43 ms는 amygdala에 불리하다 | Mind captioning 반복으로 영역별 신뢰도를 먼저 잰다(8.1절) |

* 쓰지 않는 데이터: Emo-FilM, Spacetop, NSD. 다른 자극이라 같은 클립의 코호트 간 검증이 성립하지 않는다. 확장 단계(12절)에서만 고려한다.

---

## 7. Proposed Computational Framework

### Pretrained model
공개 모델을 먼저 쓴다. 정서 encoder와 시각-의미 encoder는 이 feature 위에 선형 회귀(ridge)만 학습한다.
* **V-JEPA 2** (arXiv:2506.09985): 영상 feature. 코드 라이선스 MIT(frontier-ai 확인), 가중치는 CC-BY-NC 4.0으로 기재한 출처가 있다(arXiv:2605.29850 표 3). 본 에이전트는 가중치 라이선스를 직접 확인하지 못했다(**미확인**).
* **문장 embedding 모델**: 인간 중립 캡션 embedding용. 허용 라이선스 공개 모델 중에서 사전 등록 때 하나를 고정한다(후보와 라이선스 **미확인**).
* **TRIBE v2** (arXiv:2605.04326): zero-shot 선택 팔. CC BY-NC 4.0(저장소 LICENSE 확인), 가중치는 Hugging Face(README 링크, 직접 열람 못함). 연구 목적 사용은 가능하다.
* **선택 팔(보조, FA-P2):** 공개 가중치 VLM의 내부 정서 vector 투영. 모델 선택과 라이선스는 **미확인**이며 AI 추정으로 표기한다.
* **사용 금지:** EmoNet(Cowen & Keltner 프레임으로 학습, doi:10.1126/sciadv.aaw4358).
* **계산 자원:** **미확인.** 가정은 GPU 1~4장이다. V-JEPA 2 feature 추출(약 2,180개 짧은 클립)과 TRIBE v2 추론은 GPU 수 시간 규모로 추정하고, ridge와 통계는 CPU로 충분하다고 추정한다.

### Input representation
* **정서 encoder(E):** 클립별 규범 정서 평정 48차원(34범주 선택 비율 + 14차원 평균).
* **시각-의미 encoder(V):**
  * V-JEPA 2 embedding(클립 프레임 평균, 층은 학습 fold 안에서 선택)
  * 인간 중립 캡션 20개의 문장 embedding 평균
  * 저수준 feature: 움직임 에너지, 밝기, 대비
  * 차원은 PCA로 줄인다. 차원 수는 E와 맞추지 않고, 학습 fold 안 교차검증 정확도로 맞춘다(아래 "matched-complexity").
* **TRIBE v2 팔(T):** 무음 영상만 입력한다. 실험의 클립 반복 재생과 블록 구조를 그대로 재현한 시퀀스를 넣는다.
* **nuisance 공변량(모든 팔):** 클립 원래 길이, 코호트별 반복 재생 횟수, 블록 길이, run 안 위치(시작 후 시간), 직전 블록이 평가 블록인지(Mind captioning만).

### Output / target representation
* 영역별 블록 반응이다. HCP360 parcel 평균과 피질하 ROI 평균을 쓴다.
* 블록 반응은 Horikawa 2020 방식(4 s 이동 후 블록 평균, run 안 z-score)으로 두 코호트에서 똑같이 다시 계산한다.
* 사전 지정 표적 영역(해부학 기준, Horikawa 결과로 고르지 않음):
  * amygdala
  * 앞쪽 insula(HCP360 AAIC, AVI)
  * vmPFC/OFC(10r, 10v, 25, s32, OFC, pOFC)
  * TPJ/IPL(PGi, PGs, TPOJ1)
  * 양성 대조 시각 영역(V1, FFC, PHA1): 여기서는 V가 이겨야 정상이다.

### Training or adaptation strategy
* **D6a 모델 검증(주 분석):**
  * 클립을 5-fold로 나눈다. 같은 원본에서 나온 것으로 의심되는 클립(embedding 유사도 기준)과 내용 중복 쌍은 같은 fold에 둔다.
  * fold마다 나머지 4개 fold 클립으로만 E, V를 학습하고, 보류 fold 클립 안에서만 선택한다(cross-fitting).
  * 피험자는 Horikawa 4명으로 학습하고 1명을 보류한다(5회 순환).
  * 검증은 보류 Horikawa 피험자와 Mind captioning 6명으로 한다.
  * 결과적으로 모든 선택 클립은 "그 선택을 한 모델이 학습에서 본 적 없는 클립"이다.
* **D6b 코호트 간 재현(보조):**
  * Horikawa 5명의 실제 관찰 반응 평균으로 영역별 상위/하위 클립을 고르고, Mind captioning에서 검증한다.
  * 모델이 아니라 "정서 영역을 움직이는 클립"의 코호트 간 재현성을 본다.
  * 결과는 D6a 선택 성공률의 **경험적 상한**으로 쓴다.
* **TRIBE v2 팔:** 학습하지 않는다(zero-shot). 선택은 Horikawa와 Mind captioning 모든 피험자에게 검증할 수 있다. 단 **RQ-51 관문**(in-silico 충실도 지도)을 통과한 피질 parcel에서만 쓴다. 무음 짧은 클립 시퀀스는 TRIBE v2 학습 분포(연속 영화, 소리 있는 3 s 클립, 무음 연속 영상) 밖이고, 공개 checkpoint는 피질만 예측하므로 amygdala에는 쓰지 않는다.
* **matched-complexity:** E와 V의 학습 fold 안 교차검증 정확도를 보고한다. V를 더 크게 만든 판(층 추가, 차원 증가)과 E+V 결합 판도 함께 둔다.

### Relevant brain regions / networks
* 정서 관련: amygdala, 앞쪽 insula, vmPFC/OFC, TPJ/IPL. Horikawa 2020의 transmodal 쪽 결과와 겹치는 망(DMN 일부, salience)에 해당한다.
* 대조: V1, FFC, PHA1.
* signal-feasibility: Mind captioning 72개 반복의 영역별 반복 간 신뢰도가 사전 하한(예: split-half r 0.1 이상, 사전 등록 때 확정)보다 낮은 영역은 확증 분석에서 뺀다.

### Loss function or statistical objective
* 학습: 영역별 ridge 회귀. 목적은 평균제곱오차이고, 정규화 강도는 학습 fold 안 교차검증으로 고른다.
* **주 통계량 Δ_r(controversial 승패):**
  * 영역 r마다 보류 클립에서 "E 상위 q%이면서 V 중앙값 이하" 집합(E 단독 선택)과 "V 상위 q%이면서 E 중앙값 이하" 집합(V 단독 선택)을 만든다.
  * 두 집합은 클립 길이와 반복 재생 횟수 구간으로 짝을 맞춘다.
  * Δ_r = (E 단독 선택 클립의 관찰 반응 평균) - (V 단독 선택 클립의 관찰 반응 평균). 단위는 z이고, 피험자별로 계산한다.
* 검정:
  * 피험자별로 E/V 표지를 짝 안에서 섞는 순열 검정을 한다.
  * 6명(Mind captioning)에 대한 Bayesian prevalence를 낸다(doi:10.7554/eLife.62461).
  * 피험자와 클립을 함께 일반화하는 2-factor bootstrap 신뢰구간을 낸다(doi:10.7554/eLife.82566).
  * 영역 수에 대해 Holm 보정을 한다.
  * 귀무를 주장할 때는 사전 지정 SESOI(가장 작은 의미 있는 효과)로 동등성 검정을 한다.

### Interpretability method
* controversial 클립 목록 자체를 공개한다. 영역별로 E가 고르고 V가 고르지 않은 클립과 그 반대 클립의 캡션, 규범 정서 profile, 저수준 속성 분포를 나란히 보여 준다.
* 영역 x 선택 표적 특이성 행렬을 만든다. vmPFC용으로 고른 클립이 insula보다 vmPFC를 더 움직이는지 본다.
* E가 고른 클립의 정서 범주 분포가 한두 범주(예: 공포, 혐오)에 몰리는지 확인한다(범주 군집 효과, doi:10.1016/j.neunet.2025.107515).

---

## 8. Proposed Analyses

### 8.0 0단계 (봉인 전, Mind captioning 반응을 보지 않고 할 일)
1. 두 코호트 클립 ID 대응표를 만든다(영상 파일 해시, embedding 일치).
2. 두 코호트 학습 순서를 대조한다(events 파일).
3. 클립 원래 길이와 코호트별 반복 재생 횟수를 계산한다.
4. 표적 영역 정의를 고정한다(HCP360 parcel, 피질하 ROI). Mind captioning의 HCP360 투영 절차도 고정한다.
5. **RQ-51 관문 결과를 가져온다.** TRIBE 팔을 쓸 parcel 목록을 정한다.

### 8.1 signal-feasibility 점검
* Mind captioning 72개 반복 클립으로 영역별 반복 간 신뢰도를 계산한다. 이것은 클립 정체와 무관한 품질 지표이므로 봉인 전에 계산해도 선택에 정보가 새지 않는다. 다만 반복 클립의 정서 내용별 신뢰도는 보지 않는다.
* 정서 수준별 신뢰도는 봉인 뒤 결과 표에만 함께 보고한다.

### 8.2 D6a 모델 검증 (주 분석)
* 5-fold 클립 cross-fitting과 Horikawa 피험자 1명 보류 순환으로 E, V, (T), (VLM 팔) 선택 목록을 만든다.
* **주 산출물:** 영역별 Δ_r. 정서 영역에서 Δ_r > 0, 시각 대조 영역에서 Δ_r < 0을 예측한다.
* **보조 산출물:** 모델별 구동 대 억제 선택 차이(Tuckute식 성공률)를 무작위 클립 기준선과 비교한다. 선행이 있으므로 보조로만 보고한다.

### 8.3 D6b 코호트 간 재현 (보조)
* Horikawa 관찰 반응으로 고른 영역별 상위/하위 클립을 Mind captioning에서 검증한다.
* D6a 선택의 성공률을 D6b 성공률(경험적 상한)과 무작위 선택(하한) 사이에 놓고 보고한다.

### 8.4 비교 조건, baseline, ablation
* baseline:
  * 무작위 클립 선택(seed 봉인)
  * 저수준 feature만 쓴 선택기
  * E+V 결합 선택기
* ablation:
  * V에서 캡션 embedding 제거(영상 feature만)
  * V에서 V-JEPA 2 제거(캡션만)
  * E에서 14차원만 또는 34범주만 사용
* 72개 테스트 클립(6회 노출)은 선택 풀에서 빼고 신뢰도 계산에만 쓴다. 학습 세션 반응(1회 노출)만 검증에 쓰므로 Horikawa의 1회 노출과 조건이 맞다.

### 8.5 분석자 노출 차단과 봉인 절차 (필수)
**배경.**
* 사용자가 Mind captioning을 이미 전처리했다.
* EmoMind(arXiv:2605.16739)가 같은 코호트의 정서 decoding 결과를 공개했다.
* 이 프로젝트의 다른 Pilot(P1 RQ-08, P2 RQ-01)도 Mind captioning 반응을 분석할 예정이다(`selection.md` 6절).
* 봉인이 없으면 이 질문은 R0 상관 분석과 다르지 않다(`reviewer_notes.md` 4.3절).

**절차.**
1. **노출 기록부 작성(봉인 전).**
   * Mind captioning의 영역 수준 반응이나 그 분석 결과를 본 사람을 모두 적는다. 날짜, 본 내용, 본 영역을 적는다.
   * 사용자(전처리 수행), EmoMind 공개 결과를 읽은 사람, P1/P2 담당자를 포함한다.
   * 선택 목록을 만드는 분석자는 Mind captioning의 영역 반응을 본 적이 없어야 한다. 이미 본 사람만 있으면 D6a/D6b의 Mind captioning 검증을 "탐색적 재현"으로 낮춰 표기한다.
2. **금지 입력 목록.**
   * 선택 단계에서 Mind captioning 반응, EmoMind의 decoding 결과나 그림, 그리고 P1/P2의 Mind captioning 결과를 쓰지 않는다.
   * 선택은 Horikawa 2020 데이터, 규범 평정, 캡션, 영상 feature만으로 한다.
3. **봉인 대상 파일.**
   * `rq10_selection.csv`(영역, 선택기, 방향, fold, clip_id, 예측값)
   * `rq10_analysis.py`(Mind captioning 반응을 읽어 사전 등록 통계만 출력하는 검증 스크립트)
   * `rq10_config.yaml`(영역 정의, nuisance, q%, SESOI, 신뢰도 하한, 통계 검정, 다중비교)
   * 환경 고정 파일(패키지 버전)
   * 무작위 기준선 seed
4. **해시와 시점.**
   * 각 파일의 SHA-256 해시와 git commit 해시를 manifest 하나에 모은다.
   * manifest(해시만, 데이터 없음)를 외부 시점 기록이 남는 곳에 올린다. 예: OSF 사전 등록(비공개 embargo), Zenodo 기록, 또는 공개 timestamp 서비스.
   * 같은 manifest를 분석에 관여하지 않는 사람(Coordinator 또는 연구실 동료)에게도 보내 보관하게 한다.
5. **실행 순서 고정.**
   * RQ-10 봉인은 P1, P2가 Mind captioning의 정서 관련 영역 반응을 분석하기 **전에** 끝낸다.
   * 순서를 지킬 수 없으면 RQ-10 선택 분석자를 P1/P2와 분리한다(정보 차단).
6. **검증 실행.**
   * 검증 스크립트는 시작할 때 manifest 해시와 대조한다. 불일치하면 멈춘다.
   * 출력은 사전 등록 통계로만 제한한다. 사후 분석은 별도 파일에 "탐색"으로 표시한다.
7. **변경 기록.** 봉인 뒤 바꾼 모든 것을 날짜와 이유와 함께 `deviations.md`에 적고 결과 보고에 첨부한다.

### 8.6 통계와 검증 전략 요약
* 일반화 수준:
  * D6a: Horikawa 보류 피험자에 대해서는 새 클립 + 새 피험자(같은 코호트), Mind captioning에 대해서는 새 클립 + 새 피험자 + 새 코호트(scanner, TR, 블록 구조 다름).
  * D6b: 새 코호트에서 같은 클립.
* 피험자 일반화는 prevalence, 클립 일반화는 bootstrap으로 추론한다.
* Mind captioning 6명은 같은 순서를 공유하므로, 코호트 안 순서 효과를 피험자 간 독립성으로 세지 않는다. run 안 위치를 공변량으로 둔다.

---

## 9. Competing Explanations

| 대안 해석 | 이를 가르는 분석 |
|---|---|
| E가 고른 클립이 이긴 것은 정서가 아니라 저수준 속성(길이, 반복 재생 횟수, 움직임, 밝기) 때문이다 | 길이와 반복 횟수 구간으로 짝을 맞춘 controversial 집합. 저수준 선택기 baseline. nuisance를 잔차화한 뒤 선택한 판과 비교 |
| E가 이긴 것은 V가 덜 잘 맞춰졌기 때문이다(모델 품질 차이) | 학습 fold 안 교차검증 정확도를 함께 보고한다. V의 용량을 키운 판과 E+V 결합 판에서도 E 단독 선택이 이기는지 본다. V가 학습 fold에서 E보다 잘 맞는데도 E 선택이 이길 때만 강한 증거로 본다 |
| 규범 평정이 사실상 장면 의미를 압축한 것이라 E가 "더 나은 의미 모델"일 뿐이다 | V에 인간 중립 캡션 embedding을 포함한다. controversial 클립의 캡션 의미 범주 분포를 비교한다. RQ-08(캡션으로 설명하고 남는 정서) 결과와 영역별로 대조한다 |
| 정서 영역이 아니라 전반적 각성/현저성이 반응을 올린다 | 영역 x 선택 표적 특이성 행렬. 억제 선택(하위 q%)도 함께 검증한다. 시각 대조 영역에서 V가 이기는지(양성 대조) 본다 |
| Mind captioning에서 실패한 것은 모델이 틀려서가 아니라 코호트 차이(scanner, TR, 반복 재생, 순서) 때문이다 | D6a의 Horikawa 보류 피험자 결과와 비교한다. D6b(관찰 반응 기반 선택)도 실패하면 코호트 간 재현성 자체의 한계로 해석한다 |
| 분석자 노출로 선택이 검증 데이터에 맞춰졌다 | 8.5절 봉인. 무작위 seed 기준선이 우연 수준인지 확인한다 |
| 시선 차이(자유 시청)가 영역 반응을 만든다 | 측정 불가. V에 시각 현저성(saliency) feature를 넣는 것으로 일부만 줄인다. 한계로 명시 |
| 반복과 친숙도 효과 | 6회 노출된 72개 테스트 클립을 선택과 검증에서 뺀다. S1(예비 노출)을 뺀 판을 함께 보고한다 |

---

## 10. Potential Findings

1. **정서 영역에서 E 승리(Δ_r > 0), 시각 대조에서 V 승리.**
   * 정서 영역의 반응 차이 중 일부는 시각-의미 feature로 계산되지 않는 정서 평정 공변으로 미리 예측된다. 이 예측은 사람과 코호트를 넘어 일반화된다.
   * Horikawa 2020의 정서 우위 주장을 사전 등록 전향 검증으로 보강한다.
   * 단 라벨이 규범 평정이므로 "자극의 규범 정서 속성"에 대한 결론이다. 참가자 경험에 대한 결론이 아니다.
2. **정서 영역에서도 V 승리 또는 차이 없음(동등성 확인), 시각 대조는 정상.**
   * 정서 영역 반응을 미리 고르는 데 정서 평정이 시각-의미 feature보다 나은 정보를 주지 않는다.
   * Horikawa 2020의 정서 우위는 의미 공변량의 측정 오차나 모델 품질 차이로 생겼을 가능성이 커진다(RQ-08과 함께 해석).
3. **E 선택이 Horikawa 보류 피험자에서는 이기고 Mind captioning에서는 지는 경우.** 정서 영역 선택이 코호트 특이적이다(scanner, 블록 구조, 순서). S축(일반화)에 대한 결과다.
4. **D6b(관찰 기반 선택)부터 Mind captioning에서 실패.** 정서 영역을 움직이는 클립 자체가 코호트를 넘어 잘 재현되지 않는다. Westlin 2025의 개인 특이성 보고(arXiv:2507.00320)와 맞는 결과다.
5. **TRIBE 팔이 E만큼 맞는 경우.** 관문을 통과한 피질 영역에서는 자극만으로 계산한 in-silico 뇌도 정서 영역 구동 클립을 고를 수 있다. TRIBE 팔이 E보다 크게 못하면 in-silico 선택의 한계를 보여 준다.
6. **양성 대조(시각 영역)도 실패.** 이 설계의 검출력이 부족하다. 정서 영역 결과를 해석하지 않는다(반증으로 세지 않음).

---

## 11. Scientific Contribution

* **정서 대 의미 논쟁:** 정서 관련 영역의 반응이 "장면 내용만 보는 모델"로 미리 예측되는가, 아니면 정서 평정이 더 잘 미리 고르는가를 사전 등록 전향 검증으로 판정한다. 이 논쟁은 Horikawa 2020의 정서 모델 우위 주장(doi:10.1016/j.isci.2020.101060)과 그에 대한 측정 오차 비판(doi:10.1371/journal.pone.0152719)에 걸쳐 있다.
* **정서 영역 '선택성' 주장의 검정 방식:** 범주 선택 영역에서 쓰던 고처리량 선택성 검정(Ratan Murty 2021)과 controversial 판정(Golan 2020)을 정서 영역에 처음 적용한다. 결과가 E 승리면 정서 범주적 또는 차원적 tuning 주장을 강화하고, V 승리면 정서 영역 반응의 상당 부분이 장면 의미로 운반된다는 구성주의 쪽 해석과 맞는다.
* **방법론:** 이미 수집된 같은 자극의 두 코호트에서 봉인 절차로 전향 검증을 흉내 내는 틀을 정서 연구에 제공한다. 새 fMRI 검증(R3)보다 약하다는 점을 명시한 채로다.

---

## 12. Limitations & Risks

* **새로움이 작다.** 같은 논리가 언어망, 범주 영역, amygdala 생성 자극에서 새 fMRI로 검증되었다. 남는 부분은 controversial 승패 하나다(감사 판정).
* **이미 수집된 검증 데이터.** 봉인을 지켜도 Tuckute 2024의 새 fMRI 검증보다 약하다. 분석자 노출을 완전히 배제할 수 없으면 Mind captioning 결과는 탐색적 재현으로 낮춘다.
* **표본.** 학습 5명, 검증 6명이다. 코호트 안 피험자들은 같은 순서를 공유한다. 모집단 평균 추론이 아니라 prevalence 추론만 한다.
* **controversial 집합 크기.** 정서 평정과 시각-의미 feature가 공선적이면 두 모델이 서로 다른 클립을 고르는 경우가 적다. Pilot에서 집합 크기가 사전 하한(영역당 한쪽 15개 이상, 사전 등록 때 확정)에 못 미치면 주 분석을 할 수 없다.
* **라벨.** 규범 평정(별도 MTurk 평정자)이다. 참가자 본인 경험, 생리, 시선이 없다.
* **피질하.** Horikawa TE 43 ms에서 amygdala 신호가 약할 수 있다. 신뢰도 하한 미달이면 확증 분석에서 뺀다. TRIBE 팔은 피질만 가능하다.
* **TRIBE v2.** 무음 짧은 클립 시퀀스는 학습 분포 밖이다. RQ-51 관문을 통과한 parcel에서만 쓴다. 라이선스는 비상업(CC BY-NC 4.0)이다.
* **클립 ID 대응과 블록 구조 차이.** 두 코호트의 반복 재생 규칙이 달라(8 s 대 10 s 기준) 같은 클립의 자극 노출량이 다르다.
* **모델 라이선스와 계산 자원**은 미확인이다.
* **overlap:** EmoBrain(구 EmoViS 범위 포함)의 "정서 대 시각-의미 모델 비교"와 겹친다.

---

## 13. Pilot Experiment

**Horikawa 2020 안에서만 하는 D6a(Mind captioning 반응을 열지 않음).**
* 절차:
  * 5-fold 클립 cross-fitting과 피험자 1명 보류 순환(5회)으로 E, V 선택을 만든다.
  * 보류 Horikawa 피험자에서 Δ_r을 계산한다.
* 계산량:
  * V-JEPA 2 feature 추출은 GPU 1장으로 수 시간 이내로 추정한다(미확인).
  * 캡션 embedding은 가볍다. ridge와 순열 검정은 CPU로 충분하다.
* 이 Pilot에서 정하는 것:
  * 영역별 controversial 집합 크기
  * 양성 대조(시각 영역에서 V 승리)의 재현 여부
  * Mind captioning 확증 분석에 쓸 SESOI. Pilot 효과 크기의 절반을 쓴다(사전 규칙).
  * q% 값
* **의사결정 기준:**
  * 계속: 정서 영역 2개 이상에서 controversial 집합이 하한 이상이고, 시각 대조 영역에서 V 승리가 5회 순환 중 3회 이상 나온다. 그러면 봉인(8.5절) 후 Mind captioning 검증으로 간다.
  * 수정: 집합이 작으면 q%를 키우거나 클립 단위 대신 RSA 쌍 단위 controversial 선택(FA-P2 방식)으로 바꾼다.
  * 중단: 양성 대조가 실패하면 설계의 검출력이 없으므로 중단한다. 이때는 RQ-08과 RQ-03의 결과를 먼저 기다린다.

---

## 14. Feasibility & Priority

| 항목 | 값 | 근거 |
|---|---|---|
| 최종 점수 | **34.0 / 45** (Coordinator 36, 평가자 32), 과학 기준 5개 합 18.5 | `selection.md` 2절, `scores_final.csv` |
| 기준별 최종 점수 | Novelty 3.5, Neuroscientific Importance 3.5, AI/Modeling 3.0, Dataset Feasibility 5.0, Methodological Rigor 3.5, Falsifiability 4.5, Interpretability 3.5, Generalizability 3.0, Feasibility 4.5 | `scores_final.csv` |
| 순위 | 전체 2위, **Shortlist 2번** | `selection.md` 4절 |
| High-priority 여부 | **제외.** 감사에서 "남는 새 부분이 작다"고 판정된 질문이라 상위 5개에서 뺐다 | `selection.md` 5절 |
| 붙는 관문 | RQ-51(TRIBE 팔), signal-feasibility(피질하) | `selection.md` 4절 |
| Novelty | 낮음~중간. controversial 승패 하나만 새롭다 | 5절 |
| Impact | 중간. Horikawa 정서 우위 주장의 강한 시험이지만 결론은 규범 정서 수준 | 11절 |
| Feasibility | 높음. 기존 데이터, 공개 모델, 선형 회귀. 봉인 절차와 실행 순서가 실제 위험이다 | 8.5절 |
| 권고 | **Shortlist 유지, 실행 순서는 RQ-08과 RQ-01 Pilot보다 앞서 봉인만 먼저.** 봉인은 비용이 거의 들지 않지만, 늦어지면 분석자 노출로 질문 자체의 가치가 사라진다. 주 분석은 Horikawa 내부 Pilot 결과를 보고 결정한다 | |
| overlap | **EmoBrain(구 EmoViS 범위 포함):** 정서 대 시각-의미 모델 비교 겹침. **Emo-FilM 연구:** 겹침 없음(Emo-FilM 미사용) | `reference/existing_projects.md`, matrix.csv |

---

## 반영하지 않은 지적

1. **"선택 풀을 72개 반복 클립으로 줄여 ceiling 대비로 평가"** (adversarial-reviewer EF-P6 응답 수정 2의 함의).
   * 반영하지 않았다. 72개는 controversial 선택을 하기에 너무 적다. 또 이 72개는 학습 세션 1회 + 테스트 5회로 총 6회 노출되어 반복과 친숙도 효과가 섞인다(Mind captioning Methods).
   * 대신 72개는 영역 신뢰도 계산에만 쓰고, 검증은 1회 노출인 학습 세션 반응으로 한다.
   * 같은 응답의 "정서 수준별 ceiling을 따로 보고"는 반영했다(8.1절).
2. **"RQ-10은 R3-internal 후보"** (`rq_landscape.md` 1절 1번).
   * 반영하지 않았다. 검증 반응은 선택 이전에 이미 수집되었다. 선택이 자극 제시를 바꾸지 않았으므로 자극 조작 실험(R3)이 아니다.
   * 이 카드는 evidence-level을 **R0(사전 등록된 전향 예측)** 으로 둔다. 봉인이 깨지면 일반 R0 상관 분석이다.
3. **FA-P2의 "의미는 가깝고 정서는 다른 클립 쌍을 실측 RSA로 판정"** 을 주 분석으로 쓰는 것.
   * 반영하지 않았다. 그 설계는 쌍 수준 RSA로 정서 대 의미를 가르는 질문이라 RQ-08과 RQ-13의 범위와 겹친다.
   * 이 카드에서는 Pilot 수정 경로(13절)의 대안 선택 방식으로만 남겼다.

---

## Safeguards 점검

### CLAUDE.md 6절 구분

| 항목 | 이 카드의 처리 |
|---|---|
| Experienced vs portrayed emotion | 라벨은 별도 평정자가 자기 느낌을 보고한 규범 평정이다. 참가자 경험이 아니다. 결론은 "자극의 규범 정서 속성"으로 한정한다 |
| Human vs model-generated annotation | E는 인간 규범 평정, V의 캡션은 인간 중립 캡션이다. VLM 팔만 AI 추정이며 보조로 따로 표기한다 |
| 본인 보고 vs 규범 평정 | 본인 보고 없음. 규범 평정만 쓴다 |
| Emotion vs visual/semantic representation | 주 산출물 자체가 이 구분이다(E 대 V controversial 승패). 캡션 embedding과 영상 feature를 V에 포함한다 |
| Encoding accuracy vs explanatory adequacy | 전체 예측 정확도가 아니라 두 모델이 갈리는 클립에서의 승패로 판정한다. 학습 정확도는 보조로만 보고한다 |
| Decodability vs representation vs causality | 선택 성공은 "정서 평정이 영역 반응을 미리 예측한다"까지다. 영역이 정서를 만든다는 인과 결론은 내지 않는다 |
| In-silico vs observed | TRIBE 팔의 선택은 in-silico, 검증 반응은 관찰이다. 따로 보고한다 |
| Shared representation vs dataset-specific confound | D6a의 같은 코호트 보류 피험자 결과와 Mind captioning 결과를 나눠 보고한다. 순서, scanner, 블록 구조 차이를 공변량과 해석 단서로 둔다 |
| Exploratory vs confirmatory | 봉인된 사전 등록 분석만 확증으로 본다. 그 외와 노출이 확인된 경우는 탐색으로 표시한다 |

### 방법론 점검

| 항목 | 처리 |
|---|---|
| HRF 지연, 시간 자기상관 | Horikawa 방식(4 s 이동, 블록 평균)을 두 코호트에 똑같이 적용한다. 직전 블록 유형(평가 블록)과 run 안 위치를 공변량으로 둔다 |
| Stimulus / movie / subject leakage | 클립 5-fold cross-fitting, 내용 중복과 같은 원본 의심 클립은 같은 fold, 학습과 검증 피험자 분리, 두 코호트 피험자 비중복(사용자 확인, 원문 미기재) |
| Repeated stimulus confound | 6회 노출 72개 클립은 검증에서 제외한다. S1(예비 노출) 제외 판을 보고한다. 반복 재생 횟수는 공변량이다 |
| Inter-rater agreement, label noise | 규범 평정의 평정자 수가 비디오당 9~17명(검색 수준)이라 잡음이 있다. 평정 잡음은 E에 불리하게 작용하므로 E 승리는 보수적 결과다 |
| 시각-의미-정서 공선성 | controversial 집합으로 공선 구간을 피한다. 공선이 너무 커서 집합이 작으면 주 분석을 하지 않는다(Pilot 기준) |
| 시공간 해상도 | 블록 수준(10 s 이상) 반응만 쓴다. 클립 내 동역학은 다루지 않는다 |
| ROI 선택과 순환 추론 | 표적 영역은 해부학 기준으로 사전 지정하고, Horikawa 결과로 고르지 않는다. 선택과 검증 데이터가 분리되어 있다 |
| 다중비교 | 사전 지정 영역에 대해 Holm 보정을 한다 |
| 데이터 접근, checkpoint 라이선스 | 데이터는 사용자 보유. TRIBE v2는 CC BY-NC 4.0. V-JEPA 2 가중치, 문장 embedding, VLM 라이선스는 미확인 |
| 사전학습 오염 | EmoNet 사용 금지. V-JEPA 2와 VLM이 Cowen & Keltner 클립을 학습했는지는 미확인이므로 provenance 등록부에 적는다. TRIBE v2의 fMRI 학습 데이터에 두 코호트는 없다(arXiv:2605.04326 5.7절) |
| 데이터셋 간 주석 비호환 | 두 코호트가 같은 클립과 같은 규범 평정을 쓰므로 해당 없음 |

### 필수 태그

| 태그 | 값 |
|---|---|
| label-provenance | 대상 felt(별도 평정자가 자기 느낌을 보고) / 주체 별도 평정자 규범(Cowen & Keltner MTurk). V의 캡션은 인간 기술(정서 배제). VLM 팔은 AI 추정 |
| evidence-level | **R0** (봉인된 전향 예측). 새 자극 제시가 없으므로 R3 아님 |
| insilico-vs-observed | 혼합: TRIBE 팔 선택은 in-silico, 모든 검증은 관찰 |
| G1 | 원본 자극 필요(V-JEPA 2 feature, TRIBE 입력, 클립 길이 계산). 보유 |
| signal-feasibility | 필수. Mind captioning 반복 신뢰도로 영역별 하한 점검. amygdala는 Horikawa TE 43 ms 때문에 하한 미달 가능 |
| minimum-validation (7항목) | 1 경쟁 모델과 matched-complexity null: **충족**(E, V, E+V, 저수준, 무작위, 용량 확대 V). 2 원 값과 상한 병기: **충족**(D6b 상한, 반복 신뢰도). 3 내용 지표 다중화와 신뢰도 민감도: **부분 충족**(영상, 캡션, 저수준 feature 다중화. 평정 신뢰도 민감도는 평정자 개인 자료가 없어 제한). 4 leakage 경로별 대응: **충족**(클립 fold, 피험자 분리, 사전학습 오염 등록, 분석자 노출 봉인). 5 일반화 수준과 추론: **충족**(새 클립 + 새 피험자 + 새 코호트, prevalence와 2-factor bootstrap). 6 라벨 출처 표시: **충족**. 7 반대 결과 해석 사전 기술: **충족**(10절, 양성 대조 실패 시 해석 중지 규칙) |
