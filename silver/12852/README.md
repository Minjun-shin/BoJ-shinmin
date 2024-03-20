# 1로 만들기 2

### Silver 1

정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.

1. X가 3으로 나누어 떨어지면, 3으로 나눈다.
1. X가 2로 나누어 떨어지면, 2로 나눈다.
1. 1을 뺀다.

정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.

## 입력
첫째 줄에 1보다 크거나 같고, 10<sup>6</sup>보다 작거나 같은 자연수 N이 주어진다.

## 출력
첫째 줄에 연산을 하는 횟수의 최솟값을 출력한다.

둘째 줄에는 N을 1로 만드는 방법에 포함되어 있는 수를 공백으로 구분해서 순서대로 출력한다. 정답이 여러 가지인 경우에는 아무거나 출력한다.

## 문제풀이
큐를 이용한 넓이 우선 탐색과 다이나믹 프로그래밍으로 문제를 해결했다. N이하의 모든 숫자에 대한 결과를 저장할 길이 N+1의 리스트 `res`를 만들었다. 결과값은 해당 숫자로 가기 위한 횟수와 경로의 정보를 저장하였다. 처음에는 1에서부터 시작하여 N으로 올라가며 진행했지만 이 경우 2의 배수와 3의 배수가 무조건 존재하기에 더 많은 경우를 조회하므로 시간 초과가 났다. 따라서 N에서 1로 내려가는 방식으로 경로를 저장된 값에 추가하는 형식으로 다이나믹 프로그래밍을 작성하여 답을 도출했다.