# systems-neuro Round 2: Cross-Agent Exchange

* 작성: systems-neuro (Axis E Neural Targets, 외부 분야 Computational Psychiatry). 제안 ID 접두어 SN
* 기준일: 2026-11-12
* 따른 절차: `reference/protocols.md` P2 + Coordinator 추가 요구(제안 ID, 필수 태그, Coordinator 질문 8개)
* 읽은 것: 다른 10개 에이전트의 `round1.md`(0, 1, 3, 4, 6절 중심, 관련 chain은 전문), `outputs/axis_encyclopedia.md` 0절과 2~3절, `outputs/STAGE_STATUS.md` 사용자 결정 기록, `outputs/literature/literature_db.csv`(식별자 존재 확인용)
* 새로 확인한 논문 5편을 `literature.jsonl`에 추가했다(`added_round: "Round 2"`): doi:10.1093/cercor/bhx290, doi:10.1093/pnasnexus/pgac020, doi:10.1093/scan/nsz037, doi:10.1523/JNEUROSCI.1436-24.2025, doi:10.1126/sciadv.adw1464. 모두 Crossref로 존재 확인. 본문은 Nastase 2019(생리 관련 문장), Mind captioning(Methods 획득 사양)만 PubMed MCP로 일부 열람했고 나머지는 초록 수준이다.
* 표기: 필수 태그는 `axis_encyclopedia.md` 0.2절 정의를 따른다. evidence-level R0 상관, R1 모델 내 개입, R2 새 행동 평정, R3 새 fMRI 자극 조작, R4 뇌 개입.

---

## 0. 요약

1. 다른 에이전트의 chain 가운데 **7개가 피질하 신호 품질, 생리 신호, 전역 자율신경 성분 문제를 직접 안고 있다**(encoding-foundation Chain 2, multimodal-dynamics Chain 1과 U6, brain-inspired Chain 3, geometry-info C5와 C6, llm-semantics Chain 4, vision-decoding R2). 이들에 같은 진단(전역 성분 분리, 생리 반영 noise ceiling, signal-feasibility 게이트)을 붙이는 제안 7개(SN-P1~P7)를 보낸다.
2. **Mind captioning을 signal-feasibility 판정에 추가했다**(0.5절). 원문 Methods 기준 3T Prisma, TR 1 s, TE 30 ms, 2 mm, **multiband 6**이다. 72개 클립 5회 반복은 amygdala noise ceiling과 반복 효과 추정을 처음 가능하게 하지만, MB6은 뇌 중심부 잡음을 키울 수 있고 본문에서 생리 기록 언급을 찾지 못했다.
3. 가져온 아이디어 6개: washout 이완 시간상수(geometry-info), 생리로 부푼 ISC 상한(adversarial-reviewer), 반복 클립(vision-decoding), arousal의 감각 강도 가설(multimodal-dynamics), 신체 잔차(llm-semantics), 경로의 '속도 아닌 내용' 재정의(brain-inspired).
4. **새로움 주장은 검색으로 확인했다**(6절에 검색 경로). 그 결과 내 Round 1 판단 두 가지를 낮췄다: 영화 후 FC 이월과 HRV 감소는 Borchardt 2018이 이미 보였고(SN-P2 already_done partially), 영상 시청 중 심박 ISC는 Madsen & Parra 2022가 보였다(SN-P1의 전제는 선행, ceiling 분해는 미발견).
5. Axis 판정: "Acquisition & Signal Physics"의 태그화는 **조건부로 수용**한다. 조건은 태그 값을 구조화된 기록으로 두고, '측정 지형이 정서 위치 주장을 만드는가'라는 연구 질문은 E의 Sub-axis로 남겨 무작위 조합에 들어가게 하는 것이다(5절). Computational Psychiatry Phenotyping의 O Sub-axis화는 수용한다.

---

## 0.5 signal-feasibility 판정 갱신 (5개 데이터셋)

Round 1 0.5절 판정에 Mind captioning을 더한다. 직접 tSNR을 계산하지는 않았다.

| 데이터셋 | 획득 조건 | 반복 | 생리 | 피질하(amygdala) 판정 | 근거 |
|---|---|---|---|---|---|
| Horikawa 2020 | 3T Verio, TR 2 s, TE 43 ms, 2 mm, MB4 | 없음 | 없음 | ROI 수준 조건부, 소핵(SC, pulvinar) 부적합에 가까움 | Round 1 0.5절 |
| **Mind captioning** | **3T Prisma, TR 1 s, TE 30 ms, 2 mm, 72 slices, MB6, 전뇌** (doi:10.1126/sciadv.adw1464 Methods) | **테스트 72클립 x 5회**(지각), 회상 72클립 x 5회 | 본문에서 언급 찾지 못함 | ROI 수준 조건부. TE는 Horikawa 2020보다 유리, MB6은 중심부 시간 잡음 위험(doi:10.1016/j.neuroimage.2021.118617). 반복으로 amygdala 신뢰도를 처음 직접 계산할 수 있으나 반복 자체가 amygdala 반응을 바꾼다(doi:10.1038/s41467-024-49073-8 Discussion 6째 단락) | 원문 Methods(PubMed MCP 전문) |
| Emo-FilM | 3T, TR 1.3 s, TE 30 ms, 2.5 mm, MB3 | 없음 | PPG, 호흡, EDA 공개 | raw 재전처리 시 ROI 수준 가능 | Round 1 0.5절 |
| Spacetop | 3T Prisma, TR 0.46 s, TE 27.2 ms, 2.7 mm, MB8 | 없음 | 공개본 없음 | 영역 평균 취약, 패턴 경로 분석은 선례 있음 | Round 1 0.5절, doi:10.1016/j.neuron.2021.06.001 |
| NSD | 7T, TR 1.6 s, 1.8 mm | 이미지당 3회 | 일부 세션 | 해상도 최상, 반복과 기억 과제 confound | Round 1 0.5절 |

