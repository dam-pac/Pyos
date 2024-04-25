import os
def delete_file(file_name):
    try:
        os.remove(f"{os.path.abspath(file_name)}")
        return 0
    except FileNotFoundError:
        return 1
    except:
        return 2
def cwd():
    try:
        return os.getcwd()
    except:
        return 1
def cd(path):
    try:
        os.chdir(path)
        return 0
    except FileNotFoundError:
        return 1
    except:
        return 2
def dir(path="."):
    try:
        return os.listdir(path)
    except FileNotFoundError:
        return 1
    except:
        return 2