# Round 2: Cross-Agent Exchange (multimodal-dynamics, 제안 ID 접두어 MD)

* 에이전트: multimodal-dynamics (Axis D, M, 외부 분야 Neuroaesthetics)
* 기준일: 2026-11-12
* 절차: `reference/protocols.md` P2 + Coordinator 추가 요구(제안 ID, label-provenance, evidence-level, 질문 8개)
* 읽은 파일: 다른 10개 에이전트의 `round1.md`(0, 1, 3, 4절 전부, 6절은 내 Axis와 겹치는 chain 위주: frontier-ai CH2, CH3, geometry-info C5, systems-neuro Chain 6, encoding-foundation Chain 7, brain-inspired Chain 7, generative-counterfactual CH4), `outputs/axis_encyclopedia.md` 0절과 2절, `outputs/STAGE_STATUS.md` 사용자 결정 기록, `outputs/literature/literature_db.csv`(인용할 ID의 verified 여부 조회)
* 표기: label-provenance는 `대상(portrayed / perceived / felt) / 주체(본인 / peer / 별도 평정자 규범 / AI 추정)`, evidence-level은 R0 상관, R1 모델 내 개입, R2 새 행동 평정, R3 새 fMRI 자극 조작, R4 뇌 개입(axis_encyclopedia 0.2절). [본문] 원문 확인, [초록] 초록만, [db] literature_db.csv의 다른 에이전트 기록에 의존, [추론] 본 에이전트 추론.
* 이번 라운드에서 새로 식별자 경로(PubMed 메타데이터, PMC 전문)로 확인해 `literature.jsonl`에 추가한 논문 7편: 10.1093/scan/nsab112, 10.1126/sciadv.adw1464, 10.1093/scan/nst169, 10.1016/j.biopsycho.2017.07.020, 10.1093/cercor/bhx290, 10.1002/hbm.25277, 10.1002/hbm.25640. 총 58편.

---

## 0. Round 1 판정의 자기 수정 (선행 수행 재검색)

Coordinator가 알려 준 교훈(Stage 2 표본에서 "no"의 25%가 실제로는 선행 있음)에 따라 내 Round 1 chain의 already_done을 다시 검색했다.

| Round 1 chain | 이전 판정 | 재검색 경로 | 새로 찾은 선행 | 수정 판정 |
|---|---|---|---|---|
| Chain 1 Horikawa 정서 이월 | no | PubMed: `(carryover OR carry-over OR "sequential effects" OR "previous trial" OR hysteresis) AND (emotion OR affective) AND fMRI AND (video OR film OR movie OR clip)`, 2015년 이후. WebSearch 1회 | 정서 영화 블록 뒤 휴지기 연결성 이월: Borchardt 2018 (10.1093/cercor/bhx290 [초록]), Gaviria 2021 HBM (10.1002/hbm.25277 [초록]), Gaviria 2021 NeuroImage (10.1016/j.neuroimage.2021.118377 [db]) | **partially**. 블록-휴지 이월은 있다. 연속 짧은 클립 사이에서 다범주 정서 정보가 다음 클립 패턴에 남는지는 여전히 못 찾음 |
| Chain 3 소리가 만드는 정서 | partially | PubMed: `(soundtrack OR "film music" OR "background music" OR "source separation") AND fMRI AND (emotion OR affective) AND (movie OR film)` | 같은 영상에 음악만 바꾼 fMRI: Pehrs 2014 (10.1093/scan/nst169 [초록], aSTG가 FG-amygdala 결합 게이팅), Bezdek 2017 (10.1016/j.biopsycho.2017.07.020 [초록], 서스펜스, 음악 일치성 효과 없음), Shany 2021 (10.1002/hbm.25640 [초록]) | **partially 유지, 근거 보강**. 통제 장면의 음악 조작(R3 수준)은 있다. 자연주의 영화 전체에서 음원별(대사, 음악, 효과음) 정서 항목 기여 지도는 못 찾음 |
| Chain 4 정서 시간 수용창 | partially | systems-neuro Round 1 Chain 6의 인용 확인 후 PubMed MCP로 본문 열람 | Lettieri 2022 (10.1093/scan/nsab112 [본문]): 우측 TPJ, dPFC의 chronotopic 지도, 정서 보고 최적 시간 척도 약 3~11분 | **partially, 선행이 더 가까움**. 남는 공백: 정서 항목별(50개 CPM 항목) 시간 척도, 자극 측 시간 척도(모델 문맥 길이), 소리 유무, 짧은 클립과의 대비 |
| Chain 6 미적 하이라이트 | no | WebSearch 1회(영화 fMRI 미적 하이라이트, DMN, ISC, 정서 강도 해리) | valence와 arousal이 다른 네트워크 ISC를 조절한다는 연구는 있으나 미적 하이라이트 자체는 없음 | no 유지 (검색 1회 수준이라 Round 3에서 재확인 필요) |
| Chain 7 동역학 비교(DSA) | no | WebSearch `"dynamical similarity analysis" fMRI emotion OR affect OR naturalistic` | 없음 | no 유지 |
| Chain 2 다중모달 surprise와 정서 경계 | partially | WebSearch 1회 | 학회 초록 수준만. 단 팀 안에서 frontier-ai CH2가 거의 같은 질문을 독립 제안 | partially 유지. 팀 내 중복은 MD-P5로 조율 |

arXiv API 검색은 이번 라운드에 429(rate exceeded)로 실패해 우회하지 않았다. 위 판정은 PubMed와 WebSearch 범위다.

---

## 1. 가져온 아이디어 (다른 에이전트의 문헌에서)

### I-1. 영화 후 washout 이완과 line attractor 시간상수 (geometry-info)
* 출처: geometry-info Round 1 P7, C5. 근거: Nair 2023 (10.1016/j.cell.2022.11.027 [db, 초록]), Vinograd 2024 (10.1038/s41586-024-07915-x [db, 본문]), Gaviria 2021 (10.1016/j.neuroimage.2021.118377 [db]).
* 가져오는 내용: 정서 관성을 '정서 잠재 차원의 이완 시간상수'로 정의하고, Emo-FilM 영화 전후 90 s washout을 자연 실험으로 쓰는 발상.
* 내 쪽 변형: 내 Round 1 Chain 1(Horikawa의 2 s 휴지 사이 클립 이월)은 같은 이완 곡선의 **초기 몇 초**를, washout은 **수십 초**를 본다. 두 데이터를 하나의 이완 모형으로 묶으면 시간 척도 전 구간이 덮인다(MD-P1).

### I-2. Mind captioning 코호트의 반복 테스트 순서 (vision-decoding)
* 출처: vision-decoding Round 1 0.1절. 근거: Horikawa 2025 (10.1126/sciadv.adw1464 [본문, 내가 PMC 전문으로 Methods 재확인]).
* 확인한 사실 [본문 Methods]: 학습 세션 2,180개 비디오는 pseudorandom 순서로 1회씩이며 **이 순서는 6명 모두 같다**. 테스트 세션 72개 비디오는 5회씩, **런 안에서 pseudorandom** 순서로 제시된다. 블록은 10 s 이상(짧은 비디오 반복 재생), 블록 뒤 2 s 휴지, 런마다 평가 블록 3~4개 무작위 삽입, TR 1 s, 4 s shift 후 블록 평균.
* 가져오는 내용: 테스트 세트에서는 **같은 클립이 서로 다른 선행 클립 뒤에 나온다**. Horikawa 2020의 "5명 동일 순서" 때문에 섞이던 '클립 쌍 효과'와 '정서 이월'을 클립 정체성을 고정하고 분리할 수 있다. 또 인간 캡션이 '정서를 쓰지 말라'는 지시로 수집되어(Discussion), 내 Round 1 Chain 8(Horikawa 미적 정서)의 기술 의미(description) 통제 변수로 쓸 수 있다.
* 미확인: Horikawa 2020과 Mind captioning 학습 세션 순서가 같은지, 두 코호트의 피험자 중복 여부, 저장소의 events 파일 세부.

