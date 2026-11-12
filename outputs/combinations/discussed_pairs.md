# 이미 논의된 Axis 조합 (discussed_pairs)

* 생성: `python3 -I outputs/combinations/build_discussed_pairs.py`
* 입력: Round 1 chain 80개(주제별 Axis 매핑, Coordinator 판단), Round 2 제안 76개(제안의 '관련 Axis'), Round 3 수정안 0개
* Axis는 A~W 23개(X는 R, Y는 A에 포함). Round 1 chain의 Axis는 chain이 속한 Deliverable D 주제와 보낸 에이전트의 담당 Axis로 근사했으므로 과대 집계될 수 있다.

## 요약

* 가능한 2개 조합 253개 중 논의된 것 226개, 논의되지 않은 것 27개(그중 서로 다른 유형끼리 23개)
* 논의된 3개 조합: 621개

## 논의되지 않은 2개 조합 (서로 다른 유형, Round 4 후보)

B+K, D+G, D+S, F+V, I+W, J+U, J+V, J+W, K+L, K+P, K+V, L+W, M+V, M+W, N+W, O+V, P+V, P+W, Q+V, R+W, S+V, T+V, T+W

## 가장 많이 논의된 2개 조합 (상위 40)

| 조합 | 횟수 | 등장 라운드 |
|---|---|---|
| A+Q | 34 | R1, R2 |
| O+Q | 33 | R1, R2 |
| D+N | 30 | R1, R2 |
| A+O | 28 | R1, R2 |
| H+L | 28 | R1, R2 |
| K+O | 27 | R1, R2 |
| L+P | 26 | R1, R2 |
| F+H | 26 | R1, R2 |
| A+U | 25 | R1, R2 |
| Q+U | 22 | R1, R2 |
| H+S | 22 | R1, R2 |
| D+E | 21 | R1, R2 |
| D+K | 21 | R1, R2 |
| E+K | 21 | R1, R2 |
| O+U | 21 | R1, R2 |
| F+S | 21 | R1, R2 |
| K+Q | 20 | R1, R2 |
| Q+T | 20 | R1, R2 |
| E+N | 19 | R1, R2 |
| D+M | 19 | R1, R2 |
| B+L | 18 | R1, R2 |
| C+U | 18 | R1, R2 |
| C+H | 17 | R1, R2 |
| C+L | 17 | R1, R2 |
| H+P | 17 | R1, R2 |
| O+T | 16 | R1, R2 |
| B+C | 16 | R1, R2 |
| B+H | 16 | R1, R2 |
| B+P | 16 | R1, R2 |
| C+P | 16 | R1, R2 |
| K+N | 16 | R1, R2 |
| L+S | 16 | R1, R2 |
| K+T | 15 | R1, R2 |
| F+L | 15 | R1, R2 |
| A+K | 14 | R1, R2 |
| C+N | 13 | R1, R2 |
| C+D | 13 | R1, R2 |
| A+E | 13 | R1, R2 |
| I+R | 13 | R1, R2 |
| A+C | 13 | R1, R2 |

## 적게 논의된 2개 조합 (1~2회)

A+B(2), A+G(2), A+J(1), A+L(2), A+P(2), A+S(2), A+V(1), B+D(1), B+J(2), B+M(1), B+O(1), B+Q(2), B+T(1), C+G(2), C+S(2), C+T(1), C+V(2), C+W(2), D+F(1), D+H(2), D+P(2), D+V(1), E+P(2), E+V(2), F+I(1), F+J(1), F+K(1), F+M(2), F+N(1), G+K(1), G+N(1), G+P(2), G+R(1), G+S(2), G+T(2), G+V(1), H+K(1), H+M(2), H+V(1), I+M(2), I+O(2), I+P(2), I+Q(1), I+T(1), I+U(1), I+V(2), J+M(2), J+O(2), J+P(2), J+Q(1), J+S(2), J+T(1), K+W(1), L+O(2), L+V(1), M+R(2), M+S(1), M+U(2), N+Q(1), N+S(2), N+T(2), N+U(2), N+V(1), O+P(2), O+W(2), R+V(1), S+W(1), U+V(1), U+W(2), V+W(1)

## 가장 많이 논의된 3개 조합 (상위 40)

| 조합 | 횟수 |
|---|---|
| A+O+Q | 25 |
| F+H+S | 20 |
| K+O+Q | 18 |
| D+E+K | 18 |
| A+O+U | 17 |
| O+Q+U | 17 |
| O+Q+T | 16 |
| C+L+P | 16 |
| H+L+P | 16 |
| D+K+N | 16 |
| A+Q+U | 16 |
| H+L+S | 16 |
| B+H+L | 15 |
| B+L+P | 15 |
| D+E+N | 15 |
| E+K+N | 15 |
| F+H+L | 15 |
| F+L+S | 15 |
| A+K+O | 14 |
| B+C+H | 14 |
| A+K+Q | 13 |
| K+O+T | 13 |
| K+Q+T | 13 |
| B+C+L | 13 |
| B+C+P | 13 |
| B+H+P | 13 |
| C+H+L | 13 |
| C+H+P | 13 |
| A+O+T | 12 |
| A+Q+T | 12 |
| D+M+N | 12 |
| A+K+T | 11 |
| C+D+N | 10 |
| A+C+U | 10 |
| C+D+M | 9 |
| I+J+R | 9 |
| C+M+N | 8 |
| E+K+O | 8 |
| A+E+H | 7 |
| D+I+N | 7 |

## Axis별 등장 횟수

| Axis | 유형 | 등장한 조합 수 |
|---|---|---|
| A | Construct | 49 |
| B | Construct | 29 |
| C | Construct | 45 |
| D | Construct | 44 |
| E | Neural | 50 |
| F | Neural | 28 |
| G | Model & Method | 18 |
| H | Model & Method | 49 |
| I | Model & Method | 16 |
| J | Model & Method | 10 |
| K | Structure | 43 |
| L | Model & Method | 40 |
| M | Model & Method | 21 |
| N | Model & Method | 39 |
| O | Neural | 46 |
| P | Inference | 28 |
| Q | Inference | 51 |
| R | Structure | 24 |
| S | Inference | 31 |
| T | Inference | 31 |
| U | Inference | 41 |
| V | Construct | 5 |
| W | Construct | 13 |
