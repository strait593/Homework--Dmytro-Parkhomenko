from colorama import Fore, Back, Style
import pathlib
import os

def display_dirs(path, indent = ""):
    if not os.path.exists(path):
        return f"{path} directory does not exist"
    
    try:
        items = os.listdir(path)

    except PermissionError as e:
        print(e)

    for item in items:
        full_path = os.path.join(path, item)

        if os.path.isdir(full_path):
            print(f"{indent}{Fore.BLUE}{Style.BRIGHT}{item}")

            display_dirs(full_path, indent + "  ")

        else:
            print(f"{indent}{Fore.GREEN}{item}")
path = "C:\Users\dparh\Desktop\Data_Science\module4\additional_task\main.py"
        
if __name__ == '__main__':
    display_dirs(path)