### I-3. LLM 정서 표상의 '국소성 vs 지속성' (frontier-ai)
* 출처: frontier-ai Round 1 U2, CH3. 근거: Sofroniew 2026 (arXiv:2604.07729 [db, 본문 5.3절]).
* 가져오는 내용: LLM 정서 vector는 현재 맥락의 정서 개념을 국소적으로 추적하고 지속 상태를 유지하지 않는다는 보고. 내 이월(carry-over) 질문을 "뇌는 LLM과 달리 지속 정서 상태를 갖는가"라는 **AI-뇌 비교 질문**으로 다시 쓸 수 있다. 같은 Horikawa 클립 열을 VLM에 연속 입력했을 때 모델 정서 vector의 이월과 뇌 이월을 같은 지표로 비교한다.

### I-4. MLLM 정서 추정의 맥락 반전 실패와 연속 평정 실패 (llm-semantics)
* 출처: llm-semantics Round 1 P3, P5. 근거: Asanuma 2025 (10.1038/s41598-025-14961-6 [db, 본문]: 단일 프레임으로 정서가 정해지는 비디오에서는 잘 맞고 맥락 반전 비디오와 신체 정서에서 실패), Melhart 2025 GameVibe (arXiv:2502.04379 [db, 본문]: 비디오 단위 일치가 시간 연속 일치를 보장하지 않음).
* 가져오는 내용: Horikawa 짧은 클립 안에도 **시간 맥락이 있어야 정서가 정해지는 클립**이 있다는 단서. 내 Axis D의 "정서 시간 수용창"을 클립 단위로 내릴 수 있다(MD-P6).

### I-5. AI 라벨 하류 추론의 통계 보정 (adversarial-reviewer)
* 출처: adversarial-reviewer Round 1 U5, D4. 근거: alt-test (arXiv:2501.10970 [db, 본문]), prediction-powered inference (10.1126/science.adi6000 [db, 본문]).
* 가져오는 내용: 내 Round 1 U8(AI 연속 주석의 시간축 타당성)을 "상관이 높다" 수준이 아니라 **Emo-FilM 평정자별 원자료를 대체 평정자 기준으로 쓴 alt-test**로 판정하는 절차.

### I-6. 전역 신호의 자율신경 결합과 hybrid 상태 모형 (systems-neuro)
* 출처: systems-neuro Round 1 U2, U7. 근거: Bolt 2025 (10.1038/s41593-025-01945-y [db, 본문]), rSLDS (Linderman 2017, proceedings.mlr.press v54/linderman17a [db, 본문]).
* 가져오는 내용: (a) 내 Round 1 U6("일반화되는 arousal은 감각 강도인가")에 **자율신경-혈관 성분**이라는 세 번째 후보를 더해 3원 분해로 만든다. (b) Chang 2021이 제안한 hybrid 연속-이산 모형의 검증 문헌으로 rSLDS를 쓴다(내 Round 1 9절 3번의 빈칸 해소).

### I-7. 기분 momentum (brain-inspired)
* 출처: brain-inspired Round 1 P-7, Chain 7. 근거: Eldar 2016 (10.1016/j.tics.2015.07.010 [db, 본문]).
* 가져오는 내용: 내 Round 1 Chain 5(연속 경험에서 회고 평가로)의 요약 규칙 후보에 peak, end, 평균 외에 **momentum(정서 변화의 누적)**을 넣는다(MD-P8).

### I-8. 영화 음향 3-stem 분리와 결론 수준 사다리 (generative-counterfactual)
* 출처: generative-counterfactual Round 1 0절, CH4. 근거: DnR 3-stem 분리 (arXiv:2110.09958 [db, 초록]), HT Demucs (arXiv:2211.08553 [db, 초록]).
* 가져오는 내용: 내 Chain 3의 음원 분리 도구, 그리고 관찰 분석(R0)과 in-silico 음악 교체(R1)를 같은 질문의 두 층으로 구분하는 틀.

---

## 2. 보내는 제안

### MD-P1 → geometry-info: 클립 사이 이월과 washout 이완을 하나의 이완 모형으로
* **제안 내용:** 너희 C5(Emo-FilM 영화 후 90 s washout의 정서 이완 시간상수)를 우리 쪽 Chain 1(Horikawa 2020과 Mind captioning의 2 s 휴지 사이 클립 이월)과 묶어 검증하거나 확장할 수 있다. 같은 정서 잠재 차원(평정으로 정의)에 대해 (a) 짧은 간격 이월(Horikawa, Mind captioning, 초 단위), (b) washout 이완(Emo-FilM, 수십 초)을 하나의 leaky integrator 또는 line-attractor식 이완 모형으로 적합한다. 같은 영역의 시간상수가 두 척도에서 일관되면 '정서 관성 차원'의 강한 증거, 짧은 간격에서만 보이면 HRF 잔여나 시각 적응일 가능성이 크다. Mind captioning 테스트 세트(72개 x 5회, 런 안 pseudorandom)는 **같은 클립의 선행 클립이 바뀌는 자연 변이**를 주므로 Horikawa 2020의 고정 순서 교란을 깬다.
* **관련 Axis:** D(Affective Carry-over vs Hemodynamic Spillover), K(Dynamical Attractors), E, Q
* **근거 논문 ID:** 10.1016/j.cell.2022.11.027, 10.1038/s41586-024-07915-x, 10.1002/hbm.25277, 10.1093/cercor/bhx290, 10.1126/sciadv.abf7129, 10.1038/nn.4468, 10.1162/imag_a_00517, 10.1126/sciadv.adw1464
* **가능한 데이터셋:** Horikawa 2020(raw BIDS 연속 시계열), Mind captioning(ds005191, TR 1 s), Emo-FilM(washout, 생리)
* **예상되는 반론과 대응:**
  1. "2 s 휴지에서는 HRF 꼬리가 이월을 만든다." 대응: Mind captioning은 TR 1 s라 deconvolution이 유리하고, 블록 길이 변이(10 s~수십 s)에 따른 이월 감쇠를 HRF 예측 곡선과 비교한다. 같은 클립을 다른 선행 클립 뒤에 둔 비교는 HRF 잔여가 선행 클립의 '정서 내용'에 따라 달라지는지만 본다.
  2. "공개 전처리본은 블록 평균이라 이월이 이미 섞여 있다." 대응: raw 재전처리 필수. Emo-FilM 제공본의 high-pass(sigma 50 s, geometry-info C5 주의)도 같은 이유로 재전처리.
  3. "라벨은 규범 평정이라 참가자 상태의 이월이 아니다." 대응: 결론을 '자극 정서 정보의 신경 이월'로 한정. Emo-FilM에서는 fMRI 참가자 EDA 회복으로 간접 확인.
  4. "Mind captioning의 평가 블록(캡션 일치도 판단)이 순서를 끊는다." 대응: 평가 블록 직후 클립은 따로 분류해 공변량 처리.
* **label-provenance:** 정서 차원 정의는 perceived/felt 혼합 / 별도 평정자 규범(Horikawa MTurk, Emo-FilM consensus). 이완 측정 자체는 라벨 없음(뇌만).
* **evidence-level:** R0. insilico-vs-observed: 관찰. G1: 불필요(라벨 + raw). 선행: partially(블록-휴지 이월만, 0절 검색 경로).

