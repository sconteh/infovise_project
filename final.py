
"""

INST326 Final Project - Samuel Conteh 

Documentation: 

Our project is InfoVise, a terminal-based application that recommends the user potential career paths based on 
classes that they have actually or hypothetically taken. We offer an account feature that allows one to create an account, 
change their password if need be, print the available differntiable classes offered at the iSchool, and add courses to their 
specific account.    

Since our program runs off of terminal, all  one would need to do to run it is to enter "python/python3 final.py" within the 
directory in which the file is located. Here's an example: 

PS C:\Users\conte\OneDrive\Desktop\College\JUNIOR YEAR CLASSES\SPRING2024\INST326> python final.py

Then, the user can interact with the number based menu system. To interact with it, all 
you would need to do is enter the number that corresponds with the action that you would like to do and follow the instructions. 
Once you make a number action, you cannot go back! To exit the program, you would press 6 and enter when on the main menu.

Annotated Bibliography: 

Diveintopython. (n.d.). Update(). Dive into Python: Free Tutorials, Books to Learn Python. 
    https://diveintopython.org/functions/dictionary-methods/update


    We utlized this website to better understand how to use update(). This built-in function aided us going into the self 
    for the user and updating the possible career option for them. 

    
Programiz. (n.d.). Python Dictionary items(). Programiz: Learn to Code for Free. 
    https://www.programiz.com/python-programming/methods/dictionary/items

    To print out all of the Cognate Classes that one could take at the iSchool, we needed a for loop. And in that for loop, 
    items was used to access the variable_classes dictionary. 

Uejio, J. (n.d.). Immutable vs. Hashable – Real Python [Video]. Python Tutorials – Real Python. 
    https://realpython.com/lessons/immutable-vs-hashable/

    Throughout our code, we were facing issues with making sure that the courses taken and the potential career paths 
    that the user could take were only mentioned once. This require us to understand mutability, hashability, and how that relates 
    to lists vs. sets. This ultimately led use to using sets within our code. 
"""

# START OF CODE!
variable_classes = {
    "INST341": {"name": "Introduction to Digital Curation","career_paths": ["Data Analyst", "Digital Archivist", "Digital Specialist", "UX/UI Development"], "credits": "N/A"},
    "INST354": {"name": "Decision-Making for Information Science","career_paths": ["Artificial Intelligence/Machine Learning", "Data Analyst", "Data Engineer", "Data Scientist"],"credits": "N/A"},
    "INST364": {"name": "Human-Centered Cybersecurity","career_paths": ["Cybersecurity Analyst", "Cybersecurity Engineer", "Ethical Hacker", "Information Security Analyst/Specialist"],"credits": "N/A"},
    "INST365": {"name" : "Ethical Hacking","career_paths": ["Cybersecurity Analyst", "Cybersecurity Engineer", "Ethical Hacker", "Information Security Analyst/Specialist"],"credits": "N/A"},
    "INST366": {"name": "Privacy, Security and Ethics for Big Data","career_paths": ["Cybersecurity Analyst", "Cybersecurity Engineer", "Ethical Hacker", "Information Security Analyst/Specialist"],"credits": "N/A"},
    "INST367": {"name": "Prototyping and Development Studio","career_paths": ["Data Analyst", "Digital Archivist", "Digital Specialist", "UX/UI Development"],"credits": "N/A"},
    "INST377": {"name": "Dynamic Web Applications","career_paths": ["Data Analyst", "Digital Archivist", "Digital Specialist", "UX/UI Development"],"credits": "N/A"},
    "INST401": {"name": "Design and Human Disability and Aging","career_paths": ["Healthcare Data Analyst", "Healthtech Software Engineer", "IT Specialist"],"credits": "N/A"},
    "INST402": {"name": "Designing Patient-Centered Technologies", "career_paths": ["Healthcare Data Analyst", "Healthtech Software Engineer", "IT Specialist"],"credits": "N/A"},
    "INST414": { "name": "Data Science Techniques", "career_paths": ["Artificial Intelligence/Machine Learning", "Data Analyst", "Data Engineer", "Data Scientist"],"credits": "N/A"},
    "INST441": {"name": "Information Ethics and Policy", "career_paths": ["Healthcare Data Analyst", "Healthtech Software Engineer", "IT Specialist"], "credits": "N/A"},
    "INST442": {"name": "Digital Curation Across Disciplines", "career_paths": ["Data Analyst", "Digital Archivist", "Digital Specialist", "UX/UI Development"], "credits": "N/A"},
    "INST443": {"name": "Tools and Methods for Digital Curation", "career paths": ["Data Analyst", "Digital Archivist", "Digital Specialist", "UX/UI Development"], "credits": "N/A"},
    "INST447": {"name": "Data Sources and Manipulation", "career_paths": ["Artificial Intelligence/Machine Learning", "Data Analyst", "Data Engineer", "Data Scientist"], "credits": "N/A"},
    "INST448": {"name": "Digital Curation Research in Cultural Big Data Collections", "career_paths": ["Data Analyst", "Digital Archivist", "Digital Specialist", "UX/UI Development"], "credits": "N/A"},
    "INST452": {"name": "Health Data Analytics", "career_paths": ["Healthcare Data Analyst", "Healthtech Software Engineer", "IT Specialist"], "credits": "N/A"},
    "INST462": {"name": "Introduction to Data Visualization", "career_paths": ["Artificial Intelligence/Machine Learning", "Data Analyst", "Data Engineer", "Data Scientist"], "credits": "N/A"}, 
    "INST464": {"name": "Decision Making for Cybersecurity", "career_paths": ["Cybersecurity Analyst", "Cybersecurity Engineer", "Ethical Hacker", "Information Security Analyst/Specialist"], "credits": "N/A"},
    "INST466": {"name": "Technology, Culture, and Society", "career_paths": ["Artificial Intelligence/Machine Learning", "Data Analyst", "Data Engineer", "Data Scientist", "Social Media Analyst", "UX/UI Development"], "credits": "N/A"},
    "INST467": {"name": "Fundamentals of Cybersecurity for Policy Makers", "career_paths": ["Cybersecurity Analyst", "Cybersecurity Engineer", "Ethical Hacker", "Information Security Analyst/Specialist"], "credits": "N/A"},
}

