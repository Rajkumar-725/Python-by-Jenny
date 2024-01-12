''' RETURN STATEMENT: It is a spl statement that used inside a function only
                    : It is optional {default is none}
                    : It is the end of execution of fn {means after return no statement is ignored}
'''

def addition(a,b):
    c=a+b
    return c            # returns the value to the caller


print(addition(6,7))



print('\n\n\n')
# CONVERTING THE GIVEN NAME INTO TITLE CASE {eg: Sakshi Aggarwal}
def format_name(f_name,l_name):
    new_first_name = f_name.title()          # title function converts the given text into title case.
    new_last_name = l_name.title()

    print(f"{new_first_name, new_last_name}")
    return (f"{new_first_name, new_last_name}")



format_name("raj","kumar") #argument passing
format_name("SAKSHI","AGGARWAL") #argument passing

print('\n\n')
print(format_name("SAKSHI","AGGARWAL"))



