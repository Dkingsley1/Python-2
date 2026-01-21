def fibonacci(n):
    # Base cases: F(0)=) and F(1)=1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # recursive case: F(n) = F(n-1) + F(n-2)
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Test cases
print("6th Fibonacci number:", fibonacci(6)) # Expected: 8