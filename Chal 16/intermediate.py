#sequential control
print('Hello')
print('How are you')
print('Welcome to Moldays Tech Academy')

#simple if statement
temperature = 35
if temperature > 30:
    print('It is a hot day.')

#if-else statement
value =int(input('Please enter an integer:'))
if value<10:
    print("value is less than 10")
else:
    print("value is greater than 10")       

#nested if statement
num_1 = float(input('Please enter a number:'))
if num_1 >= 0:
    if num_1 == 0:
        print('The number is zero.')
    else:
        print('This is a positive number.')

else:
    print("This is a negative number.")


    ##if-elif-else statement
temperature = 19
if temperature > 35:
    print('It is a hot day.')
elif temperature > 20:
    print('It is a good day')
else:
    print('Enjoy your day.')           