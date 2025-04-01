# [Gold IV] Jug Hard - 11311 

[문제 링크](https://www.acmicpc.net/problem/11311) 

### 성능 요약

메모리: 15776 KB, 시간: 24 ms

### 분류

유클리드 호제법, 수학, 정수론

### 제출 일자

2025년 4월 1일 14:14:00

### 문제 설명

<p>You have two empty jugs and tap that may be used to fill a jug. When filling a jug from the tap, you can only fill it completely (i.e., you cannot partially fill it to a desired level, since there are no volume measurements on the jug).</p>

<p>You may empty either jug at any point.</p>

<p>You may transfer water between the jugs: if transferring water from a larger jug to a smaller jug, the smaller jug will be full and there will be water left behind in the larger jug.</p>

<p>Given the volumes of the two jugs, is it possible to have one jug with some specific volume of water?</p>

### 입력 

 <p>The first line contains T, the number of test cases (1 ≤ T 100 000). Each test case is composed of three integers: a b d where a and b (1 ≤ a, b ≤ 10 000 000) are the volumes of the two jugs, and d is the desired volume of water to be generated. You can assume that d ≤ max(a,b).</p>

### 출력 

 <p>For each of the T test cases, output either Yes or No, depending on whether the specific volume of water can be placed in one of the two jugs.</p>

