# Round 3 (Constructive Disagreement): llm-semantics의 검토

* 검토자: llm-semantics
* 기준일: 2026-11-12
* 절차: `reference/protocols.md` P3. 배정: `outputs/discussion/round3_assignment.md`
* 배정된 제안: **FA-P3**(frontier-ai → multimodal-dynamics), **EF-P7**(encoding-foundation → multimodal-dynamics), **ET-P6**(emotion-theory → vision-decoding)
* 읽은 원문: 각 제안의 `round2.md` 2절 서술, 근거가 된 Round 1 chain(frontier-ai CH2, CH3; multimodal-dynamics Chain 1, 2; encoding-foundation Chain 7; vision-decoding R2와 0.3절 L5; emotion-theory 5절 S3), Mind captioning 본문의 Imagery experiment 절(PMC 전문, 본 에이전트 재확인)
* 새로 확인한 문헌(본 에이전트 `literature.jsonl`에 추가): doi:10.1093/cercor/bhv086 (Saarimäki 2016, PubMed), doi:10.1038/nn.4468 (Tambini 2017, PubMed), arXiv:2410.00047 (arxiv.org/abs)
* 표기: label-provenance, evidence-level(R0~R4), insilico-vs-observed는 Deliverable B 0.2절을 따른다. "검색 범위 내 미발견"은 아래 적은 질의 범위 안의 판단이다.

## 판정 요약

| 제안 | 이미 연구됨? | 단순 적용? | Neuro Q 해결? | 정서 아닌 것을 decoding? | 현 데이터로 검증? | 더 강한 방법? | 반대 결과도 의미? | 종합 |
|---|---|---|---|---|---|---|---|---|
| FA-P3 | partially | 위험 있음(세 신호 회귀만 하면) | 부분적으로 그렇다 | **위험 큼**(상황 모델 지속, 컷, 내용 반복) | Emo-FilM 가능, Horikawa는 재호출 검정 부적합 | 있음 | 그렇다(사전 기술 시) | **수정 후 진행** |
| EF-P7 | partially | 중간 | 부분적으로 그렇다 | **위험 큼**(정서 encoding 표적이 내용을 포함) | (ii)는 가능, (i)과 (ii)의 대조는 교란, (iii)은 약함 | 있음 | 그렇다 | **수정 후 진행** |
| ET-P6 | partially | 아니다 | 그렇다(정서 기억 재현과 주관 보고) | **위험 큼**(cue 함축 정서, 의미 재활성) | 가능(72클립, 검정력 사전 계산 필요) | 있음 | 그렇다 | **수정 후 진행** |

---

## 1. FA-P3: 세 가지 예측 신호와 "지속 상태 vs 재호출" (frontier-ai → multimodal-dynamics)

### 제안 요지
V-JEPA 2 predictor 하나에서 예측오차 surprise, 예측 불확실성, 학습 진전 세 신호를 뽑아 multimodal-dynamics의 정서 경계(Chain 2), 정서 이월(Chain 1), learning progress와 묶는다. 정서 지속성은 "장면 국소 정서 신호(VLM 정서 vector 투영)를 ROI별 시간 상수로 누적한 leaky integrator"와 "국소 신호 + 과거 장면 재호출 회귀자(과거 장면과의 내용 유사도로 가중)"를 경쟁시켜 판정한다. 데이터는 Emo-FilM(주), Horikawa raw, Spacetop alignvideo.

### (1) 이미 연구된 것은 아닌가
* **검색 경로와 날짜(2026-11-12):** WebSearch "video prediction model surprise V-JEPA prediction error regressor fMRI naturalistic movie brain 2025 2026"; Round 1에서 frontier-ai, multimodal-dynamics가 각자 수행한 검색 기록 대조; PubMed 제목 검색 "Emotional brain states carry over and enhance future memory formation"으로 Tambini 2017 확인.
* **결과:**
  * V-JEPA surprise를 영화 fMRI 회귀자로 쓴 연구는 검색 범위 내 미발견. V-JEPA feature를 encoding 입력으로 쓴 사례(VIBE, arXiv:2507.17958, search_index, 본 에이전트 미검증)는 있으나 surprise 신호는 아니다.
  * 예측 신호와 자연 시청 fMRI의 결합 자체는 선행이 있다. 외부 승리 확률 모델의 surprise가 사건 경계, pupil, 도파민 관련 피질하와 연관(doi:10.1016/j.neuron.2020.10.029). LM Bayesian surprise가 사건 분절을 예측(doi:10.1111/cogs.13343). 예측오차형 경계와 불확실성형 경계의 분리(doi:10.7554/eLife.107955, DB에는 abstract_only). 반복 시청 시 사건 예측의 전방 이동(doi:10.7554/eLife.64972).
  * "지속 상태"의 선행: 정서 뇌 상태가 9~33분 뒤 중립 부호화로 이월된다(doi:10.1038/nn.4468, 통제 설계, 초록 기준). vmPFC 상태가 수십 초 이상 지속된다(doi:10.1126/sciadv.abf7129).
