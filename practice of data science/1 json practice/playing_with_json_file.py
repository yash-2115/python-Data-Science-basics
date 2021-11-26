import json

f = open(r"E:\Data Science\practice of data science\json practice\details.json", "r")
data = f.read()

# print(data)

# converting the python dict in json
json_data = json.loads(data)


for j_data in json_data:
    print(j_data)
    print(json_data[j_data])