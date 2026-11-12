# Round 1: Independent Discovery (multimodal-dynamics)

* 에이전트: multimodal-dynamics (Agent 5, Multimodal Learning & Temporal Dynamics)
* 담당: Axis D Temporal Dynamics, Axis M Multimodal Integration, 외부 분야 Aesthetics / Neuroaesthetics
* 기준일: 2026-11-12
* 절차: `reference/protocols.md` P1
* 읽은 파일: `CLAUDE.md`, `reference/protocols.md` P1, `reference/axes.md`, `reference/starting_papers.md`, `reference/existing_projects.md`(겹침 표시 전용), `reference/datasets_and_resources.md`, `outputs/stage1/dataset_intelligence_report.md`, `outputs/stage1/gate_decision.md`, `outputs/STAGE_STATUS.md`(사용자 결정 기록), `outputs/stage1/dataset_EmoFilM.md`와 `dataset_Spacetop.md`, `dataset_Horikawa.md`의 해당 절(소리 유무, 블록 구조 확인용). 다른 에이전트 폴더는 읽지 않았다.
* 문헌: `outputs/agents/multimodal-dynamics/literature.jsonl` 51편. 모두 식별자 경로(Crossref API, arXiv API, PubMed)로 존재를 확인했다(verified 51). 2024~2026년 26편. Affective Neuroscience 밖 분야(ML, 인지신경과학, 계산사회과학, 멀티미디어, 음악 인지) 20편 이상. Discussion 또는 Limitations 원문 확인(full_text) 30편, 초록만 확인(abstract_only) 20편, 미확인(no) 1편.
* 표기: [본문] Discussion/Limitations 원문 확인, [초록] 초록만 확인, [추론] 본 에이전트의 추론, [Stage 1] Stage 1 보고서 근거. 문헌은 `literature.jsonl`의 `id`로 단다.

---

## 0. 데이터 조건 (Axis D, M 관점에서 다시 정리)

Stage 1 보고서로 소리 유무와 시간 해상도를 확인했다. 사용자 결정(2026-11-12)에 따라 네 데이터셋 모두 원본 자극 보유(G1 = 보유)로 본다. 아래 질문에는 "원본 자극 필요" 여부를 따로 적어, 모델 feature 추출이 필요한 질문과 라벨, 뇌 수준만으로 되는 질문을 구분한다.

| | Horikawa (1순위) | Emo-FilM | Spacetop (alignvideo 중심) |
|---|---|---|---|
| 소리 | **무음** [Stage 1] | **있음**: 오디오 포함 in-ear plug 제시, 대사는 영어로 보임 [Stage 1: dataset_EmoFilM.md 1.6절] | **있음**: HED에 Auditory-presentation 표기 [Stage 1: dataset_Spacetop.md 1.2절] |
| 시간 구조 | 10 s 블록이 71.6%, 8 s 미만 비디오는 반복 재생, 블록마다 2 s 휴지, 런당 36블록, **5명 동일 순서**, 공개 전처리본은 4 s shift 후 블록 평균 [Stage 1] | 영화 14편(6.7~17.1분), TR 1.3 s, 영화당 1회 시청 [Stage 1] | 영상 49편(20 s~5분 39초), TR 0.46 s [Stage 1] |
| 정서 라벨 시간 해상도 | 비디오당 1개 값 | **1 Hz 연속** consensus(항목 x 영화당 3~4명) | 영상 종료 후 1회 |
| 평정 주체 | 별도 평정자(규범) | 별도 평정자(규범). 평정자는 같은 영화를 최대 6번 봄. fMRI 참가자는 부분 회고 평정(영화당 5항목, 영화 길이의 약 20%) | **fMRI 참가자 본인**, 약 51% 결측, 평정 구간이 영상 끝 HRF와 겹침 |
| 생리 | 없음 | fMRI 참가자 PPG, 호흡, EDA 공개 | 기록했으나 공개본 없음 |

이 표에서 나오는 Axis D, M의 구조적 기회:
1. **Horikawa는 '연속 짧은 자극 + 동일 순서 + 밀집 라벨'** 이라 정서 이월(carry-over)과 순서 효과를 연구하기 좋은 동시에, 그것이 기존 decoding의 교란 요인일 수 있다.
2. **소리 대비**: Horikawa(무음) vs Emo-FilM, Spacetop(소리 있음). 같은 이름 정서의 표상이 소리 유무에 따라 다른지 묻는 질문은 라벨 비호환(Stage 1 수준 2~3) 때문에 RSA나 공통 feature 공간 경유로만 가능하다.
3. **시간 해상도 사다리**: Emo-FilM(1 Hz 연속, 타인) → Spacetop(사후 1회, 본인). 연속 경험이 회고 평가로 압축되는 규칙을 묻는 질문은 두 데이터셋을 이어야 가능하다.

---

## 1. 중요한 미해결 문제

### U1. 신경 수준의 정서 이월(carry-over, hysteresis)과 HRF 잔여의 분리
* vmPFC 공간 패턴은 수십 초~분 단위로 유지된다(Chang 2021, 10.1126/sciadv.abf7129 [본문 Discussion 3번째 단락]). 정서 블록의 뇌 상태는 수십 분 뒤 중립 부호화로 이월된다(Tambini 2017, 10.1038/nn.4468 [본문]). 그러나 이월에 필요한 유도 시간과 지속 시간은 모른다(같은 논문 Discussion 5번째 단락).
* 영화 클립 연속 제시 연구는 이월 가능성을 인정하면서도 "긴 클립과 느린 BOLD로 완화된다"고만 처리했다(Saarimäki 2025, 10.1162/imag_a_00517 [본문 Limitations]).
* Horikawa는 10 s 블록이 2 s 휴지만 두고 연속되고 공개 전처리본은 4 s shift 후 블록 평균이다 [Stage 1]. HRF 꼬리(수 초~10여 초)가 다음 블록 평균에 섞인다. 즉 **직전 클립 정서가 다음 블록 패턴에 남는 현상이 'HRF 잔여'인지 '신경 이월'인지 구분된 적이 없다**. 정서 시계열 연구의 관성(inertia) 개념(Kuppens 2010, 10.1037/a0020962 [초록])을 신경 수준에서 검증할 수 있는 기회이기도 하다.

### U2. 정서 신경 동역학은 이산 상태 전이인가 연속 drift인가
* Chang 2021은 vmPFC가 "상태 + 급전이"인지 "점진적 drift"인지 구분할 수 없었고 hybrid 연속-이산 모형을 제안했다 [본문 Discussion 4번째 단락].
* Baldassano 2017의 사건 HMM은 사건 내 정보 누적을 설명하지 못한다고 스스로 밝혔다(10.1016/j.neuron.2017.06.041 [본문 Discussion]).
* Ma & Kragel 2026은 graph-like(이산 전이) 표상과 map-like(연속 공간) 표상이 순차 단계인지 별개 과정인지 열린 문제로 남겼다(10.1038/s41467-025-68240-z [본문 Discussion 6번째 단락]).
* 혼합 감정이 안정 상태인지 전이 중간 상태인지도 미결이다(Vaccaro 2024, 10.1093/cercor/bhae122 [초록]).

