# Round 1 (Independent Discovery): vision-decoding

* 에이전트: vision-decoding (Agent 3, Vision Decoding & Brain Reconstruction)
* 담당: Axis B (Perceptual & Stimulus Representation), Axis G (Decoding), 외부 분야 Memory and Mental Imagery
* 기준일: 2026-11-12
* 절차: `reference/protocols.md` P1
* 읽은 파일: `CLAUDE.md`, `reference/protocols.md`(P1), `reference/axes.md`, `reference/starting_papers.md`, `reference/existing_projects.md`, `reference/datasets_and_resources.md`, `outputs/stage1/dataset_intelligence_report.md`, `outputs/stage1/gate_decision.md`, `outputs/stage1/environment_gaps.md`, `outputs/STAGE_STATUS.md`(사용자 결정 기록 포함), `.claude/agents/vision-decoding.md`
* 독립성: 다른 에이전트 폴더(`outputs/agents/<다른 이름>/`)는 열지 않았다.
* 문헌 기록: `outputs/agents/vision-decoding/literature.jsonl` 28편. 28편 모두 식별자 경로로 존재 확인(arXiv API 13, Crossref 11, PubMed 3, 학회 공식 페이지 1). 2024~2026년 16편. Affective Neuroscience 밖 분야(ML, CV, 인지신경과학의 기억, 심상) 18편 이상. 본문(Discussion, Limitations, Conclusion) 직접 확인 23편, 초록만 5편(CLIP, Saarimäki 2016, Dijkstra 2019, Nikolaus 2025, Takagi 2023).
* 근거 표기: [본문] 논문 본문 직접 확인, [초록] 초록만 확인, [검색] 검색 색인 수준(verified로 세지 않음).
* 실행 사실: 셸에서 arxiv.org, export.arxiv.org, api.crossref.org, pmc.ncbi.nlm.nih.gov(간헐적 차단), openaccess.thecvf.com, proceedings.mlr.press 접근에 성공했다. api.github.com은 403, huggingface.co는 연결 실패라 우회하지 않았고, 코드와 checkpoint 공개 여부는 논문 본문에 적힌 경우만 [본문], 나머지는 [검색]으로 표기했다.

---

## 0. 이 라운드의 핵심 발견 (Coordinator가 먼저 볼 것)

### 0.1 Horikawa 자극의 두 번째 fMRI 코호트가 공개되어 있다 (MindCaptioning, ds005191)

Horikawa (2025, Science Advances, doi:10.1126/sciadv.adw1464) Mind captioning 연구는 **Horikawa 2020과 같은 Cowen & Keltner (2017) 비디오**를 썼다 [본문: Materials and Methods "Visual stimuli"; 자극 출처 참고문헌 36번이 Cowen & Keltner 2017이고 요청 양식 링크도 Horikawa 2020과 같다].

| 항목 | 내용 [본문] |
|---|---|
| 피험자 | 6명(일본어 모국어, 영어 능숙도 다양). S1은 예비 실험으로 같은 자극에 여러 번 노출 |
| 스캐너 | 3T Prisma, TR 1 s, 2 mm, 전뇌, multiband 6 |
| 지각 학습 데이터 | 2,196개 중 중복 16개를 뺀 고유 2,180개 비디오를 각 1회 시청(무음, 60 run) |
| 지각 테스트 | 72개 비디오를 각 5회 반복(Horikawa 2020에 없던 반복 제시, noise ceiling 추정 가능) |
| 회상 imagery | 72개 테스트 비디오를 텍스트 cue 뒤 눈 감고 회상, 비디오당 5회(30 run x 12 trial). 회상 직후 실제 비디오 재제시, 시행별 정확도와 vividness 5점 평정 |
| 주석 | 비디오당 MTurk 캡션 20개. **주석자에게 정서 반응이 아닌 시각 내용만 쓰도록 지시** |
| 보조 | retinotopy, fLoc, MT+, 언어 localizer |
| 공개 | OpenNeuro ds005191 v1.0.2(raw), figshare 10.6084/m9.figshare.25808179(전처리), GitHub horikawa-t/MindCaptioning, Zenodo 10.5281/zenodo.15686864 |

함의:
* Horikawa 2020(5명)과 합치면 **같은 2,180개 정서 비디오에 대한 11명 표본**이 된다. Stage 1이 지적한 Horikawa의 한계 중 "5명", "반복 없음(noise ceiling 불가)"을 부분적으로 보완한다. "참가자 본인 정서 보고 없음"은 그대로다(MindCaptioning 참가자는 캡션이 지각과 맞는지만 평정했다).
* 같은 정서 클립의 **회상 imagery와 vividness**가 있어 외부 분야 Memory and Mental Imagery를 정서 질문과 직접 결합할 수 있다.
* "정서를 쓰지 말라"는 지시로 수집된 **인간 중립 캡션**은 정서와 시각-의미 내용을 분리하는 자연 실험 통제 변수가 된다(AI 캡션이 아니라 인간 캡션이라는 점이 중요).
* 이미 이 데이터를 정서에 쓴 연구가 있다: EmoMind (arXiv:2605.16739, 2026)가 MindCaptioning 6명으로 34차원 C&K 정서 벡터를 해독해 정서 캡션을 생성했고, Horikawa 2020은 교차 데이터셋 평가에만 썼다 [본문]. 회상 imagery의 정서 분석은 확인 범위 내에서 찾지 못했다.

상태: 논문 Data availability 기준 공개. **OpenNeuro 저장소 내용, 라이선스, figshare에 캡션이 포함되는지는 직접 확인하지 못했다.** 사용자 보유 4개 데이터셋 밖이라 **사용 여부는 사용자 결정 사항**이다. 두 코호트 사이 피험자 중복 여부도 미확인이다(교차 코호트 일반화 주장 시 subject-level leakage 위험).

### 0.2 현행 재구성 모델은 정서를 평가한 적이 없고, 구조적으로 정서 손실을 내포한다

* MindEye2 입력은 NSD `nsdgeneral`(후두엽 시각 반응 영역) voxel뿐이다 [본문: Appendix A.2]. Brain-IT는 Algonauts 판 약 40k vertex, "주로 시각 관련 피질"이다 [본문: 5.1]. Brain-Diffuser도 nsdgeneral이며 전뇌 입력은 미래 과제로 남겼다 [본문: Discussion 넷째 단락]. 즉 **편도체, 섬엽, vmPFC의 정서 정보는 입력 단계에서 배제**된다.
* 해독 목표는 CLIP 계열 공간이고, 생성기 prior는 COCO 자연 장면(NSD) 분포다. Stage 1 보고서는 NSD 이미지 정서가가 대체로 중립이라고 기록했다. 따라서 정서 유발 영상에 이 모델을 쓰면 **정서 중립화 편향**이 예상된다(MIRAGE 3.3절은 NSD prior가 재구성 내용을 지배한다고 보고 [본문]).
* MindEye2, Brain-IT, NSD-Imagery, MIRAGE 본문에서 valence, emotion, affect 평가는 없다(키워드 검색으로 확인). NSD-Imagery와 MIRAGE는 정서 장애의 침습적 imagery를 응용처로만 언급했다 [본문: 5.1, 3.2].
* EmoMind 초록은 기존 뇌-텍스트 시스템이 "의미 내용을 복원하고 정서를 버린다"고 명시했다 [본문].

### 0.3 Portrayed vs Experienced 구분 논리 (모든 제안에 공통 적용)

