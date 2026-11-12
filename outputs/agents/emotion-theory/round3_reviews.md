# Round 3 (Constructive Disagreement): emotion-theory 검토

* 검토자: emotion-theory (Axis A, Q, U 관점; 외부 분야 Artificial Consciousness and Metacognition)
* 기준일: 2026-11-12. 절차: `reference/protocols.md` P3. 배정: `outputs/discussion/round3_assignment.md`
* 검토 대상: **GC-P2** (generative-counterfactual → llm-semantics), **FA-P3** (frontier-ai → multimodal-dynamics), **VD-P4** (vision-decoding → generative-counterfactual)
* 읽은 것: 각 제안의 원문(보낸 에이전트 round2.md 2절)과 근거 chain(generative-counterfactual round1 CH1, CH2, S7; llm-semantics round1 Chain 1; vision-decoding round1 R1, R6, 0.3절; multimodal-dynamics round1 Chain 1, 2; frontier-ai round1 T1, T5, U2)
* "이미 연구되었는가"는 이번에 직접 WebSearch와 Crossref, PubMed로 검색했고 질의와 날짜를 적었다. 새로 확인한 문헌(doi:10.1371/journal.pone.0308295)은 `literature.jsonl`에 추가했다. 검색 요약에만 나온 문헌은 근거 ID로 쓰지 않았다.

## 판정 요약

| 제안 | 이미 연구됨 | 단순 적용 | Neuro Q 해결 | 정서 아닌 내용 decoding 위험 | 현 데이터로 검증 | 더 강한 방법 | 반대 결과의 의미 | 종합 |
|---|---|---|---|---|---|---|---|---|
| GC-P2 | partially (조합은 미발견) | 아니오 (삼각 검증 설계) | 부분적 | **높음** (의미 고정 편집이 지각 단서를 바꿈) | R0, R1 가능, R2는 신규 수집 | 있음 (자연 controversial selection, 의미의 잠재변수 측정) | 있음 (결정표 보완 필요) | **조건부 지지, 수정 필요** |
| FA-P3 | partially (구성 요소는 각각 선행, 결합 미발견) | 절반 (예측 신호 부분은 모델 적용) | 지속 vs 재호출은 진짜 질문이나 식별 문제 | **높음** (VLM 정서 투영과 지속 의미 맥락이 섞임) | Emo-FilM 가능(재전처리 필요), Horikawa가 더 나은 시험대 | 있음 (rSLDS, 신경 재활성 직접 측정) | 있음 | **분리 후 지지** |
| VD-P4 | partially (상한 비교는 관행, 정서 축 평가는 미발견) | 대체로 예 (평가 인프라) | 약함 (2AFC 부분만) | **높음** (CLIP 공간 2AFC는 정서 진단적 시각 정보를 잼) | 가능 (NSD 생성기, Horikawa 프레임) | 있음 (생성 없는 latent 수준 probe) | 있음 | **방법론 인프라로 지지, 해석 범위 축소** |

---

## 1. GC-P2: 기술 잔차(통계 통제)와 의미 고정 편집(설계 통제)을 같은 voxel에서 맞대기

**요약.** llm-semantics Chain 1(정서 배제 캡션 LLM embedding을 통제한 뒤 남는 규범 정서 고유 분산, R0)과 vision-decoding R6이 "잔차가 남는 voxel"을 내면, generative-counterfactual이 같은 voxel의 encoder 예측이 의미 고정 정서 편집에 반응하는지(R1)와 편집의 정서 변화(R2 인간 평정)를 본다. 사전 등록 판정표로 두 결과를 맞대고, Kuleshov형 자극을 생성해 관점을 나눈 인간 평정("인물이 느끼는 정서", "당신이 느끼는 정서")을 받는다.

