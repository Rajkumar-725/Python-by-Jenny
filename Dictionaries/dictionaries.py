number={"Raj":97678}    #defining  the dictionry

num={"Raj":97678, 'shyam':84345, 'mohan':73489}    #defining  the dictionry with more than 1 key and values

#another way of defining dictionary {more than the previous one}
n={
    "Raj":97678,        #indentation is mandatory
    'shyam':84345,
    'mohan':73489,
    'Raj':677777            #due to duplication it overwrites the previous value
}       # 0 indentation is mandatory

print(number)   #note it is case  sensitive
print(num)
print(n)

print(num['shyam'])     #accessing individual key for value



print('\n\n\n')
#ANOTHER METHOD TO CREATE DICTIONARY {using dict function}

phone_num=dict({
    "Raj":97678,
    'shyam':84345,
    'mohan':73489,
    'Raj':677777
}     
)

print(phone_num)

phone_num["mohan"]=99999        #To update the values of keys.

# List is also allowed.
phone_num["Rohan"]={0000,22222,34444}        #To add new keys

#Nested dictioanry is also allowed.
phone_num["Geetu"]={"home":777777777, "office":6666666666}        #To add new keys
print(phone_num)

print(phone_num["Geetu"])   # Accessing each key to find values
print(phone_num["Geetu"]["home"])   # Accessing key inside key to find value of that key.


                #BY USING GET METHOD.
        #It doesn't show any error in case of key not found.
print(phone_num.get('Raj'))


print('\n\n')

# del phone_num["Raj"]        #It is used to delete the key.
# phone_num.pop("shyam")         # It is also used to delete but it also returns the deleted value{not key}.
# phone_num.clear()         # It is also used to delete all the dictionary value and doesn't return anything.

print(phone_num)
print('\n\n')
print(phone_num.keys())         # It is also used to access only keys from dictionary
print(phone_num.values())         # It is also used to access only values from dictionary
print(phone_num.items())         # It is used to print list of all the items in the form of tuples.


print('\n\n\n')
for i in phone_num:
    print(i)        #For accessing keys
    print(phone_num[i])     #For accessing values.



print('\n\n\n')
for i in phone_num.items():
    print(i)        #prints value pairs one by one.



print('\n\n\n')
#FOR COPYING 1 DICTIONARY INTO OTHER.
phone_number2 = phone_num.copy()
print(phone_number2)



print('\n\n\n')
#To find length of dictionary
print(len(phone_number2))