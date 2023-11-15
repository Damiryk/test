# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=',')
        reader = list(reader)
    # TODO считать содержимое csv файла

    with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as output_f:
        json.dump(reader, output_f, indent=4)
    # TODO Сериализовать в файл с отступами равными 4


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
