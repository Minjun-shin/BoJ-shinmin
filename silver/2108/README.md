# 통계학

### Silver 3

수를 처리하는 것은 통계학에서 상당히 중요한 일이다. 통계학에서 N개의 수를 대표하는 기본 통계값에는 다음과 같은 것들이 있다. 단, N은 홀수라고 가정하자.

- 산술평균 : N개의 수들의 합을 N으로 나눈 값
- 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
- 최빈값 : N개의 수들 중 가장 많이 나타나는 값
- 범위 : N개의 수들 중 최댓값과 최솟값의 차이

N개의 수가 주어졌을 때, 네 가지 기본 통계값을 구하는 프로그램을 작성하시오.

## 입력
첫째 줄에 수의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 단, N은 홀수이다. 그 다음 N개의 줄에는 정수들이 주어진다. 입력되는 정수의 절댓값은 4,000을 넘지 않는다.

## 출력
첫째 줄에는 산술평균을 출력한다. 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.

둘째 줄에는 중앙값을 출력한다.

셋째 줄에는 최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.

넷째 줄에는 범위를 출력한다.

## 문제풀이
- 산술평균 : `sum`과 `len`으로 구하고 `round`로 반올림
- 중앙값 : num_list를 정렬 후 `len(num_list) // 2` 인덱스에 해당하는 값 출력
- 최빈값 : 숫자의 개수를 value로 하는 `num_dict`를 구한 후 가장 큰 value를 가지는 숫자들을 리스트에 저장, 2개 이상인 경우에 두 번째 수 출력 아니면 첫 번째 수 출력
- 범위 : 정렬된 리스트의 마지막 수와 첫 번째 수의 차 출력