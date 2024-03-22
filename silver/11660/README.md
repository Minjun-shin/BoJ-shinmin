# 구간 합 구하기 5

### Silver 1

N×N개의 수가 N×N 크기의 표에 채워져 있다. (x1, y1)부터 (x2, y2)까지 합을 구하는 프로그램을 작성하시오. (x, y)는 x행 y열을 의미한다.

예를 들어, N = 4이고, 표가 아래와 같이 채워져 있는 경우를 살펴보자.

<table style="line-height:20.8px; width:158px; border: 1px solid black;">
	<tbody>
		<tr>
			<td style="text-align:center; border: 1px solid black;">1</td>
			<td style="text-align:center; border: 1px solid black;">2</td>
			<td style="text-align:center; border: 1px solid black;">3</td>
			<td style="text-align:center; border: 1px solid black;">4</td>
		</tr>
		<tr>
			<td style="text-align:center; border: 1px solid black;">2</td>
			<td style="text-align:center; border: 1px solid black;">3</td>
			<td style="text-align:center; border: 1px solid black;">4</td>
			<td style="text-align:center; border: 1px solid black;">5</td>
		</tr>
		<tr>
			<td style="text-align:center; border: 1px solid black;">3</td>
			<td style="text-align:center; border: 1px solid black;">4</td>
			<td style="text-align:center; border: 1px solid black;">5</td>
			<td style="text-align:center; border: 1px solid black;">6</td>
		</tr>
		<tr>
			<td style="text-align:center; border: 1px solid black;">4</td>
			<td style="text-align:center; border: 1px solid black;">5</td>
			<td style="text-align:center; border: 1px solid black;">6</td>
			<td style="text-align:center; border: 1px solid black;">7</td>
		</tr>
	</tbody>
</table>

여기서 (2, 2)부터 (3, 4)까지 합을 구하면 3+4+5+4+5+6 = 27이고, (4, 4)부터 (4, 4)까지 합을 구하면 7이다.

표에 채워져 있는 수와 합을 구하는 연산이 주어졌을 때, 이를 처리하는 프로그램을 작성하시오.

## 입력
첫째 줄에 표의 크기 N과 합을 구해야 하는 횟수 M이 주어진다. (1 ≤ N ≤ 1024, 1 ≤ M ≤ 100,000) 둘째 줄부터 N개의 줄에는 표에 채워져 있는 수가 1행부터 차례대로 주어진다. 다음 M개의 줄에는 네 개의 정수 x1, y1, x2, y2 가 주어지며, (x1, y1)부터 (x2, y2)의 합을 구해 출력해야 한다. 표에 채워져 있는 수는 1,000보다 작거나 같은 자연수이다. (x1 ≤ x2, y1 ≤ y2)

## 출력
총 M줄에 걸쳐 (x1, y1)부터 (x2, y2)까지 합을 구해 출력한다.

## 문제풀이
다이나믹 프로그래밍으로 문제를 해결했다. 이차원 배열 속 숫자들을 (1, 1)에서 해당 칸까지 모든 숫자의 함으로 바꾸고 (x1, y1)부터 (x2, y2)의 합을 구할 때는 (x2, y2)칸의 값에서 (x2, y1-1), (x1-1, y2)칸의 값들을 빼고 (x1-1, y1-1)칸의 값을 더해서 구했다.