세 수준을 구분한다.
* **P (portrayed):** 자극에 그려진 정서. 인물 표정, 장면 내용 등 자극 속성.
* **N (normative evoked):** 별도 평정자 집단이 그 자극을 보고 보고한 경험의 평균. Horikawa와 MindCaptioning의 C&K 34/14 평정, Emo-FilM 연속 평정이 여기에 속한다.
* **X (experienced):** 해당 fMRI 참가자 본인의 경험.

재구성 이미지나 해독 캡션의 정서는 정의상 이미지, 텍스트 공간의 속성이다. 따라서 **P 또는 N에 관한 정보이며 X의 증거가 아니다.** 분리 전략:

| 논리 | 내용 | 가능한 데이터 |
|---|---|---|
| L1 image-computable 상한 | 원 자극에 같은 정서 평가기를 적용한 값이 재구성 정서를 완전히 예측하면 그 정보는 자극 수준(P/N)이다 | Horikawa, MindCaptioning, NSD |
| L2 피험자 간 변동 | 같은 자극의 재구성 정서가 피험자마다 다르고 그 차이가 반복 간 신뢰도를 넘을 때만 개인 특이 후보다. 이것도 X가 아니라 개인 시각 처리 차이일 수 있다 | MindCaptioning 72클립 x 5회 |
| L3 본인 보고 대응 | 개인 특이 성분이 참가자 본인 보고를 예측해야 X로 해석할 수 있다 | Spacetop alignvideo(본인 평정 + 나머지 참가자 평균을 규범 대리로 사용)만 가능. Horikawa, MindCaptioning, NSD 대부분 불가 |
| L4 영역 해리 | 시각-의미 정보를 통제한 뒤 비시각 영역에서만 회복되는 정서 정보는 평가, 내수용 처리 가설과 부합. 단 decodability이지 경험이나 인과의 증거는 아님 | Horikawa, MindCaptioning(전뇌) |
| L5 회상 조건 | 자극 없는 회상에서 해독되는 정서는 현재 입력 주도는 아니나, 정서 지식(무엇이 슬픈 장면인지)의 의미 기억일 수 있음. vividness 공변과 영역 해리로 일부 구분 | MindCaptioning imagery |
| L6 생성 prior 분리 | 재구성의 정서가 뇌 해독 latent에서 왔는지 생성 prior에서 왔는지: guidance 강도 sweep, 무작위, shuffled 뇌 입력 기준선(Shirakawa 2025 방식), 동일 latent 다중 seed | 모든 재구성 분석 |

---

## 1. 중요한 미해결 문제

### U1. 재구성 파이프라인은 정서 정보를 얼마나 보존하고, 손실은 어느 단계에서 생기는가
* 근거: arXiv:2403.11207(입력 nsdgeneral, Appendix A.2; 5.1 Limitations), doi:10.1038/s41598-023-42891-8(Discussion 넷째: 전뇌 입력 미해결), arXiv:2605.16739(초록: 뇌-텍스트는 정서를 버림), doi:10.1126/sciadv.adw1464(Discussion 여덟째: 정서 반영 실패는 주석 지시 때문).
* 손실 후보 단계: (a) 입력 영역 제한, (b) 해독 목표 공간(CLIP)의 정서 표현력, (c) 생성 prior(중립 분포), (d) 주석과 학습 목표(시각 내용 위주). 어느 단계가 지배적인지 분해한 연구는 확인 범위 내에 없다.

### U2. 해독된 "정서"는 규범(N)인가 경험(X)인가
* 근거: arXiv:2605.16739(목표가 C&K 규범 평정이라고 본문이 명시하면서도 피험자별 ridge의 차이를 개인 정서 구조로 해석), arXiv:2507.00320(Discussion 둘째, 셋째: 개인별 BOLD 군집 구조가 규범 평정과 거의 대응하지 않음; 여덟째: 개인 자기보고와 조밀 촬영 필요).
* 현재 공개 자료 중 같은 데이터셋 안에서 본인 보고와 규범 대리를 함께 갖는 것은 Spacetop alignvideo뿐이다(Stage 1 3.2절).

### U3. 정서 decoding, 재구성이 "분류 + 환각"인지 조합적 표상의 복원인지
* 근거: doi:10.1016/j.neunet.2025.107515(2.2.1 output dimension collapse; 3 Discussion 첫째, 다섯째; 3.1.1). Cowen & Keltner 라이브러리는 범주를 잘 유발하도록 모은 군집 표본이라 같은 위험이 있다. Horikawa 2020의 같은 원본에서 잘린 클립 여부(movie-level leakage)도 Stage 1에서 미확인이다.
* 정서 범주 단위로 학습-테스트를 분리한 zero-shot 검증은 확인 범위 내에 없다.

### U4. 회상, 심상에서 정서 관련 표상이 재활성되는가, 그리고 시각 세부보다 더 잘 남는가
* 근거: doi:10.1126/sciadv.aaw4358(Discussion 일곱째: imagery가 시각피질 정서 코드를 활성할 수 있다는 미검증 제안), doi:10.1038/ncomms15037(Discussion 넷째: imagery의 위계적 점진 동원), arXiv:2506.06898, arXiv:2605.17198(imagery에서 저차원, 의미, 텍스트 기반 해독이 유리), doi:10.3758/s13423-017-1313-9(NEVER: 부정 정서가가 감각 재현 강화), doi:10.1038/s41467-022-33161-8(Discussion 셋째: 비공간 feature의 지각-기억 차이 미해결).
* Saarimäki 2016(doi:10.1093/cercor/bhv086)은 시나리오 imagery와 영화의 기본 정서 교차 분류를 보였지만[초록], 같은 에피소드를 보고 회상할 때의 딥 feature 수준 재활성 비교는 확인 범위 내에 없다.

### U5. 정서 정보는 시각피질 밖에서 "재구성 가능한 형태로" 추가되는가
* 근거: doi:10.1126/sciadv.aaw4358(후두엽이 정서 범주 해독), doi:10.1038/s41467-024-49073-8(OTC의 의미-정서 공동 표상), doi:10.1523/JNEUROSCI.1436-24.2025(편도체를 image-computable 함수로 모델링), arXiv:2411.07121(전뇌 해독에서 DMN, dorsal attention 기여).
* 비시각 영역이 더하는 정보가 의미인지 정서인지 분리한 연구는 확인 범위 내에 없다. WAVE는 정서를 분석하지 않았다.

### U6. 교차 피험자 공유 latent는 정서의 개인 차이를 보존하는가 지우는가
* 근거: arXiv:2403.11207(2.1 공유 자극 없이 선형 정렬), arXiv:2510.25976(5.3 voxel embedding만 적응), arXiv:2404.07850(피험자 불변 표상 학습), arXiv:2507.00320(개인 고유 구조), arXiv:2605.17198(3.2 개인 고유 imagery는 해독 주장 안 함).
* 공유 성분과 개인 성분의 정서 정보량을 따로 잰 연구는 확인 범위 내에 없다.

### U7. 정서 영역의 "선호 자극"은 무엇이며 자극 집합에 따라 달라지는가
* 근거: doi:10.1523/JNEUROSCI.1436-24.2025(Discussion 여덟째: 영화 한 편 학습이라 정서 범위 제한, 다른 자극으로 일반화 필요), arXiv:2306.03089(Limitations: 합성 이미지의 실제 검증, 새 ROI 적용), doi:10.1126/sciadv.aaw4358(Limitations: adversarial 스키마 이미지의 인간 경험 효과 미평가).

