from collections import defaultdict
import sys
input = sys.stdin.readline

n = int(input())
word_dict = defaultdict(int)
name_dict = defaultdict(set)
person = set()
for _ in range(n):
    tmp = list(map(str,input().rstrip().split()))
    name= tmp[0]
    word = tmp[1:]
    person.add(name)
    for i in range(len(word)):
        name_dict[word[i]].add(name)
        word_dict[word[i]] += 1
ans = sorted(word_dict.items(), key=lambda x:x[1], reverse=True)

per = len(person)

res = []
for key, val in ans:
    if len(name_dict[key])==per:
        res.append((key, val))

if res == []:
    print("ALL CLEAR")
else:
    result = sorted(res, key=lambda x:(-x[1], x[0]))
    for i in range(len(result)):
        print(result[i][0])