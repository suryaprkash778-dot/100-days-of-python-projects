from  tkinter import *

YELLOW = "#f7f5dd"

def miles_to_km(miles):
    return miles*1.609344

window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=100,height=200)
window.config(padx=50,pady=50)

miles_label= Label(text ="Miles",font=("Arial",12))
miles_label.grid(column=2,row=0)
miles_label.config(padx=10,pady=10)

new_label1= Label(text =f"is equal to",font=("Arial",12))
new_label1.grid(column=0,row=1)
new_label1.config(pady=10)

new_label2= Label(text =f"{0}",font=("Arial",12))
new_label2.grid(column=1,row=1)
new_label2.config(pady=10)

new_label3= Label(text =f"Km",font=("Arial",12))
new_label3.grid(column=2,row=1)
new_label3.config(pady=10)

def button_clicked():
    miles = float(input.get())
    new_text = miles_to_km(miles)
    new_label2.config(text = new_text)

button = Button(text = "Calculate", command = button_clicked,bg=YELLOW)
button.grid(column=1,row=2)

input = Entry(width=20,bg=YELLOW)
input.insert(0,f"{0}")
input.grid(column=1,row=0)

window.mainloop()
