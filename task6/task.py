import json
import sys
import numpy as np

def task(a_data, b_data):
    element_to_index = {}
    index = 1
    for cluster in a_data:
        if isinstance(cluster, list):
            for element in cluster:
                element_to_index[element] = index
        else:
            element_to_index[cluster] = index
        index += 1

    indices_list = []
    for dataset in [a_data, b_data]:
        indices = []
        for group in dataset:
            if isinstance(group, list):
                for item in group:
                    indices.append(element_to_index[item])
            else:
                indices.append(element_to_index[group])
        indices_list.append(indices)

    return round(calculate_metric(indices_list), 2)

def calculate_metric(data):
    length = len(data[0])
    x_max = np.arange(1, length + 1) * len(data)
    d_max = np.sum((x_max - np.mean(x_max))**2) / (length - 1)

    x = np.sum(np.array(data).T, axis=1)
    d = np.sum((x - np.mean(x_max))**2) / (length - 1)
    
    return d / d_max

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Необходимо ввести в формате: python task.py <json_string> <json_string>")
    else:
        a_data = json.loads(sys.argv[1])
        b_data = json.loads(sys.argv[2])
        result = task(a_data, b_data)
        print(result)