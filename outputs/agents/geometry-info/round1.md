# Round 1 (Independent Discovery): geometry-info

* 작성: geometry-info (Agent 7, Geometry, Manifolds & Information Theory)
* 기준일: 2026-11-12 / Stage 2, Round 1 / 절차: `reference/protocols.md` P1
* 담당: Axis K (Geometry & Mathematical Structure), Axis O (Individual & Population Variation), 외부 분야 Information-theoretic Neuroscience, Complex Systems
* 읽은 입력: `CLAUDE.md`, `reference/protocols.md`(P1), `reference/axes.md`, `reference/starting_papers.md`, `reference/existing_projects.md`, `outputs/stage1/dataset_intelligence_report.md`, `outputs/stage1/gate_decision.md`, `outputs/STAGE_STATUS.md`(사용자 결정 기록), `outputs/stage1/dataset_EmoFilM.md` 8절, `outputs/stage1/dataset_Horikawa.md`(재분석 목록 부분)
* 독립성: 다른 에이전트 폴더(`outputs/agents/<다른 이름>/`)는 읽지 않았다.
* 문헌: `literature.jsonl` 45편. 전부 식별자 경로로 존재 확인(`verified_by` 기준 Crossref 35, arXiv 7, PubMed 1, 학회 proceedings 2. 일부는 PubMed로도 중복 확인). 2024~2026년 11편, Affective Neuroscience 밖 분야 18편 이상. 본문(Discussion/Limitations) 직접 확인 23편, 초록만 22편. `search_index` 표기 항목 없음.
* 표기: [본문]은 논문 본문 직접 확인, [초록]은 초록만 확인, [판단]은 본 에이전트의 해석. G1은 원본 자극 필요 여부(사용자 확인으로 4개 데이터셋 모두 보유). `overlap:`은 `reference/existing_projects.md` 기준 표시만 한다.

---

## 0. 특별 지시 결과

### 0.1 Kragel 연구실 2026 연구: 서지 확정과 "이미 다룬 것 / 남긴 것"

**서지 (Crossref로 확인, 본문 직접 읽음):**
* 주 논문: Ma Y, Kragel PA (2026). Map-like representations of emotion knowledge in hippocampal-prefrontal systems. *Nature Communications* 17:1518. doi:10.1038/s41467-025-68240-z. 출판일 2026-01-26. PMC12891686 전문으로 Results, Discussion, Methods 확인.
* 이전 판: bioRxiv doi:10.1101/2025.06.03.657722 (Crossref로 존재 확인, 2025-06-06 게시, 본문 미열람).
* 같은 연구실 후속: Ma Y, Kragel PA (2026). Emotion knowledge is structured in a grid-like coordinate system in the human ventromedial prefrontal cortex. *PLOS Biology* 24:e3003795. doi:10.1371/journal.pbio.3003795 (Crossref 확인, PMC13739216 Discussion 확인). Emo-FilM이 아니라 얼굴 morph와 문구 과제를 썼다.
* 같은 연구실 가설 리뷰: Ma Y, Vafaie N, Kragel PA (2025). Embedding emotion concepts in cognitive maps. *Neuroscience & Biobehavioral Reviews* 172:106089. doi:10.1016/j.neubiorev.2025.106089 (Crossref 확인, 본문 미열람이라 jsonl에 넣지 않음).
* Emo-FilM을 쓴 인접 기준점: Zaffina L, ..., Petri G, Van De Ville D (2026). Higher-order topology uncovers the multidimensional dynamics of naturalistic emotion. bioRxiv doi:10.64898/2026.09.26.754452. Stage 1에서 "미검증"이었으나 이번에 **Crossref로 DOI와 저자 8명을 확인했고 bioRxiv 전문을 읽었다.** 동료심사 전 preprint다.

**이미 다룬 것 (Nat Commun 본문 기준):**

| 항목 | 내용 |
|---|---|
| 데이터 | Emo-FilM 29명(S07 제외), 14편 중 13편 학습 1편 시험(leave-one-film-out), FSL 제공 전처리본 |
| 라벨 | 별도 평정자 consensus 중 discrete 13개 + Feeling 4개(Good, Bad = valence; Calm, AtEase = arousal). 나머지 33개 성분 항목 미사용 |
| 공간 | 13개 범주 평정 시계열 상관(1-r)에 metric MDS → 2D affective space. 평정 시계열을 이 공간에 투영한 궤적 |
| decoding | ROI별(hippocampus 전후, entorhinal, vmPFC, amygdala) 참가자별 PLS(20 components), HRF convolution, 선형 혼합모형. searchlight는 보충 |
| 핵심 결과 | hippocampus: 범주 > 2D (r 0.0525 vs 0.0428). vmPFC: 2D > 범주 (0.0956 vs 0.0838). 이중 해리. 후측 hippocampus가 세밀한 범주에 유리. amygdala는 전측 hippocampus와 비슷 |
| 기하 | 참가자별 decoder 출력의 범주 간 상관 구조가 참가자 간 일관(Spearman 0.978), valence-only 모형(0.842)보다 full 모형이 우수 |
| 계산 모형 | TEM을 11x11 격자(무작위 one-hot 감각, 5개 행동 균등 확률)로 학습 후 MDS 격자 환경에서 무작위 보행. layer p는 hippocampus 소척도, layer g는 vmPFC 대척도에서 잘 decoding. entorhinal 약함 |
| PLOS Biol | 통제 과제에서 vmPFC hexadirectional(grid-like) 변조, 양식 간 일반화, 거리 신호가 trial별 판단 예측 |

**남긴 것 (저자 Discussion이 명시한 것 + 본 에이전트가 기하 관점에서 본 공백):**

| # | 남은 공백 | 출처 | 우리 쪽 연결 |
|---|---|---|---|
| R1 | valence-arousal 외 차원(effort, certainty, situational control)의 지도 구조 | Nat Commun Discussion 9째 단락 [본문] | Emo-FilM appraisal 항목(Predictable, Controlled, Urgency 등) 사용. Zaffina 2026이 50항목 전체를 썼으나 지도 형식 검증은 아님(partially) |
| R2 | TEM 외 RL 계열 모형 비교 | Nat Commun Discussion 9째 단락 [본문] | Chain C2 (successor representation) |
| R3 | 정서 개념이 공유 통계 규칙인가, 개인 경험으로 구성된 ad hoc 범주인가 | Nat Commun Discussion 2째 단락 [본문] | Chain C1, C3, C8 |
| R4 | graph형과 map형 표상의 관계 | Nat Commun Discussion 6째 단락 [본문] | Chain C2 (전이 그래프 기반 SR vs 연속 지도) |
| R5 | 개인 특이적 grid-like code, 개인 affect dynamics가 hexagonal 변조 개인차를 낳는지 | PLOS Biol Discussion 3째 단락 [본문] | 0.2절, Chain C2, C4 |
| R6 | 거리 척도(Euclidean vs cityblock) 구분 | PLOS Biol Discussion 4째 단락 [본문] | 5절 S5 (metric 선택 sub-axis) |
| R7 | **TEM이 실제 정서 전이 통계를 학습하지 않았다.** 균등 무작위 보행이라 "전이 통계 학습" 주장은 가정 상태 | Nat Commun Methods [본문] + [판단] | Chain C2 |
| R8 | **참가자 간 0.978은 신경 패턴 기하가 아니라 decoder 출력 기하다.** 모든 참가자의 decoder가 같은 consensus 표적으로 학습되어 출력 상관 구조가 표적 상관 구조를 물려받을 수 있다. 신경 패턴 자체의 개인 간 공유는 검정되지 않았다 | Nat Commun Methods "representational geometry" 절 [본문] + [판단] | 1절 P5, Chain C1 |
| R9 | 명시적 시청각-의미 nuisance 모형 없이 cross-film 일반화로 추상성을 주장 | Nat Commun Discussion 2째, 7째 단락 [본문] + [판단] | 다른 에이전트(vision-decoding, encoding-foundation) 영역과 결합 필요 |
| R10 | 자연주의 데이터에서의 hexadirectional 검정, Horikawa, Spacetop으로의 일반화 | 두 논문 범위 밖 [판단] | Chain C2, 3절 I3 |
| R11 | 영화 사이 90초 washout의 이완 동역학, 참가자 생리(EDA, PPG)와의 결합 | 두 논문 범위 밖 [판단] | Chain C4, C5 |

