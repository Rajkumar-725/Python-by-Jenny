            # ADDING ATTRIBUTES TO THE CLASS 
# Task of a constructor: Assign values to the data members of a class when an oject is created 
                        # :Allows us to specify what would happen when we create an object 
                        # :we can initialise the members while creating 



'''
self: refers to the actual object on which we are calling the fn.
    : It is not a parameter.
    : It is a keyword to bind the onject attribute to the argument received.
'''
class Instructor:
    def __init__(self):     # used to initialise the data-members of class while creating an onject.
        print("Creating a new onject")

instructor_1 = Instructor() #here, 'self' is 'instructor_1'     {assigning 'instructor_1' attribute}
instructor_2 = Instructor() #here, 'self' is 'instructor_2'     {assigning 'instructor_2' attribute}



print('\n\n\n')
class Students:
    def __init__(self, instructor_name, address):      #here, instructor_name and address is parameter
        self.name=instructor_name
        self.address=address
        self.followers=0    # we can set default value to the attribute 

student_1=Students("jenny","mumbai")
print(student_1)
print(student_1.name)
print(student_1.followers)

student_2=Students("Raj kumar","Bihar")
student_3=Students("Sakshi Aggarwal","Uttar Pradesh")
print(student_2.name)
# print(student_3.name)
print(student_3.followers)
print(f"The name is {student_3.name} and  address is {student_3.address}")
