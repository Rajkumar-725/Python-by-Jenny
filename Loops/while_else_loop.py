'''
while condition:
        statement(1)
else:
        statement(2)


Note: It works on list and touples also
      Else statement is only executed if while loop is completed successfully(not by forcefully terminating using break etc.)

'''

"""
                SENTINEL VALUE
        It is spl value used to terminate the loop
        If working on positive integer --> sentinel value is -1
"""

count=0
while count<5:
    print("hello")
    count +=1
else:
    print("Out of loop")


number=0
print('\n\n\n')
while number<6:
    print("How are you")
    if number==4:
        break
    number +=1
else:
    print("Statement 2")        # here, loop is forcefully terminating so else block is not executed
print("Out of loop")



print('\n\n\n\n')
# ASSIGNMENT: Sum all the input values(-ve as well as +ve) until user inputs 0.
total=0
n=int(input("Enter number {0 to quit}"))
while n!=0:
    total+=n
    n=int(input("Enter number {0 to quit}"))

print(f"your sum of total input is {total}")