판정: "Emo-FilM + hippocampus/vmPFC + 2D 지도 + TEM" 조합은 **이미 수행됨**. "Emo-FilM + 고차 위상 + 50항목 + 집단 평균"도 **이미 수행됨(preprint)**. 남은 것은 위 R1~R11이다.

### 0.2 피험자 수 조건에 따른 개인차 질문의 구분

원칙: 개인차 질문은 (가) 개인 내(idiographic) 구조, (나) 개인 쌍 사이 구조, (다) 모집단 수준 형질 연관으로 나뉜다. (다)는 Marek et al. 2022(doi:10.1038/s41586-022-04492-9)[초록]가 보였듯 수천 명 규모에서야 재현성이 생기므로, **우리 4개 데이터셋 어디에서도 형질-뇌 상관은 확증 목적으로 쓰지 않는다.** 대신 피험자 수가 적으면 (가)를 깊게, 많으면 (가)의 분포와 (나)를 넓게 본다.

| 데이터셋 | 피험자 / 1인당 자료 | 라벨 주체 | 가능한 개인차 질문 | 불가능하거나 약한 질문 | 통계 단위와 주의 |
|---|---|---|---|---|---|
| **Horikawa** | 5명 / 2,181 고유 자극, 61 run, 반복 없음, 같은 순서 | 별도 평정자 집단 평균 | (1) 피험자별 정서 기하와 차원 스펙트럼. (2) 피험자 쌍(10쌍) 사이 cross-decomposition으로 rank별 공유 vs 고유 분산. (3) 개인 고유 편차가 **독립 자극 절반에서 재현되는가**(Westlin의 "구조화된 개인 변동" 주장의 직접 검정). (4) leave-one-subject-out 정렬 일반화. (5) 각 피험자를 독립 반복(N-of-1 replication)으로 보는 분석 | 형질, 인구학, 문화 효과(5명, 여 1명). 개인 경험과 뇌의 연결(본인 보고 없음). 개인 noise ceiling(반복 없음) | 결과는 피험자별로 보고. "5명 중 몇 명에서 재현"을 1차 지표로. 같은 순서라 순서 효과가 개인 간 공유 분산에 섞이므로 run/session 회귀와 자극 순서 permutation 필요 |
| **NSD** | 8명 / 약 10,000장, 3회 반복 | 정서 라벨 사실상 없음(100장 본인 평정) | 개인 내 반복 기반 신뢰도와 차원 스펙트럼(Gauthaman 2024 방식이 이미 시각 피질에 적용). 정서 관련 질문은 다른 데이터셋에서 얻은 정서 부분공간을 투사하는 형태만 | 정서 개인차 직접 검정 | AI 추정 라벨은 "AI 추정"으로 분리 표기 |
| **Emo-FilM** | 30명 / 14편 약 2.7시간, 연속 시계열, 영화 전후 90초 washout | 별도 평정자 1 Hz consensus + 참가자 부분 사후 평정 + **참가자 본인 PPG, 호흡, EDA** + 질문지 | (1) 개인별 동역학(시점, 속도, 이완 시간상수)과 **같은 사람 생리**의 결합(개인 내 brain-body 결합). (2) 개인별 시간상수의 영화 간 신뢰도(형질성). (3) 공유 지도 + 개인별 통과 시점 모형 비교 | 질문지 형질과의 상관은 30명이라 탐색적. 개인 정서 경험 연속 보고 없음 | 영화 14편이라 영화 수준 confound. leave-one-film-out과 subject-level 분할을 동시에 |
| **Spacetop** | 논문 N=101(저장소 117명, 41 run 전부 61명) / 다과제 약 5.4시간, 같은 영상 같은 순서 | **참가자 본인 사후 평정**(alignvideo 7차원, 응답 약 51% 결측) | (1) 개인 정서 기하의 분포와 템플릿 대비 편차. (2) IS-RSA: 개인 쌍의 뇌 기하 유사도 vs 자기 평정 유사도. (3) **과제 간 개인 기하 일관성**(영상 경험, 얼굴 지각, 이야기, 통증): 개인 기하가 형질처럼 안정한가. (4) 자기 평정 구조로 개인 신경 기하 예측(Brooks 2019 방식) | 질문지 형질 연관(공개본에 설문 없음). 100명도 BWAS에는 작음. 영상 내 시간 동역학(평정이 영상 끝 1회) | 쌍별 분석은 Mantel식 피험자 단위 permutation. 결측으로 유효 N 감소. functional alignment 템플릿은 시험 피험자를 빼고 만들고 자극도 분할(피험자, 자극 누수 방지) |

요약: **Horikawa에서 가능한 개인차 질문은 "개인 고유 구조가 존재하며 재현되는가, 어느 rank에 있는가"이고, Spacetop에서 가능한 질문은 "그 고유 구조가 사람마다 어떻게 분포하고, 자기보고와 과제를 가로질러 일관된가"이다.** Emo-FilM은 그 중간으로 "개인별 동역학이 같은 사람의 몸 신호와 맞는가"를 다룬다.

---

## 1. 중요한 미해결 문제

**P1. 정서 반응에서 개인 간에 공유되는 차원은 몇 개이며, 개인 고유 변동은 어느 rank에 있는가.**
Horikawa 2020은 고차원 범주 구조와 개인 간 일관성을 보고했고[본문], Westlin 2025는 같은 데이터에서 피험자별 11~14개 군집과 평정과의 NMI 약 0.014를 보고했다[본문]. Du 2023은 encoding 가중치의 저차원 affective space를[본문], Koide-Majima 2020은 참가자 내 CCA로 18~36개(참가자 의존)를[초록], Du 2025는 MLLM 30차원을 제시했다[본문]. 방법마다 보는 rank 대역이 다르다. Gauthaman 2024는 통상적 RSA와 해부 정렬이 상위 약 10차원만 보며, 개인 간 cross-decomposition과 hyperalignment가 고차 rank의 공유를 드러낸다고 보였다[본문]. 정서 반응에 이 측정을 적용한 연구는 찾지 못했다.
근거: doi:10.1016/j.isci.2020.101060, arXiv:2507.00320, doi:10.1016/j.isci.2023.107571, doi:10.1016/j.neuroimage.2020.117258, arXiv:2509.24298, arXiv:2409.06843

**P2. 정서 지도는 정적 유사성의 지도인가, 경험된 전이의 지도인가.**
Ma & Kragel은 지도형 표상이 "사건 전이의 통계 규칙 학습"에서 나올 수 있다고 썼지만[본문 Discussion 6째 단락] TEM은 균등 무작위 보행으로 학습했다[본문 Methods]. PLOS Biol은 전이 통계의 개인차가 hexagonal 변조의 개인차를 낳을 것이라 예측만 했다[본문]. Thornton & Tamir 2017은 정서 전이 지식이 정적 유사도를 넘는 정보를 담는다고 보고했다[초록]. 경험적 전이 구조(successor geometry)와 정적 동시발생 구조를 뇌에서 겨룬 연구는 찾지 못했다.
근거: doi:10.1038/s41467-025-68240-z, doi:10.1371/journal.pbio.3003795, doi:10.1073/pnas.1616056114, doi:10.1038/nn.4650

**P3. valence는 왜 영화와 데이터셋을 넘어 전이되지 않는가.**
Ke 2025: arousal 모형은 다른 영화와 다른 참가자에게 일반화, valence는 실패. 원인 가설로 (i) 별도 표본 평정이 참가자 경험을 대표하지 못함, (ii) 활동 패턴 형식, (iii) 맥락 의존을 들고 같은 참가자 평정이 필요하다고 썼다[본문]. Zaffina 2026: valence 전이 실패에도 정서 상태의 상대 기하는 데이터셋 간 보존, "풍부성과 휴대성은 분리될 수 있다"[본문]. 세 가설을 가르는 검정은 없다.
근거: doi:10.1371/journal.pcbi.1012994, doi:10.64898/2026.09.26.754452

**P4. vmPFC 정서 신호의 개인 특이성은 "다른 지도"인가, "같은 지도의 다른 통과"인가.**
Chang 2021: 정렬 후에도 vmPFC 반응은 개인 특이적이지만 공간 상태 일부는 공유되고 발현 시점이 다르다. 연속과 이산을 결합한 hybrid 모형을 제안[본문]. Du 2023: vmPFC encoding 성능이 낮고 개인 변동이 크며 잠재 상태 기반 정렬이 필요[본문]. Ma & Kragel: vmPFC가 공유 consensus 궤적을 가장 잘 decoding(r 약 0.1)[본문]. 이 셋은 "공유 지도 + 개인별 시점·속도" 가설로 묶이지만 검정되지 않았다. Hyper-HMM은 모든 피험자가 같은 선형 상태 순서를 지난다고 가정해 재방문 상태에 맞지 않는다[본문].
근거: doi:10.1126/sciadv.abf7129, doi:10.1016/j.isci.2023.107571, doi:10.1038/s41467-025-68240-z, proceedings.neurips.cc/paper_files/paper/2023/hash/558a100caa93422df215fadb9e9b1dd7

