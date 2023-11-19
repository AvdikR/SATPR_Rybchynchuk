from scipy.optimize import linear_sum_assignment

# Матриця вартостей для задачі про призначення
cost_matrix = [
    [46, 59, 24, 62, 67],
    [47, 56, 32, 55, 70],
    [44, 52, 19, 61, 60],
    [47, 59, 17, 64, 73],
    [43, 65, 20, 60, 75]
]

# Визначення імен програмістів та програм
programmers = ["P1", "P2", "P3", "P4", "P5"]
programs = ["p1", "p2", "p3", "p4", "p5"]

Min = 0

# Вирішення задачі про призначення
row_ind, col_ind = linear_sum_assignment(cost_matrix)

# Виведення матриці з написами
print("Таблиця оцінок (Програміст/програма):")
print("     " + "  ".join(programs))
for i in range(len(cost_matrix)):
    print(f"{programmers[i]}  {cost_matrix[i]}")

print("\nОптимальне призначення:")
for i in range(len(row_ind)):
    programmer_index = row_ind[i]
    program_index = col_ind[i]
    cost = cost_matrix[programmer_index][program_index]
    Min += cost
    print(f"{programmers[programmer_index]} -> {programs[program_index]} (вартість: {cost})")

print(f"\nМінімальне значення цільової функції: {Min}")