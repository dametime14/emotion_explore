# 재탐색 라운드 독립 평가 노트 (adversarial-reviewer)

* 작성: adversarial-reviewer (Agent 12). 기준일 2026-11-12
* 산출물: `outputs/revision/scores_reviewer.csv`(28 x 11 = 308행, 결측 0, python 점검 완료), 이 노트, `outputs/agents/adversarial-reviewer/literature.jsonl`(이번 13건 추가)
* 채점 스크립트: `/tmp/claude-0/-home-user-emotion-explore/4a0aeef6-c090-5f71-8a99-9b8e7c0f6d89/scratchpad/rev/score_reviewer.py`
* **독립성:** `outputs/revision/scores_coordinator.csv`는 열지 않았다. 원 제안자의 자체 점수는 원문에 있어 읽었지만 따르지 않았고, 다른 곳은 11절에 이견으로 적었다.
* **직접 읽은 것:** `outputs/revision/plan.md` 전체, `candidates.md`, 7개 에이전트의 `revision_round.md` 전체(묶인 C-02, C-09, C-16은 두 원문 모두), `outputs/stage1/dataset_Horikawa.md`, `dataset_EmoFilM.md`, `dataset_NSD.md`의 해당 절, `outputs/STAGE_STATUS.md` 맨 아래 사용자 답변 표, `reference/protocols.md` P5~P6, `reference/existing_projects.md`, CLAUDE.md 6절.
* **채점 원칙:** plan.md 2절 그대로. 점수마다 근거 한 문장. "Horikawa가 이미 답한 것을 같은 자료로 다시 판정"하는 후보는 Neuroscientific Importance와 Novelty를 낮췄다. 모델을 만들거나 조작하는 것 자체는 감점하지 않았다. 1점은 쓰지 않았다(완전히 무가치한 후보는 없었다). 점수 분포: 2점 47, 3점 163, 4점 94, 5점 4.

---

## 1. (a) 11개 기준 합계 상위 10 (55점 만점)

| 순위 | 후보 | 합계 | AI-enabled | 1-month | 한 줄 이유 |
|---|---|---|---|---|---|
| 1 | C-11 TRIBE 잔차와 CPM, 본인 생리 | 41 | 4 | 4 | 정서 라벨 없이 학습된 인공 뇌를 null로 써서, Horikawa가 아닌 소리 있는 서사 영화에서 '지각-언어로 계산되지 않는 정서 반응'을 평가 대 신체 성분으로 나눈다. 단 대조 영역은 'TRIBE 적합도'로 맞춰야 한다 |
| 2 | C-08 정서 계산 깊이와 위계 위치 | 40 | 4 | 4 | 관찰할 수 없던 자극별 잠재 변수(재귀 요구량)를 모델이 주고, Horikawa 2020의 transmodal 결론에 대한 새 설명을 반증 가능하게 시험한다. CORnet-S 재귀 단계가 적어 변수 해상도가 약점이다 |
| 3 | C-02 뇌가 본 장면의 정서 쏠림 | 39 | 4 | 4 | decoder를 '뇌가 본 장면'의 계측기로 쓰고 합성 뇌 null과 비정서 속성 대조로 decoder 쏠림을 뺀다. 지각 조건은 자극 모델 불완전 문제가 있어 회상 대 지각 대조가 핵심이 되어야 한다 |
| 4 | C-16 학습 목표만 다른 모델 비교 | 39 | 4 | 4 | 구조와 데이터를 고정한 공개 통제 세트로 1주차부터 가능하다. Conwell 2023, 2025가 행동 평정과 시각피질 쪽을 이미 해서 새로움은 '정서 영상 fMRI + 정서 지도 조건'으로 좁아진다 |
| 5 | C-20 정서 학습이 바꾸는 층 | 39 | 3 | 5 | 추가 학습 없이 C-16 산출물로 끝나 실행성이 최상이지만, 단독으로는 정서와 뇌에 대한 말이 약하다. C-16, C-05와 합쳐야 한다 |
| 6 | C-14 정서 반응의 통합 창 | 38 | 3 | 4 | 맥락 길이 손잡이가 깔끔하고 4주 안 실행이 현실적이나 Jain & Huth 2018의 방법이 있고 D1, D2가 아니다 |
| 7 | C-13 섬엽 inferability와 EDA | 37 | 4 | 3 | 측정할 수 없던 순간별 피질 inferability를 계산하는 새 질문이나 섬엽 주변 생리 잡음이 복원 오차를 직접 바꾼다 |
| 8 | C-18 사람을 본 적 없는 시각계 | 37 | 4 | 3 | 경험 박탈이라는 관찰 불가능한 통제 대상이 얼굴 대 맥락 쟁점에 닿는다. 학습량과 지운 흔적 교란이 위험이다 |
| 9 | C-19 정서 단어를 지운 언어 지도 | 37 | 4 | 3 | Lindquist 2014 해리를 인공 학습자에서 시험해 이론 연결이 가장 구체적이다. Affection 자료 확보가 관문이다 |
| 10 | C-27 화면 대 음악 정서 충돌 | 37 | 4 | 3 | 무음 C&K 평정으로 화면 채널을 고정하는 다리가 영리하나 D3이고 배경 소리 정서에 인간 검증이 없다 |

