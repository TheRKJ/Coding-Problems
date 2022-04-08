def fib(n):
    if(n <= 2):
        answer = 1
    else:
        answer = fib(n-1) + fib(n-2)
    return answer

for i in range(10):
    print(fib(i+1), end=" ")