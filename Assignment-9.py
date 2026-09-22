import csv
import json

# Read data from CSV file
with open("input.csv", "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    data = list(csv_reader)

# Write data to JSON file
with open("output.json", "w") as json_file:
    json.dump(data, json_file, indent=4)

print("CSV data successfully converted to JSON!")