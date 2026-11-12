# Round 1 (Independent Discovery): llm-semantics

* 에이전트: llm-semantics (Agent 10, LLM, Semantics & Social Cognition)
* 주 담당: Axis C (Context, Meaning & Narrative). 외부 분야: Social and Collective Behavior, Human-AI Representation Differences
* 기준일: 2026-11-12
* 절차: `reference/protocols.md` P1
* 읽은 파일: `CLAUDE.md`, `reference/protocols.md`, `reference/axes.md`, `reference/starting_papers.md`, `reference/existing_projects.md`, `reference/datasets_and_resources.md`, `outputs/stage1/dataset_intelligence_report.md`, `outputs/stage1/gate_decision.md`, `outputs/STAGE_STATUS.md`(사용자 결정 기록 포함). 다른 에이전트 폴더는 읽지 않았다.
* 문헌: `outputs/agents/llm-semantics/literature.jsonl` 42편. verified 41편(arxiv, crossref, pubmed 식별자 경로 확인), search_index 1편(Garcia 2025, ICLR, OpenReview 접근 실패). verified 중 2024~2026년 26편, Affective Neuroscience 밖 분야 17편. 본문(Discussion, Limitations, Conclusion) 직접 확인 28편, 초록만 12편, 검색 요약 1편, 미열람 1편.
* 문헌 ID 표기: 본문에서는 `doi:...` 또는 `arXiv:...`를 그대로 쓴다. 자주 쓰는 ID의 약칭은 아래와 같다.

| 약칭 | ID | 본문 확인 |
|---|---|---|
| Du2025 | arXiv:2509.24298 | full_text |
| Asanuma2025 | doi:10.1038/s41598-025-14961-6 (arXiv:2505.12746 v2 본문) | full_text |
| Kiyokawa2024 | doi:10.1038/s41598-024-71690-y | full_text |
| MindCap2025 | doi:10.1126/sciadv.adw1464 (Horikawa, mind captioning) | full_text |
| EmoMind2026 | arXiv:2605.16739 | full_text |
| TakGratch2024 | arXiv:2408.13718 | full_text |
| Tak2025 | arXiv:2502.05489 | full_text |
| Li2024 | doi:10.1016/j.isci.2024.111401 | full_text |
| Xu2025 | doi:10.1038/s41562-025-02203-8 | full_text |
| Doerig2025 | doi:10.1038/s42256-025-01072-0 | full_text |
| Skerry2015 | doi:10.1016/j.cub.2015.06.009 | full_text |
| Miao2026 | doi:10.1038/s41467-026-71151-2 | full_text |
| Lettieri2019 | doi:10.1038/s41467-019-13599-z | full_text |
| ChenWhitney2019 | doi:10.1073/pnas.1812250116 | full_text |
| SantavirtaV2025 | doi:10.1162/imag.a.134 (GPT-4V 사회 지각) | full_text |
| SantavirtaE2025 | doi:10.1101/2025.09.18.677029 (GPT-4 정서, preprint) | abstract_only |
| LiM2026 | doi:10.1162/imag.a.1300 (Gemini 영화 주석) | full_text (bioRxiv판) |
| Houlihan2023 | doi:10.1098/rsta.2022.0047 | full_text |
| Michelmann2025 | doi:10.3758/s13428-024-02569-z | full_text |
| Kawakita2024 | doi:10.1038/s41598-024-65604-1 | full_text |

### 표기 규칙 (CLAUDE.md 6절, 에이전트 정의의 주의 사항)

라벨 출처를 항상 대괄호로 표시한다.

* **[Human-norm]**: 별도 평정자가 자기 경험을 보고하고 집계한 규범 평정 (Horikawa의 Cowen & Keltner 평정, Emo-FilM 1 Hz consensus)
* **[Self]**: fMRI 참가자 본인 보고 (Spacetop alignvideo, Emo-FilM 사후 클립 평정 일부)
* **[Attrib-human]**: 사람이 타인(인물)의 정서를 판단한 귀속 평정 (Spacetop faces, shortvideo, Miao2026의 ToM 평정)
* **[AI-est]**: 모델이 추정한 정서. 사람 평정과 별도 범주이며, 사람 평정을 대체하는 근거로 쓰지 않는다. 쓸 때는 반드시 같은 지표로 잰 사람 간 일치도와 함께 보고한다.
* **G1 필요**: 원본 자극(비디오, 오디오)이 있어야 하는 분석. 사용자 확인으로 4개 데이터셋 모두 보유 상태이나, 표시는 유지한다.

---

## 0. 핵심 질문에 대한 작업 틀: 세 층 분해

핵심 질문은 "LLM이 표현하는 정서적 의미와 인간의 뇌가 표현하는 정서적 경험을 어떻게 구분하고 비교할 것인가"다. 문헌을 읽고 나서 다음 세 층으로 나누는 것이 가장 생산적이라고 판단했다.

| 층 | 내용 | LLM/MLLM이 근사하는 정도 (근거) | 측정 수단 |
|---|---|---|---|
| L1 기술 의미 (description) | 무엇이 보이고 일어나는가. 정서 단어를 쓰지 않은 장면 기술 | 높음. 캡션 LLM embedding이 고차 시각피질을 잘 설명 (Doerig2025). 정서 배제 캡션만으로 시청 내용 문장 생성 (MindCap2025) | 정서 배제 캡션의 sentence embedding, 시각 모델 feature |
| L2 귀속 또는 추론된 정서 의미 (attributed meaning, 3인칭 평균 관찰자) | 평균적 관찰자가 이 상황에서 추론할 정서와 appraisal | 비교적 높음. GPT-4는 21개 appraisal 중 20개에서 저자 본인보다 독자 평균과 더 일치 (TakGratch2024). GPT-4V 사회 특징 r 0.79 (SantavirtaV2025). Gemini 비디오별 정서 r 0.553, 범주 수준 GW 매칭 54.6% (Asanuma2025) | LLM/MLLM 출력 [AI-est], 관찰자 귀속 평정 [Attrib-human] |
| L3 경험된 정서 (experienced affect, 1인칭, 신체, 개인 특이) | 그 사람이 실제로 느낀 것, 신체 상태와 결합된 정서 | 낮음. 저자 자기평가와는 덜 일치 (TakGratch2024). 신체 기반 정서('두근거림')와 맥락 의존 비디오에서 실패 (Asanuma2025). Gemini 영화 특징이 insula를 거의 설명 못함 (LiM2026). 합성 뇌(TRIBE)에서 클립 간 정서 구조 손실 (EmoMind2026). 언어 단독 학습은 감각운동 차원 회복 실패 (Xu2025) | [Self], 생리 신호, 개인 수준 뇌 반응 |

**중요한 측정상의 함의.** Horikawa와 Emo-FilM의 정서 라벨은 별도 평정자의 경험 보고를 평균한 [Human-norm]이다. 평균한 1인칭 보고는 통계적으로 "평균 관찰자"와 가까워지므로, LLM이 이 라벨과 잘 맞는다는 결과(Asanuma2025, Du2025, SantavirtaE2025)는 LLM이 L3를 포착한다는 증거가 아니라 L2 수준의 증거로 읽어야 한다(TakGratch2024 Discussion의 관점 가설을 데이터셋 라벨 구조에 적용한 본 에이전트의 해석). L3를 직접 겨냥할 수 있는 자료는 Spacetop alignvideo [Self]와 Emo-FilM의 생리 신호, 그리고 개인 수준 뇌 반응뿐이다(Stage 1 보고서 3.2절).

**비교 방법의 다섯 가지 형식** (이후 절의 제안이 모두 이 중 하나 이상을 쓴다).

1. **중첩 기준선 분산 분할:** L1 feature ⊂ L1+L2 feature ⊂ L1+L2+L3 지표로 encoding을 쌓아 각 층의 고유 분산 지도를 만든다. 공선성 때문에 banded ridge와 고유 분산(unique variance) 추정을 쓰고, 해석은 "설명력의 증가"이지 "표상의 존재"가 아니다.
2. **구조 비교:** RSA와 Gromov-Wasserstein optimal transport(GWOT)를 함께 쓴다. 상관은 높아도 항목 수준 대응이 실패하는 경우를 구분하기 위해서다(Kawakita2024, Asanuma2025).
3. **관점 조작:** 같은 자극에 LLM을 "관찰자", "경험자", "특정 persona"로 prompt해 각 출력이 어떤 뇌 영역의 분산을 설명하는지 비교한다(TakGratch2024, SantavirtaV2025의 future direction).
4. **잔차 분석:** 인간 평정에서 LLM 예측을 뺀 잔차가 생리, insula, 개인차를 예측하는지 본다. 잔차의 귀무 분포는 인간 평정자 split 간 잔차로 만든다(라벨 noise와 구분하기 위해).
5. **In-silico 반사실:** 텍스트 순서나 비디오 일부를 바꾼 반사실 입력으로 LLM 회귀자가 어떻게 변하는지 본다. 참가자는 원 자극만 봤으므로 결과는 모델 쪽 예측이며 뇌의 인과 증거가 아니다.

