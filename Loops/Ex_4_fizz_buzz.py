'''
        FIZZ BUZZ JOB INTERVIEW QUESTION

Question:   Write a number from 1 to n.
        cond:   if number is divisible by 3 --> print 'Fizz'
                if number is divisible by 5 --> print 'Buzz'
                if number is divisible by 3 as well as 5 --> print 'FizzBuzz'

'''
num = range(0,101)

for i in num:
    if num[i]%3 ==0 and num[i]%5 == 0:
        print("FizzBuzz")
    elif num[i]%3 == 0:
        print("Fizz")
    elif num[i]%5 == 0:
        print("Buzz")
    else:
        print(num[i])
    
