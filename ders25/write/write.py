# | Mode   | Read | Write | Truncate | Create | Cursor Position | File Must Exist     |
# | ------ | ---- | ----- | -------- | ------ | --------------- | ------------------- |
# | `'r'`  | ✅    | ❌     | ❌        | ❌      | Start           | ✅                   |
# | `'r+'` | ✅    | ✅     | ❌        | ❌      | Start           | ✅                   |
# | `'w'`  | ❌    | ✅     | ✅        | ✅      | Start           | ❌                   |
# | `'w+'` | ✅    | ✅     | ✅        | ✅      | Start           | ❌                   |
# | `'a'`  | ❌    | ✅     | ❌        | ✅      | End             | ❌                   |
# | `'a+'` | ✅    | ✅     | ❌        | ✅      | End             | ❌                   |
# | `'x'`  | ❌    | ✅     | ❌        | ✅      | Start           | ❌ (error if exists) |
# | `'x+'` | ✅    | ✅     | ❌        | ✅      | Start           | ❌ (error if exists) |



import os
file_name = "names.txt"
script_dir = os.path.dirname(__file__)  # The directory of the script
full_path = os.path.join(script_dir,file_name)

names = ["name1","name2","name3","name4","name5"]

with open(full_path,"w") as f:
    for name in names:
        f.write(f"{name}\n")


