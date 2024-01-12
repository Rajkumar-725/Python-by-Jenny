# local scope: means its meaning only reflected within the funcion.
# global scope: means its meaning is reflected throughout the program.
# block scope: it is reflected and used within that block of code only, Note: python doesn't have block scope.


a=8     #global variable
def number():
	# a=222     #local variable
	def number2():  # local funcion 
		print(f"The value within number2 is {a}")
	number2()   #fn call

	# a=5         # local variable
	# print(f"In number {a}")
	

number()    #fn call