### U8. 동영상 정서 동역학의 재구성 병목
* 근거: arXiv:2410.19452(9 Limitations: 장면 전환 구간 재구성 실패), arXiv:2605.16739(Limitations: 클립당 벡터 하나라 시간 동역학 소실). 정서 전이가 장면 전환과 겹치는 경우가 많아 Emo-FilM 같은 장편 자극에서 직접적인 장애물이다.

---

## 2. 주목할 모델과 방법론

### 2.1 재구성, 해독 모델

| 모델 | 학습 데이터 | 입력 형식 | 출력 / 학습 목표 | Pretrained weights | 라이선스 | 다른 데이터셋 이식 조건 |
|---|---|---|---|---|---|---|
| **MindEye2** (arXiv:2403.11207, ICML 2024) | NSD 8명(7명 사전학습 + 1명 fine-tune) | nsdgeneral voxel 13k~18k, GLMsingle single-trial beta, 학습셋 기준 voxel z-score [본문 A.2] | 피험자별 ridge → 4096 공유 latent → MLP → diffusion prior로 OpenCLIP ViT-bigG/14 token(256x1664). 손실: diffusion prior + retrieval contrastive + low-level. SDXL unCLIP 생성 [본문 2절] | 코드 GitHub MedARC-AI/MindEyeV2 [본문 arXiv comment], checkpoint는 Hugging Face pscotti/mindeyev2 train_logs [검색] | 코드, 가중치 라이선스 미확인 [검색]. NSD 데이터는 NSD Terms 필요 | 새 피험자는 fine-tune 데이터 필요(논문 기준 1 session). Horikawa: 비디오 블록 평균 → 프레임 선택 필요, 3T 2 mm vs 7T 1.8 mm, 시각 ROI 마스크 재정의, 피험자당 2,181 블록은 NSD 약 3 session 규모. COCO 밖 분포는 성능 저하 예상 [본문 5.1] |
| **Brain-IT** (arXiv:2510.25976, ICLR 2026) | NSD 8명 + COCO 비표지 120k에 encoder로 합성 fMRI | Algonauts 판 약 40k vertex(주로 시각 피질), 학습 시 15k 샘플링 [본문 5.1, D.1] | voxel→128 functional cluster(V2C), BIT가 adapted CLIP(L2 손실)과 VGG feature(InfoNCE) 예측, DIP + diffusion [본문 3, D.1] | 공식 코드 WeizmannVision/brainit-fmri, 결과 이미지 HF Amitz244/Brain-IT_Results. transfer learning 학습 코드는 미공개 항목 [검색]. 본문은 "출판 시 코드, checkpoint 공개" 예고 [본문 II] | 논문 CC BY-NC-SA 4.0 [본문 표기], 코드 라이선스 미확인 | 새 피험자는 voxel embedding만 최적화. 비시각 영역 token을 넣으려면 Universal Brain Encoder 재학습 필요. Horikawa는 surface 투영 필요(pycortex 자료 제공) |
| **Brain-Diffuser** (doi:10.1038/s41598-023-42891-8) | NSD 4명 | nsdgeneral voxel | VDVAE latent, CLIP-Vision, CLIP-Text latent를 ridge로 해독, Versatile Diffusion img2img | 코드와 사전학습 가중치 GitHub ozcelikfu/brain-diffuser [본문 Code availability] | 미확인 | ridge만 학습하므로 Horikawa, MindCaptioning에 **처음부터 재학습이 가장 쉽다**. 입력 영역을 바꾸는 실험에 적합. NSD-Imagery에서 imagery 일반화 최상 [본문 arXiv:2506.06898] |
| **MIRAGE** (arXiv:2605.17198) | NSD | NSD voxel | 선형 backbone, 저차원 이미지 feature + 텍스트 + 저수준 feature로 diffusion guidance | 공개 GitHub 저장소 언급 [본문 A.16], 가중치 공개 여부 미확인 | 논문 CC BY-NC-ND 4.0 [본문 표기] | imagery 해독용 설계 원칙(선형, 저차원, 텍스트)이 MindCaptioning 회상 분석에 그대로 쓰인다 |
| **Mind captioning** (doi:10.1126/sciadv.adw1464) | 자체 6명(C&K 비디오), NSD 4명 추가 분석 | 전뇌 voxel 블록 평균(4 s shift), z-score [본문] | 42개 LM의 semantic feature를 선형 해독, MLM 기반 단어 최적화로 문장 생성 | 코드 GitHub + Zenodo, 데이터 OpenNeuro, figshare [본문] | 미확인 | 자극이 Horikawa 2020과 같아 **Horikawa에 바로 이식 가능**. 정서 채널은 없음 |
| **EmoMind** (arXiv:2605.16739) | MindCaptioning 6명 | MNI 공간 피질 voxel, PCA 후 ridge [본문 3] | 중립 캡션 retrieval + 34차원 C&K 벡터 ridge, CFG rewriter | 본문에서 공개 여부 확인 못함 | 미확인 | 피험자별 matched-stimulus 보정 필요 [본문 Limitations]. 우리 질문의 가장 가까운 선행 작업 |
| **WAVE** (arXiv:2411.07121) | 대규모 fMRI 사전학습 + BOLD5000 | 전뇌 DiFuMo 1024 parcel, 5 TR clip | contrastive image-fMRI fine-tune + 생성 decoder | 코드 GitHub PPWangyc/WAVE, 모델 HF PPWangyc/WAVE-models [본문] | 논문 CC BY 4.0 [본문 표기], 코드 미확인 | parcel 시계열 입력이라 raw BIDS가 있는 Horikawa, Emo-FilM, Spacetop에 이식 가능. 비시각 네트워크 기여 분석의 선례 |
| **NeuroClips** (arXiv:2410.19452, NeurIPS 2024) | cc2017 동영상 fMRI 3명 | 시각피질 fMRI 프레임 | keyframe + perception flow를 T2V diffusion에 주입 | 미확인 | arXiv 기본 라이선스 [본문 표기] | 장면 전환 구간 실패 [본문 9]. Emo-FilM 장편 영화에는 TR 1.3 s와 전환 문제로 제한적 |
| **MindBridge** (arXiv:2404.07850, CVPR 2024) | NSD | 피험자별 크기가 다른 voxel을 aggregation | cyclic reconstruction으로 피험자 불변 표상 | 코드 GitHub littlepure2333/MindBridge [본문 arXiv comment] | 논문 CC BY-NC-SA 4.0 [본문 표기] | 공유-개인 분해 질문의 대조 모델 |
| **Takagi & Nishimoto** (CVPR 2023) | NSD | 초기 시각피질 → z, 고차 시각피질 → c | Stable Diffusion 입력 선형 해독 | 미확인 | 미확인 | z(저수준)와 c(의미)의 영역 분리 구조라 정서가 어느 경로로 들어오는지 분해에 유용 [초록] |

### 2.2 정서 encoding, 합성, 평가 도구

