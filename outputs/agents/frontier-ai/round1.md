# Round 1 (Independent Discovery): frontier-ai

* 에이전트: frontier-ai (Agent 6, Frontier AI & Representation Learning)
* 주 담당 Axis: I (AI Model Families), J (Learning Objectives), R (Explainability & Mechanistic AI)
* 기준일: 2026-11-12
* 절차: `reference/protocols.md` P1
* 읽은 입력: `CLAUDE.md`, `reference/protocols.md`(P1), `reference/axes.md`, `reference/starting_papers.md`, `reference/existing_projects.md`, `reference/datasets_and_resources.md`, `outputs/stage1/dataset_intelligence_report.md`, `outputs/stage1/gate_decision.md`, `outputs/stage1/environment_gaps.md`, `outputs/STAGE_STATUS.md`(사용자 결정 기록 포함)
* 독립성: 이번 라운드에서 다른 에이전트 폴더(`outputs/agents/<다른 이름>/`)는 열지 않았다.
* 문헌 기록: `outputs/agents/frontier-ai/literature.jsonl` (32편, 전부 식별자 경로로 존재 확인. 2024~2026년 24편. Discussion/Limitations 본문 확인 28편, 초록만 3편, 검색 요약만 1편. arXiv 또는 ML 학회 논문 27편)

## 0. 요약

1. 이 라운드의 중심 관찰: 2025~2026년 AI 연구에서 **모델 내부의 정서 표상 자체가 연구 대상**이 되었다(LLM, VLM의 emotion vector와 그 인과 효과: arXiv:2604.07729, arXiv:2609.34742, arXiv:2502.05489). 이 연구들이 스스로 남긴 미해결 문제(국소성 vs 지속성, 인물 결속, appraisal의 인과 방향, 정서 vs 상황 맥락)는 그대로 **뇌에서 검정 가능한 대조 가설**이다.
2. 두 번째 관찰: 최신 video world model(V-JEPA 2)은 embedding뿐 아니라 **latent 예측과 예측오차(surprise)**를 제공한다(arXiv:2502.11831). 정서의 예측적 성분(suddenness, predictability appraisal, 놀람)을 pixel, latent 물리, 서사 의미 수준의 예측오차로 분해할 기준 모델이 생겼다. V-JEPA surprise를 fMRI 회귀자로 쓴 연구는 이번 검색에서 찾지 못했다.
3. 세 번째 관찰: mechanistic interpretability 도구(SAE)가 fMRI encoding에 들어오기 시작했지만(arXiv:2606.06857, arXiv:2506.11123), **재학습 불안정성**(arXiv:2502.12892)과 **비디오 시간 일관성 파괴**(arXiv:2604.03919)가 아직 해결되지 않아 정서 연구에 쓰려면 안정성 검증이 전제다.
4. 네 번째 관찰: 식별성(identifiability) 이론은 "뇌-자극 contrastive 정렬은 공유되는 무엇이든 인코딩한다"(arXiv:2303.09166)는 점을 보여 준다. 정서와 시각-의미 내용의 공선성(CLAUDE.md 6절)은 분석 기법만이 아니라 **뷰(view) 설계**로 다뤄야 한다(arXiv:2106.04619).
5. 사용자 결정(4개 데이터셋 원본 자극 보유)에 따라 아래의 모델 기반 아이디어는 G1 차단 없이 네 데이터셋 모두에서 가능하다. 단 Emo-FilM 보유 영상이 크레딧 절단 연구 판본과 같은지는 미확인이다(STAGE_STATUS 사용자 결정 기록).

---

## 1. 중요한 미해결 문제

### U1. 뇌의 "정서 표상"은 정서인가, 상황 표상을 정서 축에 투영한 것인가
* 내용: Ma & Kragel (2026)은 해마-vmPFC 정서 표상이 영화 간 일반화되므로 감각 feature를 넘는 추상이라고 해석했다(Discussion 둘째, 여섯째 단락). 그러나 최신 video world model, MLLM의 상황 표상도 영화 간 일반화된다. LLM 쪽에서도 같은 문제가 제기되었다: 정서 vector가 행동을 일으키는 기능적 정서인지, 더 풍부한 상황 맥락 구조의 투영인지(arXiv:2604.13466, 2절). Du 2025가 보고한 "MLLM embedding이 인간 평정보다 뇌를 잘 예측"하는 결과(arXiv:2509.24298)도 이 두 해석을 구분하지 못한다.
* 근거: doi:10.1038/s41467-025-68240-z, arXiv:2604.13466, arXiv:2604.07729, arXiv:2509.24298, doi:10.1126/sciadv.aaw4358
* 왜 미해결인가: 정서와 상황이 자연 자극에서 강하게 공선적이고, 두 가설의 예측이 갈리는 자극을 골라 검정한 연구가 없다(이번 검색 범위).

### U2. 정서 신경 표상은 "장면 국소적"인가, "지속 상태"인가
* 내용: Sofroniew et al. (2026)은 LLM 정서 표상이 현재 token에 작동하는 정서 개념만 국소적으로 추적하고 지속 상태를 유지하지 않으며, 이것이 인간 정서(지속성)와의 차이라고 썼다(5.3절). 동시에 저자들은 자신들의 probe가 지속 표상을 놓쳤을 가능성을 남겼다. 뇌에서 자연 영화 시청 중 정서 표상이 어느 쪽인지는 직접 검정되지 않았다.
* 근거: arXiv:2604.07729 (5.3절), arXiv:2602.07570 (짧은 창은 지각 영역, 긴 창은 PCC, dmPFC), doi:10.1038/s41467-025-68240-z (vmPFC의 긴 시간 통합 언급, Discussion 셋째 단락)

### U3. 정서적 놀람과 예측성 appraisal은 어느 수준의 예측오차와 결합하는가
* 내용: V-JEPA는 latent 예측오차로 직관 물리 위반에 "놀라지만" pixel 예측 모델과 MLLM은 chance였다(arXiv:2502.11831). 뇌는 장거리, 계층적 예측을 한다(doi:10.1038/s41562-022-01516-2). 정서 반응이 pixel, latent 물리, 서사 의미 중 어느 수준의 예측오차와 고유하게 연결되는지는 미검정이다.
* 근거: arXiv:2502.11831 (Discussion), arXiv:2506.09985 (9절: 16초 예측 범위), doi:10.1038/s41562-022-01516-2, doi:10.7554/eLife.107607 (video-text 미래 feature 선행, 본문 미열람)

### U4. 정서 관련 뇌 분산을 실은 "개념"을 안정적으로 식별할 수 없다
* 내용: dense feature encoding은 무엇이 설명하는지 말하지 못한다. SAE feature encoding이 언어 fMRI에서 시작되었지만(arXiv:2606.06857), SAE는 재학습마다 사전이 달라지고(arXiv:2502.12892), 비디오에서는 hard TopK가 프레임 간 일관성을 36% 낮추며(arXiv:2604.03919), 뇌 정렬 연구는 SAE 설정 민감도를 보지 않았다(arXiv:2506.11123, 5절).
* 근거: arXiv:2606.06857, arXiv:2506.11123, arXiv:2502.12892, arXiv:2604.03919, arXiv:2502.03714

### U5. appraisal과 정서 범주의 인과 방향
* 내용: LLM에서 appraisal 방향을 조작하면 정서 출력이 바뀌지만, appraisal이 정서의 원인인지 단지 상관인지, 방향이 반대인지는 미해결로 남았다(arXiv:2502.05489, 11절 둘째 단락). LLM은 정서 개념을 인간보다 "과도하게 범주적"으로 표상한다(arXiv:2508.05880). Ma & Kragel (2026)은 effort, certainty, situational control 같은 다른 변수를 남은 과제로 들었다(Discussion 일곱째 단락).
* 근거: arXiv:2502.05489, arXiv:2508.05880, doi:10.1038/s41467-025-68240-z

### U6. 뇌-자극 정렬로 얻은 latent에서 정서를 원리적으로 분리하는 방법이 없다
* 내용: multimodal contrastive learning은 용량 제한이 없으면 공유되는 모든 요인을 인코딩한다(arXiv:2303.09166, 7절). 뇌와 자극을 정렬하면 시각-의미 내용이 latent를 채운다. 반대로 "뷰 설계가 content를 정의한다"(arXiv:2106.04619, 6절)는 원리를 쓰면 정서를 content로 지정하는 설계가 가능하지만 시도된 적이 없다(이번 검색 범위).
* 근거: arXiv:2303.09166, arXiv:2106.04619, doi:10.1038/s41586-023-06031-6

