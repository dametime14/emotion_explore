# Round 1: Independent Discovery, Brain-Inspired AI & Neuromorphic Systems

* 작성: brain-inspired (Agent 11)
* 기준일: 2026-11-12
* 절차: `reference/protocols.md` P1. 독립 탐색이므로 다른 에이전트 폴더(`outputs/agents/<다른 이름>/`)는 읽지 않았다.
* 직접 읽은 지침과 자료: `CLAUDE.md`, `reference/protocols.md` P1, `reference/axes.md`, `reference/starting_papers.md`, `reference/existing_projects.md`, `outputs/stage1/dataset_intelligence_report.md`, `outputs/stage1/gate_decision.md`, `outputs/STAGE_STATUS.md`의 사용자 결정 기록, 그리고 라벨 항목 확인을 위해 `outputs/stage1/dataset_Spacetop.md`, `dataset_EmoFilM.md`, `dataset_Horikawa.md`의 해당 절.
* 문헌 기록: `outputs/agents/brain-inspired/literature.jsonl` (50편)

## 0. 요약과 검증 현황

### 0.1 문헌 수량 (P1 기준 대조)

| 기준 | 요구 | 결과 |
|---|---|---|
| verified 논문 | 12편 이상 | **50편** (crossref 39, arxiv 9, pubmed 2). 전부 DOI, arXiv ID, PubMed 경로로 존재를 직접 확인 |
| 2024~2026년 | 4편 이상 | **18편** |
| Affective Neuroscience 밖 분야 | 3편 이상 | **19편** (scene affordance, fMRI 시각 decoding, topographic DNN, connectomics, distributional RL, world model, homeostatic robotics, RL agent 서베이, neuromorphic 등) |
| Discussion/Limitations 직접 확인 | | full_text 26편, abstract_only 8편, search_summary 2편, no 14편 |

`discussion_read: "full_text"`는 본문에 접근해 Discussion, Limitations, Future Directions 해당 단락을 직접 읽었다는 뜻이다. 그중 일부(Geuter 2017, Jepma 2018, Margalit 2024, Lappalainen 2024, Emanuel & Eldar 2023, Mobbs 2021, Petzschner 2021, Keramati 2014, Dabney 2020)는 Discussion 전체가 아니라 미해결 문제와 향후 과제가 적힌 단락만 읽었고, 읽은 위치를 `future_directions[].section`에 적었다. `"no"` 14편은 식별자로 존재만 확인했고 본문 주장에 기대지 않는다.

`already_done`에는 스키마의 no / partially / yes 외에 `unknown (미검색)`을 썼다. 이번 라운드에서 선행 수행 여부를 검색하지 못한 항목을 "no"로 적으면 사실과 달라지기 때문이다.

(Stage 2 재점검 반영) `outputs/literature/verification_sample.md`의 지적에 따라 모든 future direction의 선행 수행 여부를 arXiv API, Crossref, PubMed MCP, WebSearch로 다시 검색했다(2026-11-12). `unknown`은 모두 없앴다: unknown 45개 중 15개는 no, 8개는 partially로 바꾸었고, 22개는 본문을 읽지 않은 논문의 '(본문 미열람)' 자리표시라 삭제했다. 기존 no 17개 중 6개를 partially로 바꾸었고(no→yes는 0개), partially 1개(Kragel 2021, 근거가 미검증 포스터)를 no로 바꾸었다. 판정이 no인 항목에는 `search_scope`, 판정을 바꾼 항목에는 `recheck_note`를 달았다. 재검색에서 근거로 찾은 논문 6편(Mohammadi 2023, Leitão 2020, Morgenroth 2026, Jang & Kragel 2025, Liu et al. 2025 bioRxiv, Thornton et al. 2019)을 jsonl에 추가해 총 56편(2024~2026년 21편, crossref 42, arxiv 9, pubmed 5)이 되었다. 아래 1절과 6절의 해당 항목 끝에 바뀐 내용을 적었다.

### 0.2 접근 제약 (사실 기록)

* `pmc.ncbi.nlm.nih.gov`는 셸 curl 시 대부분 reCAPTCHA 페이지가 반환되어, PMC 전문은 PubMed MCP(`get_full_text_article`)로 읽었다.
* `www.nature.com`은 `idp.nature.com`으로 리다이렉트되며 차단, `elifesciences.org`는 406, `ojs.aaai.org`는 해석 불가였다. 우회하지 않고 PubMed MCP나 다른 공식 경로로 대체했다. AAAI 논문 1편은 서지 확인을 못 해 jsonl에 넣지 않았다.
* GitHub 저장소는 이번 세션 허용 범위 밖이라 코드 라이선스는 WebSearch 수준으로만 확인했다(2절 표에 수준 표시).

### 0.3 EmoPathway 확인 결과

* 검색 경로: arXiv API(`all:EmoPathway`, abstract 검색 "emotion pathway" AND brain/fMRI), Crossref query, Semantic Scholar(결과 없음), WebSearch 2회("EmoPathway", "Emo-Pathway" OR "EmoPath").
* 결과: **"EmoPathway"라는 이름의 논문이나 모형은 찾지 못했다(2026-11-12).** 존재 미확인으로 두며, 이 이름을 근거로 쓰지 않는다.
* 개념이나 이름이 가까운 확인된 후보:
  * **Leem, Keil, Ding, Fang (2026), arXiv:2607.19327** (Neural Computation 게재 승인 표기). Visual-Valence model: frozen VGG16(시각피질) + valence 모듈(편도체 LA/CE, OFC 영감) + 초기 시각층에서 valence 모듈로 가는 **Shortcut pathway**. 저자들은 이 shortcut이 다중 경로 가설(LeDoux 등)에 근거한다고 밝히고, shortcut이 없으면 Pavlovian 조건화를 재현하지 못했다고 보고했다(Discussion 2번째 단락 끝, Supplement 근거). 본문 직접 확인. 가장 가까운 후보다.
  * AVF-BEL (Wang et al. 2025, arXiv:2503.16454): Brain Emotional Learning 계열 시청각 경로 모형. 초록만 확인.
  * HEmoN (Huang et al. 2024, arXiv:2408.00525): 위계 정서 영역을 정보 융합으로 찾는 모형. 초록과 본문 일부 확인.
  * AAAI의 dual-pathway(개념 경로 + 지각 경로) 얼굴 정서 인식 모형: WebSearch 결과에만 보였고 서지를 확인하지 못했다(search_index 수준, jsonl 미포함).
* 권고: 사용자가 EmoPathway의 출처(저자, 학회, 링크)를 주면 재확인한다.
* (Stage 2 재점검 반영) 같은 연구군(Ding, Keil, Fang)의 Liu et al. (2025, bioRxiv, doi:10.1101/2025.10.20.683439) Visual Cortex Amygdala(VCA) 모형도 후보에 추가한다. vision transformer와 편도체 모사 모듈을 feedforward로 연결하고 편도체 fMRI와 비교한다(초록 기준). EmoPathway라는 이름은 여기서도 보이지 않았다.

---

## 1. 중요한 미해결 문제

### P-1. 정서 '지도'는 유사도 구조인가, 전이 예측 구조인가
* Ma & Kragel (2026)은 Emo-FilM에서 hippocampus와 vmPFC가 지도 같은 정서 표상을 가진다고 보고하고, 이것이 "사건 전이의 통계 학습"에서 올 수 있다고 해석했다(Discussion 6번째 단락).
* 그런데 Methods를 직접 읽어 보면 TEM 환경은 **평정 시계열 상관(1-r)의 MDS 2D 좌표를 격자화**한 것이고, agent는 그 위를 **균등 확률 random walk**로 걸었다. 즉 모형에 들어간 것은 대칭적 유사도이며 실제 정서 시간 전이가 아니다.
* Thornton & Tamir (2017)는 정서 전이가 비대칭이고 유사도로 설명할 수 없다고 보고했다(Discussion 3번째 단락).
* 저자들도 RL 기반 해마 모형과의 비교를 향후 과제로 남겼고(Discussion, Limitations 단락), graph형과 map형 표상의 관계도 열린 문제라고 적었다(Discussion 6번째 단락).
* 근거: doi:10.1038/s41467-025-68240-z, doi:10.1073/pnas.1616056114, doi:10.1038/nn.4650, doi:10.1016/j.cell.2020.10.024
* (Stage 2 재점검 반영) Thornton, Weaverdyck, Tamir (2019, doi:10.1523/JNEUROSCI.1431-18.2018)가 이미 현재 정신상태의 신경 패턴이 가능성 높은 미래 상태 패턴을 닮는다고 보고했다(사회 뇌, 특히 mPFC, 초록 기준). 따라서 "정신상태 표상에 전이 예측이 들어 있다"는 일반 주장은 신경 수준 선행이 있다. 남는 미해결 부분은 (a) 영화에서 경험된 정서 동역학, (b) 해마 SR/TEM 같은 특정 계산 모형 사이의 비교, (c) 대칭 유사도 성분을 통제한 방향성 검정이다.