---

## 1. 중요한 미해결 문제

### P1. 귀속(attribution)과 경험(experience)의 신경 분리
* 내용: 자연 영화 시청에서 정서 관련 영역(특히 우측 TPJ, MPFC)이 관객이 느낀 정서를 표상하는지, 인물에게 귀속한 정서를 표상하는지 분리되지 않았다. Lettieri2019는 주관 보고와 인물 정서의 상관 때문에 이를 결론 내릴 수 없다고 한계로 명시했다(Discussion 한계 셋째). Skerry2014(abstract)는 MPFC 일부에서 귀속과 경험의 부분 겹침을 보고했다.
* LLM 쪽 연결: LLM 정서 판단은 3인칭 평균 관찰자에 가깝다(TakGratch2024 Study 2). 따라서 LLM은 "귀속 쪽" 회귀자를 만드는 도구로 쓸 수 있지만, 경험 쪽 대리로는 약하다.
* 근거: doi:10.1038/s41467-019-13599-z, doi:10.1523/JNEUROSCI.1676-14.2014, arXiv:2408.13718

### P2. 정서 신경 표상과 장면 기술 의미의 혼동 (description confound)
* 내용: 캡션의 LLM embedding이 고차 시각피질을 잘 설명하며(Doerig2025), 정서 배제 캡션만으로 시청 내용을 문장화할 수 있다(MindCap2025). 그렇다면 Horikawa 데이터에서 보고된 정서의 분산 표상 중 얼마가 정서 고유 정보이고 얼마가 장면 의미의 재표현인지 모른다. Du2025의 "MLLM 표상이 인간 평정보다 뇌를 더 잘 설명한다"는 결과도 정서 배제 기술 기준선과 비교되지 않았다(본 에이전트가 본문에서 그런 통제를 찾지 못함). LLM 라벨을 쓴 decoding 연구는 의미 confound를 스스로 한계로 인정했다(arXiv:2606.07707 Limitations).
* 근거: doi:10.1038/s42256-025-01072-0, doi:10.1126/sciadv.adw1464, arXiv:2509.24298, arXiv:2606.07707
* overlap: EmoViS (affective brain geometry의 sensory-semantic 기원)

### P3. 맥락 의존 정서와 신체 기반 정서에서의 모델 실패가 뇌에서 무엇에 대응하는가
* 내용: MLLM은 단일 프레임으로 정서가 정해지는 비디오(아기, 동물, 공포 장면)에서는 잘 맞고, 맥락 반전이 있는 비디오와 '두근거림' 같은 신체 정서에서 실패한다(Asanuma2025 Results와 Discussion 넷째 단락). GPT-4V는 추론적, 추상적 사회 특징에서 일치도가 낮다(SantavirtaV2025 Discussion). Gemini 특징은 insula를 거의 설명하지 못한다(LiM2026 Conclusions). 이 "모델 실패 집합"이 뇌의 어떤 표상(내수용, 맥락 통합)과 대응하는지 검증된 적이 없다.
* 근거: doi:10.1038/s41598-025-14961-6, doi:10.1162/imag.a.134, doi:10.1162/imag.a.1300, arXiv:2605.16739, doi:10.1038/s41562-025-02203-8

### P4. 상황의 시간적, 인과적 구조를 담는 정서 표상
* 내용: appraisal 특징 공간이 ToM 네트워크의 정서 귀속 표상을 가장 잘 설명하지만, 평평한 특징 벡터는 "케이크를 먹고 다이어트를 다짐함"과 "다이어트를 다짐하고 케이크를 먹음"을 구분하지 못한다(Skerry2015 Discussion 'Characterizing Representational Spaces' 넷째 단락). 구조화된 생성 ToM 모형은 제한된 게임 맥락에서만 작동했고, 실세계 장면을 파싱하는 일반적 방법이 없다(Houlihan2023 Discussion). 비디오 의미역과 사건 관계 표현(arXiv:2104.00990), 상황 그래프(arXiv:1712.06761)는 컴퓨터 비전에 있으나 정서 신경과학에 연결되지 않았다.
* 근거: doi:10.1016/j.cub.2015.06.009, doi:10.1098/rsta.2022.0047, arXiv:2104.00990, arXiv:1712.06761

### P5. 모델 생성 정서 라벨의 측정 타당도
* 내용: LLM/MLLM 정서 주석의 근거가 빠르게 쌓이고 있지만(Asanuma2025, SantavirtaV2025, SantavirtaE2025), (a) 비디오 단위 일치가 시간 연속 일치를 보장하지 않고(arXiv:2502.04379, GameVibe 연속 engagement에서 대체로 실패), (b) 성적, 폭력 내용은 내용 필터로 수집 실패나 신경 대응 약화가 생기며(SantavirtaV2025 Limitations, Asanuma2025의 GPT-4V 응답률 23%), (c) LLM은 집단 평균을 내고 분산을 평탄화한다(arXiv:2402.01908 Discussion). (d) Cowen & Keltner 자극과 라벨은 2017년부터 공개되어(interactive map, Stage 1 보고서 7.6절 41번) 사전학습 오염 가능성이 있으나 이를 점검한 연구를 찾지 못했다. 일부 연구는 인간 검증을 "모델 라벨의 그럴듯함 점수"로 대신했다(arXiv:2606.07707, 평균 7.83/10).
* 근거: arXiv:2502.04379, doi:10.1162/imag.a.134, arXiv:2402.01908, arXiv:2606.07707, doi:10.1038/s41598-025-14961-6

### P6. "평균 관찰자" 모델과 개인 특이 정서의 관계
* 내용: LLM은 평균적 관찰자 관점을 학습했고(TakGratch2024), 집단을 평탄화한다(arXiv:2402.01908). 반면 Horikawa 재분석은 최소 가정에서 개인 간 변동이 크다고 보고했고(Westlin 2025, arXiv:2507.00320, 초록 기준), Miao2026은 ToM의 개인차를 다루지 못한 것을 한계로 들었다(Discussion 한계 첫째). EmoMind2026은 개인별 decoded affect가 범주 라벨이 전달하지 못하는 개인 특이 구조를 가진다고 보고했다. LLM 예측에서 벗어난 개인 보고와 뇌 반응이 같은 방향으로 벗어나는지는 검증되지 않았다.
* 근거: arXiv:2408.13718, arXiv:2402.01908, arXiv:2507.00320, doi:10.1038/s41467-026-71151-2, arXiv:2605.16739

### P7. 정서 의미의 언어, 문화 의존성과 개인 뇌 표상
* 내용: 정서 단어 의미는 언어 계통마다 다르고(valence, 생리적 활성화 축만 보편), 지리적 근접성이 그 변이를 예측한다(Jackson 2019, doi:10.1126/science.aaw8160 abstract). Du2025와 Kawakita2024는 문화, 언어 요인을 한계로 명시했다. Horikawa는 미국 MTurk 평정자의 라벨과 일본에서 촬영한 참가자 뇌의 조합인데(참가자 국적, 모국어는 Stage 1에서 미확인), 라벨 언어와 뇌의 언어가 다를 때 생기는 불일치를 다룬 연구가 없다.
* 근거: doi:10.1126/science.aaw8160, arXiv:2509.24298 (Limitations), doi:10.1038/s41598-024-65604-1 (Discussion 셋째 단락)

---

## 2. 주목해야 할 모델과 방법론

라이선스와 가중치 공개 여부는 이번 세션에서 직접 확인한 것과 사전 지식을 구분했다. "사전 지식"은 이번에 원문을 열어 확인하지 않았다는 뜻이며 Stage 4 전에 재확인해야 한다.

