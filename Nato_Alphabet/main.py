import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {value.letter:value.code for (key, value) in df.iterrows()}
print(nato_dict)

# 발생하는 Error를 exception으로 catch
is_not_error = False
while not is_not_error:
    try:
        user_input = input("Enter a number : ").upper()
        nato_list = [nato_dict[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        print(nato_list)
        is_not_error = True