### 1.1 이미 연구된 것은 아닌가
* **검색:** WebSearch "semantics-controlled emotion image editing in silico encoding model fMRI emotion versus semantic content counterfactual stimuli 2025 2026"; WebSearch "Kuleshov effect generative AI edited clips fMRI context attribution emotion observer felt rating 2024 2025"; Crossref와 PubMed로 결과 확인. 2026-11-12.
* **결과:** 세 구성 요소의 조합(같은 voxel에서 통계 잔차와 의미 고정 편집 민감도를 맞대기)은 찾지 못했다. 부분 선행은 다음과 같다.
  * 정서 편집기 자체(EmoEdit, arXiv:2405.12661)는 신경 데이터 없는 컴퓨터 비전 연구다. 검색에 나온 MooD(VA 기반 의미 제어 편집)는 식별자를 확인하지 않아 근거로 쓰지 않는다.
  * 편도체 encoding model로 합성 자극을 만든 연구(doi:10.1523/JNEUROSCI.1436-24.2025)와 뇌 유도 생성의 실측 검증(arXiv:2512.00557)은 있으나 의미 고정 조건이 없다. 정서 편집기의 hidden state가 정서 ROI보다 시각 ROI 예측과 더 맞는다는 보고(arXiv:2610.13558)는 이 제안의 편집 단계가 시각 쪽으로 미끄러질 위험의 직접 근거다.
  * Kuleshov형 자극의 fMRI는 **이미 있다.** Cao et al.(2024, doi:10.1371/journal.pone.0308295)은 실제 영화 편집 face-scene-face 시퀀스로 중립 얼굴의 valence, arousal 해석 변화와 그 신경 상관(precuneus, 해마, OFC, 섬엽 등)을 보였다(초록). Mobbs et al.(2006, doi:10.1093/scan/nsl014)이 원형이다. 두 연구 모두 평정 대상은 **인물 얼굴의 정서(귀속, 지각)**이며 관찰자 본인의 경험은 따로 묻지 않았다. 따라서 GC-P2 3번의 새로움은 "생성 편집"과 "관점 분리 평정"에 한정된다.
* **판정:** partially.

### 1.2 단순한 모델 적용에 불과한가
아니다. 두 종류의 통제(통계 잔차, 설계 편집)를 같은 voxel에서 대조하는 삼각 검증 설계이며, 결과 조합별 해석을 사전에 정한 점이 방법론적 기여다. 다만 R1 쪽은 "Horikawa 2,181개 자연 클립과 5명으로 학습한 encoder의 편집 자극 예측"이므로, 편집 방향이 학습 분포 밖이면 예측은 외삽이다. 너희가 CH1에서 적은 "feature 공간 맹시" 외에 **"학습 공선성 때문에 정서 방향 가중치가 식별되지 않는 문제"**가 있다. 자연 자극에서 정서와 의미가 공선적이면 encoder의 정서 방향 가중치는 의미 방향을 대신 담고 있을 수 있고, 편집 민감도는 그 대리 가중치를 읽는다.

### 1.3 실제로 Neuroscience Question을 해결하는가
부분적으로 해결한다. 질문은 "정서 관련 뇌 신호가 장면 의미를 넘어서는가"이며 정서 이론(정서 고유 표상 대 의미 재표현)에 직접 답한다. 그러나 두 팔이 서로 독립적인 증거가 아니다. R0 팔은 관찰 뇌, R1 팔은 같은 관찰 뇌로 학습한 encoder이고, 둘 다 같은 규범 평정을 쓴다. 두 결과가 모두 양성이어도 "뇌가 의미를 넘는 정서 신호를 가진다"의 증거 수준은 R0에 R1의 일관성이 더해진 것이지 R3가 아니다(너희 결론 수준 사다리대로). 판정표에 이 점을 명시하자.

### 1.4 Emotion 이외의 요소(visual, semantic content)를 decoding하는 것은 아닌가
**이 제안의 가장 큰 위험이다.** "의미 고정"은 캡션 embedding을 고정한다는 뜻인데, 정서를 바꾸는 편집은 표정, 조명, 색, 동작 속도 같은 **지각 단서**를 바꾼다. 저수준 생태 통계가 정서 판단과 시각피질 반응을 함께 설명한다는 결과(doi:10.1038/s41467-024-53668-6)를 보면, 편집 민감도 양성은 "의미를 넘는 정서"가 아니라 "의미를 넘는 저수준 지각 변화"일 수 있다. 의미 대 정서가 아니라 의미 대 지각의 분리가 된다. 또 Axis U 관점에서, R0 팔의 정서 라벨은 별도 평정자 규범(felt 보고의 평균), R2 팔은 새 별도 평정자이므로 둘 다 fMRI 참가자의 경험이 아니다(너희 반론 (d)에 동의).

