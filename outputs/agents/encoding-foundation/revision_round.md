# encoding-foundation 재탐색 라운드: D1 in-silico 뇌 모델과 brain foundation model

* 작성: encoding-foundation (Agent 4, Axis F, H, S)
* 기준일: 2026-11-12
* 지시: `outputs/revision/plan.md` 3절 표(출발점 RQ-51, 새 질문 방향 D1)
* 직접 읽은 파일: `outputs/revision/plan.md` 전체, `outputs/rq_landscape.md`(K9 군집, RQ-51 항목), `outputs/evaluation/scores_final.csv`와 `reviewer_notes.md`의 RQ-51 부분, `outputs/stage1/dataset_EmoFilM.md`, `dataset_Spacetop.md`(해당 절), `reference/existing_projects.md`, `reference/datasets_and_resources.md` 1절, `outputs/axis_encyclopedia.md` 3절. 모델 사실은 내려받은 논문 전문(TRIBE v2, CortexMAE, Brain-DiT)과 공개 저장소 코드(tribev2, CortexMAE, Brain-JEPA, NeuroSTORM, BrainLM)를 읽어 확인했다. 내려받은 코드는 실행하지 않았다.
* 이 문서의 "확인"은 문서나 코드를 직접 읽었다는 뜻이고, "실행 전"은 코드상 경로만 보았다는 뜻이다.

---

## 0. 요약

| ID | 한 줄 질문 | AI의 역할 (plan.md 2절 a, b, c) | 주 자료 | 모델 | 두 새 기준 자체 예상 (참고용, 채점 아님) | overlap |
|---|---|---|---|---|---|---|
| EF-RV-0 (RQ-51 재작성) | 보고 듣는 것만으로는 예측되지 않는 정서 반응은 뇌의 어디에 남고, 정서의 어떤 측면과 함께 움직일까? | b, a: 지각-언어로 계산되는 몫을 빼고 남는 공유 반응을 계산 | Emo-FilM (주), Spacetop alignvideo | TRIBE v2 (zero-shot) | AI 기여 4, 한 달 4 | Emo-FilM 연구 |
| EF-RV-1 | 영화에서 얼굴을 지워서 사라지는 정서 반응과 앞 이야기를 지워서 사라지는 정서 반응은 뇌의 서로 다른 곳에 있을까? | a, c: 반사실 편집 자극의 2×2 in-silico 실험 -> 사전 등록 -> 관찰 검증 | Emo-FilM, Spacetop shortvideo/alignvideo | TRIBE v2 + 영상 편집 | AI 기여 4, 한 달 3 | Emo-FilM 연구 |
| EF-RV-2 | 몸이 크게 반응하는 정서 순간에, 섬엽은 나머지 대뇌피질만 보고는 짐작할 수 없는 상태가 될까? | b, a: 전형적 피질 역학이 예상하는 활동과의 어긋남을 순간 단위로 계산 | Emo-FilM (참가자 생리), Spacetop | CortexMAE (masked reconstruction) | AI 기여 4, 한 달 4 | Emo-FilM 연구(자료만) |
| EF-RV-3 | 정서 관련 뇌 반응은 얼마나 먼 과거의 이야기까지 끌어와서 만들어질까? | a, b: 과거 길이만 다른 인공 이해자 계열로 통합 창 측정 | Spacetop narratives (주), Emo-FilM | 개방 언어 모델 두 계열 | AI 기여 4, 한 달 4 | Emo-FilM 연구(직접) |
| EF-RV-4 | 사람마다 다른 정서 뇌 반응은 영화가 바뀌어도 유지되는, 그 사람만의 반응 성향일까? | a, c: 개인 디지털 트윈에 보지 않은 장면을 보여 개인 지문을 얻고 사전 검증 | Emo-FilM (주), Spacetop | TRIBE v2 개인 head 미세조정 | AI 기여 4, 한 달 3 | Emo-FilM 연구, EmoBrain(반대 방향) |

* 내 순위(정서와 뇌에 대해 새로 말해 주는 양 x 한 달 실행성): EF-RV-0 > EF-RV-2 > EF-RV-3 > EF-RV-1 > EF-RV-4. 근거는 각 질문의 "주요 위험" 참조.
* 모든 질문의 공통 원칙:
  * Horikawa와 MC(C&K 무음 클립)는 TRIBE v2 입력으로 주 분석에 쓰지 않는다. TRIBE v2는 소리 있는 영화로 학습된 평균 피험자 모델이고, 무음 짧은 클립은 학습 분포 밖이다(plan.md 4절). 그래서 in-silico 입력은 소리 있는 Emo-FilM과 Spacetop으로 한다. 뇌 자료만 입력하는 brain FM(EF-RV-2)에서만 MC를 선택적으로 쓴다.
  * 모든 in-silico 결과는 관찰 자료로 검증하는 단계와 짝을 이루고, 관찰과 어긋나는 영역은 "모델이 실패한 곳"으로 따로 보고한다.

---

## 1. 공통 사실 (이번 라운드 확인 수준 표시)

### 1.1 모델

| 모델 | 확인한 사실 | 출처, 확인 방식 | 미확인 |
|---|---|---|---|
| TRIBE v2 (arXiv:2605.04326) | 영상(V-JEPA2-Giant, 직전 4 s의 64 frame), 소리(Wav2Vec-BERT 2.0, 60 s 덩어리, 덩어리 안 미래 정보 포함), 텍스트(Llama-3.2-3B, 앞 단어 문맥 포함) 특징을 transformer(8층)로 결합. 공개 checkpoint는 평균 피험자, fsaverage5 피질 20,484 vertex, 5 s 지연 보정. 코드와 가중치 CC BY-NC 4.0. 누락 양식은 0으로 채우는 규약(modality dropout 학습). transformer 출력 뒤 low-rank head와 subject layer가 있어 forward hook로 잠재를 꺼낼 수 있다. 피질하 학습 grid(run_subcortical)와 subject layer 크기 조정 옵션(resize_subject_layer)이 코드에 있다 | 논문 Methods 전문, 저장소 README, LICENSE, model.py, grids/defaults.py | 추출기 셋의 라이선스. 설정 duration_trs 100, frequency 2, text max_context_len 1024의 정확한 의미(창 길이 초 단위)는 실행 전. 피질하 공개 가중치 없음(README가 fsaverage5만 명시) |
| CortexMAE (arXiv:2510.13768) | HCP-YA 2,058시간(휴지, EMOTION 포함 7개 과제, 영화)으로 MAE 사전학습. flat map 224×560, Schaefer-400, MNI 피질 volume 세 판 공개(HF medarc/CortexMAE). TR 1 s로 선형 보간, 16 frame 입력, tube masking 0.9. 코드 Apache-2.0, 가중치 CC BY-NC 4.0(LICENSE.models). `run_masked_recon`, `run_denoise` 공개 API. 피질만(Discussion에서 피질하 미포함을 한계로 명시). NSD는 OOD 복원 검증과 probe에 썼고 사전학습에는 없다 | 논문 전문, 저장소 README, LICENSE 두 개 | 6 mm smoothing, FSL MNI 정합 자료에서의 복원 품질 |
| Brain-JEPA (arXiv:2409.19407) | Schaefer-400 + Tian S3(피질하 포함), UKB 휴지 사전학습, 가중치는 README의 Google Drive 링크 | 저장소 | 저장소에 LICENSE 파일 없음. 결과 공개용 사용 전 저자 확인 필요 |
| NeuroSTORM (arXiv:2506.11167) | 4D volume 전뇌, HF 가중치 | 저장소 | README 배지 MIT와 LICENSE 파일 Apache 불일치 |
| Brain-DiT (arXiv:2604.12683) | ID 사전학습 22개 자료에 Emo-FilM, NSD, StudyForrest, HCP Movie 포함 | 논문 3.1절 전문 | 가중치 링크("available at Link") 미추출. **Emo-FilM, NSD 분석에는 오염이라 이번 질문 전부에서 제외** |

### 1.2 자료 (Stage 1 감사와 plan.md 4절 기준)

| 자료 | 이번 질문에 쓰는 핵심 사실 | 라벨 주체 |
|---|---|---|
| Emo-FilM (ds004892, ds004872; CC0) | 30명, 단편 14편(2.5시간 이상), 소리 있음, TR 1.3 s, 2.5 mm, FSL MNI 전처리본(6 mm smoothing, WM/CSF/motion 회귀), surface 산출물 없음. PPG, 호흡, EDA 1000 Hz가 전 런에 있음(StartTime 부호 확인 필요). 50항목 1 Hz consensus(appraisal 10, motivation 10, expression 5, feeling 7, physiology 5, discrete 13). arousal, valence 문항은 없다(IntenseEmotion, Alert, Calm은 근접 항목일 뿐) | 주 라벨: 별도 평정자 44명의 규범 평정. 본인: 사후 클립 회고 평정(영화당 5항목, 항목별 영화당 3~4명), 영화별 몰입, 즐거움, 흥미, 생리 |
| Spacetop (ds005256, ds007070; CC0) | 약 100명, TR 0.46 s, fMRIPrep 25.1.4의 fsLR 91k CIFTI와 MNI volume 공개. alignvideo 49편(약 86분, 소리, 모든 참가자 같은 순서), shortvideo 21개(alignvideo 인물 장면을 수일 뒤 4.1~6.9 s로 재제시, 99명), narratives 8편 × 9 clip(연구실 제작, 4편 소리, 4편 텍스트, 원문 txt 공개, 약 105명), faces(동적 얼굴 8표정). 생리는 기록했으나 공개 파일 없음 | 전부 참가자 본인 사후 평정. alignvideo 7항목(약 51% 결측), narratives clip별 느낌(good-bad, 강도)과 기대, shortvideo 인물 판단. 별도 평정자 규범 평정 없음 |
| Horikawa 2020, MC | C&K 클립 전부 무음. 라벨은 별도 평정자 규범 평정. MC 보유본 전처리 형식 미확인 | 규범 평정 |

