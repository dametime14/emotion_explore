# Stage 4 독립 평가 노트 (adversarial-reviewer)

* 작성: adversarial-reviewer의 새 인스턴스. 기준일 2026-11-12.
* 대상: `outputs/rq_landscape.md`의 RQ-01~RQ-60. 이 인스턴스는 어느 질문도 만들지 않았다.
* 점수 파일: `outputs/evaluation/scores_reviewer.csv` (긴 형식, 540행, 열 `rq_id,criterion,score,reason`). python으로 행 수 540, 결측 0, 점수 범위 1~5, 기준 이름 9개 일치, 중복 쌍 0, em dash 0을 확인했다.
* 읽은 자료: CLAUDE.md 6절, `reference/protocols.md` P5, P6, `reference/existing_projects.md`, `reference/datasets_and_resources.md`, `outputs/rq_landscape.md`, `outputs/combinations/matrix.csv`(rq_id 60행), `outputs/discussion_record.md`, `outputs/discussion/round3_summary.md` 1절, `outputs/stage1/dataset_intelligence_report.md`, `dataset_Spacetop.md`, `dataset_EmoFilM.md`의 해당 절, `outputs/STAGE_STATUS.md`의 사용자 답변 절, `outputs/agents/adversarial-reviewer/round3_top10_review.md`, `round3_top10_addendum.md`, `outputs/literature/literature_db.csv`(근거 논문 일부), 이전 세션 scratchpad의 Mind captioning 본문 텍스트(`mindcap2025.txt`, Methods).
* **읽지 않은 것:** `outputs/evaluation/scores_coordinator.csv`, `outputs/evaluation/scores_reconciled.md`. 지시대로 열지 않았다(작업 시작 시 `outputs/evaluation/`은 비어 있었다).
* 표기: [본문] 원문 확인, [추론], [검색] 이번 검색. 사용자 확인 데이터 사실(2026-11-12)을 Stage 1 보고서보다 우선했다.

---

## 0. 채점 기준(앵커)

같은 점수가 질문마다 같은 뜻이 되도록 아래 앵커를 썼다.

| 기준 | 5 | 3 | 1 |
|---|---|---|---|
| Novelty | 직접 확인한 검색에서 가까운 선행이 없고 질문 자체가 새롭다 | 부분 선행이 있고 새 데이터나 방법 요소가 있다. Novelty Constraint 유형은 2 이하 | 이미 수행됨 |
| Neuroscientific Importance | 정서 표상의 중심 논쟁(범주 대 차원, 정서 대 의미)에 답한다 | 정보가 있으나 주변적이거나 결론이 R1 | 없음 |
| AI / Modeling Contribution | 모델이 연구 대상이거나 가설 그 자체다 | feature 추출기 이상의 설계가 있다 | AI 모델 없음 |
| Dataset Feasibility | Horikawa 2020 + Mind captioning으로 기존 라벨, 자극만으로 가능 | 라벨이 대리, 희소하거나 R1 자극이 필요 | 보유 데이터로 검정 불가 |
| Methodological Rigor | 교란, 누수, 신뢰도가 모두 통제됨 | 주요 교란을 인지했으나 일부 미해결 | 치명적 결함 |
| Falsifiability | 사전 등록된 중단, 판정 규칙 | 예측은 있으나 일부 결과가 모호 | 반증 불가 |
| Interpretability | 결과가 과학적 결론에 바로 대응 | 강한 가정이 필요 | 해석 불가 |
| Generalizability | 여러 데이터셋, 개인, 자극으로 확장이 설계됨 | 한 데이터셋 안에서 확장 경로가 있음 | 확장 불가 |
| Feasibility | 가벼운 통계, 단일 GPU | 공개 모델 여러 개, 생성 또는 미세조정 | 불가능 |

* **Horikawa 우선(P6):** Horikawa 2020 + Mind captioning으로 바로 가능한 질문만 Dataset Feasibility 5를 받았다. Emo-FilM, Spacetop만 쓰는 질문은 최대 4다.
* **Feasibility 가정:** 공개 pretrained model과 연구실 GPU 1~4장. 직접 학습(RQ-55), 시간 일관 비디오 편집(RQ-09, RQ-12), 고차원 empowerment 추정(RQ-40)은 이 가정을 넘거나 구현 위험이 커서 2점을 주었다. 자원은 미확인이다.
* **관문 연구(RQ-01 0단계, 08 0단계, 13, 17, 21 0단계, 24 0단계, 39, 49, 51):** 그 자체의 과학적 가치로 채점했다. 다른 질문의 전제라는 점은 근거에만 적었다. 그래서 RQ-17, RQ-51은 관문 가치가 커도 Neuroscientific Importance가 2다.
* 합계는 9개 기준의 단순 합이다. Dataset Feasibility와 Feasibility가 둘 다 실행 가능성을 재서 저비용 질문이 유리하다. 이를 보완하려고 1.2절에 과학 기준만 합한 보조 순위를 같이 둔다.