### 1.5 현재 Dataset으로 검증할 수 있는가
* R0 팔: Horikawa 뇌 + Mind captioning 인간 중립 캡션(비디오당 20개)으로 가능하다. 단 사용자 보유본에 캡션이 들어 있는지는 미확인이다.
* R1 팔: Horikawa로 학습한 encoder(+ TRIBE v2 zero-shot)로 가능하다.
* R2 팔: 신규 행동 평정이 필요하다(IRB, 비용). Horikawa 비디오의 요청 양식 이용 조건과 Emo-FilM 영화별 CC 조항(파생물 허용 여부)이 편집본을 새 평정자에게 보여 줄 수 있는지 결정한다(둘 다 미확인).
* Kuleshov 자극: Horikawa는 무음 짧은 클립이라 맞지 않고(너희 반론 (c)에 동의), Emo-FilM 장면은 라이선스 조건부다.

### 1.6 더 강력한 모델이나 분석 방법이 있는가
1. **생성 전에 자연 controversial selection:** Horikawa와 Mind captioning의 2,180개 클립 안에서 캡션 embedding RDM과 정서 평정 RDM이 가장 크게 갈리는 클립 쌍을 고르고 보류 피험자의 뇌가 어느 쪽을 따르는지 본다(encoding-foundation Chain 4, adversarial-reviewer I3와 같은 논리). 생성기 교란(AI다움, 신기성, 분포 이탈)이 없고 R0이지만 실측 뇌에서 판정한다. 편집은 자연 자극으로 채울 수 없는 영역만 채운다.
2. **R0 팔에서 의미를 잠재 구성개념으로 측정:** 인간 중립 캡션 하나만 통제하면 측정 오차 때문에 의미가 덜 통제되어 "정서 잔차"가 부풀려진다(doi:10.1371/journal.pone.0152719). 인간 중립 캡션, MLLM 캡션, 73개 의미 feature, 객체 라벨을 여러 지표로 두고 banded ridge와 신뢰도 민감도 분석을 쓴다(adversarial-reviewer D2와 같은 방향, doi:10.1016/j.neuroimage.2022.119728).
3. **여러 encoder의 합의:** Horikawa 학습 encoder, TRIBE v2, NSD 학습 encoder에서 편집 민감도가 일관될 때만 보고한다.

### 1.7 결과가 기대와 다를 때도 과학적으로 유의미한가
대체로 그렇다. 사전 판정표가 세 칸을 정했다. 빠진 칸이 하나 있다. **두 팔이 모두 음성**이면 (a) 정서 고유 신호가 없거나, (b) 규범 라벨의 신뢰도가 낮아 둘 다 검출력이 없거나, (c) encoder와 캡션이 같은 의미 공간에 갇혀 있다는 뜻이다. (b)를 가르려면 라벨 신뢰도(Horikawa는 평정자 원자료 비공개라 가정 범위 sweep, Emo-FilM은 직접 추정)를 함께 보고해야 한다.

