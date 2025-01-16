# [Platinum III] Split Game - 16340 

[문제 링크](https://www.acmicpc.net/problem/16340) 

### 성능 요약

메모리: 13216 KB, 시간: 52 ms

### 분류

다이나믹 프로그래밍, 게임 이론, 스프라그–그런디 정리

### 제출 일자

2025년 1월 16일 19:02:56

### 문제 설명

<p>For a long time, rich clientele of Binary Casino has been requesting a new way to gamble their money. To fulfill their wishes, the director of Binary Casino decided to introduce a new game called Split Your Tokens.</p>

<p>This game is played only when a customer is about to exit the casino. Instead of exchanging tokens won during his visit, he may take up casino’s challenge and bet all of his earned tokens on winning this game. Should the customer lose, all of his tokens are lost in favor of the casino.</p>

<p>When the game starts, the customer splits his tokens into N piles with not necessarily same amount of tokens in each pile. The customer and the casino then exchange turns – in this game we denote the customer as the first player and the casino as the second player. Each player in his turn decides which pile he wants to split and chooses a positive integer K which is smaller than the size of the selected pile. Then the player splits the selected pile into as many piles of size K as possible. If any tokens remain, they form another pile on their own. A player loses the game when he can not do any more splitting. The customer (first player) always plays first.</p>

<p>The director of Binary Casino is however not sure, whether this game will be profitable for the casino in the long term. Your task is thus to determine, for a given configuration of piles, which player wins when both players play optimally.</p>

### 입력 

 <p>The first line contains one integer N(1 ≤ N ≤ 2000), the number of piles. The second line contains a sequence of N integers P<sub>i</sub> (1 ≤ P<sub>i</sub> ≤ 2000), P<sub>i</sub> represents the number of tokens in the i-th pile.</p>

### 출력 

 <p>Output a single line with either “<code>First</code>” or “<code>Second</code>”, depending on which player wins the game if both play optimally</p>

