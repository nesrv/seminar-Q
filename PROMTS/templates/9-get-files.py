# function list all files in the current folder

def list_files():
    import os
    files = os.listdir()
    for file in files:
        print(file)



list_files()

# function list all files in the current folder with extension .txt

def list_txt_files():
    import os
    files = os.listdir()
    for file in files:
        if file.endswith('.txt'):
            print(file)


assert callable(list_txt_files)
list_txt_files()
