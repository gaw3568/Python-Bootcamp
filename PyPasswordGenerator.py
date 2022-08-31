import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

total_pswd = []

# random.choice() 함수 사용
#   total_pswd += random.choice(letters)
#   total_pswd += random.choice(symbols)
#   total_pswd += random.choice(numbers)

for num in range(0,nr_letters):
    index = random.randint(0, len(letters) - 1)
    total_pswd.append(letters[index])

for num in range(0,nr_symbols):
    index = random.randint(0, len(symbols) - 1)
    total_pswd.append(symbols[index])

for num in range(0,nr_numbers):
    index = random.randint(0, len(numbers) - 1)
    total_pswd.append(numbers[index])

# list형태를 string형태로 변환시키기
str_pswd = "".join(total_pswd)
print(f"(Easy version) Your password is : {str_pswd}")

# 쉬운 버전의 비밀번호의 각 위치를 무작위로 바꾸기
random.shuffle(total_pswd)
str_pswd = "".join(total_pswd)

print(f"(Hard Version) Your password is : {str_pswd}")

# for num in range(0,len(total_pswd)):
#     index = random.randint(0, len(total_pswd) - 1)
#     hard_pswd += total_pswd.pop(index)