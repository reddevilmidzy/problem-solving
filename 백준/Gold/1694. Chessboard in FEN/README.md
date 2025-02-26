# [Gold IV] Chessboard in FEN - 1694 

[문제 링크](https://www.acmicpc.net/problem/1694) 

### 성능 요약

메모리: 13732 KB, 시간: 16 ms

### 분류

구현

### 제출 일자

2025년 2월 26일 21:24:02

### 문제 설명

<p>In the FEN (Forsyth-Edwards Notation), a chessboard is described as follows:</p>

<ul>
	<li>The Board-Content is specified starting with the top row and ending with the bottom row.</li>
	<li>Character / is used to separate data of adjacent rows.</li>
	<li>Each row is specified from left to right.</li>
	<li>White pieces are identified by uppercase piece letters: PNBRQK.</li>
	<li>Black pieces are identified by lowercase piece letters: pnbrqk.</li>
	<li>Empty squares are represented by the numbers one through eight.</li>
	<li>A number used represents the count of contiguous empty squares along a row.</li>
	<li>Each row's sum of numbers and characters must equal 8.</li>
</ul>

<p>For example:</p>

<ul>
	<li>5k1r/2q3p1/p3p2p/1B3p1Q/n4P2/6P1/bbP2N1P/1K1RR3</li>
</ul>

<p>is the FEN notation description of the following chessboard:</p>

<p><img alt="" src="" style="height:171px; width:171px"></p>

<p>The chessboard of the beginning of a chess game is described in FEN as:</p>

<ul>
	<li>rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR</li>
</ul>

<p>Your task is simple: given a chessboard description in a FEN notation you are asked to compute the number of unoccupied squares on the board which are not attacked by any piece.</p>

### 입력 

 <p>Input is a sequence of lines, each line containing a FEN description of a chessboard. Note that the description does not necessarily give a legal chess position. Input lines do not contain whitespace.</p>

### 출력 

 <p>For each line of input, output one line containing an integer which gives the number of unoccupied squares which are not attacked.</p>

