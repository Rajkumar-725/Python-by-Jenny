'''
WAP to select a random name from a list of names and the person selected will pay for everybody bill.
'''

import random
name=input("Enter names separated by comma \n")

"""
        #BY USING CHOICE FUNCTION.

splitted_name = name.split(",")         #whenever, it found comma it splits the list
target= random.choice(splitted_name)
print(f"Bill is paid by {target}")
"""




        #WITHOUT CHOICE FUNCTION
#   .split("operator_through_which_list_is_splitted")

print(f"You have povided \t {name}")
splitted_name = name.split(",")         #whenever, it found comma it splits the list
print(f"Name after spllited \t {splitted_name}")

size=len(splitted_name)
# print(size)
selected = random.randint(0, size-1)    #select random element b/w given range
fetch=splitted_name[selected]       #fetch the element that is +nt in the selected.

print(f"The bill is paid by {fetch}")