### U3. 정서는 어느 감각 채널에 의존하며, '추상(supramodal) 정서 코드'는 언어 의미의 재표현인가
* 같은 영화의 시청각, 시각 전용, 청각 전용 판본에서 vmPFC는 모달리티 무관 범주 코드, pSTS는 모달리티 무관 valence를 보였지만, 유발되는 정서 자체가 모달리티마다 달랐다(공포는 청각만으로 어렵고 경멸은 청각판에서 쉬움). 저자는 vmPFC 추상 코드가 모든 판본에 공통인 언어 채널에 기댈 수 있다고 썼다(Lettieri 2024, 10.1126/sciadv.adk6840 [본문 Discussion]).
* 다중모달 모델의 뇌 정렬 이득은 단일모달 특징으로 부분적으로만 설명된다(Oota 2025, arXiv:2505.20027 [본문 Discussion]).
* MLLM의 정서 기하가 뇌를 더 잘 예측한다는 '감각 접지' 주장은 무음 비디오로만 검증되었다(Du 2025, arXiv:2509.24298 [본문]).
* 즉 **소리(대사, 음악, 효과음)가 어떤 정서를 얼마나 만들며, 소리를 빼면 뇌의 정서 표상이 어떻게 바뀌는지**를 자연주의 데이터와 현대 오디오 모델로 분해한 연구는 없다. 음악이 중립 영상과 결합할 때만 변연계가 반응한다는 고전 결과(Eldar 2007, 10.1093/cercor/bhm011 [초록])도 자연주의 영화에서 재검증되지 않았다.

### U4. 정서와 정서 성분마다 다른 시간 척도
* surprise는 급격하고 love는 서서히 쌓인다는 시간 척도 차이가 sliding window, framewise 분석을 왜곡할 수 있다(Morgenroth 2023, 10.1093/scan/nsad063 [본문 'A space odyssey' 절]).
* 전방 hippocampus가 love, satisfaction, guilt를 상대적으로 잘 decoding했다는 관찰은 post hoc이다(Ma & Kragel 2026 [본문 Discussion 4번째 단락]).
* 다중모달 LLM의 문맥 길이를 늘리면 고차 피질 정렬이 오르지만 최대 24 s까지만 시험했고 정서는 다루지 않았다(Jindal 2026, arXiv:2602.07570 [본문 Appendix K]). 음악 모델 MERT는 5 s 문맥으로 학습되었다(arXiv:2306.00107 [본문 Limitations]).
* **정서 항목별 고유 시간 척도와 뇌 영역의 시간 수용창(temporal receptive window)을 체계적으로 대응시킨 연구는 없다.**

### U5. 순간 경험과 회고 평가, 그리고 '누구의 정서인가'
* 연속 즐거움의 최고점이 사후 전체 미적 평가와 강하게 상관했지만(R=0.69) 연속-요약 관계(peak vs peak-end)는 미결로 남았다(Belfi 2019, 10.1016/j.neuroimage.2018.12.017 [본문 Discussion 'Felt pleasure' 절 4번째 단락]).
* 동영상에서는 순간 즐거움의 관찰자 간 일치도는 높고 사후 평가의 일치도는 낮았다(Isik & Vessel 2021, 10.3389/fnhum.2021.676032 [본문 Discussion]).
* 연속 평정과 fMRI가 다른 사람이라 개인 특이적 경험을 설명하지 못한다(Lettieri 2024 [본문 Limitations], Saarimäki 2025 [본문 Limitations], Ke 2025 10.1371/journal.pcbi.1012994 [본문 Discussion]).
* Emo-FilM(1 Hz, 별도 평정자)과 Spacetop(사후 1회, 본인)은 이 문제의 양 끝에 있다.

### U6. '일반화되는 arousal'은 정서인가 감각 강도인가, valence는 왜 일반화되지 않는가
* dynamic FC로 학습한 arousal 표지는 영화와 표본을 넘어 일반화되었지만 valence는 어떤 조건에서도 일반화되지 않았다. 저자는 deep learning 자극 feature로 arousal 구동 요인을 분해하라고 제안했다(Ke 2025 [본문 Discussion 마지막 단락]).
* 공포 장면이 더 어둡고 시끄럽다는 저수준 공선성 경고(Morgenroth 2023 [본문 'White noise' 절])와 합치면, **일반화된 arousal 표지가 음량, 움직임 같은 시청각 강도의 재표현일 가능성**이 통제되지 않았다.

### U7. 영화 특이성과 일반화
* ISC와 ISC-행동 연관이 영화마다 크게 다르며 Emo-FilM에서도 영화별 t-map 간 상관이 평균 0.10이다(Leipold 2026, 10.1162/IMAG.a.1400 [초록, 결과 일부]). 영화 14편뿐인 Emo-FilM의 정서 동역학 결과는 영화 수준 confound(장르, 음악 비중, 편집 속도)와 공선적일 수 있다.

### U8. AI 연속 정서 주석의 타당성과 시간축 검증
* LLM 연속 정서 라벨로 fMRI decoding을 한 연구는 라벨이 참가자 경험이 아니고 서사 의미를 decoding할 위험을 스스로 지적했다(Zhang 2026, arXiv:2606.07707 [본문 4.4 Limitations]). 닫힌 MLLM 주석은 버전 변동과 층 표상 접근 불가 문제가 있다(Li 2026, 10.1162/imag.a.1300 [본문 Discussion]). AI 경계는 규범 대리물이고 개인 편차는 별도 정보다(Michelmann 2023, arXiv:2301.10297 [본문 Discussion]).
* Stage 1이 지적했듯 Spacetop의 영상 단위 평정으로는 AI 주석의 **시간축** 타당성을 검증할 수 없다. Emo-FilM 1 Hz human consensus와 평정자별 원자료가 유일한 시간축 검증 기준이다.

---

## 2. 주목할 모델과 방법론

라이선스는 직접 확인하지 못한 것이 많다. GitHub API와 Hugging Face는 이 세션에서 접근하지 못했다. 확인 수준을 표에 그대로 적는다.

