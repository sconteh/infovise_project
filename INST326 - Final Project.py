"""
INST326 - Final Project - InfoVise
Samuel Conteh, 
"""

class User():
    def __init__(self, username, password, education_level, major, minor, skills, name):
        self.username = username
        self.password = password
        self.education_level = education_level
        self.major = major 
        self.minor = minor
        self.skills = skills
        self.name = name

    # I have heard that this is not foolproof. Some considerations to improve security are:
    # Hashed passwords, salted hashes, authentication libraries, password policies, 
    
class Jobs():
    class GlassdoorJobs():
    
    class IndeedJobs():

def create_account():
    # Getting User Details
    print("\nAccount Creation")
    print("----------------")
    
    name = input("Enter the name associated with this account (first and last): ")
    major = input("Enter your declared or completed major: ")
    minor = input("Enter your delcared or completed minor (enter 'none'if you do not have one): ")
    # age = int(input("Enter your age: "))
    # gender = input("Enter your gender: ")

    user = User(name, major, minor) # creation of the instance of the user class  
    print("\nAccount Created!\n")
    user.display_details() # displaying the user information 
    return user # returns the created user 

def main():
    print("\n*********************")
    print("* WELCOME TO INFOVISE *")
    print("***********************")

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

if __name__ == "__main__":
    main() # Call the main function if the script is executed directly
    
