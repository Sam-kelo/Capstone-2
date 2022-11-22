from datetime import datetime

from datetime import date

import datetime

# The reg_user function allows the user assigned as admin
# to register a user.
# If the user is "admin". The admin menu will automatically appear.
def reg_user():
        
    if username != "admin" and password != "adm1n" :
        
# If the user chooses "r" and they're not "admin", then an appropriate message
# will be displayed.        
        print ("Authorisation needed to register a new user.")

    else:

        if username == "admin" and password == "adm1n":

            if username == "admin":

                user_reg = False
                    
                new_username = input("Enter a username: ")
                        
                if new_username == username:

                    print("Username already exists, please try again.")

                    main_menu()
                        
                elif new_username != username:

                    new_password = input("Enter a password: ")

                    password_confirmation = input("Please confirm your password: ")

                    if new_password == password_confirmation:

                        user_reg = True
                
                        if new_password != password_confirmation:

                            print("Your password did not match. Please try again")
    
                        elif new_password == password_confirmation:

                            print("New user created")

                            user_reg = open("user.txt", "a")

                            user_reg.write("\n" + str(new_username) + ", " + str(new_password))

                            user_reg.close()
                                    
# Should the user want to add a task, they will  be able to do so by selecting "a".                            
def add_task():

    task_file =  open("tasks.txt", "a")

    assign = str(input("Enter the username of whom the task is for:"))
            
    title = str(input("Enter the title of the task:"))

    description = str(input("Enter a description of the task:"))
    
    due_date = str(input("Enter the due date of the task. dd mm yyyy. eg(15 Jun 2019): "))

    date_assigned = str(input("Enter the date in which the task was assigned. dd mm yyyy eg(20 Dec 2019): "))

    completion = "No"

    print("Your task has been added.")
# After the user input has been given, it is then written to the tasks textfile.
    task_file.write("\n" + str(assign) + ", " + str(title) + ", " + str(description) + ", " +

    str(due_date) + ", " + str(date_assigned) + ", " + str(completion))

    task_file.close()

# If the user selects va, all tasks will be displayed in a particular 
# format using a for loop.    
def view_all():
            
    task_viewer = open("tasks.txt", "r")
        
    for line in task_viewer:

        assign, title, description, due_date, date_assigned, completion = line.split(", ")

        print(f'''

                    Assigned to:     {assign}

                    Task:            {title}

                    Description:     {description}

                    Due Date:        {due_date}

                    Date Assigned:   {date_assigned}

                    Task Complete:   {completion}

                    ''')

    task_viewer.close()
  
# If the user selects vm, the users specifc tasks will be displayed in a 
# particular format.
def view_mine():

    string_list = []

    task_num = 0
                    
    with open("tasks.txt", "r+") as my_view:

        view_mine = my_view.readlines()

        for line in view_mine:
            
            line = line.split(", ")

    task_num += 1

    if username == line[0]:

            print(f"""

                Task number:     {task_num}

                Assigned to:     {line[0]}

                Task:            {line[1]}
    
                Description:     {line[2]}

                Due Date:        {line[3]}

                Date Assigned:   {line[4]}

                Task Complete:   {line[5]}

                """)
                
# While the users tasks are being displayed, they have the option to edit
# or return to the menu.
# A conditional statement is now used to determine what
# the program does after the user selects 1 or -1.                

    task_edit = int(input("Would you like to edit a task (1) or Return to menu (-1): "))

    if task_edit == 1:

        task_num = int(input("Please enter a Task number: "))
            
        task_num = task_num - 1

        with open("tasks.txt", "r") as file:

            tasks = file.readlines()

            users_task = tasks[task_num].strip().split(", ")

            choice = input("Would you like to mark the task as complete(m) or edit the task(e)?").lower()

            if choice == "m":

                users_task[-1] = "Yes"

                tasks[task_num] = ", ".join(users_task) + "\n"

                task_str = "".join(tasks) + "\n"

                print("Marked as complete.")

                with open("tasks.txt", "w") as f:

                    f.write(str(task_str))

            elif choice == "e" and line[5] == "No":           

                edits = input("Change assignee (a) or Change due date (b)").lower()

                if edits == "a":

                    new_assign = input("Please enter new assignee: ")

                    users_task [0] = line[0].replace(line[0], new_assign)

                    tasks[task_num] = ", ".join(users_task) + "\n"

                    task_str = "".join(tasks) + "\n"

                    print("Assignee changed.")
 
                    with open("tasks.txt", "w") as file:

                        file.write(task_str)             

                elif edits == "b":

                    due_date_change = input("Please enter a new due date. dd-mm-yyyy: ")

                    users_task [-2] = "" + line[3].replace(line[3], due_date_change)

                    tasks[task_num] = ", ".join(users_task) + "\n"

                    task_str = "".join(tasks) + "\n"

                    print("Due date changed.")

                    with open("tasks.txt", "w") as file:

                        file.write(task_str + "\n")
                                
            else:  

                print("Task is complete and cannot be edited.")

    elif task_edit == -1:

        print(menu)
                        