| # | 모델 / 방법 (근거 ID) | Pretrained weights / 코드 공개 | Input → Output | 학습 목표 | 라이선스 (확인 수준) | 우리 용도 | 주의 |
|---|---|---|---|---|---|---|---|
| 1 | **V-JEPA 2** (arXiv:2506.09985) | 공개(TRIBE가 V-JEPA 2 gigantic을 사용, arXiv:2507.22229) | 비디오 클립(TRIBE 설정: 4 s 구간 64 프레임) → patch token 잠재 표상, predictor가 가린 잠재 표상 예측 | JEPA: 잠재 공간 마스크 예측(action-free 사전학습) | TRIBE 부록 B가 "Apache"로 기재 [논문 기재, 직접 미확인] | 프레임 단위 시각 예측 오차(surprise), 불확실성 시계열 | 공간 평균하면 위치 정보 손실(TRIBE 2.3절). overlap: EmoBrain (V-JEPA2 feature) |
| 2 | **TRIBE** (arXiv:2507.22229) | 코드: github.com/facebookresearch/algonauts-2025 (논문 링크). 학습된 가중치 공개 여부는 이번에 미확인 | V-JEPA 2(비디오), Wav2Vec-BERT 2.0(오디오), Llama-3.2-3B(시간 정렬 텍스트) 2 Hz feature → 1,000 parcel fMRI | fMRI 회귀, modality dropout, 다피험자 | 구성 요소: V-JEPA 2 Apache, Wav2Vec-BERT 2.0 MIT, Llama 3.2 커뮤니티 라이선스 [논문 부록 B 기재] | modality dropout을 'in-silico 감각 박탈'로 사용, 정서 평정과 encoder 잔차 비교 | CNeuroMod 4명 학습, parcel 해상도. 예측은 in-silico이며 관찰 fMRI가 아님. TRIBE v2는 encoding-foundation 담당 |
| 3 | **Qwen2.5-Omni-7B** (arXiv:2503.20215) | 공개(GitHub QwenLM/Qwen2.5-Omni, 논문 링크) | 텍스트, 이미지, 오디오, 비디오(스트리밍) → 텍스트, 음성. TMRoPE로 오디오-비디오 시간 정렬 | 다중모달 사전학습 + 후학습(Thinker-Talker) | Apache 2.0 [검색, 2차 출처] | 공개 가중치 시청각 MLLM으로 Emo-FilM 50항목 연속 주석, 은닉 상태 feature, 오디오 on/off 비교, 문맥 길이 sweep(Jindal 2026 방식) | LIRIS-ACCEDE, Blender 영화는 인터넷 공개라 사전학습 오염 가능성. 출력은 AI 추정 정서 |
| 4 | **MERT** (arXiv:2306.00107) | 공개(GitHub yizhilll/MERT, 논문 링크) | 음악 오디오 → 프레임 단위 embedding | MLM, RVQ-VAE 음향 teacher + CQT 음악 teacher | 미확인 | 분리한 영화 음악 성분의 정서 feature | 5 s 학습 문맥(긴 음악 긴장 누적 약함) |
| 5 | **LAION-CLAP** (arXiv:2211.06687) | 공개로 알려짐, 이번에 미확인 | 오디오, 텍스트 → 공동 embedding | 오디오-텍스트 대조 학습 | 미확인 | 정서 텍스트 프롬프트 zero-shot 유사도로 소리의 규범적 정서 방향 추정 | 프롬프트 의존, AI 추정 |
| 6 | **ImageBind** (arXiv:2305.05665) | 공개(arXiv comment: Code/Models github.com/facebookresearch/ImageBind) | 이미지/비디오, 텍스트, 오디오, depth, thermal, IMU → 공동 embedding | 이미지를 결합축으로 한 InfoNCE | 미확인 (비상업 라이선스로 알려졌으나 검증 안 함) | 같은 공간에서 시각과 소리의 정서 방향 불일치(AV incongruence) 지표 | 범용 embedding이라 특화 모델보다 약함(논문 6절) |
| 7 | **EM-LLM** (arXiv:2407.09450) | 코드 공개(github.com/em-llm/EM-LLM-model, 논문 링크) | 토큰 시퀀스 → surprise 기반 사건 경계 + 그래프 보정 경계 + 검색 메모리 | 추가 학습 없음(추론 시 구조) | 미확인 | 평정 시계열, 다중모달 feature 시계열에 같은 경계 알고리즘을 적용해 '정서 에피소드' 정의 | 원래 텍스트 토큰용 |
| 8 | **Event segmentation HMM** (10.1016/j.neuron.2017.06.041), hybrid 연속-이산 모형 (Chang 2021 제안) | HMM 방법 공개 논문. hybrid 모형은 이번 라운드에 검증 문헌을 확보하지 못함 | ROI 시계열 → 사건 경계, 상태 열 | 비지도 | 해당 없음 | 정서 change point vs 신경 상태 전이 비교 | 상태 수 동일 가정(Chang 2021 Limitations) |
| 9 | **DSA (Dynamical Similarity Analysis)** (arXiv:2306.10168) | 방법. 코드 위치는 이번에 미확인 | 두 시스템의 시계열 → delay embedding + DMD(Koopman 근사) → 벡터장 Procrustes 거리 | 해당 없음 | 미확인 | 평정 궤적, vmPFC 궤적, MLLM 궤적의 동역학 비교(기하와 분리) | DMD 하이퍼파라미터 민감, fMRI의 느린 표본에서 검증 사례 없음 |
| 10 | **twRSA (time-warped RSA)** (10.1016/j.isci.2025.114072) | 방법(코드 공개 여부 미확인) | 길이가 다른 자극의 시계열 → 시간 변화 RDM 비교 | 해당 없음 | 해당 없음 | 모달리티 간 지연 가정 없이 평정, 생리, 음향, 뇌를 비교. 길이가 다른 Horikawa 클립과 Emo-FilM 장면 비교 | 시간 변화의 '패턴'만 비교하고 방향성은 없음 |

보조: Wav2Vec 2.0/HuBERT 층별 feature와 음원 분리(목소리 vs 사운드트랙)를 결합한 청각 정서 encoding 파이프라인(Pan 2025, arXiv:2509.21381 [본문]). video-SALMONN(arXiv:2406.15704 [초록])은 Qwen2.5-Omni의 대안 시청각 LLM으로 모델 특이성 점검용.

---

## 3. 다른 분야에서 가져와 적용할 연구 아이디어

| # | 원 분야와 아이디어 (근거) | Affective Neuroscience로의 이전 | 데이터셋 | 원본 자극 필요 |
|---|---|---|---|---|
| X1 | **LLM 장문맥 메모리 공학**: Bayesian surprise + 그래프 modularity로 토큰 열을 사건으로 나누는 EM-LLM (arXiv:2407.09450) | 정서 평정 시계열과 다중모달 feature 시계열에 같은 알고리즘을 적용해 '정서 에피소드'를 정의하고, 그 경계가 hippocampus 경계 반응(10.1016/j.neuron.2017.06.041)과 fMRI 참가자의 회고 평정을 예측하는지 시험 | Emo-FilM | 평정만 쓰면 불필요, feature 쓰면 필요(보유) |
| X2 | **RNN 동역학 비교(계산신경과학)**: 기하가 아닌 벡터장 수준 유사도 DSA (arXiv:2306.10168) | Ma & Kragel의 정서 '지도'를 넘어, 그 지도 위의 이동 규칙(이완 속도, 어트랙터, 관성; Kuppens 2010의 DynAffect 모수)이 평정, 뇌, 모델에서 같은지 비교 | Emo-FilM | 모델 궤적 비교 시 필요 |
| X3 | **다중모달 encoding의 modality dropout** (TRIBE, arXiv:2507.22229) | Lettieri 2024의 실제 판본 조작(맹, 농 참가자 포함)을 in-silico로 수천 장면 규모로 확장: 소리를 지웠을 때 정서 관련 parcel 예측이 어디서 무너지는가. 실제 무음 관찰은 Horikawa가 제공하므로 in-silico 예측과 관찰을 구분해 대조 | Emo-FilM, Spacetop, Horikawa | 필요 |
| X4 | **계산사회과학의 서사 정서 arc** (Reagan 2016, 10.1140/epjds/s13688-016-0093-1) | Emo-FilM 14편의 1 Hz consensus를 arc 형태로 분해해 '서사 내 위치'(상승 중, 반전 직전, 하강 후)가 vmPFC, hippocampus 상태와 연결되는지, 대사 텍스트 arc와 경험 arc가 어긋나는 지점에서 무엇이 정서를 만드는지(음악? 표정?) 분석 | Emo-FilM, Spacetop narratives | 대사 arc는 필요 |
| X5 | **멀티미디어의 관객 동기화 기반 미적 하이라이트 검출** (Muszynski 2018, 10.1145/3175497) | 관객 생리 동기화로 정의된 하이라이트를 fMRI 뇌 간 동기화(ISC)와 DMN 반응으로 검증, 정서 강도와 분리 | Emo-FilM (같은 영화 계열) | 불필요(외부 주석 입수 필요) |
| X6 | **음악 인지의 정보이론 기대 모형** (Cheung 2019, 10.1016/j.cub.2019.09.067; Brielmann & Dayan 2022, 10.1037/rev0000337) | 영화의 시각, 청각, 언어 예측 모델에서 불확실성 x 놀람 상호작용과 '학습 진전'(기대 분포의 변화)을 계산해 정서, 미적 순간을 예측 | Emo-FilM, Spacetop | 필요 |
| X7 | **음악 인지의 time-warped RSA** (10.1016/j.isci.2025.114072) | 평정자 반응 지연, HRF, 생리 지연을 각각 가정하지 않고 평정-생리-뇌-feature의 시간 변화 구조를 비교. Emo-FilM의 '보고된 생리'(평정 항목)와 '측정된 생리'(PPG, EDA)를 직접 비교 | Emo-FilM | 음향 feature 쓰면 필요 |
| X8 | **장문맥 MLLM의 시간 창 탐침** (Jindal 2026, arXiv:2602.07570) | 같은 문맥 길이 sweep을 정서 항목과 정서 관련 ROI에 적용해 '정서 시간 수용창' 지도 작성 | Emo-FilM, Spacetop | 필요 |