### MD-P2 → systems-neuro: transmodal 위치와 시간 척도의 교락에서 '소리'를 떼어 내는 2요인 설계
* **제안 내용:** 너희 Chain 6(정서 정보의 transmodal 위치가 정서 항목의 시간 척도로 예측되는가)은 Horikawa(짧고 무음)와 Emo-FilM(길고 소리 있음)을 비교하므로 너희 스스로 적은 대로 **자극 길이와 소리 유무가 함께 바뀐다**. 우리 쪽 데이터 대비로 이것을 2요인으로 풀 수 있다: 무음 축은 Horikawa와 Mind captioning의 블록 길이 변이(10 s~94 s), 소리 축은 Spacetop alignvideo(20 s~5분 39초, 모두 소리 있음)와 Emo-FilM(6.7~17.1분). 여기에 자극 측 시간 척도를 **모델 문맥 길이 sweep**(Jindal 2026 방식, video-audio MLLM)으로 정의해 정서 항목별 '필요 문맥 길이'를 측정하고, 평정 자기상관 시간 척도와 비교한다. 부분 선행인 Lettieri 2022 chronotopic 지도(polarity, intensity만)를 항목 단위로 확장한다.
* **관련 Axis:** D(Affective Timescale Hierarchy), M(Modality Dependence), E(Cortical Gradients)
* **근거 논문 ID:** 10.1093/scan/nsab112, arXiv:2602.07570, 10.1093/scan/nsad063, 10.1038/s41467-025-68240-z, 10.1126/sciadv.abf7129, 10.1016/j.isci.2020.101060, 10.1126/sciadv.adk6840
* **가능한 데이터셋:** Horikawa, Mind captioning, Spacetop alignvideo, Emo-FilM
* **예상되는 반론과 대응:**
  1. "데이터셋마다 참가자, 스캐너, 라벨 척도가 다르다." 대응: 비교는 각 데이터셋 안의 길이 효과 기울기(같은 데이터셋 안 변이)를 먼저 추정하고, 데이터셋 간에는 기울기 부호와 순위만 비교(Stage 1 수준 2~3).
  2. "Spacetop은 영상 내 연속 평정이 없다." 대응: Spacetop에서는 정서 라벨 대신 모델 문맥 길이 기반 자극 시간 척도와 뇌 ISC 시간 척도만 쓰고, 정서 항목별 분석은 Emo-FilM에서 한다.
  3. "긴 문맥 feature는 서사 의미와 공선적이다." 대응: 같은 문맥 길이의 정서 배제 기술(정서 단어 없는 캡션 embedding)을 nuisance로 넣는다(llm-semantics L1 층).
* **label-provenance:** Emo-FilM perceived/felt 혼합 / 별도 평정자 규범, Spacetop felt / 본인 사후, 모델 문맥 sweep은 AI 추정.
* **evidence-level:** R0. insilico-vs-observed: 관찰(모델 feature는 회귀자). G1: 모델 sweep은 필요(보유), 평정 시간 척도는 불필요. 선행: partially(10.1093/scan/nsab112).
* overlap: Emo-FilM 연구 (시간 정보의 뇌 기여, 부분), EmoViS (Horikawa gradient 기원, 부분)

### MD-P3 → encoding-foundation: in-silico 감각 박탈을 관찰 데이터의 '자연 모달리티 변이'로 보정하기
* **제안 내용:** 너희 Chain 7(TRIBE v2 modality dropout으로 초감각 정서 부호 중 자극 계산 가능한 부분 추정)과 개념 4.2("modality dropout = in-silico 감각 박탈")는 내 Round 1 개념 3과 독립적으로 수렴했다. 우리 쪽에서 두 가지 관찰 기준점을 더할 수 있다. (a) **실제 무음 관찰**: 같은 Cowen & Keltner 비디오를 무음으로 본 두 코호트(Horikawa 2020, Mind captioning)가 있으므로 TRIBE v2의 '비디오만' 예측을 같은 자극의 실측과 직접 비교할 수 있다. (b) **자연 음악 변이**: Emo-FilM 안에서 음악 stem 에너지가 높은 구간과 없는 구간이 자연적으로 섞여 있으므로, 관찰 fMRI에서 음악 유무에 따른 정서 encoding 차이(R0)를 먼저 추정하고 in-silico 음악 제거 효과(R1)가 그 방향과 크기를 재현하는지 본다. 덧붙여 TRIBE(v1)의 입력 창은 비디오가 직전 4 s, 텍스트가 직전 1,024단어, 오디오가 60 s 구간(양방향)이고, 그 위 transformer가 N개 TR 창 안에서 시점 사이 정보를 교환한다(arXiv:2507.22229 2.3절 [본문]). 따라서 창 안의 **자극 구동** 시간 통합은 예측할 수 있지만, 창을 넘는 지속과 자극으로 계산되지 않는 **내생** 누적은 설계상 예측하지 못한다. 특히 무음, 무대사인 Horikawa와 Mind captioning에서는 입력이 비디오 4 s 창뿐이다. 관찰 반응에서 group 예측을 뺀 잔차를 시간 척도별(이월, 누적)로 분해하면, 너희 Residual Encoding Sub-axis가 '자극 계산 불가능한 성분'을 시간 척도로 특정하게 된다. TRIBE v2의 창 설정은 이번에 확인하지 않았다.
* **관련 Axis:** M, H(Residual / Idiosyncratic Encoding), F(In-silico Representational Fidelity), D
* **근거 논문 ID:** arXiv:2605.04326, arXiv:2507.22229, 10.1126/sciadv.adk6840, 10.1126/sciadv.adw1464, arXiv:2605.16739, 10.1093/scan/nst169
* **가능한 데이터셋:** Horikawa, Mind captioning, Emo-FilM
* **예상되는 반론과 대응:**
  1. "TRIBE v2 공개 checkpoint는 fsaverage5 피질 평균 피험자만 예측하고 피질하가 없다(너희 0절)." 대응: 비교는 피질 parcel로 한정하고 amygdala 결론은 내지 않는다.
  2. "무음 코호트와 TRIBE 학습 피험자가 다르다." 대응: 비교 지표는 관계 기하(RSA)와 정서 축 투영으로, 절대 진폭은 쓰지 않는다(너희 U1과 같은 원칙).
  3. "음악 유무 구간은 장면 종류와 공선적이다." 대응: 같은 영화 안에서 시각 feature를 맞춘 구간 쌍(matched segments)으로 비교하고, 남는 차이는 R0로만 보고.
* **label-provenance:** Horikawa, Emo-FilM 평정은 perceived/felt 혼합 / 별도 평정자 규범. in-silico 예측은 라벨 아님.
* **evidence-level:** R0(관찰 기준점) + R1(in-silico). insilico-vs-observed: **혼합**(반드시 분리 보고). G1: 필요(보유).
* overlap: Emo-FilM 연구 (멀티모달 encoder로 정서 기여 분석, 부분)

### MD-P4 → generative-counterfactual: 음악 stem counterfactual에 '알려진 실험 결과의 in-silico 재현' 관문 두기
* **제안 내용:** 너희 CH4(Emo-FilM 음악 stem 제거, 교체 → TRIBE v2 예측 변화, R1)를 우리 쪽 문헌의 **실제 음악 조작 fMRI 결과**로 먼저 검증할 수 있다. Pehrs 2014는 같은 키스 장면에 행복한 음악, 슬픈 음악, 무음을 붙여 aSTG가 FG-amygdala 결합을 게이팅함을 보였고(R3 수준), Eldar 2007은 정서 음악이 중립 영상과 결합할 때만 amygdala, hippocampus가 올라간다고 보였다. Bezdek 2017은 서스펜스 장면에서 음악 일치성이 기억에 영향을 주지 않았다. 이 세 결과를 Emo-FilM이나 공개 영상 위에서 in-silico로 재현하는지(방향 일치)를 CH4의 **타당성 관문**으로 두자. 재현하지 못하는 영역에서는 CH4의 음악 효과 예측을 해석하지 않는다. 또 R0 층으로 Emo-FilM 관찰 fMRI에서 음악 stem 에너지와 정서 consensus의 상호작용 회귀(음악이 있을 때 정서-뇌 결합이 강해지는가)를 함께 보고해, R1 예측과 R0 관찰의 방향을 대조한다.
* **관련 Axis:** L(Controlled Stimulus Editing), M(Audio Source Decomposition), P, T
* **근거 논문 ID:** 10.1093/scan/nst169, 10.1093/cercor/bhm011, 10.1016/j.biopsycho.2017.07.020, 10.1002/hbm.25640, arXiv:2110.09958, arXiv:2211.08553, arXiv:2605.04326, arXiv:2509.21381
* **가능한 데이터셋:** Emo-FilM(소리 있음), Spacetop alignvideo(소리 있음, 재현 확인용)
* **예상되는 반론과 대응:**
  1. "선행 실험은 피질하(amygdala) 결과인데 TRIBE v2 공개판은 피질만 있다." 대응: Pehrs 2014의 aSTG, FG 같은 피질 노드 효과만 재현 대상으로 삼고, amygdala 부분은 관문에서 제외한다고 명시.
  2. "선행 실험 자극은 우리에게 없다." 대응: 같은 조작 구조(같은 영상 + 음악 정서가만 교체)를 Emo-FilM 장면에서 재구성. 방향 재현만 본다.
  3. "stem 분리 잡음이 효과를 만든다." 대응: 너희 설계대로 원 stem 재합성 판본을 null로.
