number1 =  int(input("Enter number 1:"))
number2 =  int(input("Enter number 2:"))
number3 =  int(input("Enter number 3:"))

max_number = 0

if ((number1 > number2) and (number1 > number3)):
    max_number = number1

if ((number2 > number1) and (number2 > number3)):
    max_number =  number2

if (number3 > number1 and number2 > number2):
    max_number =  number3

print(f"El numero mayo de los 3 es: {max_number}")



