#  Program to calculate average height from a list of height.

'''
condition :     1.don't use 
                        sum()
                        len()
                2. take input  from user
                3. Output  should be rounded to nearest whole number
''' 
height= input("Enter height separated by blank space:")
height_list=height.split(" ")


#For finding length of the list.(without using len function)
count=0
for height in height_list:
    count=count+1
print(f"you have given {count} numbers")

for i in range(count):      #It iterates the number from 0 to count {range function generate number from 0 to count variable}
    height_list[i] = int(height_list[i])    #converting string into integer datatype.
print(height_list)


# For finding sum.
total=0
for i in height_list:
    total+=i
print(total)

average= total/count
print(f"your average is {average}")
print(f"After roundoff {round(average)}")

