'''
RANGE:  generates a series of numbers. {default 0 to upper_lmt  (upp_lmt not included)}

Syntax:     range(start, stop, step_size)
    start: starting position --> optional{default 0}
    stop: Ending position --> mandatory
    step_size: How many steps you want to jump -->optional{default is 1}    (note:it can't be zero)
All the arguments must be integer.(not string, boolean etc)

'''

a=range(0,22,2)

for i in a:
    print(i)

print('\n\n\n')
# Adding number from 1 to 100 and find their sum.
b = range(0,101)
total=0
for i in b:
    total = total+i
print(total)