task_list = []

user_list= []

users_tasks = []

# If the user selects "gr", the task overview and user overview
# files will be created.
def generate_reports():
    
# Opening the tasks.txt file in order to create a list of tasks.        
    with open("tasks.txt", "r") as task_file:

        task_f = task_file.readlines()
                          
        for line in task_f:

            line = line.split(", ")

            task = line[2]

            task_list.append(task)
            
# Opening the user.txt file in order to create a list of users.            
    with open("user.txt", "r") as user_file:

        user_f = user_file.readlines()

        for line in user_f:

            lines = line.split(", ")

            user = line[0]

            user_list.append(user)                    

# The task_overview function generates the task_overview.txt file.
def task_overview():

    completed_tasks = 0

    incomplete_tasks = 0
    
    overdue_tasks = 0

# Opening tasks.txt to get complete and incomplete tasks.
    with open("tasks.txt", "r") as completed_file:

        for line in completed_file:

            line = line.split(", ")

            completion = line[5]
                
            if completion == "No":
                
                incomplete_tasks += 1
                
            elif completion == "Yes":
                
                complete_tasks += 1
                
# Using the datetime module to check if tasks are overdue.
# starts by getting todays date.
    with open("tasks.txt", "r") as overdue_file:

        overdue = overdue_file.readlines()

        for line in overdue:

            line = line.split(", ")

            completion = line[5]

            due_date_datetime = datetime.datetime.strptime(line[4], "%d %b %Y")

            today = datetime.datetime.now()

            if today > due_date_datetime and completion == "No":  
            
# "%d %b %Y" creates the time format .                 
                overdue_tasks += 1

        incomplete_percentage = (int(incomplete_tasks) /len(task_list)) * 100

        overdue_percentage = (int(overdue_tasks)/len(task_list)) * 100

# Writing elements to the file.

    with open("task_overview.txt", "w") as task_overview_file:
        
        task_overview_file.write(f"Total number of tasks that have been generated using task manager: {len(task_list)}\n")

        task_overview_file.write(f"Total number of completed tasks: {completed_tasks}\n")

        task_overview_file.write(f"Total number of incomplete tasks: {incomplete_tasks}\n")

        task_overview_file.write(f"Total number of tasks incomplete and overdue: {overdue_tasks}\n")

        task_overview_file.write(f"Percentage of tasks that are incomplete: {incomplete_percentage}\n")

        task_overview_file.write(f"Percentage of tasks that are overdue: {overdue_percentage}\n")
                
# The user_overview function generates the user_overview.txt file.
def user_overview():

    completed_tasks = 0

    incomplete_tasks = 0

    total_tasks = task_list

    total_users = user_list
            
    user_overdue_tasks = 0 

# Opening the tasks.txt to get a specifc users  tasks.
    with open("tasks.txt", "r") as user_view:

        global username

        user_v = user_view.readlines()

        for line in user_v:
            
            line = line.split(", ")

            username_ = line[0]

            user_task = line[2]

            if username == username_:  

                users_tasks.append(user_task)
                    
# Opening the tasks.txt to get a specifc users complete and incomplete tasks.
        
    with open("tasks.txt", "r") as user_completion:
         
        user_complete = user_completion.readlines()

        for line in user_complete:

            line = line.split(", ")

            completion = line[5]

            user = line[0]

            if username == user:
        
                if completion == "Yes":
                
                    completed_tasks += 1
                
                elif completion == "No":
                
                    incomplete_tasks += 1
                    
