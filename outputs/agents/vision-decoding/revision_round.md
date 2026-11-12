# 재탐색 라운드: vision-decoding (D2 주담당)

* 에이전트: vision-decoding
* 기준일: 2026-11-12
* 지시: `outputs/revision/plan.md`(전체를 직접 읽음), Coordinator 위임 메시지
* 담당: (A) 출발점 RQ-53 다시 쓰기, (B) D2 "공개 뇌 decoding 모델 + emotion head"에서 새 질문
* 읽은 자료: plan.md, `outputs/combinations/rq_table.md`의 RQ-53 원문, `outputs/rq_landscape.md` K9, `outputs/evaluation/reviewer_notes.md`의 RQ-53 지적, EmoMind 원문(arXiv:2605.16739, Round 1에서 받은 arXiv HTML 전문), 공개 저장소 4곳의 README와 LICENSE(아래 0.2절)
* 표기: [본문] 원문 직접 확인, [초록], [저장소] 공개 저장소 파일 직접 확인, [DB] `literature_db.csv` verified 항목. label-provenance와 evidence-level은 axis_encyclopedia 0.2절 형식

---

## 0. 공통 전제

### 0.1 한 문장 요약

정서를 한 번도 학습하지 않은 공개 뇌 decoder는 "뇌가 이 장면을 어떻게 표상했는가"를 자극과 같은 특징 공간에 그려 준다. 그래서 **같은 정서 head를 자극 쪽 표상과 뇌 쪽 표상에 각각 붙여 그 차이를 재면, 뇌가 자극 너머로 더한 정서를 잴 수 있다.** 관찰만으로는 이 차이를 잴 수 없다. 이 차이를 정서 정보의 양(VD-RV-A), 방향(VD-RV-1), 출처 영역(VD-RV-2), 언어로 된 기술과 회상(VD-RV-3)의 네 측면으로 나눠 묻는다.

### 0.2 공개 저장소에서 직접 확인한 것 (2026-11-12, shallow clone 후 텍스트만 읽음, 실행 없음)

| 대상 | 확인 내용 |
|---|---|
| MindEye2 (github.com/MedARC-AI/MindEyeV2) | 코드 **MIT License**(LICENSE 파일). 사전학습 checkpoint는 Hugging Face `pscotti/mindeyev2`의 `train_logs`에 있다. `final_multisubject_subj0#`은 해당 피험자를 뺀 NSD 7명 사전학습 모델이다. 전체 학습은 8xA100 80GB 기준이고, 단일 GPU에서는 hidden_dim 축소를 권한다(README). 가중치 자체의 라이선스 문구는 README에 없다. 학습 데이터가 NSD이므로 NSD 약관을 따른다고 보는 것이 안전하다 |
| Brain-IT (github.com/WeizmannVision/brainit-fmri) | checkpoint는 Hugging Face `RomanBeliy/Brain-IT`에 있다. 새 피험자 적응 스크립트(`train_transfer/`)가 공개되어 있다. README는 이 스크립트를 NSD 보류 피험자용으로 설명하면서 "다른 데이터셋으로 쉽게 바꿀 수 있다"고 적었다. **LICENSE 파일이 없다.** README는 arXiv 기록의 라이선스(Brain-IT 논문은 CC BY-NC-SA 4.0)를 따르라고 한다. 따라서 비상업 연구 용도로만 본다. Stage 2(diffusion) 학습은 H200 2장 또는 H100 4장이 필요하다 |
| Brain-Diffuser (github.com/ozcelikfu/brain-diffuser) | **MIT License**. ridge만 학습한다 |
| Mind captioning 코드 (github.com/horikawa-t/MindCaptioning) | **LICENSE 파일 없음.** 캡션 원문 `data/caption/caption_ck20.csv`가 저장소에 있다(43,920개, 비디오 2,196개 x 20개). figshare 전처리본 형식(README): 학습 2,108샘플, 지각 테스트 [72 x 5회 반복], 회상 [72 x 5회]. 반복이 평균되지 않은 형식이다 |
| MC 원자료 (OpenNeuro ds005191) | **CC0**. events.tsv에 회상 시행별 vividness, accuracy가 있다(Round 3 확인) |

캡션 중 정서 관련 단어(happy, sad, scream, cry, cute 등의 간이 사전)가 들어간 비율은 약 5.5%(2,412/43,920)였다. 간이 집계이며 plan.md 4절의 "정서 표현이 드물다"와 맞는다.

### 0.3 plan.md 4절 함정 점검표 (모든 질문 공통)

| 함정 | 이 문서의 처리 |
|---|---|
| EmoNet 누수 | 쓰지 않는다. 이미지 쪽 정서 head는 (a) C&K 평정으로 자극 쪽 feature에서 교차검증 학습한 head와 (b) C&K와 독립인 EmoSet(arXiv:2307.07961 [본문])으로 학습한 head 두 가지만 쓴다. 텍스트 쪽은 GoEmotions(arXiv:2005.00547, Reddit 텍스트)로 학습한 탐침을 쓴다 |
| MC 시험 클립 72개 | 적응과 head 학습은 MC 학습 2,108개로만 한다. 72개는 시험과 반복, 회상 분석에만 쓴다 |
| 무음 | 모든 질문이 시각 decoder만 쓴다. 소리 관련 주장은 하지 않는다 |
| MC 보유본 전처리 형식 미확인 | figshare 형식(4 s shift 블록 평균, 반복 비평균)을 기준으로 설계하고, 1주차에 보유본과 대조한다 |
| 캡션의 정서 배제 지시와 GPT-3.5 교정 | VD-RV-3에서 이것을 오히려 기준선으로 쓴다(정서를 빼라고 한 사람의 기술 대 뇌에서 읽은 기술). 교정 과정이 정서 어휘를 줄였을 가능성은 위험으로 적는다 |
| Westlin 2025 | 군집 구조는 다루지 않는다. 결과는 클립 수준 회귀와 방향 검정으로만 낸다 |
| 라벨 주체 | C&K 평정은 felt / 별도 평정자 규범이다. 참가자 본인 보고와의 연결은 NSD nsdmeadows(100장, 참가자 본인으로 보이나 지시문 미확인)에서만 탐색적으로 한다 |
| TRIBE v2 | 쓰지 않는다. 자극 구동 null은 피험자별 encoding model로 만든다 |
| VLM, MLLM 오염 | 생성 MLLM은 쓰지 않는다. CLIP 계열의 오염 가능성은 남으므로, 자극 쪽 head와 뇌 쪽 head가 같은 CLIP을 공유하는 대조 설계로 상쇄한다 |
| 선행 판정 | 질문마다 검색 질의, 날짜, 식별자를 적는다 |

