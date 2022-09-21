#Write your code below this line 👇
def prime_checker(number):
    isPrime = 0

    for num in range(2, number):
        if number % num == 0:
            isPrime += 1

    if isPrime == 2:
        print("It's a prime number")
    else:
        print("It's not a prime number")


#Write your code above this line 👆

#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
