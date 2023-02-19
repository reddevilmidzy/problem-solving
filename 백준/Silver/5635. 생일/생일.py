import sys
input = sys.stdin.readline
n = int(input())
students = []

for _ in range(n):
    name, day, month, year = map(str,input().rstrip().split())
    day,month,year = int(day), int(month), int(year)
    students.append([name, day, month, year])

students = sorted(students, key=lambda x: (x[3], x[2], x[1]))
print(students[-1][0], students[0][0], sep='\n')