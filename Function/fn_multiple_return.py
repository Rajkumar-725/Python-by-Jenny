# A fn can return multiple items at once 

# FINDING MEAN, MEDIAN AND MODE FROM LIST

import statistics       #python have inbuilt fn that can calculte mean median and mode, just import and use.

def mean_med_mode(list1):
    # return statistics.mean(list1), statistics.median(list1), statistics.mode(list1)       # It return as a tuple
    return [statistics.mean(list1), statistics.median(list1), statistics.mode(list1)]       #It returns as list


result = mean_med_mode([2,4,5,74,3,76]) 
a,b,c = mean_med_mode([2,4,5,74,3,76])      # More than 1 statement is returned at a time.
print(result)
print(f"Mean is {a}, Median is {b}, Mode is {c}")



print('\n\n\n\n')
# FUNCION WITH MULTIPLE RETURN STATEMENT

def add(a,b):
    if a==0 and b==0:
        return      #it returns none
    else:
        return a+b
    
print(add(9,8))
print(add(0,0))