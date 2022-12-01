
# Program begins with a welcome message to the user, formatted to improve experience
program_welcome = "Welcome to the Task Manager"
print("="*len(program_welcome))
print(program_welcome)
print("="*len(program_welcome))
print()

#===== importing libraries ===========
import string
from datetime import date
from datetime import datetime

#==== Login Section ====

# To validate the user login credentials
# First, we create a dictionary 'valid_login_credentials' that will that will contain usernames as keys and the passwords as values
# We set two lists, that store the registered users and registered passwords
valid_usernames = []
valid_passwords = []

# Reading the user.txt file, for every line of usernames and passwords, we populate the two lists with their respective elements 
with open('user.txt', 'r') as user_file :

    for line in user_file :
        user_credentials = line.split(", ")
        valid_usernames.append(user_credentials[0])
        valid_passwords.append(user_credentials[1].strip("\n"))

# With the extracted usernames and passwords, we create the dictionary 'valid_login_credentials' using a for loop to populate it
valid_login_credentials = {}

# usernames are stored as keys, passwords as values
for i in range(len(valid_usernames)) :
    valid_login_credentials[valid_usernames[i]] = valid_passwords[i]

# Now, we request user to enter login credentials and create a list with their input as ['username', 'password']
login = input("Log in with your username and password | Type in 'username, password': ")
user_login_credentials = login.split(", ")

# Error handling: check that the user inputs the username and password in a format that the program can read
# while the username and password are not entered as 'username, password', the program requests the user to retry
while len(login.split(", ")) != 2 :
    print("\nLogin error. Retype your username, followed by a comma, a space and then the password.\n")
    login = input("Log in with your username and password | Type in 'username, password': ")
    user_login_credentials = login.split(", ")

# if there are no errors in the input format, the program stores the username and password input into 2 variables
login_username = user_login_credentials[0]
login_password = user_login_credentials[1]

# Error handling: check that the username exists, that is, that the login credentials are valid
# while the username input is not found in the list of valid credentials
# we display an error message to the user and request the user to input username and password again
while not login_username in valid_login_credentials :
    print("\nInvalid username. Please enter a valid username and password to log in.\n")
    login = input("Log in with your username and password | Type in 'username, password': ")
    user_login_credentials = login.split(", ")
    
    # because we request the user to input these values again, we must check again for potential format errors
    # we perform the same error handling steps than in the 1st error handling section
    while len(login.split(", ")) != 2 :
        print("\nLogin error. Retype your username, followed by a comma, a space and then the password.\n")
        login = input("Log in with your username and password | Type in 'username, password': ")
        user_login_credentials = login.split(", ")
    
    login_username = user_login_credentials[0]
    login_password = user_login_credentials[1]

# by this step, the user has entered a valid username and the format of the input is correct

# Error handling: user enters a valid username but invalid password
# while the password value does not match the username key in the dictionary
# we request the user to retry
while login_password != valid_login_credentials[login_username] :
    print("\nWrong password. Please enter the correct password to log in.\n")
    login_password = input("Type in your password: ")

# once the user has succesfully input a valid username and a valid password, we display a message
print()
print("Login Successful.")
print("_"*100 + "\n")


#==== Options Menu ====