같은 Cowen & Keltner 비디오를 본 두 코호트(Horikawa 2020: TE 43 ms, MB4 / Mind captioning: TE 30 ms, MB6)는 **획득 조건만 다르고 자극이 같다.** 따라서 "피질하나 안와전두의 정서 정보가 데이터셋 간에 다르게 나오는가"를 획득 물리의 영향으로 검정할 수 있는 드문 쌍이다(5절의 근거로도 쓴다). 두 코호트의 피험자 중복 여부는 미확인이다(vision-decoding 0.1절).

---

## 1. 가져온 아이디어

### G1. 영화 후 washout의 이완 시간상수 (출처: geometry-info C5)
* 원 아이디어: 정서 잠재 차원이 영화가 끝난 뒤 감각 차원보다 느리게 이완하는지, 시간상수가 개인 형질인지를 Emo-FilM 영화 전후 90초 구간으로 측정. 근거: 시상하부 근사 line attractor의 시간상수 개인차(doi:10.1016/j.cell.2022.11.027), affective line attractor의 인과 증거(doi:10.1038/s41586-024-07915-x).
* 내 쪽에서 쓰는 방식: Round 1 chain 5(자극 유발 landscape의 '신경 관성')는 영화 중 상태 전이를 다뤘다. washout은 자극이 사라진 구간이라 **자극 구동 성분이 없는 상태에서 관성을 잴 수 있다**는 점에서 더 깨끗하다. 내가 덧붙일 것은 같은 구간의 심박, PPG 진폭, EDA 회복을 함께 적합해 '신경 이완'과 '자율신경 회복'의 시간상수를 분리하는 것이다(SN-P2와 연결).

### G2. 생리 동기화로 부푼 ISC 상한 (출처: adversarial-reviewer U3)
* 원 아이디어: 반복 없는 정서 fMRI에서 ISC 기반 상한을 쓰는데, 정서 자극이 호흡을 동기화하면 상한 자체가 생리 잡음으로 부풀 수 있다(doi:10.1093/scan/nsz037, Limitations 둘째 항목 '자극 관련 호흡과 움직임 artefact가 ISC에 기여할 수 있다'를 이 에이전트가 PubMed 전문으로 재확인).
* 내가 찾은 보강 근거: 정보성 영상 시청 중 **심박에서도 자극 구동 ISC**가 나타나고 EEG, 동공 ISC와 함께 변한다(doi:10.1093/pnasnexus/pgac020, 초록). 반대로 이 연구에서 호흡 ISC는 나타나지 않았다. 즉 오염 경로는 호흡보다 심박-혈관 쪽일 가능성이 있고, 이는 Bolt 2025의 PPG 진폭-전역 신호 결합(doi:10.1038/s41593-025-01945-y)과 맞물린다. SN-P1의 핵심 근거로 쓴다.

### G3. 같은 정서 클립의 반복 제시 (출처: vision-decoding 0.1절, R2)
* 원 아이디어: Mind captioning의 72개 클립 5회 반복으로 noise ceiling을 추정하고 회상 재활성을 검정.
* 내 쪽에서 쓰는 방식: Round 1 chain 4는 NSD 반복으로 'amygdala 정보는 반응 크기보다 반복에 따른 변화에 실려 있는가'를 물었지만, NSD는 정서 라벨이 AI 추정뿐이었다. Mind captioning은 **규범 정서 평정이 있는 정서 비디오의 반복**이므로 이 질문의 1순위 데이터가 된다(SN-P5).

### G4. 일반화되는 arousal은 감각 강도일 수 있다 (출처: multimodal-dynamics U6)
* 원 아이디어: Ke 2025의 일반화 arousal 표지(doi:10.1371/journal.pcbi.1012994)가 음량, 움직임 같은 시청각 강도의 재표현일 가능성이 통제되지 않았다(공포 장면이 어둡고 시끄럽다는 Morgenroth 2023, doi:10.1093/scan/nsad063 'White noise' 절).
* 내 쪽에서 쓰는 방식: Round 1 chain 1은 '신경 vs 자율신경' 2원 분해였다. 여기에 **감각 강도**를 셋째 축으로 넣어 3원 분해(감각 강도 / 참가자 자율신경 / 규범 정서)로 바꾼다. 세 성분은 서로 인과적으로 얽혀 있으므로(큰 소리 → 교감 반응) commonality 분석으로 공유 분산까지 보고한다.

### G5. 신체 잔차 (출처: llm-semantics Chain 4)
* 원 아이디어: MLLM이 놓치는 정서 성분(인간 규범 평정 - MLLM 추정)이 참가자 생리와 insula를 예측하는가. 근거: MLLM의 신체 기반 정서 실패(doi:10.1038/s41598-025-14961-6), Gemini 영화 feature의 insula 설명력 부족(doi:10.1162/imag.a.1300).
* 내 쪽에서 쓰는 방식: Round 1 chain 1의 '규범 arousal 중 생리로 설명되지 않는 신경 성분'과 정반대 방향의 잔차다. 둘을 합치면 **언어로 회복되는 성분, 몸으로 회복되는 성분, 둘 다 아닌 신경 성분**의 3분할이 된다. SN-P6에서 이 결합을 제안한다.

### G6. 피질하 경로는 '속도'가 아니라 '내용'으로만 검정된다 (출처: brain-inspired P-3, Chain 3)
* 원 아이디어: fMRI는 latency를 측정하지 못하므로 low road 가설은 경로가 싣는 표상 내용(얕은 층 vs 깊은 층 feature)으로만 검정 가능하다. DNN에서 초기 층 shortcut이 정서 조건화에 필요했다(arXiv:2607.19327, brain-inspired 인용).
* 내 쪽에서 쓰는 방식: Round 1 chain 3(Spacetop의 looming 추적과 통증 대조)의 결과 해석 틀을 이 기준으로 바꾼다. "경로가 looming을 추적한다"는 결과는 '빠르다'가 아니라 '저수준 운동 feature를 싣는다'로만 해석한다.

