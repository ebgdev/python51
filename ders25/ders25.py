import os
filename = os.path.dirname(__file__)
full_path = os.path.join(filename,"tl_usd_exchange_rate.csv")
full_output_path = os.path.join(filename,"output.txt")
output = open(full_output_path, "w")

with open(full_path,encoding='utf-8',buffering=1073741824) as f:
    for line in f:
        # print(line)
        saveLine = line.replace("TL:USD ,", "")
        output.write(saveLine)


output.close()
