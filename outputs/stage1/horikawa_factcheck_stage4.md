# Horikawa 관련 사실 확인 (Stage 4 준비용)

* 작성: dataset-auditor (Agent 1). 기준일 2026-11-12
* 요청: 사용자 답변 세 가지("Horikawa 2020 참가자는 일본인", "Cowen & Keltner 2,185개 영상은 모두 무음", "Horikawa 2020과 Mind captioning 피험자는 겹치지 않음")를 원문으로 확인
* 사용 경로: PubMed MCP 전문 도구(PMC), WebSearch, 앞서 읽은 OpenNeuro ds002425 README. WebFetch는 이 세션에서 pmc.ncbi.nlm.nih.gov, data.mendeley.com이 DNS 차단되어, 도구 안내에 따라 다른 출판사 페이지(cell.com, pnas.org, biorxiv.org)는 시도하지 않았다. 차단 우회는 하지 않았다.
* 표기: [원문]은 해당 논문 본문을 직접 읽음, [2차 본문]은 다른 논문 본문을 직접 읽음, [검색]은 검색 요약이나 스니펫만 봄

## 요약 판정

| 사용자 진술 | 판정 | 한 줄 근거 |
|---|---|---|
| Horikawa 2020 참가자는 일본인이다 | **원문으로 확인 불가** | Horikawa 2020의 피험자 기술은 보충자료(Transparent Methods)에만 있고 열지 못함. 확인 가능한 모든 출처(재사용 논문의 피험자 기술, OpenNeuro README)에 국적이나 모국어 언급이 **없음** |
| Cowen & Keltner의 2,185개 영상은 모두 무음이다 | **부분 확인(2차 출처), 원문 미확인** | 평정자와 fMRI 참가자 모두 소리 없이 보았다는 2차 근거는 일관됨. 그러나 원본 파일에 오디오가 원래 있었는지는 2차 서술끼리 엇갈림("소리를 제거했다"는 표현 대 "오디오 없는 영상"). PNAS Methods와 SI는 열지 못함 |
| Horikawa 2020과 Mind captioning 피험자는 겹치지 않는다 | **원문으로 확인 불가(언급 없음)** | Mind captioning 본문에 Horikawa 2020 피험자와의 중복 여부 언급이 없음. 촬영 장소, 스캐너, 윤리위원회가 다르다는 점만 확인됨. 비중복은 추론일 뿐 |

## 1. Horikawa 2020 피험자 기술

* PMC7191651 본문(PubMed MCP)의 Methods 절은 다음 한 문장뿐이다: "All methods can be found in the accompanying [Transparent Methods]." [원문]. 피험자 인원 외 정보(성별, 나이, 국적, 윤리 승인)는 본문에 없고, 보충자료는 열지 못했다.
* 본문에서 확인되는 것은 인원뿐이다: "we measured whole-brain functional magnetic resonance imaging (fMRI) signals while five subjects watched 2,181 emotionally evocative short videos" [원문, Introduction 마지막에서 둘째 단락].
* 같은 데이터를 재사용한 Du et al. (2023, iScience, doi:10.1016/j.isci.2023.107571, PMC10470388)의 STAR Methods [2차 본문]:
  * "Five healthy subjects (1 female; [평균 나이는 PMC 텍스트에서 누락]; range 23-34 years; referred to as S01-S05) with normal or corrected-to-normal vision participated in the visually evoked emotional experiment."
  * "All subjects signed written informed consent, and the study protocol was approved by the Ethics Committee of ATR."
  * 평균 나이 25.8세는 이 논문 페이지의 검색 스니펫으로만 확인 [검색].
* OpenNeuro ds002425 README와 디렉터리 [이전 감사에서 직접 읽음]: participants.tsv가 없고, README에 국적이나 모국어 기술이 없다.
* **국적, 모국어: 확인 가능한 모든 출처에 없음.** Horikawa 2020 Transparent Methods 원문에 있는지는 미확인이다. 윤리 승인 기관(ATR)도 원문이 아니라 2차 본문 기준이다.