---

## 1. 출발점 RQ-53 진단과 다시 쓰기

### 1.1 원래 질문
"정서와 상관없는 영상으로 사람들의 뇌를 맞춰도 정서 구조까지 맞춰질까?" 저정서 클립으로만 학습한 피험자 간 정렬(hyperalignment, SRM)이 고정서 클립의 정서 기하를 운반하는지, 운반되지 않는 성분은 별도 정렬 차원을 요구하는지 물었다. 데이터는 Horikawa와 MC, 근거는 VLM 사이 정서 vector 운반(arXiv:2609.34742 [DB])이었다.

### 1.2 왜 약했는가

| 새 기준 | 진단 | 점수 추정 |
|---|---|---|
| AI-enabled Affective Neuroscience Contribution | **낮음.** (1) 핵심 도구가 고전적 hyperalignment, SRM이다. AI가 관찰로 얻을 수 없는 비교 대상을 주지 않았다. (2) "정서 무관 정렬"을 C&K 안의 저정서 클립으로 정의했는데, C&K는 정서 유발 클립 모음이라 저정서가 상대적 정의로만 성립한다(reviewer_notes.md). 저정서 클립과 고정서 클립은 내용도 달라, 운반 실패가 정서 때문인지 내용 차이 때문인지 가를 수 없다. (3) 정렬이 정서를 운반하더라도, 그것이 같은 장면 내용을 공유해서인지(Doerig 2025, doi:10.1038/s42256-025-01072-0 [DB]) 뇌가 정서를 더해서인지 구분하는 자극 쪽 비교 대상이 없었다. 결국 "정렬 방법이 얼마나 일반화되는가"에 대한 답이 되고, 정서에 대해 새로 말해 주는 것이 적다 | 2/5 |
| 1-month Feasibility | **높음.** 계산이 가볍다. 다만 가볍다는 것이 그대로 Horikawa 재분석이라는 비판의 이유이기도 했다 | 4/5 |

**고칠 점.** "정서와 무관한 정렬"을 C&K 안에서 찾지 말고 밖에서 가져온다. **NSD의 일상 장면 수만 장으로 다른 사람 7~8명의 뇌를 묶은 공개 decoder의 공유 표상**이 그것이다. 이것은 정서를 한 번도 보지 않은 정렬이다. 이것을 Horikawa와 MC 피험자에 붙인 뒤 자극 쪽 표상과 같은 정서 head로 비교하면, 원래 질문(정서 무관 정렬이 정서를 운반하는가)에 "뇌가 자극 너머로 무엇을 더하는가"라는 축이 생긴다.

### [VD-RV-A] 정서를 한 번도 배우지 않은 뇌 해독기로 다른 사람의 뇌를 읽어도 감정이 읽힐까, 그리고 그 감정은 장면 자체에는 없는 것일까?

* **자세한 질문**
  * NSD 일상 장면으로만 학습된 공개 decoder(MindEye2 다피험자 사전학습 모델의 공유 latent, 보조로 Brain-IT의 기능 군집 token)를 Horikawa 5명과 MC 6명에 붙인다. 피험자별 입력층만 학습하고 공유 부분은 고정한다.
  * 첫째 질문: 이 "정서 무관 공유 표상"에서 C&K 34범주와 14차원 규범 평정이 얼마나 읽히는가.
  * 둘째 질문(핵심): 같은 선형 정서 head를 (i) 실제 자극 프레임의 표상(decoder의 목표 공간인 OpenCLIP 표상)에 붙인 경우와 (ii) 뇌에서 해독한 표상에 붙인 경우를 비교한다. **(ii)가 (i)을 넘어 규범 평정을 더 설명하는 몫**이 있는가. 그 몫이 자극 구동 null(아래)보다 큰가.
  * 셋째 질문(원래 RQ-53의 계승): 넘는 몫이 있다면, 공유 표상에 정서 지도학습 저차원 축(rank 1~4)을 하나 더했을 때 피험자 간 전이가 좋아지는가. 좋아지면 "정서는 일반 시각-의미 정렬과 다른 별도 공유 차원을 필요로 한다", 그렇지 않으면 "정서는 일반 정렬에 실려 간다"로 판정한다.
* **AI가 있어야만 가능한 이유**
  * (a) 관찰로는 만들 수 없는 통제 대상이 있다. "정서를 한 번도 본 적 없는, 다른 사람들의 뇌로 학습한 정렬"이다. 같은 사람들에게 정서 없는 장면 수만 장을 보여 주는 실험은 이미 NSD에 있고, 그 정렬은 학습된 모델 안에만 존재한다.
  * (b) 측정할 수 없던 변수를 계산한다. "뇌가 표상한 장면"과 "실제 장면"을 같은 특징 공간에 놓아야 둘의 차이를 잴 수 있다. decoder 없이는 뇌 표상을 자극 공간으로 옮길 방법이 없다.