---

## 1. (a) 9개 기준 합계 상위 15개

### 1.1 합계 순위

15위에 31점 동점이 둘(RQ-26, RQ-32)이라 16개를 적었다. 33점 동점 7개는 RQ 번호 순이다.

| 순위 | RQ | 합계 | 점수(N, NI, AI, DF, MR, F, I, G, FE) | Horikawa 계열로 바로 가능 | 한 줄 이유 |
|---|---|---|---|---|---|
| 1 | RQ-08 | 37 | 3 5 3 5 4 4 4 4 5 | 예 | 정서 배제 캡션 20개로 Horikawa 결론의 가장 약한 고리(의미 공변량 측정 오차)를 직접 시험하고, 결론 범위가 '언어 기술로 회복되지 않는 규범 정서 공변'으로 잘 한정되었다 |
| 2 | RQ-60 | 34 | 4 4 4 5 3 4 3 3 4 | 예 | 무음이라는 Horikawa의 제약을 질문으로 바꿨고 V2A 생성 모델이 가설 장치다. 단 V2A 시각 조건 embedding 대조가 필수다 |
| 3 | RQ-01 | 33 | 3 5 2 5 4 4 3 3 4 | 예 | 중심 논쟁을 같은 자극의 독립 두 코호트로 다룬다. 경쟁 가설을 Westlin 원 결과(개인 특이, 세션 정렬 군집)에 맞게 고쳐야 한다 |
| 3 | RQ-03 | 33 | 4 4 2 5 3 4 3 3 5 | 예 | 정서 기하가 자극 집합의 산물인지 같은 클립 풀의 부분집합 조작으로 시험한다. fMRI에서 이 조작의 선행을 찾지 못했다 |
| 3 | RQ-13 | 33 | 4 3 3 5 3 4 3 3 5 | 예 | 어떤 정서 쌍 대비가 내용과 분리 가능한지 정하는 지도다. 관문이라 Neuroscientific Importance는 3으로 두었다 |
| 3 | RQ-14 | 33 | 4 4 4 4 3 4 3 3 4 | 아니오(Emo-FilM 주) | situation recognition의 의미역 구조로 appraisal의 행위 주체 변수를 계산 가능하게 만든다. 공개 VidSRL 모델 정확도가 위험이다 |
| 3 | RQ-15 | 33 | 3 3 4 5 3 4 3 4 4 | 예 | AI 라벨을 쓸 때 내부 표상과 출력 중 무엇을 써야 하는지 정한다. C&K 공개 지도 오염이 출력 쪽을 유리하게 할 수 있다 |
| 3 | RQ-33 | 33 | 3 4 3 5 3 4 3 3 5 | 예 | Mind captioning의 실제 순서 변이로 맥락 동화와 대비를 가른다. HRF 잔여는 동화를 흉내 내므로 대비 결과만 강한 증거다 |
| 3 | RQ-58 | 33 | 3 4 3 4 3 4 4 3 5 | 아니오(Spacetop) | narratives의 원문 텍스트와 본인 feeling, expectation 평정으로 단기 대 장기 예측오차를 이중 해리로 검정한다 |
| 10 | RQ-10 | 32 | 3 3 3 5 3 4 3 3 5 | 예 | 코호트 간 전향 선택. Mind captioning 반응이 이미 전처리되어 있어 사전 등록과 분석자 차단이 성패를 정한다 |
| 10 | RQ-24 | 32 | 4 4 3 3 3 5 3 2 5 | 아니오(Emo-FilM) | 평정만 쓰는 0단계 중단 규칙이 명시적이다. consensus 상태열은 경험된 전이가 아니라는 한계가 남는다 |
| 10 | RQ-25 | 32 | 3 4 4 4 3 4 3 3 4 | 아니오(Emo-FilM) | world model 예측오차 대 불확실성을 appraisal 두 유형에 대응시킨다. 평정자 반복 시청이 Predictable, Suddenly를 오염시켰을 수 있다 |
| 10 | RQ-39 | 32 | 3 3 2 4 4 5 4 2 5 | 아니오(Emo-FilM) | Axis V 전체의 측정 타당성 관문. 판정 규칙이 가장 명확하다 |
| 10 | RQ-56 | 32 | 3 3 5 4 3 4 3 4 3 | 예(학습) | 뇌 정서 영역 신호로 모델을 바꾸는 역방향 설계. 무작위 영역 대조가 추가로 필요하다 |
| 15 | RQ-26 | 31 | 3 4 2 5 2 4 3 3 5 | 예 | 데이터 조건은 좋지만 'HRF 잔여는 모든 부분공간에 같은 커널' 전제가 깨져 영역별 HRF 추정을 넣어야 한다 |
| 15 | RQ-32 | 31 | 4 4 1 4 3 4 3 3 5 | 아니오(Emo-FilM) | arousal을 상태 변화 속도로 재정의하는 새 질문이고 참가자 본인 EDA가 있다. 분산 정규화가 필요하다 |

