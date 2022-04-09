def countPaths(m, n, memo):
    if (m, n) in memo:
        return(memo[(m, n)])
    elif(m == 1 or n == 1):
        ans = 1
        memo[(m, n)] = ans
    else:
        ans = countPaths(m, n-1, memo) + countPaths(m-1, n, memo)
        memo[(m, n)] = ans
    return(ans)

m = 50
n = 50
memo = {}
print(countPaths(m, n, memo))