**P5. "공유 정서 기하"의 순환성: 공유 표적이 만든 기하와 뇌가 가진 기하의 구분.**
Ma & Kragel의 참가자 간 0.978은 같은 consensus 표적으로 학습한 decoder 출력의 상관 구조다[본문 Methods]. Du 2025의 RSA는 5명 평균[본문], Zaffina 2026은 집단 평균이며 참가자 수준 scaffold는 불안정하다고 밝혔다[본문]. 표적 상관 구조를 그대로 넣은 null(예: 시간 순환 이동 표적으로 학습한 decoder의 출력 기하)과 비교하지 않으면 "뇌가 공유한 기하"를 주장할 수 없다[판단].
근거: doi:10.1038/s41467-025-68240-z, arXiv:2509.24298, doi:10.64898/2026.09.26.754452

**P6. 비지도 구조 발견은 무엇을 발견하는가: 고분산 부분공간과 정서 부분공간의 불일치.**
Westlin 2025의 NMI는 session 0.19, run 0.17로 정서 범주 0.014보다 10배 이상 크다[본문]. 피험자별 PCA 상위 분산 군집이 세션/런 구조를 상당히 반영했을 수 있다[판단]. Rand 0.85는 같은 자료의 재초기화 안정성이지 독립 자료 재현성이 아니다[판단]. Bernardi 2020은 PCA 차원이 낮아도 shattering dimensionality가 높을 수 있음을 보였고[본문], Gauthaman 2024는 분산 가중 추정이 저rank에만 민감하다고 했다[본문]. 정서 정보가 저분산 부분공간에 있다면 상위 PC 군집은 원리상 그것을 놓친다.
근거: arXiv:2507.00320, doi:10.1016/j.cell.2020.09.031, arXiv:2409.06843

**P7. 인간 자연주의 정서에서 정서 상태의 지속(관성)을 기하학적으로 정의할 수 있는가.**
마우스 VMHvl에서 근사 line attractor(시간상수 50초 이상)와 그 시간상수의 개인차가 공격성 개인차와 상관[초록 Nair 2023], 인과 교란 증거[본문 Vinograd 2024]. 인간에서는 영화 후 휴식기 carry-over가 집단 수준 연결과 CAP로 보고되었다[초록 Eryilmaz 2011, Gaviria 2021]. 개인별, 영화별 정서 잠재 차원의 이완 시간상수를 추정한 연구는 찾지 못했다. BOLD의 HRF와 자기상관 때문에 시간상수 추정에는 감각 영역 대조가 필수다[판단].
근거: doi:10.1016/j.cell.2022.11.027, doi:10.1038/s41586-024-07915-x, doi:10.1016/j.neuroimage.2010.10.021, doi:10.1016/j.neuroimage.2021.118377

**P8. 고차 상호작용의 정서 정보는 "시너지"인가 "차원 폭"인가.**
Zaffina 2026은 scaffold의 이점을 상호작용 차수보다 "표상 공간의 폭"으로 해석하고, 위반 삼각형 자체는 단일 모드로 붕괴한다고 보고했다[본문]. Luppi 2022는 시너지가 상위 연합 피질의 통합 처리를 지원한다고 보고했다[초록]. 정서 정보에 대한 부분 정보 분해(PID)를 자연주의 fMRI에 적용한 연구는 이번 검색에서 찾지 못했다.
근거: doi:10.64898/2026.09.26.754452, doi:10.1038/s41593-022-01070-0, doi:10.1038/s41567-022-01852-0

---

## 2. 주목해야 할 모델과 방법론

대부분 분석법이라 pretrained weights 개념이 없다. 라이선스는 PyPI 메타데이터로 확인했고(2026-11-12), GitHub API는 이 세션에서 막혀 저장소 라이선스 파일은 직접 보지 못했다.

| # | 모델/방법 (출처 ID) | Pretrained weights | Input → Output | 학습 목표 / 통계 목적 | 라이선스, 코드 | 우리 데이터 적용 |
|---|---|---|---|---|---|---|
| M1 | Cross-decomposition 스펙트럼 + hyperalignment (arXiv:2409.06843) | 해당 없음(분석법) | 두 피험자의 공유 자극 x voxel 행렬 → rank별 개인 간 교차공분산 스펙트럼, 공유 분산 비율 | 자극 분할 교차검증 SVD, 개인별 회전 | 논문 코드 공개 여부 미확인. hyperalignment는 M2로 대체 가능 | Horikawa(반복 불필요, 개인 간 잡음 독립), NSD(시각 대조), Emo-FilM |
| M2 | Warp hyperalignment / Individualized Neural Tuning (doi:10.1162/imag_a_00032) | 해당 없음 | 다수 피험자 영화 반응 → 공통 템플릿, 개인 tuning matrix, 새 자극에 대한 개인 반응 예측 | 앙상블 정규화 회귀(개인 표상 기하 허용) | `neuroboros` MIT (PyPI 0.1.9) | Spacetop(같은 영상 같은 순서), Emo-FilM |
| M3 | Shared Response Model (NeurIPS 2015) | 해당 없음 | 피험자별 voxel x time → k차원 공유 반응 + 개인 직교 사상, 개인 잔차 | 재구성 오차 최소화(직교 제약) | BrainIAK Apache-2.0 (PyPI 0.12) | 전 데이터셋. 잔차를 개인차 신호로 |
| M4 | Hyper-HMM (NeurIPS 2023) | 해당 없음 | 다수 피험자 fMRI + 자극 embedding → 공통 저차원 공간의 사건 분할 | HMM 우도 + 선형 투영 동시 추정 | 코드 공개 여부 미확인 | Emo-FilM. 재방문 상태 허용 확장 필요 |
| M5 | Gromov-Wasserstein / Fused Unbalanced GW (doi:10.1038/s41598-025-14961-6; arXiv:2206.09398) | 해당 없음 | 두 비유사도 행렬(또는 특징+기하) → 운반 계획, GW 거리, 미운반 질량 | (fused, unbalanced) GW 최소화 | POT MIT (0.9.7), `fugw` MIT (0.1.1) | 개인 간, 뇌-평정, 데이터셋 간 정서 기하 정렬 |
| M6 | CEBRA (doi:10.1038/s41586-023-06031-6) | fMRI용 공개 가중치 없음(직접 학습) | 시계열 (+ 평정, 생리 보조 변수) → 저차원 embedding, 개인 간 consistency | InfoNCE 대조 학습 | Apache-2.0 (PyPI 0.6.1) | Emo-FilM(평정, EDA 보조), Spacetop |
| M7 | Recurrent switching LDS (Vinograd 2024에서 사용, doi:10.1038/s41586-024-07915-x) | 해당 없음 | 잠재 시계열 → 이산 모드 + 모드별 선형 동역학, 시간상수 | 변분 추론 기반 EM | `ssm`(slinderman/ssm) PyPI 라이선스 미기재로 미확인. `dynamax` MIT (1.0.3, HMM과 선형 가우시안 상태공간 계열) | Emo-FilM 영화와 washout |
| M8 | 시간 분해 고차 위상, homological scaffold (doi:10.1038/s41567-022-01852-0; doi:10.64898/2026.09.26.754452) | 해당 없음 | 영역 시계열 → TR별 edge, triangle, scaffold | 기술적(persistent homology) | 원 코드 라이선스 미확인. `ripser` MIT, `giotto-tda` AGPLv3(카피레프트 주의), `kmapper` MIT | Emo-FilM 개인 수준 재현 |
| M9 | 부분 정보 분해(PID), integrated information decomposition (doi:10.1038/s41593-022-01070-0) | 해당 없음 | 두 원천 변수 + 표적 → unique, redundant, synergistic 정보 | 정보 분해(중복 측도 선택에 결과 의존) | `dit` BSD-3 (2.3) | Emo-FilM(표적 = 정서 평정 시계열) |
| M10 | CCGP와 shattering dimensionality (doi:10.1016/j.cell.2020.09.031) | 해당 없음 | 조건별 패턴(예: 34범주) → CCGP, SD | 선형 분류기의 교차조건 일반화 | 코드 미확인(구현 간단) | Horikawa 34범주 |
| M11 | Generalized shape metrics (arXiv:2110.14739) | 해당 없음 | 여러 표상 행렬 → 진짜 거리(metric), Euclidean embedding | Procrustes, CCA 기반 거리 | `netrep` 라이선스 미확인 | Spacetop: 개인을 metric 공간의 점으로 |
| M12 | Dynamic CPM arousal 모형 (doi:10.1371/journal.pcbi.1012994) | **학습 가중치 공개**(저자 Discussion 3째 단락), 저장소 라이선스 미확인 | sliding-window 동적 FC → arousal 시계열 | 선형 CPM | 미확인 | Emo-FilM, Spacetop에서 외부 검증. 짧은 Horikawa 블록에는 부적합(저자 언급) |
| M13 | Information bottleneck 명명 효율 (doi:10.1073/pnas.1800521115) | 해당 없음 | 의미 분포 p(u given m) + 명명 체계 q(w given m) → 복잡도, 정확도, IB 경계와의 거리 | IB Lagrangian | 원 코드 미확인 | Horikawa 범주 체계 평가 |
| M14 | TEM (Ma & Kragel 2026에서 사용) | Ma & Kragel 학습 가중치 공개 여부 미확인 | 행동 + 관측 시퀀스 → layer p, g 활성 | 다음 관측 예측 | 미확인 | Emo-FilM 실제 전이로 재학습(C2) |