* **정서와 뇌에 대해 새로 알게 되는 것**
  * 시각계의 정서 정보가 자극 특징의 재표현인지(Kragel 2019 "emotion schemas embedded in the visual system", doi:10.1126/sciadv.aaw4358 [본문]), 뇌가 덧붙인 것인지(affective realism, doi:10.1177/0956797617741718 [초록]) 처음으로 같은 척도에서 나뉜다.
  * 정서 무관 정렬이 정서를 운반하면, Westlin 2025(arXiv:2507.00320 [본문])가 강조한 개인 특이성과 별개로 "사람들이 공유하는 일반 시각 부호 위에 정서가 실린다"는 증거가 된다. 별도 축이 필요하면 정서가 일반 부호와 다른 공유 차원을 가진다는 증거가 된다. 기본정서이론이든 구성주의든 "정서가 지각 부호와 분리된 표상인가"에 답해야 하므로 두 쪽 모두에 관련된다.
* **데이터**
  * Horikawa 2020: 보유, 원본 비디오 보유, 블록 평균 native volume 전처리본, HCP360 ROI 제공(Stage 1).
  * MC: 보유, 전처리 완료. 학습 2,108, 테스트 72 x 5회(figshare 형식 기준).
  * NSD: 보유. decoder 사전학습 출처이고, 1주차 sanity check와 nsdmeadows 탐색에 쓴다.
  * 라벨: C&K 34/14(felt / 별도 평정자 규범). EmoSet(정서 head 독립 학습용, 공개 조건 미확인).
* **모델과 checkpoint**
  * MindEye2 `final_multisubject_subj0#`: 공개 [저장소], 코드 MIT, 가중치는 NSD 약관을 따름(추정, 문구 미확인).
  * Brain-IT stage-1 decoder(CLIP, VGG 분기): 공개 [저장소], LICENSE 파일 없음, 비상업 용도. Stage 2 diffusion은 쓰지 않는다.
  * OpenCLIP ViT-bigG/14(MindEye2 목표 공간): 공개.
  * GPU: 피험자 입력층만 학습하고 backbone과 prior는 고정하므로 A100 80GB 1장이면 된다(전체 학습은 8xA100이지만 쓰지 않음). 피험자 11명 x 2개 적응 방식이다.
* **핵심 분석, 예측, 반증 조건**
  1. **적응 두 방식.** (i) 표준: 자극 프레임의 OpenCLIP 목표로 입력층 학습. (ii) 정서 경량: 저수준 목표만 사용(MindEye2 blurry 저수준 분기 또는 Brain-IT VGG 분기). (ii)는 적응 단계로 정서가 들어갈 경로를 줄인다.
  2. **자극 구동 null.** 같은 피험자에서 자극 feature(OpenCLIP, 저수준, 움직임 에너지)로 voxel별 encoding model을 학습한다. 이 모델이 예측한 "합성 뇌 반응"에 실측과 같은 잡음 수준(MC 반복으로 추정)을 더해 같은 decoder에 통과시킨다. 이 경로가 만드는 "자극 너머 정서 몫"이 null 분포다. decoder의 NSD 중립 prior로 인한 수축도 null에 그대로 들어간다.
  3. **증분 지표.** 클립별로 head(뇌 해독 표상)를 head(자극 표상)와 직전 클립 head 출력(순서 이월 nuisance)에 대해 회귀한 잔차가 C&K 평정을 추가로 설명하는 정도. 교차검증은 원본 영상 단위 그룹 fold로 한다.
  4. **예측.** H1 정서 무관 표상에서 정서가 읽힌다(자극 경로로 당연히 예상됨). H2 실측의 증분이 null 증분보다 크다(뇌가 더함). H3 증분은 arousal과 위협 관련 범주(fear, horror, anxiety)에서 크다(affective realism과 편도체 재진입 예측, doi:10.1093/cercor/bhaa411 [초록]).
  5. **반증.** 두 적응 방식 모두에서 실측 증분이 null 증분과 같으면, 이 decoder 공간에서 정서는 자극이 가진 만큼만 실린다. 정서 축을 더해도 피험자 간 전이가 좋아지지 않으면 별도 차원 가설은 기각된다.
  6. **탐색(개인 경험 연결).** NSD 8명의 shared1000 중 nsdmeadows 100장(참가자 본인 평정으로 보임, 지시문 미확인)에서 같은 증분이 그 참가자의 평정 편차(본인 - 다른 참가자 평균)와 관련되는지 본다. 100장, 8명이므로 효과 크기 추정만 한다.
* **4주 계획**
  * 1주: 보유 MC 전처리본과 figshare 형식 대조, 비디오 프레임 추출과 OpenCLIP 임베딩, 시각 ROI 마스크, MindEye2 checkpoint 적재와 NSD 보류 피험자 1명으로 파이프라인 sanity check.
  * 2주: 11명 x 2개 적응 방식 학습, MC 72클립 retrieval 정확도로 적응 품질 확인(반복 평균 vs 단일 반복).
  * 3주: 자극 쪽 head와 뇌 쪽 head 학습(C&K 교차검증, EmoSet 독립), 자극 구동 null 생성, 증분 검정, 정서 축 추가 비교.
  * 4주: 코호트 간 재현(MC에서 학습한 head를 Horikawa에 적용하고 그 반대), nsdmeadows 탐색, 결과 정리.