---

## 2. 보내는 제안

### SN-P1 → encoding-foundation (Chain 2 'Limbic 맹점의 분해')
* **제안 내용:** 너희 쪽 Limbic 맹점 분해(잡음인가, 몸인가, 평가인가)를 우리 쪽 **생리 반영 noise ceiling과 전역 자율신경 성분 분해**로 검증, 확장할 수 있다.
  1. ceiling 분해: Emo-FilM의 ISC 상한을 raw BOLD, 생리 회귀 BOLD 두 판으로 계산해 차이를 '자극 구동 생리 성분'으로 보고한다. 심박은 자극에 동기화된다(doi:10.1093/pnasnexus/pgac020). 이를 빼지 않으면 "ceiling 대비 낮은 성능"이 과소 또는 과대 추정된다.
  2. 생리의 세 역할을 구분: (a) 잡음 회귀(심장, 호흡 위상), (b) 전신 상태 예측자(심박, 호흡량, PPG 진폭을 지연 반응함수와 함께, Bolt 2025의 순서 구조), (c) 둘을 뺀 뒤 남는 '신경' 분산. 너희 Chain 2의 설명 변수 (b) '참가자 생리'를 이 셋으로 쪼개야 '몸'과 '잡음'이 구분된다.
  3. 제공 전처리본(WM/CSF 회귀)은 쓰지 않는다. 전역 성분은 WM, CSF에서 회백질과 반대 부호로 움직이므로(doi:10.1038/s41593-025-01945-y, Discussion 5~6째 단락) 이 회귀가 영역마다 다르게 자율신경 성분을 지우거나 주입할 수 있다.
  4. 영역별 dropout 마스크와 tSFNR을 결과 옆에 둔다(TRIBE v2 피질하 저점수의 일부는 SNR일 수 있다).
* **관련 Axis:** E, H, F, Q, A(Interoception)
* **근거 논문 ID:** arXiv:2605.04326, doi:10.1038/s41593-025-01945-y, doi:10.1093/scan/nsz037, doi:10.1093/pnasnexus/pgac020, doi:10.1038/s41597-026-07065-x, doi:10.1016/j.neuroimage.2021.118617
* **가능한 데이터셋:** Emo-FilM(주, raw + 생리), Mind captioning(72클립 5회 반복으로 생리 없이 개인 내 반복 기반 상한 비교), Spacetop(생리 입수 시)
* **예상되는 반론:** (1) "생리 회귀가 정서 관련 신경 신호까지 지운다(과잉 보정)." 대응: 제거 전후를 모두 보고하고, Bolt 2025의 혈관성 시공간 표지(WM/CSF 반대 부호, 지연 구조)로 전신 혈관 성분만 따로 표지한다. (2) "ISC는 이미 개인 잡음을 거른다." 대응: 문제는 개인 잡음이 아니라 자극에 동기화된 공유 생리 성분이며, Nastase 2019 Limitations가 바로 이 점을 적었다.
* **label-provenance:** 50항목 = felt(평정자 자기 경험 보고) / 별도 평정자 규범. 생리 = 참가자 본인 측정(라벨 아님). **evidence-level:** R0(관찰). TRIBE v2 예측 비교는 insilico-vs-observed 혼합. **signal-feasibility:** 필수 점검(Emo-FilM raw 재전처리, 개인별 amygdala dropout, MB3 TE 30 ms; Mind captioning MB6).
* **새로움 검색:** WebSearch "inter-subject correlation physiological synchrony heart rate respiration emotional film fMRI ISC inflated noise ceiling correction"(2026-11-12) → 심박 ISC 존재(Madsen & Parra 2022)는 확인, 정서 영화 fMRI ceiling의 생리 성분 분해는 미발견. 판정: partially(전제는 선행, 분해는 no).

### SN-P2 → multimodal-dynamics (Chain 1 '정서 이월', U6 'arousal의 정체')
* **제안 내용:** 너희 쪽 Horikawa 정서 이월(Chain 1)과 일반화 arousal의 정체(U6)를 우리 쪽 **자율신경 회복 동역학과 3원 분해**로 검증할 수 있다.
  1. Emo-FilM에서 고각성 구간 뒤 심박, PPG 진폭, EDA의 회복 시간상수를 적합하고, BOLD 지속을 이것과 HRF로 설명한 뒤 남는 부분만 '신경 이월'로 부른다. 남는 부분과 '신체 이월'을 따로 보고한다(둘 다 결과).
  2. Horikawa에는 생리가 없으므로 전역 신호와 WM/CSF 반대 부호 표지를 **자율신경 대리 지표**로 넣는 민감도 분석을 한다. 대리 지표의 타당도는 생리와 BOLD가 모두 있는 Emo-FilM에서 먼저 수치로 보정한다.
  3. U6: Ke 2025 공개 CPM의 arousal 판독을 감각 강도(음량 RMS, 휘도, 운동 에너지) / 참가자 자율신경 / 규범 정서 arousal 항목으로 commonality 분해한다.
  4. 같은 진단은 geometry-info C5(washout)와 frontier-ai CH3(ROI 시간상수 τ)에도 적용된다. 자율신경 회복과 전역 성분은 모든 ROI에 느린 성분을 만들기 때문이다.
