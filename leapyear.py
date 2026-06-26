def is_year_leap(year):
    # Leap year if divisible by 4
    # but not divisible by 100,
    # unless also divisible by 400
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def days_in_month(year, month):
    # Days in each month (default for non-leap years)
    month_days = [31, 28, 31, 30, 31, 30,
                  31, 31, 30, 31, 30, 31]
    
    if month < 1 or month > 12:
        return None  # invalid month
    
    if month == 2 and is_year_leap(year):
        return 29
    return month_days[month - 1]

# Test cases
test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]

for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end=" ")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")
