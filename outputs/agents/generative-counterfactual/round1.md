# Round 1: Independent Discovery (generative-counterfactual, Agent 9)

* 작성: generative-counterfactual (주 담당 Axis L Generative & Counterfactual Methods, Axis P Causality & Scientific Inference)
* 기준일: 2026-11-12
* 따른 절차: `reference/protocols.md` P1
* 읽은 파일: `CLAUDE.md`, `reference/protocols.md`(P1), `reference/axes.md`, `reference/starting_papers.md`, `reference/existing_projects.md`, `reference/datasets_and_resources.md`, `outputs/stage1/dataset_intelligence_report.md`, `outputs/stage1/environment_gaps.md`, `outputs/STAGE_STATUS.md`(사용자 결정 기록). 다른 에이전트 폴더는 읽지 않았다.
* 문헌: `outputs/agents/generative-counterfactual/literature.jsonl` 45편. 모두 식별자 경로(Crossref API, arXiv API, PubMed)로 존재 확인. 2024~2026년 24편, Affective Neuroscience 밖 분야 20편. 본문(Discussion, Limitations, Conclusion) 직접 확인 28편, 초록만 14편, 검색 요약만 1편, 서지만 2편.
* 전제(Stage 1 확정): 4개 데이터셋 모두 원본 자극 보유(G1 = 보유). Horikawa 1순위, Emo-FilM 병행. Horikawa 원자료는 2020-04-24부터 OpenNeuro ds002425 공개. 자극 편집과 파생물 제작의 저작권 조건은 미확인이며 제약으로 기록한다(9절).
* 표기: 문헌은 DOI 또는 arXiv ID로 단다. "본 에이전트 판단"은 문헌 주장이 아니라 내 해석이다.

---

## 0. 이 보고서의 중심 관점: 결론 수준 사다리

생성형 AI를 신경과학 분석 도구로 쓸 때 가장 흔한 오류는 "자극을 바꿨다(개입했다)"는 사실을 "뇌 또는 정서에 대한 인과 결론"으로 옮기는 것이다. 이번에 읽은 문헌들은 이 구분을 스스로 명시하기 시작했다. Grosbard et al. (arXiv:2605.16468, 6절 Limitations)은 counterfactual 편집 검증이 "모델 수준에서는 인과, 뇌에 대해서는 상관"이라고 썼고, Rothermel et al. (arXiv:2609.27729, Discussion 5.1)은 Good Regulator 정리를 들어 "예측과 개입은 동치가 아니다"라고 썼다. 그래서 모든 제안에 아래 수준을 붙인다.

| 수준 | 이름 | 무엇을 바꾸고 무엇을 측정하는가 | 결론할 수 있는 것 | 결론할 수 없는 것 | 우리 데이터로 가능? |
|---|---|---|---|---|---|
| R0 | 상관(관찰) | 자연 자극, 실측 fMRI, encoding/decoding | 자극 특징 또는 평정과 뇌 반응 사이의 통계적 의존, 정보의 존재 | 어떤 자극 특징이 반응을 일으키는지, 표상 여부 | 가능 |
| R1 | 모델 내 개입 (in silico) | 자극 편집 또는 latent 개입, encoding model 예측 변화 | 학습된 모델이 그 특징 변화에 민감한가 | 실제 뇌가 같은 방식으로 반응하는가 | 가능 (원본 자극 보유) |
| R2 | 실제 자극 개입 + 행동 측정 | 편집 자극을 사람이 보고 평정 | 자극 특징 변화가 정서 보고를 바꾸는가 (편집의 manipulation check) | 뇌 반응 | 신규 행동 평정 수집 필요 (비용 낮음, IRB 필요) |
| R3 | 실제 자극 개입 + 뇌 측정 | 편집 또는 선택 자극을 새 참가자에게 제시하고 fMRI | 자극 특징 → BOLD의 인과 | 그 영역 활동이 정서 경험을 만든다는 것 | 신규 fMRI 필요 (이번 범위 밖, 설계만) |
| R4 | 뇌 개입 | 자극, 병변, neurofeedback으로 영역 활동을 직접 바꿈 | 영역 활동 → 정서 보고의 인과 | | 불가 |

근거 문헌: R1 사례 Jang & Kragel (10.1523/JNEUROSCI.1436-24.2025), BrainACTIV (10.1101/2024.10.29.620889), Grosbard (arXiv:2605.16468). R2 사례 Sadeghi (10.1038/s41467-024-53668-6, Study 5), Rothermel (arXiv:2609.27729), Gilbert (10.1101/2025.11.03.686276). R3 사례 Gu (10.1038/s42003-023-05440-7), Tuckute (10.1038/s41562-023-01783-7), Gifford (10.1038/s41562-025-02252-z), NeuroVolve (arXiv:2512.00557). R3가 R4가 아닌 이유는 Ratan Murty (10.1038/s41467-021-25409-6, Discussion 6단락)와 Kriegeskorte & Douglas (10.1016/j.conb.2019.04.002, "Representational interpretations require additional assumptions" 절)가 명시한다: 영역에 정보가 있다는 것과 그 정보가 하류에서 읽혀 행동을 만든다는 것은 다르다.

**우리 데이터셋 안의 '진짜 개입'.** 관찰 데이터라도 실험 조작이 들어 있으면 그 조작에 한해 R3 수준 결론이 가능하다. Spacetop의 통증 과제는 기만 cue(높음/낮음)를 같은 열 자극 강도에 무작위로 붙이므로 cue → BOLD 효과는 데이터셋 내부의 실제 개입이다(Stage 1 보고서 4.3절). 반대로 Horikawa는 5명이 같은 자극 순서를 보았으므로(Stage 1 보고서 4.1절) 자극 효과와 순서, 이월(carryover) 효과가 설계상 분리되지 않는다.

---

## 1. 중요한 미해결 문제

### U1. 생성 모델로 '정서'를 조작하면 의미 내용이 같이 바뀐다
* 자연 자극에서 정서와 의미가 공선적이라는 문제(CLAUDE.md 6절)는 생성 모델로 옮겨도 그대로 남는다. 정서 편집 전용 모델 EmoEdit은 정서를 주로 내용을 추가해서(예: 묘지, 일몰) 유발한다(arXiv:2405.12661, 5 Conclusion). 뇌 유도 합성에서도 같다: NeuroVolve의 amygdala 최대화 이미지는 강한 표정의 얼굴, 최소화 이미지는 사람 없는 건물과 차량이었다(arXiv:2512.00557, Results "Amygdala modulation"). amygdala를 '움직인' 것은 얼굴, 사람 유무라는 의미 범주였을 수 있다.
* Abdel-Ghaffar et al.은 OTC의 '의미' tuning이 중위 구조 특징일 수 있으며 둘을 탈상관시킨 자극 세트가 필요하다고 썼다(10.1038/s41467-024-49073-8, Discussion 4단락). Horikawa et al.의 "emotion 모델이 visual, semantic 모델보다 우세"도 2020년 feature 집합에 상대적인 결론이다(10.1016/j.isci.2020.101060, Discussion 5단락).
* Sanchez & Tsaftaris는 교란이 있으면 분류기 gradient로 만든 개입이 교란 정보를 실어 do(x)가 올바르지 않다고 썼다(arXiv:2202.10166, 6절 Limitations). valence 분류기로 유도한 편집도 같은 문제를 갖는다(본 에이전트 판단).
* **미해결:** 의미 내용을 고정한 상태에서 정서 단서만 바꾼 자극에 대해 정서 관련 영역(또는 그 encoder)이 반응하는가. 2026-11 검색 범위에서 이 형태의 연구를 찾지 못했다.

