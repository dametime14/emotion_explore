# Round 3 Reviews: brain-inspired (Agent 11)

* 기준일: 2026-11-12. 절차: `reference/protocols.md` P3. 배정: `outputs/discussion/round3_assignment.md`(GI-P5, EF-P7, VD-P4).
* 읽은 원문: geometry-info round2.md GI-P5와 그 근거 chain(vision-decoding round1 R5, encoding-foundation round1 Chain 3 요약), encoding-foundation round2.md EF-P7과 multimodal-dynamics round1 Chain 3, vision-decoding round2.md VD-P4와 generative-counterfactual round1 S7, vision-decoding round1 0.2절, R1.
* "이미 연구되었는가"는 이번에 실제로 검색했다. 검색 경로와 날짜를 각 항목에 적었다. arXiv API는 이번 세션에서 429를 반복해 일부는 WebSearch와 Crossref로 대신했다(우회 없음). 검색 색인으로만 본 자료는 search_index로 표시하고 근거로 세지 않는다.
* 판정 형식: P3의 7개 질문에 각각 답하고 수정안을 쓴다. 모든 판정에 label-provenance와 evidence-level을 함께 적는다.

---

## 1. GI-P5 (geometry-info → vision-decoding): Spacetop "잔차 대 본인 보고 편차" 제안 6개를 기준선 multiverse 하나로

**제안 요지:** 같은 영상에서 기대 반응(기준선)을 뺀 개인 뇌 잔차가 그 사람 본인 정서 보고의 집단 대비 편차를 예측하는가. 다섯 에이전트가 기준선만 다르게(TRIBE 예측, LOO peer 평균, MLLM 예측, INT 개인화, rank 대역) 같은 질문을 냈으므로 하나의 사전등록 multiverse로 묶고, 기준선 간 차이 자체를 결과로 삼는다. 잔차 신뢰도 선행 보고, rank 대역별 분해, 정서 배제 캡션 통제 확장 포함.

