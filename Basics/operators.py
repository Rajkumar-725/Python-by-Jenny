'''
Arithematic 
Comparision (Relational)
Logical
Bitwise
Assignment
Identity
Membership
'''

                                     #ARITHEMATIC
#   ** :denotes power
print(2**3)

'''
         #PRECEDANCE    :PEMDAS                     associtivity
parenthesis         ()                              
Exponential         **                              R --> L
mutiply             *  /  //  %                     L --> R             // --> flow division
add                 +                               L --> R
substract           -                               L --> R
'''



                                    #COMPARISION
                # LHS must have a name of memory location (eg. a=5)
        




                                    #BITWISE
                # first it convert the given value into binary and then apply the operators
'''
and                 &
or                  |
xor                 ^
not(compliment)     ~           :it reverses the bits [{0 into 1} and {1 into 0}]
left shift          <<          :in left shift we gain bits
right shift         >>          :in right shift we loose bits
'''

a=5         #bin 0101
b=4         #bin 0100
print(a & b)        # & :means both 1 then 1 otherwise 0, therefore(ans 0100) i.e, in decimal =4
print(a | b)        # | :means both 0 then 0 otherwise 1, therefore(ans 0101) i.e, in decimal =5
print(a ^ b)        # ^ :means both bits same= 0, otherwise 1, therefore(ans 0001) i.e, in decimal =1
print(~a)           # ~ :gives 1010 , therefore gives -6 in decimal
print(a<<2)         # It left shifts the binary number of 5 by 2 bits and convert the result into decimal





                                    #IDENTITY OPERATORS :compare objects that both are same or not, or share same memory location
#   id() :used to check id of the object or variable

#          types    : is            ;gives true if memory location is same
#                   : is not        ;gives false if memory location are same
print('\n\n\n')
print(id(a))
print(id(b))
print(a is b)
print(a is not b)




print("\n\n\n\n")
                                    # MEMBERSHIP OPERATOR :checks that the character or value is +nt in sequence or not.
        # types     :in         ;returns true when target value found in the sequence
        #           :not in     ;returns false when target value found in the sequence
a="Geetanjali"
b=[1,5,2,6,4,23]
print('j' in a)
print("Geet" in a)
print("Geet" not in a)

print('\n')
print(10 in b)
print(23 in b)