# Deliverable D: Discussion & Future-Direction Mining

* 작성: Coordinator (Stage 2). 이 파일은 `outputs/literature/build_future_directions.py`가 만든다. 표의 원 논문 ID, Discussion 위치, 데이터셋, overlap, 질문은 각 에이전트 round1.md 6절에서 추출했고(`outputs/literature/chains_index.csv`), 주제 분류와 "지금 가능해진 이유" 요약은 Coordinator 판단이다.
* 기준일: 2026-11-12
* 입력: `outputs/literature/literature_db.csv`의 future_directions(논문별), 11개 에이전트의 Discussion-to-Research chain

## 0. 요약과 선별 방법

1. **전체 future direction:** 문헌 DB의 future_directions는 674개다(`outputs/literature/future_directions_all.csv`, 한 줄에 하나). 그중 verified 논문이고 본문(full_text)을 읽었으며 already_done이 no 또는 partially인 후보는 **604개**다. already_done = yes는 9개(제외), unknown이나 미확인은 60개, 본문을 읽지 않은 논문에서 나온 항목은 25개다. 본문을 읽지 않은 항목은 CLAUDE.md 5절에 따라 future direction으로 쓰지 않는다.
2. **선별:** 604개를 하나씩 재판단하는 대신, 11개 에이전트가 P1 6절에서 만든 **Discussion-to-Research chain 80개**를 선별 결과로 쓴다. chain은 "원 논문 Discussion의 미해결 문제 → 그 뒤의 기술 발전 → 보유 데이터셋 조합 → 새 질문" 형식이며 원문 위치를 달고 있어, 지침의 선별 기준(2026년 모델이나 보유 데이터셋으로 새로 해결 가능)과 같은 판단을 이미 거쳤다. Coordinator는 chain을 주제 9개로 묶고 "지금 가능해진 이유"를 한 줄로 요약했다.
3. **선행 수행 여부:** chain의 already_done 판단은 각 에이전트의 검색 범위 안에서만 유효하다. Stage 3 Round 3와 Stage 4 선행연구 중복 감사에서 다시 확인한다.
4. **데이터:** 사용자 확인으로 4개 데이터셋의 원본 자극을 모두 보유하므로 G1 필요 chain도 실행 가능하다. 단 VD-R2는 4개 보유 데이터셋 밖의 Horikawa 2025 Mind captioning 데이터(OpenNeuro ds005191)가 필요하다.

## 1. 어떤 논문의 미해결 문제가 가장 많이 이어졌는가

chain의 Original Finding(출발 논문)과 Unresolved Question(미해결 문제 근거)에 인용된 횟수다. 한 chain이 같은 논문을 여러 번 인용해도 1로 센다.

| 논문 | 출발 논문으로 쓴 chain 수 | 미해결 문제 근거로 쓴 chain 수 |
|---|---|---|
| Horikawa T, Cowen AS, Keltner D, Kamitani Y, 2020, The Neural Represen... (doi:10.1016/j.isci.2020.101060) | 15 | 3 |
| Ma Y, Kragel PA, 2026, Map-like representations of emotion knowledge i... (doi:10.1038/s41467-025-68240-z) | 7 | 5 |
| Westlin C, Singh A, Erdogmus D, Stratis G, Barrett LF, 2025, Exploring... (arxiv:2507.00320) | 5 | 6 |
| Cowen AS, Keltner D (2017). Self-report captures 27 distinct categorie... (doi:10.1073/pnas.1702247114) | 7 | 2 |
| Kragel PA, Reddan MC, LaBar KS, Wager TD, 2019, Emotion schemas are em... (doi:10.1126/sciadv.aaw4358) | 2 | 6 |
| Chang LJ, Jolly E, Cheong JH, Rapuano KM, Greenstein N, Chen PHA, Mann... (doi:10.1126/sciadv.abf7129) | 4 | 4 |
| Du C, Lu Y, Huang Z, Sun Y, Zhou Z, 외, 2025, Bridging the behavior-neu... (arxiv:2509.24298) | 3 | 3 |
| Jang G, Kragel PA (2025). Understanding Human Amygdala Function with A... (doi:10.1523/jneurosci.1436-24.2025) | 3 | 3 |
| Mohammed BA, Gu L, Fang R (2026). EmoMind: Decoding Affective Captions... (arxiv:2605.16739) | 1 | 5 |
| Horikawa T, 2025, Mind captioning: Evolving descriptive text of mental... (doi:10.1126/sciadv.adw1464) | 3 | 2 |
| Tak AN, Gratch J, 2024, GPT-4 Emulates Average-Human Emotional Cogniti... (arxiv:2408.13718) | 3 | 2 |
| Tak AN, Banayeeanzade A, Bolourani A, Kian M, Jia R, Gratch J (2025). ... (arxiv:2502.05489) | 2 | 2 |
| Doerig A, Kietzmann TC, Allen E, Wu Y, Naselaris T, Kay K, Charest I, ... (doi:10.1038/s42256-025-01072-0) | 2 | 2 |
| Abdel-Ghaffar SA, Huth AG, Lescroart MD, Stansbury D, Gallant JL, Bish... (doi:10.1038/s41467-024-49073-8) | 2 | 2 |
| Zaffina L, Diano M, Petruso F, Preti MG, Amico E, Morgenroth E, Petri ... (doi:10.64898/2026.09.26.754452) | 3 | 0 |

Horikawa 2020(1순위 데이터셋 원 논문), Ma & Kragel 2026(Emo-FilM의 '이미 수행됨' 기준점), Cowen & Keltner 2017, Westlin 2025가 가장 많이 이어졌다. Kragel 2019(EmoNet)는 출발점보다 미해결 문제 근거로 더 많이 쓰였는데, 대부분 Horikawa와 같은 자극으로 학습된 누수 문제를 지적하는 맥락이다.

## 2. 선별한 future direction (주제별)

열 설명: **원 논문과 Discussion 위치**는 chain의 Original Finding에 적힌 출처, **지금 가능해진 이유**는 원 논문 당시에는 어려웠지만 2024~2026년 모델, 방법, 공개 데이터로 가능해진 점, **데이터셋**은 chain이 쓰는 4개 데이터셋, **overlap**은 `reference/existing_projects.md`와의 겹침 표시다. 질문은 원문을 줄였으며 전체 문장과 반증 조건은 해당 에이전트 round1.md 6절에 있다.

### T1. Horikawa 결론의 검증과 해부 (범주 결론, 재현 실패, 차원 수)

