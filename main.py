from tkinter import *
from tkinter import messagebox
from random import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letter = [choice(letters) for _ in range(randint(8,10))]
    password_number = [choice(numbers) for _ in range(randint(2,4))]
    password_symbol = [choice(symbols) for _ in range(randint(2,4))]
    password_list = password_letter + password_symbol+password_number
    random.shuffle(password_list)
    password ="".join(password_list)
    password_input.insert(0,password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email_and_username = email_and_username_input.get()
    password = password_input.get()
    if len(website) or len(password) == 0:
        messagebox.showerror(title="ERROR", message="Kindly fill the details.")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the details entered: \nEmail:{email_and_username}\n"
                                               f"Password{password}\n Is it ok to save?")

        if is_ok:
             with open("data.txt","a") as file1:
                file1.write(f"{website} | {email_and_username} | {password}\n")
                website_input.delete(0,END)
                password_input.delete(0,END)




# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("PASSWORD MANAGER")
window.config(bg="White")
window.config(padx=50,pady=50)

#LOGO
canvas = Canvas(width=200, height=200, bg="White", highlightthickness=0)
image_used = PhotoImage(file="logo.png")
canvas.create_image(100,100,image= image_used)
canvas.grid(column=1, row=0)

# CREATION OF LABELS

#LABEL 1 : WEBSITE BOX

website_label = Label(text="Website: ", bg="White", highlightthickness=0, fg="Black")
website_label.grid(column=0,row=1)

#LABEL 2 : EMAIL/USERNAME
email_and_username_label = Label(text="Email/Username: ", bg="White", highlightthickness=0, fg="Black")
email_and_username_label.grid(column=0, row=2)

#LABEL 3 : PASSWORD
password_label = Label(text="Password: ",bg="White", highlightthickness=0, fg="Black")
password_label.grid(column=0,row=3)

#WIDGETS

website_input = Entry(width=35, bg="White", highlightthickness=0, fg="Black")
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

email_and_username_input = Entry(width=35, bg="White", highlightthickness=0, fg="Black")
email_and_username_input.grid(column=1, row=2, columnspan=2)
email_and_username_input.insert(0,"holyofferings22@gmail.com")
password_input = Entry(width=21,bg="White", highlightthickness=0, fg="Black")
password_input.grid(column=1, row=3)

#buttons

generate_password_button = Button(text="Generate Password", highlightthickness=0,highlightbackground="White")
generate_password_button.config(command=password_generator)
generate_password_button.grid(row=3,column=2, )

add_button = Button(text="ADD", highlightthickness=0,highlightbackground="White", width=36, command= save)
add_button.grid(row=4,column=1,columnspan=2)



window.mainloop()