| 판정 항목 | 판정 |
|---|---|
| 1. 이미 연구되었는가 | **부분적으로 그렇다.** 핵심 아이디어인 "개인 특이 신경 반응이 개인의 정서 경험을 반영한다"는 Chang et al. 2021(doi:10.1126/sciadv.abf7129)이 자연 시청 중 vmPFC 상태 동역학의 개인 특이성과 정서 경험의 관계로 이미 보고했다(Crossref 초록: "vmPFC ... exhibits unique idiographic spatiotemporal dynamics"; 세부 분석은 WebSearch 요약 수준). 개인 특이 반응과 개인 행동을 잇는 일반 틀(IS-RSA, idiosynchrony)은 Finn et al. 2020(doi:10.1016/j.neuroimage.2020.116828, DB 수록)이 정리했다. 개인화 반응 예측(INT)도 GI의 기존 기록에 있다. **새로운 부분은 (a) 기준선 5종 비교, (b) rank 대역 분해, (c) Spacetop의 본인 사후 평정에 적용**이다. 검색: WebSearch("idiosyncratic brain response deviation from group predicts individual self-reported emotion ratings naturalistic video fMRI functional alignment residual"), api.crossref.org(doi:10.1126/sciadv.abf7129 초록, Finn 2020 서지), 2026-11-12. 결과: 기준선 잔차와 본인 보고 편차를 직접 연결한 출판 연구는 이 경로에서 미발견 |
| 2. 단순한 모델 적용인가 | 아니다. 그러나 **방법 통합(multiverse)이 중심이라 이론적 질문이 흐려질 위험**이 있다. 다섯 기준선은 각각 다른 가설("평균 관찰자 의미에서 벗어남", "자극 구동 평균에서 벗어남", "peer 합의에서 벗어남")에 대응하므로, 기준선을 가설 단위로 이름 붙여야 결과가 해석된다 |
| 3. Neuroscience Question을 해결하는가 | 해결 가능성이 있다. 질문은 "개인 특이 신경 분산이 본인 정서 경험을 운반하는가"이며 Axis U(본인 대 peer 대 AI)와 emotion-theory의 privileged access 검정(C4)에 직접 답한다. 단 결과는 상관(R0)이며 "경험을 읽었다"는 해석은 금지(CLAUDE.md 6절) |
| 4. 정서가 아닌 visual/semantic을 decoding하는 것은 아닌가 | **위험이 크다.** 기준선을 빼고 남는 개인 잔차의 주된 출처는 정서가 아니라 개인별 시선과 주의, 머리 움직임, 각성 수준일 수 있다. Spacetop alignvideo의 7개 문항 중 "engaged"가 있어, 보고 편차 자체가 정서가 아니라 몰입 편차일 수 있다. 시선 차이는 Horikawa 원 저자도 한계로 들었다(doi:10.1016/j.isci.2020.101060, Limitations 마지막 단락). 생리(EDA, PPG)는 Spacetop 공개본에 없어 자율신경 성분을 직접 통제할 수 없다 |
| 5. 현재 Dataset으로 검증 가능한가 | **조건부.** Spacetop alignvideo는 49(또는 48)개 영상을 1회씩 보고, 평정 결측 약 51%, 평정 구간이 영상 끝 HRF와 겹친다(Stage 1). 단일 시청이라 "잔차 신뢰도"를 run 분할로 구할 수 없다. 영상 내 시간 절반 분할이나 내용이 비슷한 영상 쌍으로만 근사할 수 있는데, 둘 다 약하다. Horikawa + Mind captioning 부분은 본인 정서 보고가 없어 이 질문의 결과 변수가 없다(캡션 통제 확장은 다른 질문이다) |
| 6. 더 강력한 방법이 있는가 | 있다. (a) **IS-RSA**(Finn 2020): 참가자 쌍마다 신경 잔차 유사도와 보고 편차 유사도를 비교하면 결측에 강하고 기준선 선택에 덜 민감하다. (b) 보고와 신경 편차를 함께 모형화하는 계층 베이즈(피험자, 영상 확률효과)로 결측을 모형 안에서 처리. (c) 시선 공변량은 MR 기반 시선 추정(DeepMReye, doi:10.1038/s41593-021-00947-w)으로 eye tracker 없이 만들 수 있다(안구가 촬영 범위에 있을 때) |
| 7. 결과가 기대와 달라도 의미가 있는가 | 잔차가 **신뢰할 만한데** 보고 편차를 예측하지 못하면 "개인 특이 신경 분산은 정서 경험이 아닌 다른 개인차(지각, 주의)를 운반한다"는 유의미한 음성 결과다. 기준선 간에 결과가 갈리는 것도 정보다. 그러나 잔차 신뢰도가 확보되지 않으면 어떤 결과도 해석할 수 없다. 따라서 신뢰도 게이트가 사실상 전부를 결정한다 |

**수정안**
1. **게이트를 앞에 둔다.** 잔차 신뢰도(영상 내 시간 절반 분할, 비슷한 내용 영상 쌍 간 일관성)가 기준을 넘는 ROI와 기준선만 다음 단계로 보낸다. 기준을 넘는 조합이 없으면 그 자체를 보고하고 멈춘다.
2. **1차 분석을 IS-RSA로 바꾼다.** 기준선별 잔차로 참가자 쌍 신경 유사도 행렬을 만들고, 본인 보고 편차의 참가자 쌍 유사도 행렬과 비교한다. 개인별 회귀는 2차.
3. **기준선을 가설 단위 3개로 줄이고 나머지는 부록으로.** LOO peer 평균(규범 대리), TRIBE v2 예측(자극 구동 평균 뇌, in-silico), MLLM 예측(평균 관찰자 의미, AI 추정). INT와 rank 대역은 1차 결과가 나온 뒤의 해석 단계로 둔다. 다중비교 부담을 줄인다.
4. **비정서 개인차 공변량을 넣는다.** engaged 평정, 머리 움직임, MR 기반 시선 추정, 영상별 전역 신호 편차. 정서 문항(happy, sad, afraid 등)의 편차와 engaged 편차를 같은 분석으로 돌려 정서 특이성을 비교한다.
5. **가장 가까운 선행(Chang 2021)과의 차이를 사전등록에 명시한다:** 단일 영상(TV 에피소드) 대신 49개 영상 단위 반복, 본인 사후 평정, 기준선 비교.
* **표기:** label-provenance felt / 참가자 본인(Spacetop 사후). 기준선은 peer 합의, in-silico, AI 추정으로 분리. evidence-level R0. signal-feasibility는 vmPFC 신호 손실 점검 필요.

---

