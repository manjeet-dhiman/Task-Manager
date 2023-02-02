#=====import libraries=====#
# needed for today's date
from datetime import datetime

#=====coloured terminal responses=====#
# for colour text in terminal output using ANSI code for clear responses
RED = "\033[91m"
GREEN = "\033[32m"
PURPLE = '\033[95m'
YELLOW = '\033[93m'
# resets colour to default
RESET = "\033[0m"

#=====functions=====#
# function for registering a new user
def reg_user():
    # only allow new user entry if admin has logged in
    if username_input == 'admin':

    # check if username entered is already taken
        while True:
            new_user = input("\nEnter a new username: ").lower()
            if new_user in details_dict.keys():
                print(f"{RED}The username is already taken, please type another.{RESET}")
            else:
                break

        # ask for a password
        new_password = input("\nEnter a password for the new user: ")
    
        # asks to confirm their password
        while True:
            check_password = input("\nConfirm your password: ")
            if new_password == check_password:
                print(f"{GREEN}The new user is added.{RESET}\n")
                break
            else:
                print(f"{RED}The password does not match. Please try again.{RESET}")
                continue

        # opens the file for append writing only, adds to the end
        users_file = open('user.txt', 'a', encoding='utf-8')

        # adds username and password to user.txt on a new line matching the formatting
        users_file.write("\n" + new_user + ", " + new_password)

        # closes file after use
        users_file.close()
    
    # if admin not logged in show error message
    else:
        print(f"{RED}Only admin is allowed to register new users.\n{RESET}")
        
# function to add a new task
def add_task():
    """
    checks if user entered is in username list
    if not a valid user, ask for a registered user
    """
    while True:
        username = input("\nWhich user will be carrying out the task?\n").lower()
        if username in details_dict.keys():
            print(f"\n{GREEN}{username} will carry out this task.{RESET}\n")
            break
        else:
            print(f"{RED}The user does not exist. Please try again.{RESET}")

    task_title = input("What is the title of the task?\n")
    print(f"\n{GREEN}The title of the task is:{RESET} {task_title}")

    task_description = input("\nDescribe the task?\n")
    print(f"\n{GREEN}Task description:{RESET} {task_description}")

    """
    use datetime library to enter today's date without user input
    get the date today and format date to how it is in tasks.txt
    """
    today = datetime.today()
    date_today = today.strftime('%d %b %Y')

    task_due = input("\nWhen is the task due (please use following format 03 Mar 2022)?\n")
    print(f"\n{GREEN}Due date is:{RESET} {task_due}")

    # whenever new task added assume it it not completed
    completed = 'No'

    # opens the file for writing only, appends to the end
    task_file = open('tasks.txt', 'a', encoding='utf-8')

    # write new task on a new line in the correct sequence as the previous lines in text file
    task_file.write(f"\n{username}, {task_title}, {task_description}, {date_today}, {task_due}, {completed}")

    # confirmation of addition of new task
    print(f"\n{GREEN}The new task is added.{RESET}\n")

    # closes file after use
    task_file.close()

# function to view all the tasks
def view_all():
    # opens the tasks file for reading only
    task_file = open('tasks.txt', 'r', encoding='utf-8')

    # separate each line into a list
    tasks = task_file.readlines()

    # closes file after use
    task_file.close()

    """
    for every line in tasks list, enumerate each element postion starting from 1
    separate each element via comma and space into list called split_tasks
    display each task in an easy to read manner
    use list indexes to show just that element, [0] will just be the username
    """
    for pos, line in enumerate(tasks, 1):
        split_tasks = line.split(', ')

        output = f"\n{YELLOW}⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯[{RESET} {PURPLE}Task {pos}{RESET} {YELLOW}]⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯{RESET}\n"
        output += f"\nTask:\t\t\t{split_tasks[1]}\n"
        output += f"Assigned to:\t\t{split_tasks[0]}\n"
        output += f"Date assigned:\t\t{split_tasks[3]}\n"
        output += f"Due date:\t\t{split_tasks[4]}\n"
        output += f"Task complete?\t\t{split_tasks[5]}\n"
        output += f"Task description:\n{split_tasks[2]}\n"
        output += f"\n{YELLOW}⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯{RESET}\n"

        print(output)

