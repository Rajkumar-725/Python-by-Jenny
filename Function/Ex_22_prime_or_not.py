# Checks the given number is prime or not.
'''prime number: no divisible by 1 or itself'''

def check(number):
    for i in range(2,number):
        if number%i==0:
            print("Number is not prime")
        
        else:
            print("Number is prime ")
        break

number = int(input("Enter your number"))
check(number)
