"""
INST326 - Final Project - InfoVise
Samuel Conteh, Dejon Young, Afaan Kamran, Jordan Lin
"""
import customtkinter as ctk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
# from customtkinter import filedialog, Label, PhotoImage
import sqlite3
import hashlib
import requests
import os

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

"""
def select_image_directory():
    directory = filedialog.askdirectory()
    if directory:
        return directory
    else:
        print("No directory selected.")
        return None

"""

name_of_login_file = ""

def select_directory():
    return filedialog.askdirectory()

def download_login_image():
    # <a href="https://www.freepik.com/free-ai-image/futurism-perspective-digital-nomads-lifestyle_138709280.htm#fromView=search&page=1&position=0&uuid=0a802735-0108-4504-a4a6-36b7474cc29e">Image by freepik</a>
    login_image_url = "https://www.freepik.com/free-ai-image/futurism-perspective-digital-nomads-lifestyle_138709280.htm#fromView=search&page=1&position=0&uuid=0a802735-0108-4504-a4a6-36b7474cc29e"
    response = requests.get(login_image_url)
    if response.status_code == 200:
        selected_directory = select_directory()
        if selected_directory:
            default_filename = "default_image.jpg"  # Default filename
            selected_filename = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG files", "*.jpg"), ("All files", "*.*")], initialdir=selected_directory, initialfile=default_filename)
            if selected_filename:
                with open(selected_filename, 'wb') as file:
                    file.write(response.content)
                print("Image downloaded successfully.")
                name_of_login_file = selected_filename
                return name_of_login_file  # Return the selected filename for further use
            else:
                print("Image download canceled by user.")
                return None  # Return None if download is canceled
        else:
            print("No directory selected. Image download canceled.")
            return None  # Return None if no directory selected
    """
def download_login_image():
    # <a href="https://www.freepik.com/free-ai-image/futurism-perspective-digital-nomads-lifestyle_138709280.htm#fromView=search&page=1&position=0&uuid=0a802735-0108-4504-a4a6-36b7474cc29e">Image by freepik</a>
    login_image_url = "https://www.freepik.com/free-ai-image/futurism-perspective-digital-nomads-lifestyle_138709280.htm#fromView=search&page=1&position=0&uuid=0a802735-0108-4504-a4a6-36b7474cc29e"
    
    file_name = os.path.basename(login_image_url) # Get the filename from the URL
    save_path = os.path.join(save_path, file_name)  # Define the full path to save the image
    response = requests.get(login_image_url) # send a get request to the website in which we got the login image from

    # check if the request was successful (which is represented by status code 200)
    if response.status_code == 200:
        image_content = response.content # access the content within the image 

        with open("image.jpg", "wb") as file: # save the image locally (within the individual device)
            file.write(image_content)

        # Open the image file
        try:
            image = Image.open("sign_in_page_image.jpg")
            tk_image = ImageTk.PhotoImage(image) # converts the image to a format suitable for Tkinter

        except Exception as e:
            print("Error loading image:", e) # loads a blank placeholder image if there's an error with loading the intended image file
            image = Image.new("RGB", (100, 100), "white") # Create a blank white image (you can adjust the size as needed)

            tk_image = ImageTk.PhotoImage(image)

            # Display the image in a Tkinter label or canvas
            # Replace this with your code to display the image
    else:
        # if the request fails to go through, print an error message
        print("Failed to download the image.")
    """
def open_login_window():
    download_login_image()
    
    app = ctk.CTk()
    app.title("InfoVise Sign Up/Login Page")
    app.geometry("450x360")
    app.config(bg = '#4169E1')

    font1 = ("Helvetica", 25, "bold")
    font2 = ("Roboto", 17, "bold")
    font3 = ("Roboto", 13, "bold")
    font4 = ("Roboto", 13, "bold", "underline")
    
    frame1 = ctk.CTkFrame(app, bg_color= '#4169E1', fg_color='#4169E1', width=470, height=360)
    frame1.place(x = 0, y = 0)

    image1 = PhotoImage(file=name_of_login_file)
    image1_label = Label(frame1, image=image1, bg='#4169E1')
    image1_label.place(x =0, y = 0)

    signup_label = ctk.CTkLabel(frame1, font=font1, text='Sign Up', text_color='#fff', bg_color = '#4169E1')                            
    signup_label.place(x=280, y= 20)

    username_entry = ctk.CTkEntry(frame1, font=font2, text_color='#fff', fg_color='#6941E0', bg_color='#4169E1', border_color='#41B9E0', 
                                            border_width=3, placeholder_text='Username', placeholder_text_color='#A3A3A3', width=200, height=500) 
    username_entry.place(x=230, y=80)

    password_entry = ctk.CTkEntry(frame1, font=font2, show = '*', fg_color='#6941E0', text_color='#fff', bg_color='#4169E1')
    password_entry.place(x=230, y=150)

    signup_button = ctk.CTkButton(frame1, font=font2, text_color='#fff', text = 'Sign Up', fg_color ='#E0B941', hover_color = '#000680 ', bg_color='#121111', cursor='hand2', corner_radius=5, width=120)
    signup_button.place(x=230, y=220)

    login_button = ctk.CTkButton(frame1, font=font4, text_color='#00BF77', text='Login', fg_color='#4169E1', hover_color='#4169E1',cursor='hand2', width=40)
    login_button.place(x=395, y=250)
    app.mainloop()
    
 
def run_program():
    open_login_window()


def main():
    run_program()
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

