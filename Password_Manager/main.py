# 비밀번호 생성기 및 비밀번호 관리 앱
from tkinter import *
from tkinter import messagebox
from random import *
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pswd_generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pswd_letters = [choice(letters) for _ in range(randint(8, 10))]
    pswd_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    pswd_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    sum_pswd = pswd_letters + pswd_symbols + pswd_numbers
    shuffle(sum_pswd)

    final_pswd = "".join(sum_pswd)

    if len(password_entry.get()) > 0:
        password_entry.delete(0,END)
        password_entry.insert(0,final_pswd)
    else:
        password_entry.insert(0,final_pswd)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get().title()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password":password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="There is an Empty Field.", icon='question')
    else:
        try:
            with open("data.json", 'r') as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)

            with open("data.json", 'w') as data_file:
                # saving update data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0,END)
            password_entry.delete(0,END)
            messagebox.showinfo(title="Password Create", message="It is created.")

# ---------------------------- FIND PASSWORD ------------------------------- #
def search_password():
    website = website_entry.get().title()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found", icon="error")
    else:
        if website in data:
            email_info = data[website]["email"]
            password_info = "*" * len(data[website]["password"])
            messagebox.showinfo(title="Search", message=f"E-mail : {email_info}\n Password : {password_info}", icon="info")
        else:
            messagebox.showinfo(title="Search", message=f"There is no {website} named", icon='question')



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=38)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0,"abcd@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
search_button = Button(text="Search", width=13, command=search_password)
search_button.grid(row=1, column=2)
generate_pswd_button = Button(text="Generate Password", command=pswd_generate)
generate_pswd_button.grid(row=3, column=2)
add_button = Button(text="Add", width=35, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()