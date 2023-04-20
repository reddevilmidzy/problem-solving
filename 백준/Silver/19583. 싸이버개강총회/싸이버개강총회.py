import sys
input = sys.stdin.readline

def mapping(char: chr) -> list[int]:
    return list(map(int,char.split(":")))

s,e,q = map(str,input().rstrip().split())
s = mapping(s)
e = mapping(e)
q = mapping(q)

attend = set()
ans = 0

while True:
    try:
        time, name = map(str,input().rstrip().split())
        time = mapping(time)
        if time <= s:
            attend.add(name)
        elif e <= time <= q:
            if name in attend:
                attend.remove(name)
                ans += 1
    except:
        print(ans)
        break
