import json

Data = {
    "Name" : "Alex",
    "Age" : 28,
    "Hobbies" : ["Reading", "Hiking", "Coding"]
}
with open('output.json', 'w') as f:
    json.dump(Data, f, indent=4)