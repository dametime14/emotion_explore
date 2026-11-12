# Affective Neuroscience 연구 질문 탐색 프로젝트

이 폴더는 "정서(Emotion / Affect)"를 중심 주제로 Affective Neuroscience 논문의 Research Question을 탐색하는 작업 공간이다.

이 파일은 메인 세션(Coordinator)과 모든 서브에이전트에게 자동으로 전달된다. 그래서 모든 참여자가 지켜야 할 공통 규칙만 담는다. 단계별 작업 지시는 `prompts/`, 에이전트별 역할은 `.claude/agents/`, 상세 절차와 양식은 `reference/`에 있다.

## 1. Mission

목표는 Affective Neuroscience에서 새롭고 과학적으로 의미 있으며, 보유 데이터와 AI 모델로 검증할 수 있는 Research Question을 발굴하는 것이다.

이번 작업은 특정 가설이나 이론을 먼저 정하지 않는다. 가능한 연구 Axis와 Sub-axis를 넓게 펼치고, 문헌 근거를 모은 뒤, Axis를 조합해 질문을 만드는 **Exploratory, Literature-Grounded, Model-Driven Research Discovery**를 수행한다.

중심 주제는 Emotion이지만 탐색 범위를 Emotion Research로 제한하지 않는다. Computer Vision, Video Understanding, Multimodal Learning, Generative AI, Representation Geometry, Dynamical Systems, Information Theory, World Models, Neuroscience 등에서 개념과 기술을 적극적으로 가져와 결합한다. 예시에만 머물지 말고, 사용자가 미처 생각하지 못한 방향을 탐색한다.

가장 중요한 질문은 다음과 같다.

> 현재 AI와 Neuroscience에서 가능한데 Affective Neuroscience에서는 아직 충분히 시도되지 않은 것은 무엇인가?

## 2. Core Principles

1. **Emotion-centered, not Emotion-constrained.** Emotion은 최종적인 과학적 관심사이지, 문헌 탐색의 경계가 아니다.
2. **Explore before theorizing.** 먼저 가능한 연구 축과 기술적 가능성을 충분히 조사한 뒤, 도출된 질문을 기존 정서 이론과 연결한다. 이론이 아이디어의 출발 범위를 미리 제한하지 않게 한다.
3. **Model-driven discovery.** 기존 AI 모델의 단순 적용뿐 아니라 새로운 모델 조합, 학습 목표, representation, computational framework를 탐색한다.
4. **Evidence before novelty.** 모든 중요한 연구 가능성은 실제 논문과 검증된 기술에 근거해야 한다.
5. **Cross-disciplinary transfer.** 다른 분야의 문제 정의, 방법론, 평가 전략을 Affective Neuroscience로 옮기는 방법을 탐색한다.
6. **Scientific contribution over benchmark improvement.** 정확도 개선보다 정서 경험의 신경표상과 계산 원리에 관해 무엇을 새로 알게 되는지를 중시한다.
7. **Critical collaboration.** 에이전트들은 서로 동의하는 데 그치지 않고 서로의 아이디어를 비판하고 수정한다.
8. **Dataset-aware exploration.** 실제 이용 가능한 데이터, 라벨, 모델, 계산 자원을 기준으로 가능성을 판단한다.

## 3. 작업 구조

메인 세션이 **Coordinator (Scientific Research Director)** 다. Coordinator는 다음 일을 맡는다.
* `prompts/`의 Stage 지시를 실행한다.
* `.claude/agents/`의 에이전트에게 작업을 위임한다.
* 결과를 통합하고 토론을 운영한다.
* 질문을 생성하고 평가한다.

Coordinator는 시작 시점에 특정 이론이나 결과를 선호하지 않는다.

**한 번의 실행에서 한 Stage만 수행한다.** Stage가 끝나면 `outputs/STAGE_STATUS.md`를 갱신하고 멈춘다. 사용자가 확인하고 다음 Stage를 지시하기 전에는 넘어가지 않는다.

Stage 사이의 정보는 `outputs/` 아래 파일로만 넘긴다. 새 세션은 이전 대화를 모르므로, 필요한 것은 파일에서 읽는다.

에이전트에게 위임할 때는 `.claude/agents/`에 정의된 이름의 에이전트를 사용한다. 기본 제공 Explore, Plan 타입은 이 CLAUDE.md를 읽지 않으므로 사용하지 않는다.

실제로 독립 에이전트를 실행할 수 없는 상황이면 역할을 순차적으로 수행한다. 이때 여러 에이전트를 실행한 것처럼 주장하지 않는다.

## 4. 모든 에이전트의 공통 작업 규칙

**읽기:** 작업 시작 전에 위임 메시지가 지정한 `reference/` 파일과 `reference/protocols.md`의 해당 절을 직접 읽는다. 위임 메시지의 요약만 믿지 않는다.

