# RQ-08. 장면을 말로 설명한 내용을 빼고 나도 뇌에 정서 신호가 남을까?

* 작성: llm-semantics (기원 LS-P1, 공동 VD-P3). 기준일 2026-11-12
* matrix: LIT-03 (경로: literature). 군집 K2(정서 신호와 지각, 의미 내용의 분리)
* 붙는 관문: RQ-13(정서와 장면 내용을 떼어 비교할 수 있는 정서 쌍의 지도)
* 근거 파일: `outputs/rq_landscape.md` 4절 RQ-08, `outputs/combinations/matrix.csv` LIT-03, `outputs/evaluation/prior_overlap_audit.md` 2절 RQ-08, `outputs/evaluation/reviewer_notes.md` 4.4절, `outputs/agents/adversarial-reviewer/round3_top10_review.md` 5절, `outputs/discussion/round3_summary.md`, `outputs/stage1/dataset_Horikawa.md`, `outputs/stage1/horikawa_factcheck_stage4.md`, `outputs/STAGE_STATUS.md` "사용자 답변, Stage 3 이후"

### 이 카드에서 쓰는 말

| 말 | 뜻 |
|---|---|
| 정서 배제 캡션 | Mind captioning 연구에서 크라우드 작업자가 "정서 반응은 쓰지 말고 보이는 내용만" 쓰도록 지시받고 적은 장면 설명 문장. 클립당 20개 |
| 규범 정서 평정 | fMRI 참가자가 아닌 다른 사람들(미국 MTurk 평정자)이 같은 클립을 보고 매긴 정서 평정의 평균. [Human-norm, felt] |
| 고유 분산 | 다른 feature를 모두 넣은 모형에서 한 feature 묶음(band)을 뺐을 때 줄어드는 예측력. "그 묶음만 설명하는 부분" |
| band | 같은 종류의 feature를 묶은 단위(예: 정서 평정 34개 = 정서 band) |
| banded ridge | band마다 규제 강도를 따로 정하는 선형 회귀. 뇌 encoding에 쓰는 표준 방법 |
| 교차 적합 잔차화 | 공변량을 빼는 회귀식을 학습용 자료에서만 만들고 시험용 자료에 적용해, 같은 자료로 빼고 평가하는 과적합을 막는 방법 |
| split-half 신뢰도 | 캡션 20개를 10개씩 둘로 나눠 만든 두 표상이 얼마나 일치하는지. 공변량의 측정 오차 크기를 알려 준다 |
| 역방향 분할 | 정서의 고유 분산뿐 아니라 캡션의 고유 분산도 같은 방식으로 재서 양쪽을 함께 보고하는 것 |
| V11 | 원 결과 재현. 새 분석 전에 원 논문의 수치를 같은 자료로 먼저 다시 얻는 단계 |

---

## 1. Core Research Question

* **(a) 한 줄 질문:** 장면을 말로 설명한 내용을 빼고 나도 뇌에 정서 신호가 남을까?
* **(b) 검증 가능한 세부 질문:** 사람이 정서 단어 없이 쓴 장면 설명(클립당 20개)의 의미를 측정 오차까지 보정해 통제한 뒤에도, 규범 정서 평정이 뇌 반응을 따로 설명하는 부분(고유 분산)이 무작위 feature 기준선보다 크게 남는가, 남는다면 어느 영역이며 서로 다른 두 코호트(Horikawa 2020, Mind captioning)에서 같은 영역에 나타나는가?

## 2. Scientific Motivation

* Horikawa 2020은 정서 모형이 시각 객체 모형과 73개 의미 개념 모형보다 transmodal 영역(IPL, TE, 전두 영역)을 더 잘 예측한다고 보고했다. 그러나 세 모형을 **따로** 적합해 비교했고, 함께 넣어 고유 분산을 나누지는 않았다(literature_db 기록, doi:10.1016/j.isci.2020.101060).
* Du 2023은 같은 자료에 정서 평정, motion energy, 73개 의미 평정을 banded ridge로 함께 넣었다. 그래도 저자들은 "시각, 의미 feature의 교란이 남을 수 있어 더 나은 패러다임이 필요하다"고 한계로 적었다(doi:10.1016/j.isci.2023.107571, Limitations 셋째 항목, 본 에이전트 본문 확인).
* 공변량이 거칠거나 측정 오차가 있으면 "다른 것을 통제해도 남는다"는 주장의 거짓 양성률이 매우 높아진다(doi:10.1371/journal.pone.0152719). 73개 예/아니오 개념은 장면 의미를 담기에 거칠다.
* 장면 설명 문장의 언어 모형 표상은 고차 시각피질 반응을 잘 설명한다(doi:10.1038/s42256-025-01072-0, Discussion 첫째, 둘째 단락). 그렇다면 "정서 표상"으로 보고된 신호의 상당 부분이 말로 설명 가능한 장면 의미일 수 있다.
* Mind captioning은 같은 Cowen & Keltner 클립에 **정서를 쓰지 말라는 지시로 받은 인간 캡션 20개**를 제공한다(doi:10.1126/sciadv.adw1464, Materials and Methods 'Caption annotation'과 Discussion 한계 단락, 본 에이전트 본문 확인). 이 캡션은 풍부하고, 20개라 측정 오차를 직접 잴 수 있다.
* **지식의 공백:** 의미 공변량을 풍부하게 하고 측정 오차를 보정했을 때 정서 고유 분산이 얼마나 남는지, 그것이 독립 코호트에서 같은 곳에 나타나는지는 아무도 보고하지 않았다(Stage 4 감사, 아래 5절).

