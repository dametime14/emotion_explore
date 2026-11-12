# Stage 2, 3절 인용 표본 검증 결과

작성: adversarial-reviewer (새 인스턴스). 작성일 2026-11-12.
이 파일은 검증 결과 기록이다. `literature_db.csv`와 각 에이전트의 jsonl은 읽기만 했고 수정하지 않았다. 수정은 Coordinator가 한다.

## 0. 요약

* 표본 25편(원 기록 34줄, 10개 에이전트). 식별자 오류 0, verified_by 표기 오류 0, 확인 불가 0.
* 요약, 한계, future direction의 절 위치를 원문과 대조한 결과 내용 오류는 1건(emotion-theory, Zhou 2021의 limitations 필드)뿐이다.
* CLAUDE.md 5절 위반(본문을 안 읽고 Discussion에서 future direction을 가져온 것처럼 쓴 경우)은 표본에서 0건이다. abstract_only와 no 기록은 모두 future_directions를 비우거나 "본문 미열람"으로 표시했다.
* 가장 큰 문제는 already_done이다. "no"로 적힌 future direction 14개(기록 20줄)를 다시 검색했더니 4개(기록 5줄)는 이미 수행된 연구가 있었다. 기록 기준 오판율은 25%(5/20)다. 이 문제는 frontier-ai, llm-semantics, geometry-info, multimodal-dynamics, emotion-theory 다섯 에이전트에 흩어져 있어, 한 에이전트에 몰린 문제가 아니라 팀 전체의 체계적 문제다.
* brain-inspired는 표본 5줄의 내용이 모두 정확했다. 다만 5줄 모두 already_done 검색을 하지 않았다(빈 placeholder future direction 4줄, "unknown (미검색)" 1줄). DB 전체에서도 이 에이전트의 future direction 81개 중 45개가 unknown이다.

## 1. 표본 추출

* 스크립트: `outputs/literature/draw_verification_sample.py` (Coordinator 작성)
* 시드 20261112. 후보는 `literature_db.csv`에서 verified=True이고 added_by에 adversarial-reviewer가 없는 327편. 무작위 25편.
* 재현 확인: `python3 -I outputs/literature/draw_verification_sample.py` 출력이 `verification_sample_draw.txt`와 완전히 같았다(diff 차이 없음).
* 이 인스턴스는 표본 25편 중 어느 것도 추가하지 않았다.
* 여러 에이전트가 같은 논문을 기록한 경우(5, 11, 17, 23, 25번)에는 `sources` 열이 가리키는 원 jsonl 줄을 모두 따로 검증했다. 그래서 검증 단위는 논문 25편, 원 기록 34줄이다.

## 2. 표본 목록

| # | uid | 추가 에이전트 (원 기록 수) | discussion_read (DB) | 논문 |
|---|---|---|---|---|
| 1 | arxiv:2606.06345 | encoding-foundation (1) | full_text | Benchetrit et al. 2026, Boosting Brain-to-Image Decoding with TRIBE v2 Data Augmentation |
| 2 | doi:10.1098/rstb.2016.0007 | brain-inspired (1) | no | Seth & Friston 2016, Active interoceptive inference and the emotional brain |
| 3 | arxiv:2605.23035 | frontier-ai (1) | abstract_only | Guo et al. 2026, Sparse Autoencoders Map Brain-LLM Alignment onto Cortical Semantic Topography |
| 4 | doi:10.1038/s41567-022-01852-0 | geometry-info (1) | abstract_only | Santoro et al. 2023, Higher-order organization of multivariate time series |
| 5 | doi:10.1016/j.cub.2015.06.009 | llm-semantics, emotion-theory (2) | full_text | Skerry & Saxe 2015, Neural Representations of Emotion Are Organized around Abstract Event Features |
| 6 | doi:10.64898/2025.11.30.691450 | systems-neuro (1) | abstract_only | Liu et al. 2025, Energy Landscape Analysis Reveals Thalamic Modulation of Brain State Transitions During Movie Watching |
| 7 | arxiv:2502.04379 | llm-semantics (1) | full_text | Melhart et al. 2025, Can Large Language Models Capture Video Game Engagement? |
| 8 | doi:10.1016/j.cell.2020.10.024 | brain-inspired (1) | no | Whittington et al. 2020, The Tolman-Eichenbaum Machine |
| 9 | doi:10.1038/s42003-023-04546-2 | dataset-auditor (1) | abstract_only | Jain et al. 2023, Selectivity for food in human ventral visual cortex |
| 10 | doi:10.1038/s41467-021-26977-3 | emotion-theory (1) | full_text | Zhou et al. 2021, A distributed fMRI-based signature for the subjective experience of fear |
| 11 | arxiv:2602.07570 | frontier-ai, multimodal-dynamics (2) | full_text | Jindal et al. 2026, How does longer temporal context enhance multimodal narrative video processing in the brain? |
| 12 | doi:10.1073/pnas.2500815122 | brain-inspired (1) | abstract_only | Lin et al. 2025, Habenula-ventral tegmental area functional coupling and risk aversion in humans |
| 13 | doi:10.1140/epjds/s13688-016-0093-1 | multimodal-dynamics (1) | abstract_only | Reagan et al. 2016, The emotional arcs of stories are dominated by six basic shapes |
| 14 | arxiv:2605.29850 | encoding-foundation (1) | full_text | Gokce et al. 2026, MIRAGE: Adaptive Multimodal Gating for Whole-Brain fMRI Encoding |
| 15 | arxiv:2610.22706 | encoding-foundation (1) | abstract_only | Huang et al. 2026, Brain-Aligned Multimodal LLMs for Social and Emotional Understanding of Cartoon Movies |
| 16 | doi:10.1093/scan/nsaf099 | systems-neuro (1) | abstract_only | Kirk et al. 2026, Linking subjective experience of anxiety to brain function using natural language processing |
| 17 | doi:10.1038/s41598-025-14961-6 | dataset-auditor, geometry-info, llm-semantics (3) | full_text | Asanuma et al. 2025, Correspondence of high dimensional emotion structures elicited from video clips between humans and multimodal LLMs |
| 18 | doi:10.1038/s42003-023-05440-7 | generative-counterfactual (1) | full_text | Gu et al. 2023, Human brain responses are modulated when exposed to optimized natural images or synthetically generated images |
| 19 | arxiv:2206.09398 | geometry-info (1) | full_text | Thual et al. 2022, Aligning individual brains with Fused Unbalanced Gromov-Wasserstein |
| 20 | doi:10.1109/embc58623.2025.11254034 | dataset-auditor (1) | abstract_only | David et al. 2025, Deep Neural Encoder-Decoder Model to Relate fMRI Brain Activity with Naturalistic Stimuli |
| 21 | doi:10.1016/j.neuron.2024.04.018 | brain-inspired (1) | full_text | Margalit et al. 2024, A unifying framework for functional organization in early and higher ventral visual cortex |
| 22 | arxiv:2407.09450 | multimodal-dynamics (1) | full_text | Fountas et al. 2025, Human-inspired Episodic Memory for Infinite Context LLMs (EM-LLM) |
| 23 | doi:10.1126/sciadv.abf7129 | emotion-theory, encoding-foundation, geometry-info, multimodal-dynamics, systems-neuro (5) | full_text | Chang et al. 2021, Endogenous variation in vmPFC state dynamics during naturalistic viewing reflects affective experience |
| 24 | arxiv:2502.11831 | frontier-ai (1) | full_text | Garrido et al. 2025, Intuitive physics understanding emerges from self-supervised pretraining on natural videos |
| 25 | doi:10.1038/nn.4650 | geometry-info, brain-inspired (2) | abstract_only | Stachenfeld et al. 2017, The hippocampus as a predictive map |

