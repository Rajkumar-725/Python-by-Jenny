#   PYTHON IS OBJECT ORIENTED PROGRAMMING LANGUAGE
#    i.e, every thing is considered as a object
#   Here, data_type initialisation is optional, python itself figureout the type of data.

#   Data_types are considered as classes, and variable(that we create) are known as object or instance of these classes

#type() :used to check data_type of variable.


#int        :it stores all +ve and -ve values, There is no limit range.
#float      :Includes floating number.
#string     :includes sequence of characters
#boolean    :includes true and false only
a=10
b=23.2
print(a+b)
print(type(a))      #shows data_type of a

name="Jenny"
print(type(name))   #string data_type
print(name[0])      #for fetching individual characters from the string.
print(name[3])




                            # ADDING SUFFIX 
#   0b or 0B :gives binary number
#   0o or 0O :gives octal number
#   0x or 0X :gives hexa_decimal number
print(0b10)     #gives binary of 10
print(0b10011)     #gives binary of 10011

print(0o1023)     #gives octal of 10
print(0X12)         #gives hexa_decimal number of 12


                #BOOLEAN
print("\n\n\n")
a=1
b=3
var=a<b
print(var)
print(type(var))