* **독립 연구 단위로 보면 수가 줄어든다.** RQ-01, 03, 08, 13은 Horikawa 2020 + Mind captioning 재전처리와 캡션을 공유하고, RQ-26과 RQ-33은 Mind captioning 테스트 순서를 공유한다. 상위 16개는 실제로 약 12개 연구 단위다.
* **Horikawa 우선 관점:** 상위 16개 중 9개(RQ-08, 60, 01, 03, 13, 15, 33, 10, 26)가 Horikawa 2020 + Mind captioning만으로 시작할 수 있다. RQ-56은 학습만 Horikawa 계열이다.

### 1.2 보조 순위(과학 기준 5개만 합산: Novelty, NI, MR, F, I)

RQ-08(20), RQ-01(19), RQ-24(19), RQ-39(19), 이어서 18점의 RQ-03, 14, 21, 32, 43, 58, 60.
* 합계 순위와 다른 점: RQ-21(Spacetop 본인 보고)과 RQ-43(vividness 내성 대 기억성)이 올라오고 RQ-13, RQ-15, RQ-10, RQ-56이 내려간다. 두 순위 모두에 있는 RQ-08, 01, 03, 14, 24, 58, 60, 32는 어느 가중을 써도 상위권이다.

---

## 2. (b) Shortlist에 넣으면 안 된다고 보는 질문 (치명적 결함)

"현재 문안 그대로"라는 조건이다. 고칠 수 있는 경우 고치는 방법을 적었다.

| RQ | 치명적 결함 | 살리는 방법 |
|---|---|---|
| RQ-36 | 고차원 voxel 공간에서는 서로 다른 활성 패턴이 우연히도 거의 직교하므로 '행동 준비가 실행 부분공간과 직교'는 기본값이다. 실행 부분공간도 trackball 손 움직임 하나라 다가가기, 피하기 같은 정서 행동과 대응하지 않는다 | 우연 직교성 null(무작위 패턴, 다른 과제 패턴 대비 각도 분포)을 먼저 두고, 실행 과제가 여러 운동을 포함하는 데이터가 생기기 전까지 보류 |
| RQ-23 | 같은 사람의 연속 경험과 회고 평정을 잇는 자료가 없다. Emo-FilM 연속 평정은 별도 평정자, 참가자 회고는 영화별 몰입, 즐거움, 흥미이고, Spacetop은 연속 평정이 없다. 영화 14편이라 사람당 14점이다 | 새 데이터 수집 없이는 불가 |
| RQ-38 | V-JEPA 2-AC는 로봇 팔 end-effector 행동을 입력으로 받는다. 영화에는 넣을 행동이 없어 '행동 조건 대 행동 없음' 비교가 정의되지 않는다. 두 predictor의 학습 데이터도 다르다 | 질문을 'LAPA 추정 행동을 조건으로 넣은 예측기'로 다시 정의하고 데이터 차이를 통제할 수 있는지 먼저 확인 |
| RQ-20 | 데이터셋마다 라벨 출처가 하나라 출처 효과가 자극, 장비, 참가자 효과와 완전히 교락된다(관측 단위 3개) | 데이터셋 안에서 출처를 바꾸는 비교로 축소(Emo-FilM consensus 대 참가자 사후 평정, Spacetop 본인 대 peer 평균) |
| RQ-45 | 기계 재현 지수가 높은 클립은 cue 캡션 자체에 정서가 많은 클립이고, 참가자는 회상 직전에 그 cue를 읽는다. 언어 병목 기제 없이도 예측한 상관이 나온다 | cue 텍스트만으로 계산한 정서 지수를 공변량으로 넣고 남는 관계만 해석 |
| RQ-42 | Mind captioning 회상은 실험자가 cue로 지정한 지시 심상이다. 뇌가 무엇을 재생할지 고르는 우선순위 재생이 아니다. 수동 시청 클립에는 가치 변화와 need가 정의되지 않는다 | 보유 데이터로는 불가. 휴지기 자발 재생 자료가 필요 |
| RQ-31 | 시간 자기상관이 높으면 곡률이 기계적으로 낮아진다. 고유 시간척도가 긴 정서, transmodal 영역은 정서와 무관하게 '더 곧게' 보일 것으로 예측된다 | 영역별 AR 구조와 tSNR을 맞춘 대리 자료 null을 주 검정으로 둔 뒤에만 진행 |
| RQ-16 | Spacetop 과제 사이에 공유되는 정서 축이 몇 개뿐이다(alignvideo 7차원 본인 평정, shortvideo mentalizing 7문항 중 정서는 일부, faces 표정 강도 평정은 1 run 96 trial). shortvideo는 alignvideo 장면 재노출이라 기억 효과가 섞인다 | alignvideo와 faces 설계 라벨이 공유하는 happy, sad, fear, disgust로 축소 |
| RQ-18 | 같은 시점에 여러 출처 view가 있는 곳이 Emo-FilM뿐인데 본인 view는 영화 길이의 약 20%, 영화당 5항목이다. Horikawa, Spacetop에는 같은 자극의 다른 출처 view가 없다 | Emo-FilM 사후 평정 구간으로 한정한 소규모 판본으로만 가능 |
| RQ-40 | 관객에게는 행동 채널이 없어 empowerment의 주체가 정의되지 않는다. LAPA latent action이 카메라 운동을 잡아 empowerment가 카메라 운동 다양성으로 환원될 수 있다 | 인물 관점 empowerment를 정의하고 카메라 운동을 통제한 뒤 재제안 |
| RQ-37 | groove는 박절이 분명한 음악의 성질인데 단편영화 음악의 groove 분산이 거의 없을 수 있다(미확인). Horikawa 무음 대조는 정보가 없다 | 먼저 Emo-FilM 사운드트랙의 groove feature 분산을 계산해 충분할 때만 진행 |
| RQ-46 | 인간 전달 사슬은 새 행동 데이터가 필요하고 RQ-45와 같은 cue 교란을 공유한다 | RQ-45의 cue 통제가 해결된 뒤 LLM 사슬 판본만 탐색적으로 |

