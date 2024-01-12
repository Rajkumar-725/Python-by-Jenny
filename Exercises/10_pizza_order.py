'''
                PIZZA ORDER PROGRAM
        small pizza :100
        medium      :200
        large       :300
    pepperoni for small pizza =30
    pepperoni for medium or large pizza =50
Extra cheese for any size =20
'''

inp=input("Which pizza do you want \n s=small, m=medium, l=large ")

bill=0
if(inp=='s' or inp=='S'):
    print("you ordered for small pizza of Rs 100")
    bill+=100
    
elif(inp=='m' or inp=='M'):
    print("you ordered for medium pizza of Rs 200")
    bill+=200

elif(inp=='l' or inp=='L'):
    print("you ordered for large pizza of Rs 300")
    bill+=300


pepperoni=input("Do you wna pepperoni: y or n ? ")
if pepperoni=='y' or pepperoni=='Y':
    if(inp=='s' or inp=='S'):
        bill+=30
    if(inp=='m' or inp=='M' or inp=='l' or inp=='L'):
        bill+=50
        

cheese=input("Do you wna cheese y or n ? ")
if cheese=='y' or cheese=='Y':
    bill+=20

print(f"Your Final Bill is {bill}")