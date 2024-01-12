num1 = int(input("Enter first number: "))
print("+\n-\n*\n/")
operator = input("Select any one: ")
num2 = int(input("Enter second number: "))

def calculator(num1, num2):
    if operator =='+':
        number = num1+num2
    elif operator =='-':
        number = num1-num2
    elif operator =='*':
        number = num1*num2
    elif operator =='/':
        number = num1/num2
    return number    

num1 = calculator(num1, num2)       #final value act as a first number for 2nd loop.
print(num1)
further = input("Do you wnna continue with the answer value, Type 'yes' or 'no' :")

while further=="yes":
        num1 = calculator(num1, num2)       #final value act as a first number for 2nd loop.
        print("+\n-\n*\n/")
        operator = input("Select any one: ")
        num2 = int(input("Enter second number: "))
        calculator(num1,num2)
        print(num1)
        further = input("Do you wnna continue with the answer value, Type 'yes' or 'no' :")
else:
     print("Thanks for using")
num1=0
