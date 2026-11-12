# 재탐색 라운드 상위 후보 선행연구 중복 감사 (adversarial-reviewer)

* 작성: adversarial-reviewer. 기준일 2026-11-12
* 지시: `outputs/revision/plan.md` 3절 3번("상위 후보에는 선행연구 중복 감사를 한다"), Coordinator 위임 메시지
* 대상 7개 묶음(`reviewer_notes.md` 5절 묶음 기준):
  1. C-02 D2 묶음(C-01 측정 장치, C-04 텍스트판 포함). 주 검정을 MC 같은 클립의 회상 대 지각으로 옮긴 판본
  2. C-16 + C-20 + C-05 통합(D1 학습 압력)
  3. C-18 사람을 지운 학습 자료 모델
  4. C-19 정서 단어를 지운 학습 모델
  5. C-08 재귀 계산 깊이
  6. C-11 TRIBE 잔차
  7. C-27 화면 대 음악 정서 충돌
* 읽은 자료: `outputs/revision/gap_table.md`, `adjustments.csv`, `scores_coordinator.csv`(이번부터 열람 허용), `candidates.md`, 각 원문 `revision_round.md`, `outputs/rq_cards/RQ44_recall_reconstruction.md`, `outputs/evaluation/prior_overlap_audit.md`(형식), `reference/existing_projects.md`, 내 `reviewer_notes.md`
* 확인 경로 표기:
  * [PubMed]: PubMed 메타데이터로 PMID와 DOI를 확인했다.
  * [Crossref]: api.crossref.org로 DOI를 확인했다.
  * [arXiv]: export.arxiv.org API로 arXiv ID와 초록을 확인했다.
  * [검색만]: WebSearch 결과 요약만 보았다. 식별자로 확인하지 못했으므로 verified가 아니다.
* 읽은 범위 표기: 본문, 초록, 제목만, 검색 요약.
* 접근하지 못한 경로: 우회하지 않았다.
  * 세션 프록시가 거부한 곳: openreview.net(api, api2), api.openalex.org, visionsciences.org, neurips.cc, jov.arvojournals.org
  * WebFetch에서 이름 해석에 실패한 곳: biorxiv.org, arxiv.org
  * api.semanticscholar.org는 429(요청 한도)였다.
  * 이 때문에 VSS 2025 포스터 원문, NeurIPS 2026 TRIBE v2 평가 원문, Conwell 2023 ICLR workshop 원문은 읽지 못했다(5절).

---

## 0. 판정 기준

Stage 4 감사(`outputs/evaluation/prior_overlap_audit.md` 0절)와 같은 기준을 미리 고정하고 적용했다.

| 판정 | 기준 |
|---|---|
| done | 선행 연구가 같은 가설을 같은 종류의 증거(같은 구성개념, 같은 비교)로 이미 검정했다. 우리 판본이 더하는 것은 데이터셋 교체뿐이다 |
| partially | 선행 연구가 핵심 가설 또는 그 주요 구성 요소를 다른 자극이나 설계로 검정했다. 남는 새 부분을 한 줄로 특정할 수 있다 |
| not found | 이 검색 범위에서 핵심 가설을 검정한 연구가 없다. 방법이나 인접 구성개념의 선행만 있다 |

* "not found"는 "없다"가 아니라 "이 검색 범위에서 찾지 못했다"이다.
* Google Scholar, bioRxiv 전용 검색, OpenReview 검색은 쓰지 못했다. bioRxiv 문헌은 PubMed와 Crossref에 색인된 것만 잡혔다.
* Stage 4 이후 'not found'가 뒤집힌 사례(RQ-32, RQ-14)가 있었다. 그러므로 not found 판정 셋(C-02 핵심, C-19, C-08)은 잠정이다.

---

## 1. 요약

| 묶음 | 원 제안자 판정 | 이번 판정 | 가장 가까운 선행 | 남는 새 부분(한 줄) | 권고 |
|---|---|---|---|---|---|
| **C-02** D2 묶음(회상 대 지각판) | no(VD-RV-1, GI-RV-3), partially(VD-RV-A, VD-RV-3) | **not found(핵심)**, 구성 요소는 partially | 정서 기억의 감각 재현 강화: Ritchey 2013, Bowen & Kensinger 2017, Kark & Kensinger 2019, Krenz 2025. 행동 수준 '기억 흐려짐': Cooper 2019. 합성 fMRI null: Chen, Keil, Ding 2025(VSS). 지도학습 정서 해독: EmoMind | 같은 클립의 회상과 지각에서, 정서를 배우지 않은 decoder 공간의 '정서 방향 이동'을 SNR 맞춘 합성 null과 비정서 속성 대조로 잰다 | 유지. 예측을 양방향으로 사전 등록(Cooper 2019는 '흐려짐' 쪽을 예고). RQ-44와 한 파이프라인으로 합칠 것을 권고 |
| **C-16 + C-20 + C-05** | no(FA-RV-1, GI-RV-2, FA-RV-5, BI-RV-1) | **partially** | Conwell 2024 Nat Commun, Conwell 2025 PNAS, Conwell et al. 2024 arXiv:2410.23603(SLIP 대 SimCLR, 미 평정), **Gao, Ajith & Peelen 2025**(사물 학습 AlexNet 대 정서 학습 EmoNet, 정서 평정과 시각피질 fMRI), **Soderberg, Jang & Kragel 2026**(얼굴 정서 학습 대 장면 정서 학습 ANN, pSTS와 편도체 fMRI). 되먹임 쪽은 VCA(피드포워드), Leem 2026, VSS 2025 | 같은 이미지, 같은 구조에서 정서 라벨 대 비정서 장면 속성 감독, 되먹임 대 피드포워드 미세조정을 정서 영상 fMRI의 정서 관련 분산(시각 대 transmodal)으로 비교 | 좁혀서 유지. Gao 2025의 결과(일상 장면은 사물 모델 우세, 정서 유발 자극은 EmoNet 우세)를 사전 예측에 넣는다 |
| **C-18** | no(FA-RV-3) | **partially** | **Soderberg, Jang & Kragel 2026**(얼굴 대 장면 맥락 ANN으로 pSTS, 편도체 정서 부호화 비교), Xu 2021(얼굴 박탈 DCNN), Dobs 2022, Kanwisher 2023, Chen & Whitney 2019 | '얼굴 대 맥락' 질문을 학습 과제 조작이 아니라 **학습 자료 박탈(통제된 성장)**로 묻고, 사람 있는 클립 대 없는 클립의 상호작용으로 판정 | 유지. Soderberg 2026을 가장 가까운 선행으로 명시하고, 그 결과(얼굴 표상은 pSTS, 장면 정서는 편도체와 pSTS)를 예측에 넣는다 |
| **C-19** | no(FA-RV-4) | **not found** | 사람 병변 유비: Lindquist 2014(의미 치매), **Souter, Lindquist & Jefferies 2021**(의미 실어증: valence 분류 보존, 부정 범주 구분 손상). 계산 모델: Conwell et al. 2024(언어 정렬 이득 작음, 미 평정), 구성주의 에이전트 모델 2편(arXiv:2605.09522, 2605.07761, 뇌와 시각 없음) | 언어 감독에서 정서 단어만(빈도 맞춘 비정서 단어 대조와 함께) 지운 시각 encoder로, 범주 대 valence 해리가 뇌 정렬에서 나오는지 시험 | 유지. Souter 2021을 '사람 쪽 표적 해리'로 인용 |
| **C-08** | no(BI-RV-4) | **not found** | Kar 2019(물체 인식의 재귀, 늦게 풀리는 이미지), Bo 2022(정서 장면 표상이 200~300 ms에 형성, 재귀 상호작용 시사, EEG-fMRI), Bo 2021 | 모델이 계산한 자극별 '정서 판독 계산 깊이'가 fMRI 정서 정보의 위계 위치(시각에서 transmodal)를 예측하는지 | 유지 |
| **C-11** | partially(EF-RV-0) | **partially** | NeurIPS 2026 "Evaluating TRIBE v2 Beyond Its Original Benchmarks"(검색만, 자연 정서 영화에서 정서 범주별 대응 편차와 선택적 실패), EmoMind의 TRIBE 대체 시험, Horikawa 2020(공변량 너머 정서), Morgenroth 2026(CPM 성분과 이산 정서, 행동) | TRIBE 실패 위치의 지도 다음 단계, 즉 zero-shot in-silico null을 뺀 **공유 잔차를 CPM 성분 band와 본인 생리로 분해** | 유지. 1단계(정서 영역에서 TRIBE가 실패하는가)는 NeurIPS 2026 논문과 겹칠 가능성이 높아 주 결과로 쓰지 않는다. overlap: Emo-FilM 연구(직접) |
| **C-27** | no(MD-RV-2) | **partially** | Pehrs 2014(음악이 같은 장면의 정서를 바꾸는 조작, STG가 방추-편도체 연결 조절), Bravo 2024 PNAS(불협화 음악 조작, V1 관여), Muller-Rodriguez & O'Daly 2024 arXiv:2410.17300(Forrest Gump 사운드트랙 특징과 공유 정서, STS와 쐐기앞소엽), Lettieri 2024 | 조작 없이 AI로 분리한 채널 정서에서 **자연 발생 충돌 순간**을 찾고, 신뢰도 가중 대 가치 우선 통합 규칙을 뇌와 평정자에서 비교 | 유지(D3라 우선순위는 낮음). overlap: Emo-FilM 연구(자료와 사전학습 멀티모달 feature) |

