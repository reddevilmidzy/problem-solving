import sys

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
gg_name = {}
for i in range(n):
    name = input().rstrip()
    gg_member = []
    for u in range(int(input().rstrip())):
        member = input().rstrip()
        gg_member.append(member)
    gg_member.sort()
    gg_name[name] = gg_member
# print(gg_name)

for i in range(m):
    quize = input().rstrip()
    if int(input().rstrip()) == 0:
        for m in gg_name[quize]:
            print(m)
    else:
        for a in gg_name.keys():
            if quize in gg_name[a]:
                print(a)