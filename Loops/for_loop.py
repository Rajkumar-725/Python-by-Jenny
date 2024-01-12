"""
syntax: for variable_name in sequence:
            statement(x)
"""

name=['Raj', 'Jenny', "Hello", "Geetu"]

for i in name:
    print(i)



print('\n\n')

name2=("Raj")
for j in name2:
    print(j)


print("\n\n\n")
name3=("Raj", "Geet", "Saku")
for k in name3:
    print(k)
    if k=='Raj':
        print("Hello dear")


            #PRINTING SQUARES OF GIVEN NUMBER
print('\n\n\n\n')
list=[1,2,3,4,6,8]
for square in list:
    print(square ** 2)



            #STORING SQUARES IN ANOTHER LIST
sq=[]
for square in list:
    sq.append(square ** 2)       #It stores the squares values to sq list.
print(sq)