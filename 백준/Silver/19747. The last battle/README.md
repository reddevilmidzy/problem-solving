# [Silver II] The last battle - 19747 

[문제 링크](https://www.acmicpc.net/problem/19747) 

### 성능 요약

메모리: 17984 KB, 시간: 20 ms

### 분류

애드 혹, 구현, 수학

### 제출 일자

2024년 12월 14일 23:35:51

### 문제 설명

<p>Soon there will be a final battle between people and Martians. Spies of people found out that the Martians had $n$ soldiers left. It also turned out that people as well as the Martians had exactly $n$ fighters. </p>

<p>According to the experience of past battles, people know that only one Martian with the number $i$ can defeat an $i$-th person.</p>

<p>The commander decided to build in a line of people. Learning Martians plans, the commander found out that a man with $i$-th position in the line will fight with Martian number $a_i$. People will win only if each of the fighters is guaranteed to win in their battle.</p>

<p>Firstly commander put the $i$-th person on the $i$-th position int the line. After that, he realized that he had little time before the battle, and that people can lose if the line is not rebuilt. In one second he can move a person from the last place to the beginning of the line, after this operation this fighter is in the first position, and the position number of each of the other fighters is increased by $1$. </p>

<p>Help him to find out the minimal time he can rebuild the line so that people will win.</p>

### 입력 

 <p>The first line contains an integer $n$ --- the number of fighters of each side ($1 \le n \le 2\cdot10^5$).</p>

<p>The second line contains $n$ distinct integers $a_1, a_2, \ldots, a_n$, where $a_i$ is the number of the Martian with whom the person from the $i$-th position in the line will fight ($1 \le a_i \le n$, if $i \ne j$, then $a_i \ne a_j$).</p>

### 출력 

 <p>Output a single number $k$ --- the minimum number of seconds for which the commander can rebuild the line so that people will win. If people can not defeat the Martians, print the number <<$-1$>>.</p>