---

## 3. 다른 분야에서 가져올 연구 아이디어

**I1. 시각 신경과학의 rank 분해 공유 스펙트럼 → 정서 반응의 공유 차원 수 (Horikawa, G1 불필요).**
Gauthaman 2024의 개인 간 cross-decomposition을 Horikawa 5명에 적용한다. 공유 스펙트럼의 각 rank 대역이 34범주, 14차원, semantic 73, vision 1000 feature 중 무엇으로 설명되는지 대역별 variance partitioning을 한다. 정서 고유 공유 분산이 고rank까지 이어지면 "고차원 정서 표상"을, 상위 몇 차원에만 있으면 "저차원 + 내용 혼입"을 지지한다. (Chain C1) overlap: EmoViS (Horikawa affective geometry의 sensory-semantic 기원과 부분 겹침)

**I2. 원숭이 전기생리의 추상화 기하(CCGP) → 정서 이론 논쟁의 기하 예측 (Horikawa, G1 불필요).**
Bernardi 2020의 CCGP와 SD를 Horikawa 34범주에 적용한다. 예: valence decoder를 {amusement, joy vs fear, horror}로 학습하고 {awe, aesthetic appreciation vs disgust, anxiety}로 시험(범주 단위 hold-out이라 자극 누수 없음). 예측: 기본정서이론은 범주 dichotomy의 높은 CCGP, 구성주의는 valence/arousal의 높은 CCGP와 범주의 낮은 CCGP 및 높은 SD. Ma & Kragel의 이중 해리(hippocampus 범주, vmPFC 2D)는 "hippocampus 높은 SD, vmPFC 높은 valence CCGP"로 번역된다. 선행: 이번 검색에서 정서 fMRI의 CCGP 적용은 찾지 못함(no).

**I3. 공간 항해의 grid 분석 → 자연주의 정서 궤적의 hexadirectional 검정 (Emo-FilM, Horikawa).**
PLOS Biol의 통제 과제 결과를 Emo-FilM 1 Hz 궤적의 이동 방향으로 옮긴다. Horikawa는 고정 순서 연속 클립 사이의 affective space "도약" 방향이 생기므로, 연속 궤적(Emo-FilM) 대 비연속 도약(Horikawa)을 대조할 수 있다. 위험: 궤적 속도가 느리고 방향 추정 잡음이 크며, 방향과 장면 내용이 공선적일 수 있다. Gardner 2022는 진짜 위상 검정에는 세포 수준 기록이 필요함을 시사한다[초록]. 선행: no(자연주의 데이터).

**I4. 운동 신경과학의 개체 간 잠재 동역학 보존 → "내부 상태가 맞는 사람끼리만 정렬되는가" (Spacetop).**
Safaie 2023 Discussion은 상위 영역은 내부 상태가 달라 보존이 약하고, 내부 상태를 맞추면 보존될 것이라 예상했다[본문]. Spacetop alignvideo에서 두 참가자의 잠재 궤적 정렬도(CCA)를 영상별로 계산하고, 그 영상에 대한 두 사람 자기 평정의 유사도로 예측한다. 정렬도-평정 유사도 관계가 감각 영역보다 vmPFC, insula에서 강하면 "정서 잠재 동역학은 경험이 같을 때 공유된다"를 지지. (Chain C3, C8과 연결)

**I5. 신경동물행동학의 line attractor → 영화 후 washout의 정서 이완 시간상수 (Emo-FilM).**
Nair 2023, Vinograd 2024의 "통합 차원 시간상수"를 인간 BOLD에 옮긴다. 인과 교란은 불가하지만 영화가 끝나는 순간이 입력 제거(자연 실험)가 된다. 관찰 자료이므로 attractor 존재의 인과 증거가 아니라 "이완이 감각 영역보다 느린 정서 잠재 차원이 있는가"의 기술로 한정한다. (Chain C5)

**I6. 언어학의 정보 병목 효율 → 정서 범주 체계의 효율성 (Horikawa).**
Zaslavsky 2018은 색 이름 체계가 IB 최적 경계에 가깝고 단일 trade-off 모수로 언어 변이를 설명한다고 보였다[초록]. 정서 범주 체계(기본 6, Emo-FilM 13, Cowen & Keltner 27, Horikawa 34, valence-arousal 사분면)를 "뇌의 공유 정서 공간"을 의미 공간으로 두고 평가한다. 선행: 이번 검색에서 정서 어휘에 IB를 적용한 연구 찾지 못함(no). (Chain C7)

**I7. 최적 수송의 불균형 정렬(종간 정렬) → 개인 특이성 지수와 데이터셋 고유 영역 (Spacetop, 교차 데이터셋).**
Thual 2022의 unbalanced GW는 한쪽에 대응이 없는 영역을 허용한다[본문]. 두 사람 정서 기하 사이에서 "운반되지 못한 질량"을 개인 특이성의 정량 지표로 쓴다. 교차 데이터셋에서는 공통 모델 feature 공간의 encoding 가중치 프로파일을 기능 서명으로 써서 Horikawa(무음) 피험자와 Emo-FilM(소리) 피험자를 정렬하고, 미운반 질량이 청각 관련 영역에 몰리는지 본다(G1 필요, 보유).

**I8. ML의 표상 수렴 가설 → "수렴 기울기" (Horikawa, NSD, Emo-FilM).**
Huh 2024는 양식 고유 정보와 특수 목적 시스템에서는 수렴이 깨질 수 있다고 썼다[본문 6절]. 개인 뇌 사이 정렬도(mutual k-NN)를 시각, 의미, 정서 부분공간별로 비교한다. 예측: 개인 간 수렴은 시각 > 의미 > 정서. 정서 부분공간의 낮은 수렴이 개인 평정 편차와 맞으면 개인 특이성, 맞지 않으면 잡음.

**I9. 정보 기하(Fisher information) → 정서 공간의 국소 변별력 지도 (Horikawa, Emo-FilM).**
Kriegeskorte & Wei 2021은 표상 기하가 Fisher information과 이상 관찰자 성능을 결정한다고 정리했다[초록]. 14차원(또는 2D) encoding 모형의 Jacobian과 잔차 공분산으로 J(θ)를 계산해 "어느 정서 영역에서 신경 변별력이 높은가"를 지도화한다. 예측: 위협 관련 고각성 부정 영역에서 변별력이 높다면 생존 관련 정밀화, 고르면 범용 부호. 행동 쪽 정서 granularity와 비교 가능(Emo-FilM 질문지).

---

## 4. 기존 Affective Neuroscience와 예상 밖으로 연결될 개념

**U1. Scale-free 스펙트럼 × 정보 병목 = "정서 범주 수 논쟁"의 해소 가능성.**
공유 신경 스펙트럼이 power law(scale-free)이면 자연스러운 차원 수나 범주 수가 따로 없다. 그러면 6, 13, 27, 34개 체계의 차이는 "참값 논쟁"이 아니라 소통 목적에 따른 IB trade-off 모수(β) 차이로 재해석된다. 근거: arXiv:2409.06843, doi:10.1038/s41586-019-1346-5, doi:10.1073/pnas.1800521115, doi:10.1073/pnas.1702247114. 반증: 스펙트럼에 뚜렷한 꺾임(elbow)이 있고 그 위치가 특정 범주 수와 맞으면 이 해석은 기각된다.

