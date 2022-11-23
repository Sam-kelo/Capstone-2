# Task Manager

### Purpose

Task manager is a Python program that helps businesses keep track and manage tasks assigned to each member of a team.

### Function

Task Manager gathers information from textfiles called:

* users.txt which contains username and password information. 

* tasks.txt which contains information on the name of the task, type of tasks, date assigned, due date and whether it has been completed or not.

Initially, users have to sign in using their assigned username and password. 

The following menu is displayed:

* Register user

* Add task

* View all tasks

* View my tasks

* Generate reports

* Display statistics

Once a user logs in, certain menu options are accessable depending on the type of user.
The admin user is the only one with access to register new users, view statistics and generate reports that create two text files namely,
task_overview.txt and user_overview.txt.

* task_overview displays the total number of tasks(complete and incomplete,) and tasks that are overdue.

* user_overview displays total users registered in Task Manager, total tasks assigned to each user, percentage assigned to user that are complete and incomplete.

This management system allows users to track and log detailed information off all tasks in a structured detailed manner.