### P-2. 정서 범주 표상은 '느낌'인가, 행동 affordance나 action readiness인가
* Horikawa et al. (2020)은 수동 시청 중에도 이 시스템들이 "emotional experience (or affordances)"를 부호화한다고 쓰고, 정서를 반응 결정 전에 적응 행동을 준비시키는 시스템 전반의 적응으로 해석했다(Discussion 2번째 단락). 이 해석은 검증되지 않았다.
* Bartnik et al. (2025)은 장면 affordance 표상이 물체, layout으로 환원되지 않으며 DNN feature가 affordance보다 물체 쪽에 정렬된다고 보고하고, 그 원인을 체화 결여로 보며 embodied AI와 vision-language-action 모형 비교를 제안했다(Discussion 7번째 단락과 마지막에서 둘째 단락).
* Emo-FilM에는 행동 경향을 직접 묻는 Motivation 10항목(Stop, Undo, Repeat, Oppose, Tackle, Command, Support, Move, Care, Attention)의 1 Hz 별도 평정자 평정이 이미 있다(`dataset_EmoFilM.md` 항목표). 정서 범주와 행동 경향이 같은 뇌 분산을 설명하는지 직접 비교할 수 있는 드문 조건이다.
* 근거: doi:10.1016/j.isci.2020.101060, doi:10.1073/pnas.2414005122, doi:10.1016/j.tics.2016.03.013, doi:10.1016/j.neubiorev.2022.104977
* (Stage 2 재점검 반영) 위의 "검증되지 않았다"는 표현은 범위를 좁혀야 한다. component process model 기반 fMRI가 행동 경향 성분의 신경 네트워크를 이미 보고했다: Mohammadi et al. (2023, doi:10.1093/cercor/bhad093)은 정서 클립에서 approach/avoidance 경향을 포함한 component별 네트워크를 식별했고, Leitão et al. (2020, doi:10.1371/journal.pbio.3000900)은 상호작용 게임에서 motivation 등 component의 네트워크와 동기화를 보이며 체화되고 행동 지향적인 정서 해석을 지지했다(둘 다 초록 기준). 남는 미해결 부분은 Horikawa 34범주 표상과 행동 경향 모형의 **직접 경쟁**(어느 쪽 분산이 다른 쪽을 대체하는가)이다. 또 Morgenroth et al. (2026, doi:10.1037/emo0001619)은 Emo-FilM 평정에서 13개 이산 정서가 모두 component로 신뢰성 있게 예측된다고 보고해, 두 band의 공선성이 클 것임을 시사한다.

### P-3. 피질하 '빠른 경로'는 범주 특이 정보를 싣는가, 그 내용은 정말 '조잡한(coarse)' feature인가
* Kragel et al. (2021)은 multivariate pathway identification(MPathI)으로 인간 상구-pulvinar-편도체 경로를 식별했고, 이 경로가 불쾌 이미지와 소리의 혐오성을 추적하지만 통증과 쾌 이미지에는 약하다고 보고했다. 편도체 연결은 low road, high road(시각피질), 개념적 top-down의 3개 성분으로 나뉘었다. 경로와 의식적 정서 경험의 관계는 추가 연구가 필요하다고 적었다.
* Leem et al. (2026)의 DNN에서는 shortcut 경로가 조건화에 필요했다. 반면 McFadyen et al. (2017)은 pulvinar-편도체 연결이 공간주파수와 정서에 무관하다고 보고했다(WebSearch 요약 수준). 즉 "shortcut = 저공간주파수"라는 등식 자체가 불확실하다.
* fMRI는 latency를 측정하지 못한다(Méndez-Bértolo 2016의 '빠른' 경로는 두개내 기록). 따라서 fMRI로 검정할 수 있는 것은 속도가 아니라 **경로가 싣는 표상 내용**뿐이다.
* 근거: doi:10.1016/j.neuron.2021.06.001, arXiv:2607.19327, doi:10.1523/JNEUROSCI.3525-16.2017, doi:10.1038/nn.4324, doi:10.1126/sciadv.aaw4358
* (Stage 2 재점검 반영) 편도체를 DNN feature로 encoding한 선행이 있다: Jang & Kragel (2025, doi:10.1523/JNEUROSCI.1436-24.2025)은 장편 영화 시청 fMRI로 편도체 하위영역 encoding 모형을 만들고 합성 자극으로 검증했고, Liu et al. (2025, bioRxiv, doi:10.1101/2025.10.20.683439)은 feedforward VCA 모형을 편도체 fMRI와 비교했다(둘 다 초록 기준). Badarnee et al. (2026, doi:10.7554/eLife.108043)은 위협 학습 중 pulvinar 분할 표상을 다뤘다. 남는 미해결 부분은 상구-pulvinar-편도체 **경로** 수준 표상 내용, 얕은 층 대 깊은 층 feature 비교, 34범주 비디오로의 확장, 그리고 recurrence다. 이전 판정에서 근거로 쓴 VSS 2026 포스터는 식별자로 확인하지 못해 근거에서 뺐다.

### P-4. 정서 계산 모형(active inference, RL agent)은 인간 데이터로 거의 검증되지 않았다
* Hesp et al. (2021)은 valence를 행동모형 기대 precision의 갱신(affective charge)으로 정식화하고, 다음 단계로 신경영상과 행동 패러다임에 적합해 RL과 Bayesian model comparison을 하라고 명시했다(Future Empirical Directions 첫째, 둘째 단락).
* 5년 뒤인 Pattisapu et al. (2024)과 Schumann et al. (2026)도 여전히 시뮬레이션뿐이며 인간 데이터와 비교하지 않았다고 스스로 적었다(각 Discussion의 limitations).
* Moerland et al. (2018)의 RL 정서 agent 서베이도 정서 동역학을 다루면 인간 경험 데이터와 비교해야 한다고 했다(Discussion, Testing and quality 단락).
* PubMed(2021년 이후) 검색에서 affective inference 모형을 fMRI에 적합한 연구를 찾지 못했다.
* 근거: doi:10.1162/neco_a_01341, arXiv:2407.02474, arXiv:2608.07480, doi:10.1007/s10994-017-5666-0
* (Stage 2 재점검 반영) PubMed와 WebSearch로 다시 찾아도 affective inference 정서 모형을 인간 행동이나 fMRI에 적합한 연구는 찾지 못했다. 결론 유지. 다만 시간 맥락을 넣은 정식화(Hinrichs et al. 2025, arXiv:2506.08599, 시뮬레이션)는 이미 있다.

### P-5. 기대가 지각을 바꾸는 confirmation-biased learning은 뇌에서 어떻게 구현되는가
* Yazdanpanah et al. (2026)은 통증, vicarious pain, 인지 노력에서 cue와 일치하는 PE에 learning rate가 더 큰 confirmation bias를 행동 수준에서 보였다. 저자들은 표준 Bayesian predictive coding이 이 비대칭을 포착하지 못한다고 하고, 기계적 설명으로 "양/음 강화에 서로 다른 뉴런 하위집단" 또는 metaplasticity를 제시했다(Discussion, predictive processing 단락).
* Dabney et al. (2020)의 distributional RL은 바로 그런 하위집단 비대칭의 다양성을 도파민 뉴런에서 보였고, 기분과 우울이 RPE 비대칭에서 올 수 있다고 마지막 단락에서 추측했다.
* Jepma et al. (2018)은 기대가 수정하는 통증 처리 단계의 특정, 그리고 기대, 기분, 정동 학습의 상호작용을 미해결로 남겼다(Discussion 후반).
* Lin et al. (2025)이 보상 과제 7T에서 PPE/NPE 분리와 learning rate 편향의 신경 상관을 보였지만(초록 기준), cue 일치성에 따라 비대칭이 바뀌는 조건부 비대칭과 통증/사회 cue 맥락은 다루지 않았다.
* 근거: doi:10.1073/pnas.2513856123, doi:10.1038/s41586-019-1924-6, doi:10.1038/s41562-018-0455-8, doi:10.1073/pnas.2500815122, doi:10.7554/eLife.24770
* (Stage 2 재점검 반영) distributional 부호는 도파민 밖에서도 보고되었다: Muller et al. (2024, doi:10.1038/s41593-023-01535-w)은 macaque ACC, Sousa et al. (2025, doi:10.1038/s41586-025-09089-6)은 도파민 뉴런의 다차원 분포 지도를 보고했다(모두 단일 뉴런). 동적 precision 기반 통증 기대 학습(HGF) 모형도 있다(Drusko et al. 2023, doi:10.1038/s41598-023-29758-8). 위약 기대가 NPS(상향식 통각 신호)에는 매우 작게 작용한다는 메타분석(Zunhammer et al. 2018, doi:10.1001/jamaneurol.2018.2017)은 "기대가 어느 처리 단계를 바꾸는가"에 부분적으로 답한다. 인간 fMRI에서 cue 일치성에 따른 조건부 PE 비대칭을 검정한 연구는 여전히 찾지 못했다.

