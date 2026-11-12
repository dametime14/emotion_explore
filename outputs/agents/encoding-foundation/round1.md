# Round 1 (Independent Discovery): encoding-foundation

* 작성: encoding-foundation (Agent 4, Brain Encoding & Foundation Models)
* 기준일: 2026-11-12
* 절차: `reference/protocols.md` P1. 다른 에이전트 폴더는 읽지 않았다.
* 담당 Axis: F (Brain Representation), H (Encoding), S (Generalization & Robustness)
* 문헌 기록: `outputs/agents/encoding-foundation/literature.jsonl` (41편, 전부 식별자 경로로 존재 확인)

## 0. 요약

### 문헌 현황
| 항목 | 수 |
|---|---|
| 기록 논문 | 41 |
| verified (arxiv 24, crossref 16, publisher 1) | 41 |
| 2024~2026년 | 29 |
| Affective Neuroscience 밖 분야(ML 모델, NeuroAI 평가, 마우스 digital twin, 시각 neural control 등) | 24 이상 |
| `discussion_read` = full_text / abstract_only / no | 32 / 6 / 3 |

`no` 3편(arXiv:2206.11417, arXiv:2509.24693, arXiv:2512.11582)은 사전학습 데이터 목록만 확인한 contamination 점검용 기록이다. 확인 경로는 export.arxiv.org API, arxiv.org PDF/HTML 본문, api.crossref.org, pmc.ncbi.nlm.nih.gov(직접 접속 또는 PubMed MCP), proceedings.mlr.press, biorxiv.org, GitHub 공개 저장소(git clone, 코드 실행 안 함)다.

### 핵심 메시지
1. **TRIBE v2의 서지가 확정되었다.** d'Ascoli et al. (2026), arXiv:2605.04326. 공개 checkpoint는 fsaverage5 피질의 '평균 피험자' 예측만 낸다. 논문은 피질하 8,802 voxel도 예측했지만 공개 checkpoint는 피질만이고 피험자별 readout도 없다(README, arXiv:2607.01400 8절). 코드와 가중치는 CC BY-NC 4.0이다.
2. **Contamination(fMRI):** 확인한 모델 중 Horikawa(ds002425), Emo-FilM(ds004892), Spacetop(ds005256)을 사전학습에 쓴 모델은 없다. NSD는 CortexMAE와 Omni-fMRI의 **평가**에만 쓰였다. TRIBE v2 코드에 `Allen2022Bold`라는 study 이름 분기가 있지만 공개 학습 설정에는 들어 있지 않다(미확인으로 둔다).
3. **Contamination(자극):** EmoNet은 Horikawa와 같은 Cowen & Keltner 비디오 2,185개에서 뽑은 프레임으로 학습되었다(doi:10.1126/sciadv.aaw4358 Methods). 따라서 Horikawa에서 EmoNet feature는 학습 자극을 재사용하는 셈이다. TRIBE v2의 feature 추출기(V-JEPA 2, Llama-3.2, Wav2Vec-BERT)가 우리 자극을 학습 중에 봤는지는 미확인이다.
4. **In-silico의 첫 정서 관련 실패 신호.** EmoMind(arXiv:2605.16739)에서 TRIBE v2 합성 뇌는 clip별 정서 정보는 대체로 보존했다. 그러나 clip 간 정서 관계 구조(RSA)는 실측 대비 약 26%만 남았다(rho 0.635에서 0.166). 이 비교는 같은 자극의 실측 fMRI와 짝지은 것이 아니다. 같은 자극으로 짝지은 비교는 아직 아무도 하지 않았다.
5. **자극 구동 encoder는 정서 관련 영역에서 체계적으로 약할 수 있다.** 근거는 네 가지다. TRIBE v2의 피질하 점수는 피질의 1/2~1/3이다. MIRAGE의 개선 폭은 Limbic망에서 가장 작다(arXiv:2605.29850). group encoder는 개인 특이 신호를 평균으로 붕괴시킨다(arXiv:2607.01400). vmPFC 반응은 개인 간에 이질적이다(doi:10.1126/sciadv.abf7129). 이 약점이 noise 때문인지 feature 결핍 때문인지가 핵심 미해결 문제다.
6. **뇌 입력 foundation model(CortexMAE, NeuroSTORM, Brain-JEPA 등)에는 엄밀한 정서 benchmark가 없다.** 유일한 정서 회귀(Omni-fMRI, StudyForrest)는 시간 블록을 무작위로 분할했고, 라벨은 portrayed emotion 주석으로 보인다. NeuroSTORM의 "Emotion" 93%는 HCP Hariri 과제 상태 분류다.

---

## 1. 중요한 미해결 문제