---

## 4. 기존 Affective Neuroscience와 예상 밖으로 연결될 수 있는 개념

1. **Koopman 연산자와 동역학적 켤레(conjugacy)** (arXiv:2306.10168). 정서를 '공간 위의 점'(지도, 기하)이 아니라 '공간 위의 흐름'(벡터장)으로 본다. 두 사람의 정서 공간 기하가 달라도 흐름(예: 슬픔에서 기저점으로 돌아오는 속도)이 같을 수 있고, 그 반대도 가능하다. 정서 관성(Kuppens 2010)과 vmPFC 상태 지속(Chang 2021)을 같은 언어로 묶는다. [추론]
2. **사건 분절을 통한 기억 압축 = 정서 경계**. EM-LLM은 surprise 경계로 문맥을 압축해 무한 문맥을 다룬다(arXiv:2407.09450). McClay 2023은 정서 변화가 기억의 사건 경계를 만든다고 보였다(10.1038/s41467-023-42241-2 [본문]). 둘을 합치면 "정서는 경험을 기억 단위로 자르는 압축 신호"라는 계산 가설이 된다. 오차형 경계와 불확실성형 경계의 신경 해리(Nguyen 2026, 10.7554/eLife.107955 [초록])를 정서 쪽에서 재현할 수 있다(놀람 vs 서스펜스). [추론]
3. **In-silico 감각 박탈**. 선천 맹, 농 연구(Lettieri 2024)가 실제로 하는 일을 다중모달 encoder의 modality dropout(TRIBE)으로 근사한다. 관찰 데이터(Horikawa 무음 fMRI)와 in-silico 예측을 대조하는 '반사실 감각 조건' 비교는 CLAUDE.md 6절의 in-silico vs observed 구분을 연구 설계 자체로 만든다. [추론]
4. **학습 진전(learning progress)으로서의 미적 가치**(Brielmann & Dayan 2022 [초록]). 비디오 world model(V-JEPA 2)의 내부 기대 분포가 영화를 보며 얼마나 갱신되는가를 순간 '미적 보상'으로 정의하면, 정서(valence)와 독립적인 '흥미, 감동' 신호를 모델에서 직접 뽑을 수 있다. 정서 강도와 미적 하이라이트를 분리하는 계산 도구. [추론]
5. **시간 정렬 문제의 일반화(time-warping)**. 연속 평정에는 HRF 지연과 별개로 평정자 반응 지연, 평정자의 반복 시청으로 인한 예측적 앞당김이 섞인다. Lee 2021(10.7554/eLife.64972 [본문])은 반복 시청 시 뇌 사건 경계가 인간 주석보다 앞서게 된다고 보였다. Emo-FilM 평정자는 같은 영화를 최대 6번 봤다 [Stage 1]. 따라서 **Emo-FilM consensus는 '처음 보는 fMRI 참가자'보다 앞당겨진 정서 시계열일 수 있다**. twRSA(10.1016/j.isci.2025.114072)나 lag 추정을 정서 연구의 표준 단계로 들여와야 한다. [추론, 검증 필요]

---

## 5. 새 Sub-axis 또는 하위 연구 방향

| # | 제안 | 소속 Axis | 독립 Axis 필요 여부 | 근거 |
|---|---|---|---|---|
| S1 | **Affective Carry-over vs Hemodynamic Spillover** (순차 맥락 효과의 신경 이월과 측정 잔여 분리) | D (Hysteresis / Emotional Inertia를 세분), Q와 교차 | 불필요 | Chang 2021, Tambini 2017, Saarimäki 2025, Horikawa 블록 구조 [Stage 1] |
| S2 | **Affective Timescale Hierarchy / Affective Temporal Receptive Windows** (정서 항목별 고유 시간 척도와 피질 시간 수용창의 대응) | D (Multi-timescale Integration을 정서 특화), E와 교차 | 불필요 | Morgenroth 2023, Ma & Kragel 2026, Jindal 2026, Lee 2021 |
| S3 | **Online-to-Retrospective Integration** (순간 정서가 사후 평가와 기억으로 압축되는 규칙: peak, end, 평균, 경계 가중) | D, A(Emotion Recognition vs Experience 옆), Q와 교차 | 불필요 | Belfi 2019, Isik & Vessel 2021, Fredrickson & Kahneman 1993, McClay 2023 |
| S4 | **Emotional Event Boundaries** (정서 change point가 만드는 사건 경계, 오차형 vs 불확실성형) | 현재 C(Event Boundaries)에 있음. D에 교차 등재 제안 | 불필요 | McClay 2023, Kumar 2023, Nguyen 2026, Baldassano 2017 |
| S5 | **Modality Dependence of Emotion** (어떤 정서가 소리, 영상, 대사 중 무엇에 의존하는가. 실제 판본 조작, 데이터셋 대비, in-silico ablation) | M, S(Cross-modal Transfer)와 교차 | 불필요 | Lettieri 2024, Eldar 2007, TRIBE, Oota 2025 |
| S6 | **Audio Source Decomposition for Affect** (대사, 음악, 효과음 분리 후 정서 기여 분해) | M, B(Audio / Music / Speech Features)와 교차 | 불필요 | Pan 2025, Muller-Rodriguez 2024 (arXiv:2410.17300 [초록]) |
| S7 | **Cross-modal Affective Congruence and Reliability Weighting** (시청각 정서 단서의 일치, 불일치와 단서 신뢰도 가중) | M (Audio-Visual Integration을 세분), N과 교차 | 불필요 | Gao 2026 SCAN 리뷰(10.1093/scan/nsag090 [초록])의 신뢰도 vs 가치 이중 경로 가설, Gao 2019 메타분석 |
| S8 | **Affective Dynamics Comparison** (평정, 뇌, 모델 궤적의 동역학 비교: 어트랙터, 이완, 관성) | D와 K(Dynamical Attractors, Latent Trajectories)의 교차 | 불필요(K 담당과 조율) | DSA, Kuppens 2010, Ma & Kragel 2026 |
| S9 | **Aesthetic Engagement Dynamics** (미적 하이라이트, 감동, 흥미의 시간 구조와 정서 강도와의 분리) | A(Aesthetic Emotion)와 D의 교차 | **후보**: Stage 3 조합 결과에 따라 'Aesthetic & Value Experience' 독립 Axis 검토. 현재는 A, D, N에 걸쳐 있어 독립시키면 조합이 쉬워지나 문헌량이 아직 적음 | Belfi 2019, Isik & Vessel 2021, Iigaya 2023, Muszynski 2018, Brielmann & Dayan 2022 |
| S10 | **Temporal Alignment & Lag Estimation** (HRF, 평정 반응 지연, 반복 시청 예측 앞당김, time-warping) | Q(측정)와 D의 교차 | 불필요 | Lee 2021, twRSA, Ma & Kragel(canonical HRF만 사용) |

---

## 6. Discussion-to-Research Chains

형식: `Original Finding → Unresolved Question → Technological Development → New Dataset / Model Combination → New Research Question`. 각 단계에 근거 ID와 원문 위치를 단다. 마지막에 원본 자극 필요 여부, 안전장치, 선행 수행 여부, 겹침을 적는다.