### 1.8 수정안
* **M1. 지각 대조 팔 추가:** null-edit에 더해, 정서는 바꾸지 않으면서 같은 크기의 저수준 변화(색, 대비, 공간주파수)를 주는 비정서 지각 편집을 둔다. 편집 민감도는 "정서 편집 민감도 - 지각 대조 편집 민감도"로 정의한다.
* **M2. 의미의 다지표 잠재 측정과 신뢰도 민감도**(1.6 2번).
* **M3. 순서:** 자연 controversial selection(R0, 실측 판정) → 편집(R1) → 인간 평정(R2). 생성은 2단계 이후로 미룬다.
* **M4. 관점 분리 평정의 설계:** "인물이 느끼는 정서", "이 장면이 보통 불러일으킬 정서", "당신이 느끼는 정서"의 세 지시를 **평정자 간(between-subject)**으로 배정한다. 한 사람이 세 관점을 연달아 평정하면 대비 효과가 생긴다. 이 셋은 Axis U의 대상 축(portrayed, perceived affective quality, felt)과 1대1로 대응한다.
* **M5. Kuleshov 부분의 새로움 범위:** Cao 2024와 Mobbs 2006을 선행으로 명시하고, 새로움을 생성 편집과 관점 분리 평정으로 좁힌다.
* **M6. 판정표의 넷째 칸(둘 다 음성)과 증거 수준(R0 + R1 일관성, R3 아님)을 명시한다.**
* 태그: label-provenance = 원 데이터 felt x 별도 평정자 규범, 신규 평정 portrayed / perceived / felt x 신규 별도 평정자, 캡션 기술 의미 x 별도 평정자(정서 배제 지시), AI 캡션과 정서 추정 x AI 추정. evidence-level = R0 + R1 + R2(제안자 표기와 같음).

---

## 2. FA-P3: 세 가지 예측 신호와 "지속 상태 vs 재호출"

**요약.** V-JEPA 2 predictor 하나에서 예측오차 surprise, 예측 불확실성, 학습 진전을 뽑아 multimodal-dynamics의 정서 경계(Chain 2), 이월(Chain 1), learning progress(4절 개념 4)와 묶는다. 정서 지속성은 "장면 국소 정서 신호(VLM 정서 vector 투영)를 ROI별 시간 상수로 누적한 leaky integrator"와 "국소 신호 + 과거 장면 재호출 회귀자(내용 유사도 가중)"를 경쟁시켜 "지속 상태"와 "재호출"을 구분한다.

### 2.1 이미 연구된 것은 아닌가
* **검색:** WebSearch "emotional state persistence versus memory reinstatement naturalistic movie fMRI time constant leaky integrator affect video prediction surprise", 2026-11-12. 제안자의 검색("V-JEPA latent prediction error surprise fMRI brain movie watching", "'world model' OR 'video prediction' surprise regressor fMRI naturalistic movie emotion ...")도 참조.
* **결과:** leaky integrator로 정서 지속성을 추정하거나 지속 대 재호출을 경쟁시킨 연구는 찾지 못했다. 구성 요소는 각각 선행이 있다. vmPFC의 느린 이산 상태(doi:10.1126/sciadv.abf7129), 정서 뇌 상태의 수십 분 이월(doi:10.1038/nn.4468), 시간 구조화된 사건의 예측(doi:10.7554/eLife.64972), LLM surprise와 사건 분절(doi:10.1111/cogs.13343), 정서 변화가 기억 사건 경계를 만든다는 결과(doi:10.1038/s41467-023-42241-2). 검색 요약에 나온 "10분 클립의 후반 구간이 지속 정서 분류에 가장 기여"한 FC 연구는 bioRxiv 판만 식별자로 확인되어 근거로 쓰지 않는다.
* **판정:** partially (구성 요소는 선행, 세 신호의 단일 모델 분리와 지속 대 재호출 경쟁은 미발견).

### 2.2 단순한 모델 적용에 불과한가
절반은 그렇다. V-JEPA 2 신호 세 개를 회귀자로 넣는 부분은 모델 적용이다. "같은 모델에서 세 신호를 뽑아 신호 종류의 차이를 본다"는 설계 아이디어는 좋지만, 그 결과가 정서 이론에 무엇을 말하는지가 제안에 약하다. 반면 "지속 상태 대 재호출"은 정서 동역학의 진짜 이론 질문이다(정서 관성 대 내용에 의한 재유발, Axis A의 Emotion vs Mood와 D의 Hysteresis). 두 부분은 서로 의존하지 않는 별개 프로젝트이므로 나누는 것이 낫다.

