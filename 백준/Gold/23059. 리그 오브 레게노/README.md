# [Gold II] 리그 오브 레게노 - 23059 

[문제 링크](https://www.acmicpc.net/problem/23059) 

### 성능 요약

메모리: 259712 KB, 시간: 1120 ms

### 분류

자료 구조, 그래프 이론, 해시를 사용한 집합과 맵, 위상 정렬

### 문제 설명

<p>백남이는 새 학기를 맞이하여, 리그 오브 레게노(League of Legeno)라는 게임을 시작했다. 리그 오브 레게노는 <a href="https://ko.wikipedia.org/wiki/%EB%A9%80%ED%8B%B0%ED%94%8C%EB%A0%88%EC%9D%B4%EC%96%B4_%EC%98%A8%EB%9D%BC%EC%9D%B8_%EB%B0%B0%ED%8B%80_%EC%95%84%EB%A0%88%EB%82%98">AOS</a>(Aeon of Strife) 종류의 게임으로, 5명의 플레이어가 한 팀이 되어 상대편의 주요 건물을 부수는 것이 게임의 승리 목표이다. 게임 내에서 유저들은 게임에서 승리하기 위해 자신의 캐릭터의 능력치를 올리도록 해야 한다. 맵에 등장하는 몬스터나 상대 팀의 플레이어를 처치하며 경험치와 골드를 보상으로 얻고, 이 경험치를 통해 캐릭터의 레벨을 올림으로써 레벨 증가에 따른 능력치를 얻게 된다. 그러나 한 게임에서 레벨에 대한 일정 상한선이 존재한다. 다른 방법으로는 골드를 사용하여 아이템들을 구매함으로써 자신의 능력치를 높일 수 있다.</p>

<p>아이템 사이에 미리 정해진 구매 순서가 존재한다. 이제 막 게임을 시작한 백남이는 구매 순서 전체가 아니라 두 아이템 사이의 선후관계 일부만 알고 있다. 백남이가 다음 과정을 반복하여 아이템을 구매할 때, 아이템의 전체 구매 순서를 알아내자.</p>

<ul>
	<li>현재 구매할 수 있는 아이템 중 아직 구매하지 않은 아이템을 모두 찾는다.</li>
	<li>찾은 아이템을 사전 순으로 모두 구매한다.</li>
</ul>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/2970e6b0-9d07-4dc0-999f-9a0b19c99d23/-/preview/" style="height: 500px; width: 500px;"><br>
 </p>

### 입력 

 <p>첫째 줄에는 백남이가 알고 있는 아이템 사이의 관계의 수 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>(1 ≤ <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container> ≤ 200,000)를 입력받는다. <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>개의 줄에 걸쳐서 아이템 이름을 의미하는 문자열 2개 A B가 주어진다. 아이템 A는 아이템 B를 구입하기 위해 앞서 구매해야 하는 것을 의미하며, 아이템 A와 아이템 B는 항상 다르다. 모든 아이템은 선후관계에서 적어도 한 번씩 등장한다. 아이템 이름은 알파벳 소문자로만 이루어져 있고, 공백을 포함하지 않는다. 아이템 이름의 길이는 1 이상 15 이하이다.</p>

### 출력 

 <p>먼저 구매해야 하는 아이템부터 순서대로 각 줄에 걸쳐서 출력하라. 단, 모든 아이템을 구매할 수 없다면 -1을 출력한다.</p>