class User():
    """
    Purpose: Holds all of the pertinent information of the user. 
    Self: 
        Username: the actual username of the user  
        Password: the actual password of the user 
        fname: the first name of the user 
        lname: the last name of the user 
        courses_taken: all the courses the user has taken
        career_paths: the recommended career paths associated with the courses the user has taken 
    """
    def __init__(self, username, password, fname, lname):
        self.username = username
        self.password = password
        self.fname = fname
        self.lname = lname
        self.courses_taken = set()
        self.career_paths = set()

    def add_courses(self, variable_classes):
        """
        Purpose: Adds the courses to the Users profile
        Arguments:
            variable_classes: reference to the variable_class dictionary (contains the classes that can 
            differentiate InfoSci students)
        """
        while True:
            course_codes = input("\nEnter the course codes separated by commas (or 'done' to finish): ")
            if course_codes.lower() == 'done':
                break
            
            # split the input by commas and remove any leading/trailing spaces
            split_course_codes = [code.strip().upper() for code in course_codes.split(',')]

            # validate and add each course code to the courses_taken set
            for x in split_course_codes:
                if x in variable_classes: # if the read course is in the variable_classes dictionary
                    course_info = variable_classes[x] # set that position as course_info
                    self.courses_taken.add(x) # adds the course taken into the specific profile
                    print(f"'{course_info['name']}' added to your account.")
                else:
                    print(f"Invalid course code '{x}'. Please try again.")

    def authenticate(self, entered_password):
        """
        Purpose: Returns the entered password to the User class 
        Arguments:
            entered_password: the password entered by the user
        """
        return entered_password == self.password
        
    def change_password(self, old_password, new_password):
        """
        Purpose: allows the user to change the password to their account.
        Arguments:
            old_password: the users old password
            new_password: the password that the user would like to change to 
        """
        if self.authenticate(old_password): # once the authentication goes through 
            self.password = new_password # set the user's password to whatever they input as the new_password 
            print("Password changed successfully!")
        else:
            print("Unable to change password: Incorrect old password.")

    def print_courses_taken(self):
        """
        Purpose: prints the courses that the user has taken 
        Arguments: None 
        """
        if self.courses_taken:
            print("Courses Taken:")
            for course in self.courses_taken: # iterates through all of the courses taken and prints them out 
                print(course)
        else:
            print("No courses taken yet.")
            
    def recommend_career_paths(self, variable_classes):
        """
        Purpose: recommends the career paths associated with the courses taken and puts it into the users account
        Arguments:
            variable_classes: reference to the variable_class dictionary (contains the classes that can 
            differentiate InfoSci students)
        """
        if self.courses_taken: # if within courses taken by the user 
            for course in self.courses_taken: # initiate a for loop that determines 
                if course in variable_classes: # the specific courses that is within variable_classes
                    # get the associated potential career paths   
                    possible_career_paths = variable_classes[course].get("career_paths", []) 
                    # and update it within the users career_path set 
                    self.career_paths.update(possible_career_paths)

            # prints it out
            if self.career_paths:  
                print("\nRecommended Career Paths:")
                for path in self.career_paths:
                    print(path)
            else:
                print("No recommended career paths based on the courses taken.")
        else:
            print("No courses taken yet.")


