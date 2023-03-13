from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

LABEL_FONT = ("Courier", 12, "normal")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
  password_entry.delete(0,END)

  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

  random_letters = [choice(letters) for letter in range(randint(8, 10))]
  random_symbols = [choice(symbols) for symbol in range(randint(2, 4))]
  random_numbers = [choice(numbers) for number in range(randint(2, 4))]

  password_list = random_letters + random_symbols + random_numbers

  shuffle(password_list)

  password_string = ''.join(password_list)

  password_entry.insert(END, password_string)

  pyperclip.copy(password_string)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
  website = website_entry.get()
  email = email_entry.get()
  password = password_entry.get()

  has_empties = website == "" or email == "" or password == ""

  if has_empties:
    messagebox.showerror(title="oops", message="Please fill in all fields")
    return

  is_okay_to_save = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                f"\nPassword: {password} \n"
                                                "Would you like to save?")

  if is_okay_to_save:
    with open("data.txt", mode="a") as file:
      file.write(f"{website} | {email} | {password}\n")
    
    website_entry.delete(0,END)
    password_entry.delete(0,END)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=logo_img)
canvas.grid(column=1,row=0)

website_label = Label(text="Website:", font=LABEL_FONT, fg="black", bg="white")
website_label.grid(column=0, row=1)

website_entry = Entry(width=35, highlightthickness=0)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_label = Label(text="Email/Username:", font=LABEL_FONT, fg="black", bg="white")
email_label.grid(column=0, row=2)

email_entry = Entry(width=35, highlightthickness=0)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(END, 'alepbloyd@gmail.com')

password_label = Label(text="Password:", font=LABEL_FONT, bg="white", fg="black")
password_label.grid(column=0, row=3)

password_entry = Entry(width=18, highlightthickness=0)
password_entry.grid(column=1, row=3)

generate_button = Button(text="Generate Password", highlightthickness=0, highlightbackground="white", command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", highlightthickness=0, highlightbackground="white", width=45, command=save)
add_button.grid(column=0, row=4, columnspan=3)

window.mainloop()