## 2. EF-P7 (encoding-foundation → multimodal-dynamics): In-silico 감각 박탈과 관찰된 무음 조건의 대조

**제안 요지:** TRIBE v2에 Emo-FilM을 영상만, 오디오만, 대사 텍스트만, 전체로 넣어 정서 관련 관찰 분산의 재현도를 비교하고(i), 관찰된 무음 조건(Horikawa, Mind captioning)에서 영상만 넣은 예측이 vmPFC 정서 기하를 얼마나 재현하는지 보고(ii), 음원 분리 stem 교체 반사실(iii)을 관찰된 음악 유무 구간 차이와 비교한다.

| 판정 항목 | 판정 |
|---|---|
| 1. 이미 연구되었는가 | **부분적으로 그렇다.** (a) 관찰 수준의 감각 제한 비교는 Lettieri et al. 2024(doi:10.1126/sciadv.adk6840)가 같은 영화의 단일 감각, 다감각 판본과 선천 맹, 농 참가자로 수행했다(vmPFC의 양식 무관 범주 부호, Crossref 초록 확인). (b) TRIBE의 양식 기여 ablation은 정서와 무관한 일반 지도로 수행되었다(arXiv:2507.22229, EF 자신 기록). (c) **"Evaluating TRIBE v2 Beyond Its Original Benchmarks: From Functional Localizers to Naturalistic Emotion"(NeurIPS 2026)**이 TRIBE v2를 연속 정서 주석이 있는 자연주의 영화로 평가해 정서 범주별 대응 차이와 청각 언어 조건의 선택적 실패를 보고했다는 검색 결과가 있다. 식별자를 찾지 못해 **search_index**로만 기록했고(literature.jsonl), 양식 ablation을 했는지는 미확인이다. 검색: WebSearch("encoding model modality ablation audio-only video-only predictions emotion vmPFC in silico TRIBE movie fMRI abstract affect code"), export.arxiv.org 제목 검색(결과 없음), api.crossref.org(결과 없음), 2026-11-12. **EF의 "partially" 판정에 동의하되, 위 NeurIPS 2026 평가를 Round 4 전에 본문 확인해야 한다** |
| 2. 단순한 모델 적용인가 | **상당 부분 그렇다.** (i)과 (iii)은 TRIBE에 입력을 가려 넣는 작업이며, 결과는 주로 TRIBE의 feature 추출기(V-JEPA 2, Llama 3.2, Wav2Vec-BERT)가 양식별로 무엇을 담는지에 대한 정보다. 과학적 기여는 (ii)의 "in-silico 무음 손실 = 관찰 무음 손실인가"라는 **모델 타당성 검정**에 집중되어 있다 |
| 3. Neuroscience Question을 해결하는가 | (ii)만 부분적으로. "vmPFC 정서 기하 중 영상 단일 양식으로 계산 가능한 부분은 얼마인가"는 Lettieri 2024의 양식 무관 부호 주장에 대한 자극 계산 수준의 보완이다. (i), (iii)의 in-silico 결과는 뇌에 대한 주장이 아니라 모델에 대한 주장이다(insilico-vs-observed 표기 필수) |
| 4. 정서가 아닌 visual/semantic을 decoding하는 것은 아닌가 | **위험이 있다.** 50항목 encoding의 재현도는 정서가 아니라 장면 의미의 재현도일 수 있다. 특히 대사 텍스트 입력 조건은 정서를 의미를 통해 운반한다(multimodal-dynamics Chain 3도 vmPFC 추상 부호의 언어 의존 가능성을 미해결로 남김). 정서 기하를 비교하기 전에 의미 feature로 설명되는 성분을 빼야 한다 |
| 5. 현재 Dataset으로 검증 가능한가 | **(ii)는 가능, (i)과 (iii)은 제한적.** 공개 TRIBE v2 checkpoint는 fsaverage5 피질의 평균 피험자 예측만 내고 피질하가 없다(encoding-foundation Round 1 요약 1번). 따라서 편도체, 시상 같은 limbic 표적은 빠진다. Horikawa와 Mind captioning은 원본 비디오를 보유하고(무음) 같은 자극에 관찰 fMRI가 있어 (ii)에 이상적이다. Mind captioning 72클립 5회 반복은 관찰 쪽 noise ceiling을 준다. Emo-FilM 대사 텍스트는 transcript 존재가 미확인(필요 시 ASR, AI 추정). TRIBE v2 라이선스는 CC BY-NC 4.0(EF 기록) |
| 6. 더 강력한 방법이 있는가 | (a) **관찰-관찰 전이**를 주 비교로 둘 수 있다. Emo-FilM에서 양식별 feature band(영상, 음악, 대사)로 학습한 encoder를 Horikawa 무음 자극에 영상 band만으로 적용해 관찰 Horikawa 반응을 얼마나 예측하는지 보면, in-silico 모델 대신 같은 연구에서 학습한 encoder로 "무음 조건의 정서 손실"을 잰다. (b) 관찰 무음 대비를 Emo-FilM 안에서 만들려면 음악 유무 구간 비교(R0)가 가장 직접적이다(EF도 (iii)에서 제안). (c) 의미 통제는 Mind captioning 정서 배제 인간 캡션(doi:10.1126/sciadv.adw1464)을 쓰는 것이 AI 캡션보다 낫다 |
| 7. 결과가 기대와 달라도 의미가 있는가 | 그렇다. in-silico 영상 전용 예측이 관찰 무음 정서 기하를 잘 재현하면 TRIBE v2를 무음 조건의 대리로 쓸 근거가 생기고, 재현하지 못하면 "in-silico 입력 제한은 관찰 감각 제한의 대리가 아니다"라는 분야 전체에 유용한 음성 결과가 된다(EmoMind에서 합성 뇌의 정서 RSA가 크게 떨어졌다는 기록, arXiv:2605.16739, 과도 연결). 다만 어느 쪽이든 결론은 모델 타당성에 관한 것이다 |

