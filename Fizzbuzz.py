# fizz : 3으로 완전히 나누어 떨어지는 경우
# buzz : 5으로 완전히 나누어 떨어지는 경우
# fizzbuzz : 15로 완전히 나누어 떨어지는 경우

for number in range(1,101):
    if number % 15 == 0:
        print("Fizz Buzz")
    else:
        if number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)
    