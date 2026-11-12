# 재탐색 라운드: D1 Brain-like Model (brain-inspired)

* 기준일: 2026-11-12. 지시: `outputs/revision/plan.md`(전체 직접 읽음)와 Coordinator 위임 메시지.
* 담당: (A) 출발점 RQ-54, RQ-56을 진단하고 다시 쓴다. (B) D1에서 새 질문 4개를 낸다.
* 평가 기준: plan.md 2절의 두 기준인 **AI-enabled Affective Neuroscience Contribution**과 **1-month Feasibility**. 모든 질문은 "AI 쪽으로 돌려주는 기여"가 아니라 "AI가 있어야만 물을 수 있는, 정서와 뇌에 대한 질문"을 목표로 한다.
* 지킨 함정(plan.md 4절):
  * EmoNet은 쓰지 않는다.
  * Mind captioning(MC) 학습은 2,108개로 고정하고 시험 72클립을 학습에서 뺀다.
  * C&K 클립은 무음이다.
  * MC 보유본의 전처리 형식은 미확인으로 둔다.
  * 정서 라벨은 별도 평정자의 규범 평정이다.
  * VLM과 MLLM은 C&K 오염 위험 때문에 모델 본체로 쓰지 않는다.
  * 선행 여부는 직접 검색했다(9절).
* 문헌: 이번 라운드에서 식별자로 확인한 논문 6편을 `literature.jsonl`에 추가했다(총 79편).

---

## 0. 공통 설계 원칙: "제약을 넣고 빼는 인공 뇌" 비교

이 라운드의 모든 질문은 같은 구조를 갖는다.

1. **통제된 모델 계열을 만든다.** 공개 checkpoint 하나를 고정한다. 그 위에 뇌를 닮은 제약을 하나씩 넣거나 뺀다: 재진입 feedback, 피질하 지름길, 재귀, 지형 배치, 학습 이력. 그 밖의 조건(데이터, 크기, 학습량)은 맞춘다. 사람에게는 이런 비교를 할 수 없다. 이것이 plan.md 2절 기준 (a) "학습 조건을 조작한 인공 뇌, 구조 제약을 바꾼 모델"에 해당한다.
2. **사람 뇌의 세 표지와 대조한다.** 각 모델이 아래 셋 중 무엇을 재현하는지 본다.
   * (i) 정서 선택 영역 또는 단위가 있는가, 어디에 있는가
   * (ii) 34범주 범주 구조와 gradient
   * (iii) 개인차의 모양
   * 대조 데이터는 Horikawa 2020(5명, 2,181클립 단일 제시)과 MC(6명, 2,108 학습 클립, 72클립 5회 반복)다. NSD는 시각 정렬 보정용이다.
3. **정서와 의미 내용을 분리한다.** 모든 뇌 비교에서 MC의 사람 캡션 embedding을 통제 변수로 넣는다. 이 캡션은 "정서 반응 대신 시각 내용을 쓰라"는 지시로 받았다. 이 캡션으로 설명되는 성분을 뺀 정서 기하를 1차 결과로, 빼기 전 결과를 함께 보고한다.
4. **신뢰도 상한을 둔다.** MC 시험 72클립의 5회 반복으로 ROI별 noise ceiling을 구한다. 그래서 모델 간 차이를 상한 대비로 해석한다. Horikawa는 반복이 없어 상한을 직접 구할 수 없다.
5. **누수를 막는다.**
   * EmoNet은 쓰지 않는다.
   * 정서 학습 데이터는 EmoSet(arXiv:2307.07961, 별도 평정자의 perceived 라벨, Mikels 8범주)이다. C&K 프레임, Horikawa/MC 프레임, NSD 이미지와 지각 해시 중복을 검사한다.
   * 시각 backbone은 ImageNet 계열 공개 가중치를 쓴다. 웹 규모 VLM은 C&K 오염 위험 때문에 본체로 쓰지 않는다.
6. **증거 수준을 표시한다.** 모델 안의 조작은 R1이고 뇌와의 대조는 R0다. "모델에서 X가 필요했다"는 결과를 "뇌에서 X가 필요하다"로 해석하지 않는다. 결론은 "뇌의 정서 표상은 X를 넣은 모델과 더 닮았다"까지다.

---

## 1. 출발점 RQ-54 진단과 재작성

### 1.1 원 질문

"정서를 배우게 한 AI 안에서 생긴 '정서 뉴런'은 뇌의 정서 반응을 설명할까?" EmoSet으로 학습한 모델의 창발 정서 unit을 저수준, 의미 속성으로 설명하고, 비정서 모델보다 정서 영역 분산을 고유하게 설명하는지 묻는다.

### 1.2 왜 약했는가

| 기준 | 진단 |
|---|---|
| AI-enabled Contribution | **약함.** 비교가 "정서 학습 모델 대 비정서 학습 모델의 encoding 정확도"였다. 그런데 두 모델은 데이터, 목표, 학습량이 동시에 달라서, 이기더라도 무엇 때문인지 말할 수 없다. "정서 뉴런이 뇌를 설명한다"는 결과는 결국 feature 비교(R0)라서 AI가 예측 도구 이상이 아니다. 더구나 물체 학습 망에서 정서 선택 unit이 생긴다는 것(Liu et al. 2024, doi:10.1371/journal.pcbi.1011943)과 정서 학습 망 feature가 시각피질을 예측한다는 것(Kragel et al. 2019, doi:10.1126/sciadv.aaw4358)은 이미 보고되었다. 정서 이론에 대해 말해 주는 것이 불분명했다 |
| 1-month Feasibility | 보통. EmoSet 학습과 encoding은 가능하다. 다만 "창발 unit 속성 회귀"는 unit 정의와 선택성 기준에 따라 결과가 크게 흔들려 4주 안에 결론을 내기 어렵다 |

**고칠 방향:** Liu 2024의 Discussion은 두 가설을 경쟁시켰다. 하나는 시각피질의 정서 정보가 시각 학습 자체에서 나온다는 "내재" 가설이다. 다른 하나는 편도체 등 앞쪽 영역의 되먹임에서 온다는 "재진입" 가설이다. 이 두 가설을 같은 망에서 **연결 하나만 바꿔** 구현하면, 관찰로는 할 수 없는 통제 비교가 된다.