### P-6. 정서에 전용 처리 구조가 필요한가, 범용 시각 표상에서 창발하는가
* Liu et al. (2024)은 물체 인식만 학습한 CNN에서 정서 선택 unit이 창발하고 lesion하면 정서 인식이 저하됨을 보였으나, 3범주(쾌/불쾌/중립)만 다뤘고 신경 기록과 비교하지 않아 신경적 관련성은 추측적이라고 적었다(Limitations).
* Dobs et al. (2022)은 다중 과제 최적화가 얼굴/물체 하위체계 분리를 낳는다고 보였지만, 어떤 기능이 특화될지는 완전히 예측하지 못하며 음식처럼 망에서는 분리되나 뇌에서는 보고되지 않은 사례도 있다고 적었다(Discussion 4번째 단락).
* MoRE-Brain (2025)은 뇌 네트워크 원리를 따른 MoE를 썼지만 시각 ROI만 입력으로 써서 "보는 것"만 다룬다고 스스로 한계를 적었다(Appendix Limitations).
* 근거: doi:10.1371/journal.pcbi.1011943, doi:10.1126/sciadv.abl8913, arXiv:2505.15946, doi:10.1126/sciadv.aaw4358

### P-7. 순간 정서와 누적 정서(기분, momentum)의 관계와 신경 표상
* Eldar et al. (2016)은 기분을 보상 변화의 momentum 표상으로 보고, 기분이 뇌에서 어떻게 표상되는지, 오래가는 기분과 짧은 정서가 어떻게 상호작용하는지를 미해결로 남겼다(Outstanding Questions 1, 2).
* Schumann et al. (2026)은 valence가 단기 PE만 반영해 장기 기대 불일치를 놓친다고 적었다(Discussion, limitations 첫째).
* naturalistic 영화 데이터(Emo-FilM 1 Hz)에서 이 구분을 검정한 연구는 이번 검색에서 찾지 못했다.
* 근거: doi:10.1016/j.tics.2015.07.010, arXiv:2608.07480, doi:10.1016/j.neubiorev.2022.104977

### P-8. 항상성 setpoint가 없는 정서(사회, 미적 정서)의 계산적 지위
* Keramati & Gutkin (2014)은 homeostatic RL을 항상성 조절계가 없는 보상(사회 보상, 새로움)으로 확장하는 것을 핵심 과제로 남겼다(Limitations and future directions 첫 단락). Petzschner et al. (2021)은 신체 조절에 내부 상태의 명시적 표상이 얼마나 필요한지를 열린 질문으로 둔다(Outstanding Questions).
* Horikawa의 34범주에는 awe, aesthetic appreciation, entrancement 같은 비항상성 정서가 많고, Emo-FilM에는 참가자 생리(PPG, 호흡, EDA)가 공개되어 있다.
* 근거: doi:10.7554/eLife.04811, doi:10.1016/j.tins.2020.09.012, doi:10.1101/2024.06.03.597087

---

## 2. 주목해야 할 모델과 방법론

라이선스 열의 수준: [본문] 논문에서 직접 확인, [검색] WebSearch 결과 수준, [미확인] 확인 못 함.

| 모델/방법 | 근거 ID | Pretrained weights | Input → Output | 학습 목표 | 라이선스 | 이 프로젝트에서의 용도와 주의 |
|---|---|---|---|---|---|---|
| **Successor Representation (SR)**, value-weighted SR | doi:10.1038/nn.4650 | 해당 없음(해석적 계산: M = (I - γT)^-1) | 상태 전이 행렬 T → 상태별 미래 점유 기대 | TD 학습 또는 해석해 | 해당 없음 | Emo-FilM 1 Hz 평정에서 방향성 전이 행렬을 추정해 정서 SR을 만들고 해마-vmPFC를 예측. **T와 그 전치 T'는 대칭 유사도 성분이 같으므로 "전이 방향" 효과만 분리하는 대조가 가능**(6절 Chain 1) |
| **Tolman-Eichenbaum Machine (TEM)** | doi:10.1016/j.cell.2020.10.024, doi:10.1038/s41467-025-68240-z | 공개 사전학습 가중치 없음(연구마다 학습). Ma & Kragel은 11x11 격자 16개 환경, 32,000 iteration 학습 | (관찰 one-hot, 행동) → 다음 관찰 예측. 층 g(구조), p(결합) | 다음 관찰 예측 | [미확인] (Ma & Kragel 코드 공개 여부도 이번 본문 추출에서 미확인) | 환경 그래프를 대칭 MDS가 아니라 실제 전이로 바꾼 재학습이 핵심 |
| **Distributional TD** | doi:10.1038/s41586-019-1924-6 | 해당 없음(알고리즘) | 보상 시퀀스 → 채널별 비대칭 RPE, expectile 집합 | 비대칭 TD | 해당 없음 | Spacetop social에서 voxel 수준 PE 비대칭 다양성 검정. voxel은 뉴런이 아니므로 반증용으로 제한 |
| **pymdp** (active inference) | arXiv:2201.03904 (제목, ID만 확인) | 해당 없음(생성모형을 연구자가 정의) | POMDP A, B, C, D 행렬 → 사후 신념, expected free energy, 정책 | 변분 자유에너지 최소화 | MIT [검색] | Hesp 2021의 affective charge, Pattisapu 2024의 entropy 기반 arousal을 Spacetop 과제 생성모형에 구현해 RL과 비교 |
| **HBI** (hierarchical Bayesian inference, Piray) | doi:10.1073/pnas.2513856123 (Yazdanpanah가 사용) | 해당 없음 | 모형 집합 + 행동 → 모형 증거, 집단/개인 파라미터 | 계층 베이즈 | [미확인] | Spacetop 행동 모형 비교를 Yazdanpanah와 같은 방식으로 재현하는 기준 |
| **MPathI** (multivariate pathway identification) | doi:10.1016/j.neuron.2021.06.001 | 해당 없음 | 두 영역의 trial별 다변량 패턴 → 최적 연결 패턴 가중치 | 영역 간 공분산 최대화(SVD) | MATLAB 코드 공개로 서술(URL은 추출 과정에서 누락) [미확인] | Horikawa 2,181개 단일 시행 반응에서 상구-pulvinar-편도체 경로 패턴 추정 |
| **Visual-Valence + Shortcut** | arXiv:2607.19327 | 시각 모듈은 ImageNet VGG16(공개), 학습된 valence 모듈 가중치 공개 여부 [미확인] | 이미지 → valence(1~9) | valence 회귀 + Pavlovian compound 학습 | 코드 github `lab-smile/FearConditioningAI` [본문], 라이선스 [미확인] | shortcut vs 전체 위계 feature 분리의 설계 원형. recurrence 없음 |
| **Object-trained CNN의 정서 선택 unit** | doi:10.1371/journal.pcbi.1011943 | ImageNet VGG16, AlexNet(공개) | 이미지 → 층별 활성, 선택성 지수 | 물체 분류(정서 학습 없음) | torchvision 가중치 조건 [미확인] | lesion/gain 조작을 encoding model에 넣어 정서 선택 unit의 뇌 설명 기여 측정 |
| **EmoNet** | doi:10.1126/sciadv.aaw4358 | 공개 여부 [미확인] | 이미지 → 20 정서 범주 | AlexNet 마지막 FC 재학습 | [미확인] | **누수 경고: Cowen & Keltner 비디오 2,185개의 프레임 137,482장으로 학습했다(Methods 원문 확인). Horikawa 자극과 같은 원천이므로 Horikawa 분석에 쓰면 학습-평가 누수.** NSD, Emo-FilM, Spacetop에는 사용 가능 |
| **MoRE-Brain** (hierarchical MoE) | arXiv:2505.15946 | arXiv v3 기준 "곧 공개" 표기 [본문] | NSD GLMsingle beta(nsdgeneral) → CLIP embedding → 확산모형 이미지 | expert별 CLIP 정렬 + routing | [미확인] | 피험자별 router만 적응하는 구조를 정서 encoding에 이전. 원 모형은 시각 ROI만 |
| **V-JEPA 2** | arXiv:2506.09985 (제목, ID 확인) | 공개 | 비디오 클립 → latent, 예측기(latent 미래 예측) | masked latent prediction(제목 기준 planning 포함, action-conditioned 변형 세부는 본문 미확인) | 코드 MIT, 체크포인트별 MIT/Apache-2.0 혼재 [검색] | Chain 5의 '관찰자 world model' 예측 불확실성 계산 후보. Nayebi 2023이 latent 미래 예측 모형과 고차 피질 정렬을 보인 것이 논리 근거. overlap: EmoBrain (V-JEPA2 사용) |
| **DeepGaze IIE** | arXiv:2105.12441 (제목, ID 확인) | 공개 [검색] | 이미지 → 고정 확률 지도 | saliency 예측 | [미확인] | Horikawa Limitations가 지적한 자유 시청 시선 효과의 대리 nuisance. 비디오 saliency로의 확장은 검증 필요 |
| **ViTPose** | arXiv:2204.12484 (제목, ID 확인) | 공개 [검색] | 프레임 → 인체 keypoint | 지도학습 pose 추정 | Apache-2.0 [검색] | 화면 속 행위자의 ethogram(portrayed behavior) feature. 무음 Horikawa에서도 사용 가능 |
| **TDANN** (topographic DNN) | doi:10.1016/j.neuron.2024.04.018 | 공개 여부 [미확인] (STAR Methods에 Data and Code Availability 절은 있음) | 이미지 → 피질 위치를 가진 unit 활성 | contrastive SSL + 공간 매끄러움 | [미확인] | 공간 제약 + valence 목표가 정서 지형을 낳는지 in-silico 검정(비용 큼, 우선순위 낮음) |