### U2. In silico 정서 효과가 실제 뇌로 옮겨지는가
* 정서 영역에 대한 생성적 제어는 대부분 R1 또는 R2에 머문다. Jang & Kragel은 amygdala 하위영역 합성 자극을 사람이나 fMRI로 검증하지 않았다(10.1523/JNEUROSCI.1436-24.2025). Sadeghi et al.의 VV+/VV- 합성 이미지는 행동 평정으로만 검증되었다(10.1038/s41467-024-53668-6, Methods 5).
* R3까지 간 유일한 정서 영역 사례인 NeuroVolve에서도 생성 이미지가 자연 이미지 최상위(Natural High)보다 amygdala를 더 올리지 못했고, 하향 조절은 유의하지 않았다(p=0.088; arXiv:2512.00557, Results와 Discussion limitations).
* Rothermel et al.에서 자동 평가기의 valence 이동은 컸지만(-0.61에서 +1.03 SD) 인간 평정 효과는 작았고(기울기 0.038 SD/α) diffusion 단계가 효과를 약화시켰다(arXiv:2609.27729, Discussion 5.1).
* Gu et al.은 조절 효과 크기가 encoder 정확도에 비례한다고 보고했다(10.1038/s42003-023-05440-7, Discussion 1단락). 예측력이 낮은 피질하, 내측 전전두 영역에서는 in silico 결과가 더 불확실하다.
* **미해결:** 어떤 정서 영역, 어떤 편집 유형에서 R1 결과가 R3로 옮겨지는가. 옮겨지지 않는 경계(Rothermel의 '국소 선형 영역')는 어디인가.

### U3. In silico 뇌(surrogate)는 정서 표상 구조를 얼마나 보존하는가
* TRIBE v2는 고전 시각, 언어 실험을 in silico로 재현하지만, 입력이 시각, 청각, 의미 feature뿐이고 체성감각과 내수용 신호가 없으며 뇌를 수동적 관찰자로 다룬다(arXiv:2605.04326, Discussion 2단락). 정서 이론에서 내수용은 핵심 성분이다.
* EmoMind는 실측 fMRI를 TRIBE v2 예측으로 바꾸면 점 단위 정서는 일부 유지되나 클립 간 관계 구조가 크게 손실된다고 보고했다(RSA ρ 0.635에서 0.166; arXiv:2605.16739, 5 Discussion 2단락). 다만 실측 값은 MindCaptioning 평가 클립, TRIBE 값은 Emo-FilM 영화에서 얻어 자극 집합이 다르다(같은 논문 A.10과 4.2). 장치(실측 vs 합성) 효과와 자극 효과가 섞여 있다(본 에이전트 지적).
* **미해결:** 같은 자극에서 실측과 surrogate의 정서 표상 구조가 어디서 어긋나는가. 우리 데이터셋은 TRIBE v2 학습/평가 목록(CNeuroMod, BoldMoments, Lebel2023, Wen2017; NNDb, LPP, Narratives, HCP)에 없으므로(arXiv:2605.04326, Table 1, 5.7절) 이 비교에 깨끗하게 쓸 수 있다.

### U4. 생성 자극 자체의 confound: AI다움, 신기성, 사전학습 오염
* AI 생성 정서 사진은 원본과 같은 방향의 효과를 내지만 효과 크기가 작고, 중립 AI 사진은 원본 중립보다 LPP가 컸다(10.1101/2025.11.03.686276, Discussion 4단락). NeuroVolve 생성 이미지는 V4, V8 등 중위 시각영역과 OFC 일부 반응이 자연 이미지보다 컸고 저자들은 이를 부자연스러움에 따른 하향 처리 관여 가능성으로 해석했다(arXiv:2512.00557, Results). amygdala는 신기성에 민감한 비정상 반응을 보인다(10.1038/s41467-024-49073-8, Discussion 6단락). 생성 자극의 '정서 효과'에 신기성, 현저성이 섞일 수 있다.
* Feather et al.은 모델 표상을 맞춘 자극이 인간에게 전혀 다르게 지각될 수 있음을 보였다(10.1038/s41593-023-01442-0, Discussion). encoder가 높게 예측하는 자극이 인간에게 정서적으로 같지 않을 수 있다.
* **사전학습 오염:** EmoNet은 Horikawa 자극과 같은 Cowen & Keltner 2,185개 비디오의 137,482 프레임과 규범 정서 범주로 학습되었다(10.1126/sciadv.aaw4358, Materials and Methods). Horikawa 분석에서 EmoNet feature나 EmoNet 유도 편집을 쓰면 라벨 누수가 생긴다. V-JEPA 2 등 인터넷 영상 사전학습 모델(arXiv:2506.09985)이 같은 인터넷 출처 클립을 보았는지는 미확인이다.
* **미해결:** 생성 파이프라인 고유의 효과를 정서 효과와 분리하는 표준 대조군(null-edit, 재구성 통과 원본)이 정서 연구에 정착되지 않았다.

### U5. 평정 주체가 허용하는 인과 구조
* Horikawa와 Emo-FilM의 주 라벨은 fMRI 참가자가 아닌 별도 평정자의 규범 평정이다(Stage 1 보고서 3.2절; Horikawa 2020 Limitations 1단락). 이 경우 인과 그래프는 "자극 → 참가자 뇌", "자극 → 다른 사람의 평정"이며 참가자 뇌에서 평정으로 가는 경로가 없다. 따라서 "뇌가 정서 평정을 매개한다"는 매개 분석은 정의상 성립하지 않고, decoding 성공은 "평정을 예측하는 자극 특징의 정보가 뇌에 있다"는 뜻에 그친다(본 에이전트 판단, Kriegeskorte & Douglas 10.1016/j.conb.2019.04.002의 해석 규칙과 일치).
* Horikawa et al.은 발견된 표상이 1인칭 정서가 아니라 타인의 정서 예측(ToM)일 수 있다고 직접 썼다(Limitations 2단락).
* 참가자 본인 보고가 있는 Spacetop에서만 "자극 → 뇌 → 본인 보고" 매개 구조를 세울 수 있다. 그래도 무측정 교란(각성 상태, 주의), 평정 구간과 영상 끝 HRF의 겹침(Stage 1 보고서 4.3절) 때문에 R0를 넘지 않는다. Weichwald & Peters는 개입 데이터 부족과 올바른 변수 찾기를 핵심 난제로 꼽았다(10.1162/jocn_a_01623, 5절).
* **미해결:** 데이터셋별로 어떤 인과 질문이 원리적으로 식별 가능한지의 지도.

### U6. 어떤 정서 모델이 더 나은 뇌 모델인가를 자연 자극으로는 판정하기 어렵다
* 시각피질 정서 신호를 설명하는 후보는 최소 셋이다: 정서 스키마(EmoNet; 10.1126/sciadv.aaw4358), 저수준 생태 통계(VV; 10.1038/s41467-024-53668-6), 의미 범주 × 정서 상호작용(CSVA; 10.1038/s41467-024-49073-8). 자연 이미지에서 세 모델의 feature가 상관되어 있어 모두 유의한 설명력을 보일 수 있다. Kriegeskorte & Douglas의 single-model-significance fallacy가 그대로 적용된다.
* Golan et al.은 모델들이 서로 다르게 예측하도록 합성한 controversial stimuli에서 자연 자극과 다른 모델 순위가 나온다고 보였다(10.1073/pnas.1912334117, Discussion). 정서 모델 대상으로는 행동 수준의 표정 경계 자극 연구(arXiv:2507.14549, 초록)만 찾았고 뇌 encoder 판정은 찾지 못했다.

### U7. 청각, 시간, 서사 성분의 인과 기여는 관찰 데이터로 분리되지 않는다
* Jang & Kragel의 amygdala 모델은 정적 시각 feature만 써서 청각, 언어, 습관화, 학습을 포착하지 못한다고 썼다(Discussion 7단락). Horikawa 데이터는 무음이다.
* 영화에서는 음악이 정서 장면에 맞춰 편집되므로 음악 효과와 장면 효과가 공선적이다. Ma & Kragel은 hippocampal 정서 표상이 시청각, 언어 특징이 다른 영화들 사이에서 일반화되었다는 점을 감각 신호 추상화의 근거로 들었는데(10.1038/s41467-025-68240-z, Discussion 1단락), 영화 간 일반화는 감각 특징 통제와 같지 않다(본 에이전트 판단).
* **미해결:** Emo-FilM에서 음악, 대사, 효과음 각각이 정서 관련 반응에 주는 기여. 3-stem 분리 기술(arXiv:2110.09958)이 있으나 정서 신경 연구에 쓰인 사례를 찾지 못했다.

---

## 2. 주목할 모델과 방법론

라이선스는 이번 세션에서 저장소 파일을 직접 열지 못한 경우가 많아 확인 수준을 함께 적는다. "미확인"은 사용 전 확인이 필요하다는 뜻이다.

