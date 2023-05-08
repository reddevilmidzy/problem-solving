def is_parindrom(word):
    return word == word[::-1]

def is_unique(word):
    return len(set(word)) != 1 and n != 1

word = input()
n = len(word)
if is_parindrom(word):
    if is_unique(word):
        print(n-1)
    else:
        print(-1)
else:
    print(n)