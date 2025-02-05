# [Silver I] MazeMan - 27388 

[문제 링크](https://www.acmicpc.net/problem/27388) 

### 성능 요약

메모리: 35136 KB, 시간: 64 ms

### 분류

너비 우선 탐색, 깊이 우선 탐색, 그래프 이론, 그래프 탐색

### 제출 일자

2025년 2월 5일 21:21:59

### 문제 설명

<p>You now work for a video game company - every programmer's dream! You are working on a multiplayer game where players cooperate to enter a maze and try to consume all of the "dots" as quickly as possible. Each player enters the maze at a different entrance. The mazes are randomly generated, so the minimum number of players needed to consume all of the dots can vary, and some dots may not be reachable at all.</p>

<p>You are working in the Quality Control department, analyzing the randomly generated mazes. For analysis, the mazes are represented in text. An <code>X</code> is a wall that cannot be crossed. Letters <code>A</code>-<code>W</code> are entrances. Players can only move up, down, left and right. Players can move though spaces and dots; moving over a dot eats it. If two doors are adjacent, players cannot move from one to the other. For example:</p>

<pre style="text-align: center;">XXXXXXXAXXXXXXXBXXXX
X.. ..X.X...... ...X
X.XXX...X.X.XXXXXX.X
X.X.XXXXX.X.X....X.X
X.X... ...X.X.XX.X.X
X.X.X.XXXXXXX.XX.X.X
X.X.X.X...X...X....X
X.X.X.XXXXXXX.XXXX.X
X...X.X X.. ..X..X.X
XXXXXXXDXXXXXXXXCXXX</pre>

<p>All of the reachable dots can be reached from entrances <code>A</code> and <code>C</code> (or, equivalently, <code>B</code> and <code>C</code>). There are three dots that cannot be reached.</p>

<p>Calculate the minimum number of players necessary to eat all the reachable dots, and how many dots are not reachable because they are walled off.</p>

### 입력 

 <p>This first line of input contains two integers $n$ and $m$ ($3 \le n,m \le 100$), where $n$ is the number of rows in the maze representation, and $m$ is the number of columns.</p>

<p>Each of the next $n$ lines contains a string of length exactly $m$, consisting only of the capital letters <code>A</code> through <code>X</code>, space, or period. This is the maze. The borders of the maze (rows $1$ and $n$, columns $1$ and $m$) are guaranteed to consist only of capital letters <code>A</code> through <code>X</code>. There are no entrances (<code>A</code>-<code>W</code>) in the middle of the maze.</p>

### 출력 

 <p>Output a line with two space-separated integers, the first of which is the minimum number of entrances necessary to enter in order to eat all of the dots (which may be $0$ if no dots are reachable), and the second of which is the number of dots which cannot be reached.</p>