* 원본 자극: 네 자료 모두 보유(사용자 확인, `reference/datasets_and_resources.md` 1절). 경로와 계산 자원은 미기재라 "미확인".
* Spacetop 영상은 약칭 파일명만 있어 TRIBE v2 학습 영상(CNeuroMod)과의 중복을 대조하지 못했다. 1주차 확인 항목이다.

---

## 2. (A) 출발점 RQ-51 진단과 재작성

### 2.1 원래 질문

> RQ-51. AI 뇌 모델은 실제 뇌의 정서 구조를 어디까지 재현할까? TRIBE v2 같은 in-silico 뇌가 같은 자극의 실측 fMRI에 비해 정서 구조를 시각 구조보다 더 많이 잃는가, 그 손실이 어느 parcel과 rank 대역에 몰리며 백본(V-JEPA 2) feature 자체의 한계로 설명되는가? (주 자료 MC, Horikawa, Emo-FilM)

### 2.2 왜 약했는가

| 기준 (plan.md 2절) | 진단 | 예상 점수 |
|---|---|---|
| AI-enabled Affective Neuroscience Contribution | 질문의 대상이 정서가 아니라 모델이다. 답은 "TRIBE v2가 정서 RDM을 얼마나, 어디서 잃는가"라는 모델 결함 보고이고, 정서나 뇌에 대해 새로 말하는 것이 없다. (a) 통제된 비교 대상, (b) 측정 불가 변수, (c) 새 가설 중 어느 것도 만들지 않는다. "백본 feature의 한계로 설명되는가"는 AI 쪽으로 돌려주는 진단이다. 평가 단계에서도 Neuroscientific Importance 2.5, reviewer는 "관문이라 과학적 가치는 2"로 매겼다 | 2 |
| 1-month Feasibility | 추론만 하므로 실행은 쉽다. 그러나 주 자료가 무음 C&K 클립이라 TRIBE v2 학습 분포 밖이다(plan.md 4절). 실패가 나와도 "정서 결함"인지 "무음, 짧은 반복 클립 OOD"인지 가를 수 없어, 4주 뒤 해석 가능한 결론이 남지 않는다. 공개본이 피질만이라 amygdala 같은 피질하 정서 구조는 원리적으로 비교할 수 없다 | 실행 4, 해석 가능성 2 |
| 새로움 | EmoMind(arXiv:2605.16739)가 TRIBE 합성 반응의 clip 간 정서 RSA가 0.635에서 0.166으로 떨어짐을 이미 보였다. NeurIPS 2026 TRIBE v2 평가(검색 색인만)도 정서 범주별 일치 편차를 보고했다 | partially |

* 정리: RQ-51은 "모델을 재는 자"를 연구 대상으로 삼았다. 사용자가 K9을 "모델과 뇌 비교 수준"이라 한 지적과 같은 문제다.
* 살릴 것: (1) in-silico 결과를 믿을 영역을 정하는 관문 논리는 질문이 아니라 분석의 첫 단계(양성 대조)로 옮긴다. (2) 평균 피험자, 소리 영화 학습이라는 모델 성격을 약점이 아니라 도구의 정의로 쓴다: "정서 목표 없이 다른 사람들의 영화 시청 뇌로 학습된, 지각-언어로 계산 가능한 전형적 반응".
* 버릴 것: 무음 C&K를 주 입력으로 쓰기, 모델 충실도 자체를 결론으로 삼기, 백본 진단.

### [EF-RV-0] 보고 듣는 것만으로는 예측되지 않는 정서 반응은 뇌의 어디에 남고, 정서의 어떤 측면과 함께 움직일까?

* **자세한 질문:**
  * 정서 라벨을 한 번도 쓰지 않고 다른 사람들의 수백 시간 영화 시청 fMRI로 학습된 in-silico 뇌(TRIBE v2)는, 영상, 소리, 대사만으로 "전형적인 뇌가 이 순간 보일 반응"을 계산한다. 이를 "자극 계산 가능 성분"이라 부른다.
  * 질문 1: 실측 반응에서 이 성분을 뺀 잔차 중 사람들 사이에 공유되는(자극에 묶인) 부분이, 정서 관련 영역(anterior insula, vmPFC, sgACC/pgACC, TPJ, precuneus, amygdala)에서 감각 영역이나 신뢰도를 맞춘 대조 영역보다 더 크게 남는가?
  * 질문 2: 남는 공유 잔차는 별도 평정자의 CPM 항목 중 어느 범주(appraisal, motivation, feeling, physiology, expression, discrete)로 설명되는가?
  * 질문 3: 사람마다 다른 잔차는 그 참가자 본인의 자율신경 반응(phasic EDA, 심박 변화)과 함께 움직이는가?
* **AI가 있어야만 가능한 이유:**
  * (b) 측정할 수 없던 변수를 계산한다. "이 순간 이 영역 반응 중 지각과 언어만으로 계산되는 몫"은 관찰로 얻을 수 없다. 참가자 간 평균(ISC)은 지각 몫과 정서 몫을 함께 담고, 손으로 만든 feature(밝기, 움직임, 얼굴 유무, CNN 층)는 지각 몫의 하한만 준다.
  * (a) 통제된 비교 대상을 준다. 감각과 언어로 뇌 반응을 맞추도록만 학습된 "정서를 배우지 않은 인공 뇌"가 null이 된다. 이 null은 우리 피험자 자료로 학습되지 않으므로(zero-shot), 우리 자료의 정서 관련 mapping을 흡수할 수 없다.
* **정서와 뇌에 대해 새로 알게 되는 것:**
  * 자연 서사 영화에서 정서 관련 영역 반응 중 "강한 지각-언어 모델로도 계산되지 않지만 사람들 사이에 공유되는" 성분의 영역별 지도. Horikawa 2020이 선형 시각, 의미 공변량으로 보인 "전이 영역에서 정서 범주가 공변량을 넘어선다"는 주장을, 훨씬 강한 null 아래에서 다른 자료(소리 있는 서사 영화)로 시험한다(같은 자료 재판정이 아니다).
  * 남는 성분이 appraisal 항목(Urgency, Suddenly, Predictable, Controlled, Agent, GoalsOther 등)으로 설명되면 평가 기반 설명과, physiology 항목이나 본인 EDA로 설명되면 신체 기반 설명과 맞는다. 둘 다 아니면 주의, 기억 같은 비정서 과정을 먼저 의심한다.
  * 반대로 정서 영역의 공유 잔차가 대조 영역 수준이면 "자연 영화에서 이 영역들의 정서 관련 반응은 fMRI 해상도에서 지각-언어 계산으로 대부분 설명된다"는 결론이 되고, 지각 기반 설명(Kragel 2019, Abdel-Ghaffar 2024)을 지지한다. 어느 쪽이든 정서 이론에 구체적인 무언가를 말한다.
* **데이터:**
  * 주: Emo-FilM. 30명, 14편, 소리 있음(TRIBE v2 학습 분포 안). FSL MNI 전처리본을 fsaverage5로 투영(TRIBE v2 저장소의 MNI->fsaverage 투영 도구, 실행 전). 공유 잔차는 규범 50항목과, 개인 잔차는 본인 생리와만 연결한다(라벨 주체 분리).
  * 반복: Spacetop alignvideo. fsLR 91k CIFTI를 fsaverage5로 재표집. 시간 연속 정서 라벨이 없으므로 영상 단위 분석(영상별 공유 잔차 크기와 본인 7항목 평정의 관계)만 한다.
  * Horikawa, MC: 주 분석 제외(무음 OOD). 부록으로 "무음 OOD 스트레스 시험"(영상 경로만)만 둘 수 있고, 그 결과는 해석 제한으로 표시한다.
* **모델과 checkpoint:**
  * TRIBE v2 (facebook/tribev2, 공개, CC BY-NC 4.0 확인). 평균 피험자, 피질만. 학습 자료(Wen2017, LeBel2023, BOLD Moments, CNeuroMod)에 Emo-FilM, Spacetop 뇌 자료는 없다. 추출기(V-JEPA2-Giant, Wav2Vec-BERT 2.0, Llama-3.2-3B) 라이선스는 이번 라운드 미확인이며, Llama 계열은 접근 승인이 필요한 것으로 알려져 있다(미확인). 추출기 사전학습에 Emo-FilM 일부 공개 영화가 있었을 가능성은 배제할 수 없다(뇌 자료 오염은 아님).
  * 피질하: 공개본에 없으므로 TRIBE v2 잠재(transformer 출력)에서 leave-film-out ridge readout을 학습한 "2단계 null"을 둔다. 우리 자료로 학습되므로 zero-shot null과 분리해 보고한다.
  * GPU: A100급 1장(Emo-FilM 2.5시간 + Spacetop 1.4시간 영상 특징 추출과 추론). 나머지는 CPU.