* **조건부(치명적이지는 않으나 수정 전에는 Shortlist 보류):** RQ-07(드문 범주의 차원 부족이 빈도-신뢰도 교란으로도 생긴다. 클립 수를 맞춘 재표집 null 필요), RQ-26(영역별 HRF 추정 없이는 관성 결론 불가), RQ-55(목표만 바꾼 공개 checkpoint 조합이 사실상 없다).

---

## 3. (c) 데이터에 실제로 라벨이나 자극이 없어서 성립하지 않는(또는 일부만 성립하는) 질문

| RQ | 없는 것 | 근거 | 영향 |
|---|---|---|---|
| RQ-23 | 같은 사람의 연속 정서 평정 | Emo-FilM 연속 평정은 별도 평정자 consensus, 참가자 사후 평정은 클립 약 20% + 영화별 몰입, 즐거움, 흥미(dataset_EmoFilM.md). Spacetop은 영상 종료 후 1회 평정 | 성립 안 함 |
| RQ-16 | 과제 간 대응 정서 라벨 | dataset_Spacetop.md task-faces, task-shortvideo 절 | 일부만 성립 |
| RQ-18 | 같은 자극의 다중 출처 view | Emo-FilM 사후 평정 범위, Horikawa 평정자 원자료 비공개, Spacetop 규범 평정 없음 | 일부만 성립 |
| RQ-38 | 영화의 행동 입력 | V-JEPA 2-AC 입력 정의 | 성립 안 함 |
| RQ-42 | gain 대리 변수(가치 변화, need), 자발 재생 | Mind captioning 회상은 cue 지정 지시 심상 [본문, Methods] | 성립 안 함 |
| RQ-46 | 인간 전달 사슬 자료 | matrix note | 새 수집 필요 |
| RQ-04 | 성분 상위 클립의 사람 명명 | matrix dataset 열 | 새 수집 필요(MLLM 명명만 즉시 가능) |
| RQ-30 | Spacetop의 정서적 놀람 평정 | Spacetop 평정은 영상 단위 7차원 | Spacetop 쪽은 뇌 궤적만 |
| RQ-32, RQ-50 | Emo-FilM의 arousal, valence 문항 | 50항목에 없음. IntenseEmotion, Calm, Alert, Good/Bad, AtEase 대리(Ma & Kragel도 대리 사용) | 대리 지표로만 성립 |
| RQ-52 | C&K 클립의 소리 | 사용자 확인: 보유 2,185개 모두 무음 | 원 설계 불가, Emo-FilM 판본만 |
| RQ-48 | Mind captioning 생리 | Mind captioning Methods에 생리 기록 언급 없음 | '반복 ceiling 보정'은 다른 데이터셋 값이라 적용 무리 |
| RQ-55 | 목표만 다른 공개 checkpoint | V-JEPA 2, VideoMAE, CLIP 계열의 학습 데이터와 구조가 다름 | 직접 학습 시에만 성립 |
| RQ-53 | 충분한 저정서 클립 | C&K는 정서 유발 클립 모음 | '저정서'가 상대적 정의로만 성립 |
| RQ-35 | 같은 valence 안의 충분한 동기 방향 대비 구간 | 미확인 | 0단계로 확인 필요 |
| RQ-37 | groove를 가진 영화 음악 | 미확인 | 0단계로 확인 필요 |
| RQ-03, RQ-13 (NSD 팔) | NSD 정서 라벨 | NSD는 nsdmeadows 100장만 | NSD 대조는 AI 추정 정서로만 |
| RQ-21 | 완전한 본인 평정 | alignvideo 평정 약 51% 결측, 유효 40~57명 | 성립하나 검정력 제약 |

---

## 4. (d) 채점 중 바뀐 판단과 불확실한 점수

### 4.1 바뀐 판단

