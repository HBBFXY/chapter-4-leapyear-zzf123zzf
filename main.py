def is_leap_year(year):
    try:
        year = int(year)
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return "是闰年"
        else:
            return "不是闰年"
    except ValueError:
        return "输入错误"
if __name__ == "__main__":
    year_input = input()
    result = is_leap_year(year_input)
    print(result)
