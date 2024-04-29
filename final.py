
class User():
    def __init__(self, username, password, name):
        self.username = username
        self.password = password
        self.name = name

    def authenticate(self, entered_password):
        return entered_password == self.password
    
    def change_password(self, old_password, new_password):
        if self.authenticate(old_password):
            self.password = new_password
            print("Password changed successfully!")
        else:
            print("Unable to change password: Incorrect old password.")

    def display_details(self):
        print("\n")
        print(f"Personal Details of {self.name}")


def access_user(users):
    print("Enter your username and password for the account you would like to access: ")
    entered_username = input("Username: ")
    entered_password = input("Password: ")

    for person in users:
        if person.username == entered_username and person.authenticate(entered_password):
            return person
            
    print("Invalid username or password. Please try again.")
    return None 
    
def create_account(self):
    # Getting User Details
    print("Before we can create a11 bank account, you must first create a username and password associate with it. Enter \"back")

    username = input("Enter your username: ")
    first_entered_password = input("Enter your password: ")
    second_entered_password = input("Enter your password again: ")

    if first_entered_password == second_entered_password:
        created_user = User(username, first_entered_password) # creation of the instance of the user class  
        print(f"\nAccount Created {self.name}!\n")
        created_user.display_details() # displaying the user information
        
        return created_user # returns the created user 

    else:
        print("Error: passwords do not match")    
    
def print_info_header():
    print("\n*********************************")
    print("* WELCOME TO INFOVISE DATABASE *")
    print("*********************************")

def print_menu_options():
    print("\nOptions")
    print("1. Create a New Account")
    print("2. Print User Details")
    print("3. Exit Program")

def print_no_accounts(): 
    print("\n-----------------------------------------------------------------------")
    print("No accounts found. An account must be created first before depositing")
    print("-----------------------------------------------------------------------")

def main():
    users = [] # list to store User instances (may be needed later)
    print_info_header()

    while True:
        print_menu_options()

        choice = input("Enter your choice (1-2): ")

        if choice == '1': # creating an account and inserting the user into the database
            account_creation = create_account()
            users.append(account_creation)
        
        # elif choice == '2':
            
        elif choice == '3': # exiting program
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please select a valid option (1-3)") 

if __name__ == "__main__":
    main() # Call the main function if the script is executed directly
