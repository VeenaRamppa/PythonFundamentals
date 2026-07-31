import json

# reading data from json
# file = open("friends_json.txt","r")
with open("friends_json.txt","r") as file:
    file_content = json.load(file)

#file.close()
print(file_content)

# writing data into json format

cars = [
    {"make":"Ford","model":"Fiesta"},
    {"make":"Ford","model":"Focus"}
]

file = open("cars_json.txt","w")
json.dump(cars, file)
file.close()
