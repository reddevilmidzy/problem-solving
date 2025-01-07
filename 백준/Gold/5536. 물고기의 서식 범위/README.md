# [Gold II] 물고기의 서식 범위 - 5536 

[문제 링크](https://www.acmicpc.net/problem/5536) 

### 성능 요약

메모리: 17452 KB, 시간: 20 ms

### 분류

값 / 좌표 압축, 누적 합, 스위핑

### 제출 일자

2025년 1월 8일 03:42:25

### 문제 설명

<p>해양 연구원 상근이는 동해에 서식하고 있는 N 종류의 물고기의 특성에 대해 연구하고 있다.</p>

<p>각 물고기가 서식할 수 있는 구역은 직육면체 모양이다. 물고기는 서식 범위의 경계를 포함해서 모든 곳을 자유롭게 이동할 수 있지만, 절대로 그 범위의 밖으로 나오지 않는다.</p>

<p>바다의 점은 3개 실수 (x, y, d)로 표현한다. 상공에서 볼 때, 어떤 지점을 기준으로 동쪽으로 x, 북쪽으로 y만큼 떨어진 곳에서 해수면에서 깊이가 d점인 점을 나타낸다. 바다는 평면이라고 가정한다.</p>

<p>상근이는 물고기가 K 종류 이상 서식하는 범위를 구하려고 한다. 그러한 위치의 부피를 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 N과 K가 주어진다. (1 ≤ K ≤ N ≤ 50)</p>

<p>둘째 줄부터 N개 줄에 물고기의 서식범위를 나타내는 6개의 정수 X<sub>i,1</sub> Y<sub>i,1</sub> D<sub>i,1</sub> X<sub>i,2</sub> Y<sub>i,2</sub> D<sub>i,2</sub>가 주어진다. (0 ≤ X<sub>i,1</sub> < X<sub>i,2</sub> ≤ 10<sup>6</sup>, 0 ≤ Y<sub>i,1</sub> < Y<sub>i,2</sub> ≤ 10<sup>6</sup>, 0 ≤ D<sub>i,1</sub> < D<sub>i,2</sub> ≤ 10<sup>6</sup>) 물고기의 서식 구역은 (X<sub>i,1</sub>, Y<sub>i,1</sub>, D<sub>i,1</sub>), (X<sub>i,2</sub>, Y<sub>i,1</sub>, D<sub>i,1</sub>), (X<sub>i,2</sub>, Y<sub>i,2</sub>, D<sub>i,1</sub>), (X<sub>i,1</sub>, Y<sub>i,2</sub>, D<sub>i,1</sub>), (X<sub>i,1</sub>, Y<sub>i,1</sub>, D<sub>i,2</sub>), (X<sub>i,2</sub>, Y<sub>i,1</sub>, Di,2), (X<sub>i,2</sub>, Y<sub>i,2</sub>, D<sub>i,2</sub>), (X<sub>i,1</sub>, Y<sub>i,2</sub>, D<sub>i,2</sub>)를 꼭짓점으로 하는 직육면체이다.</p>

### 출력 

 <p>첫째 줄에 K 종류 이상의 물고기가 서식하는 구역의 부피를 출력한다.</p>

