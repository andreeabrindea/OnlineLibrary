import tkinter
from tkinter import *
from PIL import ImageTk, Image
import matplotlib.pyplot as plt

root = Tk()
root.title("Online Library")
root.iconbitmap("C:/Users/tpodi/Downloads/books.ico")
root.geometry("1038x576")

# Define image
bg = ImageTk.PhotoImage(file='C:/Users/tpodi/PycharmProjects/MyLibrary/onlinelibrary.png')

# Create a canvas
bg_canvas = Canvas(root, width=1038, heigh=576)
bg_canvas.pack(fill="both", expand=True)

# Set image in canvas
bg_canvas.create_image(0, 0, image=bg, anchor="nw")

# Add Login label
bg_canvas.create_text(100, 180, text="Sign in:", font=("Britannic Bold", 24), fill="#5c739d")

# Add the entries
username = tkinter.Entry(root)
username.insert(0, "username")
bg_canvas.create_window(210, 210, window=username)

password = tkinter.Entry(root, show="*")
password.insert(0, "password")
bg_canvas.create_window(210, 250, window=password)


def open_dashboard():
    global dashboard_bg
    dashboard = Toplevel()
    root.withdraw()
    dashboard.title("Dashboard")
    dashboard.iconbitmap("C:/Users/tpodi/Downloads/books.ico")
    dashboard.geometry("1038x576")

    # Define the background image
    dashboard_bg = ImageTk.PhotoImage(file='C:/Users/tpodi/PycharmProjects/MyLibrary/dashboard.png')

    # Creating the canvas
    dashboard_canvas = Canvas(dashboard, width=1038, heigh=576)
    dashboard_canvas.pack(fill="both", expand=True)

    # Set the background image in canvas
    dashboard_canvas.create_image(0, 0, image=dashboard_bg, anchor="nw")

    # Add search button
    browse_books_button = Button(dashboard, text="Search")
    dashboard_canvas.create_window(570, 20, window=browse_books_button)

    # Add search entry
    search_entry = Entry(dashboard)
    dashboard_canvas.create_window(475, 20, window=search_entry)


def open_register():
    global name_entry, bg2_canvas, register
    root.withdraw()
    register = Toplevel(root)
    register.title("Register")
    register.iconbitmap("C:/Users/tpodi/Downloads/books.ico")
    register.geometry("1038x576")

    # Create a canvas
    bg2_canvas = tkinter.Canvas(register, width=1038, heigh=576)
    bg2_canvas.pack(fill="both", expand=True)

    # Add the register text
    bg2_canvas.create_text(200, 40, text="Create a new account:", font=("Britannic Bold", 24), fill="#5c739d")
    bg2_canvas.create_text(240, 80, text="First name:", font=("Britannic Bold", 16), fill="#fc9d6f")
    bg2_canvas.create_text(260, 120, text="Last name:", font=("Britannic Bold", 16), fill="#fc9d6f")
    bg2_canvas.create_text(280, 160, text="E-mail:", font=("Britannic Bold", 16), fill="#fc9d6f")
    bg2_canvas.create_text(280, 200, text="Username:", font=("Britannic Bold", 16), fill="#fc9d6f")
    bg2_canvas.create_text(280, 240, text="Password:", font=("Britannic Bold", 16), fill="#fc9d6f")
    bg2_canvas.create_text(280, 280, text="Address:", font=("Britannic Bold", 16), fill="#fc9d6f")

    # Add entries to the canvas
    first_name_entry = tkinter.Entry(bg2_canvas)
    bg2_canvas.create_window(400, 80, window=first_name_entry)
    last_name_entry = tkinter.Entry(bg2_canvas)
    bg2_canvas.create_window(400, 120, window=last_name_entry)
    email_entry = tkinter.Entry(bg2_canvas)
    bg2_canvas.create_window(400, 160, window=email_entry)
    username_entry = tkinter.Entry(bg2_canvas)
    bg2_canvas.create_window(400, 200, window=username_entry)
    password_entry = tkinter.Entry(bg2_canvas, show="*")
    bg2_canvas.create_window(400, 240, window=password_entry,)
    address_entry = tkinter.Entry(bg2_canvas)
    bg2_canvas.create_window(400, 280, window=address_entry)

    sign_in_button = Button(register, text="Sign in", command=open_dashboard)
    bg2_canvas.create_window(400, 310, window=sign_in_button)


# Add the login and sign up buttons
login_button = Button(root, text="Login", command=open_dashboard)
signup_button = Button(root, text="Sign up!", command=open_register)
bg_canvas.create_window(170, 280, window=login_button)
bg_canvas.create_window(230, 280, window=signup_button)


def resizer(e):
    global bg1, resized_bg, new_bg

    # Open the image
    bg1 = Image.open('C:/Users/tpodi/PycharmProjects/MyLibrary/onlinelibrary.png')

    # Resize the image
    resized_bg = bg1.resize((e.width, e.height), Image.ANTIALIAS)

    # Define the image again
    new_bg = ImageTk.PhotoImage(resized_bg)

    # Add it back to the canvas
    bg_canvas.create_image(0, 0, image=new_bg, anchor="nw")

    # Radd the text
    bg_canvas.create_text(100, 180, text="Sign in:", font=("Britannic Bold", 24), fill="#5c739d")


root.bind("<Configure>", resizer)

root.mainloop()