* **핵심 분석, 예측, 반증 조건:**
  1. 관문(옛 RQ-51에서 살린 부분): zero-shot 예측의 1차 시각, 청각 피질 정확도가 leave-one-subject-out 집단 평균 ceiling의 사전 지정 비율(예: 0.5) 이상일 때만 진행한다. 미달 영역은 해석하지 않는다.
  2. 분해: 피험자, vertex(또는 Schaefer-400 parcel)마다 y = g·p + r. 이득 g와 지연은 다른 영화에서만 맞춘다(모수 2개). 공유 잔차 비율 B = 잔차의 leave-one-out ISC / 원 반응의 leave-one-out ISC.
  3. 설명: 공유 잔차를 CPM 6개 band와 저수준 nuisance band(밝기, 움직임 에너지, 음량, 장면 전환, 얼굴과 말소리 유무)로 banded ridge, leave-film-out. band별 고유 설명량. 라벨은 HRF 합성곱 후 TR 1.3 s로 재표집.
  4. 개인 잔차: 공유 잔차를 뺀 개인 잔차와 본인 phasic EDA, 심박 변화의 피험자 내 관계. BOLD 생리 잡음(RETROICOR, HRV, RVT)을 먼저 회귀한다.
  * 예측(방향만 사전 등록): P1 V1, A1의 B는 낮다(양성 대조). P2 anterior insula, vmPFC, sgACC의 B는 신뢰도를 맞춘 대조 영역(IPS, MT+, FEF)보다 크다. P3 이 영역들의 공유 잔차에서 appraisal band 고유 설명량이 discrete band보다 크다(탐색). P4 anterior insula 개인 잔차는 phasic EDA와 정적 관계(탐색).
  * 반증: P2에서 정서 영역의 B가 대조 영역과 신뢰구간이 겹치면 "지각-언어 계산 가능" 결론을 채택한다. CPM band가 circular shift한 라벨보다 공유 잔차를 더 설명하지 못하면 "정서 성분 잔차 없음"으로 결론 낸다.
* **4주 계획:**
  * 1주: Emo-FilM 전처리본, 생리, consensus 준비. TRIBE v2 설치, 14편 특징 추출과 zero-shot 예측, MNI->fsaverage5 투영, 관문 검사. Spacetop 영상과 CNeuroMod 영상 중복 확인.
  * 2주: 사전 등록 문서 고정(영역 목록, 대조 영역, 예측 방향). 잔차 분해, 잔차 ISC 지도, ceiling 정규화. 피질하 2단계 null.
  * 3주: CPM banded ridge, 생리 처리(EDA 분해, PPG 심박, RVT), 개인 잔차 분석.
  * 4주: Spacetop 반복, 강건성(전역 신호 유무, FD 검열, smoothing 맞춤), 정리.
* **가장 가까운 선행과 차이:**
  * 검색(2026-11-12): arXiv API `all:TRIBE AND all:emotion`(arXiv:2610.13558 하나, 관련 없음), `all:"in silico" AND all:emotion AND all:fMRI`(0건), `abs:fMRI AND abs:emotion AND abs:"encoding model" AND abs:naturalistic`(0건). WebSearch "emotion categories stimulus-computable perceptual encoding model residual brain response which emotions not explained by visual features fMRI Cowen Keltner videos"(관련은 Horikawa 2020뿐).
  * Horikawa et al. 2020 (doi:10.1016/j.isci.2020.101060): 정서 범주가 전이 영역에서 시각, 의미 공변량을 넘어 설명. 차이: 공변량이 선형 feature, 자료가 무음 짧은 클립과 규범 평정. 여기서는 뇌로 학습된 삼중 양식 null, 소리 있는 서사 영화, CPM 성분과 본인 생리로 분해한다.
  * EmoMind, Mohammed et al. 2026 (arXiv:2605.16739): TRIBE 합성 반응의 정서 RSA 손실. 차이: 모델 충실도 측정(옛 RQ-51 방향)이고 잔차를 정서 지식으로 쓰지 않는다.
  * Abdel-Ghaffar et al. 2024 (doi:10.1038/s41467-024-49073-8), Kragel et al. 2019 (doi:10.1126/sciadv.aaw4358): 시각 피질의 정서 관련 tuning. 차이: 정지 이미지, 시각 경로만.
  * Saarimäki et al. 2025 (doi:10.1162/imag_a_00517, abstract만): 지각된 정서와 느낀 정서의 뇌 지형. 차이: 지각 몫을 모델로 계산해 빼지 않는다.
  * Sahu & Pandey 2026 (arXiv:2607.01400), Rodrigues 2026 (arXiv:2607.16292): TRIBE 예측을 하위 과제 feature로 쓴다. 잔차 분석은 없다.
  * NeurIPS 2026 TRIBE v2 평가(neurips2026:159782)는 검색 색인만 있어 판정에 넣지 않았다.
  * 판정: partially(Horikawa 2020의 일반 주장). in-silico null 잔차를 CPM 성분과 본인 생리로 분해한 연구는 찾지 못했다.
  * overlap: Emo-FilM 연구(사전학습 멀티모달 뇌 encoding 모델로 Emo-FilM 분석). RQ-08과의 경계: RQ-08은 사람 내용 캡션을 null로 쓰는 MC 분석이고, 여기는 뇌로 학습된 모델을 null로 쓰는 소리 영화 분석이다. 보완 관계다.
* **주요 위험:**
  * 잔차는 정서가 아니다. 주의, 기억, 서사 이해도 남는다. 결론의 중심은 CPM band 설명량과 대조 영역 비교이며, 잔차 자체를 정서라 부르지 않는다.
  * 평균 피험자, 피질만이라 피질하 결론은 우리 자료로 학습한 2단계 null에 의존한다(zero-shot 아님).
  * 6 mm smoothing 볼륨의 표면 투영 오차. 강건성으로 raw 일부를 fMRIPrep으로 재전처리한다.
  * 소리 특징은 60 s 덩어리 안의 미래 정보를 담는다(TRIBE v2 Methods, Audio embeddings). 지연 분석에서 예측이 실제보다 앞설 수 있다.
  * 규범 평정의 공유 잔차 설명은 "평정자들이 보고한 정서 성분과 공변하는 뇌 반응"이지 참가자 경험이 아니다.

---

## 3. (B) 새 D1 질문

### [EF-RV-1] 영화에서 얼굴을 지워서 사라지는 정서 반응과 앞 이야기를 지워서 사라지는 정서 반응은 뇌의 서로 다른 곳에 있을까?

* **자세한 질문:**
  * 자연 영화에서는 인물의 얼굴(사회 신호)과, 그 얼굴이 왜 중요한지 정하는 앞 이야기(맥락)가 늘 함께 나온다. 그래서 관찰 encoding으로는 amygdala, anterior insula, pSTS, vmPFC, TPJ 반응이 얼굴 자체 때문인지 맥락이 정한 관련성(relevance) 때문인지 가를 수 없다(공선성).
  * in-silico 뇌에 같은 장면의 원본, 얼굴만 지운 판, 앞 맥락만 지운 판, 둘 다 지운 판을 넣어 2×2 요인 예측을 얻고, 영역마다 얼굴 효과, 맥락 효과, 상호작용을 계산한다.
  * 이 예측을 사전 등록한 뒤 관찰 자료 두 곳에서 검증한다. (i) Spacetop: 같은 참가자가 alignvideo에서 맥락 속에 본 인물 장면을 수일 뒤 shortvideo에서 맥락 없이 다시 본 반응 차이. (ii) Emo-FilM held-out 영화: 자연 발생한 얼굴 유무와 규범 appraisal(Urgency, GoalsOther, PleasantSelf)의 상호작용.
* **AI가 있어야만 가능한 이유:**
  * (a) 관찰로 얻을 수 없는 반사실 자극(같은 장면의 얼굴 없는 판, 맥락 없는 판)에 대한 뇌 반응을 얻는다. 사람에게 2×2를 보이려면 새 수집이 필요하고, 같은 사람에게 같은 장면을 두 번 보이면 반복 효과가 섞인다.
  * (c) 영역별 효과의 방향과 크기라는 검증 가능한 가설을 만들고, 독립 관찰 자료로 시험한다(in-silico 가설 -> 사전 등록 -> 관찰 검증).
* **정서와 뇌에 대해 새로 알게 되는 것:**
  * amygdala가 얼굴 같은 사회 신호의 탐지기인지, 맥락이 정한 관련성의 탐지기인지(Sander et al. 2003)를 자연 영화 조건에서 요인 분해한 증거를 얻는다. 탐지기 설명은 얼굴 주효과가 맥락과 무관(가산), 관련성 설명은 얼굴 효과가 맥락이 있을 때만 큰 상호작용을 예측한다.
  * pSTS는 얼굴 효과, vmPFC와 TPJ는 맥락 효과가 클 것으로 예상하며, 이 배치가 관찰과 맞는지가 핵심이다. in-silico와 관찰이 어긋나는 영역(예: hippocampus, precuneus처럼 기억이 개입하는 곳)은 "지각 맥락이 아니라 기억 맥락이 필요하다"는 증거로 읽는다. 모델 실패 위치가 곧 정보가 된다.
* **데이터:**
  * in-silico 입력과 피질하 readout 학습: Emo-FilM 14편(소리 있음, 학습 분포 안).
  * 관찰 검증 1: Spacetop alignvideo + shortvideo(21개, 99명, 블록별 호감, 유사성, mentalizing 판단 과제). shortvideo 클립이 alignvideo의 정확히 같은 프레임인지, 소리가 있는지는 미확인이다. 1주차에 프레임 임베딩 대조로 확인한다.
  * 관찰 검증 2: Emo-FilM held-out 영화(leave-film-out). 얼굴 유무는 자동 검출로 만든 자극 특징(묘사된 내용)이지 정서 라벨이 아니다.
  * 보조: Spacetop faces(동적 얼굴 1.3~2.1 s, 8표정, 맥락 없음)를 "맥락 없는 얼굴"의 관찰 기준으로.