## 3. Origin of the Idea

* **에이전트 경로:**
  * llm-semantics Round 1 Chain 1(정서 배제 기술의 잔차)과 미해결 문제 P2(description confound)
  * vision-decoding Round 1 R6(정서 배제 인간 캡션을 통제한 뒤 남는 정서 분산)
  * Round 2: LS-P1(llm-semantics → vision-decoding)과 VD-P3(vision-decoding → llm-semantics)이 같은 질문으로 합쳐짐
  * Round 3: frontier-ai와 geometry-info 검토가 "측정 오차는 정서를 부풀리고 과통제는 정서를 지운다"는 맞교환을 지적. 대응으로 split-half 보정, 교차 적합, 역방향 분할, 다중 text encoder, AI 재작성 단계 분리
  * adversarial-reviewer 상위 10개 검토: Abdel-Ghaffar 2024 선행 누락, band 차원 비대칭, 원본 영상 단위 누수, 원 결과 재현(V11) 보완
  * Stage 4 선행 중복 감사: 가장 가까운 선행 Du 2023을 새로 찾음
* **가져온 분야:** NeuroAI(캡션 언어 모형 표상과 시각피질 정렬, Doerig 2025), 심리측정과 통계(공변량 측정 오차, Westfall & Yarkoni 2016), 뇌 decoding(Mind captioning의 정서 배제 캡션)
* **조합 ID:** LIT-03. Axis C(Description Residual), F, H, U, I

## 4. Prior Literature

모든 논문은 `outputs/literature/literature_db.csv`에서 verified이거나 본 에이전트 `literature.jsonl`에 식별자로 확인해 넣은 것이다. "읽은 범위"는 본 에이전트가 직접 읽은 범위다.

| # | 논문 | ID | 읽은 범위 | 이 질문에 주는 기여 |
|---|---|---|---|---|
| 1 | Du et al. 2023, Topographic representation of visually evoked emotional experiences in the human cerebral cortex, iScience | doi:10.1016/j.isci.2023.107571 | 본문(Methods, Results 일부, Limitations, PMC) | **가장 가까운 선행.** 같은 Horikawa 자료에 정서 34 + motion energy 6,555 + 의미 73의 banded ridge. 평균 21% 피질 voxel 유의, TPJ 43~62%. 고유 분산은 보고하지 않음. 남은 교란을 한계로 명시 |
| 2 | Horikawa et al. 2020, iScience | doi:10.1016/j.isci.2020.101060 | DB 기록(본문, 다른 에이전트 확인), Stage 1 보고서 | 원 결론. 정서 대 시각 객체 대 73 의미 모형을 따로 적합. 반복 제시 없음, 라벨은 별도 평정자, 자유 시청 |
| 3 | Abdel-Ghaffar et al. 2024, Nat Commun | doi:10.1038/s41467-024-49073-8 | DB 기록(본문, 다른 에이전트 확인) | 정서 이미지에서 후두측두 피질이 의미와 정서 feature에 **함께** tuning. 정서와 의미가 같은 영역에 겹친다는 직접 선행. mid-level 구조 feature는 통제하지 않았다고 저자가 적음 |
| 4 | Horikawa 2025, Mind captioning, Sci Adv | doi:10.1126/sciadv.adw1464 | 본문 | 정서 배제 캡션 20개/클립, 일본어 모국어 참가자 6명, 72개 클립 5회 반복, 언어 모형 feature로 장면 의미 decoding |
| 5 | Doerig et al. 2025, Nat Mach Intell | doi:10.1038/s42256-025-01072-0 | 본문 | 캡션 언어 모형 표상이 고차 시각피질을 잘 설명. "어떤 다른 측면이 LLM 표상에 담기는지"를 미래 과제로 둠 |
| 6 | Westfall & Yarkoni 2016, PLoS One | doi:10.1371/journal.pone.0152719 | DB 기록(본문, 다른 에이전트 확인) | 공변량 신뢰도가 불완전하면 "통제 후에도 남는다"는 주장의 거짓 양성률이 커지고 표본이 클수록 더 커짐 |
| 7 | Dupré la Tour et al. 2022, NeuroImage | doi:10.1016/j.neuroimage.2022.119728 | DB 기록(본문, 다른 에이전트 확인) | banded ridge와 variance partitioning, product measure. 선택 해제가 "표상 없음"을 뜻하지 않음 |
| 8 | Du et al. 2025, arXiv | arXiv:2509.24298 | 본문 | MLLM triplet embedding이 규범 평정보다 뇌를 잘 예측. 같은 캡션을 LLM 입력으로 씀. 정서 배제 기술 기준선과의 비교는 없음 |
| 9 | Gauthaman et al. 2024, arXiv | arXiv:2409.06843 | DB 기록(본문, 다른 에이전트 확인) | 개인 간 공유 스펙트럼 방법. 잔차 voxel의 공유 성분 분석에 씀 |
| 10 | Golan et al. 2020, PNAS | doi:10.1073/pnas.1912334117 | DB 기록(본문, 다른 에이전트 확인) | 두 모형이 다르게 예측하는 자극(controversial)으로 모형을 판별 |
| 11 | Kragel et al. 2019, Sci Adv (EmoNet) | doi:10.1126/sciadv.aaw4358 | DB 기록 | 같은 C&K 영상 프레임으로 학습되어 이 질문의 feature로 쓰면 학습-평가 누수. **사용 제외 근거** |
| 12 | Mohammed et al. 2026, EmoMind, arXiv | arXiv:2605.16739 | 본문 | Mind captioning 자료와 같은 캡션으로 정서 캡션 생성. 이 자료가 이미 분석에 노출되었음을 보여 줌(사전 등록 필요성) |

