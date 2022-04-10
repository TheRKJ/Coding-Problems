#Task-1
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

m = 3
n = 3
memo = {}
print(f"Total Paths: {countPaths(m, n, memo)}")



#Task-2
def printPaths(m, n, result):
    if(m == len(grid)-1 and n == len(grid[0])-1):
        result += f"{grid[m][n]} "
        print(result)
        return
    if(m >= len(grid) or n >= len(grid[0])):
        return
    result += f"{grid[m][n]} "
    printPaths(m, n+1, result)
    printPaths(m+1, n, result)

print("Trejectories:")
grid = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]] 
printPaths(0, 0, "")