import json
tr = {
    "0": "Молодший бухгалтер",
    "1": "Головний бухгалтер",
    "2": "Заступник головного бухгалтера (ст. м. Либідська)",
    "3": "Бухгалтер",
    "4": "Accountant (trucking company)",
    "5": "Бухгалтер (автомобильный бизнес), финансовый менеджер",
    "6": "Головний бухгалтер",
    "7": "Провідний бухгалтер",
    "8": "Помічник бухгалтера",
    "9": "Accounts Receivable Accountant with knowledge of Serbian",
    "10": "Бухгалтер",
    "11": "Бухгалтер із заробітної плати, кадровик",
    "12": "Бухгалтер-касир",
    "13": "Бухгалтер",
    "15": "Сподобалися результати пошуку?",
    "21": "Середня зарплата бухгалтера в Україні",
    "22": "Ці вакансії за містами"
}

result2 = {}
for item in tr.values():
    result2.update({item: 0})
print(result2)

result = result2

for key, value in tr.items():
    result.update({value: result[value] + 1})
print(result)

with open("test.json", "w") as file:
    json.dump(result, file, indent=4, ensure_ascii=False)
