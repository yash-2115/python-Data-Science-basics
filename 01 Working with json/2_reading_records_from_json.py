import json

f = open("01 Working with json\\book.json", "r")
s = f.read()

# This will print data that we got from json file and this will be in a foom of 
# print(s)

# json.loads will convert json string into python dictionary
book = json.loads(s)
print(book)
print(type(book))

# Lets fatch some data from the dict now
print(book['jerry'])
print(book['jerry']['age'])

for person in book:
    print(book[person])