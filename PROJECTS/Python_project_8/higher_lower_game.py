import intro_art
import database
import random

print(intro_art.intro)      # accessing value from another file.

member1 = random.choice(database.data)
member2 = random.choice(database.data)
# print(member1)
# print(member2)

def account_info(member):
    name = member['name']
    description = member['description']
    country = member["nationality"]
    print(f"Choice:   This is {name}, a {description} from {country}")

account_info(member1)     #fn call
print(intro_art.vs)
account_info(member2)     #fn call


guess = int(input("Which have more follower, Type '1' or '2' : "))
follower_count_1 = member1["follower_count"]        #accessing value from the picked dicionary
follower_count_2 = member2["follower_count"]        #accessing value from the picked dicionary
# print(follower_count_1)
# print(follower_count_2)
points=0        #addigning a point variable to store the score of winner.
if follower_count_1 > follower_count_2 and guess==1:
    points +=1

elif follower_count_1 < follower_count_2 and guess==1:
    print


