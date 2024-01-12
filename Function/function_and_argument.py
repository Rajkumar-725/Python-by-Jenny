        # FUNCTION WITHOUT ARGUMENT.
def greet():            #function defining
    print("Hi Raj")
    print("Good to meet you")

print(greet())      #function calling


print('\n\n\n')

        # FUNCTION WITH ARGUMENT
def name(a):        #here 'a' is parameter or formal parameter
    print (f"Hi  {a}")
    print("Are you fine")

a=input("Enter your name")

#passing argument at runtime
print(name(a))      #here 'a' is argument or actual parameter

print(name("ram"))      #passing argument at compile time

# NOTE: PARAMETERS AND ARUMENTS MUST BE SAME IN NUMBER.(means if parameter is 2 then arguments must be 2)