| chain | 원 논문과 Discussion 위치 | 지금 가능해진 이유 | 데이터셋 | 질문 (요약) | overlap |
|---|---|---|---|---|---|
| AR-D1 | 10.1016/j.isci.2020.101060 / doi:10.1016/j.isci.2020.101060, Discussion 1째, 4째 단락 | multiverse, specification curve 방법이 정착했고 Westlin 2025 재분석이 비교 대상으로 나옴. raw BIDS가 CC0 | Horikawa | Horikawa 데이터에서 '범주형, 고차원' 결론과 '개인 특이, 평정 무관' 결론은 분석 선택 공간의 어느 축에서 갈리며, 피험자 간 재현되는 자극 구동 분산만 남기면 어느 구조가 유지되는가? | EmoViS |
| ET-C1 | 10.1073/pnas.1702247114, 10.1016/j.isci.2020.101060 / 10.1073/pnas.1702247114, Results "Evidence for 27 Distinct Varieties" 절, Discussion 3째 단락; 10.1016/j.isci.2020.101060, Discussion 1, 4째 단락 | 반복 없이 피험자 간 cross-decomposition으로 rank별 신뢰 분산 추정(2024), rank별 개인차(2025) | Horikawa; Emo-FilM | 정서 관련 transmodal 영역에서 피험자 간 신뢰 공유 신경 차원의 스펙트럼은 시각피질처럼 scale-free인가, 특정 rank에서 꺾이는가? 그리고 공유 차원 중 시각-의미 feature로는 설명되지 않고 정서 평정으로만 설명되는 차원은 몇 개인가? | EmoViS |
| ET-C2 | 10.1016/j.isci.2020.101060, arXiv:2507.00320 / 10.1016/j.isci.2020.101060, Results "Distribution of Brain Activity Patterns" 절, Discussion 4째 단락; arXiv:2507.00320, Results, Discussion 2~3째 단락 | 피험자 간 신뢰 부분공간 추출, GLMsingle 재추정, 2-factor 교차검증 | Horikawa | 평정 정보를 쓰지 않되 피험자 간 신뢰 가능한 신경 부분공간으로 입력을 제한하면, Horikawa 정서 비디오 반응의 비지도 구조는 규범 정서 범주와 대응하는가? 그리고 Westlin이 보고한 개인 특이 군집은 피험자 내 session 간 재현되는 신뢰 가능한 개인차인가, session/run nuisance 구조인가? | - |
| GI-C1 | 10.1016/j.isci.2020.101060, arXiv:2507.00320 | cross-decomposition과 hyperalignment 스펙트럼(2024) | Horikawa; NSD | 정서 유발 비디오에 대한 transmodal 영역 반응에서 개인 간 공유되는 차원의 스펙트럼은 어떤 형태이고, 정서 평정이 고유하게 설명하는 공유 분산은 어느 rank 대역에 있는가? Westlin이 관찰한 개인 특이성은 고rank의 재현 가능한 개인 성분인가, 세션/런 drift 같은 저rank 비정서 성분인가? | EmoViS |
| SN-Chain2 | 10.1016/j.isci.2020.101060 / doi:10.1016/j.isci.2020.101060, Discussion 2~3째, 5째 단락 | 전역 성분의 자율신경 기원(2025), 상태 기반 틀, 피질하 atlas | Horikawa | Horikawa 데이터에서 정서 범주 구조가 관찰되는지는 어느 network subspace를 보는가와 전역/세션 분산을 어떻게 다루는가에 따라 체계적으로 달라지는가, 그리고 전역/감각 분산을 분리한 transmodal subspace에서는 비지도 군집도 규범 정서 평정과 정렬되는가? | EmoViS |
| FA-CH8 | arXiv:2303.09166, arXiv:2106.04619 / arXiv:2303.09166, 7 Discussion 'Implications and scope'; arXiv:2106.04619, 6 Discussion | 식별 가능한 multi-view contrastive, 조건부 contrastive | Horikawa; Emo-FilM | 같은 자극에 대해 피험자 간 공유되는 신경 latent는 몇 차원이며, 그중 정서 평정과도 공유되는 차원은 몇 개인가? 시각-의미 feature를 조건으로 통제하면 몇 개가 남는가? | EmoViS |
| ET-C6 | 10.1073/pnas.1702247114, 10.1093/cercor/bhae122 / 10.1073/pnas.1702247114, Discussion 4째 단락 마지막 문장; 같은 논문 Methods "Estimating Significance" 절 | 범주 점수 encoding을 가산성 검정으로 전환, 선택 비율 분포 라벨 | Horikawa; Emo-FilM | 단일 정서 비디오로 학습한 선형 encoding 모델은 혼합 정서 비디오의 반응을 영역별로 얼마나 예측하며, 비가산성(예측 실패)은 섬엽과 편도체 같은 영역과 vmPFC와 ACC 같은 영역 중 어디에 집중되는가? | EmoBrain |
| ET-C7 | 10.1073/pnas.1702247114, arXiv:2308.08708, 10.1016/j.tics.2024.06.007 / 10.1073/pnas.1702247114, Discussion 4째 단락; arXiv:2308.08708, 2.3.3절 | crossnobis와 2-factor 추론, 스펙트럼 smoothness 지표 | Horikawa | 정서 평정의 유사성 구조는 시각-의미 feature 유사성을 통제한 뒤 어느 영역의 신경 판별성으로 설명되며, 그 영역의 신경 공간은 평정 gradient를 국소적으로 보존하는 smooth한 부호를 보이는가? | EmoViS |
| GI-C7 | 10.1073/pnas.1800521115, 10.1073/pnas.1702247114 | IB 최적 경계 계산, 공유 정서 부분공간 | Horikawa; Emo-FilM | 인간 정서 범주 체계는 뇌의 공유 정서 공간에 대해 IB 최적 경계에 가까운가? 평정 공간 기준과 신경 공간 기준의 최적 범주 수는 다른가? | EmoViS |
| MD-Chain1 | 10.1126/sciadv.abf7129, 10.1038/nn.4468 / 10.1126/sciadv.abf7129, Discussion 3번째 단락; 10.1038/nn.4468, Discussion 1번째 단락 | 기술보다 데이터 구조 문제. 블록 길이 변이를 이용한 FIR, 개인 HRF, 순차 HMM | Horikawa; Emo-FilM | Horikawa에서 직전 비디오의 정서(34범주 profile)는 HRF 잔여와 직전 시각 내용을 통제한 뒤에도 다음 블록의 뇌 패턴에 남는가? 남는다면 이월 시간 척도는 영역별로(vmPFC, insula, amygdala 대 시각 피질) 다르고 정서 범주별로(공포, 혐오 대 오락, 기쁨) 다른가? 그리고 기존 블록 평균 decoding 성능의 일부는 이 이월 때문에 왜곡되었는가? * 원본 자극: 핵심 분석은... | - |
| MD-Chain8 | 10.1038/s41467-022-35654-y, 10.3389/fnhum.2021.676032 / 10.1038/s41467-022-35654-y, Discussion 8번째 단락; 10.3389/fnhum.2021.676032, Discussion 4번째 단락 | 시각 특징 분해, V-JEPA 2 층별 feature, MLLM 정서 기하 | Horikawa | Horikawa에서 미적 정서(aesthetic appreciation, awe, entrancement) 정보는 장면 배치, 자연 풍경, 움직임 같은 시각 특징으로 설명되는 분산을 제거한 뒤에도 DMN과 mPFC에 남는가? 장면 선택 피질의 미적 정서 신호는 전구 특징으로 설명되는가? 미적 정서는 다른 긍정 정서(joy, amusement)와 구별되는 신경 서명을 갖는가? * 원본 자극: figshare v... | EmoViS |

### T2. 정서 신호와 시각, 의미 내용 신호의 분리