| 모델 | 학습 데이터 | 입력 | 출력 / 목표 | 공개 | 이식 조건과 주의 |
|---|---|---|---|---|---|
| **EmoNet** (doi:10.1126/sciadv.aaw4358) | Cowen & Keltner 비디오 프레임(AlexNet fine-tune, 20 범주) | 이미지 | 정서 범주 확률, fc7 4096 | PyTorch 구현 ecco-laboratory/emonet-pytorch [본문: Jang & Kragel Code Availability] | **Horikawa, MindCaptioning 자극과 학습 자료가 같다**(Jang & Kragel Data Availability의 EmoNet fine-tuning 자료 요청 링크가 Horikawa 2020 비디오 요청 링크와 동일 [본문]). 이 두 데이터에서 평가기나 feature로 쓰면 오염 |
| **편도체 encoding + 합성** (doi:10.1523/JNEUROSCI.1436-24.2025) | NNDb 20명, 영화 1편 | EmoNet fc7 | 편도체 하위영역 voxel 예측, GAN 기반 activation maximization | 코드 GitHub ecco-laboratory/AMOD [본문] | 정서 범위가 넓은 Horikawa로 재학습할 가치. feature 추출기는 C&K 비노출 모델로 교체 필요 |
| **BrainDiVE** (arXiv:2306.03089, NeurIPS 2023) | NSD | encoder gradient | diffusion guided 합성 | GitHub aluo-x/BrainDiVE [검색] | 편도체, 섬엽, vmPFC encoder에 연결하면 정서 영역 선호 이미지 합성. in-silico 결과 |
| **EmoSet 학습 분류기** (arXiv:2307.07961, ICCV 2023) | 330만 장(11.8만 인간 주석) | 이미지 | 정서 범주 + 속성(밝기, 채도, 장면, 물체, 표정, 행동) | 데이터셋 공개 여부 본문에서 확인 못함 | C&K와 겹치지 않는 평가기 후보. 주석은 평정자 판단(P/N 수준) |
| **EmoGen** (arXiv:2401.04608, CVPR 2024) | EmoSet | 정서 범주 | CLIP 공간에 정렬한 정서 공간으로 T2I | 미확인 | counterfactual 정서 latent 생성, 정서 방향 정의에 사용. 내용만 다루고 색, 스타일은 제외 [본문 Limitations] |
| **CLIP / OpenCLIP** (arXiv:2103.00020) | 웹 4억 쌍 | 이미지, 텍스트 | 대조 학습 embedding | 공개 [초록 수준 지식] | 대부분 재구성 모델의 목표 공간. C&K GIF나 COCO가 학습에 포함됐는지 확인 불가(오염 가능성) |

### 2.3 데이터셋별 이식 체크리스트

| 데이터셋 | 바로 가능한 것 | 필요한 전처리 | 주요 위험 |
|---|---|---|---|
| Horikawa (보유) | Brain-Diffuser식 ridge 재학습, Mind captioning식 LM feature 해독 | 비디오 → 프레임 또는 video feature, 블록 내 짧은 클립 반복 처리, 시각 ROI와 해부학적 피질하 ROI(사전 정의), native → surface(Brain-IT) | 반복 없음, 5명, 무음, movie-level leakage, EmoNet 오염 |
| MindCaptioning (보유 미확인) | Horikawa와 같은 자극의 6명, 72클립 5회 반복, 회상 | figshare 전처리본 구조 확인 | 피험자 중복 미확인, S1 사전 노출, imagery 뒤 같은 비디오 제시로 HRF 겹침 |
| Emo-FilM (보유) | 1 Hz 연속 정서와 프레임 단위 재구성 평가 | 제공 전처리본은 6 mm smoothing이라 재구성 용도에는 raw 재전처리 권장(Stage 1), 영화 → 프레임 HRF 정렬 | 영화 14편, 소리, 장면 전환, TR 1.3 s |
| Spacetop (보유) | alignvideo 본인 평정과 leave-one-out 집단 평균 | fsLR 91k 사용 가능, 영상 프레임 | 평정 51% 결측, 49개 영상, 평정 구간과 HRF 겹침 |
| NSD (보유) | MindEye2, Brain-IT, Brain-Diffuser checkpoint 직접 사용, NSD-Imagery | 없음 | 정서 라벨 100장뿐, 중립 분포, NSD 학습 모델을 NSD 분석에 쓰면 누수 |

---

## 3. 다른 분야에 적용할 수 있는 연구 아이디어

| ID | 아이디어 | 이전 방향 | 근거 |
|---|---|---|---|
| I1 | **재구성 벤치마크의 "정서 충실도" 지표.** 의미, 저수준 지표만 쓰는 재구성 평가에 여러 출처 정서 평가기(C&K 비노출 분류기, CLIP zero-shot 프롬프트, 인간 평정)를 추가하고 평가기 간 불일치까지 보고한다. NSD 학습 prior의 정서 중립화를 정량화하는 도구가 된다 | Affective computing → BCI, 뇌 해독 평가 | arXiv:2403.11207, arXiv:2510.25976(정서 지표 없음), arXiv:2307.07961, doi:10.1016/j.neunet.2025.107515 3.1.3 |
| I2 | **Prior-vs-evidence 분해.** diffusion guidance 강도와 무작위 뇌 입력 기준선으로 "출력 정서 중 뇌 증거 몫과 생성 prior 몫"을 분리한다. 정서 구성 이론의 "사전 지식 + 감각 증거" 구도를 계산적으로 흉내 내는 측정 틀이 된다 | 생성 모델 평가 → 정서 이론 | doi:10.1126/sciadv.adw1464 Discussion 열한째(출력은 뇌 정보와 도구 prior의 혼합), doi:10.1016/j.neunet.2025.107515 2.2.5 |
| I3 | **회상 재활성 지표를 침습적 기억 연구의 계산 바이오마커로.** 같은 클립의 지각-회상 정서 재활성과 vividness의 관계를 정상군에서 정량화해 PTSD 등 연구의 기준선을 만든다. 우리 데이터에는 임상군이 없어 기준선 단계까지만 가능 | 뇌 해독 → 계산정신의학 | arXiv:2506.06898 5.1, doi:10.3758/s13423-017-1313-9 Possible Clinical Relevance |
| I4 | **정서 영역 선호 자극 합성의 응용.** 편도체, 섬엽 encoding model 기반 합성 이미지를 노출 치료 자극 설계나 미디어 정서 평가에 쓴다. 윤리적 검토가 선행되어야 하고 in-silico 예측과 실제 반응을 구분해야 한다 | 신경과학 → 응용 심리학 | doi:10.1523/JNEUROSCI.1436-24.2025, arXiv:2306.03089 |
| I5 | **Decoder-as-observer 분석.** 2단계(뇌 → feature → 출력) 해독 구조로 정보 손실 지점을 특정하는 Mind captioning의 설계를 정서에 적용해, 영역별로 "정서 정보가 존재하는가"와 "선형 판독 가능한가"를 분리한다 | 시각 과학의 ideal observer → 정서 | doi:10.1126/sciadv.adw1464 Discussion 둘째(2단계 설계로 정보 손실 위치 특정) |
| I6 | **Anti-collapse 분할의 표준화.** 정서 데이터셋에서 정서 범주, 원본 영상 단위로 학습-테스트를 분리하는 분할을 공개 표준으로 만든다 | ML 평가 방법론 → Affective Neuroscience 방법론 | doi:10.1016/j.neunet.2025.107515 3.1.1 |
| I7 | **양식 무관(modality-agnostic) 정서 decoder.** 영상과 텍스트/오디오 이야기에서 같은 정서 상태를 해독하는 decoder로 양식 불변 정서 표상을 찾는다(Spacetop alignvideo vs narratives) | 시각-언어 해독 → 다감각 정서 | doi:10.7554/eLife.107933.2 [초록] |

