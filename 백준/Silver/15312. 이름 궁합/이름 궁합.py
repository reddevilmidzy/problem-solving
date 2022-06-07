A = input()
B = input()
#A = 'ABCDE'*400
#B = 'AWSDE'*400
alpha = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
dp = [[0 for i in range(2*len(A))] for j in range(2*len(A)-1)]
for i in range(len(A)+1):
    if i != len(A):
        dp[0][i*2] = alpha[ord(A[i])-65]
    if i != 0:
        dp[0][i*2-1] = alpha[ord(B[i-1])-65]

for i in range(1, 2*len(A)-1):
    for j in range(2*len(A)-i):
        dp[i][j] = int(str(dp[i-1][j] + dp[i-1][j+1])[-1])

print(dp[-1][0], dp[-1][1], sep='')