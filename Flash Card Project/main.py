from tkinter import messagebox
from pandas import *
from tkinter import *
import random

#------------------------READ Data------------------------#
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
data_dict = {}

#------------------------check word------------------------#
def check_exist_words():
    global data_dict
    try:
        data = read_csv("data/words_to_learn.csv")
    except FileNotFoundError:
        first_data = read_csv("data/french_words.csv")
        data_dict = first_data.to_dict(orient="records")
    except errors.EmptyDataError:
        return 1
    else:
        data_dict = data.to_dict(orient="records")

#------------------------Learn Button------------------------#
def learn_word():
    if check_exist_words() == 1:
        print("없어요 단어가")
    else:
        data_dict.remove(current_card)
        new_data_csv = DataFrame(data_dict)
        new_data_csv.to_csv("data/words_to_learn.csv", index=False)

        choose_random_card()

#------------------------Play Button------------------------#
def choose_random_card():
    if check_exist_words() == 1:
        print("없어요 단어가")
    else:
        global current_card, reset_time
        screen.after_cancel(reset_time)
        current_card = random.choice(data_dict)

        canvas.itemconfig(canvas_image,image=card_front)
        canvas.itemconfig(card_title, text="French", fill="black")
        canvas.itemconfig(card_word, text=current_card["French"], fill="black")
        reset_time = screen.after(3000, change_language)

#------------------------Play Button------------------------#
def change_language():
    if check_exist_words() == 1:
        print("없어요 단어가")
    else:
        canvas.itemconfig(canvas_image,image=card_back)
        canvas.itemconfig(card_title, text ="English", fill="white")
        canvas.itemconfig(card_word, text =current_card["English"], fill="white")

#------------------------UI SETUP------------------------#
screen = Tk()
screen.title("Flash Card Project")
screen.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
reset_time = screen.after(3000,change_language)

canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
# 첫 2개의 숫자는 캔버스 내에 위치값
canvas_image = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

wrong_img = PhotoImage(file="images/wrong.png")
right_img = PhotoImage(file="images/right.png")
next_button = Button(image=wrong_img, highlightbackground=BACKGROUND_COLOR, command=choose_random_card)
next_button.grid(row=1, column=0)
check_button = Button(image=right_img, highlightbackground=BACKGROUND_COLOR, command=learn_word)
check_button.grid(row=1, column=1)

choose_random_card()

screen.mainloop()
