def factorial(n):
    if n == 0:
        return 1
    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial(n-1)

    # Test cases
    print("Factorial of 5:", factorial(5)) # Expected: 120
    print("Factorial of 0:", factorial(0)) # Expected: 1