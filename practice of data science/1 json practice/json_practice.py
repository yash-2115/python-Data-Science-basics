# Importing json modile
import json

data = {}

data["Yash Patel"] = {
    'age': 21,
    'Address': 'Gujarat',
    'Gender': "Male"
}

data["Rhythm Mendawala"] = {
    'age':21,
    'Address': 'Gujarat',
    'Gender': 'Female'
}

print(data)

# printing in a form of json
print(json.dumps(data))

# createing json from python dictionary
with open('details.json', 'w') as f:
    f.write(json.dumps(data))