| # | 모델 / 방법 | Pretrained weights 공개 | Input / Output | 학습 목표 | 라이선스 | 이 연구에서의 역할과 근거 |
|---|---|---|---|---|---|---|
| M1 | 공개 가중치 비디오 MLLM (Qwen2.5-VL, InternVL 계열 등) | 공개 (사전 지식) | 비디오 프레임 + 텍스트 prompt / 텍스트(평정, 기술), hidden state | 대규모 이미지-텍스트, 비디오-텍스트 생성 사전학습 + instruction tuning | 크기별로 다름(일부 Apache-2.0, 일부 자체 라이선스, 사전 지식, 확인 필요) | 재현 가능한 [AI-est] 주석과 hidden state 추출. 폐쇄 모델 버전 변동 문제 회피. Asanuma2025에서 공개 모델(Molmo-7B-D)은 폐쇄 모델보다 크게 낮았다(비디오별 r 0.21 vs 0.553)는 점을 감안해야 함 |
| M2 | 폐쇄 MLLM (Gemini 2.x, GPT-4.1, GPT-4o 등) | 비공개 (API) | 비디오 또는 frame + prompt / 텍스트 | 비공개 | 상용 API 약관 | 사람 평정과의 일치 근거가 가장 많다(Asanuma2025, SantavirtaV2025, SantavirtaE2025, LiM2026). 내용 필터, 버전 교체, 내부 접근 불가가 약점 |
| M3 | 공개 LLM + 기계적 해석 도구 (Llama 3.x, Gemma 2 등에 linear probe, activation patching, appraisal 방향 steering) | 공개 | 텍스트 / hidden state, 조작된 출력 | 다음 토큰 예측 + instruction tuning | Llama Community License, Gemma Terms 등(사전 지식) | Tak2025가 중간층 MHSA에서 appraisal 방향을 찾고 steering으로 출력 정서를 바꿨다. 서사 텍스트의 문장별 appraisal 궤적을 뇌 회귀자로 만들 수 있다. 정서 '표현' 회로는 arXiv:2510.11328(코드 공개, GitHub) |
| M4 | 문장 encoder (DeBERTa-large, RoBERTa-large, MPNet 계열) | 공개 | 텍스트 / 문장 embedding | masked LM 또는 문장 유사도 학습 | MIT 등(사전 지식) | L1 기술 기준선. MindCap2025가 DeBERTa-large feature로 decoder를 학습했고, Doerig2025가 캡션 embedding으로 NSD를 설명 |
| M5 | Triplet odd-one-out embedding (SPoSE 계열) | 방법(코드 공개 여부 미확인) | 대규모 triplet 선택 / 희소 비음수 embedding | 선택 확률의 likelihood 최대화 + 희소성 | 미확인 | Du2025가 MLLM과 LLM에서 7,125,330 triplet을 받아 30차원 정서 공간을 만들었다. 평정 척도의 사전 구조를 피하는 장점. 인간 triplet 직접 수집은 아직 없음(Du2025 Limitations) |
| M6 | Gromov-Wasserstein optimal transport 비지도 정렬 | 방법(툴박스 공개, 라이선스 미확인) | 두 거리 행렬 / 수송 계획, 매칭률 | entropic GW 거리 최소화 | 미확인 | 상관과 항목 수준 대응의 차이를 드러낸다. Kawakita2024(색, GPT-4 91.4% vs RGB 5.38%), Asanuma2025(정서, 항목 1.69% vs 범주 54.6%). 뇌 RSM까지 포함한 3자 정렬로 확장 가능 |
| M7 | Bayesian inverse planning ToM + appraisal 계산 (neurosymbolic) | 모형(코드 공개 여부 미확인) | 상황 변수 / 추론된 선호, 믿음, appraisal, 정서 예측 | 생성 모형의 Bayesian 역추론 | 미확인 | Houlihan2023. LLM을 상황 파서로, 구조화 모형을 추론 엔진으로 결합하면 "순수 LLM embedding" 대비 해석 가능한 대안 회귀자 |
| M8 | 비디오 상황 표현 (VidSitu식 의미역과 사건 관계, MovieGraphs식 상황 그래프) | 데이터와 기준 모델 공개(세부 라이선스 미확인) | 비디오 / 동사, 의미역, 사건 관계, 인물-관계-정서 그래프 | 지도 학습 | 미확인 | P4 해결 재료. 현재는 MLLM으로 같은 형식의 그래프를 생성하고 일부를 사람이 검증하는 경로가 현실적 |
| M9 | 정서 특화 MLLM (AffectGPT, Emotion-LLaMA) | 코드 공개, 가중치 공개 여부는 모델별 확인 필요 | 오디오+비디오+텍스트 / 개방 어휘 정서 기술, 범주 | 정서 instruction tuning | AffectGPT의 MER-Caption 데이터 CC BY-NC 4.0(논문에서 확인), 모델 라이선스 미확인 | 인물 표정과 음성 기반 portrayed emotion 주석기 후보. 관객 경험 정서와 다른 범주로 표기 |
| M10 | LLM 사건 분할과 예측 신호 (prompt 기반 사건 경계, 토큰 surprisal, 서사 예측 분포) | 공개 LLM으로 재현 가능 | 텍스트 / 경계, surprisal, 예측 분포 | 다음 토큰 예측 | 모델에 따름 | Michelmann2025는 GPT-3 경계가 개별 인간보다 합의에 가깝다고 보고. Antony 2021(doi:10.1016/j.neuron.2020.10.029)의 belief-inconsistent surprise를 서사로 옮기는 데 사용 |

**모델 선택 원칙(제안).** 재현성과 내부 표상 접근을 위해 공개 가중치 모델을 주력으로 쓰고, 폐쇄 모델은 "사람 일치도 상한 참고"로만 쓴다. 이유: Strachan 2024(doi:10.1038/s41562-024-01882-z, Discussion 마지막 단락)와 Xu2025(Discussion 다섯째 단락)가 폐쇄 모델의 불투명성을 과학적 한계로 명시했고, Strachan 2024는 출력 행동(performance)과 내부 능력(competence)이 다를 수 있음을 보였다.

---

## 3. 다른 분야에서 가져오거나 다른 분야로 보낼 수 있는 연구 아이디어

### I1. "Silicon sample"에서 "silicon rater"로: 관점 조건부 정서 주석과 평탄화 측정 (Computational Social Science → Affective Neuroscience)
* 아이디어: 사회과학의 LLM 참가자 대체 논의(arXiv:2402.01908)와 SantavirtaV2025의 future direction(persona 부여)을 가져와, 같은 자극에 대해 "관찰자", "경험자", "특정 개인 특성 persona" 조건으로 정서를 주석하게 한다. 각 조건 출력의 분산이 인간 평정자 분산보다 얼마나 작은지(평탄화 지수)를 재고, 뇌 반응 설명력과 함께 보고한다.
* 데이터: Spacetop alignvideo [Self]는 개인별 보고가 있어 평탄화를 직접 잴 수 있다(약 51% 결측 주의). Emo-FilM은 평정자별 원자료가 있어 평정자 분산과 비교 가능.
* 근거: arXiv:2402.01908, doi:10.1162/imag.a.134, arXiv:2408.13718

### I2. 컴퓨터 비전의 상황 인식(situation recognition)을 정서 encoding feature로
* 아이디어: VidSitu(의미역, 사건 관계)와 MovieGraphs(인물, 관계, 상호작용, 정서, 동기 그래프)의 표현 형식으로 Horikawa 클립과 Emo-FilM 장면을 MLLM이 그래프화하게 하고, 그래프 feature(누가 누구에게 무엇을 했고 결과가 무엇인가)를 encoding에 넣는다. 장면 전체 정서 라벨이 아니라 관계 구조가 ToM 네트워크와 정서 영역 분산을 설명하는지 본다.
* 근거: arXiv:2104.00990, arXiv:1712.06761, doi:10.1016/j.cub.2015.06.009(평평한 특징 벡터의 한계)

### I3. 색 지각 연구의 비지도 정렬을 정서 3자 정렬로
* 아이디어: Kawakita2024가 인간과 GPT의 색 유사도 구조를 GWOT로 비교한 방식을 정서로 옮겨, 뇌 RSM(참가자별), 인간 규범 평정 RSM, LLM RSM의 세 쌍을 모두 정렬한다. "LLM-인간 평정은 정렬되지만 LLM-뇌는 범주 수준에서만 정렬된다" 같은 비대칭 패턴이 L2와 L3의 차이를 진단한다.
* 근거: doi:10.1038/s41598-024-65604-1, doi:10.1038/s41598-025-14961-6