---

## 4. 기존 Affective Neuroscience와 예상 밖으로 연결될 수 있는 개념

1. **Output dimension collapse ↔ 범주 정서 논쟁.** Shirakawa 2025(doi:10.1016/j.neunet.2025.107515, 2.2.1)는 학습 자료가 군집화되어 있으면 예측 가능한 출력 차원이 붕괴해 "분류"가 "재구성"처럼 보인다고 보였다. C&K 비디오는 범주를 잘 유발하도록 수집된 군집 표본이다. 같은 통계적 기제가 "정서가 범주적으로 표상된다"는 결론을 부분적으로 만들 수 있다. Westlin 2025(arXiv:2507.00320)의 재현 실패 보고와 Horikawa 2020의 범주 결론 사이 논쟁을 ML 평가 병리의 언어로 다시 쓸 수 있다. 검증 방법은 정서 범주 hold-out zero-shot(R3).
2. **생성 prior의 환각 ↔ 정서의 예측적 구성.** 재구성은 약한 뇌 증거에 강한 생성 prior를 더한 사후 추정이다. 구성주의 정서 이론도 감각 증거와 개념 지식의 결합을 말한다. guidance 강도를 바꾸며 "정서 판단이 prior에 얼마나 의존하는가"를 재는 측정은, 사람의 정서 지각에서 맥락 prior의 비중을 재는 실험과 같은 구조다(I2).
3. **기억 재활성의 계층 역전 ↔ 정서의 top-down 주입.** Favila 2022(doi:10.1038/s41467-022-33161-8)는 기억 신호가 지각과 달리 계층 전체에서 정밀도가 일정하다는 "feedback 서명"을 보였다. EmoNet 논문(Discussion 일곱째)은 vmPFC, 편도체에서 시각피질로의 feedback이 정서 스키마를 갱신할 수 있다고 했다. 지각 중 시각피질의 정서 관련 성분이 feedforward 서명인지 feedback 서명인지를 회상 조건과 비교해 판별할 수 있다.
4. **시각 표상의 언어 정렬 ↔ 정서 개념 지식.** Doerig 2025(doi:10.1038/s42256-025-01072-0)는 고차 시각피질이 캡션 LLM embedding으로 수렴한다고 했다. 중립 지시 캡션(MindCaptioning)의 언어 통계로 환원되는 정서 정보와 그렇지 않은 정서 정보를 나누면, 정서 지각에서 개념, 언어의 역할에 대한 구성주의 주장을 시각 해독의 언어로 검증할 수 있다(R6).
5. **OTC의 행동 지향 압축 ↔ 재구성 모델의 정보 병목.** Abdel-Ghaffar 2024(doi:10.1038/s41467-024-49073-8)는 OTC 튜닝이 이미지 feature보다 행동 반응을 더 잘 예측한다고 했다. 재구성 bottleneck(CLIP latent)이 버리는 정보와 OTC가 버리는 정보가 같은지 비교하면, "정서는 행동 관련 압축의 부산물인가"를 information bottleneck 관점에서 물을 수 있다.

---

## 5. 새 Sub-axis 또는 하위 연구 방향

| ID | 이름 | 소속 Axis | 연결 Axis | 독립 Axis 필요 여부 | 근거 |
|---|---|---|---|---|---|
| S1 | **Affective Fidelity of Generative Decoding**: 재구성, 캡션 출력의 정서 충실도와 손실 원천(입력 영역, 목표 공간, 생성 prior, 주석) 분해 | G | L, T, R | 불필요 | arXiv:2403.11207, arXiv:2605.16739, doi:10.1126/sciadv.adw1464 |
| S2 | **Perception-to-Imagery Affect Cross-decoding**: 지각 학습 decoder로 회상, 심상 중 정서 재활성을 해독 | G (외부 분야 Memory and Mental Imagery와 결합) | D, E, A | **조건부 필요.** 지각 유발 정서와 내부 생성 정서의 구분은 A, B, D 어디에도 깔끔히 들어가지 않는다. 조합 단계에서 외부 분야를 Axis처럼 세려면 "U: Internally Generated Experience (Memory, Imagery, Recall)" 독립 Axis를 두는 것을 제안 | doi:10.1126/sciadv.adw1464, arXiv:2506.06898, doi:10.3758/s13423-017-1313-9 |
| S3 | **Stimulus Affect Coverage and Sampling Structure**: 학습 자극 분포의 정서 범위(NSD 중립)와 군집 구조(C&K 범주 군집)가 모델 prior와 decoding 결론에 주는 영향 | B | S, Q, T | 불필요 | doi:10.1016/j.neunet.2025.107515, arXiv:2605.17198 3.3 |
| S4 | **Shared vs Private Decoding Latents for Affect**: 교차 피험자 공유 latent와 개인 잔차의 정서 정보 배분 | G | O, F, Q | 불필요 | arXiv:2403.11207, arXiv:2510.25976, arXiv:2507.00320 |
| S5 | **Affect-preferring Stimulus Synthesis**: 정서 관련 영역 encoding model 기반 선호 자극 합성과 인간 검증 | L (B와 교차 참조) | E, H, P | 불필요 | doi:10.1523/JNEUROSCI.1436-24.2025, arXiv:2306.03089 |
| S6 | **Annotation Instruction as Stimulus Descriptor**: 같은 자극에 대한 중립 지시 캡션 vs 정서 지시 캡션이 정의하는 서로 다른 자극 표상 변수 | B | C, Q, I | 불필요 | doi:10.1126/sciadv.adw1464 Discussion 여덟째, arXiv:2605.16739 |

---

## 6. Discussion-to-Research chains

형식: Original Finding → Unresolved Question → Technological Development → New Dataset / Model Combination → New Research Question. 각 단계에 근거 ID와 원문 위치를 단다.

### R1. 재구성의 정서 충실도 격차와 비시각 영역의 회복

