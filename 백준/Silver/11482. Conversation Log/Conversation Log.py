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
ans = sorted(word_dict.items(), key=lambda x:(-x[1],x[0]))

per = len(person)
all_clear = False

for key, val in ans:
    if len(name_dict[key])==per:
        print(key)
        all_clear = True

if not all_clear:
    print("ALL CLEAR")