## 3. 검증 방법

1. **식별자:** DOI 16개는 api.crossref.org/works/{DOI}로 제목, 저자, 연도, 학술지를 받아 기록과 비교했다. arXiv ID 9개는 export.arxiv.org API로 제목, 저자, 최초 게시일, journal_ref, comment를 받아 비교했다. 기록에 함께 적힌 보조 ID(arXiv:2203.10702, arXiv:2507.12009, arXiv:2505.12746)도 확인했다.
2. **verified_by:** 기록된 경로로 실제 조회되는지 확인했다. crossref는 Crossref 레코드 존재, pubmed는 PubMed MCP(`convert_article_ids`, `search_articles`, `get_article_metadata`)로 PMID 존재, arxiv는 arXiv API 레코드 존재를 기준으로 삼았다.
3. **내용:**
   * full_text 기록: 원문을 직접 읽고 main_findings, limitations, future_directions의 text와 section을 대조했다. arXiv 7편은 arxiv.org/pdf를 pdftotext로 변환해 해당 절을 읽었다. PMC 공개 6편(Skerry 2015, Zhou 2021, Asanuma 2025, Gu 2023, Margalit 2024, Chang 2021)은 PubMed MCP `get_full_text_article`로 전문을 받아 Discussion을 단락 단위로 번호를 매겨 읽었다.
   * abstract_only와 no 기록: 초록(Crossref, arXiv, PubMed)과 대조하고, future direction을 Discussion에서 가져온 것처럼 적었는지 확인했다(CLAUDE.md 5절).
4. **already_done:** "no"로 적힌 future direction을 논문마다 1~2개 골라 다시 검색했다. 검색 경로는 export.arxiv.org 검색 API(제목, 초록 필드), WebSearch(일반 웹), PubMed 검색이다. Semantic Scholar API는 429(요청 한도 초과)로 쓰지 못했다. 기간은 원 논문 게시 이후부터 기준일 2026-11-12까지다. 짧은 검색이므로 "유지" 판정은 "이번 검색 범위에서 반증을 찾지 못함"이라는 뜻이다.

**판정 범주**
* 정확: 식별자, 표기, 내용이 원문과 맞음.
* 표기 오류: verified_by로 적은 경로에서 확인되지 않음(검색 색인 수준을 verified로 적은 경우 포함).
* 내용 오류: 기록 내용이 원문이나 사실과 다름. 두 하위 유형으로 나눈다.
  * A: main_findings, limitations, future_directions의 text나 section이 원문과 다름.
  * B: already_done "no"인데 이후 수행 연구가 실제로 있음.
* 식별자 오류: ID가 다른 논문을 가리키거나 존재하지 않음.
* 확인 불가: 원문이나 메타데이터에 접근하지 못함.
* 경미(오류로 세지 않음): 절은 맞고 단락 번호만 하나 어긋난 경우, already_done 근거 서술의 작은 부정확, 형식 편차.

## 4. 접근 경로와 한계

