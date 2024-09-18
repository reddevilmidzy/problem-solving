# [Gold III] Super Shy (Easy) - 32250 

[문제 링크](https://www.acmicpc.net/problem/32250) 

### 성능 요약

메모리: 417804 KB, 시간: 676 ms

### 분류

다이나믹 프로그래밍

### 제출 일자

2024년 9월 19일 00:10:29

### 문제 설명

<p>일렬로 배치된 빈 좌석 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>개가 있고, 사람들이 한 명씩 차례대로 앉으려고 한다.</p>

<p>사람들은 부끄러움을 많이 타기 때문에 현재 앉아 있는 사람과 최대한 멀리 떨어져 앉으려고 한다. 구체적으로, 앉을 수 있는 좌석은 아래 규칙을 따른다.</p>

<ul>
	<li>만약 먼저 앉은 사람이 아무도 없을 경우 아무 자리에나 앉을 수 있다.</li>
	<li>만약 먼저 앉은 사람이 있고 바로 옆 자리에 사람이 없는 좌석이 있다면, 그러한 좌석들 중 가장 가까운 사람과의 거리가 가장 먼 자리들 중 한 곳에 앉을 수 있다.</li>
	<li>만약 먼저 앉은 사람이 있고 바로 옆 자리에 사람이 없는 좌석이 없다면, 더 이상 앉을 수 없다.</li>
</ul>

<p>이 사람들은 부끄러움이 많기는 하지만 동시에 공익을 추구하는 착한 사람들이기 때문에, 이러한 조건을 만족하는 자리들 중에서 결과적으로 최대한 많은 사람이 앉을 수 있는 자리를 선택할 것이다.</p>

<p>좌석의 수 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>이 주어질 때 앉을 수 있는 최대 사람 수를 구하여라.</p>

### 입력 

 <p>첫째 줄에 좌석의 수 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>이 주어진다. (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c33"></mjx-c></mjx-mn><mjx-mstyle><mjx-mspace style="width: 0.167em;"></mjx-mspace></mjx-mstyle><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mstyle><mjx-mspace style="width: 0.167em;"></mjx-mspace></mjx-mstyle><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>N</mi><mo>≤</mo><mn>3</mn><mstyle scriptlevel="0"><mspace width="0.167em"></mspace></mstyle><mn>000</mn><mstyle scriptlevel="0"><mspace width="0.167em"></mspace></mstyle><mn>000</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1\leq N\leq 3\, 000\, 000$</span></mjx-container>)</p>

### 출력 

 <p>첫째 줄에 자리에 앉을 수 있는 최대 사람 수를 출력한다.</p>

