# 세부

### Gold 4

빼빼로 데이를 맞아 혜빈이와 숭이는 세부에 있는 섬에 놀러 갔다. 섬은 바다 위에 떠다니는 집과 집들을 연결하는 오크나무로 되어있는 다리로 이뤄져 있다. 숭이는 혜빈이에게 깜짝 이벤트를 해주기 위해 섬 관리자에게 혜빈이를 이벤트장소에 머물게 해달라고 하였다. 이벤트 당일 날 숭이는 금으로 된 빼빼로들을 들고 이벤트 장소로 이동하려 했다. 하지만 아뿔싸! 각 다리마다 다리 위를 지날 수 있는 무게 제한이 존재했다. 비싼 금빼빼로를 가면서 버리기 아깝던 숭이는 자신이 머물던 집에서 자신이 혜빈이에게 갈 수 있는 최대한의 금빼빼로만을 들고 가려고 한다. 따라서 숭이는 인공위성조차 해킹할 수 있는 당신에게 혜빈이에게 들고 갈 수 있는 최대한의 금빼빼로 개수를 알려달라고 부탁했다. 당신은 인공위성을 해킹하여 집들의 번호와 다리의 무게제한을 알아내었다. 이 정보를 가지고 빨리 숭이를 도와주자.

(금빼빼로 하나의 무게는 1이고, 숭이의 몸무게는 고려하지 않는다.)

## 입력
첫 번째 줄에는 섬에 존재하는 집의 수 N(2≤N≤100,000)와 다리의 수 M(1≤M≤300,000)이 주어진다. 두 번째 줄에는 숭이의 출발 위치(s)와 혜빈이의 위치(e)가 주어진다. (1≤s, e≤N, s≠e). 다음 M개의 줄에는 다리의 정보가 주어진다. 각 줄은 “집의 번호 h1(1≤h1≤N), 집의 번호 h2(1≤h2≤N), 다리의 무게제한 k(1≤k≤1,000,000)” 형식으로 주어진다. (h1집과 h2집은 무게제한이 k인 다리로 연결되어 있다.)

## 출력
숭이의 출발위치에서 혜빈이의 위치까지 숭이가 들고 갈 수 있는 금빼빼로의 최대 개수를 출력하시오.

## 문제풀이
최소 스패닝 트리 알고리즘(Prim)으로 문제를 해결했다.

두 지점을 잇는 경로 중에서 간선들의 가중치 중 가장 작은 값이 가장 큰 경로를 구하는 문제이다. 따라서 prim 알고리즘에서 최소 힙 대신 최대 힙을 사용하고 가중치의 합이 아닌 단일 값을 계산하면 된다. 최대 힙을 사용하기 위해 가중치를 음수로 저장했다. 그리고 알고리즘을 진행하다가 목적지를 방문하게 되면 반복문을 끝내게 하였다.

만약 목적지에 도달할 수 없는 경우에는 0을 출력하게 했다.