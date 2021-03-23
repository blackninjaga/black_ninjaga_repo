def is_year_leap(year):
    if (year % 4 == 0):
        if (year % 100 == 0):
            if (year % 400 == 0): return True
            else: return False
        else: return True
    else: return False

def days_in_month(year, month):
    if (month in [1,3,5,7,8,10,12]):
        return 31
    elif (month in [4,6,9,11]):
        return 30
    elif (month == 2):
        if (is_year_leap(year)):
            return 29
        else: return 28
    else: return None

def day_of_year(year, month, day):
    if year < 0 or month not in range(1,13) or day not in range(1,days_in_month(year, month)+1):
        return None
    else:
        day_num = 0
        for m in range(1, month):
            day_num += days_in_month(year, m)
        day_num += day
        return day_num

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
	yr = test_data[i]
	print(yr,"->",end="")
	result = is_year_leap(yr)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")

test_years =[2000, 1932, 1345, 2021]
test_months = [12, 8, 9, 2]
test_days = [31, 24, 18, 29]
test_results=[366, 237, 261, None]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    dy = test_days[i]
    print (yr, mo, dy, "->", end="")
    result = day_of_year(yr, mo, dy)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")