* **가장 가까운 선행과 차이**
  * EmoMind(arXiv:2605.16739) [본문]: MC 6명의 피험자별 PCA + ridge로 34차원 C&K 벡터를 **직접 지도학습**하고, 중립 캡션 retrieval과 rewriter로 정서 캡션을 만든다. Horikawa 2020은 교차 데이터셋 평가에만 쓴다(4.1절, 부록 A.4). 비교군은 정답 라벨을 받은 GPT-4이고, 합성 뇌(TRIBE)로 바꿔 넣는 시험을 한다. **차이:** (1) 우리는 decoder 학습에 정서 라벨을 쓰지 않는다(NSD에서 학습된 정서 무관 공유 표상). (2) 자극 쪽 표상에 같은 head를 붙인 대조와 자극 구동 null로 "뇌가 더한 정서"를 따로 잰다. EmoMind에는 이 대조가 없다. (3) 출력은 텍스트가 아니라 특징 공간의 정서 증분이다. (4) 별도 정서 축 검정이 있다.
  * Xing 2026(arXiv:2609.34742) [DB]: VLM 사이에서 정서 무관 정렬이 정서 vector를 운반한다. 모델 사이 결과이고 뇌는 없다.
  * Afrasiyabi 2024(arXiv:2410.00047) [본문]: Horikawa 5명 + 새 3명으로 정서 단어 cue 심상을 시각화했다. decoder를 정서 라벨로 묶어 학습했고 평가는 정성 수준이다.
  * 검색(2026-11-12): WebSearch "MindEye2 OR Brain-IT pretrained fMRI decoder latent emotion probe valence Natural Scenes Dataset transfer to emotional videos 2025 2026", WebSearch "brain decoding image reconstruction emotion evaluation valence of reconstructed images fMRI 2026", WebSearch "fMRI decoded visual representation biased toward emotional content affective realism neural decoding perceptual distortion emotional scenes decoder bias". NSD 학습 decoder에 정서 head를 붙이거나 자극 쪽 head와 대조한 연구는 찾지 못했다. **판정: no(검색 범위 내), 구성 요소는 partially**(정서 무관 정렬 운반은 모델 사이에서 Xing 2026, 정서 decoding 자체는 EmoMind)
* **주요 위험**
  * 3T 블록 평균(Horikawa TR 2 s, MC TR 1 s)과 NSD 7T single-trial beta 사이의 domain shift로 적응 품질이 낮을 수 있다. 2주차 retrieval 정확도가 우연 수준에 가까우면 Brain-Diffuser식 ridge 재학습(MIT)으로 내려간다. 그 경우 "NSD 정렬" 성격은 약해진다.
  * 비디오 1개를 프레임 표상 하나로 요약하면 움직임이 운반하는 정서가 빠진다. 다중 프레임 평균과 움직임 에너지 nuisance로 줄인다.
  * 자극 구동 null은 encoding model의 feature 공간에 묶인다. feature 공간이 놓친 자극 정보는 "뇌가 더한 것"으로 잘못 분류된다. feature를 OpenCLIP, 저수준, 움직임으로 넓히고 null의 feature 집합을 바꿔 결과가 유지되는지 본다.
  * CLIP의 사전학습 오염(C&K GIF가 웹에 공개됨). 자극 쪽과 뇌 쪽이 같은 CLIP을 쓰므로 오염은 증분 비교에서 상쇄되지만, H1의 절대값 해석에는 남는다.
  * label-provenance: felt / 별도 평정자 규범. evidence-level: R0(실측), null은 R1. 결론은 규범 정서 수준이다.
  * overlap: EmoBrain(cross-subject 정서 decoding과 부분)

---

## 2. D2 새 질문

### [VD-RV-1] 뇌는 감정이 실린 장면을 실제보다 더 감정적으로 보고 있을까?

* **자세한 질문**
  * VD-RV-A와 같은 파이프라인에서, 뇌에서 해독한 표상과 실제 자극 표상의 **차이 벡터**를 구한다. 그 차이를 정서 방향(자극 쪽 head의 가중치 방향, EmoSet head 방향)에 투영한다.
  * 질문: 이 투영값이 클립의 규범 정서 강도와 같은 방향으로 커지는가(정서 일치 과장, affective realism). 아니면 반대로 작아지는가(정서 약화). 그 크기가 자극 구동 null을 넘는가.
  * 확장 1: MC 회상에서 같은 차이를 구한다. 회상한 장면은 실제보다 더 정서 쪽으로 기우는가.
  * 확장 2: NSD nsdmeadows에서 개인의 차이 투영값이 그 사람의 평정 편차와 같은 방향인가(탐색).
* **AI가 있어야만 가능한 이유**
  * affective realism은 지금까지 행동으로만 검증되었다(doi:10.1177/0956797617741718 [초록], 중립 얼굴 판단). 신경 수준에서 "더 정서적으로 표상했다"를 말하려면, 뇌 표상을 자극과 같은 공간에 놓고 차이의 방향을 재야 한다. 정서를 모르는 decoder가 그 공간 사상을 준다.
  * decoder 자체의 편향(NSD 중립 장면 prior로의 수축)은 합성 뇌 null로 따로 떼어 낼 수 있다. 이것도 모델이 있어야 가능한 대조다.
* **정서와 뇌에 대해 새로 알게 되는 것**
  * affective realism(정서가 지각 내용 자체를 바꾼다)과 "지각은 정서 중립이고 정서는 뒤에서 덧붙는다"는 견해를 신경 표상 수준에서 대비한다.
  * 정서 장면이 지각적으로 더 생생하다는 EEV 결과(doi:10.3389/fnbeh.2013.00040 [초록], 편도체와 시각피질)가 표상 내용의 "과장"인지 신호 강도의 증가인지 구분한다. 과장이면 방향이 정서 쪽으로 기울고, 신호 증가면 크기만 커지고 방향은 그대로다.
  * 회상 확장은 NEVER(doi:10.3758/s13423-017-1313-9 [본문])의 "부정 기억의 감각 재현 강화"를 방향의 언어로 바꾼다. 기억이 정서를 과장해 저장하는지에 대한 신경 증거가 된다.
