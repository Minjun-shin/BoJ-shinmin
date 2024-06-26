# A → B

### Silver 2

정수 A를 B로 바꾸려고 한다. 가능한 연산은 다음과 같은 두 가지이다.

- 2를 곱한다.
- 1을 수의 가장 오른쪽에 추가한다. 

A를 B로 바꾸는데 필요한 연산의 최솟값을 구해보자.

## 입력
첫째 줄에 A, B (1 ≤ A < B ≤ 10<sup>9</sup>)가 주어진다.

## 출력
A를 B로 바꾸는데 필요한 연산의 최솟값에 1을 더한 값을 출력한다. 만들 수 없는 경우에는 -1을 출력한다.

## 문제풀이
A에서 B로 진행하는 것보다 B에서 A로 진행하는 것이 더 쉽다.

A == B일 때까지 진행했는데 만약 2로 나누어지는 수이면 2로 나누었고, 그렇지 않은데 1로 끝나면 끝에 있는 1을 버리는 연산을 하였다. 만약 1의 자리수가 1이 아닌 홀수이면 -1을 반환하였다. 그리고 연산을 계속하다 A보다 작아지게 되도 -1을 반환하였다. 만일 모든 연산이 정상적으로 끝나면 연산 횟수 +1을 반환하였다.