| # | 미해결 문제 | 왜 아직 미해결인가 | 근거 논문 ID |
|---|---|---|---|
| U1 | **In-silico 예측은 정서 표상의 '관계 기하'를 재현하는가.** 점별 예측(clip별 정서 정보)과 관계 구조(clip 간 거리)는 다른 문제다 | EmoMind는 해리를 보였다. 그러나 MC 실측 fMRI와 Emo-FilM 자극의 합성 반응을 비교했을 뿐, 같은 자극의 실측 fMRI와 비교하지 않았다. TRIBE v2 논문의 in-silico 검증은 시각 범주와 언어 localizer에 한정되고, 정서 관련 대비는 EmotionalPain 문장 하나로 질적 수준이다 | arXiv:2605.16739, arXiv:2605.04326, arXiv:2609.15685 |
| U2 | **'Limbic 맹점'은 잡음인가, feature 결핍인가.** 편도체, 섬엽, vmPFC, 선조체에서 자극 구동 encoder 성능이 낮은 이유 | TRIBE v2 Discussion은 내수용과 체성감각 입력 부재, 수동 관찰자 가정을 한계로 든다. MIRAGE는 Limbic망에서 개선이 가장 작다. 공개 TRIBE v2에는 측좌핵이 구조적으로 없다. Koide-Majima는 편도체 효과가 작다고 보고했다. Jang & Kragel은 습관화, 학습, 비시각 모달 의존 반응은 예측할 수 없다고 적었다. 그런데 noise ceiling으로 정규화한 Limbic 성능과 생리 변수의 추가 설명력을 같은 데이터에서 함께 본 연구는 없다 | arXiv:2605.04326, arXiv:2605.29850, arXiv:2607.01400, doi:10.1016/j.neuroimage.2020.117258, doi:10.1523/JNEUROSCI.1436-24.2025 |
| U3 | **Group-average 예측의 잔차에 개인 정서 경험이 들어 있는가** | TRIBE v2는 group 반응을 개별 피험자보다 잘 예측한다. 그러나 공개 모델은 개인차를 표현할 수 없다. Chang 2021은 vmPFC 반응이 정렬 후에도 개인 특이적이며 정서 장면에서만 동기화된다고 보였다. Haxby 2020은 정렬 후 남는 개인차가 오히려 더 신뢰할 만하다고 보였다. Horikawa 2020 Limitations는 평정자가 참가자가 아니라는 점을 든다. '관찰 반응 - 자극 구동 예측' 잔차가 본인 보고 편차를 예측하는지는 검증된 적이 없다 | arXiv:2605.04326, arXiv:2607.01400, doi:10.1126/sciadv.abf7129, doi:10.7554/eLife.56601, doi:10.1016/j.isci.2020.101060 |
| U4 | **정서 encoding의 설명적 적절성(explanatory adequacy).** 높은 encoding 정확도는 정서 표상을 입증하지 못한다 | Conwell 2024는 구조가 크게 다른 모델들이 거의 같은 예측력을 보이며, 지표(cRSA vs veRSA)에 따라 결론이 뒤집힌다고 보였다. Han 2023은 정답이 알려진 조건에서도 encoding 지표의 모델 식별력이 약하다고 보였다. Horikawa 2020의 '정서 고유 분산'은 2020년 수준 시각, 의미 feature 기준이다. Koide-Majima는 객관 정보와 정서를 정밀하게 비교하라고 명시적으로 제안했다 | doi:10.1038/s41467-024-53147-y, arXiv:2302.06677, doi:10.1016/j.isci.2020.101060, doi:10.1016/j.neuroimage.2020.117258, doi:10.1038/s41467-024-49073-8 |
| U5 | **뇌 입력 foundation model latent에 정서 구조가 있는가에 대한 누수 통제 benchmark 부재** | Brainmarks에는 정서 과제가 없다. CortexMAE는 trait 예측에서 FC baseline을 넘지 못했다. NeuroSTORM의 "Emotion"은 과제 상태 분류다. Omni-fMRI의 정서 회귀는 같은 영화 시간 블록 무작위 분할(temporal leakage)에 portrayed 라벨로 보인다. 이런 이유로 "latent가 정서를 담는다"는 주장의 근거가 아직 약하다 | arXiv:2510.13768, arXiv:2506.11167, arXiv:2601.23090, doi:10.12688/f1000research.6230.1 |
| U6 | **모델 기반 정서 분석의 contamination과 provenance** | EmoNet은 Horikawa 자극으로 학습되었다. TRIBE v2의 학습 fMRI에는 우리 데이터셋이 없지만 feature backbone의 사전학습 데이터는 미확인이다. Memento10k 클립은 TRIBE v2 학습 데이터(BOLD Moments)의 출처라 in-distribution 효과가 생긴다(arXiv:2607.16292의 데이터셋 의존 반전과 함께 해석해야 한다). OpenNeuro 광범위 사전학습 모델은 2020년부터 공개된 ds002425를 포함할 수 있어 목록 점검이 필요하다 | doi:10.1126/sciadv.aaw4358, arXiv:2605.04326, arXiv:2607.16292, arXiv:2206.11417 |
| U7 | **In-silico 정서 영역 제어와 생성 결과의 생체 검증 공백** | Jang & Kragel의 편도체 하위영역 합성 자극, TRIBE v2 feature visualization의 super-stimulus, TRIBE 예측 '정서 ROI'로 감독한 정서 편집, emulator 내부의 VAD 역추정, 생성 음악의 in-silico 정서 효과 모두 관찰 fMRI 검증이 없다. 시각 영역에서는 Gifford RNC, Ratan Murty, Bashivan이 생체 검증까지 닫았다 | doi:10.1523/JNEUROSCI.1436-24.2025, arXiv:2605.13904, arXiv:2610.13558, arXiv:2604.23865, arXiv:2604.04025, doi:10.1038/s41562-025-02252-z, doi:10.1038/s41467-021-25409-6 |
| U8 | **정서 표상의 초감각성(supramodality) 중 자극으로 계산 가능한 부분** | Lettieri 2024는 vmPFC의 모달리티 독립 범주 부호를 감각 박탈 집단으로 보였다. Jang & Kragel은 편도체 부호가 시각 특이적인지 영역 일반적인지 미해결이라고 적었다. TRIBE v2 modality dropout은 감각 박탈의 in-silico 유사물을 제공하지만 정서에 적용된 적은 없다 | doi:10.1126/sciadv.adk6840, doi:10.1523/JNEUROSCI.1436-24.2025, arXiv:2605.04326 |

---

## 2. 주목할 모델과 방법론

### 2.1 모델 사양표

공개 여부와 라이선스는 논문 본문과 GitHub 저장소(LICENSE, README)로 확인했다. Hugging Face 페이지는 직접 열지 않았다(README 링크 기준).

