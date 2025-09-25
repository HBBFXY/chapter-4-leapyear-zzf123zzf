def check_leap_year():
    """判断闰年的主函数"""
    try:
        year = int(input("请输入年份: "))
        
        # 使用单行逻辑判断
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            print(f"{year}年是闰年")
        else:
            print(f"{year}年不是闰年")
            
    except ValueError:
        print("错误：请输入有效的数字年份！")

# 运行程序
check_leap_year()
if __name__ == "__main__":
    main()