* **done 0건, partially 4건(C-16 묶음, C-18, C-11, C-27), not found 3건(C-02 핵심, C-19, C-08).**
* **원 제안자 판정과 달라진 점:**
  * C-16 묶음: no에서 partially로 바꿨다. Gao, Ajith & Peelen 2025(정서 학습 대 사물 학습 모델 비교)와 Soderberg, Jang & Kragel 2026(학습 과제가 다른 정서 ANN과 정서 영역 fMRI)이 원 제안 검색에서 빠졌다.
  * C-18: no에서 partially로 바꿨다. Soderberg 2026이 '얼굴 대 맥락'을 ANN과 fMRI로 이미 다뤘다. 다만 학습 자료 박탈은 아니다.
  * C-27: no에서 partially로 바꿨다. 음악-화면 정서 불일치의 fMRI 조작 연구(Pehrs 2014, Bravo 2024)와 자연 영화 사운드트랙 연구(Muller-Rodriguez 2024)가 있다.
  * C-02: 원 제안의 no를 핵심 가설에 대해서는 유지한다. 다만 '정서가 회상 재현의 충실도를 높인다'는 구성 요소는 이미 여러 번 보고되었다.

---

## 2. 후보별 감사

### 2.1 C-02 D2 묶음: 같은 클립을 떠올릴 때 뇌 표상은 지각 때보다 정서 쪽으로 이동하는가 (C-01 측정 장치, C-04 텍스트판 포함)

**(a) 가장 가까운 선행**

| 선행 | 식별자 | 확인 | 읽은 범위 | 관계 |
|---|---|---|---|---|
| Ritchey, Wing, LaBar, Cabeza 2013, "Neural similarity between encoding and retrieval is related to memory via hippocampal interactions", Cereb Cortex | doi:10.1093/cercor/bhs258, PMID 22967731 | [PubMed] | 초록 | 정서 각성이 부호화-인출 패턴 유사도를 높였다. 충실도이지 방향이 아니다 |
| Bowen & Kensinger 2017, "Recapitulation of emotional source context during memory retrieval", Cortex | doi:10.1016/j.cortex.2016.11.004, PMID 27923474 | [PubMed] | 초록 | 부정 맥락에서 부호화-인출 중첩이 복측 시각과 편도체에서 컸다 |
| Kark & Kensinger 2019, "Post-encoding amygdala-visuosensory coupling is associated with negative memory bias", J Neurosci | doi:10.1523/JNEUROSCI.2834-18.2019, PMID 30760626 | [PubMed] | 초록 | 시각 감각 재현 강화가 부정 기억을 지지한다(NEVER 계열) |
| Krenz et al. 2025, "Memory boost for recurring emotional events is driven by initial amygdala response promoting stable neocortical patterns", J Neurosci | doi:10.1523/JNEUROSCI.2406-23.2025, PMID 39947923 | [PubMed] | 초록 | 반복 노출 시 정서 장면의 전두두정 패턴이 더 안정적이다. MC 반복 회차 분석의 직접 선행 |
| Cooper, Kensinger & Ritchey 2019, "Memories fade: the relationship between memory vividness and remembered visual salience", Psychol Sci | doi:10.1177/0956797619836093, PMID 30897035 | [PubMed] | 초록 | **행동 수준의 방향 검정.** 기억 속 이미지는 부호화 때보다 덜 두드러지게(밝기, 채도) 재구성되었다. 부정 정서는 주관적 생생함과 부호화 정밀도를 높였다. C-02의 '과장' 예측과 반대 방향을 예고한다 |
| Feldman, Siegel, Barrett, Quigley, Wormwood 2022(Affect Sci), Siegel 2018, Gao et al. 2024(J Gen Psychol) | doi:10.1007/s42761-022-00114-9 (PMID 36046009), doi:10.1080/00221309.2024.2378326 (PMID 39023941) | [PubMed] | 초록 | affective realism은 모두 행동 판단(중립 얼굴 평가) 수준이다. 신경 표상 검정은 찾지 못했다 |
| Chen, Keil & Ding 2025, "The Origin of Affect-specific Neural Representations of Emotional Scenes in Early Visual Cortex", J Vis 25(9):1989 (VSS 2025 초록) | doi:10.1167/jov.25.9.1989 | [Crossref]로 존재와 저자 확인. 내용은 [검색만] | 검색 요약 | NSD로 학습한 CNN encoding 모델의 합성 반응에서 IAPS 정서 장면은 초기 시각피질에서 중립과 구분되지 않았고, AffectNet 얼굴은 구분되었다. 저자는 재진입 지지로 해석했다(요약 두 건 일치). **C-01~C-03의 '자극 구동 합성 null' 논리가 이미 쓰였다.** 회상, 방향, decoder 공간은 없다 |
| EmoMind (Mohammed, Gu, Fang 2026) | arXiv:2605.16739 | [arXiv] 초록 v3 | 초록(+ vision-decoding의 본문 기록) | 34차원 정서를 **지도학습으로 해독**해 중립 캡션을 다시 쓴다. 합성 뇌(TRIBE) 대체 시험이 있다. vision-decoding의 본문 확인에 따르면 회상 조건과 영역 분석이 없다. C-02는 정서를 배우지 않은 decoder로 자극과 같은 head를 비교하고 회상 대 지각을 본다 |
| Mind captioning (Horikawa 2025) | doi:10.1126/sciadv.adw1464 | [db] | 본문(이전 라운드) | 지각으로 학습한 decoder가 회상 내용 기술로 일반화되었다. 정서 방향은 다루지 않았다 |

