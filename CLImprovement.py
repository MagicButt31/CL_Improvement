import sys
import json
import os

def main():
    write_file("tasks.json", "a", "")
    clearterminal()
    print("Welcome to CLImprovement!")
    while True:
        try:
            tools_inp = input("What do you want to open ('/help' for commands)? ")
            if tools_inp.find("/") == 0:
                a = general_commands(tools_inp)
                if a == "break":
                    break
                elif a == "apps":
                    print("Apps:\ntasks: task tracker")
            else:
                if app_access(tools_inp) == "task":
                    task()
        except KeyboardInterrupt:
            print("\nnuh-uh, you have to use /quit because I say so.")

def app_access(inp):
    if inp.lower() == "task" or inp.lower() == "tasks":
        return "task"
    else:
        print("app doesn't exist")

def general_commands(inp):
    clearterminal()
    if inp == "/quit":
        sys.exit()
    elif inp == "/exit":
        return "break"
    elif inp == "/help":
        print("""Commands:
/quit: quits the whole program
/exit: exits application (quits program if on main screen)
/apps: shows apps that are available (or what an app can do)""")
        return "more commands"
    elif inp == "/apps":
        return "apps"
    else:
        print("Command doesn't exist.")

def read_file(file_name : str):
    with open(file_name, "r", encoding="utf-8") as file:
        return file.read()

def write_file(file_name: str, w_a, what_to_write):
    with open(file_name, w_a, encoding="utf-8") as file:
        file.write(what_to_write)

def clearterminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def date_converter(date):
    month_list = ["January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"]

    if date == "":
        return ""
    else:
        date = date.replace("/", " ")
        date = date.replace(".", " ")
        date = date.replace("-", " ")
        date = date.replace(",", "")
        month, day, year = date.split(" ")
        try:
            month = month_list.index(month)
            month = month + 1
        except ValueError:
            pass

        return f"{year}-{month:02}-{day:02}"

def task():
    clearterminal()
    task_list = read_file("tasks.json")
    print("Entered Tasks...")
    #add actual task saving
    while True:
        task_list = read_file("tasks.json")
        if task_list == "":
            task_list = []
        else:
            task_list = [item for item in json.loads(task_list)]
        if task_list == []:
            print("you have no tasks")
        else:
            for x in task_list:
                print(f"[{x['complete']}] {x['name']} (@{x['due_date']})")
        task_inp = input("Tasks: What do you want to do? ")
        if task_inp.find("/") == 0:
            clearterminal()
            a = general_commands(task_inp)
            if a == "break":
                break
            elif task_inp == "/help":
                a
                print("/cancel: cancels process of app")
            elif a == "apps":
                print("""Functions of tasks:
add tasks: literally just adds tasks to save
view tasks (decomissioned): view tasks that have been made
clear all tasks: removes every single task made
clear one task: clears one task at a time
complete task: completes tasks""")
        else:
            if task_inp == "add tasks" or task_inp == "add task":
                clearterminal()
                if task_list == []:
                    print("you have no tasks")
                else:
                    for x in task_list:
                        print(f"[{x['complete']}] {x['name']} (@{x['due_date']})")
                while True:
                    task_name = input("What task do you want to add (put in '/finish' to finish)? ")
                    try:
                        if task_name.find("/") == 0:
                            if task_name == "/finish":
                                clearterminal()
                                print("task(s) has been added")
                                write_file("tasks.json", "w", json.dumps(task_list, indent=4))
                                break
                            elif task_remove == "/cancel":
                                print("cancelling")
                                break
                            elif task_name == "/help":
                                print("I cannot help you right now.")
                            else:
                                print("command doesn't exist")
                        else:
                            due_date = input("when is your task due (format mm/dd/yyyy, and words are fine  )? ")
                            due_date = date_converter(due_date)
                            task_finalized = {'name': task_name, 'due_date': due_date, 'complete': ''}
                            task_list.append(task_finalized)
                    except UnboundLocalError or TypeError:
                        print("command doesn't exist")
            elif task_inp == "view tasks" or task_inp == "view tasks":
                clearterminal()
                print("command has been decomissioned")
            elif task_inp == "clear all task" or task_inp == "clear all tasks":
                clearterminal()
                write_file("tasks.json", "w", "")
                task_list = []
                print("tasks cleared")
            elif task_inp == "clear one task" or task_inp == "clear one tasks":
                clearterminal()
                if task_list == []:
                    pass
                else:
                    for x in task_list:
                        print(f"[{x['complete']}] {x['name']} (@{x['due_date']})")
                    while True:
                        task_remove = input("What task do you want to remove ('/finish' to finish)? ")
                        if task_remove.find("/") == 0:
                            if task_remove == "/finish":
                                print("task(s) has been removed")
                                write_file("tasks.json", "w", json.dumps(task_list, indent=4))
                                break
                            elif task_remove == "/cancel":
                                print("cancelling")
                                break
                            elif task_remove == "/help":
                                print("I cannot help you right now.")
                            else:
                                print("command doesn't exist")
                        else:
                            for x in task_list:
                                if x['name'] == task_remove:
                                    task_list.remove(x)
            elif task_inp == "complete task" or task_inp == "complete tasks":
                clearterminal()
                if task_list == []:
                    pass
                else:
                    for x in task_list:
                        print(f"[{x['complete']}] {x['name']} (@{x['due_date']})")
                    while True:
                        task_complete = input("What task do you want to complete ('/finish' to finish)? ")
                        if task_complete.find("/") == 0:
                            if task_complete == "/finish":
                                clearterminal()
                                print("task(s) has been complete")
                                write_file("tasks.json", "w", json.dumps(task_list, indent=4))
                                break
                            elif task_complete == "/cancel":
                                print("cancelling")
                                break
                            else:
                                print("command doesn't exist")
                        else:
                            for x in task_list:
                                if x['name'] == task_complete:
                                    x['complete'] = 'x'
            else:
                clearterminal()
                print("that does not exist")
            
main()