### 2.3 실제로 Neuroscience Question을 해결하는가
지속 대 재호출은 해결할 가치가 있지만 **식별 문제**가 크다. 영화에서는 비슷한 내용이 시간적으로 몰려 있어(같은 장면, 같은 인물) "내용 유사도 가중 재호출"과 "긴 시간 상수의 누적"이 같은 예측을 낸다. 두 가설은 비슷한 정서 내용이 **멀리 떨어진 시점에 다시 나올 때**만 갈린다: 지속은 지연에 따라 지수 감소, 재호출은 지연과 무관하게 유사도에 비례. Emo-FilM 영화 14편(6.7~17.1분)에는 이런 장거리 재등장이 적을 수 있다. 반대로 Horikawa는 서로 무관한 2,181개 클립이 고정 순서로 이어져, 내용이 비슷한 클립이 다양한 지연으로 다시 나온다. 다만 5명이 같은 순서를 봐서 특정 클립 쌍 효과와 섞인다(multimodal-dynamics Chain 1의 안전장치).

### 2.4 Emotion 이외의 요소(visual, semantic content)를 decoding하는 것은 아닌가
위험이 높다. 국소 "정서" 신호가 VLM 정서 vector 투영(AI 추정)이므로 장면 의미를 함께 싣는다. 이를 누적한 모델이 이기면 지속되는 것은 정서가 아니라 **상황 모델(의미 맥락)**일 수 있다(frontier-ai 자신의 U1: 정서 표상이 상황 표상의 투영인가). V-JEPA surprise는 물리, 시각 예측오차라서 정서와의 관계도 간접적이다(제안자 반론 (e)에 동의). 또 Axis U 관점에서, 지속성의 대상이 "참가자가 느낀 정서의 지속"인지 "정서 관련 신경 신호의 지속"인지 구분해야 한다. 연속 자기보고가 없으므로 결론은 후자로만 쓴다.

### 2.5 현재 Dataset으로 검증할 수 있는가
* Emo-FilM: 첫 시청 fMRI 참가자와 생리(PPG, 호흡, EDA)가 있어 가능하다. 단 제공 전처리본은 high-pass(sigma 50 s)가 적용되어 수십 초 이상의 시간 상수를 왜곡하므로 raw 재전처리가 필요하다(geometry-info C5 지적). 영화 한 편이 한 run이라 시간 상수 추정 가능 범위는 run 길이로 제한된다. 보유 영상이 크레딧 절단 연구 판본인지 미확인이다(G1).
* Horikawa: 지속 대 재호출 판별에는 더 나은 시험대다(2.3절). raw BIDS 연속 시계열이 필요하다.
* Spacetop alignvideo: 영상이 짧고 사이에 평정 구간이 있어 시간 상수 추정에는 약하다.

### 2.6 더 강력한 모델이나 분석 방법이 있는가
1. **명시적 상태공간 모형:** HRF와 AR 잡음을 모형 안에 둔 rSLDS나 선형 상태공간 모형으로 시간 상수를 추정한다. 합성곱 회귀자에 leaky integrator를 붙이는 방식은 HRF 오지정과 BOLD 자기상관이 가짜 지속성을 만든다(frontier-ai T5의 주의와 같음).
2. **재호출의 직접 측정:** 내용 유사도 회귀자 대신 "시점 t의 신경 패턴이 과거 정서적으로 비슷한 장면의 신경 패턴을 시각 유사도 이상으로 닮는가"를 교차검증 패턴 유사도로 직접 잰다. 회귀자 설계보다 가정이 적다.
3. **신체 채널:** 같은 참가자 EDA 회복 시간을 지속성의 독립 지표로 둔다. 신경 지속 τ와 EDA τ가 맞으면 정서 관성 해석이 강해진다(geometry-info C5와 같은 방향).
4. **서사 수준 예측:** V-JEPA 2 문맥(수 초)으로는 서사 예측을 못 하므로 대사 transcript의 LLM surprisal을 함께 넣는다(제안자 반론 (a)에 동의).

### 2.7 결과가 기대와 다를 때도 과학적으로 유의미한가
그렇다. 지속 모형도 재호출 모형도 국소 모형을 이기지 못하면, 뇌의 정서 관련 신호가 LLM처럼 장면 국소적이라는 뜻이다(arXiv:2604.07729 5.3절의 LLM 국소성 결과와 같은 방향). 이것은 AI와 뇌 정서 표상의 비교(Axis R의 Model-internal Emotion Representations)에 직접 정보를 준다. 시간 상수가 HRF 규모와 같으면 BOLD 해상도에서 정서 관성은 보이지 않는다는 결론이 된다. 다만 이런 음성 결과를 해석하려면 HRF 다양화와 위상 무작위화 null로 검출력을 먼저 보여야 한다.