* **Original Finding:** MindEye2는 nsdgeneral voxel만으로 OpenCLIP bigG latent를 해독해 SDXL로 재구성한다(arXiv:2403.11207, 2절, Appendix A.2). Brain-Diffuser에서 범주 선택 영역은 CLIP feature, 초기 시각영역은 VDVAE feature에 더 정보적이다(doi:10.1038/s41598-023-42891-8, Results "Which brain regions are used?").
* **Unresolved Question:** Brain-Diffuser는 더 넓은 영역이나 전뇌 입력을 미래 과제로 남겼다(Discussion 넷째 단락). EmoMind는 뇌-텍스트 시스템이 정서를 버린다고 지적했고(arXiv:2605.16739, Abstract), Mind captioning은 주석 지시 때문에 정서가 반영되지 않았다고 했다(doi:10.1126/sciadv.adw1464, Discussion 여덟째 단락). 재구성에 정서가 얼마나 남고, 무엇이 손실을 만드는지는 미해결이다.
* **Technological Development:** 전뇌 foundation model 해독이 DMN, dorsal attention 정보를 쓴다(arXiv:2411.07121, 3 Discussion 첫째 단락). Brain-IT는 1시간 데이터로 새 피험자에 적응한다(arXiv:2510.25976, 5.3, 7 Discussion 셋째 단락). C&K와 겹치지 않는 정서 평가기 학습 자료가 있다(arXiv:2307.07961, Abstract, 6 Conclusion).
* **New Dataset / Model Combination:** Horikawa 5명(보유) + 가능하면 MindCaptioning 6명. 원 비디오 프레임, C&K 34/14 규범 평정. 입력 3단계(시각피질 ROI / + 해부학적 사전 정의 편도체, 섬엽, OFC, vmPFC / 전뇌 parcel) x 해독 목표(CLIP image, CLIP text, 저수준) x Brain-Diffuser식 재학습. 평가: (a) 의미 충실도(원 프레임과 CLIP 유사도, 2-way identification), (b) 정서 충실도(EmoSet 학습 분류기, CLIP zero-shot 정서 프롬프트, 소규모 신규 인간 평정), (c) 원 클립 C&K 평정과의 대응.
* **New Research Question:** 시각피질만으로 재구성한 이미지는 원 자극 대비 정서 정보를 얼마나 보존하는가. 의미 충실도를 통제한 뒤에도 피질하, 변연계, 전두 입력을 추가할 때만 회복되는 정서 성분이 있는가. 있다면 그 성분은 arousal, valence, 특정 범주 중 어디에 집중되는가.
* **반증 조건:** 추가 영역으로 얻는 정서 이득이 의미 이득으로 완전히 설명되면(잔차 이득 0) "재구성 가능한 정서 정보는 시각-의미 정보로 환원된다"를 채택하고 비시각 기여 가설은 기각한다.
* **최소 파일럿:** 재구성 이전에 latent 수준에서 먼저 확인한다. figshare 전처리본으로 원 프레임 CLIP embedding을 ROI 조합별 ridge로 해독하고, 해독 embedding과 원 embedding의 정서 프롬프트 점수 상관을 캡션 유사도 통제 후 비교한다(계산량: ridge 수준).
* **안전장치:** EmoNet 평가기 금지(오염), 원본 영상 단위 그룹 분할, shuffled-fMRI 기준선(L6), ROI는 해부학적으로 사전 정의(순환 추론 방지), 다중 비교 보정, 평가기 간 불일치 보고. 결과는 P/N 수준 정보로만 해석(0.3절 L1).
* **G1:** 필요(보유). **overlap:** EmoViS (정서 표상의 감각-의미 기원 질문과 부분 겹침).

### R2. 같은 정서 클립의 회상에서 정서 재활성: 정서 우위 회상과 NEVER 검증

* **Original Finding:** 지각으로 학습한 semantic decoder가 회상 imagery에서도 내용을 기술한다(doi:10.1126/sciadv.adw1464, Results "Generating recalled content descriptions"; Discussion 둘째 단락: semantic feature가 visual feature보다 imagery 일반화가 좋음). imagery는 위계 feature를 점진적으로 동원하는 top-down 지각이다(doi:10.1038/ncomms15037, Discussion 넷째 단락).
* **Unresolved Question:** EmoNet 논문은 imagery가 시각피질 정서 코드를 활성할 수 있다고 제안만 했다(doi:10.1126/sciadv.aaw4358, Discussion 일곱째 단락). 비공간 feature의 지각-기억 차이는 encoding model 부족으로 미해결이다(doi:10.1038/s41467-022-33161-8, Discussion 셋째 단락). NEVER 모델은 부정 정서가가 감각 재현을 강화하고 그것이 생생함과 연결된다고 예측하지만 검증이 남아 있다(doi:10.3758/s13423-017-1313-9, "Description of Model", Future Directions 첫째 단락).
* **Technological Development:** 지각 학습 decoder의 imagery 일반화에는 선형, 저차원, 텍스트 guidance가 유리하다(arXiv:2506.06898, 5 Discussion 둘째 단락; arXiv:2605.17198, 3.1).
* **New Dataset / Model Combination:** MindCaptioning 회상 데이터(72클립 x 5회 x 6명, 시행별 vividness) + 같은 클립의 지각 데이터(MindCaptioning 5회 반복, Horikawa 2020 1회) + C&K 34/14 규범 평정. decoder 3종을 같은 지각 데이터로 학습: 정서(34/14 규범), 의미(중립 캡션 LM feature), 시각(저수준 DNN feature). 회상 데이터에 교차 적용.
* **New Research Question:** 같은 클립을 회상할 때 지각 학습 decoder로 해독되는 정서 정보는 의미, 시각 세부 정보보다 상대적으로 더 보존되는가(정서 우위 회상 가설). 그 보존은 규범 valence가 부정인 클립에서 더 크고 시행별 vividness와 연동되는가(NEVER). 재활성은 시각피질과 섬엽, vmPFC 중 어디에서 일어나는가.
* **반증 조건:** 정서 정보의 지각 대비 보존 비율이 의미 정보 보존 비율 이하이면 정서 우위 가설 기각. valence와 보존의 관계가 arousal 통제 후 사라지면 NEVER의 정서가 특이 예측 기각.
* **교란과 대응:** (1) 회상 직전 텍스트 cue(정서 중립 지시 캡션이지만 의미 단서 제공): 준비 구간을 별도 모델링. (2) 회상 직후 같은 비디오가 제시되어 HRF가 겹칠 수 있다(원 논문은 4 s shift 후 블록 평균): 회상 창 끝부분 절단, deconvolution, 다음 비디오 onset 회귀. (3) 72클립의 정서 분포 미확인: 검정력 사전 계산. (4) 회상에서 해독된 정서는 경험이 아니라 정서 지식일 수 있다(0.3절 L5). (5) S1 사전 노출.
* **G1:** 필요(C&K 비디오 보유, MindCaptioning 데이터 확보 필요). **overlap:** 없음(확인 범위 내).

### R3. 정서 범주 hold-out 분할로 본 조합적 정서 표상

* **Original Finding:** NSD 재구성의 상당 부분은 학습-테스트 의미 군집 중복과 output dimension collapse로 생긴 분류와 환각이다(doi:10.1016/j.neunet.2025.107515, 2.2.1, 3 Discussion 첫째 단락). 계층 feature 공간을 거치면 학습하지 않은 물체 범주를 zero-shot 식별할 수 있다(doi:10.1038/ncomms15037, Discussion 첫째 단락).
* **Unresolved Question:** Shirakawa는 분할 재설계를 권고했다(3 Discussion 다섯째 단락, 3.1.1). Westlin 2025는 개인 BOLD 군집이 규범 범주와 거의 대응하지 않았고 이론 간 직접 비교가 필요하다고 했다(arXiv:2507.00320, Discussion 셋째, 여섯째 단락). 정서 decoding이 범주 분류인지 조합적 표상인지 가리는 검증은 없다.
* **Technological Development:** 정서 공간을 CLIP 공간에 정렬하는 방법(arXiv:2401.04608, 3절 방법, Limitations), 연속 34차원 정서 벡터 해독(arXiv:2605.16739, 3.1).
* **New Dataset / Model Combination:** Horikawa(+ MindCaptioning). 분할: C&K 우세 범주 군집 단위와 원본 영상 단위로 묶은 leave-one-emotion-cluster-out. 해독 목표: (a) 34차원 규범 profile, (b) 범주 이름과 정의 문장의 텍스트 embedding, (c) 14 affective dimension. 시각-의미 통제로 중립 캡션 embedding을 함께 해독.
* **New Research Question:** 학습에서 완전히 뺀 정서 범주의 클립을, 다른 범주로 학습한 decoder가 연속 정서 공간이나 언어 공간을 통해 식별할 수 있는가. 영역별로 어떤 표상은 조합적으로 일반화하고 어떤 표상은 군집 분류에 머무는가.
* **해석 범위:** zero-shot 성공은 연속 공간 안에서 범주가 공유 성분으로 위치한다는 증거, 범주 내 정확도는 높고 zero-shot은 실패하면 군집 특이 부호화 또는 표본 군집 인공물의 증거다. 어느 쪽도 특정 정서 이론을 단독으로 판정하지는 않으며 "분석 가정 민감도 시험"으로 보고한다.
* **G1:** (a)(b)(c) 해독 자체는 불필요, 의미 통제 feature는 필요(보유). **overlap:** EmoBrain (34차원 정서 profile, cross-subject decoding과 부분 겹침).

