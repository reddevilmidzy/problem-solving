# [Platinum III] Game of Stones - 5227 

[문제 링크](https://www.acmicpc.net/problem/5227) 

### 성능 요약

메모리: 13888 KB, 시간: 8 ms

### 분류

방향 비순환 그래프, 깊이 우선 탐색, 다이나믹 프로그래밍, 게임 이론, 그래프 이론, 그래프 탐색, 스프라그–그런디 정리, 위상 정렬

### 제출 일자

2025년 2월 23일 16:27:32

### 문제 설명

<p>Captain America has just caught up with the supervillain Loki to retrieve the Cosmic Cube, and they are about to begin one of their epic battles. Loki is however tired of getting his butt kicked, and instead challenges Captain America to a battle of wits. Captain America is confident in his abilities (more precisely his trusty sidekick’s, i.e., your, abilities) and accepts the challenge.</p>

<p>Loki then explains the game. He begins by drawing an acyclic directed graph (as shown in the figure), and places a number of stones on each of the nodes. The two players take turns moving a stone from any node to one of its neighbors, following a directed edge. So the stone on node 0 (in either of the examples below) can be moved to node 1, but a stone could not be moved from node 1 to node 0. Multiple stones may be at the same node at any time. The player that cannot move any stone loses the game, and the Cosmic Cube. Let a <em>sink node</em> be a node that has no outgoing edges. As long as at least one stone is at a non-sink node, a move can be made. Hence, the goal is to be the person who moves the last such stone from a non-sink node to a sink-node.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/e2abd099-f6d2-4dbe-a9d2-9e33531801ab/-/preview/" style="width: 768px; height: 323px;"></p>

<p style="text-align: center;">Figure 2: (1) In the first case, the moves are forced (there is no choice) and player 1 wins; (2) In the second case, no matter what Player 1 does in the first move, Player 2 can win.</p>

<p>Loki doesn’t think you or Captain America are a match for him, and offers you the choice of moving first or second. You have to figure out what is the right choice.</p>

### 입력 

 <p>The input consists of a number of test cases. Each test case begins with a line containing two integers n and m, the number of nodes and the number of edges respectively (1 ≤ n ≤ 1000, 0 ≤ m ≤ 10000). Then, the next line contais the m edges, each edge given by two integers a and b: the starting and ending node of the edge (nodes are labeled from 0 to n − 1). The test case is terminated by n more integers s<sub>0</sub>, · · · , s<sub>n−1</sub> on the next line, where s<sub>i</sub> represents the number of stones that are initially placed on node i (0 ≤ s<sub>i</sub> ≤ 1000). Input is terminated by a line containing ’0 0’ which should not be processed.</p>

### 출력 

 <p>For each test case output a single line with either the word “First” if the first player will win, or the word “Second” if the second player will win (assuming optimal play by both sides).</p>