| 모델 | 유형 | Pretrained weights | 라이선스 | Input | Output | 학습 목표 | 학습 데이터 |
|---|---|---|---|---|---|---|---|
| **TRIBE v2** (arXiv:2605.04326) | 자극→뇌 encoder | 공개(HF facebook/tribev2, README). 평균 피험자, 피질만 | CC BY-NC 4.0 (코드, 저장소 LICENSE). 백본: V-JEPA 2 CC-BY-NC 4.0, Llama 3.2 Community License, Wav2Vec-BERT 2.0 MIT (arXiv:2605.29850 표 3) | 원시 영상, 오디오, 텍스트(텍스트는 TTS 후 단어 시각 추출). 2 Hz feature, 4 s 영상 창 | fsaverage5 20,484 vertex 시계열(5 s 앞당김). 논문은 피질하 8,802 voxel 포함 | 실측 BOLD와의 MSE, subject dropout, modality dropout | Wen2017, LeBel2023, BOLD Moments, CNeuroMod(25명, 약 446 h). 테스트: Narratives, Le Petit Prince, NNDb, HCP 7T movie |
| **TRIBE v1** (arXiv:2507.22229) | 자극→뇌 encoder | 코드 공개(algonauts-2025 저장소, 본 에이전트는 미열람) | 미확인 | 위와 유사 | Schaefer 1000 parcel | MSE | CNeuroMod 4명 |
| **MIRAGE** (arXiv:2605.29850) | 자극→뇌 encoder | HF epfl-neuroai/mirage(논문 링크) | 모델 미확인. 백본 Qwen3-Omni Apache-2.0 | Qwen3-Omni 48층 feature | Schaefer 1000 parcel | MSE계 회귀 | CNeuroMod 4명 |
| **CortexMAE** (arXiv:2510.13768) | 뇌 입력 자기지도 | 공개(HF medarc/CortexMAE, 50개 이상 변형) | 코드 Apache-2.0, 가중치 CC BY-NC 4.0 | fsLR 91k CIFTI를 flat map 224x560으로(기본), Schaefer-400, MNI cortex volume. 16프레임(TR 1 s) | patch embedding(latent), MAE 재구성 | MAE-st | HCP-YA 980명 2,058 h (rest, 7개 task: EMOTION 포함, movie) |
| **NeuroSTORM** (arXiv:2506.11167) | 뇌 입력 자기지도 | 공개(HF, README) | LICENSE 파일 Apache-2.0, README 배지 MIT (불일치) | 4D volume | latent, prompt tuning | MAE + STRD | UKB, ABCD, HCP-YA/A/D (28.65M 프레임) |
| **SwiFT** (arXiv:2307.05916) | 뇌 입력 | 저장소에 contrastive 사전학습 ckpt | Apache-2.0 | 4D volume(MNI, 20프레임 창) | latent | contrastive | UKB, HCP, ABCD |
| **Brain-JEPA** (arXiv:2409.19407) | 뇌 입력 | Google Drive(README) | 저장소 LICENSE 없음 (미확인) | 450 ROI(Schaefer-400+Tian-50) x 160 시점 | latent | JEPA | UKB 휴지기 |
| **BrainLM** (doi:10.1101/2023.09.12.557460) | 뇌 입력 | HF 111M, 650M | CC BY-NC-ND 4.0 | A424 parcel x 200 시점 | latent, 미래 상태 | MAE | UKB + HCP 6,700 h |
| **Omni-fMRI** (arXiv:2601.23090) | 뇌 입력 | 미확인(실험 로그 공개 언급) | 미확인 | atlas-free 4D 96^3 x 40 | latent | 자기지도(동적 patch) | UKB, AOMIC, CHCP, ISYB |
| **Brain-Mamba** (pmlr-v248-behrouz24a) | 뇌 신호 encoder 구조 | 논문에 공개 경로 없음(미확인) | 미확인 | parcel/voxel 다변량 시계열 + FC 그래프 | 분류, 이상탐지 표상 | 상호정보 사전학습 | THINGS fMRI 3명, HCP, ADHD, EEG, MEG |
| **EmoNet** (doi:10.1126/sciadv.aaw4358) | 자극→정서 CNN (encoding feature로 사용) | 공개 여부 본 에이전트 미확인 | 미확인 | 이미지 프레임 | 20개 정서 범주 | 지도학습 | **Cowen & Keltner 비디오 2,185개 프레임 = Horikawa 자극** |
| **Relational neural control** (doi:10.1038/s41562-025-02252-z) | 방법 | (NSD encoding model) | - | encoding model 예측 | 영역 쌍 정렬/분리 자극 | 탐색 + in vivo 검증 | NSD |
| **Matched-control audit** (arXiv:2607.16292) | 방법 | - | - | 예측 피질 vs 그 백본 feature | 같은 probe 성능 차이 | - | - |

### 2.2 우리 데이터셋 Contamination 점검

| 모델 | Horikawa (ds002425) | Emo-FilM (ds004892) | Spacetop (ds005256) | NSD | 근거 |
|---|---|---|---|---|---|
| TRIBE v2 (fMRI 학습/테스트) | 없음 | 없음 | 없음 | 학습 설정에 없음. 코드에 `Allen2022Bold` 분기 있음(내부 실험 가능성, 미확인) | 논문 5.7절, `grids/defaults.py` |
| TRIBE v2 feature 백본(V-JEPA 2 등) | 미확인 (인터넷 출처 영상) | 미확인 (LIRIS-ACCEDE CC 영화) | 미확인 (제3자 영상) | 미확인 (COCO는 대형 VLM 학습 분포에 흔함) | 백본 사전학습 목록은 이번 라운드에서 확인하지 않음 |
| CortexMAE | 없음 | 없음 | 없음 | 사전학습에는 없음. OOD 검증과 COCO24 benchmark에 사용 | 논문 3절, 4절 |
| NeuroSTORM | 없음 | 없음 | 없음 | 없음 | 논문 2절 |
| Brain-JEPA, BrainLM, SwiFT, BrainHarmonix, Brain-Semantoks | 없음 | 없음 | 없음 | 없음 | 각 논문 데이터 절 |
| Omni-fMRI | 없음 | 없음 | 없음 | 하위 과제(검색) | 논문 표 2 |
| Thomas 2022 (OpenNeuro 34개) | 없음 | 없음 | 없음 | 없음 | 부록 데이터 목록(ds000003~ds003524) |
| **EmoNet** | **자극 중복 (학습 프레임 출처)** | 없음 | 없음 | 없음 | Methods |
| MindEye2 계열 | 없음 | 없음 | 없음 | **학습 데이터** | 논문 |

결론: fMRI 측면의 직접 오염은 없다. 위험은 **자극 측**에 있다. EmoNet과 Horikawa는 확정된 중복이고, foundation 백본과 네 데이터셋 자극의 중복은 미확인이다. **NSD를 쓰는 encoding/decoding 모델은 NSD 학습 모델과 함께 쓰면 누수**가 생긴다(MindEye2, Gifford RNC encoder 등).

### 2.3 데이터셋별 적용 가능성 (Stage 1 사양 기준)

