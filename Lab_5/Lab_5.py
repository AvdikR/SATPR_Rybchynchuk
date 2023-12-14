import numpy as np

# Задання матриці платежів
payoff_matrix = np.array([
    [1, 9, 6, 0],
    [-2, 3, 8, 4],
    [-5, -2, 10, -3],
    [7, 4, -2, -5]
])

# Знаходження нижньої та верхньої ціни гри
lower_price = np.min(payoff_matrix)
upper_price = np.max(payoff_matrix)

# Знаходження мінімакс для стовпчиків (максимум по мінімумам)
minimax_column = np.max(np.min(payoff_matrix, axis=0))

# Знаходження максмін для рядків (мінімум по максимумах)
maxmin_row = np.min(np.max(payoff_matrix, axis=1))

# Виведення результатів
print("Нижня ціна гри:", lower_price)
print("Верхня ціна гри:", upper_price)
print("Мінімакс для стовпчиків:", minimax_column)
print("Максмін для рядків:", maxmin_row)