### 2.8 수정안
* **M1. 두 프로젝트로 분리:** (i) 예측 신호 위계: 세 신호를 Emo-FilM의 Suddenly, Predictable appraisal 평정과 참가자 EDA에 대응시킨다(frontier-ai T1과 결합). (ii) 지속 대 재호출: 주 시험대를 Horikawa 고정 순서의 "비슷한 내용의 장거리 재등장" 구조로 두고, Emo-FilM을 보조로 쓴다. 런 안 순환 이동 null로 클립 쌍 효과를 통제한다.
* **M2. 국소 정서 신호의 라벨 출처 셋:** 인간 consensus 1 Hz(별도 평정자 규범), VLM 투영(AI 추정), 참가자 EDA(신체). 지속성 결론은 최소한 인간 consensus와 신체 채널에서 재현될 때만 낸다.
* **M3. 의미 지속 대조:** 같은 ROI에서 캡션 embedding 주성분(정서 배제)에 같은 τ 적합을 한다. τ_정서 > τ_의미일 때만 "정서 특이 지속"으로 쓴다.
* **M4. raw 재전처리(50 s high-pass 미적용)와 식별 가능한 τ 범위의 사전 보고.**
* **M5. 재호출을 신경 패턴 유사도로 직접 측정**(2.6 2번).
* **M6. 해석 규칙:** "정서 경험의 지속"이 아니라 "정서 관련 신경 신호의 지속"으로 쓴다. LLM 국소성과의 비교 결과는 AI-뇌 차이 결과로 별도 보고한다.
* 태그: label-provenance = 일차 분석은 라벨 없음(참가자 뇌, 참가자 생리, 모델 신호), 국소 정서 신호는 AI 추정(VLM) / 별도 평정자 규범(consensus) / 신체(EDA)로 나눠 표기. evidence-level = R0.

---

## 3. VD-P4: 생성기의 정서 중립화를 재는 affect round-trip audit

**요약.** Horikawa 원 프레임 → 정답 CLIP, VDVAE latent → NSD로 학습된 생성기(SDXL unCLIP, Versatile Diffusion)로 재생성 → C&K 비노출 정서 평가기와 소규모 인간 평정. 뇌가 개입하지 않는 이 경로의 정서 손실을 "생성기 고유 정서 중립화"로 두고, 뇌 해독 latent 경로에서는 그 위에 더해진 손실만 뇌에 귀속한다. 또 뇌에서 해독한 캡션(의미)을 고정하고 정서 방향만 다른 두 후보를 생성한 뒤, 뇌 해독 image latent에 더 가까운 쪽을 고르는 2AFC로 "뇌 latent에 의미와 별개인 정서 방향 정보가 있는가"를 본다.

### 3.1 이미 연구된 것은 아닌가
* **검색:** WebSearch "fMRI image reconstruction emotional content preserved valence arousal evaluation diffusion decoding emotion fidelity 2024 2025 2026", 2026-11-12.
* **결과:** fMRI 재구성 이미지의 정서(valence, arousal) 충실도를 평가한 연구는 찾지 못했다. 재구성 survey(검색 요약만 봤고 식별자를 확인하지 않아 근거로 쓰지 않음)도 정서 평가를 언급하지 않았다. vision-decoding Round 1도 MindEye2, Brain-IT, NSD-Imagery, MIRAGE 본문에 정서 평가가 없음을 확인했다(arXiv:2403.11207, arXiv:2605.17198). 정답 latent로 재생성한 이미지를 상한으로 쓰는 것은 재구성 연구의 관행이다(제안자 반론 (1)). 정서 쪽 가장 가까운 선행은 텍스트 출력의 EmoMind(arXiv:2605.16739)다.
* **판정:** partially (상한 비교 관행과 텍스트 정서 해독은 선행, 이미지 정서 축 audit는 미발견).