* **모델과 checkpoint:**
  * TRIBE v2 (공개, CC BY-NC 4.0 확인). 영상 경로는 직전 4 s만 보므로, 긴 맥락은 텍스트(앞 단어 문맥)와 transformer 창이 맡는다.
  * 맥락 제거 세 방식: (1) 텍스트 문맥을 현재 문장으로 자르기(설정 max_context_len 축소), (2) transformer 창 안 이전 시간 단계 입력을 0으로 두기(학습 때 dropout 규약과 같은 형태, 코드 확인, 실행 전), (3) 다른 영화 맥락으로 바꾸기(맥락 교체 대조).
  * 얼굴 제거: 공개 얼굴 검출, 추적 모델과 video inpainting 모델(각 라이선스 미확인). 최소안은 얼굴 영역 blur 또는 mosaic. 편집 artifact 대조로 같은 면적 비얼굴 영역 편집판을 만든다.
  * 피질하: TRIBE v2 잠재 + leave-film-out readout(EF-RV-0과 공유).
  * GPU: A100급 1~2장(편집판 4종 × 14편 특징 추출, inpainting).
* **핵심 분석, 예측, 반증 조건:**
  1. in-silico 2×2: 영역 r, 시점 t마다 얼굴 효과, 맥락 효과, 상호작용. 정서 순간(규범 IntenseEmotion 상위 20%)과 중립 순간으로 나눈다.
  2. 사전 등록 산출물: 영역별 효과 순위와 부호, amygdala 상호작용 부호.
  3. 관찰 검증 1: shortvideo 시점과 같은 alignvideo 시점의 반응 차(맥락 있음 - 맥락 없음)를 영역별로 계산하고 V1의 반복 효과로 정규화한다. in-silico 맥락 효과 순위와 Spearman 상관(영역 약 20개, 순열 검정).
  4. 관찰 검증 2: held-out 영화에서 얼굴 유무 × appraisal 상호작용 회귀(저수준 nuisance 포함). amygdala 상호작용 부호가 in-silico와 같은지.
  * 예측: P1 pSTS, FFA는 얼굴 효과 우세(양성 대조). P2 vmPFC, TPJ, precuneus는 맥락 효과 우세. P3 amygdala는 관련성 설명이 맞으면 상호작용 양(+), 탐지기 설명이면 상호작용 0 근처와 얼굴 주효과.
  * 반증: 검증 1의 순위 상관이 사전 기준(순열 p < 0.05)에 못 미치면 in-silico 맥락 조작이 뇌의 맥락 효과를 대표하지 못한다고 결론 내고 P2, P3 해석을 멈춘다. 검증 2에서 amygdala 상호작용 부호가 반대면 in-silico 가설을 기각한다.
* **4주 계획:**
  * 1주: Emo-FilM 얼굴 검출, 추적, 편집판 4종(+ artifact 대조) 생성과 품질 점검. Spacetop shortvideo와 alignvideo 프레임 대응, 소리 유무 확인.
  * 2주: TRIBE v2 추론, 피질하 readout, 2×2 효과 지도. 주말에 사전 등록 고정(타임스탬프가 남는 저장소).
  * 3주: 관찰 검증 1(fsLR CIFTI, 99명), 관찰 검증 2(Emo-FilM held-out).
  * 4주: 강건성(편집법 2종, 맥락 제거 3방식), 실패 영역 정리, 보고.
* **가장 가까운 선행과 차이:**
  * 검색(2026-11-12): WebSearch "in silico perturbation encoding model video faces removed motion frozen amygdala insula response prediction emotional videos fMRI"(직접 해당 없음, Jang & Kragel 2025와 VIBE만). arXiv API `abs:"in silico" AND abs:fMRI AND abs:"encoding model"`(arXiv:2609.15685, 2510.21142, 2605.04326, 2609.36391), `abs:fMRI AND abs:emotion AND abs:perturbation AND abs:video`(0건), `all:"encoding model" AND "in silico" AND ablation AND fMRI`(0건), `amygdala AND "encoding model" AND video`(0건). PubMed "amygdala faces movie fMRI naturalistic emotion"(2건: 자료 공개 논문 1, Kirk 2022).
  * Jang & Kragel 2025 (doi:10.1523/JNEUROSCI.1436-24.2025): 영화 1편으로 학습한 amygdala encoding 모델에 이미지 합성 in-silico 실험, 붉은색과 고공간주파수 민감. 차이: 정지 시각 feature, 맥락과 소리 없음, in vivo 검증 미보고.
  * Hwang et al. 2025 (arXiv:2510.21142): digital twin encoder로 parcel 선택성 가설 생성, Limitations에서 새 fMRI 검증이 없다고 명시. 차이: 정서 아님, 정지 이미지, 관찰 검증 없음.
  * Ratan Murty et al. 2021 (doi:10.1038/s41467-021-25409-6), Gifford et al. 2025 (doi:10.1038/s41562-025-02252-z): in-silico 선택성 탐색. 차이: 시각 범주.
  * Nasirzadeh Orang et al. 2026 (arXiv:2609.15685, abstract만): encoding 모델이 기존 fMRI 연구를 재현하는지. 차이: 재현이지 새 가설의 사전 등록 검증이 아니다.
  * Kirk et al. 2022 (doi:10.1016/j.neuropsychologia.2022.108194): 영화 fMRI에서 얼굴 의존 amygdala 연결의 불안 관련성이 재현되지 않음. 관찰 연구.
  * 판정: no(찾은 범위). 정서 영화에 대한 in-silico 요인 편집과 관찰 사전 등록 검증의 조합은 찾지 못했다.
  * overlap: Emo-FilM 연구(맥락 정보와 사전학습 encoding 모델). RQ-52(소리 stem 제거)와 같은 틀이지만 조작 요인(얼굴, 맥락)이 다르다. RQ-33(MC 앞 클립 맥락)과 주제가 닿는다.
* **주요 위험:**
  * 편집 영상은 학습 분포 밖이다. inpainting artifact가 예측을 바꿀 수 있어 artifact 대조판과 편집법 두 가지를 둔다.
  * 대사가 적은 영화(일부 애니메이션)에서는 텍스트 맥락 조작이 약하다. 맥락 효과 결론은 대사가 있는 영화로 한정한다.
  * 검증 1에는 반복 노출, 기억, 과제 차이가 섞인다. V1 정규화로 일부만 제거된다. 기억 영역의 불일치는 사전에 "예상된 실패"로 적어 둔다.
  * 평균 피험자 모델이라 개인차는 다루지 않는다(EF-RV-4의 몫).
  * 한 달 안에 편집 파이프라인이 늦어지면 blur 최소안으로 축소한다.

### [EF-RV-2] 몸이 크게 반응하는 정서 순간에, 섬엽은 나머지 대뇌피질만 보고는 짐작할 수 없는 상태가 될까?

* **자세한 질문:**
  * brain foundation model(CortexMAE)은 HCP-YA 2,058시간(휴지, 7개 과제, 영화)에서 대뇌피질 활동이 공간과 시간에 걸쳐 어떻게 함께 움직이는지 masked reconstruction으로 배웠다. 정서 라벨은 쓰지 않았다.
  * 한 영역(anterior insula, dACC, sgACC/vmPFC, 대조 영역)을 16초 동안 가리고 나머지 피질로 복원하게 하면, 복원 오차는 "그 순간 그 영역이 전형적 피질 역학에서 얼마나 벗어나 있는가"를 준다. 이를 cortical inferability의 반대로 쓴다.
  * 주 질문: 참가자 본인의 phasic EDA나 심박 가속이 큰 순간에, anterior insula의 복원 오차는 대조 영역과 대조 사건(장면 전환, 음량 급증처럼 현저하지만 자율신경 반응이 작은 순간)보다 커지는가, 오히려 작아지는가?
  * 부 질문(FM embedding + emotion head를 probe로): 규범 CPM 항목 정보는 모델이 복원할 수 있는 "전형적 역학 성분"에 실리는가, 복원되지 않는 "잔차 성분"에 실리는가?
* **AI가 있어야만 가능한 이유:**
  * (b) "어떤 영역이 이 순간 나머지 피질과 얼마나 어긋나는가"는 수천 시간의 피질 역학을 학습한 모델이 있어야 순간 단위로 계산된다. 한 사람 2.5시간 자료로 만든 선형 기능 연결 예측기는 기준선으로 함께 보고한다. FM의 몫은 수천 명의 휴지와 과제 역학이라는 모집단 prior다.
  * (a) 가린 영역에 대해 "전형적 피질이 예상하는 활동"은 반사실 값이다. 관찰로 얻을 수 없다.
* **정서와 뇌에 대해 새로 알게 되는 것:**
  * 신체 반응이 큰 정서 순간의 섬엽 활동이 (i) 피질 바깥(상행 내수용 신호, 피질하)에서 온 정보를 담아 나머지 피질과 어긋나는지, (ii) salience network 전체의 동시 활성으로 피질에서 잘 짐작되는지를 가른다. (i)은 SCR과 공변하는 섬엽 활동을 신체 신호 표상으로 보는 쪽(Critchley et al. 2000)과, (ii)는 피질 예측이 내수용을 주도한다는 쪽(Barrett & Simmons 2015)과 더 잘 맞는다. 단 fMRI만으로 예측 신호와 오차 신호를 직접 가를 수 없으므로, 이 대응은 "관찰로 구분할 수 없는 해석 가설"로 표시한다.
  * 정서 정보가 일반 뇌 역학 다양체 위에 있는지 밖에 있는지는, 정서가 영역 일반 네트워크의 조합으로 만들어진다는 설명과 정서 특이 미세 패턴이 있다는 설명을 가르는 계산 시험이 된다.