* **판정: partially.** 예측 신호와 영화 fMRI, 정서 상태 이월은 각각 선행이 있다. 같은 모델에서 뽑은 세 신호의 분리와 "지속 vs 재호출" 경쟁은 검색 범위 내 미발견. FA 원안의 판정과 같다.

### (2) 단순한 모델 적용에 불과한가
세 신호를 회귀자로 넣고 정서 ROI 설명력만 비교하면 "새 모델 feature로 영화 fMRI encoding"에 가깝다(P5 Novelty Constraint의 첫 항목에 근접). 이 제안의 과학적 몫은 **지속 vs 재호출 경쟁**에 있다. 그러려면 재호출 회귀자의 설계가 핵심인데, 원안의 "과거 장면과의 내용 유사도" 가중은 아래 (4)의 교란에 취약하다.

### (3) 실제로 Neuroscience Question을 해결하는가
부분적으로 그렇다. "자연 시청 중 정서 관련 신경 신호는 HRF를 넘는 시간 상수로 누적되는가(정서 관성), 아니면 관련 과거 내용이 재호출될 때만 재등장하는가"는 정서 동역학 이론(관성, 기분과 정서의 구분)과 사건 모형 이론 사이의 실제 질문이다. 다만 V-JEPA 신호 쪽은 "latent 시각-물리 예측오차"(원안 반론 (e), arXiv:2512.06232 인용)로 해석이 한정되므로, 정서적 놀람의 핵심인 서사, 사회 수준 예측은 이 모델로 다뤄지지 않는다.

### (4) 정서 이외의 요소를 decoding하는 것은 아닌가
위험이 크다. 세 가지다.
1. **상황 모델의 지속:** 영화 속 상황(누가, 어디서, 어떤 목표로)은 장면이 바뀌어도 이어진다. 상황 모델 표상이 지속되면 정서와 무관하게 leaky integrator 서명이 나온다. "정서 지속"을 주장하려면 상황 상태의 지속을 경쟁 회귀자로 넣어야 한다.
2. **내용 재등장과 기억 재호출의 혼동:** 과거 장면과 내용이 비슷한 현재 장면은 기억 재호출이 없어도 비슷한 자극 구동 반응을 낸다. 내용 유사도 가중 회귀자는 "재호출"이 아니라 "비슷한 내용의 재등장"을 잴 수 있다.
3. **국소 정서 신호의 정체:** VLM 정서 vector 투영은 [AI 추정, 내부 표상]이며 장면 의미와 공선적이다(내 L2, arXiv:2609.34742가 정서와 무관한 정렬로 정서 대응이 복원된다고 보고). V-JEPA surprise는 컷, 카메라 이동, 음량과 공선적이다(원안 반론 (b), (c)).

### (5) 현재 Dataset으로 검증할 수 있는가
* **Emo-FilM:** 가능하다. 연속 시계열, 첫 시청 fMRI 참가자, PPG/호흡/EDA가 있다. 평정은 반복 시청한 별도 평정자의 것이라 시간 정렬 해석에 주의(원안 반론 (d)).
* **Horikawa:** 제공 전처리본은 비디오 블록 평균이라 raw BIDS 재전처리가 필요하다(Stage 1). 클립이 서로 독립적이라 "과거 장면 재호출"이 서사적으로 의미가 없다. 블록 간 이월 검정(multimodal-dynamics Chain 1)에만 쓰고 재호출 검정에서는 뺀다. 5명이 같은 순서라 특정 클립 쌍 효과와 이월이 섞인다.
* **Spacetop alignvideo:** 뇌 신호만으로는 가능하나 영상 내 정서 시간축 라벨이 없다.