방법론 평가 한 줄:
* **우선순위 높음:** SR, distributional TD, MPathI, pymdp/HBI 비교. 이미 공개된 라벨과 fMRI만으로 돌릴 수 있고(Horikawa 일부, Emo-FilM, Spacetop), 모형이 "도구"를 넘어 경쟁 가설을 낸다.
* **우선순위 낮음:** SNN/neuromorphic(Roy 2019, Kasabov 2026). 현재 정서 SNN 연구는 표현된(portrayed) 정서 분류 정확도 중심이고, spike timing 가설은 fMRI 시간해상도로 검증할 수 없다. 이 프로젝트의 데이터와 과학적 기여 기준에서는 직접 쓸 곳이 거의 없다고 판단한다.

---

## 3. 다른 분야에서 가져와 적용할 수 있는 연구 아이디어

| # | 원 분야와 개념 | 정서 연구로의 이전 | 데이터 | 근거 ID |
|---|---|---|---|---|
| I-1 | RL / Neuro-AI: distributional RL(채널별 비대칭 RPE) | Spacetop social의 cue 의존 confirmation bias가 "단일 PE 채널의 gain 조절"인지 "비대칭이 서로 다른 다중 voxel 채널"인지 검정. Dabney의 예측(비대칭과 reversal point의 상관)을 voxel 수준으로 옮김 | Spacetop social (G1 불필요) | doi:10.1038/s41586-019-1924-6, doi:10.1073/pnas.2513856123, doi:10.1073/pnas.2500815122 |
| I-2 | 해마 계산: successor representation | 정서 상태 공간 SR(방향성 전이)로 해마-vmPFC 표상 예측. 대칭 유사도(MDS), TEM-random walk와 경쟁 | Emo-FilM (G1 불필요) | doi:10.1038/nn.4650, doi:10.1038/s41467-025-68240-z, doi:10.1073/pnas.1616056114 |
| I-3 | Ecological psychology / embodied AI: affordance, VLA | 정서 범주 표상 vs 행동 경향 표상 경쟁. Emo-FilM Motivation 10항목은 인간 평정, Horikawa는 신규 주석(인간 또는 MLLM, AI 추정 표기) | Emo-FilM (G1 불필요), Horikawa (G1 필요) | doi:10.1073/pnas.2414005122, doi:10.1016/j.isci.2020.101060 |
| I-4 | Active inference + world model: 관찰자를 agent로 모형화 | 영화 시청 중 arousal을 "관찰자 예측모형의 불확실성(entropy)"으로 정의(Pattisapu의 정식화). video world model 예측 분산을 Emo-FilM Predictable, Suddenly, Alert 평정과 참가자 EDA, insula/편도체 반응에 대응 | Emo-FilM, Spacetop alignvideo (G1 필요) | arXiv:2407.02474, arXiv:2305.11772, arXiv:2506.09985 |
| I-5 | Computational cognitive neuroscience: 다중 과제 최적화와 특화 창발 | 물체 + 정서 이중 과제 망에서 정서 하위체계 분리 여부, 분리 unit의 Horikawa transmodal 예측력, lesion 효과 | Horikawa (G1 필요), 학습용 정서 라벨은 Cowen & Keltner와 독립인 자료 필요(후보 미확인) | doi:10.1126/sciadv.abl8913, doi:10.1371/journal.pcbi.1011943 |
| I-6 | Connectomics: connectome-constrained 모형 | 세포 수준 인간 connectome은 없으므로, 개인 DWI tractography 연결 강도를 피질하-피질 정서 경로 RNN의 구조 제약으로 사용. 제약이 개인별 반응 예측을 개선하는지 검정 | Spacetop (ses-01에 DWI 있음, `dataset_Spacetop.md`) | doi:10.1038/s41586-024-07939-3, doi:10.1038/s42256-023-00748-9 |
| I-7 | Computational ethology: 자동 행동 분할(ethogram) | 화면 속 행위자의 pose 기반 행동(접근, 회피, 얼어붙음, 돌봄)을 portrayed behavior feature로 만들어 evoked 정서와 분리. CLAUDE.md의 "자극에 묘사된 정서 vs 참가자 경험" 구분을 feature 수준에서 구현 | Horikawa, Emo-FilM, Spacetop (G1 필요) | doi:10.1016/j.neuron.2021.05.021, doi:10.7554/eLife.75027, arXiv:2204.12484 |
| I-8 | Active perception: saliency/시선 모형 | Horikawa 원 저자가 남긴 시선 교란(Limitations 마지막 단락)을 예측 saliency로 통제하고, 정서별 시선 분포 차이가 transmodal 정서 패턴을 얼마나 설명하는지 추정. NSD 일부 세션 eye tracking으로 예측 saliency의 타당성 점검 가능성(품질 가변, Stage 1 보고서) | Horikawa, NSD | doi:10.1016/j.isci.2020.101060, arXiv:2105.12441 |
| I-8 보완 | (Stage 2 재점검 반영) MR 기반 시선 추정 | eye tracker가 없는 Horikawa에서도 안구 MR 신호로 시선을 추정하는 DeepMReye(doi:10.1038/s41593-021-00947-w)와 영화 시청 fMRI 시선 예측(Gao et al. 2026, doi:10.1093/psyrad/kkag026)을 쓰면 예측 saliency보다 직접적인 시선 교란 변수를 만들 수 있다. 전제: Horikawa raw BIDS의 촬영 범위에 안구가 들어 있는지 확인 필요(미확인) | Horikawa, Emo-FilM | doi:10.1038/s41593-021-00947-w, doi:10.1093/psyrad/kkag026 |
| I-9 | Homeostatic RL | 참가자 생리(심박, EDA)를 내부 상태로 삼아 "항상성 편차 변화"가 어떤 정서 항목과 뇌 반응을 설명하는지, 설명하지 못하는 정서(사회, 미적)는 무엇인지 분리 | Emo-FilM (G1 불필요) | doi:10.7554/eLife.04811, doi:10.1101/2024.06.03.597087, doi:10.1016/j.tins.2020.09.012 |

---

## 4. 기존 Affective Neuroscience와 예상 밖으로 연결될 수 있는 개념

1. **통증의 confirmation bias, 도파민의 distributional code, 기분.** 세 문헌이 서로를 인용하지 않지만 같은 계산 대상(양/음 PE의 비대칭)을 다룬다. Yazdanpanah 2026은 비대칭의 기제로 하위집단을 제안했고(Discussion), Dabney 2020은 하위집단 비대칭 다양성을 보이고 기분과의 연결을 추측했으며(마지막 단락), Eldar 2016은 기분을 PE 누적으로 정의했다. 연결 가설: cue에 일치하는 증거만 키우는 학습은 '낙관/비관 채널 중 무엇을 읽느냐'의 문제이고, 그 읽기 편향이 기분처럼 느리게 변한다. 근거: doi:10.1073/pnas.2513856123, doi:10.1038/s41586-019-1924-6, doi:10.1016/j.tics.2015.07.010
2. **Alexithymia와 credit assignment.** Emanuel & Eldar (2023)는 분노와 슬픔 중 무엇을 느낄지는 나쁜 결과의 원인을 누군가의 행동에 귀속할 수 있느냐에 달렸고, 귀속이 불확실하면 분화되지 않은 부정 정서가 최선일 수 있다고 썼다(Disentangling emotions 둘째 단락). 이것은 "범주적 vs 차원적" 신경 표상 논쟁(Horikawa 2020 vs 재현 실패 보고)에 새 조건을 준다: **범주 분리도는 자극의 원인 귀속 확실성에 따라 달라질 수 있다.** Emo-FilM에는 Agent(HumanCaused/ChanceCaused) appraisal 연속 평정이 있어 귀속이 애매한 구간에서 anger와 sadness 패턴 분리도가 떨어지는지 검정할 수 있다. 근거: doi:10.1016/j.neubiorev.2022.104977, doi:10.1016/j.isci.2020.101060
3. **장면 affordance 피질과 공포.** Bartnik 2025는 PPA, OPA가 이동 affordance를 과제와 무관하게 표상한다고 보였다. 공포나 불안 비디오에서 "도망칠 경로"나 "접근 가능성" 같은 방어 관련 affordance가 장면 피질에 표상되는지는 정서 연구에서 거의 묻지 않았다. Mobbs 2020의 방어 계산(위협 거리, 시간)과 결합하면 "정서 표상의 일부가 공간 행동 가능성 지도"라는 가설이 된다. 근거: doi:10.1073/pnas.2414005122, doi:10.1016/j.tics.2019.12.016, doi:10.1073/pnas.1618228114
4. **공간 항법의 cognitive map과 영화 서사 속 정서 전이.** Ma & Kragel은 지도 비유를 썼지만 실제 이동(전이)은 넣지 않았다. 영화의 정서 흐름은 서사 구조에 묶인 '경로'이므로, SR의 비대칭성(앞으로의 정서)과 해마 장축의 시간척도 차이(Ma & Kragel Discussion 4번째 단락: 사랑, 만족, 죄책감이 전측 해마에서 더 잘 decoding)가 연결된다. 근거: doi:10.1038/s41467-025-68240-z, doi:10.1073/pnas.1616056114
5. **배선 최소화와 정서의 피질 위치.** Horikawa는 정서 표상이 unimodal-transmodal 경사의 끝에 있다고 했고, Margalit 2024와 Achterberg 2023은 공간과 배선 제약이 기능 지형을 낳는다고 보였다. "정서가 transmodal 끝에 있는 것은 여러 감각을 통합해야 하는 과제가 배선 비용 아래에서 놓일 수밖에 없는 위치이기 때문인가"라는 규범적 질문이 생긴다(검증 비용 큼). 근거: doi:10.1016/j.neuron.2024.04.018, doi:10.1038/s42256-023-00748-9, doi:10.1016/j.isci.2020.101060
6. **항상성 이론의 경계 사례로서 미적 정서.** Keramati & Gutkin의 이론이 다루지 못한다고 밝힌 영역(사회 보상, 새로움)은 Horikawa 34범주의 awe, aesthetic appreciation, entrancement와 겹친다. 측정 생리로 설명되는 정서와 설명되지 않는 정서를 나누는 것이 곧 이 이론의 반증 시험이 된다. 근거: doi:10.7554/eLife.04811