* **데이터:**
  * 주: Emo-FilM. 참가자 30명의 EDA, PPG, 호흡 1000 Hz가 전 런에 있다(StartTime 부호 확인 필요). 규범 50항목 1 Hz. FSL MNI 전처리본(2.5 mm, 6 mm smoothing)을 CortexMAE volume 입력(MNI152 2 mm 피질)으로 재표집하고, TR 1.3 s를 1 s로 선형 보간한다(CortexMAE 평가 규약과 같음).
  * 반복 1: Spacetop alignvideo. fsLR 91k CIFTI를 flat map 입력으로, TR 0.46 s를 1 s로. 생리 미공개라 영상 단위 본인 평정(afraid, engaged 등)과만 연결한다.
  * 반복 2(선택): MC 원시 연속 자료(ds005191 재전처리 필요, 보유본 형식 미확인). 부 질문(on/off-manifold의 규범 34범주 정보)만.
  * Horikawa는 블록 평균본 위주라 이 질문에 맞지 않는다.
* **모델과 checkpoint:**
  * CortexMAE (HF medarc/CortexMAE, 공개). 코드 Apache-2.0, 가중치 CC BY-NC 4.0(확인). volume, flat, parcel 세 판. HCP-YA EMOTION 과제(얼굴 정서 과제)가 사전학습에 들어 있어 "전형적 역학"에 정서 과제 상태가 일부 포함됨을 결과에 표시한다. 피질만이라 amygdala는 없다.
  * 피질하 보조(선택): Brain-JEPA(Tian S3 피질하 포함, LICENSE 없음) 또는 NeuroSTORM(라이선스 표기 불일치). 라이선스 확인 전에는 결과 공개용으로 쓰지 않는다.
  * 제외: Brain-DiT(Emo-FilM, NSD가 사전학습에 포함, 오염).
  * GPU: ViT-B 추론, 1장으로 충분(30명 × 14편 × 영역 약 20개 × mask 반복 수십 회).
* **핵심 분석, 예측, 반증 조건:**
  1. 관문: Emo-FilM에서 무작위 mask 복원 R²가 CortexMAE 논문의 NSD OOD 수준보다 극단적으로 낮지 않은지 본다. 낮으면 parcel 판으로 바꾸거나 raw 재전처리(fMRIPrep -> fsLR -> flat)로 간다.
  2. 영역 mask 복원 오차 e_r(t): 영역 r을 16 frame 전체 가리고(tube) 나머지로 복원, 창을 1 s씩 이동. 런 안에서 z-score(전처리 차이로 생기는 상수 이동 제거).
  3. 사건 고정 분석: 본인 phasic EDA 반응 시작, 심박 가속 구간 대 대조 사건(장면 전환, 음량 급증 중 EDA 반응 없음)과 무작위 시점. 혼합 모형(피험자, 영화 무작위 효과).
  4. 기준선: 다른 영화로 학습한 선형 ridge(다른 parcel -> 대상 parcel), VAR(1), 같은 피험자 휴지 런 기반 예측기.
  5. 부 질문: CPM 항목 decoding을 (i) FM encoder 잠재, (ii) FM denoise 복원 성분, (iii) 잔차(관찰 - 복원), (iv) 원 신호로 비교. leave-film-out과 leave-subject-out 둘 다.
  * 예측: P1은 양방향으로 사전 등록한다. EDA 사건에서 insula의 Δe가 대조 사건과 V1, 손 운동 영역보다 크면 피질 바깥 정보 쪽, 작으면 피질 주도 쪽. 어느 방향이든 보고한다. P2 전역 비전형 지수(모든 영역 평균 복원 오차)는 규범 IntenseEmotion, Alert와 정적 관계(탐색). P3 CPM decoding 정보의 대부분이 복원 성분에 있으면 영역 일반 역학 위 표상으로 본다(비율 기준은 사전 등록).
  * 반증: 생리 잡음 회귀(RETROICOR, HRV, RVT) 뒤 P1 효과가 사라지거나 대조 사건과 같은 크기면 "섬엽 고유 정보" 해석을 버린다. FM이 선형 기준선보다 낫지 않으면 FM의 기여 주장은 버리고 선형 결과로 보고한다.
* **4주 계획:**
  * 1주: Emo-FilM 자료, 생리 처리(EDA 분해, PPG peak, RVT, StartTime 정렬), CortexMAE 설치와 volume reader 확인, 복원 품질 관문.
  * 2주: 사전 등록 고정. 영역 mask 복원 시계열 계산, 기준선 모형.
  * 3주: 사건 고정 분석, 생리 잡음 강건성, FD 검열, 전역 신호 유무 두 판.
  * 4주: 부 질문 probe, Spacetop 반복(flat), 정리.
* **가장 가까운 선행과 차이:**
  * 검색(2026-11-12): arXiv API `all:"reconstruction error" AND fMRI AND "foundation model"`(0건), `"normative model" AND "brain dynamics" AND emotion`(0건), `abs:fMRI AND "masked autoencoder" AND anomaly`(0건), `abs:fMRI AND abs:emotion AND abs:"reconstruction error"`(0건), `abs:fMRI AND abs:"masked" AND abs:insula`(0건), `abs:fMRI AND abs:interoception AND abs:"deep learning"`(0건), `"brain foundation model" AND emotion`(EEG 연구만). WebSearch "fMRI brain dynamics foundation model reconstruction error deviation emotional arousal naturalistic movie off-manifold OR normative model brain state emotion"(식별자 있는 해당 연구 없음; 학회 초록 2건은 식별자가 없어 판정에서 제외). PubMed "skin conductance movie fMRI insula"(0건), "Emo-FilM"(자료 논문 1건만).
  * Lane et al. 2025, CortexMAE (arXiv:2510.13768): masked reconstruction과 denoise를 보였고, Discussion에서 동적 정신 상태 예측을 향후 과제로 둔다. 정서, 생리와 연결하지 않았다.
  * Thomas et al. 2022 (arXiv:2206.11417): 뇌 역학 자기지도 학습. 정서 아님.
  * Critchley et al. 2000 (doi:10.1523/JNEUROSCI.20-08-03033.2000): SCR과 공변하는 우측 anterior insula, OFC. 과제 기반, 모델 없음.
  * Gaviria et al. 2021 (doi:10.1002/hbm.25277), Borchardt et al. 2018 (doi:10.1093/cercor/bhx290): 정서 영화 중 기능 연결 역학. 차이: 순간 단위 영역 inferability를 모델로 계산하지 않고, 본인 생리 사건 고정 분석이 없다.
  * 판정: no(찾은 범위). 학회 초록은 확인 범위 밖이다.
  * overlap: Emo-FilM 연구와 자료만 겹친다(방법 다름).
* **주요 위험:**
  * 섬엽 근처는 혈관성 생리 잡음이 크다. 가장 큰 위험이라 1순위 강건성으로 둔다. EDA를 주 각성 지표로 쓰는 이유도 심박, 호흡보다 BOLD에 직접 섞이는 정도가 작기 때문이다(그래도 0은 아니다).
  * 전처리, smoothing, TR 보간에 따른 분포 이동이 영역마다 다를 수 있다. 런 내 z-score와 대조 영역 비교로 줄이고 raw 재전처리 일부로 확인한다.
  * 복원 오차는 움직임이 큰 순간에 커진다. 놀람 장면에서 FD가 같이 오를 수 있어 FD 공변량과 검열을 둔다.
  * 결과는 "피질에서의 짐작 가능성"이지 인과 경로가 아니다. 상행 신호 때문인지는 이 자료로 확정할 수 없다.

### [EF-RV-3] 정서 관련 뇌 반응은 얼마나 먼 과거의 이야기까지 끌어와서 만들어질까?

* **자세한 질문:**
  * 같은 장면도 앞 이야기에 따라 정서가 달라진다. 뇌의 각 영역이 정서적 순간에 몇 초, 몇 분 전의 이야기까지 통합하는지는 사람에게서 직접 조작하기 어렵다.
  * 같은 언어 모델에 현재 입력은 고정하고 볼 수 있는 과거 길이만 0초에서 처음부터까지 바꾼 "맥락 길이가 다른 인공 이해자" 계열을 만든다. 각 영역 반응을 가장 잘 예측하는 맥락 길이(통합 창)를 추정한다.
  * 질문 1: 통합 창은 정서가 강한 순간에 중립 순간보다 길어지는가? 그 효과는 어느 영역(vmPFC, PCC, TPJ, anterior insula, amygdala)에 있는가?
  * 질문 2: 참가자 본인 또는 별도 평정자의 정서 보고를 예측하는 데 필요한 맥락 길이(평정 창)와 뇌의 통합 창은 일치하는가? appraisal 항목과 physiology, expression 항목의 창은 다른가?
* **AI가 있어야만 가능한 이유:**
  * (a) 현재 입력은 같고 과거만 다른 비교는 사람에게는 scramble 실험(새 수집, 자극 훼손) 없이는 할 수 없다. 언어 모델의 문맥 길이는 정확히 조절되는 손잡이다. 같은 길이의 다른 이야기 맥락(맥락 교체)으로 "길이"와 "관련 내용"을 가른다.
  * (b) 영역별, 순간 유형별 정서 통합 창이라는 측정할 수 없던 변수를 계산한다.
