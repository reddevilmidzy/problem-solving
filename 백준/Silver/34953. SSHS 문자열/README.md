# [Silver V] SSHS 문자열 - 34953 

[문제 링크](https://www.acmicpc.net/problem/34953) 

### 성능 요약

메모리: 15648 KB, 시간: 4 ms

### 분류

그리디 알고리즘, 문자열, 해 구성하기

### 제출 일자

2026년 3월 17일 16:23:48

### 문제 설명

<p>서울과학고에서 SciOI 2025를 기념해 학교의 약자인 SSHS를 활용한 현수막을 만들기로 했다. 그러나 현수막에 사용할 문자 <code><span style="color:#e74c3c;">S</span></code>와 <code><span style="color:#e74c3c;">H</span></code>는 180도 회전해도 같은 모양으로 보여 현수막이 거꾸로 걸릴 수 있다. 이를 방지하기 위해 SciOI 운영진들은 어떤 방향으로 보더라도 SSHS가 많이 보이도록 하는 SSHS 문자열을 사용하기로 했다.</p>

<p>이때 SSHS 문자열은 아래 조건을 만족하는 길이 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>의 문자열 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D434 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$A$</span></mjx-container>이다.</p>

<ul>
<li><span style="color:#e74c3c;"><code>S</code></span>와 <span style="color:#e74c3c;"><code>H</code></span>로만 이루어져 있다.</li>
<li><mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"> <mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D434 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$A$</span></mjx-container>의 부분 문자열 중 <span style="color:#e74c3c;"><code>SSHS</code></span>의 개수와 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D434 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$A$</span></mjx-container>를 뒤집은 문자열의 부분 문자열 중 <span style="color:#e74c3c;"><code>SSHS</code></span>의 개수의 합이 길이 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>인 모든 문자열 중 최대이다.</li>
</ul>

<p>SSHS 문자열의 길이 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>이 주어질 때 가능한 SSHS 문자열 하나를 구하여라.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/355017c3-3900-4c57-a842-58086f737df5/-/preview/" style="height: 220px; width: 600px;"></p>

<p style="text-align: center;"><small>이미지의 예시는 설명을 돕기 위한 것이며, SSHS 문자열이 아니다.</small></p>

### 입력 

 <p>첫째 줄에 SSHS 문자열의 길이 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>이 주어진다.</p>

### 출력 

 <p>첫째 줄에 길이 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>의 SSHS 문자열을 하나 출력한다. 가능한 답이 여러 개여도 하나만 출력하면 된다.</p>

