"""
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.

A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

from eutil import clock


def month_days(days_in_year):
    assert days_in_year in [365, 366]
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if days_in_year == 366:
        month_days[1] += 1
    return month_days


@clock 
def main():
    day  = 2
    first_sundays = 0
    for year in range(1900, 2001):
        days_in_year = 365
        if year % 4 == 0 and year != 2000:
            days_in_year = days_in_year + 1  # leap year
        days_by_month = month_days(days_in_year)
        day = day % days_in_year
        for month in range(12):
            days_in_month = days_by_month[month]
            day = (day + 7) - days_in_month
            while day <= days_in_month:
                day += 7
            if (day - days_in_month) == 1 and year > 1900:
                first_sundays += 1
    return first_sundays
            
"""
An interesting note is that Gauss has a cool formula for the calculation 
of the day of the week of January 1st for any given year which can be 
extended for more general purposes: 
http://en.wikipedia.org/wiki/Determination_of_the_day_of_the_week#Formulas_derived_from_Gauss.27s_algorithm
"""

if __name__ == '__main__':
    main()










