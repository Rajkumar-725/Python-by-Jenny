'''
The statement of "else" block is executed only if "for" loop is executed successfully(should not be terminated before completion using break or condition failure).

Syntax:     for var_name in sequence/touple/list:
                    statement(s1);
            else:
                    statement(s2);

'''

number=[1,3,4,5,6,8,0,12,34,56]
for i in number:
    print (i)
else:
    print("Successfully completed")

#Here, else block is not executed
print('\n\n\n')
for i in number:
    print (i)
    if i==0:
        break
else:
    print("Successfully completed")

print("You are out of loop")
    

#Generally used in these type of cases. 
print("\n\n\n")
tuple1=(1,2,4,56,78,4,34,54)
for i in tuple1:
    if i%6==0:
        print (i)     
else:
    print("No number is divisible by 6")


print("\n\n\n")
tuple1=(1,2,4,6,78,4,34,54)
for i in tuple1:
    if i%7==0:
        print (i)     
else:
    print("No number is divisible by 6")
