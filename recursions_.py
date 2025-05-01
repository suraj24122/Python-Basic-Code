# 0 1 2 3 5 8 13

# fib(0) = 0;
# fib(1) = 1;
# fib(2) = fib(0) + fib(1);
# fib(3) = fib(1) + fib(2);
# fib(2) = fib(2) + fib(3);
# fib(n) = fib(n-1) + fib(n-2);

def fib(n):
    # return fib(n-2) + fib(n-1);
    #base case of recursion
    if(n ==0 or n == 1):
        return n;
    return fib(n-1) + fib(n-2); #recursive case of recursion

print(fib(6)); # 8