**(b) 판정: not found(핵심 가설). 구성 요소는 partially.**
* 정서가 회상 재현의 충실도를 높인다는 부분은 여러 번 보고되었다(Ritchey 2013, Bowen 2017, Kark 2019, Krenz 2025).
* 회상 표상의 **방향 이동**을 정서 축에서 잰 신경 연구는 찾지 못했다. 행동 수준의 방향 검정(Cooper 2019)은 시각 두드러짐이 '흐려진다'는 결과였다.
* affective realism의 신경 표상 검정은 찾지 못했다(PubMed "affective realism" 9건이 모두 행동 또는 이론).
* **남는 새 부분:** 같은 클립의 회상과 지각에서, 정서를 배우지 않은 decoder 공간의 정서 방향 이동을 SNR을 맞춘 합성 null과 비정서 속성 대조로 재는 것.

**(c) 설계 함의**
* 예측을 양방향으로 사전 등록한다. NEVER와 affective realism 계열은 '정서 쪽 과장'을 예측한다. Cooper 2019의 기억 흐려짐과 회상의 낮은 SNR은 '중립 쪽 수축'을 예측한다. 수축은 합성 null로 빼고 남는 방향만 해석한다.
* Krenz 2025를 MC 반복 회차(1~5회) 분석의 비교 기준으로 쓴다.
* Chen, Keil, Ding 2025가 같은 합성 null 논리를 이미 썼으므로 null 방법 자체를 새로움으로 주장하지 않는다.

**(d) RQ-44 카드와의 관계(한 줄):** 같은 MC 회상 72클립 x 5회와 같은 단서 캡션 교란을 쓴다. RQ-44는 회상 속 정서 정보의 **출처**(원 클립 흔적 대 단서 기반 재구성)를 encoding 예측으로 분해한다. C-02는 decoder 공간에서 정서 **방향과 크기의 이동**을 잰다. RQ-44가 'schema 쪽'으로 나오면 정서 배제 캡션이 단서이므로 C-02는 '중립 쪽 이동'을 예측하게 되어 두 결과가 맞물린다. 따라서 합성 null과 단서 통제를 공유하는 한 연구로 합치는 것이 낫다.

**overlap:** EmoBrain(부분: 뇌에서 정서를 해독하는 도구가 겹친다. 질문은 다르다).

### 2.2 C-16 + C-20 + C-05: 학습 목표, 미세조정 깊이, 되먹임을 통제한 모델 중 무엇이 정서 영상 fMRI의 정서 관련 분산과 닮는가

**(a) 가장 가까운 선행**

| 선행 | 식별자 | 확인 | 읽은 범위 | 관계 |
|---|---|---|---|---|
| Conwell, Prince, Kay, Alvarez, Konkle 2024, "A large-scale examination of inductive biases shaping high-level visual representation in brains and machines", Nat Commun | doi:10.1038/s41467-024-53147-y | [Crossref] | 초록(geometry-info 기록) | 구조와 데이터를 맞추면 목표(대조 학습 대 언어 정렬)의 뇌 예측 차이가 작다. 정서 아님 |
| Conwell, Graham, Boccagno, Vessel 2025, "The perceptual primacy of feeling", PNAS | doi:10.1073/pnas.2306025121, PMID 39847334 | [PubMed] | 초록 | 정서 평정(arousal, valence, beauty)을 지각 모델이 대부분 설명한다. 무작위, 범주 지도, 자기지도를 비교했다. 뇌 없음 |
| **Conwell, Hamblin, Boccagno, Mayo, Cummings, Isik, Barbu 2024**, "Using Multimodal Deep Neural Networks to Disentangle Language from Visual Aesthetics" | arXiv:2410.23603 | [arXiv] | 초록 | **SLIP 세트로 언어 정렬 효과를 통제**했다. 미(beauty) 평정에서 SimCLR가 설명 가능 분산 대부분을 설명하고 SLIP의 이득은 작았다. 뇌 없음. 내 앞선 노트에서 미검증으로 둔 ICLR 2023 workshop 요약 내용을 식별자로 확인 가능한 판으로 대체한다 |
| **Gao, Ajith & Peelen 2025**, "Object representations drive emotion schemas across a large and diverse set of daily-life scenes", bioRxiv | doi:10.1101/2025.02.19.638854 | [Crossref] 초록 | 초록 | **정서 학습(EmoNet) 대 사물 학습(AlexNet) 비교.** 일상 장면 4,913장의 정서 평정은 AlexNet이 더 잘 예측했고, 명시적 정서 유발 자극에서는 EmoNet이 우세했다. BOLD5000 시각피질 fMRI에서 LOC 패턴이 정서 평정을 가장 잘 예측했다. 모델-뇌 정렬을 목표별로 비교한 것은 아니다. EmoNet은 C&K 프레임으로 학습되어 우리 자료에는 쓸 수 없다 |
| **Soderberg, Jang & Kragel 2026**, "Sensory encoding of emotion conveyed by the face and visual context", Soc Cogn Affect Neurosci | doi:10.1093/scan/nsag028, PMID 42143618 | [PubMed] | 초록 | **표정만으로 정서를 학습한 ANN 대 장면 전체로 정서를 학습한 ANN**의 표상으로 pSTS와 편도체 fMRI(자연 자극, 두 자료 N=20, 45)를 예측했다. 표정 표상은 pSTS에, 장면 정서는 두 영역 모두에 부호화되었다. 학습 과제를 바꾼 ANN을 정서 영역 fMRI와 비교한 가장 가까운 선행이다 |
| Schwartz et al. 2023, J Neurosci | doi:10.1523/JNEUROSCI.1277-22.2023 | [Crossref] | 제목 | 정체성 학습 대 표정 학습 DCNN과 두개내 기록 |
| Liu et al. 2025 VCA, bioRxiv | doi:10.1101/2025.10.20.683439 | [Crossref] 초록, 본문은 [검색만] | 초록 | ViT + 편도체 모사 모듈. 검색 요약에 따르면 본문은 시각에서 편도체로 가는 **피드포워드** 연결이라고 적었다. 되먹임 조작은 없다 |
| Leem, Keil, Ding 2026 | arXiv:2607.19327 | [arXiv] | 초록 | 시각 모듈 + valence 모듈의 Pavlov 학습. 되먹임 조작과 뇌 시각피질 비교는 초록에 없다 |
| Chen, Keil, Ding 2025 (VSS) | doi:10.1167/jov.25.9.1989 | [Crossref], 내용 [검색만] | 검색 요약 | 재진입 가설을 합성 fMRI로 검정. 모델 구조에 되먹임을 넣지는 않았다 |