### U7. 뇌의 정서 기하는 정서와 무관한 정렬로 운반되는가 (수렴의 상한)
* 내용: VLM 간에는 정서와 무관한 ImageNet activation으로 추정한 변환이 정서 vector 대응과 steering 효과까지 운반했다(arXiv:2609.34742, 결과 3). Platonic hypothesis는 모달리티 간 수렴이 상호정보량으로 상한이 정해진다고 했다(arXiv:2405.07987, 6절). 뇌의 정서 기하가 일반 시각-의미 정렬의 부산물인지, 별도 사상이 필요한지는 미검정이다.
* 근거: arXiv:2609.34742, arXiv:2405.07987, arXiv:2605.20496

### U8. 정서의 동기(action tendency) 성분에 자극 계산 모델이 없다
* 내용: Component Process Model의 motivation 성분과 action-readiness 이론은 AI 비교 연구에서도 다루지 않았다(arXiv:2508.05880 Limitations). 비디오에서 행동 표상을 라벨 없이 뽑는 latent action model(arXiv:2410.11758)이 생겼지만 조작 비디오 밖으로는 적용되지 않았다(6절).
* 근거: arXiv:2410.11758, arXiv:2508.05880, arXiv:2502.11831 (V-JEPA는 관찰자 예측만 가능, Discussion)

### U9. 뇌 신호를 학습 목표로 쓸 때 정서 관련 귀납 편향이 생기는가
* 내용: STS fMRI 예측으로 brain-tuning한 다모달 모델은 풍자 탐지가 좋아졌지만 정서 예측(CMU-MOSEI)은 개선되지 않았다(arXiv:2511.07988, 4~5절). 정서 영역을 목표로 한 tuning은 시도되지 않았다(이번 검색 범위).
* 근거: arXiv:2511.07988, doi:10.1126/sciadv.aaw4358 (여러 모델 비교와 recurrent feedback 필요, Discussion)

---

## 2. 주목해야 할 모델 또는 방법론

라이선스는 공개 저장소의 LICENSE 파일을 git으로 직접 확인한 경우만 확정으로 적었다(받은 코드는 실행하지 않음). huggingface.co는 이번 세션에서 열지 않았으므로 가중치 페이지의 조건은 미확인이다. 계산량은 `reference/datasets_and_resources.md` 1절(계산 자원)이 비어 있어 단일 A100급 GPU 기준의 **대략적 추정**이며 실측이 아니다.

| ID | 모델/방법 | Pretrained weights | Input → Output | 학습 목표 | 라이선스 (확인 수준) |
|---|---|---|---|---|---|
| M1 | **V-JEPA 2 / 2.1** (arXiv:2506.09985) + surprise 추출 (arXiv:2502.11831) | 공개 (dl.fbaipublicfiles.com 직접 링크, ViT-L/H/g, 2.1은 2026-03 공개). 체크포인트에 predictor 가중치 포함 여부 미확인 | 비디오 클립(16~64 프레임, 256/384 px) → patch token embedding, predictor의 미래 표상, 시점별 latent 예측오차 S_t | masked latent feature prediction (JEPA). 2-AC는 행동 조건 예측 | 코드 저장소 MIT [LICENSE 직접 확인]. surprise 코드 저장소(jepa-intuitive-physics)는 CC-BY-NC 4.0 [직접 확인] |
| M2 | **Sparse Autoencoder 계열**: TopK SAE (arXiv:2406.04093), Archetypal/RA-SAE (arXiv:2502.12892), Universal SAE (arXiv:2502.03714), 시공간 contrastive SAE (arXiv:2604.03919) | 비전, 비디오 모델용 사전학습 SAE 공개 여부 미확인. 직접 학습 전제 | 모델 activation (N x d) → sparse code (N x K, K는 d의 8~32배) | 재구성 + 희소성(TopK), convex hull 제약(A-SAE), 다모델 공동 재구성(USAE), 시간 contrastive | openai/sparse_autoencoder MIT, overcomplete(A-SAE 구현) MIT [직접 확인]. USAE, 비디오 SAE 코드 미확인 |
| M3 | **Emotion vector reading/steering**: RepE LAT (arXiv:2310.01405), 정서 개념 probe (arXiv:2604.07729), 다모델 공유 정서 부분공간 (arXiv:2609.34742), appraisal 방향 조작 (arXiv:2502.05489) | 방법은 공개, 적용 대상은 open VLM/LLM(Qwen3-VL, InternVL3.5, Gemma-3 등). Claude 내부 vector는 비공개 | 정서 유도 자극(합성 이야기, 이미지) → 층별 방향 벡터. 새 자극 → 각 정서 방향 투영값 시계열 | 학습 없음(평균 차, PCA, probe). steering은 activation 덧셈 | RepE 코드 MIT [직접 확인]. EmotionCircuits-LLM GPL-3.0 [직접 확인]. 대상 VLM 라이선스는 모델별 미확인 |
| M4 | **Latent Action Model**: LAPA의 latent action quantizer (arXiv:2410.11758). 참고: V-JEPA 2-AC | LAQ 가중치(OpenX 학습) 공개로 README에 기재 (HF, 미접속) | 프레임 쌍 (t, t+H) → 이산 latent action token | VQ-VAE: 현재 프레임 + latent action으로 미래 프레임 복원 | 코드 MIT [직접 확인]. 가중치 조건 미확인 |
| M5 | **식별 가능한 multi-view contrastive** (arXiv:2303.09166, arXiv:2106.04619) + **CEBRA** (doi:10.1038/s41586-023-06031-6) | CEBRA 패키지 공개(가중치 개념 없음, 데이터마다 학습) | 신경 시계열 (T x V) + 보조 변수(연속 평정, 생리, 시간) → 저차원 embedding | InfoNCE. positive pair를 보조 변수 또는 뷰로 정의 | CEBRA Apache-2.0(v0.4.0 이후), 특허 고지 있음 [직접 확인]. cl-ica MIT [직접 확인] |
| M6 | **In-context encoder**: BraInCoRL (arXiv:2505.15813) | 공개 (SharePoint 링크, README 기재) | 이미지 feature + 소수 voxel 반응 예시 → voxelwise encoder / 예측 반응 | voxel을 과제로 보는 meta-learning | Apache-2.0 [직접 확인] |
| M7 | **Label-free Concept Bottleneck** (arXiv:2304.06129) | 원 논문용 체크포인트 공개 (README) | backbone feature → 개념 활성(LLM이 만든 개념 집합, CLIP 유사도) → 예측 | 개념층 투영 + sparse 최종층 | 저장소 루트에 LICENSE 파일 없음 → 미확인 |
| M8 | **Brain-tuning** (arXiv:2511.07988, TVLT 기반) | 연구용 tuned 가중치 공개 여부 미확인 | 비디오+오디오 → ROI voxel 예측(학습 시), 이후 일반 표상 | fMRI 예측 손실로 미세조정 | TVLT MIT로 논문 체크리스트에 기재(저장소 직접 확인 안 함) |

참고(다른 에이전트 담당 영역이지만 라이선스 위험이 커서 기록): TRIBE v2 저장소는 CC-BY-NC-4.0 [직접 확인], DINOv3는 자체 "DINOv3 License"와 접근 신청 절차 [직접 확인], platonic-rep 저장소는 루트 LICENSE 없음 [직접 확인].

### 2.1 각 기술을 뇌 데이터에 적용할 때 필요한 것