## 2. Cowen & Keltner 2017 영상의 소리

* 원문 접근 실패: PubMed MCP로 PMC5617253 전문을 두 번 요청했으나 full_text가 빈 값으로 반환되고 abstract만 왔다. pnas.org와 SI PDF는 WebFetch 차단 안내에 따라 시도하지 않았다. 따라서 **원문의 Methods와 SI에서 확인한 내용은 없다.**
* Abstract [원문]: 소리 언급 없음. "2,185 emotionally evocative short videos"만 있음.
* Horikawa 2020 본문 [원문]:
  * Discussion 7째 단락: Cowen & Keltner가 인터넷의 자극을 활용해 자극을 모았다고 쓴 뒤 "although it is worth noting that these stimuli are still only visual in nature."
  * Discussion 9째 단락: "Although here we used only visual stimuli (with no sound)"
* Du et al. 2023 [2차 본문] (fMRI 제시 조건): "(the sound of the videos was removed, leaving only the visual stimuli)". 이 표현은 적어도 일부 원본 파일에 소리가 있었을 가능성을 시사하지만 단정할 수 없다. 평정자 조건에 대한 서술은 아니다.
* Horikawa 2025 Mind captioning [2차 본문] (fMRI 제시 조건): "They were presented at the center of a gray background without sound."
* Asanuma et al. 2025 (Sci Rep, doi:10.1038/s41598-025-14961-6, PMC12402258) [2차 본문] (평정자 조건):
  * "2185 short video clips (averaging about 5 seconds in length and containing no audio) were presented to participants"
  * "the Cowen & Keltner data involve short, audio-free videos rated by English speakers"
* 보도 기사(sci.news) [검색]: 853명이 "silent 5- to-10-second videos"를 무작위로 보았다고 서술.
* **판정:** "평정 단계와 fMRI 제시 단계 모두 소리 없이 제시되었다"는 2차 출처에서 일관되게 지지된다. "원본 영상에 원래 소리가 없었다"는 의미라면 원문으로 확인하지 못했고, 2차 서술도 엇갈린다(Du 2023의 "removed" 대 Asanuma 2025의 "containing no audio"). Google Form으로 받는 배포 파일에 오디오 트랙이 있는지도 미확인이다.
* 부수 정보 [검색]: 14개 affective dimension은 평정자 하위 표본이 비디오당 9명씩 평정했고, semantic 73개 특징은 별도 표본이 예/아니오로 평정했다는 서술이 검색 스니펫에 있다. Stage 1 보고서에서 "비디오당 dimension 평정자 수 미확인"으로 둔 항목의 후보 답이지만 원문 확인 전까지는 미확인으로 유지한다.

## 3. Horikawa 2025 Mind captioning (Science Advances 11(45):eadw1464, doi:10.1126/sciadv.adw1464, PMID 41191769, PMC12588295)

PubMed MCP로 본문 전체를 받아 해당 부분을 읽었다 [원문]. 단일 저자(Tomoyasu Horikawa, NTT Communication Science Laboratories).

* 피험자 (Materials and Methods, Subjects):
  * "Six healthy individuals (S1: male, aged 37 to 38; S2: female, aged 37 to 38; S3: male, aged 33 to 34; S4: female, aged 35 to 36; S5: male, aged 29 to 30; and S6: male, aged 22 to 23) with normal or corrected-to-normal vision participated in the experiments."
  * "All were native Japanese speakers and non-native English speakers; S1 to S5 were proficient in English, while S6 had limited proficiency."
  * "the study protocol was approved by the Ethics Committee of NTT (R03-004 and R03-009)." "Data from each subject were collected over multiple scanning sessions spanning ~6 months."
  * Results 서두에도 "six subjects, all Japanese individuals who were non-native English speakers"라는 표현이 있다.
