# N-Queen

### Gold 4

N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.

N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.

## 입력
첫째 줄에 N이 주어진다. (1 ≤ N < 15)

## 출력
첫째 줄에 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력한다.

## 문제풀이
재귀함수를 사용하여 해결했다. 맨 윗 줄부터 내려가며 몇 번째 칸에 놓을지 계산하며 진행했다. `ch[i]`은 i번째 줄에서 몇 번째 칸에 놓았는지를 나타내고 `ch_D1`과 `ch_D2`는 대각선을 계산하기 위해 설정한 리스트이다. 행과 열의 인덱스 합 `n+i`의 값을 이용해 `ch_D1`의 값을, 행과 열의 인덱스 차 `n-i`의 값을 이용해 `ch_D2`의 값을 조정하며 가능한 경우에 진행하도록 하였고 마지막 줄까지 도달하면 결과값을 +1하게 하였다.