| ID | 데이터 양 | 입력 형식 | 계산량 (추정, 미검증) | 주의 |
|---|---|---|---|---|
| M1 | 학습 불필요. surprise는 자극만으로 계산 | Horikawa: 클립별(평균 약 5 s, 0.15~90 s) 프레임. Emo-FilM: 연속 영화를 0.5~1 s 간격 sliding window로 잘라 TR(1.3 s)에 맞춰 HRF 합성곱. Spacetop: TR 0.46 s에 맞춤 | Emo-FilM 9,600 s를 0.5 s stride로: 약 1.9만 window, ViT-L 기준 수 GPU 시간, ViT-g 384는 그 수 배. Horikawa 2,181 클립은 1 GPU 수 시간 이내 | 사전학습 VideoMix22M에 YouTube 계열 포함. Cowen & Keltner 비디오, LIRIS-ACCEDE 영화와의 중복 여부 확인 불가(오염). 0.15 s 같은 초단 클립은 predictor 문맥이 부족 |
| M2 | SAE 학습: 자극셋이 아닌 일반 비디오 activation 수백만 token 이상. 뇌 쪽: Horikawa 2,181 표본/피험자는 K보다 작으므로 소수 feature 선택형 회귀(Lepori 방식) 필요 | 층별 activation 저장 (예: 1천만 token x 1,024차원 fp16 약 20 GB) | SAE 학습 1 GPU 수 시간~1일, 재학습 안정성 검증 시 x5~10 | SAE를 뇌 자극만으로 학습하면 과적합과 순환 추론. 재학습 간 개념 일치율을 보고해야 함 |
| M3 | 정서 vector 추출용 합성 자극 수백~수천 개(모델 쪽). 뇌 쪽은 기존 데이터 그대로 | 비디오는 프레임 묶음 또는 짧은 클립 + 고정 prompt. 시점별 residual stream 투영값 | 8B VLM로 Horikawa 2,181 클립 수 GPU 시간, Emo-FilM 2 s window 약 4,800개 수~십여 GPU 시간 | 모델 생성 정서 신호이며 인간 평정이 아님(CLAUDE.md 6절). vector가 "의도한 개념만" 담는다는 보장 없음(arXiv:2604.07729 5.1절) |
| M4 | 학습 불필요(기존 LAQ 사용) 또는 영화 장면으로 재학습 시 수십 시간 비디오 | 프레임 쌍, 간격 H는 TR 이하로 설정 | 추론은 가벼움 | 로봇, 손 조작 도메인과 영화 장면의 차이 큼. latent action이 카메라 움직임을 포착(저자 보고)하므로 편집 컷, 카메라 이동을 nuisance로 통제해야 함 |
| M5 | Emo-FilM 피험자당 약 7,400 TR(9,600 s / 1.3 s) x 30명이면 충분. Horikawa는 공개 전처리본이 블록 평균 1 sample/비디오(2,181/피험자)라 raw 재전처리로 시계열 확보 필요 | (T x V) 행렬 + 보조 변수 행렬, HRF 지연 정렬 | CPU~단일 GPU 수 분~수 시간 | 라벨로 학습하면 라벨 구조를 재현하는 순환 위험. 영화 단위 held-out과 일관성 지표 필수 |
| M6 | meta-training은 NSD 규모 필요(공개 체크포인트 사용 권장). 적용 시 피험자당 수십~수백 예시 | 정적 이미지 feature (비디오는 keyframe으로 근사, 저자가 동적 자극 미지원 명시) | 추론 가벼움, 재-meta-training은 다중 GPU 수일 | NSD 기반 체크포인트를 NSD 평가에 쓰면 누수. 정서 ROI는 학습 분포(고차 시각피질) 밖 |
| M7 | 개념 집합 20~100개, 자극별 개념 점수 | 자극 → VLM/CLIP 유사도 또는 MLLM appraisal 평정 → 개념 벡터 | 가벼움 | MLLM이 만든 appraisal 점수는 AI 추정 라벨. Emo-FilM의 인간 appraisal 평정과 일치도를 먼저 보고해야 함 |
| M8 | 피험자당 수 시간 연속 시청 fMRI. 후보: Emo-FilM 약 2.7 h x 30명, Horikawa 약 8 h x 5명, Spacetop 영화 약 2 h | 비디오(+오디오) window와 HRF 정렬된 ROI 반응 | 300M급 모델 미세조정 수 GPU 일 | 학습과 평가 영화, 데이터셋 분리. 정서 ROI SNR이 낮아 tuning 신호가 약할 수 있음 |

---

## 3. 다른 분야에 적용할 수 있는 연구 아이디어

방향 표기: [AI→정서신경] AI 기법을 정서 신경과학으로 이전, [정서신경→AI] 정서 신경 데이터로 AI 문제를 푸는 역방향.

### T1. World-model surprise로 본 정서의 예측오차 위계 [AI→정서신경]
* 출처 분야: 발달심리의 violation-of-expectation을 video SSL에 이식한 연구(arXiv:2502.11831), 언어 예측 위계(doi:10.1038/s41562-022-01516-2).
* 아이디어: 같은 영화에서 세 수준의 예측오차 시계열을 만든다. (a) pixel 수준: VideoMAE 재구성 오차, (b) latent 물리 수준: V-JEPA 2 surprise S_t, (c) 서사 의미 수준: 대사 transcript와 장면 캡션의 LLM surprisal. 편도체, 전측 섬엽, vmPFC에서 각 수준의 고유 설명 분산을 variance partitioning으로 추정하고, Emo-FilM 평정자의 Suddenly, Predictable appraisal과 참가자 EDA와의 결합을 비교한다.
* 데이터셋: Emo-FilM(주), Horikawa(짧은 클립 내 놀람, surprise 범주와 차원 평정), Spacetop(통증 cue 기대 위반과 대비)
* 선행 수행: V-JEPA surprise를 fMRI 회귀자로 쓴 연구는 미발견(WebSearch, arXiv 검색). video-text 미래 feature 연결은 VALOR(doi:10.7554/eLife.107607, 본문 미열람)가 부분 수행.

### T2. 정서와 무관한 정렬이 정서 구조를 운반하는가 [AI→정서신경]
* 출처 분야: VLM 간 정서 vector 전이(arXiv:2609.34742), 표상 수렴(arXiv:2405.07987).
* 아이디어: 저정서 자극만으로 VLM activation→voxel 선형 사상을 학습하고, VLM 정서 vector(또는 shared emotion subspace의 consensus vector)를 이 사상에 통과시켜 고정서 자극의 뇌 패턴 차이를 예측한다. 대조로 정서 자극으로 학습한 사상, 무작위 방향을 둔다.
* 데이터셋: Horikawa(규범 평정으로 저정서 클립 선정), NSD(AI 추정 affect가 낮은 이미지로 사상 학습, nsdmeadows 100장 참가자 평정으로 시험, 표본 작아 효과 크기 추정 중심)
* 선행 수행: VLM 간에서는 수행됨(arXiv:2609.34742), 뇌로는 미발견.

### T3. 뇌를 "또 하나의 모델"로 넣은 Universal SAE [AI→정서신경]
* 출처 분야: 다모델 공동 개념 사전(arXiv:2502.03714), 안정 사전(arXiv:2502.12892).
* 아이디어: V-JEPA 2, SigLIP 계열, Qwen-VL의 activation과 피험자별 voxel 반응을 한 sparse 사전으로 공동 재구성한다. 개념을 (모든 모델+뇌 공유), (모델만), (뇌만)으로 나누고, 정서 ROI에 뇌 고유 개념이 남는지, 남는 개념이 정서 평정과 상관되는지 본다.
* 데이터셋: Horikawa(2,181 x 5명, 표본이 작아 사전 크기 제약 필요), NSD(규모 검증용)
* 선행 수행: 뇌를 USAE에 넣은 연구 미발견. SAE-voxel 대응은 NSD에서 수행됨(arXiv:2506.11123).

### T4. 정서 vs 상황 판별 검정 [AI→정서신경]
* 출처 분야: LLM 정렬 연구의 판별 검정 논리(arXiv:2604.13466, 5절).
* 아이디어: 자극 쌍을 (상황 유사, 정서 상이), (상황 상이, 정서 유사)로 골라 ROI별 RSA에서 어느 쪽 유사도가 뇌 패턴 유사도를 예측하는지 비교한다. 상황 유사도는 Horikawa 비디오당 캡션 20개(arXiv:2509.24298 Methods가 사용한 Horikawa mind captioning 자료)의 LLM embedding과 V-JEPA embedding으로, 정서 유사도는 34범주 규범 평정으로 정의한다.
* 데이터셋: Horikawa(주), Emo-FilM(장면 단위)
* 주의: 캡션 자료의 보유 여부는 미확인. 없으면 MLLM 캡션(AI 생성)으로 대체하고 그 사실을 표기.

### T5. 국소 정서 신호 vs 지속 정서 상태 [AI→정서신경]
* 출처 분야: LLM 정서 표상의 국소성 발견(arXiv:2604.07729, 5.3절).
* 아이디어: VLM 정서 vector 투영값(장면 국소 신호)을 그대로 넣은 encoding과, 이를 ROI별 시간 상수 τ로 누적한 leaky integrator(state-space) 버전을 비교한다. τ가 HRF 규모(수 초)를 크게 넘어야 설명되는 ROI를 "지속 상태 영역"으로 정의한다.
* 데이터셋: Emo-FilM(연속, 장면 전환이 많음), Spacetop(영상 직후 사후 평정의 peak-end와 대비)
* 주의: HRF 모형 오지정과 BOLD 자기상관이 가짜 지속성을 만든다. HRF 다양화, 위상 무작위화 null, 평정 시계열 자기상관과 비교 필요.

### T6. Latent action으로 본 정서의 동기 성분 [AI→정서신경]
* 출처 분야: VLA, 로봇 학습(arXiv:2410.11758).
* 아이디어: 영화 프레임 쌍에서 latent action token을 뽑아(카메라 움직임, 편집 컷은 nuisance로 통제) Emo-FilM의 Motivation 항목(action tendency) 연속 평정과 운동, 전운동, 두정 영역 반응을 optical flow와 의미 feature 대비 고유하게 설명하는지 본다.
* 데이터셋: Emo-FilM(주), Spacetop
* 선행 수행: 영화, 사회 장면에 latent action을 적용한 연구 미발견.