* 다음 순위: C-21, C-23, C-12(36), C-04, C-22, C-15(35).
* 하위: C-01, C-03, C-10, C-28(30), C-06(31), C-07, C-09(32).

## 2. (b) 새 기준 두 개(AI-enabled + 1-month)만 더한 순위

| 점수 | 후보(같은 점수 안에서는 11개 합계 순) |
|---|---|
| 8 | C-11, C-08, C-02, C-16, C-20 |
| 7 | C-14, C-13, C-18, C-19, C-27, C-21, C-23, C-04, C-22, C-05, C-26, C-24 |
| 6 | C-12, C-15, C-17, C-25, C-07, C-09, C-06, C-01 |
| 5 | C-03, C-10, C-28 |

* **상위 10(동점은 합계로 끊음):** C-11, C-08, C-02, C-16, C-20, C-14, C-13, C-18, C-19, C-27.
* 두 기준만 더하면 7점에 12개가 몰려 변별력이 낮다. 7점 묶음 안의 순서는 사실상 합계가 정한다.
* **AI-enabled 하나만 보면** 4점이 11개다: C-02, C-08, C-09, C-11, C-12, C-13, C-16, C-18, C-19, C-21, C-27. C-12와 C-09는 AI 기여는 높지만 1-month에서 2점이라 (b) 순위에서 빠졌다.

## 3. (c) 치명적 결함으로 빼야 할 후보 (현재 설계 기준)

| 후보 | 치명적 결함 | 살리는 방법 |
|---|---|---|
| **C-01** (단독 진행) | 핵심 추정량 '뇌 해독 표상의 정서 head가 자극 표상의 head를 넘어 규범 평정을 설명하는 몫'은 **'자극 feature 공간이 놓친 자극 정보'와 '뇌가 더한 정서'를 원리적으로 가르지 못한다.** C&K 평정은 평정자가 영상(움직임, 루프 재생 포함)을 보고 매긴 것이고 자극 쪽 표상은 frame CLIP이다. 합성 뇌 null도 같은 feature 공간에 묶인다. 또 같은 양은 decoder 없이 자극 feature 부분상관(Horikawa 2020의 공변량 분석)으로 계산할 수 있어 "관찰만으로는 잴 수 없다"(vision-decoding 0.1절)는 전제가 틀린다. H1(정서 무관 표상에서 정서가 읽힘)은 Conwell 2025 PNAS로 보아 당연히 예상된다 | C-02에 흡수한다. 자극을 고정한 대조(회상 대 지각, MC 반복 1~5회, MC 시험 run의 앞 클립 정서)로 바꾸면 자극 모델 불완전 문제가 상쇄된다. 지각 조건을 남길 거면 자극 feature를 영상 모델(V-JEPA 2)로 바꾸고 '최선의 자극 전용 평정 예측기'를 천장으로 둔다 |
| **C-06** | 영역 반응으로 미세조정한 모델이 **같은 C&K 분포의 보류 클립**에서 정서 구조를 보이는 것은 그 영역 반응이 규범 정서와 상관한다는 사실(Horikawa 2020의 영역별 decoding)을 모델을 거쳐 재확인하는 순환이다. 영역 밖 일반화(nsdmeadows 100장)는 이미지 대부분이 중립이라 검정력이 없다 | 평가 자극을 C&K와 다른 분포(예: Emo-FilM 프레임, 정서 사진 세트)로 바꾸고, 결과 변수를 '영역 반응 RDM과 규범 RDM의 직접 상관으로 예측되는 것보다 큰 일반화'로 정의해야 새 정보가 생긴다 |
| **C-10** | 사람 쪽 측정이 서지 않는다. 34범주별 개인 간 변동 프로필을 코호트당 5명, 6명에서 추정해야 하고, Horikawa에는 반복이 없어 잡음 보정이 안 되며 두 코호트는 스캐너가 다르다. 원 제안의 1주차 게이트에서 닫힐 가능성이 높다 | 개인 수가 많은 Emo-FilM(30명) 또는 Spacetop(약 100명)으로 옮기고, 모델 쪽도 영상 입력 모델 집단으로 바꾼다. 그 경우 한 달은 넘는다 |
| **C-24** | 이론 병목이 범주 평정(BET), 14차원 평정(appraisal), valence, arousal + 캡션(구성주의)으로 **감독**되므로 병목층 RDM이 감독 라벨 RDM으로 수렴한다. 결과는 'C&K 라벨 공간끼리의 RSA 비교', 즉 Horikawa 2020의 범주 대 차원 비교를 같은 자료로 다시 판정하는 것이 된다. 원 제안도 이 위험을 적었다 | 병목을 C&K 라벨이 아닌 독립 자료(예: EmoSet, FindingEmo의 범주, 별도 appraisal 주석)로 학습하고, C&K에서는 고정된 모델만 평가한다. 그리고 병목 RDM과 감독 라벨 RDM의 상관을 부분상관으로 빼고 남는 정렬만 해석한다 |

