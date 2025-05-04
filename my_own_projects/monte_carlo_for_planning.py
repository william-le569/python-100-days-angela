import random

def triangular_sample(low, mode, high):
    return random.triangular(low, high, mode)

success_count = 0
num_simulations = 10000

for _ in range(num_simulations):
    t1 = triangular_sample(2, 4, 6)
    t2 = triangular_sample(3, 5, 8)
    t3 = triangular_sample(1, 2, 3)
    total = t1 + t2 + t3

    if total <= 12:
        success_count += 1

probability = success_count / num_simulations
print(f"Estimated success probability: {probability:.2%}")