# [Gold III] 문자열 접기 - 16942 

[문제 링크](https://www.acmicpc.net/problem/16942) 

### 성능 요약

메모리: 31380 KB, 시간: 352 ms

### 분류

다이나믹 프로그래밍, 문자열

### 문제 설명

<p>상도는 문자열을 좋아하고, 문자열에 연산을 적용하는 것을 정말 좋아한다. 오늘 상도가 문자열에 적용할 연산은 "접기"이다.</p>

<p>접기 연산을 수행하려면, 문자열을 접을 위치를 정해야 한다. 위치는 인접한 두 문자의 사이이고, 이 위치를 기준으로 왼쪽 부분 A와 오른쪽 부분 B로 나눈다. 그 다음, B를 뒤집고, A의 위에 뒤집은 문자열 B를 놓는다. A와 B는 접은 위치를 기준으로 줄이 맞춰져 있어야 한다.</p>

<p>아래는 "<code>ABCDEFGHIJK</code>"를 F와 G의 사이에서 접은 예시이다. 위치는 '|'로 표시하면, "<code>ABCDEF|GHIJK</code>"와 같다.</p>

<pre> KJIHG
ABCDEF</pre>

<p>오른쪽 부분의 길이는 왼쪽 부분의 길이보다 길 수도 있다. 아래는 "A|BCDEFGHIJK"의 예시이다.</p>

<pre>KJIHGFEDCB
         A</pre>

<p>문자열을 접는 연산은 여러 번 수행할 수 있다. 아래는 "<code><span style="color:#27ae60;">AB</span>|<span style="color:#8e44ad;">RACA</span>|<span style="color:#2980b9;">DAB</span>|<span style="color:#e67e22;">RA</span></code>"와 "<code><span style="color:#27ae60;">X</span>|<span style="color:#8e44ad;">XXXXX</span>|<span style="color:#2980b9;">X</span>|<span style="color:#e67e22;">X</span>|<span style="color:#e74c3c;">XXXXXX</span></code>" 를 접은 예시이다.</p>

<pre>           <span style="color:#e74c3c;">XXXXXX</span>
 <span style="color:#e67e22;">AR        X</span>
<span style="color:#2980b9;">DAB        X</span>
<span style="color:#8e44ad;">ACAR       XXXXX</span>
  <span style="color:#27ae60;">AB           X</span></pre>

<p>문자열을 접으면 새로운 문자열을 만들 수 있다. 새로운 문자열은 문자열을 접은 상태에서 세로 방향으로 만들어야 한다. 문자열의 시작 위치는 항상 가장 아래에 있는 문자가 되어야 하고, 위 방향으로 문자열을 이어 붙여서 새로운 문자열을 만든다. 가장 위에 있는 문자와 가장 아래에 있는 문자의 사이에 문자가 없으면 안 된다."<code>ABCD|EFGH|IJ|K</code>"에서 만들 수 있는 새로운 문자열은 "<span style="color:#e74c3c;"><code>AHI</code></span>", "<span style="color:#8e44ad;"><code>BGJK</code></span>", "<span style="color:#2980b9;"><code>CF</code></span>", "<span style="color:#27ae60;"><code>DE</code></span>" 이다.</p>

<pre> <span style="color:#8e44ad;">K</span>
<span style="color:#e74c3c;">I</span><span style="color:#8e44ad;">J</span>
<span style="color:#e74c3c;">H</span><span style="color:#8e44ad;">G</span><span style="color:#2980b9;">F</span><span style="color:#27ae60;">E</span>
<span style="color:#e74c3c;">A</span><span style="color:#8e44ad;">B</span><span style="color:#2980b9;">C</span><span style="color:#27ae60;">D</span></pre>

<p>"<code>X|XXXXX|X|X|XXXXXX</code>"에서 만들 수 있는 새로운 문자열은 없다. 모든 세로 위치의 문자열이 가장 아래에서 시작하지 않거나, 중간에 공백이 존재하기 때문이다. "<code>A|BCDEFGHIJK</code>"에서 만들 수 있는 새로운 문자열은 "<code>AB</code>", "<code>AB|RACA|DAB|RA</code>"에서 만들 수 있는 새로운 문자열은 "<code>AABR</code>", "<code>BR</code>"이 있다.</p>

<p>문자열 S가 주어진다. S를 적절히 접어서 만들 수 있는 새로운 문자열 중에서, 같은 문자로만 이루어져 있으면서 길이가 가장 긴 것을 구해보자.</p>

### 입력 

 <p>첫째 줄에 문자열 S가 주어진다. S는 알파벳 대문자로만 이루어져 있고, 길이는 1,000보다 작거나 같다.</p>

### 출력 

 <p>첫째 줄에 문자열 S를 접어서 만들 수 있는 새로운 문자열 중에서, 같은 문자로만 이루어져 있으면서 길이가 가장 긴 것의 길이를 출력한다.</p>

