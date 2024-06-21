def evaluate_expression(expression):
    try:
        result = eval(expression)
        print(f"Result: {result}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    print("Enter a mathematical expression:")
    expression = input()
    evaluate_expression(expression)
