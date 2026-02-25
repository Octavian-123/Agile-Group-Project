import tkinter as tk
from tkinter import messagebox


# ------------------ FILE READING ------------------

def readLogins():
    with open("logins.txt", "r") as f:
        contents = f.readlines()

    newContents = []

    for line in contents:
        fields = line.strip().split(",")
        newContents.append(fields)

    return newContents


logins = readLogins()


# ------------------ LOGIN FUNCTION ------------------

def check_login():
    username = username_entry.get()
    password = password_entry.get()

    for line in logins:
        if line[0] == username and line[1] == password:
            messagebox.showinfo("Success", "Logged in successfully")
            open_menu()
            return

    messagebox.showerror("Error", "Login failed")


# ------------------ MENU WINDOW ------------------

def open_menu():
    login_frame.pack_forget()  # Hide login screen

    menu_frame.pack()

def opt1():
    messagebox.showinfo("Option 1", "This is option 1")

def opt2():
    messagebox.showinfo("Option 2", "This is option 2")

def opt3():
    messagebox.showinfo("Option 3", "This is option 3")


# ------------------ MAIN WINDOW ------------------

root = tk.Tk()
root.title("Login System")
root.geometry("300x250")

# ---------- LOGIN FRAME ----------
login_frame = tk.Frame(root)
login_frame.pack(pady=20)

tk.Label(login_frame, text="Username").pack()
username_entry = tk.Entry(login_frame)
username_entry.pack()

tk.Label(login_frame, text="Password").pack()
password_entry = tk.Entry(login_frame, show="*")
password_entry.pack()

tk.Button(login_frame, text="Login", command=check_login).pack(pady=10)


# ---------- MENU FRAME ----------
menu_frame = tk.Frame(root)

tk.Label(menu_frame, text="Main Menu", font=("Arial", 14)).pack(pady=10)

tk.Button(menu_frame, text="Option 1", command=opt1).pack(pady=5)
tk.Button(menu_frame, text="Option 2", command=opt2).pack(pady=5)
tk.Button(menu_frame, text="Option 3", command=opt3).pack(pady=5)
tk.Button(menu_frame, text="Exit", command=root.quit).pack(pady=10)


root.mainloop()
