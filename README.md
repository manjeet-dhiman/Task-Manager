# Task Manager

A Python program that manages tasks and the users assigned to each task.

## Description

This program is for for a small business that allows it to track, edit and report on tasks assigned to each member of the team.

Once logged in, a menu is presented to the 'admin' while a limited menu is presented to any other 'user'.

From the user menu, all users are able to:

* Add a new task given the input of the assigned user, task title, task description, due date, completion status and date assigned.
* View all tasks in the database.
* View tasks assigned to them and then either:
    * Mark the task as complete or,
    * Change who the task is assigned to or the due date of the task.

From the admin menu, an admin has extended permissions to:

* Register and validate a new user given the input of a username and password.
* Generate a user and task report.
* Display user and task statistics.

Each menu option calls the corresponding function for action. Any time a task or user is edited the details are updated in the following txt files.

The program works with two input files:

* A user.txt file that stores the username and password of each team member, per line.
* A tasks.txt file that stores a list of all the tasks that the team is working on, per line, which includes:
  * The username of the person to whom the task is assigned.
  * The title of the task.
  * A description of the task.
  * The date that the task was assigned to the user.
  * The due date for the task.
  * Either a ‘Yes’ or ‘No’ value specifying if the task has been completed.

The program generates two output files:

* A user_overview.txt file that displays a report of the team members statistics, per line, which includes:
  * Total number of registered users.
  * Total number of tasks that have been generated and tracked.
  * Total tasks assigned per user.
  * Percentage of total tasks assigned per user.
  * Percentage of completed tasks assigned per user.
  * Percentage of incompleted tasks assigned per user.
  * Percentage of incompleted and overdue tasks assigned per user.
* A tasks_overview.txt file that displays a report of the tasks statistics, per line, which includes:
  * Total number of tasks that have been generated and tracked.
  * Total number of completed tasks.
  * Total number of incomplete tasks.
  * Total number of incomplete and overdue task.
  * Percentage of incomplete tasks.
  * Percentage of overdue tasks.

## Functionality summary:

* User login
* Register a new user
* Add a new task
* View all tasks
* View and edit a users tasks
* Generate user and task reports
* View user and task statistics

## Programming principles

This program employs the programming concepts of conditional logic, external databases, lists, dictionaries, loops, functions and string handling. Furthermore it employs fundamental programming functions that include enumerate, .items(), indexing and date formating.

## Dependencies

from datetime import datetime

## Running the program

Run the task_manager.py file in any Python IDE.
View the tasks.txt, user.txt, tasks_overview.txt and user_overview.txt files in any text editing program, such as Notepad++.

## Code preview

```python
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
```

## Program preview

```
Enter an username: admin
admin recognised.

Enter your password: adm1n
Correct password.

Welcome Admin!

Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
gr - Generate reports
ds - Display statistics
e - Exit
: 
```

## Author

Manjeet Dhiman