# function view the tasks that are assigned to the login user and edit tasks
def view_mine():
    # open tasks file for reading
    task_read = open('tasks.txt', 'r', encoding='utf-8')

    # store each line in a list
    data = task_read.readlines()

    # close file after use
    task_read.close()

    # for every line in data list, enumerate each element postion starting from 1
    for pos, line in enumerate(data, 1):

        # list seperated for each element in a line
        split_tasks = line.split(', ')

        """
        index at 0 is the username
        if it matches the username used to log in
        it will only display the tasks corrosponding to that username
        """
        if split_tasks[0] == username_input:

            output = f"\n{YELLOW}⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯[{RESET} {PURPLE}Task {pos}{RESET} {YELLOW}]⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯{RESET}\n"
            output += f"\nTask:\t\t\t{split_tasks[1]}\n"
            output += f"Assigned to:\t\t{split_tasks[0]}\n"
            output += f"Date assigned:\t\t{split_tasks[3]}\n"
            output += f"Due date:\t\t{split_tasks[4]}\n"
            output += f"Task complete?\t\t{split_tasks[5]}\n"
            output += f"Task description:\n{split_tasks[2]}\n"
            output += f"\n{YELLOW}⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯{RESET}\n"

            print(output)

    # pick a task number, -1 at end is needed as tasks start at 1 not 0
    while True:
        task_choice = int(input("Please select a task number (-1 to go back to main menu): "))-1

        # if 0 or -2 and below picked give error
        if task_choice == -1 or task_choice <= -3:
            print(f"{RED}Invalid task number, please try again{RESET}.\n")
            continue

        # if choice more than total tasks in tasks.txt give error
        elif task_choice > len(data)-1:
            print(f"{RED}Invalid task number, please try again{RESET}.\n")
            continue
        
        # goes back to main menu
        elif task_choice == -2:
            break
        
        else:
            # place specific task line chosen into string variable
            edit_data = data[task_choice]

            # cast string into a list
            #split_data = edit_data.strip().split(', ')
            split_data = edit_data.split(', ')

            # If task is completed (Yes at end of line) deny any use of task editing
            if split_data[-1] == 'Yes\n':
                print(f"{RED}Can not edit a completed task. Please select an incomplete task.{RESET}\n")
                continue
            
            while True:
                output = f"\n{YELLOW}⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯[{RESET}{PURPLE}Select an option{RESET}{YELLOW}]⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯{RESET}\n"
                output += "1. Mark the task as complete\n"
                output += "2. Edit the task username\n"
                output += "3. Change the due date\n"
                output += "0. Choose another task\n"
                output += f"{YELLOW}⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯{RESET}\n"
                output += ": "
            
                option_choice = int(input(output))

                # changes task completed to Yes.
                if option_choice == 0:
                    break

                # changes task completed to Yes.
                if option_choice == 1:
                    split_data[-1] = "Yes\n"

                    new_data = ', '.join(split_data)
                    
                    data[task_choice] = new_data

                    print(f"{GREEN}Task has changed to completed{RESET}.\n")
                
                # changes the user task assigned to
                elif option_choice == 2:

                    # checks if username change is in list of registered users
                    while True:

                        username_change = input("\nWhich user would you change the task to: ").lower()

                        if username_change not in details_dict.keys():
                            print(f"{RED}Not registered username, please try again.{RESET}\n")
                            continue

                        else:
                            split_data[0] = username_change

                            new_data = ', '.join(split_data)
                            
                            data[task_choice] = new_data

                            print(f"{GREEN}Username has changed in the task.{RESET}\n.")
                            break
                
                # Change the due date.
                elif option_choice == 3:
                    new_due_date = input("Enter a new due date (in format 05 Jan 2023):\n")
                    
                    split_data[4] = new_due_date

                    new_data = ', '.join(split_data)
                    
                    data[task_choice] = new_data

                    print(f"{GREEN}The new due date is {new_due_date}.{RESET}\n")
                    
                # if wrong number option entered give error
                else:
                    print(f"{RED}Invalid option.{RESET}.\n")
                    
                # opens tasks.txt for writing and replaces with newly modified line (whether task complete, change in user assignment or due date)
                task_write = open('tasks.txt', 'w', encoding='utf-8')

                for line in data:
                    task_write.write(line)

                # close file after use
                task_write.close()
                break