* **label-provenance:** 음악 정서가는 perceived / AI 추정(CLAP 등) 또는 별도 평정자 규범(Emo-FilM). 선행 실험의 평정은 각 논문 참가자.
* **evidence-level:** R1(in-silico) + R0(관찰 대조). 선행 실험 결과 자체는 R3지만 우리 분석이 R3가 되는 것은 아니다. G1: 필요(보유, 영화별 CC 파생물 조건 확인 필요).
* overlap: Emo-FilM 연구 (부분)

### MD-P5 → frontier-ai: 정서적 놀람의 예측오차 수준에 '오디오 수준'과 '평정자 반복 시청' 문제를 더하기
* **제안 내용:** 너희 CH2(편도체, 섬엽, vmPFC 반응과 suddenness, predictability appraisal이 pixel, latent 물리, 서사 의미 예측오차 중 무엇과 결합하는가)와 내 Chain 2(다중모달 surprise와 정서 경계)는 같은 질문이다. 합칠 때 두 가지를 더하자. (a) **오디오 수준 예측오차**: 영화 정서는 음악과 음성에 크게 의존하므로(Lettieri 2024의 모달리티별 유발 정서 차이, Pehrs 2014) 음악, 음성 모델의 surprise를 네 번째 수준으로 넣지 않으면 'latent 물리'에 소리 surprise가 흡수될 수 있다. (b) **평정자 반복 시청**: Emo-FilM 평정자는 항목마다 모든 영화를 다시 보며 최대 6번 같은 영화를 봤다(Ma & Kragel Methods 'Emotion ratings', Stage 1). Suddenly, Predictable 평정은 처음 보는 fMRI 참가자의 놀람보다 **앞당겨지거나 약해질 수 있다**(Lee 2021: 반복 시청 시 뇌 사건 패턴이 앞당겨짐). 그래서 (i) 평정자별 원자료에서 첫 항목(첫 시청) 평정자와 나중 항목 평정자를 나눠 Suddenly 시계열의 지연과 진폭을 비교하고(항목 순서 기록 여부는 미확인), (ii) 처음 보는 fMRI 참가자의 EDA 위상 반응을 놀람의 1차 지표로 쓰자. 마지막으로 연속 결합 외에 **경계(change point) 분석**을 함께 해 오차형 경계(놀람)와 불확실성형 경계(서스펜스, Bezdek 2017)를 Nguyen 2026의 신경 순서로 구분한다.
* **관련 Axis:** D(Emotional Event Boundaries, Temporal Prediction), N(Predictive Coding), M, U(Label Provenance)
* **근거 논문 ID:** arXiv:2502.11831, arXiv:2506.09985, 10.7554/eLife.64972, 10.7554/eLife.107955, 10.1111/cogs.13343, 10.1038/s41467-023-42241-2, 10.1126/sciadv.adk6840, 10.1016/j.biopsycho.2017.07.020, 10.1038/s41467-025-68240-z
* **가능한 데이터셋:** Emo-FilM(평정, EDA, fMRI), Spacetop alignvideo(신경 경계 재현, 평정 없음)
* **예상되는 반론과 대응:**
  1. "평정자 항목 순서가 원자료에 없으면 (i)은 불가능." 대응: 그 경우 (ii) EDA 기준과 '평정 지연 추정'(평정 시계열과 모델 surprise의 교차상관 최대 지연)으로 대체.
  2. "오디오 surprise 모델이 영화 혼합음에서 신뢰할 만한가." 대응: stem 분리 후 음악과 음성 따로 계산, 분리 잡음은 null로.
  3. "모델 surprise는 참가자 surprise가 아니다." 대응: 너희 CH2 방법론 주의와 같다. in-silico 회귀자로만 쓴다.
* **label-provenance:** Suddenly, Predictable은 perceived/felt 혼합 / 별도 평정자 규범(**반복 시청자**). EDA는 felt 생리 지표 / 본인(첫 시청). 모델 surprise는 AI 추정.
* **evidence-level:** R0. G1: 필요(보유).
* overlap: Emo-FilM 연구 (부분)

### MD-P6 → llm-semantics: MLLM 정서 추정의 '시간 맥락 의존도'를 클립과 항목 단위 변수로 만들기
* **제안 내용:** 너희 P3(맥락 반전 비디오와 신체 정서에서 MLLM 실패)와 P5(연속 평정 타당도)를 우리 쪽 시간 축으로 검증, 확장할 수 있다. (a) **Horikawa 클립의 시간 의존도**: 같은 클립에 대해 단일 프레임 MLLM 평정, 전체 클립 평정, 규범 평정을 비교해 "전체 클립을 봐야 맞는 클립"을 정의한다. 이 클립들의 정서 정보가 긴 시간 수용창 영역(PMC, vmPFC)에서, 단일 프레임으로 충분한 클립은 시각 피질에서 더 잘 decoding되는지 검정한다. (b) **Emo-FilM 항목별 필요 문맥**: 시청각 MLLM에 3 s, 30 s, 영화 처음부터의 요약 문맥을 주고 1 Hz에 맞춘 연속 평정을 받아, 항목별로 어떤 문맥 길이에서 human-human 천장(평정자별 원자료)에 도달하는지 alt-test로 판정한다. love, guilt 같은 느린 항목이 긴 문맥을 요구하면 MD-P2의 항목 시간 척도와 독립적으로 일치하는지 볼 수 있다. (c) Mind captioning의 정서 배제 인간 캡션을 L1(기술 의미) 통제로 쓰면 너희 세 층 분해의 L1이 AI가 아닌 인간 기술로 고정된다.
* **관련 Axis:** C(Perceived Meaning vs Experienced Emotion), D, U(Label Provenance), Q
* **근거 논문 ID:** 10.1038/s41598-025-14961-6, arXiv:2502.04379, arXiv:2501.10970, 10.1162/imag.a.1300, 10.1162/IMAG.a.134, arXiv:2602.07570, 10.1126/sciadv.adw1464, 10.1016/j.isci.2020.101060
* **가능한 데이터셋:** Horikawa, Mind captioning(같은 비디오, 정서 배제 캡션), Emo-FilM
* **예상되는 반론과 대응:**
  1. "단일 프레임 vs 전체 클립 차이는 MLLM의 프레임 샘플링 방식에 좌우된다." 대응: 두 개 이상 모델(Qwen2.5-Omni, video-SALMONN 등)과 프레임 수 sweep으로 견고성 확인.
  2. "Horikawa는 무음이라 오디오 맥락이 없다." 대응: (a)는 시각 시간 맥락만 다룬다고 범위를 명시. 오디오 맥락은 (b) Emo-FilM에서.
  3. "사전학습 오염(Cowen & Keltner 비디오, Blender 영화)." 대응: 모델별 오염 가능성 기록, 결과를 오염 가능 모델과 낮은 모델로 층화.
* **label-provenance:** 규범(별도 평정자) vs AI 추정의 비교 자체가 목적. 대상은 perceived에 가까움(llm-semantics L2).
* **evidence-level:** R0. G1: 필요(보유).