### [BI-RV-1] 시각 뇌가 장면의 정서를 담는 것은 스스로 배워서일까, 정서 판단이 되돌려 줘서일까?

* **자세한 질문:** 물체 인식으로 사전학습한 같은 시각 망을 바탕으로 세 판본을 만든다.
  * (a) **내재:** 정서 학습 없음
  * (b) **판독:** 시각 망은 고정하고 정서 판독 모듈만 학습
  * (c) **재진입:** 정서 모듈에서 시각 망 중간층으로 되먹임 연결을 두고 정서 목표로 학습

  각 판본의 시각층 표상이 사람 시각피질(V1~V4, 외측 후두, 복측 측두)의 정서 기하를 얼마나 재현하는지 비교한다. 정서 기하는 의미 캡션을 통제한 34범주 구조다. 같은 비교를 transmodal 영역(vmPFC, TPJ, DMN)에도 한다. 특히 시각피질에서 "이미지의 시각 feature로는 설명되지 않는 정서 성분"이 (c)의 되먹임이 만든 성분과 맞는지 본다.
* **AI가 있어야만 가능한 이유:** 사람에서 재진입 경로만 끊는 조작은 할 수 없다. 편도체 병변 사례는 드물고 범위가 통제되지 않는다. 관찰 데이터의 연결성 증거(Bo et al. 2021, doi:10.1093/cercor/bhaa411: 앞쪽 영역에서 시각피질로 가는 연결이 시각피질 정서 decoding과 관련)는 상관이다. 모델에서는 다른 것을 모두 고정하고 되먹임 연결의 유무만 바꿀 수 있다. 시험 시점에 되먹임만 끊는 모델 내 lesion(R1)도 가능하다.
* **정서와 뇌에 대해 새로 알게 되는 것:** 시각피질 정서 표상의 기원 논쟁(내재 대 재진입)에 표상 내용 수준의 판정 근거를 준다.
  * (c)만 사람 시각피질의 "시각 feature 밖 정서 성분"을 재현하면, 그 성분은 재진입의 서명과 양립한다.
  * (a)로 충분하면 Kragel 2019의 "정서 schema는 시각계에 내재한다"는 해석이 강해진다.
  * 이는 구성주의 이론(정서는 앞쪽 개념 체계가 감각에 투사한 결과)과 시각 schema 이론 사이의 구체적 쟁점이다.
* **데이터:**
  * Horikawa 2020: HCP360과 피질하 ROI가 들어 있는 블록 평균 전처리본(Stage 1).
  * MC: 학습 2,108클립, 시험 72클립 5회 반복으로 noise ceiling. 정서 배제 사람 캡션. 전처리 형식은 미확인.
  * NSD: 되먹임 학습이 물체 표상 정렬을 망가뜨리지 않았는지 보는 보정용.
  * EmoSet: 정서 학습용. 라벨은 perceived이고 라이선스는 미확인.
  * 라벨: C&K 34범주와 14차원 규범 평정(별도 평정자). 쓰는 곳은 뇌 쪽 기하 정의뿐이고 모델 학습에는 쓰지 않는다.
* **모델과 checkpoint:**
  * ImageNet 사전학습 VGG16 또는 ResNet-50(torchvision 공개 가중치, 가중치 이용 조건 미확인)
  * 재귀 대조로 CORnet-S(arXiv:1909.06161, 코드 공개, 라이선스 미확인)
  * 정서 모듈과 지름길 구조의 참고 구현은 Leem et al. 2026(arXiv:2607.19327)의 공개 코드 `lab-smile/FearConditioningAI`(라이선스 미확인)
  * GPU: 판본 3개 x seed 3개의 EmoSet 학습은 GPU 1장에서 판본당 수 시간. encoding은 CPU ridge.