| 데이터셋 | TRIBE v2 (자극→뇌) | CortexMAE 등 (뇌 입력) | 주의 |
|---|---|---|---|
| Horikawa | 비디오만 입력(무음, 학습 데이터 Wen2017도 무음이라 modality dropout 상황과 같음). 실험 run 순서대로 clip 시퀀스를 만들어 예측 시계열을 얻은 뒤 관찰 데이터와 같은 블록 평균을 적용해야 한다 | 공개 전처리본은 native volume 블록 평균이라 시계열 모델 입력이 아니다. raw BIDS를 fMRIPrep으로 다시 돌려 fsLR 또는 MNI 시계열을 만들어야 한다 | 5명이라 피험자 수준 일반화가 약하다. 반복 제시가 없어 noise ceiling이 없다(대안: 피험자 간 split-half). EmoNet은 contamination |
| Emo-FilM | 영상 + 오디오 + 대사 텍스트(whisperX 단어 시각, TRIBE v2 pipeline 내장) | FSL 전처리본(6 mm smoothing, MNI)이라 flat map 입력에는 재전처리 필요 | 영화 14편이라 leave-one-film-out 14 fold. 관찰 fMRI 30명으로 ISC 기반 ceiling을 낼 수 있다 |
| Spacetop | alignvideo(소리 있음) 직접 입력 | **fsLR 91k CIFTI 제공. CortexMAE flat map에 가장 바로 맞는다** | 정서 평정은 영상 종료 후 1회, 결측 약 51% |
| NSD | 정지 이미지를 정적 영상으로 변환해 입력(arXiv:2606.06345 방식) | fsaverage beta. CortexMAE는 NSD 시계열을 평가에 쓴 적이 있다 | 정서 라벨은 nsdmeadows 100장뿐. NSD 학습 모델은 쓰지 않는다 |

### 2.4 Adaptation 방법과 필요한 데이터 양
* **TRIBE v2.** zero-shot group 예측에는 새 데이터가 필요 없다. 개인 예측은 피험자당 약 1시간 이하 데이터로 1 epoch fine-tuning한다(전체 파라미터 해제, 저랭크 subject block). 공개 checkpoint에는 피험자 head가 없으므로 subject block을 우리가 새로 학습해야 한다.
* **CortexMAE.** 고정 encoder에 attentive probe나 선형 probe를 붙인다. 입력 단위는 16 s clip이다. Brainmarks는 피험자 분리 평가를 쓴다.
* **NeuroSTORM.** prompt tuning(5% 이하 파라미터)을 쓰며 10% 데이터로도 성능이 크게 유지된다고 보고했다(HCP 기준).
* **Brain-Mamba.** 사전학습 가중치가 없어 처음부터 학습해야 한다. 방법론 후보로만 본다.

---

## 3. 다른 분야에서 가져와 적용할 수 있는 연구 아이디어

| # | 아이디어 | 출처 분야와 논문 | 정서 연구로의 적용 | 가능한 데이터 |
|---|---|---|---|---|
| I1 | **Functional barcode를 정서 tuning 예측자로** | 마우스 digital twin: 뉴런별 기능 embedding이 형태와 연결을 예측했다(doi:10.1038/s41586-025-08829-y) | TRIBE v2 readout(vertex별 latent 사상 가중치)을 vertex 'barcode'로 본다. 이것이 Horikawa에서 측정한 vertex별 정서 범주 tuning을 예측하는지 검사한다. 모델 내부 기능 embedding으로 관찰된 정서 선택성을 예측하는 셈이다 | Horikawa, Emo-FilM |
| I2 | **Controversial selection과 relational neural control** | NeuroAI 모델 비교(doi:10.1038/s41467-024-53147-y), 시각 피질 RNC(doi:10.1038/s41562-025-02252-z) | 정서 평정 모델과 시각-의미 foundation feature가 서로 다른 RDM 예측을 하는 clip만 Horikawa 2,181개에서 골라 뇌가 어느 쪽을 따르는지 본다. 편도체 대 FFA/pSTS처럼 영역 쌍을 정렬하거나 분리하는 자극을 기존 자극 풀에서 선택하고, 보류 피험자 실측 반응으로 검증한다 | Horikawa, NSD |
| I3 | **Simulation-based inference의 simulator-to-real gap을 측정 도구로** | SBI(arXiv:2604.23865) | TRIBE v2를 simulator로 두고 정서 매개변수(valence, arousal, 범주) 사후분포를 amortized 추론한다. 이를 관찰 fMRI에 적용하면 사후분포 보정 실패(calibration 이탈)의 영역별 패턴이 '모델이 놓친 정서 정보'의 지도가 된다 | Emo-FilM, Spacetop |
| I4 | **Matched-control audit** | 기억성 예측 감사(arXiv:2607.16292) | 정서 평정 예측에서 TRIBE v2 예측 피질 feature와 그 V-JEPA2 백본을 같은 probe로 비교한다. 예측 피질이 이기면 뇌 공간 투영이 정서 관련 구조를 더한다는 뜻이고, 지면 정서 정보는 백본에 이미 있다는 뜻이다 | Horikawa, Emo-FilM |
| I5 | **Ground-truth system identification으로 분석 pipeline 검증** | 정답 ANN을 표적으로 둔 식별력 검사(arXiv:2302.06677) | TRIBE v2 합성 뇌에 알려진 '정서 신호'(평정 기반 패턴)를 정해진 SNR로 심는다. 그 뒤 우리 decoding, encoding, RSA, variance partitioning pipeline이 이를 회복하는지, 시각-의미 공선성 아래에서 거짓 양성이 나는지 검사한다. 정서 연구의 power analysis와 confound 감사에 쓴다 | 4개 모두(자극 기반) |
| I6 | **고처리량 선택성 검정** | 범주 선택 영역 검정(doi:10.1038/s41467-021-25409-6) | 편도체, vmPFC, 섬엽 encoder가 최고 반응을 예측한 자극 집합이 하나의 정서 범주로 묶이는지, 아니면 시각-의미 feature로 설명되는지 본다. 합성은 하지 않고 기존 자극 screening으로 실측 검증 고리를 유지한다 | NSD 73k, Horikawa |
| I7 | **Encoder 일반화 평가에 정서를 OOD 축으로** (정서 연구에서 NeuroAI로 역수출) | Algonauts OOD 평가(arXiv:2501.00504) | 정서 강도와 범주를 OOD 조건으로 정의해 foundation encoder의 일반화 실패가 정서 내용에 집중되는지 보는 benchmark를 만든다. 결과는 NeuroAI benchmark 쪽에도 기여한다 | Horikawa, Emo-FilM |

---

## 4. 기존 Affective Neuroscience와 예상 밖으로 연결될 수 있는 개념

