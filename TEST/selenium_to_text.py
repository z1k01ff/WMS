import selenium
import json


def selenium_to_json(selenium_file, name):
    json_result = {}
    text_result = []
    for item in selenium_file:
        item = item.text
        text_result.append(item)

    for item_text in text_result:
        if item_text not in json_result:
            json_result.update({item_text: text_result.count(item_text)})
    print(json_result)

    with open(f"../TEST/{name}.json", "w") as file:
        json.dump(json_result, file, indent=4, ensure_ascii=False)


def json_to_text(name):
    with open(f"{name}.json") as file:
        json_file = json.load(file)

    text_result = ""
    for item in json_file.items():
        new_item = str(item)[2:-1].replace("',", " ->")
        text_result += f"{new_item}\n"
    return text_result

if __name__ == "__main__":
    selenium_file = ["qq", "ee", "rr", "qq", "ee", "ee", "ee", "ee"]
    print(json_to_text("test"))
