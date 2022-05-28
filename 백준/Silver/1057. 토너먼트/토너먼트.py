import time
star_time = time.time()

n, kim, im = map(int, input().split())
if n%2 == 0:
    star = [i for i in range(1, n+1)]
else:
    star = [i for i in range(1, n+2)]
cnt = 1
star[kim-1] = "kim"
star[im-1] = "im"
vs = {"kim", "im"}
new = []
name = set()
while len(star)>=2:
    for idx, s in enumerate(star):
        if idx%2 == 0:
            #print("check", s, star[idx+1])
            if s in vs and star[idx+1] in vs:
                print(cnt)
                end_time = time.time()
                #print("time :", end_time - star_time)
                exit()
            elif s in vs and star[idx+1] not in vs:
                new.append(s)
                name.add(s)
            elif star[idx+1] in vs and s not in vs:
                new.append(star[idx+1])
                name.add(star[idx+1])
            else:
                new.append(s)

            if len(name) == 2:
                name = set()
                check = (len(star) - idx+2)//2
                new.extend([i for i in range(check)])
                break

    if len(new)%2 == 0:
        star = new
    else:
        star = new
        star.append(0)
    new = []
    cnt += 1