## 5. Novelty

* **감사 판정: partially**(`prior_overlap_audit.md` 2절 RQ-08).
* **이미 수행된 것(새로움으로 주장하지 않음):**
  * 같은 Horikawa 자료에서 정서와 의미 공변량을 함께 넣은 banded ridge(Du 2023).
  * 정서와 의미가 후두측두 피질에 함께 tuning된다는 관찰(Abdel-Ghaffar 2024).
  * "정서 표상이 의미와 구분된다"를 처음 보이는 연구가 아니다.
* **남는 새 부분(감사의 네 가지):**
  1. 공변량이 사람이 쓴 정서 배제 장면 설명 20개다. 73개 예/아니오 개념보다 훨씬 풍부하다.
  2. 캡션 split-half로 공변량의 측정 오차를 재고 보정한다.
  3. 정서 고유 분산을 명시적으로 추정하고 역방향(캡션 고유 분산)도 함께 보고한다. Du 2023은 고유 분산을 보고하지 않았다.
  4. 독립 코호트(Mind captioning 6명)에서 같은 지도를 재현한다.
* **질문의 범위:** Du 2023의 Limitations가 직접 요구한 다음 단계, 즉 "의미 공변량을 풍부하게 하고 측정 오차를 보정하면 정서 고유 분산은 얼마나 남는가"만 묻는다.

## 6. Proposed Dataset

| 필요한 것 | 있는가 | 근거와 주의 |
|---|---|---|
| Horikawa 2020 fMRI(5명, 클립당 1 sample로 블록 평균, native volume, HCP360 + 피질하 ROI) | 있음 | Stage 1 G2. 4 s shift 후 블록 평균, 블록 뒤 2 s 휴지. 원시 BIDS도 있음(재전처리 가능) |
| Mind captioning fMRI(6명, 학습 클립 각 1회, 시험 72클립 5회 반복) | 있음(사용자 보유, 전처리 완료) | 저장소 파일 세부와 사용자 전처리 방식은 미확인. 논문 기준 학습 2,108클립 + 시험 72클립 = 2,180 |
| 규범 정서 평정 34범주(선택 비율) + 14차원 | 있음 | figshare features. [Human-norm, felt], 평정자 개인 자료는 비공개. 두 코호트가 같은 클립이라 같은 라벨을 씀 |
| 73개 의미 개념 평정, vision 1,000차원 feature | 있음 | figshare. 73개는 사람 주석, 1,000차원 DNN 이름은 미확인. V11 재현에 필요 |
| 정서 배제 인간 캡션 20개/클립 | 있음(사용자 확인) | 파일 형식과 클립 ID 대응은 미확인. Mind captioning 시험 72클립은 평가 블록과 회상 cue로도 쓰였다 |
| 원본 영상(motion energy, 영상 모형 feature 추출용) | 있음(사용자 보유, 2,185클립 모두 무음) | G1 필요. 재배포 제한 가능성(Mind captioning 본문이 저작권 때문에 프레임을 그림으로 대체) |
| 두 코호트 클립 ID 대응표 | 미확인 | 둘 다 2,196 제시 ID에서 중복을 뺐으나 Horikawa 코드는 15개, Mind captioning은 16개를 뺐다. 0단계에서 대응을 확인 |
| 원본 영상 출처(같은 원본에서 잘린 클립인지) | 없음 | 지각 해시와 영상 embedding으로 근접 중복 군집을 만들어 대리로 쓴다 |
| Mind captioning 평가 블록 위치(어느 클립 직후 캡션 5개가 제시되었나) | 미확인(events 파일에서 확인 필요) | reviewer_notes 4.4절: run마다 평가 블록 3~4개 |
| noise ceiling(잡음 상한) | Mind captioning 시험 72클립만 | Horikawa는 반복 제시가 없어 상한 없음 |
| 참가자 본인 정서 보고 | 없음 | 두 코호트 모두. 결론은 규범 정서 평정과의 공변으로 한정 |
| 시선(eye tracking) | 없음 | 두 코호트 모두 자유 시청. 교란으로 남는다 |
| 참가자 언어 | Mind captioning: 일본어 모국어(본문). Horikawa 2020: 사용자 확인으로 일본인(원문 미기재) | 평정자(미국 영어 사용자)와 언어, 문화가 다를 수 있다 |
| 두 코호트 피험자 중복 | 겹치지 않음(사용자 확인, 원문 미기재) | 독립 코호트로 취급 |

