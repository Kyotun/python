#Calculate days in the month according to the years attribute -> is leap or not
#If a year is a leap year, february contains 29 days.
#Doesn't matter to the other months. They always contains the same amount of days.

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and is_leap(year=year):
        return 29
    else:
        return month_days[month - 1]

months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

print("Hey, welcome to the days in month calculator!")

year = int(input("Please enter the year: "))
month = int(input("Please enter the month: "))

if month not in months:
    print("\nYou entered an invalid month.")
    print("Month should be in range [0,12]\n")
else:
    days_in_month(year=year, month=month)