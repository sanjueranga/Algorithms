s1 = "president"
s2 = "pevrdint"
m = len(s1)
n = len(s2)

dp = [[0 for i in range(m+1)] for j in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        if s1[j-1] == s2[i-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

print(dp[n][m])

dp = [[0 for i in range(m+1)] for j in range(n+1)]

for i in range(n-1,-1,-1):
	for j in range(m-1,-1,-1):
		if s1[j]==s2[i]:
			dp[i][j] = 1+dp[i+1][j+1]
		else:
			dp[i][j] = max(dp[i+1][j],dp[i][j+1])

print(dp[0][0])