## 7. Proposed Computational Framework

* **Pretrained model**(공개 모델 먼저. 모델을 새로 학습하지 않는다)
  * 문장 encoder 셋 이상: DeBERTa-large(Mind captioning이 쓴 모형), 문장 embedding 전용 모형 하나, 공개 LLM 하나(예: Llama 3.1 8B 또는 Qwen2.5 7B의 중간층 평균). 라이선스는 이번 세션에서 확인하지 않았다(**미확인**). 여러 encoder를 쓰는 이유는 결론이 한 모형의 성질이 되지 않게 하기 위해서다.
  * 저수준 시각: motion energy(Du 2023과 같은 Gabor 필터 방식).
  * 영상 모형 하나(예: 공개 video encoder). checkpoint 라이선스 **미확인**.
  * **쓰지 않는 모형:** EmoNet(같은 C&K 프레임으로 학습되어 누수, doi:10.1126/sciadv.aaw4358).
* **Input representation**
  * 정서 band: C&K 34범주 선택 비율(주), 14차원 평균(보조).
  * 캡션 band: 클립마다 캡션 20개의 encoder 표상 평균. 주 분석은 PCA 34차원(정서 band와 차원을 맞춤), 민감도 분석은 64차원과 전체 차원. split-half 분석용으로 10개씩 두 묶음의 평균도 만든다.
  * 시각 band: motion energy, vision 1,000차원(V11용), 영상 모형 표상(PCA로 차원 제한).
  * 의미 73 band: V11 재현과 비교용.
* **Output / target representation:** 클립별 블록 평균 BOLD(voxel 또는 HCP360 parcel). Horikawa는 제공 전처리본, Mind captioning은 같은 규약(4 s shift 후 블록 평균)으로 맞춘다.
* **Training or adaptation strategy:** 모든 pretrained model은 고정(feature 추출만). 피험자마다 banded ridge를 학습한다. 교차검증 fold는 근접 중복 군집과 run 단위로 묶는다. 캡션 잔차화는 학습 fold 안에서만 회귀식을 만든다(교차 적합).
* **Relevant brain regions / networks:** 전뇌. 사전 지정 ROI는 (1) Horikawa 2020과 Du 2023에서 정서 모형이 우세했던 transmodal 영역(IPL, TPJ, TE, 내측과 외측 전전두, 쐐기앞소엽), (2) 후두측두 피질(Abdel-Ghaffar 2024), (3) 섬엽, (4) amygdala와 피질하(신호 품질 점검 후 탐색적). 영역 선택은 V11 단계의 원 논문 결과로 미리 고정하고 이번 잔차 결과로 다시 고르지 않는다.
* **Loss function or statistical objective:** band별 규제 강도가 다른 ridge의 제곱 오차. 평가는 보류 클립에서 예측과 실측의 상관(r)과 설명 분산(R²). 고유 분산 = 전체 모형 R² - 해당 band를 뺀 모형 R². 측정 오차 보정은 (1) split-half 신뢰도로 감쇠 보정, (2) 한쪽 반 캡션으로 다른 쪽 반을 대리하는 도구변수식 민감도 분석.
* **Interpretability method:** 양방향 variance partitioning과 product measure(doi:10.1016/j.neuroimage.2022.119728), 정서 잔차가 남는 범주의 가중치 지도, 정서 모형과 캡션 모형이 가장 다르게 예측하는 controversial 클립 집합(doi:10.1073/pnas.1912334117), 잔차 voxel의 개인 간 공유 스펙트럼(arXiv:2409.06843), 캡션의 정서 함축 감사(아래 8절 0c).

## 8. Proposed Analyses