### MD-P7 → emotion-theory: 평정자 불일치와 혼합 정서를 '시간 구조'로 분해하기
* **제안 내용:** 너희 C5(평정자 불일치의 신경 분해: 자극 모호성 vs 개인 특이 반응 vs 측정 잡음)와 C6(혼합 정서: 선형 중첩 vs 창발 상태)을 Emo-FilM 1 Hz 시간 축으로 검증할 수 있다. (a) **불일치의 시간 고정성**: 평정자 쌍의 불일치가 영화 시간에 고정되어 여러 쌍에서 같은 순간에 커지면 자극 모호성, 시간에 고정되지 않으면 개인 특이 반응이나 잡음이다. 시간 고정 불일치가 정서 change point(전이 구간)에 몰리는지, 그 순간에 fMRI 참가자 ISC가 낮아지는지 본다. (b) **혼합 정서의 동역학적 지위**: 긍정 항목과 부정 항목이 함께 높은 구간의 지속 시간 분포, 그리고 그 구간이 단일 valence 상태 사이의 전이에 우연 이상으로 몰리는지 본다. 전이에 몰리면 혼합은 '전이 중간 상태', 독립적으로 오래 지속되면 '별도 상태' 가설을 지지한다. 신경 수준은 Vaccaro 2024의 HMM 접근을 Emo-FilM에서 재현.
* **관련 Axis:** A(Ambivalence / Mixed Emotions), Q(Inter-rater Agreement), D(Emotional Transitions), U
* **근거 논문 ID:** 10.1093/cercor/bhae122, 10.1073/pnas.1702247114, 10.1038/s41467-023-42241-2, 10.1126/sciadv.abf7129, 10.1038/s41467-019-13599-z
* **가능한 데이터셋:** Emo-FilM(평정자별 원자료 공개)
* **예상되는 반론과 대응:**
  1. "평정자 내 z-score라 '함께 높음'의 절대 기준이 없다." 대응: 평정자 내 분위수 기준으로 정의하고 기준 민감도를 보고.
  2. "항목 x 영화당 평정자가 3~4명이라 불일치 추정이 불안정하다." 대응: 영화와 항목을 합친 위계 모형, bootstrap 구간.
  3. "같은 평정자가 긍정과 부정 항목을 동시에 평정하지 않았다(항목별 다른 평정자)." 대응: 혼합 정의는 평정자 간 consensus 수준에서만 가능하다고 한정하고, '한 사람이 동시에 느낀 혼합'이라는 해석은 하지 않는다. 이것이 이 제안의 가장 큰 약점이다.
* **label-provenance:** perceived/felt 혼합 / 별도 평정자 규범(평정자별 원자료).
* **evidence-level:** R0. G1: 불필요.

### MD-P8 → brain-inspired: momentum과 회고 평가, SR 할인율과 정서 시간 척도
* **제안 내용:** 너희 Chain 7(영화 속 느린 뇌 상태가 정서 수준이 아니라 momentum을 추적하는가)을 우리 쪽 Chain 5(연속 경험이 회고 평가로 압축되는 규칙)로 확장할 수 있다. 회고 평가의 요약 규칙 후보(peak, end, 평균, peak-end)에 **영상 끝 시점의 momentum**을 넣고, Emo-FilM fMRI 참가자의 사후 영화 평정과 Spacetop alignvideo 참가자 본인 사후 평정을 무엇이 가장 잘 예측하는지 비교한다. "나쁜 영화였지만 마지막에 나아지는" 영상에서 momentum 모형과 end 모형은 다른 예측을 한다. 아울러 너희 SR 해석(geometry-info U5와 같은 방향)의 할인율 γ를 정서 항목별 시간 척도(MD-P2)와 맞춰 보면, '정서마다 다른 예측 지평'이 SR 모형과 문맥 길이 측정 양쪽에서 같은 순위를 내는지 교차 검증된다.
* **관련 Axis:** D(Online-to-Retrospective Integration), N(RL / Computational Value), A, U
* **근거 논문 ID:** 10.1016/j.tics.2015.07.010, 10.1016/j.neuroimage.2018.12.017, 10.3389/fnhum.2021.676032, 10.1037/0022-3514.65.1.45, 10.1038/nn.4650, 10.1038/s41467-025-68240-z
* **가능한 데이터셋:** Emo-FilM(consensus + 참가자 사후 평정), Spacetop alignvideo(본인 사후 7차원)
* **예상되는 반론과 대응:**
  1. "Spacetop에는 영상 내 연속 평정이 없어 momentum을 계산할 수 없다." 대응: Emo-FilM에서 시간축이 검증된 AI 연속 추정(MD-P6 (b))을 Spacetop에 적용하고 '미검증 AI 추정 시계열'로 표기(Stage 1 원칙).
  2. "Spacetop 평정 약 51% 결측, 평정 구간이 영상 끝 HRF와 겹침." 대응: 결측 패턴 분석 선행, 영상 끝 BOLD는 평정 구간 전 창만 사용.
  3. "Emo-FilM 참가자 회고 평정은 영화당 5항목, 길이 약 20%만 덮는다." 대응: 회고 평정이 있는 클립 구간 단위로 분석 단위를 줄인다.
* **label-provenance:** 예측 변수는 perceived/felt 혼합 / 별도 평정자 규범(Emo-FilM) 또는 AI 추정(Spacetop), 결과 변수는 felt / 본인 사후 보고. **관점이 다른 라벨을 잇는 설계**라는 점을 질문 자체에 명시.
* **evidence-level:** R0. G1: Spacetop 궤적 추정에 필요(보유).

---

## 3. 받은 제안에 대한 응답

받은 제안 7개와 참조 1개의 원문(보낸 에이전트 round2.md 2절)을 읽고 답한다. 요약: **수용 3(GI-P3, SN-P2, LS-P3), 수정 4(EF-P7, FA-P3, GC-P4, BI-P5), 반박 0.** 수정 4개 중 3개는 내 MD-P3, MD-P4, Chain 2와 거의 같은 질문이라 "공동 설계로 통합"이 수정의 핵심이다.

### EF-P7 (encoding-foundation): in-silico 감각 박탈과 관찰된 무음 조건의 대조 → **수정 (MD-P3와 통합)**
* 판단: 내 MD-P3(관찰 무음 코호트와 Emo-FilM 자연 음악 변이로 in-silico 감각 박탈 보정)와 같은 질문이다. "감각 박탈" 대신 "입력 제한"으로 부르자는 제안자의 대응에 동의한다(Lettieri 2024의 핵심은 발달 중 감각 경험이라 학습 중 modality dropout과 다르다, 10.1126/sciadv.adk6840).
* 수정안:
  1. (i)의 해석 한정: Lettieri 2024는 모달리티에 따라 **유발되는 정서 자체가 달라진다**고 보고했다(공포는 청각판에서 덜, 경멸은 더). 우리에게는 소리를 뺀 판본의 인간 평정이 없으므로, (i)에서 50항목 평정은 원본(시청각) 평정 그대로 쓰고 결과를 "입력을 제한했을 때 원본 정서 관련 분산 중 예측 가능한 몫"으로만 해석한다. "소리를 빼면 정서가 바뀐다"는 결론은 R2(새 평정) 없이는 내지 않는다.
  2. (ii) 비교는 관계 기하(RSA, 정서 축 투영)로 하고 절대 진폭은 쓰지 않는다. TRIBE v2 공개판은 fsaverage5 피질 평균 피험자 예측이라(encoding-foundation Round 1 0절) 피질 parcel로만 비교한다.
  3. (iii) R0 쪽은 같은 영화 안에서 시각 feature를 맞춘 구간 쌍(음악 있음 vs 없음)으로 정의한다. 음악 유무가 장면 종류와 공선적이라 그대로 비교하면 R0 기준점이 장면 효과를 실어 온다.
  4. TRIBE(v1) 입력 창(비디오 4 s, 텍스트 1,024단어, 오디오 60 s, transformer의 유한 TR 창; arXiv:2507.22229 2.3절)을 결과 해석에 명시한다. 창을 넘는 정서 성분은 설계상 예측 대상이 아니다. TRIBE v2의 창은 미확인.
* 태그: evidence-level R0 + R1, insilico-vs-observed 혼합(분리 보고).

