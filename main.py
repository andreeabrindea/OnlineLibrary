import tkinter
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import pymysql
from tkinter import messagebox
import models

root = Tk()
root.title("Online Library")
root.iconbitmap("C:/Users/tpodi/Downloads/books.ico")
root.geometry("1038x576")
root.resizable(False, False)

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
username_entry = tkinter.Entry(root)
username_entry.insert(0, "username")
bg_canvas.create_window(210, 210, window=username_entry)

password = tkinter.Entry(root, show="*")
password.insert(0, "password")
bg_canvas.create_window(210, 250, window=password)

options = ["admin", "client"]
role_entry = ttk.Combobox(root, value=options, width=17)
bg_canvas.create_window(210, 290, window=role_entry)


def open_dashboard():
    global dashboard_bg, dashboard
    dashboard = Toplevel()
    dashboard.title("Dashboard")
    dashboard.iconbitmap("C:/Users/tpodi/Downloads/books.ico")
    dashboard.geometry("1038x576")
    dashboard.resizable(False, False)

    # Define the background image
    dashboard_bg = ImageTk.PhotoImage(file='C:/Users/tpodi/PycharmProjects/MyLibrary/dashboard_background.png')

    # Creating the canvas
    dashboard_canvas = Canvas(dashboard, width=1038, heigh=576)
    dashboard_canvas.pack(fill="both", expand=True)

    # Set the background image in canvas
    dashboard_canvas.create_image(0, 0, image=dashboard_bg, anchor="nw")

    dashboard_canvas.create_text(400, 150, text="Choose one option: ", font=("Britannic Bold", 24), fill="#fc9d6f")

    def open_borrow():
        global borrow_bg, borrow
        borrow = Toplevel()
        borrow.title("Borrow a book")
        borrow.iconbitmap("C:/Users/tpodi/Downloads/books.ico")
        borrow.geometry("1038x576")
        borrow.resizable(False, False)
        root.withdraw()

        # Define the background image
        borrow_bg = ImageTk.PhotoImage(file='C:/Users/tpodi/PycharmProjects/MyLibrary/borrow_background.png')

        # Creating the canvas
        borrow_canvas = Canvas(borrow, width=1038, heigh=576)
        borrow_canvas.pack(fill="both", expand=True)

        # Set the background image in canvas
        borrow_canvas.create_image(0, 0, image=borrow_bg, anchor="nw")

        # Add enter title entry
        title_entry = Entry(borrow)
        borrow_canvas.create_window(490, 250, window=title_entry)

        def borrow_book():
            con = pymysql.connect(host="localhost",
                                  user="root",
                                  password="root",
                                  database="librarydb",
                                  charset='utf8mb4',
                                  cursorclass=pymysql.cursors.DictCursor
                                  )
            curs = con.cursor()
            curs.execute('Select * from books where name=%s', (title_entry.get()))
            row = curs.fetchone()

            if title_entry.get() == "":
                messagebox.showwarning("Warning", "You didn't enter the title name!")

            if row is None:
                messagebox.showerror("Error", "Book unavailable")
            else:
                try:
                    con = pymysql.connect(host="localhost",
                                          user="root",
                                          password="root",
                                          database="librarydb",
                                          charset='utf8mb4',
                                          cursorclass=pymysql.cursors.DictCursor
                                          )
                    curs = con.cursor()
                    curs.execute("UPDATE books SET borrowed = %s WHERE name=%s and borrowed = \"No\"",
                                 (received_user[("username")], title_entry.get()))
                    con.commit()
                    con.close()
                except Exception as es:
                    messagebox.showerror("Error!", f"Error due to: {str(es)}")
                messagebox.showinfo("Success!", "The book was borrowed! Now you can close this page.")

        # Add enter button
        enter_button = Button(borrow, text="Submit", activebackground="#5c739d", activeforeground="white", fg="#5c739d",
                              bg="#E7F2F8", font=("Britannic Bold", 11), command=lambda: borrow_book())
        borrow_canvas.create_window(490, 290, window=enter_button)

    def open_return():
        global return_book_bg, return_book
        return_book = Toplevel()
        return_book.title("Return a book")
        return_book.iconbitmap("C:/Users/tpodi/Downloads/books.ico")
        return_book.geometry("1038x576")
        return_book.resizable(False, False)

        # Define the background image
        return_book_bg = ImageTk.PhotoImage(file='C:/Users/tpodi/PycharmProjects/MyLibrary/borrow_background.png')

        # Creating the canvas
        return_book_canvas = Canvas(return_book, width=1038, heigh=576)
        return_book_canvas.pack(fill="both", expand=True)

        # Set the background image in canvas
        return_book_canvas.create_image(0, 0, image=return_book_bg, anchor="nw")

        # Add enter title entry
        title_entry = Entry(return_book)
        return_book_canvas.create_window(490, 250, window=title_entry)

        def return_books():
            con = pymysql.connect(host="localhost",
                                  user="root",
                                  password="root",
                                  database="librarydb",
                                  charset='utf8mb4',
                                  cursorclass=pymysql.cursors.DictCursor
                                  )
            curs = con.cursor()
            curs.execute('Select * from books where name=%s', (title_entry.get()))
            row = curs.fetchone()

            if title_entry.get() == "":
                messagebox.showwarning("Warning", "You didn't enter the title name!")

            if row is None:
                messagebox.showerror("Error", "Book unavailable")
            else:
                try:
                    con = pymysql.connect(host="localhost",
                                          user="root",
                                          password="root",
                                          database="librarydb",
                                          charset='utf8mb4',
                                          cursorclass=pymysql.cursors.DictCursor
                                          )
                    curs = con.cursor()
                    curs.execute("Select borrowed from books")
                    carti_imprumutate = curs.fetchone()
                    i=0
                    while carti_imprumutate is None or carti_imprumutate[("borrowed")] != received_user[("username")]:
                        carti_imprumutate = curs.fetchone()

                    if carti_imprumutate[("borrowed")] != received_user[("username")]:
                        messagebox.showwarning("Warning!", "You can't return someone else's book")

                    else:
                        curs.execute("UPDATE books SET borrowed = \"No\"WHERE name=%s and borrowed = %s",
                                     (title_entry.get(), received_user[("username")]))
                        con.commit()
                        con.close()

                        messagebox.showinfo("Success!", "The book was returned! Now you can close this page.")
                except Exception as es:
                    messagebox.showerror("Error!", f"Error due to: {str(es)}")

        # Add enter button
        enter_button = Button(return_book, text="Submit", activebackground="#5c739d", activeforeground="white",
                              fg="#5c739d", bg="#E7F2F8", font=("Britannic Bold", 11), command=lambda: return_books())
        return_book_canvas.create_window(490, 290, window=enter_button)

    # Add borrow button
    borrow_books_button = Button(dashboard, text="Borrow books", activebackground="#5c739d", activeforeground="white",
                                 fg="#5c739d", bg="#E7F2F8", font=("Britannic Bold", 11), command=open_borrow)
    dashboard_canvas.create_window(590, 200, window=borrow_books_button)

    # Add return button
    return_books_button = Button(dashboard, text="Return books", activebackground="#5c739d", activeforeground="white",
                                 fg="#5c739d", bg="#E7F2F8", font=("Britannic Bold", 11), command=open_return)
    dashboard_canvas.create_window(590, 260, window=return_books_button)

    def open_view_books():
        view = Toplevel()
        view.title("Books")
        view.iconbitmap("C:/Users/tpodi/Downloads/books.ico")
        view.resizable(False, False)

        # Creating the Frame
        m_frame = Frame(view, bd=10, width=1038, height=576, relief=RIDGE, bg='white')
        m_frame.grid()

        # Creating the TreeView with books
        scroll_y = Scrollbar(m_frame, orient=VERTICAL)
        book_records = ttk.Treeview(m_frame, height=26, columns=("idbooks", "name", "borrow"))
        scroll_y.pack(side=RIGHT, fill=Y)

        book_records.heading("idbooks", text="BOOK ID")
        book_records.heading("name", text="TITLE")
        book_records.heading("borrow", text="BORROWED")
        book_records['show'] = 'headings'

        book_records.column("idbooks", width=150)
        book_records.column("name", width=300)
        book_records.column("borrow", width=150)

        book_records.pack(fill=BOTH, expand=1)
        # Adding the database for display
        con = pymysql.connect(host="localhost",
                              user="root",
                              password="root",
                              database="librarydb",
                              charset='utf8mb4',
                              cursorclass=pymysql.cursors.DictCursor
                              )
        curs = con.cursor()
        curs.execute('Select idbooks, name, borrowed from books')
        received_books = curs.fetchone()
        book_records.delete(*book_records.get_children())

        if received_books is None:
            messagebox.showerror("Error! There are no books")

        while received_books is not None:
            print(received_books)
            book = (
                received_books["idbooks"],
                received_books["name"],
                received_books["borrowed"],
            )
            book_records.insert('', END, values=book)
            received_books = curs.fetchone()
        con.commit()
        con.close()

    # Add view books button
    view_books_button = Button(dashboard, text="View books", activebackground="#5c739d", activeforeground="white",
                               fg="#5c739d", bg="#E7F2F8", font=("Britannic Bold", 11), command=open_view_books)
    dashboard_canvas.create_window(590, 320, window=view_books_button)


