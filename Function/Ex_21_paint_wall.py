# Find out how many cans is required to paint a wall

'''
requirement: length and breadth of wall, and per can coverage.
'''
import math     #for using ceil function

def paint_calc(length,breadth,can_coverage):
    area=length*breadth
    no_of_cans=area/can_coverage
    required_cans=math.ceil(no_of_cans)     #Round the number to upper bound
    print(f"you need {no_of_cans} no of cans")
    print(f"you need {required_cans} cans")

l= int(input("Enter length"))
b= int(input("Enter breadth"))
can= int(input("Enter can coverage"))

paint_calc(l, b, can)       #by positional argument
paint_calc(length=l,breadth=b, can_coverage=can)       #by keyword argument



