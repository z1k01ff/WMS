import json

with open("test.json") as file:
    popovn = json.load(file)

result = ""

for item in popovn.items():
    new_item = str(item)[2:-1].replace("',", " ->")
    # print(new_item)
    result += f"{new_item}\n"
print(result)

text = "Welcome \n to Mate academy"
print(text)