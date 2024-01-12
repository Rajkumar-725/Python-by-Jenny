'''
NOTE: IT IS AVAILABLE IN UPPER VERSION i.e, version~3.6
f-string    :string are prefix with f
            :means formatted string
            :just write the variables into curly braces {}
                in braces :we write the value that are going to be replaced with the value
                It can also include expressions.
'''

name="Raj"
age=20
height=2.5

print("My name is " + name, " My age is " + str(age))
print("My name is " , name, " My age is " ,age)

print(f"My name is {name} and  My age is {age}")
print(f"My name is {name} and  My age is {age*2}")