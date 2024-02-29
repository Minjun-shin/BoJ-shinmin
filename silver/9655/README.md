# 돌 게임

### Silver 5

돌 게임은 두 명이서 즐기는 재밌는 게임이다.

탁자 위에 돌 N개가 있다. 상근이와 창영이는 턴을 번갈아가면서 돌을 가져가며, 돌은 1개 또는 3개 가져갈 수 있다. 마지막 돌을 가져가는 사람이 게임을 이기게 된다.

두 사람이 완벽하게 게임을 했을 때, 이기는 사람을 구하는 프로그램을 작성하시오. 게임은 상근이가 먼저 시작한다.

## 입력
첫째 줄에 N이 주어진다. (1 ≤ N ≤ 1000)

## 출력
상근이가 게임을 이기면 SK를, 창영이가 게임을 이기면 CY을 출력한다.

## 문제풀이
사실 이 문제는 홀수인지 짝수인지에 따라 답이 결정되는 문제이다. 왜냐하면 가져갈 수 있는 개수가 1개 또는 3개라는 것은 무조건 홀수 개 밖에 가져갈 수 없다는 얘기이다. 바꿔 말하면 가져가는 턴 수에 따라 총 돌의 개수가 짝수가 되고 홀수가 된다는 의미이다.

결론적으로 주어진 수가 짝수면 창영이 이기고 홀수이면 상근이 이긴다.

DP적으로 생각하면 마지막 돌을 갖기 위한 최소 횟수를 가지고자 할 것이다. 따라서 1개 전의 횟수와 3개 전의 횟수 중 최소값에 1을 더한 값을 갖게 된다. 그리고 짝수인지 홀수인지를 봐야 누구 차례인지 알 수 있다.