* **관련 Axis:** D, E, A, Q
* **근거 논문 ID:** doi:10.1093/cercor/bhx290, doi:10.1038/nn.4468, doi:10.1038/s41593-025-01945-y, doi:10.1371/journal.pcbi.1012994, doi:10.1093/scan/nsad063
* **가능한 데이터셋:** Emo-FilM(보정과 주 분석), Horikawa(대리 지표 민감도), Spacetop(TR 0.46 s로 HRF 추정 정밀화)
* **예상되는 반론:** (1) "전역 신호는 생리가 아니다." 대응: 그래서 Emo-FilM에서 대리 지표의 설명력을 먼저 보고하고 Horikawa 결과는 민감도 분석으로만 둔다. (2) "자율신경 회복도 정서의 일부다." 대응: 동의한다. 목표는 제거가 아니라 '신경 이월'과 '신체 이월'의 시간 척도를 따로 기술하는 것이다.
* **label-provenance:** Horikawa, Emo-FilM 모두 felt / 별도 평정자 규범. 생리는 참가자 측정. **evidence-level:** R0. **signal-feasibility:** Emo-FilM 제공본은 high-pass(sigma 50 s)로 느린 회복을 왜곡하므로 raw 필요(geometry-info C5도 지적). Horikawa 공개본은 블록 평균이라 raw 연속 시계열 필요.
* **새로움 검색:** WebSearch "emotional carry-over fMRI after emotional film heart rate skin conductance recovery autonomic lingering brain state" → **Borchardt 2018(doi:10.1093/cercor/bhx290)이 슬픈 영화 후 CEN 노드 FC의 정서가 특이적 이월과 HRV 감소를 보고**(초록). 신경 이월과 자율신경 회복을 분리했는지는 초록에서 확인 불가. 판정: partially. multimodal-dynamics Chain 1의 already_done "no"는 Borchardt 2018 때문에 "partially"로 고칠 것을 권한다(영화 '후' FC 이월이며 Horikawa식 연속 짧은 블록은 아님).

### SN-P3 → brain-inspired (Chain 3 'Horikawa 피질하 경로의 정서 정보 내용')
* **제안 내용:** 너희 쪽 Horikawa 경로 내용 분석을 우리 쪽 **signal-feasibility 게이트와 데이터 내장 대조**로 먼저 검증하고, Spacetop과 Mind captioning으로 확장할 수 있다.
  1. 게이트 1 (내장 양성/음성 대조): Kragel 2021의 대조 분석(LGN-V1 vs MGN-A1과 교차 연결)을 Horikawa에 그대로 돌린다. **Horikawa는 무음**이므로 LGN-V1은 교차 연결보다 강하고 MGN-A1은 교차 수준이어야 한다. 이 특이성이 안 나오면 2 mm, TE 43 ms에서 시상 수준 경로 추정을 해석할 수 없다.
  2. 게이트 2: 피험자별 native 공간 SC voxel 수, tSNR, pulvinar 부분 용적 보고.
  3. 게이트 통과 시 Horikawa 2,181 블록으로 경로 내용 분석. 이어서 Spacetop(Kragel Expt2와 같은 획득 조건, 같은 참가자의 열 통증이 음성 대조)과 Mind captioning(같은 자극, 다른 코호트, 반복 있음)으로 재현.
  4. 해석은 G6 기준(내용만, 속도 아님)을 따른다.
* **관련 Axis:** E, B, N, P
* **근거 논문 ID:** doi:10.1016/j.neuron.2021.06.001, doi:10.1523/JNEUROSCI.1436-24.2025, arXiv:2607.19327, doi:10.1016/j.neuroimage.2021.118617, doi:10.1038/s41597-026-07065-x
* **가능한 데이터셋:** Horikawa, Spacetop, Mind captioning
* **예상되는 반론:** (1) "Kragel의 대조는 7T 시계열에서 한 것이다." 대응: Expt2(3T, MB8, single-trial beta)에서도 표적 경로가 교차 경로보다 강했다(정확도 76%, AUROC .78, Kragel 2021 Results). Horikawa 블록 반응은 trial 단위라 같은 형식이다. (2) "무음이어도 스캐너 소음이 MGN을 구동한다." 대응: 소음은 블록 간 일정해 블록 간 공분산에 기여가 작다. 그래도 MGN-A1이 교차보다 강하면 그것 자체가 '블록 간 공분산이 정서와 무관한 공통 구동으로 채워진다'는 경고 신호다.
* **label-provenance:** Horikawa, Mind captioning = felt / 별도 평정자 규범(MTurk). Spacetop = felt / 참가자 본인. **evidence-level:** R0. **signal-feasibility:** 제안의 핵심(게이트 1, 2).
* **새로움 검색:** Round 1 WebSearch "superior colliculus pulvinar amygdala pathway naturalistic movie fMRI MPathI replication" → 자연 영상 경로 재현 미발견(Thieu 2025 CCN 초록은 SC looming 부호화, search_index). 무음 자극에서 MGN-A1을 음성 대조로 쓴 설계는 검색하지 않았다(설계 제안이므로 선행 판정 대상 아님).

### SN-P4 → geometry-info (C6 '고차 위상의 정서 정보: 시너지인가 차원 폭인가')
* **제안 내용:** 너희 쪽 C6의 두 가설에 **셋째 가설 '전역 성분 불변성'**을 추가해 검증할 수 있다.
  * 논리: 전역 자율신경 성분(저주파 분산의 약 25%, doi:10.1038/s41593-025-01945-y Discussion 13째 단락)은 모든 영역 쌍의 상관을 함께 움직인다. homological scaffold는 가중 rank filtration으로 만들어지므로 edge 가중치의 공통 이동에 상대적으로 덜 민감할 수 있다. Zaffina 2026이 'pairwise FC가 지배적 arousal 신호를 포착'한다고 보고했으므로(초록), pairwise FC는 전역 각성 모드에 지배되고 scaffold는 그것을 덜 받아 세밀한 profile 정보를 더 보존했을 가능성이 있다.
  * 검정: (a) 생리 회귀(주), GSR(보조) 전후로 pairwise와 scaffold의 50항목 profile 예측을 비교한다. 제거 후 pairwise가 scaffold를 따라잡으면 '불변성' 해석. (b) 너희의 차원 맞춘 무작위 투영 대조, PID 시너지 분석과 같은 표에 둔다.
