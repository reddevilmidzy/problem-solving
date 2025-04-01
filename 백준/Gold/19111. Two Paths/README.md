# [Gold II] Two Paths - 19111 

[문제 링크](https://www.acmicpc.net/problem/19111) 

### 성능 요약

메모리: 36680 KB, 시간: 108 ms

### 분류

데이크스트라, 그래프 이론, 최단 경로

### 제출 일자

2025년 4월 1일 11:00:38

### 문제 설명

<p>You are given an undirected graph with $n$ nodes (numbered from $1$ to $n$) and $m$ edges. Each edge has a length. The graph contains neither multiple edges nor self-loops.</p>

<p>Alice and Bob are now trying to play a game. Each player has to pick a path from $1$ to $n$ (not necessary a simple path). The paths have to be different.</p>

<p>Alice always moves first, and she is so clever that she took one of the shortest paths from $1$ to $n$. Now is Bob's turn. Bob wants to pick the shortest possible path from $1$ to $n$ which is different from Alice's path. Your task is to find the length of such path.</p>

<p>Two paths $S$ and $T$ are considered different if and only if they have different number of edges or there is an integer $i$ such that the $i$-th edge of $S$ differs from the $i$-th edge of $T$.</p>

### 입력 

 <p>The first line of input contains two integers: the number of nodes $n$ and the number of edges $m$ ($2 \le n \le 10^5$, $1 \le m \le 10^5$). Each of the next $m$ lines contains three integers $a$, $b$, and $w$ which mean that there is an edge between node $a$ and node $b$, and its length is $w$ ($1 \le a, b \le n$, $1 \le w \le 10^9$). It is guaranteed that there is at least one path from $1$ to $n$.</p>

### 출력 

 <p>Print a single line with a single integer: the length of a valid shortest path for Bob.</p>

