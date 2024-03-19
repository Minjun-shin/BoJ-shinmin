# 쉬운 계단 수

### Silver 1

45656이란 수를 보자.

이 수는 인접한 모든 자리의 차이가 1이다. 이런 수를 계단 수라고 한다.

N이 주어질 때, 길이가 N인 계단 수가 총 몇 개 있는지 구해보자. 0으로 시작하는 수는 계단수가 아니다.

## 입력
첫째 줄에 N이 주어진다. N은 1보다 크거나 같고, 100보다 작거나 같은 자연수이다.

## 출력
첫째 줄에 정답을 1,000,000,000으로 나눈 나머지를 출력한다.

## 문제풀이
다이나믹 프로그래밍으로 풀었다. `res`에 i번째 원소는 길이가 i+1인 숫자의 개수를 의미하는데 각 원소의 j번째 수는 끝이 j로 끝나는 숫자의 개수이다. 따라서 다음 수는 0으로 끝나는 수는 전 결과에서 1로 끝나는 수의 개수와 같고 현재 9로 끝나는 수는 전 결과에서 8로 끝나는 수의 개수와 같고 나머지 n자리수 j로 끝나는 수는 n-1자리수 j-1, j+1로 끝나는 수의 개수의 합이 된다. 이를 끝까지 진행한 마지막 결과의 합이 답이 된다.