* **관련 Axis:** K, E, D
* **근거 논문 ID:** doi:10.64898/2026.09.26.754452, doi:10.1038/s41593-025-01945-y, doi:10.1371/journal.pcbi.1012994, doi:10.64898/2026.06.08.730730
* **가능한 데이터셋:** Emo-FilM(생리 있음, 유일)
* **예상되는 반론:** (1) "GSR은 음의 상관을 만들어 위상을 왜곡한다." 대응: 주 분석은 GSR이 아니라 측정 생리 회귀로 하고, GSR은 보조 비교로만 쓴다. (2) "rank filtration도 전역 이동에 완전히 불변하지는 않다." 대응: 그래서 가설이며, 전역 성분 크기를 인위로 바꾼 시뮬레이션으로 두 표현의 민감도를 먼저 잰다.
* **label-provenance:** felt / 별도 평정자 규범(1 Hz consensus). **evidence-level:** R0, 시뮬레이션 부분은 R1. **signal-feasibility:** Emo-FilM raw 재전처리 필요(제공본의 WM/CSF 회귀가 이미 전역 성분 일부를 바꿈).
* **새로움 검색:** WebSearch "higher-order interactions homological scaffold fMRI global signal regression effect pairwise functional connectivity comparison" → scaffold와 GSR의 관계를 검정한 연구 미발견. 판정: no(검색 범위 내).

### SN-P5 → vision-decoding (R2 '회상 정서 재활성', 0.1절 Mind captioning)
* **제안 내용:** 너희 쪽 Mind captioning 지각 반복과 회상 분석을 우리 쪽 **amygdala 반복 비정상성 가설**로 확장할 수 있다.
  1. 지각 테스트(72클립 x 5회)에서 amygdala 반응을 '반복 번호 x 규범 arousal, valence'로 모델링한다. Abdel-Ghaffar 2024가 encoding 실패 원인으로 든 반복 비정상성(Discussion 6째 단락)을 측정 대상으로 바꾼다.
  2. noise ceiling은 첫 제시와 이후 제시를 나눠 따로 계산한다. 반복 감쇠가 있으면 5회 평균 기반 ceiling은 '정상성' 가정을 어긴다.
  3. 회상: 지각 단계의 반복 감쇠가 큰 클립일수록 회상 중 amygdala 재활성이 작거나 큰가를 묻는다(감쇠는 학습의 지표일 수 있다).
  4. 회상은 눈을 감는 조건이라 각성과 호흡 상태가 지각과 다를 수 있는데 생리 기록 언급이 없으므로(0.5절), 회상-지각 비교에서 전역 신호 차이를 공변량으로 보고한다.
* **관련 Axis:** E, W, Q, A
* **근거 논문 ID:** doi:10.1126/sciadv.adw1464, doi:10.1038/s41467-024-49073-8, doi:10.1523/JNEUROSCI.1436-24.2025, doi:10.1016/j.neuroimage.2021.118617, doi:10.1038/s41597-026-07065-x
* **가능한 데이터셋:** Mind captioning(주), Horikawa 2020(같은 자극 1회 제시 기준선), NSD(보조, AI 추정 라벨)
* **예상되는 반론:** (1) "6명, 72클립으로 검정력이 부족하다." 대응: 개인 내 효과 크기 추정으로 한정하고 결과는 exploratory로 표시. (2) "반복 감쇠는 정서와 무관한 novelty 효과다." 대응: 감쇠 기울기의 평균이 아니라 '규범 arousal에 따른 기울기 차이'를 검정하고 시각 피질 감쇠를 대조로 둔다. (3) "MB6 중심부 잡음." 대응: 반복 간 amygdala split-half 신뢰도를 먼저 보고하고 낮으면 중단.
* **label-provenance:** felt / 별도 평정자 규범(C&K MTurk). 회상 vividness는 참가자 본인 보고(정서 보고 아님). **evidence-level:** R0. **signal-feasibility:** MB6 TE 30 ms 2 mm, 개인별 dropout 필수.
* **새로움 검색:** WebSearch "amygdala response repeated presentations emotional video clips arousal habituation fMRI encoding model Mind captioning dataset ds005191" → 일반 amygdala 습관화 문헌(얼굴, 사진)과 Jang & Kragel 2025 encoding만 확인, 이 데이터의 반복 효과 분석은 미발견. vision-decoding 0.1절도 회상의 정서 분석은 못 찾았다고 적었다. 판정: no(이 데이터와 설계 기준), 일반 습관화 현상은 yes.

### SN-P6 → llm-semantics (Chain 4 '신체 잔차')
* **제안 내용:** 너희 쪽 신체 잔차 검정을 우리 쪽 **신경/전신 분리와 '보고 생리 vs 측정 생리' 정렬**로 강화할 수 있다.
  1. 잔차가 insula, 뇌간 BOLD를 예측하는지는 raw BOLD와 생리 회귀 BOLD 둘 다에서 본다. 잔차 → insula 상관이 전역 자율신경 성분을 거쳐 생길 수 있기 때문이다(그러면 잔차는 'insula 신경'이 아니라 '몸 상태'를 예측한 것).
  2. Emo-FilM Physiology 항목(Heartrate, Breathing, Muscle, Throat, Stomach)은 평정자가 '보고한' 생리이고, PPG, 호흡은 fMRI 참가자의 '측정' 생리다. 자극 시점 수준에서 둘을 정렬하면 "MLLM이 놓치는 것은 보고 가능한 신체 감각인가, 보고되지 않는 자율신경 반응인가"를 나눌 수 있다.
  3. G5의 3분할(언어 / 몸 / 둘 다 아닌 신경)로 결과를 정리한다.
