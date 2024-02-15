# 부분수열의 합

### Silver 2

N개의 정수로 이루어진 수열이 있을 때, 크기가 양수인 부분수열 중에서 그 수열의 원소를 다 더한 값이 S가 되는 경우의 수를 구하는 프로그램을 작성하시오.

## 입력
첫째 줄에 정수의 개수를 나타내는 N과 정수 S가 주어진다. (1 ≤ N ≤ 20, |S| ≤ 1,000,000) 둘째 줄에 N개의 정수가 빈 칸을 사이에 두고 주어진다. 주어지는 정수의 절댓값은 100,000을 넘지 않는다.

## 출력
첫째 줄에 합이 S가 되는 부분수열의 개수를 출력한다.

## 문제풀이
DFS로 모든 부분집합을 계산하여 풀었다. DFS의 `n`은 n번째 정수를 확인한다는 뜻이고 `result`는 부분집합을 저장하기 위한 변수이다.

재귀는 n을 1씩 증가시키며 하는데 부분집합에 `num_list[n]`을 포함시키는 경우와 안 포함시키는 경우 두 가지가 실행되게 하였다. 그리고 마지막 정수까지 확인한 후 공집합이 아니고 합계가 원하는 정수인 경우에 `res += 1`이 실행되게하여 결과값을 도출하였다.