def open_register():
    global name_entry, bg2_canvas, register
    register = Toplevel(root)
    register.title("Register")
    register.iconbitmap("C:/Users/tpodi/Downloads/books.ico")
    register.geometry("1038x576")
    register.resizable(False, False)

    # Create a canvas
    bg2_canvas = tkinter.Canvas(register, width=1038, heigh=576)
    bg2_canvas.pack(fill="both", expand=True)

    # Add the register text
    bg2_canvas.create_text(200, 40, text="Create a new account:", font=("Britannic Bold", 24), fill="#5c739d")
    bg2_canvas.create_text(280, 80, text="First name:", font=("Britannic Bold", 16), fill="#fc9d6f")
    bg2_canvas.create_text(280, 120, text="Last name:", font=("Britannic Bold", 16), fill="#fc9d6f")
    bg2_canvas.create_text(280, 160, text="E-mail:", font=("Britannic Bold", 16), fill="#fc9d6f")
    bg2_canvas.create_text(280, 200, text="Username:", font=("Britannic Bold", 16), fill="#fc9d6f")
    bg2_canvas.create_text(280, 240, text="Password:", font=("Britannic Bold", 16), fill="#fc9d6f")
    bg2_canvas.create_text(280, 280, text="Address:", font=("Britannic Bold", 16), fill="#fc9d6f")
    bg2_canvas.create_text(280, 320, text="Role:", font=("Britannic Bold", 16), fill="#fc9d6f")
    bg2_canvas.create_text(280, 360, text="Id:", font=("Britannic Bold", 16), fill="#fc9d6f")
    bg2_canvas.create_text(220, 400, text="Secret code (for admins):", font=("Britannic Bold", 16), fill="#fc9d6f")

    # Add entries to the canvas
    first_name_entry = tkinter.Entry(bg2_canvas)
    bg2_canvas.create_window(400, 80, window=first_name_entry)
    last_name_entry = tkinter.Entry(bg2_canvas)
    bg2_canvas.create_window(400, 120, window=last_name_entry)
    email_entry = tkinter.Entry(bg2_canvas)
    bg2_canvas.create_window(400, 160, window=email_entry)
    new_username_entry = tkinter.Entry(bg2_canvas)
    bg2_canvas.create_window(400, 200, window=new_username_entry)
    new_password_entry = tkinter.Entry(bg2_canvas, show="*")
    bg2_canvas.create_window(400, 240, window=new_password_entry)
    address_entry = tkinter.Entry(bg2_canvas)
    bg2_canvas.create_window(400, 280, window=address_entry)
    new_options = ["admin", "client"]
    role_entry2 = ttk.Combobox(bg2_canvas, value=new_options, width=17)
    bg2_canvas.create_window(400, 320, window=role_entry2)
    id_entry = tkinter.Entry(bg2_canvas)
    bg2_canvas.create_window(400, 360, window=id_entry)
    secret_code_entry = tkinter.Entry(bg2_canvas)
    bg2_canvas.create_window(400, 400, window=secret_code_entry)

    create_button = Button(register, text="Create", activebackground="#5c739d", activeforeground="white",
                           fg="#5c739d", bg="#E7F2F8", font=("Britannic Bold", 11), command=lambda: register())
    bg2_canvas.create_window(400, 440, window=create_button)

    # Creating database register
    def register():
        if first_name_entry.get() == "" or last_name_entry.get() == "" or email_entry.get() == "" or new_username_entry.get() == "" or new_password_entry.get() == "" or address_entry.get() == "":
            messagebox.showwarning("Warning", "All the fields except secret code are required!")
        if role_entry2.get() == "client" and secret_code_entry.get() != "":
            messagebox.showwarning("Warning", "Secret code is only for the admins")
        if role_entry2.get() == "admin" and secret_code_entry.get() != "IPSNAFNB":
            messagebox.showwarning("Warning", "Wrong code!")
            con = pymysql.connect(host="localhost",
                                  user="root",
                                  password="root",
                                  database="librarydb",
                                  charset='utf8mb4',
                                  cursorclass=pymysql.cursors.DictCursor
                                  )
            curs = con.cursor()
            curs.execute('Select * from users where username=%s and password=%s',
                         (new_username_entry.get(), new_password_entry.get()))
            row = curs.fetchone()
        else:
            try:
                con = pymysql.connect(host="localhost",
                                      user="root",
                                      password="root",
                                      database="librarydb",
                                      charset='utf8mb4',
                                      cursorclass=pymysql.cursors.DictCursor
                                      )
                curs = con.cursor()
                curs.execute(
                    "insert into users(idusers, first_name, last_name, username, email, password, address, role) values(%s, %s, %s, %s, %s, %s, %s, %s)",
                    (
                        id_entry.get(),
                        first_name_entry.get(),
                        last_name_entry.get(),
                        new_username_entry.get(),
                        email_entry.get(),
                        new_password_entry.get(),
                        address_entry.get(),
                        role_entry2.get()
                    ))
                con.commit()
                con.close()
                messagebox.showinfo("Success!", "Your account was created! Now you can close this page.")
            except Exception as es:
                messagebox.showerror("Error!", f"Error due to: {str(es)}")


