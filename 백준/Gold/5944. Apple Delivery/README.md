# [Gold IV] Apple Delivery - 5944 

[문제 링크](https://www.acmicpc.net/problem/5944) 

### 성능 요약

메모리: 142340 KB, 시간: 768 ms

### 분류

다익스트라(dijkstra), 그래프 이론(graphs)

### 문제 설명

<p>Bessie has two crisp red apples to deliver to two of her friends in the herd. Of course, she travels the C (1 <= C <= 200,000) cowpaths which are arranged as the usual graph which connects P (1 <= P <= 100,000) pastures conveniently numbered from 1..P: no cowpath leads from a pasture to itself, cowpaths are bidirectional, each cowpath has an associated distance, and, best of all, it is always possible to get from any pasture to any other pasture. Each cowpath connects two differing pastures P1_i (1 <= P1_i <= P) and P2_i (1 <= P2_i <= P) with a distance between them of D_i. The sum of all the distances D_i does not exceed 2,000,000,000.</p>

<p>What is the minimum total distance Bessie must travel to deliver both apples by starting at pasture PB (1 <= PB <= P) and visiting pastures PA1 (1 <= PA1 <= P) and PA2 (1 <= PA2 <= P) in any order. All three of these pastures are distinct, of course.</p>

<p>Consider this map of bracketed pasture numbers and cowpaths with distances:</p>

<pre>                3        2       2
           [1]-----[2]------[3]-----[4]
             \     / \              /
             7\   /4  \3           /2
               \ /     \          /
               [5]-----[6]------[7]
                    1       2
</pre>

<p>If Bessie starts at pasture [5] and delivers apples to pastures [1] and [4], her best path is:</p>

<p>5 -> 6-> 7 -> 4* -> 3 -> 2 -> 1*</p>

<p>with a total distance of 12.</p>

### 입력 

 <p>Line 1: Line 1 contains five space-separated integers: C, P, PB, PA1, and PA2</p>

<p>Lines 2..C+1: Line i+1 describes cowpath i by naming two pastures it connects and the distance between them: P1_i, P2_i, D_i</p>

### 출력 

 <p>Line 1: The shortest distance Bessie must travel to deliver both apples</p>