### I4. 사건 인지와 스포츠 분석의 예측 신호를 서사 정서로
* 아이디어: Antony 2021의 승리 확률 모델 자리에 LLM의 서사 예측 분포를 넣어 문장별 belief-consistent surprise와 belief-inconsistent surprise를 계산하고, LLM 사건 경계(Michelmann2025)와 함께 Spacetop narratives의 정서 평정과 BOLD에 대응시킨다. 단순 surprisal이 아니라 "주인공 운명에 대한 믿음 갱신"을 계산하는 것이 핵심이다.
* 근거: doi:10.1016/j.neuron.2020.10.029, doi:10.3758/s13428-024-02569-z, doi:10.1038/s41467-026-71151-2

### I5. 기계적 해석 가능성(mechanistic interpretability)의 개입을 뇌 encoding의 모델 쪽 ablation으로
* 아이디어: Tak2025의 appraisal 방향 steering과 arXiv:2510.11328의 정서 회로 ablation을 이용해, LLM hidden state에서 특정 appraisal 방향을 제거했을 때 뇌 encoding 성능이 어느 영역에서 얼마나 떨어지는지 본다. 이는 뇌의 인과가 아니라 "어떤 모델 정보가 뇌 예측에 필요한가"에 대한 모델 쪽 인과 검정이다(CLAUDE.md 6절의 decodability vs causality 구분).
* 근거: arXiv:2502.05489, arXiv:2510.11328, doi:10.1016/j.isci.2024.111401

### I6. 반대 방향: 뇌 유래 정서 기하를 AI 정서 정렬의 평가 기준으로 (Affective Neuroscience → AI 평가)
* 아이디어: MLLM의 "정서 정렬"을 사람 평정 일치도만으로 평가하지 않고, 뇌 RSM과의 항목 수준 정렬(GWOT 매칭률)을 추가 기준으로 쓴다. 내용 필터가 걸리는 범주(sexual desire, horror 등)에서 안전 정렬이 정서 표상을 어떻게 왜곡하는지 base 모델과 instruct 모델을 비교해 측정할 수 있다.
* 근거: arXiv:2509.24298(Discussion 'Broad applications'), doi:10.1162/imag.a.134(Limitations, 내용 필터), arXiv:2605.16739

### I7. 게임 정동 컴퓨팅의 시간 연속 검증 프로토콜을 영화 fMRI로
* 아이디어: arXiv:2502.04379가 시간 연속 engagement 예측에서 LLM이 대체로 실패했다는 결과를 출발점으로, Emo-FilM 1 Hz consensus [Human-norm]에 대해 MLLM 연속 주석의 시간 해상도별 일치도 곡선(1 s, 5 s, 장면 단위)을 만든다. 일치도가 인간 평정자 간 수준(평균 r 0.38~0.39)에 도달하는 최소 시간 척도를 찾아, 그보다 짧은 척도의 AI 시계열은 뇌 분석에 쓰지 않는 규칙을 세운다.
* 근거: arXiv:2502.04379, Stage 1 보고서 5.3 #3

---

## 4. 기존 Affective Neuroscience와 예상 밖으로 연결될 수 있는 개념

### U1. "정서의 Molyneux 문제": 기술만으로 회복되는 정서 성분과 회복되지 않는 성분
* 출발: Xu2025는 언어 단독 학습이 valence와 arousal은 회복하지만 감각운동 차원, 특히 운동 차원은 회복하지 못함을 보였다. Platonic Representation Hypothesis(arXiv:2405.07987)는 양식마다 고유 정보가 있으면 표상이 수렴할 수 없다고 한계를 적었다('Counterexamples and limitations').
* 연결: Emo-FilM의 CPM 성분(Appraisal, Motivation, Feeling, Motor expression, Physiology)을 "언어로 회복 가능성"의 축으로 재배열한다. 예측: LLM-인간 일치도는 Appraisal > Feeling > Motivation > Expression, Physiology 순이며, 일치도가 낮은 성분의 뇌 상관(insula, 체성감각, 뇌간)은 LLM 회귀자로 설명되지 않는다. 정서 이론 논쟁(구성주의의 개념 지식 역할 vs 신체 기반 이론)에 직접 연결된다(Li2024 Discussion 둘째 단락).

### U2. LLM의 "확정 회피(hyperconservatism)"와 인간의 정서적 해석 확정
* 출발: Strachan 2024는 GPT 모델이 사회적 불확실성에서 결론을 확정하지 않는 반면 인간은 불확실성을 혐오하고 가설에 확정한다고 해석했다(Discussion 다섯째~여섯째 단락).
* 연결: 평정자 간 엔트로피가 높은 모호한 Horikawa 클립에서 (a) 인간 평정 엔트로피, (b) LLM 출력 분포 엔트로피, (c) 참가자 간 뇌 패턴 일치도를 비교한다. 인간 뇌가 모호 자극에서도 개인별로 서로 다른 해석에 "확정"한다면 참가자 간 일치는 낮고 참가자 내 패턴은 날카로울 것이다. Westlin 2025가 본 큰 개인 간 변동(arXiv:2507.00320)을 "해석 확정의 개인차"로 다시 읽을 수 있는지 묻는 연결이다(탐색적).

### U3. 규범 평정은 이미 "3인칭"이다
* 출발: TakGratch2024는 GPT-4가 평균 관찰자 관점이라고 보였다. Asanuma2025는 Gemini-인간 비디오별 상관이 인간 집단 간 상관보다 약간 높다고 보고했다(Koide-Majima 자료).
* 연결: 평균한 1인칭 보고(규범 평정)는 정의상 개인 경험의 공통 성분이고, 이것이 LLM이 학습한 "언어 공동체의 평균 관찰자"와 수렴한다. 그렇다면 "LLM 예측과 개인 보고의 차이"는 라벨 noise가 아니라 개인 특이 경험의 측정치일 수 있다. 이 차이를 개인 뇌 반응의 개인 특이 성분(hyperalignment 잔차)과 연결하는 것이 새 질문이다(체인 5).

### U4. 영화 편집 이론(Kuleshov 효과)을 모델 평가와 뇌 encoding의 공통 탐침으로
* 출발: Mobbs 2006(doi:10.1093/scan/nsl014)은 같은 얼굴이 선행 맥락에 따라 다르게 귀속되고 편도체, STS, 측두극 반응이 달라짐을 보였다. ChenWhitney2019는 인물을 가려도 맥락만으로 정서를 추적할 수 있음을 보였다.
* 연결: 생성 편집으로 Kuleshov 쌍과 인물 제거 프레임을 만들어 MLLM과 영상 encoding 모델(in-silico)에 넣고 "맥락 민감도"를 측정한 뒤, 그 민감도가 높은 클립에서 실제 뇌 반응의 어떤 영역이 맥락 쪽 회귀자를 따르는지 본다. 영화학의 편집 원리가 AI 평가와 뇌 분석을 잇는다.

### U5. 언어 공동체의 정서 의미 네트워크(colexification)와 개인 뇌 RSM
* 출발: Jackson 2019는 언어 계통별 정서 의미 네트워크 차이와 보편 축(valence, 활성화)을 보였다.
* 연결: 다국어 LLM으로 같은 비디오를 일본어와 영어로 정서 기술하게 하면 "언어 공동체 의미"의 차이를 자극 수준에서 계산할 수 있다. 이것이 참가자 뇌 RSM과의 정렬을 바꾼다면, 구성주의 이론이 말하는 "개념 지식이 정서 경험을 구성한다"는 주장의 집단(collective) 수준 검증이 된다(체인 6).

---

## 5. 새 Sub-axis 또는 하위 연구 방향

