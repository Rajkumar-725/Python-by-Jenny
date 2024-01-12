# CALCULATE THE NUMBER OF DAYS IN GIVEN MONTH 


def leap_year(year):
    if year%4 == 0:
        if year%100 == 0:
            # print("May be leap year...!")
            if year%400==0:
                # print("Leap year")
                return True     #true is returned b/c it means 1.
            else:
                return False
        else:
            # print("It is leap year")
            return True
    else:
        return False


def days_in_month(year, month):
    days_list=[31,28,31,30,31,30,31,31,30,31,30,31]
    if leap_year(year) and month==2:            #leap_year fn is called here.
        return 29
    else:
        return days_list[month-1]       #since index starts from 0


year = int(input("Enter year to check"))
month = int(input("Enter month number"))

print(days_in_month(year, month))