**(b) 판정: partially.** 핵심 구성 요소를 다른 자료와 설계로 이미 다뤘다.
* 학습 목표 통제(언어 정렬): Conwell 2024, Conwell et al. 2024 arXiv
* 정서 학습 대 사물 학습: Gao 2025
* 학습 과제를 바꾼 정서 ANN과 정서 영역 fMRI: Soderberg 2026

**남는 새 부분:** 같은 이미지, 같은 구조에서 정서 라벨 대 비정서 장면 속성 감독, 그리고 되먹임 대 피드포워드 끝까지 미세조정을 대조하고, 정서 영상 fMRI의 정서 관련 분산을 시각 영역과 transmodal 영역에서 비교하는 것.

**(c) 설계 함의**
* Gao 2025는 '정서 유발 자극에서는 정서 학습 모델이 우세'라고 보고했다. C&K는 정서 유발 자극이므로 C3 대비(정서 대 장면 속성)의 사전 예측을 이 방향으로 둔다.
* Soderberg 2026은 얼굴 대 장면 정서 학습을 이미 비교했다. 그러므로 C-16에서 '정서 학습의 종류' 비교는 빼고 '정서 학습 유무와 깊이'에 집중한다.
* 되먹임 팔(C-05)은 Ding, Keil 그룹이 같은 쟁점을 연속으로 다루고 있다(VCA, Leem 2026, VSS 2025). 선점 위험을 명시한다.

**overlap:** EmoBrain(구 EmoViS 범위: Horikawa 정서 기하의 감각-의미 기원과 부분 겹침).

### 2.3 C-18: 사람이나 얼굴을 지운 자료로 키운 시각계도 사람이 나오는 장면의 뇌 정서 신호를 설명하는가

**(a) 가장 가까운 선행**

| 선행 | 식별자 | 확인 | 읽은 범위 | 관계 |
|---|---|---|---|---|
| **Soderberg, Jang & Kragel 2026**, SCAN | doi:10.1093/scan/nsag028, PMID 42143618 | [PubMed] | 초록 | 얼굴 표정 대 장면 맥락이라는 같은 이론 쟁점을 ANN과 fMRI(pSTS, 편도체)로 다뤘다. 조작은 학습 과제(무엇으로 정서를 학습했나)이고 학습 자료 박탈이 아니다 |
| Xu, Zhang, Zhen, Liu 2021, "The face module emerged in a deep convolutional neural network selectively deprived of face experience", Front Comput Neurosci | doi:10.3389/fncom.2021.626259 | [Crossref] | 제목(frontier-ai 초록 기록) | 얼굴 박탈 DCNN. 정서와 뇌 정서 신호는 다루지 않았다 |
| Dobs, Martinez, Kell, Kanwisher 2022, "Brain-like functional specialization emerges spontaneously in deep neural networks", Sci Adv | doi:10.1126/sciadv.abl8913, PMID 35294241 | [PubMed] | 초록 | 과제 최적화로 얼굴과 물체 처리가 분리된다. 정서 아님 |
| Kanwisher, Khosla, Dobs 2023, "Using artificial neural networks to ask 'why' questions of minds and brains", Trends Neurosci | doi:10.1016/j.tins.2022.12.008, PMID 36658072 | [PubMed] | 초록 | 과제와 경험을 조작한 ANN으로 '왜' 질문을 묻는 틀. C-18이 따르는 방법론의 리뷰 |
| Chen & Whitney 2019, PNAS | doi:10.1073/pnas.1812250116 | [db] | 초록(frontier-ai 기록) | 사람에서 인물을 가려도 맥락만으로 정서 추적. 행동 |

**(b) 판정: partially.** '얼굴 대 맥락'이라는 핵심 이론 쟁점을 ANN 표상과 정서 영역 fMRI로 검정한 연구(Soderberg 2026)가 있다. 학습 자료 박탈(controlled rearing)을 정서와 뇌 정서 신호에 적용한 연구는 찾지 못했다.

**남는 새 부분:** 같은 이미지에서 사람이나 얼굴만 지운 **학습 자료 박탈** 모델로, 사람 있는 클립 대 없는 클립의 정서 겹침 설명량 상호작용을 transmodal 영역까지 보는 것.

**(c) 설계 함의**
* Soderberg 2026의 결과(얼굴 표상은 pSTS, 장면 정서는 편도체와 pSTS 모두)를 사전 예측에 넣는다. 사람 지움 모델의 손실은 pSTS에서 크고 편도체에서 작아야 한다.
* 편도체 신호는 Horikawa에서 약하다(TE 43 ms). 이 예측은 MC 반복으로 신뢰도를 확인한 뒤에만 해석한다.

**overlap:** EmoBrain(구 EmoViS 범위, 부분).

### 2.4 C-19: 정서 단어를 배우지 못한 시각계는 뇌와 다르게 정서를 볼까

**(a) 가장 가까운 선행**

| 선행 | 식별자 | 확인 | 읽은 범위 | 관계 |
|---|---|---|---|---|
| Lindquist et al. 2014, Emotion | doi:10.1037/a0035293 | [db] | 초록(frontier-ai 기록) | 의미 치매 환자에서 범주 지각은 손상되고 affect 지각은 보존. 사람 쪽 원 근거 |
| **Souter, Lindquist & Jefferies 2021**, "Impaired emotion perception and categorization in semantic aphasia", Neuropsychologia | doi:10.1016/j.neuropsychologia.2021.108052, PMID 34624259 | [PubMed] | 초록 | 의미 접근 장애 환자가 valence가 다른 얼굴은 분류했으나 부정 정서 범주끼리는 구분하지 못했다. 단어 anchor가 도움이 되었다. **C-19가 인공 학습자에서 찾으려는 해리와 같은 모양**이다 |
| Conwell et al. 2024 | arXiv:2410.23603 | [arXiv] | 초록 | 언어 정렬의 이득이 작고 캡션 embedding만으로는 이미지 + 캡션보다 덜 정확했다(미 평정). 언어 '유무' 조작이지 정서 어휘 '내용' 조작은 아니다 |
| Zhang, Le Hoang, Taniguchi, Horii 2026 | arXiv:2605.09522 | [arXiv] | 초록 | 구성 정서 이론을 에이전트 간 명명 게임으로 모델링. 시각 encoder와 뇌 비교 없음 |
| Nomura, Tsubamoto, Horii 2026 | arXiv:2605.07761 | [arXiv] | 초록 | 내수용 신호와 상징 출현으로 정서의 사회적 실재를 모델링. 시각과 뇌 없음 |
| Giraud, Marelli, Nava 2023, Heliyon | doi:10.1016/j.heliyon.2023.e17864, PMID 37539291 | [PubMed] | 초록 | 분포 의미 모델이 정서의 신체 위치 보고를 예측. 언어가 정서 개념화에 기여한다는 계산 증거이나 시각 학습 조작은 아님 |

