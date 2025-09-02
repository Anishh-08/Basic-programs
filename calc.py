num1=float (input())
num2=float (input())
operator=input('Enter operator: + - * /')

if operator == '+':
    print (f'Sum of the two number is: {num1+num2}')
elif operator == '-':
    print (f'Subtraction of the two number is: {num1-num2}')
elif operator == '*':
    print (f'Multiplication of the two number is: {num1*num2}')
elif operator == '/':
    print (f'Division of the two number is: {num1/num2}')
else:
    print('Dont u know math operators stooooopid!')