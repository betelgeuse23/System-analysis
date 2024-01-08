import csv
import sys
from io import StringIO

def read_csv(csv_string):
    reader = csv.reader(StringIO(csv_string))
    return list(reader)

def build_matrix(csv_string):
    matrix = {}

    csv_data = read_csv(csv_string)

    for row in csv_data:
        node1, node2 = row

        if node1 not in matrix:
            matrix[node1] = []
        if node2 not in matrix:
            matrix[node2] = []

        matrix[node1].append(node2)

    matrix = dict(sorted(matrix.items()))
    return matrix

def calculate_metrics(matrix):
    result = {}

    for node in matrix:
        result[node] = {"r1": 0, "r2": 0, "r3": 0, "r4": 0, "r5": 0}

    def rec(node):
        i = 1
        for n in matrix[node]:
            result[n]["r4"] += 1
            i += rec(n)
        return i

    for node in matrix:
        result[node]["r1"] += len(matrix[node])
        for n in matrix[node]:
            result[n]["r2"] += 1
            result[n]["r5"] += len(matrix[node]) - 1
        result[node]["r3"] = rec(node) - result[node]["r1"] - 1
        result[node]["r4"] -= result[node]["r2"]

    return result

def generate_csv(result_metrics):
    output = StringIO()
    writer = csv.writer(output)

    for node, lengths in result_metrics.items():
        writer.writerow([lengths["r1"], lengths["r2"], lengths["r3"], lengths["r4"], lengths["r5"]])

    return output.getvalue()

def task(csv_string):
    matrix = build_matrix(csv_string)
    result_metrics = calculate_metrics(matrix)
    return generate_csv(result_metrics)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Необходимо ввести в формате: python task.py <csv_string>")
    else:
        csv_string = sys.argv[1]
        csv_string = csv_string.replace('\\n', '\n')
        result_csv = task(csv_string)
        print(result_csv)
        