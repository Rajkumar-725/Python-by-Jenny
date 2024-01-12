'''
1st check, It is disible by 4 or not
                divisible     :may be leap yr
                                 check :divisible by 100
                                             yes: shall be a leap yr
                                                    check: divisible by 400 or not
                                                                yes:Leap yr
                                                                no :Not leap yr
                                             no : leap yr

                not divisible :definetely not a leap yr
'''

year=int(input("Enter year to check"))
print(f"Your year is {year}")

if year%4 == 0:
    if year%100 == 0:
        print("May be leap year...!")
        if year%400==0:
            print("Leap year")
        else:
            print("No leap yr")
    else:
        print("It is leap year")

else:
    print("Definetely not a leap year")