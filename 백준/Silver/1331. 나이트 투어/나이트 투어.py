import sys
input = sys.stdin.readline
ans = "Valid"
visited = []
for i in range(36):
    if i == 0:
        start = input().rstrip()
        pre = start
    elif i < 35:
        now = input().rstrip()
        if ((abs(ord(pre[0]) - ord(now[0])) ==1 and abs(int(pre[1])-int(now[1])) == 2) or (abs(ord(pre[0]) - ord(now[0])) ==2 and abs(int(pre[1])-int(now[1])) == 1)) and now not in visited:
            #print("으악")
            pass
        else:   
            ans = "Invalid"
        visited.append(now)
        pre = now
    else:
        now = input().rstrip()
        if ((abs(ord(now[0]) - ord(start[0])) ==1 and abs(int(now[1])-int(start[1])) == 2) or (abs(ord(now[0]) - ord(start[0])) ==2 and abs(int(now[1])-int(start[1])) == 1)) and now not in visited:
            pass
        else:
            ans = "Invalid"

print(ans)