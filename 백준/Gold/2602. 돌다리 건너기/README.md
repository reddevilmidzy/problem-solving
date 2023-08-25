# [Gold IV] 돌다리 건너기 - 2602 

[문제 링크](https://www.acmicpc.net/problem/2602) 

### 성능 요약

메모리: 31256 KB, 시간: 84 ms

### 분류

다이나믹 프로그래밍

### 문제 설명

<p>절대반지를 얻기 위하여 반지원정대가 출발한다. 원정대가 지나가야할 다리는 두 개의 인접한 돌다리로 구성되어 있다. 하나는 <악마의 돌다리>이고 다른 하나는 <천사의 돌다리>이다.</p>

<p>아래 그림 1은 길이가 6인 다리의 한 가지 모습을 보여준다. 그림에서 위의 가로줄은 <악마의 돌다리>를 표시하는 것이고, 아래의 가로줄은 <천사의 돌다리>를 표시한다. 두 돌다리의 길이는 항상 동일하며, 각 칸의 문자는 해당 돌에 새겨진 문자를 나타낸다. 두 다리에 새겨진 각 문자는 {R, I, N, G, S} 중 하나이다.</p>

<table class="table table-bordered table-center-50 td-center td-middle">
	<tbody>
		<tr>
			<td rowspan="2">출발</td>
			<td>R</td>
			<td>I</td>
			<td>N</td>
			<td>G</td>
			<td>S</td>
			<td>R</td>
			<td rowspan="2">도착</td>
		</tr>
		<tr>
			<td>G</td>
			<td>R</td>
			<td>G</td>
			<td>G</td>
			<td>N</td>
			<td>S</td>
		</tr>
	</tbody>
</table>

<p>반지원정대가 소유하고 있는 마법의 두루마리에 <악마의 돌다리>와 <천사의 돌다리>를 건너갈 때 반드시 순서대로 밟고 지나가야할 문자들이 적혀있다. 이 순서대로 지나가지 않으면 돌다리는 무너져 반지원정대는 화산 속으로 떨어지게 된다.</p>

<p>다리를 건널 때 다음의 제한 조건을 모두 만족하면서 건너야 한다.</p>

<ol>
	<li>왼쪽(출발지역)에서 오른쪽(도착지역)으로 다리를 지나가야 하며, 반드시 마법의 두루마리에 적힌 문자열의 순서대로 모두 밟고 지나가야 한다.</li>
	<li>반드시 <악마의 돌다리>와 <천사의 돌다리>를 번갈아가면서 돌을 밟아야 한다. 단, 출발은 어떤 돌다리에서 시작해도 된다.</li>
	<li>반드시 한 칸 이상 오른쪽으로 전진해야하며, 건너뛰는 칸의 수에는 상관이 없다. 만일 돌다리의 모양이 그림 1과 같고 두루마리의 문자열이 "RGS"라면 돌다리를 건너갈 수 있는 경우는 다음의 3가지 뿐이다. (아래 그림에서 빨간색 문자는 밟고 지나가는 돌다리를 나타낸다.)</li>
</ol>

<table class="table table-bordered table-center-50 td-center td-middle">
	<tbody>
		<tr>
			<td rowspan="2">출발</td>
			<td><span style="color:red">R</span></td>
			<td>I</td>
			<td>N</td>
			<td>G</td>
			<td><span style="color:red">S</span></td>
			<td>R</td>
			<td rowspan="2">도착</td>
		</tr>
		<tr>
			<td>G</td>
			<td>R</td>
			<td><span style="color:red">G</span></td>
			<td>G</td>
			<td>N</td>
			<td>S</td>
		</tr>
	</tbody>
</table>

<table class="table table-bordered table-center-50 td-center td-middle">
	<tbody>
		<tr>
			<td rowspan="2">출발</td>
			<td><span style="color:red">R</span></td>
			<td>I</td>
			<td>N</td>
			<td>G</td>
			<td><span style="color:red">S</span></td>
			<td>R</td>
			<td rowspan="2">도착</td>
		</tr>
		<tr>
			<td>G</td>
			<td>R</td>
			<td>G</td>
			<td><span style="color:red">G</span></td>
			<td>N</td>
			<td>S</td>
		</tr>
	</tbody>
</table>

<table class="table table-bordered table-center-50 td-center td-middle">
	<tbody>
		<tr>
			<td rowspan="2">출발</td>
			<td>R</td>
			<td>I</td>
			<td>N</td>
			<td><span style="color:red">G</span></td>
			<td>S</td>
			<td>R</td>
			<td rowspan="2">도착</td>
		</tr>
		<tr>
			<td>G</td>
			<td><span style="color:red">R</span></td>
			<td>G</td>
			<td>G</td>
			<td>N</td>
			<td><span style="color:red">S</span></td>
		</tr>
	</tbody>
</table>

<p>아래의 세 방법은 실패한 방법이다.</p>

<table class="table table-bordered table-center-50 td-center td-middle">
	<tbody>
		<tr>
			<td rowspan="2">출발</td>
			<td><span style="color:red">R</span></td>
			<td>I</td>
			<td>N</td>
			<td>G</td>
			<td>S</td>
			<td>R</td>
			<td rowspan="2">도착</td>
		</tr>
		<tr>
			<td>G</td>
			<td>R</td>
			<td><span style="color:red">G</span></td>
			<td>G</td>
			<td>N</td>
			<td>S</td>
		</tr>
	</tbody>
</table>

<table class="table table-bordered table-center-50 td-center td-middle">
	<tbody>
		<tr>
			<td rowspan="2">출발</td>
			<td><span style="color:red">R</span></td>
			<td>I</td>
			<td>N</td>
			<td><span style="color:red">G</span></td>
			<td>S</td>
			<td>R</td>
			<td rowspan="2">도착</td>
		</tr>
		<tr>
			<td>G</td>
			<td>R</td>
			<td>G</td>
			<td>G</td>
			<td>N</td>
			<td><span style="color:red">S</span></td>
		</tr>
	</tbody>
</table>

<table class="table table-bordered table-center-50 td-center td-middle">
	<tbody>
		<tr>
			<td rowspan="2">출발</td>
			<td><span style="color:red">R</span></td>
			<td>I</td>
			<td>N</td>
			<td>G</td>
			<td><span style="color:red">S</span></td>
			<td>R</td>
			<td rowspan="2">도착</td>
		</tr>
		<tr>
			<td><span style="color:red">G</span></td>
			<td>R</td>
			<td>G</td>
			<td>G</td>
			<td>N</td>
			<td>S</td>
		</tr>
	</tbody>
</table>

<p>왜냐하면 첫 번째는 문자열 "RGS"를 모두 밟고 지나가야 하는 조건 1)을 만족하지 않으며, 두 번째는 번갈아가면서 돌을 밟아야 하는 조건 2)를, 세 번째는 앞으로 전진을 하여야하는 조건 3)을 만족하지 않기 때문이다.</p>

<p>마법의 두루마리에 적힌 문자열과 두 다리의 돌에 새겨진 문자열이 주어졌을 때, 돌다리를 통과할 수 있는 모든 가능한 방법의 수를 계산하는 프로그램을 작성하시오. 예를 들어, 그림 1의 경우는 통과하는 방법이 3가지가 있으므로 3을 출력해야 한다.</p>

### 입력 

 <p>첫째 줄에는 마법의 두루마리에 적힌 문자열(R, I, N, G, S 로만 구성된)이 주어진다. 이 문자열의 길이는 최소 1, 최대 20 이다. 그 다음 줄에는 각각 <악마의 돌다리>와 <천사의 돌다리>를 나타내는 같은 길이의 문자열이 주어진다. 그 길이는 1 이상, 100 이하이다.</p>

### 출력 

 <p>마법의 두루마리에 적힌 문자열의 순서대로 다리를 건너갈 수 있는 방법의 수를 출력한다. 그러한 방법이 없으면 0을 출력한다.</p>

<p>모든 테스트 데이터에 대한 출력결과는 2<sup>31</sup>-1 이하이다.</p>