**U2. 정서 관성(심리학) × line attractor 시간상수(신경동물행동학) × washout 이완(fMRI 설계의 부산물).**
fMRI 설계에서 보통 버리는 영화 전후 고정점 구간이 정서 동역학의 자연 실험이 된다. 근거: doi:10.1016/j.cell.2022.11.027, doi:10.1038/s41586-024-07915-x, doi:10.1016/j.neuroimage.2021.118377.

**U3. 추상화 기하(CCGP) × 기본정서이론 대 구성주의 논쟁.**
이론 논쟁을 "어떤 변수가 어떤 영역에서 추상 형식인가"라는 측정 가능한 기하 예측으로 바꾼다. Westlin 2025가 요구한 "귀무가설이 아닌 대안 이론과의 비교"[본문 Discussion 5째 단락]를 구체화한다. 근거: doi:10.1016/j.cell.2020.09.031, arXiv:2507.00320, doi:10.1016/j.isci.2020.101060.

**U4. 불균형 최적 수송의 "질량 소멸" × 정서 개인 특이성.**
개인 특이성을 "공통 공간으로 옮겨지지 않는 표상의 양"으로 정의하면, Westlin(개인 특이)과 Horikawa(공유)의 주장을 같은 척도의 서로 다른 값으로 비교할 수 있다. 근거: arXiv:2206.09398, doi:10.1038/s41598-025-14961-6.

**U5. Successor representation의 할인율 × hippocampus 장축 × 정서의 시간척도.**
Ma & Kragel은 love, satisfaction, guilt가 전측 hippocampus에서 더 잘 decoding된다고 보고하며 이 정서들의 긴 시간 통합을 이유로 들었다[본문 Discussion 4째 단락]. SR의 할인율 γ를 시간척도로 보면 "정서 범주마다 고유한 예측 지평"이라는 새 구성 개념이 생긴다. 근거: doi:10.1038/s41467-025-68240-z, doi:10.1038/nn.4650.

---

## 5. 새 Sub-axis 또는 하위 연구 방향

| # | 제안 | 소속 Axis | 독립 Axis 필요성 | 근거 ID |
|---|---|---|---|---|
| S1 | **Rank-resolved sharedness (공유 스펙트럼)**: rank 대역별 개인 간 공유 분산과 그 대역의 내용(정서, 의미, 시각) | K + O | 불필요. K의 Dimensionality와 O의 Universal vs Idiosyncratic을 잇는 sub-axis | arXiv:2409.06843, doi:10.1038/s41586-019-1346-5 |
| S2 | **Abstraction geometry**: CCGP, shattering dimensionality, factorization | K | 불필요 | doi:10.1016/j.cell.2020.09.031 |
| S3 | **Relaxation and persistence dynamics**: attractor 시간상수, washout 이완, 정서 관성의 기하 정의 | K (Dynamical Attractors) + D | 불필요. K와 D의 경계를 명시(아래 7절) | doi:10.1038/s41586-024-07915-x, doi:10.1016/j.neuroimage.2021.118377 |
| S4 | **Geometric idiosyncrasy metrics**: shape-metric 거리, unbalanced OT 미운반 질량, private subspace 차원 | O | 불필요 | arXiv:2110.14739, arXiv:2206.09398, NeurIPS 2015 SRM |
| S5 | **Metric choice**: Euclidean, cityblock, geodesic(manifold), successor metric 중 어느 거리가 뇌 정서 기하에 맞는가 | K | 불필요 | doi:10.1371/journal.pbio.3003795 (Discussion 4째 단락), doi:10.1038/nn.4650 |
| S6 | **Higher-order interaction and synergy**: 단체 복합체, PID 시너지 | K + E | 불필요 | doi:10.1038/s41567-022-01852-0, doi:10.1038/s41593-022-01070-0 |
| S7 | **Information-theoretic efficiency of affective categories**: IB, rate-distortion으로 정서 범주 체계 평가 | K × A (× C) | **독립 Axis 후보.** 범주 체계의 효율은 기하(K), 구성 개념(A), 언어와 의미(C), 측정(Q)에 걸치며 어느 하나에 넣으면 시야가 좁아진다. 우선 K의 sub-axis로 두고 Round 2에서 llm-semantics, emotion-theory와 논의 제안 | doi:10.1073/pnas.1800521115, doi:10.1126/science.aaw8160 |
| S8 | **Sample-size regime-aware individual differences**: deep sampling idiographic vs broad sampling nomothetic, 개인 내 결합 우선 | O (+ T) | 불필요 | doi:10.1038/s41586-022-04492-9, doi:10.1016/j.neuroimage.2020.116828 |

---

## 6. Discussion-to-Research chains

각 사슬은 `Original Finding → Unresolved Question → Technological Development → New Dataset / Model Combination → New Research Question` 형식이다. 모두 탐색 제안이며 확증 결과가 아니다.

### C1. 정서 반응의 rank 분해 공유 스펙트럼 (Horikawa 우선)

* **Original Finding:** Horikawa 2020은 정서 표상이 고차원, 범주적이며 개인 간 일관적이라 보고(doi:10.1016/j.isci.2020.101060, Discussion 1~3째 단락 [본문]). Westlin 2025는 최소 가정 분석에서 개인 고유 군집 11~14개, 평정과 NMI 약 0.014, 개인 간 군집 중첩 7.3%를 보고하고 multiverse 분석을 요구(arXiv:2507.00320, Results; Discussion 5째 단락 [본문]).
* **Unresolved Question:** 두 결론은 서로 다른 rank 대역을 본 결과인가? 개인 고유 변동은 재현 가능한 구조인가 잡음인가(Westlin의 Rand 0.85는 재초기화 안정성)? Horikawa 원 저자도 개인차 변수를 넣으면 더 강건한 표상을 찾을 수 있다고 함(Limitations of the Study 1째 단락 [본문]).
* **Technological Development:** Gauthaman 2024의 개인 간 cross-decomposition과 hyperalignment가 고rank 공유를 드러내고 RSA는 소수 차원에만 민감함을 보임. 고rank의 개인 특이 분산이 의미 있는 개인차인지 향후 과제로 남김(arXiv:2409.06843, 3.4절 마지막 단락, 4 Discussion [본문]).
* **New Dataset / Model Combination:** Horikawa 5명 x 2,181 공유 자극(반복 없어도 개인 간 잡음은 독립이라 교차공분산이 편향되지 않음) + 자극 교차분할(hyperalignment 학습 자극과 스펙트럼 평가 자극 분리) + figshare 34범주, 14차원, semantic 73, vision 1000 feature로 rank 대역별 variance partitioning. 대조: NSD 공유 이미지의 시각 피질 스펙트럼.
* **New Research Question:** "정서 유발 비디오에 대한 transmodal 영역 반응에서 개인 간 공유되는 차원의 스펙트럼은 어떤 형태이고, 정서 평정이 고유하게 설명하는 공유 분산은 어느 rank 대역에 있는가? Westlin이 관찰한 개인 특이성은 고rank의 재현 가능한 개인 성분인가, 세션/런 drift 같은 저rank 비정서 성분인가?"
* **분석과 반증:** (a) 영역별 공유 스펙트럼과 power-law 지수. (b) 대역별로 정서 feature가 시각, 의미 feature를 넘어 설명하는 분산. (c) 개인 고유 편차(개인 기하 - 템플릿 기하)의 자극 절반 간 재현성. (d) run/session 회귀 전후 Westlin식 군집의 NMI 변화. 반증: 정서 고유 공유 분산이 상위 몇 rank에만 있고 시각, 의미 통제 후 사라지면 "고차원 정서 표상"은 지지되지 않는다. 개인 편차가 자극 절반 간 재현되지 않으면 "구조화된 개인 변동"은 지지되지 않는다.
* **주의:** 5명 모두 같은 순서라 순서 효과가 공유 분산에 섞임(run 평균 회귀, 순서 블록 permutation). 평정은 별도 평정자 집단 평균이므로 "정서 평정이 설명"은 "규범 평정과 공변"으로 해석. 공개 전처리본이 native volume이라 HCP360 parcel 또는 hyperalignment로만 결합.
* G1: 핵심 분석 불필요, 최신 모델 feature 통제 시 필요(보유). 선행: no(정서 반응에 이 방법 적용 미발견). overlap: EmoViS (Horikawa 정서 기하의 sensory-semantic 기원과 부분 겹침), EmoBrain (cross-subject, 약함).

