'''
check how many times (T,R,U,E,L,O,V,E) these letters come in your and yours partner name
            add how many times T,R,U,E and L,O,V,E and write it is 2 1 or 9 1

'''

boy=input("Enter boy name")
girl=input("Enter girl name")

concatinate= boy + girl

#   .lower() :converts upper_case into lower_case
concatinate.lower()

#   .count(target_value)    :It checks, how many times the target value or argument is +nt in given string
T = concatinate.count('t')
R = concatinate.count('r')
U = concatinate.count('u')
E = concatinate.count('e')
L = concatinate.count('l')
O = concatinate.count('o')
V = concatinate.count('v')
E = concatinate.count('e')

# print(type(T))            :type=int
true = T + R + U + E    
love = L + O + V + E

print(f"Your love score is {true}{love} %, you will rock")





