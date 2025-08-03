# txt_data = "HI, I am MD. Parvaj Mosharof"

# file_path = "C:/Users/parvajio/Desktop/output.txt"

# try:
#     with open(file_path, "a") as file: #"w" for write, "x" for not existing file, "a" for add content repeatedly in the file
#         file.write("\n"+txt_data)
#         print(f"txt file '{file_path}' was created.")
# except FileExistsError:
#     print("file already exists.")

# fruites = ["apple", "mango", "pineapple"]

# file_path = "output.txt"

# with open(file_path, "w") as file:
#     for fruit in fruites:
#         file.write(fruit + "\n")
#     print("created file")

# import json

# employee = {
#     "name" : "Md. Parvaj Mosharof",
#     "age" : 21,
#     "email" : "parvajio25@gmail.com"
# }

# json_path = "outputJson.json"

# with open(json_path, "w") as file:
#     json.dump(employee, file, indent=4)
#     print("json file creted")

import csv

employees = [
    ["Name", "age", "job"],
    ["Parvaj", 30, "Developer"],
    ["rajon", 69, "hacker"],
    ["nahid", 27, "jni na"]
]

csv_file = "output.csv"

with open(csv_file, "w", newline="") as file:
    writer = csv.writer(file)
    for row in employees:
        writer.writerow(row)