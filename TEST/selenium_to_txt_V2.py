import json
import time


def selenium_to_text(selenium_file, name):
    json_result = {}
    list_txt_result = []
    for item in selenium_file:
        item = item.text
        list_txt_result.append(item)

    for item_text in list_txt_result:
        if item_text not in json_result:
            json_result.update({item_text: list_txt_result.count(item_text)})
    # print(json_result)

    text_result = ""

    for item in json_result.items():
        new_item = str(item)[2:-1].replace("',", " ->")
        text_result += f"{new_item}\n"

    test = f"Дата оновлення: {time.strftime('%X')}\n\n" + text_result

    with open(f"../TEST/{name}.json", "w") as file:
        json.dump(test, file, indent=4, ensure_ascii=False)
    return text_result


if __name__ == "__main__":
    pass