1. **RQ-01, RQ-07의 경쟁 가설 서술.** literature_db의 Westlin 2025(arXiv:2507.00320) 요약을 확인하니 결과는 '저차원 연속 구조'가 아니라 피험자별 11~14군집, 범주 NMI 0.014, 세션 NMI 0.19였다. rq_landscape와 matrix는 RQ-01에서 "Westlin 2025가 보고한 저차원 연속 구조", RQ-07에서 "Westlin(적은 차원)"이라고 적었다. RQ-01 Interpretability를 3으로, RQ-07 Interpretability를 2로 낮췄다. 이전 addendum이 H-idio(개인 군집 재현)를 LIT-01에 넣으라고 했지만 질문 문장은 아직 고쳐지지 않았다.
2. **RQ-26.** Mind captioning 본문 Methods를 읽고 block 사이 휴지가 2 s뿐임을 확인했다[본문]. matrix의 "HRF 잔여는 모든 부분공간에 같은 커널" 전제는 영역별 HRF 차이 때문에 성립하지 않는다고 판단해 Methodological Rigor를 2로 두었다. 이전 검토(top10)는 이 전제를 짚지 않았다.
3. **RQ-33.** 처음에는 RQ-26과 같은 HRF 문제로 2점을 주려 했다. 그러나 HRF 잔여가 만드는 가짜 효과는 동화 방향뿐이라 대비 결과는 진단력이 있다고 보고 3점으로 올렸다.
4. **RQ-47.** 처음에는 cue 텍스트가 회상 중에 떠 있다고 생각했다. 본문 확인 결과 cue는 별도 준비 block에 나오고, 신호음 뒤 눈을 감고 심상한다[본문]. 문제를 'HRF 지연에 의한 읽기 반응 혼입과 눈 감음 기저 변화'로 고쳤고 점수(2)는 유지했다.
5. **RQ-13.** 처음에 Methodological Rigor 4, Interpretability 4였다. 매칭 embedding이 내용을 다 담는다는 가정이 RQ-08의 공변량 완전성 문제와 같다고 보고 둘 다 3으로 낮췄다.
6. **RQ-19.** 처음 Novelty 3이었다. Du 2025가 같은 2,180개 비디오에서 MLLM 기하와 뇌의 정렬을 이미 보였으므로 Novelty Constraint(기존 라벨의 FM 예측)에 맞춰 2로 낮췄다.
7. **RQ-60.** 처음 Novelty 5를 고려했다. 이 항목은 재검색하지 않았고 matrix 판정이 partially(Meyer 2010)라 4로 두었다.

### 4.2 불확실한 점수

* **다른 에이전트 검색에 기댄 Novelty 4:** RQ-13(geometry-info Round 4), RQ-24(이전 검토 검색). 재확인하지 않았다.
* **RQ-58 Novelty 3:** 언어 청취 fMRI의 다중 시간척도 예측 연구가 더 가까운 선행일 수 있다. 이번 검토에서는 식별자로 확인하지 않아 근거에 쓰지 않았다. 확인되면 2가 될 수 있다.
* **RQ-33 Novelty 3:** 정서 지각의 serial dependence 행동 연구를 검색하지 않았다.
* **RQ-14 Feasibility와 Rigor:** 공개 VidSRL checkpoint의 존재와 성능을 확인하지 않았다. MLLM으로 의미역을 뽑으면 가능하지만 AI 생성 feature다.
* **라이선스 미확인:** TRIBE v2, MMAudio, V-JEPA 2 checkpoint. 연구 사용이 막히면 RQ-09, 25, 48, 51, 52, 56, 59, 60의 Feasibility가 내려간다.
* **RQ-49 Dataset Feasibility 2:** 관문 결과에 따라 1이 될 수도 있다.
* **RQ-32 Dataset Feasibility 4:** IntenseEmotion, Calm, Alert가 arousal 대리로 타당한지 확인하지 않았다.
* **계산 자원 미확인:** 모든 Feasibility는 GPU 1~4장 가정이다.

### 4.3 이전 검토, matrix와의 이견 (합의로 지우지 않음)

| 쟁점 | 이전 입장 | 이번 판단 |
|---|---|---|
| RQ-26 HRF 전제 | matrix(multimodal-dynamics, geometry-info 설계): HRF 잔여는 모든 부분공간에 같은 커널이라 정서 부분공간의 더 느린 감쇠만 관성 증거 | 영역마다 HRF가 달라 전제가 깨진다. 영역별 HRF 추정(예: Horikawa 블록 자료나 별도 국소 HRF 적합)을 주 분석 앞에 두어야 한다 |
| RQ-01 경쟁 가설 | rq_landscape: Westlin = 저차원 연속 구조 | Westlin = 개인 특이, 세션 정렬 군집. 질문 문장 수정 필요 |
| RQ-10의 '전향' | matrix: 관찰 데이터 안에서 가능한 가장 강한 예측 검증 | Mind captioning이 이미 전처리되어 있어 분석자 노출이 이미 있었을 수 있다. 사전 등록 시점 기록 없이는 R0 상관 분석과 다르지 않다 |
| RQ-60 우선순위 | rq_landscape에서 무작위 경로 질문으로 주목받지 않음 | 합계 2위. Horikawa 계열에서 바로 가능하고 V2A 시각 embedding 대조라는 명확한 null을 세울 수 있다 |
| 관문 질문의 점수 | rq_landscape 3.1: 관문 먼저 원칙 | 순서 원칙에는 동의한다. 그러나 관문 자체의 Neuroscientific Importance는 낮게(RQ-17, RQ-51은 2) 매겼다. 실행 순서와 과학적 가치를 분리해야 한다 |