### T7. 정서 영역 표적 brain-tuning [정서신경→AI, 동시에 AI→정서신경]
* 출처 분야: speech, 다모달 모델 brain-tuning(arXiv:2511.07988).
* 아이디어: Emo-FilM 편도체, 전측 섬엽, vmPFC 반응을 목표로 video 모델을 tuning하고, 대조로 STS, 시각피질 목표 tuning과 자극만 노출한 tuning을 둔다. 평가는 다른 데이터셋(Horikawa 규범 평정 예측, Spacetop alignvideo 사후 평정 예측, Horikawa 뇌 반응 예측)에서 한다.
* 의미: 정서 ROI가 주는 신호가 모델에 "정서 특이" 귀납 편향을 넣는지는 뇌 표상의 정보 내용에 대한 역추론 검정이다.

### T8. 뇌 정서 데이터를 AI 정서 표상의 외부 타당도 기준으로 [정서신경→AI]
* 출처 분야: LLM과 인간 정서 개념 비교(arXiv:2508.05880), 모델 내부 정서 연구(arXiv:2604.07729, arXiv:2609.34742).
* 아이디어: AI interpretability 쪽은 정서 vector의 타당성을 합성 자극과 행동으로만 검증한다. Horikawa와 Emo-FilM 뇌 반응에 대한 예측력, 범주성 지표(arXiv:2508.05880 방식)를 "뇌 기반 외부 타당도"로 제안할 수 있다. 결과는 AI 연구에도, "AI 주석이 과도하게 범주적인가"라는 정서 연구 측정 문제에도 쓰인다.

### T9. 정서 기대 위반 벤치마크로 world model 평가 [정서신경→AI]
* 아이디어: 직관 물리 VoE처럼, 정서적 기대 위반(예: 장례식장에서 웃음) 영상 쌍으로 world model의 surprise를 측정하면 "world model이 사회, 정서적 규칙성을 학습하는가"를 평가할 수 있다. 같은 자극의 인간 fMRI가 있으면 모델 surprise와 뇌 반응을 직접 비교할 수 있다. 현재 4개 데이터셋에는 통제된 위반 쌍이 없으므로 생성형 편집(Axis L)과 신규 수집이 필요하다.

---

## 4. 기존 Affective Neuroscience와 예상 밖으로 연결될 수 있는 개념

### C1. Violation-of-expectation (영아 연구 → video SSL) ↔ suddenness appraisal ↔ 정서적 놀람
V-JEPA의 surprise는 영아 VoE 패러다임을 모델 예측오차로 정량화한 것이다(arXiv:2502.11831). CPM의 suddenness, predictability appraisal(Emo-FilM 평정 항목)과 정서 범주 "surprise"(Horikawa)는 같은 계산의 다른 수준일 수 있다. 연결 논리는 "정서적 놀람은 latent 세계 모델의 예측오차가 가치, 관련성과 결합한 것"이라는 검정 가능한 가설이다.

### C2. Functional emotions의 인물 무차별성 ↔ portrayed vs experienced emotion
LLM 정서 표상은 사용자, 가상 인물, Assistant에 같은 기제로 작동한다(arXiv:2604.07729, 5.2~5.3절). 영화 시청 fMRI의 정서 decoding도 "등장인물이 표현한 정서"와 "시청자가 경험한 정서"를 구분하지 못한다(CLAUDE.md 6절 첫 구분). AI 쪽에서 1인칭 결속의 부재를 측정한 방법(같은 vector가 누구의 정서에 활성화되는가)을 뇌로 옮기면 "관점 결속(perspective binding)"이라는 새 변수가 생긴다. Spacetop은 같은 참가자에게 자기 경험(alignvideo), 인물 정서 귀속(shortvideo), 표정 지각(faces)을 모두 측정했다.

### C3. Superposition과 sparse dictionary ↔ 혼합 정서와 연속 gradient
SAE는 다의미 뉴런을 sparse 개념의 중첩으로 본다(arXiv:2406.04093). Cowen & Keltner식 "범주 사이의 연속 gradient"와 혼합 정서는 "소수 정서 개념의 sparse 중첩"으로도, "연속 다양체 위의 위치"로도 설명될 수 있다. 두 모형(sparse 조합 vs 연속 좌표)이 뇌 패턴을 예측하는 정도를 비교하면 범주 이론과 차원 이론 논쟁에 계산적 판별 기준을 준다. RepE도 혼합 정서 군집을 보고했다(arXiv:2310.01405, 6.1.1절).

### C4. 표상 수렴의 정보 상한 ↔ 정서의 "말로 다 못함"
Platonic hypothesis 저자들은 언어가 "개기일식을 보는 형언할 수 없는 경험"을 담을 수 있는지를 반례로 들고, 수렴은 모달리티 간 상호정보량으로 상한이 정해진다고 했다(arXiv:2405.07987, 6절). 무음 비디오(Horikawa)를 볼 때의 뇌 정서 표상과 정서 단어, 캡션 표상의 정렬 상한은 "정서 경험 중 언어로 전달되는 몫"의 정량 지표가 된다. Kragel 2019가 말한 "사람이 쉽게 이름 붙일 수 없는 feature"(doi:10.1126/sciadv.aaw4358, Discussion 둘째 단락)와도 연결된다.

### C5. Data augmentation이 정의하는 불변성 ↔ 정서의 자극 불변성
SSL 이론에서 content는 "뷰 사이에 늘 보존되는 것"으로 정의된다(arXiv:2106.04619). 정서를 "같은 정서를 일으키는 서로 다른 자극 사이에 보존되는 신경 성분"으로 정의하면, 정서 이론의 오랜 질문(정서는 자극 유형을 넘어 같은 신경 상태인가)이 식별성 문제로 바뀐다. 어떤 뷰 쌍을 쓰느냐가 곧 정서의 조작적 정의가 된다.

### C6. Latent action과 affordance ↔ action tendency
로봇 학습의 latent action(arXiv:2410.11758)은 "장면이 다음에 허용하는 움직임"을 라벨 없이 표현한다. 이는 Frijda의 action readiness와 생태심리학의 affordance를 비디오에서 측정할 수 있는 형태로 만든다.

---

## 5. 새 Sub-axis 또는 하위 연구 방향

| ID | 제안 | 소속 Axis | 독립 Axis 필요 여부 | 근거 |
|---|---|---|---|---|
| S1 | **World-model predictor signals**: embedding이 아닌 latent 예측 표상과 예측오차(surprise) 시계열을 뇌 회귀자로 사용 | I (주), N, D | 불필요. I에 하위항목으로 두고 N(Predictive Coding)과 교차 표시 | arXiv:2506.09985, arXiv:2502.11831 |
| S2 | **Latent Action / VLA representations**: 행동 라벨 없는 행동 표상으로 action tendency 측정 | I | 불필요 | arXiv:2410.11758 |
| S3 | **Brain-tuning (신경 반응을 학습 목표로)**: 특히 정서 ROI 표적 tuning | J | 불필요. J의 "Representation Alignment"와 구분되는 독립 하위항목 | arXiv:2511.07988 |
| S4 | **Identifiable multi-view objectives**: 뷰 설계를 가설로 쓰는 block-identifiable contrastive | J (주), P | 불필요 | arXiv:2303.09166, arXiv:2106.04619 |
| S5 | **In-context / meta-learned encoding (test-time adaptation)** | J, H, O | 불필요 | arXiv:2505.15813 |
| S6 | **Model-internal emotion representations**: AI 내부 정서 vector, functional emotion, 그 인과 효과를 뇌와 비교하는 대상으로 다룸 | R 또는 새 Axis | **독립 Axis 후보 (아래)** | arXiv:2604.07729, arXiv:2609.34742, arXiv:2502.05489 |
| S7 | **Universal concept dictionaries including brain + 안정성/시간 일관성 감사** | R (주), Q | 불필요 | arXiv:2502.03714, arXiv:2502.12892, arXiv:2604.03919 |
| S8 | **Discriminating tests between representational hypotheses** (정서 vs 상황 등) | R, P, T | 불필요. P와 T에 교차 | arXiv:2604.13466 |