* **관련 Axis:** C, E, A, U
* **근거 논문 ID:** doi:10.1038/s41598-025-14961-6, doi:10.1162/imag.a.1300, doi:10.1038/s41593-025-01945-y, doi:10.1038/s41562-017-0069, doi:10.1093/scan/nsag050
* **가능한 데이터셋:** Emo-FilM
* **예상되는 반론:** "평정자와 참가자가 달라 '보고 vs 측정' 정렬은 개인 수준이 아니다." 대응: 자극 시점 수준 정렬로만 해석하고 그렇게 명시한다(label-provenance 표기).
* **label-provenance:** 인간 규범(별도 평정자, felt) vs AI 추정(MLLM) vs 참가자 측정 생리. **evidence-level:** R0. **signal-feasibility:** insula는 비교적 양호, 뇌간은 2.5 mm와 혈관 confound로 불리(Tyszka 2026 Usage Notes 마지막 단락).
* **새로움 검색:** llm-semantics의 검색(Chain 4 already_done no)에 기댄다. 생리 분리 추가 설계는 SN-P1과 같은 검색 범위에서 미발견.

### SN-P7 → emotion-theory, adversarial-reviewer (C2, U2/D1 Horikawa multiverse) [통합 제안]
* **제안 내용:** 너희 쪽 Horikawa multiverse(emotion-theory C2의 '피험자 간 신뢰 부분공간', adversarial-reviewer D1의 '라벨 비의존 중립 기준')와 내 Round 1 chain 2('network subspace x 전역/세션 성분 처리')는 같은 불일치를 다룬다. **하나의 사전등록 설계로 합치자.**
  * 요인: 입력 경로 3종(분산 기준 PCA / 평정 기반 voxel 선택 / 피험자 간 신뢰 부분공간) x 공간 범위(whole-brain / network별 / Tian 피질하) x 전역, 세션 성분 처리(없음 / 세션 평균 제거 / 전역 성분 제거).
  * 출력: 군집-평정 NMI(chance 보정), 군집-session/run NMI, 피험자 내 재현성, **Mind captioning 코호트로의 교차 재현**(같은 2,180 클립, 다른 6명).
  * 해석 공변량: network별 tSNR. Horikawa는 TE 43 ms라 vmPFC, OFC를 포함하는 DMN subspace가 다른 network보다 신호 손실에 취약할 수 있다(추론).
* **관련 Axis:** T, Q, E, O
* **근거 논문 ID:** arXiv:2507.00320, doi:10.1016/j.isci.2020.101060, doi:10.1038/s41593-025-01945-y, doi:10.1126/sciadv.abf7129, doi:10.1126/sciadv.adw1464
* **가능한 데이터셋:** Horikawa 2020, Mind captioning
* **예상되는 반론:** "multiverse가 커지면 forking path가 늘어난다." 대응: 사전등록, specification curve로 전부 보고, 주 결론은 사전 지정 경로 하나로 낸다.
* **label-provenance:** felt / 별도 평정자 규범. **evidence-level:** R0. **signal-feasibility:** network별 tSNR을 공변량으로 기록. 두 코호트의 TE, MB 차이(0.5절)도 요인으로 기록.
* **새로움 검색:** emotion-theory의 Stage 2 재점검 검색(WebSearch 'multiverse analysis emotion categories fMRI decoding analytic choices ...')에서 Horikawa multiverse 미발견. network별 재분석과 Mind captioning 교차 재현은 이번 라운드 검색에서도 찾지 못했다(Westlin 2025 외 Horikawa 재분석 목록: Du 2023, Kiyokawa 2024, Asanuma 2025, EmoMind 2026, Stage 1 기준). 판정: no.

---

## 3. 받은 제안에 대한 응답

(Coordinator가 전달한 뒤 추가)

---

## 4. Coordinator 질문 8개에 대한 답 (systems-neuro 관점)

**Q1. Vision Decoding 연구자가 Emotion Neuroscientist의 문제를 해결할 수 있는가?**
일부만. 시각 decoding과 encoding은 '자극으로 계산 가능한 기준선'과 controversial selection을 주어 정서 고유 분산 주장을 시험하는 데 강하다(encoding-foundation Chain 4). 시각 경로 중 정서와 직접 겹치는 곳은 SC-pulvinar-amygdala인데, 이 경로가 싣는 것은 시각 모델로 계산 가능한 저수준 feature일 수 있어 시각 모델이 가장 잘 기여하는 지점이다(doi:10.1016/j.neuron.2021.06.001, doi:10.1523/JNEUROSCI.1436-24.2025). 반면 피질하 신호 품질, 신체 상태, 라벨 주체 문제는 시각 decoding으로 풀리지 않는다. EmoNet은 Horikawa 자극으로 학습되어 그 데이터의 평가기로 쓰면 누수다(doi:10.1126/sciadv.aaw4358).

**Q2. LLM의 representation이나 reasoning을 neural emotion representation 분석에 활용할 수 있는가?**
가능하다. 다만 systems 관점의 한계가 분명하다. LLM과 MLLM은 신체 기반 정서에서 실패하고(doi:10.1038/s41598-025-14961-6), 영화 feature는 insula와 체성감각 영역을 거의 설명하지 못한다(doi:10.1162/imag.a.1300). 따라서 LLM은 '언어로 회복되는 정서 성분'의 통제 변수와 기준선으로 가장 유용하고, 남는 잔차를 생리와 대조해야 한다(SN-P6). Mind captioning의 '정서를 쓰지 말라' 지시 인간 캡션은 AI 캡션보다 깨끗한 내용 통제다(doi:10.1126/sciadv.adw1464).