* **데이터**: VD-RV-A와 같다. MC 회상 72클립 x 5회(눈 감음, 시행별 vividness 보유). nsdmeadows 100장(NSD 보유, 지시문 미확인).
* **모델과 checkpoint**: VD-RV-A와 같다. 시각화(선택)에는 MindEye2 SDXL unCLIP(공개)을 쓴다. unCLIP 가중치 자체의 라이선스는 미확인이고, 기반 모델 SDXL 1.0은 CreativeML Open RAIL++-M이다(Brain-IT 저장소에 포함된 generative_models 문서의 언급 기준). 시각화 이미지 생성은 72클립 x 11명 규모라 A100 1장으로 하루 이내다.
* **핵심 분석, 예측, 반증 조건**
  1. 차이 투영 d = proj(뇌 해독 표상 - 자극 표상). 클립별로 실측 d와 null d(VD-RV-A의 합성 뇌)를 구한다.
  2. 주 검정: (실측 d - null d)와 규범 정서 강도(C&K 범주 선택 비율의 최댓값, 14차원 arousal)의 상관. 피험자별 순열 검정과 Bayesian prevalence.
  3. 방향 검정: 차이 벡터가 정서 head 방향과 이루는 각이 무작위 방향, 비정서 개념 방향(물체 범주, 장면 범주 head)과 비교해 유의하게 정서 쪽인가. 이 대조가 없으면 "모든 방향으로 커진 잡음"을 과장으로 오인한다.
  4. 예측: 위협 관련 범주와 고arousal에서 양의 과장. 미적, 고요 범주에서는 과장이 없거나 약화.
  5. 반증: 실측 d가 null d와 같거나 정서 반대 방향이면 affective realism의 표상 수준 예측은 이 데이터에서 지지되지 않는다. 방향 검정에서 정서 방향이 비정서 방향보다 특별하지 않으면 "과장"이 아니라 일반 왜곡이다.
  6. 시각화(선택, R2): 실측 뇌와 null 뇌에서 재구성한 이미지 쌍을 새 평정자에게 "어느 쪽이 더 정서적인가"로 묻는다. 측정은 1~5번이 하고 이것은 보조다.
* **4주 계획**: 1~2주는 VD-RV-A와 공유한다. 3주: 차이 투영, null, 방향 검정. 4주: 회상 확장(회상 SNR에 맞춘 null), nsdmeadows 탐색, 선택적 재구성 시각화.
* **가장 가까운 선행과 차이**
  * affective realism 행동 연구(Siegel 2018, doi:10.1177/0956797617741718), EEV fMRI(Todd 2013, doi:10.3389/fnbeh.2013.00040): 신경 표상 내용의 방향은 재지 않았다.
  * 시각피질 정서 decoding과 편도체 재진입(Bo 2021, doi:10.1093/cercor/bhaa411 [초록]): 정서 범주가 읽히는지만 보았고, 자극 대비 기울기는 보지 않았다.
  * EmoMind(arXiv:2605.16739) [본문]: 뇌에서 해독한 정서를 캡션에 주입한다. 자극 대비 기울기라는 개념이 없다.
  * 검색(2026-11-12): PubMed `(emotion-enhanced vividness OR "affective realism" OR "emotionally enhanced") AND (perception OR visual cortex)` 2009~ (9건, 행동과 활성 연구뿐), WebSearch "fMRI decoded visual representation biased toward emotional content affective realism neural decoding perceptual distortion emotional scenes decoder bias". **판정: no(검색 범위 내).**
* **주요 위험**
  * 회귀 decoder는 평균 쪽으로 수축한다. 강한 정서 클립일수록 NSD 중립 prior 쪽으로 더 끌려가므로 기본 예측은 "약화"다. 이것을 null이 정확히 재현하지 못하면 결론이 뒤집힌다. null의 잡음 수준을 MC 반복으로 맞추고, null 대비가 아니라 null과의 차이로만 해석한다.
  * 정서 방향을 C&K head로 정의하면 그 head가 학습한 자극 쪽 상관(예: 어두운 화면 = 공포)이 방향에 들어간다. EmoSet 독립 head와 결과를 대조한다.
  * nsdmeadows는 100장, 8명이고 지시문(felt vs perceived)이 미확인이다. 개인 연결은 탐색으로만 보고한다.
  * label-provenance: felt / 별도 평정자 규범(주), nsdmeadows는 참가자 본인으로 보임(탐색). evidence-level: R0, 시각화 평정은 R2.

### [VD-RV-2] 감정 정보는 눈에 들어온 직후의 시각 영역부터 실려 있을까, 아니면 뇌의 다른 곳에서 덧입혀질까?

* **자세한 질문**
  * VD-RV-A의 "자극 너머 정서 몫"과 VD-RV-1의 "정서 쪽 기울기"를 입력 영역과 표상 수준별로 나눈다.
  * 입력 영역: 초기 시각(V1~V3), 고차 시각(복측, 외측 후두측두), 고차 시각 + 편도체, OFC, 섬엽. 영역별로 decoder 입력층을 따로 적응시킨다(Brain-IT은 기능 군집 token을 영역별로 마스킹).
  * 표상 수준: 저수준 분기(Brain-IT VGG 특징, MindEye2 저수준 분기)와 의미 분기(CLIP 특징)를 따로 해독한다. "뇌가 더한 정서"가 색, 대비 같은 저수준 이미지 특징에 실리는지, 장면 의미에 실리는지를 본다.
  * 동역학: MC 72클립의 노출 이력(최대 11회)에 따라 초기 시각피질의 기울기가 편도체 반응과 함께 줄어드는지 본다.
