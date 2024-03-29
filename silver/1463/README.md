# 1로 만들기

### Silver 3

정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.

1. X가 3으로 나누어 떨어지면, 3으로 나눈다.
1. X가 2로 나누어 떨어지면, 2로 나눈다.
1. 1을 뺀다.
   
정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.

## 입력
첫째 줄에 1보다 크거나 같고, 106보다 작거나 같은 정수 N이 주어진다.

## 출력
첫째 줄에 연산을 하는 횟수의 최솟값을 출력한다.

## 문제풀이
정수 `N`은 최대 세 가지 수를 지날 수 있는데, `N - 1`, `N // 2`, `N // 3`이다.

따라서 DP의 형식으로 코드를 작성하고 위 세 수 중 가능한 모든 경우 중 가장 작은 값 + 1을 `N`의 경우의 답이 되도록 코드를 작성하였다.