### 독립 Axis 제안: "U. Machine Affect Representations (AI 내부 정서 표상)"
* 이유: 지금 분류에서 AI 내부 정서 표상은 I(모델 종류)나 R(해석 방법)에 들어가지만, 실제로는 **"무엇을 묻는가"(Construct) 유형의 대상**이다. 2026년 연구는 모델 내부 정서 표상의 기하(valence, arousal 축), 국소성, 인물 무차별성, 행동 인과성을 측정했다(arXiv:2604.07729). 이를 뇌의 정서 표상과 같은 수준의 비교 대상으로 두면 "AI 정서 표상과 뇌 정서 표상이 어디서 같고 다른가"라는 질문군이 생긴다.
* Sub-axis 후보: 정서 vector 기하, 국소성 vs 지속성, 관점 결속, appraisal 회로, 정서 표상의 행동 인과성, 다모델 공유 정서 부분공간, AI 정서 주석의 범주성 편향
* 위험: 모델 내부 표상을 주관 경험으로 해석하지 않는다는 원칙(arXiv:2604.07729 5.3, 5.5절 저자들의 단서)을 Axis 정의에 명시해야 한다. Coordinator 판단에 맡긴다.

---

## 6. Discussion-to-Research chains

형식: Original Finding → Unresolved Question → Technological Development → New Dataset / Model Combination → New Research Question. 각 단계에 근거 ID와 원문 위치를 단다. 모든 RQ는 탐색 후보이며 확정 질문이 아니다.

### CH1. 정서 지도 vs 상황 지도
* **Original Finding:** 해마는 정서 범주를 위계적으로, vmPFC는 2D affective 궤적을 표상하고 decoding이 영화 간 일반화된다. 저자는 이를 감각 feature를 넘는 추상의 근거로 해석했다. [doi:10.1038/s41467-025-68240-z, Discussion 둘째 단락과 여섯째 단락]
* **Unresolved Question:** 저자들도 지도 구조가 "사건 전이의 통계적 규칙성 학습"에서 올 수 있다고 썼다[같은 논문 Discussion 다섯째 단락]. 그렇다면 그 지도는 정서 특이적인가, 정서와 무관하게 학습된 상황, 사건 전이 구조의 투영인가. LLM에서 같은 형태의 문제가 제기되었다[arXiv:2604.13466, 2절 'Two Hypotheses'].
* **Technological Development:** 정서 라벨 없이 인터넷 비디오로 학습한 latent world model이 장면 상태와 전이를 표현한다[arXiv:2506.09985, 9절 Future work 첫째 단락: 다중 시간척도 계층 예측이 다음 과제]. LLM 정서 표상은 범용 인물 모델링 기제의 일부라는 보고[arXiv:2604.07729, 5.2절].
* **New Dataset / Model Combination:** Emo-FilM 14편 x 30명 + V-JEPA 2(또는 2.1) 장면 latent의 군집 상태와 전이 행렬 + 장면 캡션(MLLM 생성, AI 생성 표기)의 LLM embedding + 별도 평정자 정서 평정(13 discrete + Feeling).
* **New Research Question:** Emo-FilM 시청 중 해마-vmPFC의 정서 지도 구조는 정서 평정과 무관하게 학습된 video world model의 상태 전이 구조를 통제한 뒤에도 남는가? 남는다면 어느 정서 항목과 해마 장축의 어느 위치에서 남는가?
* **반증 기준:** world model 전이 구조를 조건으로 넣었을 때 정서 decoding이 영화 단위 순열 null과 구분되지 않으면 "정서 지도"는 상황 지도의 투영이라는 해석이 지지된다. 반대로 고유 분산이 남으면 정서 특이 조직의 증거가 된다(관찰 데이터이므로 인과 결론은 아님).
* **방법론 주의:** leave-one-film-out(14 fold), 영화 수준 confound, 제공 전처리본의 6 mm smoothing(raw 재전처리 권장), 평정은 별도 평정자 규범 평정이므로 참가자 경험으로 해석 금지, V-JEPA 사전학습 데이터와 LIRIS-ACCEDE 영화의 중복 확인 불가.
* overlap: Emo-FilM 연구 (Emo-FilM에서 사전학습 모델로 정서 맥락 기여 분석). Ma & Kragel 2026이 기준점(partially done).

### CH2. 정서적 놀람은 어느 수준의 예측오차인가
* **Original Finding:** latent 공간 예측으로 학습한 V-JEPA는 직관 물리 위반 영상에 유의하게 큰 surprise를 보였고, pixel 예측 모델과 MLLM은 chance였다[arXiv:2502.11831, Discussion 첫째 단락]. 뇌는 장거리, 계층적 예측 표상을 가진다[doi:10.1038/s41562-022-01516-2; 프리프린트 arXiv:2111.14232 Discussion 'Long-range predictions'].
* **Unresolved Question:** V-JEPA는 3~4초 기억, 관찰자 예측만 가능, 상호작용 위반은 chance이며 계층적 JEPA가 필요할 수 있다[arXiv:2502.11831, Discussion 둘째 단락]. 예측 범위는 약 16초다[arXiv:2506.09985, 9절]. 언어 연구는 "원시 미래는 곧 불확정해지지만 추상 표상은 오래 예측 가능"하다고 추론하고 joint embedding 손실을 언급했다[arXiv:2111.14232, Discussion 'On the potential benefit of a predicting coding architecture']. 정서 반응이 어느 수준의 예측오차와 결합하는지는 검정되지 않았다(V-JEPA surprise-fMRI 연구는 WebSearch와 arXiv 검색에서 미발견. video-text 미래 feature는 doi:10.7554/eLife.107607이 부분 수행, 본문 미열람).
* **Technological Development:** V-JEPA 2/2.1 predictor와 공개 surprise 추출 코드(jepa-intuitive-physics, CC-BY-NC). LLM surprisal을 명시적 nuisance로 넣는 sparse encoding 틀[arXiv:2606.06857, 7절 Discussion 둘째 단락].
* **New Dataset / Model Combination:** Emo-FilM(평정자의 Suddenly, Predictable appraisal 1 Hz + 참가자 EDA, PPG) + Horikawa(surprise 범주와 차원 규범 평정, 짧은 클립) + 세 수준 예측오차(VideoMAE 재구성 오차, V-JEPA 2 S_t, transcript/캡션 LLM surprisal).
* **New Research Question:** 자연 영화 시청 중 편도체, 전측 섬엽, vmPFC 반응과 평정자의 suddenness, predictability appraisal은 pixel, latent 물리, 서사 의미 예측오차 중 어느 것과 고유하게 결합하는가? 그 결합은 fMRI 참가자의 EDA 반응을 매개로 하는가?
* **반증 기준:** latent 예측오차(V-JEPA)가 pixel 오차와 LLM surprisal을 통제한 뒤 정서 ROI에서 고유 분산이 0과 구분되지 않으면 "latent 세계 모델 예측오차가 정서 반응의 한 성분"이라는 가설은 지지되지 않는다.
* **방법론 주의:** 모델 surprise는 참가자 surprise가 아니다(in-silico vs observed). appraisal은 별도 평정자, EDA는 fMRI 참가자의 것이라 주체가 다르다. 컷 편집과 장면 전환이 세 지표 모두를 올리므로 컷 회귀자를 넣는다.
* overlap: 없음(기존 프로젝트 요약 기준).

### CH3. 정서 신경 표상의 국소성, 지속성, 관점 결속
* **Original Finding:** LLM 정서 표상은 현재 맥락에 작동하는 정서 개념을 국소적으로 추적하고 지속 상태를 유지하지 않으며, 같은 표상이 어느 인물의 정서에도 적용된다[arXiv:2604.07729, 5.3절 셋째, 넷째 단락].
* **Unresolved Question:** 저자들은 선형 probe가 혼합 정서와 특정 인물에의 결속을 놓칠 수 있고[5.1절 첫째 항목], 지속 표상이 probe에 잡히지 않았을 가능성을 남겼다[5.3절 마지막 단락]. 인간 뇌에서 자연 시청 중 정서 표상이 국소적인지 지속적인지, 자기와 타인에 같은 표상이 쓰이는지는 이 비교의 반대편으로 남아 있다.
* **Technological Development:** open VLM에서 정서 vector와 다모델 공유 정서 부분공간을 추출하는 방법[arXiv:2609.34742, 7절; Appendix G.2는 video MLLM 확장을 미래 과제로 명시], RepE LAT[arXiv:2310.01405, 6.1절; 7절은 궤적과 state-space 분석을 미래 과제로 명시].
* **New Dataset / Model Combination:** Emo-FilM 연속 영화 + VLM 정서 vector 투영 시계열(모델 생성 신호) + ROI별 leaky integrator 시간 상수 추정. Spacetop 같은 참가자의 alignvideo(자기 경험 사후 평정), shortvideo(인물 mentalizing), faces(표정 지각) 비교.
* **New Research Question:** 영화 시청 중 정서 관련 뇌 반응은 장면 국소 정서 신호로 충분히 설명되는가, 아니면 HRF를 넘는 시간 상수의 누적(관성)이 필요한가? 같은 참가자에서 자기 경험 정서와 타인 정서 귀속은 같은 신경 방향을 공유하는가?
* **반증 기준:** 모든 ROI에서 최적 τ가 HRF 규모와 구분되지 않으면 "지속 상태 영역" 가설은 기각된다. 자기와 타인 조건 간 방향 cosine이 피험자 간 split-half 신뢰도 수준이면 공유 표상, 그보다 유의하게 낮으면 분리 표상으로 해석한다.
* **방법론 주의:** HRF 오지정과 자기상관(CLAUDE.md 6절), Spacetop alignvideo 평정 약 51% 결측과 평정 구간의 HRF 중첩, Emo-FilM 평정 z-score(상대 변화).
* overlap: Emo-FilM 연구 (시간 정보 기여 분석과 인접).

