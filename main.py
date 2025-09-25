def check_leap_year():
    """判断闰年的主函数"""
    try:
        # 获取用户输入
        year_input = input("请输入年份: ")
        
        # 转换为整数（这里可能抛出ValueError）
        year = int(year_input)
        
        # 闰年判断逻辑
        if year % 4 == 0:  # 能被4整除
            if year % 100 == 0:  # 能被100整除
                if year % 400 == 0:  # 能被400整除
                    print(f"{year}年是闰年")
                else:
                    print(f"{year}年不是闰年")
            else:
                print(f"{year}年是闰年")
        else:
            print(f"{year}年不是闰年")
            
    except ValueError:
        print("错误：输入的不是有效的数字！")
    except Exception as e:
        print(f"发生错误：{e}")

# 运行程序
check_leap_year()
