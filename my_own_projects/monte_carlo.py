import numpy as np
import matplotlib.pyplot as plt

# Số lần mô phỏng
n_simulations = 10000

# Các tham số
projects = {
    "A": {"mean": 0.08, "std": 0.05},
    "B": {"mean": 0.12, "std": 0.10},
    "C": {"mean": 0.06, "std": 0.02}
}

# Ngưỡng lợi nhuận mong muốn
threshold = 0.10

# Lưu kết quả
results = {}

for name, params in projects.items():
    returns = np.random.normal(loc=params["mean"], scale=params["std"], size=n_simulations)
    prob_success = np.mean(returns > threshold)
    results[name] = prob_success
    print(f"Dự án {name}: Xác suất lợi nhuận > {threshold*100:.0f}% là {prob_success:.2%}")

# Vẽ biểu đồ so sánh
plt.bar(results.keys(), results.values(), color=["skyblue", "lightgreen", "salmon"])
plt.ylabel("Xác suất đạt lợi nhuận > 10%")
plt.title("So sánh xác suất thành công giữa các dự án")
plt.ylim(0, 1)
plt.grid(True, axis='y', linestyle='--', alpha=0.7)
plt.show()