### (6) 더 강력한 모델이나 분석 방법이 있는가
* **서사 수준 예측:** V-JEPA 2 문맥은 수 초다. 대사 ASR 전사와 장면 캡션(인간 또는 MLLM, 정서 배제 지시)에 LLM을 돌려 토큰 surprisal, 다음 사건 분포의 엔트로피, 인물 운명에 대한 믿음 갱신(belief-inconsistent surprise, doi:10.1016/j.neuron.2020.10.029의 구분을 서사로 이전)을 같은 모델 비교 틀에 넣는다. 이는 내 LS-P3, LS-P8과 같은 신호다.
* **Bayesian surprise와 예측 surprise의 구분:** 사건 분절에는 일시적 Bayesian surprise가 가장 잘 맞았다(doi:10.1111/cogs.13343). V-JEPA의 "surprise"는 예측 표상과 관찰 표상의 거리라 Bayesian surprise(믿음 갱신량)와 다르다.
* **지속 모형의 대안:** leaky integrator 외에 HMM 상태 분절(Baldassano 계열)과 비교하면, 지속이 "연속 누적"인지 "이산 상태 유지"인지까지 갈린다.
* **전신 성분 분리:** 전역 fMRI 신호의 약 25%가 자율신경과 결합한다(doi:10.1038/s41593-025-01945-y). 지속 서명이 전역 자율신경 성분에서 오는지 생리 회귀 전후로 비교한다.

### (7) 결과가 기대와 다를 때도 과학적으로 유의미한가
그렇다. 사전에 다음을 적어 두면 어느 결과든 해석된다. (a) 국소 신호만으로 충분(최적 시간 상수가 HRF 규모): 자연 시청의 정서 신경 신호는 fMRI 해상도에서 장면에 묶여 있다. 이는 LLM 정서 표상이 국소적이라는 AI 쪽 보고(arXiv:2604.07729, 5.3절)와 같은 방향이라, "뇌도 그렇다"는 비교 결과가 된다. (b) 지속 우세: 정서 관성의 신경 증거. (c) 재호출 우세: 사건 기억 기반 정서 재구성. 다만 셋 모두 아래 수정안의 교란 통제를 통과해야 한다.

### 수정안
1. **가짜 재호출(pseudo-recall) 귀무 회귀자:** 같은 유사도 계산을 "아직 보지 않은 미래 장면"과 "다른 영화의 장면"에 대해서도 만든다. 진짜 재호출 회귀자는 이 둘보다 유의하게 더 설명해야 한다. 내용 재등장과 기억 재호출을 가르는 가장 값싼 통제다.
2. **상황 상태 지속 경쟁자:** MLLM으로 장면별 상황 그래프(등장인물, 장소, 목표, 관계; VidSitu, MovieGraphs 형식, arXiv:2104.00990, arXiv:1712.06761)를 만들고 [AI 추정, 기술] 그 상태의 지속을 별도 leaky integrator로 넣는다. 정서 지속은 상황 지속을 넘어설 때만 주장한다.
3. **서사 수준 예측 신호 추가:** (6)의 LLM 신호 셋을 V-JEPA 세 신호와 같은 모형 비교에 넣고, V-JEPA 결과는 "latent 시각-물리 예측오차"로만 해석한다.
4. **데이터 역할 분리:** 재호출 검정은 Emo-FilM에서만, 블록 이월은 Horikawa raw에서만 한다.
5. **결론 동사:** "정서 상태가 지속된다"가 아니라 "규범 정서 평정과 공변하는 신경 성분이 HRF를 넘는 시간 상수로 남는다"로 쓴다(emotion-theory 8절 규칙).
* **태그:** label-provenance = 일차 분석은 라벨 없음(뇌, 생리, 모델 신호). 평정 사용 시 felt / 별도 평정자 규범(반복 시청자), VLM 국소 신호는 AI 추정 / evidence-level = R0 / insilico-vs-observed = 관찰(모델 신호는 자극 기술자) / G1 = 필요(보유) / overlap: Emo-FilM 연구

---

## 2. EF-P7: In-silico 감각 박탈과 관찰된 무음 조건의 대조 (encoding-foundation → multimodal-dynamics)

### 제안 요지
(i) Emo-FilM 영화를 영상만, 오디오만, 대사 텍스트만, 전체로 각각 TRIBE v2에 넣어 정서 관련 관찰 분산(50항목 encoding)을 영역별로 얼마나 재현하는지 본다. (ii) 관찰된 무음 조건(Horikawa, Mind captioning)에서 영상만 넣은 in-silico 예측이 vmPFC 정서 기하를 얼마나 재현하는지 보고 (i)의 영상만 조건과 대조한다. (iii) 음원 분리 stem을 바꿔 넣은 R1 반사실을 원 영화의 음악 유무 구간 관찰 차이(R0)와 비교한다.