**Q3. Generative AI로 emotion과 visual semantics를 분리해 검증할 수 있는가?**
in-silico(R1)까지는 가능하지만 내 담당 표적에서는 가장 약하다. amygdala 생성 제어는 지금까지 얼굴, 사람 같은 의미 범주를 통해서만 확인되었고(arXiv:2512.00557, generative-counterfactual CH2 인용), 자극 구동 encoder의 피질하 성능은 피질의 1/2~1/3이며 공개 TRIBE v2 checkpoint에는 피질하가 없다(arXiv:2605.04326, encoding-foundation 인용). 즉 피질하 생성 제어는 검증된 표적 모델이 없다. 또 생성 자극의 신기성 자체가 amygdala를 움직인다(doi:10.1038/s41467-024-49073-8 Discussion 6째 단락). 관찰 데이터만으로는 인과 결론을 낼 수 없다.

**Q4. Emotion Dynamics를 dynamical systems나 state-space learning 문제로 재정의할 수 있는가?**
그렇다. 다만 상태 변수에 **몸을 넣어야** 한다. rSLDS(pmlr:v54/linderman17a)나 energy landscape로 network 상태 전이를 모델링할 때, 자율신경 회복과 전역 성분은 모든 영역에 느린 공통 성분을 만들어 '관성'으로 오인될 수 있다(doi:10.1038/s41593-025-01945-y). 생리를 별도 잠재 변수로 둔 결합 상태공간이 필요하다. 동물 연구의 affective line attractor(doi:10.1038/s41586-024-07915-x)가 목표 기술 형식이고, 인간에서는 Emo-FilM washout이 가장 깨끗한 시험대다(G1, SN-P2). vmPFC 상태와 drift의 구분은 Chang 2021이 hybrid 모델을 요청한 열린 문제다(doi:10.1126/sciadv.abf7129 Discussion 4째 단락).

**Q5. Brain Foundation Model의 latent에서 감정 관련 구조를 찾을 수 있는가?**
찾을 수 있을지 모르지만 아직 누수 통제 benchmark가 없다(encoding-foundation U5). 내 쪽 주의 두 가지: (1) 휴지기 사전학습 모델(Brain-JEPA, arXiv:2409.19407)의 latent가 가장 쉽게 담는 것은 전역 자율신경 성분일 수 있으므로, 생리 회귀 전후로 probe 성능을 비교해야 한다. (2) Brain-JEPA는 Tian 피질하 50 ROI를 토큰으로 넣으므로 피질하 masking ablation으로 '정서 정보의 피질하 의존도'를 물을 수 있다(Round 1 chain 7). 기준선은 공개 arousal CPM(doi:10.1371/journal.pcbi.1012994)이다.

**Q6. Music, Video, Image의 공통 정서 특징과 modality-specific 특징을 뇌 수준에서 구분할 수 있는가?**
부분적으로 가능하지만 systems 관점의 교란이 크다. 자율신경 반응은 모달리티 일반적이므로 '초감각(supramodal) 정서 코드'의 일부가 공통 신체 반응일 수 있다. 실제로 SC-pulvinar-amygdala 경로는 부정 이미지와 소리 모두를 추적했지만 통증에는 반응하지 않았다(doi:10.1016/j.neuron.2021.06.001). vmPFC의 모달리티 독립 범주 코드(doi:10.1126/sciadv.adk6840)도 생리 통제 후 재검증이 필요하다. 데이터 측면에서 음악 전용 데이터는 없고, 무음 비디오(Horikawa, Mind captioning), 시청각 영상(Emo-FilM, Spacetop), 정지 이미지(NSD)는 획득 조건도 서로 달라(0.5절) 모달리티 차이와 획득 차이가 섞인다.

**Q7. Neuroscience에서 관찰되는 정서 관련 계산을 AI architecture의 구조적 제약으로 구현할 수 있는가?**
구현 후보는 있다. (a) 이중 경로: 얕은 층 shortcut + 깊은 피질 경로(arXiv:2607.19327, brain-inspired 인용; 인간 경로 근거 doi:10.1016/j.neuron.2021.06.001). (b) 내수용 상태 채널: 외부 감각과 별도로 신체 상태 잠재 변수를 두는 구조(알로스타시스 시스템, doi:10.1038/s41562-017-0069). (c) 기능 gradient를 위치 부호화로 쓰는 구조(Brain-JEPA, arXiv:2409.19407). 다만 이런 제약이 뇌 정렬이나 정서 행동을 개선하는지는 경험적 질문이며 brain-inspired 담당 영역이다. 내 쪽 기여는 (b)를 평가할 데이터(Emo-FilM 생리)가 있다는 점이다.

**Q8. 정서 라벨이 없는 NSD 같은 데이터도 representation alignment로 의미 있게 활용할 수 있는가?**
가능하지만 경로를 구분해야 한다. NSD는 다른 데이터셋과 자극을 공유하지 않으므로 공통 모델 feature 공간이나 비지도 정렬(수준 3)만 가능하다. 정서 라벨은 AI 추정이며 PPI 같은 보정이 필요하다(doi:10.1126/science.adi6000, adversarial-reviewer U5). systems 관점에서 NSD의 고유 가치는 7T 해상도(amygdala 세분, doi:10.1038/s41593-020-00711-6)와 반복 제시인데, 반복과 기억 과제가 amygdala 반응을 비정상적으로 만든다(doi:10.1038/s41467-024-49073-8). **같은 자극을 공유하는 정렬**이 필요하면 NSD보다 Horikawa 2020과 Mind captioning 쌍이 낫다(같은 2,180 클립, 다른 코호트와 획득 조건).

---

## 5. Axis 판정에 대한 입장 (근거 보강)

