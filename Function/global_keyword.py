# GLOBAL KEYWORD:  Used to modify the global variable from inside a function.
#               : Also used to create global variable fron inside a function 

a= 10   #global variable
def number():
    global a     # It means you are referring to global variable
    a=a+1
    # a=15    # local variable
    print(a)
number()    # fn call


print('\n\n\n')

def display():
    a=20
    def show():
        global a    # If no global variable found, it creates a global variable a and assign 30 to it.
        a=30
    print(f"Value before show funcion {a}")
    show()
    print(f"Value after show funcion {a}")

display()   # fn call
print(a)    #global var call