**(b) 판정: not found.** 언어 감독에서 정서 어휘만 빼는 조작으로 범주 대 valence 해리를 시험한 연구는 찾지 못했다. 사람 병변 연구(Lindquist 2014, Souter 2021)가 표적 해리를 이미 보였고, 계산 쪽은 언어 유무 조작(Conwell et al. 2024)과 시각 없는 구성주의 에이전트 모델뿐이다.

**남는 새 부분:** 빈도를 맞춘 비정서 단어 지움 대조와 함께 정서 단어만 지운 언어 감독으로 시각 encoder를 학습하고, Lindquist, Souter식 해리(범주 손상, valence 보존)가 뇌 정렬에서도 나오는지 보는 것.

**(c) 설계 함의**
* Souter 2021의 해리는 '부정 정서 범주끼리'에서 가장 컸다. C&K 부정 범주(fear, horror, disgust, sadness, anger 등) 안의 구분을 주 지표로 사전 등록한다.
* Conwell et al. 2024를 보면 언어 정렬 자체의 효과가 작을 수 있다. 정서 단어 지움 효과는 더 작을 수 있으므로 검정력 계산을 1주차에 한다.

**overlap:** EmoBrain(구 EmoViS 범위, 의미 기원과 부분 겹침).

### 2.5 C-08: 한눈에 알 수 없는 정서일수록 뇌의 더 깊은 곳에서 표상되는가

**(a) 가장 가까운 선행**

| 선행 | 식별자 | 확인 | 읽은 범위 | 관계 |
|---|---|---|---|---|
| Kar, Kubilius, Schmidt, Issa, DiCarlo 2019, "Evidence that recurrent circuits are critical to the ventral stream's execution of core object recognition behavior", Nat Neurosci | doi:10.1038/s41593-019-0392-5 | [Crossref] | 제목(brain-inspired 기록) | 늦게 풀리는 이미지와 재귀의 필요성. 물체 인식 |
| Bo et al. 2022, "Decoding the temporal dynamics of affective scene processing", NeuroImage | doi:10.1016/j.neuroimage.2022.119532, PMID 35931307 | [PubMed] | 초록 | EEG-fMRI에서 정서 특이 표상이 200~300 ms(유쾌 약 200 ms, 불쾌 약 260 ms)에 형성되어 약 2 s 지속했다. 저자는 분산 영역 간 재귀 상호작용을 시사했다. 시간 정보이지 자극별 계산 깊이가 아니다 |
| Bo et al. 2021, Cereb Cortex | doi:10.1093/cercor/bhaa411 | [Crossref] | 제목 | 편도체에서 시각피질로의 effective connectivity와 decoding |
| Kietzmann et al. 2019, PNAS | doi:10.1073/pnas.1905544116 | [db] | 초록(brain-inspired 기록) | 시각 동역학의 재귀 |
| 동적 표정 인식에서 공간주파수 간 재귀가 모호성 해소를 돕는다는 CogSci 2020 논문 | 식별자 없음 | [검색만](brain-inspired) | 없음 | 확인 불가 |

**(b) 판정: not found.** 자극별 정서 판독 계산 깊이를 모델로 계산해 fMRI 정서 정보의 위계 위치와 잇는 연구는 찾지 못했다. Bo 2022가 정서 장면 표상의 재귀적 형성을 시간 영역에서 시사했지만 자극별 변수는 없다.

**남는 새 부분:** 모델이 계산한 자극별 '정서 판독에 필요한 재귀 단계'가 그 자극의 정서 정보가 시각피질과 transmodal 영역 중 어디에 더 실리는지를 물체 재귀 요구량 이상으로 예측하는지.

**(c) 설계 함의**
* Bo 2022는 불쾌 장면의 표상이 유쾌보다 늦게 형성된다고 보고했다. valence별 재귀 요구량 차이를 보조 예측으로 둘 수 있다.
* 블록 평균 fMRI는 시간 순서를 보지 못하므로 결론은 '위치'에 한정한다.

**overlap:** EmoBrain(구 EmoViS 범위, 부분: brain-inspired 표기를 따름).

### 2.6 C-11: 보고 듣는 것만으로 예측되지 않는 정서 반응은 어디에 남고 어떤 성분과 함께 움직이는가

**(a) 가장 가까운 선행**

| 선행 | 식별자 | 확인 | 읽은 범위 | 관계 |
|---|---|---|---|---|
| "Evaluating TRIBE v2 Beyond Its Original Benchmarks: From Functional Localizers to Naturalistic Emotion", NeurIPS 2026 포스터 | 식별자 없음. neurips.cc/virtual/2026/159782 | [검색만]. neurips.cc와 OpenReview는 프록시가 거부했고 arXiv와 Crossref에서 찾지 못함. **미검증** | 검색 요약 두 건 | 동적 시청각 localizer와 '연속 정서 주석이 있는 자연 정서 영화'로 TRIBE v2를 평가했다. 지각 대비, Multiple Demand, ToM은 맞았고 청각 언어와 일부 정서 조건에서 선택적으로 실패했다. 정서 범주별 대응 편차가 컸다. **사용 자료는 확인하지 못했다.** '연속 정서 주석'이라는 표현은 Emo-FilM과 맞지만 단정할 수 없다. 잔차 분해, CPM, 생리 분석이 있는지는 요약에 없다 |
| EmoMind (2026) | arXiv:2605.16739 | [arXiv] | 초록 | TRIBE 합성 반응 대체 시험(구조 RSA 감쇠) |
| d'Ascoli et al. 2026, TRIBE v2 | arXiv:2605.04326 | [arXiv](이전 라운드) | 초록 | 모델 자체 |
| Horikawa et al. 2020 | doi:10.1016/j.isci.2020.101060 | [db] | 본문(이전 라운드) | 정서 범주가 시각, 의미 공변량을 넘어 transmodal 영역을 설명 |
| Morgenroth et al. 2026, "Dissecting appraisal and multicomponential features of emotion", Emotion | doi:10.1037/emo0001619, PMID 41525366 | [PubMed] | 초록 | Emo-FilM 주석에서 이산 정서가 CPM 성분으로 예측되고 valence와 자기 관련성으로 위계를 이룸. 행동(주석)만 |
| Ma & Kragel 2026, "Map-like representations of emotion knowledge in hippocampal-prefrontal systems", Nat Commun | doi:10.1038/s41467-025-68240-z, PMID 41588009 | [PubMed] | 초록 | 정서 영화 fMRI에서 해마는 정서 개념 위계, vmPFC는 2차원 정동 공간을 추적 |
| Chan et al. 2026, "Individual differences of cortical and subcortical emotion-informed functional gradients", Hum Brain Mapp | doi:10.1002/hbm.70617, PMID 42568151 | [PubMed] | 초록 | 영화 정서 주석으로 고른 프레임의 기능 gradient와 개인차. C-15(개인차)에 더 가깝다 |
| Jang et al. 2026, "A representation of the visual environment in the human basolateral amygdala supports learning and choice", bioRxiv | doi:10.64898/2026.10.07.757347, PMID 42926498 | [PubMed] | 초록 | 자연 영상 encoding 모델로 BLA의 저차원 시각 표상을 찾고 closed-loop 합성으로 전향 검증. C-11의 피질하 2단계 readout에 참고 |