* **접근 성공:** api.crossref.org(21건), export.arxiv.org(메타데이터와 검색), arxiv.org/pdf(9건, 후속 연구 확인용 2건 포함), PubMed MCP(메타데이터 8건, PMC 전문 6건), WebSearch.
* **열지 못한 출처:**
  * www.nature.com: 프록시가 CONNECT 403으로 거부. Nature Communications, Scientific Reports, Communications Biology 세 편은 PMC 판본(PubMed MCP)으로 대신 읽었다.
  * pmc.ncbi.nlm.nih.gov 웹: reCAPTCHA 페이지가 반환됨. PubMed MCP로 대신 읽었다.
  * api.semanticscholar.org: 429 Too Many Requests. already_done 검색은 arXiv API, WebSearch, PubMed로 대신했다.
  * 차단된 호스트는 우회하지 않았다.
* **영향:** 표본 25편 모두 필요한 수준(full_text 기록은 전문, 나머지는 초록)까지 확인할 수 있었으므로 "확인 불가" 판정은 없다. already_done 검색은 짧은 검색이라 "유지" 판정의 재현율은 높지 않다. 특히 논문 밖 학회 초록, 비영어권 문헌은 거의 보지 못했다.
* 내려받은 파일은 `/tmp/claude-0/-home-user-emotion-explore/4a0aeef6-c090-5f71-8a99-9b8e7c0f6d89/scratchpad/verification-sample/` 아래에 두었고 실행하지 않았다.

## 5. 기록별 판정표

(1) 식별자, (2) verified_by 표기, (3) 내용, (4) already_done 점검. FD는 future direction이다.