### CH4. appraisal → emotion의 인과 방향
* **Original Finding:** LLM의 appraisal 개념 방향(other-agency, pleasantness)을 조작하면 정서 출력이 예측 가능한 방향으로 바뀐다[arXiv:2502.05489, 10 Discussion 첫째 단락].
* **Unresolved Question:** appraisal이 정서와 단지 상관되거나 인과 방향이 반대일 수 있다[arXiv:2502.05489, 11 Limitations 둘째 단락]. LLM은 정서 개념을 인간보다 범주적으로 표상하며 appraisal 외 이론은 비교되지 않았다[arXiv:2508.05880, Limitations 'Operationalization']. 정서 지식은 effort, certainty, situational control 같은 변수로 조직될 수도 있다[doi:10.1038/s41467-025-68240-z, Discussion 일곱째 단락].
* **Technological Development:** LLM 내부 appraisal 조작으로 "appraisal → emotion 영향 행렬"을 in-silico로 추정할 수 있다(가설 생성기). SAE 기반 인과 feature 분석[arXiv:2604.25866, 초록 기준].
* **New Dataset / Model Combination:** Emo-FilM appraisal 10항목 + discrete 13항목 1 Hz 평정 + 영화 transcript와 장면 캡션을 넣은 open LLM의 appraisal 조작 결과 + fMRI.
* **New Research Question:** Emo-FilM에서 appraisal 성분의 신경 표상은 discrete emotion 표상보다 시간적으로 선행하는가? LLM 내부 appraisal 조작으로 얻은 영향 행렬은 평정 시계열과 뇌에서 추정한 선행 관계와 일치하는가?
* **반증 기준:** appraisal 신경 표상이 정서 표상보다 선행하지 않거나(시차 0 또는 역방향), LLM 영향 행렬과 뇌 선행 구조의 상관이 순열 null 수준이면 "LLM appraisal 기제가 인간 정서 생성 구조를 반영한다"는 가설은 지지되지 않는다.
* **방법론 주의:** 관찰 데이터의 시간 선행은 인과가 아니다(decodability vs causality). 평정자 반응 지연이 항목마다 다를 수 있다. TR 1.3 s와 1 Hz 평정의 정렬. LLM 조작 결과는 in-silico 예측이다.
* overlap: 없음(기존 프로젝트 요약 기준).

### CH5. 정서 관련 뇌 분산을 실은 sparse 개념의 안정성
* **Original Finding:** SAE feature를 넣은 encoding이 소수 feature로 voxel군을 해석하고 사람 관련 내용에 조율된 voxel군을 찾았다[arXiv:2606.06857, 7 Discussion 첫째~넷째 단락]. SAE 단위를 voxel에 직접 사상할 수 있었다[arXiv:2506.11123, 5절 Conclusion].
* **Unresolved Question:** SAE 설정이 뇌 정렬에 미치는 영향은 보지 않았다[arXiv:2506.11123, 5절 Limitations]. SAE는 재학습마다 사전이 달라진다[arXiv:2502.12892, 3절과 6 Conclusion]. 비디오에서 표준 SAE는 시간 일관성을 파괴한다[arXiv:2604.03919, 6 Discussion과 7 Conclusion]. 다모델 사전은 마지막 층만 다뤘다[arXiv:2502.03714, Appendix A.6]. 해석은 SAE 기저에 한정된다[arXiv:2606.06857, Limitations].
* **Technological Development:** RA-SAE(안정), 시공간 contrastive SAE(시간 일관), USAE(다모델 공유).
* **New Dataset / Model Combination:** Horikawa 2,181 클립(34범주 + 14차원 규범 평정) + V-JEPA 2, SigLIP 계열, Qwen-VL activation의 RA-SAE 또는 USAE + 재학습 5회 이상. Emo-FilM에서 재현.
* **New Research Question:** Horikawa에서 정서 평정과 공유되는 뇌 분산을 설명하는 sparse 개념 집합은 SAE 재학습과 backbone 교체에 걸쳐 안정한가? 안정한 개념은 정서 개념인가, 상황, 사람, 객체 개념인가?
* **반증 기준:** 재학습 간 선택 개념의 일치율이 무작위 기대 수준이면 개념 수준 해석은 보고하지 않는다. 안정 개념이 대부분 객체, 장면 개념이면 "정서 관련 뇌 분산 = 시각-의미 내용"이라는 대안 설명이 지지된다.
* **방법론 주의:** SAE를 Horikawa 자극만으로 학습하면 순환. 반복 제시가 없어 noise ceiling이 없으므로 원 논문 방식의 대체 ceiling(내용 중복 쌍, ISC)을 함께 보고. 34범주 평정은 별도 평정자.
* overlap: EmoViS (Horikawa 정서 기하의 sensory-semantic 기원).

### CH6. 정서와 무관한 정렬이 정서 기하를 운반하는가
* **Original Finding:** 정서와 무관한 ImageNet activation으로 추정한 아키텍처 간 변환이 정서 vector의 대응과 steering 효과를 복원했다[arXiv:2609.34742, 초록 결과 3과 7 Conclusion].
* **Unresolved Question:** 비디오, 복합 정서, 연속 정서 라벨로의 확장은 미래 과제로 남았다[arXiv:2609.34742, Appendix G.2]. 모달리티 간 수렴은 상호정보량으로 상한이 정해질 수 있다[arXiv:2405.07987, 6절]. MLLM embedding의 뇌 예측 우위가 무엇 때문인지는 분해되지 않았다[arXiv:2509.24298, Limitations and future directions 둘째 단락: 두 모델 중심, 인간 기준은 시뮬레이션].
* **Technological Development:** 정서 무관 정렬 추정과 정서 vector 운반 절차, 다모델 consensus 정서 vector.
* **New Dataset / Model Combination:** Horikawa(규범 평정으로 저정서 클립을 골라 VLM→voxel 사상 학습, 고정서 클립으로 시험) + NSD(AI 추정 affect가 낮은 이미지로 사상 학습, nsdmeadows 100장 참가자 평정으로 시험).
* **New Research Question:** 정서와 무관한 자극으로만 학습한 VLM→뇌 사상에 VLM 정서 vector를 통과시키면 고정서 자극에서의 뇌 정서 패턴 차이를 예측하는가? 그 정도는 정서 범주와 ROI에 따라 어떻게 다른가?
* **반증 기준:** 운반된 정서 방향의 예측력이 무작위 방향, 내용 방향(객체 범주 방향)과 구분되지 않으면 "뇌 정서 기하는 일반 정렬로 운반된다"는 가설은 기각된다. 이 경우 정서는 별도 사상이 필요한 신경 조직이라는 해석이 강해진다.
* **방법론 주의:** 저정서 자극 선정 라벨이 인간 규범인지 AI 추정인지 표기. NSD의 정서 범위 제한과 COCO의 VLM 학습 데이터 포함(오염). NSD nsdmeadows 지시문(felt vs perceived) 미확인.
* overlap: EmoViS (방향 인접).