### FA-P3 (frontier-ai): 세 가지 예측 신호와 "지속 상태 vs 재호출" → **수정**
* 판단: 한 모델에서 예측오차, 불확실성, 학습 진전을 함께 뽑아 "모델 간 차이"와 "신호 종류 차이"를 분리하자는 설계는 내 Chain 2와 Round 1 개념 4(학습 진전으로서의 미적 가치, Brielmann & Dayan 2022, 10.1037/rev0000337)를 더 엄밀하게 만든다. 지속 상태 vs 재호출 경쟁 모형은 내 이월 질문(Chain 1, MD-P1)의 가장 중요한 대안 가설을 명시해 준다. 재호출 쪽 계산 근거로 TCM-SR(10.1037/rev0000505 [초록])을 추가한다.
* 수정안:
  1. **'학습 진전'의 정의 고정:** 가중치가 고정된 V-JEPA 2에는 학습이 없다. 학습 진전을 (a) 문맥 창 안에서 예측 불확실성이 줄어드는 정도(in-context 적응) 또는 (b) 영화를 따라 test-time 적응을 시킨 판본의 예측 손실 감소 중 하나로 사전에 정의하고, 둘을 섞지 않는다.
  2. **오디오와 대사 surprise를 같은 틀에 넣는다.** V-JEPA 2 문맥이 수 초라는 제안자의 반론 (a)에 동의하며, 음악 stem과 음성 stem의 surprise(MD-P5)를 추가해 "수준 x 모달리티 x 신호 유형" 표로 만든다. BI-P5와 한 설계로 합친다.
  3. **재호출 검정의 데이터:** 재호출 회귀자(과거 장면과의 내용 유사도 가중)는 서사가 있는 Emo-FilM에서만 의미가 있다. Horikawa는 클립 순서가 무작위라 내용 유사 재호출의 기회가 거의 없으므로, Horikawa에서는 지속 상태 쪽만 검정하고, 같은 클립이 다른 선행 클립 뒤에 오는 Mind captioning 테스트 세트(10.1126/sciadv.adw1464 Methods)를 지속 상태의 식별 조건으로 쓴다.
  4. 경쟁 모형은 같은 자유도(matched complexity)와 같은 HRF 처리로 비교하고, 컷과 음량 회귀자를 공통 nuisance로 둔다.
* 태그: evidence-level R0. label-provenance: 일차 분석은 라벨 없음(뇌, 생리, 모델 신호), 평정 사용 시 별도 평정자 규범(반복 시청자).

### GI-P3 (geometry-info): washout 이완으로 HRF 잔여와 정서 관성을 가르기 → **수용**
* 판단: "같은 영역 안에서 정서 정렬 부분공간과 시각 정렬 부분공간의 감쇠를 비교하면 HRF 잔여(모든 부분공간에 같은 커널)와 정서 관성을 구분할 수 있다"는 논리는 내 MD-P1의 '블록 길이 변이' 방법보다 HRF 문제를 더 직접 해결한다. MD-P1과 하나로 합치고, 판별 지표를 이 부분공간 대조로 바꾼다. 부분 선행(Gaviria 2021, 10.1016/j.neuroimage.2021.118377; 10.1002/hbm.25277)에 비해 새로움을 "부분공간 대조 기반 시간상수와 개인 내 신뢰도"로 한정한 것도 맞다.
* 보완 세 가지(수용 범위 안):
  1. 영화 중 정서 부분공간과 시각 부분공간은 서로 공선적이다. 시각 부분공간을 직교화한 정서 부분공간을 쓰고, 직교화 전후를 모두 보고한다.
  2. Emo-FilM은 소리가 있으므로 washout(무음 고정점)에서 **청각 정렬 부분공간**의 감쇠를 세 번째 감각 대조로 추가한다.
  3. Horikawa와 Mind captioning의 2 s 간격에서는 이완 곡선 적합 대신 t-1, t-2 블록 투사의 잔존 비율 대조를 쓰자는 제안을 그대로 채택한다. Mind captioning 전처리본은 회백질 전역 신호를 회귀했으므로(geometry-info Round 2 0.2절) raw에서 같은 파이프라인으로 맞춘다.

### SN-P2 (systems-neuro): 자율신경 회복 동역학과 arousal 3원 분해 → **수용**
* 판단: '신경 이월'과 '신체 이월'을 따로 기술한다는 목표(제거가 아니라 분리)에 동의한다. 제안자가 권한 Chain 1 already_done 수정(no → partially, Borchardt 2018 10.1093/cercor/bhx290)은 이미 이 문서 0절에 반영했다.
* 보완(수용 범위 안):
  1. Horikawa의 전역 신호 대리 지표는 Horikawa 공개 전처리본의 전역 신호 처리 여부가 미확인이고, Mind captioning 전처리본은 회백질 전역 신호를 이미 회귀했다. 두 코호트 모두 raw에서 대리 지표를 다시 계산해야 비교가 된다.
  2. U6의 3원 분해에서 '감각 강도'는 음량 RMS뿐 아니라 음원 분리 후 음악, 음성, 효과음 stem 각각의 에너지로 넣는다. 갑작스러운 효과음은 자율신경 반응(놀람)과 BOLD를 함께 움직이므로 stem 분리 없이는 감각 강도와 자율 성분이 섞인다.
  3. commonality 분석은 공선 예측자에서 불안정하므로 영화 단위 bootstrap 구간을 함께 보고한다.

### GC-P4 (generative-counterfactual): R0 분할을 R1 stem counterfactual로 확장하고 surrogate를 실제 판본 조작으로 검증 → **수정 (MD-P4와 통합)**
* 판단: R0(고유 설명량)과 R1(제거 효과)을 같은 stem 분리 결과로 정서 항목별 나란히 계산하고, 두 지표가 어긋나는 경우를 공선성 또는 surrogate 대체 예측의 진단으로 쓰자는 1번은 그대로 수용한다.
* 수정안:
  1. 2번의 surrogate 검증 기준을 바꾼다. Lettieri 2024의 판본별 차이는 대부분 **행동 평정**(어떤 정서가 유발되는가)과 영역별 encoding 적합 변화다. TRIBE v2는 평정이 아니라 뇌 반응을 예측하므로, 재현 기준은 "청각판에서 청각 피질의 정서 모형 적합 증가, 시각판에서 시각 피질 적합 증가, vmPFC 범주 부호 유지"라는 **신경 패턴의 방향**으로 한정한다. 다만 Lettieri 자극과 fMRI는 우리에게 없으므로 이 재현은 같은 조작 구조를 Emo-FilM에 적용한 질적 대조에 그친다. 내 MD-P4가 제안한 다른 관문(같은 영상 + 음악 정서가 교체: Pehrs 2014 10.1093/scan/nst169; 음악 + 중립 영상: Eldar 2007 10.1093/cercor/bhm011)을 함께 두어 관문을 두 개 이상으로 만든다.
  2. 3번(음악 시작 시점 대비 평정 lag와 뇌 lag 비교로 반복 시청 앞당김 검정)은 좋은 검정이다. 다만 음악 시작은 장면 전환과 자주 겹치므로 **연속 장면 안에서 시작하는 음악 stem onset**만 쓴다. 평정자별 원자료에 항목 평정 순서가 남아 있으면 첫 시청 평정자와 반복 시청 평정자를 나눠 같은 lag를 비교한다(MD-P5).
* 태그: evidence-level R0 + R1. G1 필요(보유, 영화별 CC 조항 확인 전 R2 금지에 동의).

