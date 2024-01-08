import json
import sys
import numpy as np

def create_table(data, mapping=None):
    a, length = {}, -1
    if mapping is None:
        mapping, length = {}, 0
    for i, cl in enumerate(data):
        if isinstance(cl, int):
            cl = [cl]
        a.update({e: i for e in cl})
        if length != -1:
            mapping.update({length + i: e for i,e in enumerate(cl)})
            length += len(cl)
                    
    length = len(mapping)
    table = np.zeros((length, length))

    for i in range(length):
        for j in range(length):
            if a[mapping[j]] <= a[mapping[i]]:
                table[j,i] = 1

    return table, mapping

def task(a_data, b_data):
    table_a, mapping = create_table(a_data)
    table_b, mapping = create_table(b_data, mapping)

    table_a, table_b = np.array(table_a), np.array(table_b)
    intersection = np.logical_and(table_a, table_b)
    transposed_intersection = np.logical_and(table_a.T, table_b.T)

    non_intersecting = []
    for i in range(len(table_a)):
        for j in range(len(table_a)):
            if not (intersection[i, j] or transposed_intersection[i, j]):
                non_intersecting.append((i, j))

    pairs = [[mapping[i], mapping[j]] for i, j in non_intersecting]

    merged = []
    for pair in pairs:
        for group in merged:
            if set(pair) & set(group):
                group.update(pair)
                break
        else:
            merged.append(set(pair))

    controversy = [list(set(group)) for group in merged]
    result, visited = [], set()

    for value in mapping.values():
        if value not in visited:
            cluster = {value}
            visited.add(value)

            for controversial in controversy:
                if value in controversial:
                    cluster.update(controversial)
                    visited.update(controversial)

            result.append(list(cluster) if len(cluster) > 1 else cluster.pop())

    return result

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Необходимо ввести в формате: python task.py <json_string> <json_string>")
    else:
        a_data = json.loads(sys.argv[1])
        b_data = json.loads(sys.argv[2])
        result = task(a_data, b_data)
        print(result)