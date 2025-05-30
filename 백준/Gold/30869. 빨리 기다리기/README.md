# [Gold I] 빨리 기다리기 - 30869 

[문제 링크](https://www.acmicpc.net/problem/30869) 

### 성능 요약

메모리: 39936 KB, 시간: 1280 ms

### 분류

데이크스트라, 그래프 이론, 최단 경로

### 제출 일자

2025년 2월 20일 17:36:35

### 문제 설명

<p>재원이의 마을에는 $N$개의 버스 정류장과 $M$개의 버스 노선이 있다.</p>

<p>$i$번 노선은 $s_i$번 정류장에서 출발해 $t_i$시간 후 $e_i$번 정류장에 도착하며, $s_i$번 정류장과 $e_i$번 정류장을 제외한 다른 정류장에는 멈추지 않는다. 또한, 배차 간격 $g_i$가 있어 $0$시에 $s_i$번 정류장에서 버스가 운행을 시작한 뒤, 매 $g_i$시간마다 $s_i$번 정류장에서 버스가 운행을 시작한다.</p>

<p>빨리 도착해야 하는 재원이는, <strong>빨리 기다리기</strong>를 사용하기로 했다. 빨리 기다리기를 사용하면, 현재 정류장에서 출발하는 노선 중 하나를 선택해 배차 간격과 무관하게 지금 당장 출발하도록 할 수 있다.</p>

<p>빨리 기다리기를 최대 $K$번 사용해 $1$번 정류장에서 $N$번 정류장까지 가는 데에 걸리는 최소 시간을 재원이에게 알려주자.</p>

### 입력 

 <p>첫 번째 줄에 정류장의 개수 $N$, 노선의 개수 $M$, 빨리 기다리기를 사용할 수 있는 최대 횟수 $K$가 공백으로 구분되어 주어진다. $(2 \leq N \leq 500;$ $1 \leq M \leq 250\,000;$ $0 \leq K \leq 500)$</p>

<p>$M$개의 줄에 걸쳐 버스 노선의 정보가 주어진다. $i+1$번째 줄에는 $i$번 버스 노선의 정보 $s_i$, $e_i$, $t_i$, $g_i$가 공백으로 구분되어 주어진다. $(1 \leq s_i, e_i \leq N;$ $s_i \neq e_i;$ $1 \leq t_i \leq 10\,000;$ $1 \leq g_i \leq 10\,000)$</p>

### 출력 

 <p>첫 번째 줄에 $1$번 정류장에서 $N$번 정류장까지 가는 데에 걸리는 최소 시간을 출력한다. 불가능한 경우에는 $-1$을 출력한다.</p>

