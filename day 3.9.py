def is_match(s, p):
    m, n = len(s), len(p)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True  
    for i in range(m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[i][j] = dp[i][j - 2] or (i > 0 and (s[i - 1] == p[j - 2] or p[j - 2] == '.') and dp[i - 1][j])
            else:
                dp[i][j] = i > 0 and (s[i - 1] == p[j - 1] or p[j - 1] == '.') and dp[i - 1][j - 1]
    return dp[m][n]

s = input("Enter the input string: ")
p = input("Enter the pattern: ")
result = is_match(s, p)
print("Does the pattern match the input string?", result)