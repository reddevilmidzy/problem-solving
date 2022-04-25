N = int(input())
moves = input()
 
# 북 : 1, 동 : 2, 남 : 3, 서 : 4
direction = 3
 
cur_Row = 0
cur_Col = 0
len_Row = 1
len_Col = 1
graph = [['.']]
 
for move in moves:
    if move == 'R':
        direction += 1
        if direction == 5:
            direction = 1

    elif move == 'L':
        direction -= 1
        if direction == 0:
            direction = 4

    else:
        if direction == 1:
            cur_Row -= 1
            # 위쪽으로 넘어갈 때
            if cur_Row == -1:
                len_Row += 1
                graph = [['#' for _ in range(len_Col)]]+graph
                cur_Row = 0

        elif direction == 2:
            cur_Col += 1
            # 오른쪽으로 넘어갈 때
            if cur_Col == len_Col:
                len_Col += 1
                for i in range(len_Row):
                    graph[i].append('#')

        elif direction == 3:
            cur_Row += 1
            # 아래로 넘어갈 때
            if cur_Row == len_Row:
                len_Row += 1
                graph.append(['#' for _ in range(len_Col)])

        elif direction == 4:
            cur_Col -= 1
            # 왼쪽으로 넘어갈 때
            if cur_Col == -1:
                len_Col += 1
                for i in range(len_Row):
                    graph[i] = ['#']+graph[i]
                cur_Col = 0

        if graph[cur_Row][cur_Col] == '#':
            graph[cur_Row][cur_Col] = '.'

for i in graph:
    print(''.join(i))