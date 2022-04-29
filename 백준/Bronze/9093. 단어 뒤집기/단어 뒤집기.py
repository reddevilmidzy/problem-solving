import sys
input = sys.stdin.readline

for i in range(int(input().rstrip())):
    word_list = []
    word = input().rstrip().split()
    for j in word:
        print(j[::-1], end=" ")
    print()