### 4.4 이번에 새로 확인한 데이터 사실 (Mind captioning 본문 Methods, [본문])

* 영상 block은 10 s 미만 클립을 반복해 10 s 이상으로 만들고, 각 block 뒤 휴지는 2 s다.
* 영상 run마다 평가 block 3~4개가 무작위로 끼어 있고, 직전 영상의 20개 캡션 중 5개(가끔 다른 영상 것)를 보여 주며 일치도를 평정하게 했다. 즉 일부 클립 직후에 정서 배제 캡션이 참가자에게 제시되었다. RQ-08의 해당 클립 응답 창 끝부분에 읽기 반응이 섞일 수 있다(영향은 작다고 추정, 미검증).
* 학습 세션 2,180개 클립의 의사 무작위 순서는 Mind captioning 6명 모두 같다. 코호트 내 쌍은 순서를 공유하고 코호트 간 쌍만 순서가 독립이다.
* 테스트 72개 클립은 두 run에 나눠 5회씩, run 안 의사 무작위 순서로 제시되었다.
* 회상 실험은 30 run x 12 trial이라 클립당 5회 회상이다. 각 trial은 준비 block(cue 캡션 제시, 20개 중 하나로 고정) → 눈 감고 심상 → 원 영상 재시청 → 정확도와 vividness 평정(5점) 순서다. vividness는 원 영상을 다시 본 뒤의 비교 평정이다.
* 같은 논문은 cue 읽기 구간만으로는 대부분의 피험자(S2 제외)에서 해독 정확도가 우연에 가까웠다고 보고했다. 그래서 cue 읽기 혼입은 의미 해독 결과를 설명하지 못하지만, 회상 구간 초반의 혼입 가능성은 남는다.

---

## 5. 부록: 질문별 핵심 전제 반증 시도 (지시 6)

판정: 유지 = 반증 시도가 실패함, 약화 = 전제가 부분적으로 흔들려 통제가 필요함, 깨짐 = 현재 문안의 전제가 성립하지 않음, 미확인 = 데이터나 문헌 확인이 더 필요함.