**수정안**
1. **(ii)를 1차 분석으로 올린다.** 같은 자극(Horikawa와 Mind captioning 비디오)에 대한 관찰 fMRI 대 TRIBE v2 영상 전용 예측. 지표는 정서 RSA(34범주 규범 평정 기반)이고, 상한은 Mind captioning 반복 기반 noise ceiling이다. 피질만 다룬다고 명시한다.
2. **정서 기하는 의미 제거 후 정의한다.** Mind captioning 정서 배제 인간 캡션 embedding으로 설명되는 성분을 뺀 잔차의 RSA를 정서 기하로 쓴다. 의미 제거 전후를 모두 보고한다.
3. **(i), (iii)은 2차로 내리고 "입력 제한 ablation"이라 부른다.** 결과는 TRIBE의 양식별 표상에 관한 것으로만 해석한다(EF 자신의 반론 대응과 같은 방향).
4. **관찰-관찰 전이 대조를 추가한다(위 6(a)).** in-silico와 관찰 encoder가 같은 결론을 내는지가 가장 강한 확인이다.
5. **선행 확인:** NeurIPS 2026 TRIBE v2 정서 평가 논문의 식별자와 본문을 확보한 뒤 새로움을 다시 판정한다.
6. 내 BI-P4(limbic 잔차의 관찰자 상태 변수)와는 피질하가 없다는 같은 제약을 공유한다. 두 제안 모두 피질하 결론은 관찰 데이터 쪽에서만 낸다.
* **표기:** label-provenance felt / 별도 평정자 규범(Horikawa 34범주, Emo-FilM 50항목). evidence-level R1(in-silico 입력 제한) + R0(관찰 대조). insilico-vs-observed 혼합. G1 필요(보유).

---

## 3. VD-P4 (vision-decoding → generative-counterfactual): 생성기의 정서 중립화를 재는 affect round-trip audit

**제안 요지:** Horikawa 원 프레임을 정답 CLIP, VDVAE latent로 보내 NSD 학습 생성기(SDXL unCLIP, Versatile Diffusion)로 재생성하고, Cowen & Keltner 비노출 정서 평가기와 소규모 인간 평정으로 정서 손실을 잰다. 뇌가 개입하지 않는 이 경로의 손실을 "생성기 고유 정서 중립화"로 정의하고, 뇌 해독 경로에서는 그 위에 더해진 손실만 뇌에 귀속한다. 역방향으로 의미(해독 캡션)는 고정하고 정서 방향만 다르게 생성한 두 후보 중 뇌 해독 latent에 가까운 쪽을 고르는 2AFC로 "의미와 별개인 정서 방향 정보"를 검정한다.