# Opening tasks.txt to get user overdue tasks.
# 'strptime()' parses a string representing a time according to a format.
# 'today()' method of date class under datetime module returns a current date.
    with open("tasks.txt", "r") as overview:

        overview_ = overview.readlines()
            
        for line in overview:
                    
            line = line.split(", ")

            completion = line[5]

            user = line[0]

            if username == user:
                
                due_date_datetime = datetime.datetime.strptime(line[4], "%d %b %Y")

                today = datetime.datetime.now()
                
                if today > due_date_datetime and completion == "No":  
                
                    user_overdue_tasks += 1
                    
# Calculations for task percentages.
        percentage_assigned = (len(task_list) / len(users_tasks)) * 100

        percentage_incomplete = (int(incomplete_tasks) / len(users_tasks)) * 100

        overdue_percentage = (int(user_overdue_tasks)/ len(users_tasks)) * 100

        percentage_completed = (int(completed_tasks)/ len(users_tasks)) * 100

    with open("user_overview.txt", "w") as user_overview_file:        
                    
# Writing elements to the file.
        user_overview_file.write(f"Total number of tasks that have been assigned to the user: {len(users_tasks)}\n")

        user_overview_file.write(f"Percentage of tasks assigned to the user: {percentage_assigned}\n")

        user_overview_file.write(f"Percentage of tasks completed: {percentage_completed}\n")

        user_overview_file.write(f"Percentage of tasks that need to be completed: {percentage_incomplete}\n")

        user_overview_file.write(f"Percentage of tasks that are incomplete: {percentage_incomplete}\n")

        user_overview_file.write(f"Percentage of tasks that are overdue: {overdue_percentage}\n")

        print("Documents generated.")

# If the user chooses s, this will display statistics such as
# the total amount of tasks and the total amount of users.
def statistics():

    global username
            
    if username != "admin" and password != "adm1n":
        
        print ("Authorisation needed to view statistics.")

    else: 

        if username == "admin" and password == "adm1n":

            if username == "admin":

                x = 0
                     
                y = 0

                with open("tasks.txt", "r") as task_file:
                            
                    for line in task_file:

                        x += 1
                    
                print (f"\nThe total number of tasks is: {x}")

                with open("user.txt", "r") as username:
                
                    for line in username:

                        y += 1
                        
                    print (f"The total number of users is: {y}")

# The task overview and user overview files may be opened for the admin
# statistics option.                            
    with open("task_overview.txt", "r") as overview_task:

        overview_task.readlines()

        for lines in overview_task:

            print(lines)

    with open("user_overview.txt", "r") as overview_user:

        overview_user.readlines()

        for lines in overview_user:

            print(lines)
             
# The program starts by opening the user text file which contains the user details.
user_file = open("user.txt", "r+")

text = user_file.readlines()

login = False

# Login starts off as false until the correct logins are entered.
while login == False:

    username = input("Enter your username: ")

    password = input("Enter your password: ")

    for lines in text:
        
# The data contained within the user text file is then split into a
# list of smaller pieces.
        user, passwrd = map(str.strip,lines.split(", "))

        if username == user and passwrd == password:

            login = True

            print("Welcome!")
        
        else:

            if user != user and passwrd != password:

                print("Invalid login details, please try again.")
                                 
user_file.close()
# Once the user is logged in, the following menu is displayed.
while True:

    menu = input("""Select one of the following options below:
                    
                    r  - Registering a user
                    a  - Adding a task
                    va - View all tasks
                    vm - view my task
                    gr - Generate reports
                    s  - Statistics
                    e  - Exit
                    
                    :""").lower()

    if menu == "r":

        reg_user()
           
    elif menu == "a":

        add_task()       

    elif menu == "va":

        view_all()
            
    elif menu == "vm":

        view_mine()
            
    elif menu == "gr":

        generate_reports()

        task_overview()

        user_overview()

    elif menu == "s":
            
        statistics()

    elif menu == "e":
        print("Goodbye!!!")
        exit()

    else:
        print("You have made a wrong choice, Please Try again")

   
