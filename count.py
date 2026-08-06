import json

data = 12345
count = 0

for i in str(data):
    count = count + 1

result = {
    "data": data,
    "count": count
}

with open("output.json", "w") as file:
    json.dump(result, file, indent=4)

print("JSON file created successfully!")