### 3.2 단순한 모델 적용에 불과한가
대체로 평가 인프라다. round-trip 자체는 새 과학 질문이 아니라 이후 R1 분석(재구성, 편집)의 공통 통제다. 이것은 결함이 아니라 성격이다. generative-counterfactual의 편집 연구(CH1, CH2, GC-P2)가 같은 계열 생성기를 쓰면 같은 중립화가 섞인다는 지적은 정확하고, 그래서 인프라로서의 가치가 크다.

### 3.3 실제로 Neuroscience Question을 해결하는가
약하다. 신경과학 질문을 담은 것은 2AFC 부분뿐이다("뇌 latent에 의미와 별개인 정서 방향 정보가 있는가"). 그런데 2AFC는 **CLIP image latent 공간에서의 거리**로 판정한다. 정서 방향이 다른 두 생성 이미지는 색, 표정, 조명 같은 시각 feature로 다르므로, 2AFC 성공은 "뇌 latent에 정서 진단적 시각 정보가 있다"를 뜻하지 "뇌가 정서를 표상한다"를 뜻하지 않는다. vision-decoding 0.3절 L1(image-computable 상한)에 따라 이 정보는 portrayed 또는 규범 수준이다. 입력 영역이 시각피질이면 편도체, 섬엽, vmPFC 정보는 처음부터 빠진다(vision-decoding 0.2절).

### 3.4 Emotion 이외의 요소(visual, semantic content)를 decoding하는 것은 아닌가
3.3절대로 위험이 높다. 평가기도 문제다. CLIP zero-shot 정서 프롬프트와 EmoSet 학습 분류기(arXiv:2307.07961)는 이미지의 정서를 인식하는 모델이라 Axis U로는 perceived x AI 추정이다. 인간 평정을 붙여도 지시문이 "이 이미지가 표현하는 정서"면 portrayed, "보면 느낄 정서"면 felt-보고다. 지시문을 명시하지 않으면 round-trip 손실의 의미가 정해지지 않는다. EmoNet은 Horikawa 자극으로 학습되어 평가기로 쓰면 안 된다(제안자도 C&K 비노출을 명시).

### 3.5 현재 Dataset으로 검증할 수 있는가
가능하다. Horikawa 원본 비디오(보유)에서 프레임을 뽑고, NSD(보유)로 학습된 공개 생성기와 VDVAE를 쓴다. 뇌 경로에는 Horikawa fMRI로 CLIP latent decoder를 학습해야 한다(5명 x 2,181개). 제약: (1) 프레임 하나를 고르면 움직임이 싣는 정서가 손실된다(제안자 반론 (3)). (2) EmoSet은 정지 이미지 학습이라 영상 프레임에 도메인 이동이 있다. (3) 소규모 인간 평정은 신규 수집이고, Horikawa 비디오 파생 이미지를 새 평정자에게 보여 줄 수 있는지는 요청 양식 조건에 달렸다(미확인).

### 3.6 더 강력한 모델이나 분석 방법이 있는가
1. **생성 없는 latent 수준 probe를 0단계로:** 정답 latent와 뇌 해독 latent 각각에서 C&K 34/14 규범 평정을 선형 probe로 예측하고, 두 성능의 차이를 "뇌 해독 손실"로 정의한다. 생성기를 거치지 않으므로 생성기 중립화와 독립적이다. round-trip은 "이미지 수준 정서 충실도" 주장을 할 때만 필요하다.
2. **평가기 다중화와 보정:** C&K 비노출 평가기 둘 이상 + 소규모 무작위 인간 평정으로 PPI 보정(doi:10.1126/science.adi6000)하고 평가기 간 불일치를 보고한다(vision-decoding I1과 같은 방향).
3. **video latent:** 다중 프레임 집계나 video 모델 latent를 병행해 움직임 관련 손실을 따로 보고한다.
4. **Mind captioning 반복 클립으로 decoding 상한:** 72클립 반복에서 decoding의 noise ceiling을 구해 "뇌 해독 손실" 중 측정 잡음 몫을 분리한다.

