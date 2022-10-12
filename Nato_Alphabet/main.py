import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {value.letter:value.code for (key, value) in df.iterrows()}

user_input = input("Enter a number : ").upper()

nato_list = [nato_dict[letter] for letter in user_input]
print(nato_list)