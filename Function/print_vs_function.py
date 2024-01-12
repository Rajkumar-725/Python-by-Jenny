'''
def add(a,b):
    c=a+b
    return c

a = int(input("Enter number a"))
b = int(input("Enter number b"))
output=add(a,b)
print(output)

'''


# REUSE OF RETURN OF 1st FUNCTION INTO 2nd FUNCTION AS AN ARGUMENT
print('\n\n\n')
def addition1(a,b):
    z = a+b
    return z

def addition2(x):
    return x+1
out1 = addition1(7,5)       # fn 'addition1' is called here.        #out1 becomes 12
print(out1)

final = addition2(out1)     #result of 'function1' is reused as a argument for another fn2
print(f"After 2nd function calling {final}")