### LS-P3 (llm-semantics): 대사 의미의 L1(어휘) vs L2(추론된 정신 상태) 분해, belief-inconsistent surprise → **수용**
* 판단: 내 Chain 3 (b)는 "대사 언어 feature"를 한 덩어리로 다뤘다. 어휘 감성과 인물 정신 상태 추론을 따로 빼야 Lettieri 2024의 "vmPFC 추상 부호는 의미에 기댄다"는 가설(10.1126/sciadv.adk6840 Discussion constructionist 단락)이 무엇을 뜻하는지 갈린다. belief-inconsistent surprise(Antony 2021, 10.1016/j.neuron.2020.10.029 [db])를 surprise 유형 목록에 추가하는 것도 수용한다(MD-P5, FA-P3, BI-P5 공동 표에 한 행).
* 보완(수용 범위 안):
  1. ASR은 원 혼합음이 아니라 음원 분리 후 **음성 stem**에 적용하면 음악과 효과음 때문에 생기는 오류를 줄일 수 있다. 분리 오류와 ASR 오류를 함께 점검하기 위해 Spacetop narratives 텍스트판을 상한으로 쓰자는 제안에 동의한다.
  2. Emo-FilM 영화마다 대사량이 크게 다를 것이다(예: 애니메이션 단편 일부는 대사가 거의 없을 수 있음, 영화별 대사량은 미확인). 이를 교란으로만 보지 말고, **대사가 적은 영화를 언어 의존성 검정의 자연 대조**로 쓰자. 대사가 적은 영화에서도 vmPFC 정서 decoding이 같은 수준이면 "언어 채널이 필수"라는 해석은 약해진다. 영화 14편이라 이 대조는 탐색적이다.

### BI-P5 (brain-inspired): arousal은 예측 불확실성인가 예측오차인가 → **수정 (FA-P3, MD-P5와 공동 설계)**
* 판단: active inference의 "arousal = 사후 신념 entropy" 정식화(arXiv:2407.02474 [db])로 오차형 대 불확실성형을 나누는 것은 내 Chain 2의 경계 유형 구분(Nguyen 2026, 10.7554/eLife.107955; 서스펜스 Bezdek 2017, 10.1016/j.biopsycho.2017.07.020)과 같은 축이다. 세 에이전트(BI, FA, MD) 공동 설계로 합치자는 제안에 동의한다.
* 수정안:
  1. **평정 항목의 출처 차이를 설계에 반영:** Suddenly, Predictable, Urgency, Alert, AtEase는 항목마다 **서로 다른 평정자 조합 3~4명**이 평정했다(평정자 1명이 항목 6개를 무작위 배정받음, Ma & Kragel Methods 'Emotion ratings', Stage 1). 평정자마다 반응 지연과 시청 횟수가 다르므로, 항목 사이의 차이(예: Suddenly는 오차와, Urgency는 불확실성과 결합)가 평정자 집단의 지연 차이로 생길 수 있다. 항목별 지연을 먼저 추정해 맞추고, 지연 이동에 대한 결과의 민감도를 보고한다.
  2. 1차 결과 변수는 처음 보는 fMRI 참가자의 EDA와 편도체, 섬엽 반응으로 두고, 평정 항목은 2차로 둔다.
  3. 불확실성 정의를 두 개 이상(앙상블 분산, 예측 분포 entropy) 쓰자는 제안자의 대응에 동의하고, 오디오 수준에서도 같은 두 정의로 계산한다.
* 태그: evidence-level R0. label-provenance: 별도 평정자 규범(반복 시청자) + 참가자 측정 생리 + 모델 계산 변수.

### (참조) GI-P2 (geometry-info → brain-inspired): 전이 행렬의 반대칭 흐름과 비가역성
* 짧은 의견: 내 Chain 7(동역학 비교)과 같은 방향이라 지지한다. 두 가지를 덧붙인다. (1) 평정 consensus의 순 흐름(A)은 **항목별 평정자 지연 차이**만으로도 생길 수 있다(예: 공포 평정자가 안도 평정자보다 빨리 반응하면 공포에서 안도로의 가짜 흐름). 항목별 지연 정렬 후 A가 남는지 먼저 확인해야 한다. (2) 방향성 비교에는 단순 전치 T'가 아니라 정상분포로 보정한 시간 역전 사슬을 써야 한다(자세한 논리는 `round3_reviews.md`의 BI-P1 검토).

---

## 4. Coordinator 질문 8개에 대한 답 (Axis D, M, Neuroaesthetics 관점)

**Q1. Vision Decoding 연구자가 Emotion Neuroscientist의 문제를 해결할 수 있는가?**
부분적으로. 정서 정보가 "이미지로 계산 가능한 상한"(vision-decoding L1)을 넘는지 판정하는 도구와 같은 비디오의 두 번째 무음 코호트(Mind captioning, 10.1126/sciadv.adw1464)는 내 질문에 직접 쓸모 있다. 그러나 시간 축에서는 한계가 분명하다. 비디오 재구성은 장면 전환 구간에서 실패하고(arXiv:2410.19452 [db]), 정서 전이는 장면 전환과 자주 겹친다. EmoMind는 클립당 정서 벡터 하나라 시간 동역학이 사라진다(arXiv:2605.16739 [db]). 입력이 시각 영역 voxel에 제한된 재구성 모델(arXiv:2403.11207 [db])은 소리와 정서 영역 정보를 원천적으로 쓰지 않는다. 그래서 시각 해독은 정서 연구의 **내용 통제와 상한 추정**을 해결하고, 동역학과 다감각, 경험 질문은 해결하지 못한다.

**Q2. LLM의 representation이나 reasoning 능력을 neural emotion representation 분석에 활용할 수 있는가?**
가능하지만 시간 타당성 검증이 먼저다. video-audio MLLM은 문맥 길이를 늘릴수록 고차 피질 정렬이 오르므로(arXiv:2602.07570) 장시간 정서 통합의 회귀자로 유망하다. 반면 비디오 단위 일치가 연속 일치를 보장하지 않고(arXiv:2502.04379), LLM 정서 표상은 국소적이며 지속 상태를 유지하지 않는다고 보고되었다(arXiv:2604.07729). 따라서 MLLM 연속 주석은 Emo-FilM 평정자별 원자료로 alt-test(arXiv:2501.10970)를 통과한 항목과 문맥 길이에서만 쓰고, 출력은 L2(귀속, 평균 관찰자) 수준의 AI 추정 정서로 표기한다(MD-P6). LLM의 국소성 자체는 뇌의 지속성과 비교할 **대조군**으로 쓸 수 있다(I-3).

**Q3. Generative AI로 emotion과 visual semantics를 분리해 검증할 수 있는가?**
시각 편집보다 **음향 편집**에서 더 깨끗하게 가능하다. 이미지 정서 편집은 내용을 함께 바꾸지만(generative-counterfactual U1, arXiv:2405.12661 [db]), 같은 영상에 음악만 바꾸면 시각 의미는 정확히 고정된다. 이 설계는 실제 fMRI로 이미 쓰인 적이 있다(Pehrs 2014, 10.1093/scan/nst169; Shany 2021, 10.1002/hbm.25640). 우리 데이터로는 stem 분리(arXiv:2110.09958) 후 in-silico 교체(R1)까지이며, 실제 뇌 효과는 선행 실험 결과의 in-silico 재현을 관문으로 둔다(MD-P4). 인간 평정을 새로 받으면 R2.

**Q4. Emotion Dynamics를 dynamical systems나 state-space learning의 문제로 재정의할 수 있는가?**
그렇다. 내 Round 1 U1, U2가 바로 이 재정의다. 도구: hybrid 연속-이산 모형 rSLDS(proceedings.mlr.press v54/linderman17a), 동역학 수준 비교 DSA(arXiv:2306.10168), 정서 확산 모형 DynAffect(10.1037/a0020962), line attractor 시간상수(10.1016/j.cell.2022.11.027). 데이터: Emo-FilM 1 Hz 평정과 fMRI, Horikawa와 Mind captioning의 클립 이월, Emo-FilM washout(MD-P1). 핵심 주의는 세 가지다. (1) 자극 구동 입력과 내생 동역학을 분리해야 한다(입력을 넣은 state-space 모형). (2) TR, HRF, high-pass 필터가 시간상수를 왜곡한다. (3) 평정 궤적의 동역학에는 커서 관성과 평정자 반복 시청이 섞인다.

