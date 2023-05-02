import sys
input = sys.stdin.readline

def dfs(word:str, cur: dict, depth: int) -> None:
    print("--"*depth + word)
    for nxt in sorted(cur[word]):
        dfs(nxt, cur[word], depth+1)

trie = dict()

n = int(input())
for _ in range(n):
    words = list(map(str,input().rstrip().split()))[1:]
    cur = trie
    for nxt in words:
        if nxt not in cur:
            cur[nxt] = dict()
        cur = cur[nxt]

depth = 0
for st in sorted(trie.keys()):
    dfs(st, trie, depth)