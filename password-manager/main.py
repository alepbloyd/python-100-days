from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

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
  website = website_entry.get().lower()
  email = email_entry.get().lower()
  password = password_entry.get()
  new_data = {
    website: {
      "email": email,
      "password": password
    }
  }

  has_empties = website == "" or email == "" or password == ""

  if has_empties:
    messagebox.showerror(title="oops", message="Please fill in all fields")
    return
  
  try:
    with open("data.json", "r") as file:
      data = json.load(file)
  except json.decoder.JSONDecodeError:
    with open("data.json", "w") as file:
      json.dump(new_data, file, indent=2)
  except FileNotFoundError:
    with open("data.json", "w") as file:
      json.dump(new_data, file, indent=2)
  else:
    data.update(new_data)
    with open("data.json", "w") as file:
      json.dump(data, file, indent=2)
  finally:
    website_entry.delete(0, END)
    password_entry.delete(0, END)

# Search for password

def find_password():
  search_string = website_entry.get().lower()
  
  if search_string == "":
    messagebox.showerror(title="Blank Search", message="Please enter a website in the 'website' field")
    return
  
  try:
    with open("data.json", "r") as file:
      data = json.load(file)
  except FileNotFoundError:
    messagebox.showerror(title="No Data File", message="No Data File Found")
  else:
    try:
      email = data[search_string]["email"]
      password = data[search_string]["password"]
    except KeyError:
      messagebox.showerror(title="Not Found", message="No details for the website exists")
    else:
      message_text = f"Website: {search_string} \n Email: {email} \n Password: {password}"
      messagebox.showinfo(title="Search Result", message=message_text)

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

website_entry = Entry(width=18, highlightthickness=0)
website_entry.grid(column=1, row=1)
website_entry.focus()

email_label = Label(text="Email/Username:", font=LABEL_FONT, fg="black", bg="white")
email_label.grid(column=0, row=2)

email_entry = Entry(width=38, highlightthickness=0)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(END, 'alepbloyd@gmail.com')

password_label = Label(text="Password:", font=LABEL_FONT, bg="white", fg="black")
password_label.grid(column=0, row=3)

password_entry = Entry(width=18, highlightthickness=0)
password_entry.grid(column=1, row=3)

generate_button = Button(width=16,text="Generate Password", highlightthickness=0, highlightbackground="white", command=generate_password)
generate_button.grid(column=2, row=3)

search_button = Button(width=16, text="Search", highlightthickness=0, highlightbackground="white", command=find_password)
search_button.grid(column=2, row=1)

add_button = Button(text="Add", highlightthickness=0, highlightbackground="white", width=48, command=save)
add_button.grid(column=0, row=4, columnspan=3)

window.mainloop()