| RQ | 핵심 전제 한 줄 | 반증 시도 | 판정 |
|---|---|---|---|
| 01 | Westlin 2025는 저차원 연속 구조를 보고했다 | literature_db 요약: 피험자별 11~14군집, 범주 NMI 0.014 | 약화(서술 수정) |
| 02 | C&K 범주 체계는 IB 효율 예측이 적용되는 명명 체계다 | 연구자가 고른 선택지 | 약화 |
| 03 | 시각 다양성과 정서 다양성을 따로 조작할 수 있다 | C&K에서 둘이 상관 | 약화 |
| 04 | 성분 상위 클립의 이름은 기존 범주와 독립적으로 나온다 | 클립이 범주 대표로 수집됨, MLLM 오염 | 약화 |
| 05 | narratives의 양식은 이야기와 독립이다 | 균형화 미확인 | 미확인 |
| 06 | 시너지 추정이 PID 추정량에 강건하다 | 추정량 간 차이 큼 | 약화 |
| 07 | 드문 범주의 전용 차원 부족은 superposition 때문이다 | 빈도-신뢰도 교란 | 약화 |
| 08 | 정서 배제 캡션은 정서 정보를 담지 않는다 | 사건 기술이 정서를 함축 | 유지(해석 한정이 이미 반영) |
| 09 | 통계 통제와 설계 통제의 실패 방식은 독립이다 | 같은 데이터, 겹치는 feature | 약화 |
| 10 | Mind captioning 검증은 전향적이다 | 데이터 존재, 전처리 완료 | 약화 |
| 11 | Horikawa amygdala encoder는 합성에 쓸 만큼 정확하다 | 3T 블록 평균, 낮은 신뢰도 | 미확인 |
| 12 | 편집은 상황 또는 정서만 바꾼다 | 저수준 통계 변화(Zhan 2026) | 약화 |
| 13 | 매칭 embedding이 내용을 충분히 담는다 | 공변량 완전성 문제 | 약화 |
| 14 | 공개 VidSRL 모델이 영화 장면 의미역을 쓸 만하게 뽑는다 | 모델 정확도 낮음 | 미확인 |
| 15 | VLM 출력은 C&K 평정을 기억하지 않는다 | 공개 지도 오염 가능 | 미확인 |
| 16 | 세 과제에 공유 정서 축이 있다 | 라벨 불일치 | 깨짐 |
| 17 | Emo-FilM 평정자 수가 alt-test에 충분하다 | 항목x영화당 3~4명 | 유지(경계) |
| 18 | 같은 시점에 여러 출처 view가 있다 | 본인 view 약 20% | 깨짐 |
| 19 | MLLM 평정은 C&K 라벨과 독립이다 | 오염 가능 | 약화 |
| 20 | 라벨 출처 효과를 자극 효과와 분리할 수 있다 | 데이터셋당 출처 1개 | 깨짐 |
| 21 | 평정 결측은 값과 무관하다 | 이전 검토 계산: 값 의존 증거 없음 | 유지(상태 관련성은 미확인) |
| 22 | 불일치의 시간 고정 성분을 분리할 수 있다 | 반복 평정 없음, 3~4명 | 약화 |
| 23 | 같은 사람의 연속 경험과 회고 평정이 있다 | 없음 | 깨짐 |
| 24 | consensus 상태열은 경험된 전이다 | 항목마다 다른 평정자 | 약화(0단계가 판정) |
| 25 | Suddenly, Predictable 평정은 첫 시청의 예측을 반영한다 | 평정자 최대 6회 시청 | 약화 |
| 26 | HRF 잔여는 모든 부분공간에 같은 커널이다 | 영역별 HRF 차이, 휴지 2 s | 깨짐 |
| 27 | MLLM 프레임 대 클립 차이는 시간 의존성이다 | MLLM 능력 차이 반영 | 약화 |
| 28 | 영화 간 동역학 유사도는 정서 때문이다 | 편집 리듬, 서사 구조 | 약화 |
| 29 | 신경 정서 상태열을 정의할 수 있다 | decoder 오차 의존 | 약화 |
| 30 | fMRI 곡률은 표상 곡률을 반영한다 | HRF 평활, 잡음 | 약화 |
| 31 | 영역 간 곡률 차이는 정서 처리를 반영한다 | 자기상관이 곡률을 낮춤 | 깨짐 |
| 32 | 패턴 변화 속도는 신호 분산과 독립이다 | arousal이 전역 분산을 키움 | 약화 |
| 33 | 직전 클립 효과는 신경 해석의 이동이다 | HRF 잔여가 동화를 흉내 | 약화(대비는 유지) |
| 34 | LAPA latent action은 장면 affordance다 | 카메라 운동 포착 | 약화 |
| 35 | 같은 valence 안에서 동기 방향이 충분히 변한다 | 확인 안 됨 | 미확인 |
| 36 | 직교성은 정보가 있는 결과다 | 고차원 우연 직교 | 깨짐 |
| 37 | 영화 음악에 groove 분산이 있다 | 비박절 배경음 가능성 | 약화(깨질 가능성 높음) |
| 38 | 영화에 행동 입력을 줄 수 있다 | 로봇 행동 공간 | 깨짐 |
| 39 | 뇌 반응이 MTMM 방법 열로 기능한다 | 성격이 다른 방법 | 유지(주의) |
| 40 | 관객 관점 empowerment를 정의할 수 있다 | 주체 미정, 카메라 운동 | 깨짐 |
| 41 | vividness 분산이 충분하다 | 3~4점 편중 | 약화 |
| 42 | 지시 회상은 우선순위 재생이다 | 실험자가 지정 | 깨짐 |
| 43 | item 안 vividness 변동은 내성 신호다 | 회상마다 원 영상 재시청 학습 | 약화 |
| 44 | 세 예측(원 클립, 캡션, cue 생성 영상)은 분리될 만큼 다르다 | cue = 캡션, 공선 | 약화 |
| 45 | 기계 재현 지수는 cue 정서와 독립이다 | 아님 | 깨짐 |
| 46 | LLM 사슬은 인간 집단 편향의 대리다 | 미확인, cue 교란 | 약화 |
| 47 | 회상 구간은 텍스트 입력 없이 기억만 담는다 | HRF 지연 혼입, 눈 감음 | 약화 |
| 48 | Mind captioning ceiling을 Emo-FilM limbic에 쓸 수 있다 | 다른 데이터셋 | 약화 |
| 49 | 3T 2~2.7 mm에서 상구, pulvinar 신호를 분석할 수 있다 | Kragel 2021 차이 작음 | 미확인(관문이 판정) |
| 50 | Emo-FilM에 arousal, valence 평정이 있다 | 대리 지표뿐 | 약화 |
| 51 | 무음 클립의 TRIBE 예측은 공정한 비교다 | 시청각 학습 모델의 분포 이탈 | 약화 |
| 52 | stem 제거 입력은 TRIBE 학습 분포 안에 있다 | 분리 잡음 | 약화 |
| 53 | C&K에 충분한 저정서 클립이 있다 | 정서 유발 모음 | 약화 |
| 54 | 정서 unit은 창발한다 | 지도 학습의 직접 산물 | 약화 |
| 55 | 목표만 다른 공개 checkpoint가 있다 | 없음 | 깨짐 |
| 56 | brain-tuning 이득은 정서 영역 신호 때문이다 | 일반 정규화 가능 | 미확인 |
| 57 | 어휘 feature와 추론 feature를 분리할 수 있다 | 강한 공선성 | 약화 |
| 58 | 오디오 이야기의 단어 시점을 정렬할 수 있다 | clip onset만 제공 | 유지(forced alignment로 해결 가능) |
| 59 | TRIBE 양식 귀속은 실제 양식 상충이다 | 모델 오차 | 약화 |
| 60 | 생성 소리 feature는 시각 feature 이상의 정보를 준다 | V2A는 영상의 결정적 함수 | 약화(V2A 시각 embedding 대조로 판정 가능) |

