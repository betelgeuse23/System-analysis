import csv
import sys
import math
from io import StringIO

def calculate_entropy(matrix):
    length = len(matrix)
    entropy = 0

    for row in matrix:
        for cell in row:
            if cell != '0':
                d = float(cell) / (length - 1)
                entropy -= d * math.log2(d)

    return round(entropy, 1)

def read_csv(csv_string):
    reader = csv.reader(StringIO(csv_string))
    return list(reader)

def task(csv_string):
    csv_string = csv_string.replace('\\n', '\n')
    matrix = read_csv(csv_string)
    result_entropy = calculate_entropy(matrix)
    return result_entropy

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Необходимо ввести в формате: python task.py <csv_string>")
    else:
        csv_string = sys.argv[1]
        result_entropy = task(csv_string)
        print(result_entropy)