**Q5. Brain Foundation Model의 latent representation에서 감정 관련 구조를 찾을 수 있는가?**
시간 척도 관점에서 새 검정을 하나 제안한다. TRIBE(v1)는 비디오 직전 4 s, 텍스트 직전 1,024단어, 오디오 60 s 구간을 입력으로 쓰고 transformer가 유한한 TR 창 안에서만 시점을 섞는다(arXiv:2507.22229 2.3절). 따라서 창을 넘는 지속과 자극으로 계산되지 않는 내생 누적은 이 모델의 예측에 **설계상 들어가지 않는다**. 관찰 반응과 in-silico 예측의 차이를 시간 척도별로 분해하면, 정서 관련 영역에서 "자극으로 계산 불가능한 느린 성분"이 얼마인지 잴 수 있다(MD-P3). 무음 Horikawa에서는 입력이 비디오 4 s 창뿐이라 이 대비가 가장 선명하다. 뇌 입력 foundation model latent의 정서 구조는 encoding-foundation U5가 지적한 대로 누수 통제 benchmark가 먼저이며, 내 쪽에서 더할 것은 latent의 시간 상수(이월 지속)를 정서 benchmark 항목으로 넣자는 것이다.

**Q6. Music, Video, Image의 공통 정서 특징과 modality-specific 특징을 뇌 수준에서 구분할 수 있는가?**
부분적으로, 그리고 데이터셋 교락에 주의해야 한다. 같은 영화를 모달리티별 판본으로 보여 준 연구는 vmPFC의 모달리티 독립 범주 부호와 초기 감각 피질의 모달리티 특이 부호를 함께 보였다(10.1126/sciadv.adk6840). 우리 5개 데이터셋에는 **순수 음악 자극이 없다**(Spacetop narratives는 음성 이야기). 그래서 음악은 Emo-FilM, Spacetop 영상의 stem 분리로만 분리할 수 있다(관찰, R0). 비디오(무음)는 Horikawa와 Mind captioning, 이미지는 NSD, 시청각 영상은 Emo-FilM과 Spacetop이다. 데이터셋 사이 비교는 참가자, 스캐너, 라벨이 함께 바뀌므로 공통 모델 공간(ImageBind, CLAP)과 RSA 수준(Stage 1 수준 2~3)으로만 한다. 가장 깨끗한 비교는 **데이터셋 안**에 있다: Emo-FilM의 음악 있음과 없음 구간, Spacetop 같은 참가자의 alignvideo(시청각) 대 narratives(오디오 vs 텍스트).

**Q7. Neuroscience에서 관찰되는 정서 관련 계산을 AI architecture의 구조적 제약으로 구현할 수 있는가?**
시간 쪽에서 두 가지 후보가 있다. (1) **지속 정서 상태 모듈**: LLM 정서 표상이 국소적이라는 보고(arXiv:2604.07729)에 대해, 뇌에서 이월과 이완 시간상수가 확인되면(MD-P1) 그것을 느린 누적 상태(leaky integrator 또는 line attractor)로 넣는 구조적 prior가 된다. (2) **정서 경계 기반 메모리 분절**: EM-LLM은 surprise 경계로 문맥을 나눈다(arXiv:2407.09450). 정서 change point가 기억 경계를 만든다는 결과(10.1038/s41467-023-42241-2)를 따라 '정서 surprise'를 경계 신호로 쓰는 변형을 만들 수 있다. 어느 쪽도 공학적 제안이며, 그 모델이 잘 작동해도 뇌가 같은 계산을 한다는 증거는 아니다(식별 가능성 문제, adversarial-reviewer U4).

**Q8. 정서 라벨이 없는 NSD 같은 데이터도 다른 데이터셋과의 representation alignment로 의미 있게 활용할 수 있는가?**
내 Axis에서는 **제한적이지만 기준선으로 유용**하다. NSD는 정지 이미지 3 s, 대체로 중립이라 정서 동역학과 소리 질문에는 쓸 수 없다. 대신 "정지, 시각 전용, 반복으로 noise ceiling이 있는" 쪽 끝을 제공한다. 예: NSD로 학습한 정지 이미지 encoder를 Horikawa 클립 프레임에 적용해 예측한 반응과 실측의 차이를 보면, Horikawa 정서 신호 가운데 **정지 시각 내용으로 설명되는 몫과 시간(움직임, 맥락)이 더하는 몫**을 나눌 수 있다(in-silico, R1). NSD 정서 라벨이 필요하면 AI 추정 라벨이므로 label-provenance를 AI로 표시한다.

---

## 5. Axis 결정에 대한 의견

1. **Aesthetic & Value Experience를 A, D, N 교차 Sub-axis로 둔 결정에 동의한다.** 다만 Round 1 이후 근거가 늘었다: brain-inspired P-8(항상성 setpoint가 없는 미적, 사회 정서의 계산적 지위)과 Horikawa 34범주의 미적 범주(aesthetic appreciation, awe, entrancement)가 독립적으로 같은 방향을 가리킨다. Stage 3 조합에서 이 Sub-axis가 3회 이상 쓰이면 독립 Axis 재검토를 요청한다.
2. **Axis U(Label Provenance & Perspective)와 label-provenance 태그에 '시간 출처' 속성 두 개를 추가하자고 제안한다.**
   * **시청 이력(exposure count):** Emo-FilM 평정자는 같은 영화를 최대 6번 봤고(Stage 1, Ma & Kragel Methods), Mind captioning S1은 예비 실험으로 같은 자극에 여러 번 노출되었다(vision-decoding 0.1절). 반복 시청은 사건 표상을 앞당긴다(10.7554/eLife.64972). 같은 '규범 평정'이라도 첫 시청과 반복 시청은 다른 측정이다.
   * **평정 시점(rating mode):** 온라인 연속(Emo-FilM 1 Hz), 자극 직후 1회(Horikawa, Spacetop), 지연 회고(Emo-FilM 참가자 클립 재시청 평정). 연속과 회고 평가는 일치도 구조가 다르다(10.3389/fnhum.2021.676032).
3. **Axis W(Internally Generated Experience)와의 연결:** Mind captioning 회상 블록은 지각 블록과 길이를 맞췄다 [본문 Methods]. 같은 클립의 지각과 회상에서 정서 정보의 시간 구조(회상에서 압축되는가, peak만 남는가)를 비교하면 W와 D(Online-to-Retrospective Integration)를 잇는 질문이 된다. 회상 정서 decoding은 vision-decoding R2의 영역이므로 Round 3에서 공동 제안으로 다룰 것을 제안한다.
4. **Axis V(Action Readiness)와의 연결:** Emo-FilM에는 Motivation 10항목의 1 Hz 평정이 있다. CPM은 성분 사이 시간 순서를 함의하지만 이론이 구체 예측을 거의 내지 않는다(10.1093/scan/nsad063 'Get out' 절). Motivation 항목과 Feeling 항목 사이의 선후(lead-lag)를 평정 지연을 보정해 추정하면 V에 시간 축 질문을 하나 더한다. 단 항목마다 평정자가 달라 평정 지연이 항목에 따라 다를 수 있다는 점이 가장 큰 위험이다.

---

## 6. 이번 라운드의 한계

* arXiv API 검색이 rate limit(429)로 실패해 선행 검색은 PubMed와 WebSearch 범위다. 특히 MD-P1(이월), MD-P6(시간 의존도), Chain 6(미적 하이라이트)의 "no"와 "partially"는 Round 3에서 arXiv 검색으로 다시 확인해야 한다.
* 다른 에이전트 round1.md의 6절은 내 Axis와 겹치는 chain만 읽었다. 나머지 chain과 2, 5, 7절은 제목과 요약 수준으로만 확인했다.
* [db] 표시 논문은 literature_db.csv의 verified 기록과 해당 에이전트의 본문 확인에 의존했다. 내가 본문을 다시 읽은 것은 Mind captioning(Methods, Discussion 일부)과 Lettieri 2022(Discussion)뿐이다.
* Mind captioning 저장소(ds005191)의 실제 events 파일, Horikawa 2020과의 학습 순서 동일 여부, 평가 블록 위치는 미확인이다. MD-P1의 설계는 이 정보가 확인되면 구체화한다.
* Emo-FilM 평정자별 원자료에 항목 평정 순서(첫 시청 여부)가 기록되어 있는지 미확인이다(MD-P5 (i)의 전제).
