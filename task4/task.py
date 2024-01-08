import math
from collections import Counter

def calculate_probabilities(counts, total_outcomes):
    probabilities = {}
    for k, v in counts.items():
        probabilities[k] = v / total_outcomes
    return probabilities

def calculate_entropy(probabilities):
    return -sum(p * math.log2(p) for p in probabilities.values())

def task():
    outcomes = [(i, j) for i in range(1, 7) for j in range(1, 7)]

    sums = Counter(a+b for a, b in outcomes)
    products = Counter(a*b for a, b in outcomes)
    
    total_outcomes = len(outcomes)
    
    prob_sums = calculate_probabilities(sums, total_outcomes)
    prob_products = calculate_probabilities(products, total_outcomes)

    joint_probs = Counter((a+b, a*b) for a, b in outcomes)
    prob_joint = calculate_probabilities(joint_probs, total_outcomes)

    H_A = calculate_entropy(prob_sums)
    H_B = calculate_entropy(prob_products)
    H_AB = calculate_entropy(prob_joint)
    HA_B = H_AB - H_A
    I_AB = H_A + H_B - H_AB

    return [round(H_AB, 2), round(H_A, 2), round(H_B, 2), round(HA_B, 2), round(I_AB, 2)]

if __name__ == "__main__":
    result = task()
    print(result)