### Chain 1. Horikawa 연속 블록의 정서 이월 (Horikawa 1순위)
* **Original Finding**: vmPFC 공간 패턴은 수십 초~분 단위로 지속된다(10.1126/sciadv.abf7129, Discussion 3번째 단락). 정서 뇌 상태는 이후 중립 부호화로 이월된다(10.1038/nn.4468, Discussion 1번째 단락).
* **Unresolved Question**: 이월에 필요한 유도와 지속 시간이 불명(10.1038/nn.4468, Discussion 5번째 단락). 클립 연속 제시의 이월은 '완화된다'고만 가정됨(10.1162/imag_a_00517, Limitations 1번째 단락). 상태 지속인지 drift인지 미결(10.1126/sciadv.abf7129, Discussion 4번째 단락).
* **Technological Development**: 원 논문 당시 기술 문제라기보다 데이터 구조 문제다. 블록 길이 변이(10 s~94 s [Stage 1])를 지렛대로 쓰는 FIR, deconvolution 모형과 개인 HRF 추정, 순차 HMM(10.1016/j.neuron.2017.06.041). 직전 클립의 시각 feature를 nuisance로 넣어 시각 적응과 정서 이월을 분리.
* **New Dataset / Model Combination**: Horikawa raw BIDS(연속 시계열) + 34범주, 14차원 라벨의 t-1, t-2 시차 설계 + (가능하면) 직전 클립 V-JEPA 2 feature. Emo-FilM 1 Hz consensus로 영역별 이월 시간 척도의 외부 검증.
* **New Research Question**: "Horikawa에서 직전 비디오의 정서(34범주 profile)는 HRF 잔여와 직전 시각 내용을 통제한 뒤에도 다음 블록의 뇌 패턴에 남는가? 남는다면 이월 시간 척도는 영역별로(vmPFC, insula, amygdala 대 시각 피질) 다르고 정서 범주별로(공포, 혐오 대 오락, 기쁨) 다른가? 그리고 기존 블록 평균 decoding 성능의 일부는 이 이월 때문에 왜곡되었는가?"
* 원본 자극: 핵심 분석은 **불필요**(라벨 + raw BIDS). 시각 nuisance를 최신 모델로 넣으려면 필요(보유).
* 안전장치: (1) 5명 동일 순서 [Stage 1]라 '특정 클립 쌍' 효과와 이월이 섞인다. 순서를 바꿀 수 없으므로 런 안 라벨 순환 이동(circular shift) null과 블록 길이 의존성(긴 블록 뒤 이월 감소 여부)으로 HRF 잔여를 판별. (2) 내용 중복 15쌍과 같은 원본 영상 클립(movie-level leakage, 미확인)은 같은 fold. (3) 라벨은 타인 규범 평정이라 '참가자 정서 상태의 이월'이 아니라 '자극 정서 정보의 신경 이월'로 해석. (4) 짧은 비디오의 반복 재생(루프)이 블록 안 반복 억제를 만들 수 있어 반복 횟수(미공개 [Stage 1])를 비디오 길이로 추정해 통제.
* already_done: no (검색 범위에서 Horikawa 이월 분석은 못 찾음. 영화 후 휴지기 이월 연구만 있음, search_index 수준).
* 겹침: 없음. 단 결과가 Horikawa decoding 기준선을 바꾸면 EmoBrain, EmoViS에 영향(겹침이 아니라 의존 관계로 기록).

### Chain 2. 다중모달 예측 surprise와 정서 사건 경계
* **Original Finding**: 정서 valence 급변이 음악 지각 변화 이상으로 기억 분절을 만든다(10.1038/s41467-023-42241-2, Discussion 2번째 단락). 언어 모델의 일시적 Bayesian surprise가 인간 사건 분절을 가장 잘 예측한다(10.1111/cogs.13343, Discussion 1번째 단락).
* **Unresolved Question**: 통제된 음악 결과가 복잡한 정서 서사로 일반화되는가(10.1038/s41467-023-42241-2, Discussion 8번째 단락). 텍스트 모델은 휴지, 억양, 정서 섞인 발화에 접근하지 못한다(10.1111/cogs.13343, Discussion 4.2 둘째 단락). 경계는 오차형과 불확실성형으로 나뉘고 신경 서명이 다르다(10.7554/eLife.107955, 초록).
* **Technological Development**: 잠재 예측 비디오 모델 V-JEPA 2(arXiv:2506.09985), 오디오-비디오 시간 정렬 MLLM(arXiv:2503.20215의 TMRoPE), 무학습 surprise 분절 + 그래프 보정(arXiv:2407.09450, 5 Discussion).
* **New Dataset / Model Combination**: Emo-FilM 1 Hz consensus에서 정서 change point 추출 + 모달리티별(영상, 음악, 대사) surprise와 불확실성 시계열 + fMRI HMM 경계(10.1016/j.neuron.2017.06.041)와 hippocampus 경계 반응. Spacetop alignvideo로 신경 경계 재현(연속 평정은 없음).
* **New Research Question**: "자연주의 영화의 정서 경계는 다중모달 예측 surprise(오차형) 또는 예측 불확실성(불확실성형)으로 환원되는가, 아니면 지각 surprise를 통제한 뒤에도 hippocampus 경계 반응과 vmPFC 상태 전이를 추가로 설명하는가? 놀람형 정서 경계와 서스펜스형 정서 경계는 Nguyen 2026이 보인 오차형, 불확실성형 신경 순서를 따르는가? 어떤 모달리티의 surprise가 어떤 정서 항목의 경계를 만드는가?"
* 원본 자극: **필요**(보유).
* 안전장치: consensus는 별도 평정자 규범 평정이고 평정자는 영화를 여러 번 봐서 경계가 앞당겨질 수 있다(개념 5). 평정 반응 지연과 HRF를 따로 추정. 저수준 컷(편집 경계)과 음향 onset을 nuisance로. 영화 14편 leave-one-film-out. 다중 비교(항목 50 x ROI).
* already_done: partially (Sherlock fMRI에서 경계 영역이 정서 내용 변화에 민감하다는 학회 초록, Emo-FilM HMM과 affective surprise 학회 초록이 검색됨. 둘 다 search_index 수준, 미출판. 다중모달 모델 surprise와 정서 경계를 경쟁시킨 출판 연구는 못 찾음).
* 겹침: overlap: Emo-FilM 연구 (영화 시청 중 시간 정보의 뇌 기여를 멀티모달 encoding으로 분석하는 계획과 방법 일부 겹침).