* **정서와 뇌에 대해 새로 알게 되는 것:**
  * 정서 반응이 순간 지각에 묶이는지, 서사 누적(평가 이론이 말하는 목표 관련성과 예측 가능성의 누적 평가)에 기대는지를 영역별로 정량화한다. 기존 TRW 위계(Lerner et al. 2011)는 이해 일반의 시간 척도이고, 정서적 순간에 창이 늘어나는지는 다루지 않았다.
  * 평정 창과 뇌 창의 대응: appraisal 평정이 긴 맥락을 요구하고 vmPFC 창이 그와 맞으면, vmPFC가 서사에 누적된 평가를 운반한다는 구체적 증거가 된다. amygdala 창이 정서 순간에도 짧으면 빠른 탐지형 기여를 시사한다(탐색).
* **데이터:**
  * 주 1: Spacetop narratives. 연구실 제작 이야기 8편 × 9 clip(4편 소리, 4편 텍스트), 원문 txt 공개, 참가자 본인의 clip별 "지금 느낌"(good-bad, 강도)과 기대(응답률 0.98), 약 105명, TR 0.46 s, fsLR CIFTI. 자체 제작 이야기라 언어 모델 사전학습 오염이 낮다. 소리 이야기의 단어 시각은 강제 정렬로 만든다(onset은 clip 단위만 제공). 텍스트 이야기의 제시 방식과 속도는 events 파일로 확인 필요.
  * 주 2: Emo-FilM 14편. 대사(자동 전사)와 장면 기술(VLM, 2 s 단위)을 시간 정렬한 서사 텍스트. 장면 기술은 모델 생성 주석(묘사된 내용)으로 표시한다. 규범 50항목 1 Hz.
  * Horikawa, MC는 맥락 없는 짧은 클립이라 주 자료가 아니다. MC의 의사 무작위 순서 맥락은 RQ-33의 몫이다.
* **모델과 checkpoint:**
  * 개방 가중치 언어 모델 두 계열(예: Llama 계열 8B급, Qwen 계열 7B급)의 중간층 은닉 상태. 라이선스 이번 라운드 미확인. 두 계열에서 결론이 같아야 채택한다.
  * 자동 전사(Whisper 계열), 장면 기술 VLM: 라이선스 확인 필요. Emo-FilM 일부는 웹 공개 영화라 VLM, LLM이 줄거리를 알 수 있다. 맥락 0에서 다음 사건을 맞히는지 보는 지식 probe로 점검하고, 인물 이름은 익명화한다.
  * TRIBE v2는 보조: 텍스트 경로 문맥 길이를 줄인 비교를 부록으로만.
  * GPU: 7~8B 모델 추론. 맥락 9단계 × 두 자료(약 1만 2천 TR) × 2계열. KV cache 재사용 시 A100급 1~2장으로 1~2일 예상(직접 측정 전).
* **핵심 분석, 예측, 반증 조건:**
  1. 특징: TR t마다 과거 k초(k = 0, 4, 8, 16, 32, 64, 128, 256 s, 처음부터)의 텍스트만 보이게 한 은닉 상태. 맥락 교체 대조(같은 길이, 다른 이야기).
  2. encoding: 피험자별(Spacetop은 집단 평균도) parcel ridge, leave-story-out 또는 leave-film-out, HRF 지연 FIR. 영역별 k-이득 곡선과 통합 창 W(최대 이득의 50%에 이르는 k).
  3. 순간 유형: 같은 모형의 예측 정확도를 정서 강한 시점(Spacetop: 본인 평정 강도 상위 clip, Emo-FilM: 규범 IntenseEmotion 상위)과 중립 시점으로 나눠 계산한다. 대사 밀도, 장면 변화량을 맞춘다.
  4. 평정 창: 같은 특징으로 평정을 예측해 항목별 W_rating을 구한다. Spacetop은 본인 평정, Emo-FilM은 규범 평정으로 따로 보고한다.
  * 예측: P1 1차 청각, 시각 피질 W는 짧고 DMN은 길다(양성 대조, Lerner 2011 재현). P2 vmPFC, anterior insula에서 정서 순간 W가 중립 순간 W보다 길다(핵심, 방향 사전 등록). P3 appraisal 항목 W_rating이 expression, physiology 항목보다 길다(Emo-FilM, 탐색). P4 맥락 교체는 같은 길이 실제 맥락보다 이득이 작다.
  * 반증: P2에서 정서 순간과 중립 순간의 W 차이가 모든 영역에서 0과 구분되지 않으면 "정서 반응이 서사 이해 일반보다 긴 통합을 요구한다"는 가설을 기각한다. P4가 실패하면(교체 맥락도 같은 이득) 이득을 길이 artifact로 보고 해석하지 않는다.
* **4주 계획:**
  * 1주: Spacetop narratives 텍스트, 소리 이야기 강제 정렬, 텍스트 제시 시각 확인, CIFTI parcellation(Schaefer-400 + 피질하). Emo-FilM 전사, 장면 기술 생성.
  * 2주: 두 언어 모델 계열 특징 추출(맥락 9단계 + 교체), 지식 probe. 사전 등록 고정.
  * 3주: encoding, k-이득 곡선, 정서-중립 비교, 평정 창.
  * 4주: 강건성(층 선택, 정규화, HRF 지연 4~6 s), 영역 간 다중비교(FDR), 정리.
* **가장 가까운 선행과 차이:**
  * 검색(2026-11-12): PubMed "temporal receptive window emotion narrative fMRI"(1건, Jääskeläinen et al. 2020 리뷰), PubMed "(temporal receptive window OR context length OR narrative context) AND (emotion OR affective) AND encoding model AND fMRI AND movie"(0건), arXiv API `abs:fMRI AND abs:emotion AND abs:"context length"`(0건), `abs:"long-context" AND abs:fMRI AND abs:movie`(Jindal 2026만), WebSearch "how much narrative context needed to predict emotion brain responses encoding model language model context length vmPFC amygdala movie"(Jindal 2026; 학회 포스터는 식별자 없음).
  * Lerner et al. 2011 (doi:10.1523/JNEUROSCI.3684-10.2011, abstract만): scramble로 TRW 위계. 차이: 자극 훼손 방식, 정서 순간 구분 없음.
  * Jindal et al. 2026 (arXiv:2602.07570): clip 길이 3~24 s에서 MLLM-뇌 정렬이 늘고 긴 창이 고차 영역과 맞음. 부록 K Limitations: 분 단위 창은 계산 문제로 미래 과제, Movie10 4명. 차이: 정서 없음, 분 단위 없음, 맥락 교체 대조 없음.
  * Zhang et al. 2026 (arXiv:2606.07707, abstract만): LLM 생성 연속 정서 주석으로 이야기 fMRI 정서 동역학 decoding. 차이: 맥락 길이 조작 없음, 주석이 모델 생성.
  * Miao et al. 2026 (doi:10.1038/s41467-026-71151-2, abstract만): Spacetop narratives의 사회 상호작용, ToM 평정과 fMRI. 차이: 정서와 맥락 길이가 아님.
  * 판정: partially(맥락 길이와 뇌 정렬의 일반 관계는 Jindal 2026, TRW는 Lerner 2011). 정서 순간 특이적 통합 창과 평정 창 대응은 찾지 못했다.
  * overlap: Emo-FilM 연구(정서 맥락과 시간 정보의 기여를 사전학습 encoding 모델로 분석)와 직접 겹친다. 차이는 맥락 길이를 조절한 모델 계열, 맥락 교체 대조, 평정 창 비교, 오염이 적은 Spacetop 이야기 주 자료다. RQ-33과 주제가 닿는다.
* **주요 위험:**
  * Spacetop narratives 정서 평정은 clip 단위(72개)라 평정 창 추정의 검정력이 낮다. Emo-FilM 1 Hz 규범 평정이 보완하지만 주체가 다르다(본인 대 별도 평정자). 두 결과를 섞지 않는다.
  * Emo-FilM 장면 기술에 VLM의 정서 해석이 섞일 수 있다. 정서 어휘를 막는 생성 지시와 사후 필터를 둔다.
  * 텍스트 이야기는 읽기 속도가 사람마다 달라 단어 시각이 어긋날 수 있다. 소리 이야기 결과를 우선한다.
  * 긴 맥락의 은닉 상태 norm 변화 같은 기술적 artifact. 층 정규화와 교체 대조로 점검한다.

### [EF-RV-4] 사람마다 다른 정서 뇌 반응은 영화가 바뀌어도 유지되는, 그 사람만의 반응 성향일까?

* **자세한 질문:**
  * 같은 영화를 보아도 정서 관련 영역의 반응은 사람마다 다르다(Chang et al. 2021의 vmPFC). 이 차이가 영화마다 새로 생기는 잡음인지, 영화가 바뀌어도 유지되는 개인 성향인지는, 한 사람이 볼 수 있는 영화 수가 적어 관찰로 확인하기 어렵다.
  * 피험자마다 in-silico 뇌의 개인 head를 일부 영화로 맞춘 "개인 디지털 트윈"을 만든다. (i) 처음 보는 영화에서 그 사람의 정서 순간 반응을 다른 사람의 트윈보다 잘 맞히는가(개인 식별성)? (ii) 트윈에 많은 장면을 보여 얻은 개인 반응 지문이 그 사람의 실제 held-out 반응 편차를 미리 맞히는가?
