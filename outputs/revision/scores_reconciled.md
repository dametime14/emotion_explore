# 재탐색 라운드 점수 대조 (Coordinator 대 adversarial-reviewer)

* 작성: Coordinator. 기준일 2026-11-12
* 입력:
  * `outputs/revision/scores_coordinator.csv`(Coordinator, `score_coordinator.py`)
  * `outputs/revision/scores_reviewer.csv`(adversarial-reviewer, Coordinator 점수 미열람)
  * `outputs/revision/adjustments.csv`(2점 이상 차이 조정)
* 생성: `python3 -I outputs/revision/reconcile.py` → `scores_final.csv`, `gap_table.md`
* 기준 11개: P6 9개 + AI-enabled Affective Neuroscience Contribution + 1-month Feasibility(정의는 `plan.md` 2절)

## 1. 대조 규칙

* 최종 점수는 두 점수의 평균이다. 단, 2점 이상 차이 나는 쌍은 Coordinator가 양쪽 근거를 읽고 `adjustments.csv`에 최종 점수와 누가 움직였는지를 적는다.
* 미조정으로 남은 쌍은 없다.

## 2. 일치도

| 지표 | 값 |
|---|---|
| 쌍 수 | 308(결측 0) |
| 완전 일치 | 56% |
| 1점 이내 | 97% |
| 2점 이상 차이 | 10쌍(C-01 3, C-24 3, C-06 2, C-02 1, C-17 1) |
| 평균 차이(Reviewer - Coordinator) | -0.26 |
| 후보 합계가 Coordinator 쪽이 높은 경우 | 28개 중 19개 |

**Coordinator의 관대함.** 차이가 가장 큰 기준은 Neuroscientific Importance(-0.79), AI-enabled 기여(-0.71), AI / Modeling Contribution(-0.61)이다. Coordinator는 "모델이 있어야 가능한가"만 보고 점수를 줬다. Reviewer는 "그 결과가 정서와 뇌에 대해 말하는가, 아니면 모델과 측정 방법에 대해 말하는가"까지 따졌다. 새 기준의 5점 정의는 후자까지 요구하므로 Reviewer 쪽이 정의에 더 가깝다. 조정에서 Coordinator가 주로 움직인 이유다.

## 3. 2점 이상 차이 조정

| 후보 | 기준 | Coord | Reviewer | 최종 | 누가 움직였나 | 요지 |
|---|---|---|---|---|---|---|
| C-01 | Neuroscientific Importance | 4 | 2 | 3 | 양쪽 | 지각 조건의 '자극 너머' 몫은 자극 feature가 놓친 정보와 갈리지 않는다. 같은 양을 decoder 없이 공변량 부분상관으로도 계산할 수 있다 |
| C-01 | Interpretability | 4 | 2 | 2 | Coordinator | 양의 결과도 affective realism, 자극 모델 불완전, 각성 전역 신호 중 무엇인지 갈린다 |
| C-01 | AI-enabled 기여 | 5 | 3 | 4 | 양쪽 | 측정 장치는 AI 고유다. 다만 단독으로는 결론이 decoder 공간 이야기로 수렴한다 |
| C-02 | Neuroscientific Importance | 5 | 3 | 4 | 양쪽 | 쟁점은 크다. 깨끗한 답은 회상 대 지각처럼 자극이 같은 대조에서만 나온다 |
| C-06 | Neuroscientific Importance | 4 | 2 | 3 | 양쪽 | 같은 C&K 분포에서 평가하면 영역-정서 상관을 재확인하는 순환이다 |
| C-06 | AI / Modeling Contribution | 5 | 3 | 4 | 양쪽 | brain-tuning 선행(Policzer 2025)이 있다 |
| C-17 | AI-enabled 기여 | 4 | 2 | 3 | 양쪽 | 결과가 주로 관찰자 모델과 rank 대역 측정의 성질에 대한 것이다 |
| C-24 | Neuroscientific Importance | 5 | 2 | 2 | Coordinator | 병목이 C&K 라벨로 감독되어 병목 RDM이 라벨 RDM으로 수렴한다. Horikawa 2020의 범주 대 차원 비교를 같은 자료로 다시 판정하게 된다 |
| C-24 | AI / Modeling Contribution | 5 | 3 | 3 | Coordinator | 작은 MLP 헤드라 병목 구조의 고유 기여가 라벨 공간 차이와 분리되지 않는다 |
| C-24 | AI-enabled 기여 | 5 | 3 | 3 | Coordinator | 이론별 인공 뇌라는 발상은 기준에 맞다. 하지만 현재 설계에서는 결과가 라벨 공간 비교로 환원된다 |

## 4. 최종 순위 (55점 만점)

