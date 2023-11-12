import json

FILENAME = 'input.json'


def task() -> float:
    with open(FILENAME) as f:
        json_data = json.load(f)

    return round(sum(element["score"] * element["weight"] for element in json_data), 3)


print(task())
