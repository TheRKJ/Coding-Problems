def howString(target_string, path):
    ans = 0
    if(target_string == ""):
        paths.append(path)
        return 1
    for i in range(len(arr)):
        if(target_string.startswith(arr[i])):
            ans += howString(target_string[len(arr[i]):], path+" "+arr[i])
            
    return ans
    
arr = ['rk', 'rak', 'ke', 'esh', 'rake']
target_string = "rakesh" 
paths = []
print("Total paths:", howString(target_string, ""))
print("Trejectories:")
for path in paths:
    print(" ",path)