### 0단계 (전제 확인, 결과에 따라 진행 여부 결정)
* **0a. 원 결과 재현(V11).**
  * Horikawa 2020의 정서 대 vision 1,000 대 의미 73 개별 모형 비교: 정서 모형 우세 영역(IPL, TE, 전두)을 재현.
  * Du 2023의 banded ridge(정서 34 + motion energy + 의미 73): 평균 약 21% 피질 voxel 유의, TPJ 비율이 가장 높은 패턴을 재현.
  * 두 결과를 Horikawa 코호트에서 먼저, 같은 절차로 Mind captioning 코호트에서 다시 얻는다. 재현이 크게 어긋나면 원인(전처리, fold, 중복 처리)을 찾기 전에는 1단계로 가지 않는다.
* **0b. 관문 RQ-13(분리 가능성 지도).** 내용이 비슷한 클립끼리 짝지을 수 있는 정서 쌍과 없는 정서 쌍을 표시한다. 짝을 거의 못 찾는 정서 범주는 이 질문의 범주별 결론에서 "이 자료로 식별 불가"로 적는다.
* **0c. 캡션 감사.**
  * 캡션 20개의 split-half 신뢰도를 PCA 성분마다 계산한다.
  * 명시적 정서 어휘가 들어간 캡션 비율을 사전 기반으로 센다.
  * 캡션만 읽고 정서를 추정한 값을 LLM reader 모드로 만든다 [AI-est, perceived affective quality]. 캡션이 정서를 얼마나 **함축**하는지 보고하는 용도이며 라벨로 쓰지 않는다.
* **0d. 누수 경로 정리.** 클립 ID 대응, 근접 중복 군집, 중복 클립 15/16개, 평가 블록 클립 목록, 모형 사전학습 자료 등록부(C&K 공개 interactive map, Mind captioning 캡션 공개 시점과 모형 출시 시점).

### 1단계 (주 분석)
* **주 비교:** 의미 band를 73개 개념에서 정서 배제 캡션(34차원)으로 바꿨을 때 정서 고유 분산이 얼마나 줄어드는가. 그리고 측정 오차를 보정한 뒤 얼마나 남는가. 이것이 주 산출물이다.
* **함께 보고하는 것:** 캡션 고유 분산(역방향), 정서와 캡션의 공유 분산, motion energy와 영상 모형 band의 고유 분산.
* **비교 조건:**
  * 기준선 1: 차원을 맞춘 무작위 feature band(34차원)로 바꿔도 정서 고유 분산이 그만큼 줄어드는가(V1).
  * 기준선 2: 캡션을 다른 클립과 섞어 짝을 깬 band(셔플 null).
  * 양성 대조: 같은 절차로 motion energy의 고유 분산이 초기 시각피질에서 검출되는가. 검출되지 않으면 절차를 고친다.
  * 회복 시뮬레이션(V5): 실제 feature와 실제 캡션 측정 오차를 써서, 알려진 크기의 "정서만의 신호"를 심은 가짜 voxel을 만들고 절차가 그것을 회복하는지 본다.
* **Ablation:** encoder 종류(3개 이상), 캡션 차원(34, 64, 전체), 캡션 수(5, 10, 20개), 정서 band 종류(34범주 대 14차원).
* **민감도 분석:** Mind captioning에서 평가 블록 직후 캡션 5개가 제시된 클립을 뺀다(reviewer_notes 4.4절). 영상 저수준 saliency feature를 추가한다(시선 교란의 부분 대리).
* **통계 검정:** 클립 단위 bootstrap으로 신뢰구간, 피험자별 결과와 유병률(5명, 6명 중 몇 명), parcel 다중 비교는 FDR. Mind captioning 시험 72클립에서는 noise ceiling 대비 비율도 보고하되 구간이 넓다는 점을 같이 적는다.
* **Validation strategy:** Horikawa 코호트를 발견용, Mind captioning 코호트를 확인용으로 미리 정한다. 확인용 코호트에서는 발견용에서 고른 parcel만 검정한다. 분석 계획과 주 경로를 시작 전에 고정한다(V10). Mind captioning은 이미 다른 연구(EmoMind)와 사용자 전처리로 노출되었으므로 고정 시점을 기록한다.

### 2단계 (보조, 결론과 분리)
* 정서 잔차가 남는 voxel의 개인 간 공유 스펙트럼.
* controversial 클립 집합에서 정서 대 캡션 모형의 판별.
* 캡션을 정서 언어로 다시 쓴 AI 재작성 band [AI-est]. 주 결론에서 분리해 탐색 결과로만 보고한다.