### Chain 3. 소리가 만드는 정서: 대사, 음악, 효과음 분해와 무음 대비
* **Original Finding**: vmPFC는 모달리티 무관 범주 코드, pSTS는 모달리티 무관 valence, 초기 감각 피질은 모달리티 특이(10.1126/sciadv.adk6840, Discussion 2~6번째 단락). 음악은 중립 영상과 결합할 때 amygdala, hippocampus 반응을 키운다(10.1093/cercor/bhm011, 초록).
* **Unresolved Question**: vmPFC 추상 코드가 공통 언어 채널(대사, 자막)에 기댈 가능성(10.1126/sciadv.adk6840, Discussion constructionist 단락). 모달리티에 따라 유발 정서 자체가 다름(같은 논문 Discussion 'sensory modality' 단락). 일반화된 arousal 표지의 자극 구동 요인 미분해(10.1371/journal.pcbi.1012994, Discussion 마지막 단락). 다중모달 이득의 출처 미해명(arXiv:2505.20027, 7 Discussion (1)).
* **Technological Development**: 음원 분리(목소리 vs 사운드트랙) + wav2vec 계열 층별 feature(arXiv:2509.21381, Conclusion), 음악 SSL MERT(arXiv:2306.00107), 시각 V-JEPA 2, 대사 transcript LLM feature, 단일모달 정보 제거 residual 방법(arXiv:2505.20027), modality dropout(arXiv:2507.22229, 3.3~3.4절).
* **New Dataset / Model Combination**: Emo-FilM(50항목 1 Hz, 소리 있음) + Spacetop alignvideo(본인 사후 평정, 소리 있음) + Horikawa(무음, 시각 전용 참조). 라벨 풀링은 불가하므로 이름 대응 범주의 RSA(Stage 1 수준 2)와 공통 feature 공간 경유(수준 3)로만 결합.
* **New Research Question**: "(a) Emo-FilM에서 정서 항목과 CPM 성분마다 대사, 음악, 효과음, 영상 feature의 고유 설명량은 어떻게 다른가, 즉 어떤 정서가 '소리 의존적'인가? (b) vmPFC와 hippocampus의 정서 decoding은 대사 언어 feature와 음악 feature를 제거한 뒤에도 남는가(Lettieri 2024의 언어 의존 가설 검증)? (c) 무음 Horikawa에서 학습한 정서 RSA 구조와 Emo-FilM 정서 구간의 뇌 RSA 구조는 소리 의존 정서에서 더 크게 어긋나는가?"
* 원본 자극: **필요**(보유).
* 안전장치: 음악 비중과 장르가 영화 수준 confound(U7). AV feature와 정서 라벨 공선성은 variance partitioning으로 보고하되 고유 분산 0이 '정서 없음'을 뜻하지 않음을 명시. Horikawa와 Emo-FilM은 평정 척도, 주체 구조, 시간 해상도가 달라 (c)는 탐색적. in-silico ablation 결과는 관찰 결과와 분리 보고.
* already_done: partially (Forrest Gump 사운드트랙 저수준 특징과 공유 정서의 연결: arXiv:2410.17300 [초록]; EEG에서 목소리 vs 사운드트랙 분해: arXiv:2509.21381. fMRI에서 음원 분리 + foundation model로 정서 항목별 모달리티 의존성을 지도화한 연구는 못 찾음).
* 겹침: overlap: Emo-FilM 연구 (사전학습 멀티모달 encoding으로 정서 맥락 기여 분석).

### Chain 4. 정서 시간 수용창 (Affective Temporal Receptive Windows)
* **Original Finding**: vmPFC는 긴 시간 통합 창을 가진다(10.1126/sciadv.abf7129, Discussion 3번째 단락). 전방 hippocampus가 love, satisfaction, guilt를 상대적으로 잘 decoding(10.1038/s41467-025-68240-z, Discussion 4번째 단락, post hoc). 장문맥 video-audio MLLM은 문맥이 길수록 고차 피질 정렬이 오른다(arXiv:2602.07570, 7 Conclusion).
* **Unresolved Question**: 정서마다 시간 척도가 다르다는 지적(10.1093/scan/nsad063, 'A space odyssey' 절 2번째 단락)이 체계적으로 검증되지 않음. MLLM 문맥은 24 s까지만, 정서는 미검토(arXiv:2602.07570, Appendix K 첫 단락).
* **Technological Development**: 문맥 길이 sweep(arXiv:2602.07570), 문맥 한계를 넘는 surprise 메모리(arXiv:2407.09450), 음악 모델 문맥 한계 인식(arXiv:2306.00107, Limitations).
* **New Dataset / Model Combination**: Emo-FilM 50항목(항목별 평정 자기상관) + Qwen2.5-Omni feature를 3 s~수 분 문맥으로 추출 + ROI별 encoding. Spacetop narratives(오디오, 텍스트 이야기)로 언어 전용 대조.
* **New Research Question**: "정서 항목마다 고유 시간 척도(평정 자기상관, 그 항목을 가장 잘 예측하는 모델 문맥 길이)가 있는가? 그 시간 척도는 해당 정서를 가장 잘 부호화하는 뇌 영역의 시간 수용창과 일치하는가(예: surprise는 짧은 창과 감각, 측두 영역, love, guilt, satisfaction은 긴 창과 전방 hippocampus, vmPFC)? CPM 성분(Appraisal, Expression, Physiology, Feeling) 사이에 일관된 시간 위계가 있는가?"
* 원본 자극: 평정 자기상관 분석은 불필요, 모델 문맥 sweep은 필요(보유).
* 안전장치: 평정 자기상관에는 평정 도구(마우스 커서) 관성과 평정자 내 z-score가 섞인다. 평정자별 원자료로 커서 동역학 기준선을 추정. 긴 문맥 feature는 서사 의미와 공선적이라 '정서 시간 척도'와 '의미 시간 척도'를 분리해야 함. HRF와 TR(1.3 s) 한계로 수 초 미만 척도는 해석 불가.
* already_done: partially (Ma & Kragel의 post hoc 관찰뿐. 정서 항목별 시간 척도 지도는 못 찾음).
* 겹침: overlap: Emo-FilM 연구 (시간 정보의 뇌 기여 분석과 일부 겹침).