* **핵심 분석:**
  1. ROI별로 각 판본의 층별 feature로 encoding한다. 분산 분할은 (a)의 feature와 (c)에만 있는 성분으로 나눈다.
  2. 의미 캡션을 잔차화한 34범주 중심 RSA를 한다.
  3. 시험 시점에 되먹임을 끊었을 때 (c)의 뇌 정렬이 떨어지는 정도를 본다.
  4. 대조군으로 같은 용량의 되먹임을 섞은 라벨로 학습한 판본(c')을 둔다. 되먹임이라는 용량 자체의 효과를 빼기 위해서다.
* **예측:** 시각피질의 정서 성분 중 의미 캡션과 (a) feature로 설명되지 않는 몫이 있고, 그 몫을 (c)가 (c')보다 더 설명하면 재진입 서명이다.
* **반증 조건:**
  * (c)가 (a), (c') 대비 고유 분산을 더하지 못하고 transmodal 영역에서만 이득이 있으면, 시각피질의 정서 정보는 내재 경로로 충분하다.
  * (c)와 (c')가 같으면 되먹임 효과는 정서가 아니라 용량이다.
  * 블록 평균 fMRI는 시간 순서를 보이지 못하므로, 이 검정은 시간이 아니라 표상 내용에 대한 것이다.
* **4주 계획:**
  * 1주: ROI 추출, 캡션 embedding, EmoSet 중복 검사, ImageNet feature 기준선 encoding, MC noise ceiling
  * 2주: (a), (b), (c), (c') 학습(seed 3)
  * 3주: encoding, 분산 분할, RSA, 모델 내 lesion
  * 4주: NSD 보정, 층별 강건성, 보고
* **가장 가까운 선행과 차이:**
  * Liu et al. 2024(doi:10.1371/journal.pcbi.1011943): feedforward만, 3범주, 뇌 비교 없음.
  * Liu et al. 2025 bioRxiv(doi:10.1101/2025.10.20.683439): 시각 망에서 편도체 모사 모듈로 가는 feedforward, 편도체 fMRI와 비교. 시각 망으로의 되먹임 여부는 WebSearch 요약에서 확인되지 않음.
  * Jang & Kragel 2025(doi:10.1523/JNEUROSCI.1436-24.2025): 편도체 encoding.
  * Bo et al. 2021: 관찰 연결성.
  * VSS 학회 초록(search_index, 식별자 미확인): encoding 모형이 만든 합성 fMRI에서는 초기 시각피질의 정서 decoding이 안 되어 재진입을 지지한다고 해석.
  * **차이:** 같은 망에서 되먹임 연결만 조작하고, 34범주와 의미 통제로 사람 시각피질 기하와 대조한다. 이런 연구는 찾지 못했다.
  * 검색: WebSearch("recurrent feedback from valence or amygdala module to visual network deep learning model reentry emotional images compared with visual cortex fMRI emotion representation"), 2026-11-12.
* **주요 위험:**
  * EmoSet 8범주와 C&K 34범주의 불일치. 뇌 쪽 기하는 34범주로, 모델 학습은 8범주로 해서 매핑을 피한다.
  * 되먹임이 시각층을 거의 바꾸지 않을 수 있다(그 자체가 결과).
  * 피험자가 11명이고 Horikawa에는 반복이 없다.
  * MC 전처리 형식이 미확인이다.
* **표기:** label-provenance felt / 별도 평정자 규범(C&K), 학습 라벨 perceived / 별도 평정자(EmoSet). evidence-level R1 + R0. insilico-vs-observed 혼합. G1 필요(보유).

---

## 2. 출발점 RQ-56 진단과 재작성

### 2.1 원 질문

"AI를 뇌의 정서 반응에 맞춰 학습시키면 사람의 정서 판단과 더 비슷해질까?" video 모델을 정서 관련 영역 fMRI로 미세조정(brain-tuning)하면 시각피질로 미세조정한 경우보다 사람 정서 판단 정렬이 좋아지는지 묻는다.

### 2.2 왜 약했는가

| 기준 | 진단 |
|---|---|
| AI-enabled Contribution | **중간 이하.** 결과의 주어가 "모델이 사람 판단과 더 비슷해졌다"라서, 기여가 AI 쪽(더 나은 정서 모델)으로 향한다. 뇌에 대해 말하는 부분("뇌 정서 표상이 라벨에 없는 정보를 갖는가")은 결론이 모호하다. 비교 대상이 시각피질 하나라 "정서 영역이라서"인지 "신호가 좋은 영역이라서"인지 가를 수 없다. 이 무작위 영역 대조의 부재는 평가자도 지적했다(reviewer_notes RQ-56). 평가 데이터(Emo-FilM, Spacetop)는 소리가 있는 영상의 평정이라, 무음 시각 모델의 정렬 평가와 맞지 않는다 |
| 1-month Feasibility | 보통. video 모델 미세조정은 무겁다. 선행으로 Policzer et al. 2025(arXiv:2511.07988, 사회 인지 영역 brain-tuning)가 있다. overlap: EmoBrain(뇌 정서 정보를 teacher-student로 증류) |

**고칠 방향:** 주어를 뇌로 바꾼다. 묻는 것은 "어느 뇌 영역의 표상을 모델에 옮겨 심었을 때, 처음 보는 자극에서 사람 같은 정서 구조가 라벨 없이 생기는가"다. 이것은 영역 표상의 **충분성에 대한 모델 기반 검정**이다. decoding은 "그 영역에 정보가 선형으로 있다"만 보이고, "그 표상이 새 자극으로 일반화되는 정서 구조를 담는가"는 보이지 못한다.

### [BI-RV-2] 뇌의 어느 부위가 가진 정보를 AI에 옮겨 심어야 처음 보는 장면에서도 사람 같은 정서 구조가 생길까?

* **자세한 질문:** 같은 시각 backbone을 영역별 fMRI 반응을 예측하도록 각각 미세조정한다(영역 이식). 영역은 다음과 같다.
  * 편도체, 섬엽, vmPFC/OFC, TPJ/STS, 시각피질
  * 대조: split-half 신뢰도와 voxel 수를 맞춘 무작위 parcel 집합 여러 개

  미세조정에는 정서 라벨을 전혀 쓰지 않는다. 그 뒤 학습에 쓰지 않은 C&K 클립과 NSD 이미지에서 각 이식 모델의 표상이 사람 규범 정서 구조를 얼마나 재현하는지 본다. 사람 규범 정서 구조는 34범주 RSA, 14차원 gradient, 적은 라벨로 학습한 선형 판독의 효율로 잰다.
* **AI가 있어야만 가능한 이유:** 한 사람의 뇌 영역 표상을 다른 학습자에게 옮겨 심어, 그것이 새 자극에서 무엇을 만들어 내는지 보는 실험은 모델로만 할 수 있다. 무작위 영역 대조와 같은 양의 라벨 미세조정 대조를 같은 backbone에서 두면, "정서 영역이라서 생기는 효과"와 "신호가 좋아서 생기는 효과"를 가를 수 있다.
* **정서와 뇌에 대해 새로 알게 되는 것:**
  * 정서 구조가 특정 영역에 집중되어 있는지(Horikawa 2020의 transmodal 결론) 판정할 수 있다.
  * 시각 schema에 이미 있는지(Kragel 2019)도 판정할 수 있다.
  * 영역이 아니라 분산된 개인 특이 패턴에 있는지(Westlin 2025 preprint의 해석)도 볼 수 있다.
  * 판정 수단은 "새 자극으로 일반화되는 정서 구조를 실어 나르는가"라는 기능적 기준이다.
* **데이터:**
  * 학습: Horikawa 2020과 MC의 학습 클립. 두 코호트는 같은 C&K 비디오를 보았다.
  * 평가: MC 시험 72클립과 무작위로 뺀 C&K 클립 10%(두 코호트 모두 학습에서 제외). 라벨은 C&K 규범 평정(별도 평정자).
  * 영역 밖 일반화: NSD shared 이미지 중 nsdmeadows valence/arousal 100장(참가자 본인 평정으로 보이나 지시문 미확인, Stage 1).
  * Emo-FilM과 Spacetop은 소리가 있는 영상의 평정이라 무음 시각 모델 평가의 주 기준으로 쓰지 않는다.
* **모델과 checkpoint:**
  * ImageNet 지도학습 ViT-B 또는 ResNet-50(torchvision 공개 가중치)에 LoRA로 미세조정한다.
  * 웹 규모 VLM은 C&K 오염 위험(plan.md 4절) 때문에 피한다.
  * 참고 선행 구현: Moussa et al. 2024(arXiv:2410.09230, 음성 모델 brain-tuning), Policzer et al. 2025.
  * GPU: 영역당 GPU 1장에서 수 시간. 영역 6개와 무작위 대조 5개, seed 2개.
* **핵심 분석:**
  1. 이식 모델별 RSA(모델 표상 대 규범 34범주 구조)와 few-shot 선형 판독 효율을 잰다.
  2. 무작위 parcel 분포 대비 순위를 매긴다.
  3. 같은 gradient step의 라벨 미세조정 판본과 비교한다.
  4. 영역별 예측력(이식 품질)을 공변량으로 둔다.
* **예측:** 특정 영역(예: vmPFC나 TPJ)의 이식이 신뢰도를 맞춘 무작위 parcel 분포의 상위 5%를 넘어 사람 정서 구조를 만든다. 그 이득은 의미 캡션 기하를 통제해도 남는다.
* **반증 조건:**
  * 어떤 정서 관련 영역도 신뢰도를 맞춘 무작위 parcel을 이기지 못하면, 정서 구조가 특정 영역 표상에 집중되어 있다는 주장은 이 기능 기준에서 지지되지 않는다(분산 또는 개인 특이 해석과 양립).
  * 시각피질 이식이 가장 좋으면 시각 schema 해석이 지지된다.
* **4주 계획:**
  * 1주: ROI와 신뢰도 계산, 신뢰도를 맞춘 무작위 parcel 생성, 보류 집합 고정, 평가 지표 구현
  * 2주: 영역별 brain-tuning
  * 3주: 평가, 라벨 미세조정 대조, NSD 일반화
  * 4주: seed 강건성과 보고
* **가장 가까운 선행과 차이:**
  * Policzer et al. 2025(arXiv:2511.07988): STS 대상, 사회 인지 과제.
  * Moussa et al. 2024: 음성 의미.
  * Liu et al. 2025 bioRxiv VCA: 편도체 모사 모듈을 valence, arousal 라벨로 학습한 뒤 편도체 fMRI와 정렬을 본 것으로, brain-tuning이 아니다.
  * Algonauts 2025 보고(arXiv:2510.06235, ID 확인, 내용은 검색 요약 수준): 영상 모델 미세조정으로 영화 fMRI 예측력이 소폭 향상.
  * **차이:** 정서 관련 영역들을 신뢰도를 맞춘 무작위 영역과 경쟁시키고, 라벨 없이 생기는 정서 구조를 결과 변수로 둔다. 이런 연구는 찾지 못했다.
  * 검색: WebSearch("brain-tuning fine-tune vision or video model on amygdala or emotion-related fMRI responses improves human emotion judgment alignment"), 2026-11-12.
* **주요 위험:**
  * 11명, Horikawa 단일 제시라 영역 반응 신뢰도가 낮다. 특히 편도체는 signal-feasibility 점검이 필요하다.
  * 이식 품질이 영역마다 달라 공변량 통제가 필수다.
  * MC 전처리 형식이 미확인이다.
  * 평가 라벨이 규범 평정이다.
  * overlap: EmoBrain(뇌 정서 정보 증류).
* **표기:** label-provenance 평가 felt / 별도 평정자 규범, NSD는 참가자 본인으로 보임(미확인). evidence-level R1(영역 이식이라는 모델 조작) + R0. insilico-vs-observed 혼합. G1 필요(보유).

---

## 3. [BI-RV-3] 시각 피질을 거치지 않는 거친 지름길은 어떤 정서를 알아보는 데 꼭 필요할까?

* **자세한 질문:** 정서 판독 모듈에 두 입력로를 둔 모델을 만든다.
  * (A) 전체 시각 위계를 거치는 길
  * (B) 초기층 또는 저공간주파수 입력에서 바로 들어오는 지름길

  조작은 세 가지다: 지름길 유무, 지름길 입력(저공간주파수, 고공간주파수, 초기층 feature), 시험 시점 지름길 차단. 이 조작으로 어떤 정서 범주가 지름길에 의존하는지 지도를 만든다. 그 의존 지도가 사람 편도체와 시상(pulvinar) 반응의 범주 프로필과 맞는지 본다. 사람 쪽 프로필은 Horikawa와 MC의 34범주 클립에서 시각피질 feature로 설명되지 않는 성분이다.
* **AI가 있어야만 가능한 이유:** 사람에서 피질 경로와 피질하 경로를 따로 끌 수 없다. fMRI는 지연시간을 재지 못해 "빠른 길"을 직접 보지 못한다. 모델에서는 지름길만 끄고 범주별 손실을 잴 수 있다. 그 손실 지도는 관찰 데이터로 계산할 수 없던 변수다(plan.md 2절 (b)).
* **정서와 뇌에 대해 새로 알게 되는 것:** "낮은 길"(LeDoux) 대 "여러 길"(Pessoa & Adolphs) 논쟁을 다룬다. 핵심은 피질하 경로가 위협 특이 탐지기인지, 정서 전반의 거친 신호인지다.
  * Kragel et al. 2021(doi:10.1016/j.neuron.2021.06.001)은 상구-pulvinar-편도체 경로가 혐오성을 추적한다고 했다.
  * McFadyen et al. 2017(doi:10.1523/JNEUROSCI.3525-16.2017)은 공간주파수와 무관한 경로를 보고했다.
  * 모델의 범주 의존 지도가 사람 편도체 프로필과 맞는 쪽이 어느 해석인지를 34범주 수준에서 가른다.
* **데이터:**
  * Horikawa 2020(피질하 ROI 포함). TE 43 ms라 피질하 신호 손실 점검이 필요하다(systems-neuro 기록).
  * MC(TE 30 ms, 반복으로 피질하 신뢰도 추정 가능).
  * EmoSet(학습).
  * signal-feasibility 게이트는 SN-P3의 내장 대조를 그대로 쓴다. 무음 자극에서 LGN-V1이 교차 연결보다 강하고 MGN-A1은 교차 수준이어야 한다.
* **모델과 checkpoint:**
  * Leem et al. 2026의 Visual-Valence + Shortcut 구조(코드 공개, 라이선스 미확인)를 EmoSet 8범주와 valence로 다시 학습한다.
  * 시각 망은 ImageNet VGG16을 고정한다.
  * GPU 1장. 판본 6개(지름길 없음/있음 x 입력 3종) x seed 3.
* **핵심 분석:**
  1. 모델: 범주별 지름길 차단 손실을 잰다.
  2. 사람: 시각피질 feature와 의미 캡션으로 예측한 편도체/pulvinar 반응의 잔차를 범주별로 평균해 프로필을 만든다.
  3. 둘을 순위 상관하고 무작위 범주 순열과 비교한다.
  4. 보조로, 지름길 모듈 feature가 편도체 잔차를 고유하게 설명하는지 encoding한다.
* **예측:** 지름길 의존이 큰 범주(예: 공포, 공포감, 혐오)가 사람 편도체 잔차 프로필의 상위와 겹친다.
* **반증 조건:**
  * 순위 상관이 순열 분포와 구분되지 않으면 지름길 계산은 사람 편도체의 범주 프로필을 설명하지 못한다.
  * 지름길 의존이 모든 범주에 고르면 "정서 전반의 거친 신호" 해석이 지지된다.
  * signal-feasibility 게이트를 통과하지 못하면 피질하 비교는 하지 않고 모델 결과만 보고한다.
* **4주 계획:**
  * 1주: 게이트(내장 대조, tSNR), 피질하 ROI 잔차 계산
  * 2주: 모델 판본 학습
  * 3주: 차단 손실 지도, 사람 프로필 대조
  * 4주: MC 재현, 보고
* **가장 가까운 선행과 차이:**
  * Leem et al. 2026(arXiv:2607.19327): 지름길이 조건화에 필요함을 보였으나 뇌 비교와 범주 지도는 없다.
  * Liu et al. 2025 VCA: feedforward, 편도체 fMRI.
  * Jang & Kragel 2025: 편도체 DNN encoding.
  * Kragel 2021: 관찰 경로 식별.
  * **차이:** 지름길 조작이 만든 범주 의존 지도를 34범주 사람 편도체 프로필과 대조한다. 이런 연구는 찾지 못했다.
  * 검색: Round 2/재점검 기록(WebSearch 2회, api.crossref.org)과 이번 WebSearch("recurrent feedback ... amygdala module ...", 2026-11-12).
* **주요 위험:**
  * 3T 피질하 신호가 약하다.
  * 블록 평균이라 시간 정보가 없다.
  * EmoSet 8범주로 학습한 모델의 34범주 C&K 클립 차단 손실은 정서 판독 출력의 변화량(범주 무관 거리)으로 잰다.
  * 지름길 정의가 결과를 좌우한다(입력 3종으로 대응).
* **표기:** label-provenance felt / 별도 평정자 규범(C&K), 학습 perceived(EmoSet). evidence-level R1 + R0. signal-feasibility 필수. G1 필요(보유).

---

## 4. [BI-RV-4] 한눈에 알 수 없는 정서일수록 뇌의 더 깊은 곳에서 표상될까?

* **자세한 질문:** 재귀 시각 망에 정서 판독을 붙여, C&K 클립마다 "재귀 요구량"을 계산한다. 재귀 요구량은 정서 판독이 안정될 때까지 필요한 재귀 단계 수, 또는 feedforward 판독 대비 재귀 판독의 이득이다. 같은 망의 물체 판독 재귀 요구량을 통제한 뒤, 정서 재귀 요구량이 큰 클립일수록 사람 뇌에서 정서 정보가 시각피질보다 transmodal 영역에 더 많이 있는지 묻는다. 정서 정보량은 각 영역에서 의미 캡션 통제 후 정서 고유 설명량으로 잰다.
* **AI가 있어야만 가능한 이유:** Horikawa와 MC에는 반응 시간 같은 자극별 처리 난이도 측정이 없다. 모델은 자극마다 "정서를 알아보는 데 필요한 계산 깊이"라는, 관찰할 수 없던 잠재 변수를 준다(plan.md 2절 (b)). 물체 인식에서 재귀가 필요한 "늦게 풀리는 이미지"를 정한 논리(Kar et al. 2019, doi:10.1038/s41593-019-0392-5)를 정서로 옮긴다.
* **정서와 뇌에 대해 새로 알게 되는 것:** Horikawa 2020은 정서 표상이 unimodal-transmodal 경사의 끝에 있다고 했다. systems-neuro는 이것이 정서 고유 속성인지 시간 적분 위계의 부산물인지 물었다(Round 1 U4). 이 질문은 세 번째 설명을 시험한다: "정서마다 필요한 계산 깊이가 다르고, 깊이가 큰 정서가 경사의 끝에 표상된다." 범주 이론(정서마다 다른 처리)과 구성 이론(맥락 통합이 많은 정서일수록 개념 체계 의존)에 각각 무엇을 말하는지는 범주별 재귀 요구량 순위로 해석한다.
* **데이터:** Horikawa 2020, MC(같은 C&K 클립, 11명). 의미 통제는 MC 캡션. NSD는 물체 재귀 요구량의 보정용이다.
* **모델과 checkpoint:**
  * CORnet-S(ImageNet, 공개, 라이선스 미확인)에 EmoSet 정서 판독과 ImageNet 물체 판독을 단계별로 붙인다.
  * 클립당 프레임 여러 장을 평균한다.
  * GPU 1장, 판독 학습은 수 시간.
* **핵심 분석:**
  1. 클립별 정서 재귀 요구량과 물체 재귀 요구량을 계산한다.
  2. 영역별(V1에서 vmPFC까지 경사 순서) 정서 고유 설명량을 클립 집합별로 추정한다.
  3. 재귀 요구량 사분위별로 경사 기울기를 비교한다.
  4. 보조로 feedforward 모델과 재귀 모델의 encoding 차이가 고요구량 클립의 고차 영역에 몰리는지 본다.
* **예측:** 정서 재귀 요구량 상위 클립에서 정서 정보의 경사 기울기가 더 가파르다(transmodal 쪽 비중이 큼). 물체 재귀 요구량은 이 효과를 설명하지 못한다.
* **반증 조건:**
  * 기울기가 사분위와 무관하면 계산 깊이 설명은 기각된다.
  * 물체 요구량을 통제하면 효과가 사라지면 그것은 정서가 아니라 시각 난이도(복잡도, 모호성) 효과다.
* **4주 계획:**
  * 1주: 프레임 추출, CORnet 판독 학습
  * 2주: 재귀 요구량 계산과 신뢰도(seed, 프레임 표본)
  * 3주: 영역별 정서 고유 설명량과 사분위 분석
  * 4주: 통제 분석(물체 요구량, 시각 복잡도)과 보고
* **가장 가까운 선행과 차이:**
  * Kar et al. 2019: 물체 인식.
  * Kietzmann et al. 2019(doi:10.1073/pnas.1905544116): 시각 동역학의 재귀.
  * 동적 얼굴 표정 인식에서 공간주파수 간 재귀가 모호성 해소를 돕는다는 CogSci 2020 논문(search_index, 식별자 미확인).
  * **차이:** 자극별 정서 계산 깊이를 fMRI의 정서 표상 위치(경사)와 잇는 연구는 찾지 못했다.
  * 검색: WebSearch("recurrent processing required for recognizing emotion in complex images late-solved emotional scenes recurrent neural network time steps social emotions"), 2026-11-12.
* **주요 위험:**
  * 재귀 요구량이 정서가 아니라 장면 복잡도나 모호성을 잴 수 있다(물체 요구량, 복잡도 공변량).
  * EmoSet 정지 이미지 판독을 영상 프레임에 쓰는 데 따른 도메인 차이.
  * 클립 단위 블록 반응이라 시간 해상도가 없다.
* **표기:** label-provenance felt / 별도 평정자 규범. evidence-level R0(모델 변수와 뇌의 대응) + R1(재귀 단계 조작). G1 필요(보유).

---

## 5. [BI-RV-5] 뇌처럼 공간 배치를 지키며 학습한 AI에서도 정서에 반응하는 구역이 따로 생길까?

* **자세한 질문:** 단위가 가상의 피질 표면에 배치되고 이웃끼리 비슷하게 반응하도록 제약된 지형 망을 쓴다.
  1. 정서 학습 없이도 정서 범주 선호 단위가 공간 군집을 이루는지 본다.
  2. 그 군집이 얼굴, 신체, 장면 선택 구역과 겹치는지 떨어져 있는지 본다.
  3. 같은 망에 정서 목표를 더해 미세조정하면 별도 군집이 생기는지 본다.
  4. 이 세 결과를 사람 복측과 외측 후두측두 피질의 정서 선호 voxel 위치와 대조한다. 사람 쪽은 MC의 fLoc localizer로 정의한 얼굴, 신체, 장면 영역과의 관계로 본다.
* **AI가 있어야만 가능한 이유:** 사람 피질이 다른 학습 목표로 발달했다면 어떤 지도가 생겼을지는 관찰할 수 없다. 지형 모델은 공간 제약을 유지한 채 학습 목표만 바꾼 "다른 발달 이력"을 준다(plan.md 2절 (a)). 지형 모델의 저자들도 같은 기제가 다른 피질 영역의 조직을 설명하는지 검증하는 것을 향후 과제로 남겼다(Margalit et al. 2024, doi:10.1016/j.neuron.2024.04.018, Discussion).
* **정서와 뇌에 대해 새로 알게 되는 것:** "정서 영역은 왜 그렇게 조직되는가"에 대한 계산적 설명을 시험한다. 시각피질의 정서 선호가 얼굴, 신체 구역의 부산물이라면 지형 모델(정서 학습 없음)과 같은 배치가 나온다. 정서 목표나 재진입 같은 추가 압력이 있어야 한다면, 정서 미세조정 판본과만 닮는다. 이는 Kragel 2019의 "시각계의 정서 schema"가 별도 조직인지, 범주 선택 구역에 얹힌 것인지에 답한다.
* **데이터:**
  * MC: fLoc, retinotopy, MT+, 언어 localizer가 있다(vision-decoding Round 1 0.1절, 논문 본문 기준). 보유 파일 포함 여부는 미확인.
  * NSD: fLoc ROI가 있어 모델 지도와 사람 범주 지도의 기본 정렬을 보정하는 데 쓴다.
  * Horikawa: localizer 포함 여부 미확인. HCP360 parcel 수준으로만 보조.
* **모델과 checkpoint:**
  * TDANN. checkpoint는 OSF(osf.io/64qv3)에, 코드는 `neuroailab/TDANN`(Zenodo 10.5281/zenodo.10294203)에 공개되어 있다. Margalit 2024의 Data and Code Availability 원문으로 확인했고, 라이선스는 미확인이다.
  * 대안: All-TNN(Lu et al. 2025, doi:10.1038/s41562-025-02220-7, checkpoint 공개 여부 미확인).
  * GPU: 공개 checkpoint 분석은 GPU 1장, 정서 미세조정은 GPU 1~4장에서 1~2일.
* **핵심 분석:**
  1. 모델 층의 단위별 정서 범주 선호를 구한다. 입력은 C&K 프레임, 측정은 범주 평정 가중 반응이다.
  2. 공간 자기상관(군집 지수)과 얼굴, 신체, 장면 선택 구역과의 거리를 잰다.
  3. 사람에서는 MC 피험자별로 정서 선호 지도와 fLoc 영역의 겹침, 거리를 같은 지표로 잰다.
  4. 정서 미세조정 판본과 비교한다.
* **예측:** 사람 정서 선호 voxel의 군집이 신체, 얼굴 구역과 겹치는 정도가 정서 학습 없는 지형 모델과 같으면 부산물 설명이다. 사람 쪽에 신체, 얼굴 구역 밖의 별도 군집이 있고 그것을 정서 미세조정 판본만 재현하면 추가 압력 설명이다.
* **반증 조건:** 사람 데이터에서 의미 캡션 통제 후 정서 선호 voxel의 공간 군집이 무작위 공간 순열과 구분되지 않으면, 시각피질의 정서 "구역" 자체가 없다. 이 경우 질문은 "정서 정보는 지형 조직 없이 분산되어 있다"는 결론으로 끝난다.
* **4주 계획:**
  * 1주: TDANN checkpoint 확보, C&K 프레임 반응 추출, MC localizer 정리
  * 2주: 모델 지형 분석, 사람 지도 계산
  * 3주: 정서 미세조정 판본 학습과 비교
  * 4주: 통계와 보고
  * 미세조정이 늦어지면 3주차를 공개 checkpoint 분석으로 줄인다.
* **가장 가까운 선행과 차이:**
  * Margalit et al. 2024(TDANN, 얼굴, 장면 등 범주 지형).
  * Lu et al. 2025(All-TNN).
  * Liu et al. 2024(비지형 망의 정서 선택 unit).
  * **차이:** 지형 모델에서 정서 선호 지도를 다루고 사람 localizer 기반 지도와 대조한 연구는 찾지 못했다.
  * 검색: WebSearch("topographic deep neural network emotion selectivity map emerges cortical organization emotional images face body scene patches TDANN All-TNN"), 2026-11-12.
* **주요 위험:**
  * 이번 목록에서 가장 무거운 질문이다(4주 경계).
  * 6명 MC의 localizer 보유 여부가 미확인이다.
  * 영상 프레임 정서는 얼굴, 신체 내용과 강하게 섞인다(의미 캡션 통제로 일부 대응).
  * 모델 피질 좌표와 사람 피질 좌표를 직접 맞출 수 없어 상대 지표(구역 간 거리, 겹침)만 비교한다.
* **표기:** label-provenance felt / 별도 평정자 규범. evidence-level R1(학습 목표 조작) + R0. G1 필요(보유).

---

## 6. [BI-RV-6] 사람마다 정서를 다르게 표상하는 이유를 서로 다르게 자란 AI들로 설명할 수 있을까?

* **자세한 질문:** 같은 구조의 모델을 학습 이력만 바꿔 여러 개 만든다.
  * (i) 무작위 초기값만 다르게
  * (ii) 학습 데이터 구성을 다르게(예: 얼굴, 사람 장면 비율)
  * (iii) 정서 라벨의 평정자 간 불일치를 흉내 낸 라벨 잡음을 다르게

  "인공 피험자 집단" 셋에서 34범주 각각의 표상이 개체 간에 얼마나 달라지는지 프로필을 만든다. 이것을 Horikawa와 MC 11명의 개인 간 정서 표상 차이 프로필(신뢰도 보정)과 비교한다.
* **AI가 있어야만 가능한 이유:** 사람의 학습 이력을 통제하거나 되돌릴 수 없다. 모델 집단은 "초기 조건만 다른 개체", "경험만 다른 개체", "가르침의 일관성만 다른 개체"를 따로 만든다. 그래서 개인차의 출처별 서명을 계산할 수 있다(plan.md 2절 (a)). 무작위 초기값만으로도 DNN 사이에 개인차가 생긴다는 결과(Mehrer et al. 2020, doi:10.1038/s41467-020-19632-w)가 출발점이다.
* **정서와 뇌에 대해 새로 알게 되는 것:** Horikawa 2020(공유된 범주 구조)과 Westlin 2025 preprint(arXiv:2507.00320, 개인별로 다른 군집, 범주 NMI 0.014)의 대립에 기제 수준의 해석을 준다.
  * 사람 개인차 프로필이 (i)과 닮으면, 정서 표상의 개인 특이성은 경험 차이 없이도 생기는 "발달 잡음"으로 설명된다.
  * (ii)와 닮으면 경험 의존(구성주의와 정합)이다.
  * (iii)과 닮으면 정서 개념 학습의 사회적 일관성 문제다.
  * 셋 다 아니면 시각 학습 밖의 요인(평가, 신체)이 개인차를 만든다.
* **데이터:**
  * Horikawa 2020(5명)과 MC(6명). 두 코호트는 스캐너와 획득 조건이 달라 코호트 안에서 따로 분석한다.
  * MC 시험 반복으로 개인 간 차이 중 측정 잡음 몫을 추정한다.
  * Horikawa는 반복이 없어 잡음 보정이 약하다.
* **모델과 checkpoint:**
  * ResNet-18 수준의 작은 망을 ImageNet 부분집합과 EmoSet으로 학습한다.
  * 조건별 10개체, 총 30개체. 개체당 GPU 1장에서 수 시간이라 4장이면 1주 안에 끝난다.
  * 대안으로 공개 seed 변이 checkpoint가 있으면 (i)에 쓴다(존재 미확인).
* **핵심 분석:**
  1. 개체마다 34범주 중심 RDM을 만든다.
  2. 범주별 개체 간 변동(leave-one-out 정렬 후)을 계산해 프로필을 만든다.
  3. 사람 쪽은 피험자별 RDM에서 같은 지표를 계산하고 잡음 상한으로 보정한다.
  4. 조건 (i), (ii), (iii) 프로필과 사람 프로필의 순위 상관을 비교한다.
* **예측과 반증:**
  * 사람 개인차 프로필이 세 조건 중 하나와 유의하게 더 닮으면 그 출처가 후보가 된다.
  * 어느 것과도 순열 기준을 넘지 못하면 "시각 학습 이력으로 설명되지 않는 개인차"라는 음성 결과다.
  * 사람 쪽 개인차 프로필 자체가 잡음 상한 아래면 질문을 판정할 수 없다. 이것이 1주차 게이트다.
* **4주 계획:**
  * 1주: 사람 개인차 프로필과 신뢰도(게이트)
  * 2주: 모델 집단 학습
  * 3주: 프로필 비교, 순열 검정
  * 4주: 코호트별 재현과 보고
* **가장 가까운 선행과 차이:**
  * Mehrer 2020: 시각 범주, seed만.
  * EEG에서 정서 평정 프로필 개인차(WebSearch 요약, 식별자 미확인).
  * **차이:** 학습 이력을 조작한 모델 집단의 개인차 서명과 사람 정서 fMRI 개인차 프로필을 비교한 연구는 찾지 못했다.
  * 검색: WebSearch("deep neural network instances random seed individual differences emotion representation compared to human individual differences fMRI emotion idiosyncrasy"), 2026-11-12.
* **주요 위험:**
  * 11명이라 개인차 프로필의 신뢰도가 낮을 수 있다(1주 게이트).
  * 코호트 차이(스캐너)가 개인차와 섞인다.
  * 모델 개체 간 차이는 "표상"의 차이이고 사람의 "경험" 차이가 아니다.
  * 정서 라벨은 규범 평정이라 참가자 본인 경험의 개인차를 직접 보지 못한다.
* **표기:** label-provenance felt / 별도 평정자 규범. evidence-level R1(학습 이력 조작) + R0. G1 필요(보유).

---

## 7. 여섯 질문의 관계와 착수 순서 제안

| 질문 | 조작하는 제약 | 묻는 사람 뇌 표지 | 4주 실현성(자체 판단) | 공유 자원 |
|---|---|---|---|---|
| BI-RV-1 | 재진입 되먹임 | 시각피질 정서 기하 | 높음 | EmoSet 학습 파이프라인, MC ceiling, 캡션 통제 |
| BI-RV-2 | 영역 이식(brain-tuning) | 영역별 정서 구조의 충분성 | 중간 | 영역 신뢰도, 보류 집합 |
| BI-RV-3 | 피질하 지름길 | 편도체 범주 프로필 | 중간(피질하 게이트) | BI-RV-1과 같은 정서 모듈 |
| BI-RV-4 | 재귀 깊이 | 정서 정보의 경사 위치 | 높음 | CORnet, 캡션 통제 |
| BI-RV-5 | 지형 배치 | 정서 선호 구역의 위치 | 낮음~중간 | TDANN checkpoint, MC localizer |
| BI-RV-6 | 학습 이력 | 개인차 프로필 | 중간(1주 게이트) | 작은 망 학습 파이프라인 |

* **1주차 공통 작업:**
  * MC 보유본 전처리 형식 확인
  * ROI 추출과 noise ceiling
  * 캡션 embedding 통제 변수
  * EmoSet 중복 검사
  * 피질하 signal-feasibility
  * 여섯 질문이 이 기반을 함께 쓴다.
* **권고:** BI-RV-1과 BI-RV-4를 먼저 시작한다. 둘 다 같은 시각 망과 정서 판독을 쓰고 1주차부터 실행할 수 있다. 하나는 연결(되먹임)을, 다른 하나는 깊이(재귀)를 조작한다. BI-RV-3은 BI-RV-1의 정서 모듈을 재사용하므로 피질하 게이트를 통과하면 바로 붙인다.

## 8. 기존 질문과의 관계와 겹침

* BI-RV-1은 RQ-54를, BI-RV-2는 RQ-56을 대체한다.
* BI-RV-3은 Round 2의 BI-P3, SN-P3, VD-P5와 같은 피질하 주제다. 차이는 관찰 경로 분석이 아니라 모델 조작이 만든 범주 의존 지도를 쓴다는 점이다.
* BI-RV-6은 GI-P5(개인 잔차 multiverse)와 개인차 주제를 공유한다. 이쪽은 개인차의 "출처"를 모델 집단으로 묻는다.
* overlap 표시(`reference/existing_projects.md` 기준):
  * BI-RV-2: overlap: EmoBrain(뇌 정서 정보를 모델 학습에 사용)
  * BI-RV-1, BI-RV-4, BI-RV-5: overlap: EmoViS(정서 기하의 감각-의미 기원과 부분 겹침)
  * BI-RV-3, BI-RV-6: 없음

## 9. 검색 기록 (모두 2026-11-12)

| 질문 | 질의(경로) | 결과 |
|---|---|---|
| BI-RV-1 | WebSearch "recurrent feedback from valence or amygdala module to visual network deep learning model reentry emotional images compared with visual cortex fMRI emotion representation" | 되먹임 연결을 조작한 모델과 사람 시각피질 정서 기하 대조는 미발견. 인접: Liu 2024, Liu 2025 VCA, Jang & Kragel 2025, Bo 2021, VSS 초록(search_index) |
| BI-RV-2 | WebSearch "brain-tuning fine-tune vision or video model on amygdala or emotion-related fMRI responses improves human emotion judgment alignment" | 정서 영역 brain-tuning은 미발견. 인접: Policzer 2025(STS), Moussa 2024, Algonauts 2025 보고(arXiv:2510.06235) |
| BI-RV-3 | Round 2와 재점검의 WebSearch 2회, api.crossref.org, 위 BI-RV-1 질의 | 지름길 조작 모델의 범주 의존 지도와 사람 편도체 프로필의 대조는 미발견 |
| BI-RV-4 | WebSearch "recurrent processing required for recognizing emotion in complex images late-solved emotional scenes recurrent neural network time steps social emotions" | 정서 재귀 요구량과 fMRI 경사의 연결은 미발견. 인접: CogSci 2020 동적 표정 재귀(search_index) |
| BI-RV-5 | WebSearch "topographic deep neural network emotion selectivity map emerges cortical organization emotional images face body scene patches TDANN All-TNN" | 지형 모델의 정서 선호 지도는 미발견 |
| BI-RV-6 | WebSearch "deep neural network instances random seed individual differences emotion representation compared to human individual differences fMRI emotion idiosyncrasy" | 미발견. 인접: Mehrer 2020 |
| 서지 확인 | api.crossref.org: Kar 2019, Mehrer 2020, All-TNN 2025. export.arxiv.org ID 조회: arXiv:1909.06161, arXiv:2410.09230. PMC 전문(이전 라운드 저장본): TDANN 코드와 checkpoint 위치 | 6편(arXiv:2510.06235 포함)을 literature.jsonl에 추가 |

Stage 2 표본에서 "no" 판정의 약 25%가 실제로는 선행 수행이었다. 그러므로 위 "미발견"은 이 검색 경로 안의 결과이고, 상위 후보로 오르면 선행 중복 감사를 다시 해야 한다.

## 10. 미확인 사항

1. MC 보유본의 전처리 형식, localizer와 캡션 포함 여부. 그리고 두 Horikawa 코호트의 피험자 중복 여부.
2. EmoSet, TDANN, CORnet, Leem 2026 코드, torchvision 가중치의 라이선스. GitHub와 Hugging Face가 차단되어 확인하지 못했다.
3. All-TNN checkpoint 공개 여부. 공개 seed 변이 checkpoint의 존재 여부.
4. Liu et al. 2025 VCA 모형에 시각 망으로 가는 되먹임이 있는지(본문 미열람). BI-RV-1의 새로움 판정에 직접 영향을 준다.
5. VSS 초록("The Origin of Affect-specific Neural Representations of Emotional Scenes in Early Visual Cortex")과 CogSci 2020 재귀 표정 논문의 식별자. 둘 다 search_index 수준이다.
6. 각 질문의 GPU 시간은 공개 보고와 일반 경험에 근거한 추정이며 실측이 아니다.
