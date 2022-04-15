def howSum(sum, path):
    ans = 0
    if(sum == 0):
        paths.append(path)
        return 1
    if(sum < 0):
        return 0
    for i in range(len(arr)):
        ans += howSum((sum - arr[i]), path+f"{arr[i]} ")
    
    return ans
    
arr = [2, 3]
sum = 7
paths = []
print("Total paths:", howSum(sum, ""))
print("Trejectories:")
for path in paths:
    print(" ",path)