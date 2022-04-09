def countPaths(m, n):
    if(m == 1 or n == 1):
        return(1)
    return(countPaths(m, n-1) + countPaths(m-1, n))

m = 3
n = 3
print(countPaths(m, n))