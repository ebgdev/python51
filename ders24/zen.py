# def fetch_lines(file_name):
#     with open(file_name, 'r') as file:
#         for line in file:
#             yield line.strip()


# zen = fetch_lines("zen.txt")
# print(next(zen))  # Prints the first line of the zen.txt file


# ---------------------

import os

# getcwd stands for get current working directory
print(os)
print("getcwd: ", os.getcwd())
script_dir = os.path.dirname(__file__)
print("script_dir: ", script_dir)
zen_txt_path = os.path.abspath("zen.txt")
full_path = os.path.join(script_dir, "zen.txt")
print("zen.txt abs path: ", zen_txt_path)
print("existance: ", os.path.exists(script_dir))
print("is direcory1: ", os.path.isdir(script_dir))
print("is file: ", os.path.isfile(full_path))
print("listing directories: ", os.listdir())


# -----------------

# Let's say your file structure is:
# /project
#    my_script.py
#    zen.txt

# 1
# cd /project
# python my_script.py

# Both abspath("zen.txt") and dirname(__file__) + "zen.txt" work.

# 2
# Now run from another location:
# cd ~
# python /project/my_script.py

# abspath("zen.txt") → ~/zen.txt (❌ WRONG — file not found)

# os.path.join(dirname(__file__), "zen.txt") → /project/zen.txt (✅ correct)





# ---------------------

# import os

# def fetch_lines(file_name):
#     script_dir = os.path.dirname(__file__)  # The directory of the script
#     full_path = os.path.join(script_dir, file_name)
#     print(script_dir)
#     print(full_path)
#     with open(full_path, 'r') as file:
#         for line in file:
#             yield line.strip()

# zen = fetch_lines("zen.txt")
# print(next(zen))



