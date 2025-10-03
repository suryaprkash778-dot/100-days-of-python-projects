from tkinter import *
from tkinter import messagebox
import random
import pyperclip

YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    pass_input.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    pass_data = pass_input.get()
    email_data = email_input.get()
    website_data = website_input.get()

    if len(pass_data)==0 or len(email_data)==0 or len(website_data)==0:
        messagebox.showerror(title="Error!",message="You left some field(s) empty!")

    else:
        is_ok = messagebox.askokcancel(title=website_data, message=f"These are the details entered:\n"
                                                                        f"Email: {email_data}\nPassword: {pass_data}")

        if is_ok:
            with open("data.txt","a+") as data:
                data.write(f"{website_data} | {email_data} | {pass_data}\n")
                pass_input.delete(0,"end")
                website_input.delete(0,"end")

# ---------------------------- UI SETUP ------------------------------- #

window =Tk()
window.title("Password Manager")
window.config(padx=40,pady=80,)

canvas = Canvas(width=200,height=200,highlightthickness=0)
img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=img)
canvas.grid(column=1,row=0)

website_label=Label(text="Website:",font=(FONT_NAME,14,"bold"))
website_label.grid(column=0,row=1)

user_label=Label(text="Email/Username:",font=(FONT_NAME,14,"bold"))
user_label.grid(column=0,row=2)

pass_label=Label(text="Password:",font=(FONT_NAME,14,"bold"))
pass_label.grid(column=0,row=3)

website_input = Entry(width=52)
website_input.grid(column=1,row=1,columnspan=2)
website_input.focus()



email_input = Entry(width=52)
email_input.grid(column=1, row=2,columnspan=2)
email_input.insert(0,"Surya.27399@stu.upes.ac.in")



pass_input = Entry(width=32)
pass_input.grid(column=1,row=3)


add_button = Button(text="Add",width=43,bg=YELLOW,command=save_data)
add_button.grid(column=1,row=4,columnspan=2)

generate_button = Button(text="Generate Password",width=15,bg=YELLOW,command=generate_password)
generate_button.grid(column=2,row=3)





window.mainloop()
