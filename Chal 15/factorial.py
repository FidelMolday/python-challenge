def factorial_iterative(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Example usage:
number = 5
print(f"Factorial of {number} (iterative): {factorial_iterative(number)}")


#Iterative Method
def factorial_iterative(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Example usage:
number = 5
print(f"Factorial of {number} (iterative): {factorial_iterative(number)}")