1. **"예측 잔차 = 평가(appraisal)."** 자극 구동 group encoder의 예측은 '평균 관찰자'의 뇌가 자극만으로 보일 반응이다. 따라서 관찰 반응에서 이를 뺀 잔차는 같은 자극을 개인이 다르게 평가한 결과를 담을 후보다. 이는 Component Process Model의 "같은 사건, 다른 평가"와 연결된다(근거: arXiv:2605.04326 2.3절, doi:10.1126/sciadv.abf7129, doi:10.7554/eLife.56601). 단 잔차에는 측정 잡음과 HRF 개인차도 섞이므로, 신뢰도로 분리해야 한다.
2. **"Modality dropout = in-silico 감각 박탈."** TRIBE v2가 학습에 쓴 modality dropout은 맹, 농 참가자 설계(doi:10.1126/sciadv.adk6840)의 계산적 유사물이다. 영상만 넣은 예측과 소리만 넣은 예측이 관찰된 vmPFC 정서 신호를 각각 얼마나 재현하는지 비교하면, 초감각 정서 부호 중 '자극으로부터 계산 가능한 부분'을 추정할 수 있다.
3. **"Feature visualization의 super-stimulus = 동물행동학의 초정상 자극(supernormal stimulus)."** 최적화된 FFA 자극은 실제 얼굴보다 예측 반응을 약 4배 끌어냈다(arXiv:2605.13904). 정서 영역에 같은 방법을 쓰면 정서적 초정상 자극(귀여움, 위협의 과장)을 얻을 수 있다. 이것이 행동학의 초정상 자극처럼 실제 정서 반응도 과장해서 유발하는지는 경험적 질문이며, computational ethology와 연결된다. 단 생체 검증 전에는 encoder의 성질이다.
4. **"Digital twin = 규범 평정자(normative rater)의 뇌 버전."** Horikawa와 Emo-FilM의 라벨은 별도 평정자의 규범 평정이다. TRIBE v2의 unseen-subject 예측은 '규범적 뇌 반응'이다. 그러면 규범 평정, 규범 뇌(in-silico), 본인 보고, 본인 뇌라는 4자 구조가 생긴다. 이는 Q축(평정 주체)과 F/H축을 잇는 측정 이론 질문이 된다.
5. **"피질 전용 표상 = 측정 불변성(measurement invariance) 문제."** flat map과 fsaverage5 출력은 피질하를 구조적으로 뺀다(arXiv:2510.13768 5.3절, arXiv:2607.01400 8절). 그러면 같은 '정서 decoding' 점수라도 표상 공간이 무엇을 포함하느냐에 따라 의미가 달라진다. 이는 심리측정의 측정 불변성 개념으로 다룰 수 있다.

---

## 5. 새 Sub-axis 또는 하위 연구 방향

| 제안 | 소속 Axis | 내용 | 독립 Axis 필요성 |
|---|---|---|---|
| **In-silico Representational Fidelity** | F (주), H, T | in-silico 예측과 관찰 반응의 일치를 점별(voxel r)이 아니라 관계 기하(RSA), 정서 축, 영역별로 측정한다 | F의 Sub-axis로 충분. 다만 L의 In-Silico Experiments와 중복되므로, L은 '실험 설계', F는 '표상 충실도'로 역할을 나눈다 |
| **Residual / Idiosyncratic Encoding** | H (주), O | 관찰 반응에서 자극 구동 group 예측을 뺀 잔차를 분석 단위로 삼는다 | H의 Sub-axis. O의 개인차와 짝을 이룬다 |
| **Brain Foundation Encoder Auditing** | H, T, R | matched-control, ground-truth recovery, feature visualization 생체 검증, 재현 감사(in-silico replication) | T와 공유하는 Sub-axis |
| **Pretraining Contamination & Stimulus Provenance** | S (주), T | fMRI 사전학습 목록, 자극 출처 중복(EmoNet-Horikawa), 백본 학습 분포 겹침 | S의 Sub-axis. 프로젝트 전체 점검 항목으로도 둔다 |
| **Synthetic-to-Real (Measurement-Apparatus) Generalization** | S | 합성 뇌에서 학습하거나 검증한 것이 실측 뇌로 이전되는가(EmoMind의 '장치 의존' 개념) | S의 Sub-axis |
| **Representation Coverage (피질 전용 vs 피질하 포함)** | F | 표상 공간이 정서 관련 피질하를 포함하는지 명시하고, 결과를 coverage에 따라 층화한다 | F의 Sub-axis |
| **Physiology-augmented Encoding** | H, (A의 Interoception) | 자극 feature와 측정 생리(PPG, 호흡, EDA)를 함께 넣은 encoding으로 limbic 잔차를 설명한다 | H의 Sub-axis |

판단: 독립 Axis를 새로 만들 정도는 아니다. 다만 "In-silico vs Observed"는 F, H, L, S, T에 걸친 횡단 쟁점이다. Coordinator가 조합 단계에서 별도 태그(예: `insilico-validation`)로 추적하기를 제안한다.

---

## 6. Discussion-to-Research Chains

각 단계 뒤 괄호에 근거 논문 ID와 원문 위치를 적는다. 모든 질문에서 in-silico 예측과 관찰 fMRI를 구분한다.

### Chain 1. In-silico 정서 기하의 충실도 (Horikawa, Emo-FilM)
* **Original Finding:** TRIBE v2 합성 뇌는 clip별 정서 정보를 대체로 보존했다. 그러나 clip 간 RSA는 실측의 약 26%만 남았다(arXiv:2605.16739, 4.2절, 5 Discussion 2단락).
* **Unresolved Question:** 그 비교는 MC 실측 fMRI와 Emo-FilM 자극의 합성 반응을 대조한 것이라 같은 자극의 짝 비교가 아니다. 저자들은 손실이 내수용, 맥락, 개인 특이 신호 때문일 것이라 추정했을 뿐 검증하지 않았다(같은 위치). 어느 영역, 어느 정서에서 관계 구조가 무너지는가?
* **Technological Development:** TRIBE v2가 in-silico 실험 플랫폼으로 공개되었다(arXiv:2605.04326, 3 Discussion 1단락). 무음 영상 학습 데이터(Wen2017)와 modality dropout이 있어 무음 자극을 입력할 수 있다(5.3절, 5.7절).
* **New Dataset / Model Combination:** Horikawa 2,181 clip을 실험 run 순서대로 TRIBE v2에 넣는다(영상만). 예측 시계열을 관찰 데이터와 같은 방식으로 블록 평균하고, 피질 parcel별로 관찰 대비 RSA를 계산한다. Emo-FilM은 14편 전체(시청각 + 대사)로 같은 비교를 하고, 피험자 30명의 ISC로 noise ceiling을 낸다. 정서 RDM(34범주, 50항목 규범 평정), 시각-의미 RDM(V-JEPA2, LLM 캡션)과의 부분 RSA로 분해한다.
* **New Research Question:** 관찰 fMRI에서 측정한 정서 표상 기하 가운데 자극 계산 가능한 group encoder가 재현하는 부분과 재현하지 못하는 부분은 어디인가? 재현되지 않는 잔차 기하는 시각-의미 feature를 통제한 뒤에도 정서 평정 기하와 정렬하는가?
* **반증 조건:** 잔차 기하가 정서 RDM과 무관하면, 관찰된 정서 기하는 자극으로 계산 가능하다는 해석이 지지된다. 이 결과도 과학적으로 의미가 있다.
* already_done: partially (arXiv:2605.16739, 짝 비교 아님).

