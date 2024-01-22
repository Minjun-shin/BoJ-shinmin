# 한수

### Silver 4

어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다. 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다. N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오.

## 입력
첫째 줄에 1,000보다 작거나 같은 자연수 N이 주어진다.

## 출력
첫째 줄에 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력한다.

## 문제풀이
숫자가 두 자리 수 이하라면 무조건 등차수열이므로 무조건 `res += 1`한다. 세 자리 수라면 숫자의 차이를 직접 계산해 등차수열이 맞다면 경우의 수에 더하였다.