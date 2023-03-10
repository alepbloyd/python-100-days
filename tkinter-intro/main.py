from tkinter import *

FONT = ("Arial", 12, "bold")

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20,pady=20)

def calc_clicked():
  miles = float(input_box.get())
  result_label.config(text=round(miles * 1.609, 2))

input_box = Entry()
input_box.config(width=10)
input_box.grid(column=1,row=0)

mile_label = Label(text="Miles", font=FONT)
mile_label.grid(column=2,row=0)

is_equal_to_label = Label(text="is equal to", font=FONT)
is_equal_to_label.grid(column=0,row=1)

result_label = Label(text="0", font=FONT)
result_label.grid(column=1,row=1)

km_label = Label(text="Km", font=FONT)
km_label.grid(column=2,row=1)

calc_button = Button(text="Calculate", command=calc_clicked)
calc_button.grid(column=1, row=2)


window.mainloop()