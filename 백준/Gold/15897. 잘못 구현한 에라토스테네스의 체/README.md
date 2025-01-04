# [Gold II] 잘못 구현한 에라토스테네스의 체 - 15897 

[문제 링크](https://www.acmicpc.net/problem/15897) 

### 성능 요약

메모리: 16332 KB, 시간: 4 ms

### 분류

수학, 정수론

### 제출 일자

2025년 1월 4일 18:27:14

### 문제 설명

<p>성원이는 오늘 이산수학 수업 시간에 에라토스테네스의 체에 대해 배웠다. 에라토스테네스의 체는 고대 그리스 수학자 에라토스테네스가 발견한 소수를 찾는 방법이다. 성원이는 이 방법에 너무나 큰 감명을 받았고, 당장 실습실에 가서 C++로 구현해보기로 했다. 그런데 성원이는 교재도 없고 필기를 하는 성격도 아니기 때문에 수업내용이 정확히 기억나지 않았다. 성원이는 기억을 열심히 더듬어 마침내 아래와 같은 코드를 작성했다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/e3f61892-1308-4a56-b3f7-eafe8fc94403/-/preview/" style="width: 340px; height: 135px;"></p>

<p>옆에 앉아있던 킹갓제너럴엠페러충무공마제스티알고리즘마스터 형석이는 성원이의 이 코드를 보고 실소를 금할 수 없었다. 아니 대체 세상에 어떤 사람이 이딴 코드를 짠단 말이지? 형석이는 신이 나서 성원이에게 이 코드의 문제점을 마구 지적했다.</p>

<blockquote>
<p>형석 : 야 성원! 이거 알고리즘이 완전히 틀렸잖아! 여긴 이렇게저렇게 고쳐야지!<br>
성원 : 아 그렇구나... 알려줘서 정말 고마워.<br>
형석 : 게다가 이 코드는 수행시간도 더럽게 오래 걸리겠네.<br>
성원 : 그래? 내가 관심법으로 보면 왠지 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D442 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c28"></mjx-c></mjx-mo><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c29"></mjx-c></mjx-mo></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>O</mi><mo stretchy="false">(</mo><mi>n</mi><mo stretchy="false">)</mo></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$O(n)$</span></mjx-container>에 돌아갈 것처럼 생겼는데?<br>
형석 : <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D442 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c28"></mjx-c></mjx-mo><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c29"></mjx-c></mjx-mo></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>O</mi><mo stretchy="false">(</mo><mi>n</mi><mo stretchy="false">)</mo></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$O(n)$</span></mjx-container>은 무슨 말도 안되는 소리야? 자 이거 봐. 수식을 이렇게저렇게 쓰면...<br>
형석 : 어라? 시간복잡도 증명이 잘 안 되네. 수학 공부를 너무 오랫동안 안 해서 그런가?<br>
성원 : IOI 금메달 킹갓제너럴알고리즘마스터도 이럴 때가 있구나.<br>
형석 : 시끄러! 그렇다면 내가 직접 연산횟수를 측정해서 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D442 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c28"></mjx-c></mjx-mo><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c29"></mjx-c></mjx-mo></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>O</mi><mo stretchy="false">(</mo><mi>n</mi><mo stretchy="false">)</mo></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$O(n)$</span></mjx-container>이 아님을 보여주지.</p>
</blockquote>

<p>형석이는 위 코드의 연산횟수를 직접 측정해서 위 코드의 시간복잡도가 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D442 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c28"></mjx-c></mjx-mo><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c29"></mjx-c></mjx-mo></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>O</mi><mo stretchy="false">(</mo><mi>n</mi><mo stretchy="false">)</mo></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$O(n)$</span></mjx-container>이 아님을 증명하려고 한다. 구체적으로 위 코드의 6번 줄이 몇 번 실행될지를 측정하고 그 데이터로 그래프를 그려 보여주려고 한다. 그런데 막상 직접 측정하려고 보니 이것은 매우 귀찮은 일이었다. 허접인 성원이때문에 내가 이 고생을 해야 한다니! 귀찮아진 형석이는 이 작업을 당신에게 떠넘겼다. 위 코드에서 n에 해당하는 값이 주어졌을 때, 위 코드의 6번 줄이 몇 번 실행될지를 계산하는 프로그램을 작성해서 형석이를 도와주자.</p>

### 입력 

 <p>첫 번째 줄에 위 프로그램의 입력 n의 값이 자연수로 주어진다. (1 ≤ n ≤ 10<sup>9</sup>)</p>

### 출력 

 <p>첫 번째 줄에 위 프로그램의 6번 줄의 실행횟수를 출력한다.</p>

