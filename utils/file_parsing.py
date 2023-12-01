def open_and_read_file(path):
    with open(path, "r") as file:
        return file.readlines()