---

## 5. 새 Sub-axis 또는 하위 연구 방향

| # | 제안 | 소속 | 독립 Axis 필요 여부와 이유 |
|---|---|---|---|
| S-1 | **Predictive Affective Maps**: 정서 상태 공간의 SR, TEM, graph vs map 표상, 방향성 전이 | N (K, D와 연결) | N 안에 둔다. 계산 원리(해마 예측 지도)가 핵심 |
| S-2 | **Distributional / Multi-channel Prediction-Error Codes**: 양/음 PE 비대칭 다양성, 조건부 비대칭(cue 일치성) | N (E, O와 연결) | N 안에 둔다 |
| S-3 | **Observer-as-Agent Modeling**: 수동 시청을 world model의 추론으로 모형화, 예측 불확실성(entropy)과 예측오차를 arousal, surprise의 계산 정의로 사용 | N (D, I, J와 연결) | N 안에 둔다. C의 Surprise / Prediction Error와 겹치므로 C는 "내용", N은 "계산 정의"로 역할을 나눌 것을 제안 |
| S-4 | **Structural Priors & Normative Specialization Tests**: connectome(DWI), 지형, 배선 제약 모형과 "왜 특화되는가" 검정(이중 과제, lesion) | N (R과 연결) | N의 Biologically Constrained Learning, Specialized Pathways를 이 이름으로 묶어 재정의 |
| S-5 | **Homeostatic / Interoceptive Control Models**: homeostatic RL, interoceptive active inference, 측정 생리와 보고 생리의 불일치 | N (A의 Interoception과 연결) | N 안에 둔다 |
| S-6 | **Action Readiness & Affordance** (행동 경향, 방어 계산, 장면 affordance) | **새 독립 Axis 후보(Construct 유형, 가칭 Axis U)** | 정서 범주(A)와 경쟁하는 구성개념이고, 지각(B)도 계산(N)도 아니다. P5 조합 규칙상 Construct 유형에 두어야 다른 Axis와 조합하기 쉽다 |
| S-7 | **Portrayed Behavior Ethogram**: 화면 속 행위자 행동의 자동 분할 feature | B (Faces / Body Language 확장) | B 안에 둔다. 외부 분야(Computational Ethology)에서 온 방법 |

---

## 6. Discussion-to-Research chain

형식: Original Finding → Unresolved Question → Technological Development → New Dataset / Model Combination → New Research Question. 각 단계에 근거 ID와 원문 위치를 단다. 겹침은 `reference/existing_projects.md` 기준 표시만 한다.

### Chain 1. 정서 지도는 유사도인가, 미래 정서의 예측인가 (Emo-FilM)