* **AI가 있어야만 가능한 이유**
  * 영역별 decoding 정확도는 관찰로도 잴 수 있다. 그러나 "자극 너머" 몫과 그 방향을 영역별, 표상 수준별로 비교하려면 모든 영역을 같은 특징 공간으로 옮겨 주는 decoder가 필요하다.
  * 저수준과 의미 특징을 따로 예측하는 두 분기 구조(Brain-IT) 덕분에 "어느 수준의 시각 표상에 정서가 덧입혀지는가"를 직접 물을 수 있다. 같은 분기를 자극에 적용한 값이 기준선이 된다.
* **정서와 뇌에 대해 새로 알게 되는 것**
  * 두 설명을 가른다. **피드포워드 스키마 설명**(Kragel 2019: 시각 위계가 정서 스키마를 계산한다)은 고차 시각에서 정서 정보가 읽히지만 자극 너머 기울기는 작다고 예측한다. **재진입 설명**(Bo 2021: 편도체→복측 시각피질 effective connectivity가 불쾌 decoding을 예측한다, Todd 2013: 편도체와 시각피질의 EEV)은 초기 시각피질에도 정서 쪽 기울기가 있고, 그 기울기가 시행별 편도체 반응과 함께 변하며, 반복으로 편도체가 습관화되면 함께 줄어든다고 예측한다.
  * 저수준 분기에서 기울기가 나오면 "뇌가 정서 장면의 색과 대비까지 다르게 표상한다"는 뜻이다. 이는 지각적 생생함 효과의 표상 수준 기제다.
* **데이터**
  * MC가 주 데이터다. TE 30 ms로 Horikawa(TE 43 ms, systems-neuro 판정)보다 편도체, OFC 신호 조건이 유리할 가능성이 있다. 72클립 x 5회 반복과 노출 이력이 있다. MC 논문은 retinotopy와 fLoc로 LVC, HVC를 정의했다. 보유본에 ROI 파일이 있는지는 미확인이므로 없으면 HCP360 atlas로 대체한다.
  * Horikawa는 같은 72클립을 1회만 본 재현 코호트다.
  * 피질하 ROI는 signal-feasibility 관문(영역별 tSNR, dropout 지도)을 통과해야 쓴다.
* **모델과 checkpoint**: Brain-IT stage-1 두 분기(공개, 비상업), MindEye2 저수준 분기(공개, MIT 코드). 영역별 적응은 피험자 x 영역 4개 x 분기 2개라 GPU 시간이 VD-RV-A의 약 4배다. 입력층만 학습하므로 A100 1~2장으로 4주 안에 가능하다.
* **핵심 분석, 예측, 반증 조건**
  1. 영역 x 분기별 자극 너머 정서 몫과 정서 쪽 기울기(VD-RV-A, VD-RV-1 지표).
  2. 고차 시각 대비 "고차 시각 + 편도체, OFC, 섬엽"의 증분. 측정 오차 위양성(doi:10.1371/journal.pone.0152719 [DB])을 줄이려고 영역 voxel 수를 맞춘 무작위 voxel 대조를 둔다.
  3. 시행별 결합: MC 테스트 반복별로 편도체 반응 크기와 초기 시각피질 기울기의 개인 내 상관. 노출 회차를 공변량으로 둔다.
  4. 예측(재진입 설명): 초기 시각 기울기 > 0, 편도체 반응과 양의 상관, 반복에 따라 감소. 예측(피드포워드 설명): 초기 시각 기울기 ≈ null, 정서 정보는 고차 시각 의미 분기에서 대부분 자극 몫.
  5. 반증: 어느 영역, 어느 분기에서도 기울기가 null과 같으면 두 설명 모두 "자극 너머" 수준에서는 구분되지 않는다. 이 경우 정서 정보는 자극 특징 재표현이라는 결론이 남는다.
* **4주 계획**
  * 1주: ROI 정의(보유본 ROI 확인, 없으면 HCP360), 영역별 tSNR과 dropout 지도, signal-feasibility 판정.
  * 2주: 영역 x 분기별 적응(VD-RV-A의 2주차 결과 재사용).
  * 3주: 영역별 지표, 증분과 무작위 voxel 대조, 시행별 편도체 결합.
  * 4주: 노출 이력 분석, Horikawa 재현, 정리.
* **가장 가까운 선행과 차이**
  * Brain-Diffuser의 ROI별 회귀 가중치 분석(doi:10.1038/s41598-023-42891-8 [본문]): 초기 시각은 저수준, 범주 영역은 CLIP 특징에 정보적임을 보였다. 정서는 다루지 않았다.
  * WAVE(arXiv:2411.07121 [본문]): 전뇌 decoding에서 DMN과 dorsal attention 기여를 보였다. 정서는 다루지 않았다.
  * Bo 2021, Todd 2013: 영역 활성과 decoding 정확도 수준이다. 자극 대비 기울기는 아니다.
  * 검색(2026-11-12): WebSearch "fMRI decoding amygdala insula voxels added to visual cortex reconstruction improves emotion whole-brain image reconstruction emotional images"(Round 2에서 수행, 결과 없음), 위 VD-RV-1 검색. **판정: no(검색 범위 내).**
* **주요 위험**
  * 작은 피질하 ROI만으로는 해독이 거의 안 될 수 있다. 피질하는 단독 입력이 아니라 "고차 시각 + 피질하"의 증분으로만 본다.
  * 3T에서 V1~V3 블록 평균 신호는 시선 차이에 민감하다. MC는 자유 시청이라 시선이 클립 의미와 정서에 따라 달라질 수 있다(Round 3 GI-P1 검토). 초기 시각 기울기의 일부가 정서 장면에서 시선이 달라진 결과일 수 있으므로, 시선 예측 모형 출력과 장면 저수준 통계를 nuisance로 둔다. 시선 기록은 없다.
  * Brain-IT 영역 마스킹은 원 설계 밖의 사용이다. 마스킹 후 성능이 무너지면 MindEye2 입력층 ROI 제한으로 대체한다.
  * label-provenance: felt / 별도 평정자 규범. evidence-level: R0. signal-feasibility: 피질하 필수.