### Chain 2. Limbic 맹점의 분해: 잡음인가, 몸인가, 평가인가 (Emo-FilM)
* **Original Finding:** TRIBE v2의 피질하 점수는 피질보다 2~3배 낮다(arXiv:2605.04326, 2.1절). 저자들은 입력이 시각, 청각, 의미로 제한되고 체성감각, 내수용감각이 없으며 뇌를 수동 관찰자로 다룬다는 점을 한계로 들었다(3 Discussion 2단락). MIRAGE의 개선은 Limbic망에서 가장 작다(arXiv:2605.29850, 4절 'Where the gains come from').
* **Unresolved Question:** 편도체 반응 중 습관화, 학습, 비시각 모달 의존 부분은 예측할 수 없었다(doi:10.1523/JNEUROSCI.1436-24.2025, Discussion 7단락). 영화 시청에서 편도체 효과는 작았다(doi:10.1016/j.neuroimage.2020.117258, bioRxiv 판 Discussion 5~6단락). 이 맹점이 낮은 SNR 때문인지 빠진 변수 때문인지는 미해결이다.
* **Technological Development:** 3모달 비선형 encoder(TRIBE v2), 피질하 학습 스크립트(`run_subcortical`, 저장소), noise ceiling 정규화 관행(arXiv:2507.22229, 3.2절).
* **New Dataset / Model Combination:** Emo-FilM 30명을 쓴다. 편도체, 섬엽, vmPFC, 선조체, 시상하부의 ISC 기반 ceiling을 구한다. 설명 변수는 (a) TRIBE v2 예측과 그 백본 feature, (b) 참가자 본인의 PPG, 호흡, EDA(1000 Hz), (c) 별도 평정자 50항목 1 Hz 평정(Appraisal, Physiology, Feeling 성분)이다. 영화 단위로 교차검증하며 variance partitioning한다.
* **New Research Question:** 정서 관련 피질하와 내수용 영역에서, ceiling으로 정규화했을 때 자극 구동 foundation encoder가 설명하지 못하는 신뢰 가능한 분산은 얼마인가? 그중 얼마가 참가자의 측정 생리, 얼마가 규범적 평가 성분으로 설명되는가?
* **주의:** 생리는 fMRI 참가자 본인, 평정은 별도 평정자라 주체가 다르다(Stage 1 보고서 4.2절). 생리 회귀는 BOLD의 심박, 호흡 잡음 제거와 혼동되므로 RETROICOR 처리 여부를 통제 조건으로 둔다.
* already_done: no (검색 범위 내). overlap: Emo-FilM 연구 (사전학습 멀티모달 뇌 인코딩으로 정서 맥락 기여 분석. 생리 분해와 ceiling 정규화 부분은 차이).

### Chain 3. Group 예측 잔차와 개인 정서 경험 (Spacetop, Emo-FilM)
* **Original Finding:** TRIBE v2는 group 평균 반응을 대부분의 개별 피험자 기록보다 잘 추정한다(arXiv:2605.04326, 2.3절). 그러나 group 학습 encoder는 영상 간, 피험자 간 특이 구조를 평균으로 붕괴시키며, 공개 checkpoint에는 피험자별 매개변수가 없다(arXiv:2607.01400, 7 Discussion 1단락, 8 Limitations).
* **Unresolved Question:** vmPFC 반응은 정렬 후에도 개인 특이적이다. 저자들은 공통 반응을 가정하는 분석이 이 영역을 오해할 수 있다고 경고했다(doi:10.1126/sciadv.abf7129, Discussion 5단락). 정렬 후 남는 개인차는 해부 정렬 때보다 더 신뢰할 만하다(doi:10.7554/eLife.56601, 'Beyond shared information' 절). Horikawa는 평정이 참가자 본인 것이 아님을 한계로 들었다(doi:10.1016/j.isci.2020.101060, Limitations of the Study 1단락). 개인 잔차가 개인 경험을 담는지는 미검증이다.
* **Technological Development:** TRIBE v2 unseen-subject 예측과 1시간 이하 subject fine-tuning(2.4절), hyperalignment.
* **New Dataset / Model Combination:** Spacetop alignvideo를 쓴다. 참가자 약 100명이 같은 영상을 같은 순서로 보고 본인 7차원 평정을 남겼다. 여기에 TRIBE v2 group 예측을 더하고 hyperalignment를 적용한다. 잔차(관찰 - group 예측) 패턴으로 참가자별 평정 편차(본인 - 집단 평균)를 예측하고, 보류 영상으로 검증한다. 평정 결측 약 51%는 결측 모형으로 처리한다.
* **New Research Question:** 자극 구동 group 반응에서 벗어난 개인 특이 신경 반응이 같은 자극에 대한 그 개인의 정서 보고 편차를 예측하는가? 그 예측은 vmPFC처럼 개인 특이성이 큰 영역에 집중되는가?
* **반증 조건:** 잔차가 평정 편차를 예측하지 못하고 감각 영역 잔차만 신뢰할 만하면, 개인 정서 차이는 이 해상도의 BOLD 잔차에 담기지 않는다는 결론이 된다.
* already_done: partially (doi:10.1126/sciadv.abf7129는 HMM 상태와 별도 표본 평정. 자극 구동 foundation 예측을 기준선으로 쓴 잔차 분석은 미발견). overlap: 없음.

