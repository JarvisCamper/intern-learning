num1 = input('Enter the first number: ')
num2 = input('Enter the second number: ')

print('Choose the operation you need: +, -, *, /')
operation = input('Enter the operation you need: ')

if operation == '+':
    result = int(num1) + int(num2)
elif operation == '-':
    result = int(num1) - int(num2)
elif operation == '*':
    result = int(num1) * int(num2)
elif operation == '/':
    if int(num2) != 0:  # Need to check integer value
        result = int(num1) / int(num2)
    else:
        result = 'Error: Division by zero is not allowed'
else:
    result = 'Invalid operation'

print('Result is:', result)
