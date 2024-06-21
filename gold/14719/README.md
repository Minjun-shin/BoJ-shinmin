# 빗물

### Gold 5

2차원 세계에 블록이 쌓여있다. 비가 오면 블록 사이에 빗물이 고인다.

![rain1](rain1.png)![rain2](rain2.png)

비는 충분히 많이 온다. 고이는 빗물의 총량은 얼마일까?

## 입력
첫 번째 줄에는 2차원 세계의 세로 길이 H과 2차원 세계의 가로 길이 W가 주어진다. (1 ≤ H, W ≤ 500)

두 번째 줄에는 블록이 쌓인 높이를 의미하는 0이상 H이하의 정수가 2차원 세계의 맨 왼쪽 위치부터 차례대로 W개 주어진다.

따라서 블록 내부의 빈 공간이 생길 수 없다. 또 2차원 세계의 바닥은 항상 막혀있다고 가정하여도 좋다.

## 출력
2차원 세계에서는 한 칸의 용량은 1이다. 고이는 빗물의 총량을 출력하여라.

빗물이 전혀 고이지 않을 경우 0을 출력하여라.

## 문제풀이
물이 고이는 오목한 곳은 양쪽에 벽이 있는 경우이다. 따라서 양쪽 방향으로 진행하며 현재 기록된 값보다 작으면 일단 고인다고 계산하고 그 차이를 기록한다. 이렇게 기록한 값들 중 각 칸마다 더 작은 값을 최종적으로 저장해서 그 값들의 함을 답으로 출력했다.