'''
Control statements;
          break       :Terminate the loop
          continue    :Skip statements{Skips all the statements after 'continue' and control will go at beginning of the loop}
          pass        :Do nothing {Defines an empty function or loop}

    pass    :Its just like a placeholder for future functions.
'''

for i in range(1,11):
    pass        # used to remove the error caused by blank loop or blank function

print('\n\n\n')
count=0
for i in range(1,11):
    print(i)
    if i==6:
        pass