* 참고(미검증 자원): Hugging Face의 커뮤니티 "TRIBE v2 Subcortical Head"(검색 결과만)가 편도체 등 피질하 반응 예측 head를 표방한다. 라이선스와 학습 자료를 확인하지 못했으므로 쓰지 않는다.

**(b) 판정: partially.** 'TRIBE v2가 자연 정서 영화에서 정서 조건별로 어디서 실패하는가'(옛 RQ-51, C-11의 1단계)는 NeurIPS 2026 논문이 다뤘을 가능성이 높다. 원문을 확인하지 못해 done이 아니라 partially로 둔다. zero-shot null을 뺀 공유 잔차를 CPM 성분 band와 본인 생리로 분해한 연구는 찾지 못했다.

**남는 새 부분:** 정서 영역과 적합도를 맞춘 대조 영역의 공유 잔차 비율을 비교하고, 그 잔차를 appraisal, physiology 등 CPM band와 참가자 본인 EDA, 심박으로 분해하는 것.

**(c) 설계 함의**
* NeurIPS 2026 논문의 사용 자료와 정서 범주별 결과를 확인하기 전에는 '정서 영역에서 TRIBE 잔차가 크다'를 주 결과로 쓰지 않는다.
* 이 논문이 '일부 정서 조건의 선택적 실패'를 보고했다면, 그것은 C-11의 잔차가 영역별 적합도 차이로 기계적으로 커질 수 있다는 내 지적(`reviewer_notes.md` 7절)을 뒷받침한다. 대조 영역을 '천장 대비 TRIBE 적합도'로 맞추는 규칙을 필수로 한다.

**overlap: Emo-FilM 연구(직접).** `reference/existing_projects.md`의 Emo-FilM 연구는 "Emo-FilM으로, 영화 시청 중 정서 맥락과 시간 정보가 뇌 반응에 어떻게 기여하는지를 사전학습된 멀티모달 뇌 인코딩 모델로 분석하는 계획"이다. C-11은 같은 자료에 사전학습 멀티모달 뇌 encoding 모델(TRIBE v2)을 쓴다. 겹치지 않는 부분은 '정서 라벨 없는 in-silico null의 잔차를 CPM과 본인 생리로 분해'하는 질문이다.

### 2.7 C-27: 영화에서 화면과 음악이 서로 다른 감정을 말할 때 뇌와 사람은 어느 쪽을 따라가는가

**(a) 가장 가까운 선행**

| 선행 | 식별자 | 확인 | 읽은 범위 | 관계 |
|---|---|---|---|---|
| Pehrs et al. 2014, "How music alters a kiss: superior temporal gyrus controls fusiform-amygdalar effective connectivity", SCAN | doi:10.1093/scan/nst169 | [Crossref] | 검색 요약(PMC4221214) | 같은 영화 장면에 음악을 바꿔 붙인 조작. 방추, 편도체, 전측 STG 통합망. 슬픈 음악에서 효과가 컸다 |
| Bravo et al. 2024, "Dissonant music engages early visual processing", PNAS | doi:10.1073/pnas.2320378121 | [Crossref] | 초록(multimodal-dynamics 기록) + 검색 요약 | 같은 단편영화에 협화, 불협화 음악. 불협화가 정서 추론을 부정 쪽으로 옮기고 V1을 움직였다 |
| Muller-Rodriguez & O'Daly 2024, "Neural association between musical features and shared emotional perception while movie-watching: fMRI study" | arXiv:2410.17300 | [arXiv] | 초록 | Forrest Gump 시청 중 공유 arousal, valence가 사운드트랙 spectrogram, tempo와 상관했다. 공유 정서 순간에 STS와 쐐기앞소엽이 활성화되었다. **자연 영화에서 사운드트랙과 정서를 연결한 가장 가까운 선행**이다. 화면 채널 분리와 충돌 분석은 없다 |
| Lettieri et al. 2024, Sci Adv | doi:10.1126/sciadv.adk6840 | [db] | 본문(multimodal-dynamics 기록) | 같은 영화의 시청각, 시각, 청각 판본을 따로 촬영 |
| Gao et al. 2026 리뷰, SCAN | doi:10.1093/scan/nsag090 | [db] | 초록 | 신뢰도 기반 대 가치 기반 이중 경로 가설과 직접 검증 필요 |
| Abdollahi et al. 2025, "Probing Multimodal Fusion in the Brain" | arXiv:2507.19052 | [arXiv] | 초록 | 검색 요약은 "시청각 일치도에 따라 예측 성능이 달라진다"고 했으나 **초록에는 그 내용이 없다.** 근거로 쓰지 않는다 |

**(b) 판정: partially.** 음악과 화면 정서의 불일치가 정서 판단과 뇌 통합에 미치는 영향은 통제 조작으로 검정되었다(Pehrs 2014, Bravo 2024). 자연 영화에서 사운드트랙 특징과 공유 정서의 관계도 보고되었다(Muller-Rodriguez 2024). 조작 없이 AI로 채널을 분리해 자연 충돌 순간을 찾고, 신뢰도 가중 대 가치 우선 규칙을 가르는 연구는 찾지 못했다.

**남는 새 부분:** Emo-FilM 14편에서 AI로 분리한 화면, 배경 소리, 대사 정서의 자연 충돌 순간에서 뇌와 평정자가 어느 채널을 따르는지, 그 선택이 채널 신뢰도에 따라 바뀌는지.

**(c) 설계 함의**
* Bravo 2024가 '음악이 V1까지 움직인다'고 했으므로, 화면 채널 정서 head의 입력(V-JEPA 2 영상 feature)과 V1 반응 사이에 음악 효과가 섞일 수 있다. 감각 피질의 채널 고유 성분 해석에 주의한다.
* Pehrs 2014는 슬픈 음악에서 통합 효과가 컸다. '가치 우선' 예측(부정 채널 우세)의 사전 근거로 쓴다.

**overlap: Emo-FilM 연구**(같은 자료와 사전학습 멀티모달 feature. 질문은 채널 분해와 충돌 규칙으로 다르다).

---

## 3. 이전에 미검증으로 둔 3건의 재시도 결과

