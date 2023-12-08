import re
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Registration Form')
root.geometry('500x500')


def submit_func():
    username = entry_name.get()
    email = entry_email.get()
    password = entry_password.get()
    password2 = entry_password2.get()

    if password and password2 and username and email:
        ch = r'\b[a-zA-Z0-9-_%$]+@[a-zA-Z0-9]+\.[a-z|A-Z]{1,3}\b'
        if re.fullmatch(ch, email):
            if password == password2:
                messagebox.showinfo('success', 'successfully registered')
                root.destroy()
            else:
                messagebox.showerror('error', 'please enter same password')
        else:
            messagebox.showerror('error', 'please enter valid email')
    else:
        messagebox.showerror('error', 'please fill all fields')


Label(text='Registration Form', font=('bold', 30)).place(x=90, y=20)

label_name = Label(root, text='Enter Name', font='bold')
label_name.place(x=50, y=120)

entry_name = Entry()
entry_name.place(x=200, y=120, height=25, width=250)

label_email = Label(root, text='Enter Email', font='bold')
label_email.place(x=50, y=170)

entry_email = Entry()
entry_email.place(x=200, y=170, height=25, width=250)

label_password = Label(root, text='Enter Password', font='bold')
label_password.place(x=50, y=220)

entry_password = Entry()
entry_password.place(x=200, y=220, height=25, width=250)

label_password = Label(root, text='Re-Enter Password', font='bold')
label_password.place(x=50, y=270)

entry_password2 = Entry()
entry_password2.place(x=200, y=270, height=25, width=250)

button_submit = Button(text='Register', font=('bold', 10), background='black', foreground='white', command=submit_func)
button_submit.place(x=180, y=330, width=100)

root.mainloop()
