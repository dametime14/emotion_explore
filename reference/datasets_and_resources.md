# 데이터셋과 계산 자원

## 1. 우리 환경 (사용자가 채워 넣을 것)

* 데이터 위치: [채워 넣기: 예) Horikawa = /path/to/horikawa, Emo-FilM = ..., Spacetop = ..., NSD = ...]
* 원본 자극 파일 보유 여부: [채워 넣기: 데이터셋별로 비디오/이미지/오디오 원본을 갖고 있는지]
* 이미 추출해 둔 feature나 embedding: [채워 넣기: 예) V-JEPA2 feature, CLIP feature 등]
* 계산 자원: [채워 넣기: 예) Perlmutter GPU 노드 종류와 할당 시간, 로컬 GPU]
* 사용 가능한 pretrained checkpoint: [채워 넣기]
* 제약: [채워 넣기: 예) 마감, 데이터 사용 동의 범위]

에이전트는 이 칸이 비어 있으면 추측하지 말고 "미확인"으로 표시한다.

## 2. 우선순위 데이터셋 (출발점 정보, Stage 1에서 원문으로 재확인할 것)

아래 내용은 Stage 1 Dataset Audit의 출발점일 뿐이다. 모든 수치는 원 논문, 공식 데이터 설명서, 저장소로 다시 확인한다.

### 2.1 Horikawa et al. (2020), 최우선
* 논문: The Neural Representation of Visually Evoked Emotion Is High-Dimensional, Categorical, and Distributed across Transmodal Brain Regions. iScience 23(5):101060. doi:10.1016/j.isci.2020.101060
* 공개 데이터: Mendeley Data, doi:10.17632/jbk2r73mzh.1 (2026년 4월 공개로 표시됨). 포함된 파일 구성을 확인할 것.
* 출발점 정보: 피험자 5명이 Cowen & Keltner (2017)의 정서 유발 비디오 약 2,180개를 **소리 없이** 시청했다. 비디오마다 34개 emotion category와 14개 affective dimension 평정이 있으며, 이 평정은 fMRI 참가자 본인이 아니라 Cowen & Keltner의 대규모 평정자 표본에서 왔다.
* 함의: 무음이므로 청각, 음악 관련 질문에는 직접 쓸 수 없다. 피험자 수가 적어 개인차 질문에 약하다.

### 2.2 Emo-FilM (Morgenroth et al., 2025)
* 논문: Scientific Data 12:684. doi:10.1038/s41597-025-04803-5
* 출발점 정보: 단편영화 14편, 총 2시간 30분 이상. fMRI 참가자 30명. 별도 평정자 44명이 50개 항목을 연속 평정했다. 항목은 discrete emotion과 Component Process Model 성분(appraisal, motivation, motor expression, physiological response, feeling)이다. 평균 inter-rater agreement는 0.38이다. 심박, 호흡, 피부전도 기록이 있다.

### 2.3 Spacetop (Jung et al., 2025)
* 논문: Scientific Data. doi:10.1038/s41597-025-05154-x. OpenNeuro ds005256.
* 출발점 정보: 101명, 1인당 약 6시간 스캔. 약 2시간의 naturalistic movie viewing과 인지, 정서, 사회, somatic/interoceptive 과제(통증 포함)가 있고, 생리 데이터가 있다. 과제별 정서 관련 평정의 종류와 시간 해상도는 확인 필요.

### 2.4 Natural Scenes Dataset (Allen et al., 2022)
* 논문: A massive 7T fMRI dataset to bridge cognitive neuroscience and artificial intelligence. Nature Neuroscience.
* 확인할 것: 정서 라벨이 기본 제공되는지. 없다면 COCO 캡션이나 외부 모델로 파생 라벨을 만들 수 있는지, 그리고 그 타당성을 뒷받침하는 선행연구가 있는지.

## 3. Stage 1 관문 (Gate)

모델 기반 연구는 원본 자극이 있어야 feature를 추출할 수 있다. 따라서 Stage 1에서 데이터셋마다 다음 세 가지를 판정한다.

* **G1:** 원본 자극 파일 접근 가능 여부. 보유 / 요청 필요 / 불가 중 하나.
* **G2:** fMRI 데이터 형식과 전처리 수준.
* **G3:** 라벨 접근 가능 여부와 평정 주체.

Horikawa의 G1이 "불가"라면 Coordinator는 Horikawa 1순위 전략에 미치는 영향과 대안을 정리하고 사용자에게 묻는다. 대안의 예는 Cowen & Keltner 자극의 별도 입수 경로, 미리 계산된 feature, 다른 데이터셋으로 우선순위 이동이다.
