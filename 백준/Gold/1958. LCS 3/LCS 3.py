import sys
input = sys.stdin.readline

word1 = input().rstrip()
word2 = input().rstrip()
word3 = input().rstrip()

def lcs(word1,word2,word3):
    n = len(word1)
    m = len(word2)
    l = len(word3)

    dp = [[[0]*(m+1) for _ in range(n+1)] for _ in range(l+1)]
    for k in range(1, l+1):
        for i in range(1, n+1):
            for j in range(1, m+1):
                if word1[i-1] == word2[j-1] == word3[k-1]:
                    dp[k][i][j] = dp[k-1][i-1][j-1] + 1
                else:
                    dp[k][i][j] = max(dp[k][i-1][j], dp[k][i][j-1], dp[k-1][i][j])
    return dp[l][n][m]

print(lcs(word1, word2, word3))