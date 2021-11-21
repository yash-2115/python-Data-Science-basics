# JOSN module is used to read and write JSON files
import json

book = {}

book['tom'] = {
    'name': 'Tom',
    'age': '25',
    'address': '123 Main St',
    'phone': '555-555-5555'
}

book['jerry'] = {
    'name': 'Jerry',
    'age': '30',
    'address': '456 Main St',
    'phone': '555-555-5555'
}

# json., dumps() is used to convert python dictionary to JSON string
json_data = json.dumps(book)

# below line will write the JSON string to a file
with open('book.json', 'w') as f:
    f.write(json_data)