| chain | 원 논문과 Discussion 위치 | 지금 가능해진 이유 | 데이터셋 | 질문 (요약) | overlap |
|---|---|---|---|---|---|
| AR-D2 | 10.1016/j.isci.2020.101060, arXiv:2509.24298 / doi:10.1016/j.isci.2020.101060, Results 'Disentangling...'; 세 모델 개별 적합 비교임을 본문 확인; arXiv:2509.24298, Results 'Bridging the behavior-neural gap...' | banded ridge와 SEM 신뢰도 보정 방법, 2024~2026 비디오와 VLM feature(원본 보유로 추출 가능) | Horikawa; Emo-FilM | 시각-의미 내용을 여러 지표의 잠재 구성개념으로 통제하고 각 feature 공간의 신뢰도를 반영하면, 정서 범주의 고유 설명 분산은 내용 지표 수에 따라 0으로 수렴하는가, 아니면 특정 영역(예: vmPFC, IPL)에서 0보다 큰 plateau를 유지하는가? | EmoViS |
| LS-Chain1 | 10.1038/s42256-025-01072-0, 10.1126/sciadv.adw1464 / doi:10.1038/s42256-025-01072-0, Discussion 첫째 단락; doi:10.1126/sciadv.adw1464, Discussion 첫째 단락과 한계 논의 첫 단락 | 정서 배제 지시로 받은 인간 캡션(Mind captioning 2025), LLM embedding 뇌 정렬(2025) | Horikawa | Horikawa 참가자의 뇌 반응에서 인간 규범 정서 평정이 정서 배제 캡션의 LLM embedding과 시각 feature를 넘어 설명하는 고유 분산은 어느 영역에 있으며, 그 지도는 MLLM 정서 추정의 고유 분산 지도와 겹치는가, 갈라지는가? | EmoViS |
| VD-R6 | 10.1038/s42256-025-01072-0, 10.1126/sciadv.adw1464 / doi:10.1038/s42256-025-01072-0, Discussion 첫째 단락; doi:10.1126/sciadv.adw1464, Materials and Methods "Caption annotation", Discussion 여덟째 단락 | 정서를 쓰지 말라는 지시로 받은 중립 캡션(Mind captioning), 정서 조건 캡션 재작성 | Horikawa | 정서를 쓰지 말라는 지시 아래 인간이 쓴 중립 캡션의 LLM embedding을 통제한 뒤에도 각 영역에 남는 C&K 규범 정서의 고유 설명 분산은 얼마인가. 그 잔차는 같은 캡션을 정서 언어로 재작성한 embedding으로 회복되는가, 아니면 언어로 회복되지 않는 시각 정서 성분이 남는가. | - |
| GC-CH1 | 10.1016/j.isci.2020.101060 / Horikawa 2020, 10.1016/j.isci.2020.101060, Discussion 5단락 | 참조 고정 최소 편집(BrainACTIV), Concept Sliders, LivePortrait. 원본 보유 | Horikawa | Horikawa에서 emotion category 모델이 우세했던 voxel의 encoder 예측 반응은, 의미 내용(캡션 embedding과 객체 구성)을 고정하고 정서 단서만 바꾼 편집에 따라 변하는가, 아니면 정서를 고정하고 의미만 바꾼 편집에만 변하는가? | EmoViS |
| EF-Chain4 | 10.1016/j.isci.2020.101060, 10.1016/j.neuroimage.2020.117258 / doi:10.1016/j.isci.2020.101060, Discussion 5단락; doi:10.1016/j.neuroimage.2020.117258, bioRxiv 판 Discussion 7단락 | 기존 자극에서 모델 예측이 갈리는 하위집합을 고르는 controversial selection(2024), 최신 foundation feature | Horikawa | 정서 규범 평정과 최신 시각-의미 foundation 표상이 서로 다른 뇌 기하를 예측하는 자극에서, 관찰된 transmodal 영역의 기하는 어느 쪽을 따르는가? | EmoViS |
| FA-CH5 | arXiv:2606.06857, arXiv:2506.11123 / arXiv:2606.06857, 7 Discussion 첫째~넷째 단락; arXiv:2506.11123, 5절 Conclusion | 안정 SAE(RA-SAE), 시공간 contrastive SAE, Universal SAE(2025~2026) | Horikawa; Emo-FilM | Horikawa에서 정서 평정과 공유되는 뇌 분산을 설명하는 sparse 개념 집합은 SAE 재학습과 backbone 교체에 걸쳐 안정한가? 안정한 개념은 정서 개념인가, 상황, 사람, 객체 개념인가? | EmoViS |
| FA-CH6 | arXiv:2609.34742 / arXiv:2609.34742, 초록 결과 3과 7 Conclusion | 정서 무관 정렬로 정서 vector를 운반하는 절차(2026) | Horikawa; NSD | 정서와 무관한 자극으로만 학습한 VLM→뇌 사상에 VLM 정서 vector를 통과시키면 고정서 자극에서의 뇌 정서 패턴 차이를 예측하는가? 그 정도는 정서 범주와 ROI에 따라 어떻게 다른가? | EmoViS |
| BI-Chain2 | 10.1016/j.isci.2020.101060 / doi:10.1016/j.isci.2020.101060, Discussion 1, 5번째 단락 | action-conditioned world model(V-JEPA 2), MLLM 행동 경향 주석. Emo-FilM Motivation 10항목 | Horikawa; Emo-FilM | 정서 범주 모형이 설명하는 transmodal 분산 중 얼마가 행동 경향(action readiness) 모형으로 대체되며, 범주 고유 분산은 남는가? | EmoViS |
| BI-Chain3 | 10.1016/j.neuron.2021.06.001, arXiv:2607.19327 / doi:10.1016/j.neuron.2021.06.001, Results/Discussion 통합 서술 후반; arXiv:2607.19327, Discussion 2번째 단락 끝 | MPathI, DNN 층 분할, recurrent 시각 모형. 원본 보유 | Horikawa; Emo-FilM; Spacetop | 34개 정서 범주 비디오에서 상구-pulvinar-편도체 경로 패턴은 혐오성 단일 축만 싣는가, 범주 특이 정보를 싣는가? 그 정보는 얕은 층(또는 저공간주파수) feature로 충분히 설명되는가? | EmoViS |
| BI-Chain6 | 10.1371/journal.pcbi.1011943, 10.1126/sciadv.abl8913, 10.1126/sciadv.aaw4358 / doi:10.1371/journal.pcbi.1011943, Discussion 첫 단락; doi:10.1126/sciadv.abl8913, Discussion 첫 단락; doi:10.1126/sciadv.aaw4358, Discussion | 이중 과제 학습과 lesion, MoE 사전지식(2025~2026) | Horikawa; NSD | 물체 + 정서 이중 과제 최적화는 정서 하위체계의 분리를 낳는가? 분리된 정서 unit은 Horikawa에서 시각피질보다 transmodal 영역 반응을 더 잘 예측하는가, lesion 시 transmodal 설명량이 선택적으로 줄어드는가? | EmoBrain |
| LS-Chain7 | 10.1073/pnas.1812250116, 10.1038/s41598-025-14961-6, 10.1093/scan/nsl014 / doi:10.1073/pnas.1812250116, Discussion 첫째 단락; doi:10.1038/s41598-025-14961-6, Results 'Well-estimated and Poorly-estimated Videos'와 Discussion 'On the other ha... | 비디오 분할과 inpainting, MLLM 정서 추정 | Horikawa; Emo-FilM | MLLM이 맥락만 보고 추정한 정서와 인물만 보고 추정한 정서는 Horikawa와 Emo-FilM 뇌 반응에서 서로 다른 영역(예: TPJ와 DMN vs STS와 얼굴 영역)의 고유 분산을 설명하는가, 그리고 둘의 상호작용(Kuleshov형 불일치)이 큰 클립에서 편도체와 측두극 반응이 커지는가? | - |
| EF-Chain6 | 10.1523/JNEUROSCI.1436-24.2025, arXiv:2605.13904 / doi:10.1523/JNEUROSCI.1436-24.2025, Discussion 6단락; 같은 논문 Discussion 8단락; arXiv:2605.13904, 6.6 Future work | 수백만 자극 screening으로 선택성 검정, RNC의 탐색과 in vivo 검증 결합(2025) | Horikawa; NSD | 정서 관련 영역에 대한 '정서 범주 선택성' 가설이 FFA, PPA 선택성처럼 고처리량 screening을 견디는가? 최고 예측 자극의 정서 일관성과 시각-의미 일관성은 어느 쪽이 큰가? | - |
| GC-CH6 | 10.1126/sciadv.aaw4358, 10.1038/s41467-024-53668-6, 10.1038/s41467-024-49073-8 / 10.1126/sciadv.aaw4358, Discussion 2단락; 10.1038/s41467-024-53668-6, Discussion 5단락 | controversial stimuli, 결정 경계 표집, model metamer | Horikawa; NSD | EmoNet, VV, 의미 기반 valence 모델이 서로 반대 valence를 예측하도록 합성한 이미지에서, NSD 학습 encoder의 시각피질과 amygdala 예측 반응, 그리고 인간 valence 평정은 각각 어느 모델을 따르는가? 뇌 encoder와 인간이 서로 다른 모델을 따른다면 그 해리는 무엇을 뜻하는가? | - |

### T3. 정서 지도, 전이, 동역학 (Ma & Kragel 2026 이후)