* 촬영 (MRI acquisition): "3.0-Tesla Siemens MAGNETOM Prisma scanner located at the WPI-IRCN Human fMRI Core, the University of Tokyo", TR 1000 ms. Horikawa 2020은 3T Siemens Verio(OpenNeuro JSON), TR 2000 ms, ATR 윤리 승인(2차 본문)이었다.
* **Horikawa 2020 피험자와의 중복 여부: 본문에 언급 없음.** "participated", "previous", "2020", "same subjects", "overlap" 등으로 검색했으나 해당 문장이 없다. PMC 텍스트에서는 참고문헌 번호가 빠져 있고, 보충자료는 읽지 않았다.
* **중요한 추가 사실 (Stage 4 관련):** Mind captioning은 Horikawa 2020과 **같은 영상 세트**를 쓴 것으로 보인다.
  * "Visual stimuli consisted of 2196 short videos (all: 0.152 to 90.1 s, mean = 6.61 s, and median = 4.51 s ...) from a previous study"
  * "Sixteen duplicates were excluded to avoid redundancy, resulting in the final set of 2180 unique videos"
  * 개수 2,196과 길이 범위가 Horikawa 2020 데이터와 일치한다. 다만 인용된 "previous study"가 누구인지는 PMC 텍스트에서 참고문헌이 빠져 직접 확인하지 못했다.
  * 설계 차이: 학습 60 run, 테스트 10 run, 테스트 72개 영상은 5회 반복 제시, 10 s 미만 영상은 10 s를 넘길 때까지 반복 재생, 영상당 crowdsourced caption 20개. 인코딩 통계의 n = 2108이며 EmoMind의 "MindCaptioning 2,108 clips"와 일치한다.
  * 저작권: "Because of copyright restrictions, the actual video frames used in the experiments have been replaced with schematic illustrations throughout this paper." Stage 1의 G1 판단(재배포 제한 가능성)을 뒷받침하는 원문 근거다.
  * 데이터 공개: "The collected video captions are available from our repository"라는 문장만 확인했다. fMRI 데이터 공개 여부와 위치는 미확인이다(PMC 텍스트에 Data availability 절이 없음).
* **판정:** 중복 여부는 원문에 없다. 장소(교토 대 도쿄), 스캐너(Verio 대 Prisma), 윤리위원회(ATR 대 NTT), 인원(5 대 6), 성비(여 1 대 여 2)가 다르다. 그러나 이것만으로 같은 사람이 없다고 결론낼 수 없다. 사용자 진술은 미검증으로 둔다.

## Stage 4에 넘길 함의

1. 국적과 언어: Mind captioning 피험자는 일본어 모국어 화자로 원문이 확인된다. Horikawa 2020 피험자는 확인되지 않는다. 따라서 "평정자(미국 영어 사용자)와 fMRI 참가자 간 문화, 언어 불일치"는 Horikawa 2020에 대해서는 가능성으로만 쓰고, 사실로 쓰지 않는다.
2. 무음: "무음 제시"는 쓸 수 있다. "원본 영상 자체가 무음"이라고 쓰지는 않는다.
3. Mind captioning은 같은 2,196개 영상에 대한 두 번째 fMRI 데이터셋 후보다. 다른 피험자 6명, 반복 제시 테스트 세트, caption이 있다. fMRI 공개 여부를 확인하면 같은 자극의 피험자 간, 데이터셋 간 검증과 noise ceiling 추정에 쓸 수 있다. 다만 두 데이터셋의 피험자 중복 여부를 먼저 확인해야 하며, 확인 전에는 독립 표본으로 취급하지 않는다.

## 미확인으로 남은 항목

* Horikawa 2020 Transparent Methods 원문(피험자 국적, 모국어, 나이, 윤리 승인 문장)
* Cowen & Keltner 2017 Methods와 SI의 소리 관련 서술, 배포 파일의 오디오 트랙 유무
* Mind captioning 보충자료와 Data availability 절, 인용된 "previous study"의 정체, fMRI 데이터 공개 여부
* 두 연구 간 피험자 중복 여부. 저자(Horikawa)나 데이터 관리자에게 문의하는 것이 가장 확실하다