| # | 모델/방법 | 용도 (Axis) | Pretrained weights | Input → Output | 학습 목표 | 라이선스 (확인 수준) | 주의점 |
|---|---|---|---|---|---|---|---|
| M1 | **TRIBE v2** (arXiv:2605.04326) | 편집 자극의 in silico 뇌 반응, 실측 대비 surrogate 기준선 (H, L) | 공개 (Hugging Face facebook/tribev2, 검색 수준) | video + audio + text → 고해상도 피질 반응 예측 (정확한 공간 단위는 본문에서 재확인 필요) | 다중 피험자 fMRI 회귀 | CC BY-NC 4.0 (검색 결과 기준, 저장소 미열람). text encoder에 LLaMA 3.2-3B 게이트 필요 | 내수용, 체성감각 입력 없음. 우리 4개 데이터셋은 학습 목록에 없음 |
| M2 | **NeuroVolve** (arXiv:2512.00557) | 다중 영역 목표 자극 생성, '+amygdala, 범주 영역 고정' 목표 (L, E) | encoder는 NSD로 직접 학습 필요. 생성기는 BLIP-Diffusion(공개) | seed image + 뇌 반응 목표 → 이미지 | Q-Former embedding에 대한 encoder 예측 gradient 최적화, 별도 validation encoder로 선택 | 코드 공개 여부, 라이선스 미확인 | 의미 범주로 수렴하는 경향(U1) |
| M3 | **BrainACTIV** (10.1101/2024.10.29.620889) | 참조 이미지 기반 최소 편집으로 영역 선호 속성 탐색 (L, R) | Stable Diffusion + IP-Adapter + CLIP (공개) | 참조 이미지 + ROI encoder → 편집 이미지 | CLIP 공간 spherical interpolation, SDEdit | 코드 저장소 존재(검색), 라이선스 미확인 | α, γ로 의미 유사도와 구조 충실도의 trade-off |
| M4 | **RNC** (10.1038/s41562-025-02252-z) | 두 영역 반응을 정렬/분리시키는 자극 탐색 (L, K) | NSD encoder 학습 필요 | 이미지 풀 + 두 영역 encoder → controlling image | univariate, multivariate 정렬/분리 목적 최적화 | 미확인 | 생성이 아닌 선택 중심이라 AI다움 confound가 적음 |
| M5 | **Concept Sliders** (arXiv:2311.12092) | 정서 단서(표정 강도, 밝기)의 연속 dose-response 자극 (L) | 공개 슬라이더 일부, SD 1.x/SDXL 기반 | 프롬프트 또는 이미지 + 슬라이더 강도 → 이미지 | 저차원 LoRA 방향, 보존 속성 명시 | 코드 MIT로 알려짐, 미확인. 기반 SD는 CreativeML OpenRAIL 계열 | 잔여 간섭(8절 Limitations) |
| M6 | **LivePortrait** (arXiv:2407.03168) | 영상 속 인물 표정만 retargeting (L, B) | 공개 | 원본 영상/이미지 + 구동 표정 → 영상 | implicit keypoint 기반 재구성 | 미확인 (얼굴 검출 구성요소의 비상업 조건 가능성) | 다수 인물, 가림, 큰 동작에서 품질 미확인 |
| M7 | **FLUX.1 Kontext** (arXiv:2506.15742) | 정지 프레임 지시문 편집, 인물 일관성 (L) | [dev] 가중치 공개로 알려짐 | 이미지 + 지시문 → 이미지 | flow matching | 비상업 라이선스로 알려짐, 미확인 | 영상 프레임 간 일관성 없음 |
| M8 | **Wan** (arXiv:2503.20314) | 영상 단위 counterfactual(배경 맥락 교체, 동작 속도) (L, D) | 공개 1.3B/14B | 텍스트/이미지/영상 → 영상 | diffusion transformer | Apache 2.0으로 알려짐, 미확인 | 원본 충실도와 시간 일관성 별도 평가 필요 |
| M9 | **3-stem 영화 음향 분리** (DnR, arXiv:2110.09958) + **HT Demucs** (arXiv:2211.08553) | Emo-FilM 음악/대사/효과음 counterfactual (L, M) | DnR baseline, HT Demucs 공개 | 혼합 음향 → stem | 분리 손실 | HT Demucs MIT로 알려짐, 미확인 | 분리 잡음. 원 stem 재합성 대조군 필요 |
| M10 | **EmoEdit** (arXiv:2405.12661), **EmotiCrafter** (arXiv:2501.05710) | 정서 유발 편집과 연속 V-A 생성. 2x2 설계의 '의미 변경' 양성 대조 (L, A) | 공개 여부 미확인 | 이미지/프롬프트 + 정서 → 이미지 | Emotion adapter, V-A embedding mapping | 미확인 | 의미 경로 편집기라 의미 고정 정서 편집에는 부적합 |
| M11 | **EmoNet** (10.1126/sciadv.aaw4358) | controversial stimuli의 후보 모델 (I) | 공개(저자 저장소로 알려짐, 미확인) | 이미지 → 20 정서 범주 | AlexNet 최종층 재학습 | 미확인 | Horikawa에는 사용 금지(라벨 누수) |
| M12 | **Controversial stimuli / model metamers** (10.1073/pnas.1912334117; 10.1038/s41593-023-01442-0) | 정서 모델 판정, encoder 불변성 시험 (L, T) | 방법론 | 후보 모델 쌍 → 불일치 최대 자극 | controversiality index 또는 활성 일치 최적화 | 해당 없음 | metamer 통과는 충분조건 아님 |
| M13 | **Interchange intervention** (arXiv:2106.02997) | 뇌 encoder 내부의 정서 정렬 latent가 예측 출력을 매개하는지 (R, P) | 방법론 | 두 입력의 내부 표상 교환 → 출력 변화 | 해당 없음 | 해당 없음 | 모델에 대한 결론이지 뇌에 대한 결론이 아님 |

데이터셋별 encoder 학습에 쓸 feature extractor는 V-JEPA 2(arXiv:2506.09985) 등이 후보이나 overlap: EmoBrain (V-JEPA2 사용)이다.

---

## 3. 다른 분야에서 가져올 연구 아이디어

각 항목 끝에 결론 수준을 적는다.

**X1. Controversial stimuli를 정서 모델 판정에 (인지계산신경과학 → 정서).** EmoNet, VV 모델, CLIP 기반 valence probe가 서로 반대 valence를 예측하도록 이미지를 합성한다. NSD 학습 encoder의 시각피질, amygdala 예측과 인간 평정이 어느 모델을 따르는지 본다. Golan et al.의 Discussion은 controversiality index 대신 모델 사후분포 엔트로피를 줄이는 최적 실험 설계를 미래 과제로 남겼다(10.1073/pnas.1912334117). 수준: R1 + R2.

**X2. Model metamer를 'affective metamer'로 (청각, 시각 계산신경과학 → 정서).** (a) 정서 관련 voxel의 encoder 예측은 같지만 의미 embedding이 크게 다른 자극 쌍, (b) 의미 embedding은 같지만 예측 정서 반응이 다른 쌍을 만든다. 인간이 (a)를 정서적으로 같다고, (b)를 다르다고 판단하는지 본다. encoder의 불변성이 인간 정서 판단의 불변성과 일치하는지 보는 보완 벤치마크다(10.1038/s41593-023-01442-0, Discussion "Limitations": 통과는 충분조건이 아니고 실패가 표상 부재를 뜻하지 않음). 수준: R1 + R2.

**X3. Counterfactual invariance stress test를 정서 decoder에 (인과 ML → 정서).** Horikawa에서 학습한 정서 decoder가 '정서를 바꾸지 않는 의미 편집'에 불변인지 시험한다(arXiv:2106.00545, 7 Discussion). 편집 자극의 실측 뇌 반응이 없으므로 "편집 자극 → encoder 예측 뇌 → decoder"의 합성 경로로만 시험할 수 있다. EmoMind가 보인 surrogate의 구조 손실(arXiv:2605.16739)을 고려하면 이 시험은 decoder의 shortcut을 드러내는 선별 도구이지 최종 판정이 아니다. 수준: R1.