### 반증 조건 (Falsifiability)
* **가설("말로 설명한 장면 의미로 회복되지 않는 규범 정서 공변이 있다")이 지지되지 않는 경우:**
  * 측정 오차를 보정한 정서 고유 분산이 사전 지정 ROI 모두에서 차원 맞춘 무작위 band 기준선과 구분되지 않는다.
  * 또는 한 코호트에서만 나타나고 확인용 코호트의 같은 parcel에서 재현되지 않는다.
  * 또는 encoder 셋 중 하나에서만 나타난다.
* **절차가 무효가 되는 경우(결론을 내지 않고 고친다):** 양성 대조 실패, 회복 시뮬레이션에서 심은 신호를 회복하지 못함, V11 재현 실패.
* **해석 경계:** 고유 분산이 0이라도 "정서가 없다"가 아니라 "이 자료의 정서 평정 공변이 장면 설명 의미로 운반된다"이다.

## 9. Competing Explanations

| 대안 해석 | 그것을 가르는 분석 |
|---|---|
| 남는 정서 분산은 캡션의 측정 오차 때문이다(과소 통제) | split-half 감쇠 보정, 교차 적합 잔차화, 캡션 수(5, 10, 20)에 따라 잔차가 줄어드는 곡선, 회복 시뮬레이션 |
| 캡션 band가 차원이 커서 정서를 다 흡수했다(과통제) | 차원 맞춘 34차원 band를 주 분석으로, 역방향 분할로 캡션 고유 분산도 보고, 무작위 band 기준선 |
| 남는 분산은 캡션에 안 쓰인 시각 정보(움직임, 색, 얼굴, 시선)다 | motion energy, 영상 모형 band, saliency feature를 함께 넣는다. 그래도 남는지 본다. 시선은 측정이 없어 완전히 배제하지 못한다(한계) |
| 캡션은 "정서를 쓰지 말라"는 지시 때문에 정서와 관련된 세부를 빠뜨렸다 | 0c 캡션 감사(명시적 정서 어휘, 캡션이 함축하는 정서). 함축 정서가 큰 클립과 작은 클립에서 잔차를 나눠 본다 |
| 남는 분산은 같은 원본 영상에서 잘린 클립끼리의 누수다 | 근접 중복 군집 단위 fold, 중복 클립 처리 |
| Mind captioning의 남는 분산은 평가 블록에서 캡션을 읽은 반응이 섞인 것이다 | 해당 클립 제외 민감도 분석 |
| 정서 범주 쌍에 따라 내용과 정서가 원래 분리되지 않는다 | RQ-13 분리 가능성 지도로 범주별 결론 범위를 제한 |
| 남는 분산은 정서가 아니라 평정 형식(선택 비율)이나 평정자 문화의 특성이다 | 14차원 평균을 대안 목표로 반복. 문화 차이는 이 자료로 가를 수 없음(한계로 기록) |

## 10. Potential Findings

1. **정서 고유 분산이 73개 개념 대비 크게 줄고, 보정 후 거의 사라진다.** Horikawa 2020과 Du 2023이 정서 표상으로 본 transmodal 지도의 대부분은 말로 설명 가능한 장면 의미와 공변한다. 원 결론의 해석 범위를 좁히는 결과다.
2. **줄지만 일부 영역(예: 섬엽, amygdala, 일부 전전두)에서 두 코호트 모두 남는다.** 그 영역에 "언어 기술로 회복되지 않는 규범 정서 공변"이 있다. 이것이 몸 상태, 평가, 시선 중 무엇인지는 이 설계로 가를 수 없고, RQ-09(설계 통제)와 생리 자료가 있는 Emo-FilM 질문으로 넘긴다.
3. **후두측두 피질에서 남는다.** Abdel-Ghaffar 2024의 "의미와 정서 공동 tuning"이 캡션 수준 의미로도 지워지지 않는다는 뜻이다. 다만 시각 band가 놓친 mid-level feature일 가능성을 함께 적는다.
4. **한 코호트에서만 남는다.** 코호트 특이 결과로 보고하고 일반화하지 않는다.
5. **절차가 실패한다(V11 재현 실패, 양성 대조 실패).** 원 결과의 재현성 자체에 대한 정보가 된다(Westlin 2025 재분석 논쟁과 연결).

## 11. Scientific Contribution

* 정서 신경과학의 핵심 쟁점 중 하나인 "정서 표상이 의미 표상과 구분되는가"에 대해, 측정 오차를 고려한 판정 기준을 처음으로 이 자료에 적용한다.
* 범주 이론과 구성주의 논쟁에 직접 답하지는 않는다. 대신 두 진영이 근거로 쓰는 Horikawa 계열 지도가 **어디까지 정서이고 어디부터 장면 의미인지**를 정해, 이후 해석의 범위를 조정한다.
* 결과 1이면 "transmodal 정서 지도 = 말로 설명 가능한 상황 의미의 지도"라는 해석이 강해지며, 정서를 상황 개념화로 보는 관점과 잘 맞는다. 결과 2이면 장면 의미로 환원되지 않는 성분의 위치가 특정되어 내수용, 평가 처리 가설을 시험할 표적이 생긴다.
* 방법 면에서는 "통제 후에도 남는다" 유형의 주장에 공변량 신뢰도 보정과 양방향 분할을 함께 보고하는 표준을 제안한다. 같은 캡션을 쓰는 RQ-44(회상), RQ-09(설계 통제)의 공통 기반이 된다.