### C2. 정적 유사성 지도 vs 경험된 전이 지도 (Emo-FilM)

* **Original Finding:** Ma & Kragel 2026: hippocampus-vmPFC의 지도형 표상이 사건 전이의 통계 규칙 학습에서 나올 수 있다(doi:10.1038/s41467-025-68240-z, Discussion 6째 단락 [본문]). 그러나 TEM은 균등 무작위 보행으로 학습(Methods [본문]). RL 모형 비교를 향후 과제로 제시(Discussion 9째 단락). PLOS Biol: 전이 통계 개인차가 hexagonal 변조 개인차를 낳을 것(doi:10.1371/journal.pbio.3003795, Discussion 3째 단락 [본문]).
* **Unresolved Question:** 뇌의 정서 지도는 정서 간 정적 동시발생 유사성을 반영하는가, 실제로 경험되는 전이 구조를 반영하는가? 둘은 다르다는 행동 증거가 있음(doi:10.1073/pnas.1616056114 [초록]).
* **Technological Development:** Successor representation(doi:10.1038/nn.4650 [초록])은 전이 행렬 T와 할인율 γ로 예측 지도를 정의하고 grid cell을 그 저차원 기저로 본다. 다중 γ로 시간척도별 지도를 만들 수 있다.
* **New Dataset / Model Combination:** Emo-FilM consensus 1 Hz 50항목에서 영화별 경험 전이 행렬을 leave-one-film-out으로 추정 → SR(γ 여러 값) 기반 RDM, 정적 상관 기반 RDM(Ma & Kragel 방식), TEM(실제 전이로 재학습) RDM을 hippocampus 전후, vmPFC의 교차검증 신경 RDM과 경쟁 비교. Horikawa의 고정 순서 클립 전이는 생태적 전이 구조가 없는 음성 대조.
* **New Research Question:** "hippocampus-vmPFC 정서 지도는 정적 동시발생 구조보다 경험된 전이 구조(successor geometry)에 더 잘 맞는가? 맞는 할인율 γ는 후측 hippocampus < 전측 hippocampus < vmPFC 순으로 커지는가?"
* **분석과 반증:** SR RDM이 정적 RDM을 통제한 뒤 신경 RDM을 추가로 설명하지 못하면 "전이 지도" 가설은 기각. γ 기울기가 장축에서 나타나지 않으면 시간척도 위계 가설 기각.
* **주의:** 영화의 전이는 서사가 만든 것이며 별도 평정자의 경험 보고다(참가자 경험 아님). 상태가 특정 영화에 몰리면 영화 정체성 혼입(영화 내 RDM 평균). 시각-의미 nuisance(G1 필요, 보유). 신경 RDM과 전이 행렬은 다른 영화로 추정해 순환 추론 방지.
* 선행: partially (doi:10.1038/s41467-025-68240-z, 무작위 보행 TEM). overlap: Emo-FilM 연구 (Emo-FilM 시간 정보 기여, 약함).

### C3. valence 비전이의 원인 판별: 개인 특이성 vs 맥락 의존 (Spacetop + Emo-FilM)

* **Original Finding:** Ke 2025: arousal 일반화, valence 실패. 원인 후보로 별도 표본 평정의 비대표성, 패턴 형식, 맥락 의존을 들고 같은 참가자 평정이 필요하다고 씀(doi:10.1371/journal.pcbi.1012994, Discussion 'In contrast to emotional arousal' 단락, 공개 데이터셋 한계 단락 [본문]). Zaffina 2026: valence 비전이에도 상대 기하는 보존, 풍부성과 휴대성의 분리, 집단 평균의 한계(doi:10.64898/2026.09.26.754452, Discussion 9째 단락, 한계 단락 [본문]).
* **Unresolved Question:** valence 전이 실패는 (i) 라벨 주체 불일치, (ii) 개인별 기하 차이, (iii) 맥락마다 바뀌는 좌표 사상 중 무엇 때문인가?
* **Technological Development:** 개인 표상 기하를 허용하는 warp hyperalignment/INT(doi:10.1162/imag_a_00032, Discussion [본문]), 점 대응 없이 관계 구조를 맞추는 GW(doi:10.1038/s41598-025-14961-6 [본문]).
* **New Dataset / Model Combination:** Spacetop alignvideo(참가자 본인 평정, 49 영상, 같은 순서)와 Emo-FilM(Good/Bad consensus, 참가자 부분 사후 평정)에서 네 모형 비교: (a) 집단 라벨 + 해부 정렬, (b) 자기 라벨 + 해부 정렬(Spacetop만), (c) 집단 라벨 + INT 개인화, (d) GW로 정렬한 관계 기하의 보존만 평가. Spacetop에는 valence 문항이 없어 happy, warm and tender 대 sad, afraid, disgusted의 대비를 파생 지표로 쓴다(파생 라벨임을 명시).
* **New Research Question:** "자기보고 라벨과 개인화 정렬을 쓰면 valence의 교차 자극 전이가 arousal 수준으로 회복되는가, 아니면 관계 기하는 보존되지만 선형 좌표 사상만 맥락마다 바뀌는가?"
* **분석과 반증:** (b), (c)가 valence에서만 큰 개선을 보이면 개인 특이성 가설 지지. 개선이 없고 (d)의 관계 기하 보존만 높으면 맥락 의존 가설 지지. 둘 다 아니면 측정 문제(Spacetop 결측 51%, 영상당 1회 평정) 가능성.
* **주의:** Spacetop 평정은 영상 종료 후 1회라 영상 내 동역학 불가. 결측이 비무작위일 수 있음. 템플릿은 시험 피험자, 시험 영상 제외로 구성.
* G1: 불필요(라벨과 fMRI), 내용 통제 시 필요(보유). 선행: no. overlap: EmoBrain (cross-subject 정서 decoding, 부분), Emo-FilM 연구 (약함).

### C4. 공유 지도, 개인별 통과: vmPFC의 시공간 개인차 (Emo-FilM)

* **Original Finding:** Chang 2021: 정렬 후에도 vmPFC는 개인 특이적, 공유 상태는 있으나 발현 시점이 다름. 같은 상태 수 가정의 한계와 hybrid(연속+이산) 모형 필요(doi:10.1126/sciadv.abf7129, Discussion 4째 단락, 한계 단락 [본문]). Du 2023: vmPFC 정렬에는 잠재 상태 기반 접근 필요(doi:10.1016/j.isci.2023.107571, Limitations of the study 3째 단락 [본문]).
* **Unresolved Question:** Ma & Kragel의 vmPFC 2D 궤적 decoding이 약한 것(r 약 0.1)은 사람마다 같은 지도를 다른 시점과 속도로 지나기 때문인가?
* **Technological Development:** rSLDS(Vinograd 2024에서 사용, doi:10.1038/s41586-024-07915-x [본문]), Hyper-HMM의 시공간 동시 정렬과 그 한계(같은 선형 상태 순서 가정, NeurIPS 2023, 5절 [본문]), CEBRA의 개인 간 consistency(doi:10.1038/s41586-023-06031-6 [초록]).
* **New Dataset / Model Combination:** Emo-FilM 30명 vmPFC. 다른 영화로 학습한 SRM 공통 공간에서 (i) 공유 지도 + 공유 시점, (ii) 공유 지도 + 개인별 time-warp, (iii) 개인별 지도의 세 모형을 보류 영화 우도와 consensus 평정 decoding으로 비교. 개인 내 기준: **같은 참가자의 EDA, PPG**에서 얻은 각성 반응 시점.
* **New Research Question:** "vmPFC 정서 표상의 개인차는 지도 자체의 차이인가, 같은 지도를 지나는 시점과 속도의 차이인가? 개인별 신경 time-warp는 같은 사람의 피부전도 반응 지연과 일치하는가?"
* **분석과 반증:** (ii)가 (i)보다 보류 우도와 decoding에서 우수하고 신경 warp와 EDA warp가 상관하면 "공유 지도, 개인 통과" 지지. (iii)이 가장 우수하면 개인 고유 지도 지지.
* **주의:** 개인별 HRF 차이(시각 피질 onset으로 추정, 데이터셋에 onset 검증 파생물 있음), 심장, 호흡 잡음(제공 전처리본에 생리 회귀 미반영, raw 재전처리 필요), 평정 주체는 별도 평정자.
* 선행: no. overlap: Emo-FilM 연구 (약함).

