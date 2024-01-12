'''
Random Module  :It generate sudo random number


import random

randint(a,b)    :return integer no. b/w a and b                             a<= num <=b
randrange(a,b)  :return integer no. b/w a and b                             a<= num <b
random()        :retun floating no.                                       0.0<= num <1.0
uniform()       :return floating no.(retuns in paricular range)
choice()        :selects random item in a sequence
shuffle()       :shuffle any sequence
'''


import random
a=random.randint(1,3)
a=random.randrange(1,3)
a=random.random()
print(a)

list=[1,3,5,7,8]
print(random.choice(list))      #takes random element from the list
print(random.shuffle(list))     #shuffle the list randomly