| 판정 항목 | 판정 |
|---|---|
| 1. 이미 연구되었는가 | **round-trip audit 자체는 미발견, 인접 요소는 있음.** 재구성 연구는 정답 latent로 재생성한 이미지를 상한으로 쓰는 관행이 있으나(VD 자신의 반론 1) 정서 축으로 측정한 사례는 이번 검색에서 찾지 못했다. vision-decoding Round 1(0.2절)도 MindEye2, Brain-IT, NSD-Imagery, MIRAGE 본문에 정서 평가가 없음을 키워드 검색으로 확인했다. 생성 모델의 정서 조작 자체는 EmoGen(arXiv:2401.04608, CLIP 공간에 정렬한 정서 공간)처럼 존재한다. 검색: WebSearch("fMRI image reconstruction emotional content preserved valence of reconstructed images evaluation diffusion decoding emotion fidelity"), 2026-11-12. 결과: Takagi & Nishimoto 계열과 MIRAGE(arXiv:2605.17198)는 의미, 저수준 충실도만 평가. 정서 충실도 평가는 미발견(이 경로 안에서) |
| 2. 단순한 모델 적용인가 | **절반은 그렇다.** round-trip은 연구 질문이라기보다 **방법론 통제(감사 절차)**다. 그 자체로는 정서에 대해 새로 알게 되는 것이 없다. 과학적 질문은 2AFC 부분("뇌 latent에 의미와 별개인 정서 방향 정보가 있는가")에 있다. 두 부분을 한 제안으로 묶되 기여 수준을 구분해 표시해야 한다 |
| 3. Neuroscience Question을 해결하는가 | 2AFC 부분은 그렇다. 시각 영역(또는 영역 추가 decoding) 해독 latent가 의미 고정 조건에서도 정서 방향을 운반하는지는 0.3절 공통 쟁점(정서 대 시각-의미 분리)에 직접 답한다. 내 관점에서는 생성기 prior가 예측 처리의 사전분포에 해당하므로, round-trip 손실은 "강한 시각 사전분포가 정서 정보를 얼마나 평탄화하는가"라는 구성주의 정서 이론의 계산 비유(vision-decoding 4절 개념 2)에 정량 근거를 준다(해석은 비유 수준) |
| 4. 정서가 아닌 visual/semantic을 decoding하는 것은 아닌가 | **2AFC의 "정서 방향" 정의가 핵심 위험이다.** CLIP 공간의 정서 방향(EmoGen 방식)은 의미 방향(예: 어두움, 피, 폐허)과 얽혀 있어, 의미 캡션을 고정해도 정서 방향 편집이 저수준 속성(밝기, 채도)과 의미 세부를 함께 바꾼다. VD 자신도 반론 4에서 편집 가족을 여럿 두자고 했다. 정서 방향이 인간 정서 평정이 아니라 텍스트 프롬프트로 정의되면 "정서"가 아니라 "정서 단어와 공기하는 시각 의미"를 검정하게 된다 |
| 5. 현재 Dataset으로 검증 가능한가 | **대체로 가능.** Horikawa와 Mind captioning 원본 비디오 보유, NSD 학습 생성기 공개(라이선스는 검색 수준). Mind captioning은 72클립 반복이 있어 해독 latent 신뢰도를 구할 수 있다. 제약: (a) C&K 비노출 정서 평가기가 필요하다(EmoNet은 누수로 사용 불가, doi:10.1126/sciadv.aaw4358). EmoSet 학습 평가기는 라이선스 미확인이고 정지 이미지 영역이다. (b) 소규모 인간 평정(R2)은 신규 수집이 필요하다. (c) 프레임 하나를 고르면 움직임이 운반하는 정서가 빠진다(VD 반론 3) |
| 6. 더 강력한 방법이 있는가 | (a) **정서 방향을 인간 규범 평정으로 정의**한다: Horikawa 34범주/14차원 규범 평정을 CLIP(또는 해독 latent) 공간에 회귀해 얻은 방향을 쓰면, 프롬프트 기반 방향보다 "정서" 정의가 덜 자의적이다. (b) **guidance 강도 곡선**: 생성 prior 강도를 바꾸며 정서 손실을 재면 중립화가 prior에서 오는지 직접 보인다(vision-decoding I2 "prior-vs-evidence 분해"). (c) **affective metamer 논리**(adversarial-reviewer I6): 정서 평가기와 인간이 같은 정서로 판단하지만 저수준 통계가 다른 이미지 쌍으로 평가기 자체를 먼저 검증. (d) 생성 경로를 정지 이미지 대신 비디오 생성기로 두는 대조 |
| 7. 결과가 기대와 달라도 의미가 있는가 | 그렇다. 생성기 round-trip에서 정서 손실이 작으면 재구성의 정서 손실은 뇌와 decoder 쪽 문제로 좁혀진다. 손실이 크면 생성형 decoding과 편집 기반 정서 연구 전체에 보정이 필요하다는 방법론적 결론이다. 2AFC가 우연 수준이면 "시각 영역 해독 latent에는 의미와 별개인 정서 방향 정보가 없다"는 해석이 가능하지만, decoder 적합도와 해독 latent 신뢰도가 확보된 경우에만 그렇다 |