### R4. 정서 유발 영상으로 학습한 정서 영역 encoding model의 선호 자극 합성

* **Original Finding:** 합성 fMRI로 ROI-optimal 이미지를 만들 수 있다(doi:10.1038/s41598-023-42891-8, Results "ROI-optimal stimuli"; arXiv:2403.11207, Appendix A.14). EmoNet feature 기반 편도체 하위영역 encoding model로 하위영역별 합성 자극이 저수준 속성에서 구분된다(doi:10.1523/JNEUROSCI.1436-24.2025, Results, Discussion 여섯째 단락).
* **Unresolved Question:** 편도체 모델은 영화 한 편으로 학습되어 정서 범위가 제한되고 다른 자극으로의 일반화가 필요하다(doi:10.1523/JNEUROSCI.1436-24.2025, Discussion 여덟째 단락). 합성 이미지의 실제 검증과 새 ROI 적용은 미래 과제다(arXiv:2306.03089, Limitations and Future Work). 스키마 adversarial 이미지의 인간 경험 효과도 미평가다(doi:10.1126/sciadv.aaw4358, Discussion 여덟째 단락). 덜 알려진 영역의 ROI-optimal 탐색이 권고되었다(doi:10.1016/j.neunet.2025.107515, 3 Discussion 둘째 단락).
* **Technological Development:** encoder gradient로 diffusion을 유도하는 BrainDiVE(arXiv:2306.03089, 방법).
* **New Dataset / Model Combination:** Horikawa 2,181클립으로 편도체 하위영역, 섬엽, vmPFC, OFC voxel encoding model 학습(feature는 C&K 비노출 모델 사용). noise ceiling은 MindCaptioning 72클립 반복으로 추정. BrainDiVE로 영역별 선호 이미지 합성. 평가: 소규모 온라인 규범 평정(신규 수집), EmoSet 평가기, 저수준 속성(색, 공간주파수). NSD 학습 encoder로 교차 예측.
* **New Research Question:** 정서 유발 영상으로 학습한 편도체, 섬엽, vmPFC encoding model이 선호하는 합성 이미지는 인간 규범 정서 공간에서 영역마다 어디에 놓이는가. 그 선호는 저수준 속성으로 환원되는가, 의미 범주로 환원되는가, 둘 다 아닌가. 학습 자극 집합(영화 한 편 vs C&K 2,181클립)에 따라 선호가 바뀌는가.
* **해석 범위:** in-silico 예측이다. 모델 선호가 곧 영역 기능은 아니며, 확증에는 합성 자극에 대한 새 fMRI가 필요하다(CLAUDE.md 6절 in-silico vs observed). 3T에서 편도체 encoding 정확도가 낮을 수 있다.
* **G1:** 필요(보유). **overlap:** 없음(Emo-FilM으로 확장 시 "Emo-FilM 연구"와 방법 일부 겹침).

### R5. 공유 latent와 개인 잔차: 규범 정서와 경험 정서의 분리 시도

* **Original Finding:** 공유 자극 없이도 피험자별 선형 사상으로 공유 latent에 정렬할 수 있다(arXiv:2403.11207, 2.1). 새 피험자 적응을 voxel embedding만으로 할 수 있다(arXiv:2510.25976, 5.3).
* **Unresolved Question:** 개인별 BOLD 구조는 같은 클립을 봐도 고유하며 개인 자기보고가 필요하다(arXiv:2507.00320, Discussion 둘째, 여덟째 단락). EmoMind의 개인 차이 해석은 본인 보고 없이 이루어졌다(arXiv:2605.16739, 5 Discussion 첫째 단락). MIRAGE도 개인 고유 imagery는 해독한다고 주장하지 않는다(arXiv:2605.17198, 3.2).
* **Technological Development:** 공유-개인 사상 구조(arXiv:2403.11207; arXiv:2510.25976), 피험자 불변 표상 학습(arXiv:2404.07850, 3절 방법).
* **New Dataset / Model Combination:** Horikawa 5명 + MindCaptioning 6명(같은 2,180클립)으로 공유 정서 latent 학습. Spacetop alignvideo(모든 참가자가 같은 영상, 본인 7차원 평정)에서 공유 latent에 정렬 후 개인 잔차 계산. 규범 대리는 해당 참가자를 뺀 나머지 참가자 평균.
* **New Research Question:** 공유 latent로 설명되지 않는 개인 잔차 성분이 그 참가자의 본인 평정이 집단 평균에서 벗어나는 정도를 예측하는가. 즉 공유 성분은 규범 정서(N), 개인 성분은 경험 정서(X)의 신경 대응물로 기능하는가.
* **반증 조건:** 개인 잔차가 본인 평정 편차를 예측하지 못하고(영상 단위 순열 검정), 공유 성분만으로 본인 평정 예측이 포화되면 "개인 경험 성분" 가설 기각.
* **교란:** Spacetop 평정 약 51% 결측, 영상 49개, 소리 있음(Horikawa는 무음, 양식 차이), 영상 직후 평정 구간과 HRF 겹침, 평정 행위의 운동 신호.
* **G1:** 필요(보유). **overlap:** EmoBrain (cross-subject emotion decoding과 부분 겹침).

### R6. 정서 배제 인간 캡션을 통제한 뒤 남는 정서 분산

* **Original Finding:** 고차 시각피질은 캡션 LLM embedding과 정렬된다(doi:10.1038/s42256-025-01072-0, Discussion 첫째 단락). Mind captioning의 캡션은 시각 내용만 쓰도록 지시되어 정서가 거의 들어가지 않았다(doi:10.1126/sciadv.adw1464, Materials and Methods "Caption annotation", Discussion 여덟째 단락).
* **Unresolved Question:** 시각 처리의 다른 측면이 LLM embedding으로 포착되는지는 미평가다(doi:10.1038/s42256-025-01072-0, Discussion 둘째 단락). OTC 연구도 의미와 mid-level 구조 분리를 과제로 남겼다(doi:10.1038/s41467-024-49073-8, Discussion 넷째 단락). EmoNet 논문은 정서 관련 시각 feature가 사람이 이름 붙인 feature로 환원되지 않는다고 했다(doi:10.1126/sciadv.aaw4358, Discussion 둘째 단락).
* **Technological Development:** LLM embedding encoding(doi:10.1038/s42256-025-01072-0), 정서 조건 캡션 재작성(arXiv:2605.16739, 3.2).
* **New Dataset / Model Combination:** Horikawa + MindCaptioning fMRI, MindCaptioning 인간 중립 캡션 20개/클립(figshare 포함 여부 확인 필요), C&K 34/14 규범 평정, 정서 언어로 재작성한 캡션(AI 생성, 별도 표기).
* **New Research Question:** 정서를 쓰지 말라는 지시 아래 인간이 쓴 중립 캡션의 LLM embedding을 통제한 뒤에도 각 영역에 남는 C&K 규범 정서의 고유 설명 분산은 얼마인가. 그 잔차는 같은 캡션을 정서 언어로 재작성한 embedding으로 회복되는가, 아니면 언어로 회복되지 않는 시각 정서 성분이 남는가.
* **해석 범위:** "중립"은 지시의 속성이지 내용의 속성이 아니다(장례식 장면 캡션은 내용상 정서를 함의). 따라서 결과는 "언어화된 장면 의미가 함의하는 정서"와 "그 외 정서"의 분리이며, 시각-의미-정서 공선성은 variance partitioning과 함께 보고한다.
* **G1:** 캡션과 평정만으로 encoding 가능(G1 불필요), 시각 feature 통제에는 필요(보유). **overlap:** EmoViS (정서 표상의 감각-의미 기원 질문과 직접 겹침).