### 5.1 Acquisition & Signal Physics: 필수 태그화를 조건부 수용
* **수용하는 이유:** 태그로 두면 모든 후보 질문에서 점검되므로 Round 1에서 걱정한 '누락'은 상당 부분 해소된다.
* **조건 1 (태그 값의 구조화):** signal-feasibility 태그를 "점검 여부"만이 아니라 다음 6개 값으로 기록할 것을 제안한다: 데이터셋, 표적 영역, 획득 조건(TR/TE/MB/voxel), tSNR과 dropout 계산 여부, 생리 기록 유무, 전처리에서 WM/CSF/전역 회귀 여부. 0.5절 표가 이 형식의 예다.
* **조건 2 (연구 질문으로서의 측정 지형은 Sub-axis로 남김):** "정서가 어디에 있는가" 주장이 획득 물리(tSNR 지형, TE, MB)와 공변하는가는 그 자체로 연구 질문이다(Round 1 4절 C2). 태그는 질문을 생성하지 못하므로 무작위 조합 경로에 들어가지 않는다. 이를 **E의 Sub-axis "Measurement Geography of Neural Targets"**로 두어 조합에서 뽑힐 수 있게 하자.
* **새 근거:** Stage 2 이후 Horikawa 2020과 Mind captioning이 **같은 자극, 다른 획득 조건**(TE 43 vs 30 ms, MB4 vs MB6)의 쌍으로 확보되었다. 획득 물리의 효과를 자극 교란 없이 검정할 수 있는 조건이 생겼으므로 Sub-axis의 데이터 조건이 충족된다. 근거: doi:10.1126/sciadv.adw1464 Methods, doi:10.1016/j.isci.2020.101060, doi:10.1016/j.neuroimage.2021.118617, doi:10.1038/s41597-026-07065-x.
* **남는 이견:** 독립 Axis 주장은 철회하되, 위 두 조건이 받아들여지지 않으면 이견으로 유지한다.

### 5.2 Computational Psychiatry Phenotyping: O의 Sub-axis + 외부 분야 수용
* 임상 표본이 없고 설문이 제한적이라는 Coordinator 판정에 동의한다. Marek 2022(doi:10.1038/s41586-022-04492-9) 기준으로도 우리 데이터의 특성 상관은 탐색 수준이다. 외부 분야 목록에 남아 조합의 외부 개념 요건 단위로 쓰일 수 있으면 충분하다.

---

## 6. 새로움 주장 검색 경로 기록

| 제안 | 검색 경로(2026-11-12) | 결과 | 판정 |
|---|---|---|---|
| SN-P1 | WebSearch "inter-subject correlation physiological synchrony heart rate respiration emotional film fMRI ISC inflated noise ceiling correction"; Crossref 서지 검색으로 Madsen & Parra 2022 확인 | 심박 ISC 존재(doi:10.1093/pnasnexus/pgac020). ceiling 분해 연구 없음 | partially |
| SN-P2 | WebSearch "emotional carry-over fMRI after emotional film heart rate skin conductance recovery autonomic lingering brain state"; PubMed "Borchardt V[Author] AND Echoes of Affective Stimulation" | Borchardt 2018 영화 후 FC 이월 + HRV 감소(doi:10.1093/cercor/bhx290). 신경/자율 분리 여부는 초록에서 불명 | partially |
| SN-P3 | Round 1 WebSearch "superior colliculus pulvinar amygdala pathway naturalistic movie fMRI MPathI replication" | 자연 영상 경로 재현 없음, SC looming CCN 초록(search_index) | partially(Round 1 기록 유지) |
| SN-P4 | WebSearch "higher-order interactions homological scaffold fMRI global signal regression effect pairwise functional connectivity comparison" | scaffold와 GSR 관계 연구 없음 | no |
| SN-P5 | WebSearch "amygdala response repeated presentations emotional video clips arousal habituation fMRI encoding model Mind captioning dataset ds005191" | 일반 습관화 문헌, Jang & Kragel 2025. 이 데이터 반복 분석 없음 | no(설계 기준) |
| SN-P6 | llm-semantics 검색 결과 인용 | - | no(llm-semantics 판정) |
| SN-P7 | emotion-theory Stage 2 재점검 검색 인용 + Stage 1의 Horikawa 재분석 목록 대조 | network별, 교차 코호트 multiverse 없음 | no |

이번 라운드에서 내 Round 1 판정 하나를 바꿔야 한다: **Round 1 chain 5(자극 유발 landscape의 신경 관성)의 already_done은 "no"에서 "partially"로 낮춘다.** Borchardt 2018이 영화 후 network FC의 정서가 특이적 이월을 보였기 때문이다(영화 '중' 상태 전이의 관성과 개인 형질성은 여전히 미발견).

---

## 7. 미확인 사항과 이견

* Mind captioning 저장소(ds005191)에 생리, eye tracking 파일이 있는지는 미확인(논문 본문 키워드 검색 기준 언급 없음). 두 Horikawa 코호트의 피험자 중복도 미확인.
* Ke 2025 공개 CPM 가중치, Brain-JEPA checkpoint의 실제 위치와 라이선스는 여전히 미확인(GitHub, huggingface 접근 제약).
* Borchardt 2018, Madsen & Parra 2022, Jang & Kragel 2025는 초록 수준이다.
* SN-P4의 '전역 성분 불변성' 가설은 homological scaffold 계산 방식에 대한 내 추론이며 Zaffina 2026 본문(bioRxiv 429)을 읽지 못한 상태에서 세웠다. geometry-info는 C6 작성 시 본문을 읽었으므로(geometry-info round1 C6) 계산 세부에 대한 반박을 환영한다.
* encoding-foundation Chain 2와 내 Round 1 chain 1은 같은 데이터, 같은 변수(Emo-FilM 생리)를 쓴다. 중복을 피하려면 Stage 3 조합에서 하나로 합치거나, encoding-foundation은 '자극 구동 encoder의 맹점', 나는 'network 판독의 자율신경 성분'으로 역할을 나누는 것이 좋다. 이 분담 자체를 SN-P1의 응답에서 정하고 싶다.
