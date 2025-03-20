# [Gold IV] 2차원 배열 다중 업데이트 단일 합 - 25826 

[문제 링크](https://www.acmicpc.net/problem/25826) 

### 성능 요약

메모리: 41412 KB, 시간: 88 ms

### 분류

누적 합, 스위핑

### 제출 일자

2025년 3월 20일 15:38:21

### 문제 설명

<p>크기가 <em>n</em> x <em>n</em>인 정수형 2차원 배열 <em>A</em>가 주어진다. 배열 <em>A</em>의 원소는 <em>A</em>[0][0], <em>A</em>[0][1], …, <em>A</em>[<em>n </em>- 1][<em>n </em>- 1]이다. 배열 <em>A</em>의 모든 원소의 초깃값은 입력으로 주어진다. 배열 <em>A</em>에 대한 <em>m</em>개의 질의가 저장된 배열 <em>B</em>가 주어진다. 배열 <em>B</em>에 저장된 <em>m</em>개의 질의는 아래 두 가지 유형으로 구분된다. 첫 번째가 유형 1을 나타내고 두 번째가 유형 2를 나타낸다.</p>

<ul>
	<li>1 <em>i</em><sub>1</sub><em> j</em><sub>1</sub><em> i</em><sub>2</sub><em> j</em><sub>2</sub><em> k</em> : 행 번호 <em>i</em>가 <em>i</em><sub>1</sub> ≤ <em>i</em> ≤ <em>i</em><sub>2</sub>이고, 열 번호 <em>j</em>가 <em>j</em><sub>1</sub> ≤ <em>j</em> ≤ <em>j</em><sub>2</sub>인 A[<em>i</em>][<em>j</em>]에 <em>k</em>를 더한다.</li>
	<li>2 <em>i</em><sub>1</sub><em> j</em><sub>1</sub><em> i</em><sub>2</sub><em> j</em><sub>2</sub> : 행 번호 <em>i</em>가 <em>i</em><sub>1</sub> ≤ <em>i</em> ≤ <em>i</em><sub>2</sub>이고, 열 번호 <em>j</em>가 <em>j</em><sub>1</sub> ≤ <em>j</em> ≤ <em>j</em><sub>2</sub>인 A[<em>i</em>][<em>j</em>]의 합을 출력한다.</li>
</ul>

<p>배열 <em>B</em>에 저장된 첫 번째 질의부터 <em>m</em>번째 질의까지 순서대로 처리하면서 유형 2에 대한 결과를 출력하자. <strong>단, 배열 <em>B</em>에는 유형 2의 질의가 마지막에 1개만 저장되어 있다.</strong></p>

### 입력 

 <p>첫 번째 줄에 <em>n</em>과 <em>m</em>이 공백을 사이에 두고 순서대로 주어진다.</p>

<p>두 번째 줄부터 <em>n</em>개의 줄에 배열 <em>A</em>의 원소가 주어진다. <em>i</em>번째 줄의 <em>j</em>번째 수는 배열 <em>A</em>의 (<em>i</em> - 1)번째 행 (<em>j</em> - 1)번째 열의 원소 A[<em>i</em> - 1][<em>j</em> - 1]을 나타낸다.</p>

<p>다음 줄부터 <em>m</em>개의 줄에 걸쳐서 배열 <em>B</em>에 저장된 <em>m</em>개의 질의가 순서대로 주어진다. 한 줄에 하나의 질의를 나타내는 수가 공백을 사이에 두고 순서대로 주어진다.</p>

### 출력 

 <p>첫 번째 줄에 유형 2의 질의 결과를 출력한다.</p>

