'''
There are 4 types of argument:
            Default
            Positional
            Keyword
            Arbitary/ Variable length
'''

#POSITIONAL ARGUMENTS: (1st position argument is assigned to 1st position parameter, respectively for 2nd and so on)
def greet(name, dept):          #fn defining (with 2 parameters)
    print(f"Hi {name}")
    print(f"you are from {dept} department")

greet("Raj","Medical")      #fn calling
greet("Medical", "Raj")      #It gives incorrect order.


print('\n\n\n')
#KEYWORD ARGUMENT: specifies the argument to their parameter manually
greet(name="Raj", dept="CS")
greet(dept="CS", name="Raj")


print('\n\n')
#MIXTURE OF POSITIONAL AND KEYWORD ARGUMENT IS ALSO POSSIBLE.
greet("Sakshi", dept="Programming")
# greet(dept="Programming", "Sakshi")       #NOTE: order is must {Keyword arg should be after positioanl arg.}



# DEFAULT ARGUMENT: default argument is provided as a backup if no argument is passed at calling time.
print('\n\n')
def congrats(name, depart, sub="Electrical"):   #note: 1st provide non-default arg and then default argument
    print(f"Hello dear {name}")
    print(f"Are you freom {depart} department")
    print(f"you have to study {sub}")

congrats("Geet", "Science")     #here, it is also known as required argument.
congrats("Sita", "Medical", "Biology")      #If argument is passed then it overwrite the default  argument



print('\n\n\n\n')
def add(*number):   #It accepts the number and become touple {b/c touple is immutable}
    sum=0
    for i in number:
        sum+=i
    print(f"The sum of  number is {sum}")
add(5,3,7)