**X4. Interchange intervention을 뇌 encoder 해석에 (mechanistic interpretability → 정서).** TRIBE v2 내부에서 Emo-FilM 1 Hz 평정으로 정서 정렬 방향을 찾고, 클립 A의 그 성분을 클립 B에 교환했을 때 amygdala, vmPFC 예측이 정서 방향으로 바뀌는지 본다(arXiv:2106.02997). 'surrogate 뇌가 정서 같은 변수를 경유해 정서 영역 반응을 예측하는가'라는 모델 내부 매개 분석이다. 결과는 모델에 관한 것이다. 수준: R1.

**X5. Content/style 식별성을 counterfactual 쌍 설계 원칙으로 (인과 표상학습 → 정서).** von Kugelgen et al.은 augmentation 선택이 content와 style의 분할을 암묵적으로 정의한다고 경고했다(arXiv:2106.04619, 6 Discussion). 정서 counterfactual 쌍도 같다: 어떤 편집을 '정서 편집'으로 정하느냐가 '정서'의 조작적 정의가 된다. 편집 가족(표정, 조명/색, 동작 속도, 음악)을 사전에 명시하고 결과가 여러 가족에서 유지되는지 보고한다. Weichwald & Peters의 분포 강건성 원리와 결합하면, 여러 편집 가족(환경)에서 불변인 encoder 가중치만 '정서 인과 후보'로 남긴다(10.1162/jocn_a_01623). 수준: R1.

**X6. 모델 선택(selection) 기반 drive/suppress (언어 신경과학 → 정서).** Tuckute et al.은 생성이 아니라 대규모 문장 풀에서 모델로 선택한 문장으로 새 참가자의 언어 네트워크를 실제로 조절했다(10.1038/s41562-023-01783-7). 정서에서는 Horikawa 2,181 클립이 선택 풀이다. Horikawa로 학습한 encoder로 Emo-FilM 장면이나 Spacetop 영상 중 특정 정서 영역을 가장 구동/억제할 자극을 고르면 AI다움 confound가 없다. 현재 데이터로는 cross-dataset 예측 검증(R0)까지, 실측 검증은 R3. Tuckute의 미래 과제(네트워크 내 특정 영역만 선택적으로 구동, Discussion 마지막 단락)를 정서 네트워크(amygdala vs insula vs vmPFC)에 적용한다.

**X7. 영화 음향 3-stem 분리 (음향 신호처리 → 정서).** Emo-FilM 음향을 대사, 음악, 효과음으로 분리하고(arXiv:2110.09958) 음악 제거, 반대 정서 음악으로 교체한 counterfactual을 TRIBE v2에 넣는다. 수준: R1, 신규 평정 시 R2.

**X8. Closed-loop Bayesian 최적화 (실시간 fMRI 방법론 → 정서).** Lorenz et al.의 neuroadaptive Bayesian optimization(10.1038/s41467-018-03657-3, 초록)을 생성 자극 공간에 적용해 amygdala와 시각피질 반응을 최대로 분리하는 자극을 실시간 탐색한다. 신규 수집 계획용이며 현재 데이터로는 오프라인 근사(R1)만 가능하다.

---

## 4. 예상 밖으로 연결될 수 있는 개념

**C1. Good Regulator 정리와 정서 조절.** Rothermel et al.은 "예측과 개입은 동치가 아니다: 결과를 예측하는 모델이 그 결과를 바꾸는 방법을 알려주지는 않는다"를 신경 surrogate의 핵심 한계로 썼다(arXiv:2609.27729, Discussion 5.1). 정서 연구로 옮기면, 정서 반응을 가장 잘 예측하는 encoder와 정서 반응을 가장 잘 바꾸는 자극 편집이 서로 다른 feature에 기대고 있을 수 있다. "잘 예측되는 영역"과 "잘 조절되는 영역"의 불일치 자체가 측정 대상이 된다. 정서 조절(reappraisal)을 제어 문제로 보는 관점과 이어진다(관련 preprint arXiv:2507.10861은 존재만 확인, 본문 미열람).

**C2. Metamer, 불변성 클래스와 구성주의 정서 이론.** 정서 범주를 '관찰자 또는 뇌 영역이 무시하는 변환들에 대한 동치류'로 정의하면, 생성 모델로 그 변환을 직접 찾을 수 있다. 어떤 변환(의미 교체, 저수준 통계 교체)에 정서 영역 반응이 불변인지가 곧 그 영역의 '정서 개념'의 경계다. 구성주의가 말하는 범주 내 변이(variable instances)를 실험적으로 표집하는 방법이 된다(Feather 10.1038/s41593-023-01442-0의 틀을 옮김, 본 에이전트 판단).

**C3. 모델 결정 경계와 정서의 모호성, 평정자 불일치.** Deng et al.은 ANN 결정 경계 근처 표정 자극이 인간 지각 변산도 키운다고 보고했다(arXiv:2507.14549, 초록). Emo-FilM 평정자 간 일치가 0.38~0.39로 낮은데(Stage 1 보고서), 그 불일치가 정서 모델들의 불확실 구간에 몰려 있는지 확인할 수 있다. 그렇다면 label noise의 일부는 측정 오류가 아니라 자극의 정서적 모호성이며, 모델 불확실성을 reliability 가중치로 쓸 수 있다.

**C4. 텍스처 합성(생태 통계)과 visual valence, biophilia.** Sadeghi et al.의 VV는 저수준 생태 통계에서 직접 valence를 읽는다는 주장이다(10.1038/s41467-024-53668-6, Discussion 2, 5단락). 텍스처 합성처럼 저수준 통계는 보존하고 의미를 파괴한 자극을 만들면 '직접 지각 경로'만 남긴 자극이 된다. 반대로 의미는 보존하고 저수준 통계를 반대 VV 쪽으로 옮긴 자극을 만들면 두 경로를 경쟁시킬 수 있다.

**C5. Cocktail fork 문제와 영화의 다중 채널 정서 유도.** 영화는 서사, 표정, 음악이 동시에 정서를 유도하도록 제작된다. 음향 분리 문제(arXiv:2110.09958)를 정서의 '채널 분리' 문제로 다시 읽으면, 채널별 기여와 상호작용(음악이 표정의 정서 해석을 바꾸는가)을 in silico로 분해할 수 있다.

---

## 5. 새 Sub-axis 또는 하위 연구 방향

| ID | 이름 | 소속 Axis | 내용 | 독립 Axis 필요? |
|---|---|---|---|---|
| S1 | **Semantics-clamped affective counterfactuals** | L (B, C와 연결) | 의미 내용(캡션 embedding, 객체 구성)을 고정하고 정서 단서만 바꾸는 편집, 그 반대 편집, 2x2 설계. manipulation check(인간 평정)와 의미 불변성 측정을 필수로 함 | 아니오. L의 핵심 Sub-axis |
| S2 | **Relational/joint neural control of affective regions** | L × E | '+amygdala, FFA/EBA/PPA 고정', 'vmPFC 정렬, hippocampus 분리' 같은 다중 영역 목표(RNC, NeuroVolve 다중 목표) | 아니오 |
| S3 | **Surrogate-brain fidelity audit for affect** | L × H × T | 같은 자극에서 실측 vs TRIBE v2 예측의 정서 구조 비교, 잔차(실측 - 예측)의 정서 정보('residual affect') | 아니오 |
| S4 | **Temporal, auditory, narrative counterfactuals for film** | L × D × M × C | 음악 stem 제거/교체, 장면 순서 교체, 맥락 장면 교체 | 아니오 |
| S5 | **Evidence-level ladder (R0~R4) 표기** | P (T와 연결) | 모든 질문에 결론 수준을 필수 표기. 데이터셋 내부의 실제 조작(Spacetop cue) 목록화 | 아니오. P의 운영 규칙으로 |
| S6 | **Rater-structure causal graphs** | P × Q | 평정 주체(규범, 본인, 타인 지각, AI 추정)에 따라 식별 가능한 인과 질문의 지도 | 아니오 |
| S7 | **Generator-prior and AI-ness confound audit** | L × Q × S | null-edit 대조, 생성 파이프라인 단계별 효과 평가(Rothermel), 사전학습 오염 점검(EmoNet-Horikawa) | 아니오 |

