import sys
import csv


def get_cell_value(file_path, row, column):
    try:
        with open(file_path, newline='') as csvfile:
            csv_reader = csv.reader(csvfile)
            data = list(csv_reader)
            if 0 <= row < len(data) and 0 <= column < len(data[0]):
                cell_value = data[row][column]
                return cell_value
            else:
                return "Такой столбец и строка не найдены."
    except FileNotFoundError:
        return "Файл не найден."


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Необходимо ввести в формате: python task.py .\example.csv <row_number> <column_number>")
    else:
        file_path = sys.argv[1]
        row_number = int(sys.argv[2])
        column_number = int(sys.argv[3])

        cell_value = get_cell_value(file_path, row_number, column_number)
        print(cell_value)