while True:

    # we present the menu to the user and convert the input to lower case.
    menu_welcome = "Options Menu"
    print(menu_welcome)
    print("="*len(menu_welcome))
    print()
    
    print("Please select one of the following Options:\n")

    # we display 2 sets of menus, one for the admin with the added Statistics option and one without for the regular user
    if login_username == 'admin' :

        print("r\t- Registering a user\na\t- Adding a task\nva\t- View all tasks\nvm\t- View my task\ns\t- Statistics\ne\t- Exit\n")
        menu = input("Option selected: ").lower()

    if login_username != 'admin' :

        print("r\t- Registering a user\na\t- Adding a task\nva\t- View all tasks\nvm\t- View my task\ne\t- Exit\n")
        menu = input("Option selected: ").lower()
    
    print("_"*100 + "\n")

    #==== Registering a user ====

    # only admins can access the Register a user option
    if menu == 'r' and login_username == 'admin':
        
        user_reg_welcome = "Register a user"
        print(user_reg_welcome)
        print("="*len(user_reg_welcome))
        print()

        # we ask the user to enter a username for the new user they want to register
        new_username = input("Please enter a new Username: ") 

        # Error handling: check if the username already exists
        # while the new username input is found as a key in the valid credentials dictionary
        # we request the user to enter a new username 
        while new_username in valid_login_credentials.keys() :
            print("\nUsername already exists.\n")
            new_username = input("Please enter a new Username: ")
        
        # Error handling: username cannot contain special characters or " "
        # we first create a list of all the characters we do not allow in a username
        special_chars = list(string.punctuation + " ")
        
        # using the any() method to iterate through all the characters in the list
        # while any of these characaters are found in the new username, we display an error message
        # and request the user to input a new username
        while any((char in special_chars) for char in new_username) == True :
            print("\nWrong input. Username cannot contain special characters.\n")
            new_username = input("Please enter a new Username: ")
        
        # at this step, the new username is valid
        # we now request the user to input a new password and retype it to perform a password check
        new_password = input("\nPlease enter a new Password: ")
        new_password_check = input("\nTo confirm the new Password, please retype it: ")
        
        # while the two inputs don't have an exact match, we request the user to enter them again
        while new_password != new_password_check :
            print("\nPasswords do to match.\n")
            new_password = input("\nPlease enter a new Password: ")
            new_password_check = input("\nTo confirm the new Password, please retype it: ")

        # at this step, the user has successfully enter a valid new username and new password
        # we add the new username and password in the format 'username, password' to a new line in the user.txt registry
        with open('user.txt', 'a+') as user_file :
            user_file.write("\n")
            user_file.write(f"{new_username}, {new_password}")

        # once we have the new username and password in the text file, we need to update the valid_login_credentials dictionary
        # to do this, we use the update method to add the new key and value
        valid_login_credentials.update({new_username: new_password})

        # once every step in this section has been successfully executed, we display a message to the user
        print()
        print(f"Success! User '{new_username}' has been registered.")
        print("_"*100 + "\n")

    # if the user is not 'admin', we prompt a message to the user requesting them to contact the admin
    elif menu == 'r' and login_username != 'admin':

        print("Unauthorized Access. Please contact the admin to register a new user.\n")
        print("_"*100 + "\n")


    #==== Adding a task ====
    elif menu == 'a':

        user_reg_welcome = "Adding a task"
        print(user_reg_welcome)
        print("="*len(user_reg_welcome))
        print()
        
        # we request the user to type in the username the task will be assigned to
        task_user = input("Who is the task assigned to? | Type in the Username: ")

        # Error handling: we check if the username input exists in the user registry
        # while the input is now found in the valid credentials dictionary keys
        # we display and error message and request the user to retry
        while not task_user in valid_login_credentials.keys() :
            print("\nUser not found.\n")
            task_user = input("Please type in a valid username: ")
        
        print(f"\nTask assigned to {task_user}\n")
        
        # we request the user to input a title for the task
        task_title = input("Task Title: ")
        print()

        # we request the user to input a description for the task
        task_description = input("Task Description: ")
        print()

        # using the imported libraries, we set the task's creation date as the current date / today
        today = date.today()
        creation_date = today.strftime('%d %b %Y')
        print(f"Task Creation Date: {creation_date}\n")  
        
        # we request the user to set a due date for the task (in a specific format that the program can read)
        due_date = input("Task Due Date | type as DD/MM/YYYY: ")
        
        # Error handling: the user does not input a valid date in the correct format
        # we set a boolean to True
        format_check = True
        
        # we test the input date for errors in the required format
        # if the format is correct (no error), the program moves to the next step
        # if there is a ValueError due to wrong format, we display an error message and set the boolean to False
        try:
            due_date = datetime.strptime(due_date, "%d/%m/%Y")
        except ValueError :
            print("\nWrong date format. Please retry.\n")
            format_check = False

        # while the boolean is False, the program requests the user to input the due date again
        # tests the block for errors as seen above and repeats until the date input is in the correct format
        while format_check == False :
            due_date = input("Task Due Date | type as DD/MM/YYYY: ")    
            try:
                due_date = datetime.strptime(due_date, "%d/%m/%Y")
                format_check = True
            except ValueError :
                print("\nWrong date format. Please retry.\n")
                format_check = False
        
        # Error handling: once the date is in the correct format, we must check that it is not less than the current date
        # while the due date is less than the current date
        # we display an error message and request the user to input the date again
        while datetime.date(due_date) < today :

            print("\nTask Due Date cannot be less than Current Date.\n")

            due_date = input("Task Due Date | type as DD/MM/YYYY: ")

            # Error handling: because we request another date input, the user can enter it in a wrong format
            # therefore, we nest the try and while method above to test for date format errors until the user enters the correct format
            format_check = True

            try:
                due_date = datetime.strptime(due_date, "%d/%m/%Y")
            except ValueError :
                print("\nWrong date format. Please retry.\n")
                format_check = False

            while format_check == False :
                due_date = input("Task Due Date | type as DD/MM/YYYY: ")    
                try:
                    due_date = datetime.strptime(due_date, "%d/%m/%Y")
                    format_check = True
                except ValueError :
                    print("\nWrong date format. Please retry.\n")
                    format_check = False

        # using the due date input, we cast it as a string with the desired format to output it into the txt file
        due_date_output = due_date.strftime('%d %b %Y')

        print(f"\nTask Due Date: {due_date_output}")

        # we set task completed as 'No'
        task_completed = "No"

        # we amend the tasks.txt file with the new task information in the same format as the existing task data
        with open('tasks.txt', 'a+') as tasks_file :
            tasks_file.write("\n")
            tasks_file.write(f"{task_user}, {task_title}, {task_description}, ")
            tasks_file.write(f"{creation_date}, {due_date_output}, {task_completed}")

        # we print a success message to the user
        print()
        print(f"Success! A task has been assigned to '{task_user}'.")
        print("_"*100 + "\n")

    #==== View my tasks ====
    elif menu == 'vm':

        user_reg_welcome = "View my tasks"
        print(user_reg_welcome)
        print("="*len(user_reg_welcome))
        print()

        # we set a list that will contain all task data read from the tasks.txt file
        my_task_data = []

        with open('tasks.txt', 'r') as f :
            
            # for every line in tasks.txt, strip the new line char
            # split the content by ", " and append them to the list set above
            for line in f :
                my_task_data += line.strip("\n").split(", ")
        
        # for every element in the list
        # if the element is equal to the logged in user's username
        # we print the task data based on the element's position on the list relative to the username element
        for i in range(0, len(my_task_data)) :
            if login_username == my_task_data[i] :
                print(f"Task:\t\t\t{my_task_data[i + 1]}")
                print(f"Assigned to:\t\t{my_task_data[i]}")
                print(f"Date assigned:\t\t{my_task_data[i + 3]}")
                print(f"Due date:\t\t{my_task_data[i + 4]}")
                print(f"Task complete?\t\t{my_task_data[i + 5]}")
                print(f"Task description:\n {my_task_data[i + 2]}")
                print("_"*100 + "\n")

    #==== View all tasks ====
    elif menu == 'va':

        user_reg_welcome = "View all tasks"
        print(user_reg_welcome)
        print("="*len(user_reg_welcome))
        print()

        # we set a list that will contain all task data read from the tasks.txt file
        all_task_data = []

        with open('tasks.txt', 'r') as f :

            # for every line in tasks.txt, strip the new line char
            # split the content by ", " and append them to the list set above
            for line in f :
                all_task_data += line.strip("\n").split(", ")
        
        # using a while loop to iterate through the list of task data
        # we set i as a counter with value 0
        # the loop starts at the first element of the list, which is the first username registered
        # we print all the task information relevant to that element's position (5 elements in total)
        # to jump to the next task, we add 6 to i (therefore skipping through all the elements in the initial task)
        i = 0
        while i in range(0, len(all_task_data)) :
            print(f"Task:\t\t\t{all_task_data[i + 1]}")
            print(f"Assigned to:\t\t{all_task_data[i]}")
            print(f"Date assigned:\t\t{all_task_data[i + 3]}")
            print(f"Due date:\t\t{all_task_data[i + 4]}")
            print(f"Task complete?\t\t{all_task_data[i + 5]}")
            print(f"Task description:\n {all_task_data[i + 2]}")
            print("_"*100 + "\n")
            i += 6

    # in case a user that's not an admin types 's' as an option by mistake, we restrict their access
    elif menu == 's' and login_username != 'admin':

        print("Unauthorized Access.")
        print("_"*100 + "\n")

    #==== Statistics (admin only) ====
    elif menu == 's' and login_username == 'admin':

        statistics_welcome = "Statistics"
        print(statistics_welcome)
        print("="*len(statistics_welcome))
        print()
        
        # with the content from user.txt file
        with open('user.txt', 'r') as user_file :
            
            # because each line represents a user
            # we can count how many users using a for loop that iterates through each line
            users_counter = 0
            for line in user_file :
                users_counter += 1
        
        with open('tasks.txt', 'r') as tasks_file :

            # because each line represents a task
            # we can count how many tasks using a for loop that iterates through each line
            tasks_counter = 0
            for line in tasks_file :
                tasks_counter += 1
        
        # we print the statistics to the admin
        print(f"Total Tasks:\t\t{tasks_counter}\n")
        print(f"Registered Users:\t{users_counter}\n")
        print("_"*100 + "\n")

    elif menu == 'e':
        print('Goodbye!!!')
        print("_"*100 + "\n")
        exit()

    else:
        print("\nWrong entry. Option selected does not exist.\n")
        print("Please try again by typing a valid letter from the Options menu.\n")
        print("_"*100 + "\n")