# Creating database connection
def login_data():
    global received_user
    if username_entry.get() == "" or password.get() == "":
        messagebox.showwarning("Warning", "Your username, password and role can't be empty!")

    con = pymysql.connect(host="localhost",
                          user="root",
                          password="root",
                          database="librarydb",
                          charset='utf8mb4',
                          cursorclass=pymysql.cursors.DictCursor
                          )
    cur = con.cursor()
    cur.execute('Select * from users where username=%s and password=%s and role=%s ',
                (username_entry.get(), password.get(), role_entry.get()))
    received_user = cur.fetchone()
    # print(received_user["idusers"])
    # print(received_user)

    if received_user is None:
        messagebox.showerror("Error", "User not found or incorrect password!")
    else:
        if role_entry.get() == "admin":
            open_administrative()
        else:
            open_dashboard()


# Add the login and sign up buttons
login_button = Button(root, text="Login", activebackground="#5c739d", activeforeground="white", fg="#5c739d",
                      bg="#E7F2F8", font=("Britannic Bold", 11), command=lambda: login_data())
signup_button = Button(root, text="Sign up!", activebackground="#5c739d", activeforeground="white", fg="#5c739d",
                       bg="#E7F2F8", font=("Britannic Bold", 11), command=open_register)
bg_canvas.create_window(170, 330, window=login_button)
bg_canvas.create_window(230, 330, window=signup_button)


