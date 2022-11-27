def search():
    n = int(input())
    sqr = int(n**0.5)
    if sqr**2 < n:
        print(sqr+1)
    else:
        print(sqr)

search()