* **AI가 있어야만 가능한 이유:**
  * (a) 같은 사람에게 수백 개의 다른 장면을 보인 반응은 관찰로 얻을 수 없다. 트윈은 그 사람이 보지 않은 자극에 대한 반사실 반응을 준다.
  * (c) 트윈에서 얻은 지문은 "이 사람은 어떤 정서 성분에서 섬엽, vmPFC가 남보다 크게 반응한다"는 개인 단위 가설이 되고, held-out 영화로 사전 검증한다.
* **정서와 뇌에 대해 새로 알게 되는 것:**
  * 자연 영화에서 정서 관련 뇌 반응의 개인차가 성향처럼 안정적인지, 어느 영역과 어느 CPM 성분에서 안정적인지. 감각 영역의 개인차(해부, 정합 차이)와 구분되는 "정서 순간 특이적" 개인차가 있으면 affective style의 신경 수준 증거가 된다.
  * 지문이 본인 사후 평정, 몰입 평정의 개인차와 맞으면, 경험 정서(본인)와 규범 정서(평정자)의 차이가 뇌 반응 성향에 실려 있다는 단서가 된다(n=30이라 탐색).
* **데이터:**
  * 주: Emo-FilM 30명 × 14편(2.5시간 이상, 소리 있음). TRIBE v2 논문은 새 피험자 적응에 1시간 남짓으로 충분하다고 보고한다. 7편으로 트윈 학습, 7편으로 검증, 교차.
  * 본인 자료: 사후 클립 회고 평정(희소), 영화별 몰입, 즐거움, 흥미, 생리. 질문지는 있으나 공개 경로 미확인.
  * 반복: Spacetop alignvideo(약 100명, 86분, 본인 영상 후 7항목, 같은 순서). 식별성 분석만.
* **모델과 checkpoint:**
  * TRIBE v2 (공개, CC BY-NC 4.0). 비상업 연구용 미세조정은 허용 범위로 해석하나 기관 확인 필요. 학습 의존성(training extras)과 subject layer 크기 조정 옵션이 코드에 있다(실행 전). 특징은 EF-RV-0에서 한 번 추출한 것을 재사용하고 개인 head만 학습한다.
  * GPU: A100급 1~2장. 30명 × 2 fold head 학습 시간은 직접 측정 전.
* **핵심 분석, 예측, 반증 조건:**
  1. 트윈 학습: 피험자 s의 7편으로 head 학습(평균 모델로 초기화), 나머지 7편 예측.
  2. 개인 식별성: held-out에서 자기 트윈과 타인 트윈의 예측 정확도 차이(식별 정확도)를 영역별, 순간 유형별(정서 강한 순간 대 중립)로 계산. 대조: V1, A1.
  3. 개인 지문: 모든 트윈에 공통 탐침 자극(다른 fold 영화, 소리 있는 Spacetop 영상)을 넣고, 예측 반응을 규범 CPM 항목에 회귀해 항목별 개인 감도 벡터를 얻는다(평균 트윈 대비 편차).
  4. 사전 검증: 지문으로 held-out 영화에서 그 사람의 관찰 반응 편차(집단 평균 대비)를 예측. 본인 평정과의 관계는 탐색으로만.
  * 예측: P1 정서 관련 영역의 식별 이득은 정서 순간에 더 크다. P2 감각 영역의 식별 이득은 순간 유형과 무관하다(해부 개인차 대조). P3 지문 기반 예측이 held-out 영화에서 우연 이상.
  * 반증: P1에서 정서 순간과 중립 순간의 식별 이득 차이가 없거나 정서 영역 이득이 감각 영역과 같은 양상이면, "정서 특이적 개인 성향" 주장을 버리고 해부, 잡음 개인차로 결론 낸다.
* **4주 계획:**
  * 1주: TRIBE v2 학습 환경, Emo-FilM fsaverage5 투영과 특징(EF-RV-0과 공유).
  * 2주: 30명 × 2 fold 트윈 학습, 학습 곡선, 식별성 분석. 사전 등록 고정.
  * 3주: 탐침 자극 지문, 사전 검증.
  * 4주: Spacetop 반복(식별성), 정리.
* **가장 가까운 선행과 차이:**
  * 검색(2026-11-12): arXiv API `abs:fMRI AND abs:"digital twin" AND abs:"individual differences"`(0건), `abs:"encoding model" AND abs:"individual differences" AND abs:emotion`(1건, 의미 표상 연구 arXiv:2606.11598, 정서 아님), `abs:"digital twin" AND abs:fMRI AND abs:emotion`(0건). WebSearch "personalized brain encoding model digital twin individual differences emotional responses fMRI movies fine-tuned per subject predicts held-out films"(정서 대상 연구 없음).
  * Chang et al. 2021 (doi:10.1126/sciadv.abf7129): vmPFC 반응의 개인 특이성과 정서 경험. 차이: 영화 한 편, 영화 간 안정성 시험과 트윈 탐침 없음.
  * d'Ascoli et al. 2026, TRIBE v2 (arXiv:2605.04326): 새 피험자 적응. 차이: 정서, 개인 성향 분석 없음.
  * Wang et al. 2025 (doi:10.1038/s41586-025-08829-y): 쥐 시각 피질 foundation model이 새 개체, 새 자극에 일반화. 차이: 종, 정서 아님.
  * Gifford et al. 2025 (doi:10.1038/s41562-025-02252-z): in-silico 탐색. 차이: 시각.
  * 판정: no(찾은 범위).
  * overlap: Emo-FilM 연구(사전학습 encoding 모델 + Emo-FilM). EmoBrain(교차 피험자 정서 decoding)과 개인차라는 반대 방향에서 닿는다.
* **주요 위험:**
  * 트윈 개인차가 정합, 해부 차이에서 올 수 있다. 정서 순간 상호작용과 감각 영역 대조로 가른다.
  * n=30이라 질문지 연관은 검정력이 없다. 주 결과는 개인 내 일반화(식별성, 사전 검증)다.
  * 6 mm smoothing 볼륨을 표면 투영하면 개인 미세 패턴이 흐려져 식별성이 과소 추정된다.
  * 1시간 남짓 자료로는 개인 head가 평균 모델에서 크게 벗어나지 못할 수 있다. 학습 곡선으로 보고한다.
  * TRIBE v2 학습 스택 설정이 늦어지면 한 달 안 완료가 어렵다(실행성 3으로 본 이유).

---

## 4. 질문 사이의 관계와 경계

* **공유 기반:** EF-RV-0, 1, 4는 "Emo-FilM -> fsaverage5 투영 + TRIBE v2 특징" 한 벌을 공유한다. EF-RV-2는 CortexMAE 파이프라인, EF-RV-3은 언어 모델 맥락 특징을 따로 쓴다. 한 사람이 둘을 묶어 하면 EF-RV-0 + EF-RV-2가 1주차 준비를 가장 많이 공유한다(Emo-FilM 생리 처리).
* **EF-RV-1과 EF-RV-3:** 둘 다 맥락을 다룬다. EF-RV-1은 얼굴과 맥락의 상호작용(무엇이 반응을 만드는가), EF-RV-3은 맥락의 길이(얼마나 먼 과거인가)다. 하나만 고른다면 실행성이 높은 EF-RV-3이 낫고, EF-RV-1의 맥락 요인은 EF-RV-3 결과로 대체할 수 있다.
* **다른 출발점, 에이전트와의 경계:**
  * RQ-08(캡션 잔차, MC): EF-RV-0과 같은 "null을 빼고 남는 것" 논리이나 null과 자료가 다르다.
  * RQ-52(소리 stem 제거, Emo-FilM): EF-RV-1과 같은 in-silico 편집 틀. 합치면 "얼굴, 맥락, 소리" 3요인 설계가 된다.
  * RQ-33(MC 앞 클립 맥락): EF-RV-1, 3과 주제가 닿는다. MC는 무음이라 TRIBE v2 대신 관찰 분석이 맞다.
  * RQ-10(내 Stage 4 카드): 정서 기준 자극 선택. 이번 질문들과 겹치지 않는다.
  * D2(vision-decoding 주담당)의 "decoding 모델 + emotion head"와 달리, EF-RV-2의 emotion head는 성능 목표가 아니라 "정서 정보가 역학 다양체 위에 있는가"를 묻는 probe다.
  * brain-inspired(D1 주담당)는 구조 제약을 바꾼 모델을 만든다. 이쪽은 뇌 자료로 학습된 기존 모델을 도구로 쓴다.

## 5. Safeguards 점검

