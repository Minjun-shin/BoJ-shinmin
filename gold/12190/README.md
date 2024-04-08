# Minesweeper (Small)

### Gold 5

Minesweeper is a computer game that became popular in the 1980s, and is still included in some versions of the Microsoft Windows operating system. This problem has a similar idea, but it does not assume you have played Minesweeper.

In this problem, you are playing a game on a grid of identical cells. The content of each cell is initially hidden. There are M mines hidden in M different cells of the grid. No other cells contain mines. You may click on any cell to reveal it. If the revealed cell contains a mine, then the game is over, and you lose. Otherwise, the revealed cell will contain a digit between 0 and 8, inclusive, which corresponds to the number of neighboring cells that contain mines. Two cells are neighbors if they share a corner or an edge. Additionally, if the revealed cell contains a 0, then all of the neighbors of the revealed cell are automatically revealed as well, recursively. When all the cells that don't contain mines have been revealed, the game ends, and you win.

For example, an initial configuration of the board may look like this ('*' denotes a mine, and 'c' is the first clicked cell):

```
*..*...**.
....*.....
..c..*....
........*.
..........
```

There are no mines adjacent to the clicked cell, so when it is revealed, it becomes a 0, and its 8 adjacent cells are revealed as well. This process continues, resulting in the following board:

```
*..*...**.
1112*.....
00012*....
00001111*.
00000001..
```

At this point, there are still un-revealed cells that do not contain mines (denoted by '.' characters), so the player has to click again in order to continue the game.

You want to win the game as quickly as possible. You want to find the minimum number of clicks to win the game. Given the size of the board (N x N), output such minimum number of clicks.

## 입력
The first line of the input gives the number of test cases, T. Ttest cases follow. First line of each test case contains one integer N. N lines strings with length N follows containing '*' and '.', denotes the Minesweeper initial board.

## 출력
For each test case, output one line containing "Case #x: y", where x is the test case number (starting from 1) and y is the minimum number of clicks to win.

## 문제풀이
지뢰찾기 게임에서 지뢰를 제외한 칸을 여는데 누르는 최소 칸의 개수를 묻는 문제이다. 특정 칸을 열었을 때 나오는 숫자는 주변 상하좌우 및 대각선 칸에 있는 지뢰의 개수이다. 이때 숫자가 0이면 주변 칸을 모두 연다. 이로 인해 열린 칸의 숫자가 0일 때에도 주변 칸을 연다.

최소로 진행하는 경우는 먼저 0인 칸을 모두 열고 남은 지뢰가 아닌 칸을 모두 여는 경우이다. 따라서 0인 숫자의 뭉치의 개수를 먼저 구했다. `is_inrange`는 해당 칸이 보드 위에 있는 칸인지 검사하는 함수 이고, `calc` 주변 칸에 지뢰가 있으면 True, 없으면 False를 반환한다.

이차원 배열을 순서대로 순회하며 열리지 않은 0인 칸을 마주치면 넓이 위주 탐색으로 주어진 규칙대로 열리는 모든 칸을 기록한다.

이때 기록한 횟수와 남은 지뢰가 아닌 칸들의 개수를 합치면 답이 된다.