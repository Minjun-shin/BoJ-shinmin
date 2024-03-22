# 곱셈

### Silver 1

자연수 A를 B번 곱한 수를 알고 싶다. 단 구하려는 수가 매우 커질 수 있으므로 이를 C로 나눈 나머지를 구하는 프로그램을 작성하시오.

## 입력
첫째 줄에 A, B, C가 빈 칸을 사이에 두고 순서대로 주어진다. A, B, C는 모두 2,147,483,647 이하의 자연수이다.

## 출력
첫째 줄에 A를 B번 곱한 수를 C로 나눈 나머지를 출력한다.

## 문제풀이
수가 매우 클 경우의 거듭제곱을 계산하는 문제이다. 이를 해결하기 위해 분할 정복으로 문제를 풀었다. 재귀 함수로 작성하였는데 만일 지수가 1인 경우 `a % c`를 출력하고 아닌 경우에는 홀수 짝수로 나누어 짝수이면 `calc(a, b // 2, c) ** 2`의 나머지를 출력하고 홀수이면 `calc(a, b // 2, c) ** 2 * calc(a, 1, c)`의 나머지를 출력했다.