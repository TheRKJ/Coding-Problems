def fib(n,memo):
    if n in memo:
        return memo[n]
    elif n <=2:
        answer = 1
        memo[n]=answer
    else:
        answer = fib(n-1,memo) + fib(n-2,memo)
        memo[n] = answer
    return answer

memo={}
for i in range(99,100):
    print(fib(i+1,memo), end=" ")