| # | 이름 | 속할 Axis | 독립 Axis 필요 여부 | 정의와 근거 |
|---|---|---|---|---|
| S1 | Attribution-Experience Gap (관점: 1인칭 vs 3인칭) | C (A, Q와 교차) | 불필요. 기존 "Perceived Meaning vs Experienced Emotion"을 이것과 S3로 쪼갠다 | 같은 장면에서 인물에게 귀속한 정서와 관객이 느낀 정서의 차이, 그리고 측정 도구(LLM, 규범 평정, 본인 보고)의 관점 차이. arXiv:2408.13718, doi:10.1038/s41467-019-13599-z |
| S2 | Situation Structure & Relational Semantics | C (B와 교차) | 불필요 | 인물, 관계, 목표, 행동의 의미역과 사건 간 인과, 시간 순서. 평평한 appraisal 벡터의 한계를 넘는 표현. doi:10.1016/j.cub.2015.06.009, arXiv:2104.00990, arXiv:1712.06761, doi:10.1098/rsta.2022.0047 |
| S3 | Description Residual (기술로 환원되지 않는 정서) | C (P, F와 교차) | 불필요 | 정서 배제 기술(L1)을 통제한 뒤 남는 정서 관련 신경 분산. doi:10.1038/s42256-025-01072-0, doi:10.1126/sciadv.adw1464 |
| S4 | Machine Raters & Annotation Provenance (모델 생성 주석의 측정 이론) | Q (모든 Axis와 교차) | **독립 Axis 후보로 제안**(아래 이유) | 모델 주석의 관점, 평탄화, 내용 필터, 사전학습 오염, 시간 해상도 타당도, 버전 변동을 다루는 측정 이론. arXiv:2402.01908, arXiv:2502.04379, doi:10.1162/imag.a.134, doi:10.1038/s41598-025-14961-6 |
| S5 | Social Primitives & Pre-reflective Inference | C (E와 교차) | 불필요 | 명시적 mentalizing 없이 사회적 상호작용의 존재만으로 ToM 영역이 동원되는 현상. 정서 귀속의 전단계. doi:10.1038/s41467-026-71151-2(Discussion 넷째 단락) |
| S6 | Collective and Cultural Emotion Semantics | C (O와 교차, 외부 분야 Social and Collective Behavior) | 불필요 | 언어 공동체 수준의 정서 의미 구조가 개인 정서 표상에 미치는 영향. doi:10.1126/science.aaw8160 |
| S7 | Narrative Prediction Signals (모델 유래 예측 신호의 유형 구분) | C (D, N과 교차) | 불필요. 기존 "Emotional Expectation", "Surprise / Prediction Error"를 재정의 | 토큰 surprisal, 사건 경계, belief-consistent/inconsistent surprise, suspense(불확실성)를 출처 모델과 함께 구분. doi:10.1016/j.neuron.2020.10.029, doi:10.3758/s13428-024-02569-z |

