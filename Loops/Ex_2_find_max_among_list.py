# Program to find maximum number from a list of number.
# cond: don't use max()
number= input("Enter your number separated by comma")
sp_number = number.split(',')

count = len(sp_number)



#for converting string into integer datatype
for i in range(count):
    sp_number[i] = int(sp_number[i])

print(sp_number)


#For finding maximum among number
maximum_number=sp_number[0]     #Assigning 0th index as maximum number
for target in sp_number:
    if target > maximum_number[i]:
        maximum_number = target

print(f"maximum number is {maximum_number}")

