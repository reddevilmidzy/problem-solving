# [Platinum II] John - 3754 

[문제 링크](https://www.acmicpc.net/problem/3754) 

### 성능 요약

메모리: 13208 KB, 시간: 0 ms

### 분류

게임 이론, 스프라그–그런디 정리

### 제출 일자

2025년 1월 28일 18:18:07

### 문제 설명

<p>Little John is playing very funny game with his younger brother. There is one big box filled with M&Ms of different colors. At first John has to eat several M&Ms of the same color. Then his opponent has to make a turn. And so on. Please note that each player has to eat at least one M&M during his turn. If John (or his brother) will eat the last M&M from the box he will be considered as a looser and he will have to buy a new candy box.</p>

<p>Both of players are using optimal game strategy. John starts first always. You will be given information about M&Ms and your task is to determine a winner of such a beautiful game. </p>

### 입력 

 <p>The first line of input will contain a single integer T – the number of test cases. Next T pairs of lines will describe tests in a following format. The first line of each test will contain an integer N – the amount of different M&M colors in a box. Next line will contain N integers A<sub>i</sub>, separated by spaces – amount of M&Ms of i-th color. </p>

<ul>
	<li>1 <= T <= 474,</li>
	<li>1 <= N <= 47,</li>
	<li>1 <= A<sub>i</sub> <= 4747 </li>
</ul>

### 출력 

 <p>Output T lines each of them containing information about game winner. Print “John” if John will win the game or “Brother” in other case. </p>

