                #   VARIABLE NAMING RULES
#   variable name should be meaningful
#   only include alpha_numeric character(a~z)(A~Z)(0~9)
#   No special symbol is allowed
#   name must start either with a letter or underscore only

'''
FOR MULTI_VARIABLE NAME

CAMEL CASE     :Every word other than 1st word start with capital letter. (myName) (myVariableName) etc...
PASCAL CASE    :Each word starts with capital letter.  (MyName) (MyClassWork) etc...
SNAKE CASE     :Each word separated by underscore. (my_name) (my_class_teacher)  etc...
'''



name=input("Enter name")
age=input("Enter age")
print(name + age)
#len()  :used to find length of string only
length=len(name)
print(length)

#or it can be written as
print(len(name))