## 12. Limitations & Risks

* **라벨:** 규범 정서 평정은 fMRI 참가자의 경험이 아니다. 결론은 "참가자 뇌가 규범 정서와 공변하는 정도"로 한정한다.
* **피험자 수:** 5명 + 6명. 개인차 결론은 내지 않는다.
* **반복 제시 없음(Horikawa):** noise ceiling이 없다. Mind captioning 72클립 ceiling은 구간이 넓다.
* **자유 시청과 시선:** 두 코호트 모두 시선 측정이 없다(Horikawa 2020 Discussion 마지막 단락, adversarial-reviewer 기록).
* **문화와 언어:** 평정자는 미국 영어 사용자, 참가자는 일본어 화자. 캡션은 영어이며 모형 입력으로만 쓴다.
* **공변량의 완전성:** 어떤 캡션 band도 장면 의미를 다 담지 못한다. 결과 2의 "남는 분산"은 언제나 "이 공변량으로 회복되지 않는 부분"이다.
* **선형 가정:** ridge는 선형이다. 비선형 관계는 놓친다.
* **블록 평균:** 짧은 클립을 반복 재생한 블록 평균이라 클립 안의 시간 변화는 다루지 않는다.
* **분석 노출:** Mind captioning 자료는 EmoMind와 사용자 전처리로 이미 노출되었다. 사전 고정 시점을 기록한다.
* **모형 사전학습 오염:** 캡션이 2025년 공개되었으므로 최신 encoder가 캡션 문장을 학습했을 수 있다. 모형 출시 시점과 함께 등록한다. 텍스트 encoder는 영상을 보지 않으므로 C&K 지도의 범주 라벨 노출 위험은 작다.
* **라이선스:** encoder, 영상 모형 checkpoint 라이선스 미확인. C&K 영상의 재배포 조건 미확인(feature 추출만 하고 영상은 배포하지 않는다).

## 13. Pilot Experiment

* **가장 작은 분석:** Horikawa 5명에서 V11(두 원 결과) 재현 + 캡션 split-half 신뢰도 계산 + 사전 지정 transmodal ROI에서 의미 73 band 대 캡션 34차원 band의 정서 고유 분산 비교(보정 전, 후).
* **필요한 것:** figshare 전처리본과 features, 캡션 파일, 클립 ID 대응표, motion energy(원본 영상). 계산은 CPU 또는 GPU 1장으로 충분하다(캡션 embedding 2,180 x 20문장, ridge는 피험자당 수 시간 규모로 추정).
* **진행 기준:** V11이 재현되고 양성 대조가 통과하면 Mind captioning으로 확장한다. 캡션 band로 바꿔도 정서 고유 분산이 73 band와 같다면 캡션 감사(0c)를 먼저 확인한다(캡션이 정보를 거의 더하지 않는 경우).
* `outputs/evaluation/selection.md` 6절 Pilot P1과 같은 내용이다.

## 14. Feasibility & Priority

* **점수(`outputs/evaluation/scores_final.csv`, 1~5):** Novelty 3, Neuroscientific Importance 5, AI / Modeling Contribution 3, Dataset Feasibility 5, Methodological Rigor 4.5, Falsifiability 4, Interpretability 4, Generalizability 3.5, Feasibility 5. **합계 37.0(1위)**, 과학 기준 5개 합 20.5(1위).
* **순위:** Substantive Shortlist 1번, High-priority Candidates 1위, Recommended Pilot P1(관문 RQ-13과 함께).
* **계산 자원:** 미확인. GPU 1~4장 가정에서 충분하다(모형 학습 없음).
* **overlap:**
  * **EmoBrain(구 EmoViS 범위):** 직접 겹침. 정서 기하의 sensory-semantic 기원 분석과 같은 물음이다.
  * **Emo-FilM 연구:** 겹침 없음(Horikawa 계열 자료만 사용).

---

## 반영하지 않은 지적