독립 Axis가 필요하다고 보지 않는다. 다만 7절처럼 L과 P의 경계를 다시 긋는 것을 제안한다.

---

## 6. Discussion-to-Research chains

형식: `Original Finding → Unresolved Question → Technological Development → New Dataset / Model Combination → New Research Question`. 각 사슬 끝에 결론 수준, 반증 조건, 경쟁 설명, overlap, 선행 수행 여부를 붙인다.

### CH1. Horikawa의 'emotion 모델 우위'는 의미를 고정해도 남는가
* **Original Finding.** transmodal 영역(DMN 계열)에서 emotion category 모델이 visual object, semantic 모델보다 반응을 잘 설명했고, visual → semantic → emotion의 unimodal-transmodal gradient가 있었다. (Horikawa 2020, 10.1016/j.isci.2020.101060, Discussion 5단락)
* **Unresolved Question.** (a) 비교 기준인 visual, semantic feature 집합은 2020년 것(1000차원 DNN, 73 semantic 항목)이다. (b) 1인칭/3인칭 정서가 섞였을 수 있다(같은 논문 Limitations 2단락). (c) Abdel-Ghaffar et al.은 의미 효과가 중위 구조 특징일 수 있어 탈상관 자극 세트가 필요하다고 썼다(10.1038/s41467-024-49073-8, Discussion 4단락). 즉 자연 클립 안에서는 '정서 라벨이 더 잘 설명한다'와 '정서 라벨이 아직 측정되지 않은 의미, 중위 특징을 대신 운반한다'를 구분할 수 없다.
* **Technological Development.** 참조 이미지 고정 최소 편집(BrainACTIV, 10.1101/2024.10.29.620889, Discussion 2단락: 상관된 저, 중, 고수준 특징 분리용 자극 설계 도구로 제안), 간섭 최소화 연속 편집(Concept Sliders, arXiv:2311.12092, 8절 Limitations: 잔여 간섭 측정 필요), 표정 retargeting(LivePortrait, arXiv:2407.03168), counterfactual 편집으로 voxel 가설 검증(MINE, arXiv:2605.16468).
* **New Dataset / Model Combination.** Horikawa 원본 클립(G1 보유) 중 인물 중심 클립 부분집합 × 2x2 편집 [정서 단서 변경(표정, 조명/색, 동작 속도) / 의미 변경(EmoEdit식 객체 교체)] + Horikawa로 학습한 stimulus-computable voxelwise encoder(V-JEPA 2, DINOv2/CLIP, VLM 캡션 embedding feature; EmoNet은 누수로 제외) + TRIBE v2 zero-shot 예측(독립 surrogate). 편집의 정서 변화는 소수 부분집합에 대한 신규 인간 규범 평정(Cowen & Keltner 문항)으로 확인.
* **New Research Question.** Horikawa에서 emotion category 모델이 우세했던 voxel의 encoder 예측 반응은, 의미 내용(캡션 embedding과 객체 구성)을 고정하고 정서 단서만 바꾼 편집에 따라 변하는가, 아니면 정서를 고정하고 의미만 바꾼 편집에만 변하는가?
* **결론 수준.** R1 (+ manipulation check는 R2). 실제 뇌가 같은 방식으로 반응하는지는 R3가 필요하다.
* **반증 조건.** 정서 단서 편집(의미 embedding 변화 ≈ 0)에서 예측 변화가 없고 의미 편집에서만 변하면, 'emotion 우위' voxel의 encoder는 의미 정보로 정서 라벨을 예측하고 있었다는 해석이 지지된다. 단 **feature 공간 맹시**를 먼저 배제해야 한다: 편집이 encoder feature 자체를 거의 바꾸지 못하면 예측 불변은 '정보 없음'이지 '부정 결과'가 아니다. 그래서 편집마다 feature 변위와 인간 평정 변화를 함께 보고한다.
* **경쟁 설명.** encoder는 자연 상관 속에서 학습되어 정서 방향의 가중치가 의미를 대신 담고 있을 수 있다. 여러 feature 공간과 여러 편집 가족에서 일관되는지로 구분한다(X5).
* **overlap: EmoViS** (Horikawa 2020 사용, affective brain geometry의 sensory-semantic 기원 질문과 방향이 겹침).
* **선행 수행.** no (2026-11 검색: 정서 + counterfactual 편집 + encoding model 조합 미발견). 범주 선택 영역 대상 유사 방법은 BrainACTIV, MINE.

### CH2. 의미 범주를 고정해도 amygdala를 움직일 수 있는가
* **Original Finding.** amygdala encoding model이 규범 valence, 붉은색, 고주파 성분에 반응했고, 하위영역별 합성 자극이 시각적으로 구분되었다. (Jang & Kragel 2025, 10.1523/JNEUROSCI.1436-24.2025, Discussion 1, 6단락)
* **Unresolved Question.** 저자들은 이 정보가 시각 특이적 정서인지 감각 일반 정서인지(Discussion 5단락), 다른 자극으로 학습하면 무엇이 일반화되는지(8단락)를 남겼다. 이후 NeuroVolve는 amygdala 생성 자극을 실측 fMRI로 검증했지만 최대화 이미지가 표정 얼굴, 최소화 이미지가 건물과 차량이었고, 생성 이미지가 자연 최상위 이미지를 넘지 못했으며 하향 조절은 유의하지 않았다(arXiv:2512.00557, Results "Amygdala modulation", Discussion limitations). 즉 amygdala 조절은 지금까지 얼굴, 사람 유무라는 의미 범주를 통해서만 확인되었다.
* **Technological Development.** 영역 간 정렬/분리 공동 제어(RNC, 10.1038/s41562-025-02252-z, Discussion 3단락), 다중 영역 혼합 목표(NeuroVolve Discussion 3단락: "+V1, -FFA" 등), 표정 강도 연속 편집(Concept Sliders).
* **New Dataset / Model Combination.** NSD 8명으로 amygdala(aseg), FFA, EBA, PPA encoder 학습 → 목표 '+amygdala(또는 -amygdala), 범주 영역 예측 고정' → 별도 validation encoder(CLIP 기반)와 TRIBE v2로 교차 확인 → Horikawa, Emo-FilM으로 학습한 amygdala encoder로 교차 데이터셋 예측 → 소규모 인간 valence/arousal 평정.
* **New Research Question.** 얼굴, 신체, 장면 선택 영역의 예측 반응을 고정한 제약 아래에서 amygdala 예측 반응을 올리거나 내리는 편집이 존재하는가? 존재한다면 그 편집 방향은 인간 valence/arousal 평정과 어떤 관계인가(valence 단극 증가, 극단성 U자, 아니면 정서와 무관한 저수준 특징)?
* **결론 수준.** R1 + R2. R3 검증용 자극 세트 설계까지가 이번 범위다.
* **예측과 반증.** Jang & Kragel의 결과는 valence 단극성 + 극단성 비선형을, Sadeghi의 VV는 저수준 통계 경로를 예측한다. 범주 고정 조건에서 amygdala 예측이 색, 공간주파수 편집으로만 움직이고 인간 평정은 변하지 않으면, amygdala encoder는 정서가 아니라 정서와 상관된 저수준 특징을 읽는다는 해석이 지지된다.
* **경쟁 설명.** 신기성(생성 자극의 AI다움)이 amygdala를 올릴 수 있다(10.1038/s41467-024-49073-8, Discussion 6단락; 10.1101/2025.11.03.686276). 모든 조건을 같은 생성 파이프라인에 통과시키는 null-edit 대조로 구분한다. amygdala encoder의 낮은 예측력(Gu 2023의 '정확도 비례' 결과)은 효과 크기 해석을 보수적으로 만든다.
* **overlap:** 해당 프로젝트 없음.
* **선행 수행.** partially. 범주 제약 없는 amygdala 제어의 in vivo 검증은 NeuroVolve가 수행. 범주 고정 조건은 미발견.