def open_administrative():
    global admin_bg
    admin = Toplevel(root)
    admin.title("Administrative mode on")
    admin.iconbitmap("C:/Users/tpodi/Downloads/books.ico")
    admin.geometry("1038x576")
    admin.resizable(False, False)
    # Define the background image
    admin_bg = ImageTk.PhotoImage(file='C:/Users/tpodi/PycharmProjects/MyLibrary/administrative.png')

    # Creating the canvas
    admin_canvas = Canvas(admin, width=1038, heigh=576)
    admin_canvas.pack(fill="both", expand=True)

    # Set the background image in canvas
    admin_canvas.create_image(0, 0, image=admin_bg, anchor="nw")

    # Add book details
    admin_canvas.create_text(200, 40, text="Add a new book:", font=("Britannic Bold", 24), fill="#5c739d")
    admin_canvas.create_text(240, 80, text="Id:", font=("Britannic Bold", 16), fill="#fc9d6f")
    admin_canvas.create_text(260, 120, text="Title:", font=("Britannic Bold", 16), fill="#fc9d6f")
    admin_canvas.create_text(280, 160, text="Author:", font=("Britannic Bold", 16), fill="#fc9d6f")
    admin_canvas.create_text(280, 200, text="Year:", font=("Britannic Bold", 16), fill="#fc9d6f")
    admin_canvas.create_text(280, 240, text="Borrowed:", font=("Britannic Bold", 16), fill="#fc9d6f")
    admin_canvas.create_text(280, 280, text="ISBN:", font=("Britannic Bold", 16), fill="#fc9d6f")

    # Add entries to the canvas
    id_entry = tkinter.Entry(admin_canvas)
    admin_canvas.create_window(400, 80, window=id_entry)
    title_entry = tkinter.Entry(admin_canvas)
    admin_canvas.create_window(400, 120, window=title_entry)
    author_entry = tkinter.Entry(admin_canvas)
    admin_canvas.create_window(400, 160, window=author_entry)
    year_entry = tkinter.Entry(admin_canvas)
    admin_canvas.create_window(400, 200, window=year_entry)
    borrowed_entry = tkinter.Entry(admin_canvas)
    admin_canvas.create_window(400, 240, window=borrowed_entry)
    ISBN_entry = tkinter.Entry(admin_canvas)
    admin_canvas.create_window(400, 280, window=ISBN_entry)

    # Creating database for adding a new book
    def add_new_book():
        if id_entry.get() == "" or title_entry.get() == "" or author_entry.get() == "" or year_entry.get() == "" or borrowed_entry.get() == "" or ISBN_entry.get() == "":
            messagebox.showwarning("Warning", "All the fields are required!")
            con = pymysql.connect(host="localhost",
                                  user="root",
                                  password="root",
                                  database="librarydb",
                                  charset='utf8mb4',
                                  cursorclass=pymysql.cursors.DictCursor
                                  )
            curs = con.cursor()
            curs.execute(
                'Select * from books where idbooks=%s and name=%s and author=%s and year=%s and borrowed=%s and ISBN=%S',
                (id_entry.get(), title_entry.get(), author_entry.get(), year_entry.get(), borrowed_entry.get(),
                 ISBN_entry.get()))
            row = curs.fetchone()

        else:
            try:
                con = pymysql.connect(host="localhost",
                                      user="root",
                                      password="root",
                                      database="librarydb",
                                      charset='utf8mb4',
                                      cursorclass=pymysql.cursors.DictCursor
                                      )
                curs = con.cursor()
                curs.execute(
                    "insert into books(idbooks, name, author, year, borrowed, ISBN) values(%s, %s, %s, %s, %s, %s)",
                    (
                        id_entry.get(),
                        title_entry.get(),
                        author_entry.get(),
                        year_entry.get(),
                        borrowed_entry.get(),
                        ISBN_entry.get(),
                    ))
                con.commit()
                con.close()
                messagebox.showinfo("Success!", "The book was added! Now you can close this page.")
            except Exception as es:
                messagebox.showerror("Error!", f"Error due to: {str(es)}")

    add_book = Button(admin, text="Add", activebackground="#5c739d", activeforeground="white",
                      fg="#5c739d", bg="#E7F2F8", font=("Britannic Bold", 11), command=lambda: add_new_book())
    admin_canvas.create_window(400, 320, window=add_book)


root.mainloop()