### C5. 영화 후 washout의 정서 이완 시간상수 (Emo-FilM)

* **Original Finding:** Nair 2023: 근사 line attractor, 시간상수 개인차와 공격성 상관(doi:10.1016/j.cell.2022.11.027 [초록]). Vinograd 2024: on-manifold 교란 지속, off-manifold 빠른 이완, 연결 강도 개인차와 attractor 안정성 상관, 유연성과 강건성의 기전이 향후 과제(doi:10.1038/s41586-024-07915-x, Discussion 마지막 단락 [본문]).
* **Unresolved Question:** 인간 자연주의 정서에서 정서 잠재 차원의 지속(관성)을 개인별, 자극별 시간상수로 측정할 수 있는가? 인간 carry-over 연구는 집단 수준 연결과 CAP였다(doi:10.1016/j.neuroimage.2010.10.021, doi:10.1016/j.neuroimage.2021.118377 [초록]).
* **Technological Development:** rSLDS와 상태공간 모형의 시간상수 추정, CEBRA로 평정 정보 잠재 차원 학습.
* **New Dataset / Model Combination:** Emo-FilM의 영화별 앞뒤 90초 washout(14편 x 30명 = 영화 후 구간 약 420개, 생리 기록 포함). 영화 중 consensus 평정으로 정의한 정서 잠재 차원을 washout에 투사해 이완 곡선을 적합하고, 시각 피질 잠재 차원의 이완(HRF 수준)을 대조로 둔다.
* **New Research Question:** "정서 영화가 끝난 뒤 정서 관련 잠재 차원은 감각 차원보다 느리게 이완하는가? 이완 시간상수는 영화 마지막 구간의 정서 종류와 강도에 따라 달라지고, 사람마다 영화 간 일관된가(형질성), 같은 사람의 EDA 회복 시간과 맞는가?"
* **분석과 반증:** 정서 차원 시간상수가 시각 대조와 다르지 않으면 "정서 관성 차원" 가설 기각. 개인 시간상수의 영화 간 ICC가 낮으면 형질 해석 기각.
* **주의:** **제공 전처리본은 high-pass(sigma 50 s)가 적용되어 수십 초 이완을 왜곡할 수 있어 raw 재전처리 필요**(Stage 1 dataset_EmoFilM.md 1.2절의 전처리 사양). washout에는 평정이 없어 정서 해석은 영화 끝 평정과 EDA로 간접 검증. 마음 방황, 졸음, 움직임 혼입. 관찰 자료이므로 attractor의 인과 증거가 아님.
* 선행: partially (doi:10.1016/j.neuroimage.2010.10.021, doi:10.1016/j.neuroimage.2021.118377; 개인별 잠재 차원 시간상수는 no). overlap: Emo-FilM 연구 (Emo-FilM 시간 정보, 약함).

### C6. 고차 위상의 정서 정보: 시너지인가 차원 폭인가 (Emo-FilM)

* **Original Finding:** Zaffina 2026: scaffold가 50항목 프로파일을 가장 잘 예측하나 이점은 "상호작용 차수가 아니라 표상 공간의 폭"이라고 해석, 위반 삼각형은 단일 모드로 붕괴, 참가자 수준 scaffold 불안정, 집단 평균 사용(doi:10.64898/2026.09.26.754452, Discussion 2~3째 단락, Methods [본문]).
* **Unresolved Question:** 고차 표현이 담는 정서 정보는 개별 영역이나 쌍에 없는 시너지 정보인가, 단지 많은 약한 모드에 퍼진 정보인가? 개인 수준에서 측정 가능한가?
* **Technological Development:** PID/ΦID(doi:10.1038/s41593-022-01070-0 [초록])로 시너지를 직접 정량. SRM 공통 공간에서 개인 잡음을 줄인 뒤 위상 추정.
* **New Dataset / Model Combination:** Emo-FilM 119 영역 시계열. (a) scaffold와 같은 유효 차원으로 맞춘 pairwise edge 무작위 투영 대조, (b) 영역 쌍의 정서 평정 시계열에 대한 시너지 지도, (c) SRM 잡음 제거 후 개인별 scaffold의 영화 분할 신뢰도.
* **New Research Question:** "자연주의 정서의 세밀한 프로파일 정보는 영역 쌍의 시너지로 존재하는가? 고차 위상의 이점은 차원 폭을 맞추면 사라지는가?"
* **분석과 반증:** 차원 맞춘 대조가 scaffold와 같으면 '폭' 해석, 시너지 쌍이 unique 정보를 넘어 정서를 설명하면 '시너지' 해석.
* **주의:** PID 결과는 중복 측도 선택에 의존(여러 측도 보고). 1 Hz consensus를 TR로 맞출 때 HRF 처리. 다중비교(영역 쌍 7,021개).
* 선행: no(정서 자연주의 fMRI의 PID 미발견). overlap: 없음.

### C7. 정서 범주 체계의 정보 병목 효율 (Horikawa)

* **Original Finding:** Zaslavsky 2018: 색 이름 체계가 IB 최적에 가깝고 원리가 다른 의미 영역에도 적용될 수 있다(doi:10.1073/pnas.1800521115 [초록]). Cowen & Keltner 2017: 27개 신뢰 가능 범주와 연속 gradient(doi:10.1073/pnas.1702247114 [초록]). Horikawa 2020은 범주가 차원보다 뇌 분산을 더 설명하나 그와 같은 정보를 가진 충분한 appraisal 집합이 있을 수 있다고 Discussion에서 단서를 둠(Discussion 3째 단락 [본문]).
* **Unresolved Question:** 정서 범주의 "올바른 수"는 경험적으로 정할 수 있는가, 아니면 압축과 정확도 사이 선택인가?
* **Technological Development:** IB 경계 계산, C1에서 얻은 공유 정서 부분공간을 의미 공간으로 사용.
* **New Dataset / Model Combination:** Horikawa 2,181 자극. 의미 분포를 (a) 34+14 평정 공간, (b) 개인 간 공유 신경 정서 부분공간으로 각각 정의하고, 기본 6, 13(Emo-FilM 이산 항목과 이름 대응되는 부분), 27, 34, valence-arousal 사분면, 데이터 기반 k-군집 체계를 IB 평면에 배치.
* **New Research Question:** "인간 정서 범주 체계는 뇌의 공유 정서 공간에 대해 IB 최적 경계에 가까운가? 평정 공간 기준과 신경 공간 기준의 최적 범주 수는 다른가?"
* **분석과 반증:** 인간 체계가 무작위 분할이나 데이터 기반 분할보다 IB 경계에서 멀면 효율 가설 기각.
* **주의:** 자극 분포는 Cowen & Keltner가 큐레이션한 라이브러리라 p(m)이 편향. 신경 공간에 시각-의미 성분이 섞임(C1의 정서 고유 부분공간 사용). 평정자(미국)와 fMRI 참가자(일본) 문화 불일치(doi:10.1126/science.aaw8160의 문화 변이 결과가 해석 배경). 이론적, 탐색적 분석.
* G1: 불필요. 선행: no. overlap: EmoViS (Horikawa 정서 기하, 약함).

### C8. 개인 정서 기하는 과제를 가로지르는 형질인가 (Spacetop)

* **Original Finding:** Gündem 2022: 범주를 가로지르는 개인 일관성('neural topography trait')(doi:10.1038/s42003-022-04324-6, Discussion H6/H7 단락 [본문]). Brooks 2019: 개인 개념 구조가 그 사람의 fusiform 표상 구조를 예측(doi:10.1073/pnas.1816408116 [초록]). Camacho 2023: 개인 정의 라벨과 성인 라벨 비교, 정서 추론 개인차와의 대응이 과제(doi:10.1038/s41593-023-01358-9, Discussion [본문]). Finn 2020: 검사-재검사 타당도와 자극 선택이 개인차 연구의 핵심 과제(doi:10.1016/j.neuroimage.2020.116828, 7절, 8절 [본문]).
* **Unresolved Question:** 개인의 정서 표상 기하 편차는 한 과제에 국한된 것인가, 양식과 과제를 넘는 안정 형질인가? 그 편차는 본인의 자기보고 구조로 설명되는가?
* **Technological Development:** INT 개인 tuning(doi:10.1162/imag_a_00032 [본문]), shape metric으로 개인을 metric 공간의 점으로(arXiv:2110.14739 [초록]).
* **New Dataset / Model Combination:** Spacetop의 같은 참가자 다과제: alignvideo(본인 경험 평정), faces(표정 강도 지각), shortvideo(인물 정서 귀속), narratives, 통증. 과제별 개인 기하 편차를 shape metric으로 계산하고 과제 간 일관성을 본다. 개인 자기 평정의 정서 공존 구조(49 영상에 걸친 7차원 평정 상관)를 개인 "개념 구조"로 둔다.
* **New Research Question:** "한 사람의 정서 표상 기하가 집단 템플릿에서 벗어나는 방향은 영상 경험, 표정 지각, 이야기, 통증 과제에서 일관되는가? 그 방향은 그 사람의 자기보고 정서 공존 구조로 예측되는가?"
* **분석과 반증:** 과제 간 편차 상관이 피험자 순열 null과 다르지 않으면 형질 가설 기각. 자기보고 구조가 신경 편차를 예측하지 못하면 Brooks식 개념 경로 기각(단 결측으로 검정력 제한).
* **주의:** Marek 2022 기준 형질 상관 확증은 불가하므로 개인 내 결합과 쌍별 구조 중심. 과제마다 자극 양식이 달라 "공통 정서 기하"가 공통 시각 처리일 위험(정서 무관 대조 과제 기하와 비교). Spacetop 설문 미공개.
* 선행: no. overlap: 없음.