| 순위 | 후보 | 방향 | 한 줄 질문(candidates.md) | Coord | Reviewer | 최종 | AI 기여 | 1개월 |
|---|---|---|---|---|---|---|---|---|
| 1 | C-16 | D1 | AI가 정서를 직접 배워야만 뇌의 정서 반응과 닮아질까, 아니면 세상을 보는 것만으로도 충분할까? | 45 | 39 | 42.0 | 4.5 | 4.0 |
| 2 | C-02 | D2 | 뇌가 본 장면은 실제 장면보다 정서 쪽으로 기울어 있을까? | 42 | 39 | 40.5 | 4.5 | 3.5 |
| 3 | C-08 | D1 | 한눈에 알 수 없는 정서일수록 뇌의 더 깊은 곳에서 표상될까? | 39 | 40 | 39.5 | 4.0 | 4.0 |
| 4 | C-18 | D1 | 사람을 한 번도 보지 못하고 자란 AI도 사람이 나오는 장면의 정서를 뇌처럼 구분할까? | 42 | 37 | 39.5 | 4.5 | 3.0 |
| 5 | C-11 | D1(in-silico 뇌) | 보고 듣는 것만으로는 예측되지 않는 정서 반응은 뇌의 어디에 남고, 정서의 어떤 측면과 함께 움직일까? | 37 | 41 | 39.0 | 4.0 | 3.5 |
| 6 | C-19 | D1, 이론 | 정서 단어를 배우지 못한 AI는 장면의 정서를 뇌와 다르게 볼까? | 41 | 37 | 39.0 | 4.5 | 3.0 |
| 7 | C-27 | D3 | 영화에서 화면과 음악이 서로 다른 감정을 말할 때, 뇌와 사람은 어느 쪽을 따라갈까? | 40 | 37 | 38.5 | 4.0 | 3.5 |
| 8 | C-12 | D1(in-silico 뇌) | 영화에서 얼굴을 지워서 사라지는 정서 반응과 앞 이야기를 지워서 사라지는 정서 반응은 뇌의 서로 다른 곳에 있을까? | 40 | 36 | 38.0 | 4.5 | 2.5 |
| 9 | C-14 | D1(in-silico 뇌) | 정서 관련 뇌 반응은 얼마나 먼 과거의 이야기까지 끌어와서 만들어질까? | 38 | 38 | 38.0 | 3.5 | 4.0 |
| 10 | C-20 | D1 | 정서를 배우면 AI의 '보는 방식' 자체가 바뀌고, 그 변화가 뇌의 시각 영역과 닮을까? | 37 | 39 | 38.0 | 3.0 | 4.5 |
| 11 | C-21 | D2, 비지도 | 뇌가 정서 단어 없이 스스로 나눈 축을 AI로 그려 보면, 그 축은 정서일까 장면 내용일까? | 40 | 36 | 38.0 | 4.0 | 3.0 |

* 12위 이하와 전체 표는 `gap_table.md`에 있다. C-01은 35.5점(18위), C-24는 조정 후 하위권이다.
* 한 줄 질문과 방향 표기는 `candidates.md` 그대로다.

## 5. 두 평가자가 같이 본 것과 다르게 본 것

* **같이 본 것.**
  * 상위 10 가운데 8개가 두 평가자 모두의 상위 10에 든다(C-16, C-02, C-08, C-18, C-11, C-19, C-27, C-14).
  * D2 안에서는 C-02가 C-01보다 강하다. 사용자가 말한 'decoder + emotion head' 자체(C-01)는 측정 장치로 C-02 안에 들어갈 때 의미가 선다.
* **다르게 본 것.**
  * C-11: Reviewer 1위(41), Coordinator 공동 17위(37). Reviewer는 Horikawa가 아닌 소리 있는 자료라는 점과 평가 대 신체 성분이라는 이론 쟁점을 높게 봤다. Coordinator는 null 모델(TRIBE) 품질에 결론이 묶이는 점을 낮게 봤다.
  * C-01, C-24: 위 3절.
* **Reviewer가 새로 찾은 선행(Coordinator가 Crossref로 3건 재확인).**
  * Conwell 2025 PNAS(doi:10.1073/pnas.2306025121): 정서 학습 없는 시각 모델이 사진 arousal, valence 평정의 설명 가능 분산 대부분을 설명했다. 뇌 자료는 없다. C-16, C-19, C-01에 영향을 준다.
  * Méndez 2022(doi:10.1098/rstb.2021.0512): 상구 모델과 정서 인식. C-07에 영향을 준다.
  * Jain & Huth 2018(doi:10.1101/327601): 문맥 길이 encoding. C-14에 영향을 준다.
  * 미검증 3건(Conwell 2023 workshop, VSS 2025 포스터, NeurIPS 2026 TRIBE v2 정서 평가)은 선행 감사에서 다시 확인한다.

## 6. 다음 단계

상위 후보의 선행연구 중복 감사(`prior_overlap_audit.md`)를 거쳐 `selection.md`에서 선정한다.
