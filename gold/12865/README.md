# 평범한 가방

### Gold 5

이 문제는 아주 평범한 배낭에 관한 문제이다.

한 달 후면 국가의 부름을 받게 되는 준서는 여행을 가려고 한다. 세상과의 단절을 슬퍼하며 최대한 즐기기 위한 여행이기 때문에, 가지고 다닐 배낭 또한 최대한 가치 있게 싸려고 한다.

준서가 여행에 필요하다고 생각하는 N개의 물건이 있다. 각 물건은 무게 W와 가치 V를 가지는데, 해당 물건을 배낭에 넣어서 가면 준서가 V만큼 즐길 수 있다. 아직 행군을 해본 적이 없는 준서는 최대 K만큼의 무게만을 넣을 수 있는 배낭만 들고 다닐 수 있다. 준서가 최대한 즐거운 여행을 하기 위해 배낭에 넣을 수 있는 물건들의 가치의 최댓값을 알려주자.

## 입력
첫 줄에 물품의 수 N(1 ≤ N ≤ 100)과 준서가 버틸 수 있는 무게 K(1 ≤ K ≤ 100,000)가 주어진다. 두 번째 줄부터 N개의 줄에 거쳐 각 물건의 무게 W(1 ≤ W ≤ 100,000)와 해당 물건의 가치 V(0 ≤ V ≤ 1,000)가 주어진다.

입력으로 주어지는 모든 수는 정수이다.

## 출력
한 줄에 배낭에 넣을 수 있는 물건들의 가치합의 최댓값을 출력한다.

## 문제풀이
다이나믹 프로그래밍의 대표적인 냅색(knapsack) 알고리즘 문제이다. 먼저 K+1 길이의 리스트를 만들었다. 인덱스가 i인 값은 무게가 i인 가방에 넣을 수 있는 가치의 최대값이다. 이를 계산하기 위해 무게가 w이고 가치가 v인 물건을 고려할 때 뒤에서부터 순서대로 w만큼 가벼운 가방의 결과값에서 v만큼의 가치를 더한 값과 기존에 저장한 값 중 최대값을 가져왔다. 이를 모든 물건에 대해서 반복하면 모든 무게에서 가차값의 최대치를 알 수 있다. 이 중에 최대값을 출력하여 답을 도출하였다.