#NESTED LIST :List within a list
roll=[1,2,3,4,[100,122,231],12,13]
print(roll)

#inner list is considered as a single element   {basically index of outer list store reference of the inner list.}
print(len(roll))

print(roll[4])
print(roll[-2])         #starts from end side
print(roll[4][1])       #accessing inner list elements