# создай программу для чтение текстовых файлов
# (см. урок по файлам)
# create a program to read text files
# (see the lesson on files)

def read_file(file_path):
    """
    Reads the contents of a text file and returns it as a string.
    """
    with open(file_path, 'r') as file:
        contents = file.read()
    return contents

