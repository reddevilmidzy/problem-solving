# [Gold IV] Hodowla - 8693 

[문제 링크](https://www.acmicpc.net/problem/8693) 

### 성능 요약

메모리: 55936 KB, 시간: 140 ms

### 분류

누적 합

### 제출 일자

2025년 3월 12일 20:38:40

### 문제 설명

<p>Bajtocki ogród działkowy (BOD) od wielu lat hoduje warzywa - wyłącznie marchewki i pietruszki. BOD ma kształt kwadratu o boku długości <em>n</em> i jest podzielony na <em>n</em> · <em>n</em> jednostkowych pól. Na każdym z nich rośnie dokładnie jedna marchewka lub jedna pietruszka.</p>

<p>Specjalna hodowla decyduje o wyjątkowości i smaku warzyw. Polega ona na corocznym wybieraniu pewnego obszaru, dla którego dokonujemy zamiany hodowli. Zamiana hodowli polega na posadzeniu marchewek wszędzie tam, gdzie rosły dotąd pietruszki, a pietruszek wszędzie tam, gdzie rosły marchewki. Na pozostałym obszarze marchewki i pietruszki rosną dokładnie tam, gdzie rok temu.</p>

<p>Właściciel ogrodu rozpisał plan hodowli na wiele lat. Zastanawia się teraz, jak będzie wyglądał jego ogród działkowy po tych wszystkich latach.</p>

### 입력 

 <p>Pierwszy wiersz standardowego wejścia zawiera jedną liczbę całkowitą <em>n</em> (1 ≤ <em>n</em> ≤ 1 000), oznaczającą rozmiar ogrodu działkowego. W <em>n</em> kolejnych wierszach znajduje się opis działki.</p>

<p>Każdy wiersz opisuje jeden pas ogrodu i zawiera <em>n</em> liczb całkowitych <em>w</em><sub>1</sub>, <em>w</em><sub>2</sub>, ..., <em>w<sub>n</sub></em>, (0 ≤ <em>w<sub>i</sub></em> ≤ 1), gdzie <em>w<sub>i</sub></em> opisuje <em>i</em>-te pole w rozpatrywanym pasie działki. Jeśli <em>w<sub>i</sub></em> jest równe 0, to na polu tym rośnie marchewka, jeśli natomiast <em>w<sub>i</sub></em> jest równe 1, to rośnie tam pietruszka.</p>

<p>Kolejny wiersz wejścia zawiera jedną liczbę całkowitą <em>m</em> (1 ≤ <em>m</em> ≤ 10<sup>6</sup>), oznaczającą liczbę lat, dla których właściciel rozpisał plan hodowli. W <em>m</em> następnych wierszach znajduje się opis zamian hodowli w kolejnych latach.</p>

<p>Każdy wiersz zawiera cztery liczby całkowite <em>x</em><sub>1</sub>, <em>y</em><sub>1</sub>, <em>x</em><sub>2</sub>, <em>y</em><sub>2</sub> (1 ≤ <em>x</em><sub>1</sub> ≤ <em>x</em><sub>2</sub> ≤ <em>n</em>, <em>y</em><sub>1</sub> ≤ <em>y</em><sub>2</sub> ≤ <em>n</em>), oznaczające, że w danym roku właściciel planuje dokonać zamiany hodowli na polach wyznaczonych przez prostokąt, ktorego lewy górny róg posiada współrzędne <em>x</em><sub>1</sub>, <em>y</em><sub>1</sub> a prawy dolny róg <em>x</em><sub>2</sub>, <em>y</em><sub>2</sub>.</p>

### 출력 

 <p>Standardowe wyjście powinno zawierać <em>n</em> wierszy. Każdy wiersz powinien opisywać kolejny pas działki po <em>m</em> latach i powinien zawierać <em>n</em> liczb całkowitych <em>w</em><sub>1</sub>, <em>w</em><sub>2</sub>, ..., <em>w<sub>n</sub></em>, gdzie <em>w<sub>i</sub></em> powinno być równe 1 - jeśli na <em>i</em> tym polu rosnąć będzie marchewka lub 0 - jeśli pietruszka.</p>