| 항목 | 이번 결과 | 상태 |
|---|---|---|
| VSS 2025 포스터(id=1989) | Crossref 서지 검색에서 doi:10.1167/jov.25.9.1989(J Vis 25(9):1989, 저자 Chen Y, Keil A, Ding M)를 찾았다. 초록은 Crossref에 없고 jov.arvojournals.org와 visionsciences.org는 프록시가 거부했다. 내용은 검색 요약 두 건(서로 일치)만 보았다 | **존재와 저자는 verified(Crossref).** 내용은 검색 요약 수준 |
| NeurIPS 2026 TRIBE v2 평가 | neurips.cc, OpenReview API는 프록시 거부. arXiv API 제목, 초록 검색과 Crossref 서지 검색에서 찾지 못했다 | **미검증 유지.** 검색 요약만 |
| Conwell 2023 ICLR workshop | iclr.cc, mlanthology.org는 이전 세션에서 해석 실패. arXiv 제목 검색과 Crossref에서 찾지 못했다. 대신 같은 저자군의 SLIP 대 SimCLR 정서(미) 평정 연구 arXiv:2410.23603을 [arXiv]로 확인했다 | **미검증 유지.** 근거는 arXiv:2410.23603으로 대체 |

* `outputs/agents/adversarial-reviewer/literature.jsonl`의 VSS 항목을 Crossref DOI로 갱신했다. 나머지 두 건은 미검증 표시를 유지했다.

## 4. 동의 편향 점검

* 원 제안자가 no로 둔 6개(C-02, C-16 묶음, C-18, C-19, C-08, C-27) 중 3개가 partially로 바뀌었다(C-16 묶음, C-18, C-27). C-02는 핵심 가설 기준으로 not found를 유지했다. 바뀐 이유는 모두 원 제안 검색에서 빠진 2024~2026 선행(Gao 2025, Soderberg 2026, Muller-Rodriguez 2024, Conwell et al. 2024 arXiv)이다.
* Soderberg, Jang & Kragel 2026은 C-16 묶음과 C-18 두 곳의 가장 가까운 선행이다. 같은 Kragel 그룹이 C-07(편도체 encoding), C-11(BLA 표상), C-12(합성 자극)와도 닿아 있어, 이 그룹의 2026년 출판물을 카드 작성 전에 한 번 더 훑을 것을 권한다.
* Ding, Keil 그룹(VSS 2025, VCA 2025, Leem 2026, Bo 2021, 2022)은 C-02, C-05, C-08 모두에 걸쳐 있다. 같은 쟁점(시각피질 정서 표상의 기원)을 계속 다루므로 선점 위험이 가장 큰 그룹이다.

## 5. 미확인 사항

1. NeurIPS 2026 TRIBE v2 평가 논문의 자료(Emo-FilM 여부), 정서 범주별 결과, 잔차 분석 여부. C-11의 1단계 판정이 여기에 달려 있다. neurips.cc 또는 openreview.net이 세션 네트워크에서 허용되어야 확인할 수 있다.
2. Chen, Keil, Ding 2025(VSS)의 초록 원문. jov.arvojournals.org 또는 visionsciences.org 허용이 필요하다.
3. Gao, Ajith & Peelen 2025의 fMRI 결과 세부(모델-뇌 정렬을 목표별로 비교했는지). bioRxiv 본문 접근이 필요하다.
4. Soderberg 2026의 두 자료가 무엇인지와 사용한 ANN의 학습 자료. C&K 프레임이 쓰였다면 우리 자료에 쓸 때 누수가 된다(초록에서는 확인 불가).
5. EmoMind에 회상 조건이 없다는 판단은 vision-decoding의 본문 기록에 기댄다. 이번에는 초록만 다시 보았다.
6. Liu 2025 VCA가 피드포워드라는 판단은 Crossref 초록(되먹임 언급 없음)과 검색 요약(본문 인용)에 기댄다.

## 6. 검색 기록 (모두 2026-11-12)