### CH7. 정서 영역 표적 brain-tuning
* **Original Finding:** STS fMRI 예측으로 tuning한 다모달 모델은 STS 정렬과 풍자 탐지가 개선되었지만 정서 예측은 개선되지 않았다[arXiv:2511.07988, 4절 Downstream Tasks Results].
* **Unresolved Question:** 저자들은 학습 맥락과 다른 맥락으로의 전이 실패, 단일 모델과 적은 평가를 한계로 들었다[arXiv:2511.07988, 5 Conclusion]. EmoNet 연구는 같은 목표의 여러 모델 비교와 recurrent feedback 모델을 요구했다[doi:10.1126/sciadv.aaw4358, Discussion 여섯째, 일곱째 단락].
* **Technological Development:** speech, 다모달 모델 brain-tuning 절차(arXiv:2511.07988과 그 선행 speech brain-tuning).
* **New Dataset / Model Combination:** Emo-FilM 편도체, 전측 섬엽, vmPFC 표적 tuning vs STS, 시각피질 표적 tuning vs 자극만 노출. 평가는 Horikawa(무음, 다른 자극과 피험자)와 Spacetop.
* **New Research Question:** 정서 ROI 반응을 목표로 brain-tuning한 비디오 모델은 STS나 시각피질 표적 tuning보다 다른 데이터셋의 정서 평정과 정서 관련 뇌 반응을 더 잘 예측하는가?
* **반증 기준:** 정서 ROI tuning의 이득이 시각피질 tuning, 자극 노출 대조와 같으면 정서 ROI 신호는 모델에 정서 특이 정보를 주지 않는다(정서 ROI 반응이 주로 감각, 내용 신호라는 해석과 양립).
* **방법론 주의:** 정서 ROI SNR, 데이터셋 간 영화 중복 없음 확인, 평가 라벨은 별도 평정자(Horikawa)와 참가자 본인(Spacetop)으로 주체가 다르다.
* overlap: EmoBrain (V-JEPA2와 teacher-student distillation 사용 가능성, 방법 일부).

### CH8. 피험자 간 공유되는 신경 정서 차원의 수
* **Original Finding:** multimodal contrastive learning은 모달리티 간 공유 요인을 block 단위로 식별하며, 용량 제한이 없으면 공유되는 모든 요인을 인코딩한다[arXiv:2303.09166, 7 Discussion 'Implications and scope']. 어떤 augmentation을 쓰느냐가 content를 정의한다[arXiv:2106.04619, 6 Discussion].
* **Unresolved Question:** content 요인 수 추정과 세 개 이상 모달리티 확장은 미해결이다[arXiv:2303.09166, 7절 Limitations and outlook]. 라벨을 쓴 contrastive embedding은 라벨 구조를 강제할 수 있다[doi:10.1038/s41586-023-06031-6, arXiv:2204.00673 v2 Discussion 셋째 단락]. 신뢰 가능한 정서 차원 수 추정은 Cowen & Keltner 방향 2로 남아 있다(`reference/starting_papers.md` 특별 지시).
* **Technological Development:** encoding 차원을 줄여 가며 공유 block을 찾는 식별 가능한 contrastive, 조건부 contrastive로 시각-의미 feature를 style로 처리.
* **New Dataset / Model Combination:** Horikawa 5명 동일 자극(raw 재전처리 필요) + Emo-FilM 30명 동일 영화. 뷰: 피험자 A 뇌, 피험자 B 뇌, 규범 정서 평정. nuisance: V-JEPA 2와 캡션 embedding.
* **New Research Question:** 같은 자극에 대해 피험자 간 공유되는 신경 latent는 몇 차원이며, 그중 정서 평정과도 공유되는 차원은 몇 개인가? 시각-의미 feature를 조건으로 통제하면 몇 개가 남는가?
* **반증 기준:** 시각-의미 feature를 통제한 뒤 정서 평정과 공유되는 차원 수가 0과 구분되지 않으면 "Horikawa 정서 표상은 고차원"이라는 원 결론의 신경 근거는 내용 feature로 설명될 수 있다(Westlin 2025 재현 실패 보고와의 관계 검토 필요, 미열람 preprint).
* **방법론 주의:** 유한 표본, 연속 latent 가정 위반, Horikawa 반복 없음(noise ceiling 없음), 영화 14편의 영화 수준 공선성.
* overlap: EmoViS (Horikawa 정서 기하), EmoBrain (cross-subject).

---

## 7. 담당 Axis 확장 제안

### Axis I (AI Model Families)
* 추가:
  * **World-model predictors** (V-JEPA 2-AC, latent 예측기). 기존 "VideoMAE / V-JEPA / Video Models"에서 encoder와 predictor를 분리한다. 근거: arXiv:2506.09985, arXiv:2502.11831
  * **Latent Action Models / VLA** (LAPA, Genie류). 근거: arXiv:2410.11758
  * **Open-weight VLM/LLM with inspectable internals** vs **API-only MLLM** 구분. 내부 표상 분석과 steering이 가능한지에 따라 할 수 있는 연구가 달라진다. 근거: arXiv:2609.34742, arXiv:2509.24298(Qwen2-VL 사용)
  * **Brain-tuned models** (fMRI로 미세조정된 모델). 근거: arXiv:2511.07988
* 재분류: "Brain-inspired / Neuromorphic Models"는 Axis N(Brain-like Computation)과 중복이 크므로 N으로 이동하고 I에는 교차 표시만 둔다.
* 우선순위 하향(삭제 아님): "Graph Neural Networks"는 4개 데이터셋 구조에서 직접 쓰임이 적다(functional connectivity 분석 시에만).

### Axis J (Learning Objectives)
* 추가:
  * **Joint-Embedding Predictive (latent prediction)**를 Masked Modeling과 구분. pixel 복원과 latent 예측은 직관 물리 이해 출현에서 결과가 갈렸다. 근거: arXiv:2502.11831
  * **Identifiable multi-view objectives** (뷰 설계가 식별되는 content를 정한다). 근거: arXiv:2303.09166, arXiv:2106.04619
  * **Brain-tuning (neural data as objective)**. 근거: arXiv:2511.07988
  * **In-context / meta-learned encoding (test-time adaptation)**. 근거: arXiv:2505.15813
  * **Sparse dictionary learning objectives** (TopK, archetypal, 시간 contrastive). R과 교차. 근거: arXiv:2406.04093, arXiv:2502.12892, arXiv:2604.03919
* 재분류: "Disentangled Representation Learning"을 "Identifiability-based Disentanglement"로 구체화한다. 비지도 disentanglement는 귀납 편향 없이 식별되지 않는다는 결과가 알려져 있으므로(Locatello et al., arXiv:1811.12359, 존재만 확인, 본문 미열람) 뷰나 보조 변수가 있는 방법으로 범위를 좁힌다.

### Axis R (Explainability & Mechanistic AI)
* 추가:
  * **Model-internal emotion vectors / functional emotion representations** (또는 독립 Axis U로 승격, 5절). 근거: arXiv:2604.07729, arXiv:2609.34742, arXiv:2310.01405, arXiv:2502.05489
  * **Universal concept dictionaries including brain**. 근거: arXiv:2502.03714
  * **Stability and temporal-coherence audits** (개념 분해의 재현성). Axis Q와 교차. 근거: arXiv:2502.12892, arXiv:2604.03919
  * **Augmented sparse encoding** (해석 가능한 sparse feature + 명시적 nuisance 회귀자). 근거: arXiv:2606.06857
  * **Discriminating tests between representational hypotheses**. Axis P, T와 교차. 근거: arXiv:2604.13466
  * **In-silico causal intervention as hypothesis generator** (모델 내부 조작 결과를 뇌 검정의 사전 예측으로 사용, 결과는 in-silico로 표기). 근거: arXiv:2502.05489, arXiv:2604.07729
* 재분류: "Model Disagreement"는 Axis T(Model Comparison)와 중복되므로 R에는 "모델 간 개념 불일치 분석(USAE 고유 개념)"으로 좁혀 둔다.

---

## 8. 교차 점검: CLAUDE.md 6절 적용 메모

| 점검 항목 | 이 라운드 아이디어에서의 구체적 위험 | 대응 |
|---|---|---|
| Pretrained 학습 데이터 오염 | EmoNet은 Cowen & Keltner 프레임 137,482장으로 학습되었고 Horikawa 자극이 같은 라이브러리다(doi:10.1126/sciadv.aaw4358, Results와 Methods). V-JEPA 2(YouTube 계열), Qwen 계열 MLLM, COCO 기반 VLM의 학습 데이터에 Cowen & Keltner 비디오, interactive map, LIRIS-ACCEDE 영화, COCO 이미지가 들어갔는지 확인할 수 없다 | EmoNet은 Horikawa 분석에서 제외하거나 오염 조건으로 별도 표기. 결과 해석에 "오염 가능성 미배제" 명시 |
| 인간 vs 모델 생성 정서 라벨 | 정서 vector 투영값, MLLM appraisal 점수, MLLM 캡션은 모두 모델 생성 신호 | 변수명에 `ai_` 접두, 인간 평정과 같은 표에 섞지 않음 |
| 참가자 경험 vs 규범 평정 | Horikawa, Emo-FilM 정서 평정은 별도 평정자 규범 평정 | 결과를 "참가자 경험"으로 쓰지 않음. Spacetop만 참가자 본인 사후 평정 |
| Decodability vs representation vs causality | CH4의 시간 선행, CH6의 운반 성공은 인과 증거가 아님 | 관찰 결과로 한정하고 인과 표현 금지 |
| In-silico vs observed | 모델 surprise, LLM appraisal 조작 결과 | in-silico 예측으로 명시하고 실제 fMRI 검정과 분리 |
| HRF와 자기상관 | CH3의 지속성 추정, CH2의 시계열 회귀 | HRF 다양화, 위상 무작위화 null, 블록 순열 |
| Stimulus/movie-level leakage | SAE와 정렬 사상을 같은 자극으로 학습, 평가 | 영화 또는 클립 단위 held-out, SAE는 외부 비디오로 학습 |
| ROI 선택과 순환 추론 | 정서 ROI를 같은 데이터의 정서 대비로 정의 | 독립 atlas(HCP360 등)나 독립 데이터셋 localizer 사용 |
| 라이선스 | TRIBE v2, jepa-intuitive-physics CC-BY-NC, DINOv3 자체 라이선스, EmotionCircuits GPL-3.0 | 연구 목적 사용과 재배포 범위를 Stage 4 pilot 전에 확인 |

