# 사용법

원래 단일 지침을 Claude Code가 읽는 위치에 맞게 나눈 폴더입니다. 각 파일의 역할은 다음과 같습니다.

| 파일 | 역할 |
|---|---|
| `CLAUDE.md` | 모든 에이전트에게 자동 전달되는 공통 규칙. Mission, 원칙, 문헌 규칙, Safeguards. |
| `.claude/agents/*.md` | 12개 에이전트 정의. 각 에이전트의 담당 Axis와 조사 범위. |
| `reference/axes.md` | Axis A~T, 외부 분야, Axis 유형과 담당 에이전트 표. |
| `reference/protocols.md` | Round 1~4, 조합 규칙, 평가 기준, Question Card와 Pilot 양식. |
| `reference/datasets_and_resources.md` | 데이터셋 출발점 정보, 우리 환경 정보 칸, Stage 1 Gate. |
| `reference/starting_papers.md` | 필수 출발 문헌. |
| `reference/existing_projects.md` | 기존 프로젝트 요약. 겹침 확인 전용. |
| `prompts/stage1~4_*.md` | 단계별 실행 지시. |

## 시작 전에

1. **폴더 위치:** 이 폴더를 EmoBrain 폴더 **바깥**에 둡니다. 안에 두면 상위 폴더의 CLAUDE.md가 함께 로드됩니다.
2. **우리 환경 정보:** `reference/datasets_and_resources.md` 1절을 채웁니다. 데이터 경로, 원본 자극 보유 여부, 계산 자원 등입니다.
3. **기존 프로젝트:** `reference/existing_projects.md`의 요약이 맞는지 확인합니다.
4. **전역 지침:** `~/.claude/CLAUDE.md`에 EmoBrain 관련 지침이 있다면 이 작업 동안 빼 둡니다. 이 파일은 모든 프로젝트에 적용됩니다.
5. **데이터 접근:** 데이터가 다른 폴더에 있으면 `claude --add-dir <데이터 경로>`로 실행합니다. 추가한 폴더의 CLAUDE.md는 기본적으로 로드되지 않습니다.

## 실행

이 폴더에서 `claude`를 실행하고 다음처럼 입력합니다.

```
@prompts/stage1_dataset_audit.md 를 실행해
```

Stage가 끝나면 Coordinator가 멈추고 `outputs/STAGE_STATUS.md`의 확인 항목을 보여줍니다. 내용을 확인하고 필요한 결정을 STAGE_STATUS.md에 적은 뒤, `/clear`로 대화를 비우고 다음 Stage를 실행합니다.

```
@prompts/stage2_axes_literature.md 를 실행해
@prompts/stage3_discussion_combination.md 를 실행해
@prompts/stage4_evaluation_proposals.md 를 실행해
```

Stage 3은 Stage 2의 에이전트를 재개하는 편이 좋습니다. 그러니 Stage 2와 3은 가능하면 같은 세션에서 이어서 실행하는 것을 권합니다. 세션이 바뀌어도 파일로 이어지게 되어 있습니다.

## 참고

* **권한 요청:** 백그라운드 에이전트의 권한 요청(WebSearch, WebFetch, 파일 쓰기)은 메인 세션에 뜹니다. Stage 2는 에이전트 11개가 동시에 검색하므로 요청이 많습니다.
* **토큰 사용량:** 에이전트마다 자체 토큰을 쓰므로 사용량이 큽니다. Stage 2가 가장 많이 씁니다.
