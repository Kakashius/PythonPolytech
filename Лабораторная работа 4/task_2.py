# TODO импортировать необходимые молули
import csv
import json


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    # TODO считать содержимое csv файла
    with open(INPUT_FILENAME, "r") as from_csv:
        data = csv.DictReader(from_csv)


        # TODO Сериализовать в файл с отступами равными 4
        with open(OUTPUT_FILENAME, "w") as to_json:
            result = []
            for row in data:
                result.append(row)
            json.dump(result, to_json, indent=4, ensure_ascii=True)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
