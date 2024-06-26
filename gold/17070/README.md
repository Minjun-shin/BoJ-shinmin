# 파이프 옮기기 1

### Gold 5

유현이가 새 집으로 이사했다. 새 집의 크기는 N×N의 격자판으로 나타낼 수 있고, 1×1크기의 정사각형 칸으로 나누어져 있다. 각각의 칸은 (r, c)로 나타낼 수 있다. 여기서 r은 행의 번호, c는 열의 번호이고, 행과 열의 번호는 1부터 시작한다. 각각의 칸은 빈 칸이거나 벽이다.

오늘은 집 수리를 위해서 파이프 하나를 옮기려고 한다. 파이프는 아래와 같은 형태이고, 2개의 연속된 칸을 차지하는 크기이다.

<p align=center>
  <img src="./pipe1.avif" style="width:15%;">
</p>

파이프는 회전시킬 수 있으며, 아래와 같이 3가지 방향이 가능하다.

<p align=center>
  <img src="./pipe2.avif" style="width:40%;">
</p>

파이프는 매우 무겁기 때문에, 유현이는 파이프를 밀어서 이동시키려고 한다. 벽에는 새로운 벽지를 발랐기 때문에, 파이프가 벽을 긁으면 안 된다. 즉, 파이프는 항상 빈 칸만 차지해야 한다.

파이프를 밀 수 있는 방향은 총 3가지가 있으며, →, ↘, ↓ 방향이다. 파이프는 밀면서 회전시킬 수 있다. 회전은 45도만 회전시킬 수 있으며, 미는 방향은 오른쪽, 아래, 또는 오른쪽 아래 대각선 방향이어야 한다.

파이프가 가로로 놓여진 경우에 가능한 이동 방법은 총 2가지, 세로로 놓여진 경우에는 2가지, 대각선 방향으로 놓여진 경우에는 3가지가 있다.

아래 그림은 파이프가 놓여진 방향에 따라서 이동할 수 있는 방법을 모두 나타낸 것이고, 꼭 빈 칸이어야 하는 곳은 색으로 표시되어져 있다.

<p align=center>
  <img src="./pipe3.avif" style="width:60%;"><br>
  가로
</p>

<p align=center>
  <img src="./pipe4.avif" style="width:60%;"><br>
  세로
</p>

<p align=center>
  <img src="./pipe5.avif" style="width:90%;"><br>
  대각선
</p>

가장 처음에 파이프는 (1, 1)와 (1, 2)를 차지하고 있고, 방향은 가로이다. 파이프의 한쪽 끝을 (N, N)로 이동시키는 방법의 개수를 구해보자.

## 입력
첫째 줄에 집의 크기 N(3 ≤ N ≤ 16)이 주어진다. 둘째 줄부터 N개의 줄에는 집의 상태가 주어진다. 빈 칸은 0, 벽은 1로 주어진다. (1, 1)과 (1, 2)는 항상 빈 칸이다.

## 출력
첫째 줄에 파이프의 한쪽 끝을 (N, N)으로 이동시키는 방법의 수를 출력한다. 이동시킬 수 없는 경우에는 0을 출력한다. 방법의 수는 항상 1,000,000보다 작거나 같다.

## 문제풀이
다이나믹 프로그래밍으로 문제를 해결했다.

전체적으로 $N \times N$형태의 dp용 배열을 만드는데 각 칸의 원소가 숫자 세 개를 갖는 리스트이다. 각 숫자는 그 칸이 파이프의 한 쪽 끝인 경우의 수인데 파이프 상태가 가로, 대각선, 세로일 때의 경우의 수이다.

이를 토대로 $N \times N$의 순회를 하는데 첫 번째 행일때는 벽이 없는 한 전에 칸에서 계속 가로로 진행하기 때문에 각 칸의 첫 번째 숫자만 갱신한다. 첫 번째 세로열은 초기 상태가 가로이기 때문에 도달할 수 없기 때문에 무시했다.

나머지 경우는 각자 그 칸에 도달할 수 있는 전의 칸을 생각해야 하는데 예를 들면 어떤 칸의 가로인 경우의 수는 바로 왼쪽 칸에서 계속 가로로 오는 경우와 대각선에서 회전한 경우 두 가지이므로 이 두 수를 더하면 된다.

벽을 고려한 방법은 일단 해당 칸이 벽이면 계산을 하지 않고 다음 칸으로 넘어갔고 대각선의 경우에는 파이프의 끝이 존재하는 두 칸뿐 아니라 $2 \times 2$칸을 모두 고려해서 그 안에 벽이 존재하면 계산하지 않았다.

모든 반복이 끝나고 (N, N)칸의 모든 값들을 더한 것이 답이 된다.