''' round(number, no_of_digits) :used to round off the given number to nearest integer
                numnber         :given number
                no_of_digits    :upto which term you want to round off.     {;It is optional}   (default is 0)
'''

print(round(7))             #type int
print(round(7, 2))          #type int
print(round(7.4565))        #type int
print(round(7.45653, 3))    #type float
print(round(7.45653, 0))    #type float

# If tie-breaking, then it return to the nearest even integer
print(round(7.5))           
print(round(6.5))           

#If second arg. is -ve
# THEN, round off is according to the  10^-(second arg.) rule
print(round(823, -1))           #here, 10^-(-1)  =10 , closest multiple of 10 in given number is 820
print(round(826.44, -1))           #here, 10^-(-1)  =10 , closest multiple of 10 in given number is 830
print(round(826.44, -2))           #here, 10^-(-2)  =100 , closest multiple of 100 in given number is 800
print(round(826.44, -3))           #here, 10^-(-3)  =1000 , closest multiple of 1000 in given number is 1000
print(round(826.44, -4))           #here, 10^-(-4)  =10000 , closest multiple of 10000 in given number is not +nt, hence 0


print("\n\n\n")
#IF NUMBER IS -VE
print(round(-12.56))
print(round(-12.2345, 1))
print(round(-12, -1))

print("\n\n\n")
print(round(8/3))
print(round(8/3, 1))