| 묶음 | # | 경로 | 질의 | 결과 |
|---|---|---|---|---|
| C-02 | 1 | WebSearch | "The Origin of Affect-specific Neural Representations of Emotional Scenes in Early Visual Cortex" Chen Keil Ding Journal of Vision 2025 | VSS 초록 요약(합성 fMRI, IAPS 비구분, 얼굴 구분) |
| C-02 | 2 | Crossref 서지 | 위 제목 | doi:10.1167/jov.25.9.1989 |
| C-02 | 3 | PubMed | (recall OR imagery OR remembered) AND (emotional OR emotion) AND (reinstatement OR reactivation OR decoding) AND (distortion OR exaggeration OR bias OR enhancement) AND fMRI AND (movie OR video OR scenes), 2016~ | 3건(Krenz 2025, Bowen 2017, Ritchey 2013) |
| C-02 | 4 | WebSearch | fMRI decoding of mental imagery or memory recall shows emotional scenes remembered more emotionally intense than perceived neural representation drift toward emotion 2024 2025 2026 | 방향 검정 없음. Krenz 2025, 학회 초록들 |
| C-02 | 5 | arXiv API | (imagery OR recall OR memory) AND fMRI AND (emotion OR emotional OR affective) AND (decoding OR reconstruction) | 5건, 해당 없음 |
| C-02 | 6 | PubMed | Kark SM[Author] AND Kensinger EA[Author] AND (reinstatement OR recapitulation) | Kark & Kensinger 2019 |
| C-02 | 7 | WebSearch | memory distortion emotional intensification recall exaggerated emotion ... neural reconstruction diffusion fMRI imagery decoding emotion | 행동 연구만(Cooper 2019 등) |
| C-02 | 8 | PubMed | Cooper RA[Author] AND Ritchey M[Author] AND memories fade | Cooper 2019 |
| C-02 | 9 | PubMed | "affective realism" OR ... , 2015~ | 9건, 모두 행동 또는 이론 |
| C-02 | 10 | arXiv API | id_list 2605.16739 | EmoMind 초록 v3 |
| C-16 | 1 | WebSearch | emotion-trained versus object-trained convolutional neural network predicts visual cortex or amygdala fMRI responses to emotional images comparison fine-tuning EmoNet AlexNet 2024 2025 | Gao, Ajith & Peelen 2025 |
| C-16 | 2 | Crossref | doi:10.1101/2025.02.19.638854 | 초록 확인 |
| C-16 | 3 | PubMed | Jang[Author] AND Kragel PA[Author] AND amygdala | Jang & Kragel 2025, **Soderberg 2026**, Jang 2026 BLA |
| C-16 | 4 | WebSearch | deep neural network model feedback from amygdala module to visual cortex layers emotional scenes reentry simulation 2025 2026 Ding Keil | VCA 피드포워드(본문 인용 요약), 되먹임 모델 없음 |
| C-16 | 5 | arXiv API | (emotion OR emotional OR affective) AND "visual cortex" AND ("neural network" OR CNN OR transformer) | 8건, 해당 없음 |
| C-16 | 6 | arXiv API | ti:"controlled assessment" OR (au:Conwell AND abs:SLIP) | arXiv:2410.23603 |
| C-18 | 1 | WebSearch | neural network trained on images with people or faces removed controlled rearing visual diet emotion recognition context brain alignment 2024 2025 2026 | 얼굴 없이 학습한 망의 얼굴 선택성만. 정서 없음 |
| C-18 | 2 | PubMed | (deep neural network ...) AND (face deprivation OR "without faces" OR "face-deprived" OR "controlled rearing" OR "diet") AND (face selectivity ...), 2019~ | 1,368건(질의가 넓음, 상위 20건 비관련). 폐기 |
| C-18 | 3 | PubMed | (Vinken K ... ) OR (Dobs K AND functional specialization) OR (Kanwisher N AND why questions) | Dobs 2022, Kanwisher 2023 등 6건 |
| C-18 | 4 | Crossref | doi:10.3389/fncom.2021.626259 | Xu 2021 확인 |
| C-19 | 1 | WebSearch | vision-language model trained with emotion words removed from captions emotion concept knowledge constructionist theory ... 2025 2026 | 없음 |
| C-19 | 2 | arXiv API | ("constructed emotion" OR constructionist OR "conceptual act") AND (model OR network OR "language model") | 2605.09522, 2605.07761 |
| C-19 | 3 | arXiv API | ("emotion words" OR "emotion concepts" OR "emotion vocabulary") AND (ablation OR removed OR removing OR without) AND (vision OR image OR CLIP) | 2건, 해당 없음 |
| C-19 | 4 | PubMed | (emotion concept knowledge OR emotion words OR emotion language) AND (neural network model OR language model OR deep learning) AND (constructionist OR ...), 2019~ | 13건 중 관련 2건(Souter 2021, Giraud 2023) |
| C-08 | 1 | WebSearch | recurrent processing required for emotion recognition in natural scenes ... Kar 2019 extension ... 2023 2024 2025 | 없음(차폐, 가림 연구만) |
| C-08 | 2 | PubMed | (recurrent OR recurrence OR feedback) AND (deep neural network OR CORnet OR convolutional) AND (emotion ...) AND (fMRI OR MEG OR EEG OR backward masking), 2019~ | 86건, 상위는 EEG 정서 인식 공학 |
| C-08 | 3 | PubMed | Decoding the temporal dynamics of affective scene processing | Bo 2022 |
| C-08 | 4 | arXiv API | (recurrent OR recurrence) AND (emotion OR affective OR valence) AND (brain OR fMRI OR "visual cortex" OR neural) AND (image OR scene OR visual) | 25건, 해당 없음 |
| C-08 | 5 | Crossref | doi:10.1038/s41593-019-0392-5 | Kar 2019 확인 |
| C-11 | 1 | WebSearch | "Evaluating TRIBE v2 Beyond Its Original Benchmarks" naturalistic emotion dataset Emo-FilM | NeurIPS 2026 요약, 자료 미확인 |
| C-11 | 2 | WebSearch | in silico brain encoding model TRIBE predicted response subtracted residual emotion naturalistic movie fMRI ... 2026 | 잔차 분석 연구 없음, 커뮤니티 피질하 head |
| C-11 | 3 | arXiv API | ti:TRIBE AND (abs:emotion OR abs:localizer); abs:"TRIBE v2" | NeurIPS 논문 없음. TRIBE v2 관련 7건 |
| C-11 | 4 | Crossref 서지 | NeurIPS 논문 제목 | 없음 |
| C-11 | 5 | PubMed | Emo-FilM OR (Morgenroth E AND emotion) OR (Ma AND Kragel PA AND emotion film), 2024~ | Morgenroth 2026, Ma & Kragel 2026, Chan 2026 등 9건 |
| C-27 | 1 | PubMed | (music OR soundtrack OR audiovisual) AND (incongruent OR incongruence OR conflict OR mismatch) AND (emotion OR emotional) AND (film OR movie OR video) AND fMRI, 2012~ | 12건, 직접 해당 없음 |
| C-27 | 2 | WebSearch | naturalistic movie fMRI audio visual emotion channels separated music source separation conflicting emotion visual versus soundtrack brain integration 2024 2025 2026 | Muller-Rodriguez 2024, Bravo 2024, Pehrs 2014 |
| C-27 | 3 | arXiv API | id_list 2410.17300, 2507.19052 | 초록 확인(2507.19052의 요약 주장은 초록에 없음) |
| C-27 | 4 | Crossref | doi:10.1073/pnas.2320378121, doi:10.1093/scan/nst169 | 두 건 확인 |
| 공통 | | curl 접속 시험 | openreview.net, api.openalex.org, visionsciences.org, neurips.cc, jov.arvojournals.org | 프록시 거부(우회하지 않음) |

---

## 7. Coordinator 추가 확인 (감사 뒤)

* **표본 재확인.** 감사에서 핵심으로 쓴 9건을 Coordinator가 직접 다시 확인했다. 서지와 초록이 감사 기록과 맞았다.
  * Crossref: Gao, Ajith & Peelen 2025(10.1101/2025.02.19.638854), Soderberg, Jang & Kragel 2026(10.1093/scan/nsag028), Cooper, Kensinger & Ritchey 2019(10.1177/0956797619836093), Chen, Keil & Ding 2025(10.1167/jov.25.9.1989), Conwell 2025(10.1073/pnas.2306025121)
  * PubMed: Souter 2021(PMID 34624259, 초록의 'valence 분류 보존, 부정 범주 구분 손상' 확인), Bo 2022(PMID 35931307, '200~300 ms 형성, 재귀 상호작용 시사' 확인)
  * arXiv: 2410.23603(Conwell 외, 미적 판단에서 언어와 시각 분리), 2410.17300(Muller-Rodriguez, 영화 음악 특징과 공유 정서)
* **NeurIPS 2026 TRIBE v2 평가 논문: 존재와 초록을 학회 공식 페이지로 확인했다(verified, publisher).**
  * 확인 경로: 사용자가 Stage 1에서 논문 사이트 허용을 승인했으므로 환경 허용 목록에 neurips.cc, api.openreview.net, api2.openreview.net, jov.arvojournals.org를 추가했다. 이후 https://neurips.cc/virtual/2026/poster/159782 를 열었다.
  * 서지: Skoullou E, Elbanna G, Conwell C, Kuniyoshi Y. NeurIPS 2026 Workshop "Foundation Models for the Brain and Body" 포스터. OpenReview id gGIIROJlMa.
  * 초록 요지: 지각, Multiple Demand, ToM 대비는 재현했다. 청각 언어 대비는 약했다. 자연 정서 영화에서 모델-뇌 대응이 정서 범주마다 크게 달랐고 일부 정서 조건에서 선택적 실패가 있었다.
  * 여전히 미확인: 사용 자료(초록에는 "연속 정서 주석이 있는 자연 정서 영화"로만 적혀 있다), 잔차 분해나 생리 분석 여부. OpenReview 본문과 API는 사이트가 로그인 확인(challenge)을 요구해 열지 못했다. 우회하지 않았다.
  * 판정 영향: C-11의 partially를 유지한다. 1단계(정서 영역에서 TRIBE가 실패하는가)는 이 논문과 겹친다고 보고 주 결과로 쓰지 않는다. 공저자 Conwell은 C-16 묶음의 선행(Conwell 2024, 2025) 저자이기도 하다.
  * `outputs/agents/coordinator/literature.jsonl`에 추가했다.
* **VSS 2025(Chen, Keil, Ding) 초록 원문:** jov.arvojournals.org가 브라우저 확인(JavaScript challenge)을 요구해 열지 못했다. 우회하지 않았다. 존재는 Crossref로 확인되어 있고 내용은 검색 요약 수준 그대로다.
