#converting temperature from fahrenheit to celsius
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Example usage:
celsius = float(input("Enter temperature in Celsius: "))
converted_temp = celsius_to_fahrenheit(celsius)
print(f"{celsius} degrees Celsius is equal to {converted_temp} degrees Fahrenheit.")
