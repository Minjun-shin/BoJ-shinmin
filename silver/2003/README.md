# 수들의 합 2

### Silver 4

N개의 수로 된 수열 A[1], A[2], …, A[N] 이 있다. 이 수열의 i번째 수부터 j번째 수까지의 합 A[i] + A[i+1] + … + A[j-1] + A[j]가 M이 되는 경우의 수를 구하는 프로그램을 작성하시오.

## 입력
첫째 줄에 N(1 ≤ N ≤ 10,000), M(1 ≤ M ≤ 300,000,000)이 주어진다. 다음 줄에는 A[1], A[2], …, A[N]이 공백으로 분리되어 주어진다. 각각의 A[x]는 30,000을 넘지 않는 자연수이다.

## 출력
첫째 줄에 경우의 수를 출력한다.

## 문제풀이
투 포인터 방식으로 풀었다. `s`와 `e`라는 변수를 두고 `s`부터 `e-1`까지의 수를 더한 값을 `total`에 저장했다. 그리고 `total`값이 원하는 수랑 비교해서 크거나 작으면 `s`와 `e`를 +1 해가며 조정하다가 같은 경우가 나올 경우에만 결과값에 추가했다. 이를 반복문으로 구현하고 종료 조건을 `e`가 끝에 도달했을 때로 하였다.