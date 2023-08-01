# [Bronze II] 지수연산 - 2052 

[문제 링크](https://www.acmicpc.net/problem/2052) 

### 성능 요약

메모리: 31256 KB, 시간: 40 ms

### 분류

임의 정밀도 / 큰 수 연산, 수학

### 문제 설명

<p>양의 정수 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>이 주어질 때, <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mstyle><mjx-mfrac><mjx-frac type="d"><mjx-num><mjx-nstrut type="d"></mjx-nstrut><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-num><mjx-dbox><mjx-dtable><mjx-line type="d"></mjx-line><mjx-row><mjx-den><mjx-dstrut type="d"></mjx-dstrut><mjx-msup><mjx-mn class="mjx-n"><mjx-c class="mjx-c32"></mjx-c></mjx-mn><mjx-script style="vertical-align: 0.289em;"><mjx-mi class="mjx-i" size="s"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-script></mjx-msup></mjx-den></mjx-row></mjx-dtable></mjx-dbox></mjx-frac></mjx-mfrac></mjx-mstyle></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mstyle displaystyle="true" scriptlevel="0"><mfrac><mn>1</mn><msup><mn>2</mn><mi>N</mi></msup></mfrac></mstyle></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$\displaystyle\frac{1}{2^N}$</span></mjx-container>을 계산하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 정수 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>이 주어진다.</p>

### 출력 

 <p>첫째 줄에 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mstyle><mjx-mfrac><mjx-frac type="d"><mjx-num><mjx-nstrut type="d"></mjx-nstrut><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-num><mjx-dbox><mjx-dtable><mjx-line type="d"></mjx-line><mjx-row><mjx-den><mjx-dstrut type="d"></mjx-dstrut><mjx-msup><mjx-mn class="mjx-n"><mjx-c class="mjx-c32"></mjx-c></mjx-mn><mjx-script style="vertical-align: 0.289em;"><mjx-mi class="mjx-i" size="s"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-script></mjx-msup></mjx-den></mjx-row></mjx-dtable></mjx-dbox></mjx-frac></mjx-mfrac></mjx-mstyle></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mstyle displaystyle="true" scriptlevel="0"><mfrac><mn>1</mn><msup><mn>2</mn><mi>N</mi></msup></mfrac></mstyle></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$\displaystyle\frac{1}{2^N}$</span></mjx-container>의 정확한 값을 소수 형태로 출력한다. 단, 뒤에 불필요한 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$0$</span></mjx-container>을 덧붙여서는 안 된다.</p>