**저장:** 상세 결과는 반드시 파일로 저장한다. 에이전트별 폴더는 `outputs/agents/<에이전트 이름>/`이다.

**보고:** Coordinator에게 돌려주는 응답에는 **15줄 이내 요약과 저장한 파일 경로**만 담는다. 상세 내용을 응답에 붙이지 않는다. 메인 세션의 컨텍스트를 아끼기 위해서다.

**독립성:** 독립 탐색 단계(Round 1)에서는 다른 에이전트의 폴더를 읽지 않는다.

**기존 프로젝트:** `reference/existing_projects.md`는 겹침 확인 용도로만 쓴다. 그 프로젝트들의 방향, 가설, 방법을 따르거나 우선하지 않는다. 겹치는 질문은 버리지 말고 `overlap: <프로젝트명>`만 표시한다.

**기록:** 검증된 결과와 미확인 사항을 항상 구분해서 쓴다. 에이전트 사이의 실제 의견 충돌은 지우지 않고 기록한다.

## 5. 문헌 규칙

**검증:** DOI, PMID, arXiv ID, 학회 proceedings URL 중 하나로 존재를 확인한 논문만 verified로 센다. 확인 경로는 doi.org, Crossref, PubMed, arXiv, OpenReview, 학회 공식 페이지 등이다.

**날조 금지:** 논문을 만들어내지 않는다. 수량을 채우려고 관련성 낮은 논문을 넣지 않는다.

**본문 확인:** Abstract만 읽고 Future Direction을 추론하지 않는다. Discussion, Limitations, Future Work 원문을 직접 확인하고, 어느 절에서 나온 내용인지 적는다. ML 논문은 Limitations와 Conclusion을 확인한다. 본문에 접근하지 못했으면 `discussion_read`를 `"no"`로 표시하고, 읽었다고 주장하지 않는다.

**선행 수행 여부:** 각 future direction마다 이후 다른 연구가 이미 수행했는지 검색해서 `already_done`에 기록한다.

**인용 방식:** 원문을 길게 옮기지 않고 요약한다.

**기간:** 2015~2026년을 폭넓게 보되, 2024~2026년의 최신 모델과 연구를 충분히 포함한다. 기준일은 2026-11-12다.

문헌 기록 파일은 `outputs/agents/<에이전트 이름>/literature.jsonl`이며, 한 줄에 논문 하나를 쓴다. 필드는 다음과 같다.

```json
{"id": "DOI 또는 arXiv ID", "citation": "저자, 연도, 제목", "year": 2024, "venue": "", "url": "",
 "verified_by": "doi.org | crossref | pubmed | arxiv | openreview | publisher",
 "axes": ["A", "K"], "domain": "", "original_question": "", "dataset_paradigm": "", "model_method": "",
 "main_findings": "", "whats_new": "", "limitations": "",
 "discussion_read": "full_text | abstract_only | no",
 "future_directions": [{"text": "", "section": "Discussion 몇째 단락 등", "already_done": "no | partially | yes (근거 논문 ID)"}],
 "transfer_to_affective_neuro": "", "applicable_datasets": ["Horikawa", "Emo-FilM", "Spacetop", "NSD"],
 "relevance": 1, "novelty": 1, "feasibility": 1, "added_by": "<에이전트 이름>"}
```

## 6. Mandatory Scientific Safeguards

Exploratory Research이지만 과학적 엄밀성을 반드시 유지한다.

다음을 구분한다.
* Emotion experienced by participants vs emotion portrayed in stimuli
* Human emotion annotation vs model-generated affective annotation
* 참가자 본인의 보고 vs 별도 평정자의 규범적(normative) 평정
* Emotion representation vs visual/semantic content representation
* Brain encoding accuracy vs explanatory adequacy
* Decodability vs neural representation vs causality
* In-silico predictions vs observed fMRI responses
* Shared representations vs dataset-specific confounds
* Exploratory findings vs confirmatory evidence

다음 방법론적 문제를 점검한다.
* HRF delay 및 temporal autocorrelation
* Stimulus-level / Movie-level / Subject-level leakage
* Repeated stimulus confounds
* Inter-rater agreement and label noise
* Visual-semantic-affective feature collinearity
* Temporal and spatial resolution limits
* ROI selection and circular inference
* Multiple comparisons
* Data access and model checkpoint availability, license
* Contamination from pretrained model training data
* Cross-dataset annotation incompatibility

Emotion Decoding 성능이 높다는 이유만으로 뇌에서 주관적 정서 경험을 직접 읽어냈다고 해석하지 않는다. 이론적으로는 가능하지만 관찰 데이터로 구분할 수 없는 설명은 명확히 표시한다.

## 7. 표기 규칙

* 산출물은 한국어로 쓴다. 논문명, 모델명, 핵심 학술 용어는 영어 원문을 유지한다.
* em dash(U+2014)를 쓰지 않는다.
* 모든 주요 주장과 연구 제안에 검증 가능한 선행연구를 연결한다.
