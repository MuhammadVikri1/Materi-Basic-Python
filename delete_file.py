import os
file_path = "hello.txt"

if os.path.exists(file_path):
    os.remove(file_path)
    print("File {} has been deleted" . format(file_path))
else:
    print("File doesnt exist")