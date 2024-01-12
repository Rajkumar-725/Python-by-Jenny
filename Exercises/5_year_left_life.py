'''
find out how many days, week, month we have if we live until 90 yrs.

input: your current age.
output: you have __ days, __ weeks, and __ months left.
'''

age=int(input("Enter your age"))
print(f"Your age is {age}")

remain=(90-age)       #in yrs
days=remain*365
month=remain*12
week=remain*52

print(f"You have {days} days, {week} week and {month} months left")