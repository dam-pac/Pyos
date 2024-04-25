from colorama import *
from OS import *
print(Fore.YELLOW, Back.CYAN, " "*10000)
clear()
print("Welcome to the PYOS system! == Login program start automatically ==")
login()
while True:
    clear()
    print(f"""    -----> Time: {time_cur()} \n
    ============================== \n
    ||  COMMAND PROMPT PROGRAM  || \n
    ============================== \n
    """)
    print("For the list of commands, type => 'cmds' or 'lc' \n For the help information, type => 'help' or '?'")
    command = input(f"\n\n    {prompt}")
    if command == "":
        pass
    elif command == "TEST":
        break




input()