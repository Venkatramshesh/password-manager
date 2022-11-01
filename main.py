import pandas
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
WHITE = "#fff"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generatepassword():


    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    symbols = ['!', '$', '%', '&',  '*', '+']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    num_letter = random.randint(5, 7)
    num_symbol = random.randint(5, 7)
    num_number = random.randint(5, 7)
    passwd = list()

    total_chars = num_letter + num_symbol + num_number
    n = 0

    for char in range(0, total_chars):
        if num_letter != 0:
            n = random.randint(0, len(letters) - 1)
            passwd.append(letters[n])
            num_letter -= 1
        if num_symbol != 0:
            n = random.randint(0, len(symbols) - 1)
            passwd.append(symbols[n])
            num_symbol -= 1
        if num_number != 0:
            n = random.randint(0, len(numbers) - 1)
            passwd.append(numbers[n])
            num_number -= 1

    random.shuffle(passwd)
    new_string = "".join(passwd)
    pyperclip.copy(new_string)
    password.insert(0,new_string)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def savepassword():
    web = website.get()
    passwd = password.get()
    em = email_save.get()
    new_data = {
        web: {
            "email": em,
            "password": passwd,
        }
    }
    if len(web)==0 or len(passwd)==0:
        messagebox.showinfo(title="Oops", message="Please make sure you havent left any fields empty.")
    else:
       try:
            passwordfile = open("C:/Users/venka/Python100days/password-manager-start/savepassword.json")
            data = json.load(passwordfile)
            data.update(new_data)
            passwordfile = open("C:/Users/venka/Python100days/password-manager-start/savepassword.json",
                                mode="w")
            json.dump(data, passwordfile, indent=4)
       except:
            FileNotFoundError
            passwordfile = open("C:/Users/venka/Python100days/password-manager-start/savepassword.json",
            mode="w")
            data = new_data
            json.dump(data,passwordfile,indent=4)
       finally:
            website.delete(0,END)
            password.delete(0,END)

def searchpassword():
    try:
        passwordfile = open("C:/Users/venka/Python100days/password-manager-start/savepassword.json")
        data = json.load(passwordfile)
        flag = False
        if website.get() in data:
            #password.insert(0,data[website.get()]['password'])
            messagebox.showinfo(title="Data", message="Email: " f"{data[website.get()]['email']}" "\n" "Password: " f"{data[website.get()]['password']}")
            #email_save.delete(0,END)
            #email_save.insert(0,data[website.get()]['email'])
            flag = True
        if flag == False:
            messagebox.showinfo(title="Sorry", message="No Details for the website exists")
    except:
        FileNotFoundError
        messagebox.showinfo(title="Sorry", message="No Data File Found")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.geometry("450x450")
window.config(padx=20, pady =20, bg=WHITE)

canvas = Canvas(width = 200, height = 200,  bg=WHITE, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(70,100,image=logo_img)
canvas.grid( row = 0, column=1)

web = Label(text="Website:")
web.grid(column=0,row=1)
website = Entry(width=28)
website.grid(row=1,column=1,columnspan=1,sticky="w")
website.focus()
search = Button(text="Search",width=10,command=searchpassword)
search.grid(column=1,row=1,sticky="e")

email = Label(text="Email/Username:")
email.grid(column=0,row=2)
email_save = Entry(width=42)
email_save.grid(column=1, row=2,columnspan=3, sticky="w")
email_save.insert(0, "venkatramshesh@yahoo.com")

passwd = Label(text="Password:")
passwd.grid(column=0,row=3)
password = Entry(width=21)
password.grid(column=1, row=3,columnspan=1, sticky="w")
generatepsswd = Button(text="Generate Password", width=15, command=generatepassword)
generatepsswd.grid(column=1,row=3, sticky="e")

add = Button(text="Add",width=35, command=savepassword)
add.grid(column=1,row=4,sticky="w")

window.mainloop()