### [VD-RV-3] 뇌에서 읽어 낸 장면 설명에는 감정을 빼라고 한 사람들의 설명보다 감정이 더 많이 담겨 있을까, 그리고 떠올릴 때는 더할까?

* **자세한 질문**
  * Mind captioning의 decoder(뇌 → DeBERTa 특징, 원 저자 코드)는 정서를 빼라는 지시로 받은 인간 캡션으로만 학습된다. decoder 학습 어디에도 정서 라벨이 없다.
  * 같은 클립에 대해 (i) 인간 캡션 20개의 특징과 (ii) 뇌에서 해독한 특징을 같은 텍스트 정서 탐침에 넣는다. 탐침은 C&K와 무관한 GoEmotions 텍스트로 같은 DeBERTa 층에서 학습한다.
  * 질문 1: (ii)가 (i)보다 정서 쪽으로 기우는가. 그 기울기가 클립의 규범 정서(C&K)와 같은 방향인가. "사람들이 쓰지 않은 정서를 뇌는 표상했다"의 언어판 검정이다.
  * 질문 2: 회상에서 해독한 특징은 지각에서 해독한 특징보다 더 정서 쪽으로 기우는가. 회상 cue가 정서 배제 캡션 하나였으므로, 회상의 정서 기울기는 cue 텍스트로 설명되기 어렵다.
  * 질문 3(선택): 원 저자 방식으로 문장을 생성해 사람이 읽는 텍스트에서도 같은 결과가 보이는지 확인한다.
* **AI가 있어야만 가능한 이유**
  * "뇌가 장면을 어떤 말로 기술하는가"는 decoder 없이는 측정할 수 없다. 언어 모델 특징 공간이 있어야 인간이 실제로 쓴 기술과 뇌의 기술을 같은 척도에서 비교할 수 있다.
  * 정서 탐침을 독립 텍스트로 학습하면, 뇌 쪽이든 인간 쪽이든 같은 자로 정서 함량을 잴 수 있다.
* **정서와 뇌에 대해 새로 알게 되는 것**
  * 장면의 의미 표상이 정서 중립인가, 정서가 섞인 상황 개념화인가를 묻는다. 구성주의는 지각된 상황이 정서 개념으로 범주화된다고 본다. 반면 "의미 내용과 정서는 분리된 채널"이라는 관점도 있다. EmoMind는 두 채널을 분리해 다루는 쪽을 택했다.
  * 회상 결과는 NEVER와 EEV-기억 공유 기반(Todd 2013)에 "기억 속 장면 기술은 정서 쪽으로 더 기운다"는 신경 증거를 더한다. 같은 클립의 지각과 회상을 같은 사람에게서 비교하므로 자극 차이가 없다.
* **데이터**
  * MC: 보유, 전처리 완료. 학습 2,108(캡션 20개씩, 공개 저장소), 테스트 72 x 5, 회상 72 x 5, 시행별 vividness(events.tsv, CC0).
  * Horikawa: 같은 클립의 1회 지각 재현(MC 저자 decoder를 Horikawa 피험자별로 다시 학습).
  * GoEmotions: 공개(arXiv:2005.00547, 서지 확인, 라이선스 미확인).
* **모델과 checkpoint**
  * Mind captioning 코드(MATLAB + Python): 공개, **LICENSE 파일 없음**(이용 조건을 저자에게 확인해야 함). figshare에 DeBERTa-large 특징과 정규화 모수가 있다.
  * DeBERTa-large: 공개.
  * GPU: ridge decoder와 탐침은 CPU로도 된다. 문장 생성(선택)은 MLM 반복 최적화라 A100 1장으로 클립 72개 x 11명이 가능하다.
* **핵심 분석, 예측, 반증 조건**
  1. 클립별 정서 함량 차 e = 탐침(뇌 해독 특징) - 탐침(인간 캡션 특징 평균). 층별로 계산한다.
  2. null: 뇌 해독 특징의 수축과 잡음을 재현하려고, 인간 캡션 특징에서 voxel encoding model로 합성 뇌를 만들고 같은 decoder로 해독한다(VD-RV-A의 null과 같은 논리).
  3. 주 검정: (실측 e - null e)가 C&K 규범 정서 강도와 같은 방향인가.
  4. 회상 검정: 회상 e - 지각 e. 회상은 SNR이 낮아 중립 쪽으로 수축하므로, 회상 SNR에 맞춘 null로 비교한다. cue 캡션이 어느 것이었는지 확인되면 cue 캡션 특징을 별도 회귀자로 넣는다.
  5. 예측: 지각에서 작은 양의 기울기, 회상에서 더 큰 기울기. 부정 정서 클립에서 더 크다(NEVER). vividness가 높은 시행에서 더 크다.
  6. 반증: 실측 e가 null e와 같으면 의미 decoder가 읽는 장면 표상에는 인간 중립 기술을 넘는 정서가 없다. 회상에서 기울기가 지각보다 크지 않으면 "기억이 정서를 과장한다"는 예측은 이 데이터에서 지지되지 않는다.
* **4주 계획**
  * 1주: 원 저자 코드로 MC 결과 재현(지각 식별 정확도), 캡션 특징과 GoEmotions 탐침 학습.
  * 2주: 지각 e와 null e, 주 검정.
  * 3주: 회상 e, SNR 맞춘 null, vividness와 정서가 조절.
  * 4주: Horikawa 재현, 선택적 문장 생성과 소규모 인간 확인, 정리.