| # | uid | 에이전트 | (1) | (2) | (3) | (4) | 판정, 오류 내용 | 근거 |
|---|---|---|---|---|---|---|---|---|
| 1 | arxiv:2606.06345 | encoding-foundation | 정확 | 정확 (arxiv) | 정확 | FD1, FD2 "no" 유지 | 정확 | arXiv API 제목, 저자 6명, 2026-06-04 일치. PDF 5 Discussion "Subject-agnostic augmentation has limits" 단락(피험자별 TRIBE 적응, 합성 데이터 가중, 다중 피험자 사전학습), "Limitations" 단락(두 데이터셋 소수 피험자, 다른 모달리티 확장) 확인. Top-10 최대 68% 향상은 초록과 4절 일치. 검색: arXiv "TRIBE AND synthetic AND fMRI", "synthetic fMRI AND augmentation AND decoding" 결과는 원 논문뿐 |
| 2 | doi:10.1098/rstb.2016.0007 | brain-inspired | 정확 | 정확 (crossref) | 정확 | 해당 없음 | 정확 (형식 편차) | Crossref 제목, 저자 일치. 한 줄 요약은 초록과 부합. FD에 "(본문 미열람)" placeholder와 already_done "unknown"을 넣어 DB n_future_directions가 1로 집계됨 |
| 3 | arxiv:2605.23035 | frontier-ai | 정확 | 정확 | 정확 | 해당 없음 | 정확 | arXiv 초록: 의미 feature가 최고 encoding 성능의 94% 회복, 사전 정의 하위범주와 피질 대응(rho 0.72). venue "CoNLL 2026"은 arXiv comment "Accepted at CoNLL 2026"과 일치 |
| 4 | doi:10.1038/s41567-022-01852-0 | geometry-info | 정확 | 정확 | 정확 | 해당 없음 | 정확 | Crossref Nature Physics 2023, 저자 4명 일치. 기록이 밝힌 arXiv:2203.10702 판(제목 "Unveiling the higher-order...", 같은 저자) 초록과 요약 일치 |
| 5a | doi:10.1016/j.cub.2015.06.009 | llm-semantics | 정확 | 정확 | 정확 | FD3 "no" 유지(신뢰도 낮음) | 정확 | PMC4824044 전문. FD1은 "Characterizing Representational Spaces" 셋째 단락("identify new sets of optimized features ... infer these features directly from text"), FD2는 넷째 단락(structured, generative knowledge representations), FD3은 Discussion 다섯째 단락("A challenge for future work ...")과 정확히 일치. limitations도 셋째, 넷째 단락 서술과 일치. already_done 근거 arXiv:2408.13718(Tak & Gratch 2024, Skerry 자극에 GPT-4 적용), doi:10.1098/rsta.2022.0047(Houlihan et al. 2023) 실재와 서술 부합. FD3 검색: WebSearch 1회(정서 특이 vs 범용 의미 표상, LLM embedding 재분석)에서 직접 해결한 연구 미발견 |
| 5b | 같음 | emotion-theory | 정확 | 정확 | 정확 | 해당 없음 | 정확 | abstract_only. 요약과 "타인 정서 귀속이며 본인 경험 아님" 지적이 초록과 부합 |
| 6 | doi:10.64898/2025.11.30.691450 | systems-neuro | 정확 | 정확 | 정확 | 해당 없음 | 정확 | Crossref posted-content, institution bioRxiv(openRxiv), 2025-12-02, 저자 일치. 초록(Sherlock, 두 우세 상태, easy/hard route, ISC 예측, thalamus 조절)과 요약 일치. eLife reviewed preprint 판본은 Crossref relation(10.7554/eLife.110061.1)으로 확인 가능하므로 "search_index 수준" 표기는 지나치게 보수적일 뿐 오류 아님 |
| 7 | arxiv:2502.04379 | llm-semantics | 정확 | 정확 | 정확 | FD1 "no" 오판, FD2 "no" 유지 | **내용 오류(B)** | 본문 VI.A Limitations 1) Static Images(3초 간격 단일 프레임, "more frames per query or using video input directly"), 2) No Fine-Tuning(low-rank adaptation 제안)과 FD 위치, 내용 일치. 그러나 arXiv:2603.18480(Wang et al., 2026-03, "Do Vision Language Models Understand Human Engagement in Games?")이 같은 GameVibe 코퍼스에서 1초 창마다 16프레임을 VLM에 입력해 검증했고 여전히 약한 성능을 보고함. FD1은 "partially"가 맞음. 같은 논문은 "No model fine-tuning is performed"라고 명시하므로 FD2 "no"는 유지. 검색: arXiv "engagement AND GameVibe" |
| 8 | doi:10.1016/j.cell.2020.10.024 | brain-inspired | 정확 | 정확 | 정확 | 해당 없음 | 정확 (형식 편차) | Crossref 일치. 한 줄 요약 부합. placeholder FD |
| 9 | doi:10.1038/s42003-023-04546-2 | dataset-auditor | 정확 | 정확 (pubmed) | 정확 | 해당 없음 | 정확 | PMID 36792693, PMC9932019 확인. 초록(두 음식 선택 영역, 흑백 localizer)과 일치 |
| 10 | doi:10.1038/s41467-021-26977-3 | emotion-theory | 정확 | 정확 | **오류** | FD "no (검색하지 않음)" 오판 | **내용 오류(A+B)** | PMC8599690 전문. FD(Discussion 2째 단락, process-specific interventions)는 정확. 그러나 limitations 필드에 "Discussion 3~4째 단락: 구조 중심과 HOT 네트워크 중심 모델 모두에 도전"을 적었는데, 이 단락들은 저자의 이론적 함의이지 한계가 아님. 저자가 밝힌 실제 한계는 Discussion 8~9째 단락(IAPS 정지 이미지만 사용, SVR 단일 기법, 사전등록 없음, 조건화 위협 decoder와 패러다임 불일치)에 있으며 기록에 빠짐. 8째 단락의 "비디오 자극이 VIFS를 활성화하는지 검증" 제안도 누락(이 프로젝트의 자연주의 영화 데이터와 직결). already_done: 검색하지 않고 "no"를 적었는데, Zhang R et al. 2022(doi:10.1016/j.bpsc.2022.09.008, PMID 36174930)가 losartan 약리 fMRI에서 "process-specific neuroaffective signatures"로 개입이 주관 공포 신경 표현을 줄이는지 평가함. "yes"가 맞음. 검색: PubMed "fear signature OR VIFS", 2022 이후 |
| 11a | arxiv:2602.07570 | frontier-ai | 정확 | 정확 | 정확 | FD1 "no" 유지 | 정확 | arXiv 저자 6명 일치. Appendix K Limitations(최대 24초, 분 단위는 계산 비용으로 미실시, 메모리 효율 장문맥 MLLM과 hierarchical chunking, CNeuroMod 4명, 영어 할리우드 영화, MEG/ECoG 확장) 원문 일치. 검색: arXiv "long-context AND brain alignment AND video", WebSearch 1회. 분 단위 MLLM 뇌 정렬 후속 미발견(Algonauts 2025 출품작의 20초 고정 창이 가장 가까움) |
| 11b | 같음 | multimodal-dynamics | 정확 | 정확 | 정확 | FD1 "no" 유지 | 정확 (경미) | 내용 일치. FD2를 "Appendix K 둘째 단락"이라 적었으나 원문은 한 단락(그림 삽입으로 끊겨 보임) |
| 12 | doi:10.1073/pnas.2500815122 | brain-inspired | 정확 | 정확 (pubmed) | 정확 | 해당 없음 | 정확 (형식 편차) | PMID 41166429 확인, 초록과 요약 일치. placeholder FD "(본문 미확인)". 참고로 PMC12595472로 전문 공개 상태였음 |
| 13 | doi:10.1140/epjds/s13688-016-0093-1 | multimodal-dynamics | 정확 | 정확 | 정확 | 해당 없음 | 정확 | Crossref 일치. arXiv:1606.07772 초록(1,327편, 여섯 core arc, 다운로드 기준 성공)과 일치 |
| 14 | arxiv:2605.29850 | encoding-foundation | 정확 | 정확 | 정확 | FD2 "no" 유지 | 정확 (경미) | 3.1절과 4 Discussion의 OOD 손실 약 40% vs 30%(저자 서술 그대로), Yeo 망별 이득(Visual 약 0.13, Dorsal Attention 약 0.12, Limbic 약 0.04), 4 Limitations, Future Work 첫째 문장 일치. 검색: arXiv "MIRAGE AND fMRI", "layer attribution AND brain encoding" 결과 없음. 경미: FD1 "partially"의 근거 arXiv:2605.04326(TRIBE v2)은 실재하나 원문은 subject-conditional linear layer와 unseen-subject layer로 기술하며 "저랭크"라는 표현은 확인되지 않음 |
| 15 | arxiv:2610.22706 | encoding-foundation | 정확 | 정확 | 정확 | 해당 없음 | 정확 | arXiv: Yiran Huang 외 4인, 2026-10-15. 초록(valence가 ToM보다 일치, The Present에서 MLLM 평정이 더 많은 영역 예측, 인간-모델 공간 중첩 제한)과 일치 |
| 16 | doi:10.1093/scan/nsaf099 | systems-neuro | 정확 | 정확 | 정확 | 해당 없음 | 정확 | Crossref 초록(preregistered 분석, secondary 분석, preliminary evidence)과 일치 |
| 17a | doi:10.1038/s41598-025-14961-6 | dataset-auditor | 정확 | 정확 (pubmed) | 정확 | FD1 "no" 유지 | 정확 | PMID 40890212 확인. PMC12402258 전문: Discussion 둘째 단락(로드맵)의 세 방향, Methods의 참가자 수준 평정 미공개, 비율 평정, 비디오당 단일 응답 서술 일치. 검색: WebSearch 1회(MLLM + 심박, 내수용 신호 + 영상 정서). rPPG와 얼굴 융합 등 인접 연구만 있고 내수용 신호를 통합한 MLLM 정서 구조 정렬 연구는 미발견 |
| 17b | 같음 | geometry-info | 정확 | 정확 (crossref) | 정확 | 미점검 | 정확 | "Towards more human-like" 절의 "However, another possibility" 단락(미세조정), 개요 단락(새 평가 틀) 일치. 같은 미세조정 FD를 llm-semantics는 "partially"로 적음(에이전트 간 기준 불일치) |
| 17c | 같음 | llm-semantics | 정확 | 정확 | 정확 | 미점검 | 정확 | Table 4 수치(비디오별 평균 상관 0.553, RDM 상관 0.555, GW 1:1 1.69%, 10범주 54.6%), Koide-Majima 자료 평균 r 0.374와 "참가자 집단 간보다 약간 높음", GPT-4V 응답률 23%(507/2185), FD 두 단락 위치 모두 일치. 근거 arXiv:2501.16566(AffectGPT), arXiv:2406.11161(Emotion-LLaMA) 실재 |
| 18 | doi:10.1038/s42003-023-05440-7 | generative-counterfactual | 정확 | 정확 (crossref; pubmed) | 정확 | 해당 없음("yes", "partially") | 정확 | PMID 37872319. PMC10593916 Discussion 3째(표본, 반복, 다양성), 5째(실시간 closed-loop 불가), 6째(BigGAN 한계, 최신 생성기, 이미지 무선효과 미포함) 단락 일치. "yes" 근거 arXiv:2512.00557(NeuroVolve, Jamison 공저) 실재 |
| 19 | arxiv:2206.09398 | geometry-info | 정확 | 정확 | 정확 | FD2 "no" 유지 | 정확 | journal_ref NeurIPS 35 (2022) 21792-21804 일치. 5 Discussion 원문(unbalanced 이득이 소표본에서 불분명, HCP 활용, 학습 가능한 템플릿, entropic epsilon 해석 곤란, 마지막 "Finally" 단락의 인간-비인간 영장류 정렬) 일치. 검색: WebSearch 2회, arXiv 저자 검색 "au:Thual". FUGW로 인간-원숭이를 정렬한 후속 연구 미발견(Xu et al. 2020의 기능 기반 교차종 정렬은 이전 연구이고 다른 방법) |
| 20 | doi:10.1109/embc58623.2025.11254034 | dataset-auditor | 정확 | 정확 (pubmed) | 정확 | 해당 없음 | 정확 | Crossref proceedings-article, PMID 41336410 확인. 인용에 적은 arXiv:2507.12009도 같은 논문. 초록과 요약 일치 |
| 21 | doi:10.1016/j.neuron.2024.04.018 | brain-inspired | 정확 | 정확 | 정확 | "unknown (미검색)" | 정확 (절차 미이행) | PMC11257790 Discussion 4째 단락(청각, 체감각, entorhinal, 두정 피질 지형 가설), 5째 단락 한계(V1과 VTC만 benchmark, feedforward라 층 내 연결 없음) 일치. already_done을 검색하지 않음(CLAUDE.md 5절 절차 미이행, 오류로는 세지 않음) |
| 22 | arxiv:2407.09450 | multimodal-dynamics | 정확 | 정확 | 정확 | FD "no" 유지 | 정확 (경미) | journal_ref ICLR 2025 일치. FD는 5 Discussion "Human studies" 단락의 "Following Michelmann et al. (2023b), one could test ..." 문장. 기록은 "3번째 단락"이라 했으나 페이지 경계를 넘는 첫 단락임. 검색: WebSearch 1회. Michelmann et al.(GPT-3 경계가 개인보다 합의에 가까움)은 선행 연구이고 EM-LLM 경계를 검증한 후속은 미발견 |
| 23a | doi:10.1126/sciadv.abf7129 | emotion-theory | 정확 | 정확 | 정확 | (FD "partially") | 정확 | PMC8064646 Discussion 4째(hybrid 모형), 6째(한계) 단락 일치. 같은 FD를 다른 4개 기록은 "no"로 적음. 근거 doi:10.1038/s41467-025-68240-z(Ma & Kragel 2026)는 실재하나 vmPFC drift 대 상태 구분 검증은 아님 |
| 23b | 같음 | encoding-foundation | 정확 | 정확 | 정확 | FD1 "no" 유지 | 정확 | 4째, 5째 단락 일치. 검색: WebSearch 1회(rSLDS/SLDS + 자연주의 영화 정서 + vmPFC). 미발견. 가장 가까운 것은 threat-of-shock 과제의 SLDS(Misra & Pessoa, eLife 102539) |
| 23c | 같음 | geometry-info | 정확 | 정확 | 정확 | FD3 "no" 오판 | **내용 오류(B)** | FD3(스캔 중 얼굴 측정으로 한 참가자 안에서 정서와 뇌 연결)은 6째 단락과 일치. 그러나 Sato et al. 2025(doi:10.1038/s42003-025-09361-5, PMID 41392191)가 정서 영화 시청 중 fMRI, 얼굴 영상, 연속 valence 평정을 같은 참가자에서 동시에 측정함(PubMed 초록 확인). vmPFC 상태 수준 연결은 아니므로 "partially"가 맞음. systems-neuro(23e)는 같은 논문을 찾아 "partially"로 적음 |
| 23d | 같음 | multimodal-dynamics | 정확 | 정확 | 정확 | FD1 "no" 유지, FD3 "no" 오판 | **내용 오류(B)** | 23c와 같은 이유. 6째 단락 위치 등 나머지는 정확 |
| 23e | 같음 | systems-neuro | 정확 | 정확 | 정확 | FD2 "partially" 정확 | 정확 | 5째 단락(susceptibility artefact, HRF 차이로 설명 안 됨), 6째 단락 일치. Sato 2025 근거 확인 |
| 24 | arxiv:2502.11831 | frontier-ai | 정확 | 정확 | 정확 | FD3 "no" 오판 | **내용 오류(B)** | Discussion 둘째 단락(3~4초 기억, 행동 조건화 불가, 계층 JEPA, action channel), 셋째 단락(영아 시점 비디오) 일치. 경미: FD3를 "둘째 단락 끝"이라 적음. arXiv:2512.06232(Su, Legris, Gureckis, Ren, 2025-12)가 SAYCam(영아 시점 영상)으로 V-JEPA를 사전학습해 IntPhys2에서 검증함(유의한 향상 없음). "yes"가 맞음. 검색: arXiv "intuitive physics AND (infant OR SAYCam OR headcam OR egocentric)". FD1, FD2의 근거 arXiv:2506.09985(V-JEPA 2) 실재 |
| 25a | doi:10.1038/nn.4650 | geometry-info | 정확 | 정확 | 정확 | 해당 없음 | 정확 | Crossref 일치. 초록(SR이 place cell 특징 설명, grid cell은 저차원 기저)과 일치 |
| 25b | 같음 | brain-inspired | 정확 | 정확 | 정확 | 해당 없음 | 정확 (경미, 형식 편차) | discussion_read "no"인데 "장소장 비대칭, 경계 효과" 같은 본문 수준 서술을 씀. 사실관계는 맞으나 출처를 열지 않은 상태의 배경지식. placeholder FD |

