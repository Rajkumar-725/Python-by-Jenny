# Calculate sum of even number from 1 to 100. (including 1 and 100)

num=range(0, 101)

total=0
for i in num:
    if num[i]%2==0:
        total += num[i]
print(total)