# function to generate task_overview.txt
def task_overview():
    # open tasks.txt
    task_file = open('tasks.txt', 'r', encoding='utf-8')

    # store each line as an element in list variable
    contents = task_file.readlines()

    # close the file after use
    task_file.close()

    # variables that count after for loop
    completed_tasks = 0
    incompleted_tasks = 0
    overdue_incompleted_tasks_total = 0

    # for every line divide by comma + space
    for line in contents:
        split_tasks = line.strip().split(', ')

        # if last element is yes increase completed_tasks by 1
        if split_tasks[-1] == 'Yes':
            completed_tasks += 1

        # if last element is no increase incompleted_tasks by 1
        elif split_tasks[-1] == 'No':
            incompleted_tasks += 1

        # extract date from line
        due_date = split_tasks[-2]

        # extract the day, month, and year from the date
        day, month, year = due_date.strip().split()

        # convert the month to its numeric equivalent (Jan = 1)
        month = datetime.strptime(month, '%b').month

        # convert the day, month, and year into integers
        date = datetime(int(year), int(month), int(day))

        # get today's date
        today = datetime.today()

        # Check if the date is overdue (earlier than the current date) and if incomplete
        if date < today and split_tasks[-1] == 'No':
            overdue_incompleted_tasks_total += 1

    # calculate incomplete tasks for whole list
    percent_incomplete = round(((incompleted_tasks / len(contents)) * 100), 2)

    # calculate incomplete overdue tasks for whole list
    percent_overdue = round(((overdue_incompleted_tasks_total / len(contents)) * 100), 2)

    # write to a new file called task_overview.txt with each result on a new line
    task_overview = open('task_overview.txt', 'w', encoding='utf-8')

    task_overview.write(f"Total number of tasks: {len(contents)}.\n")
    task_overview.write(f"Total number of completed tasks: {completed_tasks}.\n")
    task_overview.write(f"Total number of incomplete tasks: {incompleted_tasks}.\n")
    task_overview.write(f"Number of incomplete tasks that are overdue: {overdue_incompleted_tasks_total}.\n")
    task_overview.write(f"Percentage of tasks that are incomplete: {percent_incomplete}%.\n")
    task_overview.write(f"Percentage of incomplete tasks that are overdue: {percent_overdue}%.\n")

    # close after use
    task_overview.close()

# function to generate user_overview.txt
def user_overview():
    # open tasks.txt
    task_file = open('tasks.txt', 'r', encoding='utf-8')

    # store each line as an element in list variable
    contents = task_file.readlines()

    # close the file after use
    task_file.close()

    # dictionaries of various task states
    user_number_tasks = {}
    completed_tasks_users = {}
    incompleted_tasks_users = {}
    overdue_tasks_users = {}

    # determines how many tasks and complete/incomplete tasks are assigned to each user
    for line in contents:
        split_tasks = line.strip().split(', ')

        ''' 
        tasks assigned to each user
        if user(key) exists in dictionary increase its value by one
        is user(key) does not exist, add to dictionary, username(key) and the value being 1
        '''
        if split_tasks[0] in user_number_tasks.keys():
            user_number_tasks[split_tasks[0]] += 1
        
        else:
            user_number_tasks.setdefault((split_tasks[0]), 1)

        '''
        completed tasks
        add user to completed_tasks_users dictionary the user(key) and value starting at 0
        if user has completed task increase value of that user(key) by one
        '''
        completed_tasks_users.setdefault((split_tasks[0]), 0)

        if split_tasks[-1] == 'Yes':
            completed_tasks_users[(split_tasks[0])] += 1

        '''
        incomplete tasks
        add user to incompleted_tasks_users dictionary the user(key) and value starting at 0
        if user has incomplete task increase value of that user(key) by one
        '''
        incompleted_tasks_users.setdefault((split_tasks[0]), 0)

        if split_tasks[-1] == 'No':
            incompleted_tasks_users[(split_tasks[0])] += 1

    # get today's date
    today = datetime.today()

    # determines if every task assigned to each user if incomplete and overdue
    for line in contents:
        split_tasks = line.strip().split(', ')
        
        # add to dictionary user(key) and start value at 0
        overdue_tasks_users.setdefault((split_tasks[0]), 0)

        # extract date from line
        due_date = split_tasks[-2]

        # extract the day, month, and year from the date
        day, month, year = due_date.strip().split()

        # convert the month to its numeric equivalent (Jan = 1)
        month = datetime.strptime(month, '%b').month

        # convert the day, month, and year into integers
        date = datetime(int(year), int(month), int(day))

        # when incomplete and overdue increase value by 1 corrosponding to that user(key)
        if split_tasks[-1] == 'No' and date < today:
            overdue_tasks_users[(split_tasks[0])] += 1
    
    # calculates the total number of users
    total_users = len(user_number_tasks.keys())
    
    # calculates the total number of tasks
    total_tasks = sum(user_number_tasks.values())

    # write to a new file called user_overview.txt with each result on a new line
    user_overview = open('user_overview.txt', 'w', encoding='utf-8')

    # start the report with the total number of users + tasks
    user_overview.write("User overview report:\n")
    user_overview.write(f"The total number of users registered: {total_users}\n")
    user_overview.write(f"The total number of tasks: {total_tasks}\n")

    '''
    for every user(key) in user_number_tasks dictionary
    access values for each user within each specific dictionary
    calculate the percentage values of each type of task progress to 2 decimal places
    '''
    for user, num_tasks in user_number_tasks.items():
        completed_tasks = completed_tasks_users[user]
        incompleted_tasks = incompleted_tasks_users[user]
        overdue_tasks = overdue_tasks_users[user]

        user_overview.write(f"\nStatistics for {user}:\n")
        user_overview.write(f"Total number of tasks: {num_tasks}\n")
        user_overview.write(f"Percentage of assigned tasks: {round((num_tasks / total_tasks * 100), 2)}%.\n")
        user_overview.write(f"Percentage of completed tasks assigned: {round((completed_tasks / num_tasks * 100) ,2)}%.\n")
        user_overview.write(f"Percentage of incomplete tasks assigned: {round((incompleted_tasks / num_tasks * 100), 2)}%.\n")
        user_overview.write(f"Percentage of incomplete and overdue tasks assigned: {round((overdue_tasks / num_tasks * 100), 2)}%.\n")

    # close after use
    user_overview.close()