### Chain 4. 정서 고유 분산의 재검증: controversial selection (Horikawa)
* **Original Finding:** 정서 모델이 시각 객체, 의미 모델보다 여러 영역을 잘 설명했고, 단일양식에서 초양식으로 가며 시각, 의미, 정서 순서로 표상이 이동했다(doi:10.1016/j.isci.2020.101060, Discussion 5단락). Koide-Majima는 객관 정보, 정서, 뇌 활동의 정밀 비교가 필요하다고 명시했다(doi:10.1016/j.neuroimage.2020.117258, bioRxiv 판 Discussion 7단락).
* **Unresolved Question:** 구조가 다른 모델들이 거의 같은 예측력을 보이고, 지표에 따라 결론이 뒤집힌다(doi:10.1038/s41467-024-53147-y, Discussion 'Model-to-Brain linking methods' 1단락). encoding 지표는 정답 구조도 잘 식별하지 못한다(arXiv:2302.06677, 5 Discussion). 2020년 feature 기준의 '정서 고유 분산'이 최신 foundation feature 아래에서도 남는가?
* **Technological Development:** 저자들이 제안한 controversial selection, 즉 기존 자극에서 모델 예측이 갈리는 하위집합을 고르는 방법(doi:10.1038/s41467-024-53147-y, 같은 절 4단락). TRIBE v2와 V-JEPA2 feature. EmoNet은 Horikawa 자극으로 학습되었으므로 제외하거나 오염 통제 조건으로만 쓴다(doi:10.1126/sciadv.aaw4358, Methods).
* **New Dataset / Model Combination:** Horikawa에서 정서 평정 RDM(34+14)과 시각-의미 foundation RDM(V-JEPA2, LLM 캡션, TRIBE v2 예측 피질)의 예측이 가장 크게 갈리는 clip 쌍을 고른다. 이 선택은 한 피험자 집합에서 한다. 그다음 보류 피험자에서 뇌 RDM이 어느 쪽을 따르는지 검정해, 선택과 검정을 분리하여 순환 추론을 막는다.
* **New Research Question:** 정서 규범 평정과 최신 시각-의미 foundation 표상이 서로 다른 뇌 기하를 예측하는 자극에서, 관찰된 transmodal 영역의 기하는 어느 쪽을 따르는가?
* **반증 조건:** 대부분 영역이 foundation 쪽을 따르면, Horikawa의 정서 표상 주장은 시각-의미 공선성의 결과일 가능성이 커진다.
* already_done: partially (doi:10.1016/j.isci.2020.101060은 구식 feature, doi:10.1038/s41467-024-49073-8은 OTC 결합 표상. 정서 vs foundation feature의 controversial selection은 미발견). overlap: EmoViS (affective brain geometry의 sensory-semantic 기원).

### Chain 5. 뇌 입력 foundation latent의 정서 구조: 누수 통제 benchmark (Spacetop, Emo-FilM)
* **Original Finding:** fMRI foundation model은 state decoding에서는 강하지만, trait 예측에서는 단순 FC baseline을 확실히 넘지 못했다(arXiv:2510.13768, 5.4절, 6 Conclusion). 저자들은 benchmark 확장과 표준화를 한계로 들었다(6 Conclusion 한계 (3)). NeuroSTORM은 task fMRI가 사전학습의 20% 미만이라는 점을 한계로 들었다(arXiv:2506.11167, Discussion 'Limitations' 첫째).
* **Unresolved Question:** 유일한 foundation model 정서 회귀는 같은 영화 시간 블록을 7:1:2로 무작위 분할했다. 라벨은 portrayed emotion 주석으로 보인다(arXiv:2601.23090, 부록 B.2; doi:10.12688/f1000research.6230.1 초록). 따라서 latent가 경험 정서를 조직한다는 증거는 아직 없다.
* **Technological Development:** CortexMAE 공개 가중치와 Brainmarks의 재현 가능한 피험자 분리 평가(arXiv:2510.13768, 4절), 피질하 포함 parcel 변형(5.3절), NeuroSTORM prompt tuning.
* **New Dataset / Model Combination:** Spacetop은 fsLR 91k CIFTI가 제공되어 flat map 입력이 바로 가능하다. alignvideo 본인 평정, faces 표정 지각, shortvideo 귀속 판단이 있다. Emo-FilM은 fsLR로 재전처리하고 1 Hz 규범 평정을 쓴다. 고정 encoder(CortexMAE-F, CortexMAE-P+Tian, NeuroSTORM, Brain-JEPA) embedding에 probe를 붙인다. 분할은 leave-one-film-out과 leave-subject-out이다. 기준선은 FC, 원시 parcel 시계열, TRIBE v2 자극 예측이다.
* **New Research Question:** 자극 없이 뇌 동역학만으로 사전학습한 latent 공간이, 영화와 피험자를 넘어 일반화되는 경험 정서 축(본인 보고)과 귀속 정서 축(타인 정서 판단)을 구분해 조직하는가? 그 구조는 자극 구동 예측과 단순 baseline을 넘어서는가?
* **반증 조건:** probe 성능이 FC나 원시 parcel baseline 이하이면, 현재 brain foundation latent는 정서에 대해 추가 표상 가치가 없다.
* already_done: partially (arXiv:2601.23090 누수 위험 있음, arXiv:2506.11167은 HCP 과제 상태). overlap: 없음.

### Chain 6. 정서 영역 '선택성'의 고처리량 검정과 생체 검증 고리 (Horikawa, NSD)
* **Original Finding:** 편도체 하위영역별 합성 자극은 서로 구별되었다(doi:10.1523/JNEUROSCI.1436-24.2025, Discussion 6단락). 저자들은 다른 영화와 자극으로 맥락 의존성을 검사하라고 제안했다(같은 논문 Discussion 8단락). TRIBE v2 feature visualization 저자들은 최적 자극을 사람에게 보이거나 보류된 자연 fMRI와 비교해야 encoder가 아닌 피질에 대한 주장이 된다고 적었다(arXiv:2605.13904, 6.6 Future work).
* **Unresolved Question:** in-silico에서 정서 영역을 가장 강하게 구동하는 자극은 실제로 그 영역을 구동하는가? 그 자극은 하나의 정서로 묶이는가, 시각-의미 feature로 설명되는가?
* **Technological Development:** 수백만 자극 screening으로 선택성을 검정하는 방법(doi:10.1038/s41467-021-25409-6, Discussion 1단락), 탐색과 in vivo 검증을 결합한 RNC(doi:10.1038/s41562-025-02252-z, Discussion 5단락).
* **New Dataset / Model Combination:** 1단계에서는 Horikawa 피험자 4명으로 편도체, vmPFC, 섬엽 encoder를 학습하거나 TRIBE v2 zero-shot 피질 예측을 쓴다. 2단계에서 Horikawa 2,181 clip과 NSD 73k 이미지(정적 영상 변환)를 screening한다. 3단계 검증은 새 촬영 없이 Horikawa 보류 피험자의 실측 반응과 NSD 피험자의 실측 beta로 한다(NSD에서 학습한 모델은 사용하지 않는다).
* **New Research Question:** 정서 관련 영역에 대한 '정서 범주 선택성' 가설이 FFA, PPA 선택성처럼 고처리량 screening을 견디는가? 최고 예측 자극의 정서 일관성과 시각-의미 일관성은 어느 쪽이 큰가?
* **주의:** NSD는 정서 라벨이 100장뿐이라, 자극 정서는 AI 추정 라벨로만 기술된다(CLAUDE.md 6절 구분). 관찰 데이터의 선택이므로 인과 결론은 낼 수 없다.
* already_done: partially (doi:10.1523/JNEUROSCI.1436-24.2025는 생성만, 생체 검증 미보고. doi:10.1038/s41467-021-25409-6은 시각 범주 영역만).