### (1) 이미 연구된 것은 아닌가
* **검색 경로와 날짜(2026-11-12):** WebSearch "brain encoding model modality ablation audio-only visual-only movie emotion fMRI in silico versus observed silent viewing"; encoding-foundation과 multimodal-dynamics의 Round 1, 2 검색 기록 대조; literature_db에서 doi:10.1126/sciadv.adk6840, arXiv:2505.20027, arXiv:2507.22229 기록 확인.
* **결과:**
  * **관찰 수준의 모달리티 제한은 이미 있다.** Lettieri 2024(doi:10.1126/sciadv.adk6840)는 같은 영화의 시청각, 시각 전용, 청각 전용 판본을 정상 참가자와 감각 박탈 참가자에게 보여 vmPFC의 모달리티 무관 범주 정서 코드와 pSTS의 valence 코드를 보고했다(DB 기록, multimodal-dynamics full_text).
  * **모델 쪽 모달리티 제거도 있다.** 다중모달 encoder에서 한 모달리티 정보를 제거해 뇌 정렬 변화를 본 연구(arXiv:2505.20027, ICLR 2025), TRIBE v2의 일반 모달 기여 지도(arXiv:2605.04326 2.8절).
  * **in-silico 무음 예측의 관찰 검증도 일반 수준에서는 있다.** TRIBE 1판은 무성 흑백 Chaplin 영화(OOD)에서도 r 0.1686을 보고했다(arXiv:2507.22229, DB 기록).
  * 정서 encoding을 표적으로 in-silico 입력 제한과 관찰 무음 조건을 대조한 연구는 검색 범위 내 미발견.
* **판정: partially.** EF 원안의 판정과 같다. 다만 Lettieri 2024의 관찰 판본 비교가 이 제안의 가장 가까운 선행이며, 원안의 근거 목록에는 있지만 "관찰 대조쌍"의 기준으로는 쓰이지 않았다.

### (2) 단순한 모델 적용에 불과한가
중간이다. TRIBE에 입력을 바꿔 넣고 재현도를 재는 것 자체는 모델 적용이다. 과학적 몫은 "in-silico 입력 제한이 관찰 입력 제한과 같은 손실을 내는가"라는 **surrogate 타당도 검정**에 있다. 이 몫을 살리려면 같은 자극의 관찰 판본 쌍이 필요한데, 원안의 (i)-(ii) 대조는 자극이 다르다((5) 참조).

### (3) 실제로 Neuroscience Question을 해결하는가
부분적으로 그렇다. "supramodal 정서 코드 중 단일 모달리티 자극으로 계산 가능한 부분은 얼마인가"는 Lettieri 2024가 남긴 질문(vmPFC 코드가 공통 언어 채널에 기댈 가능성, multimodal-dynamics 기록)에 직접 닿는다. 특히 **대사 텍스트만 조건**은 언어 채널 가설의 in-silico 검정이 될 수 있다. 다만 그 결론은 R1(모델 내 개입)이며 실제 뇌의 모달리티 의존성에 대한 결론은 아니다.

### (4) 정서 이외의 요소를 decoding하는 것은 아닌가
위험이 크다. 표적인 "정서 관련 관찰 분산"을 50항목 평정 encoding으로 정의하면, 그 분산의 상당 부분은 장면 의미와 시청각 강도다(영화 정서 fMRI에서 공포 장면이 더 어둡고 시끄럽다는 저수준 공선성 경고, multimodal-dynamics U6에 기록된 doi:10.1093/scan/nsad063). TRIBE 예측도 내용 구동이다. 따라서 "영상만 입력이 정서 분산을 X% 재현"은 "영상만 입력이 내용 분산을 재현"과 구분되지 않는다. 내 LS-P1의 기술 잔차 표적(정서 배제 캡션과 시각 feature를 통제한 뒤 남는 정서 분산)을 함께 써야 정서 고유 부분에 대한 결론이 된다.

