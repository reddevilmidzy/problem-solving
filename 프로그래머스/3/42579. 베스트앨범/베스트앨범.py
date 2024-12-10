from collections import defaultdict
def solution(genres, plays):
    res = []
    song = defaultdict(list)
    n = len(genres)
    tot = defaultdict(int)
    
    for i in range(n):
        song[genres[i]].append((plays[i], i))
        tot[genres[i]] += plays[i]
    
    for key,val in sorted(tot.items(), key=lambda x:-x[1]):
        song[key].sort(key=lambda x:(-x[0], x[1]))
        res.append(song[key][0][1])
        if len(song[key]) > 1:
            res.append(song[key][1][1])
        
    return res