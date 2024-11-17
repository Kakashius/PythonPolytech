# TODO решите задачу
import json

def task() -> float:
    filename = "input.json"
    with open(filename, "r") as output:
        data = json.load(output)
    result = 0
    for i in data:
        result += i["score"] * i["weight"]
    return round(result, 3)
print(task())
