avg = []
for i in range(5):
    score = int(input())
    avg.append(score) if score >= 40 else avg.append(40)
print(sum(avg)//5)