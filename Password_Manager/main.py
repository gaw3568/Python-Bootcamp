# 비밀번호 생성기 및 비밀번호 관리 앱
from tkinter import *
from tkinter import messagebox
from random import *
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
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="There is an Empty Field.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail : {email}" f"\nPassword: {password} \n Is it ok to save?")

        if is_ok:
            with open("data.txt", 'a') as data_file:
                data_file.write(f"Website: {website} | Email: {email} | Password: {password}\n")
                website_entry.delete(0,END)
                password_entry.delete(0,END)

            messagebox.showinfo(title="Password Create", message="It is created.")




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
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0,"abcd@gmail.com")
password_entry = Entry(width=19)
password_entry.grid(row=3, column=1)

# Buttons
generate_pswd_button = Button(text="Generate Password", command=pswd_generate)
generate_pswd_button.grid(row=3, column=2)
add_button = Button(text="Add", width=35, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()