### CH3. 같은 자극에서 surrogate 뇌는 정서 구조를 얼마나 잃는가 ('residual affect')
* **Original Finding.** TRIBE v2는 새 자극, 과제, 피험자에 대한 whole-brain 예측과 고전 실험의 in silico 재현을 보고하며, 신경영상 프로토콜 사전 선별 플랫폼을 표방한다. 동시에 체성감각 등 입력 부재와 수동적 관찰자 가정을 한계로 적었다. (arXiv:2605.04326, Discussion 1, 2단락)
* **Unresolved Question.** EmoMind는 TRIBE v2 예측으로 실측을 대체하면 클립 간 정서 관계 구조가 크게 손실된다고 했다(arXiv:2605.16739, 5 Discussion 2단락). 그러나 실측(MindCaptioning 평가 클립)과 대체(Emo-FilM 영화)의 자극이 달라(같은 논문 4.2, A.10) 손실의 원인이 장치인지 자극인지 모른다. Jain et al.은 in silico 결과가 DL feature 공간의 능력에 묶인다고 경고했다(10.1162/nol_a_00101, Discussion "Caveats").
* **Technological Development.** 공개 가중치의 tri-modal whole-brain encoder(TRIBE v2). 우리 데이터셋이 학습에 쓰이지 않았다는 점(Table 1)이 중요하다.
* **New Dataset / Model Combination.** Horikawa 2,181 무음 클립과 Emo-FilM 14편(소리, 대사)에 TRIBE v2 예측을 계산 → 같은 자극의 실측 fMRI와 정서 평정(Horikawa 34+14, Emo-FilM 50항목 1 Hz)으로 비교.
* **New Research Question.** 같은 자극에서 TRIBE v2 예측 반응과 실측 fMRI의 정서 표상 구조(정서 RSA, 정서 차원별 encoding 가중치)는 어느 영역, 어느 정서 차원에서 갈라지는가? 실측에서 예측을 뺀 잔차가 규범 정서 평정을 추가로 설명하는가?
* **결론 수준.** R0. 다만 이 비교가 CH1, CH2, CH4의 R1 결과를 얼마나 믿을지 정하는 관문(gate)이다.
* **가능한 결과와 의미.** (a) 잔차에 정서 정보가 없음: 이 데이터의 정서 관련 신호는 이 모델이 계산하는 지각 반응과 구분되지 않는다. (b) 특정 영역(예: insula, vmPFC) 잔차에 정서 정보가 있음: 지각 기반 surrogate가 놓치는 성분의 후보. 단 개인 특이 반응, 잡음, 내수용 성분이 섞인다. Horikawa와 Emo-FilM에는 반복 제시가 없어 noise ceiling 대신 피험자 간 ISC를 상한 근사로 쓴다(Stage 1 보고서 4.1, 4.2절).
* **경쟁 설명.** 잔차의 정서 정보가 surrogate의 피질하 해상도 부족 때문일 수 있다. 영역별 예측 정확도로 가중해 해석한다. Horikawa는 블록 평균 전처리본(비디오당 1 sample)이 기본이라 TRIBE의 시간 해상도 예측을 같은 방식으로 블록 평균해 맞춘다.
* **overlap: Emo-FilM 연구** (사전학습 멀티모달 뇌 encoding으로 정서 맥락 기여 분석. Emo-FilM 부분이 겹침).
* **선행 수행.** partially (EmoMind의 대체 실험, 자극 불일치).

### CH4. Emo-FilM에서 음악을 빼거나 바꾸면 정서 관련 반응 예측은 어떻게 변하는가
* **Original Finding.** amygdala encoding model은 정적 시각 feature만 써서 청각, 언어, 습관화, 학습에 따른 반응을 예측할 수 없었다(Jang & Kragel 2025, Discussion 7단락). Horikawa et al.은 청각 내용을 포함한 후속 연구를 제안했다(Horikawa 2020, Discussion 7단락). Ma & Kragel은 hippocampal 정서 표상이 시청각, 언어 특징이 다른 영화 사이에서 일반화되었다고 보고했다(10.1038/s41467-025-68240-z, Discussion 1단락).
* **Unresolved Question.** 영화의 음악은 정서 장면에 맞춰 배치되므로 관찰 데이터로는 음악 효과와 장면 효과를 분리할 수 없다. '영화 간 일반화'는 감각 채널 통제가 아니다.
* **Technological Development.** 영화 사운드트랙 3-stem 분리(arXiv:2110.09958), 음악 세부 분리(arXiv:2211.08553), 음향 입력을 받는 whole-brain encoder(TRIBE v2).
* **New Dataset / Model Combination.** Emo-FilM 14편(G1 보유, CC 영화. 영화별 파생물 조건 미확인) → stem 분리 → counterfactual 판본: 음악 제거, 반대 정서 consensus를 가진 다른 영화 음악으로 교체, 대사만, 원 stem 재합성(분리 잡음 대조) → TRIBE v2 예측 → 원본 1 Hz 정서 평정, 참가자 생리 신호(PPG, EDA)와 비교.
* **New Research Question.** Emo-FilM에서 음악 stem을 제거하거나 반대 정서의 음악으로 바꾸면, 1 Hz 정서 평정과 가장 강하게 결합된 영역들의 예측 반응이 얼마나 변하는가? 그 변화는 원본에서 음악이 있는 구간과 없는 구간의 정서 평정 차이(관찰)와 같은 방향인가?
* **결론 수준.** R1. counterfactual 판본을 새 평정자가 평정하면 R2(영화 파생물 시청 조건 확인 후).
* **반증 조건.** 음악 교체가 청각피질 예측만 바꾸고 평정 결합 영역(예: STS, precuneus, insula)은 바꾸지 않으면, 이 surrogate 안에서 음악의 정서 기여는 감각 수준에 머문다. 원 stem 재합성 판본과 원본의 예측 차이가 음악 교체 효과보다 크면 분리 잡음이 결과를 지배하므로 해석을 중단한다.
* **overlap: Emo-FilM 연구.**
* **선행 수행.** partially. 영화 사운드트랙 음향 특징과 공유 정서의 관찰적 연관은 arXiv:2410.17300(존재만 확인, 본문 미열람), 사운드트랙 교체의 행동, 기억 효과는 검색 결과로만 봄(미검증). stem 분리 기반 in silico 신경 연구는 미발견.