### (5) 현재 Dataset으로 검증할 수 있는가
* **(i) Emo-FilM 입력 제한:** 가능하다. 다만 Emo-FilM에는 transcript가 없어 ASR 전사가 필요하고 [AI 생성 전사], 대사가 적은 영화에서는 "텍스트만" 조건이 거의 빈 입력이 되어 대사 양이 결과를 좌우한다.
* **(ii) 관찰 무음 데이터의 in-silico 충실도:** 가능하다. Horikawa와 Mind captioning은 같은 자극의 관찰 무음 fMRI이므로 영상만 입력 예측의 충실도를 직접 잴 수 있다.
* **(i)과 (ii)의 대조:** 교란이 크다. Emo-FilM과 Horikawa는 자극(완결 서사 vs 5초 클립), 라벨(50항목 1 Hz vs 34/14 클립 단위), 스캐너, 참가자가 모두 다르다. "in-silico 무음 손실 = 관찰 무음 손실"을 검정하려면 같은 자극의 소리 있는 관찰 판본과 무음 관찰 판본이 필요한데 우리 5개 데이터셋에는 없다.
* **(iii) stem 교체 vs 음악 유무 구간:** 영화에서 음악은 정서적으로 중요한 장면에 배치되므로 음악 유무 구간은 내용과 정서 강도가 다르다. 관찰 R0 차이와 in-silico R1 차이의 방향 일치는 약한 증거다.

### (6) 더 강력한 모델이나 분석 방법이 있는가
* **같은 자극의 관찰 판본 쌍:** Lettieri 2024의 판본별 데이터에 접근할 수 있으면 그것이 in-silico 입력 제한의 직접 기준이 된다(공개 여부 미확인, 확인 필요). 이것이 가장 강한 개선이다.
* **기술 텍스트 입력 조건(내 쪽 제안):** "대사 텍스트만" 외에 **화면 내용을 정서 배제 지시로 기술한 텍스트**(시각 장애인용 화면 해설과 같은 형식, MLLM 생성 [AI 추정, 기술] 또는 Horikawa 클립은 Mind captioning 인간 캡션)를 TRIBE 텍스트 경로에 넣는 조건을 추가한다. 이 조건이 vmPFC 정서 기하를 영상 입력만큼 재현하면 "언어로 기술된 장면 의미만으로 supramodal 코드가 계산된다"는 in-silico 증거가 된다. 이는 Lettieri 2024의 언어 채널 가설을 대사가 아닌 기술 의미 수준에서 검정한다.
* **자연 모달리티 변이 보정:** multimodal-dynamics의 MD-P3처럼 Emo-FilM 안에서 대사, 음악 유무가 다른 구간을 MLLM 장면 기술(L1)로 내용 매칭한 뒤 비교하면 (iii)의 교란이 줄어든다.
* **충실도 지표:** 재현도를 상관 하나로 보지 말고 관계 구조(RSA, GW 매칭률)까지 본다. TRIBE 합성 뇌는 클립별 정서 정보는 보존해도 클립 간 관계 구조를 크게 잃었다(arXiv:2605.16739, encoding-foundation 기록 rho 0.635에서 0.166).

### (7) 결과가 기대와 다를 때도 과학적으로 유의미한가
그렇다. (a) 영상만 입력이 vmPFC 정서 기하를 전체 입력만큼 재현: 시각 입력으로 충분하거나, TRIBE 영상 경로가 이미 의미를 운반한다는 뜻이다. 기술 텍스트 조건과 비교하면 둘이 갈린다. (b) 텍스트만 입력이 재현: 언어 채널 가설의 in-silico 지지. (c) 어떤 단일 입력도 재현하지 못함: 통합이 필요하다는 in-silico 증거이며 Lettieri 2024의 관찰 결과(모달리티 무관 코드)와 대조할 질문이 된다. 어느 경우든 결론은 R1로 표기한다.

### 수정안
1. **표적 재정의:** 정서 관련 관찰 분산을 (a) 50항목 encoding 전체와 (b) 기술 잔차(정서 배제 캡션 embedding과 시각 feature를 통제한 뒤 남는 정서 분산, LS-P1) 둘로 나눠 보고한다.
2. **입력 조건 추가:** 대사 텍스트(ASR), 화면 기술 텍스트(정서 배제 지시), 둘의 합. 각 텍스트의 정서 어휘 누출을 감사한다(LS-P1의 1번).
3. **(i)-(ii) 대조의 위상 변경:** 두 데이터셋 간 대조는 "탐색적 비교"로 낮추고, 주 검증은 (ii) 같은 자극의 관찰 무음 충실도로 한다. Lettieri 2024 판본 데이터 접근을 확인해 가능하면 직접 기준으로 쓴다.
4. **(iii) 내용 매칭:** 음악 유무 구간을 MLLM 장면 기술로 내용 매칭한 뒤 비교하고, 매칭 전후 결과를 함께 보고한다.
5. **이름:** 원안의 반론 대응대로 "감각 박탈" 대신 "입력 제한"으로 부른다. 발달 중 감각 박탈(Lettieri 2024의 핵심)과 학습된 모델의 입력 제거는 다르다.
* **태그:** label-provenance = felt / 별도 평정자 규범(Emo-FilM, Horikawa C&K), 전사와 화면 기술은 AI 생성 / evidence-level = R1(입력 제한, stem 교체) + R0(관찰 충실도) / insilico-vs-observed = 혼합 / G1 = 필요(보유) / overlap: Emo-FilM 연구

