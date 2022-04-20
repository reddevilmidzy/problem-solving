n = input()
measuar = list(map(int, input().split()))
print(max(measuar)*min(measuar)) if len(measuar) != 1 else print(measuar[0]**2)