* **조건부 하향(빼지는 않음):**
  * C-03: C-01 파이프라인 성공에 의존하고 핵심 결론(재진입)이 블록 평균 자료로 식별되지 않는다. C-02의 영역별 확장으로만 둔다.
  * C-07: Horikawa 제공 피질하 ROI 10개에 pulvinar가 없다(시상 전체만). 편도체 범주 프로필은 각성에 지배될 가능성이 높아 34점 순위 상관의 검정력이 낮다.
  * C-28: 원 제안도 전체판 불가로 판정했다. 축소판도 전처리 맞추기에 2주 이상이 든다.
  * C-26: 양식 = 이야기 = run 순서 교란과 소리 clip 36개라는 구조적 한계가 있다(D3이라 우선순위도 낮음).

## 4. (d) 새로 찾은 선행

| 선행 | 식별자 | 확인 경로 | 영향 후보 | 판정 |
|---|---|---|---|---|
| Conwell, Graham, Boccagno, Vessel 2025, "The perceptual primacy of feeling: Affectless visual machines explain a majority of variance in human visually evoked affect", PNAS | doi:10.1073/pnas.2306025121 | PubMed(PMID 39847334), 초록 | C-16, C-19, C-17, C-20, C-01 | **partially.** 180개 모델로 arousal, valence 평정의 설명 가능 분산 대부분을 지각 모델이 설명하고, 무작위 대 범주 지도 대 자기지도 비교를 했다. 뇌는 없다. C-16의 C2 대비(지도 대 자기지도)의 행동판이고 C-01의 H1을 사실상 예고한다 |
| Conwell, Prince, Hamblin, Alvarez 2023, "Controlled assessment of CLIP-style language-aligned vision models in prediction of brain & behavioral data", ICLR 2023 Workshop ME-FoMo | 식별자 없음. iclr.cc/virtual/2023/13599 | WebSearch 결과만(공식 페이지 직접 열람은 네트워크 차단). **verified 아님** | C-16(GI-RV-2의 C1 대비), C-19 | **partially(미검증).** SLIP 세트로 구조와 데이터를 고정하면 언어 정렬이 복측 시각 뇌 예측을 높인다는 증거가 없고, 이미지 평정 예측은 높인다고 요약된다. frontier-ai가 [search_index]로 적은 "ICLR 2023 workshop"이 이것이다 |
| Méndez et al. 2022, "A deep neural network model of the primate superior colliculus for emotion recognition", Phil Trans R Soc B | doi:10.1098/rstb.2021.0512 | PubMed(PMID 36126660), 초록 | C-07 | **partially.** 망막-상구 경로를 본뜬 DNN이 저공간주파수 조율을 보이고 M/P 편향 조작이 표정 인식에 영향을 주며 사람 SC 7T 반응과 맞물린다. C-07의 '피질하 지름길 모델' 발상의 가장 가까운 선행이다(얼굴 표정, 범주 의존 지도와 편도체 프로필 대조는 없음) |
| Jain & Huth 2018, "Incorporating Context into Language Encoding Models for fMRI" | doi:10.1101/327601 | Crossref | C-14 | **partially.** 문맥 길이를 바꾼 언어 모델로 voxel별 시간 척도를 추정하는 방법 자체가 있다. 정서 순간 특이 창은 없다 |
| "The Origin of Affect-specific Neural Representations of Emotional Scenes in Early Visual Cortex", VSS 2025 포스터 | 식별자 없음. visionsciences.org/presentation/?id=1989 | WebSearch 결과만(사이트 차단). **verified 아님** | C-05, C-03, C-01, C-02 | **partially(미검증).** NSD로 학습한 CNN encoding 모델의 합성 반응으로 IAPS 정서 장면이 초기 시각피질에서 decoding되지 않음을 보이고 재진입을 지지한다고 해석했다고 요약된다. C-01~C-03의 '자극 구동 합성 null' 논리와 C-05의 쟁점이 그대로 겹친다. brain-inspired와 frontier-ai가 [search_index]로 언급한 것과 같다 |
| "Evaluating TRIBE v2 Beyond Its Original Benchmarks: From Functional Localizers to Naturalistic Emotion", NeurIPS 2026 | 식별자 없음. neurips.cc/virtual/2026/159782 | WebSearch 결과만(사이트 차단). **verified 아님** | C-11 | **partially(미검증).** 자연 영화에서 TRIBE v2의 모델-뇌 대응이 정서 범주마다 크게 다르고 일부 정서 영역에서 선택적 실패가 있다고 요약된다. 어느 자료를 썼는지 확인 못 했다. Emo-FilM이면 C-11의 1단계(정서 영역 잔차가 큰가)와 겹친다 |
| Liu et al. 2025 VCA, bioRxiv | doi:10.1101/2025.10.20.683439 | Crossref 초록 | C-05 | 초록에 시각 망으로 가는 되먹임 언급이 없다. ViT + 편도체 모사 모듈, IAPS 평정과 편도체 fMRI 정렬. brain-inspired의 미확인 사항 4번을 초록 수준에서 해소(되먹임 없음으로 보임). 같은 그룹(Ding, Keil, Fang)이 VSS 2025, Leem 2026까지 같은 주제를 연속으로 다뤄 C-05는 선점 위험이 크다 |