## 6. 오류율

### 6.1 전체

| 단위 | 오류 있음 | 오류율 | 95% Wilson 구간 |
|---|---|---|---|
| 논문 (25편), 모든 유형 | 4편 (#7, #10, #23, #24) | 16.0% | 6.4~34.7% |
| 원 기록 (34줄), 모든 유형 | 5줄 (7, 10, 23c, 23d, 24) | 14.7% | 6.4~30.1% |
| 원 기록, 내용 오류 A만(요약, 한계, 절 위치) | 1줄 (10) | 2.9% | 0.5~14.9% |
| 식별자 오류 | 0/25 | 0% | 0~13.3% |
| verified_by 표기 오류 | 0/25 (기록 0/34) | 0% | 0~13.3% |
| already_done "no" 재검색, 기록 단위 | 5/20 | 25.0% | 11.2~46.9% |
| already_done "no" 재검색, 서로 다른 FD 단위 | 4/14 | 28.6% | 11.7~54.6% |

### 6.2 오류 유형별 건수 (기록 단위)

| 유형 | 건수 | 해당 기록 |
|---|---|---|
| 식별자 오류 | 0 | |
| 표기 오류 (verified_by) | 0 | |
| 내용 오류 A (limitations, FD, main_findings, section 불일치) | 1 | 10 (emotion-theory) |
| 내용 오류 B (already_done 오판) | 5 | 7 (llm-semantics), 10 (emotion-theory), 23c (geometry-info), 23d (multimodal-dynamics), 24 (frontier-ai) |
| CLAUDE.md 5절 위반 (미열람인데 Discussion 출처 FD) | 0 | |
| 확인 불가 | 0 | |
| 경미 (오류 미산정): 단락 번호 어긋남 | 3 | 11b, 22, 24 |
| 경미: already_done 근거 서술 부정확 | 1 | 14 ("저랭크") |
| 경미: 미열람 기록에 본문 수준 서술 | 1 | 25b |
| 절차 미이행 (already_done 미검색, placeholder FD) | 5 | 2, 8, 12, 21, 25b (모두 brain-inspired) |

### 6.3 에이전트별

에이전트당 표본이 1~5줄이라 에이전트별 비율은 통계적으로 의미가 약하다. 경향 확인용으로만 본다.

| 에이전트 | 표본 기록 | 오류 기록 | 유형 | 절차 미이행 | 경미 |
|---|---|---|---|---|---|
| encoding-foundation | 4 (1, 14, 15, 23b) | 0 | | 0 | 1 (14) |
| brain-inspired | 5 (2, 8, 12, 21, 25b) | 0 | | 5 | 1 (25b) |
| frontier-ai | 3 (3, 11a, 24) | 1 | B | 0 | 1 (24) |
| geometry-info | 5 (4, 17b, 19, 23c, 25a) | 1 | B | 0 | 0 |
| emotion-theory | 3 (5b, 10, 23a) | 1 | A+B | 0 | 0 |
| systems-neuro | 3 (6, 16, 23e) | 0 | | 0 | 0 |
| llm-semantics | 3 (5a, 7, 17c) | 1 | B | 0 | 0 |
| dataset-auditor | 3 (9, 17a, 20) | 0 | | 0 | 0 |
| multimodal-dynamics | 4 (11b, 13, 22, 23d) | 1 | B | 0 | 2 (11b, 22) |
| generative-counterfactual | 1 (18) | 0 | | 0 | 0 |

## 7. already_done 재검색 상세

| # | FD (요약) | 기록값 (에이전트) | 검색 범위 | 결과 | 판정 |
|---|---|---|---|---|---|
| 1 | 피험자별 TRIBE 적응, 합성 가중, 다중 피험자 사전학습과 결합 | no (encoding-foundation) | arXiv 검색 2건, 2026-06~11 | 원 논문 외 없음 | 유지 |
| 1 | 다른 데이터셋, 모달리티 확장 | no (encoding-foundation) | 위와 같음 | 없음 | 유지 |
| 5 | ToM 영역 표상이 정서 특이적인지 범용 의미인지 | no (llm-semantics) | WebSearch 1회 | 직접 해결 연구 미발견 | 유지 (신뢰도 낮음) |
| 7 | 비디오 직접 입력 또는 더 많은 프레임 | no (llm-semantics) | arXiv "engagement AND GameVibe" | arXiv:2603.18480 (2026-03) 16프레임/초 VLM 입력 검증 | **오판, partially** |
| 7 | LoRA 등 효율적 미세조정 | no (llm-semantics) | 같음 | 2603.18480은 미세조정 없음 명시 | 유지 |
| 10 | 주관 공포 signature를 과정 특이적 개입 평가에 활용 | no, "검색하지 않음" (emotion-theory) | PubMed 2022 이후 | doi:10.1016/j.bpsc.2022.09.008 (Zhang et al. 2022, losartan) | **오판, yes** |
| 11 | 분 단위 창, 메모리 효율 장문맥 MLLM | no (frontier-ai, multimodal-dynamics) | arXiv 1건, WebSearch 1회 | 미발견 | 유지 |
| 14 | parcel 수준 층 attribution | no (encoding-foundation) | arXiv 2건 | 미발견 (원 논문 2026-05) | 유지 |
| 17 | 내수용 신호 통합 모델 | no (dataset-auditor, llm-semantics) | WebSearch 1회 | 인접 연구만 | 유지 |
| 19 | FUGW로 인간-비인간 영장류 정렬 | no (geometry-info) | WebSearch 2회, arXiv 저자 검색 | 미발견 | 유지 |
| 22 | EM-LLM 경계가 개인보다 합의에 가까운지 | no (multimodal-dynamics) | WebSearch 1회 | EM-LLM 대상 후속 미발견 | 유지 |
| 23 | 연속-이산 hybrid 모형으로 vmPFC drift 대 상태 구분 | no 4줄, partially 1줄 | WebSearch 1회, arXiv "switching linear dynamical AND fMRI" | 자연주의 정서 vmPFC 적용 미발견 (threat-of-shock SLDS만) | "no" 유지. emotion-theory의 "partially" 근거는 약함 |
| 23 | 스캔 중 얼굴 측정으로 개인 내 정서와 뇌 연결 | no (geometry-info, multimodal-dynamics), partially (systems-neuro) | PubMed | doi:10.1038/s42003-025-09361-5 (Sato et al. 2025) | **오판 2줄, partially** |
| 24 | 영아 시점 비디오로 학습해도 직관 물리 출현하는지 | no (frontier-ai) | arXiv 1건 | arXiv:2512.06232 (Su et al. 2025-12) | **오판, yes** |

관찰:
* 오판 4건 중 3건(7, 23, 24)은 원 논문과 같은 데이터셋 이름이나 핵심 용어(GameVibe, SAYCam, 동시 얼굴 측정)로 한 번만 검색해도 찾을 수 있었다. 검색 자체를 생략했거나 원 논문 제목 수준의 검색에 그친 것으로 보인다.
* 10번은 원 저자 그룹(Becker, Zhou)의 후속 연구라 저자명 검색으로 바로 나온다.
* 같은 FD에 대해 에이전트마다 판정이 다르다(23번 두 FD, 17번 미세조정 FD). 병합 시 판정이 갈리면 근거 논문 ID가 있는 쪽을 따르는 규칙이 필요하다.

## 8. 표본 밖 관찰 (DB 전체, 읽기만 함)

표본 검증 중 확인한 패턴을 DB와 jsonl 전체에서 세어 보았다. 표본 판정에는 넣지 않았다.

* **placeholder FD:** `literature_db.csv`에서 "(본문 미열람)"처럼 내용 없는 future direction이 들어 있는 행이 22개이고 모두 brain-inspired 출처다(그중 1행은 geometry-info와 공동 기록). `merge.py`가 이를 그대로 세서 n_future_directions가 22만큼 부풀려졌다.
* **already_done 값 분포(DB 전체 future direction 674개):** no 370, partially 235, yes 9, unknown 45, "미확인" 15. unknown 45개는 모두 brain-inspired, "미확인" 15개는 모두 dataset-auditor다. 스키마(no | partially | yes)를 벗어난 값이 60개다.
* **"검색하지 않음", "미검색" 표기:** brain-inspired 5개, emotion-theory 2개. 그중 emotion-theory 2개는 값이 "no"라서 검색 없이 "no"를 적은 셈이다.
* **"yes"가 674개 중 9개(1.3%)뿐이다.** 표본 재검색에서 "no"의 약 4분의 1이 실제로는 partially나 yes였으므로, DB의 "no" 370개 중 상당수가 과소평가일 가능성이 있다. 이는 Stage 3의 Novelty Constraint 판단에 직접 영향을 준다.
* **discussion_read 비스키마 값:** "search_summary"가 dataset-auditor 14, 그 외 5. 스키마는 full_text | abstract_only | no다.
* dataset-auditor의 abstract_only 기록 하나(10.1073/pnas.1702247114)는 future direction section에 "미확인 (Discussion 본문 미열람)"이라고 정직하게 적었으므로 5절 위반이 아니다.

## 9. 자기 문헌 전체 재점검이 필요한 에이전트

**판단:** 요약, 한계, 절 위치의 정확성(내용 오류 A) 기준으로는 오류가 한 에이전트에 몰리지 않았다(전체 1건). 식별자와 표기는 오류가 없다. 따라서 이 기준으로 "전체 재점검"을 지정할 근거는 없다. 대신 다음 두 에이전트를 명시하고, 팀 전체에 already_done 재점검을 권고한다.

1. **brain-inspired: already_done 전체 재점검 필요.**
   * 이유: 표본 5줄 모두 already_done 검색을 하지 않았다(placeholder 4, "unknown (미검색)" 1). DB 전체에서도 future direction 81개 중 45개가 unknown, 5개가 "미검색"이다. CLAUDE.md 5절("각 future direction마다 이후 다른 연구가 이미 수행했는지 검색해서 already_done에 기록")을 체계적으로 이행하지 않았다.
   * 범위: future direction이 있는 모든 기록의 already_done 검색, placeholder FD 22개 삭제. 요약 내용은 표본에서 정확했으므로 재점검 대상이 아니다.
2. **emotion-theory: full_text 기록 18편의 limitations 필드와 already_done 부분 재점검 권고.**
   * 이유: 표본 3줄 중 1줄(Zhou 2021)에서 저자의 이론적 함의를 limitations로 잘못 옮기고 실제 한계 단락을 빠뜨렸으며, 검색하지 않고 "no"를 적었는데 실제로는 수행된 연구가 있었다. 같은 "검색하지 않음" 표기가 1개 더 있다. 표본이 3줄뿐이라 전체 재점검을 요구할 근거는 부족하다.
3. **팀 전체(특히 frontier-ai, llm-semantics, geometry-info, multimodal-dynamics, emotion-theory): already_done "no" 재검색 권고.**
   * 이유: 재검색한 "no" 기록 20줄 중 5줄(25%)이 오판이었고, 오판이 다섯 에이전트에 흩어져 있다. 한 에이전트의 문제가 아니라 검색 깊이의 공통 문제다.
   * 최소 절차 제안: 원 논문 데이터셋명, 모델명, 원 저자명으로 각 1회 이상 검색하고, 검색어와 기간을 already_done에 적는다. Stage 3에서 Novelty Constraint에 쓰이는 FD부터 우선 처리한다.

## 10. Coordinator 수정 제안 (이 에이전트는 파일을 수정하지 않음)

| 대상 | 현재 | 제안 |
|---|---|---|
| emotion-theory/literature.jsonl:12 (Zhou 2021) limitations | Discussion 3~4째 단락 이론적 함의 | Discussion 8~9째 단락: IAPS 정지 이미지만 사용, SVR 단일 기법, 사전등록 없음, 조건화 위협 decoder와 패러다임 불일치. FD 추가 고려: 비디오 자극에서 VIFS 검증(Discussion 8째 단락) |
| 같은 줄 already_done | no (검색하지 않음) | yes (doi:10.1016/j.bpsc.2022.09.008) |
| llm-semantics/literature.jsonl:28 (Melhart 2025) FD1 | no | partially (arXiv:2603.18480, 다중 프레임 VLM 입력, 미세조정 없음) |
| frontier-ai/literature.jsonl:2 (Garrido 2025) FD3 | no (이번 검색 범위) | yes (arXiv:2512.06232) |
| geometry-info/literature.jsonl:10, multimodal-dynamics/literature.jsonl:2 (Chang 2021) 얼굴 측정 FD | no | partially (doi:10.1038/s42003-025-09361-5) |
| encoding-foundation/literature.jsonl:10 (MIRAGE) FD1 근거 서술 | "저랭크 subject block" | "subject-conditional linear layer와 unseen-subject layer" |
| literature_db.csv n_future_directions | placeholder FD 포함 | merge.py에서 내용 없는 FD 제외 |
| already_done 비스키마 값 (unknown, 미확인) | 60개 | 재검색 후 no, partially, yes로 정리 |
| 중복 기록의 already_done 불일치 | 병합 시 그대로 나열 | 근거 ID가 있는 판정을 우선하는 규칙 |