### 3.7 결과가 기대와 다를 때도 과학적으로 유의미한가
그렇다. round-trip 손실이 작으면(생성기가 정서를 보존) 기존 재구성의 정서 손실은 뇌 해독 단계 탓이라는 결론이 나오고, 크면 기존 재구성 연구의 "정서 중립적 출력"은 상당 부분 생성기 인공물이라는 결론이 나온다. 둘 다 재구성 분야와 정서 연구에 쓸모 있다. 2AFC가 엄격한 대조 아래 우연 수준이면 "시각 영역 해독 latent는 의미를 넘는 정서 진단 정보를 싣지 않는다"는 결과이며, 시각피질에 정서 schema가 들어 있다는 주장(doi:10.1126/sciadv.aaw4358)과 대조할 수 있다.

### 3.8 수정안
* **M1. 0단계 latent probe 추가**(3.6 1번). 생성기 audit는 이미지 수준 주장에만 쓴다.
* **M2. 2AFC 대조쌍:** 정서 방향이 다른 후보쌍과 CLIP 거리를 맞춘 **비정서 시각 속성 차이 후보쌍**(예: 색온도만 다름)을 함께 두어 우연 기준을 경험적으로 만든다. 편집 가족을 여러 개 써서 결과가 유지되는지 본다(제안자 반론 (4)에 동의).
* **M3. 해석 범위:** 2AFC 성공은 "뇌 해독 시각 latent의 정서 진단적 시각 정보(portrayed 수준)"로 쓴다. 정서 표상이나 경험으로 쓰지 않는다.
* **M4. 평가기와 인간 평정의 지시문을 Axis U 대상 값으로 명시**(portrayed / perceived / felt). EmoNet 사용 금지.
* **M5. NSD 음성 대조 유지**(중립 분포에서는 손실이 작아야 한다는 제안자 예측). 여기에 Horikawa 안의 정서 강도별 층화를 더해, 손실이 고강도 클립에 몰리는지 본다.
* 태그: label-provenance = 원 자극 felt x 별도 평정자 규범, 재생성 이미지 평가는 perceived x AI 추정 또는 지시문에 따른 신규 별도 평정자. evidence-level = R1(round-trip, 2AFC), 인간 평정 추가 시 R2. insilico-vs-observed = in-silico(round-trip), 혼합(뇌 경로).

---

## 4. 세 제안에 공통으로 남기는 의견

1. **세 제안 모두 "정서 대 의미"를 "정서 대 지각"과 혼동할 위험이 있다.** 의미(캡션 embedding)를 고정하거나 통제한 뒤 남는 신호는 지각 단서(색, 표정, 움직임)일 수 있다. 정서 고유 주장을 하려면 의미 통제와 별도로 저수준 지각 통제(비정서 지각 편집, 저수준 생태 통계 feature, doi:10.1038/s41467-024-53668-6)가 필요하다.
2. **라벨 출처를 판정 단계마다 표기하자.** 세 제안 모두 별도 평정자 규범, 신규 평정, AI 평가기를 섞어 쓴다. 각 결론 문장이 어느 라벨 출처에서 나왔는지 Axis U 값으로 적어야 "인식 질문"과 "경험 질문"이 섞이지 않는다.
3. **생성을 쓰기 전에 자연 자극 선택을 먼저 하자.** 같은 Cowen & Keltner 비디오 2,180개와 두 코호트 11명이 있으므로, 모델 예측이 갈리는 자연 클립을 고르는 것만으로 R0 판정이 가능하다. 생성은 자연 자극으로 채울 수 없는 영역만 채우는 것이 생성기 교란을 줄인다.

## 5. 검색 기록

* WebSearch 4건(2026-11-12): GC-P2 2건, FA-P3 1건, VD-P4 1건. 질의는 각 절 1.1, 2.1, 3.1에 적었다.
* Crossref와 PubMed: doi:10.1371/journal.pone.0308295 서지와 초록 확인(근거로 사용, `literature.jsonl` 추가).
* 검색 요약에만 나와 근거로 쓰지 않은 것: MooD(VA 기반 의미 제어 편집), fMRI 재구성 survey, 지속 정서 FC 분류 연구(bioRxiv 판만 확인), MindCanvas preprint.
