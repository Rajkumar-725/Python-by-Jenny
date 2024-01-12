'''                PASSWORD GENERATOR
OUTPUT :        Welcome message.
                How many letter would you like in your password.
                How many symbols would you like in your password.
                How many numbers would you like in your password.
        generate a password on the basis of above info.
                
'''

import  random


# Instead of making whole list of uppercase and lowercase Alphabet, use this
letter=[]
for i in range(ord('a'), ord('z')+1):
    letter.append(chr(i))
for i in range(ord('A'), ord('Z')+1):
    letter.append(chr(i))
print(letter)
print(type(letter))


# For writing number from 0 to 9.
number=[]
for i in range(10):
    number.append(i)
    number[i]=str(number[i])
print(number)

# special symbols.
symbol=['!','@','#','$','%','&','*','(',')','+']





print("Welcome to the password Generator")
let = input("How many letter would you like in your password: ")
sym = input("How many symbols would you like in your password: ")
num = input("How many numbers would you like in your password: ")


password=[]           # password list.

#for letters.
for i in range(1, let+1):
    char = random.choice(letter)        # Chooses any random number from the letter list.
    print(type(char))
    password += char        #concatinating password and string list (since both are string)

#for symbols
for i in range(1, sym+1):
    char1 = random.choice(symbol)        # Chooses any random number from the symbol list.
    password += char1        #concatinating password and symbol list (since both are string)

for i in range(1, num+1):
    char2 = random.choice(number)        # Chooses any random number from the number list.
    password += char2        #concatinating password and number list (since both are string)

print(password)