* **Original Finding:** hippocampus는 정서 범주를, vmPFC는 2D affective space와 TEM 층 g를 상대적으로 잘 decoding했다. 저자들은 지도 같은 표상이 사건 전이의 통계 학습에서 올 수 있다고 해석했다. [doi:10.1038/s41467-025-68240-z, Discussion 3, 6번째 단락]
* **Unresolved Question:** (a) 저자 명시: RL 기반 해마 모형이 더 잘 예측하는지 검토 필요 [같은 논문, Discussion Limitations 단락 마지막 두 문장]. graph형과 map형의 관계는 열린 문제 [Discussion 6번째 단락 끝]. (b) 본 에이전트 확인: TEM 환경은 대칭 상관-MDS 격자 위 균등 random walk로 만들어져 실제 전이 방향이 모형에 없다 [같은 논문, Methods "Creating the TEM environment", "Simulating emotional experience"]. (c) 정서 전이는 비대칭이며 유사도로 설명되지 않는다 [doi:10.1073/pnas.1616056114, Discussion 3번째 단락].
* **Technological Development:** successor representation [doi:10.1038/nn.4650], TEM을 경험적 전이 그래프로 재학습 [doi:10.1016/j.cell.2020.10.024], 가치(valence)를 보상으로 둔 SR.
* **New Dataset / Model Combination:** Emo-FilM 1 Hz consensus 평정(discrete 13 + CPM 37)에서 시차 k(예: 2~10 s)의 방향성 전이 행렬을 **학습 영화에서만** 추정(leave-one-film-out). 특징 공간 4종: 대칭 MDS 좌표, TEM(random walk), SR(T), SR(T의 전치). fMRI: 전측/후측 hippocampus, vmPFC, entorhinal. 보조: Horikawa 2,181개 클립의 범주 공동출현으로 만든 대칭 유사도 구조와, 이름 대응 범주에 대한 Emo-FilM SR 기하의 일반화(수준 2 비교).
* **New Research Question:** "영화 시청 중 hippocampal-prefrontal 정서 표상은 정서 간 대칭 유사도가 아니라, 현재 정서에서 앞으로 어떤 정서가 올지에 대한 방향성 예측 구조(SR)를 담는가? 가치를 실은 SR은 vmPFC를 추가로 설명하는가?"
* **핵심 검정 논리:** SR(T)와 SR(T')는 대칭 성분이 같고 방향만 다르다. 뇌가 SR(T)를 SR(T')보다 유의하게 더 잘 따르면 '예측 방향' 증거, 차이가 없으면 Ma & Kragel의 지도는 유사도 구조로 충분히 설명된다(반증 조건).
* **주의:** 전이는 fMRI 참가자 것이 아니라 별도 평정자 consensus이며 평정자 내 z-score 값이다. 14편뿐이라 전이가 서사 특이적일 수 있다(영화 수준 confound). HRF 지연과 시계열 자기상관 보정 필요. Ma & Kragel의 효과 크기가 작아(r 약 0.04~0.10, Stage 1 보고서) 검정력이 걱정된다.
* **G1:** 불필요. **overlap: Emo-FilM 연구** (같은 데이터셋에서 정서 맥락과 시간 정보의 기여를 다룸. 방법은 다름). Stage 1 보고서 5.2 #5가 이 방향을 "Ma & Kragel partially"로 이미 표시했다.
* (Stage 2 재점검 반영) 가장 가까운 신경 선행은 Thornton, Weaverdyck, Tamir (2019, doi:10.1523/JNEUROSCI.1431-18.2018)다. 정신상태를 생각하는 과제에서 현재 상태의 패턴이 가능성 높은 미래 상태 패턴을 닮았다(mPFC 중심). Chain 1은 이 결과를 출발점으로 삼고, 새로움은 (a) 영화 정서 동역학에서 추정한 전이, (b) 해마 SR과 TEM의 비교, (c) SR(T) 대 SR(T')의 방향성 검정으로 한정한다. Thornton 2019가 대칭 유사도를 통제했는지는 초록으로 확인하지 못했으므로 Round 2 전에 본문을 확인해야 한다. 재검색(arXiv, Crossref, WebSearch)에서 SR이나 RL 모형으로 해마-vmPFC 정서 표상을 예측한 연구는 여전히 찾지 못했다.

### Chain 2. 정서 범주인가, 행동 경향인가 (Emo-FilM, Horikawa)

* **Original Finding:** 정서 범주 모형이 transmodal 영역 반응을 시각, 의미 모형보다 잘 설명했다. [doi:10.1016/j.isci.2020.101060, Discussion 1, 5번째 단락]
* **Unresolved Question:** 저자들은 이 시스템이 "emotional experience (or affordances)"를 부호화하며 정서가 반응 결정 전 적응 행동을 준비시킨다고 해석했지만 검증하지 않았다 [같은 논문, Discussion 2번째 단락 마지막 두 문장]. 1인칭 경험과 3인칭 예측의 혼재도 한계로 남겼다 [Limitations 둘째 단락]. 장면 affordance 연구는 DNN이 affordance보다 물체에 정렬되며 embodied AI, VLA 모형 비교가 필요하다고 했다 [doi:10.1073/pnas.2414005122, Discussion 7번째 단락, 마지막에서 둘째 단락].
* **Technological Development:** action-conditioned world model(V-JEPA 2, arXiv:2506.09985, 세부 미확인), MLLM 기반 행동 경향 주석(AI 추정 라벨), 정서의 RL 계산 계열 분류 [doi:10.1016/j.neubiorev.2022.104977].
* **New Dataset / Model Combination:** (1) Emo-FilM 안에서 banded ridge encoding: band A = discrete 13, band B = Motivation 10(행동 경향), band C = Appraisal 10, nuisance = 시청각-의미 feature. (2) Horikawa: 34범주 vs 행동 경향 주석(인간 또는 MLLM) vs 14차원 중 Approach, Control, Effort. 변량 분할과 RSA.
* **New Research Question:** "정서 범주 모형이 설명하는 transmodal 분산 중 얼마가 행동 경향(action readiness) 모형으로 대체되며, 범주 고유 분산은 남는가?"
* **결과 해석:** 행동 경향 band가 범주 band의 분산 대부분을 흡수하면 Horikawa의 '정서 경험' 해석보다 'affordance' 해석이 유리하다. 범주 고유 분산이 크게 남으면 범주가 행동 준비로 환원되지 않는다. 두 결과 모두 정서 이론(기능주의적 action readiness vs 범주적 느낌)에 정보를 준다.
* **주의:** 같은 평정자 집단이 두 종류 항목을 평정하면 공선성이 크다(Emo-FilM은 항목별로 평정자 블록이 다른지 확인 필요). MLLM 주석은 AI 추정이다. Horikawa 라벨은 별도 평정자 규범 평정이다.
* **G1:** Emo-FilM 분석은 불필요, Horikawa 신규 주석은 필요. **overlap: EmoViS** (affective geometry의 기원을 묻는다는 점에서 부분), **Emo-FilM 연구** (같은 데이터셋, 부분).
* (Stage 2 재점검 반영) 선행 수행 판정을 no에서 partially로 바꾸었다. component 모형 fMRI(Mohammadi et al. 2023, doi:10.1093/cercor/bhad093; Leitão et al. 2020, doi:10.1371/journal.pbio.3000900)가 approach/avoidance 경향과 motivation 성분의 뇌 네트워크를 이미 보고했다. 따라서 Chain 2의 새로움은 "행동 경향의 신경 표상 발견"이 아니라 "34범주 또는 13개 이산 정서 band가 행동 경향 band로 얼마나 대체되는가"라는 경쟁 검정이다. Morgenroth et al. (2026, doi:10.1037/emo0001619)이 Emo-FilM 평정에서 이산 정서가 component로 잘 예측된다고 보고했으므로, 파일럿 첫 단계는 두 band의 평정 수준 공선성(예: 교차 예측 R²)부터 계산해 분산 분할이 가능한지 판단하는 것이다.

### Chain 3. 피질하 경로가 싣는 정서 정보의 내용 (Horikawa)

* **Original Finding:** 상구-pulvinar-편도체 경로가 불쾌 자극의 혐오성을 추적하고, 편도체 연결은 low road, high road, 개념적 top-down 3성분으로 나뉜다 [doi:10.1016/j.neuron.2021.06.001, Results/Discussion 통합 서술 후반]. DNN에서 초기 시각층 shortcut이 정서 조건화에 필요했다 [arXiv:2607.19327, Discussion 2번째 단락 끝].
* **Unresolved Question:** 경로와 주관적 정서 경험의 관계는 추가 연구 필요, 이미지의 자기보고 mediation은 유의하지 않았다 [doi:10.1016/j.neuron.2021.06.001, 후반 단락]. DNN 모형은 recurrence와 feedback이 없다 [arXiv:2607.19327, limitations 단락]. 재귀 feedback 모형과 뇌 반응의 통합이 필요하다 [doi:10.1126/sciadv.aaw4358, Discussion 7번째 단락]. 경로가 공간주파수와 무관하다는 반대 보고도 있다 [doi:10.1523/JNEUROSCI.3525-16.2017, WebSearch 요약 수준].
* **Technological Development:** MPathI, DNN 층 분할(얕은 층 / 저공간주파수 필터 / 깊은 층), recurrent 시각 모형 [doi:10.1073/pnas.1905544116].
* **New Dataset / Model Combination:** Horikawa 2,181개 비디오의 단일 시행 블록 반응(HCP360 + 피질하 ROI). 2,181개 시행 간 공분산으로 MPathI 경로 패턴 추정. 경로 패턴을 (a) 얕은 층 feature, (b) 저공간주파수 프레임 feature, (c) 깊은 층 feature, (d) 34범주 라벨로 encoding. Emo-FilM과 Spacetop alignvideo로 소리 있는 자극 재현.
* **New Research Question:** "34개 정서 범주 비디오에서 상구-pulvinar-편도체 경로 패턴은 혐오성 단일 축만 싣는가, 범주 특이 정보를 싣는가? 그 정보는 얕은 층(또는 저공간주파수) feature로 충분히 설명되는가?"
* **반증 조건:** 경로 정보가 깊은 층 feature로 모두 설명되고 얕은 feature가 고유 분산을 더하지 못하면, '조잡한 shortcut' 가설은 표상 내용 수준에서 지지되지 않는다(latency 가설은 이 데이터로 판단 불가).
* **주의:** 3T 2 mm에서 상구, pulvinar는 부분 용적 문제가 크다(Kragel 2021은 3T에서도 다변량 접근으로 식별 가능하다고 보고). Horikawa 전처리본은 피험자 native 공간이므로 ROI를 피험자별로 정의한다. EmoNet은 Horikawa와 같은 자극 원천으로 학습되었으므로 사용 금지 또는 누수 명시. Horikawa는 무음이다.
* **G1:** 필요. **overlap: EmoViS** (sensory-semantic 기원과 부분).
* (Stage 2 재점검 반영) Jang & Kragel (2025, doi:10.1523/JNEUROSCI.1436-24.2025)이 영화 시청 fMRI에서 편도체 하위영역의 DNN encoding 모형을 이미 만들었다. Chain 3은 이 모형을 baseline으로 쓰고, 새로움을 경로(MPathI) 수준과 얕은 층 대 깊은 층 feature 비교로 한정한다. 경로와 주관적 경험의 관계에 대한 Kragel 2021 future direction은 검증 가능한 후속을 찾지 못해 no로 바꾸었다.

### Chain 4. Confirmation-biased learning의 신경 구현 (Spacetop social)

* **Original Finding:** 통증, vicarious pain, 인지 노력 모두에서 cue와 일치하는 PE에 더 크게 학습하는 confirmation bias와 직전 지각의 carryover [doi:10.1073/pnas.2513856123, Abstract, Discussion 1, 2번째 단락].
* **Unresolved Question:** 표준 Bayesian predictive coding은 일치/불일치 비대칭을 포착하지 못하며, 기계적 후보는 양/음 강화별 뉴런 하위집단 또는 metaplasticity [같은 논문, Discussion predictive processing 단락]. 기대가 수정하는 통증 처리 단계와 기분의 역할은 미해결 [doi:10.1038/s41562-018-0455-8, Discussion 후반]. 비대칭 다양성의 회로 기제와 기분 연결 [doi:10.1038/s41586-019-1924-6, 마지막 두 단락].
* **Technological Development:** distributional TD [doi:10.1038/s41586-019-1924-6], 비대칭 PE 신경 분석 [doi:10.1073/pnas.2500815122], 전측 insula 비대칭 pain PE 모형 비교 [doi:10.7554/eLife.24770].
* **New Dataset / Model Combination:** Spacetop social(세션당 pain, vicarious, cognitive 각 2 run, run당 12 trial, cue 1 s, 기대 평정 4 s, 자극 5 s, 결과 평정 4 s, TR 0.46 s; `dataset_Spacetop.md`). Yazdanpanah 최적 모형으로 trial별 PE를 구하고 전측 insula, 선조체, vmPFC, dACC에서 voxel별 양/음 PE 기울기를 추정.
* **New Research Question:** "cue와 일치하는 증거를 더 크게 반영하는 학습 편향은 (a) cue 일치성이 PE 신호의 gain을 바꾸는 단일 채널 기제인가, (b) 비대칭이 서로 다른 voxel 채널 집단의 읽기 문제인가? 그 구현은 pain, vicarious pain, cognitive effort에서 공유되는가?"
* **분석:** (a) ROI 평균에서 PE 부호 x cue 일치성 상호작용. (b) voxel 비대칭의 이질성이 세션 간 split-half로 안정적인지, 비대칭과 '중립점'의 상관(Dabney 예측의 voxel 이전), 과제 간 voxel 비대칭 순서의 보존.
* **반증 조건:** voxel 비대칭 이질성이 신뢰할 만하지 않으면 (b)는 지지되지 않는다. 일치성 gain 효과도 없으면 행동 편향은 PE 부호화가 아니라 판단, 보고 단계에서 생긴다는 해석(Jepma 2018 Discussion이 언급한 후기 단계 효과)이 남는다.
* **주의:** voxel은 뉴런이 아니므로 (b)가 지지되어도 distributional code를 확증하지는 못한다(이론적으로 가능하지만 fMRI로 구분할 수 없는 설명). cue는 기만 설계이고, 명시적 기대 평정 자체가 기대 지속을 만들 수 있다(Jepma 2018). 조건별 learning rate의 개인 수준 신뢰도가 낮다(Yazdanpanah Discussion 5번째 단락).
* **G1:** 불필요(events.tsv + fMRI). **overlap: 없음.**
* (Stage 2 재점검 반영) 비교 모형에 HGF 계열 동적 precision 모형(Drusko et al. 2023, doi:10.1038/s41598-023-29758-8)을 추가한다. Yazdanpanah 2026이 표준 predictive coding으로는 비대칭을 설명하지 못한다고 한 주장을 같은 데이터로 직접 검정하는 비교군이다. distributional 부호의 근거는 ACC(Muller et al. 2024)와 도파민 다차원 지도(Sousa et al. 2025)로 넓어졌지만 모두 단일 뉴런 기록이라, fMRI voxel 수준 해석의 한계는 그대로다.

### Chain 5. 정서 계산 이론의 인간 데이터 benchmark (Spacetop social, narratives; Emo-FilM)

* **Original Finding:** valence = 행동모형 precision 갱신(affective charge) [doi:10.1162/neco_a_01341, Discussion 첫 단락], arousal = 사후 신념 entropy, valence = utility - expected utility [arXiv:2407.02474, Abstract, Discussion], 연속 상태 운전 모형에서 미래 결과까지 조건화한 정서 신호 [arXiv:2608.07480, Discussion].
* **Unresolved Question:** 신경영상/행동 패러다임 적합과 RL 비교, trial별 AC와 valence 측정 및 신경 상관물의 대응 [doi:10.1162/neco_a_01341, Future Empirical Directions 1, 2번째 단락]. 인간 데이터 미비교 [arXiv:2407.02474 Discussion; arXiv:2608.07480 Discussion limitations 둘째]. valence가 단기 PE만 반영하므로 다중 시간척도 모형 필요 [arXiv:2608.07480, limitations 첫째]. 정서 동역학은 인간 데이터로 검증해야 함 [doi:10.1007/s10994-017-5666-0, Discussion].
* **Technological Development:** pymdp(arXiv:2201.03904), HBI 모형 비교(Yazdanpanah가 사용), video world model 예측 분산(arXiv:2305.11772의 latent 미래 예측 논리).
* **New Dataset / Model Combination:** (A) Spacetop social: trial별 기대, 결과 평정으로 RL(Yazdanpanah 최적 모형), Bayesian 모형, affective-inference 모형을 적합하고 결과 평정과 전측 insula, vmPFC 신호의 out-of-sample 예측으로 비교. (B) Spacetop narratives: clip마다 "지금 느낌"과 "다음 전개 기대" 2D 평정이 있다(`dataset_Spacetop.md` 181행). 직전 기대와 현재 느낌의 차이(단기 PE)와 이야기 초반부터 누적된 기대 불일치(장기)를 분리. (C) Emo-FilM: video world model 예측 분산을 Predictable, Suddenly, Alert 평정과 참가자 EDA에 대응.
* **New Research Question:** "정서 valence와 arousal은 결과 예측오차(RL)인가, 생성모형의 precision 갱신과 예측 불확실성(active inference)인가? 이야기 속 느낌은 단기 PE와 장기 기대 불일치 중 무엇으로 더 잘 예측되며, 그 계산 변수가 vmPFC/insula 반응을 설명하는가?"
* **반증 조건:** affective-inference 모형이 RL보다 out-of-sample 행동, 신경 예측에서 낫지 않으면 이 패러다임에서는 추가 설명력이 없다.
* **주의:** Hesp 등 스스로 보상 과제에서는 precision 변화가 RPE처럼 보인다고 적었다(Discussion 중반). 두 모형이 갈라지는 조건(contingency 변화, 불확실성 조작)이 데이터에 충분한지 모형 회복(model recovery)으로 먼저 확인해야 한다. (C)의 world model 불확실성은 인간의 것이 아니라 AI 모형의 것이고, 평정자(별도)와 EDA(참가자)의 주체가 다르다.
* **G1:** (A), (B) 평정 기반은 불필요. (C)는 필요. **overlap:** (C)는 **EmoBrain** (V-JEPA2 사용, 방법 일부)과 **Emo-FilM 연구** (부분).

### Chain 6. 정서 전용 하위체계는 최적화에서 생기는가 (Horikawa, NSD)

* **Original Finding:** 물체 학습 CNN에 정서 선택 unit이 창발하고 lesion하면 정서 인식이 떨어진다 [doi:10.1371/journal.pcbi.1011943, Discussion 첫 단락]. 다중 과제 최적화는 얼굴/물체 하위체계 분리를 낳는다 [doi:10.1126/sciadv.abl8913, Discussion 첫 단락]. 정서 schema는 시각피질에 내재 [doi:10.1126/sciadv.aaw4358, Discussion].
* **Unresolved Question:** 세분화된 정서 미검토, 신경 기록 비교 없음(신경적 관련성 추측적) [doi:10.1371/journal.pcbi.1011943, Limitations]. 어떤 기능이 특화될지, 과제 특이 inductive bias의 역할 [doi:10.1126/sciadv.abl8913, Discussion 4번째 단락]. MoE 해독은 시각 ROI만 [arXiv:2505.15946, Appendix Limitations].
* **Technological Development:** 이중 과제 학습과 lesion, 네트워크 사전지식 MoE [arXiv:2505.15946, arXiv:2605.19279].
* **New Dataset / Model Combination:** 정서 학습 데이터는 Cowen & Keltner 자극과 독립이어야 한다(EmoNet 누수 사례, 적합한 공개 정서 이미지/비디오 데이터셋은 이번 라운드에서 미확인). 신경 평가는 Horikawa 34범주. 시각 표상 사전학습과 비교 기준은 NSD.
* **New Research Question:** "물체 + 정서 이중 과제 최적화는 정서 하위체계의 분리를 낳는가? 분리된 정서 unit은 Horikawa에서 시각피질보다 transmodal 영역 반응을 더 잘 예측하는가, lesion 시 transmodal 설명량이 선택적으로 줄어드는가?"
* **결과 해석:** 분리가 없거나 분리 unit이 시각피질만 예측하면, 정서 정보는 공유 시각 표상의 읽기 결과라는 '시각 내재' 견해(Kragel 2019, Liu 2024)가 유리하다. 분리 unit이 transmodal을 선택적으로 예측하면 전용 경로 가설이 유리하다. 단 망의 분리가 뇌의 필연성을 뜻하지는 않는다(Dobs의 음식 사례).
* **주의:** Horikawa는 반복 제시가 없어 noise ceiling이 없다. 정확도 경쟁이 아니라 lesion에 따른 영역별 설명량 변화가 결과 지표다.
* **G1:** 필요. **overlap: EmoBrain** (34차원 profile을 다루는 경우 부분), **EmoViS** (부분).
* (Stage 2 재점검 반영) Liu 2024의 "신경 기록 비교 없음" 한계에는 후속이 있다: 같은 연구군의 VCA 모형(Liu et al. 2025, bioRxiv, doi:10.1101/2025.10.20.683439)이 편도체 fMRI와 비교되었고, Jang & Kragel 2025가 편도체 DNN encoding을 했다. 다만 둘 다 이중 과제에 따른 분리 여부나 lesion에 따른 영역별 설명량 변화는 다루지 않았다(초록 기준). Dobs 2022의 inductive bias 질문은 항법 RL agent에서 부분적으로 다뤄졌다(Zhang, Pitkow, Angelaki 2022, bioRxiv, doi:10.1101/2022.12.07.519515). 정서 과제 적용은 찾지 못했다.

### Chain 7. 영화 속 정서 momentum (Emo-FilM)

* **Original Finding:** 기분은 보상 변화의 momentum을 표상한다 [doi:10.1016/j.tics.2015.07.010, Concluding Remarks]. 기분은 각 정서 계산의 누적이다 [doi:10.1016/j.neubiorev.2022.104977, 'Emotional state as cumulative' 절들].
* **Unresolved Question:** 기분이 뇌에서 어떻게 표상되는지, 기분과 짧은 정서의 상호작용 [doi:10.1016/j.tics.2015.07.010, Outstanding Questions 1, 2]. 기대, 기분, 정동 학습의 상호작용 [doi:10.1038/s41562-018-0455-8, Discussion 후반]. 장기 기대 불일치 [arXiv:2608.07480, limitations 첫째].
* **Technological Development:** momentum Kalman filter(Eldar 2016 Box 2), leaky integrator, 다중 시간척도 모형.
* **New Dataset / Model Combination:** Emo-FilM의 Good/Bad, Calm, AtEase와 discrete 항목 1 Hz 평정으로 정서 수준, 변화(PE 대리), momentum 시계열을 만들고, vmPFC, 복측 선조체, DMN의 느린 상태와 참가자 생리(HR, EDA)에 대응.
* **New Research Question:** "영화 안의 느린 뇌 상태는 현재 정서 수준이 아니라 정서 변화의 누적(momentum)을 추적하는가?"
* **진단 구간:** momentum은 "아직 나쁘지만 나아지는" 구간에서 긍정 상태를, 수준 모형은 부정 상태를 예측한다. 이런 구간이 14편에 충분히 있는지부터 센다(파일럿).
* **반증 조건:** 진단 구간에서 수준 모형이나 단순 leaky integrator가 momentum만큼 맞으면 momentum 가설은 지지되지 않는다.
* **주의:** 평정은 별도 평정자의 z-score 상대값이다. 느린 상태는 스캐너 drift, 영화 수준 교란과 섞인다. 생리는 fMRI 참가자, 평정은 별도 평정자라 주체가 다르다.
* **G1:** 불필요. **overlap: Emo-FilM 연구** (부분).

---

## 7. 담당 Axis N 확장 제안

| 구분 | 현재 Sub-axis | 제안 | 이유와 근거 |
|---|---|---|---|
| 추가 | (없음) | Predictive Affective Maps (SR, TEM, graph vs map) | Ma & Kragel 2026의 미해결 문제와 방법적 간극(대칭 random walk) |
| 추가 | (없음) | Distributional / Multi-channel PE Codes | Yazdanpanah 2026, Dabney 2020, Lin 2025 |
| 추가 | (없음) | Observer-as-Agent Modeling (수동 시청의 world model 추론) | Pattisapu 2024, Schumann 2026, Nayebi 2023. C의 Surprise와 역할 분담 |
| 추가 | (없음) | Homeostatic / Interoceptive Control Models | Keramati 2014, Petzschner 2021, Yoshida 2024 |
| 재정의 | Biologically Constrained Learning, Specialized Pathways, Neural Routing | Structural Priors & Normative Specialization Tests 로 묶고, 하위에 connectome/DWI 제약, 지형/배선 제약, 이중 과제 분리, MoE routing, 다중 경로(low road, shortcut)를 둔다 | Lappalainen 2024, Margalit 2024, Achterberg 2023, Dobs 2022, MoRE-Brain 2025, Kragel 2021, Leem 2026 |
| 분할 | Emotion as Computational Value / Salience | (a) Value-based Emotion Taxonomy(가치 변화, 행동 평가, 예측의 계산 계열) (b) Precision / Uncertainty as Affect(active inference) | Emanuel & Eldar 2023, Hesp 2021. 두 전통은 같은 데이터에서 경쟁 가설을 낸다(Chain 5) |
| 유지(우선순위 하향) | Neuromorphic Systems | 유지하되 "fMRI 데이터와 직접 연결 불가, 시간 대비(event) feature 원천 정도로만 사용"으로 표시 | Roy 2019, Kasabov 2026. 현 SNN 정서 연구는 표현 정서 분류 정확도 중심 |
| 유지 | Predictive Coding, Active Inference, Hierarchical Processing, Recurrent Computation | 유지. Recurrent Computation은 Kragel 2019, Leem 2026이 공통으로 든 한계라 정서 특이 검정(Chain 3)과 연결 | doi:10.1073/pnas.1905544116 |
| 이관 제안 | (외부 분야) Embodied Cognition / Affordances, Ecological Psychology | 새 독립 Axis 후보 **U: Action Readiness & Affordance (Construct 유형)** | Horikawa 2020 Discussion, Bartnik 2025, Emo-FilM Motivation 항목 |
| 이관 제안 | (외부 분야) Computational Ethology | B의 하위 "Portrayed Behavior Ethogram"으로 (방법은 외부 분야 유래 표시 유지) | Mobbs 2021, Dima 2022 |

양방향 질문(위임 지시의 핵심 방향)에 대한 현재 답:
* **뇌 → AI 구조 제약:** 구조 제약을 넣었을 때 기능이 달라진 확인된 사례는 Leem 2026(shortcut 없으면 조건화 실패), Dobs 2022(이중 과제의 자발적 분리), Lappalainen 2024(connectome으로 파라미터 감소와 개별 뉴런 예측)다. 정서 영역에서 이 효과를 **인간 fMRI로 검증한 사례는 찾지 못했다.**
* **AI 구조 → 새 Neuroscience 질문:** SR의 방향성(T vs T')이 '정서 지도'의 성격을 가르는 검정을 만들고(Chain 1), distributional RL이 confirmation bias의 구현 형식을 묻게 하며(Chain 4), active inference가 valence/arousal의 계산 정의를 경쟁시키고(Chain 5), 이중 과제 분리가 '정서 전용 경로의 필요성'을 규범적으로 묻게 한다(Chain 6).

---

## 8. 과학적 안전장치 (CLAUDE.md 6절 대응)

* **경험 vs 묘사 정서:** Horikawa와 Emo-FilM 라벨은 별도 평정자의 1인칭 보고 규범 평정이다. Chain 1, 2, 7의 '전이', '행동 경향', 'momentum'은 모두 평정자 consensus의 속성이며 fMRI 참가자 본인의 경험이 아니다. Chain 7의 생리만 참가자 측정값이다. Spacetop social만 참가자 본인 trial 평정이다.
* **인간 주석 vs 모형 생성 주석:** MLLM 행동 경향 주석, world model 불확실성, pose ethogram은 모두 AI 추정 feature로 표기한다.
* **사전학습 오염과 누수:** EmoNet은 Cowen & Keltner 비디오 프레임으로 학습되었으므로(Kragel 2019 Methods 원문) Horikawa 분석에 쓰면 누수다. V-JEPA 계열 등 웹 규모 사전학습 모형의 Horikawa 자극 포함 여부는 미확인이다.
* **Decodability vs representation vs causality:** lesion은 모형 안의 인과 조작이지 뇌의 인과 증거가 아니다(Chain 6). SR, AC, distributional 변수와 BOLD의 상관은 '그 계산과 양립 가능함'까지만 말한다.
* **이론적으로 가능하지만 관찰 데이터로 구분할 수 없는 설명:** (1) fMRI로 '빠른 경로'의 latency는 판단 불가(Chain 3). (2) voxel 비대칭 이질성이 distributional code인지 voxel 내 혼합의 산물인지 구분 불가(Chain 4). (3) 보상 과제에서 precision 갱신과 RPE는 수학적으로 비슷하게 보일 수 있다(Hesp 2021 Discussion, Chain 5).
* **HRF, 자기상관:** Emo-FilM 1 Hz 평정과 TR 1.3 s, Spacetop TR 0.46 s의 시간 정렬에 HRF 지연 모형과 자기상관 보정 필수. 방향성 전이(Chain 1)는 HRF 지연 차이에 특히 민감하므로 평정 시계열 자체에서 추정하고 BOLD에서는 추정하지 않는다.
* **Leakage:** Emo-FilM 전이 통계와 momentum 파라미터는 학습 영화에서만 추정(leave-one-film-out). Spacetop 모형 파라미터는 세션 단위 교차검증.
* **ROI 순환:** 상구, pulvinar, 편도체, insula ROI는 해부학적 또는 독립 데이터로 정의.
* **다중 비교:** voxel 수준 비대칭 분석은 ROI 제한 + permutation.

---

## 9. 이번 라운드의 미확인 사항

1. EmoPathway의 실재와 출처 (사용자 확인 필요).
2. AAAI dual-pathway 얼굴 정서 모형의 서지 (ojs.aaai.org 차단).
3. 코드와 가중치 라이선스 대부분(pymdp, V-JEPA 2, ViTPose는 검색 수준. TEM, MPathI, EmoNet, MoRE-Brain, TDANN, Leem 2026 코드는 미확인).
4. Ma & Kragel 2026의 코드 공개 여부, Supplementary(시간 단계별 결과).
5. Emo-FilM에서 Motivation 항목과 discrete 항목을 같은 평정자가 평정했는지(공선성 판단에 필요).
6. Chain 6에 쓸, Cowen & Keltner와 독립인 공개 정서 학습 데이터셋.
7. Spacetop narratives 평정의 결측률과 clip 수(`dataset_Spacetop.md`에 구조만 있음).
8. Yoshida 2024 Neural Networks 논문 본문(제목, 저자만 확인), Stachenfeld 2017, Whittington 2020 등 `discussion_read: "no"` 14편의 본문.
9. Chain 1의 선행 수행 여부는 arXiv와 PubMed 검색 기준이며 bioRxiv 최신 preprint는 빈도 제한으로 충분히 검색하지 못했다.
10. (Stage 2 재점검 반영) 재점검에서 근거로 추가한 6편은 초록만 확인했다. 특히 Thornton et al. 2019의 대칭 유사도 통제 여부, Mohammadi et al. 2023의 component별 네트워크가 정서 범주 모형과 비교되었는지, Jang & Kragel 2025의 편도체 하위영역 결과는 본문 확인이 필요하다.
11. (Stage 2 재점검 반영) Onat & Büchel 2015(CS-US 패턴 유사성)는 WebSearch로 본 리뷰 요약에만 근거한 partially 판정이다. Horikawa raw BIDS 촬영 범위에 안구가 포함되는지(DeepMReye 적용 조건)도 미확인이다.
