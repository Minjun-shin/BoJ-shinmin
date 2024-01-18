# Compositions

### Gold 5

A composition of an integer n is an ordered set of integers which sum to n. Two compositions with the same elements but in different orders are considered different (this distinguishes compositions from partitions). For example, all the compositions of the first few integers are:

```
1: {1}
2: {1+1, 2}
3: {1+1+1, 1+2, 2+1, 3}
4: {1+1+1+1, 1+1+2, 1+2+1, 1+3, 2+1+1, 2+2, 3+1, 4}
```

Note that 1+2 and 2+1 each count as distinct compositions of 3. As you may have suspected, there are 2(n-1) compositions of n.

In this problem, we set conditions on the elements of the compositions of n. A composition misses a set S if no element of the composition is in the set S. For example, the compositions of the first few integers which miss the set of even integers are:

```
1: {1}
2: {1+1}
3: {1+1+1, 3}
4: {1+1+1+1, 1+3, 3+1}
```

No odd integer can have a composition missing the set of odd integers and any composition of an even integer consisting of only even integers must be 2 times a composition of n/2.

For this problem you will write a program to compute the number of compositions of an input integer n which miss the elements of the arithmetic sequence {m + i*k | i = 0,1,…}

## Input
The first line of input contains a single decimal integer P, (1 ≤ P ≤ 10000), which is the number of data sets that follow. Each data set should be processed identically and independently.

Each data set consists of a single line of input. It contains the data set number, K, followed by the three space separated integers n, m and k with (1 ≤ n ≤ 30) and (0 ≤ m < k < 30).

## Output
For each data set there is one line of output. The single output line consists of the data set number, K, followed by a single space followed by the number of compositions of n which miss the specified sequence.

## Solution
숫자 n을 n이하의 수의 합으로 나타내는 경우의 수를 묻는 문제이다.  
특정한 조건이 없으면 이 문제는 n 미만의 수의 경우의 수를 모두 다 합하면 된다.  
왜냐하면 `n`은 `n-1`+1이므로 `n-1`의 경우에 `+1`을 붙이면 되고 그 이전 수는 `n-2`+2...`n-i`+i...이므로 전부 더하면 된다.  
하지만 이 문제는 특수한 조건이 있다. m으로 시작하고 공차가 k인 등차수열이 포함되지 않는 경우만 포함되야 한다.  
따라서 이를 위해 n과의 차가 이에 속하지 않는 경우의 수만 더하면 된다.  
이러한 과정을 2부터 시작하여 n까지 반복하여 마지막 수를 출력하였다.