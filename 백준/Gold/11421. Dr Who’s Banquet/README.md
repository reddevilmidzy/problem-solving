# [Gold I] Dr Who’s Banquet - 11421 

[문제 링크](https://www.acmicpc.net/problem/11421) 

### 성능 요약

메모리: 23480 KB, 시간: 68 ms

### 분류

해 구성하기, 차수열, 그래프 이론, 그리디 알고리즘, 정렬

### 제출 일자

2025년 2월 5일 12:40:45

### 문제 설명

<p>Dr. Who is organising a banquet, and will be inviting several guests. A guest is happy, if he can chat with a fixed number of other guests. We assume that guests cannot talk to themselves. Help Dr. Who make all his guests happy, if possible, by organising chats between guests.</p>

### 입력 

 <p>The program input is from a text file. The file contains several data sets, and each data set is encoded on a line from the file. A data set consists of n≤10000 positive integers a<sub>1</sub>, a<sub>2</sub>, … a<sub>n</sub>, separated by single whitespaces. The last integer an is immediately followed by the newline character. Each number a<sub>i</sub>, with 1≤i≤n is the number of chat partners guest i would like to have. We assume that a<sub>i</sub>≤1000 for all 1≤i≤n. The last data set is followed by the end of file.</p>

### 출력 

 <p>If all guests can be made happy, the program output consists of a n×n matrix m, where m[i][j]=m[j][i]=1 if guests i and j chat, and m[i][j]=m[j][i]=0, otherwise. The matrix will be represented at standard output, as follows: each value m[i][j] from a row will be followed by one whitespace (including the last value from the row). Each row will be separated by the newline character. If it is not possible for all guests to be happy, then the program output is the message “fail”. The matrix and the message are allways followed by an empty line.</p>

