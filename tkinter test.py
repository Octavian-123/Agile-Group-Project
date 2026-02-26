import re
import tkinter as tk
from tkinter import messagebox

# FILE READING

def readLogins():
    with open("logins.txt", "r") as f:
        contents = f.readlines()

    newContents = []

    for line in contents:
        fields = line.strip().split(",")
        newContents.append(fields)

    return newContents


def appendLogin(username, password):
    with open("logins.txt", "a") as f:
        f.write(f"{username},{password}\n")


# LOGIN FUNCTION

def checkLogin():
    logins = readLogins()

    username = usernameEntry.get()
    password = passwordEntry.get()

    for line in logins:
        if line[0] == username and line[1] == password:
            messagebox.showinfo("Success", "Logged in successfully")
            openMenu()
            return

    messagebox.showerror("Error", "Login failed")


# USERNAME and PASSWORD CONDITIONS

def validateCredentials(username, password):

    if len(username) < 7:
        messagebox.showerror("Error", "Username must be at least 7 characters long")
        return False

    if len(password) < 7:
        messagebox.showerror("Error", "Password must be at least 7 characters long")
        return False

    if not re.search(r"[A-Z]", password):
        messagebox.showerror("Error", "Password must contain at least one capital letter")
        return False

    if not re.search(r"[0-9]", password):
        messagebox.showerror("Error", "Password must contain at least one number")
        return False

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        messagebox.showerror("Error", "Password must contain at least one special character")
        return False

    return True


# SIGN UP FUNCTIONS

def openSignup():
    loginFrame.pack_forget()
    signupFrame.pack(pady=20)


def createAccount():
    username = newUsernameEntry.get()
    password = newPasswordEntry.get()

    if username == "" or password == "":
        messagebox.showerror("Error", "Fields cannot be empty")
        return

    if not validateCredentials(username, password):
        return

    logins = readLogins()

    for line in logins:
        if line[0] == username:
            messagebox.showerror("Error", "Username already exists")
            return

    appendLogin(username, password)
    messagebox.showinfo("Success", "Account created successfully")

    signupFrame.pack_forget()
    loginFrame.pack(pady=20)


# MENU FUNCTIONS

def openMenu():
    loginFrame.pack_forget()
    menuFrame.pack()


def opt1():
    messagebox.showinfo("Option 1", "This is option 1")


def opt2():
    messagebox.showinfo("Option 2", "This is option 2")


def opt3():
    messagebox.showinfo("Option 3", "This is option 3")


# DEFAULT WINDOW
root = tk.Tk()
root.title("Login System")
root.geometry("300x250")


# SIGN UP FRAME
signupFrame = tk.Frame(root)

tk.Label(signupFrame, text="Create Account", font=("Arial", 14)).pack(pady=10)

tk.Label(signupFrame, text="New Username").pack()
newUsernameEntry = tk.Entry(signupFrame)
newUsernameEntry.pack()

tk.Label(signupFrame, text="New Password").pack()
newPasswordEntry = tk.Entry(signupFrame, show="*")
newPasswordEntry.pack()

tk.Button(signupFrame, text="Create Account", command=createAccount).pack(pady=5)
tk.Button(signupFrame, text="Back to Login", command=lambda: [signupFrame.pack_forget(), loginFrame.pack(pady=20)]).pack(pady=5)


# LOGIN FRAME
loginFrame = tk.Frame(root)
loginFrame.pack(pady=20)

tk.Label(loginFrame, text="Username").pack()
usernameEntry = tk.Entry(loginFrame)
usernameEntry.pack()

tk.Label(loginFrame, text="Password").pack()
passwordEntry = tk.Entry(loginFrame, show="*")
passwordEntry.pack()

tk.Button(loginFrame, text="Login", command=checkLogin).pack(pady=10)
tk.Button(loginFrame, text="Sign Up", command=openSignup).pack(pady=5)


# MENU FRAME
menuFrame = tk.Frame(root)

tk.Label(menuFrame, text="Main Menu", font=("Arial", 14)).pack(pady=10)

tk.Button(menuFrame, text="Option 1", command=opt1).pack(pady=5)
tk.Button(menuFrame, text="Option 2", command=opt2).pack(pady=5)
tk.Button(menuFrame, text="Option 3", command=opt3).pack(pady=5)
tk.Button(menuFrame, text="Exit", command=root.quit).pack(pady=10)


root.mainloop()
