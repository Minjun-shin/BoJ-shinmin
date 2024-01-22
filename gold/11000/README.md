# 강의실 배정

### Gold 5

수강신청의 마스터 김종혜 선생님에게 새로운 과제가 주어졌다. 

김종혜 선생님한테는 Si에 시작해서 Ti에 끝나는 N개의 수업이 주어지는데, 최소의 강의실을 사용해서 모든 수업을 가능하게 해야 한다. 

참고로, 수업이 끝난 직후에 다음 수업을 시작할 수 있다. (즉, Ti ≤ Sj 일 경우 i 수업과 j 수업은 같이 들을 수 있다.)

수강신청 대충한 게 찔리면, 선생님을 도와드리자!

## 입력
첫 번째 줄에 N이 주어진다. (1 ≤ N ≤ 200,000)

이후 N개의 줄에 Si, Ti가 주어진다. (0 ≤ Si < Ti ≤ 109)

## 출력
강의실의 개수를 출력하라.

## 문제풀이
`11000-1.py` - 시간초과 -> `input = sys.stdin.readline` -> 통과  
처음에는 비슷한 회의실 문제가 떠올라 종료된 순으로 정렬하여 풀고자 하였으나 계속해서 틀렸기에 다시 생각해보았다.

틀린 이유로는 강의 시간이 길어서 시작 시간은 빠르나 종료 시간으로 정렬하면 나중으로 배치되는 강의가 무조건 따로 강의실에 배치되는 문제가 있었다.  
따라서 정렬을 시작 시간을 기준으로 하였다.

그리고 다른 문제로는 결과 리스트였다. 결과 리스트는 시작 시간 순으로 들어가는데 그 값은 가의 종료 시간이다. 하지만 필요한 결과는 종료시간 중 가장 빨리 끝나는 시간이다.  
따라서 `heapq`를 사용하여 가장 작은 값을 `pop`할 수 있도록 하였다.

이후에는 시간초과 문제가 발생하였다. 알고리즘 상에는 더이상 줄일 수 없다고 판단하여 `sys.stdin.readline`을 사용하였다. 그 결과 통과할 수 있었다.