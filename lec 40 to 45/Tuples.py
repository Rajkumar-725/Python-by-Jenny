"""
TUPLES: store multiple items in a single variable.
      : It is similar to list in python or array in c language.
      : It uses small braces() instead of middle braces{}.

      :NOTE :TUPLE CAN'T BE MODIFIED OR CHANGED.
      :Iteration will be fast due to unchangable behaviour.
"""
name = ("Raju", "Geetu", "Saku")
age = (20,40,30)
mix = ("Raj kumar", 30, 45.23)      #mixed data_type is also possible

tuple1 = (10)     # It is not considered as a tuple.        Considered as a integer only
tuple2 = (10,)      # necessity cond is to put comma after element.

print(type(tuple1))
print(type(tuple2))

                            #PROPERTIES

print("\n\n\n")
print(name[2])          #Accessing individual index is possible
print(name[-2])         #Negative indexing is also possible

# name[1]="Raj kumar"     #tuple can't be modified
# print(name)

print('\n\n\n')         #Slicing is also possible
print(name[2:3])

print('\n\n\n')
num1 = ("Raj kumar", "Jenny lecture")
num2 = (11,22,33,44,55)
number = (num1, num2)       #nesting of tuple is also allowed 
print(number)
print(number[1])        # since, 0_index=num1 and 1_index=num2 

print('\n\n\n')
print(num1 + num2)      #concatinating is possible


print('\n\n\n')
                        # min() and max() is also allowed.
                        #   :note; we can't compare two different data_types
print(min(num2))
print(min(num2))
print(min(num2))
print(min(num1))



print('\n\n\n')
print(num2.count(22))           #counting within tuple  is also allowed
print(num2.index(44))           #It gives the indexing address of the target element



                #CONVERTING LIST INTO TUPLE
print('\n\n\n')
list=["Raj", 23, 56.7]
tuples=tuple(list)

print(type(list))
print(type(tuples))
print(tuples)


            # MATHEMATICAL OPETAIONS IS ALSO ALLOWED
print("\n\n\n")
tup5=("10,12")*4
print(tup5)