* **가장 가까운 선행과 차이**
  * Mind captioning(doi:10.1126/sciadv.adw1464) [본문]: Discussion 여덟째 단락에서 캡션이 정서를 배제해 생성 기술이 정서를 거의 반영하지 못했다고 적었다. 해독 특징 자체의 정서 함량을 인간 캡션과 비교하지는 않았다.
  * EmoMind(arXiv:2605.16739) [본문]: 같은 MC 데이터에서 34차원 정서를 **지도학습으로 해독해 rewriter로 주입**한다. Stage 1 retrieval 캡션은 학습 corpus에서 가장 가까운 인간 캡션을 고르므로 정의상 인간 캡션을 넘는 정서를 가질 수 없다(3.1절). 회상 조건과 region 분석은 없다. **차이:** 우리는 정서 라벨 없이 학습한 의미 decoder의 연속 특징에서 인간 기술 대비 정서 기울기를 재고, 회상과 지각을 같은 사람, 같은 클립에서 비교한다.
  * Afrasiyabi 2024(arXiv:2410.00047) [본문]: 정서 단어 cue로 유도한 심상을 시각화했다. 같은 클립 회상, 인간 기술 대비 비교는 없다.
  * 검색(2026-11-12): arXiv API 질의 "fMRI AND emotion AND (reconstruction OR diffusion OR captioning)"(Round 1, EmoMind만 해당), WebSearch "ds005191 OpenNeuro Horikawa mind captioning dataset reanalysis emotion imagery recall Cowen Keltner videos"(Round 1, 정서 재분석 미발견), PubMed 회상 재활성과 정서가 질의(Round 2, Kark 2019, Cocquyt 2026: 이미지와 맥락 회상, 텍스트 해독 아님). **판정: partially**(정서 캡션 decoding은 EmoMind, 회상 정서 재현은 이미지 연구). 정서 라벨 없는 의미 decoder의 인간 대비 정서 기울기와 회상 비교는 미발견.
* **주요 위험**
  * GPT-3.5 교정이 인간 캡션의 정서 어휘를 줄였다면 인간 기준선이 실제 인간 기술보다 더 중립적이다. 이 경우 "뇌가 더 정서적"은 교정의 산물일 수 있다. 교정 전 원문이 있는지 저자에게 확인하고, 없으면 교정이 정서 어휘에 미친 영향을 같은 GPT 계열로 재현 실험해 크기를 추정한다.
  * 텍스트 정서 탐침은 perceived(평정자 판단) 라벨로 학습되었다. 뇌 기술의 "정서 함량"은 관찰자 관점 척도로 잰 값이다.
  * 회상 시행은 실제 비디오 재제시 직전에 끝나 끝부분 HRF가 겹칠 수 있다(events.tsv 확인). 회상 창 끝 절단으로 다룬다.
  * MC 코드 LICENSE 부재. 재분석 결과 공개 전에 저자 확인이 필요하다.
  * label-provenance: 뇌 쪽과 인간 쪽 모두 텍스트 정서 탐침(perceived / AI 추정 탐침)으로 측정, 교차 검정 목표는 felt / 별도 평정자 규범. evidence-level: R0.

---

## 3. 네 질문의 관계와 우선순위

| 질문 | 측면 | 공유 자원 | 우선순위 의견 |
|---|---|---|---|
| VD-RV-A | 정서 무관 공유 표상의 정서 정보량과 자극 너머 몫, 별도 축 필요성 | 적응 파이프라인, 자극 구동 null | 1. 나머지 셋의 기반 |
| VD-RV-1 | 자극 너머 몫의 방향(과장 대 약화) | VD-RV-A 그대로 | 2. 이론적 대비가 가장 선명하다(affective realism) |
| VD-RV-2 | 출처 영역과 표상 수준, 반복에 따른 변화 | VD-RV-A의 영역별 반복 | 3. 피드포워드 대 재진입을 가르지만 피질하 신호 위험이 있다 |
| VD-RV-3 | 언어 기술과 회상 | 원 저자 코드, 별도 파이프라인 | 독립적으로 1주차부터 가능. VD-RV-A가 2주차에 막히면 이것이 대안이 된다 |

네 질문 모두 결론은 규범 정서 수준(별도 평정자)이다. 참가자 본인 경험과의 연결은 nsdmeadows 탐색(VD-RV-A 6번, VD-RV-1 확장 2)뿐이다. 이 한계를 카드에 명시해야 한다.

---

## 4. 검증과 미확인

* 검증: 0.2절의 저장소 사실(라이선스, checkpoint 위치, 데이터 형식, 캡션 파일), EmoMind 원문의 방법과 데이터(3.1절, 4.1절, 부록 A.4), 이번에 추가한 문헌 4편(Siegel 2018과 Todd 2013은 PubMed, Afrasiyabi 2024와 GoEmotions는 arXiv API). `literature.jsonl`은 총 42편이다.
* 미확인:
  * MindEye2 가중치의 라이선스 문구
  * EmoSet과 GoEmotions의 이용 조건
  * Mind captioning 코드와 캡션의 이용 조건(LICENSE 없음)
  * 보유 MC 전처리본이 figshare 형식과 같은지, ROI 파일 포함 여부
  * 회상 cue로 쓰인 캡션 번호
  * nsdmeadows 지시문
  * Horikawa 2020의 시청 지시(fixation 여부)
  * 3T 블록 평균에서 NSD decoder 적응이 실제로 작동하는지(2주차 관문)
* arXiv API는 이번 라운드에서 일부 질의가 429로 실패했다. 우회하지 않았다.