def access_user(main_users):
    """
    Purpose: helps access the specific account of the user. For this, the username and password is required  
    Arguments: 
        main_users: the list that the objects are being put in
    """
    # ask for the user's username and password 
    print("Enter your username and password for the account you would like to access: ")
    entered_username = input("Username: ")
    entered_password = input("Password: ")

    for created_user in main_users:
        if created_user.username == entered_username and created_user.authenticate(entered_password):
            print("\nValid username and password. Signing in...")
            return created_user
            
    print("Invalid username or password. Please try again.")
    return None 
    
def create_account():
    """
    Purpose: helps the user create their account (which is necessary for any of the other features)
    Arguments: None
    """
    # Getting User Details
    print("\n*****************************************************")
    print("* ACCOUNT CREATION - ENTER ALL INFORMATION AS SHOWN *")
    print("*****************************************************")

    # obtain all of the user's important information 
    fname = input("Enter your first name: ")
    lname = input("Enter your last name: ")
    username = input("Enter your username: ")
    password = input("Enter your new password: ")

    # print it out for the user 
    print("Entered username:", username)
    print("Entered password:", password)

    created_user = User(username, password, fname, lname) # creation of the instance of the user class  
    print("\nAccount Created!\n")
    return created_user

def print_info_header():
    """
    Purpose: Simple print statement to welcome the user 
    Arguments: None 
    """
    print("\n********************************")
    print("* WELCOME TO INFOVISE DATABASE *")
    print("********************************")

def print_goodbye():
    """
    Purpose: Simple print statement to saying farewell the user 
    Arguments: None 
    """
    print("\n********************************")
    print("* THANK YOU FOR USING INFOVISE! *")
    print("********************************")

    print("Exiting Program...")

def print_menu_options():
    """
    Purpose: Simple print statement to print the menu 
    Arguments: None 
    """
    print("\nOptions")
    print("1. Create a New Account")
    print("2. Add Courses to Account")
    print("3. Change Password")
    print("4. Print Classes Offered By iSchool")
    print("5. Print Courses Taken By User")
    print("6. Recommend Career Paths")
    print("7. Exit Program")

def print_no_accounts(): 
    """
    Purpose: Simple print statement for when no accounts are found
    Arguments: None 
    """
    print("\n-----------------------------------------------------------------------")
    print("No accounts found. An account must be created first before depositing")
    print("-----------------------------------------------------------------------")

def print_variable_classes(variable_classes):
    """
    Purpose: Prints all of the classes that can differentiate Information Science students   
    Arguments: reference to the variable_class dictionary (contains the classes that can 
    differentiate InfoSci students)
    """
    print("\nCognate Area Classes Offered:")
    for course_code, course_info in variable_classes.items():
        course_name = course_info["name"]
        print(f"{course_code} - {course_name}")

def main():
    main_users = [] # list to store User instances (may be needed later)
    print_info_header()

    while True:
        print_menu_options()

        choice = input("Enter your choice (1-7): ")

        if choice == '1': # creating an account and inserting the user into the database
            created_user = create_account()
            main_users.append(created_user)

        elif choice == '2':
            if main_users:
                found_user = access_user(main_users)
                if found_user:
                    found_user.add_courses(variable_classes)
                else: 
                    print("No matching account found.")
            else:    
                print_no_accounts()

        elif choice == '3':
            if main_users:
                found_user = access_user(main_users)
                if found_user:
                    old_password = input("Enter your old password: ")
                    new_password = input("Enter your new password: ")
                    found_user.change_password(old_password, new_password)
                else:
                    print("No matching account found. Please try again.")
            else:
                print_no_accounts()

        elif choice == '4':
            print("For this program , we are only going to take into account the classes that can differentiate each Information Science Student from another.")
            print("These essentially include the four cognate areas: Cybersecurity & Privacy, Data Science, Digital Curation, and Health Information")
            print_variable_classes(variable_classes)
        
        elif choice == '5':
            if main_users:
                found_user = access_user(main_users)
                if found_user:
                    found_user.print_courses_taken()
        
        elif choice == '6':
            if main_users:
                found_user = access_user(main_users)
                if found_user:
                    found_user.recommend_career_paths(variable_classes)

        elif choice == '7': # exiting program
            print_goodbye()
            break

        else:
            print("Invalid choice. Please select a valid option (1-3)") 

if __name__ == "__main__":
    main() # Call the main function if the script is executed directly
