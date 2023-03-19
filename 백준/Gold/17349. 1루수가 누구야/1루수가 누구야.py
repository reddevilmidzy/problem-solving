import sys
input = sys.stdin.readline
n = 9

def verify(players:dict):
    no = set()
    can = set()
    p = set([i for i in range(1, n+1)])
    for player, guess in players.items():
        if not guess:
            continue
        can_be,can_not = sum(guess), len(guess) - sum(guess)
        if can_be > 0 and can_not > 0:
            return False, {0}
        if can_be > 0:
            can.add(player)
        elif can_not > 0:
            no.add(player)
    if len(can) > 1:
        return False, {0}
    elif len(can) == 1:
        return True, can
    
    elif len(no) == 8 and len(can) == 0:
        return True, (p - no)
    
    elif len(no) > 0:
        return True, (p-no)

    return False, {0}

def set_logic(guess):
    res = dict()
    for x in range(1, n+1):
        res[x] = []

    for is_first, a in guess:
        res[a].append(is_first)

    return res

guess = [list(map(int,input().split())) for _ in range(n)]
ans = set()
for i in range(n):
    guess[i][0] = int(not guess[i][0])
    players = set_logic(guess)
    can, player = verify(players)
    if can:
        ans = ans | player
    guess[i][0] = int(not guess[i][0])
print(ans.pop() if len(ans) == 1 else -1)