**S4를 독립 Axis로 제안하는 이유.** NSD의 정서 분석은 거의 전적으로 AI 추정 라벨에 의존하고(Stage 1 G3 판정), Spacetop의 시간 해상 분석도 AI 시계열에 의존한다(Stage 1 보고서 5.3 #3). 즉 모델 주석의 타당도가 여러 Axis(A, G, H, O, S)의 결론을 동시에 좌우한다. 기존 Q의 "Inter-rater Reliability", "Subjective vs Normative Labels"는 사람 평정자를 전제로 해서 모델 고유 문제(관점, 필터, 오염, 버전)를 담지 못한다. 다만 Q와 경계가 겹치므로, 독립 Axis로 둘지 Q의 큰 Sub-axis로 둘지는 Coordinator가 다른 에이전트(특히 emotion-theory의 Q 담당) 의견과 함께 판단하기를 권한다.

---

## 6. Discussion-to-Research Chains

각 체인은 `Original Finding → Unresolved Question → Technological Development → New Dataset / Model Combination → New Research Question` 순서다. 각 단계 끝에 근거 ID와 원문 위치를 단다. 마지막에 검증 논리, 위험, G1, overlap, 선행 수행 여부를 붙인다.

### Chain 1. 정서 배제 기술의 잔차: Horikawa에서 "정서" 신호는 장면 의미를 넘어서는가

* **Original Finding:** 장면 캡션의 LLM embedding이 고차 시각 영역 반응과 정렬되며 그 성공은 캡션 전체 정보 통합에서 온다 [doi:10.1038/s42256-025-01072-0, Discussion 첫째 단락]. 같은 계열 비디오에서 정서를 배제하도록 지시받은 캡션의 LM feature만으로 언어 네트워크 밖에서 구조화된 의미를 decoding했다 [doi:10.1126/sciadv.adw1464, Discussion 첫째 단락과 한계 논의 첫 단락].
* **Unresolved Question:** LLM embedding이 시각 처리의 어떤 다른 측면까지 포착하는지 평가가 필요하다 [doi:10.1038/s42256-025-01072-0, Discussion 둘째 단락]. 캡션이 정서와 인상을 담지 않아 생성 문장에 정서가 거의 없었다 [doi:10.1126/sciadv.adw1464, 한계 논의 첫 단락]. 그렇다면 Horikawa 뇌 반응 중 정서 평정이 설명하는 분산은 기술 의미를 넘어서는가? MLLM 표상이 인간 평정보다 뇌를 더 잘 설명했다는 결과 [arXiv:2509.24298, Discussion 첫째 단락]도 기술 기준선 대비 해석이 필요하다.
* **Technological Development:** 문장 encoder와 LLM embedding의 뇌 정렬(M4), MLLM 정서 추정의 비디오 단위 일치 근거(Gemini 비디오별 r 0.553, 범주 수준 GW 54.6%) [doi:10.1038/s41598-025-14961-6, Results Table 4와 Discussion 첫째 단락], banded ridge 분산 분할.
* **New Dataset / Model Combination:** Horikawa fMRI(5명, 비디오 블록 평균) + 비디오당 20개 정서 배제 캡션(L1) [이용 가능 여부 미확인. Du2025와 EmoMind2026이 사용] + Cowen & Keltner 34범주, 14차원 [Human-norm] + 공개 MLLM의 34범주 추정 [AI-est] + 시각 모델 feature.
* **New Research Question:** "Horikawa 참가자의 뇌 반응에서 인간 규범 정서 평정이 정서 배제 캡션의 LLM embedding과 시각 feature를 넘어 설명하는 고유 분산은 어느 영역에 있으며, 그 지도는 MLLM 정서 추정의 고유 분산 지도와 겹치는가, 갈라지는가?"
* **검증 논리:** (a) 정서 고유 분산이 거의 0이면 "Horikawa의 분산된 정서 표상은 장면 의미의 재표현"이라는 해석이 지지된다. (b) 고유 분산이 insula, 편도체, vmPFC, 피질하에 남고 MLLM 고유 분산은 DMN/TPJ에 남는다면 L2(귀속 의미)와 L3(경험 관련) 성분이 공간적으로 갈린다는 증거다. (c) 두 지도가 같으면 MLLM이 인간 규범 평정의 정서 고유 성분을 근사한다는 뜻이다. 어느 결과든 해석 가능하다.
* **위험과 통제:** 반복 제시가 없어 noise ceiling 불가(Stage 1) → 참가자 간 예측 상한으로 대체. 같은 원본에서 잘린 클립의 movie-level leakage 미확인 → 원본 단위 fold. 캡션 품질과 정서 단어 누출 → 캡션에서 정서 어휘를 사전으로 검사. Cowen & Keltner 자극의 사전학습 오염 → MLLM에 출처와 범주명을 묻는 누출 탐침, 좌우 반전과 crop 변형에서 출력 안정성 비교(탐색적 점검).
* **G1:** 캡션 경로는 캡션 확보 시 불필요, MLLM 경로는 필요(보유).
* **선행 수행:** partially. Du2025가 MLLM, LLM(캡션 입력), 인간 평정의 뇌 설명력을 비교했지만 정서 배제 기술을 nuisance로 둔 잔차 분석은 본문에서 확인하지 못했다. Kiyokawa2024는 범주 수준(15x15)만 비교했다.
* **overlap: EmoViS** (affective brain geometry의 sensory-semantic 기원과 직접 겹침)

### Chain 2. 귀속 vs 경험: 영화 속 인물의 정서와 관객의 정서는 다른 곳에 표상되는가

* **Original Finding:** 우측 TPJ에 정서 차원 gradient(emotionotopy)가 있다 [doi:10.1038/s41467-019-13599-z, Discussion 둘째 단락]. GPT-4는 21개 appraisal 중 20개에서 경험자 본인보다 3인칭 독자 평균과 더 일치한다 [arXiv:2408.13718, Study 2 A절 마지막 두 단락].
* **Unresolved Question:** TPJ 지형이 주관 경험을 부호화하는지 정서 귀속을 부호화하는지 분리할 수 없었다 [doi:10.1038/s41467-019-13599-z, Discussion 한계 셋째]. LLM은 개인 변산을 반영하지 못한다 [arXiv:2408.13718, Study 2 A절].
* **Technological Development:** MLLM이 동적 장면의 사회 특징을 인간 평균과 r 0.79로 주석 [doi:10.1162/imag.a.134, Discussion 4.1절]. 정서 특화 MLLM의 인물 표현 정서 기술 [arXiv:2501.16566, Conclusion]. 관점 조건부 prompt(관찰자 vs 경험자).
* **New Dataset / Model Combination:** Emo-FilM 1 Hz 50항목 [Human-norm, 평정자 본인 경험] + MLLM의 인물별 표현 정서 시계열 [AI-est, portrayed] + MLLM의 "관객이 느낄 정서" 예측 [AI-est] + 소규모 신규 인간 귀속 평정(인물 정서, 검증용 [Attrib-human], 수집 필요) + fMRI 30명과 생리. Emo-FilM에는 transcript가 없어 대사는 ASR로 만들고 [AI-est 전사]로 표기.
* **New Research Question:** "Emo-FilM 시청 중 인물에게 귀속된 정서와 관객이 경험한 정서가 서로 어긋나는 구간(예: 인물은 공포, 관객은 연민이나 서스펜스)에서, TPJ와 dmPFC는 귀속 쪽 회귀자를, insula, 편도체, vmPFC는 경험 쪽 회귀자를 더 따르는가?"
* **검증 논리:** 두 회귀자가 대부분 시간에 상관하므로 불일치 구간이 진단적이다. 불일치 구간에서도 두 영역군이 같은 회귀자를 따르면 "귀속과 경험의 공통 표상" 가설이 지지된다. MLLM 귀속 시계열의 타당도는 소규모 인간 귀속 평정과의 일치도가 인간 간 일치 수준에 이를 때만 인정한다.
* **위험:** 평정자는 같은 영화를 최대 6번 봤다(Stage 1). HRF 지연과 1 Hz 평정의 반응 지연. 영화 14편뿐이라 영화 수준 confound → leave-one-film-out. 경험 평정이 [Self]가 아니라 [Human-norm]이므로 "개인 경험"이 아니라 "규범 경험"으로 해석을 제한.
* **G1:** 필요(보유).
* **선행 수행:** no (검색 범위 내).
* **overlap: Emo-FilM 연구** (정서 맥락의 기여를 사전학습 멀티모달 encoding으로 분석하는 계획과 부분 겹침)

### Chain 3. 서사 속 appraisal 궤적: LLM 내부 appraisal 방향이 ToM 네트워크의 하위 과정을 나누는가

* **Original Finding:** 정서 귀속의 신경 유사도 구조는 38개 abstract event feature가 가장 잘 설명한다 [doi:10.1016/j.cub.2015.06.009, Discussion 첫째~넷째 단락]. LLM 중간층에 appraisal 개념 방향이 있고 steering으로 출력 정서가 이론대로 이동한다 [arXiv:2502.05489, Discussion]. 서사 속 사회적 상호작용 처리와 ToM은 ToM 영역에서 겹친다 [doi:10.1038/s41467-026-71151-2, Discussion 첫째 단락].
* **Unresolved Question:** 특징을 텍스트에서 직접 추론하고 사건의 인과, 시간 순서를 담는 표상이 필요하다 [doi:10.1016/j.cub.2015.06.009, Discussion 'Characterizing' 셋째, 넷째 단락]. appraisal과 정서의 인과 방향, 그리고 신경과학과의 연결이 미해결이다 [arXiv:2502.05489, Limitations 둘째 단락]. ToM의 하위 과정이 분리되지 않았다 [doi:10.1038/s41467-026-71151-2, Discussion 한계 셋째].
* **Technological Development:** 공개 LLM의 linear probe와 steering(M3), 덜 제약된 상황에서 appraisal을 계산할 일반 방법의 부재를 메울 LLM 파서(M7) [doi:10.1098/rsta.2022.0047, Discussion Module (2) 마지막 단락].
* **New Dataset / Model Combination:** Spacetop narratives(텍스트 4편, 오디오 4편, fMRI 참가자 good-bad 감정과 기대 평정 [Self]) + Miao2026의 연속 ToM과 사회적 상호작용 평정 [Attrib-human, 별도 평정자 231명, 공개 여부 미확인] + 공개 LLM의 문장별 appraisal 방향 투영값 [AI-est].
* **New Research Question:** "Spacetop 서사에서 LLM 내부 appraisal 방향(other-agency, goal conduciveness, expectedness 등)에 투영한 문장별 궤적은, 인간 연속 ToM 평정, 사회적 상호작용 평정, sentiment를 통제한 뒤에도 ToM 영역 BOLD를 설명하며, 그 설명이 텍스트판과 오디오판에서 같은 지도를 보이는가?"
* **검증 논리:** 고유 분산이 없으면 LLM appraisal 공간은 인간 ToM 평정의 재표현이다. 특정 appraisal(예: other-agency)이 TPJ, 다른 appraisal(예: expectedness)이 다른 영역을 설명하면 ToM 하위 과정 분리의 근거가 된다. 텍스트-오디오 일반화로 양식 confound를 줄인다. steering으로 만든 반사실 서사는 in-silico 예측에만 쓰고 결론은 "모델이 예측한 차이"로 제한한다.
* **위험:** 서사 8편이라 이야기 수준 일반화가 약하다. LLM 확정 회피 등 출력 행동과 내부 표상의 차이 [doi:10.1038/s41562-024-01882-z, Discussion] → 출력이 아니라 hidden state 사용. 다중 비교(appraisal 수 x 영역).
* **G1:** 텍스트 경로는 서사 텍스트가 필요(Spacetop stimuli 보유). 오디오 경로는 오디오 필요.
* **선행 수행:** no (검색 범위 내). Skerry2015 자극에 GPT-4 appraisal을 적용한 행동 연구(arXiv:2408.13718)는 있으나 fMRI 연결은 확인하지 못했다.

### Chain 4. 신체 잔차: MLLM이 놓치는 정서는 생리와 insula에 있는가

* **Original Finding:** MLLM은 '두근거림' 같은 신체 기반 정서와 맥락 의존 비디오에서 실패한다 [doi:10.1038/s41598-025-14961-6, Discussion 넷째 단락(arXiv v2)]. Gemini 영화 특징은 insula, 체성감각, 이상피질을 거의 설명하지 못한다 [doi:10.1162/imag.a.1300, Conclusions]. 언어 단독 학습은 감각운동 차원을 회복하지 못한다 [doi:10.1038/s41562-025-02203-8, Discussion 첫째~셋째 단락].
* **Unresolved Question:** 저자는 내수용 신호 통합 또는 정서-장면 연합 데이터 미세조정을 제안했다 [doi:10.1038/s41598-025-14961-6, Discussion 넷째, 다섯째 단락]. 합성 뇌가 클립 간 정서 구조를 잃는 이유로 내수용, 맥락, 개인 특이 신호를 지목했다 [arXiv:2605.16739, Discussion 첫째 단락]. 모델이 놓친 부분이 실제 신체 신호와 대응하는지는 검증되지 않았다.
* **Technological Development:** MLLM의 시간 연속 주석과 그 검증 방식 [arXiv:2502.04379, Limitations], 평정자별 원자료로 만드는 라벨 noise 귀무분포.
* **New Dataset / Model Combination:** Emo-FilM 50항목 1 Hz [Human-norm](Physiology 5, Motor expression 5, Feeling 7 등 CPM 성분) + 같은 50항목의 MLLM 1 Hz 추정 [AI-est] + fMRI 참가자의 PPG, 호흡, EDA(1000 Hz) + fMRI.
* **New Research Question:** "Emo-FilM에서 MLLM과 인간 규범 평정의 일치도가 가장 낮은 CPM 성분은 Physiology와 Motor expression인가, 그리고 인간 평정에서 MLLM 예측을 뺀 잔차 시계열이 평정자 split 간 잔차(라벨 noise 귀무분포)보다 fMRI 참가자의 심박, EDA, insula와 뇌간 BOLD를 더 잘 예측하는가?"
* **검증 논리:** 잔차가 라벨 noise라면 split 간 잔차와 같은 수준으로만 생리를 예측해야 한다. 잔차가 귀무분포보다 유의하게 생리와 insula를 예측하면 "언어화 가능한 정서 의미(L2) 밖의 신체 성분(L3)"의 증거다. 반대로 Physiology 성분의 일치도가 낮지 않다면 U1의 예측(언어로 회복 불가한 신체 성분)이 기각된다.
* **위험:** 평정자와 fMRI 참가자가 다른 사람이라 생리-평정 주체 불일치(Stage 1). 평정은 평정자 내 z-score라 절대 강도 비교 불가. 생리 신호의 HRF 아닌 고유 시간 지연. 시간 해상도별 MLLM 일치도를 먼저 확인(I7).
* **G1:** 필요(보유).
* **선행 수행:** no (검색 범위 내).
* **overlap: Emo-FilM 연구** (부분: 같은 데이터, 정서 맥락 기여 분석과 일부 겹칠 수 있음)

### Chain 5. "평균 관찰자" 잔차를 개인 특이 경험의 지표로

* **Original Finding:** GPT-4는 평균적 3인칭 관찰자 관점을 학습했다 [arXiv:2408.13718, Study 2 논의와 Ethical Impact Statement 앞 단락]. LLM은 집단을 오표상하고 평탄화한다 [arXiv:2402.01908, Discussion 첫째 단락]. Horikawa 최소 가정 재분석에서 개인 간 변동이 컸다 [arXiv:2507.00320, abstract].
* **Unresolved Question:** 개인 수준에서 ToM이나 정서 관여를 측정하고 신경 활동과 잇는 방법이 필요하다 [doi:10.1038/s41467-026-71151-2, Discussion 한계 첫째]. LLM의 개인 변산 미반영 [arXiv:2408.13718]. 개인 특이 decoded affect의 가치 [arXiv:2605.16739, Conclusion].
* **Technological Development:** MLLM 영상 정서 예측(집단 독립적인 평균 관찰자 기준), functional alignment와 shared response model.
* **New Dataset / Model Combination:** Spacetop alignvideo 49편, 7차원 [Self](결측 약 51%) + MLLM 예측 [AI-est] + 같은 영상의 leave-one-out 집단 평균 [Self 집계] + fMRI(같은 영상, 같은 순서).
* **New Research Question:** "Spacetop 참가자의 영상별 자기보고가 MLLM 예측(평균 관찰자 대리)에서 벗어나는 정도는, functional alignment 후 그 참가자 뇌 반응에 남는 개인 특이 성분의 크기와 방향을 예측하는가?"
* **검증 논리:** 먼저 MLLM 예측이 leave-one-out 집단 평균과 얼마나 같은지 보고한다(같다면 MLLM은 집단 평균의 외부 대리이며 순환 없이 쓸 수 있다는 장점만 남는다). 개인 편차와 뇌 개인 특이 성분 사이에 관계가 없으면 "보고상 개인차는 신경 개인차와 무관"이라는 결과이고, 관계가 있으면 개인 특이 정서 경험의 신경 지표 후보가 된다.
* **위험:** 결측이 클릭 저장 구조에서 생겨 무작위 결측이 아닐 수 있다(Stage 1). 평정 행위가 영상 끝 HRF와 겹친다. 49개 영상의 작은 독립 표본.
* **G1:** 필요(보유).
* **선행 수행:** no (검색 범위 내).

### Chain 6. 정서 의미의 언어: 일본어로 기술한 정서와 영어로 기술한 정서 중 무엇이 Horikawa 뇌와 더 맞는가

* **Original Finding:** MLLM triplet embedding이 정서 네트워크를 잘 예측했으나 자극과 모델의 서구 문화 편향을 저자가 한계로 들었다 [arXiv:2509.24298, Limitations 둘째 단락]. GWOT는 상관이 놓치는 구조 차이를 드러낸다 [doi:10.1038/s41598-024-65604-1, Discussion 첫째 단락]. 정서 의미는 언어 계통마다 다르고 valence, 활성화만 보편이다 [doi:10.1126/science.aaw8160, abstract].
* **Unresolved Question:** 교차문화 데이터에서 정서 기하의 문화 불변/특이 성분을 구분해야 한다 [arXiv:2509.24298, Limitations 셋째 단락]. 언어, 문화 요인의 영향 검토 [doi:10.1038/s41598-024-65604-1, Discussion 셋째 단락].
* **Technological Development:** 다국어 LLM/MLLM, GWOT(M6), triplet embedding(M5).
* **New Dataset / Model Combination:** Horikawa fMRI(참가자 언어는 Stage 1 미확인. 같은 비디오 계열의 mind captioning 참가자는 일본어 모국어 화자 [doi:10.1126/sciadv.adw1464, Discussion 셋째 단락]) + 같은 MLLM을 일본어 prompt와 일본어 정서 어휘로 쓴 embedding [AI-est] vs 영어 prompt와 Cowen & Keltner 어휘 embedding [AI-est] + 미국 평정자 [Human-norm].
* **New Research Question:** "같은 Horikawa 비디오에 대해 일본어로 정서를 판단하게 한 MLLM 표상과 영어로 판단하게 한 표상 중 어느 쪽이 참가자 뇌 RSM과 항목 수준(GW 매칭률)에서 더 정렬되며, 그 차이는 valence와 arousal을 회귀한 잔여 구조에서 나타나는가?"
* **검증 논리:** 차이가 없거나 valence/arousal에만 있으면 보편 구조 가설, 잔여 구조에서 일본어 쪽이 우세하면 언어 특이 정서 의미가 뇌 표상과 맞물린다는 구성주의적 해석이 지지된다. 모델의 언어별 능력 차이를 통제하려고 정서 무관 과제(장면 기술 embedding의 뇌 정렬)에서의 언어 간 차이를 기준선으로 뺀다.
* **위험:** 참가자 언어 미확인이면 질문 자체가 성립하지 않는다(선결 조건). 5명뿐이라 참가자 수준 일반화 불가, 효과 크기 추정 중심. 번역 인공물.
* **G1:** MLLM 경로 필요(보유).
* **선행 수행:** no. Asanuma2025는 일본인 평정 자료(Koide-Majima)와 Cowen & Keltner 자료를 각각 분석했지만 뇌와의 언어별 정렬은 다루지 않았다.

### Chain 7. 맥락만 본 정서 vs 인물만 본 정서: 생성 마스킹으로 만든 in-silico 회귀자

* **Original Finding:** 인물을 가려도 맥락만으로 정서를 정확히 추적하며 맥락은 얼굴, 몸과 별개로 기여한다 [doi:10.1073/pnas.1812250116, Discussion 첫째 단락]. MLLM은 맥락 해석이 필요한 비디오에서 표면 특징에 의존해 실패한다 [doi:10.1038/s41598-025-14961-6, Results 'Well-estimated and Poorly-estimated Videos'와 Discussion 셋째 단락]. 같은 얼굴이 맥락에 따라 다른 신경 반응을 낸다 [doi:10.1093/scan/nsl014, abstract].
* **Unresolved Question:** 맥락이 시뮬레이션으로 쓰이는지 정신 상태 추론으로 쓰이는지 구분되지 않았다 [doi:10.1073/pnas.1812250116, Discussion 둘째 단락].
* **Technological Development:** 비디오 분할과 inpainting 생성 모델, MLLM 정서 추정, in-silico encoding.
* **New Dataset / Model Combination:** Horikawa 클립과 Emo-FilM 장면에 대해 (a) 원본, (b) 인물 제거(맥락만), (c) 배경 제거(인물만) 입력의 MLLM 정서 추정 [AI-est 3종] + 소표본 인간 검증(ChenWhitney2019 절차를 따른 맥락만 평정 [Attrib-human], 수집 필요) + 기존 fMRI.
* **New Research Question:** "MLLM이 맥락만 보고 추정한 정서와 인물만 보고 추정한 정서는 Horikawa와 Emo-FilM 뇌 반응에서 서로 다른 영역(예: TPJ와 DMN vs STS와 얼굴 영역)의 고유 분산을 설명하는가, 그리고 둘의 상호작용(Kuleshov형 불일치)이 큰 클립에서 편도체와 측두극 반응이 커지는가?"
* **검증 논리:** 참가자는 원본만 봤으므로 이는 원 자극을 정보원별로 분해한 회귀자 분석이며 인과 결론이 아니다(CLAUDE.md 6절). 맥락 회귀자가 TPJ/DMN을, 인물 회귀자가 STS를 설명하면 정보원별 경로 분리를 지지한다. 둘 다 같은 영역을 설명하면 조기 통합을 시사한다.
* **위험:** inpainting 인공물이 MLLM 출력을 바꾸는 confound → 무작위 영역 inpainting 대조. Horikawa 클립은 짧아(평균 약 5초) 맥락 정보가 적다.
* **G1:** 필요(보유).
* **선행 수행:** no (검색 범위 내). 생성 반사실 자극 설계는 generative-counterfactual 담당 Axis L과 겹칠 수 있어 Round 2에서 조율이 필요하다.

---

## 7. Axis C 확장 제안

### 7.1 추가 (5절 표의 S1~S7)
* S1 Attribution-Experience Gap, S2 Situation Structure & Relational Semantics, S3 Description Residual, S5 Social Primitives & Pre-reflective Inference, S6 Collective and Cultural Emotion Semantics, S7 Narrative Prediction Signals를 Axis C에 추가한다.
* S4 Machine Raters & Annotation Provenance는 독립 Axis 후보로 올린다(5절 이유 참조).

### 7.2 재분류
* **"Perceived Meaning vs Experienced Emotion" 분할:** 이 Sub-axis는 서로 다른 두 문제를 한데 묶고 있다. (a) 관점 문제(귀속 vs 경험, S1)와 (b) 내용 문제(정서 배제 기술 vs 정서, S3). (a)는 측정 주체와 뇌 영역의 문제이고 (b)는 feature 공선성과 confound 문제라서 분석 방법이 다르다. 두 Sub-axis로 나눈다.
* **"Emotional Expectation", "Surprise / Prediction Error" → S7로 통합:** 예측 신호를 계산하는 모델과 대상(토큰, 사건, 인물 운명에 대한 믿음)을 함께 명시하도록 재정의한다. Axis D(Temporal Dynamics), N(Predictive Coding)과의 교차를 표시한다.
* **"Causal Understanding", "Character Intentions", "Social Relationships" → S2 아래 묶음:** 모두 상황 구조의 구성 요소이며, 실제 분석에서는 하나의 그래프 표현으로 계산된다.
* **"Scene Context" 유지하되 정의 축소:** 배경 맥락(인물을 제외한 장면 정보)으로 한정해 Chain 7의 분해와 맞춘다.

### 7.3 삭제
* 삭제할 Sub-axis는 없다. 다만 "Contextual Reinterpretation"은 현재 4개 데이터셋에서 같은 자극을 다른 맥락으로 본 조건이 없어(Yeshurun 2017 같은 설계 부재, doi:10.1177/0956797616682029) 관찰 데이터로 직접 검증할 수 없다. LLM in-silico 시뮬레이션(맥락 prompt 조작) 수준의 탐색 항목으로 표시한다.

### 7.4 데이터셋별 Axis C 적합도 (Stage 1 사양 기준)

| Sub-axis | Horikawa | Emo-FilM | Spacetop | NSD |
|---|---|---|---|---|
| Scene Context (배경) | 가능 (무음, 짧은 클립) | 가능 | alignvideo 가능 | 정지 장면만 |
| S2 Situation Structure | 제한 (평균 약 5초) | 적합 (완결 서사) | narratives 적합 | 제한 |
| Narrative Progression / S7 | 불가 (클립 독립) | 가능 (대사는 ASR 필요) | 최적 (텍스트, 오디오) | 불가 |
| S1 Attribution-Experience | [Human-norm]만 | [Human-norm] + 부분 [Self] | [Self] + [Attrib-human] 같은 참가자 | 100장 [Self 추정] |
| S3 Description Residual | 최적 (정서 배제 캡션, 확보 필요) | 가능 (캡션 생성 필요) | 가능 | 적합 (COCO 캡션, 정서는 [AI-est]) |
| S6 Cultural Semantics | 후보 (평정자와 참가자 문화 불일치 가능성) | 스위스 참가자(평정 언어 확인 필요) | 미국 참가자 | 제한 |

---

## 부록 A. LLM/MLLM을 정서 주석기로 쓸 때의 일치도 근거와 사용 규칙

에이전트 정의의 주의 사항에 따라 annotator 제안에는 아래 근거를 함께 단다.

| 연구 | 자극과 과제 | 사람 평정과의 일치 | 비고 |
|---|---|---|---|
| Asanuma2025 | Cowen & Keltner 2,185 비디오, 34범주 | Gemini 비디오별 평균 r 0.553, RDM r 0.555, GW 항목 매칭 1.69%, 10범주 위계 매칭 54.6%. GPT-4.1 0.538, Molmo-7B-D 0.21 | 맥락 의존, 신체 기반 정서 실패. GPT-4V 응답률 23% |
| Asanuma2025 | Koide-Majima 550 비디오, 80범주(일본인) | Gemini-인간 비디오별 평균 r 0.374, 인간 집단 간보다 약간 높음 | |
| SantavirtaV2025 | 영화 장면 이미지 468, 비디오 234, 138 사회 특징 | 인간 평균과 r 0.79 | 추상, 추론적 특징 낮음. 필터 대상 내용 실패 |
| SantavirtaE2025 | 비디오 234, 120, 이미지 300, 48 정서 | "높은 정확도"(초록) | 수치 미확인 (preprint 본문 미열람) |
| TakGratch2024 | 사건 서술 1,200, 21 appraisal | 독자 평균과 더 일치(20/21), 저자 본인과는 덜 일치 | 3인칭 관점 |
| Michelmann2025 | 서사 사건 경계 | 개별 인간보다 합의 해에 가까움 | 개인 분할 연구에는 부적합(저자 경고) |
| arXiv:2502.04379 | 게임 영상 연속 engagement | 대체로 인간 연속 주석을 포착 못함 | 시간 연속 주석의 반례 |
| arXiv:2606.07707 | 서사 연속 정서 | 독립 인간 평정 일치도 없음(타당성 점수 7.83/10만) | 반면교사 |

**사용 규칙(제안).**
1. 모델 추정은 항상 [AI-est]로 따로 표기하고 사람 라벨과 합치지 않는다.
2. 일치도는 같은 자료의 사람 간 일치도와 같은 지표로 보고한다(Emo-FilM은 평정자 쌍 r 0.38~0.39가 상한 참고값).
3. 시간 연속 AI 시계열은 Emo-FilM 1 Hz consensus로 시간 척도별 타당도를 먼저 검증하고, 검증되지 않은 척도에서는 "미검증 AI 추정 시계열"로 표기한다(Stage 1 보고서 5.3 #3과 일치).
4. 개인차 분석의 표적으로 AI 라벨을 쓰지 않는다(arXiv:2402.01908). 개인차 분석에서는 AI 라벨을 "평균 관찰자 기준점"으로만 쓴다(Chain 5).
5. 내용 필터 대상 범주(sexual desire, horror, 폭력 관련)는 범주별 일치도를 따로 보고한다(doi:10.1162/imag.a.134 Limitations).
6. Cowen & Keltner 자극과 라벨은 공개 자료이므로 사전학습 오염 점검을 탐색적으로라도 수행하고 결과를 기록한다.
7. 폐쇄 모델은 버전과 날짜를 기록하고, 결론에 쓰는 분석은 공개 가중치 모델로 재현한다.

## 부록 B. 검증된 것과 미확인 사항

* **검증됨(이번 세션):** literature.jsonl의 verified 41편 서지(식별자 경로). 본문 28편의 Discussion/Limitations 내용(각 항목 `section` 필드에 위치 기록). Asanuma2025의 수치(arXiv v2 Table 4와 Results). SantavirtaV2025의 r 0.79와 한계. MindCap2025의 "캡션 작성자에게 정서 반응을 쓰지 않도록 지시" 서술과 일본어 모국어 참가자 6명. EmoMind2026의 데이터 구성(MindCaptioning 6명, Horikawa 2020, Emo-FilM 9편). Miao2026이 LLM 기반 측정을 쓰지 않았다는 점(본문 검색 기준).
* **미확인:** Horikawa 정서 배제 캡션(비디오당 20개)의 공개 여부와 이용 조건. Horikawa 2020 참가자의 국적과 모국어. Miao2026 연속 평정 자료의 공개 여부. SantavirtaE2025 본문 수치. Garcia 2025(ICLR) 본문. Ma & Kragel 2026 본문(본 에이전트 미열람). 2절 표의 라이선스 중 "사전 지식" 표시 항목. Cowen & Keltner 자극의 MLLM 사전학습 포함 여부.
* **본 에이전트의 해석(검증된 사실과 구분):** 0절의 "규범 평정은 L2에 가깝다"는 주장, Du2025에서 기술 기준선 통제 부재 판단, LiM2026의 insula 결과를 내수용 경계로 읽는 해석은 모두 문헌을 연결한 가설이며 확인된 결과가 아니다.
