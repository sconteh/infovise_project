"""
INST326 - Final Project - InfoVise
<<<<<<< HEAD
Samuel Conteh, Dejon Young, Afaan Kamran, Jordan Lin
"""
import customtkinter
import sqlite3
import hashlib

class Database():
    def __init__(self):
        self.conn = sqlite3.connect("ischool_database.db") # connects sqlite3 to the ischool database file
        self.create_table() # create an instance of the singular table 

    def create_table(self):
        cur = self.conn.cursor() # the cursor for that connection is conn.cursor 
        # creating the table 
        cur.execute("""
        CREATE TABLE IF NOT EXISTS ischool_database (
                id INTEGER PRIMARY KEY,
                username VARCHAR(255) NOT NULL,
                password VARCHAR(255) NOT NULL,
                name VARCHAR(255) NOT NULL,
                major VARCHAR(255) NOT NULL,
                minor VARCHAR(255) NOT NULL
        )
        """)

    def insert_user(self, user):
        # creates the cursor object associated with the database connection. It enables traversal over the 
        # records in the database and execute SQL queries
        cur = self.conn.cursor()

        # insertion of the users information into the database
        cur.execute("INSERT INTO ischool_database (username, password, name, major, minor) VALUES (?, ?, ?, ?, ?)", 
                    (user.username, user.password, user.name, user.major, user.minor))

        self.conn.commit() # commits the current transaction to the database which ensures changes that are made are permanently stored

        # Hardcoded users for testing
        # username1, password1 = "mike123", hashlib.sha256("mikeisgreat333".encode()).hexdigest()
        # username2, password2 = "sam123", hashlib.sha256("samisgreat333".encode()).hexdigest()
        # print(username1, password1)
        # print(username2, password2)

class User():
    def __init__(self):
        self.username = ""
        self.password = "" 
        self.name = ""
        self.major = "" 
        self.minor = ""
    
    def masked_password(self):
        return '*', len(self.password)

    def create_account(self):
        print("\nAccount Creation")
        print("----------------")
    
        self.username = input("Enter your new username: ")
        self.password = input("Enter your new password: ")
        self.name = input("Enter the name associated with this account: ")
        self.major = input("Enter your declared or completed major: ")
        self.minor = input("Enter your delcared or completed minor (enter 'none' if you do not have one): ")
  
        print("\nAccount Created!\n")

def open_login_window():
    app = customtkinter.CTk()
    app.title("InfoVise Sign Up/Login Page")
    app.geometry("500x350")
    app.config(bg = '#4169E1')

    font1 = ("Archivo", 25, "bold")
    font2 = ("Roboto", 17, "bold")
    font3 = ("Roboto", 13, "bold")
    font4 = ("Roboto", 13, "bold", "underline")
    
    frame1 = customtkinter.CTkFrame(app, bg_color= '#4169E1', fg_color='#4169E1')
    frame1.place(x = 0, y = 0)
    image1 = PhotoImage(file="")
    image1_label = Label(frame1, image=image1, bg='#4169E1')
    image1_label.place(x =0, y = 0)

    signup_label = customtkinter.CTkLabel(frame1, font=font1, text='Sign Up', text_color='', bg_color = '')                            
    signup_label.place(x=280, y= 20)

    username_entry = customtkinter.CTkEntry(frame1, font=font2, text_color='', fg_color='', bg_color='', border_color='', 
                                            border_width=3, placeholder_text='Username', placeholder_text_color='', width=, height= ) 
    username_entry.place(x=230, y=80)

    password_entry =  customtkinter.CTkEntry(frame1, font=font2, fg_color='', text_color='', bg_color='')
    password_entry.place(x=, y=)
    app.mainloop()

def run_program():
    open_login_window()


def main():

    # print("\n***********************")
    # print("* WELCOME TO INFOVISE *")
    # print("***********************")

    created_database = Database()
    users = [] # list to store User instances (may be needed later)

    while True:
        print("\nOptions")
        print("1. Create a New Account")
        print("2. Exit\n")

        choice = input("Enter your choice (1-2): ")

        if choice == '1': # creating an account and inserting the user into the database
            
            created_user = User()
            created_user.create_account()
            created_database.insert_user(created_user)
        
        elif choice == '2': # exiting program
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please select a valid option (1-2)") 

if __name__ == "__main__":
    main() # Call the main function if the script is executed directly