# function to generate reports
def generate_report():

    # call the functions
    task_overview()
    user_overview()

    # confirmation that reports are generated
    print(f"{GREEN}Reports generated for task_overview.txt and user_overview.txt{RESET}")

#====Login Section====
# open text file to read only
details = open('user.txt', 'r', encoding='utf-8')

details_dict = {}

# populate details_dict with key as username as value as password and remove escape characters
for detail in details:
    key, value = detail.split(', ')
    details_dict[key] = value.strip('\n')

# checks if username is in details_dict keys
while True:
    username_input = input("Enter an username: ").lower()

    if username_input in details_dict.keys():
        print(f"{GREEN}{username_input} recognised.{RESET}\n")
    else:
        print(f"{RED}{username_input} does not exist! Please try again.{RESET}\n")
        continue

    correct_pass = details_dict[username_input]

    # when username is accepted, check if password(value) of corrosponding key in details_dict matches
    while True:
        password_input = input("Enter your password: ").lower()

        if correct_pass == password_input:
            print(f"{GREEN}Correct password.{RESET}\n")
            print(f"{GREEN}Welcome {username_input.capitalize()}!{RESET}")
            break

        else:
            print(f"{RED}Incorrect password, please try again.{RESET}\n")
            continue
    break

# close file after use
details.close()

#====Menu Section====
"""
presenting the menu to the user and 
making sure that the user input is converted to lower case.
"""
while True:
    
    # if admin logged in show menu with added statistics option
    if username_input == 'admin':
        menu = input("""
Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
gr - Generate reports
ds - Display statistics
e - Exit
: """).lower()
        
    # not admin logged in show a standard menu
    else:
        menu = input("""
Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
e - Exit
: """).lower()

    # registering a new user
    if menu == 'r':
        # call the function
        reg_user()
        continue

    # add a new task
    elif menu == 'a':
        # call the function
        add_task()
        continue

    # view all the tasks
    elif menu == 'va':
        # call the function
        view_all()
        continue

    # view the tasks that are assigned to the login user
    elif menu == 'vm':
        # call the function
        view_mine()
        continue

    # generate reports
    if menu == 'gr':
        # call the appropiate function
        generate_report()
        continue

    # statistics
    if menu == 'ds':
        # if admin logged in carry out statistics option
        if username_input == 'admin':

            # call function to generate reports
            generate_report()

            # list to store task_overview
            task_overview = []

            # store task_overview.txt in list with each element representing a line
            with open('task_overview.txt', 'r', encoding='utf-8') as f:
                for line in f:
                    task_overview.append(line)
            
            # list to store user_overview
            user_overview = []

            # store user_overview.txt in list with each element representing a line
            with open('user_overview.txt', 'r', encoding='utf-8') as f:
                for line in f:
                    user_overview.append(line)

            # present the two statistic reports clearly
                output = f"\n{YELLOW}⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯[{RESET} {PURPLE}Statistics{RESET} {YELLOW}]⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯{RESET}\n"
                output += f"\n{PURPLE}Task Overview{RESET}\n"
                output += f"{YELLOW}⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯{RESET}\n"
                output += "".join(map(str, task_overview))
                output += f"{YELLOW}⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯{RESET}\n"
                output += f"\n{PURPLE}User Overview{RESET}\n"
                output += f"{YELLOW}⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯{RESET}\n"
                output += "".join(map(str, user_overview))
                output += f"{YELLOW}⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯{RESET}\n"

                print(output)
        
        # if not admin give incorrect menu entry
        else:
            print(f"{RED}You have made a wrong choice, Please Try again{RESET}\n")
        continue

    # end program
    elif menu == 'e':
        print(f"{GREEN}Goodbye!!!{RESET}")
        exit()

    # incorrect menu entry
    else:
        print(f"{RED}You have made a wrong choice, Please try again.{RESET}\n")