**수정안**
1. **두 부분을 분리 표시한다.** (A) round-trip audit = 방법론 인프라(새로움 낮음, 모든 생성 decoding과 편집 연구의 공통 전제), (B) 의미 고정 2AFC = 과학적 질문.
2. **정서 방향을 인간 평정으로 정의한다(6(a)).** 프롬프트 방향은 비교 조건으로만 쓴다.
3. **guidance 강도 곡선을 1차 지표로 둔다(6(b)).** 단일 강도의 손실값 대신 강도별 손실 곡선과 기울기를 보고한다.
4. **인간 평정(R2)으로 평가기를 보정한다.** Mind captioning 72클립의 원 프레임과 재생성 프레임에 소규모 인간 정서 평정을 받아 AI 평가기의 편향을 추정하고(adversarial-reviewer I1의 prediction-powered 보정 논리), 전체 2,180클립 결과에 반영한다.
5. **영역 추가 decoding과 연결한다.** 시각피질 해독 latent에 피질하, 변연계 voxel을 더했을 때(vision-decoding R1, VD-P5) 2AFC 정확도가 오르는지 보면, 정서 방향 정보가 어디서 오는지까지 답한다. 이 단계는 signal-feasibility 판정을 통과한 영역만 쓴다.
6. **움직임 정서 손실을 따로 잰다.** 다중 프레임 평균과 비디오 생성 경로를 함께 두고 단일 프레임 경로와의 차이를 "움직임이 운반하는 정서"의 하한 추정으로 보고한다.
* **표기:** label-provenance 원 자극 felt / 별도 평정자 규범, 재생성 평가는 perceived / AI 추정(평가기) 또는 신규 별도 평정자(R2). evidence-level R1(모델 내) + R2(인간 평정 추가 시). insilico-vs-observed in-silico(round-trip), 혼합(뇌 경로). G1 필요(보유).

---

## 4. 세 검토의 공통 지적

1. **신뢰도 게이트 먼저.** GI-P5(잔차 신뢰도), EF-P7(관찰 noise ceiling), VD-P4(해독 latent와 평가기 신뢰도) 모두 결과 해석이 측정 신뢰도에 달려 있다. Mind captioning 72클립 5회 반복이 세 제안 모두에서 가장 중요한 공통 자원이다.
2. **in-silico와 관찰의 결론을 분리 표기.** EF-P7과 VD-P4는 모델 타당성 검정이 핵심이며, 뇌에 대한 주장은 관찰 데이터 쪽에서만 낸다.
3. **정서 대 의미 분리의 공통 도구로 Mind captioning 정서 배제 인간 캡션을 쓴다.** EF-P7의 기하 비교, VD-P4의 2AFC, GI-P5의 캡션 통제 확장 모두에 같은 통제가 쓰일 수 있다.

## 5. 이번 검토에서 literature.jsonl에 추가한 항목

* "Evaluating TRIBE v2 Beyond Its Original Benchmarks: From Functional Localizers to Naturalistic Emotion"(NeurIPS 2026): verified_by search_index, 식별자 미확인. verified로 세지 않는다.
* (Round 2 응답에서) doi:10.1073/pnas.2109889118, doi:10.1126/sciadv.ade6049: Crossref 확인.
* 그 밖에 인용한 Chang 2021, Finn 2020, Lettieri 2024, EmoGen, DeepMReye 등은 `outputs/literature/literature_db.csv` 또는 내 jsonl에 이미 있는 verified 항목이다.
