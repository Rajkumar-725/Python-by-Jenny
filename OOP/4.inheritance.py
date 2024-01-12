'''
Inheritance: It copy all the attributes and methods from 1 class to another class.
            : increases the reusability of code.

    'Base class' or 'Parent class' or 'Super_class' :     from where we can inherit the message. {also known as 'Parent class' or 'Super class'}
    'Deived_class' or 'child_class' or 'Sub_class'  :     which inherit property from base class.

SYNTAX:     class Derived_Class_Name(BaseClassName):
                class definition or statements.
'''

class Human:        # act as base class
    def eat(self):
        print("I can eat")
    def work(self):
        print("I can work")

class Male(Human):      # act as derived class
    def float(self):    #It can also store its own attributes
        print("I can float")

    def work(self):
        print("I can't go and work") # This is called overridding
# super funcion: Used to access the 'base attribute' as well as derived at a time.
        super().work

    # pass

# male_1 = male()
human_1 = Human()
human_1.eat()

print('\n\n')
male_1 = Male()
male_1.eat()     # here, name of class id "Human" not 'Male' b/c we just copy the reference.
male_1.float()
male_1.work()