---

## 7. 담당 Axis 확장 제안

### Axis B (Perceptual & Stimulus Representation)
* **추가:** S3 Stimulus Affect Coverage and Sampling Structure, S6 Annotation Instruction as Stimulus Descriptor, "Internally Generated Stimulus Content (recalled, imagined)", "Synthetic / Generated Stimuli as Probes"(S5와 교차 참조).
* **주석:** "Audio / Music / Speech Features"는 Horikawa(무음), NSD(정지 이미지)에서 다룰 수 없고 Emo-FilM, Spacetop에서만 가능하다는 데이터 제약을 Sub-axis 옆에 표시할 것을 제안한다.

### Axis G (Decoding)
* **추가:** S1 Affective Fidelity of Generative Decoding, S2 Perception-to-Imagery Affect Cross-decoding, S4 Shared vs Private Decoding Latents, "Held-out-category (anti-collapse) Zero-shot Emotion Decoding"(R3), "Region-additive Decoding (ROI 확장, 제거에 따른 정보 증분)"(R1), "Affective Captioning (정서 채널이 있는 Neural-to-Text)"(EmoMind).
* **재분류:** "Generative Reconstruction"을 (a) 측정으로서의 재구성(정량 평가, 분할과 기준선 필수)과 (b) 시각화로서의 재구성(가설 생성)으로 나눈다. 근거: Shirakawa 2025, 3 Discussion 셋째 단락(재구성은 zero-shot이 아니어도 해독 내용의 시각화로 유용).
* **표시:** "Emotion Category Decoding"과 "Dimensional Affect Decoding"은 P5 Novelty Constraint상 기준선 항목으로 표시하고, 단독 질문으로는 최종 후보에서 제외하도록 권고한다.
* **삭제 제안:** 없음.

### 새 독립 Axis 제안 (조건부)
* **U: Internally Generated Experience (Memory, Imagery, Recall).** S2를 담는다. 외부 분야 Memory and Mental Imagery가 조합 규칙(P5)에서 "Affective Neuroscience 밖 개념" 역할을 하도록 독립 Axis로 세우는 것을 제안한다. 반대 의견이 있으면 G와 D의 하위로 두어도 된다(데이터는 MindCaptioning 회상, NSD-Imagery뿐이고 정서 imagery 전용 데이터는 없다는 점이 약점).

---

## 8. 검증된 것과 미확인 사항

### 검증됨
* 28편의 존재(식별자 경로)와 23편의 Discussion, Limitations 원문.
* MindCaptioning의 자극이 Cowen & Keltner 2017 비디오(2,180 고유)이고, 72클립 5회 반복, 72클립 회상 imagery와 vividness 평정, 정서 배제 지시 캡션, 공개 경로(논문 Data availability) [본문].
* MindEye2 입력이 nsdgeneral, Brain-IT 입력이 Algonauts 판 시각 관련 40k vertex [본문].
* MindEye2, Brain-IT, NSD-Imagery, MIRAGE 본문에 정서 평가 없음(키워드 검색).
* EmoNet fine-tuning 자료 요청 경로가 Horikawa 비디오 요청 경로와 같음(Jang & Kragel 2025 Data Availability) [본문].
* EmoMind가 MindCaptioning과 Horikawa 2020을 이미 정서 캡션에 사용 [본문].

### 미확인
* ds005191 저장소 파일 구성, 라이선스, 우리 환경 보유 여부. figshare 전처리본에 캡션과 회상 시행별 vividness가 들어 있는지.
* Horikawa 2020과 MindCaptioning 사이 피험자 중복 여부.
* 72개 테스트 클립의 C&K 정서 분포(R2 검정력).
* 회상 창과 직후 비디오 제시 사이 HRF 겹침의 실제 크기.
* MindEye2, Brain-IT, BrainDiVE, MindBridge 코드와 checkpoint의 라이선스와 실제 다운로드 위치(GitHub, Hugging Face 접근 차단으로 [검색] 수준).
* EmoSet 데이터와 학습 가중치의 공개 조건.
* CLIP, OpenCLIP 학습 자료에 C&K 비디오(GIF)나 COCO가 포함됐는지(사전학습 오염).
* NSD-Imagery 접근 조건(NSD 웹사이트 안내만 확인).
* VSS 2024 학회 초록(정서 imagery의 시각피질 valence 해독)과 VSS 2025 초록(NSD encoding model 기반 정서 장면 해독)은 검색 결과로만 보았고 literature.jsonl에 넣지 않았다.

---

## 9. 자기 비판과 예상 반론

1. **재구성을 거칠 필요가 있는가.** 정서 공간으로 직접 해독하는 편이 단순하고 통계적으로 강하다. 재구성의 고유 가치는 (a) 손실 원천을 파이프라인 단계별로 분해할 수 있고, (b) 인간 평정으로 외부 검증할 수 있으며, (c) 생성 prior의 정서 편향 자체가 과학적 질문이 된다는 점이다. 그래도 R1의 핵심 결과는 재구성 이전 latent 수준에서 먼저 확인해야 한다.
2. **정서 충실도는 의미 충실도의 부산물일 가능성이 높다.** Stage 1이 기록한 Gao 2025(객체 인식 모델이 정서 판단을 더 잘 예측)와 Doerig 2025가 이를 시사한다. R1, R6은 이것을 귀무가설로 명시했고, 귀무가설이 채택되어도 "재구성 가능한 정서 정보는 의미로 환원된다"는 과학적 결론이 된다.
3. **MindCaptioning은 보유 데이터 밖이다.** R2, R5, R6의 일부는 추가 다운로드에 의존한다. Horikawa만으로 가능한 부분(R1, R3, R4, R6의 시각 통제)을 먼저 설계할 수 있다.
4. **참가자 경험(X)에 닿는 질문은 Spacetop에서만 검증 가능하다.** Horikawa 중심 질문은 P/N 수준 결론에 머문다는 점을 모든 카드에 명시해야 한다.
5. **EmoMind와의 차별성.** EmoMind는 텍스트 출력, 지각 조건, 규범 목표, 개인 차이의 미검증 해석이다. 우리 제안은 이미지 출력의 손실 분해(R1), 회상 조건(R2), 범주 hold-out(R3), 본인 보고와의 대응(R5)으로 구분된다. Round 2에서 다른 에이전트가 EmoMind를 독립적으로 찾았는지 대조할 필요가 있다.