* 집계: 유지 5, 약화 36, 깨짐 12, 미확인 7. 이전 라운드의 반박 0건과 달리, 반증 시도를 한 줄씩 하면 60개 중 12개 질문의 현재 문안 전제가 깨진다.

---

## 6. 검색 기록 (총 15회, 모두 2026-11-12)

| # | 경로와 질의 | 결과 | 반영 |
|---|---|---|---|
| 1 | PubMed: arousal AND (state transition OR speed OR velocity OR rate of change) AND (brain state OR neural trajectory OR pattern change) AND fMRI AND (movie OR film OR naturalistic), 2015~ | 0건 | RQ-32 |
| 2 | WebSearch: representational straightening human fMRI natural movies temporal trajectory curvature visual cortex 2024 2025 | 인간 fMRI 영상 straightening 없음(마카크 V1, 모델 연구) | RQ-30, 31 |
| 3 | PubMed: (partial information decomposition OR synergy) AND (emotion OR affective) AND (amygdala OR fMRI) AND redundan*, 2015~ | 3건, 모두 무관(심부전 휴지기, 생애 휴지기, 학회 초록집) | RQ-06 |
| 4 | WebSearch: information bottleneck emotion categories efficient communication emotion lexicon naming | 정서 명명 IB 없음(색 명명, arXiv:2602.08238 볼록성) | RQ-02 |
| 5 | WebSearch: superposition sparse dictionary fMRI emotion categories more categories than dimensions | 언어망 sparse concept atom(NeurIPS 2025), 정서 적용 없음 | RQ-07 |
| 6 | WebSearch: arousal speed of brain state change fMRI naturalistic movie pattern dissimilarity consecutive TRs | 직접 선행 없음, van der Meer 2020 인접 | RQ-32 |
| 7 | PubMed: Koide-Majima[Author] AND emotion AND cortical | PMID 32798681(Koide-Majima 2020, 영화 정서 차원과 피질 표상) | RQ-01, 04 |
| 8 | WebSearch: empowerment intrinsic motivation fMRI brain controllability scene naturalistic video encoding model | 없음 | RQ-40 |
| 9 | WebSearch: prioritized replay emotional memory reactivation recall fMRI surprise prediction error gain | 정서 회상 적용 없음, Momennejad 2018(eLife 32548) 등 | RQ-42 |
| 10 | WebSearch: video recall fMRI reactivation compared to text-to-video generated from cue schema reconstruction 2025 2026 | 없음 | RQ-44 |
| 11 | WebSearch: situation recognition semantic role labeling video features fMRI encoding agent patient movie | VidSitu + fMRI 없음, bioRxiv 10.1101/288605 인접 | RQ-14 |
| 12 | WebSearch: straightening human fMRI BOLD trajectory curvature natural video | 인간 영상 fMRI 없음, 언어 fMRI 학회 초록(AR(1) 높을수록 곡률 낮음, 식별자 없어 근거로 세지 않고 추론 보조로만 언급) | RQ-31 |
| 13 | WebSearch: vision language model hidden state emotion probe versus generated emotion ratings fMRI | 내부 표상 대 출력 비교 없음, Du 2025, GPT-4 평정 연구 | RQ-15 |
| 14 | WebSearch: audiovisual incongruence film moments emotion rater disagreement fMRI | arXiv:2410.17300(저일치 영화 순간), 통제된 얼굴-음성 연구 | RQ-22, 59 |
| 15 | WebSearch: fMRI eigenspectrum power-law exponent depends on stimulus set diversity subsampling | 부분집합 조작 없음, Stringer 2019 이론, 데이터셋 간 지수 차이 | RQ-03 |

* 근거에 새로 쓴 식별자: PMID 32798681(PubMed 검색 결과로 확인), arXiv:2410.17300(arxiv.org abs URL), doi:10.7554/eLife.32548(eLife 기사 번호 URL), bioRxiv 10.1101/288605(URL). 나머지 인용 ID는 rq_landscape의 verified 근거 ID와 이전 검토에서 확인된 ID다.
* literature.jsonl은 이번 지시 범위 밖이라 갱신하지 않았다.
