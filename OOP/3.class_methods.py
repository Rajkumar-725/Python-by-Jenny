# ADDING METHODS TO THE CLASS

'''
METHODS: actions we perform on the attribute are known as method.
'''

class Instructor:
    followers =0    # class object variable
    def __init__(self, name, address):
        self.name = name
        self.address=address
        # self.followers=0


    def display(self):
        print(f"Hello dear {self.name}")    # name is fetched from init function.

Instructor_1=Instructor("jenny", "mumbai")
print(Instructor_1.name)
print(Instructor_1.address)
print(Instructor_1.followers)


print('\n\n\n')
Instructor_1.display()      # method call
print('\n')
print(Instructor_1.display())     # prints return value
# Instructor_2.display()
