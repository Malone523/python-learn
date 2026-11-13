import json
import csv

employees = [["Name", "Age", "Job"], 
             ["Sponge", 20, "Cook"], 
             ["Bob", 26, "Unemployed"]]


txt_data = "Yep"

file_path = "output.csv"

try:
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)
        print(f"json file '{file_path} created")

except FileExistsError:
    print("file exists")