---

## 3. ET-P6: 회상 vividness가 정서 부분공간 재활성을 따르는가 (emotion-theory → vision-decoding)

### 제안 요지
Mind captioning 회상 데이터에서 재활성을 시각 부분공간(저수준 DNN feature decoder)과 정서 부분공간(34/14 규범 decoder를 시각, 의미 feature로 잔차화)으로 나누고, 시행별 vividness가 어느 쪽 재활성을 더 잘 가르는지 type-2 민감도(ROC 면적, meta-d' 논리)로 비교한다. vividness가 낮은 시행에서도 정서 부분공간 재활성이 남는지 본다(탐색적).

### (1) 이미 연구된 것은 아닌가
* **검색 경로와 날짜(2026-11-12):** WebSearch "fMRI emotion classifier trained on movie viewing generalizes to mental imagery recall of emotional episodes cross-induction decoding"; WebSearch "emotional reinstatement during memory retrieval fMRI pattern similarity negative valence video recall vividness affective reactivation decoding 2023 2024 2025"; PubMed 제목 검색 "Discrete Neural Signatures of Basic Emotions"; arxiv.org/abs/2410.00047 확인; emotion-theory, vision-decoding의 검색 기록 대조.
* **결과:**
  * **지각에서 심상으로의 정서 decoding 일반화는 이미 보고되었다.** 영화와 mental imagery로 유도한 6개 기본 정서에서 분류기가 유도 조건 사이와 개인 사이로 일반화되었다(doi:10.1093/cercor/bhv086, 초록. 심상이 같은 클립의 회상인지는 본문 미확인). 원안의 선행 검색 기록에는 이 연구가 없다.
  * 비디오 회상의 재활성과 vividness 대응은 확립되어 있다(원안이 인용한 St-Laurent 2015, Bone 2020. 이 두 편은 literature_db에 없어 본 에이전트는 식별자를 확인하지 않았다).
  * 정서 라벨을 cue로 준 심상을 비디오 시청 fMRI 사상으로 decoding한 시도(arXiv:2410.00047, 초록).
  * 2026년 eNeuro 수리 원고가 정서 뉴스 클립 회상 중 DMN 하위망 재현을 다룬다는 검색 결과가 있으나 본 에이전트는 식별자를 확인하지 않았다(search_index 수준, 문헌 파일에 넣지 않음).
  * 같은 클립 회상에서 시각, 의미 성분을 뺀 정서 부분공간을 분리하고 시행별 vividness와 type-2로 비교한 연구는 검색 범위 내 미발견.
* **판정: partially.** 원안의 판정과 같지만 근거를 보강해야 한다. "정서 정보가 회상에서 재활성되는가" 자체는 Saarimäki 2016의 교차 유도 일반화로 부분 선행이 있으므로, 새로움은 (a) 클립 특이 회상, (b) 정서 부분공간의 잔차화, (c) vividness와의 type-2 비교로 한정해야 한다.

### (2) 단순한 모델 적용에 불과한가
아니다. type-2 분석으로 "주관 보고(vividness)가 어떤 신경 성분의 재활성을 따르는가"를 묻는 것은 분석 논리가 새롭다. 다만 type-2 틀은 객관적 정답이 있는 1차 과제를 전제하는데(HMeta-d, doi:10.1093/nc/nix007 초록), 여기서는 "정답" 자리에 decoder 출력(재활성 강도)이 들어간다. 원안도 decoder 잡음이 metacognitive 비효율처럼 보일 수 있다고 적었다(반론 5).

### (3) 실제로 Neuroscience Question을 해결하는가
그렇다. 정서 기억 재현(NEVER 모델, doi:10.3758/s13423-017-1313-9)과 주관 보고의 관계, 그리고 "보고되지 않은 정서 정보"라는 HOT 대 1차 이론 논쟁의 관찰 수준 단서를 준다. 단 vividness는 심상의 생생함 보고이지 정서 자각 보고가 아니라는 원안의 단서가 결론 범위를 정한다.

### (4) 정서 이외의 요소를 decoding하는 것은 아닌가
위험이 크다. 세 가지다.
1. **cue가 함축하는 정서:** 회상 준비 구간 cue는 같은 클립의 20개 캡션 중 하나를 영어와 일본어 번역으로 보여 준 것이다(doi:10.1126/sciadv.adw1464, Materials and Methods 'Imagery experiment', 본 에이전트 본문 재확인). 캡션은 정서 반응을 쓰지 말라는 지시로 수집되었지만, "장례식에서 사람들이 운다" 같은 문장은 정서를 함축한다. 회상 구간의 정서 부분공간 재활성이 cue 문장의 함축 정서(L2)를 읽은 결과일 수 있다. 원 논문은 준비 구간 의미 decoding이 회상 구간보다 낮았다고 보고했지만(fig. S12D 서술), 정서 쪽은 확인되지 않았다.
2. **의미 재활성의 운반:** Mind captioning에서 의미 feature는 시각 feature보다 회상으로 잘 일반화되었다(같은 논문 Discussion 둘째 단락). 정서 decoder를 의미 feature로 잔차화하면 남는 정서 성분이 매우 작을 수 있고, 잔차화하지 않으면 의미 재활성을 정서로 오인한다.
3. **규범 정서 지식:** decoder 목표가 C&K 별도 평정자 felt 규범이므로 회상에서 해독되는 것은 "이 장면이 보통 일으키는 정서에 대한 지식"(vision-decoding 0.3절 L5, 내 L2)일 수 있다. 참가자 본인의 회상 중 정서 경험 보고는 없다.

### (5) 현재 Dataset으로 검증할 수 있는가
가능하다. Mind captioning 6명 x 72클립 x 5회 회상, 시행별 vividness, 같은 클립의 5회 반복 지각 데이터가 있고 Horikawa 2020 지각 데이터로 decoder 학습을 보강할 수 있다(사용자 보유, 전처리 완료). 주의점:
* vividness와 정확도는 회상 직후 **실제 비디오를 다시 본 뒤** 평정했다(같은 절). vividness는 회상 중 즉시 보고가 아니라 재시청과 비교한 회고 판단이다.
* 72클립의 C&K 정서 분포와 vividness 분포를 먼저 계산해야 한다. C&K 라벨은 보유하고 있으므로 지금 바로 계산할 수 있는 파일럿 0단계다.
* 회상 직후 같은 비디오 재제시와 HRF가 겹친다(vision-decoding R2 교란 목록).
* S1은 같은 자극에 여러 번 노출된 예비 참가자다(vision-decoding 0.1).

### (6) 더 강력한 모델이나 분석 방법이 있는가
* **순방향(encoding) 분해:** decoder 대신 지각 데이터로 시각, 의미, 정서 band를 가진 banded ridge encoding model을 학습하고, 각 band가 회상 반응을 얼마나 예측하는지 시행별로 본다. decoder 잡음이 type-2 지표를 오염시키는 문제를 줄이고, 의미와 정서 band의 고유 기여를 같은 모형 안에서 분리한다.
* **시행별 ERS와 부분 RSA:** 지각-회상 패턴 유사도(encoding-retrieval similarity)를 클립별로 계산하고, 정서 RDM과 의미 RDM, 시각 RDM의 부분 상관으로 분해한다.
* **vividness 모형:** type-2 ROC 대신 개인 내 순위를 쓰는 서열 혼합 모형(vividness ~ 시각 재활성 + 의미 재활성 + 정서 재활성 + 정확도 평정 + (참가자 random slope))으로 세 성분의 고유 연관을 한 모형에서 비교한다. HMeta-d는 이진 정답을 전제하므로 그대로 쓰지 않는다.
* **cue 함축 정서 통제(내 쪽 제안):** 72개 cue 캡션 각각에 LLM reader 모드 정서 추정 [AI 추정, perceived affective quality]과 소규모 인간 reader 평정(캡션만 읽고 정서 추정, R2)을 만들어 회귀자로 넣는다. 준비 구간의 정서 decoding도 같은 방식으로 따로 보고해 회상 구간과 비교한다.

### (7) 결과가 기대와 다를 때도 과학적으로 유의미한가
그렇다. (a) 정서 재활성이 의미 재활성과 cue 함축 정서로 완전히 설명됨: 클립 회상의 "정서"는 언어화 가능한 정서 지식이라는 결과이며 정서 기억의 본성(지식 vs 재경험)에 대한 정보다. (b) 정서 재활성이 남고 vividness와 무관: 보고되지 않는 정서 정보의 약한 관찰 단서(탐색적). (c) 정서 재활성이 남고 vividness와 연동: NEVER 모델과 부합. 각 결과의 해석을 사전에 적는다.

### 수정안
1. **선행 근거 보강:** 새로움 서술에 doi:10.1093/cercor/bhv086(지각-심상 교차 유도 일반화)을 넣고, 새로움을 (a) 클립 특이 회상, (b) 정서 부분공간 잔차화, (c) vividness 연동으로 한정한다.
2. **cue 함축 정서 통제:** (6)의 cue 캡션 정서 추정을 회귀자로 넣고, 준비 구간을 대조 조건으로 보고한다.
3. **분석 축 변경:** 주 분석을 순방향 banded ridge와 서열 혼합 모형으로 두고, type-2 ROC는 보조 분석으로 둔다.
4. **vividness의 성격 명시:** "재시청 후 회고 평정"임을 결론에 적고, 정확도 평정을 공변량으로 넣는다.
5. **파일럿 0단계:** 72클립의 C&K 범주 분포, valence 분포, 시행별 vividness 분포를 먼저 계산해 검정력을 추정한다. 부정 valence 클립이 적으면 NEVER 예측 검정은 보류한다.
6. **결론 동사:** "회상에서 정서가 재경험된다"가 아니라 "지각 시 규범 정서와 공변하던 신경 성분이 회상에서 재출현한다"로 쓴다.
* **태그:** label-provenance = decoder 목표 felt / 별도 평정자 규범(C&K), vividness와 정확도는 fMRI 참가자 본인 보고(심상, 회고), cue 정서 추정은 AI 추정 + 신규 인간 reader(R2) / evidence-level = R0(신규 cue 평정 포함 시 R2) / insilico-vs-observed = 관찰 / G1 = cue 캡션과 라벨만 쓰면 불필요, 시각 feature에는 필요(보유) / overlap: 없음

---

## 부록. 이번 검토의 검색 기록

| 날짜 | 경로 | 질의 | 대상 | 주요 결과 |
|---|---|---|---|---|
| 2026-11-12 | WebSearch | video prediction model surprise V-JEPA prediction error regressor fMRI naturalistic movie brain 2025 2026 | FA-P3 | V-JEPA surprise fMRI 연구 미발견. VIBE(V-JEPA feature encoding, search_index), Nguyen 2026 eLife(오차 vs 불확실성 경계) |
| 2026-11-12 | PubMed 제목 검색 | Emotional brain states carry over and enhance future memory formation | FA-P3 | doi:10.1038/nn.4468 (PMID 28024158) 확인 |
| 2026-11-12 | WebSearch | brain encoding model modality ablation audio-only visual-only movie emotion fMRI in silico versus observed silent viewing | EF-P7 | 정서 대상 연구 미발견. arXiv:2505.20027(일반 모달 제거) |
| 2026-11-12 | literature_db 조회 | doi:10.1126/sciadv.adk6840, arXiv:2507.22229 | EF-P7 | Lettieri 2024 판본 비교, TRIBE 무성 영화 OOD r 0.1686 |
| 2026-11-12 | WebSearch | fMRI emotion classifier trained on movie viewing generalizes to mental imagery recall of emotional episodes cross-induction decoding | ET-P6 | arXiv:2410.00047, Saarimäki 2023 영화 정서 모형 일반화 |
| 2026-11-12 | PubMed 제목 검색, Crossref | Discrete Neural Signatures of Basic Emotions | ET-P6 | doi:10.1093/cercor/bhv086 (PMID 25924952): 영화와 심상 유도 간 정서 분류 일반화 |
| 2026-11-12 | WebSearch | emotional reinstatement during memory retrieval fMRI pattern similarity negative valence video recall vividness affective reactivation decoding 2023 2024 2025 | ET-P6 | 정서 부분공간과 vividness를 함께 다룬 연구 미발견. eNeuro 2026 원고(search_index, 미확인) |
| 2026-11-12 | 본문 재확인 | Mind captioning PMC 전문 'Imagery experiment' 절 | ET-P6, VD-P3 | cue는 20개 캡션 중 하나(영어 + 일본어 번역), vividness와 정확도는 재시청 후 평정 |