| chain | 원 논문과 Discussion 위치 | 지금 가능해진 이유 | 데이터셋 | 질문 (요약) | overlap |
|---|---|---|---|---|---|
| BI-Chain1 | 10.1038/s41467-025-68240-z / doi:10.1038/s41467-025-68240-z, Discussion 3, 6번째 단락 | successor representation과 경험적 전이 그래프 TEM 재학습. Emo-FilM 1 Hz 50항목 평정으로 방향성 전이 추정 가능 | Horikawa; Emo-FilM | 영화 시청 중 hippocampal-prefrontal 정서 표상은 정서 간 대칭 유사도가 아니라, 현재 정서에서 앞으로 어떤 정서가 올지에 대한 방향성 예측 구조(SR)를 담는가? 가치를 실은 SR은 vmPFC를 추가로 설명하는가? | Emo-FilM 연구 |
| GI-C2 | 10.1038/s41467-025-68240-z, 10.1371/journal.pbio.3003795 / Discussion 8째 단락 | SR과 다중 할인율, Emo-FilM 1 Hz 전이 추정 | Horikawa; Emo-FilM | hippocampus-vmPFC 정서 지도는 정적 동시발생 구조보다 경험된 전이 구조(successor geometry)에 더 잘 맞는가? 맞는 할인율 γ는 후측 hippocampus < 전측 hippocampus < vmPFC 순으로 커지는가? | Emo-FilM 연구 |
| AR-D3 | 10.1038/s41467-025-68240-z / doi:10.1038/s41467-025-68240-z, Results 'Structural abstraction...' 및 Fig. 5 설명 | ground truth 기반 식별 가능성 점검과 matched-complexity baseline 방법(2023~2024) | Emo-FilM | Emo-FilM의 hippocampal-prefrontal 신호는 TEM의 구조 추상화에 특이적인가, 아니면 같은 평정 궤적의 matched-complexity 비선형 확장이나 RL 계열 모델과 통계적으로 구별되지 않는가? 그리고 영화 14편 규모에서 이 구별은 원리적으로 가능한가? | Emo-FilM 연구 |
| FA-CH1 | 10.1038/s41467-025-68240-z / doi:10.1038/s41467-025-68240-z, Discussion 둘째 단락과 여섯째 단락 | 정서 라벨 없이 학습한 latent world model(V-JEPA 2), LLM 정서 표상의 인물 모델링 보고(2026) | Emo-FilM | Emo-FilM 시청 중 해마-vmPFC의 정서 지도 구조는 정서 평정과 무관하게 학습된 video world model의 상태 전이 구조를 통제한 뒤에도 남는가? 남는다면 어느 정서 항목과 해마 장축의 어느 위치에서 남는가? | Emo-FilM 연구 |
| BI-Chain7 | 10.1016/j.tics.2015.07.010, 10.1016/j.neubiorev.2022.104977 / doi:10.1016/j.neubiorev.2022.104977, 'Emotional state as cumulative' 절들 | momentum Kalman filter, leaky integrator. 1 Hz 연속 평정 | Emo-FilM | 영화 안의 느린 뇌 상태는 현재 정서 수준이 아니라 정서 변화의 누적(momentum)을 추적하는가? | Emo-FilM 연구 |
| MD-Chain7 | 10.1038/s41467-025-68240-z / 10.1038/s41467-025-68240-z, Discussion 6번째 단락 | 동역학 수준 비교 DSA, DynAffect | Emo-FilM | 정서 평정 궤적, vmPFC 신경 궤적, MLLM 궤적은 기하(지도)뿐 아니라 동역학(기저점으로의 이완 속도, 어트랙터 구조, 관성)에서도 같은가? 동역학 유사도는 영화 간, 참가자 간 일반화되며, 기하가 같아도 동역학이 다른 참가자(예: 정서 관성이 큰 사람)를 식별할 수 있는가? * 원본 자극: MLLM 궤적은 필요(보유), 평정-뇌 비교는 불필요. * 안전장치: fMRI 표본 간격(1.3 s)과 HRF ... | - |
| GI-C5 | 10.1016/j.cell.2022.11.027, 10.1038/s41586-024-07915-x | rSLDS 시간상수 추정, CEBRA. Emo-FilM 90 s washout과 EDA | Emo-FilM | 정서 영화가 끝난 뒤 정서 관련 잠재 차원은 감각 차원보다 느리게 이완하는가? 이완 시간상수는 영화 마지막 구간의 정서 종류와 강도에 따라 달라지고, 사람마다 영화 간 일관된가(형질성), 같은 사람의 EDA 회복 시간과 맞는가? | Emo-FilM 연구 |
| SN-Chain5 | 10.1016/j.nicl.2024.103574, 10.1016/j.jad.2026.121407, 10.64898/2025.11.30.691450 | 상태 의존 전환 rSLDS, 정서 관성 메타분석 | Emo-FilM; Spacetop | 정서 영화 시청 중 network 상태가 자극 정서 궤적이 요구하는 시점보다 늦게 이전 상태를 벗어나는 정도(신경 정서 관성)는 부정 정서 장면 이후에 커지는가, 영화를 바꿔도 개인 안에서 안정적인가? (개인 특성과의 상관은 효과 크기 추정 수준의 탐색으로 한정) | Emo-FilM 연구 |
| MD-Chain4 | 10.1126/sciadv.abf7129, 10.1038/s41467-025-68240-z, arXiv:2602.07570 / 10.1126/sciadv.abf7129, Discussion 3번째 단락; 10.1038/s41467-025-68240-z, Discussion 4번째 단락, post hoc; arXiv:2602.07570, 7 Conclusion | 멀티모달 모델의 문맥 길이 sweep(2026), surprise 메모리 | Emo-FilM; Spacetop | 정서 항목마다 고유 시간 척도(평정 자기상관, 그 항목을 가장 잘 예측하는 모델 문맥 길이)가 있는가? 그 시간 척도는 해당 정서를 가장 잘 부호화하는 뇌 영역의 시간 수용창과 일치하는가(예: surprise는 짧은 창과 감각, 측두 영역, love, guilt, satisfaction은 긴 창과 전방 hippocampus, vmPFC)? CPM 성분(Appraisal, Expression, Physiolog... | Emo-FilM 연구 |
| SN-Chain6 | 10.1016/j.isci.2020.101060 / doi:10.1016/j.isci.2020.101060, Discussion 5째 단락 | chronotopic 지도, principal gradient, HCP360으로 데이터셋 결합 | Horikawa; Emo-FilM | 정서 정보가 transmodal 끝에 위치하는 정도는 정서 항목의 고유 시간 척도로 예측되는가, 같은 이름의 정서가 짧은 무음 클립(Horikawa)에서는 gradient 중간에, 긴 소리 있는 영화(Emo-FilM)에서는 transmodal 끝에 표상되는가? | EmoViS |
| FA-CH3 | arXiv:2604.07729 / arXiv:2604.07729, 5.3절 셋째, 넷째 단락 | open VLM 정서 vector와 다모델 공유 정서 부분공간(2026), RepE | Emo-FilM; Spacetop | 영화 시청 중 정서 관련 뇌 반응은 장면 국소 정서 신호로 충분히 설명되는가, 아니면 HRF를 넘는 시간 상수의 누적(관성)이 필요한가? 같은 참가자에서 자기 경험 정서와 타인 정서 귀속은 같은 신경 방향을 공유하는가? | Emo-FilM 연구 |
| FA-CH4 | arXiv:2502.05489 / arXiv:2502.05489, 10 Discussion 첫째 단락 | LLM 내부 appraisal 조작(2025), SAE 인과 feature | Emo-FilM | Emo-FilM에서 appraisal 성분의 신경 표상은 discrete emotion 표상보다 시간적으로 선행하는가? LLM 내부 appraisal 조작으로 얻은 영향 행렬은 평정 시계열과 뇌에서 추정한 선행 관계와 일치하는가? | - |
| GI-C4 | 10.1126/sciadv.abf7129, 10.1016/j.isci.2023.107571 | rSLDS, Hyper-HMM, CEBRA | Emo-FilM | vmPFC 정서 표상의 개인차는 지도 자체의 차이인가, 같은 지도를 지나는 시점과 속도의 차이인가? 개인별 신경 time-warp는 같은 사람의 피부전도 반응 지연과 일치하는가? | Emo-FilM 연구 |
| GI-C6 | 10.64898/2026.09.26.754452 | PID / ΦID로 시너지 직접 정량, SRM | Emo-FilM | 자연주의 정서의 세밀한 프로파일 정보는 영역 쌍의 시너지로 존재하는가? 고차 위상의 이점은 차원 폭을 맞추면 사라지는가? | - |

### T4. 라벨 주체와 개인 경험 (본인 보고, peer 합의, 규범, AI)

| chain | 원 논문과 Discussion 위치 | 지금 가능해진 이유 | 데이터셋 | 질문 (요약) | overlap |
|---|---|---|---|---|---|
| ET-C4 | 10.1016/j.isci.2020.101060, arXiv:2507.00320, arXiv:2509.24298, 10.1073/pnas.1619316114 / 10.1016/j.isci.2020.101060, Limitations 1째 단락; arXiv:2507.00320, Discussion 8째 단락; arXiv:2509.24298, Results "Bridging" 절, Discussion "Bridging the behavior-neu... | self vs cross-prediction 설계(2024), 신뢰도 보정 논리, Spacetop peer 합의 활용 | Horikawa; Emo-FilM; Spacetop | 같은 영상에 대해 참가자 본인의 정서 보고는 peer 합의, AI 추정, 시청각-의미 feature가 설명하지 못하는 그 참가자 뇌 반응의 고유 분산을 설명하는가? 고유 분산이 있다면 어느 영역(vmPFC, TPJ, 섬엽)에 있으며 측정 신뢰도 보정 후에도 남는가? | - |
| ET-C5 | 10.1073/pnas.1702247114 / 10.1073/pnas.1702247114, Discussion 8째 단락; 같은 논문 Results "Emotion Elicitation" 절; Stage 1 1절 | 분포 라벨과 평정자별 모형. Emo-FilM 평정자별 원자료 공개 | Horikawa; Emo-FilM | 평정자들이 서로 다르게 보고하는 자극이나 시점에서 fMRI 피험자들의 정서 관련 신경 패턴은 (a) 피험자 안에서 모호해지는가(decoder 엔트로피 증가), (b) 피험자 사이에서 갈라지는가(패턴 일치 감소), (c) 변하지 않는가? 이 세 패턴의 비율로 평정 불일치를 자극 모호성, 개인 특이 반응, 측정 잡음으로 분해할 수 있는가? | - |
| ET-C8 | 10.1073/pnas.1702247114, arXiv:2507.00320, 10.1126/sciadv.abf7129 / 10.1073/pnas.1702247114, Discussion 9째 단락, 그림 S6; arXiv:2507.00320, Discussion 2, 7째 단락; 10.1126/sciadv.abf7129, Discussion 1, 5째 단락 | rank 범위별 신뢰 가능한 개인차 방법(2025). Spacetop 본인 평정 | Spacetop | 같은 영상을 본 참가자들 중 본인 정서 보고가 서로 비슷한 쌍은 어느 신경 rank 범위에서 서로 비슷한가? 정서 보고 유사성은 저차 고분산 성분(공유된 시각-의미 반응)이 아니라 고차 저분산 성분에 실려 있는가? | - |
| EF-Chain3 | arXiv:2605.04326, arXiv:2607.01400 / arXiv:2605.04326, 2.3절; arXiv:2607.01400, 7 Discussion 1단락, 8 Limitations | TRIBE v2의 새 피험자 예측과 짧은 fine-tuning, hyperalignment | Emo-FilM; Spacetop | 자극 구동 group 반응에서 벗어난 개인 특이 신경 반응이 같은 자극에 대한 그 개인의 정서 보고 편차를 예측하는가? 그 예측은 vmPFC처럼 개인 특이성이 큰 영역에 집중되는가? | - |
| GC-CH5 | 10.1016/j.isci.2020.101060, 10.1016/j.conb.2019.04.002 / 10.1016/j.isci.2020.101060, Limitations 1, 2단락; 10.1016/j.conb.2019.04.002, "Representational interpretations..." 절 | in-silico 기대 반응(TRIBE v2)과 fold 내 교란 회귀 | Emo-FilM; Spacetop | 같은 영상에 대해, 자극이 결정하는 기대 반응(TRIBE v2 예측 또는 다른 참가자 평균)에서 벗어난 개인 뇌 반응 편차가 그 참가자의 정서 보고가 집단 평균에서 벗어난 정도를 예측하는가? 어느 영역에서 그런가? | - |
| LS-Chain5 | arXiv:2408.13718, arXiv:2402.01908, arXiv:2507.00320 / arXiv:2408.13718, Study 2 논의와 Ethical Impact Statement 앞 단락; arXiv:2402.01908, Discussion 첫째 단락 | MLLM 평균 관찰자 예측, functional alignment | Spacetop | Spacetop 참가자의 영상별 자기보고가 MLLM 예측(평균 관찰자 대리)에서 벗어나는 정도는, functional alignment 후 그 참가자 뇌 반응에 남는 개인 특이 성분의 크기와 방향을 예측하는가? | - |
| VD-R5 | arXiv:2403.11207, arXiv:2510.25976 | 공유-개인 사상 구조(MindEye2, Brain-IT) | Horikawa; Spacetop | 공유 latent로 설명되지 않는 개인 잔차 성분이 그 참가자의 본인 평정이 집단 평균에서 벗어나는 정도를 예측하는가. 즉 공유 성분은 규범 정서(N), 개인 성분은 경험 정서(X)의 신경 대응물로 기능하는가. | - |
| GI-C3 | 10.1371/journal.pcbi.1012994, 10.64898/2026.09.26.754452 | warp hyperalignment / INT, Gromov-Wasserstein 정렬, Spacetop 본인 평정 | Emo-FilM; Spacetop | 자기보고 라벨과 개인화 정렬을 쓰면 valence의 교차 자극 전이가 arousal 수준으로 회복되는가, 아니면 관계 기하는 보존되지만 선형 좌표 사상만 맥락마다 바뀌는가? | EmoBrain |
| GI-C8 | 10.1038/s42003-022-04324-6, 10.1073/pnas.1816408116, 10.1038/s41593-023-01358-9, 10.1016/j.neuroimage.2020.116828 | INT 개인 tuning, shape metric. Spacetop 다과제 | Spacetop | 한 사람의 정서 표상 기하가 집단 템플릿에서 벗어나는 방향은 영상 경험, 표정 지각, 이야기, 통증 과제에서 일관되는가? 그 방향은 그 사람의 자기보고 정서 공존 구조로 예측되는가? | - |
| LS-Chain2 | 10.1038/s41467-019-13599-z, arXiv:2408.13718 / doi:10.1038/s41467-019-13599-z, Discussion 둘째 단락; arXiv:2408.13718, Study 2 A절 마지막 두 단락 | MLLM 사회 특징 주석(인간 평균과 r 0.79, 2025), 관점 조건부 prompt | Emo-FilM | Emo-FilM 시청 중 인물에게 귀속된 정서와 관객이 경험한 정서가 서로 어긋나는 구간(예: 인물은 공포, 관객은 연민이나 서스펜스)에서, TPJ와 dmPFC는 귀속 쪽 회귀자를, insula, 편도체, vmPFC는 경험 쪽 회귀자를 더 따르는가? | Emo-FilM 연구 |
| MD-Chain5 | 10.1016/j.neuroimage.2018.12.017, 10.3389/fnhum.2021.676032, 10.1037/0022-3514.65.1.45 / 10.1016/j.neuroimage.2018.12.017, Discussion 'Felt pleasure' 절 2번째 단락; 10.3389/fnhum.2021.676032, Discussion 'Interestingly' 단락 | Emo-FilM으로 시간축을 검증한 AI 연속 정서 추정, 정서 경계 검출 | Emo-FilM; Spacetop | 사후 정서 평가는 순간 정서 궤적의 어떤 요약(peak, end, 평균, 정서 경계 가중)으로 결정되며 그 규칙은 정서마다 다른가(예: 슬픔은 end, 공포는 peak)? 영상 종료 직후 hippocampus와 vmPFC 반응은 궤적 요약을 반영하며, 그 반응이 참가자 본인의 사후 평정 편차를 예측하는가? * 원본 자극: Spacetop 궤적 추정에 필요(보유). Emo-FilM 규칙 학습은 불필요. * 안전... | - |
| AR-D4 | 10.1162/IMAG.a.134, arXiv:2408.13718 / arXiv:2408.13718, IV General Discussion 3째, 6째 단락 | PPI(2023), DSL, alt-test(2025) 등 surrogate 라벨 보정 통계와 MLLM 주석 | Emo-FilM; Spacetop; NSD | AI 정서 라벨로 만든 voxel 수준 정서 지도는 어느 영역, 어느 정서 성분에서 편향되며, 무작위 인간 표본으로 PPI 보정하면 '정서 부호화 영역' 결론이 바뀌는가? 그리고 MLLM은 Emo-FilM 평정자를 어떤 CPM 성분에서 대체할 수 있고 어떤 성분에서 대체할 수 없는가? | - |
| LS-Chain6 | arXiv:2509.24298, 10.1038/s41598-024-65604-1, 10.1126/science.aaw8160 / arXiv:2509.24298, Limitations 둘째 단락; doi:10.1038/s41598-024-65604-1, Discussion 첫째 단락 | 다국어 LLM / MLLM, GWOT | Horikawa | 같은 Horikawa 비디오에 대해 일본어로 정서를 판단하게 한 MLLM 표상과 영어로 판단하게 한 표상 중 어느 쪽이 참가자 뇌 RSM과 항목 수준(GW 매칭률)에서 더 정렬되며, 그 차이는 valence와 arousal을 회귀한 잔여 구조에서 나타나는가? | - |

### T5. 몸과 생리 (자율신경, 내수용, 보고된 생리)

| chain | 원 논문과 Discussion 위치 | 지금 가능해진 이유 | 데이터셋 | 질문 (요약) | overlap |
|---|---|---|---|---|---|
| SN-Chain1 | 10.1371/journal.pcbi.1012994, 10.64898/2026.09.26.754452, 10.1523/JNEUROSCI.1759-16.2016 / doi:10.1371/journal.pcbi.1012994, Discussion 1째 단락 | 전역 fMRI 신호와 자율신경 결합(2025), 공개 arousal CPM 가중치 | Emo-FilM | 정서 영화 시청 중 network 수준 arousal 판독에서 참가자 자율신경-혈관성 전역 성분을 제거한 뒤에도 규범적 정서 arousal과 appraisal(Suddenly, Urgency 등)을 예측하는 신경 성분이 남는가, 남는다면 어느 연결에 있는가? | Emo-FilM 연구 |
| LS-Chain4 | 10.1038/s41598-025-14961-6, 10.1162/imag.a.1300, 10.1038/s41562-025-02203-8 / doi:10.1162/imag.a.1300, Conclusions; doi:10.1038/s41562-025-02203-8, Discussion 첫째~셋째 단락 | MLLM 시간 연속 주석, 평정자별 원자료로 라벨 noise 귀무분포 | Emo-FilM | Emo-FilM에서 MLLM과 인간 규범 평정의 일치도가 가장 낮은 CPM 성분은 Physiology와 Motor expression인가, 그리고 인간 평정에서 MLLM 예측을 뺀 잔차 시계열이 평정자 split 간 잔차(라벨 noise 귀무분포)보다 fMRI 참가자의 심박, EDA, insula와 뇌간 BOLD를 더 잘 예측하는가? | Emo-FilM 연구 |
| EF-Chain2 | arXiv:2605.04326, arXiv:2605.29850 / arXiv:2605.04326, 2.1절; 3 Discussion 2단락; arXiv:2605.29850, 4절 'Where the gains come from' | 3모달 비선형 encoder와 피질하 학습 스크립트, Emo-FilM 생리 | Emo-FilM | 정서 관련 피질하와 내수용 영역에서, ceiling으로 정규화했을 때 자극 구동 foundation encoder가 설명하지 못하는 신뢰 가능한 분산은 얼마인가? 그중 얼마가 참가자의 측정 생리, 얼마가 규범적 평가 성분으로 설명되는가? | Emo-FilM 연구 |
| ET-C3 | 10.1073/pnas.1702247114, 10.1073/pnas.1619316114, 10.1038/s41380-019-0520-3 / 10.1073/pnas.1702247114, Discussion 7째 단락; 10.1073/pnas.1619316114, HOTEC 절; 10.1038/s41380-019-0520-3, Discussion 1째 단락 | 고차원 시청각-의미 feature(원본 보유)와 Emo-FilM 참가자 생리 공개 | Emo-FilM | 시청각-의미 feature와 참가자 측정 생리를 모두 통제한 뒤 남는 '보고된 느낌(Feeling)' 고유 설명 분산은 PFC와 TPJ에 집중되는가(HOT 정합), 섬엽과 편도체에 남는가(1차 이론 정합), 아니면 넓게 분산되는가(분산 표상 정합)? 그리고 이 분포는 인지 평가(Appraisal) 항목의 분포와 다른가? | Emo-FilM 연구 |

### T6. In-silico 뇌와 foundation model의 정서 충실도

| chain | 원 논문과 Discussion 위치 | 지금 가능해진 이유 | 데이터셋 | 질문 (요약) | overlap |
|---|---|---|---|---|---|
| EF-Chain1 | arXiv:2605.16739 / arXiv:2605.16739, 4.2절, 5 Discussion 2단락 | TRIBE v2 공개(2026), modality dropout으로 무음 자극 입력 가능 | Horikawa; Emo-FilM | 관찰 fMRI에서 측정한 정서 표상 기하 가운데 자극 계산 가능한 group encoder가 재현하는 부분과 재현하지 못하는 부분은 어디인가? 재현되지 않는 잔차 기하는 시각-의미 feature를 통제한 뒤에도 정서 평정 기하와 정렬하는가? | - |
| GC-CH3 | arXiv:2605.04326 / arXiv:2605.04326, Discussion 1, 2단락 | TRIBE v2 공개, 학습 목록에 4개 데이터셋 없음(같은 자극으로 실측-예측 비교 가능) | Horikawa; Emo-FilM | 같은 자극에서 TRIBE v2 예측 반응과 실측 fMRI의 정서 표상 구조(정서 RSA, 정서 차원별 encoding 가중치)는 어느 영역, 어느 정서 차원에서 갈라지는가? 실측에서 예측을 뺀 잔차가 규범 정서 평정을 추가로 설명하는가? | Emo-FilM 연구 |
| EF-Chain7 | 10.1126/sciadv.adk6840, 10.1016/j.isci.2020.101060 / doi:10.1126/sciadv.adk6840, Discussion 3단락; doi:10.1016/j.isci.2020.101060, Discussion 마지막 단락 | TRIBE v2 modality dropout과 모달리티 ablation 지도 | Horikawa; Emo-FilM | 관찰된 vmPFC, pSTS 정서 신호 가운데 단일 모달 자극만으로 계산 가능한 부분과 다중 모달 통합이 필요한 부분은 어떻게 나뉘는가? 이 분할은 감각 박탈 연구의 결론(초감각 범주 부호)과 일치하는가? * already_done: partially (arXiv:2605.04326 2.8절은 정서와 무관한 일반 모달 기여 지도). overlap: Emo-FilM 연구 (멀티모달 encoder로 정서 기여 분... | Emo-FilM 연구 |
| EF-Chain5 | arXiv:2510.13768, arXiv:2506.11167 / arXiv:2510.13768, 5.4절, 6 Conclusion; arXiv:2506.11167, Discussion 'Limitations' 첫째 | CortexMAE 공개 가중치와 재현 가능한 평가, NeuroSTORM prompt tuning | Emo-FilM; Spacetop | 자극 없이 뇌 동역학만으로 사전학습한 latent 공간이, 영화와 피험자를 넘어 일반화되는 경험 정서 축(본인 보고)과 귀속 정서 축(타인 정서 판단)을 구분해 조직하는가? 그 구조는 자극 구동 예측과 단순 baseline을 넘어서는가? | - |
| SN-Chain7 | arXiv:2409.19407 / arXiv:2409.19407, Conclusion과 데이터 절 | 휴지기 사전학습 Brain-JEPA, 공개 arousal CPM 기준선 | Emo-FilM; Spacetop | 휴지기만으로 사전학습된 brain dynamics foundation model의 latent는 영화 중 규범 정서 profile을 parcel 기반 선형 모델보다 더 담고 있으며, 그 정보는 피질하 토큰 제거에 민감한가? | - |
| FA-CH7 | arXiv:2511.07988 / arXiv:2511.07988, 4절 Downstream Tasks Results | brain-tuning 절차(2025) | Horikawa; Emo-FilM; Spacetop | 정서 ROI 반응을 목표로 brain-tuning한 비디오 모델은 STS나 시각피질 표적 tuning보다 다른 데이터셋의 정서 평정과 정서 관련 뇌 반응을 더 잘 예측하는가? | EmoBrain |
| GC-CH7 | arXiv:2609.27729 / arXiv:2609.27729, Discussion 5.1 "Local validity" | 연속 편집과 참조 고정 편집, in-silico 국소 타당성 논의(2026) | Horikawa; NSD | 정서 편집 강도에 따른 encoder 예측 곡선과 인간 평정 곡선은 같은 선형 구간을 갖는가? 두 곡선이 갈라지는 강도는 편집 가족마다 다른가? | - |
| GC-CH2 | 10.1523/JNEUROSCI.1436-24.2025 / Jang & Kragel 2025, 10.1523/JNEUROSCI.1436-24.2025, Discussion 1, 6단락 | RNC 영역 간 공동 제어(2025), NeuroVolve 다중 목표(2025) | Horikawa; Emo-FilM; NSD | 얼굴, 신체, 장면 선택 영역의 예측 반응을 고정한 제약 아래에서 amygdala 예측 반응을 올리거나 내리는 편집이 존재하는가? 존재한다면 그 편집 방향은 인간 valence/arousal 평정과 어떤 관계인가(valence 단극 증가, 극단성 U자, 아니면 정서와 무관한 저수준 특징)? | - |
| VD-R4 | 10.1038/s41598-023-42891-8, arXiv:2403.11207, 10.1523/JNEUROSCI.1436-24.2025 / doi:10.1038/s41598-023-42891-8, Results "ROI-optimal stimuli"; arXiv:2403.11207, Appendix A.14; doi:10.1523/JNEUROSCI.1436-24.2025, Results, Discussion 여섯째 단락 | encoder gradient로 diffusion을 유도하는 BrainDiVE | Horikawa; NSD | 정서 유발 영상으로 학습한 편도체, 섬엽, vmPFC encoding model이 선호하는 합성 이미지는 인간 규범 정서 공간에서 영역마다 어디에 놓이는가. 그 선호는 저수준 속성으로 환원되는가, 의미 범주로 환원되는가, 둘 다 아닌가. 학습 자극 집합(영화 한 편 vs C&K 2,181클립)에 따라 선호가 바뀌는가. | - |
| VD-R1 | arXiv:2403.11207, 10.1038/s41598-023-42891-8 / arXiv:2403.11207, 2절, Appendix A.2; doi:10.1038/s41598-023-42891-8, Results "Which brain regions are used?" | 전뇌 foundation 해독(WAVE), Brain-IT 1시간 적응, C&K와 겹치지 않는 정서 평가기 | Horikawa | 시각피질만으로 재구성한 이미지는 원 자극 대비 정서 정보를 얼마나 보존하는가. 의미 충실도를 통제한 뒤에도 피질하, 변연계, 전두 입력을 추가할 때만 회복되는 정서 성분이 있는가. 있다면 그 성분은 arousal, valence, 특정 범주 중 어디에 집중되는가. | - |
| AR-D6 | 10.1038/s41562-023-01783-7 / doi:10.1038/s41562-023-01783-7, bioRxiv 판본 Discussion 1~2째 단락 | 예측 극값 선택, controversial selection, prevalence 추론(2023~2025) | Horikawa; Emo-FilM | 정서 feature encoding model이 특정 영역을 가장 강하게 구동하거나 억제한다고 예측한 비디오는 학습에 쓰지 않은 피험자와 자극에서 실제로 그렇게 작동하는가? 정서 모델과 시각-의미 모델이 서로 다른 비디오를 고를 때 어느 선택이 관찰 반응과 맞는가? | EmoBrain |

### T7. 소리, 서사, 예측 신호

| chain | 원 논문과 Discussion 위치 | 지금 가능해진 이유 | 데이터셋 | 질문 (요약) | overlap |
|---|---|---|---|---|---|
| MD-Chain2 | 10.1038/s41467-023-42241-2, 10.1111/cogs.13343 / 10.1038/s41467-023-42241-2, Discussion 2번째 단락; 10.1111/cogs.13343, Discussion 1번째 단락 | V-JEPA 2, 오디오-비디오 정렬 MLLM, 무학습 surprise 분절(2024) | Emo-FilM; Spacetop | 자연주의 영화의 정서 경계는 다중모달 예측 surprise(오차형) 또는 예측 불확실성(불확실성형)으로 환원되는가, 아니면 지각 surprise를 통제한 뒤에도 hippocampus 경계 반응과 vmPFC 상태 전이를 추가로 설명하는가? 놀람형 정서 경계와 서스펜스형 정서 경계는 Nguyen 2026이 보인 오차형, 불확실성형 신경 순서를 따르는가? 어떤 모달리티의 surprise가 어떤 정서 항목의 경계를 ... | Emo-FilM 연구 |
| MD-Chain3 | 10.1126/sciadv.adk6840, 10.1093/cercor/bhm011 / 10.1126/sciadv.adk6840, Discussion 2~6번째 단락 | 음원 분리, wav2vec, MERT, 단일모달 정보 제거 residual(2025) | Horikawa; Emo-FilM; Spacetop | (a) Emo-FilM에서 정서 항목과 CPM 성분마다 대사, 음악, 효과음, 영상 feature의 고유 설명량은 어떻게 다른가, 즉 어떤 정서가 '소리 의존적'인가? (b) vmPFC와 hippocampus의 정서 decoding은 대사 언어 feature와 음악 feature를 제거한 뒤에도 남는가(Lettieri 2024의 언어 의존 가설 검증)? (c) 무음 Horikawa에서 학습한 정서 RSA 구조... | Emo-FilM 연구 |
| GC-CH4 | 10.1038/s41467-025-68240-z / Jang & Kragel 2025, Discussion 7단락; Horikawa 2020, Discussion 7단락; 10.1038/s41467-025-68240-z, Discussion 1단락 | 영화 음향 3-stem 분리, 음향 입력 whole-brain encoder | Emo-FilM | Emo-FilM에서 음악 stem을 제거하거나 반대 정서의 음악으로 바꾸면, 1 Hz 정서 평정과 가장 강하게 결합된 영역들의 예측 반응이 얼마나 변하는가? 그 변화는 원본에서 음악이 있는 구간과 없는 구간의 정서 평정 차이(관찰)와 같은 방향인가? | Emo-FilM 연구 |
| FA-CH2 | arXiv:2502.11831, 10.1038/s41562-022-01516-2, arXiv:2111.14232 / arXiv:2502.11831, Discussion 첫째 단락; doi:10.1038/s41562-022-01516-2; 프리프린트 arXiv:2111.14232 Discussion 'Long-range predictions' | V-JEPA 2 predictor surprise 추출 공개 코드, LLM surprisal nuisance 틀(2026) | Horikawa; Emo-FilM | 자연 영화 시청 중 편도체, 전측 섬엽, vmPFC 반응과 평정자의 suddenness, predictability appraisal은 pixel, latent 물리, 서사 의미 예측오차 중 어느 것과 고유하게 결합하는가? 그 결합은 fMRI 참가자의 EDA 반응을 매개로 하는가? | - |
| LS-Chain3 | 10.1016/j.cub.2015.06.009, arXiv:2502.05489, 10.1038/s41467-026-71151-2 / doi:10.1016/j.cub.2015.06.009, Discussion 첫째~넷째 단락; arXiv:2502.05489, Discussion; doi:10.1038/s41467-026-71151-2, Discussion 첫째 단락 | 공개 LLM probe와 steering, LLM appraisal 파서. Spacetop narratives 텍스트 보유 | Spacetop | Spacetop 서사에서 LLM 내부 appraisal 방향(other-agency, goal conduciveness, expectedness 등)에 투영한 문장별 궤적은, 인간 연속 ToM 평정, 사회적 상호작용 평정, sentiment를 통제한 뒤에도 ToM 영역 BOLD를 설명하며, 그 설명이 텍스트판과 오디오판에서 같은 지도를 보이는가? | - |
| BI-Chain5 | 10.1162/neco_a_01341, arXiv:2407.02474, arXiv:2608.07480 / doi:10.1162/neco_a_01341, Discussion 첫 단락; arXiv:2407.02474, Abstract, Discussion; arXiv:2608.07480, Discussion | pymdp, HBI 모형 비교, video world model 예측 분산. 정서 계산 이론의 인간 benchmark가 비어 있음 | Emo-FilM; Spacetop | 정서 valence와 arousal은 결과 예측오차(RL)인가, 생성모형의 precision 갱신과 예측 불확실성(active inference)인가? 이야기 속 느낌은 단기 PE와 장기 기대 불일치 중 무엇으로 더 잘 예측되며, 그 계산 변수가 vmPFC/insula 반응을 설명하는가? | - |
| BI-Chain4 | 10.1073/pnas.2513856123 / doi:10.1073/pnas.2513856123, Abstract, Discussion 1, 2번째 단락 | distributional TD와 비대칭 PE 신경 분석(2025). Spacetop cue 조작이 공개 데이터에 있음 | Spacetop | cue와 일치하는 증거를 더 크게 반영하는 학습 편향은 (a) cue 일치성이 PE 신호의 gain을 바꾸는 단일 채널 기제인가, (b) 비대칭이 서로 다른 voxel 채널 집단의 읽기 문제인가? 그 구현은 pain, vicarious pain, cognitive effort에서 공유되는가? | - |
| MD-Chain6 | 10.1016/j.neuroimage.2018.12.017, 10.1016/j.cub.2019.09.067 / '억제 해제', 10.1016/j.neuroimage.2018.12.017, Discussion 'Aesthetically moving artworks engage the DMN' 절 1~2번째 단락 | 비디오, 오디오 예측 모델의 불확실성과 놀람, 동적 ISC | Emo-FilM | 영화의 미적 하이라이트 순간은 정서 강도(Emo-FilM 'Intense emotion' 등)를 통제한 뒤에도 DMN의 일시적 반응과 뇌 간 동기화를 만드는가? 다중모달 예측 모델의 불확실성 x 놀람 상호작용이나 '학습 진전'이 하이라이트와 그 신경 반응을 정서 강도보다 잘 예측하는가? * 원본 자극: 필요(보유). 외부 하이라이트 주석 접근 조건은 미확인. * 안전장치: 하이라이트 주석은 다른 관객의 생리 ... | - |

### T8. 기억, 심상, 반복 제시

| chain | 원 논문과 Discussion 위치 | 지금 가능해진 이유 | 데이터셋 | 질문 (요약) | overlap |
|---|---|---|---|---|---|
| VD-R2 | 10.1126/sciadv.adw1464, 10.1038/ncomms15037 / doi:10.1126/sciadv.adw1464, Results "Generating recalled content descriptions"; Discussion 둘째 단락: semantic feature가 visual feature보다 imagery 일반화가 좋음; doi:10.103... | 지각 decoder의 imagery 일반화(2025~2026). 단 Mind captioning 회상 데이터는 4개 보유 데이터셋 밖 | Horikawa | 같은 클립을 회상할 때 지각 학습 decoder로 해독되는 정서 정보는 의미, 시각 세부 정보보다 상대적으로 더 보존되는가(정서 우위 회상 가설). 그 보존은 규범 valence가 부정인 클립에서 더 크고 시행별 vividness와 연동되는가(NEVER). 재활성은 시각피질과 섬엽, vmPFC 중 어디에서 일어나는가. | - |
| VD-R3 | 10.1016/j.neunet.2025.107515, 10.1038/ncomms15037 / doi:10.1016/j.neunet.2025.107515, 2.2.1, 3 Discussion 첫째 단락; doi:10.1038/ncomms15037, Discussion 첫째 단락 | 정서 공간과 CLIP 공간 정렬, 34차원 연속 정서 해독(2026) | Horikawa | 학습에서 완전히 뺀 정서 범주의 클립을, 다른 범주로 학습한 decoder가 연속 정서 공간이나 언어 공간을 통해 식별할 수 있는가. 영역별로 어떤 표상은 조합적으로 일반화하고 어떤 표상은 군집 분류에 머무는가. | - |
| SN-Chain4 | 10.1038/s41467-024-49073-8, 10.1016/j.isci.2020.101060 / doi:10.1038/s41467-024-49073-8, Discussion 6째 단락; doi:10.1016/j.isci.2020.101060, Results | NSD 반복 번호와 간격, 7T amygdala 세분, VLM 정서 추정(AI 추정 라벨) | NSD | amygdala의 첫 제시 대비 반복 감쇠량은 이미지의 (AI 추정) 각성과 사회적 내용에 따라 달라지는가, 즉 amygdala의 정서 관련 정보는 반응 크기보다 반복에 따른 변화에 실려 있는가? | - |
| SN-Chain3 | 10.1016/j.neuron.2021.06.001 / doi:10.1016/j.neuron.2021.06.001, Results와 Methods Expt2 | Spacetop 획득 조건, 원본에서 looming 등 프레임 feature 추출, 피질하 atlas | Spacetop | 같은 참가자 안에서 colliculus-pulvinar-amygdala 경로 활동은 자연 영상의 위협 관련 시각 동역학(looming, 저공간주파수 운동)을 시간 단위로 따라가면서 열 통증에는 반응하지 않는 선택성을 유지하는가, 그리고 영상 단위 본인 공포 평정을 예측하는가? | - |

### T9. 방법론 인프라 (상한, leakage)

| chain | 원 논문과 Discussion 위치 | 지금 가능해진 이유 | 데이터셋 | 질문 (요약) | overlap |
|---|---|---|---|---|---|
| AR-D5 | 10.1016/j.isci.2020.101060 / doi:10.1016/j.isci.2020.101060, Discussion 6째 단락 | 피험자 간 상한과 GSN 방법, Emo-FilM 생리 공개, NSD 반복 자료로 보정 가능 | Horikawa; Emo-FilM; NSD | 반복이 없는 정서 fMRI에서 정서 모델이 설명 가능한 분산의 몇 %를 설명하는지 추정할 수 있는가? 피험자 간 상한은 반복 기반 상한을 얼마나 과소 또는 과대 추정하며(NSD 보정), 정서와 동기화된 생리 신호는 상한과 정서 encoding을 얼마나 부풀리는가(Emo-FilM)? | Emo-FilM 연구 |
| AR-D7 | 10.1038/s41467-024-46150-w / doi:10.1038/s41467-024-46150-w, Discussion 1~3째, 6~7째 단락 | leakage 분류(2023)와 REFORMS 체크리스트, 원본 보유로 비디오 근접 중복 탐지 가능 | - | 정서 decoding 성능 보고값 중 얼마가 동일 원본 클립, 시간 자기상관, 라벨 기반 voxel 선택, 사전학습 오염에서 오는가? | - |

## 3. 서로 다른 논문 두 편의 limitation을 연결해 생긴 질문

아래는 chain 중에서 **한 논문의 결과나 한계와 다른 논문의 한계가 맞물려** 질문이 생긴 경우를 Coordinator가 골라 정리한 것이다. 각 쌍의 출처는 해당 chain의 Original Finding과 Unresolved Question 항목이다.

| # | 논문 1의 결과 또는 한계 | 논문 2의 한계 | 둘을 연결하면 생기는 질문 | chain |
|---|---|---|---|---|
| 1 | Horikawa 2020 (doi:10.1016/j.isci.2020.101060): 평정이 fMRI 참가자가 아닌 별도 평정자 평균이라는 Limitations 1째 단락 | Westlin 2025 (arXiv:2507.00320): 개인 간 변동이 크다(preprint, 초록과 결과 기준) | 같은 자극에서 본인 보고가 타인 평균보다 그 사람 뇌를 더 잘 설명하는가. 개인 특이 신경 성분이 본인 보고의 편차를 예측하는가 | ET-C4, ET-C8, VD-R5, GC-CH5, EF-Chain3 |
| 2 | Horikawa 2020: emotion 모델이 visual, semantic 모델보다 transmodal 반응을 잘 설명(Discussion 5단락) | Abdel-Ghaffar 2024 (doi:10.1038/s41467-024-49073-8): 의미 효과가 중위 구조 특징일 수 있어 탈상관 자극이 필요(Discussion 4단락) | 의미를 고정하고 정서 단서만 바꾼 편집에서도 emotion 우위 voxel의 반응이 따라 변하는가 | GC-CH1 |
| 3 | Horikawa 2020: 세 모델을 따로 적합해 비교(Results 본문 확인) | Westfall & Yarkoni 2016 (doi:10.1371/journal.pone.0152719): 공변량 측정 오차가 증분 타당도 위양성을 만든다 | 내용 지표를 늘리고 신뢰도를 반영하면 정서 고유 분산은 0으로 수렴하는가, plateau를 유지하는가 | AR-D2 |
| 4 | Ma & Kragel 2026 (doi:10.1038/s41467-025-68240-z): TEM 환경이 대칭 유사도(MDS) 위 균등 무작위 보행(Methods) | doi:10.1073/pnas.1616056114: 정서 전이는 비대칭이며 유사도로 설명되지 않는다(Discussion, 에이전트 인용 기준) | hippocampus-vmPFC 정서 지도는 대칭 유사도가 아니라 방향성 전이 예측(successor representation)을 담는가 | BI-Chain1, GI-C2 |
| 5 | Doerig 2025 (doi:10.1038/s42256-025-01072-0): LLM 캡션 embedding이 고위 시각 반응과 정렬(Discussion 1단락) | Horikawa 2025 Mind captioning (doi:10.1126/sciadv.adw1464): 정서를 쓰지 말라는 지시로 받은 캡션이 있고 의미 feature 해독이 시각 feature보다 강함 | 정서 배제 캡션을 통제한 뒤에도 C&K 규범 정서의 고유 분산이 남는가, 언어로 회복되지 않는 시각 정서 성분이 있는가 | LS-Chain1, VD-R6 |
| 6 | Kragel 2021 (doi:10.1016/j.neuron.2021.06.001): colliculus-pulvinar-amygdala 경로가 혐오 정보를 부호화 | Leem 2026 (arXiv:2607.19327): shortcut 경로가 없으면 조건화가 재현되지 않음(Discussion 2단락) | 피질하 경로는 범주 특이 정보를 싣는가, 그 정보는 얕은 층(저공간주파수) feature로 충분한가 | BI-Chain3 |
| 7 | EmoMind 2026 (arXiv:2605.16739): TRIBE v2 합성 뇌로 대체하면 정서 RSA가 하락(실측과 합성의 자극 집합이 다름) | TRIBE v2 (arXiv:2605.04326): 학습 목록에 4개 데이터셋이 없고 피질하와 개인 readout이 없음 | 같은 자극에서 실측과 in-silico 예측의 정서 구조가 어느 영역, 어느 정서에서 갈라지며 잔차가 정서 평정을 추가로 설명하는가 | GC-CH3, EF-Chain1 |
| 8 | Lettieri 2024 (doi:10.1126/sciadv.adk6840): vmPFC의 모달리티 독립 범주 부호(감각 박탈 집단) | Horikawa 2020: 무음 자극이라 소리 기여를 볼 수 없음(Discussion 마지막 단락) | vmPFC, hippocampus 정서 신호는 대사 언어와 음악 feature를 제거해도 남는가, 무음과 소리 있는 데이터의 정서 RSA는 어떻게 다른가 | MD-Chain3, EF-Chain7 |
| 9 | Chang 2021 (doi:10.1126/sciadv.abf7129): vmPFC 상태의 개인 특이성 | Ma & Kragel 2026: 예측 시계열 유사도 구조가 참가자 간 매우 안정(같은 consensus 표적으로 학습) | vmPFC 개인차는 다른 지도인가, 같은 지도를 지나는 시점과 속도의 차이인가 | GI-C4 |
| 10 | Ke 2025 (doi:10.1371/journal.pcbi.1012994): dynamic FC로 정서 arousal 예측 | Bolt 2025 (doi:10.1038/s41593-025-01945-y): 전역 fMRI 신호가 교감 매개 생리와 결합 | network arousal 판독에서 자율신경-혈관 전역 성분을 빼도 규범 arousal과 appraisal을 예측하는 신경 성분이 남는가 | SN-Chain1 |
| 11 | Jang & Kragel 2025 (doi:10.1523/JNEUROSCI.1436-24.2025): 편도체 encoding model로 자극 합성 | NeuroVolve 2025 (arXiv:2512.00557): amygdala 최대화가 얼굴, 최소화가 건물로 의미 범주 조절이었음 | 얼굴, 신체, 장면 영역 반응을 고정한 제약 아래에서도 amygdala를 움직이는 편집이 있는가 | GC-CH2 |
| 12 | Yazdanpanah 2026 (doi:10.1073/pnas.2513856123): cue 기반 confirmation bias를 행동 수준에서 모델링 | distributional TD (doi:10.1038/s41586-019-1924-6): 비대칭 PE가 채널 집단으로 구현될 수 있음 | confirmation bias는 단일 채널 gain 조절인가, 비대칭 채널 읽기인가, pain과 vicarious pain에서 공유되는가 | BI-Chain4 |
| 13 | Kumar 2023 (doi:10.1038/s41467-023-42241-2), doi:10.1111/cogs.13343: 사건 경계와 예측 오차 | Nguyen 2026 (doi:10.7554/elife.107955): 오차형과 불확실성형 경계의 신경 순서 | 영화의 정서 경계는 다중모달 예측 surprise로 환원되는가, hippocampus 경계 반응을 추가로 설명하는가 | MD-Chain2 |
| 14 | Du 2025 (arXiv:2509.24298): 영어 기반 MLLM 정서 표상(Limitations 2째 단락) | doi:10.1038/s41598-024-65604-1: 정서 의미의 언어 의존성 | 일본어로 판단한 MLLM 정서 표상과 영어로 판단한 표상 중 어느 쪽이 Horikawa 뇌와 더 정렬되는가(참가자 언어는 미확인) | LS-Chain6 |
| 15 | Horikawa 2020 (Discussion 6째 단락): 반복 제시 부재로 설명 안 된 분산 추정 불가 | NSD 반복 자료와 피험자 간 상한 방법(doi:10.1371/journal.pcbi.1006397, doi:10.1093/scan/nsz037) | 피험자 간 상한은 반복 기반 상한을 얼마나 과소, 과대 추정하며 정서 동기 생리가 상한을 얼마나 부풀리는가 | AR-D5 |

## 4. 전체 future direction 목록과 상태

* 전체 목록: `outputs/literature/future_directions_all.csv` (열: uid, citation, discussion_read, fd_text, section, already_done, status, from_agent, applicable_datasets, axes)
* already_done 상태 분포 (verified 논문, 원 기록 기준):

| verified | discussion_read | already_done | 개수 |
|---|---|---|---|
| True | full_text | no | 369 |
| True | full_text | partially | 235 |
| True | full_text | unknown | 21 |
| True | full_text | 미확인 | 15 |
| True | no | unknown | 13 |
| True | abstract_only | unknown | 9 |
| True | full_text | yes | 9 |
| True | search_summary | unknown | 2 |
| True | abstract_only | no | 1 |

* unknown과 미확인으로 남은 항목은 선행 수행 검색을 하지 못한 것이다. Stage 3에서 해당 future direction을 쓰는 조합이 나오면 그때 검색한다.

## 5. 주의와 한계

* chain의 질문은 Round 1 독립 탐색 결과다. 서로 비슷한 질문(예: 본인 보고 vs 타인 평균 비교는 ET-C4, ET-C8, EF-Chain3, GC-CH5, LS-Chain5, VD-R5가 각각 제안)은 Stage 3 Round 2에서 합치거나 차별화한다.
* "지금 가능해진 이유"의 연도와 모델은 각 chain의 Technological Development 항목에 근거한다. 라이선스(TRIBE v2는 CC BY-NC 4.0 등)는 Deliverable B와 각 에이전트 round1.md 2절을 따른다.
* Westlin 2025는 arXiv preprint이며 재현 실패 보고다. 반대 증거로 확정해 쓰지 않는다.
* EmoNet은 Horikawa와 같은 Cowen & Keltner 비디오로 학습되었으므로 Horikawa 분석에서 feature나 평가기로 쓰는 chain은 누수 통제 조건으로만 쓴다(여러 chain이 이미 명시).
* chain에 인용되었지만 문헌 DB에 없는 식별자: arxiv:2111.14232, arxiv:2204.00673. 이 식별자는 verified로 확인되지 않았으므로 근거로 쓸 때 재확인이 필요하다.
