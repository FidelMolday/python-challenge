def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def compute_factorials(numbers):
    results = []
    for num in numbers:
        results.append(str(factorial(num)))
    return ', '.join(results)

# Example usage:
if __name__ == "__main__":
    # Input numbers for which factorial needs to be computed
    numbers = [5, 3, 7, 1, 9]
    
    # Compute factorials
    results = compute_factorials(numbers)
    
    # Print results
    print(results)