### CH5. 같은 영상을 본 사람들 사이에서, 기대 반응에서 벗어난 뇌 반응이 본인 보고의 편차를 예측하는가
* **Original Finding.** Horikawa 2020의 평정은 fMRI 참가자 것이 아니며, 발견된 표상은 1인칭 경험이 아니라 타인의 정서 예측일 수 있다(10.1016/j.isci.2020.101060, Limitations 1, 2단락). 표상 해석에는 그 정보가 하류에서 읽혀 행동(보고)에 쓰인다는 추가 근거가 필요하다(10.1016/j.conb.2019.04.002, "Representational interpretations..." 절).
* **Unresolved Question.** 규범 평정 데이터에서는 참가자 뇌와 평정이 모두 자극의 자식 노드라 뇌 → 보고 경로를 검정할 수 없다(U5). 본인 보고가 있어도 자극 자체가 뇌와 보고를 함께 결정하므로 자극 교란이 남는다.
* **Technological Development.** 자극별 '전형적 뇌 반응'의 in silico 기대값(TRIBE v2 예측, 또는 해당 참가자를 뺀 집단 평균)을 counterfactual 기준선으로 쓰는 방법. fold 내 교란 회귀(Snoek 2019, 10.1016/j.neuroimage.2018.09.074, 초록).
* **New Dataset / Model Combination.** Spacetop alignvideo(참가자 본인 평정, 모든 참가자가 같은 영상, 같은 순서) + TRIBE v2 영상별 예측 + 참가자별 fMRI. 소규모 반복은 Emo-FilM 사후 클립 회고 평정(영화당 5항목, 영화 길이의 약 20%)으로.
* **New Research Question.** 같은 영상에 대해, 자극이 결정하는 기대 반응(TRIBE v2 예측 또는 다른 참가자 평균)에서 벗어난 개인 뇌 반응 편차가 그 참가자의 정서 보고가 집단 평균에서 벗어난 정도를 예측하는가? 어느 영역에서 그런가?
* **결론 수준.** R0. 자극을 설계로 고정해 자극 교란은 제거하지만, 각성 상태와 주의 같은 무측정 교란이 남는다. 영상 직후 평정 구간이 영상 끝 HRF와 겹치는 문제(Stage 1 보고서 4.3절)는 평정 구간 이전 TR만 쓰는 방식으로 통제한다. alignvideo 평정 약 51% 결측은 결측 기제(클릭해야 저장되는 코드 구조)를 확인한 뒤 다룬다.
* **경쟁 설명.** 개인 편차의 상관이 정서가 아니라 영상 몰입도(engaged 문항)나 머리 움직임에서 올 수 있다. engaged를 공변량으로, framewise displacement를 교란으로 넣는다.
* **overlap:** 해당 프로젝트 없음.
* **선행 수행.** no (2026-11 검색 범위 내 'in silico 기대 반응 잔차 × 본인 보고 편차' 설계 미발견. 개인 고유 반응 연구 일반은 Stage 1 보고서 5.3 #4가 기회로 기록).

### CH6. 정서 모델 셋을 controversial 자극으로 판정한다
* **Original Finding.** EmoNet은 정서 관련 시각 속성을 분리하는 수단을 제공하며 그 정보는 단순 시각 특징의 선형 조합으로 환원되지 않는다(10.1126/sciadv.aaw4358, Discussion 2단락). VV는 valence 분산의 5~20%만 설명하는 별도 모드다(10.1038/s41467-024-53668-6, Discussion 5단락). OTC는 의미 × 정서를 공동 표상한다(10.1038/s41467-024-49073-8).
* **Unresolved Question.** 세 설명 모두 자연 이미지에서 유의할 수 있어 어느 쪽이 더 나은 뇌 모델인지 판정되지 않았다. 단일 모델 유의성은 증거가 아니다(10.1016/j.conb.2019.04.002, single-model-significance fallacy).
* **Technological Development.** controversial stimuli(10.1073/pnas.1912334117, Discussion "Current Limitations and Future Directions": 최적 실험 설계로의 확장 제안), 결정 경계 표집(arXiv:2507.14549), model metamer(10.1038/s41593-023-01442-0).
* **New Dataset / Model Combination.** EmoNet, VV 모델, CLIP 기반 valence probe 쌍마다 불일치가 최대인 이미지 합성 → NSD 학습 시각피질, amygdala encoder 예측(Horikawa encoder는 EmoNet 관련 누수 회피를 위해 평가에서 제외하거나 별도 표기) → NSD nsdmeadows 100장을 실측 기준점으로 → 인간 valence 평정.
* **New Research Question.** EmoNet, VV, 의미 기반 valence 모델이 서로 반대 valence를 예측하도록 합성한 이미지에서, NSD 학습 encoder의 시각피질과 amygdala 예측 반응, 그리고 인간 valence 평정은 각각 어느 모델을 따르는가? 뇌 encoder와 인간이 서로 다른 모델을 따른다면 그 해리는 무엇을 뜻하는가?
* **결론 수준.** R1 + R2.
* **가능한 결과와 의미.** 시각피질 예측은 VV, 인간 평정은 의미 모델을 따르면 Sadeghi의 '두 경로' 가설을 모델 판정 수준에서 지지한다. 모두 의미 모델을 따르면 VV, 스키마 신호는 자연 이미지에서 의미와의 상관으로 얻은 것일 수 있다. 어느 모델도 따르지 않으면 controversial 자극이 모두의 분포 밖이라는 뜻이며(Golan의 noise ceiling 미도달과 같은 상황), 자극 사실감 평정으로 확인한다.
* **overlap:** 해당 프로젝트 없음.
* **선행 수행.** no (정서 모델 대상 controversial 자극 + 뇌 encoder 판정 미발견).

### CH7. 정서 편집의 dose-response: in silico 효과가 인간에게 유효한 범위
* **Original Finding.** 자동 평가기 valence 이동은 크지만 인간 효과는 작고, 극단 섭동에서 충실도가 무너졌다. 저자들은 행동적으로 유효한 국소 선형 영역이 α=0 근처일 수 있다고 추정했다(arXiv:2609.27729, Discussion 5.1 "Local validity").
* **Unresolved Question.** 그 영역의 폭이 편집 유형(의미 경로 vs 저수준 경로)과 정서 차원에 따라 어떻게 다른지 모른다. AI 생성 자극은 원본보다 효과가 작다(10.1101/2025.11.03.686276).
* **Technological Development.** 연속 편집(Concept Sliders), 참조 고정 편집(BrainACTIV).
* **New Dataset / Model Combination.** NSD shared 이미지와 Horikawa 대표 프레임 소수 × 편집 강도 7단계(0 근처 조밀 표집, Rothermel 제안) × 편집 가족 3종 → encoder 예측 곡선 + 인간 평정 곡선.
* **New Research Question.** 정서 편집 강도에 따른 encoder 예측 곡선과 인간 평정 곡선은 같은 선형 구간을 갖는가? 두 곡선이 갈라지는 강도는 편집 가족마다 다른가?
* **결론 수준.** R1 + R2. 다른 사슬(CH1, CH2, CH6)의 편집 강도를 정하는 예비 실험(pilot) 성격.
* **선행 수행.** no (Rothermel이 제안만 함).

---

## 7. 담당 Axis 확장 제안

### Axis L (Generative & Counterfactual Methods)
* **추가:** S1 Semantics-clamped affective counterfactuals, S2 Relational/joint neural control, S3 Surrogate-brain fidelity audit, S4 Temporal/auditory/narrative counterfactuals, S7 Generator-prior and AI-ness confound audit, 그리고 "Stimulus selection as weak intervention"(생성 대신 대규모 기존 자극 풀에서 모델로 선택; Tuckute 2024, RNC).
* **재분류 1:** 기존 "Brain-conditioned Generation"은 과학적 용도가 주로 decoding이므로 1차 소속을 G(Decoding, vision-decoding 담당)로 옮기고 L은 2차로 둔다. 단 Rothermel처럼 decoding 경로를 '조작'에 쓰는 경우는 L에 남긴다.
* **재분류 2:** "Generative Experimental Design"을 (a) 오프라인 in silico 선택/합성, (b) 온라인 closed-loop(Lorenz 2018)로 나눈다. 우리 데이터로 가능한 것은 (a)뿐이다.
* **삭제:** 없음.

### Axis P (Causality & Scientific Inference)
* **추가:** S5 Evidence-level ladder(R0~R4) 표기 의무화, S6 Rater-structure causal graphs, "Dataset-internal real interventions inventory"(Spacetop cue 조작 등 데이터셋 안의 실제 조작 목록), "Distributional robustness across datasets/edit families as causal screening"(Weichwald & Peters).
* **경계 정리:** L의 "Counterfactual Representation Testing"과 P의 "Counterfactual Predictions"가 겹친다. **L은 '어떻게 counterfactual 자극이나 개입을 만드는가', P는 '그것으로 무엇을 결론할 수 있는가'** 로 나누자.
* **재분류:** "Confound Control" 중 feature collinearity 부분은 T의 Variance Partitioning과 연결 표시. 정서와 의미가 인과적으로 얽힌 경우(의미 → 정서) 교란 회귀가 신호를 지우는 과통제 위험이 있으므로(10.1016/j.neuroimage.2018.09.074 맥락의 본 에이전트 판단), "Over-control and collider risk"를 P에 명시적 Sub-axis로 둔다.

---

## 8. 새 fMRI 수집 없이 가능한 설계와 그 한계

| 설계 | 데이터 | 도달 수준 | 결론 가능한 것 | 결론 불가능한 것 | 추가 비용 |
|---|---|---|---|---|---|
| 의미 고정 정서 편집의 in silico 반응 (CH1) | Horikawa 클립 + Horikawa 학습 encoder + TRIBE v2 | R1 | encoder가 의미 없이 정서 단서에 민감한지 | 실제 뇌의 민감성 | 편집 계산, 소규모 평정 |
| 범주 고정 amygdala 제어 (CH2) | NSD encoder, Horikawa/Emo-FilM amygdala encoder | R1 (+R2) | 의미 범주 외 경로로 amygdala 모델을 움직일 수 있는지 | amygdala 실측 조절, 정서 경험 | 생성 계산, 평정 |
| Surrogate 충실도와 residual affect (CH3) | Horikawa, Emo-FilM 실측 + TRIBE v2 | R0 | surrogate가 놓치는 정서 구조의 위치 | 그 잔차의 원인(내수용인지 잡음인지) | 계산만 |
| 음악 stem counterfactual (CH4) | Emo-FilM + TRIBE v2 | R1 (+R2) | surrogate 안에서 음악의 정서 관련 기여 | 실제 뇌의 음악 기여 | 분리 계산, 평정(파생물 조건 확인 후) |
| 기대 반응 잔차와 본인 보고 (CH5) | Spacetop | R0 | 자극 교란을 뺀 뇌-보고 연관 | 뇌 → 보고 인과 | 계산만 |
| Controversial 정서 모델 판정 (CH6) | NSD encoder | R1 + R2 | 뇌 encoder와 인간이 어느 정서 모델을 따르는지 | 실측 뇌가 따르는 모델 | 합성 계산, 평정 |
| 모델 선택 drive/suppress 교차 예측 (X6) | Horikawa 학습 → Emo-FilM, Spacetop 장면 | R0 | 선택 자극의 교차 데이터셋 실측 반응(이미 수집된 자극에 한함) | 새 자극에 대한 조절 | 계산만 |

**공통 한계.** (1) R1 결과는 encoder의 학습 분포에 묶인다. 편집 자극은 정의상 분포 밖이며 encoder 예측 신뢰도가 떨어진다(10.1038/s41562-025-02252-z, Discussion 6단락). 서로 다른 encoder 여러 개의 예측 불일치를 불확실성으로 보고한다. (2) R2 평정은 '자극이 정서 보고를 바꾼다'만 보여준다. (3) 어떤 설계도 R4(뇌 → 정서)에 닿지 않는다. (4) 정서 영역 encoder의 예측력이 낮을수록 R1 결과가 R3로 옮겨질 가능성이 낮다(10.1038/s42003-023-05440-7).

---

## 9. 생성, counterfactual 연구 전용 방법론 점검표

| 항목 | 위험 | 대응 |
|---|---|---|
| 라벨 누수 | EmoNet은 Horikawa와 같은 Cowen & Keltner 비디오 프레임과 규범 라벨로 학습(10.1126/sciadv.aaw4358 Methods) | Horikawa 분석에서 EmoNet feature, EmoNet 유도 편집, EmoNet 기반 평가 금지 |
| 사전학습 오염 | COCO(NSD)는 대다수 VLM, diffusion 학습 분포 안(Stage 1 보고서 4.4절). 인터넷 영상 사전학습 모델이 Horikawa 출처 클립을 보았을 가능성 미확인 | 오염 가능 모델과 그렇지 않은 모델의 결과를 나란히 보고 |
| AI다움, 신기성 | 생성 자극의 효과 감쇠, 중립 자극 LPP 증가(10.1101/2025.11.03.686276), 생성 이미지의 중위 시각영역 반응 증가(arXiv:2512.00557) | 모든 조건(무편집 포함)을 같은 파이프라인에 통과시키는 null-edit 대조. 사실감 평정 수집 |
| 의미 누출 | 정서 편집이 의미를 바꿈(arXiv:2405.12661), 분류기 유도 편집의 교란 전달(arXiv:2202.10166) | 편집마다 캡션 embedding 거리, 객체 검출 차이, 잔여 간섭 보고 |
| feature 공간 맹시 | encoder feature가 편집에 불변이면 예측도 불변 | 편집별 feature 변위를 먼저 보고. 변위가 없으면 '정보 없음'으로 분류 |
| 국소 선형 영역 | 큰 편집 강도에서 자동 점수와 인간 지각 해리(arXiv:2609.27729) | 0 근처 조밀 표집, CH7 pilot |
| 영상 편집의 시간 일관성 | 프레임 간 깜빡임 등 인공물 | Horikawa는 비디오당 블록 평균이므로 클립 전체에 걸쳐 일관된 편집만 사용. 인공물 대조(재구성만 한 원본) |
| 생성 파이프라인 단계 효과 | diffusion 단계가 효과를 약화하거나 바꿈(arXiv:2609.27729) | 단계별(latent, 생성기) 효과 별도 평가 |
| HRF, 자기상관 | in silico 예측과 실측 비교 시 시간 정렬 | TRIBE 예측을 실측과 같은 HRF, 블록 평균 처리로 맞춤 |
| 순서 이월 | Horikawa 5명 동일 자극 순서 | 이전 클립 정서를 nuisance로. 순서 효과는 피험자 간 일관성으로 구분 불가함을 명시 |
| 원형 ROI 선택 | '정서 우세 voxel'을 같은 데이터로 고르고 같은 데이터로 평가 | voxel 선택용 분할과 encoder 학습, 평가 분할 분리 |
| 다중 비교 | voxel × 편집 × 모델 | 사전 지정 ROI와 FDR, 편집 가족 단위 검정 |
| 저작권, 파생물 | Horikawa 비디오 요청 조건 미확인, Emo-FilM 영화별 CC 조항 미확인(ND 조항이면 파생물 공유 불가), NSD 이미지는 Flickr 약관, Spacetop 제3자 영상 조건 미확인 | 편집 자극은 내부 분석용으로만, 공개는 코드와 편집 파라미터로. 평정 수집 전 조건 확인 |
| 모델 라이선스 | TRIBE v2 CC BY-NC 4.0(검색 수준), FLUX.1 [dev] 비상업(미확인), LLaMA 게이트 | 연구 목적 범위 확인, 2절 표의 미확인 항목 재확인 |
| 신규 행동 평정 | R2는 신규 인간 데이터 수집 | IRB, 평정 지시문을 Cowen & Keltner 또는 Emo-FilM 문항과 맞춰 비교 가능성 확보 |

---

## 10. 검증 상태와 미확인 사항

**검증된 것.**
* 45편 모두 식별자 경로로 존재 확인(Crossref API, arXiv API, PubMed 메타데이터).
* Discussion, Limitations, Conclusion 원문 확인 28편(PMC 전문, arXiv HTML/PDF, bioRxiv 전문). 각 사슬의 단락 위치는 내가 읽은 판본 기준이며, Tuckute 2024는 PMC 공개 preprint판(PMC10120732)으로 읽었다.
* EmoNet 학습 자료가 Cowen & Keltner 2,185 비디오 프레임이라는 사실(Kragel 2019 Methods 원문).
* TRIBE v2 학습/평가 데이터셋 목록에 Horikawa, Emo-FilM, Spacetop, NSD가 없다는 사실(arXiv:2605.04326 Table 1, 5.7절).
* NeuroVolve amygdala 실측 결과의 수치(ANOVA, Tukey 비교, High/Low 이미지 내용).

**미확인.**
* 모델 라이선스 다수(2절 표에 표시). TRIBE v2 라이선스는 검색 결과 수준.
* Concept Sliders의 ECCV 2024, HT Demucs의 ICASSP 2023 게재는 기억 기반으로 학회 페이지 미확인(jsonl venue에 표시).
* Chen et al. 2017(10.1093/biostatistics/kxx027)은 서지만 확인, 본문, 초록 미열람.
* arXiv:2410.17300(영화 사운드트랙 특징과 정서, 검색 요약만 봄), arXiv:2507.10861(diffusion 기반 reappraisal, 서지만 확인)은 jsonl에 넣었지만 본문 미열람. 사운드트랙 교체 행동 연구는 검색 결과로만 봄.
* 2절 표의 영상 편집 도구(LivePortrait, Wan)가 Horikawa 클립(짧고, 다양한 화질, 다수 인물)에 실제로 품질을 유지하는지는 시험하지 않았다.
* 각 사슬의 '선행 수행' 판단은 2026-11-12 기준 WebSearch와 arXiv 확인 범위 안의 판단이다.

**에이전트 간 의견 충돌 기록.** 이번 라운드는 독립 탐색이라 다른 에이전트 결과를 보지 않았다. Stage 1 보고서와 다른 판단 하나를 기록한다: Stage 1 보고서 5.1 #4, 5.5 #1은 "규범 평정 vs 본인 보고가 뇌를 얼마나 다르게 설명하는가"를 기회로 들었는데, 나는 여기에 "규범 평정 데이터에서는 뇌-평정 매개 구조 자체가 성립하지 않는다"(U5)는 인과 구조상의 제약을 추가한다. 이는 보고서의 판단을 뒤집는 것이 아니라 해석 범위를 좁히는 것이다.