---

## 9. 검증된 것과 미확인인 것

### 검증된 것
* literature.jsonl 32편 모두 arXiv API, Crossref, PubMed ID 변환, PMLR proceedings 페이지 중 하나로 존재를 확인했다.
* Discussion, Limitations, Conclusion 원문을 직접 읽은 논문 28편. 각 future direction에 원문 절 위치를 달았다.
* 저장소 LICENSE 파일 직접 확인: V-JEPA 2 코드 MIT, jepa-intuitive-physics CC-BY-NC 4.0, LAPA MIT, BraInCoRL Apache-2.0, openai/sparse_autoencoder MIT, overcomplete MIT, RepE MIT, cl-ica MIT, CEBRA Apache-2.0(특허 고지), DINOv3 자체 라이선스, TRIBE v2 CC-BY-NC-4.0, EmotionCircuits-LLM GPL-3.0. Label-free-CBM과 platonic-rep은 루트 LICENSE 없음.
* EmoNet 학습 자극이 Cowen & Keltner 비디오 프레임이라는 사실(PMC 본문).
* Du 2025가 Horikawa 비디오당 캡션 20개(Horikawa mind captioning 자료)를 사용했다는 사실(본문 Methods). 우리 환경에 이 캡션이 있는지는 미확인.

### 미확인
* V-JEPA 2 체크포인트에 predictor 가중치가 포함되는지, 가중치 자체의 라이선스(코드 MIT와 동일한지).
* huggingface.co에 있는 가중치(LAPA LAQ, TRIBE v2 등)의 조건(이번 세션에서 열지 않음).
* Qwen3-VL, InternVL3.5, Gemma-3 등 open VLM의 라이선스.
* Caucheteux 2023과 CEBRA는 최종 출판본이 아니라 arXiv 프리프린트 본문을 읽었다(nature.com 접속 거부). 최종본에서 Discussion이 바뀌었을 수 있다.
* VALOR(doi:10.7554/eLife.107607)는 검색 요약만 봤다(elifesciences.org가 JavaScript 요구). 저자 정보도 미확인.
* Platonic brain(arXiv:2605.20496), Shu 2026(arXiv:2604.25866), Guo 2026(arXiv:2605.23035)은 초록만 봤다.
* Gao 2024 SAE의 학회 채택 여부(ICLR 2025로 알려졌으나 미확인), Tak 2025의 ACL 트랙.
* 각 "already_done: no" 판정은 이번 arXiv 검색과 WebSearch 범위 안의 판단이다. 특히 V-JEPA surprise-fMRI, 뇌를 포함한 USAE, 정서 ROI brain-tuning, 정서 무관 정렬의 정서 운반은 Round 2 이후 다른 에이전트의 문헌과 교차 확인이 필요하다.
* 계산량 수치는 추정이며 우리 환경의 GPU 사양은 미확인이다.

### 실행 기록 (사실)
* 셸 curl로 export.arxiv.org(메타데이터, 검색), arxiv.org/pdf(본문), api.crossref.org, proceedings.mlr.press, pmc.ncbi.nlm.nih.gov(2편 본문 후 reCAPTCHA로 차단)에 접근했다. www.nature.com은 프록시 403으로 차단되었다.
* GitHub 공개 저장소 14개를 `--no-checkout`으로 받아 LICENSE와 README만 열었다. 코드는 실행하지 않았다. 내려받은 파일은 scratchpad(`/tmp/claude-0/-home-user-emotion-explore/4a0aeef6-c090-5f71-8a99-9b8e7c0f6d89/scratchpad/frontier-ai/`)에 있다.
* PubMed MCP는 DOI→PMID/PMCID 변환에만 사용했다.

---

## 부록: 문헌 목록 (literature.jsonl 요약)

| ID | 연도 | 분야 | verified_by | discussion_read |
|---|---|---|---|---|
| arXiv:2506.09985 (V-JEPA 2) | 2025 | ML | arxiv | full_text |
| arXiv:2502.11831 (Intuitive physics, V-JEPA surprise) | 2025 | ML + 발달인지 | arxiv | full_text |
| arXiv:2410.11758 (LAPA, ICLR 2025) | 2024 | ML (VLA) | arxiv | full_text |
| arXiv:2405.07987 (Platonic, ICML 2024) | 2024 | ML | arxiv | full_text |
| arXiv:2106.04619 (content/style, NeurIPS 2021) | 2021 | ML | arxiv | full_text |
| arXiv:2303.09166 (multimodal identifiability, ICLR 2023) | 2023 | ML | arxiv | full_text |
| arXiv:2304.06129 (Label-free CBM, ICLR 2023) | 2023 | ML | arxiv | full_text |
| arXiv:2210.01936 (VLM bag-of-words, ICLR 2023) | 2023 | ML | arxiv | full_text |
| arXiv:2505.15813 (BraInCoRL, NeurIPS 2025) | 2025 | Neuro-AI | arxiv | full_text |
| arXiv:2602.07570 (temporal context MLLM-brain) | 2026 | Neuro-AI | arxiv | full_text |
| arXiv:2406.04093 (TopK SAE) | 2024 | ML | arxiv | full_text |
| arXiv:2502.03714 (Universal SAE, ICML 2025) | 2025 | ML | arxiv | full_text |
| arXiv:2502.12892 (Archetypal SAE, ICML 2025) | 2025 | ML | arxiv | full_text |
| arXiv:2604.03919 (video SAE, ACM MM 2026) | 2026 | ML | arxiv | full_text |
| arXiv:2310.01405 (RepE) | 2023 | ML | arxiv | full_text |
| arXiv:2502.05489 (LLM emotion mech interp, ACL 2025) | 2025 | ML + 정서 | arxiv | full_text |
| arXiv:2604.07729 (Emotion concepts in an LLM) | 2026 | ML | arxiv | full_text |
| arXiv:2609.34742 (VLM emotion concepts generalize) | 2026 | ML | arxiv | full_text |
| arXiv:2604.13466 (functional emotions vs situational contexts) | 2026 | ML (note) | arxiv | full_text |
| arXiv:2508.05880 (Too categorical) | 2025 | ML + 정서 | arxiv | full_text |
| arXiv:2506.11123 (SAE-BrainMap) | 2025 | Neuro-AI | arxiv | full_text |
| arXiv:2606.06857 (Augmented sparse encoding) | 2026 | 언어 신경 + MI | arxiv | full_text |
| arXiv:2511.07988 (multimodal brain-tuning) | 2025 | Neuro-AI | arxiv | full_text |
| arXiv:2509.24298 (Du, MLLM 정서 기하, Horikawa) | 2025 | 정서 신경 + MLLM | arxiv | full_text |
| doi:10.1038/s41586-023-06031-6 (CEBRA) | 2023 | 계산 신경 | crossref | full_text (arXiv v2) |
| doi:10.1038/s41562-022-01516-2 (predictive coding hierarchy) | 2023 | 언어 신경 | crossref | full_text (arXiv 프리프린트) |
| doi:10.1126/sciadv.aaw4358 (EmoNet) | 2019 | 정서 신경 | pubmed | full_text |
| doi:10.1038/s41467-025-68240-z (Ma & Kragel) | 2026 | 정서 신경 | pubmed | full_text |
| arXiv:2605.20496 (Platonic brain) | 2026 | Neuro-AI | arxiv | abstract_only |
| doi:10.7554/eLife.107607 (VALOR) | 2025 | Neuro-AI | crossref | search_summary |
| arXiv:2604.25866 (SAE emotion LLM) | 2026 | ML | arxiv | abstract_only |
| arXiv:2605.23035 (SAE brain-LLM topography, CoNLL 2026) | 2026 | Neuro-AI | arxiv | abstract_only |
