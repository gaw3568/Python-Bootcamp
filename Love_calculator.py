print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()

def cnt_letter(name,num):
    if num == 1:
        cnt_t = name.count("t")
        cnt_r = name.count("r")
        cnt_u = name.count("u")
        cnt_e = name.count("e")
        cnt_true = cnt_t + cnt_r + cnt_u + cnt_e
        return cnt_true
    elif num == 2:
        cnt_l = name.count("l")
        cnt_o = name.count("o")
        cnt_v = name.count("v")
        cnt_e = name.count("e")
        cnt_love = cnt_l + cnt_o + cnt_v + cnt_e
        return cnt_love

combine_name = name1 + name2

cnt_true = cnt_letter(combine_name,1)
cnt_love = cnt_letter(combine_name,2)

score = cnt_true * 10 + cnt_love

if score < 10 or score > 90:
    print(f"your score is {score}, you go together like coke and mentos.")
elif 40 <= score <= 50:
    print(f"your score is {score}, you are alright together.")
else:
    print(f"your score is {score}.")