| 항목 | 이번 질문들의 처리 |
|---|---|
| 경험 정서 대 묘사 정서 | 얼굴 유무, 장면 기술은 묘사된 내용으로만 쓴다(EF-RV-1, 3). 정서 라벨로 부르지 않는다 |
| 사람 주석 대 모델 주석 | VLM 장면 기술, 자동 전사, 얼굴 검출은 모델 생성으로 표시(EF-RV-1, 3) |
| 본인 보고 대 규범 평정 | Emo-FilM 공유 성분은 규범 평정, 개인 성분은 본인 생리와만 연결(EF-RV-0, 2). Spacetop은 본인 평정만. 두 주체 결과를 합치지 않는다(EF-RV-3) |
| 정서 대 시각-의미 표상 | EF-RV-0이 이 구분 자체를 계산 문제로 만든다. 저수준 nuisance band 포함 |
| encoding 정확도 대 설명 적합성 | 모든 질문의 결론은 정확도가 아니라 대조 영역, 대조 사건, 맥락 교체 같은 대조 비교에서 나온다 |
| decodability 대 표상 대 인과 | EF-RV-2의 inferability는 인과가 아니다. EF-RV-1의 in-silico 편집 효과는 모델 안의 인과이며 뇌 인과는 관찰 검증 범위까지만 말한다 |
| in-silico 대 관찰 | 모든 in-silico 결과에 관찰 검증 단계와 "모델 실패 영역" 보고를 둔다 |
| 공유 표상 대 자료 특이 혼입 | Emo-FilM 주, Spacetop 반복. 두 자료의 라벨 주체가 다름을 명시 |
| 탐색 대 확증 | 방향 예측은 2주차 전에 사전 등록. 나머지는 탐색으로 표시 |
| HRF 지연, 자기상관 | TRIBE v2는 5 s 지연 보정, 우리 readout은 FIR. 순열은 circular shift, 영화 단위 |
| 자극, 영화, 피험자 누수 | leave-film-out, leave-story-out, leave-subject-out. 트윈은 영화 fold 분리 |
| 반복 자극 | Spacetop shortvideo 재제시(EF-RV-1)는 V1 정규화와 "예상된 실패" 사전 기재 |
| 라벨 잡음 | Emo-FilM 평정 일치도 평균 0.38. 항목별 IRA를 설명량 해석의 가중으로 보고 |
| 공선성 | EF-RV-1이 in-silico 편집으로 공선성을 끊는다. 관찰 단계는 banded ridge |
| 시공간 해상도 | Emo-FilM 6 mm smoothing, TR 1.3 s, Spacetop TR 0.46 s. 순간 단위 주장은 수 초 단위로 한정 |
| ROI 선택, 순환 추론 | 영역 목록과 대조 영역은 외부 atlas로 사전 지정. 결과로 영역을 고르지 않는다 |
| 다중비교 | 영역 단위 FDR, 순열 |
| checkpoint 라이선스 | TRIBE v2, CortexMAE 가중치 CC BY-NC(확인). Brain-JEPA LICENSE 없음, NeuroSTORM 불일치, 추출기와 LLM, VLM 라이선스 미확인 |
| 사전학습 오염 | Brain-DiT 제외(Emo-FilM, NSD 포함). TRIBE v2, CortexMAE 사전학습에 우리 뇌 자료 없음. 추출기, LLM, VLM의 공개 영화 노출은 지식 probe로 점검 |
| 자료 간 주석 비호환 | Emo-FilM 1 Hz 규범 50항목과 Spacetop 본인 영상 단위 7항목을 같은 척도로 합치지 않는다 |

## 6. 검색 기록 (모두 2026-11-12)

| 도구 | 질의 | 결과 |
|---|---|---|
| arXiv API | `all:"foundation model" AND all:fMRI AND all:emotion` | arXiv:2411.07121 하나(시각 경험 decoding, 정서 분석 아님) |
| arXiv API | `all:"reconstruction error" AND fMRI AND "foundation model"` | 0 |
| arXiv API | `"normative model" AND "brain dynamics" AND emotion` | 0 |
| arXiv API | `"in silico" AND encoding AND amygdala` | 0 |
| arXiv API | `"encoding model" AND "in silico" AND ablation AND fMRI` | 0 |
| arXiv API | `"brain foundation model" AND emotion` | EEG 연구만 |
| arXiv API | `abs:fMRI AND "masked autoencoder" AND anomaly` | 0 |
| arXiv API | `abs:fMRI AND "foundation model" AND naturalistic` | Brain-DiT(2604.12683), MIRAGE, TRIBE v2, 2605.19352 |
| arXiv API | `"encoding model" AND emotion AND "in silico"` | 0 |
| arXiv API | `amygdala AND "encoding model" AND video` | 0 |
| arXiv API | `all:"in silico" AND all:emotion AND all:fMRI` | 0 |
| arXiv API | `all:TRIBE AND all:emotion` | 2610.13558(관련 없음) 외 무관 1건 |
| arXiv API | `all:"foundation model" AND all:fMRI AND all:"self-report"` | 0 |
| arXiv API | `abs:fMRI AND abs:emotion AND abs:"context length"` | 0 |
| arXiv API | `abs:fMRI AND abs:emotion AND abs:perturbation AND abs:video` | 0 |
| arXiv API | `abs:fMRI AND abs:"foundation model" AND abs:affective` | 정서와 무관한 임상 4건 |
| arXiv API | `abs:fMRI AND abs:emotion AND abs:"encoding model" AND abs:naturalistic` | 0 |
| arXiv API | `abs:fMRI AND abs:emotion AND abs:"reconstruction error"` | 0 |
| arXiv API | `abs:fMRI AND abs:emotion AND abs:"brain dynamics" AND abs:pretrained` | 0 |
| arXiv API | `abs:"digital twin" AND abs:fMRI AND abs:emotion` | 0 |
| arXiv API | `abs:"in silico" AND abs:fMRI AND abs:"encoding model"` | 2609.15685, 2510.21142, 2605.04326, 2609.36391 |
| arXiv API | `abs:fMRI AND abs:"digital twin" AND abs:"individual differences"` | 0 |
| arXiv API | `abs:"encoding model" AND abs:"individual differences" AND abs:emotion` | 2606.11598(정서 아님) |
| arXiv API | `abs:fMRI AND abs:"masked" AND abs:insula` | 0 |
| arXiv API | `abs:fMRI AND abs:interoception AND abs:"deep learning"` | 0 |
| arXiv API | `abs:superstimuli AND abs:fMRI`, `au:Adeli AND au:Kriegeskorte` | Hwang 2025 superstimuli의 in vivo 검증 후속 없음 |
| arXiv API | `abs:"long-context" AND abs:fMRI AND abs:movie` | 2602.07570만 |
| PubMed | "amygdala faces movie fMRI naturalistic emotion" (2019~) | 2건(doi:10.1038/s41597-026-07065-x 자료 공개, doi:10.1016/j.neuropsychologia.2022.108194) |
| PubMed | "temporal receptive window emotion narrative fMRI" (2015~) | 1건(doi:10.1016/j.neuroimage.2020.117445 리뷰) |
| PubMed | "Emo-FilM" | 자료 논문 1건 |
| PubMed | "skin conductance movie fMRI insula" (2015~), "idiosyncratic emotion fMRI film self-report" (2018~), "Spacetop naturalistic video emotion ratings fMRI" | 0 |
| WebSearch | 위 각 질문의 "가장 가까운 선행" 항목에 적은 질의 4건 + "fMRI movie viewing individual emotional experience deviates from group consensus ..." | 식별자 있는 직접 선행 없음. Saarimäki 2025를 찾아 PubMed로 검증 |

* 차단 정책: nature.com, neurips.cc 직접 접근은 이번에도 시도하지 않았다. 학회 초록(CNS, CCN, NeuroLang)은 식별자가 없어 선행 판정에 넣지 않았다.

## 7. 미확인 사항과 사용자 확인 필요

1. 자료 경로와 계산 자원(GPU 종류, 시간): `reference/datasets_and_resources.md` 1절 미기재.
2. Spacetop shortvideo가 alignvideo와 같은 프레임인지, 소리가 있는지(EF-RV-1).
3. Spacetop narratives 텍스트 이야기의 제시 방식과 단어 시각(EF-RV-3).
4. Spacetop alignvideo 영상과 TRIBE v2 학습 영상(CNeuroMod)의 중복 여부.
5. TRIBE v2 추출기(V-JEPA2-Giant, Wav2Vec-BERT 2.0, Llama-3.2-3B), EF-RV-3의 언어 모델과 VLM, 전사 모델, 얼굴 inpainting 모델의 라이선스.
6. Brain-JEPA 라이선스(저장소에 없음), NeuroSTORM 라이선스 표기 불일치, Brain-DiT 가중치 링크.
7. TRIBE v2 설정값(duration_trs 100, frequency 2, max_context_len 1024)의 초 단위 의미, 잠재 hook 추출(코드만 확인, 실행 전).
8. CortexMAE volume reader가 FSL MNI152 정합 자료(Emo-FilM)를 그대로 받는지, 6 mm smoothing 자료의 복원 품질.
9. Emo-FilM physio의 StartTime 부호(BIDS 관례와 다름, Stage 1 지적).
10. MC 보유본 전처리 형식(EF-RV-2 선택 반복에만 해당).

## 8. literature.jsonl 추가 (13건, 총 63건)

* arXiv 검증: arXiv:2604.12683 (Brain-DiT), arXiv:2510.21142 (Hwang 2025), arXiv:2602.07570 (Jindal 2026), arXiv:2606.07707 (Zhang 2026).
* PubMed 검증: doi:10.1162/imag_a_00517 (Saarimäki 2025), doi:10.1523/JNEUROSCI.3684-10.2011 (Lerner 2011), doi:10.1523/JNEUROSCI.20-08-03033.2000 (Critchley 2000), doi:10.1515/revneuro.2003.14.4.303 (Sander 2003), doi:10.1038/nrn3950 (Barrett & Simmons 2015), doi:10.1038/s41597-025-04803-5 (Emo-FilM), doi:10.1038/s41597-025-05154-x (Spacetop), doi:10.1038/s41467-026-71151-2 (Miao 2026), doi:10.1016/j.neuropsychologia.2022.108194 (Kirk 2022).
* 본문 확인 수준: Brain-DiT(3.1절, Conclusion), Hwang 2025(Limitations), Jindal 2026(Conclusion, 부록 K)은 full_text. 나머지 10건은 abstract_only로 표시했고 future direction을 추론하지 않았다.
* Critchley 2000, Sander 2003, Lerner 2011은 2015년 이전이지만 이론 기준점으로 넣었다.
