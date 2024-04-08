"""
INST326 - Final Project - InfoVise
Samuel Conteh, 
"""

import sqlite3
import hashlib

class User():
    def __init__(self, username, password, name, major, minor):
        self.username = username
        self.password = password 
        self.name = name
        self.major = major 
        self.minor = minor
    
    # I have heard that this is not foolproof. Some considerations to improve security are:
    # Hashed passwords, salted hashes, authentication libraries, password policies, 
    
# class Jobs():
    # class GlassdoorJobs():
    
    # class IndeedJobs():

def create_account():
    print("\nAccount Creation")
    print("----------------")
    
    username = input("Enter your new username: ")
    password = ("Enter your new password: ")
    name = input("Enter the name associated with this account: ")
    major = input("Enter your declared or completed major: ")
    minor = input("Enter your delcared or completed minor (enter 'none' if you do not have one): ")

    user = User(username, password, name, major, minor) # creation of the instance of the user class  
    print("\nAccount Created!\n")
    
    return username, password, name, major, minor 
def create_connection():
    # connect to the SQLite database 
    conn = sqlite3.connect("ischool_data.db") # connects to a ___ file
    return conn

def create_database(conn):
    cur = conn.cursor() # the cursor for that connection is conn.cursor 
    # creating the table 
    cur.execute("""
    CREATE TABLE IF NOT EXISTS ischool_data (
            id INTEGER PRIMARY KEY,
            username VARCHAR(255) NOT NULL,
            password VARCHAR(255) NOT NULL,
            name VARCHAR(255) NOT NULL,
            major VARCHAR(255) NOT NULL,
            minor VARCHAR(255) NOT NULL
    )
    """)

def insert_user(conn, username, password, name, major, minor):
    # creates the cursor object associated with the database connection. It enables traversal over the 
    # records in the database and execute SQL queries
    cur = conn.cursor()

    # insertion of the users information into the database
    cur.execute("INSERT INTO ischool_data (username, password, name, major, minor) VALUES (?, ?, ?, ?, ?)", 
                (username, password, name, major, minor))

    username1, password1 = "mike123", hashlib.sha256("mikeisgreat333".encode()).hexdigest()
    username2, password2 = "sam123", hashlib.sha256("samisgreat333".encode()).hexdigest()
    print(username1, password1)
    print(username2, password2)

    conn.commit() # commits the current transaction to the database which ensures changes that are made are permanently stored

def main(conn, username, password, name, major, minor):
    print("\n***********************")
    print("* WELCOME TO INFOVISE *")
    print("***********************")

    create_connection()
    create_database(conn)
    insert_user(conn, username, password, name, major, minor)
    create_account()


    """
        users = [] # list to store User instances  

    while True:
        print("\nOptions")
        print("1. Create a New Account")
        print("2. Exit\n")

        choice = input("Enter your choice (1-2): ")

        if choice == '1': # creating an account 
            user = create_account()
            users.append(user)
        
        elif choice == '2': # exiting program
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please select a valid option (1-5).") 
    
    """

if __name__ == "__main__":
    conn = create_connection()
    username, password, name, major, minor = create_account()
    main(conn, username, password, name, major, minor) # Call the main function if the script is executed directly


