import json
import csv

file_path_txt = "input.txt"
file_path_json = "input.json"
file_path_csv = "input.csv"

try:
    with open(file_path_txt, "r") as file:
        content = file.read()
        print(content)
    print()

    with open(file_path_json, "r") as file:
        content = json.load(file)
        print(content["name"])
    print()

    with open(file_path_csv, "r") as file:
        content = csv.reader(file)
        for line in content:
            print(line[0])

except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("No permission")
except:
    print("something went wront")