* 이전 판정의 갱신: frontier-ai와 geometry-info는 C-16 선행을 "no"로 두었으나, 행동 평정과 복측 시각 뇌 각각에 대한 통제 비교는 이미 있다(위 두 Conwell). 정서 영상 fMRI의 정서 관련 분산에 대한 통제 비교는 이번 검색에서도 찾지 못했다.
* 직접 선행을 찾지 못한 후보(검색 범위 안): C-02(복원 오차의 정서 방향), C-08, C-09(지형 모델의 정서 지도), C-12, C-13, C-18, C-19, C-24(이론 병목 모델과 fMRI). Stage 4 이후 'not found' 판정이 뒤집힌 사례(RQ-32, RQ-14)가 있었으므로 모두 잠정이다.

## 5. (e) 묶을 수 있는 후보 (같은 파이프라인)

| 묶음 | 후보 | 공유하는 것 | 묶을 때 고칠 점 |
|---|---|---|---|
| D2 decoder 묶음 | C-02(핵심) + C-01 + C-03 + C-04 | voxel → embedding decoder, 같은 emotion head를 자극과 뇌에 적용, 합성 뇌 null | 핵심 대조를 '자극이 같은 조건 비교'(회상 대 지각, 반복 회차, 앞 클립 정서)로 옮긴다. C-04는 같은 null 논리의 텍스트 판이며 회상 부분만 남긴다. C-01의 MindEye2 NSD 공유 latent는 2주차 선택지로 둔다 |
| D1 학습 압력 묶음 | C-16(핵심) + C-20 + C-05 (+ C-17 head, C-18 식단, C-19 언어 내용) | EmoSet 직접 학습 파이프라인, 공개 통제 세트, '정서 겹침 설명량' 지표, Horikawa+MC 클립 반응 | C-05와 C-20은 같은 실험의 두 팔이다. (a) 고정, (b) 판독만, (c) 되먹임, (d) 피드포워드 끝까지 미세조정, (c') 라벨 섞음을 한 설계에 넣어야 (c)의 효과를 되먹임에 귀속할 수 있다. 겹침 설명량은 전체 설명량으로 정규화하고, 동등성 검정(TOST)을 사전 등록해 null도 정보가 되게 한다 |
| brain-inspired 시각 모듈 묶음 | C-08 + C-05 + C-07 | ImageNet backbone + EmoSet 정서 판독, MC 캡션 통제, noise ceiling | C-08의 재귀 요구량은 CORnet-S 단계 수가 적으므로 시간 펼친 판독 곡선의 연속 지표(예: 곡선 아래 면적)로 정의한다 |
| TRIBE 묶음 | C-11(핵심) + C-15 + C-12 | Emo-FilM fsaverage5 투영, TRIBE v2 특징 1벌, 피질하 2단계 readout | C-12의 편집 파이프라인은 무거워 C-11 결과로 영역을 좁힌 뒤에 둔다 |
| Emo-FilM 생리 묶음 | C-13 + C-11(질문 3) | EDA 분해, PPG, RVT, StartTime 정렬, 생리 잡음 회귀 | 생리 처리 1주차를 공유한다 |
| 이론 검정 묶음 | C-22 + C-23 + C-24 | V-JEPA 2 + 캡션 특징, 규범 평정, 같은 encoding 기반 | C-24는 3절의 재설계가 전제다 |
| Spacetop 정렬 묶음 | C-26 + C-28 | alignvideo 기반 functional alignment | D3라 우선순위 낮음 |

## 6. (f) 사용자 기준(AI-enabled 기여, D1, D2)에서 가장 강한 3개

1. **C-02 (D2): 뇌가 본 장면은 실제보다 정서 쪽으로 기울어 있을까?** 단, 회상 대 지각 대조를 주 검정으로 올린다.
   * 이유: D2 후보 중 유일하게 decoder가 '측정 장치'로 쓰여 관찰로 얻을 수 없는 변수(뇌 표상과 자극의 차이 방향)를 만든다. GI-RV-3의 정서 특이 과장 지수(정서 대 비정서 속성)와 합성 뇌 null이 decoder 쏠림과 일반 충실도를 뺀다.
   * 고칠 점: 지각 조건의 '자극 너머' 몫은 자극 모델 불완전과 구분되지 않는다(3절 C-01). 같은 클립의 회상 대 지각(SNR 맞춘 null), MC 반복 회차(습관화), 시험 run의 앞 클립 정서(HRF 이월은 비정서 속성 이월로 대조)를 주 검정으로 둔다. ridge판으로 1주차를 시작하고 MindEye2 적응은 선택지로 둔다.
   * 사용자가 말한 'MindEye2, Brain-IT + emotion head' 그대로의 판(C-01, C-03)은 3T 블록 평균 적응 위험과 식별 문제 때문에 이 판보다 약하다.
2. **C-16 + C-20 + C-05 통합 (D1): AI가 정서를 직접 배워야만, 또는 되먹임이 있어야만 뇌의 정서 반응과 닮아질까?**
   * 이유: 관찰로 만들 수 없는 '학습 압력만 다른 시각계'를 공개 통제 세트와 소규모 직접 학습으로 1주차부터 얻는다. 정서 schema, 일반 학습, 재진입 가설이 서로 다른 예측을 낸다.
   * 고칠 점: 새로움은 Conwell 2023, 2025 때문에 '정서 영상 fMRI의 정서 관련 분산'으로 좁혀서 주장한다. 피드포워드 끝까지 미세조정 팔을 넣고, 겹침 설명량 정규화와 동등성 검정을 사전 등록한다. Conwell 2024처럼 차이가 작게 나올 가능성이 높으므로 '차이 없음'의 해석 문장도 미리 고정한다.
3. **C-11 (D1, in-silico 뇌): 보고 듣는 것만으로 예측되지 않는 정서 반응은 어디에 남고 어떤 성분과 함께 움직일까?**
   * 이유: 합계 1위다. Horikawa가 아닌 자료(Emo-FilM, Spacetop)로 사용자의 'Horikawa 재분석' 비판을 피한다. 정서 라벨 없이 학습된 인공 뇌가 '정서 없는 기대 반응'을 주고, 결과가 평가 대 신체 성분이라는 정서 이론의 구체적 쟁점에 말한다. 추론 위주라 4주 안에 끝난다.
   * 고칠 점: TRIBE 적합도가 변연과 전전두에서 낮아 잔차 비율이 기계적으로 커진다. 대조 영역을 '천장 대비 TRIBE 적합도'로 맞추고, NeurIPS 2026 TRIBE v2 정서 평가 논문의 자료와 결과를 먼저 확인한다. overlap: Emo-FilM 연구(직접).
   * 엄격한 '뇌를 닮은 구조' 의미의 D1이 필요하면 C-08(재귀 계산 깊이)이 대안이다. 합계 2위이고 1주차 실행이 가능하다.

## 7. 후보별 핵심 전제 반증 시도 (한 줄씩)

| 후보 | 반증을 시도한 전제 | 결과 |
|---|---|---|
| C-01 | "decoder 없이는 뇌 표상과 자극의 차이를 잴 수 없다" | **반증됨.** 같은 추정량은 자극 feature 부분상관으로 계산된다. decoder의 고유 기여는 'NSD 정서 무관 latent로 제한'뿐이다 |
| C-02 | "합성 뇌 null이 decoder 쏠림을 정확히 재현한다" | 부분 반증. feature 공간 밖 정보와 정서 강도에 따른 수축 차이는 재현하지 못한다. 비정서 속성 대조와 회상 대 지각 대조로 일부 보완된다 |
| C-03 | "초기 시각 기울기는 재진입의 서명이다" | 반증 가능성 높음. 자유 시청 시선 차이와 각성에 따른 주의 이득도 같은 서명을 만든다 |
| C-04 | "해독 특징의 정서 함량이 인간 캡션보다 크면 뇌가 정서를 더 표상한 것이다" | 부분 반증. ridge가 캡션 고유 잡음을 걸러 내면 해독 값이 클립 정서와 더 상관할 수 있고, 기준 캡션은 정서 배제 지시와 GPT-3.5 교정으로 인위적으로 중립이다. 합성 null이 이를 일부 다루지만 결국 RQ-08과 같은 추정량이다 |
| C-05 | "(c)만 사람 시각피질의 정서 성분을 재현하면 재진입 서명이다" | **반증됨.** 피드포워드 끝까지 미세조정도 같은 시각층 정서 성분을 만들 수 있어 대조가 빠져 있다 |
| C-06 | "영역 이식 모델의 정서 구조는 영역 표상의 충분성을 보인다" | **반증됨(순환).** 같은 C&K 분포에서는 영역-정서 상관을 옮긴 것과 구분되지 않는다 |
| C-07 | "사람 편도체와 pulvinar의 범주 프로필을 신뢰성 있게 얻을 수 있다" | 약화. pulvinar ROI가 제공되지 않고 Horikawa TE 43 ms, 3T 블록 평균이다 |
| C-08 | "모델 재귀 요구량은 정서 고유 변수다" | 미반증, 위험 남음. 물체 요구량 통제가 있으나 사회적 복잡도, 모호성과 섞일 수 있다 |
| C-09 | "사람 VTC에 의미 통제 뒤에도 정서 선호 군집이 있다" | 미확인. 원 제안의 반증 조건이 바로 이것이며 Westlin 2025로 보아 없을 가능성도 크다 |
| C-10 | "11명에서 34범주별 개인차 프로필이 잡음 상한을 넘는다" | 반증 가능성 높음(5명, 6명, Horikawa 반복 없음) |
| C-11 | "공유 잔차 비율 B의 영역 차이는 정서 때문이다" | 부분 반증. TRIBE의 영역별 적합도 차이만으로도 B 차이가 생긴다. 대조 영역 맞춤으로 보완 가능 |
| C-12 | "TRIBE에서 앞 맥락을 지우면 뇌의 서사 맥락 효과를 흉내 낸다" | 약화. 영상 경로는 직전 4 s만 보고 맥락은 주로 텍스트 경로라 '대사 맥락' 조작에 가깝다 |
| C-13 | "복원 오차 증가는 피질 밖 정보의 표지다" | 약화. 국소 생리 잡음과 움직임도 같은 효과를 낸다. 원 제안도 해석 가설로 표시했다 |
| C-14 | "정서 순간의 긴 통합 창은 정서 때문이다" | 약화. 정서 순간이 서사 의존적 순간과 겹친다. 맥락 교체 대조는 길이 artifact만 다룬다 |
| C-15 | "트윈 지문은 정서 성향이다" | 약화. 개인 head는 해부, 정합 차이를 먼저 학습한다. 정서 순간 상호작용이 유일한 방어선이다 |
| C-16 | "목표만 다른 모델의 뇌 닮음 차이가 정서 표상의 학습 기원을 말한다" | 약화. Conwell 2024의 결과대로 차이가 작을 가능성이 높고, 일반 캡션 감독은 '정서 개념어 학습'이 아니다 |
| C-17 | "head 세밀도 효과가 차원 수 효과와 분리된다" | 미반증이나 무작위 projection 대조에 크게 의존한다 |
| C-18 | "사람 지움 식단의 손실은 사람 경험의 필요성을 뜻한다" | 약화. 지운 흔적 단서와 학습 자료 감소가 섞인다. 상호작용 설계가 일부 방어한다 |
| C-19 | "정서 단어를 지우면 정서 개념 학습이 빠진다" | 약화. 이유 서술이 정서를 함축한다. 원 제안도 인정했다 |
| C-20 | "정서 미세조정은 초기 지각 층을 바꾼다" | 반증 가능성 있음. 일반적인 미세조정은 주로 후기 층을 바꾼다. 그 자체가 결과이지만 '학습량 부족'과 구분해야 한다 |
| C-21 | "두 코호트에서 재현되는 transmodal 공유 축이 있다" | 미확인. Westlin 2025(개인별 군집, NMI 0.014)로 보아 매우 적을 수 있다. 원 제안이 1주차 닫힘 조건을 두었다 |
| C-22 | "혼합 클립은 혼합 정서 자극이다" | **반증됨(라벨 수준).** C&K 비율은 평정자 사이 공존이라 사람 안 혼합을 뜻하지 않는다. 원 제안도 인정하고 '평정자 집단 안 공존'으로 재정의했다 |
| C-23 | "캡션 기반 상황 분할은 정서와 독립이다" | 약화. 3~5 s 클립에서는 상황과 정서가 강하게 상관할 수 있다. 원 제안이 점검 단계를 두었다 |
| C-24 | "이론 병목은 이론 구조를 구현한다" | **반증됨.** 감독 라벨이 병목 RDM을 결정해 라벨 공간 비교로 환원된다 |
| C-25 | "Emo-FilM에서 분노 대 슬픔 판독 축을 믿을 만하게 학습할 수 있다" | 약화. Ma & Kragel 2026의 판독 효과가 r 약 0.04~0.10이다 |
| C-26 | "글 학습 축을 소리 clip에 투영한 점수는 양식 효과를 담는다" | 약화. 양식 = 이야기 = run 순서다. 원 제안이 직접 계산해 밝혔다 |
| C-27 | "AI 배경 소리 정서 추정은 타당하다" | 미확인. 인간 검증이 없고 consensus 예측판은 화면 채널과 섞인다 |
| C-28 | "내용 기반 정렬이 정서 성분도 정렬한다" | 약화. Wang 2024 Discussion도 내용 정렬이 개인 특이 성분을 덜 담는다고 적었다 |

## 8. 여러 후보에 걸친 공통 비판

1. **Horikawa + MC 의존.** 28개 중 19개(C-01~C-10, C-16~C-24)가 주 뇌 자료로 Horikawa + MC를 쓴다. D1, D2는 대규모 정서 자극 fMRI가 이것뿐이라 자연스럽지만, 사용자의 "대부분 Horikawa 재분석" 비판은 여전히 적용될 수 있다. 질문이 Horikawa가 이미 답한 것(범주 대 차원, 공변량 너머 정서, 영역별 decoding)으로 환원되는지를 기준으로 C-01, C-04(지각 부분), C-06, C-24를 낮췄다.
2. **D2의 추정량 문제.** '자극 너머' 몫은 언제나 '자극 feature가 놓친 것'을 포함한다. 규범 평정은 자극(영상 전체)의 함수이므로 뇌가 그 평정을 자극 모델보다 더 설명하는 것은 '자극 모델이 사람이 쓰는 정보를 놓쳤다'를 먼저 뜻한다. 자극을 고정한 대조(회상, 반복, 맥락)만이 '뇌가 더한 것'을 식별한다.
3. **D1의 '정서 겹침 설명량'.** R2(M)+R2(R)-R2(M+R)은 전체 설명량이 큰 모델에서 기계적으로 커진다. 모델 간 비교에는 R2(M) 대비 비율이나 R2(R)로 나눈 값을 함께 보고해야 한다. 프레임 평균 feature는 영상의 움직임 정보를 잃어 정지 이미지 모델 전체에 공통 불리함을 준다.
4. **null 결과의 정보성.** Conwell 2024(시각피질에서 목표 차이 작음)를 보면 D1 비교 대부분이 '차이 없음'으로 끝날 수 있다. 동등성 한계를 사전 등록하지 않으면 null은 해석할 수 없다.
5. **라벨 주체.** 모든 Horikawa, MC, Emo-FilM 결론은 별도 평정자의 규범 평정 수준이다. 참가자 본인 연결은 Spacetop(C-11 반복, C-22 팔, C-26, C-28)과 nsdmeadows 100장(C-01, C-02 탐색)뿐이다. 이 점은 원 제안 대부분이 정확히 표시했다.

## 9. Stage 1 보고서와 대조한 데이터 사실

* **Horikawa 블록 구조:** 8 s보다 짧은 영상은 8 s를 넘을 때까지 반복 재생되고 블록마다 2 s 휴지가 붙는다(dataset_Horikawa.md 59행). 'frame CLIP 한 벡터'로 자극을 요약하는 D2, D1 설계 모두 이 시간 구조를 잃는다.
* **Horikawa 피질하 ROI:** thalamus, hippocampus, hypothalamus, pallidum, brainstem, caudate, putamen, nucleus accumbens, amygdala, cerebellum 10개다(72행). pulvinar는 없다(C-07). '개별 ROI 13개'의 정체는 미확인이라 Horikawa에 localizer 기반 ROI가 있는지도 미확인이다(C-09).
* **Horikawa noise ceiling:** 반복 제시가 사실상 없어(내용 중복 15쌍) 직접 구할 수 없다(215행). C-10, C-06의 영역 신뢰도 추정에 영향.
* **NSD nsdmeadows:** 100(+3)장, 참가자 본인 평정이나 지시문 미확인, 이미지 대부분이 중립(dataset_NSD.md 22, 132행). C-01, C-02, C-06의 '개인 경험' 탐색은 효과 크기 추정 수준이다.
* **Emo-FilM:** 30명, 14편, 6 mm smoothing, 생리 1000 Hz, consensus는 3~4명 평균, arousal과 valence 문항 없음(dataset_EmoFilM.md 31~88행). C-11, C-13, C-25, C-27의 전제와 맞는다. EDA 전처리 서술은 논문에 없다(75행).
* **사용자 답변(STAGE_STATUS):** C&K 2,185개 무음, 두 코호트 비중복, MC 정서 배제 캡션 보유가 확인되어 있다. MC 보유본 전처리 형식(30번)은 여전히 미확인이며 C-02, C-03, C-04, C-21의 1주차 관문이다.

## 10. 인용 표본 점검

arXiv API(export.arxiv.org)와 Crossref API로 식별자를 해석했다.

| 인용(원문 주장) | 결과 |
|---|---|
| EmoMind arXiv:2605.16739 | 존재, 제목과 저자 일치 |
| Zhan et al. 2026 arXiv:2610.13558(TRIBE 예측으로 정서 편집 안내) | 존재(제목 "What We Talk About When We Talk About Emotion Editing"). 내용 주장은 이번에 초록을 받지 않아 미확인 |
| Leem, Keil, Ding 2026 arXiv:2607.19327("Visual-Valence + Shortcut 구조, 지름길이 조건화에 필요함을 보였다", brain-inspired) | 존재. **초록에는 시각 모듈 + valence 모듈과 Pavlov 학습만 있고 '지름길'이나 '지름길의 필요성'이 나오지 않는다.** 본문 확인 전에는 C-07의 근거로 쓰지 말아야 한다 |
| Xing et al. 2026 arXiv:2609.34742(VLM 사이 정서 무관 정렬이 정서 vector를 운반) | 초록 3번 결과("generic ImageNet activations로 추정한 변환이 정서 vector 없이도 대응과 인과 전이를 회복")와 일치 |
| Policzer et al. 2025 arXiv:2511.07988(STS, 사회 인지 brain-tuning) | 존재, 제목 일치 |
| Jindal et al. 2026 arXiv:2602.07570(3~24 s 클립, 긴 창이 고차 영역과 맞음) | 초록과 일치 |
| Mertens 2025 arXiv:2509.21384(기성 CNN과 valence 평가 fMRI) | 초록과 일치 |
| Schwartz et al. 2023 doi:10.1523/JNEUROSCI.1277-22.2023 | Crossref 제목 일치(정체성과 표정 표상의 공유 기반) |
| Kragel et al. 2021 doi:10.1016/j.neuron.2021.06.001 | Crossref 제목 일치(colliculus-pulvinar-amygdala 경로가 부정 정서를 부호화) |
| Conwell et al. 2024 doi:10.1038/s41467-024-53147-y | Crossref 제목 일치 |
| Liu et al. 2025 VCA doi:10.1101/2025.10.20.683439 | Crossref 초록 일치, 되먹임 언급 없음 |

* 불일치 1건(Leem 2026의 '지름길' 주장)과 내용 미확인 1건(Zhan 2026)이다. 나머지 9건은 식별자와 주장된 내용이 맞았다.

## 11. 원 제안자 자체 평가와의 이견 (조정하지 않고 기록)

| 후보 | 원 제안자 자체 평가 | 이 평가 | 이견의 핵심 |
|---|---|---|---|
| C-01 | vision-decoding: "관찰만으로는 이 차이를 잴 수 없다", 1순위 기반 | AI-enabled 3, 합계 하위 | 추정량이 decoder 없이도 계산된다(7절). vision-decoding은 'NSD 정서 무관 정렬'이 고유 대상이라고 볼 것이다. 이 이견은 해소되지 않았다 |
| C-16 | geometry-info: AI 기여 5. frontier-ai: 선행 "no" | AI-enabled 4, Novelty 3 | Conwell 2023, 2025가 같은 통제 세트와 정서 평정을 다뤘다. 정서 fMRI 부분은 여전히 새롭다는 점에는 동의 |
| C-12 | encoding-foundation: AI 기여 4, 한 달 3 | AI-enabled 4, 1-month 2 | 편집 파이프라인 무게와 TRIBE 맥락 조작의 범위 |
| C-17 | frontier-ai: AI 기여 중상 | AI-enabled 2 | 결과가 관찰자 모델과 측정 방법의 성질에 머문다 |
| C-24 | emotion-theory: 이론 판정 질문 | NI 2, 치명적 결함 | 감독 라벨이 병목을 결정한다. emotion-theory도 위험으로 적었으나 치명도 판단이 다르다 |
| C-05 | brain-inspired: 4주 실현성 높음, 1순위 착수 권고 | 1-month 4는 동의, Methodological Rigor 2 | 피드포워드 미세조정 대조 부재 |
| C-09 | geometry-info: AI 기여 4, 한 달 3. brain-inspired: 낮음~중간 | AI-enabled 4, 1-month 2 | brain-inspired 쪽 판단에 가깝다 |

## 12. 검색 기록과 한계 (모두 2026-11-12)

| # | 경로 | 질의 | 쓴 곳 |
|---|---|---|---|
| 1 | WebSearch | language supervision CLIP versus SimCLR emotion representation visual cortex fMRI affective images controlled comparison | C-16, C-19 |
| 2 | WebSearch | brain decoding fMRI decoded CLIP embedding emotion valence affective content beyond stimulus MindEye emotional images 2025 | C-01, C-02 |
| 3 | WebSearch | origin of affect-specific neural representations emotional scenes early visual cortex reentry amygdala deep neural network synthetic fMRI | C-03, C-05 |
| 4 | PubMed | perceptual primacy of feeling affectless visual machines visually evoked affect | C-16 |
| 5 | WebSearch | topographic deep neural network emotion valence selectivity map ventral temporal cortex TDANN affective 2025 2026 | C-09 (선행 없음) |
| 6 | WebSearch | appraisal basic emotion constructionist theory computational models compared fMRI representational similarity naturalistic video neural network bottleneck | C-24 (선행 없음) |
| 7 | WebSearch | TRIBE encoding model residual emotion Emo-FilM naturalistic film fMRI appraisal component process model 2026 | C-11 |
| 8 | WebSearch | brain-tuning fine-tune vision model amygdala insula fMRI emotion representation emerges without labels | C-06 |
| 9 | WebSearch | affective realism neural representation visual cortex emotional scenes perceived more emotional decoding fMRI 2024 2025 | C-02 |
| 10 | WebSearch | "Controlled assessment of CLIP-style language-aligned vision models" brain behavioral data authors | C-16 |
| 11 | arXiv API | abs:fMRI AND abs:emotion AND (abs:decoder OR abs:reconstruction OR abs:MindEye), 최신순 | C-01~C-04 (EmoMind 외 해당 없음) |
| 12 | arXiv API | (abs:affective OR abs:emotion) AND (abs:topographic OR abs:TDANN OR brain-tuning) | C-06, C-09 (질의가 넓어 무관 결과, 해당 없음) |
| 13 | PubMed | (CLIP OR self-supervised OR deep neural network) AND (emotion OR affective OR valence) AND fMRI AND visual cortex, 2024~ | C-07(Méndez 2022), C-22(Murray 2023 재확인) |
| 14 | WebSearch | reconstruction of emotional images from fMRI diffusion valence of reconstructed images compared to original affective bias | C-02 (선행 없음) |
| 15 | arXiv API | abs:emotion AND (fMRI OR brain) AND (training objective OR self-supervised OR language supervision OR SLIP) | C-16 (EEG 연구만) |
| 16 | Crossref | VCA, Jain & Huth 2018, Schwartz 2023, Kragel 2021, Conwell 2024 | 4, 10절 |
| 17 | arXiv API id_list | 2607.19327, 2609.34742, 2605.16739, 2610.13558, 2511.07988, 2509.21384, 2602.07570 | 10절 |

* **차단:** WebFetch로 visionsciences.org, neurips.cc, mlanthology.org, biorxiv.org, arxiv.org가 해석되지 않았다(세션 네트워크 허용 목록 밖). 그래서 VSS 2025 포스터, NeurIPS 2026 TRIBE v2 평가, Conwell 2023 ICLR workshop은 검색 결과 요약만 보았고 verified로 세지 않았다. 세 건을 확인하려면 이 호스트들을 세션 네트워크 설정에서 허용해야 한다. arXiv와 Crossref는 Bash의 API 호출로 확인했다.
* 모든 'not found'는 이 검색 경로 안의 판정이다.
* 본문을 읽은 새 문헌은 없다. 이번 추가 13건은 모두 초록 또는 서지 수준이고 `discussion_read`를 그에 맞게 표시했다.
