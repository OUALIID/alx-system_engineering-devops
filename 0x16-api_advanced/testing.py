def factorial(n):
    if n == 0:
        return 1  # Base case: factorial of 0 is 1
    else:
        return n * factorial(n - 1)  # Recursive case

result = factorial(5)  # This will calculate 5! (5 factorial)
print(result)  # Output: 120
