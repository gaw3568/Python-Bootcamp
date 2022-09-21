year = int(input("Enter a year to check the leap year : "))

""" 
1. 해가 4로 나눌때 나머지가 0으로 떨어지면 윤년이다
2. 4로 나누어떨어지지만 100으로 나누었을 때, 나머지가 0이면 윤년이 아니다.
3. 400으로 나누어떨어지면 윤년이다.
"""

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} year is Leap Year")
        else:
            print(f"{year} year is not Leap Year")
    else:
        print(f"{year} year is Leap Year")
else :
    print(f"{year} year is not Leap Year")