### Chain 7. 초감각 정서 부호의 in-silico 감각 박탈 (Emo-FilM, Horikawa)
* **Original Finding:** vmPFC는 감각 경험과 모달리티에 독립적인 범주 정서 부호를 가진다(doi:10.1126/sciadv.adk6840, Discussion 3단락). Horikawa 2020은 무음 자극의 한계를 언급하며 교차 모달 정서 표상 연구를 제안했다(doi:10.1016/j.isci.2020.101060, Discussion 마지막 단락).
* **Unresolved Question:** 편도체 encoder가 포착한 정서 부호가 시각 특이적인지 영역 일반적인지는 미해결이다(doi:10.1523/JNEUROSCI.1436-24.2025, Discussion 5단락 마지막). 초감각 부호 중 자극 정보만으로 계산 가능한 부분은 얼마인가?
* **Technological Development:** TRIBE v2 modality dropout과 모달리티 ablation 지도(arXiv:2605.04326, 2.8절, 5.3절).
* **New Dataset / Model Combination:** Emo-FilM 영화를 영상만, 오디오만, 텍스트만, 전체로 각각 TRIBE v2에 넣는다. 각 예측이 관찰 Emo-FilM fMRI의 정서 관련 분산(50항목 평정 기반 encoding)을 영역별로 얼마나 재현하는지 비교한다. 무음 관찰 데이터(Horikawa)에서 영상만 넣은 예측이 vmPFC 정서 기하를 재현하는지와 대조한다.
* **New Research Question:** 관찰된 vmPFC, pSTS 정서 신호 가운데 단일 모달 자극만으로 계산 가능한 부분과 다중 모달 통합이 필요한 부분은 어떻게 나뉘는가? 이 분할은 감각 박탈 연구의 결론(초감각 범주 부호)과 일치하는가?
* already_done: partially (arXiv:2605.04326 2.8절은 정서와 무관한 일반 모달 기여 지도). overlap: Emo-FilM 연구 (멀티모달 encoder로 정서 기여 분석. 모달리티 박탈 대조는 차이).

---

## 7. 담당 Axis 확장 제안

### Axis F: Brain Representation
* **추가:** In-silico (Model-predicted) Representations, Residual / Idiosyncratic Representations, Self-supervised Brain Foundation Latents, Representation Coverage (cortical-only vs subcortical-inclusive), Flat-map / Surface Video Representations.
* **재분류:** "Shared Latent Representations"와 "Subject-specific Representations"는 표상 형식(F)과 변이의 원천(O)으로 역할을 나눈다. F는 공간의 형식과 coverage를, O는 개인차의 의미를 다룬다.
* **명시 요구:** 모든 F 관련 결과에 '관찰 / in-silico / 혼합' 출처 태그를 붙인다.

### Axis H: Encoding
* **추가:** Residual Encoding (observed minus foundation prediction), Foundation Encoder Auditing (matched-control, ground-truth recovery, in-silico replication, feature-visualization validation), Physiology-augmented Encoding, Inverse Use of Encoders (simulation-based inference, inverse design), Zero-shot Group vs Fine-tuned Individual Encoding.
* **병합:** "Brain Foundation Model Encoding"과 "Brain Response Simulation"은 한 Sub-axis(Foundation Encoders & In-silico Simulation)로 합친다. 그 아래를 zero-shot group과 fine-tuned individual로 나눈다.
* **구분 강화:** "Emotion Feature-to-Brain"은 라벨 출처에 따라 규범 평정, 본인 보고, AI 추정 정서로 하위 구분한다.

### Axis S: Generalization & Robustness
* **추가:** Pretraining Contamination & Stimulus Provenance, Leakage-controlled Splits (stimulus/movie/subject/temporal block), Synthetic-to-Real Generalization, Preprocessing & Space Shift (volume, surface, parcel, native vs template), Cross-paradigm Generalization (자연 시청 vs 통제 과제, 예: HCP Hariri vs 영화).
* **구체화:** "Invariance / Equivariance"는 정서에 맞게 '모달리티 불변성(초감각성)'과 '맥락 불변성(같은 내용, 다른 맥락)'으로 구체화한다.
* **삭제 제안 없음.**

---

## 8. 미확인 사항 (이번 라운드에서 확인하지 못한 것)

1. TRIBE v2 Hugging Face 모델 카드의 실제 파일 구성(피질하 head 포함 여부). README와 arXiv:2607.01400은 피질만이라고 기술한다.
2. TRIBE v2 백본(V-JEPA 2의 VideoMix22M, Llama 3.2, Wav2Vec-BERT 2.0) 사전학습 데이터와 우리 자극의 중복 여부.
3. 코드의 `Allen2022Bold` 분기가 공개 checkpoint 학습에 쓰였는지 여부(공개 학습 설정에는 없음).
4. Brain-JEPA 라이선스(저장소에 LICENSE 없음), NeuroSTORM 라이선스 표기 불일치(Apache-2.0 vs MIT), Omni-fMRI와 Brain-Mamba 가중치 공개 여부, EmoNet 가중치 공개 경로.
5. Omni-fMRI StudyForrest 정서 라벨의 정확한 출처. 6개 범주로 기술되어 Labs 2015 주석과 정확히 대응하는지 원문을 확인하지 못했다.
6. BrainLM Discussion 원문(bioRxiv HTML에서 절 미검출), Bashivan 2019, Labs 2015, arXiv:2604.04025, arXiv:2609.15685, arXiv:2610.22706 본문.
7. Koide-Majima 2020은 bioRxiv 판 본문을 읽었다. NeuroImage 출판본과의 차이는 미확인이다.
8. Jang & Kragel 2025의 합성 자극이 생체 검증되었는지. 본문 Discussion에는 언급이 없었으나 보충자료는 확인하지 못했다.
9. 우리 환경의 계산 자원과 checkpoint 보유 여부(`reference/datasets_and_resources.md` 1절 보류 항목).