### Chain 5. 연속 경험에서 회고 평가로: Emo-FilM과 Spacetop 잇기
* **Original Finding**: 연속 즐거움 최고점이 사후 미적 평가와 강하게 상관(10.1016/j.neuroimage.2018.12.017, Discussion 'Felt pleasure' 절 3번째 단락). 영상에서 순간 즐거움 일치도는 높고 사후 평가 일치도는 낮음(10.3389/fnhum.2021.676032, Discussion 'Interestingly' 단락). 회고 평가의 지속시간 무시(10.1037/0022-3514.65.1.45, 본문 미열람).
* **Unresolved Question**: 연속-요약 관계(peak vs peak-end vs 평균)는 추가 연구 필요(10.1016/j.neuroimage.2018.12.017, Discussion 'Felt pleasure' 절 4번째 단락). 그 신경 기반은 미확인.
* **Technological Development**: Emo-FilM 1 Hz human consensus로 시간축이 검증된 AI 연속 정서 추정(Qwen2.5-Omni 등), 정서 경계 검출(Chain 2), 영상 종료 시점 신경 반응 분석.
* **New Dataset / Model Combination**: Emo-FilM(연속 consensus + fMRI 참가자 회고 평정) → 통합 규칙 학습. Spacetop alignvideo(참가자 본인 사후 7차원) → AI 추정 궤적에 규칙 적용, 영상 종료 직후 BOLD와 연결.
* **New Research Question**: "사후 정서 평가는 순간 정서 궤적의 어떤 요약(peak, end, 평균, 정서 경계 가중)으로 결정되며 그 규칙은 정서마다 다른가(예: 슬픔은 end, 공포는 peak)? 영상 종료 직후 hippocampus와 vmPFC 반응은 궤적 요약을 반영하며, 그 반응이 참가자 본인의 사후 평정 편차를 예측하는가?"
* 원본 자극: Spacetop 궤적 추정에 필요(보유). Emo-FilM 규칙 학습은 불필요.
* 안전장치: Spacetop 평정 구간이 영상 끝 HRF와 겹친다 [Stage 1]. 평정 약 51% 결측(무작위 결측 아님 가능성). Spacetop의 AI 궤적은 '미검증 AI 추정 시계열'로 표기(Stage 1 5.3 #3 원칙). Emo-FilM은 평정 주체가 타인, Spacetop은 본인이라 규칙 차이에 주체 차이가 섞임. Emo-FilM fMRI 참가자 회고 평정은 영화 길이 약 20%만 덮음.
* already_done: no (뇌 수준에서 회고 요약 규칙을 비교한 영화 fMRI 연구는 검색 범위에서 못 찾음. 행동 수준 peak-end 연구는 다수).
* 겹침: 없음.

### Chain 6. 영화의 미적 하이라이트: 정서 강도와 분리되는가
* **Original Finding**: DMN은 고평정 작품에서 초기에 일시적으로 반응하고 저평정 작품에서는 억제가 길어진다('억제 해제', 10.1016/j.neuroimage.2018.12.017, Discussion 'Aesthetically moving artworks engage the DMN' 절 1~2번째 단락). 음악 즐거움은 불확실성 x 놀람 상호작용을 따르며 amygdala, hippocampus, 청각 피질이 이를 반영(10.1016/j.cub.2019.09.067, 초록).
* **Unresolved Question**: 가치 구성의 시간 동역학은 recurrent 모형으로 규명해야 함(10.1038/s41467-022-35654-y, Discussion 7번째 단락). 미적 가치의 학습 기반 모형은 정지 자극 시뮬레이션뿐(10.1037/rev0000337, 초록). 관객 동기화 기반 하이라이트(10.1145/3175497, 초록)는 뇌로 검증되지 않음.
* **Technological Development**: 비디오, 오디오 예측 모델의 불확실성과 놀람, 내부 기대 분포 변화(학습 진전) 계산(V-JEPA 2, MERT). 동적 ISC(10.1016/j.neuroimage.2019.116512, 초록).
* **New Dataset / Model Combination**: Emo-FilM fMRI + fMRI 참가자 EDA(동기화 계산) + 같은 영화 계열의 외부 미적 하이라이트 주석(입수 필요) + 모델 기반 정보이론 지표.
* **New Research Question**: "영화의 미적 하이라이트 순간은 정서 강도(Emo-FilM 'Intense emotion' 등)를 통제한 뒤에도 DMN의 일시적 반응과 뇌 간 동기화를 만드는가? 다중모달 예측 모델의 불확실성 x 놀람 상호작용이나 '학습 진전'이 하이라이트와 그 신경 반응을 정서 강도보다 잘 예측하는가?"
* 원본 자극: **필요**(보유). 외부 하이라이트 주석 접근 조건은 미확인.
* 안전장치: 하이라이트 주석은 다른 관객의 생리 동기화로 정의되어 있어 '미적 경험'의 대리 지표일 뿐이다. 미적 경험, 정서 강도, 주의 각성의 공선성. fMRI 참가자 EDA와 외부 관객 동기화는 다른 집단. 정보이론 지표는 모델 의존적이므로 2개 이상 모델로 견고성 확인.
* already_done: no (영화 fMRI에서 미적 하이라이트와 정서 강도를 분리한 연구는 못 찾음).
* 겹침: 없음.

### Chain 7. 기하에서 동역학으로: 정서 궤적의 흐름 비교
* **Original Finding**: hippocampus-vmPFC가 정서 개념을 지도처럼 조직하며 이는 사건 전이 통계 학습으로 생길 수 있다(10.1038/s41467-025-68240-z, Discussion 6번째 단락).
* **Unresolved Question**: graph-like와 map-like가 순차인지 별개인지(같은 단락). drift vs 상태(10.1126/sciadv.abf7129, Discussion 4번째 단락). RL 모형 대안 미검토(10.1038/s41467-025-68240-z, Discussion 8번째 단락).
* **Technological Development**: 동역학 수준 비교 DSA(arXiv:2306.10168, 4 Discussion 셋째 단락: 실험 데이터 적용이 향후 과제), 정서 확산 모형 DynAffect(10.1037/a0020962, 초록).
* **New Dataset / Model Combination**: Emo-FilM에서 (a) consensus 평정 궤적, (b) vmPFC, hippocampus 신경 궤적(PLS 잠재 공간), (c) MLLM 은닉 상태 궤적. 영화별, 참가자별로 DSA 거리와 DynAffect 모수(어트랙터 강도, 변동성) 추정.
* **New Research Question**: "정서 평정 궤적, vmPFC 신경 궤적, MLLM 궤적은 기하(지도)뿐 아니라 동역학(기저점으로의 이완 속도, 어트랙터 구조, 관성)에서도 같은가? 동역학 유사도는 영화 간, 참가자 간 일반화되며, 기하가 같아도 동역학이 다른 참가자(예: 정서 관성이 큰 사람)를 식별할 수 있는가?"
* 원본 자극: MLLM 궤적은 필요(보유), 평정-뇌 비교는 불필요.
* 안전장치: fMRI 표본 간격(1.3 s)과 HRF 평활이 신경 동역학을 왜곡한다. 평정 궤적의 동역학에는 커서 관성이 섞인다. DSA의 DMD 모수 민감성. 신경 궤적의 '관성'과 BOLD 자기상관(temporal autocorrelation)을 구분하는 null(위상 무작위화) 필요. 탐색적 분석으로 명시.
* already_done: no (정서 fMRI에 DSA를 적용한 연구는 검색 범위에서 못 찾음).
* 겹침: 없음. geometry-info 담당(Axis K)과 Stage 3에서 조율 필요.

### Chain 8. Horikawa의 미적 정서: 시각 전구 특징인가 미적 표상인가 (Neuroaesthetics x Horikawa)
* **Original Finding**: 감각 피질의 '가치 신호' 일부는 가치의 전구 특징일 수 있다(10.1038/s41467-022-35654-y, Discussion 8번째 단락). 독립 localizer 없이 보고된 미적 신호는 특징 불균형의 오인일 수 있다(10.3389/fnhum.2021.676032, Discussion 4번째 단락).
* **Unresolved Question**: 특징은 고정하고 가치만 바꿔 분리하라는 제안(10.1038/s41467-022-35654-y, Discussion 8번째 단락), 영상과 이미지의 미적 결정 요인 차이(10.3389/fnhum.2021.676032, Discussion 영상 vs 이미지 단락).
* **Technological Development**: 저수준, 고수준 시각 특징 분해(LFS류)와 비디오 모델 층별 feature(V-JEPA 2), MLLM 정서 기하(arXiv:2509.24298).
* **New Dataset / Model Combination**: Horikawa 34범주 중 aesthetic_appreciation, awe, entrancement, admiration [Stage 1 범주 목록] + 같은 클립의 시각 특징(figshare vision feature 또는 V-JEPA 2) + HCP360 ROI(DMN, mPFC, 장면 선택 영역).
* **New Research Question**: "Horikawa에서 미적 정서(aesthetic appreciation, awe, entrancement) 정보는 장면 배치, 자연 풍경, 움직임 같은 시각 특징으로 설명되는 분산을 제거한 뒤에도 DMN과 mPFC에 남는가? 장면 선택 피질의 미적 정서 신호는 전구 특징으로 설명되는가? 미적 정서는 다른 긍정 정서(joy, amusement)와 구별되는 신경 서명을 갖는가?"
* 원본 자극: figshare vision feature만 쓰면 불필요, 최신 모델 feature는 필요(보유).
* 안전장치: 미적 범주는 자연 풍경 같은 특정 내용과 강하게 공선적일 수 있다(시각-의미-정서 공선성). 라벨은 MTurk 별도 평정자의 선택 비율. 5명이라 개인차 질문 불가. ROI는 독립 정의(HCP360) 사용으로 circular inference 회피.
* already_done: no (검색 범위에서 Horikawa 미적 범주를 따로 분석한 연구는 못 찾음. Horikawa 2020 원 논문은 정서 범주 전반만 다룸 [검색 요약]).
* 겹침: overlap: EmoViS (affective brain geometry의 sensory-semantic 기원).

---

## 7. 담당 Axis 확장 제안

### Axis D: Temporal Dynamics
* **추가**
  * Affective Carry-over vs Hemodynamic Spillover (S1). 기존 'Hysteresis / Emotional Inertia'는 개념만 있고 측정 문제(HRF 잔여, 순서 고정)를 담지 못한다.
  * Affective Timescale Hierarchy (S2). 'Multi-timescale Integration'을 정서 항목 단위로 구체화.
  * Online-to-Retrospective Integration (S3).
  * Affective Dynamics Comparison (S8). K의 'Dynamical Attractors', 'Latent Trajectories'와 교차 등재.
  * Temporal Alignment & Lag Estimation (S10). Q와 교차 등재.
* **재분류**
  * 'Temporal Prediction'(D)과 C의 'Surprise / Prediction Error', 'Emotional Expectation'은 같은 계산 대상(예측, 놀람, 불확실성)을 가리킨다. D에는 '예측의 시간 구조'(얼마나 먼 미래를 예측하는가, Lee 2021), C에는 '예측의 내용'(무엇을 기대하는가)으로 나누어 기술할 것을 제안.
  * C의 'Event Boundaries'를 D에 교차 등재하고 '정서 경계'(S4)를 하위 항목으로.
  * 'Static vs Dynamic Representations'는 범위가 넓어 '자극 단위 요약 표상 vs 시간 분해 표상'(분석 단위 선택 문제)으로 정의를 좁힐 것을 제안.
* **삭제 제안**: 없음.

### Axis M: Multimodal Integration
* **추가**
  * Modality Dependence of Emotion (S5): 판본 조작, 데이터셋 대비(무음 vs 소리), in-silico modality dropout을 묶는 하위 방향.
  * Audio Source Decomposition for Affect (S6).
  * Cross-modal Affective Congruence and Reliability Weighting (S7).
  * Temporal Context Length in Multimodal Models (문맥 길이에 따른 통합, Jindal 2026). D와 교차.
* **재분류**
  * 'Image / Video / Music Integration'은 'Audio-Visual Integration'과 겹친다. 'Audio-Visual Integration'에 통합하고, 대신 'Language-Perception Alignment' 아래에 '대사(speech) vs 자막(text) vs 비언어 소리' 구분을 둘 것을 제안(Lettieri 2024가 자막과 음성을 다른 언어 채널로 사용).
  * 'Modality Invariance'는 Lettieri 2024의 supramodal 코드 개념과 같으므로 'Supramodal vs Modality-specific Affect Coding'으로 이름을 구체화.
* **삭제 제안**: 없음.

### 외부 분야: Aesthetics / Neuroaesthetics
* A의 'Aesthetic Emotion / Awe / Beauty'는 구성개념만 다룬다. 시간 구조(S9 Aesthetic Engagement Dynamics)와 계산 원리(정보이론 가치, 학습 진전; N의 'Emotion as Computational Value / Salience'와 교차)를 하위 방향으로 추가할 것을 제안.
* 독립 Axis('Aesthetic & Value Experience')는 Stage 3에서 조합 빈도를 보고 결정. 현재 문헌(이번 라운드 7편)으로는 A, D, N의 교차 Sub-axis로 두는 편이 낫다고 판단.

---

## 8. 방법론 점검 메모 (위 질문 전체에 공통)

| 항목 | 이번 질문에서의 구체적 위험 | 대응 |
|---|---|---|
| HRF 지연, temporal autocorrelation | Horikawa 4 s shift 블록 평균의 인접 블록 혼입(Chain 1). Emo-FilM 1 Hz 평정 대 TR 1.3 s 정렬, Ma & Kragel은 canonical HRF만 사용 | 개인 HRF 추정, FIR, 위상 무작위화 null, 평정 지연을 HRF와 별도 추정 |
| 평정 반응 지연과 반복 시청 | Emo-FilM 평정자는 최대 6번 시청 [Stage 1] → 예측적 앞당김 가능(Lee 2021) | 평정 시계열과 모델 surprise의 교차상관으로 지연 추정, twRSA |
| Stimulus/movie-level leakage | Emo-FilM 14편, Horikawa 내용 중복 15쌍과 원본 영상 공유 미확인 | leave-one-film-out, 중복 쌍 같은 fold, 영화별 결과 보고(Leipold 2026) |
| 시청각-의미-정서 공선성 | 공포 장면의 어둡고 시끄러운 특성(Morgenroth 2023), 음악 비중의 영화 수준 confound | 음원 분리 feature, variance partitioning, 고유 분산 해석 주의 |
| 평정 주체 | Horikawa, Emo-FilM은 타인 규범, Spacetop은 본인 사후 | 결과 문장에 주체 명시, 주체 차이를 비교 변수로 |
| AI 추정 라벨 | MLLM 연속 주석은 '자극에 표현되거나 유발될 것으로 예상되는 정서' | Emo-FilM 평정자별 원자료의 human-human 천장 대비 평가, 'AI 추정 정서' 표기 |
| 사전학습 오염 | LIRIS-ACCEDE, Blender 영화, 유명 영화 발췌(Spacetop)는 인터넷 공개 | 모델별 오염 가능성 기록, 가능하면 오염 탐지 프롬프트 |
| In-silico vs observed | TRIBE modality dropout 예측 | 관찰 fMRI(Horikawa 무음, Emo-FilM 소리 있음)와 별도 보고 |
| 다중 비교 | 50항목 x 다수 ROI x 문맥 길이 | 사전 ROI(Gao 2019 메타분석, HCP360), FDR, 탐색 vs 확인 구분 |
| Decoding vs 경험 | 높은 decoding을 주관 경험 판독으로 해석 금지 | 모든 질문에서 '자극 정서 정보의 신경 표상'으로 서술 |

---

## 9. 미확인 사항과 한계 (이번 라운드)

1. **모델 라이선스**: GitHub API와 Hugging Face에 접근하지 못해 MERT, CLAP, ImageBind, EM-LLM의 가중치 라이선스를 확인하지 못했다. V-JEPA 2, Wav2Vec-BERT 2.0, Llama 3.2는 TRIBE 부록 기재 수준, Qwen2.5-Omni는 2차 출처 검색 수준이다. TRIBE 학습 가중치 공개 여부도 미확인.
2. **본문 미열람**: Cheung 2019, Vaccaro 2024, Eldar 2007, Sachs 2020, Gao 2019와 2026, Brielmann & Dayan 2022는 출판사 페이지가 bot check로 막혀 초록만 확인했다(우회하지 않음). Fredrickson & Kahneman 1993은 초록도 확인하지 못했다.
3. **hybrid 연속-이산 동역학 모형(rSLDS 등)**: Chang 2021이 제안한 방향이지만 이번 라운드에 검증 문헌을 literature.jsonl에 넣지 못했다. 표 2의 8번은 방향만 기록.
4. **외부 주석 접근**: Muszynski 2018 미적 하이라이트, LIRIS-ACCEDE 연속 V/A(Baveye 2015 ACII, 10.1109/ACII.2015.7344554, Crossref 확인)가 Emo-FilM 영화와 실제로 몇 편 겹치는지, 공개 조건이 무엇인지 미확인(Stage 1은 16편이라는 논문 서술을 기록).
5. **already_done 판단 범위**: WebSearch, PubMed, arXiv 검색 범위의 판단이다. 학회 초록(Sherlock 정서 경계, Emo-FilM HMM affective surprise)은 search_index 수준이라 literature.jsonl에 넣지 않았다.
6. **Horikawa 블록 구조의 세부**: 반복 재생 횟수, 원본 영상 공유 여부는 Stage 1에서도 미확인이라 Chain 1, 8의 통제 설계는 이 정보가 확인되면 수정해야 한다.
7. **verified 기준 메모**: `verified_by`는 Crossref API, arXiv API, PubMed 메타데이터로 식별자를 직접 조회한 경우에만 기록했다. Semantic Scholar는 초록 확인 보조로만 썼다.