---

## 7. 담당 Axis 확장 제안

### Axis K: Geometry & Mathematical Structure

| 조치 | 항목 | 이유 |
|---|---|---|
| 추가 | Rank-resolved sharedness / spectral geometry (S1) | "Dimensionality" 하나로는 방법별 차원 추정 충돌(P1)을 다룰 수 없다 |
| 추가 | Abstraction geometry: CCGP, shattering dimensionality, factorization (S2) | 이론 논쟁을 기하 예측으로 바꾸는 핵심 도구 |
| 추가 | Relaxation and persistence dynamics (S3) | "Dynamical Attractors"를 측정 가능한 시간상수로 구체화 |
| 추가 | Metric choice: Euclidean, cityblock, geodesic, successor metric (S5) | PLOS Biol이 남긴 문제, SR과 연결 |
| 추가 | Higher-order interaction and synergy (S6) | Zaffina 2026 이후 정서 연구의 현재 최전선 |
| 추가 | Information-theoretic efficiency (S7, 독립 Axis 후보) | IB, rate-distortion |
| 추가 | Representational metric spaces (shape metrics) | 개인과 모델을 같은 거리 공간에서 비교 |
| 재분류 | "Dynamical Attractors", "Latent Trajectories"와 Axis D의 "Recurrent / State-space Dynamics" 경계 | K는 동역학의 기하, 위상 속성(차원, 시간상수, 위상), D는 시간 구성 개념(onset, peak, 전이 시점)을 맡는다고 명시 |
| 재정의 | "Distributional Representations" | 범위가 모호하다. "확률적 표상(불확실성, 분포 부호)"과 "분포 간 정렬(OT)"로 나누고 후자는 "Optimal Transport"에 통합 |
| 경고 문구 | "Manifold Learning" | 단순 차원 축소 시각화는 P5 Novelty Constraint 대상. 반드시 교차검증, 개인 간 공유 검정, null 모형과 함께 쓰도록 주석 |

### Axis O: Individual & Population Variation

| 조치 | 항목 | 이유 |
|---|---|---|
| 추가 | Shared vs private subspace spectrum (S1과 공유) | 개인 특이성의 위치(rank)를 정량화 |
| 추가 | Individualized representational geometry (WHA/INT) | Procrustes hyperalignment는 기하를 보존하므로 기하의 개인차를 못 본다 |
| 추가 | Traversal idiosyncrasy: 개인별 시점, 속도, time-warp | P4, C4 |
| 추가 | Geometric idiosyncrasy metrics (S4) | Westlin과 Horikawa를 같은 척도로 비교 |
| 추가 | Label-subject mismatch as individual-difference signal | 규범 평정과 본인 보고의 차이를 잡음이 아니라 측정 대상으로(Spacetop 본인 vs 타인 평균, Emo-FilM consensus vs 참가자 사후 평정) |
| 추가 | Sample-size regime (S8) | Horikawa 5명과 Spacetop 약 100명에서 가능한 질문이 다르다(0.2절) |
| 재분류 | "Trait-dependent Representation" | 우리 데이터에서는 확증 불가(Spacetop 설문 미공개, Emo-FilM 30명). "탐색적"으로 표시하고 개인 내 결합을 우선 |
| 유지 | Functional Alignment, Hyperalignment / SRM, Cross-subject Generalization | 단 정렬 템플릿 구성 시 피험자, 자극 누수 방지 규칙을 Axis 설명에 명시 |

---

## 8. 검증 상태, 미확인 사항, 방법론 점검

**검증된 것**
* 45편 모두 식별자 경로로 존재 확인. Kragel 연구실 2026 두 논문, 이전 bioRxiv 판, Zaffina 2026 preprint의 DOI와 저자를 Crossref로 확인.
* 본문 직접 확인 23편: Ma & Kragel 2026 두 편, Zaffina 2026, Westlin 2025, Shariatpanahi 2025, Du 2025, Ke 2025, Horikawa 2020, Du 2023, Chang 2021, Lettieri 2019, Camacho 2023, Gündem 2022, Asanuma 2025, Vinograd 2024, Finn 2020, Gauthaman 2024, Feilong 2023, Hyper-HMM 2023(5절), Thual 2022, Safaie 2023, Bernardi 2020, Huh 2024(6절).

**미확인**
* Gauthaman 2024, Hyper-HMM, Santoro 2023 원 코드, netrep, ssm, TEM 구현, Ke 2025 가중치 저장소의 라이선스(GitHub API 차단).
* Ma, Vafaie & Kragel 2025 리뷰 본문, Ma & Kragel bioRxiv 판 본문.
* 검색 결과로만 본 관련 항목(jsonl 미기재): "Representation-First Emotion Decoding from 7T fMRI"(NeurIPS 2025 가상 페이지), suspense 영화 Mapper 분석 bioRxiv(저자 미확인), Geniesse 등 self-viewing Mapper preprint, Radchenko 구면 affective space preprint. Round 2 전에 식별자 확인 필요.
* "이미 수행됨" 판단은 이번 검색 범위(Crossref, arXiv, PubMed, WebSearch) 안의 판단이다.

**CLAUDE.md 6절 점검 (이 에이전트 제안 전체에 적용)**
* 규범 평정(Horikawa, Emo-FilM consensus)과 본인 보고(Spacetop, Emo-FilM 사후 평정)를 섞지 않는다. 기하가 "정서 평정과 공변"한다는 결과는 "참가자의 정서 경험"이 아니라 "규범 평정과 공변하는 신경 구조"로 해석한다.
* 공유 기하 주장에는 표적 상속 null(P5)과 시각-의미 nuisance(C1, C2)를 함께 둔다.
* HRF 지연과 자기상관: 시간상수(C5), time-warp(C4) 추정은 감각 영역 대조와 개인 HRF 추정을 필수로 한다.
* 누수: 정렬 템플릿과 전이 행렬은 시험 피험자, 시험 영화나 자극을 빼고 만든다. Horikawa는 순서가 같아 순서 permutation을 쓴다.
* 다중비교: 영역 쌍(C6), rank 대역(C1), 영역 x γ(C2)에 대해 사전 지정 ROI와 FDR.
* 관찰 자료의 한계: C5의 attractor 해석은 기술적이며 인과 증거가 아니다. C3의 "개인화로 회복"도 상관 수준이다.
* 탐색 vs 확증: 모든 사슬은 탐색 단계다. 확증으로 가려면 Horikawa에서 발견한 것을 Emo-FilM 또는 Spacetop에서 사전등록 반복하는 구조가 필요하다(예: C1 발견 → NSD, Emo-FilM 재현).

**다른 에이전트와 연결될 지점 (Round 2 준비용 메모)**
* vision-decoding, encoding-foundation: C1, C2의 시각-의미 nuisance feature(최신 video, MLLM feature), Ma & Kragel R9.
* emotion-theory: C7의 범주 체계, U3의 이론 예측, Spacetop 파생 valence 지표의 타당성.
* multimodal-dynamics: C4, C5의 시간척도와 washout, Horikawa 무음 vs Emo-FilM 소리의 I7.
* systems-neuro: hippocampus 장축과 vmPFC ROI 정의(C2), 생리 잡음 처리(C4, C5).
* frontier-ai: I8 수렴 기울기의 모델 쪽 측정, MLLM 정서 기하(Du 2025, Asanuma 2025).