| 지적 | 출처 | 반영하지 않은 이유 |
|---|---|---|
| fMRI 신호로 시선(안구 움직임)을 복원해 회귀하기 | `outputs/discussion_record.md` 3.1절 1번의 대응 목록 | 해당 도구를 검증한 문헌을 literature_db에서 확인하지 못했고, 두 코호트 EPI 시야에 안구가 들어가는지 미확인이다. 대신 saliency feature로 부분 대리하고 시선 교란을 한계로 남긴다 |
| 공변량 측정 오차를 잠재변수 모형(SEM)으로 직접 모형화하기 | Westfall & Yarkoni 2016(doi:10.1371/journal.pone.0152719)의 권고 | 수백 차원 embedding에 잠재변수 모형을 그대로 적용하기 어렵다. split-half 감쇠 보정, 교차 적합, 도구변수식 민감도 분석으로 부분 반영했다 |
| 의미 고정 편집(설계 통제)과 같은 voxel에서 맞대기 | GC-P2(generative-counterfactual) | 이 카드의 범위를 넘는다. RQ-09로 분리되어 있고, RQ-08 결과(잔차 voxel)가 RQ-09의 입력이 된다. 순환을 피하려면 voxel 정의와 encoder 학습 코호트를 나눠야 한다는 지적은 RQ-09에 넘긴다 |

---

## Safeguards 점검

| 항목 | 이 질문에서의 처리 |
|---|---|
| 참가자 경험 vs 자극에 묘사된 정서 | 목표는 별도 평정자의 felt 규범 평정. 참가자 경험이 아니며 묘사 정서도 아니다 |
| 인간 평정 vs 모델 생성 평정 | 주 분석은 인간 평정만. LLM reader 정서 추정과 AI 재작성 캡션은 [AI-est]로 분리, 결론에 쓰지 않음 |
| 본인 보고 vs 규범 평정 | 본인 보고 없음. 결론 동사는 "규범 정서와 공변" |
| 정서 표상 vs 시각, 의미 내용 표상 | 이 질문의 주제. 캡션, 시각, 영상 band와 양방향 분할 |
| encoding 정확도 vs 설명적 적절성 | 고유 분산이 남아도 "정서를 표상한다"가 아니라 "이 공변량으로 회복되지 않는 공변" |
| decodability vs 표상 vs 인과 | R0 관찰 분석. 인과 주장 없음 |
| in-silico vs 관찰 | 관찰만 |
| 공유 표상 vs 데이터셋 특이 교란 | 두 코호트(다른 장소, 스캐너, 참가자) 재현을 확인 기준으로 |
| 탐색 vs 확인 | Horikawa 발견, Mind captioning 확인. 2단계와 AI 재작성은 탐색 |
| HRF 지연과 시간 자기상관 | 블록 평균(4 s shift). 블록 뒤 휴지 2 s로 인접 블록 섞임 가능. run 단위 fold |
| 자극, 영상, 피험자 단위 누수 | 근접 중복 군집 fold, 중복 클립 처리, 코호트 간 확인 |
| 반복 자극 교란 | 짧은 클립 반복 재생, Mind captioning 시험 클립 5회 반복은 ceiling에만 사용 |
| 평정자 일치와 라벨 잡음 | 범주별 평정자 일치 미확인(평정자 개인 자료 비공개). 14차원으로 반복 |
| 시각-의미-정서 공선성 | 이 질문의 핵심. 차원 맞춤 band, 무작위 band null |
| 시공간 해상도 | TR 2 s(Horikawa), 1 s(Mind captioning), 블록 단위 분석 |
| ROI 선택과 순환 추론 | ROI는 V11 원 결과로 고정, 확인 코호트는 발견 코호트가 고른 parcel만 검정 |
| 다중 비교 | parcel FDR, 피험자 유병률 |
| 자료 접근, checkpoint 라이선스 | 자료 보유(사용자 확인). checkpoint 라이선스 미확인 |
| 사전학습 오염 | EmoNet 제외. encoder 출시 시점과 캡션 공개 시점 등록 |
| 데이터셋 간 주석 비호환 | 두 코호트가 같은 클립, 같은 라벨이라 해당 없음. 클립 ID 대응은 확인 필요 |
| **label-provenance** | 대상 felt, 주체 별도 평정자 규범(C&K). 캡션: 별도 작업자의 시각 내용 기술(정서 배제 지시). AI 추정 항목은 분리 표기 |
| **evidence-level** | R0 |
| **insilico-vs-observed** | 관찰 |
| **G1** | 캡션과 라벨만 쓰는 분석은 불필요. motion energy, 영상 모형 feature는 필요(보유) |
| **signal-feasibility** | 피질 parcel은 양호. amygdala와 피질하는 3T, 2 mm(Horikawa), 2 mm(Mind captioning)에서 tSNR 점검 후 탐색적 |
| **minimum-validation (V1~V12)** | V1 무작위 band null ○, V2 상한(Mind captioning 72클립만) △, V3 클립 단위 bootstrap과 셔플 null ○, V4 캡션 split-half ○, V5 회복 시뮬레이션 ○, V6 encoder 3개 이상 ○, V7 누수 등록부 ○, V8 두 코호트 ○, V9 AI 라벨 분리 ○, V10 사전 고정 ○(노출 기록 포함), V11 원 결과 재현 ○, V12 반증 해석 사전 기술 ○ |
